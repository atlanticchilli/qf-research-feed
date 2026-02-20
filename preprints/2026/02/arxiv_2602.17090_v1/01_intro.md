---
authors:
- Takuji Arai
doc_id: arxiv:2602.17090v1
family_id: arxiv:2602.17090
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Local risk-minimization for exponential additive processes
url_abs: http://arxiv.org/abs/2602.17090v1
url_html: https://arxiv.org/html/2602.17090v1
venue: arXiv q-fin
version: 1
year: 2026
---


Takuji Arai111Department of Economics, Keio University, 2-15-45 Mita, Minato-ku, Tokyo, 108-8345, Japan.
  
(arai.z8@keio.jp)

###### Abstract

We explore local risk-minimization, a quadratic hedging method for incomplete markets, in exponential additive models.
The objectives are to derive explicit mathematical expressions and to conduct numerical experiments.
While local risk-minimization is well studied for Lévy processes, little is known for the additive process case
because, unlike Lévy processes, the Lévy measure for an additive process depends on time, which significantly complicates the mathematical framework.
This paper shall provide a set of necessary conditions for deriving expressions for LRM strategies in exponential additive models, as integrability conditions on the Lévy measure,
which allow us to confirm whether these conditions are satisfied for given concrete models.
In the final section, we introduce the variance-gamma scaled self-decomposable process, a Sato process that generalizes the variance-gamma process, as a primary example,
and perform numerical experiments.
  
Keywords: Local risk-minimization, Additive processes, Malliavin-Skorohod calculus, Carr-Madan method.

## 1 Introduction

Local risk-minimization is a representative quadratic hedging method for contingent claims in incomplete financial markets.
It was undertaken by Föllmer and Sondermann [[9](https://arxiv.org/html/2602.17090v1#bib.bib9)] and Föllmer and Schweizer [[8](https://arxiv.org/html/2602.17090v1#bib.bib8)], and has been well studied for three decades since then.
For an overview of local risk-minimization, see Schweizer [[15](https://arxiv.org/html/2602.17090v1#bib.bib15)].
This paper aims to derive explicit representations of locally risk-minimizing (LRM) strategies for financial market models
in which the asset price process is an exponential additive process and to present some numerical results.

There is a large amount of literature on local risk-minimization,
but here we introduce just a part of it by focusing on explicit representations and numerical analysis for market models described by a jump process.
Arai and Suzuki [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)] derived an explicit expression for LRM strategies for models with the asset price process described by
the solution to a Lévy-driven stochastic differential equation.
In [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)], they used Malliavin calculus for Lévy processes by Solé et al. [[17](https://arxiv.org/html/2602.17090v1#bib.bib17)], and a Clark-Ocone type formula under a change of measure by Suzuki [[18](https://arxiv.org/html/2602.17090v1#bib.bib18)].
Arai et al. [[2](https://arxiv.org/html/2602.17090v1#bib.bib2)] developed a numerical method for LRM strategies in models with an exponential Lévy process as the asset price process,
using the Carr-Madan method, which is based on the fast Fourier transform (FFT).
A Lévy process is, roughly speaking, a stochastic process having independent and stationary increments.
On the other hand, relaxing the requirement of stationary increments in the definition of Lévy processes, we call such processes additive processes.
That is, the Lévy measure for an additive process depends on time.
Therefore, it is natural to examine additive processes as a generalization of Lévy processes,
and deriving expressions and developing numerical methods for market models described by an additive process are significant issues in mathematical finance.

To derive a mathematical expression for LRM strategies in models with an exponential additive asset price process, called exponential additive models henceforth,
it is necessary to employ a Malliavin calculus framework available for additive processes.
In this regard, Malliavin-Skorohod calculus, as developed by Di Nunno and Vives [[6](https://arxiv.org/html/2602.17090v1#bib.bib6)], is useful,
and a Clark-Ocone-type formula under a change of measure for additive processes obtained by Handa et al. [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] is available.
Local risk-minimization has also been discussed in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] using the same sort of argument as [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)];
however, their argument contains inaccurate statements and propositions for which no proof is given.
We should not simply regard an additive process as a non-stationary Lévy process and think that the only difference lies in whether the Lévy measure is time-dependent.
We need to note that the time dependence of the Lévy measure makes a significant difference in the mathematical discussion.

In this paper, we derive expressions of LRM strategies for exponential additive models and emphasize how time dependence affects mathematical discussion.
It is well-known that LRM strategies are given through the Föllmer-Schweizer decomposition.
The minimal martingale measure (MMM), one of the equivalent martingale measures, plays a vital role in discussing the Föllmer-Schweizer decomposition.
We need the MMM to exist and be square integrable to derive expressions for LRM strategies.
To this end, we will provide conditions that guarantee these properties as integrability conditions on the Lévy measure,
enabling verification that they are satisfied when a concrete model is given.

As an example of additive processes that frequently appear in mathematical finance, we introduce the variance-gamma scaled self-decomposable (VGSSD) process,
first proposed by Carr et al. [[3](https://arxiv.org/html/2602.17090v1#bib.bib3)], and conduct numerical experiments of LRM strategies for models written by the VGSSD process.
Here, the VGSSD process is defined as a Sato process (an additive self-similar process with self-decomposable law)
whose distribution at unit time follows a variance-gamma (VG) distribution.
Further, a VG distribution refers to the distribution of a VG process, a Lévy process defined as a time-changing Brownian motion by a gamma process.

The outline of this paper is as follows. Section 2 introduces fundamental assumptions used throughout the paper and defines LRM strategies and the MMM.
In Section 3, we focus on exponential additive models.
In particular, we provide conditions for discussing LRM strategies and for ensuring the existence and square integrability of the MMM.
Section 4 examines LRM strategies for exponential additive models, the main theme of this paper.
First, we address the result of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] and derive a mathematical expression for LRM strategies in exponential additive models.
Second, we rewrite it as an expression that enables us to compute LRM strategies numerically using the Carr-Madan method.
In Section 5, we introduce the VGSSD process as a representative additive process and conduct numerical experiments.
Section 6 concludes this paper.

## 2 Preliminaries

Throughout this paper, we consider a financial market model composed of one riskless asset and one risky asset with maturity T>0T>0.
Without loss of generality, we may assume that the interest rate is zero.
Suppose that the risky asset price process S={St}0≤t≤TS=\{S\_{t}\}\_{0\leq t\leq T} is given by a positive-valued special semimartingale defined on
a probability space (Ω,ℱ,ℙ)(\Omega,{\mathcal{F}},{\mathbb{P}}) with the canonical decomposition St=S0+Mt+AtS\_{t}=S\_{0}+M\_{t}+A\_{t},
where S0>0S\_{0}>0, M={Mt}t∈[0,T]M=\{M\_{t}\}\_{t\in[0,T]} is a martingale with M0=0M\_{0}=0, and A={At}t∈[0,T]A=\{A\_{t}\}\_{t\in[0,T]} is a predictable process of finite variation with A0=0A\_{0}=0.
Now, we suppose that SS satisfies the following conditions:

###### Assumption 2.1.

1. (SC1)

   𝔼​[[M]T]<∞{\mathbb{E}}[[M]\_{T}]<\infty and 𝔼​[(∫0T|d​At|)2]<∞\displaystyle{{\mathbb{E}}\left[\left(\int\_{0}^{T}|dA\_{t}|\right)^{2}\right]<\infty}.
2. (SC2)

   There is a predictable process λ={λt}t∈[0,T]\lambda=\{\lambda\_{t}\}\_{t\in[0,T]} such that At=∫0tλs​d​⟨M⟩s\displaystyle{A\_{t}=\int\_{0}^{t}\lambda\_{s}d\langle M\rangle\_{s}}.
3. (SC3)

   The process K={Kt}t∈[0,T]K=\{K\_{t}\}\_{t\in[0,T]} defined as Kt:=∫0tλs2​d​⟨M⟩s\displaystyle{K\_{t}:=\int\_{0}^{t}\lambda^{2}\_{s}d\langle M\rangle\_{s}} is continuous such that KT<∞K\_{T}<\infty, ℙ{\mathbb{P}}-a.s.

When SS satisfies Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes") above, SS is said to satisfy the structure condition (SC), which is closely related to the no-arbitrage condition.

Here, we define locally risk-minimizing (LRM) strategies as follows:

###### Definition 2.2.

1. 1.

   Ξ=(ξ1,ξ2)\Xi=(\xi^{1},\xi^{2}) is said to be an L2L^{2}-strategy if it satisfies the following conditions:

   1. (a)

      ξ1={ξt1}t∈[0,T]\xi^{1}=\{\xi^{1}\_{t}\}\_{t\in[0,T]} is a predictable process satisfying

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | 𝔼​[∫0T(ξt1)2​d​⟨M⟩t+(∫0T|ξt1​d​At|)2]<∞.{\mathbb{E}}\left[\int\_{0}^{T}(\xi^{1}\_{t})^{2}d\langle M\rangle\_{t}+\left(\int\_{0}^{T}|\xi^{1}\_{t}dA\_{t}|\right)^{2}\right]<\infty. |  | (2.1) |

      ξt1\xi^{1}\_{t} represents the amount of units of the risky asset an investor holds at time tt.
   2. (b)

      ξ2={ξt2}t∈[0,T]\xi^{2}=\{\xi^{2}\_{t}\}\_{t\in[0,T]} is an adapted process representing the amount of units of the riskless asset.
   3. (c)

      For any t∈[0,T]t\in[0,T], denote Vt​(Ξ):=ξt1​St+ξt2V\_{t}(\Xi):=\xi^{1}\_{t}S\_{t}+\xi^{2}\_{t}, which provides the corresponding wealth at time t∈[0,T]t\in[0,T].
      In particular, V0​(Ξ)V\_{0}(\Xi) gives the initial cost.
      Then, V​(Ξ)={Vt​(Ξ)}t∈[0,T]V(\Xi)=\{V\_{t}(\Xi)\}\_{t\in[0,T]} is a right continuous process with 𝔼​[Vt2​(Ξ)]<∞{\mathbb{E}}[V\_{t}^{2}(\Xi)]<\infty for every t∈[0,T]t\in[0,T].
2. 2.

   An L2L^{2}-strategy Ξ\Xi is said to be self-financing, if it satisfies Vt​(Ξ)=V0​(Ξ)+∫0tξs1​𝑑Ss\displaystyle{V\_{t}(\Xi)=V\_{0}(\Xi)+\int\_{0}^{t}\xi^{1}\_{s}dS\_{s}} for any t∈[0,T]t\in[0,T].
3. 3.

   Let FF be a square integrable random variable representing the payoff of a contingent claim at maturity TT.
   For an L2L^{2}-strategy Ξ\Xi, the corresponding cost process C​(Ξ)={Ct​(Ξ)}t∈[0,T]C(\Xi)=\{C\_{t}(\Xi)\}\_{t\in[0,T]} for claim FF is defined as

   |  |  |  |
   | --- | --- | --- |
   |  | Ct​(Ξ):=F​𝟏{t=T}+Vt​(Ξ)−∫0tξs1​𝑑Ss,t∈[0,T].C\_{t}(\Xi):=F{\bf 1}\_{\{t=T\}}+V\_{t}(\Xi)-\int\_{0}^{t}\xi^{1}\_{s}dS\_{s},\ \ \ t\in[0,T]. |  |
4. 4.

   An L2L^{2}-strategy Ξ\Xi is called the LRM strategy for claim FF, if VT​(Ξ)=FV\_{T}(\Xi)=F, and [C​(Ξ),M][C(\Xi),M] is a uniformly integrable martingale.
   Roughly speaking, an L2L^{2}-strategy Ξ\Xi, which is not necessarily self-financing, is LRM
   if it is the replicating strategy that minimizes a risk caused by C​(Ξ)C(\Xi) in the L2L^{2}-sense among all replicating strategies.

###### Remark 2.3.

Definition [2.2](https://arxiv.org/html/2602.17090v1#S2.Thmthm2 "Definition 2.2. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes") above is based on Theorem 1.6 of Schweizer [[15](https://arxiv.org/html/2602.17090v1#bib.bib15)].
Note that the structure condition (SC) does not usually include the continuity of KK, but it is included here because we use Theorem 1.6 of [[15](https://arxiv.org/html/2602.17090v1#bib.bib15)].

It is sufficient to get a representation of ξ1\xi^{1} in order to obtain a representation of the LRM strategy Ξ\Xi for claim FF,
since ξ2\xi^{2} is automatically determined by ξ1\xi^{1}. Here, an F∈L2​(ℙ)F\in L^{2}({\mathbb{P}}) admits a Föllmer-Schweizer decomposition, if it can be described by

|  |  |  |
| --- | --- | --- |
|  | F=F0+∫0TξtF​S​𝑑St+LTF​S,F=F\_{0}+\int\_{0}^{T}\xi^{FS}\_{t}dS\_{t}+L\_{T}^{FS}, |  |

where F0∈ℝF\_{0}\in{\mathbb{R}}, ξF​S={ξtF​S}t∈[0,T]\xi^{FS}=\{\xi^{FS}\_{t}\}\_{t\in[0,T]} is a predictable process satisfying ([2.1](https://arxiv.org/html/2602.17090v1#S2.E1 "In item 1a ‣ item 1 ‣ Definition 2.2. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes")),
and LF​S={LtF​S}t∈[0,T]L^{FS}=\{L^{FS}\_{t}\}\_{t\in[0,T]} is a square-integrable martingale orthogonal to MM with L0F​S=0L\_{0}^{FS}=0.
In addition, Proposition 5.2 of [[15](https://arxiv.org/html/2602.17090v1#bib.bib15)] proved that, under Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes"),
the LRM strategy Ξ=(ξ1,ξ2)\Xi=(\xi^{1},\xi^{2}) for claim F∈L2​(ℙ)F\in L^{2}({\mathbb{P}}) exists if and only if FF admits a Föllmer-Schweizer decomposition;
and ξt1=ξtF​S\xi^{1}\_{t}=\xi^{FS}\_{t} holds. As a result, it suffices to obtain a representation of ξF\xi^{F} in order to get the LRM strategy Ξ\Xi.

Next, we discuss the minimal martingale measure (MMM). A probability measure ℙ∗{\mathbb{P}}^{\*} equivalent to ℙ{\mathbb{P}} is called the MMM if it is an equivalent martingale measure
under which any square integrable ℙ{\mathbb{P}}-martingale orthogonal to MM remains a martingale under ℙ∗{\mathbb{P}}^{\*}.
Here, for a semimartingale Y={Yt}t∈[0,T]Y=\{Y\_{t}\}\_{t\in[0,T]} with Y0=0Y\_{0}=0, a process X={Xt}t∈[0,T]X=\{X\_{t}\}\_{t\in[0,T]} is called the stochastic exponential of YY
if it is the solution to the stochastic differential equation (SDE):

|  |  |  |
| --- | --- | --- |
|  | d​Xt=Xt−​d​Yt,X0=1.dX\_{t}=X\_{t-}dY\_{t},\ \ \ X\_{0}=1. |  |

Wedenote it as Xt=ℰt​(Y)X\_{t}={\mathcal{E}}\_{t}(Y).
Now, we define a process Mλ={Mtλ}t∈[0,T]M^{\lambda}=\{M^{\lambda}\_{t}\}\_{t\in[0,T]} as Mtλ:=−∫0tλs​𝑑Ms\displaystyle{M^{\lambda}\_{t}:=-\int\_{0}^{t}\lambda\_{s}dM\_{s}},
and consider its stochastic exponential Z:=ℰ​(Mλ)Z:={\mathcal{E}}(M^{\lambda}), that is, the process Z={Zt}t∈[0,T]Z=\{Z\_{t}\}\_{t\in[0,T]} is given as the solution to the SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zt=−λt​Zt−​d​Mt,Z0=1.dZ\_{t}=-\lambda\_{t}Z\_{t-}dM\_{t},\ \ \ Z\_{0}=1. |  | (2.2) |

As seen in Lemma 2.7 of Arai and Suzuki [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)], when ZZ is a positive square integrable martingale and Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes") is satisfied,
the MMM ℙ∗{\mathbb{P}}^{\*} exists with d​ℙ∗=ZT​d​ℙd{\mathbb{P}}^{\*}=Z\_{T}d{\mathbb{P}}. Then, for every t∈[0,T]t\in[0,T], ZtZ\_{t} satisfies

|  |  |  |
| --- | --- | --- |
|  | Zt=𝔼​[d​ℙ∗d​ℙ|ℱt].Z\_{t}={\mathbb{E}}\left[\frac{d{\mathbb{P}}^{\*}}{d{\mathbb{P}}}\Big|{\mathcal{F}}\_{t}\right]. |  |

In [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)], for the case where SS is given by the solution to an SDE driven by a Lévy process,
they obtained an explicit representation of the LRM strategy for claim FF by using the martingale representation for the product F​ZTFZ\_{T}.
In this paper, we extend [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)]’s result to exponential additive models, but the mathematical treatment is more complicated because the Lévy measure is no longer stationary,
i.e., time-dependent.

## 3 Exponential additive processes

In this section, we consider models in which S={St}0≤t≤TS=\{S\_{t}\}\_{0\leq t\leq T} follows an exponential additive process, that is,
the log-price process L={Lt}t∈[0,T]L=\{L\_{t}\}\_{t\in[0,T]} defined as Lt:=log⁡(St/S0)L\_{t}:=\log(S\_{t}/S\_{0}) becomes an additive process.
In particular, we treat only the case where LL is an additive process without the Gaussian component.

Let {(0,νt,γt)}t∈[0,T]\{(0,\nu\_{t},\gamma\_{t})\}\_{t\in[0,T]} be the system of generating triplets for the log-price process LL,
where γt\gamma\_{t} is a continuous function on [0,T][0,T] with γ0=0\gamma\_{0}=0,
and {νt}t∈[0,T]\{\nu\_{t}\}\_{t\in[0,T]} is a non-decreasing continuous sequence of Lévy measures on ℝ0{\mathbb{R}}\_{0} with ν0≡0\nu\_{0}\equiv 0.
Here, ℝ0:=ℝ\{0}{\mathbb{R}}\_{0}:={\mathbb{R}}\backslash\{0\}. More precisely, {νt}t∈[0,T]\{\nu\_{t}\}\_{t\in[0,T]} satisfies the following conditions:

1. 1.

   For each t∈[0,T]t\in[0,T], νt\nu\_{t} is a σ\sigma-finite measure such that ∫ℝ0(1∧x2)​νt​(d​x)<∞\displaystyle{\int\_{{\mathbb{R}}\_{0}}(1\wedge x^{2})\nu\_{t}(dx)<\infty}.
2. 2.

   (Non-decreasing property) For any 0≤s≤t≤T0\leq s\leq t\leq T and any B∈ℬ​(ℝ0)B\in{\mathcal{B}}({\mathbb{R}}\_{0}), νs​(B)≤νt​(B)\nu\_{s}(B)\leq\nu\_{t}(B), where ℬ​(ℝ0){\mathcal{B}}({\mathbb{R}}\_{0}) is the Borel algebra on ℝ0{\mathbb{R}}\_{0}.
3. 3.

   (Continuity) As s→t∈[0,T]s\to t\in[0,T], νs​(B)\nu\_{s}(B) converges to νt​(B)\nu\_{t}(B) for any B∈ℬ​(ℝ0)B\in{\mathcal{B}}({\mathbb{R}}\_{0}) with B⊂{x:|x|>ε}B\subset\{x:|x|>\varepsilon\} for some ε>0\varepsilon>0.

According to Theorem 9.8, Remark 9.9, and Theorem 11.5 of Sato [[14](https://arxiv.org/html/2602.17090v1#bib.bib14)], there exists an additive process LL satisfying the above conditions,
taking a modification as necessary. For every t∈[0,T]t\in[0,T], LtL\_{t} has an infinitely divisible law with the characteristic function

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ei​u​Lt]=exp⁡{i​u​γt+∫ℝ0(ei​u​x−1−i​u​x​𝟏{|x|≤1})​νt​(d​x)},u∈ℝ.{\mathbb{E}}\left[e^{iuL\_{t}}\right]=\exp\left\{iu\gamma\_{t}+\int\_{{\mathbb{R}}\_{0}}\left(e^{iux}-1-iux{\bf 1}\_{\{|x|\leq 1\}}\right)\nu\_{t}(dx)\right\},\ \ \ u\in{\mathbb{R}}. |  |

We denote by NN the Poisson random measure associated with LL, that is,

|  |  |  |
| --- | --- | --- |
|  | N​(G):=#​{t|(t,Δ​Lt)∈G},G∈ℬ​([0,T]×ℝ0),N(G):=\#\{t\ |\ (t,\Delta L\_{t})\in G\},\ \ \ G\in{\mathcal{B}}([0,T]\times{\mathbb{R}}\_{0}), |  |

where Δ​Lt:=Lt−Lt−\Delta L\_{t}:=L\_{t}-L\_{t-}. Then, its compensated measure ν¯\overline{\nu} is defined as a measure on ([0,T]×ℝ0,ℬ​([0,T]×ℝ0))([0,T]\times{\mathbb{R}}\_{0},{\mathcal{B}}([0,T]\times{\mathbb{R}}\_{0})) satisfying
ν¯​(G):=𝔼​[N​(G)]\overline{\nu}(G):={\mathbb{E}}[N(G)] for any G∈ℬ​([0,T]×ℝ0)G\in{\mathcal{B}}([0,T]\times{\mathbb{R}}\_{0}). We denote N~​(G):=N​(G)−ν¯​(G)\widetilde{N}(G):=N(G)-\overline{\nu}(G).
Note that ν¯\overline{\nu} satisfies νt​(A)=ν¯​([0,t],A)\nu\_{t}(A)=\overline{\nu}([0,t],A) and ν¯​({t},A)=0\overline{\nu}(\{t\},A)=0 for any t∈[0,T]t\in[0,T] and any A∈ℬ​(ℝ0)A\in{\mathcal{B}}({\mathbb{R}}\_{0}).
Using NN and N~\widetilde{N}, we can describe LtL\_{t} as

|  |  |  |
| --- | --- | --- |
|  | Lt=γt+∫0t∫|x|>1x​N​(d​s,d​x)+∫0t∫|x|≤1x​N~​(d​s,d​x).L\_{t}=\gamma\_{t}+\int\_{0}^{t}\int\_{|x|>1}xN(ds,dx)+\int\_{0}^{t}\int\_{|x|\leq 1}x\widetilde{N}(ds,dx). |  |

Here, taking into account Proposition 3.1 of Goutte et al. [[10](https://arxiv.org/html/2602.17090v1#bib.bib10)], we define the cumulant generating function κt\kappa\_{t} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | κt​(u):=log⁡𝔼​[eu​Lt]=u​γt+∫0t∫ℝ0(eu​x−1−u​x​𝟏{|x|≤1})​ν¯​(d​s,d​x)\kappa\_{t}(u):=\log{\mathbb{E}}[e^{uL\_{t}}]=u\gamma\_{t}+\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(e^{ux}-1-ux{\bf 1}\_{\{|x|\leq 1\}}\right)\overline{\nu}(ds,dx) |  | (3.1) |

for any u∈ℝu\in{\mathbb{R}} satisfying ∫0T∫|x|>1eu​x​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{|x|>1}e^{ux}\overline{\nu}(ds,dx)<\infty}.

Now, we assume the following:

(A1)
:   γt\gamma\_{t} is differentiable on (0,T](0,T], that is, it is expressed as γt=∫0tγs′​𝑑s\displaystyle{\gamma\_{t}=\int\_{0}^{t}\gamma^{\prime}\_{s}ds} for any t∈(0,T]t\in(0,T].

(A2)
:   The Lévy measure ν¯\overline{\nu} is absolutely continuous with respect to d​t×d​xdt\times dx, that is,
    there is a non-negative function π\pi such that ν¯​(d​t,d​x)=π​(t,x)​d​t​d​x\overline{\nu}(dt,dx)=\pi(t,x)dtdx for any t∈(0,T]t\in(0,T] and any x∈ℝ0x\in{\mathbb{R}}\_{0}.

(A3)
:   ∫0T∫|x|>1e4​x​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{|x|>1}e^{4x}\overline{\nu}(ds,dx)<\infty}.

We prove one lemma as follows:

###### Lemma 3.1.

Under Assumption (A3), ∫0T∫ℝ0(ex−1)2​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}(e^{x}-1)^{2}\overline{\nu}(dt,dx)<\infty} holds.

###### Proof.

First of all, (A3) implies that

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫1∞(ex−1)2​ν¯​(d​t,d​x)≤∫0T∫1∞e2​x​ν¯​(d​t,d​x)≤∫0T∫1∞e4​x​ν¯​(d​t,d​x)<∞.\int\_{0}^{T}\int\_{1}^{\infty}(e^{x}-1)^{2}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{1}^{\infty}e^{2x}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{1}^{\infty}e^{4x}\overline{\nu}(dt,dx)<\infty. |  |

Next, since ∫0T∫ℝ0(1∧x2)​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}(1\wedge x^{2})\overline{\nu}(dt,dx)<\infty} holds, we have

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫−∞−1(ex−1)2​ν¯​(d​t,d​x)≤∫0T∫−∞−1ν¯​(d​t,d​x)<∞,\int\_{0}^{T}\int\_{-\infty}^{-1}(e^{x}-1)^{2}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{-\infty}^{-1}\overline{\nu}(dt,dx)<\infty, |  |

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫01(ex−1)2​ν¯​(d​t,d​x)≤(e−1)2​∫0T∫01x2​ν¯​(d​t,d​x)<∞,\int\_{0}^{T}\int\_{0}^{1}(e^{x}-1)^{2}\overline{\nu}(dt,dx)\leq(e-1)^{2}\int\_{0}^{T}\int\_{0}^{1}x^{2}\overline{\nu}(dt,dx)<\infty, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫−10(ex−1)2​ν¯​(d​t,d​x)≤∫0T∫−10x2​ν¯​(d​t,d​x)<∞.\int\_{0}^{T}\int\_{-1}^{0}(e^{x}-1)^{2}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{-1}^{0}x^{2}\overline{\nu}(dt,dx)<\infty. |  |

This completes the proof of Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes").
□\Box

Under the above setting, the asset price process SS is given by the solution to the following SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=St−​{μtS​d​t+∫ℝ0(ex−1)​N~​(d​t,d​x)},S0>0,dS\_{t}=S\_{t-}\left\{\mu^{S}\_{t}dt+\int\_{{\mathbb{R}}\_{0}}\left(e^{x}-1\right)\widetilde{N}(dt,dx)\right\},\ \ \ S\_{0}>0, |  | (3.2) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | μtS:=γt′+∫ℝ0(ex−1−x​𝟏{|x|≤1})​π​(t,x)​𝑑x=∂κt​(1)∂t.\mu^{S}\_{t}:=\gamma^{\prime}\_{t}+\int\_{{\mathbb{R}}\_{0}}\left(e^{x}-1-x{\bf 1}\_{\{|x|\leq 1\}}\right)\pi(t,x)dx=\frac{\partial\kappa\_{t}(1)}{\partial t}. |  | (3.3) |

From the view of Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"), we can show that μtS\mu^{S}\_{t} is well-defined under (A1)–(A3), since ex−1−x≤2​x2e^{x}-1-x\leq 2x^{2} holds when |x|≤1|x|\leq 1.
By the same argument as Proposition 8.20 in Cont and Tankov [[4](https://arxiv.org/html/2602.17090v1#bib.bib4)], we obtain that SS, the solution to ([3.2](https://arxiv.org/html/2602.17090v1#S3.E2 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")), satisfies St=S0​eLtS\_{t}=S\_{0}e^{L\_{t}}, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​exp⁡{γt+∫0t∫|x|>1x​N​(d​s,d​x)+∫0t∫|x|≤1x​N~​(d​s,d​x)}.S\_{t}=S\_{0}\exp\left\{\gamma\_{t}+\int\_{0}^{t}\int\_{|x|>1}xN(ds,dx)+\int\_{0}^{t}\int\_{|x|\leq 1}x\widetilde{N}(ds,dx)\right\}. |  | (3.4) |

Next, we introduce a sufficient condition under which SS satisfies Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes"). To this end, we denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σt:=∫ℝ0(ex−1)2​π​(t,x)​𝑑x=∂κt​(2)∂t−2​∂κt​(1)∂t\Sigma\_{t}:=\int\_{{\mathbb{R}}\_{0}}(e^{x}-1)^{2}\pi(t,x)dx=\frac{\partial\kappa\_{t}(2)}{\partial t}-2\frac{\partial\kappa\_{t}(1)}{\partial t} |  | (3.5) |

for t∈(0,T]t\in(0,T], and assume that

(A4)
:   0≥μtS>−Σt0\geq\mu^{S}\_{t}>-\Sigma\_{t} for any t∈(0,T]t\in(0,T].

Then, we can see the following:

###### Proposition 3.2.

Under Assumptions (A1)–(A4), SS satisfies Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes").

###### Proof.

For each j=1,2j=1,2, Xt(j):=exp⁡{j​Lt−κt​(j)}X^{(j)}\_{t}:=\exp\{jL\_{t}-\kappa\_{t}(j)\} forms a martingale by (A3) and Remark 3.3 in [[10](https://arxiv.org/html/2602.17090v1#bib.bib10)].
Doob’s inequalty implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|St|2]\displaystyle{\mathbb{E}}\left[\sup\_{t\in[0,T]}|S\_{t}|^{2}\right] | =S02​𝔼​[supt∈[0,T]e2​Lt]=S02​𝔼​[supt∈[0,T]|Xt(1)​eκt​(1)|2]\displaystyle=S^{2}\_{0}{\mathbb{E}}\left[\sup\_{t\in[0,T]}e^{2L\_{t}}\right]=S^{2}\_{0}{\mathbb{E}}\left[\sup\_{t\in[0,T]}\left|X^{(1)}\_{t}e^{\kappa\_{t}(1)}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4​S02​supt∈[0,T]e2​κt​(1)​𝔼​[|XT(1)|2].\displaystyle\leq 4S^{2}\_{0}\sup\_{t\in[0,T]}e^{2\kappa\_{t}(1)}{\mathbb{E}}\left[\left|X^{(1)}\_{T}\right|^{2}\right]. |  |

Note that κt​(1)\kappa\_{t}(1) is a continuous function in tt by Proposition 3.6 of [[10](https://arxiv.org/html/2602.17090v1#bib.bib10)]. Thus, supt∈[0,T]e2​κt​(1)\sup\_{t\in[0,T]}e^{2\kappa\_{t}(1)} is finite.
Moreover, we have |XT(1)|2=XT(2)​exp⁡{κT​(2)−2​κT​(1)}\left|X^{(1)}\_{T}\right|^{2}=X^{(2)}\_{T}\exp\{\kappa\_{T}(2)-2\kappa\_{T}(1)\}. Thus,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|St|2]≤4​S02​supt∈[0,T]e2​κt​(1)​𝔼​[XT(2)]​exp⁡{κT​(2)−2​κT​(1)}<∞.{\mathbb{E}}\left[\sup\_{t\in[0,T]}|S\_{t}|^{2}\right]\leq 4S^{2}\_{0}\sup\_{t\in[0,T]}e^{2\kappa\_{t}(1)}{\mathbb{E}}\left[X^{(2)}\_{T}\right]\exp\{\kappa\_{T}(2)-2\kappa\_{T}(1)\}<\infty. |  |

Note that κT​(2)∈ℝ\kappa\_{T}(2)\in{\mathbb{R}} under (A3).

We can see that (SC1) in Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes") is satisfied by the same sort of argument as Example 2.8 of [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)].
In fact, Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") and (A4), together with the square integrability of SS shown above, ensure that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0T|d​At|)2]\displaystyle{\mathbb{E}}\left[\left(\int\_{0}^{T}|dA\_{t}|\right)^{2}\right] | ≤𝔼​[(∫0TSt−​|μtS|​𝑑t)2]≤𝔼​[supt∈[0,T]|St|2]​(∫0T|μtS|​𝑑t)2\displaystyle\leq{\mathbb{E}}\left[\left(\int\_{0}^{T}S\_{t-}|\mu^{S}\_{t}|dt\right)^{2}\right]\leq{\mathbb{E}}\left[\sup\_{t\in[0,T]}|S\_{t}|^{2}\right]\left(\int\_{0}^{T}|\mu^{S}\_{t}|dt\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[supt∈[0,T]|St|2]​(∫0TΣt​𝑑t)2<∞.\displaystyle\leq{\mathbb{E}}\left[\sup\_{t\in[0,T]}|S\_{t}|^{2}\right]\left(\int\_{0}^{T}\Sigma\_{t}dt\right)^{2}<\infty. |  |

Furthermore, the Burkholder-Davis-Gundy inequality (e.g., see Theorem 48 in Chapter IV in Protter [[12](https://arxiv.org/html/2602.17090v1#bib.bib12)]) implies that there exists a constant CC such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[[M]T]≤C​𝔼​[supt∈[0,T]|Mt|2]≤C​{|S0|2+𝔼​[supt∈[0,T]|St|2]+𝔼​[supt∈[0,T]|At|2]}<∞.{\mathbb{E}}[[M]\_{T}]\leq C{\mathbb{E}}\left[\sup\_{t\in[0,T]}|M\_{t}|^{2}\right]\leq C\left\{|S\_{0}|^{2}+{\mathbb{E}}\left[\sup\_{t\in[0,T]}|S\_{t}|^{2}\right]+{\mathbb{E}}\left[\sup\_{t\in[0,T]}|A\_{t}|^{2}\right]\right\}<\infty. |  |

Next, we focus on (SC2) and (SC3). We can see (SC2) by taking λ\lambda as

|  |  |  |  |
| --- | --- | --- | --- |
|  | λt=μtSSt−​Σt,t∈(0,T].\lambda\_{t}=\frac{\mu^{S}\_{t}}{S\_{t-}\Sigma\_{t}},\ \ \ t\in(0,T]. |  | (3.6) |

Note that this is well-defined from the view of Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"). Furthermore, (A4) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tλt2​d​⟨M⟩t\displaystyle\int\_{0}^{T}\lambda^{2}\_{t}d\langle M\rangle\_{t} | =∫0T(μtS)2Σt​𝑑t≤∫0T|μtS|​𝑑t=−∫0TμtS​𝑑t\displaystyle=\int\_{0}^{T}\frac{\left(\mu^{S}\_{t}\right)^{2}}{\Sigma\_{t}}dt\leq\int\_{0}^{T}|\mu^{S}\_{t}|dt=-\int\_{0}^{T}\mu^{S}\_{t}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|γT|+|∫0T∫ℝ0(ex−1−x​𝟏{|x|≤1})​π​(t,x)​𝑑x​𝑑t|<∞.\displaystyle\leq|\gamma\_{T}|+\left|\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left(e^{x}-1-x{\bf 1}\_{\{|x|\leq 1\}}\right)\pi(t,x)dxdt\right|<\infty. |  |

It is obvious that the process KK is continuous. As a result, (SC3) follows.
□\Box

###### Remark 3.3.

We can show Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") and Proposition [3.2](https://arxiv.org/html/2602.17090v1#S3.Thmthm2 "Proposition 3.2. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") even if we weaken (A3) to ∫0T∫|x|>1e2​x​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{|x|>1}e^{2x}\overline{\nu}(ds,dx)<\infty}.

Next, we investigate the stochastic process ZZ defined as the solution to the SDE ([2.2](https://arxiv.org/html/2602.17090v1#S2.E2 "In 2 Preliminaries ‣ Local risk-minimization for exponential additive processes")).
For t∈[0,T]t\in[0,T] and x∈ℝ0x\in{\mathbb{R}}\_{0}, denote

|  |  |  |
| --- | --- | --- |
|  | θt,x:=λt​St−​(ex−1)=μtS​(ex−1)Σt,\theta\_{t,x}:=\lambda\_{t}S\_{t-}(e^{x}-1)=\frac{\mu^{S}\_{t}(e^{x}-1)}{\Sigma\_{t}}, |  |

where λt\lambda\_{t} is defined in ([3.6](https://arxiv.org/html/2602.17090v1#S3.E6 "In Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")). We can then rewrite the SDE ([2.2](https://arxiv.org/html/2602.17090v1#S2.E2 "In 2 Preliminaries ‣ Local risk-minimization for exponential additive processes")) as d​Zt=Zt−​d​MtλdZ\_{t}=Z\_{t-}dM^{\lambda}\_{t}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mtλ=−∫0t∫ℝ0θs,x​N~​(d​s,d​x).M^{\lambda}\_{t}=-\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\theta\_{s,x}\widetilde{N}(ds,dx). |  | (3.7) |

Here, we show that ZZ is positive and square integrable. To this end, we add two more assumptions and prepare three lemmas as follows:

(A5)
:   ∫0T∫−∞−1|log⁡(1−θt,x)|2​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{-\infty}^{-1}|\log(1-\theta\_{t,x})|^{2}\overline{\nu}(dt,dx)<\infty}.

(A6)
:   ∫0T∫0<|x|≤1|ex−1|​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{0<|x|\leq 1}|e^{x}-1|\overline{\nu}(ds,dx)<\infty}, equivalently, ∫0T∫0<|x|≤1|x|​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{0<|x|\leq 1}|x|\overline{\nu}(ds,dx)<\infty}.

###### Lemma 3.4.

Assuming (A3), we have ∫0T∫ℝ0|ex−1|k​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|e^{x}-1|^{k}\overline{\nu}(dt,dx)<\infty} for k=3,4k=3,4.

###### Proof.

For k=3,4k=3,4, we have the following: |ex−1|k≤e4​x|e^{x}-1|^{k}\leq e^{4x} if x≥1x\geq 1, and |ex−1|k≤1|e^{x}-1|^{k}\leq 1 if x≤−1x\leq-1.
Moreover, |ex−1|k≤(e−1)k​xk≤(e−1)4​x2|e^{x}-1|^{k}\leq(e-1)^{k}x^{k}\leq(e-1)^{4}x^{2} if 0<x≤10<x\leq 1, and |ex−1|k≤|x|k≤x2|e^{x}-1|^{k}\leq|x|^{k}\leq x^{2} if −1≤x<0-1\leq x<0.
Thus, (A3) implies that ∫0T∫ℝ0|ex−1|k​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|e^{x}-1|^{k}\overline{\nu}(dt,dx)<\infty} for k=3,4k=3,4.
□\Box

###### Lemma 3.5.

Under Assumptions (A1)–(A5), ∫0T∫ℝ0|log⁡(1−θt,x)|2​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|\log(1-\theta\_{t,x})|^{2}\overline{\nu}(dt,dx)<\infty} holds.

###### Proof.

(A4) implies that 0≤log⁡(1−θt,x)≤(ex−1)0\leq\log(1-\theta\_{t,x})\leq(e^{x}-1) when x>0x>0. Thus, we have

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫0∞|log⁡(1−θt,x)|2​ν¯​(d​t,d​x)≤∫0T∫0∞(ex−1)2​ν¯​(d​t,d​x)<∞\int\_{0}^{T}\int\_{0}^{\infty}|\log(1-\theta\_{t,x})|^{2}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{0}^{\infty}(e^{x}-1)^{2}\overline{\nu}(dt,dx)<\infty |  |

by Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"). For x∈[−1,0)x\in[-1,0), we have

|  |  |  |
| --- | --- | --- |
|  | 0≥log⁡(1−θt,x)≥log⁡(1−θt,−1)θt,−1​θt,x=log⁡(1−θt,−1)e−1−1​(ex−1),0\geq\log(1-\theta\_{t,x})\geq\frac{\log(1-\theta\_{t,-1})}{\theta\_{t,-1}}\theta\_{t,x}=\frac{\log(1-\theta\_{t,-1})}{e^{-1}-1}(e^{x}-1), |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫−10|log⁡(1−θt,x)|2​ν¯​(d​t,d​x)≤∫0T∫−10(ex−1)2​ν¯​(d​t,d​x)<∞.\int\_{0}^{T}\int\_{-1}^{0}|\log(1-\theta\_{t,x})|^{2}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{-1}^{0}\left(e^{x}-1\right)^{2}\overline{\nu}(dt,dx)<\infty. |  |

Together with (A5), Lemma [3.5](https://arxiv.org/html/2602.17090v1#S3.Thmthm5 "Lemma 3.5. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") follows.
□\Box

###### Lemma 3.6.

Under Assumptions (A1)–(A6), ∫0T∫ℝ0(|θt,x|+|log⁡(1−θt,x)|)​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left(|\theta\_{t,x}|+|\log(1-\theta\_{t,x})|\right)\overline{\nu}(dt,dx)<\infty}.

###### Proof.

First, (A6), together with (A3), ensures that ∫0T∫ℝ0|ex−1|​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|e^{x}-1|\overline{\nu}(ds,dx)<\infty}.
Since |ex−1|≤(e−1)​|x||e^{x}-1|\leq(e-1)|x| when |x|≤1|x|\leq 1, |θt,x||\theta\_{t,x}| is integrable with respect to ν¯\overline{\nu} by (A4).
By the same way as the proof of Lemma [3.5](https://arxiv.org/html/2602.17090v1#S3.Thmthm5 "Lemma 3.5. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"), we can see the integrability condition for |log⁡(1−θt,x)||\log(1-\theta\_{t,x})|.
In fact, (A5), together with ∫0T∫−∞−1ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{-\infty}^{-1}\overline{\nu}(dt,dx)<\infty}, yields that

|  |  |  |
| --- | --- | --- |
|  | ∫0T∫−∞−1|log⁡(1−θt,x)|​ν¯​(d​t,d​x)≤∫0T∫−∞−1(1∨|log⁡(1−θt,x)|2)​ν¯​(d​t,d​x)<∞.\int\_{0}^{T}\int\_{-\infty}^{-1}|\log(1-\theta\_{t,x})|\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{-\infty}^{-1}\left(1\vee|\log(1-\theta\_{t,x})|^{2}\right)\overline{\nu}(dt,dx)<\infty. |  |

□\Box

###### Remark 3.7.

1. 1.

   The condition

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫0T∫−∞−1{log⁡(1+μtSΣt)}2​ν¯​(d​s,d​x)<∞\int\_{0}^{T}\int\_{-\infty}^{-1}\left\{\log\left(1+\frac{\mu^{S}\_{t}}{\Sigma\_{t}}\right)\right\}^{2}\overline{\nu}(ds,dx)<\infty |  | (3.8) |

   is a sufficient condition for (A5). In fact, when x<−1x<-1, we have

   |  |  |  |
   | --- | --- | --- |
   |  | 0≥log⁡(1−θt,x)≥log⁡(1+μtSΣt),0\geq\log(1-\theta\_{t,x})\geq\log\left(1+\frac{\mu^{S}\_{t}}{\Sigma\_{t}}\right), |  |

   from which ([3.8](https://arxiv.org/html/2602.17090v1#S3.E8 "In item 1 ‣ Remark 3.7. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) implies that

   |  |  |  |
   | --- | --- | --- |
   |  | ∫0T∫−∞−1|log⁡(1−θt,x)|2​ν¯​(d​t,d​x)≤∫0T∫−∞−1{log⁡(1+μtSΣt)}2​ν¯​(d​s,d​x)<∞.\int\_{0}^{T}\int\_{-\infty}^{-1}|\log(1-\theta\_{t,x})|^{2}\overline{\nu}(dt,dx)\leq\int\_{0}^{T}\int\_{-\infty}^{-1}\left\{\log\left(1+\frac{\mu^{S}\_{t}}{\Sigma\_{t}}\right)\right\}^{2}\overline{\nu}(ds,dx)<\infty. |  |
2. 2.

   When the log-price process LL is a Lévy process, μtS\mu^{S}\_{t} and Σt\Sigma\_{t} do not depend on tt.
   Thus, it is possible to simplify (A5) as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | μtSΣt>−1+ε\frac{\mu^{S}\_{t}}{\Sigma\_{t}}>-1+\varepsilon |  | (3.9) |

   for some ε>0\varepsilon>0, e.g., see Arai et al. [[2](https://arxiv.org/html/2602.17090v1#bib.bib2)]; however, ([3.9](https://arxiv.org/html/2602.17090v1#S3.E9 "In item 2 ‣ Remark 3.7. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) is too restrictive for the additive process case.

With the above preparations, we prove the following proposition:

###### Proposition 3.8.

Suppose Assumptions (A1)–(A6). Then, ZZ is a positive square integrable martingale.

###### Proof.

(A4) ensures that θt,x<1\theta\_{t,x}<1, that is, MλM^{\lambda} defined in ([3.7](https://arxiv.org/html/2602.17090v1#S3.E7 "In Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) satisfies that Δ​Mtλ>−1\Delta M^{\lambda}\_{t}>-1 for any t∈[0,T]t\in[0,T].
Furthermore, Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") ensures that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[[Mλ]T]=𝔼​[∫0T∫ℝ0θt,x2​N​(d​t,d​x)]=∫0T∫ℝ0θt,x2​ν¯​(d​t,d​x)<∞,{\mathbb{E}}\left[[M^{\lambda}]\_{T}\right]={\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\theta\_{t,x}^{2}N(dt,dx)\right]=\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\theta\_{t,x}^{2}\overline{\nu}(dt,dx)<\infty, |  |

from which MλM^{\lambda} is a uniformly integrable martingale by Corollary 3 of Theorem 26 in Chapter II of [[12](https://arxiv.org/html/2602.17090v1#bib.bib12)].
Thus, Theorem 2 of H. Sato [[13](https://arxiv.org/html/2602.17090v1#bib.bib13)] implies that Z=ℰ​(Mλ)Z={\mathcal{E}}(M^{\lambda}) is a positive uniformly integrable martingale, and it is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt=exp⁡{∫0t∫ℝ0log⁡(1−θs,x)​N~​(d​s,d​x)+∫0t∫ℝ0(log⁡(1−θs,x)+θs,x)​ν¯​(d​s,d​x)}.Z\_{t}=\exp\left\{\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\log(1-\theta\_{s,x})\widetilde{N}(ds,dx)+\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(\log(1-\theta\_{s,x})+\theta\_{s,x}\right)\overline{\nu}(ds,dx)\right\}. |  | (3.10) |

Note that the two integrals in ([3.10](https://arxiv.org/html/2602.17090v1#S3.E10 "In Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) are well-defined from the view of Lemma [3.6](https://arxiv.org/html/2602.17090v1#S3.Thmthm6 "Lemma 3.6. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"). We have then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt2\displaystyle Z^{2}\_{t} | =exp⁡{2​∫0t∫ℝ0log⁡(1−θs,x)​N~​(d​s,d​x)+2​∫0t∫ℝ0(log⁡(1−θs,x)+θs,x)​ν¯​(d​s,d​x)}\displaystyle=\exp\left\{2\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\log(1-\theta\_{s,x})\widetilde{N}(ds,dx)+2\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(\log(1-\theta\_{s,x})+\theta\_{s,x}\right)\overline{\nu}(ds,dx)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp{∫0t∫ℝ0log(1−2θs,x+θs,x2)N~(ds,dx)\displaystyle=\exp\Bigg\{\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\log(1-2\theta\_{s,x}+\theta^{2}\_{s,x})\widetilde{N}(ds,dx) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t∫ℝ0(log(1−2θs,x+θs,x2)+2θs,x−θs,x2)ν¯(ds,dx)+∫0t∫ℝ0θs,x2ν¯(ds,dx)}\displaystyle\hskip 14.22636pt+\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(\log(1-2\theta\_{s,x}+\theta^{2}\_{s,x})+2\theta\_{s,x}-\theta^{2}\_{s,x}\right)\overline{\nu}(ds,dx)+\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\theta^{2}\_{s,x}\overline{\nu}(ds,dx)\Bigg\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℰt​(M¯θ)​exp⁡{∫0t∫ℝ0θs,x2​ν¯​(d​s,d​x)},\displaystyle={\mathcal{E}}\_{t}\left(\overline{M}^{\theta}\right)\exp\left\{\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\theta^{2}\_{s,x}\overline{\nu}(ds,dx)\right\}, |  |

where M¯θ={M¯tθ}t∈[0,T]\overline{M}^{\theta}=\{\overline{M}^{\theta}\_{t}\}\_{t\in[0,T]} is the process defined as

|  |  |  |
| --- | --- | --- |
|  | M¯tθ:=∫0t∫ℝ0(−2​θs,x+θs,x2)​N~​(d​s,d​x),t∈[0,T].\overline{M}^{\theta}\_{t}:=\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(-2\theta\_{s,x}+\theta^{2}\_{s,x}\right)\widetilde{N}(ds,dx),\ \ \ t\in[0,T]. |  |

It is enough to see the integrability of ℰt​(M¯θ){\mathcal{E}}\_{t}\left(\overline{M}^{\theta}\right), since ∫0t∫ℝ0θs,x2​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\theta^{2}\_{s,x}\overline{\nu}(ds,dx)<\infty}.
To this end, we calculate the expectation of the quadratic variation of M¯θ\overline{M}^{\theta}.
From the view of Lemmas [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") and [3.4](https://arxiv.org/html/2602.17090v1#S3.Thmthm4 "Lemma 3.4. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[[M¯θ]T]\displaystyle{\mathbb{E}}\left[\left[\overline{M}^{\theta}\right]\_{T}\right] | =𝔼​[∫0T∫ℝ0(−2​θt,x+θt,x2)2​N​(d​t,d​x)]\displaystyle={\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left(-2\theta\_{t,x}+\theta^{2}\_{t,x}\right)^{2}N(dt,dx)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T∫ℝ0(4​θt,x2−4​θt,x3+θt,x4)​N​(d​t,d​x)]\displaystyle={\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left(4\theta^{2}\_{t,x}-4\theta^{3}\_{t,x}+\theta^{4}\_{t,x}\right)N(dt,dx)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0T∫ℝ0(4​θt,x2−4​θt,x3+θt,x4)​ν¯​(d​t,d​x)<∞,\displaystyle=\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left(4\theta^{2}\_{t,x}-4\theta^{3}\_{t,x}+\theta^{4}\_{t,x}\right)\overline{\nu}(dt,dx)<\infty, |  |

which implies that M¯θ\overline{M}^{\theta} is a uniformly integrable martingale.
Using Theorem 2 of [[13](https://arxiv.org/html/2602.17090v1#bib.bib13)] again, we obtain that ℰ​(M¯θ){\mathcal{E}}\left(\overline{M}^{\theta}\right) is a uniformly integrable martingale.
□\Box

From the view of the discussion so far, Assumptions (A1)–(A6) implies that the product process Z​SZS is a martingale,
and the MMM ℙ∗{\mathbb{P}}^{\*} exists with the Radon-Nikodym density d​ℙ∗d​ℙ=ZT\displaystyle{\frac{d{\mathbb{P}}^{\*}}{d{\mathbb{P}}}=Z\_{T}}.

###### Remark 3.9.

[[1](https://arxiv.org/html/2602.17090v1#bib.bib1)] used Theorem 117 of Situ [[16](https://arxiv.org/html/2602.17090v1#bib.bib16)] to show the square integrabilities of SS and ZZ for the case where ν¯\overline{\nu} is stationary.
However, Theorem 117 in [[16](https://arxiv.org/html/2602.17090v1#bib.bib16)] is not available for the non-stationary case. That is why we take a different approach in this paper.

## 4 LRM strategies for exponential additive processes

The objectives of this section are to derive a mathematical expression of LRM strategies for exponential additive models
and evolve it to a numerically tractable form.
Throughout this section, SS denotes the exponential additive process defined in ([3.2](https://arxiv.org/html/2602.17090v1#S3.E2 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) or, equivalently, ([3.4](https://arxiv.org/html/2602.17090v1#S3.E4 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")),
and we consider call options as the claims to be hedged. We denote F:=(ST−K)+F:=(S\_{T}-K)^{+}, where K>0K>0 is the strike price.

### 4.1 On the result of Handa et al. [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)]

Handa et al. [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] also discussed local risk-minimization for additive processes.
Note that their discussion is based on the Malliavin-Skorohod calculus undertaken by Di Nunno and Vives [[6](https://arxiv.org/html/2602.17090v1#bib.bib6)].
In this subsection, we examine Theorem 5.15 of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)].

In the Malliavin-Skorohod calculus, the sample space Ω\Omega must be the canonical space for a pure jump additive process,
of which each element is represented by arranging data from all jumps.
More precisely, ω∈Ω\omega\in\Omega is written as ω=((t1,x1),(t2,x2),…)\omega=((t\_{1},x\_{1}),(t\_{2},x\_{2}),\dots),
where ω\omega corresponds to the path with jumps of size xix\_{i} at time tit\_{i} for i=1,2,…i=1,2,\dots.
Note that Ω\Omega includes all finite and infinite sequences as well as the empty sequence.
Now, we denote εt,x+ω:=((t,x),(t1,,x1),(t2,x2),…)\varepsilon^{+}\_{t,x}\omega:=((t,x),(t\_{1},,x\_{1}),(t\_{2},x\_{2}),\dots), where ω=((t1,x1),(t2,x2),…)\omega=((t\_{1},x\_{1}),(t\_{2},x\_{2}),\dots).
That is, εt,x+​ω\varepsilon^{+}\_{t,x}\omega is the element of Ω\Omega by adding to ω\omega a jump of size xx at time tt.
Then, for a random variable XX on Ω\Omega, we define the differential operator Ψt,x\Psi\_{t,x} as

|  |  |  |
| --- | --- | --- |
|  | Ψt,x​X​(ω):=X​(εt,x+​ω)−X​(ω).\Psi\_{t,x}X(\omega):=X(\varepsilon^{+}\_{t,x}\omega)-X(\omega). |  |

In this paper, we no longer mention the Malliavin-Skorohod calculus. For its details, see [[6](https://arxiv.org/html/2602.17090v1#bib.bib6)] and [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)].

Let us go back to LRM strategies. [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] treated financial market models in which the asset price process SS is given by ℰ​(MH){\mathcal{E}}(M^{H}),
where MH={MtH}t∈[0,T]M^{H}=\{M^{H}\_{t}\}\_{t\in[0,T]} is a process expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | MtH=∫0tαs​𝑑s+∫0t∫ℝ0βs,x​N~​(d​s,d​x).M^{H}\_{t}=\int\_{0}^{t}\alpha\_{s}ds+\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\beta\_{s,x}\widetilde{N}(ds,dx). |  | (4.1) |

Here, α\alpha and β\beta are predictable processes, and N~\widetilde{N} is the same one as defined in Section 3.
Furthermore, in their Theorem 5.15, they derived an expression for LRM strategies in this model framework. Now, we modify it to fit our setting.

###### Proposition 4.1.

Suppose the following five conditions:

(B1)
:   ∫0T∫ℝ0|θt,x|​ν¯​(d​t,d​x)​<∞​ and ​∫0T∫ℝ0|​log⁡(1−θt,x)|ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|\theta\_{t,x}|\overline{\nu}(dt,dx)<\infty\ \mbox{ and }\ \int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|\log(1-\theta\_{t,x})|\overline{\nu}(dt,dx)<\infty}.

(B2)
:   𝔼​[ZT​F]<∞{\mathbb{E}}[Z\_{T}F]<\infty, 𝔼​[ZT​|Ψt,x​F|]<∞{\mathbb{E}}[Z\_{T}|\Psi\_{t,x}F|]<\infty for any t≥0t\geq 0 and x∈ℝ0x\in{\mathbb{R}}\_{0},
    and 
      
    𝔼​[∫0T∫ℝ0|Ψt,x​(ZT​F)|​ν¯​(d​t,d​x)]<∞\displaystyle{{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|\Psi\_{t,x}(Z\_{T}F)|\overline{\nu}(dt,dx)\right]<\infty}.

(B3)
:   The structure condition (SC), that is, Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes").

(B4)
:   ZZ is a positive square integrable martingale; and satisfies the reverse Hölder inequality,
    in other words, we can find a constant C>0C>0 such that 𝔼​[ZT2|ℱt−]≤C​Zt−2{\mathbb{E}}[Z\_{T}^{2}|{\mathcal{F}}\_{t-}]\leq CZ\_{t-}^{2} for any t∈(0,T]t\in(0,T].

(B5)
:   𝔼​[∫0T∫ℝ0|Ψt,x​F|2​ν¯​(d​t,d​x)]<∞\displaystyle{{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|\Psi\_{t,x}F|^{2}\overline{\nu}(dt,dx)\right]<\infty}.

Then, the LRM strategy ξ1,F\xi^{1,F} for the call option F=(ST−K)+F=(S\_{T}-K)^{+} is represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt1,F=1St−​Σt​∫ℝ0𝔼ℙ∗​[Ψt,x​F|ℱt−]​(ex−1)​π​(t,x)​𝑑x,\xi^{1,F}\_{t}=\frac{1}{S\_{t-}\Sigma\_{t}}\int\_{{\mathbb{R}}\_{0}}{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[\Psi\_{t,x}F|{\mathcal{F}}\_{t-}](e^{x}-1)\pi(t,x)dx, |  | (4.2) |

where Σt:=∫ℝ0(ex−1)2​π​(t,x)​𝑑x\displaystyle{\Sigma\_{t}:=\int\_{{\mathbb{R}}\_{0}}(e^{x}-1)^{2}\pi(t,x)dx}.

###### Proof.

Theorem 5.15 in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] shows that ([4.2](https://arxiv.org/html/2602.17090v1#S4.E2 "In Proposition 4.1. ‣ 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) holds under their Assumptions 4.2, 5.9, and 5.11, and (5.12);
but note that νt\nu\_{t} and ν¯\overline{\nu} are used incorrectly in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)].
Thus, we have only to verify whether the assumptions in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] hold under the five conditions (B1)-(B5).

Remark that Ψt,x​v=0\Psi\_{t,x}v=0 when vv is a deterministic function. Moreover,

|  |  |  |
| --- | --- | --- |
|  | Ψt,x​(ZT​F)=ZT​Ψt,x​F+F​Ψt,x​ZT+Ψt,x​ZT​Ψt,x​F\Psi\_{t,x}(Z\_{T}F)=Z\_{T}\Psi\_{t,x}F+F\Psi\_{t,x}Z\_{T}+\Psi\_{t,x}Z\_{T}\Psi\_{t,x}F |  |

holds by the definition of Ψt,x\Psi\_{t,x}. Additionally, H~t,z\widetilde{H}\_{t,z}, which appears in Assumption 4.2 of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)], is given by 1 in our setting.
Thus, Assumption 4.2 of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] is reduced to (B2) and “θ+log⁡(1−θ)\theta+\log(1-\theta), log⁡(1−θ)∈DomΦ\log(1-\theta)\in\mathop{\mathrm{Dom}}\nolimits\Phi”,
where we do not introduce the definition of DomΦ\mathop{\mathrm{Dom}}\nolimits\Phi, but Remark 5.9 of [[6](https://arxiv.org/html/2602.17090v1#bib.bib6)] ensures that v∈L1​(ν¯×ℙ)v\in L^{1}(\overline{\nu}\times{\mathbb{P}}) is a sufficient condition for v∈DomΦv\in\mathop{\mathrm{Dom}}\nolimits\Phi.
As a result, Assumption 4.2 of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] is derived from (B1) and (B2).
Next, Assumption 5.9 in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] is the same as (B3). In addition, Assumption 5.11 in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] is satisfied by combining (B2) with (B4).

Only (5.12) in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] remains. It can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T∫ℝ0(𝔼ℙ∗​[Ψt,x​F|ℱt−])2​ν¯​(d​t,d​x)]<∞{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left({\mathbb{E}}\_{{\mathbb{P}}^{\*}}[\Psi\_{t,x}F|{\mathcal{F}}\_{t-}]\right)^{2}\overline{\nu}(dt,dx)\right]<\infty |  |

from the view of (5.14) of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] by substituting 1 for Ht,z∗H^{\*}\_{t,z} in (5.14) of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)].
Thus, (B5), together with the reverse Hölder inequality of ZZ and Fubini’s theorem, implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T∫ℝ0(𝔼ℙ∗​[Ψt,x​F|ℱt−])2​ν¯​(d​t,d​x)]\displaystyle{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left({\mathbb{E}}\_{{\mathbb{P}}^{\*}}[\Psi\_{t,x}F|{\mathcal{F}}\_{t-}]\right)^{2}\overline{\nu}(dt,dx)\right] | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T∫ℝ0(𝔼​[ZTZt−​Ψt,x​F|ℱt−])2​ν¯​(d​t,d​x)]\displaystyle={\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left({\mathbb{E}}\left[\frac{Z\_{T}}{Z\_{t-}}\Psi\_{t,x}F\Big|{\mathcal{F}}\_{t-}\right]\right)^{2}\overline{\nu}(dt,dx)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[∫0T∫ℝ0𝔼​[ZT2Zt−2|ℱt−]​𝔼​[|Ψt,x​F|2|ℱt−]​ν¯​(d​t,d​x)]\displaystyle\leq{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}{\mathbb{E}}\left[\frac{Z^{2}\_{T}}{Z^{2}\_{t-}}\Big|{\mathcal{F}}\_{t-}\right]{\mathbb{E}}\left[|\Psi\_{t,x}F|^{2}\Big|{\mathcal{F}}\_{t-}\right]\overline{\nu}(dt,dx)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​𝔼​[∫0T∫ℝ0𝔼​[|Ψt,x​F|2|ℱt−]​ν¯​(d​t,d​x)]\displaystyle\leq C{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}{\mathbb{E}}[|\Psi\_{t,x}F|^{2}|{\mathcal{F}}\_{t-}]\overline{\nu}(dt,dx)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​𝔼​[∫0T∫ℝ0|Ψt,x​F|2​ν¯​(d​t,d​x)]<∞,\displaystyle\leq C{\mathbb{E}}\left[\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}|\Psi\_{t,x}F|^{2}\overline{\nu}(dt,dx)\right]<\infty, |  |

from which (5.12) in [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] follows. This completes the proof of Proposition [4.1](https://arxiv.org/html/2602.17090v1#S4.Thmthm1 "Proposition 4.1. ‣ 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes").
□\Box

### 4.2 Main theorem

[[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] asserts in their Corollary 5.17 that an expression for LRM strategies, when α\alpha and β\beta in ([4.1](https://arxiv.org/html/2602.17090v1#S4.E1 "In 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) are continuously deterministic functions,
can be derived by the same argument as [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)]; however, as mentioned in Remark [3.9](https://arxiv.org/html/2602.17090v1#S3.Thmthm9 "Remark 3.9. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"), the argument in [[1](https://arxiv.org/html/2602.17090v1#bib.bib1)] cannot be applied directly to the case of additive processes.
That is why we employ a different approach to show the square integrability of ZZ and SS in the previous section.
In this subsection, we correct Corollary 5.17 of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] and examine a mathematical expression for LRM strategies in exponential additive models once again.
Therefore, we show that ([4.2](https://arxiv.org/html/2602.17090v1#S4.E2 "In Proposition 4.1. ‣ 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) holds even if we replace the conditions (B1)-(B5) with (A1)-(A6).
Here, the conditions (A1)-(A6) are mainly the integrability conditions on the Lévy measure, which are formulated in a useful way to conduct the numerical experiments discussed later.
To simplify notation, the conditions (A1)–(A6) will be collectively referred to Assumption [A](https://arxiv.org/html/2602.17090v1#ThmassA1 "Assumption A. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes") as follows:

###### Assumption A.

(A1)
:   γt\gamma\_{t} is differentiable, that is, it is expressed as γt=∫0tγs′​𝑑s\displaystyle{\gamma\_{t}=\int\_{0}^{t}\gamma^{\prime}\_{s}ds}.

(A2)
:   The Lévy measure ν¯\overline{\nu} is absolutely continuous with respect to d​t×d​xdt\times dx, that is,
    there is a non-negative function π\pi such that ν¯​(d​t,d​x)=π​(t,x)​d​t​d​x\overline{\nu}(dt,dx)=\pi(t,x)dtdx for any t∈(0,T]t\in(0,T] and any x∈ℝ0x\in{\mathbb{R}}\_{0}.

(A3)
:   ∫0T∫|x|>1e4​x​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{|x|>1}e^{4x}\overline{\nu}(ds,dx)<\infty}.

(A4)
:   0≥μtS>−Σt0\geq\mu^{S}\_{t}>-\Sigma\_{t} for any t∈(0,T]t\in(0,T], where μtS\mu^{S}\_{t} and Σt\Sigma\_{t} are defined in ([3.3](https://arxiv.org/html/2602.17090v1#S3.E3 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) and ([3.5](https://arxiv.org/html/2602.17090v1#S3.E5 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")), respectively.

(A5)
:   ∫0T∫−∞−1|log⁡(1−θt,x)|2​ν¯​(d​t,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{-\infty}^{-1}|\log(1-\theta\_{t,x})|^{2}\overline{\nu}(dt,dx)<\infty}. Recall that θt,x:=μtS​(ex−1)Σt\displaystyle{\theta\_{t,x}:=\frac{\mu^{S}\_{t}(e^{x}-1)}{\Sigma\_{t}}}.

(A6)
:   ∫0T∫0<|x|≤1|ex−1|​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{0<|x|\leq 1}|e^{x}-1|\overline{\nu}(ds,dx)<\infty}, equivalently, ∫0T∫0<|x|≤1|x|​ν¯​(d​s,d​x)<∞\displaystyle{\int\_{0}^{T}\int\_{0<|x|\leq 1}|x|\overline{\nu}(ds,dx)<\infty}.

###### Theorem 4.2.

([4.2](https://arxiv.org/html/2602.17090v1#S4.E2 "In Proposition 4.1. ‣ 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) holds under Assumption [A](https://arxiv.org/html/2602.17090v1#ThmassA1 "Assumption A. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes").

###### Proof.

It suffices to see that all of (B1)–(B5) hold under Assumption [A](https://arxiv.org/html/2602.17090v1#ThmassA1 "Assumption A. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes").
Lemma [3.6](https://arxiv.org/html/2602.17090v1#S3.Thmthm6 "Lemma 3.6. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") and Proposition [3.8](https://arxiv.org/html/2602.17090v1#S3.Thmthm8 "Proposition 3.8. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") guarantee (B1) and the first condition of (B4), respectively. As seen in Proposition [3.2](https://arxiv.org/html/2602.17090v1#S3.Thmthm2 "Proposition 3.2. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"), (B3) follows.
In addition, supt∈[0,T]|St|\displaystyle{\sup\_{t\in[0,T]}|S\_{t}|} is square integrable by the proof of Proposition [3.2](https://arxiv.org/html/2602.17090v1#S3.Thmthm2 "Proposition 3.2. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes").
Hence, we obtain the first condition of (B2). A similar calculation to Lemmas 5.21 and 5.22 of [[11](https://arxiv.org/html/2602.17090v1#bib.bib11)] provides

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψt,x​F=Ψt,x​(ST−K)+=(ex​ST−K)+−(ST−K)+.\Psi\_{t,x}F=\Psi\_{t,x}(S\_{T}-K)^{+}=(e^{x}S\_{T}-K)^{+}-(S\_{T}-K)^{+}. |  | (4.3) |

Thus, |Ψt,x​F|≤(ex+1)​ST|\Psi\_{t,x}F|\leq(e^{x}+1)S\_{T}, which implies the second condition of (B2).
Next, we examine the second condition of (B4).
First, Z=ℰ​(Mλ)Z={\mathcal{E}}(M^{\lambda}) and ⟨Mλ⟩=K\langle M^{\lambda}\rangle=K hold, where MλM^{\lambda} is defined in ([3.7](https://arxiv.org/html/2602.17090v1#S3.E7 "In Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) and KK is defined in (SC3) of Assumption [2.1](https://arxiv.org/html/2602.17090v1#S2.Thmthm1 "Assumption 2.1. ‣ 2 Preliminaries ‣ Local risk-minimization for exponential additive processes").
Note that KTK\_{T} is finite and deterministic, that is, in L∞L^{\infty}; and MλM^{\lambda} is a square integrable martingale by the proof of Proposition [3.8](https://arxiv.org/html/2602.17090v1#S3.Thmthm8 "Proposition 3.8. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes").
Thus, Proposition 3.7 of Choulli et al. [[5](https://arxiv.org/html/2602.17090v1#bib.bib5)] implies that ZZ satisfies the reverse Hölder inequality.

Now, we present (B5) before proving the third condition of (B2). By ([4.3](https://arxiv.org/html/2602.17090v1#S4.E3 "In Proof. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ψt,x​F)2\displaystyle(\Psi\_{t,x}F)^{2} | ={(ex​ST−K)+−(ST−K)+}2\displaystyle=\left\{(e^{x}S\_{T}-K)^{+}-(S\_{T}-K)^{+}\right\}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(ex−1)2​ST2​𝟏{ST≥K}​𝟏{x≥log⁡(K/ST)}+(ST−K)2​𝟏{ST≥K}​𝟏{x<log⁡(K/ST)}\displaystyle=(e^{x}-1)^{2}S\_{T}^{2}{\bf 1}\_{\{S\_{T}\geq K\}}{\bf 1}\_{\{x\geq\log(K/S\_{T})\}}+(S\_{T}-K)^{2}{\bf 1}\_{\{S\_{T}\geq K\}}{\bf 1}\_{\{x<\log(K/S\_{T})\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(ex​ST−K)2​𝟏{ST<K}​𝟏{x≥log⁡(K/ST)}\displaystyle\hskip 14.22636pt+(e^{x}S\_{T}-K)^{2}{\bf 1}\_{\{S\_{T}<K\}}{\bf 1}\_{\{x\geq\log(K/S\_{T})\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(ex−1)2​ST2​𝟏{ST≥K}​𝟏{x≥log⁡(K/ST)}+(ST−ex​ST)2​𝟏{ST≥K}​𝟏{x<log⁡(K/ST)}\displaystyle\leq(e^{x}-1)^{2}S\_{T}^{2}{\bf 1}\_{\{S\_{T}\geq K\}}{\bf 1}\_{\{x\geq\log(K/S\_{T})\}}+(S\_{T}-e^{x}S\_{T})^{2}{\bf 1}\_{\{S\_{T}\geq K\}}{\bf 1}\_{\{x<\log(K/S\_{T})\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(ex​ST−ST)2​𝟏{ST<K}​𝟏{x≥log⁡(K/ST)}\displaystyle\hskip 14.22636pt+(e^{x}S\_{T}-S\_{T})^{2}{\bf 1}\_{\{S\_{T}<K\}}{\bf 1}\_{\{x\geq\log(K/S\_{T})\}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤(ex−1)2​ST2.\displaystyle\leq(e^{x}-1)^{2}S\_{T}^{2}. |  | (4.4) |

By (A3), Lemma [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes"), and the square integrability of STS\_{T}, (B5) is satisfied.

It remains to show the third condition of (B2). To this end, we calculate Ψt,x​(ZT​F)\Psi\_{t,x}(Z\_{T}F).
By the definition of Ψt,x\Psi\_{t,x}, we have Ψt,x​ZT=−θt,x​ZT\Psi\_{t,x}Z\_{T}=-\theta\_{t,x}Z\_{T}. Thus, ([4.3](https://arxiv.org/html/2602.17090v1#S4.E3 "In Proof. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψt,x​(ZT​F)\displaystyle\Psi\_{t,x}(Z\_{T}F) | =ZT​Ψt,x​F+F​Ψt,x​ZT+Ψt,x​F⋅Ψt,x​ZT\displaystyle=Z\_{T}\Psi\_{t,x}F+F\Psi\_{t,x}Z\_{T}+\Psi\_{t,x}F\cdot\Psi\_{t,x}Z\_{T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ZT​Ψt,x​F−θt,x​ZT​(F+Ψt,x​F)=ZT​Ψt,x​F−θt,x​ZT​(ex​ST−K)+.\displaystyle=Z\_{T}\Psi\_{t,x}F-\theta\_{t,x}Z\_{T}(F+\Psi\_{t,x}F)=Z\_{T}\Psi\_{t,x}F-\theta\_{t,x}Z\_{T}(e^{x}S\_{T}-K)^{+}. |  |

We have then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Ψt,x​(ZT​F)|\displaystyle|\Psi\_{t,x}(Z\_{T}F)| | ≤ZT​{|Ψt,x​F|+|θt,x|​(ex​ST−K)+}≤ZT​|ex−1|​(ST+|μtS|Σt​ex​ST)\displaystyle\leq Z\_{T}\left\{|\Psi\_{t,x}F|+|\theta\_{t,x}|(e^{x}S\_{T}-K)^{+}\right\}\leq Z\_{T}|e^{x}-1|\left(S\_{T}+\frac{|\mu^{S}\_{t}|}{\Sigma\_{t}}e^{x}S\_{T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ZT​ST​|ex−1|​(1+ex)≤ZT​ST​{(1+e)|ex−1|𝟏{x≤1}+e2​x​𝟏{x>1}}\displaystyle\leq Z\_{T}S\_{T}|e^{x}-1|(1+e^{x})\leq Z\_{T}S\_{T}\left\{(1+e)|e^{x}-1|{\bf 1}\_{\{x\leq 1\}}+e^{2x}{\bf 1}\_{\{x>1\}}\right\} |  |

by ([4.2](https://arxiv.org/html/2602.17090v1#S4.Ex44 "Proof. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")). Consequently, (A3) and (A6) imply the third condition of (B2).
□\Box

### 4.3 Numerically tractable expression

The goal of this subsection is to convert ([4.2](https://arxiv.org/html/2602.17090v1#S4.E2 "In Proposition 4.1. ‣ 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) into a numerically tractable form.
Throughout this subsection, we fix t∈[0,T]t\in[0,T] and K>0K>0. By ([4.3](https://arxiv.org/html/2602.17090v1#S4.E3 "In Proof. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")), ([4.2](https://arxiv.org/html/2602.17090v1#S4.E2 "In Proposition 4.1. ‣ 4.1 On the result of Handa et al. [11] ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) is rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt1,F=1St−​Σt​∫ℝ0𝔼ℙ∗​[(ex​ST−K)+−(ST−K)+|ℱt−]​(ex−1)​π​(t,x)​𝑑x.\xi^{1,F}\_{t}=\frac{1}{S\_{t-}\Sigma\_{t}}\int\_{{\mathbb{R}}\_{0}}{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[(e^{x}S\_{T}-K)^{+}-(S\_{T}-K)^{+}|{\mathcal{F}}\_{t-}](e^{x}-1)\pi(t,x)dx. |  | (4.5) |

Denote the characteristic function of LT−Lt=log⁡(ST/St)L\_{T}-L\_{t}=\log(S\_{T}/S\_{t}) under the MMM ℙ∗{\mathbb{P}}^{\*} as

|  |  |  |
| --- | --- | --- |
|  | ϕt,T∗​(z):=𝔼ℙ∗​[ei​z​(LT−Lt)],z∈ℂ.\phi^{\*}\_{t,T}(z):={\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[e^{iz(L\_{T}-L\_{t})}\right],\ \ \ z\in{\mathbb{C}}. |  |

For later use, we calculate ϕt,T∗\phi^{\*}\_{t,T}. To this end, we rewrite ([3.2](https://arxiv.org/html/2602.17090v1#S3.E2 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=St−​∫ℝ0(ex−1)​N~∗​(d​t,d​x),S0>0,dS\_{t}=S\_{t-}\int\_{{\mathbb{R}}\_{0}}\left(e^{x}-1\right)\widetilde{N}^{\*}(dt,dx),\ \ \ S\_{0}>0, |  | (4.6) |

where π∗​(t,x):=(1−θt,x)​π​(t,x)\pi^{\*}(t,x):=\left(1-\theta\_{t,x}\right)\pi(t,x) and N~∗​(d​t,d​x):=N​(d​t,d​x)−π∗​(t,x)​d​t​d​x\widetilde{N}^{\*}(dt,dx):=N(dt,dx)-\pi^{\*}(t,x)dtdx.
Solving the SDE ([4.6](https://arxiv.org/html/2602.17090v1#S4.E6 "In 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) by the same way as ([3.4](https://arxiv.org/html/2602.17090v1#S3.E4 "In Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")), we obtain

|  |  |  |
| --- | --- | --- |
|  | Lt=∫0t∫ℝ0(1+x​𝟏{|x|≤1}−ex)​π∗​(s,x)​𝑑s​𝑑x+∫0t∫|x|>1x​N​(d​s,d​x)+∫0t∫|x|≤1x​N~∗​(d​s,d​x),L\_{t}=\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(1+x{\bf 1}\_{\{|x|\leq 1\}}-e^{x}\right)\pi^{\*}(s,x)dsdx+\int\_{0}^{t}\int\_{|x|>1}xN(ds,dx)+\int\_{0}^{t}\int\_{|x|\leq 1}x\widetilde{N}^{\*}(ds,dx), |  |

which implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt,T∗​(z)=exp⁡{∫tT∫ℝ0(ei​z​x−i​z​ex+i​z−1)​π∗​(s,x)​𝑑x​𝑑s}.\phi^{\*}\_{t,T}(z)=\exp\left\{\int\_{t}^{T}\int\_{{\mathbb{R}}\_{0}}\left(e^{izx}-ize^{x}+iz-1\right)\pi^{\*}(s,x)dxds\right\}. |  | (4.7) |

We can see the following proposition:

###### Proposition 4.3 (Carr-Madan method).

Under Assumption [A](https://arxiv.org/html/2602.17090v1#ThmassA1 "Assumption A. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ∗​[(ST−K)+|ℱt−]=1π​∫0∞K−i​u−R+1​ϕt,T∗​(u−i​R)​St−i​u+R(i​u+R−1)​(i​u+R)​𝑑u{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[(S\_{T}-K)^{+}|{\mathcal{F}}\_{t-}]=\frac{1}{\pi}\int\_{0}^{\infty}K^{-iu-R+1}\frac{\phi^{\*}\_{t,T}(u-iR)S\_{t-}^{iu+R}}{(iu+R-1)(iu+R)}du |  | (4.8) |

for any R∈(1,2]R\in(1,2]. Note that the right-hand side is independent of the choice of R∈(1,2]R\in(1,2].

###### Proof.

Since Δ​Lt=0\Delta L\_{t}=0, ℙ{\mathbb{P}}-a.s., LT−LtL\_{T}-L\_{t} has the same law under ℙ∗{\mathbb{P}}^{\*} as LT−Lt−L\_{T}-L\_{t-}. Thus, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[(ST−K)+|ℱt−]=𝔼ℙ∗​[(S0​eLT−Lt+Lt−−K)+|ℱt−]=𝔼ℙ∗​[f​(Xt,T−log⁡(K/St−))|ℱt−],{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[(S\_{T}-K)^{+}|{\mathcal{F}}\_{t-}]={\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[\left(S\_{0}e^{L\_{T}-L\_{t}+L\_{t-}}-K\right)^{+}\Big|{\mathcal{F}}\_{t-}\right]={\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[f(X\_{t,T}-\log(K/S\_{t-}))|{\mathcal{F}}\_{t-}\right], |  |

where Xt,T:=LT−LtX\_{t,T}:=L\_{T}-L\_{t} and f​(x):=K​(ex−1)+f(x):=K(e^{x}-1)^{+}. Fix R∈(1,2]R\in(1,2] arbitrarily, and denote g​(x):=e−R​x​f​(x)g(x):=e^{-Rx}f(x) and g^​(u):=∫ℝei​u​x​g​(x)​𝑑x\widehat{g}(u):=\displaystyle{\int\_{{\mathbb{R}}}e^{iux}g(x)dx}.
Then, we can see that the following three conditions hold:

(a)
:   gg is a bounded continuous function in L1​(ℝ)L^{1}({\mathbb{R}}).

(b)
:   𝔼ℙ∗​[eR​Xt,T]<∞{\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[e^{RX\_{t,T}}\right]<\infty.

(c)
:   g^∈L1​(ℝ)\widehat{g}\in L^{1}({\mathbb{R}}).

In fact, Condition (a) holds clearly, Lemma [4.4](https://arxiv.org/html/2602.17090v1#S4.Thmthm4 "Lemma 4.4. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes") below ensures Condition (b), and Condition (c) is satisfied, since we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | g^​(u)\displaystyle\widehat{g}(u) | =K​∫ℝei​u​x​e−R​x​(ex−1)+​𝑑x=K​∫0∞(e(i​u−R+1)​x−e(i​u−R)​x)​𝑑x\displaystyle=K\int\_{{\mathbb{R}}}e^{iux}e^{-Rx}(e^{x}-1)^{+}dx=K\int\_{0}^{\infty}\left(e^{(iu-R+1)x}-e^{(iu-R)x}\right)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K​(−1i​u−R+1+1i​u−R)=K(i​u−R+1)​(i​u−R),\displaystyle=K\left(-\frac{1}{iu-R+1}+\frac{1}{iu-R}\right)=\frac{K}{(iu-R+1)(iu-R)}, |  |

and there is no real root for (i​u−R+1)​(i​u−R)=0(iu-R+1)(iu-R)=0. Denote

|  |  |  |
| --- | --- | --- |
|  | f^​(−u+i​R):=∫ℝe(−i​u−R)​x​f​(x)​𝑑x=g^​(−u).\widehat{f}(-u+iR):=\int\_{{\mathbb{R}}}e^{(-iu-R)x}f(x)dx=\widehat{g}(-u). |  |

Then, Theorem 2.2 of Eberlein et al. [[7](https://arxiv.org/html/2602.17090v1#bib.bib7)] implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ∗​[(ST−K)+|ℱt−]\displaystyle{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[(S\_{T}-K)^{+}|{\mathcal{F}}\_{t-}] | =12​π​∫ℝe(−R−i​u)​log⁡(K/St−)​ϕt,T∗​(u−i​R)​f^​(−u+i​R)​𝑑u\displaystyle=\frac{1}{2\pi}\int\_{{\mathbb{R}}}e^{(-R-iu)\log(K/S\_{t-})}\phi^{\*}\_{t,T}(u-iR)\widehat{f}(-u+iR)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​π​∫ℝe(−R−i​u)​log⁡(K/St−)​ϕt,T∗​(u−i​R)​K(−i​u−R+1)​(−i​u−R)​𝑑u\displaystyle=\frac{1}{2\pi}\int\_{{\mathbb{R}}}e^{(-R-iu)\log(K/S\_{t-})}\frac{\phi^{\*}\_{t,T}(u-iR)K}{(-iu-R+1)(-iu-R)}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​π​∫ℝK−i​u−R+1​ϕt,T∗​(u−i​R)​St−i​u+R(i​u+R−1)​(i​u+R)​𝑑u\displaystyle=\frac{1}{2\pi}\int\_{{\mathbb{R}}}K^{-iu-R+1}\frac{\phi^{\*}\_{t,T}(u-iR)S\_{t-}^{iu+R}}{(iu+R-1)(iu+R)}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1π​∫0∞K−i​u−R+1​ϕt,T∗​(u−i​R)​St−i​u+R(i​u+R−1)​(i​u+R)​𝑑u.\displaystyle=\frac{1}{\pi}\int\_{0}^{\infty}K^{-iu-R+1}\frac{\phi^{\*}\_{t,T}(u-iR)S\_{t-}^{iu+R}}{(iu+R-1)(iu+R)}du. |  |

Note that the last equality holds because the integral is real-valued and the real part of the integrand is even.
Moreover, its value is independent of the choice of R∈(1,2]R\in(1,2]. Consequently, Proposition [4.3](https://arxiv.org/html/2602.17090v1#S4.Thmthm3 "Proposition 4.3 (Carr-Madan method). ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes") follows.
□\Box

###### Lemma 4.4.

𝔼ℙ∗​[e2​Xt,T]<∞{\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[e^{2X\_{t,T}}\right]<\infty, where Xt,T=LT−LtX\_{t,T}=L\_{T}-L\_{t}.

###### Proof.

We define the process M∗={Mt∗}t∈[0,T]M^{\*}=\{M^{\*}\_{t}\}\_{t\in[0,T]} as

|  |  |  |
| --- | --- | --- |
|  | Mt∗=∫0t∫ℝ0(ex−1)​N~∗​(d​s,d​x).M^{\*}\_{t}=\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(e^{x}-1\right)\widetilde{N}^{\*}(ds,dx). |  |

We have then S=ℰ​(M∗)S={\mathcal{E}}(M^{\*}). Here, we show that M∗M^{\*} is a square integrable ℙ∗{\mathbb{P}}^{\*}-martingale such that ⟨M∗⟩\langle M^{\*}\rangle is bounded.
To this end, it suffices to make sure that ∫0T∫ℝ0(ex−1)2​π∗​(t,x)​𝑑x​𝑑t<∞\displaystyle{\int\_{0}^{T}\int\_{{\mathbb{R}}\_{0}}\left(e^{x}-1\right)^{2}\pi^{\*}(t,x)dxdt<\infty};
however, we can derive this from Lemmas [3.1](https://arxiv.org/html/2602.17090v1#S3.Thmthm1 "Lemma 3.1. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") and [3.4](https://arxiv.org/html/2602.17090v1#S3.Thmthm4 "Lemma 3.4. ‣ Proof. ‣ Proof. ‣ 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes") together with (A4).
By Proposition 3.7 of [[5](https://arxiv.org/html/2602.17090v1#bib.bib5)], SS satisfies the reverse Hölder inequality under ℙ∗{\mathbb{P}}^{\*}, that is,
there is a constant C>0C>0 such that 𝔼ℙ∗​[ST2|ℱt]≤C​St2\displaystyle{{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[S\_{T}^{2}|{\mathcal{F}}\_{t}]\leq CS\_{t}^{2}}.
As a result, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[e2​Xt,T]=𝔼ℙ∗​[e2​(LT−Lt)]=𝔼ℙ∗​[(STSt)2]=𝔼ℙ∗​[1St2​𝔼ℙ∗​[ST2|ℱt]]≤C.{\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[e^{2X\_{t,T}}\right]={\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[e^{2(L\_{T}-L\_{t})}\right]={\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[\left(\frac{S\_{T}}{S\_{t}}\right)^{2}\right]={\mathbb{E}}\_{{\mathbb{P}}^{\*}}\left[\frac{1}{S\_{t}^{2}}{\mathbb{E}}\_{{\mathbb{P}}^{\*}}[S\_{T}^{2}|{\mathcal{F}}\_{t}]\right]\leq C. |  |

□\Box

Let us further modify ([4.5](https://arxiv.org/html/2602.17090v1#S4.E5 "In 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")). First, we regard the call option price as a function of KK, and denote it by

|  |  |  |
| --- | --- | --- |
|  | f​(K):=𝔼ℙ∗​[(ST−K)+|ℱt−],K>0.f(K):={\mathbb{E}}\_{{\mathbb{P}}^{\*}}[(S\_{T}-K)^{+}|{\mathcal{F}}\_{t-}],\ \ \ K>0. |  |

Proposition [4.3](https://arxiv.org/html/2602.17090v1#S4.Thmthm3 "Proposition 4.3 (Carr-Madan method). ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes") provides that

|  |  |  |
| --- | --- | --- |
|  | f​(K)=1π​∫0∞K−i​u−R+1​ϕt,T∗​(u−i​R)​St−i​u+R(i​u+R−1)​(i​u+R)​𝑑u.f(K)=\frac{1}{\pi}\int\_{0}^{\infty}K^{-iu-R+1}\frac{\phi^{\*}\_{t,T}(u-iR)S\_{t-}^{iu+R}}{(iu+R-1)(iu+R)}du. |  |

Then, since 𝔼ℙ∗​[(ex​ST−K)+|ℱt−]=ex​f​(e−x​K){\mathbb{E}}\_{{\mathbb{P}}^{\*}}[(e^{x}S\_{T}-K)^{+}|{\mathcal{F}}\_{t-}]=e^{x}f(e^{-x}K), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt1,F\displaystyle\xi^{1,F}\_{t} | =1St−​Σt​∫ℝ0{ex​f​(e−x​K)−f​(K)}​(ex−1)​π​(t,x)​𝑑x\displaystyle=\frac{1}{S\_{t-}\Sigma\_{t}}\int\_{{\mathbb{R}}\_{0}}\{e^{x}f(e^{-x}K)-f(K)\}(e^{x}-1)\pi(t,x)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1St−​Σt​∫ℝ01π​∫0∞{e(i​u+R)​x−1}​K−i​u−R+1​ϕt,T∗​(u−i​R)​St−i​u+R(i​u+R−1)​(i​u+R)​𝑑u​(ex−1)​π​(t,x)​𝑑x\displaystyle=\frac{1}{S\_{t-}\Sigma\_{t}}\int\_{{\mathbb{R}}\_{0}}\frac{1}{\pi}\int\_{0}^{\infty}\left\{e^{(iu+R)x}-1\right\}K^{-iu-R+1}\frac{\phi^{\*}\_{t,T}(u-iR)S\_{t-}^{iu+R}}{(iu+R-1)(iu+R)}du(e^{x}-1)\pi(t,x)dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1π​St−​Σt​∫0∞K−i​u−R+1​∫ℝ0(e(i​u+R)​x−1)​(ex−1)​π​(t,x)​𝑑x​ϕt,T∗​(u−i​R)​St−i​u+R(i​u+R−1)​(i​u+R)​𝑑u.\displaystyle=\frac{1}{\pi S\_{t-}\Sigma\_{t}}\int\_{0}^{\infty}K^{-iu-R+1}\int\_{{\mathbb{R}}\_{0}}(e^{(iu+R)x}-1)(e^{x}-1)\pi(t,x)dx\frac{\phi^{\*}\_{t,T}(u-iR)S\_{t-}^{iu+R}}{(iu+R-1)(iu+R)}du. |  | (4.9) |

If we can obtain an explicit expression for the inner integral ∫ℝ0(e(i​u+R)​x−1)​(ex−1)​π​(t,x)​𝑑x\displaystyle{\int\_{{\mathbb{R}}\_{0}}(e^{(iu+R)x}-1)(e^{x}-1)\pi(t,x)dx},
then ([4.3](https://arxiv.org/html/2602.17090v1#S4.Ex67 "Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) could be computed numerically using the fast Fourier transform (FFT).

Now, we focus on the inner integral. To this end, we extend the domain of κt\kappa\_{t} defined in ([3.1](https://arxiv.org/html/2602.17090v1#S3.E1 "In 3 Exponential additive processes ‣ Local risk-minimization for exponential additive processes")) to

|  |  |  |
| --- | --- | --- |
|  | 𝒟:={z∈ℂ|∫0T∫|x|>1eℜ⁡(z)​x​π​(t,x)​𝑑x​𝑑t<∞},{\mathcal{D}}:=\left\{z\in{\mathbb{C}}\ \Big|\ \int\_{0}^{T}\int\_{|x|>1}e^{\Re(z)x}\pi(t,x)dxdt<\infty\right\}, |  |

where ℜ⁡(z)\Re(z) denotes the real part of zz. Here, recall that

|  |  |  |
| --- | --- | --- |
|  | κt​(z):=z​γt+∫0t∫ℝ0(ez​x−1−z​x​𝟏{|x|≤1})​π​(s,x)​𝑑x​𝑑s.\kappa\_{t}(z):=z\gamma\_{t}+\int\_{0}^{t}\int\_{{\mathbb{R}}\_{0}}\left(e^{zx}-1-zx{\bf 1}\_{\{|x|\leq 1\}}\right)\pi(s,x)dxds. |  |

Furthermore, we denote lt​(z):=∂κt​(z)∂t\displaystyle{l\_{t}(z):=\frac{\partial\kappa\_{t}(z)}{\partial t}} for z∈𝒟z\in{\mathcal{D}}.
Then, we can see the following:

###### Lemma 4.5.

For any z∈ℂz\in{\mathbb{C}} with z+1∈𝒟z+1\in{\mathcal{D}}, we have

|  |  |  |
| --- | --- | --- |
|  | ∫−∞∞(ez​x−1)​(ex−1)​π​(t,x)​𝑑x=lt​(z+1)−lt​(z)−lt​(1).\int\_{-\infty}^{\infty}\left(e^{zx}-1\right)\left(e^{x}-1\right)\pi(t,x)dx=l\_{t}(z+1)-l\_{t}(z)-l\_{t}(1). |  |

###### Proof.

Since lt​(z)=z​γt′+∫ℝ0(ez​x−1−z​x​𝟏{|x|≤1})​π​(t,x)​𝑑xl\_{t}(z)=z\gamma^{\prime}\_{t}+\displaystyle{\int\_{{\mathbb{R}}\_{0}}\left(e^{zx}-1-zx{\bf 1}\_{\{|x|\leq 1\}}\right)\pi(t,x)dx} for z∈𝒟z\in{\mathcal{D}}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | lt​(z+1)−lt​(z)−lt​(1)\displaystyle l\_{t}(z+1)-l\_{t}(z)-l\_{t}(1) | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(z+1)​γt′−z​γt′−γt′\displaystyle=(z+1)\gamma^{\prime}\_{t}-z\gamma^{\prime}\_{t}-\gamma^{\prime}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫ℝ0(e(z+1)​x−1−(z+1)​x​𝟏{|x|≤1}−ez​x+1+z​x​𝟏{|x|≤1}−ex+1+x​𝟏{|x|≤1})​π​(t,x)​𝑑x\displaystyle\hskip 14.22636pt+\int\_{{\mathbb{R}}\_{0}}\left(e^{(z+1)x}-1-(z+1)x{\bf 1}\_{\{|x|\leq 1\}}-e^{zx}+1+zx{\bf 1}\_{\{|x|\leq 1\}}-e^{x}+1+x{\bf 1}\_{\{|x|\leq 1\}}\right)\pi(t,x)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝ0(e(z+1)​x−ez​x−ex+1)​π​(t,x)​𝑑x.\displaystyle=\int\_{{\mathbb{R}}\_{0}}\left(e^{(z+1)x}-e^{zx}-e^{x}+1\right)\pi(t,x)dx. |  |

□\Box

Since i​u+R+1∈𝒟iu+R+1\in{\mathcal{D}} for any R∈(1,2]R\in(1,2] and u∈ℝu\in{\mathbb{R}} by (A3), Lemma [4.5](https://arxiv.org/html/2602.17090v1#S4.Thmthm5 "Lemma 4.5. ‣ Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes") implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝ0(e(i​u+R)​x−1)​(ex−1)​π​(t,x)​𝑑x=lt​(i​u+R+1)−lt​(i​u+R)−lt​(1).\int\_{{\mathbb{R}}\_{0}}(e^{(iu+R)x}-1)(e^{x}-1)\pi(t,x)dx=l\_{t}(iu+R+1)-l\_{t}(iu+R)-l\_{t}(1). |  | (4.10) |

In addition, we calculate the characteristic function ϕt,T∗\phi^{\*}\_{t,T} using Lemma [4.5](https://arxiv.org/html/2602.17090v1#S4.Thmthm5 "Lemma 4.5. ‣ Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes"). ([4.7](https://arxiv.org/html/2602.17090v1#S4.E7 "In 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(ϕt,T∗​(z))\displaystyle\log(\phi^{\*}\_{t,T}(z)) | =∫tT∫ℝ0(ei​z​x−i​z​ex+i​z−1)​π∗​(s,x)​𝑑x​𝑑s\displaystyle=\int\_{t}^{T}\int\_{{\mathbb{R}}\_{0}}\left(e^{izx}-ize^{x}+iz-1\right)\pi^{\*}(s,x)dxds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tT∫ℝ0(ei​z​x−1−i​z​(ex−1))​(1−μtSΣt​(ex−1))​π​(s,x)​𝑑x​𝑑s\displaystyle=\int\_{t}^{T}\int\_{{\mathbb{R}}\_{0}}\left(e^{izx}-1-iz(e^{x}-1)\right)\left(1-\frac{\mu^{S}\_{t}}{\Sigma\_{t}}(e^{x}-1)\right)\pi(s,x)dxds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tT(ls​(i​z)−i​z​ls​(1))​𝑑s−∫tTμtSΣt​∫ℝ0(ei​z​x−1−i​z​(ex−1))​(ex−1)​π​(s,x)​𝑑x​𝑑s\displaystyle=\int\_{t}^{T}\left(l\_{s}(iz)-izl\_{s}(1)\right)ds-\int\_{t}^{T}\frac{\mu^{S}\_{t}}{\Sigma\_{t}}\int\_{{\mathbb{R}}\_{0}}\left(e^{izx}-1-iz(e^{x}-1)\right)(e^{x}-1)\pi(s,x)dxds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫tT(ls​(i​z)−i​z​ls​(1))​𝑑s−∫tTμtSΣt​{ls​(i​z+1)−ls​(i​z)−ls​(1)−i​z​(ls​(2)−2​ls​(1))}​𝑑s.\displaystyle=\int\_{t}^{T}\left(l\_{s}(iz)-izl\_{s}(1)\right)ds-\int\_{t}^{T}\frac{\mu^{S}\_{t}}{\Sigma\_{t}}\left\{l\_{s}(iz+1)-l\_{s}(iz)-l\_{s}(1)-iz\left(l\_{s}(2)-2l\_{s}(1)\right)\right\}ds. |  | (4.11) |

## 5 Numerical experiments for VGSSD

In this section, we introduce the variance-gamma scaled self-decomposable (VGSSD) process, undertaken by Carr et al. [[3](https://arxiv.org/html/2602.17090v1#bib.bib3)], as an example of additive processes
and, using ([4.8](https://arxiv.org/html/2602.17090v1#S4.E8 "In Proposition 4.3 (Carr-Madan method). ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")), ([4.10](https://arxiv.org/html/2602.17090v1#S4.E10 "In Proof. ‣ Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")), and ([4.3](https://arxiv.org/html/2602.17090v1#S4.Ex76 "Proof. ‣ Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")), conduct numerical experiments computing the values of LRM strategies for exponential VGSSD models.

To introduce the VGSSD process, we prepare some terminologies.

###### Definition 5.1.

1. 1.

   A random variable XX is said to be self-decomposable if, for any c∈(0,1)c\in(0,1), there exists an independent random variable X(c)X^{(c)} such that X​=d​c​X+X(c)X\overset{\mathrm{d}}{=}cX+X^{(c)},
   where X1​=d​X2X\_{1}\overset{\mathrm{d}}{=}X\_{2} means that X1X\_{1} and X2X\_{2} are identically distributed.
2. 2.

   A stochastic process Y={Yt}t≥0Y=\{Y\_{t}\}\_{t\geq 0} is self-similar if there is an H>0H>0 such that Ya​t​=d​aH​YtY\_{at}\overset{\mathrm{d}}{=}a^{H}Y\_{t} for any a>0a>0 and t≥0t\geq 0.
   To emphasize the exponent HH, we say that YY is HH-self-similar.
   Furthermore, YY is called broad-sense HH-self-similar if, for any a>0a>0, there is a function ctc\_{t} from [0,∞)[0,\infty) to ℝ{\mathbb{R}} such that
   Ya​t​=d​aH​Yt+ctY\_{at}\overset{\mathrm{d}}{=}a^{H}Y\_{t}+c\_{t} holds for any t≥0t\geq 0.
3. 3.

   A stochastic process is called a Sato process if it is a self-similar additive process, and the distribution at unit time is self-decomposable.

The VGSSD process is a generalization of the variance-gamma (VG) process.
Here, a Lévy process defined as a Brownian motion subordinated to a gamma process is called a VG process.
In other words, VG processes can be described as σ​BGt+μ​Gt\sigma B\_{G\_{t}}+\mu G\_{t}, where σ>0\sigma>0, μ∈ℝ\mu\in{\mathbb{R}}, {Bt}t≥0\{B\_{t}\}\_{t\geq 0} is a one-dimensional standard Brownin motion,
and {Gt}t≥0\{G\_{t}\}\_{t\geq 0} is a Gamma process.
Besides, any VG process does not possess a Brownian component, and its Lévy density νV​G\nu^{VG} is given by νV​G​(x)=hV​G​(x)|x|\displaystyle{\nu^{VG}(x)=\frac{h^{VG}(x)}{|x|}} for x∈ℝ0x\in{\mathbb{R}}\_{0}, where

|  |  |  |
| --- | --- | --- |
|  | hV​G​(x)=C​(e−M​x​𝟏{x>0}+eG​x​𝟏{x<0}),C,G,M>0.h^{VG}(x)=C\left(e^{-Mx}{\bf 1}\_{\{x>0\}}+e^{Gx}{\bf 1}\_{\{x<0\}}\right),\ \ \ C,G,M>0. |  |

Note that the distribution of a VG process at unit time is called a VG distribution, which is self-decomposable; and
a VGSSD process is defined as a Sato process whose distribution at unit time follows a VG distribution.
Here, let XV​G={XtV​G}t≥0X^{VG}=\{X^{VG}\_{t}\}\_{t\geq 0} denote a VG process with parameters CC, GG, and MM.
We consider a market model in which the log-price process LL is given by a VGSSD process associated with XV​GX^{VG}, with self-similarity exponent HH.
Note that LL is HH-self-similar, and L1​=d​X1V​GL\_{1}\overset{\mathrm{d}}{=}X^{VG}\_{1} holds.
Then, Theorem 1 of [[3](https://arxiv.org/html/2602.17090v1#bib.bib3)] implies that the Lévy density π\pi and the drift function γt\gamma\_{t} for LL are, respectively, given by

|  |  |  |
| --- | --- | --- |
|  | π​(t,x)=C​H​t−1−H​(M​e−M​t−H​x​𝟏{x>0}+G​eG​t−H​x​𝟏{x<0}),\pi(t,x)=CHt^{-1-H}\left(Me^{-Mt^{-H}x}{\bf 1}\_{\{x>0\}}+Ge^{Gt^{-H}x}{\bf 1}\_{\{x<0\}}\right), |  |

and

|  |  |  |
| --- | --- | --- |
|  | γt=∫0t∫|x|≤1x​ν¯​(d​s,d​x).\gamma\_{t}=\int\_{0}^{t}\int\_{|x|\leq 1}x\overline{\nu}(ds,dx). |  |

Next, we add a differentiable function ρt\rho\_{t} to γt\gamma\_{t} as follows:

|  |  |  |
| --- | --- | --- |
|  | γt=ρt+∫0t∫|x|≤1x​ν¯​(d​s,d​x),t∈(0,T].\gamma\_{t}=\rho\_{t}+\int\_{0}^{t}\int\_{|x|\leq 1}x\overline{\nu}(ds,dx),\ \ \ t\in(0,T]. |  |

Under this setting, LL is no longer self-similar, but it still retains the broad-sense self-similarity.
Now, we examine Assumption [A](https://arxiv.org/html/2602.17090v1#ThmassA1 "Assumption A. ‣ 4.2 Main theorem ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes"). First, (A1) and (A2) are satisfied. Additionally, suppose

|  |  |  |  |
| --- | --- | --- | --- |
|  | 4<M​T−H.4<MT^{-H}. |  | (5.1) |

Then, (A3) is also satisfied. Besides, we can confirm (A6) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T∫|x|≤1|x|​π​(t,x)​𝑑x​𝑑t\displaystyle\int\_{0}^{T}\int\_{|x|\leq 1}|x|\pi(t,x)dxdt | =C​H​∫0Tt−1−H​{∫01M​x​e−M​t−H​x​𝑑x+∫−10G​(−x)​eG​t−H​x​𝑑x}​𝑑t\displaystyle=CH\int\_{0}^{T}t^{-1-H}\left\{\int\_{0}^{1}Mxe^{-Mt^{-H}x}dx+\int\_{-1}^{0}G(-x)e^{Gt^{-H}x}dx\right\}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​H​∫0Tt−1−H​{t2​HM+t2​HG}​𝑑t<∞.\displaystyle\leq CH\int\_{0}^{T}t^{-1-H}\left\{\frac{t^{2H}}{M}+\frac{t^{2H}}{G}\right\}dt<\infty. |  |

To discuss (A4), we denote

|  |  |  |
| --- | --- | --- |
|  | qt​(z):=∫ℝ0(ez​x−1)​π​(t,x)​𝑑xq\_{t}(z):=\int\_{{\mathbb{R}}\_{0}}\left(e^{zx}-1\right)\pi(t,x)dx |  |

for z∈𝒟z\in{\mathcal{D}}. We have then

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt​(z)\displaystyle q\_{t}(z) | =C​H​t−1−H​{∫0∞(ez​x−1)​M​e−M​t−H​x​𝑑x+∫−∞0(ez​x−1)​G​eG​t−H​x​𝑑x}\displaystyle=CHt^{-1-H}\left\{\int\_{0}^{\infty}\left(e^{zx}-1\right)Me^{-Mt^{-H}x}dx+\int\_{-\infty}^{0}\left(e^{zx}-1\right)Ge^{Gt^{-H}x}dx\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C​H​t−1−H​{M​∫0∞(e−(M​t−H−z)​x−e−M​t−H​x)​𝑑x+G​∫−∞0(e(G​t−H+z)​x−eG​t−H​x)​𝑑x}\displaystyle=CHt^{-1-H}\left\{M\int\_{0}^{\infty}\left(e^{-(Mt^{-H}-z)x}-e^{-Mt^{-H}x}\right)dx+G\int\_{-\infty}^{0}\left(e^{(Gt^{-H}+z)x}-e^{Gt^{-H}x}\right)dx\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C​H​t−1−H​{M​(1M​t−H−z−1M​t−H)+G​(1G​t−H+z−1G​t−H)}\displaystyle=CHt^{-1-H}\left\{M\left(\frac{1}{Mt^{-H}-z}-\frac{1}{Mt^{-H}}\right)+G\left(\frac{1}{Gt^{-H}+z}-\frac{1}{Gt^{-H}}\right)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C​H​t−1​z​{1M​t−H−z−1G​t−H+z}=C​H​t−1+H​z​G−M+2​z​tH(M−z​tH)​(G+z​tH).\displaystyle=CHt^{-1}z\left\{\frac{1}{Mt^{-H}-z}-\frac{1}{Gt^{-H}+z}\right\}=CHt^{-1+H}z\frac{G-M+2zt^{H}}{(M-zt^{H})(G+zt^{H})}. |  |

Thus, lt​(z)l\_{t}(z) is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | lt​(z)=z​γt′+∫ℝ0(ez​x−1−z​x​𝟏{|x|≤1})​π​(t,x)​𝑑x=z​ρt′+qt​(z),l\_{t}(z)=z\gamma^{\prime}\_{t}+\int\_{{\mathbb{R}}\_{0}}\left(e^{zx}-1-zx{\bf 1}\_{\{|x|\leq 1\}}\right)\pi(t,x)dx=z\rho^{\prime}\_{t}+q\_{t}(z), |  | (5.2) |

from which we obtain μtS=lt​(1)=ρt′+qt​(1)\mu^{S}\_{t}=l\_{t}(1)=\rho^{\prime}\_{t}+q\_{t}(1) and Σt=lt​(2)−2​lt​(1)=qt​(2)−2​qt​(1)\Sigma\_{t}=l\_{t}(2)-2l\_{t}(1)=q\_{t}(2)-2q\_{t}(1).
As a result, (A4), i.e., 0≥μtS>−Σt0\geq\mu^{S}\_{t}>-\Sigma\_{t} holds for any t∈(0,T]t\in(0,T], is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | −qt​(1)≥ρt′>qt​(1)−qt​(2)-q\_{t}(1)\geq\rho^{\prime}\_{t}>q\_{t}(1)-q\_{t}(2) |  | (5.3) |

for any t∈(0,T]t\in(0,T].
As for (A5), as the derivation of sufficient conditions is complicated, it shall be examined individually for given concrete examples.

We introduce two examples that satisfy ([5.3](https://arxiv.org/html/2602.17090v1#S5.E3 "In 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")) and (A5) as long as MM and TT are set to meet ([5.1](https://arxiv.org/html/2602.17090v1#S5.E1 "In 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")).

###### Example 5.2.

1. (1)

   The first example is when ρt′=−qt​(1)\rho^{\prime}\_{t}=-q\_{t}(1), corresponding to the case where μtS=θt,x=0\mu^{S}\_{t}=\theta\_{t,x}=0 for any t∈(0,T]t\in(0,T] and any x∈ℝ0x\in{\mathbb{R}}\_{0},
   that is, the asset price process SS becomes a ℙ{\mathbb{P}}-martingale. Thus, ℙ∗=ℙ{\mathbb{P}}^{\*}={\mathbb{P}} holds. In this case, (A5) is automatically satisfied.
   Besides, ([5.3](https://arxiv.org/html/2602.17090v1#S5.E3 "In 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")) is also satisfied, since qt​(2)>2​qt​(1)q\_{t}(2)>2q\_{t}(1) holds.
2. (2)

   Next is the case where μtSΣt=−12\displaystyle{\frac{\mu^{S}\_{t}}{\Sigma\_{t}}=-\frac{1}{2}}, in other words, ρt′=−12​qt​(2)\displaystyle{\rho^{\prime}\_{t}=-\frac{1}{2}q\_{t}(2)}.
   We can see immediately that ([5.3](https://arxiv.org/html/2602.17090v1#S5.E3 "In 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")) and (A5) are satisfied.

Here, we conduct numerical experiments for the two models introduced in Example [5.2](https://arxiv.org/html/2602.17090v1#S5.Thmthm2 "Example 5.2. ‣ 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes").
To this end, taking into account ([4.10](https://arxiv.org/html/2602.17090v1#S4.E10 "In Proof. ‣ Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")), we discretize the right-hand side of ([4.3](https://arxiv.org/html/2602.17090v1#S4.Ex67 "Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1π​St−​Σt​∑j=0N−1e(−i​zj+1)​k​{lt​(i​zj+1)−lt​(i​zj)−lt​(1)}​ϕt,T∗​(zj)​St−i​zj(i​zj−1)​i​zj​η\displaystyle\frac{1}{\pi S\_{t-}\Sigma\_{t}}\sum\_{j=0}^{N-1}e^{(-iz\_{j}+1)k}\left\{l\_{t}(iz\_{j}+1)-l\_{t}(iz\_{j})-l\_{t}(1)\right\}\frac{\phi^{\*}\_{t,T}(z\_{j})S\_{t-}^{iz\_{j}}}{(iz\_{j}-1)iz\_{j}}\eta |  | |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1π​(qt​(2)−2​qt​(1))​∑j=0N−1e(−i​zj+1)​k​{qt​(i​zj+1)−qt​(i​zj)−qt​(1)}​ϕt,T∗​(zj)​St−i​zj−1(i​zj−1)​i​zj​η,\displaystyle\hskip 22.76219pt=\frac{1}{\pi(q\_{t}(2)-2q\_{t}(1))}\sum\_{j=0}^{N-1}e^{(-iz\_{j}+1)k}\left\{q\_{t}(iz\_{j}+1)-q\_{t}(iz\_{j})-q\_{t}(1)\right\}\frac{\phi^{\*}\_{t,T}(z\_{j})S\_{t-}^{iz\_{j}-1}}{(iz\_{j}-1)iz\_{j}}\eta, |  | (5.4) |

where N∈ℕN\in{\mathbb{N}} is the number of grid points, η>0\eta>0 is the distance between adjacent grid points, k=log⁡Kk=\log K and zj:=η​j−i​Rz\_{j}:=\eta j-iR for j=0,…,N−1j=0,\dots,N-1.
With appropriate settings of NN and η\eta, ([5](https://arxiv.org/html/2602.17090v1#S5.Ex90 "5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")) provides a sufficiently accurate approximation for ξt1,F\xi^{1,F}\_{t}.
To compute ([5](https://arxiv.org/html/2602.17090v1#S5.Ex90 "5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")), we employ the FFT. In our experiments, we take N=214N=2^{14}, η=0.25\eta=0.25, and R=1.75R=1.75, which are the standard settings for the FFT.
Throughout all experiments, we set C=1C=1, G=MG=M, H=12H=\displaystyle{\frac{1}{2}}, and St−=1S\_{t-}=1. Then, we obtain

|  |  |  |
| --- | --- | --- |
|  | qt​(z)=z2M2−z2​t, and ∫tTqs​(z)​𝑑s=log⁡(M2−z2​tM2−z2​T).q\_{t}(z)=\frac{z^{2}}{M^{2}-z^{2}t},\ \ \ \mbox{ and }\ \ \ \int\_{t}^{T}q\_{s}(z)ds=\log\left(\frac{M^{2}-z^{2}t}{M^{2}-z^{2}T}\right). |  |

From the view of ([4.3](https://arxiv.org/html/2602.17090v1#S4.Ex76 "Proof. ‣ Proof. ‣ Proof. ‣ 4.3 Numerically tractable expression ‣ 4 LRM strategies for exponential additive processes ‣ Local risk-minimization for exponential additive processes")) and ([5.2](https://arxiv.org/html/2602.17090v1#S5.E2 "In 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes")), ϕt,T∗\phi^{\*}\_{t,T} for Example [5.2](https://arxiv.org/html/2602.17090v1#S5.Thmthm2 "Example 5.2. ‣ 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes") (1) satisfies

|  |  |  |
| --- | --- | --- |
|  | log⁡(ϕt,T∗​(z))=∫tT(qs​(i​z)−i​z​qs​(1))​𝑑s=log⁡(M2+z2​tM2+z2​T)−i​z​log⁡(M2−tM2−T).\log(\phi^{\*}\_{t,T}(z))=\int\_{t}^{T}\left(q\_{s}(iz)-izq\_{s}(1)\right)ds=\log\left(\frac{M^{2}+z^{2}t}{M^{2}+z^{2}T}\right)-iz\log\left(\frac{M^{2}-t}{M^{2}-T}\right). |  |

As for (2), we have the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(ϕt,T∗​(z))\displaystyle\log(\phi^{\*}\_{t,T}(z)) | =∫tT(qs​(i​z)−i​z​qs​(1))​𝑑s+12​∫tT{qs​(i​z+1)−qs​(i​z)−qs​(1)−i​z​(qs​(2)−2​qs​(1))}\displaystyle=\int\_{t}^{T}\left(q\_{s}(iz)-izq\_{s}(1)\right)ds+\frac{1}{2}\int\_{t}^{T}\left\{q\_{s}(iz+1)-q\_{s}(iz)-q\_{s}(1)-iz\left(q\_{s}(2)-2q\_{s}(1)\right)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tT{12​qs​(i​z+1)+12​qs​(i​z)−12​qs​(1)−i​z​qs​(2)}​𝑑s\displaystyle=\int\_{t}^{T}\left\{\frac{1}{2}q\_{s}(iz+1)+\frac{1}{2}q\_{s}(iz)-\frac{1}{2}q\_{s}(1)-izq\_{s}(2)\right\}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​log⁡(M2−(i​z+1)2​tM2−(i​z+1)2​T)+12​log⁡(M2+z2​tM2+z2​T)−12​log⁡(M2−tM2−T)\displaystyle=\frac{1}{2}\log\left(\frac{M^{2}-(iz+1)^{2}t}{M^{2}-(iz+1)^{2}T}\right)+\frac{1}{2}\log\left(\frac{M^{2}+z^{2}t}{M^{2}+z^{2}T}\right)-\frac{1}{2}\log\left(\frac{M^{2}-t}{M^{2}-T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −i​z​log⁡(M2−4​tM2−4​T).\displaystyle\hskip 14.22636pt-iz\log\left(\frac{M^{2}-4t}{M^{2}-4T}\right). |  |

We implement two types of experiments as follows:

1. (A)

   Fix T=1T=1 and K=1K=1, i.e., we treat the at-the-money (ATM) options.
   Instead, we vary tt from 0.010.01 to 0.990.99 in steps of 0.010.01, that is, we compute LRM strategies for ATM call options for various time-to-maturities.
   Note that, although the value of tt varies, we set StS\_{t} to 11 for any tt.
2. (B)

   Fix t=0t=0 and T=0.5T=0.5, and vary KK from 0.510.51 to 1.501.50 in steps of 0.010.01.
   That is, we compute LRM strategies at time to maturity of 0.50.5 for various moneyness levels, from out-of-the-money (OTM) to in-the-money (ITM).

We conduct the types (A) and (B) of numerical experiments for the models (1) and (2) in Example [5.2](https://arxiv.org/html/2602.17090v1#S5.Thmthm2 "Example 5.2. ‣ 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes"), that is, a total of four experiments.
In all experiments, we perform computations in two settings: M=4M=4 and M=16M=16. All experimental results are shown in Figure [1](https://arxiv.org/html/2602.17090v1#S5.F1 "Figure 1 ‣ 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes").
Panels (A1) and (A2) in Figure [1](https://arxiv.org/html/2602.17090v1#S5.F1 "Figure 1 ‣ 5 Numerical experiments for VGSSD ‣ Local risk-minimization for exponential additive processes") draw the values of LRM strategies for the ATM call option with maturity T=1T=1 at t=0.01,0.02,…,0.99t=0.01,0.02,\dots,0.99,
where we set StS\_{t} to 11 for all t=0.01,0.02,…,0.99t=0.01,0.02,\dots,0.99.
On the other hand, Panels (B1) and (B2) represent the values of LRM strategies at time 0 for call options with maturity 0.50.5 vs. strike prices K=0.51,0.52,…,1.50K=0.51,0.52,\dots,1.50,
where the present asset price S0S\_{0} is 11. In each panel, the red and blue curves correspond to M=4M=4 and M=16M=16, respectively.
In panels (B1) and (B2), the blue curves (M=16M=16) take values near 11 when K<1K<1 (i.e., ITM options), change rapidly around the ATM, and become almost 0 for OTM options.
On the other hand, the red curves (M=4M=4) change less rapidly than the blue ones.
This result is consistent with the fact that the larger the value of MM, the less likely large jumps are to occur, i.e., the smaller the fluctuations in asset prices.

![Refer to caption](x1.png)


A1  Experiment (A) for Model (1)

![Refer to caption](x2.png)


A2  Experiment (A) for Model (2)

![Refer to caption](x3.png)


B1  Experiment (B) for Model (1)

![Refer to caption](x4.png)


B2  Experiment (B) for Model (2)

Figure 1:

## 6 Conclusion

The goal of this paper is to study LRM strategies for exponential additive models. In fact, we derived a mathematical expression and its numerically tractable form.
In particular, to derive the integrability of the asset price process and the Radon-Nikodym density of the MMM,
we employed a different approach from that used in the Lévy process case.
Furthermore, in Section 5, we introduced the VGSSD process and conducted numerical experiments.
As future work, numerical experiments concerning other exponential additive models remain.

## References

* [1]
   Arai, T., & Suzuki, R. (2015). Local risk-minimization for Lévy markets. International Journal of Financial Engineering, 2(02), 1550015.
* [2]
   Arai, T., Imai, Y., & Suzuki, R. (2016). Numerical analysis on local risk-minimization for exponential Lévy models.
  International Journal of Theoretical and Applied Finance, 19(02), 1650008.
* [3]
   Carr, P., Geman, H., Madan, D.B., & Yor, M. (2007). Self-decomposability and option pricing. Mathematical Finance, 17(1), 31-57.
* [4]
   Cont, R., & Tankov, P. (2004). Financial Modeling with Jump Process, Chapman & Hall, London.
* [5]
   Choulli, T., Krawczyk, L., & Stricker, C. (1998). ℰ{\mathcal{E}}-martingales and their applications in mathematical finance. Annals of Probability, 26(2), 853-876.
* [6]
   Di Nunno, G., & Vives, J. (2017). A Malliavin–Skorohod calculus in L0L^{0} and L1L^{1} for additive and Volterra-type processes. Stochastics, 89(1), 142-170.
* [7]
   Eberlein, E., Glau, K., & Papapantoleon, A. (2010). Analysis of Fourier transform valuation formulas and applications.
  Applied Mathematical Finance, 17(3), 211-240.
* [8]
   Föllmer, H., & Schweizer, M. (1991). Hedging of contingent claims under incomplete information, in: M.H.A. Davis and R.J. Elliott (eds.),
  Applied Stochastic Analysis, Stochastics Monographs, Vol. 5, Gordon and Breach, London, 389–414.
* [9]
   Föllmer, H. and Sondermann, D. (1986), Hedging of non-redundant contingent claims, in: W. Hildenbrand and A. Mas-Colell (eds.),
  Contributions to Mathematical Economics, North-Holland, Amsterdam, 205–223.
* [10]
   Goutte, S., Oudjane, N., & Russo, F. (2014). Variance optimal hedging for continuous time additive processes and applications. Stochastics, 86(1), 147-185.
* [11]
   Handa, M., Sakuma, N., & Suzuki, R. (2024).
  A Girsanov transformed Clark-Ocone-Haussmann type formula for L1L^{1}-pure jump additive processes and its application to portfolio optimization.
  Annals of Finance, 20(3), 329-352.
* [12]
   Protter, P. E. (2004). Stochastic Integration and Differential equations. 2nd eds. Springer.
* [13]
   Sato, H. (1990). Uniform integrability of an additive martingale and its exponential. Stochastics and Stochastic Reports, 30(3-4), 163-169.
* [14]
   Sato, K. (2013). Lévy processes and infinitely divisible distributions, revised edition. Cambridge university press.
* [15]
   Schweizer, M. (2008). Local risk-minimization for multidimensional assets and payment streams. Banach Cent. Publ, 83, 213-229.
* [16]
   Situ, R. (2005). Theory of stochastic differential equations with jumps and applications:
  mathematical and analytical techniques with applications to engineering. Boston, MA: Springer US.
* [17]
   Solé, J.L., Utzet, F., & Vives, J. (2007). Canonical Lévy process and Malliavin calculus. Stochastic processes and their Applications, 117(2), 165-187.
* [18]
   Suzuki, R. (2013). A Clark-Ocone type formula under change of measure for Lévy processes with L2L^{2}-Lévy measure. Communications on Stochastic Analysis, 7(3), 3.