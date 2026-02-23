---
authors:
- Daniel Chee
- Noufel Frikha
- Libo Li
doc_id: arxiv:2602.18078v1
family_id: arxiv:2602.18078
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Entropy-regularized penalization schemes for American options and reflected
  BSDEs with singular generators
url_abs: http://arxiv.org/abs/2602.18078v1
url_html: https://arxiv.org/html/2602.18078v1
venue: arXiv q-fin
version: 1
year: 2026
---


Daniel Cheea\,{}^{a}, Noufel Frikhab\,{}^{b} and Libo Lia\,{}^{a}
  
  
  
  
  
a{}^{a\,}School of Mathematics and Statistics, University of New South Wales
  
Sydney, NSW 2052, Australia
  
  
b{}^{b\,}Université Paris 1 Panthéon-Sorbonne, Centre d’Economie de la Sorbonne,
  
106 Boulevard de l’Hôpital, 75642 Paris Cedex 13, France

###### Abstract

This paper extends our previous work in Chee *et al.* [[9](https://arxiv.org/html/2602.18078v1#bib.bib9)] to continuous-time optimal stopping problems, with a particular focus on American options within an exploratory framework.
We pursue two main objectives. First, motivated by reinforcement learning applications, we introduce an entropy-regularized penalization scheme for continuous-time optimal stopping problems. The scheme is inspired by classical penalization techniques for reflected backward stochastic differential equations (RBSDEs) and provides a smooth approximation of the degenerate stopping rule inherent to the American option problem. This regularization promotes exploration, enables the use of gradient-based optimization methods, and leads naturally to policy improvement algorithms. We establish well-posedness and convergence properties of the scheme, and illustrate its numerical feasibility through low-dimensional experiments based on policy iteration and least-squares Monte Carlo methods.
Second, from a theoretical perspective, we study the asymptotic limit of the entropy-regularized penalization as the penalization parameter tends to infinity. We show that the limiting value process solves a reflected BSDE with a logarithmically singular driver, and we prove existence and uniqueness of solutions to this new class of RBSDEs via a monotone limit argument. To the best of our knowledge, such equations have not previously been investigated in the literature.

## 1 Introduction

The numerical resolution of optimal stopping problems has long been a central topic in mathematical finance, with applications ranging from the pricing of American options to optimal liquidation and real options. In recent years, the rapid development of machine learning and reinforcement learning (RL) techniques has renewed interest in Monte Carlo–based approaches to optimal stopping, particularly in high-dimensional and model-agnostic settings. A growing literature explores the use of randomized stopping representations and
entropy regularization to recast optimal stopping problems as stochastic control problems amenable to RL algorithms; see, among others, [[5](https://arxiv.org/html/2602.18078v1#bib.bib5), [40](https://arxiv.org/html/2602.18078v1#bib.bib40), [39](https://arxiv.org/html/2602.18078v1#bib.bib39), [15](https://arxiv.org/html/2602.18078v1#bib.bib15), [14](https://arxiv.org/html/2602.18078v1#bib.bib14), [16](https://arxiv.org/html/2602.18078v1#bib.bib16), [17](https://arxiv.org/html/2602.18078v1#bib.bib17)].

In this work, we consider a continuous-time optimal stopping problem on the usual filtered probability space (Ω,ℱ,𝔽=(ℱt)0≤t≤T,ℙ)(\Omega,\mathcal{F},\mathbb{F}=(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{P}).
Given a payoff process PP, we denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=ess​supτ∈𝒯t,T⁡𝔼​[Pτ∣ℱt],V\_{t}=\operatornamewithlimits{ess\,sup}\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\tau}\mid\mathcal{F}\_{t}], |  | (1.1) |

the associated value process, where 𝒯t,T\mathcal{T}\_{t,T} is the set of 𝔽\mathbb{F}-stopping times valued in [t,T][t,T]. It is well known that VV coincides with the Snell envelope of PP and admits a Doob-Meyer-Mertens decomposition, which can be characterized via a reflected
backward stochastic differential equation (RBSDE).

Our starting point is the randomized stopping representation of Gyöngy and Šiška [[25](https://arxiv.org/html/2602.18078v1#bib.bib25)], which allows one to rewrite the optimal stopping problem as a control problem over non-negative stopping intensities. Formally, one has

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=ess​supγ∈Λ⁡𝔼​[PT​e−∫tTγu​𝑑u+∫tTPs​γs​e−∫tsγu​𝑑u​𝑑s|ℱt],\displaystyle V\_{t}=\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\mathbb{E}\Big[P\_{T}e^{-\int\_{t}^{T}\gamma\_{u}du}+\int\_{t}^{T}P\_{s}\gamma\_{s}e^{-\int\_{t}^{s}\gamma\_{u}du}ds\,\Big|\,\mathcal{F}\_{t}\Big], |  | (1.2) |

where Λ\Lambda denotes the set of admissible stopping intensities.
This formulation lies at the heart of several recent entropy-regularized and RL-based approaches to optimal stopping.

This formulation naturally leads to a backward stochastic differential equation (BSDE). Heuristically speaking, an application of Itô’s formula suggests the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=PT−(MT−Mt)+ess​supγ∈Λ​∫tT(Ps−Vs)​γs​𝑑s,\displaystyle V\_{t}=P\_{T}-(M\_{T}-M\_{t})+\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\int\_{t}^{T}(P\_{s}-V\_{s})\gamma\_{s}ds, |  | (1.3) |

where MM is a martingale.

The backward equation ([1.3](https://arxiv.org/html/2602.18078v1#S1.E3 "In 1 Introduction ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) highlights a fundamental difficulty of the continuous-time setting: the optimal stopping intensity is typically degenerate, taking values 0 or ∞\infty. This lack of regularity poses both theoretical and numerical challenges, particularly for gradient-based learning algorithms.

To overcome this difficulty, entropy regularization has been introduced in recent works, either at the level of exploratory Hamilton-Jacobi-Bellman equations or through relaxed control formulations [[16](https://arxiv.org/html/2602.18078v1#bib.bib16), [15](https://arxiv.org/html/2602.18078v1#bib.bib15), [14](https://arxiv.org/html/2602.18078v1#bib.bib14), [17](https://arxiv.org/html/2602.18078v1#bib.bib17)].
The present paper adopts a different viewpoint.
Rather than working with PDEs or relying on a specific diffusion model, we develop a purely probabilistic framework based on the BSDE characterization ([1.3](https://arxiv.org/html/2602.18078v1#S1.E3 "In 1 Introduction ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")).
Entropy regularization is introduced directly at the level of a penalization scheme for the reflected constraint, inspired by the classical penalization approach for RBSDEs introduced by El Karoui *et al.* [[19](https://arxiv.org/html/2602.18078v1#bib.bib19)].
This leads to what we term an *entropy-regularized penalization scheme*.
The resulting approach is model-independent, fully data-driven, and naturally accommodates non-linearities in the underlying market dynamics.

The paper has two main objectives.
The first is to introduce and analyze the entropy-regularized penalization scheme for computing the value of a continuous-time optimal stopping problem.
For fixed penalization and temperature parameters, we establish well-posedness of the resulting BSDE and study its convergence as the parameters are sent to their
limits.
In particular, we show that, under suitable scaling of the temperature and penalization parameters, the entropy-regularized value process converges to the classical value process VV, and we derive quantitative convergence rates under additional regularity assumptions.
We also propose and analyze a policy improvement algorithm (PIA) associated with the entropy-regularized formulation.

The second objective is of independent theoretical interest.
We show that, when the penalization parameter tends to infinity while the temperature
parameter is kept fixed, the entropy-regularized scheme converges monotonically to a
limit process VλV^{\lambda}. We prove that VλV^{\lambda} is the unique solution to a RBSDE with a
logarithmically singular driver. To the best of our knowledge, this class of RBSDEs has not previously appeared in the
literature. In the broader context of (quadratic) BSDEs with singular drivers, early contributions
include Duffie and Epstein [[13](https://arxiv.org/html/2602.18078v1#bib.bib13)], followed by works of Bahlali [[2](https://arxiv.org/html/2602.18078v1#bib.bib2)],
Bahlali *et al.* [[3](https://arxiv.org/html/2602.18078v1#bib.bib3)], and Bahlali and Tangpi [[4](https://arxiv.org/html/2602.18078v1#bib.bib4)], with more
recent developments in [[49](https://arxiv.org/html/2602.18078v1#bib.bib49), [47](https://arxiv.org/html/2602.18078v1#bib.bib47), [29](https://arxiv.org/html/2602.18078v1#bib.bib29)]. For RBSDEs with singular drivers, we also mention the recent works of Zheng [[48](https://arxiv.org/html/2602.18078v1#bib.bib48)] and Zheng *et al.* [[50](https://arxiv.org/html/2602.18078v1#bib.bib50)], which rely on domination
arguments and the Itô-Krylov formula. In contrast, our analysis relies on a monotone limit argument in the spirit of
Peng [[37](https://arxiv.org/html/2602.18078v1#bib.bib37)], and does not involve quadratic growth. Finally, we provide a probabilistic/financial interpretation of the limiting process VλV^{\lambda}. We show that VλV^{\lambda} can be interpreted as the value of an American option subject to default risk, where the default intensity depends endogenously on the distance between the value process and the payoff. As the parameter λ→0\lambda\rightarrow 0, the default intensity vanishes and the classical American option value is recovered.

The rest of the paper is organized as follows.
Section [3](https://arxiv.org/html/2602.18078v1#S3 "3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") introduces the entropy-regularized penalization scheme and studies
its convergence to the American option, as well as the associated PIA.
Section [4](https://arxiv.org/html/2602.18078v1#S4 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") is devoted to the asymptotic analysis of the scheme, including
the characterization of the limiting singular RBSDE.
Section [5.1](https://arxiv.org/html/2602.18078v1#S5.SS1 "5.1 Implicit BSDE Solver ‣ 5 Numerical Experiments ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") presents numerical experiments illustrating the performance of the
proposed algorithms. Technical proofs and auxiliary results are collected in the appendix.

## 2 Notations and Setup

We operate on the usual filtered probability space (Ω,ℱ,𝔽=(ℱt)t≥0,ℙ)(\Omega,{\mathcal{F}},{\mathbb{F}}=({\mathcal{F}}\_{t})\_{t\geq 0},{\mathbb{P}}). Additional assumptions on the filtration 𝔽\mathbb{F} will be explicitly stated when required (see Assumption [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmhyp1 "Assumption 4.1. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). We denote by 𝒪​(𝔽)\mathcal{O}({\mathbb{F}}) the space of 𝔽{\mathbb{F}} optional processes, by 𝒫​(𝔽)\mathcal{P}({\mathbb{F}}) the space of 𝔽{\mathbb{F}} predictable processes, by ℳ{\mathcal{M}} the space of 𝔽{\mathbb{F}} martingales, and by 𝒜+{\mathcal{A}}^{+} the space of 𝔽{\mathbb{F}} predictable, positive, increasing processes. We also write x∨y=max⁡(x,y)x\vee y=\max(x,y), x+=max⁡(x,0)x^{+}=\max(x,0) and x−=max⁡(−x,0)x^{-}=\max(-x,0). Throughout, CC and KK denote positive constants that may vary from line to line.

For results in optimal stopping and in the theory of BSDEs and RBSDEs under general filtrations, we refer, for example, to Maingueneau [[34](https://arxiv.org/html/2602.18078v1#bib.bib34)], El-Karoui *et al.* [[19](https://arxiv.org/html/2602.18078v1#bib.bib19)], Øksendal and Zhang [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)], Grigorova *et al.* [[23](https://arxiv.org/html/2602.18078v1#bib.bib23)], and Hamadène and Ouknine [[26](https://arxiv.org/html/2602.18078v1#bib.bib26)]. We use the following function spaces throughout the article. The Banach space of square-integrable optional processes is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮2\displaystyle\mathcal{S}^{2} | :={X∈𝒪​(𝔽):𝔼​[sup0≤t≤TXt2]<∞}.\displaystyle:=\big\{X\in\mathcal{O}(\mathbb{F}):\mathbb{E}\big[\sup\_{0\leq t\leq T}X\_{t}^{2}\big]<\infty\big\}. |  |

The space of square-integrable continuous martingales is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ2\displaystyle\mathcal{H}^{2} | :={M∈ℳ:𝔼​[[M]T]<∞},\displaystyle:=\left\{M\in\mathcal{M}:\mathbb{E}\left[[M]\_{T}\right]<\infty\right\}, |  |

where [M][M] stands for the quadratic variation of MM. The space of square-integrable, predictable, increasing processes is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒦2\displaystyle\mathcal{K}^{2} | :={A∈𝒜+:𝔼​[AT2]<∞}.\displaystyle:=\big\{A\in\mathcal{A}^{+}:\mathbb{E}\big[A\_{T}^{2}\big]<\infty\big\}. |  |

If the payoff process PP is càdlàg and satisfies suitable integrability conditions, the value process VV in ([1.1](https://arxiv.org/html/2602.18078v1#S1.E1 "In 1 Introduction ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) belongs to class (D), i.e. the family {Vτ:τ​ stopping time}\left\{V\_{\tau}:\tau\mbox{ stopping time}\right\} is uniformly integrable. In this case, VV admits the Doob-Meyer-Mertens decomposition, or equivalently, satisfies the RBSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt\displaystyle V\_{t} | =PT−(MT−Mt)+(AT−At),t∈[0,T]\displaystyle=P\_{T}-(M\_{T}-M\_{t})+(A\_{T}-A\_{t}),\qquad t\in[0,T] |  | (2.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt\displaystyle V\_{t} | ≥Ptand∫0T(Vs−−Ps−)​𝑑As=0,\displaystyle\geq P\_{t}\quad\mathrm{and}\quad\int^{T}\_{0}(V\_{s-}-P\_{s-})dA\_{s}=0, |  |

where MM is a uniformly integrable martingale and AA is a predictable increasing process. In particular, when P∈𝒮2P\in\mathcal{S}^{2}, one has (V,M,A)∈𝒮2×ℋ2×𝒦2(V,M,A)\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{K}^{2}; see, for example, Steps 1-4 in the proof of Lemma 3.3 in Grigorova *et al.* [[23](https://arxiv.org/html/2602.18078v1#bib.bib23)].

## 3 Entropy-Regularized Penalization Scheme

In this section, we introduce our entropy-regularized penalization approach for American options. The methodology builds upon the relaxed control framework developed for Bermudan options in our earlier work [[9](https://arxiv.org/html/2602.18078v1#bib.bib9)]. A key distinction between Bermudan and American options is that, in the latter case, the optimal control γ\gamma in ([1.3](https://arxiv.org/html/2602.18078v1#S1.E3 "In 1 Introduction ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) may take the value +∞+\infty. This feature leads to significant analytical difficulties, in particular regarding the well-posedness of the associated BSDEs once entropy regularization is introduced.

To address this issue, we combine entropy regularization with the classical penalization technique commonly used in the theory of reflected BSDEs. This hybrid approach allows us to retain the tractability of entropy-based methods while controlling the singular behavior of the optimal control.

Throughout this paper, we impose the following standing assumption on the payoff process.

###### Assumption 3.1.

The payoff process PP is positive, 𝔽\mathbb{F}-adapted, and càdlàg, and satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Pt|2]<∞.\mathbb{E}\Big[\sup\_{0\leq t\leq T}|P\_{t}|^{2}\Big]<\infty. |  |

We begin by truncating the control space and restricting attention to bounded controls. For a fixed n≥1n\geq 1, let Λn\Lambda\_{n} denote the set of 𝔽\mathbb{F}-predictable processes taking values in [0,n][0,n]. We consider the penalized BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtn\displaystyle V^{n}\_{t} | =PT−(MTn−Mtn)+ess​supγ∈Λn​∫tT(Ps−Vsn)​γs​𝑑s.\displaystyle=P\_{T}-(M^{n}\_{T}-M^{n}\_{t})+\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda\_{n}}\int^{T}\_{t}(P\_{s}-V^{n}\_{s})\gamma\_{s}\,ds. |  | (3.1) |

Formally, if a solution (Vn,Mn)(V^{n},M^{n}) to ([3.1](https://arxiv.org/html/2602.18078v1#S3.E1 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) exists, the optimal control is given pointwise by

|  |  |  |
| --- | --- | --- |
|  | γs∗=n​ 1{Ps−Vsn>0},\gamma^{\*}\_{s}=n\,\mathbf{1}\_{\{P\_{s}-V^{n}\_{s}>0\}}, |  |

so that the value process satisfies the classical penalization scheme

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtn\displaystyle V^{n}\_{t} | =PT−(MTn−Mtn)+∫tTn​(Ps−Vsn)+​𝑑s.\displaystyle=P\_{T}-(M^{n}\_{T}-M^{n}\_{t})+\int^{T}\_{t}n(P\_{s}-V^{n}\_{s})^{+}\,ds. |  | (3.2) |

Following [[9](https://arxiv.org/html/2602.18078v1#bib.bib9)], we now introduce an entropy-regularized version of ([3.1](https://arxiv.org/html/2602.18078v1#S3.E1 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) by relaxing the control. For λ≥0\lambda\geq 0, referred to as the *temperature parameter*, we consider the BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtλ,n\displaystyle V^{\lambda,n}\_{t} | =PT−(MTλ,n−Mtλ,n)+ess​supπ∈Πn⁡{∫tT∫0n(Ps−Vsλ,n)​u​πs​(u)−λ​πs​(u)​ln⁡πs​(u)​d​u​d​s},\displaystyle=P\_{T}-(M^{\lambda,n}\_{T}-M^{\lambda,n}\_{t})+\operatornamewithlimits{ess\,sup}\_{\pi\in\Pi\_{n}}\left\{\int^{T}\_{t}\int^{n}\_{0}(P\_{s}-V^{\lambda,n}\_{s})u\pi\_{s}(u)-\lambda\pi\_{s}(u)\ln\pi\_{s}(u)\,du\,ds\right\}, |  | (3.3) |

where Πn\Pi\_{n} denotes the set of 𝔽\mathbb{F}-predictable probability densities on [0,n][0,n], namely

|  |  |  |
| --- | --- | --- |
|  | Πn={π=(πs​(u))s∈[0,T]:(u,s)↦πs​(u)​ is ​ℬ​([0,n])⊗ℱs​ measurable, ​π​(u)≥0​ and ​∫0nπs​(u)​𝑑u=1}.\displaystyle\Pi\_{n}=\left\{\pi=(\pi\_{s}(u))\_{s\in[0,T]}\,:(u,s)\mapsto\pi\_{s}(u)\text{ is }\mathcal{B}([0,n])\otimes{\mathcal{F}}\_{s}\text{ measurable, }\pi(u)\geq 0\text{ and }\int^{n}\_{0}\pi\_{s}(u)du=1\right\}. |  |

Assuming that ([3.3](https://arxiv.org/html/2602.18078v1#S3.E3 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) is well posed, the pointwise optimal control admits a Gibbs-type representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πs∗​(u)=1λ​(Ps−Vsλ,n)enλ​(Ps−Vsλ,n)−1​e1λ​(Ps−Vsλ,n)​u,u∈[0,n].\displaystyle\pi^{\*}\_{s}(u)=\frac{\frac{1}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}{e^{\frac{n}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}-1}e^{\frac{1}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})u},\quad u\in[0,n]. |  | (3.4) |

A direct computation shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞1λ​(Ps−x)enλ​(Ps−x)−1​e1λ​(Ps−x)​u={1λ​(x−Ps)​e−1λ​(x−Ps)​u,x>Ps,0,x≤Ps,\displaystyle\lim\_{n\to\infty}\frac{\frac{1}{\lambda}(P\_{s}-x)}{e^{\frac{n}{\lambda}(P\_{s}-x)}-1}\,e^{\frac{1}{\lambda}(P\_{s}-x)u}=\begin{cases}\displaystyle\frac{1}{\lambda}(x-P\_{s})\,e^{-\frac{1}{\lambda}(x-P\_{s})u},&x>P\_{s},\\[6.0pt] 0,&x\leq P\_{s},\end{cases} |  | (3.5) |

As we shall see in Subsection [4](https://arxiv.org/html/2602.18078v1#S4 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), the regime x≤Psx\leq P\_{s} corresponds to reflection at the lower barrier PsP\_{s}.

Our objective is now to study rigorously the entropy-regularized penalization scheme ([3.3](https://arxiv.org/html/2602.18078v1#S3.E3 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), with the optimal control ([3.4](https://arxiv.org/html/2602.18078v1#S3.E4 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) substituted in, and to analyze its relationship with the value process VV of the original optimal stopping problem.

Substituting ([3.4](https://arxiv.org/html/2602.18078v1#S3.E4 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) into the generator of ([3.3](https://arxiv.org/html/2602.18078v1#S3.E3 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) yields

|  |  |  |
| --- | --- | --- |
|  | ∫0nπs∗​(u)​[(Ps−Vsλ,n)​u−(Ps−Vsλ,n)​u−λ​ln⁡(1λ​(Ps−Vsλ,n)enλ​(Ps−Vsλ,n)−1)]​𝑑u\displaystyle\int^{n}\_{0}\pi^{\*}\_{s}(u)\left[(P\_{s}-V^{\lambda,n}\_{s})u-(P\_{s}-V^{\lambda,n}\_{s})u-\lambda\ln\left(\frac{\frac{1}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}{e^{\frac{n}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}-1}\right)\right]\,du |  |
|  |  |  |
| --- | --- | --- |
|  | =−λ​ln⁡(1λ​(Ps−Vsλ,n)enλ​(Ps−Vsλ,n)−1)=λ​ln⁡(enλ​(Ps−Vsλ,n)−1nλ​(Ps−Vsλ,n))+λ​ln⁡(n).\displaystyle\qquad=-\lambda\ln\left(\frac{\frac{1}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}{e^{\frac{n}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}-1}\right)=\lambda\ln\!\left(\frac{e^{\frac{n}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}-1}{\frac{n}{\lambda}(P\_{s}-V^{\lambda,n}\_{s})}\right)+\lambda\ln(n). |  |

To simplify notation, we introduce the functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(x)=1x​ln⁡(ex−1x)andΦ​(x)=ln⁡(ex−1x),x∈ℝ.\Psi(x)=\frac{1}{x}\ln\left(\frac{e^{x}-1}{x}\right)\quad\mathrm{and}\quad\Phi(x)=\ln\left(\frac{e^{x}-1}{x}\right),\quad x\in\mathbb{R}. |  | (3.6) |

The entropy-regularized BSDE ([3.3](https://arxiv.org/html/2602.18078v1#S3.E3 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) can then be rewritten as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtλ,n\displaystyle V^{\lambda,n}\_{t} | =PT−∫tT𝑑Msλ,n+∫tT(Ps−Vsλ,n)​n​Ψ​(Ps−Vsλ,nλ/n)​𝑑s+λ​ln⁡(n)​(T−t)\displaystyle=P\_{T}-\int^{T}\_{t}dM^{\lambda,n}\_{s}+\int^{T}\_{t}(P\_{s}-V^{\lambda,n}\_{s})n\Psi\left(\frac{P\_{s}-V^{\lambda,n}\_{s}}{\lambda/n}\right)ds+\lambda\ln(n)(T-t) |  | (3.7) |

or, equivalently,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtλ,n\displaystyle V^{\lambda,n}\_{t} | =PT−∫tT𝑑Msλ,n+∫tTn​[λn​Φ​(Ps−Vsλ,nλ/n)+λn​ln⁡(n)]​𝑑s.\displaystyle=P\_{T}-\int^{T}\_{t}dM^{\lambda,n}\_{s}+\int^{T}\_{t}n\left[\frac{\lambda}{n}\Phi\left(\frac{P\_{s}-V^{\lambda,n}\_{s}}{\lambda/n}\right)+\frac{\lambda}{n}\ln(n)\right]ds. |  | (3.8) |

###### Lemma 3.1.

For each n≥1n\geq 1, the entropy-regularized penalization scheme ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) is well posed. In particular, there exists a unique solution (Vλ,n,Mλ,n)∈𝒮2×ℋ2(V^{\lambda,n},M^{\lambda,n})\in\mathcal{S}^{2}\times\mathcal{H}^{2} to ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")).

###### Proof.

By Lemma [6.2](https://arxiv.org/html/2602.18078v1#S6.Thmlem2 "Lemma 6.2. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and Lemma [6.4](https://arxiv.org/html/2602.18078v1#S6.Thmlem4 "Lemma 6.4. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), the generator is Lipschitz continuous and, for any fixed nn and λ\lambda,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|λn​Φ​(Psλ/n)|2​𝑑s]<∞.\mathbb{E}\Big[\int^{T}\_{0}\left|\frac{\lambda}{n}\Phi\left(\frac{P\_{s}}{\lambda/n}\right)\right|^{2}ds\Big]<\infty. |  |

Existence and uniqueness then follow from Theorem 3.1 in Øksendal and Zhang [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)]. ∎

### 3.1 Convergence to the American Option

In this subsection, we analyze the asymptotic behaviour of the entropy-regularized penalization scheme ([3.7](https://arxiv.org/html/2602.18078v1#S3.E7 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). For any fixed n≥1n\geq 1, we show that Vλ,nV^{\lambda,n} converges to the classical penalized value VnV^{n} defined by ([3.2](https://arxiv.org/html/2602.18078v1#S3.E2 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) as λ↓0\lambda\downarrow 0. Moreover, Theorem [3.1](https://arxiv.org/html/2602.18078v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") establishes that if the truncation parameter nn is chosen so that λ​ln⁡(n)→0\lambda\ln(n)\to 0 (for instance n=1/λn=1/\lambda), then Vλ,nV^{\lambda,n} converges to the American option value VV as λ→0\lambda\to 0. This result underpins our numerical methodology.

For t∈[0,T]t\in[0,T], define

|  |  |  |
| --- | --- | --- |
|  | Γtλ,n:=∫0tn​Ψ​(Ps−Vsλ,nλ/n)​𝑑s.\displaystyle\Gamma^{\lambda,n}\_{t}:=\int\_{0}^{t}n\,\Psi\!\left(\frac{P\_{s}-V^{\lambda,n}\_{s}}{\lambda/n}\right)ds. |  |

By Lemma [6.1](https://arxiv.org/html/2602.18078v1#S6.Thmlem1 "Lemma 6.1. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), Γλ,n\Gamma^{\lambda,n} is a bounded, non-decreasing hazard process as the integrand is non-negative and bounded by nn. Applying Itô’s formula to e−Γtλ,n​(Vtλ,n+λ​ln⁡(n)​t)e^{-\Gamma^{\lambda,n}\_{t}}(V^{\lambda,n}\_{t}+\lambda\ln(n)t) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ,n+λ​ln⁡(n)​t\displaystyle V^{\lambda,n}\_{t}+\lambda\ln(n)t | =𝔼​[(PT+λ​ln⁡(n)​T)​e−(ΓTλ,n−Γtλ,n)+∫]t,T](Pu+λ​ln⁡(n)​u)​e−(Γuλ,n−Γtλ,n)​𝑑Γuλ,n|ℱt].\displaystyle=\mathbb{E}\Big[(P\_{T}+\lambda\ln(n)T)e^{-(\Gamma^{\lambda,n}\_{T}-\Gamma^{\lambda,n}\_{t})}+\int\_{]t,T]}(P\_{u}+\lambda\ln(n)u)e^{-(\Gamma^{\lambda,n}\_{u}-\Gamma^{\lambda,n}\_{t})}d\Gamma\_{u}^{\lambda,n}\,\Big|{\mathcal{F}}\_{t}\Big]. |  |

Using the link between randomized and classical optimal stopping ([1.2](https://arxiv.org/html/2602.18078v1#S1.E2 "In 1 Introduction ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤Vtλ,n+λ​ln⁡(n)​t≤ess​supτ∈𝒯t,T⁡𝔼​[Pτ∧T+λ​ln⁡(n)​(T∧τ)|ℱt]≤Vt+λ​ln⁡(n)​T.\displaystyle 0\leq V^{\lambda,n}\_{t}+\lambda\ln(n)t\leq\operatornamewithlimits{ess\,sup}\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}\big[P\_{\tau\wedge T}+\lambda\ln(n)(T\wedge\tau)\,\big|{\mathcal{F}}\_{t}\big]\leq V\_{t}+\lambda\ln(n)T. |  | (3.9) |

Hence, if the penalization parameter nn is chosen in such a way that λ​ln⁡(n)→0\lambda\ln(n)\rightarrow 0 as λ→0\lambda\rightarrow 0, the approximation Vλ,nV^{\lambda,n} converges to the American value process VV as λ→0\lambda\rightarrow 0.

Finally, the presence of the correction term λ​ln⁡(n)​(T−t)\lambda\ln(n)(T-t) in ([3.7](https://arxiv.org/html/2602.18078v1#S3.E7 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) prevents a direct comparison with the classical penalization scheme. To overcome this difficulty, we introduce the auxiliary BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~tλ,n\displaystyle\widetilde{V}^{\lambda,n}\_{t} | =PT−∫tT𝑑Msλ,n+∫tTn​[λn​Φ​(Ps−V~sλ,nλ/n)]​𝑑s.\displaystyle=P\_{T}-\int^{T}\_{t}dM^{\lambda,n}\_{s}+\int^{T}\_{t}n\left[\frac{\lambda}{n}\Phi\left(\frac{P\_{s}-\widetilde{V}^{\lambda,n}\_{s}}{\lambda/n}\right)\right]ds. |  |

This equation is well posed, since the driver is Lipschitz continuous with constant nn by Lemma [6.2](https://arxiv.org/html/2602.18078v1#S6.Thmlem2 "Lemma 6.2. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), and P∈𝒮2P\in\mathcal{S}^{2}. Setting d​Γ~sλ,n=n​Ψ​(Ps−V~sλ,nλ/n)​d​sd\widetilde{\Gamma}\_{s}^{\lambda,n}=n\Psi\left(\frac{P\_{s}-\widetilde{V}^{\lambda,n}\_{s}}{\lambda/n}\right)ds and applying Itô’s formula to e−Γ~tλ,n​V~tλ,ne^{-\widetilde{\Gamma}^{\lambda,n}\_{t}}\widetilde{V}^{\lambda,n}\_{t}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~tλ,n\displaystyle\widetilde{V}^{\lambda,n}\_{t} | =𝔼​[PT​e−(Γ~Tλ,n−Γ~tλ,n)+∫tTPu​e−(Γ~uλ,n−Γ~tλ,n)​𝑑Γ~uλ,n|ℱt],t∈[0,T].\displaystyle=\mathbb{E}\Big[P\_{T}e^{-(\widetilde{\Gamma}^{\lambda,n}\_{T}-\widetilde{\Gamma}^{\lambda,n}\_{t})}+\int^{T}\_{t}P\_{u}e^{-(\widetilde{\Gamma}^{\lambda,n}\_{u}-\widetilde{\Gamma}^{\lambda,n}\_{t})}d\widetilde{\Gamma}\_{u}^{\lambda,n}\Big|{\mathcal{F}}\_{t}\Big],\quad t\in[0,T]. |  |

By the comparison theorem for BSDEs (see, e.g., Theorem 3.4 in [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)]), for all t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~tλ,n≤Vtn≤Vt,a.s.\widetilde{V}^{\lambda,n}\_{t}\leq V^{n}\_{t}\leq V\_{t},\quad a.s. |  | (3.10) |

recalling that VnV^{n} denotes the classical penalization scheme introduced in ([3.2](https://arxiv.org/html/2602.18078v1#S3.E2 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")).

###### Remark 3.1.

The process V~λ,n\widetilde{V}^{\lambda,n} admits a natural variational interpretation. Consider the BSDE

|  |  |  |
| --- | --- | --- |
|  | Xt=PT−∫tT𝑑Ms+ess​supπ∈Πn⁡{∫tT∫0n(Ps−Xs)​u​πs​(u)−λ​πs​(u)​ln⁡(πs​(u)n−1)​d​u​d​s},\displaystyle X\_{t}=P\_{T}-\int^{T}\_{t}dM\_{s}+\operatornamewithlimits{ess\,sup}\_{\pi\in\Pi\_{n}}\left\{\int^{T}\_{t}\int^{n}\_{0}(P\_{s}-X\_{s})u\pi\_{s}(u)-\lambda\pi\_{s}(u)\ln\left(\frac{\pi\_{s}(u)}{n^{-1}}\right)duds\right\}, |  |

where the entropy term corresponds to the Kullback–Leibler divergence of πs\pi\_{s} with respect to the uniform distribution on [0,n][0,n]. Using ([3.4](https://arxiv.org/html/2602.18078v1#S3.E4 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) together with uniqueness of solutions yields X=V~λ,nX=\widetilde{V}^{\lambda,n}.

###### Theorem 3.1.

For any positive integer nn, any 0≤λ<10\leq\lambda<1 and any t∈[0,T]t\in[0,T], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vtn−Vtλ,n|\displaystyle|V^{n}\_{t}-V^{\lambda,n}\_{t}| | ≤2​(T−t)​(1−ln⁡(1−e−1)+𝔼​[sups∈[t,T]ln⁡(Vs∨1)|ℱt])​(λ−λ​ln⁡(λ)+λ​ln⁡(n)),a.s.\displaystyle\leq 2(T-t)\big(1-\ln(1-e^{-1})+\mathbb{E}\big[\sup\_{s\in[t,T]}\ln(V\_{s}\vee 1)\big|{\mathcal{F}}\_{t}\big]\big)\big(\lambda-\lambda\ln(\lambda)+\lambda\ln(n)\big),\quad a.s. |  |

If the payoff process PP is bounded by a constant P∞P\_{\infty}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup0≤t≤T|Vtn−Vtλ,n|\displaystyle\sup\_{0\leq t\leq T}|V^{n}\_{t}-V^{\lambda,n}\_{t}| | ≤2​T​(1.5+ln⁡(P∞∨1))​(λ−λ​ln⁡(λ)+λ​ln⁡(n)),a.s.\displaystyle\leq 2T(1.5+\ln(P\_{\infty}\vee 1))\big(\lambda-\lambda\ln(\lambda)+\lambda\ln(n)\big),\quad a.s. |  |

###### Proof.

*Step 1.* By taking the difference between VnV^{n} and V~λ,n\widetilde{V}^{\lambda,n}, we obtain

|  |  |  |
| --- | --- | --- |
|  | Vtn−V~tλ,n=∫]t,T]d​(Mλ,n−Mn)s+∫[t,T[n​[(Ps−Vsn)+−λn​Φ​(Ps−V~sλ,nλ/n)]​𝑑s.V^{n}\_{t}-\widetilde{V}^{\lambda,n}\_{t}=\int\_{]t,T]}d(M^{\lambda,n}-M^{n})\_{s}+\int\_{[t,T[}n\left[(P\_{s}-V\_{s}^{n})^{+}-\frac{\lambda}{n}\Phi\left(\frac{P\_{s}-\widetilde{V}\_{s}^{\lambda,n}}{\lambda/n}\right)\right]ds. |  |

Taking c=ϵ=λ/nc=\epsilon=\lambda/n in Lemma [6.4](https://arxiv.org/html/2602.18078v1#S6.Thmlem4 "Lemma 6.4. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and using ([3.10](https://arxiv.org/html/2602.18078v1#S3.E10 "In 3.1 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtn−V~tλ,n\displaystyle V^{n}\_{t}-\widetilde{V}^{\lambda,n}\_{t} | ≤𝔼​[∫[t,T[n​[(Ps−Vsn)+−λn​Φ​(Ps−Vsnλ/n)]​𝑑s]\displaystyle\leq\mathbb{E}\left[\int\_{[t,T[}n\left[(P\_{s}-V\_{s}^{n})^{+}-\frac{\lambda}{n}\Phi\left(\frac{P\_{s}-V\_{s}^{n}}{\lambda/n}\right)\right]ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[∫[t,T[[λ−λ​ln⁡(1−e−1)+λ​ln⁡(|Ps−Vsn|∨1)−λ​ln⁡(λ)+λ​ln⁡(n)]|ℱt]\displaystyle\leq\mathbb{E}\left[\int\_{[t,T[}\left[\lambda-\lambda\ln(1-e^{-1})+\lambda\ln(|P\_{s}-V^{n}\_{s}|\vee 1)-\lambda\ln(\lambda)+\lambda\ln(n)\right]\Bigg|{\mathcal{F}}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(T−t)​(1−ln⁡(1−e−1)+𝔼​[sups∈[t,T]ln⁡(Vs∨1)|ℱt])​(λ−λ​ln⁡(λ)+λ​ln⁡(n)).\displaystyle\leq(T-t)\Big(1-\ln(1-e^{-1})+\mathbb{E}\Big[\sup\_{s\in[t,T]}\ln(V\_{s}\vee 1)\Big|{\mathcal{F}}\_{t}\Big]\Big)\big(\lambda-\lambda\ln(\lambda)+\lambda\ln(n)\big). |  |

*Step 2.* On the other hand, from the comparison theorem for BSDEs, see again Theorem 3.4 in [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)], we know that V~λ,n≤Vλ,n\widetilde{V}^{\lambda,n}\leq V^{\lambda,n}. Hence, since x↦Φ​(c−1​(P−x))x\mapsto\Phi(c^{-1}(P-x)) is non-increasing, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ,n−V~tλ,n\displaystyle V^{\lambda,n}\_{t}-\widetilde{V}^{\lambda,n}\_{t} | =𝔼​[∫tTλ​[Φ​(Ps−Vsλ,nλ/n)−Φ​(Ps−V~sλ,nλ/n)]​𝑑s|ℱt]+λ​ln⁡(n)​(T−t)\displaystyle=\mathbb{E}\left[\int^{T}\_{t}\lambda\left[\Phi\left(\frac{P\_{s}-V^{\lambda,n}\_{s}}{\lambda/n}\right)-\Phi\left(\frac{P\_{s}-\widetilde{V}^{\lambda,n}\_{s}}{\lambda/n}\right)\right]ds\Bigg|{\mathcal{F}}\_{t}\right]+\lambda\ln(n)(T-t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤λ​ln⁡(n)​(T−t).\displaystyle\leq\lambda\ln(n)(T-t). |  |

Combining the previous bounds yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Vtn−Vtλ,n|\displaystyle|V^{n}\_{t}-V^{\lambda,n}\_{t}| | ≤|Vtn−V~tλ,n|+|V~tλ,n−Vtλ,n|\displaystyle\leq|V^{n}\_{t}-\widetilde{V}^{\lambda,n}\_{t}|+|\widetilde{V}^{\lambda,n}\_{t}-V^{\lambda,n}\_{t}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(T−t)​(1−ln⁡(1−e−1)+𝔼​[sups∈[t,T]ln⁡(Vs∨1)|ℱt])​(λ−λ​ln⁡(λ)+2​λ​ln⁡(n)).\displaystyle\leq(T-t)\Big(1-\ln(1-e^{-1})+\mathbb{E}\Big[\sup\_{s\in[t,T]}\ln(V\_{s}\vee 1)\Big|{\mathcal{F}}\_{t}\Big]\Big)\big(\lambda-\lambda\ln(\lambda)+2\lambda\ln(n)\big). |  |

Finally, if PP is essentially bounded, then sups∈[t,T]Vs≤P∞\sup\_{s\in[t,T]}V\_{s}\leq P\_{\infty} so that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sups∈[t,T]ln⁡(Vs∨1)|ℱt]≤ln⁡(P∞∨1).\mathbb{E}\Big[\sup\_{s\in[t,T]}\ln(V\_{s}\vee 1)\Big|{\mathcal{F}}\_{t}\Big]\leq\ln(P\_{\infty}\vee 1). |  |

∎

Finally, classical arguments (see Steps 2–3 of Theorem 4.1 in [[26](https://arxiv.org/html/2602.18078v1#bib.bib26)]) ensure that Vn→VV^{n}\to V as n→∞n\to\infty. Theorem [3.1](https://arxiv.org/html/2602.18078v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") then implies that choosing n=n​(λ)n=n(\lambda) such that λ​ln⁡n→0\lambda\ln n\to 0 guarantees convergence of Vλ,nV^{\lambda,n} to VV as λ→0\lambda\to 0. In particular, if PP is bounded and n=1/λn=1/\lambda, then

|  |  |  |
| --- | --- | --- |
|  | |Vt1λ−Vtλ,1λ|≤C​(λ−λ​ln⁡λ).\displaystyle|V^{\frac{1}{\lambda}}\_{t}-V^{\lambda,\frac{1}{\lambda}}\_{t}|\leq C(\lambda-\lambda\ln\lambda). |  |

To obtain an explicit convergence rate towards VV, estimates of the classical penalization error V−VnV-V^{n} are required. Such results typically require additional structure on the payoff process PP and the filtration 𝔽\mathbb{F}. In the Brownian setting, one may impose the following assumption (see El Karoui *et al.* [[19](https://arxiv.org/html/2602.18078v1#bib.bib19)] and Gobet and Wang [[22](https://arxiv.org/html/2602.18078v1#bib.bib22)]):

###### Assumption 3.2.

The filtration 𝔽{\mathbb{F}} is a Brownian filtration, and the payoff process PP admits a generalized semimartingale decomposition as

|  |  |  |
| --- | --- | --- |
|  | Pt=P0+∫0tUs​𝑑s+∫0tVs​𝑑Ws+Ht,P\_{t}=P\_{0}+\int\_{0}^{t}U\_{s}ds+\int\_{0}^{t}V\_{s}dW\_{s}+H\_{t}, |  |

where U,V∈𝒮2U,V\in\mathcal{S}^{2}, and HH is continuous, non-decreasing, with HT∈L2H\_{T}\in L^{2} and H0=0H\_{0}=0.

###### Corollary 3.1.

Assume that PP is bounded and that Assumption [3.2](https://arxiv.org/html/2602.18078v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.1 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") holds. If

|  |  |  |
| --- | --- | --- |
|  | κ¯∞:=ess​sup(t,ω)∈[0,T]×Ω⁡Ut−​(ω)<∞,\overline{\kappa}\_{\infty}:=\operatornamewithlimits{ess\,sup}\_{(t,\omega)\in[0,T]\times\Omega}U\_{t}^{-}(\omega)<\infty, |  |

then we have

|  |  |  |
| --- | --- | --- |
|  | sup0≤t≤T|Vt−Vtλ,1λ|≤C​κ¯∞​(λ−λ​ln⁡λ),a.s.\displaystyle\sup\_{0\leq t\leq T}|V\_{t}-V^{\lambda,\frac{1}{\lambda}}\_{t}|\leq C\overline{\kappa}\_{\infty}(\lambda-\lambda\ln\lambda),\quad a.s. |  |

###### Proof.

By Theorem 3.5 (and Remarks 3.6-3.7) in [[22](https://arxiv.org/html/2602.18078v1#bib.bib22)],

|  |  |  |
| --- | --- | --- |
|  | 0≤Vt−Vtn≤κ¯∞n.0\leq V\_{t}-V^{n}\_{t}\leq\frac{\overline{\kappa}\_{\infty}}{n}. |  |

Choosing n=1/λn=1/\lambda and combining with Theorem [3.1](https://arxiv.org/html/2602.18078v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") yields the result.
∎

### 3.2 Policy Improvement Algorithm

In this subsection, we present a PIA for computing Vλ,nV^{\lambda,n} and analyze its convergence. Policy improvement methods are classical tools in stochastic control, providing a constructive iterative procedure that alternates between policy optimization and value evaluation, often leading to fast and numerically stable convergence.

Fix λ∈(0,1]\lambda\in(0,1] and let π=(πs)s∈[0,T]∈Πn\pi=(\pi\_{s})\_{s\in[0,T]}\in\Pi\_{n} be a conditional density process. Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(s,x,πs)\displaystyle G(s,x,\pi\_{s}) | :=∫0n{(Ps−x)​u​πs​(u)−λ​πs​(u)​ln⁡(πs​(u))}​𝑑u,\displaystyle:=\int^{n}\_{0}\Big\{(P\_{s}-x)u\pi\_{s}(u)-\lambda\pi\_{s}(u)\ln(\pi\_{s}(u))\Big\}du, |  |

and denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πs∗​(x,u):=argmaxπ​G​(s,x,πs​(u))=1λ​(Ps−x)enλ​(Ps−x)−1​e1λ​(Ps−x)​u,u∈[0,n],\pi^{\*}\_{s}(x,u):=\textrm{argmax}\_{\pi}G(s,x,\pi\_{s}(u))=\frac{\frac{1}{\lambda}(P\_{s}-x)}{e^{\frac{n}{\lambda}(P\_{s}-x)}-1}e^{\frac{1}{\lambda}(P\_{s}-x)u},\quad u\in[0,n], |  | (3.11) |

the optimal policy associated with the state xx.

Motivated by Corollary [3.1](https://arxiv.org/html/2602.18078v1#S3.Thmcor1 "Corollary 3.1. ‣ 3.1 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), we fix the truncation level n:=1/λn:=1/\lambda and set

|  |  |  |
| --- | --- | --- |
|  | 𝒱λ:=Vλ,1λ.\mathscr{V}^{\lambda}:=V^{\lambda,\frac{1}{\lambda}}. |  |

Let 𝒱λ,0\mathscr{V}^{\lambda,0} be an initial guess, e.g.

|  |  |  |
| --- | --- | --- |
|  | 𝒱tλ,0:=𝔼​[PT|ℱt],t∈[0,T].\mathscr{V}^{\lambda,0}\_{t}:=\mathbb{E}[P\_{T}|\mathcal{F}\_{t}],\quad t\in[0,T]. |  |

Given 𝒱λ,m\mathscr{V}^{\lambda,m}, the (m+1)(m+1)-th iteration consists of:

*Policy update.*

|  |  |  |  |
| --- | --- | --- | --- |
|  | πsm+1​(u):=πs∗​(𝒱sλ,m,u)=1λ​(Ps−𝒱sλ,m)enλ​(Ps−𝒱sλ,m)−1​e1λ​(Ps−𝒱sλ,m)​u,u∈[0,n].\pi^{m+1}\_{s}(u):=\pi\_{s}^{\*}(\mathscr{V}^{\lambda,m}\_{s},u)=\frac{\frac{1}{\lambda}(P\_{s}-\mathscr{V}^{\lambda,m}\_{s})}{e^{\frac{n}{\lambda}(P\_{s}-\mathscr{V}^{\lambda,m}\_{s})}-1}e^{\frac{1}{\lambda}(P\_{s}-\mathscr{V}^{\lambda,m}\_{s})u},\qquad u\in[0,n]. |  | (3.12) |

*Policy evaluation.*

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱tλ,m+1=PT−(𝒩Tλ,m+1−𝒩tλ,m+1)+∫tTG​(s,𝒱sλ,m+1,πsm+1)​𝑑s,\mathscr{V}^{\lambda,m+1}\_{t}=P\_{T}-(\mathscr{N}^{\lambda,m+1}\_{T}-\mathscr{N}^{\lambda,m+1}\_{t})+\int\_{t}^{T}G(s,\mathscr{V}^{\lambda,m+1}\_{s},\pi^{m+1}\_{s})\,ds, |  | (3.13) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(s,𝒱sλ,m+1,πsm+1)=λ​Φ​(Ps−𝒱sλ,mλ/n)+λ​ln⁡n+(𝒱sλ,m−𝒱sλ,m+1)​μπsm+1,G(s,\mathscr{V}^{\lambda,m+1}\_{s},\pi^{m+1}\_{s})=\lambda\Phi\!\left(\frac{P\_{s}-\mathscr{V}^{\lambda,m}\_{s}}{\lambda/n}\right)+\lambda\ln n+(\mathscr{V}^{\lambda,m}\_{s}-\mathscr{V}^{\lambda,m+1}\_{s})\,\mu\_{\pi^{m+1}\_{s}}, |  | (3.14) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | μπsm+1=∫0nu​πsm+1​(u)​𝑑u=n1−e−αsm​n−1αsm,αsm:=Ps−𝒱sλ,mλ.\mu\_{\pi^{m+1}\_{s}}=\int\_{0}^{n}u\,\pi^{m+1}\_{s}(u)\,du=\frac{n}{1-e^{-\alpha\_{s}^{m}n}}-\frac{1}{\alpha\_{s}^{m}},\qquad\alpha\_{s}^{m}:=\frac{P\_{s}-\mathscr{V}^{\lambda,m}\_{s}}{\lambda}. |  | (3.15) |

Each iteration requires solving
the linear BSDE ([3.13](https://arxiv.org/html/2602.18078v1#S3.E13 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), and computing πm+1∈Πn\pi^{m+1}\in\Pi\_{n} defined by ([3.12](https://arxiv.org/html/2602.18078v1#S3.E12 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). Moreover, since

|  |  |  |
| --- | --- | --- |
|  | G​(s,𝒱sλ,m,πsm+1)=G​(s,𝒱sλ,m,πs∗​(𝒱sλ,m))≥G​(s,𝒱sλ,m,πsm),G(s,\mathscr{V}^{\lambda,m}\_{s},\pi^{m+1}\_{s})=G(s,\mathscr{V}^{\lambda,m}\_{s},\pi\_{s}^{\*}(\mathscr{V}^{\lambda,m}\_{s}))\geq G(s,\mathscr{V}^{\lambda,m}\_{s},\pi^{m}\_{s}), |  |

the comparison theorem for BSDEs (Theorem 3.4 in [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)]) implies that for any integer mm and any t∈[0,T]t\in[0,T]

|  |  |  |
| --- | --- | --- |
|  | 𝒱tλ,m+1≥𝒱tλ,m,a.s.\mathscr{V}^{\lambda,m+1}\_{t}\geq\mathscr{V}^{\lambda,m}\_{t},\quad a.s. |  |

so that the sequence (𝒱tλ,m)m≥1(\mathscr{V}^{\lambda,m}\_{t})\_{m\geq 1} is monotonically non-decreasing.

###### Remark 3.2.

If the term λ​ln⁡n\lambda\ln n is removed from the driver ([3.14](https://arxiv.org/html/2602.18078v1#S3.E14 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), the same construction yields a PIA for V~λ,1/λ\widetilde{V}^{\lambda,1/\lambda}, with V~tλ,1/λ≤Vt\widetilde{V}^{\lambda,1/\lambda}\_{t}\leq V\_{t}, t∈[0,T]t\in[0,T].

###### Theorem 3.2.

For any fixed λ≥0\lambda\geq 0 and t∈[0,T)t\in[0,T), it holds

|  |  |  |
| --- | --- | --- |
|  | 0≤𝒱tλ−𝒱tλ,m≤(n​T)mm!​𝔼​[sups≤T(𝒱sλ,1−𝒱sλ,0)|ℱt],a.s.\displaystyle 0\leq\mathscr{V}\_{t}^{\lambda}-\mathscr{V}\_{t}^{\lambda,m}\leq\frac{(nT)^{m}}{m!}\mathbb{E}[\sup\_{s\leq T}(\mathscr{V}^{\lambda,1}\_{s}-\mathscr{V}^{\lambda,0}\_{s})\,|\,{\mathcal{F}}\_{t}],\quad a.s. |  |

where n=1/λn=1/\lambda is the truncation parameter.

###### Proof.

Fix t∈[0,T)t\in[0,T) and consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱tλ,m+1−𝒱tλ,m\displaystyle\mathscr{V}\_{t}^{\lambda,m+1}-\mathscr{V}\_{t}^{\lambda,m} | =−(𝒩Tλ,m+1−𝒩Tλ,m)+(𝒩tλ,m+1−𝒩tλ,m)\displaystyle=-(\mathscr{N}\_{T}^{\lambda,m+1}-\mathscr{N}\_{T}^{\lambda,m})+(\mathscr{N}\_{t}^{\lambda,m+1}-\mathscr{N}\_{t}^{\lambda,m}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tT{G​(s,𝒱sλ,m+1,πsm+1)−G​(s,𝒱sλ,m,πsm)}​𝑑s.\displaystyle\quad+\int^{T}\_{t}\left\{G(s,\mathscr{V}\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})-G(s,\mathscr{V}\_{s}^{\lambda,m},\pi\_{s}^{m})\right\}ds. |  | (3.16) |

Since 𝒱λ,m+1≥𝒱λ,m\mathscr{V}^{\lambda,m+1}\geq\mathscr{V}^{\lambda,m} and Φ\Phi is non-decreasing,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | G​(s,𝒱sλ,m+1,πsm+1)−G​(s,𝒱sλ,m,πsm)\displaystyle G(s,\mathscr{V}\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})-G(s,\mathscr{V}\_{s}^{\lambda,m},\pi\_{s}^{m}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​Φ​(Ps−𝒱sλ,mλ/n)−λ​Φ​(Ps−𝒱sλ,m−1λ/n)+(𝒱sλ,m−𝒱sλ,m+1)​μπsm+1−(𝒱sλ,m−1−𝒱sλ,m)​μπsm\displaystyle=\lambda\Phi\left(\frac{P\_{s}-\mathscr{V}\_{s}^{\lambda,m}}{\lambda/n}\right)-\lambda\Phi\left(\frac{P\_{s}-\mathscr{V}\_{s}^{\lambda,m-1}}{\lambda/n}\right)+(\mathscr{V}\_{s}^{\lambda,m}-\mathscr{V}\_{s}^{\lambda,m+1})\mu\_{\pi\_{s}^{m+1}}-(\mathscr{V}\_{s}^{\lambda,m-1}-\mathscr{V}\_{s}^{\lambda,m})\mu\_{\pi\_{s}^{m}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤n​(𝒱sλ,m−𝒱sλ,m−1).\displaystyle\leq n(\mathscr{V}\_{s}^{\lambda,m}-\mathscr{V}\_{s}^{\lambda,m-1}). |  | (3.17) |

By the Fubini-Tonelli theorem and iterating, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤𝒱tλ,m+1−𝒱tλ,m\displaystyle 0\leq\mathscr{V}^{\lambda,m+1}\_{t}-\mathscr{V}^{\lambda,m}\_{t} | =𝔼​[∫tT{G​(s,𝒱sλ,m+1,πsm+1)−G​(s,𝒱sλ,m,πsm)}​𝑑s|ℱt]\displaystyle=\mathbb{E}[\int^{T}\_{t}\left\{G(s,\mathscr{V}\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})-G(s,\mathscr{V}\_{s}^{\lambda,m},\pi\_{s}^{m})\right\}\,ds\,|\,{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤n​𝔼​[∫tT(𝒱tm−1λ,m−𝒱tm−1λ,m−1)​𝑑tm−1|ℱt]\displaystyle\leq n\mathbb{E}[\int^{T}\_{t}(\mathscr{V}^{\lambda,m}\_{t\_{m-1}}-\mathscr{V}^{\lambda,m-1}\_{t\_{m-1}})d{t\_{m-1}}\,|\,{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤nm​𝔼​[∫tT∫tm−1T…​∫t1T(𝒱t0λ,1−𝒱t0λ,0)​𝑑t0​…​𝑑tm−2​𝑑tm−1|ℱt]\displaystyle\leq n^{m}\mathbb{E}[\int^{T}\_{t}\int^{T}\_{t\_{m-1}}\dots\int^{T}\_{t\_{1}}(\mathscr{V}^{\lambda,1}\_{t\_{0}}-\mathscr{V}^{\lambda,0}\_{t\_{0}})\,dt\_{0}\dots dt\_{m-2}dt\_{m-1}\,|\,{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(n​T)mm!​𝔼​[sups≤T(𝒱sλ,1−𝒱sλ,0)|ℱt].\displaystyle\leq\frac{(nT)^{m}}{m!}\mathbb{E}\big[\sup\_{s\leq T}(\mathscr{V}^{\lambda,1}\_{s}-\mathscr{V}^{\lambda,0}\_{s})\,\big|\,{\mathcal{F}}\_{t}\big]. |  |

To obtain the convergence to 𝒱λ\mathscr{V}^{\lambda}, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(s,𝒱sλ,πs∗​(𝒱sλ))\displaystyle G(s,\mathscr{V}\_{s}^{\lambda},\pi^{\*}\_{s}(\mathscr{V}^{\lambda}\_{s})) | −G​(s,𝒱sλ,m+1,πsm+1)\displaystyle-G(s,\mathscr{V}\_{s}^{\lambda,m+1},\pi\_{s}^{m+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​Φ​(Ps−𝒱sλλ/n)−λ​Φ​(Ps−𝒱sλ,mλ/n)−(𝒱sλ,m−𝒱sλ,m+1)​μπsm\displaystyle=\lambda\Phi\left(\frac{P\_{s}-\mathscr{V}\_{s}^{\lambda}}{\lambda/n}\right)-\lambda\Phi\left(\frac{P\_{s}-\mathscr{V}\_{s}^{\lambda,m}}{\lambda/n}\right)-(\mathscr{V}\_{s}^{\lambda,m}-\mathscr{V}\_{s}^{\lambda,m+1})\mu\_{\pi\_{s}^{m}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤n​(𝒱sλ,m+1−𝒱sλ,m).\displaystyle\leq n(\mathscr{V}\_{s}^{\lambda,m+1}-\mathscr{V}\_{s}^{\lambda,m}). |  |

Hence, from similar computations and noting that G​(s,𝒱sλ,m+1,πsm+1)≤G​(s,𝒱sλ,m+1,πs∗​(𝒱sλ,m+1))G(s,\mathscr{V}^{\lambda,m+1}\_{s},\pi\_{s}^{m+1})\leq G(s,\mathscr{V}\_{s}^{\lambda,m+1},\pi^{\*}\_{s}(\mathscr{V}\_{s}^{\lambda,m+1})),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤𝒱tλ−𝒱tλ,m+1\displaystyle 0\leq\mathscr{V}^{\lambda}\_{t}-\mathscr{V}^{\lambda,m+1}\_{t} | =𝔼​[∫tT{G​(s,𝒱sλ,πs∗​(𝒱sλ))−G​(s,𝒱sλ,m+1,πsm+1)}​𝑑s|ℱt]\displaystyle=\mathbb{E}\Big[\int^{T}\_{t}\left\{G(s,\mathscr{V}\_{s}^{\lambda},\pi^{\*}\_{s}(\mathscr{V}^{\lambda}\_{s}))-G(s,\mathscr{V}\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})\right\}\,ds\,\Big|\,{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(n​T)m+1(m+1)!​𝔼​[sups≤T(𝒱sλ,1−𝒱sλ,0)|ℱt].\displaystyle\leq\frac{(nT)^{m+1}}{(m+1)!}\mathbb{E}\big[\sup\_{s\leq T}(\mathscr{V}^{\lambda,1}\_{s}-\mathscr{V}^{\lambda,0}\_{s})\,\big|\,{\mathcal{F}}\_{t}\big]. |  |

Choosing n=1/λn=1/\lambda concludes the proof.
∎

## 4 Limit of the Entropy-Regularized Penalization Scheme

This section is devoted to the analysis of the asymptotic behavior of the entropy-regularized penalization scheme ([3.3](https://arxiv.org/html/2602.18078v1#S3.E3 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) as the truncation
parameter n→∞n\to\infty, for a fixed temperature parameter λ∈(0,1]\lambda\in(0,1]. Our objective is threefold. First, we study the convergence properties of the scheme and quantify the approximation of the American option value induced by the entropy regularization. Second, we identify the limiting object as the value component of a reflected BSDE with a logarithmically singular generator.
Third, we provide a financial interpretation of this limiting formulation, highlighting the economic meaning of the entropy regularization in terms of default risk and early exercise features. Although the results presented here do not contribute directly to the numerical pricing of American options, they provide a rigorous probabilistic foundation for the entropy-regularized approach and offer structural insights into the link between regularization, reflected BSDEs with singular drivers, and optimal stopping under risk-sensitive distortions.

For n≥1n\geq 1 we introduce the continuous function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φn​(x):=ln⁡(en​x−1x),x∈ℝ∖{0},\Phi\_{n}(x):=\ln\!\left(\frac{e^{nx}-1}{x}\right),\qquad x\in\mathbb{R}\setminus\{0\}, |  | (4.1) |

and, by continuity, we extend this definition at the origin by setting Φn​(0):=ln⁡(n)\Phi\_{n}(0):=\ln(n), and let Φn−1\Phi\_{n}^{-1} denote its inverse (see Lemma [6.3](https://arxiv.org/html/2602.18078v1#S6.Thmlem3 "Lemma 6.3. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). Furthermore, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φλ,n​(s,x):=λ​ln⁡(en​(Ps−x)/λ−1(Ps−x)/λ)=λ​Φn​(Ps−xλ)=λ​Φ​(Ps−xλ/n)+λ​ln⁡(n),\Phi\_{\lambda,n}(s,x):=\lambda\ln\!\left(\frac{e^{\,n(P\_{s}-x)/\lambda}-1}{(P\_{s}-x)/\lambda}\right)=\lambda\,\Phi\_{n}\!\left(\frac{P\_{s}-x}{\lambda}\right)=\lambda\,\Phi\!\left(\frac{P\_{s}-x}{\lambda/n}\right)+\lambda\ln(n), |  | (4.2) |

and we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞Φλ,n​(s,x)=Φλ,∞​(s,x):={λ​ln⁡(λx−Ps)x>Ps,∞x≤Ps.\displaystyle\lim\_{n\rightarrow\infty}\Phi\_{\lambda,n}(s,x)=\Phi\_{\lambda,\infty}(s,x)= |  | (4.3) |

The entropy-regularized penalization scheme Vλ,nV^{\lambda,n} in ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ,n=PT−∫tT𝑑Msλ,n+∫tTΦλ,n​(s,Vsλ,n)​𝑑s,V^{\lambda,n}\_{t}=P\_{T}-\int\_{t}^{T}dM\_{s}^{\lambda,n}+\int\_{t}^{T}\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s})\,ds, |  | (4.4) |

which is also well-posed since x↦Φλ,n​(s,x)x\mapsto\Phi\_{\lambda,n}(s,x) is Lipschitz continuous and P∈𝒮2P\in\mathcal{S}^{2}, see e.g. [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)]. Furthermore, for x∈ℝ∖{0}x\in\mathbb{R}\setminus\{0\} and n≥1n\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​n​[Φn​(x)]=dd​n​[ln⁡(en​x−1x)]=x​en​xen​x−1=x1−e−n​x≥0,\frac{d}{dn}[\Phi\_{n}(x)]=\frac{d}{dn}\Big[\ln\!\left(\frac{e^{nx}-1}{x}\right)\Big]=\frac{xe^{nx}}{e^{nx}-1}=\frac{x}{1-e^{-nx}}\geq 0, |  | (4.5) |

and dd​n​[Φn​(0)]=1n≥0\frac{d}{dn}[\Phi\_{n}(0)]=\frac{1}{n}\geq 0.

Hence, for any x∈ℝx\in\mathbb{R} and any n≥1n\geq 1, we have Φλ,n​(s,x)≤Φλ,n+1​(s,x)\Phi\_{\lambda,n}(s,x)\leq\Phi\_{\lambda,n+1}(s,x). By the comparison theorem (Theorem 3.4 in [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)]), this monotonicity implies that for all integer nn and all t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ,n≤Vtλ,n+1,a.s.V^{\lambda,n}\_{t}\;\leq\;V^{\lambda,n+1}\_{t},\qquad\;\text{a.s.} |  | (4.6) |

Therefore, for all t∈[0,T]t\in[0,T], the limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ:=limn→∞Vtλ,nV^{\lambda}\_{t}:=\lim\_{n\to\infty}V^{\lambda,n}\_{t} |  | (4.7) |

exists almost surely.

###### Remark 4.1.

Intuitively, as n↑∞n\uparrow\infty, the entropy regularization creates a *soft* lower barrier given by P+λP+\lambda and the generator Φλ,n\Phi\_{\lambda,n} pushes the value process upward whenever it falls below this level, see Figure [1](https://arxiv.org/html/2602.18078v1#S4.F1 "Figure 1 ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators").
However, unlike the *hard* lower barrier PP, the value function is still allowed to move below P+λP+\lambda. We refer to subsection [4.4](https://arxiv.org/html/2602.18078v1#S4.SS4 "4.4 Probabilistic Interpretation ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") for a probabilistic interpretation of this effect.

We now turn to the analytical construction of the limit process VλV^{\lambda}.
The approach relies on a monotone stability argument for BSDEs, in the spirit
of Peng [[37](https://arxiv.org/html/2602.18078v1#bib.bib37)], adapted to the entropy-regularized structure of the driver.
More precisely, we exploit the monotonicity of the family
(Φλ,n)n≥1(\Phi\_{\lambda,n})\_{n\geq 1} and suitable uniform estimates to pass to the limit
in the penalization scheme ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")).
  
This allows us to identify the monotone limit VλV^{\lambda} as the value component
of a reflected BSDE with a logarithmically singular generator.
Under Assumption [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmhyp1 "Assumption 4.1. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), we show in Theorem [4.2](https://arxiv.org/html/2602.18078v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") that there exist processes Mλ∈ℋ2M^{\lambda}\in\mathcal{H}^{2} and Aλ∈𝒦2A^{\lambda}\in\mathcal{K}^{2} such that
(Vλ,Mλ,Aλ)(V^{\lambda},M^{\lambda},A^{\lambda}) is the unique solution in
𝒮2×ℋ2×𝒦2\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{K}^{2} of

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Vtλ=PT−∫tT𝑑Msλ+∫tTΦλ,∞​(s,Vsλ)​𝑑s+ATλ−Atλ,\displaystyle V^{\lambda}\_{t}=P\_{T}-\int^{T}\_{t}dM^{\lambda}\_{s}+\int^{T}\_{t}\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s})\,ds+A^{\lambda}\_{T}-A^{\lambda}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Vtλ≥Pt for all ​t∈[0,T],and∫0T(Vsλ−Ps)​𝑑Asλ=0,\displaystyle V^{\lambda}\_{t}\geq P\_{t}\quad\mbox{ for all }t\in[0,T],\quad\mathrm{and}\quad\int^{T}\_{0}(V^{\lambda}\_{s}-P\_{s})dA^{\lambda}\_{s}=0, |  |

We emphasize that the generator Φλ,∞(s,.)\Phi\_{\lambda,\infty}(s,.) above is *not* globally Lipschitz on [Ps,∞)[P\_{s},\infty) due to the logarithmic singularity as x↓Psx\downarrow P\_{s}.
This makes ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) a non-standard reflected BSDE, and the existence of a solution is not immediate.
Nevertheless, the generator is monotone - in fact, one-sided Lipschitz - and uniqueness of the solution follows from similar arguments to those developed by Lepeltier *et al.* [[30](https://arxiv.org/html/2602.18078v1#bib.bib30)].
For completeness, this uniqueness result is provided in the following lemma.

###### Lemma 4.1.

If (Vλ,Mλ,Aλ)∈𝒮2×ℋ2×𝒦2(V^{\lambda},M^{\lambda},A^{\lambda})\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{K}^{2} is a solution to the reflected BSDE in ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), then it is unique.

###### Proof.

Let (Vi,Mi,Ai)(V^{i},M^{i},A^{i}) for i=1,2i=1,2 be two solutions in 𝒮2×ℋ2×𝒦2\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{K}^{2}. Set V¯:=V1−V2\bar{V}:=V^{1}-V^{2} and M¯:=M1−M2\bar{M}:=M^{1}-M^{2}. Applying Itô’s formula to V¯2\bar{V}^{2} gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Vt1−Vt2)2+∫tTd​[M¯]s\displaystyle(V^{1}\_{t}-V^{2}\_{t})^{2}+\int^{T}\_{t}d[\bar{M}]\_{s} | =−2​∫tTV¯s​𝑑M¯s+2​∫tTV¯s​[Φλ,∞​(s,Vs1)−Φλ,∞​(s,Vs2)]​𝑑s\displaystyle=-2\int^{T}\_{t}\bar{V}\_{s}d\bar{M}\_{s}+2\int^{T}\_{t}\bar{V}\_{s}[\Phi\_{\lambda,\infty}(s,V^{1}\_{s})-\Phi\_{\lambda,\infty}(s,V^{2}\_{s})]ds |  | (4.8) |
|  |  | +2​∫tT(Vt1−Vt2)​(d​As1−d​As2).\displaystyle\quad+2\int^{T}\_{t}(V^{1}\_{t}-V^{2}\_{t})(dA^{1}\_{s}-dA^{2}\_{s}). |  |

Since x↦Φλ,∞​(s,x)x\mapsto\Phi\_{\lambda,\infty}(s,x) is decreasing on (Ps,∞)(P\_{s},\infty), we get V¯s​(Φλ,∞​(s,Vs1)−Φλ,∞​(s,Vs2))≤0\bar{V}\_{s}\,\big(\Phi\_{\lambda,\infty}(s,V^{1}\_{s})-\Phi\_{\lambda,\infty}(s,V^{2}\_{s})\big)\leq 0.

Furthermore, using the Skorokhod minimal reflection conditions for A1A^{1} and A2A^{2} together with Vi≥PV^{i}\geq P, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tT(Vs1−Vs2)​𝑑As1\displaystyle\int\_{t}^{T}(V^{1}\_{s}-V^{2}\_{s})\,dA^{1}\_{s} | =∫tT(Vs1−Ps+Ps−Vs2)​𝑑As1≤0,\displaystyle=\int\_{t}^{T}(V^{1}\_{s}-P\_{s}+P\_{s}-V^{2}\_{s})\,dA^{1}\_{s}\leq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tT(Vs1−Vs2)​𝑑As2\displaystyle\int\_{t}^{T}(V^{1}\_{s}-V^{2}\_{s})\,dA^{2}\_{s} | =∫tT(Vs1−Ps+Ps−Vs2)​𝑑As2≥0.\displaystyle=\int\_{t}^{T}(V^{1}\_{s}-P\_{s}+P\_{s}-V^{2}\_{s})\,dA^{2}\_{s}\geq 0. |  |

Hence the last term in ([4.8](https://arxiv.org/html/2602.18078v1#S4.E8 "In Proof. ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) is non-positive, and we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Vt1−Vt2)2+∫tTd​[M¯]s≤−2​∫tTV¯s​𝑑M¯s.(V^{1}\_{t}-V^{2}\_{t})^{2}+\int\_{t}^{T}d[\bar{M}]\_{s}\leq-2\int\_{t}^{T}\bar{V}\_{s}\,d\bar{M}\_{s}. |  | (4.9) |

The stochastic integral on the right-hand side is a uniformly integrable martingale (by an argument identical to that used in ([4.22](https://arxiv.org/html/2602.18078v1#S4.E22 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"))).
Taking expectations gives [M¯]≡0[\bar{M}]\equiv 0 which in turn yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Vt1−Vt2|2]≤0,\displaystyle{\mathbb{E}}[\,\sup\_{0\leq t\leq T}|V^{1}\_{t}-V^{2}\_{t}|^{2}]\leq 0, |  |

and therefore V1=V2V^{1}=V^{2} almost surely. Finally, since the RBSDE dynamics are identical, this forces A1=A2A^{1}=A^{2} almost surely as well.
∎

###### Remark 4.2.

Let us point our that the RBSDE in ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) lies outside the scope of the existing frameworks developed by Zheng [[48](https://arxiv.org/html/2602.18078v1#bib.bib48)] and Zheng *et al.* [[50](https://arxiv.org/html/2602.18078v1#bib.bib50)] for singular reflected BSDEs. To illustrate this, consider the simplified setting where P=0P=0, λ=1\lambda=1 and 𝔽\mathbb{F} is the Brownian filtration. Then ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) reduces to

|  |  |  |
| --- | --- | --- |
|  | Yt=−∫tTZs​𝑑Ws+∫tTln⁡(1Ys)​𝑑s+∫tT𝑑As,Y\_{t}=-\int\_{t}^{T}Z\_{s}\,dW\_{s}+\int\_{t}^{T}\ln\!\left(\frac{1}{Y\_{s}}\right)\,ds+\int\_{t}^{T}dA\_{s}, |  |

together with the reflection conditions

|  |  |  |
| --- | --- | --- |
|  | Yt≥0,∫0TYs​𝑑As=0.Y\_{t}\geq 0,\qquad\int\_{0}^{T}Y\_{s}\,dA\_{s}=0. |  |

Unlike the settings considered in [[48](https://arxiv.org/html/2602.18078v1#bib.bib48), [50](https://arxiv.org/html/2602.18078v1#bib.bib50)], this formulation lacks a quadratic term accompanying the singular driver ln⁡(1/y)\ln(1/y) for y≥0y\geq 0. The presence of such a term is a crucial assumption in the analysis of the aforementioned works, as their existence results rely on a transformation technique where the quadratic term naturally arises via Itô’s formula and the domination method (see Bahlali [[2](https://arxiv.org/html/2602.18078v1#bib.bib2)], Bahlali *et al.* [[3](https://arxiv.org/html/2602.18078v1#bib.bib3)], and Bahlali and Tangpi [[4](https://arxiv.org/html/2602.18078v1#bib.bib4)]). Consequently, the techniques developed in those works are not directly applicable to our setting.

The remainder of the section is organized as follows. Subsection 4.1 collects a series of auxiliary lemmas and quantitative estimates
on the entropy-regularized generator and its time-integrated form. These results play the role of *a priori estimates* and constitute the main analytical input for the subsequent convergence and identification arguments. In Subsection 4.2, we exploit these estimates to derive a non-asymptotic convergence rate of VλV^{\lambda} towards the American option value VV as λ↓0\lambda\downarrow 0, where VλV^{\lambda} is solely viewed as the monotone limit of the penalized scheme. Subsection 4.3 is devoted to the characterization of VλV^{\lambda} under stronger regularity assumptions. We prove that there exist processes Mλ∈ℋ2M^{\lambda}\in\mathcal{H}^{2} and Aλ∈𝒦2A^{\lambda}\in\mathcal{K}^{2} such that (Vλ,Mλ,Aλ)(V^{\lambda},M^{\lambda},A^{\lambda}) is the unique solution to the RBSDE ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), and we establish the associated optimal stopping representation. Finally, Subsection 4.4 provides a financial interpretation of this singular RBSDE, relating the entropy-regularized value process VλV^{\lambda} to the pricing of an American option subject to default risk.

As already mentioned, our analysis relies on a monotone stability argument for BSDEs, in the spirit of Peng [[37](https://arxiv.org/html/2602.18078v1#bib.bib37)], adapted to the entropy-regularized structure of the driver. More precisely, we decompose the generator Φλ,n\Phi\_{\lambda,n} into its positive and negative parts, denoted by Φλ,n+\Phi^{+}\_{\lambda,n} and Φλ,n−\Phi^{-}\_{\lambda,n}. The positive component plays a role analogous to the penalization term in classical schemes for reflected BSDEs, while the negative component is shown to be uniformly Lipschitz, with a constant independent of nn.
To handle the logarithmic singularity at the lower barrier PP in the limit n→∞n\to\infty, we additionally introduce a suitable ε\varepsilon-truncation of the driver.

### 4.1 Auxiliary Lemmas and Estimates

This subsection gathers a collection of technical lemmas and quantitative
estimates that are instrumental for the analysis carried out in Subsections 4.2 and 4.3. These results play the role of *a priori estimates* for the entropy-regularized penalization scheme and will be used repeatedly to
control the behavior of the generator and its derivatives, uniformly with respect to the penalization parameters.

More specifically, we establish several auxiliary properties of the generator Φλ,n​(s,x)\Phi\_{\lambda,n}(s,x), together with integrability and growth estimates for its
time-integrated form. These estimates are key ingredients in the proofs of the asymptotic convergence to the American option value and in the identification of the limit process VλV^{\lambda} as the solution to a singular reflected BSDE.

For any fixed parameter λ∈(0,1]\lambda\in(0,1], the function
x↦Φλ,n​(s,x)x\mapsto\Phi\_{\lambda,n}(s,x) is decreasing and admits a unique
root located at Ps−λ​Φn−1​(0)P\_{s}-\lambda\Phi^{-1}\_{n}(0).

−2-2022446688PsP\_{s}Ps+λP\_{s}+\lambdaΦ1,n​(s,x)\Phi\_{1,n}(s,x)n=1n=1n=2n=2n=5n=5n=15n=15n=∞n=\infty


Figure 1: Sketches of Φ1,n\Phi\_{1,n} for various nn and of Φ1,∞​(s,x)=−ln⁡(x−Ps)​𝟙{x>Ps}+∞​𝟙{x≤Ps}\Phi\_{1,\infty}(s,x)=-\ln(x-P\_{s})\mathds{1}\_{\{x>P\_{s}\}}+\infty\mathds{1}\_{\{x\leq P\_{s}\}}.

###### Lemma 4.2.

For all n≥1n\geq 1, one has Φn−1​(0)∈(−1,0]\Phi\_{n}^{-1}(0)\in(-1,0] and Φn−1​(0)↓−1\Phi^{-1}\_{n}(0)\downarrow-1 as n→∞n\rightarrow\infty.

###### Proof.

The case n=1n=1 yields Φ1−1​(0)=0\Phi^{-1}\_{1}(0)=0.
For n≥2n\geq 2, the root of Φn\Phi\_{n} coincides with the non-zero solution of f​(x)=en​x−x−1f(x)=e^{nx}-x-1. Since f′​(x)=n​en​x−1f^{\prime}(x)=ne^{nx}-1 and f′′​(x)=n2​en​xf^{\prime\prime}(x)=n^{2}e^{nx}, the unique minimizer is x∗=−1n​ln⁡n∈(−1,0)x\_{\*}=-\frac{1}{n}\ln n\in(-1,0) and f​(x∗)=1n+1n​ln⁡n−1<0f(x\_{\*})=\frac{1}{n}+\frac{1}{n}\ln n-1<0. Moreover, f​(−1)=e−n>0f(-1)=e^{-n}>0, and hence the intermediate value theorem
implies the existence of a unique root Φn−1​(0)∈(−1,x∗)⊂(−1,0)\Phi\_{n}^{-1}(0)\in(-1,x\_{\*})\subset(-1,0).
Differentiating the identity en​Φn−1​(0)−Φn−1​(0)−1=0e^{n\Phi^{-1}\_{n}(0)}-\Phi^{-1}\_{n}(0)-1=0 with
respect to nn yields

|  |  |  |
| --- | --- | --- |
|  | dd​n​[Φn−1​(0)]=Φn−1​(0)​en​Φn−1​(0)1−n​en​Φn−1​(0)<0,\frac{d}{dn}[\Phi^{-1}\_{n}(0)]=\frac{\Phi^{-1}\_{n}(0)e^{n\Phi^{-1}\_{n}(0)}}{1-ne^{n\Phi^{-1}\_{n}(0)}}<0, |  |

and since |Φn−1​(0)+1|=en​Φn−1​(0)≤en​x∗=1n|\Phi^{-1}\_{n}(0)+1|=e^{n\Phi^{-1}\_{n}(0)}\leq e^{nx\_{\*}}=\frac{1}{n}, we conclude that Φn−1​(0)↓−1\Phi^{-1}\_{n}(0)\downarrow-1 as n→∞n\rightarrow\infty.
∎

As a direct consequence of Lemma [4.2](https://arxiv.org/html/2602.18078v1#S4.Thmlem2 "Lemma 4.2. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), the root of
x↦Φλ,n​(s,x)x\mapsto\Phi\_{\lambda,n}(s,x) increases to Ps+λP\_{s}+\lambda as
n→∞n\to\infty, and satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ps≤Ps−λ​Φn−1​(0)≤Ps+λ.P\_{s}\leq P\_{s}-\lambda\Phi^{-1}\_{n}(0)\leq P\_{s}+\lambda. |  | (4.10) |

###### Lemma 4.3.

Fix n≥1n\geq 1.
The derivative x↦∂xΦλ,n​(s,x)x\mapsto\partial\_{x}\Phi\_{\lambda,n}(s,x) is negative and
increasing.
Furthermore, for any x∗>0x\_{\*}>0 and all x≥Ps+x∗x\geq P\_{s}+x\_{\*},

|  |  |  |
| --- | --- | --- |
|  | ∂xΦλ,n​(s,x)≥(−λx∗)∨(−n2).\partial\_{x}\Phi\_{\lambda,n}(s,x)\;\geq\;\left(-\frac{\lambda}{x\_{\*}}\right)\vee\left(-\frac{n}{2}\right). |  |

###### Proof.

From ([4.2](https://arxiv.org/html/2602.18078v1#S4.E2 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and Lemma [6.2](https://arxiv.org/html/2602.18078v1#S6.Thmlem2 "Lemma 6.2. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂xΦλ,n​(s,x)\displaystyle\partial\_{x}\Phi\_{\lambda,n}(s,x) | =−n​Φ′​(Ps−xλ/n)<0,\displaystyle=-n\Phi^{\prime}\left(\frac{P\_{s}-x}{\lambda/n}\right)<0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂x​x2Φλ,n​(s,x)\displaystyle\partial^{2}\_{xx}\Phi\_{\lambda,n}(s,x) | =n2λ​Φ′′​(Ps−xλ/n)>0.\displaystyle=\frac{n^{2}}{\lambda}\Phi^{\prime\prime}\left(\frac{P\_{s}-x}{\lambda/n}\right)>0. |  |

Hence the minimum over [Ps+x∗,∞)[P\_{s}+x\_{\*},\infty) is attained at x=Ps+x∗x=P\_{s}+x\_{\*}.
Setting y=n​x∗/λy=nx\_{\*}/\lambda, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂xΦλ,n​(s,Ps+x∗)\displaystyle\partial\_{x}\Phi\_{\lambda,n}(s,P\_{s}+x\_{\*}) | =−n​Φ′​(−n​x∗/λ)=λx∗​y​e−y−(1−e−y)1−e−y≥−λx∗,\displaystyle=-n\Phi^{\prime}\left(-nx\_{\*}/\lambda\right)=\frac{\lambda}{x\_{\*}}\frac{{{y}e^{-y}}-(1-e^{-y})}{1-e^{-y}}\geq-\frac{\lambda}{x\_{\*}}, |  | (4.11) |

where we use the fact that for y≥0y\geq 0

|  |  |  |
| --- | --- | --- |
|  | y​e−y−(1−e−y)1−e−y=y​e−y1−e−y−1∈[−1,0).\frac{{{y}e^{-y}}-(1-e^{-y})}{1-e^{-y}}=\frac{{{y}e^{-y}}}{1-e^{-y}}-1\in[-1,0). |  |

Using positivity and monotonicity of Φ′\Phi^{\prime} gives

|  |  |  |
| --- | --- | --- |
|  | ∂xΦλ,n​(s,Ps+x∗)=−n​Φ′​(−n​x⋆/λ)≥−n​Φ′​(0)=−n2.\partial\_{x}\Phi\_{\lambda,n}(s,P\_{s}+x\_{\*})=-n\Phi^{\prime}(-nx\_{\star}/\lambda)\geq-n\Phi^{\prime}(0)=-\frac{n}{2}. |  |

∎

###### Corollary 4.1.

For all x∈[Ps−λ​Φn−1​(0),∞)x\in[P\_{s}-\lambda\Phi^{-1}\_{n}(0),\infty),

|  |  |  |
| --- | --- | --- |
|  | |∂xΦλ,n​(s,x)|≤max⁡{1,1/|Φ2−1​(0)|}.|\partial\_{x}\Phi\_{\lambda,n}(s,x)|\leq\max\{1,1/|\Phi^{-1}\_{2}(0)|\}. |  |

###### Proof.

By Lemma [4.2](https://arxiv.org/html/2602.18078v1#S4.Thmlem2 "Lemma 4.2. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), we have xn:=n​Φn−1​(0)∈(−n,0]x\_{n}:=n\Phi\_{n}^{-1}(0)\in(-n,0].
The result then follows from ([4.11](https://arxiv.org/html/2602.18078v1#S4.E11 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) since, for n=1n=1, one has ∂xΦλ,1​(s,Ps−λ​x1)=−Φ′​(0)=−12\partial\_{x}\Phi\_{\lambda,1}(s,P\_{s}-\lambda x\_{1})=-\Phi^{\prime}(0)=-\frac{1}{2} and |Φn−1​(0)|≤|Φn+1−1​(0)||\Phi^{-1}\_{n}(0)|\leq|\Phi^{-1}\_{n+1}(0)| for n≥2n\geq 2.
∎

We now provide some a priori estimates on ([4.4](https://arxiv.org/html/2602.18078v1#S4.E4 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). To proceed, we set

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ktλ,n\displaystyle K^{\lambda,n}\_{t} | :=∫0tΦλ,n​(s,Vsλ,n)​𝑑s,\displaystyle:=\int^{t}\_{0}\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s})\,ds, |  | (4.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ktλ,n,±\displaystyle K^{\lambda,n,\pm}\_{t} | :=∫0tΦλ,n±​(s,Vsλ,n)​𝑑s.\displaystyle:=\int^{t}\_{0}\Phi^{\pm}\_{\lambda,n}(s,V^{\lambda,n}\_{s})\,ds. |  | (4.13) |

###### Lemma 4.4.

Assume that Assumption [3.1](https://arxiv.org/html/2602.18078v1#S3.Thmhyp1 "Assumption 3.1. ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") holds. Let (Vλ,n,Mλ,n)∈𝒮2×ℋ2(V^{\lambda,n},M^{\lambda,n})\in\mathcal{S}^{2}\times\mathcal{H}^{2} denote the unique solution to ([4.4](https://arxiv.org/html/2602.18078v1#S4.E4 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). Then there exists a constant C<∞C<\infty such that, for any n≥1n\geq 1 and any 0≤λ≤10\leq\lambda\leq 1

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤t≤T|Vtλ,n|2]+𝔼​[[Mλ,n]T]+𝔼​[|KTλ,n,+|2]+𝔼​[|KTλ,n,−|2]≤C.\displaystyle{\mathbb{E}}[\sup\_{0\leq t\leq T}|V^{\lambda,n}\_{t}|^{2}]+{\mathbb{E}}\left[[M^{\lambda,n}]\_{T}\right]+{\mathbb{E}}\big[|K^{\lambda,n,+}\_{T}|^{2}\big]+{\mathbb{E}}\big[|K^{\lambda,n,-}\_{T}|^{2}\big]\leq C. |  |

###### Proof.

*Step 1.* We write Φλ,n=Φλ,n+−Φλ,n−\Phi\_{\lambda,n}=\Phi\_{\lambda,n}^{+}-\Phi\_{\lambda,n}^{-} and observe by ([4.10](https://arxiv.org/html/2602.18078v1#S4.E10 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {x:Φn​(λ−1​(Ps−x))≥0}={x:Ps−λ​Φn−1​(0)≥x}⊆{x:Ps+λ≥x},\left\{x:\Phi\_{n}\left(\lambda^{-1}(P\_{s}-x)\right)\geq 0\right\}=\left\{x:P\_{s}-\lambda\Phi\_{n}^{-1}(0)\geq x\right\}\subseteq\left\{x:P\_{s}+\lambda\geq x\right\}, |  | (4.14) |

and similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {x:Φn​(λ−1​(Ps−x))<0}={x:Ps−λ​Φn−1​(0)<x}⊆{x:Ps<x}.\left\{x:\Phi\_{n}\left(\lambda^{-1}(P\_{s}-x)\right)<0\right\}=\left\{x:P\_{s}-\lambda\Phi\_{n}^{-1}(0)<x\right\}\subseteq\left\{x:P\_{s}<x\right\}. |  | (4.15) |

From ([4.14](https://arxiv.org/html/2602.18078v1#S4.E14 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), the positive part of the generator given by ([4.2](https://arxiv.org/html/2602.18078v1#S4.E2 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) satisfies for all x∈ℝx\in\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​Φλ,n+​(s,x)≤(Ps+λ)​Φλ,n+​(s,x),a.s.x\Phi^{+}\_{\lambda,n}(s,x)\leq(P\_{s}+\lambda)\Phi^{+}\_{\lambda,n}(s,x),\quad a.s. |  | (4.16) |

By ([4.16](https://arxiv.org/html/2602.18078v1#S4.E16 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and Young’s inequality, we obtain for any α>0\alpha>0:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (Vtλ,n)2+∫tTd​[Mλ,n]s\displaystyle(V^{\lambda,n}\_{t})^{2}+\int^{T}\_{t}d[M^{\lambda,n}]\_{s} |  | (4.17) |
|  |  | =PT2−2​∫tTVsλ,n​𝑑Msλ,n+2​∫tTVsλ,n​Φλ,n+​(s,Vsλ,n)​𝑑s−2​∫tTVsλ,n​Φλ,n−​(s,Vsλ,n)​𝑑s.\displaystyle=P^{2}\_{T}-2\int^{T}\_{t}V^{\lambda,n}\_{s}dM^{\lambda,n}\_{s}+2\int^{T}\_{t}V^{\lambda,n}\_{s}\Phi^{+}\_{\lambda,n}(s,V^{\lambda,n}\_{s})ds-2\int^{T}\_{t}V^{\lambda,n}\_{s}\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})ds. |  |
|  |  | ≤PT2−2​∫tTVsλ,n​𝑑Msλ,n+2​∫tT(Ps+λ)​Φλ,n+​(s,Vsλ,n)​𝑑s\displaystyle\leq P^{2}\_{T}-2\int^{T}\_{t}V^{\lambda,n}\_{s}dM^{\lambda,n}\_{s}+2\int^{T}\_{t}(P\_{s}+\lambda)\Phi^{+}\_{\lambda,n}(s,V^{\lambda,n}\_{s})ds |  |
|  |  | ≤PT2−2​∫tTVsλ,n​𝑑Msλ,n+2α​supt<s≤T(Ps+λ)2+2​α​(KTλ,n,+−Ktλ,n,+)2.\displaystyle\leq P^{2}\_{T}-2\int^{T}\_{t}V^{\lambda,n}\_{s}dM^{\lambda,n}\_{s}+\frac{2}{\alpha}\sup\_{t<s\leq T}(P\_{s}+\lambda)^{2}+2\alpha\big(K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t}\big)^{2}. |  |

*Step 2.* Using ([4.13](https://arxiv.org/html/2602.18078v1#S4.E13 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), the dynamics ([4.4](https://arxiv.org/html/2602.18078v1#S4.E4 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) writes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtλ,n\displaystyle V^{\lambda,n}\_{t} | =PT−∫tT𝑑Msλ,n+(KTλ,n,+−Ktλ,n,+)−(KTλ,n,−−Ktλ,n,−).\displaystyle=P\_{T}-\int^{T}\_{t}dM^{\lambda,n}\_{s}+(K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t})-(K^{\lambda,n,-}\_{T}-K^{\lambda,n,-}\_{t}). |  | (4.18) |

By Jensen’s inequality, Itô’s isometry, and the Lipschitz property of Φλ,n−\Phi^{-}\_{\lambda,n} (with constant cc independent of nn and decreasing in λ\lambda, see Corollary [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmcor1 "Corollary 4.1. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), ([4.2](https://arxiv.org/html/2602.18078v1#S4.Thmlem2 "Lemma 4.2. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and noting that Φλ,n−​(s,Ps−λ​Φn−1​(0))=0\Phi^{-}\_{\lambda,n}(s,P\_{s}-\lambda\Phi\_{n}^{-1}(0))=0, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(KTλ,n,+−Ktλ,n,+)2]\displaystyle{\mathbb{E}}\big[\big(K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t}\big)^{2}\big] | ≤4​𝔼​[PT2+(Vtλ,n)2+[Mλ,n]T−[Mλ,n]t+(∫tTΦλ,n−​(s,Vsλ,n)​𝑑s)2]\displaystyle\leq{4}{\mathbb{E}}\Big[P\_{T}^{2}+(V^{\lambda,n}\_{t})^{2}+[M^{\lambda,n}]\_{T}-[M^{\lambda,n}]\_{t}+\Big(\int^{T}\_{t}\Phi\_{\lambda,n}^{-}(s,V^{\lambda,n}\_{s})ds\Big)^{2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4​𝔼​[PT2+(Vtλ,n)2+[Mλ,n]T−[Mλ,n]t+c​(∫tT|Vsλ,n−Ps+λ​Φλ,n−1​(0)|​𝑑s)2]\displaystyle\leq{4}{\mathbb{E}}\Big[P\_{T}^{2}+(V^{\lambda,n}\_{t})^{2}+[M^{\lambda,n}]\_{T}-[M^{\lambda,n}]\_{t}+c\Big(\int^{T}\_{t}|V^{\lambda,n}\_{s}-P\_{s}+\lambda\Phi^{-1}\_{\lambda,n}(0)|ds\Big)^{2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4​(3​c​T∨1)​𝔼​[PT2+|Vtλ,n|2+[Mλ,n]T−[Mλ,n]t+∫tT((Vsλ,n)2+Ps2+λ2)​𝑑s].\displaystyle\leq{4(3cT\vee 1)}{\mathbb{E}}\Big[P\_{T}^{2}+|V^{\lambda,n}\_{t}|^{2}+[M^{\lambda,n}]\_{T}-[M^{\lambda,n}]\_{t}+\int^{T}\_{t}((V^{\lambda,n}\_{s})^{2}+P\_{s}^{2}+\lambda^{2})ds\Big]. |  |

Then by plugging the above estimates into ([4.17](https://arxiv.org/html/2602.18078v1#S4.E17 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and picking 2​α=1/(3​(4​(3​c​T∨1)))2\alpha=1/(3({4(3cT\vee 1)})) we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 23​𝔼​[(Vtλ,n)2]+23​𝔼​[[Mλ,n]T−[Mλ,n]t]≤C​(λ)​(1+∫tT𝔼​[(Vsλ,n)2]​𝑑s),\displaystyle\frac{2}{3}{\mathbb{E}}[(V^{\lambda,n}\_{t})^{2}]+\frac{2}{3}{\mathbb{E}}\big[[M^{\lambda,n}]\_{T}-[M^{\lambda,n}]\_{t}\big]\leq C(\lambda)\Big(1+\int^{T}\_{t}{\mathbb{E}}[(V^{\lambda,n}\_{s})^{2}]ds\Big), |  | (4.19) |

where the positive constant C​(λ)C(\lambda) depends on λ\lambda in an increasing way. Hence, by applying Grönwall’s inequality to ([4.19](https://arxiv.org/html/2602.18078v1#S4.E19 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we obtain sup0≤t≤T𝔼​[|Vtλ,n|2]≤C​(λ)​eT​C​(λ)≤C​(1)​eT​C​(1)\sup\_{0\leq t\leq T}{\mathbb{E}}[|V^{\lambda,n}\_{t}|^{2}]\leq C(\lambda)e^{TC(\lambda)}\leq C(1)e^{TC(1)} which in turn yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup0≤t≤T𝔼​[(Vtλ,n)2]+𝔼​[[Mλ,n]T]+𝔼​[(KTλ,n,+)2]≤C.\displaystyle\sup\_{0\leq t\leq T}{\mathbb{E}}[(V^{\lambda,n}\_{t})^{2}]+{\mathbb{E}}\left[[M^{\lambda,n}]\_{T}\right]+{\mathbb{E}}\big[\big(K^{\lambda,n,+}\_{T}\big)^{2}\big]\leq C. |  | (4.20) |

*Step 3.* By ([4.17](https://arxiv.org/html/2602.18078v1#S4.E17 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we obtain

|  |  |  |
| --- | --- | --- |
|  | sup0≤t≤T(Vtλ,n)2+∫0Td​[Mλ,n]s\displaystyle\sup\_{0\leq t\leq T}(V^{\lambda,n}\_{t})^{2}+\int^{T}\_{0}d[M^{\lambda,n}]\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤PT2+2​sup0<t≤T|∫tTVsλ,n​𝑑Msλ,n|+2α​sup0≤t≤T(Pt+λ)2+2​α​(∫0TΦλ,n+​(s,Vsλ,n)​𝑑s)2.\displaystyle\leq P^{2}\_{T}+2\sup\_{0<t\leq T}\Big|\int^{T}\_{t}V^{\lambda,n}\_{s}dM^{\lambda,n}\_{s}\Big|+\frac{2}{\alpha}\sup\_{0\leq t\leq T}(P\_{t}+\lambda)^{2}+2\alpha\Big(\int^{T}\_{0}\Phi^{+}\_{\lambda,n}(s,V^{\lambda,n}\_{s})ds\Big)^{2}. |  | (4.21) |

By the Burkholder-Davis-Gundy and the Young inequalities, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​𝔼​[sup0≤t≤T|∫tTVsλ,n​𝑑Msλ,n|]\displaystyle 2{\mathbb{E}}\Big[\,\sup\_{0\leq t\leq T}\Big|\int^{T}\_{t}V^{\lambda,n}\_{s}dM^{\lambda,n}\_{s}\Big|\Big] | ≤2​c1​𝔼​[(∫0T|Vsλ,n|2​d​[Mλ,n]s)12]\displaystyle\leq 2c\_{1}{\mathbb{E}}\Big[\Big(\int^{T}\_{0}|V^{\lambda,n}\_{s}|^{2}d[M^{\lambda,n}]\_{s}\Big)^{\frac{1}{2}}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤12​𝔼​[sup0≤t≤T(Vtλ,n)2]+2​c12​𝔼​[[Mλ,n]T].\displaystyle\leq\frac{1}{2}{\mathbb{E}}[\,\sup\_{0\leq t\leq T}(V^{\lambda,n}\_{t})^{2}]+2c\_{1}^{2}{\mathbb{E}}[[M^{\lambda,n}]\_{T}]. |  | (4.22) |

By substituting the inequality ([4.22](https://arxiv.org/html/2602.18078v1#S4.E22 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and ([4.20](https://arxiv.org/html/2602.18078v1#S4.E20 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) into ([4.21](https://arxiv.org/html/2602.18078v1#S4.E21 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and again by picking 2​α=1/(3​(4​(3​c​T∨1)))2\alpha=1/(3({4(3cT\vee 1)})), we obtain 𝔼​[sup0≤t≤T(Vtλ,n)2]≤C{\mathbb{E}}[\sup\_{0\leq t\leq T}(V^{\lambda,n}\_{t})^{2}]\leq C.

Lastly, since the map x↦Φλ,n−​(s,x)x\mapsto\Phi^{-}\_{\lambda,n}(s,x) is Lipschitz continuous with a Lipschitz constant independent of the penalty parameter nn (see Corollary [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmcor1 "Corollary 4.1. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we deduce that there exists a positive constant CC, independent of nn, such that 𝔼​[(KTλ,n,−)2]≤C​(λ){\mathbb{E}}\big[(K^{\lambda,n,-}\_{T})^{2}\big]\leq C(\lambda).
∎

###### Corollary 4.2.

For any λ∈[0,1]\lambda\in[0,1], Vλ∈𝒮2V^{\lambda}\in\mathcal{S}^{2}.

###### Proof.

The result follows from Lemma [4.4](https://arxiv.org/html/2602.18078v1#S4.Thmlem4 "Lemma 4.4. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), ([4.7](https://arxiv.org/html/2602.18078v1#S4.E7 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and Fatou’s lemma.
∎

In addition to the terms in ([4.12](https://arxiv.org/html/2602.18078v1#S4.E12 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and ([4.13](https://arxiv.org/html/2602.18078v1#S4.E13 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), for a fixed ϵ∈(0,−λ​Φ2−1​(0))\epsilon\in(0,-\lambda\Phi^{-1}\_{2}(0)), we introduce an ϵ\epsilon-truncation of the driver. By performing this truncation step, we control the derivative of the driver Φλ,n\Phi\_{\lambda,n} using ϵ\epsilon and prevent it from exploding as n→∞n\rightarrow\infty. This strategy enables us to first pass the limit as n→∞n\rightarrow\infty first and then to use monotone arguments to pass the limit as ϵ→0\epsilon\rightarrow 0. Specifically, we consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ktλ,n,ϵ:=∫0tΦλ,n​(s,Vsλ,n∨(Ps+ϵ))​𝑑s,\displaystyle K^{\lambda,n,\epsilon}\_{t}:=\int^{t}\_{0}\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))\,ds, |  | (4.23) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ktλ,n,ϵ,±:=∫0tΦλ,n±​(s,Vsλ,n∨(Ps+ϵ))​𝑑s,\displaystyle K^{\lambda,n,\epsilon,\pm}\_{t}:=\int^{t}\_{0}\Phi^{\pm}\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))\,ds, |  | (4.24) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Atλ,n,ϵ:=∫0t[Φλ,n​(s,Vsλ,n)−Φλ,n​(s,Vsλ,n∨(Ps+ϵ))]​𝑑s.\displaystyle A^{\lambda,n,\epsilon}\_{t}:=\int^{t}\_{0}[\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))]\,ds. |  | (4.25) |

We also define the two limiting processes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ktλ,ϵ:=limn→∞Ktλ,n,ϵ=∫0tΦλ,∞​(s,Vsλ∨(Ps+ϵ))​𝑑s,\displaystyle K^{\lambda,\epsilon}\_{t}:=\lim\_{n\rightarrow\infty}K^{\lambda,n,\epsilon}\_{t}=\int^{t}\_{0}\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))\,ds, |  | (4.26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ktλ:=limϵ↓0Ktλ,ϵ=∫0tλ​Φλ,∞​(s,Vsλ∨Ps)​𝑑s.\displaystyle K^{\lambda}\_{t}:=\lim\_{\epsilon\downarrow 0}K^{\lambda,\epsilon}\_{t}=\int^{t}\_{0}\lambda\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s}\vee P\_{s})\,ds. |  | (4.27) |

−2-2022446688PsP\_{s}Ps+λP\_{s}+\lambdaΦλ,n​(s,x∨(Ps+ϵ))\Phi\_{\lambda,n}(s,x\vee(P\_{s}+\epsilon))ϵ=0.5\epsilon=0.5ϵ=0.2\epsilon=0.2ϵ=0.01\epsilon=0.01


Figure 2: An illustrative sketch of the truncated generator Φλ,n​(s,x∨(Ps+ϵ))\Phi\_{\lambda,n}(s,x\vee(P\_{s}+\epsilon)) for several values of ϵ\epsilon. The functions are Lipschitz continuous and increase as ϵ→0\epsilon\rightarrow 0.

To justify the limit in ([4.26](https://arxiv.org/html/2602.18078v1#S4.E26 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), recall from Corollary [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmcor1 "Corollary 4.1. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") that the driver x↦Φλ,n​(s,x∨(Ps+ϵ))x\mapsto\Phi\_{\lambda,n}(s,x\vee(P\_{s}+\epsilon)) is Lipschitz continuous with Lipschitz constant λ/ϵ\lambda/\epsilon. This yields the bound on the integrand in ([4.23](https://arxiv.org/html/2602.18078v1#S4.E23 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"))

|  |  |  |
| --- | --- | --- |
|  | |Φλ,n​(s,Vsλ,n∨(Ps+ϵ))|≤λϵ​|Vsλ,n−Ps+λ​Φn−1​(0)|≤λϵ​(|Vsλ|+|Ps|+λ)|\Phi\_{\lambda,n}(s,V\_{s}^{\lambda,n}\vee(P\_{s}+\epsilon))|\leq\frac{\lambda}{\epsilon}|V^{\lambda,n}\_{s}-P\_{s}+\lambda\Phi^{-1}\_{n}(0)|\leq\frac{\lambda}{\epsilon}\left({|V^{\lambda}\_{s}|}+|P\_{s}|+\lambda\right) |  |

which is integrable since VλV^{\lambda} and PP are elements of 𝒮2\mathcal{S}^{2}. Moreover, by Lemma [4.3](https://arxiv.org/html/2602.18078v1#S4.Thmlem3 "Lemma 4.3. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") we have

|  |  |  |
| --- | --- | --- |
|  | |Φλ,n​(s,Vsλ,n∨(Ps+ϵ))−Φλ,∞​(s,Vsλ∨(Ps+ϵ))|\displaystyle\big|\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))-\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤|Φλ,n​(s,Vsλ,n∨(Ps+ϵ))−Φλ,n​(s,Vsλ∨(Ps+ϵ))|+|Φλ,n​(s,Vsλ∨(Ps+ϵ))−Φλ,∞​(s,Vsλ∨(Ps+ϵ))|\displaystyle\leq\big|\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))-\Phi\_{\lambda,n}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))|+|\Phi\_{\lambda,n}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))-\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤1ϵ​|Vsλ,n−Vsλ|+|Φλ,n​(s,Vsλ∨(Ps+ϵ))−Φλ,∞​(s,Vsλ∨(Ps+ϵ))|.\displaystyle\leq\frac{1}{\epsilon}|V^{\lambda,n}\_{s}-V^{\lambda}\_{s}|+\big|\Phi\_{\lambda,n}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))-\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))\big|. |  | (4.28) |

By ([4.2](https://arxiv.org/html/2602.18078v1#S4.E2 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), ([4.5](https://arxiv.org/html/2602.18078v1#S4.E5 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and ([4.6](https://arxiv.org/html/2602.18078v1#S4.E6 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), the two terms above on the right-hand side converge monotonically to zero as n→∞n\rightarrow\infty. The limit in ([4.27](https://arxiv.org/html/2602.18078v1#S4.E27 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) stems from the fact that ϵ↦Φλ,∞​(s,x∨(Ps+ϵ))\epsilon\mapsto\Phi\_{\lambda,\infty}(s,x\vee(P\_{s}+\epsilon)) is monotonically decreasing combined with the monotone convergence theorem.

We now give some uniform estimates in the 𝒮2\mathcal{S}^{2} norm for the processes Kλ,n,ϵK^{\lambda,n,\epsilon}, Kλ,n,ϵ,±K^{\lambda,n,\epsilon,\pm}, Aλ,n,ϵA^{\lambda,n,\epsilon}, Kλ,ϵK^{\lambda,\epsilon} and KλK^{\lambda}.

###### Lemma 4.5.

There exists a constant C<∞C<\infty such that for any 0<λ≤10<\lambda\leq 1, any n≥2n\geq 2 and any ϵ∈(0,−λ​Φ2−1​(0))\epsilon\in(0,-\lambda\Phi^{-1}\_{2}(0)),

|  |  |  |
| --- | --- | --- |
|  | ‖Aλ,n,ϵ‖𝒮2+‖Kλ,n,ϵ,+‖𝒮2≤C.\displaystyle\|A^{\lambda,n,\epsilon}\|\_{\mathcal{S}^{2}}+\|K^{\lambda,n,\epsilon,+}\|\_{\mathcal{S}^{2}}\leq C. |  |

###### Proof.

We first note that Aλ,n,ϵ+Kλ,n,ϵ,+=Kλ,n,+A^{\lambda,n,\epsilon}+K^{\lambda,n,\epsilon,+}=K^{\lambda,n,+}. Indeed, from ([4.14](https://arxiv.org/html/2602.18078v1#S4.E14 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and ([4.15](https://arxiv.org/html/2602.18078v1#S4.E15 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) the support of Φλ,n+​(s,⋅)\Phi\_{\lambda,n}^{+}(s,\cdot) is

|  |  |  |
| --- | --- | --- |
|  | {x:Φn​(λ−1​(Ps−x))≥0}={x:Ps−λ​Φn−1​(0)≥x},\left\{x:\Phi\_{n}\left(\lambda^{-1}(P\_{s}-x)\right)\geq 0\right\}=\left\{x:P\_{s}-\lambda\Phi\_{n}^{-1}(0)\geq x\right\}, |  |

and the support of Φλ,n−​(s,⋅)\Phi\_{\lambda,n}^{-}(s,\cdot) is

|  |  |  |
| --- | --- | --- |
|  | {x:Φn​(λ−1​(Ps−x))<0}={x:Ps−λ​Φn−1​(0)<x}.\left\{x:\Phi\_{n}\left(\lambda^{-1}(P\_{s}-x)\right)<0\right\}=\left\{x:P\_{s}-\lambda\Phi\_{n}^{-1}(0)<x\right\}. |  |

But since ϵ<−λ​Φ2−1​(0)≤−λ​Φn−1​(0)\epsilon<-\lambda\Phi\_{2}^{-1}(0)\leq-\lambda\Phi\_{n}^{-1}(0), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Atλ,n,ϵ+Ktλ,n,ϵ,+\displaystyle A^{\lambda,n,\epsilon}\_{t}+K^{\lambda,n,\epsilon,+}\_{t} | =∫0t[Φλ,n​(s,Vsλ,n)−Φλ,n​(s,Vsλ,n∨(Ps+ϵ))]​𝟙{Vsλ,n≤Ps−Φn−1​(0)}​𝑑s\displaystyle=\int^{t}\_{0}\left[\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))\right]\mathds{1}\_{\{V\_{s}^{\lambda,n}\leq P\_{s}-\Phi\_{n}^{-1}(0)\}}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t[Φλ,n​(s,Vsλ,n)−Φλ,n​(s,Vsλ,n∨(Ps+ϵ))]​𝟙{Vsλ,n>Ps−Φn−1​(0)}​𝑑s\displaystyle\hskip 10.00002pt+\int^{t}\_{0}\left[\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))\right]\mathds{1}\_{\{V\_{s}^{\lambda,n}>P\_{s}-\Phi\_{n}^{-1}(0)\}}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tΦλ,n+​(s,Vsλ,n∨(Ps+ϵ))​𝑑s\displaystyle\hskip 10.00002pt+\int\_{0}^{t}\Phi^{+}\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Ktλ,n,+.\displaystyle=K^{\lambda,n,+}\_{t}. |  |

On the other hand, we have Aλ,n,ϵA^{\lambda,n,\epsilon}, Kλ,n,ϵ,+≥0K^{\lambda,n,\epsilon,+}\geq 0, and the result follows from Lemma [4.4](https://arxiv.org/html/2602.18078v1#S4.Thmlem4 "Lemma 4.4. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators").
∎

###### Lemma 4.6.

There exists a constant C<∞C<\infty such that, for any 0<λ≤10<\lambda\leq 1 and any ϵ∈(0,−λ​Φ2−1​(0))\epsilon\in(0,-\lambda\Phi^{-1}\_{2}(0))

|  |  |  |
| --- | --- | --- |
|  | ‖Kλ‖𝒮2+‖Kλ,ϵ‖𝒮2≤C.\|K^{\lambda}\|\_{\mathcal{S}^{2}}+\|K^{\lambda,\epsilon}\|\_{\mathcal{S}^{2}}\leq C. |  |

###### Proof.

Fix ϵ<−λ​Φ2−1​(0)\epsilon<-\lambda\Phi^{-1}\_{2}(0) and n≥2n\geq 2. We first note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ktλ,n,ϵ,±\displaystyle K^{\lambda,n,\epsilon,\pm}\_{t} | =∫0tΦλ,n±​(s,Vsλ,n∨(Ps+ϵ))​𝑑s\displaystyle=\int^{t}\_{0}\Phi^{\pm}\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫0tΦλ,n±​(s,Vsλ,n)​𝑑s=Ktλ,n,±.\displaystyle\leq\int^{t}\_{0}\Phi^{\pm}\_{\lambda,n}(s,V^{\lambda,n}\_{s})ds=K^{\lambda,n,\pm}\_{t}. |  |

Hence, by Lemma [4.4](https://arxiv.org/html/2602.18078v1#S4.Thmlem4 "Lemma 4.4. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and Fatou’s lemma,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|KTλ,ϵ,±|2]≤lim infn→∞𝔼​[|KTλ,n,ϵ,±|2]≤lim infn→∞𝔼​[|KTλ,n,+|2]≤C.{\mathbb{E}}[|K\_{T}^{\lambda,\epsilon,\pm}|^{2}]\leq\liminf\_{n\rightarrow\infty}{\mathbb{E}}[|K\_{T}^{\lambda,n,\epsilon,\pm}|^{2}]\leq\liminf\_{n\rightarrow\infty}{\mathbb{E}}[|K^{\lambda,n,+}\_{T}|^{2}]\leq C. |  |

Moreover, sup0≤t≤T|Ktλ,ϵ|2≤2​|KTλ,ϵ,+|2+2​|KTλ,ϵ,−|2\sup\_{0\leq t\leq T}|K^{\lambda,\epsilon}\_{t}|^{2}\leq 2|K^{\lambda,\epsilon,+}\_{T}|^{2}+2|K^{\lambda,\epsilon,-}\_{T}|^{2} and it follows that Kλ,ϵ∈𝒮2K^{\lambda,\epsilon}\in\mathcal{S}^{2} with ‖Kλ,ϵ‖𝒮2\|K^{\lambda,\epsilon}\|\_{\mathcal{S}^{2}} bounded above by a constant CC that is independent of ϵ\epsilon and λ\lambda.

To obtain an upper bound for ‖Kλ‖𝒮2\|K^{\lambda}\|\_{\mathcal{S}^{2}}, observe that

|  |  |  |
| --- | --- | --- |
|  | |Ktλ|2=lim infϵ↓0|Ktλ,ϵ|2≤lim infϵ↓0sup0≤t≤T|Ktλ,ϵ|2.|K^{\lambda}\_{t}|^{2}=\liminf\_{\epsilon\downarrow 0}|K^{\lambda,\epsilon}\_{t}|^{2}\leq\liminf\_{\epsilon\downarrow 0}\sup\_{0\leq t\leq T}|K^{\lambda,\epsilon}\_{t}|^{2}. |  |

Therefore, by Fatou’s lemma and the bound above, ‖Kλ‖𝒮2≤lim infϵ↓0‖Kλ,ϵ‖𝒮2≤C\|K^{\lambda}\|\_{\mathcal{S}^{2}}\leq\liminf\_{\epsilon\downarrow 0}\|K^{\lambda,\epsilon}\|\_{\mathcal{S}^{2}}\leq C.
∎

### 4.2 Asymptotic Convergence to the American Option

In this subsection, we establish a convergence rate for VλV^{\lambda} towards the American option value VV as λ↓0\lambda\downarrow 0. Importantly, we point out that here VλV^{\lambda} is only considered as the monotone limit of Vλ,nV^{\lambda,n}, whose existence follows from the standard monotone convergence arguments presented at the beginning of this section, without any reference to a backward equation. The BSDE characterization of VλV^{\lambda} is deferred to Subsection 4.3, where,
under stronger assumptions, we show that VλV^{\lambda} arises as the value component of a reflected BSDE with a singular driver and admits an optimal stopping representation.
Recall that, since the payoff process PP is càdlàg and belongs to 𝒮2\mathcal{S}^{2}, the Doob-Meyer decomposition applied to the supermartingale VV guarantees the existence of a martingale MM and a continuous, non-decreasing process AA such that V=M−AV=M-A. Moreover, the process AA satisfies the Skorokhod reflection condition ∫0T(Ps−Vs)​𝑑As=0\int^{T}\_{0}(P\_{s}-V\_{s})dA\_{s}=0 which characterises the minimality of the reflection and ensures that VV coincides with the value of the American option.

We begin by establishing a technical estimate for the difference between Vλ,nV^{\lambda,n} and VV.

###### Lemma 4.7.

For any 0≤λ≤10\leq\lambda\leq 1 and any n≥1n\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | et​(Vtλ,n−Vt)2\displaystyle e^{t}(V^{\lambda,n}\_{t}-V\_{t})^{2} | ≤2​λ​eT​𝔼​[KTλ,n,+−Ktλ,n,+|ℱt]\displaystyle\leq 2\lambda e^{T}\mathbb{E}[K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t}|{\mathcal{F}}\_{t}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​eT​𝔼​[∫tT(Vsλ,n−Ps)−​𝑑As|ℱt]+eT​𝔼​[∫tT[Φλ,n−​(s,Vs)]2​𝑑s|ℱt].\displaystyle+2e^{T}\mathbb{E}\Big[\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s})^{-}dA\_{s}|{\mathcal{F}}\_{t}\Big]+e^{T}\mathbb{E}\Big[\int^{T}\_{t}[\Phi^{-}\_{\lambda,n}(s,V\_{s})]^{2}ds|{\mathcal{F}}\_{t}\Big]. |  | (4.29) |

###### Proof.

Applying Itô’s formula and using the reflected BSDE representation of VV in ([2.1](https://arxiv.org/html/2602.18078v1#S2.E1 "In 2 Notations and Setup ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we obtain

|  |  |  |
| --- | --- | --- |
|  | eβ​t​(Vtλ,n−Vt)2+∫tTeβ​s​d​[M¯λ,n]s\displaystyle e^{\beta t}(V^{\lambda,n}\_{t}-V\_{t})^{2}+\int^{T}\_{t}e^{\beta s}d[\bar{M}^{\lambda,n}]\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | =−2​∫tTeβ​s​(Vsλ,n−Vs)​𝑑M¯sλ,n+2​∫tTeβ​s​(Vsλ,n−Vs)​d​(Ksλ,n,+−As)\displaystyle=-2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})d\bar{M}^{\lambda,n}\_{s}+2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})d(K^{\lambda,n,+}\_{s}-A\_{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | −2​∫tTeβ​s​(Vsλ,n−Vs)​Φλ,n−​(s,Vsλ,n)​𝑑s−β​∫tTeβ​s​(Vsλ,n−Vs)2​𝑑s,\displaystyle\quad-2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})ds-\beta\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})^{2}ds, |  |

where M¯λ,n=Mλ,n−M\bar{M}^{\lambda,n}=M^{\lambda,n}-M. We first estimate the reflection term. Observe that

|  |  |  |
| --- | --- | --- |
|  | ∫tTeβ​s​(Vsλ,n−Vs)​d​(Ksλ,n,+−As)\displaystyle\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})d(K^{\lambda,n,+}\_{s}-A\_{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tTeβ​s​(Vsλ,n−Ps−λ)​𝑑Ksλ,n,++∫tTeβ​s​(Ps+λ−Vs)​𝑑Ksλ,n,+\displaystyle=\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-P\_{s}-\lambda)dK^{\lambda,n,+}\_{s}+\int^{T}\_{t}e^{\beta s}(P\_{s}+\lambda-V\_{s})dK^{\lambda,n,+}\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | −∫tTeβ​s​(Vsλ,n−Ps)​𝑑As+∫tTeβ​s​(Vs−Ps)​𝑑As\displaystyle\quad-\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-P\_{s})dA\_{s}+\int^{T}\_{t}e^{\beta s}(V\_{s}-P\_{s})dA\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤λ​eβ​T​(KTλ,n,+−Ktλ,n,+)+eβ​T​∫tT(Vsλ,n−Ps)−​𝑑As,\displaystyle\leq\lambda e^{\beta T}(K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t})+e^{\beta T}\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s})^{-}dA\_{s}, |  |

where the inequality follows from the facts that ∫0t(Vs−Ps)​𝑑As=0\int^{t}\_{0}(V\_{s}-P\_{s})dA\_{s}=0, V≥PV\geq P and that the non-decreasing process Kλ,nK^{\lambda,n} increases only when Vλ,n−P−λ≤0V^{\lambda,n}-P-\lambda\leq 0.

Next, we estimate the generator. We write

|  |  |  |
| --- | --- | --- |
|  | ∫tTeβ​s​(Vsλ,n−Vs)​[−Φλ,n−​(s,Vsλ,n)]​𝑑s\displaystyle\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})[-\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})]ds |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tTeβ​s​(Vsλ,n−Vs)​[−Φλ,n−​(s,Vsλ,n)+Φλ,n−​(s,Vs)]​𝑑s+∫tTeβ​s​(Vsλ,n−Vs)​[−Φλ,n−​(s,Vs)]​𝑑s\displaystyle=\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})[-\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})+\Phi^{-}\_{\lambda,n}(s,V\_{s})]ds+\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})[-\Phi^{-}\_{\lambda,n}(s,V\_{s})]ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫tTeβ​s​(Vsλ,n−Vs)+​[−Φλ,n−​(s,Vs)]​𝑑s,\displaystyle\leq\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})^{+}[-\Phi^{-}\_{\lambda,n}(s,V\_{s})]ds, |  |

where the inequality uses the fact that x↦−Φλ,n−​(s,x)=Φλ,n​(s,x)​𝟙[Ps−λ​Φn−1​(0),∞)​(x)x\mapsto-\Phi\_{\lambda,n}^{-}(s,x)=\Phi\_{\lambda,n}(s,x)\mathds{1}\_{[P\_{s}-\lambda\Phi\_{n}^{-1}(0),\infty)}(x) is a decreasing function.
Combining the above estimates and applying Young’s inequality yields

|  |  |  |
| --- | --- | --- |
|  | eβ​t​(Vtλ,n−Vt)2≤2​λ​eβ​T​𝔼​[KTλ,n,+−Ktλ,n,+|ℱt]−𝔼​[β​∫tTeβ​s​(Vsλ,n−Vs)2​𝑑s|ℱt]\displaystyle e^{\beta t}(V\_{t}^{\lambda,n}-V\_{t})^{2}\leq 2\lambda e^{\beta T}\mathbb{E}[K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t}|{\mathcal{F}}\_{t}]-{\mathbb{E}}\Big[\beta\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})^{2}ds|{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | +2​eβ​T​𝔼​[∫tT(Vsλ,n−Ps)−​𝑑As|ℱt]+2​𝔼​[∫tTeβ​s​(Vsλ,n−Vs)+​[−Φλ,n−​(s,Vs)]​𝑑s|ℱt]\displaystyle\quad+2e^{\beta T}\mathbb{E}\Big[\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s})^{-}dA\_{s}|{\mathcal{F}}\_{t}\Big]+2\mathbb{E}\Big[\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})^{+}[-\Phi^{-}\_{\lambda,n}(s,V\_{s})]ds|{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2​λ​eβ​T​𝔼​[KTλ,n,+−Ktλ,n,+|ℱt]−𝔼​[β​∫tTeβ​s​(Vsλ,n−Vs)2​𝑑s|ℱt]\displaystyle\leq 2\lambda e^{\beta T}\mathbb{E}[K^{\lambda,n,+}\_{T}-K^{\lambda,n,+}\_{t}|{\mathcal{F}}\_{t}]-{\mathbb{E}}\Big[\beta\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s})^{2}ds|{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | +2​eβ​T​𝔼​[∫tT(Vsλ,n−Ps)−​𝑑As|ℱt]+2​𝔼​[∫tTeβ​s​12​(Vsλ,n−Vs)2+eβ​s​12​[−Φλ,n−​(s,Vs)]2​d​s|ℱt].\displaystyle\quad+2e^{\beta T}\mathbb{E}\Big[\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s})^{-}dA\_{s}|{\mathcal{F}}\_{t}\Big]+2\mathbb{E}\Big[\int^{T}\_{t}e^{\beta s}\frac{1}{2}(V^{\lambda,n}\_{s}-V\_{s})^{2}+e^{\beta s}\frac{1}{2}[-\Phi^{-}\_{\lambda,n}(s,V\_{s})]^{2}ds|{\mathcal{F}}\_{t}\Big]. |  |

Choosing β=1\beta=1 yields the desired estimate ([4.29](https://arxiv.org/html/2602.18078v1#S4.E29 "In Lemma 4.7. ‣ 4.2 Asymptotic Convergence to the American Option ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")).
∎

We now state our main result which provides a quantitative control of the approximation error Vλ−VV^{\lambda}-V.

###### Theorem 4.1.

There exists a constant C<∞C<\infty such that for any 0≤t≤T0\leq t\leq T and any 0<λ≤10<\lambda\leq 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Vtλ−Vt)2\displaystyle(V^{\lambda}\_{t}-V\_{t})^{2} | ≤C​(λ​lim infn→∞𝔼​[KTλ,n,+|ℱt]+[λ​ln⁡(λ)]2+λ2​𝔼​[supt<s≤TVs2|ℱt]).\displaystyle\leq C\Big(\lambda\liminf\_{n\rightarrow\infty}\mathbb{E}[K^{\lambda,n,+}\_{T}\big|\,{\mathcal{F}}\_{t}]+[\lambda\ln(\lambda)]^{2}+\lambda^{2}\mathbb{E}\big[\sup\_{t<s\leq T}V\_{s}^{2}\,\big|\,{\mathcal{F}}\_{t}\big]\Big). |  |

If the payoff process PP is bounded, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | (V0λ−V0)2\displaystyle(V^{\lambda}\_{0}-V\_{0})^{2} | ≤C​(λ+[λ​ln⁡(λ)]2+λ2).\displaystyle\leq C\Big(\lambda+[\lambda\ln(\lambda)]^{2}+\lambda^{2}\Big). |  |

###### Proof.

Taking the lower limit in the estimate of Lemma [4.7](https://arxiv.org/html/2602.18078v1#S4.Thmlem7 "Lemma 4.7. ‣ 4.2 Asymptotic Convergence to the American Option ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | et​(Vtλ−Vt)2\displaystyle e^{t}(V\_{t}^{\lambda}-V\_{t})^{2} | ≤2​λ​eT​lim infn→∞𝔼​[KTλ,n,+|ℱt]+2​eT​lim infn→∞𝔼​[∫tT(Vsλ,n−Ps)−​𝑑Ks|ℱt]\displaystyle\leq 2\lambda e^{T}\liminf\_{n\rightarrow\infty}\mathbb{E}[K^{\lambda,n,+}\_{T}|{\mathcal{F}}\_{t}]+2e^{T}\liminf\_{n\rightarrow\infty}\mathbb{E}[\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s})^{-}dK\_{s}|{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +lim infn→∞𝔼​[∫tTes​[Φλ,n−​(s,Vs)]2​𝑑s|ℱt].\displaystyle\hskip 10.00002pt+\liminf\_{n\rightarrow\infty}\mathbb{E}[\int^{T}\_{t}e^{s}[\Phi^{-}\_{\lambda,n}(s,V\_{s})]^{2}ds|{\mathcal{F}}\_{t}]. |  |

By Lemma [4.8](https://arxiv.org/html/2602.18078v1#S4.Thmlem8 "Lemma 4.8. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and dominated convergence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | et​(Vtλ−Vt)2\displaystyle e^{t}(V\_{t}^{\lambda}-V\_{t})^{2} | ≤2​λ​eT​lim infn→∞𝔼​[KTλ,n,+|ℱt]+𝔼​[∫tTes​[λ​ln⁡(λ−1​(Vs−Ps))]2​𝟙{Vs≥Ps+λ}​𝑑s|ℱt].\displaystyle\leq 2\lambda e^{T}\liminf\_{n\rightarrow\infty}\mathbb{E}[K^{\lambda,n,+}\_{T}|{\mathcal{F}}\_{t}]+\mathbb{E}[\int^{T}\_{t}e^{s}\left[\lambda\ln\left(\lambda^{-1}(V\_{s}-P\_{s})\right)\right]^{2}\mathds{1}\_{\{V\_{s}\geq P\_{s}+\lambda\}}ds|{\mathcal{F}}\_{t}]. |  |

To proceed, we note that for Vs−Ps≥λV\_{s}-P\_{s}\geq\lambda

|  |  |  |
| --- | --- | --- |
|  | λ​ln⁡(Vs−Psλ)≤λ​ln⁡(Vs)−λ​ln⁡(λ)≤λ​Vs−2​λ​ln⁡(λ),\displaystyle\lambda\ln\left(\frac{V\_{s}-P\_{s}}{\lambda}\right)\leq\lambda\ln(V\_{s})-\lambda\ln(\lambda)\leq\lambda V\_{s}-2\lambda\ln(\lambda), |  |

where the last step uses |ln⁡(x)|≤max⁡{−ln⁡(λ),x}|\ln(x)|\leq\max\{-\ln(\lambda),x\} for x≥λx\geq\lambda. This gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | et​(Vtλ−Vt)2\displaystyle e^{t}(V^{\lambda}\_{t}-V\_{t})^{2} | ≤2​λ​eT​lim infn→∞𝔼​[KTλ,n,+|ℱt]+4​(eT−et)​(λ​ln⁡(λ))2+2​λ2​(eT−et)​𝔼​[supt<s≤TVs2|ℱt]\displaystyle\leq 2\lambda e^{T}\liminf\_{n\rightarrow\infty}\mathbb{E}[K^{\lambda,n,+}\_{T}|{\mathcal{F}}\_{t}]+4(e^{T}-e^{t})(\lambda\ln(\lambda))^{2}+2\lambda^{2}(e^{T}-e^{t})\mathbb{E}\big[\sup\_{t<s\leq T}V\_{s}^{2}\,\big|\,{\mathcal{F}}\_{t}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(λ​lim infn→∞𝔼​[KTλ,n,+|ℱt]+(λ​ln⁡(λ))2+λ2​𝔼​[supt<s≤TVs2|ℱt]).\displaystyle\leq C\Big(\lambda\liminf\_{n\rightarrow\infty}\mathbb{E}[K^{\lambda,n,+}\_{T}|{\mathcal{F}}\_{t}]+(\lambda\ln(\lambda))^{2}+\lambda^{2}\mathbb{E}\big[\sup\_{t<s\leq T}V\_{s}^{2}\,\big|\,{\mathcal{F}}\_{t}\big]\Big). |  |

For t=0t=0, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | (V0λ−V0)2\displaystyle(V^{\lambda}\_{0}-V\_{0})^{2} | ≤C​(λ​lim infn𝔼​[KTλ,n,+]+(λ​ln⁡(λ))2+λ2​𝔼​[sup0≤s≤TVs2]).\displaystyle\leq C\Big(\lambda\liminf\_{n}\mathbb{E}[K^{\lambda,n,+}\_{T}]+(\lambda\ln(\lambda))^{2}+\lambda^{2}\mathbb{E}\big[\sup\_{0\leq s\leq T}V\_{s}^{2}\big]\Big). |  |

If the payoff PP is bounded, then sup0≤s≤TVs2\sup\_{0\leq s\leq T}V\_{s}^{2} is bounded as well, which combined with Lemma [4.4](https://arxiv.org/html/2602.18078v1#S4.Thmlem4 "Lemma 4.4. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") yields the simplified estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | (V0λ−V0)2\displaystyle(V^{\lambda}\_{0}-V\_{0})^{2} | ≤C​(λ+(λ​ln⁡(λ))2+λ2).\displaystyle\leq C(\lambda+(\lambda\ln(\lambda))^{2}+\lambda^{2}). |  |

This completes the proof.
∎

### 4.3 Reflected BSDE with a Singular Driver

In this subsection, we go beyond the non-asymptotic estimates of Subsection 4.2 and investigate the RBSDE structure satisfied by the limit process VλV^{\lambda}.
Under additional assumptions, we show that VλV^{\lambda}, previously introduced as the monotone limit of the penalized value processes Vλ,nV^{\lambda,n}, can be characterized as the value component of a RBSDE with a singular driver. More precisely, we prove the existence of processes
Mλ∈ℋ2M^{\lambda}\in\mathcal{H}^{2} and Aλ∈𝒦2A^{\lambda}\in\mathcal{K}^{2} such that the
triple (Vλ,Mλ,Aλ)(V^{\lambda},M^{\lambda},A^{\lambda}) solves the reflected BSDE ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). We then derive an optimal stopping representation for VλV^{\lambda}, thereby establishing a direct link between the singular RBSDE formulation and the associated optimal stopping problem. For technical convenience, we impose the following assumption.

###### Assumption 4.1.

All 𝔽{\mathbb{F}} martingales are continuous, and the payoff process PP is continuous.

###### Remark 4.3.

The above assumption, together with Lemma [4.8](https://arxiv.org/html/2602.18078v1#S4.Thmlem8 "Lemma 4.8. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), ensures that the limit process VλV^{\lambda} possesses continuous sample paths. This continuity is essential: it allows us to invoke the Doob-Meyer decomposition to identify uniquely the martingale component MλM^{\lambda} and the increasing process AλA^{\lambda} in the reflected BSDE. The situation contrasts with the classical penalization scheme (see, e.g., [[26](https://arxiv.org/html/2602.18078v1#bib.bib26)]), where the approximating sequence (Vλ,n)n≥1(V^{\lambda,n})\_{n\geq 1} is both monotone and consists of supermartingales. In that setting, Theorem 18 of Dellacherie and Meyer [[12](https://arxiv.org/html/2602.18078v1#bib.bib12), p. 86] applies directly to guarantee that the limit of the sequence has càdlàg trajectories.
By contrast, in our framework, although (Vλ,n)n≥1(V^{\lambda,n})\_{n\geq 1} remains monotone in nn, the individual processes are not supermartingales. Consequently, the argument based on Theorem 18 of [[12](https://arxiv.org/html/2602.18078v1#bib.bib12)] cannot be used here, and additional assumptions are needed to deduce the regularity of the limit.

We begin by proving that the entropy-regularized penalization scheme forms a Cauchy sequence in 𝒮2\mathcal{S}^{2}. As a consequence, the limit VλV^{\lambda} has continuous paths and satisfies Vtλ≥PtV^{\lambda}\_{t}\geq P\_{t}, t∈[0,T]t\in[0,T].

###### Lemma 4.8.

For any λ∈[0,1]\lambda\in[0,1], the entropy regularized penalization scheme {Vλ,n}n≥2\{V^{\lambda,n}\}\_{n\geq 2} is a Cauchy sequence in 𝒮2\mathcal{S}^{2}, and its limit satisfies: for all t∈[0,T]t\in[0,T], Vtλ:=limnVtλ,n≥PtV^{\lambda}\_{t}:=\lim\_{n}V^{\lambda,n}\_{t}\geq P\_{t} a.s.

###### Proof.

*Step 1.*
For any m,n≥2m,n\geq 2, Itô’s formula yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | eβ​t​(Vtλ,n−Vtλ,m)2≤−2​∫tTeβ​s​(Vsλ,n−Vsλ,m)​𝑑M¯sλ,n,m+2​∫tTeβ​s​(Vsλ,n−Vsλ,m)​d​(Asλ,n,ϵ−Asλ,m,ϵ)\displaystyle e^{\beta t}(V^{\lambda,n}\_{t}-V\_{t}^{\lambda,m})^{2}\leq-2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V^{\lambda,m}\_{s})d\bar{M}^{\lambda,n,m}\_{s}+2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})d(A^{\lambda,n,\epsilon}\_{s}-A^{\lambda,m,\epsilon}\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​∫tTeβ​s​(Vsλ,n−Vsλ,m)​d​(Ksλ,n,ϵ,+−Ksλ,m,ϵ,+)−2​∫tTeβ​s​(Vsλ,n−Vsλ,m)​d​(Ksλ,n,ϵ,−−Ksλ,m,ϵ,−)\displaystyle\quad+2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})d(K^{\lambda,n,\epsilon,+}\_{s}-K^{\lambda,m,\epsilon,+}\_{s})-2\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})d(K^{\lambda,n,\epsilon,-}\_{s}-K^{\lambda,m,\epsilon,-}\_{s}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −β​∫tTeβ​s​(Vsλ,n−Vsλ,m)2​𝑑s,\displaystyle\quad-\beta\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})^{2}ds, |  | (4.30) |

where M¯λ,n,m=Mλ,n−Mλ,m\bar{M}^{\lambda,n,m}=M^{\lambda,n}-M^{\lambda,m}. Without loss of generality, we assume n>mn>m. We now estimate each term of the above decomposition. By ([4.25](https://arxiv.org/html/2602.18078v1#S4.E25 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), the process Aλ,n,ϵA^{\lambda,n,\epsilon} increases only on the set {Vλ,n≤P+ϵ}\left\{V^{\lambda,n}\leq P+\epsilon\right\}. Hence,

|  |  |  |
| --- | --- | --- |
|  | ∫tT(Vsλ,n−Vsλ,m)​d​(Asλ,n,ϵ−Asλ,m,ϵ)\displaystyle\int^{T}\_{t}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})d(A^{\lambda,n,\epsilon}\_{s}-A^{\lambda,m,\epsilon}\_{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tT(Vsλ,n−Ps−ϵ)​𝑑Asλ,n,ϵ+∫tT(Ps+ϵ−Vsλ,m)​𝑑Asλ,n,ϵ\displaystyle=\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s}-\epsilon)dA^{\lambda,n,\epsilon}\_{s}+\int^{T}\_{t}(P\_{s}+\epsilon-V\_{s}^{\lambda,m})dA^{\lambda,n,\epsilon}\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | −∫tT(Vsλ,n−Ps−ϵ)​𝑑Asλ,m,ϵ+∫tT(Vsλ,m−Ps−ϵ)​𝑑Asλ,m,ϵ\displaystyle\quad-\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s}-\epsilon)dA\_{s}^{\lambda,m,\epsilon}+\int^{T}\_{t}(V\_{s}^{\lambda,m}-P\_{s}-\epsilon)dA\_{s}^{\lambda,m,\epsilon} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤−∫tT(Vsλ,m−Ps−ϵ)​𝑑Asλ,n,ϵ−∫tT(Vsλ,n−Ps−ϵ)​𝑑Asλ,m,ϵ\displaystyle\leq-\int^{T}\_{t}(V\_{s}^{\lambda,m}-P\_{s}-\epsilon)dA^{\lambda,n,\epsilon}\_{s}-\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s}-\epsilon)dA\_{s}^{\lambda,m,\epsilon} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫tT(Vsλ,m−Ps−ϵ)−​𝑑Asλ,n,ϵ+∫tT(Vsλ,n−Ps−ϵ)−​𝑑Asλ,m,ϵ\displaystyle\leq\int^{T}\_{t}(V\_{s}^{\lambda,m}-P\_{s}-\epsilon)^{-}dA^{\lambda,n,\epsilon}\_{s}+\int^{T}\_{t}(V^{\lambda,n}\_{s}-P\_{s}-\epsilon)^{-}dA\_{s}^{\lambda,m,\epsilon} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0T(Vsλ,m−Ps)−​𝑑Asλ,n,ϵ+∫0T(Vsλ,n−Ps)−​𝑑Asλ,m,ϵ+ϵ​ATλ,n,ϵ+ϵ​ATλ,m,ϵ.\displaystyle\leq\int^{T}\_{0}(V\_{s}^{\lambda,m}-P\_{s})^{-}dA^{\lambda,n,\epsilon}\_{s}+\int^{T}\_{0}(V\_{s}^{\lambda,n}-P\_{s})^{-}dA^{\lambda,m,\epsilon}\_{s}+\epsilon A^{\lambda,n,\epsilon}\_{T}+\epsilon A^{\lambda,m,\epsilon}\_{T}. |  |

Since the map x↦Φλ,n+​(s,x∨(Ps+ϵ))x\mapsto\Phi^{+}\_{\lambda,n}(s,x\vee(P\_{s}+\epsilon)) is decreasing,

|  |  |  |
| --- | --- | --- |
|  | ∫tTeβ​s​(Vsλ,n−Vsλ,m)​d​(Ksλ,n,ϵ,+−Ksλ,m,ϵ,+)\displaystyle\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})d(K^{\lambda,n,\epsilon,+}\_{s}-K^{\lambda,m,\epsilon,+}\_{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tTeβ​s​(Vsλ,n−Vsλ,m)​(Φλ,n+​(s,Vsλ,n∨(Ps+ϵ))−Φλ,m+​(s,Vsλ,m∨(Ps+ϵ)))​𝑑s\displaystyle=\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})(\Phi^{+}\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))-\Phi^{+}\_{\lambda,m}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon)))ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫tTeβ​s​(Vsλ,n−Vsλ,m)​(Φλ,n+​(s,Vsλ,m∨(Ps+ϵ))−Φλ,m+​(s,Vsλ,m∨(Ps+ϵ)))​𝑑s\displaystyle\leq\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})(\Phi^{+}\_{\lambda,n}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon))-\Phi^{+}\_{\lambda,m}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon)))ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0Teβ​s​(Vsλ,n−Vsλ,m)2​𝑑s+∫0Teβ​s​(Φλ,n+​(s,Vsλ,m∨(Ps+ϵ))−Φλ,m+​(s,Vsλ,m∨(Ps+ϵ)))2​𝑑s.\displaystyle\leq\int^{T}\_{0}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})^{2}ds+\int^{T}\_{0}e^{\beta s}(\Phi^{+}\_{\lambda,n}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon))-\Phi^{+}\_{\lambda,m}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon)))^{2}ds. |  |

For the second term in the above, we have

|  |  |  |
| --- | --- | --- |
|  | ∫0Teβ​s​(Φλ,n+​(s,Vsλ,m∨(Ps+ϵ))−Φλ,m+​(s,Vsλ,m∨(Ps+ϵ)))2​𝑑s\displaystyle\int^{T}\_{0}e^{\beta s}(\Phi^{+}\_{\lambda,n}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon))-\Phi^{+}\_{\lambda,m}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon)))^{2}ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤eβ​T​∫0T((λ​Φ​(−ϵλ/n)+λ​ln⁡n)−(λ​Φ​(−ϵλ/m)+λ​ln⁡m))2​𝑑s\displaystyle\leq e^{\beta T}\int^{T}\_{0}\left(\left(\lambda\Phi\left(-\frac{\epsilon}{\lambda/n}\right)+\lambda\ln n\right)-\left(\lambda\Phi\left(-\frac{\epsilon}{\lambda/m}\right)+\lambda\ln m\right)\right)^{2}ds |  |
|  |  |  |
| --- | --- | --- |
|  | =eβ​T​T​(λ​ln⁡(e−ϵλ/n−1−ϵλ/n​−ϵλ/me−ϵλ/m−1)+λ​ln⁡(nm))2\displaystyle=e^{\beta T}T\left(\lambda\ln\left(\frac{e^{-\frac{\epsilon}{\lambda/n}}-1}{-\frac{\epsilon}{\lambda/n}}\frac{-\frac{\epsilon}{\lambda/m}}{e^{-\frac{\epsilon}{\lambda/m}}-1}\right)+\lambda\ln\left(\frac{n}{m}\right)\right)^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | =eβ​T​T​λ2​(ln⁡(e−ϵλ/n−1e−ϵλ/m−1))2,\displaystyle=e^{\beta T}T\lambda^{2}\left(\ln\left(\frac{e^{-\frac{\epsilon}{\lambda/n}}-1}{e^{-\frac{\epsilon}{\lambda/m}}-1}\right)\right)^{2}, |  |

where we use the fact that the map x↦Φλ,n​(s,x∨(Ps+ϵ))+−Φλ,m​(s,x∨(Ps+ϵ))+x\mapsto\Phi\_{\lambda,n}(s,x\vee(P\_{s}+\epsilon))^{+}-\Phi\_{\lambda,m}(s,x\vee(P\_{s}+\epsilon))^{+} is decreasing. In particular, since n>mn>m, for any x≤Ps−λ​Φm−1​(0)x\leq P\_{s}-\lambda\Phi\_{m}^{-1}(0),

|  |  |  |
| --- | --- | --- |
|  | Φλ,n​(s,x∨(Ps+ϵ))−Φλ,m​(s,x∨(Ps+ϵ))\displaystyle\Phi\_{\lambda,n}(s,x\vee(P\_{s}+\epsilon))-\Phi\_{\lambda,m}(s,x\vee(P\_{s}+\epsilon)) |  |
|  |  |  |
| --- | --- | --- |
|  | =λ​Φ​(Ps−x∨(Ps+ϵ)λ/n)−λ​Φ​(Ps−x∨(Ps+ϵ)λ/m)+λ​ln⁡(nm)\displaystyle=\lambda\Phi\left(\frac{P\_{s}-x\vee(P\_{s}+\epsilon)}{\lambda/n}\right)-\lambda\Phi\left(\frac{P\_{s}-x\vee(P\_{s}+\epsilon)}{\lambda/m}\right)+\lambda\ln\left(\frac{n}{m}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =λ​ln⁡(ePs−x∨(Ps+ϵ)λ/n−1ePs−x∨(Ps+ϵ)λ/m−1),\displaystyle={\lambda}\ln\left(\frac{e^{\frac{P\_{s}-x\vee(P\_{s}+\epsilon)}{\lambda/n}}-1}{e^{\frac{P\_{s}-x\vee(P\_{s}+\epsilon)}{\lambda/m}}-1}\right), |  |

which is decreasing by Lemma [6.5](https://arxiv.org/html/2602.18078v1#S6.Thmlem5 "Lemma 6.5. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"). For x≥Ps−λ​Φm−1​(0)x\geq P\_{s}-\lambda\Phi\_{m}^{-1}(0), the difference reduces to Φλ,n+​(s,x)\Phi\_{\lambda,n}^{+}(s,x) which is also decreasing by Lemma [6.2](https://arxiv.org/html/2602.18078v1#S6.Thmlem2 "Lemma 6.2. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators").

To estimate the integral against Kλ,n,ϵ,−−Kλ,m,ϵ,−K^{\lambda,n,\epsilon,-}-K^{\lambda,m,\epsilon,-} in equation ([4.3](https://arxiv.org/html/2602.18078v1#S4.Ex60 "Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we apply Young’s inequality to obtain

|  |  |  |
| --- | --- | --- |
|  | ∫tTeβ​s​(Vsλ,n−Vsλ,m)​d​(Ksλ,n,ϵ,−−Ksλ,m,ϵ,−)\displaystyle\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V\_{s}^{\lambda,m})d(K^{\lambda,n,\epsilon,-}\_{s}-K^{\lambda,m,\epsilon,-}\_{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫tTeβ​s​(Vsλ,n−Vsλ,m)2​𝑑s+∫tTeβ​s​(Φλ,n−​(s,Vsλ,n)−Φλ,m−​(s,Vsλ,m))2​𝑑s.\displaystyle\leq\int^{T}\_{t}e^{\beta s}(V^{\lambda,n}\_{s}-V^{\lambda,m}\_{s})^{2}ds+\int\_{t}^{T}e^{\beta s}(\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s}))^{2}ds. |  |

Regarding the local martingale term in ([4.3](https://arxiv.org/html/2602.18078v1#S4.Ex60 "Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), observe that the process

|  |  |  |
| --- | --- | --- |
|  | ∫0te−β​(t−s)​(Vsλ,n−Vsλ,m)​𝑑M¯sλ,n,m,\int^{t}\_{0}e^{-\beta(t-s)}(V^{\lambda,n}\_{s}-V^{\lambda,m}\_{s})d\bar{M}^{\lambda,n,m}\_{s}, |  |

is a uniformly integrable martingale. This follows from the BDG and Young inequalities, since

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(∫0Te−2​β​(T−s)​(Vsλ,n−Vsλ,m)2​d​[M¯λ,n,m]s)12]\displaystyle{\mathbb{E}}\left[\left(\int\_{0}^{T}e^{-2\beta(T-s)}(V^{\lambda,n}\_{s}-V^{\lambda,m}\_{s})^{2}d[\bar{M}^{\lambda,n,m}]\_{s}\right)^{\frac{1}{2}}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​𝔼​[sup0≤s≤T(Vsλ,n−Vsλ,m)2+[M¯λ,n,m]T]\displaystyle\leq C{\mathbb{E}}\left[\sup\_{0\leq s\leq T}(V^{\lambda,n}\_{s}-V^{\lambda,m}\_{s})^{2}+[\bar{M}^{\lambda,n,m}]\_{T}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​𝔼​[sup0≤s≤T(Vsλ,n)2+sup0≤s≤T(Vsλ,m)2+[M¯λ,n,m]T]<∞.\displaystyle\leq C{\mathbb{E}}\left[\sup\_{0\leq s\leq T}(V^{\lambda,n}\_{s})^{2}+\sup\_{0\leq s\leq T}(V^{\lambda,m}\_{s})^{2}+[\bar{M}^{\lambda,n,m}]\_{T}\right]<\infty. |  |

Taking expectations on both sides of ([4.3](https://arxiv.org/html/2602.18078v1#S4.Ex60 "Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and combining the above estimates, and choosing β=2\beta=2, we obtain the upper bound

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T(Vtλ,n−Vtλ,m)2]\displaystyle{\mathbb{E}}\left[\sup\_{0\leq t\leq T}(V\_{t}^{\lambda,n}-V^{\lambda,m}\_{t})^{2}\right] | ≤e2​T​𝔼​[∫0T(Vsλ,m−Ps)−​𝑑Asλ,n,ϵ]\displaystyle\leq e^{2T}{\mathbb{E}}\left[\int^{T}\_{0}(V\_{s}^{\lambda,m}-P\_{s})^{-}dA^{\lambda,n,\epsilon}\_{s}\right] |  | (4.31) |
|  |  | +e2​T​[∫0T(Vsλ,n−Ps)−​𝑑Asλ,m,ϵ]\displaystyle\quad+e^{2T}\left[\int^{T}\_{0}(V^{\lambda,n}\_{s}-P\_{s})^{-}dA\_{s}^{\lambda,m,\epsilon}\right] |  |
|  |  | +e2​T​T​λ22​[ln⁡(e−ϵλ/n−1e−ϵλ/m−1)]2\displaystyle\quad+\frac{e^{2T}T\lambda^{2}}{2}\left[\ln\left(\frac{e^{-\frac{\epsilon}{\lambda/n}}-1}{e^{-\frac{\epsilon}{\lambda/m}}-1}\right)\right]^{2} |  |
|  |  | +e2​T​𝔼​[∫0T(Φλ,n−​(s,Vsλ,n)−Φλ,m−​(s,Vsλ,m))2​𝑑s]\displaystyle\quad+e^{2T}{\mathbb{E}}\left[\int^{T}\_{0}(\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s}))^{2}ds\right] |  |
|  |  | +e2​T​ϵ​𝔼​[ATλ,n,ϵ]+e2​T​ϵ​𝔼​[ATλ,m,ϵ].\displaystyle\quad+e^{2T}\epsilon{\mathbb{E}}[A^{\lambda,n,\epsilon}\_{T}]+e^{2T}\epsilon{\mathbb{E}}[A^{\lambda,m,\epsilon}\_{T}]. |  |

*Step 2.* We consider the limit as nn, m→∞m\rightarrow\infty of each term in ([4.31](https://arxiv.org/html/2602.18078v1#S4.E31 "In Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). For the first term, recall that

|  |  |  |
| --- | --- | --- |
|  | Vtλ,m=PT−∫tT𝑑Msλ,m+∫tT𝑑Ksλ,m,ϵ,+−∫tT𝑑Ksλ,m,ϵ,−+∫tT𝑑Asλ,m,ϵ.\displaystyle V^{\lambda,m}\_{t}=P\_{T}-\int^{T}\_{t}dM^{\lambda,m}\_{s}+\int^{T}\_{t}dK^{\lambda,m,\epsilon,+}\_{s}-\int^{T}\_{t}dK^{\lambda,m,\epsilon,-}\_{s}+\int^{T}\_{t}dA^{\lambda,m,\epsilon}\_{s}. |  |

We consider the unique solution (Ym,δ,Mm,δ)(Y^{m,\delta},M^{m,\delta}) to the following BSDE with Lipschitz driver

|  |  |  |
| --- | --- | --- |
|  | Ytm,δ=PT−∫tT𝑑Msm,δ−∫tTΦλ,m−​(s,Vsλ,m)​𝑑s+∫tTβm,δ​(Ps+δ−Ysm,δ)​𝑑s,\displaystyle Y^{m,\delta}\_{t}=P\_{T}-\int\_{t}^{T}dM\_{s}^{m,\delta}-\int\_{t}^{T}\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})ds+\int\_{t}^{T}\beta\_{m,\delta}(P\_{s}+\delta-Y^{m,\delta}\_{s})ds, |  |

where βm,δ:=m​Φ′​(−δλ/m)\beta\_{m,\delta}:=m\Phi^{\prime}\left(-\frac{\delta}{\lambda/m}\right) and δ<ϵ\delta<\epsilon. By the inequality a∨b=(b−a)++aa\vee b=(b-a)^{+}+a and the mean-value theorem

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φλ,m​(s,Ysm,δ)−Φλ,m​(s,Ysm,δ∨(Ps+ϵ))\displaystyle\Phi\_{\lambda,m}(s,Y^{m,\delta}\_{s})-\Phi\_{\lambda,m}(s,Y^{m,\delta}\_{s}\vee(P\_{s}+\epsilon)) | ≥Φλ,m​(s,Ysm,δ)−Φλ,m​(s,Ysm,δ∨(Ps+δ))\displaystyle\geq\Phi\_{\lambda,m}(s,Y^{m,\delta}\_{s})-\Phi\_{\lambda,m}(s,Y^{m,\delta}\_{s}\vee(P\_{s}+\delta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥m​Φ′​(−δλ/m)​(Ps+δ−Ysm,δ).\displaystyle\geq m\Phi^{\prime}\left(-\frac{\delta}{\lambda/m}\right)(P\_{s}+\delta-Y^{m,\delta}\_{s}). |  |

Moreover, since −Φλ,m−​(s,Vsλ,m)≤Φλ,m​(s,Vsλ,m∨(Ps+ϵ))-\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})\leq\Phi\_{\lambda,m}(s,V^{\lambda,m}\_{s}\vee(P\_{s}+\epsilon)), by the comparison theorem

|  |  |  |
| --- | --- | --- |
|  | Vtλ,m≥Ytm,δ,t∈[0,T].V^{\lambda,m}\_{t}\geq Y^{m,\delta}\_{t},\quad t\in[0,T]. |  |

From Itô’s formula, we have the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yτm,δ=𝔼[\displaystyle Y^{m,\delta}\_{\tau}={\mathbb{E}}\Bigg[ | e−βm,δ​(T−τ)PT−∫τTe−βm,δ​(s−τ)Φλ,m−(s,Vsλ,m)ds+βm,δ∫τTe−βm,δ​(s−τ)(Ps+δ)ds|ℱτ],\displaystyle e^{-\beta\_{m,\delta}(T-\tau)}P\_{T}-\int\_{\tau}^{T}e^{-\beta\_{m,\delta}(s-\tau)}\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})ds+\beta\_{m,\delta}\int\_{\tau}^{T}e^{-\beta\_{m,\delta}(s-\tau)}(P\_{s}+\delta)ds\Bigg|{\mathcal{F}}\_{\tau}\Bigg], |  |

for any τ∈𝒯0,T\tau\in{\mathcal{T}}\_{0,T}. Moreover, since βm,δ→m2\beta\_{m,\delta}\rightarrow\frac{m}{2} as δ→0\delta\rightarrow 0 and

|  |  |  |
| --- | --- | --- |
|  | e−βm,δ​(T−τ)​PT−∫τTe−βm,δ​(s−τ)​Φλ,m−​(s,Vsλ,m)​𝑑s+βm,δ​∫τTe−βm,δ​(s−τ)​(Ps+δ)​𝑑s\displaystyle e^{-\beta\_{m,\delta}(T-\tau)}P\_{T}-\int\_{\tau}^{T}e^{-\beta\_{m,\delta}(s-\tau)}\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})ds+\beta\_{m,\delta}\int\_{\tau}^{T}e^{-\beta\_{m,\delta}(s-\tau)}(P\_{s}+\delta)ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤PT+m​∫0T(Ps+δ)​𝑑s\displaystyle\leq P\_{T}+m\int\_{0}^{T}(P\_{s}+\delta)ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​(sup0≤s≤T|Ps|+δ),\displaystyle\leq C\left(\sup\_{0\leq s\leq T}|P\_{s}|+\delta\right), |  |

the dominated convergence theorem guarantees that

|  |  |  |
| --- | --- | --- |
|  | Yτm:=limδ→0Yτm,δ=𝔼​[e−m2​(T−τ)​PT−∫τTe−m2​(s−τ)​Φλ,m−​(s,Vsλ,m)​𝑑s+m2​∫τTe−m2​(s−τ)​Ps​𝑑s|ℱτ].\displaystyle Y^{m}\_{\tau}:=\lim\_{\delta\rightarrow 0}Y^{m,\delta}\_{\tau}={\mathbb{E}}\Bigg[e^{-\frac{m}{2}(T-\tau)}P\_{T}-\int\_{\tau}^{T}e^{-\frac{m}{2}(s-\tau)}\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})ds+\frac{m}{2}\int\_{\tau}^{T}e^{-\frac{m}{2}(s-\tau)}P\_{s}ds\Bigg|{\mathcal{F}}\_{\tau}\Bigg]. |  |

We now pass to the limit as m→∞m\rightarrow\infty in the above limit. It follows from the Cauchy-Schwarz inequality, the Lipschitz regularity of Φλ,m−\Phi\_{\lambda,m}^{-} and the fact that Vλ,m∈𝒮2V^{\lambda,m}\in\mathcal{S}^{2} that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫τTe−m2​(s−τ)​Φλ,m−​(s,Vsλ,m)​𝑑s|ℱτ]​⟶a.s.&L2​(ℙ)​0, as ​m→∞,{\mathbb{E}}\left[\int\_{\tau}^{T}e^{-\frac{m}{2}(s-\tau)}\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})ds\Bigg|{\mathcal{F}}\_{\tau}\right]\overset{a.s.\&L^{2}(\mathbb{P})}{\longrightarrow}0,\quad\mbox{ as }m\rightarrow\infty, |  |

so that,

|  |  |  |
| --- | --- | --- |
|  | Yτm=𝔼​[e−m2​(T−τ)​PT−∫τTe−m2​(s−τ)​Φλ,m−​(s,Vsλ,m)​𝑑s+m2​∫τTe−m2​(s−τ)​Ps​𝑑s|ℱτ]\displaystyle Y^{m}\_{\tau}={\mathbb{E}}\left[e^{-\frac{m}{2}(T-\tau)}P\_{T}-\int\_{\tau}^{T}e^{-\frac{m}{2}(s-\tau)}\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})ds+\frac{m}{2}\int\_{\tau}^{T}e^{-\frac{m}{2}(s-\tau)}P\_{s}ds\Bigg|{\mathcal{F}}\_{\tau}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ⟶a.s.&L2​(ℙ)​PT​𝟙{τ=T}+Pτ​𝟙{τ<T}≥Pτ.\displaystyle\overset{a.s.\&L^{2}(\mathbb{P})}{\longrightarrow}P\_{T}\mathds{1}\_{\{\tau=T\}}+P\_{\tau}\mathds{1}\_{\{\tau<T\}}\geq P\_{\tau}. |  |

Hence, by the section theorem (see Theorem 3.2 in [[35](https://arxiv.org/html/2602.18078v1#bib.bib35)])
Vλ≥PV^{\lambda}\geq P
which in turn, using the fact that Vλ,m↑VλV^{\lambda,m}\uparrow V^{\lambda}, yields

|  |  |  |
| --- | --- | --- |
|  | (Vsλ,m−Ps)−↓0,a.s.(V^{\lambda,m}\_{s}-P\_{s})^{-}\downarrow 0,\quad a.s. |  |

It follows from Dini’s theorem that sup0≤s≤T(Vsλ,m−Ps)−↓0\sup\_{0\leq s\leq T}(V\_{s}^{\lambda,m}-P\_{s})^{-}\downarrow 0. Finally, by the Cauchy-Schwarz inequality, Lemma [4.5](https://arxiv.org/html/2602.18078v1#S4.Thmlem5 "Lemma 4.5. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and the monotone convergence theorem

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫tT(Vsλ,m−Ps)−​𝑑Asλ,n,ϵ]\displaystyle{\mathbb{E}}\left[\int\_{t}^{T}(V\_{s}^{\lambda,m}-P\_{s})^{-}dA\_{s}^{\lambda,n,\epsilon}\right] | ≤𝔼​[sup0≤s≤T(Vsλ,m−Ps)−​ATλ,n,ϵ]\displaystyle\leq{\mathbb{E}}\left[\sup\_{0\leq s\leq T}(V\_{s}^{\lambda,m}-P\_{s})^{-}A\_{T}^{\lambda,n,\epsilon}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(𝔼​[(sup0≤s≤T(Vsλ,m−Ps)−)2])12​‖Aλ,n,ϵ‖𝒮212→0,\displaystyle\leq\left({\mathbb{E}}\left[\left(\sup\_{0\leq s\leq T}(V\_{s}^{\lambda,m}-P\_{s})^{-}\right)^{2}\right]\right)^{\frac{1}{2}}\|A^{\lambda,n,\epsilon}\|\_{\mathcal{S}^{2}}^{\frac{1}{2}}\rightarrow 0, |  |

as n,m→∞n,m\rightarrow\infty. Similarly, we deduce that 𝔼​[∫tT(Vsλ,n−Ps)−​𝑑Asλ,m,ϵ]→0{\mathbb{E}}[\int\_{t}^{T}(V\_{s}^{\lambda,n}-P\_{s})^{-}dA\_{s}^{\lambda,m,\epsilon}]\rightarrow 0 as nn, m→∞m\rightarrow\infty.

The third term in ([4.31](https://arxiv.org/html/2602.18078v1#S4.E31 "In Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) vanishes since for any ϵ≥0\epsilon\geq 0

|  |  |  |
| --- | --- | --- |
|  | limn,m→∞ln⁡(e−ϵλ/n−1e−ϵλ/m−1)=0.\lim\_{n,m\rightarrow\infty}\ln\left(\frac{e^{-\frac{\epsilon}{\lambda/n}}-1}{e^{-\frac{\epsilon}{\lambda/m}}-1}\right)=0. |  |

For the fourth term in ([4.31](https://arxiv.org/html/2602.18078v1#S4.E31 "In Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), by ([4.15](https://arxiv.org/html/2602.18078v1#S4.E15 "In Proof. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and Corollary [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmcor1 "Corollary 4.1. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), we note that the function Φλ,n−​(s,x)\Phi^{-}\_{\lambda,n}(s,x) is Lipschitz continuous with coefficient independent of nn and decreasing in λ\lambda,

|  |  |  |
| --- | --- | --- |
|  | (Φλ,n−​(s,Vsλ,n)−Φλ,m−​(s,Vsλ,m))2≤4​max⁡{1,1/|Φ2−1​(0)|2}​(Vsλ)2.\displaystyle(\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s}))^{2}\leq 4\max\{1,1/|\Phi\_{2}^{-1}(0)|^{2}\}(V^{\lambda}\_{s})^{2}. |  |

Also, in view of ([4.28](https://arxiv.org/html/2602.18078v1#S4.E28 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and the Lipschitz continuity of Φλ,n−\Phi\_{\lambda,n}^{-} and Φλ,m−\Phi\_{\lambda,m}^{-} with Lipschitz coefficient C:=max⁡{1,1/|Φ2−1​(0)|}C:=\max\{1,1/|\Phi^{-1}\_{2}(0)|\} by Corollary [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmcor1 "Corollary 4.1. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), we have

|  |  |  |
| --- | --- | --- |
|  | |Φλ,n−​(s,Vsλ,n)−Φλ,m−​(s,Vsλ,m)|\displaystyle|\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤|Φλ,n−​(s,Vsλ,n)−Φλ,∞−​(s,Vsλ)|+|Φλ,∞−​(s,Vsλ)−Φλ,m−​(s,Vsλ,m)|\displaystyle\leq|\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})-\Phi^{-}\_{\lambda,\infty}(s,V\_{s}^{\lambda})|+|\Phi^{-}\_{\lambda,\infty}(s,V\_{s}^{\lambda})-\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s})| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤|Φλ,n−​(s,Vsλ,n)−Φλ,n−​(s,Vsλ)|+|Φλ,n−​(s,Vsλ)−Φλ,∞−​(s,Vsλ)|\displaystyle\leq\big|\Phi\_{\lambda,n}^{-}(s,V^{\lambda,n}\_{s})-\Phi\_{\lambda,n}^{-}(s,V^{\lambda}\_{s})|+|\Phi\_{\lambda,n}^{-}(s,V^{\lambda}\_{s})-\Phi\_{\lambda,\infty}^{-}(s,V^{\lambda}\_{s})\big| |  |
|  |  |  |
| --- | --- | --- |
|  | +|Φλ,m−​(s,Vsλ,m)−Φλ,m−​(s,Vsλ)|+|Φλ,m−​(s,Vsλ)−Φλ,∞−​(s,Vsλ)|\displaystyle\hskip 10.00002pt+\big|\Phi\_{\lambda,m}^{-}(s,V^{\lambda,m}\_{s})-\Phi\_{\lambda,m}^{-}(s,V^{\lambda}\_{s})|+|\Phi\_{\lambda,m}^{-}(s,V^{\lambda}\_{s})-\Phi\_{\lambda,\infty}^{-}(s,V^{\lambda}\_{s})\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​|Vsλ,n−Vsλ|+|Φλ,n−​(s,Vsλ)−Φλ,∞−​(s,Vsλ)|+C​|Vsλ,m−Vsλ|+|Φλ,m−​(s,Vsλ)−Φλ,∞−​(s,Vsλ)|,\displaystyle\leq C|V^{\lambda,n}\_{s}-V^{\lambda}\_{s}|+\big|\Phi\_{\lambda,n}^{-}(s,V^{\lambda}\_{s})-\Phi\_{\lambda,\infty}^{-}(s,V^{\lambda}\_{s})\big|+C|V^{\lambda,m}\_{s}-V^{\lambda}\_{s}|+\big|\Phi\_{\lambda,m}^{-}(s,V^{\lambda}\_{s})-\Phi\_{\lambda,\infty}^{-}(s,V^{\lambda}\_{s})\big|, |  |

which converges to zero as n,m→∞n,m\rightarrow\infty. Hence, by the dominated convergence theorem

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T(−Φλ,n−​(s,Vsλ,n)+Φλ,m−​(s,Vsλ,m))2​𝑑s]→0, as ​m,n→∞.{\mathbb{E}}\left[\int^{T}\_{0}(-\Phi^{-}\_{\lambda,n}(s,V^{\lambda,n}\_{s})+\Phi^{-}\_{\lambda,m}(s,V^{\lambda,m}\_{s}))^{2}ds\right]\rightarrow 0,\quad\mbox{ as }m,n\rightarrow\infty. |  |

Finally, by Lemma [4.5](https://arxiv.org/html/2602.18078v1#S4.Thmlem5 "Lemma 4.5. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), we obtain

|  |  |  |
| --- | --- | --- |
|  | e2​T​ϵ​𝔼​[ATλ,n,ϵ]+e2​T​ϵ​𝔼​[ATλ,m,ϵ]≤2​C​e2​T​ϵ.e^{2T}\epsilon{\mathbb{E}}[A^{\lambda,n,\epsilon}\_{T}]+e^{2T}\epsilon{\mathbb{E}}[A^{\lambda,m,\epsilon}\_{T}]\leq 2Ce^{2T}\epsilon. |  |

Note that the left-hand side of ([4.31](https://arxiv.org/html/2602.18078v1#S4.E31 "In Proof. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) does not depend on ϵ\epsilon. Hence, after sending n,m→∞n,m\to\infty, we may let ϵ↓0\epsilon\downarrow 0 and deduce that the sequence (Vλ,n)n≥1(V^{\lambda,n})\_{n\geq 1} is Cauchy in 𝒮2\mathcal{S}^{2}.
∎

By Lemma [4.8](https://arxiv.org/html/2602.18078v1#S4.Thmlem8 "Lemma 4.8. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), the sequence Vλ,nV^{\lambda,n} converges to VλV^{\lambda} in 𝒮2\mathcal{S}^{2} as n→∞n\to\infty, and therefore the limit inherits the continuity of the sample paths. We thus obtain the following result.

###### Corollary 4.3.

The process VλV^{\lambda} has continuous sample paths.

For fixed n≥2n\geq 2 and 0≤λ≤10\leq\lambda\leq 1, using ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) we may rewrite Vλ,nV^{\lambda,n} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vλ,n=V0λ,n+Mλ,n−(Kλ,n,ϵ+Aλ,n,ϵ).V^{\lambda,n}=V^{\lambda,n}\_{0}+M^{\lambda,n}-\bigl(K^{\lambda,n,\epsilon}+A^{\lambda,n,\epsilon}\bigr). |  | (4.32) |

We then observe that Vλ,n+Kλ,n,ϵV^{\lambda,n}+K^{\lambda,n,\epsilon} is a continuous supermartingale in 𝒮2\mathcal{S}^{2}. By the dominated convergence theorem, we may pass to the limit as n→∞n\to\infty and obtain, for all s≤ts\leq t,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[Vtλ+Ktλ,ϵ|ℱs]≤Vsλ+Ksλ,ϵ,{\mathbb{E}}\left[V^{\lambda}\_{t}+K^{\lambda,\epsilon}\_{t}\middle|{\mathcal{F}}\_{s}\right]\leq V^{\lambda}\_{s}+K^{\lambda,\epsilon}\_{s}, |  | (4.33) |

where integrability follows from Corollary [4.2](https://arxiv.org/html/2602.18078v1#S4.Thmcor2 "Corollary 4.2. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and Lemma [4.6](https://arxiv.org/html/2602.18078v1#S4.Thmlem6 "Lemma 4.6. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), since VλV^{\lambda}, Kλ,ϵK^{\lambda,\epsilon}, and PP all lie in 𝒮2\mathcal{S}^{2}. Consequently, the process Vλ+Kλ,ϵV^{\lambda}+K^{\lambda,\epsilon} is a continuous supermartingale of class (D).
By Lemma [4.8](https://arxiv.org/html/2602.18078v1#S4.Thmlem8 "Lemma 4.8. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), together with the monotonicity of Kλ,ϵK^{\lambda,\epsilon} in ϵ\epsilon, taking the limit as ϵ→0\epsilon\to 0 yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[Vtλ+Ktλ|ℱs]≤Vsλ+Ksλ.\displaystyle{\mathbb{E}}\left[V^{\lambda}\_{t}+K^{\lambda}\_{t}\middle|{\mathcal{F}}\_{s}\right]\leq V^{\lambda}\_{s}+K^{\lambda}\_{s}. |  | (4.34) |

Moreover, by Corollary [4.2](https://arxiv.org/html/2602.18078v1#S4.Thmcor2 "Corollary 4.2. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and Lemma [4.6](https://arxiv.org/html/2602.18078v1#S4.Thmlem6 "Lemma 4.6. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), both VλV^{\lambda} and KλK^{\lambda} lie in 𝒮2\mathcal{S}^{2}; hence Vλ+KλV^{\lambda}+K^{\lambda} is a process of class (D). The Doob-Meyer decomposition applied to this continuous supermartingale then guarantees the existence of a uniformly integrable martingale MλM^{\lambda} and an integrable, non-decreasing process AλA^{\lambda} such that

|  |  |  |
| --- | --- | --- |
|  | Vtλ=PT−∫tT𝑑Msλ+∫tTΦλ,∞​(s,Vsλ)​𝑑s+(ATλ−Atλ).\displaystyle V^{\lambda}\_{t}=P\_{T}-\int^{T}\_{t}dM^{\lambda}\_{s}+\int^{T}\_{t}\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s})ds+(A^{\lambda}\_{T}-A^{\lambda}\_{t}). |  |

It remains to prove that Mλ∈ℋ2M^{\lambda}\in\mathcal{H}^{2}, and that the non-decreasing process AλA^{\lambda} belongs to 𝒦2\mathcal{K}^{2} and satisfies the Skorokhod reflection condition ∫0T(Vsλ−Ps)​𝑑Asλ=0\int^{T}\_{0}(V^{\lambda}\_{s}-P\_{s})dA^{\lambda}\_{s}=0. To this end, we show that the continuous supermartingale Vλ+KλV^{\lambda}+K^{\lambda} has an optimal stopping representation.

###### Theorem 4.2.

There exist processes (Mλ,Aλ)∈ℋ2×𝒦2(M^{\lambda},A^{\lambda})\in\mathcal{H}^{2}\times\mathcal{K}^{2} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ+Ktλ\displaystyle V^{\lambda}\_{t}+K^{\lambda}\_{t} | =ess​supσ∈𝒯t,T⁡𝔼​[Pσ+Kσλ|ℱt]=Mtλ−Atλ,\displaystyle=\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\sigma}+K^{\lambda}\_{\sigma}|{\mathcal{F}}\_{t}]=M^{\lambda}\_{t}-A^{\lambda}\_{t}, |  |

and the process AλA^{\lambda} satisfies the Skorokhod reflection condition ∫0T(Vsλ−Ps)​𝑑Asλ=0\int^{T}\_{0}(V^{\lambda}\_{s}-P\_{s})\,dA^{\lambda}\_{s}=0.

###### Proof.

*Step 1.* From ([4.34](https://arxiv.org/html/2602.18078v1#S4.E34 "In 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and Lemma [4.8](https://arxiv.org/html/2602.18078v1#S4.Thmlem8 "Lemma 4.8. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") we know that Vλ+KλV^{\lambda}+K^{\lambda} is a continuous supermartingale and that Vtλ≥PtV^{\lambda}\_{t}\geq P\_{t} a.s. for all t∈[0,T]t\in[0,T]. Consequently, Vtλ+Ktλ≥Pt+KtλV^{\lambda}\_{t}+K^{\lambda}\_{t}\geq P\_{t}+K^{\lambda}\_{t} and, by the defining property of the Snell envelope associated with the process P+KλP+K^{\lambda}, it follows that

|  |  |  |
| --- | --- | --- |
|  | Vtλ+Ktλ≥ess​supσ∈𝒯t,T⁡𝔼​[Pσ+Kσλ|ℱt],a.s.\displaystyle V^{\lambda}\_{t}+K^{\lambda}\_{t}\geq\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\sigma}+K^{\lambda}\_{\sigma}|{\mathcal{F}}\_{t}],\quad a.s. |  |

*Step 2.* To establish the reverse inequality, we introduce the sequence of hitting times σnϵ:=inf{s≥t:Vsλ,n≤Ps+ϵ}∧T\sigma\_{n}^{\epsilon}:=\inf\{s\geq t:V^{\lambda,n}\_{s}\leq P\_{s}+\epsilon\}\wedge T. Since the sequence (Vλ,n)n≥1(V^{\lambda,n})\_{n\geq 1} is non-decreasing, we have σnϵ≤σn+1ϵ\sigma\_{n}^{\epsilon}\leq\sigma\_{n+1}^{\epsilon} for all nn. We may therefore define

|  |  |  |
| --- | --- | --- |
|  | σϵ:=limn→∞σnϵ,\sigma^{\epsilon}:=\lim\_{n\rightarrow\infty}\sigma\_{n}^{\epsilon}, |  |

which is a stopping time, as {σϵ≤t}=∪n{σnϵ≤t}∈ℱt\{\sigma^{\epsilon}\leq t\}=\cup\_{n}\{\sigma^{\epsilon}\_{n}\leq t\}\in{\mathcal{F}}\_{t}. By ([4.25](https://arxiv.org/html/2602.18078v1#S4.E25 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), we have Aσnϵλ,n,ϵ−Atλ,n,ϵ=0A\_{\sigma^{\epsilon}\_{n}}^{\lambda,n,\epsilon}-A\_{t}^{\lambda,n,\epsilon}=0. Hence, invoking the decomposition ([4.32](https://arxiv.org/html/2602.18078v1#S4.E32 "In 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) together with the optional sampling theorem, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ,n+Ktλ,n,ϵ\displaystyle V^{\lambda,n}\_{t}+K^{\lambda,n,\epsilon}\_{t} | =𝔼​[Mσnϵλ,n−Atλ,n,ϵ|ℱt]\displaystyle={\mathbb{E}}[M^{\lambda,n}\_{\sigma^{\epsilon}\_{n}}-A^{\lambda,n,\epsilon}\_{t}|{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[Vσnϵλ,n+Kσnϵλ,n,ϵ|ℱt]≤𝔼​[Pσnϵ+Kσnϵλ,n,ϵ|ℱt]+ϵ.\displaystyle={\mathbb{E}}[V^{\lambda,n}\_{\sigma\_{n}^{\epsilon}}+K^{\lambda,n,\epsilon}\_{\sigma\_{n}^{\epsilon}}|{\mathcal{F}}\_{t}]\leq\mathbb{E}[P\_{\sigma\_{n}^{\epsilon}}+K^{\lambda,n,\epsilon}\_{\sigma\_{n}^{\epsilon}}|{\mathcal{F}}\_{t}]+\epsilon. |  |

It follows from Lemmas [4.2](https://arxiv.org/html/2602.18078v1#S4.Thmlem2 "Lemma 4.2. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") and [4.3](https://arxiv.org/html/2602.18078v1#S4.Thmlem3 "Lemma 4.3. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), together with the inequality Vsλ,n≤VsV\_{s}^{\lambda,n}\leq V\_{s} that |Φλ,n​(s,Vsλ,n∨(Ps+ϵ))|≤λϵ​(|Vsλ|+|Ps|+λ)|\Phi\_{\lambda,n}(s,V^{\lambda,n}\_{s}\vee(P\_{s}+\epsilon))|\leq\frac{\lambda}{\epsilon}\left(|V^{\lambda}\_{s}|+|P\_{s}|+\lambda\right). Combining this estimate with the continuity of the mapping s↦Pss\mapsto P\_{s}, we may pass to the limit as n→∞n\rightarrow\infty in the previous inequality. An application of the dominated convergence theorem, together with ([4.26](https://arxiv.org/html/2602.18078v1#S4.E26 "In 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), then yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ+Ktλ,ϵ\displaystyle V^{\lambda}\_{t}+K^{\lambda,\epsilon}\_{t} | ≤𝔼​[Pσϵ+Kσϵλ,ϵ|ℱt]+ϵ.\displaystyle\leq\mathbb{E}[P\_{\sigma^{\epsilon}}+K^{\lambda,\epsilon}\_{\sigma^{\epsilon}}|{\mathcal{F}}\_{t}]+\epsilon. |  |

Next, we observe that the stopping times σϵ\sigma^{\epsilon} form an increasing family as ϵ∈ℚ∩(0,∞)\epsilon\in\mathbb{Q}\cap(0,\infty) decreases to zero. Consequently the limit σ∗:=limϵ→0σϵ\sigma^{\*}:=\lim\_{\epsilon\rightarrow 0}\sigma^{\epsilon} exists and defines a stopping time. In order to pass to the limit as ϵ\epsilon, we first note that the process Kλ,ϵK^{\lambda,\epsilon} can be decomposed as the sum of two integrable increasing processes, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ktλ,ϵ\displaystyle K^{\lambda,\epsilon}\_{t} | =∫0tΦλ,∞​(s,Vsλ∨(Ps+ϵ))​𝟙{Vsλ≤Ps+λ}​𝑑s+∫0tΦλ,∞​(s,Vsλ)​𝟙{Vsλ>Ps+λ}​𝑑s.\displaystyle=\int^{t}\_{0}\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s}\vee(P\_{s}+\epsilon))\mathds{1}\_{\{V^{\lambda}\_{s}\leq P\_{s}+\lambda\}}ds+\int^{t}\_{0}\Phi\_{\lambda,\infty}(s,V^{\lambda}\_{s})\mathds{1}\_{\{V^{\lambda}\_{s}>P\_{s}+\lambda\}}ds. |  |

The first integral defines an integrable increasing process whose integrand is monotone in ϵ<λ\epsilon<\lambda as ϵ→0\epsilon\rightarrow 0, while the second integral is an integrable decreasing process. Therefore, letting ϵ→0\epsilon\rightarrow 0 and applying the monotone convergence theorem, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ+Ktλ\displaystyle V^{\lambda}\_{t}+K^{\lambda}\_{t} | ≤𝔼​[Pσ∗+Kσ∗λ|ℱt]≤ess​supσ∈𝒯t,T⁡𝔼​[Pσ+Kσλ|ℱt].\displaystyle\leq\mathbb{E}[P\_{\sigma^{\*}}+K^{\lambda}\_{\sigma^{\*}}|{\mathcal{F}}\_{t}]\leq\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\sigma}+K^{\lambda}\_{\sigma}|{\mathcal{F}}\_{t}]. |  |

Combining this inequality with the converse bound established earlier, we conclude that

|  |  |  |
| --- | --- | --- |
|  | Vtλ+Ktλ=ess​supσ∈𝒯t,T⁡𝔼​[Pσ+Kσλ|ℱt].V^{\lambda}\_{t}+K^{\lambda}\_{t}=\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\sigma}+K^{\lambda}\_{\sigma}|{\mathcal{F}}\_{t}]. |  |

By the uniqueness of the Doob–Meyer decomposition and standard results from optimal stopping theory (see, for instance, Theorem D.13 in Karatzas and Shreve [[27](https://arxiv.org/html/2602.18078v1#bib.bib27)]), we deduce that the process AλA^{\lambda} satisfies the required Skorokhod reflection condition.

*Step 3.* To establish that Mλ∈ℋ2M^{\lambda}\in\mathcal{H}^{2} and Aλ∈𝒦2A^{\lambda}\in\mathcal{K}^{2}, we follow the argument of Lemma 3.2 in Grigorova *et al.* [[23](https://arxiv.org/html/2602.18078v1#bib.bib23)], which relies on Theorem A.2 and Corollary A.1 therein. To this end, we consider the process

|  |  |  |
| --- | --- | --- |
|  | Yt:=Vtλ+Ktλ=ess​supσ∈𝒯t,T⁡𝔼​[Pσ+Kσλ|ℱt]=Mtλ−Atλ.\displaystyle Y\_{t}:=V^{\lambda}\_{t}+K^{\lambda}\_{t}=\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\sigma}+K^{\lambda}\_{\sigma}|{\mathcal{F}}\_{t}]=M^{\lambda}\_{t}-A^{\lambda}\_{t}. |  |

By Jensen’s inequality, we obtain

|  |  |  |
| --- | --- | --- |
|  | |Yt|=|ess​supσ∈𝒯t,T𝔼[Pσ+Kσλ|ℱt]|≤ess​supσ∈𝒯t,T𝔼[|Pσ+Kσλ||ℱt]≤𝔼[sup0≤t≤T|Pt|+sup0≤t≤T|Ktλ||ℱt].\displaystyle|Y\_{t}|=|\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\sigma}+K^{\lambda}\_{\sigma}|{\mathcal{F}}\_{t}]|\leq\operatornamewithlimits{ess\,sup}\_{\sigma\in\mathcal{T}\_{t,T}}\mathbb{E}[|P\_{\sigma}+K^{\lambda}\_{\sigma}||{\mathcal{F}}\_{t}]\leq\mathbb{E}[\,\sup\_{0\leq t\leq T}|P\_{t}|+\sup\_{0\leq t\leq T}|K^{\lambda}\_{t}||{\mathcal{F}}\_{t}]. |  |

We therefore define X:=sup0≤t≤T|Pt|+sup0≤t≤T|Ktλ|X:=\sup\_{0\leq t\leq T}|P\_{t}|+\sup\_{0\leq t\leq T}|K^{\lambda}\_{t}|. Under assumption [3.1](https://arxiv.org/html/2602.18078v1#S3.Thmhyp1 "Assumption 3.1. ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), by Lemma [4.6](https://arxiv.org/html/2602.18078v1#S4.Thmlem6 "Lemma 4.6. ‣ 4.1 Auxiliary Lemmas and Estimates ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") the Cauchy-Schwarz inequality, it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X2]≤C​‖P‖𝒮2+C​‖Kλ‖𝒮2<∞.\displaystyle{\mathbb{E}}[X^{2}]\leq C\|P\|\_{\mathcal{S}^{2}}+C\|K^{\lambda}\|\_{\mathcal{S}^{2}}<\infty. |  |

Applying Doob’s martingale inequality yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼[sup0≤t≤T|Yt|2]≤𝔼[sup0≤t≤T|𝔼[X|ℱt]|2]≤C𝔼[X2].\displaystyle{\mathbb{E}}[\,\sup\_{0\leq t\leq T}|Y\_{t}|^{2}]\leq{\mathbb{E}}[\,\sup\_{0\leq t\leq T}|{\mathbb{E}}[X|{\mathcal{F}}\_{t}]|^{2}]\leq C{\mathbb{E}}[X^{2}]. |  |

Next, we note that the process Yt−𝔼​[YT|ℱt]Y\_{t}-{\mathbb{E}}[Y\_{T}|{\mathcal{F}}\_{t}] coincides with the potential generated by AλA^{\lambda}, namely

|  |  |  |
| --- | --- | --- |
|  | Yt−𝔼​[YT|ℱt]=𝔼​[ATλ−Atλ|ℱt].Y\_{t}-{\mathbb{E}}[Y\_{T}|{\mathcal{F}}\_{t}]={\mathbb{E}}[A^{\lambda}\_{T}-A^{\lambda}\_{t}|{\mathcal{F}}\_{t}]. |  |

Moreover,
|𝔼[YT|ℱt]−Yt|≤𝔼[|YT||ℱt]+|Yt|≤2𝔼[X|ℱt]|{\mathbb{E}}[Y\_{T}|{\mathcal{F}}\_{t}]-Y\_{t}|\leq{\mathbb{E}}[|Y\_{T}||{\mathcal{F}}\_{t}]+|Y\_{t}|\leq 2\mathbb{E}[X|{\mathcal{F}}\_{t}]. Invoking Theorem A.2 of [[23](https://arxiv.org/html/2602.18078v1#bib.bib23)], we therefore deduce the existence of a constant c>0c>0 such that 𝔼​[|ATλ|2]≤c​𝔼​[X2]<∞{\mathbb{E}}[|A^{\lambda}\_{T}|^{2}]\leq c{\mathbb{E}}[X^{2}]<\infty which shows that Aλ∈𝒦2A^{\lambda}\in\mathcal{K}^{2}. Finally, since Vλ,Kλ∈𝒮2V^{\lambda},K^{\lambda}\in\mathcal{S}^{2} and Aλ∈𝒦2A^{\lambda}\in\mathcal{K}^{2}, it follows directly that the martingale component MλM^{\lambda} belongs to ℋ2\mathcal{H}^{2}.
∎

### 4.4 Probabilistic Interpretation

In this subsection, we provide a probabilistic/financial interpretation of the singular reflected BSDE identified in equation ([4](https://arxiv.org/html/2602.18078v1#S4.Ex1 "4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")). In particular, we interpret the
value process VλV^{\lambda} as the price of an American-style claim subject to default risk, where the default mechanism is endogenously generated by the entropy-regularized penalization scheme.

More precisely, we consider the unique solution to the singular RBSDE

|  |  |  |
| --- | --- | --- |
|  | Vtλ=PT−(MTλ−Mtλ)+∫tTλ​ln⁡(λVsλ−Ps)​𝑑s+ATλ−Atλ,\displaystyle V^{\lambda}\_{t}=P\_{T}-(M^{\lambda}\_{T}-M^{\lambda}\_{t})+\int^{T}\_{t}\lambda\ln\!\left(\frac{\lambda}{V^{\lambda}\_{s}-P\_{s}}\right)ds+A^{\lambda}\_{T}-A^{\lambda}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ≥Ptand∫0T(Vsλ−Ps)​𝑑Asλ=0,\displaystyle V^{\lambda}\_{t}\geq P\_{t}\quad\text{and}\quad\int^{T}\_{0}(V^{\lambda}\_{s}-P\_{s})\,dA^{\lambda}\_{s}=0, |  | (4.35) |

which was shown in Subsection [4.3](https://arxiv.org/html/2602.18078v1#S4.SS3 "4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") to admit a unique solution under Assumption [4.1](https://arxiv.org/html/2602.18078v1#S4.Thmhyp1 "Assumption 4.1. ‣ 4.3 Reflected BSDE with a Singular Driver ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"). We show in Theorem [4.3](https://arxiv.org/html/2602.18078v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.4 Probabilistic Interpretation ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") that the solution VλV^{\lambda} admits an optimal stopping representation involving an endogenous default time, and that the singular driver encodes the trade-off between continuation, early exercise, and default.
To this end, we introduce an endogenous default intensity process γλ\gamma^{\lambda} defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | γsλ:=λPs+λ−Vsλ​ln⁡(λVsλ−Ps)andΓtλ:=∫0tγsλ​𝑑s.\displaystyle\gamma^{\lambda}\_{s}:=\frac{\lambda}{P\_{s}+\lambda-V^{\lambda}\_{s}}\ln\left(\frac{\lambda}{V^{\lambda}\_{s}-P\_{s}}\right)\quad\mathrm{and}\quad\Gamma^{\lambda}\_{t}:=\int^{t}\_{0}\gamma^{\lambda}\_{s}ds. |  | (4.36) |

The process γλ\gamma^{\lambda} is strictly positive and therefore defines a valid default intensity. Moreover, it explodes whenever VλV^{\lambda} approaches the payoff process PP, reflecting an imminent default when the continuation value is close to pay-off. Indeed, we have for all x≥0x\geq 0,

|  |  |  |
| --- | --- | --- |
|  | λλ−x​ln⁡(λx)>0,\displaystyle\frac{\lambda}{\lambda-x}\ln\left(\frac{\lambda}{x}\right)>0, |  |

and we have γsλ↑∞\gamma^{\lambda}\_{s}\uparrow\infty as Vsλ↓PsV^{\lambda}\_{s}\downarrow P\_{s}.

Following the standard intensity-based approach in credit risk modelling, for any t∈[0,T]t\in[0,T], we define a default time σtλ\sigma^{\lambda}\_{t} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σtλ\displaystyle\sigma^{\lambda}\_{t} | :=inf{s≥t:1−e−(Γsλ−Γtλ)≥U},\displaystyle:=\inf\{s\geq t:1-e^{-(\Gamma^{\lambda}\_{s}-\Gamma^{\lambda}\_{t})}\geq U\}, |  | (4.37) |

where UU is a uniform random variable on [0,1][0,1] independent of ℱ∞\mathcal{F}\_{\infty}. By construction, σtλ\sigma^{\lambda}\_{t} is a Cox (doubly stochastic) default time with 𝔽\mathbb{F}-intensity γλ\gamma^{\lambda}. In particular, for any u≥tu\geq t, it satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(σtλ>u|ℱ∞)=ℙ​(σtλ>u|ℱu)=e−(Γuλ−Γtλ),\displaystyle\mathbb{P}(\sigma^{\lambda}\_{t}>u\,|\,\mathcal{F}\_{\infty})=\mathbb{P}(\sigma^{\lambda}\_{t}>u\,|\,\mathcal{F}\_{u})=e^{-(\Gamma^{\lambda}\_{u}-\Gamma^{\lambda}\_{t})}, |  | (4.38) |

highlighting the structural link between default risk and early exercise incentives.

###### Theorem 4.3.

The value process VλV^{\lambda} admits the representation for each t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ=ess​supτt∈𝒯t,T⁡𝔼​[Pτt​𝟙{σtλ>τt}+(Pσtλ+λ)​ 1{σtλ≤τt}|ℱt].V\_{t}^{\lambda}=\operatornamewithlimits{ess\,sup}\_{\tau\_{t}\in\mathcal{T}\_{t,T}}\mathbb{E}\Big[P\_{\tau\_{t}}\mathds{1}\_{\{\sigma\_{t}^{\lambda}>\tau\_{t}\}}+(P\_{\sigma\_{t}^{\lambda}}+\lambda)\,\mathds{1}\_{\{\sigma\_{t}^{\lambda}\leq\tau\_{t}\}}\;\Big|\;\mathcal{F}\_{t}\Big]. |  | (4.39) |

Consequently, VλV^{\lambda} is the value of a defaultable American option with exercise payoff PP and recovery payoff P+λP+\lambda, where default occurs at the Cox time σtλ\sigma^{\lambda}\_{t} with intensity γλ\gamma^{\lambda}.

###### Proof.

In view of the preceding discussion, the backward dynamics of VλV^{\lambda} can be written as

|  |  |  |
| --- | --- | --- |
|  | Vtλ=PT+∫tT(Ps+λ−Vsλ)​γsλ​𝑑s−(MTλ−Mtλ)+ATλ−Atλ.\displaystyle V\_{t}^{\lambda}=P\_{T}+\int^{T}\_{t}(P\_{s}+\lambda-V\_{s}^{\lambda})\gamma^{\lambda}\_{s}\,ds-(M^{\lambda}\_{T}-M^{\lambda}\_{t})+A^{\lambda}\_{T}-A^{\lambda}\_{t}. |  |

Applying Itô’s formula to the process e−Γsλ​Vsλe^{-\Gamma^{\lambda}\_{s}}V^{\lambda}\_{s}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(e−Γsλ​Vsλ)\displaystyle d(e^{-\Gamma\_{s}^{\lambda}}V^{\lambda}\_{s}) | =−e−Γsλ​(Ps+λ)​γsλ​d​s+e−Γsλ​d​Msλ−e−Γsλ​d​Asλ.\displaystyle=-e^{-\Gamma\_{s}^{\lambda}}(P\_{s}+\lambda)\gamma\_{s}^{\lambda}ds+e^{-\Gamma\_{s}^{\lambda}}dM^{\lambda}\_{s}-e^{-\Gamma\_{s}^{\lambda}}dA^{\lambda}\_{s}. |  |

Define the stopping time τt∗:=inf{s≥t:Vsλ=Ps}\tau^{\*}\_{t}:=\inf\{s\geq t:V^{\lambda}\_{s}=P\_{s}\}. Integrating the above dynamics backward from tt to τt∗\tau^{\*}\_{t} and taking conditional expectations yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−Γtλ​Vtλ\displaystyle e^{-\Gamma\_{t}^{\lambda}}V^{\lambda}\_{t} | =𝔼​[Pτt∗​e−Γτt∗λ+∫tτt∗e−Γsλ​(Ps+λ)​γsλ​𝑑s+∫tτt∗e−Γsλ​𝑑Asλ∣ℱt]\displaystyle=\mathbb{E}[P\_{\tau^{\*}\_{t}}e^{-\Gamma\_{\tau^{\*}\_{t}}^{\lambda}}+\int^{\tau^{\*}\_{t}}\_{t}e^{-\Gamma\_{s}^{\lambda}}(P\_{s}+\lambda)\gamma\_{s}^{\lambda}ds+\int^{\tau^{\*}\_{t}}\_{t}e^{-\Gamma\_{s}^{\lambda}}dA^{\lambda}\_{s}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[Pτt∗​e−Γτt∗λ+∫tτt∗e−Γsλ​(Ps+λ)​γsλ​𝑑s∣ℱt].\displaystyle=\mathbb{E}[P\_{\tau^{\*}\_{t}}e^{-\Gamma\_{\tau^{\*}\_{t}}^{\lambda}}+\int^{\tau^{\*}\_{t}}\_{t}e^{-\Gamma\_{s}^{\lambda}}(P\_{s}+\lambda)\gamma\_{s}^{\lambda}ds\mid\mathcal{F}\_{t}]. |  |

where we used the fact that the reflection process AλA^{\lambda} does not increase on [t,τt∗][t,\tau^{\*}\_{t}]. Using the conditional survival probability ([4.38](https://arxiv.org/html/2602.18078v1#S4.E38 "In 4.4 Probabilistic Interpretation ‣ 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ\displaystyle V^{\lambda}\_{t} | ≤ess​supτt∈𝒯t,T⁡𝔼​[Pτt​e−(Γτtλ−Γtλ)+∫tτt(Ps+λ)​γsλ​e−(Γsλ−Γtλ)​𝑑s|ℱt]\displaystyle\leq\operatornamewithlimits{ess\,sup}\_{\tau\_{t}\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\tau\_{t}}e^{-(\Gamma\_{\tau\_{t}}^{\lambda}-\Gamma\_{t}^{\lambda})}+\int^{\tau\_{t}}\_{t}(P\_{s}+\lambda)\gamma\_{s}^{\lambda}e^{-(\Gamma\_{s}^{\lambda}-\Gamma\_{t}^{\lambda})}ds|\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ess​supτt∈𝒯t,T⁡𝔼​[Pτt​𝟙{σtλ>τt}+𝟙{σtλ≤τt}​(Pσtλ+λ)|ℱt]\displaystyle=\operatornamewithlimits{ess\,sup}\_{\tau\_{t}\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\tau\_{t}}\mathds{1}\_{\{\sigma^{\lambda}\_{t}>\tau\_{t}\}}+\mathds{1}\_{\{\sigma^{\lambda}\_{t}\leq\tau\_{t}\}}(P\_{\sigma^{\lambda}\_{t}}+\lambda)|\mathcal{F}\_{t}] |  |

To prove the reverse inequality, let τt≥t\tau\_{t}\geq t be an arbitrary 𝔽\mathbb{F}-stopping time. Repeating the above computation up to τt\tau\_{t} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−Γtλ​Vtλ\displaystyle e^{-\Gamma\_{t}^{\lambda}}V^{\lambda}\_{t} | =𝔼​[Vτt​e−Γτtλ+∫tτte−Γsλ​(Ps+λ)​γsλ​𝑑s+∫tτte−Γsλ​𝑑Asλ∣ℱt]\displaystyle=\mathbb{E}[V\_{\tau\_{t}}e^{-\Gamma\_{\tau\_{t}}^{\lambda}}+\int^{\tau\_{t}}\_{t}e^{-\Gamma\_{s}^{\lambda}}(P\_{s}+\lambda)\gamma\_{s}^{\lambda}ds+\int^{\tau\_{t}}\_{t}e^{-\Gamma\_{s}^{\lambda}}dA^{\lambda}\_{s}\mid\mathcal{F}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝔼​[Pτt​e−Γτtλ+∫tτte−Γsλ​(Ps+λ)​γsλ​𝑑s∣ℱt].\displaystyle\geq\mathbb{E}[P\_{\tau\_{t}}e^{-\Gamma\_{\tau\_{t}}^{\lambda}}+\int^{\tau\_{t}}\_{t}e^{-\Gamma\_{s}^{\lambda}}(P\_{s}+\lambda)\gamma\_{s}^{\lambda}ds\mid\mathcal{F}\_{t}]. |  |

where we have used the fact that AλA^{\lambda} is increasing and P≤VλP\leq V^{\lambda}. Combining the above computations, we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ\displaystyle V^{\lambda}\_{t} | =ess​supτt∈𝒯t,T⁡𝔼​[Pτt​𝟙{σtλ>τt}+𝟙{σtλ≤τt}​(Pσtλ+λ)|ℱt].\displaystyle=\operatornamewithlimits{ess\,sup}\_{\tau\_{t}\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\tau\_{t}}\mathds{1}\_{\{\sigma^{\lambda}\_{t}>\tau\_{t}\}}+\mathds{1}\_{\{\sigma^{\lambda}\_{t}\leq\tau\_{t}\}}(P\_{\sigma^{\lambda}\_{t}}+\lambda)|\mathcal{F}\_{t}]. |  |

∎

###### Remark 4.4.

The above representation shows that VλV^{\lambda} admits a natural interpretation as the value of a defaultable American option with exercise payoff PP and recovery payoff P+λP+\lambda. Moreover, as λ↓0\lambda\downarrow 0, the intensity process γλ\gamma^{\lambda} converges to zero, implying that the default time σtλ\sigma^{\lambda}\_{t} diverges to infinity. In this limit, the default risk vanishes and the value process VλV^{\lambda} converges to that of a standard American option with payoff process PP.

## 5 Numerical Experiments

In this section, we illustrate the practical feasibility of our methodology on a simple low-dimensional example with d=2d=2.
We consider the symmetric case of an American max-call option.
Specifically, the underlying assets are assumed to follow a dd-dimensional Black–Scholes model with dividends,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sti=S0i​exp⁡((r−δ−σ2/2)​t+σ​Wti),i=1,…,d,S\_{t}^{i}=S\_{0}^{i}\exp\big((r-\delta-\sigma^{2}/2)t+\sigma W\_{t}^{i}\big),\quad i=1,\dots,d, |  | (5.1) |

where S0iS\_{0}^{i} denotes the initial asset prices, rr the risk-free interest rate, δ\delta the constant dividend yield, σ\sigma the volatility parameter, and
W=(W1,…,Wd)W=(W^{1},\dots,W^{d}) a standard dd-dimensional Brownian motion.
Given a strike price KK, the value of the American max-call option is

|  |  |  |
| --- | --- | --- |
|  | supτ∈𝒯0,T𝔼​[e−r​τ​(max1≤i≤d⁡Sτi−K)+].\sup\_{\tau\in\mathcal{T}\_{0,T}}\mathbb{E}\!\left[e^{-r\tau}\Big(\max\_{1\leq i\leq d}S\_{\tau}^{i}-K\Big)^{+}\right]. |  |

Throughout the numerical experiment, we fix the parameters

|  |  |  |
| --- | --- | --- |
|  | S01=S02=S0,K=50,r=0.05,σ=0.2,δ=0.1,T=3.S\_{0}^{1}=S\_{0}^{2}=S\_{0},\quad K=50,\quad r=0.05,\quad\sigma=0.2,\quad\delta=0.1,\quad T=3. |  |

We discretise the time interval [0,T][0,T] using the uniform time grid tk=k​Δ​tt\_{k}=k\Delta t, k=0,⋯,Nk=0,\cdots,N, with mesh size Δ​t=T/N\Delta t=T/N. We fix N=100N=100 in our numerical experiments. We compare the prices obtained from the classical penalisation scheme ([3.2](https://arxiv.org/html/2602.18078v1#S3.E2 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), the entropy-regularised penalised BSDE ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), and the PIA defined in ([3.12](https://arxiv.org/html/2602.18078v1#S3.E12 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"))-([3.13](https://arxiv.org/html/2602.18078v1#S3.E13 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), against a binomial tree benchmark. We note that the BSDE formulations introduced above do not explicitly include discounting. Applying Itô’s formula to the randomized stopping representation ([1.2](https://arxiv.org/html/2602.18078v1#S1.E2 "In 1 Introduction ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) shows that discounting by a constant rate rr corresponds to adding a −r​V-rV term to the driver (this term is included in the implementations of ([3.2](https://arxiv.org/html/2602.18078v1#S3.E2 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")), ([3.8](https://arxiv.org/html/2602.18078v1#S3.E8 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and ([3.13](https://arxiv.org/html/2602.18078v1#S3.E13 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"))).

For numerical stability, we employ the following approximations for the functions Φ\Phi and μ​(α,n)\mu(\alpha,n) (recalling ([3.15](https://arxiv.org/html/2602.18078v1#S3.E15 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"))):

|  |  |  |
| --- | --- | --- |
|  | Φ​(x)={x+ln⁡(1−e−x)−ln⁡(x),x>10−9,ln⁡(ex−1x),x<−10−9,x2,|x|≤10−9.μ​(α,n)={n2+α​n212,if ​|α|<10−6,n−1α,if −α​n<−700,0,if −α​n>700,n1−e−α​n−1α,otherwise.\Phi(x)=\begin{cases}x+\ln(1-e^{-x})-\ln(x),&x>10^{-9},\\ \ln\!\left(\frac{e^{x}-1}{x}\right),&x<-10^{-9},\\ \frac{x}{2},&|x|\leq 10^{-9}.\end{cases}\qquad\mu(\alpha,n)=\begin{cases}\dfrac{n}{2}+\dfrac{\alpha n^{2}}{12},&\text{if }|\alpha|<10^{-6},\\ n-\dfrac{1}{\alpha},&\text{if }-\alpha n<-700,\\ 0,&\text{if }-\alpha n>700,\\ \dfrac{n}{1-e^{-\alpha n}}-\dfrac{1}{\alpha},&\text{otherwise}.\end{cases} |  |

### 5.1 Implicit BSDE Solver

We first consider the entropy-regularised penalisation scheme for the American max-call option,

|  |  |  |
| --- | --- | --- |
|  | Vtλ,n=PT−∫tT𝑑Msλ,n+∫tTn​[λn​Φ​(Ps−Vsλ,nλ/n)+λn​ln⁡(n)]−r​Vsλ,n​d​s.V^{\lambda,n}\_{t}=P\_{T}-\int^{T}\_{t}dM^{\lambda,n}\_{s}+\int^{T}\_{t}n\left[\frac{\lambda}{n}\Phi\left(\frac{P\_{s}-V^{\lambda,n}\_{s}}{\lambda/n}\right)+\frac{\lambda}{n}\ln(n)\right]-rV\_{s}^{\lambda,n}ds. |  |

For d=2d=2, this BSDE can be efficiently approximated using a least-squares regression combined with an implicit time-stepping scheme, commonly referred to as the
θ\theta-scheme; see, for instance, Lionnet *et al.* [[31](https://arxiv.org/html/2602.18078v1#bib.bib31)].
We consider the following approximation scheme

|  |  |  |
| --- | --- | --- |
|  | V¯tkλ,n=11+r​Δ​t​𝔼​[V¯tk+1λ,n|ℱtk]+Δ​t1+r​Δ​t​[λn​Φ​(Ptk−V¯tkλ,nλ/n)+λn​ln⁡(n)],k=N−1,⋯,0,\bar{V}\_{t\_{k}}^{\lambda,n}=\frac{1}{1+r\Delta t}{\mathbb{E}}[\bar{V}\_{t\_{k+1}}^{\lambda,n}|{\mathcal{F}}\_{t\_{k}}]+\frac{\Delta t}{1+r\Delta t}\left[\frac{\lambda}{n}\Phi\left(\frac{P\_{t\_{k}}-\bar{V}^{\lambda,n}\_{t\_{k}}}{\lambda/n}\right)+\frac{\lambda}{n}\ln(n)\right],\quad k=N-1,\cdots,0, |  |

with V¯Tλ,n=PT\bar{V}\_{T}^{\lambda,n}=P\_{T} and iterate backward in time. The conditional expectation is approximated via least-squares regression, after which the resulting nonlinear equation in V¯tkλ,n\bar{V}^{\lambda,n}\_{t\_{k}} is solved using Newton’s method.

### 5.2 Numerical Implementation of the PIA

We initialize the PIA with 𝒱λ,0=P0+1\mathscr{V}^{\lambda,0}=P\_{0}+1, to ensure that the initial value is strictly positive.
Given 𝒱λ,m\mathscr{V}^{\lambda,m}, the next iterate 𝒱λ,m+1\mathscr{V}^{\lambda,m+1} satisfies the linear BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱tλ,m+1\displaystyle\mathscr{V}^{\lambda,m+1}\_{t} | =PT−(𝒩Tλ,m+1−𝒩tλ,m+1)+∫tT{G​(s,𝒱sλ,m+1,πsm+1)−r​𝒱sλ,m+1}​𝑑s,\displaystyle=P\_{T}-(\mathscr{N}^{\lambda,m+1}\_{T}-\mathscr{N}^{\lambda,m+1}\_{t})+\int^{T}\_{t}\left\{G(s,\mathscr{V}^{\lambda,m+1}\_{s},\pi^{m+1}\_{s})-r\mathscr{V}^{\lambda,m+1}\_{s}\right\}\,ds, |  |

where GG is defined in ([3.14](https://arxiv.org/html/2602.18078v1#S3.E14 "In 3.2 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")).
By Theorem 3.3 in [[36](https://arxiv.org/html/2602.18078v1#bib.bib36)], this BSDE admits the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱tλ,m+1\displaystyle\mathscr{V}^{\lambda,m+1}\_{t} | =𝔼​[e−∫tTaum​𝑑u​PT+∫tTe−∫tsaum​𝑑u​bsm​𝑑s|ℱt]\displaystyle=\mathbb{E}\Big[e^{-\int\_{t}^{T}a^{m}\_{u}\,du}\,P\_{T}+\int\_{t}^{T}e^{-\int\_{t}^{s}a^{m}\_{u}\,du}\,b^{m}\_{s}ds\Big|\mathcal{F}\_{t}\Big] |  |

so that

|  |  |  |
| --- | --- | --- |
|  | 𝒱tkλ,m+1=𝔼​[e−∫tktk+1asm​𝑑s​𝒱tk+1λ,m+1+∫tktk+1e−∫tksaum​𝑑u​bsm​𝑑s|ℱtk],k=0,⋯,N−1.\mathscr{V}^{\lambda,m+1}\_{t\_{k}}=\mathbb{E}\Big[e^{-\int^{t\_{k+1}}\_{t\_{k}}a^{m}\_{s}ds}\mathscr{V}^{\lambda,m+1}\_{t\_{k+1}}+\int\_{t\_{k}}^{t\_{k+1}}e^{-\int\_{t\_{k}}^{s}a^{m}\_{u}\,du}\,b^{m}\_{s}\,ds\,\Big|\,\mathcal{F}\_{t\_{k}}\Big],\quad k=0,\cdots,N-1. |  |

We thus consider the approximation scheme

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱^tkλ,m+1\displaystyle\widehat{\mathscr{V}}\_{t\_{k}}^{\lambda,m+1} | =e−atkm​Δ​t​𝔼​[𝒱^tk+1λ,m+1|ℱtk]+btkmatkm​(1−e−atkm​Δ​t),k=N−1,⋯,0.\displaystyle=e^{-a\_{t\_{k}}^{m}\Delta t}{\mathbb{E}}\left[\widehat{\mathscr{V}}^{\lambda,m+1}\_{t\_{k+1}}\Big|{\mathcal{F}}\_{t\_{k}}\right]+\frac{b^{m}\_{t\_{k}}}{a^{m}\_{t\_{k}}}(1-e^{-a^{m}\_{t\_{k}}\Delta t}),\quad k=N-1,\cdots,0. |  | (5.2) |

where

|  |  |  |
| --- | --- | --- |
|  | atkm=μπtkm+1+randbtkm=λ​Φ​(Ptk−𝒱tkλ,mλ/n)+λ​ln⁡(n)+𝒱tkλ,m​(atkm−r).\displaystyle a^{m}\_{t\_{k}}=\mu\_{\pi^{m+1}\_{t\_{k}}}+r\qquad\text{and}\qquad b^{m}\_{t\_{k}}=\lambda\Phi\!\Big(\frac{P\_{t\_{k}}-\mathscr{V}^{\lambda,m}\_{t\_{k}}}{\lambda/n}\Big)+\lambda\ln(n)+\mathscr{V}^{\lambda,m}\_{t\_{k}}(a^{m}\_{t\_{k}}-r). |  |

The conditional mean μπtkm+1\mu\_{\pi^{m+1}\_{t\_{k}}} admits the explicit expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | μπtkm+1=μ(αtkm,n):=n1−e−αtkm​n−1αtkmwhereαtkm=Ptk−𝒱^tkλ,mλ.\mu\_{\pi^{m+1}\_{t\_{k}}}=\mu(\alpha\_{t\_{k}}^{m},n):=\frac{n}{1-e^{-\alpha\_{t\_{k}}^{m}n}}-\frac{1}{\alpha\_{t\_{k}}^{m}}\quad\mathrm{where}\quad\alpha\_{t\_{k}}^{m}=\frac{P\_{t\_{k}}-\widehat{\mathscr{V}}^{\lambda,m}\_{t\_{k}}}{\lambda}. |  | (5.3) |

Therefore, each policy update reduces to a regression step, which is iterated backwards in time for each mm. Finally, all methods require the estimation of conditional expectations.
We employ a least-squares regression based on the 13 basis functions proposed by Andersen and Broadie [[1](https://arxiv.org/html/2602.18078v1#bib.bib1)].

We report in Table [1](https://arxiv.org/html/2602.18078v1#S5.T1 "Table 1 ‣ 5.2 Numerical Implementation of the PIA ‣ 5 Numerical Experiments ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators") the numerical prices obtained for the American max-call option using the entropy-regularised implicit BSDE solver and the PIA.
For comparison, we also include the results obtained from the classical penalisation approach of El Karoui *et al.* [[19](https://arxiv.org/html/2602.18078v1#bib.bib19)] and a binomial tree approximation, which serves as a benchmark.
All entropy-based methods are implemented with temperature parameter λ=1/n\lambda=1/n, and prices are reported for several values of the initial asset price S0S\_{0} and truncation level nn.

| S0S\_{0} | nn | Implicit solver | PIA | Classical penalization | Binomial |
| --- | --- | --- | --- | --- | --- |
| 90 | 10 | 7.388 | 7.463 | 8.208 | 8.296 |
| 90 | 100 | 8.150 | 8.231 | 8.424 | 8.296 |
| 90 | 1000 | 8.285 | 8.367 | 8.460 | 8.296 |
| 100 | 10 | 13.246 | 13.349 | 14.040 | 14.211 |
| 100 | 100 | 14.086 | 14.213 | 14.357 | 14.211 |
| 100 | 1000 | 14.227 | 14.350 | 14.408 | 14.211 |
| 110 | 10 | 20.821 | 20.926 | 21.494 | 21.799 |
| 110 | 100 | 21.678 | 21.814 | 21.914 | 21.799 |
| 110 | 1000 | 21.815 | 21.926 | 21.980 | 21.799 |

Table 1: Results for American max-call option using implicit solver and policy improvement compared to classical penalization and binomial tree. The temperature parameter is set as λ=1/n\lambda=1/n. The implicit solver uses 20 steps of Newton iterations and the PIA is computed over 10 iterations.

Several observations can be drawn from Table [1](https://arxiv.org/html/2602.18078v1#S5.T1 "Table 1 ‣ 5.2 Numerical Implementation of the PIA ‣ 5 Numerical Experiments ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators").
First, the entropy-regularized method computed using the implicit solver and the PIA yield prices that converge monotonically as nn increases and consistently approach the binomial benchmark.
In contrast, the classical penalization scheme (computed using the implicit solver) exhibits a noticeably slower convergence and tends to overestimate the option value.

Second, the PIA produces prices that are systematically (slightly) higher than those obtained from the implicit solver. This behaviour is consistent with the theoretical interpretation of the PIA, which generates an increasing sequence of approximations converging to the entropy-regularized value function.

Finally, even for moderate values of nn, both entropy-based approaches deliver accurate approximations of the benchmark prices, thereby illustrating the practical efficiency and numerical stability of the proposed methodology.

## 6 Appendix

###### Lemma 6.1.

The function x↦Ψ​(x)x\mapsto\Psi(x) defined in ([3.6](https://arxiv.org/html/2602.18078v1#S3.E6 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) is a cumulative distribution function on ℝ\mathbb{R}.

###### Proof.

We first note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→∞Ψ​(x)\displaystyle\lim\_{x\to\infty}\Psi(x) | =limx→∞1x​ln⁡(ex−1x)=1,\displaystyle=\lim\_{x\to\infty}\frac{1}{x}\ln\!\left(\frac{e^{x}-1}{x}\right)=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→−∞Ψ​(x)\displaystyle\lim\_{x\to-\infty}\Psi(x) | =limx→−∞1x​ln⁡(ex−1x)=0.\displaystyle=\lim\_{x\to-\infty}\frac{1}{x}\ln\!\left(\frac{e^{x}-1}{x}\right)=0. |  |

It therefore remains to show that Ψ\Psi is non-decreasing, or equivalently that Ψ′​(x)≥0\Psi^{\prime}(x)\geq 0 for all x∈ℝx\in\mathbb{R}.

To this end, we rewrite Ψ\Psi as

|  |  |  |
| --- | --- | --- |
|  | Ψ​(x)=ln⁡(sinh⁡(x/2)x/2​e−x/2)=ln⁡(sinh⁡(x2))−ln⁡(x2)+x2.\displaystyle\Psi(x)=\ln\left(\frac{\sinh(x/2)}{x/2e^{-x/2}}\right)=\ln(\sinh(\frac{x}{2}))-\ln(\frac{x}{2})+\frac{x}{2}. |  |

Setting z:=x/2z:=x/2, it suffices to verify that

|  |  |  |
| --- | --- | --- |
|  | ∂z(ln⁡(sinh⁡(z))−ln⁡(z)+z)=coth⁡(z)−1/z+1≥0.\displaystyle\partial\_{z}(\ln(\sinh(z))-\ln(z)+z)=\coth(z)-1/z+1\geq 0. |  |

For z>1z>1, the inequality is immediate. To treat the general case, we use the identity

|  |  |  |
| --- | --- | --- |
|  | coth⁡(z)=1+1z​2​ze2​z−1\displaystyle\coth(z)=1+\frac{1}{z}\frac{2z}{e^{2z}-1} |  |

which shows that the above inequality is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 2+1z​2​ze2​z−1−1z≥0⟺2​z+2​ze2​z−1>1\displaystyle 2+\frac{1}{z}\frac{2z}{e^{2z}-1}-\frac{1}{z}\geq 0\Longleftrightarrow 2z+\frac{2z}{e^{2z}-1}>1 |  |

For x=2​z≥0x=2z\geq 0, the mean value theorem implies the existence of x∗∈[0,x]x\_{\*}\in[0,x] such that ex−1=ex∗​xe^{x}-1=e^{x\_{\*}}x and therefore x​ex≥ex−1=ex∗​xxe^{x}\geq e^{x}-1=e^{x\_{\*}}x. This establishes the inequality for x≥0x\geq 0.

If x<0x<0, the required inequality is equivalent to

|  |  |  |
| --- | --- | --- |
|  | −|x|+|x|1−e−|x|<1⟺|x|​e−|x|≤1−e−|x|\displaystyle-|x|+\frac{|x|}{1-e^{-|x|}}<1\Longleftrightarrow|x|e^{-|x|}\leq 1-e^{-|x|} |  |

which again follows from the mean value theorem and the monotonicity of the exponential function. Combining the above arguments shows that Ψ′​(x)≥0\Psi^{\prime}(x)\geq 0 for all x∈ℝx\in\mathbb{R}, completing the proof.
∎

###### Lemma 6.2.

The function Φ\Phi defined in ([3.6](https://arxiv.org/html/2602.18078v1#S3.E6 "In 3 Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) satisfies the properties that 0≤Φ′​(x)≤10\leq\Phi^{\prime}(x)\leq 1. In particular, Φ\Phi is Lipschitz continuous with Lipschitz constant 11.

###### Proof.

For x≠0x\neq 0, direct differentiation yields

|  |  |  |
| --- | --- | --- |
|  | Φ′​(x)=x​ex−(ex−1)x​(ex−1),and Φ′′​(x)=e2​x−(2+x2)​ex+1x2​(ex−1)2.\displaystyle\Phi^{\prime}(x)=\frac{xe^{x}-(e^{x}-1)}{x(e^{x}-1)},\quad\text{and }\quad\Phi^{\prime\prime}(x)=\frac{e^{2x}-(2+x^{2})e^{x}+1}{x^{2}(e^{x}-1)^{2}}. |  |

Moreover, a direct computation shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→+∞Φ′​(x)\displaystyle\lim\_{x\rightarrow+\infty}\Phi^{\prime}(x) | =limx→∞1−(x−1−(x​ex)−1)(1−e−x)=1,\displaystyle=\lim\_{x\rightarrow\infty}\frac{1-(x^{-1}-(xe^{x})^{-1})}{(1-e^{-x})}=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→−∞Φ′​(x)\displaystyle\lim\_{x\rightarrow-\infty}\Phi^{\prime}(x) | =lim|x|→∞e−|x|−(|x|−1​e−|x|−|x|−1)(e−|x|−1)=0.\displaystyle=\lim\_{|x|\rightarrow\infty}\frac{e^{-|x|}-(|x|^{-1}e^{-|x|}-|x|^{-1})}{(e^{-|x|}-1)}=0. |  |

Using the classical inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ex+e−x2=cosh⁡(x)≥1+x22∀x∈ℝ,\frac{e^{x}+e^{-x}}{2}=\cosh(x)\geq 1+\frac{x^{2}}{2}\quad\forall x\in{\mathbb{R}}, |  | (6.1) |

with equality if and only if x=0x=0, we obtain e2​x−(2+x2)​ex+1≥0e^{2x}-(2+x^{2})e^{x}+1\geq 0 and therefore Φ′′​(x)≥0\Phi^{\prime\prime}(x)\geq 0 for all x≠0x\neq 0. Hence Φ′\Phi^{\prime} is non-decreasing on ℝ∖{0}\mathbb{R}\setminus\{0\}. By monotonicity, it follows that 0≤Φ′​(x)≤10\leq\Phi^{\prime}(x)\leq 1 for all x≠0x\neq 0.
Finally, an application of l’Hôpital’s rule yields Φ′​(0)=12\Phi^{\prime}(0)=\tfrac{1}{2}, which completes the proof.
∎

The proof of the following result follows similar lines of reasoning as the previous one and is thus omitted.

###### Lemma 6.3.

The function Φn\Phi\_{n} defined in ([4.1](https://arxiv.org/html/2602.18078v1#S4.E1 "In 4 Limit of the Entropy-Regularized Penalization Scheme ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) satisfies the property that 0≤Φn′​(x)≤n0\leq\Phi^{\prime}\_{n}(x)\leq n and for any xx it is monotonically increasing in nn.

We observe that the function Φ​(x)=x​Ψ​(x)\Phi(x)=x\Psi(x) is non-positive for x<0x<0 and for x≥0x\geq 0 we have Φ​(x)≤x\Phi(x)\leq x since Ψ​(x)\Psi(x) is a CDF on ℝ\mathbb{R}. This implies that for any constant c>0c>0 we have

|  |  |  |
| --- | --- | --- |
|  | c​Φ​(x/c)≤x+\displaystyle c\Phi(x/c)\leq x^{+} |  |

###### Lemma 6.4.

For any ε∈(0,1)\varepsilon\in(0,1) and c>0c>0, the following inequality holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤x+−c​Φ​(x/c)≤ε−c​ln⁡(1−e−ε/c)+c​[ln⁡|x|]+−c​ln⁡c.0\leq x^{+}-c\,\Phi(x/c)\leq\varepsilon-c\ln\!\bigl(1-e^{-\varepsilon/c}\bigr)+c[\ln|x|]^{+}-c\ln c. |  | (6.2) |

###### Proof.

For notational convenience, set x′:=x/cx^{\prime}:=x/c. By definition of Φ\Phi, we immediately obtain

|  |  |  |
| --- | --- | --- |
|  | 0≤c​((x′)+−Φ​(x′))=x+−c​Φ​(x/c).0\leq c\bigl((x^{\prime})^{+}-\Phi(x^{\prime})\bigr)=x^{+}-c\,\Phi(x/c). |  |

We first consider the case x≥0x\geq 0.
If x>εx>\varepsilon (with ε<1\varepsilon<1), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | x′−Φ​(x′)\displaystyle x^{\prime}-\Phi(x^{\prime}) | =x′−ln⁡(ex′−1)+ln⁡x′\displaystyle=x^{\prime}-\ln(e^{x^{\prime}}-1)+\ln x^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−ln⁡(1−e−x′)+ln⁡x′\displaystyle=-\ln\bigl(1-e^{-x^{\prime}}\bigr)+\ln x^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−ln⁡(1−e−ε/c)+ln⁡x−ln⁡c\displaystyle\leq-\ln\bigl(1-e^{-\varepsilon/c}\bigr)+\ln x-\ln c |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−ln⁡(1−e−ε/c)+[ln⁡x]+−ln⁡c.\displaystyle\leq-\ln\bigl(1-e^{-\varepsilon/c}\bigr)+[\ln x]^{+}-\ln c. |  |

If 0≤x≤ε0\leq x\leq\varepsilon, we use that Φ​(0)=0\Phi(0)=0 and that Φ′\Phi^{\prime} is bounded. By the mean value theorem, there exists x∗∈[0,x/c]x\_{\*}\in[0,x/c] such that

|  |  |  |
| --- | --- | --- |
|  | Φ​(x′)=Φ′​(x∗)​xc,\Phi(x^{\prime})=\Phi^{\prime}(x\_{\*})\,\frac{x}{c}, |  |

which, by Lemma [6.2](https://arxiv.org/html/2602.18078v1#S6.Thmlem2 "Lemma 6.2. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators"), implies c​(x′−Φ​(x′))≤εc(x^{\prime}-\Phi(x^{\prime}))\leq\varepsilon.

We now turn to the case x<0x<0. Writing

|  |  |  |
| --- | --- | --- |
|  | Φ​(x)=ln⁡(ex−1x)=ln⁡(1−e−|x||x|)\displaystyle\Phi(x)=\ln\left(\frac{e^{x}-1}{x}\right)=\ln\left(\frac{1-e^{-|x|}}{|x|}\right) |  |

and proceeding as in the non-negative case, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<c​[−Φ​(x/c)]\displaystyle 0<c\left[-\Phi(x/c)\right] | ≤ε−c​ln⁡(1−e−ε/c)+c​[ln⁡(|x|)]+−c​ln⁡(c).\displaystyle\leq\varepsilon-c\ln(1-e^{-\varepsilon/c})+c[\ln(|x|)]^{+}-c\ln(c). |  |

Combining all cases yields ([6.2](https://arxiv.org/html/2602.18078v1#S6.E2 "In Lemma 6.4. ‣ 6 Appendix ‣ Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators")) and concludes the proof.
∎

###### Lemma 6.5.

Let n>mn>m. The function f:(0,1)→ℝf:(0,1)\to\mathbb{R} defined by

|  |  |  |
| --- | --- | --- |
|  | f​(x)=xn−1xm−1f(x)=\frac{x^{n}-1}{x^{m}-1} |  |

is increasing on (0,1)(0,1).

###### Proof.

A straightforward computation yields

|  |  |  |
| --- | --- | --- |
|  | f′​(x)=(n−m)​xn+m−1−n​xn−1+m​xm−1(xm−1)2=xm−1​[(n−m)​xn−n​xn−m+m](xm−1)2.f^{\prime}(x)=\frac{(n-m)x^{n+m-1}-nx^{n-1}+mx^{m-1}}{(x^{m}-1)^{2}}=\frac{x^{m-1}[(n-m)x^{n}-nx^{n-m}+m]}{(x^{m}-1)^{2}}. |  |

Since xm−1>0x^{m-1}>0 and (xm−1)2>0(x^{m}-1)^{2}>0 for x∈(0,1)x\in(0,1), the sign of f′​(x)f^{\prime}(x) is determined by the function g​(x):=(n−m)​xn−n​xn−m+mg(x):=(n-m)x^{n}-nx^{n-m}+m for x∈(0,1)x\in(0,1). Differentiating, we obtain g′​(x)=n​(n−m)​xn−1−n​(n−m)​xn−m−1=n​(n−m)​xn−m−1​(xm−1)<0g^{\prime}(x)=n(n-m)x^{n-1}-n(n-m)x^{n-m-1}=n(n-m)x^{n-m-1}(x^{m}-1)<0 so that gg is strictly decreasing on (0,1)(0,1). Moreover, limx→1−g​(x)=0\lim\_{x\rightarrow 1^{-}}g(x)=0, which implies that g​(x)≥0g(x)\geq 0 for all x∈(0,1)x\in(0,1). Consequently, f′​(x)≥0f^{\prime}(x)\geq 0 on (0,1)(0,1), and the result follows.
∎

## References

* [1]

  Andersen, L., & Broadie, M. (2004). Primal-dual simulation algorithm for pricing multidimensional American options. Management Science, 50(9), 1222–1234.
* [2]

  Bahlali, K. (2020). A domination method for solving unbounded quadratic BSDEs. Graduate J. Math. (5), 20-36.
* [3]

  Bahlali, K., Eddahbi, M., & Ouknine, Y. (2017). Quadratic BSDEs with L2L^{2}-terminal data: Existence results, Krylov’s estimate, and Itô-Krylov’s formula. Annals of Probability, 45(4), 2377–2397.
* [4]

  Bahlali, K., & Tangpi, L. (2020). BSDEs driven by |z|2/y|z|^{2}/y and applications to PDEs and decision theory. arXiv:1810.05664v3.
* [5]

  Becker, S., Cheridito, P., & Jentzen, A. (2019). Deep optimal stopping. Journal of Machine Learning Research, 20, 74.
* [6]

  Becker, S., Cheridito, P., Jentzen, A., & Welti, T. (2021). Solving high-dimensional optimal stopping problems using deep learning. European Journal of Applied Mathematics, 32, 470-514.
* [7]

  Becker, S., Cheridito, P., & Jentzen, A. (2020). Pricing and hedging American-style options with deep learning. Journal of Risk and Financial Management, 13(7), 158.
* [8]

  Broadie, M., & Glasserman, P. (2004). A stochastic mesh method for pricing high dimensional American options. Journal of Computational Finance, 7, 35–72.
* [9]

  Chee, D., Frikha, N., & Li, L. (2025). An entropy regularized BSDE approach to Bermudan options and games. <https://arxiv.org/abs/2509.18747>
* [10]

  Chee, D., Frikha, N., & Li, L. (2026). A monotone limit approach to entropy‑regularized American options. Working paper.
* [11]

  Cvitanic, J., & Karatzas, I. (1996). Backward stochastic differential equations with reflection and Dynkin games. Annals of Probability, 24(4), 2024–2056.
* [12]

  Dellacherie, C., & Meyer, P. A. (1980). Probabilités et potentiel. Chap. V-VIII. Hermann.
* [13]

  Duffie, D., & Epstein, L. G. (1992). Stochastic differential utility. Econometrica, 60, 353–394.
* [14]

  Dai, M., Sun, Y., Xu, Z. Q., & Zhou, X. Y. (2024). Learning to optimally stop a diffusion process, with financial applications. Forthcoming in Management Science, <https://arxiv.org/abs/2408.09242>
* [15]

  Dai, M., & Dong, Y. (2024). Learning an optimal investment policy with transaction costs via a randomized Dynkin game. SSRN. <https://ssrn.com/abstract=4871712>
* [16]

  Dong, Y. (2024). Randomized optimal stopping problem in continuous time and reinforcement learning algorithm. SIAM Journal on Control and Optimization, 62(3), 1590–1614.
* [17]

  Dianetti, J., Ferrari, G., & Xu, R. (2024). Exploratory optimal stopping: A singular control formulation. <https://arxiv.org/abs/2408.09335>
* [18]

  E, W., Han, J., & Jentzen, A. (2018). Solving high-dimensional partial differential equations using deep learning. Proceedings of the National Academy of Sciences, 115(34), 8505–8510.
* [19]

  El Karoui, N., Kapoudjian, C., Pardoux, E., Peng, S., & Quenez, M. C. (1997). Reflected solutions of backward SDEs, and related obstacle problems for PDEs. Annals of Probability, 25(2), 702–737.
* [20]

  Fathan, A., & Delage, E. (2021). Deep reinforcement learning for optimal stopping with application in financial engineering. <https://arxiv.org/pdf/2105.08877>
* [21]

  Felizardo, L., Matsumoto, E., Del-Moral-Hernandez, E. (2022). Solving the optimal stopping problem with reinforcement learning: An application in financial option exercise. <https://arxiv.org/abs/2208.00765>
* [22]

  Gobet, E., & Wang, W. (2026). Improved Convergence Rate for Reflected BSDEs by Penalization Method. Applied Mathematics & Optimization, 93(10).
* [23]

  Grigorova, M., Imkeller, P., Offen, E., Ouknine, Y., & Quenez, M. C. (2017). Reflected BSDEs when the obstacle is not right-continuous and optimal stopping. Ann. Appl. Probab, 27(5), 3153 - 3188.
* [24]

  Guo, I., Langrené, N., & Wu, J. (2025). Simultaneous upper and lower bounds of American-style option prices with hedging via neural networks. Quantitative Finance, 25(4), 509–525.
* [25]

  Gyöngy, I., & Šiška, D. (2008). On randomized stopping. Bernoulli, 14(2), 352–361.
* [26]

  Hamadène, S., & Ouknine, Y. (2016). Reflected backward SDEs with general jumps. Theory of Probability & Its Applications, 60(2), 263–280.
* [27]

  Karatzas, I., & Shreve, S. (1998). Methods of mathematical finance. Springer.
* [28]

  Lapeyre, B., & Lelong, J. (2021). Neural network regression for Bermudan option pricing. Monte Carlo Methods and Applications, 27(3), 227–247.
* [29]

  Laeven, R. J. A., Rosazza Gianin, E., & Zullino, M. (2024). Geometric BSDEs. arXiv preprint arXiv:2405.09260v2.
* [30]

  Lepeltier, J. P., Matoussi, A., & Xu, M. (2005). Reflected backward stochastic differential equations under monotonicity and general increasing growth conditions. Advances in Applied Probability, 37, 134–159.
* [31]

  Lionnet, A., dos Reis, G., Szpruch, L. (2015). Time discretization of FBSDE with polynomial growth drivers and reaction–diffusion PDEs. Ann. Appl. Probab. 25(5) 2563–2625.
* [32]

  Longstaff, F. A., & Schwartz, E. S. (2001). Valuing American options by simulation: A simple least-squares approach. Review of Financial Studies, 14(1), 113–147.
* [33]

  Ludkovski, L. (2018). Kriging metamodels and experimental design for Bermudan option pricing. Journal of Computational Finance, 22(1), 37–77.
* [34]

  Maingueneau, A. M. (1978). Temps d’arrêt optimaux et théorie générale. In C. Dellacherie, P. A. Meyer, & M. Weil (Eds.), Séminaire de Probabilités XII, Lecture Notes in Mathematics (Vol. 649, pp. 457–467). Springer.
* [35]

  Nikeghbali, A. (2006). An essay on the general theory of stochastic processes. Probability Surveys, 3, 345–412.
* [36]

  Øksendal, B., & Zhang, T. (2012). Backward stochastic differential equations with respect to general filtrations and applications to insider finance. Communications on Stochastic Analysis, 6(4), Article 13.
* [37]

  Peng, S. (1999). Monotonic limit theorem of BSDE and nonlinear decomposition theorem of Doob–Meyers type. Probability Theory and Related Fields, 113, 473–499.
* [38]

  Schoenmakers, J., Zhang, J., & Huang, J. (2013). Optimal dual martingales, their analysis, and application to new algorithms for Bermudan products. SIAM Journal on Financial Mathematics, 4(1), 86–116.
* [39]

  Soner, H. M., & Tissot-Daguette, V. (2025). Stopping times of boundaries: Relaxation and continuity. SIAM Journal on Control and Optimization, 63(4), 2835–2855.
* [40]

  Reppen, A. M., Soner, H. M., & Tissot-Daguette, V. (2025). Neural optimal stopping boundary. Mathematical Finance, 35, 441–469.
* [41]

  Rogers, L. C. G. (2010). Dual valuation and hedging of Bermudan options. SIAM Journal on Financial Mathematics, 1(1), 604–608.
* [42]

  Rogers, L. C. G. (2002). Monte Carlo valuation of American options. Mathematical Finance, 12(3), 271–286.
* [43]

  Tang, W., Zhang, P. Y., & Zhou, X. Y. (2023). Exploratory HJB equations and their convergence. SIAM Journal on Control and Optimization, 61(2), 789–823.
* [44]

  Wang, H., Zariphopoulou, T., & Zhou, X. Y. (2020). Reinforcement learning in continuous time and space: A stochastic control approach. Journal of Machine Learning Research, 21, 198–1–198–34.
* [45]

  Wang, S., X. Q. Yang, and K. L. Teo. (2006). ”Power Penalty Method for a Linear Complementarity Problem Arising from American Option Valuation.” Journal of Optimization Theory and Applications 129 (2), 227-254.
* [46]

  Wang, S., and Huang, C.-S. (2008). A power penalty method for solving a nonlinear parabolic complementarity problem. Nonlinear Analysis: Theory, Methods & Applications, 69(4), 1125–1137.
* [47]

  Wang, W., & Jia, G. (2025). Quadratic BSDEs with singular generators and unbounded terminal conditions: Theory and applications. Mathematics, 13(14), 2292.
* [48]

  Zheng, S. (2024). Well-posedness of quadratic RBSDEs and BSDEs with one-sided growth restrictions. arXiv:2412.21172v1.
* [49]

  Zheng, S., Zhang, L., & Feng, L. (2021). On the backward stochastic differential equation with generator f​(y)​|z|2f(y)|z|^{2}. Journal of Mathematical Analysis and Applications, 500(1), 125102.
* [50]

  Zheng, S., Zhang, L., & Meng, X. (2025). A class of quadratic reflected BSDEs with singular coefficients. Probability, Uncertainty and Quantitative Risk, (10) 3, 405-420.