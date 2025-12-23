---
authors:
- Jherek Healy
doc_id: arxiv:2512.19621v1
family_id: arxiv:2512.19621
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2512.19621v1
url_html: https://arxiv.org/html/2512.19621v1
venue: arXiv q-fin
version: 1
year: 2025
---

###### Abstract

This article provides a list of counterexamples, where some of the popular fx option interpolations break down. Interpolation of FX option prices (or equivalently volatilities), is key to risk-manage not only vanilla FX option books, but also more exotic derivatives which are typically valued with local volatility or local stochastic volatilility models.

###### keywords:

fx options; volatility; arbitrage; interpolation

\pubvolume\issuenum

1
\articlenumber1
\history
\TitleCounterexamples for FX Options Interpolations - Part I
\AuthorJherek Healy
\AuthorNamesJherek Healy

## 1 Introduction

Market prices of Foreign exchange (FX) options are typically quoted as a sparse set volatilities per option maturity.
Those correspond to the volatilities of an at-the-money (ATM) option, 25Δ\Delta and 10Δ\Delta risk-reversals and butterflies.
Depending on the currency pair and the maturity, there is much variation in what ATM exactly means: is it at the money straddle? with or without premium? spot or forward ? There are also two conventions for the risk-reversal (RR) and butterfly (BF): the simple smile convention where

|  |  |  |
| --- | --- | --- |
|  | σcall=σATM+σBF+12​σRR,σput=σATM+σBF−12​σRR,\displaystyle\sigma\_{\textmd{call}}=\sigma\_{\textmd{ATM}}+\sigma\_{\textmd{BF}}+\frac{1}{2}\sigma\_{\textmd{RR}}\,,\quad\sigma\_{\textmd{put}}=\sigma\_{\textmd{ATM}}+\sigma\_{\textmd{BF}}-\frac{1}{2}\sigma\_{\textmd{RR}}\,, |  |

and the more involved broker convention which requires a numerical solver. clark2011foreign; reiswich2012fx describe
the various conventions in details.

The conversion of RR and BF quotes to vanilla option implied volatilities will be the focus of a subsequent article. In this paper, the concern is to price and risk manage options, whose strikes will not correspond to the strikes implied
by the quoted Δ\Delta. A popular approach is to interpolate the volatilities in terms of Δ\Delta. A single Δ\Delta convention
is typically used for all maturities, regardless of the actual quoting Δ\Delta convention. malz1997option proposed to use a quadratic polynomial, cubic splines are another common choice.
Interpolating in Δ\Delta, requires to solve the following non linear problem in order to find the volatility for a given option strike:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(K)=f​(ΔF​(K,σ​(K))),\sigma(K)=f\left(\Delta\_{F}(K,\sigma(K))\right)\,, |  | (1) |

where ff is the smile representation, Φ\Phi the cumulative normal distribution, σ\sigma, the implied volatility, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔF​(K,σ​(K))=±Φ​(±ln⁡F​(T)K−σ2​(K)​T2σ​(K)​T),\Delta\_{F}(K,\sigma(K))=\pm\Phi\left(\pm\frac{\ln\frac{F(T)}{K}-\frac{\sigma^{2}(K)T}{2}}{\sigma(K)\sqrt{T}}\right)\,, |  | (2) |

for the forward delta convention without premium (+ for a call, - for a put). In (malz1997option) the function ff is a quadratic, while in (clark2018using) it is the exponential of a quartic.

To avoid the non-linear problem, clark2011foreign suggests the use of a polynomial in terms of a reduced ΔR\Delta\_{R}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔR​(K)=Φ​(ln⁡F​(T)Kσ​(F​(T))​T).\Delta\_{R}(K)=\Phi\left(\frac{\ln\frac{F(T)}{K}}{\sigma(F(T))\sqrt{T}}\right)\,. |  | (3) |

In the expression of ΔR\Delta\_{R}, the volatility is taken at-the-money only.

Those choices are simple and the representation in Δ\Delta is convenient for the traders, but they suffer from two major
drawbacks: they are not arbitrage-free, and they lead to a flat volatility for small and large strikes.
Flattening wings are not particularly realistic, as this means that all moments are finite (lee2004moment), and thus
the distribution does not really have fat tails. In addition, stochastic volatility models lead to linear wings in variance (gatheral2011convergence).

Some practitioners thus moved to more advanced representations, such as the SABR model of hagan2002managing (with β=1\beta=1),
or the SVI parameterization of gatheral2006volatility. Those do not allow
to interpolate exactly the option quotes, due to the constrained shapes of volatility smiles they can represent.
One on hand it may avoid overfitting, on the other hand, it is sometimes be desirable to fit nearly exactly to the market quotes.
For example, Clark uses the quartic representation to be able to detect some multi-modality in the implied probability density. Other uses
may relate to some risk engine limitations.

The key characteristics of an interpolation scheme for fx option volatilities are:

1. 1.

   no arbitrage,
2. 2.

   smooth implied probability density,
3. 3.

   ability to control the wings,
4. 4.

   possibility of nearly exact interpolation, even if this usually means overfitting the quotes.

In this article, we will provide a list of counterexamples, where some of the popular smile representation break down.

## 2 Oscillations in the density

wystup2017arbitrage presented one of the rare counterexample of the literature to illustrate the possibility of
negative density with the SVI parameterization, and provided detailed market data, which allow for an easy replication of the issue. It consists of FX options on AUD/NZD expiring in 7 days as of 2014/07/02. The quotes, reproduced in Table [1](https://arxiv.org/html/2512.19621v1#S2.T1 "Table 1 ‣ 2 Oscillations in the density") thus correspond to the convention of spot Δ\Delta with premium.

Table 1: Options on AUD/NZD expiring in 7 days as of 2014/07/02. F​(T)=1.07845F(T)=1.07845, BAUD​(T)=0.999712587139B\_{\textmd{AUD}}(T)=0.999712587139, spot = 1.0784. The quotes are converted to Put/Call vanilla vols using the simple approximation.

| ATM | 25Δ\Delta-RR | 25Δ\Delta-BF | 10Δ\Delta-RR | 10Δ\Delta-BF |
| --- | --- | --- | --- | --- |
| 5.14 | 0.40 | 0.25 | 0.35 | 1.175 |
| 10Δ\Delta-Put | 25Δ\Delta-Put | ATM | 25Δ\Delta-Call | 10Δ\Delta-Call |
| 6.14 | 5.19 | 5.14 | 5.59 | 6.49 |

If we calibrate SVI according to the recommendations of de2009quasi, that is enforcing a≥0a\geq 0, and thus ensuring that the variance is always positive, the
density stays positive. In Figure [1](https://arxiv.org/html/2512.19621v1#S2.F1 "Figure 1 ‣ 2 Oscillations in the density"), we plot the Dupire local variance denominator gatheral2006volatility

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(y)=1−yw​(y)​∂w∂y+14​(−14−1w​(y)+y2w​(y)2)​(∂w∂y)2+12​∂2w∂y2g(y)=1-\frac{y}{w(y)}\frac{\partial w}{\partial y}+\frac{1}{4}\left(-\frac{1}{4}-\frac{1}{w(y)}+\frac{y^{2}}{w(y)^{2}}\right)\left(\frac{\partial w}{\partial y}\right)^{2}+\frac{1}{2}\frac{\partial^{2}w}{\partial y^{2}} |  | (4) |

where w​(y)=σ2​(F​(T)​ey)​Tw(y)=\sigma^{2}(F(T)e^{y})T is the total variance in log-moneyness, F​(T)F(T) is the forward price to maturity TT. In the SVI representation, we have w(y)=aT+bT(ρ(y−m)+(y−m)2+s2w(y)=aT+bT(\rho(y-m)+\sqrt{(y-m)^{2}+s^{2}} where a,b,ρ,m,sa,b,\rho,m,s are SVI parameters).
A negative variance denominator is equivalent to a negative probability density, but the scale of the denominator function makes it easier to visualize the location of negative density.
While the constraint works well on this example, it is not guaranteed to always work, although, in general, the SVI parameterization behaves well, hence its popularity.

It turns out that when the volatilities are interpolated with a cubic spline on ΔF\Delta\_{F}, a
spurious spike appears spline density near the money. Although
wystup2017arbitrage mentions this problem for another example, it is much more significant in Figure [2](https://arxiv.org/html/2512.19621v1#S2.F2 "Figure 2 ‣ 2 Oscillations in the density"), possibly
because of the choice of interpolation axis. When applying the cubic spline to log-moneyness yy and variances σ2​(y)\sigma^{2}(y), we end up only with
a slight bimodality, more in-line with (wystup2017arbitrage, Figure 1).
The boundary conditions used for the spline interpolation also play a key role: if we set the first derivative to be zero at the boundaries and use a flat extrapolation, the probability density presents two spurious spikes and goes negative, due to the discontinuities of the second derivative at the 10​Δ10\Delta-Put and Call. If, instead, we set the second derivative to be zero at the boundaries (also called natural cubic spline), along with a linear extrapolation of the same slope, the second derivative is continuous everywhere.

![Refer to caption](x1.png)


Figure 1: Smile and local variance denominator for SVI calibrated to AUD/NZD options expiring in 7 days of of 2014/07/02.

![Refer to caption](x2.png)


Figure 2: Smile and probability density for cubic spline in log-moneyness or Δ\Delta calibrated to AUD/NZD options expiring in 7 days of of 2014/07/02.

Even when the probability density stays positive, spikes at the extrapolation points are undesirable: the numerical Γ\Gamma of vanilla options will present the same spikes and thus leads to vastly inaccurate hedges. In Figure [2](https://arxiv.org/html/2512.19621v1#S2.F2 "Figure 2 ‣ 2 Oscillations in the density"), we also notice that two modes clearly appear in the density, when using the flat extrapolation and a log-moneyness axis, which were almost invisible with the linear extrapolation and a log-moneyness axis. This is another side-effect of the spline boundary conditions.

clark2011foreign suggests to use a polynomial in simple ΔR\Delta\_{R}, as it then does not require the solution of a non-linear problem to lookup the volatility for a given strike.
This is a priori attractive, but it also leads to oscillations.
The oscillations are not limited to this example, but are present for many short term options cases. Figure [3](https://arxiv.org/html/2512.19621v1#S2.F3 "Figure 3 ‣ 2 Oscillations in the density") shows the implied
probability density for options111While unusual, the use of 5-Δ\Delta is sometimes the practice. Here the quotes are directly those of put and call options and may have been calibrated in an external system. on EUR/CZK (Euro vs. Czech Koruna) with 32 days to maturity as of 2019/12/16 (Table [2](https://arxiv.org/html/2512.19621v1#S2.T2 "Table 2 ‣ 2 Oscillations in the density")).
A remedy is to consider a polynomial in ΔF\Delta\_{F} and solve the non-linear problem.

![Refer to caption](x3.png)


Figure 3: Smile and probability density for polynomial in simple or forward Δ\Delta calibrated to EUR/CZK options expiring in 32 days of of 2019/12/16.




Table 2: Options on EUR/CZK expiring in 32 days as of 2019/12/16 in the forward Δ\Delta with premium convention. F​(T)=1.07845F(T)=1.07845, BAUD​(T)=0.999712587139B\_{\textmd{AUD}}(T)=0.999712587139, spot = 1.0784.

| 5Δ\Delta-Put | 25Δ\Delta-Put | ATM | 25Δ\Delta-Call | 5Δ\Delta-Call |
| --- | --- | --- | --- | --- |
| 3.715 | 2.765 | 2.830 | 3.340 | 4.380 |

## 3 Low volatilities

The AED currency (United Arab Emirates Dirham) is pegged to the USD, and exhibits extremely low volatility as a consequence. Surprisingly, there are quotes for FX options on USD/AED. Table [3](https://arxiv.org/html/2512.19621v1#S3.T3 "Table 3 ‣ 3 Low volatilities") presents quotes for two maturities as of 2023/01/24. The problems are similar for the different maturities, and we will consider options expiring in 9 months to illustrate the issues that arise with different interpolations.

Table 3: Quotes for options on USD/AED as of 2023/01/24 in forward Δ\Delta with premium convention. For the 9m maturity, we have F​(T)=3.67206F(T)=3.67206, rUSD​(T)=3.255%r\_{\textmd{USD}}(T)=3.255\%, spot = 3.67. The quotes are converted to Put/Call vanilla vols using the simple approximation.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Maturity | ATM | 25Δ\Delta-RR | 25Δ\Delta-BF | 10Δ\Delta-RR | 10Δ\Delta-BF |
| 1m | 0.31 | 0.142 | 0.078 | 0.343 | 0.142 |
| 9m | 0.32 | 0.152 | 0.084 | 0.412 | 0.392 |
| 1y | 0.29 | 0.132 | 0.072 | 0.359 | 0.343 |
|  | 10Δ\Delta-Put | 25Δ\Delta-Put | ATM | 25Δ\Delta-Call | 10Δ\Delta-Call |
| 9m | 0.506 | 0.328 | 0.32 | 0.48 | 0.918 |

If we fit the exponential polynomial function in Δ¯F\bar{\Delta}\_{F} to those quotes, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ¯F=Φ​(1σ​T​ln⁡(F​(T)/K)),\bar{\Delta}\_{F}=\Phi\left(\frac{1}{\sigma\sqrt{T}}\ln(F(T)/K)\right)\,, |  | (5) |

we need to be careful how to solve the non-linear Equation [1](https://arxiv.org/html/2512.19621v1#S1.E1 "In 1 Introduction") or equivalently Equation [5](https://arxiv.org/html/2512.19621v1#S3.E5 "In 3 Low volatilities"). In particular, the fixed point method described in (wystup2017fx, Section 1.4.9) does not converge. For a strike price of 3.7, the implied Δ¯F\bar{\Delta}\_{F} oscillates between two points: 1.9% and 30.1%, neither are a solution. The implied volatility oscillates as well, Figure [4](https://arxiv.org/html/2512.19621v1#S3.F4 "Figure 4 ‣ 3 Low volatilities") shows the first 32 iterations, increasing the number of iterations does not help. Because of the failure to lookup properly the volatility at a given strike, and we stop the fixed point method at a finite number of iterations, the implied volatility obtained by the fixed point method has a strange shape. Newton or Brent methods work well. We employ Δ¯F\bar{\Delta}\_{F} to make the analysis simpler, but the same observations would hold with ΔF\Delta\_{F}.

![Refer to caption](x4.png)


Figure 4: Smile and convergence of volatility lookup at strike K=3.7K=3.7 of the exponential quartic interpolation for options on USD/AED options expiring in 9 months as of 2023/01/24.

This example also illustrates a negative density with SVI and the constraint222Without the constraint, SVI would actually lead to arbitrage free prices on this example. Yes, it is the reverse as for AUD/NZD. a≥0a\geq 0 (Figure [5](https://arxiv.org/html/2512.19621v1#S3.F5 "Figure 5 ‣ 3 Low volatilities")).

![Refer to caption](x5.png)


Figure 5: Smile and local variance denominator with different interpolations of options on USD/AED options expiring in 9 months as of 2023/01/24.

The extended SSVI (xSSVI) smile is not matching the 25Δ\Delta quotes properly, due to its limited number of parameters and additional constraints that makes the local variance denominator positive. We used the calibration procedure described in (corbetta2019robust).
The exponential quartic polynomial on Δ¯F\bar{\Delta}\_{F} works well when Newton’s method is used. SABR also provides an excellent fit (better than SVI), with a positive density.
The natural cubic spline in ΔF\Delta\_{F} with linear extrapolation leads to negative density at the money.

## 4 Negative volatilities

We consider now options on EUR/TRY of maturity 1 year as of 2022/11/29. The Turkish Lira is particularly volatile, due to the high inflation in Turkey in 2022 and the resulting implied volatility smile has a somewhat unusual shape. We calibrated the vanilla options volatilities using the exponential quartic function on Δ¯F\bar{\Delta}\_{F} (Table [4](https://arxiv.org/html/2512.19621v1#S4.T4 "Table 4 ‣ 4 Negative volatilities")) and fit various smile representations on those vanilla options.

Table 4: Quotes for options on EUR/TRY as of 2022/11/29 in forward Δ\Delta with premium. For the maturity of 184 days, we have rTRY=36.77%r\_{\textmd{TRY}}=36.77\%, rEUR=1.167%r\_{\textmd{EUR}}=1.167\% . For the 1 year maturity, we have rTRY=37.73%r\_{\textmd{TRY}}=37.73\%, rEUR=1.784%r\_{\textmd{EUR}}=1.784\%, spot=19.3483.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Maturity | ATM | 25Δ\Delta-RR | 25Δ\Delta-BF | 10Δ\Delta-RR | 10Δ\Delta-BF |
| 6m | 22.12 | 9.385 | 2.187 | 21.148 | 7.633 |
| 1y | 31.13 | 11.568 | 2.931 | 27.120 | 9.307 |
|  | 10Δ\Delta-Put | 25Δ\Delta-Put | ATM | 25Δ\Delta-Call | 10Δ\Delta-Call |
| 1y | 24.08 | 28.64 | 31.13 | 40.21 | 51.20 |

The exponential polynomial representation suggests a bimodal density (Figure [6](https://arxiv.org/html/2512.19621v1#S4.F6 "Figure 6 ‣ 4 Negative volatilities")). This results in a spike in the probability density of the quintic collocation of lefloch2019model1 (which otherwise behaves well on the other examples considered in this paper) and a corresponding unnatural steep angle in the implied volatilities. SVI and xSSVI do not fit exactly the quotes, but are close enough while providing a smooth unimodal probability density. SABR (not displayed) leads to a similar fit as xSSVI.

![Refer to caption](x6.png)


Figure 6: Smile and probability density with different interpolations of options on EUR/TRY options expiring in 1 year as of 2022/11/29.

It is a priori not obvious that the probability density is truly bimodal, or if bimodality is a consequence of overfitting. In this case, it is likely the latter. More problematic is the natural cubic spline on log-moneyness, which produces negative implied variance, because the slope at the 10Δ\Delta is positive.

## 5 Manufactured example

It is possible to find more awkward examples that break many of the smile parameterization by generating
distributions from a mixture of two lognormal distributions with random333This means 4 random parameters: one weight, one mean, and two volatilities. The sum of weights equals 1 and global mean equals the forward. parameters, calculating implied volatilities for given ΔF\Delta\_{F}, until
some of the parameterization misbehaves. Such an example is provided in Table [5](https://arxiv.org/html/2512.19621v1#S5.T5 "Table 5 ‣ 5 Manufactured example"), for a maturity of 1 year, domestic and foreign rates equal to zero, and a spot price of 1.0. We use a forward Δ\Delta convention without premium. We corrected it a little bit to make it more interesting: the 10Δ\Delta quotes are a flat extrapolation of the 25Δ\Delta quotes.

Table 5: Manufactured option quotes of maturity 1 year. rd=0%r\_{d}=0\%, rf=0%r\_{f}=0\%, spot=1.0.

| 10Δ\Delta-Put | 25Δ\Delta-Put | ATM | 25Δ\Delta-Call | 10Δ\Delta-Call |
| --- | --- | --- | --- | --- |
| 26.00 | 26.00 | 19.50 | 12.70 | 12.70 |

SABR and xSSVI do not fit well but leads to similarly reasonable smiles given the awkward quotes. The SVI smile looks more odd, with a strong angle. A remedy would be to increase its ss parameter. The exponential polynomial on Δ\Delta leads to a negative density (Figure [7](https://arxiv.org/html/2512.19621v1#S5.F7 "Figure 7 ‣ 5 Manufactured example")). Cubic splines in log-moneyness or ΔF\Delta\_{F} (not displayed) also result in a negative density. Finally, the quadratic local variance gamma (LVG) of lefloch2023quadratic allows to fit the quotes very well, with a positive density.

![Refer to caption](x7.png)


Figure 7: Smile and probability density with different interpolations of manufactured options quotes.

We stress that the original quotes do not have any arbitrage. They may serve as a warning against flat extrapolation, and especially against adding fictitious flatly extrapolated quotes. The latter often leads to a multi-modal implied probability density.

## 6 Wings control

Table [6](https://arxiv.org/html/2512.19621v1#S6.T6 "Table 6 ‣ 6 Wings control") presents the implied volatilities for a dense range of vanilla put and call forward Δ\Delta for options on EURUSD of maturity 1 month as of 2022/03/11, as may be retrieved from a market data provider such as Reuters or SuperDerivatives (wystup2017fx, Section 1.5.9).

Table 6: EURUSD option vols of maturity 1 month as of 2022/03/11 in forward Δ\Delta without premium convention. F​(T)=0.975848F(T)=0.975848, rUSD=0.351836%r\_{\textmd{USD}}=0.351836\%, spot=0.9759.

| 1 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | (P) ATM (C) | 40 | 35 | 30 | 25 | 20 | 15 | 10 | 5 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14.04 | 13.01 | 12.47 | 12.16 | 11.93 | 11.73 | 11.54 | 11.38 | 11.25 | 11.02 | 10.85 | 10.78 | 10.73 | 10.68 | 10.63 | 10.58 | 10.51 | 10.45 | 11.11 |

We fit the various smile representations to the 5 usual option quotes (ATM, 25Δ\Delta and 10Δ\Delta). They have no problem matching those 5 quotes, but their wings differ significantly. Figure [8](https://arxiv.org/html/2512.19621v1#S6.F8 "Figure 8 ‣ 6 Wings control") shows that the extrapolation with Δ\Delta based interpolations such as the exponential polynomial in Δ¯F\bar{\Delta}\_{F} looks too flat compared to what is quoted by the provider. The left (put) wing of SVI looks good, but the right (call) wing is not as good, although it concerns only one observation: the 1Δ\Delta-Call, which may not be very liquid. SABR and xSVVI are
very similar and have reasonable left and right wings, while LVG leads to a good fit of the right and left wings.

![Refer to caption](x8.png)


Figure 8: Smile with different interpolations fitted to the 5 usual options quotes of maturity 1 month, for EURUSD as of as of 2022/03/11.

![Refer to caption](x9.png)


Figure 9: Smile with different interpolations fitted to the 5 usual options quotes of maturity 1 year, for EURUSD as of as of 2022/03/11.

It is enlightening to look at the case of options maturing in one year (Table [7](https://arxiv.org/html/2512.19621v1#S6.T7 "Table 7 ‣ 6 Wings control") and Figure [9](https://arxiv.org/html/2512.19621v1#S6.F9 "Figure 9 ‣ 6 Wings control")). The exponential polynomial in Δ\Delta looks better, although still too flat in the left wing and SVI is best.

Table 7: EURUSD option vols of maturity 1 year as of 2022/03/11 in forward Δ\Delta without premium convention. F​(T)=0.986772F(T)=0.986772, BUSD​(T)=0.963113%B\_{\textmd{USD}}(T)=0.963113\%, spot=0.9759.

| 1 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | (P) ATM (C) | 40 | 35 | 30 | 25 | 20 | 15 | 10 | 5 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16.0 | 14.57 | 13.46 | 12.73 | 12.19 | 11.74 | 11.32 | 10.96 | 10.65 | 10.19 | 9.84 | 9.68 | 9.57 | 9.48 | 9.4 | 9.31 | 9.21 | 9.02 | 8.87 |

wystup2023slope explains how much extrapolation can play a role in the prices of digital options. There are other important basic use cases where extrapolation play a role: auto-quantos and variance swaps. An auto-quanto option on EUR/USD is the same as a regular vanilla option on EUR/USD except for the payment currency: the auto-quanto pays out the amount max⁡(±(S​(T)−K),0)\max\left(\pm(S(T)-K),0\right) in EUR (foreign currency), for a call (resp. a put). This is equivalent to an option on max⁡(±(S​(T)−K),0)​S​(T)\max\left(\pm(S(T)-K),0\right)S(T) in USD (domestic currency). The latter can be priced by replication of vanilla options (castagna2010fx, Section 7.5):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cauto-quanto​(K,T)=2​∫K∞C​(K,T)​d​K+K​C​(K,T),Pauto-quanto​(K,T)=−2​∫0KP​(K,T)​d​K+K​P​(K,T),\displaystyle C\_{\textmd{auto-quanto}}(K,T)=2\int\_{K}^{\infty}C(K,T)\mathop{}\!\kern 0.0pt\mathrm{d}K+KC(K,T)\,,\quad P\_{\textmd{auto-quanto}}(K,T)=-2\int\_{0}^{K}P(K,T)\mathop{}\!\kern 0.0pt\mathrm{d}K+KP(K,T)\,, |  | (6) |

where C​(K,T)C(K,T) and P​(K,T)P(K,T) are call and put options of maturity TT and strike KK.
Due to the flat wings, the Δ\Delta based smiles will undervalue the auto-quanto call options and overvalue the put. For the EUR/USD options with maturity 1 year, the impact is around 3% of the option price for strikes at 10​Δ10\Delta (Table [8](https://arxiv.org/html/2512.19621v1#S6.T8 "Table 8 ‣ 6 Wings control")), with a larger discrepancy for the
put. The discrepancy is of course much more significant if we are in the extrapolation part, for example for strikes at 1​Δ1\Delta, it is a factor of 2: even larger than digitals.

The price of a newly issued variance swap, which uses a replication of vanilla options across all strikes may also be impacted.
If we use the approach of doi:10.1142/S0219024911006681, and only the 5 reference quotes, we end up with a model independent price of 11.28 (in terms of vol444The present value of the variance swap contract is the square of the vol price.) for the 1 month and 11.20 for the 1 year maturity. This is quite close to the prices obtained by replicating on a dense range of options with strikes spanning over 5 standard deviations from the forward, with the various smile representations (Table [8](https://arxiv.org/html/2512.19621v1#S6.T8 "Table 8 ‣ 6 Wings control")). The smile representation has a negligible impact for the 1 month maturity, and reaches up to 3% of the variance swap present value for the 1 year maturity. This due to the representation of the left wing, which plays a more important role than the right wing for variance swaps, due to the 1/K21/K^{2} weighting in the replication.

Table 8: Prices derivative contracts on EUR/USD for a notional of 10,000 as of 2022/03/11, using different smile representations. For the 1-month maturity, the 10​Δ10\Delta Put and Call strikes are K10,P=0.93274K\_{10,P}=0.93274, K10,C=1.014727K\_{10,C}=1.014727 and the 1​Δ1\Delta strikes are K1,P=0.889339K\_{1,P}=0.889339, K1,C=1.051435K\_{1,C}=1.051435.

| Maturity | Option type | Strike | Polynomial Δ\Delta | SVI | xSSVI | SABR | LVG |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1m | Digital Put | K10,PK\_{10,P} | 1063.88 | 1064.91 | 1067.09 | 1066.47 | 1063.88 |
|  |  | K1,PK\_{1,P} | 70.76 | 108.69 | 122.34 | 125.44 | 132.10 |
|  | Auto-quanto Call | K10,CK\_{10,C} | 14.28 | 14.34 | 14.37 | 14.31 | 14.33 |
|  |  | K1,CK\_{1,C} | 0.60 | 0.63 | 0.86 | 0.81 | 1.04 |
|  | Auto-quanto Put | K10,PK\_{10,P} | 15.12 | 15.07 | 15.09 | 15.07 | 15.00 |
|  |  | K1,PK\_{1,P} | 0.66 | 1.13 | 1.30 | 1.34 | 1.43 |
|  | Variance swap | 0 | 11.31 | 11.35 | 11.37 | 11.39 | 11.41 |
| 1y | Digital Put | K10,PK\_{10,P} | 1210.64 | 1211.74 | 1215.64 | 1269.08 | 1210.64 |
|  |  | K1,PK\_{1,P} | 101.21 | 185.30 | 204.72 | 232.28 | 232.82 |
|  | Auto-quanto Call | K10,CK\_{10,C} | 47.86 | 48.24 | 49.06 | 48.49 | 48.17 |
|  |  | K1,CK\_{1,C} | 4.21 | 4.39 | 6.97 | 6.80 | 5.60 |
|  | Auto-quanto Put | K10,PK\_{10,P} | 46.39 | 44.92 | 44.72 | 44.14 | 44.20 |
|  |  | K1,PK\_{1,P} | 2.14 | 4.27 | 4.80 | 5.47 | 4.97 |
|  | Variance swap | 0 | 10.89 | 11.03 | 11.07 | 11.16 | 11.10 |

## 7 Conclusion

Using a cubic spline is dangerous, natural boundaries and log-moneyness axis should be favored. Beside the possibility of negative or oscillating implied probability density, the natural cubic spline in log-moneyness suffers from the more important issue of a possible positive slope for the put wing extrapolation, which will need to be dealt with in a likely awkward way.
Interpolations in Δ\Delta space lead in general to too flat wings, and may misprice auto-quanto options and variance swaps of long maturities, as well as digital options beyond the 10​Δ10\Delta strikes. Another take-away, if you were to use a Δ\Delta based representation nonetheless is: don’t use the fixed-point method to lookup the volatility at a given strike.

While SVI makes sense for FX smiles, the occasional SVI arbitrages still need to be dealt with, possibly with a recalibration with a penalty. In this regard, xSSVI is attractive but may fit poorly 10​Δ10\Delta quotes in some cases. SABR was found to be similar to xSSVI in terms of fit and did not lead to negative density issues on the examples considered, but it is not guaranteed to be arbitrage-free, especially at the surface level, across maturities.
The quadratic local variance gamma model was found to provide a flexible arbitrage-free interpolation, at the cost of a more complex implementation.

In this article, the smile representations were fitted directly to vanilla option quotes, we will explore the role and impact of interpolation during the calibration to broker quotes in a follow-up article.

###### Acknowledgements.

The author would like to thank Dr. Gary Kennedy and Dr. Fabien Le Floc’h for fruitful conversations and feedback on early drafts of this paper.
\externalbibliographyyes
\appendixtitlesno