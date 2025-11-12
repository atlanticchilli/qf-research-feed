---
authors:
- Mario Ghossoub
- David Saunders
doc_id: arxiv:2009.12838v1
family_id: arxiv:2009.12838
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2009.12838] On the Continuity of the Feasible Set Mapping in Optimal Transport'
url_abs: http://arxiv.org/abs/2009.12838v1
url_html: https://ar5iv.org/html/2009.12838v1
venue: arXiv q-fin
version: 1
year: 2020
---


Mario Ghossoub
Department of Statistics and Actuarial Science, University of Waterloo,
[mario.ghossoub@uwaterloo.ca](mailto:mario.ghossoub@uwaterloo.ca).
  
David Saunders
Corresponding author. Department of Statistics and Actuarial Science, University of Waterloo,  [dsaunders@uwaterloo.ca](mailto:dsaunders@uwaterloo.ca).

###### Abstract

Consider the set of probability measures with given marginal distributions on the product of two complete, separable metric spaces, seen as a correspondence when the marginal distributions vary. In problems of optimal transport, continuity of this correspondence from marginal to joint distributions is often desired, in light of Berge’s Maximum Theorem, to establish continuity of the value function in the marginal distributions, as well as stability of the set of optimal transport plans. Bergin [[1999](#bib.bib2)] established the continuity of this correspondence, and in this note, we present a novel and considerably shorter proof of this important result. We then examine an application to an assignment game (transferable utility matching problem) with unknown type distributions.

Keywords: Optimal transport; Measures on product spaces with fixed marginals; Continuity of correspondences on spaces of measures; Matching with transferable utility; Assignment game; Hedonic pricing.

JEL Codes: C60, C61.

## 1 Introduction

Optimization problems over sets of probability measures with given marginals, and optimal transport problems in particular, arise in several contexts in economics (see, e.g., Galichon [[2016](#bib.bib9)] for a book-length treatment, and the two special issues in volumes 42(2) and 67(2) of Economic Theory). Such ubiquitous problems can be formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈Π𝒳,𝒴​(μ,ν)​∫𝒳×𝒴Φ​(x,y)​𝑑π​(x,y),𝜋subscriptΠ  𝒳𝒴𝜇𝜈supremumsubscript𝒳𝒴Φ𝑥𝑦differential-d𝜋𝑥𝑦\underset{\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)}{\sup}\ \int\_{\mathcal{X}\times\mathcal{Y}}\Phi\left(x,y\right)\,d\pi\left(x,y\right), |  | (1.1) |

where Π𝒳,𝒴​(μ,ν)subscriptΠ

𝒳𝒴𝜇𝜈\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) denotes the set of all probability measures on a product space 𝒳×𝒴𝒳𝒴\mathcal{X}\times\mathcal{Y} with given marginal distributions μ𝜇\mu on 𝒳𝒳\mathcal{X} and ν𝜈\nu on 𝒴𝒴\mathcal{Y} (called the set of couplings of μ𝜇\mu and ν𝜈\nu), and Φ:𝒳×𝒴→ℝ:Φ→𝒳𝒴ℝ\Phi:\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R} is a given function.

Hereafter, 𝒳𝒳\mathcal{X} and 𝒴𝒴\mathcal{Y} are two Polish (i.e., complete, separable, metric) spaces, with respective Borel σ𝜎\sigma-algebras ℬ𝒳subscriptℬ𝒳\mathcal{B}\_{\mathcal{X}} and ℬ𝒴subscriptℬ𝒴\mathcal{B}\_{\mathcal{Y}}. For a Polish space 𝒮𝒮\mathcal{S},
𝒫​(𝒮)𝒫𝒮\mathcal{P}(\mathcal{S}) is the set of all Borel probability measures on 𝒮𝒮\mathcal{S}. Given μ∈𝒫​(𝒳)𝜇𝒫𝒳\mu\in\mathcal{P}(\mathcal{X}), ν∈𝒫​(𝒴)𝜈𝒫𝒴\nu\in\mathcal{P}(\mathcal{Y}), it follows that

|  |  |  |
| --- | --- | --- |
|  | Π𝒳,𝒴​(μ,ν)={π∈𝒫​(𝒳×𝒴):π​(A×Y)=μ​(A),π​(X×B)=ν​(B),∀(A,B)∈ℬ𝒳×ℬ𝒴}.subscriptΠ  𝒳𝒴𝜇𝜈conditional-set𝜋𝒫𝒳𝒴formulae-sequence𝜋𝐴𝑌𝜇𝐴formulae-sequence𝜋𝑋𝐵𝜈𝐵for-all𝐴𝐵subscriptℬ𝒳subscriptℬ𝒴\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)=\Big{\{}\pi\in\mathcal{P}(\mathcal{X}\times\mathcal{Y}):\;\pi\left(A\times Y\right)=\mu\left(A\right),\ \pi\left(X\times B\right)=\nu\left(B\right),\ \forall\left(A,B\right)\in\mathcal{B}\_{\mathcal{X}}\times\mathcal{B}\_{\mathcal{Y}}\Big{\}}. |  |

For sequences {πn}n⊂𝒫​(𝒮)subscriptsubscript𝜋𝑛𝑛𝒫𝒮\{\pi\_{n}\}\_{n}\subset\mathcal{P}(\mathcal{S}), πn→π→subscript𝜋𝑛𝜋\pi\_{n}\to\pi denotes convergence in the narrow topology on 𝒫​(𝒮)𝒫𝒮\mathcal{P}(\mathcal{S}) (i.e., ∫f​𝑑πn→∫f​𝑑π→𝑓differential-dsubscript𝜋𝑛𝑓differential-d𝜋\int f\,d\pi\_{n}\to\int f\,d\pi for all f∈Cb​(𝒮)𝑓subscript𝐶𝑏𝒮f\in C\_{b}(\mathcal{S}), the space of bounded continuous functions from 𝒮𝒮\mathcal{S} to ℝℝ\mathbb{R}), which we note is metrizable by the Prokhorov metric (e.g., Billingsley [[1999](#bib.bib3), Theorem 6.8]) on 𝒫​(𝒮)𝒫𝒮\mathcal{P}(\mathcal{S}) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d𝒫​(P,Q):=inf{ε>0:P​(A)≤Q​(Aε)+ε,∀A∈ℬ𝒮},assignsubscript𝑑𝒫𝑃𝑄infimumconditional-set𝜀0formulae-sequence𝑃𝐴𝑄superscript𝐴𝜀𝜀for-all𝐴subscriptℬ𝒮d\_{\mathcal{P}}(P,Q):=\inf\Big{\{}\varepsilon>0:\;P\left(A\right)\leq Q\left(A^{\varepsilon}\right)+\varepsilon,\ \forall A\in\mathcal{B}\_{\mathcal{S}}\Big{\}}, |  | (1.2) |

where ℬ𝒮subscriptℬ𝒮\mathcal{B}\_{\mathcal{S}} denotes the Borel σ𝜎\sigma-algebra on 𝒮𝒮\mathcal{S}, and for each A∈ℬ𝒮𝐴subscriptℬ𝒮A\in\mathcal{B}\_{\mathcal{S}},

|  |  |  |
| --- | --- | --- |
|  | Aε:={y∈𝒮:d𝒮​(x,y)<ε,for some ​x∈A}.assignsuperscript𝐴𝜀conditional-set𝑦𝒮formulae-sequencesubscript𝑑𝒮𝑥𝑦𝜀for some 𝑥𝐴A^{\varepsilon}:=\Big{\{}y\in\mathcal{S}:d\_{\mathcal{S}}\left(x,y\right)<\varepsilon,\ \hbox{for some }x\in A\Big{\}}. |  |

Then for each (μ,ν)∈𝒫​(𝒳)×𝒫​(𝒴)𝜇𝜈𝒫𝒳𝒫𝒴\left(\mu,\nu\right)\in\mathcal{P}\left(\mathcal{X}\right)\times\mathcal{P}\left(\mathcal{Y}\right), Π𝒳,𝒴​(μ,ν)subscriptΠ

𝒳𝒴𝜇𝜈\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) is nonempty, convex, and compact in the narrow topology on 𝒫​(𝒳×𝒴)𝒫𝒳𝒴\mathcal{P}(\mathcal{X}\times\mathcal{Y}) (e.g., Villani [[2003](#bib.bib14), pp. 32, 49-50]).

Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) is precisely the Monge-Kantorovich optimal transport problem. Here, we are interested in the properties of the correspondence Π𝒳,𝒴:𝒫​(𝒳)×𝒫​(𝒴)↠𝒫​(𝒳×𝒴):subscriptΠ

𝒳𝒴↠𝒫𝒳𝒫𝒴𝒫𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}}:\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y})\twoheadrightarrow\mathcal{P}(\mathcal{X}\times\mathcal{Y}). Formally, Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} associates to each pair (μ,ν)∈𝒫​(𝒳)×𝒫​(𝒴)𝜇𝜈𝒫𝒳𝒫𝒴\left(\mu,\nu\right)\in\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y}) of marginal distributions the feasibility set Π𝒳,𝒴​(μ,ν)subscriptΠ

𝒳𝒴𝜇𝜈\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) of Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")). Let G​r​(Π𝒳,𝒴)𝐺𝑟subscriptΠ

𝒳𝒴Gr\left(\Pi\_{\mathcal{X},\mathcal{Y}}\right) denote the graph of the correspondence Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}}, given by

|  |  |  |
| --- | --- | --- |
|  | G​r​(Π𝒳,𝒴):={((μ,ν),π)∈(𝒫​(𝒳)×𝒫​(𝒴))×𝒫​(𝒳×𝒴):π∈Π𝒳,𝒴​(μ,ν)}.assign𝐺𝑟subscriptΠ  𝒳𝒴conditional-set𝜇𝜈𝜋𝒫𝒳𝒫𝒴𝒫𝒳𝒴𝜋subscriptΠ  𝒳𝒴𝜇𝜈Gr\left(\Pi\_{\mathcal{X},\mathcal{Y}}\right):=\Big{\{}\left(\left(\mu,\nu\right),\pi\right)\in\left(\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y})\right)\times\mathcal{P}(\mathcal{X}\times\mathcal{Y}):\;\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)\Big{\}}. |  |

We define the linear functional Ψ:G​r​(Π𝒳,𝒴)→ℝ:Ψ→𝐺𝑟subscriptΠ

𝒳𝒴ℝ\Psi:Gr\left(\Pi\_{\mathcal{X},\mathcal{Y}}\right)\rightarrow\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​((μ,ν),π):=∫𝒳×𝒴Φ​(x,y)​𝑑π​(x,y).assignΨ𝜇𝜈𝜋subscript𝒳𝒴Φ𝑥𝑦differential-d𝜋𝑥𝑦\Psi\left(\left(\mu,\nu\right),\pi\right):=\int\_{\mathcal{X}\times\mathcal{Y}}\Phi\left(x,y\right)\,d\pi\left(x,y\right). |  | (1.3) |

Furthermore, we define the value function V:𝒳×𝒴→ℝ:𝑉→𝒳𝒴ℝV:\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R} for Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(μ,ν):=supπ∈Π𝒳,𝒴​(μ,ν)​Ψ​((μ,ν),π).assign𝑉𝜇𝜈𝜋subscriptΠ  𝒳𝒴𝜇𝜈supremumΨ𝜇𝜈𝜋V\left(\mu,\nu\right):=\underset{\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)}{\sup}\Psi\left(\left(\mu,\nu\right),\pi\right). |  | (1.4) |

Finally, we define the correspondence ℳ:𝒫​(𝒳)×𝒫​(𝒴)↠𝒫​(𝒳×𝒴):ℳ↠𝒫𝒳𝒫𝒴𝒫𝒳𝒴\mathcal{M}:\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y})\twoheadrightarrow\mathcal{P}(\mathcal{X}\times\mathcal{Y}), which assigns to each given pair of marginal distributions (μ,ν)𝜇𝜈\left(\mu,\nu\right) the set of optimizers of Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")), by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ:={π∗∈Π𝒳,𝒴​(μ,ν):Ψ​((μ,ν),π∗)=V​(μ,ν)}.assignℳconditional-setsuperscript𝜋subscriptΠ  𝒳𝒴𝜇𝜈Ψ𝜇𝜈superscript𝜋𝑉𝜇𝜈\mathcal{M}:=\Big{\{}\pi^{\*}\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right):\;\Psi\left(\left(\mu,\nu\right),\pi^{\*}\right)=V\left(\mu,\nu\right)\Big{\}}. |  | (1.5) |

Note that, by the Monge-Katorovich Duality Theorem (e.g., Villani [[2003](#bib.bib14), Theorem 1.3]), nonemptiness of ℳℳ\mathcal{M} follows from the upper-semicontinuity of the function ΦΦ\Phi, as long as there are lower-semicontinuous functions a∈L1​(𝒳,ℬ𝒳,μ)𝑎superscript𝐿1𝒳subscriptℬ𝒳𝜇a\in L^{1}\left(\mathcal{X},\mathcal{B}\_{\mathcal{X}},\mu\right) and b∈L1​(𝒴,ℬ𝒴,ν)𝑏superscript𝐿1𝒴subscriptℬ𝒴𝜈b\in L^{1}\left(\mathcal{Y},\mathcal{B}\_{\mathcal{Y}},\nu\right) such that Φ​(x,y)≤a​(x)+b​(y)Φ𝑥𝑦𝑎𝑥𝑏𝑦\Phi\left(x,y\right)\leq a\left(x\right)+b\left(y\right), for μ𝜇\mu-a.e. x𝑥x and ν𝜈\nu-a.e. y𝑦y.

One is typically interested in properties of the correspondences Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} and ℳℳ\mathcal{M}, as well as continuity of the value function V𝑉V, which is important when approximating Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) in practice. Moreover, while it is immediate to see that Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} has nonempty, convex, and compact values in the narrow topology on 𝒫​(𝒳×𝒴)𝒫𝒳𝒴\mathcal{P}(\mathcal{X}\times\mathcal{Y}), the continuity of Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} is of primary concern, in light of Berge’s Maximum Theorem. Indeed, since Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} has nonempty compact values, and since 𝒫​(𝒳×𝒴)𝒫𝒳𝒴\mathcal{P}(\mathcal{X}\times\mathcal{Y}) is Hausdorff, being metrizable, continuity of the value function of Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) and upper hemicontinuity of the correspondence ℳℳ\mathcal{M} would follow from continuity of the correspondence Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}}, under mild regularity conditions on the function ΦΦ\Phi.

Bergin [[1999](#bib.bib2)] and Savchenko and Zarichnyi [[2014](#bib.bib12)] provided proofs of the continuity of the feasible set correspondence Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} based on rather lengthy arguments. In this paper, we present in Section [2](#S2 "2 Continuity of the Feasible Set Correspondence Π_{𝒳,𝒴} ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") an alternative, much shorter proof of this important result, using well-known measure theoretic tools. We then examine in Section [3](#S3 "3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") an application to a canonical matching problem with transferable utility.

## 2 Continuity of the Feasible Set Correspondence Π𝒳,𝒴subscriptΠ 𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}}

We will make use of the following two results. The first can be found in Ethier and Kurtz [[2005](#bib.bib8), Theorem 3.1.2]), and it provides a useful alternative characterization of the metrizability of narrow convergence. The second can be found in Villani [[2003](#bib.bib14), pp. 208-210]), and it is often referred to as the Gluing Lemma.

###### Lemma 2.1.

Let (𝒮,d𝒮)𝒮subscript𝑑𝒮\left(\mathcal{S},d\_{\mathcal{S}}\right) be a Polish space with Borel σ𝜎\sigma-algebra ℬ𝒮subscriptℬ𝒮\mathcal{B}\_{\mathcal{S}} and let d𝒫subscript𝑑𝒫d\_{\mathcal{P}} denote the Prokhorov metric on 𝒫​(𝒮)𝒫𝒮\mathcal{P}(\mathcal{S}), defined in eq. ([1.2](#S1.E2 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | d𝒫(P,Q)=infm∈Π𝒮,𝒮​(μ,ν)inf{ε>0:m[(x,y):d𝒮(x,y)≥ε]≤ε}.d\_{\mathcal{P}}(P,Q)=\inf\_{m\in\Pi\_{\mathcal{S},\mathcal{S}}\left(\mu,\nu\right)}\inf\Big{\{}\varepsilon>0:\;m[(x,y):d\_{\mathcal{S}}(x,y)\geq\varepsilon]\leq\varepsilon\Big{\}}. |  | (2.1) |

###### Lemma 2.2 (Gluing Lemma).

Let v1subscript𝑣1v\_{1}, v2subscript𝑣2v\_{2}, v3subscript𝑣3v\_{3} be three probability measures supported in Polish spaces 𝒮1subscript𝒮1\mathcal{S}\_{1}, 𝒮2subscript𝒮2\mathcal{S}\_{2}, 𝒮3subscript𝒮3\mathcal{S}\_{3} respectively, and let m12∈Π𝒮1,𝒮2​(v1,v2)subscript𝑚12subscriptΠ

subscript𝒮1subscript𝒮2subscript𝑣1subscript𝑣2m\_{12}\in\Pi\_{\mathcal{S}\_{1},\mathcal{S}\_{2}}\left(v\_{1},v\_{2}\right) and m23∈Π𝒮2,𝒮3​(v2,v3)subscript𝑚23subscriptΠ

subscript𝒮2subscript𝒮3subscript𝑣2subscript𝑣3m\_{23}\in\Pi\_{\mathcal{S}\_{2},\mathcal{S}\_{3}}\left(v\_{2},v\_{3}\right) be two transference plans. Then there exists a probability measure m∈𝒫​(𝒮1×𝒮2×𝒮3)𝑚𝒫subscript𝒮1subscript𝒮2subscript𝒮3m\in\mathcal{P}(\mathcal{S}\_{1}\times\mathcal{S}\_{2}\times\mathcal{S}\_{3}) with marginals m12subscript𝑚12m\_{12} on 𝒮1×𝒮2subscript𝒮1subscript𝒮2\mathcal{S}\_{1}\times\mathcal{S}\_{2} and m23subscript𝑚23m\_{23} on 𝒮2×𝒮3subscript𝒮2subscript𝒮3\mathcal{S}\_{2}\times\mathcal{S}\_{3}. That is, if ℬ𝒮1×𝒮2subscriptℬsubscript𝒮1subscript𝒮2\mathcal{B}\_{\mathcal{S}\_{1}\times\mathcal{S}\_{2}} and ℬ𝒮2×𝒮3subscriptℬsubscript𝒮2subscript𝒮3\mathcal{B}\_{\mathcal{S}\_{2}\times\mathcal{S}\_{3}} denote the Borel σ𝜎\sigma-algebras of 𝒮1×𝒮2subscript𝒮1subscript𝒮2\mathcal{S}\_{1}\times\mathcal{S}\_{2} and 𝒮2×𝒮3subscript𝒮2subscript𝒮3\mathcal{S}\_{2}\times\mathcal{S}\_{3}, respectively, then

|  |  |  |
| --- | --- | --- |
|  | m​(A×𝒮3)=m12​(A),m​(𝒮1×B)=m23​(B),∀(A,B)∈ℬ𝒮1×𝒮2×ℬ𝒮2×𝒮3.formulae-sequence𝑚𝐴subscript𝒮3subscript𝑚12𝐴formulae-sequence𝑚subscript𝒮1𝐵subscript𝑚23𝐵for-all𝐴𝐵subscriptℬsubscript𝒮1subscript𝒮2subscriptℬsubscript𝒮2subscript𝒮3m\left(A\times\mathcal{S}\_{3}\right)=m\_{12}\left(A\right),\ m\left(\mathcal{S}\_{1}\times B\right)=m\_{23}\left(B\right),\ \forall\left(A,B\right)\in\mathcal{B}\_{\mathcal{S}\_{1}\times\mathcal{S}\_{2}}\times\mathcal{B}\_{\mathcal{S}\_{2}\times\mathcal{S}\_{3}}. |  |

###### Theorem 2.3.

The correspondence Π𝒳,𝒴:𝒫​(𝒳)×𝒫​(𝒴)↠𝒫​(𝒳×𝒴):subscriptΠ

𝒳𝒴↠𝒫𝒳𝒫𝒴𝒫𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}}:\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y})\twoheadrightarrow\mathcal{P}(\mathcal{X}\times\mathcal{Y}) is continuous, and has nonempty, convex, and compact values in the narrow topology on 𝒫​(𝒳×𝒴)𝒫𝒳𝒴\mathcal{P}(\mathcal{X}\times\mathcal{Y}).

###### Proof.

First, note that for every (μ,ν)∈𝒫​(𝒳)×𝒫​(𝒴)𝜇𝜈𝒫𝒳𝒫𝒴\left(\mu,\nu\right)\in\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y}), Π𝒳,𝒴​(μ,ν)≠∅subscriptΠ

𝒳𝒴𝜇𝜈\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)\neq\varnothing, since the tensor product μ⊗νtensor-product𝜇𝜈\mu\otimes\nu belongs to Π𝒳,𝒴​(μ,ν)subscriptΠ

𝒳𝒴𝜇𝜈\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right). Moreover, Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} trivially has convex values. Compactness of the values of Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} in the narrow topology on 𝒫​(𝒳×𝒴)𝒫𝒳𝒴\mathcal{P}(\mathcal{X}\times\mathcal{Y}) is shown in Villani [[2003](#bib.bib14), pp. 49-50], for instance. We now show continuity of Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}}.

To show upper hemicontinuity, suppose that we have {((μn,νn),πn)}n⊂G​r​(Π𝒳,𝒴)subscriptsubscript𝜇𝑛subscript𝜈𝑛subscript𝜋𝑛𝑛𝐺𝑟subscriptΠ

𝒳𝒴\{\left(\left(\mu\_{n},\nu\_{n}\right),\pi\_{n}\right)\}\_{n}\subset Gr\left(\Pi\_{\mathcal{X},\mathcal{Y}}\right), with μn→μ→subscript𝜇𝑛𝜇\mu\_{n}\to\mu and νn→ν→subscript𝜈𝑛𝜈\nu\_{n}\to\nu. Hence, {μn}nsubscriptsubscript𝜇𝑛𝑛\{\mu\_{n}\}\_{n} and {νn}nsubscriptsubscript𝜈𝑛𝑛\{\nu\_{n}\}\_{n} and tight, by Prokhorov’s Theorem (e.g., Billingsley [[1999](#bib.bib3), Theorems 5.1-5.2]). Tightness of {μn}nsubscriptsubscript𝜇𝑛𝑛\{\mu\_{n}\}\_{n} and {νn}nsubscriptsubscript𝜈𝑛𝑛\{\nu\_{n}\}\_{n} implies that of {πn}nsubscriptsubscript𝜋𝑛𝑛\{\pi\_{n}\}\_{n}, so that by Prokhorov’s Theorem there exists a convergent subsequence πnk→π→subscript𝜋subscript𝑛𝑘𝜋\pi\_{n\_{k}}\to\pi. For any (f,g)∈Cb​(𝒳)×Cb​(𝒴)𝑓𝑔subscript𝐶𝑏𝒳subscript𝐶𝑏𝒴\left(f,g\right)\in C\_{b}(\mathcal{X})\times C\_{b}(\mathcal{Y}), we have

|  |  |  |
| --- | --- | --- |
|  | ∫f​𝑑π=limk→∞∫f​𝑑πnk=limk→∞∫f​𝑑μnk=∫f​𝑑μ;∫g​𝑑π=limk→∞∫g​𝑑πnk=limk→∞∫g​𝑑νnk=∫g​𝑑ν.formulae-sequence𝑓differential-d𝜋subscript→𝑘𝑓differential-dsubscript𝜋subscript𝑛𝑘subscript→𝑘𝑓differential-dsubscript𝜇subscript𝑛𝑘𝑓differential-d𝜇𝑔differential-d𝜋subscript→𝑘𝑔differential-dsubscript𝜋subscript𝑛𝑘subscript→𝑘𝑔differential-dsubscript𝜈subscript𝑛𝑘𝑔differential-d𝜈\begin{split}&\int f\,d\pi=\lim\_{k\to\infty}\int f\,d\pi\_{n\_{k}}=\lim\_{k\to\infty}\int f\,d\mu\_{n\_{k}}=\int f\,d\mu;\\ &\int g\,d\pi=\lim\_{k\to\infty}\int g\,d\pi\_{n\_{k}}=\lim\_{k\to\infty}\int g\,d\nu\_{n\_{k}}=\int g\,d\nu.\end{split} |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | ∫𝒳×𝒴[f+g]​𝑑π=∫𝒳f​𝑑μ+∫𝒴g​𝑑ν,subscript𝒳𝒴delimited-[]𝑓𝑔differential-d𝜋subscript𝒳𝑓differential-d𝜇subscript𝒴𝑔differential-d𝜈\int\_{\mathcal{X}\times\mathcal{Y}}\left[f+g\right]\,d\pi=\int\_{\mathcal{X}}f\,d\mu+\int\_{\mathcal{Y}}g\,d\nu, |  |

and since 𝒳,𝒴

𝒳𝒴\mathcal{X},\mathcal{Y} are Polish spaces, it follows from Villani [[2003](#bib.bib14), p. 18] that π∈Π𝒳,𝒴​(μ,ν)𝜋subscriptΠ

𝒳𝒴𝜇𝜈\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right).

To show lower hemicontinuity, fix π∈Π𝒳,𝒴​(μ,ν)𝜋subscriptΠ

𝒳𝒴𝜇𝜈\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) and suppose that we have {(μn,νn)}n⊂𝒫​(𝒳)×𝒫​(𝒴)subscriptsubscript𝜇𝑛subscript𝜈𝑛𝑛𝒫𝒳𝒫𝒴\{\left(\mu\_{n},\nu\_{n}\right)\}\_{n}\subset\mathcal{P}(\mathcal{X})\times\mathcal{P}(\mathcal{Y}), with μn→μ→subscript𝜇𝑛𝜇\mu\_{n}\to\mu and νn→ν→subscript𝜈𝑛𝜈\nu\_{n}\to\nu. Since μn→μ→subscript𝜇𝑛𝜇\mu\_{n}\to\mu, it follows that d𝒫​(μn,μ)→0→subscript𝑑𝒫subscript𝜇𝑛𝜇0d\_{\mathcal{P}}(\mu\_{n},\mu)\to 0, where d𝒫subscript𝑑𝒫d\_{\mathcal{P}} denotes the Prokhorov metric, characterized in Lemma [2.1](#S2.Thmtheorem1 "Lemma 2.1. ‣ 2 Continuity of the Feasible Set Correspondence Π_{𝒳,𝒴} ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport"). Fix n𝑛n, let 0<εn≤d𝒫​(μn,μ)+1n0subscript𝜀𝑛subscript𝑑𝒫subscript𝜇𝑛𝜇1𝑛0<\varepsilon\_{n}\leq d\_{\mathcal{P}}(\mu\_{n},\mu)+\tfrac{1}{n}, and let v1,n∈Π𝒳,𝒳​(μn,μ)subscript𝑣

1𝑛subscriptΠ

𝒳𝒳subscript𝜇𝑛𝜇v\_{1,n}\in\Pi\_{\mathcal{X},\mathcal{X}}(\mu\_{n},\mu) be such that v1,n[(x,x′):d𝒳(x,x′)≥εn]≤εnv\_{1,n}\left[(x,x^{\prime}):d\_{\mathcal{X}}(x,x^{\prime})\geq\varepsilon\_{n}\right]\leq\varepsilon\_{n}. Applying Lemma [2.2](#S2.Thmtheorem2 "Lemma 2.2 (Gluing Lemma). ‣ 2 Continuity of the Feasible Set Correspondence Π_{𝒳,𝒴} ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") with 𝒮i=𝒳subscript𝒮𝑖𝒳\mathcal{S}\_{i}=\mathcal{X} for i=1,2𝑖

12i=1,2, 𝒮3=𝒴subscript𝒮3𝒴\mathcal{S}\_{3}=\mathcal{Y}, π12=v1,nsubscript𝜋12subscript𝑣

1𝑛\pi\_{12}=v\_{1,n}, and π23=πsubscript𝜋23𝜋\pi\_{23}=\pi, we obtain a measure m1,nsubscript𝑚

1𝑛m\_{1,n} on 𝒳×𝒳×𝒴𝒳𝒳𝒴\mathcal{X}\times\mathcal{X}\times\mathcal{Y} with the required “bivariate” marginal distributions.

Similarly, let 0<δn≤d𝒫​(ν,νn)+1n0subscript𝛿𝑛subscript𝑑𝒫𝜈subscript𝜈𝑛1𝑛0<\delta\_{n}\leq d\_{\mathcal{P}}(\nu,\nu\_{n})+\tfrac{1}{n} and v2,n∈Π𝒴,𝒴​(ν,νn)subscript𝑣

2𝑛subscriptΠ

𝒴𝒴𝜈subscript𝜈𝑛v\_{2,n}\in\Pi\_{\mathcal{Y},\mathcal{Y}}\left(\nu,\nu\_{n}\right) be such that v2,n[(y,y′):d𝒴(y,y′)≥δn]≤δnv\_{2,n}[(y,y^{\prime}):d\_{\mathcal{Y}}(y,y^{\prime})\geq\delta\_{n}]\leq\delta\_{n}. Apply Lemma [2.2](#S2.Thmtheorem2 "Lemma 2.2 (Gluing Lemma). ‣ 2 Continuity of the Feasible Set Correspondence Π_{𝒳,𝒴} ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") again with 𝒮1=𝒳×𝒳subscript𝒮1𝒳𝒳\mathcal{S}\_{1}=\mathcal{X}\times\mathcal{X}, 𝒮2=𝒮3=𝒴subscript𝒮2subscript𝒮3𝒴\mathcal{S}\_{2}=\mathcal{S}\_{3}=\mathcal{Y}, π12=m1,nsubscript𝜋12subscript𝑚

1𝑛\pi\_{12}=m\_{1,n}, and π23=v2,nsubscript𝜋23subscript𝑣

2𝑛\pi\_{23}=v\_{2,n} to obtain a measure mnsubscript𝑚𝑛m\_{n} on 𝒳×𝒳×𝒴×𝒴𝒳𝒳𝒴𝒴\mathcal{X}\times\mathcal{X}\times\mathcal{Y}\times\mathcal{Y} with “univariate” marginal distributions μn,μ,ν,νn

subscript𝜇𝑛𝜇𝜈subscript𝜈𝑛\mu\_{n},\mu,\nu,\nu\_{n} and “bivariate” marginal distributions v1,nsubscript𝑣

1𝑛v\_{1,n} for the first and second components, π𝜋\pi for the second and third components, and v2,nsubscript𝑣

2𝑛v\_{2,n} for the third and fourth components.

Let πnsubscript𝜋𝑛\pi\_{n} denote the “bivariate” marginal distribution (on 𝒳×𝒴𝒳𝒴\mathcal{X}\times\mathcal{Y}) of the first and fourth components (so that πn∈Π𝒳,𝒴​(μn,νn)subscript𝜋𝑛subscriptΠ

𝒳𝒴subscript𝜇𝑛subscript𝜈𝑛\pi\_{n}\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu\_{n},\nu\_{n}\right)), and consider the measure m~nsubscript~𝑚𝑛\widetilde{m}\_{n} on (𝒳×𝒴)×(𝒳×𝒴)𝒳𝒴𝒳𝒴(\mathcal{X}\times\mathcal{Y})\times(\mathcal{X}\times\mathcal{Y}) with marginals (πn,π)subscript𝜋𝑛𝜋(\pi\_{n},\pi) that is the image of mnsubscript𝑚𝑛m\_{n} under the
mapping σ​(x1,x2,y1,y2)=(x1,y2,x2,y1)𝜎subscript𝑥1subscript𝑥2subscript𝑦1subscript𝑦2subscript𝑥1subscript𝑦2subscript𝑥2subscript𝑦1\sigma(x\_{1},x\_{2},y\_{1},y\_{2})=(x\_{1},y\_{2},x\_{2},y\_{1}). Metrize the product space using

|  |  |  |
| --- | --- | --- |
|  | d𝒳×𝒴​((x,y),(x′,y′)):=max⁡(d𝒳​(x,x′),d𝒴​(y,y′)),assignsubscript𝑑𝒳𝒴𝑥𝑦superscript𝑥′superscript𝑦′subscript𝑑𝒳𝑥superscript𝑥′subscript𝑑𝒴𝑦superscript𝑦′d\_{\mathcal{X}\times\mathcal{Y}}((x,y),(x^{\prime},y^{\prime})):=\max(d\_{\mathcal{X}}(x,x^{\prime}),d\_{\mathcal{Y}}(y,y^{\prime})), |  |

so that {d𝒳×𝒴((x,y),(x′,y′))≥c}⟹{d𝒳(x,x′)≥c\Big{\{}d\_{\mathcal{X}\times\mathcal{Y}}((x,y),(x^{\prime},y^{\prime}))\geq c\Big{\}}\Longrightarrow\Big{\{}d\_{\mathcal{X}}(x,x^{\prime})\geq c or d𝒴​(y,y′)≥csubscript𝑑𝒴𝑦superscript𝑦′𝑐d\_{\mathcal{Y}}(y,y^{\prime})\geq c}. Then

|  |  |  |
| --- | --- | --- |
|  | m~​[d𝒳×𝒴​((x,y),(x′,y′))≥εn+δn]≤m~​[d𝒳​(x,x′)≥εn+δn]+m~​[d𝒴​(y,y′)≥εn+δn]≤m~​[d𝒳​(x,x′)≥εn]+m~​[d𝒴​(y,y′)≥δn]≤εn+δn.~𝑚delimited-[]subscript𝑑𝒳𝒴𝑥𝑦superscript𝑥′superscript𝑦′subscript𝜀𝑛subscript𝛿𝑛~𝑚delimited-[]subscript𝑑𝒳𝑥superscript𝑥′subscript𝜀𝑛subscript𝛿𝑛~𝑚delimited-[]subscript𝑑𝒴𝑦superscript𝑦′subscript𝜀𝑛subscript𝛿𝑛~𝑚delimited-[]subscript𝑑𝒳𝑥superscript𝑥′subscript𝜀𝑛~𝑚delimited-[]subscript𝑑𝒴𝑦superscript𝑦′subscript𝛿𝑛subscript𝜀𝑛subscript𝛿𝑛\begin{split}\widetilde{m}[d\_{\mathcal{X}\times\mathcal{Y}}((x,y),(x^{\prime},y^{\prime}))\geq\varepsilon\_{n}+\delta\_{n}]&\leq\widetilde{m}[d\_{\mathcal{X}}(x,x^{\prime})\geq\varepsilon\_{n}+\delta\_{n}]+\widetilde{m}[d\_{\mathcal{Y}}(y,y^{\prime})\geq\varepsilon\_{n}+\delta\_{n}]\\ &\leq\widetilde{m}[d\_{\mathcal{X}}(x,x^{\prime})\geq\varepsilon\_{n}]+\widetilde{m}[d\_{\mathcal{Y}}(y,y^{\prime})\geq\delta\_{n}]\\ &\leq\varepsilon\_{n}+\delta\_{n}.\end{split} |  |

Thus d𝒫​(πn,π)≤εn+δnsubscript𝑑𝒫subscript𝜋𝑛𝜋subscript𝜀𝑛subscript𝛿𝑛d\_{\mathcal{P}}(\pi\_{n},\pi)\leq\varepsilon\_{n}+\delta\_{n} , πn∈Π𝒳,𝒴​(μn,νn)subscript𝜋𝑛subscriptΠ

𝒳𝒴subscript𝜇𝑛subscript𝜈𝑛\pi\_{n}\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu\_{n},\nu\_{n}\right), and πn→π→subscript𝜋𝑛𝜋\pi\_{n}\to\pi.
∎

## 3 TU Matching with Unknown Type Distributions

We consider a canonical example of a matching problem with transferable utility, or assignment game (Shapley and Shubik [[1971](#bib.bib13)]), in which a central planner seeks to assign an element x𝑥x from a population 𝒳𝒳\mathcal{X} to an element y𝑦y from a population 𝒴𝒴\mathcal{Y}. Both 𝒳𝒳\mathcal{X} and 𝒴𝒴\mathcal{Y} can be multidimensional, and we take them to be generic nonempty Polish spaces. The spaces 𝒳𝒳\mathcal{X} and 𝒴𝒴\mathcal{Y} are equipped with Borel probability measures μ𝜇\mu and ν𝜈\nu, respectively, representing the distribution of agents’ types over the respective spaces. Let Φ:𝒳×𝒴→ℝ:Φ→𝒳𝒴ℝ\Phi:\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R} denote the joint utility (or surplus) function, whereby Φ​(x,y)Φ𝑥𝑦\Phi\left(x,y\right) is the joint surplus generated if x∈𝒳𝑥𝒳x\in\mathcal{X} is matched with y∈𝒴𝑦𝒴y\in\mathcal{Y}. For instance, μ𝜇\mu can denote the distribution of skills over a set 𝒳𝒳\mathcal{X} for a population of workers, ν𝜈\nu the distribution of firm characteristics over a set 𝒴𝒴\mathcal{Y}, and Φ​(x,y)Φ𝑥𝑦\Phi\left(x,y\right) denotes the value created if a worker with skill x∈𝒳𝑥𝒳x\in\mathcal{X} is employed by a firm with characteristic y∈𝒴𝑦𝒴y\in\mathcal{Y}.

Following Chiappori et al. [[2010](#bib.bib4)], an assignment of x∈𝒳𝑥𝒳x\in\mathcal{X} to y∈𝒴𝑦𝒴y\in\mathcal{Y} is a probability measure π∈Π𝒳,𝒴​(μ,ν)𝜋subscriptΠ

𝒳𝒴𝜇𝜈\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) with support s​u​p​p​(π)⊂𝒳×𝒴𝑠𝑢𝑝𝑝𝜋𝒳𝒴supp\left(\pi\right)\subset\mathcal{X}\times\mathcal{Y}, which leads to an economic value, or total surplus of

|  |  |  |
| --- | --- | --- |
|  | ∫𝒳×𝒴Φ​(x,y)​𝑑π​(x,y).subscript𝒳𝒴Φ𝑥𝑦differential-d𝜋𝑥𝑦\int\_{\mathcal{X}\times\mathcal{Y}}\Phi\left(x,y\right)\,d\pi\left(x,y\right). |  |

A payoff corresponding to an assignment π∈Π𝒳,𝒴​(μ,ν)𝜋subscriptΠ

𝒳𝒴𝜇𝜈\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) is a pair of functions
(U𝒳,U𝒴)∈L1​(𝒳,ℬ𝒳,μ)×L1​(𝒴,ℬ𝒴,ν)subscript𝑈𝒳subscript𝑈𝒴superscript𝐿1𝒳subscriptℬ𝒳𝜇superscript𝐿1𝒴subscriptℬ𝒴𝜈\left(U\_{\mathcal{X}},U\_{\mathcal{Y}}\right)\in L^{1}\left(\mathcal{X},\mathcal{B}\_{\mathcal{X}},\mu\right)\times L^{1}\left(\mathcal{Y},\mathcal{B}\_{\mathcal{Y}},\nu\right) such that

|  |  |  |
| --- | --- | --- |
|  | U𝒳​(x)+U𝒴​(y)=Φ​(x,y),for π-a.e. ​(x,y)∈s​u​p​p​(π).formulae-sequencesubscript𝑈𝒳𝑥subscript𝑈𝒴𝑦Φ𝑥𝑦for π-a.e. 𝑥𝑦𝑠𝑢𝑝𝑝𝜋U\_{\mathcal{X}}(x)+U\_{\mathcal{Y}}(y)=\Phi\left(x,y\right),\ \hbox{for $\pi$-a.e.\,}\left(x,y\right)\in supp\left(\pi\right). |  |

An outcome is a triple (π,U𝒳,U𝒴)𝜋subscript𝑈𝒳subscript𝑈𝒴\left(\pi,U\_{\mathcal{X}},U\_{\mathcal{Y}}\right), where (U𝒳,U𝒴)subscript𝑈𝒳subscript𝑈𝒴\left(U\_{\mathcal{X}},U\_{\mathcal{Y}}\right) is a payoff corresponding to π𝜋\pi. The standard equilibrium concept used in this framework is satibility. An outcome (π,U𝒳,U𝒴)𝜋subscript𝑈𝒳subscript𝑈𝒴\left(\pi,U\_{\mathcal{X}},U\_{\mathcal{Y}}\right) is called stable if it satisfies

|  |  |  |
| --- | --- | --- |
|  | U𝒳​(x)+U𝒴​(y)≥Φ​(x,y),∀(x,y)∈𝒳×𝒴.formulae-sequencesubscript𝑈𝒳𝑥subscript𝑈𝒴𝑦Φ𝑥𝑦for-all𝑥𝑦𝒳𝒴U\_{\mathcal{X}}(x)+U\_{\mathcal{Y}}(y)\geq\Phi\left(x,y\right),\ \forall\left(x,y\right)\in\mathcal{X}\times\mathcal{Y}. |  |

Finally, a matching π𝜋\pi is stable if there exists a payoff (U𝒳,U𝒴)subscript𝑈𝒳subscript𝑈𝒴\left(U\_{\mathcal{X}},U\_{\mathcal{Y}}\right) corresponding to π𝜋\pi, such that the outcome (π,U𝒳,U𝒴)𝜋subscript𝑈𝒳subscript𝑈𝒴\left(\pi,U\_{\mathcal{X}},U\_{\mathcal{Y}}\right) is stable. Hence, stability is tantamount to robustness against deviations by both individuals and pairs. In other words stability requires that (i) no matched agent is better off unmatched; and (ii) no two unmatched agents are better off matched together than remaining in their current situation.

A fundamental result in the theory of matching with transferable utility is that stability is equivalent to surplus maximization. This result is due to Shapley and Shubik [[1971](#bib.bib13)] in the discrete case and Gretsky et al. [[1992](#bib.bib10)] in the continuous case (and it is also a consequence of the Monge-Kantorovich duality Villani [[2008](#bib.bib15), Theorem 5.10]). It was recently extended by Pass [[2019](#bib.bib11)] to a setting of tripartite matching (also known as multi-marginal optimal transport).

###### Proposition 3.1.

For a given surplus function Φ:𝒳×𝒴→ℝ:Φ→𝒳𝒴ℝ\Phi:\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R}, a matching π∈Π𝒳,𝒴​(μ,ν)𝜋subscriptΠ

𝒳𝒴𝜇𝜈\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right) is stable if and only if it solves the surplus maximization problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")):

|  |  |  |
| --- | --- | --- |
|  | supπ∈Π𝒳,𝒴​(μ,ν)​∫𝒳×𝒴Φ​(x,y)​𝑑π​(x,y).𝜋subscriptΠ  𝒳𝒴𝜇𝜈supremumsubscript𝒳𝒴Φ𝑥𝑦differential-d𝜋𝑥𝑦\underset{\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)}{\sup}\ \int\_{\mathcal{X}\times\mathcal{Y}}\Phi\left(x,y\right)\,d\pi\left(x,y\right). |  |

A central planner can hence implement a stable, that is, equilibrium assignment by solving the surplus maximization problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")). This, however, necessitates knowledge of the marginal (type) distributions μ𝜇\mu and ν𝜈\nu. If the type distributions μ𝜇\mu and ν𝜈\nu are unknown by the central planner, then since 𝒳𝒳\mathcal{X} and 𝒴𝒴\mathcal{Y} are separable, an approximation based on sampling from empirical distributions can be used, as long as the value of Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) is continuous. This, in turn, can be obtained from Berge’s Maximum Theorem when the correspondence Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} is continuous, under some regularity conditions on the surplus function ΦΦ\Phi. We summarize this in Proposition [3.2](#S3.Thmtheorem2 "Proposition 3.2. ‣ 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") below. First, however, we introduce some needed notation.

For the probability space (𝒳,ℬ𝒳,μ)𝒳subscriptℬ𝒳𝜇\left(\mathcal{X},\mathcal{B}\_{\mathcal{X}},\mu\right), there are 𝒳𝒳\mathcal{X}-valued independent random variables {Xi}i≥1subscriptsubscript𝑋𝑖𝑖1\{X\_{i}\}\_{i\geq 1} defined on a common probability space (Ω𝒳,ℱ𝒳,P𝒳)subscriptΩ𝒳subscriptℱ𝒳subscript𝑃𝒳\left(\Omega\_{\mathcal{X}},\mathcal{F}\_{\mathcal{X}},P\_{\mathcal{X}}\right), with laws ℒ​(Xi)=P𝒳∘Xi−1=μℒsubscript𝑋𝑖subscript𝑃𝒳superscriptsubscript𝑋𝑖1𝜇\mathcal{L}\left(X\_{i}\right)=P\_{\mathcal{X}}\circ X\_{i}^{-1}=\mu, for all i≥1𝑖1i\geq 1 (see, e.g., Dudley [[2002](#bib.bib5), §8.2, §11.4]).
Similarly, for the probability space (𝒴,ℬ𝒴,ν)𝒴subscriptℬ𝒴𝜈\left(\mathcal{Y},\mathcal{B}\_{\mathcal{Y}},\nu\right), there are 𝒴𝒴\mathcal{Y}-valued independent random variables {Yj}j≥1subscriptsubscript𝑌𝑗𝑗1\{Y\_{j}\}\_{j\geq 1} defined on a common probability space (Ω𝒴,ℱ𝒴,P𝒴)subscriptΩ𝒴subscriptℱ𝒴subscript𝑃𝒴\left(\Omega\_{\mathcal{Y}},\mathcal{F}\_{\mathcal{Y}},P\_{\mathcal{Y}}\right), with laws ℒ​(Yj)=P𝒴∘Yj−1=νℒsubscript𝑌𝑗subscript𝑃𝒴superscriptsubscript𝑌𝑗1𝜈\mathcal{L}\left(Y\_{j}\right)=P\_{\mathcal{Y}}\circ Y\_{j}^{-1}=\nu, for all j≥1𝑗1j\geq 1. Define the empirical measures by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn​(A)​(ω):=1n​∑i=1n𝟙A​(Xi​(ω)),∀A∈ℬ𝒳,∀ω∈Ω𝒳;formulae-sequenceassignsubscript𝜇𝑛𝐴𝜔1𝑛superscriptsubscript𝑖1𝑛subscript1𝐴subscript𝑋𝑖𝜔formulae-sequencefor-all𝐴subscriptℬ𝒳for-all𝜔subscriptΩ𝒳\mu\_{n}(A)(\omega):=\frac{1}{n}\sum\_{i=1}^{n}\mathds{1}\_{A}\left(X\_{i}(\omega)\right),\ \forall A\in\mathcal{B}\_{\mathcal{X}},\ \forall\omega\in\Omega\_{\mathcal{X}}; |  | (3.1) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | νn​(B)​(κ):=1n​∑j=1n𝟙B​(Yj​(κ)),∀B∈ℬ𝒴,∀κ∈Ω𝒴.formulae-sequenceassignsubscript𝜈𝑛𝐵𝜅1𝑛superscriptsubscript𝑗1𝑛subscript1𝐵subscript𝑌𝑗𝜅formulae-sequencefor-all𝐵subscriptℬ𝒴for-all𝜅subscriptΩ𝒴\nu\_{n}(B)(\kappa):=\frac{1}{n}\sum\_{j=1}^{n}\mathds{1}\_{B}\left(Y\_{j}(\kappa)\right),\ \forall B\in\mathcal{B}\_{\mathcal{Y}},\ \forall\kappa\in\Omega\_{\mathcal{Y}}. |  | (3.2) |

###### Proposition 3.2.

Let V:𝒳×𝒴→ℝ:𝑉→𝒳𝒴ℝV:\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R} be the value function of Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) defined in eq. ([1.4](#S1.E4 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")), and let {μn}nsubscriptsubscript𝜇𝑛𝑛\{\mu\_{n}\}\_{n} and {νn}nsubscriptsubscript𝜈𝑛𝑛\{\nu\_{n}\}\_{n} be the empricical measures defined in eq. ([3.1](#S3.E1 "In 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) and ([3.2](#S3.E2 "In 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")). If Φ∈Cb​(𝒳×𝒴)Φsubscript𝐶𝑏𝒳𝒴\Phi\in C\_{b}\left(\mathcal{X}\times\mathcal{Y}\right), then there exists a stable matching π∗superscript𝜋\pi^{\*}. Moreover,

|  |  |  |
| --- | --- | --- |
|  | V​(μn,νn)→V​(μ,ν)=∫𝒳×𝒴Φ​(x,y)​𝑑π∗​(x,y)=supπ∈Π𝒳,𝒴​(μ,ν)​Ψ​((μ,ν),π),→𝑉subscript𝜇𝑛subscript𝜈𝑛𝑉𝜇𝜈subscript𝒳𝒴Φ𝑥𝑦differential-dsuperscript𝜋𝑥𝑦𝜋subscriptΠ  𝒳𝒴𝜇𝜈supremumΨ𝜇𝜈𝜋V\left(\mu\_{n},\nu\_{n}\right)\to V\left(\mu,\nu\right)=\int\_{\mathcal{X}\times\mathcal{Y}}\Phi\left(x,y\right)\,d\pi^{\*}\left(x,y\right)=\underset{\pi\in\Pi\_{\mathcal{X},\mathcal{Y}}\left(\mu,\nu\right)}{\sup}\Psi\left(\left(\mu,\nu\right),\pi\right), |  |

where ΨΨ\Psi denotes the objective function of Problem [1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") defined in eq. ([1.3](#S1.E3 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")).

###### Proof.

First, note that by the Monge-Katorovich Duality Theorem (e.g., Villani [[2003](#bib.bib14), Theorem 1.3]), the assumption that Φ∈Cb​(𝒳×𝒴)Φsubscript𝐶𝑏𝒳𝒴\Phi\in C\_{b}\left(\mathcal{X}\times\mathcal{Y}\right) guarantees the existence of a solution π∗superscript𝜋\pi^{\*} to Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")). Hence, by Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport"), π∗superscript𝜋\pi^{\*} is a stable matching. By Theorem [2.3](#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Continuity of the Feasible Set Correspondence Π_{𝒳,𝒴} ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport"), Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} is continuous, implying that G​r​(Π𝒳,𝒴)𝐺𝑟subscriptΠ

𝒳𝒴Gr\left(\Pi\_{\mathcal{X},\mathcal{Y}}\right) is closed. Since Φ∈Cb​(𝒳×𝒴)Φsubscript𝐶𝑏𝒳𝒴\Phi\in C\_{b}\left(\mathcal{X}\times\mathcal{Y}\right), it follows that the objective function ΨΨ\Psi of Problem [1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") is continuous in the product topology. Since Π𝒳,𝒴subscriptΠ

𝒳𝒴\Pi\_{\mathcal{X},\mathcal{Y}} is continuous and has nonempty, compact values, and since 𝒫​(𝒳×𝒴)𝒫𝒳𝒴\mathcal{P}(\mathcal{X}\times\mathcal{Y}) is Hausdorff being metrizable, continuity of the value function V𝑉V of Problem ([1.1](#S1.E1 "In 1 Introduction ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")) follows from Berge’s Maximum Theorem (e.g., Aliprantis and Border [[2006](#bib.bib1), Theorem 17.31]).
By Varadarajan’s extension (Dudley [[2002](#bib.bib5), Theorem 11.4.1]) of the classical Glivenko-Cantelli Theorem, the sequences {μn}nsubscriptsubscript𝜇𝑛𝑛\{\mu\_{n}\}\_{n} and {νn}nsubscriptsubscript𝜈𝑛𝑛\{\nu\_{n}\}\_{n} converge almost surely to μ𝜇\mu and ν𝜈\nu, respectively, since the spaces 𝒳𝒳\mathcal{X} and 𝒴𝒴\mathcal{Y} are separable. Therefore, μn→μ→subscript𝜇𝑛𝜇\mu\_{n}\to\mu and νn→ν→subscript𝜈𝑛𝜈\nu\_{n}\to\nu. Hence, by continuity of V𝑉V, it follows that V​(μn,νn)→V​(μ,ν).→𝑉subscript𝜇𝑛subscript𝜈𝑛𝑉𝜇𝜈V\left(\mu\_{n},\nu\_{n}\right)\to V\left(\mu,\nu\right).
∎

###### Remark 3.3.

In light of the Monge-Katorovich Duality Theorem, the assumption in Proposition [3.2](#S3.Thmtheorem2 "Proposition 3.2. ‣ 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") that Φ∈Cb​(𝒳×𝒴)Φsubscript𝐶𝑏𝒳𝒴\Phi\in C\_{b}\left(\mathcal{X}\times\mathcal{Y}\right) can be weakened to an assumption that ΦΦ\Phi is upper-semicontinuous and that there are some lower-semicontinuous functions a∈L1​(𝒳,ℬ𝒳,μ)𝑎superscript𝐿1𝒳subscriptℬ𝒳𝜇a\in L^{1}\left(\mathcal{X},\mathcal{B}\_{\mathcal{X}},\mu\right) and b∈L1​(𝒴,ℬ𝒴,ν)𝑏superscript𝐿1𝒴subscriptℬ𝒴𝜈b\in L^{1}\left(\mathcal{Y},\mathcal{B}\_{\mathcal{Y}},\nu\right) such that

|  |  |  |
| --- | --- | --- |
|  | Φ​(x,y)≤a​(x)+b​(y), for μ-a.e. x and ν-a.e. y.Φ𝑥𝑦  𝑎𝑥𝑏𝑦 for μ-a.e. x and ν-a.e. y\Phi\left(x,y\right)\leq a\left(x\right)+b\left(y\right),\hbox{ for $\mu$-a.e.\ $x$ and $\nu$-a.e.\ $y$}. |  |

###### Remark 3.4 (Hedonic Price Equilibria).

Chiappori et al. [[2010](#bib.bib4)] show that there exists a canonical correspondence between models of hedonic pricing with quasi-linear preferences and TU matching models, and hence a fortiori surplus maximization problems (in light of Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport")). This was extended by Pass [[2019](#bib.bib11)] to a setting of multi-marginal optimal transport (tripartite matching). We refer to Ekeland [[2005](#bib.bib6)], Ekeland [[2010](#bib.bib7)], Chiappori et al. [[2010](#bib.bib4)], and Pass [[2019](#bib.bib11)] for more about models of hedonic equilibria and their equivalence to surplus maximization problems. Proposition [3.2](#S3.Thmtheorem2 "Proposition 3.2. ‣ 3 TU Matching with Unknown Type Distributions ‣ On the Continuity of the Feasible Set Mapping in Optimal Transport") above can therefore be used to show the existence of a hedonic price equilibrium, when the type distributions of buyers and sellers (the probability measures μ𝜇\mu and ν𝜈\nu) are unknown.

## References

* Aliprantis and Border [2006]

  C.D. Aliprantis and K.C. Border.
  *Infinite Dimensional Analysis: A Hitchhiker’s Guide*.
  Springer, Berlin, third edition, 2006.
* Bergin [1999]

  J. Bergin.
  On the continuity of correspondences on sets of measures with
  restricted marginals.
  *Economic Theory*, 13:471–481, 1999.
* Billingsley [1999]

  P. Billingsley.
  *Convergence of Probability Measures*.
  John Wiley & Sons, New York, second edition, 1999.
* Chiappori et al. [2010]

  P-A. Chiappori, R.J. McCann, and L.P. Nesheim.
  Hedonic price equilibria, stable matching, and optimal transport:
  equivalence, topology, and uniqueness.
  *Economic Theory*, 42(2):317–354, 2010.
* Dudley [2002]

  R.M. Dudley.
  *Real Analysis and Probability*.
  Cambridge University Press, Cambridge, second edition, 2002.
* Ekeland [2005]

  I. Ekeland.
  An optimal matching problem.
  *ESAIM: Control, Optimisation and Calculus of Variations*,
  11(1):57–71, 2005.
* Ekeland [2010]

  I. Ekeland.
  Existence, uniqueness and efficiency of equilibrium in hedonic
  markets with multidimensional types.
  *Economic Theory*, 42(2):275–315, 2010.
* Ethier and Kurtz [2005]

  S.N. Ethier and T.G. Kurtz.
  *Markov Processes: Characterization and Convergence*.
  John Wiley & Sons, Hoboken, New Jersey, second edition, 2005.
* Galichon [2016]

  A. Galichon.
  *Optimal Transport Methods in Economics*.
  Princeton University Press, Princeton, 2016.
* Gretsky et al. [1992]

  N.E. Gretsky, J.M. Ostroy, and W.R. Zame.
  The nonatomic assignment model.
  *Economic Theory*, 2(1):103–127, 1992.
* Pass [2019]

  B. Pass.
  Interpolating between matching and hedonic pricing models.
  *Economic Theory*, 67(2):393–419, 2019.
* Savchenko and Zarichnyi [2014]

  A. Savchenko and M. Zarichnyi.
  Correspondences of probability measures with restricted marginals.
  *Proc. Intern. Geom. Center*, 7(4):34–39,
  2014.
* Shapley and Shubik [1971]

  L.S. Shapley and M. Shubik.
  The assignment game i: The core.
  *International Journal of Game Theory*, 1(1):111–130, 1971.
* Villani [2003]

  C. Villani.
  *Topics in Optimal Transportation*.
  American Mathematical Society, Providence, 2003.
* Villani [2008]

  C. Villani.
  *Optimal Transport, Old and New*.
  Springer, Berlin, 2008.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2009.12838)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2009.12838)
[View original  
on arXiv](https://arxiv.org/abs/2009.12838)[►](javascript: void(0))