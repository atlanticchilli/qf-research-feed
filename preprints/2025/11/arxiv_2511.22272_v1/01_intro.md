---
authors:
- Hansjoerg Albrecher
- Jan Beirlant
doc_id: arxiv:2511.22272v1
family_id: arxiv:2511.22272
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook
  of Statistics of Extremes, Chapman & Hall
url_abs: http://arxiv.org/abs/2511.22272v1
url_html: https://arxiv.org/html/2511.22272v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hansjörg Albrecher, Jan Beirlant
Corresponding Author. Department of Actuarial Science, Faculty of
Business and Economics, Swiss
Finance Institute and Expertise Center for Climate Extremes (ECCE), University of Lausanne, CH-1015 Lausanne. Email: hansjoerg.albrecher@unil.chDepartment of Mathematics, KU Leuven, Belgium and Department of Mathematical Statistics and Actuarial Science, University of the Free State, South Africa. Email: jan.beirlant@kuleuven.be

###### Abstract

> We provide a survey of how techniques developed for the modelling of extremes naturally matter in insurance, and how they need to and can be adapted for the insurance applications. Topics covered include truncation, tempering, censoring and regression techniques. The discussed techniques are illustrated on concrete data sets.

## 1 Introduction

Modelling of largest claims naturally arises in actuarial practice. And insurance applications traditionally have been one of the prime applications of extreme value statistics. At the same time, the concrete challenges and specific constraints concerning model assumptions and available data in insurance practice also have been, and still are, a generator of interesting theoretical problems in extreme value statistics.
  
The aggregate sum of claim payments in an insurance portfolio is naturally dominated by the larger components, so that a thorough understanding of the tails of claim distributions is crucial for a proper pricing and management of insurance risk. Tail modelling is most important for reinsurance companies, as the handling of extremes is (among others) one of the main responsibilities of reinsurers.

For the appearance of very heavy tails in insurance, the marine liability data, as analyzed by Guevara-Alarcón et al. [[45](https://arxiv.org/html/2511.22272v1#bib.bib45)], can serve as an illustrative example. There, a data set of large losses from the marine line of business is statistically analyzed in a detailed manner both in terms of frequency and severity.
Figure [1](https://arxiv.org/html/2511.22272v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") reproduces the Hill plot and the Pareto QQ-plot of these claims. One observes that the extreme value index runs between 0.8 and 1.1. This means that the existence of the first moment is questionable, while the second moment is clearly infinite. Hence, the classical risk-theoretical principles do not apply, and a simple insurance coverage is not possible.

![Refer to caption](x1.png)   ![Refer to caption](x2.png)

Figure 1: Hill plot and Pareto QQ-plot of marine liability claim data, cf. Guevara-Alarcón [[45](https://arxiv.org/html/2511.22272v1#bib.bib45)].

The tail risk is then typically taken over by reinsurers against a negotiated premium.
In general, the actuarial methods that have been developed to measure and control risk need to be tailored to each concrete situation (see, e.g. [[3](https://arxiv.org/html/2511.22272v1#bib.bib3)] for a short overview and [[5](https://arxiv.org/html/2511.22272v1#bib.bib5)] for a detailed one). In particular, when the focus is on the tails, specific modelling situations and challenges with data availability occur, for which standard extreme value methods have to be adapted. In this chapter, we will discuss a number of such situations. Classical problems in extreme value analysis (EVA), such as threshold selection or bias reduction, are mentioned where available. We also deal with the estimation of insurance premiums and risk measures based on the constructed models.

In Section [2](https://arxiv.org/html/2511.22272v1#S2 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), we introduce common reinsurance forms. There, we also present those constraints on model choices and data availability in (re)insurance practice that affect the study of extremes and lead to deviations from standard extreme value theory and statistics, in order to motivate the subsequent sections. In reinsurance settings, the Pareto-type model often serves as a starting model, where a loss random variable XX is defined through

|  |  |  |
| --- | --- | --- |
|  | P​(X>x)=x−1/ξ​ℓ​(x),P(X>x)=x^{-1/\xi}\ell(x), |  |

with ξ>0\xi>0 the extreme value index and ℓ\ell a slowly varying function defined by

|  |  |  |
| --- | --- | --- |
|  | limt→∞ℓ​(x​t)ℓ​(t)=1.\lim\_{t\to\infty}\frac{\ell(xt)}{\ell(t)}=1. |  |

Section [3](https://arxiv.org/html/2511.22272v1#S3 "3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") discusses adaptations of the classical tail analysis for truncated losses, as well as the less restrictive situation of tempering. In Section [4](https://arxiv.org/html/2511.22272v1#S4 "4 Censoring ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), we deal with the case of extremes for censored data. In insurance practice, the modelling of the body of the claim distribution and its tail is often separated (distinguishing attritional and large claims), and Section [5](https://arxiv.org/html/2511.22272v1#S5 "5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") describes techniques to reconciliate the two into one model. Section [6](https://arxiv.org/html/2511.22272v1#S6 "6 Regression Modelling ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") and Section [7](https://arxiv.org/html/2511.22272v1#S7 "7 Multivariate Modelling ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") offer a discussion and literature overview of regression and multivariate settings, respectively, with attention for the specific modelling aspects listed above. The importance of a profound understanding of extremal risks is further exacerbated when it comes to the modelling of insurance losses due to natural catastrophes. In particular, dependence assumptions of risks across space and time as well as the non-stationarities of such risks in the light of climate change are to be considered. In Section [8](https://arxiv.org/html/2511.22272v1#S8 "8 Natural Catastrophe Insurance and Climate Change ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), we finish with a respective discussion.

## 2 Reinsurance and Data

Insurance companies typically pass on their exposure to potentially very large claims to reinsurance companies. Therefore, the modelling of extremal events is mainly a concern for the latter. Reinsurers then look for means to diversify these risks, often on a global scale. In the following, we will briefly describe the most common reinsurance forms used in practice and their suitability for the protection against extremal claims. For a comprehensive treatment with attention for EVA, we refer to [[5](https://arxiv.org/html/2511.22272v1#bib.bib5)].

* •

  Proportional Reinsurance. For an individual risk XiX\_{i}, a quota-share (QS) reinsurance treaty is simply a proportional risk sharing with a reinsured amount Ri=a​XiR\_{i}=a\,X\_{i} for some proportionality factor 0<a<10<a<1. It is easy to implement for an entire portfolio, leads to a natural premium scheme (proportional premiums with adjustments for claim acquisition, handling costs etc.) and does not introduce any additional mathematical complexity, as it simply rescales the original quantities. Since this contract also reinsures small claims which the insurer could easily handle himself, a popular variant is reinsurance!surplus. In this case, the proportionality factor for each risk depends on the sum insured in the underlying policy, with a larger reinsured proportion for larger sum insured, and no reinsurance coverage for sums insured that are below some threshold. While these reinsurance forms are very popular in certain lines of business (e.g. fire and property), they do not improve the shape of the tail of the risk exposure for the insurer. This is why non-proportional coverages such as the reinsurance forms described next are much more relevant when it comes to extremes.
* •

  Excess-of-Loss (XL) Reinsurance.
  For a given pre-defined retention MM in an XL treaty, the reinsurer agrees to pay for each claim in the portfolio
  the excess over the retention MM. Typically, this will only be agreed upon up to a certain limit LL, leading to the reinsured amount

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | R=∑i=1Nmin⁡{(Xi−M)+,L}R=\sum\_{i=1}^{N}\min\{(X\_{i}-M)\_{+},L\} |  | (1) |

  for individual risks XiX\_{i}, with (X−u)+:=max⁡(X−u,0)(X-u)\_{+}:=\max(X-u,0), and NN the number of claims in the portfolio (the insurer will then often look for additional XL treaties with higher layers until the remaining risk is considered ‘negligible’). When L=∞L=\infty, the intricate relation between an unbounded XL treaty and POT methodology modelling becomes apparent. Indeed, the modelling of exceedances P​(Xi−M>x​∣Xi>​M)=P​(Xi>M+x)/P​(Xi>M)P(X\_{i}-M>x\mid X\_{i}>M)={P(X\_{i}>M+x)}/{P(X\_{i}>M)} for large values of MM is at the heart of EVA.
    
  If one first aggregates all claims and then applies this principle, i.e. R=min⁡{(∑i=1NXi−M)+,L}R=\min\{(\sum\_{i=1}^{N}X\_{i}-M)\_{+},L\}, then this contract is referred to as a (bounded) Stop-Loss reinsurance treaty. Particularly for the reinsurance of catastrophe losses, it is quite popular to collect all claims due to a particular event, consider them as one claim XicX\_{i}^{c}, and apply an aggregate retention McM^{c} (and limit LcL^{c}) to get

  |  |  |  |
  | --- | --- | --- |
  |  | R=∑i=1Ncmin⁡{(Xic−Mc)+,Lc},R=\sum\_{i=1}^{N^{c}}\min\{(X^{c}\_{i}-M^{c})\_{+},L^{c}\}, |  |

  which is known as (bounded) cumulative XL (or CAT-XL). This is an attractive cover against frequency risk, namely the risk to face many claims, whose individual size may not be extreme but their sum is. Mathematically, this leads to the very same analysis, the only difference being the modelling of the distribution of XicX\_{i}^{c} and the one of the number of catastrophes NcN^{c}.
* •

  Large Claim Reinsurance. From the perspective of extreme value theory, it seems natural to also consider contracts of the form

  |  |  |  |
  | --- | --- | --- |
  |  | R=∑i=1rX(N−i+1)R=\sum\_{i=1}^{r}X\_{(N-i+1)} |  |

  for the order statistics X(1)≤⋯≤X(N)X\_{(1)}\leq\cdots\leq X\_{(N)}. This reinsurance form covers the rr largest claims in the portfolio. Variants are drop-down XL

  |  |  |  |
  | --- | --- | --- |
  |  | R=∑i=1Nmin⁡{Li,(X(N−i+1)−Mi)+},R=\sum\_{i=1}^{N}\min\{L\_{i},(X\_{(N-i+1)}-M\_{i})\_{+}\}, |  |

  where retentions and layer sizes are applied to the respective order statistics, and ECOMOR reinsurance

  |  |  |  |
  | --- | --- | --- |
  |  | R=∑i=1N(Xi−X(N−r))+,R=\sum\_{i=1}^{N}\left(X\_{i}-X\_{(N-r)}\right)\_{+}, |  |

  where the (r+1)(r+1)th largest claim serves as the retention level in an otherwise standard (unbounded) XL contract. While such large claim reinsurance contracts have been implemented in practice to some extent, they have not become popular, partly because the calculation of premiums and the modelling of the retained risk is much more complicated and hence not practical. We will therefore focus on the XL type in the sequel.

In actuarial data sets for XL reinsurance, one faces various kinds of incomplete data:

* •

  In a bounded XL treaty, the reinsurer only pays up to a limit LL for each claim, and the insurer does not necessarily share the full claim amount beyond that limit with the reinsurer, and neither the information on claims that remained below the retention MM. Hence, censoring, and in particular right censoring, at high values is to be considered.
* •

  Claims that have been incurred can still be missing due to reporting delays. Such missing data are referred to as ‘Incurred But Not Reported’ (IBNR) data.
* •

  Right-censoring also occurs when a claim has not been settled at the evaluation date, leading to ‘Reported But Not Settled’ (RBNS) claims. In case of upper limits on the underlying policy, the real costs are censored at a fixed value. The settlement of the eventual claim amounts can take very long (even decades in catastrophe and liability insurance), and the already paid amount is a natural lower bound for the eventual claim size, which also leads to right-censoring. As reported data are then not exact, one needs to work with estimates for the final value. Here, one distinguishes between ‘ultimate’ estimates for non-closed claims (based on modelling assumptions, often chain ladder development methods) and ‘incurred’ values (which are estimates from an accounting perspective, often with expert predictions on the concrete case). Such situations constitute significant challenges to an EVA.
* •

  Since extreme events are rare, there are often not many data points available for an analysis. Therefore, one needs to merge actual historical data points with ones of related risks and with expert opinions (taking into account the implied uncertainty). In some cases, one even needs to price risks without a single data point (see e.g. Fackler [[39](https://arxiv.org/html/2511.22272v1#bib.bib39)]).

On the modelling side, there often is an upper limit of the exposure (either due to contractual limits or due to physical limits, such as the overall building values in an area for the insurance of natural catastrophe claims). This results in truncation modelling. Also, claim payments are influenced by claim management and claims may, for instance, be subject to a higher level of inspection at highest damage levels leading to weaker tails than apparent from intermediate claims, leading to tempering of claim distributions (cf. Section [3.2](https://arxiv.org/html/2511.22272v1#S3.SS2 "3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") for more details). Different models at different claim level intervals are not uncommon.

For an unlimited XL treaty with retention MM, the expected reinsured amount E​(Ri){E}(R\_{i}) of a single claim XiX\_{i} with distribution function FF and finite mean, is given by

|  |  |  |
| --- | --- | --- |
|  | Π​(M):=E​{(Xi−M)+}=∫M∞{1−F​(z)}​d​z,\displaystyle\Pi(M):={E}\{(X\_{i}-M)\_{+}\}=\int\_{M}^{\infty}\{1-F(z)\}\mathop{}\!\mathrm{d}z, |  |

which is also referred to as the pure premium for RiR\_{i}.
Note that

|  |  |  |
| --- | --- | --- |
|  | Π​(M)=e​(M)​F¯​(M)\Pi(M)=e(M)\overline{F}(M) |  |

with e​(u)=E​(Xi−u​∣Xi>​u)e(u)={E}(X\_{i}-u\mid X\_{i}>u) the mean excess function which serves as a basic tool in EVA expressing the expected POT, for which estimation procedures are available in extreme value statistics.
  
With a finite layer size LL in the XL treaty, the pure premium becomes

|  |  |  |
| --- | --- | --- |
|  | E​(Ri)=∫MM+L{1−F​(z)}​d​z=Π​(M)−Π​(M+L).{E}(R\_{i})=\int\_{M}^{M+L}\{1-F(z)\}\mathop{}\!\mathrm{d}z=\Pi(M)-\Pi(M+L). |  |

Considering a retention level MM as an upper quantile or Value-at-Risk (VaR), i.e. VaR1−p=Q​(1−p)=inf{x:F​(x)≥1−p}\mbox{VaR}\_{1-p}=Q(1-p)=\inf\{x:F(x)\geq 1-p\}, the pure premium
is related to the Conditional Tail Expectation CTE1−p​(X)\mbox{CTE}\_{1-p}(X) (also known as expected shortfall in finance) defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CTE1−p​(X)\displaystyle\mbox{CTE}\_{1-p}(X) | =\displaystyle= | E​(X​∣X>​Q​(1−p))\displaystyle{E}(X\mid X>Q(1-p)) |  |
|  |  | =\displaystyle= | VaR1−p​(X)+e​(Q​(1−p)).\displaystyle\mbox{VaR}\_{1-p}(X)+e(Q(1-p)). |  |

One immediately observes

|  |  |  |
| --- | --- | --- |
|  | CTE1−p​(X)=VaR1−p​(X)+Π​{VaR1−p​(X)}p.\mbox{CTE}\_{1-p}(X)=\mbox{VaR}\_{1-p}(X)+\frac{\Pi\{\mbox{VaR}\_{1-p}(X)\}}{p}. |  |

Hence, the estimation of VaR1−p​(X)\mbox{VaR}\_{1-p}(X) and
Π​(M)\Pi(M) at small and intermediate values of pp, or correspondingly at high and intermediate values of MM, is an important building block for measuring and managing risk. However, note that the commercial values of MM and LL not necessarily correspond to statistically optimal threshold values at which tail models fit well. This leads to the need of extending the tail models to full models fitting over larger outcome sets than the thresholds following from an EVA. So, actuaries also need to construct models that simultaneously fit well to the tail and to other parts of the possible outcome set. Such full models can for instance be constructed using splicing models (cf. Section [5](https://arxiv.org/html/2511.22272v1#S5 "5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")).

## 3 Adaptations of the Classical Tail Analysis

In the following we discuss two adaptations of classical EVA that are useful for insurance applications.

### 3.1 Truncation

Practical problems can arise when using the strict Pareto distribution and the more general Pareto-type model because some probability mass can still be assigned to loss amounts that are unreasonably large or even impossible. With respect to tail fitting of insurance claim data,
upper-truncation is of interest and can for instance be due to the existence of a maximum possible loss due to policy or treaty limits or physical limits (like building values in catastrophe insurance). Such truncation effects are sometimes visible in data, for instance when an overall linear Pareto QQ-plot shows non-linear deviations at only a few top data (see Figure [2](https://arxiv.org/html/2511.22272v1#S3.F2 "Figure 2 ‣ 3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") (left)).
Let WW be an underlying non-truncated distribution with distribution function FWF\_{W} and quantile function QWQ\_{W}. Upper-truncation of the distribution of WW at some deterministic value TT then leads to the truncated loss
W∣W<TW\mid W<T, whose distribution function we denote by FTF\_{T}. In practice one does not always know if the data X1,…,XnX\_{1},\ldots,X\_{n} come from a truncated or non-truncated distribution. As a consequence, the behaviour of estimators should be evaluated under both cases, and a statistical test for upper-truncation is useful. This section is taken from Beirlant et al. [[15](https://arxiv.org/html/2511.22272v1#bib.bib15)], where the Pareto-type case is treated. Aban et al. [[1](https://arxiv.org/html/2511.22272v1#bib.bib1)] considered the strict Pareto case. In Beirlant et al. [[16](https://arxiv.org/html/2511.22272v1#bib.bib16)], the case where WW belongs to any max-domain of attraction is considered.

Upper-truncation of WW, at some truncation point TT, yields

|  |  |  |
| --- | --- | --- |
|  | F¯T​(x)=P​(W>x)−P​(W>T)1−P​(W>T)=F¯W​(x)−F¯W​(T)FW​(T),\overline{F}\_{T}(x)=\frac{P(W>x)-P(W>T)}{1-P(W>T)}=\frac{\overline{F}\_{W}(x)-\overline{F}\_{W}(T)}{F\_{W}(T)}, |  |

and the corresponding quantile function QTQ\_{T} is given by

|  |  |  |
| --- | --- | --- |
|  | QT​(1−p)=QW​[1−{F¯W​(T)+p​(1−F¯W​(T))}]=QW​[{1−F¯W​(T)}​(1−p)]Q\_{T}(1-p)=Q\_{W}[1-\{\overline{F}\_{W}(T)+p(1-\overline{F}\_{W}(T))\}]=Q\_{W}[\{1-\overline{F}\_{W}(T)\}(1-p)] |  |

or

|  |  |  |  |
| --- | --- | --- | --- |
|  | QT​(1−p)=QW​{1−F¯W​(T)​(1+pDT)},Q\_{T}(1-p)=Q\_{W}\left\{1-\overline{F}\_{W}(T)\left(1+{p\over D\_{T}}\right)\right\}, |  | (2) |

with DT:=F¯W​(T)/FW​(T)D\_{T}:=\overline{F}\_{W}(T)/F\_{W}(T) being the odds of the truncated probability mass under the non-truncated distribution WW. Note that for a fixed TT, upper-truncation models exhibit an extreme value index ξ=−1\xi=-1. For instance, in case of a simple Pareto distribution one has

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | QT​(1−p)\displaystyle Q\_{T}(1-p) | =\displaystyle= | (p​(1−T−1/ξ)+T−1/ξ)−ξ\displaystyle\left(p(1-T^{-1/\xi})+T^{-1/\xi}\right)^{-\xi} |  |
|  |  | =\displaystyle= | T​(1+p​1−T−1/ξT−1/ξ)−ξ\displaystyle T\left(1+p\frac{1-T^{-1/\xi}}{T^{-1/\xi}}\right)^{-\xi} |  |
|  |  | =\displaystyle= | T​(1−ξ​p​1−T−1/ξT−1/ξ​(1+o​(1)))​ as ​p→0.\displaystyle T\left(1-\xi p\frac{1-T^{-1/\xi}}{T^{-1/\xi}}(1+o(1))\right)\mbox{ as }p\to 0. |  |

In case of a Pareto-type WW, using POT modelling with T/t→β>0T/t\to\beta>0 as t→∞t\to\infty, the distribution of a truncated loss XX leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(X/t>y​∣X>​t)\displaystyle{P}(X/t>y\mid X>t) | =\displaystyle= | P​(W/t>y∣t<W<T)\displaystyle{P}(W/t>y\mid t<W<T) |  |
|  |  | =\displaystyle= | F¯W​(y​t)−F¯W​(T)F¯W​(t)−F¯W​(T)\displaystyle\frac{\overline{F}\_{W}(yt)-\overline{F}\_{W}(T)}{\overline{F}\_{W}(t)-\overline{F}\_{W}(T)} |  |
|  |  | =\displaystyle= | y−1/ξ​ℓF​(y​t)ℓF​(t)−(Tt)−1/ξ​ℓF​(T)ℓF​(t)1−(Tt)−1/ξ​ℓF​(T)ℓF​(t)\displaystyle\frac{y^{-1/\xi}{\ell\_{F}(yt)\over\ell\_{F}(t)}-\left({T\over t}\right)^{-1/\xi}{\ell\_{F}(T)\over\ell\_{F}(t)}}{1-\left({T\over t}\right)^{-1/\xi}{\ell\_{F}(T)\over\ell\_{F}(t)}} |  |
|  |  | →\displaystyle\to | y−1/ξ−β−1/ξ1−β−1/ξ,1<y<β,\displaystyle\frac{y^{-1/\xi}-\beta^{-1/\xi}}{1-\beta^{-1/\xi}},\quad 1<y<\beta, |  |

with ℓF\ell\_{F} a slowly varying function. Thanks to this result, the following POT approximation will be used, assuming T/t→β>0T/t\to\beta>0 as t→∞t\to\infty:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(X/t>y​∣X>​t)≈y−1/ξ−β−1/ξ1−β−1/ξ,1<y<β.{P}(X/t>y\mid X>t)\approx\frac{y^{-1/\xi}-\beta^{-1/\xi}}{1-\beta^{-1/\xi}},\quad 1<y<\beta. |  | (3) |

Using a high order statistic X(n−k)X\_{(n-k)} as the threshold tt, denoting the relative excesses by Rj,k:=X(n−j+1)/X(n−k)R\_{j,k}:=X\_{(n-j+1)}/X\_{(n-k)}, j=1,…,kj=1,\ldots,k, and estimating β\beta by R1,kR\_{1,k},
the pseudo-maximum log-likelihood function is given by (upon differentiating the right-hand side of ([3](https://arxiv.org/html/2511.22272v1#S3.E3 "In 3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")) w.r.t. yy)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡Lk,n​(ξ)\displaystyle\log L\_{k,n}(\xi) | =\displaystyle= | log​∏j=1kRj,k−1−1/ξξ​(1−R1,k−1/ξ)\displaystyle\log\prod\_{j=1}^{k}\frac{R\_{j,k}^{-1-1/\xi}}{\xi(1-R\_{1,k}^{-1/\xi})} |  |
|  |  | =\displaystyle= | −k​log⁡ξ−(1+1ξ)​∑j=1klog⁡Rj,k−k​log⁡(1−R1,k−1/ξ),\displaystyle-k\log\xi-\left(1+{1\over\xi}\right)\sum\_{j=1}^{k}\log R\_{j,k}-k\log\left(1-R\_{1,k}^{-1/\xi}\right), |  |

which leads to the defining equation for the likelihood estimator ξ^k,nT\hat{\xi}^{T}\_{k,n}:

|  |  |  |
| --- | --- | --- |
|  | Hk,n=ξ^k,nT−R1,k−1/ξ^k,nT​log⁡R1,k1−R1,k−1/ξ^k,nT.H\_{k,n}=\hat{\xi}^{T}\_{k,n}-{R\_{1,k}^{-1/\hat{\xi}^{T}\_{k,n}}\log R\_{1,k}\over 1-R\_{1,k}^{-1/\hat{\xi}^{T}\_{k,n}}}. |  |

Using ([2](https://arxiv.org/html/2511.22272v1#S3.E2 "In 3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")) and considering the ratio of quantiles QT​(1−p)Q\_{T}(1-p) with p=1/(n+1),(k+1)/(n+1)p={1/(n+1)},{(k+1)/(n+1)}, estimating QT​(1−p)Q\_{T}(1-p) by the empirical quantiles X(n)X\_{(n)} and X(n−k)X\_{(n-k)} respectively, and taking QW​(1−p)Q\_{W}(1-p) as p−ξp^{-\xi}, we arrive at a simple estimator of DT=P​(W>T)/P​(W≤T)D\_{T}={{P}(W>T)}/{{P}(W\leq T)}:

|  |  |  |
| --- | --- | --- |
|  | D^T=kn​R1,k−1/ξ^kT−1k1−R1,k−1/ξ^kT.\hat{D}\_{T}={k\over n}\frac{R\_{1,k}^{-1/\hat{\xi}\_{k}^{T}}-{1\over k}}{1-R\_{1,k}^{-1/\hat{\xi}\_{k}^{T}}}. |  |

In practice, one makes use of the admissible estimator D^T(0):=max⁡{D^T,0}\widehat{D}^{(0)}\_{T}:=\max\{\hat{D}\_{T},0\}
to make it useful in case of truncated and non-truncated Pareto-type distributions.

If DT>0D\_{T}>0, we find from ([2](https://arxiv.org/html/2511.22272v1#S3.E2 "In 3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")) for WW being strict Pareto that

|  |  |  |  |
| --- | --- | --- | --- |
|  | QT​(1−p)=P​(W>T)−1/ξ​[1+pDT]−1/ξ.Q\_{T}(1-p)={P}(W>T)^{-1/\xi}\left[1+{p\over D\_{T}}\right]^{-1/\xi}. |  | (4) |

Then, in order to construct estimators of TT and of extreme quantiles qp=QT​(1−p)q\_{p}=Q\_{T}(1-p), with ([4](https://arxiv.org/html/2511.22272v1#S3.E4 "In 3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")) we find that

|  |  |  |
| --- | --- | --- |
|  | {QT​(1−p)QT​(1−k+1n+1)}1/ξ=1+k+1(n+1)​DT1+pDT=DT+k+1n+1DT+p.\left\{{Q\_{T}(1-p)\over Q\_{T}(1-{k+1\over n+1})}\right\}^{1/\xi}={1+{k+1\over(n+1)D\_{T}}\over 1+{p\over D\_{T}}}={D\_{T}+{k+1\over n+1}\over D\_{T}+p}. |  |

Taking logarithms on both sides and estimating QT​(1−(k+1)/(n+1))Q\_{T}(1-(k+1)/(n+1)) by Xn−k,nX\_{n-k,n}, we find an estimator Q^kT​(1−p)\hat{Q}^{T}\_{k}(1-p) of Q​(1−p)Q(1-p):

|  |  |  |
| --- | --- | --- |
|  | log⁡Q^kT​(1−p)=log⁡X(n−k)+ξ^k,nT​log⁡(D^T+k+1n+1D^T+p),\log\hat{Q}^{T}\_{k}(1-p)=\log X\_{(n-k)}+\hat{\xi}^{T}\_{k,n}\log\left({\hat{D}\_{T}+{k+1\over n+1}\over\hat{D}\_{T}+p}\right), |  |

which equals the Weissman estimator [[77](https://arxiv.org/html/2511.22272v1#bib.bib77)] when D^T=0\hat{D}\_{T}=0.
An estimator T^k,n\hat{T}\_{k,n} of TT follows from letting p→0p\to 0 in the above expressions for Q^p,kT\hat{Q}^{T}\_{p,k}:

|  |  |  |
| --- | --- | --- |
|  | log⁡T^k,n=max⁡[log⁡X(n−k)+ξ^k,nT​log⁡{1+k+1(n+1)​D^T},log⁡X(n)].\log\hat{T}\_{k,n}=\max\left[\log X\_{(n-k)}+\hat{\xi}^{T}\_{k,n}\log\left\{1+{k+1\over(n+1)\hat{D}\_{T}}\right\},\log X\_{(n)}\right]. |  |

Finally, a test for a truncation setting is to consider an unbounded Pareto distribution as the null hypothesis (H0:T=∞H\_{0}:\,T=\infty) and to reject H0H\_{0} for small values of pp-value given by

|  |  |  |
| --- | --- | --- |
|  | Φ​(12​k​R¯k−0.51−R¯k),\Phi\left(\sqrt{12k}\frac{\overline{R}\_{k}-0.5}{1-\overline{R}\_{k}}\right), |  |

where R¯k=1k​∑j=1kRj,k−1/Hk,n\overline{R}\_{k}={1\over k}\sum\_{j=1}^{k}R\_{j,k}^{-1/H\_{k,n}}.

Example: Flood Risk Pooling in Europe. Prettenthaler et al. [[62](https://arxiv.org/html/2511.22272v1#bib.bib62)] discussed some challenges in insuring flood risk in Europe and analyzed (insured) flood loss data
across Europe (provided by MunichRe NatCatSERVICE), transformed into
losses expressed as a percentage of building stock value. Here we present results for the
aggregate annual losses for the period 1980–2013 for Germany. While the Pareto QQ-plot starts off linearly, truncation starts to set in at the top 15 data. Based on ([4](https://arxiv.org/html/2511.22272v1#S3.E4 "In 3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")), the truncated Pareto QQ-plot

|  |  |  |
| --- | --- | --- |
|  | {(−log⁡(D^T+jn+1),log⁡X(n−j+1))}j=1n\left\{\left(-\log\left(\hat{D}\_{T}+{j\over n+1}\right),\log X\_{(n-j+1)}\right)\right\}\_{j=1}^{n} |  |

is expected to be linear at the top data under truncation. Here the endpoint is estimated at T^=0.28%\hat{T}=0.28\%.

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2: Pareto QQ-plot (left) and truncated Pareto QQ-plot (right) for German flood loss data.

### 3.2 Tempering

An alternative way to incorporate that the power-law behaviour does not extend indefinitely is assuming tapering effects. In that case, the distribution tail eventually decays more quickly than according to the power-law, representing a kind of interpolation between the truncated and non-truncated case. Inspired by applications in geophysics and finance, Meerschaert et al. [[54](https://arxiv.org/html/2511.22272v1#bib.bib54)] discussed parameter estimation under exponential tempering of a simple Pareto law with survival function

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(X>x)=c​x−α​e−β​x,\displaystyle{P}(X>x)=cx^{-\alpha}e^{-\beta x}, |  | (5) |

where α,β>0\alpha,\beta>0 and c>0c>0 is a scale parameter.222Note here that for such tempered distributions the extreme value index equals 0 and not 1/α1/\alpha, and hence we prefer not to use the notation 1/ξ1/\xi for α\alpha in this subsection in order to avoid confusion.
In the context of insurance data, Raschke [[64](https://arxiv.org/html/2511.22272v1#bib.bib64)] recently discussed the use of the more general Weibull tempering of a simple power law with survival function

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(X>x)=c​x−α​e−(β​x)τ,\displaystyle{P}(X>x)=cx^{-\alpha}e^{-(\beta x)^{\tau}}, |  | (6) |

with c,α,β,τ>0c,\alpha,\beta,\tau>0. The generalization to the Pareto-type case was provided in Albrecher et al. [[4](https://arxiv.org/html/2511.22272v1#bib.bib4)].

Assume X=min⁡(W,Y)X=\min(W,Y) with WW and YY independent, where WW is Pareto-type distributed and

|  |  |  |
| --- | --- | --- |
|  | P​(Y>x)=e−(β​x)τ,x>0.\displaystyle{P}(Y>x)=e^{-(\beta x)^{\tau}},\quad x>0. |  |

Then for some slowly varying function ℓ\ell

|  |  |  |
| --- | --- | --- |
|  | P​(X>x)=x−α​ℓ​(x)​e−(β​x)τ.\displaystyle{P}(X>x)=x^{-\alpha}\ell(x)e^{-(\beta x)^{\tau}}. |  |

Using POT modelling with t​βt→β∞>0t\beta\_{t}\to\beta\_{\infty}>0
for x>1x>1 as t→∞t\to\infty leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(X/t>x​∣X>​t)\displaystyle{P}\left({X/t}>x\mid X>t\right) | =(t​x)−αt−α​ℓ​(x​t)ℓ​(t)​e−(βt​x​t)τe−(βt​t)τ\displaystyle=\frac{(tx)^{-\alpha}}{t^{-\alpha}}\frac{\ell(xt)}{\ell(t)}\frac{e^{-(\beta\_{t}xt)^{\tau}}}{e^{-(\beta\_{t}t)^{\tau}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x−α​ℓ​(x​t)ℓ​(t)​e−(βt​t)τ​(xτ−1)\displaystyle=x^{-\alpha}\frac{\ell(xt)}{\ell(t)}e^{-(\beta\_{t}t)^{\tau}(x^{\tau}-1)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →x−α​e−β∞τ​(xτ−1).\displaystyle\to x^{-\alpha}e^{-\beta\_{\infty}^{\tau}(x^{\tau}-1)}. |  |

Hence, the following POT approximation will be used, assuming
t​βt→β∞>0t\beta\_{t}\to\beta\_{\infty}>0 and λ=β∞τ\lambda=\beta\_{\infty}^{\tau}:

|  |  |  |
| --- | --- | --- |
|  | P​(X/t>y​∣X>​t)≈x−α​e−λ​(xτ−1).{P}(X/t>y\mid X>t)\approx x^{-\alpha}e^{-\lambda(x^{\tau}-1)}. |  |

Maximum likelihood estimators for ξ,λ,τ\xi,\lambda,\tau using POTs Rj,k=X(n−j+1)/X(n−k)R\_{j,k}=X\_{(n-j+1)}/X\_{(n-k)}, j=1,…,kj=1,\ldots,k are then obtained from

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡L​(α,λ,τ)\displaystyle\hskip-28.45274pt\log L(\alpha,\lambda,\tau) | =\displaystyle= | −(1+α)​∑j=1klog⁡Rj,k−λ​∑j=1k(Rj,kτ−1)\displaystyle-\left(1+\alpha\right)\sum\_{j=1}^{k}\log R\_{j,k}-\lambda\sum\_{j=1}^{k}\left(R\_{j,k}^{\tau}-1\right) |  |
|  |  |  | +∑j=1klog⁡(α+λ​τ​Rj,kτ).\displaystyle+\sum\_{j=1}^{k}\log\left(\alpha+\lambda\tau R\_{j,k}^{\tau}\right). |  |

Another possible approach focuses on the goodness-of-fit of the tempering model to the POT data above the different thresholds X(n−k)X\_{(n-k)},
using a QQ-plot approach. Then, for a given value of τ\tau, one finds the least-squares line through the points

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(−log⁡{1−F^k​(Rj,k)},α​log⁡Rj,k+τ​β∞τ​hτ​(Rj,k))}j=1k,\left\{\left(-\log\{1-\hat{F}\_{k}(R\_{j,k})\},\alpha\log R\_{j,k}+\tau\beta\_{\infty}^{\tau}h\_{\tau}(R\_{j,k})\right)\right\}\_{j=1}^{k}, |  | (7) |

where hτ​(x)=(xτ−1)/τh\_{\tau}(x)=(x^{\tau}-1)/\tau and F^k\hat{F}\_{k} denotes the empirical distribution function based on Rj,kR\_{j,k}, for j=1,…,kj=1,\ldots,k. Therefore, since 1−F^k​(Rj,k)=(k−j+1)/(k+1)1-\hat{F}\_{k}\left(R\_{j,k}\right)=(k-j+1)/(k+1), one is led to minimize the weighted least squares

|  |  |  |
| --- | --- | --- |
|  | WLS​(Rj,k;αk,δk,τk):=∑j=1kwj,k​{1α​log⁡k+1k−j+1−log⁡Rj,k−δ​hτ​(Rj,k)}2\displaystyle\mbox{WLS}(R\_{j,k};\alpha\_{k},\delta\_{k},\tau\_{k}):=\sum\_{j=1}^{k}w\_{j,k}\left\{\frac{1}{\alpha}\log\frac{k+1}{k-j+1}-\log R\_{j,k}-\delta h\_{\tau}\left(R\_{j,k}\right)\right\}^{2} |  |

with respect to α\alpha and δ=τ​β∞τ/α\delta=\tau\beta\_{\infty}^{\tau}/\alpha, where {wj,k,j=1,…,k}\{w\_{j,k},j=1,\ldots,k\} are appropriate weights. In particular, if wj,k=1/log⁡{(k+1)/(k−j+1)}w\_{j,k}=1/\log\{(k+1)/(k-j+1)\} when δ↓0\delta\downarrow 0, i.e. without tempering, we recover the classical Hill estimator Hk,nH\_{k,n}. Optimization of WLS also leads to an adaptive selection method for choosing kk which gives appropriate estimates for (α,τ,β∞)(\alpha,\tau,\beta\_{\infty}), choosing the kk for which the WLS value is minimal.

To estimate return periods of the type 1/P​(X>c)1/{P}(X>c) for some large outcome level cc, one can use the approximation

|  |  |  |
| --- | --- | --- |
|  | P​(X>t​x)P​(X>t)≈x−α​e−λ​τ​hτ​(x)\frac{{P}(X>tx)}{{P}(X>t)}\approx x^{-\alpha}e^{-\lambda\tau h\_{\tau}(x)} |  |

with tt large. Setting t​x=ctx=c and t=X(n−k)t=X\_{(n-k)} for some kk yields an estimator for P​(X>c){P}(X>c):

|  |  |  |
| --- | --- | --- |
|  | P^c,k=k+1n+1​(cX(n−k))−α^k​exp⁡{−λ^k​τ^k​hτ^k​(cX(n−k))},\hat{P}\_{c,k}={k+1\over n+1}\left({c\over X\_{(n-k)}}\right)^{-\hat{\alpha}\_{k}}\exp\left\{-\hat{\lambda}\_{k}\hat{\tau}\_{k}h\_{\hat{\tau}\_{k}}\left({c\over X\_{(n-k)}}\right)\right\}, |  |

where α^k,τ^k,λ^k\hat{\alpha}\_{k},\hat{\tau}\_{k},\hat{\lambda}\_{k} denote the estimators of these parameters based on the yop kk observations.
The value c=Q^p,kWc=\hat{Q}^{W}\_{p,k} solving the equation

|  |  |  |
| --- | --- | --- |
|  | k+1n+1​(cX(n−k))−α^k​exp⁡{−λ^k​τ^k​hτ^k​(cX(n−k))}=p,{k+1\over n+1}\left({c\over X\_{(n-k)}}\right)^{-\hat{\alpha}\_{k}}\exp\left\{-\hat{\lambda}\_{k}\hat{\tau}\_{k}h\_{\hat{\tau}\_{k}}\left({c\over X\_{(n-k)}}\right)\right\}=p, |  |

for a given value p≤1/np\leq{1/n} then is an estimator for an extreme quantile or return level Q​(1−p)=VaR1−pQ(1-p)=\text{VaR}\_{1-p} of XX.

Example: Norwegian Fire Insurance Data. Here, we analyze the Norwegian fire insurance data as discussed in Albrecher et al. [[4](https://arxiv.org/html/2511.22272v1#bib.bib4)]. Figure [3](https://arxiv.org/html/2511.22272v1#S3.F3 "Figure 3 ‣ 3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") depicts the Pareto and Weibull QQ-plots (the latter for the 100 largest data points). The Pareto QQ-plot becomes concave near the top points where a Weibull model appears to fit. Hence this data set is a candidate for the proposed tempering model. In Figure [3](https://arxiv.org/html/2511.22272v1#S3.F3 "Figure 3 ‣ 3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") (bottom), we present the plot of the points in ([7](https://arxiv.org/html/2511.22272v1#S3.E7 "In 3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")) with α^=1.19928,β^∞=0.003958,τ^=0.70227\hat{\alpha}=1.19928,\,\hat{\beta}\_{\infty}=0.003958,\,\hat{\tau}=0.70227 obtained at the optimal value k^=4920\hat{k}=4920, which is linear overall.

![Refer to caption](x5.png)   ![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 3: QQ-plots for Norwegian fire claims for Pareto, Weibull and tempering fit using the points in ([7](https://arxiv.org/html/2511.22272v1#S3.E7 "In 3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")) .

## 4 Censoring

In various lines of insurance business (so-called long-tailed business) one faces long periods until claim sizes are finally settled, e.g., in liability lines. At the time of the evaluation of the portfolio, a proportion of the claims are not fully dealt with yet, and hence the real cumulative
payments are unknown and censored by the payments up to evaluation. Censoring can also be due to policy limits which conceal the real underlying loss amounts. When using extreme value techniques in the risk assessment, it is important to take these censoring mechanisms into account in an appropriate way.

To formalize such a setting, let us assume that the loss random variable XX of interest is Pareto-type distributed with extreme value index ξ>0\xi>0, and let CC be a censoring random variable that is also Pareto-type distributed, possibly with a different extreme value index. One considers Z=min⁡(X,C)Z=\min(X,C) and an indicator δ=𝕀​(X≤C)\delta={\mathbb{I}}(X\leq C) which equals 1 if the observation ZZ is non-censored.
  
Let the ordered ZZ-observations and the corresponding δ\delta-values be denoted by {(Z(i),δ(i))}i=1n\{(Z\_{(i)},\delta\_{(i)})\}\_{i=1}^{n}. Then, based on the POT principle, the classical censoring likelihood based on the relative excesses Rj,k=Z(n−j+1)/Z(n−k)R\_{j,k}=Z\_{(n-j+1)}/Z\_{(n-k)}, j=1,…,kj=1,\ldots,k is given by

|  |  |  |
| --- | --- | --- |
|  | ∏j=1k(ξ−1​Rj,k−ξ−1−1)δ(n−j)​(Rj,k−ξ−1)1−δ(n−j+1).\prod\_{j=1}^{k}(\xi^{-1}R\_{j,k}^{-\xi^{-1}-1})^{\delta\_{(n-j)}}(R\_{j,k}^{-\xi^{-1}})^{1-\delta\_{(n-j+1)}}. |  |

Optimizing with respect to ξ\xi leads to the following Hill-type estimator adapted for censoring:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hk,n(c)=k−1​∑j=1klog⁡(Z(n−j+1)/Z(n−k))k−1​∑j=1kδ(n−j+1).H\_{k,n}^{(c)}=\frac{k^{-1}\sum\_{j=1}^{k}\log\left(Z\_{(n-j+1)}/Z\_{(n-k)}\right)}{k^{-1}\sum\_{j=1}^{k}\delta\_{(n-j+1)}}. |  | (8) |

This estimator equals the original Hill estimator based on the ZZ-observations, divided by the proportion of non-censored data among the top kk observations.
  
In case of random right-censoring, and assuming independence of the XX and CC sequences, the Kaplan–Meier product-limit estimator F^n\hat{F}\_{n} is the nonparametric maximum likelihood estimator of the distribution function of XX, given for all x∈(0,∞)x\in(0,\infty) by

|  |  |  |
| --- | --- | --- |
|  | 1−F^n​(x)=∏i=1n(1−𝕀​(Z(i)≤x)n−i+1)δ(i).1-\hat{F}\_{n}(x)=\prod\_{i=1}^{n}\left(1-\frac{\mathbb{I}(Z\_{(i)}\leq x)}{n-i+1}\right)^{\delta\_{(i)}}. |  |

Beirlant et al. [[19](https://arxiv.org/html/2511.22272v1#bib.bib19)] showed that Hk,n(c)H\_{k,n}^{(c)} can also be obtained as a slope estimator of the
Pareto QQ-plot adapted for censoring, featuring the points

|  |  |  |
| --- | --- | --- |
|  | {(−log⁡{1−F^​(Z(n−j+1))},log⁡Z(n−j+1))}j=1n.\left\{(-\log\{1-\hat{F}(Z\_{(n-j+1)})\},\log Z\_{(n-j+1)})\right\}\_{j=1}^{n}. |  |

Worms and Worms [[78](https://arxiv.org/html/2511.22272v1#bib.bib78)] proposed

|  |  |  |
| --- | --- | --- |
|  | ξ^kW=∑j=1kF^n​(Z(n−j+1))F^n​(Z(n−k))​(log⁡Z(n−j+1)−log⁡Z(n−j))\hat{\xi}\_{k}^{W}=\sum\_{j=1}^{k}\frac{\hat{F}\_{n}(Z\_{(n-j+1)})}{\hat{F}\_{n}(Z\_{(n-k)})}\left(\log Z\_{(n-j+1)}-\log Z\_{(n-j)}\right) |  |

as an estimator of ∫1∞F¯​(u​t)/F¯​(t)​d​(log⁡u)→ξ\int\_{1}^{\infty}{\overline{F}(ut)}/{\overline{F}(t)}\mathop{}\!\mathrm{d}(\log u)\to\xi as t→∞t\to\infty, with FF denoting the distribution function of XX.
[[35](https://arxiv.org/html/2511.22272v1#bib.bib35)] obtained a moment estimator ξ^kM\hat{\xi}\_{k}^{M} under censoring by simple division of the moment estimator by k−1​∑j=1kδ(n−j+1)k^{-1}\sum\_{j=1}^{k}\delta\_{(n-j+1)}. This estimator is then consistent, not only for Pareto-type distributions, but for FF belonging to any max-domain of attraction. They also provided the first asymptotic results for the available estimator, while Beirlant et al. [[21](https://arxiv.org/html/2511.22272v1#bib.bib21)] provided asymptotic results for a version close to ξ^kW\hat{\xi}\_{k}^{W}. Other estimators were proposed in Bladt et al. [[23](https://arxiv.org/html/2511.22272v1#bib.bib23)]. Recently, Bladt and Rodionov [[25](https://arxiv.org/html/2511.22272v1#bib.bib25)] proposed the analysis of integrals based on the product-limit
estimator of normalized top-order statistics. These integrals allow to derive asymptotic distributional properties, offering an alternative approach to
conventional plug-in estimation methods.

The available estimators tend to have a larger bias that increases with the proportion of intermediate data that are censored. Bias-reduced methods are proposed in Beirlant et al. [[17](https://arxiv.org/html/2511.22272v1#bib.bib17), [20](https://arxiv.org/html/2511.22272v1#bib.bib20)] and Bladt et al. [[23](https://arxiv.org/html/2511.22272v1#bib.bib23)], among others.

When censoring occurs due to long development times so that the final claim amount of a larger proportion of claims is underestimated at the evaluation time of the portfolio, caution is advised when using the available asymptotic normality results since the independence of XX and CC can not be taken for granted. Indeed, larger claims have a larger probability of being censored due to a longer development time. Stupfler [[73](https://arxiv.org/html/2511.22272v1#bib.bib73)] is a first paper to address this issue.

Extreme quantile estimators have been proposed in several of the abovementioned papers adapting the Weissman [[77](https://arxiv.org/html/2511.22272v1#bib.bib77)] estimator to the censoring case:

|  |  |  |
| --- | --- | --- |
|  | Q^k(c)​(1−p)=Z(n−k)​{1−F^n​(Z(n−k))p}ξ^k(c),\hat{Q}\_{k}^{(c)}(1-p)=Z\_{(n-k)}\left\{{1-\hat{F}\_{n}(Z\_{(n-k)})\over p}\right\}^{\hat{\xi}\_{k}^{(c)}}, |  |

where ξ^k(c)\hat{\xi}\_{k}^{(c)} denotes any of the extreme value index estimators discussed above.

Example: Censored Liability Loss Data. Goegebeur et al. [[42](https://arxiv.org/html/2511.22272v1#bib.bib42)] discussed the (Loss, ALAE) data set from the R package copula containing 1500 general liability claims with indemnity claims (Loss) and allocated loss adjustment expense (ALAE) related to the settlement of individual claims, such as expenses for lawyers or claim investigations. One finds that 34 observations have censored losses. In Figure [4](https://arxiv.org/html/2511.22272v1#S4.F4 "Figure 4 ‣ 4 Censoring ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), the data are plotted with the censored data in blue. Figure [5](https://arxiv.org/html/2511.22272v1#S4.F5 "Figure 5 ‣ 4 Censoring ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") displays Hk,n(c)H\_{k,n}^{(c)} (solid bold line), ξ^kW\hat{\xi}\_{k}^{W} (dashed line) and ξ^kM\hat{\xi}\_{k}^{M} (dotted line) as a function of kk. These estimates indicate a heavy tail with an extreme value index ranging between 0.5 and 1. ξ^kW\hat{\xi}\_{k}^{W} appears to suffer substantial bias which only decreases with smaller kk.

![Refer to caption](x8.png)

Figure 4: Loss versus ALAE data. Original scale (left) and log\log-scale (right).



![Refer to caption](x9.png)

Figure 5: Loss data: Comparison of extreme value index estimators Hk,n(c)H\_{k,n}^{(c)}, ξ^kW\hat{\xi}\_{k}^{W}, and ξ^kM\hat{\xi}\_{k}^{M} as a function of kk.

In cases with a high percentage of right-censored data, one can also rely on available expert information for the censored observations. This setting arises for instance for liability insurance claims, where actuarial experts build reserves based on the specificity of each open claim. These reserves can be used to improve estimation based on the already available data points from closed claims. The incorporation of expert opinion is discussed in Bladt et al. [[22](https://arxiv.org/html/2511.22272v1#bib.bib22)]. Albrecher and Bladt [[6](https://arxiv.org/html/2511.22272v1#bib.bib6)] extend the statistical censoring setup to the situation when
random measures can be assigned to the realization of datapoints, leading to a
new way of incorporating expert information into the usual parametric estimation
procedures. In some types of insurance, such as motor third-party liability insurance and both
worker’s compensation and loss of income coverage, claims might potentially reopen.
Bladt and Furrer [[24](https://arxiv.org/html/2511.22272v1#bib.bib24)] propose adaptations to the Kaplan–Meier function in order to incorporate such contaminations.

## 5 Full Models for Claims

Actuaries use models for claim sizes to set premiums,
calculate risk measures and determine capital requirements for solvency regulations. Extreme value models, based for instance on the generalized Pareto distribution, are not able to capture the characteristics over the entire range of the loss distribution, which makes them unsuitable as a global model. It is often imperative to obtain
an overall fit for the distribution of losses, for example in a risk analysis where the focus is
not only on extreme events, or when setting up a reinsurance program. Instead of trying
many different standard distributions, splicing two distributions (Klugman et al. [[48](https://arxiv.org/html/2511.22272v1#bib.bib48)]) is
often more suitable to model the complete loss distribution. In the literature, a splicing model is
also called a composite model. We hereby combine an analytically tractable (typically light-tailed) distribution for the body
which covers small and moderate losses (the so-called losses!attritional), with a heavy-tailed
distribution for the tail to capture the losses!large. In the actuarial literature, simple splicing
models have been proposed. Beirlant et al. [[18](https://arxiv.org/html/2511.22272v1#bib.bib18)] and Klugman et al. [[48](https://arxiv.org/html/2511.22272v1#bib.bib48)] consider the
splicing of the exponential distribution with the Pareto distribution. Other distributions
for the body such as the Weibull distribution (Ciumara [[30](https://arxiv.org/html/2511.22272v1#bib.bib30)]; Scollnik and Sun [[69](https://arxiv.org/html/2511.22272v1#bib.bib69)]) or
the lognormal distribution (Cooray and Ananda [[31](https://arxiv.org/html/2511.22272v1#bib.bib31)]; Scollnik [[68](https://arxiv.org/html/2511.22272v1#bib.bib68)]; Pigeon and Denuit [[59](https://arxiv.org/html/2511.22272v1#bib.bib59)]) have also been used. Nadarajah and Bakar [[58](https://arxiv.org/html/2511.22272v1#bib.bib58)], Bakar et al. [[14](https://arxiv.org/html/2511.22272v1#bib.bib14)], and Calderín-Ojeda and Kwok [[28](https://arxiv.org/html/2511.22272v1#bib.bib28)] investigate the splicing of the log-normal or Weibull distribution
with various tail distributions. Lee et al. [[50](https://arxiv.org/html/2511.22272v1#bib.bib50)] consider the splicing of a mixture of two exponentials and the GP distribution. The use of a mixture model in the first splicing component
gives more flexibility in modelling the small and moderate losses, see Fackler [[38](https://arxiv.org/html/2511.22272v1#bib.bib38)]. For a splicing approach to model cyber risk data, see, e.g., [[36](https://arxiv.org/html/2511.22272v1#bib.bib36)].

Rather than a complex search for appropriate splicing combinations of extreme and attritional models, Reynkens et al. [[65](https://arxiv.org/html/2511.22272v1#bib.bib65)] proposed a semi-automatic method for splicing, a mixed Erlang (ME)
with density

|  |  |  |
| --- | --- | --- |
|  | fME​(x;𝐫,α,λ)=∑j=1Mαj​λrj(rj−1)!​xrj−1​e−λ​x,x>0f\_{\text{ME}}(x;{\bf r},{\bf\alpha},\lambda)=\sum\_{j=1}^{M}\alpha\_{j}{\lambda^{r\_{j}}\over(r\_{j}-1)!}x^{r\_{j}-1}e^{-\lambda x},\,x>0 |  |

and integer parameters 𝐫=(r1,…,rM){\bf r}=(r\_{1},\ldots,r\_{M}) with r1<⋯<rMr\_{1}<\cdots<r\_{M}, and
an extreme value model such as a Pareto, generalized Pareto, or even truncated or tempered versions of those. Here, (α1,…,αM)(\alpha\_{1},\ldots,\alpha\_{M}) with αj>0\alpha\_{j}>0 and ∑j=1Mαj=1\sum\_{j=1}^{M}\alpha\_{j}=1 are the weights in the Erlang mixture.
The class of mixtures of Erlang distributions with a common scale 1/λ1/\lambda is dense in the space of distributions on ℝ+\mathbb{R}^{+}, and it is closed under mixtures, convolution and compounding. Hence aggregate risk calculations are simple, and XL premiums and risk measures based on quantiles can also be evaluated in a rather straightforward way. For instance, a composite ME-generalized Pareto distribution for some 0<π<10<\pi<1 has density

|  |  |  |
| --- | --- | --- |
|  | fME,GP​(x)={π​fME​(x;𝐫,α,λ)FME​(t;𝐫,α,λ),0<x≤t,(1−π)​1σ​{1+ξσ​(x−t)}−1−1/ξ,x>t,f\_{\text{ME,GP}}(x)=\left\{\begin{array}[]{ll}\pi\frac{f\_{\text{ME}}(x;{\bf r},{\bf\alpha},\lambda)}{F\_{\text{ME}}(t;{\bf r},{\bf\alpha},\lambda)},&0<x\leq t,\\ (1-\pi){1\over\sigma}\left\{1+{\xi\over\sigma}(x-t)\right\}^{-1-1/\xi},&x>t,\end{array}\right. |  |

and survival function

|  |  |  |
| --- | --- | --- |
|  | 1−FME,GP​(x)={1−π​FME​(x;𝐫,α,λ)FME​(t;𝐫,α,λ),0<x≤t,(1−π)​{1+ξσ​(x−t)}−1/ξ,x>t.1-F\_{\text{ME,GP}}(x)=\left\{\begin{array}[]{ll}1-\pi\frac{F\_{\text{ME}}(x;{\bf r},{\bf\alpha},\lambda)}{F\_{\text{ME}}(t;{\bf r},{\bf\alpha},\lambda)},&0<x\leq t,\\ (1-\pi)\left\{1+{\xi\over\sigma}(x-t)\right\}^{-1/\xi},&x>t.\end{array}\right. |  |

Fitting ME distributions through direct likelihood maximization is difficult. Lee and Lin [[51](https://arxiv.org/html/2511.22272v1#bib.bib51)] use the Expectation-Maximization (EM) algorithm proposed by Dempster et al. [[33](https://arxiv.org/html/2511.22272v1#bib.bib33)] to fit the ME distribution. Model selection criteria, such as the AIC and BIC information criteria, are then used to avoid overfitting. Verbelen et al. [[74](https://arxiv.org/html/2511.22272v1#bib.bib74)] extend this approach to censored and/or truncated data.

Rather than proposing a data-driven estimator of the splicing point tt, one can use an expert opinion on the splicing point tt based on EVA as outlined above. Then, π\pi can be estimated by the fraction of the data not larger than tt. The extreme value index ξ\xi is estimated in the algorithm, starting from the value obtained from the EVA at the threshold tt. The final estimates for ξ\xi turn out to be close to the EVA estimates. Next, the ME parameters (α,λ)(\alpha,\lambda) are estimated using the EM algorithm, cf. [[74](https://arxiv.org/html/2511.22272v1#bib.bib74)]. The number of ME components MM is estimated using a backward stepwise search, starting from a certain upper value, whereby the smallest shape is deleted if this decreases an information criterion such as AIC or BIC. Moreover, for each value of MM, the shapes 𝐫{\bf r} are adjusted based on maximising the likelihood starting from 𝐫=(s,2​s,…,M​s){\bf r}=(s,2s,\ldots,M\,s), where ss is a chosen spread.

Example: Censored Liability Loss Data. We continue the analysis of the Loss variable from the (Loss, ALAE) data set considered above. To search for splicing points, estimates of the mean excess function

|  |  |  |
| --- | --- | --- |
|  | e​(x):=E​(X−x​∣X>​x)=∫x∞F¯​(u)​d​uF¯​(x)e(x):={E}\left(X-x\mid X>x\right)={\int\_{x}^{\infty}\overline{F}(u)\mathop{}\!\mathrm{d}{u}\over\overline{F}(x)} |  |

are found to be useful. Substituting F¯\overline{F} with the Kaplan–Meier survival function leads to an estimator e^nKM​(x)\hat{e}\_{n}^{\text{KM}}(x) as a function of xx, displayed in Figure [6](https://arxiv.org/html/2511.22272v1#S5.F6 "Figure 6 ‣ 5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") (left). A concave increase appears to change into a linear pattern, starting at a threshold level around 10510^{5}.

In Figure [6](https://arxiv.org/html/2511.22272v1#S5.F6 "Figure 6 ‣ 5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") (right), the QQ-plot is given with the Kaplan–Meier quantiles set out against the quantiles of the fitted ME-Pareto splicing model. The splicing point is taken at the 50th largest observation, leading to a good fit with ξ^=0.67\hat{\xi}=0.67 and three ME components.

![Refer to caption](x10.png)
    
![Refer to caption](x11.png)

Figure 6: Loss variable from (Loss, ALAE) data set. Mean excess function e^nKM\hat{e}\_{n}^{\text{KM}} (left) and splicing QQ-plot (right).

When estimating VaR1−p\mbox{VaR}\_{1-p} for a two-component spliced distribution, we have

|  |  |  |
| --- | --- | --- |
|  | Q​(1−p)={Q1​((1−p)/π),if ​0≤p≤π,Q2​((1−p−π)/(1−π))=Q2​(1−p1−π),if ​π<p≤1,Q(1-p)=\begin{cases}Q\_{1}((1-p)/\pi),&\quad\text{if }0\leq p\leq\pi,\\ Q\_{2}((1-p-\pi)/(1-\pi))=Q\_{2}\left(1-{p\over 1-\pi}\right),&\quad\text{if }\pi<p\leq 1,\end{cases} |  |

where Q1Q\_{1} denotes the quantile function of the ME component and Q2Q\_{2} of the tail component. Q1Q\_{1} can be obtained numerically.
Taking t=X(n−k)t=X\_{(n-k)} and 1−π=(k+1)/(n+1)1-\pi=(k+1)/(n+1),
we are led to the appropriate extreme quantile estimator as discussed above, when π<p≤1\pi<p\leq 1.

When estimating Π​(u)\Pi(u) as defined in ([1](https://arxiv.org/html/2511.22272v1#S2.E1 "In 2nd item ‣ 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")), we again identify two cases: u≤t=X(n−k)u\leq t=X\_{(n-k)}, or u>t=X(n−k)u>t=X\_{(n-k)} in which case statistics of extremes can be used. When u>tu>t, then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Π​(u)\displaystyle\Pi(u) | =\displaystyle= | ∫u∞[1−{π+(1−π)​F2​(z)}]​d​z\displaystyle\int\_{u}^{\infty}[1-\{\pi+(1-\pi)F\_{2}(z)\}]\mathop{}\!\mathrm{d}{z} |  |
|  |  | =\displaystyle= | (1−π)∫u∞{1−F2(z)}dz=:(1−π)Π2(u).\displaystyle(1-\pi)\int\_{u}^{\infty}\{1-F\_{2}(z)\}\mathop{}\!\mathrm{d}{z}=:(1-\pi)\Pi\_{2}(u). |  |

When u<tu<t, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(u)\displaystyle\Pi(u) | =∫ut{1−π​F1​(z)}​d​z+∫t+∞[1−{π+(1−π)​F2​(z)}]​d​z\displaystyle=\int\_{u}^{t}\{1-\pi F\_{1}(z)\}\mathop{}\!\mathrm{d}{z}+\int\_{t}^{+\infty}[1-\{\pi+(1-\pi)F\_{2}(z)\}]\mathop{}\!\mathrm{d}{z} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(t−u)−π​∫utF1​(z)​d​z+(1−π)​∫t+∞{1−F2​(z)}​d​z\displaystyle=(t-u)-\pi\int\_{u}^{t}F\_{1}(z)\mathop{}\!\mathrm{d}{z}+(1-\pi)\int\_{t}^{+\infty}\{1-F\_{2}(z)\}\mathop{}\!\mathrm{d}{z} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(t−u)−(t−u)​π+π​∫ut{1−F1​(z)}​d​z+(1−π)​Π2​(t)\displaystyle=(t-u)-(t-u)\pi+\pi\int\_{u}^{t}\{1-F\_{1}(z)\}\mathop{}\!\mathrm{d}{z}+(1-\pi)\Pi\_{2}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−π)​(t−u)+π​Π1​(u)+(1−π)​Π2​(t).\displaystyle=(1-\pi)(t-u)+\pi\Pi\_{1}(u)+(1-\pi)\Pi\_{2}(t). |  |

Let tlt^{l} denote the lower limit of the support of the distribution of XX, and TT the upper limit.
For the ME distribution, we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Π1​(u)\displaystyle\Pi\_{1}(u) | =\displaystyle= | ∫ut{1−F1∗​(z)−F1∗​(tl)F1∗​(t)−F1∗​(tl)}​d​z\displaystyle\int\_{u}^{t}\left\{1-\frac{F\_{1}^{\*}(z)-F\_{1}^{\*}(t^{l})}{F\_{1}^{\*}(t)-F\_{1}^{\*}(t^{l})}\right\}\mathop{}\!\mathrm{d}{z} |  |
|  |  | =\displaystyle= | {F1∗​(t)−1}​(t−u)+{Π1∗​(u)−Π1∗​(t)}F1∗​(t)−F1∗​(tl),\displaystyle\frac{\left\{F\_{1}^{\*}(t)-1\right\}(t-u)+\{\Pi\_{1}^{\*}(u)-\Pi\_{1}^{\*}(t)\}}{F\_{1}^{\*}(t)-F\_{1}^{\*}(t^{l})}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | F1∗​(x)=∑j=1Mαj​(1−∑n=0rj−1e−λ​x​(λ​x)nn!)F\_{1}^{\*}(x)=\sum\_{j=1}^{M}\alpha\_{j}\left(1-\sum\_{n=0}^{r\_{j}-1}e^{-\lambda x}{(\lambda x)^{n}\over n!}\right) |  |

and, assuming that rn=nr\_{n}=n for n=1,…,Mn=1,\ldots,M,

|  |  |  |
| --- | --- | --- |
|  | Π1∗​(u)=1λ​e−λ​u​∑n=0M−1∑k=nM−1(∑j=k+1Mαj)​(λ​u)nn!.\Pi^{\*}\_{1}(u)={1\over\lambda}e^{-\lambda u}\sum\_{n=0}^{M-1}\sum\_{k=n}^{M-1}\left(\sum\_{j=k+1}^{M}\alpha\_{j}\right)\frac{(\lambda u)^{n}}{n!}. |  |

For Π2​(u)\Pi\_{2}(u) in case u>t=X(n−k)u>t=X\_{(n-k)}, see for instance Goegebeur et al. [[44](https://arxiv.org/html/2511.22272v1#bib.bib44)] for censored data.
More recent papers on splicing methods are Li and Liu [[53](https://arxiv.org/html/2511.22272v1#bib.bib53)], Bladt and Yslas [[26](https://arxiv.org/html/2511.22272v1#bib.bib26)], Poudyal and Brazauskas [[60](https://arxiv.org/html/2511.22272v1#bib.bib60)], Wang et al. [[76](https://arxiv.org/html/2511.22272v1#bib.bib76)], Raschke [[64](https://arxiv.org/html/2511.22272v1#bib.bib64)], Wang and Hobæk-Haff [[75](https://arxiv.org/html/2511.22272v1#bib.bib75)], Bolviken and Hobæk-Haff [[27](https://arxiv.org/html/2511.22272v1#bib.bib27)], Fung et al. [[40](https://arxiv.org/html/2511.22272v1#bib.bib40)] and Ghaddab et al. [[41](https://arxiv.org/html/2511.22272v1#bib.bib41)].

While the splicing approach allows to disentangle the fitting of the tail and the body of the claim size distribution, it may not seem natural to glue together two (or even more) different distributions. Also, the choice of the splicing point tt, where one transits from one ‘regime’ to another remains somewhat arbitrary. At the same time, flexible and mathematically tractable families of distributions like phase-type distributions (of which the ME family above is a special case) are not well-suited for heavy tails because their tail is exponentially bounded and many components in the mixture (i.e. a high phase-type dimension) would be needed to provide reasonable fits for higher quantiles, and even then the tail behavior is not naturally captured (which is one reason why the ME above is not used for the entire range of the distribution). Another recent alternative that circumvents the threshold choice of splicing is the class of matrix-Mittag–Leffler distributions and its power transforms, cf. Albrecher et al. [[7](https://arxiv.org/html/2511.22272v1#bib.bib7)]. This class results from inhomogeneous phase-type distributions and can be seen as transforms of matrix-exponential distributions leading to heavy tails, essentially comprising Mittag–Leffler distributions with matrix-valued parameters. In this way, one avoids the need for an increased number of parameters to compensate for too light tails with yet tractable expressions for both the fitting and subsequent calculations. The quality of the resulting fit across the entire range of the distribution can be quite remarkable, see Albrecher et al. [[7](https://arxiv.org/html/2511.22272v1#bib.bib7)] and Bladt and Yslas [[26](https://arxiv.org/html/2511.22272v1#bib.bib26)] for details.

## 6 Regression Modelling

In recent years, advanced data collection and storage techniques and practices have significantly increased the potential for relevant covariate information for the occurrence of extremes. This is of course also very relevant for insurance applications. We focus here on adaptations of techniques for censored data when covariate information is available. Regression modelling of a censored random variable YY as a function of a covariate xx is available at specific covariate values using local smoothing methods. For instance, Albrecher et al. [[5](https://arxiv.org/html/2511.22272v1#bib.bib5), Sec. 4.4.3] propose extensions of the above univariate estimation methods under random right censoring, based on the Akritas–Van Keilegom [[2](https://arxiv.org/html/2511.22272v1#bib.bib2)] extension of the Kaplan–Meier estimator. They use this method to model the extremes of final claim payments in a long-tailed portfolio as a function of the number of development years. In this way, a positive dependence between development times and heaviness of the tail can be detected.

Considering a univariate covariate XX with a specific value xx, and assuming that YY and the censoring variable CC are conditionally independent given XX, we have

|  |  |  |
| --- | --- | --- |
|  | 1−F^Y|X​(y∣x)=∏Zi≤y(1−Wi​(x;h)∑j=1nWj​(x;h)​𝕀​(Zj≥Zi))δi1-\hat{F}\_{Y|X}(y\mid x)=\prod\_{Z\_{i}\leq y}\left(1-\frac{W\_{i}(x;h)}{\sum\_{j=1}^{n}W\_{j}(x;h)\mathbb{I}(Z\_{j}\geq Z\_{i})}\right)^{\delta\_{i}} |  |

with weights

|  |  |  |
| --- | --- | --- |
|  | Wi​(x;h)={K​(x−xih)/∑δj=1K​(x−xjh),if ​δi=1,0,if ​δi=0,W\_{i}(x;h)=\begin{cases}K\left(\frac{x-x\_{i}}{h}\right)/\sum\_{\delta\_{j}=1}K\left(\frac{x-x\_{j}}{h}\right),&\qquad\text{if }\delta\_{i}=1,\\ 0,&\qquad\text{if }\delta\_{i}=0,\end{cases} |  |

where Z=min⁡(Y,C)Z=\min(Y,C), KK is a kernel function and hh is the chosen bandwidth.
Denoting the weight WW corresponding to the iith smallest ZZ-value
Zi,nZ\_{i,n} by Wi,nW\_{i,n}, we for instance obtain the following Worms-type estimator of the conditional extreme value index given X=xX=x:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ^k,nW​(X=x)\displaystyle\hat{\xi}\_{k,n}^{W}(X=x) | =\displaystyle= | ∫Zn−k,n∞{1−F^Y|X​(y∣x)}​d​(log⁡y)1−F^Y|X​(Z(n−k)∣x)\displaystyle\frac{\int\_{Z\_{n-k,n}}^{\infty}\{1-\hat{F}\_{Y|X}(y\mid x)\}\,\mathop{}\!\mathrm{d}(\log y)}{1-\hat{F}\_{Y|X}(Z\_{(n-k)}\mid x)} |  |
|  |  | =\displaystyle= | ∑j=1k(∏i=1n−j[(1−Wi,n​(x;h)1−∑l=1i−1Wl,n​(x;h))δi,n]​log⁡Z(n−j+1)Z(n−j))∏i=1n−k[(1−Wi,n​(x;h)1−∑l=1i−1Wl,n​(x;h))δi,n].\displaystyle\frac{\sum\_{j=1}^{k}\left(\prod\_{i=1}^{n-j}\left[\left(1-\frac{W\_{i,n}(x;h)}{1-\sum\_{l=1}^{i-1}W\_{l,n}(x;h)}\right)^{\delta\_{i,n}}\right]\log{Z\_{(n-j+1)}\over Z\_{(n-j)}}\right)}{\prod\_{i=1}^{n-k}\left[\left(1-\frac{W\_{i,n}(x;h)}{1-\sum\_{l=1}^{i-1}W\_{l,n}(x;h)}\right)^{\delta\_{i,n}}\right]}. |  |

Pareto QQ-plots adapted for censoring per chosen xx value, defined as

|  |  |  |
| --- | --- | --- |
|  | {(−log⁡{1−F^Y|X​(Z(n−j+1)∣x)},log⁡Z(n−j+1))}j=1n,\left\{(-\log\{1-\hat{F}\_{Y|X}(Z\_{(n-j+1)}\mid x)\},\log Z\_{(n-j+1)})\right\}\_{j=1}^{n}, |  |

can then help to assess an appropriate value of k=kxk=k\_{x}.
  
A generalization of extreme quantile estimators Q^k(c)​(1−p)\hat{Q}\_{k}^{(c)}(1-p) to the local regression setting is obtained using a local extreme value index estimator such as ξ^k,nW​(X=x)\hat{\xi}\_{k,n}^{W}(X=x) and the Akritas–Van Keilegom estimator 1−F^Y|X​(y∣x)1-\hat{F}\_{Y|X}(y\mid x).

Stupfler [[72](https://arxiv.org/html/2511.22272v1#bib.bib72)] presents a local estimator of the extreme value index under random right censoring when YY given X=xX=x belongs to any max-domain of attraction, generalizing the moment estimator proposed in Einmahl et al. [[35](https://arxiv.org/html/2511.22272v1#bib.bib35)]. Further extensions were provided in Goegebeur et al. [[43](https://arxiv.org/html/2511.22272v1#bib.bib43)], Rutikanga and Diop [[67](https://arxiv.org/html/2511.22272v1#bib.bib67)] and Dierckx et al. [[34](https://arxiv.org/html/2511.22272v1#bib.bib34)].

## 7 Multivariate Modelling

The consideration of multivariate extremes is relevant for reinsurance companies in many ways. Firstly, it naturally appears when it comes to aggregate covers across different business lines of a first line insurer, but then also for the purpose of spatial diversification across contracts with several insurers, and more generally in the overall resulting reinsurance portfolio. The general mathematical theory of multivariate extremes is a well-developed and vibrant field (see e.g. Beirlant et al. [[18](https://arxiv.org/html/2511.22272v1#bib.bib18)], Davison and Huser [[32](https://arxiv.org/html/2511.22272v1#bib.bib32)] and Engelke and Ivanovs [[37](https://arxiv.org/html/2511.22272v1#bib.bib37)] for overviews). We restrict ourselves here to some contributions that are particular to insurance applications, i.e. extensions of the previous sections to the multivariate situation.

Lee and Lin [[50](https://arxiv.org/html/2511.22272v1#bib.bib50)] define a DD-variate Erlang mixture, where each mixture component is the joint distribution of DD independent Erlang distributions with a common scale parameter 1/λ>01/\lambda>0. The dependence structure is then captured by the combination of the positive integer shape parameters of the Erlangs in each dimension. For illustration, we entirely focus on the case D=2D=2. Let 𝐫=(r1,r2)∈ℛ{\bf r}=(r\_{1},r\_{2})\in\mathcal{R} the vector of shape parameters with values in the set ℛ\mathcal{R} of allowed combinations in the set of all shape vectors with non-zero weight. The density of a bivariate Erlang mixture evaluated in 𝐱=(x1,x2)>𝟎{\bf x}=(x\_{1},x\_{2})>{\bf 0} is then defined as

|  |  |  |
| --- | --- | --- |
|  | fMME​(𝐱;α,𝐫,λ)=∑𝐫∈ℛα𝐫​∏j=12λrj​xjrj−1​e−λ​xj(rj−1)!.f\_{\text{MME}}({\bf x};{\bf\alpha},{\bf r},\lambda)=\sum\_{{\bf r}\in\mathcal{R}}\alpha\_{{\bf r}}\,\prod\_{j=1}^{2}{\lambda^{r\_{j}}x\_{j}^{r\_{j}-1}e^{-\lambda x\_{j}}\over(r\_{j}-1)!}. |  |

It can be shown that the bivariate Erlang mixture with density

|  |  |  |
| --- | --- | --- |
|  | ∑r1=1∞∑r2=1∞α𝐫​(λ)​∏j=12λrj​xjrj−1​e−λ​xj(rj−1)!\sum\_{r\_{1}=1}^{\infty}\sum\_{r\_{2}=1}^{\infty}\alpha\_{{\bf r}}(\lambda)\,\prod\_{j=1}^{2}{\lambda^{r\_{j}}x\_{j}^{r\_{j}-1}e^{-\lambda x\_{j}}\over(r\_{j}-1)!} |  |

and suitable mixing weights can approximate any given bivariate positive distribution function arbitrarily closely as λ→∞\lambda\to\infty,
cf. [[50](https://arxiv.org/html/2511.22272v1#bib.bib50)].
Verbelen et al. [[74](https://arxiv.org/html/2511.22272v1#bib.bib74)] provide a flexible fitting procedure for such multivariate mixed Erlang (MME) distributions, which iteratively uses the EM algorithm, by introducing a computationally efficient initialization and adjustment strategy for the shape parameter vectors. [[74](https://arxiv.org/html/2511.22272v1#bib.bib74)] also considered randomly censored and fixed truncated data.

When it comes to splicing, the bivariate cumulative distribution function of a splicing model with a bivariate ME and a bivariate GP distribution is now

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(𝐱)={0,if ​𝐱≤𝐭l,π​FMME​(𝐱),if ​𝐭l≤𝐱≤𝐭,π​FMME​(𝐱)+(1−π)​FMGPD​(𝐱),if ​𝐱≰𝐭,F({\bf x})=\left\{\begin{array}[]{ll}0,&\mbox{if }{\bf x}\leq{\bf t}^{l},\\ \pi F\_{\text{MME}}({\bf x}),&\mbox{if }{\bf t}^{l}\leq{\bf x}\leq{\bf t},\\ \pi F\_{\text{MME}}({\bf x})+(1-\pi)F\_{\text{MGPD}}({\bf x}),&\mbox{if }{\bf x}\nleq{\bf t},\end{array}\right. |  | (9) |

for an appropriate set of thresholds 𝐭=(t1,t2){\bf t}=(t\_{1},t\_{2}), see also [[5](https://arxiv.org/html/2511.22272v1#bib.bib5)].
For the tail component one can for instance use the bivariate GP distribution as proposed in Rootzén and Tajvidi [[66](https://arxiv.org/html/2511.22272v1#bib.bib66)] and Kiriliouk et al. [[47](https://arxiv.org/html/2511.22272v1#bib.bib47)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | FMGPD​(𝐱)\displaystyle F\_{\text{MGPD}}({\bf x}) | =θ−1[ℓ({1+ξ1​((x1−t1)∧0)σ1}−1/ξ1,{1+ξ2​((x2−t2)∧0)σ2}−1/ξ2)\displaystyle=\theta^{-1}\left[\ell\left(\left\{1+{\xi\_{1}((x\_{1}-t\_{1})\wedge 0)\over\sigma\_{1}}\right\}^{-1/\xi\_{1}},\left\{1+{\xi\_{2}((x\_{2}-t\_{2})\wedge 0)\over\sigma\_{2}}\right\}^{-1/\xi\_{2}}\right)\right. |  |  |
|  |  | −ℓ({1+ξ1​(x1−t1)σ1}−1/ξ1,{1+ξ2​(x2−t2)σ2}−1/ξ2)],\displaystyle\hskip 28.45274pt\left.-\ell\left(\left\{1+{\xi\_{1}(x\_{1}-t\_{1})\over\sigma\_{1}}\right\}^{-1/\xi\_{1}},\left\{1+{\xi\_{2}(x\_{2}-t\_{2})\over\sigma\_{2}}\right\}^{-1/\xi\_{2}}\right)\right], |  |  |

such that 𝝈+𝝃​(𝐱−𝐭)>𝟎{\boldsymbol{\sigma}}+{\boldsymbol{\xi}}({\bf x-t})>{\bf 0}, where ℓ\ell denotes the stable tail dependence function and θ=ℓ​(1,1)\theta=\ell(1,1) the extremal coefficient. In the bivariate case, we can make use of the Pickands dependence function AA with

|  |  |  |
| --- | --- | --- |
|  | ℓ​(u1,u2)=(u1+u2)​A​(u2u1+u2),\ell(u\_{1},u\_{2})=(u\_{1}+u\_{2})A\left({u\_{2}\over u\_{1}+u\_{2}}\right), |  |

for which Goegebeur et al. [[42](https://arxiv.org/html/2511.22272v1#bib.bib42)] provided the following estimator under censoring. With X~j:=−log⁡Fj​(Xj)\tilde{X}\_{j}:=-\log F\_{j}(X\_{j}) for j=1,2j=1,2,
one has

|  |  |  |
| --- | --- | --- |
|  | P​(X~1>y1,X~2>y2)=exp⁡{−(y1+y2)​A​(y1y1+y2)}.{P}(\tilde{X}\_{1}>y\_{1},\tilde{X}\_{2}>y\_{2})=\exp\left\{-(y\_{1}+y\_{2})A\left({y\_{1}\over y\_{1}+y\_{2}}\right)\right\}. |  |

As X~t:=min⁡(X~1/(1−t),X~2/t)\tilde{X}\_{t}:=\min\left({\tilde{X}\_{1}/(1-t)},{\tilde{X}\_{2}/t}\right) satisfies

|  |  |  |
| --- | --- | --- |
|  | P​(X~t>z)=e−A​(t)​z,z>0,{P}(\tilde{X}\_{t}>z)=e^{-A(t)z},\quad z>0, |  |

we are led to the estimation of the exponential parameter A​(t)A(t) based on random right-censored data X~t,i\tilde{X}\_{t,i} for i=1,…,ni=1,\ldots,n. As in ([8](https://arxiv.org/html/2511.22272v1#S4.E8 "In 4 Censoring ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")), the maximum likelihood estimator of A​(t)A(t) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | A^​(t)=proportion of uncensored data1n​∑i=1nX~t,i.\hat{A}(t)=\frac{\mbox{proportion of uncensored data}}{{1\over n}\sum\_{i=1}^{n}\tilde{X}\_{t,i}}. |  | (10) |

Note that in practice X~j\tilde{X}\_{j}, j=1,2j=1,2 is to be estimated using the Kaplan-Meier estimator of FjF\_{j}.
  
Confidence bounds can be derived using the approaches in Chapter LABEL:CH:INFERENCE. In [[42](https://arxiv.org/html/2511.22272v1#bib.bib42)], one can also find robust estimators under this setting.

Example: Censored Liability Loss Data. The estimate A^\hat{A} for the (Loss, ALAE) data from Figure [4](https://arxiv.org/html/2511.22272v1#S4.F4 "Figure 4 ‣ 4 Censoring ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall") is discussed and plotted in Goegebeur et al. [[42](https://arxiv.org/html/2511.22272v1#bib.bib42), Fig. 10].
Goegebeur et al. [[43](https://arxiv.org/html/2511.22272v1#bib.bib43)] also considered the payment
g​(X1,X2)g(X\_{1},X\_{2}) by the reinsurer given by

|  |  |  |
| --- | --- | --- |
|  | g​(X1,X2)={0,if ​X1≤M,X1−M+X1−MX1​X2,if ​M<X1≤M+L,L+LL+M​X2,if ​X1≥M+L,g(X\_{1},X\_{2})=\begin{cases}0,&\text{if }X\_{1}\leq M,\\ X\_{1}-M+{X\_{1}-M\over X\_{1}}X\_{2},&\text{if }M<X\_{1}\leq M+L,\\ L+{L\over L+M}X\_{2},&\text{if }X\_{1}\geq M+L,\end{cases} |  |

with X1X\_{1}
representing the loss and X2X\_{2} the ALAE.
The pure premium is then given by

|  |  |  |
| --- | --- | --- |
|  | E​{g​(X1,X2)}=∫[0,∞)2g​(x1,x2)​d​F^​(x1,x2){E}\left\{g(X\_{1},X\_{2})\right\}=\int\_{[0,\infty)^{2}}g(x\_{1},x\_{2})\mathop{}\!\mathrm{d}\hat{F}(x\_{1},x\_{2}) |  |

with F^\hat{F} following from ([9](https://arxiv.org/html/2511.22272v1#S7.E9 "In 7 Multivariate Modelling ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")). Numerical integration is needed here.

An alternative to splicing are again multivariate versions of matrix-Mittag–Leffler distributions, see Albrecher et al. [[8](https://arxiv.org/html/2511.22272v1#bib.bib8), [9](https://arxiv.org/html/2511.22272v1#bib.bib9)].

## 8 Natural Catastrophe Insurance and Climate Change

The importance of multivariate extremes becomes particularly apparent for the insurance of losses due to natural catastrophes, where marginal tails often are very heavy and at the same time correlation of claims and even of entire perils can be very strong. In such cases it is not even clear whether the risks are insurable, and there is a strong need for a profound understanding of the joint occurrences of extremes. In fact, each type of peril requires a quite different modelling approach in practice, see Hao et al. [[46](https://arxiv.org/html/2511.22272v1#bib.bib46)]. This may even include the need to define new spatial distance concepts. An example is a river-flow rather than Euclidian distance for locations in a river network for calibrating a max-stable process of Brown–Resnick type for joint discharges at river gauges, cf. Asadi et al. [[13](https://arxiv.org/html/2511.22272v1#bib.bib13)]; this model was then for instance used to quantify fluvial flood risk and its spatial diversification potential across a country, see Albrecher et al. [[10](https://arxiv.org/html/2511.22272v1#bib.bib10)]. Other perils like storms may be more easily linked to measurable variables like maximum wind speeds, which can be modelled itself and then inform the storm loss models of (re)insurers, see e.g. Prettenthaler et al. [[63](https://arxiv.org/html/2511.22272v1#bib.bib63)], Prahl et al. [[61](https://arxiv.org/html/2511.22272v1#bib.bib61)], Lescourret and Robert [[52](https://arxiv.org/html/2511.22272v1#bib.bib52)], Mornet et al. [[57](https://arxiv.org/html/2511.22272v1#bib.bib57)]. Whereas a causal model for hazards and their induced losses can be seen as an eventual goal, the interplay of factors is typically much too complex to solely rely on these, and bottom-up models (like hydrological models for flood risk) are not designed to fully capture extremes, so that the toolkit of statistics of extremes (and in particular regression modelling with those components that are available) remains an essential ingredient in the analysis. Perils like hailstorms are even harder to model, see e.g. Allen et al. [[12](https://arxiv.org/html/2511.22272v1#bib.bib12), [11](https://arxiv.org/html/2511.22272v1#bib.bib11)] and Miralles et al. [[56](https://arxiv.org/html/2511.22272v1#bib.bib56)]. In some cases it can also be meaningful to let the dependence structure itself depend on covariates, see e.g. Mhalla et al. [[55](https://arxiv.org/html/2511.22272v1#bib.bib55)] as well as Chapter LABEL:CH:REGMULTI.

Another direction where insurance applications generate interesting research questions is in the context of changing climatic conditions. Non-stationary data in EVA have been studied already for some time, see e.g. Chavez-Demoulin and Davison [[29](https://arxiv.org/html/2511.22272v1#bib.bib29)], but the recent evidence of climate change (see, e.g., Sobel et al. [[71](https://arxiv.org/html/2511.22272v1#bib.bib71)], Koch et al. [[49](https://arxiv.org/html/2511.22272v1#bib.bib49)], Seneviratne et al. [[70](https://arxiv.org/html/2511.22272v1#bib.bib70)]) creates new questions and challenges, both in the analysis of frequency and severity of events. A sound modelling of extremes leading to an adequate quantification of catastrophe risk is crucial for a proper risk management of reinsurance companies, so that reinsurance coverage can still be provided for natural hazards in the face of climate change.

Acknowledgement. The authors would like to thank Alaric Mueller for help with the implementation of the numerical examples, and François Dufresne for a careful reading of the manuscript.

## References

* [1]

  I. B. Aban, M. M. Meerschaert, and A. K. Panorska.
  Parameter estimation for the truncated Pareto distribution.
  Journal of the American Statistical Association,
  101(473):270–277, 2006.
* [2]

  M. G. Akritas and I. V. Keilegom.
  Estimation of bivariate and marginal distributions with censored
  data.
  Journal of the Royal Statistical Society Series B: Statistical
  Methodology, 65(2):457–471, 2003.
* [3]

  H. Albrecher.
  Reinsurance.
  Encyclopedia of Quantitative Finance, pages 1539–1543, 2010.
* [4]

  H. Albrecher, J. C. Araujo-Acuna, and J. Beirlant.
  Tempered Pareto-type modelling using Weibull distributions.
  ASTIN Bulletin, 51(2):509–538, 2021.
* [5]

  H. Albrecher, J. Beirlant, and J. L. Teugels.
  Reinsurance: Actuarial and Statistical Aspects.
  Wiley Ser. Probab. Stat. Hoboken, NJ: John Wiley & Sons, 2017.
* [6]

  H. Albrecher and M. Bladt.
  Informed censoring: The parametric combination of data and expert
  information.
  Statistical Planning and Inference, 233:106171, 2024.
* [7]

  H. Albrecher, M. Bladt, and M. Bladt.
  Matrix Mittag-Leffler distributions and modeling heavy-tailed
  risks.
  Extremes, 23(3):425–450, 2020.
* [8]

  H. Albrecher, M. Bladt, and M. Bladt.
  Multivariate fractional phase–type distributions.
  Fractional Calculus and Applied Analysis, 23(5):1431–1451,
  2020.
* [9]

  H. Albrecher, M. Bladt, and M. Bladt.
  Multivariate matrix Mittag–Leffler distributions.
  Annals of the Institute of Statistical Mathematics,
  73:369–394, 2021.
* [10]

  H. Albrecher, D. Kortschak, and F. Prettenthaler.
  Spatial dependence modeling of flood risk using max-stable processes:
  The example of Austria.
  Water, 12(6):1805, 2020.
* [11]

  J. T. Allen, M. K. Tippett, Y. Kaheil, A. H. Sobel, C. Lepore, S. Nong, and
  A. Muehlbauer.
  An extreme value model for US hail size.
  Monthly Weather Review, 145(11):4501–4519, 2017.
* [12]

  J. T. Allen, M. K. Tippett, and A. H. Sobel.
  Influence of the El Niño/Southern oscillation on tornado
  and hail frequency in the United States.
  Nature Geoscience, 8(4):278–283, 2015.
* [13]

  P. Asadi, A. C. Davison, and S. Engelke.
  Extremes on river networks.
  The Annals of Applied Statistics, 9:2023–2050, 2015.
* [14]

  S. A. Bakar, N. A. Hamzah, M. Maghsoudi, and S. Nadarajah.
  Modeling loss data using composite models.
  Insurance: Mathematics and Economics, 61:146–154, 2015.
* [15]

  J. Beirlant, I. F. Alves, and I. Gomes.
  Tail fitting for truncated and non-truncated Pareto-type
  distributions.
  Extremes, 19:429–462, 2016.
* [16]

  J. Beirlant, I. F. Alves, and T. Reynkens.
  Fitting tails affected by truncation.
  Electronic Journal of Statistics, 11:2026–2065, 2017.
* [17]

  J. Beirlant, A. Bardoutsos, T. de Wet, and I. Gijbels.
  Bias reduced tail estimation for censored Pareto type
  distributions.
  Statistics & Probability Letters, 109:78–88, 2016.
* [18]

  J. Beirlant, Y. Goegebeur, J. Segers, and J. L. Teugels.
  Statistics of extremes: theory and applications.
  John Wiley & Sons, 2004.
* [19]

  J. Beirlant, A. Guillou, G. Dierckx, and A. Fils-Villetard.
  Estimation of the extreme value index and extreme quantiles under
  random censoring.
  Extremes, 10(3):151–174, 2007.
* [20]

  J. Beirlant, G. Maribe, and A. Verster.
  Penalized bias reduction in extreme value estimation for censored
  Pareto-type data, and long-tailed insurance applications.
  Insurance: Mathematics and Economics, 78:114–122, 2018.
* [21]

  J. Beirlant, J. Worms, and R. Worms.
  Estimation of the extreme value index in a censorship framework:
  Asymptotic and finite sample behavior.
  Journal of Statistical Planning and Inference, 202:31–56,
  2019.
* [22]

  M. Bladt, H. Albrecher, and J. Beirlant.
  Combined tail estimation using censored data and expert information.
  Scandinavian Actuarial Journal, 2020(6):503–525, 2020.
* [23]

  M. Bladt, H. Albrecher, and J. Beirlant.
  Trimmed extreme value estimators for censored heavy-tailed data.
  Electronic Journal of Statistics, 15(1):3112–3136, 2021.
* [24]

  M. Bladt and C. Furrer.
  Expert Kaplan–Meier estimation.
  Scandinavian Actuarial Journal, 2024:1–27, 2024.
* [25]

  M. Bladt and I. Rodionov.
  Censored extreme value estimation.
  arXiv preprint arXiv:2312.10499, 2023.
* [26]

  M. Bladt and J. Yslas.
  Heavy-tailed phase-type distributions: a unified approach.
  Extremes, 25(3):529–565, 2022.
* [27]

  E. Bølviken and I. Hobæk Haff.
  Loss modeling with many-parameter distributions.
  Scandinavian Actuarial Journal, pages 1–18, 2024.
* [28]

  E. Calderín-Ojeda and C. F. Kwok.
  Modeling claims data with composite Stoppa models.
  Scandinavian Actuarial Journal, 2016(9):817–836, 2016.
* [29]

  V. Chavez-Demoulin and A. Davison.
  Generalized additive modelling of sample extremes.
  Journal of the Royal Statistical Society Series C: Applied
  Statistics, 54(1):207–222, 2005.
* [30]

  R. Ciumara.
  An actuarial model based on the composite Weibull-Pareto
  distribution.
  Mathematical Reports Bucharest, 8(4):401, 2006.
* [31]

  K. Cooray and M. M. Ananda.
  Modeling actuarial data with a composite Lognormal-Pareto model.
  Scandinavian Actuarial Journal, 2005(5):321–334, 2005.
* [32]

  A. C. Davison and R. Huser.
  Statistics of extremes.
  Annual Review of Statistics and its Application, 2:203–235,
  2015.
* [33]

  A. P. Dempster, N. M. Laird, and D. B. Rubin.
  Maximum likelihood from incomplete data via the EM algorithm.
  Journal of the Royal Statistical Society: Series B,
  39(1):1–22, 1977.
* [34]

  G. Dierckx, Y. Goegebeur, and A. Guillou.
  Local robust estimation of Pareto-type tails with random right
  censoring.
  Sankhyā A, 83:70–108, 2021.
* [35]

  J. H. Einmahl, A. Fils-Villetard, and A. Guillou.
  Statistics of extremes under random censoring.
  Bernoulli, 14(1):207–227, 2008.
* [36]

  M. Eling and J. Wirfs.
  What are the actual costs of cyber risk events?
  European Journal of Operational Research, 272(3):1109–1119,
  2019.
* [37]

  S. Engelke and J. Ivanovs.
  Sparse structures for multivariate extremes.
  Annual Review of Statistics and Its Application, 8:241–270,
  2021.
* [38]

  M. Fackler.
  Reinventing Pareto: Fits for both small and large losses.
  In ASTIN Colloquium, Den Haag, 2013.
* [39]

  M. Fackler.
  Premium rating without losses: How to estimate the loss frequency of
  loss-free risks.
  European Actuarial Journal, 12(1):275–316, 2022.
* [40]

  T. C. Fung, H. Jeong, and G. Tzougas.
  Soft splicing model: bridging the gap between composite model and
  finite mixture model.
  Scandinavian Actuarial Journal, 2024:168–197, 2024.
* [41]

  S. Ghaddab, M. Kacem, C. de Peretti, and L. Belkacem.
  Extreme severity modeling using a GLM-GPD combination:
  application to an excess of loss reinsurance treaty.
  Empirical Economics, 65:1105–1127, 2023.
* [42]

  Y. Goegebeur, A. Guillou, and J. Qin.
  Robust estimation of the Pickands dependence function under random
  right censoring.
  Insurance: Mathematics and Economics, 87:101–114, 2019.
* [43]

  Y. Goegebeur, A. Guillou, and J. Qin.
  Extreme value estimation of the conditional risk premium in
  reinsurance.
  Insurance: Mathematics and Economics, 96:68–80, 2021.
* [44]

  Y. Goegebeur, A. Guillou, and J. Qin.
  Conditional tail moment and reinsurance premium estimation under
  random right censoring.
  Test, 33:230–250, 2024.
* [45]

  W. Guevara-Alarcón, H. Albrecher, and P. Chowdhury.
  On marine liability portfolio modeling.
  ASTIN Bulletin, 50(1):61–93, 2020.
* [46]

  Z. Hao, V. P. Singh, and F. Hao.
  Compound extremes in hydroclimatology: a review.
  Water, 10(6):718, 2018.
* [47]

  A. Kiriliouk, H. Rootzén, J. Segers, and J. L. Wadsworth.
  Peaks over thresholds modeling with multivariate generalized Pareto
  distributions.
  Technometrics, 61(1):123–135, 2019.
* [48]

  S. A. Klugman, H. H. Panjer, and G. E. Willmot.
  Loss models: from data to decisions, volume 715.
  John Wiley & Sons, 2012.
* [49]

  E. Koch, J. Koh, A. C. Davison, C. Lepore, and M. K. Tippett.
  Trends in the extremes of environments associated with severe US
  thunderstorms.
  Journal of Climate, 34(4):1259–1272, 2021.
* [50]

  D. Lee, W. K. Li, and T. S. T. Wong.
  Modeling insurance claims via a mixture exponential model combined
  with peaks-over-threshold approach.
  Insurance: Mathematics and Economics, 51(3):538–550, 2012.
* [51]

  S. C. Lee and X. S. Lin.
  Modeling and evaluating insurance losses via mixtures of Erlang
  distributions.
  North American Actuarial Journal, 14(1):107–130, 2010.
* [52]

  L. Lescourret and C. Y. Robert.
  Extreme dependence of multivariate catastrophic losses.
  Scandinavian Actuarial Journal, 2006(4):203–225, 2006.
* [53]

  J. Li and J. Liu.
  Claims modelling with three-component composite models.
  Risks, 11(11):196, 2023.
* [54]

  M. M. Meerschaert, P. Roy, and Q. Shao.
  Parameter estimation for exponentially tempered power law
  distributions.
  Communications in Statistics-Theory and Methods,
  41(10):1839–1856, 2012.
* [55]

  L. Mhalla, M. de Carvalho, and V. Chavez-Demoulin.
  Regression-type models for extremal dependence.
  Scandinavian Journal of Statistics, 46(4):1141–1167, 2019.
* [56]

  O. Miralles, A. C. Davison, and T. Schmid.
  Bayesian modeling of insurance claims for hail damage.
  arXiv preprint arXiv:2308.04926, 2023.
* [57]

  A. Mornet, T. Opitz, M. Luzi, and S. Loisel.
  Index for predicting insurance claims from wind storms with an
  application in france.
  Risk Analysis, 35(11):2029–2056, 2015.
* [58]

  S. Nadarajah and S. A. Bakar.
  New composite models for the Danish fire insurance data.
  Scandinavian Actuarial Journal, 2014(2):180–187, 2014.
* [59]

  M. Pigeon and M. Denuit.
  Composite Lognormal–Pareto model with random threshold.
  Scandinavian Actuarial Journal, 2011(3):177–192, 2011.
* [60]

  C. Poudyal and V. Brazauskas.
  Finite-sample performance of the T-and W-estimators for the
  Pareto tail index under data truncation and censoring.
  Journal of Statistical Computation and Simulation,
  93(10):1601–1621, 2023.
* [61]

  B. F. Prahl, D. Rybski, O. Burghoff, and J. P. Kropp.
  Comparison of storm damage functions and their performance.
  Natural Hazards and Earth System Sciences, 15(4):769–788,
  2015.
* [62]

  F. Prettenthaler, H. Albrecher, P. Asadi, and J. Köberl.
  On flood risk pooling in Europe.
  Natural hazards, 88:1–20, 2017.
* [63]

  F. Prettenthaler, H. Albrecher, J. Köberl, and D. Kortschak.
  Risk and insurability of storm damages to residential buildings in
  Austria.
  The Geneva Papers on Risk and Insurance-Issues and Practice,
  37:340–364, 2012.
* [64]

  M. Raschke.
  Alternative modelling and inference methods for claim size
  distributions.
  Annals of Actuarial Science, 14(1):1–19, 2020.
* [65]

  T. Reynkens, R. Verbelen, J. Beirlant, and K. Antonio.
  Modelling censored losses using splicing: A global fit strategy with
  mixed Erlang and extreme value distributions.
  Insurance: Mathematics and Economics, 77:65–77, 2017.
* [66]

  H. Rootzén and N. Tajvidi.
  Multivariate generalized Pareto distributions.
  Bernoulli, 12(5):917–930, 2006.
* [67]

  J. U. Rutikanga and A. Diop.
  Functional kernel estimation of the conditional extreme value index
  under random right censoring.
  Afrika Statistika, 16(2):2647–2688, 2021.
* [68]

  D. P. Scollnik.
  On composite lognormal-Pareto models.
  Scandinavian Actuarial Journal, 2007(1):20–33, 2007.
* [69]

  D. P. Scollnik and C. Sun.
  Modeling with Weibull-Pareto models.
  North American Actuarial Journal, 16(2):260–272, 2012.
* [70]

  S. I. Seneviratne, X. Zhang, M. Adnan, W. Badi, C. Dereczynski, A. Di Luca,
  S. Ghosh, I. Iskander, J. Kossin, S. Lewis, F. Otto, I. Pinto, M. Satoh,
  S. Vicente-Serrano, M. Wehner, and B. Zhou.
  Weather and climate extreme events in a changing climate.
  Climate Change 2021: The Physical Science Basis. Contribution of
  Working Group I to the Sixth Assessment Report of the Intergovernmental Panel
  on Climate Change, pages 1513–1766, 2021.
* [71]

  A. H. Sobel, S. J. Camargo, T. M. Hall, C.-Y. Lee, M. K. Tippett, and A. A.
  Wing.
  Human influence on tropical cyclone intensity.
  Science, 353(6296):242–246, 2016.
* [72]

  G. Stupfler.
  Estimating the conditional extreme value index under random
  right-censoring.
  Journal of Multivariate Analysis, 144:1–24, 2016.
* [73]

  G. Stupfler.
  On the study of extremes with dependent random right-censoring.
  Extremes, 22(1):97–129, 2019.
* [74]

  R. Verbelen, L. Gong, K. Antonio, A. Badescu, and S. Lin.
  Fitting mixtures of Erlangs to censored and truncated data using
  the EM algorithm.
  ASTIN Bulletin: The Journal of the IAA, 45(3):729–758, 2015.
* [75]

  Y. Wang and I. Hobæk Haff.
  Focussed selection of the claim severity distribution.
  Scandinavian Actuarial Journal, 2019(2):129–142, 2019.
* [76]

  Y. Wang, I. Hobæk Haff, and A. Huseby.
  Modelling extreme claims via composite models and threshold selection
  methods.
  Insurance: Mathematics and Economics, 91:257–268, 2020.
* [77]

  I. Weissman.
  Estimation of parameters and large quantiles based on the kk largest
  observations.
  Journal of the American Statistical Association,
  73(364):812–815, 1978.
* [78]

  J. Worms and R. Worms.
  New estimators of the extreme value index under random right
  censoring, for heavy tailed distributions.
  Extremes, 17:337–358, 2014.

## Index

* bias reduction [§1](https://arxiv.org/html/2511.22272v1#S1.p3 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* composite model [§5](https://arxiv.org/html/2511.22272v1#S5.p1 "5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* conditional tail expectation (CTE) [§2](https://arxiv.org/html/2511.22272v1#S2.p5 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* extreme quantile estimation [§1](https://arxiv.org/html/2511.22272v1#S1 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* extreme value index [§1](https://arxiv.org/html/2511.22272v1#S1 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* full models [§2](https://arxiv.org/html/2511.22272v1#S2.p5 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* Hill plot [§1](https://arxiv.org/html/2511.22272v1#S1.p2 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* IBNR [2nd item](https://arxiv.org/html/2511.22272v1#S2.I2.i2.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* information criterion [§5](https://arxiv.org/html/2511.22272v1#S5.p4 "5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* Kaplan–Meier estimator [§6](https://arxiv.org/html/2511.22272v1#S6.p1 "6 Regression Modelling ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* losses
  + attritional [§1](https://arxiv.org/html/2511.22272v1#S1.p4 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + large [§1](https://arxiv.org/html/2511.22272v1#S1.p4 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* maximum likelihood estimation [§3.2](https://arxiv.org/html/2511.22272v1#S3.SS2.p2 "3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* mean excess function [§5](https://arxiv.org/html/2511.22272v1#S5.p5 "5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* mixed Erlang distribution [§5](https://arxiv.org/html/2511.22272v1#S5.p2 "5 Full Models for Claims ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), [§7](https://arxiv.org/html/2511.22272v1#S7.p2 "7 Multivariate Modelling ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* natural catastrophe insurance [§8](https://arxiv.org/html/2511.22272v1#S8 "8 Natural Catastrophe Insurance and Climate Change ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* Pareto QQ-plot [§1](https://arxiv.org/html/2511.22272v1#S1.p2 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* Pareto-type distribution [§1](https://arxiv.org/html/2511.22272v1#S1.p4 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), [§3.2](https://arxiv.org/html/2511.22272v1#S3.SS2.p1 "3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* POT approximation [§3.2](https://arxiv.org/html/2511.22272v1#S3.SS2.p2 "3.2 Tempering ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* premium estimation [§1](https://arxiv.org/html/2511.22272v1#S1 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* pure premium [§2](https://arxiv.org/html/2511.22272v1#S2.p5 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* RBNS [3rd item](https://arxiv.org/html/2511.22272v1#S2.I2.i3.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* regression modelling [§6](https://arxiv.org/html/2511.22272v1#S6 "6 Regression Modelling ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* reinsurance [§1](https://arxiv.org/html/2511.22272v1#S1.p1 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + cumulative XL [2nd item](https://arxiv.org/html/2511.22272v1#S2.I1.i2.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + drop-down XL [3rd item](https://arxiv.org/html/2511.22272v1#S2.I1.i3.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + ECOMOR [3rd item](https://arxiv.org/html/2511.22272v1#S2.I1.i3.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + excess-of-loss [2nd item](https://arxiv.org/html/2511.22272v1#S2.I1.i2.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), [§2](https://arxiv.org/html/2511.22272v1#S2.p5 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + proportional [1st item](https://arxiv.org/html/2511.22272v1#S2.I1.i1.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + quota-share [1st item](https://arxiv.org/html/2511.22272v1#S2.I1.i1.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + stop-loss [2nd item](https://arxiv.org/html/2511.22272v1#S2.I1.i2.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
  + surplus [1st item](https://arxiv.org/html/2511.22272v1#S2.I1.i1.p1 "In 2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* return period estimation [§1](https://arxiv.org/html/2511.22272v1#S1 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* tempering [§2](https://arxiv.org/html/2511.22272v1#S2.p4 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* threshold selection [§1](https://arxiv.org/html/2511.22272v1#S1.p3 "1 Introduction ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* truncation [§2](https://arxiv.org/html/2511.22272v1#S2.p4 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall"), [§3.1](https://arxiv.org/html/2511.22272v1#S3.SS1.p2 "3.1 Truncation ‣ 3 Adaptations of the Classical Tail Analysis ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")
* value-at-risk (VaR) [§2](https://arxiv.org/html/2511.22272v1#S2.p5 "2 Reinsurance and Data ‣ Statistics of Extremes for the Insurance Industry11footnote 1to appear in Handbook of Statistics of Extremes, Chapman & Hall")