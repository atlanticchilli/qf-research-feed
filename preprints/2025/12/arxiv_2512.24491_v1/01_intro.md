---
authors:
- Graeme Baker
- Ankita Chatterjee
doc_id: arxiv:2512.24491v1
family_id: arxiv:2512.24491
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2512.24491v1
url_html: https://arxiv.org/html/2512.24491v1
venue: arXiv q-fin
version: 1
year: 2025
---

Minimal Solutions to the Skorokhod Reflection Problem Driven by Jump Processes and an Application to Reinsurance

December 30, 2025

Graeme Baker111Department of Statistics, Columbia University, NY, USA [g.baker@columbia.edu](mailto:g.baker@columbia.edu) and Ankita Chatterjee222Department of Mathematics, Barnard College, NY, USA [ac5481@barnard.edu](mailto:ac5481@barnard.edu)

###### Abstract

We consider a reflected process in the positive orthant driven by an exogenous jump process. For a given input process, we show that there exists a unique minimal strong solution to the given particle system up until a certain stopping time, which is stated explicitly in terms of the dual formulation of a linear programming problem associated with the state of the system. We apply this model to study the ruin time of interconnected insurance firms, where the stopping time can be interpreted as the failure time of a reinsurance agreement between the firms. Our work extends the analysis of the particle system in [baker\_particle\_2025] to the case of jump driving processes, and the existence result of [reiman\_open\_1984] beyond the case of sub-stochastic reflection matrices.

## 1 Introduction

Fix a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) with a filtration 𝔽=(ℱt)t≥0−\mathbb{F}=(\mathcal{F}\_{t})\_{t\geq 0-} satisfying the usual hypotheses. Throughout this work, we require all of our stochastic processes to be càdlàg (meaning right continuous with left limits). We denote the jump of any given process AA at time tt by Δ​At:=At−At−\Delta A\_{t}:=A\_{t}-A\_{t-}. To allow for jumps at the initial time, we prepend a left limit 0−0- to a semi-infinite interval and consider the index set {0−}∪[0,∞)\{0-\}\cup[0,\infty). Consider n≥1n\geq 1 stochastic processes X1,…,XnX^{1},\dots,X^{n}, which for t≥0−t\geq 0- satisfy the system of equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xti=X0−i+ci​t−Zti+Lti−∑j≠iqi​j​Ltj,1≤i≤n,X\_{t}^{i}=X\_{0-}^{i}+c\_{i}t-Z\_{t}^{i}+L\_{t}^{i}-\sum\_{j\neq i}q\_{ij}L\_{t}^{j},\quad 1\leq i\leq n, |  | (1) |

where X0−1,…,X0−n≥0X\_{0-}^{1},\dots,X\_{0-}^{n}\geq 0 are ℱ0−\mathcal{F}\_{0-}-measurable initial conditions; c1,…,cnc\_{1},\dots,c\_{n} are non-negative constants; Q=(qi​j)i,j=1nQ=(q\_{ij})\_{i,j=1}^{n} is a non-negative matrix with qi​i=0q\_{ii}=0 for 1≤i≤n1\leq i\leq n; Z1,…,ZnZ^{1},\dots,Z^{n} are 𝔽\mathbb{F}-adapted jump processes with (almost surely) finitely many jumps in any interval (for instance, compound Poisson processes); and L1,…,LnL^{1},\dots,L^{n} are reflection processes which constrain X1,…,XnX^{1},\dots,X^{n} to remain in the non-negative orthant ℝ+n\mathbb{R}^{n}\_{+}.

We ask that the reflection processes each satisfy a one-dimensional Skorokhod reflection problem (see, for instance, [karatzas\_brownian\_2014, Lemma 6.14]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lti=sups≤t(X0−i+ci​t−Zsi−∑j≠iqi​j​Lsj)−,1≤i≤n,L\_{t}^{i}=\sup\_{s\leq t}\bigg(X\_{0-}^{i}+c\_{i}t-Z\_{s}^{i}-\sum\_{j\neq i}q\_{ij}L\_{s}^{j}\bigg)\_{-},\quad 1\leq i\leq n, |  | (2) |

where (a)−:=−min⁡(0,a)(a)\_{-}:=-\min(0,a) for a∈ℝa\in\mathbb{R}. For a given input process YY taking values in ℝ\mathbb{R}, Lt:=sups≤t(Ys)−L\_{t}:=\sup\_{s\leq t}(Y\_{s})\_{-} is the smallest non-decreasing process such that Y+LY+L is non-negative for all times. Given inputs X0−1,…,X0−nX\_{0-}^{1},\dots,X\_{0-}^{n}, and Z1,…,ZnZ^{1},\dots,Z^{n}, a strong solution to ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) consists of a pair of processes X=(X1,…,Xn)X=(X^{1},\dots,X^{n}) and L=(L1,…,Ln)L=(L^{1},\dots,L^{n}) which simultaneously satisfy ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction")) and ([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on a (possibly random) time interval [0,τ)[0,\tau).
In Theorem [1](https://arxiv.org/html/2512.24491v1#Thmtheorem1 "Theorem 1. ‣ 2 Main Result"), we show that a strong solution to ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on [0,τ)[0,\tau) can be continued to [0,τ][0,\tau] if and only if Xτ−−Δ​ZτX\_{\tau-}-\Delta Z\_{\tau} is contained in a certain dual cone. For x,y∈ℝnx,y\in\mathbb{R}^{n}, introduce the notation x≥yx\geq y to mean that xi≥yix\_{i}\geq y\_{i} for all 1≤i≤n1\leq i\leq n. As a consequence (Corollary [1](https://arxiv.org/html/2512.24491v1#Thmcorollary1 "Corollary 1. ‣ 2 Main Result")), we establish existence and uniqueness of a *minimal* solution (X,L)(X,L) and a *maximal* stopping time τ∗\tau^{\*} such that if (X~,L~)(\widetilde{X},\widetilde{L}) is any other strong solution to ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on [0,τ~)[0,\widetilde{\tau}) with the same initial condition and driving processes as (X,L)(X,L) then τ~≤τ∗\widetilde{\tau}\leq\tau^{\*} and Lt~≥Lt\widetilde{L\_{t}}\geq L\_{t} for all t∈[0,τ)t\in[0,\tau).

In a financial context, we interpret X1,…,XnX^{1},\dots,X^{n} as the resource levels of nn insurance firms bound by a reinsurance agreement. The firms collect premiums at the constant rates c1,…,cnc\_{1},\dots,c\_{n} and pay claims according to the exogenous shocks Z1,…,ZnZ^{1},\dots,Z^{n}. The matrix QQ encodes the routing of resources between firms due to reinsurance: firm ii remains solvent thanks to the the term LiL^{i}, but must contribute qi​j​Ljq\_{ij}L^{j} to firm jj. The amount transferred from all firms to firm jj by time tt is ∑i≠jqi​j​Ltj\sum\_{i\neq j}q\_{ij}L^{j}\_{t}. If ∑i≠jqi​j>1\sum\_{i\neq j}q\_{ij}>1, there is friction in the transfers to jj, possibly due to taxes or fees. The minimal solution L1,…,LnL^{1},\dots,L^{n} gives the most parsimonious choice to redistribute resources between X1,…,XnX^{1},\dots,X^{n}, keeping all resource levels non-negative at all times prior to the maximal time τ∗\tau^{\*}. We interpret τ∗\tau^{\*} itself as a ruin time, when there is insufficient liquidity and the reinsurance agreement breaks down. In Section [6](https://arxiv.org/html/2512.24491v1#S6 "6 Application to Reinsurance"), we compare ruin probabilities for a particular case with n=2n=2, both with and without reinsurance.

## 2 Main Result

When does ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) admit solutions? If the spectral radius of QQ, ρ​(Q)\rho(Q), is strictly less than 1, then solutions exist for all time by [reiman\_open\_1984, Proposition 1] (and see also [harrison\_reflected\_1981], for continuous driving processes such as Brownian motion). For ρ​(Q)≥1\rho(Q)\geq 1, can we go beyond this result? When the driving processes are Brownian motions, recent work has shown that existence and uniqueness hold on a stochastic interval which depends on the structure of QQ, the covariance of the driving processes, and the given initial condition [baker\_particle\_2025]. For the present setting where XX is driven by jump processes we state our main result, which we prove in Section [4](https://arxiv.org/html/2512.24491v1#S4 "4 Proof of Theorem 1").

###### Theorem 1.

Consider the cone C={u∈ℝn:u≥0,u⊤​(I−Q)≤0}C=\{u\in\mathbb{R}^{n}:u\geq 0,u^{\top}(I-Q)\leq 0\} and its dual cone C∗={y∈ℝn:u⊤​y≥0​ for all ​u∈C}C^{\*}=\{y\in\mathbb{R}^{n}:u^{\top}y\geq 0\text{ for all }u\in C\}.
A solution (X,L)(X,L) of ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on an interval [0,τ)[0,\tau) can be extended to [0,τ][0,\tau] if and only if Xτ−−Δ​Zτ∈C∗X\_{\tau-}-\Delta Z\_{\tau}\in C^{\*}. Moreover, when Xτ−−Δ​Zτ∈C∗X\_{\tau-}-\Delta Z\_{\tau}\in C^{\*} there exists a unique minimal Δ​Lτ\Delta L\_{\tau} with respect to the partial order ≥\geq on ℝ+n\mathbb{R}\_{+}^{n} such that Lτ=Lτ−+Δ​LτL\_{\tau}=L\_{\tau-}+\Delta L\_{\tau} gives an extension of (X,L)(X,L) on [0,τ][0,\tau].

As a corollary, show that for any given initial conditions and driving processes (Z1,…,Zn)(Z^{1},\dots,Z^{n}) there exists a unique minimal strong solution of ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on a maximal time interval (see, for instance, [delarue\_particle\_2015, cuchiero\_propagation\_2023, baker\_particle\_2025] for similar notions in a range of contexts).

###### Corollary 1.

Given inputs X0−1,…,X0−nX\_{0-}^{1},\dots,X\_{0-}^{n}, and Z1,…,ZnZ^{1},\dots,Z^{n}, there exists unique (X,L)(X,L) and τ∗\tau^{\*} such that (X,L)(X,L) solves ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on [0,τ∗)[0,\tau^{\*}) and if (X~,L~)(\widetilde{X},\widetilde{L}) is any other strong solution to ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on [0,τ~)[0,\widetilde{\tau}) with the same inputs as (X,L)(X,L) then τ~≤τ∗\widetilde{\tau}\leq\tau^{\*} and Lt~≥Lt\widetilde{L\_{t}}\geq L\_{t} for all t∈[0,τ~)t\in[0,\widetilde{\tau}).

###### Remark 1.

If ρ​(Q)<1\rho(Q)<1, then it is easy to see that CC is empty, C∗=ℝnC^{\*}=\mathbb{R}^{n}, and hence solutions may always be continued. Therefore, we have found a new derivation for the existence result of [reiman\_open\_1984, Proposition 1].

###### Proof of Corollary [1](https://arxiv.org/html/2512.24491v1#Thmcorollary1 "Corollary 1. ‣ 2 Main Result").

Consider any arbitrary solution (X~,L~)(\widetilde{X},\widetilde{L}) to ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on some interval [0,τ~)[0,\widetilde{\tau}).
Let τ1\tau\_{1} denote the first time that one or multiple of the processes Z1,…,ZnZ^{1},\dots,Z^{n} exhibit a jump. Set Lt1=⋯=Ltn=0L^{1}\_{t}=\dots=L^{n}\_{t}=0 on [0,τ1)[0,\tau\_{1}). From ([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")), we see that for 1≤i≤n1\leq i\leq n, L~ti≥0=Lti\widetilde{L}^{i}\_{t}\geq 0=L^{i}\_{t} for all t∈[0,τ1∧τ~)t\in[0,\tau\_{1}\wedge\widetilde{\tau}), where we have used the notation s∧t:=min⁡(s,t)s\wedge t:=\min(s,t). We consider now two cases:

*Case 1.* If Xτ1−−Δ​Zτ1∉C∗X\_{\tau\_{1}-}-\Delta Z\_{\tau\_{1}}\notin C^{\*}, then we set τ∗=τ1\tau^{\*}=\tau\_{1}. If τ~≥τ∗\widetilde{\tau}\geq\tau^{\*} then we must have X~τ1−−Δ​Zτ1∉C∗\widetilde{X}\_{\tau\_{1}-}-\Delta Z\_{\tau\_{1}}\notin C^{\*} and hence τ~>τ∗\widetilde{\tau}>\tau^{\*} is impossible.

*Case 2.* If Xτ1−−Δ​Zτ1∈C∗X\_{\tau\_{1}-}-\Delta Z\_{\tau\_{1}}\in C^{\*} we let Δ​Lτ1\Delta L\_{\tau\_{1}} be the unique minimal jump size from Theorem [1](https://arxiv.org/html/2512.24491v1#Thmtheorem1 "Theorem 1. ‣ 2 Main Result") and set Lτ1=0+Δ​Lτ1L\_{\tau\_{1}}=0+\Delta L\_{\tau\_{1}}.
If τ~<τ1\widetilde{\tau}<\tau\_{1}, then L~ti≥Lti\widetilde{L}^{i}\_{t}\geq L^{i}\_{t} for all t∈[0,τ1∧τ~]t\in[0,\tau\_{1}\wedge\widetilde{\tau}] trivially. If not, then suppose for the sake of contradiction that L~τ1i<Lτ1i\widetilde{L}^{i}\_{\tau\_{1}}<L^{i}\_{\tau\_{1}} for some 1≤i≤n1\leq i\leq n and for 1≤i≤n1\leq i\leq n set

|  |  |  |
| --- | --- | --- |
|  | L^ti={0t<τ1L~τ1it=τ1.\widehat{L}^{i}\_{t}=\begin{cases}0&t<\tau\_{1}\\ \widetilde{L}^{i}\_{\tau\_{1}}&t=\tau\_{1}.\end{cases} |  |

Then, the definition of τ1\tau\_{1} along with the non-negativity of X~\widetilde{X} imply that

|  |  |  |
| --- | --- | --- |
|  | X0−i+ci​t−Zti+L^ti−∑j≠iqi​j​L^tj≥0X\_{0-}^{i}+c\_{i}t-Z^{i}\_{t}+\widehat{L}^{i}\_{t}-\sum\_{j\neq i}q\_{ij}\widehat{L}^{j}\_{t}\geq 0 |  |

for all t∈[0,τ1]t\in[0,\tau\_{1}] and 1≤i≤n1\leq i\leq n. However, (Δ​L^τ11,…,Δ​L^τ1n)=(L~τ11,…,L~τ1n)(\Delta\widehat{L}^{1}\_{\tau\_{1}},\dots,\Delta\widehat{L}^{n}\_{\tau\_{1}})=(\widetilde{L}^{1}\_{\tau\_{1}},\dots,\widetilde{L}^{n}\_{\tau\_{1}}) contradicts the minimality of Δ​Lτ1\Delta L\_{\tau\_{1}} with respect to the partial order ≥\geq on ℝ+n\mathbb{R}\_{+}^{n}. Therefore L~ti≥Lti\widetilde{L}^{i}\_{t}\geq L^{i}\_{t} for all t∈[0,τ1∧τ~]t\in[0,\tau\_{1}\wedge\widetilde{\tau}].

Let τ2\tau\_{2} denote the next jump time for any of the processes Z1,…,ZnZ^{1},\dots,Z^{n}. Repeating the above argument shows that L~ti≥Lti\widetilde{L}^{i}\_{t}\geq L^{i}\_{t} for all t∈[0,τ2∧τ~]t\in[0,\tau\_{2}\wedge\widetilde{\tau}] and τ~>τ∗\widetilde{\tau}>\tau^{\*} is impossible. We continue as before with τ3,τ4\tau\_{3},\tau\_{4}, and so on. Since (X~,L~)(\widetilde{X},\widetilde{L}) and τ~\widetilde{\tau} are arbitrary, we have completed the proof. ∎

## 3 Increments of the Skorokhod Map

We prove here an auxiliary result, which allows us to express Δ​Lτ1,…,Δ​Lτn\Delta L^{1}\_{\tau},\dots,\Delta L^{n}\_{\tau} in terms of Xτ−X\_{\tau-} and Δ​Zτ\Delta Z\_{\tau}.

###### Lemma 1.

Let (Yt)t≥0−(Y\_{t})\_{t\geq 0-} be a càdlàg process taking values in ℝ\mathbb{R}. Define Lt=sups≤t(Ys)−L\_{t}=\sup\_{s\leq t}(Y\_{s})\_{-} and Xt=Yt+LtX\_{t}=Y\_{t}+L\_{t}. Then for all t≥0−t\geq 0-,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Lt=(Xt−+Δ​Yt)−\Delta L\_{t}=\left(X\_{t-}+\Delta Y\_{t}\right)\_{-} |  | (3) |

###### Proof.

We split the proof into the cases −Yt≤Lt−-Y\_{t}\leq L\_{t-} and −Yt>Lt−-Y\_{t}>L\_{t-}
First, suppose −Yt≤Lt−-Y\_{t}\leq L\_{t-}. Then Δ​Lt=0\Delta L\_{t}=0 and

|  |  |  |
| --- | --- | --- |
|  | Xt−+Δ​Yt=Yt−+Lt−+Yt−Yt−≥0.\displaystyle X\_{t-}+\Delta Y\_{t}=Y\_{t-}+L\_{t-}+Y\_{t}-Y\_{t-}\geq 0. |  |

Hence (Xt−+Δ​Yt)−=0=Δ​Lt\left(X\_{t-}+\Delta Y\_{t}\right)\_{-}=0=\Delta L\_{t} and ([3](https://arxiv.org/html/2512.24491v1#S3.E3 "In Lemma 1. ‣ 3 Increments of the Skorokhod Map")) holds. Next, if −Yt>Lt−-Y\_{t}>L\_{t-}, then Lt=−Yt≥0L\_{t}=-Y\_{t}\geq 0 and hence

|  |  |  |
| --- | --- | --- |
|  | Δ​Lt=Lt−Lt−=−Yt−(Xt−−Yt−)=−(Xt−+Δ​Yt)≥0.\displaystyle\Delta L\_{t}=L\_{t}-L\_{t-}=-Y\_{t}-(X\_{t-}-Y\_{t-})=-(X\_{t-}+\Delta Y\_{t})\geq 0. |  |

We see that ([3](https://arxiv.org/html/2512.24491v1#S3.E3 "In Lemma 1. ‣ 3 Increments of the Skorokhod Map")) is established in this case as well. ∎

## 4 Proof of Theorem [1](https://arxiv.org/html/2512.24491v1#Thmtheorem1 "Theorem 1. ‣ 2 Main Result")

We proceed by reducing to a linear programming problem.
An example of the primal and dual problems with n=2n=2 is plotted in Figure [1](https://arxiv.org/html/2512.24491v1#S4.F1 "Figure 1 ‣ 4 Proof of Theorem 1").

###### Proof.

Suppose Δ​Zτ=(Δ​Zτ1,…,Δ​Zτn)\Delta Z\_{\tau}=(\Delta Z^{1}\_{\tau},\dots,\Delta Z^{n}\_{\tau}) is non-zero (otherwise, the problem is trivial). By Lemma [1](https://arxiv.org/html/2512.24491v1#Thmlemma1 "Lemma 1. ‣ 3 Increments of the Skorokhod Map"), if we can exhibit a jump Δ​Lτ=(Δ​Lτ1,…,Δ​Lτn)∈ℝ+n\Delta L\_{\tau}=(\Delta L^{1}\_{\tau},\dots,\Delta L^{n}\_{\tau})\in\mathbb{R}^{n}\_{+} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Lτi=(Xτ−i−Δ​Zτi−∑j≠iqi​j​Δ​Lτj)−,1≤i≤n,\Delta L^{i}\_{\tau}=\bigg(X\_{\tau-}^{i}-\Delta Z\_{\tau}^{i}-\sum\_{j\neq i}q\_{ij}\Delta L\_{\tau}^{j}\bigg)\_{-},\quad 1\leq i\leq n, |  | (4) |

then setting Lτ=Lτ−+Δ​LτL\_{\tau}=L\_{\tau\_{-}}+\Delta L\_{\tau} and Xτ=Xτ−−Δ​Zτ+(I−Q)​Δ​LτX\_{\tau}=X\_{\tau\_{-}}-\Delta Z\_{\tau}+(I-Q)\Delta L\_{\tau} yields a solution to ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")) on [0,τ][0,\tau]. Consider the linear programming (LP) problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimize | ‖Δ​Lτ‖1\displaystyle\quad\|\Delta L\_{\tau}\|\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to | Δ​Lτ≥0​ and ​(I−Q)​Δ​Lτ≥−(Xτ−−Δ​Zτ).\displaystyle\quad\Delta L\_{\tau}\geq 0\text{ and }(I-Q)\Delta L\_{\tau}\geq-\left(X\_{\tau-}-\Delta Z\_{\tau}\right). |  |

If Δ​Lτ\Delta L\_{\tau} solves LP, then for each ii, at least one of the following equalities must hold

|  |  |  |
| --- | --- | --- |
|  | Δ​Lτi=0 or Δ​Lτi=−(Xτ−i−Δ​Zτi)+∑j≠iqi​j​Δ​Lτj,\displaystyle\Delta L^{i}\_{\tau}=0\quad\text{ or }\quad\Delta L^{i}\_{\tau}=-\left(X\_{\tau-}^{i}-\Delta Z\_{\tau}^{i}\right)+\sum\_{j\neq i}q\_{ij}\Delta L\_{\tau}^{j}, |  |

since otherwise Δ​Lτi\Delta L^{i}\_{\tau} may be decreased and the objective function ‖Δ​Lτ‖1\|\Delta L\_{\tau}\|\_{1} will be decreased. Hence, if Δ​Lτ\Delta L\_{\tau} solves LP then ([4](https://arxiv.org/html/2512.24491v1#S4.E4 "In Proof. ‣ 4 Proof of Theorem 1")) holds. We tackle the feasibility of LP using duality.

Rewrite the constraints on Δ​Lτ\Delta L\_{\tau} as

|  |  |  |
| --- | --- | --- |
|  | A​Δ​Lτ≥bwhereA=[I−QI]andb=[−Xτ−+Δ​Zτ0].A\Delta L\_{\tau}\geq b\quad\text{where}\quad A=\begin{bmatrix}I-Q\\ I\end{bmatrix}\quad\text{and}\quad b=\begin{bmatrix}-X\_{\tau-}+\Delta Z\_{\tau}\\ 0\end{bmatrix}. |  |

Farkas’s Lemma (see, for instance [dantzig\_linear\_1997-1, Theorem 2.1], where it is called the Infeasibility Theorem) implies that LP is infeasible if and only if there exists y≥0y\geq 0 such that y⊤​A=0y^{\top}A=0 and y⊤​b>0y^{\top}b>0. We seek to reduce this latter condition to the condition in the statement of the theorem. Write y⊤=[u⊤,v⊤]y^{\top}=[u^{\top},\,v^{\top}] where u,v∈ℝnu,v\in\mathbb{R}^{n}. Then y⊤​A=0y^{\top}A=0 implies that v⊤=−u⊤​(I−Q)v^{\top}=-u^{\top}(I-Q). The condition y⊤​b>0y^{\top}b>0 simplifies to

|  |  |  |
| --- | --- | --- |
|  | y⊤​b=−u⊤​(Xτ−−Δ​Zτ)>0.y^{\top}b=-u^{\top}(X\_{\tau-}-\Delta Z\_{\tau})>0. |  |

Therefore, LP is infeasible if and only if there exists u≥0u\geq 0 with −u⊤​(I−Q)=v⊤≥0-u^{\top}(I-Q)=v^{\top}\geq 0 and −u⊤​(Xτ−−Δ​Zτ)>0-u^{\top}(X\_{\tau-}-\Delta Z\_{\tau})>0. The conditions on uu and vv define the cone CC from the statement of the theorem, and there will be u∈Cu\in C such that −u⊤​(Xτ−−Δ​Nτ)>0-u^{\top}(X\_{\tau-}-\Delta N\_{\tau})>0 iff Xτ−−Δ​Nτ∉C∗X\_{\tau-}-\Delta N\_{\tau}\notin C^{\*}.

It remains to show uniqueness of the minimal jump. Suppose that Δ​Lτ≥0\Delta L\_{\tau}\geq 0 and [I−Q]i​Δ​Lτ=0{[I-Q]\_{i}\Delta L\_{\tau}=0}, where [I−Q]i[I-Q]\_{i} denotes the iith row of I−QI-Q. Then Δ​Lτi=∑j≠iqi​j​Δ​Lτj\Delta L\_{\tau}^{i}=\sum\_{j\neq i}q\_{ij}\Delta L\_{\tau}^{j} and hence

|  |  |  |
| --- | --- | --- |
|  | (1,1,…,1)⊤​Δ​Lτ=Δ​Lτi+∑j≠iΔ​Lτj=∑j≠i(1+qi​j)​Δ​Lτj≥0(1,1,\dots,1)^{\top}\Delta L\_{\tau}=\Delta L\_{\tau}^{i}+\sum\_{j\neq i}\Delta L\_{\tau}^{j}=\sum\_{j\neq i}(1+q\_{ij})\Delta L\_{\tau}^{j}\geq 0 |  |

with equality if and only if Δ​Lτ=0\Delta L\_{\tau}=0. Therefore, none of the constraining faces in the feasible region are orthogonal to (1,1,…,1)(1,1,\dots,1), and hence uniqueness holds for LP. Note that uniqueness still holds if the objective function is replaced by a⊤​Δ​Lτa^{\top}\Delta L\_{\tau} for any aa with strictly positive entries. This yields minimality with respect to the partial order ≥\geq on ℝ+n\mathbb{R}\_{+}^{n}.
∎

![Refer to caption](Primal.png)


(a) Primal problem. The feasible region is plotted in purple. The minimal jump is given by (1,0)(1,0).

![Refer to caption](Cone.png)


(b) Dual problem. CC is plotted in purple, and the union of the purple and blue regions gives C∗C^{\*}. Note that (−1,6)∈C∗(-1,6)\in C^{\*}.

Figure 1: Example primal and dual problems with n=2n=2, q12=q21=2q\_{12}=q\_{21}=2, and (Xτ−1−Δ​Zτ1,Xτ−2−Δ​Zτ2)=(−1,6){(X\_{\tau-}^{1}-\Delta Z\_{\tau}^{1},X\_{\tau-}^{2}-\Delta Z\_{\tau}^{2})=(-1,6)}. In this case, the primal problem is feasible.

## 5 Fixed Point Approach

When the LP problem is feasible, it can be solved efficiently using the simplex method [dantzig\_linear\_1997-1]. Another approach is to construct a solution iteratively with a monotone operator (see, for instance, a similar approach in [cuchiero\_propagation\_2023, Proposition 2.3]). For a given input vector Xτ−−Δ​ZτX\_{\tau-}-\Delta Z\_{\tau}, define the operator Γ:ℝ+n→ℝ+N\Gamma:\mathbb{R}\_{+}^{n}\to\mathbb{R}\_{+}^{N} by

|  |  |  |
| --- | --- | --- |
|  | Γ​[z]=((Xτ−1−Δ​Zτ1−∑j≠1q1​j​zj)−,…,(Xτ−1−Δ​Zτ1−∑j≠nqn​j​zj)−)\Gamma[z]=\bigg(\big(X\_{\tau-}^{1}-\Delta Z\_{\tau}^{1}-\sum\_{j\neq 1}q\_{1j}z\_{j}\big)\_{-},\dots,\big(X\_{\tau-}^{1}-\Delta Z\_{\tau}^{1}-\sum\_{j\neq n}q\_{nj}z\_{j}\big)\_{-}\bigg) |  |

We notice that fixed points of Γ\Gamma (that is, any z∗z^{\*} such that Γ​[z∗]=z∗\Gamma[z^{\*}]=z^{\*}) satisfy ([4](https://arxiv.org/html/2512.24491v1#S4.E4 "In Proof. ‣ 4 Proof of Theorem 1")). One can check that Γ\Gamma is monotone (that is, Γ​[z]≥z\Gamma[z]\geq z for all zz). Therefore, the Knaster–Tarski Theorem implies that the fixed points of Γ\Gamma form a complete lattice (this result is often used for existence of fixed points in systemic risk literature, such as the seminal work [eisenberg\_systemic\_2001]). Starting from z=0z=0 and applying Γ\Gamma iteratively yields the (*a fortiori*) unique solution to LP in the limit.

## 6 Application to Reinsurance

We consider now a particular case with n=2n=2 insurance firms. As a base case in the absence of reinsurance, we suppose that for t≥0−t\geq 0-, X(1)X^{(1)} and X(2)X^{(2)} satisfy

|  |  |  |
| --- | --- | --- |
|  | Xt(1)=X0−1+c1​t−Zt1,andXt(2)=X0−2+c1​t−Zt2,X^{(1)}\_{t}=X^{1}\_{0-}+c\_{1}t-Z^{1}\_{t},\quad\text{and}\quad X^{(2)}\_{t}=X^{2}\_{0-}+c\_{1}t-Z^{2}\_{t}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Zt1=∑k=1Nt1+Nt3Yk1,andZt2=∑k=1Nt2+Nt3Yk2;Z^{1}\_{t}=\sum\_{k=1}^{N^{1}\_{t}+N^{3}\_{t}}Y^{1}\_{k},\quad\text{and}\quad Z^{2}\_{t}=\sum\_{k=1}^{N^{2}\_{t}+N^{3}\_{t}}Y^{2}\_{k}; |  |

X0−1,X0−2X^{1}\_{0-},X^{2}\_{0-} are ℱ0−\mathcal{F}\_{0-}-measurable initial conditions; c1,c2≥0c\_{1},c\_{2}\geq 0 are fixed; N1,N2N^{1},N^{2}, and N3N^{3} are independent 𝔽\mathbb{F}-adapted Poisson processes with intensities λ1,λ2\lambda\_{1},\lambda\_{2}, and λ3\lambda\_{3}; and (Yk1)k≥1(Y^{1}\_{k})\_{k\geq 1} and (Yk2)k≥1(Y^{2}\_{k})\_{k\geq 1} are each sequences of independent and identically distributed random variables with distributions Y11Y^{1}\_{1} and Y12Y^{2}\_{1}, respectively. The ruin time of each firm is given by

|  |  |  |
| --- | --- | --- |
|  | T1=inf{t≥0:Xt(1)≤0},andT2=inf{t≥0:Xt(2)≤0}.T^{1}=\inf\{t\geq 0:X^{(1)}\_{t}\leq 0\},\quad\text{and}\quad T^{2}=\inf\{t\geq 0:X^{(2)}\_{t}\leq 0\}. |  |

We have here two instances of a classical insurance risk model (see, for instance, [kluppelberg\_ruin\_2004]), which have been coupled together by the common Poisson process N3N^{3}.

In Figure [2](https://arxiv.org/html/2512.24491v1#S6.F2 "Figure 2 ‣ 6 Application to Reinsurance"), we plot Monte Carlos estimates of the ruin probabilities t↦ℙ​(T1≤t)t\mapsto\mathbb{P}(T^{1}\leq t), t↦ℙ​(T2≤t)t\mapsto\mathbb{P}(T^{2}\leq t), t↦ℙ​(T1≤t,T2≤t)t\mapsto\mathbb{P}(T^{1}\leq t,T^{2}\leq t), and t↦ℙ​(T1≤t​ or ​T2≤t)t\mapsto\mathbb{P}(T^{1}\leq t\text{ or }T^{2}\leq t) for a particular choice of parameters. The plots were generated using 20000 Monte Carlo trials, X0−(1)=X0−(2)=5X^{(1)}\_{0-}=X^{(2)}\_{0-}=5, Y11Y^{1}\_{1} and Y12Y^{2}\_{1} are both Exp​(1)\mathrm{Exp}(1) random variables, c1=c2=1.2c\_{1}=c\_{2}=1.2, and λ1=λ2=λ3=0.6\lambda\_{1}=\lambda\_{2}=\lambda\_{3}=0.6. The conditions for the firms are symmetrical so that ℙ​(T1≤t)=ℙ​(T2≤t)\mathbb{P}(T^{1}\leq t)=\mathbb{P}(T^{2}\leq t) for all tt. Closed form solutions for the ruin probabilities are available in some special cases (see [kluppelberg\_ruin\_2004] and also [bernyk\_law\_2008]), but we do not pursue them here. For limiting behavior as t→∞t\to\infty, [jeanblanc\_mathematical\_2009, Lemma 8.7.1.1] gives that ℙ​(T1<∞)=1\mathbb{P}(T^{1}<\infty)=1 if c1/(λ1+λ3)≤𝔼​[Y11]<∞c\_{1}/(\lambda\_{1}+\lambda\_{3})\leq\mathbb{E}[Y\_{1}^{1}]<\infty, and similarly for T2T^{2}. More generally, one may deduce an integral equation for Ψ​(x):=ℙ​(T1=∞|X0−1=x){\Psi(x):=\mathbb{P}(T^{1}=\infty|X^{1}\_{0-}=x)} in the variable xx (we refer the interested reader to [jeanblanc\_mathematical\_2009, Subsection 8.7.2]).

![Refer to caption](CDF_T=500_a=0.05.png)


Figure 2: Ruin probabilities on the time interval t∈[0,500]t\in[0,500] when α=0.05\alpha=0.05.

Next, we compare to the case with reinsurance, that is, the minimal solution of the reflected system ([1](https://arxiv.org/html/2512.24491v1#S1.E1 "In 1 Introduction"))–([2](https://arxiv.org/html/2512.24491v1#S1.E2 "In 1 Introduction")). We take the same initial conditions and driving processes. We suppose that q12=q21=1+αq\_{12}=q\_{21}=1+\alpha where α>0\alpha>0 represents friction due to taxes and fees. In Figure [2](https://arxiv.org/html/2512.24491v1#S6.F2 "Figure 2 ‣ 6 Application to Reinsurance"), we have plotted a Monte Carlo estimate for t↦ℙ​(τ∗≤t)t\mapsto\mathbb{P}(\tau^{\*}\leq t) (again using 20000 trials) alongside t↦ℙ​(T1≤t)t\mapsto\mathbb{P}(T^{1}\leq t), t↦ℙ​(T1≤t,T2≤t)t\mapsto\mathbb{P}(T^{1}\leq t,T^{2}\leq t), and t↦ℙ​(T1≤t​ or ​T2≤t)t\mapsto\mathbb{P}(T^{1}\leq t\text{ or }T^{2}\leq t), with α=0.05\alpha=0.05 and all other parameters unchanged. In general, the distribution of ℙ​(τ∗≤t)\mathbb{P}(\tau^{\*}\leq t) is difficult to compute. However, for the special case α=0\alpha=0 we see that

|  |  |  |
| --- | --- | --- |
|  | Xt1+Xt2=X0−1+X0−2+(c1+c2)​t−Zt1−Zt2,X^{1}\_{t}+X^{2}\_{t}=X^{1}\_{0-}+X^{2}\_{0-}+(c\_{1}+c\_{2})t-Z^{1}\_{t}-Z^{2}\_{t}, |  |

is also a classical 1-dimensional ruin model. Using [jeanblanc\_mathematical\_2009, Lemma 8.7.1.1], we see that ℙ​(τ∗<∞)=1\mathbb{P}(\tau^{\*}<\infty)=1 when (c1+c2)/(λ1+λ2+λ3)≤23​(𝔼​[Y11]+𝔼​[Y21])(c\_{1}+c\_{2})/(\lambda\_{1}+\lambda\_{2}+\lambda\_{3})\leq\frac{2}{3}(\mathbb{E}[Y\_{1}^{1}]+\mathbb{E}[Y\_{2}^{1}]), and by comparison this sufficient condition holds for any α>0\alpha>0.

With the parameters used in Figure [2](https://arxiv.org/html/2512.24491v1#S6.F2 "Figure 2 ‣ 6 Application to Reinsurance"), at any given time we see that the Monte Carlo estimate for the ruin probability of the reflected system (X1,X2)(X^{1},X^{2}) is higher than the probability that both X(1)X^{(1)} and X(2)X^{(2)} fail, but lower than the probability that at least one of X(1)X^{(1)} and X(2)X^{(2)} fail. Furthermore, ℙ​(τ∗≤t)≤ℙ​(T1≤t)=ℙ​(T2≤t)\mathbb{P}(\tau^{\*}\leq t)\leq\mathbb{P}(T^{1}\leq t)=\mathbb{P}(T^{2}\leq t) for all tt. This suggests that each individual firm might consider opting into this reinsurance agreement to increase their individual chance of survival on a given time horizon. If the friction parameter α\alpha is increased, then the curve t↦ℙ​(T1≤t)t\mapsto\mathbb{P}(T^{1}\leq t) may no longer dominate t↦ℙ​(τ∗≤t)t\mapsto\mathbb{P}(\tau^{\*}\leq t). For instance, this is observed when α\alpha is increased to 0.50.5 and all other parameters are unchanged (see Figure [3](https://arxiv.org/html/2512.24491v1#S6.F3 "Figure 3 ‣ 6 Application to Reinsurance")).

![Refer to caption](CDF_T=500_a=0.5.png)


Figure 3: Ruin probabilities on the time interval t∈[0,500]t\in[0,500] when α=0.5\alpha=0.5.

For small times, we can compare the failure probabilities by computing the slopes of the curves. The quantities dd​t​ℙ​(T1≤t)|t=0\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(T^{1}\leq t)|\_{t=0}, dd​t​ℙ​(T2≤t)|t=0\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(T^{2}\leq t)|\_{t=0}, dd​t​ℙ​(T1≤t,T2≤t)|t=0\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(T^{1}\leq t,T^{2}\leq t)|\_{t=0}, dd​t​ℙ​(T1≤t​ or ​T2≤t)|t=0\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(T^{1}\leq t\text{ or }T^{2}\leq t)|\_{t=0}, and dd​t​ℙ​(τ∗≤t)|t=0\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(\tau^{\*}\leq t)|\_{t=0} are given by the intensities for which t↦X0−−Ztt\mapsto X\_{0-}-Z\_{t} jumps out of the regions H1={(y1,y2):y1>0}H^{1}=\{(y\_{1},y\_{2}):y\_{1}>0\}, H2={(y1,y2):y2>0}H^{2}=\{(y\_{1},y\_{2}):y\_{2}>0\}, H1∪H2H^{1}\cup H^{2}, H1∩H2H^{1}\cap H^{2}, and C∗C^{\*}, respectively. For α>0\alpha>0, the inclusions H1∩H2⊆C∗⊆H1∪H2H^{1}\cap H^{2}\subseteq C^{\*}\subseteq H^{1}\cup H^{2} imply that dd​t​ℙ​(T1≤t,T2≤t)|t=0≤dd​t​ℙ​(τ∗≤t)|t=0≤ℙ​(T1≤t​ or ​T2≤t)\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(T^{1}\leq t,T^{2}\leq t)|\_{t=0}\leq\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{P}(\tau^{\*}\leq t)|\_{t=0}\leq\mathbb{P}(T^{1}\leq t\text{ or }T^{2}\leq t) for any choice of the model parameters (X0−(1),X0−(2),Y11,Y12,c1,c2,λ1,λ2,λ3)(X^{(1)}\_{0-},X^{(2)}\_{0-},Y^{1}\_{1},Y^{2}\_{1},c\_{1},c\_{2},\lambda\_{1},\lambda\_{2},\lambda\_{3}). For instance, in Figure [4](https://arxiv.org/html/2512.24491v1#S6.F4 "Figure 4 ‣ 6 Application to Reinsurance"), we have plotted the same curves as in Figure [3](https://arxiv.org/html/2512.24491v1#S6.F3 "Figure 3 ‣ 6 Application to Reinsurance") on an interval near the origin: t∈[0,10]t\in[0,10]. While ℙ​(τ∗≤t)\mathbb{P}(\tau^{\*}\leq t) may be greater than ℙ​(T1≤t)\mathbb{P}(T^{1}\leq t) for tt sufficiently large (Figure [3](https://arxiv.org/html/2512.24491v1#S6.F3 "Figure 3 ‣ 6 Application to Reinsurance")), this is not the case for small tt (Figure [4](https://arxiv.org/html/2512.24491v1#S6.F4 "Figure 4 ‣ 6 Application to Reinsurance")).

![Refer to caption](CDF_T=10_a=0.5.png)


Figure 4: Ruin probabilities on the time interval t∈[0,10]t\in[0,10] when α=0.5\alpha=0.5.

## Acknowledgments

We acknowledge the Summer Research Institute at Barnard College as well as the Statistics Department at Columbia University for funding which supported this summer undergraduate research project. We thank Professor Karatzas for suggesting this collaboration, and for his helpful feedback on an early draft. Additionally, we thank Professor Reiman for many helpful discussions.