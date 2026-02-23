---
authors:
- Daniel Chee
- Noufel Frikha
- Libo Li
doc_id: arxiv:2602.18062v1
family_id: arxiv:2602.18062
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Monotone Limit Approach to Entropy‑Regularized American Options
url_abs: http://arxiv.org/abs/2602.18062v1
url_html: https://arxiv.org/html/2602.18062v1
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

Recent advances in continuous-time optimal stopping have been driven by entropy-regularized formulations of randomized stopping problems, with most existing approaches relying on partial differential equation methods. In this paper, we propose a fully probabilistic framework based on the Doob-Meyer-Mertens decomposition of the Snell envelope and its representation through reflected backward stochastic differential equations. We introduce an entropy-regularized penalization scheme yielding a monotone approximation of the value function and establish explicit convergence rates under suitable regularity assumptions. In addition, we develop a policy improvement algorithm based on linear backward stochastic differential equations and illustrate its performance through a simple numerical experiment for an American-style max call option.

## 1 Introduction

The numerical resolution of optimal stopping problems using Monte Carlo and machine learning techniques has been the subject of extensive research; see, for instance,
[[2](https://arxiv.org/html/2602.18062v1#bib.bib2), [3](https://arxiv.org/html/2602.18062v1#bib.bib3), [4](https://arxiv.org/html/2602.18062v1#bib.bib4), [5](https://arxiv.org/html/2602.18062v1#bib.bib5), [30](https://arxiv.org/html/2602.18062v1#bib.bib30), [29](https://arxiv.org/html/2602.18062v1#bib.bib29), [28](https://arxiv.org/html/2602.18062v1#bib.bib28), [12](https://arxiv.org/html/2602.18062v1#bib.bib12), [11](https://arxiv.org/html/2602.18062v1#bib.bib11), [13](https://arxiv.org/html/2602.18062v1#bib.bib13), [15](https://arxiv.org/html/2602.18062v1#bib.bib15)].
More recently, advances in reinforcement learning (RL) have stimulated renewed interest in continuous-time formulations of optimal stopping problems arising in mathematical finance.
A particularly remarkable and recent development in this direction is the entropy-regularized randomized stopping framework introduced independently by Dong [[13](https://arxiv.org/html/2602.18062v1#bib.bib13)], Dianetti *et al.* [[15](https://arxiv.org/html/2602.18062v1#bib.bib15)], and Dai *et al.* [[11](https://arxiv.org/html/2602.18062v1#bib.bib11)].

The entropy-regularization paradigm recasts the classical optimal stopping problem as an exploratory control problem, thereby enabling the design of RL algorithms through a partial differential equation (PDE) approach, typically via Hamilton–Jacobi–Bellman (HJB) equations.
A central feature of this framework is a policy-based interpretation, in which the control represents the instantaneous stopping intensity, conditional on survival.
This viewpoint has proved remarkably flexible and has since served as the foundation for a growing body of work extending the original formulation of [[13](https://arxiv.org/html/2602.18062v1#bib.bib13)].

Among recent contributions, Dai *et al.* [[9](https://arxiv.org/html/2602.18062v1#bib.bib9)] propose a recursive entropy-regularization scheme with biased Gaussian exploration to learn Merton-type strategies in incomplete markets.
Dai and Dong [[12](https://arxiv.org/html/2602.18062v1#bib.bib12)] investigate investment problems with transaction costs through randomized Dynkin games, while Dong and Zheng [[14](https://arxiv.org/html/2602.18062v1#bib.bib14)] study mean–variance stopping problems using an extended HJB system combined with vanishing regularization.
Further extensions include the continuous-time RL framework with regime switching developed by Huang *et al.* [[21](https://arxiv.org/html/2602.18062v1#bib.bib21)], as well as actuarial applications to insurance surrender decisions by Jia *et al.* [[22](https://arxiv.org/html/2602.18062v1#bib.bib22)].
Collectively, these works underscore the breadth and effectiveness of entropy-regularized RL methods in continuous-time stochastic control.

The present work is motivated by this expanding literature on RL for continuous-time control
[[31](https://arxiv.org/html/2602.18062v1#bib.bib31), [32](https://arxiv.org/html/2602.18062v1#bib.bib32)]
and is particularly aligned with the objectives of [[13](https://arxiv.org/html/2602.18062v1#bib.bib13)].
As in [[13](https://arxiv.org/html/2602.18062v1#bib.bib13), [15](https://arxiv.org/html/2602.18062v1#bib.bib15), [11](https://arxiv.org/html/2602.18062v1#bib.bib11)], our starting point is the randomized stopping representation of the value process VV associated with an optimal stopping problem with payoff PP.
Specifically, following Gyöngy and Šiška [[19](https://arxiv.org/html/2602.18062v1#bib.bib19), Theorem 2.1], one has

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=ess​supτ∈𝒯t,T⁡𝔼​[Pτ∣ℱt]=ess​supγ∈Λ⁡𝔼​[PT​e−∫tTγu​𝑑u+∫tTPs​γs​e−∫tsγu​𝑑u​𝑑s|ℱt],\displaystyle V\_{t}=\operatornamewithlimits{ess\,sup}\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}[P\_{\tau}\mid\mathcal{F}\_{t}]=\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\mathbb{E}\Big[P\_{T}e^{-\int\_{t}^{T}\gamma\_{u}du}+\int\_{t}^{T}P\_{s}\gamma\_{s}e^{-\int\_{t}^{s}\gamma\_{u}du}ds\,\Big|\,\mathcal{F}\_{t}\Big], |  | (1.1) |

where 𝒯t,T\mathcal{T}\_{t,T} denotes the set of stopping times taking values in [t,T][t,T] and
Λ=∪n=1∞Λn\Lambda=\cup\_{n=1}^{\infty}\Lambda\_{n}, with

|  |  |  |
| --- | --- | --- |
|  | Λn:={γ:γ​ is non-negative, adapted, and ​0≤γ≤n}.\Lambda\_{n}:=\{\gamma:\ \gamma\text{ is non-negative, adapted, and }0\leq\gamma\leq n\}. |  |

In contrast to the PDE-based approaches adopted in
[[13](https://arxiv.org/html/2602.18062v1#bib.bib13), [15](https://arxiv.org/html/2602.18062v1#bib.bib15), [11](https://arxiv.org/html/2602.18062v1#bib.bib11)],
we pursue here a purely probabilistic perspective, in the spirit of our earlier work on Bermudan options in Chee *et al.* [[6](https://arxiv.org/html/2602.18062v1#bib.bib6)].
Our analysis relies on the Doob-Meyer-Mertens decomposition of the Snell envelope VV and its characterization through reflected backward stochastic differential equations (RBSDEs or reflected BSDEs).
Formally applying Itô’s formula to the right-hand side of ([1.1](https://arxiv.org/html/2602.18062v1#S1.E1 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) suggests the backward representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=PT−(MT−Mt)+ess​supγ∈Λ​∫tT(Ps−Vs)​γs​𝑑s,\displaystyle V\_{t}=P\_{T}-(M\_{T}-M\_{t})+\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\int\_{t}^{T}(P\_{s}-V\_{s})\gamma\_{s}\,ds, |  | (1.2) |

where MM is a martingale.

The backward equation ([1.2](https://arxiv.org/html/2602.18062v1#S1.E2 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) is ill-posed, since the optimal control, if it exists, formally satisfies
γs∗=∞⋅𝟏{s≥τ∗}\gamma\_{s}^{\ast}=\infty\cdot\mathbf{1}\_{\{s\geq\tau\_{\ast}\}},
where τ∗\tau\_{\ast} denotes the optimal stopping time in ([1.1](https://arxiv.org/html/2602.18062v1#S1.E1 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")).
To overcome this difficulty, we introduce an entropy-based penalization and consider the family of BSDEs

|  |  |  |  |
| --- | --- | --- | --- |
|  | vtλ=PT−(mTλ−mtλ)+ess​supγ∈Λ​∫tT((Ps−vsλ)​γs−λ​(penalty term))​𝑑s,\displaystyle v^{\lambda}\_{t}=P\_{T}-(m^{\lambda}\_{T}-m^{\lambda}\_{t})+\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\int\_{t}^{T}\Big((P\_{s}-v^{\lambda}\_{s})\gamma\_{s}-\lambda\,(\text{penalty term})\Big)ds, |  | (1.3) |

where λ≥0\lambda\geq 0 is a temperature parameter.

Unlike [[13](https://arxiv.org/html/2602.18062v1#bib.bib13)], which employs the penalty function x​ln⁡x−xx\ln x-x, we adopt the modified entropy penalty x​ln⁡x−x+1x\ln x-x+1.
This choice yields a monotone sequence of BSDE solutions as λ↓0\lambda\downarrow 0, and we therefore refer to the resulting procedure as an *entropy-regularized penalization scheme*.
In contrast to the classical penalization approach for RBSDEs, which relies on truncating the control γ\gamma (see [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)]), our method provides a smooth and analytically tractable regularization of the reflected constraint.

For completeness, we note that a related but distinct approach is developed in our companion working paper [[7](https://arxiv.org/html/2602.18062v1#bib.bib7)], where entropy regularization is introduced through the classical truncation-based penalization scheme for reflected BSDEs, leading to a reflected equation with a singular driver.
The focus of [[7](https://arxiv.org/html/2602.18062v1#bib.bib7)] is on well-posedness and structural properties of the resulting RBSDE, whereas the present paper emphasizes convergence rates, policy improvement algorithms (PIA), and numerical implementation within the entropy-regularized framework.

The rest of the paper is organised as follows.
In Section [2](https://arxiv.org/html/2602.18062v1#S2 "2 Preliminaries ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), we introduce the probabilistic framework and recall several results from stochastic analysis that will be used throughout the paper.

Section [3](https://arxiv.org/html/2602.18062v1#S3 "3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options") is devoted to the entropy-regularized formulation of the optimal stopping problem.
We introduce the penalized BSDE associated with the randomized stopping representation and establish its well-posedness. Exploiting monotonicity arguments developed in El Karoui *et al.* [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)] and Peng [[27](https://arxiv.org/html/2602.18062v1#bib.bib27)], we then show that, as the temperature parameter λ\lambda tends to zero, the entropy-regularized value process converges monotonically to the value of the original optimal stopping problem.
Under additional regularity assumptions on the payoff process, we further derive quantitative convergence rates for both lower and upper bounds. We conclude this section by studying the PIA associated with the entropy-regularized problem.
The algorithm is based on an iterative sequence of linear BSDEs and admits an explicit policy update at each step.
We prove that the resulting sequence of value functions converges increasingly to the entropy-regularized value function at a factorial rate.

Section [4](https://arxiv.org/html/2602.18062v1#S4 "4 Numerical Experiments ‣ A Monotone Limit Approach to Entropy‑Regularized American Options") is devoted to a simple numerical experiment. We present an efficient implementation of the PIA in the case of max-call option in the Black-Scholes setting.
Our numerical results confirm the theoretical convergence properties and demonstrate that, for small values of λ\lambda, the entropy-regularized approach provides accurate approximations of classical optimal stopping prices.

Finally, we refer interested readers to our working paper [[7](https://arxiv.org/html/2602.18062v1#bib.bib7)], which introduces entropy-regularization via the standard penalization scheme for RBSDEs, investigates the well-posedness properties of the resulting RBSDE with singular driver, and provides a probabilistic interpretation of the approach.

## 2 Preliminaries

We work on a standard filtered probability space (Ω,ℱ,ℙ,𝔽)(\Omega,\mathcal{F},\mathbb{P},\mathbb{F}), where the filtration 𝔽=(ℱt)t≥0\mathbb{F}=(\mathcal{F}\_{t})\_{t\geq 0} is assumed to satisfy the usual conditions. Any additional assumptions imposed on the filtration 𝔽\mathbb{F} will be stated explicitly when required. We denote by 𝒪​(𝔽)\mathcal{O}(\mathbb{F}) the space of 𝔽\mathbb{F}-optional processes, by 𝒫​(𝔽)\mathcal{P}(\mathbb{F}) the space of 𝔽\mathbb{F}-predictable processes, by ℳ\mathcal{M} the space of 𝔽\mathbb{F}-martingales, and by 𝒜+\mathcal{A}^{+} the space of 𝔽\mathbb{F}-predictable, non-decreasing processes. We further adopt the standard notation x∨y:=max⁡(x,y)x\vee y:=\max(x,y), x+:=max⁡(x,0)x^{+}:=\max(x,0), and x−:=max⁡(−x,0)x^{-}:=\max(-x,0). Throughout the paper, CC and KK denote generic positive constants whose values may change from line to line.

We shall work extensively with the following function spaces. The Banach space of square-integrable optional processes is defined as

|  |  |  |
| --- | --- | --- |
|  | 𝒮2:={X∈𝒪​(𝔽):𝔼​[sup0≤t≤T|Xt|2]<∞}.\mathcal{S}^{2}:=\big\{X\in\mathcal{O}(\mathbb{F}):\mathbb{E}\big[\sup\_{0\leq t\leq T}|X\_{t}|^{2}\big]<\infty\big\}. |  |

The space of square-integrable 𝔽\mathbb{F}-martingales is given by

|  |  |  |
| --- | --- | --- |
|  | ℋ2:={M∈ℳ:𝔼​[[M]T]<∞},\mathcal{H}^{2}:=\big\{M\in\mathcal{M}:\mathbb{E}\big[[M]\_{T}\big]<\infty\big\}, |  |

where [M][M] denotes the quadratic variation of MM. The space of square-integrable, 𝔽\mathbb{F}-predictable, increasing processes is

|  |  |  |
| --- | --- | --- |
|  | 𝒦2:={A∈𝒜+:𝔼​[AT2]<∞}.\mathcal{K}^{2}:=\big\{A\in\mathcal{A}^{+}:\mathbb{E}\big[A\_{T}^{2}\big]<\infty\big\}. |  |

We recall that if the payoff process PP is càdlàg and satisfies appropriate integrability conditions, then the value process V=(Vt)0≤t≤TV=(V\_{t})\_{0\leq t\leq T} associated with the corresponding optimal stopping problem belongs to class (D), that is, the family {Vτ:τ​ stopping time}\{V\_{\tau}:\tau\text{ stopping time}\} is uniformly integrable. In this setting, VV admits a Doob–Meyer decomposition and equivalently satisfies the RBSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt\displaystyle V\_{t} | =PT−(MT−Mt)+(AT−At),t∈[0,T],\displaystyle=P\_{T}-(M\_{T}-M\_{t})+(A\_{T}-A\_{t}),\qquad t\in[0,T], |  | (2.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt\displaystyle V\_{t} | ≥Pt,and∫0T(Vs−−Ps−)​𝑑As=0,\displaystyle\geq P\_{t},\quad\text{and}\quad\int\_{0}^{T}(V\_{s-}-P\_{s-})\,dA\_{s}=0, |  |

where MM is a uniformly integrable 𝔽\mathbb{F}-martingale and AA is a 𝔽\mathbb{F}-predictable, increasing process. In particular, if P∈𝒮2P\in\mathcal{S}^{2}, then (V,M,A)∈𝒮2×ℋ2×𝒦2(V,M,A)\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{K}^{2}; see, for instance, Steps 1–4 in the proof of Lemma 3.3 in Grigorova *et al.* [[18](https://arxiv.org/html/2602.18062v1#bib.bib18)].

For further background on optimal stopping problems and on the theory of BSDEs and RBSDEs under general filtrations, we refer the reader to Maingueneau [[25](https://arxiv.org/html/2602.18062v1#bib.bib25)], El Karoui *et al.* [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)], Øksendal and Zhang [[26](https://arxiv.org/html/2602.18062v1#bib.bib26)], Grigorova *et al.* [[18](https://arxiv.org/html/2602.18062v1#bib.bib18)], and Hamadène and Ouknine [[20](https://arxiv.org/html/2602.18062v1#bib.bib20)].

## 3 Entropy-Regularized Penalization Scheme

In this section, we exploit the connection between the randomized stopping representation ([1.1](https://arxiv.org/html/2602.18062v1#S1.E1 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) and the associated BSDE formulation ([1.2](https://arxiv.org/html/2602.18062v1#S1.E2 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) to introduce an entropy-regularized penalization scheme. We analyze its convergence to the price of the corresponding American option as the temperature parameter λ\lambda tends to zero. We also introduce the associated policy improvement algorithm (PIA) and investigate its convergence properties.

### 3.1 Definition of the entropy-regularized penalization scheme

We begin by stating the standing assumption on the payoff process.

###### Assumption 3.1.

The payoff PP is càdlàg and uniformly bounded, with bound denoted by |P|∞|P|\_{\infty}.

As previously discussed, our main idea is to penalize the control γ\gamma directly at the level of the BSDE representation ([1.2](https://arxiv.org/html/2602.18062v1#S1.E2 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), rather than at the level of the randomized stopping problem itself. More precisely, we consider the BSDE

|  |  |  |
| --- | --- | --- |
|  | vtλ=PT−(mTλ−mtλ)+ess​supγ∈Λ​∫tT((Ps−vsλ)​γs−λ​(γs​ln⁡γs−γs+1))​𝑑s.\displaystyle v^{\lambda}\_{t}=P\_{T}-(m^{\lambda}\_{T}-m^{\lambda}\_{t})+\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\int\_{t}^{T}\Big((P\_{s}-v^{\lambda}\_{s})\gamma\_{s}-\lambda\big(\gamma\_{s}\ln\gamma\_{s}-\gamma\_{s}+1\big)\Big)\,ds. |  |

The first-order optimality condition associated with this control problem is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ps−vsλ)−λ​ln⁡(γs)=0,(P\_{s}-v^{\lambda}\_{s})-\lambda\ln(\gamma\_{s})=0, |  | (3.1) |

which yields the explicit expression for the optimal control (or policy)

|  |  |  |  |
| --- | --- | --- | --- |
|  | γs=exp⁡((Ps−vsλ)/λ).\gamma\_{s}=\exp\big((P\_{s}-v^{\lambda}\_{s})/\lambda\big). |  | (3.2) |

In particular, this optimal policy does not explode at infinity.

Substituting ([3.2](https://arxiv.org/html/2602.18062v1#S3.E2 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) back into the BSDE, we obtain the following nonlinear equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vtλ=PT−(mTλ−mtλ)+∫tTλ​(e(Ps−vsλ)/λ−1)​𝑑s.v^{\lambda}\_{t}=P\_{T}-(m^{\lambda}\_{T}-m^{\lambda}\_{t})+\int\_{t}^{T}\lambda\big(e^{(P\_{s}-v^{\lambda}\_{s})/\lambda}-1\big)\,ds. |  | (3.3) |

Throughout the remainder of this section, we refer to the family

|  |  |  |
| --- | --- | --- |
|  | {vλ:=(vtλ)t∈[0,T]:λ∈(0,1]}\big\{v^{\lambda}:=(v^{\lambda}\_{t})\_{t\in[0,T]}\;:\;\lambda\in(0,1]\big\} |  |

as the *entropy-regularized penalization scheme*. We first establish the well-posedness of the BSDE ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")). Its convergence to the value process VV of the American option with payoff PP as λ↓0\lambda\downarrow 0 is addressed in Section [3.2](https://arxiv.org/html/2602.18062v1#S3.SS2 "3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options").

###### Remark 3.1.

There are several possible ways to penalize the original control problem in ([1.2](https://arxiv.org/html/2602.18062v1#S1.E2 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")). For instance, following [[13](https://arxiv.org/html/2602.18062v1#bib.bib13)], one may consider the entropy term x​ln⁡x−xx\ln x-x, which leads to the BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ=PT−(MTλ−Mtλ)+ess​supγ∈Λ​∫tT((Ps−Vsλ)​γs−λ​(γs​ln⁡γs−γs))​𝑑s.\displaystyle V^{\lambda}\_{t}=P\_{T}-(M^{\lambda}\_{T}-M^{\lambda}\_{t})+\operatornamewithlimits{ess\,sup}\_{\gamma\in\Lambda}\int\_{t}^{T}\Big((P\_{s}-V^{\lambda}\_{s})\gamma\_{s}-\lambda(\gamma\_{s}\ln\gamma\_{s}-\gamma\_{s})\Big)\,ds. |  | (3.4) |

Assuming the existence of a solution (Vλ,Mλ)∈𝒮2×ℋ2(V^{\lambda},M^{\lambda})\in\mathcal{S}^{2}\times\mathcal{H}^{2}, the associated optimal policy is again given by ([3.2](https://arxiv.org/html/2602.18062v1#S3.E2 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), and the BSDE reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtλ=PT−(MTλ−Mtλ)+∫tTλ​e(Ps−Vsλ)/λ​𝑑s.V^{\lambda}\_{t}=P\_{T}-(M^{\lambda}\_{T}-M^{\lambda}\_{t})+\int\_{t}^{T}\lambda e^{(P\_{s}-V^{\lambda}\_{s})/\lambda}\,ds. |  | (3.5) |

The above discussion illustrates that the choice of penalization is not unique and may lead to different optimal policies and families of BSDEs. However, as we shall show below, a key advantage of our formulation compared to that of [[13](https://arxiv.org/html/2602.18062v1#bib.bib13)] is that the family of solutions (vλ)λ∈(0,1](v^{\lambda})\_{\lambda\in(0,1]} defined by ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) is monotone increasing as λ\lambda decreases.

We observe that, in the present setting, the driver in ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) is given by

|  |  |  |
| --- | --- | --- |
|  | x⟼λ​(e(Ps−x)/λ−1),x\longmapsto\lambda\big(e^{(P\_{s}-x)/\lambda}-1\big), |  |

which is monotone decreasing in xx. As a consequence, uniqueness follows from arguments similar to those developed in Lepeltier *et al.* [[23](https://arxiv.org/html/2602.18062v1#bib.bib23)]. Therefore, it suffices to establish the existence of a solution, noting that the driver is only locally Lipschitz continuous.

###### Proposition 3.1.

For any λ∈(0,1]\lambda\in(0,1], there exists a unique solution (vλ,mλ)∈𝒮2×ℳ2(v^{\lambda},m^{\lambda})\in\mathcal{S}^{2}\times{\mathcal{M}}^{2} to ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")).

###### Proof.

To prove existence, we proceed by truncation. Fix n≥Tn\geq T and consider the BSDE with Lipschitz continuous driver

|  |  |  |
| --- | --- | --- |
|  | vtλ,n=PT−∫tT𝑑msλ,n+∫tTλ​(e(Ps−vsλ,n∨(−n))/λ−1)​𝑑s.\displaystyle v^{\lambda,n}\_{t}=P\_{T}-\int\_{t}^{T}dm^{\lambda,n}\_{s}+\int\_{t}^{T}\lambda\Big(e^{(P\_{s}-v^{\lambda,n}\_{s}\vee(-n))/\lambda}-1\Big)\,ds. |  |

By standard results for BSDEs with Lipschitz drivers (see, for example, Theorem 3.1 in Øksendal and Zhang [[26](https://arxiv.org/html/2602.18062v1#bib.bib26)]), there exists a solution
(vλ,n,mλ,n)∈𝒮2×ℳ2(v^{\lambda,n},m^{\lambda,n})\in\mathcal{S}^{2}\times{\mathcal{M}}^{2}.
Moreover, taking conditional expectations yields

|  |  |  |
| --- | --- | --- |
|  | vtλ,n+λ​(T−t)=𝔼​[PT+∫tTλ​e(Ps−vsλ,n∨(−n))/λ​𝑑s|ℱt]≥0.\displaystyle v^{\lambda,n}\_{t}+\lambda(T-t)={\mathbb{E}}\Big[P\_{T}+\int\_{t}^{T}\lambda e^{(P\_{s}-v^{\lambda,n}\_{s}\vee(-n))/\lambda}\,ds\;\Big|\;{\mathcal{F}}\_{t}\Big]\geq 0. |  |

It follows that vtλ,n≥−λ​T≥−T≥−nv^{\lambda,n}\_{t}\geq-\lambda T\geq-T\geq-n, and therefore the truncation is inactive. Consequently,

|  |  |  |
| --- | --- | --- |
|  | vtλ,n=𝔼​[PT+∫tTλ​(e(Ps−vsλ,n)/λ−1)​𝑑s|ℱt],\displaystyle v^{\lambda,n}\_{t}={\mathbb{E}}\Big[P\_{T}+\int\_{t}^{T}\lambda\big(e^{(P\_{s}-v^{\lambda,n}\_{s})/\lambda}-1\big)\,ds\;\Big|\;{\mathcal{F}}\_{t}\Big], |  |

which shows that (vλ,n,mλ,n)(v^{\lambda,n},m^{\lambda,n}) actually solves ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")). The result then follows from uniqueness.
∎

### 3.2 Convergence to the American Option

In this subsection, we show that as λ↓0\lambda\downarrow 0, the entropy-regularized penalization scheme (vλ)λ∈(0,1](v^{\lambda})\_{\lambda\in(0,1]} converges to the value process VV of the American option defined in ([1.1](https://arxiv.org/html/2602.18062v1#S1.E1 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")). We also investigate the associated rate of convergence.

To this end, we introduce the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | γtλ:=λPt−vtλ​(e(Pt−vtλ)/λ−1),t∈[0,T].\displaystyle\gamma^{\lambda}\_{t}:=\frac{\lambda}{P\_{t}-v^{\lambda}\_{t}}\big(e^{(P\_{t}-v^{\lambda}\_{t})/\lambda}-1\big),\quad t\in[0,T]. |  | (3.6) |

With this notation, the BSDE ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) can be rewritten in the form

|  |  |  |
| --- | --- | --- |
|  | vtλ=PT−(mTλ−mtλ)+∫tT(Ps−vsλ)​γsλ​𝑑s.\displaystyle v\_{t}^{\lambda}=P\_{T}-(m^{\lambda}\_{T}-m^{\lambda}\_{t})+\int\_{t}^{T}(P\_{s}-v^{\lambda}\_{s})\,\gamma^{\lambda}\_{s}\,ds. |  |

Observe that the function x↦x−1​(ex−1)x\mapsto x^{-1}(e^{x}-1) is positive and strictly increasing on ℝ\mathbb{R}. As a consequence, for any fixed λ∈(0,1]\lambda\in(0,1], the process γλ\gamma^{\lambda} defined in ([3.6](https://arxiv.org/html/2602.18062v1#S3.E6 "In 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) admits a natural interpretation as a stopping intensity.

We next show that the stopping intensity process γλ\gamma^{\lambda} is uniformly bounded. Taking ℱt{\mathcal{F}}\_{t}-conditional expectations in ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) and using the fact that P≥0P\geq 0, we obtain

|  |  |  |
| --- | --- | --- |
|  | vtλ+λ​(T−t)≥0,v\_{t}^{\lambda}+\lambda(T-t)\geq 0, |  |

which implies Pt−vtλ≤Pt+λ​TP\_{t}-v^{\lambda}\_{t}\leq P\_{t}+\lambda T. Combined with the inequality

|  |  |  |
| --- | --- | --- |
|  | 0≤ex−1x≤ex+,0\leq\frac{e^{x}-1}{x}\leq e^{x^{+}}, |  |

this yields the boundedness of γλ\gamma^{\lambda} under Assumption [3.1](https://arxiv.org/html/2602.18062v1#S3.Thmhyp1 "Assumption 3.1. ‣ 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options").

Applying Itô’s formula to the process
e−∫0tγsλ​𝑑s​vtλe^{-\int\_{0}^{t}\gamma^{\lambda}\_{s}\,ds}\,v^{\lambda}\_{t}
and invoking the randomized stopping representation of optimal stopping problems in ([1.1](https://arxiv.org/html/2602.18062v1#S1.E1 "In 1 Introduction ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), we deduce that for all λ>0\lambda>0 and all t∈[0,T]t\in[0,T]

|  |  |  |
| --- | --- | --- |
|  | vtλ≤Vta.s.v^{\lambda}\_{t}\leq V\_{t}\quad a.s. |  |

Moreover, for any x∈ℝx\in\mathbb{R}, the mapping λ↦λ​(ex/λ−1)\lambda\mapsto\lambda\big(e^{x/\lambda}-1\big)
is decreasing. Indeed, a direct computation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​λ​[λ​(ex/λ−1)]=(1−xλ)​ex/λ−1≤0,\displaystyle\frac{d}{d\lambda}\!\Big[\lambda\big(e^{x/\lambda}-1\big)\Big]=\Big(1-\frac{x}{\lambda}\Big)e^{x/\lambda}-1\leq 0, |  | (3.7) |

where the inequality follows from the elementary bound 1+c≤ec1+c\leq e^{c}, valid for all c∈ℝc\in\mathbb{R}.

As a consequence, by the comparison theorem for BSDEs (see e.g. Theorem 3.4 in [[26](https://arxiv.org/html/2602.18062v1#bib.bib26)]) and the monotone convergence theorem, there exists an optional process v^:=limλ↓0vλ\widehat{v}:=\lim\_{\lambda\downarrow 0}v^{\lambda},
satisfying

|  |  |  |
| --- | --- | --- |
|  | v^t≤Vt,t∈[0,T].\widehat{v}\_{t}\leq V\_{t},\quad t\in[0,T]. |  |

Our first main result shows that this inequality is, in fact, an equality.

###### Theorem 3.1.

The entropy-regularized penalization scheme vλv^{\lambda} converges to the value of the American option VV as λ→0\lambda\rightarrow 0, that is, it holds

|  |  |  |
| --- | --- | --- |
|  | limλ↓0vtλ=Vta.s.\lim\_{\lambda\downarrow 0}v^{\lambda}\_{t}=V\_{t}\quad a.s. |  |

###### Proof.

To prove that v^=V\widehat{v}=V, it suffices to show that v^\widehat{v} is a supermartingale dominating the payoff process PP. Indeed, by the Snell envelope characterization of the value process VV, this property uniquely identifies VV as the smallest supermartingale dominating PP.

We begin by showing that v^\widehat{v} is a supermartingale.
Recall that the BSDE satisfied by vλv^{\lambda} may be rewritten as

|  |  |  |
| --- | --- | --- |
|  | vtλ−λ​t=PT−λ​T−(mTλ−mtλ)+∫tTλ​e(Ps−λ​s−(vsλ−λ​s))/λ​𝑑s.\displaystyle v\_{t}^{\lambda}-\lambda t=P\_{T}-\lambda T-(m^{\lambda}\_{T}-m^{\lambda}\_{t})+\int\_{t}^{T}\lambda e^{(P\_{s}-\lambda s-(v^{\lambda}\_{s}-\lambda s))/\lambda}\,ds. |  |

Define v¯tλ:=vtλ−λ​t\bar{v}\_{t}^{\lambda}:=v\_{t}^{\lambda}-\lambda t and P¯t:=Pt−λ​t\bar{P}\_{t}:=P\_{t}-\lambda t. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯tλ=P¯T−(mTλ−mtλ)+∫tTλ​e(P¯s−v¯sλ)/λ​𝑑s.\displaystyle\bar{v}\_{t}^{\lambda}=\bar{P}\_{T}-(m^{\lambda}\_{T}-m^{\lambda}\_{t})+\int\_{t}^{T}\lambda e^{(\bar{P}\_{s}-\bar{v}^{\lambda}\_{s})/\lambda}\,ds. |  | (3.8) |

From this representation, it follows that (v¯λ)λ>0(\bar{v}^{\lambda})\_{\lambda>0} is a family of bounded supermartingales. Moreover, since both vλv^{\lambda} and −λ​t-\lambda t are increasing as λ↓0\lambda\downarrow 0, the sequence (v¯λ)(\bar{v}^{\lambda}) is increasing in λ−1\lambda^{-1}. Consequently, v^=limλ↓0vλ\widehat{v}=\lim\_{\lambda\downarrow 0}v^{\lambda} is the almost sure limit of an increasing sequence of supermartingales. By Theorem 1.8 in Dellacherie and Meyer [[8](https://arxiv.org/html/2602.18062v1#bib.bib8)], p. 86, v^\widehat{v} is therefore a càdlàg supermartingale.

It remains to show that v^\widehat{v} dominates PP.
Since vλ≤v^≤Vv^{\lambda}\leq\widehat{v}\leq V, we have e(v^−vλ)/λ≥1e^{(\widehat{v}-v^{\lambda})/\lambda}\geq 1 and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​𝔼​[vtλ]\displaystyle\lambda\mathbb{E}[v\_{t}^{\lambda}] | =λ​𝔼​[PT]+𝔼​[∫tTλ2​(e(Ps−v^s)/λ​e(v^s−vsλ)/λ−1)​𝑑s]\displaystyle=\lambda\mathbb{E}[P\_{T}]+\mathbb{E}\!\left[\int\_{t}^{T}\lambda^{2}\Big(e^{(P\_{s}-\widehat{v}\_{s})/\lambda}e^{(\widehat{v}\_{s}-v^{\lambda}\_{s})/\lambda}-1\Big)ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥λ​𝔼​[PT]+𝔼​[∫tTλ2​(e(Ps−v^s)/λ−1)​𝑑s]\displaystyle\geq\lambda\mathbb{E}[P\_{T}]+\mathbb{E}\!\left[\int\_{t}^{T}\lambda^{2}\big(e^{(P\_{s}-\widehat{v}\_{s})/\lambda}-1\big)ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥λ​𝔼​[PT]+𝔼​[∫tTλ2​e(Ps−v^s)/λ​𝟏{v^s<Ps}​𝑑s]−λ2​(T−t)≥−λ2​(T−t).\displaystyle\geq\lambda\mathbb{E}[P\_{T}]+\mathbb{E}\!\left[\int\_{t}^{T}\lambda^{2}e^{(P\_{s}-\widehat{v}\_{s})/\lambda}\mathbf{1}\_{\{\widehat{v}\_{s}<P\_{s}\}}\,ds\right]-\lambda^{2}(T-t)\geq-\lambda^{2}(T-t). |  |

Applying Fatou’s lemma yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫tTlim infλ↓0λ2​e(Ps−v^s)/λ​𝟏{v^s<Ps}​d​s]=0.\displaystyle\mathbb{E}\!\left[\int\_{t}^{T}\liminf\_{\lambda\downarrow 0}\lambda^{2}e^{(P\_{s}-\widehat{v}\_{s})/\lambda}\mathbf{1}\_{\{\widehat{v}\_{s}<P\_{s}\}}\,ds\right]=0. |  |

Since λ2​ex/λ→+∞\lambda^{2}e^{x/\lambda}\to+\infty as λ↓0\lambda\downarrow 0 for any x>0x>0, this implies that
v^s≥Ps\widehat{v}\_{s}\geq P\_{s} for all s∈[t,T]s\in[t,T], almost surely.
Finally, as both v^\widehat{v} and PP are càdlàg processes, the inequality holds for all s∈[0,T]s\in[0,T].

We conclude that v^\widehat{v} is a supermartingale dominating PP. Since VV is the smallest such supermartingale, it follows that v^=V\widehat{v}=V.
∎

Next, we quantify the discrepancy between the entropy-regularized penalization scheme vλv^{\lambda} and the value process VV of the American option, and derive a convergence rate in the space 𝒮2\mathcal{S}^{2}.

###### Lemma 3.1.

For any λ∈(0,1]\lambda\in(0,1], the following estimate holds:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (vtλ−Vt)2+∫tTd​[mλ−M]s\displaystyle(v^{\lambda}\_{t}-V\_{t})^{2}+\int\_{t}^{T}d[m^{\lambda}-M]\_{s} | ≤2​eT−t​𝔼​[∫tT(vsλ−Ps)−​𝑑As|ℱt]+2​eT−t​λ2​(T−t).\displaystyle\leq 2e^{T-t}{\mathbb{E}}\!\left[\int\_{t}^{T}(v^{\lambda}\_{s}-P\_{s})^{-}\,dA\_{s}\,\bigg|\,{\mathcal{F}}\_{t}\right]+2e^{T-t}\lambda^{2}(T-t). |  | (3.9) |

###### Proof.

Recall from ([2.1](https://arxiv.org/html/2602.18062v1#S2.E1 "In 2 Preliminaries ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) that the value process admits the Doob–Meyer decomposition
V=M−AV=M-A, where MM is a martingale and AA is a predictable, increasing process of finite variation satisfying the Skorokhod minimality condition

|  |  |  |
| --- | --- | --- |
|  | ∫0T(Ps−−Vs−)​𝑑As=0.\int\_{0}^{T}(P\_{s-}-V\_{s-})\,dA\_{s}=0. |  |

For notational convenience, we denote the positive and negative parts of the driver of vλv^{\lambda} by

|  |  |  |
| --- | --- | --- |
|  | gsλ​(vλ)±:=λ​(e(Ps−vsλ)/λ−1)±,Gtλ,±​(vλ):=∫0tgsλ​(vλ)±​𝑑s.g^{\lambda}\_{s}(v^{\lambda})^{\pm}:=\lambda\big(e^{(P\_{s}-v^{\lambda}\_{s})/\lambda}-1\big)^{\pm},\qquad G^{\lambda,\pm}\_{t}(v^{\lambda}):=\int\_{0}^{t}g^{\lambda}\_{s}(v^{\lambda})^{\pm}\,ds. |  |

Let β≥0\beta\geq 0. Applying Itô’s formula to eβ​t​(vtλ−Vt)2e^{\beta t}(v^{\lambda}\_{t}-V\_{t})^{2} and using the reflected BSDE representation ([2.1](https://arxiv.org/html/2602.18062v1#S2.E1 "In 2 Preliminaries ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​t​(vtλ−Vt)2+∫tTeβ​s​d​[Nλ]s\displaystyle e^{\beta t}(v^{\lambda}\_{t}-V\_{t})^{2}+\int\_{t}^{T}e^{\beta s}\,d[N^{\lambda}]\_{s} | =−2​∫tTeβ​s​(vsλ−Vs)​𝑑Nsλ\displaystyle=-2\int\_{t}^{T}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})\,dN^{\lambda}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​∫tTeβ​s​(vsλ−Vs)​d​(Gsλ,+−As)\displaystyle\quad+2\int\_{t}^{T}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})\,d(G^{\lambda,+}\_{s}-A\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −2​∫tTeβ​s​(vsλ−Vs)​gsλ​(vλ)−​𝑑s\displaystyle\quad-2\int\_{t}^{T}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})g^{\lambda}\_{s}(v^{\lambda})^{-}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −β​∫tTeβ​s​(vsλ−Vs)2​𝑑s,\displaystyle\quad-\beta\int\_{t}^{T}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})^{2}\,ds, |  |

where we have set Nλ:=mλ−MN^{\lambda}:=m^{\lambda}-M.
We now focus on the reflection term. By decomposing it and using that
∫0T(Vs−Ps)​𝑑As=0\int\_{0}^{T}(V\_{s}-P\_{s})\,dA\_{s}=0, together with the facts that V≥PV\geq P and that the increasing process Gλ,+G^{\lambda,+} grows only on the set {vλ≤P}\{v^{\lambda}\leq P\}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫tTeβ​s​(vsλ−Vs)​d​(Gλ,+−A)s\displaystyle\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})d(G^{\lambda,+}-A)\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tTeβ​s​(vsλ−Ps)​𝑑Gsλ,++∫tTeβ​s​(Ps−Vs)​𝑑Gsλ,+−∫tTeβ​s​(vsλ−Ps)​𝑑As+∫tTeβ​s​(Vs−Ps)​𝑑As\displaystyle=\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-P\_{s})dG^{\lambda,+}\_{s}+\int^{T}\_{t}e^{\beta s}(P\_{s}-V\_{s})dG^{\lambda,+}\_{s}-\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-P\_{s})dA\_{s}+\int^{T}\_{t}e^{\beta s}(V\_{s}-P\_{s})dA\_{s} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤eβ​T​∫tT(vsλ−Ps)−​𝑑As.\displaystyle\leq e^{\beta T}\int^{T}\_{t}(v^{\lambda}\_{s}-P\_{s})^{-}dA\_{s}. |  |

Combining the above estimates yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​t​(vtλ−Vt)2\displaystyle e^{\beta t}(v^{\lambda}\_{t}-V\_{t})^{2} | ≤−2​∫tTeβ​s​(vsλ−Vs)​𝑑Nsλ+2​eβ​T​∫tT(vsλ−Ps)−​𝑑As\displaystyle\leq-2\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})dN^{\lambda}\_{s}+2e^{\beta T}\int^{T}\_{t}(v^{\lambda}\_{s}-P\_{s})^{-}dA\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​∫tTeβ​s​(vsλ−Vs)​[−gsλ​(vsλ)−]​𝑑s−β​∫tTeβ​s​(vsλ−Vs)2​𝑑s.\displaystyle\qquad+2\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})[-g^{\lambda}\_{s}(v^{\lambda}\_{s})^{-}]ds-\beta\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})^{2}ds. |  |

Taking ℱt{\mathcal{F}}\_{t}-conditional expectations and applying Young’s inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​t​(vtλ−Vt)2\displaystyle e^{\beta t}(v^{\lambda}\_{t}-V\_{t})^{2} | ≤2​eβ​T​𝔼​[∫tT(vsλ−Ps)−​𝑑As|ℱt]+𝔼​[∫tTeβ​s​(vsλ−Vs)2+eβ​s​[gsλ​(vsλ)−]2​d​s|ℱt]\displaystyle\leq 2e^{\beta T}\mathbb{E}[\int^{T}\_{t}(v^{\lambda}\_{s}-P\_{s})^{-}dA\_{s}|{\mathcal{F}}\_{t}]+\mathbb{E}[\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})^{2}+e^{\beta s}[g^{\lambda}\_{s}(v^{\lambda}\_{s})^{-}]^{2}\,\,ds|{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −β​𝔼​[∫tTeβ​s​(vsλ−Vs)2​𝑑s|ℱt]−2​𝔼​[∫tTeβ​s​(vsλ−Vs)​𝑑Nsλ|ℱt].\displaystyle\qquad-\beta{\mathbb{E}}[\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})^{2}ds|{\mathcal{F}}\_{t}]-2{\mathbb{E}}[\int^{T}\_{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})dN^{\lambda}\_{s}\,|\,{\mathcal{F}}\_{t}]. |  |

We conclude by choosing β=1\beta=1, noting that

|  |  |  |
| --- | --- | --- |
|  | [gsλ​(x)−]2=λ2​(ex/λ−1)2​𝟏{x<0}≤λ2,[g^{\lambda}\_{s}(x)^{-}]^{2}=\lambda^{2}(e^{x/\lambda}-1)^{2}\mathbf{1}\_{\{x<0\}}\leq\lambda^{2}, |  |

and observing that the stochastic integral
(∫0teβ​s​(vsλ−Vs)​𝑑Nsλ)t≥0\left(\int\_{0}^{t}e^{\beta s}(v^{\lambda}\_{s}-V\_{s})\,dN^{\lambda}\_{s}\right)\_{t\geq 0}
is a uniformly integrable martingale by the Burkholder-Davis-Gundy inequality. This yields the estimate ([3.9](https://arxiv.org/html/2602.18062v1#S3.E9 "In Lemma 3.1. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")).
∎

We now turn to the derivation of an explicit convergence rate of vλv^{\lambda} towards VV as λ↓0\lambda\downarrow 0. In view of Lemma [3.1](https://arxiv.org/html/2602.18062v1#S3.Thmlem1 "Lemma 3.1. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), it is sufficient to control the term

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫tT(vsλ−Ps)−​𝑑As|ℱt].{\mathbb{E}}\!\left[\int\_{t}^{T}(v^{\lambda}\_{s}-P\_{s})^{-}\,dA\_{s}\,\bigg|\,{\mathcal{F}}\_{t}\right]. |  |

Obtaining sharp bounds for this quantity is a well-known difficulty in the analysis of penalisation schemes for reflected BSDEs and, in general, requires additional structural assumptions on the payoff process PP.

We therefore begin with an auxiliary lemma, whose proof follows the approach pioneered by El Karoui *et al.* [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)] and is inspired by the recent work of Gobet and Wang [[17](https://arxiv.org/html/2602.18062v1#bib.bib17)].

###### Lemma 3.2.

There exists positive constant C<∞C<\infty such that for any λ∈(0,1]\lambda\in(0,1]

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(∫tT(vsλ−Ps)−​𝑑s)2|ℱt]≤C​(λ−λ​ln⁡λ)2.\displaystyle\mathbb{E}\Big[\Big(\int^{T}\_{t}(v^{\lambda}\_{s}-P\_{s})^{-}ds\Big)^{2}\Big|{\mathcal{F}}\_{t}\Big]\leq C(\lambda-\lambda\ln\lambda)^{2}. |  |

###### Proof.

By applying the mean value theorem to the function x↦λ​(ex/λ−1)x\mapsto\lambda\big(e^{x/\lambda}-1\big) at the point x=ε>0x=\varepsilon>0, we obtain the following lower bound for the driver:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(ex/λ−1)\displaystyle\lambda(e^{x/\lambda}-1) | ≥λ​(e(x∧ϵ)/λ−1)+(x−ϵ)+​eϵ/λ\displaystyle\geq\lambda(e^{(x\wedge\epsilon)/\lambda}-1)+(x-\epsilon)^{+}e^{\epsilon/\lambda} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥λ​(e(x∧ϵ)/λ−1)−ϵ​eϵ/λ+x+​eϵ/λ,\displaystyle\geq\lambda(e^{(x\wedge\epsilon)/\lambda}-1)-\epsilon e^{\epsilon/\lambda}+x^{+}e^{\epsilon/\lambda}, |  |

where, in the last inequality, we have used the elementary bound (x−ε)+≥x+−ε(x-\varepsilon)^{+}\geq x^{+}-\varepsilon.

Motivated by this estimate, and for fixed λ≤1\lambda\leq 1, we introduce the following BSDE with a Lipschitz continuous driver:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xtλ\displaystyle X^{\lambda}\_{t} | =PT−(MTX−MtX)+∫tTfλ,ϵ​(Ps−Xsλ)​𝑑s+∫tT(Ps−Xsλ)+​γλ,ϵ​𝑑s,\displaystyle=P\_{T}-(M^{X}\_{T}-M^{X}\_{t})+\int\_{t}^{T}f\_{\lambda,\epsilon}(P\_{s}-X^{\lambda}\_{s})ds+\int\_{t}^{T}(P\_{s}-X^{\lambda}\_{s})^{+}\gamma^{\lambda,\epsilon}ds, |  | (3.10) |

where fλ,ϵ​(x):=λ​(e(x∧ϵ)/λ−1)−ϵ​eϵ/λf\_{\lambda,\epsilon}(x):=\lambda(e^{(x\wedge\epsilon)/\lambda}-1)-\epsilon e^{\epsilon/\lambda} and γλ,ϵ:=eϵ/λ\gamma^{\lambda,\epsilon}:=e^{\epsilon/\lambda}. By the comparison theorem for BSDEs (see Theorem 3.4 in [[26](https://arxiv.org/html/2602.18062v1#bib.bib26)]), it then follows that for all t∈[0,T]t\in[0,T] and all λ∈(0,1]\lambda\in(0,1]

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtλ≤vtλ≤Vt,a.s.X^{\lambda}\_{t}\leq v^{\lambda}\_{t}\leq V\_{t},\quad a.s. |  | (3.11) |

By arguments similar to those used in Lemma [3.1](https://arxiv.org/html/2602.18062v1#S3.Thmlem1 "Lemma 3.1. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Xtλ)2+∫tTd​[MX]s\displaystyle(X^{\lambda}\_{t})^{2}+\int^{T}\_{t}d[M^{X}]\_{s} | =PT2−∫tT2​Xsλ​𝑑MsX+∫tT2​Xs​fλ,ϵ​(Ps−Xsλ)​𝑑s+∫tT2​Xsλ​(Ps−Xsλ)+​γλ,ϵ​𝑑s\displaystyle=P^{2}\_{T}-\int^{T}\_{t}2X^{\lambda}\_{s}dM^{X}\_{s}+\int^{T}\_{t}2X\_{s}f\_{\lambda,\epsilon}(P\_{s}-X^{\lambda}\_{s})ds+\int^{T}\_{t}2X^{\lambda}\_{s}(P\_{s}-X^{\lambda}\_{s})^{+}\gamma^{\lambda,\epsilon}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤PT2−∫tT2​Xsλ​𝑑MsX+∫tT2​Xsλ​fλ,ϵ​(Ps−Xsλ)​𝑑s+∫tT2​Ps​(Ps−Xsλ)+​γλ,ϵ​𝑑s\displaystyle\leq P^{2}\_{T}-\int^{T}\_{t}2X^{\lambda}\_{s}dM^{X}\_{s}+\int^{T}\_{t}2X^{\lambda}\_{s}f\_{\lambda,\epsilon}(P\_{s}-X^{\lambda}\_{s})ds+\int^{T}\_{t}2P\_{s}(P\_{s}-X^{\lambda}\_{s})^{+}\gamma^{\lambda,\epsilon}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤PT2−∫tT2​Xsλ​𝑑MsX+∫tT(Xsλ)2​𝑑s+∫tT(fλ,ϵ​(Ps−Xsλ))2​𝑑s+2α​(sup0≤s≤TPs)2\displaystyle\leq P^{2}\_{T}-\int^{T}\_{t}2X^{\lambda}\_{s}dM^{X}\_{s}+\int^{T}\_{t}(X^{\lambda}\_{s})^{2}ds+\int^{T}\_{t}(f\_{\lambda,\epsilon}(P\_{s}-X^{\lambda}\_{s}))^{2}ds+\frac{2}{\alpha}(\sup\_{0\leq s\leq T}P\_{s})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​α​(∫tT(Ps−Xsλ)+​γλ,ϵ​𝑑s)2.\displaystyle\quad+2\alpha\Big(\int^{T}\_{t}(P\_{s}-X^{\lambda}\_{s})^{+}\gamma^{\lambda,\epsilon}ds\Big)^{2}. |  |

where the last inequality follows from Young’s inequality, for an arbitrary α>0\alpha>0.

Applying Jensen’s and Cauchy–Schwarz inequalities yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[(∫tT(Ps−Xsλ)+​γλ,ϵ​𝑑s)2]\displaystyle{\mathbb{E}}\Big[\Big(\int^{T}\_{t}(P\_{s}-X^{\lambda}\_{s})^{+}\gamma^{\lambda,\epsilon}ds\Big)^{2}\Big] | ≤4​𝔼​[(Xtλ)2]+4​𝔼​[PT2]+4​𝔼​[[MX]T−[MX]t]\displaystyle\leq 4{\mathbb{E}}[(X^{\lambda}\_{t})^{2}]+4{\mathbb{E}}[P\_{T}^{2}]+4{\mathbb{E}}[[M^{X}]\_{T}-[M^{X}]\_{t}] |  | (3.12) |
|  |  | +4​T​∫tT𝔼​[(fλ,ϵ​(Ps−Xsλ))2]​𝑑s.\displaystyle\qquad+4T\int^{T}\_{t}{\mathbb{E}}[(f\_{\lambda,\epsilon}(P\_{s}-X^{\lambda}\_{s}))^{2}]ds. |  |

Choosing α\alpha such that 2​α=1122\alpha=\tfrac{1}{12}, and using the bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | (fλ,ϵ​(x))2≤2​λ2​(e(x∧ϵ)/λ−1)2+2​ϵ2​e2​ϵ/λ≤2​λ2​e2​ϵ/λ+2​ϵ2​e2​ϵ/λ,(f\_{\lambda,\epsilon}(x))^{2}\leq 2\lambda^{2}(e^{(x\wedge\epsilon)/\lambda}-1)^{2}+2\epsilon^{2}e^{2\epsilon/\lambda}\leq 2\lambda^{2}e^{2\epsilon/\lambda}+2\epsilon^{2}e^{2\epsilon/\lambda}, |  | (3.13) |

we deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | 23​𝔼​[(Xtλ)2]+23​𝔼​[∫tTd​[MX]t]\displaystyle\frac{2}{3}{\mathbb{E}}[(X^{\lambda}\_{t})^{2}]+\frac{2}{3}{\mathbb{E}}\Big[\int^{T}\_{t}d[M^{X}]\_{t}\Big] | ≤C​(1+∫tT𝔼​[(Xsλ)2]​𝑑s+∫tT𝔼​[(fλ,ϵ​(Ps−Xsλ))2]​𝑑s)\displaystyle\leq C\left(1+\int^{T}\_{t}{\mathbb{E}}[(X^{\lambda}\_{s})^{2}]ds+\int^{T}\_{t}{\mathbb{E}}[(f\_{\lambda,\epsilon}(P\_{s}-X^{\lambda}\_{s}))^{2}]ds\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(1+(λ2+ϵ2)​e2​ϵ/λ+∫tT𝔼​[(Xsλ)2]​𝑑s).\displaystyle\leq C\left(1+(\lambda^{2}+\epsilon^{2})e^{2\epsilon/\lambda}+\int^{T}\_{t}{\mathbb{E}}[(X^{\lambda}\_{s})^{2}]ds\right). |  |

An application of Grönwall’s lemma then yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup0≤t≤T𝔼​[|Xtλ|2]≤C​(1+(λ2+ϵ2)​e2​ϵ/λ),\sup\_{0\leq t\leq T}{\mathbb{E}}[|X^{\lambda}\_{t}|^{2}]\leq C\big(1+(\lambda^{2}+\epsilon^{2})e^{2\epsilon/\lambda}\big), |  | (3.14) |

and consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[[MX]T]≤C​(1+(λ2+ϵ2)​e2​ϵ/λ).{\mathbb{E}}[[M^{X}]\_{T}]\leq C\big(1+(\lambda^{2}+\epsilon^{2})e^{2\epsilon/\lambda}\big). |  | (3.15) |

Combining ([3.11](https://arxiv.org/html/2602.18062v1#S3.E11 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) with ([3.12](https://arxiv.org/html/2602.18062v1#S3.E12 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), ([3.13](https://arxiv.org/html/2602.18062v1#S3.E13 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), ([3.14](https://arxiv.org/html/2602.18062v1#S3.E14 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) and ([3.15](https://arxiv.org/html/2602.18062v1#S3.E15 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0T(vsλ−Ps)−​𝑑s)2]≤𝔼​[(∫0T(Xsλ−Ps)−​𝑑s)2]≤C​(e−2​ϵ/λ+λ2+ϵ2).\displaystyle\mathbb{E}\Big[\Big(\int^{T}\_{0}(v^{\lambda}\_{s}-P\_{s})^{-}ds\Big)^{2}\Big]\leq{\mathbb{E}}\Big[\Big(\int\_{0}^{T}(X^{\lambda}\_{s}-P\_{s})^{-}ds\Big)^{2}\Big]\leq C(e^{-2\epsilon/\lambda}+\lambda^{2}+\epsilon^{2}). |  | (3.16) |

Next, we choose ϵ\epsilon so as to optimize the convergence rate. Observe first that the constraint
ϵ/λ≥1\epsilon/\lambda\geq 1 is necessary, since this quantity must diverge as λ→0\lambda\to 0.
Consequently, the two dominant (slowest-decaying) terms are e−2​ϵ/λe^{-2\epsilon/\lambda} and ϵ2\epsilon^{2}.
Balancing these contributions leads us to impose ϵ=e−ϵ/λ\epsilon=e^{-\epsilon/\lambda}
or, equivalently, ln⁡ϵ=−ϵ/λ\ln\epsilon=-\epsilon/\lambda. This transcendental equation does not admit a closed-form solution, and we therefore seek an accurate approximation.

Rewriting the above identity yields

|  |  |  |
| --- | --- | --- |
|  | −ϵλ=ln⁡(λ)+ln⁡ϵλ−ln⁡1.\displaystyle-\frac{\epsilon}{\lambda}=\ln(\lambda)+\ln\frac{\epsilon}{\lambda}-\ln 1. |  |

By the mean value theorem, there exists some c∈[1,ϵ/λ]c\in[1,\epsilon/\lambda],

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ\displaystyle\epsilon | =−λ​1c​(ϵλ−1)−λ​ln⁡(λ)=−1c​(ϵ−λ)−λ​ln⁡(λ)\displaystyle=-\lambda\frac{1}{c}(\frac{\epsilon}{\lambda}-1)-\lambda\ln(\lambda)=-\frac{1}{c}(\epsilon-\lambda)-\lambda\ln(\lambda) |  |

which gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ=(11+1/c)​(λc−λ​ln⁡λ)≤λ−λ​ln⁡λ.\displaystyle\epsilon=\left(\frac{1}{1+1/c}\right)\left(\frac{\lambda}{c}-\lambda\ln\lambda\right)\leq\lambda-\lambda\ln\lambda. |  | (3.17) |

Motivated by this estimate, we adopt the approximate choice ϵ=λ−λ​ln⁡λ\epsilon=\lambda-\lambda\ln\lambda which clearly satisfies ϵ≥λ\epsilon\geq\lambda for all λ∈(0,1]\lambda\in(0,1].
Substituting this value into ([3.16](https://arxiv.org/html/2602.18062v1#S3.E16 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) readily gives the desired upper-bound.
∎

As in the classical penalization approach, deriving the convergence rate towards the value VV of the American option with respect to the temperature parameter λ\lambda requires additional
regularity assumptions, which we now state.

###### Assumption 3.2.

The filtration 𝔽{\mathbb{F}} is generated by a Brownian motion, and the payoff process PP admits the
generalized semimartingale decomposition

|  |  |  |
| --- | --- | --- |
|  | Pt=P0+∫0tUs​𝑑s+∫0tVs​𝑑Ws+Ht,P\_{t}=P\_{0}+\int\_{0}^{t}U\_{s}\,ds+\int\_{0}^{t}V\_{s}\,dW\_{s}+H\_{t}, |  |

where U,V∈𝒮2U,V\in\mathcal{S}^{2}, and HH is a continuous, non-decreasing process satisfying
H0=0H\_{0}=0 and HT∈L2H\_{T}\in L^{2}.

Under Assumption [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), it follows from Proposition 4.2 and Remark 4.3 in [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)]
that the reflection process AA is absolutely continuous with respect to Lebesgue measure.
Moreover, its density is uniformly dominated, in the sense that d​At≤κt​d​tdA\_{t}\leq\kappa\_{t}\,dt, with κ:=U−\kappa:=U^{-}.
As an illustration, the standard American put option satisfies Assumption [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options");
see Remark 2.3 in [[17](https://arxiv.org/html/2602.18062v1#bib.bib17)].

We are now in a position to state the main convergence result with respect to the temperature
parameter λ\lambda. Under the additional regularity imposed by Assumption [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), the
penalised value process converges to the American option value at an explicit rate in the
𝒮2\mathcal{S}^{2}-norm.

###### Theorem 3.2.

Under Assumption [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), there exists a positive constant CC such that, for any λ∈(0,1]\lambda\in\!(0,1],

|  |  |  |
| --- | --- | --- |
|  | ‖vλ−V‖𝒮2≤C​(λ−λ​ln⁡λ).\|v^{\lambda}-V\|\_{\mathcal{S}^{2}}\leq C(\lambda-\lambda\ln\lambda). |  |

###### Proof.

The proof relies on the absolute continuity of the reflection process ensured by
Assumption [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"). More precisely, by Proposition 4.2 and Remark 4.3 in
El Karoui et al. [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)], the increasing process AA satisfies
d​At≤κt​d​tdA\_{t}\leq\kappa\_{t}\,dt, where κt≤Ut−\kappa\_{t}\leq U\_{t}^{-}. It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T(Ysλ−Ps)−​𝑑As]\displaystyle{\mathbb{E}}[\int^{T}\_{0}(Y^{\lambda}\_{s}-P\_{s})^{-}dA\_{s}] | ≤𝔼​[sup0≤t≤Tκt​∫0T(Ysλ−Ps)−​𝑑s]\displaystyle\leq{\mathbb{E}}[\sup\_{0\leq t\leq T}\kappa\_{t}\int^{T}\_{0}(Y^{\lambda}\_{s}-P\_{s})^{-}ds] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[(sup0≤t≤Tκt)2]12​𝔼​[|∫0T(Ysλ−Ps)−​𝑑s|2]12.\displaystyle\leq{\mathbb{E}}[\big(\sup\_{0\leq t\leq T}\kappa\_{t}\big)^{2}]^{\frac{1}{2}}{\mathbb{E}}[|\int^{T}\_{0}(Y^{\lambda}\_{s}-P\_{s})^{-}ds\big|^{2}]^{\frac{1}{2}}. |  |

where the second inequality follows from the Cauchy-Schwarz inequality.
The conclusion then follows by combining Lemma [3.1](https://arxiv.org/html/2602.18062v1#S3.Thmlem1 "Lemma 3.1. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options") and Lemma [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmlem2 "Lemma 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options").
∎

As indicated by the two-sided bounds in ([3.11](https://arxiv.org/html/2602.18062v1#S3.E11 "In Proof. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")), the process vλv^{\lambda} provides a lower bound for the American option value VV. We now complement this result by deriving a convergence rate for a corresponding upper bound, based on the dual representation of Rogers [[30](https://arxiv.org/html/2602.18062v1#bib.bib30)]. To this end, we introduce the process uλu^{\lambda} defined by

|  |  |  |
| --- | --- | --- |
|  | utλ:=𝔼​[supt≤σ≤T(Pσ−mσλ)|ℱt]+mtλ,u^{\lambda}\_{t}:={\mathbb{E}}\!\left[\sup\_{t\leq\sigma\leq T}\bigl(P\_{\sigma}-m^{\lambda}\_{\sigma}\bigr)\,\big|\,{\mathcal{F}}\_{t}\right]+m^{\lambda}\_{t}, |  |

where mλm^{\lambda} denotes the martingale component arising in the entropy-regularized penalization scheme ([3.3](https://arxiv.org/html/2602.18062v1#S3.E3 "In 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")). Our goal is to quantify the rate at which uλu^{\lambda} converges to VV.

###### Theorem 3.3.

Under Assumption [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmhyp2 "Assumption 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), there exists a constant C<∞C<\infty such that, for any λ∈(0,1]\lambda\in(0,1],

|  |  |  |
| --- | --- | --- |
|  | ‖uλ−V‖𝒮2≤C​(λ−λ​ln⁡λ).\|u^{\lambda}-V\|\_{\mathcal{S}^{2}}\leq C\bigl(\lambda-\lambda\ln\lambda\bigr). |  |

###### Proof.

The argument relies on the fact that V=M−AV=M-A dominates the payoff process PP, together with
the monotonicity of the reflection process AA. Indeed, for any t∈[0,T]t\in[0,T], Theorem 2.1 of Rogers [[30](https://arxiv.org/html/2602.18062v1#bib.bib30)] gives utλ≥Vtu^{\lambda}\_{t}\geq V\_{t}, and we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤utλ−Vt\displaystyle 0\leq u^{\lambda}\_{t}-V\_{t} | =𝔼​[supt≤σ≤T(Pσ−mσλ)|ℱt]+mtλ−Vt\displaystyle={\mathbb{E}}\!\left[\sup\_{t\leq\sigma\leq T}(P\_{\sigma}-m^{\lambda}\_{\sigma})\,\big|\,{\mathcal{F}}\_{t}\right]+m^{\lambda}\_{t}-V\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[supt≤σ≤T(Mσ−mσλ)|ℱt]−At+mtλ−Vt\displaystyle\leq{\mathbb{E}}\!\left[\sup\_{t\leq\sigma\leq T}(M\_{\sigma}-m^{\lambda}\_{\sigma})\,\big|\,{\mathcal{F}}\_{t}\right]-A\_{t}+m^{\lambda}\_{t}-V\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[sup0≤s≤T|Ms−msλ||ℱt]+|mtλ−Mt|.\displaystyle\leq{\mathbb{E}}\!\left[\sup\_{0\leq s\leq T}|M\_{s}-m^{\lambda}\_{s}|\,\big|\,{\mathcal{F}}\_{t}\right]+|m^{\lambda}\_{t}-M\_{t}|. |  |

For notational convenience, we set Nλ:=mλ−MN^{\lambda}:=m^{\lambda}-M and define

|  |  |  |
| --- | --- | --- |
|  | ntλ:=𝔼​[sup0≤s≤T|Nsλ||ℱt].n^{\lambda}\_{t}:={\mathbb{E}}\!\left[\sup\_{0\leq s\leq T}|N^{\lambda}\_{s}|\,\big|\,{\mathcal{F}}\_{t}\right]. |  |

Applying Jensen’s inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | (utλ−Vt)2\displaystyle(u^{\lambda}\_{t}-V\_{t})^{2} | ≤2​|ntλ|2+2​|Ntλ|2≤2​(sup0≤t≤T|ntλ|)2+2​(sup0≤t≤T|Ntλ|)2.\displaystyle\leq 2|n^{\lambda}\_{t}|^{2}+2|N^{\lambda}\_{t}|^{2}\leq 2\Big(\sup\_{0\leq t\leq T}|n^{\lambda}\_{t}|\Big)^{2}+2\Big(\sup\_{0\leq t\leq T}|N^{\lambda}\_{t}|\Big)^{2}. |  |

Using repeated applications of the Burkholder-Davis-Gundy inequality together with
Itô’s isometry, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sup0≤t≤T(utλ−Vt)2]\displaystyle{\mathbb{E}}[\sup\_{0\leq t\leq T}(u^{\lambda}\_{t}-V\_{t})^{2}] | ≤2​𝔼​[|sup0≤t≤T|ntλ||2]+2​𝔼​[|sup0≤t≤T|Ntλ||2].\displaystyle\leq 2{\mathbb{E}}[|\sup\_{0\leq t\leq T}|n^{\lambda}\_{t}||^{2}]+2{\mathbb{E}}[|\sup\_{0\leq t\leq T}|N^{\lambda}\_{t}||^{2}]. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​C​𝔼​[[nλ]T]+2​C​𝔼​[[Nλ]T].\displaystyle\leq 2C{\mathbb{E}}[[n^{\lambda}]\_{T}]+2C{\mathbb{E}}[[N^{\lambda}]\_{T}]. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​C​𝔼​[|nTλ|2]+2​C​𝔼​[[Nλ]T]\displaystyle=2C{\mathbb{E}}[|n^{\lambda}\_{T}|^{2}]+2C{\mathbb{E}}[[N^{\lambda}]\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​C​𝔼​[|sup0≤t≤T|Ntλ||2]+2​C​𝔼​[[Nλ]T]≤4​C​𝔼​[[mλ−M]T].\displaystyle\leq 2C{\mathbb{E}}[|\sup\_{0\leq t\leq T}|N^{\lambda}\_{t}||^{2}]+2C{\mathbb{E}}[[N^{\lambda}]\_{T}]\leq 4C{\mathbb{E}}[[m^{\lambda}-M]\_{T}]. |  |

The conclusion follows from Lemma [3.1](https://arxiv.org/html/2602.18062v1#S3.Thmlem1 "Lemma 3.1. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options") and Lemma [3.2](https://arxiv.org/html/2602.18062v1#S3.Thmlem2 "Lemma 3.2. ‣ 3.2 Convergence to the American Option ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options").
∎

### 3.3 Policy Improvement Algorithm

In this section, we introduce the PIA associated with the
entropy-regularized formulation and analyze its convergence properties. The proposed approach
is inspired by the methodology developed in [[7](https://arxiv.org/html/2602.18062v1#bib.bib7)], and relies on an iterative procedure
alternating between policy evaluation and policy improvement. At each iteration, the policy
evaluation step consists in solving a linear BSDE,
while the policy improvement step is obtained by maximizing, in closed form, the corresponding
regularized Hamiltonian.

To this end, for a fixed temperature parameter λ>0\lambda>0, we define the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(s,x,πs)\displaystyle G(s,x,\pi\_{s}) | :=(Ps−x)​πs−λ​(πs​ln⁡πs−πs+1),\displaystyle:=(P\_{s}-x)\pi\_{s}-\lambda\bigl(\pi\_{s}\ln\pi\_{s}-\pi\_{s}+1\bigr), |  |

and denote by

|  |  |  |
| --- | --- | --- |
|  | πs∗​(x):=arg⁡maxπ⁡G​(s,x,πs)=exp⁡(Ps−xλ).\pi\_{s}^{\*}(x):=\arg\max\_{\pi}G(s,x,\pi\_{s})=\exp\!\left(\frac{P\_{s}-x}{\lambda}\right). |  |

Let π0∈Π\pi^{0}\in\Pi be an arbitrary initial policy, and define the corresponding initial value
function by vtλ,0:=𝔼​[PT∣ℱt]v^{\lambda,0}\_{t}:={\mathbb{E}}[P\_{T}\mid{\mathcal{F}}\_{t}] for t∈[0,T]t\in[0,T]. Given the current iterate
(πm,vλ,m)∈Π×𝒟(\pi^{m},v^{\lambda,m})\in\Pi\times\mathcal{D}, the (m+1)(m+1)-th policy improvement step is
constructed as follows. The policy is first updated according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | πsm+1:=πs∗​(vsλ,m)=exp⁡(Ps−vsλ,mλ),\pi^{m+1}\_{s}:=\pi^{\*}\_{s}\!\left(v^{\lambda,m}\_{s}\right)=\exp\!\left(\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}\right), |  | (3.18) |

and the corresponding value function vλ,m+1v^{\lambda,m+1} is then obtained as the unique solution
to the linear BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | vtλ,m+1=PT−(mTλ,m+1−mtλ,m+1)+∫tTG​(s,vsλ,m+1,πsm+1)​𝑑s,t∈[0,T].v^{\lambda,m+1}\_{t}=P\_{T}-\bigl(m^{\lambda,m+1}\_{T}-m^{\lambda,m+1}\_{t}\bigr)+\int\_{t}^{T}G\bigl(s,v^{\lambda,m+1}\_{s},\pi^{m+1}\_{s}\bigr)\,ds,\quad t\in[0,T]. |  | (3.19) |

We note that, for each m≥0m\geq 0, the process vλ,mv^{\lambda,m} is well defined and belongs to
𝒟\mathcal{D}. Moreover, since by construction,

|  |  |  |
| --- | --- | --- |
|  | G​(s,vsλ,m,πsm)≤G​(s,vsλ,m,πsm+1)a.s.,G\bigl(s,v^{\lambda,m}\_{s},\pi^{m}\_{s}\bigr)\leq G\bigl(s,v^{\lambda,m}\_{s},\pi^{m+1}\_{s}\bigr)\quad a.s., |  |

the comparison theorem for BSDEs (see e.g. Theorem 3.4 in [[26](https://arxiv.org/html/2602.18062v1#bib.bib26)]) implies that the sequence
{vλ,m}m≥0\{v^{\lambda,m}\}\_{m\geq 0} is non-decreasing. That is, for all integer mm and all t∈[0,T]t\in[0,T]

|  |  |  |
| --- | --- | --- |
|  | vtλ,m≤vtλ,m+1a.s..v^{\lambda,m}\_{t}\leq v^{\lambda,m+1}\_{t}\quad a.s.. |  |

We now establish the convergence rate of the above policy improvement scheme. The following result
shows that, for a fixed temperature parameter λ\lambda, the sequence of value functions
{vλ,m}m≥0\{v^{\lambda,m}\}\_{m\geq 0} converges monotonically to the entropy-regularized value function
vλv^{\lambda} at a factorial rate.

###### Theorem 3.4.

There exists C<∞C<\infty such that for any λ∈(0,1]\lambda\in(0,1] and any t∈[0,T)t\in[0,T),

|  |  |  |
| --- | --- | --- |
|  | 0≤vtλ−vtλ,m≤(C​T)mm!​𝔼​[sup0≤s≤T(vsλ,1−vsλ,0)|ℱt].\displaystyle 0\leq v\_{t}^{\lambda}-v\_{t}^{\lambda,m}\leq\frac{(CT)^{m}}{m!}\mathbb{E}\Big[\sup\_{0\leq s\leq T}(v^{\lambda,1}\_{s}-v^{\lambda,0}\_{s})\,\Big|\,{\mathcal{F}}\_{t}\Big]. |  |

###### Proof.

The driver at step m+1m+1 is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(s,vsλ,m+1,πsm+1)\displaystyle G(s,v\_{s}^{\lambda,m+1},\pi\_{s}^{m+1}) | =(Ps−vsλ,m+1)​πsm+1−λ​(πsm+1​ln⁡(πsm+1)−πsm+1+1)\displaystyle=(P\_{s}-v\_{s}^{\lambda,m+1})\pi^{m+1}\_{s}-\lambda(\pi^{m+1}\_{s}\ln(\pi^{m+1}\_{s})-\pi^{m+1}\_{s}+1) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ePs−vsλ,mλ​(vsλ,m−vsλ,m+1)+λ​(ePs−vsλ,mλ−1).\displaystyle=e^{\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}}(v\_{s}^{\lambda,m}-v\_{s}^{\lambda,m+1})+\lambda(e^{\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}}-1). |  | (3.20) |

Moreover, by Assumption [3.1](https://arxiv.org/html/2602.18062v1#S3.Thmhyp1 "Assumption 3.1. ‣ 3.1 Definition of the entropy-regularized penalization scheme ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options") the payoff PP is non-negative and bounded and therefore the initial value vλ,0v^{\lambda,0} is also bounded. Hence, by Theorem 3.3 in [[26](https://arxiv.org/html/2602.18062v1#bib.bib26)] we deduce that vλ,1v^{\lambda,1} is non-negative and thus vλ,m≥0v^{\lambda,m}\geq 0 for all mm. In view of this, the difference of the drivers can be estimated as

|  |  |  |
| --- | --- | --- |
|  | G​(s,vsλ,m+1,πsm+1)−G​(s,vsλ,m,πsm)\displaystyle G(s,v\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})-G(s,v\_{s}^{\lambda,m},\pi\_{s}^{m}) |  |
|  |  |  |
| --- | --- | --- |
|  | =ePs−vsλ,mλ​(vsλ,m−vsλ,m+1)−ePs−vsλ,m−1λ​(vsλ,m−1−vsλ,m)+λ​(ePs−vsλ,mλ−ePs−vsλ,m−1λ)\displaystyle=e^{\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}}(v\_{s}^{\lambda,m}-v\_{s}^{\lambda,m+1})-e^{\frac{P\_{s}-v^{\lambda,m-1}\_{s}}{\lambda}}(v^{\lambda,m-1}\_{s}-v^{\lambda,m}\_{s})+\lambda(e^{\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}}-e^{\frac{P\_{s}-v^{\lambda,m-1}\_{s}}{\lambda}}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤ePs−vsλ,m−1λ​(vsλ,m−vsλ,m−1)\displaystyle\leq e^{\frac{P\_{s}-v^{\lambda,m-1}\_{s}}{\lambda}}(v^{\lambda,m}\_{s}-v^{\lambda,m-1}\_{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​(vsλ,m−vsλ,m−1),\displaystyle\leq C(v^{\lambda,m}\_{s}-v^{\lambda,m-1}\_{s}), |  |

where CC is a constant independent of mm. By the previous inequality and the Fubini-Tonelli theorem, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤vtλ,m+1−vtλ,m\displaystyle 0\leq v^{\lambda,m+1}\_{t}-v^{\lambda,m}\_{t} | =𝔼​[∫tT(G​(s,vsλ,m+1,πsm+1)−G​(s,vsλ,m,πsm))​𝑑s|ℱt]\displaystyle=\mathbb{E}[\int^{T}\_{t}\Big(G(s,v\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})-G(s,v\_{s}^{\lambda,m},\pi\_{s}^{m})\Big)\,ds\,|\,{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​𝔼​[∫tT(vtm−1λ,m−vtm−1λ,m−1)​𝑑tm−1|ℱt]\displaystyle\leq C\mathbb{E}[\int^{T}\_{t}(v^{\lambda,m}\_{t\_{m-1}}-v^{\lambda,m-1}\_{t\_{m-1}})\,d{t\_{m-1}}\,|\,{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cm​𝔼​[∫tT∫tm−1T…​∫t1T(vt0λ,1−vt0λ,0)​𝑑t0​…​𝑑tm−2​𝑑tm−1|ℱt]\displaystyle\leq C^{m}\mathbb{E}[\int^{T}\_{t}\int^{T}\_{t\_{m-1}}\dots\int^{T}\_{t\_{1}}(v^{\lambda,1}\_{t\_{0}}-v^{\lambda,0}\_{t\_{0}})\,dt\_{0}\dots dt\_{m-2}dt\_{m-1}\,|\,{\mathcal{F}}\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(C​T)mm!​𝔼​[sup0≤s≤T(vsλ,1−vsλ,0)|ℱt].\displaystyle\leq\frac{(CT)^{m}}{m!}\mathbb{E}\big[\sup\_{0\leq s\leq T}(v^{\lambda,1}\_{s}-v^{\lambda,0}\_{s})\,\big|\,{\mathcal{F}}\_{t}\big]. |  |

On the other hand, by the mean value theorem G​(s,vsλ,m+1,πsm+1)≤λ​ePs−vsλ,m+1λG(s,v\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})\leq\lambda e^{\frac{P\_{s}-v\_{s}^{\lambda,m+1}}{\lambda}} and by similar computations we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤vtλ−vtλ,m+1\displaystyle 0\leq v^{\lambda}\_{t}-v^{\lambda,m+1}\_{t} | =𝔼​[∫tT(λ​(ePs−vsλλ−1)−G​(s,vsλ,m+1,πsm+1))​𝑑s|ℱt]\displaystyle=\mathbb{E}\Big[\int^{T}\_{t}\Big(\lambda(e^{\frac{P\_{s}-v\_{s}^{\lambda}}{\lambda}}-1)-G(s,v\_{s}^{\lambda,m+1},\pi\_{s}^{m+1})\Big)\,ds\,|\,{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫tT(λ​(ePs−vsλλ−ePs−vsλ,mλ)+ePs−vsλ,mλ​(vsλ,m+1−vsλ,m))​𝑑s|ℱt]\displaystyle=\mathbb{E}\Big[\int^{T}\_{t}\Big(\lambda(e^{\frac{P\_{s}-v\_{s}^{\lambda}}{\lambda}}-e^{\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}})+e^{\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}}(v\_{s}^{\lambda,m+1}-v\_{s}^{\lambda,m})\Big)\,ds\,|\,{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​𝔼​[∫tT(vsλ,m+1−vsλ,m)​𝑑s|ℱt]\displaystyle\leq C\mathbb{E}\Big[\int^{T}\_{t}(v\_{s}^{\lambda,m+1}-v\_{s}^{\lambda,m})\,ds\,|\,{\mathcal{F}}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(C​T)m+1(m+1)!​𝔼​[sup0≤s≤T(vsλ,1−vsλ,0)|ℱt].\displaystyle\leq\frac{(CT)^{m+1}}{(m+1)!}\mathbb{E}\big[\sup\_{0\leq s\leq T}(v^{\lambda,1}\_{s}-v^{\lambda,0}\_{s})\,\big|\,{\mathcal{F}}\_{t}\big]. |  |

This completes the proof.
∎

## 4 Numerical Experiments

We now turn to numerical experiments in order to illustrate the performance of the proposed iterative scheme and to assess its accuracy in practical settings.

Starting from an initial guess vλ,0>0v^{\lambda,0}>0, we observe that, in the presence of a non-zero interest rate, the sequence {vλ,m}m≥0\{v^{\lambda,m}\}\_{m\geq 0} satisfies at each iteration a linear BSDE of the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vtλ,m+1\displaystyle v^{\lambda,m+1}\_{t} | =PT−(mTλ,m+1−mtλ,m+1)+∫tT(G​(s,vsλ,m+1,πsm+1)−r​vsλ,m+1)​𝑑s,\displaystyle=P\_{T}-(m^{\lambda,m+1}\_{T}-m^{\lambda,m+1}\_{t})+\int\_{t}^{T}\Big(G(s,v^{\lambda,m+1}\_{s},\pi^{m+1}\_{s})-rv^{\lambda,m+1}\_{s}\Big)ds, |  | (4.1) |

where the function GG is defined in ([3.3](https://arxiv.org/html/2602.18062v1#S3.Ex64 "Proof. ‣ 3.3 Policy Improvement Algorithm ‣ 3 Entropy-Regularized Penalization Scheme ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) and r>0r>0 denotes the constant interest rate. It follows from ([4.1](https://arxiv.org/html/2602.18062v1#S4.E1 "In 4 Numerical Experiments ‣ A Monotone Limit Approach to Entropy‑Regularized American Options")) that, for any Δ​t≥0\Delta t\geq 0, the process vλ,m+1​tv^{\lambda,m+1}t satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | vtλ,m+1\displaystyle v^{\lambda,m+1}\_{t} | =𝔼​[e−∫tt+Δ​tasm​𝑑s​vt+Δ​tλ,m+1+∫tt+Δ​te−∫tsaum​𝑑u​bsm​𝑑s|ℱt].\displaystyle=\mathbb{E}\Big[e^{-\int^{t+\Delta t}\_{t}a^{m}\_{s}ds}v^{\lambda,m+1}\_{t+\Delta t}+\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}a^{m}\_{u}\,du}\,b^{m}\_{s}\,ds\,\Big|\,\mathcal{F}\_{t}\Big]. |  |

For small Δ​t\Delta t, a first-order approximation over the interval [t,t+Δ​t][t,t+\Delta t] then yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | vtλ,m+1\displaystyle v^{\lambda,m+1}\_{t} | ≈e−atm​Δ​t​𝔼​[vt+Δ​tλ,m+1|ℱt]+btmatm​(1−e−atm​Δ​t).\displaystyle\approx e^{-a\_{t}^{m}\Delta t}{\mathbb{E}}\left[v^{\lambda,m+1}\_{t+\Delta t}\Big|{\mathcal{F}}\_{t}\right]+\frac{b^{m}\_{t}}{a^{m}\_{t}}(1-e^{-a^{m}\_{t}\Delta t}). |  |

Here, the processes ama^{m} and bmb^{m} are defined for t∈[0,T]t\in[0,T] by

|  |  |  |
| --- | --- | --- |
|  | atm=ePt−vtλ,mλ+r,btm=ePs−vtλ,mλ​vsλ,m+λ​(ePt−vtλ,mλ−1),t∈[0,T].a^{m}\_{t}=e^{\frac{P\_{t}-v^{\lambda,m}\_{t}}{\lambda}}+r,\qquad b^{m}\_{t}=e^{\frac{P\_{s}-v^{\lambda,m}\_{t}}{\lambda}}\,v^{\lambda,m}\_{s}+\lambda\Big(e^{\frac{P\_{t}-v^{\lambda,m}\_{t}}{\lambda}}-1\Big),\quad t\in[0,T]. |  |

An important feature of this formulation is that vλ,m+1v^{\lambda,m+1} can be computed explicitly in terms of vλ,mv^{\lambda,m}.

The above discussion suggests the following iterative scheme. For a given positive integer NN, we let Δ​t=T/N\Delta t=T/N and define the uniform time grid tk=k​Δ​tt\_{k}=k\Delta t, k=0,⋯,Nk=0,\cdots,N. We then let v¯tkλ,0=𝔼​[e−r​(T−t)​PT|ℱtk]\bar{v}^{\lambda,0}\_{t\_{k}}=\mathbb{E}[e^{-r(T-t)}P\_{T}|\mathcal{F}\_{t\_{k}}], k=0,⋯,Nk=0,\cdots,N, which corresponds to the price of the European option. Then, for any integer mm and any k=N−1,⋯,0k=N-1,\cdots,0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯tkλ,m+1\displaystyle\bar{v}^{\lambda,m+1}\_{t\_{k}} | =e−a¯tkm​Δ​t​𝔼​[v¯tk+1λ,m+1|ℱtk]+b¯tkma¯tkm​(1−e−a¯tkm​Δ​t),\displaystyle=e^{-\bar{a}\_{t\_{k}}^{m}\Delta t}{\mathbb{E}}\left[\bar{v}^{\lambda,m+1}\_{t\_{k+1}}\Big|{\mathcal{F}}\_{t\_{k}}\right]+\frac{\bar{b}^{m}\_{t\_{k}}}{\bar{a}^{m}\_{t\_{k}}}(1-e^{-\bar{a}^{m}\_{t\_{k}}\Delta t}), |  |

where the process a¯m\bar{a}^{m} and b¯m\bar{b}^{m} are obtained from ama^{m} and bmb^{m} by replacing vλ,mv^{\lambda,m} by its approximation v¯λ,m\bar{v}^{\lambda,m}. The conditional expectation can be estimated using least squares regression. In the example below we regress on the 13 basis functions suggested by Andersen and Broadie [[1](https://arxiv.org/html/2602.18062v1#bib.bib1)].

We test the above scheme on the symmetric case of an American max-call option. To be specific, given the strike price KK, we recall that the price at time 0 of a max-call option is defined by

|  |  |  |
| --- | --- | --- |
|  | supτ∈𝒯0,T𝔼​[e−r​τ​(max1≤i≤d⁡Sτi−K)+].\sup\_{\tau\in\mathcal{T}\_{0,T}}\mathbb{E}\!\left[e^{-r\tau}\Big(\max\_{1\leq i\leq d}S\_{\tau}^{i}-K\Big)^{+}\right]. |  |

We assume that the underlying assets follow a dd-dimensional Black–Scholes model with dividends:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sti=s0i​exp⁡((r−δ−σ2/2)​t+σ​Wti),i=1,…,d,S\_{t}^{i}=s\_{0}^{i}\exp\big((r-\delta-\sigma^{2}/2)t+\sigma W\_{t}^{i}\big),\quad i=1,\dots,d, |  | (4.2) |

where s0is\_{0}^{i} denotes the initial values, rr the risk-free rate, δ\delta the constant dividend yield, σ\sigma the constant volatility, and W=(W1,⋯,Wd)W=(W^{1},\cdots,W^{d}) a standard dd-dimensional Brownian motion.

Below, we present our results and compare them to prices computed using the classical penalization approach of El Karoui *et al.* [[16](https://arxiv.org/html/2602.18062v1#bib.bib16)] and a binomial tree approximation.

Table [1](https://arxiv.org/html/2602.18062v1#S4.T1 "Table 1 ‣ 4 Numerical Experiments ‣ A Monotone Limit Approach to Entropy‑Regularized American Options") indicates that the PIA scheme delivers stable and accurate approximations of the American max-call price. As the parameter λ\lambda decreases, the PIA values converge monotonically and become very close to those obtained with the classical penalization or binomial approaches, thereby confirming the consistency of the method. For λ=0.001\lambda=0.001, the discrepancy between PIA and classical penalization is negligible across all tested initial prices. Moreover, the resulting prices are in good agreement with the binomial benchmark, with deviations remaining small and comparable to those observed for the classical penalization scheme. Overall, these results suggest that the proposed PIA provides a reliable and numerically efficient procedure for the valuation of American-style derivatives.

| S0S\_{0} | λ\lambda | PIA | Classical penalization | Binomial |
| --- | --- | --- | --- | --- |
| 90 | 0.1 | 8.063 | 8.208 | 8.296 |
| 90 | 0.01 | 8.380 | 8.424 | 8.296 |
| 90 | 0.001 | 8.428 | 8.460 | 8.296 |
| 100 | 0.1 | 14.017 | 14.040 | 14.211 |
| 100 | 0.01 | 14.362 | 14.357 | 14.211 |
| 100 | 0.001 | 14.412 | 14.408 | 14.211 |
| 110 | 0.1 | 21.613 | 21.494 | 21.799 |
| 110 | 0.01 | 21.971 | 21.914 | 21.799 |
| 110 | 0.001 | 22.021 | 21.980 | 21.799 |

Table 1: Price at time 0 of the American max-call option with parameters: d=2d=2, s01=s02=s0s^{1}\_{0}=s^{2}\_{0}=s\_{0}, K=100K=100, r=0.05r=0.05, σ=0.2\sigma=0.2, δ=0.1\delta=0.1, T=3T=3 and N=100N=100 and 100000100000 sample paths. The PIA is computed over 2000 iterations.

###### Remark 4.1.

In the above implementation, we notice that for vsλ,m<Psv\_{s}^{\lambda,m}<P\_{s} we have

|  |  |  |
| --- | --- | --- |
|  | vtλ,m+1≈btmatm​(1−e−atm​Δ​t)≈vtλ,m+λ.v^{\lambda,m+1}\_{t}\approx\frac{b^{m}\_{t}}{a^{m}\_{t}}(1-e^{-a^{m}\_{t}\Delta t})\approx v\_{t}^{\lambda,m}+\lambda. |  |

Namely, the optimal policy (or stopping intensity), which is of the exponential form given by
exp⁡(Ps−vsλ,mλ),\exp\!\left(\frac{P\_{s}-v^{\lambda,m}\_{s}}{\lambda}\right),
can significantly impact the update speed and the convergence of the value function when λ\lambda is small and vλ,m<Pv^{\lambda,m}<P. Consequently, for small λ\lambda, the choice of initialization can heavily influence the computational time required for the scheme to converge. For the results presented in Table [1](https://arxiv.org/html/2602.18062v1#S4.T1 "Table 1 ‣ 4 Numerical Experiments ‣ A Monotone Limit Approach to Entropy‑Regularized American Options"), we observe this behaviour for the cases of λ=0.01\lambda=0.01 and λ=0.001\lambda=0.001.

To overcome this, we consider scheduling λ\lambda by first employing large λ\lambda to prioritize convergence speed, and subsequently transition to a small λ\lambda to ensure accuracy. Namely, for the case of λ=0.001\lambda=0.001 we sequentially run the PIA for λ=0.1,0.05,0.01\lambda=0.1,0.05,0.01 and finally λ=0.001\lambda=0.001 for 500500 iterations each.

## References

* [1]

  Andersen, L., & Broadie, M. (2004). Primal-dual simulation algorithm for pricing multidimensional American options. Management Science, 50(9), 1222–1234.
* [2]

  Becker, S., Cheridito, P., & Jentzen, A. (2019). Deep optimal stopping. Journal of Machine Learning Research, 20, 74.
* [3]

  Becker, S., Cheridito, P., Jentzen, A., & Welti, T. (2021). Solving high-dimensional optimal stopping problems using deep learning. European Journal of Applied Mathematics, 32, 470-514.
* [4]

  Becker, S., Cheridito, P., & Jentzen, A. (2020). Pricing and hedging American-style options with deep learning. Journal of Risk and Financial Management, 13(7), 158.
* [5]

  Broadie, M., & Glasserman, P. (2004). A stochastic mesh method for pricing high dimensional American options. Journal of Computational Finance, 7, 35-72.
* [6]

  Chee, D., Frikha, N., & Li, L. (2025). An entropy regularized BSDE approach to Bermudan options and games. arXiv preprint arXiv:2509.18747. <https://arxiv.org/abs/2509.18747>
* [7]

  Chee, D., Frikha, N., & Li, L. (2026). Entropy-regularized penalization schemes for American options and reflected BSDEs with singular generators. Working Paper.
* [8]

  Dellacherie, C., & Meyer, P. A. (1980). Probabilités et potentiel. Chap. V-VIII. Hermann.
* [9]

  Dai, M., Dong, Y., Jia, Y., & Zhou, X. (2023). Learning Merton’s strategies in an incomplete market: Recursive entropy regularization and biased Gaussian exploration. arXiv:2312.11797 [math.OC]. Retrieved from https://arxiv.org/abs/2312.11797
* [10]

  Dai, M., & Dong, Y. (2024). Learning an optimal investment policy with transaction costs via a randomized Dynkin game. SSRN Working Paper. Retrieved from https://ssrn.com/abstract=4871712
* [11]

  Dai, M., Sun, Y., Xu, Z. Q., & Zhou, X. Y. (2024). Learning to optimally stop a diffusion process. arXiv preprint arXiv:2408.09242. <https://arxiv.org/abs/2408.09242>
* [12]

  Dai, M., & Dong, Y. (2024). Learning an optimal investment policy with transaction costs via a randomized Dynkin game. SSRN. <https://ssrn.com/abstract=4871712>
* [13]

  Dong, Y. (2024). Randomized optimal stopping problem in continuous time and reinforcement learning algorithm. SIAM Journal on Control and Optimization, 62(3), 1590–1614.
* [14]

  Dong, Y., & Zheng, H. (2025). Extended HJB equation for mean–variance stopping problem: Vanishing regularization method. arXiv preprint arXiv:2510.24128, <https://arxiv.org/abs/2510.24128>
* [15]

  Dianetti, J., Ferrari, G., & Xu, R. (2024). Exploratory optimal stopping: A singular control formulation. arXiv preprint arXiv:2408.09335. <https://arxiv.org/abs/2408.09335>
* [16]

  El Karoui, N., Kapoudjian, C., Pardoux, E., Peng, S., & Quenez, M. C. (1997). Reflected solutions of backward SDEs, and related obstacle problems for PDEs. Annals of Probability, 25(2), 702-737.
* [17]

  Gobet, E., & Wang, W. (2026). Improved Convergence Rate for Reflected BSDEs by Penalization Method. Applied Mathematics & Optimization, 93(10).
* [18]

  Grigorova, M., Imkeller, P., Offen, E., Ouknine, Y., & Quenez, M. C. (2017). Reflected BSDEs when the obstacle is not right-continuous and optimal stopping. Ann. Appl. Probab, 27(5), 3153-3188.
* [19]

  Gyöngy, I., & Šiška, D. (2008). On randomized stopping. Bernoulli, 14(2), 352–361.
* [20]

  Hamadène, S., & Ouknine, Y. (2016). Reflected backward SDEs with general jumps. Theory of Probability & Its Applications, 60(2), 263–280.
* [21]

  Huang, Y., Li, M., Yu, X., & Zhou, Z. (2025). Continuous-time reinforcement learning for optimal switching over multiple regimes. arXiv:2512.04697 <https://arxiv.org/abs/2512.04697v2>
* [22]

  Jia, B., Wang, L., & Wong, H. Y. (2024). Machine learning of surrender: Optimality and humanity. Journal of Risk and Insurance, 91(4), 915–942.
* [23]

  Lepeltier, J. P., Matoussi, A., & Xu, M. (2005). Reflected backward stochastic differential equations under monotonicity and general increasing growth conditions. Advances in Applied Probability, 37, 134–159.
* [24]

  Longstaff, F. A., & Schwartz, E. S. (2001). Valuing American options by simulation: A simple least-squares approach. Review of Financial Studies, 14(1), 113–147.
* [25]

  Maingueneau, A. M. (1978). Temps d’arrêt optimaux et théorie générale. In C. Dellacherie, P. A. Meyer, & M. Weil (Eds.), Séminaire de Probabilités XII, Lecture Notes in Mathematics (Vol. 649, pp. 457–467). Springer.
* [26]

  Øksendal, B., & Zhang, T. (2012). Backward stochastic differential equations with respect to general filtrations and applications to insider finance. Communications on Stochastic Analysis, 6(4), Article 13.
* [27]

  Peng, S. (1999). Monotonic limit theorem of BSDE and nonlinear decomposition theorem of Doob–Meyers type. Probability Theory and Related Fields, 113, 473-499.
* [28]

  Soner, H. M., & Tissot-Daguette, V. (2025). Stopping times of boundaries: Relaxation and continuity. SIAM Journal on Control and Optimization, 63(4), 2835–2855.
* [29]

  Reppen, A. M., Soner, H. M., & Tissot-Daguette, V. (2025). Neural optimal stopping boundary. Mathematical Finance, 35, 441–469. https://doi.org/10.1111/mafi.12450
* [30]

  Rogers, L. C. G. (2002). Monte Carlo valuation of American options. Mathematical Finance, 12(3), 271-286.
* [31]

  Tang, W., Zhang, P. Y., & Zhou, X. Y. (2023). Exploratory HJB equations and their convergence. SIAM Journal on Control and Optimization, 61(2), 789–823.
* [32]

  Wang, H., Zariphopoulou, T., & Zhou, X. Y. (2020). Reinforcement learning in continuous time and space: A stochastic control approach. Journal of Machine Learning Research, 21, 198–1–198–34.