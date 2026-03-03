---
authors:
- Ruodu Wang
- Jingcheng Yu
doc_id: arxiv:2603.01232v1
family_id: arxiv:2603.01232
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Submodular risk measures
url_abs: http://arxiv.org/abs/2603.01232v1
url_html: https://arxiv.org/html/2603.01232v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ruodu Wang
Department of Statistics and Actuarial Science, University of Waterloo, Canada. ✉ [wang@uwaterloo.ca](2603.01232v1/wang@uwaterloo.ca)
  
Jingcheng Yu
Department of Statistics and Actuarial Science, University of Waterloo, Canada. ✉ [j563yu@uwaterloo.ca](2603.01232v1/j563yu@uwaterloo.ca)

###### Abstract

We study submodularity for law-invariant functionals, with special attention to convex risk measures. Expected losses are modular, and certainty equivalents are submodular if and only if the underlying loss function is convex. Law-invariant coherent risk measures are submodular if and only if they are coherent distortion risk measures, which include the class of Expected Shortfall (ES).
We proceed to consider four classes of convex risk measures with explicit formulas.
For shortfall risk measures, we give a complete characterization through an inequality on the Arrow–Pratt measure of risk aversion. The optimized certainty equivalents are always submodular, whereas for the adjusted Expected Shortfall (AES) with a nonconvex penalty function, submodularity forces reduction to a standard ES. Within a subclass of monotone mean-deviation risk measures, submodularity can hold only in coherent distortion cases. In an empirical study of daily US equity returns using rolling historical estimation, no ES submodularity violations are observed, as expected from the exact ES structure of the estimator; VaR shows persistent violations linked to market stress, and AES shows a small percentage of violations.

Keywords: Law-invariant risk measures; submodularity; shortfall risk measures; linear dominance inequality; optimized certainty equivalent; distortion risk measures; empirical analysis.

## 1 Introduction

Submodularity is an important property in mathematics, optimization, economics, and data science, with particular applications in modeling transport costs, dependence, cooperative games, and social production functions.
Without being exhaustive at all, we refer to Marinacci and Montrucchio ([2004](#bib.bib15 "Introduction to the mathematics of ambiguity")) for submodularity (as well as its counterpart, supermodularity) in decision theory, to Rüschendorf ([2013](#bib.bib19 "Mathematical risk analysis. dependence, risk bounds, optimal allocations and portfolios")) for its roles in quantitative risk management, and to Bilmes ([2022](#bib.bib6 "Submodularity in machine learning and artificial intelligence")) for its roles in machine learning and artificial intelligence.

For a lattice ℒ\mathcal{L} equipped with the maximum operator ∨\vee and the minimum operator ∧\wedge, submodularity of a function f:ℒ→ℝf:\mathcal{L}\to\mathbb{R} means

|  |  |  |
| --- | --- | --- |
|  | f​(X∨Y)+f​(X∧Y)≤f​(X)+f​(Y)​ for all X,Y∈ℒ.f(X\vee Y)+f(X\wedge Y)\leq f(X)+f(Y)\mbox{~~~for all $X,Y\in\mathcal{L}$.} |  |

A common appearance of submodularity is in the context of capacities. A capacity on a σ\sigma-algebra ℱ\mathcal{F} is an increasing function v:ℱ→ℝv:\mathcal{F}\to\mathbb{R} with v​(∅)=0v(\varnothing)=0, and
it is submodular if v​(A∪B)+v​(A∩B)≤v​(A)+v​(B)v(A\cup B)+v(A\cap B)\leq v(A)+v(B) for all A,B∈ℱA,B\in\mathcal{F}, which corresponds to (ℒ,∨,∧)=(ℱ,∪,∩)(\mathcal{L},\vee,\wedge)=(\mathcal{F},\cup,\cap).

Although submodularity is popular in many fields, its relevance for risk measures has received limited attention. There is, however, a well-known connection: A comonotonic-additive and coherent risk measure must be a Choquet integral with respect to a submodular capacity; see Theorem 4.94 of Föllmer and Schied ([2016](#bib.bib11 "Stochastic finance. an introduction in discrete time")).

A major advance was made by Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")), who obtained a remarkable characterization of submodular functions under positive homogeneity and cash invariance (also known as constant additivity).
Translating this result into the language of risk measures, it says that submodular, positively homogeneous, and monetary risk measures must be coherent and comonotonic-additive.
This includes the Expected Shortfall (ES), the standard risk measure for market risk in the banking industry; see e.g., McNeil et al. ([2015](#bib.bib3 "Quantitative risk management: concepts, techniques and tools-revised edition")).
The main purpose of this paper is a systematic study of submodularity in the context of risk measures.

To characterize submodularity, we start in Section [3](#S3 "3 Expected losses and distortion risk measures ‣ Submodular risk measures") with three classes of functionals that are common in decision theory and risk management: expected losses, certainty equivalents, and coherent risk measures. For these classes, submodularity is relatively straightforward to characterize. Specifically, expected losses are the only law-invariant functionals that are modular.
Certainty equivalents are submodular if and only if the corresponding loss function is convex. Directly following from the results of Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")), for coherent risk measures, submodularity is equivalent to comonotonic additivity. This was a surprising fact obtained by Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")), as in general these two properties are quite different.

Marinacci and Montrucchio ([2008](#bib.bib16 "On concavity and supermodularity")) showed that for cash-invariant (constant-additive) risk measures on a finite space, submodularity implies convexity.
Since commonly used risk measures are cash invariant, we will mostly focus on risk measures that are convex.
In Section [4](#S4 "4 Four classes of convex risk measures ‣ Submodular risk measures"),
we study submodularity in four classes of convex monetary risk measures that have explicit formulas: the shortfall risk measures (Föllmer and Schied, [2002](#bib.bib9 "Convex measures of risk and trading constraints")), the optimized certainty equivalents (OCE) (Ben-Tal and Teboulle, [2007](#bib.bib5 "An old-new concept of convex risk measures: the optimized certainty equivalent")), adjusted Expected Shortfall (AES) (Burzoni et al., [2022](#bib.bib7 "Adjusted Expected Shortfall")), and the monotone mean-deviation measures (Han et al., [2026](#bib.bib14 "Monotonic mean-deviation risk measures")).
It turns out that, except for the case of OCE which is simpler, the other three classes all require quite sophisticated analysis to characterize submodularity.
For shortfall risk measures, submodularity concerns an inequality on the Arrow–Pratt measure of risk aversion. The optimized certainty equivalents are always submodular.
AES with a nonconvex adjustment function can only be submodular when it equals a standard ES, and we conjecture that for convex adjustment profiles submodularity leads to a reduction to ES up to a constant. For monotone mean-deviation risk measures generated by a distortion risk measure, submodularity can hold only when it is a coherent distortion risk measure.

We proceed in Section [5](#S5 "5 Discussion: Submodularity on sets ‣ Submodular risk measures") with some discussions on a related notion of submodularity studied by Ghamami and Glasserman ([2019](#bib.bib10 "Submodular risk allocation")).
Empirical results based on financial data are presented in Section [6](#S6 "6 Submodularity in financial data ‣ Submodular risk measures"), verifying some violations of submodularity for VaR and AES.
Section [7](#S7 "7 Conclusion ‣ Submodular risk measures") concludes the paper.

## 2 Choquet integrals and risk measures

We work with an atomless probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), and L∞L^{\infty} is the set of all bounded random variables on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), with L∞L^{\infty}-norm ‖X‖∞=inf{x∈ℝ:ℙ​(X>x)=0}\|X\|\_{\infty}=\inf\{x\in\mathbb{R}:\mathbb{P}(X>x)=0\}.
We treat almost surely equal random variables as identical.
Elements of L∞L^{\infty} are interpreted as random financial losses.
Two random variables XX and YY are called *comonotonic* if (X​(ω)−X​(ω′))​(Y​(ω)−Y​(ω′))≥0(X(\omega)-X(\omega^{\prime}))(Y(\omega)-Y(\omega^{\prime}))\geq 0 for all ω,ω′∈Ω\omega,\omega^{\prime}\in\Omega (ℙ×ℙ\mathbb{P}\times\mathbb{P} almost surely). We write X=dYX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y if XX and YY are equally distributed under ℙ\mathbb{P}.

A risk measure is a mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R}, and it may satisfy the following commonly studied properties.

1. (a)

   Monotonicity: ρ​(X)≤ρ​(Y)\rho(X)\leq\rho(Y) for X,Y∈L∞X,Y\in L^{\infty} with X≤YX\leq Y.
2. (b)

   Cash invariance (constant additivity): ρ​(X+c)=ρ​(X)+c\rho(X+c)=\rho(X)+c for X∈L∞X\in L^{\infty} and c∈ℝc\in\mathbb{R}.
3. (c)

   Convexity: ρ​(λ​X+(1−λ)​Y)≤λ​ρ​(X)+(1−λ)​ρ​(Y)\rho(\lambda X+(1-\lambda)Y)\leq\lambda\rho(X)+(1-\lambda)\rho(Y) for X,Y∈L∞X,Y\in L^{\infty} and λ∈[0,1]\lambda\in[0,1].
4. (d)

   Positive homogeneity: ρ​(λ​X)=λ​ρ​(X)\rho(\lambda X)=\lambda\rho(X) for X∈L∞X\in L^{\infty} and λ>0\lambda>0.
5. (e)

   Subadditivity: ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y) for X,Y∈L∞X,Y\in L^{\infty}.
6. (f)

   Comonotonic additivity: ρ​(X+Y)=ρ​(X)+ρ​(Y)\rho(X+Y)=\rho(X)+\rho(Y) for comonotonic X,Y∈L∞X,Y\in L^{\infty}.
7. (g)

   Law invariance: ρ​(X)=ρ​(Y)\rho(X)=\rho(Y) when X=dYX\mathrel{\mathop{\kern 0.0pt=}\limits^{\mathrm{d}}}Y.

Following the standard terminology in the literature, a *monetary risk measure* is a mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} satisfying (a) and (b);
a *convex risk measure* is a mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} satisfying (a)–(c);
a *coherent risk measure* is a mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} satisfying (a)–(d).
Note that convexity (c) and subadditivity (e) are equivalent under positive homogeneity (d).
Any monetary risk measure is automatically 11-Lipschitz with respect to L∞L^{\infty}-norm, and hence continuous. For more background and many properties of risk measures, see Föllmer and Schied ([2016](#bib.bib11 "Stochastic finance. an introduction in discrete time")).

As explained in the introduction, our main point of interest is the *submodularity* of ρ\rho, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X∨Y)+ρ​(X∧Y)≤ρ​(X)+ρ​(Y)​ for all X,Y∈L∞.\rho(X\vee Y)+\rho(X\wedge Y)\leq\rho(X)+\rho(Y)\mbox{~~~for all $X,Y\in L^{\infty}$}. |  | (1) |

Here, x∨y=max⁡{x,y}x\vee y=\max\{x,y\} and x∧y=min⁡{x,y}x\wedge y=\min\{x,y\} for x,y∈ℝx,y\in\mathbb{R}, and they are applied pointwise to random variables.
Moreover, we say that ρ\rho is *supermodular* if −ρ-\rho is submodular. That is, the inequality in ([1](#S2.E1 "In 2 Choquet integrals and risk measures ‣ Submodular risk measures")) is reversed.

It is straightforward to verify that submodular functions are closed under some simple operations.
For instance,
let ρ,ρ′:L∞→ℝ\rho,\rho^{\prime}:L^{\infty}\to\mathbb{R} be submodular functions. The mappings λ​ρ\lambda\rho for λ≥0\lambda\geq 0, ρ+c\rho+c for c∈ℝc\in\mathbb{R}, and ρ+ρ′\rho+\rho^{\prime} are submodular. Similarly, any convex combination of
a class {ρθ:θ∈Θ}\{\rho\_{\theta}:\theta\in\Theta\} of submodular risk measures is submodular.

We next review the results of Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")) that submodular risk measures are closely related to Choquet integrals.
Let VV be the set of mappings v:ℱ→ℝv:\mathcal{F}\to\mathbb{R} with bounded variation and v​(∅)=0v(\varnothing)=0. Here, by the variation of vv we mean
the norm

|  |  |  |
| --- | --- | --- |
|  | ∥v∥=sup{∑k=1n|v(Ak)−v(Ak−1)|:n∈ℕ;∅=A0⊆A1⊆⋯⊆An=Ω},\|v\|=\sup\left\{\sum\_{k=1}^{n}|v(A\_{k})-v(A\_{k-1})|:n\in\mathbb{N};~\varnothing=A\_{0}\subseteq A\_{1}\subseteq\dots\subseteq A\_{n}=\Omega\right\}, |  |

which is always finite if vv is increasing.
For X∈L∞X\in L^{\infty} and v∈Vv\in V, the *Choquet integral* ∫X​dv\int X\mathrm{d}v is defined as

|  |  |  |
| --- | --- | --- |
|  | ∫X​dv=∫0∞v​(X>x)​dx+∫−∞0(v​(X>x)−v​(Ω))​dx.\int X\mathrm{d}v=\int\_{0}^{\infty}v(X>x)\mathrm{d}x+\int\_{-\infty}^{0}\left(v(X>x)-v(\Omega)\right)\mathrm{d}x. |  |

We say that a mapping ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} is *Choquet* if it can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)=∫X​dv,X∈L∞\rho(X)=\int X\mathrm{d}v,~~~X\in L^{\infty} |  | (2) |

for some v∈Vv\in V.
Following Embrechts et al. ([2021](#bib.bib2 "Bayes risk, elicitability, and the expected shortfall")), monetary risk measures satisfying ([2](#S2.E2 "In 2 Choquet integrals and risk measures ‣ Submodular risk measures")) are called *Choquet risk measures*, for which the function vv in ([2](#S2.E2 "In 2 Choquet integrals and risk measures ‣ Submodular risk measures")) is a capacity with v​(Ω)=1v(\Omega)=1.
As the most important class of Choquet risk measures, the ES at level p∈(0,1)p\in(0,1) is

|  |  |  |
| --- | --- | --- |
|  | ESp​(X)=11−p​∫p1VaRq​(X)​dq,X∈L∞,\mathrm{ES}\_{p}(X)=\frac{1}{1-p}\int\_{p}^{1}\mathrm{VaR}\_{q}(X)\,\mathrm{d}q,\qquad X\in L^{\infty}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | VaRq​(X)=inf{x∈ℝ:ℙ​(X≤x)≥q}\mathrm{VaR}\_{q}(X)=\inf\{x\in\mathbb{R}:\mathbb{P}(X\leq x)\geq q\} |  |

is known as the Value-at-Risk of XX at level q∈(0,1)q\in(0,1), also the left quantile of XX at qq.
Both ESp\mathrm{ES}\_{p} and VaRp\mathrm{VaR}\_{p} are Choquet risk measures and their capacities vv in ([2](#S2.E2 "In 2 Choquet integrals and risk measures ‣ Submodular risk measures")) are given by v=ϕ∘ℙv=\phi\circ\mathbb{P}
for a function ϕ:[0,1]→[0,1]\phi:[0,1]\to[0,1] given by ϕ​(t)=min⁡{t/(1−p),1}\phi(t)=\min\{t/(1-p),1\} and ϕ​(t)=𝟙{t>1−p}\phi(t)=\mathds{1}\_{\{t>1-p\}}, respectively.
It is well known that a Choquet mapping is comonotonic-additive and norm-continuous.
Moreover, comonotonic additivity and monotonicity characterize monotone Choquet functionals (Schmeidler, [1986](#bib.bib20 "Integral representation without additivity")).

Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")) showed that a risk measure ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} is submodular, positively homogeneous, and monetary if and only if ρ\rho is a Choquet coherent risk measure.
Therefore, for monetary risk measures that are positively homogeneous, submodularity is fully characterized by comonotonic additivity and subadditivity. This result is a bit surprising as neither subadditivity nor comonotonic additivity follows from submodularity alone (which will be illustrated by many examples in this paper), and the other properties also do not imply subadditivity nor comonotonic additivity.

This observation inspired us to wonder what happens when we assume submodularity but not positive homogeneity.
Marinacci and Montrucchio ([2008](#bib.bib16 "On concavity and supermodularity")) proved that under mild conditions on the underlying space, submodularity and cash invariance imply convexity.
Therefore, we will direct our main attention to convex risk measures in our analysis.
In particular, we will consider law-invariant convex risk measures that have explicit formulas.

## 3 Expected losses and distortion risk measures

We will first investigate the expected loss functionals and distortion risk measures.
In decision theory, these functionals represent the expected utility theory and the dual utility theory of Yaari ([1987](#bib.bib23 "The dual theory of choice under risk")), two very popular decision models.

### 3.1 Expected losses

An expected loss is the mapping

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eℓ​(X)=𝔼​[ℓ​(X)],X∈L∞,\displaystyle E\_{\ell}(X)=\mathbb{E}[\ell(X)],~~~~X\in L^{\infty}, |  | (3) |

where ℓ:ℝ→ℝ\ell:\mathbb{R}\to\mathbb{R} is a measurable function, which we call a loss function.
This is analogous to the expected utility for a utility function u:ℝ→ℝu:\mathbb{R}\to\mathbb{R} in decision theory, with the difference that our random variables in L∞L^{\infty} represent losses.
Note that ℓ​(X)\ell(X) is not necessarily in the same unit as XX.
The following result gives a simple characterization of law-invariant functionals that are modular (both submodular and supermodular).

###### Theorem 1.

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be an atomless probability space and ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} be law-invariant and
∥⋅∥∞\|\cdot\|\_{\infty}-continuous.
Then the following are equivalent:

1. (i)

   ρ\rho is both submodular and supermodular.
2. (ii)

   There exists a continuous function ℓ:ℝ→ℝ\ell:\mathbb{R}\to\mathbb{R} such that
   ρ=Eℓ\rho=E\_{\ell}.

###### Proof.

(ii)⇒\Rightarrow(i):
The pointwise identity ℓ​(a)+ℓ​(b)=ℓ​(max⁡(a,b))+ℓ​(min⁡(a,b))\ell(a)+\ell(b)=\ell(\max(a,b))+\ell(\min(a,b)) gives
Eℓ​(X)+Eℓ​(Y)=Eℓ​(X∨Y)+Eℓ​(X∧Y)E\_{\ell}(X)+E\_{\ell}(Y)=E\_{\ell}(X\vee Y)+E\_{\ell}(X\wedge Y).

(i)⇒\Rightarrow(ii):
Since ρ\rho is both submodular and supermodular, it is called a *valuation*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)+ρ​(Y)=ρ​(X∨Y)+ρ​(X∧Y),∀X,Y∈L∞.\rho(X)+\rho(Y)=\rho(X\vee Y)+\rho(X\wedge Y),\qquad\forall\,X,Y\in L^{\infty}. |  | (4) |

Define ℓ​(x)=ρ​(x​𝟙Ω)\ell(x)=\rho(x\mathds{1}\_{\Omega}).
Without loss of generality, assume ρ​(0)=ℓ​(0)=0\rho(0)=\ell(0)=0. Note that ℓ\ell is continuous since ρ\rho is ∥⋅∥∞\|\cdot\|\_{\infty}-continuous and ‖x​𝟙Ω−y​𝟙Ω‖∞=|x−y|\|x\mathds{1}\_{\Omega}-y\mathds{1}\_{\Omega}\|\_{\infty}=|x-y|.

Fix a>ba>b. For t∈[0,1]t\in[0,1], choose A∈ℱA\in\mathcal{F} with ℙ​(A)=t\mathbb{P}(A)=t and set

|  |  |  |
| --- | --- | --- |
|  | ψ​(t)=ρ​(a​𝟙A+b​𝟙Ac),\psi(t)=\rho(a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}}), |  |

which is well-defined by law-invariance. For s,t≥0s,t\geq 0 with s+t≤1s+t\leq 1, choose disjoint A,BA,B with ℙ​(A)=t\mathbb{P}(A)=t, ℙ​(B)=s\mathbb{P}(B)=s. Setting X=a​𝟙A+b​𝟙AcX=a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}} and Y=a​𝟙B+b​𝟙BcY=a\mathds{1}\_{B}+b\mathds{1}\_{B^{c}}, we have X∧Y=bX\wedge Y=b and X∨Y=a​𝟙A∪B+b​𝟙(A∪B)cX\vee Y=a\mathds{1}\_{A\cup B}+b\mathds{1}\_{(A\cup B)^{c}}, so ([4](#S3.E4 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(t+s)=φ​(t)+φ​(s),s,t≥0,s+t≤1,\varphi(t+s)=\varphi(t)+\varphi(s),\qquad s,t\geq 0,\;s+t\leq 1, |  | (5) |

where φ​(t)=ψ​(t)−ψ​(0)\varphi(t)=\psi(t)-\psi(0). The family {a​𝟙A+b​𝟙Ac:A∈ℱ}\{a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}}:A\in\mathcal{F}\} is order-bounded in L∞L^{\infty}; indeed, with m=max⁡(|a|,|b|)m=\max(|a|,|b|),

|  |  |  |
| --- | --- | --- |
|  | −m​𝟙Ω≤a​𝟙A+b​𝟙Ac≤m​𝟙Ω,A∈ℱ,-m\mathds{1}\_{\Omega}\leq a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}}\leq m\mathds{1}\_{\Omega},\qquad A\in\mathcal{F}, |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | ‖a​𝟙A+b​𝟙Ac‖∞≤max⁡(|a|,|b|),A∈ℱ.\|a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}}\|\_{\infty}\leq\max(|a|,|b|),\qquad A\in\mathcal{F}. |  |

Since ρ\rho is a ∥⋅∥∞\|\cdot\|\_{\infty}-continuous valuation on the Banach lattice L∞L^{\infty}, it is bounded on order-bounded sets (Tradacete and Villanueva, [2020](#bib.bib21 "Valuations on Banach lattices"), Proposition 3.2). Hence ψ\psi is bounded on [0,1][0,1], and so is φ\varphi. Let M=supu∈[0,1]|φ​(u)|<∞M=\sup\_{u\in[0,1]}|\varphi(u)|<\infty. For any u∈[0,1/n]u\in[0,1/n], ([5](#S3.E5 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")) gives φ​(n​u)=n​φ​(u)\varphi(nu)=n\varphi(u) and thus |φ​(u)|≤M/n|\varphi(u)|\leq M/n, so φ\varphi is continuous at 0. By ([5](#S3.E5 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")), continuity at 0 implies continuity on [0,1][0,1], and φ​(q)=q​φ​(1)\varphi(q)=q\varphi(1) for rational q∈[0,1]q\in[0,1]. Therefore, by density of rationals, φ​(t)=t​φ​(1)\varphi(t)=t\varphi(1) for all t∈[0,1]t\in[0,1]. Equivalently, φ\varphi is additive and bounded on an interval, and hence linear on [0,1][0,1]. Therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(a​𝟙A+b​𝟙Ac)=(1−t)​ℓ​(b)+t​ℓ​(a)=Eℓ​(a​𝟙A+b​𝟙Ac).\rho(a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}})=(1-t)\ell(b)+t\ell(a)=E\_{\ell}(a\mathds{1}\_{A}+b\mathds{1}\_{A^{c}}). |  | (6) |

Now let X=∑i=1nxi​𝟙AiX=\sum\_{i=1}^{n}x\_{i}\mathds{1}\_{A\_{i}} be simple with x1>⋯>xnx\_{1}>\cdots>x\_{n} and ti=ℙ​(Ai)t\_{i}=\mathbb{P}(A\_{i}). We show by induction on nn that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)=Eℓ​(X).\rho(X)=E\_{\ell}(X). |  | (7) |

The case n=1n=1 is the definition of ℓ\ell, and n=2n=2 is ([6](#S3.E6 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")). For the inductive step, define Y=x2​𝟙A1+x1​𝟙A1cY=x\_{2}\mathds{1}\_{A\_{1}}+x\_{1}\mathds{1}\_{A\_{1}^{c}} (a two-valued random variable). Then X∨Y=x1X\vee Y=x\_{1} and X∧Y=x2​𝟙A1∪A2+∑i=3nxi​𝟙AiX\wedge Y=x\_{2}\mathds{1}\_{A\_{1}\cup A\_{2}}+\sum\_{i=3}^{n}x\_{i}\mathds{1}\_{A\_{i}}, which takes n−1n-1 distinct values. Applying ([4](#S3.E4 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")),

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=ℓ​(x1)+ρ​(X∧Y)−ρ​(Y).\rho(X)=\ell(x\_{1})+\rho(X\wedge Y)-\rho(Y). |  |

By the induction hypothesis and ([6](#S3.E6 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")),

|  |  |  |
| --- | --- | --- |
|  | ρ​(X∧Y)=(t1+t2)​ℓ​(x2)+∑i=3nti​ℓ​(xi),ρ​(Y)=(1−t1)​ℓ​(x1)+t1​ℓ​(x2),\rho(X\wedge Y)=(t\_{1}+t\_{2})\ell(x\_{2})+\sum\_{i=3}^{n}t\_{i}\ell(x\_{i}),\qquad\rho(Y)=(1-t\_{1})\ell(x\_{1})+t\_{1}\ell(x\_{2}), |  |

and substituting yields ([7](#S3.E7 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")).

Finally, for general X∈L∞X\in L^{\infty}, let Xk=2−k​⌊2k​X⌋X\_{k}=2^{-k}\lfloor 2^{k}X\rfloor. Then ‖Xk−X‖∞≤2−k\|X\_{k}-X\|\_{\infty}\leq 2^{-k}, so ρ​(Xk)→ρ​(X)\rho(X\_{k})\to\rho(X) by ∥⋅∥∞\|\cdot\|\_{\infty}-continuity. By ([7](#S3.E7 "In Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")), ρ​(Xk)=Eℓ​(Xk)\rho(X\_{k})=E\_{\ell}(X\_{k}). Since ℓ​(Xk)→ℓ​(X)\ell(X\_{k})\to\ell(X) almost surely and is uniformly bounded, dominated convergence gives Eℓ​(Xk)→Eℓ​(X)E\_{\ell}(X\_{k})\to E\_{\ell}(X), hence ρ​(X)=Eℓ​(X)\rho(X)=E\_{\ell}(X).
∎

### 3.2 On certainty equivalents with respect to expected losses

The certainty equivalents are a popular object in decision theory that play a similar role to risk measures. They are not monetary risk measures as they do not satisfy cash invariance in general, but they satisfy the property ρ​(c)=c\rho(c)=c for all c∈ℝc\in\mathbb{R}, so that the input and output are both the monetary scale.

Let ℓ:ℝ→ℝ\ell:\mathbb{R}\to\mathbb{R} be a strictly increasing function, and define its generalized inverse by

|  |  |  |
| --- | --- | --- |
|  | ℓ−1​(y)=inf{x∈ℝ:ℓ​(x)≥y},y∈ℝ.\ell^{-1}(y)=\inf\{x\in\mathbb{R}:\ell(x)\geq y\},\qquad y\in\mathbb{R}. |  |

The certainty equivalent (CE) with respect to the loss function ℓ\ell is given by the mapping

|  |  |  |  |
| --- | --- | --- | --- |
|  | CEℓ​(X)=ℓ−1​(𝔼​[ℓ​(X)]),X∈L∞.\displaystyle\mathrm{CE}\_{\ell}(X)=\ell^{-1}(\mathbb{E}[\ell(X)]),~~~~X\in L^{\infty}. |  | (8) |

###### Proposition 1.

The certainty equivalent functional CEℓ\mathrm{CE}\_{\ell} in ([8](#S3.E8 "In 3.2 On certainty equivalents with respect to expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")) is submodular if and only if ℓ\ell is convex.

###### Proof.

For the “if” direction, assume that ℓ\ell is convex. Since ℓ\ell is strictly increasing, its generalized inverse ℓ−1\ell^{-1} is concave. The submodularity of CEℓ\mathrm{CE}\_{\ell} is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ−1​(𝔼​[ℓ​(X∨Y)]⏟=a)+ℓ−1​(𝔼​[ℓ​(X∧Y)]⏟=b)≤ℓ−1​(𝔼​[ℓ​(X)]⏟=c)+ℓ−1​(𝔼​[ℓ​(Y)]⏟=d)\ell^{-1}(\underbrace{\mathbb{E}[\ell(X\vee Y)]}\_{=a})+\ell^{-1}(\underbrace{\mathbb{E}[\ell(X\wedge Y)]}\_{=b})\leq\ell^{-1}(\underbrace{\mathbb{E}[\ell(X)]}\_{=c})+\ell^{-1}(\underbrace{\mathbb{E}[\ell(Y)]}\_{=d}) |  | (9) |

for all X,Y∈L∞X,Y\in L^{\infty}. Because a+b=c+da+b=c+d, and ℓ\ell is increasing with
X∨Y≥XX\vee Y\geq X, X∨Y≥YX\vee Y\geq Y, X∧Y≤XX\wedge Y\leq X, and X∧Y≤YX\wedge Y\leq Y, we have
a≥ca\geq c, a≥da\geq d, b≤cb\leq c, and b≤db\leq d. Hence c,d∈[b,a]c,d\in[b,a], and
in dimension two this is equivalent to (a,b)(a,b) majorizing (c,d)(c,d), since
a+b=c+da+b=c+d and max⁡{a,b}=a≥max⁡{c,d}\max\{a,b\}=a\geq\max\{c,d\},
the concavity of ℓ−1\ell^{-1} guarantees ([9](#S3.E9 "In Proof. ‣ 3.2 On certainty equivalents with respect to expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")). For the “only if” direction, suppose that ([9](#S3.E9 "In Proof. ‣ 3.2 On certainty equivalents with respect to expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")) holds.
For any a≥ba\geq b in the
range of ℓ\ell,
we can write a=ℓ​(x)a=\ell(x) and b=ℓ​(y)b=\ell(y) for some x,y∈ℝx,y\in\mathbb{R} with x≥yx\geq y.
Let X=x​𝟙A+y​𝟙AcX=x\mathds{1}\_{A}+y\mathds{1}\_{A^{c}}
and Y=y​𝟙A+x​𝟙AcY=y\mathds{1}\_{A}+x\mathds{1}\_{A^{c}}
where AA is an event with ℙ​(A)=1/2\mathbb{P}(A)=1/2.
Then we have X∨Y=xX\vee Y=x, X∧Y=yX\wedge Y=y, and 𝔼​[ℓ​(X)]=𝔼​[ℓ​(Y)]=(a+b)/2\mathbb{E}[\ell(X)]=\mathbb{E}[\ell(Y)]=(a+b)/2.
Hence,
([9](#S3.E9 "In Proof. ‣ 3.2 On certainty equivalents with respect to expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures")) becomes

|  |  |  |
| --- | --- | --- |
|  | ℓ−1​(a)+ℓ−1​(b)≤2​ℓ−1​(a+b2),\ell^{-1}(a)+\ell^{-1}(b)\leq 2\ell^{-1}\left(\frac{a+b}{2}\right), |  |

and thus ℓ−1\ell^{-1} is midpoint concave on the range of ℓ\ell.
Since ℓ−1\ell^{-1} is increasing on ℝ\mathbb{R}, it is bounded on every closed interval and hence locally bounded. A midpoint-concave and locally bounded function on an interval is concave. Therefore, ℓ−1\ell^{-1} is concave, and ℓ\ell is convex.
∎

For this family, submodularity is characterized by convexity of the underlying loss function ℓ\ell. Specifically, CEℓ\mathrm{CE}\_{\ell} is submodular if and only if ℓ−1\ell^{-1} is concave, which is equivalent to ℓ\ell being convex.

### 3.3 Distortion risk measures

A *distortion risk measure* is a Choquet risk measure in ([2](#S2.E2 "In 2 Choquet integrals and risk measures ‣ Submodular risk measures")) satisfying v=ϕ∘ℙv=\phi\circ\mathbb{P}
for some increasing function ϕ:[0,1]→[0,1]\phi:[0,1]\to[0,1] with ϕ​(0)=0\phi(0)=0 and ϕ​(1)=1\phi(1)=1.
That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρϕ​(X)=∫X​d​(ϕ∘ℙ),X∈L∞.\rho\_{\phi}(X)=\int X\mathrm{d}(\phi\circ\mathbb{P}),~~~X\in L^{\infty}. |  | (10) |

Such functions ϕ\phi are called *distortion functions*.
The ES at level pp corresponds to the distortion function ϕ\phi given by ϕ​(t)=min⁡{t/(1−p),1}\phi(t)=\min\{t/(1-p),1\} for t∈[0,1]t\in[0,1].
For
a distortion risk measure ρϕ\rho\_{\phi}, coherence holds if and only if ϕ\phi is concave, and it is also equivalent to several other properties, such as convex-order consistency, subadditivity, quasi-convexity, and concavity on mixtures; see e.g., Wang et al., [2020](#bib.bib22 "Characterization, robustness and aggregation of signed Choquet integrals"), Theorem 3.

Using the main result of Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")) and known characterizations of distortion risk measures (Yaari, [1987](#bib.bib23 "The dual theory of choice under risk")), we arrive at the following characterization. The proof of the result is simple, but it offers several new characterizations of coherent distortion risk measures.

###### Theorem 2.

For a law-invariant risk measure ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R},
the following statements are equivalent:

1. (i)

   ρ\rho is coherent and submodular;
2. (ii)

   ρ\rho is positively homogeneous, monetary, and submodular;
3. (iii)

   ρ\rho is submodular, comonotonic-additive, and monetary;
4. (iv)

   ρ\rho is convex, comonotonic-additive, and monetary;
5. (v)

   ρ\rho is a distortion risk measure with a concave distortion function.

###### Proof.

In each implication below, we use only the properties explicitly assumed in that implication (plus law invariance from the theorem statement).

(i)⇒\Rightarrow(ii):
Immediate by definition.

(ii)⇒\Rightarrow(iii):
A monetary and positively homogeneous functional on L∞L^{\infty} is Lipschitz, hence L∞L^{\infty}-continuous. Together with submodularity, Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions"), Theorem 2.1) give a Choquet integral representation, which satisfies comonotonic additivity.

(iii)⇒\Rightarrow(iv): Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions"), Corollary 2.1) show that submodularity and subadditivity coincide for Choquet integrals.
Subadditivity is equivalent to convexity for positively homogeneous functionals.

(iv)⇒\Rightarrow(v): This follows directly from the standard characterization of distortion risk measures; see Schmeidler ([1986](#bib.bib20 "Integral representation without additivity")) and Yaari ([1987](#bib.bib23 "The dual theory of choice under risk")).

(v)⇒\Rightarrow(i): It is well known that subadditivity of a distortion risk measure is equivalent to concavity of the distortion, and submodularity follows from Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions"), Corollary 2.1).
∎

Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures") provides the coherent benchmark for this paper. In the law-invariant setting, the conjunction of positive homogeneity, monetary property, and submodularity is equivalent to a distortion representation with concave distortion. Hence, under the coherent setting, submodularity yields no class beyond coherent distortion risk measures. The subsequent sections focus on the case without positive homogeneity.

## 4 Four classes of convex risk measures

As we have seen from Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"), coherent risk measures that are submodular
are well understood and fully characterized. Next, we consider four classes of convex risk measures that admit explicit formulas.
These four classes are quite general and include most commonly used convex risk measures, such as the entropic risk measures, ES, the expectiles, and all coherent distortion risk measures.

### 4.1 Shortfall risk measures

Let ℓ:ℝ→(−∞,∞]\ell:\mathbb{R}\to(-\infty,\infty] be a strictly increasing convex function, which we call a loss function.
A *shortfall risk measure* as in Föllmer and Schied ([2002](#bib.bib9 "Convex measures of risk and trading constraints")) with loss function ℓ\ell is defined by

|  |  |  |
| --- | --- | --- |
|  | ρℓ​(X)=inf{m∈ℝ:𝔼​[ℓ​(X−m)]≤ℓ​(0)},X∈L∞.\rho\_{\ell}(X)=\inf\{m\in\mathbb{R}:\mathbb{E}[\ell(X-m)]\leq\ell(0)\},\qquad X\in L^{\infty}. |  |

Because ℓ\ell is continuous and strictly increasing,
ρℓ​(X)\rho\_{\ell}(X) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ℓ​(X−ρℓ​(X))]=ℓ​(0).\mathbb{E}[\ell(X-\rho\_{\ell}(X))]=\ell(0). |  | (11) |

Now replace ℓ\ell by

|  |  |  |
| --- | --- | --- |
|  | ℓ~​(x)=ℓ​(x)−ℓ​(0),x∈ℝ.\tilde{\ell}(x)=\ell(x)-\ell(0),\qquad x\in\mathbb{R}. |  |

Then ℓ~\tilde{\ell} is still strictly increasing and convex, and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ℓ​(X−m)]≤ℓ​(0)⇔𝔼​[ℓ~​(X−m)]≤0.\mathbb{E}[\ell(X-m)]\leq\ell(0)\iff\mathbb{E}[\tilde{\ell}(X-m)]\leq 0. |  |

Hence, this normalization does not change the shortfall risk measure and we may assume ℓ​(0)=0\ell(0)=0 without loss of generality. Under this normalization, ([11](#S4.E11 "In 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) reads as
𝔼​[ℓ​(X−ρℓ​(X))]=0.\mathbb{E}[\ell(X-\rho\_{\ell}(X))]=0.

In the next result, we consider the simpler case where ℓ∈C2​(ℝ)\ell\in C^{2}(\mathbb{R}), and let

|  |  |  |
| --- | --- | --- |
|  | R​(x)=ℓ′′​(x)ℓ′​(x)​for​x∈ℝ,and​L=infy∈ℝR​(y).R(x)=\frac{\ell^{\prime\prime}(x)}{\ell^{\prime}(x)}~\mbox{for}~x\in\mathbb{R},~~~\mbox{and}~~~L=\inf\_{y\in\mathbb{R}}R(y). |  |

Note that RR is nonnegative since ℓ\ell is convex.
The general case where ℓ\ell is convex but not necessarily in C2​(ℝ)C^{2}(\mathbb{R}) will be treated in Appendix [A](#A1 "Appendix A Omitted proofs ‣ Submodular risk measures"), which requires more involved analysis.

###### Theorem 3.

Assume ℓ∈C2​(ℝ)\ell\in C^{2}(\mathbb{R}) is strictly increasing and convex with ℓ​(0)=0\ell(0)=0. Then the shortfall risk measure ρℓ\rho\_{\ell} is submodular if and only if there exists λ∈ℝ\lambda\in\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(x)−2​L≤λ​ℓ​(x)ℓ′​(x), for all ​x∈ℝ.R(x)-2L\leq\lambda\,\frac{\ell(x)}{\ell^{\prime}(x)},\qquad\mbox{ for all }x\in\mathbb{R}. |  | (12) |

###### Proof.

Set

|  |  |  |
| --- | --- | --- |
|  | S​(x)=ℓ′​(x),h​(x)=S​(x)​(R​(x)−2​L),x∈ℝ.S(x)=\ell^{\prime}(x),\qquad h(x)=S(x)\big(R(x)-2L\big),\qquad x\in\mathbb{R}. |  |

Since ℓ\ell is strictly increasing and convex, S​(x)>0S(x)>0 for all xx, so ([12](#S4.E12 "In Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)≤λ​ℓ​(x),x∈ℝ.h(x)\leq\lambda\,\ell(x),\qquad x\in\mathbb{R}. |  | (13) |

We will show that ([13](#S4.E13 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) is necessary and sufficient for submodularity of ρℓ\rho\_{\ell}, and we prove this on uniform atomic spaces first.

Fix n≥3n\geq 3 and work on an nn-atom space with equal weights. Identify XX with 𝐱=(x1,…,xn)∈ℝn\mathbf{x}=(x\_{1},\dots,x\_{n})\in\mathbb{R}^{n} and define m​(𝐱)=ρℓ​(X)m(\mathbf{x})=\rho\_{\ell}(X). Then mm is characterized by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nℓ​(xk−m​(𝐱))=0.\sum\_{k=1}^{n}\ell(x\_{k}-m(\mathbf{x}))=0. |  | (14) |

Write yk=xk−m​(𝐱)y\_{k}=x\_{k}-m(\mathbf{x}) and

|  |  |  |
| --- | --- | --- |
|  | T​(𝐱)=∑k=1nS​(yk),wk​(𝐱)=S​(yk)T​(𝐱).T(\mathbf{x})=\sum\_{k=1}^{n}S(y\_{k}),\qquad w\_{k}(\mathbf{x})=\frac{S(y\_{k})}{T(\mathbf{x})}. |  |

Since ∑kS​(xk−m)>0\sum\_{k}S(x\_{k}-m)>0, the implicit function theorem gives m∈C2​(ℝn)m\in C^{2}(\mathbb{R}^{n}). Differentiating ([14](#S4.E14 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) with respect to xjx\_{j} yields

|  |  |  |
| --- | --- | --- |
|  | ∂jm​(𝐱)=wj​(𝐱).\partial\_{j}m(\mathbf{x})=w\_{j}(\mathbf{x}). |  |

A second differentiation, using S′=S​RS^{\prime}=SR and ∂jyk=𝟏{k=j}−wj\partial\_{j}y\_{k}=\mathbf{1}\_{\{k=j\}}-w\_{j}, gives for i≠ji\neq j

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂i​j2m​(𝐱)=−wi​wj​(R​(yi)+R​(yj)−∑k=1nwk​R​(yk)).\partial\_{ij}^{2}m(\mathbf{x})=-w\_{i}w\_{j}\Big(R(y\_{i})+R(y\_{j})-\sum\_{k=1}^{n}w\_{k}R(y\_{k})\Big). |  | (15) |

Sufficiency.
Assume ([13](#S4.E13 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")). Evaluating ([13](#S4.E13 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) at yky\_{k} gives

|  |  |  |
| --- | --- | --- |
|  | S​(yk)​(R​(yk)−2​L)≤λ​ℓ​(yk),k∈[n].S(y\_{k})\big(R(y\_{k})-2L\big)\leq\lambda\,\ell(y\_{k}),\qquad k\in[n]. |  |

Summing over kk and dividing by T​(𝐱)=∑k=1nS​(yk)>0T(\mathbf{x})=\sum\_{k=1}^{n}S(y\_{k})>0, then using ([14](#S4.E14 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")), yields

|  |  |  |
| --- | --- | --- |
|  | ∑k=1nwk​(R​(yk)−2​L)≤λT​(𝐱)​∑k=1nℓ​(yk)=0.\sum\_{k=1}^{n}w\_{k}\big(R(y\_{k})-2L\big)\leq\frac{\lambda}{T(\mathbf{x})}\sum\_{k=1}^{n}\ell(y\_{k})=0. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | ∑k=1nwk​R​(yk)≤2​L.\sum\_{k=1}^{n}w\_{k}R(y\_{k})\leq 2L. |  |

Since R​(yi)+R​(yj)≥2​LR(y\_{i})+R(y\_{j})\geq 2L, the bracket in ([15](#S4.E15 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) is nonnegative, so ∂i​j2m≤0\partial\_{ij}^{2}m\leq 0 for all i≠ji\neq j, and mm is submodular.

Necessity.
Assume ρℓ\rho\_{\ell} is submodular. Then ∂i​j2m≤0\partial\_{ij}^{2}m\leq 0 for all i≠ji\neq j on every ℝn\mathbb{R}^{n}. Since wi,wj>0w\_{i},w\_{j}>0, ([15](#S4.E15 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nwk​(𝐱)​R​(yk)≤R​(yi)+R​(yj).\sum\_{k=1}^{n}w\_{k}(\mathbf{x})\,R(y\_{k})\leq R(y\_{i})+R(y\_{j}). |  | (16) |

We first establish a balanced-sum inequality. Fix ε>0\varepsilon>0 and pick vv with R​(v)≤L+εR(v)\leq L+\varepsilon, which exists by definition of L=infRL=\inf R.
Fix any x1,…,xrx\_{1},\dots,x\_{r} with ∑k=1rℓ​(xk)=0\sum\_{k=1}^{r}\ell(x\_{k})=0.
To derive ([17](#S4.E17 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")), we build vectors where two coordinates are fixed at vv (to control the right-hand side of ([16](#S4.E16 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures"))), while NN repeated copies of (x1,…,xr)(x\_{1},\dots,x\_{r}) amplify the target sum on the left. The remaining finitely many coordinates are balancing terms chosen so that ([14](#S4.E14 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) gives m​(𝐳(N))=0m(\mathbf{z}^{(N)})=0.
Choose p∈ℝp\in\mathbb{R} with ℓ​(p)≠0\ell(p)\neq 0 and ℓ​(p)​ℓ​(v)<0\ell(p)\ell(v)<0, and set

|  |  |  |
| --- | --- | --- |
|  | M=⌊−2​ℓ​(v)ℓ​(p)⌋,d=−2​ℓ​(v)−M​ℓ​(p),M=\left\lfloor\frac{-2\ell(v)}{\ell(p)}\right\rfloor,\qquad d=-2\ell(v)-M\ell(p), |  |

so that d​ℓ​(p)≥0d\,\ell(p)\geq 0 and |d|<|ℓ​(p)||d|<|\ell(p)|.
By continuity and strict monotonicity of ℓ\ell, choose c∈ℝc\in\mathbb{R} with ℓ​(c)=d\ell(c)=d.
For each N∈ℕN\in\mathbb{N}, form 𝐳(N)∈ℝn\mathbf{z}^{(N)}\in\mathbb{R}^{n} (n=M+N​r+3n=M+Nr+3) consisting of two copies of vv, MM copies of pp, one copy of cc, and NN copies of (x1,…,xr)(x\_{1},\dots,x\_{r}). Then ∑kℓ​(zk(N))=0\sum\_{k}\ell(z\_{k}^{(N)})=0, so m​(𝐳(N))=0m(\mathbf{z}^{(N)})=0.

Apply ([16](#S4.E16 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) at 𝐳(N)\mathbf{z}^{(N)} with (i,j)(i,j) indexing the two vv-coordinates. Multiplying both sides by K=∑kS​(zk(N))K=\sum\_{k}S(z\_{k}^{(N)}) gives

|  |  |  |
| --- | --- | --- |
|  | ∑k=1nS​(zk(N))​R​(zk(N))≤2​R​(v)​K.\sum\_{k=1}^{n}S(z\_{k}^{(N)})\,R(z\_{k}^{(N)})\leq 2R(v)\,K. |  |

Rearranging and isolating the NN repeated blocks,

|  |  |  |
| --- | --- | --- |
|  | N​∑k=1rS​(xk)​(R​(xk)−2​R​(v))≤2​S​(v)​R​(v)−A,N\sum\_{k=1}^{r}S(x\_{k})\big(R(x\_{k})-2R(v)\big)\leq 2S(v)R(v)-A, |  |

where A=M​S​(p)​(R​(p)−2​R​(v))+S​(c)​(R​(c)−2​R​(v))A=MS(p)(R(p)-2R(v))+S(c)(R(c)-2R(v)) is independent of NN. Dividing by NN and letting N→∞N\to\infty yields ∑k=1rS​(xk)​(R​(xk)−2​R​(v))≤0\sum\_{k=1}^{r}S(x\_{k})(R(x\_{k})-2R(v))\leq 0. Since R​(v)≤L+εR(v)\leq L+\varepsilon,

|  |  |  |
| --- | --- | --- |
|  | ∑k=1rh​(xk)=∑k=1rS​(xk)​(R​(xk)−2​L)≤2​ε​∑k=1rS​(xk).\sum\_{k=1}^{r}h(x\_{k})=\sum\_{k=1}^{r}S(x\_{k})\big(R(x\_{k})-2L\big)\leq 2\varepsilon\sum\_{k=1}^{r}S(x\_{k}). |  |

Sending ε↓0\varepsilon\downarrow 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1rh​(xk)≤0whenever∑k=1rℓ​(xk)=0.\sum\_{k=1}^{r}h(x\_{k})\leq 0\quad\text{whenever}\quad\sum\_{k=1}^{r}\ell(x\_{k})=0. |  | (17) |

It remains to deduce ([13](#S4.E13 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) from ([17](#S4.E17 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")). Fix a,ba,b with ℓ​(a)<0<ℓ​(b)\ell(a)<0<\ell(b) and set

|  |  |  |
| --- | --- | --- |
|  | θ=ℓ​(b)ℓ​(b)−ℓ​(a)∈(0,1),θ​ℓ​(a)+(1−θ)​ℓ​(b)=0.\theta=\frac{\ell(b)}{\ell(b)-\ell(a)}\in(0,1),\qquad\theta\ell(a)+(1-\theta)\ell(b)=0. |  |

Let rN=⌈θ​N⌉r\_{N}=\lceil\theta N\rceil and sN=N−rNs\_{N}=N-r\_{N}. The residual

|  |  |  |
| --- | --- | --- |
|  | δN=−(rN​ℓ​(a)+sN​ℓ​(b))\delta\_{N}=-(r\_{N}\ell(a)+s\_{N}\ell(b)) |  |

satisfies |δN|≤|ℓ​(a)−ℓ​(b)||\delta\_{N}|\leq|\ell(a)-\ell(b)| since 0≤rN−θ​N<10\leq r\_{N}-\theta N<1, so δN/N→0\delta\_{N}/N\to 0. Choose cNc\_{N} with ℓ​(cN)=δN\ell(c\_{N})=\delta\_{N}; since δN\delta\_{N} is bounded, cNc\_{N} stays in a compact set, and by continuity of hh, h​(cN)/N→0h(c\_{N})/N\to 0. Now

|  |  |  |
| --- | --- | --- |
|  | rN​ℓ​(a)+sN​ℓ​(b)+ℓ​(cN)=0,r\_{N}\ell(a)+s\_{N}\ell(b)+\ell(c\_{N})=0, |  |

so ([17](#S4.E17 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) applied to rNr\_{N} copies of aa, sNs\_{N} copies of bb, and cNc\_{N} gives

|  |  |  |
| --- | --- | --- |
|  | rN​h​(a)+sN​h​(b)+h​(cN)≤0.r\_{N}h(a)+s\_{N}h(b)+h(c\_{N})\leq 0. |  |

Dividing by NN and letting N→∞N\to\infty:

|  |  |  |
| --- | --- | --- |
|  | θ​h​(a)+(1−θ)​h​(b)≤0⟺h​(b)ℓ​(b)≤h​(a)ℓ​(a).\theta\,h(a)+(1-\theta)\,h(b)\leq 0\;\Longleftrightarrow\;\frac{h(b)}{\ell(b)}\leq\frac{h(a)}{\ell(a)}. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | α+=supℓ​(x)>0h​(x)ℓ​(x)≤infℓ​(x)<0h​(x)ℓ​(x)=α−.\alpha^{+}=\sup\_{\ell(x)>0}\frac{h(x)}{\ell(x)}\leq\inf\_{\ell(x)<0}\frac{h(x)}{\ell(x)}=\alpha^{-}. |  |

Both sides are finite: fixing any aa with ℓ​(a)<0\ell(a)<0 shows α+≤h​(a)/ℓ​(a)<∞\alpha^{+}\leq h(a)/\ell(a)<\infty, and similarly for α−\alpha^{-}. Any λ∈[α+,α−]\lambda\in[\alpha^{+},\alpha^{-}] satisfies h​(x)≤λ​ℓ​(x)h(x)\leq\lambda\ell(x) for all xx with ℓ​(x)≠0\ell(x)\neq 0. Taking all xk=0x\_{k}=0 in ([17](#S4.E17 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) gives h​(0)≤0=λ​ℓ​(0)h(0)\leq 0=\lambda\ell(0), completing the proof of ([13](#S4.E13 "In Proof. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")).

The remaining part of the proof is to extend the case of atomic spaces to an atomless space.
This follows from Lemma [1](#Thmlemma1 "Lemma 1. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures") below.

In what follows, a sub-σ\sigma-algebra ℱ′\mathcal{F}^{\prime} of ℱ\mathcal{F} is called simple if it is generated by finitely many disjoint sets with equal probability. The corresponding space L∞​(Ω,ℱ′,ℙ)⊆L∞L^{\infty}(\Omega,\mathcal{F}^{\prime},\mathbb{P})\subseteq L^{\infty} is called a simple subspace.
If ρ\rho is submodular on L∞L^{\infty}, then clearly it is submodular on every simple subspace; the following lemma shows that the converse is also true, and therefore completing the proof of the theorem.
∎

###### Lemma 1.

Let ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} be a shortfall risk measure with a strictly increasing loss function.
If ρ\rho is submodular on every simple subspace, then ρ\rho is submodular on all of L∞L^{\infty}.

###### Proof.

Take X,Y∈L∞X,Y\in L^{\infty}.
Using some standard approximation arguments, we can find a bounded sequence of random vectors (X(n),Y(n))(X^{(n)},Y^{(n)}) with each component in a simple subspace, converging to (X,Y)(X,Y) pointwise.
By the definition of ρ\rho as the solution to the integral equation ([11](#S4.E11 "In 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) and the bounded convergence theorem, we have
ρ​(X(n))→ρ​(X)\rho(X^{(n)})\to\rho(X), ρ​(Y(n))→ρ​(Y)\rho(Y^{(n)})\to\rho(Y),
ρ​(X(n)∨Y(n))→ρ​(X∨Y)\rho(X^{(n)}\vee Y^{(n)})\to\rho(X\vee Y)
and
ρ​(X(n)∧Y(n))→ρ​(X∧Y)\rho(X^{(n)}\wedge Y^{(n)})\to\rho(X\wedge Y).
Therefore,

|  |  |  |
| --- | --- | --- |
|  | ρ​(X∨Y)+ρ​(X∧Y)−ρ​(X)−ρ​(Y)\displaystyle\rho(X\vee Y)+\rho(X\wedge Y)-\rho(X)-\rho(Y) |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞(ρ​(X(n)∨Y(n))+ρ​(X(n)∧Y(n))−ρ​(X(n))−ρ​(Y(n)))≤0,\displaystyle=\lim\_{n\to\infty}\big(\rho(X^{(n)}\vee Y^{(n)})+\rho(X^{(n)}\wedge Y^{(n)})-\rho(X^{(n)})-\rho(Y^{(n)})\big)\leq 0, |  |

where the inequality holds because each term in the sequence is ≤0\leq 0 on the simple subspace containing X(n)X^{(n)} and Y(n)Y^{(n)}.
∎

Shortfall risk measures form a broad family of convex risk measures, but submodularity is not automatic in this family.
Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures") shows that the curvature RR is important for submodularity.
A special case of ([12](#S4.E12 "In Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) is the case of λ=0\lambda=0, which yields the condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | supx∈ℝR​(x)≤2​infx∈ℝR​(x).\sup\_{x\in\mathbb{R}}R(x)\leq 2\inf\_{x\in\mathbb{R}}R(x). |  | (18) |

This is sufficient but not necessary for submodularity, but it is very easy to check.

Since loss functions ℓ\ell can be converted into utility functions uu via
ℓ​(x)=−u​(−x)\ell(x)=-u(-x), we can verify

|  |  |  |
| --- | --- | --- |
|  | R​(x)=−u′′​(−x)u′​(−x)=A​(−x),R(x)=\frac{-u^{\prime\prime}(-x)}{u^{\prime}(-x)}=A(-x), |  |

where AA is the Arrow–Pratt coefficient of absolute risk aversion (AP coefficient).
Therefore, the condition in Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures") can be seen as a structural restriction on the AP coefficient compatible with submodularity.
To interpret the sufficient condition ([18](#S4.E18 "In 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")),
it means that the AP coefficient does not change much across different wealth levels.
Recall that the exponential utility has a constant AP coefficient, and it satisfies ([18](#S4.E18 "In 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")). Indeed, the shortfall risk with an exponential utility, with the corresponding loss function given by

|  |  |  |
| --- | --- | --- |
|  | ℓ​(x)=eγ​x−1,x∈ℝ,γ>0,\ell(x)=e^{\gamma x}-1,~~x\in\mathbb{R},~\gamma>0, |  |

also belongs to the class of CE studied in Section [3.2](#S3.SS2 "3.2 On certainty equivalents with respect to expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"), and we know it is submodular from Proposition [1](#Thmproposition1 "Proposition 1. ‣ 3.2 On certainty equivalents with respect to expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"); it also follows from Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").
In the example below, we see that ([12](#S4.E12 "In Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) allows for larger classes of shortfall risk measures.

###### Example 1.

Let ℓ​(x)=e2​x+ex−2\ell(x)=e^{2x}+e^{x}-2. Then

|  |  |  |
| --- | --- | --- |
|  | R​(x)=1+2​ex2​ex+1,x∈ℝ,R(x)=1+\frac{2e^{x}}{2e^{x}+1},\qquad x\in\mathbb{R}, |  |

and we can see that RR lies strictly between 11 and 22. Therefore, ([18](#S4.E18 "In 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) holds, and the corresponding shortfall risk measure ρℓ\rho\_{\ell} is submodular.

###### Example 2.

Take ℓ​(x)=x\ell(x)=x. The corresponding shortfall risk is the mean. Note that R​(x)=0R(x)=0 for all x∈ℝx\in\mathbb{R} in this example, and thus condition ([18](#S4.E18 "In 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) holds. Thus, it is submodular by Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures"). Indeed, we know the mean is modular by Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures").

###### Example 3.

The loss function for a convex expectile is given by

|  |  |  |
| --- | --- | --- |
|  | ℓ​(x)=x+a​max⁡{x,0},x∈ℝ,a≥0.\ell(x)=x+a\max\{x,0\},\qquad x\in\mathbb{R},~a\geq 0. |  |

By Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"), a convex expectile cannot be submodular (except for the case a=0a=0, corresponding to the mean), because it is coherent but not a distortion risk measure (Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures") states that submodular and coherent risk measures must be distortion risk measures).
Note that for a≠0a\neq 0, ℓ\ell is not differentiable at 0, so we cannot directly apply Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures"); we need the more general result stated in Appendix [A](#A1 "Appendix A Omitted proofs ‣ Submodular risk measures"), which does not require differentiability. However, the intuition still applies: interpreting RR as the curvature (as a limit), then R​(0)=∞R(0)=\infty
and R​(x)=0R(x)=0 for x≠0x\neq 0. Thus, with this limiting interpretation, ([12](#S4.E12 "In Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) cannot hold, as its left-hand side is infinite, but the right-hand side is finite.

### 4.2 Optimized certainty equivalents

Ben-Tal and Teboulle ([2007](#bib.bib5 "An old-new concept of convex risk measures: the optimized certainty equivalent")) studied the optimized certainty equivalent (OCE) as risk measures. For a convex function ℓ\ell, the OCE is defined as

|  |  |  |
| --- | --- | --- |
|  | OCEℓ​(X)=infm∈ℝ{m+𝔼​[ℓ​(X−m)]},X∈L∞.\mathrm{OCE}\_{\ell}(X)=\inf\_{m\in\mathbb{R}}\big\{m+\mathbb{E}[\ell(X-m)]\big\},\qquad X\in L^{\infty}. |  |

It is known that OCEs are convex risk measures.

###### Theorem 4.

Assume ℓ:ℝ→ℝ\ell:\mathbb{R}\to\mathbb{R} is increasing and convex, and OCEℓ​(X)∈ℝ\mathrm{OCE}\_{\ell}(X)\in\mathbb{R} for all X∈L∞X\in L^{\infty}. Then the loss-based optimized certainty equivalent OCEℓ\mathrm{OCE}\_{\ell} is submodular.

###### Proof.

Fix X,Y∈L∞X,Y\in L^{\infty} and ε>0\varepsilon>0. Choose mX,mY∈ℝm\_{X},m\_{Y}\in\mathbb{R} with

|  |  |  |
| --- | --- | --- |
|  | mX+𝔼​[ℓ​(X−mX)]≤OCEℓ​(X)+ε,mY+𝔼​[ℓ​(Y−mY)]≤OCEℓ​(Y)+ε.m\_{X}+\mathbb{E}[\ell(X-m\_{X})]\leq\mathrm{OCE}\_{\ell}(X)+\varepsilon,\qquad m\_{Y}+\mathbb{E}[\ell(Y-m\_{Y})]\leq\mathrm{OCE}\_{\ell}(Y)+\varepsilon. |  |

Without loss of generality assume mX≥mYm\_{X}\geq m\_{Y}. Since mXm\_{X} and mYm\_{Y} are not necessarily optimal for X∨YX\vee Y and X∧YX\wedge Y, the definition of OCEℓ\mathrm{OCE}\_{\ell} gives

|  |  |  |
| --- | --- | --- |
|  | OCEℓ​(X∨Y)+OCEℓ​(X∧Y)≤mX+mY+𝔼​[ℓ​((X∨Y)−mX)+ℓ​((X∧Y)−mY)].\mathrm{OCE}\_{\ell}(X\vee Y)+\mathrm{OCE}\_{\ell}(X\wedge Y)\leq m\_{X}+m\_{Y}+\mathbb{E}\!\big[\ell\big((X\vee Y)-m\_{X}\big)+\ell\big((X\wedge Y)-m\_{Y}\big)\big]. |  |

It therefore suffices to show that, pointwise,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(max⁡(a,b)−mX)+ℓ​(min⁡(a,b)−mY)≤ℓ​(a−mX)+ℓ​(b−mY),\ell\big(\max(a,b)-m\_{X}\big)+\ell\big(\min(a,b)-m\_{Y}\big)\leq\ell(a-m\_{X})+\ell(b-m\_{Y}), |  | (19) |

where a=X​(ω)a=X(\omega) and b=Y​(ω)b=Y(\omega). If a≥ba\geq b, both sides are equal. If a<ba<b, set s=b−a>0s=b-a>0. Then max⁡(a,b)−mX=(a−mX)+s\max(a,b)-m\_{X}=(a-m\_{X})+s and min⁡(a,b)−mY=(b−mY)−s\min(a,b)-m\_{Y}=(b-m\_{Y})-s. Since mX≥mYm\_{X}\geq m\_{Y}, we have a−mX≤b−mY−sa-m\_{X}\leq b-m\_{Y}-s, and because the increment x↦ℓ​(x+s)−ℓ​(x)x\mapsto\ell(x+s)-\ell(x) is increasing for convex ℓ\ell,

|  |  |  |
| --- | --- | --- |
|  | ℓ​(a−mX+s)−ℓ​(a−mX)≤ℓ​(b−mY)−ℓ​(b−mY−s),\ell(a-m\_{X}+s)-\ell(a-m\_{X})\leq\ell(b-m\_{Y})-\ell(b-m\_{Y}-s), |  |

which rearranges to ([19](#S4.E19 "In Proof. ‣ 4.2 Optimized certainty equivalents ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")). Integrating over ω\omega gives

|  |  |  |
| --- | --- | --- |
|  | OCEℓ​(X∨Y)+OCEℓ​(X∧Y)≤OCEℓ​(X)+OCEℓ​(Y)+2​ε.\mathrm{OCE}\_{\ell}(X\vee Y)+\mathrm{OCE}\_{\ell}(X\wedge Y)\leq\mathrm{OCE}\_{\ell}(X)+\mathrm{OCE}\_{\ell}(Y)+2\varepsilon. |  |

Since ε>0\varepsilon>0 is arbitrary, the result follows.
∎

In contrast with the other families studied here, the OCE family requires no extra structural restriction for submodularity.

### 4.3 Adjusted ES

Burzoni et al. ([2022](#bib.bib7 "Adjusted Expected Shortfall")) defined the AES as

|  |  |  |
| --- | --- | --- |
|  | ESg​(X)=supp∈[0,1]{ESp​(X)−g​(p)},X∈L∞.\mathrm{ES}^{g}(X)=\sup\_{p\in[0,1]}\{\mathrm{ES}\_{p}(X)-g(p)\},\qquad X\in L^{\infty}. |  |

where g:[0,1]→[0,∞]g:[0,1]\to[0,\infty] is increasing with g​(0)<∞g(0)<\infty.

###### Theorem 5.

Let g:[0,1]→[0,∞]g:[0,1]\to[0,\infty] be increasing with g​(0)<∞g(0)<\infty.
Assume that gg is not convex on [0,1][0,1]. Then ESg\mathrm{ES}^{g} is submodular if and only if it is an Expected Shortfall.

###### Proof.

The “if” statement is straightforward as we have seen that ES is submodular.
Below we show the “only if” statement.
First, since p↦ESp​(X)p\mapsto\mathrm{ES}\_{p}(X) is continuous for any X∈L∞X\in L^{\infty}, we can without loss of generality assume that gg is upper semicontinuous.

Let a>0a>0, q∈[0,1]q\in[0,1], and b∈ℝb\in\mathbb{R} be three numbers, which will be determined later.
Let UU be uniformly distributed on [0,1][0,1], and let V=U​𝟙{U≥q}+(q−U)​𝟙{U<q}V=U\mathds{1}\_{\{U\geq q\}}+(q-U)\mathds{1}\_{\{U<q\}}, which is also uniformly distributed on [0,1][0,1].
Define the random variables

|  |  |  |
| --- | --- | --- |
|  | X=2​a​U+b−a;Y=2​a​V+b−a.X=2aU+b-a;~~~Y=2aV+b-a. |  |

It is easy to compute that ESp​(X)=ESp​(Y)=a​p+b\mathrm{ES}\_{p}(X)=\mathrm{ES}\_{p}(Y)=ap+b for p∈[0,1]p\in[0,1].
Moreover, for p∈[q,1]p\in[q,1], we have

|  |  |  |
| --- | --- | --- |
|  | VaRp​(X∨Y)=VaRp​(X)=2​a​p+b−a,\mathrm{VaR}\_{p}(X\vee Y)=\mathrm{VaR}\_{p}(X)=2ap+b-a, |  |

and for p∈[0,q)p\in[0,q), we have

|  |  |  |
| --- | --- | --- |
|  | VaRp​(X∨Y)=VaR(p+q)/2​(X)=a​(p+q)+b−a.\mathrm{VaR}\_{p}(X\vee Y)=\mathrm{VaR}\_{(p+q)/2}(X)=a(p+q)+b-a. |  |

Hence, for p∈[q,1]p\in[q,1] we have ESp​(X∨Y)=a​p+b\mathrm{ES}\_{p}(X\vee Y)=ap+b, and for p∈[0,q)p\in[0,q) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESp​(X∨Y)\displaystyle\mathrm{ES}\_{p}(X\vee Y) | =a1−p​(∫pq(r+q)​dr+∫q12​r​dr)+(b−a)\displaystyle=\frac{a}{1-p}\left(\int\_{p}^{q}(r+q)\mathrm{d}r+\int\_{q}^{1}2r\mathrm{d}r\right)+(b-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1−p​(q2−p22+q​(q−p)+1−q2)+(b−a)\displaystyle=\frac{a}{1-p}\left(\frac{q^{2}-p^{2}}{2}+q(q-p)+1-q^{2}\right)+(b-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1−p​(q2−p2−2​q​p2+1)+(b−a)\displaystyle=\frac{a}{1-p}\left(\frac{q^{2}-p^{2}-2qp}{2}+1\right)+(b-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1−p​(q2−p2−2​q​p2+p)+b.\displaystyle=\frac{a}{1-p}\left(\frac{q^{2}-p^{2}-2qp}{2}+p\right)+b. |  |

Hence, for p∈[0,q)p\in[0,q),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESp​(X∨Y)−ESp​(X)\displaystyle\mathrm{ES}\_{p}(X\vee Y)-\mathrm{ES}\_{p}(X) | =a1−p​(q2−p2−2​q​p2+p)−a​p\displaystyle=\frac{a}{1-p}\left(\frac{q^{2}-p^{2}-2qp}{2}+p\right)-ap |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1−p​(q2+p2−2​q​p2)\displaystyle=\frac{a}{1-p}\left(\frac{q^{2}+p^{2}-2qp}{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =a​(q−p)22​(1−p)>0.\displaystyle=\frac{a(q-p)^{2}}{2(1-p)}>0. |  | (20) |

With a,b,qa,b,q treated as parameters of XX and YY, we can proceed to discuss the submodularity of ESg\mathrm{ES}^{g}.
Let p∗=sup{p∈[0,1]:g​(p)<∞}p^{\*}=\sup\{p\in[0,1]:g(p)<\infty\} and g∗:[0,1]→(−∞,∞]g^{\*}:[0,1]\to(-\infty,\infty] be the largest (−∞,∞](-\infty,\infty]-valued convex function on [0,1][0,1] dominated by gg. Clearly, g∗​(p)=∞g^{\*}(p)=\infty for p∈(p∗,1]p\in(p^{\*},1].

Suppose that gg is not convex on [0,p∗][0,p^{\*}]. There exist distinct points p1,p2∈[0,p∗]p\_{1},p\_{2}\in[0,p^{\*}] such that g∗​(p1)=g​(p1)g^{\*}(p\_{1})=g(p\_{1}), g∗​(p2)=g​(p2)g^{\*}(p\_{2})=g(p\_{2}), and
g∗g^{\*} is linear and strictly increasing on [p1,p2][p\_{1},p\_{2}]; see e.g., Proposition 1 of Pesenti et al. ([2025](#bib.bib18 "Optimizing distortion riskmetrics with distributional uncertainty")) and recall that we assume gg is lower semicontinuous. Choose q=p2q=p\_{2} and let a,ba,b be such that the linear mapping ϕX:p↦ESp​(X)\phi\_{X}:p\mapsto\mathrm{ES}\_{p}(X) coincides with g∗g^{\*} on [p1,p2][p\_{1},p\_{2}], and clearly g∗≥ϕXg^{\*}\geq\phi\_{X} due to convexity. By using

|  |  |  |
| --- | --- | --- |
|  | ϕX​(q)=ESq​(X)=ESq​(Y)=ESq​(X∧Y)=g​(q),\phi\_{X}(q)=\mathrm{ES}\_{q}(X)=\mathrm{ES}\_{q}(Y)=\mathrm{ES}\_{q}(X\wedge Y)=g(q), |  |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESg​(X)\displaystyle\mathrm{ES}^{g}(X) | =ESg​(Y)=supp∈[0,1]{ϕX​(p)−g​(p)}=0;\displaystyle=\mathrm{ES}^{g}(Y)=\sup\_{p\in[0,1]}\left\{\phi\_{X}(p)-g(p)\right\}=0; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ESg​(X∧Y)\displaystyle\mathrm{ES}^{g}(X\wedge Y) | ≥ESq​(X∧Y)−g​(q)=0;\displaystyle\geq\mathrm{ES}\_{q}(X\wedge Y)-g(q)=0; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ESg​(X∨Y)\displaystyle\mathrm{ES}^{g}(X\vee Y) | ≥ESp1​(X∨Y)−g​(p1)=a​(q−p1)22​(1−p1)>0.\displaystyle\geq\mathrm{ES}\_{p\_{1}}(X\vee Y)-g(p\_{1})=\frac{a(q-p\_{1})^{2}}{2(1-p\_{1})}>0. |  |

Therefore, ESg​(X∨Y)+ESg​(X∧Y)>0=ESg​(X)+ESg​(Y)\mathrm{ES}^{g}(X\vee Y)+\mathrm{ES}^{g}(X\wedge Y)>0=\mathrm{ES}^{g}(X)+\mathrm{ES}^{g}(Y), showing that ESg\mathrm{ES}^{g} is not submodular.
∎

AES refines standard ES by allowing tail-dependent capital targets: different confidence levels pp can be penalized differently. As shown by Burzoni et al. ([2022](#bib.bib7 "Adjusted Expected Shortfall")), ESg\mathrm{ES}^{g} is monetary and convex, but unless it reduces to a standard ES, it is not coherent (in particular, it fails positive homogeneity). Building on this, we show that for a nonconvex gg, submodularity implies that ESg\mathrm{ES}^{g} equals a standard ESp0\mathrm{ES}\_{p\_{0}}. Consequently, except for the case where ESg\mathrm{ES}^{g} equals a standard ESp\mathrm{ES}\_{p}, AES with nonconvex adjustment is not submodular. We conjecture that the same reduction to ES up to a constant holds for convex adjustment profiles.

### 4.4 Monotone mean-deviation risk measures

A monotone mean-deviation risk measure, studied by Han et al. ([2026](#bib.bib14 "Monotonic mean-deviation risk measures")), is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)=g​(ρϕ​(X)−𝔼​[X])+𝔼​[X],X∈L∞,\rho(X)=g(\rho\_{\phi}(X)-\mathbb{E}[X])+\mathbb{E}[X],~~~X\in L^{\infty}, |  | (21) |

where g:[0,∞)→[0,∞)g:[0,\infty)\to[0,\infty) is an increasing, convex, and non-constant function satisfying g​(0)=0g(0)=0,
and ρϕ:L∞→ℝ\rho\_{\phi}:L^{\infty}\to\mathbb{R} is a distortion risk measure with a concave distortion function ϕ\phi.
In Han et al. ([2026](#bib.bib14 "Monotonic mean-deviation risk measures")), ρϕ\rho\_{\phi} in ([21](#S4.E21 "In 4.4 Monotone mean-deviation risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) can be replaced by other law-invariant coherent risk measures, but for explicit formulas, we stick to the setting of using distortion risk measures in ([21](#S4.E21 "In 4.4 Monotone mean-deviation risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")).

###### Theorem 6.

The risk measure ρ\rho in ([21](#S4.E21 "In 4.4 Monotone mean-deviation risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures")) is submodular if and only if it is a coherent distortion risk measure, that is, gg is linear or ρϕ​(X)=𝔼​[X]\rho\_{\phi}(X)=\mathbb{E}[X] for all X∈L∞X\in L^{\infty}.

###### Proof.

The “if” statement is straightforward. Below we show the “only if” statement.
Suppose that the convex function gg is not linear and ρϕ​(X)≠𝔼​[X]\rho\_{\phi}(X)\neq\mathbb{E}[X] for some X∈L∞X\in L^{\infty}, and we will show that ρ\rho is not submodular. There exists x>0x>0 such that gg is
locally nonlinear at xx, and by convexity it implies g​(y)+g​(z)>2​g​(x)g(y)+g(z)>2g(x) for all y,z≥0y,z\geq 0 with y+z=2​xy+z=2x and y≠xy\neq x.

Since ϕ\phi is not the identity and it is concave, we know ϕ​(t)>t\phi(t)>t for all t∈(0,1)t\in(0,1).
Let ψ​(t)=ϕ​(t)−t\psi(t)=\phi(t)-t for t∈(0,1)t\in(0,1).
The set {ψ​(t):t∈(0,1)}\{\psi(t):t\in(0,1)\} is a nonempty interval because of the continuity of ψ\psi on (0,1)(0,1).
Moreover, ψ​(t)→0\psi(t)\to 0 as t↑1t\uparrow 1. Therefore,
we can find p,q,r∈(0,1)p,q,r\in(0,1) with p<q<rp<q<r such that
ψ​(p)>ψ​(q)>ψ​(r)\psi(p)>\psi(q)>\psi(r) and ψ​(p)+ψ​(r)=2​ψ​(q)\psi(p)+\psi(r)=2\psi(q).
Let m=x/ψ​(q)m=x/\psi(q),
X=m​(𝟙A+𝟙C)/2X=m(\mathds{1}\_{A}+\mathds{1}\_{C})/2, and Y=m​𝟙BY=m\mathds{1}\_{B}, where the events A,B,CA,B,C satisfy A⊆B⊆CA\subseteq B\subseteq C, ℙ​(A)=p\mathbb{P}(A)=p, ℙ​(B)=q\mathbb{P}(B)=q, and ℙ​(C)=r\mathbb{P}(C)=r.
We can calculate

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρϕ​(X)−𝔼​[X]\displaystyle\rho\_{\phi}(X)-\mathbb{E}[X] | =m​(ψ​(p)+ψ​(r))/2=x;\displaystyle=m(\psi(p)+\psi(r))/2=x; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ρϕ​(Y)−𝔼​[Y]\displaystyle\rho\_{\phi}(Y)-\mathbb{E}[Y] | =m​ψ​(q)=x;\displaystyle=m\psi(q)=x; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y=ρϕ​(X∧Y)−𝔼​[X∧Y]\displaystyle y=\rho\_{\phi}(X\wedge Y)-\mathbb{E}[X\wedge Y] | =m​(ψ​(p)+ψ​(q))/2>x;\displaystyle=m(\psi(p)+\psi(q))/2>x; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | z=ρϕ​(X∨Y)−𝔼​[X∨Y]\displaystyle z=\rho\_{\phi}(X\vee Y)-\mathbb{E}[X\vee Y] | =m​(ψ​(q)+ψ​(r))/2<x.\displaystyle=m(\psi(q)+\psi(r))/2<x. |  |

Since y+z=2​xy+z=2x and y>xy>x, we get

|  |  |  |
| --- | --- | --- |
|  | ρ​(X∧Y)+ρ​(X∨Y)=g​(y)+g​(z)+𝔼​[X+Y]>2​g​(x)+𝔼​[X+Y]=ρ​(X)+ρ​(Y),\rho(X\wedge Y)+\rho(X\vee Y)=g(y)+g(z)+\mathbb{E}[X+Y]>2g(x)+\mathbb{E}[X+Y]=\rho(X)+\rho(Y), |  |

showing that ρ\rho is not submodular.
∎

The theorem above shows that submodularity is highly restrictive in this class. Submodularity excludes any active nonlinearity in the deviation weighting: either gg is linear, or ρϕ​(X)=𝔼​[X]\rho\_{\phi}(X)=\mathbb{E}[X] for all X∈L∞X\in L^{\infty}, so the deviation term vanishes.

## 5 Discussion: Submodularity on sets

We now discuss a different form of submodularity and its relation to our setting.
As mentioned in Ghamami and Glasserman ([2019](#bib.bib10 "Submodular risk allocation")) and Bilmes ([2022](#bib.bib6 "Submodularity in machine learning and artificial intelligence")), submodularity is the property of diminishing marginal risk: the marginal change in risk from adding an asset to a portfolio decreases with the addition of another asset. Mathematically, Ghamami and Glasserman ([2019](#bib.bib10 "Submodular risk allocation")) and Bilmes ([2022](#bib.bib6 "Submodularity in machine learning and artificial intelligence")) state that a set-indexed risk measure is submodular if it satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(S∪T)+v​(S∩T)≤v​(T)+v​(S),S,T⊆[n],v(S\cup T)+v(S\cap T)\leq v(T)+v(S),\qquad S,T\subseteq[n], |  | (22) |

where [n]={1,…,n}[n]=\{1,\dots,n\}.
This is submodularity of vv on the lattice (2[n],∪,∩)(2^{[n]},\cup,\cap).
It is well known that ([22](#S5.E22 "In 5 Discussion: Submodularity on sets ‣ Submodular risk measures")) is
equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(S∪{z})−v​(S)≥v​(T∪{z})−v​(T),S⊆T⊆[n],∀z∉T.v(S\cup{\{z\}})-v(S)\geq v(T\cup{\{z\}})-v(T),\qquad S\subseteq T\subseteq[n],\qquad\forall z\notin T. |  | (23) |

For a given risk measure ρ\rho and a random vector (Xi)i∈[n](X\_{i})\_{i\in[n]},
write v​(S)=ρ​(∑i∈SXi)v(S)=\rho(\sum\_{i\in S}X\_{i}) for S⊆[n]S\subseteq[n].
The submodularity of vv as defined in ([23](#S5.E23 "In 5 Discussion: Submodularity on sets ‣ Submodular risk measures")) means that, for S⊆T⊆[n]S\subseteq T\subseteq[n] and any j∉Tj\notin T, we have

|  |  |  |
| --- | --- | --- |
|  | ρ​(∑i∈SXi+Xj)−ρ​(∑i∈SXi)≥ρ​(∑i∈TXi+Xj)−ρ​(∑i∈TXi).\;\rho\!\left(\sum\_{i\in S}X\_{i}+X\_{j}\right)\;-\;\rho\!\left(\sum\_{i\in S}X\_{i}\right)\;\geq\;\rho\!\left(\sum\_{i\in T}X\_{i}+X\_{j}\right)\;-\;\rho\!\left(\sum\_{i\in T}X\_{i}\right).\; |  |

Rearranging terms, it is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(∑i∈TXi+Xj)+ρ​(∑i∈SXi)≤ρ​(∑i∈SXi+Xj)+ρ​(∑i∈TXi).\rho\left(\sum\_{i\in T}X\_{i}+X\_{j}\right)+\rho\left(\sum\_{i\in S}X\_{i}\right)\leq\rho\left(\sum\_{i\in S}X\_{i}+X\_{j}\right)+\rho\left(\sum\_{i\in T}X\_{i}\right). |  | (24) |

Suppose that (Xi)i∈[n](X\_{i})\_{i\in[n]}
has nonnegative components and
ℙ​(Xj>0,∑i∈TXi>0)=0\mathbb{P}(X\_{j}>0,\sum\_{i\in T}X\_{i}>0)=0.
Write X=∑i∈SXi+XjX=\sum\_{i\in S}X\_{i}+X\_{j}
and Y=∑i∈TXiY=\sum\_{i\in T}X\_{i},
then we have X∨Y=∑i∈TXi+XjX\vee Y=\sum\_{i\in T}X\_{i}+X\_{j}
and X∧Y=∑i∈SXiX\wedge Y=\sum\_{i\in S}X\_{i}. Therefore, ([24](#S5.E24 "In 5 Discussion: Submodularity on sets ‣ Submodular risk measures")) becomes

|  |  |  |
| --- | --- | --- |
|  | ρ​(X∨Y)+ρ​(X∧Y)≤ρ​(X)+ρ​(Y),\rho(X\vee Y)+\rho(X\wedge Y)\leq\rho(X)+\rho(Y), |  |

thus our definition of submodularity for this particular choice of (X,Y)(X,Y).

## 6 Submodularity in financial data

#### Methodology.

Daily adjusted closing prices are obtained from Stooq (primary source) with Yahoo Finance as a fallback for the period January 1, 2015 to January 31, 2025. The download window begins approximately 750 trading days before January 1, 2018 in order to provide a warm-up period for the rolling-window estimators; the sector-based results, figures, and exported statistics cover the period from January 1, 2018 onward (approximately 1,780 trading days). The pair-based analysis uses the full download period, yielding 2,286 valid days for the 250-day window and 2,036 for the 500-day window. We compute daily log returns as
rt=ln⁡(Pt)−ln⁡(Pt−1),r\_{t}=\ln(P\_{t})-\ln(P\_{t-1}), where PtP\_{t} denotes the adjusted closing price on day tt.
For each pair, returns are aligned on common trading dates and rows with any missing observations are dropped (complete-case deletion); no forward-filling or interpolation is applied.

For each stock and each trading day, we compute rolling historical VaR and ES using two window lengths:

* •

  n=250n=250 trading days (approximately one year),
* •

  n=500n=500 trading days (approximately two years).

Within each window, returns {rt}\{r\_{t}\} are converted to losses Lt=−rtL\_{t}=-r\_{t}. For a confidence level p∈(0,1)p\in(0,1), let k=⌈n​(1−p)⌉,k=\lceil n(1-p)\rceil, and let L(1)≥L(2)≥⋯≥L(n)L\_{(1)}\geq L\_{(2)}\geq\cdots\geq L\_{(n)} denote the ordered losses in descending order (largest loss first). We compute:

|  |  |  |
| --- | --- | --- |
|  | VaRp=L(k),ESp=1k​∑i=1kL(i).\mathrm{VaR}\_{p}=L\_{(k)},\qquad\mathrm{ES}\_{p}=\frac{1}{k}\sum\_{i=1}^{k}L\_{(i)}. |  |

That is, we use a historical simulation estimator based on upper-tail order statistics: VaRp\mathrm{VaR}\_{p} is the kk-th largest loss in the window, and ESp\mathrm{ES}\_{p} is the arithmetic mean of the kk largest losses. This convention is immaterial under continuous loss distributions and is conservative in finite samples when n​(1−p)n(1-p) is an integer.
We use confidence-level parameterization throughout this section; the corresponding tail probability is 1−p1-p.
For the sector-based analysis, we use p∈{0.90, 0.95}p\in\{0.90,\,0.95\}.
The pair-based analysis explores 14 levels:
p∈{0.99, 0.98,…, 0.90}p\in\{0.99,\,0.98,\,\ldots,\,0.90\} and p∈{0.88, 0.85, 0.82, 0.80}p\in\{0.88,\,0.85,\,0.82,\,0.80\},
to examine non-monotonic patterns across confidence levels.
Following the theoretical framework, we consider a two-level special case of AES:

|  |  |  |
| --- | --- | --- |
|  | AESp,q,c​(X)=max⁡{ESq​(X),ESp​(X)−c},\mathrm{AES}\_{p,q,c}(X)=\max\bigl\{\mathrm{ES}\_{q}(X),\ \mathrm{ES}\_{p}(X)-c\bigr\}, |  |

where p=0.98p=0.98 and cc is a fixed constant. This is a special case of

|  |  |  |
| --- | --- | --- |
|  | supu∈[0,1]{ESu​(X)−g​(u)},\sup\_{u\in[0,1]}\{\mathrm{ES}\_{u}(X)-g(u)\}, |  |

with only two finite levels. For the sector-based analysis, q∈{0.90,0.95}q\in\{0.90,0.95\}; for the pair-based analysis, qq ranges over the same 14 pp-levels listed above. We consider
c∈{0.01, 0.015, 0.02}.c\in\{0.01,\ 0.015,\ 0.02\}. The choice of cc values is informed by the typical gap between ESp\mathrm{ES}\_{p} and ESq\mathrm{ES}\_{q} observed in our sample: at q=0.90q=0.90, the mean gap ES0.98−ES0.90\mathrm{ES}\_{0.98}-\mathrm{ES}\_{0.90} ranges from 0.021 to 0.041 across stocks and window lengths, so that the adjustment term has a meaningful effect on AESp,q,c\mathrm{AES}\_{p,q,c} in practice.

#### Submodularity test.

For each pair of stocks (X,Y)(X,Y) and each trading day, we test the submodularity condition, where ρ\rho denotes the risk measure (VaR, ES, or AESp,q,c\mathrm{AES}\_{p,q,c}).
We record a violation when

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)+ρ​(Y)−ρ​(X∧Y)−ρ​(X∨Y)<−ϵ,ϵ=10−8,\rho(X)+\rho(Y)-\rho(X\wedge Y)-\rho(X\vee Y)<-\epsilon,\qquad\epsilon=10^{-8}, |  |

where ϵ\epsilon serves as a guard against floating-point arithmetic errors (double-precision machine epsilon is approximately 2.2×10−162.2\times 10^{-16}, so our threshold is conservative).
Here X∧YX\wedge Y and X∨YX\vee Y denote the pointwise minimum and maximum of the two loss series: within each rolling window of length nn, we compute (min⁡(LtX,LtY))t(\min(L\_{t}^{X},L\_{t}^{Y}))\_{t} and (max⁡(LtX,LtY))t(\max(L\_{t}^{X},L\_{t}^{Y}))\_{t}, then apply the same historical simulation estimator to these constructed series.
The daily violation rate is computed as the proportion of stock pairs exhibiting a violation on each day.

#### Sample construction and analysis designs.

We conduct two complementary empirical analyses that differ in sample construction and aggregation. To examine how submodularity violations vary across confidence levels, we perform a focused analysis on the three selected stock pairs (META–NFLX, DIS–GOOGL, and DIS–META), chosen to represent high-volatility technology and media firms with strong tail-risk interactions. The analysis focuses on how submodularity violations vary with confidence levels, window lengths, and (for AESp,q,c\mathrm{AES}\_{p,q,c}) the parameters (q,c)(q,c).

The second part of the analysis is a sector-based design intended to provide broad market coverage while remaining computationally tractable. Specifically, we select the top five S&P 500 constituents by market capitalization as of January 2018 (the start of the analysis window) from each of the eleven GICS sectors, resulting in 55 unique stocks (see Table [4](#A1.T4 "Table 4 ‣ A2 Stock selection ‣ Appendix A Omitted proofs ‣ Submodular risk measures") in the Appendix for the full list with market capitalizations and data sources). Using beginning-of-sample market capitalizations avoids look-ahead bias in stock selection. The constituent list itself is taken from a current snapshot of the S&P 500; firms that were removed from the index between 2018 and 2025 but still had valid price data in January 2018 may therefore be absent from our candidate pool. This residual look-ahead in the constituent list does not affect the validity of the submodularity test—which is a pointwise property of the risk-measure estimator—but it does mean that the candidate universe is conditioned on eventual index membership. For the submodularity test, we evaluate all pairwise combinations of these 55 stocks, yielding (552)=1,485\binom{55}{2}=1{,}485 pairs per trading day.

#### Summary statistics and empirical patterns.

For the pair-based analysis, Figure [1](#S6.F1 "Figure 1 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") displays VaR and ES violation rates as a function of confidence level for each pair. The VaR violation rate shows a non-monotonic pattern that varies across window lengths. For the 250-day window, rates are moderate at 80% confidence (12.5%), decrease to 10.2% at 95% confidence, and then rise sharply to 30.8% at 99% confidence. For the 500-day window, violation rates are very low at moderate confidence levels (often near 0% at 95%) but increase substantially at 98–99% confidence (19.7–27.9%). The longer window produces lower overall violation rates. As expected from the exact ES structure of the estimator, ES exhibits no submodularity violations across all confidence levels and both rolling-window lengths in our sample (Table [1](#S6.T1 "Table 1 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures")).

Figure [2](#S6.F2 "Figure 2 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") illustrates how AESp,q,c\mathrm{AES}\_{p,q,c} violation rates vary with the choice of qq and cc. Two patterns emerge. First, the effect of qq is non-monotone: violation rates are highest for intermediate values of qq and are close to zero at both extremes. When qq is very close to pp, the adjustment term dominates and AESp,q,c=ESp−c\mathrm{AES}\_{p,q,c}=\mathrm{ES}\_{p}-c, which preserves submodularity; when qq is far from pp, AESp,q,c=ESq\mathrm{AES}\_{p,q,c}=\mathrm{ES}\_{q}, which is also submodular. Second, larger values of cc generally produce higher violation rates. For example when c=0.02c=0.02, mean violation rates can reach 7–10% at certain intermediate qq values, whereas c=0.01c=0.01 keeps violations near zero (0.03%). Overall, AESp,q,c\mathrm{AES}\_{p,q,c} exhibits an average violation rate of 0.93%, placing it between ES (no observed violations) and VaR (frequent violations) (Table [1](#S6.T1 "Table 1 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures")).

Table 1: Pair-based analysis: Submodularity violation rates across three stock pairs

|  |  |  |  |
| --- | --- | --- | --- |
| Risk measure | Total tests | Violations | Rate (%) |
| VaR | 181,524 | 17,966 | 9.90 |
| ES | 181,524 | 0 | 0.00 |
| AESp,q,c\mathrm{AES}\_{p,q,c} | 544,572 | 5,041 | 0.93 |
| 3 pairs, windows 250 (N=2,286N=2{,}286) and 500 (N=2,036N=2{,}036), 14 confidence levels. | | | |
| --- | --- | --- | --- |
| AESp,q,c\mathrm{AES}\_{p,q,c}: 14 qq-levels ×\times 3 cc-values. | | | |



![Refer to caption](2603.01232v1/pictures/var_es1_conf_pairs.png)

![Refer to caption](2603.01232v1/pictures/var_es2_conf_pairs.png)

![Refer to caption](2603.01232v1/pictures/var_es3_conf_pairs.png)

Figure 1: VaR and ES: violation rate versus confidence level for each selected pair.
Top to bottom: META–NFLX, DIS–GOOGL, DIS–META.



![Refer to caption](2603.01232v1/pictures/esg1_conf_pairs.png)

![Refer to caption](2603.01232v1/pictures/esg2_conf_pairs.png)

![Refer to caption](2603.01232v1/pictures/esg3_conf_pairs.png)

Figure 2: AESp,q,c\mathrm{AES}\_{p,q,c}: violation rate versus confidence level qq for different values of cc.
Top to bottom: META–NFLX, DIS–GOOGL, DIS–META.

For the sector analysis, Table [2](#S6.T2 "Table 2 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") reports summary statistics of the daily submodularity violation rates, aggregated across all stock pairs and trading days, for each risk measure. Overall, the empirical evidence is consistent with the theoretical predictions. As expected from the exact ES structure of the estimator, no ES violations are observed over the entire sample period. In contrast, VaR frequently violates submodularity: the average daily violation rate is approximately 4.5%, with substantial variation over time (standard deviation of 2.7%) and peaks above 13%, which tend to coincide with periods of elevated market volatility. Longer estimation windows substantially reduce VaR violation rates—from 6.2% at n=250n=250 to 2.7% at n=500n=500—suggesting that sampling variability in the quantile estimate is a key driver of submodularity failures. AES, that is, AESp,q,c\mathrm{AES}\_{p,q,c}, displays only minor violations on average (mean of 0.39%, maximum of 0.99%), placing it between ES (no observed violations) and VaR (frequent violations). Moreover, the adjustment parameter cc affects the violation frequency, with larger values of cc generally associated with higher violation rates: c=0.01c=0.01 produces near-zero violations across all window lengths and qq values, whereas c=0.02c=0.02 drives most observed violations. To illustrate the time-series behavior, Figures [3](#S6.F3 "Figure 3 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") and [4](#S6.F4 "Figure 4 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") plot the daily violation rates for VaR/ES and AESp,q,c\mathrm{AES}\_{p,q,c}, respectively.

Table 2: Sector-based analysis: Daily submodularity violation rates

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Risk measure | Mean (%) | Std (%) | Min (%) | Max (%) |
| VaR | 4.45 | 2.71 | 1.35 | 13.18 |
| ES | 0.00 | 0.00 | 0.00 | 0.00 |
| AESp,q,c\mathrm{AES}\_{p,q,c} | 0.39 | 0.26 | 0.02 | 0.99 |
| January 2018–January 2025. VaR/ES at 90% and 95% confidence; AESp,q,c\mathrm{AES}\_{p,q,c} over q∈{0.90,0.95}q\in\{0.90,0.95\}, c∈{0.01,0.015,0.02}c\in\{0.01,0.015,0.02\}. Both windows. | | | | |
| --- | --- | --- | --- | --- |

![Refer to caption](2603.01232v1/pictures/var_es_violations.png)


Figure 3: Daily VaR/ES submodularity violation rate over time.

![Refer to caption](2603.01232v1/pictures/esg_violations.png)


Figure 4: Daily AESp,q,c\mathrm{AES}\_{p,q,c} submodularity violation rate over time.

Figure [1](#S6.F1 "Figure 1 ‣ Summary statistics and empirical patterns. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") provides an empirical illustration of the theoretical contrast between VaR and ES under lattice aggregation. The submodularity test concerns the response of a risk measure to the operations X∧YX\wedge Y and X∨YX\vee Y, rather than the risk level of a single position. Because VaR is quantile-based and depends on one order statistic, small changes in dependence or tail ranking can induce non-smooth changes in VaRp​(X∨Y)\mathrm{VaR}\_{p}(X\vee Y) and VaRp​(X∧Y)\mathrm{VaR}\_{p}(X\wedge Y), which leads to frequent submodularity violations. By contrast, ES averages tail losses beyond the VaR threshold and is therefore more stable under the same aggregation operations. In our sample, the absence of ES violations is consistent with the theory, whereas VaR exhibits frequent non-smooth changes under lattice recombination.

#### Subadditivity test and VIX correlation analysis.

As a complementary analysis, we test VaR for subadditivity violations using the same sector-based sample of stock pairs. For each pair (X,Y)(X,Y), we form the portfolio loss series LtX+Y=−(rtX+rtY)L\_{t}^{X+Y}=-\bigl(r\_{t}^{X}+r\_{t}^{Y}\bigr) and compute the rolling VaR of the sum directly. A subadditivity violation is recorded when

|  |  |  |
| --- | --- | --- |
|  | VaRp​(X)+VaRp​(Y)−VaRp​(X+Y)<−ϵ,ϵ=10−8,\mathrm{VaR}\_{p}(X)+\mathrm{VaR}\_{p}(Y)-\mathrm{VaR}\_{p}(X+Y)<-\epsilon,\qquad\epsilon=10^{-8}, |  |

that is, when VaRp​(X+Y)>VaRp​(X)+VaRp​(Y)\mathrm{VaR}\_{p}(X+Y)>\mathrm{VaR}\_{p}(X)+\mathrm{VaR}\_{p}(Y), so that VaR penalizes diversification. We test at confidence levels p∈{0.95, 0.975, 0.99}p\in\{0.95,\,0.975,\,0.99\} using both window lengths.

To examine the relationship between violation dynamics and market stress, we compute daily correlations between three time series: VaR submodularity violation rates, VaR subadditivity violation rates, and the CBOE Volatility Index (VIX). Table [3](#S6.T3 "Table 3 ‣ Subadditivity test and VIX correlation analysis. ‣ 6 Submodularity in financial data ‣ Submodular risk measures") reports Pearson, Spearman rank, and distance correlations for each window length and confidence level. The correlation between submodularity and subadditivity violation rates is consistently high across most configurations (Pearson 0.47–0.97, Spearman 0.48–0.89, distance 0.50–0.96), with the notable exception of the 250-day window at 99% confidence, where the correlation drops substantially (Pearson 0.47). This suggests that the lattice-based and portfolio-based notions of diversification failure tend to coincide: periods in which VaR fails submodularity are largely the same periods in which it fails subadditivity. Both violation rates also show moderate to strong positive correlation with the VIX. Pearson correlations between VIX and submodularity violation rates range from 0.20 to 0.53, while those between VIX and subadditivity violation rates range from 0.30 to 0.53, indicating that VaR diversification failures tend to coincide with periods of higher market volatility.

Table 3: Correlations between VIX, VaR submodularity violation rate, and VaR subadditivity violation rate

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Window | VaR Level | Correlation | VIX–Submod | VIX–Subadd | Submod–Subadd |
| 250 | 95% | Pearson | 0.531 | 0.534 | 0.952 |
|  |  | Spearman | 0.331 | 0.313 | 0.884 |
|  |  | Distance | 0.520 | 0.523 | 0.935 |
| 250 | 97.5% | Pearson | 0.506 | 0.509 | 0.967 |
|  |  | Spearman | 0.432 | 0.307 | 0.892 |
|  |  | Distance | 0.538 | 0.519 | 0.964 |
| 250 | 99% | Pearson | 0.201 | 0.527 | 0.467 |
|  |  | Spearman | 0.124 | 0.259 | 0.477 |
|  |  | Distance | 0.257 | 0.510 | 0.498 |
| 500 | 95% | Pearson | 0.437 | 0.485 | 0.931 |
|  |  | Spearman | 0.156 | 0.155 | 0.885 |
|  |  | Distance | 0.448 | 0.468 | 0.913 |
| 500 | 97.5% | Pearson | 0.339 | 0.300 | 0.865 |
|  |  | Spearman | 0.468 | 0.277 | 0.853 |
|  |  | Distance | 0.435 | 0.306 | 0.844 |
| 500 | 99% | Pearson | 0.487 | 0.415 | 0.935 |
|  |  | Spearman | 0.300 | 0.248 | 0.733 |
|  |  | Distance | 0.429 | 0.421 | 0.953 |
| N=1,780N=1{,}780 trading days for all configurations. | | | | | |
| --- | --- | --- | --- | --- | --- |

## 7 Conclusion

In the positively homogeneous (coherent) setting, submodularity is essentially characterized by comonotonic additivity and subadditivity; see Chateauneuf and Cornet ([2018](#bib.bib8 "Choquet representability of submodular functions")). In this paper, we investigate what
submodularity implies beyond positive homogeneity, focusing on law-invariant convex monetary risk measures on L∞L^{\infty} (and several closely related law-invariant functionals).

Our results show that submodularity is highly restrictive within classical families. Economically, lattice submodularity captures a strong form of diversification: it discourages comonotonic concentration and prevents double counting of common exposures through the inequality ρ​(X∨Y)+ρ​(X∧Y)≤ρ​(X)+ρ​(Y)\rho(X\vee Y)+\rho(X\wedge Y)\leq\rho(X)+\rho(Y). Mathematically, we obtain complete
characterizations in several explicit classes. Expected-loss functionals are both submodular and supermodular. Certainty equivalents are
submodular if and only if the underlying loss function is convex. Submodular coherent risk measures are exactly coherent distortion risk measures with concave distortions. For shortfall risk measures, we derive a sharp necessary-and-sufficient condition via the linear dominance inequality: writing L=infx∈ℝR​(x)L=\inf\_{x\in\mathbb{R}}R(x) and h​(x)=S​(x)​(R​(x)−2​L)h(x)=S(x)(R(x)-2L), the shortfall risk measure ρℓ\rho\_{\ell} is
submodular if and only if there exists λ∈ℝ\lambda\in\mathbb{R} such that h​(x)≤λ​ℓ​(x)h(x)\leq\lambda\,\ell(x) for all x∈ℝx\in\mathbb{R}. The loss-based optimized certainty equivalents are always submodular. For AES, we show that if the penalty function gg is nonconvex, then submodularity implies that ESg\mathrm{ES}^{g} equals a standard ESp\mathrm{ES}\_{p}; for convex gg, we conjecture a reduction to ES up to a constant. Finally, for monotone mean-deviation risk measures, submodularity can hold only in the coherent distortion cases.

## Appendix A Omitted proofs

### A1 Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures") without differentiability

We now extend Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures") to loss functions ℓ\ell that are not necessarily twice differentiable. Denote by S=ℓ+′S=\ell\_{+}^{\prime} the right derivative of ℓ\ell,

|  |  |  |
| --- | --- | --- |
|  | S​(u)=limh↓0ℓ​(u+h)−ℓ​(u)h,S(u)=\lim\_{h\downarrow 0}\frac{\ell(u+h)-\ell(u)}{h}, |  |

which exists and is strictly positive for every uu by convexity of ℓ\ell.

Since SS is positive and increasing, log⁡S\log S is well-defined and increasing. To handle points where log⁡S\log S is not differentiable, we work with one-sided Dini derivatives. For an extended-real function f:ℝ→[−∞,∞]f:\mathbb{R}\to[-\infty,\infty], define

|  |  |  |  |
| --- | --- | --- | --- |
|  | D+​f​(x)\displaystyle D^{+}f(x) | =lim suph↓0f​(x+h)−f​(x)h,\displaystyle=\limsup\_{h\downarrow 0}\frac{f(x+h)-f(x)}{h}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | D−​f​(x)\displaystyle D^{-}f(x) | =lim suph↓0f​(x)−f​(x−h)h,\displaystyle=\limsup\_{h\downarrow 0}\frac{f(x)-f(x-h)}{h}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | D¯−​f​(x)\displaystyle\underline{D}^{-}f(x) | =lim infh↓0f​(x)−f​(x−h)h,\displaystyle=\liminf\_{h\downarrow 0}\frac{f(x)-f(x-h)}{h}, |  |

and set

|  |  |  |
| --- | --- | --- |
|  | R+​(x)=D+​(log⁡S)​(x),R−​(x)=D−​(log⁡S)​(x),R¯−​(x)=D¯−​(log⁡S)​(x).R\_{+}(x)=D^{+}(\log S)(x),\qquad R\_{-}(x)=D^{-}(\log S)(x),\qquad\underline{R}\_{-}(x)=\underline{D}^{-}(\log S)(x). |  |

Define

|  |  |  |
| --- | --- | --- |
|  | R​(x)=min⁡{R+​(x),R¯−​(x)}∈[0,∞].R(x)=\min\{R\_{+}(x),\,\underline{R}\_{-}(x)\}\in[0,\infty]. |  |

The choice of R¯−\underline{R}\_{-} (rather than R−R\_{-}) is dictated by the lower bound in Lemma [2](#Thmlemma2 "Lemma 2. ‣ Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures") below. Since log⁡S\log S is increasing, R​(x)≥0R(x)\geq 0 for all xx; moreover, R​(x)=∞R(x)=\infty at any jump of log⁡S\log S. Set

|  |  |  |
| --- | --- | --- |
|  | L=infx∈ℝR​(x),h​(x)=S​(x)​(R​(x)−2​L).L=\inf\_{x\in\mathbb{R}}R(x),\qquad h(x)=S(x)\big(R(x)-2L\big). |  |

###### Theorem 7.

For a strictly increasing loss function ℓ\ell, the shortfall risk measure ρℓ\rho\_{\ell} is submodular if and only if there exists λ∈ℝ\lambda\in\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)≤λ​ℓ​(x),x∈ℝ.h(x)\leq\lambda\,\ell(x),\qquad x\in\mathbb{R}. |  | (25) |

###### Proof.

We follow the same route as in Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures"), to deal with finite spaces first, and then apply Lemma [1](#Thmlemma1 "Lemma 1. ‣ 4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").

Throughout, let n≥3n\geq 3 and work on ([n],2[n],ℙ)([n],2^{[n]},\mathbb{P}) with equal atom weight 1/n1/n. Identify each random variable XX with 𝐱=(X​(1),…,X​(n))∈ℝn\mathbf{x}=(X(1),\dots,X(n))\in\mathbb{R}^{n} and write m​(𝐱)=ρℓ​(X)m(\mathbf{x})=\rho\_{\ell}(X). Since ρℓ\rho\_{\ell} is monotone and cash invariant, mm is 11-Lipschitz in L∞L^{\infty}-norm. The defining equation 𝔼​[ℓ​(X−ρℓ​(X))]=0\mathbb{E}[\ell(X-\rho\_{\ell}(X))]=0 and ℓ​(0)=0\ell(0)=0 give

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nℓ​(xk−m​(𝐱))=0,𝐱∈ℝn.\sum\_{k=1}^{n}\ell(x\_{k}-m(\mathbf{x}))=0,\qquad\mathbf{x}\in\mathbb{R}^{n}. |  | (26) |

Sufficiency.
Assume ([25](#A1.E25 "In Theorem 7. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) holds. Since ℓ\ell is finite and S>0S>0, the inequality forces R​(x)<∞R(x)<\infty for every xx, so log⁡S\log S has no jumps and SS is continuous.

Differentiating ([26](#A1.E26 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) from the right in direction eje\_{j} and solving for ∇j+m\nabla^{+}\_{j}m yields the right-gradient formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇j+m​(𝐱)=wj​(𝐱),j∈[n],\nabla^{+}\_{j}m(\mathbf{x})=w\_{j}(\mathbf{x}),\qquad j\in[n], |  | (27) |

where

|  |  |  |
| --- | --- | --- |
|  | T​(𝐱)=∑k=1nS​(xk−m​(𝐱)),wj​(𝐱)=S​(xj−m​(𝐱))T​(𝐱).T(\mathbf{x})=\sum\_{k=1}^{n}S(x\_{k}-m(\mathbf{x})),\qquad w\_{j}(\mathbf{x})=\frac{S(x\_{j}-m(\mathbf{x}))}{T(\mathbf{x})}. |  |

Fix i≠ji\neq j and write yk=xk−m​(𝐱)y\_{k}=x\_{k}-m(\mathbf{x}). Since SS is monotone, it is differentiable almost everywhere, with S′​(yk)=S​(yk)​R​(yk)S^{\prime}(y\_{k})=S(y\_{k})R(y\_{k}) at differentiability points. Differentiating wiw\_{i} in direction eje\_{j} via ([27](#A1.E27 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) gives, for almost every 𝐱\mathbf{x},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇j+∇i+⁡m​(𝐱)=−wi​wj​(R​(yi)+R​(yj)−∑k=1nwk​R​(yk)).\nabla^{+}\_{j}\nabla^{+}\_{i}m(\mathbf{x})=-w\_{i}w\_{j}\Big(R(y\_{i})+R(y\_{j})-\sum\_{k=1}^{n}w\_{k}R(y\_{k})\Big). |  | (28) |

Summing ([25](#A1.E25 "In Theorem 7. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) over kk at the points yky\_{k} and using ∑kℓ​(yk)=0\sum\_{k}\ell(y\_{k})=0 yields

|  |  |  |
| --- | --- | --- |
|  | ∑k=1nwk​R​(yk)≤2​L.\sum\_{k=1}^{n}w\_{k}R(y\_{k})\leq 2L. |  |

Since R​(yi)+R​(yj)≥2​LR(y\_{i})+R(y\_{j})\geq 2L, the parenthesized expression in ([28](#A1.E28 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) is nonnegative. Therefore,

|  |  |  |
| --- | --- | --- |
|  | ∇j+∇i+⁡m​(𝐱)≤0for almost every ​𝐱.\nabla\_{j}^{+}\nabla\_{i}^{+}m(\mathbf{x})\leq 0\qquad\text{for almost every }\mathbf{x}. |  |

By Theorem 3.9.3(a) of Müller and Stoyan ([2002](#bib.bib17 "Comparison methods for stochastic models and risks")), this implies that mm is submodular on ℝn\mathbb{R}^{n}.

The necessity proof relies on the following lemma, which provides a one-sided analogue of ([28](#A1.E28 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) without differentiability.

###### Lemma 2.

Assume S:ℝ→(0,∞)S:\mathbb{R}\to(0,\infty) is continuous and increasing. Let 𝐳∈ℝn\mathbf{z}\in\mathbb{R}^{n} satisfy m​(𝐳)=0m(\mathbf{z})=0, fix i≠ji\neq j, and set

|  |  |  |
| --- | --- | --- |
|  | K=∑k=1nS​(zk),wk=wk​(𝐳)=S​(zk)K.K=\sum\_{k=1}^{n}S(z\_{k}),\qquad w\_{k}=w\_{k}(\mathbf{z})=\frac{S(z\_{k})}{K}. |  |

Assume R+​(zi)R\_{+}(z\_{i}) is finite, and that R−​(zk)R\_{-}(z\_{k}) and R¯−​(zk)\underline{R}\_{-}(z\_{k}) are finite for every k≠ik\neq i. For t≥0t\geq 0, write 𝐳​(t)=𝐳+t​ei\mathbf{z}(t)=\mathbf{z}+te\_{i} and wk​(t)=wk​(𝐳​(t))w\_{k}(t)=w\_{k}(\mathbf{z}(t)). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim inft↓0wj​(t)−wjt≥−wi​wj​(R+​(zi)+R−​(zj)−wi​R+​(zi)−∑k≠iwk​R¯−​(zk)).\liminf\_{t\downarrow 0}\frac{w\_{j}(t)-w\_{j}}{t}\geq-w\_{i}w\_{j}\Big(R\_{+}(z\_{i})+R\_{-}(z\_{j})-w\_{i}R\_{+}(z\_{i})-\sum\_{k\neq i}w\_{k}\,\underline{R}\_{-}(z\_{k})\Big). |  | (29) |

###### Proof.

Since mm is 11-Lipschitz and m​(𝐳)=0m(\mathbf{z})=0, we have 0≤m​(t)=m​(𝐳​(t))≤t0\leq m(t)=m(\mathbf{z}(t))\leq t along the path 𝐳​(t)\mathbf{z}(t), and the right-gradient formula gives m​(t)/t→wim(t)/t\to w\_{i} as t↓0t\downarrow 0.

Set δk​(t)=log⁡S​(zk​(t)−m​(t))−log⁡S​(zk)\delta\_{k}(t)=\log S(z\_{k}(t)-m(t))-\log S(z\_{k}). Then

|  |  |  |
| --- | --- | --- |
|  | log⁡wj​(t)−log⁡wj=δj​(t)−log⁡(∑k=1nwk​eδk​(t)).\log w\_{j}(t)-\log w\_{j}=\delta\_{j}(t)-\log\!\Big(\sum\_{k=1}^{n}w\_{k}\,e^{\delta\_{k}(t)}\Big). |  |

Using ex−1≥xe^{x}-1\geq x in wj​(t)=wj​exp⁡(log⁡wj​(t)−log⁡wj)w\_{j}(t)=w\_{j}\exp(\log w\_{j}(t)-\log w\_{j}) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | wj​(t)−wjt≥wj​(δj​(t)t−1t​log⁡(∑k=1nwk​eδk​(t))).\frac{w\_{j}(t)-w\_{j}}{t}\geq w\_{j}\bigg(\frac{\delta\_{j}(t)}{t}-\frac{1}{t}\log\!\Big(\sum\_{k=1}^{n}w\_{k}\,e^{\delta\_{k}(t)}\Big)\bigg). |  | (30) |

For the first term: since zj​(t)=zjz\_{j}(t)=z\_{j} and m​(t)/t→wim(t)/t\to w\_{i},

|  |  |  |
| --- | --- | --- |
|  | lim inft↓0δj​(t)t=lim inft↓0log⁡S​(zj−m​(t))−log⁡S​(zj)t≥−wi​R−​(zj).\liminf\_{t\downarrow 0}\frac{\delta\_{j}(t)}{t}=\liminf\_{t\downarrow 0}\frac{\log S(z\_{j}-m(t))-\log S(z\_{j})}{t}\geq-w\_{i}R\_{-}(z\_{j}). |  |

For the second term: the finiteness assumptions on the Dini derivatives imply the required local first-order control near t=0t=0. Hence there exist constants C>0C>0 and t0>0t\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | log⁡(∑k=1nwk​eδk​(t))≤∑k=1nwk​δk​(t)+C​t2,0<t<t0,\log\!\Big(\sum\_{k=1}^{n}w\_{k}e^{\delta\_{k}(t)}\Big)\leq\sum\_{k=1}^{n}w\_{k}\delta\_{k}(t)+Ct^{2},\qquad 0<t<t\_{0}, |  |

which yields

|  |  |  |
| --- | --- | --- |
|  | lim supt↓01t​log⁡(∑k=1nwk​eδk​(t))≤∑k=1nwk​lim supt↓0δk​(t)t.\limsup\_{t\downarrow 0}\frac{1}{t}\log\!\Big(\sum\_{k=1}^{n}w\_{k}\,e^{\delta\_{k}(t)}\Big)\leq\sum\_{k=1}^{n}w\_{k}\limsup\_{t\downarrow 0}\frac{\delta\_{k}(t)}{t}. |  |

For k=ik=i, since zi​(t)=zi+tz\_{i}(t)=z\_{i}+t and m​(t)/t→wim(t)/t\to w\_{i}, we have lim supt↓0δi​(t)/t≤(1−wi)​R+​(zi)\limsup\_{t\downarrow 0}\delta\_{i}(t)/t\leq(1-w\_{i})R\_{+}(z\_{i}). For k≠ik\neq i, since zk​(t)=zkz\_{k}(t)=z\_{k}, we have lim supt↓0δk​(t)/t≤−wi​R¯−​(zk)\limsup\_{t\downarrow 0}\delta\_{k}(t)/t\leq-w\_{i}\,\underline{R}\_{-}(z\_{k}). Therefore

|  |  |  |
| --- | --- | --- |
|  | lim supt↓01t​log⁡(∑k=1nwk​eδk​(t))≤wi​(1−wi)​R+​(zi)−wi​∑k≠iwk​R¯−​(zk).\limsup\_{t\downarrow 0}\frac{1}{t}\log\!\Big(\sum\_{k=1}^{n}w\_{k}\,e^{\delta\_{k}(t)}\Big)\leq w\_{i}(1-w\_{i})R\_{+}(z\_{i})-w\_{i}\sum\_{k\neq i}w\_{k}\,\underline{R}\_{-}(z\_{k}). |  |

Substituting both estimates into ([30](#A1.E30 "In Proof. ‣ Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) and rearranging gives ([29](#A1.E29 "In Lemma 2. ‣ Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")).
∎

Necessity.
Assume ρℓ\rho\_{\ell} is submodular, so mm is submodular on ℝn\mathbb{R}^{n} for every n≥3n\geq 3. The proof proceeds in three steps.

*Step 1: SS is continuous.*
Suppose for contradiction that SS has a jump at some point, which by cash invariance we may take to be 0:

|  |  |  |
| --- | --- | --- |
|  | s−=S​(0−)<S​(0+)=s+.s\_{-}=S(0^{-})<S(0^{+})=s\_{+}. |  |

Consider 𝐱=(−2​h,−h,0)\mathbf{x}=(-2h,-h,0) and 𝐲=(−h,−h,−h)=−h​𝟏\mathbf{y}=(-h,-h,-h)=-h\mathbf{1} in ℝ3\mathbb{R}^{3}, so that

|  |  |  |
| --- | --- | --- |
|  | 𝐱∨𝐲=(−h,−h,0),𝐱∧𝐲=(−2​h,−h,−h).\mathbf{x}\vee\mathbf{y}=(-h,-h,0),\qquad\mathbf{x}\wedge\mathbf{y}=(-2h,-h,-h). |  |

Write m​(𝐱)=−αh​hm(\mathbf{x})=-\alpha\_{h}h, m​(𝐱∨𝐲)=−βh​hm(\mathbf{x}\vee\mathbf{y})=-\beta\_{h}h, m​(𝐱∧𝐲)=−γh​hm(\mathbf{x}\wedge\mathbf{y})=-\gamma\_{h}h, and note m​(𝐲)=−hm(\mathbf{y})=-h. Dividing the defining equation ([26](#A1.E26 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) by hh and sending h↓0h\downarrow 0, using the left and right derivatives s−s\_{-} and s+s\_{+} of ℓ\ell at 0, yields limiting values

|  |  |  |
| --- | --- | --- |
|  | α=3​s−2​s−+s+,β=2​s−2​s−+s+,γ=2​(s−+s+)s−+2​s+.\alpha=\frac{3s\_{-}}{2s\_{-}+s\_{+}},\qquad\beta=\frac{2s\_{-}}{2s\_{-}+s\_{+}},\qquad\gamma=\frac{2(s\_{-}+s\_{+})}{s\_{-}+2s\_{+}}. |  |

The submodularity deficit is

|  |  |  |
| --- | --- | --- |
|  | Δh=m​(𝐱)+m​(𝐲)−m​(𝐱∨𝐲)−m​(𝐱∧𝐲)=(βh+γh−αh−1)​h,\Delta\_{h}=m(\mathbf{x})+m(\mathbf{y})-m(\mathbf{x}\vee\mathbf{y})-m(\mathbf{x}\wedge\mathbf{y})=(\beta\_{h}+\gamma\_{h}-\alpha\_{h}-1)\,h, |  |

and passing to the limit gives

|  |  |  |
| --- | --- | --- |
|  | Δhh→β+γ−α−1=s−​(s−−s+)(s−+2​s+)​(2​s−+s+)<0,\frac{\Delta\_{h}}{h}\to\beta+\gamma-\alpha-1=\frac{s\_{-}(s\_{-}-s\_{+})}{(s\_{-}+2s\_{+})(2s\_{-}+s\_{+})}<0, |  |

contradicting submodularity. Hence SS is continuous on ℝ\mathbb{R}.

Since SS is continuous, positive, and increasing, log⁡S\log S is continuous and monotone. By Lebesgue’s differentiation theorem, R​(x)<∞R(x)<\infty for almost every xx.

*Step 2: A balanced-sum inequality.*
We show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1rh​(xk)≤0whenever∑k=1rℓ​(xk)=0.\sum\_{k=1}^{r}h(x\_{k})\leq 0\qquad\text{whenever}\quad\sum\_{k=1}^{r}\ell(x\_{k})=0. |  | (31) |

Fix ε>0\varepsilon>0 and choose vv such that R​(v)≤L+εR(v)\leq L+\varepsilon and SS is differentiable at vv; this is possible since the set of differentiability points has full measure and L=infRL=\inf R.
Pick p∈ℝp\in\mathbb{R} with ℓ​(p)≠0\ell(p)\neq 0 and ℓ​(p)​ℓ​(v)<0\ell(p)\ell(v)<0, and let
M=⌊−2​ℓ​(v)/ℓ​(p)⌋M=\lfloor-2\ell(v)/\ell(p)\rfloor,
so that the residual d=−2​ℓ​(v)−M​ℓ​(p)d=-2\ell(v)-M\ell(p) satisfies d​ℓ​(p)≥0d\,\ell(p)\geq 0 and |d|<|ℓ​(p)||d|<|\ell(p)|. By continuity and strict monotonicity of ℓ\ell, there is a unique cc with ℓ​(c)=d\ell(c)=d.

Now fix x1,…,xrx\_{1},\dots,x\_{r} with ∑k=1rℓ​(xk)=0\sum\_{k=1}^{r}\ell(x\_{k})=0. For each N∈ℕN\in\mathbb{N}, form the vector 𝐳(N)∈ℝn\mathbf{z}^{(N)}\in\mathbb{R}^{n} (with n=M+N​r+3n=M+Nr+3) consisting of two copies of vv, MM copies of pp, one copy of cc, and NN copies of (x1,…,xr)(x\_{1},\dots,x\_{r}). By construction, ∑kℓ​(zk(N))=0\sum\_{k}\ell(z\_{k}^{(N)})=0, hence m​(𝐳(N))=0m(\mathbf{z}^{(N)})=0.

Apply submodularity to the pair of vv-entries: for t,s>0t,s>0,

|  |  |  |
| --- | --- | --- |
|  | m​(𝐳(N))+m​(𝐳(N)+t​ei+s​ej)≤m​(𝐳(N)+t​ei)+m​(𝐳(N)+s​ej).m(\mathbf{z}^{(N)})+m(\mathbf{z}^{(N)}+te\_{i}+se\_{j})\leq m(\mathbf{z}^{(N)}+te\_{i})+m(\mathbf{z}^{(N)}+se\_{j}). |  |

Dividing by ss, sending s↓0s\downarrow 0 (using the right-gradient formula), then dividing by tt and sending t↓0t\downarrow 0 yields

|  |  |  |
| --- | --- | --- |
|  | lim inft↓0wj​(𝐳(N)+t​ei)−wj​(𝐳(N))t≤0.\liminf\_{t\downarrow 0}\frac{w\_{j}(\mathbf{z}^{(N)}+te\_{i})-w\_{j}(\mathbf{z}^{(N)})}{t}\leq 0. |  |

Lemma [2](#Thmlemma2 "Lemma 2. ‣ Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures") provides a matching lower bound. Since zi(N)=zj(N)=vz\_{i}^{(N)}=z\_{j}^{(N)}=v and SS is differentiable at vv, all one-sided Dini derivatives at vv coincide with R​(v)R(v). (For coordinates k≠ik\neq i, the finiteness assumptions of the lemma hold after an arbitrarily small perturbation, which we then let vanish.) Combining the upper and lower bounds gives

|  |  |  |
| --- | --- | --- |
|  | ∑k=1nwk​(𝐳(N))​R​(zk(N))≤2​R​(v).\sum\_{k=1}^{n}w\_{k}(\mathbf{z}^{(N)})R(z\_{k}^{(N)})\leq 2R(v). |  |

Multiplying by K=∑kS​(zk(N))K=\sum\_{k}S(z\_{k}^{(N)}) and isolating the NN repeated blocks,

|  |  |  |
| --- | --- | --- |
|  | N​∑k=1rS​(xk)​(R​(xk)−2​R​(v))≤2​S​(v)​R​(v)−A,N\sum\_{k=1}^{r}S(x\_{k})\big(R(x\_{k})-2R(v)\big)\leq 2S(v)R(v)-A, |  |

where A=M​S​(p)​(R​(p)−2​R​(v))+S​(c)​(R​(c)−2​R​(v))A=MS(p)(R(p)-2R(v))+S(c)(R(c)-2R(v)) is independent of NN. Dividing by NN and letting N→∞N\to\infty yields ∑k=1rS​(xk)​(R​(xk)−2​R​(v))≤0\sum\_{k=1}^{r}S(x\_{k})(R(x\_{k})-2R(v))\leq 0. Since R​(v)≤L+εR(v)\leq L+\varepsilon,

|  |  |  |
| --- | --- | --- |
|  | ∑k=1rh​(xk)=∑k=1rS​(xk)​(R​(xk)−2​L)≤2​ε​∑k=1rS​(xk),\sum\_{k=1}^{r}h(x\_{k})=\sum\_{k=1}^{r}S(x\_{k})\big(R(x\_{k})-2L\big)\leq 2\varepsilon\sum\_{k=1}^{r}S(x\_{k}), |  |

and sending ε↓0\varepsilon\downarrow 0 gives ([31](#A1.E31 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")).

*Step 3: From the balanced-sum inequality to ([25](#A1.E25 "In Theorem 7. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")).*
Define ϕ​(x)=h​(x)/ℓ​(x)\phi(x)=h(x)/\ell(x) for ℓ​(x)≠0\ell(x)\neq 0 and set

|  |  |  |
| --- | --- | --- |
|  | α+=supℓ​(x)>0ϕ​(x),α−=infℓ​(x)<0ϕ​(x).\alpha^{+}=\sup\_{\ell(x)>0}\phi(x),\qquad\alpha^{-}=\inf\_{\ell(x)<0}\phi(x). |  |

We claim α+≤α−\alpha^{+}\leq\alpha^{-}, both finite; any λ∈[α+,α−]\lambda\in[\alpha^{+},\alpha^{-}] then satisfies ([25](#A1.E25 "In Theorem 7. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) for all xx with ℓ​(x)≠0\ell(x)\neq 0, and ([31](#A1.E31 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) applied to the singleton {0}\{0\} gives h​(0)≤0h(0)\leq 0, which is ([25](#A1.E25 "In Theorem 7. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) at x=0x=0.

Fix a,b∈ℝa,b\in\mathbb{R} with ℓ​(a)<0<ℓ​(b)\ell(a)<0<\ell(b) and set θ=ℓ​(b)/(ℓ​(b)−ℓ​(a))∈(0,1)\theta=\ell(b)/(\ell(b)-\ell(a))\in(0,1), so that θ​ℓ​(a)+(1−θ)​ℓ​(b)=0\theta\ell(a)+(1-\theta)\ell(b)=0.

By Dirichlet’s approximation theorem (or directly, if θ\theta is rational), there exist infinitely many pairs (rN,N)(r\_{N},N) with 1≤rN≤N−11\leq r\_{N}\leq N-1 and |θ−rN/N|<1/N2|\theta-r\_{N}/N|<1/N^{2}. Set sN=N−rNs\_{N}=N-r\_{N} and

|  |  |  |
| --- | --- | --- |
|  | δN=−(rN​ℓ​(a)+sN​ℓ​(b))=(ℓ​(b)−ℓ​(a))​(rN−θ​N),\delta\_{N}=-(r\_{N}\ell(a)+s\_{N}\ell(b))=(\ell(b)-\ell(a))(r\_{N}-\theta N), |  |

so |δN|≤|ℓ​(b)−ℓ​(a)|/N→0|\delta\_{N}|\leq|\ell(b)-\ell(a)|/N\to 0.

Fix A>0A>0 with [−2​A,2​A]⊂ℓ​((−1,1))[-2A,2A]\subset\ell((-1,1)) and set I=ℓ−1​([−2​A,2​A])⊂(−1,1)I=\ell^{-1}([-2A,2A])\subset(-1,1), I0=ℓ−1​([−A,A])⊂II\_{0}=\ell^{-1}([-A,A])\subset I. For NN large enough that |δN|≤A|\delta\_{N}|\leq A, define

|  |  |  |
| --- | --- | --- |
|  | TN​(x)=ℓ−1​(δN−ℓ​(x)),x∈I0,T\_{N}(x)=\ell^{-1}(\delta\_{N}-\ell(x)),\qquad x\in I\_{0}, |  |

so that ℓ​(x)+ℓ​(TN​(x))=δN\ell(x)+\ell(T\_{N}(x))=\delta\_{N} and TN​(I0)⊂IT\_{N}(I\_{0})\subset I. Let MN=NM\_{N}=\sqrt{N} and

|  |  |  |
| --- | --- | --- |
|  | HN={x∈I:h​(x)​ is finite and ​|h​(x)|≤MN}.H\_{N}=\{x\in I:h(x)\text{ is finite and }|h(x)|\leq M\_{N}\}. |  |

Since hh is finite almost everywhere and MN→∞M\_{N}\to\infty, we have |I∖HN|→0|I\setminus H\_{N}|\to 0.

Since SS is bounded between positive constants m≤Mm\leq M on the compact interval II, the maps ℓ\ell and ℓ−1\ell^{-1} are bi-Lipschitz on II and ℓ​(I)\ell(I), hence TN−1T\_{N}^{-1} is KK-Lipschitz with K=M/mK=M/m. Therefore |TN−1​(I∖HN)|≤K​|I∖HN||T\_{N}^{-1}(I\setminus H\_{N})|\leq K|I\setminus H\_{N}|, and

|  |  |  |
| --- | --- | --- |
|  | |I0∖(HN∩TN−1​(HN))|≤(1+K)​|I∖HN|→0.|I\_{0}\setminus(H\_{N}\cap T\_{N}^{-1}(H\_{N}))|\leq(1+K)|I\setminus H\_{N}|\to 0. |  |

For large NN, the set HN∩TN−1​(HN)∩I0H\_{N}\cap T\_{N}^{-1}(H\_{N})\cap I\_{0} has positive measure. Pick cNc\_{N} in this set and set dN=TN​(cN)d\_{N}=T\_{N}(c\_{N}). Then cN,dN∈HNc\_{N},d\_{N}\in H\_{N}, so |h​(cN)|,|h​(dN)|≤N|h(c\_{N})|,|h(d\_{N})|\leq\sqrt{N}, and

|  |  |  |
| --- | --- | --- |
|  | rN​ℓ​(a)+sN​ℓ​(b)+ℓ​(cN)+ℓ​(dN)=0.r\_{N}\ell(a)+s\_{N}\ell(b)+\ell(c\_{N})+\ell(d\_{N})=0. |  |

Applying ([31](#A1.E31 "In Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures")) to this multiset (rNr\_{N} copies of aa, sNs\_{N} copies of bb, and the pair cN,dNc\_{N},d\_{N}), dividing by NN, and letting N→∞N\to\infty (the correction (h​(cN)+h​(dN))/N→0(h(c\_{N})+h(d\_{N}))/N\to 0) gives

|  |  |  |
| --- | --- | --- |
|  | θ​h​(a)+(1−θ)​h​(b)≤0,\theta\,h(a)+(1-\theta)\,h(b)\leq 0, |  |

which rearranges to ϕ​(b)≤ϕ​(a)\phi(b)\leq\phi(a), that is, h​(b)/ℓ​(b)≤h​(a)/ℓ​(a)h(b)/\ell(b)\leq h(a)/\ell(a). Taking the supremum over bb and infimum over aa yields α+≤α−\alpha^{+}\leq\alpha^{-}. Finiteness follows by fixing one of aa or bb. This completes the proof.
∎

### A2 Stock selection

In the table below we give the list of stocks used in Section [6](#S6 "6 Submodularity in financial data ‣ Submodular risk measures").

Table 4: Top five S&P 500 constituents by market capitalization per GICS sector

| GICS Sector | Ticker | Company | Mkt Cap ($B) |
| --- | --- | --- | --- |
| Communication Services | GOOGL | Alphabet (Class A) | 644.5 |
| META | Meta Platforms | 446.9 |
| DIS | Walt Disney | 184.8 |
| VZ | Verizon Communications | 142.3 |
| T | AT&T | 114.1 |
| Consumer Discretionary | AMZN | Amazon | 632.1 |
| HD | Home Depot | 153.5 |
| MCD | McDonald’s | 101.8 |
| CCL | Carnival | 85.7 |
| NKE | Nike | 85.0 |
| Consumer Staples | WMT | Walmart | 230.9 |
| PG | Procter & Gamble | 172.1 |
| KO | Coca-Cola | 154.5 |
| PEP | PepsiCo | 127.4 |
| PM | Philip Morris | 107.0 |
| Energy | XOM | ExxonMobil | 237.9 |
| CVX | Chevron | 169.5 |
| SLB | Schlumberger | 77.1 |
| OXY | Occidental Petroleum | 58.1 |
| COP | ConocoPhillips | 50.8 |
| Financials | BRK-B | Berkshire Hathaway | 426.7 |
| JPM | JPMorgan Chase | 229.0 |
| V | Visa | 204.1 |
| BAC | Bank of America | 178.4 |
| WFC | Wells Fargo | 150.4 |
| Health Care | JNJ | Johnson & Johnson | 270.6 |
| UNH | UnitedHealth | 177.2 |
| PFE | Pfizer | 135.6 |
| ABBV | AbbVie | 121.4 |
| MRK | Merck | 103.4 |
| Industrials | BA | Boeing | 223.0 |
| RTX | RTX Corporation | 88.6 |
| GE | General Electric | 82.5 |
| HON | Honeywell | 79.4 |
| MMM | 3M | 78.5 |
| Information Technology | AAPL | Apple | 599.6 |
| MSFT | Microsoft | 583.3 |
| INTC | Intel | 199.4 |
| ORCL | Oracle | 121.8 |
| CSCO | Cisco Systems | 119.9 |
| Materials | LIN | Linde | 62.9 |
| ECL | Ecolab | 34.9 |
| SHW | Sherwin-Williams | 31.9 |
| IFF | International Flavors | 31.8 |
| NEM | Newmont | 31.7 |
| Real Estate | AMT | American Tower | 53.2 |
| PLD | Prologis | 46.9 |
| SPG | Simon Property Group | 40.1 |
| EQIX | Equinix | 37.5 |
| O | Realty Income | 34.0 |
| Utilities | PCG | PG&E | 111.1 |
| NEE | NextEra Energy | 65.1 |
| D | Dominion Energy | 47.7 |
| DUK | Duke Energy | 47.0 |
| SO | Southern Company | 39.3 |

Market capitalizations are approximate values as of January 2, 2018, computed from historical shares outstanding and historical adjusted closing prices via the yfinance API. S&P 500 constituent list from the datasets/s-and-p-500-companies GitHub repository.

## References

* A. Ben-Tal and M. Teboulle (2007)
  An old-new concept of convex risk measures: the optimized certainty equivalent.
  Mathematical Finance 17 (3),  pp. 449–476.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Submodular risk measures"),
  [§4.2](#S4.SS2.p1.1 "4.2 Optimized certainty equivalents ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").
* J. Bilmes (2022)
  Submodularity in machine learning and artificial intelligence.
  arXiv preprint arXiv:2202.00132.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Submodular risk measures"),
  [§5](#S5.p1.18 "5 Discussion: Submodularity on sets ‣ Submodular risk measures").
* M. Burzoni, C. Munari, and R. Wang (2022)
  Adjusted Expected Shortfall.
  Journal of Banking and Finance 134,  pp. 106297.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Submodular risk measures"),
  [§4.3](#S4.SS3.p1.3 "4.3 Adjusted ES ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures"),
  [§4.3](#S4.SS3.p2.7 "4.3 Adjusted ES ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").
* A. Chateauneuf and B. Cornet (2018)
  Choquet representability of submodular functions.
  Mathematical Programming Series B 168,  pp. 615–629.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Submodular risk measures"),
  [§1](#S1.p5.1 "1 Introduction ‣ Submodular risk measures"),
  [§2](#S2.p5.4 "2 Choquet integrals and risk measures ‣ Submodular risk measures"),
  [§2](#S2.p6.2 "2 Choquet integrals and risk measures ‣ Submodular risk measures"),
  [§3.3](#S3.SS3.3.p3.3 "Proof. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"),
  [§3.3](#S3.SS3.4.p4.1 "Proof. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"),
  [§3.3](#S3.SS3.6.p6.1 "Proof. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"),
  [§3.3](#S3.SS3.p2.1 "3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"),
  [§7](#S7.p1.1 "7 Conclusion ‣ Submodular risk measures").
* P. Embrechts, T. Mao, Q. Wang, and R. Wang (2021)
  Bayes risk, elicitability, and the expected shortfall.
  Mathematical Finance 31 (4),  pp. 1190–1217.
  Cited by: [§2](#S2.p5.13 "2 Choquet integrals and risk measures ‣ Submodular risk measures").
* H. Föllmer and A. Schied (2002)
  Convex measures of risk and trading constraints.
  Finance and Stochastics 6 (4),  pp. 429–447.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Submodular risk measures"),
  [§4.1](#S4.SS1.p1.2 "4.1 Shortfall risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").
* H. Föllmer and A. Schied (2016)
  Stochastic finance. an introduction in discrete time.
  4 edition, Walter de Gruyter, Berlin.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Submodular risk measures"),
  [§2](#S2.p2.6 "2 Choquet integrals and risk measures ‣ Submodular risk measures").
* S. Ghamami and P. Glasserman (2019)
  Submodular risk allocation.
  Management Science 65 (10),  pp. 4656–4675.
  Cited by: [§1](#S1.p7.1 "1 Introduction ‣ Submodular risk measures"),
  [§5](#S5.p1.18 "5 Discussion: Submodularity on sets ‣ Submodular risk measures").
* X. Han, R. Wang, and Q. Wu (2026)
  Monotonic mean-deviation risk measures.
  Finance and Stochastics.
  Note: Published online 4 February 2026
  External Links: [Document](https://dx.doi.org/10.1007/s00780-026-00586-8)
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Submodular risk measures"),
  [§4.4](#S4.SS4.p1.5 "4.4 Monotone mean-deviation risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures"),
  [§4.4](#S4.SS4.p1.6 "4.4 Monotone mean-deviation risk measures ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").
* M. Marinacci and L. Montrucchio (2004)
  Introduction to the mathematics of ambiguity.
  In Uncertainty in Economic Theory, I. Gilboa (Ed.),
   pp. 46–107.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Submodular risk measures").
* M. Marinacci and L. Montrucchio (2008)
  On concavity and supermodularity.
  Journal of Mathematical Analysis and Applications 344 (2),  pp. 642–654.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Submodular risk measures"),
  [§2](#S2.p7.1 "2 Choquet integrals and risk measures ‣ Submodular risk measures").
* A. J. McNeil, R. Frey, and P. Embrechts (2015)
  Quantitative risk management: concepts, techniques and tools-revised edition.
   Princeton university press.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Submodular risk measures").
* A. Müller and D. Stoyan (2002)
  Comparison methods for stochastic models and risks.
   Wiley.
  Cited by: [§A1](#A1.SS1.5.p5.13 "Proof. ‣ A1 Theorem 3 without differentiability ‣ Appendix A Omitted proofs ‣ Submodular risk measures").
* G. Pesenti, Q. Wang, and R. Wang (2025)
  Optimizing distortion riskmetrics with distributional uncertainty.
  Mathematical Programming 213 (1–2),  pp. 51–106.
  Note: arXiv:2011.04889
  External Links: [Document](https://dx.doi.org/10.1007/s10107-024-02128-6)
  Cited by: [§4.3](#S4.SS3.4.p4.14 "Proof. ‣ 4.3 Adjusted ES ‣ 4 Four classes of convex risk measures ‣ Submodular risk measures").
* L. Rüschendorf (2013)
  Mathematical risk analysis. dependence, risk bounds, optimal allocations and portfolios.
   Springer, Heidelberg.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Submodular risk measures").
* D. Schmeidler (1986)
  Integral representation without additivity.
  Proceedings of the American Mathematical Society 97 (2),  pp. 255–261.
  Cited by: [§2](#S2.p5.24 "2 Choquet integrals and risk measures ‣ Submodular risk measures"),
  [§3.3](#S3.SS3.5.p5.1 "Proof. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures").
* P. Tradacete and I. Villanueva (2020)
  Valuations on Banach lattices.
  International Mathematics Research Notices 2020 (8),  pp. 2468–2500.
  Cited by: [§3.1](#S3.SS1.4.p4.37 "Proof. ‣ 3.1 Expected losses ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures").
* R. Wang, Y. Wei, and G. E. Willmot (2020)
  Characterization, robustness and aggregation of signed Choquet integrals.
  Mathematics of Operations Research 45 (3),  pp. 993–1015.
  Cited by: [§3.3](#S3.SS3.p1.11 "3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures").
* M. E. Yaari (1987)
  The dual theory of choice under risk.
  Econometrica 55 (1),  pp. 95–115.
  Cited by: [§3.3](#S3.SS3.5.p5.1 "Proof. ‣ 3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"),
  [§3.3](#S3.SS3.p2.1 "3.3 Distortion risk measures ‣ 3 Expected losses and distortion risk measures ‣ Submodular risk measures"),
  [§3](#S3.p1.1 "3 Expected losses and distortion risk measures ‣ Submodular risk measures").

BETA