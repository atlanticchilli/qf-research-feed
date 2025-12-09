---
authors:
- Zachary Feinstein
doc_id: arxiv:2512.06505v1
family_id: arxiv:2512.06505
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Amortizing Perpetual Options
url_abs: http://arxiv.org/abs/2512.06505v1
url_html: https://arxiv.org/html/2512.06505v1
venue: arXiv q-fin
version: 1
year: 2025
---


Zachary Feinstein
School of Business, Stevens Institute of Technology, Hoboken, NJ 07030, USA, zfeinste@stevens.edu. Portions of this work are the subject of a provisional U.S. patent application filed by the author.

(December 6, 2025)

###### Abstract

In this work, we introduce *amortizing perpetual options* (AmPOs), a fungible variant of continuous-installment options suitable for exchange-based trading. Traditional installment options lapse when holders cease their payments, destroying fungibility across units of notional. AmPOs replace explicit installment payments and the need for lapsing logic with an implicit payment scheme via a deterministic decay in the claimable notional. This amortization ensures all units evolve identically, preserving fungibility. Under the Black-Scholes framework, AmPO valuation can be reduced to an equivalent vanilla perpetual American option on a dividend-paying asset. In this way, analytical expressions are possible for the exercise boundaries and risk-neutral valuations for calls and puts. These formulas and relations allow us to derive the Greeks and study comparative statics with respect to the amortization rate. Illustrative numerical case studies demonstrate how the amortization rate shapes option behavior and reveal the resulting tradeoffs in the effective volatility sensitivity.

## 1 Introduction

Perpetual contracts are experiencing a renaissance due to their adoption in decentralized finance and cryptocurrency markets. Though introduced in [[17](https://arxiv.org/html/2512.06505v1#bib.bib17)] for, e.g., a market on real estate indices, perpetual futures on cryptocurrencies are liquidly traded on a number of markets such as *Hyperliquid* and *Binance*. These contracts readily allow traders to purchase leveraged positions or to short assets which, otherwise, are technologically incapable of such a position; we refer the interested reader to, e.g., [[1](https://arxiv.org/html/2512.06505v1#bib.bib1), [3](https://arxiv.org/html/2512.06505v1#bib.bib3)]. However, perpetual futures only provide users with linear payoffs. Perpetual options, which replicate elements of the funding rate structure of perpetual futures, have recently been introduced in decentralized systems. We highlight everlasting options [[19](https://arxiv.org/html/2512.06505v1#bib.bib19)] and Panoptic [[14](https://arxiv.org/html/2512.06505v1#bib.bib14)] as specific perpetual option variants.

However, though perpetual futures have found wide usage in cryptocurrencies, perpetual options have *not* gained the same market share. Notably, the stochastic funding rates used in everlasting options and at Panoptic can be viewed as types of installment options. An installment option is one in which cash flows are exchanged between the long and short positions [[8](https://arxiv.org/html/2512.06505v1#bib.bib8), [4](https://arxiv.org/html/2512.06505v1#bib.bib4)]. Traditionally, these cash flows exist solely from the long to the short holders. Such options, however, only trade over-the-counter due to the nature of these contracts [[4](https://arxiv.org/html/2512.06505v1#bib.bib4)].
Specifically, installment options grant the holder a dual optionality: exercise or lapse. Because the lapsing logic comes from failure to make the installment payment in full, the notional units of these contracts are *not* identical and, therefore, cannot trade on an exchange.
For the purposes of this work, we specifically highlight continuous-installment (CI) options which require a continuous stream of payments from the option holder to the option underwriter in order to keep the contract alive [[12](https://arxiv.org/html/2512.06505v1#bib.bib12), [13](https://arxiv.org/html/2512.06505v1#bib.bib13)].

The remainder of this paper is organized as follows. In Section [2](https://arxiv.org/html/2512.06505v1#S2 "2 Amortizing Options ‣ Amortizing Perpetual Options"), we introduce an exchange-tradable variant of CI options; this is accomplished by replacing the explicit installment payments with implicit amortization of the options notional. In Section [3](https://arxiv.org/html/2512.06505v1#S3 "3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), under the Black-Scholes framework, we study the risk-neutral valuation and Greeks by determining an equivalence with vanilla perpetual American options for a dividend-paying asset. In that same section, we also extend the Greeks to consider sensitivity of the option behavior to the contractual amortization rate. Section [4](https://arxiv.org/html/2512.06505v1#S4 "4 Discussion and Applications ‣ Amortizing Perpetual Options") then presents a brief discussion of applicability of this new option type for use in hedging for both traditional and decentralized finance settings. Section [5](https://arxiv.org/html/2512.06505v1#S5 "5 Conclusion ‣ Amortizing Perpetual Options") concludes.

## 2 Amortizing Options

As highlighted within Section [1](https://arxiv.org/html/2512.06505v1#S1 "1 Introduction ‣ Amortizing Perpetual Options"), CI options present a novel approach to perpetual contracts which enforce an explicit time-cost on the option holder [[6](https://arxiv.org/html/2512.06505v1#bib.bib6), [12](https://arxiv.org/html/2512.06505v1#bib.bib12), [13](https://arxiv.org/html/2512.06505v1#bib.bib13)]. For such options, the buyer pays an initial premium V0>0V\_{0}>0 to the underwriter for a claimable notional of N0>0N\_{0}>0 upon exercise. However, in contrast to traditional options, the holder also needs to pay continuous installments ct​d​tc\_{t}dt per unit of notional to the underwriter to keep the contract alive. In this way, the holder has two forms of optionality:

1. 1.

   the right to exercise, and
2. 2.

   the right to lapse by halting the installment payments.

Installment options have been offered over-the-counter in a few markets: “installment warrants on Australian stocks listed on the Australian Stock Exchange (ASX) [[10](https://arxiv.org/html/2512.06505v1#bib.bib10), [4](https://arxiv.org/html/2512.06505v1#bib.bib4)], a 10-year warrant with nine annual payments offered by Deutsche Bank [[7](https://arxiv.org/html/2512.06505v1#bib.bib7)], and so on,”  [[12](https://arxiv.org/html/2512.06505v1#bib.bib12), Section 1]. However, because lapsing destroys fungibility across units of notional, i.e. partial lapsing by making a partial installment payment is *not* permissible, traditional CI options are not amenable to exchange-based trading.

###### Example 2.1.

Traditionally, as described in [[12](https://arxiv.org/html/2512.06505v1#bib.bib12)], CI options specify installments as either: (1) constant over time ct≡c>0c\_{t}\equiv c>0, or (2) a constant multiple of the underlying asset’s value ct≡γ​Stc\_{t}\equiv\gamma S\_{t} for underlying StS\_{t} with γ>0\gamma>0.

Herein we propose a variant of CI options. Instead of directly paying the continuous installments, the option holder implicitly sells a fraction of his or her option holdings back to the underwriter at the current premium.
Formally, if Nt>0N\_{t}>0 denotes the time tt claimable notional and Vt>0V\_{t}>0 denotes the option’s premium per unit notional, then funding the installment cost ct​Nt​d​tc\_{t}N\_{t}dt with a sale of the notional leads to an exponential decay in the notional:

|  |  |  |
| --- | --- | --- |
|  | d​Nt=−qt​Nt​d​t,qt=ct/Vt.dN\_{t}=-q\_{t}N\_{t}dt,\quad q\_{t}=c\_{t}/V\_{t}. |  |

Notably, because the notional is decreasing from these implicit payments, the requisite installment payments are also decreasing over time. In contrast to CI options in which the option underwriter is paid continuously in time, this option variant “pays” the underwriter via the decrease in his or her risk exposure.

###### Definition 2.2.

An amortizing perpetual option (AmPO) is an implicit payment, perpetual American CI option with installment costs ct=q​Vtc\_{t}=qV\_{t} for some constant amortization rate q>0q>0.

###### Remark 1.

While the fraction-of-premium installment payments (ct=q​Vtc\_{t}=qV\_{t}) implied by AmPO contracts is non-standard, it leads to a fixed, predictable amortization rate q>0q>0 for the notional.
In this way, the holder’s position deterministically decays over time, independent of the underlying market conditions.
On the other hand, the underwriter is continuously compensated in proportion to the notional and fair-value exposure being carried; this holds because the implicit installment payments reduce that exposure in line with the contract’s value.

In contrast, under standard CI structures (as in Example [2.1](https://arxiv.org/html/2512.06505v1#S2.Thmtheorem1 "Example 2.1. ‣ 2 Amortizing Options ‣ Amortizing Perpetual Options")), the amortization rate ct/Vtc\_{t}/V\_{t} can spike or plummet with market conditions. For instance, if the underlying asset’s price remains constant, but its volatility rises, then VtV\_{t} increases while ctc\_{t} remains constant. Under such a scenario, the realized amortization rate would fall, leaving the underwriter with a disproportionately large remaining exposure.

###### Remark 2.

Alternative installment payments (e.g., as in Example [2.1](https://arxiv.org/html/2512.06505v1#S2.Thmtheorem1 "Example 2.1. ‣ 2 Amortizing Options ‣ Amortizing Perpetual Options")) can be chosen instead, leading to time-varying amortization rates ct/Vtc\_{t}/V\_{t}.
Regardless of the installment cost structure, amortizing CI variants become exchange tradable as every unit of notional is always identical and cannot lapse independently, i.e., all contract units are perfectly fungible.
For such state-dependent amortization schedules, the valuation problem to be presented in Section [3.1](https://arxiv.org/html/2512.06505v1#S3.SS1 "3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") can be approached along the lines of [[2](https://arxiv.org/html/2512.06505v1#bib.bib2)].
For simplicity, herein we focus solely on the constant amortization case presented in Definition [2.2](https://arxiv.org/html/2512.06505v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Amortizing Options ‣ Amortizing Perpetual Options").

###### Remark 3.

Step options [[15](https://arxiv.org/html/2512.06505v1#bib.bib15), [9](https://arxiv.org/html/2512.06505v1#bib.bib9)] similarly feature payoffs with an effective notional that can decay over time. However, in contrast to the deterministic amortization of AmPOs, the decay in step options depends on the occupation time of the underlying, thus requiring path-dependent valuation and eliminating the fungibility required for exchange-based trading.

## 3 Risk-Neutral Valuation

|  | Call Option | Put Option |
| --- | --- | --- |
| Price | KαC−1​((αC−1)​S0αC​K)αC\frac{K}{\alpha\_{C}-1}\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{\alpha\_{C}} | K1+αP​(αP​K(1+αP)​S0)αP\frac{K}{1+\alpha\_{P}}\left(\frac{\alpha\_{P}K}{(1+\alpha\_{P})S\_{0}}\right)^{\alpha\_{P}} |
| Delta | ((αC−1)​S0αC​K)αC−1\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{\alpha\_{C}-1} | −(αP​K(1+αP)​S0)1+αP-\left(\frac{\alpha\_{P}K}{(1+\alpha\_{P})S\_{0}}\right)^{1+\alpha\_{P}} |
| Gamma | (αC−1)2αC​K​((αC−1)​S0αC​K)αC−2\frac{(\alpha\_{C}-1)^{2}}{\alpha\_{C}K}\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{\alpha\_{C}-2} | αP​KS02​(αP​K(1+αP)​S0)αP\frac{\alpha\_{P}K}{S\_{0}^{2}}\left(\frac{\alpha\_{P}K}{(1+\alpha\_{P})S\_{0}}\right)^{\alpha\_{P}} |
| Theta | 0 | 0 |
| Vega | 4​C0σ​log⁡((αC−1)​S0αC​K)​((αC−2)​r−q(2​αC−1)​σ2+2​r)\frac{4C\_{0}}{\sigma}\log\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)\left(\frac{(\alpha\_{C}-2)r-q}{(2\alpha\_{C}-1)\sigma^{2}+2r}\right) | 4​P0σ​log⁡((1+αP)​S0αP​K)​((2+αP)​r+q(2​αP+1)​σ2−2​r)\frac{4P\_{0}}{\sigma}\log\left(\frac{(1+\alpha\_{P})S\_{0}}{\alpha\_{P}K}\right)\left(\frac{(2+\alpha\_{P})r+q}{(2\alpha\_{P}+1)\sigma^{2}-2r}\right) |

Table 1: Summary table of AmPO risk-neutral valuation and Greeks for a constant notional exposure.

Within this section, we want to investigate the risk-neutral valuation of these AmPOs as presented in the prior section. To do so, we follow Assumption [3.1](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") throughout the remainder of this work.

###### Assumption 3.1.

Let (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) be a filtered probability space satisfying the usual conditions.
Consider a complete market with constant risk-free rate r≥0r\geq 0 and risky asset with price S=(St)t≥0S=(S\_{t})\_{t\geq 0}.
Let ℚ∼ℙ\mathbb{Q}\sim\mathbb{P} denote the unique risk-neutral measure for this market and consider the ℚ\mathbb{Q}-Brownian motion (w.r.t. (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0}) W=(Wt)t≥0W=(W\_{t})\_{t\geq 0}.
For the remainder of this work, we will assume that SS follows a geometric Brownian motion under ℚ\mathbb{Q}:

|  |  |  |
| --- | --- | --- |
|  | d​St=St​(r​d​t+σ​d​Wt)dS\_{t}=S\_{t}(rdt+\sigma dW\_{t}) |  |

with initial price S0>0S\_{0}>0 and volatility σ>0\sigma>0.

### 3.1 Pricing

To determine the risk-neutral value of an AmPO, we first observe a fundamental symmetry in the value process. Holding an AmPO involves a decaying notional Nt=e−q​t​N0N\_{t}=e^{-qt}N\_{0} on the options payoff Φ​(⋅)\Phi(\cdot). That is, from the holder’s perspective, the position’s value is Nt​V​(St)N\_{t}V(S\_{t}) for AmPO option value V​(⋅)V(\cdot) with payoff Nτ​Φ​(Sτ)N\_{\tau}\Phi(S\_{\tau}) at exercise time τ\tau. The amortization immediately shows up as an additional discounting term (i.e., an effective risk-free rate r+qr+q); with this augmented risk-free rate, the amortization also functionally appears as a drag on the modified drift to the underlying asset (i.e., an effective dividend yield qq). In this way, in Lemma [3.2](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we demonstrate that AmPO valuation perfectly coincides with (vanilla) perpetual American options under modified parameters.

###### Lemma 3.2.

The AmPO with amortization rate q>0q>0 is priced identically to the perpetual American option with the same payoff, effective risk-free rate r+qr+q, and dividend yield qq.

###### Proof.

Let V:ℝ+→ℝV:\mathbb{R}\_{+}\to\mathbb{R} denote the price of one unit of the AmPO as a function of the underlying.
Given an original notional position N0=1N\_{0}=1 wlog, the AmPO contract’s value at time tt is given by Πt=e−q​t​V​(St)\Pi\_{t}=e^{-qt}V(S\_{t}).
In particular, the discounted value process (e−r​t​Πt)t≥0(e^{-rt}\Pi\_{t})\_{t\geq 0} must be a ℚ\mathbb{Q}-martingale. Applying Itô’s lemma, we recover the standard Black-Scholes differential equation:

|  |  |  |
| --- | --- | --- |
|  | 0=12​σ2​St2​V′′​(St)+r​St​V′​(St)−(r+q)​V​(St).0=\frac{1}{2}\sigma^{2}S\_{t}^{2}V^{\prime\prime}(S\_{t})+rS\_{t}V^{\prime}(S\_{t})-(r+q)V(S\_{t}). |  |

The desired result follows directly by comparing this ODE to the standard result for perpetual American options on dividend-paying assets (see, e.g., [[11](https://arxiv.org/html/2512.06505v1#bib.bib11), Chapter 26.2]).
∎

Following Lemma [3.2](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), the pricing of call and put AmPOs trivially follow from the results of, e.g., [[11](https://arxiv.org/html/2512.06505v1#bib.bib11), Chapter 26.2]. For this reason, we omit the proof for the pricing of call and put AmPOs.

###### Corollary 3.3 (Call Option Pricing).

Consider a call AmPO with strike K>0K>0 and amortization rate q>0q>0.
The optimal exercise boundary is S¯C=αC​KαC−1\bar{S}\_{C}=\frac{\alpha\_{C}K}{\alpha\_{C}-1} for αC=(rσ2+12)2+2​(r+q)σ2−rσ2+12>1\alpha\_{C}=\sqrt{\left(\frac{r}{\sigma^{2}}+\frac{1}{2}\right)^{2}+\frac{2(r+q)}{\sigma^{2}}}-\frac{r}{\sigma^{2}}+\frac{1}{2}>1. Under optimal execution, the premium for this option is

|  |  |  |
| --- | --- | --- |
|  | C0=KαC−1​((αC−1)​S0αC​K)αC.C\_{0}=\frac{K}{\alpha\_{C}-1}\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{\alpha\_{C}}. |  |

###### Corollary 3.4 (Put Option Pricing).

Consider a put AmPO with strike K>0K>0 and amortization rate q>0q>0.
The optimal exercise boundary is S¯P=αP​K1+αP\bar{S}\_{P}=\frac{\alpha\_{P}K}{1+\alpha\_{P}} for αP=(rσ2+12)2+2​(r+q)σ2+rσ2−12>0\alpha\_{P}=\sqrt{\left(\frac{r}{\sigma^{2}}+\frac{1}{2}\right)^{2}+\frac{2(r+q)}{\sigma^{2}}}+\frac{r}{\sigma^{2}}-\frac{1}{2}>0. Under optimal execution, the premium for this option is

|  |  |  |
| --- | --- | --- |
|  | P0=K1+αP​(αP​K(1+αP)​S0)αP.P\_{0}=\frac{K}{1+\alpha\_{P}}\left(\frac{\alpha\_{P}K}{(1+\alpha\_{P})S\_{0}}\right)^{\alpha\_{P}}. |  |

We conclude this discussion of risk-neutral valuation by considering how the amortization qq can mimic an effective maturity date TT. That is, for a given amortization rate, we can define the effective maturity as the time TT such that the option’s premium coincides with a standard, dated American option with the same underlying dynamics.

###### Example 3.5.

Consider an asset price following Assumption [3.1](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") with risk-free rate r=5%r=5\%, volatility σ=50%\sigma=50\%, and initial price S0=100S\_{0}=100. Consider the at-the-money call option (i.e., K=100K=100) with amortization rate qq. In Figure [1(a)](https://arxiv.org/html/2512.06505v1#S3.F1.sf1 "In Figure 1 ‣ Example 3.5. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we plot the maturity of the at-the-money (American) call option which has the same premium as the AmPO with amortization rate qq.111As the assets under consideration here pay 0 dividends, American and European call options have the same premium. As expected, the effective maturity TT is decreasing in the amortization rate qq. Notably, even though the effective maturity is decreasing, the effective notional (e−q​Te^{-qT}) at the effective maturity is also decreasing in the amortization rate (see Figure [1(b)](https://arxiv.org/html/2512.06505v1#S3.F1.sf2 "In Figure 1 ‣ Example 3.5. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options")). For the selected parameters, even at high amortization rates (q≈1q\approx 1), the AmPO has over 65% of its original notional value remaining at the time that the equivalent dated option would expire.

![Refer to caption](x1.png)


(a) The effective maturity date TT as a function of the amortization rate qq.

![Refer to caption](x2.png)


(b) The effective notional (e−q​Te^{-qT}) of the AmPO with amortization rate qq at its effective maturity date TT.

Figure 1: Example [3.5](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem5 "Example 3.5. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"): Comparison of AmPO and dated at-the-money call options.

### 3.2 Greeks

As call and put AmPOs can be valued via an equivalence relation with perpetual American options as provided in Section [3.1](https://arxiv.org/html/2512.06505v1#S3.SS1 "3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we can follow standard results to determine the dependence of these structures on the underlying system parameters.
The main results from this section are summarized in Table [1](https://arxiv.org/html/2512.06505v1#S3.T1 "Table 1 ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options").
Throughout this section we omit the proofs as they follow directly from the aforementioned relation to vanilla perpetual American options.

###### Remark 4.

Herein we consider the Greeks of the valuation for a *constant* notional exposure, i.e., dependence of the explicit premia C0C\_{0} and P0P\_{0} for calls and puts, respectively. However, we note that the realized exposure is amortizing for an investor that is either long or short AmPOs. Therefore, in practice, the realized Greeks should be discounted by the amortization factor appropriately. (Further discussions will be provided for Theta in Remark [5](https://arxiv.org/html/2512.06505v1#Thmremark5 "Remark 5 (Theta). ‣ 3.2 Greeks ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") below.)

###### Corollary 3.6 (Delta).

Consider call and put AmPOs with strike K>0K>0 and amortization rate q>0q>0. The Delta for call and put options are provided, respectively, by:

|  |  |  |
| --- | --- | --- |
|  | ΔC:=∂C0∂S0={((αC−1)​S0αC​K)αC−1if ​S0≤S¯C1if ​S0>S¯C and ΔP:=∂P0∂S0={−(αP​K(1+αP)​S0)1+αPif ​S0≥S¯P−1if ​S0<S¯P.\Delta\_{C}:=\frac{\partial C\_{0}}{\partial S\_{0}}=\begin{cases}\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{\alpha\_{C}-1}&\text{if }S\_{0}\leq\bar{S}\_{C}\\ 1&\text{if }S\_{0}>\bar{S}\_{C}\end{cases}\quad\text{ and }\quad\Delta\_{P}:=\frac{\partial P\_{0}}{\partial S\_{0}}=\begin{cases}-\left(\frac{\alpha\_{P}K}{(1+\alpha\_{P})S\_{0}}\right)^{1+\alpha\_{P}}&\text{if }S\_{0}\geq\bar{S}\_{P}\\ -1&\text{if }S\_{0}<\bar{S}\_{P}.\end{cases} |  |

Furthermore, ΔC>0\Delta\_{C}>0 and ΔP<0\Delta\_{P}<0 for any S0>0S\_{0}>0.

###### Corollary 3.7 (Gamma).

Consider call and put AmPOs with strike K>0K>0 and amortization rate q>0q>0. The Gamma for call and put options are provided, respectively, by:

|  |  |  |
| --- | --- | --- |
|  | ΓC:=∂2C0∂S02={(αC−1)2αC​K​((αC−1)​S0αC​K)αC−2if ​S0≤S¯C0if ​S0>S¯C​ and ​ΓP:=∂2P0∂S02={αP​KS02​(αP​K(1+αP)​S0)αPif ​S0≥S¯P0if ​S0<S¯P.\Gamma\_{C}:=\frac{\partial^{2}C\_{0}}{\partial S\_{0}^{2}}=\begin{cases}\frac{(\alpha\_{C}-1)^{2}}{\alpha\_{C}K}\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{\alpha\_{C}-2}&\text{if }S\_{0}\leq\bar{S}\_{C}\\ 0&\text{if }S\_{0}>\bar{S}\_{C}\end{cases}\;\text{ and }\;\Gamma\_{P}:=\frac{\partial^{2}P\_{0}}{\partial S\_{0}^{2}}=\begin{cases}\frac{\alpha\_{P}K}{S\_{0}^{2}}\left(\frac{\alpha\_{P}K}{(1+\alpha\_{P})S\_{0}}\right)^{\alpha\_{P}}&\text{if }S\_{0}\geq\bar{S}\_{P}\\ 0&\text{if }S\_{0}<\bar{S}\_{P}.\end{cases} |  |

Furthermore, ΓC,ΓP≥0\Gamma\_{C},\Gamma\_{P}\geq 0 for any S0>0S\_{0}>0.

###### Remark 5 (Theta).

Theta, typically, refers to the dependence of the premium on the “time to maturity”. Because AmPOs are perpetual options, the risk-neutral price exhibits zero explicit time decay (e.g., ∂C0∂t=0\frac{\partial C\_{0}}{\partial t}=0 for call options).
However, due to the amortization, the holder or underwriter of such options will, in fact, have an *economic exposure* that depends on time. This decay is directly computable as −q​C0<0-qC\_{0}<0 or −q​P0<0-qP\_{0}<0 for call and put options, respectively. It is exactly this non-zero Theta(-like) decay that distinguishes AmPOs from vanilla perpetual options and creates an effective realized time exposure.

###### Corollary 3.8 (Vega).

Consider call and put AmPOs with strike K>0K>0 and amortization rate q>0q>0. The Vega for call and put options are provided, respectively, by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | νC\displaystyle\nu\_{C} | =∂C0∂σ={4​C0σ​log⁡((αC−1)​S0αC​K)​((αC−2)​r−q(2​αC−1)​σ2+2​r)if ​S0≤S¯C0if ​S0>S¯C\displaystyle=\frac{\partial C\_{0}}{\partial\sigma}=\begin{cases}\frac{4C\_{0}}{\sigma}\log\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)\left(\frac{(\alpha\_{C}-2)r-q}{(2\alpha\_{C}-1)\sigma^{2}+2r}\right)&\text{if }S\_{0}\leq\bar{S}\_{C}\\ 0&\text{if }S\_{0}>\bar{S}\_{C}\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | νP\displaystyle\nu\_{P} | =∂P0∂σ={4​P0σ​log⁡((1+αP)​S0αP​K)​((2+αP)​r+q(2​αP+1)​σ2−2​r)if ​S0≥S¯P0if ​S0<S¯P.\displaystyle=\frac{\partial P\_{0}}{\partial\sigma}=\begin{cases}\frac{4P\_{0}}{\sigma}\log\left(\frac{(1+\alpha\_{P})S\_{0}}{\alpha\_{P}K}\right)\left(\frac{(2+\alpha\_{P})r+q}{(2\alpha\_{P}+1)\sigma^{2}-2r}\right)&\text{if }S\_{0}\geq\bar{S}\_{P}\\ 0&\text{if }S\_{0}<\bar{S}\_{P}.\end{cases} |  |

Furthermore, νC,νP≥0\nu\_{C},\nu\_{P}\geq 0 for any S0>0S\_{0}>0.

###### Example 3.9.

Consider the same setting as Example [3.5](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem5 "Example 3.5. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"). Again comparing AmPOs to their effective dated counterparts, we want to consider the relative safety of AmPOs. In Figure [2(a)](https://arxiv.org/html/2512.06505v1#S3.F2.sf1 "In Figure 2 ‣ Example 3.9. ‣ 3.2 Greeks ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we plot the “safety ratio” between the AmPO Gamma and the Gamma of the effectively dated (American) call option. The lower this ratio, the more stable the option price is to fluctuations in the underlying. Notably, this ratio is increasing in the amortization rate, but stays below 80% for even extremely high amortization rates (e.g., q=1q=1). Similarly, in Figure [2(b)](https://arxiv.org/html/2512.06505v1#S3.F2.sf2 "In Figure 2 ‣ Example 3.9. ‣ 3.2 Greeks ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we consider the “cost efficiency” of AmPOs by computing the ratio between the economic Theta (i.e., −q​C0-qC\_{0}) from amortization against the Theta of the effectively dated option. Here, again, we find that the dated options lose value faster even at high amortization rates with a maximum observed efficiency ratio (at q=1q=1) of under 75%.

![Refer to caption](x3.png)


(a) The ratio of the AmPO Gamma against its effectively dated peer.

![Refer to caption](x4.png)


(b) The ratio of the AmPO (economic) Theta against its effectively dated peer.

Figure 2: Example [3.9](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem9 "Example 3.9. ‣ 3.2 Greeks ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"): Comparison of AmPO and dated at-the-money call options.

### 3.3 Comparative Statistics on Amortization Rate

Finally, as the amortization rate qq appears directly within both the effective risk free rate (r+qr+q) and effective dividend yield (qq) of the equivalently valued perpetual American option, the choice of this contractual parameter can have a strong influence on the valuation and Greeks of AmPOs.
However, since we have proposed AmPOs to maintain a constant qq throughout the lifetime of the option, we do not want to consider this dependence in the same way as the Greeks (i.e., for hedging purposes), but rather as a way to understand the implications and tradeoffs of choosing the qq for a contract. In doing so, we will focus on three aspects of the AmPO contracts: the risk-neutral valuation; the optimal exercise boundary; and the Vega. Throughout this section we set α¯:=(αC+αP)/2>0\bar{\alpha}:=(\alpha\_{C}+\alpha\_{P})/2>0 for notational simplicity.

###### Assumption 3.10.

For simplicity of notation, throughout this section we consider S0≤S¯CS\_{0}\leq\bar{S}\_{C} for call options and S0≥S¯PS\_{0}\geq\bar{S}\_{P} for put options.

First, as expected, increasing qq accelerates economic amortization, reducing the value for the holder and, therefore, also the premium. This is provided in Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") below.

###### Corollary 3.11.

Consider call and put AmPOs with strike K>0K>0. The premium for both option types is decreasing in the amortization rate q>0q>0:

|  |  |  |
| --- | --- | --- |
|  | ∂C0∂q=C0σ2​α¯​log⁡((αC−1)​S0αC​K)≤0 and ∂P0∂q=−P0σ2​α¯​log⁡((1+αP)​S0αP​K)≤0.\frac{\partial C\_{0}}{\partial q}=\frac{C\_{0}}{\sigma^{2}\bar{\alpha}}\log\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)\leq 0\quad\text{ and }\quad\frac{\partial P\_{0}}{\partial q}=-\frac{P\_{0}}{\sigma^{2}\bar{\alpha}}\log\left(\frac{(1+\alpha\_{P})S\_{0}}{\alpha\_{P}K}\right)\leq 0. |  |

###### Proof.

Consider the call AmPO; we omit the proof of put AmPOs as the arguments follow comparably.
Recall from Corollary [3.3](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem3 "Corollary 3.3 (Call Option Pricing). ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") that the premium of the call AmPO C0C\_{0} depends on the amortization rate qq solely through αC\alpha\_{C}. Thus, through an application of the chain rule, we find ∂C0∂q=∂C0∂αC​∂αC∂q\frac{\partial C\_{0}}{\partial q}=\frac{\partial C\_{0}}{\partial\alpha\_{C}}\frac{\partial\alpha\_{C}}{\partial q}. By differentiation, we find

|  |  |  |
| --- | --- | --- |
|  | ∂C0∂αC=C0​log⁡((αC−1)​S0αC​K)≤0 and ∂αC∂q=1σ2​α¯>0\displaystyle\frac{\partial C\_{0}}{\partial\alpha\_{C}}=C\_{0}\log\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)\leq 0\quad\text{ and }\quad\frac{\partial\alpha\_{C}}{\partial q}=\frac{1}{\sigma^{2}\bar{\alpha}}>0 |  |

thus completing the proof.
∎

###### Remark 6.

Within Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we found that the premium for both AmPO calls and puts are decreasing in the amortization rate qq. In fact, it can easily be seen that the limiting behavior of these options is to vanilla perpetual American options as q↘0q\searrow 0 and to the intrinsic value of the option as q↗∞q\nearrow\infty.

As the option premium decreases in the amortization rate, the optimal exercise boundary is similarly decaying towards the strike price (i.e., decreasing for call options and increasing for put options). In this way, the optimal exercise becomes more conservative as the amortization accelerates.

###### Corollary 3.12.

Consider call and put AmPOs with strike K>0K>0. The optimal exercise boundary is decreasing to KK for call options and increasing to KK for put options as qq increases, i.e.,

|  |  |  |
| --- | --- | --- |
|  | ∂S¯C∂q=−Kσ2​(αC−1)2​α¯≤0 and ∂S¯P∂q=Kσ2​(1+αP)2​α¯≥0\frac{\partial\bar{S}\_{C}}{\partial q}=-\frac{K}{\sigma^{2}(\alpha\_{C}-1)^{2}\bar{\alpha}}\leq 0\quad\text{ and }\quad\frac{\partial\bar{S}\_{P}}{\partial q}=\frac{K}{\sigma^{2}(1+\alpha\_{P})^{2}\bar{\alpha}}\geq 0 |  |

with limq↗∞S¯C=K\lim\_{q\nearrow\infty}\bar{S}\_{C}=K and limq↗∞S¯P=K\lim\_{q\nearrow\infty}\bar{S}\_{P}=K.

###### Proof.

As with the proof of Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), this result trivially follows from an application of the chain rule as S¯C,S¯P\bar{S}\_{C},\bar{S}\_{P} depend only on qq through αC,αP\alpha\_{C},\alpha\_{P} respectively.
∎

Finally, we find that not only does the AmPO premium decrease and the optimal exercise boundary decay, as amortization accelerates, but we also see that the Vega of these options also drops. In this way, higher amortization rates can lead to option prices that are less sensitive to the underlying market dynamics. In fact, as highlighted in Remark [6](https://arxiv.org/html/2512.06505v1#Thmremark6 "Remark 6. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), as the amortization rate approaches ∞\infty, the premium of these options approaches the intrinsic value which is insensitive to the volatility.

###### Corollary 3.13.

Consider call and put AmPOs with strike K>0K>0. The Vega is decreasing in the amortization rate qq.

###### Proof.

Fix the amortization rate q>0q>0.

* •

  *Call Options:* Consider the dependence of C0C\_{0} on qq as provided in Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"). Notably, the dependence on σ\sigma occurs only through αC\alpha\_{C} and α¯\bar{\alpha}.
  Thus, from an application of the chain rule, we find

  |  |  |  |
  | --- | --- | --- |
  |  | ∂2C0∂σ​∂q=(∂∂αC​∂C0∂q)​∂αC∂σ+(∂∂α¯​∂C0∂q)​∂α¯∂σ.\frac{\partial^{2}C\_{0}}{\partial\sigma\partial q}=\left(\frac{\partial}{\partial\alpha\_{C}}\frac{\partial C\_{0}}{\partial q}\right)\frac{\partial\alpha\_{C}}{\partial\sigma}+\left(\frac{\partial}{\partial\bar{\alpha}}\frac{\partial C\_{0}}{\partial q}\right)\frac{\partial\bar{\alpha}}{\partial\sigma}. |  |

  Expanding out each individual term we conclude

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂∂αC​∂C0∂q\displaystyle\frac{\partial}{\partial\alpha\_{C}}\frac{\partial C\_{0}}{\partial q} | =C0σ2​αC​α¯[αC(αC−1)log((αC−1)​S0αC​K)2+1]>0\displaystyle=\frac{C\_{0}}{\sigma^{2}\alpha\_{C}\bar{\alpha}}\left[\alpha\_{C}(\alpha\_{C}-1)\log\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)^{2}+1\right]>0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂αC∂σ\displaystyle\frac{\partial\alpha\_{C}}{\partial\sigma} | =1σ3​[2​r−2​r2+σ2​(3​r+2​q)σ2​α¯]\displaystyle=\frac{1}{\sigma^{3}}\left[2r-\frac{2r^{2}+\sigma^{2}(3r+2q)}{\sigma^{2}\bar{\alpha}}\right] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂∂α¯​∂C0∂q\displaystyle\frac{\partial}{\partial\bar{\alpha}}\frac{\partial C\_{0}}{\partial q} | =−C0σ2​α¯2​log⁡((αC−1)​S0αC​K)>0\displaystyle=-\frac{C\_{0}}{\sigma^{2}\bar{\alpha}^{2}}\log\left(\frac{(\alpha\_{C}-1)S\_{0}}{\alpha\_{C}K}\right)>0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂α¯∂σ\displaystyle\frac{\partial\bar{\alpha}}{\partial\sigma} | =−2​r2+σ2​(3​r+2​q)σ5​α¯<0.\displaystyle=-\frac{2r^{2}+\sigma^{2}(3r+2q)}{\sigma^{5}\bar{\alpha}}<0. |  |

  Thus the stated monotonicity of Vega holds if ∂αC∂σ<0\frac{\partial\alpha\_{C}}{\partial\sigma}<0. In fact, this is easily verified by observing 4​r2​σ4​α¯2<(2​r2+σ2​(3​r+2​q))24r^{2}\sigma^{4}\bar{\alpha}^{2}<(2r^{2}+\sigma^{2}(3r+2q))^{2}.
* •

  *Put Options:* Consider the dependence of P0P\_{0} on qq as provided in Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"). Notably, the dependence on σ\sigma occurs only through αP\alpha\_{P} and α¯\bar{\alpha}.
  Thus, from an application of the chain rule, we find

  |  |  |  |
  | --- | --- | --- |
  |  | ∂2P0∂σ​∂q=(∂∂αP​∂P0∂q)​∂αP∂σ+(∂∂α¯​∂P0∂q)​∂α¯∂σ.\frac{\partial^{2}P\_{0}}{\partial\sigma\partial q}=\left(\frac{\partial}{\partial\alpha\_{P}}\frac{\partial P\_{0}}{\partial q}\right)\frac{\partial\alpha\_{P}}{\partial\sigma}+\left(\frac{\partial}{\partial\bar{\alpha}}\frac{\partial P\_{0}}{\partial q}\right)\frac{\partial\bar{\alpha}}{\partial\sigma}. |  |

  Expanding out each individual term we immediately reach the desired monotonicity:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂∂αP​∂P0∂q\displaystyle\frac{\partial}{\partial\alpha\_{P}}\frac{\partial P\_{0}}{\partial q} | =P0σ2​α¯[log((1+αP)​S0αP​K)2+1(1+αP)​αP]>0\displaystyle=\frac{P\_{0}}{\sigma^{2}\bar{\alpha}}\left[\log\left(\frac{(1+\alpha\_{P})S\_{0}}{\alpha\_{P}K}\right)^{2}+\frac{1}{(1+\alpha\_{P})\alpha\_{P}}\right]>0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂αP∂σ\displaystyle\frac{\partial\alpha\_{P}}{\partial\sigma} | =−1σ3​[2​r+2​r2+σ2​(3​r+2​q)σ2​α¯]<0\displaystyle=-\frac{1}{\sigma^{3}}\left[2r+\frac{2r^{2}+\sigma^{2}(3r+2q)}{\sigma^{2}\bar{\alpha}}\right]<0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂∂α¯​∂P0∂q\displaystyle\frac{\partial}{\partial\bar{\alpha}}\frac{\partial P\_{0}}{\partial q} | =P0σ2​α¯2​log⁡((1+αP)​S0αP​K)>0\displaystyle=\frac{P\_{0}}{\sigma^{2}\bar{\alpha}^{2}}\log\left(\frac{(1+\alpha\_{P})S\_{0}}{\alpha\_{P}K}\right)>0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∂α¯∂σ\displaystyle\frac{\partial\bar{\alpha}}{\partial\sigma} | =−2​r2+σ2​(3​r+2​q)σ5​α¯<0.\displaystyle=-\frac{2r^{2}+\sigma^{2}(3r+2q)}{\sigma^{5}\bar{\alpha}}<0. |  |

∎

In the prior Examples [3.5](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem5 "Example 3.5. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") and [3.9](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem9 "Example 3.9. ‣ 3.2 Greeks ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"), we have analyzed how AmPOs compare with dated options. In the following example, we wish to consider how selecting the amortization rate can be used to optimize a volatility-based strategy.

###### Example 3.14.

Consider the setting of Example [3.5](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem5 "Example 3.5. ‣ 3.1 Pricing ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"). Recall from Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") and Corollary [3.13](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") that both the premium and Vega of an AmPO are decreasing in the amortization rate qq. As the realized Vega of a position depends on the budget actually invested, we now want to consider how the ratio of the Vega to premium behaves to consider a simplified optimization problem: consider an investor who wants to take as leveraged a volatility position as possible using AmPOs with a $100 budget constraint. To do so, we consider three strategies: bullish volatility with call options (Figure [3(a)](https://arxiv.org/html/2512.06505v1#S3.F3.sf1 "In Figure 3 ‣ Example 3.14. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options")); bearish volatility with put options (Figure [3(b)](https://arxiv.org/html/2512.06505v1#S3.F3.sf2 "In Figure 3 ‣ Example 3.14. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options")); and neutral volatility with an at-the-money straddle (Figure [3(c)](https://arxiv.org/html/2512.06505v1#S3.F3.sf3 "In Figure 3 ‣ Example 3.14. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options")). Notably, though bullish and neutral strategies have increasing positional Vegas, the bearish strategy has a non-monotonic behavior coming from the simultaneous drop in both premium and Vega. For the current parameter setting, the optimal bearish volatility strategy (which also provides the maximum positional Vega among all 3 strategies) is with an amortization rate of q∗≈14.26%q^{\*}\approx 14.26\%.

![Refer to caption](x5.png)


(a) Call options

![Refer to caption](x6.png)


(b) Put options

![Refer to caption](x7.png)


(c) Straddle

Figure 3: Example [3.14](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem14 "Example 3.14. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options"): Vega of a $100 position in call, put, and straddle strategies.

## 4 Discussion and Applications

Thus far, we have considered the construction and valuation of AmPOs. Within this section, we will briefly consider use cases for these novel perpetual options. In doing so, we will consider applications both within traditional financial markets and decentralized, i.e., blockchain-based, markets.

### 4.1 Traditional Finance

Consider that installment options have been traded in over-the-counter markets already [[12](https://arxiv.org/html/2512.06505v1#bib.bib12)]. However, as noted in Section [2](https://arxiv.org/html/2512.06505v1#S2 "2 Amortizing Options ‣ Amortizing Perpetual Options"), such options are non-fungible because of the specific requirements of installment payments and lapsing logic. In contrast, AmPOs provide an option type that can be transacted on a central limit order book. This exchange-based tradability permits more robust price-discovery and the possibility of more frequent transactions (due to, e.g., the ability to close long and short positions easily with market operations).

Notably, due to the deterministic cost-of-carry of AmPOs, large institutional investors (e.g., pension plans) can hold a large perpetual protective position while only needing to pay small re-upping charges to maintain the desired notional exposure. This is in contrast to dated options which require rolls around the expiry date. Such rolling operations become high-risk events due to the timing involved as, e.g., the Greeks of at-the-money options can explode near expiry.

### 4.2 Decentralized Finance

While exchange-tradability is beneficial in traditional markets, it is essential for use in decentralized finance (DeFi) due to the unique nature of blockchain technologies. Though non-fungible tokens exist in decentralized finance, they are generally traded in illiquid markets, such as *OpenSea*, because every contract would need to find a specific counterparty. In comparison, fungible tokens trade in liquid off-chain limit order books or on-chain automated market makers.

Automated market makers function by holding reserves of two or more assets against which anyone can transact [[5](https://arxiv.org/html/2512.06505v1#bib.bib5)]. These asset reserves are supplied by liquidity providers in exchange for the fees earned on every transaction. However, though the liquidity providers earn fees, their supplied assets are at risk of being sold to liquidity takers. Because of adverse selection effects, the effective position held by the liquidity providers (less the fees) is strictly worse than if replicated in an external market; this economic difference has been termed the loss-versus-rebalancing [[16](https://arxiv.org/html/2512.06505v1#bib.bib16)]. Notably, as a variant of CI options, AmPOs would be readily usable to hedge against this loss-versus-rebalancing [[18](https://arxiv.org/html/2512.06505v1#bib.bib18)] without requiring rolling-based risks.

## 5 Conclusion

Within this work, we introduced amortizing perpetual options, a fungible variant of continuous-installment options which are, therefore, suitable for exchange-based trading. Under a constant amortization rate, we found an equivalence relation between AmPOs and vanilla perpetual American options on dividend-paying assets. This relation permits standard analytical valuations and, thus, allowed us to characterize the Greeks and analyze the sensitivities of option behavior to the contractual amortization rate.

Our analysis in Section [3](https://arxiv.org/html/2512.06505v1#S3 "3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options") assumed the complete market structure of the Black-Scholes framework with the constant amortization rate. Extending the study of AmPOs to incomplete markets and stochastic amortization rates presents several natural directions for future work. For instance, one could investigate the optimal amortization rate for long and short positions as there is a natural tradeoff between a higher amortization rate and lower initial premium (Corollary [3.11](https://arxiv.org/html/2512.06505v1#S3.Thmtheorem11 "Corollary 3.11. ‣ 3.3 Comparative Statistics on Amortization Rate ‣ 3 Risk-Neutral Valuation ‣ Amortizing Perpetual Options")). In this way, an equilibrium amortization rate can arise from utility-indifference or heterogeneous-agent considerations. Such extensions would provide a framework for designing amortization rates in practice.

## References

* Ackerer et al., [2023]

  Ackerer, D., Hugonnier, J., and Jermann, U. (2023).
  Perpetual futures pricing.
  Mathematical Finance.
* Al-Hadad and Palmowski, [2024]

  Al-Hadad, J. and Palmowski, Z. (2024).
  Perpetual american options with asset-dependent discounting.
  Applied Mathematics & Optimization, 89(1):18.
* Angeris et al., [2023]

  Angeris, G., Chitra, T., Evans, A., and Lorig, M. (2023).
  A primer on perpetuals.
  SIAM Journal on Financial Mathematics, 14(1):SC17–SC30.
* Ben-Ameur et al., [2006]

  Ben-Ameur, H., Breton, M., and François, P. (2006).
  A dynamic programming approach to price installment options.
  European Journal of Operational Research, 169(2):667–676.
* Bichuch and Feinstein, [2022]

  Bichuch, M. and Feinstein, Z. (2022).
  Axioms for automated market makers: A mathematical framework in
  fintech and decentralized finance.
  arXiv preprint arXiv:2210.01227.
* Ciurlia and Caperdoni, [2009]

  Ciurlia, P. and Caperdoni, C. (2009).
  A note on the pricing of perpetual continuous-installment options.
  Mathematical Methods in Economics and Finance, 4(1):11–26.
* Davis et al., [2001]

  Davis, M. H., Schachermayer, W., and Tompkins, R. G. (2001).
  Pricing, no-arbitrage bounds and robusthedging of instalment options.
  Quantitative Finance, 1(6):597.
* Davis et al., [2002]

  Davis, M. H., Schachermayer, W., and Tompkins, R. G. (2002).
  Installment options and static hedging.
  The Journal of Risk Finance, 3(2):46–52.
* Detemple et al., [2020]

  Detemple, J., Abdou, S. L., and Moraux, F. (2020).
  American step options.
  European Journal of Operational Research, 282(1):363–385.
* François, [2005]

  François, P. (2005).
  Pricing asx installment warrants under garch h. ben-ameur, m. breton.
  Les Cahiers du GERAD ISSN, 711:2440.
* Hull, [2018]

  Hull, J. C. (2018).
  Options, Futures, and Other Derivatives.
  Pearson, 10th edition.
* Kimura, [2009]

  Kimura, T. (2009).
  American continuous-installment options: Valuation and premium
  decomposition.
  SIAM Journal on Applied Mathematics, 70(3):803–824.
* Kimura, [2010]

  Kimura, T. (2010).
  Valuing continuous-installment options.
  European Journal of Operational Research, 201(1):222–230.
* Lambert and Kristensen, [2022]

  Lambert, G. and Kristensen, J. (2022).
  Panoptic: the perpetual, oracle-free options protocol.
  arXiv preprint arXiv:2204.14232.
* Linetsky, [1999]

  Linetsky, V. (1999).
  Step options.
  Mathematical Finance, 9(1):55–96.
* Milionis et al., [2022]

  Milionis, J., Moallemi, C. C., Roughgarden, T., and Zhang, A. L. (2022).
  Automated market making and loss-versus-rebalancing.
  arXiv preprint arXiv:2208.06046.
* Shiller, [1993]

  Shiller, R. J. (1993).
  Measuring asset values for cash settlement in derivative markets:
  hedonic repeated measures indices and perpetual futures.
  The Journal of Finance, 48(3):911–931.
* Singh et al., [2025]

  Singh, S. F., Li, R. K. X., Gaskin, S., Wu, Y., Klinck, J., Michalopoulos, P.,
  Poulos, Z., and Veneris, A. (2025).
  Modeling loss-versus-rebalancing in automated market makers via
  continuous-installment options.
  arXiv preprint arXiv:2508.02971.
* White and Bankman-Fried, [2021]

  White, D. and Bankman-Fried, S. (2021).
  Everlasting options.
  <https://www.paradigm.xyz/2021/05/everlasting-options>.