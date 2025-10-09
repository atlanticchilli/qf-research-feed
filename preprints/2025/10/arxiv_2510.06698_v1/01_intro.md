---
authors:
- Raquel M. Gaspar
- Thorsten Schmidt
doc_id: arxiv:2510.06698v1
family_id: arxiv:2510.06698
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Insurance products with guarantees in an affine setting
url_abs: http://arxiv.org/abs/2510.06698v1
url_html: https://arxiv.org/html/2510.06698v1
venue: arXiv q-fin
version: 1
year: 2025
---


Raquel M. Gaspar
ISEG Research, Lisbon School of Economics and Management, Universidade de Lisboa, Portugal
[rmgaspar@iseg.ulisboa.pt](mailto:rmgaspar@iseg.ulisboa.pt)
 and 
Thorsten Schmidt
Department of Mathematical Stochastics, University of Freiburg, Germany
[thorsten.schmidt@stochastik.uni-freiburg.de](mailto:thorsten.schmidt@stochastik.uni-freiburg.de)

###### Abstract.

For the attractivity of medium- and long-term insurance products
it is necessary to participate on the profitability of stock markets.
To eliminate downside-risk, guarantees should be included which naturally gives rise to the problem of valuing contracts in a unified insurance–finance framework.

We study a general setup that allows for joint modelling of financial markets, mortality, and policyholder behaviour. Within this framework, we propose a general affine approach and obtain explicit valuation formulas for variable annuities and related contracts that remain computationally tractable due to the affine structure. The model permits flexible dependence between mortality and equity dynamics, as highlighted by the empirical evidence from the COVID-19 pandemic. Moreover, surrender intensities are modelled as functions of the driving affine process, thereby introducing market dependence into lapse behaviour. The resulting framework combines analytical tractability with sufficient flexibility to capture key features of long-term insurance products.

The work of R.M. Gaspar was partially supported by FCT, I.P., the Portuguese national funding agency for science, research and technology, under the Project UID06522. We also thank the MAPFRE foundation for support through the Research Grant Ignacio H. de Larramendi. The work of T. Schmidt was partially supported by a grant from Deutsche Forschungsgemeinschaft under the project SCHM 2160/15-1. Support of the FDMAI is gratefully acknowledged. We want to thank Wilfried Donatien Kuissi Kamdem and Felix Tambe Ndonfack for a careful reading of the manuscript and David Criens for his comments on an earlier version of the manuscript.

## 1. Introduction

The design of retirement products, and more generally medium- and long-term insurance products, remains one of the central challenges in modern insurance mathematics since longevity, low interest rates and uncertainty about asset returns must be handled in an cost-efficient and risk-sensitive manner. Variable annuities and related products form an important class in this context, combining participation in equity markets with embedded guarantees to reduce risk. Their valuation and risk-management poses significant challenges, in particular over a long time horizon.

We start in a general setup in discrete time and show how to obtain valuation formulas that guarantee absence of insurance-finance arbitrage in the sense of Artzner et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib3)). To obtain tractable results we use enlargement of filtration techniques and derive quite general results for one, two or possibly more stopping times related to the contract (like mortality and surrender).

Towards a flexible and tractable setting, we propose to use affine models. Affine processes constitute a flexible and highly tractable class which makes them well suited for the problem at hand.
In contrast to many existing approaches we allow for a quite general dependence between insurance and finance products, which leads to technical difficulties. In particular, we address the valuation problem when both mortality and surrender are possibly correlated to the financial markets. We propose to use enlargement-of-filtration techniques which are, to the best of our knowledge, applied in this form for the first time to the valuation of insurance products. The considered framework also allows to incorporate more than two stopping times.

In the literature, different approaches have been proposed for the valuation of variable annuities and similar products (see e.g., Dhaene et al. ([2017](https://arxiv.org/html/2510.06698v1#bib.bib13)), Dhaene et al. ([2013](https://arxiv.org/html/2510.06698v1#bib.bib12)), Pelsser and Stadje ([2014](https://arxiv.org/html/2510.06698v1#bib.bib25)) and Malamud et al. ([2008](https://arxiv.org/html/2510.06698v1#bib.bib22)) and references therein). More recently, 2-step and 3-step approaches have been proposed as for example in Deelstra et al. ([2020](https://arxiv.org/html/2510.06698v1#bib.bib11)); Barigou et al. ([2023](https://arxiv.org/html/2510.06698v1#bib.bib5)) and in Linders ([2023](https://arxiv.org/html/2510.06698v1#bib.bib21)). Extensions of the insurance-finance framework we consider here to uncertainty can be found in Oberpriller et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib24)) and to the benchmark approach in Platen et al. ([2025](https://arxiv.org/html/2510.06698v1#bib.bib26)).

On the other side, tontines and related products have been proposed as competitive pension products and we refer to Milevsky and Salisbury ([2015](https://arxiv.org/html/2510.06698v1#bib.bib23)), Winter and Planchet ([2022](https://arxiv.org/html/2510.06698v1#bib.bib27)), Chen et al. ([2020](https://arxiv.org/html/2510.06698v1#bib.bib10)), Chen et al. ([2019](https://arxiv.org/html/2510.06698v1#bib.bib9)) and further literature therein.

The paper is organised as follows: in Section [2](https://arxiv.org/html/2510.06698v1#S2 "2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting") we introduce insurance-finance markets and provide with Theorem [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting") an fundamental theorem which will be used later on for valuation without insurance-finance arbitrage, a so-called IFA-free valuation. In Section [3](https://arxiv.org/html/2510.06698v1#S3 "3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting") we introduce the framework for insurance products with guarantees, which include variable annuities as a special case. Proposition [3.1](https://arxiv.org/html/2510.06698v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting") as a key result provides IFA-free valuation formulas for all building blocks of a variable annuity with guarantee, surrender and death benefit. For more explicit and tractable formulas we will use enlargements of filtrations, which are introduced in section [4](https://arxiv.org/html/2510.06698v1#S4 "4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting"). In particular, results for multiple stopping times are given and the setting for two stopping times (mortality and surrender) is developed in more detail. Section [5](https://arxiv.org/html/2510.06698v1#S5 "5. An affine framework ‣ Insurance products with guarantees in an affine setting") introduces a general affine process under the statistical and the risk-neutral measure and develops the key formulas needed for the valuation. Section [6](https://arxiv.org/html/2510.06698v1#S6 "6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting") provides the valuation results for the building blocks of a variable annuity in an affine framework and Section [7](https://arxiv.org/html/2510.06698v1#S7 "7. Conclusion ‣ Insurance products with guarantees in an affine setting") concludes.

## 2. Insurance-finance markets and arbitrage-free valuation

We follow Artzner et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib3)) and consider financial markets and insurance contracts with minimal assumptions on their dependence. To this end, consider a probability space (Ω,ℋ,P)(\Omega,{\mathscr{H}},P) and a discrete, finite time interval 𝕋={0,1,…,T}\mathbb{T}=\{0,1,...,T\}. Information is divided into publicly available information (like stock prices, life tables, etc.), captured by the filtration
𝔽=(ℱt)t∈𝕋\mathbb{F}=({\mathscr{F}}\_{t})\_{t\in\mathbb{T}} and internal information only available to the considered insurance company. This are typically the survival times of the insured clients, together with further information on the clients, like for example health states, encoded in the filtration ℍ=(ℋt)t∈𝕋\mathbb{H}=({\mathscr{H}}\_{t})\_{t\in\mathbb{T}}. We assume that ℍ\mathbb{H} already encompasses public information , i.e.

|  |  |  |
| --- | --- | --- |
|  | ℱt⊆ℋtfor ​t=0,…,T.\displaystyle{\mathscr{F}}\_{t}\subseteq{\mathscr{H}}\_{t}\quad\text{for }t=0,\dots,T. |  |

###### Remark 2.1 (Choice of the filtrations).

The main role of 𝔽\mathbb{F} is to capture information which does *not* introduce arbitrage on the financial market or changes the market pricing, see Theorem [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting") for the precise statement. Hence, one could also include insurance information here, as long as no financial arbitrage is created, which would both simplify pricing and hedging.
In contrast, the role of ℍ\mathbb{H} is to be general enough to capture insurance information which possibly could lead to an arbitrage on the financial market. Using this information is forbidden, however, by the law of insider trading.
In Artzner et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib3)), an additional filtration 𝔾\mathbb{G} was introduced to precisely capture this effect, while here - for simplicity - we stay with two filtrations only.

### 2.1. The financial market

The financial market consists of the risk-free account and dd tradeable securities. Discounted price processes of the tradeable securities are given by the 𝔽\mathbb{F}-adapted process S=(S1,…,Sd)S=(S^{1},\dots,S^{d}).

A *trading strategy* on the financial market is a dd-dimensional, 𝔽\mathbb{F}-adapted process ξ=(ξt)0≤t≤T−1\xi=(\xi\_{t})\_{0\leq t\leq T-1} with ξt=(ξt1,…,ξtd)\xi\_{t}=(\xi^{1}\_{t},\dots,\xi^{d}\_{t}). For a trading strategy, its *(discounted) value*
is given by (see for example Föllmer and Schied ([2011](https://arxiv.org/html/2510.06698v1#bib.bib16)), Proposition 5.7),

|  |  |  |
| --- | --- | --- |
|  | VF​(ξ):=(ξ⋅S)T=∑t=0T−1∑j=1dξtj​Δ​Stj,V^{F}(\xi):=(\xi\cdot S)\_{T}=\sum\_{t=0}^{T-1}\sum\_{j=1}^{d}\xi^{j}\_{t}\;\Delta S^{j}\_{t}, |  |

with Δ​St=St+1−St\Delta S\_{t}=S\_{t+1}-S\_{t}.
Here we choose to add the superscript FF to emphasize that VV is the value of trading on the financial market.

It is well-known that the financial market is arbitrage free if there exists an equivalent martingale measure. For the following we will therefore assume that the set ℳe,b​(S,𝔽){\mathscr{M}}\_{e,b}(S,\mathbb{F}) of equivalent martingale measures with bounded densities is not empty.

### 2.2. The insurance market

Besides trading on the financial market, the insurance company can build a portfolio of insurance contracts. We assume that the insurance company can contract with possibly infinitely many *insurance seekers*.

We concentrate on one type of insurance contract.
Such a contract, initiated at time tt, offers *benefits* at maturity TT which can be identified with a ℋT{\mathscr{H}}\_{T}-measurable non-negative random variable Xt,TX\_{t,T} (already discounted). In exchange for this benefits, the insured pays a non-negative premium ptp\_{t} at tt, satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | pt∈L+1​(ℋt)=L+1​(Ω,ℋt,P).\displaystyle p\_{t}\in L^{1}\_{+}({\mathscr{H}}\_{t})=L^{1}\_{+}(\Omega,{\mathscr{H}}\_{t},P). |  | (1) |

While financial contracts are standardised, insurance contracts are individual: they are linked to personal quantities as for example the life time of the insured, such that each contract is different.

We consider a homogeneous cohort (say of the same gender, age and health state) which buy the same type of insurance contract and therefore will pay the same premium for the contract.
The associated ℋT{\mathscr{H}}\_{T}-measurable benefits of the individual contracts, however, are different and are denoted by Xt,T1,Xt,T2,…X^{1}\_{t,T},X^{2}\_{t,T},\dots\;.
With these, insurance trading at tt is described by an *insurance allocation* ψ=(ψti)t≥0,i≥1\psi=(\psi^{i}\_{t})\_{t\geq 0,i\geq 1}: for each t=0,…,T−1t=0,\dots,T-1, this is a ℋt{\mathscr{H}}\_{t}-measurable, non-negative random sequence, where ψti\psi^{i}\_{t} denotes the size of the contract with the it​hi^{th} insurance seeker.
The (discounted) value of the allocation is hence given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​(ψ):=∑t=0T−1∑i≥1ψti​(pt−Xt,Ti),\displaystyle V^{I}(\psi):=\sum\_{t=0}^{T-1}\sum\_{i\geq 1}\psi^{i}\_{t}\big(p\_{t}-X^{i}\_{t,T}\big), |  | (2) |

where II is used as superscript to describe the value of building an insurance allocation.

To obtain realistic strategies, we assume that in an allocation the insurance is allowed to trade only with finitely many contracts, whereafter we take limits. More precisely, an *insurance portfolio strategy* is a sequence ψ:=(ψn)n≥1\psi:=(\psi^{n})\_{n\geq 1} of allocations. Each allocation ψn=(ψtn,i)t≥0,i≥1\psi^{n}=(\psi\_{t}^{n,i})\_{t\geq 0,i\geq 1} has only finitely many non-negative entries. In addition, we impose the following *admissibility condition* for a portfolio strategy:
*Convergence of the insurance volume*: there exist random variables γt≥0\gamma\_{t}\geq 0, 0≤t<T0\leq t<T so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ψtn‖:=∑i≥1ψtn,i→γta.s. for all ​t<T.\displaystyle\parallel\psi^{n}\_{t}\parallel:=\sum\_{i\geq 1}~\psi^{n,i}\_{t}\rightarrow\gamma\_{t}\quad\text{a.s. for all }t<T. |  | (3) |

The precise measurability of γt\gamma\_{t} is explained in the next subsection.
Later, we are interested in the particular case of a bounded portfolio strategy:
in addition to ([3](https://arxiv.org/html/2510.06698v1#S2.E3 "In 2.2. The insurance market ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting")) we say that the portfolio strategy ψ\psi is *bounded* if there exists c>0c>0 so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ψtn‖≤c.\displaystyle\parallel\psi^{n}\_{t}\parallel\leq c. |  | (4) |

for all n≥1n\geq 1 and 0≤t<T0\leq t<T.

It turns out that the σ\sigma-algebra

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋt,T:=ℋt∨ℱT\displaystyle{\mathscr{H}}\_{t,T}:={\mathscr{H}}\_{t}\vee{\mathscr{F}}\_{T} |  | (5) |

containing the insurance information up to date tt and ℱT{\mathscr{F}}\_{T}, plays a distinctive role.
We make the following assumptions:

###### Assumption 2.1.

For all t∈𝕋t\in\mathbb{T}, the standard contract Xt,T∈L2​(Ω,ℋT,P)X\_{t,T}\in L^{2}(\Omega,{\mathscr{H}}\_{T},P) and the individual ones Xt,TiX^{i}\_{t,T} satisfy

1. (1)

   Xt,T1,Xt,T2,⋯∈L2​(Ω,ℋT,P)X^{1}\_{t,T},X\_{t,T}^{2},\dots\in L^{2}(\Omega,{\mathscr{H}}\_{T},P) are ℋt,T{\mathscr{H}}\_{t,T}-conditionally independent,
2. (2)

   E​[Xt,Ti|ℋt,T]=E​[Xt,T|ℋt,T],i=1,2,…\ E[X^{i}\_{t,T}|{\mathscr{H}}\_{t,T}]=E[X\_{t,T}|{\mathscr{H}}\_{t,T}],\ i=1,2,\dots, and
3. (3)

   Var⁡(Xt,Ti|ℋt,T)=Var⁡(Xt,T|ℋt,T)<∞,i=1,2,….\operatorname{Var}(X^{i}\_{t,T}|{\mathscr{H}}\_{t,T})=\operatorname{Var}(X\_{t,T}|{\mathscr{H}}\_{t,T})<\infty,\ i=1,2,\dots.

Intuitively, the assumption on *conditional* independence is very general since it includes all available financial information (until the final time TT). This covers in particular the important case of a pandemic: when stock prices fall and mortality increases - which can be modelled through a hidden factor or via an intensity directly depending on the stock market, as for example in Ballotta et al. ([2019](https://arxiv.org/html/2510.06698v1#bib.bib4)).

An *insurance-finance strategy* is now the pair (ψ,ξ)(\psi,\xi) which achieves the (discounted) *insurance-finance value*

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞VI​(ψn)+VF​(ξ).\displaystyle\lim\_{n\to\infty}V^{I}(\psi^{n})+V^{F}(\xi). |  | (6) |

### 2.3. Insurance-finance arbitrage

The *insurance-finance market* is hence given by the triplet (X,p,S)(X,p,S).
An admissible insurance portfolio strategy (ψn)n≥1(\psi^{n})\_{n\geq 1}, and an insurer’s trading strategy ξ\xi form an *insurance-finance arbitrage* (IFA), if

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞VI​(ψn)+VF​(ξ)∈L0+\{0}.\displaystyle\lim\_{n\to\infty}V^{I}(\psi^{n})+V^{F}(\xi)\in L\_{0}^{+}\backslash\{0\}. |  | (7) |

If there is no general IFA on the insurance-finance market, we say no general insurance-finance arbitrage (NIFA0) holds. If there is no bounded IFA, we say NIFA∞ holds.

In the following theorem, contained in Artzner et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib3)),
absence of insurance arbitrage is characterized, however in a slightly simplified version.
For this result we also rely on a measure P∗P^{\*} which is equivalent to PP (and later on take the role of an equivalent martingale measure, i.e. a risk-neutral measure).
We need a similar assumption as Assumption [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.2. The insurance market ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting") for P∗P^{\*}, where we additionally assume that the conditional expectation of Xt,TX\_{t,T} under P∗P^{\*} coincides with those under PP:

###### Assumption 2.2.

Consider P∗∼PP^{\*}\sim P and assume that
for all t∈𝕋t\in\mathbb{T},

1. (1)

   Xt,T1,Xt,T2,⋯∈L2​(Ω,ℋT,P∗)X^{1}\_{t,T},X\_{t,T}^{2},\dots\in L^{2}(\Omega,{\mathscr{H}}\_{T},P^{\*}) are ℋt,T{\mathscr{H}}\_{t,T}-conditionally independent under P∗P^{\*},
2. (2)

   EP∗​[Xt,Ti|ℋt,T]=EP∗​[Xt,T1|ℋt,T],i=2,3,…\ E\_{P^{\*}}[X^{i}\_{t,T}|{\mathscr{H}}\_{t,T}]=E\_{P^{\*}}[X^{1}\_{t,T}|{\mathscr{H}}\_{t,T}],\ i=2,3,\dots, and
3. (3)

   VarP∗⁡(Xt,Ti|ℋt,T)=VarP∗⁡(Xt,T1|ℋt,T)<∞,i=2,3,….\operatorname{Var}\_{P^{\*}}(X^{i}\_{t,T}|{\mathscr{H}}\_{t,T})=\operatorname{Var}\_{P^{\*}}(X^{1}\_{t,T}|{\mathscr{H}}\_{t,T})<\infty,\ i=2,3,\dots.

We recall that ℳe,b​(S,𝔽){\mathscr{M}}\_{e,b}(S,\mathbb{F}) is the set of equivalent martingale measures with bounded density on the financial market given by stock prices SS and filtration 𝔽\mathbb{F}. Then, the following holds.

###### Theorem 2.1.

On the insurance-finance market (X,p,S)(X,p,S) with Assumption [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.2. The insurance market ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting"), the sequence of implications
([i](https://arxiv.org/html/2510.06698v1#S2.I3.i1 "item i ‣ Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting"))⇒\Rightarrow
([ii](https://arxiv.org/html/2510.06698v1#S2.I3.i2 "item ii ‣ Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting"))   holds for the following assertions:

1. (i)

   N​I​F​A0NIFA^{0} holds,
2. (ii)

   There exists P∗∼PP^{\*}\sim P on (Ω,ℋT−1,T)(\Omega,{\mathscr{H}}\_{T-1,T}) so that

   1. (ii.a)

      P∗|ℱT∈ℳe,b​(S,𝔽)\;P^{\*}|\_{{\mathscr{F}}\_{T}}\in{\mathscr{M}}\_{e,b}(S,\mathbb{F})\; and
   2. (ii.b)

      EP∗​[pt−Xt,T|ℱt]≤0\;E\_{P^{\*}}\big[p\_{t}-X\_{t,T}\big|{\mathscr{F}}\_{t}\big]\leq 0 for t=0,…,T−1t=0,\dots,T-1.

Moreover, if ([ii](https://arxiv.org/html/2510.06698v1#S2.I3.i2 "item ii ‣ Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting")) holds and P∗P^{\*} satisfies Assumption [2.2](https://arxiv.org/html/2510.06698v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting"), then

1. (iii)

   N​I​F​A∞NIFA^{\infty} holds.

For us, the most important implication is ([iii](https://arxiv.org/html/2510.06698v1#S2.I4.i3 "item iii ‣ Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting")): if we find such a P∗P^{\*} then there are no insurance-finance arbitrages. This can be achieved as follows: assume that Assumption 2.1 holds and denote by LL the Radon-Nikodym derivative of QQ with respect to P|ℱTP|\_{{\mathscr{F}}\_{T}}, such that d​Q=L​d​PdQ=L\;dP. Then, define P∗P^{\*} on (Ω,ℋT)(\Omega,{\mathscr{H}}\_{T}) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​P∗=L​d​P.\displaystyle dP^{\*}=L\,dP. |  | (8) |

In this case, P∗P^{\*} is the so-called *QP-measure* which we denote by Q⊙P\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP}. By Proposition 4.1 in Artzner et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib3)), this P∗P^{\*} coincides with QQ on ℱT{\mathscr{F}}\_{T}, hence it is *market-consistent*. On the other side, for X∈L1X\in L^{1} or bounded from below,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ⊙P​[X|ℱt]\displaystyle E\_{\operatorname{Q\odot P}}[X\,|\,{\mathscr{F}}\_{t}] | =EQ​[EP​[X|ℱT]|ℱt].\displaystyle=E\_{Q}\big[E\_{P}[X\,|\,{\mathscr{F}}\_{T}]\,|\,{\mathscr{F}}\_{t}\big]. |  | (9) |

Intuitively, this rule describes how to evaluate insurance contracts in an IFA-free way: by projection onto the publicly available information (under PP) and afterwards by applying the risk-neutral pricing rule (under some QQ calibrated to available market data). For further details we refer to Artzner et al. ([2024](https://arxiv.org/html/2510.06698v1#bib.bib3)).

In the following, we will show how to use this result on highly flexible affine models in insurance-finance markets.

## 3. IFA-free valuation of insurance products with guarantees

In this setting, we provide a general framework for insurance products with guarantees, where we include typical contract specifications of variable annuities. The setting is modular and general, such that also other types of insurance products can be valued using this approach.

A *variable annuity* (VA) is an insurance contract which gives the holder a variety of benefits in exchange for a sequence of payments. The contract has a maturity T>0T>0.
We start by explaining typical contract specifications of a variable annuity.

While up to now we considered already discounted quantities, for the contract specifications we prefer to state the quantities in undiscounted terms, and denote by

|  |  |  |
| --- | --- | --- |
|  | β​(t,T) \beta(t,T) |  |

the discounting factor at time tt of the secure payment of 1 unit of money at time TT (which is often captured through the bank account S0S^{0} with β​(t,T)=St0/ST0\beta(t,T)=\nicefrac{{S^{0}\_{t}}}{{S^{0}\_{T}}}). Whenever starting from time 0, we simplify the notation by setting β​(T):=β​(0,T)\beta(T):=\beta(0,T).

### 3.1. Contract details

The payments π1,…,πn\pi\_{1},\dots,\pi\_{n} are due at a discrete time grid T0=0<T1<⋯<Tn<Tn+1=TT\_{0}=0<T\_{1}<\cdots<T\_{n}<T\_{n+1}=T, where the annuity requires the payment πi\pi\_{i} at time TiT\_{i}. These investments are immediately invested in a fund and we denote the value process of the fund by Fπ=(Ftπ)F^{\pi}=(F^{\pi}\_{t}). For simplicity, we assume that β\beta is deterministic, since in most practical applications we have in mind the impact of the other quantities (mortality, stock price, growth rate) will be significantly stronger.

###### Remark 3.1 (On the underlying fund).

The main observation due in this respect is that the premium is not paid at a single time up-front, but by a series of payments. This means, if investments are in the stock S1=SS^{1}=S, say, that the value of the underlying fund at time tt is, given no surrender or death,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ftπ=(∑i=1n𝟙{Ti≤t}​πiSTi)⋅St.\displaystyle F\_{t}^{\pi}=\Big(\sum\_{i=1}^{n}{\mathds{1}}\_{\{T\_{i}\leq t\}}\frac{\pi\_{i}}{S\_{T\_{i}}}\Big)\cdot S\_{t}. |  | (10) |

Consequences of these types of payments where already studied in Bernard et al. ([2017](https://arxiv.org/html/2510.06698v1#bib.bib6)) and in Hainaut and Devineau ([2025](https://arxiv.org/html/2510.06698v1#bib.bib18)), but not in a general affine framework.

In the specification which we consider here, the VA offers three features:

1. (i)

   a guaranteed minimum accumulation benefit (GMAB),
2. (ii)

   a surrender benefit (SB), and
3. (iii)

   a death benefit (DB).

The precise description of these benefits can be done as follows:
first, the GMAB equals the best of two investment choices, either the value of the underlying fund or a guaranteed amount.

More specific, let us consider the guarantee of a fixed interest rate δ\delta over the lifetime of the contract: if we upcount all payments to the maturity TT, we obtain that the guarantee sums up to

|  |  |  |
| --- | --- | --- |
|  | KTπ=∑i=1neδ​(T−Ti)​πi.K^{\pi}\_{T}=\sum\_{i=1}^{n}e^{\delta(T-T\_{i})}\pi\_{i}. |  |

Analogously, the value of the accumulated payments done until time tt computes to Ktπ=∑i=1n𝟙{Ti≤t}​eδ​(t−Ti)​πiK^{\pi}\_{t}=\sum\_{i=1}^{n}{\mathds{1}}\_{\{T\_{i}\leq t\}}e^{\delta(t-T\_{i})}\pi\_{i}.

At maturity the policyholder receives either the value of the fund or the value of the payments, invested with the guaranteed interest rate δ\delta, which equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡(FTπ,KTπ).\displaystyle\max(F\_{T}^{\pi},K\_{T}^{\pi}). |  | (11) |

This, however, can only be claimed if the policyholder is still alive at time TT *and* she did not surrender before.

Second, in case of early *surrender*
her right of refund is restricted to the current fund account value reduced by a *compulsory surrender penalty*.
For simplicity, we assume surrender is possible on the same grid as the payments are done. In case of surrender at time TiT\_{i}, the surrender benefit is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB​(Ti):=FTiπ⋅pSB​(Ti),\displaystyle{\rm SB}(T\_{i}):=F^{\pi}\_{T\_{i}}\cdot p\_{\text{SB}}(T\_{i}), |  | (12) |

where the penalty pSB:[0,T]→(0,1]p\_{\text{SB}}:[0,T]\to(0,1] is a deterministic function of time. Choosing pp small at early times and equal or close to one at later times allows to overcome the problem that initial expenses of the contract may not be covered in the case of early surrender.

Third, in case of death before TT, the *death benefit* provides a payoff, but only if the early surrender option has not been exercised yet. It includes the same guarantee (for simplicity) as in the GMAB, but this time paid out at the next TiT\_{i} after death. Therefore, the payoff of the death benefit in case of death at time tt such that Ti−1<t≤TiT\_{i-1}<t\leq T\_{i} is settled at time TiT\_{i} and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | DB​(Ti):=max⁡(FTiπ,KTiπ).\displaystyle{\rm DB}(T\_{i}):=\max(F\_{T\_{i}}^{\pi},K\_{T\_{i}}^{\pi}). |  | (13) |

### 3.2. Mortality and surrender

Regarding mortality and surrender we assume that the given insurance clients are a homogeneous cohort in the sense that the probabilistic description of the individual mortality time τm,i\tau^{m,i} can be captured by the probabilistic modelling of the mortality τm\tau^{m} of a typical individual, which we detail in the following. This is done via an intensity-based approach and hence depends on the individual survival τm,i\tau^{m,i}, but otherwise on a common intensity. Furthermore, as typical in life-insurance, we introduce the current age xx as additional covariable.

In this regard, assume that the remaining lifetime τm​(x)\tau^{m}(x) of a insured person aged xx years is a ℍ\mathbb{H}-stopping time with intensity λm​(x)\lambda^{m}(x). i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τm​(x)>T​|ℋt,τm​(x)>​t)=𝟙{τm​(x)>t}​E​[e−∫tTλsm​(x)​𝑑s|ℋt].\displaystyle P(\tau^{m}(x)>T\,|\,{\mathscr{H}}\_{t},\,\tau^{m}(x)>t)={\mathds{1}}\_{\{\tau^{m}(x)>t\}}E\Big[e^{-\int\_{t}^{T}\lambda^{m}\_{s}(x)ds}|{\mathscr{H}}\_{t}\Big]. |  | (14) |

###### Remark 3.2 (Intensity-based setting).

In particular, for each individual ii aged xx years we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τm,i​(x)>T​|ℋt,τm​(x)>​t)=𝟙{τm,ix)>t}​E​[e−∫tTλsm​(x)​𝑑s|ℋt].\displaystyle P(\tau^{m,i}(x)>T\,|\,{\mathscr{H}}\_{t}\,,\tau^{m}(x)>t)={\mathds{1}}\_{\{\tau^{m,i}x)>t\}}E\Big[e^{-\int\_{t}^{T}\lambda^{m}\_{s}(x)ds}|{\mathscr{H}}\_{t}\Big]. |  | (15) |

This assumption precisely reflects what we call a *homogeneous* cohort of insured persons: while individual surrender or mortality occurs of course individually, the estimated probability distributions are the same for all individuals in the considered cohort. ⋄\diamond

In case of early surrender at time TiT\_{i}, the policyholder can reinvest the surrender benefit SB​(Ti){\rm SB}(T\_{i}) for the remaining time until the maturity TT leading to the benefit

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB​(Ti)​β​(Ti,T)−1\displaystyle{\rm SB}(T\_{i})\beta(T\_{i},T)^{-1} |  | (16) |

at maturity TT.

By τs\tau^{s} we denote the time when the policy holder decides to exercise the surrender option.
Similar to mortality, we assume that τs\tau^{s} satisfied

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τs>T​|ℋt,τs>​t)=𝟙{τs>t}​E​[e−∫tTλus​𝑑s|ℋt].\displaystyle P(\tau^{s}>T\,|\,{\mathscr{H}}\_{t},\,\tau^{s}>t)={\mathds{1}}\_{\{\tau^{s}>t\}}E\Big[e^{-\int\_{t}^{T}\lambda^{s}\_{u}ds}|{\mathscr{H}}\_{t}\Big]. |  | (17) |

For further literature in this regard, and a detailed treatment of random times with intensities and associated enlargements of filtrations, see Aksamit and Jeanblanc ([2017](https://arxiv.org/html/2510.06698v1#bib.bib2)). The approach chosen here falls in the class of so-called doubly-stochastic modeling approaches for the random times and the related immersion hypothesis holds.
Note, that even if the policy holder decides in continuous time, the exercise of the surrender option only takes place on a discrete grid: more precisely, if Ti−1<τs≤TiT\_{i-1}<\tau^{s}\leq T\_{i} then surrender takes place at TiT\_{i} leading to the payoff specified in Equation([16](https://arxiv.org/html/2510.06698v1#S3.E16 "In 3.2. Mortality and surrender ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")).

### 3.3. The valuation rule

The value of the variable annuity decomposes in GMAB, SB and DB (all of course depending on the maturity TT) in a linear way which allows to apply (for example) the QP-rule directly for IFA-free pricing. We denote the expectation under P∗P^{\*} by E∗=EP∗E^{\*}=E\_{P^{\*}}. We call the premium of an insurance-finance contract *fair* if it does not introduce any IFA. In this sense, prices obtained by the QP-rule or by taking expectations under a measure P∗P^{\*} as in Theorem [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting") induce fair premia.

###### Proposition 3.1.

Assume that P∗P^{\*} is as in Theorem [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting"). Then, an IFA-free valuation of the variable annuity is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VAt=Πt+GMABt+SBt+DBt,0≤t≤T,\displaystyle{\rm VA}\_{t}={\Pi}\_{t}+{\rm GMAB}\_{t}+{\rm SB}\_{t}+{\rm DB}\_{t},\qquad 0\leq t\leq T, |  | (18) |

where

1. (i) 

   the *discounted value of the future (and the present) payments* is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Πt=−∑i=0nβ​(t,Ti)​πi​ 1{Ti≥t}​E∗​[𝟙{τm>Ti,τs>Ti}|ℱt];\displaystyle{\Pi}\_{t}=-\sum\_{i=0}^{n}\beta(t,T\_{i})\pi\_{i}\,{\mathds{1}}\_{\{T\_{i}\geq t\}}E^{\*}\Big[{\mathds{1}}\_{\{\tau^{m}>T\_{i},\,\tau^{s}>T\_{i}\}}\,\big|\,{\mathscr{F}}\_{t}\Big]; |  | (19) |
2. (ii) 

   the value of the *guaranteed minimum accumulation benefit* is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | GMABt=β​(t,T)​E∗​[𝟙{τm​(x)>T}​𝟙{τs>T}⋅max⁡(FTπ,KTπ)|ℱt];\displaystyle{\rm GMAB}\_{t}=\beta(t,T)\,E^{\*}\Big[{\mathds{1}}\_{\{\tau^{m}(x)>T\}}{\mathds{1}}\_{\{\tau^{s}>T\}}\cdot\max(F\_{T}^{\pi},K\_{T}^{\pi})\,\big|\,{\mathscr{F}}\_{t}\Big]; |  | (20) |
3. (iii) 

   the value of the *death benefit*

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | DBt=∑k=1n+1β​(t,Tk)​E∗​[𝟙{τm​(x)<τs}​𝟙{Tk−1<τm​(x)≤Tk}​max⁡(FTkπ,KTkπ)|ℱt];\displaystyle{\rm DB}\_{t}=\sum\_{k=1}^{n+1}\beta(t,T\_{k})\,E^{\*}\bigg[{\mathds{1}}\_{\{\tau^{m}(x)<\tau^{s}\}}{\mathds{1}}\_{\{T\_{k-1}<\tau^{m}(x)\leq T\_{k}\}}\max(F\_{T\_{k}}^{\pi},K\_{T\_{k}}^{\pi})\big|{\mathscr{F}}\_{t}\bigg]; |  | (21) |
4. (iv) 

   the value of the *surrender benefit* is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | SBt=∑k=1nβ​(t,Tk)​E∗​[𝟙{Tk−1<τs≤Tk}​𝟙{τs<τm​(x)}​FTkπ​p​(Tk)|ℱt].\displaystyle{\rm SB}\_{t}=\sum\_{k=1}^{n}\beta(t,T\_{k})\,E^{\*}\Big[{\mathds{1}}\_{\{T\_{k-1}<\tau^{s}\leq T\_{k}\}}{\mathds{1}}\_{\{\tau^{s}<\tau^{m}(x)\}}F\_{T\_{k}}^{\pi}p(T\_{k})\,\big|\,{\mathscr{F}}\_{t}\Big]. |  | (22) |

###### Proof.

First, recall that the (non-random) payment πi\pi\_{i} is done at time TiT\_{i}, i=0,…,ni=0,\dots,n. Since all quantities are deterministic, we sum the discounted payments after or at tt, take conditional P∗P^{\*}-expectations and ([19](https://arxiv.org/html/2510.06698v1#S3.E19 "In item i ‣ Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")) follows.

Second, recall that the GMAB provides a payoff only if the policyholder still alive until TT (i.e., {τm​(x)>T}\{\tau^{m}(x)>T\}) and if there was no surrender until this time (i.e., {τs>T}\{\tau^{s}>T\}). The payoff max⁡(FTkπ,KTkπ)\max(F\_{T\_{k}}^{\pi},K\_{T\_{k}}^{\pi}), see Equation ([11](https://arxiv.org/html/2510.06698v1#S3.E11 "In 3.1. Contract details ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")), is ℱT{\mathscr{F}}\_{T}-measurable and paid at maturity TT. Taking conditional P∗P^{\*}-expectations leads to the expression in ([20](https://arxiv.org/html/2510.06698v1#S3.E20 "In item ii ‣ Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")).

Third, the death benefit provides a payoff only if the surrender option was not exercised before. Hence, if Tk−1<τm​(x)≤TkT\_{k-1}<\tau^{m}(x)\leq T\_{k}, the contract pays the amount max⁡(FTkπ,KTkπ)\max(F\_{T\_{k}}^{\pi},K\_{T\_{k}}^{\pi}) at TkT\_{k}; conditional on no previous surrender of course. Summing again over all possible time T1,…,Tn+1=TT\_{1},\dots,T\_{n+1}=T and taking P∗P^{\*}-expectations, Equation ([21](https://arxiv.org/html/2510.06698v1#S3.E21 "In item iii ‣ Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")) follows.

Fourth, we consider the surrender option. This option can only be exercised if the insurer is still alive (i.e., {τs<τm​(x)}\{\tau^{s}<\tau^{m}(x)\}).
According to Equation ([12](https://arxiv.org/html/2510.06698v1#S3.E12 "In 3.1. Contract details ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")), the payoff at TkT\_{k} is FTkπ​p​(Tk)F^{\pi}\_{T\_{k}}p(T\_{k}) if Tk−1<τs≤TkT\_{k-1}<\tau^{s}\leq T\_{k}, i.e. if surrender is exercised between Tk−1T\_{k-1} and TkT\_{k}. Summing the relevant dates, discounting and taking P∗P^{\*}-expectations lead to Equation ([22](https://arxiv.org/html/2510.06698v1#S3.E22 "In item iv ‣ Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")).

These four components add up to the price of the variable annuity. Hence the value in ([18](https://arxiv.org/html/2510.06698v1#S3.E18 "In Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")) is an IFA-free valuation by Theorem [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting").
∎

Valuing the fund FπF^{\pi} itself is possible by risk-neutral pricing when mortality and surrender are independent of SS *and* sufficiently tractable. Otherwise, as we will show in the later sections, this task can become quite involved.

In the following, it therefore remains to propose a tractable framework where the associated components of Equation ([18](https://arxiv.org/html/2510.06698v1#S3.E18 "In Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")) can be computed efficiently. We proceed in two steps - first, we will introduce appropriate enlargement of filtration techniques and second, we will introduce an affine framework which in our eyes is flexible enough to capture all stylised facts in the market and on the other side allows tractable pricing rules.

## 4. Progressive filtration enlargements

To obtain a tractable pricing rule, we introduce an additional structure on the insurance filtration ℍ\mathbb{H} by utilizing the theory of progressive enlargements.
For simplicity, we concentrate on the case where ℍ\mathbb{H} is given by the smallest possibly enlargement of the publicly available information, given by the filtration 𝔽\mathbb{F}, in our context: this is the enlargement with mortality and surrender times only111The filtration ℍ\mathbb{H} can additionally be enlarged by independent information without changing the approach. For example this could be mortality of additional clients, if those data does not contain additional information, which is the case when the mortality intensity is 𝔽\mathbb{F}-measurable. The study of more complicated settings with incomplete information remains a topic for future research..

First, we concentrate on a single random time τ=τm\tau=\tau^{m}, which models the random life time of the insured client. We consider multiple times in Section [4.1](https://arxiv.org/html/2510.06698v1#S4.SS1 "4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting").
The main assumption we make is to assume that {τ>t}\{\tau>t\}, t≥0t\geq 0, are atoms in the enlarged filtration ℍ\mathbb{H}: assume that for all t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋt⋂{τ>t}=ℱt⋂{τ>t}.\displaystyle{\mathscr{H}}\_{t}\mathbin{\scalebox{0.9}{$\bigcap$}}\{\tau>t\}={\mathscr{F}}\_{t}\mathbin{\scalebox{0.9}{$\bigcap$}}\{\tau>t\}. |  | (23) |

This means that for each H∈ℋtH\in{\mathscr{H}}\_{t} there exists an F∈ℱtF\in{\mathscr{F}}\_{t}, such that H∩{τ>t}=F∩{τ>t}H\cap\{\tau>t\}=F\cap\{\tau>t\} and vice versa.
A classical and well-known example where ([23](https://arxiv.org/html/2510.06698v1#S4.E23 "In 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) holds is the progressive enlargement of 𝔽\mathbb{F} with the random time τ\tau.

###### Remark 4.1 (Progressive enlargement).

Assume that for all t≥0t\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋt:=σ({F⋂{τ≤s}:F∈ℱt,s≤t})=:ℱt∨{τ∧t},\displaystyle{\mathscr{H}}\_{t}:=\sigma\big(\{F\mathbin{\scalebox{0.9}{$\bigcap$}}\{\tau\leq s\}:F\in{\mathscr{F}}\_{t},s\leq t\}\big)=:{\mathscr{F}}\_{t}\vee\{\tau\wedge t\}, |  | (24) |

then ℍ\mathbb{H} is called the *progressive enlargement* of 𝔽\mathbb{F} with τ\tau.
Then ([23](https://arxiv.org/html/2510.06698v1#S4.E23 "In 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) holds: indeed, this follows from

|  |  |  |
| --- | --- | --- |
|  | F⋂{τ>s}⋂{τ>t}=F⋂{τ>t},F\mathbin{\scalebox{0.9}{$\bigcap$}}\{\tau>s\}\mathbin{\scalebox{0.9}{$\bigcap$}}\{\tau>t\}=F\mathbin{\scalebox{0.9}{$\bigcap$}}\{\tau>t\}, |  |

for 0≤s≤t≤T0\leq s\leq t\leq T and F∈ℱt.F\in{\mathscr{F}}\_{t}.
For a detailed study and many references to related literature see Aksamit and Jeanblanc ([2017](https://arxiv.org/html/2510.06698v1#bib.bib2)). Typically, we will be interested in a filtration which contains more information, like the employment status, health status, surrender behaviour, etc. ♢\diamondsuit

For a pricing rule, fix tt and consider a measure P∗P^{\*} as in Theorem [2.1](https://arxiv.org/html/2510.06698v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting"), for example P∗=Q⊙PP^{\*}=\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP} as in the QP-rule. Then, fair insurance pricing works as follows: the insurance premium ptp\_{t} is computed via taking expectations under P∗P^{\*} with respect to ℱt{\mathscr{F}}\_{t}.
In this regard, denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=P∗​(τ>t|ℱt),t∈𝕋,\displaystyle G\_{t}=P^{\*}(\tau>t\,|\,{\mathscr{F}}\_{t}),\qquad t\in\mathbb{T}, |  | (25) |

the *Azéma supermartingale* under P∗P^{\*}. The Azéma supermartingale decodes the survival probability of τ\tau in the smaller filtration 𝔽\mathbb{F}.

###### Proposition 4.1.

Assume 𝔽⊂ℍ\mathbb{F}\subset\mathbb{H}, τ\tau being a ℍ\mathbb{H}-stopping time, and that ([23](https://arxiv.org/html/2510.06698v1#S4.E23 "In 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) holds.
Then, for any 𝔽\mathbb{F}-adapted process AA bounded from below,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E∗​[Aτ|ℋt]\displaystyle E^{\*}[A\_{\tau}\,|\,{\mathscr{H}}\_{t}] | =𝟙{τ≤t}​Aτ+𝟙{τ>t,Gt>0}​Gt−1​E∗​[Aτ​𝟙{τ>t}|ℱt]\displaystyle={\mathds{1}}\_{\{\tau\leq t\}}A\_{\tau}+{\mathds{1}}\_{\{\tau>t,\,G\_{t}>0\}}G\_{t}^{-1}E^{\*}\Big[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}\,|\,{\mathscr{F}}\_{t}\Big] |  | (26) |

holds for all t∈𝕋t\in\mathbb{T}.

###### Proof.

Consider Aτ=Aτ​𝟙{τ≤t}+Aτ​𝟙{τ>t}A\_{\tau}=A\_{\tau}{\mathds{1}}\_{\{\tau\leq t\}}+A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}. Since
Aτ​𝟙{τ≤t}A\_{\tau}{\mathds{1}}\_{\{\tau\leq t\}} is ℋt{\mathscr{H}}\_{t}-measurable, we obtain E∗​[Aτ​𝟙{τ≤t}|ℋt]=Aτ​𝟙{τ≤t}E^{\*}[A\_{\tau}{\mathds{1}}\_{\{\tau\leq t\}}|{\mathscr{H}}\_{t}]=A\_{\tau}{\mathds{1}}\_{\{\tau\leq t\}}, the first addend of ([26](https://arxiv.org/html/2510.06698v1#S4.E26 "In Proposition 4.1. ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")).

Next, we consider Aτ​𝟙{τ>t}A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}. Note that E∗​[Aτ​𝟙{τ>t}|ℱt]E^{\*}[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{t}] vanishes on the set {τ>t,Gt=0}\{\tau>t,\,G\_{t}=0\}, and so does the second addend in ([26](https://arxiv.org/html/2510.06698v1#S4.E26 "In Proposition 4.1. ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")). So, we may assume Gt>0G\_{t}>0 everywhere. Now, ([23](https://arxiv.org/html/2510.06698v1#S4.E23 "In 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) implies that for any t≥0t\geq 0 and any ℋt{\mathscr{H}}\_{t}-measurable random variable A~t\tilde{A}\_{t} we find a ℱt{\mathscr{F}}\_{t}-measurable random variable YtY\_{t}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | A~t​𝟙{τ>t}=Yt​𝟙{τ>t}\displaystyle\tilde{A}\_{t}{\mathds{1}}\_{\{\tau>t\}}=Y\_{t}{\mathds{1}}\_{\{\tau>t\}} |  | (27) |

by an application of the monotone class theorem. Using E∗​[Aτ​𝟙{τ>t}|ℋt]E^{\*}[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{H}}\_{t}] for A~t\tilde{A}\_{t} in this equation and taking conditional expectation with respect to ℱt{\mathscr{F}}\_{t}, we obtain that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gt−1​E∗​[E∗​[Aτ|ℋt]​𝟙{τ>t}|ℱt]\displaystyle G\_{t}^{-1}E^{\*}\Big[E^{\*}[A\_{\tau}|{\mathscr{H}}\_{t}]{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{t}\Big] | =Gt−1​E∗​[Yt​𝟙{τ>t}|ℱt]=Yt.\displaystyle=G\_{t}^{-1}E^{\*}\Big[Y\_{t}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{t}\Big]=Y\_{t}. |  | (28) |

On the other hand,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E∗​[E∗​[Aτ|ℋt]​𝟙{τ>t}|ℱt]\displaystyle E^{\*}\Big[E^{\*}[A\_{\tau}|{\mathscr{H}}\_{t}]{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{t}\Big] | =E∗​[Aτ​𝟙{τ>t}|ℱt]\displaystyle=E^{\*}\Big[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{t}\Big] |  |

and the proof of the proposition is finished.
∎

We add a simple corollary for the QP-rule which follows directly by Equation ([9](https://arxiv.org/html/2510.06698v1#S2.E9 "In 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting")).

###### Corollary 4.2.

Assume that P∗=Q⊙PP^{\*}=\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP}. Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E∗​[Aτ​𝟙{τ>t}|ℱt]=EQ​[EP​[Aτ​𝟙{τ>t}|ℱT]|ℱt].\displaystyle E^{\*}\Big[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}\,|\,{\mathscr{F}}\_{t}\Big]=E\_{Q}\Big[E\_{P}[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{T}]\,|\,{\mathscr{F}}\_{t}\Big]. |  | (29) |

###### Example 4.1 (Doubly stochastic stopping times).

The most important example regarding modeling with affine processes will be a doubly stochastic setting, which we introduce now.
Consider an 𝔽\mathbb{F}-adapted, increasing process Λ=(Λt)t∈𝕋\Lambda=(\Lambda\_{t})\_{t\in\mathbb{T}} with Λ0=0\Lambda\_{0}=0 together with an independent exponential random variable EE and let222Such a construction is called *doubly stochastic*. We refer to Bielecki and Rutkowski ([2002](https://arxiv.org/html/2510.06698v1#bib.bib7)); Brémaud ([1981](https://arxiv.org/html/2510.06698v1#bib.bib8)); Gehmlich and Schmidt ([2018](https://arxiv.org/html/2510.06698v1#bib.bib17)) for details and references. If Λt=∫0tλs​𝑑s\Lambda\_{t}=\int\_{0}^{t}\lambda\_{s}ds, then λ\lambda is called the *intensity* of τ\tau. If the intensity is deterministic, it is called *hazard rate*.

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ=inf{t∈𝕋:Λt≥E},\displaystyle\tau=\inf\{t\in\mathbb{T}:\Lambda\_{t}\geq E\}, |  | (30) |

with the convention that inf∅=T+1\inf\emptyset=T+1.
Then, τ\tau is not an 𝔽\mathbb{F}-stopping time, but it is a stopping time in the progressive enlargement ℍ\mathbb{H}. In particular,

|  |  |  |
| --- | --- | --- |
|  | Gt=P∗​(τ>t|ℱt)=P∗​(Λt​<E|​ℱt)=e−ΛtG\_{t}=P^{\*}(\tau>t|{\mathscr{F}}\_{t})=P^{\*}(\Lambda\_{t}<E|{\mathscr{F}}\_{t})=e^{-\Lambda\_{t}} |  |

for any t∈𝕋t\in\mathbb{T}.
Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E∗​[Aτ​𝟙{τ>t}|ℋt]\displaystyle E^{\*}[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{H}}\_{t}] | =𝟙{τ>t}​Gt−1​∑s=t+1TE∗​[As​P∗​(τ=s|ℱs)|ℱt]\displaystyle={\mathds{1}}\_{\{\tau>t\}}G\_{t}^{-1}\sum\_{s=t+1}^{T}E^{\*}[A\_{s}P^{\*}(\tau=s\,|\,{\mathscr{F}}\_{s})|{\mathscr{F}}\_{t}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝟙{τ>t}​eΛt​∑s=t+1TE∗​[As​(e−Λs−1−e−Λs)|ℱt].\displaystyle={\mathds{1}}\_{\{\tau>t\}}e^{\Lambda\_{t}}\sum\_{s=t+1}^{T}E^{\*}\big[A\_{s}\big(e^{-\Lambda\_{s-1}}-e^{-\Lambda\_{s}}\big)|{\mathscr{F}}\_{t}\big]. |  | (31) |

Additionally, if P∗=Q⊙PP^{\*}=\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP}, then

|  |  |  |
| --- | --- | --- |
|  | E∗​[As​(e−Λs−1−e−Λs)|ℱt]=EQ​[As​(e−Λs−1−e−Λs)|ℱt],E^{\*}\big[A\_{s}\big(e^{-\Lambda\_{s-1}}-e^{-\Lambda\_{s}}\big)|{\mathscr{F}}\_{t}\big]=E\_{Q}[A\_{s}\big(e^{-\Lambda\_{s-1}}-e^{-\Lambda\_{s}}\big)|{\mathscr{F}}\_{t}\big], |  |

such that the evaluation of the payment stream AA (typically depending on financial quantities like interest rates and stock markets) can be done in a market-consistent way.
These formulae are key results for the valuation of a large number of hybrid products.
♢\diamondsuit

An additional difficulty arises when AA is not 𝔽\mathbb{F}-measurable. Here one is able to exploit the structure of the progressive enlargement in the case where τ\tau is honest. For example, Corollary 5.12 in Aksamit and Jeanblanc ([2017](https://arxiv.org/html/2510.06698v1#bib.bib2)) allows to decompose XX in several 𝔽\mathbb{F}-adapted components on random intervals depending solely on τ\tau.

###### Proposition 4.3.

Consider P∗=Q⊙PP^{\*}=\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP} and
assume 𝔽⊂ℍ\mathbb{F}\subset\mathbb{H}, τ\tau being a ℍ\mathbb{H}-stopping time, and that ([23](https://arxiv.org/html/2510.06698v1#S4.E23 "In 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) holds.
Then, for any ℍ\mathbb{H}-adapted process AA and any ℱT{\mathscr{F}}\_{T}-measurable random variable FTF\_{T}, both bounded from below, it holds that for all t∈𝕋t\in\mathbb{T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[FT​Aτ|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[F\_{T}A\_{\tau}|{\mathscr{H}}\_{t}] | =𝟙{τ≤t}​Aτ​EQ⊙P​[FT|ℋt]\displaystyle={\mathds{1}}\_{\{\tau\leq t\}}A\_{\tau}E\_{\operatorname{Q\odot P}}[F\_{T}|{\mathscr{H}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟙{τ>t,Gt>0}​Gt−1​EQ​[FT​EP​[Aτ​𝟙{τ>t}|ℱT]|ℱt].\displaystyle+{\mathds{1}}\_{\{\tau>t,\,G\_{t}>0\}}\;G\_{t}^{-1}E\_{Q}\Big[F\_{T}E\_{P}[A\_{\tau}{\mathds{1}}\_{\{\tau>t\}}|{\mathscr{F}}\_{T}]|{\mathscr{F}}\_{t}\Big]. |  |

The proof follows as for Proposition [4.1](https://arxiv.org/html/2510.06698v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting").

### 4.1. Multiple stopping times

For the insurance company it is of course important to consider more than one stopping time, and to allow for dependence between these stopping times. We generalise the previous framework by considering a countable number of atoms and provide the associated generalisations of the previously obtained results.

We start by providing the key result for multiple stopping times. To this end,
consider for each t∈𝕋t\in\mathbb{T} ℋt{\mathscr{H}}\_{t}-measurable sets (Pt1,Pt2,…,Ptn)(P\_{t}^{1},P\_{t}^{2},\dots,P\_{t}^{n}) such that Pti∩Ptj=∅P\_{t}^{i}\cap P\_{t}^{j}=\emptyset for i≠ji\neq j.
Assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋt⋂Pti=ℱt⋂Pti,1≤i≤n,t∈𝕋,\displaystyle{\mathscr{H}}\_{t}\mathbin{\scalebox{0.9}{$\bigcap$}}P\_{t}^{i}={\mathscr{F}}\_{t}\mathbin{\scalebox{0.9}{$\bigcap$}}P\_{t}^{i},\qquad 1\leq i\leq n,\ t\in\mathbb{T}, |  | (32) |

and denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gti:=P∗​(Pti|ℱt),t∈𝕋,\displaystyle G\_{t}^{i}:=P^{\*}(P\_{t}^{i}\,|\,{\mathscr{F}}\_{t}),\quad t\in\mathbb{T}, |  | (33) |

the respective generalization of the Azéma supermartingale. Note that without additional assumptions GiG^{i} does not need to be a supermartingale. Nevertheless, we have the following generalization of Proposition [4.1](https://arxiv.org/html/2510.06698v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting") directly formulated in terms of Q⊙P\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP}. The respective version with general P∗P^{\*} follows easily. Set Ωt=∑i=1nPti\Omega\_{t}=\sum\_{i=1}^{n}P\_{t}^{i}.

###### Proposition 4.4.

Assume 𝔽⊆ℍ\mathbb{F}\subseteq\mathbb{H}, and that ([32](https://arxiv.org/html/2510.06698v1#S4.E32 "In 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) and ([33](https://arxiv.org/html/2510.06698v1#S4.E33 "In 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) hold.
Then, for any ℋT{\mathscr{H}}\_{T}-measurable random variable AA bounded from below,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝟙Ωt​EQ⊙P​[A|ℋt]\displaystyle{\mathds{1}}\_{\Omega\_{t}}E\_{\operatorname{Q\odot P}}[A\,|\,{\mathscr{H}}\_{t}] | =∑i=1n𝟙Pti∩{Gti>0}​(Gti)−1​EQ​[EP​[A​ 1Pti|ℱT]|ℱt]\displaystyle=\sum\_{i=1}^{n}{\mathds{1}}\_{P\_{t}^{i}\cap\{G\_{t}^{i}>0\}}(G\_{t}^{i})^{-1}E\_{Q}\Big[E\_{P}[A\,{\mathds{1}}\_{P\_{t}^{i}}|\,{\mathscr{F}}\_{T}]|{\mathscr{F}}\_{t}\Big] |  | (34) |

holds for all t∈𝕋t\in\mathbb{T}.

###### Proof.

First, we decompose

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟙Ωt​EQ⊙P​[A|ℋt]=∑i=1n𝟙Pti​EQ⊙P​[A​ 1Pti|ℋt].\displaystyle{\mathds{1}}\_{\Omega\_{t}}E\_{\operatorname{Q\odot P}}[A|{\mathscr{H}}\_{t}]=\sum\_{i=1}^{n}{\mathds{1}}\_{P\_{t}^{i}}E\_{\operatorname{Q\odot P}}[A\,{\mathds{1}}\_{P\_{t}^{i}}|{\mathscr{H}}\_{t}]. |  | (35) |

For the following, we fix ii.
From ([32](https://arxiv.org/html/2510.06698v1#S4.E32 "In 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")), a monotone class arguments gives the following: for a ℋt{\mathscr{H}}\_{t}-measurable random variable XtX\_{t} we can find a ℱt{\mathscr{F}}\_{t}-measurable random variable Y~t\tilde{Y}\_{t}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt​𝟙Pti=Y~t​𝟙Pti.\displaystyle X\_{t}{\mathds{1}}\_{P\_{t}^{i}}=\tilde{Y}\_{t}{\mathds{1}}\_{P\_{t}^{i}}. |  | (36) |

Hence, there exists an ℱt{\mathscr{F}}\_{t}-measurable random variable YtY\_{t} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[A|ℋt]​ 1Pti=Yt​𝟙Pti.\displaystyle E\_{\operatorname{Q\odot P}}[A|{\mathscr{H}}\_{t}]\,{\mathds{1}}\_{P\_{t}^{i}}=Y\_{t}{\mathds{1}}\_{P\_{t}^{i}}. |  | (37) |

Taking conditional expectations with respect to ℱt{\mathscr{F}}\_{t} and multiplying with 𝟙Pti{\mathds{1}}\_{P\_{t}^{i}} yields that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟙Pti​EQ⊙P​[EQ⊙P​[A​ 1Pti|ℋt]|ℱt]\displaystyle{\mathds{1}}\_{P\_{t}^{i}}E\_{\operatorname{Q\odot P}}\Big[E\_{\operatorname{Q\odot P}}[A\,{\mathds{1}}\_{P\_{t}^{i}}|{\mathscr{H}}\_{t}]|{\mathscr{F}}\_{t}\Big] | =Yt​Gti​ 1Pti.\displaystyle=Y\_{t}G\_{t}^{i}\,{\mathds{1}}\_{P\_{t}^{i}}. |  |

The left hand side equals 𝟙Pti​EQ⊙P​[A​ 1Pti|ℱt]{\mathds{1}}\_{P\_{t}^{i}}E\_{\operatorname{Q\odot P}}[A\,{\mathds{1}}\_{P\_{t}^{i}}|{\mathscr{F}}\_{t}], which consequently vanishes when Gti=0G\_{t}^{i}=0. Inserting ([37](https://arxiv.org/html/2510.06698v1#S4.E37 "In 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟙Pti∩{Gti>0}​(Gti)−1​EQ⊙P​[A​ 1Pti|ℱt]\displaystyle{\mathds{1}}\_{P\_{t}^{i}\cap\{G\_{t}^{i}>0\}}(G\_{t}^{i})^{-1}E\_{\operatorname{Q\odot P}}\big[A\,{\mathds{1}}\_{P\_{t}^{i}}|{\mathscr{F}}\_{t}\big] | =EQ⊙P​[A​ 1Pti|ℋt]​𝟙Pti.\displaystyle=E\_{\operatorname{Q\odot P}}\big[A\,{\mathds{1}}\_{P\_{t}^{i}}|{\mathscr{H}}\_{t}\big]{\mathds{1}}\_{P\_{t}^{i}}. |  |

The claim now follows by combining this with ([9](https://arxiv.org/html/2510.06698v1#S2.E9 "In 2.3. Insurance-finance arbitrage ‣ 2. Insurance-finance markets and arbitrage-free valuation ‣ Insurance products with guarantees in an affine setting")) and ([35](https://arxiv.org/html/2510.06698v1#S4.E35 "In 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")).
∎

### 4.2. Two stopping times

The most relevant case in this paper is the case with two stopping times,
mortality τm\tau^{m} and surrender τs\tau^{s}.
In many papers it is assumed that they are independent or conditionally independent. This can be a serious restriction for the applications we have in mind: indeed, dependence between remaining life time and surrender is of course possible and should be taken into account. We may use the above result to do so.
Motivated by this, we will develop Proposition [4.4](https://arxiv.org/html/2510.06698v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting") further in the case of two stopping times.

Consider two 𝔽\mathbb{F}-adapted, increasing processes Λm\Lambda^{m}, and Λs\Lambda^{s} associated to τm\tau^{m} and τs\tau^{s}, respectively. Assume that there exist two standard exponential random variables Em,E^{m}, and EsE^{s}, independent of ℱT{\mathscr{F}}\_{T} having continuous survival copula

|  |  |  |
| --- | --- | --- |
|  | C¯​(u1,u2):=P​(exp⁡(−Em)<u1,exp⁡(−Es)<u2).\bar{C}(u\_{1},u\_{2}):=P\big(\exp(-E^{m})<u\_{1},\exp(-E^{s})<u\_{2}\big). |  |

Let
τm=inf{t∈𝕋:Λtm≥Em},\tau^{m}=\inf\{t\in\mathbb{T}:\Lambda\_{t}^{m}\geq E^{m}\}, and τs=inf{t∈𝕋:Λts≥Es}\tau^{s}=\inf\{t\in\mathbb{T}:\Lambda\_{t}^{s}\geq E^{s}\}; again we impose the convention that inf∅=T+1\inf\emptyset=T+1.
Using independence of EmE^{m}, EsE^{s} and ℱT{\mathscr{F}}\_{T}, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τm>t1,τs>t2|ℱT)\displaystyle P(\tau^{m}>t\_{1},\tau^{s}>t\_{2}|{\mathscr{F}}\_{T}) | =P​(Λt1m<Em,Λt2s​<Es|​ℱT)\displaystyle=P(\Lambda^{m}\_{t\_{1}}<E^{m},\Lambda^{s}\_{t\_{2}}<E^{s}|{\mathscr{F}}\_{T}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =P​(exp⁡(−Em)<e−Λt1m,exp⁡(−Es)​<e−Λt2s|​ℱT)\displaystyle=P\big(\exp(-E^{m})<e^{-\Lambda^{m}\_{t\_{1}}},\ \exp(-E^{s})<e^{-\Lambda^{s}\_{t\_{2}}}|{\mathscr{F}}\_{T}\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =C¯​(e−Λt1m,e−Λt2s).\displaystyle=\bar{C}\big(e^{-\Lambda^{m}\_{t\_{1}}},\ e^{-\Lambda^{s}\_{t\_{2}}}\big). |  | (38) |

###### Example 4.2 (Conditional independence).

If in addition, EmE^{m} and EsE^{s} are independent, then τm\tau^{m} and τs\tau^{s} are independent conditional on ℱT{\mathscr{F}}\_{T} and C​(u,v)=u⋅vC(u,v)=u\cdot v. This simplifies the computations significantly since then

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τm>t1,τs>t2|ℱT)=exp⁡(−Λt1m−Λt2s).\displaystyle P(\tau^{m}>t\_{1},\tau^{s}>t\_{2}|{\mathscr{F}}\_{T})=\exp(-\Lambda^{m}\_{t\_{1}}-\Lambda^{s}\_{t\_{2}}). |  | (39) |

This is a highly tractable extension of the doubly stochastic setting from Example [4.1](https://arxiv.org/html/2510.06698v1#S4.Thmexample1 "Example 4.1 (Doubly stochastic stopping times). ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting").
♢\diamondsuit

Fix t∈𝕋t\in\mathbb{T} and consider the disjoint ℋt{\mathscr{H}}\_{t}-measurable sets

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt1,1\displaystyle P\_{t}^{1,1} | :={τm>t,τs>t},\displaystyle:=\{\tau^{m}>t,\tau^{s}>t\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt2,u\displaystyle P\_{t}^{2,u} | :={τm>t,τs=u},u=0,…,t−1,\displaystyle:=\{\tau^{m}>t,\tau^{s}=u\},\ u=0,\dots,t-1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt3,u\displaystyle P\_{t}^{3,u} | :={τm=u,τs>t},u=0,…,t−1,\displaystyle:=\{\tau^{m}=u,\tau^{s}>t\},\ u=0,\dots,t-1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt4,u,v\displaystyle P\_{t}^{4,u,v} | :={τm=u,τs=v},u,v=0,…,t−1,\displaystyle:=\{\tau^{m}=u,\tau^{s}=v\},\ u,v=0,\dots,t-1, |  |

which will take the role of Pt1,…,PtnP\_{t}^{1},\dots,P\_{t}^{n} in the previous section.

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(t1,t2):=\displaystyle\Gamma(t\_{1},t\_{2}):= | P​(τm>t1,τs>t2|ℱT)=P​(τm>t1,τs>t2|ℱmax⁡{t1,t2})\displaystyle\ P(\tau^{m}>t\_{1},\tau^{s}>t\_{2}|{\mathscr{F}}\_{T})=P(\tau^{m}>t\_{1},\tau^{s}>t\_{2}|{\mathscr{F}}\_{\max\{t\_{1},t\_{2}\}}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | C¯​(exp⁡(−Λt1m),exp⁡(−Λt2s)).\displaystyle\ \bar{C}(\exp(-\Lambda^{m}\_{t\_{1}}),\exp(-\Lambda^{s}\_{t\_{2}})). |  | (40) |

Then we obtain from ([4.2](https://arxiv.org/html/2510.06698v1#S4.Ex15 "4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt1,1:=P​(τm>t,τs>t|ℱT)=Γ​(t,t),Gt2,u:=P​(τm>t,τs=u|ℱT)=P​(τm>t,τs>u−1|ℱT)−P​(τm>t,τs>u|ℱT)=Γ​(t,u−1)−Γ​(t,u),Gt3,u:=P​(τm=u,τs>t|ℱT)=Γ​(u−1,t)−Γ​(u,t),Gt4,u,v:=P​(τm=u,τs=v|ℱT)=Γ​(u−1,v−1)−Γ​(u,v−1)−Γ​(u−1,v)+Γ​(u,v),\displaystyle\begin{aligned} G\_{t}^{1,1}&:=P(\tau^{m}>t,\tau^{s}>t|{\mathscr{F}}\_{T})=\Gamma(t,t),\\ G\_{t}^{2,u}&:=P(\tau^{m}>t,\tau^{s}=u|{\mathscr{F}}\_{T})=P(\tau^{m}>t,\tau^{s}>u-1|{\mathscr{F}}\_{T})-P(\tau^{m}>t,\tau^{s}>u|{\mathscr{F}}\_{T})\\ &\,\,=\Gamma(t,u-1)-\Gamma(t,u),\\ G\_{t}^{3,u}&:=P(\tau^{m}=u,\tau^{s}>t|{\mathscr{F}}\_{T})=\Gamma(u-1,t)-\Gamma(u,t),\\ G\_{t}^{4,u,v}&:=P(\tau^{m}=u,\tau^{s}=v|{\mathscr{F}}\_{T})\\ &\,\,=\Gamma(u-1,v-1)-\Gamma(u,v-1)-\Gamma(u-1,v)+\Gamma(u,v),\end{aligned} |  | (41) |

where again u,v∈{0,…,t−1}u,v\in\{0,\dots,t-1\}.

Now, consider two 𝔽\mathbb{F}-adapted payment streams AmA^{m} and AsA^{s}. If the insurer dies at τm\tau^{m} before surrendering, he will receive AτmmA^{m}\_{\tau^{m}} while if he first surrenders, he will receive AτssA^{s}\_{\tau^{s}}. Precisely, this defines the following payoff:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt,T=𝟙{τm>t,τs>t}​(𝟙{τm<T,τm<τs}​Aτmm+𝟙{τs<T,τs≤τm}​Aτss).\displaystyle X\_{t,T}={\mathds{1}}\_{\{\tau^{m}>t,\tau^{s}>t\}}({\mathds{1}}\_{\{\tau^{m}<T,\tau^{m}<\tau^{s}\}}A^{m}\_{\tau^{m}}+{\mathds{1}}\_{\{\tau^{s}<T,\tau^{s}\leq\tau^{m}\}}A^{s}\_{\tau^{s}}). |  | (42) |

###### Proposition 4.5.

If we consider P∗=Q⊙PP^{\*}=\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP}, then
for the payoff in ([42](https://arxiv.org/html/2510.06698v1#S4.E42 "In 4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[Xt,T|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[X\_{t,T}|{\mathscr{H}}\_{t}] | =𝟙{τm>t,τs>t}​(Gt1,1)−1​∑u=t+1T−1EQ​[Aum​Gu3,u+Aus​Gu−12,u|ℱt].\displaystyle={\mathds{1}}\_{\{\tau^{m}>t,\tau^{s}>t\}}(G\_{t}^{1,1})^{-1}\sum\_{u=t+1}^{T-1}E\_{Q}[A\_{u}^{m}\,G\_{u}^{3,u}+A\_{u}^{s}\,G\_{u-1}^{2,u}|{\mathscr{F}}\_{t}]. |  |

###### Proof.

For the part with AmA^{m} we obtain the following decomposition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟙{t<τm<T,τm<τs}​Aτmm\displaystyle{\mathds{1}}\_{\{t<\tau^{m}<T,\ \tau^{m}<\tau^{s}\}}A^{m}\_{\tau^{m}} | =∑u=t+1T−1𝟙{τm=u,τs>u}​Aum=∑u=t+1T−1𝟙Pu3,u​Aum.\displaystyle=\sum\_{u=t+1}^{T-1}{\mathds{1}}\_{\{\tau^{m}=u,\tau^{s}>u\}}A^{m}\_{u}=\sum\_{u=t+1}^{T-1}{\mathds{1}}\_{P\_{u}^{3,u}}\,A^{m}\_{u}. |  |

Similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟙{t<τs<T,τm≥τs}​Aτss\displaystyle{\mathds{1}}\_{\{t<\tau^{s}<T,\tau^{m}\geq\tau^{s}\}}A^{s}\_{\tau^{s}} | =∑u=t+1T−1𝟙{τs=u,τm>u−1}​Aus=∑u=t+1T−1𝟙Pu−12,u​Aus.\displaystyle=\sum\_{u=t+1}^{T-1}{\mathds{1}}\_{\{\tau^{s}=u,\tau^{m}>u-1\}}A^{s}\_{u}=\sum\_{u=t+1}^{T-1}{\mathds{1}}\_{P\_{u-1}^{2,u}}A^{s}\_{u}. |  |

The result now follows by applying Proposition [4.4](https://arxiv.org/html/2510.06698v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.1. Multiple stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting").
∎

## 5. An affine framework

Affine processes are a highly tractable class of processes and highly suited to the question at hand, in particular for modelling stochastic mortality term structures and surrender times which depend on the evolution of the stock market. We refer to Keller-Ressel et al. ([2019](https://arxiv.org/html/2510.06698v1#bib.bib20)) for a detailed treatment of affine processes, including affine processes in discrete time.

In this section we propose a new framework in discrete time for the valuation of insurance products linked to financial markets. This generalizes existing approaches in three aspects: first, we incorporate the QP-approach in a general setting which allows for dependencies between financial markets, mortality, surrender and further factors. Note that this requires modelling the affine process under PP for the insurance quantities and under QQ for the parts of the affine process referring to the financial market. Second, it is important to acknowledge that the insurance part of the contract is monitored in discrete time, however. We therefore consider a discrete affine framework, i.e. an affine process with stochastic discontinuities. In the existing works in the insurance literature, only stochastically continuous affine processes are used. Third, we introduce valuation formulas for more than one stopping time, to include stochastic mortality and surrender, for example.

In this regard, assume that there is a driving d′d^{\prime}-dimensional process Z=(Zt)t∈𝕋Z=(Z\_{t})\_{t\in\mathbb{T}}. The process ZZ is *affine*, if it is a Markov process and its characteristic function is exponential affine. We additionally require the existence of exponential moments, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[exp⁡(u​Zt+1)|Zt]=exp⁡(A​(u)+B​(u)⋅Zt)\displaystyle E[\exp(uZ\_{t+1})|Z\_{t}]=\exp\big(A(u)+B(u)\cdot Z\_{t}\big) |  | (43) |

for 0≤t<T0\leq t<T and all u∈ℝd′u\in\mathbb{R}^{d^{\prime}}; with deterministic functions A:ℝd′→ℝA:\mathbb{R}^{d^{\prime}}\to\mathbb{R} and B:ℝd′→ℝd′B:\mathbb{R}^{d^{\prime}}\to\mathbb{R}^{d^{\prime}}. We will denote the state space of ZZ by 𝒵{\mathcal{Z}}. Typically 𝒵=ℝ≥0m×ℝn{\mathcal{Z}}=\mathbb{R}^{m}\_{\geq 0}\times\mathbb{R}^{n} with m+n=d′m+n=d^{\prime}.

In the light of the QP-rule it will be important to distinguish between the 𝔽\mathbb{F}-adapted parts of ZZ and the parts which are only ℍ\mathbb{H}-adapted. This will become important when we consider the set of equivalent martingale measures ℳe​(𝔽){\mathscr{M}}\_{e}(\mathbb{F}) where the choice of 𝔽\mathbb{F} plays an important role. In this regard, let Z=(X,Y)Z=(X,Y) with ZZ generating the publicly available information filtration 𝔽\mathbb{F}; here XX is d1d\_{1}-dimensional and YY is d2d\_{2}-dimensional, with d1+d2=d′d\_{1}+d\_{2}=d^{\prime}. Note that XX might contain insurance-related quantities which are not publicly available.

We model the stock market as an exponential driven by the affine process with an additional drift, i.e. we assume that discounted stock prices are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=exp⁡(a0​t+a⋅Yt),t≥0,\displaystyle S\_{t}=\exp(a\_{0}t+a\cdot Y\_{t}),\qquad t\geq 0, |  | (44) |

with (a0,a)=(a0,a1,…,ad2)∈ℝ1+d2(a\_{0},a)=(a\_{0},a\_{1},\dots,a\_{d\_{2}})\in\mathbb{R}^{1+d\_{2}}. This modeling contains the Black-Scholes model and exponential Lévy models as a special case (in discrete time).

Moreover, we assume that the conditional distribution of XtX\_{t}, conditional on YtY\_{t} and Xt−1X\_{t-1} has affine form and denote

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EP​[exp⁡(u⋅Xt)|Yt,Xt−1]\displaystyle E\_{P}[\exp(u\cdot X\_{t})|Y\_{t},X\_{t-1}] | =exp⁡(α​(u)+β​(u)⋅Xt−1+γ​(u)⋅Yt),\displaystyle=\exp\Big(\alpha(u)+\beta(u)\cdot X\_{t-1}+\gamma(u)\cdot Y\_{t}\Big), |  | (45) |

for all 0<t≤T0<t\leq T and u∈ℝd′u\in\mathbb{R}^{d^{\prime}}. The coefficients α,β,\alpha,\beta, and γ\gamma can be computed from AA and BB from Equation ([43](https://arxiv.org/html/2510.06698v1#S5.E43 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")).

To ensure absence of financial arbitrage, we assume that there exists an equivalent martingale measure QQ. To achieve a high degree of tractability, we assume that YY is again affine under QQ (with existing exponential moments),

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​[exp⁡(u​Yt+1)|Yt]=exp⁡(AQ​(u)+BQ​(u)⋅Yt)\displaystyle E\_{Q}[\exp(uY\_{t+1})|Y\_{t}]=\exp\big(A\_{Q}(u)+B\_{Q}(u)\cdot Y\_{t}\big) |  | (46) |

for all 0≤t<T0\leq t<T and u∈ℝd2u\in\mathbb{R}^{d\_{2}}.

###### Remark 5.1.

The Esscher change of measure is one well-known example which keeps the affine property during the measure change, but not the only one, see for example Kallsen and Muhle-Karbe ([2010](https://arxiv.org/html/2510.06698v1#bib.bib19)).

### 5.1. The case of one stopping time

For the modelling of a single random time τ\tau, we follow the doubly stochastic approach introduced in Example [4.1](https://arxiv.org/html/2510.06698v1#S4.Thmexample1 "Example 4.1 (Doubly stochastic stopping times). ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting"). Precisely, we consider a non-decreasing process Λ≥0\Lambda\geq 0 given by

|  |  |  |
| --- | --- | --- |
|  | Λt=b0+∑s=0t(b⋅Xs+c⋅Ys),t≥0\Lambda\_{t}=b\_{0}+\sum\_{s=0}^{t}\Big(b\cdot X\_{s}+c\cdot Y\_{s}\Big),\qquad t\geq 0 |  |

with (b0,b,c)∈ℝ1+d′(b\_{0},b,c)\in\mathbb{R}^{1+d^{\prime}}. Here, b0b\_{0} is chosen such that Λ0=0\Lambda\_{0}=0, guaranteeing in particular P​(τ=0)=0P(\tau=0)=0, and (b,c)(b,c) are chosen such that Λ\Lambda is non-decreasing.

Denote by 𝔽Z\mathbb{F}^{Z} the filtration generated by ZZ.
We assume that τ\tau is a doubly-stochastic stopping time, i.e. it satisfies ([30](https://arxiv.org/html/2510.06698v1#S4.E30 "In Example 4.1 (Doubly stochastic stopping times). ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) with
cumulative intensity Λ\Lambda.
Moreover, let ℍ\mathbb{H} be the progressive enlargement of 𝔽Z\mathbb{F}^{Z} with τ\tau, ℋt=ℱtZ∨(τ∧t){\mathscr{H}}\_{t}={\mathscr{F}}^{Z}\_{t}\vee(\tau\wedge t), for all t∈𝕋t\in\mathbb{T}.

For valuing the death benefit, we are interested in the claim Sτ​𝟙{t<τ≤T}S\_{\tau}{\mathds{1}}\_{\{t<\tau\leq T\}}, which we decompose to

|  |  |  |
| --- | --- | --- |
|  | ∑s=t+1TSs​(𝟙{τ>s−1}−𝟙{τ>s}).\sum\_{s=t+1}^{T}S\_{s}({\mathds{1}}\_{\{\tau>s-1\}}-{\mathds{1}}\_{\{\tau>s\}}). |  |

The following proposition allows to value this claim as well as the claim ST​𝟙{τ>T}S\_{T}{\mathds{1}}\_{\{\tau>T\}}.

Before this, we nee to introduce some notation.
We introduce the following recursive notation: define ϕ​(T)=α​(−b)+AQ​(a−c+γ​(−b))\phi(T)=\alpha(-b)+A\_{Q}(a-c+\gamma(-b)), ψ1​(T)=β​(−b)\psi^{1}(T)=\beta(-b), and ψ2​(T)=BQ​(a−c+γ​(−b))\psi^{2}(T)=B\_{Q}(a-c+\gamma(-b));
now let u​(s)=ψ1​(s+1)−bu(s)=\psi^{1}(s+1)-b, v​(s)=ψ2​(s+1)−cv(s)=\psi^{2}(s+1)-c and set

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(s)\displaystyle\phi(s) | =α​(u​(s))+AQ​(v​(s)+γ​(u​(s))),\displaystyle=\alpha(u(s))+A\_{Q}(v(s)+\gamma(u(s))), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ1​(s)\displaystyle\ \psi^{1}(s) | =β​(u​(s)),\displaystyle=\beta(u(s)), |  | (47) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ2​(s)\displaystyle\psi^{2}(s) | =BQ​(v​(s)+γ​(u​(s)))\displaystyle=B\_{Q}(v(s)+\gamma(u(s))) |  |

for s=0,…,T−1s=0,\dots,T-1. Moreover,
ϕ′​(T)=AQ​(a)\phi^{\prime}(T)=A\_{Q}(a), ψ′⁣1​(T)=0\psi^{\prime 1}(T)=0, and ψ′⁣2​(T)=BQ​(a)\psi^{\prime 2}(T)=B\_{Q}(a), following the same recursion rule ([5.1](https://arxiv.org/html/2510.06698v1#S5.Ex27 "5.1. The case of one stopping time ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")).
Denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(t,T)=∑s=t+1Tϕ​(s),\displaystyle\Phi(t,T)=\sum\_{s=t+1}^{T}\phi(s), |  | (48) |

and, analogously, Φ′​(t,T)=∑s=t+1Tϕ′​(s)\Phi^{\prime}(t,T)=\sum\_{s=t+1}^{T}\phi^{\prime}(s). Moreover we write

|  |  |  |
| --- | --- | --- |
|  | ψ​(t+1)⋅Zt:=ψ1​(t+1)⋅Xt+ψ2​(t+1)⋅Yt,\psi(t+1)\cdot Z\_{t}:=\psi^{1}(t+1)\cdot X\_{t}+\psi^{2}(t+1)\cdot Y\_{t}, |  |

again analogously for ψ′\psi^{\prime}.

###### Proposition 5.1.

We have the following valuation-results

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[ST​𝟙{τ>T}|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[S\_{T}{\mathds{1}}\_{\{\tau>T\}}|{\mathscr{H}}\_{t}] | =𝟙{τ>t}​ea0​T+Φ​(t,T)+ψ​(t+1)⋅Zt,\displaystyle={\mathds{1}}\_{\{\tau>t\}}e^{a\_{0}T+\Phi(t,T)+\psi(t+1)\cdot Z\_{t}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[ST​𝟙{τ>T−1}|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[S\_{T}{\mathds{1}}\_{\{\tau>T-1\}}|{\mathscr{H}}\_{t}] | =𝟙{τ>t}​ea0​T+Φ′​(t,T)+ψ′​(t+1)⋅Zt.\displaystyle={\mathds{1}}\_{\{\tau>t\}}e^{a\_{0}T+\Phi^{\prime}(t,T)+\psi^{\prime}(t+1)\cdot Z\_{t}}. |  |

###### Proof.

Using Proposition [4.3](https://arxiv.org/html/2510.06698v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting"), and the affine representations of SS and Λ\Lambda, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P\displaystyle E\_{\operatorname{Q\odot P}} | [ST​𝟙{τ>T}|ℋt]=𝟙{τ>t}​eΛt​EQ⊙P​[ST​e−ΛT|ℱtZ]\displaystyle[S\_{T}{\mathds{1}}\_{\{\tau>T\}}|{\mathscr{H}}\_{t}]={\mathds{1}}\_{\{\tau>t\}}e^{\Lambda\_{t}}E\_{\operatorname{Q\odot P}}[S\_{T}e^{-\Lambda\_{T}}|{\mathscr{F}}^{Z}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝟙{τ>t}​EQ⊙P​[exp⁡(a0​T+a⋅YT−∑s=t+1T(b⋅Xs+c⋅Ys))|Zt].\displaystyle={\mathds{1}}\_{\{\tau>t\}}E\_{\operatorname{Q\odot P}}\Big[\exp\Big(a\_{0}T+a\cdot Y\_{T}-\sum\_{s=t+1}^{T}\big(b\cdot X\_{s}+c\cdot Y\_{s}\big)\Big)\,\big|\,Z\_{t}\Big]. |  |

Now we proceed iteratively: first, consider the summation index s=Ts=T in the above equation.
Then, by Equation ([45](https://arxiv.org/html/2510.06698v1#S5.E45 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and by Equation ([46](https://arxiv.org/html/2510.06698v1#S5.E46 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")), respectively,

|  |  |  |  |
| --- | --- | --- | --- |
|  | EP​[e−b⋅XT|ℱT−1Z∨YT]\displaystyle E\_{P}[e^{-b\,\cdot X\_{T}}|{\mathscr{F}}^{Z}\_{T-1}\vee Y\_{T}] | =eα​(−b)+β​(−b)⋅XT−1+γ​(−b)⋅YT,\displaystyle=e^{\alpha(-b)+\beta(-b)\cdot X\_{T-1}+\gamma(-b)\cdot Y\_{T}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​[e(a−c+γ​(−b))⋅YT|ℱT−1Z]\displaystyle E\_{Q}[e^{(a-c+\gamma(-b))\cdot Y\_{T}}|{\mathscr{F}}^{Z}\_{T-1}] | =eAQ​(a−c+γ​(−b))+BQ​(a−c+γ​(−b))⋅YT−1.\displaystyle=e^{A\_{Q}(a-c+\gamma(-b))+B\_{Q}(a-c+\gamma(-b))\cdot Y\_{T-1}}. |  |

Altogether, these two steps yield that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ⊙P​[eu⋅Xs+v⋅Ys|ℱs−1Z]\displaystyle E\_{\operatorname{Q\odot P}}[e^{u\cdot X\_{s}+v\cdot Y\_{s}}|{\mathscr{F}}^{Z}\_{s-1}] | =eα​(u)+β​(u)⋅Xs−1+AQ​(v+γ​(u))+BQ​(v+γ​(u))⋅Ys−1.\displaystyle=e^{\alpha(u)+\beta(u)\cdot X\_{s-1}+A\_{Q}(v+\gamma(u))+B\_{Q}(v+\gamma(u))\cdot Y\_{s-1}}. |  | (49) |

With this formula, we can compute the next step (corresponding to the summation index s=T−1s=T-1) where we choose
u=β​(−b)−bu=\beta(-b)-b and v=BQ​(a−c+γ​(−b))−cv=B\_{Q}(a-c+\gamma(-b))-c.
Proceeding iteratively until s=t+1s=t+1 yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[ST​𝟙{τ>T}|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[S\_{T}{\mathds{1}}\_{\{\tau>T\}}|{\mathscr{H}}\_{t}] | =𝟙{τ>t}​ea0​T+∑s=t+1Tϕ​(s)+ψ1​(t+1)⋅Xt+ψ2​(t+1)⋅Yt,\displaystyle={\mathds{1}}\_{\{\tau>t\}}e^{a\_{0}T+\sum\_{s=t+1}^{T}\phi(s)+\psi^{1}(t+1)\cdot X\_{t}+\psi^{2}(t+1)\cdot Y\_{t}}, |  |

the first claim.
The second claim follows in a similar way. ∎

### 5.2. Survival and surrender

Since we are interested in modelling surrender and survival, we need to consider two stopping times. To exploit the full power of the affine framework, we will assume that they are conditionally independent, as in Example [4.2](https://arxiv.org/html/2510.06698v1#S4.Thmexample2 "Example 4.2 (Conditional independence). ‣ 4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting").
More general schemes could use copulas or
could include self-exciting effects, like in Errais et al. ([2010](https://arxiv.org/html/2510.06698v1#bib.bib14)) which, however, seems less important for the insurance application we have in mind.

In this regard, let τm,τs\tau^{m},\tau^{s} be conditionally independent, doubly stochastic random times as introduced in Section [4.2](https://arxiv.org/html/2510.06698v1#S4.SS2 "4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting") with associated cumulated intensities Λm\Lambda^{m} and Λs\Lambda^{s}. We assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λti=b0i+∑s=0t(bi⋅Xs+ci⋅Ys),t≥0\displaystyle\Lambda\_{t}^{i}=b\_{0}^{i}+\sum\_{s=0}^{t}\big(b^{i}\cdot X\_{s}+c^{i}\cdot Y\_{s}\big),\qquad t\geq 0 |  | (50) |

with (b0i,bi,ci)∈ℝ1+d′(b\_{0}^{i},b^{i},c^{i})\in\mathbb{R}^{1+d^{\prime}}, i∈{m,s}i\in\{m,s\}. Again, the coefficients need to be chosen such that the processes start in 0 and are increasing.

First, we obtain that under these assumptions by Equation ([39](https://arxiv.org/html/2510.06698v1#S4.E39 "In Example 4.2 (Conditional independence). ‣ 4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) and Equations ([41](https://arxiv.org/html/2510.06698v1#S4.E41 "In 4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt1,1\displaystyle G\_{t}^{1,1} | =e−Λtm−Λts,\displaystyle=e^{-\Lambda^{m}\_{t}-\Lambda^{s}\_{t}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gt2,u\displaystyle G\_{t}^{2,u} | =e−Λtm​(e−Λu−1s−e−Λus),\displaystyle=e^{-\Lambda^{m}\_{t}}\Big(e^{-\Lambda^{s}\_{u-1}}-e^{-\Lambda^{s}\_{u}}\Big), |  | (51) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt3,u\displaystyle G\_{t}^{3,u} | =(e−Λu−1m−e−Λum)​e−Λts\displaystyle=\Big(e^{-\Lambda^{m}\_{u-1}}-e^{-\Lambda^{m}\_{u}}\Big)e^{-\Lambda^{s}\_{t}} |  |

with an analogous expression for G4G^{4} (which will not be used here).

From these expressions it is clear that we need to generalize our previous notions of ϕ\phi and ψ\psi. Fix 0≤s<T0\leq s<T and
consider κ=(κ1,κ2)\kappa=(\kappa^{1},\kappa^{2}), (we use κ1\kappa^{1} for the coefficients associated with XX and κ2\kappa^{2} for those associated with YY) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ​(t,s)=κ​(a,t,s):={(−bm,a−cm)t=T,(−bm,−cm)s<t<T,(−bm−bs,−cm−cs)t≤s,\displaystyle\kappa(t,s)=\kappa(a,t,s):=\begin{cases}(-b^{m},a-c^{m})&t=T,\\ (-b^{m},-c^{m})&s<t<T,\\ (-b^{m}-b^{s},-c^{m}-c^{s})&t\leq s,\end{cases} |  | (52) |

for s∈{0,…,T}s\in\{0,\dots,T\}. We highlight the dependence on aa, whenever necessary, through the notation κ​(a,t,s)\kappa(a,t,s).
Note that, with this definition κ1​(T,T)=−bm\kappa^{1}(T,T)=-b^{m} and κ2​(T,T)=a−cm\kappa^{2}(T,T)=a-c^{m}, for example.

Next, we define recursively, following ([5.1](https://arxiv.org/html/2510.06698v1#S5.Ex27 "5.1. The case of one stopping time ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(T,s)=α​(κ1​(s,T))+AQ​(κ2​(s,T)+γ​(κ1​(s,T))),ψ1​(T,s)=β​(κ1​(s,T)),ψ2​(T,s)=BQ​(κ2​(s,T)+γ​(κ1​(s,T)))ϕ​(t,s)=α​(u​(t,s))+AQ​(v​(t,s)+γ​(u​(t,s))),ψ1​(t,s)=β​(u​(t,s)),ψ2​(t,s)=BQ​(v​(t,s)+γ​(u​(t,s))),\displaystyle\begin{aligned} \phi(T,s)&=\alpha(\kappa^{1}(s,T))+A\_{Q}(\kappa^{2}(s,T)+\gamma(\kappa^{1}(s,T))),\\ \psi^{1}(T,s)&=\beta(\kappa^{1}(s,T)),\\ \psi^{2}(T,s)&=B\_{Q}(\kappa^{2}(s,T)+\gamma(\kappa^{1}(s,T)))\\ \phi(t,s)&=\alpha(u(t,s))+A\_{Q}(v(t,s)+\gamma(u(t,s))),\\ \psi^{1}(t,s)&=\beta(u(t,s)),\\ \psi^{2}(t,s)&=B\_{Q}(v(t,s)+\gamma(u(t,s))),\end{aligned} |  | (53) |

with u​(t,s)=ψ1​(t+1,s)+κ1​(t,s)u(t,s)=\psi^{1}(t+1,s)+\kappa^{1}(t,s), v​(t,s)=ψ2​(t+1,s)+κ2​(t,s)v(t,s)=\psi^{2}(t+1,s)+\kappa^{2}(t,s) and t=0,…,T−1t=0,\dots,T-1.
Again, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(t,s,T)=∑t′=t+1Tϕ​(t′,s)\displaystyle\Phi(t,s,T)=\sum\_{t^{\prime}=t+1}^{T}\phi(t^{\prime},s) |  | (54) |

and ψ1⋅X+ψ2⋅Y=ψ⋅Z\psi^{1}\cdot X+\psi^{2}\cdot Y=\psi\cdot Z. The coefficients ϕ′,ψ′\phi^{\prime},\ \psi^{\prime} and Φ′\Phi^{\prime} are obtained by the same recursion, exchanging bmb^{m} and cmc^{m} for bsb^{s} and csc^{s} in κ\kappa.
With this notation, we have the following valuation-results:

###### Proposition 5.2.

For t≤s≤Tt\leq s\leq T, and on {τm>t,τs>t}\{\tau^{m}>t,\tau^{s}>t\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[ST​𝟙{τm>T,τs>s}|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[S\_{T}{\mathds{1}}\_{\{\tau^{m}>T,\tau^{s}>s\}}|{\mathscr{H}}\_{t}] | =eΛtm+Λts​EQ⊙P​[ST​e−ΛTm−Λss|ℱtZ]\displaystyle=e^{\Lambda^{m}\_{t}+\Lambda^{s}\_{t}}E\_{\operatorname{Q\odot P}}[S\_{T}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ea0​T+Φ​(t,s,T)+ψ​(t+1,s)⋅Zt\displaystyle=e^{a\_{0}T+\Phi(t,s,T)+\psi(t+1,s)\cdot Z\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[ST​𝟙{τm>s,τs>T}|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}[S\_{T}{\mathds{1}}\_{\{\tau^{m}>s,\tau^{s}>T\}}|{\mathscr{H}}\_{t}] | =eΛtm+Λts​EQ⊙P​[ST​e−Λsm−ΛTs|ℱtZ]\displaystyle=e^{\Lambda^{m}\_{t}+\Lambda^{s}\_{t}}E\_{\operatorname{Q\odot P}}[S\_{T}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{T}}|{\mathscr{F}}^{Z}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ea0​T+Φ′​(t,s,T)+ψ′​(t+1,s)⋅Zt.\displaystyle=e^{a\_{0}T+\Phi^{\prime}(t,s,T)+\psi^{\prime}(t+1,s)\cdot Z\_{t}}. |  |

###### Proof.

We proceed iteratively as in the proof of Proposition [5.1](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem1 "Proposition 5.1. ‣ 5.1. The case of one stopping time ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"). Note that, by Equations ([44](https://arxiv.org/html/2510.06698v1#S5.E44 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and ([50](https://arxiv.org/html/2510.06698v1#S5.E50 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ST⋅eΛtm+Λts⋅e−ΛTm−Λss=ea0​T+a⋅YT−∑i=t+1T(bm​Xi+cm​Yi)−∑j=t+1s(bs​Xj+cs​Yj).\displaystyle S\_{T}\cdot e^{\Lambda^{m}\_{t}+\Lambda^{s}\_{t}}\cdot e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{s}}=e^{a\_{0}T+a\cdot Y\_{T}-\sum\_{i=t+1}^{T}(b^{m}X\_{i}+c^{m}Y\_{i})-\sum\_{j=t+1}^{s}(b^{s}X\_{j}+c^{s}Y\_{j})}. |  | (55) |

For the time point TT with s<Ts<T, we obtain with ([49](https://arxiv.org/html/2510.06698v1#S5.E49 "In 5.1. The case of one stopping time ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[e−bm⋅XT+(a−cm)⋅YT|ℱT−1Z]\displaystyle E\_{\operatorname{Q\odot P}}[e^{-b^{m}\cdot X\_{T}+(a-c^{m})\cdot Y\_{T}}|{\mathscr{F}}^{Z}\_{T-1}] | =eα​(−bm)+β​(−bm)⋅XT−1+AQ​(a−cm+γ​(−bm))+BQ​(a−cm+γ​(−bm))⋅YT−1\displaystyle=e^{\alpha(-b^{m})+\beta(-b^{m})\cdot X\_{T-1}+A\_{Q}(a-c^{m}+\gamma(-b^{m}))+B\_{Q}(a-c^{m}+\gamma(-b^{m}))\cdot Y\_{T-1}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =eϕ​(T,T)+ψ1​(T,T)⋅XT−1+ψ2​(T,T)⋅YT−1.\displaystyle=e^{\phi(T,T)+\psi^{1}(T,T)\cdot X\_{T-1}+\psi^{2}(T,T)\cdot Y\_{T-1}}. |  | (56) |

Note that ϕ​(T,T)=ϕ​(T,s)\phi(T,T)=\phi(T,s) and ψ​(T,T)=ψ​(T,s)\psi(T,T)=\psi(T,s) by definition.
For the time point T−1T-1, we have to compute (since s≤T−1s\leq T-1)

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[e(ψ1​(T,s)−bm)⋅XT+(ψ2​(T,s)−cm)⋅YT|ℱT−1Z]\displaystyle E\_{\operatorname{Q\odot P}}\Big[e^{(\psi^{1}(T,s)-b^{m})\cdot X\_{T}+(\psi^{2}(T,s)-c^{m})\cdot Y\_{T}}|{\mathscr{F}}^{Z}\_{T-1}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =EQ⊙P​[eu​(T−1,s)⋅XT+v​(T−1,s)⋅YT|ℱT−1Z]\displaystyle=E\_{\operatorname{Q\odot P}}\Big[e^{u(T-1,s)\cdot X\_{T}+v(T-1,s)\cdot Y\_{T}}|{\mathscr{F}}^{Z}\_{T-1}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =eϕ​(T−1,s)+ψ1​(T−1,s)⋅XT−1+ψ2​(T−1,s)⋅YT−1,\displaystyle=e^{\phi(T-1,s)+\psi^{1}(T-1,s)\cdot X\_{T-1}+\psi^{2}(T-1,s)\cdot Y\_{T-1}}, |  | (57) |

where we again used Equation ([49](https://arxiv.org/html/2510.06698v1#S5.E49 "In 5.1. The case of one stopping time ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")).
For time points t′≤T−1t^{\prime}\leq T-1 we have to consider the two cases t′>st^{\prime}>s and t′≤st^{\prime}\leq s. For the first case, we obtain as above that

|  |  |  |
| --- | --- | --- |
|  | EQ​[e(ψ1​(t′,s)−bm)⋅Xt′+(ψ2​(t′,s)−cm)⋅Yt′|ℱt′−1Z]=eϕ​(t′−1,s)+ψ1​(t′−1,s)⋅Xt′−1+ψ2​(t′−1,s)⋅Yt′−1.\displaystyle E\_{Q}[e^{(\psi^{1}(t^{\prime},s)-b^{m})\cdot X\_{t^{\prime}}+(\psi^{2}(t^{\prime},s)-c^{m})\cdot Y\_{t^{\prime}}}|{\mathscr{F}}^{Z}\_{t^{\prime}-1}]=e^{\phi(t^{\prime}-1,s)+\psi^{1}(t^{\prime}-1,s)\cdot X\_{t^{\prime}-1}+\psi^{2}(t^{\prime}-1,s)\cdot Y\_{t^{\prime}-1}}. |  |

For t′≤st^{\prime}\leq s on the other side, we have to compute, see Equation ([55](https://arxiv.org/html/2510.06698v1#S5.E55 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[e(ψ1​(t′,s)−bm−bs)⋅Xt′+(ψ2​(t′,s)−cm−cs)⋅Yt′|ℱt′−1Z]\displaystyle E\_{\operatorname{Q\odot P}}\Big[e^{(\psi^{1}(t^{\prime},s)-b^{m}-b^{s})\cdot X\_{t^{\prime}}+(\psi^{2}(t^{\prime},s)-c^{m}-c^{s})\cdot Y\_{t^{\prime}}}|{\mathscr{F}}^{Z}\_{t^{\prime}-1}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =EQ⊙P​[eu​(t′,s)⋅Xt′+v​(t′,s)⋅Yt′|ℱt′−1Z]\displaystyle=E\_{\operatorname{Q\odot P}}\Big[e^{u(t^{\prime},s)\cdot X\_{t^{\prime}}+v(t^{\prime},s)\cdot Y\_{t^{\prime}}}|{\mathscr{F}}^{Z}\_{t^{\prime}-1}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =eϕ​(t′−1,s)+ψ1​(t′−1,s)⋅Xt′−1+ψ2​(t′−1,s)⋅Yt′−1\displaystyle=e^{\phi(t^{\prime}-1,s)+\psi^{1}(t^{\prime}-1,s)\cdot X\_{t^{\prime}-1}+\psi^{2}(t^{\prime}-1,s)\cdot Y\_{t^{\prime}-1}} |  |

and the first claim follows for s<Ts<T. For the second claim, note that we have to consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | ST⋅eΛtm+Λts⋅e−Λsm−ΛTs=ea0​T+a⋅YT−∑i=t+1s(bm​Xi+cm​Yi)−∑j=t+1T(bs​Xj+cs​Yj).\displaystyle S\_{T}\cdot e^{\Lambda^{m}\_{t}+\Lambda^{s}\_{t}}\cdot e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{T}}=e^{a\_{0}T+a\cdot Y\_{T}-\sum\_{i=t+1}^{s}(b^{m}X\_{i}+c^{m}Y\_{i})-\sum\_{j=t+1}^{T}(b^{s}X\_{j}+c^{s}Y\_{j})}. |  | (58) |

This means the recursion starts with coefficients bsb^{s} and csc^{s} instead of bmb^{m} and cmc^{m} which gives the coefficients ϕ′\phi^{\prime}, and ψ′\psi^{\prime} and the second claim follows.

Finally, if s=Ts=T, at the final time point TT, we have to modify and consider

|  |  |  |
| --- | --- | --- |
|  | EQ⊙P​[e(−bm−bs)⋅XT+(a−cm−cs)⋅YT|ℱT−1Z]\displaystyle E\_{\operatorname{Q\odot P}}[e^{(-b^{m}-b^{s})\cdot X\_{T}+(a-c^{m}-c^{s})\cdot Y\_{T}}|{\mathscr{F}}^{Z}\_{T-1}] |  |

instead. This is reflected by the choice of κ​(T,T)\kappa(T,T) in Equation ([52](https://arxiv.org/html/2510.06698v1#S5.E52 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and the conclusion follows.
∎

In the next step we extend this proposition to allow for fractions ST/ST′.\nicefrac{{S\_{T}}}{{S\_{T^{\prime}}}}. While for T′≤tT^{\prime}\leq t this immediate, the following results gives the extension for T′>t.T^{\prime}>t. Also the case T′=TT^{\prime}=T can be obtained readily from Proposition [5.2](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting") by letting a0=a=0a\_{0}=a=0.

Define recursively, as above

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ2​(T,s,T′)=BQ​(κ2​(s,T)+γ​(κ1​(s,T)))ψ2​(t,s,T′)=BQ​(v​(t,s)+γ​(u​(t,s)))−𝟙{t−1=T′}​a.\displaystyle\begin{aligned} \psi^{2}(T,s,T^{\prime})&=B\_{Q}(\kappa^{2}(s,T)+\gamma(\kappa^{1}(s,T)))\\ \psi^{2}(t,s,T^{\prime})&=B\_{Q}(v(t,s)+\gamma(u(t,s)))-{\mathds{1}}\_{\{t-1=T^{\prime}\}}a.\end{aligned} |  | (59) |

and let
ψ1(t,s)⋅X+ψ2(t,s,T′)⋅Y=:ψ(t,s,T′)⋅Z\psi^{1}(t,s)\cdot X+\psi^{2}(t,s,T^{\prime})\cdot Y=:\psi(t,s,T^{\prime})\cdot Z. The coefficient ψ′\psi^{\prime} is obtained by the same recursion, exchanging bmb^{m} and cmc^{m} for bsb^{s} and csc^{s} in κ\kappa.

###### Proposition 5.3.

For t≤s≤Tt\leq s\leq T and t<T′<Tt<T^{\prime}<T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−ΛTm−Λss|ℱtZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] | =ea0​(T−T′)+Φ​(t,s,T)+ψ​(t+1,s,T′)⋅Zt\displaystyle=e^{a\_{0}(T-T^{\prime})+\Phi(t,s,T)+\psi(t+1,s,T^{\prime})\cdot Z\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−Λsm−ΛTs|ℋt]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{T}}|{\mathscr{H}}\_{t}\Big] | =ea0​(T−T′)+Φ′​(t,s,T)+ψ′​(t+1,s,T′)⋅Zt.\displaystyle=e^{a\_{0}(T-T^{\prime})+\Phi^{\prime}(t,s,T)+\psi^{\prime}(t+1,s,T^{\prime})\cdot Z\_{t}}. |  |

###### Proof.

The proof proceeds similarly as in the proof of Proposition [5.2](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"). To start with, we note that, by Equations ([44](https://arxiv.org/html/2510.06698v1#S5.E44 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and ([50](https://arxiv.org/html/2510.06698v1#S5.E50 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | STST′⋅eΛtm+Λts⋅e−ΛTm−Λss=ea0​(T−T′)+a⋅(YT−YT′)−∑i=t+1T(bm​Xi+cm​Yi)−∑j=t+1s(bs​Xj+cs​Yj).\displaystyle\frac{S\_{T}}{S\_{T^{\prime}}}\cdot e^{\Lambda^{m}\_{t}+\Lambda^{s}\_{t}}\cdot e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{s}}=e^{a\_{0}(T-T^{\prime})+a\cdot(Y\_{T}-Y\_{T^{\prime}})-\sum\_{i=t+1}^{T}(b^{m}X\_{i}+c^{m}Y\_{i})-\sum\_{j=t+1}^{s}(b^{s}X\_{j}+c^{s}Y\_{j})}. |  | (60) |

For the time point T>T′T>T^{\prime}, we recall from ([56](https://arxiv.org/html/2510.06698v1#S5.E56 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[e−bm⋅XT+(a−cm)⋅YT|ℱT−1Z]\displaystyle E\_{\operatorname{Q\odot P}}[e^{-b^{m}\cdot X\_{T}+(a-c^{m})\cdot Y\_{T}}|{\mathscr{F}}^{Z}\_{T-1}] | =eϕ​(T,T)+ψ1​(T,T)⋅XT−1+ψ2​(T,T)⋅YT−1.\displaystyle=e^{\phi(T,T)+\psi^{1}(T,T)\cdot X\_{T-1}+\psi^{2}(T,T)\cdot Y\_{T-1}}. |  |

Note that ϕ​(T,T,T′)=ϕ​(T,s,T′)\phi(T,T,T^{\prime})=\phi(T,s,T^{\prime}) and ψ​(T,T,T′)=ψ​(T,s,T′)\psi(T,T,T^{\prime})=\psi(T,s,T^{\prime}) by definition.
For the time point T−1T-1, we have to compute (since s≤T−1s\leq T-1)

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[e(ψ1​(T,s)−bm)⋅XT+(ψ2​(T,s)−cm)⋅YT−a​YT′|ℱT−1Z]\displaystyle E\_{\operatorname{Q\odot P}}\Big[e^{(\psi^{1}(T,s)-b^{m})\cdot X\_{T}+(\psi^{2}(T,s)-c^{m})\cdot Y\_{T}-aY\_{T^{\prime}}}|{\mathscr{F}}^{Z}\_{T-1}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =eϕ​(T−1,s)+ψ1​(T−1,s)⋅XT−1+ψ2​(T−1,s)⋅YT−1−a​YT′,\displaystyle=e^{\phi(T-1,s)+\psi^{1}(T-1,s)\cdot X\_{T-1}+\psi^{2}(T-1,s)\cdot Y\_{T-1}-aY\_{T^{\prime}}}, |  |

according to Equation ([57](https://arxiv.org/html/2510.06698v1#S5.E57 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")).
It becomes apparent, that for T−1=T′T-1=T^{\prime}, ψ2​(T−1,s)\psi^{2}(T-1,s) from the recursion in Proposition [5.2](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting") has to be replaced by ψ2​(T−1,s)−a\psi^{2}(T-1,s)-a and the claim follows easily.
∎

For the next result, we first extend ([46](https://arxiv.org/html/2510.06698v1#S5.E46 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) to arbitrary times. For t<Tt<T, we define recursively

|  |  |  |  |
| --- | --- | --- | --- |
|  | AQ​(T−1,T)=a0​T+AQ​(a),AQ​(t,T)=AQ​(t+1,T)+AQ​(BQ​(t+1,T)),BQ​(T−1,T)=BQ​(a)BQ​(t,T)=BQ​(BQ​(t+1,T)).\displaystyle\begin{aligned} A\_{Q}(T-1,T)&=a\_{0}T+A\_{Q}(a),\\ A\_{Q}(t,T)&=A\_{Q}(t+1,T)+A\_{Q}(B\_{Q}(t+1,T)),\\ B\_{Q}(T-1,T)&=B\_{Q}(a)\\ B\_{Q}(t,T)&=B\_{Q}(B\_{Q}(t+1,T)).\end{aligned} |  | (61) |

We will also use the notation AQ​(t,T,a0,a)A\_{Q}(t,T,a\_{0},a) and BQ​(t,T,a)B\_{Q}(t,T,a) to highlight the dependence on a0a\_{0} and aa, whenever necessary.

###### Proposition 5.4.

Under Equation ([46](https://arxiv.org/html/2510.06698v1#S5.E46 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​[ST|ℱtZ]=eAQ​(t,T)+BQ​(t,T)⋅Yt\displaystyle E\_{Q}[S\_{T}|{\mathscr{F}}\_{t}^{Z}]=e^{A\_{Q}(t,T)+B\_{Q}(t,T)\cdot Y\_{t}} |  | (62) |

with the coefficients AQ​(t,T)A\_{Q}(t,T) and BQ​(t,T)B\_{Q}(t,T) defined in Equation ([61](https://arxiv.org/html/2510.06698v1#S5.E61 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")).

###### Proof.

This result follows by an iterated application of ([46](https://arxiv.org/html/2510.06698v1#S5.E46 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")). Indeed, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​[ST|ℱT−1Z]\displaystyle E\_{Q}[S\_{T}|{\mathscr{F}}\_{T-1}^{Z}] | =ea0​T+AQ​(a)+BQ​(a)⋅YT−1=eAQ​(T−1,T)+BQ​(T−1,T)⋅YT−1.\displaystyle=e^{a\_{0}T+A\_{Q}(a)+B\_{Q}(a)\cdot Y\_{T-1}}=e^{A\_{Q}(T-1,T)+B\_{Q}(T-1,T)\cdot Y\_{T-1}}. |  |

Moreover, for any s≥ts\geq t and s≤Ts\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ​[eAQ​(s+1,T)+BQ​(s+1,T)⋅Ys+1|ℱsZ]\displaystyle E\_{Q}[e^{A\_{Q}(s+1,T)+B\_{Q}(s+1,T)\cdot Y\_{s+1}}|{\mathscr{F}}\_{s}^{Z}] | =eAQ​(s+1,T)+AQ​(BQ​(s+1,T))+BQ​(BQ​(s+1,T))⋅Ys\displaystyle=e^{A\_{Q}(s+1,T)+A\_{Q}(B\_{Q}(s+1,T))+B\_{Q}(B\_{Q}(s+1,T))\cdot Y\_{s}} |  |

and the claim follows.
∎

For the following result, we need to handle the dependence on aa specifically depending on time.
We therefore define recursively, as above

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ2​(T,s,T′,a,a¯)=BQ​(κ2​(a,s,T)+γ​(κ1​(a,s,T)))ψ2​(t,s,T′,a,a¯)=BQ​(v​(a,t,s)+γ​(u​(a,t,s)))−𝟙{t−1=T′}​a¯.\displaystyle\begin{aligned} \psi^{2}(T,s,T^{\prime},a,\bar{a})&=B\_{Q}(\kappa^{2}(a,s,T)+\gamma(\kappa^{1}(a,s,T)))\\ \psi^{2}(t,s,T^{\prime},a,\bar{a})&=B\_{Q}(v(a,t,s)+\gamma(u(a,t,s)))-{\mathds{1}}\_{\{t-1=T^{\prime}\}}\bar{a}.\end{aligned} |  | (63) |

with u​(a,t,s)=ψ1​(t+1,s)+κ1​(a,t,s)u(a,t,s)=\psi^{1}(t+1,s)+\kappa^{1}(a,t,s), v​(a,t,s)=ψ2​(a,t+1,s)+κ2​(a,t,s)v(a,t,s)=\psi^{2}(a,t+1,s)+\kappa^{2}(a,t,s)
and let
ψ1(t,s)⋅X+ψ2(t,s,T′,a,a¯)⋅Y=:ψ(t,s,T′,a,a¯)⋅Z\psi^{1}(t,s)\cdot X+\psi^{2}(t,s,T^{\prime},a,\bar{a})\cdot Y=:\psi(t,s,T^{\prime},a,\bar{a})\cdot Z. The coefficient ψ′\psi^{\prime} is obtained by the same recursion, exchanging bmb^{m} and cmc^{m} for bsb^{s} and csc^{s} in κ\kappa.

###### Proposition 5.5.

For t≤s<Tt\leq s<T and t<T′<st<T^{\prime}<s,

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−Λsm−Λss|ℱtZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] | =eAQ​(s,T)−a0​T+Φ​(t,s,s)+ψ​(t+1,s,T′,BQ​(s,T),a)⋅Zt.\displaystyle=e^{A\_{Q}(s,T)-a\_{0}T+\Phi(t,s,s)+\psi(t+1,s,T^{\prime},B\_{Q}(s,T),a)\cdot Z\_{t}}. |  |

On the other side, if s≤T′≤Ts\leq T^{\prime}\leq T, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−Λsm−Λss|ℱtZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] | =e−a0​T′+AQ​(T′,T)+AQ​(s,T′,0,(BQ​(T′,T)−a))\displaystyle=e^{-a\_{0}T^{\prime}+A\_{Q}(T^{\prime},T)+A\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅eΦ​(t,s,s,BQ​(s,T′,0,(BQ​(T′,T)−a)))+ψ​(t+1,s,BQ​(s,T′,0,(BQ​(T′,T)−a)))⋅Zt\displaystyle\quad\cdot e^{\Phi\big(t,s,s,B\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))\big)+\psi\big(t+1,s,B\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))\big)\cdot Z\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅e−Λtm−Λts.\displaystyle\quad\cdot e^{-\Lambda\_{t}^{m}-\Lambda\_{t}^{s}}. |  |

###### Proof.

We use iterated conditional expectations and the affine property to prove this result. Note that, in the case where T′<sT^{\prime}<s, by Equation ([62](https://arxiv.org/html/2510.06698v1#S5.E62 "In Proposition 5.4. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−Λsm−Λss|ℱtZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] | =EQ⊙P​[eAQ​(s,T)+BQ​(s,T)⋅YsST′​e−Λsm−Λss|ℱtZ]\displaystyle=E\_{\operatorname{Q\odot P}}\Big[\frac{e^{A\_{Q}(s,T)+B\_{Q}(s,T)\cdot Y\_{s}}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =eAQ​(s,T)−a0​T′​EQ⊙P​[eBQ​(s,T)⋅Ysea⋅YT′​e−Λsm−Λss|ℱtZ].\displaystyle=e^{A\_{Q}(s,T)-a\_{0}T^{\prime}}E\_{\operatorname{Q\odot P}}\Big[\frac{e^{B\_{Q}(s,T)\cdot Y\_{s}}}{e^{a\cdot Y\_{T^{\prime}}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big]. |  |

With a view on Equation ([60](https://arxiv.org/html/2510.06698v1#S5.E60 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")), we can now apply Proposition [5.3](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"), however replacing a⋅Ysa\cdot Y\_{s} by BQ​(s,T)⋅YsB\_{Q}(s,T)\cdot Y\_{s}. This is captured by adjusting the coefficients accordingly, using the notation from ([63](https://arxiv.org/html/2510.06698v1#S5.E63 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−Λsm−Λss|ℱtZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] | =eAQ​(s,T)−a0​T+Φ​(t,s,s)+ψ​(t+1,s,T′,BQ​(s,T),a)⋅Zt.\displaystyle=e^{A\_{Q}(s,T)-a\_{0}T+\Phi(t,s,s)+\psi(t+1,s,T^{\prime},B\_{Q}(s,T),a)\cdot Z\_{t}}. |  |

On the other side, if T′≥sT^{\prime}\geq s,

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′|ℱsZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}|{\mathscr{F}}\_{s}^{Z}\Big] | =EQ⊙P​[e−a0​T′+AQ​(T′,T)+(BQ​(T′,T)−a)⋅YT′|ℱsZ]\displaystyle=E\_{\operatorname{Q\odot P}}\Big[e^{-a\_{0}T^{\prime}+A\_{Q}(T^{\prime},T)+(B\_{Q}(T^{\prime},T)-a)\cdot Y\_{T^{\prime}}}|{\mathscr{F}}\_{s}^{Z}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−a0​T′+AQ​(T′,T)⋅eAQ​(s,T′,0,(BQ​(T′,T)−a))+BQ​(s,T′,0,(BQ​(T′,T)−a))⋅Zs.\displaystyle=e^{-a\_{0}T^{\prime}+A\_{Q}(T^{\prime},T)}\cdot{e^{A\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))+B\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))\cdot Z\_{s}}}. |  |

Using Proposition [5.2](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[STST′​e−Λsm−Λss|ℱtZ]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\frac{S\_{T}}{S\_{T^{\prime}}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}^{Z}\_{t}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−a0​T′+AQ​(T′,T)+AQ​(s,T′,0,(BQ​(T′,T)−a))⋅EQ⊙P​[eBQ​(s,T′,0,(BQ​(T′,T)−a))⋅Zs​e−Λsm−Λss|ℱtZ]\displaystyle=e^{-a\_{0}T^{\prime}+A\_{Q}(T^{\prime},T)+A\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))}\cdot E\_{\operatorname{Q\odot P}}\Big[e^{B\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))\cdot Z\_{s}}e^{-\Lambda^{m}\_{s}-\Lambda^{s}\_{s}}|{\mathscr{F}}\_{t}^{Z}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−a0​T′+AQ​(T′,T)+AQ​(s,T′,0,(BQ​(T′,T)−a))\displaystyle=e^{-a\_{0}T^{\prime}+A\_{Q}(T^{\prime},T)+A\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅eΦ​(t,s,s,BQ​(s,T′,0,(BQ​(T′,T)−a)))+ψ​(t+1,s,BQ​(s,T′,0,(BQ​(T′,T)−a)))⋅Zt\displaystyle\quad\cdot e^{\Phi\big(t,s,s,B\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))\big)+\psi\big(t+1,s,B\_{Q}(s,T^{\prime},0,(B\_{Q}(T^{\prime},T)-a))\big)\cdot Z\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅e−Λtm−Λts\displaystyle\quad\cdot e^{-\Lambda\_{t}^{m}-\Lambda\_{t}^{s}} |  |

and the proof is finished.
∎

## 6. The valuation of the variable annuity

Coming back to the IFA-free valuation of a variable annuity, we now can utilize the obtained results on affine processes.

In the following, we utilise Φ\Phi, ψ\psi, Φ′\Phi^{\prime} and ψ′\psi^{\prime} as defined in Equations ([53](https://arxiv.org/html/2510.06698v1#S5.E53 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")), ([54](https://arxiv.org/html/2510.06698v1#S5.E54 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and ([59](https://arxiv.org/html/2510.06698v1#S5.E59 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")).
The special case of just computing the discounted value of future payments without reference to the stock price can be computed by letting a0=0a\_{0}=0 and a=0a=0. To emphasize this, we will write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ0​(t,u,T)\displaystyle\Phi^{0}(t,u,T) |  | (64) |

for the function Φ​(t,u,T)\Phi(t,u,T) obtained from ([53](https://arxiv.org/html/2510.06698v1#S5.E53 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")), ([54](https://arxiv.org/html/2510.06698v1#S5.E54 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and ([59](https://arxiv.org/html/2510.06698v1#S5.E59 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) with a=0a=0. We use a similar notation for the function ψ\psi. It will also be useful when we can modify the parameter aa. For this, we will use the notation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(t,u,T,a)\displaystyle\Phi(t,u,T,a) |  | (65) |

and, similarly for ψ\psi.
For clarity, we summarise the assumptions made until now in the following assumption.

###### Assumption 6.1.

We assume that

1. (i)

   The pricing measure P∗=Q⊙PP^{\*}=\operatorname{Q\mkern-2.0mu\odot\mkern-2.0muP} is the QP-measure
2. (ii)

   Z=(X,Y)Z=(X,Y) is the affine process which satisfies Equations ([45](https://arxiv.org/html/2510.06698v1#S5.E45 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and ([46](https://arxiv.org/html/2510.06698v1#S5.E46 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) with parameters α,β,γ\alpha,\beta,\gamma and AQ,BQA\_{Q},B\_{Q}, respectively.
3. (iii)

   The discounted stock price SS satisfies Equation ([44](https://arxiv.org/html/2510.06698v1#S5.E44 "In 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) with parameters a0,aa\_{0},a.
4. (iv)

   τm\tau^{m} and τS\tau^{S} are double stochastic random times with associated cumulated intensities Λm\Lambda^{m} and Λs\Lambda^{s} satisfying Equation ([50](https://arxiv.org/html/2510.06698v1#S5.E50 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) with parameters b0i,bi,cib\_{0}^{i},b^{i},c^{i} for i∈{m,s}i\in\{m,s\}, respectively.
5. (v)

   The functions ψ\psi, Φ′\Phi^{\prime} and ψ′\psi^{\prime} are defined in Equations ([53](https://arxiv.org/html/2510.06698v1#S5.E53 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and ([54](https://arxiv.org/html/2510.06698v1#S5.E54 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) where we also use the notation defined in Equation ([64](https://arxiv.org/html/2510.06698v1#S6.E64 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")) and Equation ([65](https://arxiv.org/html/2510.06698v1#S6.E65 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")).

Recall that the contract details of the variable annuity were introduced in Section [3.1](https://arxiv.org/html/2510.06698v1#S3.SS1 "3.1. Contract details ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting").

###### Proposition 6.1.

Assume that Assumption [6.1](https://arxiv.org/html/2510.06698v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting") holds. Then, the IFA-free price of the surrender benefit is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB0\displaystyle{\rm SB}\_{0} | =∑k=1nβ​(Tk)​p​(Tk)⋅∑i=1kπi​∑t=Tk−1+1Tkea0​(Tk−Ti)​(eΦ​(0,t−1,t)+ψ​(1,t−1,Ti)⋅Z0−eΦ​(0,t,t)+ψ​(1,t,Ti)⋅Z0).\displaystyle=\sum\_{k=1}^{n}\beta(T\_{k})p(T\_{k})\cdot\sum\_{i=1}^{k}\pi\_{i}\sum\_{t=T\_{k-1}+1}^{T\_{k}}e^{a\_{0}(T\_{k}-T\_{i})}\Big(e^{\Phi(0,t-1,t)+\psi(1,t-1,T\_{i})\cdot Z\_{0}}-e^{\Phi(0,t,t)+\psi(1,t,T\_{i})\cdot Z\_{0}}\Big). |  |

###### Proof.

By Proposition [3.1](https://arxiv.org/html/2510.06698v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting"), the surrender benefit is given by

|  |  |  |
| --- | --- | --- |
|  | SB0=∑k=1nβ​(Tk)​p​(Tk)​EQ⊙P​[𝟙{Tk−1<τs≤Tk}​𝟙{τs<τm}​FTkπ].{\rm SB}\_{0}=\sum\_{k=1}^{n}\beta(T\_{k})p(T\_{k})\,E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{T\_{k-1}<\tau^{s}\leq T\_{k}\}}{\mathds{1}}\_{\{\tau^{s}<\tau^{m}\}}F^{\pi}\_{T\_{k}}\Big]. |  |

The value of the fund FπF^{\pi} can be deduced from Equation ([10](https://arxiv.org/html/2510.06698v1#S3.E10 "In Remark 3.1 (On the underlying fund). ‣ 3.1. Contract details ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting")), such that
we have to compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[𝟙{Tk−1<τs≤Tk}​𝟙{τs<τm}​STkSTi]\displaystyle E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{T\_{k-1}<\tau^{s}\leq T\_{k}\}}{\mathds{1}}\_{\{\tau^{s}<\tau^{m}\}}\frac{S\_{T\_{k}}}{S\_{T\_{i}}}\Big] |  | (66) |

for all i∈{1,…,k}i\in\{1,\dots,k\}. We write short XTki:=STk/STiX^{i}\_{T\_{k}}:=\nicefrac{{S\_{T\_{k}}}}{{S\_{T\_{i}}}}.

As in Proposition [4.5](https://arxiv.org/html/2510.06698v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.2. Two stopping times ‣ 4. Progressive filtration enlargements ‣ Insurance products with guarantees in an affine setting") we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[𝟙{Tk−1<τs≤Tk}​𝟙{τs<τm}​XTki]\displaystyle E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{T\_{k-1}<\tau^{s}\leq T\_{k}\}}{\mathds{1}}\_{\{\tau^{s}<\tau^{m}\}}X^{i}\_{T\_{k}}\Big] | =∑t=Tk−1+1TkEQ⊙P​[𝟙{τs=t}​𝟙{t<τm}​XTki]\displaystyle=\sum\_{t=T\_{k-1}+1}^{T\_{k}}E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{\tau^{s}=t\}}{\mathds{1}}\_{\{t<\tau^{m}\}}X^{i}\_{T\_{k}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑t=Tk−1+1TkEQ⊙P​[EP​[𝟙{τs=t}​𝟙{t<τm}|ℱTKZ]​XTki]\displaystyle=\sum\_{t=T\_{k-1}+1}^{T\_{k}}E\_{\operatorname{Q\odot P}}\Big[E\_{P}\big[{\mathds{1}}\_{\{\tau^{s}=t\}}{\mathds{1}}\_{\{t<\tau^{m}\}}|{\mathscr{F}}^{Z}\_{T\_{K}}\big]X^{i}\_{T\_{k}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑t=Tk−1+1TkEQ⊙P​[EP​[𝟙{τs=t}​𝟙{t<τm}|ℱtZ]​XTki]\displaystyle=\sum\_{t=T\_{k-1}+1}^{T\_{k}}E\_{\operatorname{Q\odot P}}\Big[E\_{P}\big[{\mathds{1}}\_{\{\tau^{s}=t\}}{\mathds{1}}\_{\{t<\tau^{m}\}}|{\mathscr{F}}^{Z}\_{t}\big]X^{i}\_{T\_{k}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑t=Tk−1+1TkEQ⊙P​[Gt3,t​XTki].\displaystyle=\sum\_{t=T\_{k-1}+1}^{T\_{k}}E\_{\operatorname{Q\odot P}}\Big[G\_{t}^{3,t}\,X^{i}\_{T\_{k}}\Big]. |  |

By Equation ([5.2](https://arxiv.org/html/2510.06698v1#S5.Ex37 "5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")), we obtain that

|  |  |  |
| --- | --- | --- |
|  | Gt3,t=(e−Λt−1s−e−Λts)​e−Λtm.\displaystyle G^{3,t}\_{t}=\Big(e^{-\Lambda^{s}\_{t-1}}-e^{-\Lambda^{s}\_{t}}\Big)e^{-\Lambda^{m}\_{t}}. |  |

Hence, from Proposition [5.3](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[Gt3,t​XTki]\displaystyle E\_{\operatorname{Q\odot P}}[G^{3,t}\_{t}X^{i}\_{T\_{k}}] | =EQ​[STkSTi​(e−Λt−1s−e−Λts)​e−Λtm]\displaystyle=E\_{Q}\Big[\frac{S\_{T\_{k}}}{S\_{T\_{i}}}\Big(e^{-\Lambda^{s}\_{t-1}}-e^{-\Lambda^{s}\_{t}}\Big)e^{-\Lambda^{m}\_{t}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ea0​(Tk−Ti)​(eΦ​(0,t−1,t)+ψ​(1,t−1,Ti)⋅Z0−eΦ​(0,t,t)+ψ​(1,t,Ti)⋅Z0).∎\displaystyle=e^{a\_{0}(T\_{k}-T\_{i})}\Big(e^{\Phi(0,t-1,t)+\psi(1,t-1,T\_{i})\cdot Z\_{0}}-e^{\Phi(0,t,t)+\psi(1,t,T\_{i})\cdot Z\_{0}}\Big).\qed |  |

For the following it is important to notice that FπF^{\pi} is no longer affine, even if SS is. The computation of tractable formulas therefore becomes more complicated. If there is only a single investment, i.e. when n=1n=1, then the following result provides the associated valuation formulas. If the fund FπF^{\pi} can be well approximated by an affine process, the result also suffices of course. For the general case one needs to rely on more complicated Fourier decompositions, see for example Lemma 10.3 in Filipović ([2009](https://arxiv.org/html/2510.06698v1#bib.bib15)).

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | f~​(w,λ,A¯)=12​π​e(w+i​λ)​A¯​K−(w−1+i​λ)(w+i​λ)​(w−1+i​λ)\displaystyle\widetilde{f}(w,\lambda,\bar{A})=\frac{1}{2\pi}e^{(w+i\lambda)\bar{A}}\frac{K^{-(w-1+i\lambda)}}{(w+i\lambda)(w-1+i\lambda)} |  | (67) |

for any w>1w>1.

###### Proposition 6.2.

Assume that Assumption [6.1](https://arxiv.org/html/2510.06698v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting") holds and in addition that n=1n=1. Then, the IFA-free valuation of the GMAB is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | GMAB0\displaystyle{\rm GMAB}\_{0} | =PTπ⋅eΦ0​(0,T,T)+ψ0​(1,T)⋅Z0\displaystyle=P\_{T}^{\pi}\cdot e^{\Phi^{0}(0,T,T)+\psi^{0}(1,T)\cdot Z\_{0}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​π​∫eΦ​(0,T,T,(w+i​λ)​a)+ψ​(1,T,T1,(w+i​λ)​a)⋅Z0​f~​(w,λ,a0​(T−T1))​𝑑λ.\displaystyle+\frac{1}{2\pi}\int e^{\Phi(0,T,T,(w+i\lambda)a)+\psi(1,T,T\_{1},(w+i\lambda)a)\cdot Z\_{0}}\,\widetilde{f}(w,\lambda,a\_{0}(T-T\_{1}))d\lambda. |  |

###### Proof.

To begin with, we observe that for n=1n=1 and t≥T1,t\geq T\_{1},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ftπ=π1​StST1.\displaystyle F^{\pi}\_{t}=\pi\_{1}\frac{S\_{t}}{S\_{T\_{1}}}. |  | (68) |

Then, following Proposition [3.1](https://arxiv.org/html/2510.06698v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting"), with K=K′/π1K=\nicefrac{{K^{\prime}}}{{\pi\_{1}}},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ⊙P​[𝟙{τm>T,τs>T}​max⁡(FTπ,K′)]\displaystyle E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{\tau^{m}>T,\tau^{s}>T\}}\max(F\_{T}^{\pi},K^{\prime})\Big] | =K′​EQ⊙P​[e−ΛTm−ΛTs]+π1​EQ⊙P​[(STST1−K)+​e−ΛTm−ΛTs],\displaystyle=K^{\prime}E\_{\operatorname{Q\odot P}}\Big[e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big]+\pi\_{1}E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big], |  | (69) |

such that we have to value a call on ST/ST1\nicefrac{{S\_{T}}}{{S\_{T\_{1}}}} with strike KK. This can be done in affine models by relying on Fourier inversion, and we follow Chapter 10 in Filipović ([2009](https://arxiv.org/html/2510.06698v1#bib.bib15)). First, note that, using ([64](https://arxiv.org/html/2510.06698v1#S6.E64 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ⊙P​[e−ΛTm−ΛTs]\displaystyle E\_{\operatorname{Q\odot P}}\Big[e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big] | =eΦ0​(0,T,T)+ψ0​(1,T)⋅Z0.\displaystyle=e^{\Phi^{0}(0,T,T)+\psi^{0}(1,T)\cdot Z\_{0}}. |  | (70) |

In the following, we will condition on ℱT1Z{\mathscr{F}}^{Z}\_{T\_{1}} and use the affine property.
Next, observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | STST1\displaystyle\frac{S\_{T}}{S\_{T\_{1}}} | =ea0​(T−T1)+a⋅YT−a⋅YT1.\displaystyle=e^{a\_{0}(T-T\_{1})+a\cdot Y\_{T}-a\cdot Y\_{T\_{1}}}. |  |

To obtain an affine representation we stack the vector Z¯=(ZT,ZT1)\bar{Z}=(Z\_{T},Z\_{T\_{1}}) and denote the associated coefficients by

|  |  |  |  |
| --- | --- | --- | --- |
|  | B¯:=((0,a),(0,−a))\displaystyle\bar{B}:=\big((0,a),(0,-a)\big) |  | (71) |

together with A¯=a0​(T−T1)\bar{A}=a\_{0}(T-T\_{1})
such that

|  |  |  |
| --- | --- | --- |
|  | STST1=eA¯+B¯⋅Z¯.\displaystyle\frac{S\_{T}}{S\_{T\_{1}}}=e^{\bar{A}+\bar{B}\cdot\bar{Z}}. |  |

As in Corollary 10.4 in Filipović ([2009](https://arxiv.org/html/2510.06698v1#bib.bib15)) we have the integral representation

|  |  |  |
| --- | --- | --- |
|  | (eA¯+B¯⋅z−K)+=12​π​∫e(w+i​λ)​B¯⋅z​f~​(w,λ,A¯)​𝑑λ\Big(e^{\bar{A}+\bar{B}\cdot z}-K\Big)^{+}=\frac{1}{2\pi}\int e^{(w+i\lambda)\bar{B}\cdot z}\,\widetilde{f}(w,\lambda,\bar{A})d\lambda |  |

for some appropriate w>1w>1.
An application of Fubini’s theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[(STST1−K)+​e−ΛTm−ΛTs]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =EQ⊙P​[(eA¯+B¯⋅Z¯−K)+​e−ΛTm−ΛTs]\displaystyle=E\_{\operatorname{Q\odot P}}\Big[\Big(e^{\bar{A}+\bar{B}\cdot\bar{Z}}-K\Big)^{+}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​π​∫EQ⊙P​[e(w+i​λ)​B¯⋅Z¯​e−ΛTm−ΛTs]​f~​(w,λ,A¯)​𝑑λ.\displaystyle=\frac{1}{2\pi}\int E\_{\operatorname{Q\odot P}}\Big[e^{(w+i\lambda)\bar{B}\cdot\bar{Z}}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big]\,\widetilde{f}(w,\lambda,\bar{A})d\lambda. |  |

The inner expectation computes to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ⊙P​[e(w+i​λ)​B¯⋅Z¯​e−ΛTm−ΛTs]\displaystyle E\_{\operatorname{Q\odot P}}\Big[e^{(w+i\lambda)\bar{B}\cdot\bar{Z}}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\Big] | =EQ⊙P​[e(w+i​λ)​a⋅YTe(w+i​λ)​a⋅YT1​e−ΛTm−ΛTs].\displaystyle=E\_{\operatorname{Q\odot P}}\bigg[\frac{e^{(w+i\lambda)a\cdot Y\_{T}}}{e^{(w+i\lambda)a\cdot Y\_{T\_{1}}}}e^{-\Lambda^{m}\_{T}-\Lambda^{s}\_{T}}\bigg]. |  | (72) |

This can be computed using the first expression in Proposition [5.3](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting") by choosing a0=0a\_{0}=0 and letting aa be equal to (w+i​λ)​a(w+i\lambda)a. Using the notation defined in Equation ([65](https://arxiv.org/html/2510.06698v1#S6.E65 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")), we obtain that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ([72](https://arxiv.org/html/2510.06698v1#S6.E72 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")) | =exp⁡(Φ​(0,T,T,(w+i​λ)​a)+ψ​(1,T,T1,(w+i​λ)​a)⋅Z0)\displaystyle=\exp\Big(\Phi(0,T,T,(w+i\lambda)a)+\psi(1,T,T\_{1},(w+i\lambda)a)\cdot Z\_{0}\Big) |  | (73) |

and the claim follows.
∎

The death benefit is more complicated and we introduce the following notation. Denote

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | DB1​(t)\displaystyle{\rm DB}^{1}(t) | =PT1π​(e−Λt−1m−e−Λtm)​e−Λts.\displaystyle=P\_{T\_{1}}^{\pi}\Big(e^{-\Lambda^{m}\_{t-1}}-e^{-\Lambda^{m}\_{t}}\Big)e^{-\Lambda\_{t}^{s}}. |  | (74) |

Recall the notation for AQA\_{Q} and BQB\_{Q} in Equation ([61](https://arxiv.org/html/2510.06698v1#S5.E61 "In 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) and let for t≥T1t\geq T\_{1}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | DB2​(t)\displaystyle{\rm DB}^{2}(t) | =eAQ​(t,T,0,(w+i​λ)​a)+Φ​(0,t,t,0,(w+i​λ)​a)+ψ​(1,t,T1,BQ​(t,T,(w+i​λ)​a),(w+i​λ)​a)⋅Z0\displaystyle=e^{A\_{Q}(t,T,0,(w+i\lambda)a)+\Phi(0,t,t,0,(w+i\lambda)a)+\psi(1,t,T\_{1},B\_{Q}(t,T,(w+i\lambda)a),(w+i\lambda)a)\cdot Z\_{0}} |  | (75) |

while for t<T1t<T\_{1},

|  |  |  |  |
| --- | --- | --- | --- |
|  | DB2​(t)\displaystyle{\rm DB}^{2}(t) | =eAQ​(T′,T,0,(w+i​λ)​a)+AQ​(t,T1,0,(BQ​(T1,T,(w+i​λ)​a)−(w+i​λ)​a))\displaystyle=e^{A\_{Q}(T^{\prime},T,0,(w+i\lambda)a)+A\_{Q}(t,T\_{1},0,(B\_{Q}(T\_{1},T,(w+i\lambda)a)-(w+i\lambda)a))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅eΦ​(0,t,t,BQ​(t,T1,(BQ​(T1,T,0,(w+i​λ)​a)−(w+i​λ)​a)))\displaystyle\quad\cdot e^{\Phi\big(0,t,t,B\_{Q}(t,T\_{1},(B\_{Q}(T\_{1},T,0,(w+i\lambda)a)-(w+i\lambda)a))\big)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⋅eψ​(1,t,BQ​(t,T1,(w+i​λ)​a,(BQ​(T1,T,(w+i​λ)​a)−(w+i​λ)​a)))⋅Z0.\displaystyle\quad\cdot e^{\psi\big(1,t,B\_{Q}(t,T\_{1},(w+i\lambda)a,(B\_{Q}(T\_{1},T,(w+i\lambda)a)-(w+i\lambda)a))\big)\cdot Z\_{0}}. |  | (76) |

###### Proposition 6.3.

Assume that Assumption [6.1](https://arxiv.org/html/2510.06698v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting") holds and in addition that n=1n=1. Then, the IFA-free valuation of the death benefit is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DB0\displaystyle{\rm DB}\_{0} | =β​(T1)⋅∑t=1TkDB1​(t)+β​(T1)⋅π1​∑t=1T1DB2​(t).\displaystyle=\beta(T\_{1})\cdot\sum\_{t=1}^{T\_{k}}{\rm DB}^{1}(t)+\beta(T\_{1})\cdot\pi\_{1}\sum\_{t=1}^{T\_{1}}{\rm DB}^{2}(t). |  |

###### Proof.

According to Proposition [3.1](https://arxiv.org/html/2510.06698v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.3. The valuation rule ‣ 3. IFA-free valuation of insurance products with guarantees ‣ Insurance products with guarantees in an affine setting"), with n=1n=1,

|  |  |  |
| --- | --- | --- |
|  | DB0=β​(T1)​EQ⊙P​[𝟙{τm∈(0,T1]}​𝟙{τs>τm}​max⁡(FT1π,KT1π)].\displaystyle{\rm DB}\_{0}=\beta(T\_{1})E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{\tau^{m}\in(0,T\_{1}]\}}{\mathds{1}}\_{\{\tau^{s}>\tau^{m}\}}\max(F\_{T\_{1}}^{\pi},K\_{T\_{1}}^{\pi})\Big]. |  |

We note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[𝟙{τm≤T1}​𝟙{τs>τm}​max⁡(FT1π,KT1π)]\displaystyle E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{\tau^{m}\leq T\_{1}\}}{\mathds{1}}\_{\{\tau^{s}>\tau^{m}\}}\max(F\_{T\_{1}}^{\pi},K\_{T\_{1}}^{\pi})\Big] | =∑t=1T1EQ⊙P​[𝟙{τm=t}​𝟙{τs>t}​max⁡(FT1π,KT1π)]\displaystyle=\sum\_{t=1}^{T\_{1}}E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{\tau^{m}=t\}}{\mathds{1}}\_{\{\tau^{s}>t\}}\max(F\_{T\_{1}}^{\pi},K\_{T\_{1}}^{\pi})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑t=1T1EQ⊙P​[𝟙{τm=t}​𝟙{τs>t​s}​max⁡(FT1π,KT1π)]\displaystyle=\sum\_{t=1}^{T\_{1}}E\_{\operatorname{Q\odot P}}\Big[{\mathds{1}}\_{\{\tau^{m}=t\}}{\mathds{1}}\_{\{\tau^{s}>ts\}}\max(F\_{T\_{1}}^{\pi},K\_{T\_{1}}^{\pi})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑t=1T1EQ⊙P​[Gt3,t​max⁡(FT1π,TT1π)]\displaystyle=\sum\_{t=1}^{T\_{1}}E\_{\operatorname{Q\odot P}}\Big[G\_{t}^{3,t}\max(F\_{T\_{1}}^{\pi},T\_{T\_{1}}^{\pi})\Big] |  |

We therefore focus on

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[Gt3,t​max⁡(FT1π,K′)]\displaystyle E\_{\operatorname{Q\odot P}}\Big[G\_{t}^{3,t}\max(F\_{T\_{1}}^{\pi},K^{\prime})\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K′​EQ⊙P​[Gt3,t]+π1​EQ⊙P​[(STST1−K)+​Gt3,t].\displaystyle=K^{\prime}E\_{\operatorname{Q\odot P}}\Big[G\_{t}^{3,t}\Big]+\pi\_{1}\,E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}G\_{t}^{3,t}\Big]. |  |

Recall from Equation ([5.2](https://arxiv.org/html/2510.06698v1#S5.Ex37 "5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt3,t\displaystyle G\_{t}^{3,t} | =(e−Λt−1m−e−Λtm)​e−Λts\displaystyle=\Big(e^{-\Lambda^{m}\_{t-1}}-e^{-\Lambda^{m}\_{t}}\Big)e^{-\Lambda\_{t}^{s}} |  |

Proceeding as for Equation ([70](https://arxiv.org/html/2510.06698v1#S6.E70 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[Gt3,t]\displaystyle E\_{\operatorname{Q\odot P}}\Big[G\_{t}^{3,t}\Big] | =(eΦ0​(0,t−1,t)+ψ0​(1,t−1)⋅Z0−eΦ0​(0,t,t)+ψ0​(1,t)⋅Z0).\displaystyle=\Big(e^{\Phi^{0}(0,t-1,t)+\psi^{0}(1,t-1)\cdot Z\_{0}}-e^{\Phi^{0}(0,t,t)+\psi^{0}(1,t)\cdot Z\_{0}}\Big). |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[(STST1−K)+​Gt3,t]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}G\_{t}^{3,t}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =EQ⊙P​[(STST1−K)+​e−Λt−1m−Λts]−EQ⊙P​[(STST1−K)+​e−Λtm−Λts].\displaystyle=E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}e^{-\Lambda^{m}\_{t-1}-\Lambda\_{t}^{s}}\Big]-E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}e^{-\Lambda^{m}\_{t}-\Lambda\_{t}^{s}}\Big]. |  |

Now we obtain, as in the proof of Proposition [6.2](https://arxiv.org/html/2510.06698v1#S6.Thmtheorem2 "Proposition 6.2. ‣ 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ⊙P​[(STST1−K)+​e−Λtm−Λts]\displaystyle E\_{\operatorname{Q\odot P}}\Big[\Big(\frac{S\_{T}}{S\_{T\_{1}}}-K\Big)^{+}e^{-\Lambda^{m}\_{t}-\Lambda^{s}\_{t}}\Big] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =EQ⊙P​[(eA¯+B¯⋅Z¯−K)+​e−Λtm−Λts]\displaystyle=E\_{\operatorname{Q\odot P}}\Big[\Big(e^{\bar{A}+\bar{B}\cdot\bar{Z}}-K\Big)^{+}e^{-\Lambda^{m}\_{t}-\Lambda^{s}\_{t}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​π​∫EQ⊙P​[e(w+i​λ)​B¯⋅Z¯​e−Λtm−Λts]​f~​(w,λ,A¯)​𝑑λ.\displaystyle=\frac{1}{2\pi}\int E\_{\operatorname{Q\odot P}}\Big[e^{(w+i\lambda)\bar{B}\cdot\bar{Z}}e^{-\Lambda^{m}\_{t}-\Lambda^{s}\_{t}}\Big]\,\widetilde{f}(w,\lambda,\bar{A})d\lambda. |  |

The inner expectation computes to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ⊙P​[e(w+i​λ)​B¯⋅Z¯​e−Λtm−Λts]\displaystyle E\_{\operatorname{Q\odot P}}\Big[e^{(w+i\lambda)\bar{B}\cdot\bar{Z}}e^{-\Lambda^{m}\_{t}-\Lambda^{s}\_{t}}\Big] | =EQ⊙P​[e(w+i​λ)​a⋅YTe(w+i​λ)​a⋅YT1​e−Λtm−Λts].\displaystyle=E\_{\operatorname{Q\odot P}}\bigg[\frac{e^{(w+i\lambda)a\cdot Y\_{T}}}{e^{(w+i\lambda)a\cdot Y\_{T\_{1}}}}e^{-\Lambda^{m}\_{t}-\Lambda^{s}\_{t}}\bigg]. |  | (77) |

For this, we can proceed exactly as in Proposition [5.5](https://arxiv.org/html/2510.06698v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5.2. Survival and surrender ‣ 5. An affine framework ‣ Insurance products with guarantees in an affine setting"), however replacing aa by (w+i​λ)​a(w+i\lambda)a.
This gives us, when t≥T1t\geq T\_{1},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ([77](https://arxiv.org/html/2510.06698v1#S6.E77 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting")) | =eAQ​(t,T,0,(w+i​λ)​a)+Φ​(0,t,t,0,(w+i​λ)​a)+ψ​(1,t,T1,BQ​(t,T,(w+i​λ)​a),(w+i​λ)​a)⋅Z0.\displaystyle=e^{A\_{Q}(t,T,0,(w+i\lambda)a)+\Phi(0,t,t,0,(w+i\lambda)a)+\psi(1,t,T\_{1},B\_{Q}(t,T,(w+i\lambda)a),(w+i\lambda)a)\cdot Z\_{0}}. |  |

On the other side, for t<T1t<T\_{1}, we obtain that

|  |  |  |
| --- | --- | --- |
|  | ([77](https://arxiv.org/html/2510.06698v1#S6.E77 "In 6. The valuation of the variable annuity ‣ Insurance products with guarantees in an affine setting"))=eAQ​(T1,T,0,(w+i​λ)​a)+AQ​(t,T1,0,(BQ​(T1,T,(w+i​λ)​a)−(w+i​λ)​a))\displaystyle\eqref{temp 1295}=e^{A\_{Q}(T\_{1},T,0,(w+i\lambda)a)+A\_{Q}(t,T\_{1},0,(B\_{Q}(T\_{1},T,(w+i\lambda)a)-(w+i\lambda)a))} |  |
|  |  |  |
| --- | --- | --- |
|  | ⋅eΦ​(0,t,t,BQ​(t,T1,(BQ​(T1,T,0,(w+i​λ)​a)−(w+i​λ)​a)))+ψ​(1,t,BQ​(t,T1,(w+i​λ)​a,(BQ​(T1,T,(w+i​λ)​a)−(w+i​λ)​a)))⋅Z0\displaystyle\cdot e^{\Phi\big(0,t,t,B\_{Q}(t,T\_{1},(B\_{Q}(T\_{1},T,0,(w+i\lambda)a)-(w+i\lambda)a))\big)+\psi\big(1,t,B\_{Q}(t,T\_{1},(w+i\lambda)a,(B\_{Q}(T\_{1},T,(w+i\lambda)a)-(w+i\lambda)a))\big)\cdot Z\_{0}} |  |

and the proof is finished.
∎

## 7. Conclusion

Summarising, this paper shows that in a highly flexible affine framework, a very general class of insurance policies, including variable annuities with guarantees, can be valued in a tractable and insurance-finance arbitrage-free way. The formulas are more involved, if the payoffs become more complicated, as is the case for example for the death benefit - where in particular interactions between survival and surrender times need to be handled.

## References

* (1)
* Aksamit and Jeanblanc (2017)

  Aksamit, A. and Jeanblanc, M. (2017), Enlargements of Filtration with Finance in view, Springer Briefs in
  Quantitative Finance, Springer.
* Artzner et al. (2024)

  Artzner, P., Eisele, K.-T. and Schmidt, T. (2024), ‘Insurance - finance arbitrage’, Mathematical
  Finance pp. 1–35.
* Ballotta et al. (2019)

  Ballotta, L., Eberlein, E., Schmidt, T. and Zeineddine, R.
  (2019), ‘Variable annuities in a
  Lévy-based hybrid model with surrender risk’, Quantitative Finance
  20(5), 867 – 886.
* Barigou et al. (2023)

  Barigou, K., Linders, D. and Yang, F. (2023), ‘Actuarial-consistency and two-step actuarial
  valuations: a new paradigm to insurance valuation’, Scandinavian
  Actuarial Journal 2023(2), 191–217.
* Bernard et al. (2017)

  Bernard, C., Cui, Z. and Vanduffel, S. (2017), ‘Impact of flexible periodic premiums on variable
  annuity guarantees’, North American actuarial journal 21(1), 63–86.
* Bielecki and Rutkowski (2002)

  Bielecki, T. and Rutkowski, M. (2002), Credit Risk: Modeling, Valuation and Hedging, Springer Verlag. Berlin
  Heidelberg New York.
* Brémaud (1981)

  Brémaud, P. (1981), Point Processes
  and Queues, Springer Verlag. Berlin Heidelberg New York.
* Chen et al. (2019)

  Chen, A., Hieber, P. and Klein, J. K. (2019), ‘Tonuity: A novel individual-oriented retirement
  plan’, ASTIN Bulletin: The Journal of the IAA 49(1), 5–30.
* Chen et al. (2020)

  Chen, A., Rach, M. and Sehner, T. (2020), ‘On the optimal combination of annuities and
  tontines’, ASTIN Bulletin: The Journal of the IAA 50(1), 95–129.
* Deelstra et al. (2020)

  Deelstra, G., Devolder, P., Gnameho, K. and Hieber, P.
  (2020), ‘Valuation of hybrid financial and
  actuarial products in life insurance by a novel three-step method’, ASTIN Bulletin 50(3), 709–742.
* Dhaene et al. (2013)

  Dhaene, J., Kukush, A., Luciano, E., Schoutens, W. and Stassen, B.
  (2013), ‘A note on the (in-)dependence
  between financial and actuarial risks’, Insurance: Mathematics and
  Economics 52, 522–531.
* Dhaene et al. (2017)

  Dhaene, J., Stassen, B., Barigou, K., Linders, D. and Chen, Z.
  (2017), ‘Fair valuation of insurance
  liabilities: Merging actuarial judgement and market-consistency’, Insurance: Mathematics and Economics 76, 14–27.
* Errais et al. (2010)

  Errais, E., Giesecke, K. and Goldberg, L. R. (2010), ‘Affine point processes and portfolio credit risk’,
  SIAM Journal on Financial Mathematics 1, 642–665.
* Filipović (2009)

  Filipović, D. (2009), Term Structure
  Models: A Graduate Course, Springer Verlag. Berlin Heidelberg New York.
* Föllmer and Schied (2011)

  Föllmer, H. and Schied, A. (2011),
  Stochastic Finance, Walter de Gruyter, Berlin.
* Gehmlich and Schmidt (2018)

  Gehmlich, F. and Schmidt, T. (2018),
  ‘Dynamic defaultable term structure modelling beyond the intensity paradigm’,
  Mathematical Finance 28(1), 211–239.
* Hainaut and Devineau (2025)

  Hainaut, D. and Devineau, L. (2025),
  ‘Participating life insurances in an equity-libor market model’, European Actuarial Journal pp. 1–35.
* Kallsen and Muhle-Karbe (2010)

  Kallsen, J. and Muhle-Karbe, J. (2010), ‘Exponentially affine martingales, affine measure
  changes and exponential moments of affine processes’, Stochastic
  Processes and their Applications 120(2), 163–181.
* Keller-Ressel et al. (2019)

  Keller-Ressel, M., Schmidt, T. and Wardenga, R.
  (2019), ‘Affine processes beyond stochastic
  continuity’, Annals of Applied Probability 29, 3387 – 3437.
* Linders (2023)

  Linders, D. (2023), ‘The 3-step hedge-based
  valuation: fair valuation in the presence of systematic risks’, ASTIN
  Bulletin 53(2), 418–442.
* Malamud et al. (2008)

  Malamud, S., Trubowitz, E. and Wüthrich, M. V. (2008), ‘Market consistent pricing of insurance products’,
  ASTIN Bulletin 38(2), 483–526.
* Milevsky and Salisbury (2015)

  Milevsky, M. A. and Salisbury, T. S. (2015), ‘Optimal retirement income tontines’, Insurance:
  Mathematics and economics 64, 91–105.
* Oberpriller et al. (2024)

  Oberpriller, K., Ritter, M. and Schmidt, T. (2024), ‘Robust asymptotic insurance-finance arbitrage’, European Actuarial Journal pp. 1–35.
* Pelsser and Stadje (2014)

  Pelsser, A. and Stadje, M. (2014),
  ‘Time-consistent and market-consistent evaluations’, Mathematical
  Finance 24(1), 25–65.
* Platen et al. (2025)

  Platen, E., Schmidt, T. and Schmutz, M. (2025), ‘Benchmark-neutral risk-minimization for insurance
  products and nonreplicable claims’, arXiv .
* Winter and Planchet (2022)

  Winter, P. and Planchet, F. (2022),
  ‘Modern tontines as a pension solution: A practical overview’, European
  Actuarial Journal 12(1), 3–32.