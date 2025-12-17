---
authors:
- Heeyoung Kwon
- Kasper Larsen
doc_id: arxiv:2512.14680v1
family_id: arxiv:2512.14680
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2512.14680v1
url_html: https://arxiv.org/html/2512.14680v1
venue: arXiv q-fin
version: 1
year: 2025
---

Long-run survival in limited stock market participation models with power utilities111Kasper Larsen is corresponding author and has contract information: Email: KL756@math.rutgers.edu and mailing address: Department of Mathematics, Rutgers University, Hill Center 330 - Busch Campus, 110 Frelinghuysen Road, Piscataway, NJ 08854-8019, USA. We thank Paolo Guasoni for discussions.

Heeyoung Kwon
  
Rutgers University

Kasper Larsen
  
Rutgers University

December 16, 2025

> Abstract: We extend the limited participation model in Basak and Cuoco (1998) to allow for traders with different time-preference coefficients but identical constant relative risk-aversion coefficients. Our main result gives parameter restrictions which ensure the existence of a Radner equilibrium. As an application, we give further parameter restrictions which ensure all traders survive in the long run.

Keywords: Singular ODE, incomplete equilibrium, long-run survival

Declaration of interest: Heeyoung Kwon has no conflicts of interest. Kasper Larsen has no conflicts of interest.

Declaration of generative AI in scientific writing: No AI nor AI-assisted tools have been used.

Data availability statement: We do not analyze nor generate any datasets.

## 1 Introduction

Basak and Cuoco (1998) construct a continuous-time Radner equilibrium model with two traders. One trader can access both the stock and money markets whereas the second trader cannot hold stocks. When both traders have log utilities and identical time preferences, Basak and Cuoco (1998) prove existence of a Radner equilibrium. We consider a model extension where both traders have identical power-utility functions but have different time-preference coefficients. Our main result gives parameter restrictions which ensure the existence of a Radner equilibrium. Our existence proof is based on showing that a non-linear, singular, and path-dependent first-order ODE has a global 𝒞1{\mathcal{C}}^{1} solution. As an application, we show that different time-preference parameters can produce long-run survival of both traders.

There exist several variations of Basak and Cuoco (1998). For example, Hugonnier (2012) considers more general participation constraints and proves existence of bubbles in equilibrium (i.e., the stock price differs from its discounted future dividends). Prieto (2013) extends Hugonnier (2012) further and proves the existence of an equilibrium when the unrestricted trader has a power-utility function. Both Hugonnier (2012) and Prieto (2013) assume that the restricted trader has a log-utility function. Because the restricted trader faces an incomplete financial market, her optimal investment and consumption problem is difficult to analyze, however, the log-utility assumption makes it explicitly solvable. Finally, we mention Weston (2023) who proves equilibrium existence for traders with heterogenous exponential utilities. Because exponential utilities have domain ℝ\mathbb{R}, Weston (2023) can allow consumption rates to become negative and this model relaxation makes the exponential optimization problems non-singular.

More recently, Guasoni, Larsen, and Leoni (2025) prove equilibrium existence when both traders have identical power utilities and identical time-preference coefficients. Their equilibrium existence proof hinges on proving global existence of a 𝒞1{\mathcal{C}}^{1} solution to a non-linear, singular, and path-dependent first-order ODE with quadratic growth terms. We extend their setting to allow for different time-preference coefficients (but keeping identical power utilities). Our relaxation produces a new cubic term in the resulting ODE and our main mathematical contribution is to prove that a unique global 𝒞1{\mathcal{C}}^{1} solution exists of the resulting ODE.

We conclude by applying our equilibrium to studying long-term survival of traders. In asset pricing theory, a model’s stability properties are often used to judge its quality.222For example, to resolve asset pricing puzzles, such as the interest rate puzzle from Weil (1989) and the equity premium puzzle from Mehra and Prescott (1985), many popular models exhibit stationarity properties because such properties are useful for model calibration. In continuous-time settings similar to ours, Kogan, Ross, Wang, and Westerfield (2006) show that traders with incorrect beliefs have zero long-run consumption-share limits and Yan (2008) shows that a trader’s long-run consumption share limit is determined by her survival index. More recent references on survival analysis include Bhamra and Uppal (2014), Borovička (2019), and Huang and Liu (2025). Unfortunately, the equilibrium models in both Basak and Cuoco (1998) and Guasoni, Larsen, and Leoni (2025) cannot produce survival of the restricted trader because the long-run limit of her consumption-share process is zero. In contrast, we show that our model with heterogenous time-preference parameters allows for both traders to survive in the long run. For comparison, we show that the log-power model in Prieto (2013) can also produce surviving traders.

## 2 Radner equilibrium

The following modeling setting is from Basak and Cuoco (1998). To study the traders’ survival properties, we use an infinite time horizon. However, this model variation of Basak and Cuoco (1998) is not new and is already discussed in Remark 3 in Hugonnier (2012). Our probability space is denoted by (Ω,𝔽,ℙ)(\Omega,\mathbb{F},\mathbb{P}) on which (Bt)t≥0(B\_{t})\_{t\geq 0} is a Brownian motion. The filtration is ℱt0:=σ​(Bs)s∈[0,t]\mathcal{F}\_{t}^{0}:=\sigma(B\_{s})\_{s\in[0,t]} and we assume 𝔽=∨t≥0ℱt0\mathbb{F}=\vee\_{t\geq 0}\mathcal{F}\_{t}^{0}. As usual, the augmented filtration is defined as ℱt:=ℱt0∨𝔽\mathcal{F}\_{t}:=\mathcal{F}\_{t}^{0}\vee\mathbb{F}’s ℙ\mathbb{P}-nullsets for t≥0t\geq 0.

### 2.1 Individual optimization

We consider a pure-exchange economy where the consumption good serves as the model’s numéraire. The single stock pays dividends at rate D=(Dt)t≥0D=(D\_{t})\_{t\geq 0} where

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Dt:=Dt​(μD​d​t+σD​d​Bt),D0>0.\displaystyle dD\_{t}:=D\_{t}\big(\mu\_{D}dt+\sigma\_{D}dB\_{t}\big),\quad D\_{0}>0. |  | (2.1) |

In ([2.1](https://arxiv.org/html/2512.14680v1#S2.E1 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")), the constants D0>0D\_{0}>0, μD∈ℝ\mu\_{D}\in\mathbb{R}, and σD>0\sigma\_{D}>0 are model input. The stock has price processes S=(St)t≥0S=(S\_{t})\_{t\geq 0} and money market account has price process S(0)=(S(0))t≥0S^{(0)}=(S^{(0)})\_{t\geq 0}. These two price processes are conjectured have Itô dynamics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St(0)\displaystyle dS^{(0)}\_{t} | =rt​St(0)​d​t,S0(0):=1,\displaystyle=r\_{t}S^{(0)}\_{t}dt,\quad S\_{0}^{(0)}:=1, |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St\displaystyle dS\_{t} | =(St​rt−Dt)​d​t+St​σS,t​(κt​d​t+d​Bt),S0∈(0,∞).\displaystyle=(S\_{t}r\_{t}-D\_{t})dt+S\_{t}\sigma\_{S,t}(\kappa\_{t}dt+dB\_{t}),\quad S\_{0}\in(0,\infty). |  | (2.3) |

In ([2.2](https://arxiv.org/html/2512.14680v1#S2.E2 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) and ([2.3](https://arxiv.org/html/2512.14680v1#S2.E3 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")), the quantities S0∈(0,∞)S\_{0}\in(0,\infty), r∈ℒloc1r\in{\mathcal{L}}^{1}\_{\text{loc}}, and (κ,σS)∈ℒloc2(\kappa,\sigma\_{S})\in{\mathcal{L}}^{2}\_{\text{loc}} are determined in equilibrium. For notational simplicity, we normalize the shares of stock to one and the shares of the money market to zero.

Trader 1 can trade both the stock and the money market and her wealth process has dynamics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​X1,t:=rt​X1,t​d​t+θ1,t​St​σS,t​(κt​d​t+d​Bt)−c1,t​d​t,X1,0:=θ1,0−(0)+S0∈ℝ.\displaystyle\begin{split}dX\_{1,t}&:=r\_{t}X\_{1,t}dt+\theta\_{1,t}S\_{t}\sigma\_{S,t}(\kappa\_{t}dt+dB\_{t})-c\_{1,t}dt,\\ X\_{1,0}&:=\theta^{(0)}\_{1,0-}+S\_{0}\in\mathbb{R}.\end{split} | |  | (2.4) |

In ([2.4](https://arxiv.org/html/2512.14680v1#S2.E4 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")), trader 1’s controls are the consumption rate c1c\_{1} and the number of shares held θ1\theta\_{1}. As in Basak and Cuoco (1998), trader 1’s endowed shares of the money market account θ1,0−(0)\theta^{(0)}\_{1,0-} is assumed to be negative, i.e., θ1,0−(0)∈(−∞,0)\theta^{(0)}\_{1,0-}\in(-\infty,0).

Trader 2 cannot trade the stock and so her wealth process has dynamics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​X2,t:=rt​X2,t​d​t−c2,t​d​t,X2,0:=θ2,0−(0)∈(0,∞).\displaystyle\begin{split}dX\_{2,t}&:=r\_{t}X\_{2,t}dt-c\_{2,t}dt,\\ X\_{2,0}&:=\theta^{(0)}\_{2,0-}\in(0,\infty).\end{split} | |  | (2.5) |

In ([2.5](https://arxiv.org/html/2512.14680v1#S2.E5 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")), trader 2’s control is the consumption-rate process c2c\_{2} and θ2,0−(0)=−θ1,0−(0)>0\theta^{(0)}\_{2,0-}=-\theta^{(0)}\_{1,0-}>0 denotes her number of endowed shares of the money market account.

Compared to Guasoni, Larsen, and Leoni (2025), our model allows for different time-preference coefficients β1\beta\_{1} and β2\beta\_{2}. However, the two traders have a common constant relative risk-aversion coefficient γ∈(0,1)\gamma\in(0,1). We assume that trader 1 has objective

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supθ1,c1∈𝒜111−γ​𝔼​[∫0∞e−β1​t​c1,t1−γ​𝑑t]\displaystyle\sup\_{\theta\_{1},c\_{1}\in{\mathcal{A}}\_{1}}\tfrac{1}{1-\gamma}\mathbb{E}\left[\int\_{0}^{\infty}e^{-\beta\_{1}t}c^{1-\gamma}\_{1,t}dt\right] |  | (2.6) |

whereas trader 2 has objective

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supc2∈𝒜211−γ​𝔼​[∫0∞e−β2​t​c2,t1−γ​𝑑t].\displaystyle\sup\_{c\_{2}\in{\mathcal{A}}\_{2}}\tfrac{1}{1-\gamma}\mathbb{E}\left[\int\_{0}^{\infty}e^{-\beta\_{2}t}c^{1-\gamma}\_{2,t}dt\right]. |  | (2.7) |

As we shall in Section [2.3](https://arxiv.org/html/2512.14680v1#S2.SS3 "2.3 Survival analysis ‣ 2 Radner equilibrium") below, this extension allows both traders to survive in the long run. In ([2.6](https://arxiv.org/html/2512.14680v1#S2.E6 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) and ([2.7](https://arxiv.org/html/2512.14680v1#S2.E7 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")), the admissible sets 𝒜1{\mathcal{A}}\_{1} and 𝒜2{\mathcal{A}}\_{2} in ([2.6](https://arxiv.org/html/2512.14680v1#S2.E6 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) are defined as:

###### Definition 2.1 (Admissibility).

Progressively measurable processes (θ1,c1)(\theta\_{1},c\_{1}) are admissible iff c1,t≥0c\_{1,t}\geq 0 for all t≥0t\geq 0 and the solution of ([2.4](https://arxiv.org/html/2512.14680v1#S2.E4 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) exists and satisfies X1,t≥0X\_{1,t}\geq 0 for all t≥0t\geq 0. In this case, we write (θ1,c1)∈𝒜1(\theta\_{1},c\_{1})\in{\mathcal{A}}\_{1}. Similarly, a progressively measurable process c2c\_{2} is admissible iff c2,t≥0c\_{2,t}\geq 0 for all t≥0t\geq 0 and the solution of ([2.5](https://arxiv.org/html/2512.14680v1#S2.E5 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) exists and satisfies X2,t≥0X\_{2,t}\geq 0 for all t≥0t\geq 0. In this case, we write c2∈𝒜2c\_{2}\in{\mathcal{A}}\_{2}.
♢\hfill\diamondsuit

### 2.2 Equilibrium

The following definition is standard and can be found in, e.g., Chapter 10 Duffie (2001).

###### Definition 2.2 (Radner equilibrium).

A constant S0∈(0,∞)S\_{0}\in(0,\infty), progressively measurable processes r∈ℒloc1r\in{\mathcal{L}}^{1}\_{\text{loc}} and (κ,σS)∈ℒloc2(\kappa,\sigma\_{S})\in{\mathcal{L}}^{2}\_{\text{loc}}, and controls (θ^1,c^1)∈𝒜1(\hat{\theta}\_{1},\hat{c}\_{1})\in{\mathcal{A}}\_{1} and c^2∈𝒜2\hat{c}\_{2}\in{\mathcal{A}}\_{2} constitute a Radner equilibrium iff:

* (i)

  The controls (θ^1,c^1)∈𝒜1(\hat{\theta}\_{1},\hat{c}\_{1})\in{\mathcal{A}}\_{1} maximize ([2.6](https://arxiv.org/html/2512.14680v1#S2.E6 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")).
* (ii)

  The control c^2∈𝒜2\hat{c}\_{2}\in{\mathcal{A}}\_{2} maximizes ([2.7](https://arxiv.org/html/2512.14680v1#S2.E7 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")).
* (iii)

  The stock and consumption markets clear in the sense

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | θ^1,t=1and c^1,t+c^2,t=Dt,for all ​t≥0.\displaystyle\hat{\theta}\_{1,t}=1\quad\text{and }\quad\hat{c}\_{1,t}+\hat{c}\_{2,t}=D\_{t},\quad\text{for all }t\geq 0. |  | (2.8) |

♢\hfill\diamondsuit

Walras’ law ensures that clearing in both the stock and consumption markets implies that money market clears too. This additional clearing property stems from the self-financing wealth dynamics ([2.4](https://arxiv.org/html/2512.14680v1#S2.E4 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) and ([2.5](https://arxiv.org/html/2512.14680v1#S2.E5 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")).

The next lemma gives the existence of a solution to a governing ODE, which we subsequently use to produce a Radner equilibrium. The lemma is proven in the next section.

###### Lemma 2.3.

Let γ∈(0,1)\gamma\in(0,1), σD2>0\sigma^{2}\_{D}>0, A∈(1+δ−2​δγ,∞)A\in(1+\delta-\frac{2\delta}{\gamma},\infty), and δ∈(−γ,0)\delta\in(-\gamma,0).

1. 1.

   There exists ξ0∈(0,∞)\xi\_{0}\in(0,\infty) such that ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium"))-([2.10](https://arxiv.org/html/2512.14680v1#S2.E10 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) has a unique solution h∈𝒞1​([0,1])h\in{\mathcal{C}}^{1}([0,1]) with γ≤hξ0​(y)≤1\gamma\leq h\_{\xi\_{0}}(y)\leq 1 for all y∈[0,1]y\in[0,1] and h′​(1)=(1−γ)​(γ2+γ−δ)γ​(A−δ−1)+2​δ>0h^{\prime}(1)=\frac{(1-\gamma)(\gamma^{2}+\gamma-\delta)}{\gamma(A-\delta-1)+2\delta}>0 of the ODE

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h′​(y)=a0​(y)+a1​(y)1−y​h​(y)+a2​(h,y)1−y​h​(y)2+δ​y1−y​h​(y)2​(1−h​(y)γ),\displaystyle h^{\prime}(y)=a\_{0}(y)+\frac{a\_{1}(y)}{1-y}h(y)+\frac{a\_{2}(h,y)}{1-y}h(y)^{2}+\frac{\delta y}{1-y}h(y)^{2}\Big(1-\frac{h(y)}{\gamma}\Big), |  | (2.9) |

   for y∈(0,1)y\in(0,1), boundary values

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h​(0)=γ,h​(1)=1,\displaystyle h(0)=\gamma,\quad h(1)=1, |  | (2.10) |

   and functions

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | a0​(y):=γ​(1+γ)y,y∈(0,1],a1​(y):=(2​γ+1)​y−(1+γ)y,y∈(0,1],a2​(h,y):=ξ0σD2​exp⁡{∫0yh​(q)−11−q​𝑑q}−A,y∈[0,1).\displaystyle\begin{split}a\_{0}(y)&:=\frac{\gamma(1+\gamma)}{y},\quad y\in(0,1],\\ a\_{1}(y)&:=\frac{(2\gamma+1)y-(1+\gamma)}{y},\quad y\in(0,1],\\ a\_{2}(h,y)&:=\frac{\xi\_{0}}{\sigma\_{D}^{2}}\exp\Big\{\int\_{0}^{y}\frac{h(q)-1}{1-q}dq\Big\}-A,\;\;y\in[0,1).\end{split} | |  | (2.11) |
2. 2.

   For the drift function μY\mu\_{Y} and and volatility function σY\sigma\_{Y} defined as

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | μY​(y):=σD2​(1−y)​y​h​(y)​(2​γ2+δ​y​h​(y))−γ​(γ+1)​(2​y−1)2​γ​y​h​(y)2,σY​(y):=σD​1−yh​(y),\displaystyle\begin{split}\mu\_{Y}(y)&:=\sigma\_{D}^{2}(1-y)\frac{yh(y)\big(2\gamma^{2}+\delta yh(y)\big)-\gamma(\gamma+1)(2y-1)}{2\gamma yh(y)^{2}},\\ \sigma\_{Y}(y)&:=\sigma\_{D}\frac{1-y}{h(y)},\end{split} | |  | (2.12) |

   for y∈(0,1)y\in(0,1), there exists a unique strong solution of the SDE

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | d​Yt=μY​(Yt)​d​t+σY​(Yt)​d​Bt,Y0∈(0,1).\displaystyle dY\_{t}=\mu\_{Y}(Y\_{t})dt+\sigma\_{Y}(Y\_{t})dB\_{t},\quad Y\_{0}\in(0,1). |  | (2.13) |

The next theorem is our main contribution and it uses the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(y):=2ξ0​exp⁡{−∫0yh​(q)1−q​𝑑q}​(1−γ)−γ,y∈[0,1),\displaystyle g(y):=\frac{2}{\xi\_{0}}\exp\Big\{-\int\_{0}^{y}\frac{h(q)}{1-q}dq\Big\}(1-\gamma)^{-\gamma},\quad y\in[0,1), |  | (2.14) |

where hh solves the ODE in ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")). Based on hh’s properties, the function gg satisfies

|  |  |  |
| --- | --- | --- |
|  | g′​(0)=g​(1)=0,g′​(y)<0,y∈[0,1].g^{\prime}(0)=g(1)=0,\quad g^{\prime}(y)<0,\quad y\in[0,1]. |  |

The proof of the next result is given at the end of the next section.

###### Theorem 2.4.

Let γ∈(0,1)\gamma\in(0,1), σD2>0\sigma^{2}\_{D}>0, and assume the constants

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ:=2​(β2−β1)σD2\displaystyle\delta:=\frac{2(\beta\_{2}-\beta\_{1})}{\sigma\_{D}^{2}} |  | (2.15) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | A:=2​β2+σD2−(1−γ)​(2​μD−γ​σD2)σD2\displaystyle A:=\frac{2\beta\_{2}+\sigma\_{D}^{2}-(1-\gamma)(2\mu\_{D}-\gamma\sigma\_{D}^{2})}{\sigma\_{D}^{2}} |  | (2.16) |

satisfy A∈(1+δ−2​δγ,∞)A\in(1+\delta-\frac{2\delta}{\gamma},\infty) and δ∈(−γ,0)\delta\in(-\gamma,0). For θ2,0−(0)∈(0,g​(0)D0)\theta^{(0)}\_{2,0-}\in\big(0,\frac{g(0)}{D\_{0}}\big), let Y0∈(0,1)Y\_{0}\in(0,1) solve g​(Y0)​D0​(1−Y0)γ=θ2,0−(0)g(Y\_{0})D\_{0}(1-Y\_{0})^{\gamma}=\theta^{(0)}\_{2,0-}. Then, there exists a Radner equilibrium in which
the equilibrium interest rate process is rt=r​(Yt)∈ℒloc1r\_{t}=r(Y\_{t})\in{\mathcal{L}}\_{\text{loc}}^{1} and the equilibrium market price of risk process is κt=κ​(Yt)∈ℒloc2\kappa\_{t}=\kappa(Y\_{t})\in{\mathcal{L}}\_{\text{loc}}^{2} for the deterministic functions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | r​(y):=β2+y​(β1−β2)+γ​μD−12​γ​(γ+1)​σD2−γ​(γ+1)​σD2​(1−y)2​y​h​(y)2,κ​(y):=γ​σD​(1−yy​h​(y)+1),\displaystyle\begin{split}r(y)&:=\beta\_{2}+y(\beta\_{1}-\beta\_{2})+\gamma\mu\_{D}-\frac{1}{2}\gamma(\gamma+1)\sigma\_{D}^{2}-\frac{\gamma(\gamma+1)\sigma\_{D}^{2}(1-y)}{2yh(y)^{2}},\\ \kappa(y)&:=\gamma\sigma\_{D}\left(\frac{1-y}{yh(y)}+1\right),\end{split} | |  | (2.17) |

for y∈(0,1)y\in(0,1) and the equilibrium consumption-rate processes for ([2.6](https://arxiv.org/html/2512.14680v1#S2.E6 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) and ([2.7](https://arxiv.org/html/2512.14680v1#S2.E7 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) are

|  |  |  |  |
| --- | --- | --- | --- |
|  | c^1,t:=Dt​Yt,c^2,t:=Dt​(1−Yt),t≥0,\displaystyle\hat{c}\_{1,t}:=D\_{t}Y\_{t},\quad\hat{c}\_{2,t}:=D\_{t}(1-Y\_{t}),\quad t\geq 0, |  | (2.18) |

where the state-process YY is as in ([2.13](https://arxiv.org/html/2512.14680v1#S2.E13 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")).

Based on ([2.18](https://arxiv.org/html/2512.14680v1#S2.E18 "In Theorem 2.4. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")), we say that YY is the equilibrium consumption-share process of trader 1.

### 2.3 Survival analysis

As in Kogan, Ross, Wang, and Westerfield (2006) and Yan (2008), we use the consumption share process ([2.13](https://arxiv.org/html/2512.14680v1#S2.E13 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) to determine if a trader survives in the long run.

###### Definition 2.5.

Trader 1, respectively Trader 2, becomes extinct iff

|  |  |  |
| --- | --- | --- |
|  | limt→∞Yt=0,respectively ​limt→∞(1−Yt)=0,almost surely.\lim\_{t\to\infty}Y\_{t}=0,\quad\text{respectively }\lim\_{t\to\infty}(1-Y\_{t})=0,\quad\text{almost surely}. |  |

Otherwise, Trader 1, respectively Trader 2, is said to survive.
♢\hfill\diamondsuit

Based on this definition, even if one of the consumption shares converges to zero in the sense limt→∞Yt∈{0,1}\lim\_{t\to\infty}Y\_{t}\in\{0,1\}, the corresponding equilibrium consumption-rate process c^1\hat{c}\_{1} or c^2\hat{c}\_{2} in ([2.18](https://arxiv.org/html/2512.14680v1#S2.E18 "In Theorem 2.4. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) may or may not converge to zero. This is because the geometric Brownian motion in ([2.1](https://arxiv.org/html/2512.14680v1#S2.E1 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) satisfies limt→∞Dt=∞\lim\_{t\to\infty}D\_{t}=\infty whenever μD>12​σD2\mu\_{D}>\frac{1}{2}\sigma\_{D}^{2}.

For β1=β2\beta\_{1}=\beta\_{2}, Lemmas 3.2 and 3.3 in Guasoni, Larsen, and Leoni (2025) ensure that the scale function ss defined in ([2.24](https://arxiv.org/html/2512.14680v1#S2.E24 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) below satisfies s​(0)=−∞s(0)=-\infty and s​(1)<∞s(1)<\infty and ensure that both boundaries y=0y=0 and y=1y=1 are not attainable. Therefore, for β1=β2\beta\_{1}=\beta\_{2}, Proposition 5.5.22(c) in Karatzas and Shreve (1988) gives limt→∞Yt=1\lim\_{t\to\infty}Y\_{t}=1 almost surely.
This property also holds in Basak and Cuoco (1998) where γ=1\gamma=1 and h​(y)=1h(y)=1 for all y∈[0,1]y\in[0,1]. Consequently, in these two models, the restricted trader becomes extinct. In contrast, the next result shows that
when β2<β1\beta\_{2}<\beta\_{1}, both traders can survive.

###### Lemma 2.6.

Assume the setting of Theorem [2.4](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium"). When δ∈(−γ,−γ2)\delta\in(-\gamma,-\gamma^{2}), both traders survive.

###### Proof.

Let hh be as in Lemma [2.3](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium"). For a constant a∈(0,1)a\in(0,1), we define the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(y):=exp⁡{−2​∫ayμY​(x)σY​(x)2​𝑑x},y∈(0,1),\displaystyle\rho(y):=\exp\Big\{-2\int\_{a}^{y}\frac{\mu\_{Y}(x)}{\sigma\_{Y}(x)^{2}}dx\Big\},\quad y\in(0,1), |  | (2.19) |

where the drift μY\mu\_{Y} and volatility σY\sigma\_{Y} are defined in ([2.12](https://arxiv.org/html/2512.14680v1#S2.E12 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")). Because h∈𝒞1​([0,1])h\in{\mathcal{C}}^{1}([0,1]), we can expand the ratio μY​(y)σY2​(y)\frac{\mu\_{Y}(y)}{\sigma\_{Y}^{2}(y)} at y=0y=0 and at y=1y=1 to see

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y​μY​(y)σY​(y)2\displaystyle y\frac{\mu\_{Y}(y)}{\sigma\_{Y}(y)^{2}} | =1+γ2+O​(y),y↓0,\displaystyle=\frac{1+\gamma}{2}+O(y),\quad y\downarrow 0, |  | (2.20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1−y)​μY​(y)σY​(y)2\displaystyle(1-y)\frac{\mu\_{Y}(y)}{\sigma\_{Y}(y)^{2}} | =(γ−1)​γ+δ2​γ+O​(1−y),y↑1.\displaystyle=\frac{(\gamma-1)\gamma+\delta}{2\gamma}+O(1-y),\quad y\uparrow 1. |  | (2.21) |

Consequently, the expansions of ρ\rho in ([2.19](https://arxiv.org/html/2512.14680v1#S2.E19 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ρ​(y)=e∫yaO​(x)x​𝑑x​e∫ya1+γx​𝑑x=e∫yaO​(x)x​𝑑x​(ay)1+γ,y∈(0,a],\displaystyle\begin{split}\rho(y)&=e^{\int\_{y}^{a}\frac{O(x)}{x}dx}e^{\int\_{y}^{a}\frac{1+\gamma}{x}dx}\\ &=e^{\int\_{y}^{a}\frac{O(x)}{x}dx}\Big(\frac{a}{y}\Big)^{1+\gamma},\quad y\in(0,a],\end{split} | |  | (2.22) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ρ​(y)=e∫ayO​(1−x)1−x​𝑑x​e∫ay1−γ−δγ1−x​𝑑x=e∫ayO​(1−x)1−x​𝑑x​(1−a1−y)1−γ−δγ,y∈[a,1).\displaystyle\begin{split}\rho(y)&=e^{\int\_{a}^{y}\frac{O(1-x)}{1-x}dx}e^{\int\_{a}^{y}\frac{1-\gamma-\frac{\delta}{\gamma}}{1-x}dx}\\ &=e^{\int\_{a}^{y}\frac{O(1-x)}{1-x}dx}\Big(\frac{1-a}{1-y}\Big)^{1-\gamma-\frac{\delta}{\gamma}},\quad y\in[a,1).\end{split} | |  | (2.23) |

The scale function is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(y):=∫ayρ​(x)​𝑑x,y∈(0,1).\displaystyle s(y):=\int\_{a}^{y}\rho(x)dx,\quad y\in(0,1). |  | (2.24) |

From ([2.22](https://arxiv.org/html/2512.14680v1#S2.E22 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")), we see that s​(0):=limy↓0s​(y)=−∞s(0):=\lim\_{y\downarrow 0}s(y)=-\infty. For δ∈(−γ,−γ2]\delta\in(-\gamma,-\gamma^{2}], we see from ([2.23](https://arxiv.org/html/2512.14680v1#S2.E23 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) that s​(1):=limy↑1s​(y)=∞s(1):=\lim\_{y\uparrow 1}s(y)=\infty. Proposition 5.5.22(a) in Karatzas and Shreve (1988) gives that YY is recurrent.

To see that the natural-scale process s​(Yt)s(Y\_{t}) is positive recurrent, we use the speed measure with density function

|  |  |  |
| --- | --- | --- |
|  | m​(d​z)d​z:=1ρ​(s−1​(z))​σY​(s−1​(z))2,z∈ℝ.\frac{m(dz)}{dz}:=\frac{1}{\rho\big(s^{-1}(z)\big)\sigma\_{Y}\big(s^{-1}(z)\big)^{2}},\quad z\in\mathbb{R}. |  |

To see that this density function is integrable, we first substitute x:=s−1​(z)x:=s^{-1}(z) so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝm​(d​z)=∫011ρ​(x)​σY​(x)2​𝑑x.\displaystyle\int\_{\mathbb{R}}m(dz)=\int\_{0}^{1}\frac{1}{\rho(x)\sigma\_{Y}(x)^{2}}dx. |  | (2.25) |

We start with integrability at x=0x=0 for ([2.25](https://arxiv.org/html/2512.14680v1#S2.E25 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")). Because h​(0)=γh(0)=\gamma, we have from ([2.12](https://arxiv.org/html/2512.14680v1#S2.E12 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) that σY​(0)=σDγ\sigma\_{Y}(0)=\frac{\sigma\_{D}}{\gamma}, hence, it suffices to show that 1ρ​(x)\frac{1}{\rho(x)} is integrable at x=0x=0. This follows from ([2.22](https://arxiv.org/html/2512.14680v1#S2.E22 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")). Next, we show integrability at x=1x=1 for ([2.25](https://arxiv.org/html/2512.14680v1#S2.E25 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")). From ([2.12](https://arxiv.org/html/2512.14680v1#S2.E12 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")), ([2.23](https://arxiv.org/html/2512.14680v1#S2.E23 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")), and h​(1)=1h(1)=1, there exists an irrelevant constant c>0c>0 such that

|  |  |  |
| --- | --- | --- |
|  | 1ρ​(x)​σY​(x)2≤c(1−x)γ+δγ−1​(1−x)2=c(1−x)γ+δγ+1.\displaystyle\frac{1}{\rho(x)\sigma\_{Y}(x)^{2}}\leq\frac{c}{(1-x)^{\gamma+\frac{\delta}{\gamma}-1}(1-x)^{2}}=\frac{c}{(1-x)^{\gamma+\frac{\delta}{\gamma}+1}}. |  |

Because δ<−γ2\delta<-\gamma^{2}, the right-hand-side is integrable at x=1x=1. Lemma 33.19 in Kallenberg (2021) ensures that s​(Yt)s(Y\_{t}) is positive recurrent, hence, limt→∞|s​(Yt)|=∞\lim\_{t\to\infty}|s(Y\_{t})|=\infty in probability is impossible. Consequently, both limt→∞Yt=0\lim\_{t\to\infty}Y\_{t}=0 in probability and limt→∞Yt=1\lim\_{t\to\infty}Y\_{t}=1 in probability are impossible.

♢\hfill\diamondsuit

We conclude this section by showing that the model in Prieto (2013) can also produce surviving traders. In Prieto (2013), the restricted trader has a log-utility function, the unrestricted trader has a power-utility function, and both traders have the same time-preference parameter. As discussed in the introduction, when the restricted trader has a log-utility function, the optimization problem ([2.7](https://arxiv.org/html/2512.14680v1#S2.E7 "In 2.1 Individual optimization ‣ 2 Radner equilibrium")) becomes explicitly solvable with h​(y)=1h(y)=1 for y∈[0,1]y\in[0,1].

We adjust the proof of Lemma [2.6](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem6 "Lemma 2.6. ‣ 2.3 Survival analysis ‣ 2 Radner equilibrium") based on

|  |  |  |  |
| --- | --- | --- | --- |
|  | Prieto (2013)​{y​μY​(y)σY​(y)2=1+γ2+O​(y),y↓0,(1−y)​μY​(y)σY​(y)2=(1−γ)​(2​μD−(2+γ)​σD2)2​σD2+O​(1−y),y↑1.\displaystyle\text{ Prieto (2013)}\;\;\begin{cases}y\frac{\mu\_{Y}(y)}{\sigma\_{Y}(y)^{2}}=\frac{1+\gamma}{2}+O(y),\quad y\downarrow 0,\\ (1-y)\frac{\mu\_{Y}(y)}{\sigma\_{Y}(y)^{2}}=\frac{(1-\gamma)\big(2\mu\_{D}-(2+\gamma)\sigma\_{D}^{2}\big)}{2\sigma\_{D}^{2}}+O(1-y),\quad y\uparrow 1.\end{cases} |  | (2.26) |

We see that the left-end point y=0y=0 in ([2.26](https://arxiv.org/html/2512.14680v1#S2.E26 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) is similar to ([2.22](https://arxiv.org/html/2512.14680v1#S2.E22 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")). The analysis for the right-end point y=1y=1 in ([2.26](https://arxiv.org/html/2512.14680v1#S2.E26 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) is slightly different from ([2.23](https://arxiv.org/html/2512.14680v1#S2.E23 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")). Based on ([2.26](https://arxiv.org/html/2512.14680v1#S2.E26 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(y)\displaystyle\rho(y) | =e∫ayO​(1−x)1−x​𝑑x​e∫ay(1−γ)​(2+γ−2​μD/σD2)1−x​𝑑x\displaystyle=e^{\int\_{a}^{y}\frac{O(1-x)}{1-x}dx}e^{\int\_{a}^{y}\frac{(1-\gamma)\left(2+\gamma-2\mu\_{D}/\sigma\_{D}^{2}\right)}{1-x}dx} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e∫ayO​(1−x)1−x​𝑑x​(1−a1−y)(1−γ)​(2+γ−2​μD/σD2),y∈[a,1).\displaystyle=e^{\int\_{a}^{y}\frac{O(1-x)}{1-x}dx}\Big(\frac{1-a}{1-y}\Big)^{(1-\gamma)\left(2+\gamma-2\mu\_{D}/\sigma\_{D}^{2}\right)},\quad y\in[a,1). |  |

When the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | η:=(1−γ)​(2+γ−2​μD/σD2)≥1\displaystyle\eta:=(1-\gamma)\left(2+\gamma-2\mu\_{D}/\sigma\_{D}^{2}\right)\geq 1 |  | (2.27) |

holds, the scale function ρ​(y)\rho(y) in ([2.24](https://arxiv.org/html/2512.14680v1#S2.E24 "In 2.3 Survival analysis ‣ 2 Radner equilibrium")) is not integrable at y=1y=1. Therefore, for η≥1\eta\geq 1, the process YY is recurrent. To see that YY is positive recurrent when η>1\eta>1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1ρ​(x)​σ​(x)2\displaystyle\frac{1}{\rho(x)\sigma(x)^{2}} | ≤c(1−y)−η​(1−y)2=c(1−y)2−η,\displaystyle\leq\frac{c}{(1-y)^{-\eta}(1-y)^{2}}=\frac{c}{(1-y)^{2-\eta}}, |  |

where c>0c>0 is an irrelevant constant. The right-hand side is integrable for η>1\eta>1, and so both traders survive in the long run.

## 3 Proofs

This section adjusts the proofs in Guasoni, Larsen, and Leoni (2025) to accommodate different time-preference coefficients β1\beta\_{1} and β2\beta\_{2}. Mathematically speaking, when β1≠β2\beta\_{1}\neq\beta\_{2}, the governing ODE ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) has a new cubic term proportional to β2−β1\beta\_{2}-\beta\_{1}.

### 3.1 Auxiliary ODE analysis

In this subsection, we consider the ODE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {f′​(y)=a0​(y)+a1​(y)1−y​f​(y)+a31−y​f​(y)2+δ​y1−y​f​(y)2​(1−f​(y)γ),y∈(0,1),f​(t0)=f0,\displaystyle\begin{cases}f^{\prime}(y)=a\_{0}(y)+\frac{a\_{1}(y)}{1-y}f(y)+\frac{a\_{3}}{1-y}f(y)^{2}+\frac{\delta y}{1-y}f(y)^{2}\Big(1-\frac{f(y)}{\gamma}\Big),\quad y\in(0,1),\\ f(t\_{0})=f\_{0},\end{cases} |  | (3.1) |

for constants t0,f0,a3,δ,γ∈ℝt\_{0},f\_{0},a\_{3},\delta,\gamma\in\mathbb{R} and functions a0a\_{0} and a1a\_{1} from ([2.11](https://arxiv.org/html/2512.14680v1#S2.E11 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")).

###### Theorem 3.1.

Let γ∈(0,1)\gamma\in(0,1), δ∈(−γ,0)\delta\in(-\gamma,0), and a3∈[−1,δ​1−γγ−γ)a\_{3}\in[-1,\delta\frac{1-\gamma}{\gamma}-\gamma).

1. 1.

   For t0:=0t\_{0}:=0 and f0:=γf\_{0}:=\gamma, there exists f∈𝒞​([0,1])∩𝒞1​([0,1))f\in{\mathcal{C}}([0,1])\cap{\mathcal{C}}^{1}([0,1)) such that ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) holds with γ≤f​(y)<1\gamma\leq f(y)<1 for all y∈[0,1]y\in[0,1] and

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | f​(1)=γ2​δ​(a3+δ+(a3+δ)2+4​δ)<1.\displaystyle f(1)=\frac{\gamma}{2\delta}\Big(a\_{3}+\delta+\sqrt{(a\_{3}+\delta)^{2}+4\delta}\Big)<1. |  | (3.2) |
2. 2.

   For y0∈(0,1)y\_{0}\in(0,1) and f0∈(0,γ2​δ​(a3+δ+(a3+δ)2+4​δ)]f\_{0}\in\big(0,\frac{\gamma}{2\delta}\big(a\_{3}+\delta+\sqrt{(a\_{3}+\delta)^{2}+4\delta}\big)\big], there exists f∈𝒞​([y0,1])∩𝒞1​([y0,1))f\in{\mathcal{C}}([y\_{0},1])\cap{\mathcal{C}}^{1}([y\_{0},1)) such that ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) and ([3.2](https://arxiv.org/html/2512.14680v1#S3.E2 "In item 1 ‣ Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) hold and f​(y)<1f(y)<1 for all y∈[y0,1]y\in[y\_{0},1].

###### Proof.

The second part is easier prove because there is no singularity at y0∈(0,1)y\_{0}\in(0,1), and so for brevity we only prove the first part.

Step 1/3: This step ensures that all coefficient restrictions are internally consistent.
(i) To see that the interval [−1,δ​1−γγ−γ][-1,\delta\frac{1-\gamma}{\gamma}-\gamma] is a non-trivial subinterval of [−1,0)[-1,0), we use γ∈(0,1)\gamma\in(0,1) and δ∈(−γ,0)\delta\in(-\gamma,0) to see

|  |  |  |
| --- | --- | --- |
|  | −1<δ​1−γγ−γ<0.-1<\delta\frac{1-\gamma}{\gamma}-\gamma<0. |  |

(ii) To see that the term inside the square-root in ([3.2](https://arxiv.org/html/2512.14680v1#S3.E2 "In item 1 ‣ Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) is positive, we use δ<0\delta<0 to see that the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | [−1,0)∋a3→(a3+δ)2\displaystyle[-1,0)\ni a\_{3}\to(a\_{3}+\delta)^{2} |  | (3.3) |

is decreasing. This gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a3+δ)2+4​δ≥(δ​1−γγ−γ+δ)2+4​δ=(γ2+δ)2γ2>0.\displaystyle(a\_{3}+\delta)^{2}+4\delta\geq\Big(\delta\frac{1-\gamma}{\gamma}-\gamma+\delta\Big)^{2}+4\delta=\frac{\left(\gamma^{2}+\delta\right)^{2}}{\gamma^{2}}>0. |  | (3.4) |

(iii) To see that the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | [−1,δ​1−γγ−γ]∋a3→a3+δ+(a3+δ)2+4​δ\displaystyle[-1,\delta\frac{1-\gamma}{\gamma}-\gamma]\ni a\_{3}\to a\_{3}+\delta+\sqrt{(a\_{3}+\delta)^{2}+4\delta} |  | (3.5) |

is decreasing, we compute the derivative

|  |  |  |
| --- | --- | --- |
|  | ∂∂a3​(a3+δ+(a3+δ)2+4​δ)=1+a3+δ(a3+δ)2+4​δ.\frac{\partial}{\partial a\_{3}}\Big(a\_{3}+\delta+\sqrt{(a\_{3}+\delta)^{2}+4\delta}\Big)=1+\frac{a\_{3}+\delta}{\sqrt{(a\_{3}+\delta)^{2}+4\delta}}. |  |

Therefore, the function ([3.5](https://arxiv.org/html/2512.14680v1#S3.E5 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) is decreasing if and only if it is negative. In other words, we need

|  |  |  |  |
| --- | --- | --- | --- |
|  | −(a3+δ)≥(a3+δ)2+4​δ.\displaystyle-(a\_{3}+\delta)\geq\sqrt{(a\_{3}+\delta)^{2}+4\delta}. |  | (3.6) |

Because both sides of ([3.6](https://arxiv.org/html/2512.14680v1#S3.E6 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) are positive, we can square and use δ<0\delta<0 to see that ([3.6](https://arxiv.org/html/2512.14680v1#S3.E6 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) holds.

(iv) To see the upper bound in ([3.2](https://arxiv.org/html/2512.14680v1#S3.E2 "In item 1 ‣ Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs")), we evaluate the function in
([3.5](https://arxiv.org/html/2512.14680v1#S3.E5 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) at a3:=δ​1−γγ−γa\_{3}:=\delta\frac{1-\gamma}{\gamma}-\gamma to see

|  |  |  |
| --- | --- | --- |
|  | γ2​δ​(a3+δ+(a3+δ)2+4​δ)<|γ2+δ|−γ2+δ2​δ,a3∈(−∞,δ​1−γγ−γ).\frac{\gamma}{2\delta}\Big(a\_{3}+\delta+\sqrt{(a\_{3}+\delta)^{2}+4\delta}\Big)<\frac{|\gamma^{2}+\delta|-\gamma^{2}+\delta}{2\delta},\quad a\_{3}\in(-\infty,\delta\frac{1-\gamma}{\gamma}-\gamma). |  |

By splitting into two cases γ2+δ≥0\gamma^{2}+\delta\geq 0 and γ2+δ<0\gamma^{2}+\delta<0, we get

|  |  |  |
| --- | --- | --- |
|  | |γ2+δ|−γ2+δ2​δ={−γ2δ,δ∈(−γ,−γ2]1,δ∈(−γ2,0)≤1.\frac{|\gamma^{2}+\delta|-\gamma^{2}+\delta}{2\delta}=\begin{cases}-\frac{\gamma^{2}}{\delta},\quad\delta\in(-\gamma,-\gamma^{2}]\\ 1,\quad\delta\in(-\gamma^{2},0)\end{cases}\leq 1. |  |

Step 2/3: Relative to Theorem 2.4 in Guasoni, Larsen, and Leoni (2025), when δ≠0\delta\neq 0, the term

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​y1−y​f​(y)2​(1−f​(y)γ),y∈[0,1),\displaystyle\frac{\delta y}{1-y}f(y)^{2}\Big(1-\frac{f(y)}{\gamma}\Big),\quad y\in[0,1), |  | (3.7) |

in ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) is new. However, the local existence and comparison results in Theorems 2.2 and 2.3 in Guasoni, Larsen, and Leon (2025) continue to hold for the ODE in ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")). This is because the singularity in ([3.7](https://arxiv.org/html/2512.14680v1#S3.E7 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) is at y=1y=1, whereas Theorems 2.2 and 2.3 in Guasoni, Larsen, and Leoni (2025) are local around the initial point y=0y=0.

Step 3/3: For a3:=−1a\_{3}:=-1, we see that the constant f​(y):=γf(y):=\gamma solves ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")). Therefore, for a3≥−1a\_{3}\geq-1, the comparison principle ensures that all local solutions of ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) are lower bounded by γ\gamma.

Step 3/3: This step proves that a global solution of ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) exists. To this end, we let f​(y)>0f(y)>0 be a local solution for y∈[0,y∗)y\in[0,y^{\*}) where y∗∈(0,1]y^{\*}\in(0,1] gives ff’s maximal interval of existence.

First, to see that f​(y)<1f(y)<1 for y∈[0,y∗)y\in[0,y^{\*}), we argue by contradiction and assume there exists y1∈[0,y∗)y\_{1}\in[0,y^{\*}) such that f​(y1)≥1f(y\_{1})\geq 1. Then, because f​(0)=γ<1f(0)=\gamma<1, there exists y0∈(0,y∗)y\_{0}\in(0,y^{\*}) with f​(y0)=1f(y\_{0})=1 and f′​(y0)≥0f^{\prime}(y\_{0})\geq 0. The ODE in ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) gives the contradiction

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0≤a0​(y0)+a1​(y0)1−y0+a31−y0+δ​y01−y0​(1−1γ)≤a0​(y0)+a1​(y0)1−y0+δ​1−γγ−γ1−y0+δ​y01−y0​(1−1γ)=(γ−1)​(γ2+γ−δ​y0)γ​y0<0.\displaystyle\begin{split}0&\leq a\_{0}(y\_{0})+\frac{a\_{1}(y\_{0})}{1-y\_{0}}+\frac{a\_{3}}{1-y\_{0}}+\frac{\delta y\_{0}}{1-y\_{0}}\Big(1-\frac{1}{\gamma}\Big)\\ &\leq a\_{0}(y\_{0})+\frac{a\_{1}(y\_{0})}{1-y\_{0}}+\frac{\delta\frac{1-\gamma}{\gamma}-\gamma}{1-y\_{0}}+\frac{\delta y\_{0}}{1-y\_{0}}\Big(1-\frac{1}{\gamma}\Big)\\ &=\frac{(\gamma-1)\left(\gamma^{2}+\gamma-\delta y\_{0}\right)}{\gamma y\_{0}}\\ &<0.\end{split} | |  | (3.8) |

Second, to see that limy↑y∗f​(y)\lim\_{y\uparrow y^{\*}}f(y) exists, it suffices to rule out finite oscillations because of the previous boundedness property. For y∗∈(0,1)y^{\*}\in(0,1), there is no singularity in ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) and a standard Lipschitz argument rules out oscillations. To rule out finite oscillations for y∗=1y^{\*}=1, we let (yn)n∈ℕ⊂(0,1)(y\_{n})\_{n\in\mathbb{N}}\subset(0,1) converge to y∗=1y^{\*}=1 such that f′​(yn)=0f^{\prime}(y\_{n})=0. Because ff is bounded, by using a subsequence if necessary, we can assume

|  |  |  |
| --- | --- | --- |
|  | l:=limn→∞f​(yn)l:=\lim\_{n\to\infty}f(y\_{n}) |  |

exists in [γ,1][\gamma,1]. The proof is concluded by showing that there is only one possible value for ll. Multiplying 1−y1-y on both sides in ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) and replacing yy with yny\_{n} give the limit

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=γ​l+a3​l2+δ​l2​(1−lγ),\displaystyle\begin{split}0&=\gamma l+a\_{3}l^{2}+\delta l^{2}\Big(1-\frac{l}{\gamma}\Big),\\ \end{split} | |  | (3.9) |

The cubic polynomial in ([3.9](https://arxiv.org/html/2512.14680v1#S3.E9 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) has the 3 roots l∈{0,γ2​δ​(a3+δ±(a3+δ)2+4​δ)}l\in\Big\{0,\frac{\gamma}{2\delta}\Big(a\_{3}+\delta\pm\sqrt{(a\_{3}+\delta)^{2}+4\delta}\Big)\Big\}. Because γ≤f≤1\gamma\leq f\leq 1, we have l∈[γ,1]l\in[\gamma,1] and so it suffices to prove

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ2​δ​(a3+δ−(a3+δ)2+4​δ)>1\displaystyle\frac{\gamma}{2\delta}\Big(a\_{3}+\delta-\sqrt{(a\_{3}+\delta)^{2}+4\delta}\Big)>1 |  | (3.10) |

From ([3.4](https://arxiv.org/html/2512.14680v1#S3.E4 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −(a3+δ)2+4​δ≤−|γ2+δ|γ.\displaystyle-\sqrt{(a\_{3}+\delta)^{2}+4\delta}\leq-\frac{|\gamma^{2}+\delta|}{\gamma}. |  | (3.11) |

By splitting into two cases γ2+δ≥0\gamma^{2}+\delta\geq 0 and γ2+δ<0\gamma^{2}+\delta<0, we get

|  |  |  |
| --- | --- | --- |
|  | a3+δ−|γ2+δ|γ<δγ−γ−|γ2+δ|γ={2​δγ,δ∈(−γ,−γ2]−2​γ,δ∈(−γ2,0)≤2​δγ,a\_{3}+\delta-\frac{|\gamma^{2}+\delta|}{\gamma}<\frac{\delta}{\gamma}-\gamma-\frac{|\gamma^{2}+\delta|}{\gamma}=\begin{cases}\frac{2\delta}{\gamma},\quad\delta\in(-\gamma,-\gamma^{2}]\\ -2\gamma,\quad\delta\in(-\gamma^{2},0)\end{cases}\leq\frac{2\delta}{\gamma}, |  |

which shows ([3.10](https://arxiv.org/html/2512.14680v1#S3.E10 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")).

♢\hfill\diamondsuit

### 3.2 Governing ODE analysis

Relative to Guasoni, Larsen, and Leoni (2025), when δ≠0\delta\neq 0, the term

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​y1−y​h​(y)2​(1−h​(y)γ),y∈[0,1),\displaystyle\frac{\delta y}{1-y}h(y)^{2}\Big(1-\frac{h(y)}{\gamma}\Big),\quad y\in[0,1), |  | (3.12) |

in ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) is new. As in the Step 2 in the proof of Theorem [3.1](https://arxiv.org/html/2512.14680v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs"), for ξ≥0\xi\geq 0, the existence of a local solution hξ​(y)>0h\_{\xi}(y)>0 of ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) for yy near 0 with h​(0)=γh(0)=\gamma follows as in Theorem 2.5 in Guasoni, Larsen, and Leoni (2025). This is because the cubic term ([3.12](https://arxiv.org/html/2512.14680v1#S3.E12 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) has no singularity at y=0y=0.

Uniqueness of local solutions of ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) with h​(0)=γh(0)=\gamma follows from the following Lipschitz estimates. For ξ≥0\xi\geq 0, we define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | yξ:=inf{y>0:hξ​(y)=1}∧1,Fξ​(y):=ξσD2​exp⁡{∫0yhξ​(q)−11−q​𝑑q},y∈[0,yξ].\displaystyle\begin{split}y\_{\xi}&:=\inf\{y>0:h\_{\xi}(y)=1\}\land 1,\\ F\_{\xi}(y)&:=\frac{\xi}{\sigma\_{D}^{2}}\exp\Big\{\int\_{0}^{y}\frac{h\_{\xi}(q)-1}{1-q}dq\Big\},\quad y\in[0,y\_{\xi}].\end{split} | |  | (3.13) |

###### Lemma 3.2.

Let γ∈(0,1)\gamma\in(0,1), σD2>0\sigma\_{D}^{2}>0, A>1A>1, δ<0\delta<0, y0∈(0,1)y\_{0}\in(0,1), and ξ¯>0\bar{\xi}>0. Then, there exist constants M1>0M\_{1}>0 and M2>0M\_{2}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |hξ1​(y)−hξ2​(y)|≤M1​y​|ξ1−ξ2|,y∈[0,yξ1∧yξ2∧y0],ξ1,ξ2∈[0,ξ¯],\displaystyle|h\_{\xi\_{1}}(y)-h\_{\xi\_{2}}(y)|\leq M\_{1}y|\xi\_{1}-\xi\_{2}|,\quad y\in[0,y\_{\xi\_{1}}\land y\_{\xi\_{2}}\land y\_{0}],\quad\xi\_{1},\xi\_{2}\in[0,\bar{\xi}], |  | (3.14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Fξ1​(y)−Fξ2​(y)|≤M2​|ξ1−ξ2|,y∈[0,yξ1∧yξ2∧y0],ξ1,ξ2∈[0,ξ¯].\displaystyle|F\_{\xi\_{1}}(y)-F\_{\xi\_{2}}(y)|\leq M\_{2}|\xi\_{1}-\xi\_{2}|,\quad y\in[0,y\_{\xi\_{1}}\land y\_{\xi\_{2}}\land y\_{0}],\quad\xi\_{1},\xi\_{2}\in[0,\bar{\xi}]. |  | (3.15) |

###### Proof.

For ξ1,ξ2∈[0,ξ¯]\xi\_{1},\xi\_{2}\in[0,\bar{\xi}], we let h1,h2∈𝒞1​([0,yξi))h\_{1},h\_{2}\in{\mathcal{C}}^{1}([0,y\_{\xi\_{i}})) be the corresponding local solutions of ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")). We rewrite ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hi′​(y)+1+γy​(hi​(y)−γ)=γ1−y​hi​(y)+Fξi​(y)−A1−y​hi​(y)2+δ​y1−y​hi​(y)2​(1−hi​(y)γ),\displaystyle\begin{split}&h\_{i}^{\prime}(y)+\frac{1+\gamma}{y}\big(h\_{i}(y)-\gamma\big)\\ &=\frac{\gamma}{1-y}h\_{i}(y)+\frac{F\_{\xi\_{i}}(y)-A}{1-y}h\_{i}(y)^{2}+\frac{\delta y}{1-y}h\_{i}(y)^{2}\Big(1-\frac{h\_{i}(y)}{\gamma}\Big),\end{split} | |  | (3.16) |

for y∈(0,yξi)y\in(0,y\_{\xi\_{i}}). Subtracting and multiplying by y1+γy^{1+\gamma} give us

|  |  |  |
| --- | --- | --- |
|  | y1+γ​(h1′​(y)−h2′​(y))+yγ​(1+γ)​(h1​(y)−h2​(y))\displaystyle y^{1+\gamma}\big(h\_{1}^{\prime}(y)-h\_{2}^{\prime}(y)\big)+y^{\gamma}(1+\gamma)\big(h\_{1}(y)-h\_{2}(y)\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =y1+γ​γ1−y​(h1​(y)−h2​(y))\displaystyle=y^{1+\gamma}\frac{\gamma}{1-y}\big(h\_{1}(y)-h\_{2}(y)\big) |  |
|  |  |  |
| --- | --- | --- |
|  | +y1+γ​Fξ1​(y)−Fξ2​(y)1−y​h1​(y)2+y1+γ​Fξ2​(y)−A1−y​(h1​(y)2−h2​(y)2)\displaystyle+y^{1+\gamma}\frac{F\_{\xi\_{1}}(y)-F\_{\xi\_{2}}(y)}{1-y}h\_{1}(y)^{2}+y^{1+\gamma}\frac{F\_{\xi\_{2}}(y)-A}{1-y}\big(h\_{1}(y)^{2}-h\_{2}(y)^{2}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | +y1+γ​δ​y1−y​(h1​(y)2​(1−h1​(y)γ)−h2​(y)2​(1−h2​(y)γ)),y<yξ1∧yξ2.\displaystyle+y^{1+\gamma}\frac{\delta y}{1-y}\bigg(h\_{1}(y)^{2}\Big(1-\frac{h\_{1}(y)}{\gamma}\Big)-h\_{2}(y)^{2}\Big(1-\frac{h\_{2}(y)}{\gamma}\Big)\bigg),\quad y<y\_{\xi\_{1}}\land y\_{\xi\_{2}}. |  |

Because 0≤hi≤10\leq h\_{i}\leq 1, we have the bounds

|  |  |  |
| --- | --- | --- |
|  | |h1​(y)2−h2​(y)2|=(h1​(y)+h2​(y))​|h1​(y)−h2​(y)|≤2​|h1​(y)−h2​(y)|,\displaystyle\big|h\_{1}(y)^{2}-h\_{2}(y)^{2}\big|=\big(h\_{1}(y)+h\_{2}(y)\big)\big|h\_{1}(y)-h\_{2}(y)\big|\leq 2\big|h\_{1}(y)-h\_{2}(y)\big|, |  |

and

|  |  |  |
| --- | --- | --- |
|  | |h1​(y)2​(1−h1​(y)γ)−h2​(y)2​(1−h2​(y)γ)|\displaystyle\bigg|h\_{1}(y)^{2}\Big(1-\frac{h\_{1}(y)}{\gamma}\Big)-h\_{2}(y)^{2}\Big(1-\frac{h\_{2}(y)}{\gamma}\Big)\bigg| |  |
|  |  |  |
| --- | --- | --- |
|  | =|h1​(y)−h2​(y)|​|h1​(y)+h2​(y)−h1​(y)​h2​(y)+h1​(y)2+h2​(y)2γ|\displaystyle=\big|h\_{1}(y)-h\_{2}(y)\big|\left|h\_{1}(y)+h\_{2}(y)-\frac{h\_{1}(y)h\_{2}(y)+h\_{1}(y)^{2}+h\_{2}(y)^{2}}{\gamma}\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤|h1​(y)−h2​(y)|​(2+3γ).\displaystyle\leq\big|h\_{1}(y)-h\_{2}(y)\big|\big(2+\frac{3}{\gamma}\big). |  |

These bounds allow us to use Gronwall’s inequality to derive the bounds ([3.14](https://arxiv.org/html/2512.14680v1#S3.E14 "In Lemma 3.2. ‣ 3.2 Governing ODE analysis ‣ 3 Proofs"))-([3.15](https://arxiv.org/html/2512.14680v1#S3.E15 "In Lemma 3.2. ‣ 3.2 Governing ODE analysis ‣ 3 Proofs")). Because the arguments are identical to those in the proof of Lemma 2.8 in Guasoni, Larsen, and Leoni (2025), we omit the details.

♢\hfill\diamondsuit

*Proof of Lemma [2.3](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium").1:* The following proof adjusts the proof of Theorem 1.1 in Guasoni, Larsen, and Leoni (2025) to include the cubic term in ([3.12](https://arxiv.org/html/2512.14680v1#S3.E12 "In 3.2 Governing ODE analysis ‣ 3 Proofs")).

Step 1/7: For ξ∈(0,(A+δ​1−γγ−γ)​σD2)\xi\in(0,(A+\delta\frac{1-\gamma}{\gamma}-\gamma)\sigma\_{D}^{2}), this step ensures that a global solution to ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) and h​(0)=γh(0)=\gamma exists. We let ff be the solution of ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) produced by Theorem [3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs") for

|  |  |  |
| --- | --- | --- |
|  | a3:=ξσD2−A<δ​1−γγ−γ.a\_{3}:=\frac{\xi}{\sigma\_{D}^{2}}-A<\delta\frac{1-\gamma}{\gamma}-\gamma. |  |

We define

|  |  |  |
| --- | --- | --- |
|  | y1:=inf{y>0:h​(y)=1}∈(0,1]∪{∞}.y\_{1}:=\inf\{y>0:h(y)=1\}\in(0,1]\cup\{\infty\}. |  |

To see y1=∞y\_{1}=\infty, we assume to the contrary that y1∈(0,1]y\_{1}\in(0,1]. Continuity of hh gives h​(y1)=1h(y\_{1})=1. However, ([2.11](https://arxiv.org/html/2512.14680v1#S2.E11 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) gives a2​(h,y)≤ξσD2−A=a3a\_{2}(h,y)\leq\frac{\xi}{\sigma\_{D}^{2}}-A=a\_{3} for y∈[0,y1]y\in[0,y\_{1}] and the comparison principle produces h≤f<1h\leq f<1.

To rule out finite oscillations at some interior point y∗∈(0,1)y^{\*}\in(0,1), we note that there is no singularity in ([3.1](https://arxiv.org/html/2512.14680v1#S3.E1 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) and a standard Lipschitz argument ensures that limy↑y∗h​(y)\lim\_{y\uparrow y^{\*}}h(y) exists. To rule out finite oscillations at y∗=1y^{\*}=1, we note that h​(y)<1h(y)<1 for y∈[0,1)y\in[0,1) gives a2​(h,y)≤ξσD2−A=a3a\_{2}(h,y)\leq\frac{\xi}{\sigma\_{D}^{2}}-A=a\_{3} for y∈[0,1)y\in[0,1), hence, the comparison principle gives h≤f<1h\leq f<1. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤lim supy↑1exp⁡{∫0yh​(q)−11−q​𝑑q}≤lim supy↑1exp⁡{∫0yf​(q)−11−q​𝑑q}=0,\displaystyle 0\leq\limsup\_{y\uparrow 1}\exp\left\{\int\_{0}^{y}\frac{h(q)-1}{1-q}dq\right\}\leq\limsup\_{y\uparrow 1}\exp\left\{\int\_{0}^{y}\frac{f(q)-1}{1-q}dq\right\}=0, |  | (3.17) |

where the last equality uses f​(1)<1f(1)<1. All in all, limy↑1exp⁡{∫0yh​(q)−11−q​𝑑q}=0\lim\_{y\uparrow 1}\exp\big\{\int\_{0}^{y}\frac{h(q)-1}{1-q}dq\big\}=0. To see that limy↑1h​(y)\lim\_{y\uparrow 1}h(y) exists, we proceed as in Step 3/3 of the proof of Theorem [3.1](https://arxiv.org/html/2512.14680v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs") and let (yn)n∈ℕ⊂(0,1)(y\_{n})\_{n\in\mathbb{N}}\subset(0,1) converge to y∗=1y^{\*}=1 such that h′​(yn)=0h^{\prime}(y\_{n})=0. Because hh is bounded, by using a subsequence if necessary, we can assume l:=limn→∞h​(yn)∈[0,1)l:=\lim\_{n\to\infty}h(y\_{n})\in[0,1) exists and solves the analogue of
([3.9](https://arxiv.org/html/2512.14680v1#S3.E9 "In 3.1 Auxiliary ODE analysis ‣ 3 Proofs")) given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0=γ​l−A​l2+δ​l2​(1−lγ).\displaystyle\begin{split}0&=\gamma l-Al^{2}+\delta l^{2}\Big(1-\frac{l}{\gamma}\Big).\end{split} | |  | (3.18) |

Similar to Step 3/3 of the proof of Theorem [3.1](https://arxiv.org/html/2512.14680v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs"), the cubic equation ([3.18](https://arxiv.org/html/2512.14680v1#S3.E18 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) has exactly one solution in (0,1)(0,1), which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | l=γ2​δ​(δ−A+(A−δ)2+4​δ)≤γ.\displaystyle l=\frac{\gamma}{2\delta}\Big(\delta-A+\sqrt{(A-\delta)^{2}+4\delta}\Big)\leq\gamma. |  | (3.19) |

The upper bound in ([3.19](https://arxiv.org/html/2512.14680v1#S3.E19 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) comes from A≥1A\geq 1. To rule out l=0l=0 as a possible limit, we argue by contradiction to see

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =limn→∞(a0​(yn)+h​(yn)1−yn​(a1​(yn)+a2​(h,yn)​h​(yn)+δ​yn​h​(yn)​(1−h​(yn)γ)))\displaystyle=\lim\_{n\to\infty}\bigg(a\_{0}(y\_{n})+\frac{h(y\_{n})}{1-y\_{n}}\Big(a\_{1}(y\_{n})+a\_{2}(h,y\_{n})h(y\_{n})+\delta y\_{n}h(y\_{n})\big(1-\frac{h(y\_{n})}{\gamma}\big)\Big)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =γ​(1+γ)+limn→∞h​(yn)1−yn​γ.\displaystyle=\gamma(1+\gamma)+\lim\_{n\to\infty}\frac{h(y\_{n})}{1-y\_{n}}\gamma. |  |

This gives a contradiction because h≥0h\geq 0. All in all, hh cannot oscillate and limy↑1h​(y)\lim\_{y\uparrow 1}h(y) exists and equals ll in ([3.19](https://arxiv.org/html/2512.14680v1#S3.E19 "In 3.2 Governing ODE analysis ‣ 3 Proofs")).

Step 2/7: For y0∈(0,1)y\_{0}\in(0,1), this step proves that limξ↑∞h​(y0)=∞\lim\_{\xi\uparrow\infty}h(y\_{0})=\infty. Because δ<0\delta<0 and h>0h>0, the cubic term ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) is non-negative and so we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | h′​(y)≥a0​(y)+a1​(y)1−y​h​(y)+a2​(h,y)+δ​y1−y​h​(y)2.\displaystyle h^{\prime}(y)\geq a\_{0}(y)+\frac{a\_{1}(y)}{1-y}h(y)+\frac{a\_{2}(h,y)+\delta y}{1-y}h(y)^{2}. |  | (3.20) |

As in Lemma 2.7 in Guasoni, Larsen, and Leoni (2025), the comparison principle ensures that hh is bigger than the solution to a quadratic Riccati equation. For sufficiently large ξ>0\xi>0, the solution to this Riccati equation explodes at some y∈(0,y0]y\in(0,y\_{0}].

Step 3/7: As in Guasoni, Larsen, and Leoni (2025), we define the subset Ξ\Xi of (0,∞)(0,\infty) by

|  |  |  |
| --- | --- | --- |
|  | Ξ:={ξ>0:h∈𝒞​([0,1])∩𝒞1​([0,1)) solves ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) with ​h​(0)=γ​ and ​h​(1)≤γ}.\Xi:=\big\{\xi>0:\text{$h\in{\mathcal{C}}([0,1])\cap{\mathcal{C}}^{1}([0,1))$ solves \eqref{hODE} with }h(0)=\gamma\text{ and }h(1)\leq\gamma\big\}. |  |

Step 2 ensures that ξ<A+δ​1−γγ−γ\xi<A+\delta\frac{1-\gamma}{\gamma}-\gamma produces a solution hh with h<1h<1. This step generalizes this property to all ξ∈Ξ\xi\in\Xi. The proof is similar to the proof of Lemma 2.10.2 in Guasoni, Larsen, and Leoni (2025). We assume for the sake of contradiction that there exists y0∈[0,1]y\_{0}\in[0,1] with h​(y0)≥1h(y\_{0})\geq 1. Because h​(0)=γ<1h(0)=\gamma<1 and h​(1)≤γ<1h(1)\leq\gamma<1, we have y0∈(0,1)y\_{0}\in(0,1) and so

|  |  |  |
| --- | --- | --- |
|  | h′​(y0)=0,h′′​(y0)≤0.h^{\prime}(y\_{0})=0,\quad h^{\prime\prime}(y\_{0})\leq 0. |  |

Inserting h′​(y0)=0h^{\prime}(y\_{0})=0 into ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) produces

|  |  |  |  |
| --- | --- | --- | --- |
|  | a2​(h,y0)=−(1−y)​a0​(y0)h​(y0)2−a1​(y0)h​(y0)−δ​y0​(γ−h​(y0))γ.\displaystyle a\_{2}(h,y\_{0})=-\frac{(1-y)a\_{0}(y\_{0})}{h(y\_{0})^{2}}-\frac{a\_{1}(y\_{0})}{h(y\_{0})}-\frac{\delta y\_{0}\big(\gamma-h(y\_{0})\big)}{\gamma}. |  | (3.21) |

By using h′​(y0)=0h^{\prime}(y\_{0})=0 and ([3.21](https://arxiv.org/html/2512.14680v1#S3.E21 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) when computing the derivative of ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")), we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h′′​(y0)=(h​(y0)−γ)​(γ2+γ−δ​y02​h​(y0)2)γ​(1−y0)​y02+h​(y0)21−y0​∂∂y​a2​(h,y0)≥(γ+1)​(h​(y0)−γ)(1−y0)​y02.\displaystyle\begin{split}h^{\prime\prime}(y\_{0})&=\frac{\big(h(y\_{0})-\gamma\big)\big(\gamma^{2}+\gamma-\delta y\_{0}^{2}h(y\_{0})^{2}\big)}{\gamma(1-y\_{0})y\_{0}^{2}}+\frac{h(y\_{0})^{2}}{1-y\_{0}}\frac{\partial}{\partial y}a\_{2}(h,y\_{0})\\ &\geq\frac{(\gamma+1)\big(h(y\_{0})-\gamma\big)}{(1-y\_{0})y\_{0}^{2}}.\end{split} | |  | (3.22) |

The inequality in ([3.22](https://arxiv.org/html/2512.14680v1#S3.E22 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) comes from δ<0\delta<0 and

|  |  |  |
| --- | --- | --- |
|  | ∂∂y​a2​(h,y)=ξσD2​exp⁡{∫0yh​(q)−11−q​𝑑q}​h​(y)−11−y,\frac{\partial}{\partial y}a\_{2}(h,y)=\frac{\xi}{\sigma\_{D}^{2}}\exp\Big\{\int\_{0}^{y}\frac{h(q)-1}{1-q}dq\Big\}\frac{h(y)-1}{1-y}, |  |

which is non-negative at y=y0y=y\_{0} because we have assumed h​(y0)≥1h(y\_{0})\geq 1. The second line in ([3.22](https://arxiv.org/html/2512.14680v1#S3.E22 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) is strictly positive, which contradicts h′′​(y0)≤0h^{\prime\prime}(y\_{0})\leq 0.

Step 4/7: Step 2 ensures that Ξ≠∅\Xi\neq\emptyset and Step 3 ensures that Ξ\Xi is a bounded subset of (0,∞)(0,\infty). Consequently, ξ0:=supΞ∈(0,∞)\xi\_{0}:=\sup\Xi\in(0,\infty). This step proves ξ0∉Ξ\xi\_{0}\notin\Xi. We argue by contradiction and assume ξ0∈Ξ\xi\_{0}\in\Xi and let hξ0h\_{\xi\_{0}} denote the corresponding solution to ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")). Next, we use Lemma [3.2](https://arxiv.org/html/2512.14680v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.2 Governing ODE analysis ‣ 3 Proofs") to construct ξ0′∈(ξ0,ξ0+1)\xi\_{0}^{\prime}\in(\xi\_{0},\xi\_{0}+1) with ξ0′∈Ξ\xi\_{0}^{\prime}\in\Xi.
The assumption ξ0∈Ξ\xi\_{0}\in\Xi gives hξ0​(1)≤γ<1h\_{\xi\_{0}}(1)\leq\gamma<1 and, similarly to ([3.17](https://arxiv.org/html/2512.14680v1#S3.E17 "In 3.2 Governing ODE analysis ‣ 3 Proofs")), we have limy↑1Fξ0​(y)=0\lim\_{y\uparrow 1}F\_{\xi\_{0}}(y)=0. Therefore, because A>1A>1, we can find y0∈(0,1)y\_{0}\in(0,1) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀y∈(y0,1):Fξ0​(y)<A−12.\displaystyle\forall y\in(y\_{0},1):F\_{\xi\_{0}}(y)<\frac{A-1}{2}. |  | (3.23) |

From ([3.14](https://arxiv.org/html/2512.14680v1#S3.E14 "In Lemma 3.2. ‣ 3.2 Governing ODE analysis ‣ 3 Proofs")), there exists a constant M1M\_{1} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀ξ∈(ξ0,ξ0+1)∀y∈[0,yξ∧y0]:|hξ(y)−hξ0(y)|≤M1|ξ−ξ0|.\displaystyle\forall\xi\in(\xi\_{0},\xi\_{0}+1)\;\forall y\in[0,y\_{\xi}\land y\_{0}]:\quad|h\_{\xi}(y)-h\_{\xi\_{0}}(y)|\leq M\_{1}|\xi-\xi\_{0}|. |  | (3.24) |

Because hξ0<1h\_{\xi\_{0}}<1, we can find ξ∈(ξ0,ξ0+1)\xi\in(\xi\_{0},\xi\_{0}+1) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | hξ​(y)≤|hξ​(y)−hξ0​(y)|+hξ0​(y)≤M1​|ξ−ξ0|+supy∈[0,1]hξ0​(y)<1,\displaystyle h\_{\xi}(y)\leq|h\_{\xi}(y)-h\_{\xi\_{0}}(y)|+h\_{\xi\_{0}}(y)\leq M\_{1}|\xi-\xi\_{0}|+\sup\_{y\in[0,1]}h\_{\xi\_{0}}(y)<1, |  | (3.25) |

for y≤yξ∧y0=y0y\leq y\_{\xi}\land y\_{0}=y\_{0}. From ([3.15](https://arxiv.org/html/2512.14680v1#S3.E15 "In Lemma 3.2. ‣ 3.2 Governing ODE analysis ‣ 3 Proofs")), there exists a constant M2M\_{2} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀ξ∈(ξ0,ξ0+1)∀y∈[0,yξ∧y0]:|Fξ(y)−Fξ0(y)|≤M2|ξ−ξ0|.\displaystyle\forall\xi\in(\xi\_{0},\xi\_{0}+1)\;\forall y\in[0,y\_{\xi}\land y\_{0}]:\quad|F\_{\xi}(y)-F\_{\xi\_{0}}(y)|\leq M\_{2}|\xi-\xi\_{0}|. |  | (3.26) |

Let ξ∈(ξ0,ξ0+1)\xi\in(\xi\_{0},\xi\_{0}+1) satisfy ([3.25](https://arxiv.org/html/2512.14680v1#S3.E25 "In 3.2 Governing ODE analysis ‣ 3 Proofs")). Because yξ>y0y\_{\xi}>y\_{0}, the inequality ([3.26](https://arxiv.org/html/2512.14680v1#S3.E26 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fξ​(y0)≤|Fξ​(y0)−Fξ0​(y0)|+Fξ0​(y0)≤M2​|ξ−ξ0|+A−12,\displaystyle F\_{\xi}(y\_{0})\leq|F\_{\xi}(y\_{0})-F\_{\xi\_{0}}(y\_{0})|+F\_{\xi\_{0}}(y\_{0})\leq M\_{2}|\xi-\xi\_{0}|+\frac{A-1}{2}, |  | (3.27) |

where the last inequality uses ([3.23](https://arxiv.org/html/2512.14680v1#S3.E23 "In 3.2 Governing ODE analysis ‣ 3 Proofs")). Because M2M\_{2} does not depend on ξ\xi, we can lower ξ\xi so that ([3.27](https://arxiv.org/html/2512.14680v1#S3.E27 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) ensures Fξ​(y0)<A−1F\_{\xi}(y\_{0})<A-1. Because Fξ​(y)F\_{\xi}(y) is decreasing in y∈[0,yξ]y\in[0,y\_{\xi}], we can use the comparison principle to see hξ​(y)≤f​(y)<1h\_{\xi}(y)\leq f(y)<1 for y∈[y0,yξ]y\in[y\_{0},y\_{\xi}] for ff given by Theorem [3.1](https://arxiv.org/html/2512.14680v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs").2 with a3:=−1a\_{3}:=-1 and f​(y0)=hξ​(y0)f(y\_{0})=h\_{\xi}(y\_{0}). Therefore, yξ=1y\_{\xi}=1 and because ξ>ξ0\xi>\xi\_{0}, we get a contradiction.

Step 5/7: We let (ξn)n∈ℕ⊂Ξ(\xi\_{n})\_{n\in\mathbb{N}}\subset\Xi be an increasing sequence converging to ξ0:=supΞ\xi\_{0}:=\sup\Xi. This step proves that the pointwise limit hξ0:=limn→∞hξnh\_{\xi\_{0}}:=\lim\_{n\to\infty}h\_{\xi\_{n}} exists and satisfies ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) and ([2.10](https://arxiv.org/html/2512.14680v1#S2.E10 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")). The comparison principle ensures that hξn≤hξn+1h\_{\xi\_{n}}\leq h\_{\xi\_{n+1}} and so hξ0h\_{\xi\_{0}} is a well-defined limit. The Monotone Convergence Theorem ensures that ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) holds. To see that hξ0​(1)=1h\_{\xi\_{0}}(1)=1 in ([2.10](https://arxiv.org/html/2512.14680v1#S2.E10 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) holds, we can use 0≤hξ0≤10\leq h\_{\xi\_{0}}\leq 1 and argue as in Step 2 to rule out oscillations and so hξ0​(1):=limy↑1hξ0​(y)∈[0,1]h\_{\xi\_{0}}(1):=\lim\_{y\uparrow 1}h\_{\xi\_{0}}(y)\in[0,1] exists. However, Step 5 and local uniqueness of solutions give hξ0∉Ξh\_{\xi\_{0}}\notin\Xi and so hξ0​(1)∈(γ,1]h\_{\xi\_{0}}(1)\in(\gamma,1]. To see that hξ0​(1)∈(γ,1)h\_{\xi\_{0}}(1)\in(\gamma,1) is impossible, we can argue as in Step 2.

Step 6/7: The ODE in ([2.9](https://arxiv.org/html/2512.14680v1#S2.E9 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) produces the integral representation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y1+γ​(1−y)γ​hξ0​(y)=∫0yq1+γ​(1−q)γ​(a0​(q)+a2​(hξ0,q)1−q​hξ0​(q)2+δ​q1−q​hξ0​(q)2​(1−hξ0​(q)γ))​𝑑q,\displaystyle\begin{split}&y^{1+\gamma}(1-y)^{\gamma}h\_{\xi\_{0}}(y)\\ &=\int\_{0}^{y}q^{1+\gamma}(1-q)^{\gamma}\bigg(a\_{0}(q)+\frac{a\_{2}(h\_{\xi\_{0}},q)}{1-q}h\_{\xi\_{0}}(q)^{2}+\frac{\delta q}{1-q}h\_{\xi\_{0}}(q)^{2}\Big(1-\frac{h\_{\xi\_{0}}(q)}{\gamma}\Big)\bigg)dq,\end{split} | |  | (3.28) |

for y∈[0,1)y\in[0,1). Because 0≤hξ0≤10\leq h\_{\xi\_{0}}\leq 1 and hξ0​(0)=γ<1h\_{\xi\_{0}}(0)=\gamma<1, the following limit exists

|  |  |  |
| --- | --- | --- |
|  | ∫01hξ0​(q)−11−q​𝑑q:=limy↑1∫0yhξ0​(q)−11−q​𝑑q∈[−∞,0).\int\_{0}^{1}\frac{h\_{\xi\_{0}}(q)-1}{1-q}dq:=\lim\_{y\uparrow 1}\int\_{0}^{y}\frac{h\_{\xi\_{0}}(q)-1}{1-q}dq\in[-\infty,0). |  |

Unlike ([3.17](https://arxiv.org/html/2512.14680v1#S3.E17 "In 3.2 Governing ODE analysis ‣ 3 Proofs")), this limit is finite. To compute the limit, we divide y1+γ​(1−y)γy^{1+\gamma}(1-y)^{\gamma} on both sides of ([3.28](https://arxiv.org/html/2512.14680v1#S3.E28 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) and use L’Hopital’s rule when passing y↑1y\uparrow 1 to see

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡{∫01hξ0​(q)−11−q​𝑑q}=σD2ξ0​(A−γ+δ​1−γγ).\displaystyle\exp\left\{\int\_{0}^{1}\frac{h\_{\xi\_{0}}(q)-1}{1-q}dq\right\}=\frac{\sigma\_{D}^{2}}{\xi\_{0}}\Big(A-\gamma+\delta\frac{1-\gamma}{\gamma}\Big). |  | (3.29) |

To see that hξ0≥γh\_{\xi\_{0}}\geq\gamma, the limit in ([3.29](https://arxiv.org/html/2512.14680v1#S3.E29 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) and hξ0≤1h\_{\xi\_{0}}\leq 1 produce the following bound for
([2.11](https://arxiv.org/html/2512.14680v1#S2.E11 "In item 1 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium"))

|  |  |  |
| --- | --- | --- |
|  | a2​(hξ0,y)≥σD2ξ0​exp⁡{∫01hξ0​(q)−11−q​𝑑q}−A=δ​1−γγ−γ>−1.a\_{2}(h\_{\xi\_{0}},y)\geq\frac{\sigma\_{D}^{2}}{\xi\_{0}}\exp\left\{\int\_{0}^{1}\frac{h\_{\xi\_{0}}(q)-1}{1-q}dq\right\}-A=\delta\frac{1-\gamma}{\gamma}-\gamma>-1. |  |

The comparison principle gives hξ0≥f≥γh\_{\xi\_{0}}\geq f\geq\gamma where ff is from Theorem [3.1](https://arxiv.org/html/2512.14680v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Auxiliary ODE analysis ‣ 3 Proofs") with a3:=−1a\_{3}:=-1.

Step 7/7: Because hξ0≤1h\_{\xi\_{0}}\leq 1, the difference quotient satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(y):=1−hξ0​(y)1−y≥0,y∈[0,1).\displaystyle g(y):=\frac{1-h\_{\xi\_{0}}(y)}{1-y}\geq 0,\quad y\in[0,1). |  | (3.30) |

To prove that limy↑1g​(y)\lim\_{y\uparrow 1}g(y) exists and is identical to limy↑1hξ0′​(y)\lim\_{y\uparrow 1}h^{\prime}\_{\xi\_{0}}(y), we need a representation of g′g^{\prime} and g′′g^{\prime\prime}. The formula in ([3.29](https://arxiv.org/html/2512.14680v1#S3.E29 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) allows us to rewrite Fξ0F\_{\xi\_{0}} in ([3.13](https://arxiv.org/html/2512.14680v1#S3.E13 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) as

|  |  |  |
| --- | --- | --- |
|  | Fξ0​(y)=(A−γ+δ​1−γγ)​exp⁡{∫y1g​(q)​𝑑q},y∈[0,1].F\_{\xi\_{0}}(y)=\Big(A-\gamma+\delta\frac{1-\gamma}{\gamma}\Big)\exp\Big\{\int\_{y}^{1}g(q)dq\Big\},\quad y\in[0,1]. |  |

Inserting this expression into ([3.16](https://arxiv.org/html/2512.14680v1#S3.E16 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) and using g′​(y)=g​(y)−hξ0′​(y)1−yg^{\prime}(y)=\frac{g(y)-h^{\prime}\_{\xi\_{0}}(y)}{1-y} give

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(y)−(1−y)​g′​(y)=1+γy​(γ−hξ0​(y))+γ​hξ0​(y)​g​(y)+(A−γ+δ​1−γγ)​exp⁡{∫y1g​(q)​𝑑q}−11−y​hξ0​(y)2+δ​y​hξ0​(y)2​(g​(y)γ+1+γγ​y).\displaystyle\begin{split}g(y)-(1-y)g^{\prime}(y)&=\frac{1+\gamma}{y}\big(\gamma-h\_{\xi\_{0}}(y)\big)+\gamma h\_{\xi\_{0}}(y)g(y)\\ &+\Big(A-\gamma+\delta\frac{1-\gamma}{\gamma}\Big)\frac{\exp\Big\{\int\_{y}^{1}g(q)dq\Big\}-1}{1-y}h\_{\xi\_{0}}(y)^{2}\\ &+\delta yh\_{\xi\_{0}}(y)^{2}\Big(\frac{g(y)}{\gamma}+\frac{1+\gamma}{\gamma y}\Big).\end{split} | |  | (3.31) |

We split the argument into two cases: First, we argue by contradiction to rule out that g​(y)g(y) increases to infinity as y↑1y\uparrow 1. The Mean-Value Theorem and the assumed monotonicity of g​(y)≥0g(y)\geq 0 for yy near 11 give

|  |  |  |
| --- | --- | --- |
|  | exp⁡{∫y1g​(q)​𝑑q}−1≥exp⁡{∫y1g​(q)​𝑑q}​g​(y)​(1−y)≥g​(y)​(1−y).\displaystyle\exp\Big\{\int\_{y}^{1}g(q)dq\Big\}-1\geq\exp\Big\{\int\_{y}^{1}g(q)dq\Big\}g(y)(1-y)\geq g(y)(1-y). |  |

Combining this inequality with the ODE in ([3.31](https://arxiv.org/html/2512.14680v1#S3.E31 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) and g′​(y)≥0g^{\prime}(y)\geq 0 gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(y)≥1+γy​(γ−hξ0​(y))+γ​hξ0​(y)​g​(y)+(A−γ+δ​1−γγ)​g​(y)​hξ0​(y)2+δ​y​hξ0​(y)2​(g​(y)γ+1−γγ​y).\displaystyle\begin{split}g(y)&\geq\frac{1+\gamma}{y}\big(\gamma-h\_{\xi\_{0}}(y)\big)+\gamma h\_{\xi\_{0}}(y)g(y)\\ &+\Big(A-\gamma+\delta\frac{1-\gamma}{\gamma}\Big)g(y)h\_{\xi\_{0}}(y)^{2}+\delta yh\_{\xi\_{0}}(y)^{2}\Big(\frac{g(y)}{\gamma}+\frac{1-\gamma}{\gamma y}\Big).\end{split} | |  | (3.32) |

Rearranging ([3.32](https://arxiv.org/html/2512.14680v1#S3.E32 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) and passing y↑1y\uparrow 1 produce the contradiction

|  |  |  |
| --- | --- | --- |
|  | 1−γ2+δ−δγ≥(A−1−δ+2​δγ)​limy↑1g​(y)=∞.1-\gamma^{2}+\delta-\frac{\delta}{\gamma}\geq\Big(A-1-\delta+2\frac{\delta}{\gamma}\Big)\lim\_{y\uparrow 1}g(y)=\infty. |  |

Second, we consider oscillations. We differentiate ([3.31](https://arxiv.org/html/2512.14680v1#S3.E31 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) at a point y∈(0,1)y\in(0,1) with g′​(y)=0g^{\prime}(y)=0 to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(1−y)2​y2​g′′​(y)\displaystyle\gamma(1-y)^{2}y^{2}g^{\prime\prime}(y) | =yg(y)(yh(y)(2Aγ+e∫y1g​(q)​𝑑q(h(y)−2)(Aγ−γ(γ+δ)+δ)−γ2\displaystyle=yg(y)\Big(yh(y)\big(2A\gamma+e^{\int\_{y}^{1}g(q)dq}(h(y)-2)(A\gamma-\gamma(\gamma+\delta)+\delta)-\gamma^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2δyh(y)−δh(y)−2γδy+2δy)+γ(γ−(γ+2)y+1))\displaystyle+2\delta yh(y)-\delta h(y)-2\gamma\delta y+2\delta y\big)+\gamma(\gamma-(\gamma+2)y+1)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(γ+1)​γ2+(y−1)​y2​g​(y)2​(γ2+2​δ​y​h​(y))\displaystyle+(\gamma+1)\gamma^{2}+(y-1)y^{2}g(y)^{2}\left(\gamma^{2}+2\delta yh(y)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(γ−1)​δ​y2​h​(y)2−(γ+1)​γ​h​(y),y∈(0,1).\displaystyle-(\gamma-1)\delta y^{2}h(y)^{2}-(\gamma+1)\gamma h(y),\quad y\in(0,1). |  |

Let (yn)n∈ℕ(y\_{n})\_{n\in\mathbb{N}} be a sequence of local maxima for gg with yn↑1y\_{n}\uparrow 1 such that

|  |  |  |
| --- | --- | --- |
|  | ∀n∈ℕ:g′(yn)=0,g′′(yn)≤0,limn→∞g(yn)=lim supy↑1g(y)∈[0,∞].\forall n\in\mathbb{N}:\quad g^{\prime}(y\_{n})=0,\quad g^{\prime\prime}(y\_{n})\leq 0,\quad\lim\_{n\to\infty}g(y\_{n})=\limsup\_{y\uparrow 1}g(y)\in[0,\infty]. |  |

Because hξ0​(1)=1h\_{\xi\_{0}}(1)=1, we have

|  |  |  |
| --- | --- | --- |
|  | limn→∞(1−yn)​g​(yn)=limn→∞(1−hξ0​(yn))=0.\lim\_{n\to\infty}(1-y\_{n})g(y\_{n})=\lim\_{n\to\infty}\big(1-h\_{\xi\_{0}}(y\_{n})\big)=0. |  |

Therefore, the above ODE for g′′g^{\prime\prime} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≥limn→∞γ​(1−yn)2​yn2​g′′​(yn)\displaystyle\geq\lim\_{n\to\infty}\gamma(1-y\_{n})^{2}y^{2}\_{n}g^{\prime\prime}(y\_{n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(1−γ)​(γ2+γ−δ)+(γ​(A−δ−1)+2​δ)​limn→∞g​(yn).\displaystyle=-(1-\gamma)\left(\gamma^{2}+\gamma-\delta\right)+\Big(\gamma(A-\delta-1)+2\delta\Big)\lim\_{n\to\infty}g(y\_{n}). |  |

This gives the upper bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supy↑1g​(y)≤(1−γ)​(γ2+γ−δ)γ​(A−δ−1)+2​δ.\displaystyle\limsup\_{y\uparrow 1}g(y)\leq\frac{(1-\gamma)\left(\gamma^{2}+\gamma-\delta\right)}{\gamma(A-\delta-1)+2\delta}. |  | (3.33) |

Next, let (yn)n∈ℕ(y\_{n})\_{n\in\mathbb{N}} be a sequence of local minima for gg with yn↑1y\_{n}\uparrow 1 such that

|  |  |  |
| --- | --- | --- |
|  | ∀n∈ℕ:g′(yn)=0,g′′(yn)≥0,limn→∞g(yn)=lim infy↑1g(y)∈[0,∞].\forall n\in\mathbb{N}:\quad g^{\prime}(y\_{n})=0,\quad g^{\prime\prime}(y\_{n})\geq 0,\quad\lim\_{n\to\infty}g(y\_{n})=\liminf\_{y\uparrow 1}g(y)\in[0,\infty]. |  |

Then, similarly to ([3.33](https://arxiv.org/html/2512.14680v1#S3.E33 "In 3.2 Governing ODE analysis ‣ 3 Proofs")), we have the lower bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infn→∞g​(yn)≥(1−γ)​(γ2+γ−δ)γ​(A−δ−1)+2​δ.\displaystyle\liminf\_{n\to\infty}g(y\_{n})\geq\frac{(1-\gamma)\left(\gamma^{2}+\gamma-\delta\right)}{\gamma(A-\delta-1)+2\delta}. |  | (3.34) |

The two bounds ([3.33](https://arxiv.org/html/2512.14680v1#S3.E33 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) and ([3.34](https://arxiv.org/html/2512.14680v1#S3.E34 "In 3.2 Governing ODE analysis ‣ 3 Proofs")) produce the limit limy↑1g​(y)=g​(1)=(1−γ)​(γ2+γ−δ)γ​(A−δ−1)+2​δ\lim\_{y\uparrow 1}g(y)=g(1)=\frac{(1-\gamma)\left(\gamma^{2}+\gamma-\delta\right)}{\gamma(A-\delta-1)+2\delta}.

An application of L’Hopital’s rule shows that hξ0′​(1):=limy↑1hξ0′​(y)h\_{\xi\_{0}}^{\prime}(1):=\lim\_{y\uparrow 1}h\_{\xi\_{0}}^{\prime}(y) also exists with hξ0′​(1)=g​(1)h\_{\xi\_{0}}^{\prime}(1)=g(1). Because the argument is identical to the one given in the proof of Lemma 2.10.7 in Guasoni, Larsen, and Leoni (2025), we omit the details.

♢\hfill\diamondsuit

### 3.3 Remaining proofs

*Proof of Lemma [2.3](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium").2:* A strong solution to ([2.13](https://arxiv.org/html/2512.14680v1#S2.E13 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")) is proven as in Theorem 3.1 in Guasoni, Larsen, and Leoni (2025).

♢\hfill\diamondsuit

*Proof of Theorem [2.4](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium"):* Given Lemma [2.3](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium"), the proof of Theorem [2.4](https://arxiv.org/html/2512.14680v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium") is identical to the proof of Theorem 3.6.2 in Guasoni, Larsen, and Leoni (2025). The only difference is the classification of the boundary point y=1y=1 for the SDE ([2.13](https://arxiv.org/html/2512.14680v1#S2.E13 "In item 2 ‣ Lemma 2.3. ‣ 2.2 Equilibrium ‣ 2 Radner equilibrium")). However, the needed adjustment was already presented in the survival analysis in Section
[2.3](https://arxiv.org/html/2512.14680v1#S2.SS3 "2.3 Survival analysis ‣ 2 Radner equilibrium").

♢\hfill\diamondsuit

## References

* [1]
   J. Borovička (2019): *Survival and long-run dynamics with heterogeneous
  beliefs under recursive preferences*, Journal of Political Economy 128, 206-251.
* [2]
   S. Basak, D. Cuoco (1998): *An equilibrium model with restricted stock market participation*, Review of Financial Studies 11, 309–341.
* [3]
   H. S. Bhamra and R. Uppal (2014): *Asset prices with heterogeneity in preferences and beliefs*, Review of Financial Studies 27(2), 519–580.
* [4]
   D. Duffie (2001): *Dynamic asset pricing theory*, 3rd Ed., Princeton University Press.
* [5]
   P. Guasoni, K. Larsen, and G. Leoni (2025): *Existence of an equilibrium with limited stock market participation and power utilities*, Journal of Differential Equations 448, 1–56.
* [6]
   B. Huang and H. Liu (2025): *Wealth dynamics and asset prices with
  heterogeneous beliefs under smooth ambiguity*, working paper.
* [7]
   J. Hugonnier (2012): *Rational asset pricing bubbles and portfolio
  constraints*, Journal of Economic Theory 147, 2260–2302.
* [8]
   O. Kallenberg (2021): *Foundations of modern probability*, 3rd Ed., Springer.
* [9]
   I. Karatzas, S. Shreve (1988): *Brownian motion and stochastic calculus*, 2nd Ed., Springer.
* [10]
   L. Kogan, S. A. Ross, J. Wang, and M. M. Westerfield (2006): *The price impact and survival of irrational traders*, Journal of Finance 61, 195–229.
* [11]
  R. Mehra and E. C. Prescott (1985): *The equity premium: A puzzle*, Journal of Monetary Economics 15(2), 145–161.
* [12]
   R. Prieto (2013): *Dynamic equilibrium with heterogeneous agents and risk constraints*, working paper.
* [13]
   P. Weil (1989): *The equity premium puzzle and the risk-free rate puzzle*, Journal of Monetary Economics 24, 401–421.
* [14]
   K. Weston (2024): *Existence of an equilibrium with limited participation*, Finance & Stochastics 28(2), 329–361.
* [15]
   H. Yan (2008): *Natural selection in financial markets: Does it work?*, Management Science 54(11), 1935–1950.