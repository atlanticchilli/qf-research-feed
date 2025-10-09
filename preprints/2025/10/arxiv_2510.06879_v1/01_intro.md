---
authors:
- Natascha Hey
- Eyal Neuman
- Sturmius Tuschmann
doc_id: arxiv:2510.06879v1
family_id: arxiv:2510.06879
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Nonparametric Estimation of Self- and Cross-Impact
url_abs: http://arxiv.org/abs/2510.06879v1
url_html: https://arxiv.org/html/2510.06879v1
venue: arXiv q-fin
version: 1
year: 2025
---


Natascha Hey
NH is supported by the Briger Family Digital Finance Lab at the Columbia Business School.
Graduate School of Business, Columbia University

Eyal Neuman
Department of Mathematics, Imperial College London

Sturmius Tuschmann
ST is supported by the EPSRC Centre for Doctoral Training in Mathematics of Random Systems: Analysis, Modelling and Simulation (EP/S023925/1).
Department of Mathematics, Imperial College London

(October 8, 2025)

###### Abstract

We introduce an offline nonparametric estimator for concave multi-asset propagator models based on a dataset of correlated price trajectories and metaorders. Compared to parametric models, our framework avoids parameter explosion in the multi-asset case and yields confidence bounds for the estimator. We implement the estimator using both proprietary metaorder data from Capital Fund Management (CFM) and publicly available S&P order flow data, where we augment the former dataset using a metaorder proxy. In particular, we provide unbiased evidence that self-impact is concave and exhibits a shifted power-law decay, and show that the metaorder proxy stabilizes the calibration. Moreover, we find that introducing cross-impact provides a significant gain in explanatory power, with concave specifications outperforming linear ones, suggesting that the square-root law extends to cross-impact. We also measure asymmetric cross-impact between assets driven by relative liquidity differences. Finally, we demonstrate that a shape-constrained projection of the nonparametric kernel not only ensures interpretability but also slightly outperforms established parametric models in terms of predictive accuracy.

Mathematics Subject Classification (2020):
:   62G08, 62L05, 91G80

Keywords:
:   market impact, cross-impact, concave price impact, nonparametric estimation, metaorder, order flow imbalance

## 1 Introduction

Price impact refers to the empirical observation that executing a large order adversely affects the price of a risky asset in a persistent manner, resulting in less favorable execution prices. It is well documented that price impact is concave with respect to trade size: larger trades tend to move prices less per unit volume than smaller trades, a property not captured by linear models. Instead, the empirical literature supports a square-root law of market impact [[8](https://arxiv.org/html/2510.06879v1#bib.bib8), [10](https://arxiv.org/html/2510.06879v1#bib.bib10), [31](https://arxiv.org/html/2510.06879v1#bib.bib31), [41](https://arxiv.org/html/2510.06879v1#bib.bib41), [45](https://arxiv.org/html/2510.06879v1#bib.bib45)], where the peak impact induced by a large *metaorder* of size QQ is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ipeak=Y​σD​sign​(Q)​|QVD|δ,I^{\text{peak}}=Y\sigma\_{D}\,\text{sign}(Q)\left|\frac{Q}{V\_{D}}\right|^{\delta}, |  | (1.1) |

where YY is a constant of order one, VDV\_{D} is the total daily traded volume, and σD\sigma\_{D} is the daily volatility. The square-root law states that empirically the exponent δ\delta is well approximated as 0.50.5. It has been shown to hold in various markets (such as equities, foreign exchange, options, and even cryptocurrencies), and is general enough to encompass different types of market liquidity, broad classes of execution strategies, and a range of trading frequencies [[10](https://arxiv.org/html/2510.06879v1#bib.bib10), [17](https://arxiv.org/html/2510.06879v1#bib.bib17), [25](https://arxiv.org/html/2510.06879v1#bib.bib25), [46](https://arxiv.org/html/2510.06879v1#bib.bib46), [47](https://arxiv.org/html/2510.06879v1#bib.bib47), [49](https://arxiv.org/html/2510.06879v1#bib.bib49)].

While the square-root law provides a simple connection between the metaorder size and its impact on the mid-price, price impact evolves dynamically, and the reaction of the mid-price to the metaorder is mostly transient. Consequently, an agent seeking to liquidate a large order must split it into smaller parts, referred to as *child orders*, which are typically executed over a period of hours or days. Propagator models are a central tool for mathematically describing this decay phenomenon. They express price moves in terms of the influence of past trades and therefore capture the decay of price impact after each trade [[12](https://arxiv.org/html/2510.06879v1#bib.bib12), [20](https://arxiv.org/html/2510.06879v1#bib.bib20)]. For a metaorder split into child orders {Qtj}j=0M−1\{Q\_{t\_{j}}\}\_{j=0}^{M-1} across MM time intervals, the price process PP follows the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pti+1−Pt0=∑j=0iGi,j​hc​(Qtj)+ϵti,i=0,…,M−1,P\_{t\_{i+1}}-P\_{t\_{0}}=\sum\_{j=0}^{i}G\_{i,j}h\_{c}(Q\_{t\_{j}})+\epsilon\_{t\_{i}},\quad i=0,\dots,M-1, |  | (1.2) |

where hc​(x):=sgn​(x)​|x|ch\_{c}(x):=\text{sgn}(x)|x|^{c} with c∈(0,1]c\in(0,1] is a concave impact function and (ϵti)i=0M−1(\epsilon\_{t\_{i}})\_{i=0}^{M-1} represents the noise. Here G=(Gi,j)i,j=0M−1G=(G\_{i,j})\_{i,j=0}^{M-1} is called the propagator, which is typically decreasing in the lag i−ji-j, reflecting the decaying effect of price impact. Obizhaeva and Wang [[38](https://arxiv.org/html/2510.06879v1#bib.bib38)] and Gârleanu and Pedersen [[19](https://arxiv.org/html/2510.06879v1#bib.bib19)], along with follow-up papers, assume that the price impact decays exponentially over time, that is, Gi,j=κ​e−ρ​(ti−tj)G\_{i,j}=\kappa e^{-\rho(t\_{i}-t\_{j})} for some positive constants κ\kappa and ρ\rho.
On the other hand, Bouchaud et al. [[12](https://arxiv.org/html/2510.06879v1#bib.bib12)] (see Chapter 13.2.1 and references therein) report on empirical observations that the propagator GG exhibits power-law decay in the lag, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gi,j≈(ti−tj)−β,0≤j<i≤M−1,G\_{i,j}\approx(t\_{i}-t\_{j})^{-\beta},\quad 0\leq j<i\leq M-1, |  | (1.3) |

where 0<β<10<\beta<1, and these results are also supported by theoretical arguments. A well-known example à la Almgren and Chriss addresses the case where all entries of GG are identical, then the sum in ([1.2](https://arxiv.org/html/2510.06879v1#S1.E2 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")) represents permanent price impact. If G=λ​𝕀MG=\lambda\mathbb{I}\_{M}, where λ>0\lambda>0 and 𝕀M∈ℝM×M\mathbb{I}\_{M}\in\mathbb{R}^{M\times M} is the identity matrix, the sum in ([1.2](https://arxiv.org/html/2510.06879v1#S1.E2 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")) represents temporary price impact (see [[6](https://arxiv.org/html/2510.06879v1#bib.bib6), [7](https://arxiv.org/html/2510.06879v1#bib.bib7)]).

Cross-impact models provide an additional explanation for the price dynamics of a risky asset in terms of the influence of past trades of other assets in the market. Throughout this paper, we will adopt the convention introduced in Section 14.5.3 of [[12](https://arxiv.org/html/2510.06879v1#bib.bib12)] and refer to price impact as the aggregated effects of self-impact and cross-impact. When there are d≥2d\geq 2 assets in the market with prices denoted by P=(P1,…,Pd)P=(P^{1},\ldots,P^{d}), the evolution of the returns is given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pti+1ℓ−Pt0ℓ=∑k=1d∑j=0iGi,j(ℓ,k)​hc(ℓ,k)​(Qtjk)+ϵtiℓ,i=0,…,M−1,ℓ=1,…,d,P^{\ell}\_{t\_{i+1}}-P^{\ell}\_{t\_{0}}=\sum\_{k=1}^{d}\sum\_{j=0}^{i}G^{(\ell,k)}\_{i,j}h\_{c\_{(\ell,k)}}(Q^{k}\_{t\_{j}})+\epsilon^{\ell}\_{t\_{i}},\quad i=0,\dots,M-1,\ \ell=1,\dots,d, |  | (1.4) |

where (Qtjk)j=0M−1(Q^{k}\_{t\_{j}})\_{j=0}^{M-1} are the traded volumes in asset k∈{1,…,d}k\in\{1,\ldots,d\} at each time interval, and (Gi,j(ℓ,k))(\smash{G^{(\ell,k)}\_{i,j}}) are propagators that quantify the self-impact of asset ℓ\ell and the cross-impact of all assets k≠ℓk\neq\ell on the asset ℓ\ell. The functions hc(ℓ,k)h\_{c\_{(\ell,k)}} are from the same class as in ([1.2](https://arxiv.org/html/2510.06879v1#S1.E2 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")), and can have different concavity parameters c(ℓ,k)c\_{(\ell,k)} for self- and cross-impact (see [[9](https://arxiv.org/html/2510.06879v1#bib.bib9), [12](https://arxiv.org/html/2510.06879v1#bib.bib12), [24](https://arxiv.org/html/2510.06879v1#bib.bib24), [27](https://arxiv.org/html/2510.06879v1#bib.bib27), [32](https://arxiv.org/html/2510.06879v1#bib.bib32), [42](https://arxiv.org/html/2510.06879v1#bib.bib42), [44](https://arxiv.org/html/2510.06879v1#bib.bib44)] for various versions of this model). Bouchaud et al. [[12](https://arxiv.org/html/2510.06879v1#bib.bib12)] (see Chapter 14.5.3) report on two main empirical observations regarding cross-impact:

* (i)

  diagonal and off-diagonal elements of the propagator matrix (G(ℓ,k))(\smash{G^{(\ell,k)}}) exhibit a power-law decay in the lag, that is, G(ℓ,k)​(t,s)≈(t−s)−βℓ​kG^{(\ell,k)}(t,s)\approx(t-s)^{-\beta\_{\ell k}}, with βℓ​k∈(0,1)\beta\_{\ell k}\in(0,1).
* (ii)

  most cross-correlations between price moves (≈60−90%\approx 60-90\%, depending on the timescale), are mediated by trades themselves, that is, through a cross-impact mechanism, rather than through the cross-correlation of noise terms, which are not directly related to trading.

The controversy surrounding the shape of the propagator has raised challenging questions regarding statistical estimation methods. Several estimators for the price impact kernel in the convolution case (i.e., where Gi,j=Gi−jG\_{i,j}=G\_{i-j}) have been proposed in [[9](https://arxiv.org/html/2510.06879v1#bib.bib9), [11](https://arxiv.org/html/2510.06879v1#bib.bib11), [18](https://arxiv.org/html/2510.06879v1#bib.bib18), [47](https://arxiv.org/html/2510.06879v1#bib.bib47)] and in Chapter 13.2 of [[12](https://arxiv.org/html/2510.06879v1#bib.bib12)]. These regression-based estimation methods are already common practice in the industry, but they overlook several mathematical issues, such as the ill-posedness of the least-squares estimation problem, dependencies between price trajectories, and error margins. A rigorous nonparametric estimation method for the price impact kernel in ([1.2](https://arxiv.org/html/2510.06879v1#S1.E2 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")) in the linear case (i.e., c=1c=1) was introduced in [[36](https://arxiv.org/html/2510.06879v1#bib.bib36)], where estimation is carried out in an online learning framework. A different approach using offline nonparametric estimation (i.e., using historical metaorder data) was developed in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] for the linear single-asset propagator model, and subsequently tested on data in [[48](https://arxiv.org/html/2510.06879v1#bib.bib48)].

The main objective of this paper is to extend the nonparametric method from [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] to the concave multi-asset impact model in ([1.4](https://arxiv.org/html/2510.06879v1#S1.E4 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")), and to implement the estimator using both proprietary metaorder data by Capital Fund Management (CFM) and public order flow data.
By incorporating the empirically supported square-root law, this extension significantly improves the goodness-of-fit in kernel estimation. Moreover, adding cross-impact between assets leads to an additional improvement, which is however of smaller magnitude than the one due to concavity.

A central theoretical challenge when moving from linear to concave impact models is to study the absence of price manipulation. That is, the overall costs due to price impact should always be nonnegative for any admissible trading strategy [[15](https://arxiv.org/html/2510.06879v1#bib.bib15), [20](https://arxiv.org/html/2510.06879v1#bib.bib20), [21](https://arxiv.org/html/2510.06879v1#bib.bib21), [22](https://arxiv.org/html/2510.06879v1#bib.bib22), [25](https://arxiv.org/html/2510.06879v1#bib.bib25), [26](https://arxiv.org/html/2510.06879v1#bib.bib26)]. For the linear multi-asset setting, sufficient conditions for convolution kernels that preclude price manipulation have been derived in both the discrete-time [[5](https://arxiv.org/html/2510.06879v1#bib.bib5)] and the continuous-time case [[1](https://arxiv.org/html/2510.06879v1#bib.bib1)]. For the concave case, already for one asset, a large class of continuous-time models with a nonlinear impact function hh and a nonsingular propagator GG admits price manipulation (see Proposition 1 of [[21](https://arxiv.org/html/2510.06879v1#bib.bib21)]). Moreover, even for singular kernels such as the power-law propagator, examples of price manipulation can be constructed [[15](https://arxiv.org/html/2510.06879v1#bib.bib15), [20](https://arxiv.org/html/2510.06879v1#bib.bib20)]. To complement those findings, we extend Proposition 1 of [[21](https://arxiv.org/html/2510.06879v1#bib.bib21)] to the discrete-time setting from ([1.2](https://arxiv.org/html/2510.06879v1#S1.E2 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")), demonstrating that price manipulation cannot be ruled out for nonsingular convolution kernels and nonlinear impact functions in the discrete-time case either (see Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")). As our result applies only to nonsingular kernels, we nevertheless adopt the concave model in our empirical analysis, mainly motivated by its superior goodness-of-fit.

One of the main practical challenges in applying the estimator to proprietary metaorder data lies in data scarcity. Institutional investors often execute only a single metaorder per day per asset, meaning that even long historical datasets rarely contain more than 10001000 metaorders per asset. This limited sample size is insufficient to reliably estimate high-dimensional impact kernels, especially when accounting for liquidity- or tick-size-specific effects. To address this, a proprietary dataset from CFM is enhanced using the synthetic metaorder generation procedure introduced in [[29](https://arxiv.org/html/2510.06879v1#bib.bib29)], which is inspired by empirical findings in [[30](https://arxiv.org/html/2510.06879v1#bib.bib30), [41](https://arxiv.org/html/2510.06879v1#bib.bib41)]. These synthetic metaorders are constructed by randomly sampling from tick-by-tick data and assigning trades to proxy metaorders via a systematic prescription described in Section [3.2](https://arxiv.org/html/2510.06879v1#S3.SS2 "3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact").

In our empirical analysis, the propagator kernel is estimated nonparametrically using two metaorder datasets: CFM’s proprietary corn futures trades over a ten-year horizon and an enhanced version where we augment the dataset with synthetic metaorders. The enhanced dataset yields a smoother kernel that better captures the decay of impact, as shown in Figure [1](https://arxiv.org/html/2510.06879v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact"). In particular, we find that self-impact decays across multiple timescales without assuming any specific kernel shape. Additionally, self-impact estimations on the original CFM dataset show that concavity is a crucial driver of predictive power. Models with square-root impact systematically outperform their linear counterparts, in line with prior evidence [[23](https://arxiv.org/html/2510.06879v1#bib.bib23)]. Moreover, incorporating cross-impact across contracts with different expiries provides an additional and statistically significant gain in explanatory power. In particular, predictive accuracy improves when cross-impact is modeled as concave rather than linear, suggesting that the square-root law extends to cross-impact. Finally, we find that multi-asset estimations reveal asymmetric cross-impact patterns caused by relative liquidity differences, with more liquid assets exerting stronger and more persistent impacts on their less liquid counterparts. See Section [3.4](https://arxiv.org/html/2510.06879v1#S3.SS4 "3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") for details.

![Refer to caption](x1.png)


Figure 1: Estimated self-impact kernel for the square-root model (c=0.5c=0.5) using CFM’s proprietary data (gray) and the enhanced dataset with synthetic metaorders (blue) together with the projection of the kernel (dahed blue). The calibration is performed on metaorders for three corn futures with staggered maturities traded on the Chicago Mercantile Exchange (CME) between 2012 and 2022.

As a complementary analysis, we apply the nonparametric estimator to a public order flow dataset for US equities, shifting the focus from the impact of a single agent to the market’s price response to aggregate order flow imbalance. The nonparametric estimator confirms a shifted power-law decay of self-impact without imposing any parametric form, as illustrated in Figure [2](https://arxiv.org/html/2510.06879v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact"). Moreover, the projection onto a set of kernels with shape constraints markedly improves out-of-sample stability relative to the raw kernel. Predictive performance is driven primarily by concavity: square-root–type specifications outperform linear ones, with the optimal concavity for binned order flow being lower than that for metaorders, reflecting larger effective sizes in aggregated bins. Incorporating cross-impact further increases explanatory power, with concave cross-impact outperforming linear cross-impact, and we observe asymmetric cross-impact effects due to relative liquidity differences. Altogether, our results show that the setting based on order flow exhibits the same qualitative structure as the metaorder setting. See Section [3.5](https://arxiv.org/html/2510.06879v1#S3.SS5 "3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") for details.

![Refer to caption](x2.png)


Figure 2: Estimated self-impact kernel for the square-root model (c=0.5c=0.5) using aggregate order flow imbalance averaged over 197 stocks of the S&P 500 in 2024 (gray) and the corresponding power-law fit (blue).

##### Our main contributions.

Below we summarize our main contributions in detail:

1. 1.

   We extend the offline nonparametric estimator of [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] from the linear single-asset setting to the concave multi-asset framework from ([1.4](https://arxiv.org/html/2510.06879v1#S1.E4 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")). Our extension allows distinct self-impact and cross-impact concavities, and yields confidence bounds for the estimator (see Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")).
   Importantly, the nonparametric estimator avoids a parameter explosion in the multi-asset setting. While parametric propagators with single-exponential (1-EXP), double-exponential (2-EXP), or power-law (POWER) decay require up to 𝒪​(d2)\mathcal{O}(d^{2}) tuned parameters and thus a grid search that scales quadratically in the number of assets dd, the nonparametric propagator (RAW) and its projection enforcing shape constraints (PROJ) require none (see Tables [1](https://arxiv.org/html/2510.06879v1#S1.T1 "Table 1 ‣ Our main contributions. ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact") and [3](https://arxiv.org/html/2510.06879v1#S3.T3 "Table 3 ‣ Price Impact Models ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")).
2. 2.

   We prove that the discrete-time impact model in ([1.2](https://arxiv.org/html/2510.06879v1#S1.E2 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")) admits price manipulation whenever GG is a convolution kernel that is continuous in 0 with G​(0)>0G(0)>0 and h:ℝ→ℝh:{\mathbb{R}}\to{\mathbb{R}} is continuous, odd, and not linear (see Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")). This result extends Proposition 1 of [[21](https://arxiv.org/html/2510.06879v1#bib.bib21)] to the discrete-time setting.
3. 3.

   We extend the metaorder proxy method from [[29](https://arxiv.org/html/2510.06879v1#bib.bib29)], originally employed to augment sparse proprietary datasets, to the multi-asset setting. The proxy preserves key microstructure features, such as sign persistence and realistic size distribution, and materially stabilizes kernel estimates prior to projection (see Figure [1](https://arxiv.org/html/2510.06879v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact") and Section [3.2](https://arxiv.org/html/2510.06879v1#S3.SS2 "3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). As a result, we show on CFM’s proprietary metaorder data that the proxy improves the predictive power of single- and multi-asset impact models (see Table [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")).
4. 4.

   On CFM’s proprietary metaorder dataset, we confirm that self-impact is concave and decays across multiple timescales, with square-root impact doubling the prediction performance in terms of R2R^{2} compared to the linear case (see Table [4](https://arxiv.org/html/2510.06879v1#S3.T4 "Table 4 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and Figure [6](https://arxiv.org/html/2510.06879v1#S3.F6 "Figure 6 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). Moreover, we find that the proxy enhancement smoothens the decay and improves the R2R^{2} from 4.6% to 4.8%, and that adding additional assets raises it further to 6.3−6.5%6.3-6.5\% (see Figures [1](https://arxiv.org/html/2510.06879v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact"), [7](https://arxiv.org/html/2510.06879v1#S3.F7 "Figure 7 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and Table [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")), suggesting that the square-root law holds for cross-impact as well (see Table [5](https://arxiv.org/html/2510.06879v1#S3.T5 "Table 5 ‣ 3.4.2 Cross-Impact Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and Figure [6](https://arxiv.org/html/2510.06879v1#S3.F6 "Figure 6 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). We also measure asymmetric cross-impact dynamics caused by relative liquidity differences (see Figure [8](https://arxiv.org/html/2510.06879v1#S3.F8 "Figure 8 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")).
5. 5.

   On the public order flow dataset, we confirm that self-impact is concave and that the estimated decay kernel is best fitted by a shifted power-law (see Figures [2](https://arxiv.org/html/2510.06879v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact"), [9](https://arxiv.org/html/2510.06879v1#S3.F9 "Figure 9 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and Table [8](https://arxiv.org/html/2510.06879v1#S3.T8 "Table 8 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")), with the projected kernel significantly outperforming parametric models (see Table [7](https://arxiv.org/html/2510.06879v1#S3.T7 "Table 7 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). The introduction of cross-impact further improves prediction performance, with concave specifications outperforming linear ones as in the metaorder case (see Table [9](https://arxiv.org/html/2510.06879v1#S3.T9 "Table 9 ‣ 3.5.2 Cross-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). Finally, asymmetric cross-impact can be observed for highly correlated stocks as well (see Figure [10](https://arxiv.org/html/2510.06879v1#S3.F10 "Figure 10 ‣ 3.5.2 Cross-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")).

| Model | Propagator | Tuned parameters | Search dimension |
| --- | --- | --- | --- |
| 1-EXP | e−ρ​te^{-\rho t} | ρ\rho | d2d^{2} |
| 2-EXP | w1​e−ρ1​t+(1−w1)​e−ρ2​tw\_{1}e^{-\rho\_{1}t}+(1-w\_{1})e^{-\rho\_{2}t} | ρ1,ρ2\rho\_{1},\rho\_{2} | 2​d22d^{2} |
| POWER | (t+τ)−β(t+\tau)^{-\beta} | β,τ\beta,\tau | 2​d22d^{2} |
| RAW | G~​(t)\widetilde{G}(t) | None | 0 |
| PROJ | G​(t)G(t) | None | 0 |

Table 1: Propagators, tuned parameters per propagator, and number of tuned parameters needed for dd assets in the parametric models 1-EXP, 2-EXP, POWER and the nonparametric models RAW, PROJ described above. The number of concavity parameters is the same for all propagators, and therefore omitted for the model comparison.

##### Structure of the paper.

The remainder of this paper is structured as follows. Section [2](https://arxiv.org/html/2510.06879v1#S2 "2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") presents the theoretical foundations, that is, the definition of the concave multivariate propagator model and the offline estimator used for kernel calibration in Section [2.1](https://arxiv.org/html/2510.06879v1#S2.SS1 "2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), a price manipulation result for the model in Section [2.2](https://arxiv.org/html/2510.06879v1#S2.SS2 "2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), and a confidence interval for the estimator in Section [2.3](https://arxiv.org/html/2510.06879v1#S2.SS3 "2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"). Section [3](https://arxiv.org/html/2510.06879v1#S3 "3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") contains the empirical analysis, including the construction of synthetic metaorders in Section [3.2](https://arxiv.org/html/2510.06879v1#S3.SS2 "3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), the methodology needed for reliable kernel estimation in Section [3.3](https://arxiv.org/html/2510.06879v1#S3.SS3 "3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), the empirical findings for proprietary metaorder data in Section [3.4](https://arxiv.org/html/2510.06879v1#S3.SS4 "3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and the empirical findings for public order flow data in Section [3.5](https://arxiv.org/html/2510.06879v1#S3.SS5 "3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact").

## 2 Nonparametric Impact Estimation from Offline Data

This section introduces the offline dataset and methodology used to estimate the true impact kernel denoted by 𝑮∗=((G∗)(k,ℓ))\boldsymbol{G}^{\*}=\big((G^{\*})^{(k,\ell)}\big), that was introduced in ([1.4](https://arxiv.org/html/2510.06879v1#S1.E4 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")). The static dataset consists of either metaorders or order flow imbalances and their corresponding price trajectories observed across multiple time periods and assets.
A least-squares framework is used to estimate 𝑮∗\boldsymbol{G}^{\*}, in both an unconstrained and a constrained setting, where the constrained estimator enforces admissibility conditions derived from no-arbitrage arguments in the linear propagator model.

### 2.1 Offline Dataset

Throughout, we fix the number of assets d∈ℕd\in{\mathbb{N}}, a time horizon T>0T>0, and an equidistant partition 𝕋:={0=t0,t1,…,tM=T}\mathbb{T}:=\{0=t\_{0},t\_{1},\ldots,t\_{M}=T\} of the interval [0,T][0,T] consisting of M∈ℕM\in{\mathbb{N}} subintervals. The offline dataset is defined as follows.

###### Definition 2.1.

Let N∈ℕN\in\mathbb{N} be the number of episodes in the dataset and consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟={(𝑷ti(n))i=0M,(𝑸ti(n))i=0M−1|n=1,…,N},\mathcal{D}=\left\{(\boldsymbol{P}\_{t\_{i}}^{(n)})^{M}\_{i=0},(\boldsymbol{Q}\_{t\_{i}}^{(n)})^{M-1}\_{i=0}\,\Big|\,n=1,\dots,N\right\}, |  | (2.1) |

where 𝐏ti(n)=((Pti1)(n),…,(Ptid)(n))⊤∈ℝd\boldsymbol{P}^{(n)}\_{t\_{i}}=\left((P\_{t\_{i}}^{1})^{(n)},\ldots,(P\_{t\_{i}}^{d})^{(n)}\right)^{\top}\in{\mathbb{R}}^{d} and 𝐐ti(n)=((Qti1)(n),…,(Qtid)(n))⊤∈ℝd\boldsymbol{Q}^{(n)}\_{t\_{i}}=\left((Q\_{t\_{i}}^{1})^{(n)},\dots,(Q\_{t\_{i}}^{d})^{(n)}\right)^{\top}\in{\mathbb{R}}^{d} respectively capture the observed price and traded volume for all dd assets at time tit\_{i} in the nn-th episode. For n=1,…,Nn=1,\ldots,N,
define 𝐏(n):=(𝐏ti(n))i=0M\smash{\boldsymbol{P}^{(n)}:=(\boldsymbol{P}^{(n)}\_{t\_{i}})\_{i=0}^{M}} and 𝐐(n):=(𝐐ti(n))i=0M−1\smash{\boldsymbol{Q}^{(n)}:=(\boldsymbol{Q}^{(n)}\_{t\_{i}})\_{i=0}^{M-1}}.

We call 𝒟\mathcal{D} an offline dataset if (𝐏(n),𝐐(n))n=1N(\boldsymbol{P}^{(n)},\boldsymbol{Q}^{(n)})\_{n=1}^{N}
are realizations of random variables defined on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P})
satisfying the following properties: for each episode n∈{1,…,N}n\in\{1,\ldots,N\}, 𝐐(n)\boldsymbol{Q}^{(n)} is measurable with respect to the σ\sigma-algebra ℱn−1\mathcal{F}\_{n-1}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱn−1=σ​{(𝑷(r))r=1n−1,(𝑸(r))r=1n−1},\mathcal{F}\_{n-1}=\sigma\left\{\big(\boldsymbol{P}^{(r)}\big)\_{r=1}^{n-1},\big(\boldsymbol{Q}^{(r)}\big)\_{r=1}^{n-1}\right\}, |  | (2.2) |

and there exist ℱn\mathcal{F}\_{n}-measurable random variables ϵti(n)=((ϵti1)(n),…,(ϵtid)(n))⊤\boldsymbol{\epsilon}^{(n)}\_{t\_{i}}=\big((\epsilon^{1}\_{t\_{i}})^{(n)},\ldots,(\epsilon^{d}\_{t\_{i}})^{(n)}\big)^{\top}
such that the price evolution follows a concave multi-asset propagator model with additive noise,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑷ti+1(n)−𝑷t0(n)=∑j=0i𝑮i−j∗​h​(𝑸tj(n))+ϵti(n),i=0,…,M−1,\boldsymbol{P}^{(n)}\_{t\_{i+1}}-\boldsymbol{P}^{(n)}\_{t\_{0}}=\sum\_{j=0}^{i}\boldsymbol{G}^{\*}\_{i-j}h(\boldsymbol{Q}^{(n)}\_{t\_{j}})+\boldsymbol{\epsilon}^{(n)}\_{t\_{i}},\quad i=0,\ldots,M-1, |  | (2.3) |

where 𝐆∗∈ℝM×d×d\boldsymbol{G}^{\*}\in\mathbb{R}^{M\times d\times d} is the true (unknown) convolution kernel and h:ℝ→ℝh:{\mathbb{R}}\to{\mathbb{R}} is a continuous, increasing function that is concave on [0,∞)[0,\infty) and is applied elementwise. The random variables satisfy 𝔼​[ϵti(n)|ℱn−1]=0\smash{\mathbb{E}[\boldsymbol{\epsilon}\_{t\_{i}}^{(n)}|\mathcal{F}\_{n-1}]=0} and 𝔼​[(ϵti(n))⊤​ϵti(n)]<∞\smash{\mathbb{E}[(\boldsymbol{\epsilon}^{(n)}\_{t\_{i}})^{\top}\boldsymbol{\epsilon}^{(n)}\_{t\_{i}}]<\infty} for all i=0,…,M−1i=0,\dots,M-1.

###### Remark 2.2.

A common specification of the concave impact function hh in Definition [2.1](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") is

|  |  |  |  |
| --- | --- | --- | --- |
|  | hc​(x)=sgn⁡(x)​|x|c,c∈(0,1],h\_{c}(x)=\operatorname{sgn}(x)|x|^{c},\quad c\in(0,1], |  | (2.4) |

which we also use in the empirical analysis in Section [3](https://arxiv.org/html/2510.06879v1#S3 "3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"). In practice, ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) can be generalized by letting the concavity depend on the asset pair. A case of particular interest is a two-parameter version in which self- and cross-impact are governed by hcSh\_{c\_{S}} and hcXh\_{c\_{X}} for constants cS,cX∈(0,1]c\_{S},c\_{X}\in(0,1], respectively. While Definition [2.1](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") does not cover this variant, it can be incorporated with minor notational changes, and all subsequent arguments carry over unchanged.

Define ϵ(n):=(ϵti(n))i=0M−1\smash{\boldsymbol{\epsilon}^{(n)}:=(\boldsymbol{\epsilon}^{(n)}\_{t\_{i}})\_{i=0}^{M-1}}. For any k∈ℕk\in{\mathbb{N}} and u,v∈ℝku,v\in{\mathbb{R}}^{k}, we denote by ⟨u,v⟩ℝk\langle u,v\rangle\_{{\mathbb{R}}^{k}} the inner product in ℝk{\mathbb{R}}^{k} and by ‖v‖ℝk\|v\|\_{{\mathbb{R}}^{k}} the Euclidean norm. In line with [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)], the noise is assumed to be conditionally sub-Gaussian. This assumption enables the application of high-probability bounds to the estimated propagator matrices. Moreover, this setting is versatile enough to allow for dependence between the price trajectories in consecutive trading periods.

###### Assumption 2.3.

Given an offline dataset 𝒟\mathcal{D} of size N∈ℕN\in\mathbb{N}, there exists a known constant R>0R>0 such that for all n=1,…,Nn=1,\ldots,N,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[exp⁡(⟨v,ϵ(n)⟩ℝM​d)|ℱn−1]≤exp⁡(R2​‖v‖ℝM​d22),for all ​v∈ℝM​d,\mathbb{E}\Big[\exp\big(\langle v,\boldsymbol{\epsilon}^{(n)}\rangle\_{{\mathbb{R}}^{Md}}\big)|\mathcal{F}\_{n-1}\Big]\leq\exp\left(\frac{R^{2}\|v\|\_{{\mathbb{R}}^{Md}}^{2}}{2}\right),\quad\text{for all }v\in\mathbb{R}^{Md}, |  | (2.5) |

that is, each ϵ(n)\boldsymbol{\epsilon}^{(n)} is RR-conditionally sub-Gaussian with respect to ℱn−1\mathcal{F}\_{n-1}.

### 2.2 Price Manipulation and Admissible Kernels

Let 𝑮∈ℝM×d×d\boldsymbol{G}\in\mathbb{R}^{M\times d\times d} be a propagator kernel and 𝑸:=(𝑸ti)i=0M−1\boldsymbol{Q}:=(\boldsymbol{Q}\_{t\_{i}})\_{i=0}^{M-1} with

|  |  |  |
| --- | --- | --- |
|  | 𝑸ti=((Qti1),…,(Qtid))⊤∈ℝd\boldsymbol{Q}\_{t\_{i}}=\left((Q\_{t\_{i}}^{1}),\ldots,(Q\_{t\_{i}}^{d})\right)^{\top}\in{\mathbb{R}}^{d} |  |

be a sequence of trades in the dd assets. In line with Lemma 1 of [[5](https://arxiv.org/html/2510.06879v1#bib.bib5)], it follows from ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) that the total execution costs corresponding to 𝑸\boldsymbol{Q} caused by the self- and cross-impact associated with 𝑮\boldsymbol{G} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞𝕋​(𝑸):=12​∑i,j=0M−1𝑸ti⊤​𝑮¯i−j​h​(𝑸tj),\mathcal{C}\_{\mathbb{T}}(\boldsymbol{Q}):=\frac{1}{2}\sum\_{i,j=0}^{M-1}\boldsymbol{Q}\_{t\_{i}}^{\top}\bar{\boldsymbol{G}}\_{i-j}h(\boldsymbol{Q}\_{t\_{j}}), |  | (2.6) |

where 𝑮¯∈ℝ(2​M−1)×d×d\bar{\boldsymbol{G}}\in\mathbb{R}^{(2M-1)\times d\times d} is given by

|  |  |  |
| --- | --- | --- |
|  | 𝑮¯i={𝑮i,1≤i≤M−1,12​(𝑮0+𝑮0⊤),i=0,𝑮−i⊤,1≤−i≤M−1.\bar{\boldsymbol{G}}\_{i}=\begin{cases}\boldsymbol{G}\_{i},\phantom{\frac{1}{2}(\boldsymbol{G}\_{0}+\boldsymbol{G}\_{0}^{\top})\boldsymbol{G}\_{-i}^{\top}}1\leq i\leq M-1,\\ \frac{1}{2}(\boldsymbol{G}\_{0}+\boldsymbol{G}\_{0}^{\top}),\phantom{\boldsymbol{G}\_{i}\boldsymbol{G}\_{-i}^{\top}}i=0,\\ \boldsymbol{G}\_{-i}^{\top},\phantom{\boldsymbol{G}\_{i}\frac{1}{2}(\boldsymbol{G}\_{0}+\boldsymbol{G}\_{0}^{\top})}1\leq-i\leq M-1.\end{cases} |  |

The condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞𝕋​(𝑸)≥0,for all ​𝑸=(𝑸ti)i=0M−1​ and all ​𝕋,\mathcal{C}\_{\mathbb{T}}(\boldsymbol{Q})\geq 0,\quad\text{for all }\boldsymbol{Q}=(\boldsymbol{Q}\_{t\_{i}})\_{i=0}^{M-1}\text{ and all }\mathbb{T}, |  | (2.7) |

is a regularity condition for the underlying impact model that rules out the possibility of profiting from exploiting one’s own market impact (see, e.g., [[1](https://arxiv.org/html/2510.06879v1#bib.bib1), [5](https://arxiv.org/html/2510.06879v1#bib.bib5), [20](https://arxiv.org/html/2510.06879v1#bib.bib20), [21](https://arxiv.org/html/2510.06879v1#bib.bib21), [22](https://arxiv.org/html/2510.06879v1#bib.bib22), [24](https://arxiv.org/html/2510.06879v1#bib.bib24)]). For linear cross-impact (h​(x)=xh(x)=x), conditions that prevent price manipulation have been derived in Theorem 2 of [[5](https://arxiv.org/html/2510.06879v1#bib.bib5)] for the discrete-time case and in Theorem 2.14 of [[1](https://arxiv.org/html/2510.06879v1#bib.bib1)] for the continuous-time case (see also Theorem 1.2 of [[35](https://arxiv.org/html/2510.06879v1#bib.bib35)] for their equivalence). To preclude price manipulation, kernels must be nonnegative, convex, symmetric, and nonincreasing. However, the present work incorporates concave impact functions hh, for which the theoretical understanding of admissibility is more involved. For the continuous-time case, it is known that already for a single asset any model with a nonlinear impact function hh and a kernel 𝑮\boldsymbol{G} that is nonsingular at time zero admits price manipulation (see Proposition 1 of [[21](https://arxiv.org/html/2510.06879v1#bib.bib21)]). Moreover, even for singular kernels such as the power-law propagator, examples for price manipulation can be constructed (see [[15](https://arxiv.org/html/2510.06879v1#bib.bib15), [20](https://arxiv.org/html/2510.06879v1#bib.bib20)]). The following theorem shows that there is not much hope to rule out price manipulation for the discrete-time case either.

###### Theorem 2.4.

Let H:[0,T]2→ℝH:[0,T]^{2}\to{\mathbb{R}} and suppose that there exists t∗∈[0,T)t^{\*}\in[0,T) such that HH is continuous in (t∗,t∗)(t^{\*},t^{\*}) with H​(t∗,t∗)>0H(t^{\*},t^{\*})>0. Let h:ℝ→ℝh:\mathbb{R}\to\mathbb{R} be continuous, odd function which is not linear, that is, not of the form h​(x)=q​xh(x)=qx for some q∈ℝq\in{\mathbb{R}}.
Then for every M≥3M\geq 3 there exist t0<…<tM−1t\_{0}<\ldots<t\_{M-1} and x0,…,xM−1∈ℝx\_{0},\dots,x\_{M-1}\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ∑i,j=0M−1xi​H​(ti,tj)​h​(xj)< 0.\sum\_{i,j=0}^{M-1}x\_{i}\,H(t\_{i},t\_{j})\,h(x\_{j})\;<\;0. |  |

In particular, given a kernel G:[0,T]→ℝG:[0,T]\to{\mathbb{R}} that is continuous in 0 with G​(0)>0G(0)>0, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i,j=0M−1xi​G​(|ti−tj|)​h​(xj)< 0.\sum\_{i,j=0}^{M-1}x\_{i}\,G(|t\_{i}-t\_{j}|)\,h(x\_{j})\;<\;0. |  | (2.8) |

The proof of Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") is given in the Appendix [B](https://arxiv.org/html/2510.06879v1#A2 "Appendix B Proofs ‣ Nonparametric Estimation of Self- and Cross-Impact").

###### Remark 2.5.

By ([2.6](https://arxiv.org/html/2510.06879v1#S2.E6 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) and ([2.7](https://arxiv.org/html/2510.06879v1#S2.E7 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), for any GG and hh as in Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), the corresponding single-asset impact model admits price manipulation. In particular, Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") extends Proposition 1 of [[21](https://arxiv.org/html/2510.06879v1#bib.bib21)] to the discrete-time setting.

###### Remark 2.6.

A concave impact model in which the absence of price manipulation can be ensured is the Alfonsi-Fruth-Schied model (see [[2](https://arxiv.org/html/2510.06879v1#bib.bib2), [3](https://arxiv.org/html/2510.06879v1#bib.bib3), [4](https://arxiv.org/html/2510.06879v1#bib.bib4), [21](https://arxiv.org/html/2510.06879v1#bib.bib21), [40](https://arxiv.org/html/2510.06879v1#bib.bib40)]). For a related multi-asset framework, necessary conditions for this absence in terms of kernel matrix properties were recently established in [[24](https://arxiv.org/html/2510.06879v1#bib.bib24)] (see Lemma 5.1 therein). Notably, when the concavity parameter cc of the impact function hch\_{c} from ([2.4](https://arxiv.org/html/2510.06879v1#S2.E4 "In Remark 2.2. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) is contained in [0.5,1][0.5,1], the conditions closely resemble those in the linear setting. While the Alfonsi-Fruth-Schied model provides a useful framework to study concave impact, it is not suitable for our purposes, since it relies on the assumption that the impact decays exponentially. Moreover, its calibration requires additional data compared to the model in ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), which is often not available in proprietary metaorder datasets.

In this work, given that Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") only holds for nonsingular kernels and that the introduction of shape constraints in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] improves the kernel estimation, we adopt and slightly relax the admissibility conditions from the linear case (see Theorem 2.14 in [[1](https://arxiv.org/html/2510.06879v1#bib.bib1)] and Theorem 2 in [[5](https://arxiv.org/html/2510.06879v1#bib.bib5)]). As we will see in our empirical analysis, this will significantly improve the model’s out-of-sample performance (see Section [3](https://arxiv.org/html/2510.06879v1#S3 "3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). To wit, we no longer enforce symmetry of the propagator matrix to allow for asymmetric cross-impact across assets. The resulting class of admissible kernels includes all 𝑮∈ℝM×d×d\boldsymbol{G}\in\mathbb{R}^{M\times d\times d} such that the induced matrix-valued map {0,…,M−1}→ℝd×d,i↦𝑮i\{0,\ldots,M-1\}\rightarrow\mathbb{R}^{d\times d},\ i\mapsto\boldsymbol{G}\_{i} is nonnegative, nonincreasing, and convex. Formally, the set of admissible kernels is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢ad:={𝑮=(𝑮i)i=0M−1|v⊤​𝑮i​v≥0,0≤i≤M−1,v⊤​𝑮i+1​v≤v⊤​𝑮i​v,0≤i≤M−2,v⊤​(𝑮i+2−𝑮i+1)​v≤v⊤​(𝑮i+1−𝑮i)​v,0≤i≤M−3,for all ​v∈ℝd.}.\mathcal{G}\_{\mathrm{ad}}:=\left\{\boldsymbol{G}=\left(\boldsymbol{G}\_{i}\right)^{M-1}\_{i=0}\ \left|\ \begin{aligned} &v^{\top}\boldsymbol{G}\_{i}v\geq 0,&&0\leq i\leq M-1,\\ &v^{\top}\boldsymbol{G}\_{i+1}v\leq v^{\top}\boldsymbol{G}\_{i}v,&&0\leq i\leq M-2,\\ &v^{\top}(\boldsymbol{G}\_{i+2}-\boldsymbol{G}\_{i+1})v\leq v^{\top}(\boldsymbol{G}\_{i+1}-\boldsymbol{G}\_{i})v,\ &&0\leq i\leq M-3,\\ &\text{for all }v\in\mathbb{R}^{d}.\end{aligned}\right.\right\}. |  | (2.9) |

In ([2.9](https://arxiv.org/html/2510.06879v1#S2.E9 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), the first, second, and third conditions respectively ensure nonnegativity, monotonicity, and convexity of 𝑮\boldsymbol{G}, respectively. This translates into requiring that the self-impact terms are nonnegative and dominate the cross-impact terms, and that all impact terms decay in a convex manner.
Typical examples of cross-impact propagator matrices in 𝒢ad\mathcal{G}\_{\mathrm{ad}} include kernels with exponential or power-law decay; see Example 2.2 in [[1](https://arxiv.org/html/2510.06879v1#bib.bib1)] for a comprehensive overview.

###### Remark 2.7.

In ([2.9](https://arxiv.org/html/2510.06879v1#S2.E9 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), we may additionally require the following symmetry condition,

|  |  |  |
| --- | --- | --- |
|  | 𝑮i=𝑮i⊤,0≤i≤M−1,\boldsymbol{G}\_{i}=\boldsymbol{G}\_{i}^{\top},\quad 0\leq i\leq M-1, |  |

without affecting any of the results below. As expounded above, this ensures the absence of price manipulation in the case of linear impact (see Theorem 2 in [[5](https://arxiv.org/html/2510.06879v1#bib.bib5)]), but it restricts attention to symmetric cross-impact. However, because our focus is on concave impact, where such no-manipulation guarantees generally fail, we retain the baseline definition of 𝒢ad\mathcal{G}\_{\mathrm{ad}} in ([2.9](https://arxiv.org/html/2510.06879v1#S2.E9 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")).

### 2.3 Nonparametric Estimation

The true unknown propagator matrix 𝑮∗∈ℝM×d×d\boldsymbol{G}^{\*}\in{\mathbb{R}}^{M\times d\times d} is estimated via a least-squares method with constraints. For this, we introduce the following convention.

###### Convention 2.8.

Given 𝐆∈ℝM×d×d\boldsymbol{G}\in{\mathbb{R}}^{M\times d\times d}, we identify ℝM×d×d{\mathbb{R}}^{M\times d\times d} with ℝM​d2{\mathbb{R}}^{Md^{2}} via the vectorization that stacks entries so that ℓ∈{1,…,d}\ell\in\{1,\ldots,d\} is the slowest-varying index, then i∈{0,…,M−1}i\in\{0,\ldots,M-1\}, and k∈{1,…,d}k\in\{1,\ldots,d\} is the fastest:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑮=(G0(1,1),…,G0(1,d),…,GM−1(1,1),…,GM−1(1,d),…,G0(d,1),…,G0(d,d),…,GM−1(d,1),…,GM−1(d,d))⊤.\boldsymbol{G}=\left(G^{(1,1)}\_{0},\ldots,G^{(1,d)}\_{0},\ldots,G^{(1,1)}\_{M-1},\ldots,G^{(1,d)}\_{M-1},\ldots,G^{(d,1)}\_{0},\ldots,G^{(d,d)}\_{0},\ldots,G^{(d,1)}\_{M-1},\ldots,G^{(d,d)}\_{M-1}\right)^{\top}. |  | (2.10) |

By this identification, we will always use the same notation for the tensor and its vectorization, writing 𝐆\boldsymbol{G} for either, with the intended meaning clear from context.

For each episode n∈{1,…,N}n\in\{1,\ldots,N\}, define the vector of observed returns 𝒚(n)∈ℝM​d\boldsymbol{y}^{(n)}\in\mathbb{R}^{Md} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚(n)=(((Pti+11)(n)−(Pt01)(n))i=0M−1⋮((Pti+1d)(n)−(Pt0d)(n))i=0M−1).\boldsymbol{y}^{(n)}=\begin{pmatrix}\big((P\_{t\_{i+1}}^{1})^{(n)}-(P\_{t\_{0}}^{1})^{(n)}\big)\_{i=0}^{M-1}\\ \vdots\\ \big((P\_{t\_{i+1}}^{d})^{(n)}-(P\_{t\_{0}}^{d})^{(n)}\big)\_{i=0}^{M-1}\end{pmatrix}. |  | (2.11) |

Moreover, define the auxiliary matrices 𝑫(n)∈ℝM×(M​d)\boldsymbol{D}^{(n)}\in\mathbb{R}^{M\times(Md)} and 𝑼(n)∈ℝ(M​d)×(M​d2)\boldsymbol{U}^{(n)}\in\mathbb{R}^{(Md)\times(Md^{2})} capturing the transformed traded volume as

|  |  |  |
| --- | --- | --- |
|  | 𝑫(n)=(h​((Qt01)(n))…h​((Qt0d)(n))0…0h​((Qt11)(n))…h​((Qt1d)(n))h​((Qt01)(n))…0⋮⋮⋮⋮⋱⋮h​((QtM−11)(n))…h​((QtM−1d)(n))h​((QtM−21)(n))…h​((Qt0d)(n))),\boldsymbol{D}^{(n)}=\begin{pmatrix}h\big((Q^{1}\_{t\_{0}})^{(n)}\big)&\dots&h\big((Q^{d}\_{t\_{0}})^{(n)}\big)&0&\dots&0\\ h\big((Q^{1}\_{t\_{1}})^{(n)}\big)&\dots&h\big((Q^{d}\_{t\_{1}})^{(n)}\big)&h\big((Q^{1}\_{t\_{0}})^{(n)}\big)&\dots&0\\ \vdots&\vdots&\vdots&\vdots&\ddots&\vdots\\ h\big((Q^{1}\_{t\_{M-1}})^{(n)}\big)&\dots&h\big((Q^{d}\_{t\_{M-1}})^{(n)}\big)&h\big((Q^{1}\_{t\_{M-2}})^{(n)}\big)&\dots&h\big((Q^{d}\_{t\_{0}})^{(n)}\big)\end{pmatrix}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑼(n)=(𝑫(n)0…00𝑫(n)⋱⋮⋮⋱⋱00…0𝑫(n)).\boldsymbol{U}^{(n)}=\begin{pmatrix}\boldsymbol{D}^{(n)}&0&\dots&0\\ 0&\boldsymbol{D}^{(n)}&\ddots&\vdots\\ \vdots&\ddots&\ddots&0\\ 0&\dots&0&\boldsymbol{D}^{(n)}\end{pmatrix}. |  | (2.12) |

Then, by ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), ([2.10](https://arxiv.org/html/2510.06879v1#S2.E10 "In Convention 2.8. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), and ([2.12](https://arxiv.org/html/2510.06879v1#S2.E12 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), the observed returns in ([2.11](https://arxiv.org/html/2510.06879v1#S2.E11 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) satisfy the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚(n)=𝑼(n)​𝑮∗+ϵ(n).\boldsymbol{y}^{(n)}=\boldsymbol{U}^{(n)}\boldsymbol{G}^{\*}+\boldsymbol{\epsilon}^{(n)}. |  | (2.13) |

In line with [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)], this motivates us to consider the following constrained least-squares estimator,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑮N,λ:=arg​min𝑮∈𝒢ad⁡(∑n=1N‖𝒚(n)−𝑼(n)​𝑮‖ℝM​d2+λ​‖𝑮‖ℝM​d22),\boldsymbol{G}\_{N,\lambda}:=\operatorname\*{arg\,min}\_{\boldsymbol{G}\in\mathcal{G}\_{\mathrm{ad}}}\left(\sum\_{n=1}^{N}\left\|\boldsymbol{y}^{(n)}-\boldsymbol{U}^{(n)}\boldsymbol{G}\right\|\_{{\mathbb{R}}^{Md}}^{2}+\lambda\left\|\boldsymbol{G}\right\|\_{{\mathbb{R}}^{Md^{2}}}^{2}\right), |  | (2.14) |

where λ>0\lambda>0 is a regularization parameter, and 𝒢ad\mathcal{G}\_{\mathrm{ad}} is the set of admissible kernels from ([2.9](https://arxiv.org/html/2510.06879v1#S2.E9 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")).

###### Remark 2.9.

As noted in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)], the regularization parameter λ>0\lambda>0 ensures the strong convexity of ([2.14](https://arxiv.org/html/2510.06879v1#S2.E14 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) in 𝐆\boldsymbol{G}. Together with the fact that 𝒢ad\mathcal{G}\_{\mathrm{ad}} in ([2.9](https://arxiv.org/html/2510.06879v1#S2.E9 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) is nonempty, closed, and convex, we obtain that 𝐆N,λ\boldsymbol{G}\_{N,\lambda} is uniquely defined. This analogously holds when 𝒢ad\mathcal{G}\_{\mathrm{ad}} is modified as in Remark [2.7](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem7 "Remark 2.7. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"). This regularization parameter is necessary in general, as it ensures the invertibility of the matrix on the left-hand side of ([2.18](https://arxiv.org/html/2510.06879v1#S2.E18 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")). In the multivariate setting, asset-specific regularization parameters Λ=(λ(ℓ,k))ℓ,k=1d\Lambda=(\lambda^{(\ell,k)})\_{\ell,k=1}^{d} can be introduced in practice. The optimization problem ([2.14](https://arxiv.org/html/2510.06879v1#S2.E14 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) then becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑮N,Λ:=arg​min𝑮∈𝒢ad⁡(∑n=1N‖𝒚(n)−𝑼(n)​𝑮‖ℝM​d2+∑ℓ,k=1dλ(ℓ,k)​‖(Gi(ℓ,k))i=0M−1‖ℝM2).\boldsymbol{G}\_{N,\Lambda}:=\operatorname\*{arg\,min}\_{\boldsymbol{G}\in\mathcal{G}\_{\mathrm{ad}}}\left(\sum\_{n=1}^{N}\left\|\boldsymbol{y}^{(n)}-\boldsymbol{U}^{(n)}\boldsymbol{G}\right\|\_{{\mathbb{R}}^{Md}}^{2}\right.\left.+\sum\_{\ell,k=1}^{d}\lambda^{(\ell,k)}\left\|(G\_{i}^{(\ell,k)})\_{i=0}^{M-1}\right\|\_{{\mathbb{R}}^{M}}^{2}\right). |  | (2.15) |

The constrained estimator 𝑮N,λ\boldsymbol{G}\_{N,\lambda} in ([2.14](https://arxiv.org/html/2510.06879v1#S2.E14 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) can be computed by projecting the corresponding unconstrained least-squares estimator onto the set 𝒢ad\mathcal{G}\_{\mathrm{ad}}. Indeed, letting,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑮~N,λ:=arg​min𝑮∈ℝM​d2⁡(∑n=1N‖𝒚(n)−𝑼(n)​𝑮‖ℝM​d2+λ​‖𝑮‖ℝM​d22),\tilde{\boldsymbol{G}}\_{N,\lambda}:=\operatorname\*{arg\,min}\_{\boldsymbol{G}\in{\mathbb{R}}^{Md^{2}}}\left(\sum\_{n=1}^{N}\left\|\boldsymbol{y}^{(n)}-\boldsymbol{U}^{(n)}\boldsymbol{G}\right\|\_{{\mathbb{R}}^{Md}}^{2}+\lambda\left\|\boldsymbol{G}\right\|\_{{\mathbb{R}}^{Md^{2}}}^{2}\right), |  | (2.16) |

we have that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑮N,λ\displaystyle\boldsymbol{G}\_{N,\lambda} | =arg​min𝑮∈𝒢ad⁡‖WN,λ1/2​(𝑮−𝑮~N,λ)‖ℝM​d22,\displaystyle=\operatorname\*{arg\,min}\_{\boldsymbol{G}\in\mathcal{G}\_{\mathrm{ad}}}\left\|W^{1/2}\_{N,\lambda}\left(\boldsymbol{G}-\tilde{\boldsymbol{G}}\_{N,\lambda}\right)\right\|\_{{\mathbb{R}}^{Md^{2}}}^{2}, |  | (2.17) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | WN,λ:=∑n=1N(𝑼(n))⊤​𝑼(n)+λ​𝕀M​d2,𝑮~N,λ:=WN,λ−1​∑n=1N(𝑼(n))⊤​𝒚(n),W\_{N,\lambda}:=\sum\_{n=1}^{N}(\boldsymbol{U}^{(n)})^{\top}\boldsymbol{U}^{(n)}+\lambda\mathbb{I}\_{Md^{2}},\quad\tilde{\boldsymbol{G}}\_{N,\lambda}:=W^{-1}\_{N,\lambda}\sum\_{n=1}^{N}(\boldsymbol{U}^{(n)})^{\top}\boldsymbol{y}^{(n)}, |  | (2.18) |

where 𝒚(n)\boldsymbol{y}^{(n)} and 𝑼(n)\boldsymbol{U}^{(n)} are defined in ([2.11](https://arxiv.org/html/2510.06879v1#S2.E11 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) and ([2.12](https://arxiv.org/html/2510.06879v1#S2.E12 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), respectively, and 𝕀M​d2\mathbb{I}\_{Md^{2}} denotes the identity matrix of size (M​d2)×(M​d2)(Md^{2})\times(Md^{2}). That is, the unconstrained problem ([2.16](https://arxiv.org/html/2510.06879v1#S2.E16 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) is solved explicitly by ([2.18](https://arxiv.org/html/2510.06879v1#S2.E18 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), and the constrained problem ([2.14](https://arxiv.org/html/2510.06879v1#S2.E14 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) can be solved efficiently by means of ([2.17](https://arxiv.org/html/2510.06879v1#S2.E17 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) and standard convex optimization packages (see, e.g., [[16](https://arxiv.org/html/2510.06879v1#bib.bib16)]).

This estimation procedure extends the functional regression with structural constraints on the kernel shape from [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] to the multivariate setting. In particular, the confidence region of the estimated impact coefficients 𝑮N,λ\boldsymbol{G}\_{N,\lambda} in terms of the observed data can be derived analogously to Theorem 2.14 therein.

###### Theorem 2.10.

Suppose that the true propagator matrix 𝐆∗\boldsymbol{G}^{\*} is contained in the set of admissible kernels 𝒢ad\mathcal{G}\_{\mathrm{ad}} from ([2.9](https://arxiv.org/html/2510.06879v1#S2.E9 "In 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) and that Assumption [2.3](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem3 "Assumption 2.3. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") holds. For any λ>0\lambda>0, let the constrained least-squares estimator 𝐆N,λ\boldsymbol{G}\_{N,\lambda} be defined as in ([2.14](https://arxiv.org/html/2510.06879v1#S2.E14 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")). Then, for all λ>0\lambda>0 and δ∈(0,1)\delta\in(0,1), with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖WN,λ1/2​(𝑮N,λ−𝑮∗)‖ℝM​d2≤R​(2​log⁡(det(WN,λ)δ2​λM​d2))1/2+λ​‖WN,λ−1/2​𝑮∗‖ℝM​d2,\left\|{W\_{N,\lambda}^{1/2}}\big(\boldsymbol{G}\_{N,\lambda}-\boldsymbol{G}^{\*}\big)\right\|\_{{\mathbb{R}}^{Md^{2}}}\leq R\left(2\log\left(\frac{\det(W\_{N,\lambda})}{\delta^{2}\lambda^{Md^{2}}}\right)\right)^{1/2}+\lambda\left\|{W^{-1/2}\_{N,\lambda}}\boldsymbol{G}^{\*}\right\|\_{{\mathbb{R}}^{Md^{2}}}, |  | (2.19) |

where WN,λ=∑n=1N(𝐔(n))⊤​𝐔(n)+λ​𝕀M​d2W\_{N,\lambda}=\sum\_{n=1}^{N}(\boldsymbol{U}^{(n)})^{\top}\boldsymbol{U}^{(n)}+\lambda\mathbb{I}\_{Md^{2}} and R>0R>0 is the constant from Assumption [2.3](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem3 "Assumption 2.3. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact").

###### Remark 2.11.

Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") extends Theorem 2.14 from [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] into two important directions. First, it allows the introduction of a concave impact function hh as in ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")). More importantly, it allows the analysis of a portfolio of dd assets with cross-impact across them as specified in ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")). Note that the convergence rate in Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") remains similar to the one in Theorem 2.14 from [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)], with the only difference being the dimensional scaling. Since the estimator now involves d2d^{2} kernels over MM time steps, the determinant term contributes a factor of λ−M​d2\lambda^{-Md^{2}} instead of λ−M\lambda^{-M}.

The proof of Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") is deferred to the Appendix [B](https://arxiv.org/html/2510.06879v1#A2 "Appendix B Proofs ‣ Nonparametric Estimation of Self- and Cross-Impact").

## 3 Empirical Analysis

This section presents the nonparametric estimation of self- and cross-impact propagators for metaorders on futures contracts and for aggregate order flow on S&P 500 stocks. In both cases, self-impact models are calibrated and evaluated first, followed by cross-impact models. Moreover, their prediction performance is compared to established parametric models with single-exponential, double-exponential, and power-law decay. As the number of observed metaorders in a single contract is limited, a proxy mechanism is employed to synthetically augment the dataset. Using corn futures as an example, we show that this augmentation enables more robust estimation of the impact kernel. The results indicate that concave impact functions outperform their linear counterparts in the single-asset case. Accordingly, the identified concavity parameter is retained for subsequent model calibration within the multivariate framework involving contracts with different maturities.

### 3.1 Datasets

Our study draws on a combination of proprietary and public datasets including various asset classes. These datasets serve distinct but complementary research purposes: the first two focus on the estimation of price impact from metaorders in futures markets, while the third examines order flow imbalance in equity markets.

#### 1. Metaorders on energy and agricultural futures

We start by integrating proprietary execution data from Capital Fund Management (CFM), consisting of 12,00012,000 metaorders across energy and agricultural futures, including oil, gas, metals, corn, wheat, and soybeans traded on the Chicago Mercantile Exchange (CME) from 2012 to 2022. The inherent challenge stems from the disparate trading hours - energy futures exhibit near-continuous 23-hour trading sessions, whereas agricultural products have intraday breaks. To address this, we constrain our analysis to a synchronous trading window from 9:30 AM to 2:20 PM Eastern Time (ET), enabling a consistent interpretation of execution trajectories across the combined dataset.

#### 2. Synthetic metaorders on corn futures

To delve deeper into the self- and cross-impact dynamics within the agricultural sector under conditions of sparse data, our analysis narrows to corn futures. We select three contracts with staggered maturities, all based on the same underlying and exhibiting return correlations above 90%. Specifically, we use the front contract (Corn0) and the next two deferred maturities (Corn1 and Corn2), expiring in one, two, and three quarters, respectively. This dataset comprises approximately 15001500 metaorders.

In recognizing the limited availability of proprietary metaorders, which restricts reliable impact estimation, we augment this dataset with a synthetic metaorder proxy specifically for corn futures. Inspired by empirical insights and methodologies highlighted in [[30](https://arxiv.org/html/2510.06879v1#bib.bib30), [41](https://arxiv.org/html/2510.06879v1#bib.bib41)], this proxy is constructed through an algorithm that introduces trade-sign autocorrelation and randomized trader ID assignment. This synthetic enrichment ensures consistency with observed market microstructure features and enhances the robustness of price impact estimation at the single-asset and portfolio level.

#### 3. Order flow imbalance in equities

Finally, we use high-frequency tick data from the LOBSTER database to analyze price dynamics driven by aggregate order flow imbalance. The dataset includes detailed order book events for all NASDAQ-traded stocks, in particular, all executed orders. Our study focuses on 197 constituents of the S&P 500 with complete data across all 237 regular trading days in 2024, where trading hours run from 9:30 AM to 4:00 PM ET.

Unlike the proprietary metaorder data, which enables the study of the price impact of an individual agent’s actions, this dataset allows us to model how prices respond to the total observed order flow in the market. It thus addresses a distinct but complementary question: not how one’s own trading moves prices, but how prices change as a result of aggregated traded volume. Understanding and quantifying this mechanism is crucial for the optimal execution of one’s own trades as well.

### 3.2 Metaorder Proxy

The number of available metaorders in the proprietary dataset is insufficient to support a reliable estimation of the impact kernel on a per-product basis. As shown in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)], the convergence rate of the estimator depends on both the number of samples and the number of trading periods MM. While the dataset does not permit an increase in MM, the number of effective samples can be enhanced by introducing a synthetic metaorder generation procedure, inspired by the findings in [[30](https://arxiv.org/html/2510.06879v1#bib.bib30)].

The approach originates from proprietary data on the Tokyo Stock Exchange, where the authors had access to full trade-level information, including trader identifiers. They observed that individual traders tend to execute consecutive trades in the same direction, forming buy or sell sequences. Metaorders were identified by aggregating consecutive trades of the same sign per trader, resetting upon sign reversal. The authors of [[29](https://arxiv.org/html/2510.06879v1#bib.bib29)] noticed that the presence of trader IDs was not essential to reproduce this behavior. Instead, one can simulate such identifiers by randomly assigning trades to synthetic IDs, thereby generating proxy metaorders via the following algorithm:

1. 1.

   Assign to each trade a random integer nT∈{0,1,…,NT−1}n\_{T}\in\{0,1,\ldots,N\_{T}-1\} where NTN\_{T} is a pre-determined fixed positive integer. The integers are sampled uniformly from this finite set, representing synthetic trader IDs.
2. 2.

   Group all trades with the same assigned nTn\_{T} and sort them in chronological order.
3. 3.

   Partition each sequence into metaorders by aggregating trades with identical signs (buy or sell), terminating the sequence upon sign change.

Table [2](https://arxiv.org/html/2510.06879v1#S3.T2 "Table 2 ‣ 3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") illustrates this procedure on a toy example. For instance, trades with nT=0n\_{T}=0 form a consistent sell-side sequence {−1,−1,−1}\{-1,-1,-1\}, corresponding to a single metaorder with three child orders. In contrast, trades with nT=1n\_{T}=1 exhibit a sign change, resulting in two separate metaorders with one and two child orders, respectively. The average length of a metaorder is influenced by both the chosen value for NTN\_{T} and the empirical rate of sign changes in the underlying trade flow.

Figure [3](https://arxiv.org/html/2510.06879v1#S3.F3 "Figure 3 ‣ 3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") displays the peak impact, as defined in ([1.1](https://arxiv.org/html/2510.06879v1#S1.E1 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")), for synthetic metaorders on TBOND, 10USNOTE, EUROSTOXX, DAX, and CORN0 futures, filtered to include only those with at least four child orders. All observed impact curves exhibit concave scaling behavior, consistent with a power-law relation. Empirically, the impact function fits a square-root law with exponent in the range δ∈[0.5,0.7]\delta\in[0.5,0.7]. The metaorder volume range is bounded below by microstructural properties (notably for large-tick assets such as DAX) and above by the decreasing likelihood of long, uninterrupted sign sequences in the trade flow. In practice, the upper bound is observed around 1% of the daily traded volume.

| Time | Volume Traded | Trader ID (nTn\_{T}) | Metaorder Assignment |
| --- | --- | --- | --- |
| 10:05:011 | -1 | 0 | 1 |
| 10:06:123 | -1 | 1 | 2 |
| 10:06:509 | -1 | 2 | 3 |
| 10:07:205 | -1 | 0 | 1 |
| 10:07:388 | 1 | 2 | 4 |
| 10:07:434 | 1 | 3 | 5 |
| 10:07:786 | -1 | 1 | 2 |
| 10:08:657 | -1 | 3 | 6 |
| 10:09:476 | -1 | 0 | 1 |
| 10:09:567 | 1 | 1 | 7 |

Table 2: Example of synthetic metaorder construction via randomized trader ID assignment and sign-based grouping.

![Refer to caption](x3.png)


Figure 3: For various futures contracts, the synthetic meta-order impact rescaled by daily volatility I/σDI/\sigma\_{D} is plotted against its volume fraction Q/VDQ/V\_{D} in log-log scale. The dashed black curve represents square-root scaling. The characteristic concave shape of the impact function is reproduced and holds broadly across assets.

Choosing NTN\_{T} requires careful calibration to the microstructural properties of the asset under study. For small NTN\_{T} (e.g., NT≈1N\_{T}\approx 1), artificially long metaorders are generated, which are unrealistic in practice. Conversely, large NTN\_{T} (e.g., NT≈N\_{T}\approx number of trades per day) results in metaorders with trades sparsely distributed over the day, diluting the temporal structure. Thus, intermediate values of NTN\_{T} must be selected to capture liquidity and volatility features of the asset.

The minimum and maximum feasible metaorder sizes depend on both the asset’s tick size and its intraday trade frequency. Figure [4](https://arxiv.org/html/2510.06879v1#S3.F4 "Figure 4 ‣ 3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") demonstrates that the smallest possible metaorder volume is influenced by the average trade size in the underlying asset. For large-tick assets, where the average trade size is relatively small, fewer shares are needed to achieve a significant dollar position, resulting in smaller metaorders. This suggests an inverse relationship between the minimum volume of metaorders and the average trade size of the asset. Consequently, the computational thresholds, which vary between 10−610^{-6} and 10−410^{-4}, as shown in Figure [3](https://arxiv.org/html/2510.06879v1#S3.F3 "Figure 3 ‣ 3.2 Metaorder Proxy ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), can be explained by the average tick size. Assets such as the DAX and CORN contracts exhibit larger thresholds compared to their smaller tick counterparts.

![Refer to caption](x4.png)


Figure 4: Minimum metaorder size as a function of the average trade size in the underlying asset. The metaorder volume depends on the tick-size of the underlying asset; large ticks require less trades to accumulate a large volume.

### 3.3 Methodology

#### Metaorders on futures

All metaorder-based analyses, whether from proprietary execution data or synthetic proxies, are conducted on a uniform 5-minute time grid. Even though some futures on the CME are traded 23 hours a day, we restrict ourselves to the most liquid trading hours that begin with the agricultural futures market opening at 9:30 AM ET and extends through 59 subsequent 5-minute bins, concluding at 1:20 PM. Return observations are constructed from this reference point. The corresponding volume process is set to zero in time bins where no trades occur. Assuming a Time-Weighted Average Price (TWAP) strategy, volumes during execution are presumed to be evenly distributed across the 5-minute bins.

To estimate cross-impact across multiple instruments, we analyze specific pairs and triplets of futures contracts that are have a correlation of more than 90%. This involves systematically pairing each front-month contract with its subsequent contract. For contracts nearing expiration, we exclude trading activity during the settlement period to avoid the peculiarities associated with end-of-life contract dynamics. This practice helps maintain the accuracy of cross-impact calibration.

#### Order flow imbalance in equities

All analyses based on order flow imbalance are carried out on an equidistant 10-second time grid. We partition the 6.5-hour trading session of the S&P 500, spanning from 9:30 AM to 4:00 PM ET, into 2340 distinct 10-second bins. This consistent partitioning aligns with established research [[14](https://arxiv.org/html/2510.06879v1#bib.bib14), [33](https://arxiv.org/html/2510.06879v1#bib.bib33), [34](https://arxiv.org/html/2510.06879v1#bib.bib34)], balancing the need for precision with data and absence of microstructure effects. The order flow imbalance is quantified as the cumulative sum of signed trade volumes within each bin.

From the original pool of 503 S&P 500 stocks as of December 31, 2024, we focus exclusively on constituents exhibiting active limit order book presence in at least 1800 bins per day. This condition narrows our analysis to 197 stocks. We exclude the final half-hour of the trading day to avoid the heightened volatility seen then, but retain the opening hour since price impact builds up most strongly during this period and is therefore essential for intraday decay estimation, resulting in a refined data set of 2160 bins per day.

To estimate cross-impact across multiple stocks, we analyze the stock pair Coca-Cola (KO), PepsiCo (PEP) and the stock triplet triplet ConocoPhillips (COP), Chevron (CVX), Exxon Mobil (XOM), which exhibit pairwise 10-second return correlations of 50-70% throughout 2024. In contrast to the case of metaorders on futures, we don’t have to account for expiries, settlements, or other contract dynamics here.

In line with [[33](https://arxiv.org/html/2510.06879v1#bib.bib33)], to assess the predictive power when introducing cross-impact, we consider a market portfolio and assess the prediction performance of a bivariate cross-impact model which captures cross-impact between the market portfolio and the stocks, instead of focusing on specific stock pairs. Here the market portfolio is constructed as a weighted sum, with prices and trades computed by weighting prices and trades of the individual assets by traded notional in the respective bin. Subsequently, the market portfolio is treated like an asset for the model calibration; see [[33](https://arxiv.org/html/2510.06879v1#bib.bib33)] for details.

#### Normalization

To correct for intraday volatility patterns in all datasets, such as higher volatility at the open and close, returns are scaled by a modified Garman–Klass volatility estimator. Recalling Definition [2.1](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), given an asset ℓ∈{1,…​d}\ell\in\{1,\ldots d\} and a time interval [tj,ti+1][t\_{j},t\_{i+1}] for 0≤j≤i≤M−10\leq j\leq i\leq M-1, consider

|  |  |  |
| --- | --- | --- |
|  | σ[tj,ti+1]ℓ:=13​(High−Low)[tj,ti+1]ℓ+23​|Last−First|[tj,ti+1]ℓ,\sigma^{\ell}\_{[t\_{j},t\_{i+1}]}:=\frac{1}{3}(\text{High}-\text{Low})\_{[t\_{j},t\_{i+1}]}^{\ell}+\frac{2}{3}|\text{Last}-\text{First}|\_{[t\_{j},t\_{i+1}]}^{\ell}, |  |

where "High" and "Low" represent the highest and lowest price within the respective interval and "First" and "Last" represent the mid-prices at the beginning and end of the interval. As bin durations increase, volatility scales with the square root of time. This becomes apparent from the first subplot in Figure [5](https://arxiv.org/html/2510.06879v1#S3.F5 "Figure 5 ‣ Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), where the two curves represent the 10-second bin volatility and the cumulative volatility of AAPL, respectively.

As for volatility, trading volume exhibits a comparable intraday pattern. The lower panel in Figure [5](https://arxiv.org/html/2510.06879v1#S3.F5 "Figure 5 ‣ Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") highlights the traded volume fraction specifically for futures contracts. Notably, there are peaks in trading activity associated with predictable news events, such as the Weekly Petroleum Status Report and the World Agricultural Supply and Demand Estimation (WASDE) Report. These peaks demonstrate the significant influence of scheduled announcements on liquidity patterns throughout the trading day.

During periods of high liquidity, the same trade volume results in a smaller price impact compared to periods of low liquidity. To adjust for this variance, trade volumes are normalized using the average volume profile corresponding to each time of day. Specifically, let VDV\_{D} denote the total daily traded volume and VtiV\_{t\_{i}} the volume in a given bin [ti,ti+1][t\_{i},t\_{i+1}]. Then, we normalize the volume (Qtiℓ)(n)(Q\_{t\_{i}}^{\ell})^{(n)} in an asset ℓ∈{1,…,d}\ell\in\{1,\ldots,d\} at timestep ti∈𝕋t\_{i}\in\mathbb{T} in episode n∈{1,…,N}n\in\{1,\ldots,N\} as follows:

|  |  |  |
| --- | --- | --- |
|  | (Q~tiℓ)(n):=(Qtiℓ)(n)(VDℓ)(n)​1w​∑r=n−w+1n(VDℓ)(r)(Vtiℓ)(r),(\tilde{Q}\_{t\_{i}}^{\ell})^{(n)}:=\frac{(Q\_{t\_{i}}^{\ell})^{(n)}}{(V\_{D}^{\ell})^{(n)}}\frac{1}{w}\sum\_{r=n-w+1}^{n}\frac{(V^{\ell}\_{D})^{(r)}}{(V^{\ell}\_{t\_{i}})^{(r)}}, |  |

where samples are chronologically ordered in time and the rolling window mean is defined as w:=min​(n,20)w:=\text{min}(n,20) days. To account for different concavities, we recall the class of impact functions hch\_{c} from ([2.4](https://arxiv.org/html/2510.06879v1#S2.E4 "In Remark 2.2. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")), and introduce the notations hcSh\_{c\_{S}} and hcXh\_{c\_{X}} to differentiate between self- and cross-impact, respectively.
Taking into account the aforementioned normalization and specification of the impact function, the propagator model ([2.3](https://arxiv.org/html/2510.06879v1#S2.E3 "In Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pti+1ℓ−Pt0ℓσ[t0,ti+1]ℓ=∑j=0iGi−j(ℓ,ℓ)​hcS​(Q~tjℓ)+∑k≠ℓd∑j=0iGi−j(ℓ,k)​hcX​(Q~tjk),i=0,…,M−1,ℓ=1,…​d,\frac{P^{\ell}\_{t\_{i+1}}-P^{\ell}\_{t\_{0}}}{\sigma^{\ell}\_{[t\_{0},t\_{i+1}]}}=\sum\_{j=0}^{i}G^{({\ell},{\ell})}\_{i-j}h\_{c\_{S}}\Big(\tilde{Q}^{\ell}\_{t\_{j}}\Big)+\sum\_{k\neq\ell}^{d}\sum\_{j=0}^{i}G^{(\ell,k)}\_{i-j}h\_{c\_{X}}\Big(\tilde{Q}^{k}\_{t\_{j}}\Big),\quad i=0,\ldots,M-1,\ \ell=1,\ldots d, |  | (3.1) |

where we omit the superscript (n)(n) for simplicity. Unlike in previous studies such as [[39](https://arxiv.org/html/2510.06879v1#bib.bib39), [43](https://arxiv.org/html/2510.06879v1#bib.bib43)], the kernel 𝑮\boldsymbol{G} in our setup does not absorb the volatility term. This normalization ensures robustness with respect to noisy estimates for small bin sizes, and allows the impact kernel to be estimated from inputs that are free from seasonal intraday patterns in volatility and liquidity.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 5: Upper panel: the volatility and cumulative volatility patterns of AAPL stock throughout NASDAQ trading hours, emphasizing varying impacts over different trading periods. Vertical lines mark the NASDAQ opening and closing times. Lower panel: the intraday traded volume profile for energy (orange) and agriculture (blue) futures contracts. Key events such as the Weekly Petroleum Status Report and the WASDE Report influence trading patterns and are indicated with vertical lines. Vertical lines also indicate trading times allowing for liquidity comparisons at different times of the day. Both volume and volatility normalizations are essential for capturing intraday variations in liquidity and return, with each contract analyzed over a rolling 20-day window.

#### Predictive Power

To assess the predictive power of the estimated impact kernels, we employ different strategies tailored to each dataset type.

For the metaorder datasets (both real and synthetic), we estimate the kernel on the full sample rather than splitting it into separate training and test sets, given the limited data available. This choice ensures that calibration incorporates all observed metaorders, providing the most reliable estimates in this context. Model performance is then evaluated through the coefficient of determination R2R^{2}, which allows for direct comparison across specifications.

In contrast, for the order flow datasets, we evaluate the explanatory strength of the impact kernels by examining both in-sample and out-of-sample predictive performance. We adopt a rolling time-based evaluation scheme similar to that in [[33](https://arxiv.org/html/2510.06879v1#bib.bib33)]. Here, models are trained on one month of data and validated on the subsequent month, repeated over a one-year span. The model performance is then measured across the two prediction horizons h=1h=1 minute and h=5h=5 minutes, that is, assuming the traded volumes are known, prices are predicted 1 minute or 5 minutes in advance using the estimated models. The resulting in-sample R2R^{2} values are averaged over 12 months, and the out-of-sample R2R^{2} values are averaged over 11 months.

#### Price Impact Models

We compare the performance of the nonparametric estimator with classical parametric propagator models, where all models share the general form ([3.1](https://arxiv.org/html/2510.06879v1#S3.E1 "In Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")). Given an asset pair (ℓ,k)∈{1,d}2(\ell,k)\in\{1,d\}^{2} and 0≤j≤i≤M−10\leq j\leq i\leq M-1, we consider the parametric kernels

* •

  Single-Exponential (1-EXP): Gi−j(ℓ,k)=Y​e−ρ​(ti−tj)G\_{i-j}^{(\ell,k)}=Ye^{-\rho(t\_{i}-t\_{j})};
* •

  Double-Exponential (2-EXP): Gi−j(ℓ,k)=Y​(w1​e−ρ1​(ti−tj)+(1−w1)​e−ρ2​(ti−tj))G\_{i-j}^{(\ell,k)}=Y\Big(w\_{1}e^{-\rho\_{1}(t\_{i}-t\_{j})}+(1-w\_{1})e^{-\rho\_{2}(t\_{i}-t\_{j})}\Big);
* •

  Power-Law (POWER): Gi−j(ℓ,k)=Y​(ti−tj+τ)−βG\_{i-j}^{(\ell,k)}=Y(t\_{i}-t\_{j}+\tau)^{-\beta};

where YY is a constant of order one as in ([1.1](https://arxiv.org/html/2510.06879v1#S1.E1 "In 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")), and the two nonparametric kernels

* •

  Raw Nonparametric (RAW): Gi−j(ℓ,k)=(G~N,λ)i−j(ℓ,k)G\_{i-j}^{(\ell,k)}=(\tilde{G}\_{N,\lambda})\_{i-j}^{(\ell,k)}, as defined in ([2.16](https://arxiv.org/html/2510.06879v1#S2.E16 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"));
* •

  Projected Nonparametric (PROJ): Gi−j(ℓ,k)=(GN,λ)i−j(ℓ,k)G\_{i-j}^{(\ell,k)}=(G\_{N,\lambda})\_{i-j}^{(\ell,k)}, as defined in ([2.14](https://arxiv.org/html/2510.06879v1#S2.E14 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")).

In line with [[25](https://arxiv.org/html/2510.06879v1#bib.bib25), [33](https://arxiv.org/html/2510.06879v1#bib.bib33), [34](https://arxiv.org/html/2510.06879v1#bib.bib34)], each of the three parametric models is fitted by fixing ρ\rho, (ρ1,ρ2)(\rho\_{1},\rho\_{2}), or (τ,β)(\tau,\beta) first, and precomputing the corresponding normalized impact changes (Iti+1−Iti)/Y(I\_{t\_{i+1}}-I\_{t\_{i}})/Y.
Then, assuming that alpha signals average out, observed price changes can be decomposed into price impact and unaffected prices, so that YY can be estimated by regressing price changes against the normalized impact changes. Finally, parameter tuning is performed via a grid search to find the optimal values ρ∗\rho^{\*}, (ρ1∗,ρ2∗)(\rho^{\*}\_{1},\rho^{\*}\_{2}), or (τ∗,β∗)(\tau^{\*},\beta^{\*}). Specifically, for the grid search of the exponential models, we define the interval of half-lives log⁡(2)/ρ∈[30,720 000]\log($2$)/\rho\in[30,$720\,000$] seconds and denote by NρN\_{\rho}, Nρ1N\_{\rho\_{1}}, Nρ2N\_{\rho\_{2}} the numbers of corresponding grid points within this interval. For the power-law models, the grid search includes decay parameters β∈[0,1]\beta\in[0,1] and shifts τ∈[10,7200]\tau\in[10,$7200$] seconds, with NβN\_{\beta}, NτN\_{\tau} specifying the numbers of associated grid points. Table [3](https://arxiv.org/html/2510.06879v1#S3.T3 "Table 3 ‣ Price Impact Models ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") summarizes the degrees of freedom and tuning requirements for each model. The complexity of parametric models increases significantly as the number of grid points grows, leading to a rapid escalation in computational demands for parameter optimization.

| Model | Free parameters | Tuned parameters | Grid points |
| --- | --- | --- | --- |
| 1-EXP | Y,ρY,\rho | ρ\rho | NρN\_{\rho} |
| 2-EXP | Y,w1,ρ1,ρ2Y,w\_{1},\rho\_{1},\rho\_{2} | ρ1,ρ2\rho\_{1},\rho\_{2} | Nρ1​Nρ2N\_{\rho\_{1}}N\_{\rho\_{2}} |
| POWER | Y,β,τY,\beta,\tau | β,τ\beta,\tau | Nβ​NτN\_{\beta}N\_{\tau} |
| RAW | (G~i)i=0M−1(\tilde{G}\_{i})\_{i=0}^{M-1} | None | 1 |
| PROJ | (Gi)i=0M−1(G\_{i})\_{i=0}^{M-1} | None | 1 |

Table 3: The free parameters per propagator, tuned parameters per propagator, and the number of grid points per propagator for the different models. Here, NρN\_{\rho}, Nρ1N\_{\rho\_{1}}, Nρ2N\_{\rho\_{2}}, NβN\_{\beta}, and NτN\_{\tau} refer to the number of grid points for ρ\rho, ρ1\rho\_{1}, ρ2\rho\_{2}, β\beta, and τ\tau, respectively.

### 3.4 Understanding Metaorder Impact

This section examines the impact of metaorders across different model specifications, as detailed in Tables [4](https://arxiv.org/html/2510.06879v1#S3.T4 "Table 4 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), [5](https://arxiv.org/html/2510.06879v1#S3.T5 "Table 5 ‣ 3.4.2 Cross-Impact Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"). Our key findings are the following:

1. 1.

   Self-impact is shown to be concave and to decay across multiple timescales (a relative R2R^{2} improvement of
   94.4%94.4\% from a linear to a concave model and 1.06%1.06\% for the nonparametric estimator as compared to exponential decay). The nonparametric estimators supports power-law or multi-exponential decay without assuming any specific kernel shape, as stated in Table [4](https://arxiv.org/html/2510.06879v1#S3.T4 "Table 4 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") and illustrated in Figure [1](https://arxiv.org/html/2510.06879v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact").
2. 2.

   The metaorder proxy enhances decay calibration when data is sparse, as can be seen in Table [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") (a relative R2R^{2} improvement of 14.29%14.29\%). Data enhancement offers an improved predictive accuracy by providing smoother and more reliable decay profiles.
3. 3.

   Table [5](https://arxiv.org/html/2510.06879v1#S3.T5 "Table 5 ‣ 3.4.2 Cross-Impact Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") highlights that cross-impact is concave (a relative R2R^{2} improvement of 1.74%1.74\% from linear to concave cross-impact). The predictive power also increases with the number of assets that are considered, as shown in Table [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") (a relative R2R^{2} improvement of 31.25%31.25\% for one cross-asset and 35.45%35.45\% for two cross-assets). Cross-impact can reflect combined effects of self-impact responses and order flow imbalances. Figure [6](https://arxiv.org/html/2510.06879v1#S3.F6 "Figure 6 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") illustrates the models performance ratio when varying the cross-impact concavity parameter.

In the following two subsections, we provide additional details about our results on self- and cross-impact estimations.

#### 3.4.1 Self-Impact Nonparametric Estimation

We begin by evaluating self-impact using the original CFM metaorder dataset, which contains trades on energy and agricultural futures contracts without synthetic metaorders. A key element of this analysis is the concavity of the self-impact function hcSh\_{c\_{S}} from ([3.1](https://arxiv.org/html/2510.06879v1#S3.E1 "In Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")), parameterized by cSc\_{S}. For each value of cSc\_{S}, we compute the coefficient of determination R2​(cS)R^{2}(c\_{S}) to assess predictive accuracy. The point estimate c^S\hat{c}\_{S} denotes the value of cSc\_{S} that maximizes R2​(cS)R^{2}(c\_{S}). Figure [6](https://arxiv.org/html/2510.06879v1#S3.F6 "Figure 6 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") shows the relative performance ratio R2​(cS)/R2​(c^S)R^{2}(c\_{S})/R^{2}(\hat{c}\_{S}) for the single-asset model (blue). The curve peaks around the square-root case (cS≈0.5c\_{S}\approx 0.5). The value significantly decreases for higher or lower values in line with the results of [[23](https://arxiv.org/html/2510.06879v1#bib.bib23)].

| Propagator | Concavity cSc\_{S} | R2R^{2} |
| --- | --- | --- |
| 1-EXP | 1 | 0.53% |
| 2-EXP | 1 | 0.54% |
| POWER | 1 | 0.53% |
| RAW | 1 | 0.54% |
| PROJ | 1 | 0.54% |
| 1-EXP | 0.5 | 1.036% |
| 2-EXP | 0.5 | 1.049% |
| POWER | 0.5 | 1.044% |
| RAW | 0.5 | 1.05% |
| PROJ | 0.5 | 1.049% |

Table 4: Performance of linear and square-root propagator models on the original CFM metaorder dataset. Linear models perform approximately half as well. Models with multiple transient impact decay timescales perform best.

We then compare various decay kernel specifications under linear and square-root impact. Table [4](https://arxiv.org/html/2510.06879v1#S3.T4 "Table 4 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") summarizes the R2R^{2} values in % of explained variance for all considered models. Among these, the nonparametric kernel (without projection) achieves the highest performance of approximately 1.05% as expected. Notably, the projected nonparametric kernel performs equally well as the parametric multi-timescale models, despite requiring no tuning.

Overall, the relatively modest R2R^{2} values align with expectations given CFM’s limited trading volume relative to the broader market. The measured values highlight the subtler influence of CFM’s trading activities, falling within the anticipated range of 0.1−10.1-1% that corresponds to the average volume fraction traded in the time interval.

![Refer to caption](x7.png)


Figure 6: R2R^{2} performance as a function of the concavities c∙c\_{\bullet} for self- and cross-impact. The blue curve represents R2R^{2} for self-impact models with varying concavity parameters cSc\_{S}. The orange curve shows R2R^{2} for cross-impact models, fixing cS=0.5c\_{S}=0.5 while varying cXc\_{X}. Both curves peak around 0.5−0.60.5-0.6.

#### 3.4.2 Cross-Impact Estimation

We now extend the analysis to cross-impact using metaorders on multiple contracts with different expiries. The goal is to understand how the execution of one asset affects the price of another and whether such effects can improve prediction performance beyond self-impact alone.

To evaluate the predictive value of cross-impact, we compare two classes of models. First, we consider the self-impact-only models RAW and PROJ, which estimate the kernels based on the traded volume of each asset individually. We recall the notions of raw and projected estimators arise from ([2.16](https://arxiv.org/html/2510.06879v1#S2.E16 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) and ([2.17](https://arxiv.org/html/2510.06879v1#S2.E17 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) respectively. Specifically, we calibrate the self-impact kernel components in the first term of ([3.1](https://arxiv.org/html/2510.06879v1#S3.E1 "In Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")) for each asset ℓ∈{1,…,d}\ell\in\{1,\ldots,d\}, and set the cross-impact kernel components in the second term of ([3.1](https://arxiv.org/html/2510.06879v1#S3.E1 "In Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")) to zero. Second, we consider the cross-impact models CROSS-RAW and CROSS-PROJ, incorporating both self-impact and cross-impact by accounting for influences from contracts with the next expiry. In these models, we calibrate all kernel components in ([3.1](https://arxiv.org/html/2510.06879v1#S3.E1 "In Normalization ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")) across all asset pairs (ℓ,k)∈{1,…​d}2(\ell,k)\in\{1,\ldots d\}^{2}.

| Propagator | Concavity cXc\_{X} | R2R^{2} |
| --- | --- | --- |
| RAW | – | 1.05% |
| PROJ | – | 1.049% |
| CROSS-RAW | 1 | 1.15% |
| CROSS-PROJ | 1 | 1.13% |
| CROSS-RAW | 0.5 | 1.17% |
| CROSS-PROJ | 0.5 | 1.15% |

Table 5: Performance of self and cross-impact models on metaorder data using projected (PROJ) and raw (RAW) kernels. The concave cross-impact model fits best.

Table [5](https://arxiv.org/html/2510.06879v1#S3.T5 "Table 5 ‣ 3.4.2 Cross-Impact Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") summarizes the R2R^{2} values for these models, using both a square-root and linear function hcXh\_{c\_{X}} for the cross-impact term while keeping cS=0.5c\_{S}=0.5. The projected square-root cross-impact kernel improves R2R^{2} from 1.05% (self-impact only, where cXc\_{X} is not needed) to 1.17%. Interestingly, when the cross-impact kernel is assumed to be linear, performance decreases to 1.15%, showing that cross-impact is concave as suggested in [[24](https://arxiv.org/html/2510.06879v1#bib.bib24)]. The concavity of cross-impact is further investigated in Figure [6](https://arxiv.org/html/2510.06879v1#S3.F6 "Figure 6 ‣ 3.4.1 Self-Impact Nonparametric Estimation ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") where the orange curve plots the models’ performance ratio across various concavity parameters cXc\_{X}. When integrating both self- and cross-impact contributions, peaks are observed around 0.5−0.60.5-0.6.

Nonetheless, accurately measuring cXc\_{X} is challenging due to cross-impact being a second-order effect. While data suggests that both concavities peak in the same range, determining whether cX>cSc\_{X}>c\_{S} remains elusive given the low signal-to-noise ratio. Cross-asset price adjustments might occur not only in response to price changes initiated by self-impact but also due to observed order flow imbalances. This suggests that the cross-impact relationship could exhibit characteristics of both square-root and linear effects, reflecting a convolution of these dynamics.

#### 3.4.3 Impact Estimation with the Enhanced Dataset

Figure [1](https://arxiv.org/html/2510.06879v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact") compares the impact kernel estimated from the trades on corn futures (gray) with that from the proxy-enhanced dataset (blue). The kernel from raw CFM metaorders appears irregular and noisy, whereas the extended sample yields a smooth, monotonic decay consistent with known empirical regularities. Figure [7](https://arxiv.org/html/2510.06879v1#S3.F7 "Figure 7 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") further illustrates this in a log-log scale. After rescaling the kernel by a factor of t\sqrt{t} to correct for volatility normalization in the returns, it follows a near-linear trend with a slope of −0.5-0.5, consistent with the square-root law observed in [[11](https://arxiv.org/html/2510.06879v1#bib.bib11), [13](https://arxiv.org/html/2510.06879v1#bib.bib13)].

While concavity in volume is the dominant contribution to the predictive power of the impact-model, the decay is a second-order effect, consistent with findings in [[25](https://arxiv.org/html/2510.06879v1#bib.bib25)]. The first 33 rows of Table [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") show that R2R^{2} improves when including proxy data.

| Concavity cSc\_{S} | Concavity cXc\_{X} | Assets | Enhanced | R2R^{2} |
| --- | --- | --- | --- | --- |
| 1 | – | 1 | ✗ | 3.2% |
| 0.5 | – | 1 | ✗ | 4.6% |
| 0.5 | – | 1 | ✓ | 4.8% |
| 0.5 | 0.5 | 2 | ✓ | 6.3% |
| 0.5 | 0.5 | 3 | ✓ | 6.5% |

Table 6: Performance of self and cross-impact models using the nonparametric raw estimator (RAW). The table compares models with different numbers of assets, concavity parameters, and indicates whether the dataset is enhanced with synthetic metaorders.

![Refer to caption](x8.png)


Figure 7: Impact kernel estimates G:=G(ℓ,ℓ)G:=G^{(\ell,\ell)} for square-root self-impact with (blue) and without proxy-enhanced date (grey) in log-log scale. The proxy-enhanced kernel, after rescaling, decays smoothly and can be approximated by a power-law propagator with an exponent of -0.5.

Next, we consider nonparametric estimations for multi-asset cross-impact models on the enhanced dataset of corn futures. The two-asset model shows that including a second highly correlated contract increases R2R^{2} from 4.8% to 6.3%, a substantial gain over the self-impact-only specification. The three-asset model increases R2R^{2} further to 6.5% (see the last two entries of Table [6](https://arxiv.org/html/2510.06879v1#S3.T6 "Table 6 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")).

The two left panels in Figure [8](https://arxiv.org/html/2510.06879v1#S3.F8 "Figure 8 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") illustrate the estimated propagators for two corn futures with different expirations, indexed by 0 and 1 (see Section [3.1](https://arxiv.org/html/2510.06879v1#S3.SS1 "3.1 Datasets ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") for details on the index notation). We observe that the kernels are asymmetric: the impact of Corn0 on Corn1 is stronger than the reverse. This asymmetry reflects liquidity differences across assets, with Corn1 being less liquid. Our findings are consistent with previous observations on immediate aggregate order flow impact in [[27](https://arxiv.org/html/2510.06879v1#bib.bib27)]. However, while that study focuses on estimating the peak cross-impact kernel as a static object varying with liquidity differences, we go further by directly calibrating the full propagator of metaorders, which captures the dynamics of liquidity differences over time.

The right-hand side of Figure [8](https://arxiv.org/html/2510.06879v1#S3.F8 "Figure 8 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") extends the estimation to three assets. While the qualitative patterns persist, the estimates become less stable. The width of the confidence intervals derived in Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact") increases substantially for a single asset to a multi-asset model. This confirms that cross-impact estimation is subject to high variance, but the structure of the kernels remains interpretable. In particular, cross-impact can exceed self-impact in magnitude, depending on relative liquidity.

![Refer to caption](x9.png)


Figure 8: Cross-impact kernels are estimated for corn future contracts with different expiries. The solid and dashed lines depict the raw and projected kernels, respectively. Left column: results are shown for a two-asset model, where cross-impact is estimated from Corn0 (blue) to itself (above) or to Corn1 (below) and from Corn1 (orange) to Corn0 (above) or to itself (below). The different cross and self-impact ratios reflect liquidity differences. Right column: for the three-asset model, cross and self-impact kernels are similarly estimated across Corn0, Corn1, and Corn2 (gray). The relative importance of these kernels varies with liquidity, and increasing dimensionality leads to less stable calibrations.

![Refer to caption](x10.png)


Figure 9: Comparison of impact decay kernels across selected stocks using various estimators. The subplots display the estimated kernel shapes for AAPL, ADBE, and ABBV, alongside an aggregated analysis across multiple stocks. Each subplot includes the raw kernel, projected kernel, and parametric fits using one exponential, two exponentials, and a power-law.

### 3.5 Understanding Aggregate Impact

We now turn our attention to the analysis based on order flow imbalance. Our main results using public market data of S&P 500 stocks are as follows:

1. 1.

   Self-impact is concave (a relative out-of-sample R2R^{2} improvement of 75.98%−183.89%75.98\%-183.89\% depending on the model and prediction horizon for cS=0.5c\_{S}=0.5 compared to cS=1c\_{S}=1, see Table [7](https://arxiv.org/html/2510.06879v1#S3.T7 "Table 7 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"). For the projected nonparametric kernel, we find an optimal concavity parameter of about cS≈0.3c\_{S}\approx 0.3 (a relative out-of-sample R2R^{2} improvement of 84.39%−89.05%84.39\%-89.05\% depending on the prediction horizon compared to the linear case), see Table [8](https://arxiv.org/html/2510.06879v1#S3.T8 "Table 8 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact").
2. 2.

   As for metaorders, the nonparametric estimator validates a power-law decay of self-impact for aggregate order flow in an unbiased manner, that is, without imposing a parametric structure on the decay kernel, as illustrated in Figures [2](https://arxiv.org/html/2510.06879v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact") and [9](https://arxiv.org/html/2510.06879v1#S3.F9 "Figure 9 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"). In particular, we find that a shifted power-law kernel yields the best fit for the nonparametrically estimated kernel, as shown in Figure [2](https://arxiv.org/html/2510.06879v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact").
3. 3.

   Both the raw and projected estimated kernels achieve higher in-sample performance compared to the parametric kernels (a relative in-sample R2R^{2} improvement of 0.89%−18.64%0.89\%-18.64\% depending on the model, concavity, and prediction horizon). While the raw kernel exhibits lower out-of-sample performance than the parametric models, the projected estimated kernel performs better out-of-sample (a relative out-of-sample R2R^{2} improvement of 1.86%−24.65%1.86\%-24.65\% depending on the model, concavity, and prediction horizon), as can be seen from Table [7](https://arxiv.org/html/2510.06879v1#S3.T7 "Table 7 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact").
4. 4.

   Cross-impact induced by aggregate order flow exhibits concavity just as in the metaorder case. Nonparametric square-root cross-impact models fit better than their linear counterparts (a relative out-of-sample R2R^{2} improvement of 0.87%−2.2%0.87\%-2.2\% depending on the prediction horizon), as shown in Table [9](https://arxiv.org/html/2510.06879v1#S3.T9 "Table 9 ‣ 3.5.2 Cross-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact").

#### 3.5.1 Self-Impact Estimation

Figure [2](https://arxiv.org/html/2510.06879v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact") shows the nonparametric kernel estimated universally from all 197 stocks in our dataset, confirming the power-law nature of price impact decay for US equities. Figure [9](https://arxiv.org/html/2510.06879v1#S3.F9 "Figure 9 ‣ 3.4.3 Impact Estimation with the Enhanced Dataset ‣ 3.4 Understanding Metaorder Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") then displays the estimated kernels for single stocks, illustrating the nonparametric estimation and suggesting a power-law decay as well.

| Propagator | Concavity cSc\_{S} | Horizon | IS R2R^{2} | OOS R2R^{2} |
| --- | --- | --- | --- | --- |
| 1-EXP | 1 | 1 | 16.36% | 15.45% |
| 2-EXP | 1 | 1 | 17.74% | 15.80% |
| POWER | 1 | 1 | 18.03% | 16.27% |
| RAW | 1 | 1 | 19.41% | 9.05% |
| PROJ | 1 | 1 | 19.02% | 16.90% |
| 1-EXP | 0.5 | 1 | 30.28% | 29.48% |
| 2-EXP | 0.5 | 1 | 30.94% | 29.99% |
| POWER | 0.5 | 1 | 30.90% | 30.12% |
| RAW | 0.5 | 1 | 31.27% | 22.51% |
| PROJ | 0.5 | 1 | 31.18% | 30.68% |
| 1-EXP | 1 | 5 | 11.67% | 10.02% |
| 2-EXP | 1 | 5 | 12.18% | 11.52% |
| POWER | 1 | 5 | 12.42% | 11.69% |
| RAW | 1 | 5 | 12.98% | 5.40% |
| PROJ | 1 | 5 | 12.53% | 12.49% |
| 1-EXP | 0.5 | 5 | 22.32% | 20.63% |
| 2-EXP | 0.5 | 5 | 22.51% | 20.67% |
| POWER | 0.5 | 5 | 22.43% | 20.59% |
| RAW | 0.5 | 5 | 23.75% | 15.33% |
| PROJ | 0.5 | 5 | 23.36% | 21.98% |

Table 7: In- and out-of-sample performance of the linear and square-root parametric models 1-EXP, 2-EXP, POWER and the nonparametric models RAW, PROJ for prediction horizons h=h= 1min, 5min. The projected nonparametrically estimated kernel PROJ achieves the best prediction power.

Table [7](https://arxiv.org/html/2510.06879v1#S3.T7 "Table 7 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") summarizes the in- and out-of-sample performance of the linear and square-root propagator model for different decay kernels and prediction horizons. As explained in Section [3.3](https://arxiv.org/html/2510.06879v1#S3.SS3 "3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), this includes a grid search over the tuned parameters listed in Table [3](https://arxiv.org/html/2510.06879v1#S3.T3 "Table 3 ‣ Price Impact Models ‣ 3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") for each parametric propagator. Notably, the projected nonparametrically estimated kernel achieves the best out-of-sample prediction power among the models considered. This is because the raw kernel estimates tend to be quite spiky, so the projection step effectively smoothens out high-frequency noise and substantially reduces overfitting. By contrast, in the metaorder setting with 5-minute bins the kernel is already estimated over much coarser intervals, so applying the same projection yields only marginal gains in forecast power.

Table [7](https://arxiv.org/html/2510.06879v1#S3.T7 "Table 7 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") indicates that the impact concavity parameter exerts a stronger influence on the prediction performance than the impact decay. Motivated by this finding, Table [8](https://arxiv.org/html/2510.06879v1#S3.T8 "Table 8 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") compares the out-of-sample performance of the projected estimated kernel for various concavity values.

Consistent with the results of [[34](https://arxiv.org/html/2510.06879v1#bib.bib34)], our analysis suggests that a concavity parameter of approximately 0.3 yields optimal prediction performance. This outcome is likely due to the fact that we aggregated the data into bins and treated the aggregate signed volume in each bin as a single order, thereby producing relatively large order sizes. These findings align with those of [[28](https://arxiv.org/html/2510.06879v1#bib.bib28)], who observed a concavity parameter of around 0.5 for small volumes and 0.2 for large volumes in US stocks.

| Concavity cSc\_{S} | Horizon | IS R2R^{2} | OOS R2R^{2} |
| --- | --- | --- | --- |
| 0.5 | 1 | 31.18% | 30.68% |
| 0.4 | 1 | 32.05% | 31.38% |
| 0.3 | 1 | 33.42% | 31.95% |
| 0.2 | 1 | 32.46% | 30.81% |
| 0.1 | 1 | 29.01% | 27.30% |
| 0.5 | 5 | 23.36% | 21.98% |
| 0.4 | 5 | 24.11% | 22.74% |
| 0.3 | 5 | 24.65% | 23.03% |
| 0.2 | 5 | 24.17% | 22.79% |
| 0.1 | 5 | 22.50% | 20.08% |

Table 8: In- and out-of-sample performance of the nonparametric propagator model PROJ for different concavities cS=c\_{S}= 0.1, 0.2, 0.3, 0.4, 0.5 and prediction horizons h=h= 1min, 5min. A concavity parameter of 0.3 yields the highest prediction performance.

#### 3.5.2 Cross-Impact Estimation

| Model | Concavity cSc\_{S} | Concavity cXc\_{X} | Horizon | IS R2R^{2} | OOS R2R^{2} |
| --- | --- | --- | --- | --- | --- |
| PROJ | 1 | - | 1 | 19.02% | 16.90% |
| CROSS-PROJ | 1 | 1 | 1 | 21.33% | 18.92% |
| PROJ | 0.5 | - | 1 | 31.18% | 30.68% |
| CROSS-PROJ | 0.5 | 1 | 1 | 31.32% | 30.90% |
| CROSS-PROJ | 0.5 | 0.5 | 1 | 32.39% | 31.17% |
| PROJ | 1 | - | 5 | 12.53% | 12.49% |
| CROSS-PROJ | 1 | 1 | 5 | 14.58% | 14.55% |
| PROJ | 0.5 | - | 5 | 23.36% | 21.98% |
| CROSS-PROJ | 0.5 | 1 | 5 | 23.71% | 22.25% |
| CROSS-PROJ | 0.5 | 0.5 | 5 | 24.25% | 22.74% |

Table 9: In- and out-of-sample performance of the linear and square-root propagator models PROJ (without cross-impact) and CROSS-PROJ (with cross-impact) for horizons h=h= 1min, 5min. The introduction of cross-impact increases predictive power, with the increase being larger for concave cross-impact.

In line with the analysis in Section [3](https://arxiv.org/html/2510.06879v1#S3 "3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), we extend our framework to capture cross‐impact effects by applying the nonparametric estimation procedure described in Section [2](https://arxiv.org/html/2510.06879v1#S2 "2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"). Figure [10](https://arxiv.org/html/2510.06879v1#S3.F10 "Figure 10 ‣ 3.5.2 Cross-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") displays the estimated cross‐impact kernels for a pair (left panels) and a triplet (right panels) of highly correlated equities. In each case, the kernels exhibit a pronounced convex decay, and one can observe a cross-impact effect in both directions. One notable strength of the nonparametric estimator in the multi-asset case is that the number of tuned parameters remains zero for for dd assets, whereas it is of order 𝒪​(d2)\mathcal{O}(d^{2}) for parametric kernels (see Table [1](https://arxiv.org/html/2510.06879v1#S1.T1 "Table 1 ‣ Our main contributions. ‣ 1 Introduction ‣ Nonparametric Estimation of Self- and Cross-Impact")).

We also assess whether the introduction of cross-impact enhances predictive power for nonparametrically estimated impact models. For this, we follow the procedure of [[33](https://arxiv.org/html/2510.06879v1#bib.bib33)] and compare the performance of the following two models:

* •

  Single-asset projected propagator model (PROJ) as in Section [3.3](https://arxiv.org/html/2510.06879v1#S3.SS3 "3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"),
  where the impact in each asset ℓ∈{1,…​d}\ell\in\{1,\ldots d\} only depends on the traded volume in that asset.
* •

  Multi-asset projected propagator model (CROSS-PROJ), where the impact in each asset ℓ∈{1,…​d}\ell\in\{1,\ldots d\} depends not only on the traded volume in that asset, but also on the traded volume in the overall market. Here, prices, traded volumes, and volatility of the market portfolio are computed as in [[33](https://arxiv.org/html/2510.06879v1#bib.bib33)], treating it just like an asset. Consequently, the cross-impact propagator matrix is obtained via a nonparametric estimation followed by a projection as before, with the two underlying assets given by the asset ℓ\ell and the market portfolio.

Table [9](https://arxiv.org/html/2510.06879v1#S3.T9 "Table 9 ‣ 3.5.2 Cross-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") summarizes results for these models. We observe that including cross-impact terms improves the fit for linear models and slightly for square-root models. Additionally, correct concavity choice impacts predictive power significantly, with square-root cross-impact yielding better prediction performance than linear cross-impact. Interestingly, when replacing the market portfolio from Section [3.3](https://arxiv.org/html/2510.06879v1#S3.SS3 "3.3 Methodology ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") with another stock that has a high 10-second return correlation with the underlying stock (≥60%\geq 60\%), we only observe modest performance gains in terms of out-of-sample R2R^{2} on average, indicating that the traded volume in the whole market carries more predictive power than the traded volume in one correlated stock.

Figure [10](https://arxiv.org/html/2510.06879v1#S3.F10 "Figure 10 ‣ 3.5.2 Cross-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact") shows the estimated cross-impact kernels for a pair and a triplet of stocks. The left column presents a two-asset model with Coca-Cola (KO) and PepsiCo (PEP), which exhibit a 10-second return correlation of 54%. Due to similar market capitalizations and liquidity, the cross-impact effects are nearly symmetric in both directions. The self-impact kernels for KO and PEP exhibit a decay pattern consistent with a power-law, reflecting the similar characteristics of these stocks.

The right column illustrates a three-asset model for ConocoPhillips (COP), Chevron (CVX), and Exxon Mobil (XOM), which have pairwise 10-second return correlations of 61%, 62%, and 67%, respectively. Cross-impact and self-impact kernels are calculated highlighting the liquidity distribution. The strongest cross-impact is observed from the more liquid XOM to the less liquid CVX and COP, while impacts in the reverse direction are considerably weaker. This demonstrates the liquidity gradient from XOM to CVX and COP.

![Refer to caption](x11.png)


Figure 10: Cross-impact kernels are estimated for correlated stocks. The solid and dashed lines depict the raw and projected kernels, respectively. Left column: Results are shown for a two-asset model, where cross-impact is estimated from Coca-Cola (KO) (blue) to itself (above) or to PepsiCo (PEP) (below) and from PEP (orange) to KO (above) or on itself (below). The cross-impact effects are nearly symmetric in both directions and impact decays. Right column: For the three-asset model, cross- and self-impact kernels are similarly estimated across the largest three US oil companies ConocoPhillips (COP), Chevron (CVX), and Exxon Mobil (XOM) (gray). As market capitalization and liquidity decrease from XOM to CVX to COP, the strongest cross-impact is observed flowing from the more liquid XOM into the less liquid CVX and COP, while, conversely, impacts in the opposite direction are markedly weaker.

## Appendix A Robustness Check

In Section [3.5](https://arxiv.org/html/2510.06879v1#S3.SS5 "3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact"), we aggregated the events using a bin size of 10 seconds. Using the same collection of stocks, we now increase the bin size to 5 minutes to make the aggregate impact analysis comparable to the metaorder impact analysis, 72 data points per trading day after removing the last half-hour. Table [10](https://arxiv.org/html/2510.06879v1#A1.T10 "Table 10 ‣ Appendix A Robustness Check ‣ Nonparametric Estimation of Self- and Cross-Impact") presents a summary of the in- and out-of-sample performance for different decay kernels using a bin size of 5 minutes.

Compared to the analysis with 10-second bins (see Table [7](https://arxiv.org/html/2510.06879v1#S3.T7 "Table 7 ‣ 3.5.1 Self-Impact Estimation ‣ 3.5 Understanding Aggregate Impact ‣ 3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")), predictive power declines when using larger bins, likely due to reduced accuracy from data aggregation. However, in comparison to the metaorder impact case (see Section [3](https://arxiv.org/html/2510.06879v1#S3 "3 Empirical Analysis ‣ Nonparametric Estimation of Self- and Cross-Impact")), predictive power improves. This enhancement is due to the fact that, for aggregated impact, the signed volume of the entire market serves as a stronger explanatory variable than the signed volume of a metaorder, which represents only a minor perturbation of the market’s total order flow.

| Propagator | Concavity cSc\_{S} | Horizon | IS R2R^{2} | OOS R2R^{2} |
| --- | --- | --- | --- | --- |
| 1-EXP | 1 | 5 | 14.60% | 9.96% |
| 2-EXP | 1 | 5 | 14.95% | 9.86% |
| POWER | 1 | 5 | 14.70% | 10.01% |
| RAW | 1 | 5 | 12.17% | 7.58% |
| PROJ | 1 | 5 | 14.56% | 9.93% |
| 1-EXP | 0.5 | 5 | 18.16% | 17.25% |
| 2-EXP | 0.5 | 5 | 18.51% | 17.30% |
| POWER | 0.5 | 5 | 18.21% | 17.35% |
| RAW | 0.5 | 5 | 16.56% | 14.94% |
| PROJ | 0.5 | 5 | 18.05% | 17.18% |

Table 10: In- and out-of-sample performance of the linear and square-root parametric models 1-EXP, 2-EXP, POWER and the nonparametric models RAW, PROJ for a bin size of 5 minutes.

## Appendix B Proofs

We now provide the proof of Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), which generalizes the proof of Theorem 2.14 in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] to the concave multi-asset framework.

###### Proof of Theorem [2.10](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact").

The proof is similar to the proof of Theorem 2.14 in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)]. Namely, let (ℱn)n≥0(\mathcal{F}\_{n})\_{n\geq 0} be the filtration from Definition [2.1](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"). Then 𝑼(n)\boldsymbol{U}^{(n)} from ([2.12](https://arxiv.org/html/2510.06879v1#S2.E12 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) is ℱn−1\mathcal{F}\_{n-1}-measurable and 𝒚(n)\boldsymbol{y}^{(n)} from ([2.11](https://arxiv.org/html/2510.06879v1#S2.E11 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) is ℱn\mathcal{F}\_{n}-measurable. Define X:=ℝM​d2X:={\mathbb{R}}^{Md^{2}}, Y:=ℝM​dY:={\mathbb{R}}^{Md}, and

|  |  |  |
| --- | --- | --- |
|  | An:X→Y,An​(v):=𝑼(n)​v,n=1,…,N.A\_{n}:X\to Y,\quad A\_{n}(v):=\boldsymbol{U}^{(n)}v,\quad n=1,\ldots,N. |  |

Then, recalling ([2.13](https://arxiv.org/html/2510.06879v1#S2.E13 "In 2.3 Nonparametric Estimation ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact")) and Assumption [2.3](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem3 "Assumption 2.3. ‣ 2.1 Offline Dataset ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), we get from Theorem 4.5 in [[37](https://arxiv.org/html/2510.06879v1#bib.bib37)] that for all λ>0\lambda>0,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ‖WN,λ1/2​(𝑮N,λ−𝑮∗)‖ℝM​d2\displaystyle\left\|{W\_{N,\lambda}^{1/2}}\big(\boldsymbol{G}\_{N,\lambda}-\boldsymbol{G}^{\*}\big)\right\|\_{{\mathbb{R}}^{Md^{2}}} |  | (B.1) |
|  |  | ≤R​(2​log⁡(det(λ−1​WN,λ)δ2))1/2+λ​‖WN,λ−1/2​𝑮∗‖ℝM​d2\displaystyle\leq R\left(2\log\left(\frac{\det(\lambda^{-1}W\_{N,\lambda})}{\delta^{2}}\right)\right)^{1/2}+\lambda\left\|{W^{-1/2}\_{N,\lambda}}\boldsymbol{G}^{\*}\right\|\_{{\mathbb{R}}^{Md^{2}}} |  |
|  |  | =R​(2​log⁡(det(WN,λ)δ2​λM​d2))1/2+λ​‖WN,λ−1/2​𝑮∗‖ℝM​d2.\displaystyle=R\left(2\log\left(\frac{\det(W\_{N,\lambda})}{\delta^{2}\lambda^{Md^{2}}}\right)\right)^{1/2}+\lambda\left\|{W^{-1/2}\_{N,\lambda}}\boldsymbol{G}^{\*}\right\|\_{{\mathbb{R}}^{Md^{2}}}. |  |

This proves the desired bound.
∎

Next, we give the proof of Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact"), which extends Proposition 1 of [[22](https://arxiv.org/html/2510.06879v1#bib.bib22)] to the discrete-time framework.

###### Proof of Theorem [2.4](https://arxiv.org/html/2510.06879v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Price Manipulation and Admissible Kernels ‣ 2 Nonparametric Impact Estimation from Offline Data ‣ Nonparametric Estimation of Self- and Cross-Impact").

Since hh is continuous, odd, and not linear, there exist a,b∈ℝa,b\in\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | s:=h​(a)+h​(b)+h​(−a−b)≠0.s:=h(a)+h(b)+h(-a-b)\neq 0. |  | (B.2) |

Otherwise, if h​(a)+h​(b)+h​(−a−b)=0h(a)+h(b)+h(-a-b)=0 for all a,b∈ℝa,b\in{\mathbb{R}}, then due to the oddness the identity becomes h​(a+b)=h​(a)+h​(b)h(a+b)=h(a)+h(b) for all a,b∈ℝa,b\in{\mathbb{R}}, which gives a contradiction as the continuity of hh then yields h​(x)=q​xh(x)=qx for some q∈ℝq\in{\mathbb{R}}. Moreover, using the oddness again, we can assume s<0s<0 without loss of generality.
Fix such a,ba,b and set x0:=ax\_{0}:=a, x1:=bx\_{1}:=b, x2=:−a−bx\_{2}=:-a-b, and x3=…=xM−1=0x\_{3}=\ldots=x\_{M-1}=0. Take t0=…=tM−1=t∗t\_{0}=\ldots=t\_{M-1}=t^{\*}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=∑i,j=0M−1xi​H​(ti,tj)​h​(xj)=H​(t∗,t∗)​(∑i=0M=1xi)​(∑j=0M−1h​(xj))=H​(t∗,t∗)⋅0⋅s=0,S=\sum\_{i,j=0}^{M-1}x\_{i}H(t\_{i},t\_{j})h(x\_{j})=H(t^{\*},t^{\*})\Big(\sum\_{i=0}^{M=1}x\_{i}\Big)\Big(\sum\_{j=0}^{M-1}h(x\_{j})\Big)=H(t^{\*},t^{\*})\cdot 0\cdot s=0, |  | (B.3) |

with H​(t∗,t∗)>0H(t^{\*},t^{\*})>0 and s<0s<0 defined in ([B.2](https://arxiv.org/html/2510.06879v1#A2.E2 "In Appendix B Proofs ‣ Nonparametric Estimation of Self- and Cross-Impact")). Next, replace x0x\_{0} by x0+εx\_{0}+\varepsilon for some ε>0\varepsilon>0, so that ∑i=0M−1xi=ε\sum\_{i=0}^{M-1}x\_{i}=\varepsilon. By the fact that s<0s<0 and the continuity of hh at x0x\_{0}, for sufficiently small ε\varepsilon we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=0M−1h​(xj)=s+(h​(x0+ε)−h​(x0))<0.\sum\_{j=0}^{M-1}h(x\_{j})=s+\big(h(x\_{0}+\varepsilon)-h(x\_{0})\big)<0. |  | (B.4) |

Hence, ([B.3](https://arxiv.org/html/2510.06879v1#A2.E3 "In Appendix B Proofs ‣ Nonparametric Estimation of Self- and Cross-Impact")) and ([B.4](https://arxiv.org/html/2510.06879v1#A2.E4 "In Appendix B Proofs ‣ Nonparametric Estimation of Self- and Cross-Impact")) yield S<0S<0. Finally, by the continuity of HH in (t∗,t∗)(t^{\*},t^{\*}), choosing the distinct points ti:=t∗+i​δt\_{i}:=t^{\*}+i\delta for sufficiently small δ>0\delta>0 preserves negativity of SS. The second part of the theorem then follows from choosing H​(t,s)=G​(|t−s|)H(t,s)=G(|t-s|) for all t,s∈[0,T]t,s\in[0,T].
∎

## References

* Abi Jaber et al. [2024]

  E. Abi Jaber, E. Neuman, and S. Tuschmann.
  Optimal portfolio choice with cross-impact propagators.
  *Preprint*, 2024.
* Alfonsi and Acevedo [2014]

  A. Alfonsi and J. I. Acevedo.
  Optimal execution and price manipulations in time-varying limit order
  books.
  *Applied Mathematical Finance*, 21(3):201–237, 2014.
* Alfonsi and Schied [2010]

  A. Alfonsi and A. Schied.
  Optimal trade execution and absence of price manipulations in limit
  order book models.
  *SIAM Journal on Financial Mathematics*, 1(1):490–522, 2010.
* Alfonsi et al. [2010]

  A. Alfonsi, A. Fruth, and A. Schied.
  Optimal execution strategies in limit order books with general shape
  functions.
  *Quantitative Finance*, 10(2):143–157,
  2010.
* Alfonsi et al. [2016]

  A. Alfonsi, F. Klöck, and A. Schied.
  Multivariate transient price impact and matrix-valued positive
  definite functions.
  *Mathematics of Operations Research*, 41(3):914–934, 2016.
* Almgren and Chriss [1999]

  R. Almgren and N. Chriss.
  Value under liquidation.
  *Risk*, 12:61–63, 1999.
* Almgren and Chriss [2000]

  R. Almgren and N. Chriss.
  Optimal execution of portfolio transactions.
  *Journal of Risk*, 3(2):5–39, 2000.
* Almgren et al. [2005]

  R. Almgren, C. Thum, E. Hauptmann, and H. Li.
  Direct estimation of equity market impact.
  *Risk*, 18(7):58–62, 2005.
* Benzaquen et al. [2017]

  M. Benzaquen, I. Mastromatteo, Z. Eisler, and J.-P. Bouchaud.
  Dissecting cross-impact on stock markets: An empirical analysis.
  *Journal of Statistical Mechanics: Theory and Experiment*,
  2017(2):023406, 2017.
* Bershova and Rakhlin [2013]

  N. Bershova and D. Rakhlin.
  The non-linear market impact of large trades: Evidence from buy-side
  order flow.
  *Quantitative Finance*, 13(11):1759–1778,
  2013.
* Bouchaud et al. [2004]

  J.-P. Bouchaud, Y. Gefen, M. Potters, and M. Wyart.
  Fluctuations and response in financial markets: The subtle nature of
  random price changes.
  *Quantitative Finance*, 4(2):176–190, 2004.
* Bouchaud et al. [2018]

  J.-P. Bouchaud, J. Bonart, J. Donier, and M. Gould.
  *Trades, Quotes and Prices: Financial Markets Under the
  Microscope*.
  Cambridge University Press, 2018.
* Bucci et al. [2015]

  F. Bucci, M. Benzaquen, F. Lillo, and J.-P. Bouchaud.
  Slow decay of impact in equity markets.
  *Market Microstructure and Liquidity*, 4(3):1950006, 2015.
* Cont et al. [2014]

  R. Cont, A. Kukanov, and S. Stoikov.
  The price impact of order book events.
  *Journal of Financial Econometrics*, 12(1):47–88, 2014.
* Curato et al. [2017]

  G. Curato, J. Gatheral, and F. Lillo.
  Optimal execution with non-linear transient market impact.
  *Quantitative Finance*, 17(1):41–54, 2017.
* Diamond and Boyd [2016]

  S. Diamond and S. Boyd.
  CVXPY: A Python-embedded modeling language for convex
  optimization.
  *Journal of Machine Learning Research*, 17(83):1–5, 2016.
* Donier and Bonart [2015]

  J. Donier and J. Bonart.
  A million metaorder analysis of market impact on the bitcoin.
  *Market Microstructure and Liquidity*, 01(02):1550008, 2015.
* Forde et al. [2022]

  M. Forde, L. Sánchez-Betancourt, and B. Smith.
  Optimal trade execution for Gaussian signals with power-law
  resilience.
  *Quantitative Finance*, 22(3):585–596,
  2022.
* Gârleanu and Pedersen [2016]

  N. Gârleanu and L. H. Pedersen.
  Dynamic portfolio choice with frictions.
  *Journal of Economic Theory*, 165:487–516, 2016.
* Gatheral [2010]

  J. Gatheral.
  No-dynamic-arbitrage and market impact.
  *Quantitative Finance*, 10(7):749–759,
  2010.
* Gatheral et al. [2011]

  J. Gatheral, A. Schied, and A. Slynko.
  Exponential resilience and decay of market impact.
  In *Econophysics of Order-driven Markets*, pages 225–236.
  Springer, 2011.
* Gatheral et al. [2012]

  J. Gatheral, A. Schied, and A. Slynko.
  Transient linear price impact and Fredholm integral equations.
  *Mathematical Finance*, 22(3):445–474,
  2012.
* Hey et al. [2024a]

  N. Hey, J.-P. Bouchaud, I. Mastromatteo, J. Muhle-Karbe, and K. Webster.
  The cost of misspecifying price impact.
  *Risk*, January, 2024a.
* Hey et al. [2024b]

  N. Hey, I. Mastromatteo, and J. Muhle-Karbe.
  Concave cross impact.
  *Preprint*, 2024b.
* Hey et al. [2025]

  N. Hey, I. Mastromatteo, J. Muhle-Karbe, and K. Webster.
  Trading with concave price impact and impact decay - theory and
  evidence.
  *Operations Research*, 2025.
* Huberman and Stanzl [2004]

  G. Huberman and W. Stanzl.
  Price manipulation and quasi-arbitrage.
  *Econometrica*, 72(4):1247–1275, 2004.
* Le Coz et al. [2023]

  V. Le Coz, I. Mastromatteo, D. Challet, and M. Benzaquen.
  When is cross impact relevant?
  *Preprint*, 2023.
* Lillo et al. [2003]

  F. Lillo, J. Farmer, and R. Mantegna.
  Master curve for price-impact function.
  *Nature*, 421:129–130, 2003.
* Maitrier et al. [2025a]

  G. Maitrier, G. Loeper, and J.-P. Bouchaud.
  Generating realistic metaorders from public data.
  *Preprint*, 2025a.
* Maitrier et al. [2025b]

  G. Maitrier, G. Loeper, K. Kanazawa, and J.-P. Bouchaud.
  The "double" square-root law: Evidence for the mechanical origin of
  market impact using Tokyo Stock Exchange data.
  *Preprint*, 2025b.
* Mastromatteo et al. [2014]

  I. Mastromatteo, B. Tóth, and J.-P. Bouchaud.
  Agent-based models for latent liquidity and concave price impact.
  *Physical Review E*, 89(4):042805, 2014.
* Mastromatteo et al. [2017]

  I. Mastromatteo, M. Benzaquen, Z. Eisler, and J.-P. Bouchaud.
  Trading lightly: Cross-impact and optimal portfolio execution.
  *Risk*, July, 2017.
* Muhle-Karbe and Tracy [2024]

  J. Muhle-Karbe and C. Tracy.
  Stochastic liquidity as a proxy for concave multi-asset propagator
  models.
  *Preprint*, 2024.
* Muhle-Karbe et al. [2024]

  J. Muhle-Karbe, Z. Wang, and K. Webster.
  Stochastic liquidity as a proxy for nonlinear price impact.
  *Operations Research*, 72(2):444–458, 2024.
* Neuman and Tuschmann [2025]

  E. Neuman and S. Tuschmann.
  The Mercer-Young theorem for matrix-valued kernels on separable
  metric spaces.
  *Positivity*, 29(3):35, 2025.
* Neuman and Zhang [2025]

  E. Neuman and Y. Zhang.
  Statistical learning with sublinear regret of propagator models.
  *To appear in Annals of Applied Probability*, 2025.
* Neuman et al. [2023]

  E. Neuman, W. Stockinger, and Y. Zhang.
  An offline learning approach to propagator models.
  *Preprint*, 2023.
* Obizhaeva and Wang [2013]

  A. A. Obizhaeva and J. Wang.
  Optimal trading strategy and supply/demand dynamics.
  *Journal of Financial Markets*, 16(1):1–32,
  2013.
* Patzelt and Bouchaud [2017]

  F. Patzelt and J.-P. Bouchaud.
  Nonlinear price impact from linear models.
  *Journal of Statistical Mechanics: Theory and Experiment*,
  2017(12):123404, 2017.
* Predoiu et al. [2011]

  S. Predoiu, G. Shaikhet, and S. Shreve.
  Optimal execution in a general one-sided limit-order book.
  *SIAM Journal on Financial Mathematics*, 2(1):183–212, 2011.
* Sato and Kanazawa [2024]

  Y. Sato and K. Kanazawa.
  Does the square-root price impact law belong to the strict universal
  scalings?: quantitative support by a complete survey of the Tokyo stock
  exchange market.
  *Preprint*, 2024.
* Schneider and Lillo [2019]

  M. Schneider and F. Lillo.
  Cross-impact and no-dynamic-arbitrage.
  *Quantitative Finance*, 19(1):137–154,
  2019.
* Taranto et al. [2016]

  D. E. Taranto, G. Bormetti, J.-P. Bouchaud, F. Lillo, and B. Toth.
  Linear models for the impact of order flow on prices I. Propagators:
  Transient vs. History Dependent Impact.
  *Preprint*, 2016.
* Tomas et al. [2022]

  M. Tomas, I. Mastromatteo, and M. Benzaquen.
  How to build a cross-impact model from first principles: Theoretical
  requirements and empirical results.
  *Quantitative Finance*, 22(6):1017–1036,
  2022.
* Tóth et al. [2011]

  B. Tóth, Y. Lemperiere, C. Deremble, J. De Lataillade, J. Kockelkoren, and
  J.-P. Bouchaud.
  Anomalous price impact and the critical nature of liquidity in
  financial markets.
  *Physical Review X*, 1(2):021006, 2011.
* Tóth et al. [2016]

  B. Tóth, Z. Eisler, and J.-P. Bouchaud.
  The square-root impace law also holds for option markets.
  *Wilmott*, 2016(85):70–73, 2016.
* Tóth et al. [2017]

  B. Tóth, Z. Eisler, and J.-P. Bouchaud.
  The short-term price impact of trades is universal.
  *Market Microstructure and Liquidity*, 03(02):1850002, 2017.
* Veldman [2024]

  F. Veldman.
  Market impact modeling and optimal execution strategies for equity
  trading.
  *Master Thesis*, 2024.
* Zarinelli et al. [2015]

  E. Zarinelli, M. Treccani, J. D. Farmer, and F. Lillo.
  Beyond the square root: Evidence for logarithmic dependence of market
  impact on size and participation rate.
  *Market Microstructure and Liquidity*, 01(02):1550004, 2015.