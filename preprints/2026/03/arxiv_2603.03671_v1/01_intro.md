---
authors:
- Takanobu Mizuta
- Isao Yagi
doc_id: arxiv:2603.03671v1
family_id: arxiv:2603.03671
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Is an investor stolen their profits by mimic investors? Investigated by an
  agent-based model Note that the opinions contained herein are solely those of the
  authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.
url_abs: http://arxiv.org/abs/2603.03671v1
url_html: https://arxiv.org/html/2603.03671v1
venue: arXiv q-fin
version: 1
year: 2026
---


Takanobu Mizuta
  
Isao Yagi

###### Abstract

Some investors say increasing investors with the same strategy decreasing their profits per an investor. On the other hand, some investors using technical analysis used to use same strategy and parameters with other investors, and say that it is better. Those argues are conflicted each other because one argues using with same strategy decreases profits but another argues it increase profits. However, those arguments have not been investigated yet. In this study, the agent-based artificial financial market model(ABAFMM) was built by adding “additional agents”(AAs) that includes additional fundamental agents (AFAs) and additional technical agents (ATAs) to the prior model. The AFAs(ATAs) trade obeying simple fundamental(technical) strategy having only the one parameter. We investigated earnings of AAs when AAs increased. We found that in the case with increasing AFAs, market prices are made stable that leads to decrease their profits. In the case with increasing ATAs, market prices are made unstable that leads to gain their profits more.

## I Introduction

Some investors say increasing investors with the same strategy decreasing their profits per an investor. On the other hand, some investors using technical analysis used to use same strategy and parameters with other investors, and say that it is better. Those argues are conflicted each other because one argues using with same strategy decreases profits but another argues it increase profits. However, those arguments have not been investigated yet.

As so many factors affect price formation in actual markets, empirical studies cannot be conducted to isolate the direct effect of increasing investors using exactly same investment strategy. In contrast, an artificial market model, which is an agent-based artificial financial market model(ABAFMM)[[1](#bib.bib1 "Financial market design by an agent-based model")] can isolate the pure contributions of increasing such investors. ABAFMMs have greatly contributed to design a financial market that works well, and that includes making and/or modulating detailed regulations and/or rules[[1](#bib.bib1 "Financial market design by an agent-based model")]. The design of a financial market is very important for the development and maintenance of an advanced economy, but designing it is not easy because changes in detailed rules, even those that seem trivial, sometimes have unexpectedly large impacts and side effects in a financial market, which is a complex system. Traditional economics cannot treat a financial market as a complex system in which micro–macro interaction and feedback loops have played essential roles, because traditional economics can only treat macrophenomena and micro processes separately. ABAFMM can do it, however.

In this study, the ABAFMM was built by adding “additional agents”(AAs) that includes additional fundamental agents (AFAs) and additional technical agents (ATAs) to the prior model of Mizuta and Yagi [[1](#bib.bib1 "Financial market design by an agent-based model")]. The AFAs(ATAs) trade obeying simple fundamental(technical) strategy having only the one parameter. We investigated earnings of AAs when AAs increased.

![Refer to caption](2603.03671v1/x1.png)


Figure 1: Timing of AAs placing orders.

## II Model

An exchange uses a continuous double auction to determine the market price. In the auction mechanism, multiple buyers and sellers compete to buy and sell stocks in the market, and transactions can occur at any time whenever an offer to buy and one to sell match. The minimum unit of a price change is δ​P\delta P. The buy-order and sell-order prices are rounder down and up to the nearest fraction, respectively.

### II-A Normal agents(NAs)

To replicate the nature of price formation in actual financial markets, we introduced the normal agents(NAs) to model a general investor. The number of NAs is nn for the each exchange. The NAs can short sell freely. The holding positions are not limited, so the NAs can take an infinite number of shares for both long and short positions. Time tt increases time tt one when an NA place an order.

NAs always order only one share. First, NA 11 places an order to buy or sell a stock; then NA 22 places an order to buy or sell. After that, NAs 3,4,,,n3,4,,,n each place orders to buy or sell. After the NA nn placed an order, going back to the first NA, 11 places an order to buy or sell, and at NAs 2,3,,,,n2,3,,,,n each place orders to buy or sell, and this cycle is repeated.

An NA determines the order price and buys or sells using a combination of fundamental and technical analysis strategies to form an expectation of the stock return. The expected return of NA jj at tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | re,jt=(w1,j​ln⁡PfPt−1+w2,j​ln⁡Pt−1Pt−τj−1+w3,j​ϵjt)/Σi3​wi,j,r^{t}\_{e,j}=(w\_{1,j}\ln{\frac{P\_{f}}{P^{t-1}}}+w\_{2,j}\ln{\frac{P^{t-1}}{P^{t-\tau\_{j}-1}}}+w\_{3,j}\epsilon^{t}\_{j})/\Sigma\_{i}^{3}w\_{i,j}, |  | (1) |

where wi,jw\_{i,j} is the weight of term ii for NA jj and is independently determined by random variables uniformly distributed on the interval (0,wi,m​a​x)(0,w\_{i,max}) at the start of the simulation for each NA. ln\ln is the natural logarithm. PfP\_{f} is a fundamental value and is a constant. PtP^{t} is a mid-price (the average of the highest buy-order price and the lowest sell-order price) at tt, and ϵjt\epsilon^{t}\_{j} is determined by random variables from a normal distribution with average 0 and variance σϵ\sigma\_{\epsilon} at tt. τj\tau\_{j} is independently determined by random variables uniformly distributed on the interval (1,τm​a​x)(1,\tau\_{max}) at the start of the simulation for each NA111When t<τjt<\tau\_{j}, the second term of Eq. ([1](#S2.E1 "In II-A Normal agents(NAs) ‣ II Model ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.")) is zero..

The first term in Eq. ([1](#S2.E1 "In II-A Normal agents(NAs) ‣ II Model ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.")) represents a fundamental strategy: the NA expects a positive return when the market price is lower than the fundamental value, and vice versa. The second term represents a technical analysis strategy using a historical return: the NA expects a positive return when the historical market return is positive, and vice versa. The third term represents noise.

After the expected return has been determined, the expected price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pe,jt=Pt−1​exp⁡(re,jt).P^{t}\_{e,j}=P^{t-1}\exp{(r^{t}\_{e,j})}. |  | (2) |

Order prices are scattered around the expected price Pe,jtP^{t}\_{e,j} to replicate many waiting limit orders. An order price Po,jtP^{t}\_{o,j} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Po,jt=Pe,jt+Pd​(2​ρjt−1),P^{t}\_{o,j}=P^{t}\_{e,j}+P\_{d}(2\rho^{t}\_{j}-1), |  | (3) |

where ρjt\rho^{t}\_{j} is determined by random variables uniformly distributed on the interval (0,1)(0,1) at tt and PdP\_{d} is a constant. This means that Po,jtP^{t}\_{o,j} is determined by random variables uniformly distributed on the interval (Pe,jt−Pd,Pe,jt+Pd)(P^{t}\_{e,j}-P\_{d},P^{t}\_{e,j}+P\_{d})

Whether the NA buys or sells is determined by the magnitude relationship between Pe,jtP^{t}\_{e,j} and Po,jtP^{t}\_{o,j}. Here222When t<tct<t\_{c}, to generate enough waiting orders, the NA places an order to buy one share when Pf>Po,jtP\_{f}>P^{t}\_{o,j}, or to sell one share when Pf<Po,jtP\_{f}<P^{t}\_{o,j}. ,

* when Pe,jt>Po,jtP^{t}\_{e,j}>P^{t}\_{o,j}, the NA places an buy order,
* when Pe,jt<Po,jtP^{t}\_{e,j}<P^{t}\_{o,j}, the NA places an sell order.

The remaining order is canceled tct\_{c}.

### II-B Additional Agents (AAs)

Additional agents(AAs) that includes additional fundamental agents (AFAs) and additional technical agents (ATAs). The AFAs(ATAs) trade obeying simple fundamental(technical) strategy having only the one parameter. We investigated earnings of AAs when AAs increased. Fig [1](#S1.F1 "Figure 1 ‣ I Introduction ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.") illustrated when AAs place orders. When the one AA is added it places an order at some random time. It places orders at the fixed same time after second loops. When the two AAs are added first added AA places an order at the fixed same time and the second added AA places an order at some random time. They place orders at the fixed same time after second loops. When more than three AAs are added, they place orders as the same way. AA is added one by one, final number of AAs is nan\_{a}.

#### II-B1 Additional Fundamental Agents (AFAs)

Here, we denote that the highest buy-order price is PbtP^{t}\_{b} and the lowest sell-order price is PstP^{t}\_{s} at tt.

When Pst<PfP^{t}\_{s}<P\_{f}, AFAs buy one share when they have no shares and buy two shares when they short-sold one share. In this case, they finally hold one share. They do not place orders when they already have one share.

When Pbt>PfP^{t}\_{b}>P\_{f}, AFAs short-sell one share when they have no shares and short-sell two shares(sell one share and short-sell one share) when they short-sell one share one share. In this case, they finally short-sell one share. They do not place orders when they already short-sold one share.

In other cases, they do not place orders.

#### II-B2 Additional Technical Agents (ATAs)

Here, all ATAs have same the one parameter, t​ata that how long do they refer the price ago.

When Pst>Pt−t​aP^{t}\_{s}>P^{t-ta}, ATAs buy one share when they have no shares and buy two shares when they short-sold one share. In this case, they finally hold one share. They do not place orders when they already have one share.

When Pbt<Pt−t​aP^{t}\_{b}<P^{t-ta}, ATAs short-sell one share when they have no shares and short-sell two shares(sell one share and short-sell one share) when they short-sell one share one share. In this case, they finally short-sell one share. They do not place orders when they already short-sold one share.

In other cases, they do not place orders.

![Refer to caption](2603.03671v1/x2.png)


Figure 2: Time evolution of market prices PtP^{t} without an AA, with 99 AFAs and 99 ATAs.

![Refer to caption](2603.03671v1/x3.png)


Figure 3: The average of final profits and number of trades of AAs for nan\_{a}.

![Refer to caption](2603.03671v1/x4.png)


Figure 4: Mechanism of AFAs stabilizing markets.

![Refer to caption](2603.03671v1/x5.png)


Figure 5: Mechanism of ATAs unstabilize markets.

## III Simulation results

In this study, I set δ​P=0.01,Pf=10000\delta P=0.01,P\_{f}=10000, and for the NAs, n=1000,w1,m​a​x=1,w2,m​a​x=100,w3,m​a​x=1,τm​a​x=10000,σϵ=0.03,Pd=1000n=1000,w\_{1,max}=1,w\_{2,max}=100,w\_{3,max}=1,\tau\_{max}=10000,\sigma\_{\epsilon}=0.03,P\_{d}=1000, and tc=10000t\_{c}=10000 as same as Mizuta et. al. [[1](#bib.bib1 "Financial market design by an agent-based model")]. For AAs, I set n​a=99,t​a=100000na=99,ta=100000. The simulations ran to t=te=20000000t=t\_{e}=20000000.

Fig. [2](#S2.F2 "Figure 2 ‣ II-B2 Additional Technical Agents (ATAs) ‣ II-B Additional Agents (AAs) ‣ II Model ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.") shows time evolution of market prices PtP^{t} without AAs, with 99 AFAs and 99 AFAs. The market is stabilized with AFAs. This means that increasing AFAs make the market more stable. On the other hand, the market is very unstable with ATAs. ATAs amplify the market variation.

Fig. [3](#S2.F3 "Figure 3 ‣ II-B2 Additional Technical Agents (ATAs) ‣ II-B Additional Agents (AAs) ‣ II Model ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.") shows the average of final profits and number of trades of AAs for nan\_{a}. Holding shares at the simulation finished were evaluated with PfP\_{f}. In the case with ATAs, more ATAs, more profits. Number of trades was rapidly declined in na<20n\_{a}<20 but it was stable in na>20n\_{a}>20. This shows that ATAs gain more profits to amplify the variation of market prices by impacts of themselves’ trades. On the other hand, in the case with AFAs the market prices were stables.

Fig. [4](#S2.F4 "Figure 4 ‣ II-B2 Additional Technical Agents (ATAs) ‣ II-B Additional Agents (AAs) ‣ II Model ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.") illustrated mechanism of AFAs stabilizing markets. Here, we discuss a falling case. When market prices fell, AFAs buy. These buys leads market prices to increase and converge with the fundamental price. AFAs gain the price gap between the market and fundamental as a profit, but the gap is decreasing by themselves’ trades that leads market stable. So, trades of AFAs make the price gap decreased and weaken this profit process. This process is a negative feedback process.

Fig. [5](#S2.F5 "Figure 5 ‣ II-B2 Additional Technical Agents (ATAs) ‣ II-B Additional Agents (AAs) ‣ II Model ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.") illustrated mechanism of ATAs unstabilize markets. Here, we discuss an increasing market price case. When market prices increase, ATAs buy. These buys leads market prices to increase more. Increasing market prices more by themselves’ trades leads more profits and market unstable. So, trades of ATAs make the market prices unstable more, gain more profits and strengthen this profit process. This process is a positive feedback process.

## IV Summary

In this study, the ABAFMM was built by adding AAs that includes AFAs and ATAs to the prior model of Mizuta and Yagi [[1](#bib.bib1 "Financial market design by an agent-based model")]. The AFAs(ATAs) trade obeying simple fundamental(technical) strategy having only the one parameter. We investigated earnings of AAs when AAs increased. We found that in the case with increasing AFAs, market prices are made stable that leads to decrease their profits. In the case with increasing ATAs, market prices are made unstable that leads to gain their profits more.

## References

* [1]
  T. Mizuta and I. Yagi (2025)
  Financial market design by an agent-based model.
   Springer Nature.
  Note: * [2]
    https://doi.org/10.1007/978-981-96-1713-5
  Cited by: [§I](#S1.p2.1 "I Introduction ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd."),
  [§I](#S1.p3.1 "I Introduction ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd."),
  [§III](#S3.p1.5 "III Simulation results ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd."),
  [§IV](#S4.p1.1 "IV Summary ‣ Is an investor stolen their profits by mimic investors? Investigated by an agent-based model Note that the opinions contained herein are solely those of the authors and do not necessarily reflect those of SPARX Asset Management Co., Ltd.").

BETA