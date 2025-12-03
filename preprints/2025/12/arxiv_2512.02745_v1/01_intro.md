---
authors:
- Qinling Wang
- Xiaoyu Shen
- Fang Fang
doc_id: arxiv:2512.02745v1
family_id: arxiv:2512.02745
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Note on the Conditions for COS Convergence
url_abs: http://arxiv.org/abs/2512.02745v1
url_html: https://arxiv.org/html/2512.02745v1
venue: arXiv q-fin
version: 1
year: 2025
---


Qinling Wang
Delft Institute of Applied Mathematics, Delft University of Technology, 2628 CD Delft, the Netherlands
([q.wang-7@tudelft.nl](mailto:q.wang-7@tudelft.nl)).
  
Xiaoyu Shen
[FF Quant Advisory B.V.](https://fsquaredquant.nl), 3531 WR Utrecht, the Netherlands ([xiaoyu.shen@ffquant.nl](mailto:xiaoyu.shen@ffquant.nl)).
  
Fang Fang
[FF Quant Advisory B.V.](https://fsquaredquant.nl), 3531 WR Utrecht, the Netherlands ([fang.fang@ffquant.nl](mailto:fang.fang@ffquant.nl)) and Delft Institute of Applied Mathematics, Delft University of Technology, 2628 CD Delft, the Netherlands ( [f.fang@tudelft.nl](mailto:f.fang@tudelft.nl)).

###### Abstract

We study the truncation error of the COS method and give simple, verifiable conditions that guarantee convergence. In one dimension, COS is admissible when the density belongs to both L1 and L2 and has a finite weighted L2 moment of order strictly greater than one. We extend the result to multiple dimensions by requiring the moment order to exceed the dimension. These conditions enlarge the class of densities covered by previous analyses and include heavy-tailed distributions such as Student t with small degrees of freedom.

## 1 Introduction

Fourier-based methods have become fundamental tools in computational
probability, quantitative finance, and the numerical solution of
integro–differential equations.
Among these techniques, the COS method of
Fang and Oosterlee [fang2009novel] is particularly attractive due to its exponential
convergence for sufficiently regular densities and its ability to exploit
closed-form characteristic functions.
The method approximates a target
probability density function (pdf) ff on a truncated interval [−L,L][-L,L]
through a cosine series expansion whose coefficients computed from
the characteristic function of ff.
A central theoretical question is
therefore to understand the behavior of the COS approximation error as both the number
of cosine modes KK and the truncation parameter LL tend to infinity.

In the existing literature, the convergence of the COS method is typically
established under assumptions that ensure sufficiently fast decay of ff.
A widely used sufficient condition is the so-called
*COS-admissibility* introduced in [junike2022precise], which requires the tail cosine energy

|  |  |  |
| --- | --- | --- |
|  | B​(L):=∑k=0∞1L​|∫ℝ∖[−L,L]f​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x|2.B(L):=\sum\_{k=0}^{\infty}\frac{1}{L}\Bigg|\int\_{\mathbb{R}\setminus[-L,L]}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)\,dx\Bigg|^{2}. |  |

to vanish as L→∞L\to\infty. It has also been proven that if B​(L)→0B(L)\to 0, then the L2L^{2}-error of the COS
approximation converges to zero as K,L→∞K,L\to\infty, providing a clean and
practical criterion for sufficiently regular densities commonly encountered in
applications.

The purpose of this paper is to provide some weaker conditions under which the PDF is
COS-admissible. We show that ff is COS-admissible as long as
f∈L1∩L2f\in L^{1}\cap L^{2} and it has a finite pp-th *square-integrable*
moment ∫|x|p​|f​(x)|2<∞\int|x|^{p}|f(x)|^{2}<\infty for some p>1p>1. And we can extend this analysis
to higher dimensions. This enlarges the set of distributions which are COS-admissible, making COS method
a reliable method for many distributions and financial models.

## 2 Review of the COS method and the COS-admissibility

We recall the framework of the COS method (in one dimension) given in [fang2009novel] and the condition for the COS method to converge given in [junike2022precise].

Consider a pdf ff and a sufficiently large interval [a,b]⊂ℝ[a,b]\subset\mathbb{R}, the Fourier-cosine series expansion can be given by

|  |  |  |
| --- | --- | --- |
|  | f​(x)≈∑′k=0∞Ak​cos⁡(k​π​x−ab−a)x∈(a,b)f(x)\approx{\sum\nolimits\!^{\prime}}\_{k=0}^{\infty}A\_{k}\cos\!\left(k\pi\frac{x-a}{b-a}\right)\quad x\in(a,b) |  |

with

|  |  |  |
| --- | --- | --- |
|  | Ak=2b−a​∫abf​(x)​cos⁡(k​π​x−ab−a)​𝑑x.A\_{k}=\frac{2}{b-a}\int\_{a}^{b}f(x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx. |  |

Assume [a,b][a,b] is chosen such that the truncated integral can approximate the infinite counterpart very well, i.e.

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(ω)≔∫abei​ω​x​f​(x)​𝑑x≈∫ℝei​ω​x​f​(x)​𝑑x=ϕ​(ω).\phi\_{1}(\omega)\coloneqq\int\_{a}^{b}e^{i\omega x}f(x)dx\approx\int\_{\mathbb{R}}e^{i\omega x}f(x)dx=\phi(\omega). |  |

We note that AkA\_{k} can be computed by ϕ1\phi\_{1}:

|  |  |  |
| --- | --- | --- |
|  | Ak=2b−a​ℜ⁡[ϕ1​(k​πb−a)⋅exp⁡(−i​k​a​πb−a)],A\_{k}=\frac{2}{b-a}\Re\left[\phi\_{1}(\frac{k\pi}{b-a})\cdot\exp(-i\frac{ka\pi}{b-a})\right], |  |

replace ϕ1\phi\_{1} with ϕ\phi, we can approximate AkA\_{k} by

|  |  |  |
| --- | --- | --- |
|  | Fk≔2b−a​ℜ⁡[ϕ​(k​πb−a)⋅exp⁡(−i​k​a​πb−a)].F\_{k}\coloneqq\frac{2}{b-a}\Re\left[\phi(\frac{k\pi}{b-a})\cdot\exp(-i\frac{ka\pi}{b-a})\right]. |  |

Replace AkA\_{k} by FkF\_{k} and truncate the Fourier-cosine series, we can approximate the pdf ff with

|  |  |  |
| --- | --- | --- |
|  | f1N​(x)≔∑′k=0N−1Fk​cos⁡(k​π​x−ab−a).f\_{1}^{N}(x)\coloneqq{\sum\nolimits\!^{\prime}}\_{k=0}^{N-1}F\_{k}\cos\!\left(k\pi\frac{x-a}{b-a}\right). |  |

To make things easier, we would only consider the case where a=−La=-L and b=Lb=L for some L>0L>0 in the following part of the paper.

It is important to ask, under which condition, can we say that f1Nf\_{1}^{N} will converge to ff (in some sense of convergence) as both NN and LL go in infinity? It is answered in [junike2022precise], where it has been proven that when a pdf is COS-admissible, the COS method will converge in L2L^{2}.

###### Definition 1.

A function f∈L1f\in L^{1} is called COS-admissible if

|  |  |  |
| --- | --- | --- |
|  | B​(L)≔∑k=0∞1L​|∫ℝ∖[−L,L]f​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x|2→0​ as ​L→∞.B(L)\coloneqq\sum\_{k=0}^{\infty}\frac{1}{L}\Bigg|\int\_{\mathbb{R}\setminus[-L,L]}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)\,dx\Bigg|^{2}\to 0\text{ as }L\to\infty. |  |

###### Theorem 1.

Assume f∈L1∩L2f\in L^{1}\cap L^{2} to be COS-admissible, then

|  |  |  |
| --- | --- | --- |
|  | limL→∞lim supN→∞‖f−f1N‖2=0.\lim\_{L\to\infty}\limsup\_{N\to\infty}\|f-f\_{1}^{N}\|\_{2}=0. |  |

It is usually not easy to check if a pdf ff is COS-admissible directly. Authors of [junike2022precise] gave a condition under which the pdf is COS-admissible.
We would extend this result a bit so that more distributions can be covered and compare these two conditions in the Remark [1](https://arxiv.org/html/2512.02745v1#Thmremark1 "Remark 1. ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence").

## 3 Generalized Moment Bound

We derive a decay rate depending on available square-integrable moments of ff.

###### Proposition 1 (Moment-based COS bound).

Let p>1p>1. Suppose f∈L1​(ℝ)∩L2​(ℝ)f\in L^{1}(\mathbb{R})\cap L^{2}(\mathbb{R}) and |x|p/2​f​(x)∈L2​(ℝ)|x|^{p/2}f(x)\in L^{2}(\mathbb{R}) (equivalently ∫ℝ|x|p​|f​(x)|2​𝑑x<∞\int\_{\mathbb{R}}|x|^{p}|f(x)|^{2}dx<\infty). Then ff is COS-admissible and

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(L)≤2​ζ​(p)​(L−p​∫|x|>L|x|p​|f​(x)|2​𝑑x+∫|x|>L|f​(x)|2​𝑑x),L>0.B(L)\leq 2\,\zeta(p)\Bigg(L^{-p}\int\_{|x|>L}|x|^{p}|f(x)|^{2}dx+\int\_{|x|>L}|f(x)|^{2}dx\Bigg),\quad L>0. |  | (1) |

In particular the tail-sensitive rate bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(L)≤4​ζ​(p)​L−p​∫|x|>L|x|p​|f​(x)|2​𝑑xB(L)\leq 4\,\zeta(p)\,L^{-p}\int\_{|x|>L}|x|^{p}|f(x)|^{2}dx |  | (2) |

holds, and since ∫|x|>L|x|p​|f|2≤∫ℝ|x|p​|f|2\int\_{|x|>L}|x|^{p}|f|^{2}\leq\int\_{\mathbb{R}}|x|^{p}|f|^{2} we obtain the uniform bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(L)≤4​ζ​(p)​L−p​∫ℝ|x|p​|f​(x)|2​𝑑x.B(L)\leq 4\,\zeta(p)\,L^{-p}\int\_{\mathbb{R}}|x|^{p}|f(x)|^{2}dx. |  | (3) |

Consequently B​(L)=O​(L−p)B(L)=O(L^{-p}) and more precisely

|  |  |  |
| --- | --- | --- |
|  | B​(L)≤2​ζ​(p)​L−p​∫ℝ|x|p​|f​(x)|2​𝑑x+o​(L−p).B(L)\leq 2\,\zeta(p)\,L^{-p}\int\_{\mathbb{R}}|x|^{p}|f(x)|^{2}dx+o(L^{-p}). |  |

###### Proof.

It suffices to bound the contributions from x>Lx>L and x<−Lx<-L symmetrically. Define for k≥0k\geq 0 the positive tail integrals

|  |  |  |
| --- | --- | --- |
|  | Ik+​(L):=∫L∞f​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x.I\_{k}^{+}(L):=\int\_{L}^{\infty}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)dx. |  |

Partition [L,∞)[L,\infty) into disjoint blocks of length 2​L2L:

|  |  |  |
| --- | --- | --- |
|  | Ij:=[2​j​L−L, 2​j​L+L],j≥1.I\_{j}:=[2jL-L,\,2jL+L],\qquad j\geq 1. |  |

Then by absolute convergence (f∈L1f\in L^{1})

|  |  |  |
| --- | --- | --- |
|  | Ik+​(L)=∑j=1∞∫Ijf​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x.I\_{k}^{+}(L)=\sum\_{j=1}^{\infty}\int\_{I\_{j}}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)dx. |  |

Apply weighted Cauchy–Schwarz with weights j−p/2j^{-p/2} and jp/2j^{p/2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Ik+​(L)|2\displaystyle|I\_{k}^{+}(L)|^{2} | =|∑j=1∞j−p/2​jp/2​∫Ijf​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x|2\displaystyle=\Bigg|\sum\_{j=1}^{\infty}j^{-p/2}\,j^{p/2}\int\_{I\_{j}}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)dx\Bigg|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(∑j=1∞j−p)​(∑j=1∞jp​|∫Ijf​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x|2)\displaystyle\leq\Big(\sum\_{j=1}^{\infty}j^{-p}\Big)\Bigg(\sum\_{j=1}^{\infty}j^{p}\Big|\int\_{I\_{j}}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)dx\Big|^{2}\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ζ​(p)​∑j=1∞jp​|∫Ijf​(x)​cos⁡(k​π​(x+L)2​L)​𝑑x|2.\displaystyle=\zeta(p)\sum\_{j=1}^{\infty}j^{p}\Big|\int\_{I\_{j}}f(x)\cos\Big(\frac{k\pi(x+L)}{2L}\Big)dx\Big|^{2}. |  |

Summing in kk and using blockwise Parseval (orthogonality of the cosine family on an interval of length 2​L2L; any normalization discrepancy for k=0k=0 is absorbed into a factor ≤2\leq 2) yields

|  |  |  |
| --- | --- | --- |
|  | ∑k=0∞1L​|Ik+​(L)|2≤2​ζ​(p)​∑j=1∞jp​∫Ij|f​(x)|2​𝑑x.\sum\_{k=0}^{\infty}\frac{1}{L}|I\_{k}^{+}(L)|^{2}\leq 2\zeta(p)\sum\_{j=1}^{\infty}j^{p}\int\_{I\_{j}}|f(x)|^{2}dx. |  |

For x∈Ijx\in I\_{j} we have (2​j−1)​L≤x≤(2​j+1)​L(2j-1)L\leq x\leq(2j+1)L, hence j≤(x/L+1)/2j\leq(x/L+1)/2 and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | jp≤2−p​(x/L+1)p≤12​((x/L)p+1).j^{p}\leq 2^{-p}(x/L+1)^{p}\leq\tfrac{1}{2}\big((x/L)^{p}+1\big). |  | (4) |

Here we used the convexity inequality (a+b)p≤2p−1​(ap+bp)(a+b)^{p}\leq 2^{p-1}(a^{p}+b^{p}) for a,b≥0a,b\geq 0 and p>1p>1.
Thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1∞jp​∫Ij|f​(x)|2​𝑑x\displaystyle\sum\_{j=1}^{\infty}j^{p}\int\_{I\_{j}}|f(x)|^{2}dx | ≤12​L−p​∫x≥L|x|p​|f​(x)|2​𝑑x+12​∫x≥L|f​(x)|2​𝑑x.\displaystyle\leq\tfrac{1}{2}L^{-p}\int\_{x\geq L}|x|^{p}|f(x)|^{2}dx+\tfrac{1}{2}\int\_{x\geq L}|f(x)|^{2}dx. |  |

Combining gives for the positive tail

|  |  |  |
| --- | --- | --- |
|  | ∑k=0∞1L​|Ik+​(L)|2≤ζ​(p)​(L−p​∫x≥L|x|p​|f​(x)|2​𝑑x+∫x≥L|f​(x)|2​𝑑x).\sum\_{k=0}^{\infty}\frac{1}{L}|I\_{k}^{+}(L)|^{2}\leq\zeta(p)\Big(L^{-p}\int\_{x\geq L}|x|^{p}|f(x)|^{2}dx+\int\_{x\geq L}|f(x)|^{2}dx\Big). |  |

The negative tail x<−Lx<-L is handled identically (replace xx by −x-x), producing the same bound. Adding the two contributions yields ([1](https://arxiv.org/html/2512.02745v1#S3.E1 "In Proposition 1 (Moment-based COS bound). ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence")).

To obtain the rate, note that for |x|>L|x|>L we have |x|p≥Lp|x|^{p}\geq L^{p}, hence

|  |  |  |
| --- | --- | --- |
|  | ∫|x|>L|f​(x)|2​𝑑x≤L−p​∫|x|>L|x|p​|f​(x)|2​𝑑x≤L−p​∫ℝ|x|p​|f​(x)|2​𝑑x.\int\_{|x|>L}|f(x)|^{2}dx\leq L^{-p}\int\_{|x|>L}|x|^{p}|f(x)|^{2}dx\leq L^{-p}\int\_{\mathbb{R}}|x|^{p}|f(x)|^{2}dx. |  |

Applying the same bound to the first term in ([1](https://arxiv.org/html/2512.02745v1#S3.E1 "In Proposition 1 (Moment-based COS bound). ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence")) shows

|  |  |  |
| --- | --- | --- |
|  | B​(L)≤4​ζ​(p)​L−p​∫|x|>L|x|p​|f​(x)|2​𝑑x,B(L)\leq 4\zeta(p)L^{-p}\int\_{|x|>L}|x|^{p}|f(x)|^{2}dx, |  |

which is ([2](https://arxiv.org/html/2512.02745v1#S3.E2 "In Proposition 1 (Moment-based COS bound). ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence")). Dropping the restriction |x|>L|x|>L gives ([3](https://arxiv.org/html/2512.02745v1#S3.E3 "In Proposition 1 (Moment-based COS bound). ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence")). Thus B​(L)=O​(L−p)B(L)=O(L^{-p}) with explicit constant 4​ζ​(p)​∫ℝ|x|p​|f​(x)|2​𝑑x4\zeta(p)\int\_{\mathbb{R}}|x|^{p}|f(x)|^{2}dx. (Refining k=0k=0 normalization can reduce the factor.) Since |x|p​|f​(x)|2∈L1|x|^{p}|f(x)|^{2}\in L^{1}, the bound also implies B​(L)→0B(L)\to 0.
∎

###### Corollary 1 (Bounded density with finite (1+ε)(1+\varepsilon) moment).

Let ff be a bounded pdf, i.e. 0≤f≤M0\leq f\leq M for some M>0M>0.
Assume that for some ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ|x| 1+ε​f​(x)​𝑑x=m<∞.\int\_{\mathbb{R}}|x|^{\,1+\varepsilon}\,f(x)\,dx=m<\infty. |  |

Then ff satisfies the moment condition of Proposition [1](https://arxiv.org/html/2512.02745v1#Thmprop1 "Proposition 1 (Moment-based COS bound). ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence"), and is
therefore COS-admissible with explicit rate

|  |  |  |
| --- | --- | --- |
|  | B​(L)≤ 4​ζ​(1+ε)​M​m​L−1−ε.B(L)\;\leq\;4\zeta(1+\varepsilon)MmL^{-1-\varepsilon}. |  |

###### Proof of Corollary.

Apply Proposition [1](https://arxiv.org/html/2512.02745v1#Thmprop1 "Proposition 1 (Moment-based COS bound). ‣ 3 Generalized Moment Bound ‣ A Note on the Conditions for COS Convergence") with p=1+εp=1+\varepsilon. Boundedness gives |x| 1+ε​f​(x)2≤M​|x| 1+ε​f​(x)|x|^{\,1+\varepsilon}f(x)^{2}\leq M|x|^{\,1+\varepsilon}f(x). For |x|>L|x|>L, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(L)≤\displaystyle B(L)\leq | 4​ζ​(1+ε)​L−1−ε​∫|x|>L|x| 1+ε​|f​(x)|2​𝑑x\displaystyle 4\zeta(1+\varepsilon)L^{-1-\varepsilon}\int\_{|x|>L}|x|^{\,1+\varepsilon}|f(x)|^{2}dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 4​ζ​(1+ε)​L−1−ε​M​∫|x|>L|x| 1+ε​f​(x)​𝑑x\displaystyle 4\zeta(1+\varepsilon)L^{-1-\varepsilon}M\int\_{|x|>L}|x|^{\,1+\varepsilon}f(x)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 4​ζ​(1+ε)​M​m​L−1−ε.\displaystyle 4\zeta(1+\varepsilon)MmL^{-1-\varepsilon}. |  |

∎

###### Remark 1.

* •

  Finite first and second moments alone do not suffice: one can construct smooth probability densities whose ∫|x|​f\int|x|f and ∫x2​f\int x^{2}f converge while ∫f2=∞\int f^{2}=\infty, invalidating Parseval-based bounds. Boundedness (or some other strong conditions such as monotone tail decay) prevents such spike constructions.
* •

  In [junike2022precise], the authors proved that a density ff is
  COS-admissible under the assumptions

  |  |  |  |
  | --- | --- | --- |
  |  | f∈L1​(ℝ)∩L2​(ℝ)and|x|p/2​f​(x)∈L2​(ℝ)for ​p=2.f\in L^{1}(\mathbb{R})\cap L^{2}(\mathbb{R})\qquad\text{and}\qquad|x|^{p/2}f(x)\in L^{2}(\mathbb{R})\quad\text{for }p=2. |  |

  In the present work, we extend this result by showing that COS-admissibility
  already holds under the weaker requirement p>1p>1.
  This relaxation is important, since many relevant distributions satisfy our
  condition but not the stronger condition in [junike2022precise].
  For example, a Student–tt density with degrees of freedom
  0<ν≤120<\nu\leq\tfrac{1}{2} does not satisfy the condition for p=2p=2,
  whereas it does satisfy the condition for some p>1p>1.
  This is because the density of a Student–t​(ν)t(\nu) distribution satisfies
  f​(x)∼C​|x|−(ν+1)f(x)\sim C|x|^{-(\nu+1)} as |x|→∞|x|\to\infty, so
  |x|2​f​(x)2∼|x|−2​ν|x|^{2}f(x)^{2}\sim|x|^{-2\nu} is non–integrable when ν≤1/2\nu\leq 1/2,
  while |x|p​f​(x)2∼|x|−2​ν−2+p|x|^{p}f(x)^{2}\sim|x|^{-2\nu-2+p} is integrable for some p>1p>1 whenever ν>0\nu>0.

  Hence, our result provides theoretical guarantees of COS-admissibility
  for a substantially broader class of distributions.

## 4 Multidimensional Extension

The multi-dimensional COS method is introduced in [ruijter2012two]. And the similar definition and condition of the COS-admissibility for the multi-dimensional case is given in [junike2023characteristic].
We can also give a better condition under which the COS-admissibility is guaranteed for the multi-dimensional COS.

Let d≥1d\geq 1 and f:ℝd→ℝf:\mathbb{R}^{d}\to\mathbb{R} with f∈L1​(ℝd)∩L2​(ℝd)f\in L^{1}(\mathbb{R}^{d})\cap L^{2}(\mathbb{R}^{d}). Assume

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|x|p​|f​(x)|2​𝑑x<∞for some ​p>d.\int\_{\mathbb{R}^{d}}|x|^{p}|f(x)|^{2}dx<\infty\quad\text{for some }p>d. |  |

For L>0L>0 define

|  |  |  |
| --- | --- | --- |
|  | Bd​(L):=∑𝐤∈ℕ0d1Ld​|∫ℝd∖[−L,L]df​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x|2.B\_{d}(L):=\sum\_{\mathbf{k}\in\mathbb{N}\_{0}^{d}}\frac{1}{L^{d}}\Bigg|\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}f(x)\prod\_{i=1}^{d}\cos\Big(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\Big)dx\Bigg|^{2}. |  |

We say that ff is dd-dimensional COS-admissible if Bd​(L)→0B\_{d}(L)\to 0 as L→∞L\to\infty.

###### Proposition 2 (Weighted dd-dimensional COS bound).

Let d≥1d\geq 1 and let

|  |  |  |
| --- | --- | --- |
|  | f:ℝd→ℝ,f∈L1​(ℝd)∩L2​(ℝd).f:\mathbb{R}^{d}\to\mathbb{R},\qquad f\in L^{1}(\mathbb{R}^{d})\cap L^{2}(\mathbb{R}^{d}). |  |

Assume that for some p>dp>d,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|x|p​|f​(x)|2​𝑑x<∞.\int\_{\mathbb{R}^{d}}|x|^{p}\,|f(x)|^{2}\,dx<\infty. |  |

Then ff is dd-dimensional COS-admissible: Bd​(L)→0B\_{d}(L)\to 0 as L→∞L\to\infty.
More precisely,

|  |  |  |
| --- | --- | --- |
|  | Bd​(L)≤Cd,p​L−p​∫ℝd∖[−L,L]d|x|p​|f​(x)|2​𝑑x.B\_{d}(L)\leq C\_{d,p}L^{-p}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|x|^{p}|f(x)|^{2}\,dx. |  |

where

|  |  |  |
| --- | --- | --- |
|  | Cd,p=2d−1​(1+dp/2)​∑m∈ℤd∖{0}|m|−p<∞.C\_{d,p}=2^{d-1}(1+d^{p/2})\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{-p}<\infty. |  |

###### Proof.

We first decompose the complement of the cube [−L,L]d[-L,L]^{d} into disjoint cubes of side length 2​L2L.
For each integer vector m=(m1,…,md)∈ℤdm=(m\_{1},\dots,m\_{d})\in\mathbb{Z}^{d}, define

|  |  |  |
| --- | --- | --- |
|  | Qm=∏i=1d[(2​mi−1)​L,(2​mi+1)​L].Q\_{m}=\prod\_{i=1}^{d}[(2m\_{i}-1)L,\,(2m\_{i}+1)L]. |  |

Then Q0=[−L,L]dQ\_{0}=[-L,L]^{d}, and all other cubes tile the complement:

|  |  |  |
| --- | --- | --- |
|  | ℝd∖[−L,L]d=⨆m∈ℤd∖{0}Qm.\mathbb{R}^{d}\setminus[-L,L]^{d}=\bigsqcup\_{m\in\mathbb{Z}^{d}\setminus\{0\}}Q\_{m}. |  |

For 𝐤=(k1,…,kd)∈ℕ0d\mathbf{k}=(k\_{1},\dots,k\_{d})\in\mathbb{N}\_{0}^{d} define

|  |  |  |
| --- | --- | --- |
|  | I𝐤​(L)=∫ℝd∖[−L,L]df​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x.I\_{\mathbf{k}}(L)=\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx. |  |

Using the partition,

|  |  |  |
| --- | --- | --- |
|  | I𝐤​(L)=∑m∈ℤd∖{0}∫Qmf​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x.I\_{\mathbf{k}}(L)=\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}\int\_{Q\_{m}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx. |  |

Let |m|≔(m12+⋯+md2)1/2|m|\coloneqq(m\_{1}^{2}+\cdots+m\_{d}^{2})^{1/2} denote the Euclidean norm of of mm. Apply Cauchy–Schwarz with weights |m|−p/2|m|^{-p/2} and |m|p/2|m|^{p/2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |I𝐤​(L)|2\displaystyle|I\_{\mathbf{k}}(L)|^{2} | =|∑m∈ℤd∖{0}|m|−p/2​(|m|p/2​∫Qmf​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x)|2\displaystyle=\left|\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{-p/2}\;\Big(|m|^{p/2}\!\int\_{Q\_{m}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx\Big)\right|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(∑m∈ℤd∖{0}|m|−p)​(∑m∈ℤd∖{0}|m|p​|∫Qmf​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x|2).\displaystyle\leq\left(\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{-p}\right)\left(\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{p}\left|\int\_{Q\_{m}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx\right|^{2}\right). |  |

Let

|  |  |  |
| --- | --- | --- |
|  | Sd,p≔∑m∈ℤd∖{0}|m|−p,Sd,p<∞​(p>d).S\_{d,p}\coloneqq\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{-p},\qquad S\_{d,p}<\infty\ (p>d). |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |I𝐤​(L)|2≤Sd,p​∑m∈ℤd∖{0}|m|p​|∫Qmf​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x|2.|I\_{\mathbf{k}}(L)|^{2}\leq S\_{d,p}\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{p}\left|\int\_{Q\_{m}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx\right|^{2}. |  | (5) |

Next we sum over 𝐤\mathbf{k} and use Parseval on each cube QmQ\_{m}.
After translation, QmQ\_{m} becomes [0,2​L]d[0,2L]^{d}, and the functions

|  |  |  |
| --- | --- | --- |
|  | ∏i=1dcos⁡(ki​π​ti2​L),𝐤∈ℕ0d,\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi t\_{i}}{2L}\right),\qquad\mathbf{k}\in\mathbb{N}\_{0}^{d}, |  |

form an orthogonal system in L2​([0,2​L]d)L^{2}([0,2L]^{d}).
The normalization constants differ for ki=0k\_{i}=0, but each such factor is bounded by 22,
so the product across dd dimensions contributes at most 2d2^{d}.
Thus Parseval gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑𝐤∈ℕ0d1Ld​|∫Qmf​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x|2≤ 2d​∫Qm|f​(x)|2​𝑑x.\sum\_{\mathbf{k}\in\mathbb{N}\_{0}^{d}}\frac{1}{L^{d}}\left|\int\_{Q\_{m}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx\right|^{2}\ \leq\ 2^{d}\int\_{Q\_{m}}|f(x)|^{2}\,dx. |  | (6) |

Multiply ([5](https://arxiv.org/html/2512.02745v1#S4.E5 "In 4 Multidimensional Extension ‣ A Note on the Conditions for COS Convergence")) by L−dL^{-d} and sum over 𝐤\mathbf{k}, then apply ([6](https://arxiv.org/html/2512.02745v1#S4.E6 "In 4 Multidimensional Extension ‣ A Note on the Conditions for COS Convergence")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bd​(L)\displaystyle B\_{d}(L) | =∑𝐤∈ℕ0d|I𝐤​(L)|2Ld\displaystyle=\sum\_{\mathbf{k}\in\mathbb{N}\_{0}^{d}}\frac{|I\_{\mathbf{k}}(L)|^{2}}{L^{d}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Sd,p​∑m∈ℤd∖{0}|m|p​∑𝐤∈ℕ0d1Ld​|∫Qmf​(x)​∏i=1dcos⁡(ki​π​(xi+L)2​L)​d​x|2\displaystyle\leq S\_{d,p}\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{p}\sum\_{\mathbf{k}\in\mathbb{N}\_{0}^{d}}\frac{1}{L^{d}}\left|\int\_{Q\_{m}}f(x)\prod\_{i=1}^{d}\cos\!\left(\frac{k\_{i}\pi(x\_{i}+L)}{2L}\right)\,dx\right|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2d​Sd,p​∑m∈ℤd∖{0}|m|p​∫Qm|f​(x)|2​𝑑x.\displaystyle\leq 2^{d}S\_{d,p}\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{p}\int\_{Q\_{m}}|f(x)|^{2}dx. |  |

We now compare |m||m| and |x||x| for x∈Qmx\in Q\_{m}.
By geometry of cubes,

|  |  |  |
| --- | --- | --- |
|  | (2​|m|−d)​L≤|x|≤(2​|m|+d)​L.(2|m|-\sqrt{d})L\ \leq\ |x|\ \leq\ (2|m|+\sqrt{d})L. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | |m|≤|x|/L+d2,|m|p≤12​((|x|/L)p+dp/2),|m|\ \leq\ \frac{|x|/L+\sqrt{d}}{2},\qquad|m|^{p}\leq\frac{1}{2}\Big((|x|/L)^{p}+d^{p/2}\Big), |  |

using (a+b)p≤2p−1​(ap+bp)(a+b)^{p}\leq 2^{p-1}(a^{p}+b^{p}).

Therefore

|  |  |  |
| --- | --- | --- |
|  | ∑m∈ℤd∖{0}|m|p​∫Qm|f​(x)|2​𝑑x≤12​L−p​∫ℝd∖[−L,L]d|x|p​|f​(x)|2​𝑑x+12​dp/2​∫ℝd∖[−L,L]d|f​(x)|2​𝑑x.\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{p}\int\_{Q\_{m}}|f(x)|^{2}dx\leq\frac{1}{2}L^{-p}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|x|^{p}|f(x)|^{2}\,dx+\frac{1}{2}d^{p/2}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|f(x)|^{2}\,dx. |  |

Combining,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bd​(L)≤\displaystyle B\_{d}(L)\leq | 2d​Sd,p​[12​L−p​∫ℝd∖[−L,L]d|x|p​|f​(x)|2​𝑑x+12​dp/2​∫ℝd∖[−L,L]d|f​(x)|2​𝑑x]\displaystyle 2^{d}S\_{d,p}\left[\frac{1}{2}L^{-p}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|x|^{p}|f(x)|^{2}\,dx+\frac{1}{2}d^{p/2}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|f(x)|^{2}\,dx\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 2dSd,p[12L−p∫ℝd∖[−L,L]d|x|p|f(x)|2dx+12dp/2L−p∫ℝd∖[−L,L]d|x|p|f(x)|2dx.]\displaystyle 2^{d}S\_{d,p}\left[\frac{1}{2}L^{-p}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|x|^{p}|f(x)|^{2}\,dx+\frac{1}{2}d^{p/2}L^{-p}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|x|^{p}|f(x)|^{2}\,dx.\right] |  |

Absorbing dp/2d^{p/2} into the constant

|  |  |  |
| --- | --- | --- |
|  | Cd,p=2d​Sd,p​(12+12​dp/2)=2d−1​(1+dp/2)​∑m∈ℤd∖{0}|m|−p<∞,C\_{d,p}=2^{d}S\_{d,p}(\frac{1}{2}+\frac{1}{2}d^{p/2})=2^{d-1}(1+d^{p/2})\sum\_{m\in\mathbb{Z}^{d}\setminus\{0\}}|m|^{-p}<\infty, |  |

we obtain the stated bound:

|  |  |  |
| --- | --- | --- |
|  | Bd​(L)≤Cd,p​L−p​∫ℝd∖[−L,L]d|x|p​|f​(x)|2​𝑑x.B\_{d}(L)\leq C\_{d,p}L^{-p}\!\!\int\_{\mathbb{R}^{d}\setminus[-L,L]^{d}}|x|^{p}|f(x)|^{2}\,dx. |  |

With the condition ∫ℝd|x|p​|f​(x)|2​𝑑x<∞\int\_{\mathbb{R}^{d}}|x|^{p}\,|f(x)|^{2}\,dx<\infty, we have that Bd​(L)=O​(L−p)B\_{d}(L)=O(L^{-p}) and Bd​(L)→0B\_{d}(L)\to 0 as L→∞L\to\infty.
∎

###### Remark 2 (Rectangular truncation domains).

The COS expansion on [−L,L]d[-L,L]^{d} is used only for notational simplicity.
The proof of Proposition [2](https://arxiv.org/html/2512.02745v1#Thmprop2 "Proposition 2 (Weighted 𝑑-dimensional COS bound). ‣ 4 Multidimensional Extension ‣ A Note on the Conditions for COS Convergence") extends verbatim to
rectangular truncation domains of the form

|  |  |  |
| --- | --- | --- |
|  | [−L1,L1]×⋯×[−Ld,Ld].[-L\_{1},L\_{1}]\times\cdots\times[-L\_{d},L\_{d}]. |  |

In this case one partitions ℝd∖[−L1,L1]×⋯×[−Ld,Ld]\mathbb{R}^{d}\setminus[-L\_{1},L\_{1}]\times\cdots\times[-L\_{d},L\_{d}]
into translated boxes of side lengths 2​L1,…,2​Ld2L\_{1},\dots,2L\_{d}, and the same
Cauchy–Schwarz and blockwise Parseval arguments apply.
If mini⁡Li→∞\min\_{i}L\_{i}\to\infty, then Bd​(L1,…,Ld)→0B\_{d}(L\_{1},\dots,L\_{d})\to 0 with the same rate
O​(mini⁡Li−p)O\!\left(\min\_{i}L\_{i}^{-p}\right).
Thus COS-admissibility does not require equal truncation lengths in each dimension.

###### Remark 3.

As in the one-dimensional case, this proposition implies that any multi-variate Student-t distribution is COS-admissible.