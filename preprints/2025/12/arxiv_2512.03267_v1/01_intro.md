---
authors:
- Aline Goulard
- Karl Grosse-Erdmann
doc_id: arxiv:2512.03267v1
family_id: arxiv:2512.03267
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures
url_abs: http://arxiv.org/abs/2512.03267v1
url_html: https://arxiv.org/html/2512.03267v1
venue: arXiv q-fin
version: 1
year: 2025
---


Aline Goulard and Karl Grosse-Erdmann
Aline Goulard,
Département de Mathématique, Université de Mons, 20 Place du Parc, 7000 Mons, Belgium
[alinegoulard@gmail.com](mailto:alinegoulard@gmail.com)
Karl Grosse-Erdmann,
Département de Mathématique, Université de Mons, 20 Place du Parc, 7000 Mons, Belgium
[kg.grosse-erdmann@umons.ac.be](mailto:kg.grosse-erdmann@umons.ac.be)

###### Abstract.

In financial and actuarial research, distortion and Haezendonck-Goovaerts risk measures are attractive due to their strong properties. They have so far been treated separately. In this paper, following a suggestion by Goovaerts, Linders, Van Weert, and Tank, we introduce and study a new class of risk measure that encompasses the distortion and Haezendonck-Goovaerts risk measures, aptly called the distortion Haezendonck-Goovaerts risk measures. They will be defined on a larger space than the space of bounded risks. We provide situations where these new risk measures are coherent, and explore their risk theoretic properties.

###### Key words and phrases:

Distortion risk measure, Orlicz premium, Haezendonck-Goovaerts risk measure, Orlicz-Lorentz premium, distortion Haezendonck-Goovaerts risk measure, coherent risk measure, Fatou property

###### 2020 Mathematics Subject Classification:

Primary 91G70; Secondary 46E30

## 1. Introduction

Risk measures occupy a prominent role in financial and actuarial research, see [[14](https://arxiv.org/html/2512.03267v1#bib.bib14)], [[21](https://arxiv.org/html/2512.03267v1#bib.bib21)], [[49](https://arxiv.org/html/2512.03267v1#bib.bib49)], and [[50](https://arxiv.org/html/2512.03267v1#bib.bib50)]. The most basic risk measure is Value at Risk VaRα, 0<α≤10<\alpha\leq 1, which is simply the quantile of order α\alpha of a given risk XX: VaR(X)α=FX−1(α){}\_{\alpha}(X)=F\_{X}^{-1}(\alpha). Once it was recognized that VaR does not satisfy the desirable property of subadditivity (but see the discussion in [[17](https://arxiv.org/html/2512.03267v1#bib.bib17)]), more advanced risk measures were proposed and studied. The best known subadditive alternative to VaR is the Tail Value at Risk TVaRα, 0<α<10<\alpha<1, also known as Expected Shortfall, Average Value at Risk or Conditional Value at Risk, which is a weighted (or distorted) version of VaR. Using different weight functions, one is led to the large and well-studied family of distortion risk measures, defined by

|  |  |  |
| --- | --- | --- |
|  | ρg​(X)=∫01FX−1​(1−u)​dg​(u),\rho\_{g}(X)=\int\_{0}^{1}F\_{X}^{-1}(1-u)\mathrm{d}g(u), |  |

where gg is a distortion function. The literature on these risk measures is extensive, see for example [[3](https://arxiv.org/html/2512.03267v1#bib.bib3)], [[16](https://arxiv.org/html/2512.03267v1#bib.bib16)], [[18](https://arxiv.org/html/2512.03267v1#bib.bib18)], [[27](https://arxiv.org/html/2512.03267v1#bib.bib27)], and [[55](https://arxiv.org/html/2512.03267v1#bib.bib55)]; see also [[30](https://arxiv.org/html/2512.03267v1#bib.bib30)] and [[57](https://arxiv.org/html/2512.03267v1#bib.bib57)], where they are called weighted VaR.

A different class of risk measures is based on the idea of applying a convex function ϕ\phi (more precisely, a Young function) to VaR. Inspired by the theory of Orlicz spaces, Haezendonck and Goovaerts [[29](https://arxiv.org/html/2512.03267v1#bib.bib29)] defined a corresponding Orlicz premium for positive risks XX, see Definition [4.2](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem2 "Definition 4.2. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"); it may be defined equivalently as

|  |  |  |
| --- | --- | --- |
|  | πϕ,α​(X)=inf{a>0:∫01ϕ​(FX−1​(1−u)a)​du≤1−α},\pi\_{\phi,\alpha}(X)=\inf\Big\{a>0:\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}u\leq 1-\alpha\Big\}, |  |

where α<1\alpha<1. The extension to real-valued risks in a cash-invariant way was subsequently proposed by Goovaerts et al. [[26](https://arxiv.org/html/2512.03267v1#bib.bib26)] as ρϕ,α​(X)=infx∈ℝ(πϕ,α​((X−x)+)+x)\rho\_{\phi,\alpha}(X)=\inf\_{x\in\mathbb{R}}(\pi\_{\phi,\alpha}((X-x)^{+})+x). These so-called Haezendonck-Goovaerts risk measures (see [[27](https://arxiv.org/html/2512.03267v1#bib.bib27), p. 13]) have been studied intensively, see for example [[2](https://arxiv.org/html/2512.03267v1#bib.bib2)], [[3](https://arxiv.org/html/2512.03267v1#bib.bib3)], [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)], [[6](https://arxiv.org/html/2512.03267v1#bib.bib6)], [[7](https://arxiv.org/html/2512.03267v1#bib.bib7)], [[8](https://arxiv.org/html/2512.03267v1#bib.bib8)], [[23](https://arxiv.org/html/2512.03267v1#bib.bib23)], [[26](https://arxiv.org/html/2512.03267v1#bib.bib26)], [[27](https://arxiv.org/html/2512.03267v1#bib.bib27)], [[38](https://arxiv.org/html/2512.03267v1#bib.bib38)], and [[53](https://arxiv.org/html/2512.03267v1#bib.bib53)].

It therefore seems natural and of interest to combine these two ways of weighting VaR. This was suggested, en passant, by Goovaerts, Linders, Van Weert, and Tank [[27](https://arxiv.org/html/2512.03267v1#bib.bib27), Definition 4.2]. Analysing their suggestion leads us to the premium

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(X)=inf{a>0:∫01ϕ​(FX−1​(1−u)a)​dg​(u)≤1−α},\displaystyle\pi\_{g,\phi,\alpha}(X)=\inf\Big\{a>0:\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)\leq 1-\alpha\Big\}, |  |

which we call an Orlicz-Lorentz premium in view of its link with the Orlicz-Lorentz spaces, and to the distortion Haezendonck-Goovaerts risk measure

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​(X)=infx∈ℝ(πg,ϕ,α​((X−x)+)+x).\rho\_{g,\phi,\alpha}(X)=\inf\_{x\in\mathbb{R}}(\pi\_{g,\phi,\alpha}((X-x)^{+})+x). |  |

The main aim of our paper is to determine natural sets where these risk measures are defined, and to study their risk theoretic properties. Our main result is that the distortion Haezendonck-Goovaerts risk measures are coherent whenever gg is concave, thereby generalizing the known properties for distortion and Haezendonck-Goovaerts risk measures.

The large majority of our results were first presented in 2022 in the PhD thesis of the first author [[28](https://arxiv.org/html/2512.03267v1#bib.bib28)]. The main additional contributions are the investigation of Fatou properties, the realization that the Orlicz-Lorentz premia are closely related to the Orlicz-Lorentz spaces from functional analysis (hence their name), and the observation that, in many cases, Haezendonck-Goovaerts risk measures reduce to the expectation when α=0\alpha=0. Also, we offer a different proof of coherence: while in [[28](https://arxiv.org/html/2512.03267v1#bib.bib28)], the proof was more direct, we proceed here via the notions of stop-loss order and comonotonicity, as suggested in [[18](https://arxiv.org/html/2512.03267v1#bib.bib18)] and [[56](https://arxiv.org/html/2512.03267v1#bib.bib56)].

The paper is organized as follows. In Section [2](https://arxiv.org/html/2512.03267v1#S2 "2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we recall the main risk theoretic properties that are discussed in this paper.
Sections [3](https://arxiv.org/html/2512.03267v1#S3 "3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [4](https://arxiv.org/html/2512.03267v1#S4 "4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") present the distortion risk measures and the Haezendonck-Goovaerts risk measures, respectively; they prepare the ground for the following section, but they also add some new aspects to the known theory, like Example [3.9](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem9 "Example 3.9. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), Proposition [4.13](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem13 "Proposition 4.13. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), and the unexpected Corollary [4.20](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem20 "Corollary 4.20. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). Section [5](https://arxiv.org/html/2512.03267v1#S5 "5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") constitutes the main part of this paper, a thorough investigation of the distortion Haezendonck-Goovaerts risk measures.

We remark that recently, and independently, Wu and Xu [[58](https://arxiv.org/html/2512.03267v1#bib.bib58)] have also proposed versions of the Orlicz-Lorentz premia and the distortion Haezendonck-Goovaerts risk measures. We discuss the relationship with our work in the final Section [6](https://arxiv.org/html/2512.03267v1#S6 "6. Concluding remarks ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). We also suggest there some open problems.

Let us finally mention that properties like “positive” and “decreasing” are meant in the large sense. Also, random variables that coincide almost surely are identified. Thus, for example, “X≥YX\geq Y” means that “X≥YX\geq Y a.s.” We emphasize that ess​sup​X\mathrm{ess\,sup\,}X is defined for any random variable, having the value ∞\infty if XX is not bounded above. The following well-known properties of the quantile function FX−1​(u)=inf{x∈ℝ:FX​(x)≥u}F\_{X}^{-1}(u)=\inf\{x\in\mathbb{R}:F\_{X}(x)\geq u\} will be used repeatedly. If hh is a continuous increasing function on ℝ\mathbb{R} then Fh​(X)−1=h​(FX−1)F^{-1}\_{h(X)}=h(F^{-1}\_{X}); if hh is a positive measurable function on ℝ\mathbb{R} then ∫Ωh​(X)​dP=∫01h​(FX−1​(u))​du\int\_{\Omega}h(X)\mathrm{d}P=\int\_{0}^{1}h(F\_{X}^{-1}(u))\mathrm{d}u; and u≤FX​(x)u\leq F\_{X}(x) holds if and only if FX−1​(u)≤xF\_{X}^{-1}(u)\leq x.

## 2. Risk measures

Throughout this paper, risk variables XX are real random variables on a given probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P). We follow the usual convention from insurance mathematics: positive values of XX correspond to losses, negative ones correspond to gains.

###### Definition 2.1.

Let 𝒳\mathcal{X} be a set of risks that contains the constants.

(a) A risk measure is a functional ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R}.

(b) A risk measure ρ\rho is said to be coherent if it satisfies the following conditions:

1. (i)

   If X,Y∈𝒳X,Y\in\mathcal{X} with X≤YX\leq Y then ρ​(X)≤ρ​(Y)\rho(X)\leq\rho(Y). (Monotonicity)
2. (ii)

   If X∈𝒳X\in\mathcal{X} and b∈ℝb\in\mathbb{R} with X+b∈𝒳X+b\in\mathcal{X} then ρ​(X+b)=ρ​(X)+b\rho(X+b)=\rho(X)+b. (Cash-invariance)
3. (iii)

   If X∈𝒳X\in\mathcal{X} and λ≥0\lambda\geq 0 with λ​X∈𝒳\lambda X\in\mathcal{X} then ρ​(λ​X)=λ​ρ​(X)\rho(\lambda X)=\lambda\rho(X). (Positive homogeneity)
4. (iv)

   If X,Y∈𝒳X,Y\in\mathcal{X} with X+Y∈𝒳X+Y\in\mathcal{X} then ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y). (Subadditivity)

The notion of coherence was introduced in [[4](https://arxiv.org/html/2512.03267v1#bib.bib4)]. In the insurance literature, ρ\rho is also sometimes called a premium principle, see [[23](https://arxiv.org/html/2512.03267v1#bib.bib23)] or [[56](https://arxiv.org/html/2512.03267v1#bib.bib56)]; see also Remark [4.3](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem3 "Remark 4.3. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below. In the finance literature, the differing sign convention for risks, where positive values correspond to gains, leads to different notions of monotonicity and cash-invariance, see [[4](https://arxiv.org/html/2512.03267v1#bib.bib4)], [[21](https://arxiv.org/html/2512.03267v1#bib.bib21)] or [[49](https://arxiv.org/html/2512.03267v1#bib.bib49)].

###### Remark 2.2.

If 𝒳\mathcal{X} is a convex cone, then, for any X,Y∈𝒳X,Y\in\mathcal{X}, b∈ℝb\in\mathbb{R}, and λ≥0\lambda\geq 0, X+Y,X+bX+Y,X+b, and λ​X∈𝒳\lambda X\in\mathcal{X}, so that the extra assumptions in (ii)–(iv) are not needed. But we will see in Example [3.9](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem9 "Example 3.9. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below that even for concave distortion functions the natural domain of definition of the corresponding distortion risk measure need not be a convex cone.

Another desirable property of risk measures is that they are law-invariant: if a risk XX has the same distribution as a risk Y∈𝒳Y\in\mathcal{X} then X∈𝒳X\in\mathcal{X} and ρ​(X)=ρ​(Y)\rho(X)=\rho(Y). It will be immediately clear from their definitions that all the particular risk measures studied in this paper are law-invariant.

We next consider some continuity properties.

###### Definition 2.3.

Let ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R} be a risk measure.

(a) ρ\rho is said to have the Fatou property if, for any sequence (Xn)n(X\_{n})\_{n} in 𝒳\mathcal{X} and X,Y1,Y2∈𝒳X,Y\_{1},Y\_{2}\in\mathcal{X},

|  |  |  |
| --- | --- | --- |
|  | Xn→X&∀n,Y1≤Xn≤Y2⟹ρ​(X)≤lim infn→∞ρ​(Xn).\displaystyle X\_{n}\to X\ \&\ \forall n,Y\_{1}\leq X\_{n}\leq Y\_{2}\Longrightarrow\rho(X)\leq\liminf\_{n\to\infty}\rho(X\_{n}). |  |

(b) ρ\rho is said to have the reverse Fatou property if, for any sequence (Xn)n(X\_{n})\_{n} in 𝒳\mathcal{X} and X,Y1,Y2∈𝒳X,Y\_{1},Y\_{2}\in\mathcal{X},

|  |  |  |
| --- | --- | --- |
|  | Xn→X&∀n,Y1≤Xn≤Y2⟹ρ​(X)≥lim supn→∞ρ​(Xn).\displaystyle X\_{n}\to X\ \&\ \forall n,Y\_{1}\leq X\_{n}\leq Y\_{2}\Longrightarrow\rho(X)\geq\limsup\_{n\to\infty}\rho(X\_{n}). |  |

(c) ρ\rho is said to have the Lebesgue property if, for any sequence (Xn)n(X\_{n})\_{n} in 𝒳\mathcal{X} and X,Y1,Y2∈𝒳X,Y\_{1},Y\_{2}\in\mathcal{X},

|  |  |  |
| --- | --- | --- |
|  | Xn→X&∀n,Y1≤Xn≤Y2⟹ρ​(X)=limn→∞ρ​(Xn).\displaystyle X\_{n}\to X\ \&\ \forall n,Y\_{1}\leq X\_{n}\leq Y\_{2}\Longrightarrow\rho(X)=\lim\_{n\to\infty}\rho(X\_{n}). |  |

Thus, ρ\rho has the Lebesgue property if and only if it has both the Fatou and the reverse Fatou property.

###### Remark 2.4.

Some discussion of these definitions is in order.

(a) By a well known property, one can replace almost sure convergence by convergence in probability.

(b) In the literature, one usually demands that |Xn|≤Y|X\_{n}|\leq Y for some Y∈𝒳Y\in\mathcal{X}. But this happens often in the context where −Y∈𝒳-Y\in\mathcal{X} whenever Y∈𝒳Y\in\mathcal{X}. In our context we found it useful to demand explicitly a lower bound from 𝒳\mathcal{X}; see Example [3.15](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem15 "Example 3.15. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

(c) Suppose that 𝒳\mathcal{X} has the property that, for any risk XX, if there are Y1,Y2∈𝒳Y\_{1},Y\_{2}\in\mathcal{X} with Y1≤X≤Y2Y\_{1}\leq X\leq Y\_{2} then X∈𝒳X\in\mathcal{X}.

If ρ\rho is monotonic, then ρ\rho has the Fatou property if and only if, for any sequence (Xn)n(X\_{n})\_{n} in 𝒳\mathcal{X} and any X∈𝒳X\in\mathcal{X},

|  |  |  |
| --- | --- | --- |
|  | Xn↗X⟹ρ​(Xn)→ρ​(X);X\_{n}\nearrow X\Longrightarrow\rho(X\_{n})\to\rho(X); |  |

and ρ\rho has the reverse Fatou property if and only if, for any sequence (Xn)n(X\_{n})\_{n} in 𝒳\mathcal{X} and any X∈𝒳X\in\mathcal{X},

|  |  |  |
| --- | --- | --- |
|  | Xn↘X⟹ρ​(Xn)→ρ​(X).X\_{n}\searrow X\Longrightarrow\rho(X\_{n})\to\rho(X). |  |

This follows by passing to infk≥nXk\inf\_{k\geq n}X\_{k} and supk≥nXk\sup\_{k\geq n}X\_{k}, respectively.

If ρ\rho is anti-monotonic, that is, if X,Y∈𝒳X,Y\in\mathcal{X} with X≤YX\leq Y implies that ρ​(X)≥ρ​(Y)\rho(X)\geq\rho(Y), then, obviously, the arrows ↗\nearrow and ↘\searrow need to be interchanged; see also [[21](https://arxiv.org/html/2512.03267v1#bib.bib21), Section 4.2].

(d) The reverse Fatou property does not seem to have been given a name in the literature so far.

(e) By a remarkable result of Jouini, Schachermayer, and Touzi [[33](https://arxiv.org/html/2512.03267v1#bib.bib33)], see also [[52](https://arxiv.org/html/2512.03267v1#bib.bib52)] and [[37](https://arxiv.org/html/2512.03267v1#bib.bib37)], every law-invariant coherent risk measure on the space L∞L^{\infty} over an atom-less probability space has the Fatou property. For an extension to Orlicz spaces, see [[11](https://arxiv.org/html/2512.03267v1#bib.bib11), Corollary 2.5].

## 3. Distortion risk measures

###### Definition 3.1.

A distortion function is a function g:[0,1]→[0,1]g:[0,1]\to[0,1] that is increasing and right-continuous with limu↗1g​(u)=g​(1)=1\lim\_{u\nearrow 1}g(u)=g(1)=1.

In the literature, the requirements on a distortion function vary considerably. Often, g​(0)=0g(0)=0 is also required; on this, see Example [3.6](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem6 "Example 3.6. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below. Our choice is motivated by the well-known one-to-one correspondence between increasing and right-continuous functions g:[0,1]→[0,1]g:[0,1]\to[0,1] with g​(1)=1g(1)=1 and Borel probability measures on [0,1][0,1], which is given by μg​([0,u])=g​(u)\mu\_{g}([0,u])=g(u), u∈[0,1]u\in[0,1]. The Lebesgue-Stieltjes integral ∫01f​dg\int\_{0}^{1}f\mathrm{d}g is then understood in the Lebesgue sense with respect to μg\mu\_{g}. Note that we write ∫01f​dg\int\_{0}^{1}f\mathrm{d}g instead of the more correct form ∫[0,1]f​dg\int\_{[0,1]}f\mathrm{d}g, while ∫(0,1]f​dg\int\_{(0,1]}f\mathrm{d}g has possibly a different value. We also set g​(0−)=0g(0-)=0.

The distortion risk measures will be defined on the following space.

###### Definition 3.2.

Let gg be a distortion function. Then Lg=Lg​(Ω)L\_{g}=L\_{g}(\Omega) is the space of all risks X:Ω→ℝX:\Omega\to\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ∫01|FX−1​(1−u)|​dg​(u)<∞.\int\_{0}^{1}|F\_{X}^{-1}(1-u)|\mathrm{d}g(u)<\infty. |  |

###### Remark 3.3.

In [[41](https://arxiv.org/html/2512.03267v1#bib.bib41)], Pichler seems to suggest that natural domains of risk measures have the property that if XX is a risk in the domain then so is |X||X|, see [[41](https://arxiv.org/html/2512.03267v1#bib.bib41), Proposition 5]. For example, if gg is given by g​(u)=∫0uw​(v)​dvg(u)=\int\_{0}^{u}w(v)\mathrm{d}v, u∈[0,1]u\in[0,1], then
Pichler takes as the natural domain of the distortion risk measure ρg\rho\_{g} the set {X:∫01F|X|−1​(1−u)​w​(u)​du<∞}\{X:\int\_{0}^{1}F\_{|X|}^{-1}(1-u)w(u)\mathrm{d}u<\infty\}, see [[41](https://arxiv.org/html/2512.03267v1#bib.bib41), Definition 8].

The problem with this approach is that, by considering |X||X|, gains (corresponding to negative values) and losses (corresponding to positive values) are treated on the same footing. We therefore prefer to consider |FX−1||F\_{X}^{-1}| instead of F|X|−1F\_{|X|}^{-1} in the above definition (and in Definition [5.1](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem1 "Definition 5.1. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below).

We will continue the discussion in Remark [3.18](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem18 "Remark 3.18. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

Since, for any risk XX, FX−1​(0)=−∞F\_{X}^{-1}(0)=-\infty, LgL\_{g} would be empty if μg​({1})=g​(1)−g​(1−)>0\mu\_{g}(\{1\})=g(1)-g(1-)>0. This is the reason why we require g​(1−)=g​(1)g(1-)=g(1) for our distortion functions. On the other hand, since g​(1−)=g​(1)g(1-)=g(1), every bounded risk belongs to LgL\_{g}, that is,

|  |  |  |
| --- | --- | --- |
|  | L∞⊂Lg.L^{\infty}\subset L\_{g}. |  |

In the same vein, if g​(0)>0g(0)>0 then a risk XX can only belong to LgL\_{g} if FX−1​(1)<∞F\_{X}^{-1}(1)<\infty, which means that XX is bounded above.

###### Definition 3.4.

Let gg be a distortion function. The distortion risk measure ρg:Lg→ℝ\rho\_{g}:L\_{g}\to\mathbb{R} is given by

|  |  |  |
| --- | --- | --- |
|  | ρg​(X)=∫01FX−1​(1−u)​dg​(u).\rho\_{g}(X)=\int\_{0}^{1}F\_{X}^{-1}(1-u)\mathrm{d}g(u). |  |

We have a useful alternative representation; see also, for example, [[14](https://arxiv.org/html/2512.03267v1#bib.bib14), Section 2.6.1.2] and [[18](https://arxiv.org/html/2512.03267v1#bib.bib18), Section 5.1], where, however, gg is the left-continuous version of ours.

###### Proposition 3.5.

Let X∈LgX\in L\_{g}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ\displaystyle\rho | (X)g=−∫−∞0(1−g(F¯X(x)−))dx+∫0∞g(F¯X(x)−)dx,{}\_{g}(X)=-\int\_{-\infty}^{0}(1-g(\overline{F}\_{X}(x)-))\mathrm{d}x+\int\_{0}^{\infty}g(\overline{F}\_{X}(x)-)\mathrm{d}x, |  |

where F¯X​(x)=1−FX​(x)\overline{F}\_{X}(x)=1-F\_{X}(x) and g​(u−)=limv↗ug​(v)g(u-)=\lim\_{v\nearrow u}g(v) is the left-hand limit, with g​(0−)=0g(0-)=0.

###### Proof.

Note that, by using Fubini and properties of FX−1F\_{X}^{-1},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg​(X)\displaystyle\rho\_{g}(X) | =−∫FX−1​(1−u)≤0∫FX−1​(1−u)≤x≤0dx​dg​(u)+∫FX−1​(1−u)>0∫0≤x<FX−1​(1−u)dx​dg​(u)\displaystyle=-\int\_{F\_{X}^{-1}(1-u)\leq 0}\int\_{F\_{X}^{-1}(1-u)\leq x\leq 0}\mathrm{d}x\mathrm{d}g(u)+\int\_{F\_{X}^{-1}(1-u)>0}\int\_{0\leq x<F\_{X}^{-1}(1-u)}\mathrm{d}x\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫u≥F¯X​(0)∫F¯X​(x)≤u,x≤0dx​dg​(u)+∫u<F¯X​(0)∫F¯X​(x)>u,x≥0dx​dg​(u)\displaystyle=-\int\_{u\geq\overline{F}\_{X}(0)}\int\_{\overline{F}\_{X}(x)\leq u,x\leq 0}\mathrm{d}x\mathrm{d}g(u)+\int\_{u<\overline{F}\_{X}(0)}\int\_{\overline{F}\_{X}(x)>u,x\geq 0}\mathrm{d}x\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫x≤0∫u≥F¯X​(x)dg​(u)​dx+∫x≥0∫u<F¯X​(x)dg​(u)​dx,\displaystyle=-\int\_{x\leq 0}\int\_{u\geq\overline{F}\_{X}(x)}\mathrm{d}g(u)\mathrm{d}x+\int\_{x\geq 0}\int\_{u<\overline{F}\_{X}(x)}\mathrm{d}g(u)\mathrm{d}x, |  |

which yields the claimed identity.
∎

In particular, for positive risks XX, we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg​(X)=∫0∞g​(F¯X​(x)−)​dx.\rho\_{g}(X)=\int\_{0}^{\infty}g(\overline{F}\_{X}(x)-)\mathrm{d}x. |  | (3.1) |

###### Example 3.6.

We have three classical examples of distortion risk measures. If g​(u)=ug(u)=u then ρg​(X)=E​(X)\rho\_{g}(X)=E(X) on the set Lg=L1L\_{g}=L^{1} of integrable risks. If g​(u)=𝟙[1−α,1]​(u)g(u)=\mathds{1}\_{[1-\alpha,1]}(u), 0<α<10<\alpha<1, then ρg​(X)=VaRα​(X)=FX−1​(α)\rho\_{g}(X)=\mathrm{VaR}\_{\alpha}(X)=F\_{X}^{-1}(\alpha) (Value at Risk) on the set of all risks; in the extreme case of α=0\alpha=0 we have with g​(u)≡1g(u)\equiv 1 that ρg​(X)=VaR1​(X)=ess​sup​X\rho\_{g}(X)=\mathrm{VaR}\_{1}(X)=\mathrm{ess\,sup\,}X on the set of all risks for which X+∈L∞X^{+}\in L^{\infty}; it therefore makes sense not to demand that g​(0)=0g(0)=0. Finally, if g​(u)=min⁡(u1−α,1)g(u)=\min\big(\frac{u}{1-\alpha},1\big), 0<α<10<\alpha<1, then ρg​(X)=TVaRα​(X)=11−α​∫α1FX−1​(u)​du\rho\_{g}(X)=\mathrm{TVaR}\_{\alpha}(X)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}F\_{X}^{-1}(u)\mathrm{d}u (Tail Value at Risk) on the set of all risks for which X+∈L1X^{+}\in L^{1}.

We recall a well-known formula for TVaR, which is due to Rockafellar and Uryasev [[47](https://arxiv.org/html/2512.03267v1#bib.bib47)], [[48](https://arxiv.org/html/2512.03267v1#bib.bib48)], and Acerbi and Tasche [[1](https://arxiv.org/html/2512.03267v1#bib.bib1)]; for short proofs, see [[18](https://arxiv.org/html/2512.03267v1#bib.bib18), p. 582] or [[21](https://arxiv.org/html/2512.03267v1#bib.bib21), Proposition 4.51]. It can be used, for example, to show that TVaR is subadditive, see [[20](https://arxiv.org/html/2512.03267v1#bib.bib20), Section 3.2]. This type of formula will guide us throughout the paper, see Definitions [4.10](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem10 "Definition 4.10. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.22](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem22 "Definition 5.22. ‣ 5.6. Distortion Haezendonck-Goovaerts risk measures ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Proposition 3.7.

Let 0<α<10<\alpha<1. If X+∈L1X^{+}\in L^{1}, then

|  |  |  |
| --- | --- | --- |
|  | TVaRα​(X)=minx∈ℝ⁡(11−α​E​((X−x)+)+x),\emph{TVaR}\_{\alpha}(X)=\min\_{x\in\mathbb{R}}\Big(\frac{1}{1-\alpha}E\big((X-x)^{+}\big)+x\Big), |  |

where the minimum is attained at x=FX−1​(α)x=F\_{X}^{-1}(\alpha).

The case of the Tail Value at Risk shows that X∈LgX\in L\_{g} does not necessarily imply that |X|∈Lg|X|\in L\_{g}. The following, however, is a direct consequence of the definition and the monotonicity of VaR.

###### Proposition 3.8.

If Y1,Y2∈LgY\_{1},Y\_{2}\in L\_{g} and Y1≤X≤Y2Y\_{1}\leq X\leq Y\_{2} then X∈LgX\in L\_{g}.

The next example shows a rather unexpected problem with the domain of distortion risk measures, which does not seem to have been noticed before.

###### Example 3.9.

There exists a concave distortion function gg for which LgL\_{g} is not a convex cone. Indeed, consider g:[0,1]→[0,1]g:[0,1]\to[0,1] given by g​(u)=43​(1−e−3)​u​𝟙[0,34)​(u)+(1−e−u1−u)​𝟙[34,1)​(u)g(u)=\frac{4}{3}(1-\mathrm{e}^{-3})u\mathds{1}\_{[0,\frac{3}{4})}(u)+(1-\mathrm{e}^{-\frac{u}{1-u}})\mathds{1}\_{[\frac{3}{4},1)}(u) with g​(1)=1g(1)=1.

On Ω=[−1,1]\Omega=[-1,1] with the normalized Lebesgue measure, we consider X​(ω)=−e1|ω|​𝟙[−1,0)​(ω)X(\omega)=-\mathrm{e}^{\frac{1}{|\omega|}}\mathds{1}\_{[-1,0)}(\omega) and Y​(ω)=−e1|ω|​𝟙(0,1]​(ω)Y(\omega)=-\mathrm{e}^{\frac{1}{|\omega|}}\mathds{1}\_{(0,1]}(\omega). We calculate that FX​(x)=FY​(x)=12​ln⁡(−x)​𝟙(−∞,−e)​(x)+12​𝟙[−e,0)​(x)+𝟙[0,∞)​(x)F\_{X}(x)=F\_{Y}(x)=\frac{1}{2\ln(-x)}\mathds{1}\_{(-\infty,-\mathrm{e})}(x)+\frac{1}{2}\mathds{1}\_{[-\mathrm{e},0)}(x)+\mathds{1}\_{[0,\infty)}(x) for x∈ℝx\in\mathbb{R} and FX−1​(u)=−e12​u​𝟙(0,12]​(u)F\_{X}^{-1}(u)=-\mathrm{e}^{\frac{1}{2u}}\mathds{1}\_{(0,\frac{1}{2}]}(u) for u∈(0,1]u\in(0,1]. Then ∫01|FX−1​(1−u)|​dg​(u)=∫121e12​(1−u)​g′​(u)​du=C+∫341e12​(1−u)​1(1−u)2​e−11−u​e​du<∞\int\_{0}^{1}|F\_{X}^{-1}(1-u)|\mathrm{d}g(u)=\int\_{\frac{1}{2}}^{1}\mathrm{e}^{\frac{1}{2(1-u)}}g^{\prime}(u)\mathrm{d}u=C+\int\_{\frac{3}{4}}^{1}\mathrm{e}^{\frac{1}{2(1-u)}}\frac{1}{(1-u)^{2}}\mathrm{e}^{-\frac{1}{1-u}}\mathrm{e}\,\mathrm{d}u<\infty, where CC is some constant, so that X∈LgX\in L\_{g} and hence also Y∈LgY\in L\_{g}. On the other hand, FX+Y​(x)=1ln⁡(−x)​𝟙(−∞,−e)​(x)+𝟙[−e,∞)​(x)F\_{X+Y}(x)=\frac{1}{\ln(-x)}\mathds{1}\_{(-\infty,-\mathrm{e})}(x)+\mathds{1}\_{[-\mathrm{e},\infty)}(x) and FX+Y−1​(u)=−e1uF\_{X+Y}^{-1}(u)=-\mathrm{e}^{\frac{1}{u}}, so that ∫01|FX+Y−1​(1−u)|​dg​(u)≥∫341e11−u​1(1−u)2​e−11−u​e​du=∞\int\_{0}^{1}|F\_{X+Y}^{-1}(1-u)|\mathrm{d}g(u)\geq\int\_{\frac{3}{4}}^{1}\mathrm{e}^{\frac{1}{1-u}}\frac{1}{(1-u)^{2}}\mathrm{e}^{-\frac{1}{1-u}}\mathrm{e}\,\mathrm{d}u=\infty, which shows that X+Y∉LgX+Y\notin L\_{g}. Thus LgL\_{g} is not a convex cone.

In Subsection [5.7](https://arxiv.org/html/2512.03267v1#S5.SS7 "5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we will find conditions on gg under which LgL\_{g} is a convex cone.

The following is an immediate consequence of the corresponding properties for the Value at Risk.

###### Proposition 3.10.

The distortion risk measure ρg\rho\_{g} is monotonic, cash-invariant and positively homogeneous on LgL\_{g}.

It is well known that while Value at Risk is not subadditive, it is (even) additive for comonotonic risks, see [[18](https://arxiv.org/html/2512.03267v1#bib.bib18), Theorem 4.2.1]. There are various ways to define comonotonicity, see [[15](https://arxiv.org/html/2512.03267v1#bib.bib15), Definition 4, Theorem 2]. Maybe the one that expresses best the idea behind this notion is to say that two risks XX and YY are comonotonic if there is a random variable ZZ with values in an interval I⊂ℝI\subset\mathbb{R} and two increasing functions f1,f2:I→ℝf\_{1},f\_{2}:I\to\mathbb{R} such that (X,Y)(X,Y) and (f1​(Z),f2​(Z))(f\_{1}(Z),f\_{2}(Z)) have the same distribution.

Now, the definition of the distortion risk measures and the mentioned property of VaR\mathrm{VaR} immediately imply the following; see also [[18](https://arxiv.org/html/2512.03267v1#bib.bib18), p. 593].

###### Proposition 3.11.

Let X,Y∈LgX,Y\in L\_{g} be comonotonic. Then X+Y∈LgX+Y\in L\_{g} and

|  |  |  |
| --- | --- | --- |
|  | ρg​(X+Y)=ρg​(X)+ρg​(Y).\rho\_{g}(X+Y)=\rho\_{g}(X)+\rho\_{g}(Y). |  |

The next result is well known if g​(0)=0g(0)=0, see [[18](https://arxiv.org/html/2512.03267v1#bib.bib18)], [[55](https://arxiv.org/html/2512.03267v1#bib.bib55)], [[56](https://arxiv.org/html/2512.03267v1#bib.bib56)]. In general, gg is a convex combination of the constant distortion function g1=1g\_{1}=1 and a distortion function g2g\_{2} with g2​(0)=0g\_{2}(0)=0. Thus ρg\rho\_{g} is a convex combination of ρg1=VaR1=ess​sup\rho\_{g\_{1}}=\mathrm{VaR}\_{1}=\mathrm{ess\,sup\,} and ρg2\rho\_{g\_{2}}, and both are coherent.

###### Theorem 3.12.

If gg is concave, then the distortion risk measure ρg\rho\_{g} is coherent on LgL\_{g}.

We will give a proof of the theorem for the more general distortion Haezendonck-Goovaerts risk measures in Section [5](https://arxiv.org/html/2512.03267v1#S5 "5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

We next turn to continuity properties.

###### Proposition 3.13.

The distortion risk measure ρg\rho\_{g} has the Fatou property on LgL\_{g}.

###### Proof.

By Remark [2.4](https://arxiv.org/html/2512.03267v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) and Propositions [3.8](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [3.10](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") it suffices to show that if Xn↗XX\_{n}\nearrow X and X1,X∈LgX\_{1},X\in L\_{g} then ρg​(Xn)→ρg​(X)\rho\_{g}(X\_{n})\to\rho\_{g}(X). Now, the hypothesis implies that F¯Xn​(x)↗F¯X​(x)\overline{F}\_{X\_{n}}(x)\nearrow\overline{F}\_{X}(x) for all x∈ℝx\in\mathbb{R} with at most countably many exceptions. Since u↦g​(u−)u\mapsto g(u-) is left-continuous and increasing, we deduce that g​(F¯Xn​(x)−)↗g​(F¯X​(x)−)g(\overline{F}\_{X\_{n}}(x)-)\nearrow g(\overline{F}\_{X}(x)-) for these xx. Since X1≤Xn≤XX\_{1}\leq X\_{n}\leq X for all nn, Proposition [3.5](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and the dominated convergence theorem implies that ρg​(Xn)→ρg​(X)\rho\_{g}(X\_{n})\to\rho\_{g}(X).
∎

In particular, we have the following, which should be known, but we haven’t been able to find a reference.

###### Corollary 3.14.

For 0<α≤10<\alpha\leq 1, the Value at Risk *VaRα* has the Fatou property.

###### Example 3.15.

On Ω=[0,1]\Omega=[0,1] with the Lebesgue measure, we consider the risks Xn=−n​𝟙[0,1/n]X\_{n}=-n\mathds{1}\_{[0,1/n]}, n≥2n\geq 2, so that Xn→X:=0X\_{n}\to X:=0. Let gg be the distortion function g​(u)=(−1+2​u)​𝟙[1/2,1]​(u)g(u)=(-1+2u)\mathds{1}\_{[1/2,1]}(u). Then ρg​(Xn)=∫1−1/n(−n)​2​du=−2\rho\_{g}(X\_{n})=\int\_{1-1/n}(-n)2\mathrm{d}u=-2, and hence ρg​(X)>lim infn→∞ρg​(Xn)\rho\_{g}(X)>\liminf\_{n\to\infty}\rho\_{g}(X\_{n}). On the other hand, taking Y=supn≥2|Xn|Y=\sup\_{n\geq 2}|X\_{n}|, one verifies that Y∈LgY\in L\_{g}; note however that −Y∉Lg-Y\notin L\_{g}. This example shows that while the Fatou property holds on LgL\_{g} in the sense of Definition [2.3](https://arxiv.org/html/2512.03267v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), it would not hold if we had only demanded that ∀n,|Xn|≤Y\forall n,|X\_{n}|\leq Y for some Y∈LgY\in L\_{g}.

We turn to the reverse Fatou property.

###### Proposition 3.16.

*(a)* If g​(0)=0g(0)=0 and gg is continuous, then ρg\rho\_{g} has the reverse Fatou property on LgL\_{g}, and hence the Lebesgue property.

*(b)* If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless, then ρg\rho\_{g} has the reverse Fatou property on LgL\_{g} if and only if g​(0)=0g(0)=0 and gg is continuous.

###### Proof.

(a) This follows exactly as in the proof of Proposition [3.13](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem13 "Proposition 3.13. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), taking account of the continuity of gg; note that g​(0−)=0g(0-)=0.

(b) Suppose that gg is not continuous or that g​(0)≠0g(0)\neq 0. Then there is some u∈[0,1)u\in\mathopen{[}0,1) such that g​(u−)<g​(u)g(u-)<g(u). Let (pn)n(p\_{n})\_{n} be a strictly decreasing sequence in [0,1][0,1] with limit uu. If PP is atomless, there exists a decreasing sequence (An)n(A\_{n})\_{n} of sets in 𝒜\mathcal{A} with P​(An)=pnP(A\_{n})=p\_{n}, n≥1n\geq 1, see [[24](https://arxiv.org/html/2512.03267v1#bib.bib24), Theorem 8.14.2]. Then A:=⋂n=1∞AnA:=\bigcap\_{n=1}^{\infty}A\_{n} satisfies P​(A)=uP(A)=u. Let Xn=𝟙AnX\_{n}=\mathds{1}\_{A\_{n}} and X=𝟙AX=\mathds{1}\_{A}, which belong to LgL\_{g} as bounded risks. Then Xn→XX\_{n}\to X on Ω\Omega and 0≤Xn≤10\leq X\_{n}\leq 1 for all nn, with 0,1∈Lg0,1\in L\_{g}. Moreover, by ([3.1](https://arxiv.org/html/2512.03267v1#S3.E1 "In 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), we find that ρg​(Xn)=g​(pn−)≥g​(u)\rho\_{g}(X\_{n})=g(p\_{n}-)\geq g(u) for all nn and ρg​(X)=g​(u−)\rho\_{g}(X)=g(u-), so that ρg​(X)<lim supn→∞ρg​(Xn)\rho\_{g}(X)<\limsup\_{n\to\infty}\rho\_{g}(X\_{n}), contradicting the reverse Fatou property.
∎

###### Remark 3.17.

Since the counter-example is taken from L∞L^{\infty}, the proposition remains true in the more restrictive setting of L∞L^{\infty}.

We finally discuss an interesting link between the domain LgL\_{g} and Lorentz spaces.

###### Remark 3.18.

In functional analysis,

|  |  |  |
| --- | --- | --- |
|  | X∗​(u)=F|X|−1​(1−u),u∈[0,1),X^{\*}(u)=F\_{|X|}^{-1}(1-u),\ u\in[0,1), |  |

with X∗​(1)=0X^{\*}(1)=0, is known as the nonincreasing rearrangement of XX, see [[9](https://arxiv.org/html/2512.03267v1#bib.bib9)], [[24](https://arxiv.org/html/2512.03267v1#bib.bib24)], [[42](https://arxiv.org/html/2512.03267v1#bib.bib42)]. If w:[0,1]→ℝw:[0,1]\to\mathbb{R} is a positive measurable function with ∫01w​(u)​du=1\int\_{0}^{1}w(u)\mathrm{d}u=1, then

|  |  |  |
| --- | --- | --- |
|  | Λ​(w)={X:‖X‖:=∫01X∗​(u)​w​(u)​du<∞}\Lambda(w)=\Big\{X:\|X\|:=\int\_{0}^{1}X^{\ast}(u)w(u)\mathrm{d}u<\infty\Big\} |  |

is called a (classical) Lorentz space, see [[9](https://arxiv.org/html/2512.03267v1#bib.bib9)], [[39](https://arxiv.org/html/2512.03267v1#bib.bib39)], [[42](https://arxiv.org/html/2512.03267v1#bib.bib42)]. Setting g​(u)=∫0uw​(v)​dvg(u)=\int\_{0}^{u}w(v)\mathrm{d}v, u∈[0,1]u\in[0,1], we obtain a continuous distortion function with g​(0)=0g(0)=0. Then Λ​(w)={X:|X|∈Lg}\Lambda(w)=\{X:|X|\in L\_{g}\} and ‖X‖=ρg​(|X|)\|X\|=\rho\_{g}(|X|) for X∈Λ​(w)X\in\Lambda(w).

For these distortion functions gg, one can even define LgL\_{g} and ρg\rho\_{g} completely in terms of notions introduced by Lorentz. Indeed, X∈LgX\in L\_{g} if and only if X+∈Λ​(w)X^{+}\in\Lambda(w) and infx∈ℝ(‖(X−x)+‖+x)>−∞\inf\_{x\in\mathbb{R}}(\|(X-x)^{+}\|+x)>-\infty; in that case, the infimum gives ρg​(X)\rho\_{g}(X). For the proof see Proposition [7.1](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem1 "Proposition 7.1. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") in the Appendix.

Now, decreasing functions ww correspond to concave distortion functions gg with g​(0)=0g(0)=0. In that case, and for Ω=[0,1]\Omega=[0,1], Lorentz [[39](https://arxiv.org/html/2512.03267v1#bib.bib39)] showed that ∥⋅∥\|\cdot\| defines a norm on Λ​(w)\Lambda(w); for general spaces Ω\Omega, see [[9](https://arxiv.org/html/2512.03267v1#bib.bib9), Theorem 2.5.1]. The fact that ∥⋅∥\|\cdot\| is a norm implies that the corresponding distortion risk measure is subadditive on the positive cone of LgL\_{g}. In addition, one can show that Λ​(w)⊂Lg\Lambda(w)\subset L\_{g}; we give the proof in the Appendix, see Proposition [7.2](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem2 "Proposition 7.2. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

The connection between distortion risk measures and Lorentz space norms was also recently noted in [[22](https://arxiv.org/html/2512.03267v1#bib.bib22), Section 4.5].

## 4. Haezendonck-Goovaerts risk measures

We recall here the definition of the Haezendonck-Goovaerts risk measures. They are defined on Orlicz spaces, which are well-known spaces from functional analysis, see [[10](https://arxiv.org/html/2512.03267v1#bib.bib10)], [[19](https://arxiv.org/html/2512.03267v1#bib.bib19), Chapter 2], [[42](https://arxiv.org/html/2512.03267v1#bib.bib42)] or [[45](https://arxiv.org/html/2512.03267v1#bib.bib45)].

###### Definition 4.1.

A Young function is a convex function ϕ:[0,∞)→[0,∞)\phi:[0,\infty)\to[0,\infty) with ϕ​(0)=0\phi(0)=0 and limt→∞ϕ​(t)=∞\lim\_{t\to\infty}\phi(t)=\infty. The corresponding Orlicz space Lϕ=Lϕ​(Ω)L^{\phi}=L^{\phi}(\Omega) is the space of all risks X:Ω→ℝX:\Omega\to\mathbb{R} for which there is some a>0a>0 such that

|  |  |  |
| --- | --- | --- |
|  | E​(ϕ​(|X|a))<∞.E\Big(\phi\Big(\frac{|X|}{a}\Big)\Big)<\infty. |  |

Young functions are also known as Orlicz functions. They are sometimes assumed to be strictly increasing (see [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)]), and they are often assumed to be normalized, that is, ϕ​(1)=1\phi(1)=1 (see [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)], [[7](https://arxiv.org/html/2512.03267v1#bib.bib7)], [[29](https://arxiv.org/html/2512.03267v1#bib.bib29)]). If ϕ​(1)>0\phi(1)>0, normalization can always be achieved by replacing ϕ\phi with ϕϕ​(1)\frac{\phi}{\phi(1)}.

We have that

|  |  |  |
| --- | --- | --- |
|  | L∞⊂Lϕ⊂L1,L^{\infty}\subset L^{\phi}\subset L^{1}, |  |

see Proposition [5.2](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below for a generalization. Moreover, LϕL^{\phi} is a vector space, see [[19](https://arxiv.org/html/2512.03267v1#bib.bib19), Theorem 2.1.11].

As a preliminary step towards the Haezendonck-Goovaerts risk measures, one considers the Orlicz premia, which are defined for positive risks. We denote by L+ϕL^{\phi}\_{+} the convex cone of positive risks in LϕL^{\phi}.

###### Definition 4.2.

Let ϕ\phi be a Young function and α<1\alpha<1. The Orlicz premium πϕ,α:L+ϕ→ℝ\pi\_{\phi,\alpha}:L^{\phi}\_{+}\to\mathbb{R} is given by

|  |  |  |
| --- | --- | --- |
|  | πϕ,α​(X)=inf{a>0:E​(ϕ​(Xa))≤1−α}.\pi\_{\phi,\alpha}(X)=\inf\Big\{a>0:E\Big(\phi\Big(\frac{X}{a}\Big)\Big)\leq 1-\alpha\Big\}. |  |

For α=0\alpha=0, the Orlicz premium coincides with the Luxemburg norm in the Orlicz space LϕL^{\phi}, see [[10](https://arxiv.org/html/2512.03267v1#bib.bib10)], [[19](https://arxiv.org/html/2512.03267v1#bib.bib19)].

###### Remark 4.3.

(a) We interpret ϕ​(X)\phi(X) as the evaluation of the risk XX by the risk taker (or by the regulator). Since the role of a risk measure (and of a premium, see below) is to be on the prudent side, the value of ϕ​(X)\phi(X) should be proportionally larger for larger values of XX, meaning that ϕ\phi is not only increasing but convex. Now let us extend ϕ\phi in an increasing and convex way to all of ℝ\mathbb{R}. Since, by our sign convention, the financial position associated to the risk XX is −X-X, it makes sense to write ϕ​(X)=−U​(−X)\phi(X)=-U(-X), where UU is an increasing concave function, that is, a (risk averse) utility function. In other words, the function ϕ\phi is, up to a sign change, a utility function. See also Remark [5.5](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem5 "Remark 5.5. ‣ 5.2. Orlicz-Lorentz premia ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b) below.

(b) We add a word on terminology. In financial mathematics, risk measures are meant to quantify the “downside risk” ([[21](https://arxiv.org/html/2512.03267v1#bib.bib21), p. 194]) or the “riskiness” of a risk ([[14](https://arxiv.org/html/2512.03267v1#bib.bib14), p. 61]). This is well captured by VaR and its variants. Thus, while the expectation E​(X)E(X) is a coherent risk measure, it is of little interest. In insurance mathematics, the insurance risk is the “amount of money paid by an insurance company to indemnify a policyholder” ([[14](https://arxiv.org/html/2512.03267v1#bib.bib14), Definition 1.4.3]). In return, the insurer receives a premium. This is well captured by the expectation E​(X)E(X), called the net premium ([[14](https://arxiv.org/html/2512.03267v1#bib.bib14), p. 61]), and its variants. The Orlicz space norm being such a variant, it seems more appropriate to call πϕ,α\pi\_{\phi,\alpha} a premium (as, for example, in [[29](https://arxiv.org/html/2512.03267v1#bib.bib29)] and [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)]) than a risk measure.

We note that, while Haezendonck and Goovaerts [[29](https://arxiv.org/html/2512.03267v1#bib.bib29)] only consider α=0\alpha=0, later work requires that α∈[0,1)\alpha\in[0,1), see [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)] and [[7](https://arxiv.org/html/2512.03267v1#bib.bib7)], in each case with a normalized ϕ\phi.

We have that πϕ,α\pi\_{\phi,\alpha} takes finite values because E​(ϕ​(Xa))→0E\big(\phi\big(\frac{X}{a}\big)\big)\to 0 as a→∞a\to\infty by the dominated convergence theorem.

###### Remark 4.4.

If X≠0X\neq 0 then the infimum in the definition of πϕ,α​(X)\pi\_{\phi,\alpha}(X) is attained. If, moreover, X∈L+∞X\in L^{\infty}\_{+}, or else X∈L+ϕX\in L^{\phi}\_{+} and ϕ\phi satisfies the Δ2\Delta^{2}-condition, see ([4.1](https://arxiv.org/html/2512.03267v1#S4.E1 "In 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) below, then there is a unique value a>0a>0 such that
E​(ϕ​(Xa))=1−αE\big(\phi\big(\frac{X}{a}\big)\big)=1-\alpha; and a=πϕ,α​(X)a=\pi\_{\phi,\alpha}(X). These facts are given in [[29](https://arxiv.org/html/2512.03267v1#bib.bib29), Theorem 2] and [[7](https://arxiv.org/html/2512.03267v1#bib.bib7), p. 108]. A proof in a more general situation will be given in Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below. Note also that, by an example given in [[29](https://arxiv.org/html/2512.03267v1#bib.bib29), pp. 45-46], one cannot drop the Δ2\Delta^{2}-condition in the statement above.

We collect the main properties of the Orlicz premia. For normalized ϕ\phi and bounded risks, the first two results were obtained in [[29](https://arxiv.org/html/2512.03267v1#bib.bib29), Theorem 2] if α=0\alpha=0 and stated in [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 2] if α≥0\alpha\geq 0.

###### Proposition 4.5.

1. *(a)*

   For any X∈L+ϕX\in L\_{+}^{\phi},

   |  |  |  |
   | --- | --- | --- |
   |  | E​(X)ϕ−1​(1−α)≤πϕ,α​(X)≤ess​sup​Xϕ−1​(1−α).\frac{E(X)}{\phi^{-1}(1-\alpha)}\leq\pi\_{\phi,\alpha}(X)\leq\frac{\mathrm{ess\,sup\,}X}{\phi^{-1}(1-\alpha)}. |  |
2. *(b)*

   For any b≥0b\geq 0, πϕ,α​(b)=bϕ−1​(1−α)\pi\_{\phi,\alpha}(b)=\frac{b}{\phi^{-1}(1-\alpha)}.

###### Theorem 4.6.

The Orlicz premium πϕ,α\pi\_{\phi,\alpha} is monotonic, positively homogeneous, and subadditive on L+ϕL\_{+}^{\phi}.

The next two results were recently obtained, for 0<α<10<\alpha<1, inside the proofs of [[23](https://arxiv.org/html/2512.03267v1#bib.bib23), Theorems 3.3 and 3.4]; see also [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 2].

###### Proposition 4.7.

The Orlicz premium πϕ,α\pi\_{\phi,\alpha} has the Fatou property on L+ϕL\_{+}^{\phi}.

Recall that a Young function satisfies the Δ2\Delta\_{2}-condition if there exist s≥0s\geq 0 and K>0K>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(2​t)≤K​ϕ​(t)\phi(2t)\leq K\phi(t) |  | (4.1) |

for all t∈[s,∞)t\in[s,\infty).

###### Proposition 4.8.

*(a)* If ϕ\phi satisfies the Δ2\Delta\_{2}-condition, then πϕ,α\pi\_{\phi,\alpha} has the reverse Fatou property on L+ϕL\_{+}^{\phi}, and hence the Lebesgue property.

*(b)* If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless, then πϕ,α\pi\_{\phi,\alpha} has the reverse Fatou property on L+ϕL\_{+}^{\phi} if and only if ϕ\phi satisfies the Δ2\Delta\_{2}-condition.

On L+∞L^{\infty}\_{+}, there is no restriction, see [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 17] when α≥0\alpha\geq 0.

###### Proposition 4.9.

The Orlicz premium πϕ,α\pi\_{\phi,\alpha} has the reverse Fatou property on L+∞L^{\infty}\_{+}.

These five results will be proved, in greater generality, in Propositions [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.14](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem14 "Proposition 5.14. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.15](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem15 "Proposition 5.15. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.16](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem16 "Proposition 5.16. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and Theorem [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below.

Now, Orlicz premia in general lack the important property of cash-invariance. It suffices to consider ϕ​(t)=t2\phi(t)=t^{2} and α=0\alpha=0, so that πϕ,0​(X)=E​(X2)12\pi\_{\phi,0}(X)=E(X^{2})^{\frac{1}{2}}. It is surprising that a simple procedure allows to add cash-invariance while preserving the other three properties of coherence.

###### Definition 4.10.

Let ϕ\phi be a normalized Young function and α∈[0,1)\alpha\in[0,1). The Haezendonck-Goovaerts risk measure ρϕ,α:Lϕ→ℝ\rho\_{\phi,\alpha}:L^{\phi}\to\mathbb{R} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρϕ,α​(X)=infx∈ℝ(πϕ,α​((X−x)+)+x).\rho\_{\phi,\alpha}(X)=\inf\_{x\in\mathbb{R}}\big(\pi\_{\phi,\alpha}((X-x)^{+})+x\big). |  | (4.2) |

In this definition, we have restricted ϕ\phi and α\alpha. The minimal requirement would be that α≥1−ϕ​(1)\alpha\geq 1-\phi(1). Indeed, if α<1−ϕ​(1)\alpha<1-\phi(1), that is, ϕ−1​(1−α)>1\phi^{-1}(1-\alpha)>1, then it follows from Proposition [4.5](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b) that, for x≤1x\leq 1, πϕ,α​((1−x)+)+x=1−xϕ−1​(1−α)+x=1+x​(ϕ−1​(1−α)−1)ϕ−1​(1−α)\pi\_{\phi,\alpha}((1-x)^{+})+x=\frac{1-x}{\phi^{-1}(1-\alpha)}+x=\frac{1+x(\phi^{-1}(1-\alpha)-1)}{\phi^{-1}(1-\alpha)}, so that ρϕ,α​(1)=−∞\rho\_{\phi,\alpha}(1)=-\infty. Thus, in order to have a risk measure, we need to impose that α≥1−ϕ​(1)\alpha\geq 1-\phi(1). Since also α<1\alpha<1, ϕ​(1)\phi(1) must be nonzero. Hence we can normalize ϕ\phi, and then α∈[0,1)\alpha\in[0,1).

Now, whenever X∈LϕX\in L^{\phi}, then (X−x)+∈L+ϕ(X-x)^{+}\in L\_{+}^{\phi} for any x∈ℝx\in\mathbb{R}; also, under the assumptions on ϕ\phi and α\alpha, the infimum is in ℝ\mathbb{R}. We will show these assertions in more generality in Remark [5.24](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem24 "Remark 5.24. ‣ 5.6. Distortion Haezendonck-Goovaerts risk measures ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below. Thus, ρϕ,α\rho\_{\phi,\alpha} is a well-defined risk measure.

###### Remark 4.11.

The Haezendonck-Goovaerts risk measures were introduced by Goovaerts, Kaas, Dhaene, and Tang [[26](https://arxiv.org/html/2512.03267v1#bib.bib26)] in a slightly different form. Formula ([4.2](https://arxiv.org/html/2512.03267v1#S4.E2 "In Definition 4.10. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) is due to Bellini and Rosazza Gianin [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)], who were motivated by the representation of TVaR given in Proposition [3.7](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"); see also [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), p. 989] for a nice discussion.

###### Example 4.12.

Let us take for ϕ\phi the identity function. Then, for X∈L+ϕ=L+1X\in L^{\phi}\_{+}=L^{1}\_{+}, πϕ,α​(X)=11−α​E​(X)\pi\_{\phi,\alpha}(X)=\frac{1}{1-\alpha}E(X), α<1\alpha<1. Thus, if 0<α<10<\alpha<1 and X∈Lϕ=L1X\in L^{\phi}=L^{1}, then ρϕ,α​(X)=TVaRα​(X)\rho\_{\phi,\alpha}(X)=\text{TVaR}\_{\alpha}(X) by Proposition [3.7](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

It follows easily from Theorem [4.6](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem6 "Theorem 4.6. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that the function x↦πϕ,α​((X−x)+)+xx\mapsto\pi\_{\phi,\alpha}((X-x)^{+})+x is convex for any α<1\alpha<1, see also [[7](https://arxiv.org/html/2512.03267v1#bib.bib7), Proposition 3(a)]. Moreover, for 0<α<10<\alpha<1, it was shown in [[7](https://arxiv.org/html/2512.03267v1#bib.bib7), Proposition 3(b)] that the function has a minimum, that is, the infimum in ([4.2](https://arxiv.org/html/2512.03267v1#S4.E2 "In Definition 4.10. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) is attained. We will prove more general results in Propositions [5.28](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem28 "Proposition 5.28. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a) and [5.30](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem30 "Proposition 5.30. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a) below. We will also see in Proposition [5.30](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem30 "Proposition 5.30. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b) that the minimum is unique if ϕ\phi is strictly convex and satisfies the Δ2\Delta\_{2}-condition and if P​(X=ess​sup​X)=0P(X=\mathrm{ess\,sup\,}X)=0.

It turns out that the case of α=0\alpha=0 is exceptional. In [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Example 15], an example was given where the infimum in ([4.2](https://arxiv.org/html/2512.03267v1#S4.E2 "In Definition 4.10. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) is not attained. This led subsequent authors to only consider the case of α>0\alpha>0; see for example [[2](https://arxiv.org/html/2512.03267v1#bib.bib2), p. 79]. We will first show that the example in [[5](https://arxiv.org/html/2512.03267v1#bib.bib5)] is, in fact, a special case of a very general situation.

###### Proposition 4.13.

Let α=0\alpha=0 and X∈LϕX\in L^{\phi}.

*(a)* Then x↦πϕ,0​((X−x)+)+xx\mapsto\pi\_{\phi,0}((X-x)^{+})+x is increasing on ℝ\mathbb{R}. In particular,

|  |  |  |
| --- | --- | --- |
|  | ρϕ,0​(X)=limx→−∞(πϕ,0​((X−x)+)+x).\rho\_{\phi,0}(X)=\lim\_{x\to-\infty}\big(\pi\_{\phi,0}((X-x)^{+})+x\big). |  |

*(b)* Let ϕ\phi be strictly convex and satisfy the Δ2\Delta\_{2}-condition. If P​(X=ess​sup​X)=0P(X=\mathrm{ess\,sup\,}X)=0 then x↦πϕ,0​((X−x)+)+xx\mapsto\pi\_{\phi,0}((X-x)^{+})+x is strictly increasing on ℝ\mathbb{R}. In particular, the function does not attain its infimum.

A more general result will be proved in Proposition [5.33](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem33 "Proposition 5.33. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below.

We now collect the main properties of Haezendonck-Goovaerts risk measures; the results were obtained for certain subspaces of LϕL^{\phi} in [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 12] and [[26](https://arxiv.org/html/2512.03267v1#bib.bib26), Theorems 3.1, 3.2]. The general case will follow from Proposition [5.34](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem34 "Proposition 5.34. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and Theorem [5.46](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem46 "Theorem 5.46. ‣ 5.10. Distortion HG: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below.

###### Proposition 4.14.

Let X∈LϕX\in L^{\phi}. Then:

1. *(a)*

   ρϕ,α​(X)≤πϕ,α​(X+)\rho\_{\phi,\alpha}(X)\leq\pi\_{\phi,\alpha}(X^{+}).
2. *(b)*

   E​(X)≤ρϕ,α​(X)≤ess​sup​XE(X)\leq\rho\_{\phi,\alpha}(X)\leq\mathrm{ess\,sup\,}X.
3. *(c)*

   If α≠0\alpha\neq 0 then ρϕ,α​(X)≥VaRα​(X)\rho\_{\phi,\alpha}(X)\geq\mathrm{VaR}\_{\alpha}(X).

###### Theorem 4.15.

The Haezendonck-Goovaerts risk measure ρϕ,α\rho\_{\phi,\alpha} is coherent on LϕL^{\phi}.

As for continuity properties, the following were obtained in [[23](https://arxiv.org/html/2512.03267v1#bib.bib23), Theorems 3.3 and 3.4] and [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 17] for 0<α<10<\alpha<1. The case of α=0\alpha=0 is of little interest, see Theorem [4.19](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem19 "Theorem 4.19. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below; but see also Problem [6.3](https://arxiv.org/html/2512.03267v1#S6.Thmtheorem3 "Problem 6.3. ‣ 6.1. Problems ‣ 6. Concluding remarks ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Proposition 4.16.

If 0<α<10<\alpha<1, then ρϕ,α\rho\_{\phi,\alpha} has the Fatou property on LϕL^{\phi}.

###### Proposition 4.17.

*(a)* If ϕ\phi satisfies the Δ2\Delta\_{2}-condition then ρϕ,α\rho\_{\phi,\alpha} has the reverse Fatou property on LϕL^{\phi}.

*(b)* Let 0<α<10<\alpha<1. If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless and if ρg,ϕ,α\rho\_{g,\phi,\alpha} has the reverse Fatou property on LϕL^{\phi} then ϕ\phi satisfies the Δ2\Delta\_{2}-condition.

###### Proposition 4.18.

The Haezendonck-Goovaerts risk measure ρϕ,α\rho\_{\phi,\alpha} has the reverse Fatou property on L∞L^{\infty}.

These results will be generalized in Propositions [5.37](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem37 "Proposition 5.37. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.38](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem38 "Proposition 5.38. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.39](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem39 "Proposition 5.39. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), and [5.41](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem41 "Proposition 5.41. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below.

Finally, as we have seen, the case α=0\alpha=0 is quite exceptional. Indeed, in that case, the Haezendonck-Goovaerts risk measure is trivial on bounded risks, in some sense. This surprising fact does not seem to have been observed before.

###### Theorem 4.19.

Let α=0\alpha=0. Then, for all X∈L∞X\in L^{\infty},

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(X)≤ρϕ,0​(X)≤c+c−​E​(X+)−c−c+​E​(X−),E(X)\leq\rho\_{\phi,0}(X)\leq\frac{c\_{+}}{c\_{-}}E(X^{+})-\frac{c\_{-}}{c\_{+}}E(X^{-}), |  | (4.3) |

where c−c\_{-} is the left derivative of ϕ\phi at 11, and c+c\_{+} is the right derivative of ϕ\phi at 11. If ϕ\phi satisfies the Δ2\Delta\_{2}-condition then this holds for all X∈LϕX\in L^{\phi}.

###### Corollary 4.20.

Let α=0\alpha=0. If ϕ\phi is differentiable at 11 and satisfies the Δ2\Delta\_{2}-condition, then, for all X∈LϕX\in L^{\phi},

|  |  |  |
| --- | --- | --- |
|  | ρϕ,0​(X)=E​(X).\rho\_{\phi,0}(X)=E(X). |  |

For example, for the natural choice of ϕ​(t)=tc\phi(t)=t^{c}, c≥1c\geq 1, ρϕ,0\rho\_{\phi,0} coincides with the expectation, which is not considered a good risk measure.

We will obtain a more general result below, see Theorem [5.47](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem47 "Theorem 5.47. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") with Corollary [5.48](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem48 "Corollary 5.48. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

The following example shows that, if ϕ\phi is not differentiable at 1, ρϕ,0\rho\_{\phi,0} need not reduce to the expectation.

###### Example 4.21.

We consider the normalized Young function ϕ​(t)=t\phi(t)=t, 0≤t≤10\leq t\leq 1, and ϕ​(t)=2​t−1\phi(t)=2t-1, t>1t>1. Let XX be uniformly distributed on [0,1][0,1]. One calculates that, for x<0x<0, πϕ,0​((X−x)+)+x=2−2\pi\_{\phi,0}((X-x)^{+})+x=2-\sqrt{2}, so that, by Proposition [4.13](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem13 "Proposition 4.13. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a), ρϕ,0​(X)=2−2>E​(X)\rho\_{\phi,0}(X)=2-\sqrt{2}>E(X). Also, X≥0X\geq 0 and ρϕ,0​(X)≤2​E​(X)\rho\_{\phi,0}(X)\leq 2E(X), confirming ([4.3](https://arxiv.org/html/2512.03267v1#S4.E3 "In Theorem 4.19. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")).

Moreover, if we take XX to be uniformly distributed on [−1,0][-1,0], then, by cash-invariance, ρϕ,0​(X)=1−2>E​(X)\rho\_{\phi,0}(X)=1-\sqrt{2}>E(X). Also, X≤0X\leq 0 and ρϕ,0​(X)≤12​E​(X)\rho\_{\phi,0}(X)\leq\tfrac{1}{2}E(X), confirming again ([4.3](https://arxiv.org/html/2512.03267v1#S4.E3 "In Theorem 4.19. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")).

## 5. Distortion Haezendonck-Goovaerts risk measures

We now come to the main contribution of this work: the combination of distortion risk measures and Haezendonck-Goovaerts risk measures into a single new class of risk measures. This was suggested in 2012 by Goovaerts, Linders, Van Weert, and Tank [[27](https://arxiv.org/html/2512.03267v1#bib.bib27), Definition 4.2].

### 5.1. The domain

We begin by defining the set of risks where the distortion Haezendonck-Goovaerts risk measures will be defined.

By a property of quantile functions we have that

|  |  |  |
| --- | --- | --- |
|  | E​(ϕ​(|X|a))=∫01ϕ​(|FX−1​(1−u)|a)​du.E\Big(\phi\Big(\frac{|X|}{a}\Big)\Big)=\int\_{0}^{1}\phi\Big(\frac{|F\_{X}^{-1}(1-u)|}{a}\Big)\mathrm{d}u. |  |

Motivated by this we are led to distort LϕL^{\phi} into a new space LgϕL^{\phi}\_{g}; we refrain from giving this space a name, see Remark [5.5](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem5 "Remark 5.5. ‣ 5.2. Orlicz-Lorentz premia ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Definition 5.1.

Let gg be a distortion function and ϕ\phi a Young function. Then Lgϕ=Lgϕ​(Ω)L^{\phi}\_{g}=L^{\phi}\_{g}(\Omega) is the space of all risks X:Ω→ℝX:\Omega\to\mathbb{R} for which there is some a>0a>0 such that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(|FX−1​(1−u)|a)​dg​(u)<∞.\int\_{0}^{1}\phi\Big(\frac{|F\_{X}^{-1}(1-u)|}{a}\Big)\mathrm{d}g(u)<\infty. |  |

By the above, if gg is the identity then Lgϕ=LϕL\_{g}^{\phi}=L^{\phi}; and if ϕ\phi is the identity then Lgϕ=LgL\_{g}^{\phi}=L\_{g}.

As in our discussion in Section [3](https://arxiv.org/html/2512.03267v1#S3 "3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we see that if g​(0)>0g(0)>0 then X∈LgϕX\in L\_{g}^{\phi} implies that XX is bounded above. And the fact that g​(1−)=g​(1)g(1-)=g(1) implies that the bounded risks belong to LgϕL^{\phi}\_{g}. Indeed, we have the following.

###### Proposition 5.2.

We have that

|  |  |  |
| --- | --- | --- |
|  | L∞⊂Lgϕ⊂Lg.L^{\infty}\subset L^{\phi}\_{g}\subset L\_{g}. |  |

###### Proof.

For the second inclusion, note that since ϕ\phi is convex and necessarily increasing there are c>0c>0 and b∈ℝb\in\mathbb{R} such that ϕ​(t)≥c​t+b\phi(t)\geq ct+b for all t≥0t\geq 0. Thus

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(|FX−1​(1−u)|a)​dg​(u)≥ca​∫01|FX−1​(1−u)|​dg​(u)+b,\displaystyle\int\_{0}^{1}\phi\Big(\frac{|F\_{X}^{-1}(1-u)|}{a}\Big)\mathrm{d}g(u)\geq\frac{c}{a}\int\_{0}^{1}|F\_{X}^{-1}(1-u)|\mathrm{d}g(u)+b, |  |

so that X∈LgϕX\in L\_{g}^{\phi} implies that X∈LgX\in L\_{g}.
∎

We have seen in Example [3.9](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem9 "Example 3.9. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that LgϕL\_{g}^{\phi} is not necessarily a convex cone, even if gg is concave and ϕ\phi is the identity. In Subsection [5.7](https://arxiv.org/html/2512.03267v1#S5.SS7 "5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we will present conditions on a concave distribution function so that LgϕL\_{g}^{\phi} is a convex cone, for any Young function.

Also, by Section [3](https://arxiv.org/html/2512.03267v1#S3 "3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), X∈LgϕX\in L\_{g}^{\phi} does not necessarily imply that |X|∈Lgϕ|X|\in L\_{g}^{\phi}. Instead, the definition implies the following.

###### Proposition 5.3.

If Y1,Y2∈LgϕY\_{1},Y\_{2}\in L\_{g}^{\phi} and Y1≤X≤Y2Y\_{1}\leq X\leq Y\_{2} then X∈LgϕX\in L\_{g}^{\phi}.

### 5.2. Orlicz-Lorentz premia

We start the definition of the distortion Haezendonck-Goovaerts risk measures by distorting the Orlicz premia.

We denote by (Lgϕ)+(L\_{g}^{\phi})\_{+} the set of positive risks in LgϕL\_{g}^{\phi}. Since FX−1F\_{X}^{-1} is positive for such risks we have that X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+} if and only if X≥0X\geq 0 and

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)<∞\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)<\infty |  |

for some a>0a>0.

###### Definition 5.4.

Let gg be a distortion function, ϕ\phi a Young function, and α<1\alpha<1. The Orlicz-Lorentz premium πg,ϕ,α:(Lgϕ)+→ℝ\pi\_{g,\phi,\alpha}:(L^{\phi}\_{g})\_{+}\to\mathbb{R} is given by

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(X)=inf{a>0:∫01ϕ​(FX−1​(1−u)a)​dg​(u)≤1−α}.\displaystyle\pi\_{g,\phi,\alpha}(X)=\inf\Big\{a>0:\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)\leq 1-\alpha\Big\}. |  |

###### Remark 5.5.

(a) The premium is named after the Orlicz-Lorentz spaces of functional analysis, see [[32](https://arxiv.org/html/2512.03267v1#bib.bib32)], [[35](https://arxiv.org/html/2512.03267v1#bib.bib35)], [[36](https://arxiv.org/html/2512.03267v1#bib.bib36), Section 5]. If w:[0,1]→ℝw:[0,1]\to\mathbb{R} is a positive measurable function with ∫01w​(u)​du=1\int\_{0}^{1}w(u)\mathrm{d}u=1 and ϕ\phi is a Young function, then the Orlicz-Lorentz space Λϕ,w=Λϕ,w​(Ω)\Lambda\_{\phi,w}=\Lambda\_{\phi,w}(\Omega) is defined as the space of all measurable functions XX on Ω\Omega such that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(X∗a)​w​(u)​du<∞​ for some a>0,\int\_{0}^{1}\phi\Big(\frac{X^{\*}}{a}\Big)w(u)\mathrm{d}u<\infty\text{ for some $a>0$}, |  |

where X∗X^{\ast} is the nonincreasing rearrangement of XX, see Remark [3.18](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem18 "Remark 3.18. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). In that context one defines

|  |  |  |
| --- | --- | --- |
|  | ‖X‖=inf{a>0:∫01ϕ​(X∗​(u)a)​w​(u)​du≤1}.\|X\|=\inf\Big\{a>0:\int\_{0}^{1}\phi\Big(\frac{X^{\*}(u)}{a}\Big)w(u)\mathrm{d}u\leq 1\Big\}. |  |

We consider again the corresponding distortion function g​(u)=∫0uw​(v)​dvg(u)=\int\_{0}^{u}w(v)\mathrm{d}v, u∈[0,1]u\in[0,1]. Then Λϕ,w={X:|X|∈Lgϕ}\Lambda\_{\phi,w}=\{X:|X|\in L\_{g}^{\phi}\} and ‖X‖=πg,ϕ,0​(|X|)\|X\|=\pi\_{g,\phi,0}(|X|) for X∈Λϕ,wX\in\Lambda\_{\phi,w}. However, in general, one cannot recover LgϕL\_{g}^{\phi} from Λϕ,w\Lambda\_{\phi,w} in the same way as in Remark [3.18](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem18 "Remark 3.18. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), see Example [7.5](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem5 "Example 7.5. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") in the Appendix.

In the literature, Orlicz-Lorentz spaces are usually studied for decreasing weights ww. In that case, Λϕ,w⊂Lgϕ\Lambda\_{\phi,w}\subset L\_{g}^{\phi}, see Proposition [7.4](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem4 "Proposition 7.4. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") in the Appendix.

(b) In keeping with Remark [4.3](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem3 "Remark 4.3. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a), let us extend ϕ\phi to an increasing convex function on ℝ\mathbb{R}, define the (concave) utility function U​(t)=−ϕ​(−t)U(t)=-\phi(-t) on ℝ\mathbb{R}, and consider the financial position Y:=−XY:=-X associated with the risk X≥0X\geq 0. In decision theory, the Choquet integral

|  |  |  |  |
| --- | --- | --- | --- |
|  | (C)​∫U​(Y)​d​(h∘P)(C)\int U(Y)\mathrm{d}(h\circ P) |  | (5.1) |

is called the rank-dependent expected utility of YY with respect to a distortion function hh with h​(0)=0h(0)=0. This notion was introduced for discrete YY by Quiggin [[43](https://arxiv.org/html/2512.03267v1#bib.bib43)], [[44](https://arxiv.org/html/2512.03267v1#bib.bib44)], see [[31](https://arxiv.org/html/2512.03267v1#bib.bib31), p. 68] for the general formula, and has since been studied extensively in decision theory, see [[54](https://arxiv.org/html/2512.03267v1#bib.bib54)], and more recently also in AI research, see [[25](https://arxiv.org/html/2512.03267v1#bib.bib25)]. One can show that ([5.1](https://arxiv.org/html/2512.03267v1#S5.E1 "In Remark 5.5. ‣ 5.2. Orlicz-Lorentz premia ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) coincides with

|  |  |  |
| --- | --- | --- |
|  | −∫01ϕ​(FX−1​(1−u))​dg​(u),-\int\_{0}^{1}\phi(F\_{X}^{-1}(1-u))\mathrm{d}g(u), |  |

where g​(u)=1−h​((1−u)−)g(u)=1-h((1-u)-), see Proposition [7.6](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem6 "Proposition 7.6. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") in the Appendix. Thus there is a close link between Orlicz-Lorentz premia and rank-dependent expected utility. We are grateful to Daniël Linders for suggesting that such a link might exist.

If gg is the identity then the Orlicz-Lorentz premium πg,ϕ,α=πϕ,α\pi\_{g,\phi,\alpha}=\pi\_{\phi,\alpha} is the Orlicz premium; and if ϕ\phi is the identity then πg,ϕ,0=ρg\pi\_{g,\phi,0}=\rho\_{g} is the distortion risk measure (on the positive risks in LgL\_{g}).

We see as in Section [4](https://arxiv.org/html/2512.03267v1#S4 "4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that πg,ϕ,α\pi\_{g,\phi,\alpha} takes finite values. While possibly not useful we note that, since ϕ\phi is a continuous increasing function, we have by a property of quantile functions that

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,α​(X)=inf{a>0:ρg​(ϕ​(Xa))≤1−α},\pi\_{g,\phi,\alpha}(X)=\inf\Big\{a>0:\rho\_{g}\Big(\phi\Big(\frac{X}{a}\Big)\Big)\leq 1-\alpha\Big\}, |  | (5.2) |

that is, one replaces the expectation by ρg\rho\_{g} in Definition [4.2](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem2 "Definition 4.2. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

### 5.3. Orlicz-Lorentz: the infimum

In view of the definition of the Orlicz-Lorentz premia, two questions arise: is the infimum attained, and if so do we have equality in the defining condition at the minimum. In general, the answers are negative.

###### Example 5.6.

Clearly, for X=0X=0, the infimum is not attained. But this can also happen for nonzero risks. If, for example, X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+} with P​(X=0)=12P(X=0)=\frac{1}{2} and g​(u)=max⁡(2​u−1,0)g(u)=\max(2u-1,0), then ∫01ϕ​(FX−1​(1−u)a)​dg​(u)=0\int\_{0}^{1}\phi\big(\frac{F\_{X}^{-1}(1-u)}{a}\big)\mathrm{d}g(u)=0 for all a>0a>0, so that πg,ϕ,α​(X)=0\pi\_{g,\phi,\alpha}(X)=0, and the infimum is not attained.

An example where we do not have equality in the defining condition at the minimum was given in [[29](https://arxiv.org/html/2512.03267v1#bib.bib29), pp. 45-46], where gg is even the identity function.

In order to obtain positive answers, let XX be any positive risk, not necessarily in (Lgϕ)+(L^{\phi}\_{g})\_{+}, and consider the function ψ:(0,∞)→[0,∞]\psi:(0,\infty)\to[0,\infty] given by

|  |  |  |
| --- | --- | --- |
|  | ψ​(x)=∫01ϕ​(FX−1​(1−u)x)​dg​(u).\psi(x)=\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{x}\Big)\mathrm{d}g(u). |  |

The following lemma generalizes and extends [[29](https://arxiv.org/html/2512.03267v1#bib.bib29), Lemma 4].

###### Lemma 5.7.

Let gg be a distortion function, ϕ\phi a Young function, and X≥0X\geq 0. Then:

1. *(a)*

   Either {ψ=0}=∅\{\psi=0\}=\varnothing or {ψ=0}=(0,∞)\{\psi=0\}=(0,\infty). Moreover, {ψ=0}=∅\{\psi=0\}=\varnothing if and only if X≠0X\neq 0 and gg is not identically 0 on [0,P​(X>0))[0,P(X>0)).
2. *(b)*

   If g=0g=0 on some neighbourhood of 0, or if X∈L∞X\in L^{\infty}, then {ψ<∞}=(0,∞)\{\psi<\infty\}=(0,\infty).
3. *(c)*

   If ϕ\phi satisfies the Δ2\Delta\_{2}-condition, then either {ψ<∞}=∅\{\psi<\infty\}=\varnothing or {ψ<∞}=(0,∞)\{\psi<\infty\}=(0,\infty).
4. *(d)*

   ψ\psi is right-continuous.
5. *(e)*

   ψ\psi is continuous at every interior point of {ψ<∞}\{\psi<\infty\}.
6. *(f)*

   ψ\psi is decreasing.
7. *(g)*

   ψ\psi is strictly decreasing on {0<ψ<∞}\{0<\psi<\infty\}.
8. *(h)*

   If {ψ=0}=∅\{\psi=0\}=\varnothing then limx→0ψ​(x)=∞\lim\_{x\to 0}\psi(x)=\infty.
9. *(i)*

   If {ψ<∞}≠∅\{\psi<\infty\}\neq\varnothing then limx→∞ψ​(x)=0\lim\_{x\to\infty}\psi(x)=0.

###### Proof.

Assertion (d) follows from the monotone convergence theorem, (e) and (i) follow from the dominated convergence theorem, while (f) is obvious.

(a) If X=0X=0 then {ψ=0}=(0,∞)\{\psi=0\}=(0,\infty). Else suppose that X≠0X\neq 0, and hence q:=P​(X>0)>0q:=P(X>0)>0. Thus FX−1​(1−u)=0F\_{X}^{-1}(1-u)=0 for u∈[q,1)u\in[q,1) and FX−1​(1−u)>0F\_{X}^{-1}(1-u)>0 for u∈[0,q)u\in[0,q). If g=0g=0 on [0,q)[0,q), then μg​([0,q))=0\mu\_{g}([0,q))=0, where μg\mu\_{g} is the probability measure induced by gg. It follows that {ψ=0}=(0,∞)\{\psi=0\}=(0,\infty). If gg is not identically 0 on [0,q)[0,q), then {ψ=0}=∅\{\psi=0\}=\varnothing.

(g) We may assume that {0<ψ<∞}≠∅\{0<\psi<\infty\}\neq\varnothing. By (a), q:=P​(X>0)>0q:=P(X>0)>0 and g=0g=0 on [0,P​(X>0))[0,P(X>0)), so that μg​([0,q))>0\mu\_{g}([0,q))>0. Also, as we have seen above, FX−1​(1−u)=0F\_{X}^{-1}(1-u)=0 for u∈[q,1)u\in[q,1), so that ψ​(z)=∫[0,q)ϕ​(FX−1​(1−u)z)​dg​(u)\psi(z)=\int\_{[0,q)}\phi(\frac{F\_{X}^{-1}(1-u)}{z})\mathrm{d}g(u) for all z>0z>0, and FX−1​(1−u)>0F\_{X}^{-1}(1-u)>0 for u∈[0,q)u\in[0,q).

Now let x,y∈{0<ψ<∞}x,y\in\{0<\psi<\infty\} and x<yx<y. Since ϕ\phi is strictly increasing on {ϕ>0}\{\phi>0\}, we have for u∈[0,q)u\in[0,q) that ϕ​(FX−1​(1−u)x)>ϕ​(FX−1​(1−u)y)\phi\big(\frac{F\_{X}^{-1}(1-u)}{x}\big)>\phi\big(\frac{F\_{X}^{-1}(1-u)}{y}\big). Since ψ​(y)<∞\psi(y)<\infty, this implies that ψ​(x)>ψ​(y)\psi(x)>\psi(y).

(h) Let q=P​(X>0)q=P(X>0). As in (g), the hypothesis implies q>0q>0, μg​([0,q))>0\mu\_{g}([0,q))>0, ψ​(x)=∫[0,q)ϕ​(FX−1​(1−u)x)​dg​(u)\psi(x)=\int\_{[0,q)}\phi(\frac{F\_{X}^{-1}(1-u)}{x})\mathrm{d}g(u) for x>0x>0, and FX−1​(1−u)>0F\_{X}^{-1}(1-u)>0 for u∈[0,q)u\in[0,q). Then the claim follows from the monotone convergence theorem.

(b) Suppose that g=0g=0 on [0,u0)[0,u\_{0}) for some u0∈(0,1)u\_{0}\in(0,1). Then ψ​(x)=∫[u0,1]ϕ​(FX−1​(1−u)x)​dg​(u)<∞\psi(x)=\int\_{[u\_{0},1]}\phi(\frac{F\_{X}^{-1}(1-u)}{x})\mathrm{d}g(u)<\infty for all x>0x>0. If X∈L∞X\in L^{\infty}, then FX−1F\_{X}^{-1} is bounded on (0,1](0,1] and therefore {ψ<∞}=(0,∞)\{\psi<\infty\}=(0,\infty).

(c) Suppose that there is some a>0a>0 such that ψ​(a)<∞\psi(a)<\infty. Then it follows from the Δ2\Delta\_{2}-condition that, for some s≥0s\geq 0 and K>0K>0, ϕ​(ya/2n)≤Kn​ϕ​(ya)\phi(\frac{y}{a/2^{n}})\leq K^{n}\phi(\frac{y}{a}) for all y≥a​sy\geq as and hence ψ​(a2n)<∞\psi(\frac{a}{2^{n}})<\infty, for all n≥1n\geq 1. Thus, (f) implies that {ψ<∞}=(0,∞)\{\psi<\infty\}=(0,\infty).
∎

Part (a) of the following lemma gives a partial converse of property (c) above, part (b) is for later use. The proof is inspired by that of [[59](https://arxiv.org/html/2512.03267v1#bib.bib59), Theorem 133.4].

###### Lemma 5.8.

Suppose that the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless. Let gg be a distortion function with g​(0)=0g(0)=0 and g>0g>0 on (0,1](0,1] that is continuous on some neighbourhood of 0, and let ϕ\phi be a Young function that does not satisfy the Δ2\Delta\_{2}-condition.

*(a)* Then there is a risk X≥0X\geq 0 on Ω\Omega and y>x>0y>x>0 such that ψ​(x)=∞\psi(x)=\infty and ψ​(y)<∞\psi(y)<\infty.

*(b)* There are risks Xn∈(Lgϕ)+X\_{n}\in(L\_{g}^{\phi})\_{+} such that Xn↘0X\_{n}\searrow 0, but πg,ϕ,α​(Xn)≥12\pi\_{g,\phi,\alpha}(X\_{n})\geq\frac{1}{2} for all nn.

###### Proof.

(a) First, if ϕ\phi does not satisfy the Δ2\Delta\_{2}-condition, there is a strictly increasing positive sequence (tn)n(t\_{n})\_{n} such that ϕ​(2​tn)≥n​ϕ​(tn)\phi(2t\_{n})\geq n\phi(t\_{n}) and ϕ​(tn)≥1\phi(t\_{n})\geq 1, n≥1n\geq 1.

Now, by assumption, there is some u0∈(0,1]u\_{0}\in(0,1] such that g​(u0)>0g(u\_{0})>0 and g:[0,u0]→[0,g​(u0)]g:[0,u\_{0}]\to[0,g(u\_{0})] is continuous and hence surjective.

Next choose a strictly positive sequence (an)n(a\_{n})\_{n} such that ∑n=1∞an=g​(u0)\sum\_{n=1}^{\infty}a\_{n}=g(u\_{0}) and ∑n=1∞n​an=∞\sum\_{n=1}^{\infty}na\_{n}=\infty. By surjectivity, there is a strictly decreasing sequence (bn)n≥0(b\_{n})\_{n\geq 0} in (0,u0](0,u\_{0}] such that g​(bn)=∑k=n+1∞akϕ​(tk)g(b\_{n})=\sum\_{k=n+1}^{\infty}\frac{a\_{k}}{\phi(t\_{k})}, n≥0n\geq 0. Since g>0g>0 on (0,1](0,1], we have that bn→0b\_{n}\to 0.

Finally, since PP is atomless, there exists a pairwise disjoint sequence (An)n≥1(A\_{n})\_{n\geq 1} of sets in 𝒜\mathcal{A} with P​(An)=bn−1−bnP(A\_{n})=b\_{n-1}-b\_{n}, n≥1n\geq 1; see [[24](https://arxiv.org/html/2512.03267v1#bib.bib24), Theorem 8.14.2]. Consider the risk X=∑n=1∞tn​𝟙AnX=\sum\_{n=1}^{\infty}t\_{n}\mathds{1}\_{A\_{n}}. Then FX​(x)=1−bn−1F\_{X}(x)=1-b\_{n-1} for tn−1≤x<tnt\_{n-1}\leq x<t\_{n}, n≥1n\geq 1, where t0=0t\_{0}=0. Thus we have that

|  |  |  |
| --- | --- | --- |
|  | ψ​(1)=∑n=1∞ϕ​(tn)​(g​(bn−1)−g​(bn))=∑n=1∞an<∞,\psi(1)=\sum\_{n=1}^{\infty}\phi(t\_{n})(g(b\_{n-1})-g(b\_{n}))=\sum\_{n=1}^{\infty}a\_{n}<\infty, |  |

where we have used that gg is continuous at each bnb\_{n}; in the same way,

|  |  |  |
| --- | --- | --- |
|  | ψ​(12)=∑n=1∞ϕ​(2​tn)​anϕ​(tn)≥∑n=1∞n​an=∞.\psi(\tfrac{1}{2})=\sum\_{n=1}^{\infty}\phi(2t\_{n})\frac{a\_{n}}{\phi(t\_{n})}\geq\sum\_{n=1}^{\infty}na\_{n}=\infty. |  |

This proves the claim.

(b) Consider the risk X=∑n=1∞tn​𝟙AnX=\sum\_{n=1}^{\infty}t\_{n}\mathds{1}\_{A\_{n}} of part (a), and let Xn=∑k=n∞tk​𝟙AkX\_{n}=\sum\_{k=n}^{\infty}t\_{k}\mathds{1}\_{A\_{k}}, so that Xn↘0X\_{n}\searrow 0. Then X=X1X=X\_{1} satisfies ψ​(1)<∞\psi(1)<\infty, so that Xn∈(Lgϕ)+X\_{n}\in(L\_{g}^{\phi})\_{+} for all nn. Also,

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FXn−1​(1−u)1/2)​dg​(u)=∑k=n∞ϕ​(2​tk)​akϕ​(tk)≥∑k=n∞k​ak=∞,\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X\_{n}}^{-1}(1-u)}{1/2}\Big)\mathrm{d}g(u)=\sum\_{k=n}^{\infty}\phi(2t\_{k})\frac{a\_{k}}{\phi(t\_{k})}\geq\sum\_{k=n}^{\infty}ka\_{k}=\infty, |  |

so that πg,ϕ,α​(Xn)≥12\pi\_{g,\phi,\alpha}(X\_{n})\geq\tfrac{1}{2} for all nn, which had to be shown.
∎

Assertion (a) of the following result now characterizes when the infimum in the definition of the Orlicz-Lorentz premium is attained.

###### Proposition 5.9.

Let X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+}.

*(a)* We have that πg,ϕ,α​(X)≠0\pi\_{g,\phi,\alpha}(X)\neq 0 if and only if X≠0X\neq 0 and gg is not identically 0 on [0,P​(X>0))[0,P(X>0)). In that case,

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(X)=min⁡{a>0:∫01ϕ​(FX−1​(1−u)a)​dg​(u)≤1−α}.\displaystyle\pi\_{g,\phi,\alpha}(X)=\min\Big\{a>0:\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)\leq 1-\alpha\Big\}. |  |

*(b)* If a>0a>0 satisfies

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)=1−α,\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)=1-\alpha, |  |

then a=πg,ϕ,α​(X)a=\pi\_{g,\phi,\alpha}(X).

*(c)* Suppose that πg,ϕ,α​(X)≠0\pi\_{g,\phi,\alpha}(X)\neq 0. If g=0g=0 on some neighbourhood of 0, or if X∈L∞X\in L^{\infty}, or if ϕ\phi satisfies the Δ2\Delta\_{2}-condition, then there is a unique value a>0a>0 such that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)=1−α,\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)=1-\alpha, |  |

and a=πg,ϕ,α​(X)a=\pi\_{g,\phi,\alpha}(X).

###### Proof.

(a) If X=0X=0, or if X≠0X\neq 0 and g=0g=0 on [0,P​(X>0))[0,P(X>0)), then ψ​(x)=0\psi(x)=0 for all x>0x>0 by Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a), so that πg,ϕ,α​(X)=0\pi\_{g,\phi,\alpha}(X)=0. Otherwise, the result follows from the points (a), (d), (h) and (i) of Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"); note that {ψ<∞}≠∅\{\psi<\infty\}\neq\varnothing because X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+}.

(b) follows from Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(g).

(c) Again, {ψ<∞}≠∅\{\psi<\infty\}\neq\varnothing because X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+}. Thus, Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b) and (c) imply that {ψ<∞}=(0,∞)\{\psi<\infty\}=(0,\infty). Then existence follows from points (a), (e), (h) and (i) of Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). And uniqueness follows from (b) above.
∎

In other words, under the assumptions stated in (c), one can define πg,ϕ,α​(X)\pi\_{g,\phi,\alpha}(X) as the unique value satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)πg,ϕ,α​(X))​dg​(u)=1−α.\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{\pi\_{g,\phi,\alpha}(X)}\Big)\mathrm{d}g(u)=1-\alpha. |  | (5.3) |

This is the case, in particular, if gg is the identity function, X≠0X\neq 0, and either XX is bounded or ϕ\phi satisfies the Δ2\Delta\_{2}-condition, so that we recover the findings in [[29](https://arxiv.org/html/2512.03267v1#bib.bib29), Remark 3] and [[7](https://arxiv.org/html/2512.03267v1#bib.bib7), p. 108].

###### Remark 5.10.

In analogy to the so-called Orlicz hearts, see [[7](https://arxiv.org/html/2512.03267v1#bib.bib7)], [[19](https://arxiv.org/html/2512.03267v1#bib.bib19)], [[45](https://arxiv.org/html/2512.03267v1#bib.bib45), Section 3.4, Definition 2], one might define the heart MgϕM\_{g}^{\phi} of LgϕL\_{g}^{\phi} as the space of all risks XX for which

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(|FX−1​(1−u)|a)​dg​(u)<∞\int\_{0}^{1}\phi\Big(\frac{|F\_{X}^{-1}(1-u)|}{a}\Big)\mathrm{d}g(u)<\infty |  |

holds for all a>0a>0. It follows as in the proof of Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b) that

|  |  |  |
| --- | --- | --- |
|  | L∞⊂Mgϕ⊂Lgϕ.L^{\infty}\subset M\_{g}^{\phi}\subset L\_{g}^{\phi}. |  |

Moreover, by the proof of Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c), Mgϕ=LgϕM\_{g}^{\phi}=L\_{g}^{\phi} if ϕ\phi satisfies the Δ2\Delta\_{2}-condition. Now, several results in this paper that depend on the Δ2\Delta\_{2}-condition do in fact hold in MgϕM\_{g}^{\phi} for any ϕ\phi. For example, identity ([5.3](https://arxiv.org/html/2512.03267v1#S5.E3 "In 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) holds for all X∈MgϕX\in M\_{g}^{\phi} provided that πg,ϕ,α​(X)≠0\pi\_{g,\phi,\alpha}(X)\neq 0.

Since we are mainly interested in results that hold on all of LgϕL\_{g}^{\phi}, we do not pursue this aspect here.

### 5.4. Orlicz-Lorentz: risk theoretic properties

We obtain several properties of general Orlicz-Lorentz premia.

###### Proposition 5.11.

1. *(a)*

   For any X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+},

   |  |  |  |
   | --- | --- | --- |
   |  | ρg​(X)ϕ−1​(1−α)≤πg,ϕ,α​(X)≤ess​sup​Xϕ−1​(1−α).\frac{\rho\_{g}(X)}{\phi^{-1}(1-\alpha)}\leq\pi\_{g,\phi,\alpha}(X)\leq\frac{\mathrm{ess\,sup\,}X}{\phi^{-1}(1-\alpha)}. |  |
2. *(b)*

   For any b≥0b\geq 0, πg,ϕ,α​(b)=bϕ−1​(1−α)\pi\_{g,\phi,\alpha}(b)=\frac{b}{\phi^{-1}(1-\alpha)}.

###### Proof.

(a) First note that, by the assumptions on ϕ\phi, ϕ−1​(1−α)>0\phi^{-1}(1-\alpha)>0 is well defined and ϕ​(ϕ−1​(1−α))=1−α\phi(\phi^{-1}(1-\alpha))=1-\alpha.

The first inequality is trivial if ρg​(X)=0\rho\_{g}(X)=0. Else let 0<ε<ρg​(X)0<\varepsilon<\rho\_{g}(X). Then Jensen’s inequality implies by convexity of ϕ\phi that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)(ρg​(X)−ε)/ϕ−1​(1−α))​dg​(u)\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{(\rho\_{g}(X)-\varepsilon)/\phi^{-1}(1-\alpha)}\Big)\mathrm{d}g(u) | ≥ϕ​(ϕ−1​(1−α)ρg​(X)−ε​∫01FX−1​(1−u)​dg​(u))\displaystyle\geq\phi\Big(\frac{\phi^{-1}(1-\alpha)}{\rho\_{g}(X)-\varepsilon}\int\_{0}^{1}F\_{X}^{-1}(1-u)\mathrm{d}g(u)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϕ​(ϕ−1​(1−α)ρg​(X)−ε​ρg​(X))>1−α,\displaystyle=\phi\Big(\frac{\phi^{-1}(1-\alpha)}{\rho\_{g}(X)-\varepsilon}\rho\_{g}(X)\Big)>1-\alpha, |  |

where we have used that ϕ\phi is strictly increasing on {ϕ>0}\{\phi>0\}. Thus πg,ϕ,α​(X)≥ρg​(X)−εϕ−1​(1−α)\pi\_{g,\phi,\alpha}(X)\geq\frac{\rho\_{g}(X)-\varepsilon}{\phi^{-1}(1-\alpha)} for any ε>0\varepsilon>0, which implies the first inequality.

The second inequality is trivial if ess​sup​X=∞\mathrm{ess\,sup\,}X=\infty. Otherwise we use the fact that FX−1F\_{X}^{-1} is bounded by ess​sup​X\mathrm{ess\,sup\,}X and take a=ess​sup​Xϕ−1​(1−α)a=\frac{\mathrm{ess\,sup\,}X}{\phi^{-1}(1-\alpha)}.

(b) follows directly from the fact that Fb−1=bF^{-1}\_{b}=b on (0,1](0,1] and Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b).
∎

###### Proposition 5.12.

The Orlicz-Lorentz premium πg,ϕ,α\pi\_{g,\phi,\alpha} is monotonic and positively homogeneous on (Lgϕ)+(L\_{g}^{\phi})\_{+}.

###### Proof.

The monotonicity follows from the monotonicity of ϕ\phi and FX−1F\_{X}^{-1}. The positive homogeneity follows from the fact that, for λ>0\lambda>0, ϕ​(Fλ​X−1​(1−u)a)=ϕ​(FX−1​(1−u)a/λ)\phi\big(\frac{F\_{\lambda X}^{-1}(1-u)}{a}\big)=\phi\big(\frac{F\_{X}^{-1}(1-u)}{a/\lambda}\big); note also that πg,ϕ,α​(0)=0\pi\_{g,\phi,\alpha}(0)=0.
∎

We will next show that Orlicz-Lorentz premia are subadditive for comonotonic risks; unlike for the distortion risk measures, see Proposition
[3.11](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), one cannot expect additivity here because Orlicz premia already fail to have this property. For a concrete counter-example, take ϕ​(t)=t2\phi(t)=t^{2}, any α<1\alpha<1, X=𝟙[0,12)​(U)X=\mathds{1}\_{[0,\frac{1}{2})}(U) and Y=𝟙[12,1]​(U)Y=\mathds{1}\_{[\frac{1}{2},1]}(U), where UU is uniformly distributed on [0,1][0,1].

###### Proposition 5.13.

Let X,Y∈(Lgϕ)+X,Y\in(L\_{g}^{\phi})\_{+} be comonotonic risks. Then
X+Y∈(Lgϕ)+X+Y\in(L\_{g}^{\phi})\_{+} and

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(X+Y)≤πg,ϕ,α​(X)+πg,ϕ,α​(Y).\pi\_{g,\phi,\alpha}(X+Y)\leq\pi\_{g,\phi,\alpha}(X)+\pi\_{g,\phi,\alpha}(Y). |  |

###### Proof.

Let ε>0\varepsilon>0. Then there are a1,a2>0a\_{1},a\_{2}>0 with a1<πg,ϕ,α​(X)+εa\_{1}<\pi\_{g,\phi,\alpha}(X)+\varepsilon and a2<πg,ϕ,α​(Y)+εa\_{2}<\pi\_{g,\phi,\alpha}(Y)+\varepsilon
such that ∫01ϕ​(FX−1​(1−u)a1)​dg​(u)≤1−α\int\_{0}^{1}\phi(\frac{F\_{X}^{-1}(1-u)}{a\_{1}})\mathrm{d}g(u)\leq 1-\alpha and ∫01ϕ​(FY−1​(1−u)a2)​dg​(u)≤1−α\int\_{0}^{1}\phi(\frac{F\_{Y}^{-1}(1-u)}{a\_{2}})\mathrm{d}g(u)\leq 1-\alpha.

Now, by comonotonic additivity of VaR\mathrm{VaR}, we have that FX+Y−1=FX−1+FY−1F\_{X+Y}^{-1}=F\_{X}^{-1}+F\_{Y}^{-1} and therefore, using the convexity of ϕ\phi,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(FX+Y−1​(1−u)a1+a2)\displaystyle\phi\Big(\frac{F\_{X+Y}^{-1}(1-u)}{a\_{1}+a\_{2}}\Big) | =ϕ​(a1a1+a2​FX−1​(1−u)a1+a2a1+a2​FY−1​(1−u)a2)\displaystyle=\phi\Big(\frac{a\_{1}}{a\_{1}+a\_{2}}\frac{F\_{X}^{-1}(1-u)}{a\_{1}}+\frac{a\_{2}}{a\_{1}+a\_{2}}\frac{F\_{Y}^{-1}(1-u)}{a\_{2}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤a1a1+a2​ϕ​(FX−1​(1−u)a1)+a2a1+a2​ϕ​(FY−1​(1−u)a2).\displaystyle\leq\frac{a\_{1}}{a\_{1}+a\_{2}}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a\_{1}}\Big)+\frac{a\_{2}}{a\_{1}+a\_{2}}\phi\Big(\frac{F\_{Y}^{-1}(1-u)}{a\_{2}}\Big). |  |

Integrating with respect to d​g\mathrm{d}g we obtain by the properties of a1a\_{1} and a2a\_{2} that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX+Y−1​(1−u)a1+a2)​dg​(u)≤1−α,\int\_{0}^{1}\phi\Big(\frac{F\_{X+Y}^{-1}(1-u)}{a\_{1}+a\_{2}}\Big)\mathrm{d}g(u)\leq 1-\alpha, |  |

which implies that X+Y∈(Lgϕ)+X+Y\in(L\_{g}^{\phi})\_{+} and

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(X+Y)≤a1+a2.\pi\_{g,\phi,\alpha}(X+Y)\leq a\_{1}+a\_{2}. |  |

Since ε>0\varepsilon>0 is arbitrary, the result follows.
∎

As for the Fatou properties, we have the following results.

###### Proposition 5.14.

The Orlicz-Lorentz premium πg,ϕ,α\pi\_{g,\phi,\alpha} has the Fatou property on (Lgϕ)+(L\_{g}^{\phi})\_{+}.

###### Proof.

By Remark [2.4](https://arxiv.org/html/2512.03267v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) and Proposition [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") it suffices to show that if Xn↗XX\_{n}\nearrow X and X1,X∈(Lgϕ)+X\_{1},X\in(L\_{g}^{\phi})\_{+} then πg,ϕ,α​(Xn)→πg,ϕ,α​(X)\pi\_{g,\phi,\alpha}(X\_{n})\to\pi\_{g,\phi,\alpha}(X), or, equivalently, πg,ϕ,α​(X)≤supnπg,ϕ,α​(Xn)\pi\_{g,\phi,\alpha}(X)\leq\sup\_{n}\pi\_{g,\phi,\alpha}(X\_{n}).

We first note that by ([3.1](https://arxiv.org/html/2512.03267v1#S3.E1 "In 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) and a property of quantile functions we have for X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+} and a>0a>0

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)=∫0∞g​(F¯ϕ​(Xa)​(x)−)​dx.\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)=\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X}{a})}(x)-\big)\mathrm{d}x. |  |

Let Xn↗XX\_{n}\nearrow X with X1,X∈(Lgϕ)+X\_{1},X\in(L\_{g}^{\phi})\_{+}. As in the proof of Proposition [3.13](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem13 "Proposition 3.13. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") one deduces that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FXn−1​(1−u)a)​dg​(u)↗∫01ϕ​(FX−1​(1−u)a)​dg​(u).\int\_{0}^{1}\phi\Big(\frac{F\_{X\_{n}}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)\nearrow\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u). |  | (5.4) |

Take a=supnπg,ϕ,α​(Xn)a=\sup\_{n}\pi\_{g,\phi,\alpha}(X\_{n}) and ε>0\varepsilon>0. By definition, we have for any nn,

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FXn−1​(1−u)a+ε)​dg​(u)≤1−α.\int\_{0}^{1}\phi\Big(\frac{F\_{X\_{n}}^{-1}(1-u)}{a+\varepsilon}\Big)\mathrm{d}g(u)\leq 1-\alpha. |  |

By ([5.4](https://arxiv.org/html/2512.03267v1#S5.E4 "In 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) we find that ∫01ϕ​(FX−1​(1−u)a+ε)​dg​(u)≤1−α\int\_{0}^{1}\phi(\frac{F\_{X}^{-1}(1-u)}{a+\varepsilon})\mathrm{d}g(u)\leq 1-\alpha and thus πg,ϕ,α​(X)≤a+ε\pi\_{g,\phi,\alpha}(X)\leq a+\varepsilon. Since ε>0\varepsilon>0 is arbitrary, the claim follows.
∎

In the sequel, the following property (Pg,ϕP\_{g,\phi}) will be crucial:
  

– g​(0)=0g(0)=0,
– gg is continuous, and
– either g=0g=0 on some neighbourhood of 0
– or ϕ\phi satisfies the Δ2\Delta\_{2}-condition.

###### Proposition 5.15.

*(a)* If *(Pg,ϕP\_{g,\phi})* holds, then πg,ϕ,α\pi\_{g,\phi,\alpha} has the reverse Fatou property on (Lgϕ)+(L\_{g}^{\phi})\_{+}, and hence the Lebesgue property.

*(b)* If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless, then πg,ϕ,α\pi\_{g,\phi,\alpha} has the reverse Fatou property on (Lgϕ)+(L\_{g}^{\phi})\_{+} if and only if *(Pg,ϕP\_{g,\phi})* holds.

###### Proof.

(a) It suffices, by Remark [2.4](https://arxiv.org/html/2512.03267v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) and Proposition [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), to prove that if Xn↘XX\_{n}\searrow X and X1,X∈(Lgϕ)+X\_{1},X\in(L\_{g}^{\phi})\_{+} then πg,ϕ,α​(X)≥infnπg,ϕ,α​(Xn)\pi\_{g,\phi,\alpha}(X)\geq\inf\_{n}\pi\_{g,\phi,\alpha}(X\_{n}). This is trivial if a:=infnπg,ϕ,α​(Xn)=0a:=\inf\_{n}\pi\_{g,\phi,\alpha}(X\_{n})=0. So suppose that a>0a>0, and let an=πg,ϕ,α​(Xn)a\_{n}=\pi\_{g,\phi,\alpha}(X\_{n}), n≥1n\geq 1. Since an>0a\_{n}>0, Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) with (Pg,ϕP\_{g,\phi}) implies that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FXn−1​(1−u)an)​dg​(u)=1−α\int\_{0}^{1}\phi\Big(\frac{F\_{X\_{n}}^{-1}(1-u)}{a\_{n}}\Big)\mathrm{d}g(u)=1-\alpha |  |

for all nn. Hence, by ([3.1](https://arxiv.org/html/2512.03267v1#S3.E1 "In 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), a property of quantile functions, the continuity of gg, and the fact that g​(0−)=g​(0)=0g(0-)=g(0)=0,

|  |  |  |
| --- | --- | --- |
|  | ∫0∞g​(F¯ϕ​(Xnan)​(x))​dx=1−α\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X\_{n}}{a\_{n}})}(x)\big)\mathrm{d}x=1-\alpha |  |

for all nn. Now since Xn→XX\_{n}\to X, an→a≠0a\_{n}\to a\neq 0, and ϕ\phi is continuous, we have that ϕ​(Xnan)→ϕ​(Xa)\phi(\frac{X\_{n}}{a\_{n}})\to\phi(\frac{X}{a}), and hence F¯ϕ​(Xnan)​(x)→F¯ϕ​(Xa)​(x)\overline{F}\_{\phi(\frac{X\_{n}}{a\_{n}})}(x)\to\overline{F}\_{\phi(\frac{X}{a})}(x) for all x≥0x\geq 0 with at most countably many exceptions. In view of the continuity of gg we deduce that

|  |  |  |
| --- | --- | --- |
|  | ∫0∞g​(F¯ϕ​(Xa)​(x))​dx=1−α,\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X}{a})}(x)\big)\mathrm{d}x=1-\alpha, |  |

where we have used the dominated convergence theorem; note that 0≤Xn≤X10\leq X\_{n}\leq X\_{1} and, by Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b) and (c), ∫0∞g​(F¯ϕ​(X1a)​(x))​dx<∞\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X\_{1}}{a})}(x)\big)\mathrm{d}x<\infty.

Now, by Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), we obtain that πg,ϕ,α​(X)=a\pi\_{g,\phi,\alpha}(X)=a.

(b) Suppose that πg,ϕ,α\pi\_{g,\phi,\alpha} possesses the reverse Fatou property.

First, suppose that gg is not continuous or that g​(0)≠0g(0)\neq 0. Then there is some u∈[0,1)u\in\mathopen{[}0,1) such that g​(u−)<g​(u)g(u-)<g(u); recall that g​(0−)=0g(0-)=0. Let (pn)n(p\_{n})\_{n} be a strictly decreasing sequence in [0,1][0,1] with limit uu. As in the proof of Proposition [3.16](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem16 "Proposition 3.16. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), we define Xn=𝟙AnX\_{n}=\mathds{1}\_{A\_{n}} and X=𝟙AX=\mathds{1}\_{A}, where (An)n(A\_{n})\_{n} is a decreasing sequence of sets in 𝒜\mathcal{A} with P​(An)=pnP(A\_{n})=p\_{n}, n≥1n\geq 1, and A:=⋂n=1∞AnA:=\bigcap\_{n=1}^{\infty}A\_{n}, which satisfies P​(A)=uP(A)=u. Then the XnX\_{n} belong to (Lgϕ)+(L\_{g}^{\phi})\_{+} as bounded risks, and Xn→XX\_{n}\to X on Ω\Omega. Also, πg,ϕ,α​(Xn)=inf{a>0:ϕ​(1a)​g​(pn−)≤1−α}\pi\_{g,\phi,\alpha}(X\_{n})=\inf\{a>0:\phi(\frac{1}{a})g(p\_{n}-)\leq 1-\alpha\}, hence

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(Xn)=1ϕ−1​(1−αg​(pn−))≥1ϕ−1​(1−αg​(u))\pi\_{g,\phi,\alpha}(X\_{n})=\frac{1}{\phi^{-1}\Big(\frac{1-\alpha}{g(p\_{n}-)}\Big)}\geq\frac{1}{\phi^{-1}\Big(\frac{1-\alpha}{g(u)}\Big)} |  |

for all nn, while πg,ϕ,α​(X)=1/ϕ−1​(1−αg​(u−))\pi\_{g,\phi,\alpha}(X)=1/\phi^{-1}(\frac{1-\alpha}{g(u-)}) for u>0u>0 and πg,ϕ,α​(X)=0\pi\_{g,\phi,\alpha}(X)=0 for u=0u=0. Since ϕ−1\phi^{-1} is strictly increasing on (0,∞)(0,\infty), we see that πg,ϕ,α​(X)<lim supn→∞πg,ϕ,α​(Xn)\pi\_{g,\phi,\alpha}(X)<\limsup\_{n\to\infty}\pi\_{g,\phi,\alpha}(X\_{n}), contradicting the reverse Fatou property. So we have that gg is continuous and g​(0)=0g(0)=0.

Secondly, suppose that g>0g>0 on (0,1](0,1] and that ϕ\phi does not satisfy the Δ2\Delta\_{2}-condition. Then, by Lemma [5.8](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem8 "Lemma 5.8. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), there are risks Xn∈(Lgϕ)+X\_{n}\in(L\_{g}^{\phi})\_{+} such that Xn↘0X\_{n}\searrow 0 and πg,ϕ,α​(Xn)≥12\pi\_{g,\phi,\alpha}(X\_{n})\geq\frac{1}{2} for all nn. This contradicts the reverse Fatou property.
∎

When we decide to work on L+∞L^{\infty}\_{+}, Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) tells us that we do not need to demand that gg is constant on some neighbourhood of 0 or that ϕ\phi satisfies the Δ2\Delta\_{2}-condition. Thus the same proof as above yields the following.

###### Proposition 5.16.

*(a)* If g​(0)=0g(0)=0 and gg is continuous, then πg,ϕ,α\pi\_{g,\phi,\alpha} has the reverse Fatou property on L+∞L^{\infty}\_{+}, and hence the Lebesgue property.

*(b)* If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless, then πg,ϕ,α\pi\_{g,\phi,\alpha} has the reverse Fatou property on L+∞L^{\infty}\_{+} if and only if g​(0)=0g(0)=0 and gg is continuous.

Also, πg,ϕ,α\pi\_{g,\phi,\alpha} quite trivially preserves dominance in the stochastic order. Recall that a risk XX is said to be smaller than a risk YY in stochastic dominance (or in stochastic order), denoted as X≤stYX\leq\_{\text{st}}Y, if

|  |  |  |
| --- | --- | --- |
|  | FX​(x)≥FY​(x)for all x∈ℝ,F\_{X}(x)\geq F\_{Y}(x)\quad\text{for all $x\in\mathbb{R}$}, |  |

which is equivalent to saying that FX−1​(u)≤FY−1​(u)F\_{X}^{-1}(u)\leq F\_{Y}^{-1}(u) for all u∈(0,1)u\in(0,1); see [[14](https://arxiv.org/html/2512.03267v1#bib.bib14)], [[18](https://arxiv.org/html/2512.03267v1#bib.bib18)], [[51](https://arxiv.org/html/2512.03267v1#bib.bib51)].

Thus we have:

###### Proposition 5.17.

Let Y∈(Lgϕ)+Y\in(L\_{g}^{\phi})\_{+} and X≥0X\geq 0. Then

|  |  |  |
| --- | --- | --- |
|  | X≤*st*Y⟹X∈(Lgϕ)+​ and ​πg,ϕ,α​(X)≤πg,ϕ,α​(Y).X\leq\_{\emph{\text{st}}}Y\Longrightarrow X\in(L\_{g}^{\phi})\_{+}\text{ and }\pi\_{g,\phi,\alpha}(X)\leq\pi\_{g,\phi,\alpha}(Y). |  |

### 5.5. Orlicz-Lorentz: the concave case

In order to deduce stronger properties of the Orlicz-Lorentz premia we will now demand that gg be concave.

We first need the following technical result on general positive risks, which is an immediate consequence of a well known representation of the Tail Value at Risk.

###### Lemma 5.18.

Let ϕ\phi be a Young function, X≥0X\geq 0 a risk, a>0a>0 and 0<β≤10<\beta\leq 1. Then, for any x≥0x\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ∫0βϕ​(FX−1​(1−u)a)​du≤E​((ϕ​(Xa)−x)+)+β​x,\displaystyle\int\_{0}^{\beta}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}u\leq E\Big(\Big(\phi\Big(\frac{X}{a}\Big)-x\Big)^{+}\Big)+\beta x, |  |

with equality at x=ϕ​(FX−1​(1−β)a)x=\phi\big(\frac{F\_{X}^{-1}(1-\beta)}{a}\big) if β<1\beta<1 and x=0x=0 if β=1\beta=1.

###### Proof.

Let XX be a positive risk. If X∈L1X\in L^{1} and 0<α<10<\alpha<1, we have by Proposition [3.7](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that, for any x≥0x\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 11−α​∫α1FX−1​(u)​du≤11−α​E​((X−x)+)+x,\frac{1}{1-\alpha}\int\_{\alpha}^{1}F\_{X}^{-1}(u)\mathrm{d}u\leq\frac{1}{1-\alpha}E\big((X-x)^{+}\big)+x, |  |

with equality at x=FX−1​(α)x=F\_{X}^{-1}(\alpha). If α=0\alpha=0 then

|  |  |  |
| --- | --- | --- |
|  | ∫α1FX−1​(u)​du=E​(X)≤E​((X−x)+)+x\int\_{\alpha}^{1}F\_{X}^{-1}(u)\mathrm{d}u=E(X)\leq E\big((X-x)^{+}\big)+x |  |

for any x≥0x\geq 0 since y≤(y−x)++xy\leq(y-x)^{+}+x, y∈ℝy\in\mathbb{R}, and we have equality for x=0x=0.

If E​(X)=∞E(X)=\infty, both sides of these inequalities are infinite for any x≥0x\geq 0.

Writing β=1−α\beta=1-\alpha and replacing XX by ϕ​(Xa)\phi\big(\frac{X}{a}\big) then proves the claim, where we note that Fϕ​(X/a)−1=ϕ​(FX−1/a)F^{-1}\_{\phi(X/a)}=\phi(F\_{X}^{-1}/a).
∎

We can now show that πg,ϕ,α\pi\_{g,\phi,\alpha} preserves stop-loss order. Here, a risk XX is said to be smaller than a risk YY in stop-loss order (or in increasing convex order), denoted as X≤slYX\leq\_{\text{sl}}Y, if

|  |  |  |
| --- | --- | --- |
|  | E​((X−d)+)≤E​((Y−d)+)for all d∈ℝ,E((X-d)^{+})\leq E((Y-d)^{+})\quad\text{for all $d\in\mathbb{R}$}, |  |

see [[14](https://arxiv.org/html/2512.03267v1#bib.bib14)], [[18](https://arxiv.org/html/2512.03267v1#bib.bib18)], [[51](https://arxiv.org/html/2512.03267v1#bib.bib51)]. If XX and YY are positive, this is equivalent to saying that E​(φ​(X))≤E​(φ​(Y))E(\varphi(X))\leq E(\varphi(Y)) for all increasing convex functions φ\varphi on ℝ\mathbb{R} for which the expectations exist, see [[51](https://arxiv.org/html/2512.03267v1#bib.bib51), Theorem 4.A.2].

###### Proposition 5.19.

Let gg be concave. Let X≥0X\geq 0 and Y∈(Lgϕ)+Y\in(L\_{g}^{\phi})\_{+}. Then

|  |  |  |
| --- | --- | --- |
|  | X≤*sl*Y⟹X∈(Lgϕ)+​ and ​πg,ϕ,α​(X)≤πg,ϕ,α​(Y).X\leq\_{\emph{\text{sl}}}Y\Longrightarrow X\in(L\_{g}^{\phi})\_{+}\text{ and }\pi\_{g,\phi,\alpha}(X)\leq\pi\_{g,\phi,\alpha}(Y). |  |

###### Proof.

Let X≥0X\geq 0 and Y∈(Lgϕ)+Y\in(L\_{g}^{\phi})\_{+} with X≤slYX\leq\_{\text{sl}}Y.

Let us first assume that gg is concave and piecewise linear. Then there are 0<β1<β2<…<βn=10<\beta\_{1}<\beta\_{2}<\ldots<\beta\_{n}=1, c0≥1c\_{0}\geq 1 and ck>0c\_{k}>0, k=1,…,n,k=1,\ldots,n, such that

|  |  |  |
| --- | --- | --- |
|  | g​(u)=c0+∑k=1nck​min⁡(uβk,1),u∈[0,1].g(u)=c\_{0}+\sum\_{k=1}^{n}c\_{k}\min\Big(\frac{u}{\beta\_{k}},1\Big),u\in[0,1]. |  |

Since c0+∑k=1nck=1c\_{0}+\sum\_{k=1}^{n}c\_{k}=1, gg is a convex combination of the functions g0=1g\_{0}=1 and gk​(u)=min⁡(uβk,1)g\_{k}(u)=\min\big(\frac{u}{\beta\_{k}},1\big), k=1,…,nk=1,\ldots,n. Thus, for any a>0a>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u) | =∑k=0nck​∫01ϕ​(FX−1​(1−u)a)​dgk​(u)\displaystyle=\sum\_{k=0}^{n}c\_{k}\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g\_{k}(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c0​ϕ​(FX−1​(1)a)+∑k=1nckβk​∫0βkϕ​(FX−1​(1−u)a)​du,\displaystyle=c\_{0}\phi\Big(\frac{F\_{X}^{-1}(1)}{a}\Big)+\sum\_{k=1}^{n}\frac{c\_{k}}{\beta\_{k}}\int\_{0}^{\beta\_{k}}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}u, |  |

and similarly for YY. Note that if c0>0c\_{0}>0 then XX is bounded above because X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+}, see the discussion after Definition [5.1](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem1 "Definition 5.1. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). Now, X≤slYX\leq\_{\text{sl}}Y implies, in particular, that ess​sup​X≤ess​sup​Y\mathrm{ess\,sup\,}X\leq\mathrm{ess\,sup\,}Y (use the argument in [[14](https://arxiv.org/html/2512.03267v1#bib.bib14), Section 3.4.1.1]), hence FX−1​(1)≤FY−1​(1)<∞F\_{X}^{-1}(1)\leq F\_{Y}^{-1}(1)<\infty. Thus, the first term is defined. On the other hand, if c0=0c\_{0}=0, we take it to be zero.

Let xk=ϕ​(FY−1​(1−βk)a)x\_{k}=\phi\big(\frac{F\_{Y}^{-1}(1-\beta\_{k})}{a}\big), k=1,…,n−1k=1,\ldots,n-1, and xn=0x\_{n}=0. It then follows with Lemma [5.18](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem18 "Lemma 5.18. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)≤c0​ϕ​(FX−1​(1)a)+∑k=1nckβk​(E​((ϕ​(Xa)−xk)+)+βk​xk).\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)\leq c\_{0}\phi\Big(\frac{F\_{X}^{-1}(1)}{a}\Big)+\sum\_{k=1}^{n}\frac{c\_{k}}{\beta\_{k}}\Big(E\Big(\Big(\phi\Big(\frac{X}{a}\Big)-x\_{k}\Big)^{+}\Big)+\beta\_{k}x\_{k}\Big). |  |

As we have seen, FX−1​(1)≤FY−1​(1)F\_{X}^{-1}(1)\leq F\_{Y}^{-1}(1). Also, since t↦(ϕ​(ta)−x)+t\mapsto\big(\phi\big(\frac{t}{a}\big)-x\big)^{+} is an increasing convex function on [0,∞)[0,\infty), the stop-loss order implies that E​((ϕ​(Xa)−xk)+)≤E​((ϕ​(Ya)−xk)+)E\big(\big(\phi\big(\frac{X}{a}\big)-x\_{k}\big)^{+}\big)\leq E\big(\big(\phi\big(\frac{Y}{a}\big)-x\_{k}\big)^{+}\big) for k=1,…,nk=1,\ldots,n. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u) | ≤c0​ϕ​(FY−1​(1)a)+∑k=1nckβk​(E​((ϕ​(Ya)−xk)+)+βk​xk)\displaystyle\leq c\_{0}\phi\Big(\frac{F\_{Y}^{-1}(1)}{a}\Big)+\sum\_{k=1}^{n}\frac{c\_{k}}{\beta\_{k}}\Big(E\Big(\Big(\phi\Big(\frac{Y}{a}\Big)-x\_{k}\Big)^{+}\Big)+\beta\_{k}x\_{k}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01ϕ​(FY−1​(1−u)a)​dg​(u),\displaystyle=\int\_{0}^{1}\phi\Big(\frac{F\_{Y}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u), |  |

where the last equality follows from Lemma [5.18](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem18 "Lemma 5.18. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") with the definition of the xkx\_{k}.

To finish the proof, let gg be an arbitrary concave distortion function. Then there exists an increasing sequence (gn)n(g\_{n})\_{n} of piecewise linear concave distortion functions that tends pointwise to gg as n→∞n\to\infty, and hence also gn​(u−)→g​(u−)g\_{n}(u-)\to g(u-) for all u∈[0,1]u\in[0,1].
If X∈(Lgϕ)+X\in(L\_{g}^{\phi})\_{+}, then also X∈(Lgnϕ)+X\in(L\_{g\_{n}}^{\phi})\_{+} for all nn.

Using ([3.1](https://arxiv.org/html/2512.03267v1#S3.E1 "In 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), a property of quantile functions, and the monotone convergence theorem, we then get, for any a>0a>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dgn​(u)\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g\_{n}(u) | =∫0∞gn​(F¯ϕ​(Xa)​(x)−)​dx\displaystyle=\int\_{0}^{\infty}g\_{n}\big(\overline{F}\_{\phi(\frac{X}{a})}(x)-\big)\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →∫0∞g​(F¯ϕ​(Xa)​(x)−)​dx=∫01ϕ​(FX−1​(1−u)a)​dg​(u).\displaystyle\to\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X}{a})}(x)-\big)\mathrm{d}x=\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u). |  |

Since the same holds for YY, the previous inequality for piecewise linear concave distortion functions implies that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−1​(1−u)a)​dg​(u)≤∫01ϕ​(FY−1​(1−u)a)​dg​(u).\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)\leq\int\_{0}^{1}\phi\Big(\frac{F\_{Y}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u). |  |

Since this holds for all a>0a>0, we finally deduce that

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(X)≤πg,ϕ,α​(Y).∎\pi\_{g,\phi,\alpha}(X)\leq\pi\_{g,\phi,\alpha}(Y).\qed |  |

This now leads to a simple proof that for concave distortion functions, the Orlicz-Lorentz premia are subadditive. Indeed, it was shown in [[56](https://arxiv.org/html/2512.03267v1#bib.bib56), Corollary 8] that any risk measure that preserves stop-loss and is additive for comonotonic risks is subadditive for arbitrary risks. But the proof for this given in [[18](https://arxiv.org/html/2512.03267v1#bib.bib18), Theorem 4.2.2] also works if the risk measure is only subadditive for comonotonic risks. For the sake of completeness, we give the proof here; recall that X=dYX=\_{d}Y means that XX and YY have the same distribution.

###### Lemma 5.20.

Suppose that the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless. Let 𝒳\mathcal{X} be a set of positive risks on Ω\Omega that contains the constants and ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R} a risk measure such that

1. *(i)*

   X≥0X\geq 0, Y∈𝒳Y\in\mathcal{X}, X=dYX=\_{d}Y ⟹\Longrightarrow X∈𝒳X\in\mathcal{X} and ρ​(X)=ρ​(Y)\rho(X)=\rho(Y);
2. *(ii)*

   X,Y∈𝒳X,Y\in\mathcal{X} comonotonic ⟹\Longrightarrow X+Y∈𝒳X+Y\in\mathcal{X} and ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y);
3. *(iii)*

   X≥0X\geq 0, Y∈𝒳Y\in\mathcal{X}, X≤*sl*YX\leq\_{\emph{\text{sl}}}Y ⟹X∈𝒳\Longrightarrow X\in\mathcal{X} and ρ​(X)≤ρ​(Y)\rho(X)\leq\rho(Y).

Then, for all X,Y∈𝒳X,Y\in\mathcal{X}, X+Y∈𝒳X+Y\in\mathcal{X} and ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y).

###### Proof.

Let X,Y∈𝒳X,Y\in\mathcal{X}. Since PP has no atoms, there is a random variable UU on Ω\Omega that is uniformly distributed on (0,1)(0,1), see [[21](https://arxiv.org/html/2512.03267v1#bib.bib21), Proposition A.31]. Then Xc:=FX−1​(U)X^{c}:=F\_{X}^{-1}(U) and XX have the same distribution, as do Yc:=FY−1​(U)Y^{c}:=F\_{Y}^{-1}(U) and YY, see [[14](https://arxiv.org/html/2512.03267v1#bib.bib14), Property 1.5.20]. By (i), Xc,Yc∈𝒳X^{c},Y^{c}\in\mathcal{X}. Now, XcX^{c} and YcY^{c} are comonotonic, so that, by (ii) with (i), Xc+Yc∈𝒳X^{c}+Y^{c}\in\mathcal{X} and ρ​(Xc+Yc)≤ρ​(X)+ρ​(Y)\rho(X^{c}+Y^{c})\leq\rho(X)+\rho(Y). Moreover, we have that X+Y≤slXc+YcX+Y\leq\_{\text{sl}}X^{c}+Y^{c}, see [[15](https://arxiv.org/html/2512.03267v1#bib.bib15), Theorem 7] or [[34](https://arxiv.org/html/2512.03267v1#bib.bib34), Proposition 1]. Thus, by (iii), X+Y∈𝒳X+Y\in\mathcal{X} and ρ​(X+Y)≤ρ​(Xc+Yc)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X^{c}+Y^{c})\leq\rho(X)+\rho(Y), as had to be shown.
∎

Thus we obtain the main result of this section.

###### Theorem 5.21.

If gg is concave, then (Lgϕ)+(L\_{g}^{\phi})\_{+} is a convex cone, and the Orlicz-Lorentz premium πg,ϕ,α\pi\_{g,\phi,\alpha} is subadditive on (Lgϕ)+(L\_{g}^{\phi})\_{+}.

###### Proof.

We first assume that the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless. Then, by Propositions [5.13](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem13 "Proposition 5.13. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.19](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem19 "Proposition 5.19. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), πg,ϕ,α\pi\_{g,\phi,\alpha} satisfies assumptions (ii) and (iii) of Lemma [5.20](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem20 "Lemma 5.20. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), while assumption (i) obviously holds. Thus (Lgϕ)+(L\_{g}^{\phi})\_{+} is invariant under taking sums, and πg,ϕ,α\pi\_{g,\phi,\alpha} is subadditive. Since (Lgϕ)+(L\_{g}^{\phi})\_{+} is also clearly invariant under positive scalar multiplication, it is a convex cone.

There is a slight technical problem if PP is not atomless. However, by [[24](https://arxiv.org/html/2512.03267v1#bib.bib24), Example 8.14.3], the product space given by Ω~=Ω×[0,1]\widetilde{\Omega}=\Omega\times[0,1], 𝒜~=𝒜⊗ℬ​[0,1]\widetilde{\mathcal{A}}=\mathcal{A}\otimes\mathcal{B}[0,1], P~=P⊗m\widetilde{P}=P\otimes m, is atomless, where mm is the Lebesgue measure. Then the mapping (Lgϕ)+​(Ω)→(Lgϕ)+​(Ω~)(L\_{g}^{\phi})\_{+}(\Omega)\to(L\_{g}^{\phi})\_{+}(\widetilde{\Omega}), X↦X~X\mapsto\widetilde{X} with X~​(ω,u)=X​(ω)\widetilde{X}(\omega,u)=X(\omega) for (ω,u)∈Ω×[0,1](\omega,u)\in\Omega\times[0,1], allows to transfer the result from (Lgϕ)+​(Ω~)(L\_{g}^{\phi})\_{+}(\widetilde{\Omega}) to (Lgϕ)+​(Ω)(L\_{g}^{\phi})\_{+}(\Omega); note that X+Y~=X~+Y~.\widetilde{X+Y}=\widetilde{X}+\widetilde{Y}.
∎

We have followed here the strategy of proof from [[18](https://arxiv.org/html/2512.03267v1#bib.bib18), Section 5.2] or [[56](https://arxiv.org/html/2512.03267v1#bib.bib56), Corollary 8]; a different, self-contained proof of Theorem [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") was given by the first author in [[28](https://arxiv.org/html/2512.03267v1#bib.bib28)].

### 5.6. Distortion Haezendonck-Goovaerts risk measures

Having the Orlicz-Lorentz premia at our disposal, we can now define the distortion Haezendonck-Goovaerts risk measures by the same simple procedure as in Section [4](https://arxiv.org/html/2512.03267v1#S4 "4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Definition 5.22.

Let gg be a distortion function, ϕ\phi a normalized Young function, and α∈[0,1)\alpha\in[0,1). The distortion Haezendonck-Goovaerts risk measure ρg,ϕ,α:Lgϕ→ℝ\rho\_{g,\phi,\alpha}:L^{\phi}\_{g}\to\mathbb{R} is given by

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​(X)=infx∈ℝ(πg,ϕ,α​((X−x)+)+x).\rho\_{g,\phi,\alpha}(X)=\inf\_{x\in\mathbb{R}}\big(\pi\_{g,\phi,\alpha}((X-x)^{+})+x\big). |  |

It follows as in our discussion after Definition [4.10](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem10 "Definition 4.10. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), using Proposition [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), that we can assume here without loss of generality that ϕ\phi is normalized and that we need to impose that α≥0\alpha\geq 0, and thus α∈[0,1)\alpha\in[0,1), in order to have a risk measure.

###### Remark 5.23.

The definition of the distortion Haezendonck-Goovaerts risk measure was suggested by Definition 4.2 of Goovaerts, Linders, Van Weert, and Tank [[27](https://arxiv.org/html/2512.03267v1#bib.bib27)], who call it the optimal generalized Haezendonck–Goovaerts risk measure; they consider the case when α∈(0,1)\alpha\in(0,1). The link between the two definitions becomes clearer by noting that

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​((X−x)+)+x=inf{a>x:∫01ϕ​((FX−1​(1−u)−x)+a−x)​dg​(u)≤1−α}.\displaystyle\rho\_{g,\phi,\alpha}((X-x)^{+})+x=\inf\Big\{a>x:\int\_{0}^{1}\phi\Big(\frac{(F\_{X}^{-1}(1-u)-x)^{+}}{a-x}\Big)\mathrm{d}g(u)\leq 1-\alpha\Big\}. |  |

Thus the definitions coincide for X∈L∞X\in L^{\infty} if gg is continuously differentiable with g​(0)=0g(0)=0, see Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c).

###### Remark 5.24.

Let us convince ourselves that the distortion Haezendonck-Goovaerts risk measures are well defined. First, let X∈LgϕX\in L\_{g}^{\phi} and x∈ℝx\in\mathbb{R}. By a property of quantile functions and the convexity of ϕ\phi we have, for any a>0a>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(F(X−x)+−1​(1−u)a+1)​dg​(u)\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{(X-x)^{+}}^{-1}(1-u)}{a+1}\Big)\mathrm{d}g(u) | =∫01ϕ​((FX−1​(1−u)−x)+a+1)​dg​(u)\displaystyle=\int\_{0}^{1}\phi\Big(\frac{(F\_{X}^{-1}(1-u)-x)^{+}}{a+1}\Big)\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫01ϕ​((|FX−1​(1−u)|+|x|)a+1)​dg​(u)\displaystyle\leq\int\_{0}^{1}\phi\Big(\frac{(|F\_{X}^{-1}(1-u)|+|x|)}{a+1}\Big)\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤aa+1​∫01ϕ​(|FX−1​(1−u)|a)​dg​(u)+1a+1​ϕ​(|x|),\displaystyle\leq\frac{a}{a+1}\int\_{0}^{1}\phi\Big(\frac{|F\_{X}^{-1}(1-u)|}{a}\Big)\mathrm{d}g(u)+\frac{1}{a+1}\phi(|x|), |  |

which shows that (X−x)+∈(Lgϕ)+(X-x)^{+}\in(L\_{g}^{\phi})\_{+}, so that πg,ϕ,α\pi\_{g,\phi,\alpha} can be applied. This argument is valid for any Young function ϕ\phi and any α<1\alpha<1.

Secondly, if ϕ\phi is normalized and α∈[0,1)\alpha\in[0,1) then ϕ−1​(1−α)≤1\phi^{-1}(1-\alpha)\leq 1. Thus it follows with Proposition [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a) that, for any x∈ℝx\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,α​((X−x)+)+x≥ρg​((X−x)+)ϕ−1​(1−α)+x≥ρg​((X−x)+)+x≥ρg​(X−x)+x=ρg​(X),\begin{split}\pi\_{g,\phi,\alpha}((X-x)^{+})+x&\geq\frac{\rho\_{g}((X-x)^{+})}{\phi^{-1}(1-\alpha)}+x\geq\rho\_{g}((X-x)^{+})+x\\ &\geq\rho\_{g}(X-x)+x=\rho\_{g}(X),\end{split} |  | (5.5) |

where we have used that ρg\rho\_{g} is cash-invariant and monotonic. Thus ρg,ϕ,α​(X)∈ℝ\rho\_{g,\phi,\alpha}(X)\in\mathbb{R}, as required from a risk measure.

###### Example 5.25.

(a) If ϕ\phi is the identity and α=0\alpha=0, then, for X∈Lgϕ=LgX\in L\_{g}^{\phi}=L\_{g}, πg,ϕ,0​((X−x)+)+x=ρg​((X−x)+)+x=∫01((FX−1​(1−u)−x)++x)​dg​(u)\pi\_{g,\phi,0}((X-x)^{+})+x=\rho\_{g}((X-x)^{+})+x=\int\_{0}^{1}((F\_{X}^{-1}(1-u)-x)^{+}+x)\mathrm{d}g(u) decreases as xx decreases. Thus, by the dominated convergence theorem, ρg,ϕ,0​(X)=ρg​(X)\rho\_{g,\phi,0}(X)=\rho\_{g}(X). This will be considerably generalized in Corollary [5.48](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem48 "Corollary 5.48. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below.

(b) Let α∈[0,1)\alpha\in[0,1). If gg is the identity function then ρg,ϕ,α​(X)=ρϕ,α​(X)\rho\_{g,\phi,\alpha}(X)=\rho\_{\phi,\alpha}(X) for all X∈Lgϕ=LϕX\in L\_{g}^{\phi}=L^{\phi}.

(c) Let α∈[0,1)\alpha\in[0,1) and β∈(0,1)\beta\in(0,1). If g​(u)=𝟙[1−β,1]​(u)g(u)=\mathds{1}\_{[1-\beta,1]}(u), then πg,ϕ,α​(X)=VaRβ​(X)ϕ−1​(1−α)\pi\_{g,\phi,\alpha}(X)=\frac{\mathrm{VaR}\_{\beta}(X)}{\phi^{-1}(1-\alpha)} for all risks X≥0X\geq 0. Since VaRβ​((X−x)+)=(VaRβ​(X)−x)+\mathrm{VaR}\_{\beta}((X-x)^{+})=(\mathrm{VaR}\_{\beta}(X)-x)^{+}, we obtain that ρg,ϕ,α​(X)=VaRβ​(X)\rho\_{g,\phi,\alpha}(X)=\mathrm{VaR}\_{\beta}(X) for any risk XX, independently of α\alpha.

### 5.7. Distortion HG: Convex cone

From Example [3.9](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem9 "Example 3.9. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we know that the set LgϕL\_{g}^{\phi} of risks is not necessarily a convex cone, even if gg is concave. On the other hand, if gg is the identity then Lgϕ=LϕL\_{g}^{\phi}=L^{\phi} is (even) a vector space. By Theorem [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we have that (Lgϕ)+(L\_{g}^{\phi})\_{+} is a convex cone whenever gg is concave. This remains true for LgϕL\_{g}^{\phi} under additional assumptions on gg.

###### Proposition 5.26.

If gg is concave and constant on some interval [u0,1][u\_{0},1], u0∈[0,1)u\_{0}\in[0,1), then LgϕL\_{g}^{\phi} is a convex cone.

###### Proof.

We first claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | X∈Lgϕ⟺X+∈(Lgϕ)+.X\in L\_{g}^{\phi}\Longleftrightarrow X^{+}\in(L\_{g}^{\phi})\_{+}. |  | (5.6) |

To see this, let u1=P​(X>0)u\_{1}=P(X>0). Then FX−1​(1−u)>0F\_{X}^{-1}(1-u)>0 for u<u1u<u\_{1} and FX−1​(1−u)≤0F\_{X}^{-1}(1-u)\leq 0 for u≥u1u\geq u\_{1}. If u1=1u\_{1}=1, X≥0X\geq 0, and the claim holds. Otherwise, we can assume that u1≤u0u\_{1}\leq u\_{0}. Then, for any a>0a>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ(|FX−1​(1−u)|a)dg(u)=∫[0,u1)ϕ(\displaystyle\int\_{0}^{1}\phi\Big(\frac{|F\_{X}^{-1}(1-u)|}{a}\Big)\mathrm{d}g(u)=\int\_{[0,u\_{1})}\phi\Big( | FX−1​(1−u)a)dg(u)+∫[u1,u0]ϕ(−FX−1​(1−u)a)dg(u)\displaystyle\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)+\int\_{[u\_{1},u\_{0}]}\phi\Big(\frac{-F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫(u0,1]ϕ​(−FX−1​(1−u)a)​dg​(u).\displaystyle+\int\_{(u\_{0},1]}\phi\Big(\frac{-F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u). |  | (5.7) |

Here, the second term on the right is finite, and the third term vanishes by hypothesis.

Since FX+−1=(FX−1)+F\_{X^{+}}^{-1}=(F\_{X}^{-1})^{+}, we have by the same argument that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(FX+−1​(1−u)a)​dg​(u)=∫[0,u1)ϕ​(FX−1​(1−u)a)​dg​(u).\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{X^{+}}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u)=\int\_{[0,u\_{1})}\phi\Big(\frac{F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u). |  | (5.8) |

Thus ∫01ϕ​(|FX−1​(1−u)|a)​dg​(u)<∞\int\_{0}^{1}\phi\big(\frac{|F\_{X}^{-1}(1-u)|}{a}\big)\mathrm{d}g(u)<\infty if and only if
∫01ϕ​(FX+−1​(1−u)a)​dg​(u)<∞\int\_{0}^{1}\phi\big(\frac{F\_{X^{+}}^{-1}(1-u)}{a}\big)\mathrm{d}g(u)<\infty, which proves the claim.

Let us now show that LgϕL\_{g}^{\phi} is a convex cone. Since it is invariant under positive scalar multiplication, we need to show that it is invariant under taking sums. Thus let X,Y∈LgϕX,Y\in L\_{g}^{\phi}. By ([5.6](https://arxiv.org/html/2512.03267v1#S5.E6 "In 5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), X+,Y+∈(Lgϕ)+X^{+},Y^{+}\in(L\_{g}^{\phi})\_{+}, hence X++Y+∈(Lgϕ)+X^{+}+Y^{+}\in(L\_{g}^{\phi})\_{+} by Theorem [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). Since (X+Y)+≤X++Y+(X+Y)^{+}\leq X^{+}+Y^{+}, also (X+Y)+∈(Lgϕ)+(X+Y)^{+}\in(L\_{g}^{\phi})\_{+} by Proposition [3.8](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), and hence X+Y∈LgϕX+Y\in L\_{g}^{\phi} by ([5.6](https://arxiv.org/html/2512.03267v1#S5.E6 "In 5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) again.
∎

###### Proposition 5.27.

If gg is concave with g′​(1)>0g^{\prime}(1)>0, then LgϕL\_{g}^{\phi} is a convex cone.

###### Proof.

We first claim that

|  |  |  |
| --- | --- | --- |
|  | X∈Lgϕ⟺X+∈(Lgϕ)+​ and ​X−∈Lϕ.X\in L\_{g}^{\phi}\Longleftrightarrow X^{+}\in(L\_{g}^{\phi})\_{+}\text{ and }X^{-}\in L^{\phi}. |  |

To see this, we first note that, since gg is concave, it is almost everywhere differentiable, and it is (left-)differentiable at 11 with g′​(1)≥0g^{\prime}(1)\geq 0. We assume then that g′​(1)>0g^{\prime}(1)>0. Let again u1=P​(X>0)u\_{1}=P(X>0), where we can once more assume that u1<1u\_{1}<1. Choose any u0∈(u1,1)u\_{0}\in(u\_{1},1) where g′g^{\prime} is differentiable. We then have again ([5.7](https://arxiv.org/html/2512.03267v1#S5.Ex55 "5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) and ([5.8](https://arxiv.org/html/2512.03267v1#S5.E8 "In 5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")).

This time, concerning the third term on the right of ([5.7](https://arxiv.org/html/2512.03267v1#S5.Ex55 "5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), we have for u0≤u≤1u\_{0}\leq u\leq 1 that c≤g′​(u)≤dc\leq g^{\prime}(u)\leq d almost everywhere, where d:=g′​(u0)d:=g^{\prime}(u\_{0}) and c:=g′​(1)>0c:=g^{\prime}(1)>0. Noting that d​g​(u)=g′​(u)​d​u\mathrm{d}g(u)=g^{\prime}(u)\mathrm{d}u on [u0,1][u\_{0},1], we thus see that the third term is finite if and only if
∫u01ϕ​(−FX−1​(1−u)a)​du\int\_{u\_{0}}^{1}\phi\big(\frac{-F\_{X}^{-1}(1-u)}{a}\big)\mathrm{d}u is finite, hence if and only if

|  |  |  |
| --- | --- | --- |
|  | ∫u11ϕ​(−FX−1​(1−u)a)​du=∫01ϕ​(|F−X−−1​(1−u)|a)​du=E​(ϕ​(|X−|a))\displaystyle\int\_{u\_{1}}^{1}\phi\Big(\frac{-F\_{X}^{-1}(1-u)}{a}\Big)\mathrm{d}u=\int\_{0}^{1}\phi\Big(\frac{|F\_{-X^{-}}^{-1}(1-u)|}{a}\Big)\mathrm{d}u=E\Big(\phi\Big(\frac{|X^{-}|}{a}\Big)\Big) |  |

is finite.

Altogether we have that ∫01ϕ​(|FX−1​(1−u)|a)​dg​(u)<∞\int\_{0}^{1}\phi\big(\frac{|F\_{X}^{-1}(1-u)|}{a}\big)\mathrm{d}g(u)<\infty if and only if
∫01ϕ​(FX+−1​(1−u)a)​dg​(u)<∞\int\_{0}^{1}\phi\big(\frac{F\_{X^{+}}^{-1}(1-u)}{a}\big)\mathrm{d}g(u)<\infty and E​(ϕ​(|X−|a))<∞E\big(\phi\big(\frac{|X^{-}|}{a}\big)\big)<\infty, which proves the claim.

From here, the proof can be finished as that of Proposition [5.26](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem26 "Proposition 5.26. ‣ 5.7. Distortion HG: Convex cone ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), using that (Lgϕ)+(L^{\phi}\_{g})\_{+} and LϕL^{\phi} are convex cones.
∎

### 5.8. Distortion HG: the infimum

The definition of the distortion Haezendock-Goovaerts risk measure as an infimum raises again the question whether it is, in fact, a minimum. If α≠0\alpha\neq 0, this is indeed the case, and we give conditions under which the minimum is unique. We first show the following, which is valid for any Young function and any α<1\alpha<1.

###### Proposition 5.28.

Let ϕ\phi be a Young function, α<1\alpha<1, and X∈LgϕX\in L\_{g}^{\phi}.

*(a)* Then the mapping x↦πg,ϕ,α​((X−x)+)x\mapsto\pi\_{g,\phi,\alpha}((X-x)^{+}) is convex on ℝ\mathbb{R}.

*(b)* Let gg be continuous, g​(0)=0g(0)=0, g>0g>0 on (0,1](0,1], and let ϕ\phi be strictly convex and satisfy the Δ2\Delta\_{2}-condition. If P​(X=ess​sup​X)=0P(X=\mathrm{ess\,sup\,}X)=0 then x↦πg,ϕ,α​((X−x)+)+xx\mapsto\pi\_{g,\phi,\alpha}((X-x)^{+})+x is strictly convex for x<ess​sup​Xx<\mathrm{ess\,sup\,}X.

###### Proof.

(a) Note that the functions z↦(z−x)+z\mapsto(z-x)^{+} are convex and increasing on ℝ\mathbb{R} for any x∈ℝx\in\mathbb{R}.

Now let x,y∈ℝx,y\in\mathbb{R} and 0≤λ≤10\leq\lambda\leq 1. It follows that the risks λ​(X−x)+\lambda(X-x)^{+} and (1−λ)​(X−y)+(1-\lambda)(X-y)^{+} are comonotonic. Propositions [5.13](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem13 "Proposition 5.13. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") then imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,α​((X−(λ​x+(1−λ)​y))+)\displaystyle\pi\_{g,\phi,\alpha}((X-(\lambda x+(1-\lambda)y))^{+}) | =πg,ϕ,α​((λ​(X−x)+(1−λ)​(X−y))+)\displaystyle=\pi\_{g,\phi,\alpha}((\lambda(X-x)+(1-\lambda)(X-y))^{+}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤πg,ϕ,α​(λ​(X−x)++(1−λ)​(X−y)+)\displaystyle\leq\pi\_{g,\phi,\alpha}(\lambda(X-x)^{+}+(1-\lambda)(X-y)^{+}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤πg,ϕ,α​(λ​(X−x)+)+πg,ϕ,α​((1−λ)​(X−y)+)\displaystyle\leq\pi\_{g,\phi,\alpha}(\lambda(X-x)^{+})+\pi\_{g,\phi,\alpha}((1-\lambda)(X-y)^{+}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​πg,ϕ,α​((X−x)+)+(1−λ)​πg,ϕ,α​((X−y)+),\displaystyle=\lambda\pi\_{g,\phi,\alpha}((X-x)^{+})+(1-\lambda)\pi\_{g,\phi,\alpha}((X-y)^{+}), |  |

which had to be shown.

(b) Let ψ=11−α​ϕ\psi=\frac{1}{1-\alpha}\phi and μg\mu\_{g} the measure induced by gg, see the discussion after Definition [3.1](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). Then, for any Y∈(Lgϕ)+Y\in(L\_{g}^{\phi})\_{+},

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α(Y)=∥FY−1(1−⋅)∥,\pi\_{g,\phi,\alpha}(Y)=\|F\_{Y}^{-1}(1-\cdot)\|, |  |

where ∥⋅∥\|\cdot\| is the Luxemburg norm in the Orlicz space Lψ​([0,1],ℬ​[0,1],μg)L^{\psi}([0,1],\mathcal{B}[0,1],\mu\_{g}), see [[10](https://arxiv.org/html/2512.03267v1#bib.bib10)], [[19](https://arxiv.org/html/2512.03267v1#bib.bib19)], [[45](https://arxiv.org/html/2512.03267v1#bib.bib45), p. 54]. Since gg is continuous with g​(0)=0g(0)=0, the measure μg\mu\_{g} is atomless. Thus, under the stated additional assumptions, the above Luxemburg norm is rotund, see [[45](https://arxiv.org/html/2512.03267v1#bib.bib45), Section 7.1, Corollary 5], that is, for Y1,Y2∈LψY\_{1},Y\_{2}\in L^{\psi} not collinear and 0<λ<10<\lambda<1, ‖λ​Y1+(1−λ)​Y2‖<λ​‖Y1‖+(1−λ)​‖Y2‖\|\lambda Y\_{1}+(1-\lambda)Y\_{2}\|<\lambda\|Y\_{1}\|+(1-\lambda)\|Y\_{2}\|, see [[40](https://arxiv.org/html/2512.03267v1#bib.bib40), Proposition 5.1.11].

Now, let x1<x2<ess​sup​Xx\_{1}<x\_{2}<\mathrm{ess\,sup\,}X. Then F(X−x1)+−1(1−⋅)=(FX−1−x1)+(1−⋅)F\_{(X-x\_{1})^{+}}^{-1}(1-\cdot)=(F\_{X}^{-1}-x\_{1})^{+}(1-\cdot) and F(X−x2)+−1(1−⋅)=(FX−1−x2)+(1−⋅)F\_{(X-x\_{2})^{+}}^{-1}(1-\cdot)=(F\_{X}^{-1}-x\_{2})^{+}(1-\cdot) are not collinear. Otherwise there were a,b∈ℝa,b\in\mathbb{R} not both zero such that a(FX−1−x1)+(1−⋅)=b(FX−1−x2)+(1−⋅)a(F\_{X}^{-1}-x\_{1})^{+}(1-\cdot)=b(F\_{X}^{-1}-x\_{2})^{+}(1-\cdot) μg\mu\_{g}-almost everywhere. Let p=FX​(x2)p=F\_{X}(x\_{2}). Since x2<ess​sup​Xx\_{2}<\mathrm{ess\,sup\,}X, we have that p<1p<1 and FX−1​(1−u)>x2F\_{X}^{-1}(1-u)>x\_{2} for 0≤u<1−p0\leq u<1-p. Thus a​(FX−1−x1)​(1−u)=b​(FX−1−x2)​(1−u)a(F\_{X}^{-1}-x\_{1})(1-u)=b(F\_{X}^{-1}-x\_{2})(1-u) for μg\mu\_{g}-almost every u∈[0,1−p)u\in[0,1-p). By hypothesis, μg​([0,q))>0\mu\_{g}([0,q))>0 for all q>0q>0. Note that a≠ba\neq b because otherwise μg​(x1=x2)≥μg​([0,1−p))>0\mu\_{g}(x\_{1}=x\_{2})\geq\mu\_{g}([0,1-p))>0. Hence there is some c∈ℝc\in\mathbb{R} such that FX−1​(1−u)=cF\_{X}^{-1}(1-u)=c for μg\mu\_{g}-almost every u∈[0,1−p)u\in[0,1-p); since u↦FX−1​(1−u)u\mapsto F\_{X}^{-1}(1-u) is decreasing, we deduce that there is some u0>0u\_{0}>0 such that
FX−1​(1−u)=cF\_{X}^{-1}(1-u)=c for 0≤u≤u00\leq u\leq u\_{0}, which implies that c=ess​sup​Xc=\mathrm{ess\,sup\,}X and P​(X=c)>0P(X=c)>0, contradicting the hypothesis.

Now, using the convexity of the functions z↦(z−x)+z\mapsto(z-x)^{+}, Proposition [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), and the comonotonic additivity of VaR, we have for 0<λ<10<\lambda<1 that

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,α​((X−(λ​x1+(1−λ)​x2))+)\displaystyle\pi\_{g,\phi,\alpha}((X-(\lambda x\_{1}+(1-\lambda)x\_{2}))^{+}) | ≤πg,ϕ,α​(λ​(X−x1)++(1−λ)​(X−x2)+)\displaystyle\leq\pi\_{g,\phi,\alpha}(\lambda(X-x\_{1})^{+}+(1-\lambda)(X-x\_{2})^{+}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∥Fλ​(X−x1)++(1−λ)​(X−x2)+−1(1−⋅)∥\displaystyle=\|F^{-1}\_{\lambda(X-x\_{1})^{+}+(1-\lambda)(X-x\_{2})^{+}}(1-\cdot)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∥λF(X−x1)+−1(1−⋅)+(1−λ)F(X−x2)+−1(1−⋅)∥\displaystyle=\|\lambda F^{-1}\_{(X-x\_{1})^{+}}(1-\cdot)+(1-\lambda)F^{-1}\_{(X-x\_{2})^{+}}(1-\cdot)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <λ∥F(X−x1)+−1(1−⋅)∥+(1−λ)∥F(X−x2)+−1(1−⋅)∥\displaystyle<\lambda\|F^{-1}\_{(X-x\_{1})^{+}}(1-\cdot)\|+(1-\lambda)\|F^{-1}\_{(X-x\_{2})^{+}}(1-\cdot)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​πg,ϕ,α​((X−x1)+)+(1−λ)​πϕ,α​((X−x2)+),\displaystyle=\lambda\pi\_{g,\phi,\alpha}((X-x\_{1})^{+})+(1-\lambda)\pi\_{\phi,\alpha}((X-x\_{2})^{+}), |  |

so that x↦πg,ϕ,α​((X−x)+)+xx\mapsto\pi\_{g,\phi,\alpha}((X-x)^{+})+x is strictly convex for x<ess​sup​Xx<\mathrm{ess\,sup\,}X.
∎

###### Example 5.29.

Let gg be the identity, ϕ​(t)=t2\phi(t)=t^{2}, and α<1\alpha<1. If P​(X=0)=P​(X=1)=12P(X=0)=P(X=1)=\frac{1}{2}, then πg,ϕ,α​((X−x)+)+x=12​(1−α)​(1−x)+x\pi\_{g,\phi,\alpha}((X-x)^{+})+x=\frac{1}{\sqrt{2(1-\alpha)}}(1-x)+x for 0<x<10<x<1, which is not strictly convex. Thus, part (b) of the proposition may fail if P​(X=ess​sup​X)>0P(X=\mathrm{ess\,sup\,}X)>0; the example also contradicts [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 11(f)] and [[7](https://arxiv.org/html/2512.03267v1#bib.bib7), Proposition 3(c)].

Part (a) of the proposition implies that the minimum in the definition of the distortion Haezendonck-Goovaerts risk measure is attained if α≠0\alpha\neq 0.

###### Proposition 5.30.

Let 0<α<10<\alpha<1 and X∈LgϕX\in L\_{g}^{\phi}.

*(a)* Then

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​(X)=minx∈ℝ⁡(πg,ϕ,α​((X−x)+)+x).\rho\_{g,\phi,\alpha}(X)=\min\_{x\in\mathbb{R}}\big(\pi\_{g,\phi,\alpha}((X-x)^{+})+x\big). |  |

*(b)* Let gg be continuous, g​(0)=0g(0)=0, g>0g>0 on (0,1](0,1], and let ϕ\phi be strictly convex and satisfy the Δ2\Delta\_{2}-condition. If P​(X=ess​sup​X)=0P(X=\mathrm{ess\,sup\,}X)=0 then there is a unique value x∈ℝx\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​(X)=πg,ϕ,α​((X−x)+)+x.\rho\_{g,\phi,\alpha}(X)=\pi\_{g,\phi,\alpha}((X-x)^{+})+x. |  |

###### Proof.

(a) We follow the proof of [[7](https://arxiv.org/html/2512.03267v1#bib.bib7), Proposition 3(b)]. By Proposition [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a) we have, for any x∈ℝx\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​((X−x)+)+x≥ρg​((X−x)+)ϕ−1​(1−α)+x,\pi\_{g,\phi,\alpha}((X-x)^{+})+x\geq\frac{\rho\_{g}((X-x)^{+})}{\phi^{-1}(1-\alpha)}+x, |  |

and therefore by monotonicity and cash-invariance of ρg\rho\_{g},

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,α​((X−x)+)+x≥ρg​(X)−xϕ−1​(1−α)+x=ρg​(X)ϕ−1​(1−α)+x​(1−1ϕ−1​(1−α)).\pi\_{g,\phi,\alpha}((X-x)^{+})+x\geq\frac{\rho\_{g}(X)-x}{\phi^{-1}(1-\alpha)}+x=\frac{\rho\_{g}(X)}{\phi^{-1}(1-\alpha)}+x\Big(1-\frac{1}{\phi^{-1}(1-\alpha)}\Big). |  | (5.9) |

It follows from these two inequalities that the function x↦πg,ϕ,α​((X−x)+)+xx\mapsto\pi\_{g,\phi,\alpha}((X-x)^{+})+x tends to ∞\infty as x→±∞x\to\pm\infty; note that ϕ−1​(1−α)<1\phi^{-1}(1-\alpha)<1. Since the function is convex by Proposition [5.28](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem28 "Proposition 5.28. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a), the result follows.

(b) This is a direct consequence of part (a), Proposition [5.28](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem28 "Proposition 5.28. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), and the fact that πg,ϕ,α​((X−x)+)+x=x\pi\_{g,\phi,\alpha}((X-x)^{+})+x=x for x≥ess​sup​Xx\geq\mathrm{ess\,sup\,}X.
∎

###### Example 5.31.

A variant of Example [5.29](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem29 "Example 5.29. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") shows that part (b) of the proposition may fail for any α∈(0,1)\alpha\in(0,1), if P​(X=ess​sup​X)>0P(X=\mathrm{ess\,sup\,}X)>0. Indeed, if gg is the identity, ϕ​(t)=t2\phi(t)=t^{2}, P​(X=0)=αP(X=0)=\alpha, and P​(X=1)=1−αP(X=1)=1-\alpha, then πg,ϕ,α​((X−x)+)+x=1\pi\_{g,\phi,\alpha}((X-x)^{+})+x=1 for 0≤x≤10\leq x\leq 1, so that the minimum is not uniquely attained.

The proof of Proposition [5.30](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem30 "Proposition 5.30. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") also gives us some information on the location of a minimum.

###### Lemma 5.32.

Let 0<α<10<\alpha<1. Let Y1,Y2∈LgϕY\_{1},Y\_{2}\in L\_{g}^{\phi} and Y1≤X≤Y2Y\_{1}\leq X\leq Y\_{2}. If

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​(X)=πg,ϕ,α​((X−x)+)+x\rho\_{g,\phi,\alpha}(X)=\pi\_{g,\phi,\alpha}((X-x)^{+})+x |  |

then

|  |  |  |
| --- | --- | --- |
|  | ρg​(Y1)−ϕ−1​(1−α)​ρg,ϕ,α​(Y2)1−ϕ−1​(1−α)≤x≤ρg,ϕ,α​(Y2).\frac{\rho\_{g}(Y\_{1})-\phi^{-1}(1-\alpha)\rho\_{g,\phi,\alpha}(Y\_{2})}{1-\phi^{-1}(1-\alpha)}\leq x\leq\rho\_{g,\phi,\alpha}(Y\_{2}). |  |

###### Proof.

First note that, by Proposition [5.3](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), X∈LgϕX\in L\_{g}^{\phi}. The right-hand inequality is clear by positivity of πg,ϕ,α\pi\_{g,\phi,\alpha} and monotonicity of ρg,ϕ,α\rho\_{g,\phi,\alpha}. Next, by ([5.9](https://arxiv.org/html/2512.03267v1#S5.E9 "In 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")),

|  |  |  |
| --- | --- | --- |
|  | x≥ρg​(X)ϕ−1​(1−α)−ρg,ϕ,α​(X)1ϕ−1​(1−α)−1,x\geq\frac{\frac{\rho\_{g}(X)}{\phi^{-1}(1-\alpha)}-\rho\_{g,\phi,\alpha}(X)}{\frac{1}{\phi^{-1}(1-\alpha)}-1}, |  |

which implies the left-hand inequality by the monotonicity of ρg\rho\_{g} and ρg,ϕ,α\rho\_{g,\phi,\alpha}.
∎

Of course, one obtains the best estimate if Y1=Y2=XY\_{1}=Y\_{2}=X, but it is in the above form that the lemma will be useful in the sequel.

For α=0\alpha=0, the situation is quite different.

###### Proposition 5.33.

Let α=0\alpha=0 and X∈LgϕX\in L\_{g}^{\phi}.

*(a)* Then x↦πg,ϕ,0​((X−x)+)+xx\mapsto\pi\_{g,\phi,0}((X-x)^{+})+x is increasing on ℝ\mathbb{R}. In particular,

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,0​(X)=limx→−∞(πg,ϕ,0​((X−x)+)+x).\rho\_{g,\phi,0}(X)=\lim\_{x\to-\infty}\big(\pi\_{g,\phi,0}((X-x)^{+})+x\big). |  |

*(b)* Let gg be continuous, g​(0)=0g(0)=0, g>0g>0 on (0,1](0,1], and let ϕ\phi be strictly convex and satisfy the Δ2\Delta\_{2}-condition. If P​(X=ess​sup​X)=0P(X=\mathrm{ess\,sup\,}X)=0 then x↦πg,ϕ,0​((X−x)+)+xx\mapsto\pi\_{g,\phi,0}((X-x)^{+})+x is strictly increasing on ℝ\mathbb{R}. In particular, the function does not attain its infimum.

###### Proof.

(a) Let x1<x2x\_{1}<x\_{2}. Using Proposition [5.13](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem13 "Proposition 5.13. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), applied to the comonotonic risks (X−x1)+−(X−x2)+(X-x\_{1})^{+}-(X-x\_{2})^{+} and (X−x2)+(X-x\_{2})^{+}, the fact that (x−x1)+−(x−x2)+≤x2−x1(x-x\_{1})^{+}-(x-x\_{2})^{+}\leq x\_{2}-x\_{1} for all x∈ℝx\in\mathbb{R}, and Propositions [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,0​((X−x1)+)\displaystyle\pi\_{g,\phi,0}((X-x\_{1})^{+}) | =πg,ϕ,0​((X−x1)+−(X−x2)++(X−x2)+)\displaystyle=\pi\_{g,\phi,0}((X-x\_{1})^{+}-(X-x\_{2})^{+}+(X-x\_{2})^{+}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤πg,ϕ,0​((X−x1)+−(X−x2)+)+πg,ϕ,0​((X−x2)+)\displaystyle\leq\pi\_{g,\phi,0}((X-x\_{1})^{+}-(X-x\_{2})^{+})+\pi\_{g,\phi,0}((X-x\_{2})^{+}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤x2−x1+πg,ϕ,0​((X−x2)+),\displaystyle\leq x\_{2}-x\_{1}+\pi\_{g,\phi,0}((X-x\_{2})^{+}), |  |

which implies the claim.

(b) This is a direct consequence of part (a), Proposition [5.28](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem28 "Proposition 5.28. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), and the fact that πg,ϕ,0​((X−x)+)+x=x\pi\_{g,\phi,0}((X-x)^{+})+x=x for x≥ess​sup​Xx\geq\mathrm{ess\,sup\,}X.
∎

As in the undistorted case, for α=0\alpha=0 the distortion Haezendonck-Goovaerts risk measure often reduces to the corresponding distortion risk measure. Since we first need some more knowledge about these risk measures, we postpone the discussion, see Theorem [5.47](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem47 "Theorem 5.47. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") below.

### 5.9. Distortion HG: risk theoretic properties

We collect several important properties of the distortion Haezendonck-Goovaerts risk measures.

###### Proposition 5.34.

Let X∈LgϕX\in L\_{g}^{\phi}. Then:

1. *(a)*

   ρg,ϕ,α​(X)≤πg,ϕ,α​(X+)\rho\_{g,\phi,\alpha}(X)\leq\pi\_{g,\phi,\alpha}(X^{+}).
2. *(b)*

   ρg​(X)≤ρg,ϕ,α​(X)≤ess​sup​X\rho\_{g}(X)\leq\rho\_{g,\phi,\alpha}(X)\leq\mathrm{ess\,sup\,}X.

Suppose, in addition, that g:[0,1]→[0,1]g:[0,1]\to[0,1] is bijective, and let α≠0\alpha\neq 0. Then:

1. *(c)*

   ρg,ϕ,α​(X)≥VaR1−g−1​(1−α)​(X)\rho\_{g,\phi,\alpha}(X)\geq\mathrm{VaR}\_{1-g^{-1}(1-\alpha)}(X).

###### Proof.

(a) is obvious by taking x=0x=0 in the definition of ρg,ϕ,α\rho\_{g,\phi,\alpha}.

(b) The first inequality follows form ([5.5](https://arxiv.org/html/2512.03267v1#S5.E5 "In Remark 5.24. ‣ 5.6. Distortion Haezendonck-Goovaerts risk measures ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) by definition of ρg,ϕ,α\rho\_{g,\phi,\alpha}. The second inequality is trivial if ess​sup​X=∞\mathrm{ess\,sup\,}X=\infty; otherwise it follows by taking x=ess​sup​Xx=\mathrm{ess\,sup\,}X in the definition of ρg,ϕ,α\rho\_{g,\phi,\alpha}.

(c) We note that, for any a>0a>0 and b∈ℝb\in\mathbb{R}, 𝟙{b>a}≤ϕ​(b+a)\mathds{1}\_{\{b>a\}}\leq\phi\big(\frac{b^{+}}{a}\big). Thus, for any a>0a>0 and x∈ℝx\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01ϕ​(F(X−x)+−1​(1−u)a)​dg​(u)\displaystyle\int\_{0}^{1}\phi\Big(\frac{F\_{(X-x)^{+}}^{-1}(1-u)}{a}\Big)\mathrm{d}g(u) | =∫01ϕ​((FX−1​(1−u)−x)+a)​dg​(u)\displaystyle=\int\_{0}^{1}\phi\Big(\frac{(F\_{X}^{-1}(1-u)-x)^{+}}{a}\Big)\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥∫01𝟙{FX−1​(1−u)−x>a}​dg​(u)=∫01𝟙{u<1−FX​(a+x)}​dg​(u)\displaystyle\geq\int\_{0}^{1}\mathds{1}\_{\{F\_{X}^{-1}(1-u)-x>a\}}\mathrm{d}g(u)=\int\_{0}^{1}\mathds{1}\_{\{u<1-F\_{X}(a+x)\}}\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =g​(1−FX​(x+a)),\displaystyle=g(1-F\_{X}(x+a)), |  |

where we have applied properties of quantile functions; note also that gg is necessarily continuous with g​(0)=0g(0)=0. Hence πg,ϕ,α​((X−x)+)≥inf{a:g​(1−FX​(a+x))≤1−α}=inf{a:FX​(a+x)≥1−g−1​(1−α)}=VaR1−g−1​(1−α)​(X)−x\pi\_{g,\phi,\alpha}((X-x)^{+})\geq\inf\{a:g(1-F\_{X}(a+x))\leq 1-\alpha\}=\inf\{a:F\_{X}(a+x)\geq 1-g^{-1}(1-\alpha)\}=\mathrm{VaR}\_{1-g^{-1}(1-\alpha)}(X)-x. The definition of ρg,ϕ,α\rho\_{g,\phi,\alpha} then yields the claim.
∎

###### Proposition 5.35.

The distortion Haezendonck-Goovaerts risk measure ρg,ϕ,α\rho\_{g,\phi,\alpha} is monotonic, cash-invariant and positively homogeneous on LgϕL\_{g}^{\phi}.

###### Proof.

Cash-invariance follows from the identity

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​((X+b−x)+)+x=πg,ϕ,α​((X−(x−b))+)+(x−b)+b.\displaystyle\pi\_{g,\phi,\alpha}((X+b-x)^{+})+x=\pi\_{g,\phi,\alpha}((X-(x-b))^{+})+(x-b)+b. |  |

Monotonicity passes from πg,ϕ,α\pi\_{g,\phi,\alpha} to ρg,ϕ,α\rho\_{g,\phi,\alpha} since (X−x)+≤(Y−x)+(X-x)^{+}\leq(Y-x)^{+} if X≤YX\leq Y. Positive homogeneity for λ>0\lambda>0 follows from the identity

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​((λ​X−x)+)+x=λ​(πg,ϕ,α​((X−xλ)+)+xλ).\pi\_{g,\phi,\alpha}((\lambda X-x)^{+})+x=\lambda\big(\pi\_{g,\phi,\alpha}((X-\tfrac{x}{\lambda})^{+})+\tfrac{x}{\lambda}\big). |  |

For λ=0\lambda=0 we note that πg,ϕ,α​((0−0)+)+0=0\pi\_{g,\phi,\alpha}((0-0)^{+})+0=0, πg,ϕ,α​((0−x)+)+x≥0\pi\_{g,\phi,\alpha}((0-x)^{+})+x\geq 0 if x>0x>0, and πg,ϕ,α​((0−x)+)+x=πg,ϕ,α​(−x)+x=(−x)​πg,ϕ,α​(1)+x≥0\pi\_{g,\phi,\alpha}((0-x)^{+})+x=\pi\_{g,\phi,\alpha}(-x)+x=(-x)\pi\_{g,\phi,\alpha}(1)+x\geq 0 if x<0x<0, where we have used the positive homogeneity of πg,ϕ,α\pi\_{g,\phi,\alpha} and that πg,ϕ,α​(1)≥1\pi\_{g,\phi,\alpha}(1)\geq 1 by Proposition [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b). Thus, ρg,ϕ,α​(0)=0\rho\_{g,\phi,\alpha}(0)=0.
∎

The distortion Haezendonck-Goovaerts risk measures are subadditive for comonotonic risks.

###### Proposition 5.36.

Let X,Y∈LgϕX,Y\in L\_{g}^{\phi} be comonotonic risks. Then X+Y∈LgϕX+Y\in L\_{g}^{\phi} and

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,α​(X+Y)≤ρg,ϕ,α​(X)+ρg,ϕ,α​(Y).\rho\_{g,\phi,\alpha}(X+Y)\leq\rho\_{g,\phi,\alpha}(X)+\rho\_{g,\phi,\alpha}(Y). |  |

###### Proof.

Let X,Y∈LgϕX,Y\in L\_{g}^{\phi} be comonotonic. Since VaR is additive for comonotonic risks, we have that |FX+Y−1​(1−u)|≤|FX−1​(1−u)|+|FY−1​(1−u)||F\_{X+Y}^{-1}(1-u)|\leq|F\_{X}^{-1}(1-u)|+|F\_{Y}^{-1}(1-u)| for all u∈[0,1)u\in[0,1). Thus, by the argument in the proof of Proposition [5.13](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem13 "Proposition 5.13. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and using the monotonicity of ϕ\phi, we find that X+Y∈LgϕX+Y\in L\_{g}^{\phi}.

Next, let x,y∈ℝx,y\in\mathbb{R}. Since XX and YY are comonotonic, there is a random variable ZZ with values in an interval I⊂ℝI\subset\mathbb{R} and two increasing functions f1,f2:I→ℝf\_{1},f\_{2}:I\to\mathbb{R} such that (X,Y)(X,Y) and (f1​(Z),f2​(Z))(f\_{1}(Z),f\_{2}(Z)) have the same distribution. But then ((X−x)+,(Y−y)+)((X-x)^{+},(Y-y)^{+}) and ((f1​(Z)−x)+,(f2​(Z)−y)+)((f\_{1}(Z)-x)^{+},(f\_{2}(Z)-y)^{+}) have the same distribution, so that also (X−x)+(X-x)^{+} and (Y−y)+(Y-y)^{+} are comonotonic. Thus, by Proposition [5.13](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem13 "Proposition 5.13. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and the monotonicity of πg,ϕ,α\pi\_{g,\phi,\alpha}, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,ϕ,α​((X+Y−(x+y))+)+(x+y)\displaystyle\pi\_{g,\phi,\alpha}((X+Y-(x+y))^{+})+(x+y) | ≤πg,ϕ,α​((X−x)++(Y−y)+)+(x+y)\displaystyle\leq\pi\_{g,\phi,\alpha}((X-x)^{+}+(Y-y)^{+})+(x+y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤πg,ϕ,α​((X−x)+)+x+πg,ϕ,α​((Y−y)+)+y.\displaystyle\leq\pi\_{g,\phi,\alpha}((X-x)^{+})+x+\pi\_{g,\phi,\alpha}((Y-y)^{+})+y. |  |

Taking infima on both sides implies the claim.
∎

We turn to continuity properties. In the following results, some proofs require that α≠0\alpha\neq 0.

###### Proposition 5.37.

If 0<α<10<\alpha<1, then ρg,ϕ,α\rho\_{g,\phi,\alpha} has the Fatou property on LgϕL\_{g}^{\phi}.

###### Proof.

By Remark [2.4](https://arxiv.org/html/2512.03267v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) and Propositions [5.3](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.35](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem35 "Proposition 5.35. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") it suffices to show that if Xn↗XX\_{n}\nearrow X and X1,X∈LgϕX\_{1},X\in L\_{g}^{\phi} then ρg,ϕ,α​(X)≤lim supn→∞ρg,ϕ,α​(Xn)\rho\_{g,\phi,\alpha}(X)\leq\limsup\_{n\to\infty}\rho\_{g,\phi,\alpha}(X\_{n}).

For this, we use an idea of [[23](https://arxiv.org/html/2512.03267v1#bib.bib23)]. By Proposition [5.30](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem30 "Proposition 5.30. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), for any nn, there are xn∈ℝx\_{n}\in\mathbb{R} such that ρg,ϕ,α​(Xn)=πg,ϕ,α​((Xn−xn)+)+xn\rho\_{g,\phi,\alpha}(X\_{n})=\pi\_{g,\phi,\alpha}((X\_{n}-x\_{n})^{+})+x\_{n}. Since X1≤Xn≤XX\_{1}\leq X\_{n}\leq X for all nn, it follows from Lemma [5.32](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem32 "Lemma 5.32. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that the sequence (xn)n(x\_{n})\_{n} is bounded, hence has a convergent subsequence. We may then assume that the whole sequence converges, and we put x0=limn→∞xnx\_{0}=\lim\_{n\to\infty}x\_{n}. But then (Xn−xn)+→(X−x0)+(X\_{n}-x\_{n})^{+}\to(X-x\_{0})^{+} and 0≤(Xn−xn)+≤(X−infk|xk|)+∈(Lgϕ)+0\leq(X\_{n}-x\_{n})^{+}\leq(X-\inf\_{k}|x\_{k}|)^{+}\in(L\_{g}^{\phi})^{+} for all nn. Using Proposition [5.14](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem14 "Proposition 5.14. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), we then get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg,ϕ,α​(X)\displaystyle\rho\_{g,\phi,\alpha}(X) | ≤πg,ϕ,α​((X−x0)+)+x0≤lim infn→∞πg,ϕ,α​((Xn−xn)+)+x0\displaystyle\leq\pi\_{g,\phi,\alpha}((X-x\_{0})^{+})+x\_{0}\leq\liminf\_{n\to\infty}\pi\_{g,\phi,\alpha}((X\_{n}-x\_{n})^{+})+x\_{0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =lim infn→∞(πg,ϕ,α​((Xn−xn)+)+xn)=lim infn→∞ρg,ϕ,α​(Xn)=lim supn→∞ρg,ϕ,α​(Xn),\displaystyle=\liminf\_{n\to\infty}\big(\pi\_{g,\phi,\alpha}((X\_{n}-x\_{n})^{+})+x\_{n}\big)=\liminf\_{n\to\infty}\rho\_{g,\phi,\alpha}(X\_{n})=\limsup\_{n\to\infty}\rho\_{g,\phi,\alpha}(X\_{n}), |  |

as desired.
∎

For the reverse Fatou property, recall the Property (Pg,ϕP\_{g,\phi}) stated before Proposition [5.15](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem15 "Proposition 5.15. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Proposition 5.38.

Let α∈[0,1)\alpha\in[0,1). If *(Pg,ϕP\_{g,\phi})* holds, then ρg,ϕ,α\rho\_{g,\phi,\alpha} has the reverse Fatou property on LgϕL\_{g}^{\phi}.

###### Proof.

It suffices by Remark [2.4](https://arxiv.org/html/2512.03267v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2. Risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) and Propositions [5.3](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.35](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem35 "Proposition 5.35. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") to show that if Xn↘XX\_{n}\searrow X and X1,X∈LgϕX\_{1},X\in L\_{g}^{\phi} then ρg,ϕ,α​(X)≥infn≥1ρg,ϕ,α​(Xn)\rho\_{g,\phi,\alpha}(X)\geq\inf\_{n\geq 1}\rho\_{g,\phi,\alpha}(X\_{n}).

For this, we follow the proof of [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 17]. By Proposition [5.15](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem15 "Proposition 5.15. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") we have, for all x∈ℝx\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​((X−x)+)≥infn≥1πg,ϕ,α​((Xn−x)+).\pi\_{g,\phi,\alpha}((X-x)^{+})\geq\inf\_{n\geq 1}\pi\_{g,\phi,\alpha}((X\_{n}-x)^{+}). |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | infn≥1ρg,ϕ,α​(Xn)\displaystyle\inf\_{n\geq 1}\rho\_{g,\phi,\alpha}(X\_{n}) | =infn≥1infx∈ℝ(πg,ϕ,α​((Xn−x)+)+x)=infx∈ℝinfn≥1(πg,ϕ,α​((Xn−x)+)+x)\displaystyle=\inf\_{n\geq 1}\inf\_{x\in\mathbb{R}}(\pi\_{g,\phi,\alpha}((X\_{n}-x)^{+})+x)=\inf\_{x\in\mathbb{R}}\inf\_{n\geq 1}(\pi\_{g,\phi,\alpha}((X\_{n}-x)^{+})+x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤infx∈ℝ(πg,ϕ,α​((X−x)+)+x)=ρg,ϕ,α​(X),\displaystyle\leq\inf\_{x\in\mathbb{R}}(\pi\_{g,\phi,\alpha}((X-x)^{+})+x)=\rho\_{g,\phi,\alpha}(X), |  |

as desired.
∎

Using Proposition [5.16](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem16 "Proposition 5.16. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") instead of Proposition [5.15](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem15 "Proposition 5.15. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), we obtain in the same way a variant on L∞L^{\infty}.

###### Proposition 5.39.

Let α∈[0,1)\alpha\in[0,1). If g​(0)=0g(0)=0 and gg is continuous, then ρg,ϕ,α\rho\_{g,\phi,\alpha} has the reverse Fatou property on L∞L^{\infty}.

Unfortunately, we only have partial converses: we are not able to show that gg must be continuous if ρg,ϕ,α\rho\_{g,\phi,\alpha} has the reverse Fatou property. Using ideas from the proof of [[23](https://arxiv.org/html/2512.03267v1#bib.bib23), Proposition 3.4], we have the following.

###### Lemma 5.40.

Let 0<α<10<\alpha<1. If (Xn)n(X\_{n})\_{n} is a decreasing sequence in (Lgϕ)+(L\_{g}^{\phi})\_{+}, then ρg,ϕ,α​(Xn)→0\rho\_{g,\phi,\alpha}(X\_{n})\to 0 implies that πg,ϕ,α​(Xn)→0\pi\_{g,\phi,\alpha}(X\_{n})\to 0.

###### Proof.

Let us define σn​(x)=πg,ϕ,α​((Xn−x)+)+x\sigma\_{n}(x)=\pi\_{g,\phi,\alpha}((X\_{n}-x)^{+})+x, x∈ℝx\in\mathbb{R}. By Proposition [5.30](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem30 "Proposition 5.30. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), there are xn∈ℝx\_{n}\in\mathbb{R} such that ρg,ϕ,α​(Xn)=σn​(xn)\rho\_{g,\phi,\alpha}(X\_{n})=\sigma\_{n}(x\_{n}), n≥1n\geq 1. By Lemma [5.32](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem32 "Lemma 5.32. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), applied with Y1=0Y\_{1}=0 and Y2=XnY\_{2}=X\_{n}, ρg,ϕ,α​(Xn)→0\rho\_{g,\phi,\alpha}(X\_{n})\to 0 implies that xn→0x\_{n}\to 0.

Now, the functions σn\sigma\_{n} are convex by Proposition [5.28](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem28 "Proposition 5.28. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a). If xn>0x\_{n}>0, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤σn​(0)\displaystyle 0\leq\sigma\_{n}(0) | =σn​(11+xn​xn+xn1+xn​(−1))≤11+xn​σn​(xn)+xn1+xn​σn​(−1)\displaystyle=\sigma\_{n}(\tfrac{1}{1+x\_{n}}x\_{n}+\tfrac{x\_{n}}{1+x\_{n}}(-1))\leq\tfrac{1}{1+x\_{n}}\sigma\_{n}(x\_{n})+\tfrac{x\_{n}}{1+x\_{n}}\sigma\_{n}(-1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤11+xn​σn​(xn)+xn1+xn​σ1​(−1),\displaystyle\leq\tfrac{1}{1+x\_{n}}\sigma\_{n}(x\_{n})+\tfrac{x\_{n}}{1+x\_{n}}\sigma\_{1}(-1), |  |

where in the last line we have used the monotonicity of πg,ϕ,α\pi\_{g,\phi,\alpha}. In the same way, if xn<0x\_{n}<0, then

|  |  |  |
| --- | --- | --- |
|  | 0≤σn​(0)≤11−xn​σn​(xn)+−xn1−xn​σ1​(1).0\leq\sigma\_{n}(0)\leq\tfrac{1}{1-x\_{n}}\sigma\_{n}(x\_{n})+\tfrac{-x\_{n}}{1-x\_{n}}\sigma\_{1}(1). |  |

Since xn→0x\_{n}\to 0 and σn​(xn)→0\sigma\_{n}(x\_{n})\to 0, we have altogether that πg,ϕ,α​(Xn)=σn​(0)→0\pi\_{g,\phi,\alpha}(X\_{n})=\sigma\_{n}(0)\to 0.
∎

###### Proposition 5.41.

Let 0<α<10<\alpha<1. If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless and if ρg,ϕ,α\rho\_{g,\phi,\alpha} has the reverse Fatou property on LgϕL\_{g}^{\phi} then g​(0)=0g(0)=0, and if gg is continuous on some neighbourhood of 0 then either g=0g=0 on some neighbourhood of 0 or ϕ\phi satisfies the Δ2\Delta\_{2}-condition.

###### Proof.

We first show that g​(0)=0g(0)=0. To see this, let (An)n(A\_{n})\_{n} be a decreasing sequence of sets in 𝒜\mathcal{A} with P​(An)=1nP(A\_{n})=\frac{1}{n}; see the proof of Proposition [3.16](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem16 "Proposition 3.16. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). If Xn=𝟙AnX\_{n}=\mathds{1}\_{A\_{n}}, n≥1n\geq 1, then Xn↘0X\_{n}\searrow 0; also, Xn∈LgϕX\_{n}\in L\_{g}^{\phi} as bounded risks. By the reverse Fatou property, we have that ρg,ϕ,α​(Xn)→0\rho\_{g,\phi,\alpha}(X\_{n})\to 0. By Lemma [5.40](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem40 "Lemma 5.40. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), πg,ϕ,α​(Xn)→0\pi\_{g,\phi,\alpha}(X\_{n})\to 0. Now, a simple calculation shows that

|  |  |  |
| --- | --- | --- |
|  | πg,ϕ,α​(Xn)=1ϕ−1​(1−αg​(1n−)),\pi\_{g,\phi,\alpha}(X\_{n})=\frac{1}{\phi^{-1}\big(\frac{1-\alpha}{g(\frac{1}{n}-)}\big)}, |  |

see also the proof of Proposition [5.15](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem15 "Proposition 5.15. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). We then deduce that g​(0)=0g(0)=0.

Next suppose that gg is continuous on some neighbourhood of 0, g>0g>0 on (0,1](0,1], and that ϕ\phi does not satisfy the Δ2\Delta\_{2}-condition. Then, by Lemma [5.8](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem8 "Lemma 5.8. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), there are risks Xn∈(Lgϕ)+X\_{n}\in(L\_{g}^{\phi})\_{+} such that Xn↘0X\_{n}\searrow 0 with πg,ϕ,α​(Xn)≥12\pi\_{g,\phi,\alpha}(X\_{n})\geq\frac{1}{2} for all nn. It follows from Lemma [5.40](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem40 "Lemma 5.40. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that ρg,ϕ,α​(Xn)↛0\rho\_{g,\phi,\alpha}(X\_{n})\not\to 0, contradicting the reverse Fatou property.
∎

The above proof also gives a version on L∞L^{\infty}.

###### Proposition 5.42.

Let 0<α<10<\alpha<1. If the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless and if ρg,ϕ,α\rho\_{g,\phi,\alpha} has the reverse Fatou property on L∞L^{\infty} then g​(0)=0g(0)=0.

Proposition [5.17](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem17 "Proposition 5.17. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") easily implies the following. Indeed, X≤stYX\leq\_{\text{st}}Y implies that (X−x)+≤st(Y−x)+(X-x)^{+}\leq\_{\text{st}}(Y-x)^{+} for any xx; it suffices to note that F(X−x)+−1=(FX−1−x)+F^{-1}\_{(X-x)^{+}}=(F^{-1}\_{X}-x)^{+}.

###### Proposition 5.43.

Let α∈[0,1)\alpha\in[0,1) and X,Y∈LgϕX,Y\in L\_{g}^{\phi}. Then

|  |  |  |
| --- | --- | --- |
|  | X≤*st*Y⟹ρg,ϕ,α​(X)≤ρg,ϕ,α​(Y).X\leq\_{\emph{\text{st}}}Y\Longrightarrow\rho\_{g,\phi,\alpha}(X)\leq\rho\_{g,\phi,\alpha}(Y). |  |

### 5.10. Distortion HG: the concave case

First, Proposition [5.19](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem19 "Proposition 5.19. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") easily yields the following. It suffices to note that if φ\varphi is an increasing convex function, then so is z↦φ​((z−x)+)z\mapsto\varphi((z-x)^{+}), hence X≤slYX\leq\_{\text{sl}}Y implies that (X−x)+≤sl(Y−x)+(X-x)^{+}\leq\_{\text{sl}}(Y-x)^{+} for any xx.

###### Proposition 5.44.

Let gg be concave. If X,Y∈LgϕX,Y\in L\_{g}^{\phi}, then

|  |  |  |
| --- | --- | --- |
|  | X≤*sl*Y⟹ρg,ϕ,α​(X)≤ρg,ϕ,α​(Y).X\leq\_{\emph{\text{sl}}}Y\Longrightarrow\rho\_{g,\phi,\alpha}(X)\leq\rho\_{g,\phi,\alpha}(Y). |  |

We also need a variant of Lemma [5.20](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem20 "Lemma 5.20. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), which is proved quite similarly.

###### Lemma 5.45.

Suppose that the underlying probability space (Ω,𝒜,P)(\Omega,\mathcal{A},P) is atomless. Let 𝒳\mathcal{X} be a set of risks on Ω\Omega that contains the constants and ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R} a risk measure such that

1. *(i)*

   XX a risk, Y∈𝒳Y\in\mathcal{X}, X=dYX=\_{d}Y ⟹\Longrightarrow X∈𝒳X\in\mathcal{X}, ρ​(X)=ρ​(Y)\rho(X)=\rho(Y);
2. *(ii)*

   X,Y∈𝒳X,Y\in\mathcal{X} comonotonic ⟹\Longrightarrow X+Y∈𝒳X+Y\in\mathcal{X} and ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y);
3. *(iii)*

   X,Y∈𝒳X,Y\in\mathcal{X}, X≤*sl*YX\leq\_{\emph{\text{sl}}}Y ⟹\Longrightarrow ρ​(X)≤ρ​(Y)\rho(X)\leq\rho(Y).

Then, for all X,Y∈𝒳X,Y\in\mathcal{X}, if X+Y∈𝒳X+Y\in\mathcal{X} then ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y); that is, ρ\rho is subadditive.

We arrive at the main result of this paper. It follows, as in the proof of Theorem [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), from Lemma [5.45](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem45 "Lemma 5.45. ‣ 5.10. Distortion HG: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and Propositions [5.35](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem35 "Proposition 5.35. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.36](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem36 "Proposition 5.36. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [5.44](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem44 "Proposition 5.44. ‣ 5.10. Distortion HG: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Theorem 5.46.

Let gg be concave. Then the distortion Haezendonck-Goovaerts risk measure ρg,ϕ,α\rho\_{g,\phi,\alpha} is coherent on LgϕL\_{g}^{\phi}.

The proof by the first author given in [[28](https://arxiv.org/html/2512.03267v1#bib.bib28)] was based on Theorem [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), using a generalization of [[5](https://arxiv.org/html/2512.03267v1#bib.bib5), Proposition 13] and a variant of [[46](https://arxiv.org/html/2512.03267v1#bib.bib46), Theorem 1].

We recall that, by Example [3.9](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem9 "Example 3.9. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), the set LgϕL\_{g}^{\phi} is not necessarily a convex cone, even if gg is concave and ϕ\phi is the identity.

We do not know if concavity of gg is necessary for the coherence of ρg,ϕ,α\rho\_{g,\phi,\alpha}, see Problem [6.1](https://arxiv.org/html/2512.03267v1#S6.Thmtheorem1 "Problem 6.1. ‣ 6.1. Problems ‣ 6. Concluding remarks ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

### 5.11. The case of α=0\alpha=0

We turn to the announced reduction of the distortion Haezendonck-Goovaerts risk measure ρg,ϕ,0\rho\_{g,\phi,0}.

###### Theorem 5.47.

Let α=0\alpha=0. Then, for all X∈L∞X\in L^{\infty},

|  |  |  |
| --- | --- | --- |
|  | ρg​(X)≤ρg,ϕ,0​(X)≤c+c−​ρg​(X+)+c−c+​ρg​(−X−),\rho\_{g}(X)\leq\rho\_{g,\phi,0}(X)\leq\frac{c\_{+}}{c\_{-}}\rho\_{g}(X^{+})+\frac{c\_{-}}{c\_{+}}\rho\_{g}(-X^{-}), |  |

where c−c\_{-} is the left derivative of ϕ\phi at 11, and c+c\_{+} is the right derivative of ϕ\phi at 11. If ϕ\phi satisfies the Δ2\Delta\_{2}-condition, then this holds for all X∈LgϕX\in L\_{g}^{\phi}.

###### Corollary 5.48.

Let α=0\alpha=0. If ϕ\phi is differentiable at 11 and satisfies the Δ2\Delta\_{2}-condition, then

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,0=ρg\rho\_{g,\phi,0}=\rho\_{g} |  |

on LgϕL\_{g}^{\phi}.

Since the proof is quite technical, we relegate it to the Appendix, see Section [7](https://arxiv.org/html/2512.03267v1#S7 "7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

## 6. Concluding remarks

### 6.1. Problems

We suggest the following.

###### Problem 6.1.

Let gg be a distortion function, ϕ\phi a normalized Young function, and 0<α<10<\alpha<1. Characterize the coherence of the distortion Haezendonck-Goovaerts risk measure ρg,ϕ,α\rho\_{g,\phi,\alpha}.

###### Problem 6.2.

Let gg be a distortion function, ϕ\phi a normalized Young function, and 0<α<10<\alpha<1. Characterize the validity of the reverse Fatou property for the distortion Haezendonck-Goovaerts risk measure ρg,ϕ,α\rho\_{g,\phi,\alpha} on LgϕL\_{g}^{\phi}.

It might also be of interest, though of little consequence, to explore further the properties of ρg,ϕ,α\rho\_{g,\phi,\alpha} for α=0\alpha=0. In particular, we propose the following.

###### Problem 6.3.

Let gg be a distortion function, ϕ\phi a normalized Young function, and α=0\alpha=0. Does ρg,ϕ,0\rho\_{g,\phi,0} always have the Fatou property on LgϕL\_{g}^{\phi}? Characterize the validity of the reverse Fatou property for ρg,ϕ,0\rho\_{g,\phi,0} on LgϕL\_{g}^{\phi}.

### 6.2. Related work

Wu and Xu [[58](https://arxiv.org/html/2512.03267v1#bib.bib58)] have also, and independently, defined the Orlicz-Lorentz premium and the distortion Haezendonck-Goovaerts risk measure, but only for bounded risks and for distortion functions gg that are continuous and satisfy g​(0)=0g(0)=0. More precisely, given a continuous increasing function w:[0,1]→[0,1]w:[0,1]\to[0,1] with w​(0)=0w(0)=0 and w​(1)=1w(1)=1, a strictly increasing normalized Young function, and α∈[0,1)\alpha\in[0,1), they define a premium for X∈L+∞X\in L^{\infty}\_{+} as

|  |  |  |
| --- | --- | --- |
|  | π​(X)=inf{a>0:∫0∞ϕ​(t)​dw​(FX/a)​(t)≤1−α},\pi(X)=\inf\Big\{a>0:\int\_{0}^{\infty}\phi(t)\mathrm{d}w(F\_{X/a})(t)\leq 1-\alpha\Big\}, |  |

see [[58](https://arxiv.org/html/2512.03267v1#bib.bib58), equation (1.6)]. Now, using a push-forward measure argument and the fact that {FX−1​(1−u)≤x}={u<1−FX​(x)}c\{F\_{X}^{-1}(1-u)\leq x\}=\{u<1-F\_{X}(x)\}^{c}, we see that π\pi is the Orlicz-Lorentz premium for ϕ\phi, α\alpha, and the distortion function

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u)=1−w​(1−u),u∈[0,1],g(u)=1-w(1-u),\ u\in[0,1], |  | (6.1) |

which implies that gg is continuous and g​(0)=0g(0)=0. They then define a risk measure for X∈L∞X\in L^{\infty} in the usual way by

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=infx∈ℝ(π​((X−x)+)+x),\rho(X)=\inf\_{x\in\mathbb{R}}\big(\pi((X-x)^{+})+x\big), |  |

see [[58](https://arxiv.org/html/2512.03267v1#bib.bib58), equation (1.10)]. In that context they obtain Propositions [5.11](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem11 "Proposition 5.11. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.12](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem12 "Proposition 5.12. ‣ 5.4. Orlicz-Lorentz: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.30](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem30 "Proposition 5.30. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and Theorems [5.21](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem21 "Theorem 5.21. ‣ 5.5. Orlicz-Lorentz: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [5.46](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem46 "Theorem 5.46. ‣ 5.10. Distortion HG: the concave case ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), see [[58](https://arxiv.org/html/2512.03267v1#bib.bib58), Propositions 2.1 and 4.1]; their proof of coherence relies on the coherence of TVaR, see [[58](https://arxiv.org/html/2512.03267v1#bib.bib58), Appendix A]. However, in [[58](https://arxiv.org/html/2512.03267v1#bib.bib58), Proposition 2.1(i)] they claim that the infimum in the definition of π\pi is always attained if X≠0X\neq 0. Example [5.6](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem6 "Example 5.6. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") above shows that this is not the case (a fact also noted in [[12](https://arxiv.org/html/2512.03267v1#bib.bib12), p. 18]).

Motivated by the paper of Wu and Xu, Chudziak and Rela [[12](https://arxiv.org/html/2512.03267v1#bib.bib12)] have further generalized the Orlicz-Lorentz premia by replacing the function g​(F¯X​(x))=g​(P​(X>x))g(\overline{F}\_{X}(x))=g(P(X>x)) in ([5.2](https://arxiv.org/html/2512.03267v1#S5.E2 "In 5.2. Orlicz-Lorentz premia ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) & ([3.1](https://arxiv.org/html/2512.03267v1#S3.E1 "In 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) by μ​({X>x})\mu(\{X>x\}) for a general capacity μ\mu, using Choquet integrals, see [[12](https://arxiv.org/html/2512.03267v1#bib.bib12), equations (3), (5), (6)]. We remark, however, that their counter-example to [[58](https://arxiv.org/html/2512.03267v1#bib.bib58), Proposition 2.1(ix)] in [[12](https://arxiv.org/html/2512.03267v1#bib.bib12), p. 19] is not correct; they identify Wu and Xu’s ww with gg, while the correct link is given in ([6.1](https://arxiv.org/html/2512.03267v1#S6.E1 "In 6.2. Related work ‣ 6. Concluding remarks ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) above, so that a convex ww in fact corresponds to a concave gg.

## 7. Appendix

We first prove claims made in Remark [3.18](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem18 "Remark 3.18. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") concerning the relationship between the domain LgL\_{g} of a distortion risk measure and the Lorentz spaces. For this, let w:[0,1]→ℝw:[0,1]\to\mathbb{R} be a positive measurable function with ∫01w​(u)​du=1\int\_{0}^{1}w(u)\mathrm{d}u=1. Define g​(u)=∫0uw​(v)​dvg(u)=\int\_{0}^{u}w(v)\mathrm{d}v, u∈[0,1]u\in[0,1], which is a distortion function. Then consider the (classical) Lorentz space

|  |  |  |
| --- | --- | --- |
|  | Λ​(w)={X:‖X‖:=∫01F|X|−1​(1−u)​w​(u)​du<∞}.\Lambda(w)=\Big\{X:\|X\|:=\int\_{0}^{1}F\_{|X|}^{-1}(1-u)w(u)\mathrm{d}u<\infty\Big\}. |  |

###### Proposition 7.1.

We have that X∈LgX\in L\_{g} if and only if X+∈Λ​(w)X^{+}\in\Lambda(w) and ρ:=infx∈ℝ(‖(X−x)+‖+x)>−∞\rho:=\inf\_{x\in\mathbb{R}}(\|(X-x)^{+}\|+x)>-\infty; in that case, ρg​(X)=ρ\rho\_{g}(X)=\rho.

###### Proof.

For the proof of necessity, follow the argument in Example [5.25](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem25 "Example 5.25. ‣ 5.6. Distortion Haezendonck-Goovaerts risk measures ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a) and note that ρg​(X)=‖X‖\rho\_{g}(X)=\|X\| if X≥0X\geq 0. For sufficiency, let x≤0x\leq 0, and write I−={u∈(0,1):FX−1​(1−u)≤0}I\_{-}=\{u\in(0,1):F\_{X}^{-1}(1-u)\leq 0\}, I+=(0,1)∖I−I\_{+}=(0,1)\setminus I\_{-}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(X−x)+‖+x\displaystyle\|(X-x)^{+}\|+x | =∫01(F(X−x)+−1​(1−u)+x)​w​(u)​du\displaystyle=\int\_{0}^{1}(F^{-1}\_{(X-x)^{+}}(1-u)+x)w(u)\mathrm{d}u |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(∫I−+∫I+)​((FX−1​(1−u)−x)++x)​w​(u)​d​u.\displaystyle=\Big(\int\_{I\_{-}}+\int\_{I\_{+}}\Big)\big((F^{-1}\_{X}(1-u)-x)^{+}+x\big)w(u)\mathrm{d}u. |  |

Since x≤0x\leq 0, the second integral coincides with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫I+FX−1​(1−u)​w​(u)​du=∫I+FX+−1​(1−u)​w​(u)​du<∞,\int\_{I\_{+}}F^{-1}\_{X}(1-u)w(u)\mathrm{d}u=\int\_{I\_{+}}F^{-1}\_{X^{+}}(1-u)w(u)\mathrm{d}u<\infty, |  | (7.1) |

where we have used the first hypothesis. Thus, the second hypothesis implies that

|  |  |  |
| --- | --- | --- |
|  | infx≤0∫I−((FX−1​(1−u)−x)++x)​w​(u)​du>−∞.\inf\_{x\leq 0}\int\_{I\_{-}}\big((F^{-1}\_{X}(1-u)-x)^{+}+x\big)w(u)\mathrm{d}u>-\infty. |  |

Since the integrands are negative and decrease as xx decreases, the monotone convergence theorem implies that ∫I−FX−1​(1−u)​w​(u)​du>−∞\int\_{I\_{-}}F^{-1}\_{X}(1-u)w(u)\mathrm{d}u>-\infty, hence

|  |  |  |
| --- | --- | --- |
|  | ∫I−|FX−1​(1−u)|​w​(u)​du<∞.\int\_{I\_{-}}|F^{-1}\_{X}(1-u)|w(u)\mathrm{d}u<\infty. |  |

Altogether we get that

|  |  |  |
| --- | --- | --- |
|  | ∫01|FX−1​(1−u)|​w​(u)​du=(∫I−+∫I+)​|FX−1​(1−u)|​w​(u)​d​u<∞,\int\_{0}^{1}|F^{-1}\_{X}(1-u)|w(u)\mathrm{d}u=\Big(\int\_{I\_{-}}+\int\_{I\_{+}}\Big)|F^{-1}\_{X}(1-u)|w(u)\mathrm{d}u<\infty, |  |

where the second integral is finite by ([7.1](https://arxiv.org/html/2512.03267v1#S7.E1 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")).
∎

###### Proposition 7.2.

If ww is decreasing, then Λ​(w)⊂Lg\Lambda(w)\subset L\_{g}.

###### Proof.

Let X∈Λ​(w)X\in\Lambda(w). We claim that X∈LgX\in L\_{g}, that is ∫01|FX−1​(1−u)|​w​(u)​du<∞\int\_{0}^{1}|F\_{X}^{-1}(1-u)|w(u)\mathrm{d}u<\infty.

First, by monotonicity of VaR, we have that FX−1≤F|X|−1F\_{X}^{-1}\leq F\_{|X|}^{-1}, hence |FX−1​(1−u)|≤F|X|−1​(1−u)|F\_{X}^{-1}(1-u)|\leq F\_{|X|}^{-1}(1-u) if FX−1​(1−u)≥0F\_{X}^{-1}(1-u)\geq 0. Secondly, the upper and lower quantile functions coincide almost everywhere, see [[21](https://arxiv.org/html/2512.03267v1#bib.bib21), Lemma A.19]. Thus, with [[21](https://arxiv.org/html/2512.03267v1#bib.bib21), equation (4.44)] we have that FX−1​(1−u)=−F−X−1​(u)≥−F|X|−1​(u)F\_{X}^{-1}(1-u)=-F\_{-X}^{-1}(u)\geq-F\_{|X|}^{-1}(u) for almost all u∈[0,1]u\in[0,1], and hence |FX−1​(1−u)|≤F|X|−1​(u)|F\_{X}^{-1}(1-u)|\leq F\_{|X|}^{-1}(u) a.e. if FX−1​(1−u)≤0F\_{X}^{-1}(1-u)\leq 0.

Now, if X≥0X\geq 0, then there is nothing to prove.

Next, let X≤0X\leq 0, so that FX−1≤0F\_{X}^{-1}\leq 0 on [0,1][0,1]. Since ww is decreasing, we have that w​(u)≤w​(1−u)w(u)\leq w(1-u) if u≥12u\geq\frac{1}{2}. Hence ∫1/21|FX−1​(1−u)|​w​(u)​du≤∫1/21F|X|−1​(u)​w​(1−u)​du=∫01/2F|X|−1​(1−u)​w​(u)​du<∞\int\_{1/2}^{1}|F\_{X}^{-1}(1-u)|w(u)\mathrm{d}u\leq\int\_{1/2}^{1}F\_{|X|}^{-1}(u)w(1-u)\mathrm{d}u=\int\_{0}^{1/2}F\_{|X|}^{-1}(1-u)w(u)\mathrm{d}u<\infty. Since u↦|FX−1​(1−u)|u\mapsto|F\_{X}^{-1}(1-u)| is increasing, we obtain that X∈LgX\in L\_{g}.

In the remaining case, there is some δ∈(0,12]\delta\in(0,\frac{1}{2}] such that FX−1​(1−u)≥0F\_{X}^{-1}(1-u)\geq 0 if u≤δu\leq\delta and FX−1​(1−u)≤0F\_{X}^{-1}(1-u)\leq 0 if u≥1−δu\geq 1-\delta. It follows as above that ∫1−δ1|FX−1​(1−u)|​w​(u)​du<∞\int\_{1-\delta}^{1}|F\_{X}^{-1}(1-u)|w(u)\mathrm{d}u<\infty; also, ∫0δ|FX−1​(1−u)|​w​(u)​du≤∫0δF|X|−1​(1−u)​w​(u)​du<∞\int\_{0}^{\delta}|F\_{X}^{-1}(1-u)|w(u)\mathrm{d}u\leq\int\_{0}^{\delta}F\_{|X|}^{-1}(1-u)w(u)\mathrm{d}u<\infty. This then implies again that X∈LgX\in L\_{g}.
∎

###### Example 7.3.

(a) There is a decreasing weight ww such that Λ​(w)⊊Lg\Lambda(w)\subsetneq L\_{g}. Indeed, let w​(u)=2​(1−u)w(u)=2(1-u), u∈[0,1]u\in[0,1]. Also, choose a random variable YY with FY​(x)=1−1xF\_{Y}(x)=1-\frac{1}{x}, x≥1x\geq 1, and take X=−YX=-Y. Then |FX−1​(1−u)|=11−u|F\_{X}^{-1}(1-u)|=\frac{1}{1-u}, hence X∈LgX\in L\_{g}, but F|X|−1​(1−u)=1uF\_{|X|}^{-1}(1-u)=\frac{1}{u}, which shows that X∉Λ​(w)X\notin\Lambda(w).

(b) There is a weight ww (which is necessarily not decreasing) such that Λ​(w)⊄Lg\Lambda(w)\not\subset L\_{g}. Indeed, let w​(u)=2​uw(u)=2u, u∈[0,1]u\in[0,1], and take the same random variable XX as in (a). Then X∈Λ​(w)X\in\Lambda(w) but X∉LgX\notin L\_{g}.

In the same way, one can justify a claim made in Remark [5.5](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem5 "Remark 5.5. ‣ 5.2. Orlicz-Lorentz premia ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a); for the notation we refer to Section [5](https://arxiv.org/html/2512.03267v1#S5 "5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

###### Proposition 7.4.

Let ϕ\phi be a Young function and ww decreasing. Then Λϕ,w⊂Lgϕ\Lambda\_{\phi,w}\subset L\_{g}^{\phi}.

On the other hand, the analogue of Proposition [7.1](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem1 "Proposition 7.1. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") fails in general, even if gg is the identity.

###### Example 7.5.

Let gg be the identity and ϕ​(t)=t2\phi(t)=t^{2}. On Ω=(0,1]\Omega=(0,1] with the Lebesgue measure, we consider X​(ω)=−1ωX(\omega)=-\frac{1}{\sqrt{\omega}}. Then X∉LgϕX\notin L\_{g}^{\phi}. But one calculates that, for x≤−2x\leq-2, ‖(X−x)+‖+x=x2+4​x+2​ln⁡|x|+3+x≥−2\|(X-x)^{+}\|+x=\sqrt{x^{2}+4x+2\ln|x|+3}+x\geq-2.

We next prove a claim made in Remark [5.5](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem5 "Remark 5.5. ‣ 5.2. Orlicz-Lorentz premia ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b).

###### Proposition 7.6.

Let ϕ:ℝ→ℝ\phi:\mathbb{R}\to\mathbb{R} be an increasing convex function with ϕ​(0)=0\phi(0)=0, U​(t)=−ϕ​(−t)U(t)=-\phi(-t), t∈ℝt\in\mathbb{R}, the corresponding increasing concave function. Let hh be a distortion function with h​(0)=0h(0)=0, and define g​(u)=1−h​((1−u)−)g(u)=1-h((1-u)-), u∈[0,1]u\in[0,1]. Then gg is a distortion function with g​(0)=0g(0)=0 and, for any positive random variable XX,

|  |  |  |
| --- | --- | --- |
|  | (C)​∫U​(−X)​d​(h∘P)=−∫01ϕ​(FX−1​(1−u))​dg​(u),(C)\int U(-X)\mathrm{d}(h\circ P)=-\int\_{0}^{1}\phi(F\_{X}^{-1}(1-u))\mathrm{d}g(u), |  |

where the integral on the left is a Choquet integral.

###### Proof.

It is easy to see that gg is a distortion function with g​(u−)=1−h​(1−u)g(u-)=1-h(1-u) on [0,1][0,1].

For the notion of Choquet integrals, we refer to [[13](https://arxiv.org/html/2512.03267v1#bib.bib13)] and [[31](https://arxiv.org/html/2512.03267v1#bib.bib31), p. 68]. Using a property of quantile functions and writing Z=ϕ​(X)Z=\phi(X), we see that it suffices to show that

|  |  |  |
| --- | --- | --- |
|  | (C)​∫(−Z)​d​(h∘P)=−∫01FZ−1​(1−u)​dg​(u).(C)\int(-Z)\mathrm{d}(h\circ P)=-\int\_{0}^{1}F\_{Z}^{-1}(1-u)\mathrm{d}g(u). |  |

Since Z≥0Z\geq 0, the Choquet integral equals

|  |  |  |
| --- | --- | --- |
|  | ∫−∞0(h​(F¯−Z​(x))−1)​dx=−∫0∞(1−h​(F¯−Z​(−x)))​dx.\int\_{-\infty}^{0}(h(\overline{F}\_{-Z}(x))-1)\mathrm{d}x=-\int\_{0}^{\infty}(1-h(\overline{F}\_{-Z}(-x)))\mathrm{d}x. |  |

Now, F¯−Z​(−x)=P​(−Z>−x)=1−P​(Z≥x)\overline{F}\_{-Z}(-x)=P(-Z>-x)=1-P(Z\geq x). For all but countably many xx, this coincides with 1−P​(Z>x)=1−F¯Z​(x)1-P(Z>x)=1-\overline{F}\_{Z}(x). For these xx, we have

|  |  |  |
| --- | --- | --- |
|  | 1−h​(F¯−Z​(−x))=1−h​(1−F¯Z​(x))=g​(F¯Z​(x)−).1-h(\overline{F}\_{-Z}(-x))=1-h(1-\overline{F}\_{Z}(x))=g(\overline{F}\_{Z}(x)-). |  |

Hence, the Choquet integral equals

|  |  |  |
| --- | --- | --- |
|  | −∫0∞g​(F¯Z​(x)−)​dx=−∫01FZ−1​(1−u)​dg​(u),-\int\_{0}^{\infty}g(\overline{F}\_{Z}(x)-)\mathrm{d}x=-\int\_{0}^{1}F\_{Z}^{-1}(1-u)\mathrm{d}g(u), |  |

where we have used Proposition [3.5](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). This proves the claim.
∎

We finally give the proof of Theorem [5.47](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem47 "Theorem 5.47. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") (and hence of Theorem [4.19](https://arxiv.org/html/2512.03267v1#S4.Thmtheorem19 "Theorem 4.19. ‣ 4. Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")). For this we need two auxiliary results.

###### Lemma 7.7.

Let gg be a distortion function and X∈LgX\in L\_{g}. Then Xn:=max⁡(min⁡(X,n),−n)∈LgX\_{n}:=\max(\min(X,n),-n)\in L\_{g}, n≥1n\geq 1, and limn→∞ρg​(Xn)=ρg​(X)\lim\_{n\to\infty}\rho\_{g}(X\_{n})=\rho\_{g}(X).

###### Proof.

We have that |FXn−1|≤|FX−1||F^{-1}\_{X\_{n}}|\leq|F^{-1}\_{X}| and FXn−1→FX−1F^{-1}\_{X\_{n}}\to F^{-1}\_{X} on (0,1](0,1]. Thus the result follows from Definitions [3.2](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem2 "Definition 3.2. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), [3.4](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem4 "Definition 3.4. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), and the dominated convergence theorem.
∎

###### Lemma 7.8.

Let gg be a distortion function with g​(0)=0g(0)=0, ϕ\phi a normalized Young function that satisfies the Δ2\Delta\_{2}-condition, and α=0\alpha=0. Let Xn∈(Lgϕ)+X\_{n}\in(L\_{g}^{\phi})^{+} with Xn↘0X\_{n}\searrow 0. Then ρg,ϕ,0​(Xn)→0\rho\_{g,\phi,0}(X\_{n})\to 0.

###### Proof.

By Proposition [5.34](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem34 "Proposition 5.34. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a) and the positivity of the XnX\_{n} it suffices to show that an:=πg,ϕ,0​(Xn)→0a\_{n}:=\pi\_{g,\phi,0}(X\_{n})\to 0.

Suppose, on the contrary, that a:=limnan>0a:=\lim\_{n}a\_{n}>0. Then, for any nn, an>0a\_{n}>0, and by Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) we get that ∫01ϕ​(FXn−1​(1−u)an)​dg​(u)=1\int\_{0}^{1}\phi(\frac{F\_{X\_{n}}^{-1}(1-u)}{a\_{n}})\mathrm{d}g(u)=1, where we have used the Δ2\Delta\_{2}-condition. Hence, by ([3.1](https://arxiv.org/html/2512.03267v1#S3.E1 "In 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) and a property of quantile functions,

|  |  |  |
| --- | --- | --- |
|  | ∫0∞g​(F¯ϕ​(Xnan)​(x)−)​dx=1.\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X\_{n}}{a\_{n}})}(x)-\big)\mathrm{d}x=1. |  |

On the other hand, since Xnan→0\frac{X\_{n}}{a\_{n}}\to 0, F¯ϕ​(Xnan)​(x)→0\overline{F}\_{\phi(\frac{X\_{n}}{a\_{n}})}(x)\to 0 for all x>0x>0. Since g​(0)=0g(0)=0 and gg is continuous at 0, the dominated convergence theorem implies that 0=10=1; note that, by Lemma [5.7](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem7 "Lemma 5.7. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c), ∫0∞g​(F¯ϕ​(X1a)​(x)−)​dx<∞\int\_{0}^{\infty}g\big(\overline{F}\_{\phi(\frac{X\_{1}}{a})}(x)-\big)\mathrm{d}x<\infty by the Δ2\Delta\_{2}-condition. This is the desired contradiction.
∎

###### Proof of Theorem [5.47](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem47 "Theorem 5.47. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

Let X∈LgϕX\in L\_{g}^{\phi}. For simplicity we write π=πg,ϕ,0\pi=\pi\_{g,\phi,0} and σ​(x)=π​((X−x)+)+x\sigma(x)=\pi((X-x)^{+})+x, x∈ℝx\in\mathbb{R}. By Proposition [5.33](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem33 "Proposition 5.33. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a), ρg,ϕ,0​(X)=limx→−∞σ​(x)\rho\_{g,\phi,0}(X)=\lim\_{x\to-\infty}\sigma(x).

The proof requires several steps.

(1) We first suppose that XX is bounded.

(1a) Since ϕ\phi is convex, it is left- and right-differentiable at 11, so that c−c\_{-} and c+c\_{+} exist. Thus there is an increasing function h:[0,∞)→[0,∞)h:[0,\infty)\to[0,\infty) with h​(t)→0h(t)\to 0 as t→0t\to 0 such that, for 0≤t≤10\leq t\leq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤ϕ​(t)−(1+c−​(t−1))≤h​(|t−1|)​|t−1|,0\leq\phi(t)-(1+c\_{-}(t-1))\leq h(|t-1|)|t-1|, |  | (7.2) |

and, for t≥1t\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤ϕ​(t)−(1+c+​(t−1))≤h​(|t−1|)​|t−1|.0\leq\phi(t)-(1+c\_{+}(t-1))\leq h(|t-1|)|t-1|. |  | (7.3) |

Next, let x<ess​inf​Xx<\mathrm{ess\,inf\,}X. Then P​(X−x>0)=1P(X-x>0)=1, hence π​(X−x)≠0\pi(X-x)\neq 0 by Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(a); and since X−xX-x is bounded we have by Proposition [5.9](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem9 "Proposition 5.9. ‣ 5.3. Orlicz-Lorentz: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(c) that

|  |  |  |
| --- | --- | --- |
|  | ∫01ϕ​(FX−x−1​(1−u)π​(X−x))​dg​(u)=1.\int\_{0}^{1}\phi\Big(\frac{F\_{X-x}^{-1}(1-u)}{\pi(X-x)}\Big)\mathrm{d}g(u)=1. |  |

Since σ​(x)−x=π​((X−x)+)=π​(X−x)>0\sigma(x)-x=\pi((X-x)^{+})=\pi(X-x)>0, we have, using a property of quantile functions and the fact that g​(1−)=g​(1)g(1-)=g(1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫[0,1)ϕ​(FX−1​(1−u)−xσ​(x)−x)​dg​(u)=1.\int\_{[0,1)}\phi\Big(\frac{F\_{X}^{-1}(1-u)-x}{\sigma(x)-x}\Big)\mathrm{d}g(u)=1. |  | (7.4) |

Also, since XX is bounded, σ\sigma is increasing and σ​(t)\sigma(t) converges as t→−∞t\to-\infty, there is some M>0M>0 such that |FX−1|≤M|F\_{X}^{-1}|\leq M on (0,1](0,1] and |σ|≤M|\sigma|\leq M on (−∞,0](-\infty,0].

Writing t​(u)=FX−1​(1−u)−xσ​(x)−xt(u)=\frac{F\_{X}^{-1}(1-u)-x}{\sigma(x)-x}, we have that t​(u)−1=FX−1​(1−u)−σ​(x)σ​(x)−xt(u)-1=\frac{F\_{X}^{-1}(1-u)-\sigma(x)}{\sigma(x)-x}. Let I−={u∈[0,1):FX−1​(1−u)≤σ​(x)}I\_{-}=\{u\in[0,1):F\_{X}^{-1}(1-u)\leq\sigma(x)\} and I+=[0,1)∖I−I\_{+}=[0,1)\setminus I\_{-}. Thus t​(u)≤1t(u)\leq 1 if and only if u∈I−u\in I\_{-}.

We now integrate ϕ​(t​(u))−(1+c−​(t​(u)−1))\phi(t(u))-(1+c\_{-}(t(u)-1)) over I−I\_{-} and ϕ​(t​(u))−(1+c+​(t​(u)−1))\phi(t(u))-(1+c\_{+}(t(u)-1)) over I+I\_{+}, add the results, and apply ([7.2](https://arxiv.org/html/2512.03267v1#S7.E2 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), ([7.3](https://arxiv.org/html/2512.03267v1#S7.E3 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), ([7.4](https://arxiv.org/html/2512.03267v1#S7.E4 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) and the fact that ∫[0,1)dg​(u)=1\int\_{[0,1)}\mathrm{d}g(u)=1. We thus get, for x<−Mx<-M,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −c−​∫I−FX−1​(1−u)−σ​(x)σ​(x)−x​dg​(u)−\displaystyle-c\_{-}\int\_{I\_{-}}\frac{F\_{X}^{-1}(1-u)-\sigma(x)}{\sigma(x)-x}\,\mathrm{d}g(u)- | c+​∫I+FX−1​(1−u)−σ​(x)σ​(x)−x​dg​(u)\displaystyle c\_{+}\int\_{I\_{+}}\frac{F\_{X}^{-1}(1-u)-\sigma(x)}{\sigma(x)-x}\,\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h​(2​M|x|−M)​∫[0,1)|FX−1​(1−u)−σ​(x)σ​(x)−x|​dg​(u)\displaystyle\leq h\Big(\frac{2M}{|x|-M}\Big)\int\_{[0,1)}\Big|\frac{F\_{X}^{-1}(1-u)-\sigma(x)}{\sigma(x)-x}\Big|\mathrm{d}g(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h​(2​M|x|−M)​2​Mσ​(x)−x.\displaystyle\leq h\Big(\frac{2M}{|x|-M}\Big)\frac{2M}{\sigma(x)-x}. |  |

Writing δ:=c+−c−≥0\delta:=c\_{+}-c\_{-}\geq 0, and noting the definition of ρg​(X)\rho\_{g}(X), we thus find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | c−​(σ​(x)−ρg​(X))+δ​∫I+(σ​(x)−FX−1​(1−u))​dg​(u)≤2​M.h​(2​M|x|−M).\displaystyle c\_{-}(\sigma(x)-\rho\_{g}(X))+\delta\int\_{I\_{+}}(\sigma(x)-F\_{X}^{-1}(1-u))\mathrm{d}g(u)\leq 2M.h\Big(\frac{2M}{|x|-M}\Big). |  | (7.5) |

We now distinguish two cases.

(1b) Suppose that X≥0X\geq 0. Then FX−1≥0F\_{X}^{-1}\geq 0 on (0,1](0,1]; also, ρg,ϕ,0​(X)≥0\rho\_{g,\phi,0}(X)\geq 0 by monotonicity and hence σ​(x)≥0\sigma(x)\geq 0 for all xx by Proposition [5.33](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem33 "Proposition 5.33. ‣ 5.8. Distortion HG: the infimum ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"). Thus, ([7.5](https://arxiv.org/html/2512.03267v1#S7.E5 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) implies that

|  |  |  |
| --- | --- | --- |
|  | c−​(σ​(x)−ρg​(X))≤δ​ρg​(X)+2​M.h​(2​M|x|−M).c\_{-}(\sigma(x)-\rho\_{g}(X))\leq\delta\rho\_{g}(X)+2M.h\Big(\frac{2M}{|x|-M}\Big). |  |

Letting x→−∞x\to-\infty, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg,ϕ,0​(X)≤(δc−+1)​ρg​(X)=c+c−​ρg​(X).\rho\_{g,\phi,0}(X)\leq\Big(\frac{\delta}{c\_{-}}+1\Big)\rho\_{g}(X)=\frac{c\_{+}}{c\_{-}}\rho\_{g}(X). |  | (7.6) |

(1c) Now let X≤0X\leq 0, hence FX−1≤0F\_{X}^{-1}\leq 0 on (0,1](0,1]. Since I+=∅I\_{+}=\varnothing if σ​(x)≥0\sigma(x)\geq 0, we see that ∫I+(−σ​(x))​dg​(u)≤(−σ​(x))+\int\_{I\_{+}}(-\sigma(x))\mathrm{d}g(u)\leq(-\sigma(x))^{+}. Thus, ([7.5](https://arxiv.org/html/2512.03267v1#S7.E5 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) implies that

|  |  |  |
| --- | --- | --- |
|  | c−​(σ​(x)−ρg​(X))≤δ​(−σ​(x))++2​M.h​(2​M|x|−M).c\_{-}(\sigma(x)-\rho\_{g}(X))\leq\delta(-\sigma(x))^{+}+2M.h\Big(\frac{2M}{|x|-M}\Big). |  |

Letting x→−∞x\to-\infty, and noting that ρg,ϕ,0​(X)≤0\rho\_{g,\phi,0}(X)\leq 0, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg,ϕ,0​(X)≤c−c−+δ​ρg​(X)=c−c+​ρg​(X).\rho\_{g,\phi,0}(X)\leq\frac{c\_{-}}{c\_{-}+\delta}\rho\_{g}(X)=\frac{c\_{-}}{c\_{+}}\rho\_{g}(X). |  | (7.7) |

(1d) Finally, for arbitrary bounded XX, we write X=X+−X−X=X^{+}-X^{-}. Since X+=max⁡(X,0)X^{+}=\max(X,0) and −X−=min⁡(X,0)-X^{-}=\min(X,0) are comonotonic, Proposition [5.36](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem36 "Proposition 5.36. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), ([7.6](https://arxiv.org/html/2512.03267v1#S7.E6 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) and ([7.7](https://arxiv.org/html/2512.03267v1#S7.E7 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), with Proposition [5.34](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem34 "Proposition 5.34. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")(b), imply that

|  |  |  |
| --- | --- | --- |
|  | ρg​(X)≤ρg,ϕ,0​(X)≤ρg,ϕ,0​(X+)+ρg,ϕ,0​(−X−)≤c+c−​ρg​(X+)+c−c+​ρg​(−X−).\displaystyle\rho\_{g}(X)\leq\rho\_{g,\phi,0}(X)\leq\rho\_{g,\phi,0}(X^{+})+\rho\_{g,\phi,0}(-X^{-})\leq\frac{c\_{+}}{c\_{-}}\rho\_{g}(X^{+})+\frac{c\_{-}}{c\_{+}}\rho\_{g}(-X^{-}). |  |

This shows the desired inequality for X∈L∞X\in L^{\infty}.

(2) We now let X∈LgϕX\in L\_{g}^{\phi} be arbitrary, where we assume that ϕ\phi satisfies the Δ2\Delta\_{2}-condition.

(2a) Suppose again that X≥0X\geq 0. Assume first that g​(0)=0g(0)=0. Since X=min⁡(X,n)+(X−n)+X=\min(X,n)+(X-n)^{+}, and since min⁡(X,n)\min(X,n) and (X−n)+(X-n)^{+} are comonotonic, it follows from Proposition [5.36](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem36 "Proposition 5.36. ‣ 5.9. Distortion HG: risk theoretic properties ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") that ρg,ϕ,0​(X)≤ρg,ϕ,0​(min⁡(X,n))+ρg,ϕ,0​((X−n)+)\rho\_{g,\phi,0}(X)\leq\rho\_{g,\phi,0}(\min(X,n))+\rho\_{g,\phi,0}((X-n)^{+}), hence, by ([7.6](https://arxiv.org/html/2512.03267v1#S7.E6 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")),

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,0​(X)≤c+c−​ρg​(min⁡(X,n))+ρg,ϕ,0​((X−n)+).\rho\_{g,\phi,0}(X)\leq\frac{c\_{+}}{c\_{-}}\rho\_{g}(\min(X,n))+\rho\_{g,\phi,0}((X-n)^{+}). |  |

Letting n→∞n\to\infty, and applying Lemmas [7.7](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem7 "Lemma 7.7. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and [7.8](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem8 "Lemma 7.8. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg,ϕ,0​(X)≤c+c−​ρg​(X).\rho\_{g,\phi,0}(X)\leq\frac{c\_{+}}{c\_{-}}\rho\_{g}(X). |  | (7.8) |

On the other hand, suppose that g​(0)>0g(0)>0. Then XX is bounded above, hence bounded, by the discussion after Definition [5.1](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem1 "Definition 5.1. ‣ 5.1. The domain ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), so that ([7.8](https://arxiv.org/html/2512.03267v1#S7.E8 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) holds by ([7.6](https://arxiv.org/html/2512.03267v1#S7.E6 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")).

(2b) Now suppose that X≤0X\leq 0. Then, for n≥1n\geq 1,

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,0​(X)≤ρg,ϕ,0​(max⁡(X,−n)).\rho\_{g,\phi,0}(X)\leq\rho\_{g,\phi,0}(\max(X,-n)). |  |

Applying ([7.7](https://arxiv.org/html/2512.03267v1#S7.E7 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")), we get that

|  |  |  |
| --- | --- | --- |
|  | ρg,ϕ,0​(X)≤c−c+​ρg​(max⁡(X,−n)).\rho\_{g,\phi,0}(X)\leq\frac{c\_{-}}{c\_{+}}\rho\_{g}(\max(X,-n)). |  |

Letting n→∞n\to\infty, and applying Lemma [7.7](https://arxiv.org/html/2512.03267v1#S7.Thmtheorem7 "Lemma 7.7. ‣ 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures"), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg,ϕ,0​(X)≤c−c+​ρg​(X).\rho\_{g,\phi,0}(X)\leq\frac{c\_{-}}{c\_{+}}\rho\_{g}(X). |  | (7.9) |

(2c) One can now obtain the desired inequality for arbitrary X∈LgϕX\in L\_{g}^{\phi} as in (1d), using this time ([7.8](https://arxiv.org/html/2512.03267v1#S7.E8 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")) and ([7.9](https://arxiv.org/html/2512.03267v1#S7.E9 "In 7. Appendix ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures")).
∎

###### Proof of Corollary [5.48](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem48 "Corollary 5.48. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures").

If ϕ\phi is differentiable at 11 then c−=c+c\_{-}=c\_{+} in Theorem [5.47](https://arxiv.org/html/2512.03267v1#S5.Thmtheorem47 "Theorem 5.47. ‣ 5.11. The case of 𝛼=0 ‣ 5. Distortion Haezendonck-Goovaerts risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") and hence

|  |  |  |
| --- | --- | --- |
|  | ρg​(X)≤ρg,ϕ,0​(X)≤ρg​(X+)+ρg​(−X−).\rho\_{g}(X)\leq\rho\_{g,\phi,0}(X)\leq\rho\_{g}(X^{+})+\rho\_{g}(-X^{-}). |  |

Since X+X^{+} and −X−-X^{-} are comonotonic, Proposition [3.11](https://arxiv.org/html/2512.03267v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3. Distortion risk measures ‣ Orlicz-Lorentz premia and Distortion Haezendonck-Goovaerts risk measures") implies that the right-hand side equals
ρg​(X+−X−)=ρg​(X)\rho\_{g}(X^{+}-X^{-})=\rho\_{g}(X), so that the result follows.
∎

### Acknowledgements

The authors are grateful to Anna Kamińska for sharing her expertise on Orlicz-Lorentz spaces. We also thank Emanuela Rosazza Gianin and the members of the PhD-committee of the first author, Michèle Vermaele, Jan Dhaene, and Daniël Linders, for interesting discussions.

## References

* [1]
   C. Acerbi and D. Tasche, On the coherence of expected shortfall, *J. Banking & Finance* 26 (2002), 1487–1503.
* [2]
   J. Y. Ahn and N. D. Shyamalkumar, Asymptotic theory for the empirical Haezendonck-Goovaerts risk measure, *Insurance Math. Econom.* 55 (2014), 78–90.
* [3]
   M. Amarante and F.-B. Liebrich, Distortion risk measures: prudence, coherence, and the expected shortfall, *Math. Finance* 34 (2024), 1291–1327.
* [4]
   P. Artzner, F. Delbaen, J.-M. Eber, and D. Heath, Coherent measures of risk, *Math. Finance* 9 (1999), 203–228.
* [5]
   F. Bellini and E. Rosazza Gianin, On Haezendonck risk measures, *J. Banking & Finance* 32 (2008), 986–994.
* [6]
   F. Bellini and E. Rosazza Gianin, Optimal portfolios with Haezendonck risk measures, *Statist. Decisions* 26 (2008), 89–108.
* [7]
   F. Bellini and E. Rosazza Gianin, Haezendonck-Goovaerts risk measures and Orlicz quantiles, *Insurance Math. Econom.* 51 (2012), 107–114.
* [8]
   G. Canna, F. Centrone, and E. Rosazza Gianin, Haezendonck-Goovaerts capital allocation rules, *Insurance Math. Econom*. 101 (2021), 173–185.
* [9]
   M. J. Carro, J. A. Raposo, and J. Soria, Recent developments in the theory of Lorentz spaces and weighted inequalities,
  *Mem. Amer. Math. Soc.* 187 (2007), no. 877.
* [10]
   S. Chen, Geometry of Orlicz spaces, Dissertationes Math. (Rozprawy Mat.) 356 (1996).
* [11]
   S. Chen, N. Gao, D. H. Leung, and L. Li, Automatic Fatou property of law-invariant risk measures, *Insurance Math. Econom.* 105 (2022), 41–53.
* [12]
   J. Chudziak and P. Rela, The Orlicz premium principle under uncertainty, *Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. RACSAM* 119 (2025), Paper No. 116, 23 pp.
* [13]
   D. Denneberg, *Non-additive measure and integral*, Kluwer, Dordrecht 1994.
* [14]
   M. Denuit, J. Dhaene, M. Goovaerts, and R. Kaas, Actuarial theory for dependent risks, John Wiley & Sons,
  Chichester 2005.
* [15]
   J. Dhaene, M. Denuit, M. J. Goovaerts, R Kaas, and D. Vyncke, The concept of comonotonicity in actuarial science and finance: theory, Insurance Math. Econom. 31 (2002), 3–33.
* [16]
   J. Dhaene, A. Kukush, D. Linders, and Q. Tang, Remarks on quantiles and distortion risk measures, *Eur. Actuar. J.* 2 (2012), 319–328.
* [17]
   J. Dhaene, R. J. A. Laeven, S. Vanduffel, G. Darkiewicz, and M. J. Goovaerts, Can a coherent risk measure be too subadditive, *J. Risk Insurance* 75 (2008), 365–386.
* [18]
   J. Dhaene, S. Vanduffel, M. J. Goovaerts, R. Kaas, Q. Tang, and D. Vyncke, Risk measures and comonotonicity: a review, *Stoch. Models* 22 (2006), 573–606.
* [19]
   G. A. Edgar and L. Sucheston, Stopping times and directed processes, Cambridge University Press, Cambridge 1992.
* [20]
   P. Embrechts and R. Wang, Seven proofs for the subadditivity of expected shortfall, *Depend. Model.* 3 (2015), 126–140.
* [21]
   H. Föllmer and A. Schied, Stochastic finance, fourth edition, De Gruyter, Berlin 2016.
* [22]
   C. Fröhlich and R. C. Williamson, Risk measures and upper probabilities: coherence and stratification, *J. Mach. Learn. Res.* 25 (2024), Paper No. 207, 100 pp.
* [23]
   N. Gao, C. Munari, and F. Xanthos, Stability properties of Haezendonck–Goovaerts premium principles, *Insurance Math. Econom.* 94 (2020), 94–99.
* [24]
   H. Geiss and S. Geiss, Measure, probability and functional analysis, Springer, Cham 2025.
* [25]
   C. Gonzales and P. Perny, Decision under uncertainty, in: P. Marquis, O. Papini, and H. Prade (editors), *A guided tour of artificial intelligence research. Vol. I. Knowledge representation, reasoning and learning*, pp. 549–586,
  Springer, Cham 2020.
* [26]
   M. J. Goovaerts, R. Kaas, J. Dhaene, and Q. Tang, Some new classes of consistent risk measures, *Insurance Math. Econom.* 34 (2004), 505–516.
* [27]
   M. Goovaerts, D. Linders, K. Van Weert, and F. Tank, On the interplay between distortion, mean value and Haezendonck-Goovaerts risk measures, *Insurance Math. Econom.* 51 (2012), 10–18.
* [28]
   A. Goulard, Les mesures de risque de Haezendonck-Wang, PhD-thesis, Université de Mons, Mons 2022.
* [29]
   J. Haezendonck and M. Goovaerts, A new premium calculation principle based on Orlicz norms,
  *Insurance Math. Econom.* 1 (1982), 41–53.
* [30]
   X. D. He, H. Jin, and X. Y. Zhou, Dynamic portfolio choice when risk is measured by weighted VaR, *Math. Oper. Res.* 40 (2015), 773–796.
* [31]
   S. Heilpern, A rank-dependent generalization of zero utility principle, *Insurance Math. Econom.* 33 (2003), 67–73.
* [32]
   H. Hudzik, H., A. Kamińska, and M. Mastyło, On the dual of Orlicz-Lorentz space, *Proc. Amer. Math. Soc.* 130 (2002), 1645–1654.
* [33]
   E. Jouini, W. Schachermayer, and N. Touzi, Law invariant risk measures have the Fatou property, in: *Advances in mathematical economics. Vol. 9*, pp. 49–71, Springer, Tokyo 2006.
* [34]
   R. Kaas, J. Dhaene, and M. J. Goovaerts, Upper and lower bounds for sums of random variables, *Insurance Math. Econom.* 27 (2000), 151–168.
* [35]
   A. Kamińska, Some remarks on Orlicz-Lorentz spaces, *Math. Nachr.* 147 (1990), 29–38.
* [36]
   A. Kamińska, L. Maligranda, and L. E. Persson, Indices, convexity and concavity of Calderón-Lozanovskii spaces,
  *Math. Scand.* 92 (2003), 141–160.
* [37]
   F.-B. Liebrich and C. Munari, Short communication: revisiting the automatic Fatou property of law-invariant functionals, *SIAM J. Financial Math.* 16 (2025), SC1–SC11.
* [38]
   Q. Liu, L. Peng, and X. Wang, Haezendonck-Goovaerts risk measure with a heavy tailed loss, *Insurance Math. Econom.* 76 (2017), 28–47.
* [39]
   G. G. Lorentz, On the theory of spaces Λ\Lambda, *Pacific J. Math.* 1 (1951), 411–429.
* [40]
   R. E. Megginson, An introduction to Banach space theory, Springer, New York 1998.
* [41]
   A. Pichler, The natural Banach space for version independent risk measures, *Insurance Math. Econom.* 53 (2013), 405–415.
* [42]
   L. Pick, A. Kufner, O. John, and S. Fučík, *Function spaces, Vol. 1,* second edition, Walter de Gruyter & Co., Berlin 2013.
* [43]
   J. Quiggin, A theory of anticipated utility, *J. Econ. Behav. Organization* 3 (1982), 323–343.
* [44]
   J. Quiggin, *Generalized expected utility theory: The rank-dependent model*, Kluwer, Boston 1993.
* [45]
   M. M. Rao and Z. D. Ren, *Theory of Orlicz spaces*, Marcel Dekker, New York 1991.
* [46]
   R. T. Rockafellar, *Conjugate duality and optimization*, Society for Industrial and Applied Mathematics, Philadelphia, PA 1974.
* [47]
   R. T. Rockafellar and S. Uryasev, Optimization of conditional value-at-risk, *J. Risk* 2 (2000), no. 2, 21–41.
* [48]
   R. T. Rockafellar and S. Uryasev, Conditional value-at-risk for general loss distributions, *J. Banking & Finance* 26 (2002), 1443–1471.
* [49]
   E. Rosazza Gianin and C. Sgarra, *Mathematical finance: theory review and exercises*, Springer, Cham 2013.
* [50]
   L. Rüschendorf, Mathematical risk analysis, Springer, Heidelberg 2013.
* [51]
   M. Shaked and J. G. Shanthikumar, Stochastic orders, Springer, New York 2007.
* [52]
   G. Svindland, Continuity properties of law-invariant (quasi-)convex risk functions on L∞L^{\infty}, *Math. Financ. Econ.* 3 (2010), 39–43.
* [53]
   Q. Tang and F. Yang, Extreme value analysis of the Haezendonck-Goovaerts risk measure with a general Young function, *Insurance Math. Econom.* 59 (2014), 311–320.
* [54]
   P. P. Wakker, *Prospect theory: For risk and ambiguity*, Cambridge University Press, Cambridge 2010.
* [55]
   S. Wang, Premium calculation by transforming the layer premium density, *ASTIN Bull.* 26 (1996), 71–92.
* [56]
   S. Wang and J. Dhaene, Comonotonicity, correlation order and premium principles, *Insurance Math. Econom.* 22 (1998), 235–242.
* [57]
   P. Wei, Risk management with weighted VaR, *Math. Finance* 28 (2018), 1020–1060.
* [58]
   Q. Wu and H. Xu, Robust distorted Orlicz premium: modelling, computational scheme and applications (April 26, 2022). Available at SSRN: http://dx.doi.org/10.2139/ssrn.4093580.
* [59]
   A. C. Zaanen, Riesz spaces. II, North-Holland Publishing Co., Amsterdam 1983.