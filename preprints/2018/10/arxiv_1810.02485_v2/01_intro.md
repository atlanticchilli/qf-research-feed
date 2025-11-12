---
authors:
- Alex Garivaltis
doc_id: arxiv:1810.02485v2
family_id: arxiv:1810.02485
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[1810.02485] Exact Replication of the Best Rebalancing Rule in Hindsight1footnote
  11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments
  that improved the paper.'
url_abs: http://arxiv.org/abs/1810.02485v2
url_html: https://ar5iv.org/html/1810.02485v2
venue: arXiv q-fin
version: 2
year: 2018
---

###### Abstract

This paper prices and replicates the financial derivative whose payoff at T𝑇T is the wealth that would have accrued to a $1currency-dollar1\$1 deposit into the best continuously-rebalanced portfolio (or fixed-fraction betting scheme) determined in hindsight. For the single-stock Black-Scholes market, Ordentlich and Cover (1998) only priced this derivative at time-0, giving C0=1+σ​T/(2​π)subscript𝐶01𝜎𝑇2𝜋C\_{0}=1+\sigma\sqrt{T/(2\pi)}. Of course, the general time-t𝑡t price is not equal to 1+σ​(T−t)/(2​π)1𝜎𝑇𝑡2𝜋1+\sigma\sqrt{(T-t)/(2\pi)}.

I complete the Ordentlich-Cover (1998) analysis by deriving the price at any time t𝑡t. By contrast, I also study the more natural case of the best levered rebalancing rule in hindsight. This yields C​(S,t)=T/t⋅exp⁡{r​t+σ2​b​(S,t)2⋅t/2}𝐶𝑆𝑡⋅𝑇𝑡𝑟𝑡⋅superscript𝜎2𝑏superscript𝑆𝑡2𝑡2C(S,t)=\sqrt{T/t}\cdot\,\exp\{rt+\sigma^{2}b(S,t)^{2}\cdot t/2\}, where b​(S,t)𝑏𝑆𝑡b(S,t) is the best rebalancing rule in hindsight over the observed history [0,t]0𝑡[0,t]. I show that the replicating strategy amounts to betting the fraction b​(S,t)𝑏𝑆𝑡b(S,t) of wealth on the stock over the interval [t,t+d​t].𝑡𝑡𝑑𝑡[t,t+dt]. This fact holds for the general market with n𝑛n correlated stocks in geometric Brownian motion: we get C​(S,t)=(T/t)n/2​exp⁡(r​t+b′​Σ​b⋅t/2)𝐶𝑆𝑡superscript𝑇𝑡𝑛2𝑟𝑡⋅superscript𝑏′Σ𝑏𝑡2C(S,t)=(T/t)^{n/2}\exp(rt+b^{\prime}\Sigma b\cdot t/2), where ΣΣ\Sigma is the covariance of instantaneous returns per unit time. This result matches the 𝒪​(Tn/2)𝒪superscript𝑇𝑛2\mathcal{O}(T^{n/2}) “cost of universality” derived by Cover in his “universal portfolio theory” (1986, 1991, 1996, 1998), which super-replicates the same derivative in discrete-time. The replicating strategy compounds its money at the same asymptotic rate as the best levered rebalancing rule in hindsight, thereby beating the market asymptotically. Naturally enough, we find that the American-style version of Cover’s Derivative is never exercised early in equilibrium.

Keywords: Exotic Options, Lookback Options, Correlation Options, Continuously-Rebalanced Portfolios, Kelly Criterion, Universal Portfolios, Dynamic Replication

JEL Classification: C44, D53, D81, G11, G13

## 1 Introduction

The exotic option literature has several examples (Wilmott 1998) of derivatives with “lookback” or “no-regret” features. For example, a floating-strike lookback call allows its owner to look back at the price history of a given stock, buy a share at the realized minimum m:=min1≤t≤T​Stassign𝑚1𝑡𝑇subscript𝑆𝑡m:=\underset{1\leq t\leq T}{\min}\,\,S\_{t}, and sell it at the terminal price STsubscript𝑆𝑇S\_{T}. Similarly, a fixed-strike lookback call allows its owner to buy one share at a fixed price K𝐾K, and sell it at the historical maximum M:=max1≤t≤T​Stassign𝑀1𝑡𝑇subscript𝑆𝑡M:=\underset{1\leq t\leq T}{\max}\,\,S\_{t}.

This paper prices and replicates a markedly different type of lookback option, whose payoff is equal to the final wealth that would have accrued to a $1currency-dollar1\$1 deposit into the best continuous rebalancing rule (or fixed-fraction betting scheme) determined in hindsight. This contingent claim has been studied by Cover and his collaborators (1986, 1991, 1996, 1998) who used it as a performance benchmark for discrete-time portfolio selection algorithms. Ordentlich and Cover’s important (1998) paper (on the “max-min universal portfolio”) super-replicates this derivative in discrete-time.

In the context of one underlying stock, a rebalancing rule is a fixed-fraction betting scheme that continuously maintains some fraction b∈(−∞,+∞)𝑏b\in(-\infty,+\infty) of wealth in the stock and keeps the rest in cash. The portfolio is held for the differential time interval [t,t+d​t]𝑡𝑡𝑑𝑡[t,t+dt], at which point it is rebalanced to the target allocation. If b>1𝑏1b>1, the scheme uses margin loans, but continuously maintains a fixed debt-to-assets ratio of 1−1/b11𝑏1-1/b. Say, for b=2𝑏2b=2 the scheme would keep a 50%percent5050\% loan-to-value ratio at all times. Thus, when the stock rises, the trader instantly adjusts by borrowing additional cash against his new wealth. Similarly, on a downtick he will de-lever himself by selling a precise amount of the stock. For example, using b=2𝑏2b=2 on the S&P 500 index from January 2012 through August 2018 would have, under monthly rebalancing, compounded one’s money at 31.8%percent31.831.8\% annually, as compared to buying and holding the index (b=1𝑏1b=1), which would have yielded 15.6%percent15.615.6\% annually. This is illustrated in Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.").

![Refer to caption](/html/1810.02485/assets/200.png)


Figure 1: b=2𝑏2b=2 for Vanguard S&P 500 index ETF under monthly rebalancing, Jan 2012-Aug 2018.

By contrast to the constant leveraged (2x) exposure discussed above, rebalancing rules b∈(0,1)𝑏01b\in(0,1) amount to “volatility harvesting” strategies (Luenberger 1998) that “live off the fluctuations” of the underlying. Such rules are mechanical schemes for “buying the dips and selling the rips,” and they profit from mean-reversion in cyclical or “sideways” markets. For example, using b=0.5𝑏0.5b=0.5 for shares of Advanced Micro Devices (AMD) with monthly rebalancing over the author’s lifetime (April 1986 through August 2018), the trader would have compounded at 7.79%percent7.797.79\% per year, compared to 1.77%percent1.771.77\% for b=1𝑏1b=1. This is illustrated in Figure [2](#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.").

![Refer to caption](/html/1810.02485/assets/amd.png)


Figure 2: b=0.5𝑏0.5b=0.5 for AMD shares under monthly rebalancing, Apr 1986-Aug 2018.

These examples make it clear that the best rebalancing rule in hindsight will handily outperform the underlying over long periods. For an underlying whose price failed to rise during the lookback period, the best rebalancing rule in hindsight can outperform by holding all cash (b=0𝑏0b=0) or by shorting the stock (b<0𝑏0b<0). Inevitably, one lives to regret the fact that he did not use the best rebalancing rule in hindsight. In 1986, no one could have reliably predicted that b=0.5𝑏0.5b=0.5 would beat AMD by 6 percent a year. But (at least in the Black-Scholes world) it was possible to delta-hedge the final wealth of the best continuous rebalancing rule in hindsight. Such is the business of this paper.

### 1.1 Contribution

Ordentlich and Cover (1998) priced this derivative at time-0, for a single underlying with unlevered hindsight optimization. The last result in their paper is the formula C0=1+σ​T/(2​π)subscript𝐶01𝜎𝑇2𝜋C\_{0}=1+\sigma\sqrt{T/(2\pi)}, where T𝑇T is the horizon and σ𝜎\sigma is the volatility. Of course, the general time-t𝑡t price is not equal to 1+σ​(T−t)/(2​π)1𝜎𝑇𝑡2𝜋1+\sigma\sqrt{(T-t)/(2\pi)}. Accordingly, this paper completes the Ordentlich-Cover (1998) analysis, deriving the eponymous Cost of Achieving the Best (constant-rebalanced) Portfolio in Hindsight at any time t𝑡t, for levered hindsight optimization over any number of correlated stocks in geometric Brownian motion. When leverage is allowed in the hindsight optimization, replication becomes especially simple. At time t𝑡t, we just look back at the observed history [0,t]0𝑡[0,t] and compute the best (currently known) rebalancing rule in hindsight, here denoted b​(S,t)𝑏𝑆𝑡b(S,t). We then bet the fraction b​(S,t)𝑏𝑆𝑡b(S,t) of wealth on the stock over [t,t+d​t]𝑡𝑡𝑑𝑡[t,t+dt]. This is equivalent to holding Δ​(S,t):=b​(S,t)​C​(S,t)/SassignΔ𝑆𝑡𝑏𝑆𝑡𝐶𝑆𝑡𝑆\Delta(S,t):=b(S,t)C(S,t)/S shares of the stock in state (S,t)𝑆𝑡(S,t). The replicating strategy serves to translate Ordentlich and Cover’s (1998) “max-min universal portfolio” into continuous time. Thus, the present paper does for Ordentlich and Cover (1998) what Jamshidian (1992) did for Cover’s original (1991) performance-weighted universal portfolio.

### 1.2 Related Literature

Cover’s universal portfolios (and the corresponding individual sequence approach to investment) have generated a thriving literature in mathematical finance, computer science, and machine learning. Parkes and Huberman (2001) study a cooperative multiagent search model of portfolio selection. Barron and Yu (2003) supply investment strategies that are universal with respect to constant-rebalanced option portfolios. Iyengar (2005) analyzes universal growth-optimal investment in a discrete-time market with transaction costs. Stoltz and Lugosi (2005) extend the concept of internal regret to the on-line portfolio selection problem. They develop sequential investment strategies that minimize cumulative internal regret under model uncertainty. DeMarzo, Kremer, and Mansour (2006) use on-line trading algorithms and regret minimization to derive robust bounds for option prices. Györfi, Lugosi, and Udina (2006) study kernel-based sequential investment strategies that guarantee optimal capital growth for markets with ergodic stationary return processes. Kozat and Singer (2011) deal with semiconstant-rebalanced portfolios that rebalance only at selected points in time, and thus may avoid rebalancing if the prospective benefits are outweighed by transaction costs. They exhibit on-line investment strategies that asymptotically achieve the wealth of the best semiconstant-rebalanced portfolio for the realized sequence of asset returns. Rujeerapaiboon, Kuhn, and Wiesemann (2015) use robust optimization techniques to build fixed-mix strategies offering performance guarantees that are similar to the growth-optimal portfolio.

Portfolio rebalancing is a key tenet of Fernholz’s (2002) stochastic portfolio theory. Wong (2015) extends Cover’s universal portfolio to the nonparametric family of functionally generated portfolios in stochastic portfolio theory. Cuchiero, Schachermayer, and Wong (2016) show that, under appropriate hypotheses, the asymptotic compound-growth rate of Cover’s universal portfolio coincides with that of stochastic portfolio theory and the numéraire portfolio. On a more practical basis, rebalancing is a perennially important aspect of tactical asset allocation. For instance, Israelov and Tummala (2018) study short option overlays that can be used to hedge one’s exposure to allocation drift between planned rebalances. Gort and Burgener (2014) describe and backtest option selling techniques that serve to rebalance institutional investors’ asset exposures to predefined targets. An AQR White Paper by Ilmanen and Maloney (2015) discusses the key considerations for investors deciding on whether and how to rebalance their portfolios.

## 2 One Underlying

### 2.1 Payoff Computation

For simplicity, we start with a single underlying stock whose price Stsubscript𝑆𝑡S\_{t} follows the geometric Brownian motion

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=μ​d​t+σ​d​Wt,𝑑subscript𝑆𝑡subscript𝑆𝑡𝜇𝑑𝑡𝜎𝑑subscript𝑊𝑡\frac{dS\_{t}}{S\_{t}}=\mu\,dt+\sigma\,dW\_{t}, |  | (1) |

where μ𝜇\mu is the drift, σ𝜎\sigma is the volatility, and Wtsubscript𝑊𝑡W\_{t} is a standard Brownian motion. There is a risk-free bond whose price Bt:=er​tassignsubscript𝐵𝑡superscript𝑒𝑟𝑡B\_{t}:=e^{rt} follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​BtBt=r​d​t,𝑑subscript𝐵𝑡subscript𝐵𝑡𝑟𝑑𝑡\frac{dB\_{t}}{B\_{t}}=r\,dt, |  | (2) |

where r𝑟r is the continuously-compounded interest rate. We consider constant rebalancing rules, or fixed-fraction betting schemes, that “bet” the fraction b∈(−∞,+∞)𝑏b\in(-\infty,+\infty) of wealth on the stock over the interval [t,t+d​t]𝑡𝑡𝑑𝑡[t,t+dt]. Assume that the gambler starts with $1currency-dollar1\$1, and let Vt=Vt​(b)subscript𝑉𝑡subscript𝑉𝑡𝑏V\_{t}=V\_{t}(b) denote his wealth at t𝑡t. He thus owns b​Vt/St𝑏subscript𝑉𝑡subscript𝑆𝑡bV\_{t}/S\_{t} shares of the stock at t𝑡t, and has the remaining (1−b)​Vt1𝑏subscript𝑉𝑡(1-b)V\_{t} dollars invested in bonds. The gambler’s wealth evolves according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt​(b)Vt​(b)=b​d​StSt+(1−b)​d​BtBt=[r+b​(μ−r)]​d​t+b​σ​d​Wt.𝑑subscript𝑉𝑡𝑏subscript𝑉𝑡𝑏𝑏𝑑subscript𝑆𝑡subscript𝑆𝑡1𝑏𝑑subscript𝐵𝑡subscript𝐵𝑡delimited-[]𝑟𝑏𝜇𝑟𝑑𝑡𝑏𝜎𝑑subscript𝑊𝑡\frac{dV\_{t}(b)}{V\_{t}(b)}=b\,\frac{dS\_{t}}{S\_{t}}+(1-b)\frac{dB\_{t}}{B\_{t}}=[r+b(\mu-r)]dt+b\sigma\,dW\_{t}. |  | (3) |

Since Vt​(b)subscript𝑉𝑡𝑏V\_{t}(b) is a geometric Brownian motion, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(b)=exp⁡{[r+(μ−r)​b−σ2​b2/2]​t+b​σ​Wt}.subscript𝑉𝑡𝑏delimited-[]𝑟𝜇𝑟𝑏superscript𝜎2superscript𝑏22𝑡𝑏𝜎subscript𝑊𝑡V\_{t}(b)=\exp\{[r+(\mu-r)b-\sigma^{2}b^{2}/2]t+b\sigma W\_{t}\}. |  | (4) |

In the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​exp⁡{(μ−σ2/2)​t+σ​Wt},subscript𝑆𝑡subscript𝑆0𝜇superscript𝜎22𝑡𝜎subscript𝑊𝑡S\_{t}=S\_{0}\exp\{(\mu-\sigma^{2}/2)t+\sigma W\_{t}\}, |  | (5) |

we can solve for σ​Wt𝜎subscript𝑊𝑡\sigma W\_{t} in terms of Stsubscript𝑆𝑡S\_{t}, and substitute the resulting expression into ([4](#S2.E4 "In 2.1 Payoff Computation ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.")). This yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(b)=exp⁡{(r−σ2​b2/2)​t+b​[log⁡(St/S0)−(r−σ2/2)​t]}.subscript𝑉𝑡𝑏𝑟superscript𝜎2superscript𝑏22𝑡𝑏delimited-[]subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑡V\_{t}(b)=\exp\{(r-\sigma^{2}b^{2}/2)t+b[\log(S\_{t}/S\_{0})-(r-\sigma^{2}/2)t]\}. |  | (6) |

Thus, we note that Vt​(b)subscript𝑉𝑡𝑏V\_{t}(b) can be calculated without any explicit reference to the drift parameter μ𝜇\mu. The trader’s wealth is Markovian: it depends only on the current state (St,t)subscript𝑆𝑡𝑡(S\_{t},t).

To find the best rebalancing rule in hindsight over [0,t]0𝑡[0,t], we maximize Vt​(b)subscript𝑉𝑡𝑏V\_{t}(b) with respect to b𝑏b. Since the exponent is quadratic in b𝑏b, the best rebalancing rule in hindsight over [0,t]0𝑡[0,t] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(St,t):=log⁡(St/S0)−(r−σ2/2)​tσ2​t.assign𝑏subscript𝑆𝑡𝑡subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑡superscript𝜎2𝑡\boxed{b(S\_{t},t):=\frac{\log(S\_{t}/S\_{0})-(r-\sigma^{2}/2)t}{\sigma^{2}t}}. |  | (7) |

If we write μ^​(S,t):=log⁡(S/S0)/t+σ2/2assign^𝜇𝑆𝑡𝑆subscript𝑆0𝑡superscript𝜎22\hat{\mu}(S,t):=\log(S/S\_{0})/t+\sigma^{2}/2, we get the expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(S,t)=μ^​(S,t)−rσ2.𝑏𝑆𝑡^𝜇𝑆𝑡𝑟superscript𝜎2\boxed{b(S,t)=\frac{\hat{\mu}(S,t)-r}{\sigma^{2}}}. |  | (8) |

Let Vt∗:=maxb∈ℝ⁡Vt​(b)assignsuperscriptsubscript𝑉𝑡subscript𝑏ℝsubscript𝑉𝑡𝑏V\_{t}^{\*}:=\max\limits\_{b\in\mathbb{R}}V\_{t}(b) denote the final wealth of the best levered rebalancing rule in hindsight over [0,t]0𝑡[0,t]. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∗=exp⁡{r​t+σ2​b​(S,t)2⋅t/2}.superscriptsubscript𝑉𝑡𝑟𝑡⋅superscript𝜎2𝑏superscript𝑆𝑡2𝑡2\boxed{V\_{t}^{\*}=\exp\{rt+\sigma^{2}b(S,t)^{2}\cdot t/2\}}. |  | (9) |

Figure [3](#S2.F3 "Figure 3 ‣ 2.1 Payoff Computation ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") plots this payoff for different volatilities, assuming a risk-free rate of r:=0assign𝑟0r:=0 over a horizon of T:=5assign𝑇5T:=5 years.

![Refer to caption](/html/1810.02485/assets/payoff.png)


Figure 3: The payoff of Cover’s Derivative for levered hindsight optimization, T:=5,S0:=100,r:=0.formulae-sequenceassign𝑇5formulae-sequenceassignsubscript𝑆0100assign𝑟0T:=5,S\_{0}:=100,r:=0.

In Ordentlich and Cover (1998), the hindsight optimization is over unlevered rebalancing rules b∈[0,1]𝑏01b\in[0,1], and in that context, the best unlevered rebalancing rule in hindsight is bu​(S,t):=max⁡{min⁡{b​(S,t),1},0}assignsuperscript𝑏𝑢𝑆𝑡𝑏𝑆𝑡10b^{u}(S,t):=\max\{\min\{b(S,t),1\},0\}. Thus, they use the payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∗:=max0≤b≤1⁡Vt​(b)={er​tif​b​(S,t)≤0exp⁡{r​t+σ2​b​(S,t)2⋅t/2}if​  0≤b​(S,t)≤1St/S0if​b​(S,t)≥1.assignsuperscriptsubscript𝑉𝑡subscript0𝑏1subscript𝑉𝑡𝑏casessuperscript𝑒𝑟𝑡if𝑏𝑆𝑡0𝑟𝑡⋅superscript𝜎2𝑏superscript𝑆𝑡2𝑡2if  0𝑏𝑆𝑡1subscript𝑆𝑡subscript𝑆0if𝑏𝑆𝑡1\displaystyle\boxed{V\_{t}^{\*}:=\max\_{0\leq b\leq 1}V\_{t}(b)=\left\{\begin{array}[]{cc}e^{rt}&\hskip 14.22636pt\text{if}\,\,b(S,t)\leq 0\\ \exp\{rt+\sigma^{2}b(S,t)^{2}\cdot t/2\}&\hskip 14.22636pt\text{if}\,\,0\leq b(S,t)\leq 1\\ S\_{t}/S\_{0}&\text{if}\,\,b(S,t)\geq 1\\ \end{array}\right.}. |  | (13) |

Figure [4](#S2.F4 "Figure 4 ‣ 2.1 Payoff Computation ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") plots the unlevered payoff for different volatilities, assuming a risk-free rate of r:=0assign𝑟0r:=0 over a horizon of T:=2assign𝑇2T:=2 years.

![Refer to caption](/html/1810.02485/assets/payoffUnlevered.png)


Figure 4: The payoff of Cover’s Derivative for unlevered hindsight optimization, T:=2,S0:=100,r:=0.formulae-sequenceassign𝑇2formulae-sequenceassignsubscript𝑆0100assign𝑟0T:=2,S\_{0}:=100,r:=0.

Consider the European-style derivative (“hindsight allocation option”) whose payoff at T𝑇T is VT∗​(ST)superscriptsubscript𝑉𝑇subscript𝑆𝑇V\_{T}^{\*}(S\_{T}).
Let ℚℚ\mathbb{Q} denote the equivalent martingale measure. Ordentlich and Cover (1998) computed the expected present value

|  |  |  |  |
| --- | --- | --- | --- |
|  | C0:=e−r​T​𝔼0ℚ​[VT∗]=1+σ​T2​πassignsubscript𝐶0superscript𝑒𝑟𝑇superscriptsubscript𝔼0ℚdelimited-[]superscriptsubscript𝑉𝑇1𝜎𝑇2𝜋\boxed{C\_{0}:=e^{-rT}\mathbb{E}\_{0}^{\mathbb{Q}}[V\_{T}^{\*}]=1+\sigma\sqrt{\frac{T}{2\pi}}} |  | (14) |

with respect to ℚℚ\mathbb{Q} and the information available at t=0𝑡0t=0. If someone buys a dollar’s worth of this derivative at t=0𝑡0t=0 (for some distant expiration date T𝑇T), he will compound his money at the same asymptotic rate as the best unlevered rebalancing rule in hindsight. His initial dollar buys him 1/C01subscript𝐶01/C\_{0} units of the derivative, yielding final wealth VT∗/{1+σ​T/(2​π)}.superscriptsubscript𝑉𝑇1𝜎𝑇2𝜋V\_{T}^{\*}/\big{\{}1+\sigma\sqrt{T/(2\pi)}\big{\}}. After holding the option for T𝑇T years, the excess continuously-compounded growth rate of the best rebalancing rule in hindsight (over and above that of the option holder) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​log⁡VT∗−1T​log⁡{VT∗1+σ​T/(2​π)}=1T​log⁡{1+σ​T2​π},1𝑇subscriptsuperscript𝑉𝑇1𝑇superscriptsubscript𝑉𝑇1𝜎𝑇2𝜋1𝑇1𝜎𝑇2𝜋\frac{1}{T}\log V^{\*}\_{T}-\frac{1}{T}\log\bigg{\{}\frac{V\_{T}^{\*}}{1+\sigma\sqrt{T/(2\pi)}}\bigg{\}}=\frac{1}{T}\log\bigg{\{}1+\sigma\sqrt{\frac{T}{2\pi}}\bigg{\}}, |  | (15) |

which tends to 0 as T→∞→𝑇T\to\infty. Note that the excess growth rate is deterministic. Figure [5](#S2.F5 "Figure 5 ‣ 2.1 Payoff Computation ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") plots this excess growth rate for different volatilities and maturities.

![Refer to caption](/html/1810.02485/assets/regret.png)


Figure 5: Excess continuously-compounded annual growth rate (%) of the best (unlevered) rebalancing rule in hindsight over that of the replicating strategy.

### 2.2 No-Arbitrage Price

We find it somewhat more natural to start with levered hindsight optimization, corresponding to the payoff VT∗:=maxb∈ℝ⁡VT​(b)assignsuperscriptsubscript𝑉𝑇subscript𝑏ℝsubscript𝑉𝑇𝑏V\_{T}^{\*}:=\max\limits\_{b\in\mathbb{R}}V\_{T}(b). Accordingly, we take up the Black-Scholes (1973) equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​σ2​S2​∂2C∂S2+r​S​∂C∂S+∂C∂t−r​C=012superscript𝜎2superscript𝑆2superscript2𝐶superscript𝑆2𝑟𝑆𝐶𝑆𝐶𝑡𝑟𝐶0\frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}C}{\partial S^{2}}+rS\frac{\partial C}{\partial S}+\frac{\partial C}{\partial t}-rC=0 |  | (16) |

along with the boundary condition C​(S,T):=exp⁡{r​T+σ2​b​(S,T)2⋅T/2}assign𝐶𝑆𝑇𝑟𝑇⋅superscript𝜎2𝑏superscript𝑆𝑇2𝑇2C(S,T):=\exp\{rT+\sigma^{2}b(S,T)^{2}\cdot T/2\}. For convenience, we define the auxiliary variable

|  |  |  |  |
| --- | --- | --- | --- |
|  | zt:=log⁡(St/S0)−(r−σ2/2)​tσ​t,assignsubscript𝑧𝑡subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑡𝜎𝑡\boxed{z\_{t}:=\frac{\log(S\_{t}/S\_{0})-(r-\sigma^{2}/2)t}{\sigma\sqrt{t}}}, |  | (17) |

which is a unit normal with respect to the equivalent martingale measure. Under this notation, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(S,t)=z​(S,t)σ​t.𝑏𝑆𝑡𝑧𝑆𝑡𝜎𝑡\boxed{b(S,t)=\frac{z(S,t)}{\sigma\sqrt{t}}}. |  | (18) |

Thus, the final payoff of Cover’s rebalancing option is

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT∗=exp⁡(r​T+zT2/2).superscriptsubscript𝑉𝑇𝑟𝑇superscriptsubscript𝑧𝑇22V\_{T}^{\*}=\exp(rT+z\_{T}^{2}/2). |  | (19) |

The intrinsic value at time t𝑡t is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∗=exp⁡(r​t+zt2/2).superscriptsubscript𝑉𝑡𝑟𝑡superscriptsubscript𝑧𝑡22\boxed{V\_{t}^{\*}=\exp(rt+z\_{t}^{2}/2)}. |  | (20) |

We proceed to compute the expected discounted payoff with respect to the equivalent martingale measure and the information available at t𝑡t. To this end, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | zT=tT⋅zt+1−tT⋅y,subscript𝑧𝑇⋅𝑡𝑇subscript𝑧𝑡⋅1𝑡𝑇𝑦z\_{T}=\sqrt{\frac{t}{T}}\cdot z\_{t}+\sqrt{1-\frac{t}{T}}\cdot y, |  | (21) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | y:=log⁡(ST/St)−(r−σ2/2)​(T−t)σ​T−t.assign𝑦subscript𝑆𝑇subscript𝑆𝑡𝑟superscript𝜎22𝑇𝑡𝜎𝑇𝑡y:=\frac{\log(S\_{T}/S\_{t})-(r-\sigma^{2}/2)(T-t)}{\sigma\sqrt{T-t}}. |  | (22) |

y𝑦y is a unit normal with respect to the equivalent martingale measure and the information available at t𝑡t. Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼tℚ​[exp⁡(zT2/2)]=exp⁡{t​zt2/(2​T)}2​π​∫−∞∞exp⁡{−t2​T​y2+t​(T−t)T​zt​y}​𝑑y.superscriptsubscript𝔼𝑡ℚdelimited-[]superscriptsubscript𝑧𝑇22𝑡superscriptsubscript𝑧𝑡22𝑇2𝜋superscriptsubscript𝑡2𝑇superscript𝑦2𝑡𝑇𝑡𝑇subscript𝑧𝑡𝑦differential-d𝑦\mathbb{E}\_{t}^{\mathbb{Q}}[\exp(z\_{T}^{2}/2)]=\frac{\exp\{tz\_{t}^{2}/(2T)\}}{\sqrt{2\pi}}\int\limits\_{-\infty}^{\infty}\exp\bigg{\{}-\frac{t}{2T}y^{2}+\frac{\sqrt{t(T-t)}}{T}z\_{t}y\bigg{\}}dy. |  | (23) |

To evaluate the integral, we make note of the general formula (cf. the appendix to Reiner and Rubinstein 1992)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ABe−α​y2+β​y​𝑑y=πα​exp⁡(β24​α)​[N​(B​2​α−β2​α)−N​(A​2​α−β2​α)],superscriptsubscript𝐴𝐵superscript𝑒𝛼superscript𝑦2𝛽𝑦differential-d𝑦𝜋𝛼superscript𝛽24𝛼delimited-[]𝑁𝐵2𝛼𝛽2𝛼𝑁𝐴2𝛼𝛽2𝛼\int\limits\_{A}^{B}e^{-\alpha y^{2}+\beta y}dy=\sqrt{\frac{\pi}{\alpha}}\exp\bigg{(}\frac{\beta^{2}}{4\alpha}\bigg{)}\bigg{[}N\bigg{(}B\sqrt{2\alpha}-\frac{\beta}{\sqrt{2\alpha}}\bigg{)}-N\bigg{(}A\sqrt{2\alpha}-\frac{\beta}{\sqrt{2\alpha}}\bigg{)}\bigg{]}, |  | (24) |

where α>0𝛼0\alpha>0 and N​(⋅)𝑁⋅N(\cdot) is the cumulative normal distribution function. Putting α:=t/(2​T),assign𝛼𝑡2𝑇\alpha:=t/(2T), β:=t​(T−t)T​ztassign𝛽𝑡𝑇𝑡𝑇subscript𝑧𝑡\beta:=\frac{\sqrt{t(T-t)}}{T}z\_{t}, A:=−∞assign𝐴A:=-\infty, and B:=+∞assign𝐵B:=+\infty, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼tℚ​[exp⁡(zT2/2)]=Tt​exp⁡(zt2/2).superscriptsubscript𝔼𝑡ℚdelimited-[]superscriptsubscript𝑧𝑇22𝑇𝑡superscriptsubscript𝑧𝑡22\mathbb{E}\_{t}^{\mathbb{Q}}[\exp(z\_{T}^{2}/2)]=\sqrt{\frac{T}{t}}\exp(z\_{t}^{2}/2). |  | (25) |

###### Theorem 1.

For levered hindsight optimization (over all b∈ℝ𝑏ℝb\in\mathbb{R}), the price of Cover’s rebalancing option is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(S,t)=Tt​exp⁡(r​t+z2/2)=Tt​exp⁡{r​t+σ2​b​(S,t)2⋅t/2}=Tt​Vt∗,𝐶𝑆𝑡𝑇𝑡𝑟𝑡superscript𝑧22𝑇𝑡𝑟𝑡⋅superscript𝜎2𝑏superscript𝑆𝑡2𝑡2𝑇𝑡superscriptsubscript𝑉𝑡\boxed{C(S,t)=\sqrt{\frac{T}{t}}\exp(rt+z^{2}/2)=\sqrt{\frac{T}{t}}\exp\{rt+\sigma^{2}b(S,t)^{2}\cdot t/2\}=\sqrt{\frac{T}{t}}V\_{t}^{\*}}, |  | (26) |

where z:={log⁡(S/S0)−(r−σ2/2)​t}/(σ​t)assign𝑧𝑆subscript𝑆0𝑟superscript𝜎22𝑡𝜎𝑡z:=\{\log(S/S\_{0})-(r-\sigma^{2}/2)t\}/(\sigma\sqrt{t}), b​(S,t)𝑏𝑆𝑡b(S,t) is the best rebalancing rule in hindsight over [0,t]0𝑡[0,t], and Vt∗superscriptsubscript𝑉𝑡V\_{t}^{\*} is the intrinsic value at time t𝑡t.

###### Theorem 2.

The American-style version of Cover’s Derivative (that expires at T𝑇T, has zero exercise price, and pays Vt∗superscriptsubscript𝑉𝑡V\_{t}^{\*} upon exercise at t𝑡t) will never be excercised early in equilibrium. The American price Ca​(S,t)subscript𝐶𝑎𝑆𝑡C\_{a}(S,t) is equal to the European price Ce​(S,t)=T/t⋅Vt∗subscript𝐶𝑒𝑆𝑡⋅𝑇𝑡superscriptsubscript𝑉𝑡C\_{e}(S,t)=\sqrt{T/t}\cdot V\_{t}^{\*}.

###### Proof.

Note that Ce​(St,t)>Vt∗subscript𝐶𝑒subscript𝑆𝑡𝑡superscriptsubscript𝑉𝑡C\_{e}(S\_{t},t)>V\_{t}^{\*} for 0<t<T0𝑡𝑇0<t<T, e.g. the European price of Cover’s Derivative always exceeds the exercise value. To prevent arbitrage opportunities, we must have Ca​(S,t)≥Ce​(S,t)subscript𝐶𝑎𝑆𝑡subscript𝐶𝑒𝑆𝑡C\_{a}(S,t)\geq C\_{e}(S,t) on account of the additional rights granted by the American-style option. Thus, we always have Ca​(St,t)>Vt∗subscript𝐶𝑎subscript𝑆𝑡𝑡superscriptsubscript𝑉𝑡C\_{a}(S\_{t},t)>V\_{t}^{\*}, which means, to quote Merton’s (1973) terminology, that the option is “worth more alive than dead.” In equilibrium, there are always willing buyers ready to pay more than the exercise value, so the option would be sold to such buyers instead of being exercised. Thus, early exercise being useless anyhow, we conclude that Ca​(S,t)=Ce​(S,t)subscript𝐶𝑎𝑆𝑡subscript𝐶𝑒𝑆𝑡C\_{a}(S,t)=C\_{e}(S,t).
∎

To be quite formal about it, the present American option valuation problem (cf. Wilmott 1998) consists in solving the partial differential inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​σ2​S2​∂2C∂S2+r​S​∂C∂S+∂C∂t−r​C≤012superscript𝜎2superscript𝑆2superscript2𝐶superscript𝑆2𝑟𝑆𝐶𝑆𝐶𝑡𝑟𝐶0\frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}C}{\partial S^{2}}+rS\frac{\partial C}{\partial S}+\frac{\partial C}{\partial t}-rC\leq 0 |  | (27) |

together with the side conditions C​(S,T)=VT∗,C​(S,t)≥Vt∗formulae-sequence𝐶𝑆𝑇superscriptsubscript𝑉𝑇𝐶𝑆𝑡superscriptsubscript𝑉𝑡C(S,T)=V\_{T}^{\*},C(S,t)\geq V\_{t}^{\*}, and subject to the proviso that ∂C/∂S𝐶𝑆\partial C/\partial S is continuous. These conditions are all indeed satisfied by the formula C​(S,t)=T/t⋅Vt∗=T/t⋅exp⁡{r​t+z​(S,t)2/2}.𝐶𝑆𝑡⋅𝑇𝑡superscriptsubscript𝑉𝑡⋅𝑇𝑡𝑟𝑡𝑧superscript𝑆𝑡22C(S,t)=\sqrt{T/t}\cdot V\_{t}^{\*}=\sqrt{T/t}\cdot\exp\{rt+z(S,t)^{2}/2\}.

### 2.3 Replicating Strategy and the Greeks

Differentiating the price, we find at once that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ:=∂C∂S=C⋅zS​σ​t=C⋅b​(S,t)S.assignΔ𝐶𝑆⋅𝐶𝑧𝑆𝜎𝑡⋅𝐶𝑏𝑆𝑡𝑆\boxed{\Delta:=\frac{\partial C}{\partial S}=\frac{C\cdot z}{S\sigma\sqrt{t}}=\frac{C\cdot b(S,t)}{S}}. |  | (28) |

or, equivalently, that Δ​S/C=b​(S,t)Δ𝑆𝐶𝑏𝑆𝑡\Delta S/C=b(S,t).

###### Theorem 3.

The replicating strategy for Cover’s Derivative bets the fraction b​(S,t)𝑏𝑆𝑡b(S,t) of wealth on the stock in state (S,t)𝑆𝑡(S,t). Thus, to replicate Cover’s Derivative, one just uses the best rebalancing rule in hindsight as it is known at time t𝑡t.

Hence, for the complete market with a single stock in geometric Brownian motion, assuming levered hindsight optimization, the following three trading strategies are identical:

1. 1.

   The strategy that looks back over the known price history [0,t]0𝑡[0,t], finds the best continuously-rebalanced portfolio in hindsight, and uses that portfolio over the interval [t,t+d​t]𝑡𝑡𝑑𝑡[t,t+dt]
2. 2.

   The ΔΔ\Delta-hedging strategy induced by Cover’s Derivative
3. 3.

   The natural estimator (μ^−r)/σ2^𝜇𝑟superscript𝜎2(\hat{\mu}-r)/\sigma^{2} of the continuous-time Kelly rule (μ−r)/σ𝜇𝑟𝜎(\mu-r)/\sigma (cf. Luenberger 1998)

For reference, we catalog the rest of the Greeks below.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ:=∂Δ∂S=z2−1(S​σ​t)3​CassignΓΔ𝑆superscript𝑧21superscript𝑆𝜎𝑡3𝐶\boxed{\Gamma:=\frac{\partial\Delta}{\partial S}=\frac{z^{2}-1}{(S\sigma\sqrt{t})^{3}}C} |  | (29) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ:=∂C∂t=(r−12​t−z22)​CassignΘ𝐶𝑡𝑟12𝑡superscript𝑧22𝐶\boxed{\Theta:=\frac{\partial C}{\partial t}=\bigg{(}r-\frac{1}{2t}-\frac{z^{2}}{2}\bigg{)}C} |  | (30) |

Thus, there will be significant time decay in the option value for small times t𝑡t and for extreme price realizations in either direction.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν:=∂C∂σ=[t2+r+log⁡(S0/S)σ2​t]​C​z.assign𝜈𝐶𝜎delimited-[]𝑡2𝑟subscript𝑆0𝑆superscript𝜎2𝑡𝐶𝑧\boxed{\nu:=\frac{\partial C}{\partial\sigma}=\bigg{[}\frac{\sqrt{t}}{2}+\frac{r+\log(S\_{0}/S)}{\sigma^{2}t}\bigg{]}Cz}. |  | (31) |

There are generally two implied volatilities that rationalize a given observed value of C𝐶C. To show this, we start with the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | z2=2​(log⁡C−r​t)+log⁡(t/T).superscript𝑧22𝐶𝑟𝑡𝑡𝑇z^{2}=2(\log\,C-rt)+\log(t/T). |  | (32) |

Comparing ([32](#S2.E32 "In 2.3 Replicating Strategy and the Greeks ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.")) with the definition

|  |  |  |  |
| --- | --- | --- | --- |
|  | z2=[log⁡(St/S0)−(r−σ2/2)​t]2σ2​t,superscript𝑧2superscriptdelimited-[]subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑡2superscript𝜎2𝑡z^{2}=\frac{[\log(S\_{t}/S\_{0})-(r-\sigma^{2}/2)t]^{2}}{\sigma^{2}t}, |  | (33) |

we get a quadratic equation in the variance σ2superscript𝜎2\sigma^{2}.
The lowest possible rational option price is T/t⋅er​t⋅𝑇𝑡superscript𝑒𝑟𝑡\sqrt{T/t}\cdot e^{rt}, which corresponds to zt=0subscript𝑧𝑡0z\_{t}=0. This happens if and when St=S0​e(r−σ2/2)​tsubscript𝑆𝑡subscript𝑆0superscript𝑒𝑟superscript𝜎22𝑡S\_{t}=S\_{0}e^{(r-\sigma^{2}/2)t}. Figure [6](#S2.F6 "Figure 6 ‣ 2.3 Replicating Strategy and the Greeks ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") plots the option price against σ𝜎\sigma for the parameters t:=0.5assign𝑡0.5t:=0.5, T:=1assign𝑇1T:=1, r:=0.03assign𝑟0.03r:=0.03, S0:=100assignsubscript𝑆0100S\_{0}:=100, and St:=105assignsubscript𝑆𝑡105S\_{t}:=105.

![Refer to caption](/html/1810.02485/assets/vol.png)


Figure 6: The dual implied volatilities that rationalize an observed price of Cover’s Derivative, t:=0.5assign𝑡0.5t:=0.5, T:=1assign𝑇1T:=1, r:=0.03assign𝑟0.03r:=0.03, S0:=100assignsubscript𝑆0100S\_{0}:=100, St:=105assignsubscript𝑆𝑡105S\_{t}:=105.

Finally, we have the interest rate sensitivity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ:=∂C∂r=[1−b​(S,t)]​C​t.assign𝜌𝐶𝑟delimited-[]1𝑏𝑆𝑡𝐶𝑡\boxed{\rho:=\frac{\partial C}{\partial r}=[1-b(S,t)]Ct}. |  | (34) |

Thus, when the best rebalancing rule in hindsight makes a positive allocation to cash, higher interest rates will make the option more valuable. When the hindsight-optimized rebalancing rule uses margin debt (b​(S,t)>1𝑏𝑆𝑡1b(S,t)>1), higher interest rates will make the option less valuable.

### 2.4 Unlevered Hindsight Optimization

In this subsection, we take up the case of unlevered hindsight optimization, obtaining a more direct generalization of Ordentlich and Cover’s (1998) formula C0=1+σ​T/(2​π)subscript𝐶01𝜎𝑇2𝜋C\_{0}=1+\sigma\sqrt{T/(2\pi)}. Thus, we consider the payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∗:={er​tif​zt≤0exp⁡(r​t+zt2/2)if​  0≤zt≤σ​t,St/S0if​zt≥σ​tassignsuperscriptsubscript𝑉𝑡casessuperscript𝑒𝑟𝑡ifsubscript𝑧𝑡0𝑟𝑡superscriptsubscript𝑧𝑡22if  0subscript𝑧𝑡𝜎𝑡subscript𝑆𝑡subscript𝑆0ifsubscript𝑧𝑡𝜎𝑡\displaystyle V\_{t}^{\*}:=\left\{\begin{array}[]{cc}e^{rt}&\hskip 14.22636pt\text{if}\,\,z\_{t}\leq 0\\ \exp(rt+z\_{t}^{2}/2)&\hskip 14.22636pt\text{if}\,\,0\leq z\_{t}\leq\sigma\sqrt{t},\\ S\_{t}/S\_{0}&\text{if}\,\,z\_{t}\geq\sigma\sqrt{t}\\ \end{array}\right. |  | (38) |

where zt:={log⁡(St/S0)−(r−σ2/2)​t}/(σ​t)assignsubscript𝑧𝑡subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑡𝜎𝑡z\_{t}:=\{\log(S\_{t}/S\_{0})-(r-\sigma^{2}/2)t\}/(\sigma\sqrt{t}).
In this connection, the replicating strategy no longer coincides with the best (unlevered) rebalancing rule in hindsight bu​(S,t)superscript𝑏𝑢𝑆𝑡b^{u}(S,t) over the known history [0,t]0𝑡[0,t].

Again, we make the decomposition zT=t/T⋅zt+1−t/T⋅ysubscript𝑧𝑇⋅𝑡𝑇subscript𝑧𝑡⋅1𝑡𝑇𝑦z\_{T}=\sqrt{t/T}\cdot z\_{t}+\sqrt{1-t/T}\cdot y, where y:={log⁡(ST/St)−(r−σ2/2)​(T−t)}/(σ​T−t)assign𝑦subscript𝑆𝑇subscript𝑆𝑡𝑟superscript𝜎22𝑇𝑡𝜎𝑇𝑡y:=\{\log(S\_{T}/S\_{t})-(r-\sigma^{2}/2)(T-t)\}/(\sigma\sqrt{T-t}). With this terminology, the final payoff becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT∗={er​Tif​y≤−zt​t/(T−t)exp⁡(r​T+zT2/2)if−zt​t/(T−t)≤y≤(σ​T−t​zt)/T−t.ST/S0if​y≥(σ​T−t​zt)/T−tsuperscriptsubscript𝑉𝑇casessuperscript𝑒𝑟𝑇if𝑦subscript𝑧𝑡𝑡𝑇𝑡𝑟𝑇superscriptsubscript𝑧𝑇22ifsubscript𝑧𝑡𝑡𝑇𝑡𝑦𝜎𝑇𝑡subscript𝑧𝑡𝑇𝑡subscript𝑆𝑇subscript𝑆0if𝑦𝜎𝑇𝑡subscript𝑧𝑡𝑇𝑡\displaystyle V\_{T}^{\*}=\left\{\begin{array}[]{cc}e^{rT}&\hskip 14.22636pt\text{if}\,\,y\leq-z\_{t}\sqrt{t/(T-t)}\\ \exp(rT+z\_{T}^{2}/2)&\hskip 14.22636pt\text{if}\,\,-z\_{t}\sqrt{t/(T-t)}\leq y\leq(\sigma T-\sqrt{t}z\_{t})/\sqrt{T-t}.\\ S\_{T}/S\_{0}&\text{if}\,\,y\geq(\sigma T-\sqrt{t}z\_{t})/\sqrt{T-t}\\ \end{array}\right. |  | (42) |

The expected discounted payoff is the sum of three integrals I1+I2+I3subscript𝐼1subscript𝐼2subscript𝐼3I\_{1}+I\_{2}+I\_{3}, corresponding to the three events
bu​(ST,T)=0superscript𝑏𝑢subscript𝑆𝑇𝑇0b^{u}(S\_{T},T)=0, 0<bu​(ST,T)<10superscript𝑏𝑢subscript𝑆𝑇𝑇10<b^{u}(S\_{T},T)<1, and bu​(ST,T)=1superscript𝑏𝑢subscript𝑆𝑇𝑇1b^{u}(S\_{T},T)=1. Each integral constitutes a separate solution of the Black-Scholes equation. To further simplify the notation, we define A:=−zt​t/(T−t)assign𝐴subscript𝑧𝑡𝑡𝑇𝑡A:=-z\_{t}\sqrt{t/(T-t)} and B:=A+σ​T/T−tassign𝐵𝐴𝜎𝑇𝑇𝑡B:=A+\sigma T/\sqrt{T-t}. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I1:=12​π​∫−∞Aexp⁡(r​t−y2/2)​𝑑y=er​t​N​(A),assignsubscript𝐼112𝜋superscriptsubscript𝐴𝑟𝑡superscript𝑦22differential-d𝑦superscript𝑒𝑟𝑡𝑁𝐴I\_{1}:=\frac{1}{\sqrt{2\pi}}\int\limits\_{-\infty}^{A}\exp(rt-y^{2}/2)dy=e^{rt}N(A), |  | (43) |

where N​(⋅)𝑁⋅N(\cdot) is the cumulative normal distribution function. Next, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | I2:=exp⁡{r​t+t​zt2/(2​T)}2​π​∫ABexp⁡(−t2​T​y2+t​(T−t)T​zt​y)​𝑑y.assignsubscript𝐼2𝑟𝑡𝑡superscriptsubscript𝑧𝑡22𝑇2𝜋superscriptsubscript𝐴𝐵𝑡2𝑇superscript𝑦2𝑡𝑇𝑡𝑇subscript𝑧𝑡𝑦differential-d𝑦I\_{2}:=\frac{\exp\{rt+tz\_{t}^{2}/(2T)\}}{\sqrt{2\pi}}\int\limits\_{A}^{B}\exp\bigg{(}-\frac{t}{2T}y^{2}+\frac{\sqrt{t(T-t)}}{T}z\_{t}y\bigg{)}dy. |  | (44) |

Evaluating the integral and simplifying, one has

|  |  |  |  |
| --- | --- | --- | --- |
|  | I2=Tt​exp⁡(r​t+zt2/2)​[N​(A​Tt+σ​t​TT−t)−N​(A​Tt)].subscript𝐼2𝑇𝑡𝑟𝑡superscriptsubscript𝑧𝑡22delimited-[]𝑁𝐴𝑇𝑡𝜎𝑡𝑇𝑇𝑡𝑁𝐴𝑇𝑡I\_{2}=\sqrt{\frac{T}{t}}\exp(rt+z\_{t}^{2}/2)\bigg{[}N\bigg{(}A\sqrt{\frac{T}{t}}+\sigma\sqrt{\frac{tT}{T-t}}\bigg{)}-N\bigg{(}A\sqrt{\frac{T}{t}}\bigg{)}\bigg{]}. |  | (45) |

Finally, we calculate

|  |  |  |  |
| --- | --- | --- | --- |
|  | I3:=e−r​(T−t)​StS0⋅exp⁡{(r−σ2/2)​(T−t)}2​π​∫B∞exp⁡(−y2/2+σ​T−t⋅y)​𝑑y,assignsubscript𝐼3⋅superscript𝑒𝑟𝑇𝑡subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑇𝑡2𝜋superscriptsubscript𝐵superscript𝑦22⋅𝜎𝑇𝑡𝑦differential-d𝑦I\_{3}:=e^{-r(T-t)}\frac{S\_{t}}{S\_{0}}\cdot\frac{\exp\{(r-\sigma^{2}/2)(T-t)\}}{\sqrt{2\pi}}\int\limits\_{B}^{\infty}\exp\big{(}-y^{2}/2+\sigma\sqrt{T-t}\cdot y\big{)}dy, |  | (46) |

which simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | I3=StS0​N​(σ​T−t−B).subscript𝐼3subscript𝑆𝑡subscript𝑆0𝑁𝜎𝑇𝑡𝐵I\_{3}=\frac{S\_{t}}{S\_{0}}N(\sigma\sqrt{T-t}-B). |  | (47) |

###### Theorem 4.

For the single-stock Black-Scholes market with unlevered hindsight optimization, the price Cu​(S,t)superscript𝐶𝑢𝑆𝑡C^{u}(S,t) of Cover’s Derivative is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cu​(S,t)=er​t​N​(A)+C​(S,t)​[N​(A​Tt+σ​t​TT−t)−N​(A​Tt)]+StS0​N​(σ​T−t−B),superscript𝐶𝑢𝑆𝑡superscript𝑒𝑟𝑡𝑁𝐴𝐶𝑆𝑡delimited-[]𝑁𝐴𝑇𝑡𝜎𝑡𝑇𝑇𝑡𝑁𝐴𝑇𝑡subscript𝑆𝑡subscript𝑆0𝑁𝜎𝑇𝑡𝐵C^{u}(S,t)=e^{rt}N(A)+C(S,t)\bigg{[}N\bigg{(}A\sqrt{\frac{T}{t}}+\sigma\sqrt{\frac{tT}{T-t}}\bigg{)}-N\bigg{(}A\sqrt{\frac{T}{t}}\bigg{)}\bigg{]}\\ +\frac{S\_{t}}{S\_{0}}N(\sigma\sqrt{T-t}-B),\\ |  | (48) |

where z:={log⁡(St/S0)−(r−σ2/2)​t}/(σ​t)assign𝑧subscript𝑆𝑡subscript𝑆0𝑟superscript𝜎22𝑡𝜎𝑡z:=\{\log(S\_{t}/S\_{0})-(r-\sigma^{2}/2)t\}/(\sigma\sqrt{t}), A:=−z​t/(T−t)assign𝐴𝑧𝑡𝑇𝑡A:=-z\sqrt{t/(T-t)}, B:=A+σ​T/T−tassign𝐵𝐴𝜎𝑇𝑇𝑡B:=A+\sigma T/\sqrt{T-t}, and C​(S,t):=T/t⋅exp⁡(r​t+z2/2)assign𝐶𝑆𝑡⋅𝑇𝑡𝑟𝑡superscript𝑧22C(S,t):=\sqrt{T/t}\cdot\exp(rt+z^{2}/2) is the price of Cover’s Derivative under levered hindsight optimization.

### 2.5 Binomial Lattice Price

For the sake of completeness, we proceed to derive the general price of Cover’s Derivative on the Cox-Ross-Rubinstein (1979) binomial lattice. By abuse of notation, let r𝑟r denote the per-period interest rate, with R:=1+rassign𝑅1𝑟R:=1+r being the gross rate of interest. We subdivide the interval [0,T]0𝑇[0,T] into N𝑁N subintervals of length Δ​t:=T/NassignΔ𝑡𝑇𝑁\Delta t:=T/N. The stock price S​(t)𝑆𝑡S(t) evolves according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(t+Δ​t)={S​(t)⋅uwith probability ​pS​(t)⋅dwith probability ​1−p𝑆𝑡Δ𝑡cases⋅𝑆𝑡𝑢with probability 𝑝⋅𝑆𝑡𝑑with probability 1𝑝S(t+\Delta t)=\begin{cases}S(t)\cdot u&\text{with probability }p\\ S(t)\cdot d&\text{with probability }1-p\\ \end{cases} |  | (49) |

where u,d

𝑢𝑑u,d are constants such that 0<d<R<u0𝑑𝑅𝑢0<d<R<u. We let q:=(R−d)/(u−d)assign𝑞𝑅𝑑𝑢𝑑q:=(R-d)/(u-d) be the risk-neutral probability, with 1−q=(u−R)/(u−d)1𝑞𝑢𝑅𝑢𝑑1-q=(u-R)/(u-d). The payoff-relevant state is the number of ups j𝑗j, where 0≤j≤N0𝑗𝑁0\leq j\leq N. After N𝑁N plays, the (possibly levered) rebalancing rule b𝑏b has grown the initial dollar into

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT​(b):=RN​[1+b​(u/R−1)]j​[1+b​(d/R−1)]N−j.assignsubscript𝑉𝑇𝑏superscript𝑅𝑁superscriptdelimited-[]1𝑏𝑢𝑅1𝑗superscriptdelimited-[]1𝑏𝑑𝑅1𝑁𝑗V\_{T}(b):=R^{N}[1+b(u/R-1)]^{j}[1+b(d/R-1)]^{N-j}. |  | (50) |

To get the best rebalancing rule in hindsight over [0,T]0𝑇[0,T], we take logs and differentiate with respect to b𝑏b, yielding the first-order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | j​(u−R)​[1+b​(d/R−1)]+(N−j)​(d−R)​[1+b​(u/R−1)]=0.𝑗𝑢𝑅delimited-[]1𝑏𝑑𝑅1𝑁𝑗𝑑𝑅delimited-[]1𝑏𝑢𝑅10j(u-R)[1+b(d/R-1)]+(N-j)(d-R)[1+b(u/R-1)]=0. |  | (51) |

Solving and simplifying, the best rebalancing rule in hindsight (after j𝑗j ups and N−j𝑁𝑗N-j downs) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(j,N):=RN​(u−d)​(jq−N−j1−q)assign𝑏𝑗𝑁𝑅𝑁𝑢𝑑𝑗𝑞𝑁𝑗1𝑞b(j,N):=\frac{R}{N(u-d)}\bigg{(}\frac{j}{q}-\frac{N-j}{1-q}\bigg{)} |  | (52) |

The final payoff of Cover’s Derivative is

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT∗​(j,N):=(RN)N​(jq)j​(N−j1−q)N−j,assignsuperscriptsubscript𝑉𝑇𝑗𝑁superscript𝑅𝑁𝑁superscript𝑗𝑞𝑗superscript𝑁𝑗1𝑞𝑁𝑗V\_{T}^{\*}(j,N):=\bigg{(}\frac{R}{N}\bigg{)}^{N}\bigg{(}\frac{j}{q}\bigg{)}^{j}\bigg{(}\frac{N-j}{1-q}\bigg{)}^{N-j}, |  | (53) |

where we have adopted the convention that 00:=1assignsuperscript0010^{0}:=1. If the hindsight-optimization is restricted to unlevered rebalancing rules b∈[0,1],𝑏01b\in[0,1], then the payoff becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | VT∗:={RNif ​j≤N​q(RN)N​(jq)j​(N−j1−q)N−jif ​N​q<j<N​q+u−dR​q​(1−q).uj​dN−jif ​j≥N​q+u−dR​q​(1−q)assignsuperscriptsubscript𝑉𝑇casessuperscript𝑅𝑁if 𝑗𝑁𝑞superscript𝑅𝑁𝑁superscript𝑗𝑞𝑗superscript𝑁𝑗1𝑞𝑁𝑗if 𝑁𝑞𝑗𝑁𝑞𝑢𝑑𝑅𝑞1𝑞superscript𝑢𝑗superscript𝑑𝑁𝑗if 𝑗𝑁𝑞𝑢𝑑𝑅𝑞1𝑞\displaystyle V\_{T}^{\*}:=\left\{\begin{array}[]{cc}R^{N}&\hskip 14.22636pt\text{if }j\leq Nq\\ (\frac{R}{N})^{N}\big{(}\frac{j}{q}\big{)}^{j}\big{(}\frac{N-j}{1-q}\big{)}^{N-j}&\hskip 14.22636pt\text{if }Nq<j<Nq+\frac{u-d}{Rq(1-q)}.\\ u^{j}d^{N-j}&\text{if }j\geq Nq+\frac{u-d}{Rq(1-q)}\\ \end{array}\right. |  | (57) |

For unlevered hindsight optimization, Ordentlich and Cover (1998) gave us the time-0 price

|  |  |  |  |
| --- | --- | --- | --- |
|  | C0=Prob​{j≤N​q}+∑N​q<j<N​q+u−dR​q​(1−q)(Nj)​(jN)j​(1−jN)N−j+∑j≥N​q+u−dR​q​(1−q)(Nj)​(q​u)j​[(1−q)​d]N−j.subscript𝐶0Prob𝑗𝑁𝑞subscript𝑁𝑞𝑗𝑁𝑞𝑢𝑑𝑅𝑞1𝑞binomial𝑁𝑗superscript𝑗𝑁𝑗superscript1𝑗𝑁𝑁𝑗subscript𝑗𝑁𝑞𝑢𝑑𝑅𝑞1𝑞binomial𝑁𝑗superscript𝑞𝑢𝑗superscriptdelimited-[]1𝑞𝑑𝑁𝑗C\_{0}=\text{Prob}\{j\leq Nq\}+\sum\limits\_{Nq<j<Nq+\frac{u-d}{Rq(1-q)}}\binom{N}{j}\bigg{(}\frac{j}{N}\bigg{)}^{j}\bigg{(}1-\frac{j}{N}\bigg{)}^{N-j}\\ +\sum\limits\_{j\geq Nq+\frac{u-d}{Rq(1-q)}}\binom{N}{j}(qu)^{j}[(1-q)d]^{N-j}.\\ |  | (58) |

We supplement this formula by computing the general price under levered hindsight optimization in state (k,n)𝑘𝑛(k,n), where k𝑘k upticks have occured in the first n𝑛n time steps. Letting j𝑗j denote the number of upticks in the next N−n𝑁𝑛N-n steps, the expected discounted payoff in state (k,n)𝑘𝑛(k,n) with respect to the risk-neutral measure is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(k,n):=q−k​(1−q)k−n​∑j=0N−n(N−nj)​(j+kN)j+k​(1−j+kN)N−j−k.assign𝐶𝑘𝑛superscript𝑞𝑘superscript1𝑞𝑘𝑛superscriptsubscript𝑗0𝑁𝑛binomial𝑁𝑛𝑗superscript𝑗𝑘𝑁𝑗𝑘superscript1𝑗𝑘𝑁𝑁𝑗𝑘C(k,n):=q^{-k}(1-q)^{k-n}\sum\limits\_{j=0}^{N-n}\binom{N-n}{j}\bigg{(}\frac{j+k}{N}\bigg{)}^{j+k}\bigg{(}1-\frac{j+k}{N}\bigg{)}^{N-j-k}. |  | (59) |

This being done, one can replicate Cover’s Derivative on the binomial lattice by using our general price C​(k,n)𝐶𝑘𝑛C(k,n) in conjunction with the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ:=Cu−CdS​(u−d)=C​(k+1,n+1)−C​(k,n+1)S​(u−d),assignΔsubscript𝐶𝑢subscript𝐶𝑑𝑆𝑢𝑑𝐶𝑘1𝑛1𝐶𝑘𝑛1𝑆𝑢𝑑\Delta:=\frac{C\_{u}-C\_{d}}{S(u-d)}=\frac{C(k+1,n+1)-C(k,n+1)}{S(u-d)}, |  | (60) |

where S𝑆S is the current stock price, n𝑛n is the number of time steps to date, and k𝑘k is the number of upticks that have occured so far.

To obtain a more direct generalization of ([58](#S2.E58 "In 2.5 Binomial Lattice Price ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.")), we close this subsection by computing the price of Cover’s Derivative for unlevered hindsight optimization in all possible states (k,n).𝑘𝑛(k,n). The price consists of three terms Cu​(k,n):=Σ1+Σ2+Σ3assignsuperscript𝐶𝑢𝑘𝑛subscriptΣ1subscriptΣ2subscriptΣ3C^{u}(k,n):=\Sigma\_{1}+\Sigma\_{2}+\Sigma\_{3}, corresponding to the three events b∗≤0superscript𝑏0b^{\*}\leq 0, 0<b∗<10superscript𝑏10<b^{\*}<1, and b∗≥1.superscript𝑏1b^{\*}\geq 1. Again, j𝑗j will denote the number of upticks that occur over the next N−n𝑁𝑛N-n time steps. We start with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ1:=∑0≤j≤N​q−k(N−nj)​qj​(1−q)N−n−j.assignsubscriptΣ1subscript0𝑗𝑁𝑞𝑘binomial𝑁𝑛𝑗superscript𝑞𝑗superscript1𝑞𝑁𝑛𝑗\Sigma\_{1}:=\sum\limits\_{0\leq j\leq Nq-k}\binom{N-n}{j}q^{j}(1-q)^{N-n-j}. |  | (61) |

Next, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ2:=q−k​(1−q)k−n​∑N​q−k<j<N​q−k+u−dR​q​(1−q)(N−nj)​(j+kN)j+k​(1−j+kN)N−j−k.assignsubscriptΣ2superscript𝑞𝑘superscript1𝑞𝑘𝑛subscript𝑁𝑞𝑘𝑗𝑁𝑞𝑘𝑢𝑑𝑅𝑞1𝑞binomial𝑁𝑛𝑗superscript𝑗𝑘𝑁𝑗𝑘superscript1𝑗𝑘𝑁𝑁𝑗𝑘\Sigma\_{2}:=q^{-k}(1-q)^{k-n}\sum\limits\_{Nq-k<j<Nq-k+\frac{u-d}{Rq(1-q)}}\binom{N-n}{j}\bigg{(}\frac{j+k}{N}\bigg{)}^{j+k}\bigg{(}1-\frac{j+k}{N}\bigg{)}^{N-j-k}. |  | (62) |

Finally, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ3:=q−k​(1−q)k−n​∑j≥N​q−k+u−dR​q​(1−q)(N−nj)​(q​u)k+j​[(1−q)​d]N−k−j.assignsubscriptΣ3superscript𝑞𝑘superscript1𝑞𝑘𝑛subscript𝑗𝑁𝑞𝑘𝑢𝑑𝑅𝑞1𝑞binomial𝑁𝑛𝑗superscript𝑞𝑢𝑘𝑗superscriptdelimited-[]1𝑞𝑑𝑁𝑘𝑗\Sigma\_{3}:=q^{-k}(1-q)^{k-n}\sum\limits\_{j\geq Nq-k+\frac{u-d}{Rq(1-q)}}\binom{N-n}{j}(qu)^{k+j}[(1-q)d]^{N-k-j}. |  | (63) |

#### Simulation: “Shannon’s Demon”

To illustrate the replication of Cover’s Derivative on a binomial lattice, we simulate Shannon’s canonical discrete-time example (cf. Poundstone 2010). This amounts to the parameters u:=2assign𝑢2u:=2, d:=1/2assign𝑑12d:=1/2, r:=0assign𝑟0r:=0, R=1𝑅1R=1, and the risk-neutral probability q=1/3𝑞13q=1/3. The gambler buys (replicates) a dollar’s worth of Cover’s Derivative at n=0𝑛0n=0, and holds the option until n=N𝑛𝑁n=N. His wealth after n𝑛n steps (and k𝑘k upticks) is C​(k,n)/C​(0,0)𝐶𝑘𝑛𝐶00C(k,n)/C(0,0). By comparison, the stock price will be 22​k−n.superscript22𝑘𝑛2^{2k-n}. Figure [7](#S2.F7 "Figure 7 ‣ Simulation: “Shannon’s Demon” ‣ 2.5 Binomial Lattice Price ‣ 2 One Underlying ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") plots a sample path for N:=300assign𝑁300N:=300 periods.

![Refer to caption](/html/1810.02485/assets/discreteDemon.png)


Figure 7: Replication of Cover’s Derivative on the binomial lattice for Shannon’s canonical example (“Shannon’s Demon”).

## 3 Several Underlyings

We turn our attention to the general stock market with n𝑛n correlated stocks (i=1,…,n)𝑖

1…𝑛(i=1,...,n) that follow the geometric Brownian motions

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Si​tSi​t=μi​d​t+σi​d​Wi​t,𝑑subscript𝑆𝑖𝑡subscript𝑆𝑖𝑡subscript𝜇𝑖𝑑𝑡subscript𝜎𝑖𝑑subscript𝑊𝑖𝑡\frac{dS\_{it}}{S\_{it}}=\mu\_{i}\,dt+\sigma\_{i}\,dW\_{it}, |  | (64) |

where Si​tsubscript𝑆𝑖𝑡S\_{it} is the price of stock i𝑖i at t𝑡t and μi,σi

subscript𝜇𝑖subscript𝜎𝑖\mu\_{i},\sigma\_{i} are the drift and volatility of stock i𝑖i, respectively. The (Wi​t)i=1nsuperscriptsubscriptsubscript𝑊𝑖𝑡𝑖1𝑛(W\_{it})\_{i=1}^{n} are standard Brownian motions, with ρi​j:=Corr​(d​Wi​t,d​Wj​t)assignsubscript𝜌𝑖𝑗Corr𝑑subscript𝑊𝑖𝑡𝑑subscript𝑊𝑗𝑡\rho\_{ij}:=\text{Corr}(dW\_{it},dW\_{jt}) being the correlation coefficient of the instantaneous changes in Wi​tsubscript𝑊𝑖𝑡W\_{it} and Wj​tsubscript𝑊𝑗𝑡W\_{jt}. The correlation matrix, which is assumed to be invertible, is denoted R:=[ρi​j]n×nassign𝑅subscriptdelimited-[]subscript𝜌𝑖𝑗𝑛𝑛R:=[\rho\_{ij}]\_{n\times n}.
Next, we let

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​j:=ρi​j​σi​σj=Cov​(d​Si​tSi​t,d​Sj​tSj​t)/d​t.assignsubscript𝜎𝑖𝑗subscript𝜌𝑖𝑗subscript𝜎𝑖subscript𝜎𝑗Cov𝑑subscript𝑆𝑖𝑡subscript𝑆𝑖𝑡𝑑subscript𝑆𝑗𝑡subscript𝑆𝑗𝑡𝑑𝑡\sigma\_{ij}:=\rho\_{ij}\sigma\_{i}\sigma\_{j}=\text{Cov}\bigg{(}\frac{dS\_{it}}{S\_{it}},\frac{dS\_{jt}}{S\_{jt}}\bigg{)}\big{/}dt. |  | (65) |

We let Σ:=[σi​j]n×nassignΣsubscriptdelimited-[]subscript𝜎𝑖𝑗𝑛𝑛\Sigma:=[\sigma\_{ij}]\_{n\times n} denote the covariance matrix of instantaneous returns per unit time, and we write Σ=M​R​MΣ𝑀𝑅𝑀\Sigma=MRM, where M:=diag​(σ1,…,σn)assign𝑀diagsubscript𝜎1…subscript𝜎𝑛M:=\text{diag}(\sigma\_{1},...,\sigma\_{n}) is the diagonal matrix of volatilities.

We take up the general rebalancing rules b:=(b1,…,bn)′∈ℝn,assign𝑏superscriptsubscript𝑏1…subscript𝑏𝑛′superscriptℝ𝑛b:=(b\_{1},...,b\_{n})^{\prime}\in\mathbb{R}^{n}, where bisubscript𝑏𝑖b\_{i} is the fraction of wealth bet on stock i𝑖i over the interval [t,t+d​t].𝑡𝑡𝑑𝑡[t,t+dt]. Thus, the trader keeps the fraction 1−∑i=1nbi1superscriptsubscript𝑖1𝑛subscript𝑏𝑖1-\sum\limits\_{i=1}^{n}b\_{i} of his wealth in bonds over the interval [t,t+d​t].𝑡𝑡𝑑𝑡[t,t+dt]. As before, we let Vt​(b)subscript𝑉𝑡𝑏V\_{t}(b) denote the gambler’s wealth at t𝑡t, where V0:=1.assignsubscript𝑉01V\_{0}:=1. The trader’s wealth evolves according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt​(b)Vt​(b)=∑i=1nbi​d​Si​tSi​t+(1−∑i=1nbi)​d​BtBt=[∑i=1nbi​μi+(1−∑i=1nbi)​r]​d​t+∑i=1nbi​σi​d​Wi​t.𝑑subscript𝑉𝑡𝑏subscript𝑉𝑡𝑏superscriptsubscript𝑖1𝑛subscript𝑏𝑖𝑑subscript𝑆𝑖𝑡subscript𝑆𝑖𝑡1superscriptsubscript𝑖1𝑛subscript𝑏𝑖𝑑subscript𝐵𝑡subscript𝐵𝑡delimited-[]superscriptsubscript𝑖1𝑛subscript𝑏𝑖subscript𝜇𝑖1superscriptsubscript𝑖1𝑛subscript𝑏𝑖𝑟𝑑𝑡superscriptsubscript𝑖1𝑛subscript𝑏𝑖subscript𝜎𝑖𝑑subscript𝑊𝑖𝑡\frac{dV\_{t}(b)}{V\_{t}(b)}=\sum\limits\_{i=1}^{n}b\_{i}\frac{dS\_{it}}{S\_{it}}+\bigg{(}1-\sum\limits\_{i=1}^{n}b\_{i}\bigg{)}\frac{dB\_{t}}{B\_{t}}\\ =\bigg{[}\sum\limits\_{i=1}^{n}b\_{i}\mu\_{i}+\bigg{(}1-\sum\limits\_{i=1}^{n}b\_{i}\bigg{)}r\bigg{]}dt+\sum\limits\_{i=1}^{n}b\_{i}\sigma\_{i}dW\_{it}.\\ |  | (66) |

For brevity, let μ:=(μ1,…,μn)′assign𝜇superscriptsubscript𝜇1…subscript𝜇𝑛′\mu:=(\mu\_{1},...,\mu\_{n})^{\prime} denote the vector of drifts. We then have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt​(b)Vt​(b)=[r+(μ−r​1)′​b]​d​t+∑i=1nbi​σi​d​Wi​t,𝑑subscript𝑉𝑡𝑏subscript𝑉𝑡𝑏delimited-[]𝑟superscript𝜇𝑟1′𝑏𝑑𝑡superscriptsubscript𝑖1𝑛subscript𝑏𝑖subscript𝜎𝑖𝑑subscript𝑊𝑖𝑡\frac{dV\_{t}(b)}{V\_{t}(b)}=[r+(\mu-r\textbf{1})^{\prime}b]dt+\sum\_{i=1}^{n}b\_{i}\sigma\_{i}dW\_{it}, |  | (67) |

where 1:=(1,…,1)′assign1superscript1…1′\textbf{1}:=(1,...,1)^{\prime} is an n×1𝑛1n\times 1 vector of ones. The solution of this stochastic differential equation is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(b)=exp⁡{[r+(μ−r​1)′​b−b′​Σ​b/2]​t+∑i=1nbi​σi​Wi​t}.subscript𝑉𝑡𝑏delimited-[]𝑟superscript𝜇𝑟1′𝑏superscript𝑏′Σ𝑏2𝑡superscriptsubscript𝑖1𝑛subscript𝑏𝑖subscript𝜎𝑖subscript𝑊𝑖𝑡V\_{t}(b)=\exp\bigg{\{}[r+(\mu-r\textbf{1})^{\prime}b-b^{\prime}\Sigma b/2]t+\sum\limits\_{i=1}^{n}b\_{i}\sigma\_{i}W\_{it}\bigg{\}}. |  | (68) |

This can be verified directly by applying the multivariate version of Itô’s Lemma (Björk 1998) to the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(W1,…,Wn,t):=exp⁡{[r+(μ−r​1)′​b−b′​Σ​b/2]​t+∑i=1nbi​σi​Wi}.assign𝐹subscript𝑊1…subscript𝑊𝑛𝑡delimited-[]𝑟superscript𝜇𝑟1′𝑏superscript𝑏′Σ𝑏2𝑡superscriptsubscript𝑖1𝑛subscript𝑏𝑖subscript𝜎𝑖subscript𝑊𝑖F(W\_{1},...,W\_{n},t):=\exp\bigg{\{}[r+(\mu-r\textbf{1})^{\prime}b-b^{\prime}\Sigma b/2]t+\sum\limits\_{i=1}^{n}b\_{i}\sigma\_{i}W\_{i}\bigg{\}}. |  | (69) |

Indeed, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ft=∂F∂t​d​t+∑i=1n∂F∂Wi​d​Wi​t+12​∑i=1n∑j=1n∂2F∂Wi​∂Wj​ρi​j​d​t.𝑑subscript𝐹𝑡𝐹𝑡𝑑𝑡superscriptsubscript𝑖1𝑛𝐹subscript𝑊𝑖𝑑subscript𝑊𝑖𝑡12superscriptsubscript𝑖1𝑛superscriptsubscript𝑗1𝑛superscript2𝐹subscript𝑊𝑖subscript𝑊𝑗subscript𝜌𝑖𝑗𝑑𝑡dF\_{t}=\frac{\partial{F}}{\partial{t}}dt+\sum\_{i=1}^{n}\frac{\partial{F}}{\partial{W\_{i}}}dW\_{it}+\frac{1}{2}\sum\_{i=1}^{n}\sum\_{j=1}^{n}\frac{\partial^{2}F}{\partial W\_{i}\partial W\_{j}}\rho\_{ij}dt. |  | (70) |

Substituting ∂F/∂t=F⋅[r+(μ−r​1)′​b−b′​Σ​b/2]𝐹𝑡⋅𝐹delimited-[]𝑟superscript𝜇𝑟1′𝑏superscript𝑏′Σ𝑏2\partial F/\partial t=F\cdot[r+(\mu-r\textbf{1})^{\prime}b-b^{\prime}\Sigma b/2], ∂F/∂Wi=F⋅bi​σi,𝐹subscript𝑊𝑖⋅𝐹subscript𝑏𝑖subscript𝜎𝑖\partial F/\partial W\_{i}=F\cdot b\_{i}\sigma\_{i}, and ∂2F/∂Wi​∂Wj=F⋅bi​bj​σi​σjsuperscript2𝐹subscript𝑊𝑖subscript𝑊𝑗⋅𝐹subscript𝑏𝑖subscript𝑏𝑗subscript𝜎𝑖subscript𝜎𝑗\partial^{2}F/\partial W\_{i}\partial W\_{j}=F\cdot b\_{i}b\_{j}\sigma\_{i}\sigma\_{j} yields the desired result. Proceeding as before, we take the expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​Wi​t=log⁡(Si​t/Si​0)−(μi−σi2/2)​tsubscript𝜎𝑖subscript𝑊𝑖𝑡subscript𝑆𝑖𝑡subscript𝑆𝑖0subscript𝜇𝑖superscriptsubscript𝜎𝑖22𝑡\sigma\_{i}W\_{it}=\log(S\_{it}/S\_{i0})-(\mu\_{i}-\sigma\_{i}^{2}/2)t |  | (71) |

and substitute it into ([68](#S3.E68 "In 3 Several Underlyings ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.")). This yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(b)=exp⁡{(r−b′​Σ​b/2)​t+∑i=1nbi​[log⁡(Si​t/Si​0)−(r−σi2/2)​t]}.subscript𝑉𝑡𝑏𝑟superscript𝑏′Σ𝑏2𝑡superscriptsubscript𝑖1𝑛subscript𝑏𝑖delimited-[]subscript𝑆𝑖𝑡subscript𝑆𝑖0𝑟superscriptsubscript𝜎𝑖22𝑡V\_{t}(b)=\exp\bigg{\{}(r-b^{\prime}\Sigma b/2)t+\sum\_{i=1}^{n}b\_{i}[\log(S\_{it}/S\_{i0})-(r-\sigma\_{i}^{2}/2)t]\bigg{\}}. |  | (72) |

For brevity, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi:=log⁡(Si​t/Si​0)−(r−σi2/2)​tσi​t.assignsubscript𝑧𝑖subscript𝑆𝑖𝑡subscript𝑆𝑖0𝑟superscriptsubscript𝜎𝑖22𝑡subscript𝜎𝑖𝑡\boxed{z\_{i}:=\frac{\log(S\_{it}/S\_{i0})-(r-\sigma\_{i}^{2}/2)t}{\sigma\_{i}\sqrt{t}}}. |  | (73) |

Under the equivalent martingale measure, the variables z:=(z1,…,zn)′assign𝑧superscriptsubscript𝑧1…subscript𝑧𝑛′z:=(z\_{1},...,z\_{n})^{\prime} are all unit normals, with correlation matrix R=[ρi​j]𝑅delimited-[]subscript𝜌𝑖𝑗R=[\rho\_{ij}]. Thus, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(b)=exp⁡{(r−b′​Σ​b/2)​t+t⋅z′​M​b}.subscript𝑉𝑡𝑏𝑟superscript𝑏′Σ𝑏2𝑡⋅𝑡superscript𝑧′𝑀𝑏V\_{t}(b)=\exp\{(r-b^{\prime}\Sigma b/2)t+\sqrt{t}\cdot z^{\prime}Mb\}. |  | (74) |

Maximizing Vt​(b)subscript𝑉𝑡𝑏V\_{t}(b) with respect to b𝑏b, we get the first-order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | t​Σ​b=t​M​z.𝑡Σ𝑏𝑡𝑀𝑧t\Sigma b=\sqrt{t}Mz. |  | (75) |

For simplicity, let S:=(S1,…,Sn)′assign𝑆superscriptsubscript𝑆1…subscript𝑆𝑛′S:=(S\_{1},...,S\_{n})^{\prime} denote the vector of stock prices, and let b​(S,t)𝑏𝑆𝑡b(S,t) denote the best rebalancing rule in hindsight over [0,t]0𝑡[0,t]. Solving the first-order condition yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(S,t)=1t⋅M−1​R−1​z.𝑏𝑆𝑡⋅1𝑡superscript𝑀1superscript𝑅1𝑧\boxed{b(S,t)=\frac{1}{\sqrt{t}}\cdot M^{-1}R^{-1}z}. |  | (76) |

The final wealth that accrues to a $1currency-dollar1\$1 deposit into the best rebalancing rule in hindsight over [0,t]0𝑡[0,t] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∗=exp⁡(r​t+z′​R−1​z/2)=exp⁡(r​t+t⋅b′​Σ​b/2).superscriptsubscript𝑉𝑡𝑟𝑡superscript𝑧′superscript𝑅1𝑧2𝑟𝑡⋅𝑡superscript𝑏′Σ𝑏2\boxed{V\_{t}^{\*}=\exp(rt+z^{\prime}R^{-1}z/2)=\exp(rt+t\cdot b^{\prime}\Sigma b/2)}. |  | (77) |

Hence, the final payoff of Cover’s Derivative is VT∗=exp⁡(r​T+z′​R−1​z/2)superscriptsubscript𝑉𝑇𝑟𝑇superscript𝑧′superscript𝑅1𝑧2V\_{T}^{\*}=\exp(rT+z^{\prime}R^{-1}z/2). Again, we see that the final wealth of the best (levered) rebalancing rule in hindsight is Markovian: it depends only on the current state (S1,…,Sn,t)subscript𝑆1…subscript𝑆𝑛𝑡(S\_{1},...,S\_{n},t).

We pass to the multivariate version of the Black-Scholes equation (Wilmott 2001), which governs the no-arbitrage price of “rainbow” or “correlation” options dependent on several underlyings. As usual C​(S1,…,Sn,t)=C​(S,t)𝐶subscript𝑆1…subscript𝑆𝑛𝑡𝐶𝑆𝑡C(S\_{1},...,S\_{n},t)=C(S,t) will denote the price of Cover’s Derivative. We solve the differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​∑i=1n∑j=1nρi​j​σi​σj​Si​Sj​∂2C∂Si​∂Sj+r​∑i=1nSi​∂C∂Si+∂C∂t−r​C=012superscriptsubscript𝑖1𝑛superscriptsubscript𝑗1𝑛subscript𝜌𝑖𝑗subscript𝜎𝑖subscript𝜎𝑗subscript𝑆𝑖subscript𝑆𝑗superscript2𝐶subscript𝑆𝑖subscript𝑆𝑗𝑟superscriptsubscript𝑖1𝑛subscript𝑆𝑖𝐶subscript𝑆𝑖𝐶𝑡𝑟𝐶0\frac{1}{2}\sum\_{i=1}^{n}\sum\_{j=1}^{n}\rho\_{ij}\sigma\_{i}\sigma\_{j}S\_{i}S\_{j}\frac{\partial^{2}C}{\partial S\_{i}\partial S\_{j}}+r\sum\limits\_{i=1}^{n}S\_{i}\frac{\partial C}{\partial S\_{i}}+\frac{\partial C}{\partial t}-rC=0 |  | (78) |

with the boundary condition C​(S,T):=VT∗​(S)=exp⁡(r​T+zT′​R−1​zT/2)assign𝐶𝑆𝑇superscriptsubscript𝑉𝑇𝑆𝑟𝑇superscriptsubscript𝑧𝑇′superscript𝑅1subscript𝑧𝑇2C(S,T):=V\_{T}^{\*}(S)=\exp(rT+z\_{T}^{\prime}R^{-1}z\_{T}/2). As usual, we do this by computing the expected discounted payoff with respect to the equivalent martingale measure.

To this end, we again write

|  |  |  |  |
| --- | --- | --- | --- |
|  | zT=t/T⋅zt+1−t/T⋅y,subscript𝑧𝑇⋅𝑡𝑇subscript𝑧𝑡⋅1𝑡𝑇𝑦z\_{T}=\sqrt{t/T}\cdot z\_{t}+\sqrt{1-t/T}\cdot y, |  | (79) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi:=log⁡(Si​T/Si​t)−(r−σi2/2)​(T−t)σi​T−t.assignsubscript𝑦𝑖subscript𝑆𝑖𝑇subscript𝑆𝑖𝑡𝑟superscriptsubscript𝜎𝑖22𝑇𝑡subscript𝜎𝑖𝑇𝑡y\_{i}:=\frac{\log(S\_{iT}/S\_{it})-(r-\sigma\_{i}^{2}/2)(T-t)}{\sigma\_{i}\sqrt{T-t}}. |  | (80) |

The yisubscript𝑦𝑖y\_{i} are all unit normals with respect to the equivalent martingale measure ℚℚ\mathbb{Q} and the information available at t𝑡t. R𝑅R is the correlation matrix of the random vector y:=(y1,…,yn)′assign𝑦superscriptsubscript𝑦1…subscript𝑦𝑛′y:=(y\_{1},...,y\_{n})^{\prime}. The conditional density of y𝑦y is
f​(y):=(2​π)−n/2​det(R)−1/2​exp⁡(−y′​R−1​y/2)assign𝑓𝑦superscript2𝜋𝑛2superscript𝑅12superscript𝑦′superscript𝑅1𝑦2f(y):=(2\pi)^{-n/2}\det(R)^{-1/2}\exp(-y^{\prime}R^{-1}y/2). Expanding the quadratic form zT′​R−1​zTsuperscriptsubscript𝑧𝑇′superscript𝑅1subscript𝑧𝑇z\_{T}^{\prime}R^{-1}z\_{T}, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | zT′​R−1​zT/2=t2​T​zt′​R−1​zt+t​(T−t)T​zt′​R−1​y+T−t2​T​y′​R−1​y.superscriptsubscript𝑧𝑇′superscript𝑅1subscript𝑧𝑇2𝑡2𝑇superscriptsubscript𝑧𝑡′superscript𝑅1subscript𝑧𝑡𝑡𝑇𝑡𝑇superscriptsubscript𝑧𝑡′superscript𝑅1𝑦𝑇𝑡2𝑇superscript𝑦′superscript𝑅1𝑦z\_{T}^{\prime}R^{-1}z\_{T}/2=\frac{t}{2T}z\_{t}^{\prime}R^{-1}z\_{t}+\frac{\sqrt{t(T-t)}}{T}z\_{t}^{\prime}R^{-1}y+\frac{T-t}{2T}y^{\prime}R^{-1}y. |  | (81) |

Thus, we find that 𝔼tℚ​[exp⁡(zT′​R−1​zT/2)]=superscriptsubscript𝔼𝑡ℚdelimited-[]superscriptsubscript𝑧𝑇′superscript𝑅1subscript𝑧𝑇2absent\mathbb{E}\_{t}^{\mathbb{Q}}[\exp(z\_{T}^{\prime}R^{-1}z\_{T}/2)]=

|  |  |  |  |
| --- | --- | --- | --- |
|  | (2​π)−n/2​det(R)−1/2​exp⁡(t2​T​zt′​R−1​zt)×∫−∞∞⋯∫−∞∞exp(−t2​Ty′R−1y+t​(T−t)Tzt′R−1y)dy1⋯dyn.superscript2𝜋𝑛2superscript𝑅12𝑡2𝑇superscriptsubscript𝑧𝑡′superscript𝑅1subscript𝑧𝑡superscriptsubscript⋯superscriptsubscript𝑡2𝑇superscript𝑦′superscript𝑅1𝑦𝑡𝑇𝑡𝑇superscriptsubscript𝑧𝑡′superscript𝑅1𝑦𝑑subscript𝑦1⋯𝑑subscript𝑦𝑛(2\pi)^{-n/2}\det(R)^{-1/2}\exp\bigg{(}\frac{t}{2T}z\_{t}^{\prime}R^{-1}z\_{t}\bigg{)}\\ \times\int\limits\_{-\infty}^{\infty}\cdot\cdot\cdot\int\limits\_{-\infty}^{\infty}\exp\bigg{(}-\frac{t}{2T}y^{\prime}R^{-1}y+\frac{\sqrt{t(T-t)}}{T}z\_{t}^{\prime}R^{-1}y\bigg{)}dy\_{1}\cdot\cdot\cdot dy\_{n}.\\ |  | (82) |

To evaluate the multiple integral, we use the general formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫−∞∞⋯​∫−∞∞exp⁡(−y′​A​y+β′​y)​𝑑y1​⋯​𝑑yn=πn/2​det(A)−1/2​exp⁡(β′​A−1​β/4),superscriptsubscript⋯superscriptsubscriptsuperscript𝑦′𝐴𝑦superscript𝛽′𝑦differential-dsubscript𝑦1⋯differential-dsubscript𝑦𝑛superscript𝜋𝑛2superscript𝐴12superscript𝛽′superscript𝐴1𝛽4\int\limits\_{-\infty}^{\infty}\cdot\cdot\cdot\int\limits\_{-\infty}^{\infty}\exp(-y^{\prime}Ay+\beta^{\prime}y)dy\_{1}\cdot\cdot\cdot dy\_{n}=\pi^{n/2}\det(A)^{-1/2}\exp(\beta^{\prime}A^{-1}\beta/4), |  | (83) |

where A𝐴A is any symmetric positive definite n×n𝑛𝑛n\times n matrix and β=(β1,…,βn)′𝛽superscriptsubscript𝛽1…subscript𝛽𝑛′\beta=(\beta\_{1},...,\beta\_{n})^{\prime} is any vector of constants. Putting A:=t/(2​T)⋅R−1assign𝐴⋅𝑡2𝑇superscript𝑅1A:=t/(2T)\cdot R^{-1}, β:=t​(T−t)/T⋅R−1​ztassign𝛽⋅𝑡𝑇𝑡𝑇superscript𝑅1subscript𝑧𝑡\beta:=\sqrt{t(T-t)}\big{/}T\cdot R^{-1}z\_{t}, and simplifying, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼tℚ​[exp⁡(zT′​R−1​zT/2)]=(T/t)n/2​exp⁡(zt′​R−1​zt/2).superscriptsubscript𝔼𝑡ℚdelimited-[]superscriptsubscript𝑧𝑇′superscript𝑅1subscript𝑧𝑇2superscript𝑇𝑡𝑛2superscriptsubscript𝑧𝑡′superscript𝑅1subscript𝑧𝑡2\mathbb{E}\_{t}^{\mathbb{Q}}[\exp(z\_{T}^{\prime}R^{-1}z\_{T}/2)]=(T/t)^{n/2}\exp(z\_{t}^{\prime}R^{-1}z\_{t}/2). |  | (84) |

###### Theorem 5.

For levered hindsight optimization (over all b∈ℝn𝑏superscriptℝ𝑛b\in\mathbb{R}^{n}), the price of Cover’s Derivative is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(S,t)=(T/t)n/2​exp⁡(r​t+z′​R−1​z/2)=(T/t)n/2​exp⁡(r​t+t⋅b′​Σ​b/2)=(T/t)n/2⋅Vt∗,𝐶𝑆𝑡superscript𝑇𝑡𝑛2𝑟𝑡superscript𝑧′superscript𝑅1𝑧2superscript𝑇𝑡𝑛2𝑟𝑡⋅𝑡superscript𝑏′Σ𝑏2⋅superscript𝑇𝑡𝑛2superscriptsubscript𝑉𝑡\boxed{C(S,t)=(T/t)^{n/2}\exp(rt+z^{\prime}R^{-1}z/2)=(T/t)^{n/2}\exp(rt+t\cdot b^{\prime}\Sigma b/2)=(T/t)^{n/2}\cdot V\_{t}^{\*}}, |  | (85) |

where zi:={log⁡(Si​t/Si​0)−(r−σi2/2)​t}/(σi​t)assignsubscript𝑧𝑖subscript𝑆𝑖𝑡subscript𝑆𝑖0𝑟superscriptsubscript𝜎𝑖22𝑡subscript𝜎𝑖𝑡z\_{i}:=\{\log(S\_{it}/S\_{i0})-(r-\sigma\_{i}^{2}/2)t\}/(\sigma\_{i}\sqrt{t}), b​(S,t)𝑏𝑆𝑡b(S,t) is the best rebalancing rule in hindsight over [0,t]0𝑡[0,t], and Vt∗superscriptsubscript𝑉𝑡V\_{t}^{\*} is the intrinsic value at time t𝑡t.

###### Theorem 6.

For the general market with n𝑛n correlated stocks in geometric Brownian motion, the American-style version of Cover’s Derivative (that expires at T𝑇T, has zero exercise price, and pays Vt∗superscriptsubscript𝑉𝑡V\_{t}^{\*} upon exercise at t𝑡t) will never be excercised early in equilibrium. The American price Ca​(S,t)subscript𝐶𝑎𝑆𝑡C\_{a}(S,t) is equal to the European price Ce​(S,t)=(T/t)n/2⋅Vt∗subscript𝐶𝑒𝑆𝑡⋅superscript𝑇𝑡𝑛2superscriptsubscript𝑉𝑡C\_{e}(S,t)=(T/t)^{n/2}\cdot V\_{t}^{\*}.

###### Proof.

Immediately, we see that the option is “worth more alive than dead” on account of the inequalities Ca​(S,t)≥Ce​(S,t)=(T/t)n/2⋅Vt∗>Vt∗subscript𝐶𝑎𝑆𝑡subscript𝐶𝑒𝑆𝑡⋅superscript𝑇𝑡𝑛2superscriptsubscript𝑉𝑡superscriptsubscript𝑉𝑡C\_{a}(S,t)\geq C\_{e}(S,t)=(T/t)^{n/2}\cdot V\_{t}^{\*}>V\_{t}^{\*} for 0<t<T0𝑡𝑇0<t<T.
∎

To find the replicating strategy, we again differentiate the price, getting

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δi:=∂C∂Si=C⋅(R−1​zt)iSi​σi​t=C⋅bi​(S,t)Si,assignsubscriptΔ𝑖𝐶subscript𝑆𝑖⋅𝐶subscriptsuperscript𝑅1subscript𝑧𝑡𝑖subscript𝑆𝑖subscript𝜎𝑖𝑡⋅𝐶subscript𝑏𝑖𝑆𝑡subscript𝑆𝑖\boxed{\Delta\_{i}:=\frac{\partial C}{\partial S\_{i}}=\frac{C\cdot(R^{-1}z\_{t})\_{i}}{S\_{i}\sigma\_{i}\sqrt{t}}=\frac{C\cdot b\_{i}(S,t)}{S\_{i}}}, |  | (86) |

where (R−1​zt)isubscriptsuperscript𝑅1subscript𝑧𝑡𝑖(R^{-1}z\_{t})\_{i} is the it​hsuperscript𝑖𝑡ℎi^{th} coordinate of the vector R−1​ztsuperscript𝑅1subscript𝑧𝑡R^{-1}z\_{t}. Thus, we have the relation Δi​Si/C=bi​(S,t)subscriptΔ𝑖subscript𝑆𝑖𝐶subscript𝑏𝑖𝑆𝑡\Delta\_{i}S\_{i}/C=b\_{i}(S,t).

###### Theorem 7.

The replicating strategy for Cover’s Derivative bets the fraction bi​(S,t)subscript𝑏𝑖𝑆𝑡b\_{i}(S,t) of wealth on stock i𝑖i in state (S,t)𝑆𝑡(S,t). Thus, to replicate Cover’s Derivative, one just uses the best rebalancing rule in hindsight as it is known at time t𝑡t.

For the general stock market, we have again concluded that the following three trading strategies are identical:

1. 1.

   The strategy that looks back over the known price history [0,t]0𝑡[0,t], finds the best continuously-rebalanced portfolio in hindsight, and uses that portfolio over the interval [t,t+d​t]𝑡𝑡𝑑𝑡[t,t+dt]
2. 2.

   The ΔΔ\Delta-hedging strategy induced by Cover’s Derivative
3. 3.

   The natural estimator Σ−1​(μ^−r​1)superscriptΣ1^𝜇𝑟1\Sigma^{-1}(\hat{\mu}-r\textbf{1}) of the continuous-time Kelly rule Σ−1​(μ−r​1)superscriptΣ1𝜇𝑟1\Sigma^{-1}(\mu-r\textbf{1}) (cf. Luenberger 1998).

## 4 Simulations

We proceed to give three simulations that help visualize the behavior of the replicating strategy over T:=200assign𝑇200T:=200 years under a risk-free rate of r:=0.02assign𝑟0.02r:=0.02. We let νi:=μi−σi2/2assignsubscript𝜈𝑖subscript𝜇𝑖subscriptsuperscript𝜎2𝑖2\nu\_{i}:=\mu\_{i}-\sigma^{2}\_{i}/2 denote the compound-annual growth rate of stock i𝑖i, and we normalize the initial stock prices to Si​0:=1assignsubscript𝑆𝑖01S\_{i0}:=1. We also normalize the trader’s initial wealth to $1currency-dollar1\$1. Simulations 1 and 2 deal with the univariate case. For the first 5 years of the experiment, the trader holds a single share of the stock. Then at t=5,𝑡5t=5, he puts all his money into Cover’s Derivative. The waiting period is necessary because C→+∞→𝐶C\to+\infty as t→0+→𝑡superscript0t\to 0^{+}. Thus, for t≤5𝑡5t\leq 5 the trader’s wealth is Stsubscript𝑆𝑡S\_{t}, and for t≥5𝑡5t\geq 5 his wealth is S5​C​(St,t)/C​(S5,5)subscript𝑆5𝐶subscript𝑆𝑡𝑡𝐶subscript𝑆55S\_{5}C(S\_{t},t)/C(S\_{5},5).

#### Simulation 1

We put ν:=0.04assign𝜈0.04\nu:=0.04 and σ:=0.7assign𝜎0.7\sigma:=0.7. The Kelly growth rate (Luenberger 1998) for this market is 9.17%percent9.179.17\% and the Kelly bet is b∗=0.54superscript𝑏0.54b^{\*}=0.54. The replicating strategy learns to hold significant cash balances and “live off the fluctuations,” which are substantial on account of the 70%percent7070\% annual volatility. Figure [8](#S4.F8 "Figure 8 ‣ Simulation 1 ‣ 4 Simulations ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") gives a sample path.

![Refer to caption](/html/1810.02485/assets/sim1.png)


Figure 8: Outcome for ν:=0.04,σ:=0.7.formulae-sequenceassign𝜈0.04assign𝜎0.7\nu:=0.04,\sigma:=0.7.

#### Simulation 2

Next, we use ν:=0.08assign𝜈0.08\nu:=0.08 and σ:=0.17assign𝜎0.17\sigma:=0.17. The Kelly growth rate is 11.6%percent11.611.6\% and the Kelly bet is b∗=2.57superscript𝑏2.57b^{\*}=2.57. The replicating strategy uses enormous leverage in an effort to exploit low interest rates and the favorable risk/return profile. This is Figure [9](#S4.F9 "Figure 9 ‣ Simulation 2 ‣ 4 Simulations ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper."). After 200 years, the stock price has appreciated from $1currency-dollar1\$1 a share to $100currency-dollar100\$100 million a share, but the replicating strategy has grown the initial dollar into $1currency-dollar1\$1 trillion.

![Refer to caption](/html/1810.02485/assets/sim2.png)


Figure 9: Outcome for ν:=0.08,σ:=0.17.formulae-sequenceassign𝜈0.08assign𝜎0.17\nu:=0.08,\sigma:=0.17.

#### Simulation 3

Finally, we simulate the bivariate case. At t=0𝑡0t=0, the trader puts $0.50currency-dollar0.50\$0.50 into each stock. He holds this portfolio for 5 years, and then he puts all his money into Cover’s Derivative. Thus, for t≤5𝑡5t\leq 5 his wealth is 0.5​[S1​(t)+S2​(t)]0.5delimited-[]subscript𝑆1𝑡subscript𝑆2𝑡0.5[S\_{1}(t)+S\_{2}(t)], and for t≥5𝑡5t\geq 5 his wealth is 0.5​[S1​(5)+S2​(5)]​C​(St,t)/C​(S5,5)0.5delimited-[]subscript𝑆15subscript𝑆25𝐶subscript𝑆𝑡𝑡𝐶subscript𝑆550.5[S\_{1}(5)+S\_{2}(5)]C(S\_{t},t)/C(S\_{5},5).

We use ν:=(0.03,0.08)′assign𝜈superscript0.030.08′\nu:=(0.03,0.08)^{\prime} and σ:=(0.55,0.7)′assign𝜎superscript0.550.7′\sigma:=(0.55,0.7)^{\prime}, with ρ:=0.2assign𝜌0.2\rho:=0.2 being the correlation of instantaneous returns. The Kelly growth rate is 13.7%percent13.713.7\% and the Kelly fractions are b∗=(0.39,0.56)′superscript𝑏superscript0.390.56′b^{\*}=(0.39,0.56)^{\prime}. Figure [10](#S4.F10 "Figure 10 ‣ Simulation 3 ‣ 4 Simulations ‣ Exact Replication of the Best Rebalancing Rule in Hindsight1footnote 11footnote 1I thank anonymous reviewers for their time, effort, and valuable comments that improved the paper.") gives the result. On this particular sample path, the replicating strategy uses leverage for decades on end, in spite of the fact that a Kelly gambler would continuously hold 5%percent55\% of wealth in cash.

![Refer to caption](/html/1810.02485/assets/sim3.png)


Figure 10: Outcome for ν:=(0.03,0.08)′,σ:=(0.55,0.7)′,ρ:=0.2.formulae-sequenceassign𝜈superscript0.030.08′formulae-sequenceassign𝜎superscript0.550.7′assign𝜌0.2\nu:=(0.03,0.08)^{\prime},\,\sigma:=(0.55,0.7)^{\prime},\,\rho:=0.2.

## 5 Limitations and Constraints

To close the paper, we briefly review the practical limitations of our framework and main results. First, our entire analysis resides squarely within the Black-Scholes complete market consisting of a risk-free bond and several correlated stocks in geometric Brownian motion. Accordingly, we have operated under the classical assumption of continuous trading in a frictionless environment that is free of taxes, transaction costs, and bid-ask spreads. Importantly, we have assumed that one can operate without any institutional constraints on leverage or value at risk. A potentially unlimited supply of margin loans is presumed to be available at the risk-free rate, and all securities can be sold short with full use of the proceeds. In accordance with the Kelly theory of asymptotic capital growth, the trader is willing to stomach any level of volatility or short-term drawdown in service of achieving the optimum asymptotic growth rate. As far as actual praxis on behalf of long lived institutions (say, sovereign wealth funds or university endowments), we have not modelled or simulated the behavior of our investment strategy in the presence of ongoing deposits and withdrawals.

Finally, we make the technical note that in certain (mathematically degenerate) situations, our “beat the market asymptotically” slogan can turn into “tie the market asymptotically.” For, if the best rebalancing rule in hindsight over [0,T]0𝑇[0,T] amounts to buying and holding one of the stocks (e.g. if b​(ST,T)𝑏subscript𝑆𝑇𝑇b(S\_{T},T) is a unit basis vector), then the compound growth rate of the practitioner will lag the best performing stock in the market (in the one-underlying case, the market itself) by an amount that becomes vanishingly small as T→∞→𝑇T\to\infty. This finite-sample growth rate lag is precisely the “cost of universality,” that is, the cost of having to learn the growth optimal rebalancing rule on-the-fly.

## 6 Conclusion

This paper priced and replicated an exotic option (“Cover’s Derivative”) whose payoff equals the final wealth that would have accrued to a $1currency-dollar1\$1 deposit into the best leveraged, continuously-rebalanced portfolio in hindsight. A rebalancing rule is a fixed-fraction betting scheme that trades continuously so as to maintain a target proportion bisubscript𝑏𝑖b\_{i} of wealth in each stock i𝑖i. For the Black-Scholes market with n𝑛n correlated stocks in geometric Brownian motion, the no-arbitrage price of Cover’s rebalancing option is C​(S,t)=(T/t)n/2​exp⁡(r​t+t⋅b′​Σ​b/2)𝐶𝑆𝑡superscript𝑇𝑡𝑛2𝑟𝑡⋅𝑡superscript𝑏′Σ𝑏2C(S,t)=(T/t)^{n/2}\exp(rt+t\cdot b^{\prime}\Sigma b/2), where b=b​(S,t)𝑏𝑏𝑆𝑡b=b(S,t) is the best rebalancing rule in hindsight over [0,t]0𝑡[0,t] and ΣΣ\Sigma is the covariance of instantaneous returns per unit time. Since C𝐶C is equal to (T/t)n/2superscript𝑇𝑡𝑛2(T/t)^{n/2} times intrinsic value, the American-style version of Cover’s Derivative will never be exercised early in equilibrium because the option is “worth more alive than dead.”

The order of magnitude C​(S,t;T)=𝒪​(Tn/2)𝐶𝑆𝑡𝑇𝒪superscript𝑇𝑛2C(S,t;T)=\mathcal{O}(T^{n/2}) agrees with the super-replicating price derived by Cover in his discrete-time universal portfolio theory. A sophisticated, long-lived institution that puts money into the replicating strategy (a strategy which turns out to be horizon-free) will grow its endowment at the same asymptotic rate as the best levered rebalancing rule in hindsight. In the long-run, with probability approaching 1, it will beat the market averages by an exponential factor. Of course, this guarantee is subject to the proviso that the best levered rebalancing rule in hindsight must sustain a higher asymptotic growth rate than the market index.

The replicating strategy amounts to betting the fraction bi​(S,t)subscript𝑏𝑖𝑆𝑡b\_{i}(S,t) of wealth on stock i𝑖i at time t𝑡t, where b​(S,t)𝑏𝑆𝑡b(S,t) is the best rebalancing rule in hindsight over the currently known price history. If someone knows the covariance ΣΣ\Sigma of instantaneous returns (but not necessarily the drifts of the various stocks), he can use the formula b​(S,t)=M−1​R−1​z/t𝑏𝑆𝑡superscript𝑀1superscript𝑅1𝑧𝑡b(S,t)=M^{-1}R^{-1}z/\sqrt{t}, where R𝑅R is the correlation matrix of instantaneous returns, M:=diag​(σ1,…,σn)assign𝑀diagsubscript𝜎1…subscript𝜎𝑛M:=\text{diag}(\sigma\_{1},...,\sigma\_{n}) is the (diagonal) matrix of volatilities, and zi:={log⁡(Si​t/Si​0)−(r−σi2/2)​t}/(σi​t)assignsubscript𝑧𝑖subscript𝑆𝑖𝑡subscript𝑆𝑖0𝑟superscriptsubscript𝜎𝑖22𝑡subscript𝜎𝑖𝑡z\_{i}:=\{\log(S\_{it}/S\_{i0})-(r-\sigma\_{i}^{2}/2)t\}/(\sigma\_{i}\sqrt{t}). But even if he is ignorant of ΣΣ\Sigma, he can still find b​(S,t)𝑏𝑆𝑡b(S,t) at any given time by hindsight-optimizing over the known price history.

Another expression for the replicating strategy is b​(S,t)=Σ−1​(μ^−r​1)𝑏𝑆𝑡superscriptΣ1^𝜇𝑟1b(S,t)=\Sigma^{-1}(\hat{\mu}-r\textbf{1}), where μ^i:=log⁡(Si​t/Si​0)/t+σi2/2assignsubscript^𝜇𝑖subscript𝑆𝑖𝑡subscript𝑆𝑖0𝑡superscriptsubscript𝜎𝑖22\hat{\mu}\_{i}:=\log(S\_{it}/S\_{i0})/t+\sigma\_{i}^{2}/2 is the natural estimator of the drift of stock i𝑖i. The replicating strategy converges in mean square to the continuous-time Kelly rule, b∗:=Σ−1​(μ−r​1)assignsuperscript𝑏superscriptΣ1𝜇𝑟1b^{\*}:=\Sigma^{-1}(\mu-r\textbf{1}), and its realized compound-growth rate converges to the Kelly (1956) optimum asymptotic growth rate, which is γ∗:=r+(1/2)​(μ−r​1)′​Σ−1​(μ−r​1)assignsuperscript𝛾𝑟12superscript𝜇𝑟1′superscriptΣ1𝜇𝑟1\gamma^{\*}:=r+(1/2)(\mu-r\textbf{1})^{\prime}\Sigma^{-1}(\mu-r\textbf{1}). This happens because the intrinsic value of Cover’s Derivative grows at an asymptotic rate of γ∗superscript𝛾\gamma^{\*} per unit time. A $1currency-dollar1\$1 deposit into the replicating strategy at time t𝑡t guarantees that the trader will achieve, at T𝑇T, the deterministic fraction VT∗/C​(St,t)superscriptsubscript𝑉𝑇𝐶subscript𝑆𝑡𝑡V\_{T}^{\*}/C(S\_{t},t) of the final wealth of the best rebalancing rule in hindsight. The excess continuously-compounded growth rate of VT∗superscriptsubscript𝑉𝑇V\_{T}^{\*} (over and above that of the replicating strategy) is at most {r​t+zt′​R−1​zt/2+n​log⁡(T/t)/2}/(T−t)𝑟𝑡superscriptsubscript𝑧𝑡′superscript𝑅1subscript𝑧𝑡2𝑛𝑇𝑡2𝑇𝑡\{rt+z\_{t}^{\prime}R^{-1}z\_{t}/2+n\log(T/t)/2\}/(T-t), which tends to 00 as T→∞→𝑇T\to\infty.

## Acknowledgment

I thank Erik Ordentlich and Thomas Cover for their timeless paper, The Cost of Achieving the Best Portfolio in Hindsight, which I found uplifting to the spirit.

## References

* [1]

  Barron, A. and Yu, J., 2003. Maximal Compounded Wealth for Portfolios of Stocks and Options. Working Paper.
* [2]

  Björk, T., 1998. Arbitrage Theory in Continuous Time. Oxford University Press.
* [3]

  Black, F. and Scholes, M., 1973. The Pricing of Options and Corporate Liabilities. Journal of Political Economy, 81(3), pp.637-654.
* [4]

  Cover, T.M., 1991. Universal Portfolios. Mathematical Finance, 1(1), pp.1-29.
* [5]

  Cover, T.M. and Gluss, D.H., 1986. Empirical Bayes Stock Market Portfolios. Advances in Applied Mathematics, 7(2), pp.170-181.
* [6]

  Cover, T.M. and Ordentlich, E., 1996. Universal Portfolios with Side Information. IEEE Transactions on Information Theory, 42(2), pp.348-363.
* [7]

  Cox, J.C., Ross, S.A. and Rubinstein, M., 1979. Option Pricing: A Simplified Approach. Journal of Financial Economics, 7(3), pp.229-263.
* [8]

  Cuchiero, C., Schachermayer, W. and Wong, T.K.L., 2016. Cover’s Universal Portfolio, Stochastic Portfolio Theory and the Numéraire Portfolio. arXiv preprint, arXiv:1611.09631.
* [9]

  DeMarzo, P., Kremer, I. and Mansour, Y., 2006, Online Trading Algorithms and Robust Option Pricing. In Proceedings of the Thirty-Eighth Annual ACM Symposium on Theory of Computing, pp.477-486.
* [10]

  Fernholz, E.R., 2002. Stochastic Portfolio Theory. Springer.
* [11]

  Gort, C., and Burgener, E., 2014. Rebalancing Using Options. Working Paper.
* [12]

  Györfi, L., Lugosi, G. and Udina, F., 2006. Nonparametric Kernel-Based Sequential Investment Strategies. Mathematical Finance 16(2), pp.337-357.
* [13]

  Ilmanen, A. and Maloney, T., 2015. Portfolio Rebalancing Part 1 of 2: Strategic Asset Allocation. AQR White Paper, 2015.
* [14]

  Israelov, R. and Tummala, H., 2018. An Alternative Option to Portfolio Rebalancing. The Journal of Derivatives, (25)3, pp.7-32.
* [15]

  Iyengar, G., 2005. Universal Investment in Markets with Transaction Costs. Mathematical Finance, 15(2), pp.359-371.
* [16]

  Jamshidian, F., 1992. Asymptotically Optimal Portfolios. Mathematical Finance, 2(2), pp.131-150.
* [17]

  Kelly, J.L., 1956. A New Interpretation of Information Rate. Bell System Technical Journal, 35(4), pp.917-926.
* [18]

  Kozat, S.S. and Singer, A.C., 2011. Universal Semiconstant Rebalanced Portfolios. Mathematical Finance, 21(2), pp.293-311.
* [19]

  Luenberger, D.G., 1998. Investment Science. Oxford University Press.
* [20]

  Merton, R.C., 1973. Theory of Rational Option Pricing. The Bell Journal of Economics and Management Science, pp.141-183.
* [21]

  Ordentlich, E. and Cover, T.M., 1998. The Cost of Achieving the Best Portfolio in Hindsight. Mathematics of Operations Research, 23(4), pp.960-982.
* [22]

  Parkes, D.C. and Huberman, B.A., 2001. Multiagent Cooperative Search for Portfolio Selection. Games and Economic Behavior, 35, pp.124-165.
* [23]

  Poundstone, W., 2010. Fortune’s Formula: The Untold Story of the Scientific Betting System that Beat the Casinos and Wall Street. Hill and Wang.
* [24]

  Reiner, E. and Rubinstein, M., 1992. Exotic Options. Working paper.
* [25]

  Rujeerapaiboon, N., Kuhn, D. and Wiesemann, W., 2015. Robust Growth-Optimal Portfolios. Management Science, 62(7), pp.2090-2109.
* [26]

  Stoltz, G. and Lugosi, G., 2005. Internal Regret in On-Line Portfolio Selection. Machine Learning, 59(1-2), pp.125-159.
* [27]

  Wilmott, P., 1998. Derivatives: the Theory and Practice of Financial Engineering. John Wiley & Sons.
* [28]

  Wilmott, P., 2001. Paul Wilmott Introduces Quantitative Finance. John Wiley & Sons.
* [29]

  Wong, T.K.L., 2015. Universal Portfolios in Stochastic Portfolio Theory. arXiv preprint, arXiv:1510.02808.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/1810.02485)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1810.02485)
[View original  
on arXiv](https://arxiv.org/abs/1810.02485)[►](javascript: void(0))