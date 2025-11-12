---
authors:
- Meng-Jou Lu
- Cathy Yi-Hsuan Chen
- Wolfgang Karl Härdle
doc_id: arxiv:2009.12092v2
family_id: arxiv:2009.12092
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2009.12092] Copula-Based Factor Model for Credit Risk Analysis11footnote
  1This is a post-peer-review, pre-copyedit version of an article published in Review
  of Quantitative Finance and Accounting. The final authenticated version is available
  online at: https://doi.org/10.1007/s11156-016-0613-x'
url_abs: http://arxiv.org/abs/2009.12092v2
url_html: https://ar5iv.org/html/2009.12092v2
venue: arXiv q-fin
version: 2
year: 2020
---


Chen, Cathy Yi-Hsuan
Corresponding author. Department of Finance, Chung
Hua University, 707, WuFu Rd., Hsinchu 300, Taiwan. Ladislaus von Bortkiewicz Chair of Statistics,
Humboldt–Universität zu Berlin, C.A.S.E. – Center for
Applied Statistics and Economics, Unter den Linden 6, 10099 Berlin, Germany. E-mail:
cathy1107@gmail.com. 
  


  
Härdle, Karl Wolfgang
 Ladislaus von Bortkiewicz Chair of Statistics,
Humboldt–Universität zu Berlin, C.A.S.E. – Center for
Applied Statistics and Economics, Unter den Linden 6, 10099 Berlin, Germany. Sim Kee Boon Institute for
Financial Economics, Singapore Management University
Administration Building, 81 Victoria Street, 188065 Singapore.
E-mail: haerdle@hu-berlin.de.

(This version: )

###### Abstract

JEL classification: C38, C53, F34, G11, G17
Keywords: Factor Model, Conditional Factor
Loading, State-Dependent
Recovery Rate

JEL classification: C38, C53, F34, G11, G17
Keywords: Factor Model, Conditional Factor
Loading, State-Dependent
Recovery Rate

## 1 Introduction

The global economy has repeatedly observed clusters of default
events, such as the burst of the dotcom bubble in 2001, and the
financial crisis from 2007 to 2009. The clustered default has been
attributed to systematic risk which plays a crucial role in the
default event. To discover this issue, numerous studies emphasise
the role of systematic risk by employing a factor model
( Andersen and Sidenius, [2004](#bib.bib5); 
Pan and Singleton, [2008](#bib.bib36); 
Rosen and Saunders, [2010](#bib.bib40)). The factor model is a prevalent way to
capture the obligors’ shared behaviour through a joint common factor, and to
reduce the dimension of dependence parameters which benefits bond portfolio management. However, one can still find some unrealistic settings on this method such as a constant and linear dependence
structure with thin tails of risk factor distribution embedded.

The factor copula model
imposes a dependence structure on common factors and the variables interested. In credit risk measurement, the factor loading represents the sensitivity of the n𝑛nth obligor to the systematic factor. All the
correlations between obligors arise from their dependence on the
common factor. The common factor plays a major role in determining their joint dependence. By applying factor copula model into credit risk modelling, we are able to decompose a latent variable into the systematic and the
idiosyncratic component which are independent. A latent variable usually represents the proxy of firms’ assets or liquidation value (
Andersen and Sidenius, [2004](#bib.bib5)). Default is triggered by
company asset values falling below a threshold, representing a
fraction of company debt (
Merton, [1974](#bib.bib34)). In this model, credit risk is measured by a Gaussian random default variable generated from firm asset
value that is latent and modelled by a factor copula framework. The implied firm value from the model ideally projects the default time we desire; that is, a lower firm value is, a shorter default time is.

A constant factor loading assumption embedded in a one factor
Gaussian model is inconsistent with the fact that the loading on common factors varies over time, which hampers the measurement of the dependency structures of obligors.
This observation is in fact at the core of research on the
mispricing of structured products (
Choroś-Tomczyk et al., [2013](#bib.bib13); 
Choroś-Tomczyk et al., [2014](#bib.bib14)).
Longin and Solnik ([2001](#bib.bib33)) and
[Ang and Chen](#bib.bib7) (2002b) argue that a
“correlation breakdown” 
structure acts better in the dependence specification. Note that if we
set the factor loading constant, we may underestimate the default
risk as the market turns downward. Our simulation and empirical evidence show that a greater factor loading in market downturn leads to a higher contribution of common factor on firm value.

In addition to the specification of factor loading, a
critical and essential part in calculating the portfolio loss
function is recovery rate. According to Table 1, a
state-dependent recovery rate model is suggested since the
recovery rate seems to be subject to the market conditions; that
is, higher in a bull market and lower in a bear market. By closely
looking, one observes a lower average annual recovery rate in the
period 1998 to 2001 (internet bubble) and 2008 to 2009 (US
subprime crisis) compared to the rest of the periods with bullish prospects. It is certain that the recovery rate in
the bull market should not be lower than that in the bear market.
Therefore, the recovery rate is likely to vary with market
conditions, which resembles the behaviour of the default rate. Notice
that the market condition is the unique common factor shared
between recovery rate and default
rate, and causes their time variations.

|  | Bond | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Year | Sr. Sec. | Sr. Unsec. | Sr. Sub. | Sub. | Jr. Sub. | All Bonds |
| 1997 | 75.5% | 56.1% | 44.7% | 33.1% | 30.6% | 48.8% |
| 1998 | 46.8% | 39.5% | 45.0% | 18.2% | 62.0% | 38.3% |
| 1999 | 36.0% | 38.0% | 26.9% | 35.6% | n.a. | 33.8% |
| 2000 | 38.6% | 24.2% | 20.8% | 31.9% | 7.0% | 25.1% |
| 2001 | 31.7% | 21.2% | 19.8% | 15.9% | 47.0% | 21.6% |
| 2002 | 50.6% | 29.5% | 21.4% | 23.4% | n.a. | 29.7% |
| 2003 | 69.2% | 41.9% | 37.2% | 12.3% | n.a. | 41.2% |
| 2004 | 73.3% | 52.1% | 42.3% | 94.0% | n.a. | 58.5% |
| 2005 | 71.9% | 54.9% | 32.8% | 51.3% | n.a. | 56.5% |
| 2006 | 74.6% | 55.0% | 41.4% | 56.1% | n.a. | 55.0% |
| 2007 | 80.6% | 53.7% | 56.2% | n.a. | n.a. | 55.1% |
| 2008 | 54.9% | 33.2% | 23.3% | 23.6% | n.a. | 33.9% |
| 2009 | 37.5% | 36.9% | 22.7% | 45.3% | n.a. | 33.9% |
| 2010 | 62.5% | 51.5% | 37.5% | 33.7% | n.a. | 51.8% |
| 2011 | 63.3% | 41.3% | 36.7% | 35.4% | n.a. | 46.3% |
| 2012 | 51.2% | 43.0% | 33.7% | 37.3% | n.a. | 44.7% |
| 2013 | 57.7% | 43.8% | 20.7% | 26.4% | n.a. | 45.6% |

Table 1: Annual defaulted corporate bond recoveries
Annual corporate bond recovery rates based on post default trading
price, Moody’s 27th annual default study. Note that Sr. Sec., Sr. Unsec., Sr. Sub., Sub., and Jr. Sub. represent senior secured, senior unsecured, senior subordinated, subordinated and junior subordinated, respectively.

Andersen and Sidenius ([2004](#bib.bib5)) address that
both default events and recovery rates are driven by a single
factor, but with an independent assumption between default and
recovery rate. There are reasons to doubt this assumption.
Chen ([2010](#bib.bib11)) demonstrates that the
recovery rates are strongly negatively correlated with default
rates (is given as -0.82). As a consequence, the dependence
between them depends on the common factor represented by the state
of macroeconomics. We claim that the common factor (market) governs the default rate and recovery rate simultaneously and creates their association implicitly. One of our purposes is to build a tractable
model that is capable of reflecting the obligors’ behaviour in
reacting to the impact from the market. In addition, we show that a systematic risk plays a critical role
in credit measurement and prediction, and contributes more
to a firm’s credit risk in a market downturn than in a tranquil
period. In this sense, the factor loading on common factor is conditional on market states. This conditional specification enables risk managers to be alerted regarding risk to the deterioration of the credit conditions when the market
turns
down, which avoids underestimating the default probability.

We extend the one factor Gaussian copula model in two ways.
Firstly, to improve the factor loading of
Andersen and Sidenius ([2004](#bib.bib5)) given a two-point
distribution, we apply the state-dependent concept from
Kim and Finger ([2000](#bib.bib32)) with the specific distributions
to characterise the correlations in hectic or quiet periods, respectively. It
potentially captures two typical features of equity index
distributions: fat tails and a skew to the left. However, for a
two-point distribution setting, it is difficult to decide on the threshold
level of the two-point distribution, and on a time to be chosen
arbitrarily. Secondly, by relaxing the constant recovery rate presumed naively by academia and industry, our state-dependent
recovery rate model permits that the systematic risk factor determines the Loss Given Default (LGD), as suggested by
Amraoui et al. ([2012](#bib.bib3)). In addition, it
restricts the recovery rate, as a percentage of the notional is
bounded on [0,1] to achieve the tractable and numerically
efficient missions. In summary, we contribute the incorporation of
the state-dependent recovery rate into the conditional factor
copula model, and model them by sharing the unique common factor.
The common factor governs the default rate and recovery rate
simultaneously, and creates their association implicitly. Our
Monte Carlo simulation and empirical evidence
appropriately reflect this feature.

We propose four competing default models that have been widely
applied to measure credit risk, and evaluate their relative
performances on the accuracy of forecasting default in the
following year. This comparison, by mapping the various factor
copula models developed in the past and current literature to the
competing models, fosters the discussion on the model performance.
Therefore, to achieve a broader and robust comparison, we group
the factor copula models developed in the literature into four competing
models: (1) The FC model: the standard one-factor
Gaussian copula model with the constant recovery rate
(Van der Voort, [2007](#bib.bib45); Rosen and Saunders, [2010](#bib.bib40)). (2) The RFL model: the
one-factor Gaussian copula model with the factor loadings tied to
the state of common factor and the recoveries being assumed constant (Kalemanova et al., [2007](#bib.bib30); Chen et al., [2014](#bib.bib12)). (3) The RR model: standard
one-factor Gaussian copula model but the recoveries being related
to the state of the macroeconomic state
(Amraoui and Hitier, [2008](#bib.bib4);
Elouerkhaoui, [2009](#bib.bib19); Amraoui et al., [2012](#bib.bib3)), and (4) The RRFL
model: a conditional factor
loading specification together with a state-dependent recovery rate, and this is the model what we are developing and contributing to. If further empirical results show its best performance on default prediction, the outstanding performance of our refined RRFL model becomes very clear.

In the FC model, we estimate the Spearman’s correlation coefficient
between each obligor and common factor and set the recovery rate
as constant. This is a conventional model to measure the capital
requirement in the Basel II accord. By relaxing the constant
correlation in the RFL model, we suggest that the conditional factor loading plays
a significant role in capturing an asymmetric systematic impact
from the market. The RR model uses the method
proposed by Amraoui et al. ([2012](#bib.bib3)) to
investigate the effect of stochastic recovery rate. It allows the
LGD function to be driven by the common factor and the hazard rate, but keeps factor loadings constant. In the RRFL
model, we incorporate the conditional factor loading into
state-dependent recovery rate and model them by sharing the unique
common factor. To evaluate whether these two specifications carry
significant improvements to the default prediction, we use the data
set of daily stock indices of the S&P 500 to represent the market (common factor) and the respective stock prices
of the default companies for the period of 5 years before
the default year from the Datastream database.

Our default data analysis contains 2008 and 2009, as collected by
Moody’s report. We use Moody’s Ultimate Recovery Database (URD)
which is the ultimate payoff that obligors can obtain when the default
emerges from bankruptcy or is liquidated instead of the
post-default trading price as proposed by
Carty et al. ([1998](#bib.bib10)). They examine whether the
trading price represents a rational forecast of actual recovery,
and find that it is not a rational estimation of actual
recovery. For this period, we employ a state-dependent concept in
order to capture an asymmetric impact from the common risk factor.
As a result, we achieve the goal that both conditional factor loading and
state-dependent recovery rates improve the calibration of our default
prediction. The conventional factor copula underestimates the
impact of systematic risk and portfolio credit loss when the market is in downturn. We find that the incorporation of
factor loading into the state-dependent recovery rate improves the accuracy of the default prediction. This
result is coherent with the goal of Basel III, which emphasises the role of systematic risk on overall
financial stability and systemic risk. In our later empirical analysis, we concentrate on the senior unsecured bond, since there is a rich data source available.

The remainder of the study is organised as follows. Section 2
describes the goal of Basel III. We present a general framework
and the standard one-factor Copula in section 3. Besides, we
extend the standard one-factor Copula by using the conditional factor
loading and the state-dependent recovery model. Section 4 describes
the data set. In the section 5, we offer empirical evidence.
Section 6
presents the conclusion.

## 2 Systematic risk in Basel III

As highlighted by Basel III, systemic risk is crucial in financial markets from several aspects. First, a bank can trigger a shock throughout a system and spill over to its counterparties (Drehmann and Tarashev, [2013](#bib.bib18)).
Secondly, procyclicality could destabilise the whole
systemic risk (Committee et al., [2009](#bib.bib15)). The borrowers hardly fund more as their collateral assets have depreciated caused by weak economic conditions. Third, since Basel II focused on minimising the default probability of individuals, this accord failed to guarantee a stable financial system due to a lack of concern for systemic risk. Therefore, a new Basel accord is expected to emphasize its role.

Systematic factor is one of the important drivers of systemic risk and probably constituting a serious threat to systemic fragility ( Schwerter, [2011](#bib.bib42);  Uhde and Michalak, [2010](#bib.bib44)). Tarashev et al. ([2010](#bib.bib43)) also distinguish between systemic risk and systematic risk. The former refers to the risk that impedes the financial system, while the latter refers to the commonality in risk exposures of financial institutions. Their model assumes that systemic risk can have systematic and idiosyncratic components. It is understandable that systemic risk is heightened by systematic risk. A bank is characterised as one of systemically important (too-big-to-fail) financial institutions, its default would lead to a dramatic impact on systemic risk. This is the very reason what Basel III attempts to regulate and prevent. Through our paper, our model proposes that the contribution of systematic risk is higher than that of idiosyncratic component, and this dominance is characterised by a higher factor loading on systematic risk during a market downturn. We, therefore, see the contribution of systematic risk on credit risk varies with time and market conditions. In this regard, one shall concern on the interconnection between credit risk and market risk. It is worth noting that the points mentioned above determine the sufficiency of capital requirement in the banking industry.

To obtain the sufficient capital requirements, recovery rate is one of determinant variables in credit risk estimation. A real observation is that in a recession period, recovery rates tend to decrease while default rates tend to rise. As such, increasing capital requirement under this condition seems necessary. Most early academic studies on credit risk assume that recovery rates are deterministic ( Schönbucher, [2001](#bib.bib41);  Rosen and Saunders, [2010](#bib.bib40)), or they are stochastic but independent from default probabilities ( Jarrow et al., [1997](#bib.bib29);  Andersen and Sidenius, [2004](#bib.bib5)). Neglecting the nature of stochastic in recovery rate and the interdependence between recovery rates and default rates result in a biased credit risk estimation ( Altman et al., [2005](#bib.bib2)).

To be close to the spirit of Basel III, our study extends the existing literature into two dimensions. First, we highlight that systematic risk is a predominant factor in a recession period, and proceed a relative contribution analysis to measure the proportional contribution from a systematic risk in comparison with that from an idiosyncratic component. Second, we propose a methodology in which recovery rates and default rates are correlated by sharing a unique factor, and both are state-dependent. Our model design, the simulation and empirical results provide a bundle of justifications for the goals of Basel III.

## 3 Methodology

### 3.1 Default modelling

Recognising the importance of systematic risk, one-factor Gaussian models have been considered an important tool
underlying the internal ratings based approach (
Crouhy et al., [2000](#bib.bib16); 
Pykhtin and Dev, [2002](#bib.bib38); 
Frey and McNeil, [2003](#bib.bib22)) and used to price CDOs
( Hull and White, [2004](#bib.bib28); 
Andersen and Sidenius, [2004](#bib.bib5); 
Choroś-Tomczyk et al., [2013](#bib.bib13)). It reduces the number of
correlations being estimated from N​(N−1)2𝑁𝑁12\frac{N(N-1)}{2} by a
multivariate Gaussian Model to N𝑁N which represents the number of assets. Specifically, we use
a non-standardised Gaussian model to represent the deteriorating
market condition by presuming a negative mean value together with a higher volatility.
The model is based on decomposing a latent variable Uisubscript𝑈𝑖U\_{i} for obligor i𝑖i into the systematic factor Z𝑍Z and the idiosyncratic component εi​tsubscript𝜀𝑖𝑡\varepsilon\_{it}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui=αi​Z+1−αi2​εii=1,…,Nformulae-sequencesubscript𝑈𝑖subscript𝛼𝑖𝑍1superscriptsubscript𝛼𝑖2subscript𝜀𝑖𝑖  1…𝑁U\_{i}=\alpha\_{i}Z+\sqrt{1-\alpha\_{i}^{2}}\varepsilon\_{i}\hskip 14.22636pti=1,\ldots,N |  | (1) |

where −1≤αi≤11subscript𝛼𝑖1-1\leq\alpha\_{i}\leq 1. Suppose that Z∼N​(μ,σ2)similar-to𝑍N𝜇superscript𝜎2Z\sim\textsf{N}(\mu,\sigma^{2}) and εisubscript𝜀𝑖\varepsilon\_{i} have zero-mean
unit-variance distributions. In a Gaussian content, Z𝑍Z and
εisubscript𝜀𝑖\varepsilon\_{i} are orthogonal and εisubscript𝜀𝑖\varepsilon\_{i} are
mutually uncorrelated. The distribution of vector U𝑈U can be
described by a copula
function which joins two marginals, Z𝑍Z and εisubscript𝜀𝑖\varepsilon\_{i}. The correlation coefficient ρi​jsubscript𝜌𝑖𝑗\rho\_{ij} between Uisubscript𝑈𝑖U\_{i} and Ujsubscript𝑈𝑗U\_{j} can be described by their αisubscript𝛼𝑖\alpha\_{i} and αjsubscript𝛼𝑗\alpha\_{j}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρi​j=αi​αj​σ2αi2​(σ2−1)+1​αj2​(σ2−1)+1subscript𝜌𝑖𝑗subscript𝛼𝑖subscript𝛼𝑗superscript𝜎2superscriptsubscript𝛼𝑖2superscript𝜎211superscriptsubscript𝛼𝑗2superscript𝜎211\rho\_{ij}=\frac{\alpha\_{i}\alpha\_{j}\sigma^{2}}{\sqrt{\alpha\_{i}^{2}(\sigma^{2}-1)+1}\sqrt{\alpha\_{j}^{2}(\sigma^{2}-1)+1}} |  | (2) |

where σi=αi2​(σ2−1)+1,σj=αj2​(σ2−1)+1formulae-sequencesubscript𝜎𝑖superscriptsubscript𝛼𝑖2superscript𝜎211subscript𝜎𝑗superscriptsubscript𝛼𝑗2superscript𝜎211\sigma\_{i}=\sqrt{\alpha\_{i}^{2}(\sigma^{2}-1)+1},\sigma\_{j}=\sqrt{\alpha\_{j}^{2}(\sigma^{2}-1)+1}. As a consequence,
the number of correlations describing the dependency structure is
reduced in size since only N𝑁N parameters αi:i=1,…,N:subscript𝛼𝑖𝑖

1…𝑁{\alpha\_{i}:i=1,\ldots,N} need to be estimated.
We express the covariance matrices between Uisubscript𝑈𝑖U\_{i} and Ujsubscript𝑈𝑗U\_{j} under a factor model,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σi​j=σi2​σj2​(1ρi​jρj​i1)subscriptΣ𝑖𝑗superscriptsubscript𝜎𝑖2superscriptsubscript𝜎𝑗21subscript𝜌𝑖𝑗subscript𝜌𝑗𝑖1\Sigma\_{ij}=\sigma\_{i}^{2}\sigma\_{j}^{2}\left(\begin{array}[c]{cc}1&\rho\_{ij}\\ \rho\_{ji}&1\end{array}\right) |  | (3) |

The one-factor Gaussian copula model we consider is used
to model the default indicators to time t𝑡t, 𝐈​{τi≤t}𝐈subscript𝜏𝑖𝑡\mathbf{I}\left\{\tau\_{i}\leq t\right\}, by projecting Uisubscript𝑈𝑖U\_{i}
into τisubscript𝜏𝑖\tau\_{i}. Uisubscript𝑈𝑖U\_{i} here can be viewed as the proxies for firm
asset and liquidation value (
Andersen and Sidenius, [2004](#bib.bib5)). In this regard, the lower
asset value of firm the shorter time to default, τisubscript𝜏𝑖\tau\_{i}. More
precisely, Ui≤F−1​{Pi​(t)}subscript𝑈𝑖superscript𝐹1subscript𝑃𝑖𝑡U\_{i}\leq F^{-1}\{P\_{i}(t)\} leads to τi≤tsubscript𝜏𝑖𝑡\tau\_{i}\leq t, where
Pi​(t)subscript𝑃𝑖𝑡P\_{i}(t) is a hazard rate and marginal probability that obligor i𝑖i
defaults before t𝑡t, and F−1​(⋅)superscript𝐹1⋅F^{-1}(\cdot) donates the inverse cdf of any distribution. The default indicator then can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐈​{τi≤t}=𝐈​[Ui≤F−1​{Pi​(t)}]𝐈subscript𝜏𝑖𝑡𝐈delimited-[]subscript𝑈𝑖superscript𝐹1subscript𝑃𝑖𝑡\mathbf{I}\left\{\tau\_{i}\leq t\right\}=\mathbf{I}\left[U\_{i}\leq F^{-1}\{P\_{i}(t)\}\right] |  | (4) |

Given the LGD for each i𝑖i, Gi,i=1,…,Nformulae-sequence

subscript𝐺𝑖𝑖
1

…𝑁G\_{i},i=1,\ldots,N, we aggregate them as total portfolio loss, L𝐿L, as following,

|  |  |  |  |
| --- | --- | --- | --- |
|  | L=∑i=1NGi​𝐈​{τi≤t}=∑i=1NGi​𝐈​[Ui≤F−1​{Pi​(t)}]𝐿superscriptsubscript𝑖1𝑁subscript𝐺𝑖𝐈subscript𝜏𝑖𝑡superscriptsubscript𝑖1𝑁subscript𝐺𝑖𝐈delimited-[]subscript𝑈𝑖superscript𝐹1subscript𝑃𝑖𝑡L=\displaystyle\sum\_{i=1}^{N}G\_{i}\mathbf{I}\left\{\tau\_{i}\leq t\right\}=\displaystyle\sum\_{i=1}^{N}G\_{i}\mathbf{I}\left[U\_{i}\leq F^{-1}\{P\_{i}(t)\}\right] |  | (5) |

### 3.2 Conditional default model

In accordance with the spirit of Basel III, the systematic latent factor, Z𝑍Z, representing the general economic
condition that characterises the systematic credit risk influences the default probability Pi​(t)subscript𝑃𝑖𝑡P\_{i}(t) and the
recovery rate Ri=1−Gisubscript𝑅𝑖1subscript𝐺𝑖R\_{i}=1-G\_{i}. So given Z𝑍Z, one may write the
conditional default probability Pi​(Z|S=H,Q)subscript𝑃𝑖conditional𝑍𝑆

𝐻𝑄P\_{i}(Z|S=H,Q)
and conditional LGD, Gi​(Z|S=H,Q)subscript𝐺𝑖conditional𝑍𝑆

𝐻𝑄G\_{i}(Z|S=H,Q) as a function of Z𝑍Z, and it is state-dependent, S∈{H,Q}SH,Q\mbox{S}\in\{\mbox{H,Q}\}. H, and Q represent the hectic and quiet periods, respectively.

A higher factor loading, αisubscript𝛼𝑖\alpha\_{i} in equation (1) has been observed in hectic periods (
Longin and Solnik, [2001](#bib.bib33); [Ang and Bekaert](#bib.bib6)
2002a; [Ang and Chen](#bib.bib7) 2002b). This
observation can be modelled by a regime-switching mechanism, requiring a
globally valid time series structure for αisubscript𝛼𝑖\alpha\_{i} from t𝑡t.
Avoiding such a possible too rigid structure, we assume the two
asset returns, Z𝑍Z common factor proxied by USD S&P 500, Uisubscript𝑈𝑖U\_{i} (firm stock price) have a mixture of bivariate normal distribution
(See Appendix A) to obtain the estimation of αiHsubscriptsuperscript𝛼𝐻𝑖\alpha^{H}\_{i} and αiQsubscriptsuperscript𝛼𝑄𝑖\alpha^{Q}\_{i}. Given the
conditional factor loading, αiH,αiQ

subscriptsuperscript𝛼𝐻𝑖subscriptsuperscript𝛼𝑄𝑖\alpha^{H}\_{i},\alpha^{Q}\_{i}, the conditional default model is defined as following,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui|S=H=αiH​Z+1−(αiH)2​εievaluated-atsubscript𝑈𝑖S=Hsubscriptsuperscript𝛼𝐻𝑖𝑍1superscriptsubscriptsuperscript𝛼𝐻𝑖2subscript𝜀𝑖U\_{i}|\_{\mbox{S=H}}=\alpha^{H}\_{i}Z+\sqrt{1-(\alpha^{H}\_{i})^{2}}\varepsilon\_{i} |  | (6) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui|S=Q=αiQ​Z+1−(αiQ)2​εievaluated-atsubscript𝑈𝑖S=Qsubscriptsuperscript𝛼𝑄𝑖𝑍1superscriptsubscriptsuperscript𝛼𝑄𝑖2subscript𝜀𝑖U\_{i}|\_{\mbox{S=Q}}=\alpha^{Q}\_{i}Z+\sqrt{1-(\alpha^{Q}\_{i})^{2}}\varepsilon\_{i} |  | (7) |

Therefore, the state-dependent conditional default probability can be denoted by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τi​<t|​S)=F​[F−1​{Pi​(t)}−αiS​Z1−(αiS)2]=Pi​(Z|S)S∈{H,Q}formulae-sequence𝑃subscript𝜏𝑖bra𝑡S𝐹delimited-[]superscript𝐹1subscript𝑃𝑖𝑡subscriptsuperscript𝛼𝑆𝑖𝑍1superscriptsubscriptsuperscript𝛼𝑆𝑖2subscript𝑃𝑖conditional𝑍SSH,QP(\tau\_{i}<t|\mbox{S})=F\left[{\frac{F^{-1}\{P\_{i}(t)\}-\alpha^{S}\_{i}Z}{\sqrt{1-(\alpha^{S}\_{i})^{2}}}}\right]=P\_{i}(Z|\mbox{S})\hskip 14.22636pt\mbox{S}\in\{\mbox{H,Q}\} |  | (8) |

Given Pi​(t)subscript𝑃𝑖𝑡P\_{i}(t), if the factor loadings
in hectic periods are greater than ones in quiet days, say αH>αQsuperscript𝛼𝐻superscript𝛼𝑄\alpha^{H}>\alpha^{Q}, and if the index return of S&P 500 is negative in a bad
market condition, both conditions will result in a higher conditional default
probability in equation (8). From equation (8), the systematic
risk, Z𝑍Z, and the corresponding factor loading govern the
conditional default probability, which is consistent with
empirical findings (Andersen and Sidenius, [2004](#bib.bib5);
Bonti et al., [2006](#bib.bib8)). It is worth pointing out that αiSsubscriptsuperscript𝛼𝑆𝑖\alpha^{S}\_{i} is state-dependent instead of a
constant setting in previous literature
(Andersen and Sidenius, [2004](#bib.bib5);
Amraoui et al., [2012](#bib.bib3)).
[Ang and Chen](#bib.bib7) (2002b) set
probability of both regimes equally (w=0.5𝑤0.5w=0.5), instead, we
estimate it from the historical data of the S&P 500 Index return proxied for systematic risk, Z𝑍Z, P(S=H)=ω𝜔\omega, P(S=Q)=1−ω1𝜔1-\omega by
Expectation-Maximization (EM) algorithm.

Likewise, the recovery rates can be designed in this way by incorporating market condition as a main driver across different states. Based on the finding of
Das and Hanouna ([2009](#bib.bib17)), recovery rates are
negatively correlated with probabilities of defaults and driven by market condition. By relaxing
constant recovery rates, we follow
Amraoui et al. ([2012](#bib.bib3)) to connect recovery rates
and default events via a common factor, but extend their model to a
conditional or state-dependent framework. The recovery rate is
governed by the state of economy, in addition, we
incorporate a conditional correlation structure, αiSsubscriptsuperscript𝛼𝑆𝑖\alpha^{S}\_{i}, into stochastic recovery rate model, and set Ri​(Z|S=H,Q)subscript𝑅𝑖conditional𝑍𝑆

𝐻𝑄R\_{i}(Z|S=H,Q), of obligor i𝑖i, in relation
to the common factor Z𝑍Z and the marginal default probability
Pisubscript𝑃𝑖P\_{i}. The state-dependent recovery rate is expressed as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gi​(Z|S=H)=(1−Ri¯)​F​[{F−1​(P¯i)−αiH​Z}/1−(αiH)2]F​[{F−1​(Pi)−αiH​Z}/1−(αiH)2]subscript𝐺𝑖conditional𝑍S=H1¯subscript𝑅𝑖𝐹delimited-[]superscript𝐹1subscript¯𝑃𝑖subscriptsuperscript𝛼𝐻𝑖𝑍1superscriptsubscriptsuperscript𝛼𝐻𝑖2𝐹delimited-[]superscript𝐹1subscript𝑃𝑖subscriptsuperscript𝛼𝐻𝑖𝑍1superscriptsubscriptsuperscript𝛼𝐻𝑖2G\_{i}(Z|\mbox{S=H})=(1-\overline{R\_{i}})\frac{F\left[\{F^{-1}\left(\overline{P}\_{i}\right)-\alpha^{H}\_{i}Z\}/\sqrt{1-(\alpha^{H}\_{i})^{2}}\right]}{F\left[\{F^{-1}\left(P\_{i}\right)-\alpha^{H}\_{i}Z\}/\sqrt{1-(\alpha^{H}\_{i})^{2}}\right]} |  | (9) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gi​(Z|S=Q)=(1−Ri¯)​F​[{F−1​(P¯i)−αiQ​Z}/1−(αiQ)2]F​[{F−1​(Pi)−αiQ​Z}/1−(αiQ)2]subscript𝐺𝑖conditional𝑍S=Q1¯subscript𝑅𝑖𝐹delimited-[]superscript𝐹1subscript¯𝑃𝑖subscriptsuperscript𝛼𝑄𝑖𝑍1superscriptsubscriptsuperscript𝛼𝑄𝑖2𝐹delimited-[]superscript𝐹1subscript𝑃𝑖subscriptsuperscript𝛼𝑄𝑖𝑍1superscriptsubscriptsuperscript𝛼𝑄𝑖2G\_{i}(Z|\mbox{S=Q})=(1-\overline{R\_{i}})\frac{F\left[\{F^{-1}\left(\overline{P}\_{i}\right)-\alpha^{Q}\_{i}Z\}/\sqrt{1-(\alpha^{Q}\_{i})^{2}}\right]}{F\left[\{F^{-1}\left(P\_{i}\right)-\alpha^{Q}\_{i}Z\}/\sqrt{1-(\alpha^{Q}\_{i})^{2}}\right]} |  | (10) |

In equation (9, 10), 0≤Ri¯≤Ri≤10¯subscript𝑅𝑖subscript𝑅𝑖10\leq\bar{R\_{i}}\leq R\_{i}\leq 1
which means a downward shift of Ri¯¯subscript𝑅𝑖\bar{R\_{i}} to Risubscript𝑅𝑖R\_{i}, so that
Ri¯=Ri−υ¯subscript𝑅𝑖subscript𝑅𝑖𝜐\bar{R\_{i}}=R\_{i}-\upsilon and Ri≥υ>0subscript𝑅𝑖𝜐0R\_{i}\geq\upsilon>0. υ𝜐\upsilon is size
of downward shift. By assuming that expected loss in name i𝑖i
remains unchanged, we set (1−Ri)​Pi=(1−R¯i)​P¯i1subscript𝑅𝑖subscript𝑃𝑖1subscript¯𝑅𝑖subscript¯𝑃𝑖(1-R\_{i})P\_{i}=(1-\bar{R}\_{i})\bar{P}\_{i}.
Please see the proof in A.1 in
Amraoui et al. ([2012](#bib.bib3)). F​(⋅)𝐹⋅F(\cdot) denotes any
distribution and P¯isubscript¯𝑃𝑖\overline{P}\_{i} is the adjusted default
probability calibrated proposed by
Amraoui and Hitier ([2008](#bib.bib4)). The LGD function,
Gi​(Z|S=H,Q)subscript𝐺𝑖conditional𝑍S=H,QG\_{i}(Z|\mbox{S=H,Q}) essentially can be obtained according to
formula (9,10). Numerous studies show that recoveries decline
during recessions ( Altman et al., [2005](#bib.bib2);
 Bruche and Gonzalez-Aguado, [2010](#bib.bib9)). Consistent with the
spirit of equation (6,7), we design αHsuperscript𝛼𝐻\alpha^{H}, αQsuperscript𝛼𝑄\alpha^{Q}, the
factor loading in equation (9,10) are therefore conditional and
state-dependent. Moreover, a partial derivative of LGD function
with respect to Z𝑍Z is less than zero proved by property 3.2 in
Amraoui and Hitier ([2008](#bib.bib4)), which means that
Gi​(Z|S=H,Q)subscript𝐺𝑖conditional𝑍S=H,QG\_{i}(Z|\mbox{S=H,Q}) is decreasing in Z𝑍Z. By assuming αH>αQsuperscript𝛼𝐻superscript𝛼𝑄\alpha^{H}>\alpha^{Q}, which means that a higher factor loading that is usually accompanied by a bad market condition on Z𝑍Z tends to increase LGD. The magnitude of LGD is not only influenced by Z𝑍Z but also sensitive to the factor loading under Z𝑍Z; this is what we point out and contribute to the literature. In addition, recovery rates are
also linked to the probability of default and they are negatively
correlated (see  Altman et al., [2005](#bib.bib2);
 Khieu et al., [2012](#bib.bib31)). With
Z𝑍Z, Pisubscript𝑃𝑖P\_{i} and the estimated conditional factor loading
αHsuperscript𝛼𝐻\alpha^{H}, αQsuperscript𝛼𝑄\alpha^{Q}, we obtain the state-dependent recovery
rate, Ri​(Z|S=H,Q)subscript𝑅𝑖conditional𝑍S=H,QR\_{i}(Z|\mbox{S=H,Q}), and state-dependent LGD, Gi​(Z|S=H,Q)=1−Ri​(Z|S=H,Q)subscript𝐺𝑖conditional𝑍S=H,Q1subscript𝑅𝑖conditional𝑍S=H,QG\_{i}(Z|\mbox{S=H,Q})=1-R\_{i}(Z|\mbox{S=H,Q}).

With these two specifications, the conditional default probability
Pi​(Z|S=H,Q)subscript𝑃𝑖conditional𝑍S=H,QP\_{i}(Z|\mbox{S=H,Q}) and conditional LGD, Gi​(Z|S=H,Q)subscript𝐺𝑖conditional𝑍S=H,QG\_{i}(Z|\mbox{S=H,Q}),
conditional expected loss,
therefore, is

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(Li|Z)=ω​Gi​(Z|S=H)​Pi​(Z|S=H)+(1−ω)​Gi​(Z|S=Q)​Pi​(Z|S=Q)Econditionalsubscript𝐿𝑖𝑍𝜔subscript𝐺𝑖conditional𝑍S=Hsubscript𝑃𝑖conditional𝑍S=H1𝜔subscript𝐺𝑖conditional𝑍S=Qsubscript𝑃𝑖conditional𝑍S=Q\textsf{E}(L\_{i}|Z)=\omega G\_{i}(Z|\mbox{S=H})P\_{i}(Z|\mbox{S=H})+(1-\omega)G\_{i}(Z|\mbox{S=Q})P\_{i}(Z|\mbox{S=Q}) |  | (11) |

where ω=P(S=H)𝜔P(S=H)\omega=\mbox{P(S=H)} and 1−ω=P(S=Q)1𝜔P(S=Q)1-\omega=\mbox{P(S=Q)}. H and Q represent the hectic and quiet periods, respectively.

### 3.3 Monte Carlo simulation

In this section, we investigate the performance of default
prediction by establishing a simulation of realistic scenarios.
The default probability and recovery rate function are governed by
systematic factors generated from different regimes. Indeed, they
are crucial elements in evaluating the accuracy of the default
prediction. Our interest is to see whether the design of
conditional factor loadings and state-dependent recovery rates contribute to the
default prediction.

#### 3.3.1 One-factor non-standardized Gaussian copula

We simulate one-factor non-standardised Gaussian copula subject to
different states. As described in equation (6) and (7), we
generate systematic factor Z𝑍Z by non-standardised Gaussian
distribution with different volatilities and independent
εi′​ssuperscriptsubscript𝜀𝑖′𝑠\varepsilon\_{i}^{\prime}s . To reflect the nature of distinct
variations exhibited in different market conditions.

Through a mixture bivariate distribution setting in Appendix A,
the conditional factor loadings, αiHsubscriptsuperscript𝛼𝐻𝑖\alpha^{H}\_{i} and αiQsubscriptsuperscript𝛼𝑄𝑖\alpha^{Q}\_{i} are
derived, in the one-factor non-standardised Gaussian copula model.
We estimate them from the daily stock returns of S&P 500 and of
collected default companies during the crisis (2008-2009) period.
The five-year period prior to the crisis period is the estimation
period for the conditional factor loadings. The return of S&P 500
Index represented as a systematic factor, Z𝑍Z, is presumed to
distribute as N​(−0.03,3.05)N0.033.05\textsf{N}(-0.03,3.05) estimated in 2008 and
2009, while εi∼N​(0,1)similar-tosubscript𝜀𝑖N01\varepsilon\_{i}\sim\textsf{N}(0,1) represents
idiosyncratic risk. Z𝑍Z and εisubscript𝜀𝑖\varepsilon\_{i} are generated 1000
scenarios, respectively. Given any one of generated systematic
factor random variables, Z𝑍Z, and using Bayes’ rule, we calculate
the conditional probability that date t𝑡t belonged to the hectic
is π​(Z=z)𝜋𝑍𝑧\pi(Z=z) by using its counterpart,
unconditional probability ω𝜔\omega, as a formula (12).

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(S=H|Z=z)=π​(Z=z)=ω​φ​(z|θH)(1−ω)​φ​(z|θQ)+ω​φ​(z|θH)P𝑆conditional𝐻𝑍𝑧𝜋𝑍𝑧𝜔𝜑conditional𝑧superscript𝜃𝐻1𝜔𝜑conditional𝑧superscript𝜃𝑄𝜔𝜑conditional𝑧superscript𝜃𝐻\mbox{P}(S=H|Z=z)=\pi(Z=z)=\frac{\omega\varphi(z|\theta^{H})}{(1-\omega)\varphi(z|\theta^{Q})+\omega\varphi(z|\theta^{H})} |  | (12) |

θH,θQ

superscript𝜃𝐻superscript𝜃𝑄\theta^{H},\theta^{Q} represent the parameters of
distribution in the hectic (H) and the quiet (Q) period. φ​(⋅)𝜑⋅\varphi(\cdot)
is a normal distribution. Plugging αiH,αiQ

subscriptsuperscript𝛼𝐻𝑖subscriptsuperscript𝛼𝑄𝑖\alpha^{H}\_{i},\alpha^{Q}\_{i} shared
with the same simulated Z𝑍Z random variables, conditional Ui|U\_{i}|S
is generated as developed in equation(6, 7). These simulated
random variables together with the published hazard rates hi​(t)subscriptℎ𝑖𝑡h\_{i}(t)
ideally produce the simulated default times.

#### 3.3.2 Default time

Projecting Uisubscript𝑈𝑖U\_{i} simulated from section 3.3.1 to default time, τisubscript𝜏𝑖\tau\_{i}, stated
in equation(4) provides the clue as to whether the firm defaults before
time. We set t=1𝑡1t=1, represents the time interval of 1 year, so
that τi<1subscript𝜏𝑖1\tau\_{i}<1 is referred to a default event in the i𝑖ith
obligor. The hazard rate hisubscriptℎ𝑖h\_{i} is the probability of
occurrence of the default event within one year. τisubscript𝜏𝑖\tau\_{i} is
referred to default time of i𝑖ith obligor. More precisely, the
expected value of E​[I​(τi<1)]Edelimited-[]Isubscript𝜏𝑖1\textsf{E}[\mbox{I}(\tau\_{i}<1)] is
P​(τi<1)Psubscript𝜏𝑖1\mbox{P}(\tau\_{i}<1) or named as Pisubscript𝑃𝑖P\_{i}, see
Franke et al. ([2015](#bib.bib21)) Chapter 22, that can be
connected to the firm’s stock return or firm’s value, Uisubscript𝑈𝑖U\_{i} leads
to Pi=E​[I​{Ui<Fi−1​(Pi)}]subscript𝑃𝑖Edelimited-[]Isubscript𝑈𝑖superscriptsubscript𝐹𝑖1subscript𝑃𝑖P\_{i}=\textsf{E}[\mbox{I}\{U\_{i}<F\_{i}^{-1}(P\_{i})\}] where Fisubscript𝐹𝑖F\_{i}
denote the cdf of Uisubscript𝑈𝑖U\_{i}. By applying generated Uisubscript𝑈𝑖U\_{i} from the
conditional factor model into the definition of the survival rate, we
have generated default time, τisubscript𝜏𝑖\tau\_{i}, derived from
1−exp​(−Pi​τi)=F​(Ui)1expsubscript𝑃𝑖subscript𝜏𝑖𝐹subscript𝑈𝑖1-\mbox{exp}(-P\_{i}\tau\_{i})=F(U\_{i})
( Hull, [2006](#bib.bib26)). To keep on the state-dependent environment, the conditional default time for each obligor is generated by formula (13).

|  |  |  |  |
| --- | --- | --- | --- |
|  | τi|S=−log​{1−F​(Ui|S)}Piconditionalsubscript𝜏𝑖Slog1𝐹evaluated-atsubscript𝑈𝑖Ssubscript𝑃𝑖\tau\_{i}|\mbox{S}=-\frac{\mbox{log}\{1-F(U\_{i}|\_{\mbox{S}})\}}{P\_{i}} |  | (13) |

where Pisubscript𝑃𝑖P\_{i} is the hazard rate or marginal probability
that obligor i𝑖i will default during the first year, conditional on
no earlier default, and is obtained from Moody’s report. It is the
cumulative of default rates during the first year. Equation (13) states that
Ui|Sconditionalsubscript𝑈𝑖SU\_{i}|\mbox{S} becomes larger, τi|Sconditionalsubscript𝜏𝑖S\tau\_{i}|\mbox{S} will become
longer. The larger Uisubscript𝑈𝑖U\_{i} reduces the tendency of default and
postpones the default time, τi|Sconditionalsubscript𝜏𝑖S\tau\_{i}|\mbox{S}.

#### 3.3.3 State-dependent recovery rate simulation

In the third step, we consider a more realistic situation by
simulating recovery rates as described in our settings. The
adjusted default probability Pi¯¯subscript𝑃𝑖\bar{P\_{i}} is calibrated by using
hazard rate Pisubscript𝑃𝑖P\_{i} from Moody’s report. Ri¯¯subscript𝑅𝑖\bar{R\_{i}} is a lower
bound for state-dependent recovery rates [0,1], therefore, we set
Ri¯=0¯subscript𝑅𝑖0\bar{R\_{i}}=0 in the simplest case. With αiH,αiQ,Z,Pi¯

subscriptsuperscript𝛼𝐻𝑖subscriptsuperscript𝛼𝑄𝑖𝑍¯subscript𝑃𝑖\alpha^{H}\_{i},\alpha^{Q}\_{i},Z,\bar{P\_{i}}, the simulated state-dependent recovery rates are obtained by
formula (9, 10).

#### 3.3.4 Loss function

By changing scenarios to quiet and hectic states, we assume the exposure of each obligor is 100 million and generate the expected
loss
under the given scenarios corresponding to formula (11).

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(Li|Z)=π​(Z=z)​Gi​(Z|S=H)​Pi​(Z|S=H)+(1−π​(Z=z))​Gi​(Z|S=Q)​Pi​(Z|S=Q)Econditionalsubscript𝐿𝑖𝑍𝜋𝑍𝑧subscript𝐺𝑖conditional𝑍S=Hsubscript𝑃𝑖conditional𝑍S=H1𝜋𝑍𝑧subscript𝐺𝑖conditional𝑍S=Qsubscript𝑃𝑖conditional𝑍S=Q\textsf{E}(L\_{i}|Z)=\pi(Z=z)G\_{i}(Z|\mbox{S=H})P\_{i}(Z|\mbox{S=H})+(1-\pi(Z=z))G\_{i}(Z|\mbox{S=Q})P\_{i}(Z|\mbox{S=Q}) |  | (14) |

Given the simulated Z random variables, conditional probability π​(Z=z)𝜋𝑍𝑧\pi(Z=z) naturally provides better information than unconditional probability ω𝜔\omega does. By the given formula (14), we
compare the theoretical loss amounts across four models with the
realised loss values, and evaluate the performance of the default prediction by the mean of square error.

#### 3.3.5 Absolute error

In step 5, the performance of the competing models: FC, RFC, RR,
RRFC are evaluated here to decide which one is the best in
predicting the default for the following year. Absolute Error (AE)
here is linked to the prediction performance and is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | AE=(actual portfolio loss - expected portfolio loss)AEactual portfolio loss - expected portfolio loss\mbox{AE}=(\mbox{actual portfolio loss - expected portfolio loss}) |  | (15) |

where actual portfolio loss is from Moody’s report.
Expected loss is estimated from equation (14), whereas in an
unconditional default model, it is
computed from formula (5). For each competing model, we generate 1000 scenarios, then, the mean of absolute error referred as MAE is calculated.
One can expect that the best one is entailed on the minimum AE and MAE as well.

## 4 Data

We use the list of default companies for 2008 through to 2009
published by Moody’s annual report since this is a rich available data
source. In total, we obtained 341 defaults with
corporate bond recovery rates from Moody’s URD covering the period
from 1987 to 2007. We focus on senior unsecured bonds because of their wide use in
financial contracts, regulatory rules, and the risk of measuring for
assets under the standardised approach of Basel II (
Pagratis and Stringa, [2009](#bib.bib35)). We also collected the credit rating
of obligors from Moody’s report in order to measure the hazard
rate. Although there are 94 and 247 default firms in 2008 and
2009, the observations were reduced due to missing stock prices and
credit rates of obligors’ bonds. If there was a lack of stock
prices of default subsidiary companies, we used stock prices of
parent companies instead. In all cases, 31 and 62 sampling firms were collected in 2008 and 2009, respectively.

To estimate the conditional factor loadings of sampling firms, we collect the daily USD
S&P 500 return and the respective stock return of the default companies for
a 5-year period prior to the default year from the Datastream
database. USD S&P 500 Index here simply represents the common systematic risk. By assuming a mixture of bivariate normal distribution, we estimate the parameters including factor loadings by EM algorithm. Table 2
presents the results of EM algorithm.

| Model | Probability | Mean | STD |
| --- | --- | --- | --- |
| Period | 2003-2007 |  |  |
| Unconditional (one normal) | 100.00% | 0.03% | 0.77% |
| Conditional on quiet | 58.68% | 0.10% | 0.43% |
| Conditional on hectic | 41.32% | -0.08% | 1.07% |
| Period | 2004-2008 |  |  |
| Unconditional (one normal) | 100.00% | 0.03% | 0.83% |
| Conditional on quiet | 56.77% | 0.10% | 0.38% |
| Conditional on hectic | 43.23% | -0.06% | 1.17% |

Table 2: Estimate mixture of normal distribution by employing
an
EM algorithm
STD represent standard deviation

As presented in Table 2, the volatility of the hectic distribution
is larger than that of the quiet distribution, and the mean of the
hectic distribution is smaller than that of the quiet
distribution, reflecting the fat tails and a skew
to the right which are consistent with
Kim and Finger ([2000](#bib.bib32)).

## 5 Empirical result

### 5.1 Conditional factor loading estimation

Figure 1 and 2 shows that the
majority of correlation coefficients or called factor loadings in factor copula model during the hectic period is
higher than in the quiet period. The proposed correlation structure leads to more accurate and realistic implementations, and to avoid the underestimation of factor loading in a hectic period or the overestimation in a quiet period. These ideas
are well known in statistics and have already been applied to
financial questions ([Ang and Chen](#bib.bib7)
2002b;
Patton, [2004](#bib.bib37)).

![Refer to caption](/html/2009.12092/assets/Fig1_1.png)


Figure 1: Conditional and unconditional factor loading comparision in 2008
The estimation of Conditional and Unconditional Factor Loading between S&P 500 and default companies in 2008.

![Refer to caption](/html/2009.12092/assets/Fig2.png)


Figure 2: Conditional and unconditional factor loading comparision in 2009
The estimation of Conditional and Unconditional Factor Loading between S&P 500 and default companies in 2009.

In our approach, we consider this asymmetric correlation structure under
real market conditions to implement the conditional default model
developed in Section 3.2. As shown in Figure 1 and 2, the factor loadings αisubscript𝛼𝑖\alpha\_{i} in state H are higher than those in state Q. As factor loadings get higher in state H, the correlation coefficient ρi​jsubscript𝜌𝑖𝑗\rho\_{ij} between firm i𝑖i and j𝑗j defined in equation (2) is expected to increase in this market condition. Therefore, obligors tend to comove more
closely during hectic periods than during quiet periods.

### 5.2 State-dependant recovery rate estimation

To demonstrate the impact of market conditions measured by Z on
the state-dependent recovery rate, in Figure 3 we depict the
relationship between the state-dependent recovery rate and the
S&P 500 (the proxy for systematic factor Z) in blue
‘\*’, which developed in section 3.2.
One can observe that the effect of the systematic factor on the
recovery rate is positive, the recovery rate gets higher as Z𝑍Z grows. Since the slope of this curve is
influenced by estimated αiH,αiQ

subscriptsuperscript𝛼𝐻𝑖subscriptsuperscript𝛼𝑄𝑖\alpha^{H}\_{i},\alpha^{Q}\_{i} corresponding to
formula (9, 10), the slopes behave differently in the four panels but keep positive
monotonically. We also depict the stochastic recovery rates in
red ‘+’  estimated and simulated through
Amraoui et al. ([2012](#bib.bib3)) model, in comparison with blue ‘\*’, simulated from our model. Taking (c) E\*TRADE as an example, we observe that compared with the simulated recovery rates based on equation (9) and (10), those generated from Amraoui et al. ([2012](#bib.bib3)), by assuming constant factor loadings, tend to produce higher recovery rates in the market downturn and lower ones in the booming market. This evidence suggests that the recovery rate may be overestimated in a bearish market but underestimated in a bullish market if the constant factor loading is assumed. As a consequence, an underestimation of credit loss in a bearish market but an overestimation in a bullish market are highly possible. Similarly, the evidence from (a) Glitnir
banki (b) Lehman Brothers Holdings, Inc. and (d) Idearc, Inc. are comparable and consistent. Note that the impact of the systematic factor on recovery rate seems nonlinear, it is higher in the market downturn but relatively milder in the booming market, and the marginal slope decreases abruptly when the index return
decreases, whereas the marginal slope decelerates when the index
return becomes positive. This simulation result is in accordance with Moody’s
report in Table 1. From 2004 to 2006, the annual recovery rate of
senior unsecured bond increases slowly. When the crisis started in
August 2007, the recovery rate drops dramatically. By capturing the
correlation structure, αH>αQsuperscript𝛼𝐻superscript𝛼𝑄\alpha^{H}>\alpha^{Q}, as shown in (a), (c)
and (d), we find this asymmetric pattern which is more consistent with
the reality.

Having the simulated recovery rates from equations (9, 10), we are more interested in the relation between it and conditional default probability from equation (8). As can been seen in Figure 4, the simulation result shows
the downward trend between default probability and recovery rate consisted with
Altman et al. ([2005](#bib.bib2)) and
Das and Hanouna ([2009](#bib.bib17)). It shows that the common factor governs the default rate and recovery rate simultaneously and creates their negative association implicitly.
Altman et al. ([2005](#bib.bib2)) find that permitting a
dependence between default rates and recovery rates increases
around 29% in the Value at Risk compared with a model that assumes no
dependence between default rates and recovery rates.

![Refer to caption](/html/2009.12092/assets/Glitnirbanki_2008.png)


a Glitnir banki:
α=0.044,αQ=0.029,αH=0.067formulae-sequence𝛼0.044formulae-sequencesuperscript𝛼𝑄0.029superscript𝛼𝐻0.067\alpha=0.044,\alpha^{Q}=0.029,\alpha^{H}=0.067

![Refer to caption](/html/2009.12092/assets/Lehman3_2008.png)


b Lehman Bro.:
α=0.125,αQ=0.013,αH=0.208formulae-sequence𝛼0.125formulae-sequencesuperscript𝛼𝑄0.013superscript𝛼𝐻0.208\alpha=0.125,\alpha^{Q}=0.013,\alpha^{H}=0.208

![Refer to caption](/html/2009.12092/assets/ETRADE_2009.png)


c E\*TRADE:
α=0.548,αQ=0.172,αH=0.426formulae-sequence𝛼0.548formulae-sequencesuperscript𝛼𝑄0.172superscript𝛼𝐻0.426\alpha=0.548,\alpha^{Q}=0.172,\alpha^{H}=0.426

![Refer to caption](/html/2009.12092/assets/Idearc_2009.png)


d Idearc, Inc.:
α=0.237,αQ=0.028,αH=0.356formulae-sequence𝛼0.237formulae-sequencesuperscript𝛼𝑄0.028superscript𝛼𝐻0.356\alpha=0.237,\alpha^{Q}=0.028,\alpha^{H}=0.356

Figure 4: The relationship between state-dependent recovery rate and index return of S&P 500,
Z𝑍Z.
Panel (a) and (b), ‘\*’  in blue illustrates the pattern of state-dependent recovery rate of Glitnir banki and Lehman Brothers Holdings,
Inc. which incorporate conditional factor loading in 2008. ‘+’  in red plots the recoveries proposed by Amraoui et al. ([2012](#bib.bib3)). In
panel (c) and (d), E\*TRADE Financial Corp. and Idearc, Inc. in 2009.




(a) 2008

(b) 2009

Figure 5: The relationship between state-dependent recovery rates and default
probabilities
By simulating Z∼N​(−0.03,3.05)similar-to𝑍N0.033.05Z\sim\textsf{N}(-0.03,3.05), it plots the relationship between the state-dependent recovery rate and default probabilities, given the conditional factor
loading. By simulating 1000 observations, we estimate
the default probabilities and state-dependent recovery rate from formula (8) and (9,10).

### 5.3 Empirical results of absolute errors

To gauge the conditional factor loading and state-dependent
recovery rate approaches for default prediction, we propose four
models: (1) The FC model: the
standard one-factor Gaussian copula model with the constant
recovery rate developed by Van der Voort ([2007](#bib.bib45)) and Rosen and Saunders ([2010](#bib.bib40)) (2) The RFL model: the
one-factor Gaussian copula model with the factor loadings tied to
the state of common factor and the recoveries being assumed as constant proposed by Kalemanova et al. ([2007](#bib.bib30)) and Chen et al. ([2014](#bib.bib12)). (3) The RR model:
standard one-factor Gaussian copula model but the recoveries being
related to the state of the macroeconomic state (Amraoui and Hitier, [2008](#bib.bib4);
Elouerkhaoui, [2009](#bib.bib19); Amraoui et al., [2012](#bib.bib3)), and (4) The RRFL
model: a conditional factor
loading specification together with a state-dependent recovery rate. We address the question of whether the two specifications,
conditional factor loading and the state-dependent recovery rate model
are meaningful and significant in explaining the gap between expected and
practical loss value. In order to check the predictive ability of the different
models, we report the AE and MAE estimated
from section 3.3.5.

Table 3 reports the AE between actual portfolio loss and expected
portfolio loss constructed by 31 and 62 observations in 2008 and 2009,
respectively. In a comparison with
four models, one can observe that the estimate of expected portfolio loss in
the RRFL model is highest and closest to the corresponding actual one, which means the expected portfolio losses
may be underestimated by the other three models. Especially, a modelling recovery rate in a stochastic fashion indeed contributes to credit loss estimation.

We compare the four competing models of each obligor and choose
the best model which achieves the minimum AE and MAE. It can be seen that
including the conditional factor loading (RFL model) instead of the Spearman
correlation (FC model) does not significantly improve the estimations in 2008 and 2009. As can be seen in Table 4, we find that introducing
the state-dependent recovery rate (RR model) leads to a promising improvement
over the standard model (FC model). We interpret this as saying that the setting of stochastic recovery rate seems necessary, which brings a remarkable improvement on default prediction. This result is consistent with Altman et al. ([2005](#bib.bib2)) and Ferreira and Laux ([2007](#bib.bib20)). Compared with the RR model, the RRFL model
includes conditional factor loading in default probabilities and
a state-dependent recovery rates function which produces much more
modest improvements.

We propose two specifications on factor loading, and recovery rates across four models. If we assume that default probabilities are
the function of two-state correlation constructers, but recovery
rates do not, the specification is only identified concentrated on factor loading. In this case, the recovery rates do not
contain information about the state of business cycle. Conversely, if
we assume that recovery rates vary, but factor loading is fixed, then the refinement is only through the
variation in the recovery rate. Since the RRFL model with both specifications is superior to the
other three competing models, there is no redundant specification in this study. In this regard, we extend the models proposed by prior literatures (Van der Voort, [2007](#bib.bib45); Rosen and Saunders, [2010](#bib.bib40); Kalemanova et al., [2007](#bib.bib30); Chen et al., [2014](#bib.bib12); Amraoui and Hitier, [2008](#bib.bib4);
Elouerkhaoui, [2009](#bib.bib19); Amraoui et al., [2012](#bib.bib3)) which leads more accurate default prediction in one year.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | FC | RFL | RR | RRFL |  |
| 2008 |  |  |  |  |  |
| Actual portfolio loss | 2035.02 | 2035.02 | 2035.02 | 2035.02 |  |
| Expected portfolio loss | 509.60 | 527.06 | 687.01 | 690.86 |  |
| AE | 1525.42 | 1507.96 | 1348.01 | 1344.16 |  |
| MAE | 47.12 | 47.67 | 42.13 | 42.01 |  |
| Expected portfolio loss/Actual portfolio loss | 25.04% | 25.90% | 33.76% | 33.95% |  |
| 2009 |  |  |  |  |  |
| Actual portfolio loss | 4073.80 | 4073.80 | 4073.80 | 4073.80 |  |
| Expected portfolio loss | 1203.56 | 1212.38 | 1769.14 | 1788.05 |  |
| AE | 2870.24 | 2861.42 | 2304.67 | 2285.75 |  |
| MAE | 43.49 | 43.35 | 34.92 | 34.63 |  |
| Expected portfolio loss/Actual portfolio loss | 29.54% | 29.76% | 43.43% | 43.89% |  |

Table 3: The mean of actual portfolio loss, expected portfolio loss and AE, MAE (in million)
This table reports the
AE and MAE by comparing the four models: (1) The FC model: the
standard one-factor Gaussian copula model with the constant
recovery rate. (2) The RFL model: the
one-factor Gaussian copula model with the factor loadings tied to
the state of common factor and the recoveries being assumed to be constant. (3) The RR model:
standard one-factor Gaussian copula model but the recoveries being
related to the state of the macroeconomic state. and (4)The RRFL
model: a conditional factor
loading specification together with a state-dependent recovery rate. This table also presents the difference between actual portfolio loss and expected portfolio loss as referred to AE, and divided by 31 and 62 observations in 2008 and 2009, respectively, as MAE. The percentage represents expected portfolio loss divided by the actual portfolio loss.

### 5.4 Basel III: Relative contribution

Since Basel III is proposed to control systematic risk (one of systemic risk measures) to
achieve the goal of overall financial stability, systematic risk
has been considered one of the main causes of the 2007-2009 crisis.
In this section, we highlight the role of systematic risk and its
impact to fit the
goals of Basel III. The aim of relative contribution analysis is to
investigate the proportional contribution from systematic risk in
comparison to that from the idiosyncratic component. By measuring
the systematic risk, αiS​Zsuperscriptsubscript𝛼𝑖𝑆𝑍\alpha\_{i}^{S}Z, and idiosyncratic risk,
1−(αiS)2​εi1superscriptsubscriptsuperscript𝛼𝑆𝑖2subscript𝜀𝑖\sqrt{1-(\alpha^{S}\_{i})^{2}}\varepsilon\_{i},
S∈{H,Q}SH,Q\mbox{S}\in\{\mbox{H,Q}\} from formula (6,7), we depict a
scatter plot for simulated systematic risk (horizontal axis) and
idiosyncratic risk (vertical axis) in Figure 5. As can be seen in the 2D plot in 2008, the 45∘superscript4545^{\circ} line represents the proportion of systematic risk is equal to that of idiosyncratic risk. If scattered
points are located in the ‘A, B, C, D’  zones, the contribution of
systematic risk on default risk is greater than idiosyncratic risk. On the other hand, if scattered points are settled in the ‘a, b, c, d’  areas, the contribution of
systematic component is less than idiosyncratic risk. For example, the effect of systematic risk on default risk will become larger when point ‘Y’  moves to point ‘X’. Most literature focus on
either systematic ( Huang et al., [2009](#bib.bib24);
 Acharya et al., [2010](#bib.bib1)) or firm-specific
components ( Goyal and Santa-Clara, [2003](#bib.bib23);
Ferreira and Laux, [2007](#bib.bib20)), and a limit number of studies compare the influence of both of them.

By simulating Z∼N​(−0.03,3.05)similar-to𝑍N0.033.05Z\sim\textsf{N}(-0.03,3.05), each simulated Z random variable can therefore be mapped into a specific conditional probability of being hectic state in Eq. (12). We depict the scatters in three groups here. The first group (marked as ‘+’  in green) only includes the simulated Z r.v. with projecting conditional probabilities above 75%percent7575\%-quartile, and indicates that they are generated in distress. The second group (marked as ‘\*’  in blue) includes the Z r.v. with projecting conditional probabilities below 25%percent2525\%-quartile to indicate that they are generated in a bullish atmosphere. The third group (marked as ‘x’  in red) collects the rest. With regards to the tranquil
scenarios (‘blue ’  points) in 2008, most observations were located in the area where
the relative contribution of idiosyncratic risk is larger than the
economy-wide component, that the credit risk was mainly
driven by the idiosyncratic component before the subprime crisis as reported in the Rodríguez-Moreno and Peña ([2013](#bib.bib39)) article. In their article, they
find that idiosyncratic components are larger than systematic risk
before the subprime crisis, extracted from the CDX-IG-5y by using
high-frequent measures. At the beginning of the financial crisis,
systematic risk skyrocketed. Intuitively, the systematic risk increases sharply due to the larger factor loadings when the market is in hectic scenarios. Our result shows systematic risk is
higher than the idiosyncratic component in the hectic scenarios (‘green ’ points) in 2008; in
the quiet scenarios, firm-specific factors, however, are mostly important at some
points, as proposed by
Rodríguez-Moreno and Peña ([2013](#bib.bib39)). Similarly, it has
been shown that the relative contribution of the systematic component
explains a higher proportion of obligor asset value in 2009.

More visibly, the 3D plot identifies the relationship among the
level of average Ui|Sevaluated-atsubscript𝑈𝑖SU\_{i}|\_{\mbox{S}} referred to as the mean of firms’ value,
systematic and idiosyncratic component. Each observation in Figure
4 reflects its mean of Ui|Sevaluated-atsubscript𝑈𝑖SU\_{i}|\_{\mbox{S}} i=1,…,N𝑖

1…𝑁i=1,\ldots,N in each simulating
day in 2008 and 2009, respectively. As can be seen in Figure 5, the
points in the hectic period marked as green circles indicates a
negative shock from systematic risk which lowers the average asset
value of obligors; specifically, the majority of observations show
a negative impact of systematic shock which accounts for a larger
proportion on the firms’ values substantially. Note that it is easy to drive the default event since it lowers
the firms’ value significantly. On the
other hand, the points in quiet days marked as blue circles
indicate a positive shock from the systematic component. However,
the negative shock from firm-specific factors
may compromise the benefit from economy-wide components that lowers the
level of average Ui|Sevaluated-atsubscript𝑈𝑖SU\_{i}|\_{\mbox{S}} at some points.

Our model emphasises the importance of systematic risk which
explains most obligors default behaviour particular in hectic
periods, which is one of the important measures of Basel III
( Schwerter, [2011](#bib.bib42);  Uhde and Michalak, [2010](#bib.bib44);  Tarashev et al., [2010](#bib.bib43)). To be specific, we measure and
demonstrate the contribution of overall systematic risk to each
asset, and identify the impact direction from systematic and idiosyncratic
risk. Moreover, it can be applied to a variety of systematic risk
measures. In this sense, portfolio managers should be aware of the
systematic risk which influences the value of portfolios
substantially. We propose that the regulatory tool of Basel III
could be estimated according to such
contributions. A related question is how these measures can aid policymakers. The
measures in this paper can be used as a tool to prevent systematic
crisis. Our model can be used as an early warning system that will
alert the regulators when an individual bank is in trouble and to intervene before the crisis happens.

![Refer to caption](/html/2009.12092/assets/2008_2D_20150704.png)

![Refer to caption](/html/2009.12092/assets/2008_3D_20150704.png)

(a) 2008

![Refer to caption](/html/2009.12092/assets/2009_2D_20150704.png)

![Refer to caption](/html/2009.12092/assets/2009_3D_20150704.png)

(b) 2009

Figure 7: The 2D and 3D scatters plot of relative
contribution
By simulating Z∼N​(−0.03,3.05)similar-to𝑍N0.033.05Z\sim\textsf{N}(-0.03,3.05), the 2D graphic illustrates the relationship between the mean of systematic risk, αi​Zsubscript𝛼𝑖𝑍\alpha\_{i}Z, and idiosyncratic risk, 1−αi2​εi1superscriptsubscript𝛼𝑖2subscript𝜀𝑖\sqrt{1-\alpha\_{i}^{2}}\varepsilon\_{i}. Each simulated Z random variable can therefore be mapped into a specific conditional probability of being hectic state in Eq. (12). We depict the scatters in three groups here. The first group (marked as ‘+’  in green) only includes the simulated Z r.v. with projecting conditional probabilities above 75%percent7575\%-quartile, and indicates that they are generated in distress. The second group (marked as ‘\*’  in blue) includes the Z r.v. with projecting conditional probabilities below 25%percent2525\%-quartile to indicate that they are generated in a bullish atmosphere. The third group (marked as ‘x’  in red) collects the rest. In 3D plot, observations
in hectic periods are marked as green circles. In quiet
days are marked as blue circles, otherwise as red
circles.

### 5.5 Robustness test

Since Table 3 reports that the expected portfolio loss is far away from the actual portfolio loss, we gauge that using bond credit rates as a measure of hazard rate has the disadvantage that they are released annually by Moody’s report. In this section, we use credit default swap (CDS) spread data as an alternative market-based measure of the company’s credit risk. A CDS spread is a financial swap agreement that the seller of CDS will compensate the buyer in the event of a loan default. Basically, the variation of CDS spread reflects the dynamic of risk condition or hazard rate implicitly. The larger the CDS spread is, the riskier the debtor is. Therefore, the hazard rate, κ¯¯𝜅\bar{\kappa}, for a company can be estimated by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ¯=s1−R¯𝜅𝑠1𝑅\bar{\kappa}=\frac{s}{1-R} |  | (16) |

where s𝑠s is CDS spread. We consider the latest one-year CDS quotes of obligors before the default year provided from Datastream. We also use a credit spread which is the yield on a annual par yield bond issued by the obligors over one-year LIBOR (London Interbank Offered Rate) if the obligor doesn’t have CDS data. Theoretically, the CDS spread is very close to the credit spread ( Hull and White, [2000](#bib.bib27);  Hull et al., [2004](#bib.bib25)). By plugging in the recovery rate, R𝑅R, obtained from Moody’s report, we compute the
average default intensity, κ¯¯𝜅\bar{\kappa}, per year conditional on no earlier
default instead of Pisubscript𝑃𝑖P\_{i}. Compared with Pisubscript𝑃𝑖P\_{i} from Moody’s annual report, a CDS spread with active trading activity reflects
market assessments of default risk in a timely fashion. In this regard, the proposed models with an incorporation of the hazard rate implied in CDS spreads may produce a better prediction.

According to Table 4, the models with a hazard rate implied in a CDS
spread seem to perform better than those with a hazard rate from historical
bond credit rates. By comparing Tables 3 and 4, generally, a CDS spread as the hazard rate measure reflects information more timely than the bond credit rate does. As can be seen in Table 4, the RRFL model outperforms in robustness test. In both Tables, the RRFL model consistently outperforms, which produces the expected portfolio loss most closely to the actual portfolio loss.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | FC | RFL | RR | RRFL |  |
| 2008 |  |  |  |  |  |
| Actual portfolio loss | 1401.31 | 1401.31 | 1401.31 | 1401.31 |  |
| Expected portfolio loss | 560.50 | 533.82 | 589.54 | 591.40 |  |
| AE | 840.81 | 867.49 | 811.77 | 809.91 |  |
| MAE | 35.03 | 36.15 | 33.82 | 33.75 |  |
| Expected portfolio loss/Actual portfolio loss | 40.00% | 38.09% | 42.07% | 42.20% |  |
| 2009 |  |  |  |  |  |
| Actual portfolio loss | 2707.30 | 2707.30 | 2707.30 | 2707.30 |  |
| Expected portfolio loss | 1457.07 | 1462.18 | 1677.89 | 1683.97 |  |
| AE | 1250.23 | 1245.12 | 1029.42 | 1023.33 |  |
| MAE | 29.77 | 29.65 | 24.51 | 24.37 |  |
| Expected portfolio loss/Actual portfolio loss | 53.82% | 54.01% | 61.98% | 62.20% |  |

Table 4: The actual portfolio loss, expected portfolio loss, AE, and MAE (in million) for robustness
This table reports the value of AE and MAE of four models by using market-based method during 2008 and 2009. This table also shows the actual portfolio loss and expected portfolio loss of 24 and 42 observations in 2008 and 2009. The percentage represents expected portfolio loss divided by the actual portfolio loss.

## 6 Conclusion

This paper proposes a refined factor copula model for credit
risk prediction. On the basis of our estimated model, we find that
systematic risk plays a critical role in governing default
rates and recovery rates simultaneously. Our simulation results
show that recoveries vary with the returns of the S&P 500 and the
impact of systematic factors on the recovery rate is asymmetric by characterising a higher factor loading in hectic periods than in tranquil ones. Among the various factor copula models developed in the past and current literature as the competing models, the one with conditional random factor loading and a state-dependent recovery rate turns out to be the most superior. In other words, our refined model contributes to literature that have been mapped to 3 groups of competing models (the FC, RFL, and RR models)

As a response to Basel III, we measure and demonstrate the
contribution of overall systematic risk to each firm’s value and
identify the relative role of the systematic and idiosyncratic risk.
Moreover, it can be applied to a variety of systematic risk
measures, and aids regulators in preventing a systematic crisis. In
addition, by investigating the effect of state-dependent recovery
rates on the loss function, we suggest that banks should apply this issue on capital requirement to make sure of its sufficiency.

In further research, we plan to go beyond this study in several ways. For instance, other copula functions can be modelled to capture various dependence structures. Secondly, the marginal distribution can be considered in a more general way to capture a fat-tail feature. We will leave these issues for future studies.

## Acknowledgements

This research was financially
supported by the Deutsche Forschungsgemeinschaft (DFG) via SFB 649
”Ökonomisches Risiko” and IRTG 1792 ”High-Dimensional
Non-Stationary Times Series” is gratefully acknowledged.

## Appendix A Conditional Factor Loading

We assume the two asset returns Z𝑍Z (USD S&P 500), Uisubscript𝑈𝑖U\_{i} (firm
stock price) to have a mixture of bivariate normal distribution:
(Z,Ui)∼similar-to𝑍subscript𝑈𝑖absent(Z,U\_{i})\sim

|  |  |  |  |
| --- | --- | --- | --- |
|  | {N​{[μZQμiQ],[(σZQ)2(σZQ)​(αQ)​(σiQ)(σZQ)​(αQ)​(σiQ)(σiQ)2]}P⁡(S=Q)=1−ωN​{[μZHμiH],[(σZH)2(σZH)​(αH)​(σiH)(σZH)​(αH)​(σiH)(σiH)2]}P⁡(S=H)=ωcases𝑁delimited-[]subscriptsuperscript𝜇𝑄𝑍subscriptsuperscript𝜇𝑄𝑖delimited-[]superscriptsubscriptsuperscript𝜎𝑄𝑍2subscriptsuperscript𝜎𝑄𝑍superscript𝛼𝑄subscriptsuperscript𝜎𝑄𝑖subscriptsuperscript𝜎𝑄𝑍superscript𝛼𝑄subscriptsuperscript𝜎𝑄𝑖superscriptsubscriptsuperscript𝜎𝑄𝑖2PS=Q1𝜔𝑁delimited-[]subscriptsuperscript𝜇𝐻𝑍subscriptsuperscript𝜇𝐻𝑖delimited-[]superscriptsubscriptsuperscript𝜎𝐻𝑍2subscriptsuperscript𝜎𝐻𝑍superscript𝛼𝐻subscriptsuperscript𝜎𝐻𝑖subscriptsuperscript𝜎𝐻𝑍superscript𝛼𝐻subscriptsuperscript𝜎𝐻𝑖superscriptsubscriptsuperscript𝜎𝐻𝑖2PS=H𝜔\left\{\begin{array}[]{cc}N\left\{\begin{array}[]{cc}\left[\begin{array}[]{c}\mu^{Q}\_{Z}\\ \mu^{Q}\_{i}\end{array}\right],&\left[\begin{array}[]{cc}(\sigma^{Q}\_{Z})^{2}&(\sigma^{Q}\_{Z})(\alpha^{Q})(\sigma^{Q}\_{i})\\ (\sigma^{Q}\_{Z})(\alpha^{Q})(\sigma^{Q}\_{i})&(\sigma^{Q}\_{i})^{2}\end{array}\right]\end{array}\right\}&\operatorname{P}(\mbox{S=Q})=1-\omega\\ N\left\{\begin{array}[]{cc}\left[\begin{array}[]{c}\mu^{H}\_{Z}\\ \mu^{H}\_{i}\end{array}\right],&\left[\begin{array}[]{cc}(\sigma^{H}\_{Z})^{2}&(\sigma^{H}\_{Z})(\alpha^{H})(\sigma^{H}\_{i})\\ (\sigma^{H}\_{Z})(\alpha^{H})(\sigma^{H}\_{i})&(\sigma^{H}\_{i})^{2}\end{array}\right]\end{array}\right\}&\operatorname{P}(\mbox{S=H})=\omega\end{array}\right. |  | (A.1) |

where volatility in hectic periods is higher than in a
quiet periods, (σiH)2>(σiQ)2superscriptsubscriptsuperscript𝜎𝐻𝑖2superscriptsubscriptsuperscript𝜎𝑄𝑖2(\sigma^{H}\_{i})^{2}>(\sigma^{Q}\_{i})^{2}. αQsuperscript𝛼𝑄\alpha^{Q} and αHsuperscript𝛼𝐻\alpha^{H} are the correlation coefficient between each obligor and the S&P 500 in quiet and hectic period proposed by Kim and Finger ([2000](#bib.bib32)), respectively.
We estimate the unknown parameters ω𝜔\omega, μZQsubscriptsuperscript𝜇𝑄𝑍\mu^{Q}\_{Z}, σZQsubscriptsuperscript𝜎𝑄𝑍\sigma^{Q}\_{Z}, μZHsubscriptsuperscript𝜇𝐻𝑍\mu^{H}\_{Z}, σZHsubscriptsuperscript𝜎𝐻𝑍\sigma^{H}\_{Z} from the marginal
distribution of Z𝑍Z:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {N​[μZQ,(σZQ)2]P⁡(S=Q)=1−ωN​[μZH,(σZH)2]P⁡(S=H)=ωcases𝑁delimited-[]subscriptsuperscript𝜇𝑄𝑍superscriptsubscriptsuperscript𝜎𝑄𝑍2PS=Q1𝜔𝑁delimited-[]subscriptsuperscript𝜇𝐻𝑍superscriptsubscriptsuperscript𝜎𝐻𝑍2PS=H𝜔\left\{\begin{array}[]{cc}N\left[\begin{array}[]{cc}\mu^{Q}\_{Z},&(\sigma^{Q}\_{Z})^{2}\end{array}\right]&\operatorname{P}(\mbox{S=Q})=1-\omega\\ N\left[\begin{array}[]{cc}\mu^{H}\_{Z},&(\sigma^{H}\_{Z})^{2}\end{array}\right]&\operatorname{P}(\mbox{S=H})=\omega\end{array}\right. |  | (A.2) |

## References

* Acharya et al. (2010)

  Acharya, V.V., Pedersen, L.H.,
  Philippon, T., Richardson, M.P.,
  2010.
  Measuring systemic risk .
* Altman et al. (2005)

  Altman, E.I., Brady, B.,
  Resti, A., Sironi, A.,
  2005.
  The link between default and recovery rates: Theory,
  empirical evidence, and implications\*.
  The Journal of Business 78,
  2203–2228.
* Amraoui et al. (2012)

  Amraoui, S., Cousot, L.,
  Hitier, S., Laurent, J.P.,
  2012.
  Pricing CDOs with state-dependent stochastic
  recovery rates.
  Quantitative Finance 12,
  1219–1240.
* Amraoui and Hitier (2008)

  Amraoui, S., Hitier, S.,
  2008.
  Optimal stochastic recovery for base correlation.
  BNP Paribas .
* Andersen and Sidenius (2004)

  Andersen, L.B., Sidenius, J.,
  2004.
  Extensions to the gaussian copula: Random recovery
  and random factor loadings.
  Journal of Credit Risk 1,
  29–70.
* Ang and Bekaert (2002a)

  Ang, A., Bekaert, G.,
  2002a.
  International asset allocation with regime shifts.
  Review of Financial studies 15,
  1137–1187.
* Ang and Chen (2002b)

  Ang, A., Chen, J., 2002b.
  Asymmetric correlations of equity portfolios.
  Journal of Financial Economics
  63, 443–494.
* Bonti et al. (2006)

  Bonti, G., Kalkbrener, M.,
  Lotz, C., Stahl, G.,
  2006.
  Credit risk concentrations under stress.
  Journal of Credit Risk 2,
  115–136.
* Bruche and Gonzalez-Aguado (2010)

  Bruche, M., Gonzalez-Aguado, C.,
  2010.
  Recovery rates, default probabilities, and the credit
  cycle.
  Journal of Banking & Finance
  34, 754–764.
* Carty et al. (1998)

  Carty, L.V., Hamilton, D.T.,
  Keenan, S.C., Moss, A.,
  Mulvaney, M., Marshella, T.,
  Subhas, M., 1998.
  Bankrupt bank loan recoveries.
  Moody’s investors service 15,
  79.
* Chen (2010)

  Chen, H., 2010.
  Macroeconomic conditions and the puzzles of credit
  spreads and capital structure.
  The Journal of Finance 65,
  2171–2212.
* Chen et al. (2014)

  Chen, J., Liu, Z., Li,
  S., 2014.
  Mixed copula model with stochastic correlation for
  cdo pricing.
  Economic Modelling 40,
  167–174.
* Choroś-Tomczyk et al. (2013)

  Choroś-Tomczyk, B., Härdle, W.K.,
  Okhrin, O., 2013.
  Valuation of collateralized debt obligations with
  hierarchical archimedean copulae.
  Journal of Empirical Finance 24,
  42–62.
* Choroś-Tomczyk et al. (2014)

  Choroś-Tomczyk, B., Härdle, W.K.,
  Overbeck, L., 2014.
  Copula dynamics in CDOs.
  Quantitative Finance 14,
  1573–1585.
* Committee et al. (2009)

  Committee, B., et al., 2009.
  Strengthening the resilience of the banking sector.
  Basel Committee .
* Crouhy et al. (2000)

  Crouhy, M., Galai, D.,
  Mark, R., 2000.
  A comparative analysis of current credit risk
  models.
  Journal of Banking & Finance
  24, 59–117.
* Das and Hanouna (2009)

  Das, S.R., Hanouna, P.,
  2009.
  Hedging credit: Equity liquidity matters.
  Journal of Financial Intermediation
  18, 112–123.
* Drehmann and Tarashev (2013)

  Drehmann, M., Tarashev, N.,
  2013.
  Measuring the systemic importance of interconnected
  banks.
  Journal of Financial Intermediation
  22, 586–607.
* Elouerkhaoui (2009)

  Elouerkhaoui, Y., 2009.
  Base correlation calibration with a stochastic
  recovery model.
  Technical Report. working paper, Citigroup Global
  Markets.
* Ferreira and Laux (2007)

  Ferreira, M.A., Laux, P.A.,
  2007.
  Corporate governance, idiosyncratic risk, and
  information flow.
  The Journal of Finance 62,
  951–989.
* Franke et al. (2015)

  Franke, J., Härdle, W.K.,
  Hafner, C.M., 2015.
  Statistics of financial markets: an introduction.
  Springer Science & Business Media.
* Frey and McNeil (2003)

  Frey, R., McNeil, A.J.,
  2003.
  Dependent defaults in models of portfolio credit
  risk.
  Journal of Risk 6,
  59–92.
* Goyal and Santa-Clara (2003)

  Goyal, A., Santa-Clara, P.,
  2003.
  Idiosyncratic risk matters!
  The Journal of Finance 58,
  975–1008.
* Huang et al. (2009)

  Huang, X., Zhou, H., Zhu,
  H., 2009.
  A framework for assessing the systemic risk of major
  financial institutions.
  Journal of Banking & Finance
  33, 2036–2049.
* Hull et al. (2004)

  Hull, J., Nelken, I.,
  White, A., 2004.
  Merton’s model, credit risk, and volatility skews.
  Journal of Credit Risk Volume 1,
  03–27.
* Hull (2006)

  Hull, J.C., 2006.
  Options, futures, and other derivatives.
  Pearson Education India.
* Hull and White (2000)

  Hull, J.C., White, A.,
  2000.
  Valuing credit default swaps i: No counterparty
  default risk .
* Hull and White (2004)

  Hull, J.C., White, A.D.,
  2004.
  Valuation of a CDO and an n𝑛n-th to default CDS
  without monte carlo simulation.
  The Journal of Derivatives 12,
  8–23.
* Jarrow et al. (1997)

  Jarrow, R.A., Lando, D.,
  Turnbull, S.M., 1997.
  A markov model for the term structure of credit risk
  spreads.
  Review of financial studies 10,
  481–523.
* Kalemanova et al. (2007)

  Kalemanova, A., Schmid, B.,
  Werner, R., 2007.
  The normal inverse gaussian distribution for
  synthetic CDO pricing.
  The Journal of Derivatives 14,
  80–94.
* Khieu et al. (2012)

  Khieu, H.D., Mullineaux, D.J.,
  Yi, H.C., 2012.
  The determinants of bank loan recovery rates.
  Journal of Banking & Finance
  36, 923–933.
* Kim and Finger (2000)

  Kim, J., Finger, C.C.,
  2000.
  A stress test to incorporate correlation breakdown.
  Journal of Risk 2,
  5–20.
* Longin and Solnik (2001)

  Longin, F., Solnik, B.,
  2001.
  Extreme correlation of international equity markets.
  The Journal of Finance 56,
  649–676.
* Merton (1974)

  Merton, R.C., 1974.
  On the pricing of corporate debt: The risk structure
  of interest rates\*.
  The Journal of Finance 29,
  449–470.
* Pagratis and Stringa (2009)

  Pagratis, S., Stringa, M.,
  2009.
  Modeling bank senior unsecured ratings: a reasoned
  structured approach to bank credit assessment.
  International Journal of Central Banking
  5, 1–39.
* Pan and Singleton (2008)

  Pan, J., Singleton, K.J.,
  2008.
  Default and recovery implicit in the term structure
  of sovereign CDS spreads.
  The Journal of Finance 63,
  2345–2384.
* Patton (2004)

  Patton, A.J., 2004.
  On the out-of-sample importance of skewness and
  asymmetric dependence for asset allocation.
  Journal of Financial Econometrics
  2, 130–168.
* Pykhtin and Dev (2002)

  Pykhtin, M., Dev, A., 2002.
  Credit risk in asset securitizations: Analytical
  model.
  Risk 15,
  S16–S20.
* Rodríguez-Moreno and Peña (2013)

  Rodríguez-Moreno, M., Peña, J.I.,
  2013.
  Systemic risk measures: The simpler the better?
  Journal of Banking & Finance
  37, 1817–1831.
* Rosen and Saunders (2010)

  Rosen, D., Saunders, D.,
  2010.
  Risk factor contributions in portfolio credit risk
  models.
  Journal of Banking & Finance
  34, 336–349.
* Schönbucher (2001)

  Schönbucher, P.J., 2001.
  Factor models: Portfolio credit risks when defaults
  are correlated.
  The Journal of Risk Finance 3,
  45–56.
* Schwerter (2011)

  Schwerter, S., 2011.
  Basel iii’s ability to mitigate systemic risk.
  Journal of financial regulation and compliance
  19, 337–354.
* Tarashev et al. (2010)

  Tarashev, N.A., Borio, C.E.,
  Tsatsaronis, K., 2010.
  Attributing systemic risk to individual institutions
  .
* Uhde and Michalak (2010)

  Uhde, A., Michalak, T.C.,
  2010.
  Securitization and systematic risk in european
  banking: Empirical evidence.
  Journal of Banking & Finance
  34, 3061–3077.
* Van der Voort (2007)

  Van der Voort, M., 2007.
  Factor copulas: External defaults.
  The Journal of Derivatives 14,
  94–102.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2009.12092)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2009.12092)
[View original  
on arXiv](https://arxiv.org/abs/2009.12092)[►](javascript: void(0))