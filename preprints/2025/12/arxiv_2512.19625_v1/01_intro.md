---
authors:
- Jherek Healy
doc_id: arxiv:2512.19625v1
family_id: arxiv:2512.19625
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2512.19625v1
url_html: https://arxiv.org/html/2512.19625v1
venue: arXiv q-fin
version: 1
year: 2025
---

###### Abstract

This follow-up article analyzes the impact of foreign exchange option interpolation on the vanilla option implied volatilities. In particular different exact interpolations of broker quotes may lead to different implied volatilities at the 10Δ\Delta and 25Δ\Delta Puts and Calls.

###### keywords:

fx options; volatility; arbitrage; interpolation

\pubvolume\issuenum

1
\articlenumber1
\history
\TitleCounterexamples for FX Options Interpolations - Part II
\AuthorJherek Healy
\AuthorNamesJherek Healy

## 1 Introduction

Market prices of Foreign exchange (FX) options are typically quoted as a sparse set volatilities per option maturity.
Those correspond to the volatilities of an at-the-money (ATM) option, 25Δ\Delta and 10Δ\Delta risk-reversals and butterflies.
Depending on the currency pair and the maturity, there is much variation in what ATM exactly means: is it at the money straddle? with or without premium? spot or forward ? There are also two conventions for the risk-reversal (RR) and butterfly (BF): the simple smile convention where

|  |  |  |  |
| --- | --- | --- | --- |
|  | σcall=σATM+σBF+12​σRR,σput=σATM+σBF−12​σRR,\displaystyle\sigma\_{\textmd{call}}=\sigma\_{\textmd{ATM}}+\sigma\_{\textmd{BF}}+\frac{1}{2}\sigma\_{\textmd{RR}}\,,\quad\sigma\_{\textmd{put}}=\sigma\_{\textmd{ATM}}+\sigma\_{\textmd{BF}}-\frac{1}{2}\sigma\_{\textmd{RR}}\,, |  | (1) |

and the more involved broker convention which requires a numerical solver. In this article, we focus on the latter.

In the broker convention, the ATM quote stays simple. Latin America currency pairs use the ATM forward convention where the vanilla ATM strike KK is such that K=F​(0,T)K=F(0,T) where F​(0,T)F(0,T) is the forward to maturity (e.g. USD/BRL, USD/MXN). For other currency pairs, pips or percent Δ\Delta may be used. The choice depends on the general convention (also applicable to the other option quotes beside ATM) of the currency pair and is based on the strike of a delta neutral straddle. If the premium currency is the same as the primary currency, the convention is to use a percentage111Also known as Δ\Delta with premium. Δ\Delta (e.g. EUR/CHF, EUR/TRY), and otherwise the pips Δ\Delta (e.g. EUR/USD, AUD/USD). When the convention is different from the ATM forward convention, the percentage or pips spot Δ\Delta may222This is not always true, since the 2008 crisis and the associated low levels of liquidity in short-term interest rate products, forward Δ\Delta tends to be also used. be used for maturities up to and including one year when the currency pair only contains currencies from OECD economies (e.g. USD, EUR, JPY, GBP, AUD, NZD, CAD, CHF, NOK, SEK, DKK). For all other cases, the pips or percentage forward Δ\Delta is used. Those read

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔF,pips=η​Φ​(η​d1​(K,σ)),ΔF,pct=KF​(0,T)​η​Φ​(η​d2​(K,σ)),\Delta\_{F,\textmd{pips}}=\eta\Phi(\eta d\_{1}(K,\sigma))\,,\quad\Delta\_{F,\textmd{pct}}=\frac{K}{F(0,T)}\eta\Phi(\eta d\_{2}(K,\sigma))\,, |  | (2) |

where d1​(K,σ)=1σ​T​ln⁡F​(0,T)K+12​σ​Td\_{1}(K,\sigma)=\frac{1}{\sigma\sqrt{T}}\ln\frac{F(0,T)}{K}+\frac{1}{2}\sigma\sqrt{T}, d2=d1−σ​Td\_{2}=d\_{1}-\sigma\sqrt{T} and η=±1\eta=\pm 1 for respectively a call and a put option. We refer the reader to clark2011foreign; reiswich2012fx for exhaustive (but key) details on the various conventions.

The delta neutral straddle strike is determined by the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(1,K,T,σATM)+Δ​(−1,K,T,σATM)=0.\Delta(1,K,T,\sigma\_{\textmd{ATM}})+\Delta(-1,K,T,\sigma\_{\textmd{ATM}})=0\,. |  | (3) |

The strike is independent of the spot or forward delta convention as the discounting term will factor out. Equation [3](https://arxiv.org/html/2512.19625v1#S1.E3 "In 1 Introduction") leads to explicit solutions for the ATM delta neutral strike price:

|  |  |  |  |
| --- | --- | --- | --- |
|  | KDNS,pips=F​(0,T)​e12​σATM2​T,KDNS,pct=F​(0,T)​e−12​σATM2​T,K\_{\textmd{DNS},\textmd{pips}}=F(0,T)e^{\frac{1}{2}\sigma\_{\textmd{ATM}}^{2}T}\,,\quad K\_{\textmd{DNS},\textmd{pct}}=F(0,T)e^{-\frac{1}{2}\sigma\_{\textmd{ATM}}^{2}T}\,, |  | (4) |

where σATM\sigma\_{\textmd{ATM}} is the given ATM market volatility.

The 10- and 25- Put and Call Δ\Delta are not directly given but implied from the quotes of markets strangles and risk-reversals. The price of a market strangle reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | VMS,x​Δ\displaystyle V\_{\textmd{MS},x\Delta} | =V​(−1,KMS,P,x​Δ,T,σATM+σ¯BF,x​Δ)\displaystyle=V(-1,K\_{\textmd{MS},\textmd{P},x\Delta},T,\sigma\_{\textmd{ATM}}+\bar{\sigma}\_{\textmd{BF},x\Delta}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +V​(1,KMS,C,x​Δ,T,σATM+σ¯BF,x​Δ),\displaystyle+V(1,K\_{\textmd{MS},\textmd{C},x\Delta},T,\sigma\_{\textmd{ATM}}+\bar{\sigma}\_{\textmd{BF},x\Delta})\,, |  | (5) |

where V​(±1,K,T,σ)V(\pm 1,K,T,\sigma) is the price of a vanilla European call (resp. put) option of strike KK and maturity TT and volatilty σ\sigma and x∈{10,25}x\in\{10,25\}. The same volatility (our market quote σ¯BF,x​Δ)\bar{\sigma}\_{\textmd{BF},x\Delta})) is used for both call and put in the broker convention, at different strikes KMS,P,x​ΔK\_{\textmd{MS},\textmd{P},x\Delta} and KMS,C,x​ΔK\_{\textmd{MS},\textmd{C},x\Delta}. Those strikes are defined such that the following holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(−1,KMS,P,x​Δ,T,σATM+σ¯BF,x​Δ)\displaystyle\Delta(-1,K\_{\textmd{MS},\textmd{P},x\Delta},T,\sigma\_{\textmd{ATM}}+\bar{\sigma}\_{\textmd{BF},x\Delta}) | =−x%,\displaystyle=-x\%\,, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​(1,KMS,C,x​Δ,T,σATM+σ¯BF,x​Δ)\displaystyle\Delta(1,K\_{\textmd{MS},\textmd{C},x\Delta},T,\sigma\_{\textmd{ATM}}+\bar{\sigma}\_{\textmd{BF},x\Delta}) | =+x%.\displaystyle=+x\%\,. |  | (6) |

While Equation [6](https://arxiv.org/html/2512.19625v1#S1.E6 "In 1 Introduction") gives the strikes of the market strangle, we do not know the European option volatilities for those strikes, we only know the overall strangle strategy price through σATM+σBF,x​Δ\sigma\_{\textmd{ATM}}+\sigma\_{\textmd{BF},x\Delta}.

The risk-reversal quotes are defined such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | σRR,x​Δ=σC,x​Δ−σP,x​Δ.\displaystyle\sigma\_{\textmd{RR},x\Delta}=\sigma\_{\textmd{C},x\Delta}-\sigma\_{\textmd{P},x\Delta}\,. |  | (7) |

In particular, the quote is negative if σC,x​Δ<σP,x​Δ\sigma\_{\textmd{C},x\Delta}<\sigma\_{\textmd{P},x\Delta}. Finding the volatilities σC,x​Δ\sigma\_{\textmd{C},x\Delta} and σP,x​Δ\sigma\_{\textmd{P},x\Delta} (and the corresponding vanilla option strikes) necessitates a continuous representation of volatilities across strikes, as the vanilla option strikes do not correspond to the market strangle strikes. Let σ​(K)\sigma(K) be such a representation, we have then the following system to solve:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ​(KATM)\displaystyle\sigma(K\_{\textmd{ATM}}) | =σATM,\displaystyle=\sigma\_{\textmd{ATM}}\,, |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​(1,KC,x​Δ,T,σ​(KC,x​Δ))\displaystyle\Delta(1,K\_{\textmd{C},x\Delta},T,\sigma(K\_{\textmd{C},x\Delta})) | =+x​Δ%,\displaystyle=+x\Delta\%\,, |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​(−1,KP,x​Δ,T,σ​(KP,x​Δ))\displaystyle\Delta(-1,K\_{\textmd{P},x\Delta},T,\sigma(K\_{\textmd{P},x\Delta})) | =−x​Δ%,\displaystyle=-x\Delta\%\,, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(−1,KMS,P,x​Δ,T,σ​(KMS,P,x​Δ))+V​(1,KMS,C,x​Δ,T,σ​(KMS,C,x​Δ))\displaystyle V(-1,K\_{\textmd{MS},\textmd{P},x\Delta},T,\sigma(K\_{\textmd{MS},\textmd{P},x\Delta}))+V(1,K\_{\textmd{MS},\textmd{C},x\Delta},T,\sigma(K\_{\textmd{MS},\textmd{C},x\Delta})) | =VMS,x​Δ,\displaystyle=V\_{\textmd{MS},x\Delta}\,, |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ​(KC,x​Δ)−σ​(KP,x​Δ)\displaystyle\sigma(K\_{\textmd{C},x\Delta})-\sigma(K\_{\textmd{P},x\Delta}) | =σRR,x​Δ.\displaystyle=\sigma\_{\textmd{RR},x\Delta}\,. |  | (12) |

Due to the difference between KMS,P,x​ΔK\_{\textmd{MS},\textmd{P},x\Delta} and KP,x​ΔK\_{\textmd{P},x\Delta}, there are nine different strikes involved, not just five. The strikes KC,x​Δ,KP,x​ΔK\_{\textmd{C},x\Delta},K\_{\textmd{P},x\Delta} may be solved exactly using Equations [9](https://arxiv.org/html/2512.19625v1#S1.E9 "In 1 Introduction") and [10](https://arxiv.org/html/2512.19625v1#S1.E10 "In 1 Introduction") for given volatilities. We then have 5 remaining equations to fit the volatility representation σ​(K)\sigma(K). There are several ways to perform the fit.

clark2011foreign describes how to solve the system assuming a single unknown, the smile butterfly volatility σBF,25​Δ\sigma\_{\textmd{BF},25\Delta}, and does not try to fit to 10​Δ10\Delta quotes. We adapt the algorithm to handle 10​Δ10\Delta and 25​Δ25\Delta quotes together:

1. 1.

   Choose an initial guess for the smile butterfly volatilities {σBF,25​Δ,σBF,10​Δ}\{\sigma\_{\textmd{BF},25\Delta},\sigma\_{\textmd{BF},10\Delta}\}, typically the market butterfly quotes {σ¯BF,25​Δ,σ¯BF,10​Δ}\{\bar{\sigma}\_{\textmd{BF},25\Delta},\bar{\sigma}\_{\textmd{BF},10\Delta}\} (which corresponds to slightly different strikes).
2. 2.

   Use Equation [1](https://arxiv.org/html/2512.19625v1#S1.E1 "In 1 Introduction") to obtain σC,25​Δ,σP,25​Δ,σC,10​Δ,σP,10​Δ\sigma\_{\textmd{C},25\Delta},\sigma\_{\textmd{P},25\Delta},\sigma\_{\textmd{C},10\Delta},\sigma\_{\textmd{P},10\Delta} from the risk reversal quotes. Equation [1](https://arxiv.org/html/2512.19625v1#S1.E1 "In 1 Introduction") is exact when the vanilla volatilities correspond to the smile implied Δ\Deltas, which is the case here.
3. 3.

   Calculate the vanilla option strikes by solving Equations [9](https://arxiv.org/html/2512.19625v1#S1.E9 "In 1 Introduction") and [10](https://arxiv.org/html/2512.19625v1#S1.E10 "In 1 Introduction").
4. 4.

   Find parameters of σ​(K)\sigma(K) using a least-squares-optimizer on the volatilities σATM,σC,25​Δ,σP,25​Δ,σC,10​Δ,σP,10​Δ\sigma\_{\textmd{ATM}},\sigma\_{\textmd{C},25\Delta},\sigma\_{\textmd{P},25\Delta},\sigma\_{\textmd{C},10\Delta},\sigma\_{\textmd{P},10\Delta}.
5. 5.

   Price up the market strangle using σ​(K)\sigma(K). The least-squares error in model price against the market price (Equation [11](https://arxiv.org/html/2512.19625v1#S1.E11 "In 1 Introduction")) defines the objective.

A Gauss-Newton optimizer klare2013gn may be used to find the least-squares solution in option prices. The unknown σBF,25​Δ\sigma\_{\textmd{BF},25\Delta} may be negative, it is perfectly acceptable (wystup2018butterfly). The bound constraint is for the vanilla volatilities given by Equation [1](https://arxiv.org/html/2512.19625v1#S1.E1 "In 1 Introduction") to be positive.

This presupposes that the representation σ​(K)\sigma(K) fits well to the ATM, 10Δ\Delta and 25Δ\Delta strikes: the smile fitting procedure to vanillas is somewhat decoupled from the fitting to market strangles. For non-exact interpolations, it may be particularly relevant to add the error in ATM and RR volatilities, corresponding to Equations [8](https://arxiv.org/html/2512.19625v1#S1.E8 "In 1 Introduction") and [12](https://arxiv.org/html/2512.19625v1#S1.E12 "In 1 Introduction"), to the objective in step (5). The output has then a dimension of five. The intent is to recouple the vanilla fit with the market strangle fit. There is however a caveat: the market strangle error is minimized in terms of price, while the ATM and RR errors are minimized in terms of volatility. In order to obtain a similar error scale, an inverse vega weight wMS,x​Δw\_{\textmd{MS},x\Delta} must be used in the market strangle model vs. market price error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wMS,x​Δ=1[ϕ​(d1​(KMS,P,σATM+σ¯BF,x​Δ))+ϕ​(d1​(KMS,C,σATM+σ¯BF,x​Δ))]​T​F​(0,T).w\_{\textmd{MS},x\Delta}=\frac{1}{\left[\phi\left(d\_{1}(K\_{\textmd{MS},\textmd{P}},\sigma\_{\textmd{ATM}}+\bar{\sigma}\_{\textmd{BF},x\Delta})\right)+\phi\left(d\_{1}(K\_{\textmd{MS},\textmd{C}},\sigma\_{\textmd{ATM}}+\bar{\sigma}\_{\textmd{BF},x\Delta})\right)\right]\sqrt{T}F(0,T)}\,. |  | (13) |

An additional subtlety is how and when to solve for the strikes of the Δ\Delta based quotes. Indeed, the two risk-reversals define vanilla Δ\Delta-based quotes according to the currency pair and maturity convention. In Step 3, clark2011foreign suggests that the smile parameterization should be used, and thus Step 4 should actually be merged with Step 3, such that we solve for the strike, using the smile. This makes a difference if the objective of dimension 2, and we will adopt this approach in our numerical examples, but it should not matter much if the objective is of dimension 5 with an error in RR volatilities computed according to the 10Δ\Delta and 25Δ\Delta vanilla options, as implied by the calibrated smile in Step 4.

Finally, it is also possible to perform a single minimization, where the parameters of the representation σ​(K)\sigma(K) are the unknown: the initial guess would be computed based on the smile convention, the objective would be the extended objective of dimension 5 based on the volatilities given by the parameters. It is in general less practical, since this direct algorithm does not allow for an easy reuse of an existing vanilla option smile calibration, while the above algorithm is identical regardless of the smile interpolation. The outcome of the calibration should be the same as the nested algorithm when the extended objective of dimension 5 is also used there.

In this article, we examine a few counterexamples where the fitting procedure does not necessary lead to an adequate interpolation of vanilla option prices.

## 2 At-the-money error

We consider options of maturity 147 days on EUR/HKD as of January 25, 2024 (Table [1](https://arxiv.org/html/2512.19625v1#S2.T1 "Table 1 ‣ 2 At-the-money error")).
With exact interpolations such as a spline in log-moneyness, a cubic spline in forward Δ\Delta or a polynomial in Δ\Delta, the vanilla implied volatilities are almost exactly the same. The SABR approximation333In the case of FX options it is usual to set the SABR parameter β=1\beta=1 to avoid any probability mass at zero. of hagan2002managing does not fit exactly, which leads to small differences in the vanilla implied volatilies.

Table 1: Options on EUR/HKD expiring in 147 days as of January 25, 2024. F​(T)=8.500504F(T)=8.500504, BEUR​(T)=0.9848102B\_{\textmd{EUR}}(T)=0.9848102, spot = 8.510111.

| ATM | 25Δ\Delta-RR | 25Δ\Delta-BF | 10Δ\Delta-RR | 10Δ\Delta-BF |
| --- | --- | --- | --- | --- |
| 6.575 | -0.647 | 0.202 | -1.200 | 0.570 |

There are two potential issues with the final objective of dimension 2, which consists only in the error in strangle prices:

* •

  The ATM error may be larger than we wish. Figure[1](https://arxiv.org/html/2512.19625v1#S2.F1 "Figure 1 ‣ 2 At-the-money error") shows an absolute ATM error in volatility of 0.09%, which dominates the other errors.
  A remedy is to match exactly the ATM volatility, thus reducing the number of parameters to fit, which is a common SABR calibration practice (west2005calibration).
* •

  The error in risk-reversals is not controlled.

Table 2: Absolute error in weighted MS prices and RR, ATM vols %. Violet indicates errors not part of the final objective.

| Maturity | Model | Obj. dim. | 25Δ\Delta MS | 10Δ\Delta MS | 25Δ\Delta RR | 10​Δ10\Delta RR | ATM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1y | XSSVI | 2 | 0.0864 | -0.0367 | 0.1629 | -2.8797 | 0.0552 |
|  |  | 5 | 0.0869 | -0.3024 | 1.2725 | -0.6790 | 0.0471 |
| 2y |  | 2 | 0.0000 | 0.0000 | 2.7042 | 1.7177 | 0.0422 |
|  |  | 5 | -0.2498 | -0.2881 | 1.3137 | -0.6915 | 0.1043 |

![Refer to caption](x1.png)


Figure 1: Vanilla implied volatilities for EUR/HKD 147 days options with the SABR parameterization.

Figure [1](https://arxiv.org/html/2512.19625v1#S2.F1 "Figure 1 ‣ 2 At-the-money error") displays the implied volatility smiles corresponding to the various calibration strategies.
The RR calibration issue is clearer when calibrating the XSSVI parameterization of corbetta2019robust to EUR/TRY options of maturity 1 year as of 2022/11/29 (Figure [2](https://arxiv.org/html/2512.19625v1#S2.F2 "Figure 2 ‣ 2 At-the-money error")).
Using the extended objective of dimension 5 proves to be key here.

![Refer to caption](x2.png)


Figure 2: Vanilla implied volatilities for EUR/TRY 1y options with the XSSVI parameterization.

Looking at those makes us think we may fit SABR or XSSVI directly to the vanilla option volatilities implied by an exact interpolation such as a cubic spline in log-moneyness from the ATM, RR and BF quotes. This is a third approach to the FX smile calibration. Its main advantages would be simplicity, robustness (because the interpolations are exact, and thus the conversions with market convention deltas are more direct), and easy reuse of existing model calibration algorithms to vanillas.
In the next section we will discover that the choice of exact interpolation may matter more than we would like.

## 3 When exact interpolations lead to different volatilities

We consider now options on EUR/TRY of maturity 2 year as of 2022/11/29 (Table [3](https://arxiv.org/html/2512.19625v1#S3.T3 "Table 3 ‣ 3 When exact interpolations lead to different volatilities")). The Turkish Lira is particularly volatile, due to the high inflation in Turkey in 2022 and the resulting implied volatility smile has a somewhat unusual shape.

Table 3: Quotes for options on EUR/TRY as of 2022/11/29 in forward Δ\Delta with premium.
For the maturity of 1 year, we have rTRY=37.73%r\_{\textmd{TRY}}=37.73\%, rEUR=1.784%r\_{\textmd{EUR}}=1.784\%, spot=19.3483.
For the maturity of 2 years, we have rTRY=37.65%r\_{\textmd{TRY}}=37.65\%, rEUR=1.950%r\_{\textmd{EUR}}=1.950\%. The ⋆\star indicates manufactured quotes.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Maturity | ATM | 25Δ\Delta-RR | 25Δ\Delta-BF | 10Δ\Delta-RR | 10Δ\Delta-BF |
| 6m | 22.12 | 9.385 | 2.187 | 21.148 | 7.633 |
| 1y | 31.13 | 11.568 | 2.931 | 27.120 | 9.307 |
|  | 10Δ\Delta-Put | 25Δ\Delta-Put | ATM | 25Δ\Delta-Call | 10Δ\Delta-Call |
| 1y | 24.08 | 28.64 | 31.13 | 40.21 | 51.20 |

We calibrate the cubic spline in log-moneyness, cubic spline in forward Δ\Delta and polynomial in simple Δ\Delta. They interpolate exactly the vanilla option volatilities and thus, the objective dimension does not matter. It turns out that the resulting vanilla implied volatilities can be quite different, especially the 10Δ\Delta Put and Call, even though the error in MS, RR and ATM prices is zero. This is also an example where the simple smile convention approximation does not lead to correct vanilla implied volatilities.
The exponential polynomial in simple444Δsimple=Φ​(log⁡(F/K)/σ​T)\Delta\_{\textmd{simple}}=\Phi(\log(F/K)/\sigma\sqrt{T}). Contrary to Clark, we use the actual volatility and fully solve the strike for a given Δ\Delta. Δ\Delta of clark2011foreign leads to nearly the same implied vanilla quotes as the cubic spline on forward Δ\Delta.

![Refer to caption](x3.png)


Figure 3: Exact interpolations calibrated to options on EUR/TRY expiring in 2 year as of 2022/11/29.

Which vanillas are better to calibrate to? In Figure [4](https://arxiv.org/html/2512.19625v1#S3.F4 "Figure 4 ‣ 3 When exact interpolations lead to different volatilities"), we calibrate SABR and XSSVI to the vanilla option volatilities implied by the cubic spline in Δ\Delta and in log-moneyness. On this somewhat extreme data, the full model calibration is very close to the calibration of vanillas implied by the log-moneyness based spline.

![Refer to caption](x4.png)


(a) SABR

![Refer to caption](x5.png)


(b) XSSVI

Figure 4: SABR and XSSVI calibrated to vanilla implied quotes for EUR/TRY expiring in 2 year as of 2022/11/29.

This is not always the case, in Figure [5](https://arxiv.org/html/2512.19625v1#S3.F5 "Figure 5 ‣ 3 When exact interpolations lead to different volatilities"), we calibrate XSSVI to options on USD/JPY of maturity 1 year with quotes given in (clark2011foreign, Table 3.4 and Section 3.5.5). The Delta based spline calibration is then the closest to the full model calibration. Here, the SABR calibration (not displayed) is nearly identical regardless of the choice of approach.

![Refer to caption](x6.png)


Figure 5: Exact interpolations calibrated to options on USD/JPY expiring in 1 year.

## 4 Manufactured example

If we bump slightly the 25​Δ25\Delta-RR quote and change the sign of the RR quotes in Table [3](https://arxiv.org/html/2512.19625v1#S3.T3 "Table 3 ‣ 3 When exact interpolations lead to different volatilities"), we still have arbitrage-free quotes.
The calibration against those manufactured market quotes using a polynomial in Δ\Delta leads to an oscillating smile.
The resulting vanilla implied volatilities at 10​Δ10\Delta are also clearly distinct from the ones of the spline based calibrations (Figure [6](https://arxiv.org/html/2512.19625v1#S4.F6 "Figure 6 ‣ 4 Manufactured example")).

![Refer to caption](x7.png)


Figure 6: Exact interpolations calibrated to manufactured quotes for options on EUR/TRY options expiring in 2 year as of 2022/11/29. The polynomial in Δ\Delta oscillates.

## 5 Numerical issues

### 5.1 Call Δ\Delta with premium

Delta lookups can be tricky:
the Call ΔF,pct\Delta\_{F,\textmd{pct}} is a non monotonic function of strike, or equivalently, of log-moneyness.
As a consequence, reiswich2012fx advise to first search for the maximum and then solve for the strike on the right side of the maximum, corresponding to OTM strikes. jackel2020strike proposes a fast, accurate and robust numerical method tailored to this problem.

It becomes even more challenging if we calibrate the smile function based on the market Delta quotes directly, which is essentially what is described in (clark2011foreign). A non-linear solver needs to be used to lookup the model volatility at given Δ\Deltas, for each choice of model parameters done by the smile calibration minimizer.
Some Δ\Deltas may not be reachable by any strike as, for high volatilities, the maximum ΔF,pct\Delta\_{F,\textmd{pct}} can be below 25% (e.g. Figure [7](https://arxiv.org/html/2512.19625v1#S5.F7 "Figure 7 ‣ 5.1 Call Δ with premium ‣ 5 Numerical issues")).
This means that the smile function may not be able to produce a quote for the 25Δ\Delta call option.

![Refer to caption](x8.png)


Figure 7: Call Forward Δ\Delta with premium as a function of log-moneyness for a large volatility σ=125%\sigma=125\% and T=2T=2 years.
Notice the non-monotonicity and the peak not reaching Δ=25%\Delta=25\%.

There are other edge cases, such as very low quoted vols, or exploding model vols, which may happen in the wings of SABR and lead to non-sensical Deltas, during the minimization.

### 5.2 Delta for a given strike

Some smile representations we considered involve a direct Δ\Delta based interpolation.
For example, the polynomial in Δ\Delta function with coefficients (ai)i=0,…,5(a\_{i})\_{i=0,...,5} reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(Δsimple)=exp⁡(∑i=04ai​Δsimple​(K,σ)i)\sigma(\Delta\_{\textmd{simple}})=\exp\left(\sum\_{i=0}^{4}a\_{i}\Delta\_{\textmd{simple}}(K,\sigma)^{i}\right) |  | (14) |

where Δsimple​(K,σ)=Φ​(ln⁡F​(0,T)/Kσ​T)\Delta\_{\textmd{simple}}(K,\sigma)=\Phi\left(\frac{\ln F(0,T)/K}{\sigma\sqrt{T}}\right).

In order to price vanilla options, we need to find the volatility for a given fixed strike, with the above implicit definition of
the smile function in terms of Δsimple\Delta\_{\textmd{simple}}.
wystup2017fx describes the simple fixed point iteration:

1. 1.

   Choose σ0\sigma\_{0} = at-the-money vol.
2. 2.

   Calculate Δn+1=Δsimple​(K,σn)\Delta\_{n+1}=\Delta\_{\textmd{simple}}(K,\sigma\_{n}).
3. 3.

   Take σn+1=σ​(Δn+1)\sigma\_{n+1}=\sigma(\Delta\_{n+1}), using Equation [14](https://arxiv.org/html/2512.19625v1#S5.E14 "In 5.2 Delta for a given strike ‣ 5 Numerical issues").
4. 4.

   If |σn+1−σn|<ϵ|\sigma\_{n+1}-\sigma\_{n}|<\epsilon, then quit, otherwise continue with Step 2.

This leads to an infinite loop for 𝒂=(0.114,−11.8,49.2,−84.1,48.5)\bm{a}=(0.114,-11.8,49.2,-84.1,48.5), T=2T=2, F​(0,T)=39.51F(0,T)=39.51, σ0=32%\sigma\_{0}=32\%, K=10K=10.
The smile corresponding to this polynomial is presented in Figure [8](https://arxiv.org/html/2512.19625v1#S5.F8 "Figure 8 ‣ 5.2 Delta for a given strike ‣ 5 Numerical issues").
A better idea would be to use the Newton’s method:

1. 1.

   Choose σ0\sigma\_{0} = at-the-money vol.
2. 2.

   Define the objective function f​(v)=σ​(Δsimple​(K,v))−vf(v)=\sigma(\Delta\_{\textmd{simple}}(K,v))-v, using Equation [14](https://arxiv.org/html/2512.19625v1#S5.E14 "In 5.2 Delta for a given strike ‣ 5 Numerical issues").
3. 3.

   Use Newton’s method on ff, starting with v=σ0v=\sigma\_{0}.

This also fails, this time for a lower strike, for example K=5K=5.
A more robust way is to define the objective as a function of Δ\Delta instead of volatility:

1. 1.

   Define the objective function g​(d)=Δsimple​(K,σ​(d))−dg(d)=\Delta\_{\textmd{simple}}(K,\sigma(d))-d, using Equation [14](https://arxiv.org/html/2512.19625v1#S5.E14 "In 5.2 Delta for a given strike ‣ 5 Numerical issues").
2. 2.

   Use bracketing solver such the TOMS748 solver of alefeld1995algorithm to solve g​(d)=0g(d)=0 on [0,1]. This leads to a solution dfinald\_{\textmd{final}}.
3. 3.

   Then Δsimple​(K,σ)=dfinal\Delta\_{\textmd{simple}}(K,\sigma)=d\_{\textmd{final}}.

If, instead of a bracketing solver, we were to use Newton’s method, dd may pushed beyond the range [0,1].
It is possible to rely on Newton’s method, using a transformation hh on dd from ℝ→(0,1)\mathbb{R}\to(0,1), such as the sigmoid function.

![Refer to caption](x9.png)


(a) Smile in Δsimple\Delta\_{\textmd{simple}}

![Refer to caption](x10.png)


(b) Δsimple​(K,σ)\Delta\_{\textmd{simple}}(K,\sigma) is monotonic

Figure 8: Example of problematic polynomial in Δsimple\Delta\_{\textmd{simple}}.

### 5.3 Non monotonic Deltas

During the calibration of SABR, some parameters tried by the minimizer may lead to arbitrages, because we use only an approximation for the SABR model (the one from obloj2007fine), a common practice, but this expansion is really only valid for a small vol-of-vol. A consequence is a non monotonic forward Δ\Delta, even for Put-Δ\Delta or ΔF,pips\Delta\_{F,\textmd{pips}} (without premium). Two examples of SABR parameters are provided in Table [4](https://arxiv.org/html/2512.19625v1#S5.T4 "Table 4 ‣ 5.3 Non monotonic Deltas ‣ 5 Numerical issues"). Figure [9](https://arxiv.org/html/2512.19625v1#S5.F9 "Figure 9 ‣ 5.3 Non monotonic Deltas ‣ 5 Numerical issues") shows the non-monotonic Call ΔF,pips\Delta\_{F,\textmd{pips}}, which does not reach 30%, meaning the SABR wing is bad, and has arbitrages.

Table 4: Examples of SABR parameters which lead to non monotonic ΔF,pips\Delta\_{F,\textmd{pips}} with F​(0,T)=39.512F(0,T)=39.512, T=2T=2, B​(0,T)=0.96175B(0,T)=0.96175.

| Set | α\alpha | β\beta | ρ\rho | ν\nu |
| --- | --- | --- | --- | --- |
| I | 34.9% | 1 | 54.4% | 127% |
| II | 37.5 % | 1 | 66.0% | 100% |



![Refer to caption](x11.png)


(a) Smile

![Refer to caption](x12.png)


(b) Call ΔF,pips\Delta\_{F,\textmd{pips}}

Figure 9: A problematic SABR smile. The ΔF,pips\Delta\_{F,\textmd{pips}} does not reach 25% and is not monotonic.

Those parameters do not allow to obtain a price for a 10​Δ10\Delta or a 25​Δ25\Delta Call. This will need to be dealt with in not-so-obvious manners in the minimization. A remedy may be to use an arbitrage-free implementation of SABR (lefloch2014finite).

## 6 Conclusion

We reviewed different ways to calibrate a model to the market quotes, and how this choice may impact the outcome of the calibration.

The most precise is to fully calibrate directly the model to the market MS, RR and ATM quotes, but care needs to be taken such that the final objective is sensitive to all quotes. There is then a negligible difference between a calibration of the smile parameterization directly to volatilities in the market Δ\Delta convention or to volatilities in fixed strikes. While calibrating directly to quotes in Δ\Deltas is attractive, is suffers from the eventuality of many more numerical issues, and requires more computational resources.

The simplest, and likely more robust way is to use an exact interpolation to imply some vanilla implied volatilities, which replicate exactly the market quotes. And then to calibrate the chosen smooth parameterization on top of those. The exact interpolation bypasses many caveats with Δ\Delta inversions.
We have seen that there is no unique solution to this problem, the use of a cubic spline on log-moneyness seems the simplest. The difference in the error against market quotes is usually negligible (Table [5](https://arxiv.org/html/2512.19625v1#A1.T5 "Table 5 ‣ Appendix A Calibration errors")).

###### Acknowledgements.

The author would like to thank Dr. Gary Kennedy and Dr. Fabien Le Floc’h for fruitful conversations and feedback on early drafts of this paper.
\externalbibliographyyes
\appendixtitlesno

## Appendix A Calibration errors

Table 5: Calibration error corresponding to the objective of dimension 5, for different option sets, using a calibration, (a) on top of vanilla quotes implied by a spline in log-moneyness, (b) on top of vanilla quotes implied by a spline in Δ\Delta, (c1) with the objective of dimension 2 and converting strikes up-front before the smile calibration step 4, (c2) with the objective of dimension 2 and steps 3 and 4 merged such that the parameterization is directly calibrated to Δ\Delta quotes, (d1) with the objective of dimension 5 and converting strikes up-front before the smile calibration step 4, (d2) with the objective of dimension 5 and steps 3 and 4 merged.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Option set | Model | Calibration | ℓ2\ell\_{2} Error | |
|  |  |  | Fixed Strikes | Fixed Δ\Deltas |
| USD/AED 7d | ATM SABR | Spline | 0.00005 |  |
|  |  | Spline Δ\Delta | 0.00005 |  |
|  |  | Dimension 2 | 0.00258 | 0.00004 |
|  |  | Dimension 5 | 0.00004 | 0.00004 |
|  | SABR | Dimension 5 | 0.00004 | 0.00004 |
|  | XSSVI | Spline | 0.00259 |  |
|  |  | Spline Δ\Delta | 0.00261 |  |
|  |  | Dimension 2 | 0.00491 | 0.00491 |
|  |  | Dimension 5 | 0.00149 | 0.00149 |
| EUR/TRY 2y | ATM SABR | Spline | 0.00679 |  |
|  |  | Spline Δ\Delta | 0.01140 |  |
|  |  | Dimension 2 | 0.00821 | 0.00831 |
|  |  | Dimension 5 | 0.00665 | 0.00663 |
|  | SABR | Dimension 5 | 0.00665 | 0.00663 |
|  | XSSVI | Spline | 0.01557 |  |
|  |  | Spline Δ\Delta | 0.01657 |  |
|  |  | Dimension 2 | 0.01593 | 0.03203 |
|  |  | Dimension 5 | 0.01536 | 0.01536 |
| EUR/HKD 147d | ATM SABR | Spline | 0.00069 |  |
|  |  | Spline Δ\Delta | 0.00069 |  |
|  |  | Dimension 2 | 0.00722 | 0.00073 |
|  |  | Dimension 5 | 0.00068 | 0.00067 |
|  | SABR | Dimension 5 | 0.00059 | 0.00059 |
|  | XSSVI | Spline | 0.00057 |  |
|  |  | Spline Δ\Delta | 0.00057 |  |
|  |  | Dimension 2 | 0.01870 | 0.00083 |
|  |  | Dimension 5 | 0.00056 | 0.00057 |
| AUD/NZD 1w | ATM SABR | Spline | 0.00219 |  |
|  |  | Spline Δ\Delta | 0.00219 |  |
|  |  | Dimension 2 | 0.00238 | 0.00215 |
|  |  | Dimension 5 | 0.00215 | 0.00215 |
|  | SABR | Dimension 5 | 0.00218 | 0.00214 |
|  | XSSVI | Spline | 0.00212 |  |
|  |  | Spline Δ\Delta | 0.00212 |  |
|  |  | Dimension 2 | 0.00213 | 0.00211 |
|  |  | Dimension 5 | 0.00211 | 0.00211 |
| USD/JPY 1y | ATM SABR | Spline | 0.00325 |  |
|  |  | Spline Δ\Delta | 0.00314 |  |
|  |  | Dimension 2 | 0.00280 | 0.00266 |
|  |  | Dimension 5 | 0.00260 | 0.00257 |
|  | SABR | Dimension 5 | 0.00260 | 0.00257 |
|  | XSSVI | Spline | 0.00856 |  |
|  |  | Spline Δ\Delta | 0.00771 |  |
|  |  | Dimension 2 | 0.00876 | 0.00749 |
|  |  | Dimension 5 | 0.00737 | 0.00743 |