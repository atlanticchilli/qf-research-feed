---
authors:
- Nawaf Mohammed
doc_id: arxiv:2512.07787v1
family_id: arxiv:2512.07787
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables'
url_abs: http://arxiv.org/abs/2512.07787v1
url_html: https://arxiv.org/html/2512.07787v1
venue: arXiv q-fin
version: 1
year: 2025
---


Nawaf Mohammed 
<nawaf.mohammed.ac@gmail.com>

###### Abstract

We investigate the extremal aggregation behavior of Value-at-Risk (VaR) – that is, its additivity properties across all probability levels – for sums of one-sided random variables. For risks supported on [0,∞)[0,\infty), we show that VaR sub-additivity is impossible except in the degenerate case of exact additivity, which holds only under co-monotonicity. To characterize when VaR is instead fully super-additive, we introduce two structural conditions: negative simplex dependence (NSD) for the joint distribution and simplex dominance (SD) for a margin-dependent functional. Together, these conditions provide a unified and easily verifiable framework that accommodates non-identical margins, heavy-tailed laws, and a wide spectrum of negative dependence structures. All results extend to random variables with arbitrary finite lower or upper endpoints, yielding sharp constraints on when strict sub- or super-additivity can occur.

  

Key words and phrases: Value-at-Risk; VaR sub-additivity; VaR super-additivity; one-sided random variables; negative simplex dependence; simplex dominant functions

JEL Classification:

## 1 Introduction

The study of quantiles has long been a cornerstone of mathematical and statistical research. Quantiles provide a fundamental link between abstract probability models and the observable outcomes they generate. In risk management, in particular, quantiles have been regarded as essential tools for assessing the riskiness of losses, asset prices, and other financial variables. Their most prominent manifestation is the Value-at-Risk (VaR) [Linsmeier2000], which is interpreted as the minimum amount of capital a financial institution must hold so that losses exceed this level only with a small, pre-specified probability.
  
 
  
A variety of risk measures have been developed to refine or extend VaR. Among them, the conditional tail expectation – also known as expected shortfall – [Acerbi.2002, Tasche2002] addresses several limitations of VaR, most notably the failure of sub-additivity. Nevertheless, interest in VaR has persisted, partly due to its ability to capture the opposite phenomenon of super-additivity, a feature that does not rely on the integrability requirements imposed by alternative risk measures. In this paper, we examine the extremal behaviors of VaR, focusing on the conditions under which it exhibits sub-additivity or super-additivity across all probability thresholds.
  
 
  
To formalize our analysis, we consider random vectors 𝑿=(X1,…,Xn)\bm{X}=(X\_{1},\dots,X\_{n}), n∈ℕn\in\mathbb{N}, whose components are random variables representing, for example, asset prices or insurance losses. We focus in particular on their aggregate,

|  |  |  |
| --- | --- | --- |
|  | S=∑i=1nXi.S=\sum\_{i=1}^{n}X\_{i}. |  |

For any random variable or random vector, we denote its probability density function, cumulative distribution function (CDF), and decumulative (survival) function (DDF) by ff, FF, and F¯\overline{F}, respectively, using subscripts to indicate the relevant variables. For example, F𝑿F\_{\bm{X}} denotes the joint CDF of the random vector 𝐗\mathbf{X}, while FXiF\_{X\_{i}} denotes the marginal CDF of XiX\_{i} for i∈{1,…,n}i\in\{1,\dots,n\}. Unless explicitly stated, we impose no integrability assumptions on the random variables.
  
  
Throughout the remainder of the paper, we assume that each random variable XiX\_{i} has support with lower endpoint at zero, that is,

|  |  |  |
| --- | --- | --- |
|  | ai=sup{x∈ℝ:FXi​(x)≤0}=0,∀i∈{1,…,n}.a\_{i}=\sup\{x\in\mathbb{R}:F\_{X\_{i}}(x)\leq 0\}=0,\qquad\forall i\in\{1,\dots,n\}. |  |

In the final section, we show how this assumption can be relaxed. In particular, we extend all results to the setting where the lower endpoints aia\_{i} are arbitrary but finite, and also to the complementary case in which the random variables are instead bounded above.
  
  
Finally, for any random variable ZZ, we define its VaR at confidence level p∈(0,1)p\in(0,1) as the left-quantile (left-inverse) of its distribution:

|  |  |  |
| --- | --- | --- |
|  | VaRp​[Z]=inf{z∈ℝ:FZ​(z)≥p}.\mathrm{VaR}\_{p}[Z]=\inf\{z\in\mathbb{R}:F\_{Z}(z)\geq p\}. |  |

Our primary objective is to investigate how the VaR of the sum,
VaRp​[S]{\mathrm{VaR}}\_{p}[S], compares to the sum of the individual VaRs,
∑i=1nVaRp​[Xi]\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i}] for all p∈(0,1)p\in(0,1). To provide a precise framework for this comparison, we
introduce the following definitions.

###### Definition 1.1.

We say that 𝐗\bm{X} is
VaR sub-additive (respectively, VaR super-additive) if

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRp​[S]≤(≥)​∑i=1nVaRp​[Xi],∀p∈(0,1).{\mathrm{VaR}}\_{p}[S]\leq(\geq)\;\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i}],\quad\forall p\in(0,1). |  | (1.1) |

In particular, 𝐗\bm{X} is called VaR additive if equality holds for all probability levels p∈(0,1)p\in(0,1).

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2512.07787v1#S2 "2 VaR Sub-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") establishes an impossibility theorem for VaR sub-additivity, extending the recent findings of [Imamura2025] and showing that sub-additivity can occur only in the degenerate case of VaR additivity. Section [3](https://arxiv.org/html/2512.07787v1#S3 "3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") develops a new and unified characterization of VaR super-additivity that encompasses most existing results in the literature while allowing for non-identically distributed margins and a wider range of dependence structures. In Section [4](https://arxiv.org/html/2512.07787v1#S4 "4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), we generalize these results to random variables with arbitrary finite lower or upper endpoints. Section [5](https://arxiv.org/html/2512.07787v1#S5 "5 Conclusions ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") concludes the paper.

## 2 VaR Sub-additivity

VaR sub-additivity is widely regarded as a desirable property, as it reflects the risk-reducing effect of diversification. In pursuit of this property, numerous alternative risk measures have been introduced to guarantee it. The literature has examined VaR sub-additivity in various settings, including asymptotic regimes [Danielsson2013] and classes of distributions such as the elliptical distributions where VaR is known to be sub-additive for confidence levels p≥12p\geq\frac{\displaystyle 1}{\displaystyle 2} [McNeil2015]. Nevertheless, when we examine VaR sub-additivity for right-sided random variables, the conclusion turns out to be remarkably simple. As we show in the next theorem, VaR sub-additivity cannot occur in our setting except in the degenerate case of exact additivity. Before presenting this main result, we recall the notion of co-monotonicity, which represents the extremal form of positive dependence.

###### Definition 2.1.

A random vector 𝐗\bm{X} is co-monotonic if its joint CDF F𝐗F\_{\bm{X}} is the Fréchet upper bound

|  |  |  |
| --- | --- | --- |
|  | F𝑿​(x1,…,xn)=min⁡{FX1​(x1),…,FXn​(xn)}.F\_{\bm{X}}(x\_{1},\dots,x\_{n})=\min\left\{F\_{X\_{1}}(x\_{1}),\dots,F\_{X\_{n}}(x\_{n})\right\}. |  |

###### Theorem 2.2.

𝑿\bm{X} is VaR sub-additive if and only if 𝐗\bm{X} is VaR additive. In addition, 𝐗\bm{X} must be a co-monotonic vector.

###### Proof.

The reverse implication follows trivially from Definition  [1.1](https://arxiv.org/html/2512.07787v1#S1.Thmtheorem1 "Definition 1.1. ‣ 1 Introduction ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables").

For the ’only if’ implication, suppose that 𝑿\bm{X} is VaR sub-additive.
Fix any constant k>0k>0, and define the truncated random vector

|  |  |  |
| --- | --- | --- |
|  | 𝑿k=(X1,k,…,Xn,k),Xi,k≔dXi∣S≤k,i∈{1,…,n},\bm{X}\_{k}=(X\_{1,k},\dots,X\_{n,k}),\qquad X\_{i,k}\stackrel{{\scriptstyle d}}{{\coloneqq}}X\_{i}\mid S\leq k,\quad i\in\{1,\dots,n\}, |  |

and let

|  |  |  |
| --- | --- | --- |
|  | Sk≔d∑i=1nXi,k.S\_{k}\stackrel{{\scriptstyle d}}{{\coloneqq}}\sum\_{i=1}^{n}X\_{i,k}. |  |

The conditional variables Xi,kX\_{i,k} are well-defined since each XiX\_{i} has a zero lower endpoint and k>0k>0.
  
The CDFs of Xi,kX\_{i,k} and SkS\_{k} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | FXi,k​(xi)\displaystyle F\_{X\_{i,k}}(x\_{i}) | ={ℙ​(Xi≤xi,S≤k)FS​(k),xi<k,1,xi≥k,\displaystyle=\begin{cases}\dfrac{\mathbb{P}(X\_{i}\leq x\_{i},\,S\leq k)}{F\_{S}(k)},&x\_{i}<k,\\[8.50012pt] 1,&x\_{i}\geq k,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | FSk​(s)\displaystyle F\_{S\_{k}}(s) | ={FS​(s)FS​(k),s<k,1,s≥k.\displaystyle=\begin{cases}\dfrac{F\_{S}(s)}{F\_{S}(k)},&s<k,\\[4.25006pt] 1,&s\geq k.\end{cases} |  |

Next, define random variables (X~1,k,…,X~n,k)(\widetilde{X}\_{1,k},\dots,\widetilde{X}\_{n,k}) via

|  |  |  |  |
| --- | --- | --- | --- |
|  | FX~i,k​(xi)\displaystyle F\_{\widetilde{X}\_{i,k}}(x\_{i}) | ={FXi​(xi)FS​(k),xi<VaRFS​(k)​[Xi],1,xi≥VaRFS​(k)​[Xi].\displaystyle=\begin{cases}\dfrac{F\_{X\_{i}}(x\_{i})}{F\_{S}(k)},&x\_{i}<{\mathrm{VaR}}\_{F\_{S}(k)}[X\_{i}],\\[8.50012pt] 1,&x\_{i}\geq{\mathrm{VaR}}\_{F\_{S}(k)}[X\_{i}].\end{cases} |  |

For xi<VaRFS​(k)​[Xi]x\_{i}<{\mathrm{VaR}}\_{F\_{S}(k)}[X\_{i}], we have FXi​(xi)<FS​(k)≤FXi​(VaRFS​(k)​[Xi])F\_{X\_{i}}(x\_{i})<F\_{S}(k)\leq F\_{X\_{i}}({\mathrm{VaR}}\_{F\_{S}(k)}[X\_{i}]). Then the ratio FXi​(xi)FS​(k)\frac{\displaystyle F\_{X\_{i}}(x\_{i})}{\displaystyle F\_{S}(k)} is strictly less than 1, and xi<kx\_{i}<k, so the CDFs are well-defined.
  
From the definitions of FXi,kF\_{X\_{i,k}} and FX~i,kF\_{\widetilde{X}\_{i,k}}, we observe that

|  |  |  |
| --- | --- | --- |
|  | FXi,k​(xi)≤FX~i,k​(xi),∀xi∈[0,∞),F\_{X\_{i,k}}(x\_{i})\leq F\_{\widetilde{X}\_{i,k}}(x\_{i}),\qquad\forall x\_{i}\in[0,\infty), |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | VaRp​[X~i,k]=VaRp​FS​(k)​[Xi]≤VaRp​[Xi,k],∀p∈(0,1).{\mathrm{VaR}}\_{p}[\widetilde{X}\_{i,k}]={\mathrm{VaR}}\_{pF\_{S}(k)}[X\_{i}]\leq{\mathrm{VaR}}\_{p}[X\_{i,k}],\qquad\forall p\in(0,1). |  |

Similarly, by definition of FSkF\_{S\_{k}},

|  |  |  |
| --- | --- | --- |
|  | VaRp​[Sk]=VaRp​FS​(k)​[S],∀p∈(0,1).{\mathrm{VaR}}\_{p}[S\_{k}]={\mathrm{VaR}}\_{pF\_{S}(k)}[S],\qquad\forall p\in(0,1). |  |

  

Since 𝑿\bm{X} is VaR sub-additive,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRp​[Sk]=VaRp​FS​(k)​[S]\displaystyle{\mathrm{VaR}}\_{p}[S\_{k}]={\mathrm{VaR}}\_{pF\_{S}(k)}[S] | ≤∑i=1nVaRp​FS​(k)​[Xi]\displaystyle\leq\sum\_{i=1}^{n}{\mathrm{VaR}}\_{pF\_{S}(k)}[X\_{i}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i=1nVaRp​[Xi,k],\displaystyle\leq\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i,k}], |  |

and therefore,

|  |  |  |
| --- | --- | --- |
|  | VaRp​[Sk]≤∑i=1nVaRp​[Xi,k],∀p∈(0,1).{\mathrm{VaR}}\_{p}[S\_{k}]\leq\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i,k}],\qquad\forall p\in(0,1). |  |

Hence, 𝑿k\bm{X}\_{k} is also VaR sub-additive.

Since each Xi,kX\_{i,k} has a finite expectation (𝔼​[Xi,k]≤k<∞\mathbb{E}[X\_{i,k}]\leq k<\infty), Theorem 1 in [Imamura2025] implies that 𝑿k\bm{X}\_{k} is co-monotonic and consequently VaR additive i.e.:

|  |  |  |
| --- | --- | --- |
|  | F𝑿k​(x1,…,xn)=min⁡{FX1,k​(x1),…,FXn,k​(xn)},F\_{\bm{X}\_{k}}(x\_{1},\dots,x\_{n})=\min\{F\_{X\_{1,k}}(x\_{1}),\dots,F\_{X\_{n,k}}(x\_{n})\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | VaRp​[Sk]=∑i=1nVaRp​[Xi,k],∀p∈(0,1).{\mathrm{VaR}}\_{p}[S\_{k}]=\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i,k}],\qquad\forall p\in(0,1). |  |

Finally, by the monotone convergence of both the numerator
ℙ​(Xi≤xi,S≤k)\mathbb{P}(X\_{i}\leq x\_{i},S\leq k)
and denominator ℙ​(S≤k)\mathbb{P}(S\leq k), each marginal CDF satisfies

|  |  |  |
| --- | --- | --- |
|  | FXi,k​(xi)→FXi​(xi),as ​k→∞,F\_{X\_{i,k}}(x\_{i})\to F\_{X\_{i}}(x\_{i}),\qquad\text{as }k\to\infty, |  |

for every xi∈[0,∞)x\_{i}\in[0,\infty). Hence,

|  |  |  |
| --- | --- | --- |
|  | F𝑿k​(x1,…,xn)→F𝑿​(x1,…,xn),∀(x1,…,xn)∈[0,∞)n,F\_{\bm{X}\_{k}}(x\_{1},\dots,x\_{n})\to F\_{\bm{X}}(x\_{1},\dots,x\_{n}),\qquad\forall(x\_{1},\dots,x\_{n})\in[0,\infty)^{n}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | F𝑿​(x1,…,xn)=min⁡{FX1​(x1),…,FXn​(xn)}.F\_{\bm{X}}(x\_{1},\dots,x\_{n})=\min\{F\_{X\_{1}}(x\_{1}),\dots,F\_{X\_{n}}(x\_{n})\}. |  |

Thus, 𝑿\bm{X} is co-monotonic and VaR additive.
∎

Theorem [2.2](https://arxiv.org/html/2512.07787v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2 VaR Sub-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") extends and strengthens the main result of [Imamura2025], which relied on integrability assumptions. It reveals the rigid phenomenon of the impossibility of VaR sub-additivity for random variables supported on [0,∞)[0,\infty). The sub-additivity inequality is satisfied only in the degenerate case where VaR is exactly additive, and such additivity occurs exclusively under co-monotonicity.

## 3 VaR super-additivity

Unlike the sub-additivity property of VaR, the opposite effect -— VaR super-additivity -— can in fact arise. For instance, consider the case of a counter-monotonic random vector.

|  |  |  |
| --- | --- | --- |
|  | 𝑿=(X,1X),\bm{X}=\left(X,\frac{1}{X}\right), |  |

whose joint CDF is given by

|  |  |  |
| --- | --- | --- |
|  | F𝑿​(x1,x2)=max⁡{FX​(x1)+F1/X​(x2)−1, 0},F\_{\bm{X}}(x\_{1},x\_{2})=\max\{F\_{X}(x\_{1})+F\_{1/X}(x\_{2})-1,\,0\}, |  |

where XX follows a Type II Pareto distribution with CDF

|  |  |  |
| --- | --- | --- |
|  | FX​(x)=1−(θθ+x)α,x≥0,α,θ>0.F\_{X}(x)=1-\left(\frac{\theta}{\theta+x}\right)^{\alpha},\qquad x\geq 0,\;\alpha,\theta>0. |  |

For simplicity, take α=θ=1\alpha=\theta=1. The marginals are then identical Pareto(II) variables with

|  |  |  |
| --- | --- | --- |
|  | VaRp​[X]=p1−p.{\mathrm{VaR}}\_{p}[X]=\frac{p}{1-p}. |  |

A direct calculation shows that the VaR of the sum is

|  |  |  |
| --- | --- | --- |
|  | VaRp​[X+1/X]=2​(1+p2)1−p2.{\mathrm{VaR}}\_{p}[X+1/X]=\frac{2(1+p^{2})}{1-p^{2}}. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | 2​(1+p2)1−p2>2​p1−p,∀p∈(0,1),\frac{2(1+p^{2})}{1-p^{2}}>\frac{2p}{1-p},\qquad\forall\,p\in(0,1), |  |

the vector 𝑿\bm{X} is VaR super-additive. This example demonstrates that VaR super-additivity can appear naturally from a suitable choice of dependence and margins.
  
  
Although several studies have constructed families of distributions that exhibit tail-level VaR super-additivity [Embrechts2008, Embrechts2009b, Zhu2023], relatively few have examined this behavior across all probability levels pp. [Ibragimov2009] analyzed full-range super-additivity in i.i.d. stable distributions, and [Chen2025] introduced a class of random vectors with identically distributed, weakly negatively associated margins for which VaR is fully super-additive. The counter-monotonic vector presented above is a special case of this class. Taken together, these results show that VaR super-additivity is not a pathological anomaly but occurs naturally under economically meaningful and probabilistically coherent conditions.
  
  
Although not stated in this form, Theorem 1 of [Imamura2025] also implies a strong constraint on when super-additivity can happen. If all components XiX\_{i} are integrable i.e. 𝔼​[|Xi|]<∞\mathbb{E}[|X\_{i}|]<\infty, then VaR super-additivity is equivalent to VaR additivity. Consequently, to construct examples of random vectors
𝑿\bm{X} that are genuinely VaR super-additive, at least one of the components must be non-integrable. Our counter-monotonic example above shows this implication as the two Pareto II variables have infinite means. The converse, however, does not necessarily hold. Non-integrability is intrinsically a tail property and does not by itself guarantee full super-additivity. The following example illustrates this point.

###### Example 3.1.

Let 𝐗\bm{X} be a bivariate random vector.

* (1)

  Suppose 𝑿\bm{X} is counter-monotonic and defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑿=(X,11+X),\bm{X}=\left(X,\;\frac{1}{1+X}\right), |  |

  where XX follows a Pareto Type II distribution with unit scale and unit shape.
  Since

  |  |  |  |
  | --- | --- | --- |
  |  | 11+X∼Unif​(0,1),\frac{1}{1+X}\sim\mathrm{Unif}(0,1), |  |

  we obtain 𝔼​[11+X]=12\mathbb{E}\!\left[\frac{\displaystyle 1}{\displaystyle\mathstrut 1+X}\right]=\frac{\displaystyle 1}{\displaystyle 2}, while 𝔼​[X]=∞\mathbb{E}[X]=\infty for this Pareto distribution.

  The marginal VaR functions are therefore

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[X]=p1−p,VaRp​[11+X]=p.{\mathrm{VaR}}\_{p}[X]=\frac{p}{1-p},\qquad{\mathrm{VaR}}\_{p}\!\left[\frac{1}{1+X}\right]=p. |  |

  For the sum S=X+11+XS=X+\frac{\displaystyle 1}{\displaystyle\mathstrut 1+X}, one can show that

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[S]=p2−p+11−p.{\mathrm{VaR}}\_{p}[S]=\frac{p^{2}-p+1}{1-p}. |  |

  Comparing VaRp​[S]{\mathrm{VaR}}\_{p}[S] with VaRp​[X]+VaRp​[11+X]{\mathrm{VaR}}\_{p}[X]+{\mathrm{VaR}}\_{p}\!\left[\frac{\displaystyle 1}{\displaystyle\mathstrut 1+X}\right] reveals that VaR is super-additive for
  p∈(0,12],p\in\left(0,\frac{\displaystyle 1}{\displaystyle 2}\right],
  and sub-additive for
  p∈[12,1).p\in\left[\frac{\displaystyle 1}{\displaystyle 2},1\right).
* (2)

  Consider now a bivariate random vector 𝑿=(X1,X2)\bm{X}=(X\_{1},X\_{2}) with joint distribution function

  |  |  |  |
  | --- | --- | --- |
  |  | F𝑿​(x1,x2)=C​(FX1​(x1),FX2​(x2)),F\_{\bm{X}}(x\_{1},x\_{2})=C\!\left(F\_{X\_{1}}(x\_{1}),\,F\_{X\_{2}}(x\_{2})\right), |  |

  where FX1F\_{X\_{1}} and FX2F\_{X\_{2}} are Pareto (II) marginal distributions with parameters
  α1=α2=θ1=θ2=1\alpha\_{1}=\alpha\_{2}=\theta\_{1}=\theta\_{2}=1.
  The copula C​(u,v)C(u,v) is an Ordinal Sum copula (see Example 3.4 in [10.5555/1952073]) given by

  |  |  |  |
  | --- | --- | --- |
  |  | C​(u,v)={max⁡{u+v−12, 0},(u,v)∈[0,12]2,max⁡{u+v−1,12},(u,v)∈(12,1]2,min⁡{u,v},otherwise.C(u,v)=\begin{cases}\max\!\left\{u+v-\frac{\displaystyle 1}{\displaystyle 2},\,0\right\},&(u,v)\in\left[0,\frac{\displaystyle 1}{\displaystyle 2}\right]^{2},\\[5.10011pt] \max\!\left\{u+v-1,\,\frac{\displaystyle 1}{\displaystyle 2}\right\},&(u,v)\in\left(\frac{\displaystyle 1}{\displaystyle 2},1\right]^{2},\\[5.10011pt] \min\{u,v\},&\text{otherwise}.\end{cases} |  |

  ![Refer to caption](supportofC.png)


  Figure 1: Support of the Ordinal Sum copula C​(u,v)C(u,v) on the unit square [0,1]2[0,1]^{2}.

  Since both marginals are Pareto (II) with unit shape then their expectations are infinite. Their common VaR is

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[X1]=VaRp​[X2]=p1−p.{\mathrm{VaR}}\_{p}[X\_{1}]={\mathrm{VaR}}\_{p}[X\_{2}]=\frac{p}{1-p}. |  |

  For the sum S=X1+X2S=X\_{1}+X\_{2}, the VaR is piecewise and given by

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[S]={6+8​p2 9−4​p2,0<p≤12,2−2​p​(1−p)p​(1−p),12<p<1.{\mathrm{VaR}}\_{p}[S]=\begin{cases}\dfrac{6+8p^{2}}{\,9-4p^{2}\,},&0<p\leq\frac{\displaystyle 1}{\displaystyle 2},\\[6.80011pt] \dfrac{2-2p(1-p)}{p(1-p)},&\frac{\displaystyle 1}{\displaystyle 2}<p<1.\end{cases} |  |

  A direct comparison between VaRp​[S]{\mathrm{VaR}}\_{p}[S] and
  VaRp​[X1]+VaRp​[X2]{\mathrm{VaR}}\_{p}[X\_{1}]+{\mathrm{VaR}}\_{p}[X\_{2}] shows that VaRp​[S]{\mathrm{VaR}}\_{p}[S] is sub-additive whenever

  |  |  |  |
  | --- | --- | --- |
  |  | p∈[3−62,12],p\in\left[\frac{3-\sqrt{6}}{2},\,\frac{1}{2}\right], |  |

  and super-additive for all remaining values of pp.

Example [3.1](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem1 "Example 3.1. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") demonstrates that even in cases where we have
(1) counter-monotonic dependence with one non-integrable margin, and
(2) two non-counter-monotonic, non-integrable margins,
the resulting dependence-margin combination may still exhibit intervals of VaR sub-additivity. Thus, neither a particular dependence structure nor the mere non-integrability of margins is sufficient on its own to guarantee VaR super-additivity. In fact, the negative dependence used in part (2) of the example is significantly weaker than full counter-monotonicity.
  
  
This indicates that VaR super-additivity cannot be deduced from dependence alone, nor from marginal tail behavior in isolation. Rather, it requires analyzing how the joint distribution interacts with the full set of marginal distributions. It is this interaction that determines whether a given random vector
𝑿\bm{X} belongs to a class for which VaR is guaranteed to be super-additive.
  
Our objective, therefore, is to identify a dependence property together with a corresponding marginal behavior that, when combined, imply VaR super-additivity. Such a characterization must be sufficiently general to encompass all known results in the literature, yet specific enough to allow for straightforward verification.
  
  
Before presenting our main result, we introduce two key concepts.

###### Definition 3.2.

We say 𝐗\bm{X} is negative simplex dependent (NSD) if

|  |  |  |
| --- | --- | --- |
|  | FS​(t)≤∏i=1nFXi​(t),∀t∈[0,∞).F\_{S}(t)\leq\prod\_{i=1}^{n}F\_{X\_{i}}(t),\qquad\forall t\in[0,\infty). |  |

###### Definition 3.3.

A function Φ:[0,∞)n→(−∞,0]\Phi:[0,\infty)^{n}\to(-\infty,0] is called simplex dominant (SD) if

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)≥Φ​(s,…,s),s=∑i=1nxi,∀(x1,…,xn)∈[0,∞)n.\Phi(x\_{1},\dots,x\_{n})\geq\Phi(s,\dots,s),\qquad s=\sum\_{i=1}^{n}x\_{i},\quad\forall(x\_{1},\dots,x\_{n})\in[0,\infty)^{n}. |  |

###### Theorem 3.4.

If 𝐗\bm{X} is NSD with continuous FXiF\_{X\_{i}}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(x1,…,xn)=∑i=1nxi​log⁡FXi​(xi),\Phi(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}x\_{i}\log F\_{X\_{i}}(x\_{i}), |  | (3.1) |

is SD then 𝐗\bm{X} is VaR super-additive.

###### Proof.

Since FS​(VaRp​[S])≥pF\_{S}\left({\mathrm{VaR}}\_{p}[S]\right)\geq p, then VaR super-additivity is equivalent to showing that

|  |  |  |
| --- | --- | --- |
|  | p≥FS​(∑i=1nVaRp​[Xi]),∀p∈(0,1).p\;\geq\;F\_{S}\!\left(\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i}]\right),\qquad\forall p\in(0,1). |  |

For simplicity, let us use the notations

|  |  |  |
| --- | --- | --- |
|  | xi​(p):=VaRp​[Xi],s​(p):=∑i=1nxi​(p).x\_{i}(p):={\mathrm{VaR}}\_{p}[X\_{i}],\qquad s(p):=\sum\_{i=1}^{n}x\_{i}(p). |  |

First, since Φ\Phi is SD, setting each coordinate xix\_{i} to xi​(p)x\_{i}(p) yields

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1​(p),…,xn​(p))≥Φ​(s​(p),…,s​(p)),\Phi\bigl(x\_{1}(p),\dots,x\_{n}(p)\bigr)\;\geq\;\Phi\bigl(s(p),\dots,s(p)\bigr), |  |

hence

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nxi​(p)​log⁡FXi​(xi​(p))≥s​(p)​∑i=1nlog⁡FXi​(s​(p)).\sum\_{i=1}^{n}x\_{i}(p)\log F\_{X\_{i}}(x\_{i}(p))\;\geq\;s(p)\sum\_{i=1}^{n}\log F\_{X\_{i}}(s(p)). |  |

Second, because each FXiF\_{X\_{i}} is continuous, we have FXi​(xi​(p))=pF\_{X\_{i}}(x\_{i}(p))=p, and therefore

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nxi​(p)​log⁡p≥s​(p)​∑i=1nlog⁡FXi​(s​(p)),\sum\_{i=1}^{n}x\_{i}(p)\log p\;\geq\;s(p)\sum\_{i=1}^{n}\log F\_{X\_{i}}(s(p)), |  |

|  |  |  |
| --- | --- | --- |
|  | ⟹s​(p)​log⁡p≥s​(p)​∑i=1nlog⁡FXi​(s​(p)).\implies s(p)\log p\;\geq\;s(p)\sum\_{i=1}^{n}\log F\_{X\_{i}}(s(p)). |  |

Given we have s​(p)>0s(p)>0, dividing by s​(p)s(p) yields

|  |  |  |
| --- | --- | --- |
|  | log⁡p≥∑i=1nlog⁡FXi​(s​(p)).\log p\;\geq\;\sum\_{i=1}^{n}\log F\_{X\_{i}}(s(p)). |  |

Exponentiating gives

|  |  |  |
| --- | --- | --- |
|  | p≥∏i=1nFXi​(s​(p)).p\;\geq\;\prod\_{i=1}^{n}F\_{X\_{i}}(s(p)). |  |

Finally, for NSD vectors, the joint distribution satisfies

|  |  |  |
| --- | --- | --- |
|  | FS​(t)≤∏i=1nFXi​(t),∀t∈[0,∞).F\_{S}(t)\;\leq\;\prod\_{i=1}^{n}F\_{X\_{i}}(t),\qquad\forall t\in[0,\infty). |  |

Thus at t=s​(p)t=s(p),

|  |  |  |
| --- | --- | --- |
|  | ∏i=1nFXi​(s​(p))≥FS​(s​(p)).\prod\_{i=1}^{n}F\_{X\_{i}}(s(p))\;\geq\;F\_{S}(s(p)). |  |

Combining with the previous inequality gives

|  |  |  |
| --- | --- | --- |
|  | p≥∏i=1nFXi​(s​(p))≥FS​(s​(p))=FS​(∑i=1nVaRp​[Xi]),∀p∈(0,1),p\;\geq\;\prod\_{i=1}^{n}F\_{X\_{i}}(s(p))\;\geq\;F\_{S}(s(p))\;=\;F\_{S}\!\left(\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i}]\right),\qquad\forall p\in(0,1), |  |

i.e.

|  |  |  |
| --- | --- | --- |
|  | p≥FS​(∑i=1nVaRp​[Xi]),∀p∈(0,1),p\;\geq\;F\_{S}\!\left(\sum\_{i=1}^{n}{\mathrm{VaR}}\_{p}[X\_{i}]\right),\qquad\forall p\in(0,1), |  |

which is precisely VaR super-additivity. This completes the proof.
∎

The strength of Theorem [3.4](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") lies in its ability to encompass a broad class of dependence structures while permitting considerable flexibility in the choice of marginal distributions, which need not be identical.
  
The following two propositions provide sufficient conditions for establishing the NSD and SD properties.

###### Proposition 3.5.

When 𝐗\bm{X} is negative lower orthant dependent (NLOD) [Block1982a, Joe1997], that is

|  |  |  |
| --- | --- | --- |
|  | F𝑿​(x1,…,xn)≤∏i=1nFXi​(xi),∀(x1,…,xn)∈[0,∞)n,F\_{\bm{X}}(x\_{1},\dots,x\_{n})\leq\prod\_{i=1}^{n}F\_{X\_{i}}(x\_{i}),\ \forall(x\_{1},\dots,x\_{n})\in[0,\infty)^{n}, |  |

then 𝐗\bm{X} is NSD.

###### Proof.

The result can be easily deduced since the nn-simplex lies inside the nn-cube (as a corner of the nn-cube) which gives

|  |  |  |
| --- | --- | --- |
|  | FS​(t)≤F𝑿​(t,…,t)≤∏i=1nFXi​(t),∀t∈[0,∞).F\_{S}(t)\leq F\_{\bm{X}}(t,\dots,t)\leq\prod\_{i=1}^{n}F\_{X\_{i}}(t),\ \forall t\in[0,\infty). |  |

In fact, to be NSD, 𝑿\bm{X} need only be NLOD along the diagonal (t,…,t),t∈[0,∞)(t,\dots,t),\ t\in[0,\infty), and not necessarily everywhere.
∎

###### Proposition 3.6.

If Φ\Phi is non-increasing in the sense that

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)≥Φ​(y1,…,yn)​whenever ​xi<yi​ for all ​i∈{1,…,n},\Phi(x\_{1},\dots,x\_{n})\geq\Phi(y\_{1},\dots,y\_{n})\quad\text{whenever }x\_{i}<y\_{i}\text{ for all }i\in\{1,\dots,n\}, |  |

then Φ\Phi is SD. Moreover, suppose each ϕi\phi\_{i} is continuous and

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)=∑i=1nϕi​(xi).\Phi(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}\phi\_{i}(x\_{i}). |  |

Then Φ\Phi is non-increasing if and only if each ϕi\phi\_{i} is non-increasing. Consequently, if all ϕi\phi\_{i} are non-increasing then Φ\Phi is SD.

###### Proof.

First part. Fix (x1,…,xn)∈[0,∞)n(x\_{1},\dots,x\_{n})\in[0,\infty)^{n} and set

|  |  |  |
| --- | --- | --- |
|  | y1=⋯=yn=s:=∑i=1nxi.y\_{1}=\dots=y\_{n}=s:=\sum\_{i=1}^{n}x\_{i}. |  |

Since xi<sx\_{i}<s for all ii, the non-increasing property implies

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)≥Φ​(y1,…,yn)=Φ​(s,…,s),\Phi(x\_{1},\dots,x\_{n})\geq\Phi(y\_{1},\dots,y\_{n})=\Phi(s,\dots,s), |  |

and therefore Φ\Phi is SD.
  
Second part. Assume Φ\Phi can be written as

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)=∑i=1nϕi​(xi),\Phi(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}\phi\_{i}(x\_{i}), |  |

with each ϕi\phi\_{i} continuous. If every ϕ\phi is non-increasing then the sum of non-increasing functions is non-increasing i.e. Φ\Phi is non-increasing.
  
Conversely, suppose that Φ\Phi is non-increasing, but for contradiction, some coordinate function ϕj\phi\_{j} is not non-increasing i.e. there exists xj∗<yj∗x^{\*}\_{j}<y^{\*}\_{j} such that ϕj​(xj∗)<ϕj​(yj∗)\phi\_{j}(x^{\*}\_{j})<\phi\_{j}(y^{\*}\_{j}) for some j∈{1,…,n}j\in\{1,\dots,n\}. Set ϵ=ϕj​(yj∗)−ϕj​(xj∗)>0\epsilon=\phi\_{j}(y^{\*}\_{j})-\phi\_{j}(x^{\*}\_{j})>0 and by continuity of each ϕi\phi\_{i}, i≠ji\neq j, there exists δi\delta\_{i} such that |ϕi​(yi)−ϕi​(xi)|<ϵn|\phi\_{i}(y\_{i})-\phi\_{i}(x\_{i})|<\frac{\displaystyle\epsilon}{\displaystyle n} whenever |yi−xi|<δi|y\_{i}-x\_{i}|<\delta\_{i}. From the continuity domain of each ϕi\phi\_{i}, pick xi∗<yi∗x^{\*}\_{i}<y^{\*}\_{i} such that |yi∗−xi∗|<δi|y^{\*}\_{i}-x^{\*}\_{i}|<\delta\_{i}, then for all those xi∗<yi∗x^{\*}\_{i}<y^{\*}\_{i} together with xj∗<yj∗x^{\*}\_{j}<y^{\*}\_{j},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(y1∗,…,yn∗)−Φ​(x1∗,…,xn∗)\displaystyle\Phi(y^{\*}\_{1},\dots,y^{\*}\_{n})-\Phi(x^{\*}\_{1},\dots,x^{\*}\_{n}) | =∑i=1n(ϕi​(yi∗)−ϕi​(xi∗)),\displaystyle=\sum\_{i=1}^{n}\left(\phi\_{i}(y^{\*}\_{i})-\phi\_{i}(x^{\*}\_{i})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϵ+∑i≠j(ϕi​(yi∗)−ϕi​(xi∗)),\displaystyle=\epsilon+\sum\_{i\neq j}\left(\phi\_{i}(y^{\*}\_{i})-\phi\_{i}(x^{\*}\_{i})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >ϵ−∑i≠jϵn,\displaystyle>\epsilon-\sum\_{i\neq j}\frac{\displaystyle\epsilon}{\displaystyle n}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϵn,\displaystyle=\frac{\displaystyle\epsilon}{\displaystyle n}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >0.\displaystyle>0. |  |

i.e. Φ\Phi is not non-increasing, leading to a contradiction. Hence each ϕi\phi\_{i} must be non-increasing. Consequently, by the first part of the proof, Φ\Phi is SD whenever all ϕi\phi\_{i} are non-increasing.
∎

###### Corollary 3.7.

If 𝐗\bm{X} is NLOD with continuous FXiF\_{X\_{i}}, and each ϕi​(xi)=xi​log⁡FXi​(xi)\phi\_{i}(x\_{i})=x\_{i}\log F\_{X\_{i}}(x\_{i}) in Equation ([3.1](https://arxiv.org/html/2512.07787v1#S3.E1 "In Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is non-increasing, then 𝐗\bm{X} is VaR super-additive.

The NSD property captures the dependence requirement on the joint distribution of 𝑿\bm{X} that ensures VaR super-additivity. We note, in passing, that the dependence structure used in part (2) of Example [3.1](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem1 "Example 3.1. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") is weaker than NSD, specifically it fails the NSD property at t∈(710,1+2)t\in\left(\frac{\displaystyle 7}{\displaystyle\mathstrut 10},1+\sqrt{2}\right). This contributed, though was not strictly required, to the failure of VaR super-additivity in that example. Nonetheless, by definition, NSD is a relatively weak form of negative dependence and is strictly implied by NLOD.
  
Below we provide an example of a VaR super-additive random vector 𝑿\bm{X} that satisfies NSD but not NLOD.

###### Example 3.8.

Consider the random vector

|  |  |  |
| --- | --- | --- |
|  | 𝑿=(X,X,1X),\bm{X}=\left(X,\,X,\,\frac{1}{X}\right), |  |

where XX follows a unit-scale, unit-shape Pareto II distribution.
Its joint distribution function is

|  |  |  |
| --- | --- | --- |
|  | F𝑿​(x1,x2,x3)={0,1x3≥min⁡{x1,x2},x31+x3−11+min⁡{x1,x2},1x3<min⁡{x1,x2}.F\_{\bm{X}}(x\_{1},x\_{2},x\_{3})=\begin{cases}0,&\displaystyle\frac{1}{x\_{3}}\geq\min\{x\_{1},x\_{2}\},\\[6.0pt] \displaystyle\frac{x\_{3}}{1+x\_{3}}-\frac{1}{1+\min\{x\_{1},x\_{2}\}},&\displaystyle\frac{1}{x\_{3}}<\min\{x\_{1},x\_{2}\}.\end{cases} |  |

The distribution of the sum S=X+X+1/XS=X+X+1/X may be computed explicitly:

|  |  |  |
| --- | --- | --- |
|  | FS​(s)={0,s≤2​2,s2−8s+3,s>2​2.F\_{S}(s)=\begin{cases}0,&s\leq 2\sqrt{2},\\[4.0pt] \displaystyle\frac{\sqrt{s^{2}-8}}{\,s+3\,},&s>2\sqrt{2}.\end{cases} |  |

Each marginal distribution is identical:

|  |  |  |
| --- | --- | --- |
|  | FX​(x)=1−11+x,x≥0.F\_{X}(x)=1-\frac{1}{1+x},\qquad x\geq 0. |  |

To verify that 𝐗\bm{X} is NSD, observe first that for 0≤t≤2​20\leq t\leq 2\sqrt{2},

|  |  |  |
| --- | --- | --- |
|  | FS​(t)=0≤(t1+t)3=FX​(t)3.F\_{S}(t)=0\leq\left(\frac{t}{1+t}\right)^{3}=F\_{X}(t)^{3}. |  |

For t>2​2t>2\sqrt{2}, one checks analytically that

|  |  |  |
| --- | --- | --- |
|  | FS​(t)=t2−8t+3<(t1+t)3=FX​(t)3.F\_{S}(t)=\frac{\sqrt{t^{2}-8}}{t+3}\;<\;\left(\frac{t}{1+t}\right)^{3}=F\_{X}(t)^{3}. |  |

Thus FS​(t)≤FX​(t)3F\_{S}(t)\leq F\_{X}(t)^{3} for all t≥0t\geq 0, proving that 𝐗\bm{X} is NSD.
  
Next we show that 𝐗\bm{X} is not NLOD. For t>1t>1,

|  |  |  |
| --- | --- | --- |
|  | F𝑿​(t,t,t)−FX​(t)3=t−11+t−t3(1+t)3=t2−t−1(1+t)3.F\_{\bm{X}}(t,t,t)-F\_{X}(t)^{3}=\frac{t-1}{1+t}-\frac{t^{3}}{(1+t)^{3}}=\frac{t^{2}-t-1}{(1+t)^{3}}. |  |

A simple algebraic check shows that t2−t−1≥0t^{2}-t-1\geq 0 whenever

|  |  |  |
| --- | --- | --- |
|  | t≥5+12.t\geq\frac{\sqrt{5}+1}{2}. |  |

Hence F𝐗​(t,t,t)≥FX​(t)3F\_{\bm{X}}(t,t,t)\geq F\_{X}(t)^{3} for all such tt, implying that 𝐗\bm{X} fails to be NLOD, even along the diagonal.
  
We now compare the associated VaRs. The marginal VaRs are

|  |  |  |
| --- | --- | --- |
|  | VaRp​[X]=p1−p,{\mathrm{VaR}}\_{p}[X]=\frac{p}{1-p}, |  |

whereas for the sum we have

|  |  |  |
| --- | --- | --- |
|  | VaRp​[S]=3​p2+p2+8 1−p2.{\mathrm{VaR}}\_{p}[S]=\frac{3p^{2}+\sqrt{p^{2}+8}}{\,1-p^{2}\,}. |  |

A direct algebraic comparison yields

|  |  |  |
| --- | --- | --- |
|  | VaRp​[S]=3​p2+p2+81−p2>3​p1−p=3​VaRp​[X],∀p∈(0,1),{\mathrm{VaR}}\_{p}[S]=\frac{3p^{2}+\sqrt{p^{2}+8}}{1-p^{2}}\;>\;\frac{3p}{1-p}=3\,{\mathrm{VaR}}\_{p}[X],\quad\forall p\in(0,1), |  |

so 𝐗\bm{X} is VaR super-additive.
  
This conclusion is an immediate consequence of Theorem [3.4](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"): we have already shown that 𝐗\bm{X} is NSD, and for the chosen unit-shape Pareto margins the functions ϕi​(xi)=xi​log⁡FXi​(xi)\phi\_{i}(x\_{i})=x\_{i}\log F\_{X\_{i}}(x\_{i}) in Equation ([3.1](https://arxiv.org/html/2512.07787v1#S3.E1 "In Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) are non-increasing (as will be demonstrated in Example [3.9](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem9 "Example 3.9. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) and consequently SD by Proposition [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables").

The second part of Theorem [3.4](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") imposes structural conditions on the marginal distributions by specifying the behaviour of the function Φ\Phi in Equation ([3.1](https://arxiv.org/html/2512.07787v1#S3.E1 "In Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")).
In practice, the SD property may not be straightforward to verify, so it is useful to rely on the non-increasing criteria. Applying the condition of Proposition [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") to the function Φ\Phi in Equation ([3.1](https://arxiv.org/html/2512.07787v1#S3.E1 "In Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")), i.e.

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)=∑i=1nϕi​(xi),where​ϕi​(xi)=xi​log⁡FXi​(xi),\Phi(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}\phi\_{i}(x\_{i}),\quad\mathrm{where}\quad\phi\_{i}(x\_{i})=x\_{i}\log F\_{X\_{i}}(x\_{i}), |  |

it suffices to verify that each ϕi​(xi)\phi\_{i}(x\_{i}) is non-increasing on [0,∞)[0,\infty). This is convenient, as it reduces the verification of SD to checking each margin separately. The following example gives instances of marginal distributions for which the non-increasing property holds.

###### Example 3.9.

We present below several standard continuous distribution functions FXiF\_{X\_{i}} for which the non-increasing property of ϕi\phi\_{i} holds.

* (1)

  Fréchet distribution.
  The CDF is

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=exp⁡(−(xiθi)−αi),xi≥0,αi,θi>0,F\_{X\_{i}}(x\_{i})=\exp\left(-\left(\frac{\displaystyle x\_{i}}{\displaystyle\theta\_{i}}\right)^{-\alpha\_{i}}\right),\qquad x\_{i}\geq 0,\ \alpha\_{i},\theta\_{i}>0, |  |

  which yields

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕi​(xi)\displaystyle\phi\_{i}(x\_{i}) | =−xi​(xiθi)−αi\displaystyle=-x\_{i}\left(\frac{x\_{i}}{\theta\_{i}}\right)^{-\alpha\_{i}} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =−θiαi​xi 1−αi.\displaystyle=-\theta\_{i}^{\alpha\_{i}}x\_{i}^{\,1-\alpha\_{i}}. |  |

  This function is non-increasing precisely when 0<αi≤10<\alpha\_{i}\leq 1.
* (2)

  Pareto(II)/Lomax distribution.
  Here

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=1−(θiθi+xi)αi,xi≥0,αi,θi>0,F\_{X\_{i}}(x\_{i})=1-\left(\frac{\displaystyle\theta\_{i}}{\displaystyle\theta\_{i}+x\_{i}}\right)^{\alpha\_{i}},\qquad x\_{i}\geq 0,\ \alpha\_{i},\theta\_{i}>0, |  |

  and thus

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi​(xi)=xi​log⁡(1−(θiθi+xi)αi).\phi\_{i}(x\_{i})=x\_{i}\log\!\left(1-\left(\frac{\displaystyle\theta\_{i}}{\displaystyle\theta\_{i}+x\_{i}}\right)^{\alpha\_{i}}\right). |  |

  The derivative becomes

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕi′​(xi)\displaystyle\phi\_{i}^{{}^{\prime}}(x\_{i}) | =log⁡FXi​(xi)+xi​fXi​(xi)FXi​(xi)\displaystyle=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle x\_{i}f\_{X\_{i}}(x\_{i})}{\displaystyle F\_{X\_{i}}(x\_{i})} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =log⁡FXi​(xi)+αi​xi​F¯Xi​(xi)(θi+xi)​FXi​(xi).\displaystyle=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle\alpha\_{i}x\_{i}\overline{F}\_{X\_{i}}(x\_{i})}{\displaystyle(\theta\_{i}+x\_{i})F\_{X\_{i}}(x\_{i})}. |  |

  Claim. ϕi′​(xi)≤0\phi\_{i}^{{}^{\prime}}(x\_{i})\leq 0 for all xi∈[0,∞)x\_{i}\in[0,\infty) if and only if 0<αi≤10<\alpha\_{i}\leq 1.

  *Necessity.*
  Assume ϕi′​(xi)≤0\phi\_{i}^{{}^{\prime}}(x\_{i})\leq 0 on [0,∞)[0,\infty), and suppose αi>1\alpha\_{i}>1.
  Consider

  |  |  |  |
  | --- | --- | --- |
  |  | limxi→∞ϕi′​(xi)F¯Xi​(xi)=αi−1.\lim\_{x\_{i}\to\infty}\frac{\displaystyle\phi\_{i}^{{}^{\prime}}(x\_{i})}{\displaystyle\overline{F}\_{X\_{i}}(x\_{i})}=\alpha\_{i}-1. |  |

  Since αi>1\alpha\_{i}>1, the ratio becomes positive for sufficiently large xix\_{i}, contradicting the non-positivity of ϕi′\phi\_{i}^{{}^{\prime}}.
  Thus, necessarily 0<αi≤10<\alpha\_{i}\leq 1.

  *Sufficiency.*
  Assume 0<αi≤10<\alpha\_{i}\leq 1.
  Rewrite the derivative as

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕi′​(xi)\displaystyle\phi\_{i}^{{}^{\prime}}(x\_{i}) | =−∫FXi​(xi)11w​dw+αi​xi(θi+xi)​FXi​(xi)​∫FXi​(xi)1dw\displaystyle=-\int\_{F\_{X\_{i}}(x\_{i})}^{1}\frac{\displaystyle 1}{\displaystyle w}\,\mathrm{d}w+\frac{\displaystyle\alpha\_{i}x\_{i}}{\displaystyle(\theta\_{i}+x\_{i})F\_{X\_{i}}(x\_{i})}\int\_{F\_{X\_{i}}(x\_{i})}^{1}\mathrm{d}w |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =−∫FXi​(xi)1(θi+xi)​FXi​(xi)−αi​xi​ww​(θi+xi)​FXi​(xi)​dw.\displaystyle=-\int\_{F\_{X\_{i}}(x\_{i})}^{1}\frac{\displaystyle(\theta\_{i}+x\_{i})F\_{X\_{i}}(x\_{i})-\alpha\_{i}x\_{i}w}{\displaystyle w(\theta\_{i}+x\_{i})F\_{X\_{i}}(x\_{i})}\,\mathrm{d}w. |  |

  Since FXi​(xi)≤w≤1F\_{X\_{i}}(x\_{i})\leq w\leq 1, a sufficient condition for the integrand to be non-negative is

  |  |  |  |
  | --- | --- | --- |
  |  | (θi+xi)​FXi​(xi)−αi​xi≥0.(\theta\_{i}+x\_{i})F\_{X\_{i}}(x\_{i})-\alpha\_{i}x\_{i}\geq 0. |  |

  Applying the mean value theorem to t↦tαit\mapsto t^{\alpha\_{i}} on
  [θiθi+xi,1]\left[\frac{\displaystyle\theta\_{i}}{\displaystyle\theta\_{i}+x\_{i}},1\right] yields the inequality and thus the desired non-positivity.

  Therefore, ϕi\phi\_{i} is non-increasing if and only if 0<αi≤10<\alpha\_{i}\leq 1.
* (3)

  Lévy distribution.
  With

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=erfc​(θi2​xi),xi≥0,θi>0,F\_{X\_{i}}(x\_{i})=\mathrm{erfc}\!\left(\sqrt{\frac{\theta\_{i}}{2x\_{i}}}\right),\qquad x\_{i}\geq 0,\ \theta\_{i}>0, |  |

  define

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi​(xi)=xi​log⁡(erfc​(θi2​xi)).\phi\_{i}(x\_{i})=x\_{i}\log\!\left(\mathrm{erfc}\!\left(\sqrt{\frac{\theta\_{i}}{2x\_{i}}}\right)\right). |  |

  Differentiating gives

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi′​(xi)=log⁡(erfc​(θi2​xi))+θi2​π​xi​exp⁡(−θi2​xi)erfc​(θi2​xi).\phi\_{i}^{\prime}(x\_{i})=\log\!\left(\mathrm{erfc}\!\left(\sqrt{\frac{\theta\_{i}}{2x\_{i}}}\right)\right)+\frac{\sqrt{\frac{\displaystyle\theta\_{i}}{\displaystyle 2\pi x\_{i}}}\exp\!\left(-\frac{\displaystyle\theta\_{i}}{\displaystyle 2x\_{i}}\right)}{\mathrm{erfc}\!\left(\sqrt{\frac{\displaystyle\theta\_{i}}{\displaystyle 2x\_{i}}}\right)}. |  |

  Let t=θi2​xit=\sqrt{\frac{\displaystyle\theta\_{i}}{\displaystyle 2x\_{i}}}.
  Then ϕi′​(xi)≤0\phi\_{i}^{\prime}(x\_{i})\leq 0 is equivalent to ψi​(t)≤0\psi\_{i}(t)\leq 0, where

  |  |  |  |
  | --- | --- | --- |
  |  | ψi​(t)=log⁡(erfc​(t))+t​exp⁡(−t2)π​erfc​(t).\psi\_{i}(t)=\log(\mathrm{erfc}(t))+\frac{t\exp(-t^{2})}{\sqrt{\pi}\,\mathrm{erfc}(t)}. |  |

  Since

  |  |  |  |
  | --- | --- | --- |
  |  | limt→0+ψi​(t)=0,limt→∞ψi​(t)=−∞,\lim\_{t\to 0^{+}}\psi\_{i}(t)=0,\qquad\lim\_{t\to\infty}\psi\_{i}(t)=-\infty, |  |

  it suffices to show ψi′​(t)≤0\psi\_{i}^{\prime}(t)\leq 0.
  Differentiation leads to

  |  |  |  |
  | --- | --- | --- |
  |  | ψi′​(t)=exp⁡(−2​t2)​(2​t−π​exp⁡(t2)​(2​t2+1)​erfc​(t))π​erfc​(t)2,\psi\_{i}^{\prime}(t)=\frac{\exp(-2t^{2})\left(2t-\sqrt{\pi}\,\exp(t^{2})(2t^{2}+1)\mathrm{erfc}(t)\right)}{\pi\,\mathrm{erfc}(t)^{2}}, |  |

  which is non-positive whenever

  |  |  |  |
  | --- | --- | --- |
  |  | 2​t​exp⁡(−t2)π​(2​t2+1)≤erfc​(t),\frac{2t\exp(-t^{2})}{\sqrt{\pi}(2t^{2}+1)}\leq\mathrm{erfc}(t), |  |

  the classical Mills ratio bound [Mills1926].
  Thus ϕi′​(xi)≤0\phi\_{i}^{\prime}(x\_{i})\leq 0 for all xi≥0x\_{i}\geq 0.
* (4)

  One-parameter Beta Prime distribution.
  With

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=(xi1+xi)αi,xi≥0,αi>0,F\_{X\_{i}}(x\_{i})=\left(\frac{\displaystyle x\_{i}}{\displaystyle 1+x\_{i}}\right)^{\alpha\_{i}},\qquad x\_{i}\geq 0,\ \alpha\_{i}>0, |  |

  we have

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi​(xi)=αi​xi​log⁡(xi1+xi).\phi\_{i}(x\_{i})=\alpha\_{i}x\_{i}\log\!\left(\frac{\displaystyle x\_{i}}{\displaystyle 1+x\_{i}}\right). |  |

  Differentiation gives

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕi′​(xi)\displaystyle\phi\_{i}^{\prime}(x\_{i}) | =αi​(log⁡(xi1+xi)+11+xi)\displaystyle=\alpha\_{i}\left(\log\!\left(\frac{\displaystyle x\_{i}}{\displaystyle 1+x\_{i}}\right)+\frac{\displaystyle 1}{\displaystyle 1+x\_{i}}\right) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =αi​(−∑k=1∞1k​(11+xi)k+11+xi)\displaystyle=\alpha\_{i}\left(-\sum\_{k=1}^{\infty}\frac{1}{k}\left(\frac{1}{1+x\_{i}}\right)^{k}+\frac{\displaystyle 1}{\displaystyle 1+x\_{i}}\right) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤αi​(−11+xi+11+xi)=0.\displaystyle\leq\alpha\_{i}\left(-\frac{1}{1+x\_{i}}+\frac{\displaystyle 1}{\displaystyle 1+x\_{i}}\right)=0. |  |

  Hence ϕi\phi\_{i} is non-increasing for all αi>0\alpha\_{i}>0.
* (5)

  Log-hazard distribution.
  If

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=exp⁡{−log(1+xi)αixi},xi≥0,αi∈(−∞,1),F\_{X\_{i}}(x\_{i})=\exp\!\left\{-\frac{\displaystyle\log(1+x\_{i})^{\alpha\_{i}}}{\displaystyle x\_{i}}\right\},\qquad x\_{i}\geq 0,\ \alpha\_{i}\in(-\infty,1), |  |

  then

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi(xi)=−log(1+xi)αi.\phi\_{i}(x\_{i})=-\log(1+x\_{i})^{\alpha\_{i}}. |  |

  This is non-increasing whenever log(1+xi)αi\log(1+x\_{i})^{\alpha\_{i}} is non-decreasing, which occurs exactly when 0≤αi<10\leq\alpha\_{i}<1.
* (6)

  Log-Cauchy distribution.
  The CDF is

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=12+1π​arctan⁡(αi​log⁡(xi)),xi≥0,αi>0.F\_{X\_{i}}(x\_{i})=\frac{\displaystyle 1}{\displaystyle 2}+\frac{\displaystyle 1}{\displaystyle\pi}\arctan(\alpha\_{i}\log(x\_{i})),\qquad x\_{i}\geq 0,\ \alpha\_{i}>0. |  |

  Hence

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi​(xi)=xi​log⁡(12+1π​arctan⁡(αi​log⁡(xi))).\phi\_{i}(x\_{i})=x\_{i}\log\!\left(\frac{\displaystyle 1}{\displaystyle 2}+\frac{\displaystyle 1}{\displaystyle\pi}\arctan(\alpha\_{i}\log(x\_{i}))\right). |  |

  Differentiation yields

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi′​(xi)=log⁡FXi​(xi)+αiπ​(1+(αi​log⁡(xi))2)​FXi​(xi).\phi\_{i}^{\prime}(x\_{i})=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle\alpha\_{i}}{\displaystyle\pi(1+(\alpha\_{i}\log(x\_{i}))^{2})\,F\_{X\_{i}}(x\_{i})}. |  |

  Introducing θ=arctan⁡(αi​log⁡(xi))\theta=\arctan(\alpha\_{i}\log(x\_{i})) gives

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi′​(xi)=log⁡FXi​(xi)+αi​cos2⁡θπ​FXi​(xi)=log⁡FXi​(xi)+αi​sin2⁡(π​FXi​(xi))π​FXi​(xi).\phi\_{i}^{\prime}(x\_{i})=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle\alpha\_{i}\cos^{2}\theta}{\displaystyle\pi F\_{X\_{i}}(x\_{i})}=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle\alpha\_{i}\sin^{2}(\pi F\_{X\_{i}}(x\_{i}))}{\displaystyle\pi F\_{X\_{i}}(x\_{i})}. |  |

  To test non-positivity, define

  |  |  |  |
  | --- | --- | --- |
  |  | ψi​(u)=log⁡(u)+αi​sin2⁡(π​u)π​u,u∈[0,1].\psi\_{i}(u)=\log(u)+\frac{\displaystyle\alpha\_{i}\sin^{2}(\pi u)}{\displaystyle\pi u},\qquad u\in[0,1]. |  |

  Then ϕi′​(xi)≤0\phi\_{i}^{\prime}(x\_{i})\leq 0 holds for all xi≥0x\_{i}\geq 0 precisely when ψi​(u)≤0\psi\_{i}(u)\leq 0, ∀u∈[0,1]\forall u\in[0,1] or equivalently when

  |  |  |  |
  | --- | --- | --- |
  |  | 0<αi≤infu∈[0,1]−π​u​log⁡(u)sin2⁡(π​u)≈1.0568.0<\alpha\_{i}\leq\inf\_{u\in[0,1]}\frac{\displaystyle-\pi u\log(u)}{\displaystyle\sin^{2}(\pi u)}\approx 1.0568. |  |
* (7)

  Inverse-Gamma distribution.
  The CDF can be written as

  |  |  |  |
  | --- | --- | --- |
  |  | FXi​(xi)=1Γ​(αi)​Γ​(αi,θixi),xi≥0,αi,θi>0,F\_{X\_{i}}(x\_{i})=\frac{1}{\Gamma(\alpha\_{i})}\Gamma\!\left(\alpha\_{i},\frac{\displaystyle\theta\_{i}}{\displaystyle x\_{i}}\right),\qquad x\_{i}\geq 0,\ \alpha\_{i},\theta\_{i}>0, |  |

  leading to

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi​(xi)=xi​log⁡(1Γ​(αi)​Γ​(αi,θixi)).\phi\_{i}(x\_{i})=x\_{i}\log\!\left(\frac{1}{\Gamma(\alpha\_{i})}\Gamma(\alpha\_{i},\tfrac{\theta\_{i}}{x\_{i}})\right). |  |

  Differentiation gives

  |  |  |  |
  | --- | --- | --- |
  |  | ϕi′​(xi)=log⁡FXi​(xi)+(θixi)αi​exp⁡(−θi/xi)Γ​(αi)​FXi​(xi).\phi\_{i}^{\prime}(x\_{i})=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle\left(\frac{\displaystyle\theta\_{i}}{\displaystyle x\_{i}}\right)^{\alpha\_{i}}\exp(-\theta\_{i}/x\_{i})}{\displaystyle\Gamma(\alpha\_{i})\,F\_{X\_{i}}(x\_{i})}. |  |

  Let t=θi/xit=\theta\_{i}/x\_{i}.
  Then ϕi′​(xi)≤0\phi\_{i}^{\prime}(x\_{i})\leq 0 is equivalent to ψi​(t)≤0\psi\_{i}(t)\leq 0, where

  |  |  |  |
  | --- | --- | --- |
  |  | ψi​(t)=log⁡(1Γ​(αi)​Γ​(αi,t))+tαi​exp⁡(−t)Γ​(αi,t).\psi\_{i}(t)=\log\!\left(\frac{1}{\Gamma(\alpha\_{i})}\Gamma(\alpha\_{i},t)\right)+\frac{\displaystyle t^{\alpha\_{i}}\exp(-t)}{\displaystyle\Gamma(\alpha\_{i},t)}. |  |

  Claim. ψi​(t)≤0\psi\_{i}(t)\leq 0 for all t≥0t\geq 0 if and only if 0<αi≤10<\alpha\_{i}\leq 1.

  *Necessity.*
  Limits give

  |  |  |  |
  | --- | --- | --- |
  |  | limt→0+ψi​(t)=0,limt→∞ψi​(t)={−∞,0<αi<1,0,αi=1,+∞,αi>1,\lim\_{t\to 0^{+}}\psi\_{i}(t)=0,\qquad\lim\_{t\to\infty}\psi\_{i}(t)=\begin{cases}-\infty,&0<\alpha\_{i}<1,\\ 0,&\alpha\_{i}=1,\\ +\infty,&\alpha\_{i}>1,\end{cases} |  |

  so non-positivity requires 0<αi≤10<\alpha\_{i}\leq 1.

  *Sufficiency.*
  If 0<αi≤10<\alpha\_{i}\leq 1, then

  |  |  |  |
  | --- | --- | --- |
  |  | ψi′​(t)=tαi−1​exp⁡(−2​t)​(tαi−exp⁡(t)​(t+1−αi)​Γ​(αi,t))Γ​(αi,t)2,\psi\_{i}^{\prime}(t)=\frac{t^{\alpha\_{i}-1}\exp(-2t)\bigl(t^{\alpha\_{i}}-\exp(t)(t+1-\alpha\_{i})\Gamma(\alpha\_{i},t)\bigr)}{\Gamma(\alpha\_{i},t)^{2}}, |  |

  which is non-positive whenever

  |  |  |  |
  | --- | --- | --- |
  |  | tαi​exp⁡(−t)t+1−αi≤Γ​(αi,t),\frac{t^{\alpha\_{i}}\exp(-t)}{t+1-\alpha\_{i}}\leq\Gamma(\alpha\_{i},t), |  |

  a Gautschi-type lower bound [Gautschi1959].
  Thus ψi\psi\_{i} is non-increasing with ψi​(0)=0\psi\_{i}(0)=0, proving ψi​(t)≤0\psi\_{i}(t)\leq 0 on [0,∞)[0,\infty).

  Therefore, ϕi\phi\_{i} is non-increasing on [0,∞)[0,\infty) if and only if 0<αi≤10<\alpha\_{i}\leq 1.

###### Proposition 3.10.

The following conditions are equivalent to the functions ϕi​(xi)=xi​log⁡FXi​(xi)\phi\_{i}(x\_{i})=x\_{i}\log F\_{X\_{i}}(x\_{i}) being non-increasing on [0,∞)[0,\infty).

* (i)

  Suppose that FXiF\_{X\_{i}} is differentiable then ϕi​(xi)\phi\_{i}(x\_{i}) is non-increasing for all xi∈[0,∞)x\_{i}\in[0,\infty) if and only if

  |  |  |  |
  | --- | --- | --- |
  |  | xi​hXi​(xi)≤∫xi∞hXi​(w)​dw,∀xi∈[0,∞).x\_{i}h\_{X\_{i}}(x\_{i})\leq\int\_{x\_{i}}^{\infty}h\_{X\_{i}}(w)\mathrm{d}w,\quad\forall x\_{i}\in[0,\infty). |  |

  Where hXi​(xi)=fXi​(xi)FXi​(xi)h\_{X\_{i}}(x\_{i})=\frac{\displaystyle f\_{X\_{i}}(x\_{i})}{\displaystyle F\_{X\_{i}}(x\_{i})} is the reverse hazard rate function [Block1998] of the random variable XiX\_{i}.
* (ii)

  ϕi​(xi)\phi\_{i}(x\_{i}) is non-increasing for all xi∈[0,∞)x\_{i}\in[0,\infty) if and only if the function Gi=log∘FXiG\_{i}=\log\circ F\_{X\_{i}} satisfies the scale-shrinking property, that is for any xi∈[0,∞)x\_{i}\in[0,\infty):

  |  |  |  |
  | --- | --- | --- |
  |  | Gi​(λ​xi)≤1λ​G​(xi),∀λ∈[1,∞).G\_{i}(\lambda x\_{i})\leq\frac{\displaystyle 1}{\displaystyle\lambda}G(x\_{i}),\ \quad\forall\lambda\in[1,\infty). |  |

###### Proof.

We will prove each claim separately.

* (i)

  Suppose FXiF\_{X\_{i}} is differentiable then:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕi′​(xi)\displaystyle\phi\_{i}^{{}^{\prime}}(x\_{i}) | =log⁡FXi​(xi)+xi​fXi​(xi)FXi​(xi),\displaystyle=\log F\_{X\_{i}}(x\_{i})+\frac{\displaystyle x\_{i}f\_{X\_{i}}(x\_{i})}{\displaystyle F\_{X\_{i}}(x\_{i})}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =−∫xi∞fXi​(w)FXi​(w)​dw+xi​fXi​(xi)FXi​(xi),\displaystyle=-\int\_{x\_{i}}^{\infty}\frac{\displaystyle f\_{X\_{i}}(w)}{\displaystyle F\_{X\_{i}}(w)}\mathrm{d}w+\frac{\displaystyle x\_{i}f\_{X\_{i}}(x\_{i})}{\displaystyle F\_{X\_{i}}(x\_{i})}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =−∫xi∞hXi​(w)​dw+xi​hXi​(xi).\displaystyle=-\int\_{x\_{i}}^{\infty}h\_{X\_{i}}(w)\mathrm{d}w+x\_{i}h\_{X\_{i}}(x\_{i}). |  |

  That means ϕi′​(xi)≤0,∀xi∈[0,∞)\phi\_{i}^{{}^{\prime}}(x\_{i})\leq 0,\ \forall x\_{i}\in[0,\infty), i.e. ϕi​(xi)\phi\_{i}(x\_{i}) is non-increasing for all xi∈[0,∞)x\_{i}\in[0,\infty), if and only if

  |  |  |  |
  | --- | --- | --- |
  |  | xi​hXi​(xi)≤∫xi∞hXi​(w)​dw,∀xi∈[0,∞).x\_{i}h\_{X\_{i}}(x\_{i})\leq\int\_{x\_{i}}^{\infty}h\_{X\_{i}}(w)\mathrm{d}w,\quad\forall x\_{i}\in[0,\infty). |  |
* (ii)

  Pick any xi≤yix\_{i}\leq y\_{i} such that yi=λ​xiy\_{i}=\lambda x\_{i}, λ≥1\lambda\geq 1, then

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | yi​Gi​(yi)\displaystyle y\_{i}G\_{i}(y\_{i}) | ≤xi​Gi​(xi),\displaystyle\leq x\_{i}G\_{i}(x\_{i}), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ⇔λ​xi​Gi​(λ​xi)\displaystyle\iff\lambda x\_{i}G\_{i}(\lambda x\_{i}) | ≤xi​Gi​(xi),\displaystyle\leq x\_{i}G\_{i}(x\_{i}), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ⇔Gi​(λ​xi)\displaystyle\iff G\_{i}(\lambda x\_{i}) | ≤1λ​Gi​(xi).\displaystyle\leq\frac{\displaystyle 1}{\displaystyle\lambda}G\_{i}(x\_{i}). |  |

∎

Although the non-increasing property is tractable, it is stronger than what is required for VaR super-additivity. The next example shows that Φ\Phi may be SD without being non-increasing.

###### Example 3.11.

Let 𝐗=(X1,X2,X3)\bm{X}=(X\_{1},X\_{2},X\_{3}) be an independent random vector (a special case of NSD).
Assume that X1X\_{1} and X2X\_{2} are Fréchet distributed with unit scales and shape parameters
α1=α2=12\alpha\_{1}=\alpha\_{2}=\tfrac{1}{2}, while X3X\_{3} has a piecewise CDF composed of a power-law part followed by a Fréchet CDF with θ3=1\theta\_{3}=1 and α3=12\alpha\_{3}=\tfrac{1}{2}.
Explicitly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | FX1​(x)=FX2​(x)\displaystyle F\_{X\_{1}}(x)=F\_{X\_{2}}(x) | =exp⁡(−1x),\displaystyle=\exp\!\left(-\frac{1}{\sqrt{x}}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ,FX3(x3)\displaystyle,F\_{X\_{3}}(x\_{3}) | ={x32e,0≤x3≤1,exp⁡(−1x3),x3>1.\displaystyle=\begin{cases}\dfrac{x\_{3}^{2}}{e},&0\leq x\_{3}\leq 1,\\[5.69054pt] \exp\!\left(-\dfrac{1}{\sqrt{x\_{3}}}\right),&x\_{3}>1.\end{cases} |  |

The corresponding ϕi\phi\_{i}-functions (as defined in Theorem  [3.4](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ1​(x1)\displaystyle\phi\_{1}(x\_{1}) | =−x1,\displaystyle=-\sqrt{x\_{1}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ2​(x2)\displaystyle\phi\_{2}(x\_{2}) | =−x2,\displaystyle=-\sqrt{x\_{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ3​(x3)\displaystyle\phi\_{3}(x\_{3}) | ={x3​(2​log⁡x3−1),0≤x3≤1,−x3,x3>1.\displaystyle=\begin{cases}x\_{3}\!\left(2\log x\_{3}-1\right),&0\leq x\_{3}\leq 1,\\[4.2679pt] -\sqrt{x\_{3}},&x\_{3}>1.\end{cases} |  |

It is clear that ϕ1\phi\_{1} and ϕ2\phi\_{2} are non-increasing, whereas ϕ3\phi\_{3} fails to be non-increasing on the interval x3∈[1e,1]x\_{3}\in\left[\frac{\displaystyle 1}{\displaystyle\sqrt{e}},1\right].
Figure [2](https://arxiv.org/html/2512.07787v1#S3.F2 "Figure 2 ‣ Example 3.11. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") shows the graphs of these functions.

![Refer to caption](phi12nonSD.png)


(a) ϕ1\phi\_{1} and ϕ2\phi\_{2}

![Refer to caption](phi3nonSD.png)


(b) ϕ3\phi\_{3}

Figure 2: The marginal ϕi\phi\_{i} functions.

By Proposition [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), this implies that Φ\Phi is not globally non-increasing.
Nevertheless, we now verify that the SD condition for

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,x2,x3)=ϕ1​(x1)+ϕ2​(x2)+ϕ3​(x3)\Phi(x\_{1},x\_{2},x\_{3})=\phi\_{1}(x\_{1})+\phi\_{2}(x\_{2})+\phi\_{3}(x\_{3}) |  |

still holds.
We claim that for all x1,x2,x3≥0x\_{1},x\_{2},x\_{3}\geq 0,

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,x2,x3)≥Φ​(s,s,s),s=x1+x2+x3.\Phi(x\_{1},x\_{2},x\_{3})\;\geq\;\Phi(s,s,s),\qquad s=x\_{1}+x\_{2}+x\_{3}. |  |

Since x1+x2≤2​(x1+x2)=2​(s−x3)\sqrt{x\_{1}}+\sqrt{x\_{2}}\leq\sqrt{2(x\_{1}+x\_{2})}=\sqrt{2(s-x\_{3})}, we obtain

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,x2,x3)=−x1−x2+ϕ3​(x3)≥−2​s−x3+ϕ3​(x3).\Phi(x\_{1},x\_{2},x\_{3})=-\sqrt{x\_{1}}-\sqrt{x\_{2}}+\phi\_{3}(x\_{3})\;\geq\;-\sqrt{2}\,\sqrt{s-x\_{3}}+\phi\_{3}(x\_{3}). |  |

For fixed ss, consider the function

|  |  |  |
| --- | --- | --- |
|  | x3↦2​s−2​s−x3+ϕ3​(x3)−ϕ3​(s).x\_{3}\mapsto 2\sqrt{s}-\sqrt{2}\sqrt{s-x\_{3}}+\phi\_{3}(x\_{3})-\phi\_{3}(s). |  |

It is convex on each smooth piece of [0,s][0,s]; hence its minimum occurs at one of the points
x3∈{0,1,s}x\_{3}\in\{0,1,s\}.
Evaluating at these points yields nonnegative values:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​s−2​s−0+ϕ3​(0)−ϕ3​(s)\displaystyle 2\sqrt{s}-\sqrt{2\!}\sqrt{s-0}+\phi\_{3}(0)-\phi\_{3}(s) | ≥0,\displaystyle\geq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​s−2​s−1+ϕ3​(1)−ϕ3​(s)\displaystyle 2\sqrt{s}-\sqrt{2\!}\sqrt{s-1}+\phi\_{3}(1)-\phi\_{3}(s) | ≥0,\displaystyle\geq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​s−2​s−s+ϕ3​(s)−ϕ3​(s)\displaystyle 2\sqrt{s}-\sqrt{2\!}\sqrt{s-s}+\phi\_{3}(s)-\phi\_{3}(s) | =2​s≥0.\displaystyle=2\sqrt{s}\geq 0. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | −2​s−x3+ϕ3​(x3)≥−2​s+ϕ3​(s)=Φ​(s,s,s),-\sqrt{2}\,\sqrt{s-x\_{3}}+\phi\_{3}(x\_{3})\;\geq\;-2\sqrt{s}+\phi\_{3}(s)=\Phi(s,s,s), |  |

and the claim follows.

While the VaR of the sum SS can only be computed numerically, the VaRs of the marginals are given explicitly. For X1X\_{1} and X2X\_{2},

|  |  |  |
| --- | --- | --- |
|  | VaRp​[X1]=VaRp​[X2]=1log2⁡(1/p),{\mathrm{VaR}}\_{p}[X\_{1}]={\mathrm{VaR}}\_{p}[X\_{2}]=\frac{1}{\log^{2}(1/p)}, |  |

and for X3X\_{3},

|  |  |  |
| --- | --- | --- |
|  | VaRp​[X3]={e​p,0<p≤1e,1log2⁡(1/p),1e<p<1.{\mathrm{VaR}}\_{p}[X\_{3}]=\begin{cases}\sqrt{e}\,\sqrt{p},&0<p\leq\frac{\displaystyle 1}{\displaystyle e},\\[5.69054pt] \dfrac{1}{\log^{2}(1/p)},&\frac{\displaystyle 1}{\displaystyle e}<p<1.\end{cases} |  |

Figure [3](https://arxiv.org/html/2512.07787v1#S3.F3 "Figure 3 ‣ Example 3.11. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") compares VaRp​[S]{\mathrm{VaR}}\_{p}[S] with the sum of marginal VaRs.

![Refer to caption](VaRnonSD.png)


Figure 3: Comparison of VaRp​[S]{\mathrm{VaR}}\_{p}[S] and VaRp​[X1]+VaRp​[X2]+VaRp​[X3]{\mathrm{VaR}}\_{p}[X\_{1}]+{\mathrm{VaR}}\_{p}[X\_{2}]+{\mathrm{VaR}}\_{p}[X\_{3}].

Figure [3](https://arxiv.org/html/2512.07787v1#S3.F3 "Figure 3 ‣ Example 3.11. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") shows that 𝐗\bm{X} is VaR super-additive.
This example illustrates that an NSD vector may have an SD aggregator Φ\Phi without Φ\Phi being globally non-increasing, while still exhibiting VaR super-additivity.

A natural question that follows any characterization of a property for random vectors is: under what transformations does the property persist? In this spirit, we examine the conditions under which the transformed random vector

|  |  |  |
| --- | --- | --- |
|  | 𝑿~=(ξ1​(X1),…,ξn​(Xn)),\widetilde{\bm{X}}=(\xi\_{1}(X\_{1}),\dots,\xi\_{n}(X\_{n})), |  |

where each ξi:[0,∞)→[0,∞)\xi\_{i}:[0,\infty)\to[0,\infty) is measurable, preserves the property of VaR super-additivity. Specifically, we seek to identify assumptions on the functions ξi\xi\_{i} that ensure 𝑿~\widetilde{\bm{X}} remains VaR super-additive whenever the original vector 𝑿=(X1,…,Xn)\bm{X}=(X\_{1},\dots,X\_{n}) is already VaR super-additive.

###### Proposition 3.12.

Let 𝐗\bm{X} be NLOD with continuous marginal distributions FXiF\_{X\_{i}}, and suppose each ϕi\phi\_{i} in Equation ([3.1](https://arxiv.org/html/2512.07787v1#S3.E1 "In Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is non-increasing. Define

|  |  |  |
| --- | --- | --- |
|  | 𝑿~=(X~1,…,X~n),where ​X~i=ξi​(Xi).\widetilde{\bm{X}}=(\widetilde{X}\_{1},\dots,\widetilde{X}\_{n}),\quad\text{where }\widetilde{X}\_{i}=\xi\_{i}(X\_{i}). |  |

If each ξi\xi\_{i} is strictly increasing, convex, and satisfies ξi​(0)=0\xi\_{i}(0)=0, then 𝐗~\widetilde{\bm{X}} is VaR super-additive.

###### Proof.

First, since 𝑿\bm{X} is NLOD and each ξi\xi\_{i} is strictly increasing, we have

|  |  |  |
| --- | --- | --- |
|  | F𝑿~​(x1,…,xn)=F𝑿​(ξ1−1​(x1),…,ξn−1​(xn))≤∏i=1nFXi​(ξi−1​(xi))=∏i=1nFX~i​(xi),F\_{\widetilde{\bm{X}}}(x\_{1},\dots,x\_{n})=F\_{\bm{X}}\big(\xi\_{1}^{-1}(x\_{1}),\dots,\xi\_{n}^{-1}(x\_{n})\big)\leq\prod\_{i=1}^{n}F\_{X\_{i}}\big(\xi\_{i}^{-1}(x\_{i})\big)=\prod\_{i=1}^{n}F\_{\widetilde{X}\_{i}}(x\_{i}), |  |

which establishes that 𝑿~\widetilde{\bm{X}} is NLOD.

Moreover, strict monotonicity and convexity of ξi\xi\_{i} imply that ξi−1\xi\_{i}^{-1} is continuous and strictly increasing. Combined with the continuity of FXiF\_{X\_{i}}, this ensures that each marginal CDF

|  |  |  |
| --- | --- | --- |
|  | FX~i=FXi∘ξi−1F\_{\widetilde{X}\_{i}}=F\_{X\_{i}}\circ\xi\_{i}^{-1} |  |

is continuous.
  
Second, define

|  |  |  |
| --- | --- | --- |
|  | ϕ~i​(xi)=xi​log⁡FX~i​(xi).\widetilde{\phi}\_{i}(x\_{i})=x\_{i}\log F\_{\widetilde{X}\_{i}}(x\_{i}). |  |

For xi<yix\_{i}<y\_{i}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ~i​(yi)\displaystyle\widetilde{\phi}\_{i}(y\_{i}) | =yi​log⁡FX~i​(yi),\displaystyle=y\_{i}\log F\_{\widetilde{X}\_{i}}(y\_{i}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =yi​log⁡FXi​(ξi−1​(yi)),\displaystyle=y\_{i}\log F\_{X\_{i}}\left(\xi\_{i}^{-1}(y\_{i})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤yi​ξi−1​(xi)ξi−1​(yi)​log⁡FXi​(ξi−1​(xi)),\displaystyle\leq y\_{i}\frac{\displaystyle\xi\_{i}^{-1}(x\_{i})}{\displaystyle\xi\_{i}^{-1}(y\_{i})}\log F\_{X\_{i}}\left(\xi\_{i}^{-1}(x\_{i})\right), |  |

where the last inequality follows by applying the non-increasing property of ϕi\phi\_{i} to the strictly increasing pair ξi−1​(xi)<ξi−1​(yi)\xi\_{i}^{-1}(x\_{i})<\xi\_{i}^{-1}(y\_{i}).
  
By convexity of ξi\xi\_{i} and the condition ξi​(0)=0\xi\_{i}(0)=0, the secant slopes from the origin are non-decreasing: for 0<ui<vi0<u\_{i}<v\_{i},

|  |  |  |
| --- | --- | --- |
|  | ξi​(ui)ui≤ξi​(vi)vi.\frac{\xi\_{i}(u\_{i})}{u\_{i}}\leq\frac{\xi\_{i}(v\_{i})}{v\_{i}}. |  |

Setting ui=ξi−1​(xi)u\_{i}=\xi\_{i}^{-1}(x\_{i}) and vi=ξi−1​(yi)v\_{i}=\xi\_{i}^{-1}(y\_{i}) gives

|  |  |  |
| --- | --- | --- |
|  | xiξi−1​(xi)≤yiξi−1​(yi)⟹xi≤yi​ξi−1​(xi)ξi−1​(yi).\frac{x\_{i}}{\xi\_{i}^{-1}(x\_{i})}\leq\frac{y\_{i}}{\xi\_{i}^{-1}(y\_{i})}\quad\implies\quad x\_{i}\leq y\_{i}\frac{\xi\_{i}^{-1}(x\_{i})}{\xi\_{i}^{-1}(y\_{i})}. |  |

Combining these results, and noting that log∘FXi\log\circ F\_{X\_{i}} is a negative function, we obtain

|  |  |  |
| --- | --- | --- |
|  | ϕ~i​(yi)≤yi​ξi−1​(xi)ξi−1​(yi)​log⁡FXi​(ξi−1​(xi))≤xi​log⁡FXi​(ξi−1​(xi))=ϕ~i​(xi),\widetilde{\phi}\_{i}(y\_{i})\leq y\_{i}\frac{\xi\_{i}^{-1}(x\_{i})}{\xi\_{i}^{-1}(y\_{i})}\log F\_{X\_{i}}\big(\xi\_{i}^{-1}(x\_{i})\big)\leq x\_{i}\log F\_{X\_{i}}\big(\xi\_{i}^{-1}(x\_{i})\big)=\widetilde{\phi}\_{i}(x\_{i}), |  |

so ϕ~i​(xi)\widetilde{\phi}\_{i}(x\_{i}) is non-increasing for all xi∈[0,∞)x\_{i}\in[0,\infty).
  
Applying Corollary [3.7](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem7 "Corollary 3.7. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), we conclude that 𝑿~\widetilde{\bm{X}} is VaR super-additive.
∎

We conclude this section by noting that although the NSD and SD properties allow Theorem [3.4](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") to characterize a broad class of random vectors for which super-additivity is guaranteed, they are not the only indicators of VaR super-additivity. The following example illustrates situations in which VaR is super-additive even when neither NSD nor SD is satisfied.

###### Example 3.13.

Let 𝐗=(X1,X2)\bm{X}=(X\_{1},X\_{2}) be a bivariate random vector.

* (1)

  Assume that 𝑿\bm{X} follows a bivariate Pareto distribution of Type II with unit scale parameters and shape 0<α≤10<\alpha\leq 1. Its joint DDF is

  |  |  |  |
  | --- | --- | --- |
  |  | F¯𝑿​(x1,x2)=(1+x1+x2)−α,x1,x2≥0.\overline{F}\_{\bm{X}}(x\_{1},x\_{2})=(1+x\_{1}+x\_{2})^{-\alpha},\qquad x\_{1},x\_{2}\geq 0. |  |

  Consequently, X1X\_{1} and X2X\_{2} have Pareto (II) marginal CDFs with the same shape parameter:

  |  |  |  |
  | --- | --- | --- |
  |  | FX1​(x)=FX2​(x)=1−(1+x)−α,x≥0.F\_{X\_{1}}(x)=F\_{X\_{2}}(x)=1-(1+x)^{-\alpha},\qquad x\geq 0. |  |

  A direct computation shows that the CDF of the sum S=X1+X2S=X\_{1}+X\_{2} is

  |  |  |  |
  | --- | --- | --- |
  |  | FS​(s)=1−(1+s)−α−1​(1+(α+1)​s),s≥0.F\_{S}(s)=1-(1+s)^{-\alpha-1}\bigl(1+(\alpha+1)s\bigr),\qquad s\geq 0. |  |

  We now compare FS​(t)F\_{S}(t) with FX1​(t)​FX2​(t)F\_{X\_{1}}(t)F\_{X\_{2}}(t).
  Since 0<α≤10<\alpha\leq 1, one checks that

  |  |  |  |
  | --- | --- | --- |
  |  | α​t1+t≤1−(1+t)−α,t≥0.\frac{\alpha t}{1+t}\leq 1-(1+t)^{-\alpha},\qquad t\geq 0. |  |

  Using this inequality, we rewrite FS​(t)F\_{S}(t) as

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | FS​(t)\displaystyle F\_{S}(t) | =1−(1+t)−α−1​(1+(α+1)​t)\displaystyle=1-(1+t)^{-\alpha-1}(1+(\alpha+1)t) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =1−(1+t)−α​(1+α​t1+t)\displaystyle=1-(1+t)^{-\alpha}\left(1+\frac{\alpha t}{1+t}\right) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≥1−(1+t)−α​(2−(1+t)−α)\displaystyle\geq 1-(1+t)^{-\alpha}\left(2-(1+t)^{-\alpha}\right) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =1−2​(1+t)−α+(1+t)−2​α\displaystyle=1-2(1+t)^{-\alpha}+(1+t)^{-2\alpha} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =(1−(1+t)−α)2\displaystyle=\left(1-(1+t)^{-\alpha}\right)^{2} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =FX1​(t)​FX2​(t).\displaystyle=F\_{X\_{1}}(t)\,F\_{X\_{2}}(t). |  |

  Hence FS​(t)≥FX1​(t)​FX2​(t)F\_{S}(t)\geq F\_{X\_{1}}(t)F\_{X\_{2}}(t) for all t≥0t\geq 0, meaning that 𝑿\bm{X} is *not* NSD.

  From Example [3.9](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem9 "Example 3.9. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), the functions ϕi\phi\_{i} are non-increasing for Pareto (II) marginals with 0<α≤10<\alpha\leq 1, and therefore Φ\Phi is SD.

  To compute VaRs, set α=1\alpha=1 for simplicity. Then

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[X1]=VaRp​[X2]=p1−p,VaRp​[S]=p+p1−p.{\mathrm{VaR}}\_{p}[X\_{1}]={\mathrm{VaR}}\_{p}[X\_{2}]=\frac{p}{1-p},\qquad{\mathrm{VaR}}\_{p}[S]=\frac{p+\sqrt{p}}{1-p}. |  |

  Since p≥p\sqrt{p}\geq p, we have

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[S]=p+p1−p≥2​p1−p=VaRp​[X1]+VaRp​[X2],{\mathrm{VaR}}\_{p}[S]=\frac{p+\sqrt{p}}{1-p}\geq\frac{2p}{1-p}={\mathrm{VaR}}\_{p}[X\_{1}]+{\mathrm{VaR}}\_{p}[X\_{2}], |  |

  showing that 𝑿\bm{X} is VaR super-additive.
* (2)

  Next, suppose that 𝑿\bm{X} is a mutually exclusive [Dhaene1999] discrete vector supported on

  |  |  |  |
  | --- | --- | --- |
  |  | {(2−k,0):k≥1}∪{(0,2−k):k≥1},\bigl\{(2^{-k},0):k\geq 1\bigr\}\ \cup\ \bigl\{(0,2^{-k}):k\geq 1\bigr\}, |  |

  with joint probability masses

  |  |  |  |
  | --- | --- | --- |
  |  | ℙ​((X1,X2)=(2−k,0))=ℙ​((X1,X2)=(0,2−k))=12k−1,k≥1.\mathbb{P}\bigl((X\_{1},X\_{2})=(2^{-k},0)\bigr)=\mathbb{P}\bigl((X\_{1},X\_{2})=(0,2^{-k})\bigr)=\frac{1}{2^{\,k-1}},\qquad k\geq 1. |  |

  Using geometric-series identities, one obtains the marginal CDFs

  |  |  |  |
  | --- | --- | --- |
  |  | FX1​(x)=FX2​(x)={0,x<0,12,0≤x<2,1−2−(k+1),2k≤x<2k+1,k≥1,\displaystyle F\_{X\_{1}}(x)=F\_{X\_{2}}(x)=\begin{cases}0,&x<0,\\[4.0pt] \tfrac{1}{2},&0\leq x<2,\\[4.0pt] 1-2^{-(k+1)},&2^{k}\leq x<2^{k+1},\qquad k\geq 1,\end{cases} |  |

  and the CDF of the sum

  |  |  |  |
  | --- | --- | --- |
  |  | FS​(s)={0,s<2,1−2−k,2k≤s<2k+1,k≥1.F\_{S}(s)=\begin{cases}0,&s<2,\\[4.0pt] 1-2^{-k},&2^{k}\leq s<2^{k+1},\qquad k\geq 1.\end{cases} |  |

  For t<2t<2, we immediately see that FS​(t)<FX1​(t)​FX2​(t)F\_{S}(t)<F\_{X\_{1}}(t)F\_{X\_{2}}(t).
  For t≥2t\geq 2 (with 2k≤t<2k+12^{k}\leq t<2^{k+1}), we have

  |  |  |  |
  | --- | --- | --- |
  |  | FS​(t)=1−2−k<1−2−k+2−(2​k+2)=(1−2−(k+1))2=FX1​(t)​FX2​(t),F\_{S}(t)=1-2^{-k}<1-2^{-k}+2^{-(2k+2)}=\bigl(1-2^{-(k+1)}\bigr)^{2}=F\_{X\_{1}}(t)F\_{X\_{2}}(t), |  |

  so 𝑿\bm{X} is NSD. This expected as the random vector 𝑿\bm{X} has a counter-monotonic joint law which belongs to the NSD class.

  The marginal CDFs are discontinuous, and the functions ϕi​(x)=x​log⁡FXi​(x)\phi\_{i}(x)=x\log F\_{X\_{i}}(x) are not non-increasing.
  To see the latter, take x=2k<y=2k+1x=2^{k}<y=2^{k+1}, k≥1k\geq 1. Then

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕi​(y)−ϕi​(x)\displaystyle\phi\_{i}(y)-\phi\_{i}(x) | =2k+1​log⁡(1−2−(k+2))−2k​log⁡(1−2−(k+1))\displaystyle=2^{k+1}\log\Bigl(1-2^{-(k+2)}\Bigr)-2^{k}\log\Bigl(1-2^{-(k+1)}\Bigr) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =2k​log⁡(1+12k+3​12k+1−1)>0.\displaystyle=2^{k}\log\left(1+\frac{1}{2^{k+3}}\frac{1}{2^{k+1}-1}\right)>0. |  |

  Thus ϕi\phi\_{i} is strictly increasing along the sequence {2k}\{2^{k}\}, and consequently Φ\Phi is not SD (take x=y=2kx=y=2^{k} and s=x+y=2k+1s=x+y=2^{k+1} then Φ​(x,y)=Φ​(2k,2k)<Φ​(2k+1,2k+1)=Φ​(s,s)\Phi(x,y)=\Phi(2^{k},2^{k})<\Phi(2^{k+1},2^{k+1})=\Phi(s,s)).

  Finally, the VaR functions are

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | VaRp​[X1]=VaRp​[X2]\displaystyle{\mathrm{VaR}}\_{p}[X\_{1}]={\mathrm{VaR}}\_{p}[X\_{2}] | ={0,0<p≤12,2k,1−2−k<p≤1−2−(k+1),k≥1,\displaystyle=\begin{cases}0,&0<p\leq\tfrac{1}{2},\\[4.0pt] 2^{k},&1-2^{-k}<p\leq 1-2^{-(k+1)},\qquad k\geq 1,\end{cases} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | VaRp​[S]\displaystyle{\mathrm{VaR}}\_{p}[S] | =2k,1−2−(k−1)<p≤1−2−k,k≥1.\displaystyle=2^{k},\hskip 17.00024pt1-2^{-(k-1)}<p\leq 1-2^{-k},\ \ k\geq 1. |  |

  Hence, for 0<p≤120<p\leq\tfrac{1}{2},

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[S]=2>0=VaRp​[X1]+VaRp​[X2],{\mathrm{VaR}}\_{p}[S]=2>0={\mathrm{VaR}}\_{p}[X\_{1}]+{\mathrm{VaR}}\_{p}[X\_{2}], |  |

  and for any k≥2k\geq 2 and the corresponding range of pp,

  |  |  |  |
  | --- | --- | --- |
  |  | VaRp​[S]=2k=2k−1+2k−1=VaRp​[X1]+VaRp​[X2].{\mathrm{VaR}}\_{p}[S]=2^{k}=2^{k-1}+2^{k-1}={\mathrm{VaR}}\_{p}[X\_{1}]+{\mathrm{VaR}}\_{p}[X\_{2}]. |  |

  Therefore, 𝑿\bm{X} is VaR super-additive in this case as well.

## 4 Further Generalizations and Remarks

The results established in Sections [2](https://arxiv.org/html/2512.07787v1#S2 "2 VaR Sub-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") and [3](https://arxiv.org/html/2512.07787v1#S3 "3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") extend naturally to random variables whose supports begin at arbitrary finite lower end-points

|  |  |  |
| --- | --- | --- |
|  | ai=sup{x∈ℝ:FXi​(x)≤0}>−∞,∀i∈{1,…,n}.a\_{i}=\sup\{x\in\mathbb{R}:F\_{X\_{i}}(x)\leq 0\}>-\infty,\qquad\forall i\in\{1,\dots,n\}. |  |

We denote the corresponding random vector by

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒂=(X1a1,…,Xnan),𝒂=(a1,…,an)∈ℝn,\bm{X}^{\bm{a}}=(X\_{1}^{a\_{1}},\dots,X\_{n}^{a\_{n}}),\qquad\bm{a}=(a\_{1},\dots,a\_{n})\in\mathbb{R}^{n}, |  |

with 𝑿𝟎=𝑿\bm{X}^{\bm{0}}=\bm{X} representing the previously studied case of random variables supported on [0,∞)[0,\infty).

Similarly, the theory extends to random variables possessing arbitrary finite upper end-points

|  |  |  |
| --- | --- | --- |
|  | bi=inf{x∈ℝ:FXi​(x)≥1}<∞,∀i∈{1,…,n},b\_{i}=\inf\{x\in\mathbb{R}:F\_{X\_{i}}(x)\geq 1\}<\infty,\qquad\forall i\in\{1,\dots,n\}, |  |

for which we write

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒃=(X1b1,…,Xnbn),𝒃=(b1,…,bn)∈ℝn.\bm{X}^{\bm{b}}=(X\_{1}^{b\_{1}},\dots,X\_{n}^{b\_{n}}),\qquad\bm{b}=(b\_{1},\dots,b\_{n})\in\mathbb{R}^{n}. |  |

For notational convenience, define the corresponding sum random variables by

|  |  |  |
| --- | --- | --- |
|  | S𝒂=∑i=1nXiai,S𝒃=∑i=1nXibi.S^{\bm{a}}=\sum\_{i=1}^{n}X\_{i}^{a\_{i}},\qquad S^{\bm{b}}=\sum\_{i=1}^{n}X\_{i}^{b\_{i}}. |  |

It is immediate that both transformed vectors admit the simple representations

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒂=𝒂+𝑿,𝑿𝒃=𝒃−𝑿,\bm{X}^{\bm{a}}=\bm{a}+\bm{X},\qquad\bm{X}^{\bm{b}}=\bm{b}-\bm{X}, |  |

and, due to the translation and scale equivariance of VaR, their components satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRp​[Xiai]\displaystyle{\mathrm{VaR}}\_{p}[X\_{i}^{a\_{i}}] | =VaRp​[ai+Xi]=ai+VaRp​[Xi],\displaystyle={\mathrm{VaR}}\_{p}[a\_{i}+X\_{i}]=a\_{i}+{\mathrm{VaR}}\_{p}[X\_{i}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRp​[Xibi]\displaystyle{\mathrm{VaR}}\_{p}[X\_{i}^{b\_{i}}] | =VaRp​[bi−Xi]=bi−VaR1−p​[Xi].\displaystyle={\mathrm{VaR}}\_{p}[b\_{i}-X\_{i}]=b\_{i}-{\mathrm{VaR}}\_{1-p}[X\_{i}]. |  |

Both facts will be crucial in what follows.

###### Proposition 4.1.

The following equivalences hold:

* (i)

  𝑿𝒂\bm{X}^{\bm{a}} is VaR sub-additive if and only if 𝑿𝒂\bm{X}^{\bm{a}} is VaR additive.
* (ii)

  𝑿𝒃\bm{X}^{\bm{b}} is VaR super-additive if and only if 𝑿𝒃\bm{X}^{\bm{b}} is VaR additive.

In both cases, the random vectors 𝐗𝐚\bm{X}^{\bm{a}} and 𝐗𝐛\bm{X}^{\bm{b}} must be co-monotonic.

###### Proof.

The proof in each case follows from the translation and scale equivariance properties of VaR.

(i)
Using translation equivariance,

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒂​ is VaR sub-additive⇔𝑿​ is VaR sub-additive.\bm{X}^{\bm{a}}\text{ is VaR sub-additive}\iff\bm{X}\text{ is VaR sub-additive}. |  |

By Theorem [2.2](https://arxiv.org/html/2512.07787v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2 VaR Sub-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"),

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒂​ is VaR sub-additive⇔𝑿​ is VaR additive.\bm{X}^{\bm{a}}\text{ is VaR sub-additive}\iff\bm{X}\text{ is VaR additive}. |  |

Applying translation equivariance once more yields

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒂​ is VaR sub-additive⇔𝑿𝒂​ is VaR additive.\bm{X}^{\bm{a}}\text{ is VaR sub-additive}\iff\bm{X}^{\bm{a}}\text{ is VaR additive}. |  |

(ii)
Using both scale and translation equivariance,

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒃​ is VaR super-additive⇔𝑿​ is VaR sub-additive.\bm{X}^{\bm{b}}\text{ is VaR super-additive}\iff\bm{X}\text{ is VaR sub-additive}. |  |

Applying Theorem [2.2](https://arxiv.org/html/2512.07787v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2 VaR Sub-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") again gives

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒃​ is VaR super-additive⇔𝑿​ is VaR additive.\bm{X}^{\bm{b}}\text{ is VaR super-additive}\iff\bm{X}\text{ is VaR additive}. |  |

Repeating the equivariance arguments leads to

|  |  |  |
| --- | --- | --- |
|  | 𝑿𝒃​ is VaR super-additive⇔𝑿𝒃​ is VaR additive.\bm{X}^{\bm{b}}\text{ is VaR super-additive}\iff\bm{X}^{\bm{b}}\text{ is VaR additive}. |  |

Finally, in both parts, co-monotonicity follows directly from Theorem [2.2](https://arxiv.org/html/2512.07787v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2 VaR Sub-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables").
∎

The preceding proposition highlights an important structural limitation: VaR sub-additivity cannot occur for random variables with finite lower end-points, while VaR super-additivity cannot occur for random variables with finite upper end-points.

###### Corollary 4.2.

For compactly supported random variables 𝐗𝐚,𝐛\bm{X}^{\bm{a},\bm{b}}, i.e. random variables possessing both finite lower and upper end-points, VaR sub-additivity and VaR super-additivity are each equivalent to VaR additivity. Consequently, such random variables can never exhibit strict VaR sub-additivity or strict VaR super-additivity.

The limitations of VaR in the prior discussion motivates the search for conditions, analogous to those developed in Section [3](https://arxiv.org/html/2512.07787v1#S3 "3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), that permit the analysis of VaR super- and sub-additivity in more flexible settings. That prompts us to extend the general results of Section [3](https://arxiv.org/html/2512.07787v1#S3 "3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") to these shifted and scaled settings.
In particular, the following proposition provides analogous conditions for VaR super-additivity of the shifted vector 𝑿𝒂\bm{X}^{\bm{a}} and VaR sub-additivity of the reflected and shifted vector 𝑿𝒃\bm{X}^{\bm{b}}.

###### Proposition 4.3.

* (i)

  Suppose 𝑿𝒂\bm{X}^{\bm{a}} has continuous marginal CDFs FXiaiF\_{X\_{i}^{a\_{i}}} and satisfies

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | FS𝒂​(t+a+)≤∏i=1nFXiai​(t+ai),a+=∑i=1nai,∀t∈[0,∞),F\_{S^{\bm{a}}}(t+a\_{+})\leq\prod\_{i=1}^{n}F\_{X\_{i}^{a\_{i}}}(t+a\_{i}),\qquad a\_{+}=\sum\_{i=1}^{n}a\_{i},\quad\forall t\in[0,\infty), |  | (4.1) |

  and that the function

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Φ𝒂​(x1,…,xn)=∑i=1nxi​log⁡FXiai​(xi+ai),xi∈[0,∞),\Phi^{\bm{a}}(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}x\_{i}\log F\_{X\_{i}^{a\_{i}}}(x\_{i}+a\_{i}),\qquad x\_{i}\in[0,\infty), |  | (4.2) |

  is SD. Then 𝑿𝒂\bm{X}^{\bm{a}} is VaR super-additive.
* (ii)

  Suppose 𝑿𝒃\bm{X}^{\bm{b}} has continuous marginal DDFs F¯Xibi\overline{F}\_{X\_{i}^{b\_{i}}} and satisfies

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | F¯S𝒃​(b+−t)≤∏i=1nF¯Xibi​(bi−t),b+=∑i=1nbi,∀t∈[0,∞),\overline{F}\_{S^{\bm{b}}}(b\_{+}-t)\leq\prod\_{i=1}^{n}\overline{F}\_{X\_{i}^{b\_{i}}}(b\_{i}-t),\qquad b\_{+}=\sum\_{i=1}^{n}b\_{i},\quad\forall t\in[0,\infty), |  | (4.3) |

  and that the function

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Φ𝒃​(x1,…,xn)=∑i=1nxi​log⁡F¯Xibi​(bi−xi),xi∈[0,∞),\Phi^{\bm{b}}(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}x\_{i}\log\overline{F}\_{X\_{i}^{b\_{i}}}(b\_{i}-x\_{i}),\qquad x\_{i}\in[0,\infty), |  | (4.4) |

  is SD. Then 𝑿𝒃\bm{X}^{\bm{b}} is VaR sub-additive.

###### Proof.

Continuity of each FXiF\_{X\_{i}} follows from the continuity of FXiaiF\_{X\_{i}^{a\_{i}}} or of F¯Xibi\overline{F}\_{X\_{i}^{b\_{i}}}.

(i)
Since 𝑿𝒂=𝒂+𝑿\bm{X}^{\bm{a}}=\bm{a}+\bm{X} and S𝒂=S+a+S^{\bm{a}}=S+a\_{+}, we have

|  |  |  |
| --- | --- | --- |
|  | FS𝒂​(t+a+)=FS​(t),FXiai​(xi+ai)=FXi​(xi).F\_{S^{\bm{a}}}(t+a\_{+})=F\_{S}(t),\qquad F\_{X\_{i}^{a\_{i}}}(x\_{i}+a\_{i})=F\_{X\_{i}}(x\_{i}). |  |

Thus the condition in Equation ([4.1](https://arxiv.org/html/2512.07787v1#S4.E1 "In item (i) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) implies

|  |  |  |
| --- | --- | --- |
|  | FS​(t)≤∏i=1nFXi​(t),∀t∈[0,∞),F\_{S}(t)\leq\prod\_{i=1}^{n}F\_{X\_{i}}(t),\qquad\forall t\in[0,\infty), |  |

i.e. 𝑿\bm{X} is NSD. Moreover, if

|  |  |  |
| --- | --- | --- |
|  | Φ𝒂​(x1,…,xn)=∑i=1nxi​log⁡FXiai​(xi+ai)\Phi^{\bm{a}}(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}x\_{i}\log F\_{X\_{i}^{a\_{i}}}(x\_{i}+a\_{i}) |  |

is SD, then so is

|  |  |  |
| --- | --- | --- |
|  | Φ​(x1,…,xn)=∑i=1nxi​log⁡FXi​(xi).\Phi(x\_{1},\dots,x\_{n})=\sum\_{i=1}^{n}x\_{i}\log F\_{X\_{i}}(x\_{i}). |  |

By Theorem [3.4](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), 𝑿\bm{X} is VaR super-additive.
Translation equivariance then gives that 𝑿𝒂\bm{X}^{\bm{a}} is VaR super-additive.

(ii)
Since 𝑿𝒃=𝒃−𝑿\bm{X}^{\bm{b}}=\bm{b}-\bm{X} and S𝒃=b+−SS^{\bm{b}}=b\_{+}-S, we obtain

|  |  |  |
| --- | --- | --- |
|  | F¯S𝒃​(b+−t)=FS​(t),F¯Xibi​(bi−xi)=FXi​(xi).\overline{F}\_{S^{\bm{b}}}(b\_{+}-t)=F\_{S}(t),\qquad\overline{F}\_{X\_{i}^{b\_{i}}}(b\_{i}-x\_{i})=F\_{X\_{i}}(x\_{i}). |  |

Applying the same reasoning as in part (i), the given assumptions imply that 𝑿\bm{X} is VaR super-additive.
Using both scale and translation equivariance, we conclude that 𝑿𝒃\bm{X}^{\bm{b}} is VaR sub-additive.
∎

Using the results we obtained in Proposition [4.3](https://arxiv.org/html/2512.07787v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), we can now delineate the sufficient conditions that parallel those of
Propositions [3.5](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") and [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables").
These conditions are easily verifiable and ensure that 𝑿𝒂\bm{X}^{\bm{a}} (resp. 𝑿𝒃\bm{X}^{\bm{b}}) is VaR super-additive
(resp. VaR sub-additive).

###### Proposition 4.4.

* (i)

  If 𝑿𝒂\bm{X}^{\bm{a}} is NLOD with continuous FXiaiF\_{X\_{i}^{a\_{i}}}, and if each function appearing in
  Equation ([4.2](https://arxiv.org/html/2512.07787v1#S4.E2 "In item (i) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")),

  |  |  |  |
  | --- | --- | --- |
  |  | ϕiai​(xi)=xi​log⁡FXiai​(xi+ai),xi∈[0,∞),\phi\_{i}^{a\_{i}}(x\_{i})=x\_{i}\log F\_{X\_{i}^{a\_{i}}}(x\_{i}+a\_{i}),\qquad x\_{i}\in[0,\infty), |  |

  is non-increasing, then 𝑿𝒂\bm{X}^{\bm{a}} is VaR super-additive.
* (ii)

  If 𝑿𝒃\bm{X}^{\bm{b}} is NUOD (defined analogously to NLOD but with DDFs instead of CDFs) with
  continuous F¯Xibi\overline{F}\_{X\_{i}^{b\_{i}}}, and if each function appearing in Equation ([4.4](https://arxiv.org/html/2512.07787v1#S4.E4 "In item (ii) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")),

  |  |  |  |
  | --- | --- | --- |
  |  | ϕibi​(xi)=xi​log⁡F¯Xibi​(bi−xi),xi∈[0,∞),\phi\_{i}^{b\_{i}}(x\_{i})=x\_{i}\log\overline{F}\_{X\_{i}^{b\_{i}}}(b\_{i}-x\_{i}),\qquad x\_{i}\in[0,\infty), |  |

  is non-increasing, then 𝑿𝒃\bm{X}^{\bm{b}} is VaR sub-additive.

###### Proof.

* (i)

  We begin by verifying that the condition in Equation ([4.1](https://arxiv.org/html/2512.07787v1#S4.E1 "In item (i) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) holds.
  Since 𝑿𝒂\bm{X}^{\bm{a}} is NLOD, we have

  |  |  |  |
  | --- | --- | --- |
  |  | F𝑿𝒂​(x1,…,xn)≤∏i=1nFXiai​(xi),∀xi∈[ai,∞).F\_{\bm{X}^{\bm{a}}}(x\_{1},\dots,x\_{n})\leq\prod\_{i=1}^{n}F\_{X\_{i}^{a\_{i}}}(x\_{i}),\qquad\forall x\_{i}\in[a\_{i},\infty). |  |

  To relate this to the distribution of the shifted sum S𝒂S^{\bm{a}}, observe that the nn-box
  [a1,x1]×⋯×[an,xn][a\_{1},x\_{1}]\times\dots\times[a\_{n},x\_{n}] contains the nn-simplex with origin (a1,…,an)(a\_{1},\dots,a\_{n})
  and vertices

  |  |  |  |
  | --- | --- | --- |
  |  | {(x1,a2,…,an),(a1,x2,…,an),…,(a1,a2,…,xn)}.\{(x\_{1},a\_{2},\dots,a\_{n}),(a\_{1},x\_{2},\dots,a\_{n}),\dots,(a\_{1},a\_{2},\dots,x\_{n})\}. |  |

  Setting each xi=t+aix\_{i}=t+a\_{i} with t∈[0,∞)t\in[0,\infty) ensures that this simplex lies inside the box, and
  therefore

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | FS𝒂​(t+a+)≤F𝑿𝒂​(t+a1,…,t+an)\displaystyle F\_{S^{\bm{a}}}(t+a\_{+})\leq F\_{\bm{X}^{\bm{a}}}(t+a\_{1},\dots,t+a\_{n}) | ≤∏i=1nFXiai​(t+ai),∀t∈[0,∞),\displaystyle\leq\prod\_{i=1}^{n}F\_{X\_{i}^{a\_{i}}}(t+a\_{i}),\hskip 17.00024pt\forall t\in[0,\infty), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ⟹FS𝒂​(t+a+)\displaystyle\implies\qquad F\_{S^{\bm{a}}}(t+a\_{+}) | ≤∏i=1nFXiai​(t+ai).\displaystyle\leq\prod\_{i=1}^{n}F\_{X\_{i}^{a\_{i}}}(t+a\_{i}). |  |

  Hence the requirement in Equation ([4.1](https://arxiv.org/html/2512.07787v1#S4.E1 "In item (i) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is satisfied.
  As in Proposition [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), note that it actually suffices for 𝑿𝒂\bm{X}^{\bm{a}} to be NLOD
  only along the shifted diagonal (t+a1,…,t+an)(t+a\_{1},\dots,t+a\_{n}), since this is the only region relevant for the
  comparison with S𝒂S^{\bm{a}}.

  Next, if each function ϕiai\phi\_{i}^{a\_{i}} is non-increasing, then by
  Proposition [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), the function Φ𝒂\Phi^{\bm{a}} is SD.
  Combining this property with the continuity of each FXiaiF\_{X\_{i}^{a\_{i}}}, we may invoke
  Proposition [4.3](https://arxiv.org/html/2512.07787v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") to conclude that 𝑿𝒂\bm{X}^{\bm{a}} is VaR super-additive.
* (ii)

  The proof mirrors that of part (i).
  Using the NUOD property of 𝑿𝒃\bm{X}^{\bm{b}}, we obtain

  |  |  |  |
  | --- | --- | --- |
  |  | F¯𝑿𝒃​(x1,…,xn)≤∏i=1nF¯Xibi​(xi),∀xi∈(−∞,bi].\overline{F}\_{\bm{X}^{\bm{b}}}(x\_{1},\dots,x\_{n})\leq\prod\_{i=1}^{n}\overline{F}\_{X\_{i}^{b\_{i}}}(x\_{i}),\qquad\forall x\_{i}\in(-\infty,b\_{i}]. |  |

  In this setting, the nn-box [x1,b1]×⋯×[xn,bn][x\_{1},b\_{1}]\times\dots\times[x\_{n},b\_{n}] contains a “reversed” nn-simplex
  with origin (b1,…,bn)(b\_{1},\dots,b\_{n}) and vertices

  |  |  |  |
  | --- | --- | --- |
  |  | {(x1,b2,…,bn),(b1,x2,…,bn),…,(b1,b2,…,xn)}.\{(x\_{1},b\_{2},\dots,b\_{n}),(b\_{1},x\_{2},\dots,b\_{n}),\dots,(b\_{1},b\_{2},\dots,x\_{n})\}. |  |

  Setting xi=bi−tx\_{i}=b\_{i}-t with t∈[0,∞)t\in[0,\infty) gives

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | F¯S𝒃​(b+−t)≤F¯𝑿𝒃​(b1−t,…,bn−t)\displaystyle\overline{F}\_{S^{\bm{b}}}(b\_{+}-t)\leq\overline{F}\_{\bm{X}^{\bm{b}}}(b\_{1}-t,\dots,b\_{n}-t) | ≤∏i=1nF¯Xibi​(bi−t),∀t∈[0,∞),\displaystyle\leq\prod\_{i=1}^{n}\overline{F}\_{X\_{i}^{b\_{i}}}(b\_{i}-t),\hskip 17.00024pt\forall t\in[0,\infty), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ⟹F¯S𝒃​(b+−t)\displaystyle\implies\qquad\overline{F}\_{S^{\bm{b}}}(b\_{+}-t) | ≤∏i=1nF¯Xibi​(bi−t).\displaystyle\leq\prod\_{i=1}^{n}\overline{F}\_{X\_{i}^{b\_{i}}}(b\_{i}-t). |  |

  Thus the condition in Equation ([4.3](https://arxiv.org/html/2512.07787v1#S4.E3 "In item (ii) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) holds.
  Again, as in part (i), it suffices that the NUOD property holds only along the shifted diagonal
  (b1−t,…,bn−t)(b\_{1}-t,\dots,b\_{n}-t).

  Finally, if each ϕibi\phi\_{i}^{b\_{i}} is non-increasing, then Proposition [3.6](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") guarantees
  that Φ𝒃\Phi^{\bm{b}} is SD.
  Together with continuity of each F¯Xibi\overline{F}\_{X\_{i}^{b\_{i}}}, Proposition [4.3](https://arxiv.org/html/2512.07787v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables") implies that
  𝑿𝒃\bm{X}^{\bm{b}} is VaR sub-additive.

∎

We end this section by investigating what happens if we take measurable functions of the components of 𝑿𝒂\bm{X}^{\bm{a}} (resp. 𝑿𝒃\bm{X}^{\bm{b}}) when VaR super-additivity (resp. VaR sub-additivity) holds. The results are direct extension of those in Proposition [3.12](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem12 "Proposition 3.12. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables").

###### Proposition 4.5.

* (i)

  Suppose 𝑿𝒂\bm{X}^{\bm{a}} is NLOD with continuous margins FXiaiF\_{X\_{i}^{a\_{i}}}, and assume that each ϕiai\phi\_{i}^{a\_{i}} in Equation ([4.2](https://arxiv.org/html/2512.07787v1#S4.E2 "In item (i) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is non-increasing. Let

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑿~𝒂=(X~1a1,…,X~nan),\widetilde{\bm{X}}^{\bm{a}}=\left(\widetilde{X}\_{1}^{a\_{1}},\dots,\widetilde{X}\_{n}^{a\_{n}}\right), |  |

  where X~iai=ξi​(Xiai)\widetilde{X}\_{i}^{a\_{i}}=\xi\_{i}(X\_{i}^{a\_{i}}) for ξi:[ai,∞)→[ai,∞)\xi\_{i}:[a\_{i},\infty)\to[a\_{i},\infty). If each ξi\xi\_{i} is strictly increasing, convex, and satisfies ξi​(ai)=ai\xi\_{i}(a\_{i})=a\_{i}, then 𝑿~𝒂\widetilde{\bm{X}}^{\bm{a}} is VaR super-additive.
* (ii)

  Assume 𝑿𝒃\bm{X}^{\bm{b}} is NUOD with continuous margins F¯Xibi\overline{F}\_{X\_{i}^{b\_{i}}}, and suppose that each ϕibi\phi\_{i}^{b\_{i}} in Equation ([4.4](https://arxiv.org/html/2512.07787v1#S4.E4 "In item (ii) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is non-increasing. Define

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑿~𝒃=(X~1b1,…,X~nbn),\widetilde{\bm{X}}^{\bm{b}}=\left(\widetilde{X}\_{1}^{b\_{1}},\dots,\widetilde{X}\_{n}^{b\_{n}}\right), |  |

  where X~ibi=ξi​(Xibi)\widetilde{X}\_{i}^{b\_{i}}=\xi\_{i}(X\_{i}^{b\_{i}}) for ξi:(−∞,bi]→(−∞,bi]\xi\_{i}:(-\infty,b\_{i}]\to(-\infty,b\_{i}]. If each ξi\xi\_{i} is strictly increasing, convex, and satisfies ξi​(bi)=bi\xi\_{i}(b\_{i})=b\_{i}, then 𝑿~𝒃\widetilde{\bm{X}}^{\bm{b}} is VaR sub-additive.

###### Proof.

The argument follows the same structure as Proposition [3.12](https://arxiv.org/html/2512.07787v1#S3.Thmtheorem12 "Proposition 3.12. ‣ 3 VaR super-additivity ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"). Under the stated assumptions, two observations hold immediately:

1. •

   Since the margins FXiaiF\_{X\_{i}^{a\_{i}}} and F¯Xibi\overline{F}\_{X\_{i}^{b\_{i}}} are continuous and each ξi\xi\_{i} is strictly increasing and convex, it follows that the transformed margins FX~iaiF\_{\widetilde{X}\_{i}^{a\_{i}}} and F¯X~ibi\overline{F}\_{\widetilde{X}\_{i}^{b\_{i}}} are also continuous.
2. •

   The strict monotonicity of the mappings ξi\xi\_{i} ensures that the NLOD (resp. NUOD) property of 𝑿𝒂\bm{X}^{\bm{a}} (resp. 𝑿𝒃\bm{X}^{\bm{b}}) is preserved by the coordinate-wise transformation, so 𝑿~𝒂\widetilde{\bm{X}}^{\bm{a}} (resp. 𝑿~𝒃\widetilde{\bm{X}}^{\bm{b}}) is likewise NLOD (resp. NUOD).

Thus, it remains to verify that ϕ~iai\widetilde{\phi}\_{i}^{a\_{i}} and ϕ~ibi\widetilde{\phi}\_{i}^{b\_{i}} are non-increasing.

* (i)

  Case of ϕ~iai\widetilde{\phi}\_{i}^{a\_{i}}:
  Fix xi<yix\_{i}<y\_{i}. Then,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕ~iai​(yi)\displaystyle\widetilde{\phi}\_{i}^{a\_{i}}(y\_{i}) | =yi​log⁡FX~iai​(yi+ai)\displaystyle=y\_{i}\log F\_{\widetilde{X}\_{i}^{a\_{i}}}(y\_{i}+a\_{i}) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =yi​log⁡FXiai​(ξi−1​(yi+ai)).\displaystyle=y\_{i}\log F\_{X\_{i}^{a\_{i}}}\left(\xi\_{i}^{-1}(y\_{i}+a\_{i})\right). |  |

  Applying the non-increasing property of ϕiai\phi\_{i}^{a\_{i}} to the strictly increasing pair

  |  |  |  |
  | --- | --- | --- |
  |  | ξi−1​(xi+ai)−ai<ξi−1​(yi+ai)−ai\xi\_{i}^{-1}(x\_{i}+a\_{i})-a\_{i}<\xi\_{i}^{-1}(y\_{i}+a\_{i})-a\_{i} |  |

  yields

  |  |  |  |
  | --- | --- | --- |
  |  | ϕ~iai​(yi)≤yi​ξi−1​(xi+ai)−aiξi−1​(yi+ai)−ai​log⁡FXiai​(ξi−1​(xi+ai)).\widetilde{\phi}\_{i}^{a\_{i}}(y\_{i})\leq y\_{i}\frac{\xi\_{i}^{-1}(x\_{i}+a\_{i})-a\_{i}}{\xi\_{i}^{-1}(y\_{i}+a\_{i})-a\_{i}}\log F\_{X\_{i}^{a\_{i}}}(\xi\_{i}^{-1}(x\_{i}+a\_{i})). |  |

  Next, the convexity of ξi\xi\_{i} and the condition ξi​(ai)=ai\xi\_{i}(a\_{i})=a\_{i} imply that the secant slopes from aia\_{i} are non-decreasing: for all ai<ui<via\_{i}<u\_{i}<v\_{i},

  |  |  |  |
  | --- | --- | --- |
  |  | ξi​(ui)−aiui−ai≤ξi​(vi)−aivi−ai.\frac{\xi\_{i}(u\_{i})-a\_{i}}{u\_{i}-a\_{i}}\leq\frac{\xi\_{i}(v\_{i})-a\_{i}}{v\_{i}-a\_{i}}. |  |

  With ui=ξi−1​(xi+ai)u\_{i}=\xi\_{i}^{-1}(x\_{i}+a\_{i}) and vi=ξi−1​(yi+ai)v\_{i}=\xi\_{i}^{-1}(y\_{i}+a\_{i}), this becomes

  |  |  |  |
  | --- | --- | --- |
  |  | xiξi−1​(xi+ai)−ai≤yiξi−1​(yi+ai)−ai,\frac{x\_{i}}{\xi\_{i}^{-1}(x\_{i}+a\_{i})-a\_{i}}\leq\frac{y\_{i}}{\xi\_{i}^{-1}(y\_{i}+a\_{i})-a\_{i}}, |  |

  which is equivalent to

  |  |  |  |
  | --- | --- | --- |
  |  | xi≤yi​ξi−1​(xi+ai)−aiξi−1​(yi+ai)−ai.x\_{i}\leq y\_{i}\frac{\xi\_{i}^{-1}(x\_{i}+a\_{i})-a\_{i}}{\xi\_{i}^{-1}(y\_{i}+a\_{i})-a\_{i}}. |  |

  Since log∘FXiai\log\circ F\_{X\_{i}^{a\_{i}}} is negative, combining the inequalities gives

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕ~iai​(yi)\displaystyle\widetilde{\phi}\_{i}^{a\_{i}}(y\_{i}) | ≤yi​ξi−1​(xi+ai)−aiξi−1​(yi+ai)−ai​log⁡FXiai​(ξi−1​(xi+ai))\displaystyle\leq y\_{i}\frac{\xi\_{i}^{-1}(x\_{i}+a\_{i})-a\_{i}}{\xi\_{i}^{-1}(y\_{i}+a\_{i})-a\_{i}}\log F\_{X\_{i}^{a\_{i}}}(\xi\_{i}^{-1}(x\_{i}+a\_{i})) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤xi​log⁡FXiai​(ξi−1​(xi+ai))=ϕ~iai​(xi).\displaystyle\leq x\_{i}\log F\_{X\_{i}^{a\_{i}}}(\xi\_{i}^{-1}(x\_{i}+a\_{i}))=\widetilde{\phi}\_{i}^{a\_{i}}(x\_{i}). |  |

  Hence, ϕ~iai\widetilde{\phi}\_{i}^{a\_{i}} in ([4.2](https://arxiv.org/html/2512.07787v1#S4.E2 "In item (i) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is non-increasing on [0,∞)[0,\infty).
  By Proposition [4.4](https://arxiv.org/html/2512.07787v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), we conclude that 𝑿~𝒂\widetilde{\bm{X}}^{\bm{a}} is VaR super-additive.
* (ii)

  Case of ϕ~ibi\widetilde{\phi}\_{i}^{b\_{i}}: An analogous argument applies. Let xi<yix\_{i}<y\_{i}. Then

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕ~ibi​(yi)\displaystyle\widetilde{\phi}\_{i}^{b\_{i}}(y\_{i}) | =yi​log⁡F¯X~ibi​(bi−yi)\displaystyle=y\_{i}\log\overline{F}\_{\widetilde{X}\_{i}^{b\_{i}}}(b\_{i}-y\_{i}) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =yi​log⁡F¯Xibi​(ξi−1​(bi−yi)).\displaystyle=y\_{i}\log\overline{F}\_{X\_{i}^{b\_{i}}}\bigl(\xi\_{i}^{-1}(b\_{i}-y\_{i})\bigr). |  |

  Applying the non-increasing property of ϕibi\phi\_{i}^{b\_{i}} to the strictly increasing pair

  |  |  |  |
  | --- | --- | --- |
  |  | bi−ξi−1​(bi−xi)<bi−ξi−1​(bi−yi)b\_{i}-\xi\_{i}^{-1}(b\_{i}-x\_{i})<b\_{i}-\xi\_{i}^{-1}(b\_{i}-y\_{i}) |  |

  gives

  |  |  |  |
  | --- | --- | --- |
  |  | ϕ~ibi​(yi)≤yi​bi−ξi−1​(bi−xi)bi−ξi−1​(bi−yi)​log⁡F¯Xibi​(ξi−1​(bi−xi)).\widetilde{\phi}\_{i}^{b\_{i}}(y\_{i})\leq y\_{i}\frac{b\_{i}-\xi\_{i}^{-1}(b\_{i}-x\_{i})}{\,b\_{i}-\xi\_{i}^{-1}(b\_{i}-y\_{i})}\log\overline{F}\_{X\_{i}^{b\_{i}}}\bigl(\xi\_{i}^{-1}(b\_{i}-x\_{i})\bigr). |  |

  Furthermore, convexity of ξi\xi\_{i} and the constraint ξi​(bi)=bi\xi\_{i}(b\_{i})=b\_{i} imply that secant slopes from bib\_{i} are non-decreasing: for ui<vi<biu\_{i}<v\_{i}<b\_{i},

  |  |  |  |
  | --- | --- | --- |
  |  | bi−ξi​(ui)bi−ui≤bi−ξi​(vi)bi−vi.\frac{b\_{i}-\xi\_{i}(u\_{i})}{b\_{i}-u\_{i}}\leq\frac{b\_{i}-\xi\_{i}(v\_{i})}{b\_{i}-v\_{i}}. |  |

  Substituting ui=ξi−1​(bi−xi)u\_{i}=\xi\_{i}^{-1}(b\_{i}-x\_{i}) and vi=ξi−1​(bi−yi)v\_{i}=\xi\_{i}^{-1}(b\_{i}-y\_{i}) yields

  |  |  |  |
  | --- | --- | --- |
  |  | xibi−ξi−1​(bi−xi)≤yibi−ξi−1​(bi−yi),\frac{x\_{i}}{b\_{i}-\xi\_{i}^{-1}(b\_{i}-x\_{i})}\leq\frac{y\_{i}}{b\_{i}-\xi\_{i}^{-1}(b\_{i}-y\_{i})}, |  |

  which is equivalent to

  |  |  |  |
  | --- | --- | --- |
  |  | xi≤yi​bi−ξi−1​(bi−xi)bi−ξi−1​(bi−yi).x\_{i}\leq y\_{i}\frac{b\_{i}-\xi\_{i}^{-1}(b\_{i}-x\_{i})}{b\_{i}-\xi\_{i}^{-1}(b\_{i}-y\_{i})}. |  |

  Since log∘F¯Xibi\log\circ\overline{F}\_{X\_{i}^{b\_{i}}} is negative, we conclude

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ϕ~ibi​(yi)\displaystyle\widetilde{\phi}\_{i}^{b\_{i}}(y\_{i}) | ≤yi​bi−ξi−1​(bi−xi)bi−ξi−1​(bi−yi)​log⁡F¯Xibi​(ξi−1​(bi−xi))\displaystyle\leq y\_{i}\frac{b\_{i}-\xi\_{i}^{-1}(b\_{i}-x\_{i})}{b\_{i}-\xi\_{i}^{-1}(b\_{i}-y\_{i})}\log\overline{F}\_{X\_{i}^{b\_{i}}}\bigl(\xi\_{i}^{-1}(b\_{i}-x\_{i})\bigr) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤xi​log⁡F¯Xibi​(ξi−1​(bi−xi))=ϕ~ibi​(xi).\displaystyle\leq x\_{i}\log\overline{F}\_{X\_{i}^{b\_{i}}}\bigl(\xi\_{i}^{-1}(b\_{i}-x\_{i})\bigr)=\widetilde{\phi}\_{i}^{b\_{i}}(x\_{i}). |  |

  Thus ϕ~ibi\widetilde{\phi}\_{i}^{b\_{i}} in ([4.4](https://arxiv.org/html/2512.07787v1#S4.E4 "In item (ii) ‣ Proposition 4.3. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables")) is non-increasing on [0,∞)[0,\infty), and by Proposition [4.4](https://arxiv.org/html/2512.07787v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4 Further Generalizations and Remarks ‣ VaR at Its Extremes: Impossibilities and Conditions for One-Sided Random Variables"), 𝑿~𝒃\widetilde{\bm{X}}^{\bm{b}} is VaR sub-additive.

∎

## 5 Conclusions

This paper provides a comprehensive characterization of the extremal aggregation behavior of Value-at-Risk for sums of one-sided random variables. We first established an impossibility result: for risks supported on [0,∞)[0,\infty), VaR sub-additivity can arise only through exact additivity – a phenomenon exclusive to co-monotonic vectors. On the opposite end of the spectrum, we developed a general and flexible framework for full VaR super-additivity. The key insight is that super-additivity does not follow from dependence or marginal structure in isolation, but from their joint interaction as captured by the NSD and SD conditions. These conditions unify and extend existing results in the literature, while accommodating non-identical margins and a diverse range of negative dependence structures.
  
  
We further showed that the theory remains robust under shifts, reflections, and monotone convex transformations of the components, and that analogous principles govern aggregation when the random variables have arbitrary finite endpoints. Taken together, the results reveal a sharp dichotomy: in lower-bounded settings, VaR is structurally incompatible with sub-additivity yet naturally exhibits super-additivity under suitable dependence–margin configurations, whereas the pattern is reversed in upper-bounded settings. This characterization not only clarifies the conditions under which VaR behaves as a diversification-averse or diversification-seeking risk measure, but also offers practical criteria for detecting such behavior in applications involving heavy tails or negatively dependent risks.