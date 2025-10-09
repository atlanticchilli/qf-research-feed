---
authors:
- Dávid Csercsik
- Mihály András Vághy
doc_id: arxiv:2510.07025v1
family_id: arxiv:2510.07025
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform
  uncertainty of clearing prices
url_abs: http://arxiv.org/abs/2510.07025v1
url_html: https://arxiv.org/html/2510.07025v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dávid Csercsik
Institute of Economics, ELTE Centre for Economic and Regional Studies Tóth Kálmán u. 4., H-1097 Budapest, Hungary
  
*csercsik.david@krtk.elte.hu*
Pázmány Péter Catholic University, Faculty of Information Technology and Bionics, Práter u. 50/A H-1083 Budapest, Hungary
  
*vaghy.mihaly.andras@itk.ppke.hu*
Corresponding author

Mihály András Vághy
Pázmány Péter Catholic University, Faculty of Information Technology and Bionics, Práter u. 50/A H-1083 Budapest, Hungary
  
*vaghy.mihaly.andras@itk.ppke.hu*

###### Abstract

In a recent publication, using a simple two-period model, which is already capable to capture essential non-convex multiperiod bids, Richstein et al. have shown that in the case of optimal bidding, multi-part bidding always ensures a higher expected profit for the bidder, compared to simple bidding and block-bidding. The model proposed in their analysis assumes a uniform distribution of the market-clearing prices in both periods. In this paper, we study how the conclusions of the analysis are affected, if a very simple, symmetric, stepwise-constant but non-uniform distribution is assumed in the case of the market-clearing price. We show that the results of Richstein et al. also hold in this case.

## 1 Introduction

Since the introduction of liberalized electricity markets [[5](https://arxiv.org/html/2510.07025v1#bib.bib5)], and day-ahead power exchanges in particular [[4](https://arxiv.org/html/2510.07025v1#bib.bib4)], profit-oriented participation in such markets is a fundamental incentive for generator companies (GenCos) [[12](https://arxiv.org/html/2510.07025v1#bib.bib12)].
As formulated in [[13](https://arxiv.org/html/2510.07025v1#bib.bib13)], *’participants* (of electricity spot markets) *have to make decisions independently under complicated situations with insufficient information about their rivals and various uncertainties in the market such as load variations, competitor’s behavior, and power system contingencies.’*
As a consequence, the problem of strategic or optimal bidding (i.e. decision making under the uncertainty of the market outcome) has been widely studied in the literature, using different models and various assumptions [[3](https://arxiv.org/html/2510.07025v1#bib.bib3), [13](https://arxiv.org/html/2510.07025v1#bib.bib13), [16](https://arxiv.org/html/2510.07025v1#bib.bib16)].

### 1.1 Related literature

The reviews [[13](https://arxiv.org/html/2510.07025v1#bib.bib13), [16](https://arxiv.org/html/2510.07025v1#bib.bib16)] classify the literature models for bidding strategy analysis and identify 3 main groups of models: (1) single GenCo optimization models, (2) game theory based models, and (3) agent-based models (the article [[13](https://arxiv.org/html/2510.07025v1#bib.bib13)] also considers a fourth group, namely ’other and hybrid models’).
Single GenCo models focus on the behavior of a single supply-side player, neglecting or simplifying the strategic behavior of other market participants. One of the most important property of such models is that the market clearing price (MCP) is usually considered as an exogenous (independent) variable, in other words, the generating unit in question does not exerts market power, the bids submitted by it do not affect the result of the market outcome.
Game theory models in contrast typically assume that the market equilibrium is the direct consequence of the strategy (bid) choice of participants. Agent based models simulate the rule-based decision making process and interaction of participants (agents), usually assuming that the potentially heterogeneous agents have imperfect or local information, based on which they determine their bids.

In addition, let us note that several recent papers formulating single GenCo optimization models or agent-based models are focusing on characteristic features and the implied optimal bidding strategy of various participant types, e.g. electric vehicle aggregators [[19](https://arxiv.org/html/2510.07025v1#bib.bib19), [20](https://arxiv.org/html/2510.07025v1#bib.bib20)] or demand side aggregators in general [[21](https://arxiv.org/html/2510.07025v1#bib.bib21)], hydro-electric plants [[18](https://arxiv.org/html/2510.07025v1#bib.bib18)], wind producers [[22](https://arxiv.org/html/2510.07025v1#bib.bib22), [9](https://arxiv.org/html/2510.07025v1#bib.bib9)], electro-voltaic producers [[1](https://arxiv.org/html/2510.07025v1#bib.bib1)] and so on.

### 1.2 Motivations and aim

A significant part of optimal bidding models in the literature consider a simplified generation cost model, in which start-up costs and variable costs of generation are not considered individually. These models usually assume that generating units are described by a single cost parameter, quantifying their generation cost per unit per bidding period, which internalizes all types of costs.
The above methodology is used, e.g. in the game theory based model [[10](https://arxiv.org/html/2510.07025v1#bib.bib10)], which approaches the problem of strategic bidding via equilibrium theory in the case of clearing price auctions, assuming a finite number of interacting participants, who do have information about each others parameters.
However, as it is described in [[5](https://arxiv.org/html/2510.07025v1#bib.bib5)], the internalisation of start-up costs often has significant drawbacks.

On the other hand, while there are examples of optimal bidding models, which consider multiperiod scenarios – see e.g. [[7](https://arxiv.org/html/2510.07025v1#bib.bib7), [8](https://arxiv.org/html/2510.07025v1#bib.bib8), [2](https://arxiv.org/html/2510.07025v1#bib.bib2)] –, these models consider the multiperiod nature of the auction rather as an iterative, repeated framework, and do not consider special non-convex orders typically used in day-ahead electricity markets, as the block order [[15](https://arxiv.org/html/2510.07025v1#bib.bib15)], which potentially include multiple periods as well, thus define interdependencies between clearing periods [[14](https://arxiv.org/html/2510.07025v1#bib.bib14)].

The recent article by Richstein et al. [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)] considers a single GenCo scenario, in a two-period market, where the participant in question has the possibility to submit either conventional single-period bids which are cleared and paid off independently for the two periods, or multi-period bids (block bid or multi-part bid), which are cleared and paid off simultaneously considering the resulting MCPs of both periods. The article takes into account the start-up and variable cost components of generation, and assumes uniform distribution of the market-clearing price in both periods considered. In this paper, closed form analytic expressions are derived and compared regarding the optimal bid values and the implied expected profit in either case of bid formats.
The main conclusion of [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)] is that the expected profit is always the highest in the case of multi-part bidding, irrespective of the cost parameters of the actuasl unit.

In the current article, we analyze how sensitive this result is with respect to the modelling assumptions, i.e. we derive a similar analysis, under a different model of the uncertainty regarding the market clearing prices, which is still simple enough to allow for analytic results.

## 2 Methods

We consider a simple, two-period market scenario, and a generating unit bidding in this market. Apart from assumptions regarding the distribution of the market clearing price, we use the same assumptions, notations and parameters as in [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)].

### 2.1 Cost model of the generating unit

The generating unit in question is characterized by
a fixed, positive start-up cost csc\_{s}, which occurs in any case the power plant produces in one or two periods.
In addition, the plant has positive variable production cost, arising in each period in which the plant is producing, and in contrast to the start-up costs, it depends on the produced quantity (linearly): the parameter cvc\_{v} is the linear coefficient describing the ratio of the quantity-dependent production cost, and the produced quantity.

Following the assumptions made in [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)], we assume that the production quantities are normalized (i.e. the unit is either producing 0 or 1 unit in each period). Thus, the CGC\_{G} generation cost of the unit may be described as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | CG={cs+2​cv,if the unit produces in both periods, cs+cv,if the unit produces in one of the periods, 0,otherwise. C\_{G}=\begin{cases}c\_{s}+2c\_{v},\qquad&\text{if the unit produces in both periods, }\\ c\_{s}+c\_{v},\qquad&\text{if the unit produces in one of the periods, }\\ 0,\qquad&\text{otherwise. }\\ \end{cases} |  | (1) |

### 2.2 Model of the two-period market

We consider a simple two-period market model and assume that the market-clearing prices of the periods, denoted by 0≤p1≤10\leq p\_{1}\leq 1 and 0≤p2≤10\leq p\_{2}\leq 1 for period 1 and 2, respectively, are independent continuous random variables. Furthermore, we assume that the generating unit has no market power, in other words, the bids submitted by the unit in question do not affect the clearing prices.

In contrast to the original article [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)], where the authors assumed that the distribution of market-clearing prices is uniform for each period, we assume a simple non-uniform, stepwise symmetric distribution for p1p\_{1} and p2p\_{2}. This is on the one hand in accordance with the results of simulation studies described in [[6](https://arxiv.org/html/2510.07025v1#bib.bib6)], which shows that if all bid prices and quantities in the demand and supply side of a day-ahead market follow uniform distributions, the distribution of the market clearing price resembles to a normal distribution, i.e. values in the middle of the interval are more likely to appear.
Regarding the statistical analysis of European day-ahead market clearing prices, on may refer to [[11](https://arxiv.org/html/2510.07025v1#bib.bib11)].

We assume the simple stepwise distribution depicted in Figure [1](https://arxiv.org/html/2510.07025v1#S2.F1 "Figure 1 ‣ 2.2 Model of the two-period market ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices") for both p1p\_{1} and p2p\_{2}.

![Refer to caption](figures/tombos_eloszlas_fuggv.png)


Figure 1: Stepwise distribution

The formal equations of the probability density functions for p1p\_{1} and p2p\_{2}, denoted by ρp1​(x)\rho\_{p\_{1}}(x) and ρp2​(x)\rho\_{p\_{2}}(x), are given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρp1​(x)=ρp2​(x)={12,0≤x<14,32,14≤x<34,12,34≤x<1,0,otherwise.\rho\_{p\_{1}}(x)=\rho\_{p\_{2}}(x)=\begin{cases}\frac{1}{2},\qquad&0\leq x<\frac{1}{4},\\ \frac{3}{2},\qquad&\frac{1}{4}\leq x<\frac{3}{4},\\ \frac{1}{2},\qquad&\frac{3}{4}\leq x<1,\\ 0,&\text{otherwise.}\end{cases} |  | (2) |

Let us note that the parameters of the proposed stepwise distribution (i.e. breakpoints and step-values) may be chosen arbitrarily. The results to be presented may be adjusted more or less straightforwardly to similar stepwise distributions with other parameters as well. By altering the assumption regarding the distribution of p1p\_{1} and p2p\_{2}, the model may be considered more realistic, but in the same time, as we will see, it remains still simple enough to obtain analytical results regarding the optimal bid values.

### 2.3 Simple bidding

In the simple bid format, the generating unit bids for each period separately with bids characterized by the prices b1b\_{1} and b2b\_{2}. If the realised market clearing prices p1p\_{1} and p2p\_{2} are equal or greater than the respective bid prices p1p\_{1} and p2p\_{2}, both bids are accepted and the unit needs to produce in both periods with the associated costs. In this case, the unit is paid off according to the market-clearing prices p1p\_{1} and p2p\_{2}, i.e. the income of the unit (II) equals p1+p2p\_{1}+p\_{2}. If the market-clearing price exceeds the bid price in only one of the periods, the respective can be individually accepted, while the other bid is rejected, so that a unit may produce in one period, but not in the other. Let πS\pi\_{S} denote the profit for an actor in the case of simple bidding. Considering the cost model described in Eq. ([1](https://arxiv.org/html/2510.07025v1#S2.E1 "In 2.1 Cost model of the generating unit ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")), it can be calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | πS​(b1,b2,p1,p2)=I−CG={p1+p2−cs−2​cv,p1≥b1,p2≥b2,p1−cs−cv,p1≥b1,p2<b2,p2−cs−cv,p1<b1,p2≥b2,0,otherwise.\pi\_{S}(b\_{1},b\_{2},p\_{1},p\_{2})=I-C\_{G}=\begin{cases}p\_{1}+p\_{2}-c\_{s}-2c\_{v},\qquad&p\_{1}\geq b\_{1},\penalty 10000\ p\_{2}\geq b\_{2},\\ p\_{1}-c\_{s}-c\_{v},\qquad&p\_{1}\geq b\_{1},\penalty 10000\ p\_{2}<b\_{2},\\ p\_{2}-c\_{s}-c\_{v},\qquad&p\_{1}<b\_{1},\penalty 10000\ p\_{2}\geq b\_{2},\\ 0,\qquad&\text{otherwise.}\\ \end{cases} |  | (3) |

Following [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)], we assume b1=b2=bb\_{1}=b\_{2}=b and define πS​(b,p1,p2)=πS​(b,b,p1,p2)\pi\_{S}(b,p\_{1},p\_{2})=\pi\_{S}(b,b,p\_{1},p\_{2}). The expected profit E​[πS​(b)]E[\pi\_{S}(b)], as a function of bb, can be given as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​[πS​(b)]\displaystyle E[\pi\_{S}(b)] | =∫01∫01πS​(b,p1,p2)​ρp1​(x)​ρp2​(y)​dx​dy\displaystyle=\int\_{0}^{1}\int\_{0}^{1}\pi\_{S}(b,p\_{1},p\_{2})\rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y} |  | (4) |
|  |  | =∫b1∫b1(p1+p2−cs−2​cv)​ρp1​(x)​ρp2​(y)​dx​dy\displaystyle=\int\_{b}^{1}\int\_{b}^{1}(p\_{1}+p\_{2}-c\_{s}-2c\_{v})\penalty 10000\ \rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y} |  |
|  |  | +∫0b∫b1(p1−cs−cv)​ρp1​(x)​ρp2​(y)​dx​dy\displaystyle+\int\_{0}^{b}\int\_{b}^{1}(p\_{1}-c\_{s}-c\_{v})\penalty 10000\ \rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y} |  |
|  |  | +∫b1∫0b(p2−cs−cv)​ρp1​(x)​ρp2​(y)​dx​dy.\displaystyle+\int\_{b}^{1}\int\_{0}^{b}(p\_{2}-c\_{s}-c\_{v})\penalty 10000\ \rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y}. |  |

### 2.4 Block bidding

In the case of block bidding, a single bid including both periods is submitted, which is either fully accepted or fully rejected. Hence, if the block bid is accepted, the unit is producing in both periods.
The profit for block bidding is denoted by πB\pi\_{B} and may be calculated as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | πB​(b,p1,p2)={p1+p2−cs−2​cv,p1+p2≥b,0,otherwise. \pi\_{B}(b,p\_{1},p\_{2})=\begin{cases}p\_{1}+p\_{2}-c\_{s}-2c\_{v},\qquad&p\_{1}+p\_{2}\geq b,\\ 0,\qquad&\text{otherwise. }\\ \end{cases} |  | (5) |

The expected profit E​[πB​(b)]E[\pi\_{B}(b)] can be computed as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​[πB​(b)]\displaystyle E[\pi\_{B}(b)] | =∫01∫01πB​(b,p1,p2)​ρp1​(x)​ρp2​(y)​dx​dy\displaystyle=\int\_{0}^{1}\int\_{0}^{1}\pi\_{B}(b,p\_{1},p\_{2})\rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y} |  | (6) |
|  |  | =∫0b∫b−y1(p1+p2−cs−2​cv)​ρp1​(x)​ρp2​(y)​dx​dy\displaystyle=\int\_{0}^{b}\int\_{b-y}^{1}(p\_{1}+p\_{2}-c\_{s}-2c\_{v})\rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y} |  |
|  |  | +∫b1∫01(p1+p2−cs−2​cv)​ρp1​(x)​ρp2​(y)​dx​dy.\displaystyle+\int\_{b}^{1}\int\_{0}^{1}(p\_{1}+p\_{2}-c\_{s}-2c\_{v})\rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y}. |  |

### 2.5 Multi-part bidding

Multi-part bidding allows the participant to explicitly bid the values of the start-up cost bsb\_{s} and variable cost bvb\_{v} that are valid for
both periods. Dependent on market prices the bid will be accepted in one, two, or no periods.
The profit for multi-part bidding is denoted by πM\pi\_{M} and can be given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | πM​(bs,bv,p1,p2)={p1−cs−cv,p1≥bs+bv,p2<bv,p2−cs−cv,p1<bv,p2≥bs+bv,p1+p2−cs−2​cv,p1,p2≥bv,p1+p2≥bs+2​bv,0,otherwise. \pi\_{M}(b\_{s},b\_{v},p\_{1},p\_{2})=\begin{cases}p\_{1}-c\_{s}-c\_{v},\qquad&p\_{1}\geq b\_{s}+b\_{v},\penalty 10000\ p\_{2}<b\_{v},\\ p\_{2}-c\_{s}-c\_{v},\qquad&p\_{1}<b\_{v},\penalty 10000\ p\_{2}\geq b\_{s}+b\_{v},\\ p\_{1}+p\_{2}-c\_{s}-2c\_{v},\qquad&p\_{1},p\_{2}\geq b\_{v},\penalty 10000\ p\_{1}+p\_{2}\geq b\_{s}+2b\_{v},\\ 0,\qquad&\text{otherwise. }\\ \end{cases} |  | (7) |

In this case the expected profit can be described as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]=∫01∫01πM​(bs,bv,p1,p2)​ρp1​(x)​ρp2​(y)​dx​dy.E[\pi\_{M}(b\_{s},b\_{v})]=\int\_{0}^{1}\int\_{0}^{1}\pi\_{M}(b\_{s},b\_{v},p\_{1},p\_{2})\rho\_{p\_{1}}(x)\rho\_{p\_{2}}(y)\differential{x}\differential{y}.\\ |  | (8) |

We have to compute the integrals for the following 21 cases:

1. 1.

   0≤bv<140\leq b\_{v}<\frac{1}{4}

   1. (a)

      0≤bs≤14−bv0\leq b\_{s}\leq\frac{1}{4}-b\_{v}
   2. (b)

      14−bv≤bs<12−2​bv\frac{1}{4}-b\_{v}\leq b\_{s}<\frac{1}{2}-2b\_{v}
   3. (c)

      12−2​bv≤bs<34−bv\frac{1}{2}-2b\_{v}\leq b\_{s}<\frac{3}{4}-b\_{v}
   4. (d)

      34−bv≤bs<1−2​bv\frac{3}{4}-b\_{v}\leq b\_{s}<1-2b\_{v}
   5. (e)

      1−2​bv≤bs<1−bv1-2b\_{v}\leq b\_{s}<1-b\_{v}
   6. (f)

      1−bv≤bs<54−2​bv1-b\_{v}\leq b\_{s}<\frac{5}{4}-2b\_{v}
   7. (g)

      54−2​bv≤bs<32−2​bv\frac{5}{4}-2b\_{v}\leq b\_{s}<\frac{3}{2}-2b\_{v}
   8. (h)

      32−2​bv≤bs<74−2​bv\frac{3}{2}-2b\_{v}\leq b\_{s}<\frac{7}{4}-2b\_{v}
   9. (i)

      74−2​bv≤bs<2−2​bv\frac{7}{4}-2b\_{v}\leq b\_{s}<2-2b\_{v}
2. 2.

   14≤bv<12\frac{1}{4}\leq b\_{v}<\frac{1}{2}

   1. (a)

      0≤bs<34−bv0\leq b\_{s}<\frac{3}{4}-b\_{v}
   2. (b)

      34−bv≤bs<1−bv\frac{3}{4}-b\_{v}\leq b\_{s}<1-b\_{v}
   3. (c)

      1−bv≤bs<32−2​bv1-b\_{v}\leq b\_{s}<\frac{3}{2}-2b\_{v}
   4. (d)

      32−2​bv≤bs<74−2​bv\frac{3}{2}-2b\_{v}\leq b\_{s}<\frac{7}{4}-2b\_{v}
   5. (e)

      74−2​bv≤bs<2−2​bv\frac{7}{4}-2b\_{v}\leq b\_{s}<2-2b\_{v}
3. 3.

   12≤bv<34\frac{1}{2}\leq b\_{v}<\frac{3}{4}

   1. (a)

      0≤bs<34−bv0\leq b\_{s}<\frac{3}{4}-b\_{v}
   2. (b)

      34−bv≤bs<32−2​bv\frac{3}{4}-b\_{v}\leq b\_{s}<\frac{3}{2}-2b\_{v}
   3. (c)

      32−2​bv≤bs<1−bv\frac{3}{2}-2b\_{v}\leq b\_{s}<1-b\_{v}
   4. (d)

      1−bv≤bs<74−2​bv1-b\_{v}\leq b\_{s}<\frac{7}{4}-2b\_{v}
   5. (e)

      74−2​bv≤bs<2−2​bv\frac{7}{4}-2b\_{v}\leq b\_{s}<2-2b\_{v}
4. 4.

   34≤bs<1\frac{3}{4}\leq b\_{s}<1

   1. (a)

      0≤bs<1−bv0\leq b\_{s}<1-b\_{v}
   2. (b)

      1−bv≤bs<2−2​bv1-b\_{v}\leq b\_{s}<2-2b\_{v}

## 3 Results

## 4 Results

### 4.1 Simple bidding

In this subsection, we derive the optimal bidding strategy in the case of simple bidding, assuming the stepwise distribution of p1p\_{1} and p2p\_{2} as described in Eq. ([2](https://arxiv.org/html/2510.07025v1#S2.E2 "In 2.2 Model of the two-period market ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")).

Computing the integrals in Eq. ([3](https://arxiv.org/html/2510.07025v1#S2.E3 "In 2.3 Simple bidding ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πS​(b)]={14​(−2​b2+b2​cs+4​b​cv−8​cv−4​cs+4),0≤b<14,116(−24b2+36b2cs+48bcv−12bcs−40cv−15cs+17),14≤b<34,14​(−2​b2+b2​cs+4​b​cv+2​b​cs−4​cv−3​cs+2),34≤b≤1.E[\pi\_{S}(b)]=\begin{cases}\displaystyle\frac{1}{4}\quantity\big(-2b^{2}+b^{2}c\_{s}+4bc\_{v}-8c\_{v}-4c\_{s}+4),\qquad&0\leq b<\frac{1}{4},\\[9.24994pt] \begin{aligned} \frac{1}{16}\Big(-24b^{2}+36b^{2}c\_{s}+48bc\_{v}\\ -12bc\_{s}-40c\_{v}-15c\_{s}+17\Big),\end{aligned}\qquad&\frac{1}{4}\leq b<\frac{3}{4},\\[9.24994pt] \displaystyle\frac{1}{4}\quantity\big(-2b^{2}+b^{2}c\_{s}+4bc\_{v}+2bc\_{s}-4c\_{v}-3c\_{s}+2),&\frac{3}{4}\leq b\leq 1.\end{cases} |  | (9) |

The algebraic details of the calculations are described in Appendix A. To determine the optimal bid, we need to find the maximum of Eq. ([9](https://arxiv.org/html/2510.07025v1#S4.E9 "In 4.1 Simple bidding ‣ 4 Results ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")). Since the expected profit is given as a piecewise function, the set of critical points consists of not just the extrema of the three cases, but also of the points b=0b=0, b=14b=\frac{1}{4}, b=34b=\frac{3}{4} and b=1b=1.

The derivatives are given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ddb⁡E​[πS​(b)]={12​b​(cs−2)+cv,0≤b<14,34​(b​(6​cs−4)−cs+4​cv),14≤b<34,12​(b​(−2+cs)+cs+2​cv),34≤b≤1.\derivative{b}E[\pi\_{S}(b)]=\begin{cases}\displaystyle\frac{1}{2}b(c\_{s}-2)+c\_{v},\qquad&0\leq b<\frac{1}{4},\\[9.24994pt] \displaystyle\frac{3}{4}\quantity\big(b(6c\_{s}-4)-c\_{s}+4c\_{v}),\qquad&\frac{1}{4}\leq b<\frac{3}{4},\\[9.24994pt] \displaystyle\frac{1}{2}(b(-2+c\_{s})+c\_{s}+2c\_{v}),&\frac{3}{4}\leq b\leq 1.\end{cases} |  | (10) |

Then the set of critical points is

|  |  |  |  |
| --- | --- | --- | --- |
|  | {0,14,34,1,−2​cvcs−2,−cs+4​cv6​cs−4,−cs−2​cvcs−2},\quantity\bigg{0,\frac{1}{4},\frac{3}{4},1,\frac{-2c\_{v}}{c\_{s}-2},\frac{-c\_{s}+4c\_{v}}{6c\_{s}-4},\frac{-c\_{s}-2c\_{v}}{c\_{s}-2}}, |  | (11) |

and thus the optimal bidding strategy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | bS∗=max⁡(E​[πS​(b)]|b∈{0,14,34,1,−2​cvcs−2,−cs+4​cv6​cs−4,−cs−2​cvcs−2}).b\_{S}^{\*}=\max\quantity\Bigg(E[\pi\_{S}(b)]\bigg|b\in\quantity\bigg{0,\frac{1}{4},\frac{3}{4},1,\frac{-2c\_{v}}{c\_{s}-2},\frac{-c\_{s}+4c\_{v}}{6c\_{s}-4},\frac{-c\_{s}-2c\_{v}}{c\_{s}-2}}). |  | (12) |

Note, that for example in case A it might happen that the optimal bb value of −2​cvcs−2-\frac{2c\_{v}}{c\_{s}-2} is not in the corresponding interval 0≤b<140\leq b<\frac{1}{4}. In this case that part of E​[πS]E[\pi\_{S}] reaches its maximal value at one of the endpoints of the underlying interval and the function value at −2​cvcs−2-\frac{2c\_{v}}{c\_{s}-2} need not to be checked. Figure [2](https://arxiv.org/html/2510.07025v1#S4.F2 "Figure 2 ‣ 4.1 Simple bidding ‣ 4 Results ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices") shows the contour plot of the maximal expected profit as a function of csc\_{s} and cvc\_{v}.

![Refer to caption](figures/anon_CEpi_simple_5000.png)


Figure 2: Contour plot of the maximal expected profit for simple bidding.

### 4.2 Block bidding

Computing the integrals in Eq. ([6](https://arxiv.org/html/2510.07025v1#S2.E6 "In 2.4 Block bidding ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πB​(b)]={−b312+b2​(cs+2​cv)8−2​cv−cs+1,0≤b<14,−5​b312+b2​(5​cs+10​cv+1)8−b​(cs+2​cv)4−31​cs+62​cv32+383384,14≤b<12,−3​b34+b2​(9​cs+18​cv+4)8−b​(3​cs+6​cv)4−27​cs+54​cv32+125128,12≤b<34,−5​b312+b2​(5​cs+10​cv)8−9​cs+18​cv8+6764,34≤b<1,5​b312−b2​(5​cs+10​cv+10)8+b​(5​cs+10​cv)2−19​cs+38​cv8+281192,1≤b<54,3​b34−b2​(9​cs+18​cv+15)8+b​(15​cs+30​cv)4−101​cs+202​cv32+229128,54≤b<32,5​b312−b2​(5​cs+10​cv+9)8+b​(9​cs+18​cv)4−65​cs+130​cv32+157128,32≤b<74,b312−b2​(cs+2​cv+2)8+b​(cs+2​cv)2−cs+2​cv2+13,74≤b<2.E[\pi\_{B}(b)]=\begin{cases}\displaystyle-\frac{b^{3}}{12}+\frac{b^{2}(c\_{s}+2c\_{v})}{8}-2c\_{v}-c\_{s}+1,\qquad&0\leq b<\frac{1}{4},\\[9.24994pt] \begin{aligned} &-\frac{5b^{3}}{12}+\frac{b^{2}(5c\_{s}+10c\_{v}+1)}{8}\\ &-\frac{b(c\_{s}+2c\_{v})}{4}-\frac{31c\_{s}+62c\_{v}}{32}+\frac{383}{384},\end{aligned}\qquad&\frac{1}{4}\leq b<\frac{1}{2},\\[18.49988pt] \begin{aligned} &-\frac{3b^{3}}{4}+\frac{b^{2}(9c\_{s}+18c\_{v}+4)}{8}\\ &-\frac{b(3c\_{s}+6c\_{v})}{4}-\frac{27c\_{s}+54c\_{v}}{32}+\frac{125}{128},\end{aligned}\qquad&\frac{1}{2}\leq b<\frac{3}{4},\\[18.49988pt] \displaystyle-\frac{5b^{3}}{12}+\frac{b^{2}(5c\_{s}+10c\_{v})}{8}-\frac{9c\_{s}+18c\_{v}}{8}+\frac{67}{64},\qquad&\frac{3}{4}\leq b<1,\\[9.24994pt] \begin{aligned} &\frac{5b^{3}}{12}-\frac{b^{2}(5c\_{s}+10c\_{v}+10)}{8}\\ &+\frac{b(5c\_{s}+10c\_{v})}{2}-\frac{19c\_{s}+38c\_{v}}{8}+\frac{281}{192},\end{aligned}\qquad&1\leq b<\frac{5}{4},\\[18.49988pt] \begin{aligned} &\frac{3b^{3}}{4}-\frac{b^{2}(9c\_{s}+18c\_{v}+15)}{8}\\ &+\frac{b(15c\_{s}+30c\_{v})}{4}-\frac{101c\_{s}+202c\_{v}}{32}+\frac{229}{128},\end{aligned}\qquad&\frac{5}{4}\leq b<\frac{3}{2},\\[18.49988pt] \begin{aligned} &\frac{5b^{3}}{12}-\frac{b^{2}(5c\_{s}+10c\_{v}+9)}{8}\\ &+\frac{b(9c\_{s}+18c\_{v})}{4}-\frac{65c\_{s}+130c\_{v}}{32}+\frac{157}{128},\end{aligned}\qquad&\frac{3}{2}\leq b<\frac{7}{4},\\[18.49988pt] \displaystyle\frac{b^{3}}{12}-\frac{b^{2}(c\_{s}+2c\_{v}+2)}{8}+\frac{b(c\_{s}+2c\_{v})}{2}-\frac{c\_{s}+2c\_{v}}{2}+\frac{1}{3},\qquad&\frac{7}{4}\leq b<2.\end{cases} |  | (13) |

Figure [3](https://arxiv.org/html/2510.07025v1#S4.F3 "Figure 3 ‣ 4.2 Block bidding ‣ 4 Results ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices") shows the contour plot of the expected profit as a function of csc\_{s} and cvc\_{v}.

![Refer to caption](figures/anon_CEpi_block_5000.png)


Figure 3: Contour plot of the maximal expected profit for block bidding.

The derivatives are given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ddb⁡E​[πB​(b)]={−b24+b(cs+2cv2,0≤b<14,−5​b24+b​(5​cs+10​cv+1)4−cs+2​cv414≤b<12,−9​b34+b(9cs+9cv+34−3​cs+6​cv412≤b<34,−5​b24+b​(5​cs+10​cv)4,34≤b<1,5​b24−b​(5​cs+10​cv+10)4+5​cs+10​cv21≤b<54,9​b24−b​(9​cs+18​cv+15)4+15​cs+30​cv454≤b<32,5​b24−b(5cs+10cv+94+9​cs+18​cv432≤b<74,b24−b​(cs+2​cv+2)4+cs+2​cv2,74≤b<2.\derivative{b}E[\pi\_{B}(b)]=\begin{cases}\displaystyle-\frac{b^{2}}{4}+\frac{b(c\_{s}+2c\_{v}}{2},\qquad&0\leq b<\frac{1}{4},\\[9.24994pt] \displaystyle-\frac{5b^{2}}{4}+\frac{b(5c\_{s}+10c\_{v}+1)}{4}-\frac{c\_{s}+2c\_{v}}{4}\qquad&\frac{1}{4}\leq b<\frac{1}{2},\\[9.24994pt] \displaystyle-\frac{9b^{3}}{4}+\frac{b(9c\_{s}+9c\_{v}+3}{4}-\frac{3c\_{s}+6c\_{v}}{4}\qquad&\frac{1}{2}\leq b<\frac{3}{4},\\[9.24994pt] \displaystyle-\frac{5b^{2}}{4}+\frac{b(5c\_{s}+10c\_{v})}{4},\qquad&\frac{3}{4}\leq b<1,\\[9.24994pt] \displaystyle\frac{5b^{2}}{4}-\frac{b(5c\_{s}+10c\_{v}+10)}{4}+\frac{5c\_{s}+10c\_{v}}{2}\qquad&1\leq b<\frac{5}{4},\\[9.24994pt] \displaystyle\frac{9b^{2}}{4}-\frac{b(9c\_{s}+18c\_{v}+15)}{4}+\frac{15c\_{s}+30c\_{v}}{4}\qquad&\frac{5}{4}\leq b<\frac{3}{2},\\[9.24994pt] \displaystyle\frac{5b^{2}}{4}-\frac{b(5c\_{s}+10c\_{v}+9}{4}+\frac{9c\_{s}+18c\_{v}}{4}\qquad&\frac{3}{2}\leq b<\frac{7}{4},\\[9.24994pt] \displaystyle\frac{b^{2}}{4}-\frac{b(c\_{s}+2c\_{v}+2)}{4}+\frac{c\_{s}+2c\_{v}}{2},\qquad&\frac{7}{4}\leq b<2.\end{cases} |  | (14) |

Then the set of critical points is

|  |  |  |  |
| --- | --- | --- | --- |
|  | {0,14,12,34,1,54,32,74,2,cs+2​cv},\quantity\bigg{0,\frac{1}{4},\frac{1}{2},\frac{3}{4},1,\frac{5}{4},\frac{3}{2},\frac{7}{4},2,c\_{s}+2c\_{v}}, |  | (15) |

and thus the optimal bidding strategy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | bB∗=max⁡(E​[πB​(b)]|b∈{0,14,12,34,1,54,32,74,2,cs+2​cv}).b\_{B}^{\*}=\max\quantity\Bigg(E[\pi\_{B}(b)]\bigg|b\in\quantity\bigg{0,\frac{1}{4},\frac{1}{2},\frac{3}{4},1,\frac{5}{4},\frac{3}{2},\frac{7}{4},2,c\_{s}+2c\_{v}}). |  | (16) |

### 4.3 Multi-part bidding

Figure [4](https://arxiv.org/html/2510.07025v1#S4.F4 "Figure 4 ‣ 4.3 Multi-part bidding ‣ 4 Results ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices") shows the contour plot of the expected profit as a function of csc\_{s} and cvc\_{v}.

![Refer to caption](figures/anon_CEpi_multipart_5000.png)


Figure 4: Contour plot of the maximal expected profit for multi-part bidding.

### 4.4 Comparison

Figure [5](https://arxiv.org/html/2510.07025v1#S4.F5 "Figure 5 ‣ 4.4 Comparison ‣ 4 Results ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices") depicts the contour of maximal expected profits, as a function of csc\_{s} and cvc\_{v}, considering all possible bidding formats. As one may notice, this figure aligns with Fig. [4](https://arxiv.org/html/2510.07025v1#S4.F4 "Figure 4 ‣ 4.3 Multi-part bidding ‣ 4 Results ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices").

![Refer to caption](figures/anon_CEpi_combined_5000.png)


Figure 5: Contour plot of the maximal expected profit, considering all possible bidding formats.



![Refer to caption](figures/anon_CEpi_simple_v_multipart_5000.png)

![Refer to caption](figures/anon_CEpi_block_v_multipart_5000.png)

Figure 6: Contour plots of ratios of simple vs. multipart bidding and block vs multipart bidding.

## 5 Conclusions

The article [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)] has shown that multipart bidding results in higher expected profits compared to simple and block bidding, independent of the parameters csc\_{s} and cvc\_{v}, when assuming uniform distribution of the market-clearing prices. We repeated the analysis for a simple case of non-uniform market-clearing prices, where the density function is piecewise constant and symmetric. Although analytical results for the relation of the bidding formats are not presented in the current article, the numerical results derived are in line with the previous results of [[17](https://arxiv.org/html/2510.07025v1#bib.bib17)] in the sense that multipart bidding proves to be optimal also in this case of the clearing price distribution. Although an analytical proof is nontrivial even in this case, further work is required to decide whether the optimality of multipart bidding is valid independent of the distribution of the market-clearing price.

## 6 Acknowledgements

This work has been supported by the Fund FK 137608 of the Hungarian National Research, Development and Innovation Office.

## 7 Acknowledgements

This work has been supported by the Fund FK 137608 of the Hungarian National Research, Development and Innovation Office.

## References

* [1]

  Ricardo Jorge Bessa and MA Matos.
  Global against divided optimization for the participation of an ev
  aggregator in the day-ahead electricity market. part i: Theory.
  Electric Power Systems Research, 95:309–318, 2013.
* [2]

  Tu Bo, Takayuki Ishizaki, Masakazu Koike, Nobuyuki Yamaguchi, and Jun-ichi
  Imura.
  Optimal bidding strategy for multiperiod electricity market with
  consideration of pv prediction uncertainty.
  In 2017 56th Annual Conference of the Society of Instrument and
  Control Engineers of Japan (SICE), pages 293–298. IEEE, 2017.
* [3]

  Antonio J Conejo, Miguel Carrión, Juan M Morales, et al.
  Decision making under uncertainty in electricity markets,
  volume 1.
  Springer, 2010.
* [4]

  J. Contreras, O. Candiles, J. I. De La Fuente, and T. Gomez.
  Auction design in day-ahead electricity markets.
  IEEE Transactions on Power Systems, 16(1):88–96, Feb 2001.
* [5]

  Peter Cramton.
  Electricity market design.
  Oxford Review of Economic Policy, 33(4), 2017.
* [6]

  Dávid Csercsik.
  A two-sided price-decoupled pay-as-bid auction approach for the
  clearing of day-ahead electricity markets.
  In E3S Web of Conferences, volume 162, page 01006. EDP
  Sciences, 2020.
* [7]

  S De la Torre, AJ Conejo, and J Contreras.
  Simulating oligopolistic pool-based electricity markets: A
  multiperiod approach.
  Power Systems, IEEE Transactions on, 18(4):1547–1555, 2003.
* [8]

  Sebastián De la Torre, Javier Contreras, and Antonio J Conejo.
  Finding multiperiod nash equilibria in pool-based electricity
  markets.
  Power Systems, IEEE Transactions on, 19(1):643–651, 2004.
* [9]

  Victoria Guerrero-Mestre, Agustín A Sanchez de la Nieta, Javier Contreras,
  and Joao PS Catalao.
  Optimal bidding of a group of wind farms in day-ahead markets through
  an external agent.
  IEEE Transactions on Power Systems, 31(4):2688–2700, 2015.
* [10]

  Shangyou Hao.
  A study of basic bidding strategy in clearing pricing auctions.
  IEEE Transactions on Power Systems, 15(3):975–980, 2000.
* [11]

  Ronald Huisman and Mehtap Kilic.
  A history of european electricity day-ahead prices.
  Applied Economics, 45(18):2683–2693, 2013.
* [12]

  P.R. Kleindorfer, D.-J. Wu, and C.S. Fernando.
  Strategic gaming in electric power markets.
  European Journal of Operational Research, 130:156–168, 2001.
* [13]

  Gong Li, Jing Shi, and Xiuli Qu.
  Modeling methods for genco bidding strategy optimization in the
  liberalized electricity spot market–a state-of-the-art review.
  Energy, 36(8):4686–4700, 2011.
* [14]

  Mehdi Madani.
  Revisiting European day-ahead electricity market auctions: MIP
  models and algorithms.
  PhD thesis, Université catholique de Louvain, 2017.
* [15]

  Leonardo Meeus, Karolien Verhaegen, and Ronnie Belmans.
  Block order restrictions in combinatorial electric energy auctions.
  European journal of operational research, 196(3):1202–1206,
  2009.
* [16]

  M Prabavathi and R Gnanadass.
  Energy bidding strategies for restructured electricity market.
  International Journal of Electrical Power & Energy Systems,
  64:956–966, 2015.
* [17]

  J. C. Richstein, C. Lorenz, and K. Neuhoff.
  An auction story: How simple bids struggle with uncertainty.
  Energy Economics, 89(10), 2020.
* [18]

  Gregory Steeger, Luiz Augusto Barroso, and Steffen Rebennack.
  Optimal bidding strategies for hydro-electric producers: A literature
  survey.
  IEEE Transactions on Power Systems, 29(4):1758–1766, 2014.
* [19]

  Stylianos I Vagropoulos and Anastasios G Bakirtzis.
  Optimal bidding strategy for electric vehicle aggregators in
  electricity markets.
  IEEE Transactions on power systems, 28(4):4031–4041, 2013.
* [20]

  Marina González Vayá and Göran Andersson.
  Optimal bidding strategy of a plug-in electric vehicle aggregator in
  day-ahead electricity markets under uncertainty.
  IEEE transactions on power systems, 30(5):2375–2385, 2014.
* [21]

  Zhiwei Xu, Zechun Hu, Yonghua Song, and Jianhui Wang.
  Risk-averse optimal bidding strategy for demand-side resource
  aggregators in day-ahead electricity markets under uncertainty.
  IEEE Transactions on Smart Grid, 8(1):96–105, 2015.
* [22]

  Haifeng Zhang, Feng Gao, Jiang Wu, Kun Liu, and Xiaolin Liu.
  Optimal bidding strategies for wind power producers in the day-ahead
  electricity market.
  Energies, 5(11):4804–4823, 2012.

## Appendix A

### 7.1 Case A

In this case we suppose that 0≤b<140\leq b<\frac{1}{4}, thus ([4](https://arxiv.org/html/2510.07025v1#S2.E4 "In 2.3 Simple bidding ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")) may be written as

|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫b1412​(x+y−cs−2​cv)​𝑑x+∫143432​(x+y−cs−2​cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{b}^{1}\left(\int\_{b}^{\frac{1}{4}}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dx+\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{3}{2}(x+y-c\_{s}-2c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫34112​(x+y−cs−2​cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{b}^{1}\left(\int\_{\frac{3}{4}}^{1}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫0b(∫b1412​(x−cs−cv)​𝑑x+∫143432​(x−cs−cv)​𝑑x+∫34112​(x−cs−cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{0}^{b}\left(\int\_{b}^{\frac{1}{4}}\frac{1}{2}(x-c\_{s}-c\_{v})dx+\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{3}{2}(x-c\_{s}-c\_{v})dx+\int\_{\frac{3}{4}}^{1}\frac{1}{2}(x-c\_{s}-c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫0b12​(y−cs−cv)​𝑑x)​ρp2​(y)​𝑑y=\displaystyle\int\_{b}^{1}\left(\int\_{0}^{b}\frac{1}{2}(y-c\_{s}-c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy= |  |

|  |  |  |
| --- | --- | --- |
|  | ∫b14∫b1412​12​(x+y−cs−2​cv)​𝑑x​𝑑y+∫b14∫143412​32​(x+y−cs−2​cv)​𝑑x​𝑑y+\displaystyle\int\_{b}^{\frac{1}{4}}\int\_{b}^{\frac{1}{4}}\frac{1}{2}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dxdy+\int\_{b}^{\frac{1}{4}}\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{1}{2}\frac{3}{2}(x+y-c\_{s}-2c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∫b14∫34112​12​(x+y−cs−2​cv)​𝑑x​𝑑y​∫1434∫b1432​12​(x+y−cs−2​cv)​𝑑x​𝑑y+\displaystyle+\int\_{b}^{\frac{1}{4}}\int\_{\frac{3}{4}}^{1}\frac{1}{2}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dxdy\int\_{\frac{1}{4}}^{\frac{3}{4}}\int\_{b}^{\frac{1}{4}}\frac{3}{2}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∫1434∫143432​32​(x+y−cs−2​cv)​𝑑x​𝑑y+∫1434∫34132​12​(x+y−cs−2​cv)​𝑑x​𝑑y+\displaystyle+\int\_{\frac{1}{4}}^{\frac{3}{4}}\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{3}{2}\frac{3}{2}(x+y-c\_{s}-2c\_{v})dxdy+\int\_{\frac{1}{4}}^{\frac{3}{4}}\int\_{\frac{3}{4}}^{1}\frac{3}{2}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫341∫b1412​12​(x+y−cs−2​cv)​𝑑x​𝑑y+∫341∫143412​32​(x+y−cs−2​cv)​𝑑x​𝑑y+\displaystyle\int\_{\frac{3}{4}}^{1}\int\_{b}^{\frac{1}{4}}\frac{1}{2}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dxdy+\int\_{\frac{3}{4}}^{1}\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{1}{2}\frac{3}{2}(x+y-c\_{s}-2c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∫341∫34112​12​(x+y−cs−2​cv)​𝑑x​𝑑y​∫0b∫b1412​12​(x−cs−cv)​𝑑x​𝑑y+\displaystyle+\int\_{\frac{3}{4}}^{1}\int\_{\frac{3}{4}}^{1}\frac{1}{2}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dxdy\int\_{0}^{b}\int\_{b}^{\frac{1}{4}}\frac{1}{2}\frac{1}{2}(x-c\_{s}-c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∫0b∫143412​32​(x−cs−cv)​𝑑x​𝑑y+∫0b∫34112​12​(x−cs−cv)​𝑑x​𝑑y+\displaystyle+\int\_{0}^{b}\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{1}{2}\frac{3}{2}(x-c\_{s}-c\_{v})dxdy+\int\_{0}^{b}\int\_{\frac{3}{4}}^{1}\frac{1}{2}\frac{1}{2}(x-c\_{s}-c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫b14∫0b12​12​(y−cs−cv)​𝑑x​𝑑y+∫1434∫0b32​12​(y−cs−cv)​𝑑x​𝑑y+\displaystyle\int\_{b}^{\frac{1}{4}}\int\_{0}^{b}\frac{1}{2}\frac{1}{2}(y-c\_{s}-c\_{v})dxdy+\int\_{\frac{1}{4}}^{\frac{3}{4}}\int\_{0}^{b}\frac{3}{2}\frac{1}{2}(y-c\_{s}-c\_{v})dxdy+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∫341∫0b12​12​(y−cs−cv)​𝑑x​𝑑y=\displaystyle+\int\_{\frac{3}{4}}^{1}\int\_{0}^{b}\frac{1}{2}\frac{1}{2}(y-c\_{s}-c\_{v})dxdy= |  |

Wolram Alpha [Wolfram] has been used for algebraic simplification.

|  |  |  |
| --- | --- | --- |
|  | 1256​(1−4​b)2​(4​b−4​cs−8​cv+1)−3256​(4​b−1)​(4​b−8​cs−16​cv+5)\displaystyle\frac{1}{256}(1-4b)^{2}(4b-4c\_{s}-8c\_{v}+1)-\frac{3}{256}(4b-1)(4b-8c\_{s}-16c\_{v}+5) |  |
|  |  |  |
| --- | --- | --- |
|  | −1128​(4​b−1)​(b−2​cs−4​cv+2)−3256​(4​b−1)​(4​b−8​cs−16​cv+5)\displaystyle-\frac{1}{128}(4b-1)(b-2c\_{s}-4c\_{v}+2)-\frac{3}{256}(4b-1)(4b-8c\_{s}-16c\_{v}+5) |  |
|  |  |  |
| --- | --- | --- |
|  | −916​(cs+2​cv−1)−1256​(8​cs+16​cv−11)−1128​(4​b−1)​(b−2​cs−4​cv+2)\displaystyle-\frac{9}{16}(c\_{s}+2c\_{v}-1)-\frac{1}{256}(8c\_{s}+16c\_{v}-11)-\frac{1}{128}(4b-1)(b-2c\_{s}-4c\_{v}+2) |  |
|  |  |  |
| --- | --- | --- |
|  | −3256​(8​cs+16​cv−11)+1256​(−4​cs−8​cv+7)−1128​b​(4​b−1)​(4​b−8​cs−8​cv+1)\displaystyle-\frac{3}{256}(8c\_{s}+16c\_{v}-11)+\frac{1}{256}(-4c\_{s}-8c\_{v}+7)-\frac{1}{128}b(4b-1)(4b-8c\_{s}-8c\_{v}+1) |  |
|  |  |  |
| --- | --- | --- |
|  | −316​b​(2​cs+2​cv−1)−1128​b​(8​cs+8​cv−7)−1128​b​(4​b−1)​(4​b−8​cs−8​cv+1)\displaystyle-\frac{3}{16}b(2c\_{s}+2c\_{v}-1)-\frac{1}{128}b(8c\_{s}+8c\_{v}-7)-\frac{1}{128}b(4b-1)(4b-8c\_{s}-8c\_{v}+1) |  |
|  |  |  |
| --- | --- | --- |
|  | −316​b​(2​cs+2​cv−1)−1128​b​(8​cs+8​cv−7)=\displaystyle-\frac{3}{16}b(2c\_{s}+2c\_{v}-1)-\frac{1}{128}b(8c\_{s}+8c\_{v}-7)= |  |

|  |  |  |
| --- | --- | --- |
|  | =−2​b2+b2​cs+4​b​cv−4​cs−8​cv+44=\frac{-2b^{2}+b^{2}c\_{s}+4bc\_{v}-4c\_{s}-8c\_{v}+4}{4} |  |

### 7.2 Case B

In this case we suppose that 14≤b<34\frac{1}{4}\leq b<\frac{3}{4}, thus Eq. ([4](https://arxiv.org/html/2510.07025v1#S2.E4 "In 2.3 Simple bidding ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")) may be written as

|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫b3432​(x+y−cs−2​cv)​𝑑x+∫34112​(x+y−cs−2​cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{b}^{1}\left(\int\_{b}^{\frac{3}{4}}\frac{3}{2}(x+y-c\_{s}-2c\_{v})dx+\int\_{\frac{3}{4}}^{1}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫0b(∫b3432​(x−cs−cv)​𝑑x+∫34112​(x−cs−cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{0}^{b}\left(\int\_{b}^{\frac{3}{4}}\frac{3}{2}(x-c\_{s}-c\_{v})dx+\int\_{\frac{3}{4}}^{1}\frac{1}{2}(x-c\_{s}-c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫01412​(y−cs−cv)​𝑑x+∫14b32​(y−cs−cv)​𝑑x)​ρp2​(y)​𝑑y\displaystyle\int\_{b}^{1}\left(\int\_{0}^{\frac{1}{4}}\frac{1}{2}(y-c\_{s}-c\_{v})dx+\int\_{\frac{1}{4}}^{b}\frac{3}{2}(y-c\_{s}-c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy |  |

Which is equal to:

|  |  |  |
| --- | --- | --- |
|  | −24​b2+36​b2​cs+48​b​cv−12​b​cs−40​cv−15​cs+1716\frac{-24b^{2}+36b^{2}c\_{s}+48bc\_{v}-12bc\_{s}-40c\_{v}-15c\_{s}+17}{16} |  |

### 7.3 Case C

In this case we suppose that 34≤b≤1\frac{3}{4}\leq b\leq 1, thus Eq. ([4](https://arxiv.org/html/2510.07025v1#S2.E4 "In 2.3 Simple bidding ‣ 2 Methods ‣ Optimal bidding in multiperiod day-ahead electricity markets assuming non-uniform uncertainty of clearing prices")) may be written as

|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫b112​(x+y−cs−2​cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{b}^{1}\left(\int\_{b}^{1}\frac{1}{2}(x+y-c\_{s}-2c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫0b(∫b112​(x−cs−cv)​𝑑x)​ρp2​(y)​𝑑y+\displaystyle\int\_{0}^{b}\left(\int\_{b}^{1}\frac{1}{2}(x-c\_{s}-c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy+ |  |
|  |  |  |
| --- | --- | --- |
|  | ∫b1(∫01412​(y−cs−cv)​𝑑x+∫143432​(y−cs−cv)​𝑑x+∫34b12​(y−cs−cv)​𝑑x)​ρp2​(y)​𝑑y\displaystyle\int\_{b}^{1}\left(\int\_{0}^{\frac{1}{4}}\frac{1}{2}(y-c\_{s}-c\_{v})dx+\int\_{\frac{1}{4}}^{\frac{3}{4}}\frac{3}{2}(y-c\_{s}-c\_{v})dx+\int\_{\frac{3}{4}}^{b}\frac{1}{2}(y-c\_{s}-c\_{v})dx\right)\rho\_{p\_{2}}(y)\penalty 10000\ dy |  |

Which is equal to:

|  |  |  |
| --- | --- | --- |
|  | −2​b2+b2​cs+4​b​cv+2​b​cs−4​cv−3​cs+24\frac{-2b^{2}+b^{2}c\_{s}+4bc\_{v}+2bc\_{s}-4c\_{v}-3c\_{s}+2}{4} |  |

### 7.4 Algebraic details in the case of multi-part bidding

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−bs312−bs2​bv2+bs2​cs8+bs2​cv4−bs​bv22+bs​bv​cs2+bs​bv​cv2\displaystyle=-\frac{{b\_{s}}^{3}}{12}-\frac{{b\_{s}}^{2}b\_{v}}{2}+\frac{{b\_{s}}^{2}c\_{s}}{8}+\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{b\_{s}{b\_{v}}^{2}}{2}+\frac{b\_{s}b\_{v}c\_{s}}{2}+\frac{b\_{s}b\_{v}c\_{v}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +bv2​cs4−bv22+bv​cv−cs−2​cv+1\displaystyle+\frac{{b\_{v}}^{2}c\_{s}}{4}-\frac{{b\_{v}}^{2}}{2}+b\_{v}c\_{v}-c\_{s}-2c\_{v}+1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−5​bs312−5​bs2​bv2+5​bs2​cs8+5​bs2​cv4+bs28−7​bs​bv22+5​bs​bv​cs2\displaystyle=-\frac{5{b\_{s}}^{3}}{12}-\frac{5{b\_{s}}^{2}b\_{v}}{2}+\frac{5{b\_{s}}^{2}c\_{s}}{8}+\frac{5{b\_{s}}^{2}c\_{v}}{4}+\frac{{b\_{s}}^{2}}{8}-\frac{7b\_{s}{b\_{v}}^{2}}{2}+\frac{5b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +7​bs​bv​cv2+bs​bv2−bs​cs4−bs​cv2−4​bv33+7​bv2​cs4+2​bv2​cv−bv28\displaystyle+\frac{7b\_{s}b\_{v}c\_{v}}{2}+\frac{b\_{s}b\_{v}}{2}-\frac{b\_{s}c\_{s}}{4}-\frac{b\_{s}c\_{v}}{2}-\frac{4{b\_{v}}^{3}}{3}+\frac{7{b\_{v}}^{2}c\_{s}}{4}+2{b\_{v}}^{2}c\_{v}-\frac{{b\_{v}}^{2}}{8} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −bv​cs2+bv​cv4−31​cs32−31​cv16+383384\displaystyle-\frac{b\_{v}c\_{s}}{2}+\frac{b\_{v}c\_{v}}{4}-\frac{31c\_{s}}{32}-\frac{31c\_{v}}{16}+\frac{383}{384} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−3​bs34−9​bs2​bv2+9​bs2​cs8+9​bs2​cv4+3​bs28−15​bs​bv22+9​bs​bv​cs2\displaystyle=-\frac{3{b\_{s}}^{3}}{4}-\frac{9{b\_{s}}^{2}b\_{v}}{2}+\frac{9{b\_{s}}^{2}c\_{s}}{8}+\frac{9{b\_{s}}^{2}c\_{v}}{4}+\frac{3{b\_{s}}^{2}}{8}-\frac{15b\_{s}{b\_{v}}^{2}}{2}+\frac{9b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +15​bs​bv​cv2+3​bs​bv2−3​bs​cs4−3​bs​cv2−4​bv3+15​bv2​cs4+6​bv2​cv\displaystyle+\frac{15b\_{s}b\_{v}c\_{v}}{2}+\frac{3b\_{s}b\_{v}}{2}-\frac{3b\_{s}c\_{s}}{4}-\frac{3b\_{s}c\_{v}}{2}-4{b\_{v}}^{3}+\frac{15{b\_{v}}^{2}c\_{s}}{4}+6{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +7​bv28−3​bv​cs2−7​bv​cv4−27​cs32−27​cv16+125128\displaystyle+\frac{7{b\_{v}}^{2}}{8}-\frac{3b\_{v}c\_{s}}{2}-\frac{7b\_{v}c\_{v}}{4}-\frac{27c\_{s}}{32}-\frac{27c\_{v}}{16}+\frac{125}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−5​bs312−5​bs2​bv2+5​bs2​cs8+5​bs2​cv4−9​bs​bv22+5​bs​bv​cs2+9​bs​bv​cv2\displaystyle=-\frac{5{b\_{s}}^{3}}{12}-\frac{5{b\_{s}}^{2}b\_{v}}{2}+\frac{5{b\_{s}}^{2}c\_{s}}{8}+\frac{5{b\_{s}}^{2}c\_{v}}{4}-\frac{9b\_{s}{b\_{v}}^{2}}{2}+\frac{5b\_{s}b\_{v}c\_{s}}{2}+\frac{9b\_{s}b\_{v}c\_{v}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −8​bv33+9​bv2​cs4+4​bv2​cv−bv24+bv​cv2−9​cs8−9​cv4+6764\displaystyle-\frac{8{b\_{v}}^{3}}{3}+\frac{9{b\_{v}}^{2}c\_{s}}{4}+4{b\_{v}}^{2}c\_{v}-\frac{{b\_{v}}^{2}}{4}+\frac{b\_{v}c\_{v}}{2}-\frac{9c\_{s}}{8}-\frac{9c\_{v}}{4}+\frac{67}{64} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs34+3​bs2​bv2−3​bs2​cs8−3​bs2​cv4−bs2+7​bs​bv22−3​bs​bv​cs2−7​bs​bv​cv2\displaystyle=\frac{{b\_{s}}^{3}}{4}+\frac{3{b\_{s}}^{2}b\_{v}}{2}-\frac{3{b\_{s}}^{2}c\_{s}}{8}-\frac{3{b\_{s}}^{2}c\_{v}}{4}-{b\_{s}}^{2}+\frac{7b\_{s}{b\_{v}}^{2}}{2}-\frac{3b\_{s}b\_{v}c\_{s}}{2}-\frac{7b\_{s}b\_{v}c\_{v}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −4​bs​bv+2​bs​cs+4​bs​cv+8​bv33−7​bv2​cs4−4​bv2​cv−17​bv24+4​bv​cs\displaystyle-4b\_{s}b\_{v}+2b\_{s}c\_{s}+4b\_{s}c\_{v}+\frac{8{b\_{v}}^{3}}{3}-\frac{7{b\_{v}}^{2}c\_{s}}{4}-4{b\_{v}}^{2}c\_{v}-\frac{17{b\_{v}}^{2}}{4}+4b\_{v}c\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +17​bv​cv2−17​cs8−17​cv4+265192\displaystyle+\frac{17b\_{v}c\_{v}}{2}-\frac{17c\_{s}}{8}-\frac{17c\_{v}}{4}+\frac{265}{192} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =5​bs312+5​bs2​bv2−5​bs2​cs8−5​bs2​cv4−5​bs24+5​bs​bv2−5​bs​bv​cs2\displaystyle=\frac{5{b\_{s}}^{3}}{12}+\frac{5{b\_{s}}^{2}b\_{v}}{2}-\frac{5{b\_{s}}^{2}c\_{s}}{8}-\frac{5{b\_{s}}^{2}c\_{v}}{4}-\frac{5{b\_{s}}^{2}}{4}+5b\_{s}{b\_{v}}^{2}-\frac{5b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −5​bs​bv​cv−5​bs​bv+5​bs​cs2+5​bs​cv+10​bv33−5​bv2​cs2−5​bv2​cv\displaystyle-5b\_{s}b\_{v}c\_{v}-5b\_{s}b\_{v}+\frac{5b\_{s}c\_{s}}{2}+5b\_{s}c\_{v}+\frac{10{b\_{v}}^{3}}{3}-\frac{5{b\_{v}}^{2}c\_{s}}{2}-5{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −5​bv2+5​bv​cs+10​bv​cv−19​cs8−19​cv4+281192\displaystyle-5{b\_{v}}^{2}+5b\_{v}c\_{s}+10b\_{v}c\_{v}-\frac{19c\_{s}}{8}-\frac{19c\_{v}}{4}+\frac{281}{192} |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =3​bs34+9​bs2​bv2−9​bs2​cs8−9​bs2​cv4−15​bs28+9​bs​bv2−9​bs​bv​cs2\displaystyle=\frac{3{b\_{s}}^{3}}{4}+\frac{9{b\_{s}}^{2}b\_{v}}{2}-\frac{9{b\_{s}}^{2}c\_{s}}{8}-\frac{9{b\_{s}}^{2}c\_{v}}{4}-\frac{15{b\_{s}}^{2}}{8}+9b\_{s}{b\_{v}}^{2}-\frac{9b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −9​bs​bv​cv−15​bs​bv2+15​bs​cs4+15​bs​cv2+6​bv3−9​bv2​cs2−9​bv2​cv\displaystyle-9b\_{s}b\_{v}c\_{v}-\frac{15b\_{s}b\_{v}}{2}+\frac{15b\_{s}c\_{s}}{4}+\frac{15b\_{s}c\_{v}}{2}+6{b\_{v}}^{3}-\frac{9{b\_{v}}^{2}c\_{s}}{2}-9{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −15​bv22+15​bv​cs2+15​bv​cv−101​cs32−101​cv16+229128\displaystyle-\frac{15{b\_{v}}^{2}}{2}+\frac{15b\_{v}c\_{s}}{2}+15b\_{v}c\_{v}-\frac{101c\_{s}}{32}-\frac{101c\_{v}}{16}+\frac{229}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =5​bs312+5​bs2​bv2−5​bs2​cs8−5​bs2​cv4−9​bs28+5​bs​bv2−5​bs​bv​cs2\displaystyle=\frac{5{b\_{s}}^{3}}{12}+\frac{5{b\_{s}}^{2}b\_{v}}{2}-\frac{5{b\_{s}}^{2}c\_{s}}{8}-\frac{5{b\_{s}}^{2}c\_{v}}{4}-\frac{9{b\_{s}}^{2}}{8}+5b\_{s}{b\_{v}}^{2}-\frac{5b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −5​bs​bv​cv−9​bs​bv2+9​bs​cs4+9​bs​cv2+10​bv33−5​bv2​cs2−5​bv2​cv\displaystyle-5b\_{s}b\_{v}c\_{v}-\frac{9b\_{s}b\_{v}}{2}+\frac{9b\_{s}c\_{s}}{4}+\frac{9b\_{s}c\_{v}}{2}+\frac{10{b\_{v}}^{3}}{3}-\frac{5{b\_{v}}^{2}c\_{s}}{2}-5{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −9​bv22+9​bv​cs2+9​bv​cv−65​cs32−65​cv16+157128\displaystyle-\frac{9{b\_{v}}^{2}}{2}+\frac{9b\_{v}c\_{s}}{2}+9b\_{v}c\_{v}-\frac{65c\_{s}}{32}-\frac{65c\_{v}}{16}+\frac{157}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs312+bs2​bv2−bs2​cs8−bs2​cv4−bs24+bs​bv2−bs​bv​cs2−bs​bv​cv−bs​bv\displaystyle=\frac{{b\_{s}}^{3}}{12}+\frac{{b\_{s}}^{2}b\_{v}}{2}-\frac{{b\_{s}}^{2}c\_{s}}{8}-\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{{b\_{s}}^{2}}{4}+b\_{s}{b\_{v}}^{2}-\frac{b\_{s}b\_{v}c\_{s}}{2}-b\_{s}b\_{v}c\_{v}-b\_{s}b\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +bs​cs2+bs​cv+2​bv33−bv2​cs2−bv2​cv−bv2+bv​cs+2​bv​cv−cs2−cv+13\displaystyle+\frac{b\_{s}c\_{s}}{2}+b\_{s}c\_{v}+\frac{2{b\_{v}}^{3}}{3}-\frac{{b\_{v}}^{2}c\_{s}}{2}-{b\_{v}}^{2}c\_{v}-{b\_{v}}^{2}+b\_{v}c\_{s}+2b\_{v}c\_{v}-\frac{c\_{s}}{2}-c\_{v}+\frac{1}{3} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−3​bs34−9​bs2​bv2+9​bs2​cs8+9​bs2​cv4+3​bs28−9​bs​bv22\displaystyle=-\frac{3{b\_{s}}^{3}}{4}-\frac{9{b\_{s}}^{2}b\_{v}}{2}+\frac{9{b\_{s}}^{2}c\_{s}}{8}+\frac{9{b\_{s}}^{2}c\_{v}}{4}+\frac{3{b\_{s}}^{2}}{8}-\frac{9b\_{s}{b\_{v}}^{2}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +9​bs​bv​cs2+9​bs​bv​cv2+3​bs​bv4−3​bs​cs4−3​bs​cv4+9​bv2​cs4\displaystyle+\frac{9b\_{s}b\_{v}c\_{s}}{2}+\frac{9b\_{s}b\_{v}c\_{v}}{2}+\frac{3b\_{s}b\_{v}}{4}-\frac{3b\_{s}c\_{s}}{4}-\frac{3b\_{s}c\_{v}}{4}+\frac{9{b\_{v}}^{2}c\_{s}}{4} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −3​bv22−3​bv​cs4+3​bv​cv−15​cs16−5​cv2+1716\displaystyle-\frac{3{b\_{v}}^{2}}{2}-\frac{3b\_{v}c\_{s}}{4}+3b\_{v}c\_{v}-\frac{15c\_{s}}{16}-\frac{5c\_{v}}{2}+\frac{17}{16} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs34+3​bs2​bv2−3​bs2​cs8−3​bs2​cv4−bs2+9​bs​bv22−3​bs​bv​cs2\displaystyle=\frac{{b\_{s}}^{3}}{4}+\frac{3{b\_{s}}^{2}b\_{v}}{2}-\frac{3{b\_{s}}^{2}c\_{s}}{8}-\frac{3{b\_{s}}^{2}c\_{v}}{4}-{b\_{s}}^{2}+\frac{9b\_{s}{b\_{v}}^{2}}{2}-\frac{3b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −9​bs​bv​cv2−17​bs​bv4+2​bs​cs+17​bs​cv4+4​bv3−9​bv2​cs4−6​bv2​cv\displaystyle-\frac{9b\_{s}b\_{v}c\_{v}}{2}-\frac{17b\_{s}b\_{v}}{4}+2b\_{s}c\_{s}+\frac{17b\_{s}c\_{v}}{4}+4{b\_{v}}^{3}-\frac{9{b\_{v}}^{2}c\_{s}}{4}-6{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −41​bv28+17​bv​cs4+41​bv​cv4−69​cs32−73​cv16+181128\displaystyle-\frac{41{b\_{v}}^{2}}{8}+\frac{17b\_{v}c\_{s}}{4}+\frac{41b\_{v}c\_{v}}{4}-\frac{69c\_{s}}{32}-\frac{73c\_{v}}{16}+\frac{181}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =3​bs34+9​bs2​bv2−9​bs2​cs8−9​bs2​cv4−15​bs28+9​bs​bv2−9​bs​bv​cs2\displaystyle=\frac{3{b\_{s}}^{3}}{4}+\frac{9{b\_{s}}^{2}b\_{v}}{2}-\frac{9{b\_{s}}^{2}c\_{s}}{8}-\frac{9{b\_{s}}^{2}c\_{v}}{4}-\frac{15{b\_{s}}^{2}}{8}+9b\_{s}{b\_{v}}^{2}-\frac{9b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −9​bs​bv​cv−15​bs​bv2+15​bs​cs4+15​bs​cv2+6​bv3−9​bv2​cs2−9​bv2​cv\displaystyle-9b\_{s}b\_{v}c\_{v}-\frac{15b\_{s}b\_{v}}{2}+\frac{15b\_{s}c\_{s}}{4}+\frac{15b\_{s}c\_{v}}{2}+6{b\_{v}}^{3}-\frac{9{b\_{v}}^{2}c\_{s}}{2}-9{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −15​bv22+15​bv​cs2+15​bv​cv−101​cs32−101​cv16+229128\displaystyle-\frac{15{b\_{v}}^{2}}{2}+\frac{15b\_{v}c\_{s}}{2}+15b\_{v}c\_{v}-\frac{101c\_{s}}{32}-\frac{101c\_{v}}{16}+\frac{229}{128} |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =5​bs312+5​bs2​bv2−5​bs2​cs8−5​bs2​cv4−9​bs28+5​bs​bv2−5​bs​bv​cs2\displaystyle=\frac{5{b\_{s}}^{3}}{12}+\frac{5{b\_{s}}^{2}b\_{v}}{2}-\frac{5{b\_{s}}^{2}c\_{s}}{8}-\frac{5{b\_{s}}^{2}c\_{v}}{4}-\frac{9{b\_{s}}^{2}}{8}+5b\_{s}{b\_{v}}^{2}-\frac{5b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −5​bs​bv​cv−9​bs​bv2+9​bs​cs4+9​bs​cv2+10​bv33−5​bv2​cs2−5​bv2​cv\displaystyle-5b\_{s}b\_{v}c\_{v}-\frac{9b\_{s}b\_{v}}{2}+\frac{9b\_{s}c\_{s}}{4}+\frac{9b\_{s}c\_{v}}{2}+\frac{10{b\_{v}}^{3}}{3}-\frac{5{b\_{v}}^{2}c\_{s}}{2}-5{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −9​bv22+9​bv​cs2+9​bv​cv−65​cs32−65​cv16+157128\displaystyle-\frac{9{b\_{v}}^{2}}{2}+\frac{9b\_{v}c\_{s}}{2}+9b\_{v}c\_{v}-\frac{65c\_{s}}{32}-\frac{65c\_{v}}{16}+\frac{157}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs312+bs2​bv2−bs2​cs8−bs2​cv4−bs24+bs​bv2−bs​bv​cs2−bs​bv​cv−bs​bv\displaystyle=\frac{{b\_{s}}^{3}}{12}+\frac{{b\_{s}}^{2}b\_{v}}{2}-\frac{{b\_{s}}^{2}c\_{s}}{8}-\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{{b\_{s}}^{2}}{4}+b\_{s}{b\_{v}}^{2}-\frac{b\_{s}b\_{v}c\_{s}}{2}-b\_{s}b\_{v}c\_{v}-b\_{s}b\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +bs​cs2+bs​cv+2​bv33−bv2​cs2−bv2​cv−bv2+bv​cs+2​bv​cv−cs2−cv+13\displaystyle+\frac{b\_{s}c\_{s}}{2}+b\_{s}c\_{v}+\frac{2{b\_{v}}^{3}}{3}-\frac{{b\_{v}}^{2}c\_{s}}{2}-{b\_{v}}^{2}c\_{v}-{b\_{v}}^{2}+b\_{v}c\_{s}+2b\_{v}c\_{v}-\frac{c\_{s}}{2}-c\_{v}+\frac{1}{3} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−3​bs34−9​bs2​bv2+9​bs2​cs8+9​bs2​cv4+3​bs28−9​bs​bv22\displaystyle=-\frac{3{b\_{s}}^{3}}{4}-\frac{9{b\_{s}}^{2}b\_{v}}{2}+\frac{9{b\_{s}}^{2}c\_{s}}{8}+\frac{9{b\_{s}}^{2}c\_{v}}{4}+\frac{3{b\_{s}}^{2}}{8}-\frac{9b\_{s}{b\_{v}}^{2}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +9​bs​bv​cs2+9​bs​bv​cv2+3​bs​bv4−3​bs​cs4−3​bs​cv4+9​bv2​cs4\displaystyle+\frac{9b\_{s}b\_{v}c\_{s}}{2}+\frac{9b\_{s}b\_{v}c\_{v}}{2}+\frac{3b\_{s}b\_{v}}{4}-\frac{3b\_{s}c\_{s}}{4}-\frac{3b\_{s}c\_{v}}{4}+\frac{9{b\_{v}}^{2}c\_{s}}{4} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −3​bv22−3​bv​cs4+3​bv​cv−15​cs16−5​cv2+1716\displaystyle-\frac{3{b\_{v}}^{2}}{2}-\frac{3b\_{v}c\_{s}}{4}+3b\_{v}c\_{v}-\frac{15c\_{s}}{16}-\frac{5c\_{v}}{2}+\frac{17}{16} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs34+3​bs2​bv2−3​bs2​cs8−3​bs2​cv4−bs2+9​bs​bv22−3​bs​bv​cs2\displaystyle=\frac{{b\_{s}}^{3}}{4}+\frac{3{b\_{s}}^{2}b\_{v}}{2}-\frac{3{b\_{s}}^{2}c\_{s}}{8}-\frac{3{b\_{s}}^{2}c\_{v}}{4}-{b\_{s}}^{2}+\frac{9b\_{s}{b\_{v}}^{2}}{2}-\frac{3b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −9​bs​bv​cv2−17​bs​bv4+2​bs​cs+17​bs​cv4+4​bv3−9​bv2​cs4−6​bv2​cv\displaystyle-\frac{9b\_{s}b\_{v}c\_{v}}{2}-\frac{17b\_{s}b\_{v}}{4}+2b\_{s}c\_{s}+\frac{17b\_{s}c\_{v}}{4}+4{b\_{v}}^{3}-\frac{9{b\_{v}}^{2}c\_{s}}{4}-6{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −41​bv28+17​bv​cs4+41​bv​cv4−69​cs32−73​cv16+181128\displaystyle-\frac{41{b\_{v}}^{2}}{8}+\frac{17b\_{v}c\_{s}}{4}+\frac{41b\_{v}c\_{v}}{4}-\frac{69c\_{s}}{32}-\frac{73c\_{v}}{16}+\frac{181}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−bs312−bs2​bv2+bs2​cs8+bs2​cv4−bs24+bs​bv22+bs​bv​cs2\displaystyle=-\frac{{b\_{s}}^{3}}{12}-\frac{{b\_{s}}^{2}b\_{v}}{2}+\frac{{b\_{s}}^{2}c\_{s}}{8}+\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{{b\_{s}}^{2}}{4}+\frac{b\_{s}{b\_{v}}^{2}}{2}+\frac{b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −bs​bv​cv2−5​bs​bv4+bs​cs2+5​bs​cv4+4​bv33−bv2​cs4−2​bv2​cv\displaystyle-\frac{b\_{s}b\_{v}c\_{v}}{2}-\frac{5b\_{s}b\_{v}}{4}+\frac{b\_{s}c\_{s}}{2}+\frac{5b\_{s}c\_{v}}{4}+\frac{4{b\_{v}}^{3}}{3}-\frac{{b\_{v}}^{2}c\_{s}}{4}-2{b\_{v}}^{2}c\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −17​bv28+5​bv​cs4+17​bv​cv4−33​cs32−37​cv16+109128\displaystyle-\frac{17{b\_{v}}^{2}}{8}+\frac{5b\_{v}c\_{s}}{4}+\frac{17b\_{v}c\_{v}}{4}-\frac{33c\_{s}}{32}-\frac{37c\_{v}}{16}+\frac{109}{128} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =5​bs312+5​bs2​bv2−5​bs2​cs8−5​bs2​cv4−9​bs28+5​bs​bv2−5​bs​bv​cs2\displaystyle=\frac{5{b\_{s}}^{3}}{12}+\frac{5{b\_{s}}^{2}b\_{v}}{2}-\frac{5{b\_{s}}^{2}c\_{s}}{8}-\frac{5{b\_{s}}^{2}c\_{v}}{4}-\frac{9{b\_{s}}^{2}}{8}+5b\_{s}{b\_{v}}^{2}-\frac{5b\_{s}b\_{v}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −5​bs​bv​cv−9​bs​bv2+9​bs​cs4+9​bs​cv2+10​bv33−5​bv2​cs2\displaystyle-5b\_{s}b\_{v}c\_{v}-\frac{9b\_{s}b\_{v}}{2}+\frac{9b\_{s}c\_{s}}{4}+\frac{9b\_{s}c\_{v}}{2}+\frac{10{b\_{v}}^{3}}{3}-\frac{5{b\_{v}}^{2}c\_{s}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −5​bv2​cv−9​bv22+9​bv​cs2+9​bv​cv−65​cs32−65​cv16+157128\displaystyle-5{b\_{v}}^{2}c\_{v}-\frac{9{b\_{v}}^{2}}{2}+\frac{9b\_{v}c\_{s}}{2}+9b\_{v}c\_{v}-\frac{65c\_{s}}{32}-\frac{65c\_{v}}{16}+\frac{157}{128} |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs312+bs2​bv2−bs2​cs8−bs2​cv4−bs24+bs​bv2−bs​bv​cs2−bs​bv​cv−bs​bv\displaystyle=\frac{{b\_{s}}^{3}}{12}+\frac{{b\_{s}}^{2}b\_{v}}{2}-\frac{{b\_{s}}^{2}c\_{s}}{8}-\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{{b\_{s}}^{2}}{4}+b\_{s}{b\_{v}}^{2}-\frac{b\_{s}b\_{v}c\_{s}}{2}-b\_{s}b\_{v}c\_{v}-b\_{s}b\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +bs​cs2+bs​cv+2​bv33−bv2​cs2−bv2​cv−bv2+bv​cs+2​bv​cv−cs2−cv+13\displaystyle+\frac{b\_{s}c\_{s}}{2}+b\_{s}c\_{v}+\frac{2{b\_{v}}^{3}}{3}-\frac{{b\_{v}}^{2}c\_{s}}{2}-{b\_{v}}^{2}c\_{v}-{b\_{v}}^{2}+b\_{v}c\_{s}+2b\_{v}c\_{v}-\frac{c\_{s}}{2}-c\_{v}+\frac{1}{3} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =−bs312−bs2​bv2+bs2​cs8+bs2​cv4−bs24−bs​bv22+bs​bv​cs2+bs​bv​cv2\displaystyle=-\frac{{b\_{s}}^{3}}{12}-\frac{{b\_{s}}^{2}b\_{v}}{2}+\frac{{b\_{s}}^{2}c\_{s}}{8}+\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{{b\_{s}}^{2}}{4}-\frac{b\_{s}{b\_{v}}^{2}}{2}+\frac{b\_{s}b\_{v}c\_{s}}{2}+\frac{b\_{s}b\_{v}c\_{v}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −bs​bv2+bs​cs2+bs​cv2+bv2​cs4−bv22+bv​cs2+bv​cv−3​cs4−cv+12\displaystyle-\frac{b\_{s}b\_{v}}{2}+\frac{b\_{s}c\_{s}}{2}+\frac{b\_{s}c\_{v}}{2}+\frac{{b\_{v}}^{2}c\_{s}}{4}-\frac{{b\_{v}}^{2}}{2}+\frac{b\_{v}c\_{s}}{2}+b\_{v}c\_{v}-\frac{3c\_{s}}{4}-c\_{v}+\frac{1}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[πM​(bs,bv)]\displaystyle E[\pi\_{M}(b\_{s},b\_{v})] | =bs312+bs2​bv2−bs2​cs8−bs2​cv4−bs24+bs​bv2−bs​bv​cs2−bs​bv​cv−bs​bv\displaystyle=\frac{{b\_{s}}^{3}}{12}+\frac{{b\_{s}}^{2}b\_{v}}{2}-\frac{{b\_{s}}^{2}c\_{s}}{8}-\frac{{b\_{s}}^{2}c\_{v}}{4}-\frac{{b\_{s}}^{2}}{4}+b\_{s}{b\_{v}}^{2}-\frac{b\_{s}b\_{v}c\_{s}}{2}-b\_{s}b\_{v}c\_{v}-b\_{s}b\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +bs​cs2+bs​cv+2​bv33−bv2​cs2−bv2​cv−bv2+bv​cs+2​bv​cv−cs2−cv+13\displaystyle+\frac{b\_{s}c\_{s}}{2}+b\_{s}c\_{v}+\frac{2{b\_{v}}^{3}}{3}-\frac{{b\_{v}}^{2}c\_{s}}{2}-{b\_{v}}^{2}c\_{v}-{b\_{v}}^{2}+b\_{v}c\_{s}+2b\_{v}c\_{v}-\frac{c\_{s}}{2}-c\_{v}+\frac{1}{3} |  |