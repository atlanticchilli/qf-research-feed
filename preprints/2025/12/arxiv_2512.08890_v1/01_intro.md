---
authors:
- Krzysztof Burnecki
- Marek Teuerle
- Martyna Zdeb
doc_id: arxiv:2512.08890v1
family_id: arxiv:2512.08890
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Modelling and valuation of catastrophe bonds across multiple regions
url_abs: http://arxiv.org/abs/2512.08890v1
url_html: https://arxiv.org/html/2512.08890v1
venue: arXiv q-fin
version: 1
year: 2025
---


Krzysztof Burnecki

Marek Teuerle

Martyna Zdeb

###### Abstract

The insurance-linked securities (ILS) market, as a form of alternative risk transfer, has been at the forefront of innovative risk-transfer solutions. The catastrophe bond (CAT bond) market now represents almost
half of the entire ILS market and is growing steadily. Since CAT bonds are often tied to risks in different regions, we follow this idea by constructing different pricing models that incorporate various scenarios of dependence between catastrophe losses in different areas. Namely, we consider independent, proportional, and arbitrary two-dimensional distribution cases. We also derive a normal approximation of the prices. Finally, to include the market price of risk, we apply Wang’s transform. We illustrate the differences between the scenarios and the performance of the approximation on the Property Claim Services data.

###### keywords:

Multi-region catastrophe bond , Gaussian copula , Monte Carlo simulations , Wang transform

††journal: arXiv

\affiliation

[inst1]organization=Faculty of Pure and Applied Mathematics, Hugo Steinhaus Center, Wrocław University of Science and Technology,addressline=Wyspianskiego 27,
city=50-370 Wrocław,
country=Poland

## 1 Introduction

Floods, earthquakes, and severe storms are major threats to society. In addition to loss of life and bodily injury, natural catastrophes can inflict damage to property, reducing both wealth and productive capacity, potentially resulting in significant financial losses on both macro- and micro-levels. The total cost typically reflects both the severity of the initial damage and the speed with which reconstruction can be completed. This is why insurance can play a protective role [Swissres].

Insured losses from global natural catastrophes reached USD 137 billion in 2024, driven primarily by Hurricanes Helene and Milton and severe convective storms. Secondary perils were the largest contributor to these losses, and significant fires, such as those in Los Angeles in early 2025, suggest that this trend of high secondary peril losses may continue. Looking ahead, if the typical 5-7% annual increase persists, insured losses could reach USD 145 billion in 2025. Although secondary risks have recently represented a larger part of yearly insured losses, primary risks still represent the greatest potential for catastrophic loss. Historically, a single major primary event, such as a hurricane hitting a densely populated urban centre, could result in losses that far exceed the current trend [Swissreport2025].

Developed in the 1990s, catastrophe bonds (CAT bonds) are a financial tool that allows insurance companies to offload natural disaster risks onto capital markets. They were created as an innovative answer to the growing number and intensity of major events such as hurricanes, earthquakes, and floods, which had significantly stressed insurers and reinsurers financially. For investors, these bonds offer a way to diversify their holdings while simultaneously providing insurers with protection against massive, potentially devastating losses [Barrieu2010, Barrieu2025].

The structure commonly involves a Special Purpose Vehicle (SPV), which issues the bonds to investors and simultaneously enters into a reinsurance agreement with the sponsor. The premium paid by the sponsor to the SPV funds the coupon payments made to the bondholders. Payouts to the sponsor (and corresponding losses of principal for investors) are contingent upon the occurrence of a predefined catastrophic event exceeding a certain severity threshold (usually three years), determined by specific trigger mechanisms. These triggers can be based on the sponsor’s actual losses (indemnity), objective physical parameters of the event (parametric), industry-wide losses (industry loss), or losses estimated by a third-party model (modelled loss) [BraunKousky2021].

CAT bonds function as a type of Alternative Risk Transfer, offering advantages not just to insurers but also to governments and businesses highly exposed to natural disasters. Occasionally, national entities have issued these bonds to secure funds for post-disaster relief and recovery. As such, CAT bonds are a crucial instrument for enhancing resilience in areas susceptible to natural catastrophes, helping to stabilise local economies after such events. In addition, pioneering risk transfer methods, such as CAT bonds, can help address existing protection gaps and improve individual and community resilience [burnecki2023catastrophe].

For the second year in a row, more than 90 catastrophe bond and related insurance-linked transactions were placed in 2024, with the 93 coming close to the 95 deals of last year. In terms of 144A property cat bond issuance, 2024 has set a new record of USD 16.6 billion, up 11% on the previous high of 2023. The total 144A cat bond issuance, which includes 144A cat bonds Covering other lines of re/insurance business such as cyber and terrorism, also hit a new high of USD 17.2 billion [artemisreport2025].

Much of the research focused on modelling natural catastrophes and pricing related risk securitization solutions addresses the issue of arbitrage-free valuation and market completeness. The field evolved from using simple early models to more complex approaches incorporating stochastic interest rates and contingent claims [taylor, burkuktay11, Brenda2010, mm, NowakRomaniuk2013, NowakRomaniuk2018, vaugirard2004canonical, braun]. Currently, there is increased interest in pricing advanced instruments like catastrophe options, futures, contingent convertible CAT bonds, and risk swaps [braun, burgiupal2019, Arnone2021Catastrophic].

We also note that to address the pricing challenges in insurance and finance, particularly for non-hedgeable risks, various risk measures and premium calculation principles have been developed. One important class is distortion risk measures explored by Wang [Wang1995, Wang1996a]. These measures calculate an insurance premium or risk capital by transforming, or distorting, the probability distribution of the underlying loss variable [Wang2002].

In practice, the issuance of a catastrophe bond typically involves a specialized modeling firm to quantify the catastrophe risk. These risk modelers estimate the probability of first loss (PFL) and provide an expected loss (EL) estimate for investors. Several studies have examined the relationship between price spreads and EL and other explanatory variables in the regression framework, see, e.g. [braun2, LaneBeckwith2021]. Additional work includes studies on implied Poisson intensities from observed prices [BEER2022106350], the use of machine learning techniques [Lane2018, GotGurWit2020], the application of mean utility functionals for CAT bond pricing [petra2021], and the use of extreme value theory for pricing earthquake-related catastrophe bonds [zimbidis2007modeling].

Historically, CAT bonds were designed with a single trigger event that, if it occurs and meets specified criteria, can lead to a payout to the issuer and potential loss of principal for investors. However, the use of multiple triggers is gaining importance. CAT bonds are frequently structured into several tranches. These tranches are differentiated by their risk-return profiles. The variation between tranches can be based on several factors, including the specific trigger event, the reference peril (the type of natural catastrophe Covered), and the defined Covered territory or geographic area. This allows different tranches to cater to investors with varying risk appetites. Existing literature has highlighted the issue of multi-peril ILS sometimes related to different regions. See, for instance, the pioneering work by Lane [lane2004] explored ”arbitrage-equivalent” pricing for Covers that could be either bought or sold or [haslip2010pricing], a study divided Italy into three seismic zones and priced three CAT bonds with different default risk levels, and also [Shao2015] for an empirical study of
California earthquake data within the multi-peril risk model. In [Burnecki2024Pricing] the authors introduced a model for multi-peril CAT bonds where a trigger can be activated if losses from at least one Covered peril exceed a set threshold.

Reflecting the multi-regional nature of CAT bond risks, in this paper, we introduce pricing models which are designed to incorporate diverse scenarios regarding the dependence of catastrophe losses across different geographic areas.

## 2 Three approaches for modelling dependence in different regions

In this section we introduce three approaches to modelling natural catastrophe losses in two regions. The methodology can be extended to more than two regions. The first assumes full independence between the aggregate loss processes in both regions. In the second case, we assume that the loss amounts of common catastrophes split between between the two regions with a fixed (deterministic) proportion. Other catastrophes that hit separately the two regions are modelled with independent aggregate loss processes. The third approach assumes that the proportion for common catastrophes varies randomly from loss to loss.

### 2.1 Model 1. Independent loss processes

We want to model losses caused by a selected peril in two regions. The simplest idea is to model them as two independent aggregate loss processes (Si​(t),t>0),i=1,2(S\_{i}(t),t>0),i=1,2, each corresponding to one of the regions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {S1​(t)=∑i=1N(1)​(t)Xi,S2​(t)=∑i=1N(2)​(t)Yi,\displaystyle\displaystyle\left\{\begin{array}[]{ll}S\_{1}(t)&=\sum\limits\_{i=1}^{N^{(1)}(t)}X\_{i},\\ \\ S\_{2}(t)&=\sum\limits\_{i=1}^{N^{(2)}(t)}Y\_{i},\end{array}\right. |  | (4) |

where N(1)​(t)\displaystyle N^{(1)}(t) and N(2)​(t)\displaystyle N^{(2)}(t) are counting processes, independent of each other, and {Xi,i∈ℕ}\displaystyle\{X\_{i},i\in\mathbb{N}\} and {Yi,i∈ℕ}\displaystyle\{Y\_{i},i\in\mathbb{N}\} are independent identically distributed (i.i.d.) positive random variables describing the losses in each region.
We also assume that {Xi,i∈ℕ}\displaystyle\{X\_{i},i\in\mathbb{N}\} and {Yi,i∈ℕ}\displaystyle\{Y\_{i},i\in\mathbb{N}\} are independent.

### 2.2 Model 2. Losses split proportionally with a fixed proportion

For the second approach, we assume that when a catastrophe hits both of the considered regions, the losses are split with constant proportion p\displaystyle p, 0<p<1\displaystyle 0<p<1. The first region is affected by the part p\displaystyle p of the loss and the part 1−p\displaystyle 1-p affects the second region. The model can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {S1​(t)=∑i=1N(1)​(t)Xi+p​∑i=1N(2)​(t)Zi,S2​(t)=∑i=1N(3)​(t)Yi+(1−p)​∑i=1N(2)​(t)Zi.\displaystyle\displaystyle\left\{\begin{array}[]{ll}S\_{1}(t)&=\sum\limits\_{i=1}^{N^{(1)}(t)}X\_{i}+p\sum\limits\_{i=1}^{N^{(2)}(t)}Z\_{i},\\ \\ S\_{2}(t)&=\sum\limits\_{i=1}^{N^{(3)}(t)}Y\_{i}+(1-p)\sum\limits\_{i=1}^{N^{(2)}(t)}Z\_{i}.\end{array}\right. |  | (8) |

The processes N(1)​(t)\displaystyle N^{(1)}(t) and N(3)​(t)\displaystyle N^{(3)}(t) count losses that occurred only in one of the regions, and the i.i.d. variables {Xi,i∈ℕ}\displaystyle\{X\_{i},i\in\mathbb{N}\} and {Yi,i∈ℕ}\displaystyle\{Y\_{i},i\in\mathbb{N}\} describe the losses in the first and second regions, respectively. The process N(2)​(t)\displaystyle N^{(2)}(t) describes the flow of losses that appear in both regions. The variables {Zi,i∈ℕ}\displaystyle\{Z\_{i},i\in\mathbb{N}\} represent the corresponding losses and are divided in proportion p\displaystyle p between two regions. We assume that all counting processes and all loss amount random variables are mutually independent.

### 2.3 Model 3. Dependent losses

Instead of splitting common losses with a fixed proportion, we can model them as correlated random variables with a given correlation coefficient. In that case, the two-dimensional aggregate loss process that describes the losses in the considered regions can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {S1​(t)=∑i=1N(1)​(t)Xi(1)+∑i=1N(2)​(t)Xi(2),S2​(t)=∑i=1N(3)​(t)Yi(1)+∑i=1N(2)​(t)Yi(2).\displaystyle\displaystyle\left\{\begin{array}[]{ll}S\_{1}(t)&=\sum\limits\_{i=1}^{N^{(1)}(t)}X\_{i}^{(1)}+\sum\limits\_{i=1}^{N^{(2)}(t)}X\_{i}^{(2)},\\ \\ S\_{2}(t)&=\sum\limits\_{i=1}^{N^{(3)}(t)}Y\_{i}^{(1)}+\sum\limits\_{i=1}^{N^{(2)}(t)}Y\_{i}^{(2)}.\end{array}\right. |  | (12) |

The part describing losses only in one of the regions is the same as in Model 2, namely the processes N(1)​(t)\displaystyle N^{(1)}(t) and N(3)​(t)\displaystyle N^{(3)}(t) count losses that occurred only in one of the regions, and i.i.d. variables {Xi(1),i∈ℕ}\displaystyle\{X\_{i}^{(1)},i\in\mathbb{N}\} and {Yi(1),i∈ℕ}\displaystyle\{Y\_{i}^{(1)},i\in\mathbb{N}\} model the sizes of these losses. The process N(2)​(t)\displaystyle N^{(2)}(t) counts losses that occur in both regions at the same time and variables {Xi(2),i∈ℕ}\displaystyle\{X\_{i}^{(2)},i\in\mathbb{N}\} and {Yi(2),i∈ℕ}\displaystyle\{Y\_{i}^{(2)},i\in\mathbb{N}\} model their sizes. We assume that they are, in general, dependent and we know their correlation coefficient.

We assume that all counting processes N(i),i=1,2,3\displaystyle N^{(i)},i=1,2,3 are independent of loss amount random variables and that the losses that occured only in one region are independent of the losses from catastrophes that hit both regions.

## 3 Pricing of a zero-coupon CAT bond under a physical measure

Let 𝐒={S1​(t),S2​(t)}\displaystyle\mathbf{S}=\{S\_{1}(t),S\_{2}(t)\} be a two-dimensional process describing losses caused by a chosen peril in two regions.
A zero-coupon (ZC) CAT bond with the maturity time T\displaystyle T will be triggered if the aggregate losses of at least one of the regions exceed corresponding threshold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(T)={1,if​(S1​(T)<D1∧S2​(T)<D2),c,if​(S1​(T)≥D1∨S2​(T)≥D2),\displaystyle\displaystyle P(T)=\left\{\begin{array}[]{ll}1,&\mathrm{if}\left(S\_{1}(T)<D\_{1}\land S\_{2}(T)<D\_{2}\right),\\ c,&\mathrm{if}\left(S\_{1}(T)\geq D\_{1}\lor S\_{2}(T)\geq D\_{2}\right),\end{array}\right. |  | (15) |

where 0≤c≤1\displaystyle 0\leq c\leq 1 is a recovery rate and Di\displaystyle D\_{i} (i=1,2\displaystyle i=1,2) denotes the threshold for the respective region.

The price of a ZC CAT bond with maturity time T\displaystyle T and face value 1\displaystyle 1, with payoff function defined in equation ([15](https://arxiv.org/html/2512.08890v1#S3.E15 "In 3 Pricing of a zero-coupon CAT bond under a physical measure ‣ Modelling and valuation of catastrophe bonds across multiple regions")) can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V0\displaystyle\displaystyle V\_{0} | =e−r​T​Eℙ​[P​(T)]=\displaystyle\displaystyle=e^{-rT}\mathrm{E}\_{\mathbb{P}}\left[P(T)\right]= |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−r​T[P(S1(T)<D1∧S2(T)<D2)\displaystyle\displaystyle=e^{-rT}\left[\mathrm{P}\left(S\_{1}(T)<D\_{1}\land S\_{2}(T)<D\_{2}\right)\right. |  | (16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +cP(S1(T)≥D1∨S2(T)≥D2)]=\displaystyle\displaystyle\qquad+c\left.\mathrm{P}\left(S\_{1}(T)\geq D\_{1}\lor S\_{2}(T)\geq D\_{2}\right)\right]= |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−r​T​[c+(1−c)​P​(S1​(T)<D1∧S2​(T)<D2)],\displaystyle\displaystyle=e^{-rT}\left[c+(1-c)\mathrm{P}\left(S\_{1}(T)<D\_{1}\land S\_{2}(T)<D\_{2}\right)\right], |  | (17) |

where ℙ\displaystyle\mathbb{P} is the physical measure.

### 3.1 Normal approximation

To balance tractability, speed, and accuracy, actuaries can apply approximations to solve real-world insurance problems. We propose here a normal approximation of the price of the considered bond.

We want to approximate the price given by formula ([17](https://arxiv.org/html/2512.08890v1#S3.E17 "In 3 Pricing of a zero-coupon CAT bond under a physical measure ‣ Modelling and valuation of catastrophe bonds across multiple regions")) using the bivariate normal distribution 𝑵=(N1,N2)\displaystyle\boldsymbol{N}=(N\_{1},N\_{2}) with mean

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁=(E​S1​(T)E​S2​(T))\boldsymbol{\mu}=\begin{pmatrix}\mathrm{E}S\_{1}\left(T\right)\\ \mathrm{E}S\_{2}\left(T\right)\end{pmatrix} |  | (18) |

and covariance matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=(Var​S1​(T)Cov​(S1​(T),S2​(T))Cov​(S1​(T),S2​(T))Var​S2​(T)).\boldsymbol{\Sigma}=\begin{pmatrix}\mathrm{Var}S\_{1}\left(T\right)&\mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)\\ \mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)&\mathrm{Var}S\_{2}\left(T\right)\end{pmatrix}. |  | (19) |

This leads to the approximate pricing formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V0a​p​p​r​o​x=e−r​T​[c+(1−c)​P​(N1<D1∧N2<D2)].V\_{0}^{approx}=e^{-rT}\left[c+(1-c)\mathrm{P}\left(N\_{1}<D\_{1}\land N\_{2}<D\_{2}\right)\right]. |  | (20) |

We now aim to specify the formula for Models 1-3.

#### 3.1.1 Model 1

For Model 1 given by equation ([4](https://arxiv.org/html/2512.08890v1#S2.E4 "In 2.1 Model 1. Independent loss processes ‣ 2 Three approaches for modelling dependence in different regions ‣ Modelling and valuation of catastrophe bonds across multiple regions"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁=(E​S1​(T)E​S2​(T))=(E​(N(1)​(T))​E​X1E​(N(2)​(T))​E​Y1)\boldsymbol{\mu}=\begin{pmatrix}\mathrm{E}S\_{1}\left(T\right)\\ \mathrm{E}S\_{2}\left(T\right)\end{pmatrix}=\begin{pmatrix}\mathrm{E}\left(N^{(1)}(T)\right)\mathrm{E}X\_{1}\\ \mathrm{E}\left(N^{(2)}(T)\right)\mathrm{E}Y\_{1}\end{pmatrix} |  | (21) |

and covariance matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=(Var​S1​(T)Cov​(S1​(T),S2​(T))Cov​(S1​(T),S2​(T))Var​S2​(T)),\boldsymbol{\Sigma}=\begin{pmatrix}\mathrm{Var}S\_{1}\left(T\right)&\mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)\\ \mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)&\mathrm{Var}S\_{2}\left(T\right)\end{pmatrix}, |  | (22) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var\displaystyle\displaystyle\mathrm{Var} | (S1​(T))=Var​(X1)​E​(N(1)​(T))+(E​(X1))2​Var​(N(1)​(T)),\displaystyle\displaystyle\left(S\_{1}\left(T\right)\right)=\mathrm{Var}(X\_{1})\mathrm{E}\left(N^{(1)}(T)\right)+\left(\mathrm{E}(X\_{1})\right)^{2}\mathrm{Var}\left(N^{(1)}(T)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Var\displaystyle\displaystyle\mathrm{Var} | (S2​(T))=Var​(Y1)​E​(N(2)​(T))+(E​(Y1))2​Var​(N(2)​(T)),\displaystyle\displaystyle\left(S\_{2}\left(T\right)\right)=\mathrm{Var}(Y\_{1})\mathrm{E}\left(N^{(2)}(T)\right)+\left(\mathrm{E}(Y\_{1})\right)^{2}\mathrm{Var}\left(N^{(2)}(T)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov\displaystyle\displaystyle\mathrm{Cov} | (S1​(T),S2​(T))=0.\displaystyle\displaystyle\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)=0. |  |

#### 3.1.2 Model 2

For Model 2 given by equation ([8](https://arxiv.org/html/2512.08890v1#S2.E8 "In 2.2 Model 2. Losses split proportionally with a fixed proportion ‣ 2 Three approaches for modelling dependence in different regions ‣ Modelling and valuation of catastrophe bonds across multiple regions"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁=(E​S1​(T)E​S2​(T))=(E​(N(1)​(T))​E​X1+p​E​(N(2)​(T))​E​ZE​(N(3)​(T))​E​Y1+(1−p)​E​(N(2)​(T))​E​Z),\boldsymbol{\mu}=\begin{pmatrix}\mathrm{E}S\_{1}\left(T\right)\\ \mathrm{E}S\_{2}\left(T\right)\end{pmatrix}=\begin{pmatrix}\mathrm{E}\left(N^{(1)}(T)\right)\mathrm{E}X\_{1}+p\,\mathrm{E}\left(N^{(2)}(T)\right)\mathrm{E}Z\\ \mathrm{E}\left(N^{(3)}(T)\right)\mathrm{E}Y\_{1}+(1-p)\,\mathrm{E}\left(N^{(2)}(T)\right)\mathrm{E}Z\end{pmatrix}, |  | (23) |

and covariance matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=(Var​S1​(T)Cov​(S1​(T),S2​(T))Cov​(S1​(T),S2​(T))Var​S2​(T)),\boldsymbol{\Sigma}=\begin{pmatrix}\mathrm{Var}S\_{1}\left(T\right)&\mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)\\ \mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)&\mathrm{Var}S\_{2}\left(T\right)\end{pmatrix}, |  | (24) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var\displaystyle\displaystyle\mathrm{Var} | (S1​(T))=Var​(X1)​E​(N(1)​(T))+(E​(X1))2​Var​(N(1)​(T))+\displaystyle\displaystyle\left(S\_{1}\left(T\right)\right)=\mathrm{Var}(X\_{1})\mathrm{E}\left(N^{(1)}(T)\right)+\left(\mathrm{E}(X\_{1})\right)^{2}\mathrm{Var}\left(N^{(1)}(T)\right)+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +p2​[Var​(Z1)​E​(N(2)​(T))+(E​Z1)2​Var​(N(2)​(T))],\displaystyle\displaystyle+p^{2}\left[\mathrm{Var}(Z\_{1})\mathrm{E}\left(N^{(2)}(T)\right)+\left(\mathrm{E}Z\_{1}\right)^{2}\mathrm{Var}\left(N^{(2)}(T)\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Var\displaystyle\displaystyle\mathrm{Var} | (S2​(T))=Var​(Y1)​E​(N(3)​(T))+(E​(Y1))2​Var​(N(3)​(T))+\displaystyle\displaystyle\left(S\_{2}\left(T\right)\right)=\mathrm{Var}(Y\_{1})\mathrm{E}\left(N^{(3)}(T)\right)+\left(\mathrm{E}(Y\_{1})\right)^{2}\mathrm{Var}\left(N^{(3)}(T)\right)+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−p)2​[Var​(Z1)​E​(N(2)​(T))+(E​Z1)2​Var​(N(2)​(T))],\displaystyle\displaystyle+(1-p)^{2}\left[\mathrm{Var}(Z\_{1})\mathrm{E}\left(N^{(2)}(T)\right)+\left(\mathrm{E}Z\_{1}\right)^{2}\mathrm{Var}\left(N^{(2)}(T)\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov\displaystyle\displaystyle\mathrm{Cov} | (S1(T),S2(T))=p(1−p)[Var(Z1)E(N(2)(T))\displaystyle\displaystyle\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)=p(1-p)\left[\mathrm{Var}(Z\_{1})\mathrm{E}\left(N^{(2)}(T)\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(EZ1)2Var(N(2)(T))].\displaystyle\displaystyle+\left.\left(\mathrm{E}Z\_{1}\right)^{2}\mathrm{Var}\left(N^{(2)}(T)\right)\right]. |  |

#### 3.1.3 Dependent losses

For Model 3 given by equation ([12](https://arxiv.org/html/2512.08890v1#S2.E12 "In 2.3 Model 3. Dependent losses ‣ 2 Three approaches for modelling dependence in different regions ‣ Modelling and valuation of catastrophe bonds across multiple regions"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁=(E​S1​(T)E​S2​(T))=(E​(N(1)​(T))​E​X(1)+E​(N(2)​(T))​E​X(2)E​(N(3)​(T))​E​Y(1)+E​(N(2)​(T))​E​Y(2))\boldsymbol{\mu}=\begin{pmatrix}\mathrm{E}S\_{1}\left(T\right)\\ \mathrm{E}S\_{2}\left(T\right)\end{pmatrix}=\begin{pmatrix}\mathrm{E}\left(N^{(1)}(T)\right)\mathrm{E}X^{(1)}+\mathrm{E}\left(N^{(2)}(T)\right)\mathrm{E}X^{(2)}\\ \mathrm{E}\left(N^{(3)}(T)\right)\mathrm{E}Y^{(1)}+\mathrm{E}\left(N^{(2)}(T)\right)\mathrm{E}Y^{(2)}\end{pmatrix} |  | (25) |

and covariance matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=(Var​S1​(T)Cov​(S1​(T),S2​(T))Cov​(S1​(T),S2​(T))Var​S2​(T)),\boldsymbol{\Sigma}=\begin{pmatrix}\mathrm{Var}S\_{1}\left(T\right)&\mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)\\ \mathrm{Cov}\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)&\mathrm{Var}S\_{2}\left(T\right)\end{pmatrix}, |  | (26) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var\displaystyle\displaystyle\mathrm{Var} | (S1​(T))=Var​(X(1))​E​(N(1)​(T))+(E​(X(1)))2​Var​(N(1)​(T))+\displaystyle\displaystyle\left(S\_{1}\left(T\right)\right)=\mathrm{Var}(X^{(1)})\mathrm{E}\left(N^{(1)}(T)\right)+\left(\mathrm{E}(X^{(1)})\right)^{2}\mathrm{Var}\left(N^{(1)}(T)\right)+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Var​(X(2))​E​(N(2)​(T))+(E​(X(2)))2​Var​(N(2)​(T)),\displaystyle\displaystyle\qquad+\mathrm{Var}(X^{(2)})\mathrm{E}\left(N^{(2)}(T)\right)+\left(\mathrm{E}(X^{(2)})\right)^{2}\mathrm{Var}\left(N^{(2)}(T)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Var\displaystyle\displaystyle\mathrm{Var} | (S2​(T))=Var​(Y(1))​E​(N(3)​(T))+(E​(Y(1)))2​Var​(N(3)​(T))+\displaystyle\displaystyle\left(S\_{2}\left(T\right)\right)=\mathrm{Var}(Y^{(1)})\mathrm{E}\left(N^{(3)}(T)\right)+\left(\mathrm{E}(Y^{(1)})\right)^{2}\mathrm{Var}\left(N^{(3)}(T)\right)+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Var​(Y(2))​E​(N(2)​(T))+(E​(Y(2)))2​Var​(N(2)​(T)),\displaystyle\displaystyle\qquad+\mathrm{Var}(Y^{(2)})\mathrm{E}\left(N^{(2)}(T)\right)+\left(\mathrm{E}(Y^{(2)})\right)^{2}\mathrm{Var}\left(N^{(2)}(T)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov\displaystyle\displaystyle\mathrm{Cov} | (S1​(T),S2​(T))=E​[(N(2)​(T))2]​Cov​(X(2),Y(2))\displaystyle\displaystyle\left(S\_{1}\left(T\right),S\_{2}\left(T\right)\right)=\mathrm{E}\left[\left(N^{(2)}(T)\right)^{2}\right]\mathrm{Cov}\left(X^{(2)},Y^{(2)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +E​X(2)​Var​(N(2)​(T))​E​Y(2).\displaystyle\displaystyle+\mathrm{E}X^{(2)}\mathrm{Var}\left(N^{(2)}(T)\right)\mathrm{E}Y^{(2)}. |  |

## 4 Wang transform

The Wang transform is a tool from actuarial science and risk management, which helps to adjust probabilities so that they reflect risk aversion rather than just expected values [Wang2002].
Let X\displaystyle X be the future value of a financial asset at time T\displaystyle T, with a cumulative distribution function F​(x)\displaystyle F(x). Wang proposed a pricing method based on a transform given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | F∗​(x)=Φ​[Φ−1​(F​(x))+λ],F^{\*}(x)=\Phi\left[\Phi^{-1}\left(F(x)\right)+\lambda\right], |  | (27) |

where Φ​(x)\displaystyle\Phi(x) is a cumulative distribution function (cdf) of standard normal distribution and parameter λ\displaystyle\lambda is called the market price of risk [Wang1995, Wang1996a]. The mean value E∗​[X]\displaystyle E^{\*}\left[X\right], taken under F∗​(x)\displaystyle F^{\*}(x), defines a risk-adjusted value of X\displaystyle X at time T\displaystyle T.

When applied to the cumulative distribution function of normal or log-normal distributions, Wang’s transform only changes their parameters [Wang2002].

1. 1.

   If F​(x)\displaystyle F(x) is a cdf of normal distribution with parameters μ∈R\displaystyle\mu\in R and σ>0\displaystyle\sigma>0, denoted by 𝒩​(μ,σ2)\displaystyle\mathcal{N}\left(\mu,\sigma^{2}\right), then F∗​(x)\displaystyle F^{\*}(x) is a cdf of normal distribution 𝒩​(μ−λ​σ,σ2)\displaystyle\mathcal{N}\left(\mu-\lambda\sigma,\sigma^{2}\right).
2. 2.

   If F​(x)\displaystyle F(x) is a cdf of log-normal distribution with parameters μ∈R\displaystyle\mu\in R and σ>0\displaystyle\sigma>0, denoted by ℒ​𝒩​(μ,σ2)\displaystyle\mathcal{LN}\left(\mu,\sigma^{2}\right), then F∗​(x)\displaystyle F^{\*}(x) is a cdf of log-normal distribution ℒ​𝒩​(μ−λ​σ,σ2)\displaystyle\mathcal{LN}\left(\mu-\lambda\sigma,\sigma^{2}\right).

For a liability described by the loss variable Y\displaystyle Y with cdf F​(y)\displaystyle F(y), the Wang transform is given as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S∗​(x)=Φ​[Φ−1​(S​(x))+λ],S^{\*}(x)=\Phi\left[\Phi^{-1}\left(S(x)\right)+\lambda\right], |  | (28) |

where S​(x)=1−F​(x)\displaystyle S(x)=1-F(x) is the tail of the distribution.

A liability can be treated as a negative asset, so two transformations can be used equivalently when dealing with insurance losses:

1. 1.

   apply transform given by equation ([27](https://arxiv.org/html/2512.08890v1#S4.E27 "In 4 Wang transform ‣ Modelling and valuation of catastrophe bonds across multiple regions")) with −λ\displaystyle-\lambda to the cdf F​(y)\displaystyle F(y) of the loss variable;
2. 2.

   apply transform given by equation ([28](https://arxiv.org/html/2512.08890v1#S4.E28 "In 4 Wang transform ‣ Modelling and valuation of catastrophe bonds across multiple regions")) with λ\displaystyle\lambda to the cdf F​(y)\displaystyle F(y)
   of the loss variable.

While pricing a contingent payoff Y=h​(X)\displaystyle Y=h(X), we can apply the Wang transform in one of two ways. First, we can apply the Wang transform to the distribution F​(x)\displaystyle F(x) of the underlying risk X\displaystyle X and then find the distribution of the contingent payoff Y∗=h​(X∗),\displaystyle Y^{\*}=h(X^{\*}), where X∗\displaystyle X^{\*} is the modified underlying risk variable, after the Wang transform was applied to the distribution of X\displaystyle X. Another possibility is to find the distribution G​(y)\displaystyle G(y) of the contingent payoff for Y=h​(X)\displaystyle Y=h(X) and apply the Wang transform to it, using the same λ\displaystyle\lambda as in the first method.

In case of our models, we apply the Wang transform directly to the distributions of losses. Then, we use the modified distributions for simulations leading
to the ZC CAT bonds prices. Since we are dealing with losses, we use the transform given by formula ([27](https://arxiv.org/html/2512.08890v1#S4.E27 "In 4 Wang transform ‣ Modelling and valuation of catastrophe bonds across multiple regions")) with negative values of the parameter λ\displaystyle\lambda and investigate the impact of the parameter λ\displaystyle\lambda on the final price of the ZC CAT bond.

## 5 Case study: PCS data

![Refer to caption](Figure/mapa_OKTX_ILKY.png)


Figure 1: Location of analysed pairs of states in the USA – Oklahoma and Texas, Illinois and Kentucky (from: <https://github.com/joncutrer/geopandas-tutorial>).

Property Claim Services (PCS) is the insurance industry’s well-known source for reporting catastrophic property losses. From the PCS dataset, we selected losses caused by two types of perils: wind and thunderstorm events, and winter storms, which were two of the most common perils in the set. We analyse two pairs of states: the first one is Oklahoma and Texas, the second one is Illinois and Kentucky, see Figure [1](https://arxiv.org/html/2512.08890v1#S5.F1 "Figure 1 ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions").

Since only natural disasters exceeding 25 million USD have recently been recorded in the PSC database, we extracted the losses from the historical database that are above that threshold (after the adjustment with the Consumer Price Index). To identify and validate the left-truncated distributions underlying the observed loss amounts, we apply the procedure explained in detail in [giuricich].

For Model 1 with independent losses, we treat the losses from each state as independent and fit their distributions separately.
Then, the sample is divided into three categories: losses that only happened in the first state, losses that only happened in the second state, and common losses caused by the same catastrophe in both states at the same time. In Model 2, we assume that the common losses are proportionally divided between the two states. The distribution is fitted to the total loss from two states and the p\displaystyle p of the loss is assigned to the first state and 1−p\displaystyle 1-p to the second.
In Model 3, we fit the distributions separately to the losses from each state and calculate the Spearman correlation coefficient. We use that correlation coefficient, since, for the simulation procedure, we use the method proposed by Fackler in [fackler1991genspec], which relies on the Spearman correlation.

### 5.1 Oklahoma and Texas

![Refer to caption](x1.png)


Figure 2: Adjusted losses in billion USD caused in (a) Oklahoma, (b) Texas by wind and thunderstorm events and winter storms.

Texas and Oklahoma were the two states most affected by natural disasters (in terms of the number of the catastrophes) during the considered period. There were 163 catastrophes in Texas and 85 in Oklahoma in total, of which 44 events occurred in both states at the same time. The data set is presented in Figure [2](https://arxiv.org/html/2512.08890v1#S5.F2 "Figure 2 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions").

To describe the moments of catastrophe occurrence, we fitted a homogeneous Poisson process with intensity λ>0\displaystyle\lambda>0. For the first model, we need two processes, one for all losses in Oklahoma and one for all losses in Texas. For Models 2 and 3, we need two Poisson processes counting losses that occur only in one of the states and the third one that counts the events happening in both regions. The fitted λ\displaystyle\lambda values were the following:

1. 1.

   for all catastrophes that occurred in Oklahoma: λ=2.89\displaystyle\lambda=2.89;
2. 2.

   for all catastrophes that occurred in Texas: λ=6.04\displaystyle\lambda=6.04;
3. 3.

   for catastrophes that occurred only in Texas: λ=4.76\displaystyle\lambda=4.76;
4. 4.

   for catastrophes that occurred only in Oklahoma: λ=1.53\displaystyle\lambda=1.53;
5. 5.

   for catastrophes that hit both Oklahoma and Texas: λ=1.40\displaystyle\lambda=1.40.

The next step is to identify the distribution of the losses in each case considered for the three proposed models: all losses in the region, losses that only affect the given region, common and total losses in both regions. Distributions such as log-normal, Weibull, Pareto, and inverse Gaussian were fitted to the samples, taking into account that the data were left-truncated at 25 billion dollars. The goodness of fit was tested using Kolmogorov-Smirnov (KS), Kuiper (V), Anderson Darling (AD), and Cramer von Mises (CvM) test statistics. The best results were obtained with log-normal and inverse Gaussian distributions. The fitted distributions with their parameters are presented in Table [1](https://arxiv.org/html/2512.08890v1#S5.T1 "Table 1 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions").

Table 1: Results of the identification and validation procedure for losses in Oklahoma and Texas for all considered models. Test statistics with simulated p\displaystyle p-values (in italics).

| Losses | Distribution | KS | V | AnD | CvM |
| --- | --- | --- | --- | --- | --- |
| all in OK | Log-normal | 0.207 | 0.353 | 0.629 | 0.074 |
| μ=−4.783,σ=1.841\displaystyle\mu=-4.783,\sigma=1.841 | 0.961 | 0.935 | 0.642 | 0.971 |
| all in TX | Log-normal | 0.523 | 0.941 | 0.499 | 0.091 |
| μ=−2.702,σ=1.246\displaystyle\mu=-2.702,\sigma=1.246 | 0.862 | 0.671 | 0.831 | 0.783 |
| only in OK | Log-normal | 0.148 | 0.272 | 0.464 | 0.057 |
| μ=−5.012,σ=1.864\displaystyle\mu=-5.012,\sigma=1.864 | 0.990 | 0.967 | 0.517 | 0.984 |
| only in TX | Log-normal | 0.474 | 0.890 | 0.482 | 0.087 |
| μ=−2.807,σ=1.266\displaystyle\mu=-2.807,\sigma=1.266 | 0.900 | 0.732 | 0.860 | 0.818 |
| total common | Log-normal | 0.874 | 1.480 | 0.957 | 0.156 |
| in OK&TX | μ=−1.477,σ=0.902\displaystyle\mu=-1.477,\sigma=0.902 | 0.039 | 0.035 | 0.013 | 0.020 |
| common in OK | Log-normal | 0.276 | 0.489 | 0.595 | 0.089 |
| μ=−4.564,σ=1.812\displaystyle\mu=-4.564,\sigma=1.812 | 0.942 | 0.885 | 0.550 | 0.965 |
| common in TX | Inverse Gaussian | 0.496 | 0.913 | 0.244 | 0.039 |
| μ=0.181,λ=0.098\displaystyle\mu=0.181,\lambda=0.098 | 0.868 | 0.729 | 0.916 | 0.902 |

For Models 2 and 3, we need to analyse the dependence between losses from common events. In Figure [3](https://arxiv.org/html/2512.08890v1#S5.F3 "Figure 3 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions"), the percentage share of losses in Oklahoma and Texas was depicted. In most cases, the losses in Texas were higher than those in Oklahoma, although both states suffered extremely high losses a few times. Based on that analysis, the parameter p\displaystyle p of Model 2 was set to 0.41\displaystyle 0.41, which corresponds to the historical mean percentage share.

![Refer to caption](x2.png)


Figure 3: (a) Box plots and (b) histograms of the percentage share of common losses of Oklahoma and Texas. The average percentage share is equal to p=0.41\displaystyle p=0.41.

In Model 3, we assume that the losses from common catastrophes are correlated with a given correlation coefficient. For the analysed data, the Spearman correlation coefficient is equal to ρ=0.31\displaystyle\rho=0.31, whereas the Pearson correlation coefficient is very close to zero.

![Refer to caption](x3.png)


Figure 4: Comparison of real and simulated common losses in Oklahoma and Texas for (a) proportionally split losses model and (b) dependent model.

Both approaches to describing the losses common to both regions are illustrated in Figure [4](https://arxiv.org/html/2512.08890v1#S5.F4 "Figure 4 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions"). The modelling approach that assumes that a total loss is split in a common proportion is shown in Figure [4](https://arxiv.org/html/2512.08890v1#S5.F4 "Figure 4 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). We can clearly observe that it gives a worse fit than the approach that uses two correlated variables, presented in Figure [4](https://arxiv.org/html/2512.08890v1#S5.F4 "Figure 4 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions") (b). However, assuming a constant proportion between the losses may simplify both modelling and subsequent simulations, so it is worth investigating.

Having fitted the models, we investigate now how the choice of the loss model and the normal approximation affect the price of a CAT bond with a payoff defined in ([15](https://arxiv.org/html/2512.08890v1#S3.E15 "In 3 Pricing of a zero-coupon CAT bond under a physical measure ‣ Modelling and valuation of catastrophe bonds across multiple regions")). We assume the recovery rate c=0\displaystyle c=0 and a constant interest rate r=0.03\displaystyle r=0.03. The price of a two year zero-coupon CAT bond is calculated by means of 20K Monte Carlo simulations. The bond threshold for Oklahoma is denoted by D1\displaystyle D\_{1} and for Texas by D2\displaystyle D\_{2}.

![Refer to caption](x4.png)

Figure 5: ZC CAT prices for independent model (Model 1) for OK and TX: (a) price from Monte Carlo simulations, (b) normal approximation and (c) relative error of the approximation.

![Refer to caption](x5.png)

Figure 6: ZC CAT bond prices for model with proportionally split losses (Model 2) for OK and TX: (a) price from Monte Carlo simulations, (b) normal approximation and (c) relative error of the approximation.

![Refer to caption](x6.png)

Figure 7: ZC CAT bond prices for dependent model (Model 3) for OK and TX: (a) price from Monte Carlo simulations, (b) normal approximation and (c) relative error of the approximation.

First, the price for Model 1 with independent losses was calculated with the help of Monte Carlo simulations, see Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). As expected, the price increases with increasing thresholds D1\displaystyle D\_{1} and D2\displaystyle D\_{2}. In Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b) the results of the normal approximation are presented. To this end, the mean vector and covariance matrix necessary for the approximation (see equations ([21](https://arxiv.org/html/2512.08890v1#S3.E21 "In 3.1.1 Model 1 ‣ 3.1 Normal approximation ‣ 3 Pricing of a zero-coupon CAT bond under a physical measure ‣ Modelling and valuation of catastrophe bonds across multiple regions")) and ([22](https://arxiv.org/html/2512.08890v1#S3.E22 "In 3.1.1 Model 1 ‣ 3.1 Normal approximation ‣ 3 Pricing of a zero-coupon CAT bond under a physical measure ‣ Modelling and valuation of catastrophe bonds across multiple regions"))) were calculated for left-truncated distributions fitted to the data. We can see that the normal approximation gives rise to higher prices. The relative error of the approximation (with respect to the simulated values) is shown in Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c), and does not exceed 3%.

The relation between thresholds and the price of the CAT bond is also valid for Model 2, see Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). The normal approximation overestimates the price (Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b)) but the relative error of the approximation again does not exceed 3%, cf. Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c).

The normal approximation yields the worst result in the case of Model 3 with dependent losses, namely we observe larger differences between prices obtained from Monte Carlo simulations (Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a)) and the approximated values (Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b)). The approximation underestimates the price by up to 10% in the worst case, see Figure [7](https://arxiv.org/html/2512.08890v1#S5.F7 "Figure 7 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c).

![Refer to caption](x7.png)


Figure 8: Differences between ZC CAT bond prices obtained from different models for OK and TX: (a) Model 2 – Model 1, (b) Model 3 – Model 1, (c) Model 3 – Model 2.

Finally, the differences between the prices obtained from all models are illustrated in Figure [8](https://arxiv.org/html/2512.08890v1#S5.F8 "Figure 8 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions"). We can see that Model 2 leads to higher prices than Model 1, see Figure [8](https://arxiv.org/html/2512.08890v1#S5.F8 "Figure 8 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). Moreover, Model 2 gives higher prices than Model 3, see Figure [8](https://arxiv.org/html/2512.08890v1#S5.F8 "Figure 8 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c). Hence, Model 2 leads to the highest CAT bond prices, In Figure [8](https://arxiv.org/html/2512.08890v1#S5.F8 "Figure 8 ‣ 5.1 Oklahoma and Texas ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b) we can observe that the differences between the prices obtained from Model 1 and Model 3 are mostly close to zero, only for lower values of D2\displaystyle D\_{2} the prices calculated from Model 1 are significantly higher.

### 5.2 Illinois and Kentucky

We now study the natural catastrophe losses that occurred in Illinois and Kentucky. In Illinois 111 catastrophes occurred, and Kentucky was affected by 45 events in the analysed period. Of these, 18 events affected both states simultaneously. The adjusted losses in both states are presented in Figure [10](https://arxiv.org/html/2512.08890v1#S5.F10 "Figure 10 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions").

![Refer to caption](x8.png)

Figure 9: Adjusted losses in billion USD caused in (a) Illinois, (b) Kentucky by wind and thunderstorm events and winter storms.

![Refer to caption](x9.png)

Figure 10: (a) Box plots and (b) histograms of the percentage share of common losses of Illinois and Kentucky. The average percentage share is to p=0.49\displaystyle p=0.49 for Oklahoma.

Similarly as before, five counting processes are needed, two for all losses in each region, two for losses affecting only one region, and one process for losses from disasters occurring in both regions. We fitted intensities of homogeneous Poisson processes and obtained the following results:

1. 1.

   for all catastrophes that occurred in Illinois: λ=3.59\displaystyle\lambda=3.59;
2. 2.

   for all catastrophes that occurred in Kentucky: λ=1.46\displaystyle\lambda=1.46;
3. 3.

   for catastrophes that occurred only in Illinois: λ=2.72\displaystyle\lambda=2.72;
4. 4.

   for catastrophes that occurred only in Kentucky: λ=0.59\displaystyle\lambda=0.59;
5. 5.

   for catastrophes that hit both Illinois and Kentucky: λ=0.89\displaystyle\lambda=0.89.

The same left-truncated distributions as for losses in Oklahoma and Texas were tested for Illinois and Kentucky. The distribution parameters that gave the best fit, together with test statistics and simulated p\displaystyle p-values, are presented in Table [2](https://arxiv.org/html/2512.08890v1#S5.T2 "Table 2 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions"). The distributions of common losses in Illinois and Kentucky were best described by the Pareto and log-normal distributions, respectively. The log-normal distribution was selected for all other cases.

Table 2: Results of the identification and validation procedure for losses in Illinois and Kentucky for all considered models. Test statistics with simulated p\displaystyle p-values (in italics).

| Losses | Distribution | KS | V | AnD | CvM |
| --- | --- | --- | --- | --- | --- |
| all in IL | Log-normal | 0.215 | 0.390 | 0.544 | 0.075 |
| μ=−4.554,σ=1.386\displaystyle\mu=-4.554,\sigma=1.386 | 0.962 | 0.915 | 0.667 | 0.976 |
| all in KY | Log-normal | 0.070 | 0.1370 | 0.119 | 0.014 |
| μ=−4.869,σ=1.736\displaystyle\mu=-4.869,\sigma=1.736 | 1.000 | 1.000 | 0.526 | 1.000 |
| only in IL | Log-normal | 0.118 | 0.197 | 0.468 | 0.063 |
| μ=−5.288.σ=1.569\displaystyle\mu=-5.288.\sigma=1.569 | 0.982 | 0.973 | 0.555 | 0.989 |
| only in KY | Log-normal | 0.120 | 0.219 | 0.271 | 0.037 |
| μ=−4.709,σ=1.749\displaystyle\mu=-4.709,\sigma=1.749 | 0.998 | 0.994 | 0.506 | 0.994 |
| total common | Log-normal | 0.641 | 1.150 | 0.621 | 0.086 |
| in IL&KY | μ=−1.942,σ=0.718\displaystyle\mu=-1.942,\sigma=0.718 | 0.327 | 0.252 | 0.111 | 0.121 |
| common in IL | Pareto | 0.307 | 0.518 | 0.228 | 0.037 |
| k=0.314,σ=0.032\displaystyle k=0.314,\sigma=0.032 | 0.918 | 0.867 | 0.86 | 0.98 |
| common in KY | Log-normal | 0.106 | 0.187 | 0.283 | 0.029 |
| μ=−4.918,σ=1.713\displaystyle\mu=-4.918,\sigma=1.713 | 0.998 | 0.995 | 0.499 | 0.998 |

The distribution of the percentage share of common losses of
Illinois and Kentucky is depicted in Figure [10](https://arxiv.org/html/2512.08890v1#S5.F10 "Figure 10 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions"). Compared to the previous pair, in this case, the losses are more evenly distributed across two states. The average percentage share was close to p=0.5\displaystyle p=0.5, which is the value chosen for Model 2. The Spearman correlation coefficient is equal to ρ=0.22\displaystyle\rho=0.22, whereas the Pearson correlation coefficient is very close to zero.
Two approaches to modelling losses from common events in Illinois and Kentucky are illustrated in Figure [11](https://arxiv.org/html/2512.08890v1#S5.F11 "Figure 11 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions"), with the approach of Model 3 giving a better fit to the data than the approach of Model 2.

![Refer to caption](x10.png)


Figure 11: Comparison of real and simulated common losses in Illinois and Kentucky for (a) proportionally split losses model and (b) dependent model.

In order to obtain the CAT bond prices, we choose the same bond parameters as before, so c=0\displaystyle c=0 and r=0.03\displaystyle r=0.03. The price of a two year zero-coupon CAT bond is calculated by means of 20K Monte Carlo simulations. The bond threshold for Illinois is denoted by D1\displaystyle D\_{1} and for Kentucky by D2\displaystyle D\_{2}.

The prices for Model 1 with independent losses calculated with the help of Monte Carlo simulations are presented in Figure [13](https://arxiv.org/html/2512.08890v1#S5.F13 "Figure 13 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). The price clearly increases with increasing thresholds D1\displaystyle D\_{1} and D2\displaystyle D\_{2}. In Figure [13](https://arxiv.org/html/2512.08890v1#S5.F13 "Figure 13 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b) the results of the normal approximation are presented. We can see that, contrary to the previously considered pair of states, the normal approximation mostly yields lower prices. The relative error of the approximation (with respect to the simulated values) is presented in Figure [13](https://arxiv.org/html/2512.08890v1#S5.F13 "Figure 13 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c), and reaches -8%.

The prices calculated for Model 2 are shown in Figure [13](https://arxiv.org/html/2512.08890v1#S5.F13 "Figure 13 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). They clearly increase with respect to the thresholds D1\displaystyle D\_{1} and D2\displaystyle D\_{2}. Now, the normal approximation is quite close to the price obtained from Monte Carlo simulations, see Figures [13](https://arxiv.org/html/2512.08890v1#S5.F13 "Figure 13 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b) [13](https://arxiv.org/html/2512.08890v1#S5.F13 "Figure 13 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c). The relative error of the approximation again usually is low only for small D1\displaystyle D\_{1}’s and D2\displaystyle D\_{2}’s it reaches -6%.

As for the previous pair of states, the normal approximation yields the worst result in the case of Model 3 with dependent losses, namely we observe larger differences between prices obtained from Monte Carlo simulations (Figure [14](https://arxiv.org/html/2512.08890v1#S5.F14 "Figure 14 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a)) and the approximated values (Figure [14](https://arxiv.org/html/2512.08890v1#S5.F14 "Figure 14 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b)). The approximation underestimates the price by up to 40% in the worst case, cf. Figure [14](https://arxiv.org/html/2512.08890v1#S5.F14 "Figure 14 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c).

![Refer to caption](x11.png)

Figure 12: ZC CAT bond prices for independent model (Model 1) for IL and KY: (a) price from Monte Carlo simulations, (b) normal approximation and (c) relative difference.

![Refer to caption](x12.png)

Figure 13: ZC CAT bond prices for model with proportionally split losses (Model 2) for IL and KY: (a) price from Monte Carlo simulations, (b) normal approximation and (c) relative difference.

![Refer to caption](x13.png)


Figure 14: ZC CAT bond prices for dependent model (Model 3) for IL and KY: (a) price from Monte Carlo simulations, (b) normal approximation and (c) relative difference.

![Refer to caption](x14.png)


Figure 15: Differences between ZC CAT bond prices obtained from different models for IL and KY: (a) Model 2 – Model 1, (b) Model 3 – Model 1, (c) Model 3 – Model 2.

To compare all three models, in Figure [15](https://arxiv.org/html/2512.08890v1#S5.F15 "Figure 15 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions") we analyse the differences between the obtained prices. From Figure [15](https://arxiv.org/html/2512.08890v1#S5.F15 "Figure 15 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a), we can see that Model 2, including the relation between common losses, usually leads to higher prices. We can observe in Figure [15](https://arxiv.org/html/2512.08890v1#S5.F15 "Figure 15 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b) that Model 3 gives lower prices than Model 1. We can see in Figure [15](https://arxiv.org/html/2512.08890v1#S5.F15 "Figure 15 ‣ 5.2 Illinois and Kentucky ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(c) that all differences are negative, which means that the prices obtained from Model 2 are also higher than the prices obtained from Model 3, so, in this case, including the correlation slightly decreases the price of the bond.

### 5.3 Wang transform

![Refer to caption](x15.png)


Figure 16: Prices of ZC CAT bond obtained from different models (by means of Monte Carlo simulations), for (a) OK and TX, (b) IL and KY, with Wang transform applied to the distribution of losses with varying parameter λ.\displaystyle\lambda.

In this part, we examine the influence of the Wang transform on the CAT bond pricing under each model. We applied the transform defined in ([27](https://arxiv.org/html/2512.08890v1#S4.E27 "In 4 Wang transform ‣ Modelling and valuation of catastrophe bonds across multiple regions")) directly to the distribution of the losses, so negative values of the parameter λ\displaystyle\lambda are used.

In the case of Oklahoma and Texas, we set the thresholds at D1=6\displaystyle D\_{1}=6 and D2=8\displaystyle D\_{2}=8 billion dollars. The results for all models are shown in Figure [16](https://arxiv.org/html/2512.08890v1#S5.F16 "Figure 16 ‣ 5.3 Wang transform ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(a). With an increase in the absolute value of the parameter λ\displaystyle\lambda, representing the market price of risk, the price of the CAT bond decreases. We also notice that for the chosen values of D1\displaystyle D\_{1} and D2\displaystyle D\_{2}, Model 2 gives the highest prices, while Model 1 and Model 3 give similar values.

Similar results were obtained for Illinois and Kentucky, see Figure [16](https://arxiv.org/html/2512.08890v1#S5.F16 "Figure 16 ‣ 5.3 Wang transform ‣ 5 Case study: PCS data ‣ Modelling and valuation of catastrophe bonds across multiple regions")(b). In this case, both thresholds were equal to 3 billion dollars. For the chosen values of D1\displaystyle D\_{1} and D2\displaystyle D\_{2}, Model 2 gives the highest prices, and the prices obtained from Model 1 are higher than those from dependent losses.

## 6 Conclusions

Catastrophe bonds have emerged as a vital mechanism for transferring disaster risk to capital markets, offering benefits such as portfolio diversification, improved risk management for insurers, and improved financial stability for disaster-prone regions [Barrieu2010].However, the complexities in pricing, structuring, and market accessibility highlight challenges that continue to shape the evolution of the CAT bond market. As climate change amplifies the frequency and severity of catastrophic events, the role of CAT bonds is expected to grow, prompting ongoing research to improve their efficacy and expand their use in both financial and societal risk-management strategies [burnecki2023catastrophe].

In this study, we proposed and analysed three distinct modelling approaches for representing catastrophe losses across multiple geographic regions. The models capture a spectrum of dependence structures: from full independence (Model 1), to proportional sharing of common losses (Model 2), to flexible correlation-based dependence (Model 3).

Our results show that the assumed dependency mechanism significantly affects the valuation of the CAT bond. In particular, Model 2 systematically yields higher prices than both Models 1 and 3, reflecting its more conservative treatment of common catastrophic events. Moreover, Model 3 can generate higher or lower prices depending on the empirical correlation structure; for the datasets studied (Oklahoma–Texas and Illinois–Kentucky), introducing correlation tended to decrease prices relative to the proportional model, although its performance varied between thresholds.

We further evaluated a normal approximation to the two-dimensional loss distribution. Across all models, the approximation was computationally efficient and reasonably accurate for moderate threshold values, typically producing errors below 3% for the first two models. However, for the more complex dependent-loss structure (Model 3), the approximation deteriorated, especially for the Illinois–Kentucky dataset, where errors reached 40%. This highlights that reliance on normal approximations should be applied with caution when modelling correlated heavy-tailed phenomena, especially in the presence of left-truncation and heterogeneous dependence.

We also analysed the influence of the Wang transform to incorporate a market price of risk. In both regional case studies, increasing the absolute value of the distortion parameter led to lower CAT bond prices, consistent with the transform’s risk-adjustment effect. The ranking of models remained stable: the proportional-loss model consistently produced the highest prices, whereas the dependent-loss model yielded prices closest to the independent case. These findings confirm that the choice of dependence assumptions plays a more dominant role than risk-loading adjustments in shaping final price levels.

Overall, our framework demonstrates how multi-regional loss modelling can substantially influence CAT bond valuation, and it provides practitioners with flexible tools to incorporate different regional interdependencies. While the study focuses on two-region settings, the modelling concepts naturally extend to higher-dimensional problems, including multi-peril or multi-state ILS structures.

We believe that our findings can be helpful in modelling and pricing other ILS tied to natural disasters and provide a foundation for further research toward more accurate and robust multi-region catastrophe-risk valuation.

## Acknowledgements

The authors’ research was supported by the National Science Centre, Poland (NCN), OPUS grant no. 2022/47/B/HS4/02139.