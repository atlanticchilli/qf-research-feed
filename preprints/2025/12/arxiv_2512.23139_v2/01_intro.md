---
authors:
- Fabio Bellini
- Muqiao Huang
- Qiuqi Wang
- Ruodu Wang
doc_id: arxiv:2512.23139v2
family_id: arxiv:2512.23139
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Lambda Expected Shortfall
url_abs: http://arxiv.org/abs/2512.23139v2
url_html: https://arxiv.org/html/2512.23139v2
venue: arXiv q-fin
version: 2
year: 2025
---


Fabio Bellini
Department of Statistics and Quantitative Methods, University of Milano-Bicocca, Italy. fabio.bellini@unimib.it
  
Muqiao Huang
Department of Statistics and Actuarial Science, University of Waterloo, Canada. m5huang@uwaterloo.ca
  
Qiuqi Wang
Maurice R. Greenberg School of Risk Science, Georgia State University, USA. qwang30@gsu.edu
  
Ruodu Wang
Department of Statistics and Actuarial Science, University of Waterloo, Canada. wang@uwaterloo.ca

###### Abstract

The Lambda Value-at-Risk (Λ\Lambda-VaR\mathrm{VaR}) is a generalization of the Value-at-Risk (VaR), which has been actively studied in quantitative finance. Over the past two decades, the Expected Shortfall (ES) has become one of the most important risk measures alongside VaR because of its various desirable properties in the practice of optimization, risk management, and financial regulation. Analogously to the intimate relation between ES and VaR, we introduce the Lambda Expected Shortfall (Λ\Lambda-ES\mathrm{ES}), as a generalization of ES and a counterpart to Λ\Lambda-VaR\mathrm{VaR}.
Our definition of Λ\Lambda-ES\mathrm{ES}
has an explicit formula and many convenient properties, and we show that it is the smallest quasi-convex and law-invariant risk measure dominating Λ\Lambda-VaR\mathrm{VaR} under mild assumptions. We examine further properties of Λ\Lambda-ES, its dual representation, and related optimization problems.

Keywords: Lambda Value-at-Risk, quantiles, Expected Shortfall, quasi-convexity, dual representation

## 1 Introduction

Financial institutions and regulators make use of sophisticated tools to quantify potential losses and manage financial exposures effectively. Among the most widely adopted risk measures are the Value-at-Risk (VaR) and the Expected Shortfall (ES), each with distinct theoretical properties and practical implications.
VaR has long served as a standard for risk assessment due to its intuitive interpretability. However, its well-documented limitations, such as the lack of subadditivity and non-convexity for general loss distributions and inability of capturing tail risk (see e.g., Daníelsson et al., [2001](https://arxiv.org/html/2512.23139v2#bib.bib10); McNeil et al., [2015](https://arxiv.org/html/2512.23139v2#bib.bib34); Embrechts et al., [2018](https://arxiv.org/html/2512.23139v2#bib.bib14)), have spurred the development of more robust alternatives. ES, also known as the Conditional Value-at-Risk (CVaR), emerged as the most popular alternative, with desirable features such as coherence (Artzner et al., [1999](https://arxiv.org/html/2512.23139v2#bib.bib2); Acerbi and Tasche, [2002](https://arxiv.org/html/2512.23139v2#bib.bib1)), convexity (Föllmer and Schied, [2002](https://arxiv.org/html/2512.23139v2#bib.bib19); Frittelli and Rosazza Gianin, [2002](https://arxiv.org/html/2512.23139v2#bib.bib22)), optimization properties (Rockafellar and Uryasev, [2002](https://arxiv.org/html/2512.23139v2#bib.bib35); Embrechts et al., [2022](https://arxiv.org/html/2512.23139v2#bib.bib15)),
and axiomatization via portfolio concentration (Wang and Zitikis, [2021](https://arxiv.org/html/2512.23139v2#bib.bib39)),
although it suffers from the lack of elicitability (Gneiting, [2011](https://arxiv.org/html/2512.23139v2#bib.bib23); Ziegel, [2016](https://arxiv.org/html/2512.23139v2#bib.bib40); Kou and Peng, [2016](https://arxiv.org/html/2512.23139v2#bib.bib28); Fissler and Ziegel, [2016](https://arxiv.org/html/2512.23139v2#bib.bib18)).

As a flexible generalization of VaR, the class of Lambda Value-at-Risk (Λ\Lambda-VaR) was introduced by Frittelli et al. ([2014](https://arxiv.org/html/2512.23139v2#bib.bib21)). The class of Λ\Lambda-VaR offers enhanced adaptability for modeling diverse risk preferences and regulatory contexts beyond a fixed confidence level.
Λ\Lambda-VaR is found to satisfy several useful properties in finance, including monotonicity, cash subadditivity, elicitability (Bellini and Bignozzi, [2015](https://arxiv.org/html/2512.23139v2#bib.bib3)), robustness (Burzoni et al., [2017](https://arxiv.org/html/2512.23139v2#bib.bib6)), and quasi-star-shapeness (Han et al., [2025](https://arxiv.org/html/2512.23139v2#bib.bib25)).
Bellini and Peri ([2022](https://arxiv.org/html/2512.23139v2#bib.bib4)) obtained an axiomatic characterization of Λ\Lambda-VaR, in particular justifying the choice of Λ\Lambda to be a (weakly) decreasing function.
As a risk measure,
Λ\Lambda-VaR has also been studied from practical aspects such as estimation and backtesting (Hitaj et al., [2018](https://arxiv.org/html/2512.23139v2#bib.bib26); Corbetta and Peri, [2018](https://arxiv.org/html/2512.23139v2#bib.bib9)), distributionally robust optimizations (Han and Liu, [2025](https://arxiv.org/html/2512.23139v2#bib.bib24)), capital allocations (Ince et al., [2022](https://arxiv.org/html/2512.23139v2#bib.bib27); Liu, [2025](https://arxiv.org/html/2512.23139v2#bib.bib32)), and optimal insurance problems (Boonen et al., [2025](https://arxiv.org/html/2512.23139v2#bib.bib5)).
While Λ\Lambda-VaR successfully broadens the scope of VaR, it retains the essential drawbacks of VaR for not being convex and not being able to capture tail risk. A natural remedy for the problem is to introduce an equally flexible generalization of ES as an alternative to Λ\Lambda-VaR. A suitable way of defining such a risk measure that preserves its desirable properties and strong theoretical foundations has not been found.

This paper addresses this gap by introducing the Lambda Expected Shortfall (Λ\Lambda-ES), a natural counterpart to Λ\Lambda-VaR.
There are many potential ways to generalize ES to a class of risk measures parametrized by a function Λ\Lambda.
A key consideration in ES and its generalization is its consistency with respect to portfolio diversification, modelled via convexity by Föllmer and Schied ([2002](https://arxiv.org/html/2512.23139v2#bib.bib19)); Frittelli and Rosazza Gianin ([2002](https://arxiv.org/html/2512.23139v2#bib.bib22)).
For general risk measures, Cerreia-Vioglio et al. ([2011](https://arxiv.org/html/2512.23139v2#bib.bib8)) argued that diversification preferences should be modelled by quasi-convexity, which is equivalent to convexity for monetary risk measures.
Keeping this property as our fundamental requirement for a generalization of ES, we find that there is one formulation that has the most advantages, inspired by a recent Λ\Lambda-VaR representation result of Han et al. ([2025](https://arxiv.org/html/2512.23139v2#bib.bib25)).
For a decreasing function Λ\Lambda, we define Λ\Lambda-ES of a random variable XX by

|  |  |  |  |
| --- | --- | --- | --- |
|  | supx∈ℝ(ESΛ​(x)​(X)∧x).\sup\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\wedge x\right). |  | (1) |

We demonstrate that Λ\Lambda-ES defined in ([1](https://arxiv.org/html/2512.23139v2#S1.E1 "In 1 Introduction ‣ Lambda Expected Shortfall")) possesses several critical properties (Proposition [2](https://arxiv.org/html/2512.23139v2#Thmproposition2 "Proposition 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")), analogous to those that establish ES as an improved alternative to VaR. More importantly,
based on a new result on the domination of ES over VaR (Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")), we show that Λ\Lambda-ES is the smallest quasi-convex and law-invariant risk measure that dominates Λ\Lambda-VaR (Theorem [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")). This result extends the classic dominance between VaR and ES (Delbaen, [2012](https://arxiv.org/html/2512.23139v2#bib.bib11); Föllmer and Schied, [2016](https://arxiv.org/html/2512.23139v2#bib.bib20)).

Beyond the foundational definition and properties of Λ\Lambda-ES, which are the topics of Section [3](https://arxiv.org/html/2512.23139v2#S3 "3 Lambda ES ‣ Lambda Expected Shortfall"), we proceed to conduct a comprehensive analysis of this new class of risk measures. In Section [4](https://arxiv.org/html/2512.23139v2#S4 "4 Dual representation ‣ Lambda Expected Shortfall"), we obtain a dual representation of Λ\Lambda-ES (Theorem [3](https://arxiv.org/html/2512.23139v2#Thmtheorem3 "Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall")), offering deeper insights into its theoretical structure and connections to quasi-convex cash-subadditive risk measures. In Section [5](https://arxiv.org/html/2512.23139v2#S5 "5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall"), we explore the properties of Λ\Lambda-ES in optimization problems, both as an objective function to minimize and as a constraint to impose, and analyze various forms of convexity in relevant reformulations of ES optimization problems.
In Section [6](https://arxiv.org/html/2512.23139v2#S6 "6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall"), results are naturally extended to the space L1L^{1} of integrable random variables, sometimes under slightly stronger assumptions.
Section [7](https://arxiv.org/html/2512.23139v2#S7 "7 Conclusion ‣ Lambda Expected Shortfall") concludes the paper.
Some alternative potential formulations for Λ\Lambda-ES are discussed in Appendix [A](https://arxiv.org/html/2512.23139v2#A1 "Appendix A Other possible formulations of Lambda ES ‣ Lambda Expected Shortfall"), demonstrating why our proposed definition is the most robust, theoretically consistent, and desirable for risk management applications.

## 2 VaR, Lambda VaR and ES

### 2.1 Risk measures

Let L0L^{0} be the space of all random variables on an atomless probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), L1L^{1} be the space of all random variables with finite mean, and L∞L^{\infty} be the set of all essentially bounded random variables.
Write ℝ¯=[−∞,∞]\overline{\mathbb{R}}=[-\infty,\infty] and ℝ+=[0,∞)\mathbb{R}\_{+}=[0,\infty). For any n∈ℕn\in\mathbb{N}, denote by [n]={1,…,n}[n]=\{1,\dots,n\}. For any x,y∈ℝ¯x,y\in\overline{\mathbb{R}}, write x∧y=min⁡{x,y}x\wedge y=\min\{x,y\}, x∨y=max⁡{x,y}x\vee y=\max\{x,y\}, x+=x∨0x\_{+}=x\vee 0, and x−=x∧0x\_{-}=x\wedge 0. For any function f:ℝ→ℝf:\mathbb{R}\to\mathbb{R} and x∈ℝx\in\mathbb{R}, we write f​(x−)=limy↑xf​(y)f(x-)=\lim\_{y\uparrow x}f(y) and f​(x+)=limy↓xf​(y)f(x+)=\lim\_{y\downarrow x}f(y), if they exist. Let ℳc​(ℝ)\mathcal{M}\_{c}(\mathbb{R}) denote the set of compactly supported distributions on ℝ\mathbb{R}.

We start with risk measures that are used to quantify risks. A risk measure is a mapping ρ:𝒳→ℝ¯\rho:\mathcal{X}\to\overline{\mathbb{R}}, where 𝒳\mathcal{X} is the space of random variables where ρ\rho is defined. Below, we list several common properties that a risk measure may satisfy, and their financial interpretation is well documented in the literature (e.g., Artzner et al., [1999](https://arxiv.org/html/2512.23139v2#bib.bib2); Föllmer and Schied, [2002](https://arxiv.org/html/2512.23139v2#bib.bib19); Frittelli and Rosazza Gianin, [2002](https://arxiv.org/html/2512.23139v2#bib.bib22)). The risk measure ρ\rho is called a *monetary risk measure* if it satisfies

* –

  *Monotonicity:* ρ​(X)⩾ρ​(Y)\rho(X)\geqslant\rho(Y) for all X,Y∈𝒳X,Y\in\mathcal{X} and X⩾YX\geqslant Y almost surely;
* –

  *Cash additivity (or translation invariance):* ρ​(X+m)=ρ​(X)+m\rho(X+m)=\rho(X)+m for all X∈𝒳X\in\mathcal{X} and m∈ℝm\in\mathbb{R}.

A monetary risk measure is often required to satisfy

* –

  *Normalization:* ρ​(t)=t\rho(t)=t for all t∈ℝt\in\mathbb{R}.

A monetary risk measure is called *coherent* if it further satisfies111Whenever convexity or subadditivity is discussed, the range of ρ\rho includes at most one of ∞\infty and −∞-\infty to avoid ∞−∞\infty-\infty.

* –

  *Positive homogeneity:* ρ​(γ​X)=γ​ρ​(X)\rho(\gamma X)=\gamma\rho(X) for all X∈𝒳X\in\mathcal{X} and γ∈(0,∞)\gamma\in(0,\infty);
* –

  *Subadditivity:* ρ​(X+Y)⩽ρ​(X)+ρ​(Y)\rho(X+Y)\leqslant\rho(X)+\rho(Y) for all X,Y∈𝒳X,Y\in\mathcal{X};

whereas a monetary risk measure is called a *convex risk measure* if it further satisfies

* –

  *Convexity:* ρ​(γ​X+(1−γ)​Y)⩽γ​ρ​(X)+(1−γ)​ρ​(Y)\rho(\gamma X+(1-\gamma)Y)\leqslant\gamma\rho(X)+(1-\gamma)\rho(Y) for all X,Y∈𝒳X,Y\in\mathcal{X} and γ∈[0,1]\gamma\in[0,1].

Convexity is motivated by diversification effects in risk measurement.
To incorporate non-constant interest rates, El Karoui and Ravanelli ([2009](https://arxiv.org/html/2512.23139v2#bib.bib12)) relaxes cash additivity to

* –

  *Cash subadditivity:* ρ​(X+m)⩽ρ​(X)+m\rho(X+m)\leqslant\rho(X)+m for all X∈𝒳X\in\mathcal{X} and m∈ℝ+m\in\mathbb{R}\_{+}.

For cash-subadditive risk measures, Cerreia-Vioglio et al. ([2011](https://arxiv.org/html/2512.23139v2#bib.bib8)) argued that the diversification effect is characterized by

* –

  *Quasi-convexity:* ρ​(γ​X+(1−γ)​Y)⩽max⁡{ρ​(X),ρ​(Y)}\rho(\gamma X+(1-\gamma)Y)\leqslant\max\{\rho(X),\rho(Y)\} for all X,Y∈𝒳X,Y\in\mathcal{X} and γ∈[0,1]\gamma\in[0,1].

Many commonly used convex risk measures (such as the Expected Shortfall defined below) also satisfy law invariance and concavity with respect to distribution mixtures.

* –

  *Law invariance:* ρ​(X)=ρ​(Y)\rho(X)=\rho(Y) for all X,Y∈𝒳X,Y\in\mathcal{X} with the same distribution.
* –

  *Concavity* (resp. *quasi-concavity*) *in mixtures:* ρ\rho is law invariant and the function F↦ρ​(XF)F\mapsto\rho(X\_{F}) on ℳc​(ℝ)\mathcal{M}\_{c}(\mathbb{R}) is concave (resp. quasi-concave), where XFX\_{F} is a random variable with distribution F∈ℳc​(ℝ)F\in\mathcal{M}\_{c}(\mathbb{R}).

Further properties of risk measures that we will consider in this paper include

* –

  *SSD-consistency:* ρ​(X)⩾ρ​(Y)\rho(X)\geqslant\rho(Y) for all X,Y∈𝒳X,Y\in\mathcal{X} and X⪰icxYX\succeq\_{\rm icx}Y.222Here, SSD represents second-order stochastic dominance. For X,Y∈𝒳X,Y\in\mathcal{X}, we say that XX *dominates* YY in *increasing convex order*, denoted by X⪰icxYX\succeq\_{\rm icx}Y, if 𝔼​[f​(X)]⩾𝔼​[f​(Y)]\mathbb{E}[f(X)]\geqslant\mathbb{E}[f(Y)] for all increasing and convex functions f:ℝ→ℝf:\mathbb{R}\to\mathbb{R}. SSD-consistent monetary risk measures are characterized by Mao and Wang ([2020](https://arxiv.org/html/2512.23139v2#bib.bib33)).
* –

  *L1L^{1}-continuity:* ρ​(Xn)→ρ​(X)\rho(X\_{n})\to\rho(X) for all X,X1,X2​⋯∈𝒳X,X\_{1},X\_{2}\dots\in\mathcal{X} and Xn→L1XX\_{n}\stackrel{{\scriptstyle L^{1}}}{{\to}}X as n→∞n\to\infty.

### 2.2 VaR and Lambda VaR

The *Value-at-Risk* (VaR) at level α∈[0,1]\alpha\in[0,1] is defined as the left quantile, namely,

|  |  |  |
| --- | --- | --- |
|  | VaRα​(X)=inf{x∈ℝ:ℙ​(X⩽x)⩾α},X∈L0.\mathrm{VaR}\_{\alpha}(X)=\inf\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)\geqslant\alpha\},~~~X\in L^{0}. |  |

Similarly, the *upper Value-at-Risk* (VaR+\mathrm{VaR}^{+}) at level α∈[0,1]\alpha\in[0,1] is defined as the right quantile:

|  |  |  |
| --- | --- | --- |
|  | VaRα+​(X)=inf{x∈ℝ:ℙ​(X⩽x)>α},X∈L0.\mathrm{VaR}^{+}\_{\alpha}(X)=\inf\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)>\alpha\},~~~X\in L^{0}. |  |

Using these formulations, for any X∈L0X\in L^{0}, VaR0​(X)=−∞\mathrm{VaR}\_{0}(X)=-\infty, VaR1+​(X)=∞\mathrm{VaR}^{+}\_{1}(X)=\infty, VaR1​(X)\mathrm{VaR}\_{1}(X) is the essential supremum of XX,
and VaR0+​(X)\mathrm{VaR}^{+}\_{0}(X) is the essential infimum of XX. Moreover, VaRα​(X),VaRα+​(X)∈ℝ\mathrm{VaR}\_{\alpha}(X),\mathrm{VaR}^{+}\_{\alpha}(X)\in\mathbb{R} for any α∈(0,1)\alpha\in(0,1).
Both versions of VaR satisfy monotonicity, cash additivity, positive homogeneity, law invariance, and quasi-concavity in mixtures, but not quasi-convexity, concavity in mixtures, or SSD-consistency.

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a decreasing function. Throughout, all terms of “increasing” and “decreasing” are in the weak sense.
The *Λ\Lambda-Value-at-Risk* (Λ\Lambda-VaR, or Λ\Lambda-quantile), denoted by
VaRΛ:L0→ℝ¯\mathrm{VaR}\_{\Lambda}:L^{0}\to\overline{\mathbb{R}},
is defined as

|  |  |  |
| --- | --- | --- |
|  | VaRΛ​(X)=inf{x∈ℝ:ℙ​(X⩽x)⩾Λ​(x)}=sup{x∈ℝ:ℙ​(X⩽x)<Λ​(x)},X∈L0.\mathrm{VaR}\_{\Lambda}(X)=\inf\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)\geqslant\Lambda(x)\}=\sup\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)<\Lambda(x)\},~~~X\in L^{0}. |  |

Frittelli et al. ([2014](https://arxiv.org/html/2512.23139v2#bib.bib21)) originally introduced Λ\Lambda-VaR focusing on the case that Λ\Lambda is increasing. Bellini and Bignozzi ([2015](https://arxiv.org/html/2512.23139v2#bib.bib3)) showed that Λ\Lambda-VaR with a decreasing Λ\Lambda satisfies elicitability, and it is not true for increasing Λ\Lambda (Burzoni et al., [2017](https://arxiv.org/html/2512.23139v2#bib.bib6)). A more decisive result is the axiomatic justification of
Bellini and Peri ([2022](https://arxiv.org/html/2512.23139v2#bib.bib4)) for using a decreasing function Λ\Lambda. Han et al. ([2025](https://arxiv.org/html/2512.23139v2#bib.bib25)) further showed that Λ\Lambda-VaR with a decreasing Λ\Lambda is cash subadditive and hence L∞L^{\infty}-continuous, but with an increasing Λ\Lambda even L∞L^{\infty}-continuity fails. For these reasons, our study focuses on the case of decreasing Λ\Lambda.

VaR has two versions, and so does Λ\Lambda-VaR. We define the *upper Λ\Lambda-VaR*, denoted by VaRΛ+:L0→ℝ¯\mathrm{VaR}^{+}\_{\Lambda}:L^{0}\to\overline{\mathbb{R}}, as

|  |  |  |
| --- | --- | --- |
|  | VaRΛ+​(X)=inf{x∈ℝ:ℙ​(X⩽x)>Λ​(x)}=sup{x∈ℝ:ℙ​(X⩽x)⩽Λ​(x)},X∈L0.\mathrm{VaR}^{+}\_{\Lambda}(X)=\inf\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)>\Lambda(x)\}=\sup\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)\leqslant\Lambda(x)\},~~~X\in L^{0}. |  |

If Λ\Lambda is a constant α∈[0,1]\alpha\in[0,1] (written Λ≡α\Lambda\equiv\alpha), then VaRΛ=VaRα\mathrm{VaR}\_{\Lambda}=\mathrm{VaR}\_{\alpha} and VaRΛ+=VaRα+\mathrm{VaR}^{+}\_{\Lambda}=\mathrm{VaR}^{+}\_{\alpha}.
The risk measure Λ\Lambda-VaR is monotone, but not cash additive or positively homogeneous, thus losing some usual properties of VaR.

Han et al. ([2025](https://arxiv.org/html/2512.23139v2#bib.bib25), Theorem 1) gives a representation of Λ\Lambda-VaR, which will be useful for our study. Below, we state the result and extend it to Λ\Lambda-VaR+\mathrm{VaR}^{+}.

###### Proposition 1.

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a decreasing function. The risk measures VaRΛ\mathrm{VaR}\_{\Lambda} and VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} admit the following representations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRΛ​(X)=supx∈ℝ(VaRΛ​(x)​(X)∧x)=infx∈ℝ(VaRΛ​(x)​(X)∨x),X∈L0,\displaystyle\mathrm{VaR}\_{\Lambda}(X)=\sup\_{x\in\mathbb{R}}\left(\mathrm{VaR}\_{\Lambda(x)}(X)\wedge x\right)=\inf\_{x\in\mathbb{R}}\left(\mathrm{VaR}\_{\Lambda(x)}(X)\vee x\right),~~~X\in L^{0}, |  | (2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRΛ+​(X)=supx∈ℝ(VaRΛ​(x)+​(X)∧x)=infx∈ℝ(VaRΛ​(x)+​(X)∨x),X∈L0.\displaystyle\mathrm{VaR}^{+}\_{\Lambda}(X)=\sup\_{x\in\mathbb{R}}\left(\mathrm{VaR}^{+}\_{\Lambda(x)}(X)\wedge x\right)=\inf\_{x\in\mathbb{R}}\left(\mathrm{VaR}^{+}\_{\Lambda(x)}(X)\vee x\right),~~~X\in L^{0}. |  | (3) |

###### Proof.

Equation ([2](https://arxiv.org/html/2512.23139v2#S2.E2 "In Proposition 1. ‣ 2.2 VaR and Lambda VaR ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) holds directly by Theorem 1 of Han et al. ([2025](https://arxiv.org/html/2512.23139v2#bib.bib25)) for all decreasing functions Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] that are not constantly 0. For Λ≡0\Lambda\equiv 0, we have

|  |  |  |
| --- | --- | --- |
|  | supx∈ℝ(−∞∧x)=infx∈ℝ(−∞∨x)=−∞=VaR0​(X).\sup\_{x\in\mathbb{R}}\left(-\infty\wedge x\right)=\inf\_{x\in\mathbb{R}}\left(-\infty\vee x\right)=-\infty=\mathrm{VaR}\_{0}(X). |  |

Thus ([2](https://arxiv.org/html/2512.23139v2#S2.E2 "In Proposition 1. ‣ 2.2 VaR and Lambda VaR ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) holds for all decreasing functions Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1]. To see ([3](https://arxiv.org/html/2512.23139v2#S2.E3 "In Proposition 1. ‣ 2.2 VaR and Lambda VaR ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")), using some standard relations between quantiles and distribution functions, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRΛ+​(X)\displaystyle\mathrm{VaR}^{+}\_{\Lambda}(X) | =sup{x∈ℝ:ℙ​(X⩽x)⩽Λ​(x)}\displaystyle=\sup\{x\in\mathbb{R}:\mathbb{P}(X\leqslant x)\leqslant\Lambda(x)\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =sup{x∈ℝ:VaRΛ​(x)+​(X)⩾x}=supx∈ℝ{VaRΛ​(x)+​(X)∧x},\displaystyle=\sup\{x\in\mathbb{R}:\mathrm{VaR}^{+}\_{\Lambda(x)}(X)\geqslant x\}=\sup\_{x\in\mathbb{R}}\left\{\mathrm{VaR}^{+}\_{\Lambda(x)}(X)\wedge x\right\}, |  |

and similarly,

|  |  |  |
| --- | --- | --- |
|  | VaRΛ+​(X)=inf{x∈ℝ:VaRΛ​(x)+​(X)<x}=infx∈ℝ{VaRΛ​(x)+​(X)∨x}.\displaystyle\mathrm{VaR}^{+}\_{\Lambda}(X)=\inf\{x\in\mathbb{R}:\mathrm{VaR}^{+}\_{\Lambda(x)}(X)<x\}=\inf\_{x\in\mathbb{R}}\left\{\mathrm{VaR}^{+}\_{\Lambda(x)}(X)\vee x\right\}. |  |

The proof is complete.
∎

### 2.3 Expected Shortfall

The standard risk measure in banking regulation, the *Expected Shortfall* (ES), can be defined via a few different formulations.
First, as the most standard definition, ES at level α∈[0,1]\alpha\in[0,1] is defined as the mapping
ESα:L∞→ℝ\mathrm{ES}\_{\alpha}:L^{\infty}\to\mathbb{R} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα​(X)=11−α​∫α1VaRβ​(X)​dβ​ for α∈[0,1),\displaystyle\mathrm{ES}\_{\alpha}(X)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\mathrm{VaR}\_{\beta}(X)\mathrm{d}\beta\mbox{ for $\alpha\in[0,1)$}, |  | (4) |

and ES1​(X)=VaR1​(X)\mathrm{ES}\_{1}(X)=\mathrm{VaR}\_{1}(X).
Note that ES0=𝔼\mathrm{ES}\_{0}=\mathbb{E} and the definition of ESα\mathrm{ES}\_{\alpha} in ([4](https://arxiv.org/html/2512.23139v2#S2.E4 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) can be easily extended to L1L^{1}. We will discuss risk measures on L1L^{1} in Section [6](https://arxiv.org/html/2512.23139v2#S6 "6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall").
An ES satisfies all properties listed in Section [2.1](https://arxiv.org/html/2512.23139v2#S2.SS1 "2.1 Risk measures ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall").
Second, as shown by Rockafellar and Uryasev ([2002](https://arxiv.org/html/2512.23139v2#bib.bib35)), for α∈[0,1]\alpha\in[0,1], ESα\mathrm{ES}\_{\alpha} can be equivalently formulated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα​(X)=minx∈ℝ⁡{x+11−α​𝔼​[(X−x)+]},X∈L∞,\displaystyle\mathrm{ES}\_{\alpha}(X)=\min\_{x\in\mathbb{R}}\left\{x+\frac{1}{1-\alpha}\mathbb{E}[(X-x)\_{+}]\right\},~~~X\in L^{\infty}, |  | (5) |

where we set 0/0=00/0=0 and x/0=∞x/0=\infty for x>0x>0. The representation ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) connects to VaR via

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​minx∈ℝ⁡{x+11−α​𝔼​[(X−x)+]}={[VaRα​(X),VaRα+​(X)],if​α∈[0,1),VaR1​(X),if​α=1,​X∈L∞.\displaystyle\operatorname\*{arg\,min}\_{x\in\mathbb{R}}\left\{x+\frac{1}{1-\alpha}\mathbb{E}[(X-x)\_{+}]\right\}=\left\{\begin{array}[]{ll}[\mathrm{VaR}\_{\alpha}(X),\mathrm{VaR}^{+}\_{\alpha}(X)],&\mbox{if}~\alpha\in[0,1),\\ \mathrm{VaR}\_{1}(X),&\mbox{if}~\alpha=1,\end{array}\right.~~~X\in L^{\infty}. |  | (8) |

We call ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) and ([8](https://arxiv.org/html/2512.23139v2#S2.E8 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) the Rockafellar–Uryasev (RU) formulas for VaR and ES.
Third, it is known that the risk measure ESα\mathrm{ES}\_{\alpha} is the smallest law-invariant coherent risk measure dominating VaRα\mathrm{VaR}\_{\alpha} (Delbaen, [2012](https://arxiv.org/html/2512.23139v2#bib.bib11), Theorem 52).
Convexity is important and relevant for risk management, and for this reason, ES is regarded as an improvement of VaR.
In the next result, we show that ESα\mathrm{ES}\_{\alpha} is also the smallest mapping dominating VaRα\mathrm{VaR}\_{\alpha} satisfying quasi-convexity and law invariance.
As far as we know, this result is new, and it is based on a VaR-ES asymptotic equivalence result of Wang and Wang ([2015](https://arxiv.org/html/2512.23139v2#bib.bib37)) and a result in Embrechts et al. ([2015](https://arxiv.org/html/2512.23139v2#bib.bib16)) on the sum of negatively dependent sequences. Throughout the paper, we write ρ⩾ρ~\rho\geqslant\widetilde{\rho} for mappings ρ:𝒳→ℝ¯\rho:\mathcal{X}\to\overline{\mathbb{R}} and ρ~:𝒳~→ℝ¯\widetilde{\rho}:\widetilde{\mathcal{X}}\to\overline{\mathbb{R}} to represent the dominance of ρ\rho over ρ~\widetilde{\rho} on their common domain (i.e., ρ​(X)⩾ρ~​(X)\rho(X)\geqslant\widetilde{\rho}(X) for all X∈𝒳∩𝒳~X\in\mathcal{X}\cap\widetilde{\mathcal{X}}), and typically we have either 𝒳⊆𝒳~\mathcal{X}\subseteq\widetilde{\mathcal{X}} or 𝒳~⊆𝒳\widetilde{\mathcal{X}}\subseteq\mathcal{X}.

###### Theorem 1.

The following equalities hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα=min⁡{ρ:L∞→ℝ¯∣ρ⩾VaRα​and ρ is quasi-convex and law invariant},α∈(0,1].\displaystyle\mathrm{ES}\_{\alpha}=\min\{\rho:L^{\infty}\to\overline{\mathbb{R}}\mid\rho\geqslant\mathrm{VaR}\_{\alpha}~\mbox{and $\rho$ is quasi-convex and law invariant}\},~\alpha\in(0,1]. |  | (9) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα=min⁡{ρ:L∞→ℝ¯∣ρ⩾VaRα+​and ρ is quasi-convex and law invariant},α∈[0,1).\displaystyle\mathrm{ES}\_{\alpha}=\min\{\rho:L^{\infty}\to\overline{\mathbb{R}}\mid\rho\geqslant\mathrm{VaR}^{+}\_{\alpha}~\mbox{and $\rho$ is quasi-convex and law invariant}\},~\alpha\in[0,1). |  | (10) |

###### Proof.

(i) We first prove ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")). Let ρ\rho be quasi-convex and law invariant satisfying ρ⩾VaRα\rho\geqslant\mathrm{VaR}\_{\alpha}.
If α=1\alpha=1, it is clear that ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) holds, because VaR1\mathrm{VaR}\_{1} is quasi-convex and law invariant.
Next, suppose α∈(0,1)\alpha\in(0,1).
For any X∈L∞X\in L^{\infty} with distribution FF, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ρ​(X)\displaystyle\rho(X) | =sup{max⁡{ρ​(X1),…,ρ​(Xn)}:Xi∼dF,i∈[n]}\displaystyle=\sup\left\{\max\{\rho(X\_{1}),\dots,\rho(X\_{n})\}:{X\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F,~i\in[n]}\right\} |  | [law invariance of ρ\rho] |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⩾sup{ρ​(X1+⋯+Xnn):Xi∼dF,i∈[n]}\displaystyle\geqslant\sup\left\{\rho\left(\frac{X\_{1}+\dots+X\_{n}}{n}\right):{X\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F,~i\in[n]}\right\} |  | [quasi-convexity of ρ\rho] |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⩾sup{VaRα​(X1+⋯+Xnn):Xi∼dF,i∈[n]}\displaystyle\geqslant\sup\left\{\mathrm{VaR}\_{\alpha}\left(\frac{X\_{1}+\dots+X\_{n}}{n}\right):{X\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F,~i\in[n]}\right\} |  | [ρ⩾VaRα\rho\geqslant\mathrm{VaR}\_{\alpha}] |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1n​sup{VaRα​(X1+⋯+Xn):Xi∼dF,i∈[n]}\displaystyle=\frac{1}{n}\sup\left\{\mathrm{VaR}\_{\alpha}\left({X\_{1}+\dots+X\_{n}}\right):{X\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F,~i\in[n]}\right\} |  | [positive homogeneity of VaRα\mathrm{VaR}\_{\alpha}] |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | →ESα​(X),as n→∞.\displaystyle\to\mathrm{ES}\_{\alpha}(X),~~~\mbox{as $n\to\infty$}. |  | [Corollary 3.7 of Wang and Wang ([2015](https://arxiv.org/html/2512.23139v2#bib.bib37))] |

This shows that ρ⩾ESα\rho\geqslant\mathrm{ES}\_{\alpha} for any ρ\rho in the set in ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")).
Since ESα\mathrm{ES}\_{\alpha} also satisfies law invariance and quasi-convexity, we know that the minimum of the set in ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) is ESα\mathrm{ES}\_{\alpha}.

(ii) For α∈(0,1)\alpha\in(0,1), the result in part (i) implies that ESα\mathrm{ES}\_{\alpha} is the smallest quasi-convex and law-invariant risk measure that dominates VaRα\mathrm{VaR}\_{\alpha},
and since ESα⩾VaRα+⩾VaRα\mathrm{ES}\_{\alpha}\geqslant\mathrm{VaR}\_{\alpha}^{+}\geqslant\mathrm{VaR}\_{\alpha}, the conclusion also holds for VaRα+\mathrm{VaR}\_{\alpha}^{+}.

For α=0\alpha=0 and X∈L∞X\in L^{\infty} with distribution FF, write M=VaR1​(X)−VaR0+​(X)M=\mathrm{VaR}\_{1}(X)-\mathrm{VaR}^{+}\_{0}(X). For any n∈ℕn\in\mathbb{N}, by Corollary A.3 of Embrechts et al. ([2015](https://arxiv.org/html/2512.23139v2#bib.bib16)), there exist X~i∼dF\widetilde{X}\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F, i∈[n]i\in[n], such that
|∑i=1nX~i/n−𝔼​[X]|⩽M/n.|\sum^{n}\_{i=1}\widetilde{X}\_{i}/n-\mathbb{E}[X]|\leqslant M/n.
Hence,
∑i=1nX~i/n⩾𝔼​[X]−M/n.\sum^{n}\_{i=1}\widetilde{X}\_{i}/n\geqslant\mathbb{E}[X]-M/n.
It yields that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X]⩾1n​VaR0+​(X~1+⋯+X~n)⩾𝔼​[X]−Mn.\mathbb{E}[X]\geqslant\frac{1}{n}\mathrm{VaR}^{+}\_{0}\left({\widetilde{X}\_{1}+\dots+\widetilde{X}\_{n}}\right)\geqslant\mathbb{E}[X]-\frac{M}{n}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | 1n​sup{VaR0+​(X1+⋯+Xn):Xi∼dF,i∈[n]}→𝔼​[X],as ​n→∞.\frac{1}{n}\sup\left\{\mathrm{VaR}^{+}\_{0}\left({X\_{1}+\dots+X\_{n}}\right):{X\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F,~i\in[n]}\right\}\to\mathbb{E}[X],~~~\mbox{as }n\to\infty. |  |

Hence, we have ρ​(X)⩾𝔼​[X]\rho(X)\geqslant\mathbb{E}[X] in the same sense as the argument in part (i). As 𝔼\mathbb{E} dominates the essential infimum VaR0+\mathrm{VaR}^{+}\_{0}, it implies that 𝔼\mathbb{E} is the smallest quasi-convex and law-invariant risk measure that dominates VaR0+\mathrm{VaR}^{+}\_{0}.
∎

Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") is stronger than two classical results: Föllmer and Schied ([2016](https://arxiv.org/html/2512.23139v2#bib.bib20), Theorem 4.67), which requires ρ\rho in ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) to be convex, monetary and Fatou-continuous,
and
Delbaen ([2012](https://arxiv.org/html/2512.23139v2#bib.bib11), Theorem 52), which requires ρ\rho in ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) to be coherent.333We say a risk measure ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R} is *Fatou-continuous* if it is lower semicontinuous under bounded pointwise convergence: For all bounded X,X1,X2,⋯∈𝒳X,X\_{1},X\_{2},\dots\in\mathcal{X} such that Xn→XX\_{n}\to X pointwise as n→∞n\to\infty, ρ​(X)⩽lim infn→∞ρ​(Xn)\rho(X)\leqslant\liminf\_{n\to\infty}\rho(X\_{n}).
Both of the two results above further assumed that ρ\rho takes finite values and α∈(0,1)\alpha\in(0,1), but these differences are not essential.
We note that ([9](https://arxiv.org/html/2512.23139v2#S2.E9 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) fails for α=0\alpha=0 because VaR0=−∞\mathrm{VaR}\_{0}=-\infty is quasi-convex, and the smallest quasi-convex and law-invariant risk measure dominating VaR0\mathrm{VaR}\_{0} is itself instead of ES0=𝔼\mathrm{ES}\_{0}=\mathbb{E}.
Similarly,
([10](https://arxiv.org/html/2512.23139v2#S2.E10 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) fails for α=1\alpha=1 because VaR1+=∞\mathrm{VaR}\_{1}^{+}=\infty is quasi-convex, and
the smallest quasi-convex and law-invariant risk measure dominating VaR1+\mathrm{VaR}\_{1}^{+} is itself instead of ES1=VaR1\mathrm{ES}\_{1}=\mathrm{VaR}\_{1}.

## 3 Lambda ES

Now we turn to our main task of formulating the
Λ\Lambda-Expected Shortfall (Λ\Lambda-ES).
By introducing a new class of risk measures, there should be some clear gain. Otherwise, the newly defined class is not useful.
The following properties are also satisfied by Λ\Lambda-VaR, and they will be considered as basic requirements for Λ\Lambda-ES. We believe their desirability is self-evident.

* –

  Λ\Lambda-ES should be parameterized only by the function Λ\Lambda.
* –

  Λ\Lambda-ES should coincide with ESα\mathrm{ES}\_{\alpha} when Λ\Lambda is equal to a constant α∈[0,1]\alpha\in[0,1].
* –

  Λ\Lambda-ES should increase as Λ\Lambda increases.
* –

  Λ\Lambda-ES should be monotone and law invariant.

The next four properties are additional requirements for Λ\Lambda-ES to be considered a useful alternative to Λ\Lambda-VaR, and they highlight the contrasts between ES and VaR.

* –

  Λ\Lambda-ES should dominate Λ\Lambda-VaR. This is analogous to the dominance of ES over VaR.
* –

  Λ\Lambda-ES should be quasi-convex. This should be the key improvement of Λ\Lambda-ES over Λ\Lambda-VaR so that it captures the diversification effects.
* –

  Λ\Lambda-ES should be SSD-consistent. This property allows for Λ\Lambda-ES to capture strong risk aversion in decision theory and to make consistent risk assessment.
* –

  Λ\Lambda-ES should be
  L1L^{1}-continuous.
  This property models a form of robustness for law-invariant risk measures (Krätschmer et al., [2014](https://arxiv.org/html/2512.23139v2#bib.bib29)).

Some other properties, such as normalization, cash subadditivity, and quasi-concavity in mixtures are also natural from the corresponding properties of ES, although they may be less critical.

With these desirable properties in mind, we are ready to define the Λ\Lambda-ES.
We first give the formal definition, which is inspired by the Λ\Lambda-VaR representtion in Proposition [1](https://arxiv.org/html/2512.23139v2#Thmproposition1 "Proposition 1. ‣ 2.2 VaR and Lambda VaR ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall"), and then show that it satisfies all desirable properties discussed above.

###### Definition 1 (Λ\Lambda-Expected Shortfall).

For a decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1], the *Λ\Lambda-Expected Shortfall* (Λ\Lambda-ES) is defined as the risk measure ESΛ:L∞→ℝ\mathrm{ES}\_{\Lambda}:L^{\infty}\to\mathbb{R} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)=supx∈ℝ(ESΛ​(x)​(X)∧x),X∈L∞.\displaystyle\mathrm{ES}\_{\Lambda}(X)=\sup\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\wedge x\right),~~~X\in L^{\infty}. |  | (11) |

Note the distinction in notation: ESΛ\mathrm{ES}\_{\Lambda} is the mathematical object in ([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")), whereas Λ\Lambda-ES refers to the concept, as we have been speaking of it without formal definition.

Figure [1](https://arxiv.org/html/2512.23139v2#S3.F1 "Figure 1 ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") illustrates the definition of ESΛ\mathrm{ES}\_{\Lambda} when the function Λ\Lambda is continuous and discontinuous, respectively. Writing x∗=ESΛ​(X)x^{\*}=\mathrm{ES}\_{\Lambda}(X),
we can see that (x∗,x∗)(x^{\*},x^{\*}) is the unique intersection point between the graph (linearly interpolated) of the function x↦ESΛ​(x)​(X)x\mapsto\mathrm{ES}\_{\Lambda(x)}(X) and the graph of the identity. From the right panel of Figure [1](https://arxiv.org/html/2512.23139v2#S3.F1 "Figure 1 ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"), we can also see that whether x↦ESΛ​(x)​(X)x\mapsto\mathrm{ES}\_{\Lambda(x)}(X) is left- or right-continuous at x∗x^{\*} (or neither) does not matter.

x∗x^{\*}ESΛ​(X)\mathrm{ES}\_{\Lambda}(X)f1​(x)=ESΛ​(x)​(X)f\_{1}(x)=\mathrm{ES}\_{\Lambda(x)}(X)f2​(x)=xf\_{2}(x)=xxxx∗x^{\*}ESΛ​(X)\mathrm{ES}\_{\Lambda}(X)f1​(x)=ESΛ​(x)​(X)f\_{1}(x)=\mathrm{ES}\_{\Lambda(x)}(X)f2​(x)=xf\_{2}(x)=xxx

Figure 1: Illustration of ESΛ\mathrm{ES}\_{\Lambda} in Definition [1](https://arxiv.org/html/2512.23139v2#Thmdefinition1 "Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"); left panel shows ESΛ\mathrm{ES}\_{\Lambda} for a continuous Λ\Lambda; right panel shows ESΛ\mathrm{ES}\_{\Lambda} for Λ\Lambda that is discontinuous at x∗=ESΛ​(X)x^{\*}=\mathrm{ES}\_{\Lambda}(X)

By definition, ESΛ\mathrm{ES}\_{\Lambda} is finite on L∞L^{\infty}; see also item (a) of Proposition [2](https://arxiv.org/html/2512.23139v2#Thmproposition2 "Proposition 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") below.
The next result shows that ESΛ\mathrm{ES}\_{\Lambda} is the smallest quasi-convex and law-invariant mapping dominating VaRΛ\mathrm{VaR}\_{\Lambda}.
Therefore, it is the unique formulation of the concept of Λ\Lambda-ES that generalizes the ES-VaR relation in Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall").

###### Theorem 2.

The following statements hold.

1. (i)

   For a decreasing function Λ:ℝ→(0,1]\Lambda:\mathbb{R}\to(0,1], the smallest quasi-convex and law-invariant risk measure on L∞L^{\infty} dominating VaRΛ\mathrm{VaR}\_{\Lambda} is ESΛ\mathrm{ES}\_{\Lambda}, that is,
   ES\_Λ= min{ρ: L^∞→R∣ρ⩾VaR\_Λ and ρ\rho is quasi-convex and law invariant}.
2. (ii)

   For a decreasing function Λ:ℝ→[0,1)\Lambda:\mathbb{R}\to[0,1), the smallest quasi-convex and law-invariant risk measure on L∞L^{\infty} dominating VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} is ESΛ\mathrm{ES}\_{\Lambda}, that is,
   ES\_Λ= min{ρ: L^∞→R∣ρ⩾VaR^+\_Λ and ρ\rho is quasi-convex and law invariant}.

Moreover, the following identity holds for all decreasing functions Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)=infx∈ℝ(ESΛ​(x)​(X)∨x),X∈L∞.\displaystyle\mathrm{ES}\_{\Lambda}(X)=\inf\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\vee x\right),~~~X\in L^{\infty}. |  | (12) |

###### Proof.

Using ([2](https://arxiv.org/html/2512.23139v2#S2.E2 "In Proposition 1. ‣ 2.2 VaR and Lambda VaR ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall"))–([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")), we can see that ESΛ\mathrm{ES}\_{\Lambda}
dominates VaRΛ\mathrm{VaR}\_{\Lambda} for Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] (resp. VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} for Λ:ℝ→[0,1)\Lambda:\mathbb{R}\to[0,1)) because ESα⩾VaRα\mathrm{ES}\_{\alpha}\geqslant\mathrm{VaR}\_{\alpha} for all α∈[0,1]\alpha\in[0,1] (resp. ESα⩾VaRα+\mathrm{ES}\_{\alpha}\geqslant\mathrm{VaR}^{+}\_{\alpha} for all α∈[0,1)\alpha\in[0,1)).
Moreover, ESΛ\mathrm{ES}\_{\Lambda}
is law invariant by definition. Next, we show that ESΛ\mathrm{ES}\_{\Lambda} is quasi-convex. Note that for any given α∈[0,1]\alpha\in[0,1], ESα\mathrm{ES}\_{\alpha} is quasi-convex. Further, an increasing transform of a quasi-convex function is quasi-convex, as well as the supremum of a set of quasi-convex functions. Using these facts,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(x)​ is quasi-convex for each x∈ℝ\displaystyle\mathrm{ES}\_{\Lambda(x)}\mbox{ is quasi-convex for each $x\in\mathbb{R}$} | ⟹ESΛ​(x)∧x​ is quasi-convex for each x∈ℝ\displaystyle\implies\mathrm{ES}\_{\Lambda(x)}\wedge x\mbox{ is quasi-convex for each $x\in\mathbb{R}$} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟹supx∈ℝ(ESΛ​(x)∧x)​ is quasi-convex.\displaystyle\implies\sup\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}\wedge x\right)\mbox{ is quasi-convex.} |  |

Therefore, ESΛ\mathrm{ES}\_{\Lambda} is a quasi-convex and law-invariant risk measure dominating VaRΛ\mathrm{VaR}\_{\Lambda} for Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1]
(resp. VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} for Λ:ℝ→[0,1)\Lambda:\mathbb{R}\to[0,1)).

Next, for Λ:ℝ→(0,1]\Lambda:\mathbb{R}\to(0,1], we show that for any ρ\rho that is quasi-convex, law invariant, and satisfying ρ⩾VaRΛ\rho\geqslant\mathrm{VaR}\_{\Lambda},
it must be ρ⩾ESΛ\rho\geqslant\mathrm{ES}\_{\Lambda}.
For any X∈L∞X\in L^{\infty}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)⩾VaRΛ​(X)\displaystyle\rho(X)\geqslant\mathrm{VaR}\_{\Lambda}(X) | ⟹ρ​(X)⩾supx∈ℝ(VaRΛ​(x)​(X)∧x)\displaystyle\implies\rho(X)\geqslant\sup\_{x\in\mathbb{R}}\left(\mathrm{VaR}\_{\Lambda(x)}(X)\wedge x\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟹for all x∈ℝ:​ρ​(X)⩾VaRΛ​(x)​(X)​ or ​ρ​(X)⩾x\displaystyle\implies\mbox{for all $x\in\mathbb{R}:~$}\rho(X)\geqslant\mathrm{VaR}\_{\Lambda(x)}(X)\mbox{ or }\rho(X)\geqslant x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | [Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")] | ⟹for all x∈ℝ:​ρ​(X)⩾ESΛ​(x)​(X)​ or ​ρ​(X)⩾x\displaystyle\implies\mbox{for all $x\in\mathbb{R}:~$}\rho(X)\geqslant\mathrm{ES}\_{\Lambda(x)}(X)\mbox{ or }\rho(X)\geqslant x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟹ρ​(X)⩾supx∈ℝ(ESΛ​(x)​(X)∧x)=ESΛ​(X).\displaystyle\implies\rho(X)\geqslant\sup\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\wedge x\right)=\mathrm{ES}\_{\Lambda}(X). |  |

For Λ:ℝ→[0,1)\Lambda:\mathbb{R}\to[0,1), for any ρ\rho that is quasi-convex, law invariant, and satisfying ρ⩾VaRΛ+\rho\geqslant\mathrm{VaR}^{+}\_{\Lambda}, we have ρ​(X)⩾ESΛ​(X)\rho(X)\geqslant\mathrm{ES}\_{\Lambda}(X) for any X∈L∞X\in L^{\infty} with the same argument as above by replacing VaRΛ​(x)\mathrm{VaR}\_{\Lambda(x)} by VaRΛ​(x)+\mathrm{VaR}^{+}\_{\Lambda(x)} for all x∈ℝx\in\mathbb{R}.
This completes the proof of statements (i) and (ii).
The final statement in ([12](https://arxiv.org/html/2512.23139v2#S3.E12 "In Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")) follows from ([2](https://arxiv.org/html/2512.23139v2#S2.E2 "In Proposition 1. ‣ 2.2 VaR and Lambda VaR ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")), by noting that an ES curve α↦ESα​(X)\alpha\mapsto\mathrm{ES}\_{\alpha}(X) for X∈L∞X\in L^{\infty} can be written as a VaR (resp. VaR+\mathrm{VaR}^{+}) curve α↦VaRα​(Y)\alpha\mapsto\mathrm{VaR}\_{\alpha}(Y) for some Y∈L0Y\in L^{0} on α∈(0,1]\alpha\in(0,1] (resp. α∈[0,1)\alpha\in[0,1)); see e.g., Lemma 4.5 of Burzoni et al. ([2022](https://arxiv.org/html/2512.23139v2#bib.bib7)).
∎

In Theorem [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"),
the reason to exclude 0 (resp. 11) in part (i) (resp. part (ii)) from the range of Λ\Lambda is the same as that in Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall"), where 0 (resp. 11) is excluded from the domination of ESα\mathrm{ES}\_{\alpha} over VaRα\mathrm{VaR}\_{\alpha} (resp. VaRα+\mathrm{VaR}\_{\alpha}^{+}), explained at the end of Section [2.3](https://arxiv.org/html/2512.23139v2#S2.SS3 "2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall").

An immediate consequence of ([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"))–([12](https://arxiv.org/html/2512.23139v2#S3.E12 "In Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")) is that, for any X∈L∞X\in L^{\infty} and x∈ℝx\in\mathbb{R}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(x+)​(X)⩽x⩽ESΛ​(x−)​(X)⇔ESΛ​(X)=x.\displaystyle\mathrm{ES}\_{\Lambda(x+)}(X)\leqslant x\leqslant\mathrm{ES}\_{\Lambda(x-)}(X)~\iff~\mathrm{ES}\_{\Lambda}(X)=x. |  | (13) |

This is also illustrated in Figure [1](https://arxiv.org/html/2512.23139v2#S3.F1 "Figure 1 ‣ 3 Lambda ES ‣ Lambda Expected Shortfall").
As a result of ([13](https://arxiv.org/html/2512.23139v2#S3.E13 "In 3 Lambda ES ‣ Lambda Expected Shortfall")), for any X∈L∞X\in L^{\infty} and x∈ℝx\in\mathbb{R}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(x)​(X)=x⟹ESΛ​(X)=x;\displaystyle\mathrm{ES}\_{\Lambda(x)}(X)=x~\implies~\mathrm{ES}\_{\Lambda}(X)=x; |  | (14) |

moreover, if Λ\Lambda is continuous, then
([14](https://arxiv.org/html/2512.23139v2#S3.E14 "In 3 Lambda ES ‣ Lambda Expected Shortfall")) becomes an equivalence.
These relations will be convenient in some proof arguments.

###### Remark 1.

As standard in the risk measures literature, the main results are formulated on the space L∞L^{\infty} of essentially bounded random variables.
The results in
Theorems [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") and [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")
hold on the space L1L^{1} of integrable random variables for α\alpha and Λ\Lambda taking values in (0,1)(0,1), following the same proof arguments, but for α=0\alpha=0 and α=1\alpha=1, some minor adjustments are needed.
It is straightforward to see that
all other results hold on L1L^{1}. We discuss the details in Section [6](https://arxiv.org/html/2512.23139v2#S6 "6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall").

###### Remark 2.

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a decreasing function and ρΛ=VaRΛ\rho\_{\Lambda}=\mathrm{VaR}\_{\Lambda}, VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} or ESΛ\mathrm{ES}\_{\Lambda}. The supremum in
ρ=supx∈ℝ{ρΛ​(x)∧x}\rho=\sup\_{x\in\mathbb{R}}\{\rho\_{\Lambda(x)}\wedge x\}
is a maximum when Λ\Lambda is left-continuous; similarly the infimum in
ρ=infx∈ℝ{ρΛ​(x)∨x}\rho=\inf\_{x\in\mathbb{R}}\{\rho\_{\Lambda(x)}\vee x\}
is a minimum when Λ\Lambda is right-continuous; see Figure [1](https://arxiv.org/html/2512.23139v2#S3.F1 "Figure 1 ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") for an illustration.

It is clear that ESΛ\mathrm{ES}\_{\Lambda} is parameterized only by the function Λ\Lambda, and ESΛ=ESα\mathrm{ES}\_{\Lambda}=\mathrm{ES}\_{\alpha} when Λ≡α\Lambda\equiv\alpha for some α∈(0,1)\alpha\in(0,1). It satisfies all other desirable properties as a good candidate for Λ\Lambda-ES\mathrm{ES} as discussed in the beginning of the section, which we summarize in the following result.

###### Proposition 2.

For any decreasing functions Λ,Λ′:ℝ→[0,1]\Lambda,\Lambda^{\prime}:\mathbb{R}\to[0,1], the risk measure ESΛ\mathrm{ES}\_{\Lambda} satisfies the following properties:
(a) ESΛ⩾ESΛ′\mathrm{ES}\_{\Lambda}\geqslant\mathrm{ES}\_{\Lambda^{\prime}} when Λ⩾Λ′\Lambda\geqslant\Lambda^{\prime};
(b) ESΛ\mathrm{ES}\_{\Lambda} is monotone;
(c) ESΛ⩾VaRΛ\mathrm{ES}\_{\Lambda}\geqslant\mathrm{VaR}\_{\Lambda};
(d) ESΛ\mathrm{ES}\_{\Lambda} is quasi-convex;
(e) ESΛ\mathrm{ES}\_{\Lambda} is normalized;
(f) ESΛ\mathrm{ES}\_{\Lambda} is cash subadditive;
(g) ESΛ\mathrm{ES}\_{\Lambda} is SSD-consistent;
(h) ESΛ\mathrm{ES}\_{\Lambda} is quasi-concave in mixtures;
(i) ESΛ\mathrm{ES}\_{\Lambda} is L1L^{1}-continuous when Λ\Lambda takes values in [0,1)[0,1).

###### Proof.

Items (a) and (b) are straightforward because ESα​(X)\mathrm{ES}\_{\alpha}(X) is monotone (increasing) in both α\alpha and XX, and the supremum of monotone transformations of ESα​(X)\mathrm{ES}\_{\alpha}(X) is also monotone.
Items (c) and (d) are implied by Theorem [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"). Item (e) follows from ([14](https://arxiv.org/html/2512.23139v2#S3.E14 "In 3 Lambda ES ‣ Lambda Expected Shortfall")).

To see item (f), for c∈ℝ+c\in\mathbb{R}\_{+} and X∈L∞X\in L^{\infty}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ESΛ​(X+c)=supx∈ℝ{ESΛ​(x)​(X+c)∧x}\displaystyle\mathrm{ES}\_{\Lambda}(X+c)=\sup\_{x\in\mathbb{R}}\{\mathrm{ES}\_{\Lambda(x)}(X+c)\wedge x\} | =supx∈ℝ{(ESΛ​(x)​(X)+c)∧x}\displaystyle=\sup\_{x\in\mathbb{R}}\{(\mathrm{ES}\_{\Lambda(x)}(X)+c)\wedge x\} |  | [cash additivity of ES] |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽supx∈ℝ{ESΛ​(x)​(X)∧x}+c=ESΛ​(X)+c.\displaystyle\leqslant\sup\_{x\in\mathbb{R}}\{\mathrm{ES}\_{\Lambda(x)}(X)\wedge x\}+c=\mathrm{ES}\_{\Lambda}(X)+c. |  |

Item (g) follows by applying Lemma 4 of
Han et al. ([2025](https://arxiv.org/html/2512.23139v2#bib.bib25)), using the fact that ESΛ\mathrm{ES}\_{\Lambda} is cash subadditive, monotone, quasi-convex, and law invariant. Cash subadditivity is proved in item (e). Law invariance of ESΛ\mathrm{ES}\_{\Lambda} is clear from the representation in ([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")) and the law invariance of ES.

For item (h), we first note that ESα\mathrm{ES}\_{\alpha} is concave in mixtures (Wang et al., [2020](https://arxiv.org/html/2512.23139v2#bib.bib38), Theorem 3) for each α∈[0,1]\alpha\in[0,1].
Since quasi-concavity is preserved under increasing transforms, we know that ESα∨x\mathrm{ES}\_{\alpha}\vee x is also quasi-concave in mixtures.
By using ([12](https://arxiv.org/html/2512.23139v2#S3.E12 "In Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")) and the fact that the infimum of quasi-concave functions is quasi-concave, we know that ESΛ\mathrm{ES}\_{\Lambda} is quasi-concave in mixtures.

To prove item (i),
first note that ESα\mathrm{ES}\_{\alpha} is L1L^{1}-continuous (e.g., Rüschendorf, [2013](https://arxiv.org/html/2512.23139v2#bib.bib36), Corollary 7.10) for each α∈[0,1)\alpha\in[0,1). Take any random variable XX and any sequence (Xn)n∈ℕ(X\_{n})\_{n\in\mathbb{N}} in L∞L^{\infty} such that Xn→XX\_{n}\to X in L1L^{1} as n→∞n\to\infty.
Let fn:x↦ESΛ​(x)​(Xn)−xf\_{n}:x\mapsto\mathrm{ES}\_{\Lambda(x)}(X\_{n})-x
and f:x↦ESΛ​(x)​(X)−xf:x\mapsto\mathrm{ES}\_{\Lambda(x)}(X)-x.
By ([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")), for any y,zy,z with
y<ESΛ​(X)<zy<\mathrm{ES}\_{\Lambda}(X)<z, we have f​(y)>0>f​(z)f(y)>0>f(z). Therefore, because fn→ff\_{n}\to f pointwise,
we have fn​(y)>0>fn​(z)f\_{n}(y)>0>f\_{n}(z) for nn large enough. This implies y⩽ESΛ​(Xn)⩽zy\leqslant\mathrm{ES}\_{\Lambda}(X\_{n})\leqslant z via ([13](https://arxiv.org/html/2512.23139v2#S3.E13 "In 3 Lambda ES ‣ Lambda Expected Shortfall")). Since y,zy,z are arbitrarily close to ESΛ​(X)\mathrm{ES}\_{\Lambda}(X), we know
ESΛ​(Xn)→ESΛ​(X)\mathrm{ES}\_{\Lambda}(X\_{n})\to\mathrm{ES}\_{\Lambda}(X).
∎

By item (a) of Proposition [2](https://arxiv.org/html/2512.23139v2#Thmproposition2 "Proposition 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"), it is straightforward that ESΛ\mathrm{ES}\_{\Lambda} is bounded above by ES1\mathrm{ES}\_{1} and below by 𝔼\mathbb{E} on L∞L^{\infty}, which also holds when ESΛ\mathrm{ES}\_{\Lambda} is formulated on larger spaces such as L1L^{1}.
The assumption that Λ\Lambda does not take the value 11 in item (i) is not dispensable, noting that ES1\mathrm{ES}\_{1} is not L1L^{1}-continuous.

The next result shows that although Λ\Lambda-ES is quasi-concave in mixtures and quasi-convex, it is neither concave in mixtures nor convex in general, unless it is an ES. This result also highlights the fact that quasi-convexity and convexity are different in strength for cash-subadditive risk measures, although they coincide for monetary risk measures, as shown by Cerreia-Vioglio et al. ([2011](https://arxiv.org/html/2512.23139v2#bib.bib8)).

###### Proposition 3.

For any decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1], the following are equivalent.

1. (i)

   The risk measure ESΛ\mathrm{ES}\_{\Lambda} is convex.
2. (ii)

   The risk measure ESΛ\mathrm{ES}\_{\Lambda} is concave in mixtures.
3. (iii)

   The function Λ\Lambda is constant on ℝ\mathbb{R}.

###### Proof.

“(iii) ⇒\Rightarrow (i)” and “(iii) ⇒\Rightarrow (ii)” follow from the facts that ES is convex and ES is concave in mixtures.
To prove “(i) ⇒\Rightarrow (iii)”, suppose that ESΛ\mathrm{ES}\_{\Lambda} is convex and for contradiction that Λ\Lambda is not constant on ℝ\mathbb{R}. There exist x>yx>y with Λ​(x−)<Λ​((x+y)/2)⩽Λ​(y)\Lambda(x-)<\Lambda((x+y)/2)\leqslant\Lambda(y). Take X,Y∈L∞X,Y\in L^{\infty} with 1−ℙ​(X=x)=ℙ​(X=y)=Λ​((x+y)/2)1-\mathbb{P}(X=x)=\mathbb{P}(X=y)=\Lambda((x+y)/2) and Y=yY=y. It follows that ESΛ​(Y)=y\mathrm{ES}\_{\Lambda}(Y)=y and ESΛ​((X+Y)/2)=(x+y)/2\mathrm{ES}\_{\Lambda}((X+Y)/2)=(x+y)/2.
Because Λ​(x−)<Λ​((x+y)/2)\Lambda(x-)<\Lambda((x+y)/2), we have ESΛ​(x−)​(X)<x\mathrm{ES}\_{\Lambda(x-)}(X)<x. By ([13](https://arxiv.org/html/2512.23139v2#S3.E13 "In 3 Lambda ES ‣ Lambda Expected Shortfall")), we have ESΛ​(X)<x\mathrm{ES}\_{\Lambda}(X)<x.
It follows that ESΛ​(X)/2+ESΛ​(Y)/2<ESΛ​((X+Y)/2)\mathrm{ES}\_{\Lambda}(X)/2+\mathrm{ES}\_{\Lambda}(Y)/2<\mathrm{ES}\_{\Lambda}((X+Y)/2), contradicting the convexity of ESΛ\mathrm{ES}\_{\Lambda}.
Therefore, Λ\Lambda is constant on ℝ\mathbb{R}.

“(ii) ⇒\Rightarrow (iii)”: Suppose that Λ\Lambda is not constant on ℝ\mathbb{R}. Since
Λ\Lambda is bounded, it cannot be concave.
Hence, there exist distinct points x,y,z∈ℝx,y,z\in\mathbb{R} and θ∈(0,1)\theta\in(0,1)
such that z=θ​x+(1−θ)​yz=\theta x+(1-\theta)y and Λ​(z)<θ​Λ​(x)+(1−θ)​Λ​(y).\Lambda(z)<\theta\Lambda(x)+(1-\theta)\Lambda(y). By the continuity of linear functions, there exists γ∈(0,1)\gamma\in(0,1) in any neighborhood of θ\theta
such that z<γ​x+(1−γ)​yz<\gamma x+(1-\gamma)y and Λ​(z)<γ​Λ​(x)+(1−γ)​Λ​(y).\Lambda(z)<\gamma\Lambda(x)+(1-\gamma)\Lambda(y). Write p=Λ​(x)p=\Lambda(x), q=Λ​(y)q=\Lambda(y) and r=γ​p+(1−γ)​qr=\gamma p+(1-\gamma)q.
Take independent events A,B,C∈ℱA,B,C\in\mathcal{F} such that ℙ​(A)=1−p\mathbb{P}(A)=1-p, ℙ​(B)=1−q\mathbb{P}(B)=1-q, and ℙ​(C)=γ\mathbb{P}(C)=\gamma.
For some constant K>max⁡{−x,−y}K>\max\{-x,-y\} (to be determined later), let

|  |  |  |
| --- | --- | --- |
|  | X=x​𝟏A−K​𝟏Ac,Y=y​𝟏B−K​𝟏Bc, and ​Z=𝟏C​X+𝟏Cc​Y.X=x\mathbf{1}\_{A}-K\mathbf{1}\_{A^{c}},~~Y=y\mathbf{1}\_{B}-K\mathbf{1}\_{B^{c}},\mbox{~~and~~}Z=\mathbf{1}\_{C}X+\mathbf{1}\_{C^{c}}Y. |  |

We can calculate ESp​(X)=x\mathrm{ES}\_{p}(X)=x and ESq​(Y)=y\mathrm{ES}\_{q}(Y)=y. By ([14](https://arxiv.org/html/2512.23139v2#S3.E14 "In 3 Lambda ES ‣ Lambda Expected Shortfall")), we have ESΛ​(X)=x\mathrm{ES}\_{\Lambda}(X)=x and ESΛ​(Y)=y\mathrm{ES}\_{\Lambda}(Y)=y. Note that the distribution of ZZ is the mixture of those of XX and YY with weights γ\gamma and (1−γ)(1-\gamma) respectively. We will show ESΛ​(Z)⩽z\mathrm{ES}\_{\Lambda}(Z)\leqslant z for large KK, which, together with z<γ​ESΛ​(X)+(1−γ)​ESΛ​(Y)z<\gamma\mathrm{ES}\_{\Lambda}(X)+(1-\gamma)\mathrm{ES}\_{\Lambda}(Y), disproves the concavity in mixtures of ESΛ\mathrm{ES}\_{\Lambda}.

Because ℙ​(Z=−K)=γ​ℙ​(X=−K)+(1−γ)​ℙ​(Y=−K)=γ​p+(1−γ)​q=r\mathbb{P}(Z=-K)=\gamma\mathbb{P}(X=-K)+(1-\gamma)\mathbb{P}(Y=-K)=\gamma p+(1-\gamma)q=r and Λ​(z)<r\Lambda(z)<r,

|  |  |  |
| --- | --- | --- |
|  | ESΛ​(z)​(Z)=11−Λ​(z)​(−(r−Λ​(z))​K+∫r1VaRβ​(Z)​dβ)⩽−K​r−Λ​(z)1−Λ​(z)+1−r1−Λ​(z)​max⁡{x,y},\mathrm{ES}\_{\Lambda(z)}(Z)=\frac{1}{1-\Lambda(z)}\left(-(r-\Lambda(z))K+{\int\_{r}^{1}\mathrm{VaR}\_{\beta}(Z)\,\mathrm{d}\beta}\right)\leqslant-K\frac{r-\Lambda(z)}{1-\Lambda(z)}+\frac{1-r}{1-\Lambda(z)}\max\{x,y\}, |  |

which tends to −∞-\infty as K→∞K\to\infty.
In particular, for some KK large enough, we have ESΛ​(z)​(Z)⩽z\mathrm{ES}\_{\Lambda(z)}(Z)\leqslant z. Using ([12](https://arxiv.org/html/2512.23139v2#S3.E12 "In Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")), we get ESΛ​(Z)⩽z\mathrm{ES}\_{\Lambda}(Z)\leqslant z.
∎

###### Remark 3.

Another feature of ES and VaR is that they are tail risk measures in the sense of Liu and Wang ([2021](https://arxiv.org/html/2512.23139v2#bib.bib31)).
More precisely, for α∈(0,1)\alpha\in(0,1),
an α\alpha-tail risk measure is a risk measure ρ\rho such that ρ​(X)=ρ​(Y)\rho(X)=\rho(Y) when the left quantile functions of XX and YY coincide on (α,1)(\alpha,1).
It is straightforward to verify that ESΛ\mathrm{ES}\_{\Lambda} (resp. VaRΛ\mathrm{VaR}\_{\Lambda}) is an α\alpha-tail risk measure if and only if Λ⩾α\Lambda\geqslant\alpha (resp. Λ>α\Lambda>\alpha) on ℝ\mathbb{R}.

## 4 Dual representation

We now study the dual representation of ESΛ\mathrm{ES}\_{\Lambda} as a quasi-convex and cash-subadditive risk measure, in the form of Cerreia-Vioglio et al. ([2011](https://arxiv.org/html/2512.23139v2#bib.bib8)).
Denote by ℳ1,f=ℳ1,f​(Ω,ℱ,ℙ)\mathcal{M}\_{1,f}=\mathcal{M}\_{1,f}(\Omega,\mathcal{F},\mathbb{P}) the set of all finitely additive probability measures that are absolutely continuous with respect to ℙ\mathbb{P}. The following result shows the dual representation of ESΛ\mathrm{ES}\_{\Lambda} as a direct consequence of its definition in ([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")).

###### Theorem 3.

For any decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1], the risk measure ESΛ\mathrm{ES}\_{\Lambda} adopts the following representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)=supℚ∈ℳ1,fR​(𝔼ℚ​[X],ℚ),X∈L∞,\mathrm{ES}\_{\Lambda}(X)=\sup\_{\mathbb{Q}\in\mathcal{M}\_{1,f}}R(\mathbb{E}\_{\mathbb{Q}}[X],\mathbb{Q}),~~~X\in L^{\infty}, |  | (15) |

where for (t,ℚ)∈ℝ×ℳ1,f(t,\mathbb{Q})\in\mathbb{R}\times\mathcal{M}\_{1,f},

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(t,ℚ)=supx∈ℝ{t∧x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely},\displaystyle R(t,\mathbb{Q})=\sup\_{x\in\mathbb{R}}\left\{t\wedge x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\}, |  | (16) |

where we write d​ℙ/d​ℚ=1/(d​ℚ/d​ℙ)\mathrm{d}\mathbb{P}/\mathrm{d}\mathbb{Q}=1/(\mathrm{d}\mathbb{Q}/\mathrm{d}\mathbb{P}) with 1/0=∞1/0=\infty.
Moreover, the following statements hold.

1. (i)

   The supremum in ([15](https://arxiv.org/html/2512.23139v2#S4.E15 "In Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall")) is a maximum if Λ\Lambda is left-continuous.
2. (ii)

   (t,ℚ)↦R​(t,ℚ)(t,\mathbb{Q})\mapsto R(t,\mathbb{Q}) is upper semicontinuous, quasi-concave, and increasing in tt;
3. (iii)

   inft∈ℝR​(t,ℚ)=inft∈ℝR​(t,ℚ′)\inf\_{t\in\mathbb{R}}R(t,\mathbb{Q})=\inf\_{t\in\mathbb{R}}R(t,\mathbb{Q}^{\prime}) for all ℚ,ℚ′∈ℳ1,f\mathbb{Q},\mathbb{Q}^{\prime}\in\mathcal{M}\_{1,f};
4. (iv)

   R​(t1,ℚ)−R​(t2,ℚ)⩽t1−t2R(t\_{1},\mathbb{Q})-R(t\_{2},\mathbb{Q})\leqslant t\_{1}-t\_{2} for all t1⩾t2t\_{1}\geqslant t\_{2} and ℚ∈ℳ1,f\mathbb{Q}\in\mathcal{M}\_{1,f}.

###### Proof.

Define

|  |  |  |
| --- | --- | --- |
|  | 𝒫Λ​(x)={ℚ∈ℳ1,f:d​ℚd​ℙ⩽11−Λ​(x),ℙ​-almost surely},x∈ℝ.\mathcal{P}\_{\Lambda(x)}=\left\{\mathbb{Q}\in\mathcal{M}\_{1,f}~:~\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\leqslant\frac{1}{1-\Lambda(x)},~\mathbb{P}\mbox{-almost surely}\right\},~~x\in\mathbb{R}. |  |

For any X∈L1X\in L^{1} and x∈ℝx\in\mathbb{R}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)\displaystyle\mathrm{ES}\_{\Lambda}(X) | =supx∈ℝ(ESΛ​(x)​(X)∧x)\displaystyle=\sup\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\wedge x\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =supx∈ℝ{maxℚ∈𝒫Λ​(x)⁡𝔼ℚ​[X]∧x}\displaystyle=\sup\_{x\in\mathbb{R}}\left\{\max\_{\mathbb{Q}\in\mathcal{P}\_{\Lambda(x)}}\mathbb{E}\_{\mathbb{Q}}[X]\wedge x\right\} |  | [Theorem 4.52 of Föllmer and Schied ([2016](https://arxiv.org/html/2512.23139v2#bib.bib20))] |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supx∈ℝmaxℚ∈𝒫Λ​(x)⁡{𝔼ℚ​[X]∧x}\displaystyle=\sup\_{x\in\mathbb{R}}\max\_{\mathbb{Q}\in\mathcal{P}\_{\Lambda(x)}}\left\{\mathbb{E}\_{\mathbb{Q}}[X]\wedge x\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supℚ∈ℳ1,fsupx∈ℝ{𝔼ℚ​[X]∧x:Λ​(x)⩾1−1d​ℚ/d​ℙ,ℙ​-almost surely},\displaystyle=\sup\_{\mathbb{Q}\in\mathcal{M}\_{1,f}}\sup\_{x\in\mathbb{R}}\left\{\mathbb{E}\_{\mathbb{Q}}[X]\wedge x~:~\Lambda(x)\geqslant 1-\frac{1}{\mathrm{d}\mathbb{Q}/\mathrm{d}\mathbb{P}},~\mathbb{P}\mbox{-almost surely}\right\}, |  |

where the supremum over x∈ℝx\in\mathbb{R} can be changed to a maximum when Λ\Lambda is left-continuous. This implies statement (i).
Further because

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ​(Λ​(x)⩾1−d​ℙd​ℚ)=1\displaystyle\mathbb{Q}\left(\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}}\right)=1 | ⇔𝔼ℙ​[𝟏{Λ​(x)⩾1−1d​ℚ/d​ℙ}​d​ℚd​ℙ]=1\displaystyle\iff\mathbb{E}\_{\mathbb{P}}\left[\mathbf{1}\_{\left\{\Lambda(x)\geqslant 1-\frac{1}{\mathrm{d}\mathbb{Q}/\mathrm{d}\mathbb{P}}\right\}}\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}\right]=1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔ℙ​({d​ℚd​ℙ=0​or​Λ​(x)⩾1−1d​ℚ/d​ℙ})=1\displaystyle\iff\mathbb{P}\left(\left\{\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}=0~\mbox{or}~\Lambda(x)\geqslant 1-\frac{1}{\mathrm{d}\mathbb{Q}/\mathrm{d}\mathbb{P}}\right\}\right)=1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔ℙ​(Λ​(x)⩾1−1d​ℚ/d​ℙ)=1,\displaystyle\iff\mathbb{P}\left(\Lambda(x)\geqslant 1-\frac{1}{\mathrm{d}\mathbb{Q}/\mathrm{d}\mathbb{P}}\right)=1, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | ESΛ​(X)=supℚ∈ℳ1,fsupx∈ℝ{𝔼ℚ​[X]∧x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}.\mathrm{ES}\_{\Lambda}(X)=\sup\_{\mathbb{Q}\in\mathcal{M}\_{1,f}}\sup\_{x\in\mathbb{R}}\left\{\mathbb{E}\_{\mathbb{Q}}[X]\wedge x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\}. |  |

Now it remains to check statements (ii)-(iv).

(ii) Upper semicontinuity can be seen by showing that for all t0∈ℝt\_{0}\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supt→t0R​(t,ℚ)\displaystyle\limsup\_{t\to t\_{0}}R(t,\mathbb{Q}) | =limδ↓0supx∈ℝ{(t0+δ)∧x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}\displaystyle=\lim\_{\delta\downarrow 0}\sup\_{x\in\mathbb{R}}\left\{(t\_{0}+\delta)\wedge x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limδ↓0supx∈ℝ{t0∧x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}=R​(t0,ℚ).\displaystyle=\lim\_{\delta\downarrow 0}\sup\_{x\in\mathbb{R}}\left\{t\_{0}\wedge x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\}=R(t\_{0},\mathbb{Q}). |  |

Monotonicity is straightforward, and quasi-concavity is implied by monotonicity.
Statement (iii) is clear because inft∈ℝR​(t,ℚ)=−∞\inf\_{t\in\mathbb{R}}R(t,\mathbb{Q})=-\infty for all ℚ∈ℳ1,f\mathbb{Q}\in\mathcal{M}\_{1,f}.

(iv) For all t1⩾t2t\_{1}\geqslant t\_{2} and ℚ∈ℳ1,f\mathbb{Q}\in\mathcal{M}\_{1,f},

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(t1,ℚ)−R​(t2,ℚ)=\displaystyle R(t\_{1},\mathbb{Q})-R(t\_{2},\mathbb{Q})= | t1∧supx∈ℝ{x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}\displaystyle~t\_{1}\wedge\sup\_{x\in\mathbb{R}}\left\{x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −t2∧supx∈ℝ{x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}⩽t1−t2.\displaystyle-t\_{2}\wedge\sup\_{x\in\mathbb{R}}\left\{x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\}\leqslant t\_{1}-t\_{2}. |  |

The proof is complete.
∎

###### Remark 4.

Suppose that Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] is decreasing and left-continuous. The function RR we obtained in ([16](https://arxiv.org/html/2512.23139v2#S4.E16 "In Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall")) is a special case of that obtained by Theorem 3.1 of Cerreia-Vioglio et al. ([2011](https://arxiv.org/html/2512.23139v2#bib.bib8)) for quasi-convex cash-subadditive risk measures:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(t,ℚ)=inf{ESΛ​(Y):𝔼ℚ​[Y]=t},(t,ℚ)∈ℝ×ℳ1,f.R(t,\mathbb{Q})=\inf\{\mathrm{ES}\_{\Lambda}(Y):\mathbb{E}\_{\mathbb{Q}}[Y]=t\},~(t,\mathbb{Q})\in\mathbb{R}\times\mathcal{M}\_{1,f}. |  | (17) |

Theorem [3](https://arxiv.org/html/2512.23139v2#Thmtheorem3 "Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall") automatically implies ([17](https://arxiv.org/html/2512.23139v2#S4.E17 "In Remark 4. ‣ 4 Dual representation ‣ Lambda Expected Shortfall")). Below, we show another self-contained proof for ([17](https://arxiv.org/html/2512.23139v2#S4.E17 "In Remark 4. ‣ 4 Dual representation ‣ Lambda Expected Shortfall")) to provide more mathematical insight. This proof can be seen as an alternative proof for Theorem [3](https://arxiv.org/html/2512.23139v2#Thmtheorem3 "Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall") with Λ\Lambda being left-continuous.
For any Y∈L∞Y\in L^{\infty}, due to boundedness of YY, there exist a,b∈ℝa,b\in\mathbb{R} with a<ba<b, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(Y)=supy∈[a,b](ESΛ​(y)​(Y)∧y).\mathrm{ES}\_{\Lambda}(Y)=\sup\_{y\in[a,b]}\left(\mathrm{ES}\_{\Lambda(y)}(Y)\wedge y\right). |  | (18) |

For any y1,y2∈[a,b]y\_{1},y\_{2}\in[a,b] with y1⩽y2y\_{1}\leqslant y\_{2} and γ∈[0,1]\gamma\in[0,1], because y↦ESΛ​(y)y\mapsto\mathrm{ES}\_{\Lambda(y)} is decreasing, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ESΛ​(γ​y1+(1−γ)​y2)​(Y)∧(γ​y1+(1−γ)​y2)\displaystyle\mathrm{ES}\_{\Lambda(\gamma y\_{1}+(1-\gamma)y\_{2})}(Y)\wedge\left(\gamma y\_{1}+(1-\gamma)y\_{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={ESΛ​(γ​y1+(1−γ)​y2)​(Y)⩾ESΛ​(y2)​(Y),if​ESΛ​(γ​y1+(1−γ)​y2)​(Y)⩽γ​y1+(1−γ)​y2,γ​y1+(1−γ)​y2⩾y1,otherwise\displaystyle=\left\{\begin{array}[]{ll}\mathrm{ES}\_{\Lambda(\gamma y\_{1}+(1-\gamma)y\_{2})}(Y)\geqslant\mathrm{ES}\_{\Lambda(y\_{2})}(Y),&\mbox{if}~~\mathrm{ES}\_{\Lambda(\gamma y\_{1}+(1-\gamma)y\_{2})}(Y)\leqslant\gamma y\_{1}+(1-\gamma)y\_{2},\\ \gamma y\_{1}+(1-\gamma)y\_{2}\geqslant y\_{1},&\mbox{otherwise}\end{array}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾(ESΛ​(y1)​(Y)∧y1)∧(ESΛ​(y2)​(Y)∧y2).\displaystyle\geqslant\left(\mathrm{ES}\_{\Lambda(y\_{1})}(Y)\wedge y\_{1}\right)\wedge\left(\mathrm{ES}\_{\Lambda(y\_{2})}(Y)\wedge y\_{2}\right). |  |

Thus the function y↦ESΛ​(y)​(Y)∧yy\mapsto\mathrm{ES}\_{\Lambda(y)}(Y)\wedge y is quasi-concave. For any (t,ℚ)∈ℝ×ℳ1,f(t,\mathbb{Q})\in\mathbb{R}\times\mathcal{M}\_{1,f}, it is clear that the set {Y∈L∞:𝔼ℚ​[Y]=t}\{Y\in L^{\infty}:\mathbb{E}\_{\mathbb{Q}}[Y]=t\} is convex and the mapping Y↦ESΛ​(y)​(Y)∧yY\mapsto\mathrm{ES}\_{\Lambda(y)}(Y)\wedge y is convex due to convexity of ES\mathrm{ES}. Hence,

|  |  |  |
| --- | --- | --- |
|  | inf{ESΛ​(Y):𝔼ℚ​[Y]=t}\displaystyle\inf\left\{\mathrm{ES}\_{\Lambda}(Y):\mathbb{E}\_{\mathbb{Q}}[Y]=t\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =inf{supy∈[a,b](ESΛ​(y)​(Y)∧y):𝔼ℚ​[Y]=t}\displaystyle=\inf\left\{\sup\_{y\in[a,b]}\left(\mathrm{ES}\_{\Lambda(y)}(Y)\wedge y\right):\mathbb{E}\_{\mathbb{Q}}[Y]=t\right\} |  | [by ([18](https://arxiv.org/html/2512.23139v2#S4.E18 "In Remark 4. ‣ 4 Dual representation ‣ Lambda Expected Shortfall"))] |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =supy∈[a,b](inf𝔼ℚ​[Y]=tESΛ​(y)​(Y)∧y)\displaystyle=\sup\_{y\in[a,b]}\left(\inf\_{\mathbb{E}\_{\mathbb{Q}}[Y]=t}\mathrm{ES}\_{\Lambda(y)}(Y)\wedge y\right) |  | [minimax theorem (Fan, [1953](https://arxiv.org/html/2512.23139v2#bib.bib17))] |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =supy∈[a,b](infc∈ℝinfY∈L∞(ESΛ​(y)​(Y)−c​(𝔼ℚ​[Y]−t))∧y)\displaystyle=\sup\_{y\in[a,b]}\left(\inf\_{c\in\mathbb{R}}\inf\_{Y\in L^{\infty}}\left(\mathrm{ES}\_{\Lambda(y)}(Y)-c(\mathbb{E}\_{\mathbb{Q}}[Y]-t)\right)\wedge y\right) |  | [Lagrange duality] |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =supy∈[a,b](infc∈ℝ(c​t−α​(c​ℚ))∧y)\displaystyle=\sup\_{y\in[a,b]}\left(\inf\_{c\in\mathbb{R}}\left(ct-\alpha(c\mathbb{Q})\right)\wedge y\right) |  | [α​(ℚ)=supY∈L∞(𝔼ℚ​[Y]−ESΛ​(y)​(Y))]\left[\displaystyle\alpha(\mathbb{Q})=\sup\_{Y\in L^{\infty}}(\mathbb{E}\_{\mathbb{Q}}[Y]-\mathrm{ES}\_{\Lambda(y)}(Y))\right] |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =supy∈[a,b]((t−α​(ℚ))∧y).\displaystyle=\sup\_{y\in[a,b]}\left(\left(t-\alpha(\mathbb{Q})\right)\wedge y\right). |  | [cash additivity of ES\mathrm{ES}] |

For all ℚ∈ℳ1,f\mathbb{Q}\in\mathcal{M}\_{1,f} and y∈[a,b]y\in[a,b], by Corollary 4.19 and Theorem 4.52 of Föllmer and Schied ([2016](https://arxiv.org/html/2512.23139v2#bib.bib20)), we have α​(ℚ)=0\alpha(\mathbb{Q})=0 if d​ℚ/d​ℙ⩽1/(1−Λ​(y))\mathrm{d}\mathbb{Q}/\mathrm{d}\mathbb{P}\leqslant 1/(1-\Lambda(y)), ℙ\mathbb{P}-almost surely and α​(ℚ)=∞\alpha(\mathbb{Q})=\infty otherwise. Therefore, we have

|  |  |  |
| --- | --- | --- |
|  | supy∈[a,b]((t−α​(ℚ))∧y)=maxx∈ℝ⁡{t∧x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}.\sup\_{y\in[a,b]}\left(\left(t-\alpha(\mathbb{Q})\right)\wedge y\right)=\max\_{x\in\mathbb{R}}\left\{t\wedge x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\}. |  |

## 5 The Rockafellar–Uryasev formula and optimization

### 5.1 Representing Lambda ES as a minimization

The well-known relation between VaR and ES obtained by
Rockafellar and Uryasev ([2002](https://arxiv.org/html/2512.23139v2#bib.bib35)) as shown in ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) provides a promising solution to ES-based optimization problems.
Let I​(ℝ¯)I(\overline{\mathbb{R}}) be the set of all closed real intervals, including intervals of [ℓ,∞][\ell,\infty], [ℓ,∞)[\ell,\infty), [−∞,ℓ][-\infty,\ell], (−∞,ℓ](-\infty,\ell], and [ℓ,ℓ]={ℓ}[\ell,\ell]=\{\ell\} for ℓ∈ℝ¯\ell\in\overline{\mathbb{R}}. A pair of risk measures (ϕ,ρ):𝒳→I​(ℝ¯)×ℝ¯(\phi,\rho):\mathcal{X}\to I(\overline{\mathbb{R}})\times\overline{\mathbb{R}} is called a *Bayes pair* (Embrechts et al., [2021](https://arxiv.org/html/2512.23139v2#bib.bib13)) if for some *loss function* S:ℝ¯2→ℝ¯S:\overline{\mathbb{R}}^{2}\to\overline{\mathbb{R}},

|  |  |  |
| --- | --- | --- |
|  | ϕ​(X)=arg​mina∈ℝ¯⁡𝔼​[S​(a,X)],and​ρ​(X)=mina∈ℝ¯⁡𝔼​[S​(a,X)],X∈𝒳.\phi(X)=\operatorname\*{arg\,min}\_{a\in\overline{\mathbb{R}}}\mathbb{E}[S(a,X)],~\mbox{and}~\rho(X)=\min\_{a\in\overline{\mathbb{R}}}\mathbb{E}[S(a,X)],~~X\in\mathcal{X}. |  |

If ϕ\phi is further cash additive (naturally defined for interval-valued functions), then we call ρ\rho a *Bayes risk measure*, and ϕ\phi the corresponding *Bayes estimator*.
It is clear that (VaR,ES)(\mathrm{VaR},\mathrm{ES}) is a Bayes pair by ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")). A natural question is whether we can also write ESΛ\mathrm{ES}\_{\Lambda} as the minimum of some loss function and find its corresponding minimizer.
Ideally, we may expect to find the relation between VaRΛ\mathrm{VaR}\_{\Lambda} and ESΛ\mathrm{ES}\_{\Lambda} similar to (VaR,ES)(\mathrm{VaR},\mathrm{ES}) in optimization.
Below we show a representation of ESΛ\mathrm{ES}\_{\Lambda} based on the relation ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")), which we call the RU formula of ESΛ\mathrm{ES}\_{\Lambda}. Define the mapping TΛ:ℝ×ℝ×L∞→(−∞,∞]T\_{\Lambda}:\mathbb{R}\times\mathbb{R}\times L^{\infty}\to(-\infty,\infty] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | TΛ:(a,x,X)↦𝔼​[a+11−Λ​(x)​(X−a)+]∨x.T\_{\Lambda}:(a,x,X)\mapsto\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x. |  | (19) |

The next result also demonstrates the convexity of TΛT\_{\Lambda} in different variables. We use the term “joint convexity” when there are multiple variables to emphasize its difference from marginal convexity.

###### Theorem 4.

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a right-continuous decreasing function and TΛT\_{\Lambda} be given in ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)=min(a,x)∈ℝ2⁡TΛ​(a,x,X)=min(a,x)∈ℝ2⁡{𝔼​[a+11−Λ​(x)​(X−a)+]∨x},X∈L∞,\mathrm{ES}\_{\Lambda}(X)=\min\_{(a,x)\in\mathbb{R}^{2}}T\_{\Lambda}(a,x,X)=\min\_{(a,x)\in\mathbb{R}^{2}}\left\{\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x\right\},~~X\in L^{\infty}, |  | (20) |

where the minima are obtained at x∗=ESΛ​(X)x^{\*}=\mathrm{ES}\_{\Lambda}(X) and

|  |  |  |
| --- | --- | --- |
|  | a∗​{∈[VaRΛ​(x∗)​(X),VaRΛ​(x∗)+​(X)],if​Λ​(x∗)∈[0,1),=VaR1​(X),if​Λ​(x∗)=1.a^{\*}\left\{\begin{array}[]{ll}\in[\mathrm{VaR}\_{\Lambda(x^{\*})}(X),\mathrm{VaR}^{+}\_{\Lambda(x^{\*})}(X)],&\mbox{if}~\Lambda(x^{\*})\in[0,1),\\ =\mathrm{VaR}\_{1}(X),&\mbox{if}~\Lambda(x^{\*})=1.\end{array}\right. |  |

Moreover,

1. (i)

   TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly convex in (a,X)∈ℝ×L∞(a,X)\in\mathbb{R}\times L^{\infty} for all x∈ℝx\in\mathbb{R};
2. (ii)

   TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is convex in x∈ℝx\in\mathbb{R} for all (a,X)∈ℝ×L∞(a,X)\in\mathbb{R}\times L^{\infty} if and only if the function x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex;
3. (iii)

   the following statements are equivalent:

   1. (a)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly convex in (a,x)∈ℝ2(a,x)\in\mathbb{R}^{2} for all X∈L∞X\in L^{\infty};
   2. (b)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly quasi-convex in (a,x)∈ℝ2(a,x)\in\mathbb{R}^{2} for all X∈L∞X\in L^{\infty};
   3. (c)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly convex in (a,x,X)∈ℝ×ℝ×L∞(a,x,X)\in\mathbb{R}\times\mathbb{R}\times L^{\infty};
   4. (d)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly quasi-convex in (a,x,X)∈ℝ×ℝ×L∞(a,x,X)\in\mathbb{R}\times\mathbb{R}\times L^{\infty};
   5. (e)

      Λ\Lambda is constant on ℝ\mathbb{R}.

###### Proof.

For any X∈L∞X\in L^{\infty}, we have by Theorem [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall"), formulation ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")), and Remark [2](https://arxiv.org/html/2512.23139v2#Thmremark2 "Remark 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)=minx∈ℝ⁡{ESΛ​(x)​(X)∨x}\displaystyle\mathrm{ES}\_{\Lambda}(X)=\min\_{x\in\mathbb{R}}\left\{\mathrm{ES}\_{\Lambda(x)}(X)\vee x\right\} | =minx∈ℝ⁡{mina∈ℝ⁡𝔼​[a+11−Λ​(x)​(X−a)+]∨x}\displaystyle=\min\_{x\in\mathbb{R}}\left\{\min\_{a\in\mathbb{R}}\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minx∈ℝ⁡mina∈ℝ⁡{𝔼​[a+11−Λ​(x)​(X−a)+]∨x}.\displaystyle=\min\_{x\in\mathbb{R}}\min\_{a\in\mathbb{R}}\left\{\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x\right\}. |  |

For the optimization problem above, the minimizer x∗=ESΛ​(X)x^{\*}=\mathrm{ES}\_{\Lambda}(X) is obtained by definition ([11](https://arxiv.org/html/2512.23139v2#S3.E11 "In Definition 1 (Λ-Expected Shortfall). ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")), and the minimizer a∗a^{\*} is obtained by ([8](https://arxiv.org/html/2512.23139v2#S2.E8 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")).

Statement (i) is straightforward. We prove statements (ii) - (iv).

(ii) The “if” part is clear by the convexity of x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)). To show the “only if” part, suppose ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) is convex in xx. Let
x¯=inf{x∈ℝ:Λ​(x)=0}.\bar{x}=\inf\{x\in\mathbb{R}:\Lambda(x)=0\}.
Right-continuity of Λ\Lambda yields that Λ​(x¯)=0\Lambda(\bar{x})=0.
We first prove x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex in x∈(−∞,x¯)x\in(-\infty,\bar{x}).
Suppose for contradiction that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 11−Λ​(x0+y02)>12​(1−Λ​(x0))+12​(1−Λ​(y0)),for some​x0,y0∈(−∞,x¯).\frac{1}{1-\Lambda\left(\frac{x\_{0}+y\_{0}}{2}\right)}>\frac{1}{2(1-\Lambda(x\_{0}))}+\frac{1}{2(1-\Lambda(y\_{0}))},~~\mbox{for some}~x\_{0},y\_{0}\in(-\infty,\bar{x}). |  | (21) |

Because it is clear that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lima↓−∞𝔼​[a+11−Λ​(x)​(X−a)+]=∞,for all​x∈(−∞,x¯),\lim\_{a\downarrow-\infty}\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]=\infty,~~\mbox{for all}~x\in(-\infty,\bar{x}), |  | (22) |

there exists a0∈ℝa\_{0}\in\mathbb{R}, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​[a0+11−Λ​(x0)​(X−a0)+]⩾x0,𝔼​[a0+11−Λ​(y0)​(X−a0)+]⩾y0,\displaystyle\mathbb{E}\left[a\_{0}+\frac{1}{1-\Lambda(x\_{0})}(X-a\_{0})\_{+}\right]\geqslant x\_{0},~\mathbb{E}\left[a\_{0}+\frac{1}{1-\Lambda(y\_{0})}(X-a\_{0})\_{+}\right]\geqslant y\_{0}, |  | (23) |
|  | and | 𝔼​[a0+11−Λ​((x0+y0)/2)​(X−a0)+]⩾x0+y02.\displaystyle\mathbb{E}\left[a\_{0}+\frac{1}{1-\Lambda\left((x\_{0}+y\_{0})/2\right)}(X-a\_{0})\_{+}\right]\geqslant\frac{x\_{0}+y\_{0}}{2}. |  |

([21](https://arxiv.org/html/2512.23139v2#S5.E21 "In Proof. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) and ([23](https://arxiv.org/html/2512.23139v2#S5.E23 "In Proof. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) together contradict the fact that ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) is convex in xx. Therefore, the function x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex in x∈(−∞,x¯)x\in(-\infty,\bar{x}).

Next, we show that x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex in x∈ℝx\in\mathbb{R}. Because x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is decreasing, it suffices to show that x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is continuous at x¯\bar{x} if x¯<∞\bar{x}<\infty. Suppose for contradiction that Λ​(x¯−)>0\Lambda(\bar{x}-)>0. Because of ([22](https://arxiv.org/html/2512.23139v2#S5.E22 "In Proof. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")), there exists a1∈(−∞,ess​-​sup​(X))a\_{1}\in(-\infty,\mathrm{ess\mbox{-}sup}(X)), such that
𝔼​[a1+(X−a1)+/(1−Λ​(x¯−))]>x¯.\mathbb{E}[a\_{1}+(X-a\_{1})\_{+}/(1-\Lambda(\bar{x}-))]>\bar{x}.
It is clear that 𝔼​[(X−a1)+]>0\mathbb{E}[(X-a\_{1})\_{+}]>0 and thus

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[a1+11−Λ​(x¯−)​(X−a1)+]>𝔼​[a1+(X−a1)+].\mathbb{E}\left[a\_{1}+\frac{1}{1-\Lambda(\bar{x}-)}(X-a\_{1})\_{+}\right]>\mathbb{E}\left[a\_{1}+(X-a\_{1})\_{+}\right]. |  |

It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limx↑x¯𝔼​[a1+11−Λ​(x)​(X−a1)+]∨x2+𝔼​[a1+(X−a1)+]∨x¯2\displaystyle\lim\_{x\uparrow\bar{x}}\frac{\mathbb{E}\left[a\_{1}+\frac{1}{1-\Lambda(x)}(X-a\_{1})\_{+}\right]\vee x}{2}+\frac{\mathbb{E}\left[a\_{1}+(X-a\_{1})\_{+}\right]\vee\bar{x}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <𝔼​[a1+11−Λ​(x¯−)​(X−a1)+]=limx↑x¯{𝔼​[a1+11−Λ​((x+x¯)/2)​(X−a1)+]∨x+x¯2}.\displaystyle<\mathbb{E}\left[a\_{1}+\frac{1}{1-\Lambda(\bar{x}-)}(X-a\_{1})\_{+}\right]=\lim\_{x\uparrow\bar{x}}\left\{\mathbb{E}\left[a\_{1}+\frac{1}{1-\Lambda((x+\bar{x})/2)}(X-a\_{1})\_{+}\right]\vee\frac{x+\bar{x}}{2}\right\}. |  |

This contradicts with the convexity of ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")). Therefore, x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex in x∈ℝx\in\mathbb{R}.

Next, we prove statement (iii). It is straightforward that (a) ⇒\Rightarrow (b) and (c) ⇒\Rightarrow (d).

“(e) ⇒\Rightarrow (a)”: This follows by the convexity of ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) in a∈ℝa\in\mathbb{R} and the fact that an increasing convex transform of a convex function is still convex. We show the “only if” part.

“(b) ⇒\Rightarrow (e)”: Suppose that ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) is jointly quasi-convex in (a,x)∈ℝ2(a,x)\in\mathbb{R}^{2} for all X∈L∞X\in L^{\infty}. Suppose for contradiction that Λ\Lambda is decreasing and non-constant on ℝ\mathbb{R}. There exists x,y,t∈ℝx,y,t\in\mathbb{R} with y<x⩽ty<x\leqslant t, such that Λ​(y)⩾Λ​((x+y)/2)>Λ​(x)\Lambda(y)\geqslant\Lambda((x+y)/2)>\Lambda(x). Take a<b=ta<b=t, and X∈L∞X\in L^{\infty} with ℙ​(X=a)=1−ℙ​(X=t)=Λ​(x)\mathbb{P}(X=a)=1-\mathbb{P}(X=t)=\Lambda(x). Because Λ​(x)<1\Lambda(x)<1, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[a+11−Λ​(x)​(X−a)+]∨x=𝔼​[b+11−Λ​(y)​(X−b)+]∨y=t,\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x=\mathbb{E}\left[b+\frac{1}{1-\Lambda(y)}(X-b)\_{+}\right]\vee y=t, |  |

whereas

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[a+b2+11−Λ​(x+y2)​(X−a+b2)+]∨x+y2\displaystyle\mathbb{E}\left[\frac{a+b}{2}+\frac{1}{1-\Lambda\left(\frac{x+y}{2}\right)}\left(X-\frac{a+b}{2}\right)\_{+}\right]\vee\frac{x+y}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={a+t2+1−Λ​(x)1−Λ​(x+y2)​(t−a+t2)}∨x+y2>t.\displaystyle=\left\{\frac{a+t}{2}+\frac{1-\Lambda(x)}{1-\Lambda\left(\frac{x+y}{2}\right)}\left(t-\frac{a+t}{2}\right)\right\}\vee\frac{x+y}{2}>t. |  |

This contradicts the joint quasi-convexity of ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) in (a,x)∈ℝ2(a,x)\in\mathbb{R}^{2}, and thus Λ\Lambda is constant on ℝ\mathbb{R}.

“(e) ⇒\Rightarrow (c)”: This follows by statement (i) and the fact that an increasing convex transform of a convex function is still convex.

“(d) ⇒\Rightarrow (e)”: This follows directly by the proof for the implication “(b) ⇒\Rightarrow (e)”.
∎

For the RU formula of Λ\Lambda-ES, Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall") indicates that we do not guarantee joint convexity (or quasi-convexity) of the objective ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) in (a,x)∈ℝ2(a,x)\in\mathbb{R}^{2} or (a,x,X)∈ℝ×ℝ×L∞(a,x,X)\in\mathbb{R}\times\mathbb{R}\times L^{\infty} unless Λ\Lambda is a constant (i.e., ESΛ\mathrm{ES}\_{\Lambda} is an ES). Nevertheless, the mapping ([19](https://arxiv.org/html/2512.23139v2#S5.E19 "In 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) is convex in x∈ℝx\in\mathbb{R} when the function x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex.
Two examples satisfying this condition are: Λ\Lambda is a constant (i.e. the usual ES)
and Λ​(x)=(ea​x+1)−1\Lambda(x)=(e^{ax}+1)^{-1} for a>0a>0.444The example Λ​(x)=(ea​x+1)−1\Lambda(x)=(e^{ax}+1)^{-1}, a>0a>0, x∈ℝx\in\mathbb{R}, provides a suggestion of a non-trivial choice of the ESΛ\mathrm{ES}\_{\Lambda} risk measure to use in practice. By Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall"), an obvious advantage of such a choice is that it makes the objective of a practical Λ\Lambda-ES-based optimization problem convex in the variable xx.
Moreover, Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall") shows that ESΛ\mathrm{ES}\_{\Lambda} has a similar feature to a Bayes risk measure introduced by Embrechts et al. ([2021](https://arxiv.org/html/2512.23139v2#bib.bib13)), as it can be represented as the minimum of an expected loss function with an additional transformation.
The corresponding minimizer is the interval of the left- and right-quantiles at the level of Λ​(x∗)\Lambda(x^{\*}) instead of [VaRΛ,VaRΛ+][\mathrm{VaR}\_{\Lambda},\mathrm{VaR}^{+}\_{\Lambda}].

A possible direction to explore the issue of Bayes pair is through the scoring function of Λ\Lambda-VaR\mathrm{VaR}.555A set-valued functional ρ:𝒳→2ℝ\rho:\mathcal{X}\to 2^{\mathbb{R}} is called *elicitable* on 𝒳\mathcal{X} if there exists a function (*scoring function*) S:ℝ¯2→ℝ¯S:\overline{\mathbb{R}}^{2}\to\overline{\mathbb{R}}, such that

ρ​(X)=arg​mina∈ℝ¯⁡𝔼​[S​(a,X)],X∈𝒳.\rho(X)=\operatorname\*{arg\,min}\_{a\in\overline{\mathbb{R}}}\mathbb{E}[S(a,X)],~~X\in\mathcal{X}.
 Bellini and Bignozzi ([2015](https://arxiv.org/html/2512.23139v2#bib.bib3)) and Burzoni et al. ([2017](https://arxiv.org/html/2512.23139v2#bib.bib6)) showed that for a decreasing function Λ:ℝ→(0,1)\Lambda:\mathbb{R}\to(0,1), VaRΛ\mathrm{VaR}\_{\Lambda} is elicitable with the scoring function

|  |  |  |
| --- | --- | --- |
|  | SΛ​(a,y)=(a−y)+−∫yaΛ​(t)​dt=(y−a)+−∫ay(1−Λ​(t))​dt,a∈ℝ¯,y∈ℝ.S\_{\Lambda}(a,y)=(a-y)\_{+}-\int\_{y}^{a}\Lambda(t)\,\mathrm{d}t=(y-a)\_{+}-\int\_{a}^{y}(1-\Lambda(t))\,\mathrm{d}t,~~a\in\overline{\mathbb{R}},~y\in\mathbb{R}. |  |

The pair of risk measures we get with the above scoring function is (VaRΛ,ρ)(\mathrm{VaR}\_{\Lambda},\rho), where

|  |  |  |
| --- | --- | --- |
|  | ρΛ​(X)=mina∈ℝ¯⁡𝔼​[c​SΛ​(a,X)+f​(X)],X∈L∞,\rho\_{\Lambda}(X)=\min\_{a\in\overline{\mathbb{R}}}\mathbb{E}[cS\_{\Lambda}(a,X)+f(X)],~~X\in L^{\infty}, |  |

for some constant c>0c>0 and real function f:ℝ→ℝf:\mathbb{R}\to\mathbb{R}. The risk measure (VaRΛ,ρΛ)(\mathrm{VaR}\_{\Lambda},\rho\_{\Lambda}) is not a Bayes pair because VaRΛ\mathrm{VaR}\_{\Lambda} is not cash additive in general. Moreover, we find that ρΛ\rho\_{\Lambda} cannot satisfy quasi-convexity, normalization, and ρΛ⩾VaRΛ\rho\_{\Lambda}\geqslant\mathrm{VaR}\_{\Lambda} simultaneously, and thus does not coincide with ESΛ\mathrm{ES}\_{\Lambda} for any choices of cc and ff. We put the detailed arguments for this conflict in Appendix [A](https://arxiv.org/html/2512.23139v2#A1 "Appendix A Other possible formulations of Lambda ES ‣ Lambda Expected Shortfall").

### 5.2 Optimization with Lambda ES

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a decreasing function. We demonstrate general ideas of solving optimization problems with Λ\Lambda-ES as a constraint or an objective. For n∈ℕn\in\mathbb{N}, let 𝐋=(L1,…,Ln)∈(L∞)n\mathbf{L}=(L\_{1},\dots,L\_{n})\in(L^{\infty})^{n} represent a vector of losses, 𝜽∈Θ\bm{\theta}\in\Theta represent a decision variable, where Θ\Theta is a convex set of actions, and f:Θ×ℝn→ℝf:\Theta\times\mathbb{R}^{n}\to\mathbb{R} represent a loss function. For a typical example in finance, we can use 𝐋\mathbf{L} as the vector of losses from multiple assets and 𝜽\bm{\theta} as a portfolio weight vector.

First, we are interested in a problem where the decision maker minimizes an objective risk measure ρ:L∞→ℝ¯\rho:L^{\infty}\to\overline{\mathbb{R}} of the aggregate loss f​(𝜽,𝐋)f(\bm{\theta},\mathbf{L}), guaranteeing that the Λ\Lambda-ES of the total loss does not exceed a pre-specified value ℓ∈ℝ\ell\in\mathbb{R}. Namely, we consider the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝜽∈Θ⁡ρ​(f​(𝜽,𝐋))​subject to​ESΛ​(f​(𝜽,𝐋))⩽ℓ.\min\_{\bm{\theta}\in\Theta}\rho(f(\bm{\theta},\mathbf{L}))~~~\mbox{subject to}~\mathrm{ES}\_{\Lambda}(f(\bm{\theta},\mathbf{L}))\leqslant\ell. |  | (24) |

The following result provides a possible direction to simplify the problem above.

###### Proposition 4.

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a right-continuous decreasing function. The constraint ESΛ​(f​(𝛉,𝐋))⩽ℓ\mathrm{ES}\_{\Lambda}(f(\bm{\theta},\mathbf{L}))\leqslant\ell in ([24](https://arxiv.org/html/2512.23139v2#S5.E24 "In 5.2 Optimization with Lambda ES ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) is equivalent to ESΛ​(ℓ)​(f​(𝛉,𝐋))⩽ℓ\mathrm{ES}\_{\Lambda(\ell)}(f(\bm{\theta},\mathbf{L}))\leqslant\ell.

###### Proof.

By definition, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(f​(𝜽,𝐋))⩽ℓ\displaystyle\mathrm{ES}\_{\Lambda}(f(\bm{\theta},\mathbf{L}))\leqslant\ell | ⇔supx∈ℝ(ESΛ​(x)​(f​(𝜽,𝐋))∧x)⩽ℓ\displaystyle\iff\sup\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(f(\bm{\theta},\mathbf{L}))\wedge x\right)\leqslant\ell |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔for all x∈ℝ:ESΛ​(x)(f(𝜽,𝐋))⩽ℓorx⩽ℓ\displaystyle\iff\mbox{for all }x\in\mathbb{R}:~\mathrm{ES}\_{\Lambda(x)}(f(\bm{\theta},\mathbf{L}))\leqslant\ell~\mbox{or}~x\leqslant\ell |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔supx>ℓESΛ​(x)(f(𝜽,𝐋))⩽ℓ⇔ESΛ​(ℓ)(f(𝜽,𝐋))⩽ℓ,\displaystyle\iff\sup\_{x>\ell}\mathrm{ES}\_{\Lambda(x)}(f(\bm{\theta},\mathbf{L}))\leqslant\ell\iff\mathrm{ES}\_{\Lambda(\ell)}(f(\bm{\theta},\mathbf{L}))\leqslant\ell, |  |

where the last equivalence holds by right-continuity of Λ\Lambda.
∎

Proposition [4](https://arxiv.org/html/2512.23139v2#Thmproposition4 "Proposition 4. ‣ 5.2 Optimization with Lambda ES ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall") implies that an optimization problem with a Λ\Lambda-ES constraint of level ℓ∈ℝ\ell\in\mathbb{R} can be equivalently converted to a problem with the constraint on ESΛ​(ℓ)\mathrm{ES}\_{\Lambda(\ell)} of the same level ℓ\ell. ES-constrained optimization problem has been studed extensively in the literature (see e.g., Krokhmal et al., [2002](https://arxiv.org/html/2512.23139v2#bib.bib30)).

Another natural question to study is how to minimize Λ\Lambda-ES as an objective:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝜽∈Θ⁡ESΛ​(f​(𝜽,𝐋)).\min\_{\bm{\theta}\in\Theta}\mathrm{ES}\_{\Lambda}(f(\bm{\theta},\mathbf{L})). |  | (25) |

The result below provides general insights into solving Λ\Lambda-ES-based optimization problems. In specific problems, we may also consider some constraints along with the problem ([25](https://arxiv.org/html/2512.23139v2#S5.E25 "In 5.2 Optimization with Lambda ES ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")), which does not change the nature of our equivalence result. Define the mapping T~Λ:Θ×ℝ×ℝ×(L∞)n→ℝ¯\widetilde{T}\_{\Lambda}:\Theta\times\mathbb{R}\times\mathbb{R}\times(L^{\infty})^{n}\to\overline{\mathbb{R}} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | T~Λ​(𝜽,a,x,𝐋)=𝔼​[a+11−Λ​(x)​(f​(𝜽,𝐋)−a)+]∨x.\widetilde{T}\_{\Lambda}(\bm{\theta},a,x,\mathbf{L})=\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(f(\bm{\theta},\mathbf{L})-a)\_{+}\right]\vee x. |  | (26) |

###### Proposition 5.

For a right-continuous decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝜽∈Θ⁡ESΛ​(f​(𝜽,𝐋))=min(𝜽,a,x)∈Θ×ℝ×ℝ⁡{𝔼​[a+11−Λ​(x)​(f​(𝜽,𝐋)−a)+]∨x}.\min\_{\bm{\theta}\in\Theta}\mathrm{ES}\_{\Lambda}(f(\bm{\theta},\mathbf{L}))=\min\_{(\bm{\theta},a,x)\in\Theta\times\mathbb{R}\times\mathbb{R}}\left\{\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(f(\bm{\theta},\mathbf{L})-a)\_{+}\right]\vee x\right\}. |  | (27) |

Moreover, for T~Λ\widetilde{T}\_{\Lambda} defined in ([26](https://arxiv.org/html/2512.23139v2#S5.E26 "In 5.2 Optimization with Lambda ES ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")),

1. (i)

   T~Λ​(𝜽,a,x,𝐋)\widetilde{T}\_{\Lambda}(\bm{\theta},a,x,\mathbf{L}) is convex in a∈ℝa\in\mathbb{R} for all (𝜽,x,𝐋)∈Θ×ℝ×(L∞)n(\bm{\theta},x,\mathbf{L})\in\Theta\times\mathbb{R}\times(L^{\infty})^{n}.
2. (ii)

   if in addition, Λ\Lambda is not constantly 11, then T~Λ​(𝜽,a,x,𝐋)\widetilde{T}\_{\Lambda}(\bm{\theta},a,x,\mathbf{L}) is jointly convex in (𝜽,𝐋)∈Θ×(L∞)n(\bm{\theta},\mathbf{L})\in\Theta\times(L^{\infty})^{n} for all (a,x)∈ℝ2(a,x)\in\mathbb{R}^{2} if and only if f​(𝜽,𝐋)f(\bm{\theta},\mathbf{L}) is jointly convex in (𝜽,𝐋)(\bm{\theta},\mathbf{L}).
3. (iii)

   T~Λ​(𝜽,a,x,𝐋)\widetilde{T}\_{\Lambda}(\bm{\theta},a,x,\mathbf{L}) is convex in x∈ℝx\in\mathbb{R} for all (𝜽,a,𝐋)∈Θ×ℝ×(L∞)n(\bm{\theta},a,\mathbf{L})\in\Theta\times\mathbb{R}\times(L^{\infty})^{n} if and only if the function x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex.

###### Proof.

The equation ([27](https://arxiv.org/html/2512.23139v2#S5.E27 "In Proposition 5. ‣ 5.2 Optimization with Lambda ES ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) holds directly by Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall"). Statements (i) and (iii) follow by Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall"). Statement (ii) is straightforward.
∎

## 6 Extensions to the space of integrable random variabls

In this section, we extend our discussions on ES and Λ\Lambda-ES from the space of L∞L^{\infty} to L1L^{1}.
Similarly to the corresponding definitions on L∞L^{\infty}, we define ES at level α∈[0,1]\alpha\in[0,1] as the mapping
ESα:L1→ℝ¯\mathrm{ES}\_{\alpha}:L^{1}\to\overline{\mathbb{R}} given by

|  |  |  |
| --- | --- | --- |
|  | ESα​(X)=11−α​∫α1VaRβ​(X)​dβ​ for α∈[0,1),\mathrm{ES}\_{\alpha}(X)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\mathrm{VaR}\_{\beta}(X)\,\mathrm{d}\beta\mbox{ for $\alpha\in[0,1)$}, |  |

and ES1​(X)=VaR1​(X)\mathrm{ES}\_{1}(X)=\mathrm{VaR}\_{1}(X); for a decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1], we define ESΛ:L1→ℝ¯\mathrm{ES}\_{\Lambda}:L^{1}\to\overline{\mathbb{R}} as

|  |  |  |
| --- | --- | --- |
|  | ESΛ​(X)=supx∈ℝ{ESΛ​(x)​(X)∧x},X∈L1.\mathrm{ES}\_{\Lambda}(X)=\sup\_{x\in\mathbb{R}}\left\{\mathrm{ES}\_{\Lambda(x)}(X)\wedge x\right\},~~X\in L^{1}. |  |

Some of the results in the previous sections can be naturally extended to L1L^{1}, whereas others only hold under a weakened setup, for which we provide independent proofs for completeness. For the convenience of our discussion, we first note that the properties in Propositions [2](https://arxiv.org/html/2512.23139v2#Thmproposition2 "Proposition 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") and [3](https://arxiv.org/html/2512.23139v2#Thmproposition3 "Proposition 3. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") still hold for ESΛ\mathrm{ES}\_{\Lambda} on L1L^{1} by the same arguments in its proof replacing L∞L^{\infty} by L1L^{1}.

### 6.1 Finiteness of Lambda ES

Below we show the finiteness of Λ\Lambda-ES on L1L^{1}. As a result, the risk measure ESΛ\mathrm{ES}\_{\Lambda} is always well-defined (possibly being ∞\infty) on L1L^{1}.

###### Proposition 6.

Let Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1] be a decreasing function.
The mapping ESΛ:L1→ℝ¯\mathrm{ES}\_{\Lambda}:L^{1}\to\overline{\mathbb{R}}
satisfies

|  |  |  |
| --- | --- | --- |
|  | −∞<𝔼​[X]⩽ESΛ​(X)⩽ES1​(X),X∈L1.-\infty<\mathbb{E}[X]\leqslant\mathrm{ES}\_{\Lambda}(X)\leqslant\mathrm{ES}\_{1}(X),~~~X\in L^{1}. |  |

In particular, ESΛ​(X)\mathrm{ES}\_{\Lambda}(X) is finite on L1L^{1} if and only if VaR1​(X)<∞\mathrm{VaR}\_{1}(X)<\infty or
Λ\Lambda is not constantly 11.

###### Proof.

The relation −∞<𝔼⩽ESΛ⩽ES1-\infty<\mathbb{E}\leqslant\mathrm{ES}\_{\Lambda}\leqslant\mathrm{ES}\_{1} holds by item (a) of Proposition [2](https://arxiv.org/html/2512.23139v2#Thmproposition2 "Proposition 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") on L1L^{1}. We prove the “if” part of the second statement, whose “only if” part is straightforward.

For any X∈L1X\in L^{1}, first, suppose that VaR1​(X)<∞\mathrm{VaR}\_{1}(X)<\infty. It is straightforward that ESΛ​(X)⩽ES1​(X)=VaR1​(X)<∞\mathrm{ES}\_{\Lambda}(X)\leqslant\mathrm{ES}\_{1}(X)=\mathrm{VaR}\_{1}(X)<\infty. Next, suppose that Λ\Lambda is not constantly 11. There exists x0∈ℝx\_{0}\in\mathbb{R}, such that 0⩽Λ​(x0)<10\leqslant\Lambda(x\_{0})<1. It follows that ESΛ​(x0)​(X)<∞\mathrm{ES}\_{\Lambda(x\_{0})}(X)<\infty. By ([12](https://arxiv.org/html/2512.23139v2#S3.E12 "In Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall")),

|  |  |  |
| --- | --- | --- |
|  | ESΛ​(X)=infx∈ℝ(ESΛ​(x)​(X)∨x)⩽ESΛ​(x0)​(X)∨x0<∞.\mathrm{ES}\_{\Lambda}(X)=\inf\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\vee x\right)\leqslant\mathrm{ES}\_{\Lambda(x\_{0})}(X)\vee x\_{0}<\infty. |  |

The proof is complete.
∎

### 6.2 Dominance of ES and Lambda ES

Here, we examine the L1L^{1} versions of the dominance results in Theorems [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") and [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall").
Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") does not hold in general if we extend the space of ESα\mathrm{ES}\_{\alpha} from L∞L^{\infty} to L1L^{1} because the dominance may fail at α=0\alpha=0. A counterexample can be: Let ρ:L1→ℝ¯\rho:L^{1}\to\overline{\mathbb{R}} be a risk measure defined as follows.

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)={ess​-​sup​(X),if ​ess​-​sup​(X)=∞​or​ess​-​inf​(X)>−∞,−∞,if ​ess​-​sup​(X)<∞​and​ess​-​inf​(X)=−∞,​X∈L1.\rho(X)=\left\{\begin{array}[]{ll}\mathrm{ess\mbox{-}sup}(X),&\mbox{if }\mathrm{ess\mbox{-}sup}(X)=\infty~\mbox{or}~\mathrm{ess\mbox{-}inf}(X)>-\infty,\\ -\infty,&\mbox{if }\mathrm{ess\mbox{-}sup}(X)<\infty~\mbox{and}~\mathrm{ess\mbox{-}inf}(X)=-\infty,\end{array}\right.~X\in L^{1}. |  |

One can check that ρ\rho is quasi-convex, law invariant, and ρ⩾VaR0+\rho\geqslant\mathrm{VaR}^{+}\_{0}. However, the condition ρ⩾𝔼\rho\geqslant\mathbb{E} fails. Therefore, 𝔼\mathbb{E} is not the smallest quasi-convex and law-invariant risk measure dominating VaR0+\mathrm{VaR}^{+}\_{0} and thus ([10](https://arxiv.org/html/2512.23139v2#S2.E10 "In Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")) in Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") fails for α=0\alpha=0.

Below, we state the dominance results for ES over VaR and Λ\Lambda-ES over Λ\Lambda-VaR on the space of L1L^{1}. Both results rely on slightly stronger assumptions than Theorems [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") and [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") regarding the case of α=0\alpha=0. Write L¯1\underline{L}^{1} as the set of all random variables in L1L^{1} that are essentially bounded from below.

###### Theorem 5.

For any α∈(0,1]\alpha\in(0,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα=min⁡{ρ:L1→ℝ¯∣ρ⩾VaRα​and ρ is quasi-convex and law invariant}.\displaystyle\mathrm{ES}\_{\alpha}=\min\{\rho:L^{1}\to\overline{\mathbb{R}}\mid\rho\geqslant\mathrm{VaR}\_{\alpha}~\mbox{and $\rho$ is quasi-convex and law invariant}\}. |  | (28) |

For any α∈(0,1)\alpha\in(0,1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα=min⁡{ρ:L1→ℝ¯∣ρ⩾VaRα+​and ρ is quasi-convex and law invariant}.\displaystyle\mathrm{ES}\_{\alpha}=\min\{\rho:L^{1}\to\overline{\mathbb{R}}\mid\rho\geqslant\mathrm{VaR}^{+}\_{\alpha}~\mbox{and $\rho$ is quasi-convex and law invariant}\}. |  | (29) |

For any α∈[0,1)\alpha\in[0,1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα=min⁡{ρ:L¯1→ℝ¯∣ρ⩾VaRα+​and ρ is quasi-convex and law invariant}.\displaystyle\mathrm{ES}\_{\alpha}=\min\{\rho:\underline{L}^{1}\to\overline{\mathbb{R}}\mid\rho\geqslant\mathrm{VaR}^{+}\_{\alpha}~\mbox{and $\rho$ is quasi-convex and law invariant}\}. |  | (30) |

###### Proof.

The proofs of ([28](https://arxiv.org/html/2512.23139v2#S6.E28 "In Theorem 5. ‣ 6.2 Dominance of ES and Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")), ([29](https://arxiv.org/html/2512.23139v2#S6.E29 "In Theorem 5. ‣ 6.2 Dominance of ES and Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")), and the case of α∈(0,1)\alpha\in(0,1) in ([30](https://arxiv.org/html/2512.23139v2#S6.E30 "In Theorem 5. ‣ 6.2 Dominance of ES and Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")) follow directly from those for Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall") whose arguments still hold on L1L^{1}. We only need to prove ([30](https://arxiv.org/html/2512.23139v2#S6.E30 "In Theorem 5. ‣ 6.2 Dominance of ES and Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")) for α=0\alpha=0.

For any n∈ℕn\in\mathbb{N} and X∈L¯1X\in\underline{L}^{1} with distribution FF, write Kn=n+VaR0+​(X)K\_{n}=\sqrt{n}+\mathrm{VaR}^{+}\_{0}(X). By Corollary A.3 of Embrechts et al. ([2015](https://arxiv.org/html/2512.23139v2#bib.bib16)), there exist X~i∼dF\widetilde{X}\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F, i∈[n]i\in[n], such that

|  |  |  |
| --- | --- | --- |
|  | |1n​∑i=1n(X~i∧Kn)−𝔼​[X∧Kn]|⩽nn=1n.\left|\frac{1}{n}\sum^{n}\_{i=1}\left(\widetilde{X}\_{i}\wedge K\_{n}\right)-\mathbb{E}\left[X\wedge K\_{n}\right]\right|\leqslant\frac{\sqrt{n}}{n}=\frac{1}{\sqrt{n}}. |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1n(X~i∧Kn)⩾𝔼​[X∧Kn]−1n,\frac{1}{n}\sum^{n}\_{i=1}\left(\widetilde{X}\_{i}\wedge K\_{n}\right)\geqslant\mathbb{E}\left[X\wedge K\_{n}\right]-\frac{1}{\sqrt{n}}, |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X∧Kn]⩾1n​VaR0+​((X~1∧Kn)+⋯+(X~n∧Kn))⩾𝔼​[X∧Kn]−1n.\mathbb{E}\left[X\wedge K\_{n}\right]\geqslant\frac{1}{n}\mathrm{VaR}^{+}\_{0}\left(\left(\widetilde{X}\_{1}\wedge K\_{n}\right)+\cdots+\left(\widetilde{X}\_{n}\wedge K\_{n}\right)\right)\geqslant\mathbb{E}\left[X\wedge K\_{n}\right]-\frac{1}{\sqrt{n}}. |  |

Letting n→∞n\to\infty, by monotone convergence theorem, we have

|  |  |  |
| --- | --- | --- |
|  | 1n​sup{VaR0+​(X1+⋯+Xn):Xi∼dF,i∈[n]}→𝔼​[X].\frac{1}{n}\sup\left\{\mathrm{VaR}^{+}\_{0}\left({X}\_{1}+\cdots+{X}\_{n}\right):X\_{i}\mathrel{\mathop{\kern 0.0pt\sim}\limits^{\mathrm{d}}}F,~i\in[n]\right\}\to\mathbb{E}[X]. |  |

The rest of the proof follows from that for Theorem [1](https://arxiv.org/html/2512.23139v2#Thmtheorem1 "Theorem 1. ‣ 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall").
∎

With Theorem [5](https://arxiv.org/html/2512.23139v2#Thmtheorem5 "Theorem 5. ‣ 6.2 Dominance of ES and Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall"), we obtain
the following result, which extends the domain in Theorem [2](https://arxiv.org/html/2512.23139v2#Thmtheorem2 "Theorem 2. ‣ 3 Lambda ES ‣ Lambda Expected Shortfall") from L∞L^{\infty} to L1L^{1} or L¯1\underline{L}^{1}.

###### Theorem 6.

The following statements hold.

1. (i)

   For a decreasing function Λ:ℝ→(0,1]\Lambda:\mathbb{R}\to(0,1], the smallest quasi-convex and law-invariant risk measure on L1L^{1} dominating VaRΛ\mathrm{VaR}\_{\Lambda} is ESΛ\mathrm{ES}\_{\Lambda}, that is,
   ES\_Λ= min{ρ: L^1→R∣ρ⩾VaR\_Λ and ρ\rho is quasi-convex and law invariant}.
2. (ii)

   For a decreasing function Λ:ℝ→(0,1)\Lambda:\mathbb{R}\to(0,1), the smallest quasi-convex and law-invariant risk measure on L1L^{1} dominating VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} is ESΛ\mathrm{ES}\_{\Lambda}, that is,
   ES\_Λ= min{ρ: L^1→R∣ρ⩾VaR^+\_Λ and ρ\rho is quasi-convex and law invariant}.
3. (iii)

   For a decreasing function Λ:ℝ→[0,1)\Lambda:\mathbb{R}\to[0,1), the smallest quasi-convex and law-invariant risk measure on L¯1\underline{L}^{1} dominating VaRΛ+\mathrm{VaR}^{+}\_{\Lambda} is ESΛ\mathrm{ES}\_{\Lambda}, that is,
   ES\_Λ= min{ρ: L^1→R∣ρ⩾VaR^+\_Λ and ρ\rho is quasi-convex and law invariant}.

Moreover, the identity holds for all decreasing functions Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1]:

|  |  |  |
| --- | --- | --- |
|  | ESΛ​(X)=infx∈ℝ(ESΛ​(x)​(X)∨x),X∈L1.\mathrm{ES}\_{\Lambda}(X)=\inf\_{x\in\mathbb{R}}\left(\mathrm{ES}\_{\Lambda(x)}(X)\vee x\right),~~~X\in L^{1}. |  |

### 6.3 Dual representation and RU formula for Lambda ES

In this section, we restate the dual representation (Theorem [3](https://arxiv.org/html/2512.23139v2#Thmtheorem3 "Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall")) and the RU formula (Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) for Λ\Lambda-ES on L1L^{1}. The proofs of both results below follow from the same arguments as those for Theorems [3](https://arxiv.org/html/2512.23139v2#Thmtheorem3 "Theorem 3. ‣ 4 Dual representation ‣ Lambda Expected Shortfall") and [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall") by replacing L∞L^{\infty} with L1L^{1}.

###### Theorem 7.

For any decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1], the risk measure ESΛ\mathrm{ES}\_{\Lambda} adopts the following representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESΛ​(X)=supℚ∈ℳ1,fR​(𝔼ℚ​[X],ℚ),X∈L1,\mathrm{ES}\_{\Lambda}(X)=\sup\_{\mathbb{Q}\in\mathcal{M}\_{1,f}}R(\mathbb{E}\_{\mathbb{Q}}[X],\mathbb{Q}),~~~X\in L^{1}, |  | (31) |

where for (t,ℚ)∈ℝ×ℳ1,f(t,\mathbb{Q})\in\mathbb{R}\times\mathcal{M}\_{1,f},

|  |  |  |
| --- | --- | --- |
|  | R​(t,ℚ)=supx∈ℝ{t∧x:Λ​(x)⩾1−d​ℙd​ℚ,ℚ​-almost surely}.R(t,\mathbb{Q})=\sup\_{x\in\mathbb{R}}\left\{t\wedge x~:~\Lambda(x)\geqslant 1-\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}},~\mathbb{Q}\mbox{-almost surely}\right\}. |  |

Moreover, the following are true:

1. (i)

   The supremum in ([31](https://arxiv.org/html/2512.23139v2#S6.E31 "In Theorem 7. ‣ 6.3 Dual representation and RU formula for Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")) can be changed to a maximum if Λ\Lambda is left-continuous.
2. (ii)

   (t,ℚ)↦R​(t,ℚ)(t,\mathbb{Q})\mapsto R(t,\mathbb{Q}) is upper semicontinuous, quasi-concave, and increasing in tt;
3. (iii)

   inft∈ℝR​(t,ℚ)=inft∈ℝR​(t,ℚ′)\inf\_{t\in\mathbb{R}}R(t,\mathbb{Q})=\inf\_{t\in\mathbb{R}}R(t,\mathbb{Q}^{\prime}) for all ℚ,ℚ′∈ℳ1,f\mathbb{Q},\mathbb{Q}^{\prime}\in\mathcal{M}\_{1,f};
4. (iv)

   R​(t1,ℚ)−R​(t2,ℚ)⩽t1−t2R(t\_{1},\mathbb{Q})-R(t\_{2},\mathbb{Q})\leqslant t\_{1}-t\_{2} for all t1⩾t2t\_{1}\geqslant t\_{2} and ℚ∈ℳ1,f\mathbb{Q}\in\mathcal{M}\_{1,f}.

With a slight abuse of notation, we define the mapping TΛ:ℝ¯×ℝ×L1→ℝ¯T\_{\Lambda}:\overline{\mathbb{R}}\times\mathbb{R}\times L^{1}\to\overline{\mathbb{R}} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | TΛ:(a,x,X)↦𝔼​[a+11−Λ​(x)​(X−a)+]∨x.T\_{\Lambda}:(a,x,X)\mapsto\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x. |  | (32) |

###### Proposition 7.

For any right-continuous decreasing function Λ:ℝ→[0,1]\Lambda:\mathbb{R}\to[0,1], the risk measure ESΛ\mathrm{ES}\_{\Lambda} can be represented as follows.

|  |  |  |
| --- | --- | --- |
|  | ESΛ​(X)=min(a,x)∈ℝ¯×ℝ⁡T​(a,x,X)=min(a,x)∈ℝ¯×ℝ⁡{𝔼​[a+11−Λ​(x)​(X−a)+]∨x},X∈L1,\mathrm{ES}\_{\Lambda}(X)=\min\_{(a,x)\in\overline{\mathbb{R}}\times\mathbb{R}}T(a,x,X)=\min\_{(a,x)\in\overline{\mathbb{R}}\times\mathbb{R}}\left\{\mathbb{E}\left[a+\frac{1}{1-\Lambda(x)}(X-a)\_{+}\right]\vee x\right\},~~X\in L^{1}, |  |

where the minima are obtained at x∗=ESΛ​(X)x^{\*}=\mathrm{ES}\_{\Lambda}(X) and

|  |  |  |
| --- | --- | --- |
|  | a∗​{∈[VaRΛ​(x∗)​(X),VaRΛ​(x∗)+​(X)],if​Λ​(x∗)∈[0,1),=VaR1​(X),if​Λ​(x∗)=1.a^{\*}\left\{\begin{array}[]{ll}\in[\mathrm{VaR}\_{\Lambda(x^{\*})}(X),\mathrm{VaR}^{+}\_{\Lambda(x^{\*})}(X)],&\mbox{if}~\Lambda(x^{\*})\in[0,1),\\ =\mathrm{VaR}\_{1}(X),&\mbox{if}~\Lambda(x^{\*})=1.\end{array}\right. |  |

Moreover, for TΛT\_{\Lambda} defined in ([32](https://arxiv.org/html/2512.23139v2#S6.E32 "In 6.3 Dual representation and RU formula for Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")),

1. (i)

   TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly convex in (a,X)∈ℝ¯×L1(a,X)\in\overline{\mathbb{R}}\times L^{1} for all x∈ℝx\in\mathbb{R};
2. (ii)

   TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is convex in x∈ℝx\in\mathbb{R} for all (a,X)∈ℝ¯×L1(a,X)\in\overline{\mathbb{R}}\times L^{1} if and only if the function x↦1/(1−Λ​(x))x\mapsto 1/(1-\Lambda(x)) is convex;
3. (iii)

   the following statements are equivalent:

   1. (a)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly convex in (a,x)∈ℝ¯×ℝ(a,x)\in\overline{\mathbb{R}}\times\mathbb{R} for all X∈L1X\in L^{1};
   2. (b)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly quasi-convex in (a,x)∈ℝ¯×ℝ(a,x)\in\overline{\mathbb{R}}\times\mathbb{R} for all X∈L1X\in L^{1};
   3. (c)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly convex in (a,x,X)∈ℝ¯×ℝ×L1(a,x,X)\in\overline{\mathbb{R}}\times\mathbb{R}\times L^{1};
   4. (d)

      TΛ​(a,x,X)T\_{\Lambda}(a,x,X) is jointly quasi-convex in (a,x,X)∈ℝ¯×ℝ×L1(a,x,X)\in\overline{\mathbb{R}}\times\mathbb{R}\times L^{1};
   5. (e)

      Λ\Lambda is constant on ℝ\mathbb{R}.

## 7 Conclusion

This paper introduces the Λ\Lambda-ES, a new and theoretically grounded generalization of ES that robustly extends the Λ\Lambda-VaR framework.
We obtain an explicit representation of Λ\Lambda-ES and verify that it satisfies several crucial properties as a desired counterpart to Λ\Lambda-VaR. In particular, we show that Λ\Lambda-ES is the smallest quasi-convex and law-invariant risk measure that dominates Λ\Lambda-VaR. The dual representation of Λ\Lambda-ES further connects it to established results on quasi-convex cash-subadditive risk measures. The RU formula of Λ\Lambda-ES provides useful insights for its potential applications to optimization problems.
Practically, Λ\Lambda-ES shares the advantages of Λ\Lambda-VaR as a flexible model for risk assessment, and it has additional benefits in risk management such as quasi-convexity, L1L^{1}-continuity, and dual representation, thus sharing the advantages of ES over VaR.

### Acknowledgments

RW acknowledges financial support from the Natural Sciences and Engineering Research Council (NSERC) of Canada (Grant Nos. RGPIN-2024-03728, CRC-2022-00141).

## References

* Acerbi and Tasche (2002)

  Acerbi, C. and Tasche, D. (2002). On the coherence of expected shortfall. *Journal of Banking and Finance*, 26(7), 1487–1503.
* Artzner et al. (1999)
  Artzner, P., Delbaen, F., Eber, J.-M. and Heath, D. (1999). Coherent measures of risk. *Mathematical Finance*, 9(3), 203–228.
* Bellini and Bignozzi (2015)
   Bellini, F. and Bignozzi, V. (2015). On elicitable risk measures. *Quantitative Finance*, 15(5), 725–733.
* Bellini and Peri (2022)

  Bellini, F. and Peri, I. (2022). An axiomatization of Λ\Lambda-quantiles. *SIAM Journal on Financial Mathematics*, 13(1), 26–38.
* Boonen et al. (2025)

  Boonen, T. J., Chen, Y., Han, X. and Wang, Q. (2025). Optimal insurance design with Lambda-Value-at-Risk. *European Journal of Operational Research*, 327(1), 232–246.
* Burzoni et al. (2017)

  Burzoni, M., Peri, I., and Ruffo, C. M. (2017). On the properties of the Lambda
  Value at Risk: robustness, elicitability and consistency. *Quantitative Finance*, 17(11), 1735–1743.
* Burzoni et al. (2022)

  Burzoni, M., Munari, C. and Wang, R. (2022). Adjusted Expected Shortfall. *Journal of Banking and Finance*, 134, 106297.
* Cerreia-Vioglio et al. (2011)

  Cerreia-Vioglio, S., Maccheroni, F., Marinacci, M. and Montrucchio, L. (2011). Risk measures:
  Rationality and diversification. *Mathematical Finance*, 21(4), 743–774.
* Corbetta and Peri (2018)

  Corbetta, J. and Peri, I. (2018). Backtesting Lambda value at risk. *European Journal of Finance*, 24(13), 1075–1087.
* Daníelsson et al. (2001)

  Daníelsson, J., Embrechts, P., Goodhart, C., Keating, C., Muennich, F., Renault, O. and Shin, H. S. (2001). An academic response to Basel II.
  *LSE Special Paper Series May 2001.*
* Delbaen (2012)

  Delbaen, F. (2012). *Monetary Utility Functions*. Osaka University Press, Osaka.
* El Karoui and Ravanelli (2009)
   El Karoui, N. and Ravanelli, C. (2009). Cash subadditive risk measures and interest rate ambiguity. *Mathematical Finance*, 19(4), 562–590.
* Embrechts et al. (2021)

  Embrechts, P., Mao, T., Wang, Q. and Wang, R. (2021). Bayes risk, elicitability, and the Expected Shortfall. *Mathematical Finance*, 31, 1190–1217.
* Embrechts et al. (2018)

  Embrechts, P., Liu, H. and Wang, R. (2018). Quantile-based risk sharing. *Operations Research*, 66(4), 936–949.
* Embrechts et al. (2022)
   Embrechts, P., Schied, A. and Wang, R. (2022). Robustness in the optimization of risk measures. *Operations Research*, 70(1), 95–110.
* Embrechts et al. (2015)
   Embrechts, P., Wang, B. and Wang, R. (2015). Aggregation-robustness and model uncertainty of regulatory risk measures. Finance and Stochastics, 19(4), 763–790.
* Fan (1953)

  Fan, K. (1953). Minimax theorems. *Proceedings of the National Academy of Sciences*, 39(1), 42–47.
* Fissler and Ziegel (2016)

  Fissler, T. and Ziegel, J. F. (2016). Higher order elicitability and Osband’s principle. *Annals of Statistics*, 44(4), 1680–1707.
* Föllmer and Schied (2002)
   Föllmer, H. and Schied, A. (2002).
  Convex measures of risk and trading constraints. *Finance and Stochastics*, 6(4), 429–447.
* Föllmer and Schied (2016)
   Föllmer, H. and Schied, A. (2016). *Stochastic Finance. An Introduction in Discrete Time*. Fourth Edition. Walter de Gruyter, Berlin.
* Frittelli et al. (2014)

  Frittelli, M., Maggis, M. and Peri, I. (2014). Risk measures on 𝒫​(ℝ)\mathcal{P}(\mathbb{R}) and value at risk with probability/loss function. *Mathematical Finance*, 24(3), 442–463.
* Frittelli and Rosazza Gianin (2002)

  Frittelli, M. and Rosazza Gianin, E. (2002). Putting order in risk measures. *Journal of Banking and Finance*, 26, 1473–1486.
* Gneiting (2011)

  Gneiting, T. (2011).
  Making and evaluating point forecasts.
  Journal of the American Statistical Association, 106(494), 746–762.
* Han and Liu (2025)

  Han, X. and Liu, P. (2025). Robust Lambda-quantiles and extreme probabilities. *Mathematical Finance*, forthcoming.
* Han et al. (2025)

  Han, X., Wang, Q., Wang, R. and Xia, J. (2025). Cash-subadditive risk measures without quasi-convexity. *Mathematics of Operations Research*, forthcoming.
* Hitaj et al. (2018)

  Hitaj, A., Mateus, C. and Peri, I. (2018). Lambda value at risk and regulatory capital: a dynamic approach to tail risk. *Risks*, 6(1), 17.
* Ince et al. (2022)

  Ince, A., Peri, I. and Pesenti, S. (2022). Risk contributions of lambda quantiles. *Quantitative Finance*, 22(10), 1871–1891.
* Kou and Peng (2016)

  Kou, S. and Peng, X. (2016). On the measurement of economic tail risk. *Operations Research*, 64(5), 1056–1072.
* Krätschmer et al. (2014)

  Krätschmer, V., Schied, A. and  Zähle, H. (2014).
  Comparative and quantitiative robustness for law-invariant risk
  measures.
  *Finance and Stochastics*, 18(2), 271–295.
* Krokhmal et al. (2002)

  Krokhmal, P., Palmquist, J. and Uryasev, S. (2002). Portfolio optimization with conditional value-at-risk objective and constraints. *Journal of Risk*, 4, 43–68.
* Liu and Wang (2021)

  Liu, F. and Wang, R. (2021). A theory for measures of tail risk. *Mathematics of Operations Research*, 46(3), 1109–1128.
* Liu (2025)

  Liu, P. (2025). Risk sharing with Lambda Value at Risk. *Mathematics of Operations Research*, 50(1), 313–333.
* Mao and Wang (2020)

  Mao, T. and Wang, R. (2020). Risk aversion in regulatory capital calculation. *SIAM Journal on Financial Mathematics*, 11(1), 169–200.
* McNeil et al. (2015)

  McNeil, A. J., Frey, R. and Embrechts, P. (2015). *Quantitative
  Risk Management: Concepts, Techniques and Tools*. Revised Edition. Princeton, NJ:
  Princeton University Press.
* Rockafellar and Uryasev (2002)

  Rockafellar, R. T. and Uryasev, S. (2002). Conditional value-at-risk for general loss distributions. *Journal of Banking and Finance*, 26(7), 1443–1471.
* Rüschendorf (2013)

  Rüschendorf, L. (2013).
  Mathematical Risk Analysis. Dependence, Risk Bounds, Optimal
  Allocations and Portfolios.
  Springer, Heidelberg.
* Wang and Wang (2015)

  Wang, B. and Wang, R. (2015). Extreme negative dependence and risk aggregation.
  Journal of Multivariate Analysis. 136, 12–25.
* Wang et al. (2020)

  Wang, R., Wei, Y. and Willmot, G. E. (2020). Characterization, robustness and aggregation of signed Choquet integrals. *Mathematics of Operations Research*, 45(3), 993–1015.
* Wang and Zitikis (2021)

  Wang, R. and Zitikis, R. (2021). An axiomatic foundation for the Expected Shortfall. *Management Science*, 67, 1413–1429.
* Ziegel (2016)

  Ziegel, J. (2016). Coherence and elicitability. Mathematical Finance, 26, 901–918.

## Appendix A Other possible formulations of Lambda ES

There may be many ways of generalizing ES using a parameter Λ\Lambda.
Below we explain a few possible ways of defining Λ\Lambda-ES that fail to satisfy basic requirements, and thus they are not suitable definitions.

### A.1 An algebraic formulation

We first consider an algebraic way of defining ES.
We can rewrite ESα\mathrm{ES}\_{\alpha} as (Acerbi and Tasche, [2002](https://arxiv.org/html/2512.23139v2#bib.bib1))

|  |  |  |
| --- | --- | --- |
|  | ESα​(X)=11−α​𝔼​[X​𝟙{X⩾VaRα​(X)}]+VaRα​(X)​(1−α−ℙ​(X⩾VaRα​(X))).\displaystyle\mathrm{ES}\_{\alpha}(X)=\frac{1}{1-\alpha}\mathbb{E}\left[X\mathds{1}\_{\{X\geqslant\mathrm{VaR}\_{\alpha}(X)\}}\right]+\mathrm{VaR}\_{\alpha}(X)(1-\alpha-\mathbb{P}(X\geqslant\mathrm{VaR}\_{\alpha}(X))). |  |

Denote by Lc1L^{1}\_{c} the set of all random variables in L1L^{1} with continuous distributions. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα​(X)=𝔼​[X∣X⩾VaRα​(X)],X∈Lc1.\displaystyle\mathrm{ES}\_{\alpha}(X)=\mathbb{E}\left[X\mid X\geqslant\mathrm{VaR}\_{\alpha}(X)\right],~~~X\in L^{1}\_{c}. |  | (A.1) |

To define Λ\Lambda-ES on continuous random variables using the idea of formulation ([A.1](https://arxiv.org/html/2512.23139v2#A1.E1 "In A.1 An algebraic formulation ‣ Appendix A Other possible formulations of Lambda ES ‣ Lambda Expected Shortfall")), a choice is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρΛ​(X)=𝔼​[X∣X⩾VaRΛ​(X)],X∈Lc1.\displaystyle\rho\_{\Lambda}(X)=\mathbb{E}\left[X\mid X\geqslant\mathrm{VaR}\_{\Lambda}(X)\right],~~~X\in L^{1}\_{c}. |  | (A.2) |

However, this formulation is not monotone, as the following example shows.
Let Ω=[0,1]\Omega=[0,1] with ℙ\mathbb{P} the Lebesgue measure. Let 0<ϵ<100<\epsilon<10.
For ω∈Ω\omega\in\Omega define

|  |  |  |
| --- | --- | --- |
|  | X​(ω)=ϵ​(ω−0.1)+𝟙(0.1,0.9]​(ω)+10⋅𝟙(0.9,1]​(ω)​ and ​Y​(ω)=ϵ​(ω−1)+10⋅𝟙(0.9,1]​(ω),X(\omega)=\epsilon(\omega-0.1)+\mathds{1}\_{(0.1,0.9]}(\omega)+10\cdot\mathds{1}\_{(0.9,1]}(\omega)\mbox{~and~}Y(\omega)=\epsilon(\omega-1)+10\cdot\mathds{1}\_{(0.9,1]}(\omega), |  |

so that X⩾YX\geqslant Y. Let Λ\Lambda be a strictly decreasing function with Λ​(1)=0.1\Lambda(1)=0.1 and Λ​(0)=0.9\Lambda(0)=0.9. We can compute

|  |  |  |
| --- | --- | --- |
|  | VaRΛ​(X)=1​so​that​ρΛ​(X)=2+0.45​ϵ.\mathrm{VaR}\_{\Lambda}(X)=1\mathrm{~so~that~}\rho\_{\Lambda}(X)=2+0.45\epsilon. |  |

On the other hand,

|  |  |  |
| --- | --- | --- |
|  | VaRΛ​(Y)=0​so​that​ρΛ​(Y)=10−0.05​ϵ.\mathrm{VaR}\_{\Lambda}(Y)=0\mathrm{~so~that~}\rho\_{\Lambda}(Y)=10-0.05\epsilon. |  |

Taking ϵ↓0\epsilon\downarrow 0 yields that ρΛ\rho\_{\Lambda} in ([A.2](https://arxiv.org/html/2512.23139v2#A1.E2 "In A.1 An algebraic formulation ‣ Appendix A Other possible formulations of Lambda ES ‣ Lambda Expected Shortfall")) is not monotone and is therefore undesirable.

### A.2 A formulation based on the Rockafellar–Uryasev formula

Another possible formulation of Λ\Lambda-ES is based on the RU formula in ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall")). Namely, for a decreasing function Λ:ℝ→(0,1)\Lambda:\mathbb{R}\to(0,1), we may define the following candidate risk measure

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρΛ​(X)=infx∈ℝ{x+11−Λ​(x)​𝔼​[(X−x)+]},X∈L1.\displaystyle\rho\_{\Lambda}(X)=\inf\_{x\in\mathbb{R}}\left\{x+\frac{1}{1-\Lambda(x)}\mathbb{E}[(X-x)\_{+}]\right\},~~~X\in L^{1}. |  | (A.3) |

Here, we use infimum because the minimum may not exist in general.
Clearly, ρΛ\rho\_{\Lambda} is monotone in both Λ\Lambda and XX, is law invariant, and specializes to ESα\mathrm{ES}\_{\alpha} when Λ≡α\Lambda\equiv\alpha for α∈(0,1)\alpha\in(0,1). Comparing ([A.3](https://arxiv.org/html/2512.23139v2#A1.E3 "In A.2 A formulation based on the Rockafellar–Uryasev formula ‣ Appendix A Other possible formulations of Lambda ES ‣ Lambda Expected Shortfall")) to Theorem [4](https://arxiv.org/html/2512.23139v2#Thmtheorem4 "Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall"), we are optimizing ([20](https://arxiv.org/html/2512.23139v2#S5.E20 "In Theorem 4. ‣ 5.1 Representing Lambda ES as a minimization ‣ 5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall")) over the subset {(a,x)∈ℝ2:a=x}\{(a,x)\in\mathbb{R}^{2}:a=x\} so that the optimum is larger. We have ESΛ⩽ρΛ\mathrm{ES}\_{\Lambda}\leqslant\rho\_{\Lambda} so that ρΛ\rho\_{\Lambda} also dominates VaRΛ\mathrm{VaR}\_{\Lambda}. However,
the following counterexample shows that ρΛ\rho\_{\Lambda} defined in ([A.3](https://arxiv.org/html/2512.23139v2#A1.E3 "In A.2 A formulation based on the Rockafellar–Uryasev formula ‣ Appendix A Other possible formulations of Lambda ES ‣ Lambda Expected Shortfall")) is not quasi-convex in general, and is thus not an ideal candidate for Λ\Lambda-ES.

Let a0,b0,α,β,ϵ∈ℝa\_{0},b\_{0},\alpha,\beta,\epsilon\in\mathbb{R} with b0<a0b\_{0}<a\_{0}, ϵ>0\epsilon>0, and 3/4<β<α<13/4<\beta<\alpha<1. Let

|  |  |  |
| --- | --- | --- |
|  | Λ0​(a)=α+(β−α)​𝟙{a>a0},a∈ℝ.\Lambda\_{0}(a)=\alpha+(\beta-\alpha)\mathds{1}\_{\{a>a\_{0}\}},~~a\in\mathbb{R}. |  |

It is clear that

|  |  |  |
| --- | --- | --- |
|  | ρΛ0​(X)=infx⩽a0{x+11−α​𝔼​[(X−x)+]}∧infx>a0{x+11−β​𝔼​[(X−x)+]},X∈L1.\rho\_{\Lambda\_{0}}(X)=\inf\_{x\leqslant a\_{0}}\left\{x+\frac{1}{1-\alpha}\mathbb{E}[(X-x)\_{+}]\right\}\wedge\inf\_{x>a\_{0}}\left\{x+\frac{1}{1-\beta}\mathbb{E}[(X-x)\_{+}]\right\},~~~X\in L^{1}. |  |

Take Y,Z∈L∞Y,Z\in L^{\infty} such that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Z=a0−ϵ)=1−ℙ​(Z=b0)=3/4,Y=a0+3​ϵ.\mathbb{P}(Z=a\_{0}-\epsilon)=1-\mathbb{P}(Z=b\_{0})=3/4,~Y=a\_{0}+3\epsilon. |  |

It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ρΛ0​(Z)=ESα​(Z)=a0−ϵ,ρΛ0​(Y)=a0+3​ϵ,\displaystyle\rho\_{\Lambda\_{0}}(Z)=\mathrm{ES}\_{\alpha}(Z)=a\_{0}-\epsilon,~\rho\_{\Lambda\_{0}}(Y)=a\_{0}+3\epsilon, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | and | ρΛ0​(Y+Z2)=a0+11−β​𝔼​[(Y+Z2−a0)+]=a0+3/41−β​ϵ>a0+3​ϵ.\displaystyle\rho\_{\Lambda\_{0}}\left(\frac{Y+Z}{2}\right)=a\_{0}+\frac{1}{1-\beta}\mathbb{E}\left[\left(\frac{Y+Z}{2}-a\_{0}\right)\_{+}\right]=a\_{0}+\frac{3/4}{1-\beta}\epsilon>a\_{0}+3\epsilon. |  |

This indicates that ρΛ0\rho\_{\Lambda\_{0}} is not quasi-convex.

### A.3 A formulation based on the score function of Lambda VaR

Let Λ:ℝ→(0,1)\Lambda:\mathbb{R}\to(0,1) be a decreasing function.
As discussed in Section [5](https://arxiv.org/html/2512.23139v2#S5 "5 The Rockafellar–Uryasev formula and optimization ‣ Lambda Expected Shortfall"), a natural possible formulation of Λ\Lambda-ES is

|  |  |  |
| --- | --- | --- |
|  | ρΛ​(X)=mina∈ℝ¯⁡𝔼​[c​SΛ​(a,X)+f​(X)],X∈L∞,\rho\_{\Lambda}(X)=\min\_{a\in\overline{\mathbb{R}}}\mathbb{E}[cS\_{\Lambda}(a,X)+f(X)],~~X\in L^{\infty}, |  |

where c>0c>0 is a constant, f:ℝ→ℝf:\mathbb{R}\to\mathbb{R} is a real function, and

|  |  |  |
| --- | --- | --- |
|  | SΛ​(a,y)=(a−y)+−∫yaΛ​(t)​dt=(y−a)+−∫ay(1−Λ​(t))​dt,a∈ℝ¯,y∈ℝ,S\_{\Lambda}(a,y)=(a-y)\_{+}-\int\_{y}^{a}\Lambda(t)\,\mathrm{d}t=(y-a)\_{+}-\int\_{a}^{y}(1-\Lambda(t))\,\mathrm{d}t,~~a\in\overline{\mathbb{R}},~y\in\mathbb{R}, |  |

is the scoring function for VaRΛ\mathrm{VaR}\_{\Lambda} with

|  |  |  |
| --- | --- | --- |
|  | VaRΛ​(X)∈arg​mina∈ℝ¯⁡𝔼​[SΛ​(a,X)],X∈L∞.\mathrm{VaR}\_{\Lambda}(X)\in\operatorname\*{arg\,min}\_{a\in\overline{\mathbb{R}}}\mathbb{E}[S\_{\Lambda}(a,X)],~~X\in L^{\infty}. |  |

The following argument shows that ρΛ\rho\_{\Lambda} cannot satisfy quasi-convexity, normalization, and ρΛ⩾VaRΛ\rho\_{\Lambda}\geqslant\mathrm{VaR}\_{\Lambda} simultaneously and is thus not a good candidate for Λ\Lambda-ES.

1. (i)

   Suppose that ρΛ\rho\_{\Lambda} is normalized. For all a∈ℝa\in\mathbb{R}, VaRΛ​(a)=a\mathrm{VaR}\_{\Lambda}(a)=a, and thus
   a=ρ\_Λ(a)=cS\_Λ(a,a)+f(a)=f(a).
   Therefore, we have f​(a)=af(a)=a for all a∈ℝa\in\mathbb{R}.
2. (ii)

   Suppose that ρΛ\rho\_{\Lambda} is normalized and ρΛ⩾VaRΛ\rho\_{\Lambda}\geqslant\mathrm{VaR}\_{\Lambda}. It implies that ρα∗⩾VaRα∗\rho\_{\alpha^{\*}}\geqslant\mathrm{VaR}\_{\alpha^{\*}} for all α∗∈[infx∈ℝΛ​(x),supx∈ℝΛ​(x)]\alpha^{\*}\in[\inf\_{x\in\mathbb{R}}\Lambda(x),\sup\_{x\in\mathbb{R}}\Lambda(x)]. For all X∈L∞X\in L^{\infty},

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[c​(X−VaRα∗​(X))+−c​(1−α∗)​(X−VaRα∗​(X))+X]\displaystyle\mathbb{E}\left[c(X-\mathrm{VaR}\_{\alpha^{\*}}(X))\_{+}-c(1-\alpha^{\*})(X-\mathrm{VaR}\_{\alpha^{\*}}(X))+X\right] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | =ρα∗​(X)⩾ESα∗​(X)\displaystyle=\rho\_{\alpha^{\*}}(X)\geqslant\mathrm{ES}\_{\alpha^{\*}}(X) |  | [Theorem [5](https://arxiv.org/html/2512.23139v2#Thmtheorem5 "Theorem 5. ‣ 6.2 Dominance of ES and Lambda ES ‣ 6 Extensions to the space of integrable random variabls ‣ Lambda Expected Shortfall")] |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | =𝔼​[11−α∗​(X−VaRα∗​(X))+−(X−VaRα∗​(X))+X]\displaystyle=\mathbb{E}\left[\frac{1}{1-\alpha^{\*}}(X-\mathrm{VaR}\_{\alpha^{\*}}(X))\_{+}-(X-\mathrm{VaR}\_{\alpha^{\*}}(X))+X\right] |  | [by ([5](https://arxiv.org/html/2512.23139v2#S2.E5 "In 2.3 Expected Shortfall ‣ 2 VaR, Lambda VaR and ES ‣ Lambda Expected Shortfall"))] |

   Therefore, c⩾1/(1−α∗)c\geqslant 1/(1-\alpha^{\*}) for all α∗∈[infx∈ℝΛ​(x),supx∈ℝΛ​(x)]\alpha^{\*}\in[\inf\_{x\in\mathbb{R}}\Lambda(x),\sup\_{x\in\mathbb{R}}\Lambda(x)], and thus c⩾1/(1−supx∈ℝΛ​(x))c\geqslant 1/(1-\sup\_{x\in\mathbb{R}}\Lambda(x)).
3. (iii)

   Suppose that ρΛ\rho\_{\Lambda} is quasi-convex, normalized, and ρΛ⩾VaRΛ\rho\_{\Lambda}\geqslant\mathrm{VaR}\_{\Lambda}.
   Let x0,y0,t0∈ℝx\_{0},y\_{0},t\_{0}\in\mathbb{R}, and α1,α2,α3∈(0,1)\alpha\_{1},\alpha\_{2},\alpha\_{3}\in(0,1) with
   0<x0<t0<y00<x\_{0}<t\_{0}<y\_{0}, α1<1/4<1/2<α2<α3\alpha\_{1}<1/4<1/2<\alpha\_{2}<\alpha\_{3},
   and Λ\_0(x)=α\_31\_{x¡0}+α\_21\_{0⩽x¡t\_0}+α\_11\_{x⩾t\_0}.
   Take X,Y∈L∞X,Y\in L^{\infty} such that P(X=x\_0)=P(X=-x\_0)=14, P(X=y\_0)=12, and Y=2X1\_{X=y\_0}-X.
   It follows that VaR\_Λ\_0(X)=VaR\_Λ\_0(Y)=VaR\_Λ\_0(X+Y2)=t\_0.
   For x∈ℝx\in\mathbb{R}, write
   g(x)=cSΛ0(t0,x)+f(x)=c(x-t0)+-c∫xt0(1-Λ0(t)) dt+x=1{x¡0}((1-c(1-α3))x+c(1-α2)t0)+1{0⩽x¡t0}((1-c(1-α2))x+c(1-α2)t0)+1{x⩾t0}((1+cα1)x-cα1t0),  x∈R.
   Because c⩾1/(1−supx∈ℝΛ0​(x))c\geqslant 1/(1-\sup\_{x\in\mathbb{R}}\Lambda\_{0}(x)) by (ii), we have c⩾1/(1−α3)c\geqslant 1/(1-\alpha\_{3}) and thus g​(−x0)+g​(x0)<2​g​(0)g(-x\_{0})+g(x\_{0})<2g(0). It follows that
   ρ\_Λ\_0(X)=ρ\_Λ\_0(Y)=g(-x0)+g(x0)4+g(y0)2¡g(0)+g(y0)2=ρ\_Λ\_0(X+Y2).
   This leads to a contradiction to the quasi-convexity of ρΛ0\rho\_{\Lambda\_{0}} and thus ρΛ\rho\_{\Lambda} cannot be quasi-convex, normalized, and ρΛ⩾VaRΛ\rho\_{\Lambda}\geqslant\mathrm{VaR}\_{\Lambda} simultaneously for all decreasing functions Λ:ℝ→(0,1)\Lambda:\mathbb{R}\to(0,1).