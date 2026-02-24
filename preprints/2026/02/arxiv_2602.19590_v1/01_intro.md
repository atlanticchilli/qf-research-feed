---
authors:
- Ezra Goliath
- Tim Gebbie
doc_id: arxiv:2602.19590v1
family_id: arxiv:2602.19590
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Metaorder modelling and identification from public data
url_abs: http://arxiv.org/abs/2602.19590v1
url_html: https://arxiv.org/html/2602.19590v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ezra Goliath
[gltezr001@myuct.ac.za](mailto:gltezr001@myuct.ac.za)

Tim Gebbie
[tim.gebbie@uct.ac.za](mailto:tim.gebbie@uct.ac.za)
Department of Statistical Science, University of Cape Town, Rondebosch 7701, South Africa

###### Abstract

Market-order flow in financial markets exhibits long-range correlations. This is a widely known stylised fact of financial markets. A popular hypothesis for this stylised fact comes from the Lillo–Mike–Farmer (LMF) order-splitting theory. However, quantitative tests of this theory have historically relied on proprietary datasets with trader identifiers, limiting reproducibility and cross-market validation. We show that the LMF theory can be validated using publicly available Johannesburg Stock Exchange (JSE) data by leveraging recently developed methods for reconstructing synthetic metaorders. We demonstrate the validation using 3 years of Transaction and Quote Data (TAQ) for the largest 100 stocks on the JSE when assuming that there are either N=50 or N=150 effective traders managing metaorders in the market.

###### keywords:

LMF theory, metaorders, order-splitting, long-memory, auto-correlation function, power-law
  
Subject Areas: Econophysics, financial markets, agent-based modeling, electronic trading.

## 1 Introduction

Long-range autocorrelations (LRC) of market-order flow is a widely known macroscopic phenomenon of financial markets [[11](https://arxiv.org/html/2602.19590v1#bib.bib7 "The long memory of the efficient market"), [12](https://arxiv.org/html/2602.19590v1#bib.bib2 "Theory for long memory in supply and demand")]. The idea is that macroscopic phenomena in continuously traded double-auction intraday financial markets are predominantly due to the aggregated effects of microscopic actions i.e. the bottom-up aggregation of individual trades. This can be contrasted both with top-down causes such as market wide information shocks, or the coordinated actions of agents at the macro-economic level [[20](https://arxiv.org/html/2602.19590v1#bib.bib9 "Hierarchical causality in financial economics")] and prices that result for Walrusian like closing auctions.

One hypothesis is that LRC arise in the market-order flow due to the order-splitting behaviour of traders [[12](https://arxiv.org/html/2602.19590v1#bib.bib2 "Theory for long memory in supply and demand")]. The key microscopic contributor is then the aggregation of metaorders after they have been broken up and mixed in real markets. Even if the reason (or the cause) for the metaorders themselves is top-down from market actors operator at lower frequency at the level of mutual funds and macro-economic events. This top-down cause can be thought to come from some latent order-book [[19](https://arxiv.org/html/2602.19590v1#bib.bib8 "How does the market use information? evidence from the response of prices to trades")].

This idea then links the microscopic properties of trades directly to macroscopic averaged measurables; the trade-sign auto-correlations and the shape of the price impact. Such a direct link should be surprising if one places more value on exogenous information shocks, fundamental information, and general news flow, and then some sort of idea of predictability in stock market price changes themselves, rather then endogenous causes of dynamics and emergence.

Concretely, it was proposed that the decay exponent γ\gamma of the autocorrelation function (ACF) of the trade signs (say ϵ\epsilon) are directly related to the power-law exponent α\alpha of the probability of finding a metaorder of length LL through the relation: γ=α−1\gamma=\alpha-1 [[12](https://arxiv.org/html/2602.19590v1#bib.bib2 "Theory for long memory in supply and demand")].

This result is known as the LMF theory111That the probability of metaorders of length LL is P​(L)∝L−α−1P(L)\propto L^{-\alpha-1} for α>1\alpha>1, and the autocorrelations in the trade signs ϵ\epsilon are C​(τ)∝τ−γC(\tau)\propto\tau^{-\gamma} for a delay τ\tau such that γ=α−1\gamma=\alpha-1. and was initially argued via simulation, but was later empirically validated on the Tokyo Stock Exchange (TSE) [[16](https://arxiv.org/html/2602.19590v1#bib.bib12 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model"), [17](https://arxiv.org/html/2602.19590v1#bib.bib11 "Quantitative statistical analysis of order-splitting behavior of individual trading accounts in the japanese stock market over nine years")].

This validation is a remarkable and surprising result! The importance of this result has been discussed elsewhere [[13](https://arxiv.org/html/2602.19590v1#bib.bib10 "Decoding the dynamics of supply and demand"), [3](https://arxiv.org/html/2602.19590v1#bib.bib13 "The universal law behind market price swings")], but essentially it is a phenomenological law that explains the convexity of the price impact and hence the square-root law of the price impact of metaorders. It also supports a very specific microscopic cause for the key macroscopic universal features of intraday stock market dynamics and how the order-flow can be predictable even when the price changes are not.

Verification of the LMF theory on other markets following Sato and Kanazawa [[16](https://arxiv.org/html/2602.19590v1#bib.bib12 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model")] has proven to be difficult because of the need to acquire datasets that contain trader identification information and broker codes. These fields are required to be able to reconstruct the underlying metaorders from the market transaction and limit order update messages. Here a metaorder is a linked sequence of buy (or sell) orders +1​(−1)+1(-1) coming from a single agent operating in the market. There are then many such agents and hence many metaorders. We label the metaorders with index jj to refer to the jj-th metaorder Q(j)Q^{(j)} comprising of nn orders qi(j)q^{(j)}\_{i} for i∈[1:n]i\in[1:n]. A metaorder could be considered to represent the simplest type of trading schedule. The details of the parent order generating the metaorders are typically considered to be private and hence not made more generally available to researchers and market participants.

However, recent work on metaorder reconstruction using very simple distributional assumptions has proved to have been able to preserve key aggregate properties of financial markets [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]. Here we combined these two innovations to address the data issue and reverse engineer the individual trades to generate synthetic metaorders from publicly available Johannesburg Stock Exchange (JSE) data for the largest 100 stocks (Table [4](https://arxiv.org/html/2602.19590v1#S7.T4 "Table 4 ‣ 7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data")). This was carried out over a three year period, from 1 January 2023 to 31 December 2025 using trade by trade event data (See Appendix [7.1](https://arxiv.org/html/2602.19590v1#S7.SS1 "7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data")). The data includes only publicly available trades and order-book updates, and was sourced through the BMLL Data Lab platform [[2](https://arxiv.org/html/2602.19590v1#bib.bib17 "BMLL Data Lab Python Development Environment")].

In Section [2](https://arxiv.org/html/2602.19590v1#S2 "2 Data Description ‣ Metaorder modelling and identification from public data") we provide details about the data source and how the data was pre-processed. In Section [3](https://arxiv.org/html/2602.19590v1#S3 "3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") we describe how we have implemented the method of Maitrier et al. [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")], and then provide some of the missing algorithm details [[10](https://arxiv.org/html/2602.19590v1#bib.bib22 "Metaorder modelling and identification (github repository)")]. We explicitly provide two simple variants of the metaorder reconstruction method, and demonstrate how we have validated the metaorders.

In Section [4](https://arxiv.org/html/2602.19590v1#S4 "4 Testing the LMF theory ‣ Metaorder modelling and identification from public data") we validate the Lillo-Mike-Farmer theory [[12](https://arxiv.org/html/2602.19590v1#bib.bib2 "Theory for long memory in supply and demand")] following the broad idea of Sato and Kanazawa [[16](https://arxiv.org/html/2602.19590v1#bib.bib12 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model")] but with the reconstructed metaorders following our implementation of the method of Maitrier et al. [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]. Part of the metaorder reconstruction method requires choosing the number of effective traders operating within the market, here for indicative purposes we choose: N=50N=50, and N=150N=150. The other part is making distributional assumptions about the metaorder themselves. The results are reasonably robust to a reasonable choice of both the number of traders and the distributional shape.

We then provide a brief conclusion in Section [5](https://arxiv.org/html/2602.19590v1#S5 "5 Conclusion ‣ Metaorder modelling and identification from public data"). The key result is that we have evidence of the Lillo et al. [[12](https://arxiv.org/html/2602.19590v1#bib.bib2 "Theory for long memory in supply and demand")] theory holding on the JSE despite using reconstructed orders. This suggest the metaorder recovery methods are reasonably robust in the volume regime that the LMF theory holds.

## 2 Data Description

The analyses are based on high-frequency Level 1 trade data, which provides the basic information for each executed trade, including the timestamp, traded price, traded volume, and trade direction (±1\pm 1 for buy and sell respectively). Cleaning and some pre-processing was done beforehand. Specifically, the mid-prices just before and just after the trades were included in the data sets.

The data extended from 1 January 2023 to 31 December 2025 for the assets in Table [4](https://arxiv.org/html/2602.19590v1#S7.T4 "Table 4 ‣ 7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") (See Section [7.1](https://arxiv.org/html/2602.19590v1#S7.SS1 "7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data")). Using the data, we were able to calculate the intraday volatility, daily volume, and mid-prices. This processed data was then used to generate the synthetic metaorders. Table [5](https://arxiv.org/html/2602.19590v1#S7.T5 "Table 5 ‣ 7.2 Sample of the processed data ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") in Section [7.2](https://arxiv.org/html/2602.19590v1#S7.SS2 "7.2 Sample of the processed data ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") has an example snippet of the data that was used.

To generate synthetic metaorders, we applied Algorithm [1](https://arxiv.org/html/2602.19590v1#alg1 "Algorithm 1 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"), which assigns trades to synthetic traders using a mapping function that preserves the chronological order of trades. This procedure requires specifying NN the number of synthetic traders, and the distribution of their trader participation, here either homogeneous or power-law. Using this ”mapping”, sequences of consecutive trades with the same sign for each synthetic trader are defined as metaorders and compiled using Algorithm [2](https://arxiv.org/html/2602.19590v1#alg2 "Algorithm 2 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). Table [6](https://arxiv.org/html/2602.19590v1#S7.T6 "Table 6 ‣ 7.3 Sample of data after applying algorithms 1 and 2 ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") in Section [7.3](https://arxiv.org/html/2602.19590v1#S7.SS3 "7.3 Sample of data after applying algorithms 1 and 2 ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") has an example snippet of the output from Algorithm [2](https://arxiv.org/html/2602.19590v1#alg2 "Algorithm 2 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").

These metaorders are subsequently used to study the square-root law of metaorder impact, the time independence of metaorder impact, the execution profile and the post execution profile.

## 3 Generating synthetic metaorders

Numerous attempts have been made to generate synthetic metaorders from public data. The validity and quality of these synthetic metaorders is tested by comparing their reproduced stylised facts to empirically proven stylised facts of metaorders. These stylised facts are [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]:

1. 1.

   The square root law (SQL) of metaorder impact,
2. 2.

   The time independence of metaorder impact,
3. 3.

   The concave profile of metaorder execution, and
4. 4.

   The post execution decay of metaorder impact.

The validation of these stylised facts are individually addressed in sections [3.2](https://arxiv.org/html/2602.19590v1#S3.SS2 "3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"), [3.3](https://arxiv.org/html/2602.19590v1#S3.SS3 "3.3 Time independence of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"), [3.4](https://arxiv.org/html/2602.19590v1#S3.SS4 "3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") and [3.5](https://arxiv.org/html/2602.19590v1#S3.SS5 "3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") below. First, we will discuss the metaorder generating algorithm of Maitrier et al. [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")] in Section [3.1](https://arxiv.org/html/2602.19590v1#S3.SS1 "3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").

### 3.1 The metaorder generating algorithms

Previous attempts have failed to reproduce all the stylised facts of metaorders. As far as we know, the only method that can generate metaorders which reproduce all stylised facts is the one proposed in [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]. Their algorithm uses a mapping function to assign trades to a predetermined number of traders while maintaining chronological order of the the trades.

Algorithm 1  Mapping Function

1:Number of traders NN and trader participation distribution FF

2:Trades are assigned according to participation weights pjp\_{j} for the jj-th trader:

3:Draw fj∼Ff\_{j}\sim F for j=1,…,Nj=1,\dots,N

4:Normalise frequencies:

|  |  |  |
| --- | --- | --- |
|  | pj=fj∑kfkp\_{j}=\frac{f\_{j}}{\sum\_{k}f\_{k}} |  |

5:Compute cumulative probabilities

|  |  |  |
| --- | --- | --- |
|  | cj=∑k=1jpkc\_{j}=\sum\_{k=1}^{j}p\_{k} |  |

with c0=0c\_{0}=0

6:for each order qiq\_{i} in the market do

7:  Draw a random variable U∼𝒰​(0,1)U\sim\mathcal{U}(0,1)

8:  Find the trader jj such that cj−1≤U<cjc\_{j-1}\leq U<c\_{j}

9:  Assign the trade to jj-th agent.

10:end for




Algorithm 2  Generation of Synthetic Metaorders

1:Cleaned public trade data for a given asset and trading day: trade volumes qℓq\_{\ell} and mℓm\_{\ell} mid-prices at order book events ℓ∈[1,L]\ell\in[1,L].

2:Set of synthetic metaorders: {qi(j)}i=1nj\{q^{(j)}\_{i}\}\_{i=1}^{n\_{j}}.

3:Compute daily traded volume: ℓ∈[1,L]\ell\in[1,L].:

|  |  |  |
| --- | --- | --- |
|  | VD=∑ℓ=1LqℓV\_{D}=\sum\_{\ell=1}^{L}q\_{\ell} |  |

4:Compute the intraday volatility:

|  |  |  |
| --- | --- | --- |
|  | σD=mmax−mminmopen,\sigma\_{D}=\frac{m\_{\max}-m\_{\min}}{m\_{\mathrm{open}}}, |  |

using the maximum: mmaxm\_{\max}, minimum: mminm\_{\min}, and first mid-price: mopenm\_{\mathrm{open}}, of the day.

5:Apply the Mapping Function (Algorithm [1](https://arxiv.org/html/2602.19590v1#alg1 "Algorithm 1 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data")) to assign each trade to a synthetic trader while maintaining chronological order.

6:Sort trades by trader and timestamp

7:Define the jj-th metaorder as a sequence of trades with the same trade sign (from the same trader): {qi(j)}i=1nj\{q^{(j)}\_{i}\}\_{i=1}^{n\_{j}}

8:Compute features of metaorder:

1. 6.1

   log mid-prices just before: ln⁡(m0(j))\ln(m^{(j)}\_{0}),
2. 6.2

   number of child orders: njn\_{j}
3. 6.3

   log mid-prices just after: ln⁡(mnj+1(j))\ln(m^{(j)}\_{n\_{j}+1})
4. 6.4

   total traded volume of the metaorder: Q(j)Q^{(j)}
5. 6.5

   execution duration: TjT\_{j}
6. 6.6

   any other relevant quantities.

9:Aggregate metaorder statistics

10:Only return those with more than 1 child order

We have used both homogeneous: f≡f0f\equiv f\_{0}, and power-law: P​(f)∝f−δP(f)\propto f^{-\delta}, distributions for our trader participation distributions. The homogeneous distribution was defined such that f1=f2=⋯=fNf\_{1}=f\_{2}=\dots=f\_{N}. Samples from the power-law were obtained using inverse transform sampling. Our implementation of this algorithm allows us to specify a minimum and maximum number of trades that a trader can have, and the power-law exponent δ\delta. We have set default values of minimum = 1, maximum = total number of trades for the day and δ=2\delta=2.

Algorithm [2](https://arxiv.org/html/2602.19590v1#alg2 "Algorithm 2 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") generates the synthetic metaorders from public TAQ data. The assignment of trades to specific traders is controlled by Algorithm [1](https://arxiv.org/html/2602.19590v1#alg1 "Algorithm 1 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). It is critically important that trades remain in chronological order and that the mapping is unique. Once a trade is assigned to a trader, it cannot be assigned to a different trader as well. This corresponds to sampling without repetition [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")].

In real markets, trader activity distributions are well approximated by power-laws [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]. However, the precise distribution and the optimal number of traders NN to generate the synthetic metaorders are not known a priori. To account for this uncertainty, we generate metaorders using both homogeneous and power-law trader participation distributions, as well as multiple values of NN. This gives us a crude understanding of how the different trader participation distributions and different NN values affect the quality of the metaorders.

### 3.2 The Square Root Law

Given the jj-th metaorder made up of njn\_{j} trades, we define the total executed volume of the metaorder as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q(j)=∑i=1njqi(j).Q^{(j)}=\sum\_{i=1}^{n\_{j}}q^{(j)}\_{i}. |  | (1) |

where qi(j)q^{(j)}\_{i} is the volume of the ii-th trade of metaorder jj. The measured price impact of the metaorder is computed from change in the limit-order book induced by the transactions resulting from the metaorder and measured by the change in the mid-price from the start to the end of the metaorder:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(Q(j))=ϵ(j)×(ln⁡(mnj+1(j))−ln⁡(m0(j))).I(Q^{(j)})=\epsilon^{(j)}\times\left(\ln(m^{(j)}\_{n\_{j}+1})-\ln(m^{(j)}\_{0})\right). |  | (2) |

Here mnj+1m\_{n\_{j}+1} is the mid-price just after the metaorder ends, m0m\_{0} is the mid-price just before the metaorder starts and ϵ\epsilon is the trade sign of the metaorder where j∈[1,N]j\in[1,N], for the N traders to index the trade schedule from Equation [1](https://arxiv.org/html/2602.19590v1#S3.E1 "Equation 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").

The SQL states that the price change induced by a large metaorder of volume QQ is proportional to Q\sqrt{Q} [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]. The theoretical price impact of metaorders is given as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(Q)=Y​σD​QVD,I(Q)=Y\sigma\_{D}\sqrt{\frac{Q}{V\_{D}}}, |  | (3) |

where QQ is the total volume traded in the metaorder, VDV\_{D} is the daily traded volume, σD\sigma\_{D} is the intraday volatility222We used a 20 day moving average for both VDV\_{D} and σD\sigma\_{D} and YY is a prefactor [[18](https://arxiv.org/html/2602.19590v1#bib.bib4 "Anomalous price impact and the critical nature of liquidity in financial markets")]. Here for notational convenience we have dropped the metaorder and trader label; this is implicit in its definition.

![Refer to caption](x1.png)


((a)) GRT and GFI

![Refer to caption](x2.png)


((b)) Top 100 stocks

Figure 1: SQL for (a) GRT and GFI displayed individually and (b) all the stocks in the top 100 stocks compiled into a single line with the theoretical SQL given in red. In both cases a homogeneous distribution was used for the trader participation with the number of traders set to 4.

Figure [1](https://arxiv.org/html/2602.19590v1#S3.F1 "Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") is a log-log plot of metaorder impact for two stocks (Figure [1(a)](https://arxiv.org/html/2602.19590v1#S3.F1.sf1 "Figure 1(a) ‣ Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data")) and for the top 100 stocks (Figure [1(b)](https://arxiv.org/html/2602.19590v1#S3.F1.sf2 "Figure 1(b) ‣ Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data")) with the theoretical SQL given in red. Metaorders were generated by specifying 4 traders and a homogeneous trader participation distribution333The mapping function requires us to specify the number of traders and trader distribution apriori. Check Section [3.1](https://arxiv.org/html/2602.19590v1#S3.SS1 "3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") for details on the mapping function and metaorder generating algorithm.. The figure was created by first binning by Q/VDQ/V\_{D} into 40 equally spaced bins in the logarithmic space and then taking the bin centers as the xx domain values. The range, yy value for each bin was then taken to be the the average metaorder impact of the observations in that bin.

Figure [1(a)](https://arxiv.org/html/2602.19590v1#S3.F1.sf1 "Figure 1(a) ‣ Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the metaorder impact for GFI (a more liquid stock) and GRT (a less liquid stock). From this figure it is clear that the impact curve for GRT lies above the impact curve for GFI. This indicates that for an equal relative order size Q/VDQ/V\_{D}, the metaorder impact of GRT is larger than for GFI. This is a consequence of lower liquidity in GRT. Despite this, for Q/VD∈[10−3.5,10−1.5]Q/V\_{D}\in[10^{-3.5},10^{-1.5}] we see that GRT obeys the SQL and for Q/VD∈[10−5,10−2.5]Q/V\_{D}\in[10^{-5},10^{-2.5}] GFI obeys the SQRL. Values outside of these approximate intervals are noise relative to the hypothesis with smaller trades exceeding the SQL fit and larger trades having lower impact than the fitted SQL.

Figure [1(b)](https://arxiv.org/html/2602.19590v1#S3.F1.sf2 "Figure 1(b) ‣ Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the metaorder impact curve for all stocks in the top 100 compiled into a single curve by doing the binning procedure for all stocks together instead of separately. From this figure it is clear that the overall metaorder impact of the top 100 stocks obeys the SQL for Q/VD∈[10−4,100.5]Q/V\_{D}\in[10^{-4},10^{0.5}] when normalised for the different intraday volatilities444This suggests two different normalisation procedures, first by relative volatility, the other, using the ADV to shift the price impact.. We again see divergence from the theoretical SQL outside of this range but this is again due to noise.

### 3.3 Time independence of metaorder impact

It has been shown that metaorder impact is independent of metaorder duration TT [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")].

Figure [2](https://arxiv.org/html/2602.19590v1#S3.F2 "Figure 2 ‣ 3.3 Time independence of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the independence of metaorder impact with respect to TT for GFI and GRT. A histogram of the metaorder durations is given in grey and the normalised impact is overlayed. Metaorders were once again generated by specifying 4 traders and a homogeneous trader participation distribution. The x axis is logarithmically scaled.

Given the logarithmically scaled x axis, it is clear that the impact remains relatively flat as TT increases. This indicates approximate independence between the impact and TT. Both subfigures show long left tails with short right tails, indicating far more metaorders with short TT’s compared to long TT’s. Figure [2(a)](https://arxiv.org/html/2602.19590v1#S3.F2.sf1 "Figure 2(a) ‣ Figure 2 ‣ 3.3 Time independence of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") specifically has a fatter tail than Figure [2(b)](https://arxiv.org/html/2602.19590v1#S3.F2.sf2 "Figure 2(b) ‣ Figure 2 ‣ 3.3 Time independence of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") which could be indicative of more algorithmic and high frequency trading occcuring for GFI.

![Refer to caption](x3.png)


((a)) GFI

![Refer to caption](x4.png)


((b)) GRT

Figure 2: Approximate independence of metaorder impact with respect to the duration of the metaorder for (a) GFI (more liquid) and (b) GRT (less liquid). Majority of metaorders have a duration between 1 and 30 minutes.

### 3.4 The concave profile of metaorder impact

So far we have only investigated the impact of entire metaorders, now we investigate the impact of individual trades inside each metaorder. An analysis of 400 000 metaorders showed that there are two stages of metaorder impact, the concave profile during execution and the convex decay after execution [[1](https://arxiv.org/html/2602.19590v1#bib.bib5 "Market impacts and the life cycle of investors orders")]. For now we will investigate the concave profile during metaorder execution.

We take the the theoretical price impact profile during metaorder execution to be:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(ϕ×Q)=ϕ​I​(Q),I(\phi\times Q)=\sqrt{\phi}I(Q), |  | (4) |

where ϕ∈[0,1]\phi\in[0,1] is the fraction of the total metaorder volume that has been executed. ϕ=0\phi=0 at the start of the metaoder and ϕ=1\phi=1 by the end of the metaorder. More concretely, ϕ=∑i=1nqi/Q\phi=\sum\_{i=1}^{n}q\_{i}/Q and qiq\_{i} is the volume traded in a single child order of a metaorder of volume QQ [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")].

Since all the metaorders have different durations, we use ϕ\phi as a volume based measure of time. This has the desired effect of standardising the duration to a unit long window([0,1][0,1]). We also scale the price impact by 1/σD​Q1/\sigma\_{D}\sqrt{Q} to normalise the impact. Doing this changes the theoretical price impact profile to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(ϕ×Q)σD​Q=ϕ×I​(Q)σD​Q\frac{I(\phi\times Q)}{\sigma\_{D}\sqrt{Q}}=\sqrt{\phi}\times\frac{I(Q)}{\sigma\_{D}\sqrt{Q}} |  | (5) |

We measured the impact profile of a metaorder as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(ϕ×Q)=ϵ×(ln⁡(mi+1)−ln⁡(m0))I(\phi\times Q)=\epsilon\times(\ln(m\_{i+1})-\ln(m\_{0})) |  | (6) |

where m0m\_{0} is the mid-price just before the metaorder begins and mi+1m\_{i+1} is the mid-price just after execution of the it​hi^{th} child order. This is measured for each child order in a metaorder.

![Refer to caption](x5.png)


((a)) GFI

![Refer to caption](x6.png)


((b)) GRT

Figure 3: Concave profile of metaorder impact. The dynamic impact is plotted as a function of ϕ\phi, the proportion of the metaorder which has been executed, for (a) GFI (more liquid) and (b) GRT (less liquid). Metaorders were generated by specifying 20 traders and a power-law trader participation distribution with δ=2\delta=2. Only metaorders with 10 or more child orders were used for this analysis. The fitted curves are shown in red. See Table [1](https://arxiv.org/html/2602.19590v1#S3.T1 "Table 1 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") for the fitted profiles for GFI and GRT respectively using Equation [7](https://arxiv.org/html/2602.19590v1#S3.E7 "Equation 7 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").



|  |  |  |  |
| --- | --- | --- | --- |
| Description | Ticker | γ1\gamma\_{1} [×10−4][\times 10^{-4}] | γ2\gamma\_{2} |
| Gold Fields Ltd. | GFI | 9.79 ±\pm 0.20 | 1.001 ±\pm 0.044 |
| Growthpoint Ltd. | GRT | 4.54 ±\pm 0.14 | 0.766 ±\pm 0.057 |

Table 1: Fitted values for metaorder execution profiles of GFI and GRT for the scaling factor γ1\gamma\_{1}, and the exponent γ2\gamma\_{2} from Equation [7](https://arxiv.org/html/2602.19590v1#S3.E7 "Equation 7 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). These are the fits for Figure [3(a)](https://arxiv.org/html/2602.19590v1#S3.F3.sf1 "Figure 3(a) ‣ Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") for GFI and Figure [3(b)](https://arxiv.org/html/2602.19590v1#S3.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") for GRT.

Figure [3](https://arxiv.org/html/2602.19590v1#S3.F3 "Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the impact profile during execution of the metaorders for GFI and GRT with the fitted curve of the profile shown in red. Metaorders were generated by specifying 20 traders and a power-law trader participation distribution with δ=2\delta=2. Only metaorders with 10 or more child orders were used for this analysis. It was assumed that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(ϕ×Q)σD​Q=γ1×ϕγ2.\frac{I(\phi\times Q)}{\sigma\_{D}\sqrt{Q}}=\gamma\_{1}\times\phi^{\gamma\_{2}}. |  | (7) |

Here ϕ\phi is still the fraction of the measured metaorder as in Equation [4](https://arxiv.org/html/2602.19590v1#S3.E4 "Equation 4 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). Numerical optimisation555curve\_fit was used for the optimisation, this uses non-linear least squares to fit a curve to the data. was used to estimate the values of γ1,2\gamma\_{1,2}. The values reported in Table [1](https://arxiv.org/html/2602.19590v1#S3.T1 "Table 1 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") are point estimates with the 95% wald confidence interval half widths. The plots were made by binning ϕ\phi and using the mean dynamic impact of each bin as the representative y value.

From Figure [3(b)](https://arxiv.org/html/2602.19590v1#S3.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") and Table [1](https://arxiv.org/html/2602.19590v1#S3.T1 "Table 1 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") we notice that for GRT the metaorders are on average with concave execution profiles. The parameter estimate of γ2\gamma\_{2} for GRT is 0.77±0.060.77\pm 0.06, indicating that there is indeed concavity in the execution profile. The concavity is however less than the theoretical, which proposed a γ2\gamma\_{2} value of 0.50.5. Similarly, the parameter estimate of the scaling factor γ1=4.5±0.1×10−4\gamma\_{1}=4.5\pm 0.1\times 10^{-4} which is quite similar to the actual peak dynamic impact value near 5.0×10−45.0\times 10^{-4}. This matches the theory which proposed a scaling factor equal to the peak impact.

However, while the execution profile for GRT is concave, Figure [3(b)](https://arxiv.org/html/2602.19590v1#S3.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows that the execution profile for GFI lacks the characteristic concavity that we expect from real metaorders. Table [1](https://arxiv.org/html/2602.19590v1#S3.T1 "Table 1 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") indicates that the parameter estimate of γ2\gamma\_{2} is approximately unity, which is linear. This result is likely due to an improper specification of the number of traders NN and highlights the need for stock specific tuning when using this method of synthetic metaorder generation.

### 3.5 Post metaorder execution impact decay

Next, we investigate the convex decay of price impact after execution of the metaorder. Using the same theoretical impact decay function as [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(Q,z)=I​(Q)​(z1−β−(z−1)1−β)I(Q,\penalty 10000\ z)=I(Q)\left(z^{1-\beta}-\left(z-1\right)^{1-\beta}\right) |  | (8) |

and scaling by 1/σD​Q1/\sigma\_{D}\sqrt{Q}, we get a new theoretical decay function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(Q,z)σD​Q=I​(Q)σD​Q×(z1−β−(z−1)1−β)\frac{I(Q,\penalty 10000\ z)}{\sigma\_{D}\sqrt{Q}}=\frac{I(Q)}{\sigma\_{D}\sqrt{Q}}\times\left(z^{1-\beta}-\left(z-1\right)^{1-\beta}\right) |  | (9) |

where z=tT≥1z=\frac{t}{T}\geq 1 is rescaled time. tt is the time since the start of the metaoder i.e\it i.e, t=0t=0 corresponds to the start of the metaorder, t=Tt=T corresponds to the end of the metaorder and t>Tt>T is after the metaoder. TT is once again the duration of the metaorder. Both tt and TT were measured in minutes.

![Refer to caption](x7.png)


Figure 4: Convex post execution decay of impact for GRT. Dynamic impact is plotted as a function of zz, the rescaled time. Metaorders were generated by specifying 20 traders and a power-law trader participation distribution with δ=2\delta=2. The fitted line is shown in red.

Figure [4](https://arxiv.org/html/2602.19590v1#S3.F4 "Figure 4 ‣ 3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the observed impact decay for metaorders generated from GRT. The metaorders were once again generated by specifying 20 traders, a power-law trader participation distribution with δ=2\delta=2 and only including metaorders with 10 or more child orders. The plot was produced by binning zz values and using the mean dynamic impact of each bin as the representative y value.

From the Figure, it is clear that there is more noise compared to the execution profile(Figure [3(b)](https://arxiv.org/html/2602.19590v1#S3.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data")). However, assuming a relation of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(Q,z)σD​Q=γ0×(z1−β−(z−1)1−β)\frac{I(Q,\penalty 10000\ z)}{\sigma\_{D}\sqrt{Q}}=\gamma\_{0}\times\left(z^{1-\beta}-\left(z-1\right)^{1-\beta}\right) |  | (10) |

we were still able to find estimates of the prefactor δ\delta and for β\beta. Table [2](https://arxiv.org/html/2602.19590v1#S3.T2 "Table 2 ‣ 3.6 Validation of the synthetic metaorders ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") reports the point estimates along with the half widths of a 95% wald confidence interval. The estimated value for β\beta was found to be 0.2410.241. This result closely matches the result of β=0.19\beta=0.19 obtained in [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")] which used synthetic metaorders, and matches even more closely to the β=0.22\beta=0.22 result obtained in [[4](https://arxiv.org/html/2602.19590v1#bib.bib21 "Slow decay of impact in equity markets")] which used real metaorders. We also recovered a γ0=5.01±0.2×10−4\gamma\_{0}=5.01\pm 0.2\times 10^{-4} which matches the observed peak dynamic impact near 5×10−45\times 10^{-4}. This result is accordance with the theory which suggests a prefactor of I​(Q)σD​Q\frac{I(Q)}{\sigma\_{D}\sqrt{Q}}. Check Equation [9](https://arxiv.org/html/2602.19590v1#S3.E9 "Equation 9 ‣ 3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").

### 3.6 Validation of the synthetic metaorders

We have shown that the synthetic metaorders we have generated do indeed reproduce the key stylised facts of metaorders, namely, the square-root law, time independence of impact, concave execution profile and the convex impact decay. This suggests that algorithm [1](https://arxiv.org/html/2602.19590v1#alg1 "Algorithm 1 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") and [2](https://arxiv.org/html/2602.19590v1#alg2 "Algorithm 2 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") capture the dynamics of market activity and as such, allow us to use these synthetic metaorders to investigate the LMF theory.

|  |  |  |  |
| --- | --- | --- | --- |
| Description | Ticker | γ0\gamma\_{0} [×10−4][\times 10^{-4}] | β\beta |
| Growthpoint Ltd. | GRT | 5.01 ±\pm 0.194 | 0.241 ±\pm 0.033 |

Table 2: Fitted values for metaorder post execution impact decay for GRT.

### 3.7 Example metaorder execution profile

Figure [3(b)](https://arxiv.org/html/2602.19590v1#S3.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the execution profile of all metaorders with 10 or more child orders when specifying 20 traders and a power-law trader participation distribution with δ=2\delta=2 for GRT. Table [1](https://arxiv.org/html/2602.19590v1#S3.T1 "Table 1 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") reports the fitted values of a curve of the form γ1×ϕγ2\gamma\_{1}\times\phi^{\gamma\_{2}} for both GRT and GFI. Specifically, γ2\gamma\_{2} for GRT was found to be 0.77±0.060.77\pm 0.06. It is therefore clear that, on average, the concavity of the execution profiles for GRT are much smaller than the theoretical, which suggests a γ2\gamma\_{2} value of 0.50.5 (square-root)[[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")].

A likely reason for this mismatch is due to a misspecification in the number of traders NN and the power-law exponent δ\delta. Nevertheless, Table [3](https://arxiv.org/html/2602.19590v1#S3.T3 "Table 3 ‣ 3.7 Example metaorder execution profile ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") and Figure [5](https://arxiv.org/html/2602.19590v1#S3.F5 "Figure 5 ‣ 3.7 Example metaorder execution profile ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") show the execution profile for a single metaorder from GRT when specifying 20 traders and a power-law trader distribution with δ=2\delta=2.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ii | ϕ\phi | mn+im\_{n+i} | I​(ϕ×Q)×10−4I(\phi\times Q)\times 10^{-4} | QQ |
| 1 | 0.03 | 1478.00 | 6.77 | 2500.00 |
| 2 | 0.22 | 1479.00 | 13.53 | 14559.00 |
| 3 | 0.37 | 1479.00 | 13.53 | 11652.00 |
| 4 | 0.38 | 1479.50 | 16.91 | 989.00 |
| 5 | 0.39 | 1479.50 | 16.91 | 254.00 |
| 6 | 0.50 | 1479.50 | 16.91 | 8700.00 |
| 7 | 0.53 | 1479.50 | 16.91 | 2266.00 |
| 8 | 0.56 | 1480.00 | 20.29 | 2100.00 |
| 9 | 0.65 | 1479.50 | 16.91 | 7455.00 |
| 10 | 0.83 | 1480.00 | 20.29 | 13724.00 |
| 11 | 1.00 | 1479.50 | 16.91 | 13181.00 |

Table 3: Example metaorder from GRT with 20 traders and a power-law trader participation distribution



![Refer to caption](x8.png)


((a)) Peak impact

![Refer to caption](x9.png)


((b)) Peak dynamic impact

Figure 5: The execution profiles of a single metaorder from GRT when using (a), the peak impact I​(Q)I(Q) and (b), when using the peak dynamic impact. Metaorders were generated by specifying 20 traders and a power-law trader participation distribution. The theoretical profiles are shown in red.

Table [3](https://arxiv.org/html/2602.19590v1#S3.T3 "Table 3 ‣ 3.7 Example metaorder execution profile ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the value of ϕ\phi, volume, mid price immediately after, and the impact profile of the individual child orders (check Equation [6](https://arxiv.org/html/2602.19590v1#S3.E6 "Equation 6 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") for details on how the impact profile was calculated.) of the metaorder. Figure [5](https://arxiv.org/html/2602.19590v1#S3.F5 "Figure 5 ‣ 3.7 Example metaorder execution profile ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows the execution profiles when using the peak impact I​(Q)I(Q) and when using the peak dynamic impact I​QσD​Q\frac{IQ}{\sigma\_{D}\sqrt{Q}}. The actual observed execution profile, while not perfectly aligned with the theoretical curve, does exhibit a similar level of concavity. This shows that there are metaorders which match the theoretical execution profile, but due to misspecification of the number of traders, the aggregate execution profile is flattened.

## 4 Testing the LMF theory

The Lillo-Mike-Farmer (LMF) theory provides a microscopic explanation for the long-range correlation (LRC) observed in market-order flow. Empirically, trade signs of market orders exhibit strong persistence. Specifically, autocorrelations in trade signs have a power-law decay in time-lag τ\tau.To show this, we start by first defining the autocorrelation as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^​(τ)≔∑ℓ=1Nϵ−τϵℓ​ϵℓ+τNϵ−τ,\hat{C}(\tau)\coloneq\sum\_{\ell=1}^{N\_{\epsilon}-\tau}\frac{\epsilon\_{\ell}\epsilon\_{\ell+\tau}}{N\_{\epsilon}-\tau}, |  | (11) |

where ϵℓ=±1\epsilon\_{\ell}=\pm 1 are the measured market order signs, NϵN\_{\epsilon} is the number of market orders. The LMF model attributes this macroscopic long memory to the microscopic behavior of order-splitting traders (STs) who divide large metaorders into sequences of smaller child orders of the same sign [[16](https://arxiv.org/html/2602.19590v1#bib.bib12 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model")].

### 4.1 Relationship between γ\gamma and α\alpha

The key assumption of the LMF model is that metaorder lengths LL follow a power-law distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(L)∼L−α−1,α>1,P(L)\sim L^{-\alpha-1},\quad\alpha>1, |  | (12) |

and that the presence of STs is sufficient to generate the observed LRC. Under the assumption of random order submissions by STs, the model predicts a simple quantitative relation between the microscopic exponent α\alpha and the macroscopic LRC exponent γ\gamma:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=α−1.\gamma=\alpha-1. |  | (13) |

This remarkable result connects a directly measurable macroscopic property of the market (the decay of order autocorrelations) to a microscopic property of trader behaviour (the distribution of metaorder sizes).

### 4.2 Empirical Estimation of α\alpha and γ\gamma

To test this prediction, we first classify traders into STs and random traders (RTs) using a strategy clustering procedure. Metaorder lengths LL are then extracted as consecutive sequences of same-sign orders from STs. Using the [Clauset et al.](https://arxiv.org/html/2602.19590v1#bib.bib3 "Power-law distributions in empirical data") method for power-law fitting, we estimate the exponent α\alpha for each stock in our dataset [[16](https://arxiv.org/html/2602.19590v1#bib.bib12 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model")]. Simultaneously, we compute the autocorrelation function of the market order signs and fit the decay to estimate γ\gamma using an unbiased estimator that corrects for finite-sample bias.

![Refer to caption](x10.png)


((a)) N = 50

![Refer to caption](x11.png)


((b)) N = 150

Figure 6: Scattered box plots between α−1\alpha-1 and γ\gamma with the median indicated in orange. (a) shows the results when using 50 traders with power-law trader distribution and (b) shows the result when using 150 traders with a power-law distribution. In both cases, δ=2\delta=2.

Figure [6](https://arxiv.org/html/2602.19590v1#S4.F6 "Figure 6 ‣ 4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data") shows the empirical relationship between α\alpha and γ\gamma for two sample scenarios: 50 traders with a power-law distribution of trading intensity and δ=2\delta=2 (Figure [6(a)](https://arxiv.org/html/2602.19590v1#S4.F6.sf1 "Figure 6(a) ‣ Figure 6 ‣ 4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data")) and 150 traders with power-law distribution of trading intensity with δ=2\delta=2 (Figure [6(b)](https://arxiv.org/html/2602.19590v1#S4.F6.sf2 "Figure 6(b) ‣ Figure 6 ‣ 4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data")). The median of each bin is indicated in orange. As predicted by the LMF theory, the data points lie close to the line γ=α−1\gamma=\alpha-1, confirming that the long-range correlation of order signs is quantitatively explained by the distribution of metaorder lengths.

## 5 Conclusion

In Section [3](https://arxiv.org/html/2602.19590v1#S3 "3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") we have shown that we are able to generate synthetic metaorders from public TAQ data using the methods proposed by Maitrier et al. [[14](https://arxiv.org/html/2602.19590v1#bib.bib1 "Generating realistic metaorders from public data")]. Figure [1](https://arxiv.org/html/2602.19590v1#S3.F1 "Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows that the impact of the synthetic metaorders obey the square root law. In particular, Figure [1(b)](https://arxiv.org/html/2602.19590v1#S3.F1.sf2 "Figure 1(b) ‣ Figure 1 ‣ 3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows that the aggregated metaorder impact of all the stocks in the top 100 show remarkable obedience to the theoretical square root law. Figure [2](https://arxiv.org/html/2602.19590v1#S3.F2 "Figure 2 ‣ 3.3 Time independence of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows that the impact of the synthetic metaorders are independent of their durations. Figure [3](https://arxiv.org/html/2602.19590v1#S3.F3 "Figure 3 ‣ 3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows that the execution profile of the synthetic metaorders is concave, indicating that the impact is not linear in ϕ\phi. The impact is large initially, but tapers down as the metaorder nears completion. Figure [4](https://arxiv.org/html/2602.19590v1#S3.F4 "Figure 4 ‣ 3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") shows that post execution, the impact is non permanent and decays according to Equation [9](https://arxiv.org/html/2602.19590v1#S3.E9 "Equation 9 ‣ 3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). Together, these figures show that the synthetic metaorders are indeed realistic.

In Section [4](https://arxiv.org/html/2602.19590v1#S4 "4 Testing the LMF theory ‣ Metaorder modelling and identification from public data") we show that using the synthetic metaorders, we can recover the approximate relation γ=α−1\gamma=\alpha-1 that is proposed in [[12](https://arxiv.org/html/2602.19590v1#bib.bib2 "Theory for long memory in supply and demand")]. Figure [6](https://arxiv.org/html/2602.19590v1#S4.F6 "Figure 6 ‣ 4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data") shows the approximate relation we recover when using a power-law distribution with 50 traders(Figure [6(a)](https://arxiv.org/html/2602.19590v1#S4.F6.sf1 "Figure 6(a) ‣ Figure 6 ‣ 4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data")) and when using a power-law distribution with 150 trades(Figure [6(b)](https://arxiv.org/html/2602.19590v1#S4.F6.sf2 "Figure 6(b) ‣ Figure 6 ‣ 4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data")). These results are consistent with the results obtained by Sato and Kanazawa [[16](https://arxiv.org/html/2602.19590v1#bib.bib12 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model")] in which real metaorder data was used.

These results show that we can recover realistic synthetic metaorders from public TAQ data and then use those synthetic metaorders to show that there is a relationship between the long range correlation decay exponent γ\gamma, and the power-law exponent α\alpha, of the metaorder run lengths distribution.

The results are consistent with related agent-based modelling work where the metaorders were modelled as learnt TWAP strategies executed by multiple interacting reinforcement learning agents [[8](https://arxiv.org/html/2602.19590v1#bib.bib18 "Many learning agents interacting with an agent-based market model")], and then aggregated in a reactive agent-based model [[7](https://arxiv.org/html/2602.19590v1#bib.bib14 "A simple learning agent interacting with an agent-based market model")] (in particular their Figure 6). They demonstrate how the decay in the trade sign autocorrelations caused by metaorders mixing with other agents can be tuned to fit the empirical data while retaining little memory in the price fluctuations, and recover a square root price impact law and hence the required convexity in the price impact of orders.

This can then be shown to be consistent and recoverable using reaction-diffusion simulation methods [[6](https://arxiv.org/html/2602.19590v1#bib.bib16 "Non-uniformly sampled simulated price impact of an order-book")] following the latent order-book approach of Mastromatteo et al. [[15](https://arxiv.org/html/2602.19590v1#bib.bib19 "Agent-based models for latent liquidity and concave price impact")], Donier et al. [[9](https://arxiv.org/html/2602.19590v1#bib.bib20 "A fully consistent, minimal model for non-linear market impact")]. This both validates the centrality of metaorder flow in the generation of long-memory in financial markets, but also demonstrates what is necessary (and sufficient) for reasonably realistic simulations of financial markets beyond the sequential time and low-frequency regime typical of most older agent-based models.

## 6 Acknowledgements

We would like to thank Nasheen Sharma and Vuyo Mashiqa from the JSE, and the JSE for supporting the project. We thank Daniela Stevenson for suggestions and feedback.

## References

* [1]
  E. Bacry, A. Iuga, M. Lasnier, and C. Lehalle (2014)
  Market impacts and the life cycle of investors orders.
  External Links: 1412.0217,
  [Link](https://arxiv.org/abs/1412.0217)
  Cited by: [§3.4](https://arxiv.org/html/2602.19590v1#S3.SS4.p1.1 "3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").
* [2]
  BMLL Technologies (2026)
  BMLL Data Lab Python Development Environment.
  Note: Accessed: 2026-02-02
  External Links: [Link](https://www.bmlltech.com/)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p8.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§7.2](https://arxiv.org/html/2602.19590v1#S7.SS2.p1.1 "7.2 Sample of the processed data ‣ 7 Appendix ‣ Metaorder modelling and identification from public data"),
  [Table 4](https://arxiv.org/html/2602.19590v1#S7.T4 "In 7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data"),
  [Table 4](https://arxiv.org/html/2602.19590v1#S7.T4.4.2 "In 7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data").
* [3]
  J. Bouchaud (2025)
  The universal law behind market price swings.
  Physics 18,  pp. 196.
  External Links: [Link](https://physics.aps.org/articles/v18/196)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p6.1 "1 Introduction ‣ Metaorder modelling and identification from public data").
* [4]
  X. Brokmann, E. Serie, J. Kockelkoren, and J. -P. Bouchaud (2014)
  Slow decay of impact in equity markets.
  External Links: 1407.3390,
  [Link](https://arxiv.org/abs/1407.3390)
  Cited by: [§3.5](https://arxiv.org/html/2602.19590v1#S3.SS5.p7.9 "3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").
* [5]
  A. Clauset, C. R. Shalizi, and M. E. J. Newman (2009-11)
  Power-law distributions in empirical data.
  SIAM Review 51 (4),  pp. 661–703.
  External Links: ISSN 1095-7200,
  [Link](http://dx.doi.org/10.1137/070710111),
  [Document](https://dx.doi.org/10.1137/070710111)
  Cited by: [§4.2](https://arxiv.org/html/2602.19590v1#S4.SS2.p1.3 "4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data").
* [6]
  D. Diana and T. Gebbie (2025)
  Non-uniformly sampled simulated price impact of an order-book.
  Journal of Computational and Applied Mathematics 456,  pp. 116202.
  External Links: ISSN 0377-0427,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.cam.2024.116202),
  [Link](https://www.sciencedirect.com/science/article/pii/S0377042724004515)
  Cited by: [§5](https://arxiv.org/html/2602.19590v1#S5.p5.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [7]
  M. Dicks, A. Paskaramoorthy, and T. Gebbie (2023)
  A simple learning agent interacting with an agent-based market model.
  Physica A: Statistical Mechanics and its Applications.
  External Links: [Document](https://dx.doi.org/10.1016/j.physa.2023.129363),
  [Link](https://doi.org/10.1016/j.physa.2023.129363)
  Cited by: [§5](https://arxiv.org/html/2602.19590v1#S5.p4.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [8]
  M. Dicks, A. Paskaramoorthy, and T. Gebbie (2023)
  Many learning agents interacting with an agent-based market model.
  arXiv preprint arXiv:2303.07393.
  External Links: 2303.07393,
  [Link](https://arxiv.org/abs/2303.07393)
  Cited by: [§5](https://arxiv.org/html/2602.19590v1#S5.p4.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [9]
  J. Donier, J. Bonart, I. Mastromatteo, and J. Bouchaud (2015)
  A fully consistent, minimal model for non-linear market impact.
  Quantitative Finance 15 (7),  pp. 1109–1121.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2015.1032540),
  [Link](https://doi.org/10.1080/14697688.2015.1032540)
  Cited by: [§5](https://arxiv.org/html/2602.19590v1#S5.p5.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [10]
  E. Goliath and T. Gebbie (2026)
  Metaorder modelling and identification (github repository).
  Note: <https://github.com/EzraGoliath/Metaorder-modelling-and-identification-Msc-thesis->Accessed: 2026-02-17
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p9.1 "1 Introduction ‣ Metaorder modelling and identification from public data").
* [11]
  F. Lillo and J. D. Farmer (2004)
  The long memory of the efficient market.
  Studies in Nonlinear Dynamics and Econometrics 8 (3).
  External Links: [Document](https://dx.doi.org/10.2202/1558-3708.1144)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p1.1 "1 Introduction ‣ Metaorder modelling and identification from public data").
* [12]
  F. Lillo, S. Mike, and J. D. Farmer (2005-06)
  Theory for long memory in supply and demand.
  Phys. Rev. E 71,  pp. 066122.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevE.71.066122),
  [Link](https://link.aps.org/doi/10.1103/PhysRevE.71.066122)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p1.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p10.2 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p11.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p2.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p4.5 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§5](https://arxiv.org/html/2602.19590v1#S5.p2.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [13]
  F. Lillo (2023)
  Decoding the dynamics of supply and demand.
  Physics 16,  pp. 192.
  External Links: [Link](https://physics.aps.org/articles/v16/192)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p6.1 "1 Introduction ‣ Metaorder modelling and identification from public data").
* [14]
  G. Maitrier, G. Loeper, and J. Bouchaud (2025)
  Generating realistic metaorders from public data.
  External Links: 2503.18199,
  [Link](https://arxiv.org/abs/2503.18199)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p10.2 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p8.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p9.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§3.1](https://arxiv.org/html/2602.19590v1#S3.SS1.p1.1 "3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.1](https://arxiv.org/html/2602.19590v1#S3.SS1.p3.1 "3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.1](https://arxiv.org/html/2602.19590v1#S3.SS1.p4.3 "3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.2](https://arxiv.org/html/2602.19590v1#S3.SS2.p2.2 "3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.3](https://arxiv.org/html/2602.19590v1#S3.SS3.p1.1 "3.3 Time independence of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.4](https://arxiv.org/html/2602.19590v1#S3.SS4.p2.6 "3.4 The concave profile of metaorder impact ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.5](https://arxiv.org/html/2602.19590v1#S3.SS5.p1.1 "3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.5](https://arxiv.org/html/2602.19590v1#S3.SS5.p7.9 "3.5 Post metaorder execution impact decay ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3.7](https://arxiv.org/html/2602.19590v1#S3.SS7.p1.6 "3.7 Example metaorder execution profile ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3](https://arxiv.org/html/2602.19590v1#S3.p1.1 "3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§3](https://arxiv.org/html/2602.19590v1#S3.p1.2 "3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"),
  [§5](https://arxiv.org/html/2602.19590v1#S5.p1.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [15]
  I. Mastromatteo, B. Toth, and J. Bouchaud (2014)
  Agent-based models for latent liquidity and concave price impact.
  Physical Review E 89 (4),  pp. 042805.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevE.89.042805),
  [Link](https://doi.org/10.1103/PhysRevE.89.042805)
  Cited by: [§5](https://arxiv.org/html/2602.19590v1#S5.p5.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [16]
  Y. Sato and K. Kanazawa (2023)
  Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the lillo-mike-farmer model.
  Physical Review Letters 131 (19),  pp. 197401.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevLett.131.197401),
  [Link](https://link.aps.org/doi/10.1103/PhysRevLett.131.197401)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p10.2 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p5.1 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§1](https://arxiv.org/html/2602.19590v1#S1.p7.7 "1 Introduction ‣ Metaorder modelling and identification from public data"),
  [§4.2](https://arxiv.org/html/2602.19590v1#S4.SS2.p1.3 "4.2 Empirical Estimation of 𝛼 and 𝛾 ‣ 4 Testing the LMF theory ‣ Metaorder modelling and identification from public data"),
  [§4](https://arxiv.org/html/2602.19590v1#S4.p1.3 "4 Testing the LMF theory ‣ Metaorder modelling and identification from public data"),
  [§5](https://arxiv.org/html/2602.19590v1#S5.p2.1 "5 Conclusion ‣ Metaorder modelling and identification from public data").
* [17]
  Y. Sato and K. Kanazawa (2023)
  Quantitative statistical analysis of order-splitting behavior of individual trading accounts in the japanese stock market over nine years.
  Physical Review Research 5 (4),  pp. 043131.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevResearch.5.043131),
  [Link](https://link.aps.org/doi/10.1103/PhysRevResearch.5.043131)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p5.1 "1 Introduction ‣ Metaorder modelling and identification from public data").
* [18]
  B. Tóth, Y. Lempérière, C. Deremble, J. de Lataillade, J. Kockelkoren, and J.-P. Bouchaud (2011-10)
  Anomalous price impact and the critical nature of liquidity in financial markets.
  Physical Review X 1 (2).
  External Links: ISSN 2160-3308,
  [Link](http://dx.doi.org/10.1103/PhysRevX.1.021006),
  [Document](https://dx.doi.org/10.1103/physrevx.1.021006)
  Cited by: [§3.2](https://arxiv.org/html/2602.19590v1#S3.SS2.p2.6 "3.2 The Square Root Law ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data").
* [19]
  B. Tóth, Z. Eisler, F. Lillo, J. Kockelkoren, and J. Bouchaud (2011)
  How does the market use information? evidence from the response of prices to trades.
  Quantitative Finance 11 (4),  pp. 817–828.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2010.481632)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p2.1 "1 Introduction ‣ Metaorder modelling and identification from public data").
* [20]
  D. Wilcox and T. Gebbie (2014)
  Hierarchical causality in financial economics.
  arXiv preprint arXiv:1408.5585.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.1408.5585)
  Cited by: [§1](https://arxiv.org/html/2602.19590v1#S1.p1.1 "1 Introduction ‣ Metaorder modelling and identification from public data").

## 7 Appendix

### 7.1 Stocks used in the analysis

|  |  |  |  |
| --- | --- | --- | --- |
| ABG | ACL | AEG | AEL |
| AFE | AFT | AGL | ANG |
| ANH | APN | ARI | AVI |
| BHG | BID | BLU | BOX |
| BTI | BTN | BVT | BYI |
| CCD | CLS | CML | CPR |
| DCP | DIB | DRD | DSY |
| EQU | EXX | FFB | FSR |
| FTB | GFI | GLN | GND |
| GRT | HAR | IMP | INL |
| INP | ITE | JBL | KAP |
| KP2 | KST | LAB | LHC |
| LTE | MDI | MNP | MRP |
| MSP | MTM | MTN | N91 |
| NED | NPH | NPN | NRP |
| NTC | NY1 | OMN | OMU |
| OPA | ORN | OUT | PAN |
| PIK | PPC | PPE | PPH |
| PRX | QLT | RBO | RDF |
| REM | RNI | S32 | SAC |
| SAP | SBK | SHP | SLM |
| SOL | SPG | SRE | SSS |
| SSU | SSW | TFG | TGA |
| TKG | TRU | VAL | VKE |
| VOD | WBC | WHL | YRK |

Table 4: The JSE tickers of the 100 stocks used in the analyses for the project. [[2](https://arxiv.org/html/2602.19590v1#bib.bib17 "BMLL Data Lab Python Development Environment")][[2](https://arxiv.org/html/2602.19590v1#bib.bib17 "BMLL Data Lab Python Development Environment")] ticker names and descriptions and listing dates corporate actions references. See Table [5](https://arxiv.org/html/2602.19590v1#S7.T5 "Table 5 ‣ 7.2 Sample of the processed data ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") for an example of the panel of processed data (after the data engineering) that is ready for the datascience.

The 100 stocks used in the analyses are shown in Table [4](https://arxiv.org/html/2602.19590v1#S7.T4 "Table 4 ‣ 7.1 Stocks used in the analysis ‣ 7 Appendix ‣ Metaorder modelling and identification from public data"). The table displays the tickers as presented by the JSE. These specific stocks were selected by sorting all the stocks on the JSE by volume traded and then choosing the first 100 that contained data from 1 Jan 2023 to 31 Dec 2025.

### 7.2 Sample of the processed data

Panel A

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Row | MIC | Ticker | ListingId | Date | DateTime | ExchangeSequenceNumber | Daily Volume | Daily Volatility |
| 1 | XJSE | AGL | 418405540 | 2023-01-03 | 2023-01-03 09:01:34.362134 | 74722 | 453236.000000 | 0.018747 |
| 2 | XJSE | AGL | 418405540 | 2023-01-03 | 2023-01-03 09:01:34.362332 | 74724 | 453236.000000 | 0.018747 |
| 3 | XJSE | AGL | 418405540 | 2023-01-03 | 2023-01-03 09:01:58.046172 | 86046 | 453236.000000 | 0.018747 |
| 4 | XJSE | AGL | 418405540 | 2023-01-03 | 2023-01-03 09:01:58.296837 | 86214 | 453236.000000 | 0.018747 |
| 5 | XJSE | AGL | 418405540 | 2023-01-03 | 2023-01-03 09:03:21.577601 | 111646 | 453236.000000 | 0.018747 |

Panel B

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Row | Trade Sign | Trade Price | Volume | Mid-price before | Mid-price after(immediate) | Mid-price after(delayed) | Daily Volatility(alt) |
| 1 | 1 | 66400.000000 | 8.000000 | 66258.500000 | 66259.000000 | 66258.500000 | 0.018674 |
| 2 | 1 | 66399.000000 | 5.000000 | 66258.500000 | 66259.000000 | 66213.000000 | 0.018674 |
| 3 | 1 | 66200.000000 | 1000.000000 | 66213.000000 | 66214.500000 | 66214.500000 | 0.018674 |
| 4 | 1 | 66164.000000 | 141.000000 | 66214.500000 | 66215.500000 | 66227.500000 | 0.018674 |
| 5 | 1 | 66298.000000 | 1.000000 | 66227.500000 | 66227.500000 | 66262.500000 | 0.018674 |

Table 5: Sample of processed data for Anglo American plc (Ticker AGL)

Table [5](https://arxiv.org/html/2602.19590v1#S7.T5 "Table 5 ‣ 7.2 Sample of the processed data ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") reports a snippet of the raw data after some basic processing. The data from BMLL [[2](https://arxiv.org/html/2602.19590v1#bib.bib17 "BMLL Data Lab Python Development Environment")] was cleaned and had some basic processing done to it. The only processing done by us was the addition of the Mid-price after(delayed), the Daily Volume, Daily volatility and Daily Volatility(alt). Mid-price after (delayed) is mid-price after the trade and just before the following trade. These values were not used in the analyses, only Mid-price after (immediate) was used in the analyses. Daily Volume is the total volume executed in the day. Daily volatility is the daily volatility, calculated as in Algorithm [2](https://arxiv.org/html/2602.19590v1#alg2 "Algorithm 2 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). Daily Volatility (alt) is an alternate way of calculating the daily volatility but calculated as ln⁡(mmax)−ln⁡(mmin)\ln(m\_{\mathrm{max}})-\ln(m\_{\mathrm{min}}). These values were never used in the analyses.

### 7.3 Sample of data after applying algorithms 1 and 2

Table 6: Sample of processed data for Anglo American plc (Ticker AGL) after applying algorithms 1 and 2

Panel A

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Row | RIC | Date | Start time | End time | daily volume | intraday volatility | number child orders | volume traded |
| 1 | AGL | 2023-01-03 | 2023-01-03 09:05:07.210790 | 2023-01-03 09:15:38.527148 | 453236.000000 | 0.018747 | 4 | 418.000000 |
| 2 | AGL | 2023-01-03 | 2023-01-03 09:18:48.526544 | 2023-01-03 09:23:20.103792 | 453236.000000 | 0.018747 | 6 | 324.000000 |
| 3 | AGL | 2023-01-03 | 2023-01-03 09:24:17.372554 | 2023-01-03 09:24:42.540623 | 453236.000000 | 0.018747 | 3 | 291.000000 |
| 4 | AGL | 2023-01-03 | 2023-01-03 09:25:00.119142 | 2023-01-03 09:28:31.092101 | 453236.000000 | 0.018747 | 5 | 425.000000 |
| 5 | AGL | 2023-01-03 | 2023-01-03 09:35:12.840937 | 2023-01-03 09:35:23.140791 | 453236.000000 | 0.018747 | 4 | 231.000000 |

Panel B

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Row | trade sign | impact(shortfall) | impact(ave per trade) | impact(simple) | 20 AD volume | 20 AD volatility |
| 1 | 1 | 0.002170 | 0.000258 | 0.006093 | 453236.000000 | 0.018747 |
| 2 | -1 | 0.002989 | 0.000047 | 0.002456 | 453236.000000 | 0.018747 |
| 3 | 1 | 0.000776 | 0.000493 | 0.000722 | 453236.000000 | 0.018747 |
| 4 | -1 | 0.002236 | 0.000047 | 0.002948 | 453236.000000 | 0.018747 |
| 5 | 1 | 0.000723 | 0.000178 | 0.000686 | 453236.000000 | 0.018747 |

Table [6](https://arxiv.org/html/2602.19590v1#S7.T6 "Table 6 ‣ 7.3 Sample of data after applying algorithms 1 and 2 ‣ 7 Appendix ‣ Metaorder modelling and identification from public data") shows a snippet of the processed data after applying algorithms [1](https://arxiv.org/html/2602.19590v1#alg1 "Algorithm 1 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data") and [2](https://arxiv.org/html/2602.19590v1#alg2 "Algorithm 2 ‣ 3.1 The metaorder generating algorithms ‣ 3 Generating synthetic metaorders ‣ Metaorder modelling and identification from public data"). We generated the synthetic metaorders by specifying 4 traders and a homogeneous trader participation distribution. The table shows the first 5 metaorders for Anglo American plc (Ticker AGL).

The table reports multiple different versions of 𝑖𝑚𝑝𝑎𝑐𝑡\it{impact} but only 𝑖𝑚𝑝𝑎𝑐𝑡​(𝑠𝑖𝑚𝑝𝑙𝑒)\it{impact(simple)} was used in the analyses. For convenience we have referred to 𝑖𝑚𝑝𝑎𝑐𝑡​(𝑠𝑖𝑚𝑝𝑙𝑒)\it{impact(simple)} as just the impact.