---
authors:
- Matt Brigida
doc_id: arxiv:2510.07671v1
family_id: arxiv:2510.07671
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Time-Varying Volatility of Bank Betas
url_abs: http://arxiv.org/abs/2510.07671v1
url_html: https://arxiv.org/html/2510.07671v1
venue: arXiv q-fin
version: 1
year: 2025
---


Matt Brigida
SUNY Polytechnic Institute, 100 Seymour Rd, Utica NY 13502. Email: matthew.brigida@sunypoly.edu

(October 9, 2025)

###### Abstract

Research has shown banks match interest income and expense betas, and thereby obtain net interest income margins which are insensitive to changes in short-term interest rates. The present analysis extends this research in a number of ways. First, we use state-space methods to estimate time-varying betas and test whether they are matched at each time interval. We find substantial variation in interest income and expense betas, which drives variation in net interest margin beta coefficients. Second, we estimate the time-varying conditional volatility of beta forecasts—the uncertainty of future beta values. We find uncertainty in interest expense beta coefficients drives uncertainty in interest income betas. Further, large banks have greater expense beta uncertainty, whereas small banks have greater income beta uncertainty. Lastly, we find evidence that uncertainty in interest expense betas is priced by the market, and is negatively related to bank stock prices. This is a new and previously unmeasured source of unhedgeable risk in bank stocks, and highlights an additional benefit of the Federal Reserve’s Zero Interest Rate Policy.

*JEL Codes*: E02; E60; F02; F35; G28

Keywords: Bank Interest and Expense; Interest Rate Risk; Net Interest Margins; Time-Varying Parameters

## 1 Introduction

Recent research has found evidence that banks hedge interest rate risk by matching the sensitivities of interest income and expense to changes in short-term interest rates ([[8](https://arxiv.org/html/2510.07671v1#bib.bibx8)]). The result is that net interest margins are insensitive to interest rate changes. Banks are able to do this through a *deposit franchise* which acts like long-term debt rather than the short rate. That is, the deposit franchise allows banks to maintain interest expense betas which behave similarly to interest income betas. Therefore, in the presence of a deposit franchise, maturity transformation does not cause interest rate risk.

[[8](https://arxiv.org/html/2510.07671v1#bib.bibx8)] estimate static interest income and expense beta coefficients over their entire sample. There is, however, expected to be substantial variation in interest income betas throughout the period given the sensitivity of duration to the coupon rate and yield. This raises the question of whether banks are able to match interest income and expense betas over time. Further, the extent to which the betas are matched does not measure a bank’s *uncertainty about whether they will be matched*. This uncertainty is a yet unmeasured source of bank risk.

Thus matching interest income and expense betas is likely to be done continually. Banks forecast future interest income and expense betas and then adjust their balance sheet to attempt to lessen any difference. Then banks reforecast betas and adjust their balance sheet in a continual dynamic matching strategy. A natural model of this process is the Kalman filter, which models a rational market participant which updates forecasts of estimated coefficients in a Bayesian manner as new information arrives in an uncertain environment ([[16](https://arxiv.org/html/2510.07671v1#bib.bibx16)]).

In a similar state-space analysis [[3](https://arxiv.org/html/2510.07671v1#bib.bibx3)] found large banks tend to match income and expense betas at the annual frequency (which may be too infrequently sampled to detect a lead-lag relationship). Additionally, in their analysis bank betas were calculated using interest income and expense in levels rather than changes. Importantly, they also only considered the point estimate of the deposit beta and ignored the uncertainty in the beta estimate.

Our analysis makes a number of contributions. First, we show that while banks match interest income and expense betas over time, there is substantial variation in these betas. Moreover, we find evidence that interest expense betas drive interest income betas. Second, we estimate the time-varying conditional volatility of beta forecasts, which measures the uncertainty of future beta values. We find uncertainty in interest expense beta coefficients Granger causes uncertainty in interest income betas. Lastly, we find evidence that uncertainty in interest expense betas is priced by the market, and is negatively related to bank stock prices. This is a new and previously unmeasured source of unhedgeable risk in bank stocks.

This uncertainty about beta values peaked during the 2008 financial crisis, and the 2023 regional banking crisis. There was also substantial uncertainty prior to the 2008 financial crisis, however very low uncertainty during the post-2008 crisis period which was driven by the Federal Reserve’s zero interest rate policy. This latter point shows an additional channel by which the Fed’s ZIRP policy was supportive of the banking sector—low beta uncertainty raises bank equity values.

[[8](https://arxiv.org/html/2510.07671v1#bib.bibx8)] found banks can hedge interest rate risk by matching interest income and expense betas. However our results show that this method of hedging is dynamic, and banks constantly have to match interest income betas to interest expense betas. This matching process introduces a risk that at a given point the betas will not be matched, and an uncertainty about the ability to match the betas in the future. Therefore, the ability to hedge interest rate risk is limited through matching betas is limited, and more of an active process than previous research made it seem.

Our analysis contributes to knowledge on the relationship between interest rate changes and bank profitability. [[12](https://arxiv.org/html/2510.07671v1#bib.bibx12)] and [[13](https://arxiv.org/html/2510.07671v1#bib.bibx13)] find bank profits have little exposure to interest rate changes, however using a data set spanning 10 countries [[10](https://arxiv.org/html/2510.07671v1#bib.bibx10)] finds interest rate changes have a mixed effect on bank profitability. [[18](https://arxiv.org/html/2510.07671v1#bib.bibx18)] highlights the use of interest rate derivatives to decouple bank lending policy from interest rate shocks.

A separate set of research has focused on the effect of interest rate changes on bank equity. [[11](https://arxiv.org/html/2510.07671v1#bib.bibx11)] find evidence that shocks to interest rates do affect bank equity levels, however the effect on banks is only marginally greater than the effect on all firms. [[1](https://arxiv.org/html/2510.07671v1#bib.bibx1)] and [[2](https://arxiv.org/html/2510.07671v1#bib.bibx2)], however, find evidence that bank balance sheets are significantly exposed to interest rate shocks.

In addition to recent research on matching interest and expense betas ([[8](https://arxiv.org/html/2510.07671v1#bib.bibx8)]), bank deposit betas are widely used in academic research on bank market power ([[7](https://arxiv.org/html/2510.07671v1#bib.bibx7)]). Bank betas are also extensively used in industry and by regulators such as the Federal Reserve Board of Governors ([[17](https://arxiv.org/html/2510.07671v1#bib.bibx17)]).

Our analysis also contributes to research on the relationship between deposits and policy rate increases. [[14](https://arxiv.org/html/2510.07671v1#bib.bibx14)] find as short-term rates rise, depositors tend to shift to time deposits from savings accounts and similar products. Moreover, the when bank deposit rates do not increase in kind with short-term interest rates, some depositors switch to money market funds ([[20](https://arxiv.org/html/2510.07671v1#bib.bibx20)]). Thus we can expect interest expense betas to rise when interest rates rise.

The remainder of the paper is organized as follows. Section 2 outlines our dataset and empirical methods. Section 3 discusses our results and section 4 concludes.

## 2 Data and Methods

Our dataset is built from a database of FDIC Call reports and ranges from October 1992 to June 2024. We collect total interest income to assets (FDIC BankFind code: *INTINCY*), expense to assets (*EINTEXP*111This is variable a cumulative annual interest expense, which we difference to obtain the quarterly interest expense.), and assets for each bank over each quarter. Federal funds rate data is obtained from the St Louis Federal Reserve Bank’s FRED Database.

We analyze bank deciles separately to control for variation in NIM and bank performance driven by bank size. Nonetheless there is substantial heterogeneity among banks within each decile due to the priorities of each bank’s operations. For example, banks’ focusing on credit card operations have a much higher NIM than custody and investment banks. Regional banks typically have a NIM in between these extremes.

### 2.1 Empirical Methods

We first estimate constant coefficient regressions, and then test these for parameter instability. If we can reject constant coefficients, this motivates estimating our interest income and expense betas as time-varying parameters vie state-space methods. Further, this latter method affords estimates of beta conditional volatility. The following subsections describe each empirical method.

#### 2.1.1 Constant Regression Coefficients

To calculate the interest income beta we estimate the parameters of the following time-series regression for each decile *d*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​I​n​t​I​n​cd​t=αdI​n​c+βd,0I​n​c​Δ​F​e​d​F​u​n​d​st+βd,1I​n​c​Δ​F​e​d​F​u​n​d​st−1+ϵd​t\Delta IntInc\_{dt}=\alpha^{Inc}\_{d}+\beta^{Inc}\_{d,0}\Delta FedFunds\_{t}+\beta^{Inc}\_{d,1}\Delta FedFunds\_{t-1}+\epsilon\_{dt} |  | (1) |

and we report:

|  |  |  |
| --- | --- | --- |
|  | βdI​n​c=βd,0I​n​c+βd,1I​n​c\beta^{Inc}\_{d}=\beta^{Inc}\_{d,0}+\beta^{Inc}\_{d,1} |  |

for each decile *d*.

We calculate interest expense betas in the same fashion.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​I​n​t​E​x​pd​t=αdE​x​p+βd,0E​x​p​Δ​F​e​d​F​u​n​d​st+βd,1E​x​p​Δ​F​e​d​F​u​n​d​st−1+ϵd​t\Delta IntExp\_{dt}=\alpha^{Exp}\_{d}+\beta^{Exp}\_{d,0}\Delta FedFunds\_{t}+\beta^{Exp}\_{d,1}\Delta FedFunds\_{t-1}+\epsilon\_{dt} |  | (2) |

and we report:

|  |  |  |
| --- | --- | --- |
|  | βdE​x​p=βd,0E​x​p+βd,1E​x​p\beta^{Exp}\_{d}=\beta^{Exp}\_{d,0}+\beta^{Exp}\_{d,1} |  |

for each decile *d*.

Once we have these income and expense beta coefficients for each decile, we can calculate the NIM beta by decile with:

|  |  |  |
| --- | --- | --- |
|  | βdN​I​M=βdI​n​c−βdE​x​p\beta^{NIM}\_{d}=\beta^{Inc}\_{d}-\beta^{Exp}\_{d} |  |

#### 2.1.2 Test for Non-Constant Coefficients

Once we estimate interest expense and interest income beta coefficients, we then test for constant coefficients with the [[4](https://arxiv.org/html/2510.07671v1#bib.bibx4)] test. We use the [[4](https://arxiv.org/html/2510.07671v1#bib.bibx4)] test for a number of reasons. First, we expect the coefficients to change smoothly through time, rather than discretely (in which case either a [[5](https://arxiv.org/html/2510.07671v1#bib.bibx5)] or [[19](https://arxiv.org/html/2510.07671v1#bib.bibx19)] test would be appropriate). Second, given time-varying coefficients are potentially driven by changes in the underlying interest rates, coefficients which change according to a random walk is appropriate.

#### 2.1.3 Time-Varying Beta Estimates

Allowing the parameters of our interest income and expense equations to vary over time affords:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​I​n​t​I​n​cd​t=αd,t+βd,0,tI​n​c​Δ​F​e​d​F​u​n​d​st+βd,1,tI​n​c​Δ​F​e​d​F​u​n​d​st−1+ϵd​t\Delta IntInc\_{dt}=\alpha\_{d,t}+\beta^{Inc}\_{d,0,t}\Delta FedFunds\_{t}+\beta^{Inc}\_{d,1,t}\Delta FedFunds\_{t-1}+\epsilon\_{dt} |  | (3) |

where coefficients take the form of a random walk:

|  |  |  |
| --- | --- | --- |
|  | αd,tI​n​c=μ1+γ1​αd,t−1I​n​c+ν1,t\alpha^{Inc}\_{d,t}=\mu\_{1}+\gamma\_{1}\alpha^{Inc}\_{d,t-1}+\nu\_{1,t} |  |

|  |  |  |
| --- | --- | --- |
|  | βd,0,tI​n​c=μ2+γ2​βd,0,t−1I​n​c+ν2,t\beta^{Inc}\_{d,0,t}=\mu\_{2}+\gamma\_{2}\beta^{Inc}\_{d,0,t-1}+\nu\_{2,t} |  |

|  |  |  |
| --- | --- | --- |
|  | βd,1,tI​n​c=μ3+γ3​βd,1,t−1I​n​c+ν3,t\beta^{Inc}\_{d,1,t}=\mu\_{3}+\gamma\_{3}\beta^{Inc}\_{d,1,t-1}+\nu\_{3,t} |  |

|  |  |  |
| --- | --- | --- |
|  | ϵt∼i.i.d.N​(0,R)\epsilon\_{t}\sim i.i.d.N(0,R) |  |

|  |  |  |
| --- | --- | --- |
|  | νt∼i.i.d.N​(0,Q)\nu\_{t}\sim i.i.d.N(0,Q) |  |

|  |  |  |
| --- | --- | --- |
|  | E​(ϵt,νt′)=0E(\epsilon\_{t},\nu^{\prime}\_{t})=0 |  |

and Δ​I​n​t​I​n​cd​t\Delta IntInc\_{dt} is the quarterly change interest income for decile dd at time tt and Δ​F​e​d​F​u​n​d​st\Delta FedFunds\_{t} is the quarterly change in the Federal Funds rate at time tt. βd,0,tI​n​c\beta^{Inc}\_{d,0,t} is the time-varying coefficient on the contemporaneous Federal Funds rate change for decile dd at time tt, and βd,1,tI​n​c\beta^{Inc}\_{d,1,t} is the coefficient on the Federal Funds rate change lagged one quarter.

The structural form of the time-varying regression coefficients is a random walk. This form is suggested by [[9](https://arxiv.org/html/2510.07671v1#bib.bibx9)] for cases where market participants modify their estimate of the state solely on the arrival of new information. In addition, [[6](https://arxiv.org/html/2510.07671v1#bib.bibx6)] found that random walk coefficients quickly learn changes in the relationship between model variables.

#### 2.1.4 Conditional Volatility

In addition to time-varying-parameter coefficients, our model also affords an estimate of conditional volatility through the conditional variance of forecast errors from the Kalman filter (see [[15](https://arxiv.org/html/2510.07671v1#bib.bibx15)]). Specifically, we estimate the conditional variance as Ht|t−1=xt−1​Pt|t−1​xt−1′+σe2H\_{t|t-1}=x\_{t-1}P\_{t|t-1}x^{\prime}\_{t-1}+\sigma^{2}\_{e} where xt−1x\_{t-1} is the vector of the change in the Federal Funds rate and its lag, Pt|t−1P\_{t|t-1} is the variance-covariance matrix of βt\beta\_{t} conditional on information available at time t−1t-1 (βt|t−1\beta\_{t|t-1}), and σe2\sigma^{2}\_{e} is the variance of the disturbance term.

## 3 Results

Results are summarized in sections 3.1 through 3.4. Section 3.1 summarizes the constant coefficient estimates, as well as the tests for time-varying coefficients. Section 3.2 discusses the results from the state-space formulation with time varying interest expense and income beta coefficients, and also provides results of Granger causality between interest expense and income coefficients. Section 3.3 provides estimates of time-varying interest income and expense beta conditional volatility, as well as test of Granger causality between interest income and expense volatilities. Section 3.3 also contains tests of whether this conditional volatility is priced by market participants.

### 3.1 Constant Coefficient Regressions

Results from constant coefficient regressions are in table 1 below. Over our sample period, and every decile, we estimate bank interest expense is slightly more sensitive to the short rate than bank income. This results in a estimated inverse correlation between the short rate and bank net interest margin.

As bank size increases, the sensitivity of interest expense to the short rate also increases (from 0.1966 in the smallest banks to 0.3423 at the largest). This is consistent with smaller banks relying on a deposit franchise for funding, while larger banks rely more on capital markets and wholesale deposits which are more sensitive to short rate changes. Since interest income betas are much more uniform across bank size, NIM betas are lower for larger banks.

Table 1: Interest income, expense and NIM beta estimated from constant coefficient regressions. Data are quarterly and range from October 1992 to June 2024.

| Decile | Interest Income Beta | Interest Expense Beta | NIM Beta |
| --- | --- | --- | --- |
| 1 | 0.09143 | 0.1966 | -0.10517 |
| 2 | 0.09294 | 0.2212 | -0.12826 |
| 3 | 0.09576 | 0.2396 | -0.14384 |
| 4 | 0.10307 | 0.2471 | -0.14403 |
| 5 | 0.10133 | 0.2587 | -0.15737 |
| 6 | 0.10187 | 0.2624 | -0.16053 |
| 7 | 0.10519 | 0.2769 | -0.17171 |
| 8 | 0.10974 | 0.2796 | -0.16986 |
| 9 | 0.11214 | 0.2993 | -0.18716 |
| 10 | 0.12661 | 0.3423 | -0.21569 |

*Tests for Time-Varying Coefficients*

Applying the [[4](https://arxiv.org/html/2510.07671v1#bib.bibx4)] we are able to reject the null of constant coefficients over all deciles. This evidence motivates the estimation of time-varying coefficients, which vary according to a random walk.

### 3.2 Time-Varying Coefficients

Plots of time-varying beta coefficients be decile are in figures 1, 2, and 3 below. Figures 4, 5, and 6 show histograms of the time-varying beta coefficients by decile. Interest income betas typically range between -0.2 and 0.4, though the range differs by decile. Augmented Dickey-Fuller tests on all time-varying beta coefficient series reject the null, which is evidence the beta coefficient series do not contain a unit root.

![Refer to caption](x1.png)


Figure 1: Time-Varying Interest Income Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x2.png)


Figure 2: Time-Varying Interest Expense Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x3.png)


Figure 3: Time-Varying Net Interest Margin Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x4.png)


Figure 4: Histograms of Time-Varying Interest Income Beta be decile. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x5.png)


Figure 5: Histograms of Time-Varying Interest Expense Beta be decile. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x6.png)


Figure 6: Histograms of Time-Varying NIM Beta be decile. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

#### 3.2.1 Granger Causality

Table 2 below provides results from Granger causality tests on time-varying interest expense and income beta coefficients. We find some evidence (at the 10% level of significance) over 4 of 10 deciles that interest expense beta coefficients Granger cause interest income betas. This is consistent with interest expense sensitivities being driven by exogenous shocks, such as Federal Finds rate changes, and interest income betas being changed to match the expense betas. There is no evidence of interest income betas Granger causing expense betas.

Table 2: Granger Causality tests. Beta coefficient are in levels and are quarterly ranging from October 1992 to June 2024. Granger causality results are from the SSR based F-test with 4 lagged quarters.

| Decile | βi​i⇒βi​e\beta\_{ii}\Rightarrow\beta\_{ie} | βi​e⇒βi​i\beta\_{ie}\Rightarrow\beta\_{ii} |
| --- | --- | --- |
| 1 | 0.3532 | 1.7442 |
|  | (0.8413) | (0.1453) |
| 2 | 0.3757 | 1.4759 |
|  | (0.8256) | (0.2143) |
| 3 | 0.4705 | 0.1336 |
|  | (0.7573) | (0.9697) |
| 4 | 1.0544 | 2.2982 |
|  | (0.3827) | (0.0634)∗ |
| 5 | 1.0130 | 0.7629 |
|  | (0.4039) | (0.5516) |
| 6 | 0.4154 | 1.1725 |
|  | (0.7972) | (0.3269) |
| 7 | 0.4006 | 2.0748 |
|  | (0.8078) | (0.0889)∗ |
| 8 | 1.3051 | 2.0697 |
|  | (0.2725) | (0.0896)∗ |
| 9 | 0.1652 | 2.1506 |
|  | (0.9556) | (0.0793)∗ |
| 10 | 0.1788 | 0.8444 |
|  | (0.9489) | (0.4999) |

### 3.3 Conditional Volatility

Plots of the conditional volatility of interest income and expense are in figures 7 and 8 below. Notably, across deciles, there are peaks in volatility at the 2008 crisis, and the 2023 regional bank crisis. There is also a smaller increase in volatility around the 2000 technology bubble crash. Interestingly, volatility was lowest during the post-2008 crisis period, which was dominated by the zero interest rate policy and quantitative easing.

Interest expense beta uncertainty generally peaks a year after interest income beta uncertainty. This may be because going into a crisis a bank becomes uncertain about how sensitive their income will be to interest rates, whereas coming out of the crisis banks are uncertain how sensitive their expenses will be to interest rates.

![Refer to caption](x7.png)


Figure 7: Time-Varying Conditional Volatility of the Interest Income Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x8.png)


Figure 8: Time-Varying Conditional Volatility of the Interest Expense Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x9.png)


Figure 9: Time-Varying Conditional Volatility of the Interest Income Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

![Refer to caption](x10.png)


Figure 10: Time-Varying Conditional Volatility of the Interest Expense Beta. The beta was estimated over the sample of quarterly data from October 1992 to June 2024.

#### 3.3.1 Large vs Small Bank Conditional Volatility

Figure 9 and 10 show an interesting relationship between bank size and interest income and expense conditional volatility. Figure 9 shows smaller banks have much higher interest income beta uncertainty relative large banks. Conversely, figure 10 shows larger banks have much higher levels of interest expense beta uncertainty relative to small banks.

These figures also show notable peaks prior to the 2008 financial crisis and the 2023 regional banking crisis. Also, volatility was generally higher prior to the 2008 financial crisis, however was exceptionally low and stable in the aftermath of the crisis. This may be due to the Federal Reserves zero interest rate policy. Descriptive statistics for interest income and expense beta volatility are in tables 3 and 4 below.

These results are consistent with smaller banks relying on a strong deposit franchise to keep expenses low. That is, the profit strategy of small banks is to control interest expense. This is sensible given their assets are generally mortgage loans and banks have little pricing power on mortgage rates. Large banks, however, rely less on low funding rates and more on income generated through credit card, investment banking, and other higher margin sources.

Table 3: Descriptive Statistics: Interest income beta conditional volatility by decile. There are 125 quarters.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean | 0.0700 | 0.0958 | 0.0882 | 0.0585 | 0.0443 | 0.0570 | 0.0808 | 0.0352 | 0.0464 | 0.0546 |
| std | 0.0605 | 0.1163 | 0.1004 | 0.0480 | 0.0479 | 0.0483 | 0.0399 | 0.0397 | 0.0418 | 0.0555 |
| min | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 25% | 0.0322 | 0.0152 | 0.0165 | 0.0280 | 0.0111 | 0.0212 | 0.0560 | 0.0080 | 0.0207 | 0.0123 |
| 50% | 0.0468 | 0.0445 | 0.0574 | 0.0395 | 0.0235 | 0.0421 | 0.0662 | 0.0169 | 0.0278 | 0.0375 |
| 75% | 0.0800 | 0.1312 | 0.1147 | 0.0629 | 0.0578 | 0.0741 | 0.0872 | 0.0470 | 0.0522 | 0.0694 |
| max | 0.3316 | 0.5407 | 0.4960 | 0.2568 | 0.2305 | 0.2489 | 0.2548 | 0.1838 | 0.2153 | 0.2773 |




Table 4: Descriptive Statistics: Interest expense beta conditional volatility by decile. There are 125 quarters.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean | 0.0566 | 0.0607 | 0.0539 | 0.0559 | 0.0465 | 0.0702 | 0.0775 | 0.0736 | 0.0649 | 0.0507 |
| std | 0.0408 | 0.0233 | 0.0355 | 0.0266 | 0.0222 | 0.0609 | 0.0676 | 0.0537 | 0.0444 | 0.0286 |
| min | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 25% | 0.0304 | 0.0467 | 0.0324 | 0.0396 | 0.0342 | 0.0326 | 0.0347 | 0.0346 | 0.0366 | 0.0323 |
| 50% | 0.0415 | 0.0518 | 0.0416 | 0.0459 | 0.0392 | 0.0470 | 0.0532 | 0.0547 | 0.0492 | 0.0401 |
| 75% | 0.0621 | 0.0655 | 0.0583 | 0.0619 | 0.0509 | 0.0787 | 0.0906 | 0.0886 | 0.0742 | 0.0583 |
| max | 0.2354 | 0.1857 | 0.2093 | 0.1840 | 0.1820 | 0.3590 | 0.4040 | 0.2683 | 0.2531 | 0.1812 |

#### 3.3.2 Tests of Conditional Volatility Granger Causality

Table 3 reports Granger Causality results between interest income and expense beta conditional volatilities. We find evidence of bi-directional (or mutual) Granger causality between interest expense beta conditional volatility and that of interest income. Over every decile interest expense beta volatility Granger causes interest income, and over all but 3 deciles interest income Granger causes interest expense. The interpretation of these results is that either series will help predict the other series, however this evidence is consistent with uncertainty in one variable causing uncertainty in the other as banks try and match these two betas.

Table 5: Granger Causality tests. The volatility series are in levels and are quarterly ranging from October 1992 to June 2024. Granger causality results are from the SSR based F-test with 4 lagged quarters.

| Decile | Hi​i⇒Hi​e\sqrt{H\_{ii}}\Rightarrow\sqrt{H\_{ie}} | Hi​e⇒Hi​i\sqrt{H\_{ie}}\Rightarrow\sqrt{H\_{ii}} |
| --- | --- | --- |
| 1 | 495.5744 | 8.1844 |
|  | (0.0000)∗∗∗∗ | (0.0000)∗∗∗∗ |
| 2 | 0.9632 | 61.1280 |
|  | (0.4307) | (0.0000)∗∗∗∗ |
| 3 | 30.3265 | 15.5039 |
|  | (0.0000)∗∗∗∗ | (0.0000)∗∗∗∗ |
| 4 | 1.7093 | 6.2638 |
|  | (0.1530) | (0.0001)∗∗∗∗ |
| 5 | 0.8505 | 2.3117 |
|  | (0.4962) | (0.0621)∗ |
| 6 | 58.5093 | 40.0344 |
|  | (0.0000)∗∗∗∗ | (0.0000)∗∗∗∗ |
| 7 | 3.5682 | 2.7466 |
|  | (0.0089)∗∗∗ | (0.0319)∗∗ |
| 8 | 9.8772 | 18.9940 |
|  | (0.0000)∗∗∗∗ | (0.0000)∗∗∗∗ |
| 9 | 2.4967 | 4.1224 |
|  | (0.0468)∗∗ | (0.0038)∗∗∗ |
| 10 | 5.0288 | 97.6406 |
|  | (0.0009)∗∗∗∗ | (0.0000)∗∗∗∗ |

#### 3.3.3 The Market Price of Beta Uncertainty

A natural question is whether market participants incorporate interest income and expense beta uncertainty into bank stock prices. If so, we should expect stock prices to decline when uncertainty rises. To begin to answer this question we estimate the following regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rX​L​F,t=γ0+γ1​Δ​C​VE​x​p,t+γ2​Δ​C​VI​n​c,t+γ3​rM,t+ξtr\_{XLF,t}=\gamma\_{0}+\gamma\_{1}\Delta CV\_{Exp,t}+\gamma\_{2}\Delta CV\_{Inc,t}+\gamma\_{3}r\_{M,t}+\xi\_{t} |  | (4) |

where X​L​FXLF are returns on the market-capitalization-weighted Financial Select Sector SPDR Fund over quarter tt. C​VE​x​p,tCV\_{Exp,t} and C​VI​n​c,tCV\_{Inc,t} are quarterly interest expense and income beta conditional volatility for decile 10 over quarter tt. We use decile 10 because these banks dominate the market capitalization of X​L​FXLF. rM,tr\_{M,t} are quarterly returns on the SPDR S&P 500 ETF Trust (ticker S​P​YSPY). The parameters of the regression are estimated from the first quarter of 1999 to the first quarter of 2024.

Table 6: Estimated coefficients from estimating equation 4 above via OLS. Data are quarterly and range from Q1 1999 to Q1 2024.

| Parameter | Coefficient | value |
| --- | --- | --- |
| γ0\gamma\_{0} | -0.0063 | 0.3191 |
| γ1\gamma\_{1} | -1.1454 | 0.0006\*\*\*\* |
| γ2\gamma\_{2} | 0.0926 | 0.4705 |
| γ3\gamma\_{3} | 1.1078 | 0.0000\*\*\*\* |
| A​d​j.R2Adj.\ R^{2} | 0.7206 |  |

The coefficient on interest expense beta uncertainty is negative at significant at the 0.1% level. This is evidence that uncertainty regarding how interest expense will react to changes in the short rate is indeed priced by market participants. Further, the negative sign indicates as this uncertainty increases, bank stock returns decline. The standard deviation of the change in interest expense beta conditional volatility is 0.0205, and given our estimated coefficient on CV of -1.1454, this means if there is a one standard deviation increase in conditional beta volatility large bank market capitalizations will decline by 2.34%. Given the 10 largest banks have a collevtive market capitalization of approximately $2 trillion, a one standard deviation increase in interest expense beta uncertainty lowers the largest bank stocks by about $47 billion.

Interestingly, the coefficient on interest income uncertainty is insignificant. This is evidence that market participants react to uncertainty in how bank expenses will react to the short rate, though not how income will react to the short rate. Given we find greater evidence that interest expense beta uncertainty Granger cause interest income beta uncertainty than vice versa, it may be that the market is reacting to the first increase in uncertainty.

## 4 Conclusions

It was commonly assumed that by borrowing short-term and lending long-term, thereby creating a duration mismatch between their assets and liabilities, banks exposed themselves to substantial interest rate risk. Recent research, however, has shown banks match the sensitivities of their interest income and expense to the short rate, and so doing obtain net interest income margins which are generally insensitive to changes in short-term interest rates.

This matching of interest income and expense sensitivities (betas) is more likely to be a dynamic interest rate risk strategy, rather than static. As interest rate levels change, the duration of assets changes and so do the sensitivities of interest income to the short rate. Therefore, match must constantly adjust their assets and liabilities to match their sensitivities in the presence of a stochastic short rate. Consistent with this hypothesis, we find evidence for interest income and expense betas which vary according to a random walk, and weak evidence that interest expense betas may Granger cause interest income betas.

We also estimate the conditional volatility of our beta forecasts, which provides a number of interesting results. First, beta uncertainty increased markedly prior to the 2008 financial crisis and 2023 regional banking crisis. Also, from approximately 2009 to 2019 beta uncertainty became very low across deciles. This result highlights the role of the Federal Reserve’s zero interest rate policy in providing both low and predictable funding rates for banks. Interestingly, prior to each financial crisis, interest expense beta uncertainty rose most for large banks however interest income beta uncertainty rose most for small banks. This highlights the small bank reliance on their deposit franchise and the large bank focus on generating income. Consistent with results on the time-varying betas themselves, we find interest expense beta uncertainty Granger causes uncertainty in interest income betas. This result is consistent with shocks to interest expense betas being transferred to interest income betas.

Lastly, we find evidence that interest expense beta forecast uncertainty is priced by market participants. In particular, a one standard deviation increase in interest expense beta forecast uncertainty will reduce large bank stock values by 2.34%. This is a previously undocumented and unmeasured source of bank risk, and this risk is not hedgeable with current methods and instruments. Given the Federal Reserve’s zero interest rate policy significantly reduced interest expense beta uncertainty, we also document an additional avenue of post-2008-crisis support for large banks.

## References

* [1]
  Juliane Begenau, Monika Piazzesi and Martin Schneider
  “Banks’ Risk Exposures”
  In *National Bureau of Economic Research*, 2015
  DOI: [10.3386/w21334](https://dx.doi.org/10.3386/w21334)
* [2]
  Juliane Begenau and Erik Stafford
  “Do Banks Have an Edge?”
  In *SSRN Electronic Journal*
  Elsevier BV, 2018
  DOI: [10.2139/ssrn.3095550](https://dx.doi.org/10.2139/ssrn.3095550)
* [3]
  Matt Brigida and Kathleen Brigida
  “Time-variation in bank income and expense betas”
  In *Managerial Finance* 51.2
  Emerald Publishing Limited, 2025, pp. 206–215
* [4]
  Robert L Brown, James Durbin and James M Evans
  “Techniques for testing the constancy of regression
  relationships over time”
  In *Journal of the Royal Statistical Society Series B:
  Statistical Methodology* 37.2
  Oxford University Press, 1975, pp. 149–163
* [5]
  Gregory C Chow
  “Tests of equality between sets of coefficients in two linear
  regressions”
  In *Econometrica: Journal of the Econometric Society*
  JSTOR, 1960, pp. 591–605
* [6]
  Thomas Dangl and Michael Halling
  “Predictive regressions with time-varying coefficients”
  In *Journal of Financial Economics* 106.1
  Elsevier, 2012, pp. 157–181
* [7]
  Itamar Drechsler, Alexi Savov and Philipp Schnabl
  “The deposits channel of monetary policy”
  In *The Quarterly Journal of Economics* 132.4
  Oxford University Press, 2017, pp. 1819–1876
* [8]
  Itamar Drechsler, Alexi Savov and Philipp Schnabl
  “Banking on deposits: Maturity transformation without interest
  rate risk”
  In *The Journal of Finance* 76.3
  Wiley Online Library, 2021, pp. 1091–1143
* [9]
  Robert Fry Engle and Mark Wayne Watson
  “Applications of Kalman filtering in econometrics”
  Harvard University, 1985
* [10]
  William English
  “Interest rate risk and bank net interest margins”
  In *BIS Quarterly Review* 10, 2002, pp. 67–82
* [11]
  William B. English, Skander J. Heuvel and Egon Zakrajšek
  “Interest rate risk and bank equity valuations”
  In *Journal of Monetary Economics* 98
  Elsevier BV, 2018, pp. 80–97
  DOI: [10.1016/j.jmoneco.2018.04.010](https://dx.doi.org/10.1016/j.jmoneco.2018.04.010)
* [12]
  Mark J. Flannery
  “Market Interest Rates and Commercial Bank Profitability: An
  Empirical Investigation”
  In *The Journal of Finance* 36.5
  Wiley, 1981, pp. 1085–1101
  DOI: [10.1111/j.1540-6261.1981.tb01078.x](https://dx.doi.org/10.1111/j.1540-6261.1981.tb01078.x)
* [13]
  Mark J. Flannery
  “Interest Rates and Bank Profitability: Additional Evidence:
  Note”
  In *Journal of Money, Credit and Banking* 15.3
  JSTOR, 1983, pp. 355
  DOI: [10.2307/1992486](https://dx.doi.org/10.2307/1992486)
* [14]
  Emily Greenwald, Sam Schulhofer-Wohl and Josh Younger
  “Deposit Convexity, Monetary Policy and Financial Stability”
  In *FRB of Dallas Working Paper*, 2023
* [15]
  Chang-Jin Kim and Charles R. Nelson
  “The Time-Varying-Parameter Model for Modeling Changing
  Conditional Variance: The Case of the Lucas Hypothesis”
  In *Journal of Business and Economic Statistics* 7.4
  Informa UK Limited, 1989, pp. 433–440
  DOI: [10.1080/07350015.1989.10509755](https://dx.doi.org/10.1080/07350015.1989.10509755)
* [16]
  Chang-Jin Kim and Charles R Nelson
  “State-space models with regime switching: classical and
  Gibbs-sampling approaches with applications”
  MIT press, 2017
* [17]
  Lori Leu Kleymenova and Cindy M. Vojtech
  “Is This Time Different: How Are Banks Performing during the
  Recent Interest Rate Increases Compared to 2004-2006?”
  In *FEDS Notes. Washington: Board of Governors of the
  Federal Reserve System*, 2024
  URL: <https://doi.org/10.17016/2380-7172.3466.>
* [18]
  Amiyatosh Purnanandam
  “Interest rate derivatives at commercial banks: An empirical
  investigation”
  In *Journal of Monetary Economics* 54.6
  Elsevier BV, 2007, pp. 1769–1808
  DOI: [10.1016/j.jmoneco.2006.07.009](https://dx.doi.org/10.1016/j.jmoneco.2006.07.009)
* [19]
  Richard E Quandt
  “Tests of the hypothesis that a linear regression system obeys
  two separate regimes”
  In *Journal of the American statistical Association* 55.290
  Taylor & Francis, 1960, pp. 324–330
* [20]
  Kairong Xiao
  “Monetary transmission through shadow banks”
  In *The Review of Financial Studies* 33.6
  Oxford University Press, 2020, pp. 2379–2420