---
authors:
- Rem Sadykhov
- Geoff Goodell
- Philip Treleaven
doc_id: arxiv:2602.17373v1
family_id: arxiv:2602.17373
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Impacts of Economic Policies on Wealth Distribution in Token Economies How
  do endogenous and exogenous economic policies impact wealth distribution in token
  economies?
url_abs: http://arxiv.org/abs/2602.17373v1
url_html: https://arxiv.org/html/2602.17373v1
venue: arXiv q-fin
version: 1
year: 2026
---


R. Sadykhov


 Dr.G. Goodell and Prof.P. Treleaven

(January 2026)

In this paper, we analyse the impacts of exogenous and endogenous factors on wealth distribution in the Bitcoin token economy, where wealth distribution refers to the distribution of BTC between economic participants or groups of economic participants. The objective of the paper is to analyse the impact of economic policies on wealth distribution in the Bitcoin ecosystem.

Different macroeconomic and microeconomic time series are used to eliminate noise in the wealth distribution time series, and the causality analysis is performed between Bitcoin Improvement Proposals (i.e., BIPs) and the cleaned wealth distribution data to reveal possible patterns in the impacts that the endogenous policies have on wealth distribution in token economies. Lastly, a structure for economic policy taxonomy in token economies is proposed where different the policy implementations are illustrated by existing BIPs.

This approach highlights the actions available to the policy makers, as well as providing a technique for analysis of policy impacts in token economies and their categorization.

## 1 Introduction

Since the introduction of blockchain in 2008, token economies (as defined by Sadykhov et al. [[1](https://arxiv.org/html/2602.17373v1#bib.bib1)]) have become some of the most popular financial systems, and as their growth continues many wonder how can such decentralized economic mechanisms be regulated and what policies can financial regulators introduce to ensure that token economies are stable, comply with anti-money laundering and anti-terrorist funding schemes, and are taxable.

In order to understand what policies must be set, it is important first to evaluate what policies have an impact on token economies. The level at which the policies are applied should also be considered: would setting an administered interest rate for overnight repurchase agreements help to incentivize economic activity in a token economy, or does it require a specific incentive program to stimulate consumption? From this question, it is evident that there are different types of policies that can target a token economy and we would be referring to these as exogenous and endogenous policies.

Exogenous policies are the policies that are introduced outside of the token economy’s scope, and these policies are usually directed at the “global” state of an economy (e.g., setting a tax bounds for different income tax categories, issuing capital gains tax credit, etc.). In contrast, endogenous policies are the policies set inside of the token economy (e.g., maximum supply) and are directed purely at the economic activity inside it. Note, that we do not claim that every exogenous policy is unrellated to the state of a token economy, there can be policies that introduce a tax on realized income which is specific to a token economy, and vice versa, there can be endogenous policies whose impact spills over into the global economy.

From these definitions of exogenous and endogenous policies, we deduce that exogenous policies tend to have a much larger scope, and therefore, in order to study the effect of endogenous policies we somehow have to filter out the “noise” produced by the exogenous policies and by non-policy related events. Without this step we will not be able to determine whether the endogenous policy had an impact, was it implemented in response to something that has affected the token economy, or did not have any impact at all.

Finally, to conduct our research, we measure the policy impact using wealth distribution (i.e., distribution of wealth between buckets of Bitcoin addresses). The reason for this choice is because wealth distribution demonstrates the economic activity in an economy as economic activity is the redistribution of wealth in an economy. Also, wealth distribution is a great benchmark to see how policies impact different compartments of the population, as very often, policy makers target different agent categories [[1](https://arxiv.org/html/2602.17373v1#bib.bib1)] based on their wealth or income level.

With all of the above points, the aim of this paper is to examine how different exogenous and endogenous policies impact the wealth distribution in a token economy, and to develop a method for performing such analysis for a generic token economy. We also aim to map endogenous policies to their exogenous counterparts in the economic policy taxonomy.

## 2 Scope

In this paper we will perform analysis described above using the data from the Bitcoin token economy. The reason for this choice is the availability of high quality data on Bitcoin, and in particular the existence of Bitcoin Improvement Proposals [[7](https://arxiv.org/html/2602.17373v1#bib.bib7)] (i.e., BIPs). BIPs are organised into a repository of proposals submitted by Bitcoin community to improve the design of Bitcoin. These improvement proposals range from cybersecurity and performance improvements, to the design of Bitcoin’s economic mechanism. Not all BIPs will be relevant to the construction of economic policy taxonomy for token economies, but we still will use them in our analysis of wealth redistribution. Therefore, for all purposes we will be treating BIPs as the endogenous policies of the Bitcoin token economy.

The Bitcoin wealth distribution data that we use, along with the Bitcoin close price data, are taken from CCData [[8](https://arxiv.org/html/2602.17373v1#bib.bib8)]. The wealth distribution data is broken down into 10 buckets each of which is a sum of holdings of all addresses that satisfy that buckets’ bounds. For example, the bucket labelled *From 1 to 10* is a time series of a sum of all Bitcoin holdings that belong to addresses who hold between 1 and 10 Bitcoins at the given time.

First, note that the sum of all 10 buckets is nothing else but the time series of Bitcoin’s current supply. Second, the addresses in this buckets are not constrained to stay in the same bucket for the duration of the time series, and therefore, the number of addresses in each bucket can change in time just as well as the wealth of that bucket.

The software that we will use to perform the analysis is written in combination of Rust and Python programming languages, and the libraries used to analyse the data are DigiFi [[12](https://arxiv.org/html/2602.17373v1#bib.bib12)], Statsmodels [[13](https://arxiv.org/html/2602.17373v1#bib.bib13)], SciPy [[14](https://arxiv.org/html/2602.17373v1#bib.bib14)] and Numpy [[15](https://arxiv.org/html/2602.17373v1#bib.bib15)].

To perform the rest of our analysis, we need exogenous policies time series, macroeconomic and microeconomic data. The data in these three categories we see as the potential variables that may have a significant impact on wealth distribution, and therefore, we would like to check whether there is any noise accossiated with the time series that represent these categories. The time series used for the analysis are listed below.

### 2.1 Exogenous Policies Data

The exogenous policies are the policies that are set outside of scope of a token economy. To represent exogenous policies we use the time series defined below. Note that in brackets we place the source, time series identifier used by the source, measurement frequency, and the last date in the time series.

* •

  Federal Funds Effective Rate (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], DFF, Daily, 28-08-2025)
* •

  Personal Current Taxes (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], W055RC1, Monthly, 01-07-2025)
* •

  5-Year High Quality Market (HQM) Corporate Bond Par Yield (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], HQMCB5YRP, Monthly, 01-07-2025)
* •

  10-Year High Quality Market (HQM) Corporate Bond Par Yield (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], HQMCB10YRP, Monthly, 01-07-2025)
* •

  30-Year High Quality Market (HQM) Corporate Bond Par Yield (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], HQMCB30YRP, Monthly, 01-07-2025)
* •

  5-Year High Quality Market (HQM) Corporate Bond Spot Rate (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], HQMCB5YR, Monthy, 01-07-2025)
* •

  10-Year High Quality Market (HQM) Corporate Bond Spot Rate (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], HQMCB10YR, Monthly, 01-07-2025)
* •

  30-Year High Quality Market (HQM) Corporate Bond Spot Rate (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], HQMCB30YR, Monthly, 01-07-2025)
* •

  British Government Securities, Nominal Par Yields, 5 year (IADB [[10](https://arxiv.org/html/2602.17373v1#bib.bib10)], IUDSNPY, Daily, 29-08-2025)
* •

  British Government Securities, Nominal Par Yields, 10 year (IADB [[10](https://arxiv.org/html/2602.17373v1#bib.bib10)], IUDMNPY, Daily, 29-08-2025)
* •

  British Government Securities, Nominal Par Yields, 20 year (IADB [[10](https://arxiv.org/html/2602.17373v1#bib.bib10)], IUDLNPY, Daily, 29-08-2025)
* •

  British Government Securities, Nominal Zero Coupon Yields, 5 year (IADB [[10](https://arxiv.org/html/2602.17373v1#bib.bib10)], IUDSNZC, Daily, 29-08-2025)
* •

  British Government Securities, Nominal Zero Coupon Yields, 10 year (IADB [[10](https://arxiv.org/html/2602.17373v1#bib.bib10)], IUDMNZC, Daily, 29-08-2025)
* •

  British Government Securities, Nominal Zero Coupon Yields, 20 year (IADB [[10](https://arxiv.org/html/2602.17373v1#bib.bib10)], IUDLNZC, Daily, 29-08-2025)

The reason we selected these features as the exogenous policy data is beacuse authorities and regulators can directly immpact them, and through these, impact the rest of the economy. This specific selection was also made because the data for these time series was accessible and all of the readings in these time series span at least from 2008 to August 2025, which is important as it maps to the range of the data for our Bitcoin supply distribution data. There are plenty of other time series that could be considered here, but we will limit our analysis to this data only.

### 2.2 Macroeconomic Data

Below are the time series that we use to explain some of the noise that exists in the wealth distribution time series due to macroeconomic factos. Just like in the case with exogenous policies, there are some time series that may better explain some of the variance of the wealth distribution buckets, but we stick to these as they are accessible and cover a lot of diverse macroeconomic factors.

* •

  Total Nonfarm All Employees (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], PAYEMS, Monthly, 01-07-2025)
* •

  Unemployment Rate (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], UNRATE, Monthly, 01-07-2025)
* •

  M1 (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], WM1NS, Weekly, 04-08-2025)
* •

  M2 (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], WM2NS, Weekly, 04-08-2025)
* •

  Market Value of Gross Federal Debt (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], MVGFD027MNFRBDAL, Monthly, 01-07-2025)
* •

  Market Value of Privately Held Gross Federal Debt (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], MVPHGFD027MNFRBDAL, Monthly, 01-07-2025)
* •

  Consumer Price Index for All Urban Consumers: All Items in U.S. City Average (FRED [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], CPIAUCSL, Monthly, 01-07-2025)
* •

  Gold Price Against US Dollar (Yahoo! Finance [[11](https://arxiv.org/html/2602.17373v1#bib.bib11)], GC=F, Daily, 26-08-2025)

### 2.3 Microeconomic Data

Lastly, we selected a microeconomic time series that we believe is also relevant to the analysis, as semiconductors are used by the graphics cards, which are often tied to the Bitcoin mining, so we decided to include this time series to check whether it impacts the wealth distribution data.

* •

  Producer Price Index by Industry: Semiconductor and Other Electronic Component Manufacturing (FRED, [[9](https://arxiv.org/html/2602.17373v1#bib.bib9)], PCU33443344, Monthly, 01-07-2025)

## 3 Impact of Exogenous Factors on Wealth Distribution

In this section we examine the significance of different features described in Section [2](https://arxiv.org/html/2602.17373v1#S2 "2 Scope ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") for Bitcoin’s wealth distribution, how do they impact the wealth distribution buckets, and consequently, we clear the wealth distribution buckets from the noise introduced by these features to facilitate further analysis of the cleared data. We start by creating a model for each of the wealth distribution buckets in terms of the features from Section [2](https://arxiv.org/html/2602.17373v1#S2 "2 Scope ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"). Once we filter out the insignificant features from the model, we use this model to extract the noise term ϵ\epsilon that the features fail to explain, as we consider it to be the the data that is cleaned from the impact of exogenous factors, and so we use it to analyze the impacts of BIPs in the next section.

### 3.1 Data Pre-Processing

Before proceeding with our analysis, we must transform all of the time series so that they become stationary. The motivation for this is that most economic and financial time series are non-stationary and they usually experience some drift over time (e.g., exponential-like rise in *Personal Current Taxes* from 1959 to 2025). This property of time series can skew our analysis as if we pick a large enough time frame and two time series that are non-stationary, there will always be a relationship between them (e.g., positive Pearson correlation) since both time series drift away from their starting point over time.

To mitigate this phenomenon we must apply data transformations to the time series in order to convert these time series to stationary time series. For that we use two distinct transformations: first-order differencing and log change transformation.

First-order differencing is a transformation where for every time step in a time series we subtract previous value in the time series from the current value in the time series so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​xt=xt−xt−1\Delta x\_{t}=x\_{t}-x\_{t-1} |  | (1) |

where Δ​xt\Delta x\_{t} is the transformed value of the series. Note that this transformation produces a time series which is one element shorter than the original time series since the initial value of the series does not have a value before it in the time series. This transformation we apply to the following time series:

* •

  Federal Funds Rate
* •

  5 Year HQM Corporate Bond Par Yield
* •

  10 Year HQM Corporate Bond Par Yield
* •

  30 Year HQM Corporate Bond Par Yield
* •

  5 Year HQM Corporate Bond Spot Rate
* •

  10 Year HQM Corporate Bond Spot Rate
* •

  30 Year HQM Corporate Bond Spot Rate
* •

  5 Year Gilts (Nominal Par Yield)
* •

  10 Year Gilts (Nominal Par Yield)
* •

  20 Year Gilts (Nominal Par Yield)
* •

  5 Year Gilts (Nominal Zero Coupon Yield)
* •

  10 Year Gilts (Nominal Zero Coupon Yield)
* •

  20 Year Gilts (Nominal Zero Coupon Yield)
* •

  Unemployment Rate
* •

  Gold Price Against USD

All of the time series listed above are quoted as a rate, so by applying the first-order differencing we obtain time series of changes in the original time series. The reason we want a time series of changes in the original is because we want a stationary time series that tells us how much the original one grew or declined by independently from the previous time steps, so that we can compare the growth/decline patterns across different time series. Under this transformation the distribution of increments Δ​xt\Delta x\_{t} is not skewed due to their size since a rise and decline by fixed Δ​xt\Delta x\_{t} leaves the original value xtx\_{t} unchanged (Conversely, assume a case where xtx\_{t} is increased by 5% and then decresed by 5% - the resulting value wil not be equal to xtx\_{t}, and so the distribution of increments might be skewed towards positive increments Δ​xt\Delta x\_{t} under a simple percent change transformation).

The second transformation type we use is the log-change transformation, which is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=l​n​(xt)−l​n​(xt−1)R\_{t}=ln(x\_{t})-ln(x\_{t-1}) |  | (2) |

where RtR\_{t} is the log-change of the original time series. As before, this time transformation produces a time series which is one element shorter than the original one. We apply this transformation to all time series excluding the ones listed above under the first-order differencing, and we also apply log-change to wealth distribution time series themselves. As before, log-change transformation yields time series that are stationary and it also eliminates the skewness bias described above.

Lastly, by applying these transformations to original time series we obtained their stationary counterparts, we now run an Engle-Granger two-step cointegration test with a 5%5\% confidence level between all of the transformed independent variables (i.e., our features’ time series) and all of the transformed dependent variables (i.e., wealth distribution buckets) to confirm that there is a long-term stable relationship between the features and wealth distribution time series. The cointegration test was passed by every pair of independent and dependent variables.

### 3.2 Linear Regression Analysis of Wealth Distribution

Having transformed the data into stationary time series, we now attempt to explain away some of the variance in the wealth distribution that potentially belongs to external factors. To do so we propose to design a linear regression model for every wealth distribution bucket in terms of the exogenous factor time series we have at our disposal.

The reason for using linear regression is that it produces a good estimate for the linear dependency between independent and dependent variables, and since many relationships in econommics and finance are considered to be linear, linear regression is a fitting tool to use. In section [3.1](https://arxiv.org/html/2602.17373v1#S3.SS1 "3.1 Data Pre-Processing ‣ 3 Impact of Exogenous Factors on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") we have also ensured that the time series we use are stationary and the linear combination of stationary time series is also stationary, which means that we can use linear regression to model the change in wealth distribution using the independent variables we have proposed.

Linear regression also comes with a useful toolkit for systematically filtering out insignificant independent variables by performing a t-test on the linear regression slope and a check for colinearity between independent variables by computing the variance inflation factor. However, before applying those, we must construct a base model with all available time series. In the context of this paper we refer to such models as the “global linear regression” models as we regress over all of the available data. A global linear regression is of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=α+β1​X1+β2​X2+…+βn​Xn+ϵY=\alpha+\beta\_{1}X\_{1}+\beta\_{2}X\_{2}+...+\beta\_{n}X\_{n}+\epsilon |  | (3) |

where YY is the transformed wealth distribution bucket and XiX\_{i}’s are the transformed independent variables. Note that since we have 10 wealth distribution buckets we will have 10 different global linear regression models.

Another caveat of this approach to explaining the variance in wealth distribution is that the time series we use as the features XiX\_{i} of the model all have different lengths and different frequencies. This means that we had a choice of whether to do an inner join on the data or perform a left join of features with the respective wealth distribution bucket and fill-in the missing data. Since we wanted to preserve as much of the relationship as possible, we decided to downsample our data set and use monthly readings for all variables, which resulted in the data set with 140 historical data points for each of the 10 models. We consider this to be sufficient sample size to run linear regression on in order to establish the significance of the independent variables.

After running all 10 global linear regression models, we have obtained the estimators α\alpha and βi\beta\_{i} for the model along side their standard errors S​EαSE\_{\alpha} and S​EβiSE\_{\beta\_{i}}, which are used in the t-tests. For the t-tests, we assumed that the null hypothesis is βi=0\beta\_{i}=0 (i.e., there is no relationship between the independent variable ii and the wealth distribution bucket) since we have never fitted the model before and we want to use the global linear regression to check for the existence of relationships between our independent and dependent variables. The results of the t-tests for all global linear regression models are presented in Appendix [B](https://arxiv.org/html/2602.17373v1#A2 "Appendix B Global Linear Regression (p-values) ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?").

Each column name in these tables is a wealth distribution bucket, and once transformed, represents YY from equation [3](https://arxiv.org/html/2602.17373v1#S3.E3 "In 3.2 Linear Regression Analysis of Wealth Distribution ‣ 3 Impact of Exogenous Factors on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), while every row name is the name of the feature before it was transformaed to become XiX\_{i}. The way these tables can be interprited is that every column represents a model for the specific wealth distribution bucket where the row names are the features we used in this model to predict the changes in this wealth distribution bucket. The tables’ cells show p-values of the linear regression slope t-test.

To check for significance we use a 5%5\% confidence level - the highlighted cells demonstrate the significant relationships in the independent variables and wealth distribution buckets. However, we must now filter out all of the insignificant features for every model, run the linear regression and again check for significance of each feature again. Once we have done that, we discover that some independent variables that were previously significant became insignificant. Thus we carry on with this cycle until only the variables that are significant according to the t-test at 5%5\% confidence level remain in our models.

The results for completely filtered models are presented in Appendix LABEL:appendix:FilteredLinearRegressionPValues. From these tables we see that the only significant independent variables left are *Federal Funds Rate* and *M2 (US)* that contribute to *From 0 to 0.001* and *From 10 to 100* wealth distribution bucket respectively.

### 3.3 Cleaning of Wealth Distribution Data

Having created the models for the wealth distribution buckets, we now use these models to find the error term ϵ\epsilon that we can use for our analysis of BIPs and their impacts. Notice that ϵ\epsilon for all wealth distribution buckets except for *From 0 to 0.001* and *From 10 to 100* will be simply the transformed wealth distribution buckets, since they don’t have any features in their model to explain the variance.

The only models with significant parameters according to the t-tests are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | YFrom 0 to 0.001=0.02188​XFederal Funds Rate+ϵY\_{\text{From 0 to 0.001}}=0.02188X\_{\text{Federal Funds Rate}}+\epsilon |  | (4) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | YFrom 10 to 100=0.12899​XM2 (US)+ϵ,Y\_{\text{From 10 to 100}}=0.12899X\_{\text{M2 (US)}}+\epsilon, |  | (5) |

where we included the slope coefficients for the models, and the p-values for XFederal Funds RateX\_{\text{Federal Funds Rate}} and XM2 (US)X\_{\text{M2 (US)}} are 0.0000100.000010 and 0.0015550.001555 respectively. Note that both models do not have an intercept as the itercepts in either model did not have a significant t-score.

Since we established the shapes of the models, we can now obtain the error terms for these models, which we assume to be cleaned data that is not explained away by the exogenous factors. We will see that this assumption is important in the next section when we will by studying the impact of BIPs on this cleaned data.

### 3.4 Summary

In this section we have described a procedure by which we explain away the noise in wealth distribution buckets attributed to the exogenous factors to the Bitcoin token economy. We have transformed the data into stationary time series to eliminate undesired side effects of processing raw data. Then we constructed multivariate linear regression models which we used to remove the insignificant independent variables from our analysis, and then to clean the wealth distribution data to obtain the data the variance in which we assume is primarily explained by the Bitcoin Improvement Proposals.

## 4 Impact of Endogenous Policies on Wealth Distribution

In this section we check what Bitcoin Improvement Proposals (BIPs) can be considered as financial policies, examine their possible causal relationship with the Bitcoin wealth distribution buckets, and compare the results from different causality testing techniques. To ensure that the wealth distribution is not impacted by any exogenous factors, we have filtered out the noise produced by these such factors in the previous section. We refer to the supply distribution where the imapct of exogenous factors has been removed as the cleaned wealth distribution.

The analysis procedure employed here can be broken down into the following steps:

1. 1.

   Select a set of BIPs to perform an analysis with
2. 2.

   Create a signal time series out of the selected subset of BIPs
3. 3.

   Run a causal relationship test between the BIPs signal time series and the cleaned wealth distribution

Following this process, we can determine whether a subset of BIPs potentially causes the changes in the wealth distribution. However, there are two major questions that arise from the process described above: how do we select a subset of BIPs to test whether they cause the changes in the wealth distribution; and what causation test do we use to test for the existence of the relationship. We attempt to answer these questions in the two subsequent sections respectively.

### 4.1 Filtering of BIPs Data

In an ideal world, we would have a label on each BIP that represents whether this BIP is an economic policy or not, which then we would be able to use in our analysis. However, even if that were true, there would still be a number of “non-economical” BIPs that would probably cause some wealth redistribution that would must be included in the analysis. There is also no possibility to run the causation tests iteratively creating samples with different combinations of BIPs as at the moment of writing there are 176 BIPs whcih makes an iterative sampling technique highly impractical.

Due to these issues, we decided on a different approach for selecting the “economic policy” BIPs and running the causality tests. Instead of having one subset of BIPs, we decided on having the following four subsets:

* •

  All BIPs: A set that contains all available BIPs
* •

  All Economy-Related BIPs: BIPs that we manually selected that seem to be economic policies - more on the selection process later
* •

  Major Economy-Related BIPs: BIPs that are considered to have large impact according to different sources
* •

  All Economy-Related BIPs Except the Major Economy-Related Ones

In the further sections we elaborate on our choices and methodology for selecting BIPs for these subsets.

#### 4.1.1 All BIPs

The fist category (i.e., *All BIPs*) is a set of BIPs that will be used as the benchmark data for the control test, and since most of the BIPs are distributted across the time span of the cleaned wealth distribution data, we expect the signal time series containing all BIPs to have too much noice to pass most causality tests available.

#### 4.1.2 All Economy-Related BIPs

The second category (i.e., *All Economy-Related BIPs*) represents BIPs that we consider to be economic policies or BIPs that we believe have the potential to cause wealth redistribution. One of the objectives of this paper is to provide an initial framework for categorizing policies in token economies, but due to nonexistence of such yet we had to go over all the BIPs and manually select the BIPs that we think broadly fit under the following categories:

* •

  Improvements Aimed Directly at Supply or Liqudity: 9, 42, 100, 101, 102, 103, 104, 105, 106, 107, 109, 152, 331
* •

  Transaction Improvements or Upgrades: 11, 13, 16, 65, 66, 68, 78, 79, 112, 115, 116, 118, 125, 127, 129, 134, 146, 174, 322, 324, 330, 352, 370, 373
* •

  Embedded Financial Instruments and Solutions: 197, 199, 300, 345
* •

  Security and Privacy Improvements or Failures: 30, 50, 53, 54, 151, 351
* •

  Hierarchical Deterministic Wallets: 32, 39, 43, 44, 49, 84, 88, 175
* •

  SegWit: 91, 141, 148, 173
* •

  Taproot: 326, 327, 341, 343, 371
* •

  Improvements that Simplify or Popularize the Bitcoin Economy: 1, 21, 47, 61, 70, 72, 75, 111, 380

Note two things: first, this categorization for structuring economic policies in a token economy is only an initial suggestion for the framework and is not necessarily exaustive; second, there are BIPs that can satisfy multiple categories (e.g., *BIP 39* proposes an introduction of mnemonic code for generation of HD wallets, which can be categorized under the HD wallets improvement or as the improvement that simplifies/popularizes Bitcoin to its end users), in which case we place it under a category that has a more limiting definition (e.g., *BIP 39* goes into the HD wallets category).

By categorizing BIPs into these categories it helps us to understand what part of the token economy they are targeting and will help us in building the economic policy taxonomy for token economies in Section [5](https://arxiv.org/html/2602.17373v1#S5 "5 Economic Policy Taxonomy of Token Economies ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"). The reason we do not use these categories for our analysis directly is because they have been manually selected and as explained above some of the BIPs have stong overlap with other categories so we would have to come up with a mechanism for deciding whether to include these BIPs or not, which will make the results even more subjective.

Lastly, notice that we have purposefully defined *Hierarchical Deterministic Wallets*, *SegWit* and *Taproot* as separate categories. The motivation behind this is that these were major series of updates to many different parts of Bitcoin that have caused a lot of discussions in the Bitcoin community at the time of their releases. Therefore, we hypothesise that these events would have caused major changes in the wealth distribution and since each of them touched upon a lot of different parts of the Bitcoin ecosystem, we decided to treat BIPs related to them as separate categories.

#### 4.1.3 Major Economy-Related BIPs

As mentioned in the previous section, there are some BIPs that stand out amongst the other ones as they proposed or described major changes to the Bitcoin token economy. We have counted five such BIPs, notably:

* •

  BIP 32 (2012-02-11, Informational, Final): Hierarchical deterministic wallets are proposed that can be interchanged between clients, and allow generation of public keys without disclosing the private key.
* •

  BIP 42 (2014-04-01, Standards Track, Final): Introduction of static money supply for Bitcoin.
* •

  BIP 50 (2013-03-20, Informational, Final): A block that had a larger number of total transaction inputs than previously seen was mined and broadcasted. Bitcoin 0.8 nodes were able to handle this, but some pre-0.8 Bitcoin nodes rejected it, causing an unexpected fork of the blockchain. Bitcoin 0.8 nodes had to downgrade to resolve the fork, during this time there was at least on large double spend, which was not intended to be malicius (i.e., was experimental).
* •

  BIP 141 (2015-12-21, Standards Track, Final): Defines a new structure called a ”witness” that is committed to blocks separately from the transaction merkle tree. This structure contains data required to check transaction validity but not required to determine transaction effects. In particular, scripts and signatures are moved into this new structure. The witness is committed in a tree that is nested into the block’s existing merkle root via the coinbase transaction for the purpose of making this BIP soft fork compatible.
* •

  BIP 341 (2020-01-19, Standards Track, Final): Proposes a new SegWit version 1 output type, with spending rules based on Taproot, Schnorr signatures, and Merkle branches.

We decided to construct a separate signal time series out of these major BIPs as we expect them to have the most significant impact on the cleaned wealth distribution data.

#### 4.1.4 All Economy-Related BIPs Expect the Major Economy-Related Ones

We define this category as the set subtraction between the *All Economy-Related BIPs* and *Major Economy-Related BIPs* (Note that the latter is the subset of the former). The reason we included this set of BIPs into our analysis is because if the previous two categories produce deviating results, we would like to understand what exact difference do the *Major Economy-Related BIPs* make, so this subset also acts as a control test just like the category *All BIPs*.

### 4.2 Granger-Casusality Test

Having motivated our selection of BIPs for constructing the signal time series, we now move to the selection of the causality testing techniques available to us. The tool that is most commonly used for this purpose in the industry and acadmic research is the Granger-causality test [[4](https://arxiv.org/html/2602.17373v1#bib.bib4)].

The method proposed by Granger [[4](https://arxiv.org/html/2602.17373v1#bib.bib4)] relies on breaking down the two time series, whose causal relationship is being tested, into their oscillator subparts using the Fourier transformation, which is a very theoretical approach and which can lead to long compute times and inaccuracies when used in computational data processing. For this reason, in statistical packages like *statsmodels* [[13](https://arxiv.org/html/2602.17373v1#bib.bib13)] there exist Granger-causality test functions that are optimized for computational analysis. Upon examination of different statistical packages the authors have found inconsistencies of implementation between different statistical packages and methodologies proposed as alternatives to the spectral analysis proposed by Granger in his original work [[4](https://arxiv.org/html/2602.17373v1#bib.bib4)].

In online resources like Wikipedia [[5](https://arxiv.org/html/2602.17373v1#bib.bib5)], the process for testing for Granger-causality can be summarised as the follows given the independent variable *X* and the dependent variable *Y*:

1. 1.

   Create an autoregressive model of *Y*, with the order of model being determined by the partial autocorrelation function, where the order is the highest order of *Y* above some set critical level. Call this model a nested model.
2. 2.

   Extend the nested model to include autoregressive terms of *X*, where the order of *X* is selected by minimizing an information criterion (e.g., Akaike, Bayesian, etc.).
3. 3.

   Iteratively filter out the insignificant lagged terms of *X* until only the terms that pass t-test at a given critical level remain. Call this model the parent model.
4. 4.

   Run the F-test between the nested and parent models to determine whether adding the independent variable *X* explains away some of the variance, given the specified critical level for the F-test.

Such procedure reasonably replaces the original procedure introduced by Granger. However, upon examining the Granger-causality test in the *statsmodels* Python package, it became apparent that the test implemented there uses a variable called m​a​x​\_​o​r​d​e​rmax\\_order which acts as the order for the lagged terms of *X* and *Y* simultaneously, therefore, creating nested and parent multivariate linear regression models with orders O​(m​a​x​\_​o​r​d​e​r)O(max\\_order) and O​(2​m​a​x​\_​o​r​d​e​r)O(2max\\_order) respectively. The Granger-causality test in the package also ignores the t-test filtering.

The problem with this implementation is that it is a lot less limiting than the one suggested by Wikipedia [[5](https://arxiv.org/html/2602.17373v1#bib.bib5)], and yet the package only cites the original paper, which takes a completely different approach. To ensure the validity of results, we decided to use both test variations calling the *statsmodels* implementation a “Simple” test and the Wikipedia one a “Full” test, since it provides a more sophisticated filtering process. Both of these techniques are implemented in the Rust package DigiFi [[12](https://arxiv.org/html/2602.17373v1#bib.bib12)], which we used for the analysis.

### 4.3 Endogenous Policies Analysis

Now that we have selected the sets of BIPs and the tools that we will use in our analysis, we can perform the tests. From Section [3](https://arxiv.org/html/2602.17373v1#S3 "3 Impact of Exogenous Factors on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), we know that the cleaned wealth distribution data is in the monthly format as most of the exogenous factors we have used to clean data are quoted on a monthly basis. This means that when we convert the BIP sets we have selected into signal time series, we have to make it monthly as well (i.e., if there was a BIP relased in that month, the value of the time series for that month is 11 and otherwise it is 0). Appendix [A](https://arxiv.org/html/2602.17373v1#A1 "Appendix A Cleaned Supply Distribution Data ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") shows each cleaned supply distribution bucket in a blue line, and the BIPs as the dashed vertical red lines (Note that these plots include every BIP).

As there are ten cleaned wealth distribution buckets, four BIP signal time series and two Granger-causality test variants, we will have 8080 results, where the value TT (i.e., True) indicates the existence of Granger-causality between the respective BIP signal time series and the cleaned wealth distribution data, while FF (i.e., False) means there is not enough evidence to conclude that there is Granger-causality. For further convenience, we have added extra information about each of the tests’ results - for tests that have shown a Granger-causality we have added a longest significant lag in the parent model in the brackets next to TT (note that for “Simple” test it will always be equal to the maximum lag that we set, as “Simple” test does no apply t-test filtering‘), whereas for failed tests we have included the reason for its failure in the bracket next to FF. Also note that we have used very standard parameters for tests: for the “Full” test we used 10%10\% critical interval for the partial autocorrelation function with its maximum lag set to 1010 (i.e., 1010 months in terms of our data), 1010 maximum lag for the independent variable, and 5%5\% critical level for both t-test and F-test; for the “Simple” test we have used 1010 maximum lag (as described above it applies to both time series) and a 5%5\% critical level for the F-test (“Simple” test does not have t-test, so there is no critical level for it).

The results are presented in Appendix [C](https://arxiv.org/html/2602.17373v1#A3 "Appendix C BIPs Causality Analysis ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), where the cells with TT have been highlighted for convenience. The first thing we note is the consistency between the two Granger-causality test implementations, where we see a similarity between the patterns across the data. This is important as it means that different causality test implementations yield similar results.

The second observation is that, as expected, *All BIPs* signal time series doesn’t show significant causal relationship with any of the wealth distribution buckets as it potentially proves to be too uniform. Other signal time series, however, have all showed some causal relationship with at least one of the wealth distribution buckets.

Furthermore, we note that *All Economy-Related BIPs* set seems to cause significant wealth redistribution amongst the wealthy addresses, yet the *Major Economy-Related BIPs* set has impacted the poorer and mid-wealth addresses. To further formulate the hypothesis that can help explain this pattern in the data, we must mention that there is a distinction between addresses and real people, and therefore, the behavioural factors that may impact one person may impact multiple addresses that are controlled by that individual and vice versa, when multiple people share an ownership of one address the behavioural factors may not impact that address, yet impact the people. Because of the lack of data, in this analysis we assume that the addresses correspond to people, and therefore, when we talk about the behavioural factors that may affect addresses we assume that these factors affect the people who are represented by these addresses.

The significant wealth redistribution among the wealthier addresses is an interesting pattern as it may suggest that the more wealthy addresses are more engaged in the Bitcoin ecosystem as they have higher stake in it, while the addresses with less wealth are less engaged in the process and they only respond to large economic events as these get propagated through many different communication and marketing channels. It could also signify that the more wealthy addresses better anticipate the major changes (or even cause them as the wealthy addresses are the de facto governors of the system) and they gradually move wealth, therefore, pricing-in the major changes to the Bitcoin economy. To add to this from a different perspective, it may also imply that if the majority of poorer addresses are owned by a small group of individuals, it may point to the difficulty of redistributing wealth by these individuals when the small changes to the economy are made, whereas when the big policy changes are introduced, they may be forced to react. This, however, does not change the pattern in the data: the wealthier addresses seem to respond to the “minor” economic policy changes, and the poorer addresses seem to be more reactive to the “major” policy changes.

In general, we hypothesize that this discrepancy is caused by the information asymmetry where the wealthy addresses move wealth quickly in response to the release of “minor” economic policies as they constantly monitor the space and have the resources to do so, yet they price in the “major” economic policy changes as they either directly cause these changes or are aware of them. On the contrary, the owners of the poorer addresses seem to either pay less attention or have poor information about the “minor” economic policy changes so they don’t respond to it, while the “major” policy changes cause poorer addresses to make reactive investment decisions as they don’t anticipate the changes. We can visualize this hypothesis by the table [1](https://arxiv.org/html/2602.17373v1#S4.T1 "Table 1 ‣ 4.3 Endogenous Policies Analysis ‣ 4 Impact of Endogenous Policies on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), where the lack of the response to the policy changes is indicated by FF and statistically significant response (i.e., significant log-change in wealth distribution) to policy changes is indicated by TT.

|  |  |  |
| --- | --- | --- |
|  | Wealthier Addresses | Poorer Addresses |
| |  | | --- | | Major Economic | | Policy Changes | | |  | | --- | | False | | (Priced In) | | True |
| |  | | --- | | Minor Economic | | Policy Changes | | True | |  | | --- | | False | | (Little Resources/Small Stake) | |

Table 1: Possible explanation of patterns present in causation analysis between BIPs and wealth redistribution

Next, we see that the control tests with *All Economy-Related BIPs Except Major Economy-Related Ones* signal time series shows a pretty similar picture to the tests run with the *All Economy-Related BIPs* as expected with only difference being the “Simple” test with *From 10 to 100* bucket. The possible reason for this is that the test value was very close to the critical level and it barely managed to pass, but we do not see a trend that would suggest that removing *Major Economy-Related BIPs* from *All Economy-Related BIPs* should produce a completely different set of results.

Finally, we must discuss the sensitivity of our results to the parameters that we have used. In the table in Appendix [C](https://arxiv.org/html/2602.17373v1#A3 "Appendix C BIPs Causality Analysis ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), we see that for the “Full” test there is a cell that implies that the lag of 1010 months is still significant, so we wondered what happens if we shrink or extend the test window. We decided to re-run the same Granger-causality tests, but this time with 66 and 1212 as the maximum lag for the partial autocorrelation function and independent variable (i.e., 66 and 1212 months), the results of these tests are presented in Appendices [D](https://arxiv.org/html/2602.17373v1#A4 "Appendix D BIPs Causality Analysis (6 months) ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") and [E](https://arxiv.org/html/2602.17373v1#A5 "Appendix E BIPs Causality Analysis (12 months) ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") respectively. Despite the slight difference in the results, the overall pattern seems to remain the same, which makes us believe that this pattern is relatively stable and is not significantly impacted when changing the test window. The other interesting result from this sensitivity analysis, is that in the 1212 months table in Appendix [E](https://arxiv.org/html/2602.17373v1#A5 "Appendix E BIPs Causality Analysis (12 months) ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), the “Full” test shows that the longest significant lag is 66 months, which lines up with the result from the 66 months table (note that despite not being presented in the table in Appendix [C](https://arxiv.org/html/2602.17373v1#A3 "Appendix C BIPs Causality Analysis ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), the cell that shows 1010 months as the longest significant lag for the “Full” test also has 66 months lag as being significant according to the t-test, so all three tables line up in that conclusion). Therefore, we hypothesise that 66 months is the longest significant period for BIPs to make an impact on wealth distribution as per the results from the “Full” test, while the 1010 months cell we see as a statistical anomaly.

### 4.4 Summary

These results are interesting because they highlight potential patterns in wealth redistribution, but it also signifies that our approach of selecting policies, albeit somewhat subjectively, is not a coincidence and that we potentially can formalize it into a taxonomy. We also see that BIPs do have an impact on wealth distribution, and that different sets of policies have impacts on different wealth distribution buckets in the Bitcoin economy. This section, in conjunction with the previous one, proposes a technique for analysis of policies and their impact on token economies, and can potentially be generalized to standard economies given the appropriate data.

This methodology can be further improved by adding a more in-depth analysis of the linear regressions that were constructed as part of the “Full” Granger-causality test such as the review of the p-values produced by the iterative t-tests for every coefficient and the p-value of the F-test. This would explain the deviation between the “Full” and “Simple” tests, and provide feedback on whether the selected confidence levels were too restrictive or permissive. The other improvement that could be added to this analysis technique is a procedure for determining the maximum order of the partial autocorrelation function and maximum lag of the independent variable in the “Full” test, and the maximum lag in the “Simple” test. For the purpose of the paper, we assume that BIPs do not have an impact delay of over 1010 months and from the sensitivity analysis we see that the most significant impact delay is 66 months, but it would be useful to define a procedure for determining that impact delay window. However, we leave both of these improvement proposals for future work.

## 5 Economic Policy Taxonomy of Token Economies

In this section we aim to formalize the observation made in Subsection [4.1.2](https://arxiv.org/html/2602.17373v1#S4.SS1.SSS2 "4.1.2 All Economy-Related BIPs ‣ 4.1 Filtering of BIPs Data ‣ 4 Impact of Endogenous Policies on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), where we have clustered BIPs into categories justifying it by stating that they seem to be “economy-related”. To create a taxonomy of economic policy in token economies, we will use the frameowrk proposed in *Economic Policy Taxonomy* [[3](https://arxiv.org/html/2602.17373v1#bib.bib3)] as the backbone, and will map BIPs to parts of that framework, and vice versa, we will use that framework to suggest possible policies that could be implemented in token economies. However, upon previous examining of BIPs we know that some of these policies, despite us considering them economic policies, cannot be mapped directly to the policies in standard economies. For this reason we will split this section into two parts: the first part is the taxonomy of economic policies in token economies that can be mapped to the policies in standard economies; and the second part is the taxonomy of economic policies that are specific to the token economies.

Before we begin, notice that here we propose a starting point for a taxonomy that should be extended and modified with future research, rather than accepted as the complete and exhaustive list. In this section we adopt the definitions of policy and atomic policy as per *Economic Policy Taxonomy* [[3](https://arxiv.org/html/2602.17373v1#bib.bib3)]:

###### Definition 1.

Policy is a set of ideas or a plan of what to do in particular situations that has been agreed to officially by a group of people, a business organization, a government or a political party.

###### Definition 2.

Atomic Policy is an individual action or idea that applies a change to a specific body or phenomena.

We specifically aim to identify atomic policies as these are the individual actions that cannot be broken down into smaller set of actions. These are very useful to understand as a global economic policy is a set of atomic actions implemented at once, which are aimed at specific parts of the economy. Understanding possible atomic policies means we are able to design more precise economy models using the DeTEcT framework.

### 5.1 Standard Economic Policy Taxonomy in Token Economies

The caveat of recreating a policy taxonomy framework for token economies is that we need a government and central bank to map the atomic policies from standard economies, but since token economies are considered decentralised there is no one agent in the economy that is responsible for setting policies and redistributing wealth. To solve this issue we can use *Control Mechanism* proposed in DeTEcT [[1](https://arxiv.org/html/2602.17373v1#bib.bib1)] as an agent in the economy that receives and spends wealth, which we can think of as the protocol itself. While it is true that the protocol itself is goverened by other agents in the economy, and therefore, there is a distinction in governance and wealth redistribution flows, the taxonomy is only concerned with the cash flows and not the governance infrastructure, which without loss of generality can be abstracted away.

Since *Control Mechanism* is considered to be a unique agent, yet in standard economy we would have *Government* and *Central Bank* as two different entities, we propose preserving the distinction between fiscal and monetarty policies even in token economies as it will provide a better mapping with the standard economy policies and will allow us in the future to separate the roles of *Control Mechanism* into a “government-like” and “central bank-like” agents inside a token economy, which itself can be considered an atomic policy.

We start by introducing an income statement for *Control Mechanism* where we separate it into two parts as described above: fiscal-like and monetary-like parts.

* •

  Fiscal-Like Income Statement

  + –

    Revenue

    - \*

      Transaction Fees: Fees paid directly to the protocol (Not to confuse with the transaction fees that are paid to the miners for including a transaction in a block).
  + –

    Expenses

    - \*

      Cost of Sales: Tokens issued to the agents that maintain economy operation (e.g., miners).
    - \*

      Incentives: Incentives issues by *Control Mechanism* to economy participants for satisfying a predetermined condition.
* •

  Monetary-Like Income Statement

  + –

    Revenue

    - \*

      Sale of Foreign Currency: Reaquisition of tokens for other type of currency.
  + –

    Expenses

    - \*

      Purchase of Foreign Currency: Sale of tokens for other type of currency.

The statements defined here are a lot more compact than the ones defined in *Economic Policy Taxonomy* [[3](https://arxiv.org/html/2602.17373v1#bib.bib3)] as there are fewer moving parts in token economies than there are in standard economies. However, as there are limited number of BIPs, we can more clearly outline atomic policies that *Control Mechanism* can use to regulate an economy and provide examples of policy implementations. Below is the mapping between the token economy fiscal-like policies and a standard economy fiscal policies:

* •

  Revenue Policy

  + –

    Transaction Fee Size: Amount of tokens payable for transaction completion that will be “burned” (i.e., Removed from current circulation).
* •

  Expenditure Policy

  + –

    Mining Fee Size: Size of rewards issued by the protocol to the agents that produce and validate transaction blocks.
  + –

    Intentive Size: Size of reward issued by the protocol to the agents that satisfy specific criteria.
  + –

    Incentive Criteria: Criteria that must be satisfied by an economy participant in order to receive a token reward.
* •

  Auxiliary Policy

  + –

    Auctions: Allowing for economy participants to negotiate the terms of a transaction among themselves (e.g., *BIPs 78, 199*).

Since most policies implemented by *Control Mechanism* are directed at changes in supply or regulation of transactions and trade of financial instruments inside a token economy, there are far more monetary-like atomic policies that we have managed to identify in using BIPs:

* •

  Debt and Credit Policy: Policy surrounding creation or issuance of debt by the *Control Mechanism*.

  + –

    Fixed Supply: Maximum bound for the supply set in the economy (e.g., *BIP 42*).
  + –

    Dynamic Supply: Infinite maximum bound for the supply set in the economy.
  + –

    Supply Increment: Additional issuance of tokens to the maximum supply.
  + –

    Supply Decrement: Removal of tokens from the maximum supply.
* •

  Financial Markets Policy: Regulation of transactions and financial instruments issued or build on top of the token economy.

  + –

    Complex Transaction: Transactions with conditions attached that are defined by the transacting parties that describe input, output or intermediary constraints that have to be satisfied for the transaction to be successful (e.g., *BIPs 13, 16*).

    - \*

      Number of Signatures: Number of signatures required by the transaction to complete (e.g., *BIP 11*).
    - \*

      Relative Lock-Time: Timestamp that triggers the completion of transaction (e.g., *BIP 68*).
    - \*

      Future Agreement: The output of a completed transaction is unspendable until some timestamp (e.g., *BIP 65*).
    - \*

      Debt Agreement: Transaction contract that creates a debt agreement between the transacting parties (e.g., *BIP 197*).
    - \*

      Transaction Order: Order in which consequtive transactions must be executed.
    - \*

      Proof of Identity: Request to obtain a proof of identity before the completion of the transaction (e.g., *BIP 75*).
    - \*

      Proof of Reserves: Request to obtain proof of reserves before the completion of the transaction (e.g., *BIP 127*).
    - \*

      Destination: Restrictions on the future destinations of the transaction (e.g., *BIPs 112, 118*).
    - \*

      Recovery Path: Specification of transaction recovery path that can be used to recover wealth to the specified address before the transaction is complete (e.g., *BIP 345*).
    - \*

      System State: State of economy or system is used to constrain the transaction (e.g., *BIP 115*).
    - \*

      Mutable Transactions: Ability for a transaction participant to mutate the state of the transaction after its completion (e.g., *BIPs 125, 141, 370, 371, 373*).
    - \*

      Offline Transactions Support for offline and/or delayed transactions (e.g., *BIP 174*).
    - \*

      Ancestor Package Propagation: Request to relay an unconfirmed ancestor package of the given transaction for in-depth filtering of future transaction tree (e.g., *BIP 331*).
  + –

    Transaction Validation: Validation of transactions against rules defined by the protocol (e.g., *BIPs 53, 54, 66, 146, 173*).

    - \*

      Double Spend Validation: Validation for the transaction not to spend the wealth that has been spent already or mimic another transaction by id or other metadata (e.g., *BIP 30*).
    - \*

      Transaction Size: Maximum cap on the size of the transaction to be included in the block and, by extension, the block itself (e.g., *BIPs 100, 101, 102, 103, 104, 105, 106, 107, 109*).
    - \*

      Metadata: Standardisation and requirements for the transaction metadata that is passed into the block or between peers (e.g., *BIP 152*).
    - \*

      Withdrawal Validation: Requirements for the withdrawal of wealth from L2 and higher layer solutions to the L1 (e.g., *BIP 300*).

This concludes the initial mapping between the atomic policies we identified in token economies to the atomic policies defined in standard economies. Note that the general structure of the taxonomy has been well-preserved, which hints at some overlap between policy making in standard economies versus token economies.

### 5.2 Economic Policy Taxonomy Specific to Token Economies

In this section we cover the economic policies that are specific to the token economies, and therefore, didn’t make it into the taxonomy defined in the previous section. Note that their exclusion from the former taxonomy part does not say anything about their potential impact on the wealth distribution.

* •

  Liquidity Policy: Policies directed at the change in liquidity or transaction throughput in the economy.

  + –

    Hard Fork: Split of the blockchain protocol by nodes based on the applied set of policies.
  + –

    Simultaneous Soft Forks: Ability of a blockchain to run multiple soft forks simultaneously without loosing liquidity due to different software versions (e.g., *BIP 9*).
  + –

    Fork Activation Requirements: Requirements laid out by the economy participants that trigger the activation of a fork (e.g., *BIPs 91, 148, 343*).
* •

  Wealth Storage Policy: Policy that describes how and where wealth will be stored (e.g., wallets)

  + –

    Hierarchical Deterministic Wallets: Wallets that generate addresses in a hierachical structure of addresses that do not disclose a private key and can be shared between economy participants for the purpose of transacting and storing wealth (e.g., *BIPs 32, 44, 175*).
  + –

    MultiSig Wallets: Wallets that require multiple private keys to sign off a transaction (e.g., *BIP 129*).
  + –

    Aggregate Key: Allows generation of aggregate key by multiple signers (e.g., *BIP 327*).
  + –

    Wallet Constraints: Constraints imposed on wallets (e.g., *BIP 88*).
* •

  Social Policy: Policies directed at simplifying, popularizing or enhancing the adoption of token economy by general public (e.g., *BIPs 61, 380*).

  + –

    Standardized Policy Design Mechanism: Mechanism that enables economy participants to create improvement proposals, vote on them and implement them (e.g., *BIP 1*).
  + –

    Payment Schemes: Mechanisms for facilitation of transactions between vendors and customers (e.g., *BIPs 21, 47, 70, 72, 79, 111, 322, 324, 330, 341, 351, 352*).
  + –

    Mnemonic Schemes: Design policy to allow the use of easy-to-remember variables such as primary or public keys by economy participants (e.g., *BIP 39*).
* •

  Auxiliary Policies: Policies that are unique and have limited overlap with other policies.

  + –

    Protocol Choice: Choice of protocol and its rules for processing and validating transactions, as well as allowing the development of higher layer solutions.
  + –

    Monetary Authority: Unique protocol for regulating wealth redistribution and controlling supply vs separate governance and fiscal institutions.

### 5.3 Analysis of Policy Taxonomy Compartments

Having proposed a taxonomy, we have allocated BIPs from the *All Economy-Related BIPs* set to the respective atomic policies or parts of the taxonomy that need to be broken down into atomic policies in the future work (e.g., *Auctions*). Our proposed taxonomy contains three major policy categories: *Fiscal-Like Policies*, *Monetary-Like Policies* and *Purely Tokenomic Policies* (i.e., Policies specific to the token economies). Since we have BIPs reprsenting each of these categories in our taxonomy, we decided to see if the Granger-causality analysis described in Section [4](https://arxiv.org/html/2602.17373v1#S4 "4 Impact of Endogenous Policies on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") can reveal any patternss in this categorisation, so we have run the Granger-causality tests again but with the following three sets of BIPs:

* •

  Fiscal-Like BIPs: 78, 199
* •

  Monetary-Like BIPs: 11, 13, 16, 30, 42, 53, 54, 65, 66, 68, 75, 100, 101, 102, 103, 104, 105, 106, 107, 109, 112, 115, 118, 125, 127, 141, 146, 152, 173, 174, 197, 300, 331, 345, 370, 371, 373
* •

  Purely Tokenomic BIPs: 1, 9, 21, 32, 39, 44, 47, 61, 70, 72, 79, 88, 91, 111, 129, 148, 175, 322, 324, 327, 330, 341, 343, 351, 352, 380

The parameters for the tests were as in the section before: for the “Full” test - 10%10\% critical interval for the partial autocorrelation function with maximum lag of 1010, 1010 maximum lag for the independent variable, and 5%5\% critical level for the t-test and F-test; for the “Simple” test - maximum lag of 1010, and 5%5\% critical level for the F-test. The results of the analysis are presented in Appendix [F](https://arxiv.org/html/2602.17373v1#A6 "Appendix F Taxonomised BIPs Causality Analysis ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"), where TT indicates that the set of BIPs Granger-causes the change in the Bitcoin wealth distribution bucket.

From the table, we see that the results are very sporadic and don’t showcase any visible patterns. The “Simple” and “Full” tests don’t seem to be consistent, and there is also no clear division in what policies impact what wealth distribution buckets. One possible pattern we may trace is that *Purely Tokenomics BIPs* set impacts a multitude of wealth distribution buckets.

A possible explanation of the discrepancy between this result and the causality analysis in Appendix [C](https://arxiv.org/html/2602.17373v1#A3 "Appendix C BIPs Causality Analysis ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") is that different wealth buckets may pay attention to BIPs that introduce changes to the Bitcoin economy, but they do not care whether these are fiscal, monetary, or any other. We speculate that the responses we see in the wealth distribution buckets are caused by specific atomic policies rather than an implementation of a fiscal or monetary policy specifically, which is what we would expect to see.

### 5.4 Summary

In this section we devised a starting point for economic policy taxonomy of token economies. We have used the structure introduced for standard economies [[3](https://arxiv.org/html/2602.17373v1#bib.bib3)] to understand what atomic policies in token economies have their alternatives in standard economies and what policies are exclusive to token economies. This destinction can help us understand the structural difference between the token and standard economies. We analysed whether the attribution of a policy to fiscal or monetary policy makes a difference for the economy participants, and from our results we conclude that such labels don’t seem to have consistent patterns for Bitcoin wealth redistribution. This taxonomy can be further enhanced by going though improvement proposals for token economies sush as Ethereum (i.e., EIPs), but we leave this for future work.

## 6 Future Work

Having conducted our research, we would like to point out a few areas for future research and development of the methodology proposed here. First, we would like to mention that there are many additional exogenous factors that we could consider filtering out in the future, such as factors outside the US and UK jurisdictions (e.g., ECB policies, Chinese central bank policies, etc.), fundamental shocks (e.g., world news, recessions, etc.) and many more. For this purpose, it would be useful to develop a framework that can be used to tell what factors need to be filtered out so that the economic time series in question can be considered “cleaned”.

Second, the methodology for analysing the impacts of policies that we have suggested in this paper can be further improved as per subsection [4.4](https://arxiv.org/html/2602.17373v1#S4.SS4 "4.4 Summary ‣ 4 Impact of Endogenous Policies on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?"). Namely, more rigorous analysis of “Full” Granger-causality test can be derived, where the comparison of the linear regression models of the “Full” and “Simple” tests can be made to determine what lagged features have been filtered out and how sensitive the results of the Granger-causality test are to the changes in the confidence levels of t-tests and F-tests. In addition, a method for determining maximum lag parameters for both tests would be a good addition to the analysis methodology.

The results from Section [4](https://arxiv.org/html/2602.17373v1#S4 "4 Impact of Endogenous Policies on Wealth Distribution ‣ Impacts of Economic Policies on Wealth Distribution in Token Economies How do endogenous and exogenous economic policies impact wealth distribution in token economies?") can be examined further from perspective of token economies, but also from perspective of standard economies and finance. From perspective of token economies, we can try to prove the hypothesis that the wealthier addresses price in the changes in policy by examining the movement of wealth of individual wealthy addresses, while also examining when the poorer addresses tend to execute transactions in comparison to *Major Economy-Related BIPs* signal time series. The time frame of transaction execution added to this research can potentially reveal further patterns in response patterns of different economy participants to the changes in economic policies.

However, these results may also hint at some patterns in standard economies and finance, which can be examined by applying the methodology descibed in this paper. For instance, we can check if “major” economic policy changes proposed or made by a government or central bank are indeed priced in by other economic participants, and whether information asymmetry does cause the discrepancy in response and actions of different Gini coefficient buckets.

Lastly, the economic policy taxonomy for token economies can be further improved by examining the policies implemented or proposed in other token economies such as Ethereum or Solana. These will expand our understanding of possible actions that the policy makers have, and will create a better reference for future research.

## 7 Conclusion

The aim of this paper was to analyse the impact of endogenous policies, represented by BIPs, on the wealth distribution in the Bitcoin token economy, check whether these policies have any impact on the distribution, and understand what atomic polices can be implemented by the regulators in an economy.

We have analysed what exogenous factors impact the Bitcoin wealth distribution, and we conclude that only *Federal Funds Rate* and *M2 (US)* have significant impact on *From 0 to 0.001* and *From 10 to 100* buckets of wealth distribution respectively. Using these results, we have cleaned the wealth distribution data from the noise produce by the external factors and proceeded to examine the causality between the endogenous policies (i.e., BIPs) and the cleaned wealth distribution. From this analysis we conclude that BIPs indeed Granger-cause wealth redistribution, and the poorer addresses in the Bitcoin token economy seem to be impacted by *Major Economy-Related BIPs*, while the richer addresses are impacted by *All Economy-Related BIPs*. This result may hint at the difference in attention that different economy participants pay to the policies being implemented due to the difference in “stake” (i.e., wealth) they have in the economy, or could be attributed to richer addresses being better at predicting major policy changes. According to the sensitivity analysis of the Granger-causality test, we also claim that the impact delay window for BIPs is 66 months, so if new policies are being introduced they should take at most 66 months to make a statistically significant impact.

Guided by the structure intoduced in the *Economic Policy Taxonomy*, we constructed a taxonomy of policies in token economies. We motivated the choices of atomic policies with examples from BIPs, which explains their previous inclusion in the causality analysis. We note that the structure of the taxonomy we constructed for token economies is alike to the structure of policy taxonomy for standard economies, but there are some atomic policies that we could not map to the standard economies, which potentially demonstrates the structural difference in regulation of standard and token economies.

In conclusion, this paper has studied the impacts of exogenous and endogenous factors on the wealth distribution in Bitcoin ecosystem, introduced a starting point for categorization of economic policies in token economies, and proposed a procedure for the analysis of impacts of policies on wealth distribution.

\appendixpage

## Appendix A Cleaned Supply Distribution Data

* Hint
* •

  Red dotted lines represent BIPs
* •

  Year labels on the charts mark the start of the year

![Refer to caption](images/From_0_to_0.001.png)

Figure 1: Log change in wealth distribution of bucket *From 0 to 0.001*

![Refer to caption](images/From_0.001_to_0.01.png)

Figure 2: Log change in wealth distribution of bucket *From 0.001 to 0.01*



![Refer to caption](images/From_0.01_to_0.1.png)

Figure 3: Log change in wealth distribution of bucket *From 0.01 to 0.1*

![Refer to caption](images/From_0.1_to_1.png)

Figure 4: Log change in wealth distribution of bucket *From 0.1 to 1*



![Refer to caption](images/From_1_to_10.png)

Figure 5: Log change in wealth distribution of bucket *From 1 to 10*

![Refer to caption](images/From_10_to_100.png)

Figure 6: Log change in wealth distribution of bucket *From 10 to 100*



![Refer to caption](images/From_100_to_1000.png)

Figure 7: Log change in wealth distribution of bucket *From 100 to 1000*

![Refer to caption](images/From_1000_to_10000.png)

Figure 8: Log change in wealth distribution of bucket *From 1000 to 10000*



![Refer to caption](images/From_10000_to_100000.png)

Figure 9: Log change in wealth distribution of bucket *From 10000 to 100000*

![Refer to caption](images/From_100000_to_infinity.png)

Figure 10: Log change in wealth distribution of bucket *From 100000 to infinity*

## Appendix B Global Linear Regression (p-values)

Hint: Asterisk and cell shading highlight the p-values below the chosen critical level of 5%5\%.

|  | From 0 to 0.001 | From 0.001 to 0.01 | From 0.01 to 0.1 | From 0.1 to 1 | From 1 to 10 |
| --- | --- | --- | --- | --- | --- |
| Bitcoin (Close Price) | 0.95552 | 0.05879 | 0.11609 | 0.39121 | 0.2371 |
| Gold Price Against USD | 0.78693 | 0.77605 | 0.17878 | 0.24755 | 0.75837 |
| |  | | --- | | 20 Year GILTs | | (Nominal Zero Coupon Yield) | | 0.03687∗0.03687^{\ast} | 0.33783 | 0.8859 | 0.67275 | 0.73541 |
| |  | | --- | | 10 Year GILTs | | (Nominal Zero Coupon Yield) | | 0.83118 | 0.30361 | 0.10171 | 0.14961 | 0.3184 |
| |  | | --- | | 5 Year GILTs | | (Nominal Zero Coupon Yield) | | 0.30856 | 0.96274 | 0.78562 | 0.79379 | 0.89922 |
| |  | | --- | | 20 Year GILTs | | (Nominal Par Yield) | | 0.68882 | 0.84201 | 0.80301 | 0.71128 | 0.49422 |
| |  | | --- | | 10 Year GILTs | | (Nominal Par Yield) | | 0.47746 | 0.65285 | 0.33442 | 0.58821 | 0.51561 |
| |  | | --- | | 5 Year GILTs | | (Nominal Par Yield) | | 0.57838 | 0.0172∗0.0172^{\ast} | 0.48107 | 0.24873 | 0.07603 |
| |  | | --- | | Producer Price Index | | (Semiconductors and | | Electronic Components) | | 0.59451 | 0.97032 | 0.57565 | 0.59474 | 0.71034 |
| |  | | --- | | 30 Year High Quality Market | | Corporate Bond Spot Rate | | 0.90286 | 0.75138 | 0.41004 | 0.24977 | 0.70001 |
| |  | | --- | | 10 Year High Quality Market | | Corporate Bond Spot Rate | | 0.75744 | 0.50603 | 0.79627 | 0.31648 | 0.85344 |
| |  | | --- | | 5 Year High Quality Market | | Corporate Bond Spot Rate | | 0.12468 | 0.4359 | 0.36901 | 0.74853 | 0.44947 |
| |  | | --- | | 30 Year High Quality Market | | Corporate Bond Par Yield | | 0.0981 | 0.35661 | 0.55473 | 0.73128 | 0.33157 |
| |  | | --- | | 10 Year High Quality Market | | Corporate Bond Par Yield | | 0.34237 | 0.4497 | 0.25276 | 0.67013 | 0.16626 |
| |  | | --- | | 5 Year High Quality Market | | Corporate Bond Par Yield | | 0.88041 | 0.58471 | 0.61756 | 0.21268 | 0.59216 |
| Unemployment Rate (US) | 0.83498 | 0.07568 | 0.72303 | 0.76021 | 0.06659 |
| Consumer Price Index (US) | 0.65166 | 0.89672 | 0.72195 | 0.88553 | 0.91983 |
| |  | | --- | | Market Value of Privately Held | | Gross Federal Debt | | 0.96968 | 0.81238 | 0.91815 | 0.70745 | 0.94792 |
| |  | | --- | | Market Value of | | Gross Federal Debt | | 0.11826 | 0.23086 | 0.10521 | 0.39906 | 0.10054 |
| M2 (US) | 0.79448 | 0.24604 | 0.46469 | 0.20304 | 0.86395 |
| M1 (US) | 0.99723 | 0.28262 | 0.32516 | 0.11052 | 0.33234 |
| Nonfarm Payroll (US) | 0.84165 | 0.04645∗0.04645^{\ast} | 0.70288 | 0.73462 | 0.04578∗0.04578^{\ast} |
| Personal Current Taxes (US) | 0.06454 | 0.12047 | 0.36148 | 0.52582 | 0.57357 |
| Federal Funds Rate | 0.01864∗0.01864^{\ast} | 0.91238 | 0.80898 | 0.98497 | 0.10087 |

|  | From 10 to 100 | From 100 to 1000 | From 1000 to 10000 | From 10000 to 100000 | From 100000 to infinity |
| --- | --- | --- | --- | --- | --- |
| Bitcoin (Close Price) | 0.93867 | 0.46682 | 0.70236 | 0.21032 | 0.80568 |
| Gold Price Against USD | 0.76503 | 0.68464 | 0.07651 | 0.6149 | 0.68218 |
| |  | | --- | | 20 Year GILTs | | (Nominal Zero Coupon Yield) | | 0.51814 | 0.43059 | 0.80933 | 0.34878 | 0.40557 |
| |  | | --- | | 10 Year GILTs | | (Nominal Zero Coupon Yield) | | 0.89177 | 0.69377 | 0.2441 | 0.28757 | 0.90289 |
| |  | | --- | | 5 Year GILTs | | (Nominal Zero Coupon Yield) | | 0.35175 | 0.68574 | 0.38014 | 0.59197 | 0.22758 |
| |  | | --- | | 20 Year GILTs | | (Nominal Par Yield) | | 0.01138∗0.01138^{\ast} | 0.30415 | 0.25454 | 0.82128 | 0.39393 |
| |  | | --- | | 10 Year GILTs | | (Nominal Par Yield) | | 0.64698 | 0.46399 | 0.63107 | 0.59572 | 0.19319 |
| |  | | --- | | 5 Year GILTs | | (Nominal Par Yield) | | 0.4147 | 0.17991 | 0.80825 | 0.44746 | 0.64333 |
| |  | | --- | | Producer Price Index | | (Semiconductors and | | Electronic Components) | | 0.63546 | 0.19781 | 0.8154 | 0.42572 | 0.37454 |
| |  | | --- | | 30 Year High Quality Market | | Corporate Bond Spot Rate | | 0.57632 | 0.66095 | 0.43108 | 0.54761 | 0.36277 |
| |  | | --- | | 10 Year High Quality Market | | Corporate Bond Spot Rate | | 0.41708 | 0.56404 | 0.72565 | 0.26456 | 0.52256 |
| |  | | --- | | 5 Year High Quality Market | | Corporate Bond Spot Rate | | 0.16551 | 0.39963 | 0.96729 | 0.12264 | 0.52284 |
| |  | | --- | | 30 Year High Quality Market | | Corporate Bond Par Yield | | 0.37634 | 0.39991 | 0.51794 | 0.47668 | 0.62582 |
| |  | | --- | | 10 Year High Quality Market | | Corporate Bond Par Yield | | 0.62523 | 0.38101 | 0.28999 | 0.74516 | 0.42881 |
| |  | | --- | | 5 Year High Quality Market | | Corporate Bond Par Yield | | 0.83063 | 0.65482 | 0.03731∗0.03731^{\ast} | 0.85632 | 0.50252 |
| Unemployment Rate (US) | 0.52021 | 0.58443 | 0.64602 | 0.09818 | 0.92865 |
| Consumer Price Index (US) | 0.20949 | 0.89747 | 0.02143∗0.02143^{\ast} | 0.43401 | 0.63789 |
| |  | | --- | | Market Value of Privately Held | | Gross Federal Debt | | 0.33362 | 0.16659 | 0.06504 | 0.55106 | 0.95536 |
| |  | | --- | | Market Value of | | Gross Federal Debt | | 0.57143 | 0.61409 | 0.95303 | 0.59789 | 0.01417∗0.01417^{\ast} |
| M2 (US) | 0.02234∗0.02234^{\ast} | 0.63307 | 0.89056 | 0.16755 | 0.57691 |
| M1 (US) | 0.91529 | 0.43484 | 0.97615 | 0.07317 | 0.79659 |
| Nonfarm Payroll (US) | 0.52601 | 0.4809 | 0.80202 | 0.12235 | 0.84016 |
| Personal Current Taxes (US) | 0.72656 | 0.35213 | 0.12155 | 0.30312 | 0.88685 |
| Federal Funds Rate | 0.06506 | 0.30516 | 0.21317 | 0.87413 | 0.16522 |

## Appendix C BIPs Causality Analysis

True: Accept the assumption of Granger-causality

* •

  T (x): xx is the longest significant lag (in months) of the independent variable in the parent model in the Granger-causality test.

False: Reject the assumption of Granger-causality

* •

  F (a): Could not select a model with autoregressive terms of the independent variable as all models have infinite Akaike information criterion.
* •

  F (b): All autoregressive terms of the independent variable have been filtered out as insignificant according to the t-test.
* •

  F (c): Autoregressive terms of the independent variable do not add explanatory power according to the F-test.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Simple Test, All BIPs | Simple Test, All Economy-Related BIPs | Simple Test, Major Economy-Related BIPs | Simple Test, All Economy-Related BIPs (Except the major ones) | Full Test, All BIPs | Full Test, All Economy-Related BIPs | Full Test, Major Economy-Related BIPs | Full Test, All Economy-Related BIPs (Except the major ones) |
| From 0 to 0.001 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |
| From 0.001 to 0.01 | F (c) | F (c) | T (10) | F (c) | F (b) | F (b) | T (3) | F (b) |
| From 0.01 to 0.1 | F (c) | F (c) | T (10) | F (c) | F (b) | F (b) | T (10) | F (b) |
| From 0.1 to 1 | F (c) | F (c) | T (10) | F (c) | F (b) | F (b) | T (1) | F (b) |
| From 1 to 10 | F (c) | F (c) | T (10) | F (c) | F (b) | F (b) | F (b) | F (b) |
| From 10 to 100 | F (c) | F (c) | F (c) | T (10) | F (b) | F (b) | F (b) | F (b) |
| From 100 to 1000 | F (c) | F (c) | T (10) | F (c) | F (b) | F (b) | F (c) | F (b) |
| From 1000 to 10000 | F (c) | F (c) | F (c) | F (c) | F (b) | T (3) | F (b) | T (3) |
| From 10000 to 100000 | F (c) | T (10) | F (c) | T (10) | F (b) | T (6) | F (b) | T (6) |
| From 100000 to infinity | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |

## Appendix D BIPs Causality Analysis (6 months)

True: Accept the assumption of Granger-causality

* •

  T (x): xx is the longest significant lag (in months) of the independent variable in the parent model in the Granger-causality test.

False: Reject the assumption of Granger-causality

* •

  F (a): Could not select a model with autoregressive terms of the independent variable as all models have infinite Akaike information criterion.
* •

  F (b): All autoregressive terms of the independent variable have been filtered out as insignificant according to the t-test.
* •

  F (c): Autoregressive terms of the independent variable do not add explanatory power according to the F-test.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Simple Test, All BIPs | Simple Test, All Economy-Related BIPs | Simple Test, Major Economy-Related BIPs | Simple Test, All Economy-Related BIPs (Except the major ones) | Full Test, All BIPs | Full Test, All Economy-Related BIPs | Full Test, Major Economy-Related BIPs | Full Test, All Economy-Related BIPs (Except the major ones) |
| From 0 to 0.001 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |
| From 0.001 to 0.01 | F (c) | F (c) | T (6) | F (c) | F (b) | F (b) | T (3) | F (b) |
| From 0.01 to 0.1 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | T (6) | F (b) |
| From 0.1 to 1 | F (c) | F (c) | T (6) | F (c) | F (b) | F (b) | T (1) | F (b) |
| From 1 to 10 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |
| From 10 to 100 | F (c) | T (6) | F (c) | T (6) | F (b) | F (b) | F (b) | F (b) |
| From 100 to 1000 | F (c) | F (c) | T (6) | F (c) | F (b) | F (b) | F (c) | F (b) |
| From 1000 to 10000 | F (c) | F (c) | F (c) | F (c) | F (b) | T (3) | F (b) | T (3) |
| From 10000 to 100000 | F (c) | F (c) | F (c) | F (c) | F (c) | T (1) | T (3) | T (1) |
| From 100000 to infinity | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |

## Appendix E BIPs Causality Analysis (12 months)

True: Accept the assumption of Granger-causality

* •

  T (x): xx is the longest significant lag (in months) of the independent variable in the parent model in the Granger-causality test.

False: Reject the assumption of Granger-causality

* •

  F (a): Could not select a model with autoregressive terms of the independent variable as all models have infinite Akaike information criterion.
* •

  F (b): All autoregressive terms of the independent variable have been filtered out as insignificant according to the t-test.
* •

  F (c): Autoregressive terms of the independent variable do not add explanatory power according to the F-test.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Simple Test, All BIPs | Simple Test, All Economy-Related BIPs | Simple Test, Major Economy-Related BIPs | Simple Test, All Economy-Related BIPs (Except the major ones) | Full Test, All BIPs | Full Test, All Economy-Related BIPs | Full Test, Major Economy-Related BIPs | Full Test, All Economy-Related BIPs (Except the major ones) |
| From 0 to 0.001 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (c) |
| From 0.001 to 0.01 | F (c) | F (c) | T (12) | F (c) | F (b) | F (b) | T (3) | F (b) |
| From 0.01 to 0.1 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |
| From 0.1 to 1 | F (c) | F (c) | T (12) | F (c) | F (b) | F (b) | T (1) | F (b) |
| From 1 to 10 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |
| From 10 to 100 | F (c) | F (c) | F (c) | T (12) | F (b) | F (b) | F (b) | F (b) |
| From 100 to 1000 | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (c) | F (b) |
| From 1000 to 10000 | F (c) | F (c) | F (c) | F (c) | F (b) | T (3) | F (b) | T (3) |
| From 10000 to 100000 | F (c) | T (12) | F (c) | T (12) | F (c) | T (6) | F (b) | T (6) |
| From 100000 to infinity | F (c) | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) | F (b) |

## Appendix F Taxonomised BIPs Causality Analysis

True: Accept the assumption of Granger-causality

* •

  T (x): xx is the longest significant lag (in months) of the independent variable in the parent model in the Granger-causality test.

False: Reject the assumption of Granger-causality

* •

  F (a): Could not select a model with autoregressive terms of the independent variable as all models have infinite Akaike information criterion.
* •

  F (b): All autoregressive terms of the independent variable have been filtered out as insignificant according to the t-test.
* •

  F (c): Autoregressive terms of the independent variable do not add explanatory power according to the F-test.

|  | Simple Test, Fiscal-Like BIPs | Simple Test, Monetary-Like BIPs | Simple Test, Purely Tokenomic BIPs | Full Test, Fiscal-Like BIPs | Full Test, Monetary-Like BIPs | Full Test, Purely Tokenomic BIPs |
| --- | --- | --- | --- | --- | --- | --- |
| From 0 to 0.001 | F (c) | F (c) | F (c) | F (b) | F (b) | F (b) |
| From 0.001 to 0.01 | F (c) | T (10) | T (10) | F (b) | T (10) | F (b) |
| From 0.01 to 0.1 | F (c) | F (c) | F (c) | T (9) | F (b) | F (b) |
| From 0.1 to 1 | F (c) | T (10) | F (c) | F (b) | T (8) | T (5) |
| From 1 to 10 | T (10) | F (c) | T (10) | T (4) | F (b) | T (2) |
| From 10 to 100 | F (c) | T (10) | F (c) | F (b) | F (b) | F (b) |
| From 100 to 1000 | F (c) | F (c) | T (10) | F (b) | F (b) | T (7) |
| From 1000 to 10000 | T (10) | F (c) | F (c) | F (b) | F (b) | T (3) |
| From 10000 to 100000 | F (c) | F (c) | F (c) | T (5) | T (6) | T (1) |
| From 100000 to infinity | F (c) | T (10) | F (c) | F (b) | F (b) | F (b) |

## References

* [1]
   R. Sadykhov, G. Goodell, D. de Montigny, M. Schoernig and P. Treleaven, December 2023. *Decentralized Token Economy Theory (DeTEcT)*. DOI: <https://doi.org/10.3389/fbloc.2023.1298330>
* [2]
   R. Sadykhov, G. Goodell and P. Treleaven, January 2025. *DeTEcT: Dynamic and Probabilistic Parameters Extension*. DOI: <https://doi.org/10.3389/fbloc.2024.1448160>
* [3]
   R. Sadykhov, G. Goodell and P. Treleaven, July 2025. *Economic Policy Taxonomy*. DOI: <https://doi.org/10.48550/arXiv.2507.03233>
* [4]
   C.W.J. Granger, August 1969. *Investigating Causal Relations by Econometric Models and Cross-Spectral Methods*. DOI: <https://doi.org/10.2307/1912791>
* [5]
   *Wikipedia: Granger Causality*, January 15, 2026. <https://en.wikipedia.org/wiki/Granger_causality>
* [6]
   *Blockchain and Distributed Ledger Technologies - Vocabulary*, January 2023. DOI: <https://www.iso.org/obp/ui/#iso:std:iso:22739:dis:ed-2:v1:en>
* [7]
   *Bitcoin Improvement Proposals*. <https://github.com/bitcoin/bips>
* [8]
   *CCData API*. <https://developers.coindesk.com/documentation/data-api/introduction>, June 24, 2025.
* [9]
   FRED, Federal Bank of St. Louis. <https://fredhelp.stlouisfed.org>, June 24, 2025.
* [10]
   IADB, Bank of England Database. <https://www.bankofengland.co.uk/boeapps/database/>, June 25, 2025.
* [11]
   Yahoo! Finance. <https://uk.finance.yahoo.com/>, September 02, 2025.
* [12]
   DigiFi, General purpose financial library, version 3.0.5. <https://crates.io/crates/digifi>
* [13]
   Seabold, Skipper, and Josef Perktold. *statsmodels: Econometric and statistical modeling with python.* Proceedings of the 9th Python in Science Conference. 2010.
* [14]
   Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, CJ Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E.A. Quintero, Charles R Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. (2020) *SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python.* Nature Methods, 17(3), 261-272. DOI: <https://doi.org/10.1038/s41592-019-0686-2>.
* [15]
   Harris, C.R., Millman, K.J., van der Walt, S.J. et al. *Array programming with NumPy*. Nature 585, 357–362 (2020). DOI: <https://doi.org/10.1038/s41586-020-2649-2>.