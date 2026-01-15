---
authors:
- Masaaki Fukasawa
doc_id: arxiv:2601.09324v1
family_id: arxiv:2601.09324
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Martingale expansion for stochastic volatility
url_abs: http://arxiv.org/abs/2601.09324v1
url_html: https://arxiv.org/html/2601.09324v1
venue: arXiv q-fin
version: 1
year: 2026
---


Masaaki Fukasawa
  
Graduate School of Engineering Science
  
The University of Osaka
  
560-8531 Japan

###### Abstract

The martingale expansion provides a refined approximation to the marginal distributions of martingales beyond the normal approximation implied by the martingale central limit theorem. We develop a martingale expansion framework specifically suited to continuous stochastic volatility models. Our approach accommodates both small volatility‑of‑volatility and fast mean‑reversion models, yielding first‑order perturbation expansions under essentially minimal conditions.

## 1 Introduction

Stochastic volatility (SV) models constitute a central class of continuous‑time asset price models in which the instantaneous variance of returns is itself governed by an additional stochastic process. Unlike the classical Black–Scholes framework, which assumes constant volatility, SV models allow volatility to evolve randomly over time, thereby capturing a range of empirically observed features of financial markets, including volatility clustering, heavy‑tailed return distributions, and pronounced implied‑volatility smiles and skews.

Formally, an SV model specifies the joint dynamics of an asset price process
SS and its latent spot variance process VV, typically through a system of coupled stochastic differential equations. The spot variance process VV is often mean‑reverting and may be correlated with the asset‑price shocks, a feature that enables the model to reproduce leverage effects observed in equity markets. Prominent examples include the Heston model, in which VV follows a square‑root diffusion, and the SABR model, widely used in interest‑rate markets due to a closed form approximation formula for the implied volatility.

The flexibility afforded by stochastic volatility has made SV models indispensable in modern derivative pricing and risk management. They provide a more realistic representation of market dynamics and yield option prices that align more closely with observed implied‑volatility surfaces. At the same time, the introduction of a latent volatility factor complicates both analytical tractability and statistical inference, motivating a substantial literature on approximation methods, asymptotic expansions, and efficient numerical schemes.

Consider an abstract SV model with zero interest rates

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=Vt​d​Bt,Bt=ρ​Wt+1−ρ2​Wt⟂\frac{\mathrm{d}S\_{t}}{S\_{t}}=\sqrt{V\_{t}}\mathrm{d}B\_{t},\ \ B\_{t}=\rho W\_{t}+\sqrt{1-\rho^{2}}W^{\perp}\_{t} |  | (1) |

for an asset price process SS,
where (W,W⟂)(W,W^{\perp}) is a 22-dimensional standard Brownian motion on a filtered probability space (,,𝖯,{}t)(\Omega,\px@ScrF,\mathsf{P},\{{}\_{t}\}),
ρ∈(−1,1)\rho\in(-1,1),
and VV is a nonnegative cadlag process adapted to a smaller filtration {}t\{{}\_{t}\}
to which WW is also adapted while W⟂W^{\perp} is independent.
Suppose that V=VϵV=V^{\epsilon} depends on a parameter ϵ>0\epsilon>0 and
as ϵ→0\epsilon\to 0,

|  |  |  |
| --- | --- | --- |
|  | \ilimits@0T​Vtϵ​d​t−vϵ\intslop\ilimits@\_{0}^{T}V^{\epsilon}\_{t}\mathrm{d}t-v^{\epsilon} |  |

converges to 0 in probability for a deterministic positive sequence vϵv^{\epsilon} with limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | v0:=limϵ→0vϵ>0.v^{0}:=\lim\_{\epsilon\to 0}v^{\epsilon}>0. |  | (2) |

Then S=SϵS=S^{\epsilon} also depends on ϵ\epsilon and
by the martingale central limit theorem,
log⁡ST=log⁡STϵ\log S\_{T}=\log S^{\epsilon}\_{T} converges in law to the normal distribution with mean
−v0/2-v^{0}/2 and variance v0v^{0}.
The model ([1](https://arxiv.org/html/2601.09324v1#S1.E1 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")) with small ϵ>0\epsilon>0 is close to the Black-Scholes model in this sense.

Since SV models generally do not admit closed-form expressions for derivative prices or hedging strategies, asymptotic expansions
with respect to ϵ\epsilon for various models of VϵV^{\epsilon}
have been extensively developed for both practical implementation and theoretical analysis. Examples include
small volatility-of-volatility models, e.g. [[14](https://arxiv.org/html/2601.09324v1#bib.bib14), [5](https://arxiv.org/html/2601.09324v1#bib.bib5), [1](https://arxiv.org/html/2601.09324v1#bib.bib1), [4](https://arxiv.org/html/2601.09324v1#bib.bib4), [3](https://arxiv.org/html/2601.09324v1#bib.bib3)], where ϵ\epsilon is the volatility parameter of VϵV^{\epsilon}, and fast-mean-reverting models, e.g. [[8](https://arxiv.org/html/2601.09324v1#bib.bib8), [10](https://arxiv.org/html/2601.09324v1#bib.bib10), [13](https://arxiv.org/html/2601.09324v1#bib.bib13)],
where VϵV^{\epsilon} is ergodic and a certain negative power of ϵ\epsilon is the time scale parameter of VϵV^{\epsilon}.

In [[9](https://arxiv.org/html/2601.09324v1#bib.bib9)], the author introduced a unified framework for computing and validating first-order asymptotic expansions, based on Yoshida’s martingale expansion theory [[17](https://arxiv.org/html/2601.09324v1#bib.bib17), [18](https://arxiv.org/html/2601.09324v1#bib.bib18)] combined with a partial Malliavin calculus.
In the present paper, we propose an alternative approach that is more direct and elementary, and which in particular establishes the validity of the first-order expansion under weaker and essentially minimal conditions.

The martingale expansion was first formulated by Mykland [[15](https://arxiv.org/html/2601.09324v1#bib.bib15), [16](https://arxiv.org/html/2601.09324v1#bib.bib16)] for twice continuously differentiable test functions using Itô’s formula, and then by Yoshida [[17](https://arxiv.org/html/2601.09324v1#bib.bib17), [18](https://arxiv.org/html/2601.09324v1#bib.bib18)] for a general test function under a non-degeneracy condition on Malliavin covariances.
In [[9](https://arxiv.org/html/2601.09324v1#bib.bib9)], we relied on the condition
|ρ|<1|\rho|<1 that provides a smoothness of the distribution of STS\_{T}, admitting an effective application of the partial Malliavin calculus to ensure the required non-degeneracy.
In the present paper, we directly utilize a smoothness property due to |ρ|<1|\rho|<1 to bypass the Malliavin calculus.

## 2 Results

Here we state the main results of the paper. All the proofs are deferred to Section [4](https://arxiv.org/html/2601.09324v1#S4 "4 Proofs ‣ Martingale expansion for stochastic volatility").
Let T>0T>0 be fixed and

|  |  |  |
| --- | --- | --- |
|  | (Xϵ,Yϵ)=(1vϵ​\ilimits@0T​d​StSt,1ϵ​(\ilimits@0T​Vtϵ​d​t−vϵ)).(X^{\epsilon},Y^{\epsilon})=\left(\frac{1}{\sqrt{v^{\epsilon}}}\intslop\ilimits@\_{0}^{T}\frac{\mathrm{d}S\_{t}}{S\_{t}},\frac{1}{\epsilon}\left(\intslop\ilimits@\_{0}^{T}V^{\epsilon}\_{t}\mathrm{d}t-v^{\epsilon}\right)\right). |  |

###### Theorem 1

If YϵY^{\epsilon} is uniformly integrable and if
(Xϵ,Yϵ)(X^{\epsilon},Y^{\epsilon}) converges in law to such (X,Y)(X,Y)
that x↦𝖤​[Y|X=x]x\mapsto\mathsf{E}[Y|X=x] is twice continuously differentiable
with

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim|x|→∞𝖤​[Y|X=x]​ϕ​(x)=lim|x|→∞dd​x​(𝖤​[Y|X=x]​ϕ​(x))=0\lim\_{|x|\to\infty}\mathsf{E}[Y|X=x]\phi(x)=\lim\_{|x|\to\infty}\frac{\mathrm{d}}{\mathrm{d}x}(\mathsf{E}[Y|X=x]\phi(x))=0 |  | (3) |

as ϵ→0\epsilon\to 0,
then for any bounded Borel function ff,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[f​(STϵ)]=\ilimits@​f​(S0​exp⁡{vϵ​x−vϵ2})​ϕϵ​(x)​d​x+o​(ϵ),\mathsf{E}[f(S^{\epsilon}\_{T})]=\intslop\ilimits@f\left(S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}\right)\phi^{\epsilon}(x)\mathrm{d}x+o(\epsilon), |  | (4) |

where

|  |  |  |
| --- | --- | --- |
|  | ϕϵ​(x)=ϕ​(x)+ϵ2​vϵ​dd​x​(𝖤​[Y|X=x]​ϕ​(x))+ϵ2​vϵ​d2d​x2​(𝖤​[Y|X=x]​ϕ​(x))\phi^{\epsilon}(x)=\phi(x)+\frac{\epsilon}{2\sqrt{v^{\epsilon}}}\frac{\mathrm{d}}{\mathrm{d}x}(\mathsf{E}[Y|X=x]\phi(x))+\frac{\epsilon}{2v^{\epsilon}}\frac{\mathrm{d}^{2}}{\mathrm{d}x^{2}}(\mathsf{E}[Y|X=x]\phi(x)) |  |

and ϕ\phi is the standard normal density function.

###### Remark 1

By the martingale central limit theorem, the martingale marginal XϵX^{\epsilon} converges to the standard normal distribution if ϵ​Yϵ→0\epsilon Y^{\epsilon}\to 0. Therefore,
XX is always a standard normal random variable under the assumption.
As illustrated in [[9](https://arxiv.org/html/2601.09324v1#bib.bib9)], for both small volatility-of-volatility and fast-mean-reverting models, by suitably choosing vϵv^{\epsilon}, it is straight-forward to observe that (Xϵ,Yϵ)(X^{\epsilon},Y^{\epsilon}) converges in law to a 22-dimensional centered normal distribution. In such a case, YY is equal in law to 𝖤​[X​Y]​X+Z\mathsf{E}[XY]X+Z with a centered normal random variable ZZ with 𝖤​[X​Z]=0\mathsf{E}[XZ]=0. In particular, 𝖤​[Y|X=x]=𝖤​[X​Y]​x\mathsf{E}[Y|X=x]=\mathsf{E}[XY]x, and ([3](https://arxiv.org/html/2601.09324v1#S2.E3 "In Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")) is then trivial.

###### Corollary 1

Under the assumption of Theorem [1](https://arxiv.org/html/2601.09324v1#Thmthm1 "Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility"), for any K>0K>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[(K−STϵ)+]=pK​(S0,vϵ)+ϵ2​vϵ​K​𝖤​[Y|X=−d−​(S0,vϵ)]​ϕ​(−d−​(S0,vϵ))+o​(ϵ)=pK​(S0,vϵ)+ϵ​∂pK∂t​(S0,vϵ)​𝖤​[Y|X=−d−​(S0,vϵ)]+o​(ϵ)=pK​(S0,vϵ+ϵ​𝖤​[Y|X=−d−​(S0,vϵ)]+o​(ϵ)),\begin{split}\mathsf{E}[(K-S^{\epsilon}\_{T})\_{+}]&=p\_{K}(S\_{0},v^{\epsilon})+\frac{\epsilon}{2\sqrt{v^{\epsilon}}}K\mathsf{E}[Y|X=-d\_{-}(S\_{0},v^{\epsilon})]\phi(-d\_{-}(S\_{0},v^{\epsilon}))+o(\epsilon)\\ &=p\_{K}(S\_{0},v^{\epsilon})+\epsilon\frac{\partial p\_{K}}{\partial t}(S\_{0},v^{\epsilon})\mathsf{E}[Y|X=-d\_{-}(S\_{0},v^{\epsilon})]+o(\epsilon)\\ &=p\_{K}\left(S\_{0},v^{\epsilon}+\epsilon\mathsf{E}[Y|X=-d\_{-}(S\_{0},v^{\epsilon})]+o(\epsilon)\right),\end{split} |  | (5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | pK​(s,t)=K​(−d−​(s,t))−s​(−d+​(s,t)),d±​(s,t)=1t​(log⁡sK±t2)\begin{split}&p\_{K}(s,t)=K\Phi(-d\_{-}(s,t))-s\Phi(-d\_{+}(s,t)),\\ &d\_{\pm}(s,t)=\frac{1}{\sqrt{t}}\left(\log\frac{s}{K}\pm\frac{t}{2}\right)\end{split} |  | (6) |

and is the standard normal distribution function.

###### Remark 2

Note that pK​(s,t)p\_{K}(s,t) in ([6](https://arxiv.org/html/2601.09324v1#S2.E6 "In Corollary 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")) is the Black-Scholes put option price function with total variance tt.
The last expression of ([5](https://arxiv.org/html/2601.09324v1#S2.E5 "In Corollary 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")) implies that the Black-Scholes implied total variance vhat​(K)\hat{v}(K), which is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[(K−STϵ)+]=pK​(S0,vhat​(K)),\mathsf{E}[(K-S^{\epsilon}\_{T})\_{+}]=p\_{K}(S\_{0},\hat{v}(K)), |  | (7) |

is expanded as

|  |  |  |  |
| --- | --- | --- | --- |
|  | vhat​(K)=vϵ+ϵ​𝖤​[Y|X=−d−​(S0,vϵ)]+o​(ϵ).\hat{v}(K)=v^{\epsilon}+\epsilon\mathsf{E}[Y|X=-d\_{-}(S\_{0},v^{\epsilon})]+o(\epsilon). |  | (8) |

Although this is valid for any K>0K>0 as an asymptotic formula, taking into account how it is derived, we can expect its numerical accuracy only when

|  |  |  |
| --- | --- | --- |
|  | ∂pK∂t​(S0,vϵ)=K2​vϵ​ϕ​(−d−​(S0,vϵ))=S02​vϵ​ϕ​(−d+​(S0,vϵ))\frac{\partial p\_{K}}{\partial t}(S\_{0},v^{\epsilon})=\frac{K}{2\sqrt{v^{\epsilon}}}\phi(-d\_{-}(S\_{0},v^{\epsilon}))=\frac{S\_{0}}{2\sqrt{v^{\epsilon}}}\phi(-d\_{+}(S\_{0},v^{\epsilon})) |  |

is not too small, which is the case KK is near S0S\_{0}, i.e., around the at-the-money.
Since (X,Y)(X,Y) is the limit of (Xϵ,Yϵ(X^{\epsilon},Y^{\epsilon}), and so, is the limit of

|  |  |  |
| --- | --- | --- |
|  | (1vϵ​(log⁡STS0+vϵ2),Yϵ),\left(\frac{1}{\sqrt{v^{\epsilon}}}\left(\log\frac{S\_{T}}{S\_{0}}+\frac{v^{\epsilon}}{2}\right),Y^{\epsilon}\right), |  |

by formally replacing (X,Y)(X,Y) with the above, we reach a conceptually interesting formula

|  |  |  |
| --- | --- | --- |
|  | vhat​(K)≈𝖤​[\ilimits@0T​Vuϵ​d​u|ST=K].\hat{v}(K)\approx\mathsf{E}\left[\intslop\ilimits@\_{0}^{T}V^{\epsilon}\_{u}\mathrm{d}u\bigg|S\_{T}=K\right]. |  |

A rigorous validation of this formula is left for future research.

###### Remark 3

As is well-known,
differentiating the defining equation ([7](https://arxiv.org/html/2601.09324v1#S2.E7 "In Remark 2 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")) of the implied total variance in log moneyness,
we reach a volatility skew formula

|  |  |  |
| --- | --- | --- |
|  | ∂∂k​vhat​(S0​ek)=𝖯​[S0​ek>STϵ]−(−d−​(S0,vhat​(S0​ek)))ϕ​(−d−​(S0,vhat​(S0​ek))).\frac{\partial}{\partial k}\sqrt{\hat{v}(S\_{0}e^{k})}=\frac{\mathsf{P}[S\_{0}e^{k}>S^{\epsilon}\_{T}]-\Phi(-d\_{-}(S\_{0},\hat{v}(S\_{0}e^{k})))}{\phi(-d\_{-}(S\_{0},\hat{v}(S\_{0}e^{k})))}. |  |

Here, the derivative exists because under the current assumption of |ρ|<1|\rho|<1, log⁡STϵ\log S^{\epsilon}\_{T} follows a mixed normal distribution and in particular admits a density.
We have asymptotic expansions for both 𝖯​[K>STϵ]\mathsf{P}[K>S^{\epsilon}\_{T}] and
vhat​(K)\hat{v}(K) from ([4](https://arxiv.org/html/2601.09324v1#S2.E4 "In Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")) with f​(s)=1(−∞,K)​(s)f(s)=1\_{(-\infty,K)}(s) and ([8](https://arxiv.org/html/2601.09324v1#S2.E8 "In Remark 2 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")). Substituting those, we obtain

|  |  |  |
| --- | --- | --- |
|  | ∂∂k​vhat​(S0​ek)=ϵ2​vϵ​∂∂k​𝖤​[Y|X=kvϵ+vϵ2]+o​(ϵ).\frac{\partial}{\partial k}\sqrt{\hat{v}(S\_{0}e^{k})}=\frac{\epsilon}{2\sqrt{v^{\epsilon}}}\frac{\partial}{\partial k}\mathsf{E}\left[Y\bigg|X=\frac{k}{\sqrt{v^{\epsilon}}}+\frac{\sqrt{v^{\epsilon}}}{2}\right]+o(\epsilon). |  |

In the case 𝖤​[Y|X=x]=𝖤​[X​Y]​x\mathsf{E}[Y|X=x]=\mathsf{E}[XY]x mentioned in Remark [1](https://arxiv.org/html/2601.09324v1#Thmrem1 "Remark 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂k​vhat​(S0​ek)=ϵ2​vϵ​𝖤​[X​Y]+o​(ϵ).\frac{\partial}{\partial k}\sqrt{\hat{v}(S\_{0}e^{k})}=\frac{\epsilon}{2v^{\epsilon}}\mathsf{E}\left[XY\right]+o(\epsilon). |  | (9) |

###### Remark 4

In [[9](https://arxiv.org/html/2601.09324v1#bib.bib9)], a more abstract framework is given, which in particular incorporates jumps and time-dependent ρ\rho. For a continuous model ([1](https://arxiv.org/html/2601.09324v1#S1.E1 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")), it however requires a stronger moment conditions on (Xϵ,Yϵ)(X^{\epsilon},Y^{\epsilon}).

## 3 Example

In [[9](https://arxiv.org/html/2601.09324v1#bib.bib9)], we have already observed how the martingale expansion framework accommodates various perturbation models including small volatility-of-volatility and fast-mean-reverting models. Here, for an illustrative purpose, we take the small volatility-of-volatility expansion of a Bergomi-type model as an example.

Consider

|  |  |  |
| --- | --- | --- |
|  | Vtϵ=V0​(t)​exp⁡{ϵ​\slimits@i=1d​\ilimits@0t​ki​(t−s)​d​Wsi−ϵ22​\slimits@i=1d​\ilimits@0t​ki​(t−s)2​d​s}V^{\epsilon}\_{t}=V\_{0}(t)\exp\left\{\epsilon\sumop\slimits@\_{i=1}^{d}\intslop\ilimits@\_{0}^{t}k\_{i}(t-s)\mathrm{d}W^{i}\_{s}-\frac{\epsilon^{2}}{2}\sumop\slimits@\_{i=1}^{d}\intslop\ilimits@\_{0}^{t}k\_{i}(t-s)^{2}\mathrm{d}s\right\} |  |

with a small volatility-of-volatility parameter ϵ>0\epsilon>0,
where V0​(t)V\_{0}(t) is a deterministic positive continuous function,
(W1,…,Wd)(W^{1},\dots,W^{d}) is a dd-dimensional standard Brownian motion correlated with BB in ([1](https://arxiv.org/html/2601.09324v1#S1.E1 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")) as

|  |  |  |
| --- | --- | --- |
|  | d​⟨B,Wi⟩t=ρi​d​t,ρ:=\slimits@i=1d​ρi2∈(−1,1),\mathrm{d}\langle B,W^{i}\rangle\_{t}=\rho\_{i}\mathrm{d}t,\ \ \rho:=\sqrt{\sumop\slimits@\_{i=1}^{d}\rho\_{i}^{2}}\in(-1,1), |  |

and kik\_{i} are locally square integrable functions on [0,∞)[0,\infty).

The function t↦V0​(t)t\mapsto V\_{0}(t) is called the forward variance curve (at time 0), due to
V0​(t)=𝖤​[Vtϵ]V\_{0}(t)=\mathsf{E}[V^{\epsilon}\_{t}].
The case ki​(t)=ai​e−bi​tk\_{i}(t)=a\_{i}e^{-b\_{i}t}, ai,bi>0a\_{i},b\_{i}>0,
describes the Bergomi model (see [[6](https://arxiv.org/html/2601.09324v1#bib.bib6)]).
The case d=1d=1 with k1​(t)=a​tH−1/2k\_{1}(t)=at^{H-1/2}, a>0a>0, H∈(0,1/2)H\in(0,1/2), describes the rough Bergomi model proposed by [[3](https://arxiv.org/html/2601.09324v1#bib.bib3)].
In [[7](https://arxiv.org/html/2601.09324v1#bib.bib7), [11](https://arxiv.org/html/2601.09324v1#bib.bib11), [12](https://arxiv.org/html/2601.09324v1#bib.bib12)],
short-time (non-small volatility-of-volatility) expansions of the implied volatility and skew for this type of model are given.
We refer the reader to Section 8.3 of [[2](https://arxiv.org/html/2601.09324v1#bib.bib2)] for the difference between short-time and small volatility-of-volatility expansions.

Consistently to ([1](https://arxiv.org/html/2601.09324v1#S1.E1 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")), we have a decomposition

|  |  |  |
| --- | --- | --- |
|  | B=ρ​W+1−ρ2​W⟂,W=1ρ​\slimits@i=1d​ρi​Wi,W⟂=11−ρ2​(B−\slimits@i=1d​ρi​Wi)B=\rho W+\sqrt{1-\rho^{2}}W^{\perp},\ \ W=\frac{1}{\rho}\sumop\slimits@\_{i=1}^{d}\rho\_{i}W^{i},\ \ \ \ W^{\perp}=\frac{1}{\sqrt{1-\rho^{2}}}\left(B-\sumop\slimits@\_{i=1}^{d}\rho\_{i}W^{i}\right) |  |

with W⟂W^{\perp} being a standard Brownian motion independent of (W1,…,Wd)(W^{1},\dots,W^{d}).
We take as {}t\{{}\_{t}\} the natural filtration generated by (W1,…,Wd)(W^{1},\dots,W^{d}).

By taking

|  |  |  |
| --- | --- | --- |
|  | vϵ=𝖤​[\ilimits@0T​Vt​d​t]=\ilimits@0T​V0​(t)​d​t,v^{\epsilon}=\mathsf{E}\left[\intslop\ilimits@\_{0}^{T}V\_{t}\mathrm{d}t\right]=\intslop\ilimits@\_{0}^{T}V\_{0}(t)\mathrm{d}t, |  |

as ϵ→0\epsilon\to 0, we have

|  |  |  |
| --- | --- | --- |
|  | (Xϵ,Yϵ)=(1vϵ​\ilimits@tT​V0​(s)​d​Bs,\ilimits@0T​V0​(s)​\ilimits@0s​\slimits@i=1d​ki​(s−u)​d​Wui​d​s)+op​(1).(X^{\epsilon},Y^{\epsilon})=\left(\frac{1}{\sqrt{v^{\epsilon}}}\intslop\ilimits@\_{t}^{T}\sqrt{V\_{0}(s)}\mathrm{d}B\_{s},\intslop\ilimits@\_{0}^{T}V\_{0}(s)\intslop\ilimits@\_{0}^{s}\sumop\slimits@\_{i=1}^{d}k\_{i}(s-u)\mathrm{d}W^{i}\_{u}\mathrm{d}s\right)+o\_{p}(1). |  |

The leading term (X,Y)(X,Y) is centered normal
with covariance

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[X​Y]=𝖤​[1vϵ​\ilimits@0T​V0​(s)​d​Bs​\ilimits@0T​V0​(s)​\ilimits@0s​\slimits@i=1d​ki​(s−u)​d​Wui​d​s]=1vϵ​\slimits@i=1d​𝖤​[\ilimits@0T​V0​(s)​d​Bs​\ilimits@0T​\ilimits@sT​V0​(u)​ki​(u−s)​d​u​d​Wsi]=1vϵ​\ilimits@0T​V0​(s)​\ilimits@sT​V0​(u)​\slimits@i=1d​ρi​ki​(u−s)​d​u​d​s.\begin{split}\mathsf{E}[XY]&=\mathsf{E}\left[\frac{1}{\sqrt{v^{\epsilon}}}\intslop\ilimits@\_{0}^{T}\sqrt{V\_{0}(s)}\mathrm{d}B\_{s}\intslop\ilimits@\_{0}^{T}V\_{0}(s)\intslop\ilimits@\_{0}^{s}\sumop\slimits@\_{i=1}^{d}k\_{i}(s-u)\mathrm{d}W^{i}\_{u}\mathrm{d}s\right]\\ &=\frac{1}{\sqrt{v^{\epsilon}}}\sumop\slimits@\_{i=1}^{d}\mathsf{E}\left[\intslop\ilimits@\_{0}^{T}\sqrt{V\_{0}(s)}\mathrm{d}B\_{s}\intslop\ilimits@\_{0}^{T}\intslop\ilimits@\_{s}^{T}V\_{0}(u)k\_{i}(u-s)\mathrm{d}u\mathrm{d}W^{i}\_{s}\right]\\ &=\frac{1}{\sqrt{v^{\epsilon}}}\intslop\ilimits@\_{0}^{T}\sqrt{V\_{0}(s)}\intslop\ilimits@\_{s}^{T}V\_{0}(u)\sumop\slimits@\_{i=1}^{d}\rho\_{i}k\_{i}(u-s)\mathrm{d}u\mathrm{d}s.\end{split} |  |

The uniform integrability of YϵY^{\epsilon} can be easily shown by observing its boundedness in L2L^{2}. Since 𝖤​[Y|X=x]=𝖤​[X​Y]​x\mathsf{E}[Y|X=x]=\mathsf{E}[XY]x, all the assumptions of Theorem [1](https://arxiv.org/html/2601.09324v1#Thmthm1 "Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility") are satisfied. We have in particular ([9](https://arxiv.org/html/2601.09324v1#S2.E9 "In Remark 3 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")) with 𝖤​[X​Y]\mathsf{E}[XY] given above.

## 4 Proofs

### 4.1 Proof of Theorem [1](https://arxiv.org/html/2601.09324v1#Thmthm1 "Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")

i). Take δ∈(0,1−ρ2)\delta\in(0,1-\rho^{2}) and let

|  |  |  |
| --- | --- | --- |
|  | τ=inf{t≥0;ρ2​\ilimits@0t​Vsϵ​d​s≥(1−δ)​vϵ}.\tau=\inf\left\{t\geq 0;\rho^{2}\intslop\ilimits@\_{0}^{t}V^{\epsilon}\_{s}\mathrm{d}s\geq(1-\delta)v^{\epsilon}\right\}. |  |

Here we are going to show

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[f​(STϵ)]=𝖤​[f​(ST∧τϵ)]+o​(ϵ).\mathsf{E}[f(S^{\epsilon}\_{T})]=\mathsf{E}[f(S^{\epsilon}\_{T\wedge\tau})]+o(\epsilon). |  | (10) |

Since ff is bounded,

|  |  |  |
| --- | --- | --- |
|  | |𝖤​[f​(STϵ)]−𝖤​[f​(ST∧τϵ)]|≤2​\|​f​\|∞​𝖯​[τ≤T].|\mathsf{E}[f(S^{\epsilon}\_{T})]-\mathsf{E}[f(S^{\epsilon}\_{T\wedge\tau})]|\leq 2\|f\|\_{\infty}\mathsf{P}[\tau\leq T]. |  |

Then, we obtain ([10](https://arxiv.org/html/2601.09324v1#S4.E10 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")) from

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖯​[τ≤T]=𝖯​[ϵ​ρ2​Yϵ≥(1−δ−ρ2)​vϵ]≤ϵ​ρ2(1−δ−ρ2)​vϵ​𝖤​[|Yϵ|;|Yϵ|≥(1−δ−ρ2)​vϵϵ​ρ2],\begin{split}\mathsf{P}[\tau\leq T]&=\mathsf{P}[\epsilon\rho^{2}Y^{\epsilon}\geq(1-\delta-\rho^{2})v^{\epsilon}]\\ &\leq\frac{\epsilon\rho^{2}}{(1-\delta-\rho^{2})v^{\epsilon}}\mathsf{E}\left[|Y^{\epsilon}|;|Y^{\epsilon}|\geq\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}\right],\end{split} |  | (11) |

which is of o​(ϵ)o(\epsilon)
by the uniform integrability of YϵY^{\epsilon} and ([2](https://arxiv.org/html/2601.09324v1#S1.E2 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")).
  
ii).
Here we decompose 𝖤​[f​(ST∧τϵ)]\mathsf{E}[f(S^{\epsilon}\_{T\wedge\tau})] to extract its leading term.
Since W⟂W^{\perp} is independent of T, we have

|  |  |  |
| --- | --- | --- |
|  | 𝖤[f(ST∧τϵ)]=𝖤[𝖤[f(ST∧τϵ)|]T]=𝖤[p(ShatTϵ,(1−ρ2)\ilimits@0T∧τVsϵds)],\mathsf{E}[f(S^{\epsilon}\_{T\wedge\tau})]=\mathsf{E}[\mathsf{E}[f(S^{\epsilon}\_{T\wedge\tau})|{}\_{T}]]=\mathsf{E}\left[p\left(\hat{S}^{\epsilon}\_{T},(1-\rho^{2})\intslop\ilimits@\_{0}^{T\wedge\tau}V^{\epsilon}\_{s}\mathrm{d}s\right)\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | Shattϵ=S0​exp⁡{ρ​Ztϵ−ρ22​⟨Zϵ⟩t},Ztϵ=\ilimits@0t∧τ​Vsϵ​d​Ws.\hat{S}^{\epsilon}\_{t}=S\_{0}\exp\left\{\rho Z^{\epsilon}\_{t}-\frac{\rho^{2}}{2}\langle Z^{\epsilon}\rangle\_{t}\right\},\ \ Z^{\epsilon}\_{t}=\intslop\ilimits@\_{0}^{t\wedge\tau}\sqrt{V^{\epsilon}\_{s}}\mathrm{d}W\_{s}. |  |

and

|  |  |  |
| --- | --- | --- |
|  | p​(s,t)=\ilimits@​f​(s​exp⁡{t​x−t2})​ϕ​(x)​d​x.p(s,t)=\intslop\ilimits@f\left(s\exp\left\{\sqrt{t}x-\frac{t}{2}\right\}\right)\phi(x)\mathrm{d}x. |  |

Since pp solves the partial differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂p∂t=12​s2​∂2p∂s2,p​(s,0)=f​(s),\frac{\partial p}{\partial t}=\frac{1}{2}s^{2}\frac{\partial^{2}p}{\partial s^{2}},\ \ p(s,0)=f(s), |  | (12) |

putting

|  |  |  |
| --- | --- | --- |
|  | =uϵvϵ−ρ2\ilimits@0u∧τVtϵdt,{}^{\epsilon}\_{u}=v^{\epsilon}-\rho^{2}\intslop\ilimits@\_{0}^{u\wedge\tau}V^{\epsilon}\_{t}\mathrm{d}t, |  |

Itô’s formula gives

|  |  |  |
| --- | --- | --- |
|  | p(ShatTϵ,)Tϵ=p(S0,vϵ)+\ilimits@0T∂p∂s(Shatuϵ,)uϵdShatuϵ,p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})=p(S\_{0},v^{\epsilon})+\intslop\ilimits@\_{0}^{T}\frac{\partial p}{\partial s}(\hat{S}^{\epsilon}\_{u},{}^{\epsilon}\_{u})\mathrm{d}\hat{S}^{\epsilon}\_{u}, |  |

and so, noting ≥uϵδvϵ>0{}^{\epsilon}\_{u}\geq\delta v^{\epsilon}>0,

|  |  |  |
| --- | --- | --- |
|  | 𝖤[p(ShatTϵ,)Tϵ]=p(S0,vϵ).\mathsf{E}[p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})]=p(S\_{0},v^{\epsilon}). |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[f​(ST∧τϵ)]=p(S0,vϵ)+𝖤[p(ShatTϵ,(1−ρ2)\ilimits@0T∧τVuϵdu)−p(ShatTϵ,)Tϵ]=p(S0,vϵ)+𝖤[p(ShatTϵ,+TϵϵYhatϵ)−p(ShatTϵ,)Tϵ],\begin{split}&\mathsf{E}[f(S^{\epsilon}\_{T\wedge\tau})]\\ &=p(S\_{0},v^{\epsilon})+\mathsf{E}\left[p\left(\hat{S}^{\epsilon}\_{T},(1-\rho^{2})\intslop\ilimits@\_{0}^{T\wedge\tau}V^{\epsilon}\_{u}\mathrm{d}u\right)-p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})\right]\\ &=p(S\_{0},v^{\epsilon})+\mathsf{E}\left[p\left(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T}+\epsilon\hat{Y}^{\epsilon}\right)-p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})\right],\end{split} |  | (13) |

where

|  |  |  |
| --- | --- | --- |
|  | Yhatϵ=1ϵ​(\ilimits@0T∧τ​Vuϵ​d​u−vϵ)=Yϵ​1{τ>T}+(1−δ−ρ2)​vϵϵ​ρ2​1{τ≤T}.\hat{Y}^{\epsilon}=\frac{1}{\epsilon}\left(\intslop\ilimits@\_{0}^{T\wedge\tau}V^{\epsilon}\_{u}\mathrm{d}u-v^{\epsilon}\right)=Y^{\epsilon}1\_{\{\tau>T\}}+\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}1\_{\{\tau\leq T\}}. |  |

iii). Here we are going to show that Yhatϵ\hat{Y}^{\epsilon} is uniformly integrable.
By ([11](https://arxiv.org/html/2601.09324v1#S4.E11 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")),

|  |  |  |
| --- | --- | --- |
|  | supϵ>0𝖤​[(1−δ−ρ2)​vϵϵ​ρ2​1{τ≤T};(1−δ−ρ2)​vϵϵ​ρ2​1{τ≤T}≥K]≤sup{(1−δ−ρ2)​vϵϵ​ρ2​𝖯​[τ≤T];(1−δ−ρ2)​vϵϵ​ρ2≥K}≤sup{𝖤​[|Yϵ|;|Yϵ|≥(1−δ−ρ2)​vϵϵ​ρ2];(1−δ−ρ2)​vϵϵ​ρ2≥K}≤supϵ>0𝖤​[|Yϵ|;|Yϵ|≥K],\begin{split}&\sup\_{\epsilon>0}\mathsf{E}\left[\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}1\_{\{\tau\leq T\}};\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}1\_{\{\tau\leq T\}}\geq K\right]\\ &\leq\sup\left\{\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}\mathsf{P}[\tau\leq T];\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}\geq K\right\}\\ &\leq\sup\left\{\mathsf{E}\left[|Y^{\epsilon}|;|Y^{\epsilon}|\geq\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}\right];\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon\rho^{2}}\geq K\right\}\\ &\leq\sup\_{\epsilon>0}\mathsf{E}\left[|Y^{\epsilon}|;|Y^{\epsilon}|\geq K\right],\end{split} |  |

which converges to 0 as K→∞K\to\infty by the uniform integrability of YϵY^{\epsilon}. Therefore, Yhatϵ\hat{Y}^{\epsilon} also is uniformly integrable.
  
iv). Let

|  |  |  |
| --- | --- | --- |
|  | A={(1−ρ2)​\ilimits@0T∧τ​Vuϵ​d​u>δ​vϵ}.A=\left\{(1-\rho^{2})\intslop\ilimits@\_{0}^{T\wedge\tau}V^{\epsilon}\_{u}\mathrm{d}u>\delta v^{\epsilon}\right\}. |  |

We have

|  |  |  |
| --- | --- | --- |
|  | 𝖯​[Ac]=𝖯​[Yhatϵ≤−(1−δ−ρ2)​vϵϵ​(1−ρ2)]≤ϵ​(1−ρ2)(1−δ−ρ2)​vϵ​𝖤​[|Yhatϵ|;|Yhatϵ|≥(1−δ−ρ2)​vϵϵ​(1−ρ2)],\begin{split}\mathsf{P}[A^{c}]&=\mathsf{P}\left[\hat{Y}^{\epsilon}\leq-\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon(1-\rho^{2})}\right]\\ &\leq\frac{\epsilon(1-\rho^{2})}{(1-\delta-\rho^{2})v^{\epsilon}}\mathsf{E}\left[|\hat{Y}^{\epsilon}|;|\hat{Y}^{\epsilon}|\geq\frac{(1-\delta-\rho^{2})v^{\epsilon}}{\epsilon(1-\rho^{2})}\right],\end{split} |  |

which is of o​(ϵ)o(\epsilon) by the uniform integrability of Yhatϵ\hat{Y}^{\epsilon} and ([2](https://arxiv.org/html/2601.09324v1#S1.E2 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")).
Since ff is bounded, so is pp. This implies that

|  |  |  |
| --- | --- | --- |
|  | 𝖤[p(ShatTϵ,+TϵϵYhatϵ)−p(ShatTϵ,)Tϵ]=𝖤[p(ShatTϵ,+TϵϵYhatϵ)−p(ShatTϵ,)Tϵ;A]+o(ϵ)\mathsf{E}\left[p\left(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T}+\epsilon\hat{Y}^{\epsilon}\right)-p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})\right]=\mathsf{E}\left[p\left(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T}+\epsilon\hat{Y}^{\epsilon}\right)-p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T});A\right]+o(\epsilon) |  |

We have

|  |  |  |
| --- | --- | --- |
|  | p(ShatTϵ,+TϵϵYhatϵ)−p(ShatTϵ,)Tϵ=ϵYhatϵ\ilimits@01∂p∂t(ShatTϵ,+TϵrϵYhatϵ)drp\left(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T}+\epsilon\hat{Y}^{\epsilon}\right)-p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})=\epsilon\hat{Y}^{\epsilon}\intslop\ilimits@\_{0}^{1}\frac{\partial p}{\partial t}\left(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T}+r\epsilon\hat{Y}^{\epsilon}\right)\mathrm{d}r |  |

and on the set AA,

|  |  |  |
| --- | --- | --- |
|  | +TϵrϵYhatϵ≥δvϵ{}^{\epsilon}\_{T}+r\epsilon\hat{Y}^{\epsilon}\geq\delta v^{\epsilon} |  |

for all r∈[0,1]r\in[0,1]. Combining with the above, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤[p(ShatTϵ,+TϵϵYhatϵ)−p(ShatTϵ,)Tϵ]=ϵ𝖤[Yhatϵ\ilimits@01∂p∂t(ShatTϵ,(+TϵrϵYhatϵ)∨(δvϵ))dr;A]+o(ϵ)\begin{split}&\mathsf{E}\left[p\left(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T}+\epsilon\hat{Y}^{\epsilon}\right)-p(\hat{S}^{\epsilon}\_{T},{}^{\epsilon}\_{T})\right]\\ &=\epsilon\mathsf{E}\left[\hat{Y}^{\epsilon}\intslop\ilimits@\_{0}^{1}\frac{\partial p}{\partial t}\left(\hat{S}^{\epsilon}\_{T},({}^{\epsilon}\_{T}+r\epsilon\hat{Y}^{\epsilon})\vee(\delta v^{\epsilon})\right)\mathrm{d}r;A\right]+o(\epsilon)\end{split} |  | (14) |

v). Notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂p∂t​(s,t)=\ilimits@​f​(s​ew)​∂∂t​ϕ​(wt+t2)​d​w\frac{\partial p}{\partial t}(s,t)=\intslop\ilimits@f(se^{w})\frac{\partial}{\partial t}\phi\left(\frac{w}{\sqrt{t}}+\frac{\sqrt{t}}{2}\right)\mathrm{d}w |  | (15) |

and because ff is bounded,

|  |  |  |
| --- | --- | --- |
|  | ∂p∂t​(s,u∨(δ​vϵ))\frac{\partial p}{\partial t}(s,u\vee(\delta v^{\epsilon})) |  |

is bounded in ss, uu and sufficiently small ϵ\epsilon under ([2](https://arxiv.org/html/2601.09324v1#S1.E2 "In 1 Introduction ‣ Martingale expansion for stochastic volatility")).
  
vi).
Since (Xϵ,Yϵ)→(X,Y)(X^{\epsilon},Y^{\epsilon})\to(X,Y) in law, with the aid of i), we have

|  |  |  |
| --- | --- | --- |
|  | (1vϵ​\ilimits@0T∧τ​Vtϵ​d​Bt,Yhatϵ)→(X,Y)\left(\frac{1}{\sqrt{v^{\epsilon}}}\intslop\ilimits@\_{0}^{T\wedge\tau}\sqrt{V^{\epsilon}\_{t}}\mathrm{d}B\_{t},\hat{Y}^{\epsilon}\right)\to\left(X,Y\right) |  |

in law as ϵ→0\epsilon\to 0. On the other hand,

|  |  |  |
| --- | --- | --- |
|  | \ilimits@0T∧τVtϵdBt=ρZTϵ+(1−ρ2)(vϵ+ϵYhatϵ)Nϵ,\intslop\ilimits@\_{0}^{T\wedge\tau}\sqrt{V^{\epsilon}\_{t}}\mathrm{d}B\_{t}=\rho Z^{\epsilon}\_{T}+\sqrt{(1-\rho^{2})(v^{\epsilon}+\epsilon\hat{Y}^{\epsilon}})N^{\epsilon}, |  |

where NϵN^{\epsilon} is a standard normal random variable independent of (ZTϵ,Yhatϵ)(Z^{\epsilon}\_{T},\hat{Y}^{\epsilon}).
Therefore, the sequence of joint distribution

|  |  |  |
| --- | --- | --- |
|  | (1vϵ​\ilimits@0T∧τ​Vtϵ​d​Bt,Yhatϵ,ZTϵ,Nϵ)\left(\frac{1}{\sqrt{v^{\epsilon}}}\intslop\ilimits@\_{0}^{T\wedge\tau}\sqrt{V^{\epsilon}\_{t}}\mathrm{d}B\_{t},\hat{Y}^{\epsilon},Z^{\epsilon}\_{T},N^{\epsilon}\right) |  |

is tight, of which an accumulation point is uniquely determined as (X,Y,Z,N)(X,Y,Z,N)
such that NN is a standard normal random variable independent of (Y,Z)(Y,Z) and

|  |  |  |
| --- | --- | --- |
|  | ρ​Z+(1−ρ2)​v0​N=X.\rho Z+\sqrt{(1-\rho^{2})v^{0}}N=X. |  |

Since XX must be a standard normal random variable by the martingale central limit theorem,
ZZ is a centered normal random variable with variance v0v^{0}.
  
vii). From iii), iv), v) and vi), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limϵ→0𝖤[Yhatϵ\ilimits@01∂p∂t(ShatTϵ,(+TϵrϵYhatϵ)∨(δvϵ))dr;A]=limϵ→0𝖤[Yhatϵ\ilimits@01∂p∂t(ShatTϵ,(+TϵrϵYhatϵ)∨(δvϵ))dr]=𝖤​[Y​∂p∂t​(Shat0,(1−ρ2)​v0)],\begin{split}&\lim\_{\epsilon\to 0}\mathsf{E}\left[\hat{Y}^{\epsilon}\intslop\ilimits@\_{0}^{1}\frac{\partial p}{\partial t}\left(\hat{S}^{\epsilon}\_{T},({}^{\epsilon}\_{T}+r\epsilon\hat{Y}^{\epsilon})\vee(\delta v^{\epsilon})\right)\mathrm{d}r;A\right]\\ &=\lim\_{\epsilon\to 0}\mathsf{E}\left[\hat{Y}^{\epsilon}\intslop\ilimits@\_{0}^{1}\frac{\partial p}{\partial t}\left(\hat{S}^{\epsilon}\_{T},({}^{\epsilon}\_{T}+r\epsilon\hat{Y}^{\epsilon})\vee(\delta v^{\epsilon})\right)\mathrm{d}r\right]\\ &=\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\hat{S}^{0},(1-\rho^{2})v^{0})\right],\end{split} |  | (16) |

where

|  |  |  |
| --- | --- | --- |
|  | Shat0=S0​exp⁡{ρ​Z−ρ22​v0}.\hat{S}^{0}=S\_{0}\exp\left\{\rho Z-\frac{\rho^{2}}{2}v^{0}\right\}. |  |

From ([10](https://arxiv.org/html/2601.09324v1#S4.E10 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")), ([13](https://arxiv.org/html/2601.09324v1#S4.E13 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")), ([14](https://arxiv.org/html/2601.09324v1#S4.E14 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")) and ([16](https://arxiv.org/html/2601.09324v1#S4.E16 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[f​(STϵ)]=p​(S0,vϵ)+ϵ​𝖤​[Y​∂p∂t​(Shat0,(1−ρ2)​v0)]+o​(ϵ).\mathsf{E}[f(S^{\epsilon}\_{T})]=p(S\_{0},v^{\epsilon})+\epsilon\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\hat{S}^{0},(1-\rho^{2})v^{0})\right]+o(\epsilon). |  | (17) |

viii). Let Wcheck\check{W} be a standard Brownian motion independent of (Y,Z)(Y,Z) and

|  |  |  |
| --- | --- | --- |
|  | Scheckτ=Shat0​exp⁡{(1−ρ2)​v0​Wcheckτ−12​(1−ρ2)​v0​τ},checkτ=(1−ρ2)​v0​(1−τ)+δ.\check{S}\_{\tau}=\hat{S}^{0}\exp\left\{\sqrt{(1-\rho^{2})v^{0}}\check{W}\_{\tau}-\frac{1}{2}(1-\rho^{2})v^{0}\tau\right\},\ \ \check{\Sigma}\_{\tau}=(1-\rho^{2})v^{0}(1-\tau)+\delta. |  |

Then, by Itô’s formula and ([12](https://arxiv.org/html/2601.09324v1#S4.E12 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")),

|  |  |  |
| --- | --- | --- |
|  | ∂p∂t​(Scheck1,check1)=∂p∂t​(Scheck0,check0)+\ilimits@01​∂2p∂s​∂t​(Scheckτ,checkτ)​d​Scheckτ,\frac{\partial p}{\partial t}(\check{S}\_{1},\check{\Sigma}\_{1})=\frac{\partial p}{\partial t}(\check{S}\_{0},\check{\Sigma}\_{0})+\intslop\ilimits@\_{0}^{1}\frac{\partial^{2}p}{\partial s\partial t}(\check{S}\_{\tau},\check{\Sigma}\_{\tau})\mathrm{d}\check{S}\_{\tau}, |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[Y​∂p∂t​(Scheck1,check1)]=𝖤​[Y​∂p∂t​(Scheck0,check0)]=𝖤​[Y​∂p∂t​(Shat0,(1−ρ2)​v0+δ)].\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\check{S}\_{1},\check{\Sigma}\_{1})\right]=\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\check{S}\_{0},\check{\Sigma}\_{0})\right]=\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\hat{S}^{0},(1-\rho^{2})v^{0}+\delta)\right]. |  | (18) |

Notice that the joint law of (Scheck1,Y)(\check{S}\_{1},Y) is identical to

|  |  |  |
| --- | --- | --- |
|  | (S0​exp⁡{v0​X−v02},Y).\left(S\_{0}\exp\left\{\sqrt{v^{0}}X-\frac{v^{0}}{2}\right\},Y\right). |  |

Therefore, using again ([12](https://arxiv.org/html/2601.09324v1#S4.E12 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")),

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[Y​∂p∂t​(Scheck1,check1)]=12​𝖤​[Y​Shat12​∂2p∂s2​(Scheck1,check1)]=12​\ilimits@​𝖤​[Y|X=x]​(S0​ev0​x−v0/2)2​∂2p∂s2​(S0​ev0​x−v0/2,δ)​ϕ​(x)​d​x=12​\ilimits@​𝖤​[Y|X=x]​(1v0​∂2∂x2−1v0​∂∂x)​p​(S0​ev0​x−v0/2,δ)​ϕ​(x)​d​x=12​\ilimits@​p​(S0​ev0​x−v0/2,δ)​(1v0​∂2∂x2+1v0​∂∂x)​(𝖤​[Y|X=x]​ϕ​(x))​d​x.\begin{split}&\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\check{S}\_{1},\check{\Sigma}\_{1})\right]=\frac{1}{2}\mathsf{E}\left[Y\hat{S}\_{1}^{2}\frac{\partial^{2}p}{\partial s^{2}}(\check{S}\_{1},\check{\Sigma}\_{1})\right]\\ &=\frac{1}{2}\intslop\ilimits@\mathsf{E}[Y|X=x]\left(S\_{0}e^{\sqrt{v^{0}}x-v^{0}/2}\right)^{2}\frac{\partial^{2}p}{\partial s^{2}}\left(S\_{0}e^{\sqrt{v^{0}}x-v^{0}/2},\delta\right)\phi(x)\mathrm{d}x\\ &=\frac{1}{2}\intslop\ilimits@\mathsf{E}[Y|X=x]\left(\frac{1}{v^{0}}\frac{\partial^{2}}{\partial x^{2}}-\frac{1}{\sqrt{v^{0}}}\frac{\partial}{\partial x}\right)p\left(S\_{0}e^{\sqrt{v^{0}}x-v^{0}/2},\delta\right)\phi(x)\mathrm{d}x\\ &=\frac{1}{2}\intslop\ilimits@p\left(S\_{0}e^{\sqrt{v^{0}}x-v^{0}/2},\delta\right)\left(\frac{1}{v^{0}}\frac{\partial^{2}}{\partial x^{2}}+\frac{1}{\sqrt{v^{0}}}\frac{\partial}{\partial x}\right)(\mathsf{E}[Y|X=x]\phi(x))\mathrm{d}x.\end{split} |  |

Here we have used ([3](https://arxiv.org/html/2601.09324v1#S2.E3 "In Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")). Then, by ([18](https://arxiv.org/html/2601.09324v1#S4.E18 "In 4.1 Proof of Theorem 1 ‣ 4 Proofs ‣ Martingale expansion for stochastic volatility")),

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[Y​∂p∂t​(Shat0,(1−ρ2)​v0)]=limδ→0𝖤​[Y​∂p∂t​(Shat0,(1−ρ2)​v0+δ)]=12​\ilimits@​p​(S0​ev0​x−v0/2,0)​(1v0​∂2∂x2+1v0​∂∂x)​(𝖤​[Y|X=x]​ϕ​(x))​d​x.\begin{split}&\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\hat{S}^{0},(1-\rho^{2})v^{0})\right]=\lim\_{\delta\to 0}\mathsf{E}\left[Y\frac{\partial p}{\partial t}(\hat{S}^{0},(1-\rho^{2})v^{0}+\delta)\right]\\ &=\frac{1}{2}\intslop\ilimits@p\left(S\_{0}e^{\sqrt{v^{0}}x-v^{0}/2},0\right)\left(\frac{1}{v^{0}}\frac{\partial^{2}}{\partial x^{2}}+\frac{1}{\sqrt{v^{0}}}\frac{\partial}{\partial x}\right)(\mathsf{E}[Y|X=x]\phi(x))\mathrm{d}x.\end{split} |  |

The rest would be clear.

### 4.2 Proof of Corollary [1](https://arxiv.org/html/2601.09324v1#Thmcor1 "Corollary 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility")

First note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | pK​(S0,vϵ)=\ilimits@​f​(S0​exp⁡{vϵ​x−vϵ2})​ϕ​(x)​d​xp\_{K}(S\_{0},v^{\epsilon})=\intslop\ilimits@f\left(S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}\right)\phi(x)\mathrm{d}x |  | (19) |

for f​(s)=(K−s)+f(s)=(K-s)\_{+}. Let g​(x)=𝖤​[Y|X=x]​ϕ​(x)g(x)=\mathsf{E}[Y|X=x]\phi(x)
and d−=d−​(S0,vϵ)d\_{-}=d\_{-}(S\_{0},v^{\epsilon}). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | \ilimits@​f​(S0​exp⁡{vϵ​x−vϵ2})​dd​x​g​(x)​d​x=\ilimits@−∞−d−​(K−S0​exp⁡{vϵ​x−vϵ2})​dd​x​g​(x)​d​x=vϵ​\ilimits@−∞−d−​S0​exp⁡{vϵ​x−vϵ2}​g​(x)​d​x\begin{split}&\intslop\ilimits@f\left(S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}\right)\frac{\mathrm{d}}{\mathrm{d}x}g(x)\mathrm{d}x\\ &=\intslop\ilimits@\_{-\infty}^{-d\_{-}}\left(K-S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}\right)\frac{\mathrm{d}}{\mathrm{d}x}g(x)\mathrm{d}x\\ &=\sqrt{v^{\epsilon}}\intslop\ilimits@\_{-\infty}^{-d\_{-}}S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}g(x)\mathrm{d}x\end{split} |  | (20) |

by ([3](https://arxiv.org/html/2601.09324v1#S2.E3 "In Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility"))
and similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | \ilimits@​f​(S0​exp⁡{vϵ​x−vϵ2})​d2d​x2​g​(x)​d​x=vϵ​\ilimits@−∞−d−​S0​exp⁡{vϵ​x−vϵ2}​dd​x​g​(x)​d​x=vϵ​[S0​exp⁡{vϵ​x−vϵ2}​g​(x)]−∞−d−−vϵ​\ilimits@−∞−d−​S0​exp⁡{vϵ​x−vϵ2}​g​(x)​d​x.\begin{split}&\intslop\ilimits@f\left(S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}\right)\frac{\mathrm{d}^{2}}{\mathrm{d}x^{2}}g(x)\mathrm{d}x\\ &=\sqrt{v^{\epsilon}}\intslop\ilimits@\_{-\infty}^{-d\_{-}}S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}\frac{\mathrm{d}}{\mathrm{d}x}g(x)\mathrm{d}x\\ &=\sqrt{v^{\epsilon}}\left[S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}g(x)\right]^{-d\_{-}}\_{-\infty}-v^{\epsilon}\intslop\ilimits@\_{-\infty}^{-d\_{-}}S\_{0}\exp\left\{\sqrt{v^{\epsilon}}x-\frac{v^{\epsilon}}{2}\right\}g(x)\mathrm{d}x.\end{split} |  | (21) |

The result then follows from Theorem [1](https://arxiv.org/html/2601.09324v1#Thmthm1 "Theorem 1 ‣ 2 Results ‣ Martingale expansion for stochastic volatility").

## References

* [1]

  Alòs, E., A decomposition formula for option prices in the Heston model and applications to option pricing approximation. Finance Stoch. 16, 403–422 (2012).
* [2]

  Bayer, C., Friz, P., Fukasawa, M., Gatheral, J., Jacquier, A., and Rosenbaum, M., Rough volatility, SIAM (2023).
* [3]

  Bayer, C., Friz, P., and Gatheral, J., Pricing under rough volatility. Quantitative Finance 16(6), 887–904 (2016).
* [4]

  Benhamou, E., Gobet, E., and Miri, M.,
  Time Dependent Heston Model, SIAM J. Financial Math. 1, 289-325 (2010).
* [5]

  Bergomi, L. and Guyon, J., Stochastic Volatility’s Orderly Smiles, Risk Magazine, pages 60-66, May 2012.
* [6]

  Bergomi, L., Stochastic Volatility Modeling, CRC Press (2026).
* [7]

  El Euch, O., Fukasawa, M., Gatheral, J., and Rosenbaum, M., Short-term at-the-money asymptotics under stochastic volatility models, SIAM J. Financial Math. 10, 491-511 (2019).
* [8]

  Fouque, J.P., Papanicolaou, G., and Sircar, K.R., Derivatives in Financial Markets with Stochastic Volatility. Cambridge University Press, Cambridge (2000).
* [9]

  Fukasawa, M., Asymptotic analysis for stochastic volatility: martingale expansion. Finance Stoch. 15, 635–654 (2011).
* [10]

  Fukasawa, M., Asymptotic analysis for stochastic volatility: Edgeworth Expansion. Electron. J. Probab. 16, 764-791 (2011).
* [11]

  Fukasawa, M., Volatility has to be rough. Quantitative Finance 21, 1-8 (2021).
* [12]

  Fukasawa, M., Wiener spiral for volatility modeling. Theory of Probability & Its Applications 68, 481-500 (2023).
* [13]

  Garnier J and Sølna K., Option pricing under fast-varying long-memory stochastic volatility. Mathematical Finance 29, 39–83 (2019).
* [14]

  Lewis, A.L. Option Valuation under Stochastic Volatility, with Mathematica Code. Finance Press,
  Newport Beach (2000).
* [15]

  Mykland, P. A., Asymptotic Expansions for Martingales. Ann. Probab. 21 (2) 800–818 (1993).
* [16]

  Mykland, P. A., Martingale Expansions and Second Order Inference. Ann. Statist. 23 (3) 707-731 (1995).
* [17]

  Yoshida, N. Malliavin calculus and asymptotic expansion for martingales. Probab. Theory Relat.
  Fields 109, 301–342 (1997).
* [18]

  Yoshida, N., Malliavin calculus and martingale expansion. Bull. Sci. Math. 125, 431–456 (2001).