---
authors:
- Tim Leung
- Matthew Lorig
doc_id: arxiv:2602.00858v1
family_id: arxiv:2602.00858
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Short-Rate-Dependent Volatility Models
url_abs: http://arxiv.org/abs/2602.00858v1
url_html: https://arxiv.org/html/2602.00858v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tim Leung
Department of Applied Mathematics, University of Washington. e-mail: <timleung@uw.edu>
  
Matthew Lorig
Department of Applied Mathematics, University of Washington. e-mail: <mlorig@uw.edu>

(This version: )

###### Abstract

We price European options in a class of models in which the volatility of the underlying risky asset depends on the short rate of interest.
Our study results in an explicit pricing formula that depends on knowledge of a characteristic function.
We provide examples of models in which the characteristic function can be computed analytically and, thus, the value of European options is explicit. Numerical implementation to produce the implied volatility is also presented.

Keywords: short rate model, interest rate, stochastic volatility, CIR process, Jacobi process.

## 1 Introduction

Monetary policy easing by the Federal Reserve — most visibly through reductions in the target federal funds rate — has long been recognized as a catalyst for movements in risk-bearing assets. Early work highlighted the transmission channel from lower short term rates to higher equity valuations via discounted cash flow effects and a shift in investor risk appetite [Bernanke, [2005](https://arxiv.org/html/2602.00858v1#bib.bib3)]. More recent empirical studies have shown that the very act of cutting rates also coincides with a measurable rise in market uncertainty, as captured by the CBOE Volatility Index (VIX). Gürkaynak et al. [[2005](https://arxiv.org/html/2602.00858v1#bib.bib6)] document a statistically significant increase in implied volatility in the days surrounding Fed rate-cut announcements, suggesting that markets anticipate heightened future dispersion in returns.
  
The relationship between monetary easing and volatility is not merely a short‑run phenomenon. Bekaert and Hoerova [[2014](https://arxiv.org/html/2602.00858v1#bib.bib2)] demonstrate that periods of accommodative policy are associated with sustained elevations in the VIX, reflecting a broader reallocation toward riskier assets and the attendant amplification of price swings. Complementary evidence from the post-Great Recession era indicates that each successive rate cut tends to generate a larger incremental jump in the VIX, possibly because investors interpret repeated easing as a signal of deteriorating macroeconomic conditions [Liu et al., [2022](https://arxiv.org/html/2602.00858v1#bib.bib8)]. Moreover, high-frequency analyses reveal that the announcement effect alone accounts for a sizable fraction of daily VIX spikes, independent of contemporaneous macro news releases [Anderson et al., [2020](https://arxiv.org/html/2602.00858v1#bib.bib1)].
  
In this paper we present a market model in which the volatility of a risky asset depends on the short rate of interest. In this setting, we provide an explicit formula to price European options up to a characteristic function. Although our framework is flexible enough to allow for the volatility of the risky asset to be either positively or negatively correlated with the short rate, consistent with the literature above, we present two examples in which volatility is negatively correlated in the short rate and in which the characteristic function needed to price options can be computed explicitly.
  
The rest of this paper proceeds as follows:
in Section [2](https://arxiv.org/html/2602.00858v1#S2 "2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models"), we present a general class of models for the short rate of interest and a risky asset.
In Section [3](https://arxiv.org/html/2602.00858v1#S3 "3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models"), we derive an explicit formula, written in terms of a characteristic function, for the price of a European-style financial derivative written on the risky asset.
The special case of a European call, from which implied volatility is defined, is treated in Section [4](https://arxiv.org/html/2602.00858v1#S4 "4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models").
Section [5](https://arxiv.org/html/2602.00858v1#S5 "5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models") focuses on the setting in which the short rate is driven by a Cox-Ingersoll-Ross (CIR) process Cox et al. [[1985](https://arxiv.org/html/2602.00858v1#bib.bib4)].
And, Section [6](https://arxiv.org/html/2602.00858v1#S6 "6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models") examines the case in which the short rate is driven by a Jacobi diffusion Delbaen and Shirakawa [[2002](https://arxiv.org/html/2602.00858v1#bib.bib5)].
In both the CIR-driven and Jacobi-driven settings, the characteristic function needed to price European claims can be computed explicitly.
Some concluding remarks are offered in Section [7](https://arxiv.org/html/2602.00858v1#S7 "7 Conclusion ‣ Short-Rate-Dependent Volatility Models").

## 2 A general class of short-rate-dependent volatility models

To begin, we fix a time horizon <∞\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}<\infty and consider a continuous-time financial market, defined on a filtered probability space (Ω,,,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\Omegaup,\mathscr{{\mst@F\/}},\mathds{{\mst@F\/}},\mathds{{\mst@P\/}}) with no arbitrage and no transaction costs. The probability measure represents the market’s chosen pricing measure taking the money market account =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@M\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} as numéraire. The filtration =(t)0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathds{{\mst@F\/}}=(\mathscr{{\mst@F\/}}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} represents the history of the market.
  
We suppose that the money market account is strictly positive, continuous and non-decreasing. As such, there exists a non-negative -adapted short rate process =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@R\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} such that the money market account satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =dtt​t​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={}\_{\mst@t}{}\_{\mst@t}\,\mathrm{{\mst@d}}{\mst@t}. |  | (1) |

We will focus on the case in which the dynamics of the short rate and the price of a risky asset =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@S\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} are of the form

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | t | =r()t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@r}({}\_{\mst@t}), | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =b()tdt+a()td,t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@b}({}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}+{\mst@a}({}\_{\mst@t})\mathrm{{\mst@d}}{}\_{\mst@t}, |  | (2) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | t | =et,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{{}\_{\mst@t}}, | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(r()t−12c2()t)dt+c()t(ρd+tρ¯d)t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({\mst@r}({}\_{\mst@t})-\tfrac{1}{2}{\mst@c}^{2}({}\_{\mst@t})\Big)\mathrm{{\mst@d}}{\mst@t}+{\mst@c}({}\_{\mst@t})\Big(\rhoup\mathrm{{\mst@d}}{}\_{\mst@t}+\bar{\rhoup}\mathrm{{\mst@d}}{}\_{\mst@t}\Big), |  | (3) |

where =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@W\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} and =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@B\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} are independent (,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\mathds{{\mst@P\/}},\mathds{{\mst@F\/}})-Brownian motions and ρ¯:=1−ρ2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\bar{\rhoup}:=\sqrt{1-\rhoup^{2}} with —​ρ​—≤1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar|\rhoup|\leq 1. We shall refer to the process =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@Y\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} as the driver of the short rate due to the fact that =r​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@R\/}={\mst@r}({\mst@Y\/}). Though, one can also think of as the driver of the volatility of the log\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\log-price , which is given by c​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}({\mst@Y\/}) in ([3](https://arxiv.org/html/2602.00858v1#S2.E3 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")).
  
Throughout this paper, we will assume the following:

###### Assumption 1.

Henceforth:

* (i)

  The functions (a,b,c,r)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@a},{\mst@b},{\mst@c},{\mst@r}) are such that SDEs ([2](https://arxiv.org/html/2602.00858v1#S2.E2 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models"))–([3](https://arxiv.org/html/2602.00858v1#S2.E3 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")) admit a unique strong solution on [0,]\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar[0,{\mst@T\/}] and, for some p>2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@p}>2, we have

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | [sup0≤t≤(—​—pt+—​—pt)]\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathds{{\mst@E\/}}\Big[\sup\_{0\leq{\mst@t}\leq{\mst@T\/}}\big(|{}\_{\mst@t}|^{\mst@p}+|{}\_{\mst@t}|^{\mst@p}\big)\Big] | <∞​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle<\infty. |  | (4) |
* (ii)

  For all t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@t}\leq{\mst@T\/}, the short rate satisfies =tr()t≥0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}\_{\mst@t}={\mst@r}({}\_{\mst@t})\geq 0, the process ∈t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}\_{\mst@t}\in\mathds{{\mst@R\/}} and (/t)t<∞\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathds{{\mst@E\/}}({}\_{\mst@t}/{}\_{\mst@t})<\infty.

Under Assumption [1](https://arxiv.org/html/2602.00858v1#Thmtheorem1 "Assumption 1. ‣ 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models"), the process /\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@S\/}/{\mst@M\/} is a (,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\mathds{{\mst@P\/}},\mathds{{\mst@F\/}})-martingale, as it must be in the absence of arbitrage.

## 3 Pricing of European-style claims

Now, consider a European derivative that pays φ​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup() at time . The value =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@V\/}=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} of this derivative satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | tt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\frac{{}\_{\mst@t}}{{}\_{\mst@t}} | =t=tφ​(),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathds{{\mst@E\/}}\_{\mst@t}\frac{}{}=\mathds{{\mst@E\/}}\_{\mst@t}\frac{\phiup()}{}, |  | (5) |

where we have introduced the short-hand notation t⋅:=(⋅—t)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathds{{\mst@E\/}}\_{\mst@t}\,\cdot\,:=\mathds{{\mst@E\/}}(\,\cdot\,|\mathscr{{\mst@F\/}}\_{\mst@t}). From ([5](https://arxiv.org/html/2602.00858v1#S3.E5 "In 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) we deduce that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | t | =te−∫tr()sds​φ​()​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\phiup(). |  | (6) |

In order to find an explicit expression for t the following lemma will be helpful.

###### Lemma 2.

Fix ω∈\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\omegaup\in\mathds{{\mst@C\/}} and suppose

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | exp(12∫0—−𝚒ωρc()s—2ds)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathds{{\mst@E\/}}\exp\Big(\frac{1}{2}\int\_{0}|-\mathtt{{\mst@i}}\omegaup\rhoup\,{\mst@c}({}\_{\mst@s})|^{2}\mathrm{{\mst@d}}{\mst@s}\Big) | <∞​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle<\infty. |  | (7) |

Consider the following (complex-valued) change of measure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​~d\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\frac{\mathrm{{\mst@d}}\widetilde{\mathds{{\mst@P\/}}}}{\mathrm{{\mst@d}}\mathds{{\mst@P\/}}} | :=e−∫0(−𝚒ωρc()s)d−s12∫0(−𝚒ωρc()s)2ds​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\mathrm{{\mst@e}}^{-\int\_{0}(-\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s}))\mathrm{{\mst@d}}{}\_{\mst@s}-\frac{1}{2}\int\_{0}(-\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s}))^{2}\mathrm{{\mst@d}}{\mst@s}}. |  | (8) |

Then the dynamics of under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(b()t+𝚒ωρa()tc()t)dt+a()td~t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({\mst@b}({}\_{\mst@t})+\mathtt{{\mst@i}}\omegaup\rhoup{\mst@a}({}\_{\mst@t}){\mst@c}({}\_{\mst@t})\Big)\mathrm{{\mst@d}}{\mst@t}+{\mst@a}({}\_{\mst@t})\mathrm{{\mst@d}}\widetilde{{\mst@W\/}}\_{\mst@t}, |  | (9) |

where the process ~=(~t)0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{{\mst@W\/}}=(\widetilde{{\mst@W\/}}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}} is a (~,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\widetilde{\mathds{{\mst@P\/}}},\mathds{{\mst@F\/}})-Brownian motion and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | te−∫tr()sds+𝚒ω\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\mathtt{{\mst@i}}\omegaup} | =e𝚒ωt(t,;t,1−𝚒ω,𝚒ω/2+ω2/2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},1-\mathtt{{\mst@i}}\omegaup,\mathtt{{\mst@i}}\omegaup/2+\omegaup^{2}/2), |  | (10) |

where the function is defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (t,y;,w,z)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@G\/}({\mst@t},{\mst@y};{\mst@T\/},{\mst@w},{\mst@z}) | :=~(e−w∫tr()sds−z∫tc2()sds—=ty).\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\widetilde{\mathds{{\mst@E\/}}}\Big(\mathrm{{\mst@e}}^{-{\mst@w}\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}-{\mst@z}\int\_{\mst@t}{\mst@c}^{2}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\,\Big|\,{}\_{\mst@t}={\mst@y}\Big). |  | (11) |

with ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@E\/}}} denoting expectation under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}}.

###### Proof.

By Assumption [1](https://arxiv.org/html/2602.00858v1#Thmtheorem1 "Assumption 1. ‣ 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")(i), the process c​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}({\mst@Y\/}) is progressively measurable and
∫0—c()s—2ds<∞\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathds{{\mst@E\/}}\int\_{0}|{\mst@c}({}\_{\mst@s})|^{2}\mathrm{{\mst@d}}{\mst@s}<\infty, so the stochastic integral
∫0(−𝚒ωρc()s)ds\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\int\_{0}(-\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s}))\mathrm{{\mst@d}}{}\_{\mst@s} is well-defined.
The condition ([7](https://arxiv.org/html/2602.00858v1#S3.E7 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) is Novikov’s criterion, which implies that the stochastic exponential in ([8](https://arxiv.org/html/2602.00858v1#S3.E8 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) is a true martingale with expectation one. Thus (d​~/d)=1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathds{{\mst@E\/}}(\mathrm{{\mst@d}}\widetilde{\mathds{{\mst@P\/}}}/\mathrm{{\mst@d}}\mathds{{\mst@P\/}})=1, and ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} is a probability measure equivalent to .
  
Next, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | te−∫tr()sds+𝚒ω\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\mathtt{{\mst@i}}\omegaup} |  | (12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =et𝚒ωt​e−∫tr()sds+𝚒ω(−)t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\mathtt{{\mst@i}}\omegaup(-{}\_{\mst@t})} |  | (13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =et𝚒ωt​e−∫tr()sds+𝚒ω∫t(r()s−12c2()s)ds+𝚒ω∫tc()s(ρd+sρ¯d)s\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\mathtt{{\mst@i}}\omegaup\int\_{\mst@t}({\mst@r}({}\_{\mst@s})-\tfrac{1}{2}{\mst@c}^{2}({}\_{\mst@s}))\mathrm{{\mst@d}}{\mst@s}+\mathtt{{\mst@i}}\omegaup\int\_{\mst@t}{\mst@c}({}\_{\mst@s})(\rhoup\mathrm{{\mst@d}}{}\_{\mst@s}+\bar{\rhoup}\mathrm{{\mst@d}}{}\_{\mst@s})} |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =et𝚒ωtet−(1−𝚒ω)∫tr()sds−𝚒​ω2∫tc2()sds+∫t𝚒ωρc()sds(e∫t𝚒ωρ¯c()sds—,s0≤s≤)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-(1-\mathtt{{\mst@i}}\omegaup)\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}-\frac{\mathtt{{\mst@i}}\omegaup}{2}\int\_{\mst@t}{\mst@c}^{2}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\int\_{\mst@t}\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s})\mathrm{{\mst@d}}{}\_{\mst@s}}\mathds{{\mst@E\/}}\_{\mst@t}\!\Big(\mathrm{{\mst@e}}^{\int\_{\mst@t}\mathtt{{\mst@i}}\omegaup\bar{\rhoup}{\mst@c}({}\_{\mst@s})\mathrm{{\mst@d}}{}\_{\mst@s}}\,\Big|\,{}\_{\mst@s},0\leq{\mst@s}\leq{\mst@T\/}\Big) |  | (15) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =et𝚒ωt​e−(1−𝚒ω)∫tr()sds−(𝚒​ω2+ρ¯2​ω22)∫tc2()sds+∫t𝚒ωρc()sds\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-(1-\mathtt{{\mst@i}}\omegaup)\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}-(\frac{\mathtt{{\mst@i}}\omegaup}{2}+\frac{\bar{\rhoup}^{2}\omegaup^{2}}{2})\int\_{\mst@t}{\mst@c}^{2}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\int\_{\mst@t}\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s})\mathrm{{\mst@d}}{}\_{\mst@s}} |  | (16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =et𝚒ωt​e−(1−𝚒ω)∫tr()sds−(𝚒​ω2+ρ¯2​ω22+ρ2​ω22)∫tc2()sds−∫t(−𝚒ωρc()s)d−s12∫t(−𝚒ωρc()s)2ds\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-(1-\mathtt{{\mst@i}}\omegaup)\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}-(\frac{\mathtt{{\mst@i}}\omegaup}{2}+\frac{\bar{\rhoup}^{2}\omegaup^{2}}{2}+\frac{\rhoup^{2}\omegaup^{2}}{2})\int\_{\mst@t}{\mst@c}^{2}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}-\int\_{\mst@t}(-\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s}))\mathrm{{\mst@d}}{}\_{\mst@s}-\frac{1}{2}\int\_{\mst@t}(-\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@s}))^{2}\mathrm{{\mst@d}}{\mst@s}} |  | (17) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =e𝚒ωt​~t​e−(1−𝚒ω)∫tr()sds−(𝚒​ω2+ω22)∫tc2()sds\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}\widetilde{\mathds{{\mst@E\/}}}\_{\mst@t}\mathrm{{\mst@e}}^{-(1-\mathtt{{\mst@i}}\omegaup)\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}-(\frac{\mathtt{{\mst@i}}\omegaup}{2}+\frac{\omegaup^{2}}{2})\int\_{\mst@t}{\mst@c}^{2}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}} |  | (18) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =e𝚒ωt(t,;t,1−𝚒ω,𝚒ω/2+ω2/2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},1-\mathtt{{\mst@i}}\omegaup,\mathtt{{\mst@i}}\omegaup/2+\omegaup^{2}/2), |  | (19) |

where the second-to-last equality follows from ([8](https://arxiv.org/html/2602.00858v1#S3.E8 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), the last equality follows from ([11](https://arxiv.org/html/2602.00858v1#S3.E11 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), and the existence of the function is guaranteed by the Markov property of (which holds under Assumption [1](https://arxiv.org/html/2602.00858v1#Thmtheorem1 "Assumption 1. ‣ 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")(i)).
  
Next, noting from Girsanov’s Theorem that the process ~=(~t)0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{{\mst@W\/}}=(\widetilde{{\mst@W\/}}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}}, defined by

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | d​~t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}\widetilde{{\mst@W\/}}\_{\mst@t} | =d−t𝚒ωρc()tdt,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@d}}{}\_{\mst@t}-\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}, | ~0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{{\mst@W\/}}\_{0} | =0,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=0, |  | (20) |

is a Brownian motion under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}}, we see from ([2](https://arxiv.org/html/2602.00858v1#S2.E2 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")) that the dynamics of under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =b()tdt+a()t(d~t+𝚒ωρc()tdt),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@b}({}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}+{\mst@a}({}\_{\mst@t})\Big(\mathrm{{\mst@d}}\widetilde{{\mst@W\/}}\_{\mst@t}+\mathtt{{\mst@i}}\omegaup\rhoup{\mst@c}({}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}\Big), |  | (21) |

which, after grouping the d​t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathrm{{\mst@d}}{\mst@t}-terms, is equivalent to ([9](https://arxiv.org/html/2602.00858v1#S3.E9 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")).
∎

It will be convenient at this point to introduce the generalized Fourier transform and inverse Fourier transform of φ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup.
Assuming φ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup is continuous and eωi​x​φ​(x)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathrm{{\mst@e}}^{\omegaup\_{\mst@i}{\mst@x}}\phiup({\mst@x}) is integrable for some ωi∈\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\omegaup\_{\mst@i}\in\mathds{{\mst@R\/}} we have

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Fourier Transform:\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\textbf{Fourier Transform}: | [φ]​(ω)≡φ^​(ω)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@F\/}[\phiup](\omegaup)\equiv\widehat{\phiup}(\omegaup) | :=∫d​x​φ​(x)​e−𝚒​ω​x,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\int\mathrm{{\mst@d}}{\mst@x}\,\phiup({\mst@x})\mathrm{{\mst@e}}^{-\mathtt{{\mst@i}}\omegaup{\mst@x}}, | ω\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\omegaup | =ωr+𝚒​ωi,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\omegaup\_{\mst@r}+\mathtt{{\mst@i}}\omegaup\_{\mst@i}, | ωr,ωi\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\omegaup\_{\mst@r},\omegaup\_{\mst@i} | ∈,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\in\mathds{{\mst@R\/}}, |  | (22) |
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Inverse Transform:\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\textbf{Inverse Transform}: | [φ^]−1(x)≡φ(x)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{}^{-1}[\widehat{\phiup}]({\mst@x})\equiv\phiup({\mst@x}) | =∫d​ωr2​π​φ^​(ω)​e𝚒​ω​x​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\int\frac{\mathrm{{\mst@d}}\omegaup\_{\mst@r}}{2\piup}\widehat{\phiup}(\omegaup)\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{\mst@x}}. |  | | | | | (23) |

We can now give an explicit expression for the time t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@t} value t of an option that pays φ​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup() at time .

###### Theorem 3.

Consider a derivative that pays φ​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup() at time . Suppose Assumption [1](https://arxiv.org/html/2602.00858v1#Thmtheorem1 "Assumption 1. ‣ 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models") holds, and assume there exists ωi∈\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\omegaup\_{\mst@i}\in\mathds{{\mst@R\/}} such that

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | eωi​x​φ​(x)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@e}}^{\omegaup\_{\mst@i}{\mst@x}}\phiup({\mst@x}) | ∈()1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\in{}^{1}(\mathds{{\mst@R\/}}) | and | [e−∫0r()sds​eωi]\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathds{{\mst@E\/}}\Big[\mathrm{{\mst@e}}^{-\int\_{0}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\,\mathrm{{\mst@e}}^{\omegaup\_{\mst@i}}\Big] | <∞​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle<\infty. |  | (24) |

Consider the vertical line {ω=ωr+𝚒ωi:ωr∈}\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\{\omegaup=\omegaup\_{\mst@r}+\mathtt{{\mst@i}}\omegaup\_{\mst@i}:\omegaup\_{\mst@r}\in\mathds{{\mst@R\/}}\} and assume for each ω=ωr+𝚒​ωi\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\omegaup=\omegaup\_{\mst@r}+\mathtt{{\mst@i}}\omegaup\_{\mst@i} on this line the Novikov condition ([7](https://arxiv.org/html/2602.00858v1#S3.E7 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) holds so that Lemma [2](https://arxiv.org/html/2602.00858v1#Thmtheorem2 "Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models") applies.
Denote by φ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{\phiup} the generalized Fourier transform of φ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup as in ([22](https://arxiv.org/html/2602.00858v1#S3.E22 "In 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")). Then the value of the derivative satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | t | =∫d​ωr2​πφ^(ω)e𝚒ωt(t,;t,1−𝚒ω,ω2/2+𝚒ω/2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\int\frac{\mathrm{{\mst@d}}\omegaup\_{\mst@r}}{2\piup}\widehat{\phiup}(\omegaup)\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},1-\mathtt{{\mst@i}}\omegaup,\omegaup^{2}/2+\mathtt{{\mst@i}}\omegaup/2), |  | (25) |

where the function is given by ([11](https://arxiv.org/html/2602.00858v1#S3.E11 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")).

###### Proof.

Inserting ([23](https://arxiv.org/html/2602.00858v1#S3.E23 "In 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) into ([6](https://arxiv.org/html/2602.00858v1#S3.E6 "In 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | t | =te−∫tr()sds​φ​()=te−∫tr()sds​∫d​ωr2​π​φ^​(ω)​e𝚒​ω​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\phiup()=\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\int\frac{\mathrm{{\mst@d}}\omegaup\_{\mst@r}}{2\piup}\widehat{\phiup}(\omegaup)\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup}. |  | (26) |

From ([24](https://arxiv.org/html/2602.00858v1#S3.E24 "In Theorem 3. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")),
the map
ωr↦φ^​(ω)​e−∫tr()sds​eωi\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\omegaup\_{\mst@r}\mapsto\widehat{\phiup}(\omegaup)\,\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\mathrm{{\mst@e}}^{\omegaup\_{\mst@i}} is integrable, and
t[e−∫tr()sdseωi]<∞\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathds{{\mst@E\/}}\_{\mst@t}\big[\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}\mathrm{{\mst@e}}^{\omegaup\_{\mst@i}}\big]<\infty.
Thus, we may apply Fubini’s theorem to interchange expectation and integration:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | t | =∫d​ωr2​π​φ^​(ω)t​e−∫tr()sds+𝚒ω​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\int\frac{\mathrm{{\mst@d}}\omegaup\_{\mst@r}}{2\piup}\widehat{\phiup}(\omegaup)\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}+\mathtt{{\mst@i}}\omegaup}. |  | (27) |

For each such ω\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\omegaup in the vertical line {ω=ωr+𝚒ωi:ωr∈}\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\{\omegaup=\omegaup\_{\mst@r}+\mathtt{{\mst@i}}\omegaup\_{\mst@i}:\omegaup\_{\mst@r}\in\mathds{{\mst@R\/}}\}, the Novikov condition ([7](https://arxiv.org/html/2602.00858v1#S3.E7 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) holds by assumption, so Lemma [2](https://arxiv.org/html/2602.00858v1#Thmtheorem2 "Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models") applies. Inserting ([10](https://arxiv.org/html/2602.00858v1#S3.E10 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) into ([27](https://arxiv.org/html/2602.00858v1#S3.E27 "In Proof. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), we obtain ([25](https://arxiv.org/html/2602.00858v1#S3.E25 "In Theorem 3. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")).
∎

We see from ([25](https://arxiv.org/html/2602.00858v1#S3.E25 "In Theorem 3. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) that, to price an option, we require an explicit expression for the function . We will provide such an expression in Sections [5](https://arxiv.org/html/2602.00858v1#S5 "5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models") and [6](https://arxiv.org/html/2602.00858v1#S6 "6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models"), when we study specific models for (,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@R\/},{\mst@S\/}). But, first, we review some important definitions related to call options and implied volatility.

## 4 Call options and Implied Volatility

Perhaps the most widely-traded European derivative is that of a call option, which has a payoff function φ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | φ​(x)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\phiup({\mst@x}) | =(ex−)+,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=(\mathrm{{\mst@e}}^{{\mst@x}}-{\mst@K\/})^{+}, |  | (28) |

where is the strike. Inserting ([28](https://arxiv.org/html/2602.00858v1#S4.E28 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")) into ([22](https://arxiv.org/html/2602.00858v1#S3.E22 "In 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), we obtain

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | φ^​(x)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widehat{\phiup}({\mst@x}) | =−1−𝚒​ωω2+𝚒​ω,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{-{}^{1-\mathtt{{\mst@i}}\omegaup}}{\omegaup^{2}+\mathtt{{\mst@i}}\omegaup}, | ωi\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\omegaup\_{\mst@i} | <−1​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle<-1. |  | (29) |

The price of a call option, denoted (,)=((,)t)0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@C\/}({\mst@T\/},{\mst@K\/})=({}\_{\mst@t}({\mst@T\/},{\mst@K\/}))\_{0\leq{\mst@t}\leq{\mst@T\/}}, is then obtained by inserting ([29](https://arxiv.org/html/2602.00858v1#S4.E29 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")) into ([25](https://arxiv.org/html/2602.00858v1#S3.E25 "In Theorem 3. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")). We have

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (,)t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{}\_{\mst@t}({\mst@T\/},{\mst@K\/}) | =∫d​ωr2​π(−1−𝚒​ωω2+𝚒​ω)e𝚒ωt(t,;t,1−𝚒ω,ω2/2+𝚒ω/2)=:(t,,t;t,),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\int\frac{\mathrm{{\mst@d}}\omegaup\_{\mst@r}}{2\piup}\Big(\frac{-{}^{1-\mathtt{{\mst@i}}\omegaup}}{\omegaup^{2}+\mathtt{{\mst@i}}\omegaup}\Big)\mathrm{{\mst@e}}^{\mathtt{{\mst@i}}\omegaup{}\_{\mst@t}}{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},1-\mathtt{{\mst@i}}\omegaup,\omegaup^{2}/2+\mathtt{{\mst@i}}\omegaup/2)=:{\mst@C\/}({\mst@t},{}\_{\mst@t},{}\_{\mst@t};{\mst@T\/},{\mst@K\/}), | ωi\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\omegaup\_{\mst@i} | <−1​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle<-1. |  | (30) |

It will be helpful at this point to introduce a zero-coupon bond maturing at time , denoted by =()t0≤t≤\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar=({}\_{\mst@t})\_{0\leq{\mst@t}\leq{\mst@T\/}}, which pays one unit of currency at time . Setting φ​()=1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup()=1 in ([6](https://arxiv.org/html/2602.00858v1#S3.E6 "In 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | t | =te−∫tr()sds=:(t,;t),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{\mst@r}({}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}=:{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/}), |  | (31) |

where the existence of the function is guaranteed by the Markov property of .

###### Remark 4.

Note that (t,;t)≠(t,;t,1,0)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/})\neq{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},1,0) as the expectation in ([11](https://arxiv.org/html/2602.00858v1#S3.E11 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) is taken under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} while the expectation in ([31](https://arxiv.org/html/2602.00858v1#S4.E31 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")) is taken under .

We can now define Black-Scholes implied volatility, which is the unique positive solution ς≡ςt(,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\sigmaup\equiv\sigmaup\_{\mst@t}({\mst@T\/},{\mst@K\/}) of

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (,)tt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\frac{{}\_{\mst@t}({\mst@T\/},{\mst@K\/})}{{}\_{\mst@t}} | =(t,;tς,,)BS,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={}^{\textrm{BS}}({\mst@t},{}\_{\mst@t};\sigmaup,{\mst@T\/},{\mst@K\/}), | t | =tt,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{{}\_{\mst@t}}{{}\_{\mst@t}}, |  | (32) |

where (t,;tς,,)BS\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}^{\textrm{BS}}({\mst@t},{}\_{\mst@t};\sigmaup,{\mst@T\/},{\mst@K\/}) is the Black-Scholes price of a call, which is given by

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (t,;tς,,)BS\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{}^{\textrm{BS}}({\mst@t},{}\_{\mst@t};\sigmaup,{\mst@T\/},{\mst@K\/}) | :=Φt​(d+)−Φ​(d−),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:={}\_{\mst@t}\Phiup({\mst@d}\_{+})-{\mst@K\/}\Phiup({\mst@d}\_{-}), | d±\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@d}\_{\pm} | :=1ς​−t​(log⁡t±ς2​(−t)2)​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\frac{1}{\sigmaup\sqrt{{\mst@T\/}-{\mst@t}}}\Big(\log\frac{{}\_{\mst@t}}{{\mst@K\/}}\pm\frac{\sigmaup^{2}({\mst@T\/}-{\mst@t})}{2}\Big). |  | (33) |

In subsequent sections we will plot implied volatility as a function of log\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\log-moneyness , which is defined as follows

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | :=log⁡(t),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\log\Big(\frac{{\mst@K\/}}{{}\_{\mst@t}}\Big), | ⇒\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\Rightarrow | =e​.t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}{}\_{\mst@t}. |  | (34) |

With the above definitions, we can express implied volatility as the unique positive solution ς≡ςt(,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\sigmaup\equiv\sigmaup\_{\mst@t}({\mst@T\/},{\mst@L\/}) of

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (t,,t;t,e+t/(t,;t))(t,;t)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\frac{{\mst@C\/}({\mst@t},{}\_{\mst@t},{}\_{\mst@t};{\mst@T\/},\mathrm{{\mst@e}}^{{}\_{\mst@t}+{\mst@L\/}}/{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/}))}{{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/})} | =(t,et/(t,;t);ς,,e+t/(t,;t))BS,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={}^{\textrm{BS}}({\mst@t},\mathrm{{\mst@e}}\_{\mst@t}/{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/});\sigmaup,{\mst@T\/},\mathrm{{\mst@e}}^{{}\_{\mst@t}+{\mst@L\/}}/{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/})), |  | (35) |

where the functions , and BS\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}^{\textrm{BS}} are defined in ([30](https://arxiv.org/html/2602.00858v1#S4.E30 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")), ([31](https://arxiv.org/html/2602.00858v1#S4.E31 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")) and ([33](https://arxiv.org/html/2602.00858v1#S4.E33 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")), respectively.

## 5 Example: CIR-driven short rate

Throughout this section, we assume that the coefficients (r,b,a,c)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@r},{\mst@b},{\mst@a},{\mst@c}) are given by

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | r​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@r}({\mst@y}) | =y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@y}, | b​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@b}({\mst@y}) | =ϰ​(ϑ−y),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup(\thetaup-{\mst@y}), | a​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@a}({\mst@y}) | =δ​y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\deltaup\sqrt{{\mst@y}}, | c​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@c}({\mst@y}) | =γ2/r​(y)=γ/y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\sqrt{\gammaup^{2}/{\mst@r}({\mst@y})}=\gammaup/\sqrt{{\mst@y}}, |  | (36) |

where ϰ,ϑ,δ>0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\kappaup,\thetaup,\deltaup>0 and 2​ϰ​ϑ>δ2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar 2\kappaup\thetaup>\deltaup^{2} (the Feller condition), which ensures that the process remains strictly positive.
Note that the volatility c​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}({\mst@Y\/}) of the risky asset =e\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@S\/}=\mathrm{{\mst@e}} rises when short rate =r​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@R\/}={\mst@r}({\mst@Y\/}) falls.
Inserting ([36](https://arxiv.org/html/2602.00858v1#S5.E36 "In 5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models")) into ([2](https://arxiv.org/html/2602.00858v1#S2.E2 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")) and ([3](https://arxiv.org/html/2602.00858v1#S2.E3 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")), the dynamics of (,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@X\/},{\mst@Y\/}) under become

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =ϰ(ϑ−)tdt+δtd,t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup(\thetaup-{}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}+\deltaup\sqrt{{}\_{\mst@t}}\mathrm{{\mst@d}}{}\_{\mst@t}, | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(−tγ22t)dt+γt(ρd+tρ¯d)t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({}\_{\mst@t}-\frac{\gammaup^{2}}{2{}\_{\mst@t}}\Big)\mathrm{{\mst@d}}{\mst@t}+\frac{\gammaup}{\sqrt{{}\_{\mst@t}}}\Big(\rhoup\mathrm{{\mst@d}}{}\_{\mst@t}+\bar{\rhoup}\mathrm{{\mst@d}}{}\_{\mst@t}\Big), |  | (37) |

Similarly, inserting ([36](https://arxiv.org/html/2602.00858v1#S5.E36 "In 5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models")) into ([9](https://arxiv.org/html/2602.00858v1#S3.E9 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), we see that the dynamics of under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} are given by

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =ϰ(ϑ~−)tdt+δtd~t.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup(\widetilde{\thetaup}-{}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}+\deltaup\sqrt{{}\_{\mst@t}}\mathrm{{\mst@d}}\widetilde{{\mst@W\/}}\_{\mst@t}. | ϑ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{\thetaup} | :=ϑ+𝚒​ω​ρ​δ​γ/ϰ​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\thetaup+\mathtt{{\mst@i}}\omegaup\rhoup\deltaup\gammaup/\kappaup. |  | (38) |

Thus, the effect of moving from to ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} is to change the mean of the process from ϑ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\thetaup to ϑ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\thetaup}.
  
With the coefficients (r,b,a,c)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@r},{\mst@b},{\mst@a},{\mst@c}) as given in ([36](https://arxiv.org/html/2602.00858v1#S5.E36 "In 5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models")), the functions and , defined in ([11](https://arxiv.org/html/2602.00858v1#S3.E11 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) and ([31](https://arxiv.org/html/2602.00858v1#S4.E31 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")), respectively, are

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (t,;t,w,z)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},{\mst@w},{\mst@z}) | =~t​e−w∫tdss−zγ2∫t(1/)sds,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\widetilde{\mathds{{\mst@E\/}}}\_{\mst@t}\mathrm{{\mst@e}}^{-{\mst@w}\int\_{\mst@t}{}\_{\mst@s}\mathrm{{\mst@d}}{\mst@s}-{\mst@z}\gammaup^{2}\int\_{\mst@t}(1/{}\_{\mst@s})\mathrm{{\mst@d}}{\mst@s}}, | (t,;t)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/}) | =te−∫tds​s\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\int\_{\mst@t}{}\_{\mst@s}\mathrm{{\mst@d}}{\mst@s}} |  | (39) |

From [Hurd and Kuznetsov, [2008](https://arxiv.org/html/2602.00858v1#bib.bib7), Theorem 3.1], the functions in ([39](https://arxiv.org/html/2602.00858v1#S5.E39 "In 5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models")) is given explicitly by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (t,y;,w,z)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@G\/}({\mst@t},{\mst@y};{\mst@T\/},{\mst@w},{\mst@z}) | =e−(a~​v1+b​v2+δ2​v1​v2)​(−t)​yv2​(η−t−v1)−α~−v2−1​η−tα~+2​v2+1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{-(\widetilde{{\mst@a}}{\mst@v}\_{1}+{\mst@b}{\mst@v}\_{2}+\deltaup^{2}{\mst@v}\_{1}{\mst@v}\_{2})({\mst@T\/}-{\mst@t})}{\mst@y}^{{\mst@v}\_{2}}(\etaup\_{{\mst@T\/}-{\mst@t}}-{\mst@v}\_{1})^{-\widetilde{\alphaup}-{\mst@v}\_{2}-1}\etaup\_{{\mst@T\/}-{\mst@t}}^{\widetilde{\alphaup}+2{\mst@v}\_{2}+1} |  | (40) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×exp⁡(−y​v1​(1−η−t)​e−(β/2+v1)​δ2​(−t)η−t−v1)​η​(α~+v2+1)η​(α~+2​v2+1)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad\times\exp\left(-{\mst@y}{\mst@v}\_{1}\left(1-\etaup\_{{\mst@T\/}-{\mst@t}}\right)\frac{\mathrm{{\mst@e}}^{-(\betaup/2+{\mst@v}\_{1})\deltaup^{2}({\mst@T\/}-{\mst@t})}}{\etaup\_{{\mst@T\/}-{\mst@t}}-{\mst@v}\_{1}}\right)\frac{\etaup(\widetilde{\alphaup}+{\mst@v}\_{2}+1)}{\etaup(\widetilde{\alphaup}+2{\mst@v}\_{2}+1)} |  | (41) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×(v2,α~+2v2+1;−η−t2​y​e−(β/2+v1)​δ2​(−t)η−t−v1)11,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad\times\,{}\_{1}{}\_{1}\left({\mst@v}\_{2},\widetilde{\alphaup}+2{\mst@v}\_{2}+1;-\frac{\etaup\_{{\mst@T\/}-{\mst@t}}^{2}{\mst@y}{\mst@e}^{-(\betaup/2+{\mst@v}\_{1})\deltaup^{2}({\mst@T\/}-{\mst@t})}}{\etaup\_{{\mst@T\/}-{\mst@t}}-{\mst@v}\_{1}}\right), |  | (42) |

where 11\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}\_{1}{}\_{1} is a confluent hypergeometric function and

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | a~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{{\mst@a}} | =ϰ​ϑ~,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup\widetilde{\thetaup}, | v1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@v}\_{1} | =12​(−2​ϰδ2+(2​ϰδ2)2+8​wδ2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{1}{2}\left(-\frac{2\kappaup}{\deltaup^{2}}+\sqrt{\left(\frac{2\kappaup}{\deltaup^{2}}\right)^{2}+\frac{8{\mst@w}}{\deltaup^{2}}}\right), |  | (43) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | α~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{\alphaup} | =2​ϰ​ϑ~δ2−1,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2\kappaup\widetilde{\thetaup}}{\deltaup^{2}}-1, | v2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@v}\_{2} | =12​(−α~+α~2+8​z​γ2δ2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{1}{2}\left(-\tilde{\alphaup}+\sqrt{\tilde{\alphaup}^{2}+\frac{8{\mst@z}\gammaup^{2}}{\deltaup^{2}}}\right), |  | (44) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | β\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\betaup | =2​ϰδ2,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2\kappaup}{\deltaup^{2}}, | η−t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\etaup\_{{\mst@T\/}-{\mst@t}} | =(β+2​v1)​(1−e−(β/2+v1)​δ2​(−t))−1​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=(\betaup+2{\mst@v}\_{1})\left(1-\mathrm{{\mst@e}}^{-(\betaup/2+{\mst@v}\_{1})\deltaup^{2}({\mst@T\/}-{\mst@t})}\right)^{-1}. |  | (45) |

Similarly, using [Hurd and Kuznetsov, [2008](https://arxiv.org/html/2602.00858v1#bib.bib7), Theorem 3.1], the function in ([39](https://arxiv.org/html/2602.00858v1#S5.E39 "In 5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models")) is given explicitly by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (t,y;)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@B\/}({\mst@t},{\mst@y};{\mst@T\/}) | =exp(−(t;)−(t;)y),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\exp\Big(-{\mst@P\/}({\mst@t};{\mst@T\/})-{\mst@Q\/}({\mst@t};{\mst@T\/}){\mst@y}\Big), |  | (46) |

where we have defined

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (t;)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@P\/}({\mst@t};{\mst@T\/}) | =−2​ϰ​ϑδ2​log⁡(2​ζ​e(ϰ+ζ)​(−t)/22​ζ+(ϰ+ζ)​(eζ​(−t)−1)),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{-2\kappaup\thetaup}{\deltaup^{2}}\log\Big(\frac{2\zetaup\mathrm{{\mst@e}}^{(\kappaup+\zetaup)({\mst@T\/}-{\mst@t})/2}}{2\zetaup+(\kappaup+\zetaup)(\mathrm{{\mst@e}}^{\zetaup({\mst@T\/}-{\mst@t})}-1)}\Big), | (t,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@Q\/}({\mst@t},{\mst@T\/}) | =2​(eζ​(−t)−1)2​ζ+(ϰ+ζ)​(eζ​(−t)−1),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2(\mathrm{{\mst@e}}^{\zetaup({\mst@T\/}-{\mst@t})}-1)}{2\zetaup+(\kappaup+\zetaup)(\mathrm{{\mst@e}}^{\zetaup({\mst@T\/}-{\mst@t})}-1)}, | ζ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\zetaup | =ϰ2+2​δ2,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\sqrt{\kappaup^{2}+2\deltaup^{2}}, |  | (47) |

which is the well-known formula for the price of a zero-coupon bond when the short rate is modeled by a CIR process.
  
In Figure [1](https://arxiv.org/html/2602.00858v1#A2.F1 "Figure 1 ‣ Short-Rate-Dependent Volatility Models"), we plot implied volatility ς0(,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\sigmaup\_{0}({\mst@T\/},{\mst@L\/}) as a function of log-moneyness for two different maturities and three different correlation coefficients ρ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup. For both long and short maturities (=1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}=1 and =0.25\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}=0.25, respectively), the implied volatility becomes more skewed when correlation ρ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup increases from 0 to 1. Also, the implied volatility tends to be higher at longer maturity. The Wolfram Mathematica © code used to produce the plots is given in Appendix [B](https://arxiv.org/html/2602.00858v1#A2 "Appendix B Wolfram Mathematica © code ‣ Short-Rate-Dependent Volatility Models").

###### Remark 5.

The astute reader will observe that – even when ρ=0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup=0, the implied volatility smile is not symmetric. The reason is that, although from ([2](https://arxiv.org/html/2602.00858v1#S2.E2 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models"))-([3](https://arxiv.org/html/2602.00858v1#S2.E3 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")) we have d[,]t=0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathrm{{\mst@d}}[{\mst@X\/},{\mst@Y\/}]\_{\mst@t}=0 when ρ=0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup=0, we also have from equations ([74](https://arxiv.org/html/2602.00858v1#A1.E74 "In Appendix A Dynamics of under the -forward measure in the CIR setting ‣ Short-Rate-Dependent Volatility Models"))-([76](https://arxiv.org/html/2602.00858v1#A1.E76 "In Appendix A Dynamics of under the -forward measure in the CIR setting ‣ Short-Rate-Dependent Volatility Models")) in Appendix [A](https://arxiv.org/html/2602.00858v1#A1 "Appendix A Dynamics of under the -forward measure in the CIR setting ‣ Short-Rate-Dependent Volatility Models") that d[,]t=a2()t(t;)dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\mathrm{{\mst@d}}[,{\mst@Y\/}]\_{\mst@t}={\mst@a}^{2}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\mathrm{{\mst@d}}{\mst@t} when ρ=0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup=0, where =log\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar=\log. The non-zero co-variation results in an asymmetric implied volatility smile.

###### Remark 6.

Another analytically tractable model can be obtained by setting the functions (r,a,b,c)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@r},{\mst@a},{\mst@b},{\mst@c}) equal to

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | r​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@r}({\mst@y}) | =y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@y}, | b​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@b}({\mst@y}) | =ϰ​(ϑ−y),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup(\thetaup-{\mst@y}), | a​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@a}({\mst@y}) | =δ​y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\deltaup\sqrt{{\mst@y}}, | c​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@c}({\mst@y}) | =γ​r​(y)=γ​y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\gammaup\sqrt{{\mst@r}({\mst@y})}=\gammaup\sqrt{{\mst@y}}, |  | (48) |

which corresponds to the Heston model with a CIR-driven short rate.
In this case, the volatility of is proportional to the square root of the interest rate: c​()=γ​\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}({\mst@Y\/})=\gammaup\sqrt{{\mst@R\/}}.

## 6 Example: Jacobi-driven short rate

Throughout this section, we suppose that the coefficients (r,a,b,c)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@r},{\mst@a},{\mst@b},{\mst@c}) are given by

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | r​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@r}({\mst@y}) | =η​y1−y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{\etaup{\mst@y}}{1-{\mst@y}}, | b​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@b}({\mst@y}) | =ϰ−ϑ​y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup-\thetaup{\mst@y}, | a​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@a}({\mst@y}) | =δ​y​(1−y),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\deltaup\sqrt{{\mst@y}(1-{\mst@y})}, | c​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@c}({\mst@y}) | =γ​ηr​(y)=γ​1−yy,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{\gammaup\sqrt{\etaup}}{\sqrt{{\mst@r}({\mst@y})}}=\gammaup\sqrt{\frac{1-{\mst@y}}{{\mst@y}}}, |  | (49) |

where δ>0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\deltaup>0, ϰ>δ2/2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\kappaup>\deltaup^{2}/2 and ϑ−ϰ>δ2/2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\thetaup-\kappaup>\deltaup^{2}/2, which ensures that 0<<1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar 0<{\mst@Y\/}<1.
Observe, the volatility c​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}({\mst@Y\/}) of the risky asset =e\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@S\/}=\mathrm{{\mst@e}} rises when the short rate =r​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@R\/}={\mst@r}({\mst@Y\/}) falls.
Inserting ([49](https://arxiv.org/html/2602.00858v1#S6.E49 "In 6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models")) into ([2](https://arxiv.org/html/2602.00858v1#S2.E2 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")) and ([3](https://arxiv.org/html/2602.00858v1#S2.E3 "In 2 A general class of short-rate-dependent volatility models ‣ Short-Rate-Dependent Volatility Models")), we obtain the dynamics of (,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@X\/},{\mst@Y\/}) under . We have

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(ϰ−ϑ)tdt+δ(1−)ttd,t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big(\kappaup-\thetaup{}\_{\mst@t}\Big)\mathrm{{\mst@d}}{\mst@t}+\deltaup\sqrt{{}\_{\mst@t}(1-{}\_{\mst@t})}\mathrm{{\mst@d}}{}\_{\mst@t}, | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(ηt1−t−γ2(1−)t2t)dt+γ1−tt(ρd+tρ¯d)t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big(\frac{\etaup{}\_{\mst@t}}{1-{}\_{\mst@t}}-\frac{\gammaup^{2}(1-{}\_{\mst@t})}{2{}\_{\mst@t}}\Big)\mathrm{{\mst@d}}{\mst@t}+\gammaup\sqrt{\frac{1-{}\_{\mst@t}}{{}\_{\mst@t}}}\Big(\rhoup\mathrm{{\mst@d}}{}\_{\mst@t}+\bar{\rhoup}\mathrm{{\mst@d}}{}\_{\mst@t}\Big), |  | (50) |

Similarly, inserting ([49](https://arxiv.org/html/2602.00858v1#S6.E49 "In 6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models")) into ([9](https://arxiv.org/html/2602.00858v1#S3.E9 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")), we see that the dynamics of under ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} are

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(ϰ~−ϑ~)tdt+δ(1−)ttd~t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big(\widetilde{\kappaup}-\widetilde{\thetaup}{}\_{\mst@t}\Big)\mathrm{{\mst@d}}{\mst@t}+\deltaup\sqrt{{}\_{\mst@t}(1-{}\_{\mst@t})}\mathrm{{\mst@d}}\widetilde{{\mst@W\/}}\_{\mst@t}, | ϰ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{\kappaup} | =ϰ+𝚒​ω​ρ​δ​γ,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup+\mathtt{{\mst@i}}\omegaup\rhoup\deltaup\gammaup, | ϑ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{\thetaup} | =ϑ+𝚒​ω​ρ​δ​γ​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\thetaup+\mathtt{{\mst@i}}\omegaup\rhoup\deltaup\gammaup. |  | (51) |

Thus, the effect of changing from to ~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widetilde{\mathds{{\mst@P\/}}} is to shift the parameters (ϰ,ϑ)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\kappaup,\thetaup) to (ϰ~,ϑ~)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\widetilde{\kappaup},\widetilde{\thetaup}).
  
With the coefficients (r,b,a,c)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@r},{\mst@b},{\mst@a},{\mst@c}) as given in ([49](https://arxiv.org/html/2602.00858v1#S6.E49 "In 6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models")), the functions and , defined in ([11](https://arxiv.org/html/2602.00858v1#S3.E11 "In Lemma 2. ‣ 3 Pricing of European-style claims ‣ Short-Rate-Dependent Volatility Models")) and ([31](https://arxiv.org/html/2602.00858v1#S4.E31 "In 4 Call options and Implied Volatility ‣ Short-Rate-Dependent Volatility Models")), respectively, become

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (t,;t,w,z)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},{\mst@w},{\mst@z}) | =~t​e−w​η​∫ts1−s​d​s−z​γ2​∫t1−ss​d​s,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\widetilde{\mathds{{\mst@E\/}}}\_{\mst@t}\mathrm{{\mst@e}}^{-{\mst@w}\etaup\int\_{\mst@t}\frac{{}\_{\mst@s}}{1-{}\_{\mst@s}}\mathrm{{\mst@d}}{\mst@s}-{\mst@z}\gammaup^{2}\int\_{\mst@t}\frac{1-{}\_{\mst@s}}{{}\_{\mst@s}}\mathrm{{\mst@d}}{\mst@s}}, | (t,;t)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@B\/}({\mst@t},{}\_{\mst@t};{\mst@T\/}) | =te−η​∫ts1−s​d​s​.​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathds{{\mst@E\/}}\_{\mst@t}\mathrm{{\mst@e}}^{-\etaup\int\_{\mst@t}\frac{{}\_{\mst@s}}{1-{}\_{\mst@s}}\mathrm{{\mst@d}}{\mst@s}}.. |  | (52) |

We have from [Hurd and Kuznetsov, [2008](https://arxiv.org/html/2602.00858v1#bib.bib7), Theorem 4.1] that the function in ([52](https://arxiv.org/html/2602.00858v1#S6.E52 "In 6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models")) is given explicitly by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (t,;t,w,z)=e−((ϑ~−ϰ~)​v~1+ϰ~​v~2+δ2​v~1​v~2)​(−t)yv~1(1−y)v~2Γ​(α~+v~1+1)​Γ​(β~+v~2+1)​Γ​(α~+β~+2​v~1+2​v~2+1)Γ​(α~+v~1+β~+v~2+2)​Γ​(α~+2​v~1+1)​Γ​(β~+2​v~2+1)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@G\/}({\mst@t},{}\_{\mst@t};{\mst@T\/},{\mst@w},{\mst@z})=\mathrm{{\mst@e}}^{-((\widetilde{\thetaup}-\widetilde{\kappaup})\widetilde{{\mst@v}}\_{1}+\widetilde{\kappaup}\widetilde{{\mst@v}}\_{2}+\deltaup^{2}\widetilde{{\mst@v}}\_{1}\widetilde{{\mst@v}}\_{2})({\mst@T\/}-{\mst@t})}{\mst@y}^{\widetilde{{\mst@v}}\_{1}}(1-{\mst@y})^{\widetilde{{\mst@v}}\_{2}}\frac{\Gammaup(\widetilde{\alphaup}+\widetilde{{\mst@v}}\_{1}+1)\Gammaup(\widetilde{\betaup}+\widetilde{{\mst@v}}\_{2}+1)\Gammaup(\widetilde{\alphaup}+\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{1}+2\widetilde{{\mst@v}}\_{2}+1)}{\Gammaup(\widetilde{\alphaup}+\widetilde{{\mst@v}}\_{1}+\widetilde{\betaup}+\widetilde{{\mst@v}}\_{2}+2)\Gammaup(\widetilde{\alphaup}+2\widetilde{{\mst@v}}\_{1}+1)\Gammaup(\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{2}+1)} |  | (53) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=0∞e−n​(n+α~+β~+2​v~1+2​v~2+1)​δ2​(−t)/2​(α~+β~+2​v~1+2​v~2+1)n(α~+2​v~1+1)n​(2​n+α~+β~+2​v~1+2​v~2+1)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad\sum\_{{\mst@n}=0}^{\infty}\mathrm{{\mst@e}}^{-{\mst@n}({\mst@n}+\widetilde{\alphaup}+\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{1}+2\widetilde{{\mst@v}}\_{2}+1)\deltaup^{2}({\mst@T\/}-{\mst@t})/2}\frac{(\widetilde{\alphaup}+\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{1}+2\widetilde{{\mst@v}}\_{2}+1)\_{\mst@n}}{(\widetilde{\alphaup}+2\widetilde{{\mst@v}}\_{1}+1)\_{\mst@n}}(2{\mst@n}+\widetilde{\alphaup}+\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{1}+2\widetilde{{\mst@v}}\_{2}+1) |  | (54) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (−n,α~+β~+2v~1+2v~2+n+1,β~+v~2+1;α~+β~+v~1+v~2+2,β~+2v~2+1;1)32(2y−1)n(α~+2​v~1,β~+2​v~2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad{}\_{3}{}\_{2}\left(-{\mst@n},\widetilde{\alphaup}+\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{1}+2\widetilde{{\mst@v}}\_{2}+{\mst@n}+1,\widetilde{\betaup}+\widetilde{{\mst@v}}\_{2}+1;\widetilde{\alphaup}+\widetilde{\betaup}+\widetilde{{\mst@v}}\_{1}+\widetilde{{\mst@v}}\_{2}+2,\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{2}+1;1\right){}\_{\mst@n}^{(\widetilde{\alphaup}+2\widetilde{{\mst@v}}\_{1},\widetilde{\betaup}+2\widetilde{{\mst@v}}\_{2})}(2{\mst@y}-1), |  | (55) |

where (⋅)n\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(\cdot)\_{\mst@n} is the Pochhammer symbol, the functions (⋅,⋅)n\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}\_{\mst@n}^{(\cdot,\cdot)} are Jacobi polynomials, and

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | α~\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{\alphaup} | =2​ϰ~δ2−1,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2\widetilde{\kappaup}}{\deltaup^{2}}-1, | v~1\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{{\mst@v}}\_{1} | =12​(−α~+α~2+8​z​γ2δ2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{1}{2}\left(-\widetilde{\alphaup}+\sqrt{\widetilde{\alphaup}^{2}+\frac{8{\mst@z}\gammaup^{2}}{\deltaup^{2}}}\right), | β~,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{\betaup}, | =2​(ϑ~−ϰ~)δ2−1,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2(\widetilde{\thetaup}-\widetilde{\kappaup})}{\deltaup^{2}}-1, | v~2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widetilde{{\mst@v}}\_{2} | =12​(−β~+β~2+8​w​ηδ2)​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{1}{2}\left(-\widetilde{\betaup}+\sqrt{\widetilde{\betaup}^{2}+\frac{8{\mst@w}\etaup}{\deltaup^{2}}}\right). |  | (56) |

Similarly, we have from [Hurd and Kuznetsov, [2008](https://arxiv.org/html/2602.00858v1#bib.bib7), Theorem 4.1] that the function in ([52](https://arxiv.org/html/2602.00858v1#S6.E52 "In 6 Example: Jacobi-driven short rate ‣ Short-Rate-Dependent Volatility Models")) is given explicitly by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (t,y;)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@B\/}({\mst@t},{\mst@y};{\mst@T\/}) | =e−ϰ​v2​(−t)​(1−y)v2​Γ​(α+1)​Γ​(β+v2+1)​Γ​(α+β+2​v2+1)Γ​(α+β+v2+2)​Γ​(α+1)​Γ​(β+2​v2+1)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@e}}^{-\kappaup{\mst@v}\_{2}({\mst@T\/}-{\mst@t})}(1-{\mst@y})^{{\mst@v}\_{2}}\frac{\Gammaup(\alphaup+1)\Gammaup(\betaup+{\mst@v}\_{2}+1)\Gammaup(\alphaup+\betaup+2{\mst@v}\_{2}+1)}{\Gammaup(\alphaup+\betaup+{\mst@v}\_{2}+2)\Gammaup(\alphaup+1)\Gammaup(\betaup+2{\mst@v}\_{2}+1)} |  | (57) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∑n=0∞e−n​(n+α+β+2​v2+1)​δ2​(−t)/2​(α+β+2​v2+1)n(α+1)n​(2​n+α+β+2​v2+1)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad\sum\_{{\mst@n}=0}^{\infty}\mathrm{{\mst@e}}^{-{\mst@n}({\mst@n}+\alphaup+\betaup+2{\mst@v}\_{2}+1)\deltaup^{2}({\mst@T\/}-{\mst@t})/2}\frac{(\alphaup+\betaup+2{\mst@v}\_{2}+1)\_{\mst@n}}{(\alphaup+1)\_{\mst@n}}(2{\mst@n}+\alphaup+\betaup+2{\mst@v}\_{2}+1) |  | (58) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (−n,α+β+2v2+n+1,β+v2+1;α+β+v2+2,β+2v2+1;1)32(2y−1)n(α,β+2​v2),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad{}\_{3}{}\_{2}\left(-{\mst@n},\alphaup+\betaup+2{\mst@v}\_{2}+{\mst@n}+1,\betaup+{\mst@v}\_{2}+1;\alphaup+\betaup+{\mst@v}\_{2}+2,\betaup+2{\mst@v}\_{2}+1;1\right){}\_{\mst@n}^{(\alphaup,\betaup+2{\mst@v}\_{2})}(2{\mst@y}-1), |  | (59) |

where we have introduced

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | α\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\alphaup | =2​ϰδ2−1,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2\kappaup}{\deltaup^{2}}-1, | β\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\betaup | =2​(ϑ−ϰ)δ2−1,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{2(\thetaup-\kappaup)}{\deltaup^{2}}-1, | v2\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@v}\_{2} | =12​(−β+β2+8​ηδ2)​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{1}{2}\left(-\betaup+\sqrt{\betaup^{2}+\frac{8\etaup}{\deltaup^{2}}}\right). |  | (60) |

###### Remark 7.

Another analytically tractable model can be obtained by setting the functions (r,a,b,c)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar({\mst@r},{\mst@a},{\mst@b},{\mst@c}) equal to

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | r​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@r}({\mst@y}) | =η​y1−y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\frac{\etaup{\mst@y}}{1-{\mst@y}}, | b​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@b}({\mst@y}) | =ϰ−ϑ​y,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\kappaup-\thetaup{\mst@y}, | a​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@a}({\mst@y}) | =δ​y​(1−y),\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\deltaup\sqrt{{\mst@y}(1-{\mst@y})}, | c​(y)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle{\mst@c}({\mst@y}) | =γ​y1−y​.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\gammaup\sqrt{\frac{{\mst@y}}{1-{\mst@y}}}. |  | (61) |

In this case, however, the volatility of is proportional to the squire root of the interest rate: c​()=γ​/η\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}({\mst@Y\/})=\gammaup\sqrt{{\mst@R\/}/\etaup}.

## 7 Conclusion

This paper develops a flexible class of short‑rate–dependent volatility models in which the instantaneous volatility of a risky asset is an explicit function of the driver of the short rate. Within this framework, European option prices are expressed via a Fourier representation that reduces the pricing problem to the computation of a characteristic function associated with the time-integrals of the short rate r​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@r}({\mst@Y\/}) and stochastic variance c2​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@c}^{2}({\mst@Y\/}). The representation is obtained under simple integrability and martingale assumptions that ensure the validity of a complex Girsanov transform and justify the use of generalized Fourier techniques for payoffs of the form φ​()\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\phiup().
  
Two analytically tractable specifications illustrate the approach: a CIR driver with a short rate equal to and a volatility proportional to 1/\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar 1/\sqrt{{\mst@Y\/}}, and a Jacobi driver with a short rate proportional to /(1−)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@Y\/}/(1-{\mst@Y\/}) and a volatility proportional to (1−)/\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\sqrt{(1-{\mst@Y\/})/{\mst@Y\/}}. In both cases, explicit formulas for the relevant Laplace transforms, and hence for the characteristic function , are available through results of Hurd and Kuznetsov [[2008](https://arxiv.org/html/2602.00858v1#bib.bib7)], which in turn yield closed-form integral expressions for European call prices and associated Black-Scholes implied volatilities. Numerical illustrations highlight the ability of short-rate-dependent volatility to generate asymmetric implied volatility smiles, even in parameter regimes where the covariance between the log-price and the short rate vanishes under the original pricing measure.
  
The framework can be extended in several directions, including multi-factor specifications for the short rate, alternative functional forms for the volatility-rate linkage, and the valuation of path‑dependent or exotic claims under the same Fourier transform methodology. Such extensions would allow for a more detailed study of how monetary policy and interest rate uncertainty are transmitted into the equity volatility surface. Therefore, they may help bridge the gap between reduced-form stochastic volatility models and term-structure models used in fixed‑ ncome markets.

## Appendix A Dynamics of under the -forward measure in the CIR setting

In this Appendix, we derive the dynamics of (=log,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar(=\log,{\mst@Y\/}) under the -forward probability measure for the model presented in Section [5](https://arxiv.org/html/2602.00858v1#S5 "5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models").
To begin, we note that the dynamics of the price of the risky asset and the price of a zero-coupon bond can be written as

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =r()tdtt+c()t(ρd+tρ¯d)tt,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@r}({}\_{\mst@t}){}\_{\mst@t}\mathrm{{\mst@d}}{\mst@t}+{\mst@c}({}\_{\mst@t}){}\_{\mst@t}(\rhoup\mathrm{{\mst@d}}{}\_{\mst@t}+\bar{\rhoup}\mathrm{{\mst@d}}{}\_{\mst@t}), | t | =exp(−(t;)−(t;))t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\exp\Big(-{\mst@P\/}({\mst@t};{\mst@T\/})-{\mst@Q\/}({\mst@t};{\mst@T\/}){}\_{\mst@t}\Big), |  | (62) |

where the functions and are given in ([47](https://arxiv.org/html/2602.00858v1#S5.E47 "In 5 Example: CIR-driven short rate ‣ Short-Rate-Dependent Volatility Models")).
From this, we compute the dynamics of /\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@S\/}/{\mst@M\/} and /\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar/{\mst@M\/}, both of which are martingales under . We have

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | d​(tt)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}\Big(\frac{{}\_{\mst@t}}{{}\_{\mst@t}}\Big) | =c()t(tt)t(ρd+tρ¯d)t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@c}({}\_{\mst@t}){}\_{\mst@t}\Big(\frac{{}\_{\mst@t}}{{}\_{\mst@t}}\Big)(\rhoup\mathrm{{\mst@d}}{}\_{\mst@t}+\bar{\rhoup}\mathrm{{\mst@d}}{}\_{\mst@t}), | d​(tt)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}\Big(\frac{{}\_{\mst@t}}{{}\_{\mst@t}}\Big) | =−a()t(t;)(tt)d.t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=-{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\Big(\frac{{}\_{\mst@t}}{{}\_{\mst@t}}\Big)\mathrm{{\mst@d}}{}\_{\mst@t}. |  | (63) |

Next, we derive the dynamics of =/\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar={\mst@S\/}/, which is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =d​(tt)=d​(/tt/tt)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@d}}\Big(\frac{{}\_{\mst@t}}{{}\_{\mst@t}}\Big)=\mathrm{{\mst@d}}\Big(\frac{{}\_{\mst@t}/{}\_{\mst@t}}{{}\_{\mst@t}/{}\_{\mst@t}}\Big) |  | (64) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(a2()t(t;)2+ρa()t(t;)c()t)dtt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({\mst@a}^{2}({}\_{\mst@t}){}^{2}({\mst@t};{\mst@T\/})+\rhoup{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/}){\mst@c}({}\_{\mst@t})\Big){}\_{\mst@t}\mathrm{{\mst@d}}{\mst@t} |  | (65) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(a()t(t;)+ρc()t)dt+tρ¯c()tdt.t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad+\Big({\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})+\rhoup{\mst@c}({}\_{\mst@t})\Big){}\_{\mst@t}\mathrm{{\mst@d}}{}\_{\mst@t}+\bar{\rhoup}{\mst@c}({}\_{\mst@t}){}\_{\mst@t}\mathrm{{\mst@d}}{}\_{\mst@t}. |  | (66) |

Now, let us define the -forward probability measure ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{\mathds{{\mst@P\/}}}, whose relation to is given by the following change of measure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​^d\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\frac{\mathrm{{\mst@d}}\widehat{\mathds{{\mst@P\/}}}}{\mathrm{{\mst@d}}\mathds{{\mst@P\/}}} | :=00=exp(−12∫0(a()t(t;))2dt−∫0(a()t(t;))d)t.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle:=\frac{{}\_{0}}{{}\_{0}}=\exp\Big(-\frac{1}{2}\int\_{0}({\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/}))^{2}\mathrm{{\mst@d}}{\mst@t}-\int\_{0}\big({\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\big)\mathrm{{\mst@d}}{}\_{\mst@t}\Big). |  | (67) |

Under ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{\mathds{{\mst@P\/}}}, the processes ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{{\mst@W\/}} and ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{{\mst@B\/}}, defined by

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | d​^t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}\widehat{{\mst@W\/}}\_{\mst@t} | =d+ta()t(t;)dt,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@d}}{}\_{\mst@t}+{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\mathrm{{\mst@d}}{\mst@t}, | ^0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widehat{{\mst@W\/}}\_{0} | =0,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=0, |  | (68) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | d​^t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}\widehat{{\mst@B\/}}\_{\mst@t} | =d,t\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\mathrm{{\mst@d}}{}\_{\mst@t}, | ^0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\widehat{{\mst@B\/}}\_{0} | =0,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=0, |  | (69) |

are independent Brownian motion. As such, the dynamics of under ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{\mathds{{\mst@P\/}}} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =(a2()t(t;)2+ρa()t(t;)c()t)dtt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({\mst@a}^{2}({}\_{\mst@t}){}^{2}({\mst@t};{\mst@T\/})+\rhoup{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/}){\mst@c}({}\_{\mst@t})\Big){}\_{\mst@t}\mathrm{{\mst@d}}{\mst@t} |  | (70) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(a()t(t;)+ρc()t)(d^t−a()t(t;)dt)t+ρ¯c()tdt^t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad+\Big({\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})+\rhoup{\mst@c}({}\_{\mst@t})\Big){}\_{\mst@t}(\mathrm{{\mst@d}}\widehat{{\mst@W\/}}\_{\mst@t}-{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\mathrm{{\mst@d}}{\mst@t})+\bar{\rhoup}{\mst@c}({}\_{\mst@t}){}\_{\mst@t}\mathrm{{\mst@d}}\widehat{{\mst@B\/}}\_{\mst@t}, |  | (71) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(a()t(t;)+ρc()t)dt^t+ρ¯c()tdt^t.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})+\rhoup{\mst@c}({}\_{\mst@t})\Big){}\_{\mst@t}\mathrm{{\mst@d}}\widehat{{\mst@W\/}}\_{\mst@t}+\bar{\rhoup}{\mst@c}({}\_{\mst@t}){}\_{\mst@t}\mathrm{{\mst@d}}\widehat{{\mst@B\/}}\_{\mst@t}. |  | (72) |

Observe that is a martingale under the -forward measure ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{\mathds{{\mst@P\/}}}, as it should be.
Finally, the dynamics of and :=log\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar:=\log under ^\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\widehat{\mathds{{\mst@P\/}}} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =b()tdt+a()t(d^t−a()t(t;)dt)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle={\mst@b}({}\_{\mst@t})\mathrm{{\mst@d}}{\mst@t}+{\mst@a}({}\_{\mst@t})(\mathrm{{\mst@d}}\widehat{{\mst@W\/}}\_{\mst@t}-{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\mathrm{{\mst@d}}{\mst@t}) |  | (73) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(b()t−a2()t(t;))dt+a()td^t,\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=\Big({\mst@b}({}\_{\mst@t})-{\mst@a}^{2}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})\Big)\mathrm{{\mst@d}}{\mst@t}+{\mst@a}({}\_{\mst@t})\mathrm{{\mst@d}}\widehat{{\mst@W\/}}\_{\mst@t}, |  | (74) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\mathrm{{\mst@d}}{}\_{\mst@t} | =−12(a2()t(t;)2+c2()t+2ρa()t(t;)c()t)dt\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle=-\frac{1}{2}\Big({\mst@a}^{2}({}\_{\mst@t}){}^{2}({\mst@t};{\mst@T\/})+{\mst@c}^{2}({}\_{\mst@t})+2\rhoup{\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/}){\mst@c}({}\_{\mst@t})\Big)\mathrm{{\mst@d}}{\mst@t} |  | (75) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(a()t(t;)+ρc()t)d^t+ρ¯c()td^t.\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\displaystyle\quad+\Big({\mst@a}({}\_{\mst@t}){\mst@Q\/}({\mst@t};{\mst@T\/})+\rhoup{\mst@c}({}\_{\mst@t})\Big)\mathrm{{\mst@d}}\widehat{{\mst@W\/}}\_{\mst@t}+\bar{\rhoup}{\mst@c}({}\_{\mst@t})\mathrm{{\mst@d}}\widehat{{\mst@B\/}}\_{\mst@t}. |  | (76) |

## Appendix B Wolfram Mathematica © code

In this Appendix, we provide the Wolfram Mathematica © code that was used to produce the implied volatility plots in Figure [1](https://arxiv.org/html/2602.00858v1#A2.F1 "Figure 1 ‣ Short-Rate-Dependent Volatility Models").

[⬇](data:text/plain;base64,Q2xlYXJBbGxbIkdsb2JhbGAqIl0KCigqIEJvbmQgUHJpY2UgKikKQltUXyx5XyxcW0thcHBhXV8sXFtUaGV0YV1fLFxbRGVsdGFdX106PU1vZHVsZVt7XFtHYW1tYV0xLEIxLEExfSwKXFtHYW1tYV0xPVNxcnRbXFtLYXBwYV1eMisyIFxbRGVsdGFdXjJdOwpCMT0oMiAoRXhwW1xbR2FtbWFdMSBUXS0xKSkvKChcW0thcHBhXStcW0dhbW1hXTEpIChFeHBbXFtHYW1tYV0xIFRdLTEpKzIgXFtHYW1tYV0xKTtBMT0oMiBcW0dhbW1hXTEgRXhwWyhcW0thcHBhXStcW0dhbW1hXTEpIFQvMl0vKChcW0thcHBhXStcW0dhbW1hXTEpIChFeHBbXFtHYW1tYV0xIFRdLTEpKzIgXFtHYW1tYV0xKSleKDIgXFtLYXBwYV0gXFtUaGV0YV0vXFtEZWx0YV1eMik7CkExIEV4cFstQjEgeV0KXQoKKCpNYXRoZW1hdGljYSBDb2RlIGZvciBHXkNJUiAoRXF1YXRpb24gMTApIFNvdXJjZToiRXhwbGljaXQgZm9ybXVsYXMgZm9yIExhcGxhY2UgdHJhbnNmb3JtcyBvZiBzdG9jaGFzdGljIGludGVncmFscyIgYnkgVC5SLkh1cmQgYW5kIEEuS3V6bmV0c292LiopCgpHQ0lSW1RfLHhfLGQxXyxkMl8sdzFfLHcyXyxhXyxiXyxjX106PU1vZHVsZVt7XFtBbHBoYV0sXFtCZXRhXSx2MSx2MixcW0dhbW1hXVQsekFyZyxleHBvbmVudFRlcm0scHJlRmFjdG9yLGh5cGVyR2VvbVRlcm19LApcW0FscGhhXT0yKmEvY14yLTE7ClxbQmV0YV09MipiL2NeMjsKdjE9MS8yKigtXFtCZXRhXStTcXJ0W1xbQmV0YV1eMis4KmQxL2NeMl0pOwp2Mj0xLzIqKC1cW0FscGhhXStTcXJ0W1xbQWxwaGFdXjIrOCpkMi9jXjJdKTsKXFtHYW1tYV1UPShcW0JldGFdKzIqdjEpLygxLUV4cFstKFxbQmV0YV0vMit2MSkqY14yKlRdKTsKekFyZz0tKChcW0dhbW1hXVReMip4KkV4cFstKFxbQmV0YV0vMit2MSkqY14yKlRdKS8oXFtHYW1tYV1UK3cxLXYxKSk7CnByZUZhY3Rvcj1FeHBbLShhKnYxK2IqdjIrY14yKnYxKnYyKSpUXSp4XnYyKihcW0dhbW1hXVQrdzEtdjEpXigtXFtBbHBoYV0tdjItdzItMSkqXFtHYW1tYV1UXihcW0FscGhhXSsyKnYyKzEpOwpleHBvbmVudFRlcm09RXhwWy14Kih2MSsoXFtHYW1tYV1UKih3MS12MSkpLyhcW0dhbW1hXVQrdzEtdjEpKkV4cFstKFxbQmV0YV0vMit2MSkqY14yKlRdKV07Cmh5cGVyR2VvbVRlcm09KEdhbW1hW1xbQWxwaGFdK3YyK3cyKzFdL0dhbW1hW1xbQWxwaGFdKzIqdjIrMV0pKkh5cGVyZ2VvbWV0cmljMUYxW3YyLXcyLFxbQWxwaGFdKzIqdjIrMSx6QXJnXTsKcHJlRmFjdG9yKmV4cG9uZW50VGVybSpoeXBlckdlb21UZXJtCl07CgpHW1xbT21lZ2FdXyxUXyx5Xyx3Xyx6XyxcW0thcHBhXV8sXFtUaGV0YV1fLFxbRGVsdGFdXyxcW1Job11fLFxbR2FtbWFdX106PU1vZHVsZVt7YSxiLGMseCxkMSxkMix3MSx3Mn0sCmE9XFtLYXBwYV0gKFxbVGhldGFdICsgSSBcW09tZWdhXSBcW1Job10gXFtEZWx0YV0gXFtHYW1tYV0gLyBcW0thcHBhXSk7CmI9XFtLYXBwYV07CmM9XFtEZWx0YV07Cng9eTsKZDE9dzsKZDI9XFtHYW1tYV1eMiB6Owp3MT0wOwp3Mj0wOwpHQ0lSW1QseCxkMSxkMix3MSx3MixhLGIsY10KXTsKClxbQ2FwaXRhbFBoaV1oYXRbXFtPbWVnYV1fLEtfXTo9LUteKDEtSSBcW09tZWdhXSkvKFxbT21lZ2FdXjIrSSBcW09tZWdhXSk7CgpjYWxsUHJpY2VbVF8seF8seV8sXFtLYXBwYV1fLFxbVGhldGFdXyxcW0RlbHRhXV8sXFtSaG9dXyxcW0dhbW1hXV8sS19dOj1Nb2R1bGVbe1xbT21lZ2FdaSxcW09tZWdhXSx3LHp9LApcW09tZWdhXWk9LTEuNTsKXFtPbWVnYV09XFtPbWVnYV1yICsgSSBcW09tZWdhXWk7Cnc9MS1JIFxbT21lZ2FdOwp6PVxbT21lZ2FdXjIvMitJIFxbT21lZ2FdLzI7CigxL1xbUGldKSBOSW50ZWdyYXRlW1JlW1xbQ2FwaXRhbFBoaV1oYXRbXFtPbWVnYV0sS10gRXhwW0kgXFtPbWVnYV0geF0gR1tcW09tZWdhXSxULHksdyx6LFxbS2FwcGFdLFxbVGhldGFdLFxbRGVsdGFdLFxbUmhvXSxcW0dhbW1hXV1dLHtcW09tZWdhXXIsMCxcW0luZmluaXR5XX0sTWV0aG9kLT4iTGV2aW5SdWxlIixXb3JraW5nUHJlY2lzaW9uLT4yMCxQcmVjaXNpb25Hb2FsLT44LE1heFJlY3Vyc2lvbi0+MzBdCl07CgooKiBCbGFjay1TY2hvbGVzIENhbGwgcHJpY2UgKikKYmxhY2tTY2hvbGVzQ2FsbFtGXyxLXyxcW1RhdV1fLFxbU2lnbWFdX106PU1vZHVsZVt7ZDEsZDJ9LApkMT0oTG9nW0YvS10rKFxbU2lnbWFdXjIvMikgXFtUYXVdKS8oXFtTaWdtYV0gU3FydFtcW1RhdV1dKTsKZDI9ZDEtXFtTaWdtYV0gU3FydFtcW1RhdV1dOwpGIENERltOb3JtYWxEaXN0cmlidXRpb25bXSxkMV0tSyBDREZbTm9ybWFsRGlzdHJpYnV0aW9uW10sZDJdXQoKKCpJbXBsaWVkIHZvbGF0aWxpdHkgc29sdmVyIGZvciBnaXZlbiBMIGFuZCBcW1Job10qKQppbXBsaWVkVm9sW1RfLHhfLHlfLFxbS2FwcGFdXyxcW1RoZXRhXV8sXFtEZWx0YV1fLFxbUmhvXV8sXFtHYW1tYV1fLExfXTo9TW9kdWxlW3tLLGNNb2RlbCxjRm9yd2FyZCxGfSwKSz1FeHBbeCtMXS9CW1QseSxcW0thcHBhXSxcW1RoZXRhXSxcW0RlbHRhXV07CmNNb2RlbD1jYWxsUHJpY2VbVCx4LHksXFtLYXBwYV0sXFtUaGV0YV0sXFtEZWx0YV0sXFtSaG9dLFxbR2FtbWFdLEtdOwpjRm9yd2FyZD1jTW9kZWwvQltULHksXFtLYXBwYV0sXFtUaGV0YV0sXFtEZWx0YV1dOwpGPUV4cFt4XS9CW1QseSxcW0thcHBhXSxcW1RoZXRhXSxcW0RlbHRhXV07CklmW2NGb3J3YXJkPD0wfHxjRm9yd2FyZD49RXhwW3hdLFJldHVyblswXV07ClxbU2lnbWFdLy4gUXVpZXRARmluZFJvb3RbYmxhY2tTY2hvbGVzQ2FsbFtGLEssVCxcW1NpZ21hXV09PWNGb3J3YXJkLHtcW1NpZ21hXSwwLjJ9LE1heEl0ZXJhdGlvbnMtPjEwMCxXb3JraW5nUHJlY2lzaW9uLT4yMF1dCgooKlBhcmFtZXRlcnMqKQpcW0thcHBhXT0wLjU7ICAgICAgICgqbWVhbiByZXZlcnNpb24gc3BlZWQtbW9kZXJhdGUqKQpcW1RoZXRhXT0wLjA1OyAgICAgICgqbG9uZy10ZXJtIG1lYW4gaW50ZXJlc3QgcmF0ZSB+NSUqKQpcW0RlbHRhXT0wLjk1U3FydFsyIFxbS2FwcGFdIFxbVGhldGFdXTsgICAgICAoKnZvbGF0aWxpdHkgb2YgWS10eXBpY2FsIGZvciByYXRlcyopClxbR2FtbWFdPTAuMlNxcnRbXFtUaGV0YV1dOyAgICAgKCp2b2xhdGlsaXR5IHBhcmFtOmluaXRpYWwgdm9sIFxbR2FtbWFdL1xbU3FydF1cW1RoZXRhXVxbVGlsZGVUaWxkZV0wLjIqKQp0PTA7ICgqIGluaXRpYWwgdGltZSAqKQp4PUxvZ1sxMDBdOyAoKmN1cnJlbnQgbG9nLXByaWNlLCBTMD0xMDAqKQp5PVxbVGhldGFdOyAgICAgKCppbml0aWFsIHNob3J0IHJhdGUgfjUlKikKClByaW50WyJQbG90IEltcGxpZWQgVm9sIGFzIGEgZnVuY3Rpb24gb2YgTG9nIE1vbmV5bmVzcywgVCA9IDAuMjUiXQpMbWluPS0wLjM7CkxtYXg9MC4zOwpUPTAuMjU7ClBsb3RbewppbXBsaWVkVm9sW1QseCx5LFxbS2FwcGFdLFxbVGhldGFdLFxbRGVsdGFdLDEsXFtHYW1tYV0sTF0sCmltcGxpZWRWb2xbVCx4LHksXFtLYXBwYV0sXFtUaGV0YV0sXFtEZWx0YV0sMS8yLFxbR2FtbWFdLExdLAppbXBsaWVkVm9sW1QseCx5LFxbS2FwcGFdLFxbVGhldGFdLFxbRGVsdGFdLDAsXFtHYW1tYV0sTF0KfSx7TCxMbWluLExtYXh9LFBsb3RQb2ludHMtPjMwLE1heFJlY3Vyc2lvbi0+MCwKUGxvdFN0eWxlLT57e0JsYWNrLERvdHRlZH0se0JsYWNrLERhc2hlZH0sQmxhY2t9XQoKUHJpbnRbIlBsb3QgSW1wbGllZCBWb2wgYXMgYSBmdW5jdGlvbiBvZiBMb2cgTW9uZXluZXNzLCBUID0gMS4wIl0KTG1pbj0tMC41OwpMbWF4PTAuNTsKVD0xLjA7ClBsb3RbewppbXBsaWVkVm9sW1QseCx5LFxbS2FwcGFdLFxbVGhldGFdLFxbRGVsdGFdLDEsXFtHYW1tYV0sTF0sCmltcGxpZWRWb2xbVCx4LHksXFtLYXBwYV0sXFtUaGV0YV0sXFtEZWx0YV0sMS8yLFxbR2FtbWFdLExdLAppbXBsaWVkVm9sW1QseCx5LFxbS2FwcGFdLFxbVGhldGFdLFxbRGVsdGFdLDAsXFtHYW1tYV0sTF0KfSx7TCxMbWluLExtYXh9LFBsb3RQb2ludHMtPjMwLE1heFJlY3Vyc2lvbi0+MCwKUGxvdFN0eWxlLT57e0JsYWNrLERvdHRlZH0se0JsYWNrLERhc2hlZH0sQmxhY2t9XQo=)

1ClearAll["Global‘\*"]

2

3(\* Bond Price \*)

4B[T\_,y\_,\[Kappa]\_,\[Theta]\_,\[Delta]\_]:=Module[{\[Gamma]1,B1,A1},

5\[Gamma]1=Sqrt[\[Kappa]^2+2 \[Delta]^2];

6B1=(2 (Exp[\[Gamma]1 T]-1))/((\[Kappa]+\[Gamma]1) (Exp[\[Gamma]1 T]-1)+2 \[Gamma]1);A1=(2 \[Gamma]1 Exp[(\[Kappa]+\[Gamma]1) T/2]/((\[Kappa]+\[Gamma]1) (Exp[\[Gamma]1 T]-1)+2 \[Gamma]1))^(2 \[Kappa] \[Theta]/\[Delta]^2);

7A1 Exp[-B1 y]

8]

9

10(\*Mathematica Code for G^CIR (Equation 10) Source:"Explicit formulas for Laplace transforms of stochastic integrals" by T.R.Hurd and A.Kuznetsov.\*)

11

12GCIR[T\_,x\_,d1\_,d2\_,w1\_,w2\_,a\_,b\_,c\_]:=Module[{\[Alpha],\[Beta],v1,v2,\[Gamma]T,zArg,exponentTerm,preFactor,hyperGeomTerm},

13\[Alpha]=2\*a/c^2-1;

14\[Beta]=2\*b/c^2;

15v1=1/2\*(-\[Beta]+Sqrt[\[Beta]^2+8\*d1/c^2]);

16v2=1/2\*(-\[Alpha]+Sqrt[\[Alpha]^2+8\*d2/c^2]);

17\[Gamma]T=(\[Beta]+2\*v1)/(1-Exp[-(\[Beta]/2+v1)\*c^2\*T]);

18zArg=-((\[Gamma]T^2\*x\*Exp[-(\[Beta]/2+v1)\*c^2\*T])/(\[Gamma]T+w1-v1));

19preFactor=Exp[-(a\*v1+b\*v2+c^2\*v1\*v2)\*T]\*x^v2\*(\[Gamma]T+w1-v1)^(-\[Alpha]-v2-w2-1)\*\[Gamma]T^(\[Alpha]+2\*v2+1);

20exponentTerm=Exp[-x\*(v1+(\[Gamma]T\*(w1-v1))/(\[Gamma]T+w1-v1)\*Exp[-(\[Beta]/2+v1)\*c^2\*T])];

21hyperGeomTerm=(Gamma[\[Alpha]+v2+w2+1]/Gamma[\[Alpha]+2\*v2+1])\*Hypergeometric1F1[v2-w2,\[Alpha]+2\*v2+1,zArg];

22preFactor\*exponentTerm\*hyperGeomTerm

23];

24

25G[\[Omega]\_,T\_,y\_,w\_,z\_,\[Kappa]\_,\[Theta]\_,\[Delta]\_,\[Rho]\_,\[Gamma]\_]:=Module[{a,b,c,x,d1,d2,w1,w2},

26a=\[Kappa] (\[Theta] + I \[Omega] \[Rho] \[Delta] \[Gamma] / \[Kappa]);

27b=\[Kappa];

28c=\[Delta];

29x=y;

30d1=w;

31d2=\[Gamma]^2 z;

32w1=0;

33w2=0;

34GCIR[T,x,d1,d2,w1,w2,a,b,c]

35];

36

37\[CapitalPhi]hat[\[Omega]\_,K\_]:=-K^(1-I \[Omega])/(\[Omega]^2+I \[Omega]);

38

39callPrice[T\_,x\_,y\_,\[Kappa]\_,\[Theta]\_,\[Delta]\_,\[Rho]\_,\[Gamma]\_,K\_]:=Module[{\[Omega]i,\[Omega],w,z},

40\[Omega]i=-1.5;

41\[Omega]=\[Omega]r + I \[Omega]i;

42w=1-I \[Omega];

43z=\[Omega]^2/2+I \[Omega]/2;

44(1/\[Pi]) NIntegrate[Re[\[CapitalPhi]hat[\[Omega],K] Exp[I \[Omega] x] G[\[Omega],T,y,w,z,\[Kappa],\[Theta],\[Delta],\[Rho],\[Gamma]]],{\[Omega]r,0,\[Infinity]},Method->"LevinRule",WorkingPrecision->20,PrecisionGoal->8,MaxRecursion->30]

45];

46

47(\* Black-Scholes Call price \*)

48blackScholesCall[F\_,K\_,\[Tau]\_,\[Sigma]\_]:=Module[{d1,d2},

49d1=(Log[F/K]+(\[Sigma]^2/2) \[Tau])/(\[Sigma] Sqrt[\[Tau]]);

50d2=d1-\[Sigma] Sqrt[\[Tau]];

51F CDF[NormalDistribution[],d1]-K CDF[NormalDistribution[],d2]]

52

53(\*Implied volatility solver for given L and \[Rho]\*)

54impliedVol[T\_,x\_,y\_,\[Kappa]\_,\[Theta]\_,\[Delta]\_,\[Rho]\_,\[Gamma]\_,L\_]:=Module[{K,cModel,cForward,F},

55K=Exp[x+L]/B[T,y,\[Kappa],\[Theta],\[Delta]];

56cModel=callPrice[T,x,y,\[Kappa],\[Theta],\[Delta],\[Rho],\[Gamma],K];

57cForward=cModel/B[T,y,\[Kappa],\[Theta],\[Delta]];

58F=Exp[x]/B[T,y,\[Kappa],\[Theta],\[Delta]];

59If[cForward<=0||cForward>=Exp[x],Return[0]];

60\[Sigma]/. Quiet@FindRoot[blackScholesCall[F,K,T,\[Sigma]]==cForward,{\[Sigma],0.2},MaxIterations->100,WorkingPrecision->20]]

61

62(\*Parameters\*)

63\[Kappa]=0.5; (\*mean reversion speed-moderate\*)

64\[Theta]=0.05; (\*long-term mean interest rate ~5%\*)

65\[Delta]=0.95Sqrt[2 \[Kappa] \[Theta]]; (\*volatility of Y-typical for rates\*)

66\[Gamma]=0.2Sqrt[\[Theta]]; (\*volatility param:initial vol \[Gamma]/\[Sqrt]\[Theta]\[TildeTilde]0.2\*)

67t=0; (\* initial time \*)

68x=Log[100]; (\*current log-price, S0=100\*)

69y=\[Theta]; (\*initial short rate ~5%\*)

70

71Print["Plot Implied Vol as a function of Log Moneyness, T = 0.25"]

72Lmin=-0.3;

73Lmax=0.3;

74T=0.25;

75Plot[{

76impliedVol[T,x,y,\[Kappa],\[Theta],\[Delta],1,\[Gamma],L],

77impliedVol[T,x,y,\[Kappa],\[Theta],\[Delta],1/2,\[Gamma],L],

78impliedVol[T,x,y,\[Kappa],\[Theta],\[Delta],0,\[Gamma],L]

79},{L,Lmin,Lmax},PlotPoints->30,MaxRecursion->0,

80PlotStyle->{{Black,Dotted},{Black,Dashed},Black}]

81

82Print["Plot Implied Vol as a function of Log Moneyness, T = 1.0"]

83Lmin=-0.5;

84Lmax=0.5;

85T=1.0;

86Plot[{

87impliedVol[T,x,y,\[Kappa],\[Theta],\[Delta],1,\[Gamma],L],

88impliedVol[T,x,y,\[Kappa],\[Theta],\[Delta],1/2,\[Gamma],L],

89impliedVol[T,x,y,\[Kappa],\[Theta],\[Delta],0,\[Gamma],L]

90},{L,Lmin,Lmax},PlotPoints->30,MaxRecursion->0,

91PlotStyle->{{Black,Dotted},{Black,Dashed},Black}]

## References

* Anderson et al. [2020]

  J. Anderson, P. Kearney, and S. Lee.
  Fed announcements and intraday VIX dynamics.
  *Journal of Financial Markets*, 48:100530, 2020.
  doi: 10.1016/j.finmar.2020.100530.
* Bekaert and Hoerova [2014]

  G. Bekaert and M. Hoerova.
  The VIX and expected stock market returns.
  *Management Science*, 60(5):1245–1261,
  2014.
  doi: 10.1287/mnsc.2013.1845.
* Bernanke [2005]

  B. S. Bernanke.
  Monetary policy and asset prices.
  *Journal of Economic Perspectives*, 19(4):33–54, 2005.
  doi: 10.1257/089533005774357745.
* Cox et al. [1985]

  J. C. Cox, J. E. Ingersoll, Jr., and S. A. Ross.
  A theory of the term structure of interest rates.
  *Econometrica*, 53(2):385–408, 1985.
* Delbaen and Shirakawa [2002]

  F. Delbaen and H. Shirakawa.
  An interest rate model with upper and lower bounds.
  *Asia-Pacific Financial Markets*, 9(3):191–209, 2002.
* Gürkaynak et al. [2005]

  R. S. Gürkaynak, B. P. Sack, and E. T. Swanson.
  The effects of monetary policy on asset prices.
  *Journal of Monetary Economics*, 52(6):1155–1180, 2005.
  doi: 10.1016/j.jmoneco.2005.02.001.
* Hurd and Kuznetsov [2008]

  T. R. Hurd and A. Kuznetsov.
  Explicit formulas for Laplace transforms of stochastic integrals.
  *Markov Processes and Related Fields*, 14(2):277–290, 2008.
* Liu et al. [2022]

  Y. Liu, W. Zhang, and M. Chen.
  Rate cuts and equity volatility: Evidence from the post‑COVID
  era.
  *Review of Financial Studies*, 35(8):3821–3865, 2022.
  doi: 10.1093/rfs/hhac045.

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| =0.25\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}=0.25 | =1.00\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}=1.00 |

Figure 1: The implied volatility ς0(,)\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\sigmaup\_{0}({\mst@T\/},{\mst@L\/}) is plotted as a function of log-moneyness for two different maturities, =0.25\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}=0.25 and =1.00\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@T\/}=1.00, and three correlation coefficients, ρ=0.00\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup=0.00 (solid), ρ=0.5\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup=0.5 (dashed) and ρ=1.00\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\rhoup=1.00 (dotted). Other parameters are fixed at the following values: ϰ=0.5\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\kappaup=0.5, ϑ=0.05\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\thetaup=0.05, δ=0.95​2​ϰ​ϑ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\deltaup=0.95\sqrt{2\kappaup\thetaup}, γ=0.2​ϑ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar\gammaup=0.2\sqrt{\thetaup}, t=0\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{\mst@t}=0, =0log100\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}\_{0}=\log 100, and =0ϑ\mst@varfam@dot\mst@varfam@slash\mst@varfam@vbar{}\_{0}=\thetaup.