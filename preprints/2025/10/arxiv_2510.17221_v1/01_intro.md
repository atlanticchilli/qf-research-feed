---
authors:
- Jacek Wszoła
- Krzysztof Burnecki
- Marek Teuerle
- Martyna Zdeb
doc_id: arxiv:2510.17221v1
family_id: arxiv:2510.17221
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Design and valuation of multi-region CoCoCat bonds
url_abs: http://arxiv.org/abs/2510.17221v1
url_html: https://arxiv.org/html/2510.17221v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jacek Wszoła, Krzysztof Burnecki, Marek Teuerle, Martyna Zdeb
Jacek Wszoła, Krzysztof Burnecki, Marek Teuerle, Martyna Zdeb
  
Faculty of Pure and Applied Mathematics
  
Wrocław University of Science and Technology
  
Wyspiańskiego 27
  
50-370 Wrocław, Poland
[krzysztof.burnecki@pwr.edu.pl](mailto:krzysztof.burnecki@pwr.edu.pl)

(Date: August 26, 2025)

###### Abstract.

This paper introduces a novel multidimensional insurance-linked instrument: a contingent convertible bond (CoCoCat bond) whose conversion trigger is activated by predefined natural catastrophes across multiple geographical regions. We develop such a model explicitly accounting for the complex dependencies between regional catastrophe losses. Specifically, we explore scenarios ranging from complete independence to proportional loss dependencies, both with fixed and random loss amounts. Utilizing change-of-measure techniques, we derive risk-neutral pricing formulas tailored to these diverse dependence structures. By fitting our model to real-world natural catastrophe data from Property Claim Services, we demonstrate the significant impact of inter-regional dependencies on the CoCoCat bond’s pricing, highlighting the importance of multidimensional risk assessment for this innovative financial instrument.

Work supported by NCN Grant No. 2022/47/B/HS4/02139

## 1. Introduction

Insurance-linked securities (ILS) represent a class of financial instruments designed to transfer specific insurance-related risks, predominantly those associated with natural catastrophes but increasingly encompassing other areas such as cyber, mortality, and longevity risks, from sponsoring entities to capital market investors [[12](https://arxiv.org/html/2510.17221v1#bib.bib12), [2](https://arxiv.org/html/2510.17221v1#bib.bib2), [7](https://arxiv.org/html/2510.17221v1#bib.bib7), [34](https://arxiv.org/html/2510.17221v1#bib.bib34)]. Sponsors typically include insurance and reinsurance companies seeking alternative risk capital or capacity, but also governments and corporations seeking to manage exposure to extreme events [[27](https://arxiv.org/html/2510.17221v1#bib.bib27), [20](https://arxiv.org/html/2510.17221v1#bib.bib20)]. The fundamental mechanism involves the sponsor paying a premium or coupon to investors in exchange for financial protection against predefined trigger events. This protection is facilitated through a Special Purpose Vehicle (SPV), an entity created specifically for the transaction, which issues the securities (often bonds) to investors. The proceeds from the issuance are held in a collateral account, usually invested in highly secure, liquid assets. If no triggering event occurs during the security’s term, investors receive their principal back along with the agreed-upon coupon payments, which typically offer a premium over risk-free rates. However, if a predefined trigger event (e.g., a hurricane of a certain intensity hitting a specific region, industry losses exceeding a threshold, or the sponsor’s own losses surpassing a level) occurs, the principal, and sometimes accrued interest, is partially or fully forgiven and used to cover the sponsor’s claims arising from the event [[2](https://arxiv.org/html/2510.17221v1#bib.bib2)].

This structure offers potential benefits to both parties. For sponsors, ILS provide access to the vast capacity of the capital markets, which significantly exceeds that of the traditional reinsurance market, allowing for the transfer of large, peak risks that might otherwise be difficult or expensive to reinsure. It diversifies their sources of risk capital, potentially reduces counterparty credit risk (as ILS are typically fully collateralized), and can offer multi-year coverage stability [[12](https://arxiv.org/html/2510.17221v1#bib.bib12)]. For investors, ILS offer the potential for attractive yields and, crucially, returns that are largely uncorrelated with traditional financial assets like stocks and bonds, since the underlying risks (e.g., natural disasters) are generally independent of economic cycles. This low correlation makes ILS a valuable tool for portfolio diversification [[13](https://arxiv.org/html/2510.17221v1#bib.bib13), [14](https://arxiv.org/html/2510.17221v1#bib.bib14)].

While early ILS transactions often focused on single, well-understood peak perils in specific regions (e.g., US hurricane risk), the market has evolved to include more complex structures covering multiple perils and/or multiple geographic regions. Multi-peril ILS bundle coverage for different types of risks (e.g., earthquake and windstorm) within a single instrument, while multi-region ILS cover risks across different geographical areas (e.g., US and Europe, or multiple countries within a region). Examples include bonds covering US wind and earthquake jointly, North American multiperil risks, or combinations like European wind and Turkish earthquake [[49](https://arxiv.org/html/2510.17221v1#bib.bib49), [34](https://arxiv.org/html/2510.17221v1#bib.bib34)].
In [[11](https://arxiv.org/html/2510.17221v1#bib.bib11)] a framework for pricing insurance-linked securities that are associated with multiple natural catastrophe risks was developed. As a representative case, a multi-peril catastrophe bond was designed that can be linked either to industry loss indices or to the actual losses experienced by an insurer.

The literature proposes several theoretical frameworks to address the challenges of pricing ILS in incomplete markets. Arbitrage-Free Pricing (Risk-Neutral Framework) adapts standard asset pricing theory. One method assumes investors are risk-neutral specifically towards the non-systematic jump risk associated with catastrophe events, implying the risk-neutral probability measure for these events coincides with the real-world physical probability measure [[3](https://arxiv.org/html/2510.17221v1#bib.bib3), [17](https://arxiv.org/html/2510.17221v1#bib.bib17)]. Alternatively, pricing can be performed under an equivalent martingale measure derived using techniques such as the Esscher transform or the Wang transform, which explicitly incorporate a market price of the risk parameter to adjust probabilities [[4](https://arxiv.org/html/2510.17221v1#bib.bib4), [53](https://arxiv.org/html/2510.17221v1#bib.bib53)]. Another approach is contingent claim analysis (CCA). This framework values ILS, particularly catastrophe bonds, as derivative securities, similar to options written on an underlying measure of catastrophe loss or event occurrence [[40](https://arxiv.org/html/2510.17221v1#bib.bib40), [45](https://arxiv.org/html/2510.17221v1#bib.bib45), [52](https://arxiv.org/html/2510.17221v1#bib.bib52)]. It is also worth mentioning utility-based frameworks. These models analyse the decision to issue or invest in ILS from the perspective of maximising expected utility [[38](https://arxiv.org/html/2510.17221v1#bib.bib38), [47](https://arxiv.org/html/2510.17221v1#bib.bib47)].

Complementing theoretical models, empirical and statistical approaches aim to explain observed ILS prices or forecast future prices based on data. Early empirical work focused on identifying the key determinants of ILS spreads (the premium over the risk-free rate) at issuance using linear or log-linear regression models [[33](https://arxiv.org/html/2510.17221v1#bib.bib33)]. Common explanatory variables include measures of risk (expected loss (EL), probability of first loss (PFL)), bond characteristics (term, size, trigger type, peril, region, sponsor identity/quality, credit rating), and market conditions (reinsurance market cycle indicators like Rate-on-Line indices, general credit market spreads like high-yield bond spreads) [[6](https://arxiv.org/html/2510.17221v1#bib.bib6), [32](https://arxiv.org/html/2510.17221v1#bib.bib32)]. More recent research uses machine learning (ML) techniques, such as gradient boost machines (e.g., XGBoost), random forests and geometric deep learning approach, to model ILS prices [[31](https://arxiv.org/html/2510.17221v1#bib.bib31), [25](https://arxiv.org/html/2510.17221v1#bib.bib25), [16](https://arxiv.org/html/2510.17221v1#bib.bib16), [21](https://arxiv.org/html/2510.17221v1#bib.bib21)]. ML models excel at capturing complex, non-linear dependencies and interaction effects among a large number of potential predictors without requiring pre-specified functional forms.

A crucial input for many pricing models is the statistical distribution of potential losses or the probability of trigger events. Research focuses on fitting appropriate probability distributions (e.g., generalised extreme value (GEV), generalized Pareto distribution (GPD), Burr, lognormal) to historical catastrophe loss data, often using extreme value theory [[40](https://arxiv.org/html/2510.17221v1#bib.bib40), [41](https://arxiv.org/html/2510.17221v1#bib.bib41), [55](https://arxiv.org/html/2510.17221v1#bib.bib55)]. For multi-peril or potentially dependent risks, copula functions are used to model the dependence structure between marginal loss distributions [[54](https://arxiv.org/html/2510.17221v1#bib.bib54), [51](https://arxiv.org/html/2510.17221v1#bib.bib51)]. These statistical analyses often need to account for data limitations like left-truncation (only losses above a certain threshold being recorded) [[23](https://arxiv.org/html/2510.17221v1#bib.bib23), [11](https://arxiv.org/html/2510.17221v1#bib.bib11)].

In ILS, event arrivals are typically modelled by counting processes: homogeneous (HPP) or non-homogeneous Poisson processes (NHPPs) for single-peril frequency (with seasonality captured via time-varying intensities), as in actuarial treatments of seasonal CAT bonds and flood-hedging CAT bonds that use NHPPs with trend and seasonality [[40](https://arxiv.org/html/2510.17221v1#bib.bib40), [10](https://arxiv.org/html/2510.17221v1#bib.bib10)]. To allow intensity to jump and decay after shocks, and to accommodate over-dispersion relative to Poisson, many pricing frameworks use Cox (doubly stochastic Poisson) models, often with shot-noise intensities; these are standard in catastrophe derivatives and CAT-bond pricing [[19](https://arxiv.org/html/2510.17221v1#bib.bib19)]. When exponential inter-arrival times are too restrictive, renewal processes provide a flexible alternative for inter-event timing and have been used directly in CAT-bond valuation [[8](https://arxiv.org/html/2510.17221v1#bib.bib8), [48](https://arxiv.org/html/2510.17221v1#bib.bib48)].
For perils with clustering—most notably earthquakes—self-exciting point processes such as Hawkes/ETAS better capture aftershock cascades and materially affect risk-based CAT-bond metrics [[43](https://arxiv.org/html/2510.17221v1#bib.bib43), [39](https://arxiv.org/html/2510.17221v1#bib.bib39)].
Finally, portfolio-level dependence across regions/perils is often handled with common-shock Poisson frameworks that correlate event counts while preserving marginal structures, a device widely adopted in insurance risk modelling and applicable to multi-peril ILS [[37](https://arxiv.org/html/2510.17221v1#bib.bib37)].

The potential impact of climate change adds another layer of complexity [[44](https://arxiv.org/html/2510.17221v1#bib.bib44)]. Climate change may alter the frequency, intensity and geographical distribution of weather-related risks such as hurricanes, floods, and wildfires, which may make historical data less relevant for predicting future risk [[50](https://arxiv.org/html/2510.17221v1#bib.bib50)].

Recently in the banking industry, ”contingent capita” instruments, such as contingent convertible (CoCo) bonds, have gained the support of various academics, practitioners, economists, regulators and banks as a potential avenue to reduce the need for bailouts of institutions that are classified as ‘too-big-to-fail’ [[22](https://arxiv.org/html/2510.17221v1#bib.bib22)]. Contingent capital instruments are a type of debt instrument with a loss-absorbing mechanism: that is, they are automatically converted into common equity or written down when a pre-specified trigger event occurs [[22](https://arxiv.org/html/2510.17221v1#bib.bib22)].

Given the success of contingent capital instruments, such as CoCo bonds, in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] the authors specified a special type of CoCo bond for insurers and reinsurers.
Such a CoCoCat bond can be seen as a special type of CoCo bond. CoCo bonds are characterised by two important features, namely the conversion trigger and the conversion mechanism.

In this paper, we consider a CoCoCat bond which is a contingent convertible bond that has a trigger linked to the occurrence of a single or sequence of predefined natural catastrophes in different regions, and a conversion mechanism whereby the bond either (i)
converts into common equity of the issuer (therefore increasing the size of common equity
in issue), at a predefined conversion rate as specified in the bond covenant, or (ii) is written
down (both principal and coupons) by a fixed percentage which is specified in the covenant. We construct a model that explicitly captures the intricate dependence patterns among regional catastrophe losses. Our analysis covers a range of scenarios, from fully independent events to proportionally dependent losses, considering both fixed and random loss magnitudes. By applying change-of-measure methods, we derive risk-neutral pricing formulas that reflect these various dependency structures.

The structure of the paper is as follows. Section [2](https://arxiv.org/html/2510.17221v1#S2 "2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds") introduces the concept of CoCoCat models applied across multiple regions, examining three distinct scenarios: fully independent loss processes, independent loss amounts, and proportional loss amounts under both fixed and random settings. In Section [3](https://arxiv.org/html/2510.17221v1#S3 "3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds"), we apply change-of-measure techniques to develop a valuation framework and derive risk-neutral pricing formulas tailored to these scenarios. The results are categorized into three groups based on the underlying assumptions about the loss mechanisms. Section [4](https://arxiv.org/html/2510.17221v1#S4 "4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") presents detailed proofs of the key results from Section [3](https://arxiv.org/html/2510.17221v1#S3 "3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds"). Section [5](https://arxiv.org/html/2510.17221v1#S5 "5. Further possible generalizations ‣ Design and valuation of multi-region CoCoCat bonds") discusses potential extensions of the model to accommodate claims from three or more regions. In Section [5](https://arxiv.org/html/2510.17221v1#S5 "5. Further possible generalizations ‣ Design and valuation of multi-region CoCoCat bonds"), we perform numerical analyses using the pricing formulas from Section [3](https://arxiv.org/html/2510.17221v1#S3 "3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds") to explore how CoCoCat bond prices respond to changes in model parameters. The catastrophe loss models are calibrated using data from Property Claims Services. The paper concludes in Section [7](https://arxiv.org/html/2510.17221v1#S7 "7. Conclusions ‣ Design and valuation of multi-region CoCoCat bonds") with a summary of the main findings.

## 2. Considered models

We lay here the groundwork for the valuation of multi-peril and multi-region CoCoCat bonds by detailing the mathematical frameworks employed.
The section begins by establishing fundamental assumptions.

### 2.1. Assumptions

Loosely following [[29](https://arxiv.org/html/2510.17221v1#bib.bib29)], we commence under the real-world probability measure. Under any probability measure, the price of the CAT bond depends on two emerging phenomena: financial market-related risk and catastrophe-related risk. Since the catastrophe-risk variables will give rise to jumps, we need to work in an incomplete markets setting and, moreover, note that complicated changes of measure could arise. To avoid this, we make the following assumption in line with much of the previous literature on pricing catastrophe-linked financial instruments. Evidence in support of this assumption has been found by [[28](https://arxiv.org/html/2510.17221v1#bib.bib28)] and [[18](https://arxiv.org/html/2510.17221v1#bib.bib18)], but is disputed by [[13](https://arxiv.org/html/2510.17221v1#bib.bib13)] and [[26](https://arxiv.org/html/2510.17221v1#bib.bib26)], see also the discussion in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)].

###### Assumption 2.1.

Catastrophe risk variables and financial market risk variables are independent in the real world.

We now continue our analysis by considering two financial-market-related processes. For the purposes of CAT bond pricing, we assume that on this space exists a riskless bank account based on an interest rate process, which we shall adopt as the numéraire asset later.

We also follow the incomplete market framework of [[42](https://arxiv.org/html/2510.17221v1#bib.bib42)]. Such a framework has been used extensively in the literature when valuing derivatives with payoffs linked to natural catastrophes; see, for example, [[1](https://arxiv.org/html/2510.17221v1#bib.bib1)], [[35](https://arxiv.org/html/2510.17221v1#bib.bib35)], [[52](https://arxiv.org/html/2510.17221v1#bib.bib52)], [[29](https://arxiv.org/html/2510.17221v1#bib.bib29)], [[36](https://arxiv.org/html/2510.17221v1#bib.bib36)], [[40](https://arxiv.org/html/2510.17221v1#bib.bib40)], [[45](https://arxiv.org/html/2510.17221v1#bib.bib45)], and [[15](https://arxiv.org/html/2510.17221v1#bib.bib15)]. On the basis of its pervasiveness in the literature to date, the following assumption is made in our work.

###### Assumption 2.2.

Investors are risk-neutral towards the jump risk posed by the natural catastrophe risk variables.

However, it must be borne in mind that recent empirical catastrophe bond pricing literature has shown that catastrophe bonds do not have a zero risk premium, see, for example, [[46](https://arxiv.org/html/2510.17221v1#bib.bib46)], [[6](https://arxiv.org/html/2510.17221v1#bib.bib6)] and [[24](https://arxiv.org/html/2510.17221v1#bib.bib24)]. This effect could also extend to other catastrophe-linked ILS instruments. Against this backdrop, it is possible to infer that pricing models based on the zero risk-premium assumption may give rise to values lower than those given by pricing models which assume a non-zero risk premium. In consequence, the usage of these pricing models may require additional margins added to the calculated value, or margins added to the parameters of the distributions associated with the jump process, all at the discretion of the issuer.

Despite this, we remain true to Assumption [2.2](https://arxiv.org/html/2510.17221v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2.1. Assumptions ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds") in our work for two reasons. First, it aligns with actuarial pricing techniques, which, as noted by [[5](https://arxiv.org/html/2510.17221v1#bib.bib5)], dominate in practice. Second, and more importantly, it can be adjusted to the range of underlying state variables in the model that are not investment assets and, therefore, not tradable. in the model. Hence, we can use real-world data to price, and this is useful given the scarcity of (and difficulty of obtaining) pricing data for many catastrophe-linked ILS.

In this paper, we consider three specialised cases of multi-region loss processes, which are crucial for subsequent pricing formulae. These models provide the foundation for understanding how catastrophic events in multiple regions and their financial implications are structured and analysed within the paper.
First, let us introduce a general 2D pricing framework.

### 2.2. General 2D pricing framework

The general construction builds on the 1D framework introduced in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]. The 2D framework describes both the financial market risk and the catastrophe risk variables. The former follow the classical Black-Scholes dynamics with appropriately selected stochastic interest rate process, while in the latter the two-dimensional aggregate loss process which can be modelled by various compound Poisson processes.

First, we establish some notation on the parameters of the CoCoCat bond, which covers the risk in two regions. Let:

* •

  T>0T>0 be the term of the CoCoCat bond;
* •

  Z>0Z>0 be the principal invested;
* •

  0<t1<t2<…<tN=T0<t\_{1}<t\_{2}<\ldots<t\_{N}=T be the coupon paying dates with constant yearly time period between the dates: Δ=ti−ti−1\Delta=t\_{i}-t\_{i-1} for i=2,3,…,Ni=2,3,\ldots,N;
* •

  c⩾0c\geqslant 0 be the constant spread (i.e. the catastrophe risk premium);
* •

  ζ∈[0,1]\zeta\in[0,1] be the conversion fraction;
* •

  D1,D2>0D\_{1},D\_{2}>0 be the threshold levels for the trigger corresponding to two selected regions;
* •

  KP>0K\_{P}>0 be the conversion price.

Moreover, let {St:t⩾0}\{S\_{t}:t\geqslant 0\} denote the share price process of the issuing firm. It is natural to express it
in terms of financial and catastrophic risk variables.
Following the idea of Assumption [2.1](https://arxiv.org/html/2510.17221v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. Assumptions ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds") we assume that it can be decomposed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=Stℱ​St𝒞,\displaystyle S\_{t}=S\_{t}^{\mathcal{F}}S\_{t}^{\mathcal{C}}, |  | (2.1) |

where {Stℱ:t⩾0}\{S\_{t}^{\mathcal{F}}:t\geqslant 0\} and {St𝒞:t⩾0}\{S\_{t}^{\mathcal{C}}:t\geqslant 0\} are two independent processes driven by financial market risk and catastrophic risk, respectively. Additionally, we set S0S\_{0} to be the price of the issuing firm at time t=0t=0.

The part of the model corresponding to the financial world is very similar to the 1D case in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]. We use the standard Black–Scholes dynamics and for the structure of interest rate {rt:t⩾0}\{r\_{t}:t\geqslant 0\} we select Longstaff’s model, namely under the real-word measure ℙ\mathbb{P}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​rt\displaystyle dr\_{t} | =θ^r​(m^r−rt)​d​t+σ^r​rt​d​W^t1,\displaystyle=\hat{\theta}\_{r}(\hat{m}\_{r}-\sqrt{r\_{t}})\,dt+\hat{\sigma}\_{r}\sqrt{r\_{t}}d\hat{W}\_{t}^{1}, |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Stℱ\displaystyle dS\_{t}^{\mathcal{F}} | =μS​Stℱ​d​t+σS​Stℱ​d​W^t2.\displaystyle=\mu\_{S}S\_{t}^{\mathcal{F}}dt+\sigma\_{S}S\_{t}^{\mathcal{F}}d\hat{W}\_{t}^{2}. |  | (2.3) |

The processes W^t1\hat{W}\_{t}^{1} and W^t2\hat{W}\_{t}^{2} are Brownian motions, which satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨W^t1,W^t2⟩=ρ​d​t\displaystyle d\langle\hat{W}\_{t}^{1},\hat{W}\_{t}^{2}\rangle=\rho\,dt |  | (2.4) |

for some ρ∈[−1,1]\rho\in[-1,1].
These assumptions imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Stℱ=S0​exp⁡(σS​W^t2+∫0t(ru−12​σS2)​𝑑u).\displaystyle S\_{t}^{\mathcal{F}}=S\_{0}\exp\left(\sigma\_{S}\hat{W}\_{t}^{2}+\int\_{0}^{t}(r\_{u}-\tfrac{1}{2}\sigma\_{S}^{2})du\right). |  | (2.5) |

Note that instead of Longstaff’s model, one can choose any interest rate model invariant to the Girsanov transformation with a constant kernel, such as Vasicek’s model or Hull-White’s model. Moreover, all of these three models admit a closed-form solution to the price of a zero-coupon bond paying 1 at maturity.

Now, we characterise the part of the model corresponding to the catastrophe-risk variables. We define

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞=exp⁡(−α​Lt1−β​Lt2+α​κ1​∫0tλu1​𝑑u+β​κ2​∫0tλu2​𝑑u),\displaystyle S\_{t}^{\mathcal{C}}=\exp\left(-\alpha L\_{t}^{1}-\beta L\_{t}^{2}+\alpha\kappa\_{1}\int\_{0}^{t}\lambda\_{u}^{1}\,du+\beta\kappa\_{2}\int\_{0}^{t}\lambda\_{u}^{2}\,du\right), |  | (2.6) |

where α,β,κ1,κ2>0\alpha,\beta,\kappa\_{1},\kappa\_{2}>0 and Lt1L\_{t}^{1}, Lt2L\_{t}^{2} denote the aggregate loss processes given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt1=∑k=1Nt1Xk1,\displaystyle L\_{t}^{1}=\sum\_{k=1}^{N\_{t}^{1}}X\_{k}^{1}, | Lt2=∑k=1Nt2Xk2.\displaystyle L\_{t}^{2}=\sum\_{k=1}^{N\_{t}^{2}}X\_{k}^{2}. |  |

Here, Nt1N\_{t}^{1} and Nt2N\_{t}^{2} are non-homogeneous Poisson processes with cumulative deterministic intensities

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λt1=∫0tλu1​𝑑u,\displaystyle\Lambda\_{t}^{1}=\int\_{0}^{t}\lambda\_{u}^{1}\,du, | Λt2=∫0tλu2​𝑑u,\displaystyle\Lambda\_{t}^{2}=\int\_{0}^{t}\lambda\_{u}^{2}\,du, |  |

respectively, for some non-negative intensity functions λu1\lambda\_{u}^{1} and λu2\lambda\_{u}^{2}.

The loss amounts described by non-negative continuous random variables X11,X21,X31​…X\_{1}^{1},X\_{2}^{1},X\_{3}^{1}\ldots and X12,X22,X32,…X\_{1}^{2},X\_{2}^{2},X\_{3}^{2},\ldots are pairwise independent and identically distributed with distribution functions FX1F\_{X}^{1}, FX2F\_{X}^{2} and densities fX1f\_{X}^{1}, fX2f\_{X}^{2}, respectively. By pairwise independent, we mean here that for any i=1,2i=1,2 and k,l∈ℕk,l\in\mathbb{N}, k≠lk\neq l random variables XkiX\_{k}^{i} and XjiX\_{j}^{i} are independent. In particular, note that this definition allows for the dependency of variables Xk1X\_{k}^{1} and Xl2X\_{l}^{2} for some k,l∈ℕk,l\in\mathbb{N}. This is a natural assumption regarding the fact that these variables are identified with loss amounts in two different regions.

The aggregate loss processes Lt1L\_{t}^{1} and Lt2L\_{t}^{2} correspond to the behaviour of CoCoCat bond’s iith underlying index. The constants α,β\alpha,\beta represent the effect of catastrophic losses on the logarithm of the share price. The coefficients κ1\kappa\_{1} and κ2\kappa\_{2} correspond to Poisson processes Nt1N\_{t}^{1} and Nt2N\_{t}^{2}, respectively. Specifically, if Nt1N\_{t}^{1} and Nt2N\_{t}^{2} are the same process, which we will denote by NtN\_{t}, then κ1=κ2\kappa\_{1}=\kappa\_{2} and we denote this common value as κ\kappa.

We consider three special cases of the aggregate loss process and, for these cases, we will provide appropriate pricing formulae. We now give precise mathematical assumptions for these cases and provide their interpretation.

### 2.3. Independent loss processes (ILP)

Suppose that we observe losses from two different regions with two different frequencies. Mathematically speaking, we assume that the variables Nt1,Nt2N\_{t}^{1},N\_{t}^{2}, Xk1,Xk2X\_{k}^{1},X\_{k}^{2} are (pairwise) independent for any k∈ℕk\in\mathbb{N}. Clearly, the aggregated loss processes Lt1L\_{t}^{1} and Lt2L\_{t}^{2} are also independent. Therefore, we can rewrite ([2.1](https://arxiv.org/html/2510.17221v1#S2.E1 "In 2.2. General 2D pricing framework ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞=St𝒞,1​St𝒞,2,\displaystyle S\_{t}^{\mathcal{C}}=S\_{t}^{\mathcal{C},1}S\_{t}^{\mathcal{C},2}, |  | (2.7) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞,1=exp⁡(−α​∑k=1Nt1Xk1+α​κ1​∫0tλu1​𝑑u),\displaystyle S\_{t}^{\mathcal{C},1}=\exp\left(-\alpha\sum\_{k=1}^{N\_{t}^{1}}X\_{k}^{1}+\alpha\kappa\_{1}\int\_{0}^{t}\lambda\_{u}^{1}\,du\right), | St𝒞,2=exp⁡(−β​∑k=1Nt2Xk2+β​κ2​∫0tλu2​𝑑u).\displaystyle S\_{t}^{\mathcal{C},2}=\exp\left(-\beta\sum\_{k=1}^{N\_{t}^{2}}X\_{k}^{2}+\beta\kappa\_{2}\int\_{0}^{t}\lambda\_{u}^{2}\,du\right). |  |

Note that St𝒞,1\smash{S\_{t}^{\mathcal{C},1}} and St𝒞,2\smash{S\_{t}^{\mathcal{C},2}} are independent single-region processes for the 1D model (see equation (7) in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]). Formula ([2.7](https://arxiv.org/html/2510.17221v1#S2.E7 "In 2.3. Independent loss processes (ILP) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")) provides a very convenient way to represent the catastrophic share price process, allowing the use of 1D methods.

Another way of thinking about the ILP assumption is to treat the two distinct regions as one and simply reduce the problem to the 1D case. One can define the merged aggregate loss process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=αα+β​Lt1+βα+β​Lt2.\displaystyle L\_{t}=\frac{\alpha}{\alpha+\beta}L\_{t}^{1}+\frac{\beta}{\alpha+\beta}L\_{t}^{2}. |  | (2.8) |

It is easy to see that LtL\_{t} is a compound Poisson process itself. Its frequency component reads Nt1+Nt2N\_{t}^{1}+N\_{t}^{2} with time-dependent cumulative intensity Λt=Λt1+Λt2\Lambda\_{t}=\Lambda\_{t}^{1}+\Lambda\_{t}^{2}. Moreover, LtL\_{t} has random loss amounts X1,X2,X3,…X\_{1},X\_{2},X\_{3},\ldots which are i.i.d. random variables following the mixture of distributions FX1F\_{X}^{1} and FX2F\_{X}^{2}. However, it should be noted that, in general, the distribution of XkX\_{k} may be time-dependent, unlike the distributions of Xk1X\_{k}^{1} and Xk2X\_{k}^{2}. This problem does not arise when Nt1N\_{t}^{1} and Nt2N\_{t}^{2} are homogeneous Poisson processes.

In this notation, equation ([2.6](https://arxiv.org/html/2510.17221v1#S2.E6 "In 2.2. General 2D pricing framework ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞\displaystyle S\_{t}^{\mathcal{C}} | =exp⁡(−(α+β)​Lt+α​κ1​∫0tλs1​𝑑s+β​κ2​∫0tλs2​𝑑s).\displaystyle=\exp\left(-(\alpha+\beta)L\_{t}+\alpha\kappa\_{1}\int\_{0}^{t}\lambda\_{s}^{1}\,ds+\beta\kappa\_{2}\int\_{0}^{t}\lambda\_{s}^{2}\,ds\right). |  |

Although this way of seeing the ILP assumption can seem very natural, it will not be very helpful in pricing, mainly because of non-matching integral components. However, it can be considered an inspiration to use this trick for the two remaining cases.

### 2.4. Independent loss amounts (ILA)

Suppose that losses from two distinct regions occur at the same time. It means that the loss amount variables Xk1X\_{k}^{1} and Xk2X\_{k}^{2} are independent in the sense that for any k,l∈ℕk,l\in\mathbb{N}, i,j=1,2i,j=1,2 such that (i,k)≠(j,l)(i,k)\neq(j,l) variables XkiX\_{k}^{i} and XljX\_{l}^{j} are independent. Moreover, the processes Nt1N\_{t}^{1} and Nt2N\_{t}^{2} are the same, so we denote both as NtN\_{t}. The cumulative intensity of NtN\_{t} is denoted as Λt\Lambda\_{t}.

We can again define the aggregate loss process merged in the same vein as in ([2.8](https://arxiv.org/html/2510.17221v1#S2.E8 "In 2.3. Independent loss processes (ILP) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")), but since for ILA loss frequency is the same, it simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=αα+β​Lt1+βα+β​Lt2=∑k=1Nt(αα+β​Xk1+βα+β​Xk2).\displaystyle L\_{t}=\frac{\alpha}{\alpha+\beta}L\_{t}^{1}+\frac{\beta}{\alpha+\beta}L\_{t}^{2}=\sum\_{k=1}^{N\_{t}}\left(\frac{\alpha}{\alpha+\beta}X\_{k}^{1}+\frac{\beta}{\alpha+\beta}X\_{k}^{2}\right). |  | (2.9) |

One can easily identify the distribution of the summands XkX\_{k}, as they are the sums of two independent random variables.

Since under the ILA assumption the losses occur simultaneously, we have κ1=κ2=κ\kappa\_{1}=\kappa\_{2}=\kappa. Equation (​[2.6](https://arxiv.org/html/2510.17221v1#S2.E6 "In 2.2. General 2D pricing framework ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")​)\eqref{stc-formula} can be rewritten again in terms of the merged aggregate loss process LtL\_{t} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞\displaystyle S\_{t}^{\mathcal{C}} | =exp⁡(−(α+β)​Lt+κ​(α+β)​∫0tλs​𝑑s).\displaystyle=\exp\left(-(\alpha+\beta)L\_{t}+\kappa(\alpha+\beta)\int\_{0}^{t}\lambda\_{s}\,ds\right). |  |

Thus, it can be seen that in this approach, the process St𝒞S\_{t}^{\mathcal{C}} can be reduced to its single-region analogue.

### 2.5. Proportional loss amounts (PLA)

Now, let us consider a case where not only the losses occur at the same time but the losses XkX\_{k} themselves are split proportionally among the regions. Similarly to the ILA assumption, we denote the common counting Poisson process by NtN\_{t} and its cumulative intensity by Λt\Lambda\_{t}. We consider two types of proportional splits of losses:

1. (a)

   Constant proportional loss amounts (cPLA): for fixed and deterministic proportion coefficient p∈(0,1)p\in(0,1), the loss amounts satisfy:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Xk1=p​Xk,\displaystyle X\_{k}^{1}=pX\_{k}, | Xk2=(1−p)​Xk,\displaystyle X\_{k}^{2}=(1-p)X\_{k}, |  |

   where XkX\_{k} is a sequence of i.i.d. random variables with distribution function FXF\_{X} and density fXf\_{X}.
2. (b)

   Random proportional loss amounts (rPLA): for random proportion coefficient P∈(0,1)P\in(0,1), loss amounts satisfy:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Xk1=P​Xk,\displaystyle X\_{k}^{1}=PX\_{k}, | Xk2=(1−P)​Xk.\displaystyle X\_{k}^{2}=(1-P)X\_{k}. |  |

   We additionally assume that PP is independent of XkX\_{k} and PP and has a distribution function FPF\_{P}.

Note that for the rPLA case we do not assume that PP is a continuous random variable. This allows us to recover the cPLA case simply by defining P=pP=p with probability 1 for p∈(0,1)p\in(0,1). For that reason, throughout the rest of the paper we mainly focus on the more general case (random PP).

For PLA, it is more convenient to slightly modify the previous definition of the merged aggregate loss process and define it as

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​Lt1+β​Lt2=(α​P+β​(1−P))​∑k=1NtXk=Q​Lt,\displaystyle\alpha L\_{t}^{1}+\beta L\_{t}^{2}=(\alpha P+\beta(1-P))\sum\_{k=1}^{N\_{t}}X\_{k}=QL\_{t}, |  | (2.10) |

where Q=α​P+β​(1−P)Q=\alpha P+\beta(1-P) and Lt=∑k=1NtXkL\_{t}=\sum\_{k=1}^{N\_{t}}X\_{k}. Here, LtL\_{t} refers to the standard aggregate loss process. Therefore, the catastrophic share price process can be written as

|  |  |  |
| --- | --- | --- |
|  | St𝒞=exp⁡(−Q​Lt+κ​(α+β)​∫0tλu​𝑑u).\displaystyle S\_{t}^{\mathcal{C}}=\exp\left(-QL\_{t}+\kappa(\alpha+\beta)\int\_{0}^{t}\lambda\_{u}\,du\right). |  |

Note that for certain special cases, some simplifications are possible. For α=β\alpha=\beta we have Q=αQ=\alpha and hence St𝒞S\_{t}^{\mathcal{C}} reduces to the single-region case, with loss amounts given by α​Xk\alpha X\_{k} and effect of losses (α+β\alpha+\beta) equal to 2​α2\alpha. Another example is when P=12P=\frac{1}{2} with probability 1 (or p=1/2p=1/2). Then we obtain another single-region process with the losses (α+β)​Xk/2(\alpha+\beta)X\_{k}/2 and effect of losses α+β\alpha+\beta.

Another possible assumption to study would be a further generalisation of the rPLA case and considering floating proportional coefficients PkP\_{k}, for which the losses would be Xk1=Pk​XkX\_{k}^{1}=P\_{k}X\_{k} and Xk2=(1−Pk)​XkX\_{k}^{2}=(1-P\_{k})X\_{k}. Despite its realistic nature, this assumption poses many difficulties, such as finding the distribution of the trigger time. However, it opens the door to further development of multi-region framework.

## 3. Risk-neutral pricing: analytic formulae

Under the risk-neutral measure ℚ\mathbb{Q} the catastrophe-risk and financial market risk variables are captured by the following system
of equations.

###### Proposition 3.1.

The multi-region model is defined by the following system of equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​rt\displaystyle dr\_{t} | =θr​(mr−rt)​d​t+σr​rt​d​Wt1,\displaystyle=\theta\_{r}(m\_{r}-\sqrt{r\_{t}})\,dt+\sigma\_{r}\sqrt{r\_{t}}dW\_{t}^{1}, |  | (3.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =Stℱ​St𝒞,\displaystyle=S\_{t}^{\mathcal{F}}S\_{t}^{\mathcal{C}}, |  | (3.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | St𝒞\displaystyle S\_{t}^{\mathcal{C}} | =exp⁡(−α​Lt1−β​Lt2+α​κ1​∫0tλu1​𝑑u+β​κ2​∫0tλu2​𝑑u),\displaystyle=\exp\left(-\alpha L\_{t}^{1}-\beta L\_{t}^{2}+\alpha\kappa\_{1}\int\_{0}^{t}\lambda\_{u}^{1}\,du+\beta\kappa\_{2}\int\_{0}^{t}\lambda\_{u}^{2}\,du\right), |  | (3.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Stℱ\displaystyle dS\_{t}^{\mathcal{F}} | =μS​Stℱ​d​t+σS​Stℱ​d​Wt2,\displaystyle=\mu\_{S}S\_{t}^{\mathcal{F}}dt+\sigma\_{S}S\_{t}^{\mathcal{F}}dW\_{t}^{2}, |  | (3.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​⟨Wt1,Wt2⟩\displaystyle d\langle W\_{t}^{1},W\_{t}^{2}\rangle | =ρ​d​t,\displaystyle=\rho dt, |  | (3.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Lt1,Lt2)\displaystyle(L\_{t}^{1},L\_{t}^{2}) | =(∑k=1Nt1Xk1,∑k=1Nt2Xk2,)\displaystyle=\left(\sum\_{k=1}^{N\_{t}^{1}}X\_{k}^{1},\,\sum\_{k=1}^{N\_{t}^{2}}X\_{k}^{2},\right) |  | (3.6) |

where θr\theta\_{r} and mrm\_{r} are the risk-neutral parameters for the interest rate process and
W~t1\tilde{W}^{1}\_{t} and W~t2\tilde{W}^{2}\_{t} are two Brownian motions under the measure ℚF\mathbb{Q}\_{F} as specified in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)].

We now go into the details of pricing.

### 3.1. CoCoCat bond’s mechanism. General pricing formula

Before we present the main results of the paper, we specify some additional notation. Let R​(t,ti−1,ti)R(t,t\_{i-1},t\_{i}) be the forward risk-free (like LIBOR) rate at time tt for the interval [ti−1,ti][t\_{i-1},t\_{i}]. Since Δ=ti−ti−1\Delta=t\_{i}-t\_{i-1} is constant, the risk-free process R​(t,t,t+Δ)R(t,t,t+\Delta) at time tt is denoted as {Rt:t⩾0}\{R\_{t}:t\geqslant 0\}. We also define the discounted riskless bank account associated with the process {rt:t⩾0}\{r\_{t}:t\geqslant 0\} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(0,t)=exp⁡(−∫0trs​𝑑s).\displaystyle B(0,t)=\exp\left(-\int\_{0}^{t}r\_{s}\,ds\right). |  | (3.7) |

Hence, risk-neutral price at time tt of a zero-coupon bond paying one unit at maturity TT (T>tT>t) can be calculated as the conditional expectation given by 𝔼ℚ​[B​(0,T)|ℱt]\mathbb{E}^{\mathbb{Q}}[B(0,T)|\mathcal{F}\_{t}] for t∈[0,T]t\in[0,T]. However, in pricing, we will focus on t=0t=0. Note that in this case, the above expectation is no longer conditional since r0r\_{0} is deterministic. We denote the price of a zero-coupon unit bond with maturity TT as

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(r0,T,θr,mr,σr)=𝔼ℚ​B​(0,T)\displaystyle P(r\_{0},T,\theta\_{r},m\_{r},\sigma\_{r})=\mathbb{E}^{\mathbb{Q}}B(0,T) |  | (3.8) |

when the interest rate rtr\_{t} is given by the model ([3.1](https://arxiv.org/html/2510.17221v1#S3.E1 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) with parameters θr,mr,σr\theta\_{r},\,m\_{r},\,\sigma\_{r} and initial value r0r\_{0}. The analytical formulae for ([3.8](https://arxiv.org/html/2510.17221v1#S3.E8 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) are well-known in the literature. These famous results are recalled below.

###### Proposition 3.2.

If rtr\_{t} follows Longstaff’s model, we have

|  |  |  |
| --- | --- | --- |
|  | P​(r0,T,θr,mr,σr)=A​(T)​exp⁡(r0​B​(T)+r0​C​(T)),\displaystyle P(r\_{0},T,\theta\_{r},m\_{r},\sigma\_{r})=A(T)\exp(r\_{0}B(T)+\sqrt{r\_{0}}C(T)), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(T)\displaystyle A(T) | =(21+eψ​T)1/2​exp⁡(c1+c2​T+c31+eψ​T),\displaystyle=\left(\frac{2}{1+e^{\psi T}}\right)^{1/2}\exp\left(c\_{1}+c\_{2}T+\frac{c\_{3}}{1+e^{\psi T}}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(T)\displaystyle B(T) | =−ψσr2+2​ψσr2​(1+eψ​T),\displaystyle=-\frac{\psi}{\sigma\_{r}^{2}}+\frac{2\psi}{\sigma\_{r}^{2}(1+e^{\psi T})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(T)\displaystyle C(T) | =2​θr​(1−eψ​T/2)σr2​(1+eψ​T)\displaystyle=\frac{2\theta\_{r}(1-e^{\psi T/2})}{\sigma\_{r}^{2}(1+e^{\psi T})} |  |

and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ψ=2​σr,\displaystyle\psi=\sqrt{2}\sigma\_{r}, | c1=θr2ψ​σr2,\displaystyle c\_{1}=\frac{\theta\_{r}^{2}}{\psi\sigma\_{r}^{2}}, | c2=ψ4−θr2ψ2,\displaystyle c\_{2}=\frac{\psi}{4}-\frac{\theta\_{r}^{2}}{\psi^{2}}, | c3=−4​θr2ψ3.\displaystyle c\_{3}=-\frac{4\theta\_{r}^{2}}{\psi^{3}}. |  |

Let us recall the general CoCoCat bond mechanism. With the principal KK invested in the bond, the coupons with rate c+LIBORc+\operatorname{LIBOR} are paid at times t1<t2<…<tN=Tt\_{1}<t\_{2}<\ldots<t\_{N}=T until the maturity date TT or upon the occurrence of a trigger, whichever happens first. If the trigger does not occur before maturity, all the money is returned to the investor. Otherwise, immediately upon the time of trigger, the conversion mechanism is activated and ζ​K\zeta K is converted to common equity.

This construction is very similar to the 1D case presented in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]. The major difference is that in our case two catastrophic indices are considered and the trigger is activated when L1⩾D1L\_{1}\geqslant D\_{1} or L2⩾D2L\_{2}\geqslant D\_{2}. In other words, we define the trigger time as

|  |  |  |
| --- | --- | --- |
|  | τ=min⁡{τ1,τ2},\displaystyle\tau=\min\{\tau\_{1},\tau\_{2}\}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ1=inf{t⩾0:Lt1⩾D1},\displaystyle\tau\_{1}=\inf\{t\geqslant 0:L\_{t}^{1}\geqslant D\_{1}\}, | τ2=inf{t⩾0:Lt2⩾D2}\displaystyle\tau\_{2}=\inf\{t\geqslant 0:L\_{t}^{2}\geqslant D\_{2}\} |  |

are the times the aggregate loss processes LtiL\_{t}^{i} first exceed the values DiD\_{i} for i=1,2i=1,2. This definition of trigger time, despite being very natural, constitutes the main difficulty in valuation multi-region CoCoCat bonds, even though the catastrophic stock price process can often be reduced to a single-region case, as shown in previous sections.

By the mechanism of the CoCoCat bond, the following general pricing formula holds.

###### Lemma 3.3.

The issue-date risk-neutral price of a multi-region CoCoCat bond is

|  |  |  |
| --- | --- | --- |
|  | V0=𝔼ℚ​[I1+I2+I3],\displaystyle V\_{0}=\mathbb{E}^{\mathbb{Q}}[I\_{1}+I\_{2}+I\_{3}], |  |

where ℚ\mathbb{Q} is the risk-neutral measure and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I1=∑i=1N(Rti−1+c)​Δ​Z​𝟙τ>ti​B​(0,ti),\displaystyle I\_{1}=\sum\_{i=1}^{N}(R\_{t\_{i-1}}+c)\Delta Z\mathbb{1}\_{\tau>t\_{i}}B(0,t\_{i}), | I2=ζ​ZKP​Sτ​𝟙τ⩽T​B​(0,τ),\displaystyle I\_{2}=\frac{\zeta Z}{K\_{P}}S\_{\tau}\mathbb{1}\_{\tau\leqslant T}B(0,\tau), | I3=Z​𝟙τ>T​B​(0,T).\displaystyle I\_{3}=Z\mathbb{1}\_{\tau>T}B(0,T). |  |

In this paper, we consider exponential conversion functions, that is KP=SτνK\_{P}=S\_{\tau}^{\nu}, where ν∈[0,1]\nu\in[0,1]. In particular, if ν=0\nu=0, then the conversion amount does not depend on the share price at the trigger moment, as it is constant. On the other hand, if ν=1\nu=1, the conversion amount is equal to the share price at the trigger moment and I2I\_{2} simplifies significantly.

Given the appropriate martingale measure ℚ\mathbb{Q}, the above expectations can be calculated by repeating the reasoning presented in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] (see Sections 4.1-4.3 therein). For random variables I1,I3I\_{1},I\_{3}, results are similar to those from the 1D case, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​I1=Z​Δ​(R0+c)​P​(r0,t1,θr,mr,σr)​ℚ​(τ>t1)+Z​∑i=2Nℚ​(τ>ti)​(P​(r0,ti−1,θr,mr,σr)+(1−c​Δ)​P​(r0,ti,θr,mr,σr))\displaystyle\begin{aligned} \mathbb{E}I\_{1}&=Z\Delta(R\_{0}+c)P(r\_{0},t\_{1},\theta\_{r},m\_{r},\sigma\_{r})\mathbb{Q}(\tau>t\_{1})\\ &+Z\sum\_{i=2}^{N}\mathbb{Q}(\tau>t\_{i})(P(r\_{0},t\_{i-1},\theta\_{r},m\_{r},\sigma\_{r})+(1-c\Delta)P(r\_{0},t\_{i},\theta\_{r},m\_{r},\sigma\_{r}))\end{aligned} |  | (3.9) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​I3=Z​P​(r0,T,θr,mr,σr)​ℚ​(τ>T).\displaystyle\mathbb{E}I\_{3}=ZP(r\_{0},T,\theta\_{r},m\_{r},\sigma\_{r})\mathbb{Q}(\tau>T). |  | (3.10) |

The only difference in the above formulas with respect to the 1D case is the distribution of τ\tau which we will study separately for each model.

Evaluation of the remaining expectation, 𝔼ℚ​I2\mathbb{E}^{\mathbb{Q}}I\_{2}, requires more advanced tools leading to more complicated analytical formulas but still easy to use. This will be exploited now in detail.

### 3.2. Main results

In this section we present the main results, namely the analytic formulae for risk-neutral price of multi-region CoCoCat bonds. We split the results into three groups, based on the assumptions on the loss process (ILP, ILA, PLA).

For any appropriate function f:(0,∞)→ℝf:(0,\infty)\to\mathbb{R}, we denote its Laplace transform by

|  |  |  |
| --- | --- | --- |
|  | (ℒ​f)​(z)=∫0∞e−x​z​f​(x)​𝑑x.\displaystyle(\mathcal{L}f)(z)=\int\_{0}^{\infty}e^{-xz}f(x)\,dx. |  |

The nnth convolution power of the function ff is denoted by fn⁣∗f^{n\*} for n=1,2,3​…n=1,2,3\ldots For convenience, we assume that f0⁣∗f^{0\*} is identically equal to one.

###### Theorem 3.4.

Risk-neutral price of CoCoCat bond is equal to

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​I1+𝔼ℚ​I2+𝔼ℚ​I3.\displaystyle\mathbb{E}^{\mathbb{Q}}I\_{1}+\mathbb{E}^{\mathbb{Q}}I\_{2}+\mathbb{E}^{\mathbb{Q}}I\_{3}. |  |

Here 𝔼ℚ​I1\mathbb{E}^{\mathbb{Q}}I\_{1} is given by ([3.9](https://arxiv.org/html/2510.17221v1#S3.E9 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")), 𝔼ℚ​I3\mathbb{E}^{\mathbb{Q}}I\_{3} is given by ([3.10](https://arxiv.org/html/2510.17221v1#S3.E10 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) and

1. (a)

   for ILP,

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼ℚ​I2=ξ​Z​S01−ν​∫0Texp⁡(−12​ν​(1−ν)2​σS2​t)​Φ​(t)​P​(r0,t,θ¯r,m¯r,σ¯r)​Fτν​(d​t),\displaystyle\mathbb{E}^{\mathbb{Q}}I\_{2}=\xi ZS\_{0}^{1-\nu}\int\_{0}^{T}\exp\left(-\tfrac{1}{2}\nu(1-\nu)^{2}\sigma\_{S}^{2}t\right)\Phi(t)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})\,F\_{\tau}^{\nu}(dt), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Φ​(t)\displaystyle\Phi(t) | =exp(−Λt1(1−(ℒfX1)(α(1−ν))−Λt2(1−(ℒfX2)(β(1−ν))\displaystyle=\exp\bigg{(}-\Lambda\_{t}^{1}(1-(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))-\Lambda\_{t}^{2}(1-(\mathscr{L}f\_{X}^{2})(\beta(1-\nu)) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +(1−ν)(Λt1(1−(ℒfX1)(α))+Λt2(1−(ℒfX2)(β))))\displaystyle+(1-\nu)\left(\Lambda\_{t}^{1}(1-(\mathcal{L}f\_{X}^{1})(\alpha))+\Lambda\_{t}^{2}(1-(\mathcal{L}f\_{X}^{2})(\beta))\right)\bigg{)} |  |

   and FτνF\_{\tau}^{\nu} is described by Proposition [4.2](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") with parameters Λtν,1\Lambda\_{t}^{\nu,1}, Λtν,2\Lambda\_{t}^{\nu,2}, FXν,1F\_{X}^{\nu,1}, FXν,2F\_{X}^{\nu,2} described by Proposition [4.3](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds");
2. (b)

   for ILA,

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼ℚ​I2=ξ​Z​S01−ν​∫0Texp⁡(−12​ν​(1−ν)2​σS2​t)​Φ​(t)​P​(r0,t,θ¯r,m¯r,σ¯r)​Fτν​(d​t),\displaystyle\mathbb{E}^{\mathbb{Q}}I\_{2}=\xi ZS\_{0}^{1-\nu}\int\_{0}^{T}\exp\left(-\tfrac{1}{2}\nu(1-\nu)^{2}\sigma\_{S}^{2}t\right)\Phi(t)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})\,F\_{\tau}^{\nu}(dt), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Φ​(t)\displaystyle\Phi(t) | =exp(−Λt(1−(ℒfX1)(α(1−ν))(ℒfX2)(β(1−ν)))\displaystyle=\exp\bigg{(}-\Lambda\_{t}(1-(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +(1−ν)Λt(1−(ℒfX1)(α)(ℒfX2)(β)))\displaystyle+(1-\nu)\Lambda\_{t}(1-(\mathscr{L}f\_{X}^{1})(\alpha)(\mathscr{L}f\_{X}^{2})(\beta))\bigg{)} |  |

   and FτνF\_{\tau}^{\nu} is described by Proposition [4.5](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") with parameters Λtν\Lambda\_{t}^{\nu}, FXν,1F\_{X}^{\nu,1}, FXν,2F\_{X}^{\nu,2} described by Proposition [4.6](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem6 "Proposition 4.6. ‣ 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds");
3. (c)

   for PLA,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼ℚ​I2\displaystyle\mathbb{E}^{\mathbb{Q}}I\_{2} | =ξZS01−ν∫01(∫0Texp(−12ν(1−ν)2σS2t)Φ(t,p)\displaystyle=\xi ZS\_{0}^{1-\nu}\int\_{0}^{1}\bigg{(}\int\_{0}^{T}\exp\left(-\tfrac{1}{2}\nu(1-\nu)^{2}\sigma\_{S}^{2}t\right)\Phi(t,p) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ×P(r0,t,θ¯r,m¯r,σ¯r)Fτν|p(dt))FP(dp),\displaystyle\times P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})\,F\_{\tau}^{\nu|p}(dt)\bigg{)}F\_{P}(dp), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Φ​(t,p)\displaystyle\Phi(t,p) | =exp(−Λt(1−(ℒfX)((1−ν)(αp+β(1−p)))\displaystyle=\exp\bigg{(}-\Lambda\_{t}(1-(\mathcal{L}f\_{X})((1-\nu)(\alpha p+\beta(1-p))) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +(1−ν)Λt(1−𝔼ℙC[(ℒfX)(αP+β(1−P))])).\displaystyle+(1-\nu)\Lambda\_{t}\left(1-\mathbb{E}^{\mathbb{P}\_{C}}\left[(\mathcal{L}f\_{X})(\alpha P+\beta(1-P))\right]\right)\bigg{)}. |  |

   and

   |  |  |  |
   | --- | --- | --- |
   |  | Fτν|p​(t)=1−∑n=0∞(Λtν)nn!​exp⁡(−Λtν)​(FXν)n⁣∗​(Dp),\displaystyle F\_{\tau}^{\nu|p}(t)=1-\sum\_{n=0}^{\infty}\frac{(\Lambda\_{t}^{\nu})^{n}}{n!}\exp(-\Lambda\_{t}^{\nu})(F\_{X}^{\nu})^{n\*}(D\_{p}), |  |

   where Dp=min⁡{D1/p,D2/(1−p)}D\_{p}=\min\{D\_{1}/p,D\_{2}/(1-p)\} and Λtν\Lambda\_{t}^{\nu}, FXνF\_{X}^{\nu} are described by Proposition [4.9](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem9 "Proposition 4.9. ‣ 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds").

Furthermore, in all three cases we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θ¯r=ν​(θr−σr​σS​ρ​(1−ν)),\displaystyle\bar{\theta}\_{r}=\sqrt{\nu}(\theta\_{r}-\sigma\_{r}\sigma\_{S}\rho(1-\nu)), | m¯r=ν​mr​θr/θ¯r,\displaystyle\bar{m}\_{r}=\nu m\_{r}\theta\_{r}/\bar{\theta}\_{r}, | σ¯r=ν​σr.\displaystyle\bar{\sigma}\_{r}=\sqrt{\nu}\sigma\_{r}. |  |

## 4. Risk-neutral pricing: proofs

In order to price multi-region CoCoCat bonds, we redevelop methods introduced in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] for the single-region model. We provide three proofs, each for different assumptions on the loss processes: ILP, ILA, PLA, described in Sections [2.3](https://arxiv.org/html/2510.17221v1#S2.SS3 "2.3. Independent loss processes (ILP) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds"), [2.4](https://arxiv.org/html/2510.17221v1#S2.SS4 "2.4. Independent loss amounts (ILA) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds"), [2.5](https://arxiv.org/html/2510.17221v1#S2.SS5 "2.5. Proportional loss amounts (PLA) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds"), respectively.

We first notice that the model’s equations ([3.1](https://arxiv.org/html/2510.17221v1#S3.E1 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")), ([3.4](https://arxiv.org/html/2510.17221v1#S3.E4 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")), ([3.5](https://arxiv.org/html/2510.17221v1#S3.E5 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) and (20), (24), (25) in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] are exactly the same. In other words, in the 2D case we do not change the part of the model corresponding to the financial world. Thus, we will omit these parts in the proof which are identical to the one-dimensional one. Our main goal is to evaluate the expected value 𝔼​I2\mathbb{E}I\_{2} described in Lemma [3.3](https://arxiv.org/html/2510.17221v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds").

We divide the present section into three subsections. Although all three proofs may seem similar, their differences lie primarily in the complexity of the loss models. The first model is the simplest, while the last one is the most complex, requiring the use of more advanced methods for valuation. However, all three proofs share common procedural steps, which we describe below.

Step 1. Finding a risk-neutral measure ℚ\mathbb{Q}. This step can be considered as an equivalent of Theorem 3 in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]. As mentioned before, the assumptions regarding the financial word in the 1D and 2D cases are the same, so we only focus on finding the value of κ\kappa (or κ1\kappa\_{1} and κ2\kappa\_{2} for the independent loss processes) such that St𝒞S\_{t}^{\mathcal{C}} is a martingale.

Step 2. Finding the distribution of the trigger time τ\tau with respect to ℚ\mathbb{Q}. Recall that the trigger time τ\tau is the first moment at which at least one of the events {L1⩾D1}\{L\_{1}\geqslant D\_{1}\} or {L2⩾D2}\{L\_{2}\geqslant D\_{2}\} occurs. Clearly, the distribution of τ\tau depends on the distributions of Lt1L\_{t}^{1} and Lt2L\_{t}^{2}, but sometimes it depends solely on the distribution of a certain linear combination of the processes Lt1L\_{t}^{1} and Lt2L\_{t}^{2}. Identifying such processes, which we call τ\tau-dependencies, is crucial in the next steps.

Step 3. Defining a new measure ℙν\mathbb{P}^{\nu} using the Radon–Nikodym derivative. The most challenging aspect of evaluating 𝔼ℚ​I2\mathbb{E}^{\mathbb{Q}}I\_{2} is that the process I2I\_{2} is a certain function of Lτ1L\_{\tau}^{1} and Lτ2L\_{\tau}^{2}, multiplied by the indicator of an event {τ⩽T}\{\tau\leqslant T\}, and at the same time τ\tau depends on loss processes. In order to overcome this problem and simply reduce the terms Lτ1L\_{\tau}^{1} and Lτ2L\_{\tau}^{2} from the expectation, we introduce a new measure.

Step 4. Identifying the distribution of τ\tau-dependencies with respect to ℙν\mathbb{P}^{\nu}. Since the τ\tau-dependencies found in Step 2 are always compound Poisson processes, the aim of this step is to prove that after change of measure, the τ\tau-dependencies preserve the type of distribution; that is, they are still compound Poisson processes but with different parameters. So we can easily identify the distribution of τ\tau with respect to ℙν\mathbb{P}^{\nu} simply by substituting the new parameters.

Step 5. Deriving pricing formula using the change of measure techniques. We apply the results of Steps 3 and 4. The new measure ℙν\mathbb{P}^{\nu} introduced in Step 3 allows us to eliminate the problematic terms in 𝔼ℚ​I2\mathbb{E}^{\mathbb{Q}}I\_{2} and calculate this expectation relatively easily, since the distribution of τ\tau with respect to ℙν\mathbb{P}^{\nu} is known from Step 4.

While for the first two models (ILP and ILA) this scheme can be applied directly, for the third model (PLA) major modifications are needed. This is due to the presence of an additional source of randomness, which is the proportion coefficient PP. We provide a detailed description of these changes in the subsection dedicated to this model.

### 4.1. Independent loss process

Recall that under ILP assumption all variables Nt1N\_{t}^{1}, Nt2N\_{t}^{2}, Xk1X\_{k}^{1}, Xk2X\_{k}^{2} are independent, and thus the catastrophic share price process St𝒞S\_{t}^{\mathcal{C}} is a product of two independent single-region catastrophic share price processes: St𝒞,1\smash{S\_{t}^{\mathcal{C},1}}, St𝒞,2\smash{S\_{t}^{\mathcal{C},2}} (see ([2.7](https://arxiv.org/html/2510.17221v1#S2.E7 "In 2.3. Independent loss processes (ILP) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds"))).

###### Lemma 4.1.

For ILP and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | κ1=1α​(1−(ℒ​fX)​(α)),\displaystyle\kappa\_{1}=\frac{1}{\alpha}(1-(\mathcal{L}f\_{X})(\alpha)), | κ2=1β​(1−(ℒ​fX)​(β))\displaystyle\kappa\_{2}=\frac{1}{\beta}(1-(\mathcal{L}f\_{X})(\beta)) |  | (4.1) |

there exists a risk-neutral measure ℚ=ℚF⊗ℙC\mathbb{Q}=\mathbb{Q}\_{F}\otimes\mathbb{P}\_{C} and the catastrophe-risk and financial market risk variables under this measure are captured by equations ([3.1](https://arxiv.org/html/2510.17221v1#S3.E1 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds"))-([3.6](https://arxiv.org/html/2510.17221v1#S3.E6 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")).

###### Proof.

Since the financial-world measure is the same as in the 1D case, the second part of the lemma follows for the first part of the proof of Theorem 3 in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]. It only remains to find the values of κ1,κ2>0\kappa\_{1},\kappa\_{2}>0 for which the process St𝒞S\_{t}^{\mathcal{C}} is a martingale, that is, the equation 𝔼ℙC​[St𝒞|𝒞s]=Ss𝒞\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C}}\,|\,\mathcal{C}\_{s}]=S\_{s}^{\mathcal{C}} is satisfied for all s<ts<t. By independence of St𝒞,1\smash{S\_{t}^{\mathcal{C},1}} and St𝒞,2\smash{S\_{t}^{\mathcal{C},2}}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙC​[St𝒞|𝒞s]=𝔼ℙC​[St𝒞,1​St𝒞,2|𝒞s]=𝔼ℙC​[St𝒞,1|𝒞s]​𝔼ℙC​[St𝒞,2|𝒞s].\displaystyle\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C}}\,|\,\mathcal{C}\_{s}]=\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C},1}S\_{t}^{\mathcal{C},2}\,|\,\mathcal{C}\_{s}]=\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C},1}\,|\,\mathcal{C}\_{s}]\,\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C},2}\,|\,\mathcal{C}\_{s}]. |  |

Since St𝒞,1\smash{S\_{t}^{\mathcal{C},1}} and St𝒞,2\smash{S\_{t}^{\mathcal{C},2}} are catastrophic share prices for the 1D model, by Theorem 3 in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)], for κ1,κ2\kappa\_{1},\kappa\_{2} given by ([4.1](https://arxiv.org/html/2510.17221v1#S4.E1 "In Lemma 4.1. ‣ 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) the processes St𝒞,1\smash{S\_{t}^{\mathcal{C},1}} and St𝒞,2\smash{S\_{t}^{\mathcal{C},2}} are martingales. Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙC​[St𝒞|𝒞s]=Ss𝒞,1​Ss𝒞,2=Ss𝒞,\displaystyle\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C}}\,|\,\mathcal{C}\_{s}]=S\_{s}^{\mathcal{C},1}S\_{s}^{\mathcal{C},2}=S\_{s}^{\mathcal{C}}, |  |

and the martingale condition for St𝒞\smash{S\_{t}^{\mathcal{C}}} is satisfied.
∎

###### Proposition 4.2.

For ILP, under measure ℚ\mathbb{Q}, trigger time τ\tau has a distribution function FτF\_{\tau} given by

|  |  |  |
| --- | --- | --- |
|  | Fτ​(t)=1−exp⁡(−Λt1−Λt2)​(∑n=0∞(Λt1)nn!​(FX1)n⁣∗​(D1))​(∑n=0∞(Λt2)nn!​(FX2)n⁣∗​(D2))\displaystyle F\_{\tau}(t)=1-\exp(-\Lambda\_{t}^{1}-\Lambda\_{t}^{2})\left(\sum\_{n=0}^{\infty}\frac{(\Lambda\_{t}^{1})^{n}}{n!}(F\_{X}^{1})^{n\*}(D\_{1})\right)\left(\sum\_{n=0}^{\infty}\frac{(\Lambda\_{t}^{2})^{n}}{n!}(F\_{X}^{2})^{n\*}(D\_{2})\right) |  |

for t⩾0t\geqslant 0.

###### Proof.

By the independence of Lt1L\_{t}^{1} and Lt2L\_{t}^{2}, for t>0t>0 we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ​(τ>t)\displaystyle\mathbb{Q}(\tau>t) | =ℙC​(τ>t)\displaystyle=\mathbb{P}\_{C}(\tau>t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(τ1>t,τ2>t)\displaystyle=\mathbb{P}\_{C}(\tau\_{1}>t,\,\tau\_{2}>t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(Lt1<D1,Lt2<D2)\displaystyle=\mathbb{P}\_{C}(L\_{t}^{1}<D\_{1},\,L\_{t}^{2}<D\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(Lt1<D1)​ℙC​(Lt2<D2).\displaystyle=\mathbb{P}\_{C}(L\_{t}^{1}<D\_{1})\,\mathbb{P}\_{C}(L\_{t}^{2}<D\_{2}). |  |

Recall that Lt1L\_{t}^{1} is a compound Poisson process with cumulative intensity Λt1\Lambda\_{t}^{1} and loss distribution function FX1F\_{X}^{1}. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙC​(Lt1<D1)\displaystyle\mathbb{P}\_{C}(L\_{t}^{1}<D\_{1}) | =∑n=0∞(Λt1)nn!​exp⁡(−Λt1)​(FX1)n⁣∗​(D1).\displaystyle=\sum\_{n=0}^{\infty}\frac{(\Lambda\_{t}^{1})^{n}}{n!}\exp(-\Lambda\_{t}^{1})(F\_{X}^{1})^{n\*}(D\_{1}). |  |

This yields the desired formula.
∎

Note that even tough the case of ILP is the simplest one considering in this paper, the density function of τ\tau, which we further denote as fτ​(t)=Fτ′​(t)f\_{\tau}(t)=F^{\prime}\_{\tau}(t), does not follow any neat formula, as opposed to the other two assumptions. Since the calculations are easy, but rather tedious, we omit it here.

Following the third step, we now define a new measure ℙν\mathbb{P}^{\nu} by Radon-Nikodym derivative. We put

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙνd​ℙC|𝒞^t=exp(−α(1−ν)Lt1−β(1−ν)Lt2+Λt1(1−(ℒfX1)(α(1−ν))+Λt2(1−(ℒfX2)(β(1−ν)))=η(t),\displaystyle\begin{aligned} \frac{d\mathbb{P}^{\nu}}{d\mathbb{P}\_{C}}\Bigg{|}\_{\hat{\mathcal{C}}\_{t}}&=\exp\big{(}-\alpha(1-\nu)L\_{t}^{1}-\beta(1-\nu)L\_{t}^{2}\\ &+\Lambda\_{t}^{1}(1-(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))+\Lambda\_{t}^{2}(1-(\mathscr{L}f\_{X}^{2})(\beta(1-\nu))\big{)}=\eta(t),\end{aligned} |  | (4.2) |

where η​(t)\eta(t) is an exponential martingale. Comparing ([4.2](https://arxiv.org/html/2510.17221v1#S4.E2 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) to (47)-(49) from [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)], one can observe that for ILP the transformation kernel η​(t)\eta(t) is a product of two kernels corresponding to independent single-region catastrophic share price processes. This fact should not be surprising regarding the independence of Lt1L\_{t}^{1} and Lt2L\_{t}^{2}.

By Proposition ([4.5](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")), we deduce that the processes Lt1L\_{t}^{1} and Lt2L\_{t}^{2} are τ\tau-dependencies for ILP. Hence, we are interested in finding their distributions under ℙν\mathbb{P}^{\nu}.

###### Proposition 4.3.

The processes Lt1,Lt2L\_{t}^{1},L\_{t}^{2} under the measure ℙν\mathbb{P}^{\nu} are compound Poisson process with the same frequency with cumulative intensities

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λtν,1=Λt1​(ℒ​fX1)​(α​(1−ν)),\displaystyle\Lambda^{\nu,1}\_{t}=\Lambda\_{t}^{1}(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu)), | Λtν,2=Λt2​(ℒ​fX2)​(β​(1−ν))\displaystyle\Lambda^{\nu,2}\_{t}=\Lambda\_{t}^{2}(\mathcal{L}f\_{X}^{2})(\beta(1-\nu)) |  |

and loss distribution functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | FXν,1​(x)=exp⁡(−α​(1−ν)​x)(ℒ​fX1)​(α​(1−ν))​FX1​(x),\displaystyle F\_{X}^{\nu,1}(x)=\frac{\exp(-\alpha(1-\nu)x)}{(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))}F\_{X}^{1}(x), | FXν,2​(x)=exp⁡(−β​(1−ν)​x)(ℒ​fX2)​(β​(1−ν))​FX2​(x).\displaystyle F\_{X}^{\nu,2}(x)=\frac{\exp(-\beta(1-\nu)x)}{(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))}F\_{X}^{2}(x). |  |

###### Proof.

We prove the assertion by comparing moment generating functions. Recall that for compound Poisson process Lt1L\_{t}^{1} and z∈ℝz\in\mathbb{R} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙC​exp⁡(−z​Lt1)=exp⁡(((ℒ​fX1)​(z)−1)​Λt1).\displaystyle\mathbb{E}^{\mathbb{P}\_{C}}\exp(-zL\_{t}^{1})=\exp(((\mathcal{L}f\_{X}^{1})(z)-1)\Lambda\_{t}^{1}). |  | (4.3) |

By the formula ([4.2](https://arxiv.org/html/2510.17221v1#S4.E2 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) and independence of Lt1L\_{t}^{1} and Lt2L\_{t}^{2},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙν​exp⁡(−z​Lt1)\displaystyle\mathbb{E}^{\mathbb{P}^{\nu}}\exp(-zL\_{t}^{1}) | =𝔼ℙC​[exp⁡(−z​Lt1)​η​(t)]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp(-zL\_{t}^{1})\,\eta(t)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​exp⁡(−(z+α​(1−ν))​Lt1−β​(1−ν)​Lt2)\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\exp(-(z+\alpha(1-\nu))L\_{t}^{1}-\beta(1-\nu)L\_{t}^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp(Λt1(1−(ℒfX1)(α(1−ν))+Λt2(1−(ℒfX2)(β(1−ν)))\displaystyle\times\exp(\Lambda\_{t}^{1}(1-(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))+\Lambda\_{t}^{2}(1-(\mathscr{L}f\_{X}^{2})(\beta(1-\nu))) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(((ℒ​fX1)​(z+α​(1−ν))−1)​Λt1)\displaystyle=\exp(((\mathscr{L}f\_{X}^{1})(z+\alpha(1-\nu))-1)\Lambda\_{t}^{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡(((ℒ​fX2)​(β​(1−ν))−1)​Λt2)\displaystyle\times\exp(((\mathscr{L}f\_{X}^{2})(\beta(1-\nu))-1)\Lambda\_{t}^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp(Λt1(1−(ℒfX1)(α(1−ν))+Λt2(1−(ℒfX2)(β(1−ν)))\displaystyle\times\exp(\Lambda\_{t}^{1}(1-(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))+\Lambda\_{t}^{2}(1-(\mathscr{L}f\_{X}^{2})(\beta(1-\nu))) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(Λt1​((ℒ​fX1)​(z+α​(1−ν))−(ℒ​fX1)​(α​(1−ν))))\displaystyle=\exp(\Lambda\_{t}^{1}((\mathscr{L}f\_{X}^{1})(z+\alpha(1-\nu))-(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu)))) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(Λt1​(ℒ​fX1)​(α​(1−ν))​((ℒ​fX1)​(z+α​(1−ν))(ℒ​fX1)​(α​(1−ν))−1)).\displaystyle=\exp\left(\Lambda\_{t}^{1}(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))\left(\frac{(\mathscr{L}f\_{X}^{1})(z+\alpha(1-\nu))}{(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))}-1\right)\right). |  |

Comparing the above formula to ([4.3](https://arxiv.org/html/2510.17221v1#S4.E3 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")), we obtain

|  |  |  |
| --- | --- | --- |
|  | Λtν,1=Λt1​(ℒ​fX1)​(α​(1−ν)).\displaystyle\Lambda\_{t}^{\nu,1}=\Lambda\_{t}^{1}(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu)). |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | (ℒ​fX1)​(z+α​(1−ν))(ℒ​fX1)​(α​(1−ν))=∫0∞e−x​z​e−α​(1−ν)​x​F​(d​x)(ℒ​fX1)​(α​(1−ν))=∫0∞e−x​z​FXν,1​(d​x)=(ℒ​FXν,1)​(z).\displaystyle\frac{(\mathscr{L}f\_{X}^{1})(z+\alpha(1-\nu))}{(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))}=\int\_{0}^{\infty}e^{-xz}\frac{e^{-\alpha(1-\nu)x}F(dx)}{(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu))}=\int\_{0}^{\infty}e^{-xz}F\_{X}^{\nu,1}(dx)=(\mathscr{L}F\_{X}^{\nu,1})(z). |  |

and hence we read that FXν,1F^{\nu,1}\_{X} has the desired form. The remaining part of the proof for Lt2L\_{t}^{2} is identical.
∎

Combining Propositions [4.2](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") and [4.3](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds"), we find that distribution function FτνF\_{\tau}^{\nu} of τ\tau with respect to the measure ℙν\mathbb{P}^{\nu} is given by the same formula but with Λtν,i\Lambda\_{t}^{\nu,i} and FXν,iF\_{X}^{\nu,i} instead of Λti\Lambda\_{t}^{i} and FXiF\_{X}^{i} for i=1,2i=1,2. With these tools, we are now ready to evaluate the expected value of I2I\_{2}. Omitting the constants, by ([2.5](https://arxiv.org/html/2510.17221v1#S2.E5 "In 2.2. General 2D pricing framework ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")), ([2.6](https://arxiv.org/html/2510.17221v1#S2.E6 "In 2.2. General 2D pricing framework ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")), ([3.7](https://arxiv.org/html/2510.17221v1#S3.E7 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ[Sτ1−νB(0,τ)𝟙τ⩽T]=𝔼ℚ[exp(−α(1−ν)Lτ1−β(1−ν)Lτ2−ν∫0τrudu+(1−ν)σSWτ2+(1−ν)(ακ1Λτ1+βκ2Λτ2−12τσS2))𝟙τ⩽T].\displaystyle\begin{aligned} \mathbb{E}^{\mathbb{Q}}\big{[}S\_{\tau}^{1-\nu}B(0,\tau)&\mathbb{1}\_{\tau\leqslant T}\big{]}\\ &=\mathbb{E}^{\mathbb{Q}}\bigg{[}\exp\bigg{(}-\alpha(1-\nu)L\_{\tau}^{1}-\beta(1-\nu)L\_{\tau}^{2}-\nu\int\_{0}^{\tau}r\_{u}\,du\\ &+(1-\nu)\sigma\_{S}W\_{\tau}^{2}+(1-\nu)\left(\alpha\kappa\_{1}\Lambda\_{\tau}^{1}+\beta\kappa\_{2}\Lambda\_{\tau}^{2}-\tfrac{1}{2}\tau\sigma\_{S}^{2}\right)\bigg{)}\mathbb{1}\_{\tau\leqslant T}\bigg{]}.\end{aligned} |  | (4.4) |

We now define a new product measure ℚ¯=ℙν⊗ℚF\overline{\mathbb{Q}}=\mathbb{P}^{\nu}\otimes\mathbb{Q}\_{F} such that for any A∈𝒞^tA\in\hat{\mathcal{C}}\_{t} and B∈ℱ^tB\in\hat{\mathcal{F}}\_{t} we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ¯​𝟙A×B=𝔼ℙν​𝟙A​𝔼ℚF​𝟙B=𝔼ℙν​[η​(t)​𝟙A]​𝔼F​𝟙B=𝔼ℚ​[η​(t)​𝟙A×B].\displaystyle\mathbb{E}^{\overline{\mathbb{Q}}}\mathbb{1}\_{A\times B}=\mathbb{E}^{\mathbb{P}^{\nu}}\mathbb{1}\_{A}\,\mathbb{E}^{\mathbb{Q}\_{F}}\mathbb{1}\_{B}=\mathbb{E}^{\mathbb{P}^{\nu}}[\eta(t)\mathbb{1}\_{A}]\,\mathbb{E}\_{F}\mathbb{1}\_{B}=\mathbb{E}^{\mathbb{Q}}[\eta(t)\mathbb{1}\_{A\times B}]. |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | d​ℚ¯d​ℚ|𝒢t=η​(t),\displaystyle\frac{d\overline{\mathbb{Q}}}{d\mathbb{Q}}\bigg{|}\_{\mathcal{G}\_{t}}=\eta(t), |  |

where η​(t)\eta(t) is defined by ([4.2](https://arxiv.org/html/2510.17221v1#S4.E2 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")). In the above equation one can change deterministic tt to a stopping time τ\tau, provided that τ<∞\tau<\infty (see Proposition 1.7.1.4 in [[30](https://arxiv.org/html/2510.17221v1#bib.bib30)]). Thus, ([4.4](https://arxiv.org/html/2510.17221v1#S4.E4 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) is equal to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ¯​[φ​(τ)​exp⁡(−ν​∫0τru​𝑑u+(1−ν)​σS​Wτ2)​𝟙τ⩽T],\displaystyle\mathbb{E}^{\overline{\mathbb{Q}}}\bigg{[}\varphi(\tau)\exp\bigg{(}-\nu\int\_{0}^{\tau}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{\tau}^{2}\bigg{)}\mathbb{1}\_{\tau\leqslant T}\bigg{]}, |  | (4.5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ(τ)=exp(−Λτ1(1−(ℒfX1)(α(1−ν))\displaystyle\varphi(\tau)=\exp\bigg{(}-\Lambda\_{\tau}^{1}(1-(\mathscr{L}f\_{X}^{1})(\alpha(1-\nu)) | −Λτ2(1−(ℒfX2)(β(1−ν))\displaystyle-\Lambda\_{\tau}^{2}(1-(\mathscr{L}f\_{X}^{2})(\beta(1-\nu)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ν)(ακ1Λτ1+βκ2Λτ2−12τσS2)).\displaystyle+(1-\nu)\left(\alpha\kappa\_{1}\Lambda\_{\tau}^{1}+\beta\kappa\_{2}\Lambda\_{\tau}^{2}-\tfrac{1}{2}\tau\sigma\_{S}^{2}\right)\bigg{)}. |  |

Denoting the density of τ\tau under ℚ¯\overline{\mathbb{Q}} (or under ℙν\mathbb{P}^{\nu}) by fτνf\_{\tau}^{\nu} and conditioning ([4.5](https://arxiv.org/html/2510.17221v1#S4.E5 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) with τ\tau, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ¯[φ(τ)𝔼ℚ¯[exp(−ν∫0τrudu+(1−ν)σSWτ2)𝟙τ⩽T|τ]]=∫0Tφ​(t)​𝔼ℚF​[exp⁡(−ν​∫0tru​𝑑u+(1−ν)​σS​Wt2)]​fτν​(t)​𝑑t.\displaystyle\begin{aligned} \mathbb{E}^{\overline{\mathbb{Q}}}\bigg{[}\varphi(\tau)\,\mathbb{E}^{\overline{\mathbb{Q}}}&\bigg{[}\exp\bigg{(}-\nu\int\_{0}^{\tau}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{\tau}^{2}\bigg{)}\mathbb{1}\_{\tau\leqslant T}\,|\,\tau\bigg{]}\bigg{]}\\ &=\int\_{0}^{T}\varphi(t)\,\mathbb{E}^{\mathbb{Q}\_{F}}\left[\exp\left(-\nu\int\_{0}^{t}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{t}^{2}\right)\right]f\_{\tau}^{\nu}(t)\,dt.\end{aligned} |  | (4.6) |

By the arguments presented in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] (see Lemma 2 and equations (55)-(60) therein), the above expectation with respect to the financial measure ℚF\mathbb{Q}\_{F} can be simplified to

|  |  |  |
| --- | --- | --- |
|  | exp⁡(12​(1−ν)2​σS2​t)​P​(r0,t,θ¯r,m¯r,σ¯r),\displaystyle\exp\left(\tfrac{1}{2}(1-\nu)^{2}\sigma\_{S}^{2}t\right)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r}), |  |

where

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | θ¯r=ν​(θr−σr​σS​ρ​(1−ν)),\displaystyle\bar{\theta}\_{r}=\sqrt{\nu}(\theta\_{r}-\sigma\_{r}\sigma\_{S}\rho(1-\nu)), | m¯r=ν​mr​θr/θ¯r,\displaystyle\bar{m}\_{r}=\nu m\_{r}\theta\_{r}/\bar{\theta}\_{r}, | σ¯r=ν​σr.\displaystyle\bar{\sigma}\_{r}=\sqrt{\nu}\sigma\_{r}. |  | (4.7) |

Therefore ([4.6](https://arxiv.org/html/2510.17221v1#S4.E6 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) can be expressed as

|  |  |  |
| --- | --- | --- |
|  | ∫0tφ​(t)​exp⁡(12​(1−ν)2​σS2​t)​P​(r0,t,θ¯r,m¯r,σ¯r)​fτν​(t)​𝑑t,\displaystyle\int\_{0}^{t}\varphi(t)\exp\left(\tfrac{1}{2}(1-\nu)^{2}\sigma\_{S}^{2}t\right)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})f\_{\tau}^{\nu}(t)\,dt, |  |

which proves the theorem for ILP case. ∎

### 4.2. Independent loss amounts

The second type of aggregated loss process that we consider is ILA, in which the loss amounts are independent with common counting process NtN\_{t}. Merged aggregate loss process LtL\_{t} defined by ([2.9](https://arxiv.org/html/2510.17221v1#S2.E9 "In 2.4. Independent loss amounts (ILA) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds")) obeys compound Poisson distribution with loss amounts

|  |  |  |
| --- | --- | --- |
|  | Xk=αα+β​Xk1+βα+β​Xk2.\displaystyle X\_{k}=\frac{\alpha}{\alpha+\beta}X\_{k}^{1}+\frac{\beta}{\alpha+\beta}X\_{k}^{2}. |  |

It is easy to see that if FX1F\_{X}^{1} and FX2F\_{X}^{2} are distribution functions of X1X\_{1} and X2X\_{2}, respectively, then the distribution function FXF\_{X} of XkX\_{k} is given by the convolution

|  |  |  |  |
| --- | --- | --- | --- |
|  | FX​(x)=(F~X1∗F~X2)​(x),\displaystyle F\_{X}(x)=(\tilde{F}\_{X}^{1}\*\tilde{F}\_{X}^{2})(x), |  | (4.8) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | F~X1​(x)=FX1​(α​xα+β),\displaystyle\tilde{F}\_{X}^{1}(x)=F\_{X}^{1}\left(\frac{\alpha x}{\alpha+\beta}\right), | F~X2​(x)=FX2​(β​xα+β).\displaystyle\tilde{F}\_{X}^{2}(x)=F\_{X}^{2}\left(\frac{\beta x}{\alpha+\beta}\right). |  |

In this case, catastrophic share price process ([3.3](https://arxiv.org/html/2510.17221v1#S3.E3 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞\displaystyle S\_{t}^{\mathcal{C}} | =exp⁡(−(α+β)​Lt+(α+β)​κ​∫0tλu​𝑑u).\displaystyle=\exp\left(-(\alpha+\beta)L\_{t}+(\alpha+\beta)\kappa\int\_{0}^{t}\lambda\_{u}\,du\right). |  |

The proof for ILA also follows the steps described at the beginning of this section. Below we present a few results crucial in proving the pricing formula.

###### Lemma 4.4.

For ILA and

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ=1α+β​(1−(ℒ​fX1)​(α)​(ℒ​fX2)​(β))\displaystyle\kappa=\frac{1}{\alpha+\beta}\left(1-(\mathcal{L}f\_{X}^{1})(\alpha)(\mathcal{L}f\_{X}^{2})(\beta)\right) |  | (4.9) |

there exists a risk-neutral measure ℚ=ℚF⊗ℙC\mathbb{Q}=\mathbb{Q}\_{F}\otimes\mathbb{P}\_{C} and the catastrophe-risk and financial market risk variables under this measure are captured by equations ([3.1](https://arxiv.org/html/2510.17221v1#S3.E1 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds"))-([3.6](https://arxiv.org/html/2510.17221v1#S3.E6 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")).

###### Proof.

Inserting α+β\alpha+\beta instead of α\alpha and FXF\_{X} given by ([4.8](https://arxiv.org/html/2510.17221v1#S4.E8 "In 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) into Theorem 3 in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] leads to our claim with

|  |  |  |
| --- | --- | --- |
|  | κ=1α+β​(1−(ℒ​fX)​(α+β)).\displaystyle\kappa=\frac{1}{\alpha+\beta}(1-(\mathcal{L}f\_{X})(\alpha+\beta)). |  |

Recall that Xk=αα+β​Xk1+βα+β​Xk2X\_{k}=\frac{\alpha}{\alpha+\beta}X\_{k}^{1}+\frac{\beta}{\alpha+\beta}X\_{k}^{2} and by that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℒ​fX)​(α+β)\displaystyle(\mathcal{L}f\_{X})(\alpha+\beta) | =𝔼ℚ​exp⁡(−(α+β)​Xk)\displaystyle=\mathbb{E}^{\mathbb{Q}}\exp\left(-(\alpha+\beta)X\_{k}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ​exp⁡(−α​Xk1−β​Xk2)=(ℒ​fX1)​(α)​(ℒ​fX2)​(β).\displaystyle=\mathbb{E}^{\mathbb{Q}}\exp\left(-\alpha X\_{k}^{1}-\beta X\_{k}^{2}\right)=(\mathcal{L}f\_{X}^{1})(\alpha)(\mathcal{L}f\_{X}^{2})(\beta). |  |

This concludes the proof.
∎

###### Proposition 4.5.

For independent loss amounts, under measure ℚ\mathbb{Q}, trigger time τ\tau has a distribution function FτF\_{\tau} and density fτf\_{\tau} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fτ​(t)\displaystyle F\_{\tau}(t) | =1−∑n=0∞Λtnn!​exp⁡(−Λt)​(FX1)n⁣∗​(D1)​(FX2)n⁣∗​(D2),\displaystyle=1-\sum\_{n=0}^{\infty}\frac{\Lambda\_{t}^{n}}{n!}\exp(-\Lambda\_{t})(F\_{X}^{1})^{n\*}(D\_{1})(F\_{X}^{2})^{n\*}(D\_{2}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | fτ​(t)\displaystyle f\_{\tau}(t) | =λt​exp⁡(−Λt)​(1−∑n=1∞(Λtn−1(n−1)!−Λtnn!)​(FX1)n⁣∗​(D1)​(FX2)n⁣∗​(D2))\displaystyle=\lambda\_{t}\exp(-\Lambda\_{t})\left(1-\sum\_{n=1}^{\infty}\left(\frac{\Lambda\_{t}^{n-1}}{(n-1)!}-\frac{\Lambda\_{t}^{n}}{n!}\right)(F\_{X}^{1})^{n\*}(D\_{1})(F\_{X}^{2})^{n\*}(D\_{2})\right) |  |

for t⩾0t\geqslant 0.

###### Proof.

Let t>0t>0. Observe that τ\tau does not depend on financial world and only on catastrophic world, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ​(τ>t)\displaystyle\mathbb{Q}(\tau>t) | =ℙC​(τ>t)\displaystyle=\mathbb{P}\_{C}(\tau>t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(τ1>t,τ2>t)\displaystyle=\mathbb{P}\_{C}(\tau\_{1}>t,\,\tau\_{2}>t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(Lt1<D1,Lt2<D2)\displaystyle=\mathbb{P}\_{C}\left(L\_{t}^{1}<D\_{1},\,L\_{t}^{2}<D\_{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[ℙC​(Lt1<D1,Lt2​<D2|​Nt)]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\mathbb{P}\_{C}\left(L\_{t}^{1}<D\_{1},\,L\_{t}^{2}<D\_{2}\,|\,N\_{t}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[ℙC​(Lt1​<D1|​Nt)​ℙC​(Lt2​<D2|​Nt)]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\mathbb{P}\_{C}\left(L\_{t}^{1}<D\_{1}\,|N\_{t}\,\right)\mathbb{P}\_{C}\left(L\_{t}^{2}<D\_{2}\,|\,N\_{t}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[(FX1)Nt⁣∗​(D1)​(FX2)Nt⁣∗​(D2)].\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[(F\_{X}^{1})^{N\_{t}\*}(D\_{1})(F\_{X}^{2})^{N\_{t}\*}(D\_{2})\right]. |  |

Above we used the fact that Lt1,Lt2L\_{t}^{1},L\_{t}^{2} are independent conditionally on NtN\_{t}. Since NtN\_{t} has a Poisson distribution with cumulative intensity Λt\Lambda\_{t}, we have

|  |  |  |
| --- | --- | --- |
|  | ℚ​(τ>t)=∑n=0∞Λtnn!​exp⁡(−Λt)​(FX1)n⁣∗​(D1)​(FX2)n⁣∗​(D2),\displaystyle\mathbb{Q}(\tau>t)=\sum\_{n=0}^{\infty}\frac{\Lambda\_{t}^{n}}{n!}\exp(-\Lambda\_{t})(F\_{X}^{1})^{n\*}(D\_{1})(F\_{X}^{2})^{n\*}(D\_{2}), |  |

Differentiating the above formula with respect to tt yields

|  |  |  |
| --- | --- | --- |
|  | λt​exp⁡(−Λt)​(∑n=1∞(Λtn−1(n−1)!−Λtnn!)​(FX1)n⁣∗​(D1)​(FX2)n⁣∗​(D2)−1)\displaystyle\lambda\_{t}\exp(-\Lambda\_{t})\left(\sum\_{n=1}^{\infty}\left(\frac{\Lambda\_{t}^{n-1}}{(n-1)!}-\frac{\Lambda\_{t}^{n}}{n!}\right)(F\_{X}^{1})^{n\*}(D\_{1})(F\_{X}^{2})^{n\*}(D\_{2})-1\right) |  |

and the assertion follows.
∎

The next part of the proof is also analogical; we define a new measure ℙν\mathbb{P}^{\nu} by its Radon–Nikodym derivative:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙνd​ℙC|𝒞^t=exp(−(1−ν)(α+β)Lt+Λt(1−(ℒfX1)(α(1−ν))(ℒfX2)(β(1−ν))))=η(t),\displaystyle\begin{aligned} \frac{d\mathbb{P}^{\nu}}{d\mathbb{P}\_{C}}\Bigg{|}\_{\hat{\mathcal{C}}\_{t}}&=\exp\bigg{(}-(1-\nu)(\alpha+\beta)L\_{t}\\ &\quad+\Lambda\_{t}(1-(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu)))\bigg{)}=\eta(t),\end{aligned} |  | (4.10) |

where η​(t)\eta(t) is again an exponential martingale.

Similarly to the ILP case, for ILA the τ\tau-dependencies indicated by Proposition [4.10](https://arxiv.org/html/2510.17221v1#S4.E10 "In 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") are again aggregated loss processes Lt1L\_{t}^{1} and Lt2L\_{t}^{2}. The following result fulfils the fourth step of the proof.

###### Proposition 4.6.

The processes Lt1,Lt2L\_{t}^{1},L\_{t}^{2} under the measure ℙν\mathbb{P}^{\nu} are compound Poisson process with the same frequency with cumulative intensity

|  |  |  |
| --- | --- | --- |
|  | Λtν=Λt​(ℒ​fX1)​(α​(1−ν))​(ℒ​fX2)​(β​(1−ν))\displaystyle\Lambda^{\nu}\_{t}=\Lambda\_{t}(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu)) |  |

and loss distribution functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | FXν,1​(x)=exp⁡(−α​(1−ν)​x)(ℒ​fX1)​(α​(1−ν))​FX1​(x),\displaystyle F\_{X}^{\nu,1}(x)=\frac{\exp(-\alpha(1-\nu)x)}{(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))}F\_{X}^{1}(x), | FXν,2​(x)=exp⁡(−β​(1−ν)​x)(ℒ​fX2)​(β​(1−ν))​FX2​(x).\displaystyle F\_{X}^{\nu,2}(x)=\frac{\exp(-\beta(1-\nu)x)}{(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))}F\_{X}^{2}(x). |  |

###### Proof.

We check the distributions directly by studying the moment generating functions. Recall that for the compound Poisson process Lt1L\_{t}^{1} and z∈ℝz\in\mathbb{R} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙC​exp⁡(−z​Lt1)=exp⁡(((ℒ​fX1)​(z)−1)​Λt).\displaystyle\mathbb{E}^{\mathbb{P}\_{C}}\exp(-zL\_{t}^{1})=\exp(((\mathcal{L}f\_{X}^{1})(z)-1)\Lambda\_{t}). |  | (4.11) |

By the change of measure ([4.10](https://arxiv.org/html/2510.17221v1#S4.E10 "In 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙν​exp⁡(−z​Lt1)=𝔼ℙC​[exp⁡(−z​Lt1)​η​(t)]=exp⁡((1−(ℒ​fX1)​((1−ν)​(α))​(ℒ​fX2)​((1−ν)​(β)))​Λt)×𝔼ℙC​exp⁡(−(z+α​(1−ν))​Lt1−β​(1−ν)​Lt2).\displaystyle\begin{aligned} \mathbb{E}^{\mathbb{P}^{\nu}}\exp(-zL\_{t}^{1})&=\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp(-zL\_{t}^{1})\eta(t)\right]\\ &=\exp((1-(\mathcal{L}f\_{X}^{1})((1-\nu)(\alpha))(\mathcal{L}f\_{X}^{2})((1-\nu)(\beta)))\Lambda\_{t})\\ &\times\mathbb{E}^{\mathbb{P}\_{C}}\exp\left(-(z+\alpha(1-\nu))L\_{t}^{1}-\beta(1-\nu)L\_{t}^{2}\right).\end{aligned} |  | (4.12) |

Recall that Lt1L\_{t}^{1} and Lt2L\_{t}^{2} are independent conditionally on NtN\_{t}, hence the latter expectation is equal to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙC\displaystyle\mathbb{E}^{\mathbb{P}\_{C}} | [𝔼ℙC​[exp⁡(−(z+α​(1−ν))​Lt1−β​(1−ν)​Lt2)|Nt]]\displaystyle\left[\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp\left(-(z+\alpha(1-\nu))L\_{t}^{1}-\beta(1-\nu)L\_{t}^{2}\right)\,|\,N\_{t}\right]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[𝔼ℙC​[exp⁡(−(z+α​(1−ν))​Lt1)|Nt]​𝔼ℙC​[exp⁡(−β​(1−ν)​Lt2)|Nt]]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\bigg{[}\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp(-(z+\alpha(1-\nu))L\_{t}^{1})\,|\,N\_{t}\right]\,\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp(-\beta(1-\nu)L\_{t}^{2})\,|\,N\_{t}\right]\bigg{]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[∏k=1Nt𝔼ℙC​[exp⁡(−(z+α​(1−ν))​X11)]​𝔼ℙC​[exp⁡(−β​(1−ν)​X12)]]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\bigg{[}\prod\_{k=1}^{N\_{t}}\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp(-(z+\alpha(1-\nu))X\_{1}^{1})\right]\,\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp(-\beta(1-\nu)X\_{1}^{2})\right]\bigg{]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[∏k=1Nt(ℒ​fX1)​(z+α​(1−ν))​(ℒ​fX2)​(β​(1−ν))]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\bigg{[}\prod\_{k=1}^{N\_{t}}(\mathcal{L}f\_{X}^{1})(z+\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))\bigg{]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[((ℒ​fX1)​(z+α​(1−ν))​(ℒ​fX2)​(β​(1−ν)))Nt].\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\bigg{[}\big{(}(\mathcal{L}f\_{X}^{1})(z+\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))\big{)}^{N\_{t}}\bigg{]}. |  |

We observe that the latter expected value above is a probability generating function of NtN\_{t} evaluated in (ℒ​fX1)​(z+α​(1−ν))​(ℒ​fX2)​(β​(1−ν))(\mathcal{L}f\_{X}^{1})(z+\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu)). Hence, this is equal to

|  |  |  |
| --- | --- | --- |
|  | exp⁡(((ℒ​fX1)​(z+α​(1−ν))​(ℒ​fX2)​(β​(1−ν))−1)​Λt).\displaystyle\exp\big{(}((\mathcal{L}f\_{X}^{1})(z+\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))-1)\Lambda\_{t}\big{)}. |  |

Inserting this into ([4.12](https://arxiv.org/html/2510.17221v1#S4.E12 "In 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙν\displaystyle\mathbb{E}^{\mathbb{P}^{\nu}} | exp⁡(−z​Lt1)\displaystyle\exp(-zL\_{t}^{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp((ℒfX1)(z+α(1−ν))(ℒfX2)(β(1−ν))Λt\displaystyle=\exp\big{(}(\mathcal{L}f\_{X}^{1})(z+\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))\Lambda\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(ℒfX1)((1−ν)(α))(ℒfX2)((1−ν)β))Λt)\displaystyle-(\mathcal{L}f\_{X}^{1})((1-\nu)(\alpha))(\mathcal{L}f\_{X}^{2})((1-\nu)\beta))\Lambda\_{t}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(Λt​(ℒ​fX1)​(α​(1−ν))​(ℒ​fX2)​(β​(1−ν))​((ℒ​fX1)​(z+α​(1−ν))(ℒ​fX1)​(α​(1−ν))−1)).\displaystyle=\exp\left(\Lambda\_{t}(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))\left(\frac{(\mathcal{L}f\_{X}^{1})(z+\alpha(1-\nu))}{(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))}-1\right)\right). |  |

We obtain our claim for Lt1L\_{t}^{1} by comparing the parameters with ([4.11](https://arxiv.org/html/2510.17221v1#S4.E11 "In 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")). By similar arguments, one can prove an analogous result for Lt2L\_{t}^{2}.
∎

The rest of the calculations can be directly repeated from the proof for ILP. We change the product measure ℚ\mathbb{Q} for the new one ℚ¯=ℙν⊗ℚF\smash{\overline{\mathbb{Q}}=\mathbb{P}^{\nu}\otimes\mathbb{Q}\_{F}} and after analogous transformations we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ[Sτ1−νB(0,τ)\displaystyle\mathbb{E}^{\mathbb{Q}}\big{[}S\_{\tau}^{1-\nu}B(0,\tau) | 𝟙τ⩽T]=∫0tφ(t)exp(12(1−ν)2σS2t)P(r0,t,θ¯r,m¯r,σ¯r)fτν(t)dt,\displaystyle\mathbb{1}\_{\tau\leqslant T}\big{]}=\int\_{0}^{t}\varphi(t)\exp\left(\tfrac{1}{2}(1-\nu)^{2}\sigma\_{S}^{2}t\right)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})f\_{\tau}^{\nu}(t)\,dt, |  |

where the density fτνf\_{\tau}^{\nu} of τ\tau under ℙν\mathbb{P}^{\nu} follows from replacing Λt\Lambda\_{t} and FXF\_{X} in density fτf\_{\tau} from Proposition [4.5](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") with Λtν\Lambda\_{t}^{\nu} and FXνF\_{X}^{\nu} from Proposition [4.6](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem6 "Proposition 4.6. ‣ 4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds"), parameters θ¯\bar{\theta}, m¯r\bar{m}\_{r}, σ¯r\bar{\sigma}\_{r} are defined as in ([4.7](https://arxiv.org/html/2510.17221v1#S4.E7 "In 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ(t)=exp(−Λt(1−\displaystyle\varphi(t)=\exp\bigg{(}-\Lambda\_{t}(1- | (ℒfX1)(α(1−ν))(ℒfX2)(β(1−ν)))\displaystyle(\mathcal{L}f\_{X}^{1})(\alpha(1-\nu))(\mathcal{L}f\_{X}^{2})(\beta(1-\nu))) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ν)((α+β)κΛt−12tσS2)).\displaystyle+(1-\nu)\left((\alpha+\beta)\kappa\Lambda\_{t}-\tfrac{1}{2}t\sigma\_{S}^{2}\right)\bigg{)}. |  |

This finishes the proof for ILA. ∎

### 4.3. Proportional loss amounts

Now we will focus on the model with proportional loss amounts. Recall that in this case the catastrophic share price is given by the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | St𝒞=exp⁡(α​∑k=1NtP​Xk+β​∑k=1Nt(1−P)​Xk+κ​(α+β)​∫0tλu​𝑑u),\displaystyle S\_{t}^{\mathcal{C}}=\exp\left(\alpha\sum\_{k=1}^{N\_{t}}PX\_{k}+\beta\sum\_{k=1}^{N\_{t}}(1-P)X\_{k}+\kappa(\alpha+\beta)\int\_{0}^{t}\lambda\_{u}\,du\right), |  | (4.13) |

where Nt,P,XkN\_{t},P,X\_{k} are all independent. Following the notation introduced in Section [2.5](https://arxiv.org/html/2510.17221v1#S2.SS5 "2.5. Proportional loss amounts (PLA) ‣ 2. Considered models ‣ Design and valuation of multi-region CoCoCat bonds"), let Q=α​P+β​(1−P)Q=\alpha P+\beta(1-P) and Lt=∑k=1NtXkL\_{t}=\sum\_{k=1}^{N\_{t}}X\_{k} so that

|  |  |  |
| --- | --- | --- |
|  | α​∑k=1NtP​Xk+β​∑k=1Nt(1−P)​Xk=Q​Lt,\displaystyle\alpha\sum\_{k=1}^{N\_{t}}PX\_{k}+\beta\sum\_{k=1}^{N\_{t}}(1-P)X\_{k}=QL\_{t}, |  |

As before, we will start with finding a risk-neutral measure for this model. We state our result as a separate lemma.

###### Lemma 4.7.

For RPL and

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ=1α+β​(1−𝔼ℙC​[(ℒ​fX)​(Q)])\displaystyle\kappa=\frac{1}{\alpha+\beta}\left(1-\mathbb{E}^{\mathbb{P}\_{C}}\left[(\mathcal{L}f\_{X})(Q)\right]\right) |  | (4.14) |

there exists a risk-neutral measure ℚ=ℚF⊗ℙC\mathbb{Q}=\mathbb{Q}\_{F}\otimes\mathbb{P}\_{C} and the catastrophe-risk and financial market risk variables under this measure are captured by equations ([3.1](https://arxiv.org/html/2510.17221v1#S3.E1 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds"))-([3.6](https://arxiv.org/html/2510.17221v1#S3.E6 "In Proposition 3.1. ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")).

###### Proof.

Since the financial-world measure is the same as in 1-D case, the second part of the lemma follows for the first part of the proof of Theorem 3 in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)]. It remains only to find the value of κ>0\kappa>0 for which the process St𝒞S\_{t}^{\mathcal{C}} is a martingale, that is the equation 𝔼ℙC​[St𝒞|𝒞s]=Ss𝒞\mathbb{E}^{\mathbb{P}\_{C}}[S\_{t}^{\mathcal{C}}|\mathcal{C}\_{s}]=S\_{s}^{\mathcal{C}} is satisfied for all s<ts<t.

This condition can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙC​[exp⁡(−Q​(Lt−Ls)+κ​(α+β)​∫stλu​𝑑u)|𝒞s]=1.\displaystyle\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp\left(-Q(L\_{t}-L\_{s})+\kappa(\alpha+\beta)\int\_{s}^{t}\lambda\_{u}\,du\right)|\,\mathcal{C}\_{s}\right]=1. |  | (4.15) |

Let us inspect expectation 𝔼ℙC​exp⁡(−Q​(Lt−Ls))\mathbb{E}^{\mathbb{P}\_{C}}\exp(-Q(L\_{t}-L\_{s})). Conditioning twice, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙC​exp⁡(−Q​(Lt−Ls))\displaystyle\mathbb{E}^{\mathbb{P}\_{C}}\exp(-Q(L\_{t}-L\_{s})) | =𝔼ℙC[𝔼ℙC[𝔼ℙC[exp(−Q(Lt−Ls))|Q]|Nt−Ns]]]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\mathbb{E}^{\mathbb{P}\_{C}}[\mathbb{E}^{\mathbb{P}\_{C}}[\exp(-Q(L\_{t}-L\_{s}))\,|\,Q]|\,N\_{t}-N\_{s}]]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[𝔼ℙC​[𝔼ℙC​[exp⁡(−Q​∑k=1Nt−NsXk)|Q]|Nt−Ns]]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\mathbb{E}^{\mathbb{P}\_{C}}\left[\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp\left(-Q\sum\_{k=1}^{N\_{t}-N\_{s}}X\_{k}\right)|\,Q\right]|\,N\_{t}-N\_{s}\right]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[∏k=1Nt−Ns𝔼ℙC​[𝔼ℙC​[exp⁡(−Q​Xk)|Q]]]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\prod\_{k=1}^{N\_{t}-N\_{s}}\mathbb{E}^{\mathbb{P}\_{C}}\left[\mathbb{E}^{\mathbb{P}\_{C}}\left[\exp\left(-QX\_{k}\right)|\,Q\right]\right]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[∏k=1Nt−Ns𝔼ℙC​[(ℒ​fX)​(Q)]]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[\prod\_{k=1}^{N\_{t}-N\_{s}}\mathbb{E}^{\mathbb{P}\_{C}}[(\mathcal{L}f\_{X})(Q)]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙC​[(𝔼ℙC​[(ℒ​fX)​(Q)])Nt−Ns]\displaystyle=\mathbb{E}^{\mathbb{P}\_{C}}\left[(\mathbb{E}^{\mathbb{P}\_{C}}[(\mathcal{L}f\_{X})(Q)])^{N\_{t}-N\_{s}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =GNt−Ns​(𝔼ℙC​[(ℒ​fX)​(Q)])\displaystyle=G\_{N\_{t}-N\_{s}}(\mathbb{E}^{\mathbb{P}\_{C}}[(\mathcal{L}f\_{X})(Q)]) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡((𝔼ℙC​[(ℒ​fX)​(Q)]−1)​∫stλu​𝑑u).\displaystyle=\exp\left((\mathbb{E}^{\mathbb{P}\_{C}}[(\mathcal{L}f\_{X})(Q)]-1)\int\_{s}^{t}\lambda\_{u}\,du\right). |  |

where GNt−NsG\_{N\_{t}-N\_{s}} is the probability generating function of the Poisson random variable with mean ∫stλu​𝑑u\int\_{s}^{t}\lambda\_{u}\,du. Hence, ([4.15](https://arxiv.org/html/2510.17221v1#S4.E15 "In 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) is satisfied if and only if

|  |  |  |
| --- | --- | --- |
|  | κ=1α+β​(1−𝔼ℙC​[(ℒ​fX)​(Q)])\displaystyle\kappa=\frac{1}{\alpha+\beta}\left(1-\mathbb{E}^{\mathbb{P}\_{C}}\left[(\mathcal{L}f\_{X})(Q)\right]\right) |  |

and the proof is complete.
∎

Note that when we assume fixed proportional loss amounts with deterministic proportion coefficient pp instead of random PP, the above result remains true with q=α​p+β​(1−p)q=\alpha p+\beta(1-p) instead of QQ. Since qq is deterministic, equation ([4.14](https://arxiv.org/html/2510.17221v1#S4.E14 "In Lemma 4.7. ‣ 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) simplifies to

|  |  |  |
| --- | --- | --- |
|  | κ=1α+β​(1−(ℒ​fX)​(q)).\displaystyle\kappa=\frac{1}{\alpha+\beta}(1-(\mathcal{L}f\_{X})(q)). |  |

Before we proceed to the next step of the proof, let us explain the idea for RPL. Recall that our aim is to calculate 𝔼ℚ​[Sτ1−ν​B​(0,τ)​𝟙τ⩽T]\mathbb{E}^{\mathbb{Q}}\big{[}S\_{\tau}^{1-\nu}B(0,\tau)\mathbb{1}\_{\tau\leqslant T}\big{]}, where, unlike for ILP and ILA, the process StS\_{t} depends also PP. That’s why we condition this expected value with PP to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[𝔼ℚ​[Sτ1−ν​B​(0,τ)​𝟙τ⩽T|P]].\displaystyle\mathbb{E}^{\mathbb{Q}}\left[\mathbb{E}^{\mathbb{Q}}\left[S\_{\tau}^{1-\nu}B(0,\tau)\mathbb{1}\_{\tau\leqslant T}\,|\,P\right]\right]. |  | (4.16) |

In this case, the trick with change of measure will be applied in the inner (conditional) expectation. We define a conditional catastrophic measure ℙC|P​(A)\mathbb{P}\_{C|P}(A) such that for any A∈𝒞^∞\smash{A\in\hat{\mathcal{C}}\_{\infty}} we have

|  |  |  |
| --- | --- | --- |
|  | ℙC|P​(A)=ℙC​(A|P).\displaystyle\mathbb{P}\_{C|P}(A)=\mathbb{P}\_{C}(A|P). |  |

Similarly, let ℚ|P=ℙC|P⊗ℚF\mathbb{Q}\_{|P}=\mathbb{P}\_{C|P}\otimes\mathbb{Q}\_{F} be a corresponding product measure. We can now rewrite ([4.16](https://arxiv.org/html/2510.17221v1#S4.E16 "In 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[𝔼ℚ|P​[Sτ1−ν​B​(0,τ)​𝟙τ⩽T]]\displaystyle\mathbb{E}^{\mathbb{Q}}\left[\mathbb{E}^{\mathbb{Q}\_{|P}}\left[S\_{\tau}^{1-\nu}B(0,\tau)\mathbb{1}\_{\tau\leqslant T}\right]\right] |  | (4.17) |

and continue to work with the inner expectation according to a similar scheme as for ILP and ILA but with ℚ|P\mathbb{Q}\_{|P} instead of ℚ\mathbb{Q}.

Proceeding to the second step of the proof, we identify the distribution of the time of the trigger time τ\tau. The results are given in the following proposition.

###### Proposition 4.8.

For random proportional loss process, under measure ℚ|P\mathbb{Q}\_{|P}, trigger time τ\tau has a distribution function FτF\_{\tau} and density fτf\_{\tau} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fτ​(t)\displaystyle F\_{\tau}(t) | =1−∑n=0∞Λtnn!​exp⁡(−Λt)​FXn⁣∗​(DP)\displaystyle=1-\sum\_{n=0}^{\infty}\frac{\Lambda\_{t}^{n}}{n!}\exp(-\Lambda\_{t})F\_{X}^{n\*}(D\_{P}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | fτ​(t)\displaystyle f\_{\tau}(t) | =λt​exp⁡(−Λt)​(1−∑n=1∞(Λtn−1(n−1)!−Λtnn!)​FXn⁣∗​(DP))\displaystyle=\lambda\_{t}\exp(-\Lambda\_{t})\left(1-\sum\_{n=1}^{\infty}\left(\frac{\Lambda\_{t}^{n-1}}{(n-1)!}-\frac{\Lambda\_{t}^{n}}{n!}\right)F\_{X}^{n\*}(D\_{P})\right) |  |

for t⩾0t\geqslant 0, where DP=min⁡{D1/P,D2/(1−P)}D\_{P}=\min\left\{D\_{1}/P,D\_{2}/(1-P)\right\}.

###### Proof.

Let t>0t>0. As before, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ|P​(τ>t)\displaystyle\mathbb{Q}\_{|P}(\tau>t) | =ℙC​(τ>t|P)\displaystyle=\mathbb{P}\_{C}(\tau>t\,|\,P) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(τ1>t,τ2>t|P)\displaystyle=\mathbb{P}\_{C}(\tau\_{1}>t,\,\tau\_{2}>t\,|\,P) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(Lt1<D1,Lt2​<D2|​P)\displaystyle=\mathbb{P}\_{C}\left(L\_{t}^{1}<D\_{1},\,L\_{t}^{2}<D\_{2}\,|\,P\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(P​Lt<D1,(1−P)​Lt​<D2|​P)\displaystyle=\mathbb{P}\_{C}\left(PL\_{t}<D\_{1},\,(1-P)L\_{t}<D\_{2}\,|\,P\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙC​(Lt​<DP|​P).\displaystyle=\mathbb{P}\_{C}\left(L\_{t}<D\_{P}\,|\,P\right). |  |

where Lt=∑k=1NtXkL\_{t}=\sum\_{k=1}^{N\_{t}}X\_{k} and DP=min⁡{D1/P,D2/(1−P)}D\_{P}=\min\left\{D\_{1}/P,D\_{2}/(1-P)\right\}. Recall that NtN\_{t} follows a Poisson distribution with cumulative intensity Λt\Lambda\_{t} and (Xk)(X\_{k}) are i.i.d. random variables, independent from NtN\_{t}, with distribution function FXF\_{X}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙC​(Lt​<DP|​P)\displaystyle\mathbb{P}\_{C}(L\_{t}<D\_{P}\,|\,P) | =ℙC​(Lt=0|P)+ℙC​(0<Lt​<DP|​P)\displaystyle=\mathbb{P}\_{C}(L\_{t}=0\,|\,P)+\mathbb{P}\_{C}(0<L\_{t}<D\_{P}\,|\,P) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−Λt)+∑n=1∞Λtnn!​exp⁡(−Λt)​FXn⁣∗​(DP),\displaystyle=\exp(-\Lambda\_{t})+\sum\_{n=1}^{\infty}\frac{\Lambda\_{t}^{n}}{n!}\exp(-\Lambda\_{t})F\_{X}^{n\*}(D\_{P}), |  |

Differentiating the above formula with respect to tt yields

|  |  |  |
| --- | --- | --- |
|  | λt​exp⁡(−Λt)​(∑n=1∞(Λtn−1(n−1)!−Λtnn!)​FXn⁣∗​(DP)−1)\displaystyle\lambda\_{t}\exp(-\Lambda\_{t})\left(\sum\_{n=1}^{\infty}\left(\frac{\Lambda\_{t}^{n-1}}{(n-1)!}-\frac{\Lambda\_{t}^{n}}{n!}\right)F\_{X}^{n\*}(D\_{P})-1\right) |  |

and the assertion follows.
∎

Note that this result is also useful for calculating the probabilities that appear in ([3.9](https://arxiv.org/html/2510.17221v1#S3.E9 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) or ([3.10](https://arxiv.org/html/2510.17221v1#S3.E10 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")). More precisely, for t⩾0t\geqslant 0 we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ​(τ>t)\displaystyle\mathbb{Q}(\tau>t) | =𝔼ℚ​[ℚ​(τ>t|P)]\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\mathbb{Q}(\tau>t\,|\,P)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(∑n=0∞Λtnn!​exp⁡(−Λt)​FXn⁣∗​(Dp))​FP​(d​p)\displaystyle=\int\_{0}^{1}\left(\sum\_{n=0}^{\infty}\frac{\Lambda\_{t}^{n}}{n!}\exp(-\Lambda\_{t})F\_{X}^{n\*}(D\_{p})\right)F\_{P}(dp) |  |

The third step is to find a new conditional measure which we will denote as ℙν|P\mathbb{P}^{\nu|P}. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙν|Pd​ℙC|P|𝒞^t=exp⁡(−(1−ν)​Q​Lt+Λt​(1−(ℒ​fX)​((1−ν)​Q)))=η​(t).\displaystyle\frac{d\mathbb{P}^{\nu|P}}{d\mathbb{P}\_{C|P}}\Bigg{|}\_{\hat{\mathcal{C}}\_{t}}=\exp(-(1-\nu)QL\_{t}+\Lambda\_{t}(1-(\mathcal{L}f\_{X})((1-\nu)Q)))=\eta(t). |  | (4.18) |

It is easy to verify that the process η​(t)\eta(t) is an exponential ℙν|P\mathbb{P}^{\nu|P}-martingale.

By Proposition [4.8](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds"), we also find that that the process LtL\_{t} is a τ\tau-dependency under the conditional measure. As a fourth step, we prove that LtL\_{t} preserves its distribution with respect to the new measure, as it was in previous cases.

###### Proposition 4.9.

The process LtL\_{t} under the measure ℙν|P\mathbb{P}^{\nu|P} is a compound Poisson process with parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λtν|P=Λt​(ℒ​fX)​((1−ν)​Q),\displaystyle\Lambda^{\nu|P}\_{t}=\Lambda\_{t}(\mathcal{L}f\_{X})((1-\nu)Q), | FXν|P​(x)=exp⁡(−(1−ν)​Q​x)(ℒ​fX)​((1−ν)​Q)​FX​(x).\displaystyle F\_{X}^{\nu|P}(x)=\frac{\exp(-(1-\nu)Qx)}{(\mathcal{L}f\_{X})((1-\nu)Q)}F\_{X}(x). |  |

###### Proof.

Our claim easily follows from Proposition [4.3](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") with α=Q\alpha=Q and β=0\beta=0.
∎

The final step is similar to the ILP and ILA case. We define a new measure Q¯|P=ℙν|P⊗ℚF\overline{Q}\_{|P}=\mathbb{P}^{\nu|P}\otimes\mathbb{Q}\_{F} such that

|  |  |  |
| --- | --- | --- |
|  | d​ℚ¯d​ℚ|𝒢t=η​(t),\displaystyle\frac{d\overline{\mathbb{Q}}}{d\mathbb{Q}}\bigg{|}\_{\mathcal{G}\_{t}}=\eta(t), |  |

where η​(t)\eta(t) is defined by ([4.18](https://arxiv.org/html/2510.17221v1#S4.E18 "In 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")). Then we examine the inner expectation value in ([4.17](https://arxiv.org/html/2510.17221v1#S4.E17 "In 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")), which yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ|P\displaystyle\mathbb{E}^{\mathbb{Q}\_{|P}} | [Sτ1−ν​B​(0,τ)​𝟙τ⩽T]\displaystyle\left[S\_{\tau}^{1-\nu}B(0,\tau)\mathbb{1}\_{\tau\leqslant T}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ|P[exp(−(1−ν)QLt−ν∫0τrudu+(1−ν)σSWτ2\displaystyle=\mathbb{E}^{\mathbb{Q}\_{|P}}\bigg{[}\exp\bigg{(}-(1-\nu)QL\_{t}-\nu\int\_{0}^{\tau}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{\tau}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ν)(ακ1Λτ1+βκ2Λτ2−12τσS2))𝟙τ⩽T]\displaystyle\quad+(1-\nu)\left(\alpha\kappa\_{1}\Lambda\_{\tau}^{1}+\beta\kappa\_{2}\Lambda\_{\tau}^{2}-\tfrac{1}{2}\tau\sigma\_{S}^{2}\right)\bigg{)}\mathbb{1}\_{\tau\leqslant T}\bigg{]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼Q¯|P​[φ​(τ,Q)​exp⁡(−ν​∫0τru​𝑑u+(1−ν)​σS​Wτ2)​𝟙τ⩽T],\displaystyle=\mathbb{E}^{\overline{Q}\_{|P}}\bigg{[}\varphi(\tau,Q)\exp\bigg{(}-\nu\int\_{0}^{\tau}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{\tau}^{2}\bigg{)}\mathbb{1}\_{\tau\leqslant T}\bigg{]}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | φ​(t,q)=exp⁡(−Λt​(1−(ℒ​fX)​((1−ν)​q))+(1−ν)​((α+β)​κ​Λt−12​t​σS2)).\displaystyle\varphi(t,q)=\exp\left(-\Lambda\_{t}(1-(\mathcal{L}f\_{X})((1-\nu)q))+(1-\nu)\left((\alpha+\beta)\kappa\Lambda\_{t}-\tfrac{1}{2}t\sigma\_{S}^{2}\right)\right). |  |

Conditioning with τ\tau gives us

|  |  |  |
| --- | --- | --- |
|  | ∫0Tφ​(t,Q)​𝔼ℚF​[exp⁡(−ν​∫0τru​𝑑u+(1−ν)​σS​Wτ2)]​fτν|P​(t)​𝑑t.\displaystyle\int\_{0}^{T}\varphi(t,Q)\,\mathbb{E}^{\mathbb{Q}\_{F}}\left[\exp\bigg{(}-\nu\int\_{0}^{\tau}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{\tau}^{2}\bigg{)}\right]f\_{\tau}^{\nu|P}(t)\,dt. |  |

This expression is very similar with these obtained in the previous cases. Since no changes considering the financial measure were made and financial and catastrophic worlds are independent, we can write

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚF​[exp⁡(−ν​∫0τru​𝑑u+(1−ν)​σS​Wτ2)]=exp⁡(12​(1−ν)2​σS2​t)​P​(r0,t,θ¯r,m¯r,σ¯r),\displaystyle\mathbb{E}^{\mathbb{Q}\_{F}}\left[\exp\bigg{(}-\nu\int\_{0}^{\tau}r\_{u}\,du+(1-\nu)\sigma\_{S}W\_{\tau}^{2}\bigg{)}\right]=\exp\left(\tfrac{1}{2}(1-\nu)^{2}\sigma\_{S}^{2}t\right)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r}), |  |

as before.

Regarding ([4.17](https://arxiv.org/html/2510.17221v1#S4.E17 "In 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds")) and the above results, we obtain the final pricing formula:

|  |  |  |
| --- | --- | --- |
|  | ∫01(∫0Tφ​(t,q)​exp⁡(12​(1−ν)2​σS2​t)​P​(r0,t,θ¯r,m¯r,σ¯r)​fτν|p​(t)​𝑑t)​FP​(d​p),\displaystyle\int\_{0}^{1}\left(\int\_{0}^{T}\varphi(t,q)\,\exp\left(\tfrac{1}{2}(1-\nu)^{2}\sigma\_{S}^{2}t\right)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})\,f\_{\tau}^{\nu|p}(t)\,dt\right)F\_{P}(dp), |  |

where fτν|pf\_{\tau}^{\nu|p} follows the same formula to fτf\_{\tau} in Proposition [4.8](https://arxiv.org/html/2510.17221v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4.3. Proportional loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") with P=pP=p, and Λtν\Lambda\_{t}^{\nu} and FXνF\_{X}^{\nu} instead of Λt\Lambda\_{t} and FXF\_{X}.

Note that if we consider fixed proportional loss amounts, that is when P=p∈(0,1)P=p\in(0,1) with probability one, the above formula simplifies; for example the outer integral vanishes. We leave the details to the reader. ∎

## 5. Further possible generalizations

Regarding the results and methods of pricing gathered in this paper, one can generalise considered model for losses from three regions and more. It can be easily done for ILP and ILA. However, under the assumption of PLA, additional technical difficulties appear (they are primarily related to the proportion coefficients). In the following, we provide a result for the two former assumptions.

Consider RR different regions, where R=1,2,3,…R=1,2,3,\ldots, and RR aggregate loss processes defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ltr=∑k=1NtrXkr\displaystyle L\_{t}^{r}=\sum\_{k=1}^{N\_{t}^{r}}X\_{k}^{r} | for ​r=1,2,…,R,\displaystyle\text{for }r=1,2,\ldots,R, |  |

where X1r,X2r,X3r,…X\_{1}^{r},X\_{2}^{r},X\_{3}^{r},\ldots is a sequence of i.i.d. positive, continuous random variables with distribution functions FXrF\_{X}^{r} and densities fXrf\_{X}^{r}, independent from the Poisson process NtrN\_{t}^{r} with cumulative intensities Λtr=∫0tλur​𝑑u\smash{\Lambda\_{t}^{r}=\int\_{0}^{t}\lambda\_{u}^{r}\,du}.

Under ILP, the processes LtrL\_{t}^{r} and LtsL\_{t}^{s} are independent for different r,sr,s in the sense of pairwise independence of any two different random components therein. Under ILA, we assume that the processes NtrN\_{t}^{r} are equal for every rr and we denote them by NtN\_{t} and their cumulative intensity as Λt\Lambda\_{t}.

For positive thresholds D1,D2,…,DRD\_{1},D\_{2},\ldots,D\_{R} we put

|  |  |  |  |
| --- | --- | --- | --- |
|  | τr=min⁡{t⩾0:Ltr⩾Dr},\displaystyle\tau\_{r}=\min\{t\geqslant 0:L\_{t}^{r}\geqslant D\_{r}\}, | for ​r=1,2,…,R\displaystyle\text{for }r=1,2,\ldots,R |  |

and the trigger time for the multi-region CoCoCat bond is defined as

|  |  |  |
| --- | --- | --- |
|  | τ=min⁡{τr:r=1,2,…,R}.\displaystyle\tau=\min\{\tau\_{r}:r=1,2,\ldots,R\}. |  |

###### Theorem 5.1.

Risk-neutral price of multi-region CoCoCat for RR regions is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​I1+𝔼ℚ​I2+𝔼ℚ​I3.\displaystyle\mathbb{E}^{\mathbb{Q}}I\_{1}+\mathbb{E}^{\mathbb{Q}}I\_{2}+\mathbb{E}^{\mathbb{Q}}I\_{3}. |  |

The first and third component are described by ([3.9](https://arxiv.org/html/2510.17221v1#S3.E9 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) and ([3.10](https://arxiv.org/html/2510.17221v1#S3.E10 "In 3.1. CoCoCat bond’s mechanism. General pricing formula ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds")) while the second reads

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​I2=ζ​Z​S01−ν​∫0∞exp⁡(−12​ν​(1−ν)​t​σS2)​Φ​(t)​P​(r0,t,θ¯r,m¯r,σ¯r)​Fτν​(d​t),\displaystyle\mathbb{E}^{\mathbb{Q}}I\_{2}=\zeta ZS\_{0}^{1-\nu}\int\_{0}^{\infty}\exp\left(-\tfrac{1}{2}\nu(1-\nu)t\sigma\_{S}^{2}\right)\Phi(t)P(r\_{0},t,\bar{\theta}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r})F\_{\tau}^{\nu}(dt), |  |

where θ¯r,m¯r,σ¯r{\bar{\theta}}\_{r},\bar{m}\_{r},\bar{\sigma}\_{r} are described in Theorem [3.4](https://arxiv.org/html/2510.17221v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2. Main results ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds"). Moreover,

|  |  |  |
| --- | --- | --- |
|  | Φ​(t)={∏r=1Rexp(−Λtr(1−(ℒfXr)(αr(1−ν)))−(1−ν)(1−(ℒfXr)(αr))))for ILP,exp⁡(−Λt​(1−ν)​(1−∏r=1R(ℒ​fXr)​(αr))−∏r=1R(ℒ​fXr)​(αr​(1−ν)))for ILA,\displaystyle\Phi(t)=\begin{cases}\displaystyle{\prod\_{r=1}^{R}\exp\bigg{(}-\Lambda\_{t}^{r}\big{(}1-(\mathcal{L}f\_{X}^{r})(\alpha\_{r}(1-\nu)))-(1-\nu)(1-(\mathcal{L}f\_{X}^{r})(\alpha\_{r}))\big{)}\bigg{)}}&\text{for ILP},\\ \displaystyle{\exp\left(-\Lambda\_{t}(1-\nu)\left(1-\prod\_{r=1}^{R}(\mathcal{L}f\_{X}^{r})(\alpha\_{r})\right)-\prod\_{r=1}^{R}(\mathcal{L}f\_{X}^{r})(\alpha\_{r}(1-\nu))\right)}&\text{for ILA},\end{cases} |  |

and

|  |  |  |
| --- | --- | --- |
|  | Fτν​(t)={1−∏r=1R(exp⁡(−Λtν,r)​∑n=0∞(Λtν,r)nn!​(FXν,r)n⁣∗​(Dr))for ILP,1−exp⁡(−Λtν)​∑n=0∞((Λtν)nn!​∏r=1R(FXν,r)n⁣∗​(Dr))for ILA,\displaystyle F\_{\tau}^{\nu}(t)=\begin{cases}\displaystyle{1-\prod\_{r=1}^{R}\left(\exp(-\Lambda\_{t}^{\nu,r})\sum\_{n=0}^{\infty}\frac{(\Lambda\_{t}^{\nu,r})^{n}}{n!}(F\_{X}^{\nu,r})^{n\*}(D\_{r})\right)}&\text{for ILP},\\ \displaystyle{1-\exp(-\Lambda\_{t}^{\nu})\sum\_{n=0}^{\infty}\left(\frac{(\Lambda\_{t}^{\nu})^{n}}{n!}\prod\_{r=1}^{R}(F\_{X}^{\nu,r})^{n\*}(D\_{r})\right)}&\text{for ILA},\end{cases} |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λtν,r=Λtr​(ℒ​fXr)​(αr​(1−ν)),\displaystyle\Lambda\_{t}^{\nu,r}=\Lambda\_{t}^{r}(\mathcal{L}f\_{X}^{r})(\alpha\_{r}(1-\nu)), | Λtν=Λt​∏r=1R(ℒ​fXr)​(αr​(1−ν))\displaystyle\Lambda^{\nu}\_{t}=\Lambda\_{t}\prod\_{r=1}^{R}(\mathcal{L}f\_{X}^{r})(\alpha\_{r}(1-\nu)) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | FXν,r\displaystyle F\_{X}^{\nu,r} | =exp⁡(−αr​(1−ν)​x)(ℒ​fXr)​(αr​(1−ν))​FXr​(x),\displaystyle=\frac{\exp(-\alpha\_{r}(1-\nu)x)}{(\mathcal{L}f\_{X}^{r})(\alpha\_{r}(1-\nu))}F\_{X}^{r}(x), |  |

for r=1,2,…,Rr=1,2,\ldots,R

The proof of Theorem [5.1](https://arxiv.org/html/2510.17221v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5. Further possible generalizations ‣ Design and valuation of multi-region CoCoCat bonds") can be easily carried out by repeating the reasoning presented in Sections [4.1](https://arxiv.org/html/2510.17221v1#S4.SS1 "4.1. Independent loss process ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds") and [4.2](https://arxiv.org/html/2510.17221v1#S4.SS2 "4.2. Independent loss amounts ‣ 4. Risk-neutral pricing: proofs ‣ Design and valuation of multi-region CoCoCat bonds"). Note that by putting R=2R=2 we can retrieve results from Theorem [3.4](https://arxiv.org/html/2510.17221v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2. Main results ‣ 3. Risk-neutral pricing: analytic formulae ‣ Design and valuation of multi-region CoCoCat bonds") and for R=1R=1 both cases (ILP and ILA) are equivalent and the main result from [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] follows.

Another natural generalisation of this result would be redefining the trigger of CoCoCat bond. Let r0=1,2,…,Rr\_{0}=1,2,\dots,R and assume that the CoCoCat bond mechanism is activated when exactly r0r\_{0} out of RR thresholds are exceeded. In pricing, this definition would involve the distribution of r0r\_{0}th order statistic for RR random variables. Although it is mathematically doable, the authors are aware that such modification would not produce any neat formulae. The details are therefore left for the reader.

## 6. Numerical illustration

In this section, we investigate the behaviour of the price of multi-region CoCoCat bonds through numerical experiments. We analyse the price as a function of the initial capitals D1D\_{1} and D2D\_{2}, and the value of the parameter ν\nu of the conversion price KP=S0ν.K\_{P}=S\_{0}^{\nu}.

The parameters of the models were calibrated using data from the Property Claims Services (PCS). The chosen sample consisted of losses caused by 44 wind, thunderstorm, and winter storm events that occurred at the same time in Oklahoma and Texas between 1985 and 2011. Loss amounts were adjusted using the consumer price index.

In most of the events, the losses that occurred in Texas were higher than in Oklahoma. However, Oklahoma was not exempt from extreme losses and was heavily affected by tornadoes in May 1990 and May 2010, see Figure [1](https://arxiv.org/html/2510.17221v1#S6.F1 "Figure 1 ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds")(a). The highest losses in Texas were also caused by tornadoes: in April 1994 and April 2011, see Figure [1](https://arxiv.org/html/2510.17221v1#S6.F1 "Figure 1 ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds")(b). The box plots of loss amounts presented in Figure [1](https://arxiv.org/html/2510.17221v1#S6.F1 "Figure 1 ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds")(c) clearly show skewness in both samples and heavy tails of the losses.

![Refer to caption](x1.png)


Figure 1. Adjusted losses occurred in (a) Oklahoma and (b) Texas,
in billion USD, together with (c) their box plots.

Among log-normal, Pareto, gamma, Weibull, inverse Gaussian and generalised extreme value distributions, the former gave the smallest values of the Kolmogorov-Smirnov (KS), Cramer von Mises (CvM) and Anderson and Darling (AD) test statistics (for the description of the tests we refer to [[10](https://arxiv.org/html/2510.17221v1#bib.bib10)]). The log-normal distribution is given by the density:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=1x​σ​2​π​exp⁡(−(ln⁡(x)−μ)22​σ2),x>0,μ∈ℝ,σ>0.f(x)=\frac{1}{x\sigma\sqrt{2\pi}}\exp{\left(-\frac{\left(\ln(x)-\mu\right)^{2}}{2\sigma^{2}}\right)},\quad x>0,\;\mu\in\mathbb{R},\;\sigma>0. |  | (6.1) |

In Table [1](https://arxiv.org/html/2510.17221v1#S6.T1 "Table 1 ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds") parameters of the distribution fitted to the losses in each state and the total loss from both states are presented.

Table 1. Parameters of log-normal distribution fitted to data sample used in models with independent loss amounts (ILA) and proportional loss amounts (PLA).

| Model | State | Parameters of log-normal distribution |
| --- | --- | --- |
| ILA | OK | μ=−4.564\mu=-4.564, σ=1.813\sigma=1.813 |
| TX | μ=−2.439\mu=-2.439, σ=1.183\sigma=1.183 |
| PLA | total loss | μ=−1.477\mu=-1.477, σ=0.902\sigma=0.902 |

The timing of catastrophes was modelled by a homogeneous Poisson process with the annual intensity parameter λ=1.4\lambda=1.4. The value was estimated using the least squares method by comparing the mean value of the Poisson process 𝔼​N​(t)=Λ​t\mathbb{E}N(t)=\Lambda t with the aggregate number of events in our data set. Considering a small sample size, the homogeneous Poisson process gave a reasonable fit to the data with the following errors: MSE = 10.13, MAE = 2.53, MAPE = 30.6%.

For illustration purposes, we consider a 5-year CoCoCat bond, which pays quarterly coupons at an annual rate 10%10\% plus a risk-free rate (like LIBOR). If the bond is triggered, ζ=10%\zeta=10\% of the nominal is converted into the sponsor’s equity at price SτνS\_{\tau}^{\nu}, where SτS\_{\tau} is the price of the share at the trigger moment τ\tau and the parameter ν∈(0,1).\nu\in(0,1). For simplicity, we assume that the nominal is Z=1Z=1.

The Longstaff’s model with r0=0.02;θr=0.2,σr=0.03r\_{0}=0.02;\theta\_{r}=0.2,\sigma\_{r}=0.03 was used to model the interest rate process. The parameters of the stock price process were: S0=10,σs=0.2S\_{0}=10,\sigma\_{s}=0.2. The correlation coefficient of the share and interest rate processes was set to ρ=−0.5.\rho=-0.5.

### 6.1. Results for ILA models

![Refer to caption](x2.png)

Figure 2. Prices obtained for the ILA model for (a) ν=0.2\nu=0.2, (b) ν=0.5\nu=0.5, (c) ν=0.8\nu=0.8, with respect to D1D\_{1} and D2D\_{2} (in billion USD).

![Refer to caption](x3.png)

Figure 3. Prices obtained for the ILA model for different values of ν\nu for (a) D1=0.4D\_{1}=0.4, (b) D1=2D\_{1}=2, (c) D1=4D\_{1}=4 billion USD, with respect to D2D\_{2}.

We begin with the analysis of the ILA model, where losses from each state are described as independent random variables. The impact of losses on stock prices of the bond’s issuer is described by the parameters.

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=δ𝔼​[Xk1],β=δ𝔼​[Xk2],\alpha=\frac{\delta}{\mathbb{E}[X\_{k}^{1}]},\quad\beta=\frac{\delta}{\mathbb{E}[X\_{k}^{2}]}, |  | (6.2) |

where δ=0.02\delta=0.02, as in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)].

In Figure [3](https://arxiv.org/html/2510.17221v1#S6.F3 "Figure 3 ‣ 6.1. Results for ILA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds"), the price of the CoCoCat bond is presented as a function of D1D\_{1} and D2D\_{2} for the three chosen values of the parameter ν\nu. We can observe that as thresholds increase, so does the price of the bond. The higher D1D\_{1} and D2D\_{2}, the lower the probability of losses exceeding given thresholds, resulting in the payment of all coupons and the nominal. We also observe that as ν\nu increases, the price decreases, which is visible for small values of D2D\_{2}.
When the bond is triggered, ζ​Z\zeta Z is converted into the equity at conversion price SτνS\_{\tau}^{\nu}. For higher values of ν\nu, the owner of the bond gets fewer units of the share since the conversion cost is higher. Consequently, the total value of the shares obtained at the moment of conversion is smaller, explaining the decrease in the price of the CoCoCat bond.
In Figure [3](https://arxiv.org/html/2510.17221v1#S6.F3 "Figure 3 ‣ 6.1. Results for ILA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds") we can clearly see that the impact of the parameter ν\nu is weakening as the thresholds D1D\_{1} and D2D\_{2} increase, since the probability of conversion of the nominal to equity decreases.

### 6.2. Results for PLA models

Next, we move on to models with proportional loss amounts.
The total loss is divided according to the proportion PP, that is, for a common loss XkX\_{k}, the value of P​XKPX\_{K} is assigned to Oklahoma and (1−P)​Xk(1-P)X\_{k} to Texas.

For models with proportional loss amounts, the impact of losses on stock prices of the bond’s issuer is described by the parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=δ𝔼​[P​Xk],β=δ𝔼​[X​(1−P)],\alpha=\frac{\delta}{\mathbb{E}[PX\_{k}]},\quad\beta=\frac{\delta}{\mathbb{E}[X(1-P)]}, |  | (6.3) |

where δ=0.02\delta=0.02 as before.

The average proportion for historical data was found to be approximately equal to 0.380.38 and the box plot of the proportions between losses is presented in Figure [4](https://arxiv.org/html/2510.17221v1#S6.F4 "Figure 4 ‣ 6.2. Results for PLA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds")(a). In the model with constant PLA (cPLA), we assume that the proportion PP is equal to 0.380.38 with probability 1. We can interpret it as OK taking 38% of the loss and TX taking 62% of the total loss.

The price of the CoCoCat bond as a function of thresholds is presented in Figure [6](https://arxiv.org/html/2510.17221v1#S6.F6 "Figure 6 ‣ 6.2. Results for PLA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds"). Similarly as for the ILA model, the higher D1D\_{1} and D2D\_{2} are, the higher the price. We can observe that the value of the price quickly converges to the maximum value. Again, an increase in ν\nu causes a decrease in the price which is especially visible for smaller values of D1D\_{1} and D2D\_{2}, see Figure [6](https://arxiv.org/html/2510.17221v1#S6.F6 "Figure 6 ‣ 6.2. Results for PLA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds").

![Refer to caption](x4.png)


Figure 4. (a) Box plots for proportion between losses. (b) Normalized histogram of proportions compared with the density of fitted beta distribution.

In the random PLA (rPLA) model, we describe the proportion between losses by the beta distribution with density:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=xα−1​(1−x)β−1B​(α,β),x∈[0,1],α>0,β>0,f(x)=\frac{x^{\alpha-1}\left(1-x\right)^{\beta-1}}{B\left(\alpha,\beta\right)},\quad x\in[0,1],\;\alpha>0,\;\beta>0, |  | (6.4) |

where B​(x)B(x) is the beta function. Using the maximum likelihood method, the parameters α=2.1531\alpha=2.1531, β=3.5135\beta=3.5135 were fitted. The expected value of this variable is equal to 0.380.38, so it is the same as the constant proportion. The distribution fits the data well, see Figure [4](https://arxiv.org/html/2510.17221v1#S6.F4 "Figure 4 ‣ 6.2. Results for PLA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds")(b). Moreover, KS, CvM and AD tests did not reject the beta distribution hypothesis.

![Refer to caption](x5.png)

Figure 5. Prices obtained for the cPLA model for (a) ν=0.2\nu=0.2, (b) ν=0.5\nu=0.5, (a) ν=0.8\nu=0.8, with respect to D1D\_{1} and D2D\_{2} (in billion USD).

![Refer to caption](x6.png)

Figure 6. Prices obtained for the cPLA model for different values of ν\nu for (a) D1=0.4D\_{1}=0.4, (b) D1=2D\_{1}=2, (c) D1=4D\_{1}=4 billion USD, with respect to D2D\_{2}.

The prices of the CoCoCat bond for the rPLA model are presented in Figure [8](https://arxiv.org/html/2510.17221v1#S6.F8 "Figure 8 ‣ 6.3. Comparison of the models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds"). The prices behave similarly to the results for constant proportion, see Figure [6](https://arxiv.org/html/2510.17221v1#S6.F6 "Figure 6 ‣ 6.2. Results for PLA models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds"), but the increase in the price as the thresholds grow is slower. The parameter ν\nu also impacts the price, see Figure [8](https://arxiv.org/html/2510.17221v1#S6.F8 "Figure 8 ‣ 6.3. Comparison of the models ‣ 6. Numerical illustration ‣ Design and valuation of multi-region CoCoCat bonds"), especially for lower thresholds.

### 6.3. Comparison of the models

We take thresholds D1D\_{1} and D2D\_{2} as quantiles of order qq of the total loss. The prices naturally increase as we take higher quantiles of the distribution (since D1D\_{1} and D2D\_{2} are getting higher). We can also clearly observe the impact of ν\nu on the prices – the higher ν\nu, the lower the price.
The effect is the most visible for smaller values of thresholds D1D\_{1} and D2D\_{2}, when the possibility of conversion is much higher.

![Refer to caption](x7.png)

Figure 7. Prices obtained for the rPLA model for (a) ν=0.2\nu=0.2, (b) ν=0.5\nu=0.5, (a) ν=0.8\nu=0.8, with respect to D1D\_{1} and D2D\_{2} (in billion USD).

![Refer to caption](x8.png)

Figure 8. Prices obtained for the rPLA model for different values of ν\nu for (a) D1=0.4D\_{1}=0.4, (b) D1=2D\_{1}=2, (c) D1=4D\_{1}=4 billion USD, with respect to D2D\_{2}.

![Refer to caption](x9.png)


Figure 9. Prices obtained for the (a) ILA, (b) cPLA, (c) rPLA models, for D1D\_{1} and D2D\_{2} being qq-quantiles of respective loss distributions, for different ν\nu, with respect to qq.

## 7. Conclusions

Insurance-linked securities, in particular CAT bonds, is a dynamic and evolving market where multi-peril and multi-region structures play an increasingly significant role. These complex instruments represent a sophisticated convergence of insurance risk management and capital markets finance, driven by sponsors’ needs for comprehensive coverage and large-scale capacity, and investors’ search for yield and diversification.

A CoCoCat, introduced in [[9](https://arxiv.org/html/2510.17221v1#bib.bib9)] can help stabilise their issuers’ balance sheets in times of distress; particularly in times of extreme natural catastrophes potentially spurring on large non-independent insurance-related losses.
In this paper, we addressed a novel insurance-linked instrument which is in the form of a contingent convertible bond (CoCoCat bond) with a trigger linked to the occurrence of predefined natural catastrophes in different regions. To this end, we constructed a pricing model that incorporated different dependence scenarios between regions.

First, we introduced a general 2D model. This comprehensive model is designed to capture both financial market risk and catastrophe risk variables. The financial market component is modelled using classical Black-Scholes dynamics, incorporating a stochastic interest-rate process, for which Longstaff’s model is specifically chosen. The catastrophe risk component was addressed by modelling a 2D aggregate loss process, which can be represented by various compound Poisson processes.

Then, we proposed three specialised cases of modelling the aggregate loss processes, which are crucial for the subsequent pricing formulae, namely

1. (1)

   ILP: This model assumes that losses originate from two distinct regions and that these losses occur with different frequencies. Crucially, under ILP, the variables representing the number of losses and the loss amounts in the two regions are considered pairwise independent, leading to independent aggregate loss processes for each region.
2. (2)

   ILA: In this scenario, it is assumed that losses in the two different regions occur simultaneously, meaning that they share the same loss frequency. However, the amounts of these losses (Xk1X\_{k}^{1} and Xk2X\_{k}^{2}) are independent of each other.
3. (3)

   PLA: This model also assumes that losses occur at the same time. The distinguishing feature here is that the loss amounts themselves are split proportionally between the two regions. Two sub-types were considered:

   * •

     cPLA: The proportion of loss allocated to each region is fixed and deterministic.
   * •

     rPLA: The proportion of loss is a random variable, independent of the loss amounts and their frequency. For this case, we considered the beta distribution.

Next, for all considered cases, we derived the risk-neutral pricing formulas using change-of-measure techniques. We were able to find intuitive and analytical expressions for the prices. An exponential
change of measure allowed us to separately deal with financial markets as well as catastrophe-risk variables, and a Girsanov-like transformation allowed us to synthetically remove a Brownian motion from the expectation containing two correlated Brownian motions.

We arrived at an analytical expression for the conversion feature (and hence the price) which only required simulation of the loss process in order to empirically estimate the distribution of the time-of-trigger of the equity conversion feature. We note that Monte Carlo simulation could be used to estimate the value of the conversion feature of the CoCoCat directly. However, our simplification to an analytical formula has more in its favour, since only one process had to be simulated.

We also fitted the model to the natural catastrophe data provided by Property Claim Services and investigated the influence of the dependence on the bond prices. We presented numerical experiments as a first foray into the price behaviour of the CoCoCat. Gaining an understanding of the IL CoCoCat price behaviour, for varying parameters, is crucial in the design stage of such an instrument.

The prices we obtained in our analyses were in accordance with intuition: the higher the threshold level of the IL CoCoCat, the greater the price.
We also found that the conversion fraction significantly impacts the value of the conversion feature; namely, the lower the conversion factor, the higher the price. Finally, we discovered that the prices under different dependence scenarios vary. For the choices of parameters considered, the independence scenario yielded the lowest prices. This justifies the need to choose the right approach. Finally, we note that other dependence scenarios can also be analysed, but a key advantage of the introduced models is their ability to produce simple pricing formulas with parameters that can be readily estimated from loss data.

## CRediT authorship contribution statement

Jacek Wszoła: Writing – original draft, Formal analysis, Methodology, Validation, Proofs. Krzysztof Burnecki: Writing – review & editing, Conceptualization, Methodology, Validation, Supervision. Marek Teuerle: Writing – review & editing, Conceptualization, Methodology, Validation, Supervision. Martyna Zdeb: Writing – Original Draft, Software, Visualization.

## References

* [1]

  G. Bakshi and D. Madan.
  Average rate claims with emphasis on catastrophe loss options.
  Journal of Financial and Quantitative Analysis, 37(1):93–115, 2002.
* [2]

  P. Barrieu and L. Albertini.
  The Handbook of Insurance-Linked Securities.
  John Wiley & Sons, 2010.
* [3]

  Y. Baryshnikov, A. Mayo, and D. R. Taylor.
  Pricing of CAT bonds.
  Working paper, 1998.
* [4]

  D. Bauer, M. Börger, and J. Ruß.
  On the pricing of longevity-linked securities.
  Insurance: Mathematics and Economics, 46(1):139–149, 2010.
* [5]

  A. Braun.
  Pricing catastrophe swaps: A contingent claims approach.
  Insurance: Mathematics and Economics, 49(3):520–536, 2011.
* [6]

  A. Braun.
  Pricing in the primary market for cat bonds: new empirical evidence.
  Journal of Risk and Insurnace, 83(4):811–847, 2016.
* [7]

  A. Braun, H. Schmeiser, and F. Schreiber.
  Cyber insurance-linked securities.
  ASTIN Bulletin: The Journal of the IAA, 52(3):965–1003, 2022.
* [8]

  K. Burnecki and M. N. Giuricich.
  Stable weak approximation at work in index-linked catastrophe bond pricing.
  Risks, 5(4), 2017.
* [9]

  K. Burnecki, M. N. Giuricich, and Z. Palmowski.
  Valuation of contingent convertible catastrophe bonds – the case for equity conversion.
  Insurance Mathematics and Economics, 88:238–254, 2019.
* [10]

  K. Burnecki, J. Janczura, and R. Weron.
  Building loss models.
  In P. Čižek, W. Härdle, and R. Weron, editors, Statistical Tools for Finance and Insurance, 2nd Edition, pages 293–328. Springer, 2011.
* [11]

  K. Burnecki, M. A. Teuerle, and M. Zdeb.
  Pricing of insurance-linked securities: A multi-peril approach.
  Journal of Mathematics in Industry, 14(1):14, 2024.
* [12]

  E. Canabarro, M. Finkemeier, R. R. Anderson, and F. Bendimerad.
  Analyzing insurance-linked securities.
  The Journal of Risk Finance, 1(2):49–75, 2000.
* [13]

  P. Carayannopoulos and M. F. Perez.
  Diversification through catastrophe bonds: lessons from the subprime financial crisis.
  The Geneva Papers on Risk and Insurance-Issues and Practice, 40(1):1–28, 2015.
* [14]

  A. Chakrabatu.
  Insurance linked securities.
  In K. Mitchell-Wallace, M. Foote, J. Hillier, and M. Jones, editors, Natural Catastrophe Risk Management and Modelling: A Practitioner’s Guide, pages 158–167. John Wiley & Sons, New York, 2017.
* [15]

  C. W. Chang and J. S. Chang.
  An Integrated Approach to Pricing Catastrophe Reinsurance.
  Risks, 5(3):51, 2017.
* [16]

  R. Chen, M. Herrmann, L. Hong, and M. Yu.
  Pricing catastrophe bonds – a probabilistic machine learning approach.
  arXiv preprint arXiv:2405.00697, May 2024.
* [17]

  S. H. Cox and H. W. Pedersen.
  Catastrophe risk bonds.
  North American Actuarial Journal, 4(4):56–82, 2000.
* [18]

  J. D. Cummins and M. A. Weiss.
  Convergence of insurance and financial markets: Hybrid and securitized risk-transfer solutions.
  Journal of Risk and Insurnace., 76(3):493–545, 2009.
* [19]

  A. Dassios and J. Jang.
  Pricing of catastrophe reinsurance and derivatives using the Cox process with shot noise intensity.
  Finance and Stochastics, 7(1):73–95, 2003.
* [20]

  G. Deligiannakis, A. Zimbidis, and I. Papanikolaou.
  Earthquake loss and solvency capital requirement calculation using a fault-specific catastrophe model.
  The Geneva Papers on Risk and Insurance - Issues and Practice, 48(4):821–846, 2023.
* [21]

  D. Domfeh and S. Safarveisi.
  Catnet: A geometric deep learning approach for cat bond spread prediction in the primary market, 2025.
* [22]

  M. J. Flannery.
  Stabilizing large financial institutions with contingent capital certificates.
  Quarterly Journal of Finance, 6(02):1650006, 2016.
* [23]

  M. Giuricich and K. Burnecki.
  Modelling of left-truncated heavy-tailed data with application to catastrophe bond pricing.
  Physica A: Statistical Mechanics and its Applications, 525:498–513, 2019.
* [24]

  M. Gürtler, M. Hibbeln, and C. Winkelvos.
  The impact of the financial crisis and natural catastrophes on CAT bonds.
  Journal of Risk and Insurance, 83(3):579–612, 2016.
* [25]

  T. Götze, M. Gürtler, and E. Witowski.
  Improving cat bond pricing models via machine learning.
  Journal of Asset Management, 21:428–446, 09 2020.
* [26]

  B. Hagendorff, J. Hagendorff, and K. Keasey.
  The impact of mega-catastrophes on insurers: An exposure-based analysis of the US homeowners’ insurance market.
  Risk Analysis, 35(1):157–173, 2015.
* [27]

  W. K. Härdle and B. L. Cabrera.
  Calibrating CAT bonds for Mexican earthquakes.
  Journal of Risk and Insurance, 77(3):625–650, 2010.
* [28]

  R. E. Hoyt and K. A. McCullough.
  Catastrophe insurance options: Are they zero-beta assets?
  Journal of Insurance Issues, 22:147–163, 1999.
* [29]

  S. Jaimungal and T. Wang.
  Catastrophe options with stochastic interest rates and compound Poisson losses.
  Insurance: Mathematics and Economics, 38(3):469–483, 2006.
* [30]

  M. Jeanblanc, M. Yor, and M. Chesney.
  Mathematical methods for financial markets.
  Springer Science & Business Media, 2009.
* [31]

  M. Lane.
  Regressions and machine learning - some observations, some lessons.
  Lane Financial LLC, 2018.
* [32]

  M. Lane and R. Beckwith.
  The loss file - natural catastrophe ils issues 2001-2020.
  Lane Financial LLC, 2021.
* [33]

  M. N. Lane.
  Rationale and results with the LFC cat bond pricing model.
  Lane Financial LLC, Chicago, 2003.
* [34]

  M. N. Lane and R. G. Beckwith.
  The natural catastrophe ils market, 2001-2023 and its analysis.
  Technical report, Lane Financial LLC, March 2024.
* [35]

  J. P. Lee and M. T. Yu.
  Pricing default-risky CAT bonds with moral hazard and basis risk.
  Journal of Risk and Insurnace, 69:25–44, 2002.
* [36]

  J. P. Lee and M. T. Yu.
  Valuation of catastrophe reinsurance with catastrophe bonds.
  Insurance: Mathematics and Economics, 41(2):264–278, 2007.
* [37]

  F. Lindskog and A. J. McNeil.
  Common poisson shock models: Applications to insurance and credit risk modelling.
  ASTIN Bulletin, 33(2):209–238, 2003.
* [38]

  H. Liu, Q. Tang, and Z. Yuan.
  Indifference pricing of insurance-linked securities in a multi-period model.
  European Journal of Operational Research, 289(2):793–805, 2021.
* [39]

  E. Louloudis and A. Zimbidis.
  Robust modeling of earthquake catastrophe risk for insurance: An integrated approach incorporating active faults and an epidemic-type model.
  ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part A: Civil Engineering, 10:188, 2024.
* [40]

  Z. G. Ma and C. Q. Ma.
  Pricing catastrophe risk bonds: A mixed approximation method.
  Insurance: Mathematics and Economics, 52(2):243–254, 2013.
* [41]

  V. Manathunga and V. Novozhilov.
  Effect of earthquake sequences on risk-based catastrophe bond pricing.
  Risks, 11(9):156, 2023.
* [42]

  R. C. Merton.
  Option pricing when underlying stock returns are discontinuous.
  Journal of Financial Economics, 3(1):125–144, 1976.
* [43]

  H. K. Mistry, A. Hernandez, P. Guéguen, and D. Lombardi.
  Effect of earthquake sequences on risk-based catastrophe bond pricing.
  Risk Analysis, 44(9):2270–2285, 2024.
* [44]

  C. Morana and G. Sbrana.
  Climate change implications for the catastrophe bonds market: An empirical analysis.
  Economic Modelling, 81:274–294, 2019.
* [45]

  P. Nowak and M. Romaniuk.
  Pricing and simulations of catastrophe bonds.
  Insurance: Mathematics and Economics, 52(1):18–28, 2013.
* [46]

  D. Papachristou.
  Statistical Analysis of the Spreads of Catastrophe Bonds at the Time of Issue.
  Working Paper, presented at the 39th ASTIN Colloquium., 2009.
* [47]

  E. V. Petracou, A. Xepapadeas, and A. N. Yannacopoulos.
  Decision making under model uncertainty: Fréchet–Wasserstein mean preferences.
  Management Science, 68:1195–1211, 2021.
* [48]

  S. Safarveisi, D. Domfeh, and A. Chatterjee.
  Catastrophe bond pricing under the renewal process.
  Scandinavian Actuarial Journal, 0(0):1–28, 2025.
* [49]

  Swiss Re Capital Markets.
  Insurance-linked securities market insights february 2024.
  Technical report, Swiss Re, February 2024.
* [50]

  SwissRe.
  sigma 2/2020: Natural catastrophes in times of economic accumulation and climate change, 2020.
  Zurich, Switzerland.
* [51]

  L. Tang, C. Ling, and X. Wen.
  Pricing multi-event triggered catastrophe bonds based on copula–pot model.
  Risks, 11(5):97, 2023.
* [52]

  V. E. Vaugirard.
  Pricing catastrophe bonds by an arbitrage approach.
  The Quarterly Review of Economics and Finance, 43(1):119–132, 2003.
* [53]

  S. S. Wang.
  Cat bond pricing using probability transforms.
  Geneva Papers, 278:19–29, 2004.
* [54]

  B. Wei, Y. Liu, and Y. Hou.
  Pricing hybrid-triggered catastrophe bonds based on copula–EVT model.
  Quantitative Finance and Economics, 6(1):137–154, 2022.
* [55]

  A. A. Zimbidis, N. E. Frangos, and A. A. Pantelous.
  Modeling earthquake risk via extreme value theory and pricing the respective catastrophe bonds.
  ASTIN Bulletin, 37(1):163–184, 2007.