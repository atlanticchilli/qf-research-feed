---
authors:
- Masaaki Fujii
doc_id: arxiv:2512.21621v1
family_id: arxiv:2512.21621
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Mean-Field Price Formation on Trees with a Network of Relative Performance
  Concerns
url_abs: http://arxiv.org/abs/2512.21621v1
url_html: https://arxiv.org/html/2512.21621v1
venue: arXiv q-fin
version: 1
year: 2025
---


Masaaki Fujii111mfujii@e.u-tokyo.ac.jp, Graduate School of Economics, The University of Tokyo, Tokyo, Japan 
222The author is not responsible in any manner for any losses caused by the use of any contents in this research.

( First version: December 25, 2025
)

###### Abstract

Financial firms and institutional investors are routinely evaluated based on their performance relative to their peers.
These relative performance concerns significantly influence risk-taking behavior and market dynamics.
While the literature studying Nash equilibrium under such relative performance competitions is extensive,
its effect on asset price formation remains largely unexplored. This paper investigates mean-field equilibrium price formation
of a single risky stock in a discrete-time market where agents exhibit exponential utility and relative performance concerns.
Unlike existing literature that typically treats asset prices as exogenous, we impose a market-clearing condition to determine
the price dynamics endogenously within a relative performance equilibrium. Using a binomial tree framework,
we establish the existence and uniqueness of the market-clearing mean-field equilibrium in both single- and multi-population settings.
Finally, we provide illustrative numerical examples demonstrating the equilibrium price distributions and agents’ optimal position sizes.

Keywords:
mean-field game, multiple populations, market-clearing, relative performance concerns

## 1 Introduction

In this paper, we study the problem of equilibrium price formation for agents with exponential utility.
In addition to a partially hedgeable stochastic terminal liability, each agent is assumed to have concerns
over the average trading performance of peers. We assume the presence of multiple heterogeneous populations
forming a network of relative performance concerns and study how it influences the equilibrium
price distribution under the market-clearing condition. To handle this many-agent problem,
we make use of techniques from mean-field game (MFG) theory.
MFG was pioneered independently by the seminal works
of Lasry & Lions [[39](https://arxiv.org/html/2512.21621v1#bib.bib39), [40](https://arxiv.org/html/2512.21621v1#bib.bib40), [41](https://arxiv.org/html/2512.21621v1#bib.bib41)] and by those of Huang et al. [[34](https://arxiv.org/html/2512.21621v1#bib.bib34), [35](https://arxiv.org/html/2512.21621v1#bib.bib35), [36](https://arxiv.org/html/2512.21621v1#bib.bib36)].
MFG is a powerful tool to analyze symmetric strategic interactions
in large populations when each individual player has a negligible
impact on the collective behavior and the state of the others.
This condition is particularly well suited
for financial and economic applications,
and there is an extensive body of literature applying MFG techniques to many-agent problems.
See, for example, [[1](https://arxiv.org/html/2512.21621v1#bib.bib1), [2](https://arxiv.org/html/2512.21621v1#bib.bib2), [3](https://arxiv.org/html/2512.21621v1#bib.bib3), [4](https://arxiv.org/html/2512.21621v1#bib.bib4), [6](https://arxiv.org/html/2512.21621v1#bib.bib6), [25](https://arxiv.org/html/2512.21621v1#bib.bib25)]
and the references therein.

In recent years, there have also been major advances in MFG theory for applications
in the equilibrium price-formation problem, where the asset price process is endogenously constructed to ensure
that demand and supply always balance among heterogeneous but exchangeable agents,
rather than being exogenously given.
Gomes & Saúde [[27](https://arxiv.org/html/2512.21621v1#bib.bib27)] present a deterministic model
of electricity prices. Its extension with random supply is given by Gomes et al. [[26](https://arxiv.org/html/2512.21621v1#bib.bib26)].
Ashrafyan et al. [[5](https://arxiv.org/html/2512.21621v1#bib.bib5)] propose a duality approach transforming these problems
into variational ones. Shrivats et al. [[33](https://arxiv.org/html/2512.21621v1#bib.bib33)] address a price formation problem for
the solar renewable energy certificate (SREC). Féron et al. [[13](https://arxiv.org/html/2512.21621v1#bib.bib13)] develop a tractable
equilibrium model for intraday electricity markets.
Sarto et al. [[32](https://arxiv.org/html/2512.21621v1#bib.bib32)] study cap-and-trade pollution regulation.
Regarding price formation in securities markets, Fujii & Takahashi [[22](https://arxiv.org/html/2512.21621v1#bib.bib22)] show
that the equilibrium price process can be characterized by FBSDEs of conditional
McKean-Vlasov type. The strong convergence to the mean-field limit from a finite-agent setting
is proved in [[23](https://arxiv.org/html/2512.21621v1#bib.bib23)], and its extension to the presence of a major player is given in [[24](https://arxiv.org/html/2512.21621v1#bib.bib24)] by the same authors.
Fujii [[19](https://arxiv.org/html/2512.21621v1#bib.bib19)] develops a model that allows the co-presence of cooperative and non-cooperative populations.
By using the martingale optimality principle developed by Hu et al. [[28](https://arxiv.org/html/2512.21621v1#bib.bib28)],
Fujii & Sekine [[20](https://arxiv.org/html/2512.21621v1#bib.bib20), [21](https://arxiv.org/html/2512.21621v1#bib.bib21)] solve the mean-field price formation
for agents with exponential utilities, allowing for general self-financing strategies.
In contrast to these continuous-time models, Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)]
adopts a discrete-time framework with a recombining binomial tree for the stock price process.
By leveraging the simple structure of the binomial lattice, the author provides
the explicit solutions for the equilibrium transition probabilities for exponential utility as well as exponential-type recursive utility
in the presence of multiple populations.

Despite these advancements, the aforementioned models assume that agents are concerned exclusively with
their own trading performance. In practice, however, institutional investors and
fund managers are often evaluated based on their performance relative to a benchmark or the average
performance of their peers. Such relative performance concerns, often referred to as ”keeping up with the Joneses,”
can lead to significant changes in risk-taking behavior and market dynamics.
This motivation has led to an extensive study of optimal investment under relative performance concerns.
The foundational work of Espinosa & Touzi [[12](https://arxiv.org/html/2512.21621v1#bib.bib12)] investigates the Nash equilibrium in a finite-agent setting
as well as its large population limit. Specifically, they analyze unconstrained agents with general utilities
and constrained agents with exponential utilities.
On the other hand, Frei & dos Reis [[14](https://arxiv.org/html/2512.21621v1#bib.bib14)] explore the existence of equilibrium in similar games
and also construct a counterexample to show that an equilibrium may not exist.
Lacker & Zariphopoulou [[30](https://arxiv.org/html/2512.21621v1#bib.bib30)] introduce a model where agents trade distinct stocks
correlated through a common noise.
Later, with the development of MFG theory, the idea of distinct stocks introduced by [[30](https://arxiv.org/html/2512.21621v1#bib.bib30)]
has been applied to various models and setups. For instance, Fu [[15](https://arxiv.org/html/2512.21621v1#bib.bib15)], Fu & Zhou [[16](https://arxiv.org/html/2512.21621v1#bib.bib16)],
and more recently Dianetti et al. [[9](https://arxiv.org/html/2512.21621v1#bib.bib9)] and
Fu & Horst [[17](https://arxiv.org/html/2512.21621v1#bib.bib17)] investigate mean-field
portfolio games with various preference structures, including consumption and Epstein-Zin preferences.
The use of forward utilities in relative performance MFGs has also been analyzed by dos Reis & Platonov [[10](https://arxiv.org/html/2512.21621v1#bib.bib10), [11](https://arxiv.org/html/2512.21621v1#bib.bib11)].

However, while these works provide deep insights into optimal strategies and Nash equilibria
for the relative performance competitions, they treat the asset price process as exogenously given.
Hence the problem of how such relative concerns endogenously shape the market stock price remains largely unanswered, in particular,
for incomplete markets. As observed in Espinosa & Touzi [[12](https://arxiv.org/html/2512.21621v1#bib.bib12)], when the risk-premium of the stock
is independent of the strength of relative concerns θ\theta,
the effective risk tolerance of each agent and hence their optimal position
increase as θ\theta increases. They even diverge in the limit θ→1\theta\rightarrow 1.
This raises a natural question: what would happen if we impose the market-clearing condition?
By definition, market clearing prevents all agents from simultaneously holding infinitely large positions in the same direction.
It is plausible that the risk premium strongly depends on θ\theta and adjusts the demand for the stock among the agents
to clear the market.
Unfortunately, since the existing literature relies heavily on very complex and delicate mathematics
of quadratic backward stochastic differential equations (BSDEs) and their mean-field extensions,
imposing the market-clearing condition on top of the relative performance
Nash equilibrium presents a formidable technical challenge.

In this paper, we fill this gap by extending the discrete-time framework of Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)] to incorporate
relative performance concerns. We combine MFG theory with the classic idea of binomial trees, initiated by Sharpe [[43](https://arxiv.org/html/2512.21621v1#bib.bib43)]
and formalized in Cox, Ross & Rubinstein [[7](https://arxiv.org/html/2512.21621v1#bib.bib7)].
We consider a market populated by agents—financial and investment firms—categorized into distinct populations, indexed by p=1,2,…,mp=1,2,\ldots,m,
who engage in self-financing trading with a common risky stock and a risk-free money market account.
Agents in each population are subject to distinct stochastic liabilities FpF^{p}
and distinct distributions of idiosyncratic factors.
More crucially, we introduce a heterogeneous network of relative performance concerns
represented by (θp,ki,1≤p,k≤m,i=1,2,…)(\theta^{i}\_{p,k},1\leq p,k\leq m,i=1,2,\ldots), which denote the sensitivity of agent-ii in population pp
relative to the average performance of population kk. The aggregate structure of this network is captured by an m×mm\times m interaction matrix
Θ:=𝔼​[θi]\Theta:=\mathbb{E}[\theta^{i}].
Our main contributions are summarized as follows:

* •

  In the single population case (m=1m=1), we prove the existence and uniqueness of the market-clearing mean-field
  equilibrium (MC-MFE) associated with the relative-performance mean-field equilibrium (RP-MFE)
  for any sensitivity parameter Θ∈ℝ\Theta\in\mathbb{R}.
* •

  In the mm-population case, we prove that there is a unique MC-MFE provided that (I−Θ)(I-\Theta)
  is invertible or dim​Ker​(I−Θ)=1\mathrm{dim}~\mathrm{Ker}(I-\Theta)=1. Moreover, utilizing resolvent expansion techniques,
  we demonstrate that the equilibrium solutions remain continuous even around the singular points where
  (I−Θ)(I-\Theta) exhibits a first-order pole.
* •

  We derive all these results explicitly based on tractable backward induction arguments and provide
  several illustrative numerical examples.

The rest of the paper is organized as follows: Section [2](https://arxiv.org/html/2512.21621v1#S2 "2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") studies the single population case m=1m=1
with relative performance concerns (θi,i∈ℕ)(\theta^{i},i\in\mathbb{N});
Section [3](https://arxiv.org/html/2512.21621v1#S3 "3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") analyzes an mm-population model with a network of relative
performance concerns (θp,ki,1≤p,k≤m,i∈ℕ)(\theta^{i}\_{p,k},1\leq p,k\leq m,i\in\mathbb{N}). The continuity around the first-order pole of (I−Θ)(I-\Theta)
is also investigated; Section [4](https://arxiv.org/html/2512.21621v1#S4 "4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") presents several illustrative numerical examples;
and Section [5](https://arxiv.org/html/2512.21621v1#S5 "5 Concluding remarks ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") gives concluding remarks.

## 2 Single population with relative performance concerns

### 2.1 The setup and notation

We adopt essentially the same setup and notation used in Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)].
(Ω0,ℱ0,(ℱtn0)n=1N,ℙ0)(\Omega^{0},{\cal F}^{0},({\cal F}^{0}\_{t\_{n}})\_{n=1}^{N},\mathbb{P}^{0}) is a complete filtered probability space, where
0=t0<t1<…<tN=T0=t\_{0}<t\_{1}<\ldots<t\_{N}=T is an equally spaced time sequence using a time step Δ:=T/N\Delta:=T/N where T<∞T<\infty
and N∈ℕN\in\mathbb{N} are given constants. This space is used to model the common shocks to every agent.
Specifically, the filtration (ℱtn0)n=0N({\cal F}\_{t\_{n}}^{0})\_{n=0}^{N} is generated by two stochastic processes: a strictly positive
process (Sn:=S​(tn))n=0N(S\_{n}:=S(t\_{n}))\_{n=0}^{N} and a dYd\_{Y}-dimensional
process (Yn:=Y​(tn))n=0N(Y\_{n}:=Y(t\_{n}))\_{n=0}^{N}, i.e., ℱtn0:=σ​{Sk,Yk;0≤k≤n}{\cal F}\_{t\_{n}}^{0}:=\sigma\{S\_{k},Y\_{k};0\leq k\leq n\}.
We use the process S:=(Sn)n=0NS:=(S\_{n})\_{n=0}^{N} to represent a risky stock price process and Y:=(Yn)n=0NY:=(Y\_{n})\_{n=0}^{N}
standalone non-tradable macroeconomic and/or environmental
factors that affect all the agents. We set S0>0S\_{0}>0 and Y0∈ℝdYY\_{0}\in\mathbb{R}^{d\_{Y}} as given constants and thus ℱ00{\cal F}\_{0}^{0} is trivial.
For each n=1,…,Nn=1,\ldots,N, we assume that the ℱtn0{\cal F}\_{t\_{n}}^{0}-measurable random variable

|  |  |  |
| --- | --- | --- |
|  | R~n:=Sn/Sn−1\widetilde{R}\_{n}:=S\_{n}/S\_{n-1} |  |

takes only the two possible values, either u~\widetilde{u} or d~\widetilde{d}. In other words, we restrict
the trajectories of (Sn)n=0N(S\_{n})\_{n=0}^{N} onto a recombining binomial tree.
The set of all possible values taken by SnS\_{n} is thus given by 𝒮n:={S0​u~k​d~n−k,0≤k≤n}{\cal S}\_{n}:=\{S\_{0}\widetilde{u}^{k}\widetilde{d}^{n-k},0\leq k\leq n\},
which is a finite subset of (0,∞)(0,\infty). We denote by 𝒮n:={(sk)k=0n∈ℝn+1:ℙ0​(Sk=sk,0≤k≤n)>0}{\cal S}^{n}:=\{(s\_{k})\_{k=0}^{n}\in\mathbb{R}^{n+1}:\mathbb{P}^{0}(S\_{k}=s\_{k},0\leq k\leq n)>0\} the set of all values taken by the stock price trajectory (Sk)k=0n(S\_{k})\_{k=0}^{n}.
To avoid technical subtleties with conditional probabilities, we also assume that the process YY
takes values in a finite set at every tnt\_{n}. We use 𝒴n:={y∈ℝdY:ℙ0​(Yn=y)>0}{\cal Y}\_{n}:=\{y\in\mathbb{R}^{d\_{Y}}:\mathbb{P}^{0}(Y\_{n}=y)>0\}
and 𝒴n:={(yk)k=0n∈ℝdY​(n+1):ℙ0​(Yk=yk,0≤k≤n)>0}{\cal Y}^{n}:=\{(y\_{k})\_{k=0}^{n}\in\mathbb{R}^{d\_{Y}(n+1)}:\mathbb{P}^{0}(Y\_{k}=y\_{k},0\leq k\leq n)>0\} to denote the set of
all values taken by YnY\_{n} and (Yk)k=0n(Y\_{k})\_{k=0}^{n}, respectively.

In addition to the above space, we introduce a countably infinite number of complete filtered
probability spaces (Ωi,ℱi,(ℱtni)n=0N,ℙi)(\Omega^{i},{\cal F}^{i},({\cal F}^{i}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{i}), i∈ℕi\in\mathbb{N},
which are used to model idiosyncratic shocks to each agent-ii, i=1,2,…i=1,2,\ldots.
For each ii, (Ωi,ℱi,(ℱtni)n=0N,ℙi)(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}) is endowed with
ℱ0i{\cal F}\_{0}^{i}-measurable random variables (ξi,γi,θi)(\xi\_{i},\gamma\_{i},\theta\_{i}) as well as an (ℱtni)n=0N({\cal F}^{i}\_{t\_{n}})\_{n=0}^{N}-adapted
stochastic process Zi:=(Zni:=Zi​(tn))n=0NZ^{i}:=(Z\_{n}^{i}:=Z^{i}(t\_{n}))\_{n=0}^{N}. Here, ξi,γi\xi\_{i},\gamma\_{i} and θi\theta\_{i}
are all ℝ\mathbb{R}-valued. ξi\xi\_{i} represents the initial wealth, γi\gamma\_{i}
the coefficient of absolute risk aversion, and θi\theta\_{i} denotes the strength of the relative performance
concern of agent-ii, respectively. The dZd\_{Z}-dimensional process ZiZ^{i} is used to model
idiosyncratic shocks to agent-ii. We denote the range of random variable ZniZ\_{n}^{i} by 𝒵n{\cal Z}\_{n}.
The fact that (ξi,γi,θi)(\xi\_{i},\gamma\_{i},\theta\_{i}) are ℱ0i{\cal F}\_{0}^{i}-measurable means that agent-ii knows
their initial wealth, the size of risk aversion, and the strength of the relative
performance concern at time zero. Note that there is no need to impose
the restriction of a finite state space on variables other than (S,Y)(S,Y).

By the standard procedures (see, for example, Klenke [[38](https://arxiv.org/html/2512.21621v1#bib.bib38), Chapter 14]), the complete filtered probability space
(Ω,ℱ,(ℱtn)n=0N,ℙ)(\Omega,{\cal F},({\cal F}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}) is defined as the product of all the above spaces

|  |  |  |
| --- | --- | --- |
|  | (Ω,ℱ,(ℱtn)n=0N,ℙ):=(Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)⊗i=1∞(Ωi,ℱi,(ℱtni)n=0N,ℙi)(\Omega,{\cal F},({\cal F}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}):=(\Omega^{0},{\cal F}^{0},({\cal F}\_{t\_{n}}^{0})\_{n=0}^{N},\mathbb{P}^{0})\otimes\_{i=1}^{\infty}(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}) |  |

which denotes the full probability space containing the entire environment of our model.
Therefore, by construction, (S,Y)(S,Y) and (ξi,γi,Zi),i∈ℕ(\xi\_{i},\gamma\_{i},Z^{i}),~i\in\mathbb{N} are mutually independent.
On the other hand, the relevant probability space for each agent-ii is the product probability space defined by

|  |  |  |
| --- | --- | --- |
|  | (Ω0,i,ℱ0,i,(ℱtn0,i)n=0N,ℙ0,i):=(Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)⊗(Ωi,ℱi,(ℱtni)n=0N,ℙi),(\Omega^{0,i},{\cal F}^{0,i},({\cal F}\_{t\_{n}}^{0,i})\_{n=0}^{N},\mathbb{P}^{0,i}):=(\Omega^{0},{\cal F}^{0},({\cal F}\_{t\_{n}}^{0})\_{n=0}^{N},\mathbb{P}^{0})\otimes(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}), |  |

which reflects our assumption that common shocks are public knowledge, but the idiosyncratic shocks are private to
each agent. We shall use the same symbols, such as (Sn,Yn,γi,⋯)(S\_{n},Y\_{n},\gamma\_{i},\cdots), if they are
defined as trivial extensions on larger product probability spaces.
Expectations with respect to ℙ0\mathbb{P}^{0}, ℙi\mathbb{P}^{i}, ℙ0,i\mathbb{P}^{0,i} and ℙ\mathbb{P} are denoted by 𝔼0​[⋅]\mathbb{E}^{0}[\cdot], 𝔼i​[⋅]\mathbb{E}^{i}[\cdot],
𝔼0,i​[⋅]\mathbb{E}^{0,i}[\cdot] and 𝔼​[⋅]\mathbb{E}[\cdot], respectively.

We introduce the symbols 𝐒n:=(S0,S1,…,Sn){\bf{S}}^{n}:=(S\_{0},S\_{1},\ldots,S\_{n})
to denote a stock-price trajectory and 𝐘n:=(Y0,Y1,…,Yn){\bf{Y}}^{n}:=(Y\_{0},Y\_{1},\ldots,Y\_{n}) as a common-noise trajectory,
𝐬n:=(s0,s1,…,sn)∈𝒮n{\bf{s}}^{n}:=(s\_{0},s\_{1},\ldots,s\_{n})\in{\cal S}^{n} and 𝐲n:=(y0,y1,…,yn)∈𝒴n{\bf{y}}^{n}:=(y\_{0},y\_{1},\ldots,y\_{n})\in{\cal Y}^{n} serve as their specific realizations.
For 𝐬∈𝒮n−1{\bf{s}}\in{\cal S}^{n-1}, we use the symbols (𝐬​u~)n:=(𝐬n−1,sn−1​u~)∈𝒮n({\bf{s}}\widetilde{u})^{n}:=({\bf{s}}^{n-1},s\_{n-1}\widetilde{u})\in{\cal S}^{n}
and (𝐬​d~)n:=(𝐬n−1,sn−1​d~)∈𝒮n({\bf{s}}\widetilde{d})^{n}:=({\bf{s}}^{n-1},s\_{n-1}\widetilde{d})\in{\cal S}^{n}. Moreover, for 𝐲=(y0,…,yn)∈𝒴n{\bf{y}}=(y\_{0},\ldots,y\_{n})\in{\cal Y}^{n},
(y0,…,yn−1)(y\_{0},\ldots,y\_{n-1}) is denoted by 𝐲−{\bf{y}}^{-}. For 𝐬∈𝒮n{\bf{s}}\in{\cal S}^{n}, we denote its kk-th element by sks\_{k}
and similarly yky\_{k} for 𝐲∈𝒴n{\bf{y}}\in{\cal Y}^{n}.
We also introduce an ℱ0i{\cal F}^{i}\_{0}-measurable 22-tuple
ϱi:=(γi,θi)\varrho\_{i}:=(\gamma\_{i},\theta\_{i}) for notational simplicity.
To lighten the notational burden, we shall use expressions such as
𝔼0,i[⋅|𝐬,𝐲,zi,ϱi]\mathbb{E}^{0,i}[\cdot|{\bf{s}},{\bf{y}},z^{i},\varrho\_{i}] for (𝐬,𝐲,zi)∈𝒮n−1×𝒴n−1×𝒵n−1({\bf{s}},{\bf{y}},z^{i})\in{\cal S}^{n-1}\times{\cal Y}^{n-1}\times{\cal Z}\_{n-1},
to denote the conditional expectation 𝔼0,i[⋅|𝐒n−1=𝐬,𝐘n−1=𝐲,Zn−1i=zi,ϱi=ϱi]\mathbb{E}^{0,i}[\cdot|{\bf{S}}^{n-1}={\bf{s}},{\bf{Y}}^{n-1}={\bf{y}},Z\_{n-1}^{i}=z^{i},\varrho\_{i}=\varrho\_{i}]. With a slight abuse of notation, we shall use the same symbols for the
realizations of the ℱ0i{\cal F}^{i}\_{0}-measurable random variables (e.g., ϱi\varrho\_{i}).

We assume that the risk-free (nominal) interest rate is given by a constant r≥0r\geq 0.
The time-tnt\_{n} value of the money-market account is thus given by exp⁡(r​n​Δ)\exp(rn\Delta).
To make the notation simple, we introduce the constants

|  |  |  |
| --- | --- | --- |
|  | u:=u~−exp⁡(r​Δ),d:=d~−exp⁡(r​Δ),u:=\widetilde{u}-\exp(r\Delta),\quad d:=\widetilde{d}-\exp(r\Delta), |  |

and an ℱtn0{\cal F}^{0}\_{t\_{n}}-measurable random variable, which takes values either uu or dd,

|  |  |  |
| --- | --- | --- |
|  | Rn:=R~n−exp⁡(r​Δ),R\_{n}:=\widetilde{R}\_{n}-\exp(r\Delta), |  |

for each 1≤n≤N1\leq n\leq N.
We also use the symbol β:=exp⁡(r​Δ)\beta:=\exp(r\Delta). For notational simplicity, we also introduce the ℱ0i{\cal F}^{i}\_{0}-measurable process (γni)n=0N(\gamma\_{n}^{i})\_{n=0}^{N}
defined by γni:=(βN/βn)​γi\gamma\_{n}^{i}:=(\beta^{N}/\beta^{n})\gamma\_{i}.

For the above introduced variables and processes, we assume the following:

###### Assumption 2.1.

(i): u~\widetilde{u} and d~\widetilde{d} are real constants satisfying 0<d~<exp⁡(r​Δ)<u~<∞0<\widetilde{d}<\exp(r\Delta)<\widetilde{u}<\infty.
  
(ii): The variables (ξi,γi,θi,Zi)(\xi\_{i},\gamma\_{i},\theta\_{i},Z^{i}) are identically distributed across all the agents i=1,2,…i=1,2,\ldots.
  
(iii): There exist real constants ξ¯,ξ¯\underline{\xi},\overline{\xi}, γ¯,γ¯\underline{\gamma},\overline{\gamma}, and θ¯,θ¯\underline{\theta},\overline{\theta} so that
for every i∈ℕi\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | ξi∈[ξ¯,ξ¯]⊂ℝ,ϱi:=(γi,θi)∈Γ:=[γ¯,γ¯]×[θ¯,θ¯]⊂(0,∞)×ℝ.\xi\_{i}\in[\underline{\xi},\overline{\xi}]\subset\mathbb{R},\quad\varrho\_{i}:=(\gamma\_{i},\theta\_{i})\in\Gamma:=[\underline{\gamma},\overline{\gamma}]\times[\underline{\theta},\overline{\theta}]\subset(0,\infty)\times\mathbb{R}. |  |

(iv): For each ii, the process ZiZ^{i} is Markovian, i.e., 𝔼i​[f​(Zni)|ℱtki]=𝔼i​[f​(Zni)|Zki]\mathbb{E}^{i}[f(Z\_{n}^{i})|{\cal F}^{i}\_{t\_{k}}]=\mathbb{E}^{i}[f(Z\_{n}^{i})|Z\_{k}^{i}] for every
bounded measurable function ff on 𝒵n{\cal Z}\_{n} and k≤nk\leq n.
  
(v): The process YY is Markovian, i.e., 𝔼0​[f​(Yn)|ℱtk0]=𝔼0​[f​(Yn)|Yk]\mathbb{E}^{0}[f(Y\_{n})|{\cal F}^{0}\_{t\_{k}}]=\mathbb{E}^{0}[f(Y\_{n})|Y\_{k}] for every bounded measurable
function ff on 𝒴n{\cal Y}\_{n} and k≤nk\leq n.
  
(vi): The transition probabilities of S=(Sn)n=0NS=(S\_{n})\_{n=0}^{N} satisfy, for every 0≤n≤N−10\leq n\leq N-1, a.s.,

|  |  |  |
| --- | --- | --- |
|  | ℙ0(Sn+1=u~Sn|ℱtn0)=ℙ0(Sn+1=u~Sn|Sn,Yn)=:pn(Sn,Yn),ℙ0(Sn+1=d~Sn|ℱtn0)=ℙ0(Sn+1=d~Sn|Sn,Yn)=:qn(Sn,Yn),\begin{split}&\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|{\cal F}\_{t\_{n}}^{0})=\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|S\_{n},Y\_{n})=:p\_{n}(S\_{n},Y\_{n}),\\ &\mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|{\cal F}\_{t\_{n}}^{0})=\mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|S\_{n},Y\_{n})=:q\_{n}(S\_{n},Y\_{n}),\end{split} |  |

where pn,qn(:=1−pn):𝒮n×𝒴n→ℝ,0≤n≤N−1p\_{n},q\_{n}~(:=1-p\_{n}):{\cal S}\_{n}\times{\cal Y}\_{n}\rightarrow\mathbb{R},0\leq n\leq N-1 are bounded measurable functions
satisfying

|  |  |  |
| --- | --- | --- |
|  | 0<pn​(s,y),qn​(s,y)<10<p\_{n}(s,y),q\_{n}(s,y)<1 |  |

for every (s,y)∈𝒮n×𝒴n(s,y)\in{\cal S}\_{n}\times{\cal Y}\_{n}.

We now provide remarks on the assumptions. By (i), we have d<0<ud<0<u.
It is well-known that the transition probabilities under the risk-neutral measure ℚ\mathbb{Q}
are given by pℚ:=(exp⁡(r​Δ)−d~)/(u~−d~)=(−d)/(u−d)p^{\mathbb{Q}}:=(\exp(r\Delta)-\widetilde{d})/(\widetilde{u}-\widetilde{d})=(-d)/(u-d) for the up-move and
qℚ:=1−pℚq^{\mathbb{Q}}:=1-p^{\mathbb{Q}} for the down-move of the stock price. In this paper, we fix the relative transition size (u~,d~)(\widetilde{u},\widetilde{d})
to be constant across all nodes; however, this is done merely for simplicity.
The analysis of the paper still holds even if (u~,d~)(\widetilde{u},\widetilde{d}) varies from node to node.
It is known that, by adjusting (u~,d~)(\widetilde{u},\widetilde{d}) node by node according to the result by Derman & Kani [[8](https://arxiv.org/html/2512.21621v1#bib.bib8)],
we can reproduce the implied volatility surface in the option market, while keeping the recombining property of
the binomial tree intact. Therefore, if necessary, our discussion below can be constructed
on a binomial tree whose risk-neutral distribution is consistent with the option market.
The Markovian assumptions of (iv) and (v) can be imposed without loss of generality
by lifting YY and ZiZ^{i} to higher dimensional processes.
The generalization to the path-dependent transition probabilities, such as pn−1​(𝐒n,Yn)p\_{n-1}({\bf{S}}^{n},Y\_{n}),
will be discussed in later sections.
Under the above conditions (v) and (vi), (Sn+1,Yn+1)(S\_{n+1},Y\_{n+1}) satisfy the property:

|  |  |  |
| --- | --- | --- |
|  | 𝔼0[f(Sn+1)g(Yn+1)|ℱtn0]=𝔼0[f(Sn+1)|Sn,Yn]𝔼0[g(Yn+1)|Yn]a.s.,0≤n≤N−1,\mathbb{E}^{0}[f(S\_{n+1})g(Y\_{n+1})|{\cal F}\_{t\_{n}}^{0}]=\mathbb{E}^{0}[f(S\_{n+1})|S\_{n},Y\_{n}]\mathbb{E}^{0}[g(Y\_{n+1})|Y\_{n}]~{\rm a.s.,}\quad 0\leq n\leq N-1, |  |

for any bounded measurable functions f:𝒮n+1→ℝf:{\cal S}\_{n+1}\rightarrow\mathbb{R} and g:𝒴n+1→ℝg:{\cal Y}\_{n+1}\rightarrow\mathbb{R}.
The process YY can be interpreted as representing some standalone macroeconomic and/or environmental factors
which are not influenced by the agents’ trading activities. In regime switching models, YY can be used to
model the state process of the regimes.

###### Remark 2.1.

The bound for the transition probabilities (vi) guarantees that the probability measures
ℙ0∘S−1\mathbb{P}^{0}\circ S^{-1} and ℚ∘S−1\mathbb{Q}\circ S^{-1} are equivalent. Hence the system is arbitrage free.

### 2.2 Optimization problem

Consider a financial market which consists of a large number of agents, agent-ii, 1≤i≤Np1\leq i\leq N\_{p}.
We suppose that the preference of each agent-ii is characterized
by the exponential utility at the terminal time t=tNt=t\_{N} with the absolute risk-aversion coefficient γi\gamma\_{i}:

|  |  |  |
| --- | --- | --- |
|  | −exp⁡(−γi​(XNi−θiNp−1​∑j≠iXNj−F​(SN,YN,ZNi))).-\exp\Bigl(-\gamma\_{i}\Bigl(X\_{N}^{i}-\frac{\theta\_{i}}{N\_{p}-1}\sum\_{j\neq i}X\_{N}^{j}-F(S\_{N},Y\_{N},Z\_{N}^{i})\Bigr)\Bigr). |  |

Here, Xi:=(Xni:=Xi​(tn))n=0NX^{i}:=(X\_{n}^{i}:=X^{i}(t\_{n}))\_{n=0}^{N} is the wealth process of agent-ii, and the term FF denotes
a stochastic terminal liability which depends on the realizations of the stock price SNS\_{N}, the
non-tradable macroeconomic factors YNY\_{N}, as well as the idiosyncratic factors ZNiZ^{i}\_{N}.
A key extension relative to the previous work Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)] is the presence of the relative performance concern
represented by the second term. The coefficient θi\theta\_{i} gives its strength and direction;
θi>0\theta\_{i}>0 denotes a situation with the relative performance competition, and θi<0\theta\_{i}<0
corresponds to altruistic preferences (or homophilous interaction as termed by Hu & Zariphopoulou [[29](https://arxiv.org/html/2512.21621v1#bib.bib29)]),
where agents derive positive utility from the wealth of others.
In this section, we are interested in the mean-field limit Np→∞N\_{p}\rightarrow\infty of the above problem.

We now formulate the optimization problem for each agent. Agent-ii, for i=1,2,…i=1,2,\ldots, with an initial wealth ξi\xi\_{i},
engages in self-financing trading with the risk-free money market account and a single risky stock.
They adopt an (ℱtn0,i)n=0N−1({\cal F}^{0,i}\_{t\_{n}})\_{n=0}^{N-1}-adapted trading strategy (ϕni)n=0N−1(\phi\_{n}^{i})\_{n=0}^{N-1},
denoting the invested amount of cash in the stock at time tnt\_{n}.
The associated wealth process of agent-ii, Xi:=(Xni:=Xi​(tn))n=0NX^{i}:=(X\_{n}^{i}:=X^{i}(t\_{n}))\_{n=0}^{N}, follows the dynamics

|  |  |  |
| --- | --- | --- |
|  | Xn+1i=exp⁡(r​Δ)​(Xni−ϕni)+ϕni​R~n+1=β​Xni+ϕni​Rn+1,\begin{split}X\_{n+1}^{i}&=\exp(r\Delta)(X\_{n}^{i}-\phi^{i}\_{n})+\phi^{i}\_{n}\widetilde{R}\_{n+1}\\ &=\beta X\_{n}^{i}+\phi^{i}\_{n}R\_{n+1},\end{split} |  |

where X0i=ξiX\_{0}^{i}=\xi\_{i}. Recall that β:=exp⁡(r​Δ)\beta:=\exp(r\Delta) and Rn+1:=R~n+1−exp⁡(r​Δ)R\_{n+1}:=\widetilde{R}\_{n+1}-\exp(r\Delta).

Each agent-ii seeks to solve the optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(ϕni)n=0N−1∈𝔸i𝔼0,i[−exp(−γi(XNi−θiμN(𝐒N,𝐘N−1)−F(SN,YN,ZNi))|ℱ00,i],\sup\_{(\phi^{i}\_{n})\_{n=0}^{N-1}\in\mathbb{A}^{i}}\mathbb{E}^{0,i}\Bigl[-\exp\Bigl(-\gamma\_{i}\bigl(X\_{N}^{i}-\theta\_{i}\mu\_{N}({\bf{S}}^{N},{\bf{Y}}^{N-1})-F(S\_{N},Y\_{N},Z\_{N}^{i})\Bigr)|{\cal F}\_{0}^{0,i}\Bigr], |  | ( 2.1) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝔸i:={(ϕni)n=0N−1:ϕni is an ℱtn0,i-measurable real-valued random variable}\mathbb{A}^{i}:=\{(\phi^{i}\_{n})\_{n=0}^{N-1}:\text{$\phi^{i}\_{n}$ is an ${\cal F}^{0,i}\_{t\_{n}}$-measurable real-valued random variable}\} |  |

denotes the admissible control space. μN:𝒮N×𝒴N−1→ℝ\mu\_{N}:{\cal S}^{N}\times{\cal Y}^{N-1}\rightarrow\mathbb{R}
is an appropriate measurable function. We shall search for the fixed point (μn)n=0N(\mu\_{n})\_{n=0}^{N} with μ0:=𝔼i​[ξi]\mu\_{0}:=\mathbb{E}^{i}[\xi\_{i}]
and μn:𝒮n×𝒴n−1→ℝ\mu\_{n}:{\cal S}^{n}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N, such that

|  |  |  |
| --- | --- | --- |
|  | μn​(𝐒n,𝐘n−1)=𝔼0,i​[Xni|ℱtn0]​a.s..\mu\_{n}({\bf{S}}^{n},{\bf{Y}}^{n-1})=\mathbb{E}^{0,i}\bigl[X\_{n}^{i}|{\cal F}^{0}\_{t\_{n}}\bigr]~{\rm a.s..} |  |

The independence of μn\mu\_{n} from YnY\_{n} follows from the dynamics of wealth XiX^{i} and the
condition (vi) in Assumption [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

###### Remark 2.2 (Economic interpretation of the agents).

Throughout this paper, we interpret the agents not as individual investors,
but as trading desks of institutional market participants, encompassing both financial
intermediaries (e.g., dealer banks, market makers) and active asset managers (e.g., hedge funds, insurance firms).
In this context, the terminal liability FF represents inventory risk, derivatives obligations, or specific investment
mandates arising from client orders and insurance contracts, which are not under the direct control of the trading desks.
In fact, these institutions are often structurally obligated to manage these risks to maintain client relationships or
fulfill business duties. The fee income or premiums received from clients for these services are also non-tradable
and inherent to the business; they are thus embedded in FF as a negative contribution to the liability.
This interpretation naturally justifies the presence of liabilities and sophisticated optimization,
as well as the introduction of relative performance concerns driven by the highly competitive nature of the financial industry.

###### Assumption 2.2.

(i): F:𝒮N×𝒴N×𝒵N→ℝF:{\cal S}\_{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}\rightarrow\mathbb{R} is a bounded measurable function.
  
(ii): Every agent is a price-taker in the sense that they consider the stock price process
(and hence its transition probabilities specified in Assumption [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (vi)) to be
exogenously determined by the collective actions of the others and unaffected by the agent’s own trading strategies.
  
(iii): Every agent treats the mean-field terms (μn)n=0N(\mu\_{n})\_{n=0}^{N}, μn:𝒮n×𝒴n−1→ℝ\mu\_{n}:{\cal S}^{n}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, as
exogenous bounded measurable functions, believing they are determined by the collective actions of the others and
unaffected by the agent’s own trading strategies.
333Since the domain 𝒮N×𝒴N−1{\cal S}^{N}\times{\cal Y}^{N-1} is finite, the boundedness assumption is redundant.
However, we make it explicit for clarity. We keep this convention throughout the paper.

As a preliminary step, we first study, for 1≤n≤N1\leq n\leq N, the one-period problem at t=tn−1t=t\_{n-1} for the interval [tn−1,tn][t\_{n-1},t\_{n}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supϕn−1i𝔼0,i​[−exp⁡(−γni​(Xni−θi​μn​(𝐒n,𝐘n−1)))​Vn​(Sn,Yn,Zni,ϱi)|ℱtn−10,i]\sup\_{\phi^{i}\_{n-1}}\mathbb{E}^{0,i}\Bigl[-\exp\Bigl(-\gamma\_{n}^{i}\bigl(X\_{n}^{i}-\theta\_{i}\mu\_{n}({\bf{S}}^{n},{\bf{Y}}^{n-1})\bigr)\Bigr)V\_{n}(S\_{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})|{\cal F}\_{t\_{n-1}}^{0,i}\Bigr] |  | ( 2.2) |

where the supremum is taken over the ℱtn−10,i{\cal F}^{0,i}\_{t\_{n-1}}-measurable real-valued random variables. We recall that γni\gamma\_{n}^{i} is defined as
γni:=(βN/βn)​γi\gamma\_{n}^{i}:=(\beta^{N}/\beta^{n})\gamma\_{i} and ϱi\varrho\_{i} is the 2-tuple ϱi:=(γi,θi)\varrho\_{i}:=(\gamma\_{i},\theta\_{i}).

###### Lemma 2.1.

Let Assumption [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and Assumption [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (ii) and (iii) be in force.
Assume, moreover, that Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}\_{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R} is a measurable function
satisfying the uniform bounds 0<cn≤Vn≤Cn<∞0<c\_{n}\leq V\_{n}\leq C\_{n}<\infty on its domain with some positive constants cnc\_{n} and CnC\_{n}.
Then the problem ([2.2](https://arxiv.org/html/2512.21621v1#S2.E2 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single-tmp}) has a unique optimal solution ϕn−1i,∗\phi^{i,\*}\_{n-1}
defined by a bounded measurable function ϕn−1i,∗:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝ\phi^{i,\*}\_{n-1}:{\cal S}^{n-1}\times{\cal Y}^{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R},
such that ϕn−1i,∗:=ϕn−1i,∗​(𝐒n−1,𝐘n−1,Zn−1i,ϱi)\phi\_{n-1}^{i,\*}:=\phi^{i,\*}\_{n-1}({\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i},\varrho\_{i}) a.s., where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1i,∗​(𝐬,𝐲,zi,ϱi):=θi​Δn​(𝐬,𝐲)u−d+1γni​(u−d)​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)+log⁡fn−1​(s,y,zi,ϱi)}.\begin{split}&\phi^{i,\*}\_{n-1}({\bf{s}},{\bf{y}},z^{i},\varrho\_{i}):=\frac{\theta\_{i}\Delta\_{n}({\bf{s}},{\bf{y}})}{u-d}+\frac{1}{\gamma\_{n}^{i}(u-d)}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)+\log f\_{n-1}(s,y,z^{i},\varrho\_{i})\Bigr\}.\end{split} |  | ( 2.3) |

Here, s=sn−1∈𝒮n−1s=s\_{n-1}\in{\cal S}\_{n-1} and y=yn−1∈𝒴n−1y=y\_{n-1}\in{\cal Y}\_{n-1} are the last elements of 𝐬∈𝒮n−1{\bf{s}}\in{\cal S}^{n-1} and 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1},
respectively. Furthermore, fn−1:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝf\_{n-1}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}
is a measurable function satisfying the uniform bounds 0<c¯n≤fn−1≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}\leq\overline{C}\_{n}<\infty on its domain
with some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n},
and Δn:𝒮n−1×𝒴n−1→ℝ\Delta\_{n}:{\cal S}^{n-1}\times{\cal Y}^{n-1}\rightarrow\mathbb{R} is a bounded measurable function.
They are defined respectively by

|  |  |  |
| --- | --- | --- |
|  | fn−1​(s,y,zi,ϱi):=𝔼0,i​[Vn​(s​u~,Yn,Zni,ϱi)|y,zi,ϱi]𝔼0,i​[Vn​(s​d~,Yn,Zni,ϱi)|y,zi,ϱi],Δn​(𝐬,𝐲):=μn​((𝐬​u~)n,𝐲)−μn​((𝐬​d~)n,𝐲).\begin{split}&f\_{n-1}(s,y,z^{i},\varrho\_{i}):=\frac{\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]}{\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]},\\ &\Delta\_{n}({\bf{s}},{\bf{y}}):=\mu\_{n}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})-\mu\_{n}(({\bf{s}}\widetilde{d})^{n},{\bf{y}}).\end{split} |  |

###### Proof.

We solve the problem on each set {ω0,i∈Ω0,i:(Xn−1i,𝐒n−1,𝐘n−1,Zn−1i,ϱi)=(xi,𝐬,𝐲,zi,ϱi)}\{\omega^{0,i}\in\Omega^{0,i}:(X\_{n-1}^{i},{\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i},\varrho\_{i})=(x^{i},{\bf{s}},{\bf{y}},z^{i},\varrho\_{i})\}.
Here, with a slight abuse of notation, we use the same symbols for the realizations of ℱ0i{\cal F}^{i}\_{0}-measurable random variables.
Recall that s:=sn−1s:=s\_{n-1} and y:=yn−1y:=y\_{n-1}, i.e., the last elements of 𝐬∈𝒮n−1{\bf{s}}\in{\cal S}^{n-1} and 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1}, respectively.
Then the problem ([2.2](https://arxiv.org/html/2512.21621v1#S2.E2 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single-tmp}) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | infϕi∈ℝ𝔼0,i​[exp⁡(−γni​(β​xi+ϕi​Rn−θi​μn​(𝐒n,𝐘n−1)))​Vn​(Sn,Yn,Zni,ϱi)|𝐬,𝐲,zi,ϱi]=exp(−γn−1ixi)infϕi{pn−1(s,y)exp(−γni(ϕiu−θiμn((𝐬u~)n,𝐲)))𝔼0,i[Vn(su~,Yn,Zni,ϱi)|y,zi,ϱi]+qn−1(s,y)exp(−γni(ϕid−θiμn((𝐬d~)n,𝐲)))𝔼0,i[Vn(sd~,Yn,Zni,ϱi)|y,zi,ϱi]},\begin{split}&\inf\_{\phi^{i}\in\mathbb{R}}\mathbb{E}^{0,i}\Bigl[\exp\Bigl(-\gamma\_{n}^{i}\bigl(\beta x^{i}+\phi^{i}R\_{n}-\theta\_{i}\mu\_{n}({\bf{S}}^{n},{\bf{Y}}^{n-1})\bigr)\Bigr)V\_{n}(S\_{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})|{\bf{s}},{\bf{y}},z^{i},\varrho\_{i}\Bigr]\\ &=\exp(-\gamma\_{n-1}^{i}x^{i})\inf\_{\phi^{i}}\Bigl\{p\_{n-1}(s,y)\exp\Bigl(-\gamma\_{n}^{i}\bigl(\phi^{i}u-\theta\_{i}\mu\_{n}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]\\ &\qquad\qquad+q\_{n-1}(s,y)\exp\Bigl(-\gamma\_{n}^{i}\bigl(\phi^{i}d-\theta\_{i}\mu\_{n}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]\Bigr\},\end{split} |  | ( 2.4) |

where we have used the property (vi) in Assumption [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). Since γni>0\gamma\_{n}^{i}>0 and d<0<ud<0<u, it is easy to see
that the optimal trade position ϕi,∗\phi^{i,\*} is uniquely characterized by

|  |  |  |
| --- | --- | --- |
|  | pn−1​(s,y)​u​exp⁡(−γni​(ϕi,∗​u−θi​μn​((𝐬​u~)n,𝐲)))​𝔼0,i​[Vn​(s​u~,Yn,Zni,ϱi)|y,zi,ϱi]+qn−1​(s,y)​d​exp⁡(−γni​(ϕi,∗​d−θi​μn​((𝐬​d~)n,𝐲)))​𝔼0,i​[Vn​(s​d~,Yn,Zni,ϱi)|y,zi,ϱi]=0,\begin{split}&p\_{n-1}(s,y)u\exp\Bigl(-\gamma\_{n}^{i}\bigl(\phi^{i,\*}u-\theta\_{i}\mu\_{n}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]\\ &\quad+q\_{n-1}(s,y)d\exp\Bigl(-\gamma\_{n}^{i}\bigl(\phi^{i,\*}d-\theta\_{i}\mu\_{n}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]=0,\end{split} |  |

which gives the desired result. The existence of positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n} for fn−1f\_{n-1} follows
immediately from the boundedness of VnV\_{n}.
∎

### 2.3 Relative performance mean-field equilibrium

###### Definition 2.1.

We sat that the system is in the relative performance mean-field equilibrium (RP-MFE)
if the problem ([2.1](https://arxiv.org/html/2512.21621v1#S2.E1 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single}) has an optimal solution (ϕn−1i,∗)n=1N,i=1,2,…(\phi^{i,\*}\_{n-1})\_{n=1}^{N},i=1,2,\ldots,
for the agents satisfying Assumption [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (ii) and (iii),
such that,
with μ0:=𝔼i​[ξi]\mu\_{0}:=\mathbb{E}^{i}[\xi\_{i}], the bounded measurable functions μn:𝒮n×𝒴n−1→ℝ\mu\_{n}:{\cal S}^{n}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N satisfy
the fixed point condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn(𝐒n,𝐘n−1)=𝔼0,i[Xni,∗|ℱtn0]a.s.,1≤n≤N,\mu\_{n}({\bf{S}}^{n},{\bf{Y}}^{n-1})=\mathbb{E}^{0,i}\bigl[X\_{n}^{i,\*}|{\cal F}^{0}\_{t\_{n}}\bigr]~{\rm a.s.,}\quad 1\leq n\leq N, |  | ( 2.5) |

where Xi,∗X^{i,\*} denotes the wealth process associated with the optimal control ϕi,∗\phi^{i,\*}.
Moreover, we denote the associated processes in the RP-MFE by (μ^,ϕ^i)(\widehat{\mu},\widehat{\phi}^{i}),
and refer to them as the solution pair of the RP-MFE. We also use the symbol X^i\widehat{X}^{i} for i=1,2,…i=1,2,\ldots
to represent the wealth process of agent-ii associated with ϕ^i\widehat{\phi}^{i} and the initial condition ξi\xi\_{i}.

Since we are dealing with a symmetric problem with i.i.d.​ variables and processes (ξi,γi,θi,Zi)i≥1(\xi\_{i},\gamma\_{i},\theta\_{i},Z^{i})\_{i\geq 1}, the choice
of the representative agent is arbitrary.
Since the filtration (ℱtk0)k=0N({\cal F}^{0}\_{t\_{k}})\_{k=0}^{N} is generated by (S,Y)(S,Y), the fixed-point condition ([2.5](https://arxiv.org/html/2512.21621v1#S2.E5 "In Definition 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-single-mu})
can be equivalently represented by using agent-11 as the representative:

|  |  |  |
| --- | --- | --- |
|  | μn​(𝐬,𝐲−)=𝔼1​[Xn1,∗|𝐬,𝐲]=𝔼1​[Xn1,∗|𝐬,𝐲−],\mu\_{n}({\bf{s}},{\bf{y}}^{-})=\mathbb{E}^{1}\bigl[X\_{n}^{1,\*}|{\bf{s}},{\bf{y}}\bigr]=\mathbb{E}^{1}\bigl[X\_{n}^{1,\*}|{\bf{s}},{\bf{y}}^{-}\bigr], |  |

for every (𝐬,𝐲−)∈𝒮n×𝒴n−1({\bf{s}},{\bf{y}}^{-})\in{\cal S}^{n}\times{\cal Y}^{n-1}. Here, 𝐲=(𝐲−,yn)∈𝒴n{\bf{y}}=({\bf{y}}^{-},y\_{n})\in{\cal Y}^{n}.
In the following, we prove the existence and uniqueness of the RP-MFE. We will show that the path-dependence
of ϕn−1i,∗\phi^{i,\*}\_{n-1} on (𝐬,𝐲)∈𝒮n−1×𝒴n−1({\bf{s}},{\bf{y}})\in{\cal S}^{n-1}\times{\cal Y}^{n-1} reduces to dependence on the current state
(s,y)=(sn−1,yn−1)∈𝒮n−1×𝒴n−1(s,y)=(s\_{n-1},y\_{n-1})\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1} in the RP-MFE.
It is well known that the RP-MFE constitutes an ϵ\epsilon-Nash equilibrium for the
corresponding finite-agent game; we refer the reader to Appendix [A](https://arxiv.org/html/2512.21621v1#A1 "Appendix A Connection to the finite population game ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") for a brief explanation.

###### Theorem 2.1.

Let Assumptions [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") be in force. Assume further that 𝔼1​[θ1]≠1\mathbb{E}^{1}[\theta\_{1}]\neq 1.
Then there exists a unique RP-MFE for the problem ([2.1](https://arxiv.org/html/2512.21621v1#S2.E1 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single}) with the solution pair (μ^,ϕ^i)(\widehat{\mu},\widehat{\phi}^{i}). The associated
optimal strategy (ϕ^n−1i)n=1N(\widehat{\phi}^{i}\_{n-1})\_{n=1}^{N} is given by the bounded measurable function ϕ^n−1i:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝ\widehat{\phi}\_{n-1}^{i}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i​(s,y,zi,ϱi):=1γni​(u−d)​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)+log⁡fn−1​(s,y,zi,ϱi)}+1u−d​θi1−𝔼1​[θ1]​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)​𝔼1​[1γn1]+𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]}\begin{split}&\widehat{\phi}^{i}\_{n-1}(s,y,z^{i},\varrho\_{i}):=\frac{1}{\gamma\_{n}^{i}(u-d)}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)+\log f\_{n-1}(s,y,z^{i},\varrho\_{i})\Bigr\}\\ &\qquad+\frac{1}{u-d}\frac{\theta\_{i}}{1-\mathbb{E}^{1}[\theta\_{1}]}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]+\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr\}\end{split} |  | ( 2.6) |

and the dynamics of the associated mean-field terms (μ^n)n=1N(\widehat{\mu}\_{n})\_{n=1}^{N} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^n​((𝐬​u~)n,𝐲)=β​μ^n−1​(𝐬,𝐲−)+u​𝔼1​[ϕ^n−11​(s,y,Zn−11,ϱ1)],μ^n​((𝐬​d~)n,𝐲)=β​μ^n−1​(𝐬,𝐲−)+d​𝔼1​[ϕ^n−11​(s,y,Zn−11,ϱ1)],\begin{split}\widehat{\mu}\_{n}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})&=\beta\widehat{\mu}\_{n-1}({\bf{s}},{\bf{y}}^{-})+u\mathbb{E}^{1}[\widehat{\phi}^{1}\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})],\\ \widehat{\mu}\_{n}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})&=\beta\widehat{\mu}\_{n-1}({\bf{s}},{\bf{y}}^{-})+d\mathbb{E}^{1}[\widehat{\phi}^{1}\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})],\end{split} |  | ( 2.7) |

with the initial condition μ^0:=𝔼1​[ξ1]\widehat{\mu}\_{0}:=\mathbb{E}^{1}[\xi\_{1}] and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼1​[ϕ^n−11​(s,y,Zn−11,ϱ1)]=1u−d​11−𝔼1​[θ1]​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)​𝔼1​[1γn1]+𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]}.\mathbb{E}^{1}[\widehat{\phi}^{1}\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})]=\frac{1}{u-d}\frac{1}{1-\mathbb{E}^{1}[\theta\_{1}]}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]+\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr\}. |  | ( 2.8) |

Here, s:=sn−1s:=s\_{n-1} and y:=yn−1y:=y\_{n-1} are the last elements of (𝐬,𝐲)∈𝒮n−1×𝒴n−1({\bf{s}},{\bf{y}})\in{\cal S}^{n-1}\times{\cal Y}^{n-1},
and 𝐲−{\bf{y}}^{-} is such that (𝐲−,yn−1)=𝐲∈𝒴n−1({\bf{y}}^{-},y\_{n-1})={\bf{y}}\in{\cal Y}^{n-1}.
The function fn−1:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝf\_{n-1}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}
is defined as in Lemma [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). It satisfies the uniform bounds 0<c¯n≤fn−1≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}\leq\overline{C}\_{n}<\infty
on its domain for some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}, and is given by

|  |  |  |
| --- | --- | --- |
|  | fn−1​(s,y,zi,ϱi):=𝔼0,i​[Vn​(s​u~,Yn,Zni,ϱi)|y,zi,ϱi]𝔼0,i​[Vn​(s​d~,Yn,Zni,ϱi)|y,zi,ϱi].f\_{n-1}(s,y,z^{i},\varrho\_{i}):=\frac{\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]}{\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]}. |  |

Here, Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}\_{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R}, 0≤n≤N0\leq n\leq N,
are measurable functions satisfying the uniform bounds 0<cn≤Vn≤Cn<∞0<c\_{n}\leq V\_{n}\leq C\_{n}<\infty on their respective domains
for some positive constants cnc\_{n} and CnC\_{n}. They are defined recursively by

|  |  |  |
| --- | --- | --- |
|  | VN​(s,y,zi,ϱi):=exp⁡(γi​F​(s,y,zi)),V\_{N}(s,y,z^{i},\varrho\_{i}):=\exp\bigl(\gamma\_{i}F(s,y,z^{i})\bigr), |  |

for each (s,y,zi,ϱi)∈𝒮N×𝒴N×𝒵N×Γ(s,y,z^{i},\varrho\_{i})\in{\cal S}\_{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}\times\Gamma, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn−1​(s,y,zi,ϱi)=pn−1​(s,y)​exp⁡(−γni​u​(ϕ^n−1i​(s,y,zi,ϱi)−θi​𝔼1​[ϕ^n−11​(s,y,Zn−11,ϱ1)]))​𝔼0,i​[Vn​(s​u~,Yn,Zni,ϱi)|y,zi,ϱi]+qn−1​(s,y)​exp⁡(−γni​d​(ϕ^n−1i​(s,y,zi,ϱi)−θi​𝔼1​[ϕ^n−11​(s,y,Zn−11,ϱ1)]))​𝔼0,i​[Vn​(s​d~,Yn,Zni,ϱi)|y,zi,ϱi]\begin{split}&V\_{n-1}(s,y,z^{i},\varrho\_{i})\\ &=p\_{n-1}(s,y)\exp\Bigl(-\gamma\_{n}^{i}u\bigl(\widehat{\phi}^{i}\_{n-1}(s,y,z^{i},\varrho\_{i})-\theta\_{i}\mathbb{E}^{1}[\widehat{\phi}^{1}\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})]\bigr)\Bigr)\mathbb{E}^{0,i}\bigl[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}\bigr]\\ &+q\_{n-1}(s,y)\exp\Bigl(-\gamma\_{n}^{i}d\bigl(\widehat{\phi}^{i}\_{n-1}(s,y,z^{i},\varrho\_{i})-\theta\_{i}\mathbb{E}^{1}[\widehat{\phi}^{1}\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})]\bigr)\Bigr)\mathbb{E}^{0,i}\bigl[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}\bigr]\end{split} |  | ( 2.9) |

for each (s,y,zi,ϱi)∈𝒮n−1×𝒴n−1×𝒵n−1×Γ(s,y,z^{i},\varrho\_{i})\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma, 1≤n≤N1\leq n\leq N.

###### Remark.

Note that (1/γni)​log⁡Vn(1/\gamma\_{n}^{i})\log V\_{n} represents the effective liability at tnt\_{n}.

###### Proof.

Suppose that the problem for agent-ii at tn−1t\_{n-1} for the period [tn−1,tn][t\_{n-1},t\_{n}] is
given by the form ([2.2](https://arxiv.org/html/2512.21621v1#S2.E2 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single-tmp}). To apply Lemma [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"),
we assume that Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}\_{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R}
is a measurable function satisfying the uniform bounds cn≤Vn≤Cnc\_{n}\leq V\_{n}\leq C\_{n} on its domain for some positive constants cnc\_{n}
and CnC\_{n}. This clearly holds at t=tN−1t=t\_{N-1} for the last interval [tN−1,tN][t\_{N-1},t\_{N}]
with VN​(s,y,zi,ϱi):=exp⁡(γi​F​(s,y,zi))V\_{N}(s,y,z^{i},\varrho\_{i}):=\exp\bigl(\gamma\_{i}F(s,y,z^{i})\bigr).

In view of ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp}) in Lemma [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), the evolution of the wealth process of agent-ii under the
optimal strategy ϕn−1i,∗\phi^{i,\*}\_{n-1} is given by

|  |  |  |
| --- | --- | --- |
|  | Xni,∗=β​Xn−1i,∗+ϕn−1i,∗​(𝐒n−1,𝐘n−1,Zn−1i,ϱi)​Rn.X\_{n}^{i,\*}=\beta X\_{n-1}^{i,\*}+\phi\_{n-1}^{i,\*}({\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i},\varrho\_{i})R\_{n}. |  |

Consider the problem conditioned on the event {(𝐒n−1,𝐘n−1)=(𝐬,𝐲)}\{({\bf{S}}^{n-1},{\bf{Y}}^{n-1})=({\bf{s}},{\bf{y}})\} in ℱtn−10{\cal F}^{0}\_{t\_{n-1}}.
Under the induction hypothesis that 𝔼0,1​[Xn−11,∗|𝐬,𝐲]\mathbb{E}^{0,1}[X\_{n-1}^{1,\*}|{\bf{s}},{\bf{y}}]
is of the form μn−1​(𝐬,𝐲−)\mu\_{n-1}({\bf{s}},{\bf{y}}^{-}) with (𝐬,𝐲−)∈𝒮n−1×𝒴n−2({\bf{s}},{\bf{y}}^{-})\in{\cal S}^{n-1}\times{\cal Y}^{n-2} (when n=1n=1, we simply set μ0=𝔼1​[ξ1]\mu\_{0}=\mathbb{E}^{1}[\xi\_{1}]), and utilizing the i.i.d.​ property of (ξi,γi,θi,Zi),i=1,2,…(\xi\_{i},\gamma\_{i},\theta\_{i},Z^{i}),i=1,2,\ldots,
the condition for the RP-MFE for the period [tn−1,tn][t\_{n-1},t\_{n}] is
equivalently given by the following evolution equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn​((𝐬​u~)n,𝐲)=β​μn−1​(𝐬,𝐲−)+u​𝔼1​[ϕn−11,∗​(𝐬,𝐲,Zn−11,ϱ1)],μn​((𝐬​d~)n,𝐲)=β​μn−1​(𝐬,𝐲−)+d​𝔼1​[ϕn−11,∗​(𝐬,𝐲,Zn−11,ϱ1)].\begin{split}\mu\_{n}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})&=\beta\mu\_{n-1}({\bf{s}},{\bf{y}}^{-})+u\mathbb{E}^{1}[\phi^{1,\*}\_{n-1}({\bf{s}},{\bf{y}},Z\_{n-1}^{1},\varrho\_{1})],\\ \mu\_{n}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})&=\beta\mu\_{n-1}({\bf{s}},{\bf{y}}^{-})+d\mathbb{E}^{1}[\phi^{1,\*}\_{n-1}({\bf{s}},{\bf{y}},Z\_{n-1}^{1},\varrho\_{1})].\end{split} |  | ( 2.10) |

To solve the above equations, observe that ϕn−1i,∗\phi^{i,\*}\_{n-1} in ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp}) depends
on the mean-field term μn\mu\_{n} only through its difference Δn​(𝐬,𝐲)\Delta\_{n}({\bf{s}},{\bf{y}}).
By taking the difference in ([2.10](https://arxiv.org/html/2512.21621v1#S2.E10 "In Proof. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-RP-MFE-eq}), we obtain the equation for Δn​(𝐬,𝐲)\Delta\_{n}({\bf{s}},{\bf{y}}) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn​(𝐬,𝐲)=𝔼1​[θ1]​Δn​(𝐬,𝐲)+{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)​𝔼1​[1γn1]+𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]}.\Delta\_{n}({\bf{s}},{\bf{y}})=\mathbb{E}^{1}[\theta\_{1}]\Delta\_{n}({\bf{s}},{\bf{y}})+\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]+\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr\}. |  | ( 2.11) |

Since 𝔼1​[θ1]≠1\mathbb{E}^{1}[\theta\_{1}]\neq 1 by assumption, this equation determines Δn\Delta\_{n} uniquely as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn​(s,y)=11−𝔼1​[θ1]​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)​𝔼1​[1γn1]+𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]}\Delta\_{n}(s,y)=\frac{1}{1-\mathbb{E}^{1}[\theta\_{1}]}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]+\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr\} |  | ( 2.12) |

for each (s,y)=(sn−1,yn−1)(s,y)=(s\_{n-1},y\_{n-1}). Note that Δn\Delta\_{n} is seen to be independent of the entire trajectory of (S,Y)(S,Y) up to time tn−2t\_{n-2},
depending only on the current state (sn−1,yn−1)(s\_{n-1},y\_{n-1}).
Substituting Δn​(s,y)\Delta\_{n}(s,y) in ([2.12](https://arxiv.org/html/2512.21621v1#S2.E12 "In Proof. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-Deln}) for Δn​(𝐬,𝐲)\Delta\_{n}({\bf{s}},{\bf{y}}) in ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp}) yields
the expression ϕn−1i,∗\phi^{i,\*}\_{n-1} as given by ([2.6](https://arxiv.org/html/2512.21621v1#S2.E6 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal}) and hence its expectation as in ([2.8](https://arxiv.org/html/2512.21621v1#S2.E8 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-exp}).
Moreover, ([2.10](https://arxiv.org/html/2512.21621v1#S2.E10 "In Proof. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-RP-MFE-eq}) is shown to be equivalent to ([2.7](https://arxiv.org/html/2512.21621v1#S2.E7 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-rp-mfe}).
Since ϕn−1i,∗\phi^{i,\*}\_{n-1} given by ([2.6](https://arxiv.org/html/2512.21621v1#S2.E6 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal}) is a bounded measurable function due to
the uniform bounds on fn−1f\_{n-1}, i.e., c¯n≤fn−1≤C¯n\overline{c}\_{n}\leq f\_{n-1}\leq\overline{C}\_{n}, the mean-field term μn\mu\_{n} is also bounded and measurable
provided that μn−1\mu\_{n-1} is.
Thus, under the assumption that 𝔼0,1​[Xn−11,∗|𝐬,𝐲]=μn−1​(𝐬,𝐲−)\mathbb{E}^{0,1}[X\_{n-1}^{1,\*}|{\bf{s}},{\bf{y}}]=\mu\_{n-1}({\bf{s}},{\bf{y}}^{-}) with some bounded measurable
function μn−1\mu\_{n-1}, ([2.6](https://arxiv.org/html/2512.21621v1#S2.E6 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal}) and ([2.7](https://arxiv.org/html/2512.21621v1#S2.E7 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-rp-mfe})
provide a unique candidate for the solution pair of RP-MFE for the interval [tn−1,tn][t\_{n-1},t\_{n}].

It remains to show that this procedure can be iterated backward from the last interval [tN−1,tN][t\_{N-1},t\_{N}] to the
first one [t0,t1][t\_{0},t\_{1}]. From ([2.4](https://arxiv.org/html/2512.21621v1#S2.E4 "In Proof. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")(\ref{middle-valueF}), we see that the
value function at tn−1t\_{n-1} is given by

|  |  |  |
| --- | --- | --- |
|  | −exp(−γn−1ixi){pn−1(s,y)e−γni​(ϕn−1i,∗​u−θi​μn​((𝐬​u~)n,𝐲))𝔼0,i[Vn(su~,Yn,Zni,ϱi)|y,zi,ϱi]+qn−1(s,y)e−γni​(ϕn−1i,∗​d−θi​μn​((𝐬​d~)n,𝐲))𝔼0,i[Vn(sd~,Yn,Zni,ϱi)|y,zi,ϱi]}\begin{split}&-\exp(-\gamma\_{n-1}^{i}x^{i})\Bigl\{p\_{n-1}(s,y)e^{-\gamma\_{n}^{i}(\phi^{i,\*}\_{n-1}u-\theta\_{i}\mu\_{n}(({\bf{s}}\widetilde{u})^{n},{\bf{y}}))}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]\\ &\qquad+q\_{n-1}(s,y)e^{-\gamma\_{n}^{i}(\phi^{i,\*}\_{n-1}d-\theta\_{i}\mu\_{n}(({\bf{s}}\widetilde{d})^{n},{\bf{y}}))}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\varrho\_{i})|y,z^{i},\varrho\_{i}]\Bigr\}\end{split} |  |

for each realization (xi,𝐬,𝐲,zi,ϱi)(x^{i},{\bf{s}},{\bf{y}},z^{i},\varrho\_{i}) of (Xn−1i,∗,𝐒n−1,𝐘n−1,Zn−1i,ϱi)(X\_{n-1}^{i,\*},{\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i},\varrho\_{i})
with the conventions (s,y)=(sn−1,yn−1)(s,y)=(s\_{n-1},y\_{n-1}).
Let Vn−1V\_{n-1} be defined in ([2.9](https://arxiv.org/html/2512.21621v1#S2.E9 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-Vnm1}), which again satisfies the uniform bounds
cn−1≤Vn−1≤Cn−1c\_{n-1}\leq V\_{n-1}\leq C\_{n-1} on its domain with some positive constants cn−1c\_{n-1} and Cn−1C\_{n-1}.
By invoking ([2.7](https://arxiv.org/html/2512.21621v1#S2.E7 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-rp-mfe}), the value function at tn−1t\_{n-1} can now be expressed as

|  |  |  |
| --- | --- | --- |
|  | −exp⁡(−γn−1i​(xi−θi​μn−1​(𝐬,𝐲−)))​Vn−1​(s,y,zi,ϱi)-\exp\bigl(-\gamma\_{n-1}^{i}(x^{i}-\theta\_{i}\mu\_{n-1}({\bf{s}},{\bf{y}}^{-}))\bigr)V\_{n-1}(s,y,z^{i},\varrho\_{i}) |  |

yielding a problem of the same form as in ([2.2](https://arxiv.org/html/2512.21621v1#S2.E2 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single-tmp}) used in Lemma [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
The boundedness condition on the mean-field terms (μn)n=1N(\mu\_{n})\_{n=1}^{N} thus reduces to that of μ0:=𝔼1​[ξ1]\mu\_{0}:=\mathbb{E}^{1}[\xi\_{1}].
Since ξi∈[ξ¯,ξ¯]\xi\_{i}\in[\underline{\xi},\overline{\xi}] is bounded, the entire process (μn)n=0N(\mu\_{n})\_{n=0}^{N} is now bounded and becomes consistent with our assumption.
Thus we conclude that the above constructed optimal strategy ϕi,∗\phi^{i,\*}
and the associated mean-field μ=(μn)n=0N\mu=(\mu\_{n})\_{n=0}^{N} satisfy the fixed point condition ([2.5](https://arxiv.org/html/2512.21621v1#S2.E5 "In Definition 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-single-mu}),
and hence μ\mu and ϕi,∗\phi^{i,\*} constitute a RP-MFE solution pair, which we denote by
(μ^,ϕ^i)(\widehat{\mu},\widehat{\phi}^{i}) for the problem ([2.1](https://arxiv.org/html/2512.21621v1#S2.E1 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single}).

The uniqueness of RP-MFE follows immediately from the construction: firstly, the
optimal control in each interval by Lemma [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") for a given μn\mu\_{n} is unique;
secondly, the dynamics of the mean-field term (μn)n≥1(\mu\_{n})\_{n\geq 1} is
uniquely determined by the evolution equations ([2.7](https://arxiv.org/html/2512.21621v1#S2.E7 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-rp-mfe}) with a given initial condition μ0∈ℝ\mu\_{0}\in\mathbb{R}.
∎

###### Remark 2.3.

We analyze three regimes defined by the value of the expected relative
performance concerns 𝔼1​[θ1]:\mathbb{E}^{1}[\theta\_{1}]: 𝔼1​[θ1]≤0\mathbb{E}^{1}[\theta\_{1}]\leq 0,
0<𝔼1​[θ1]<10<\mathbb{E}^{1}[\theta\_{1}]<1,
and 𝔼1​[θ1]>1\mathbb{E}^{1}[\theta\_{1}]>1.
First, we introduce the variable:

|  |  |  |
| --- | --- | --- |
|  | 𝒯n:=11−𝔼1​[θ1]​𝔼1​[1γn1].{\cal T}\_{n}:=\frac{1}{1-\mathbb{E}^{1}[\theta\_{1}]}\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]. |  |

Observing the expression in ([2.8](https://arxiv.org/html/2512.21621v1#S2.E8 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-exp}), we can identify 𝒯n\mathcal{T}\_{n}
as the aggregate effective risk tolerance.

* •

  𝔼1​[θ1]≤0\mathbb{E}^{1}[\theta\_{1}]\leq 0:
  In this regime, on average, the lower the expected relative concern 𝔼1​[θ1]\mathbb{E}^{1}[\theta\_{1}] is,
  the smaller the aggregate risk tolerance 𝒯n\mathcal{T}\_{n} becomes,
  implying that the agents are, on average, more risk-averse.
  This is because the mean-field interaction term θi​μn​(𝐒n,𝐘n−1)\theta\_{i}\mu\_{n}(\mathbf{S}^{n},\mathbf{Y}^{n-1}) in the objective function
  ([2.2](https://arxiv.org/html/2512.21621v1#S2.E2 "In 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-single-tmp}) aligns with the wealth of agent-ii and thus increases the exposure to the risk
  in the stock position.
* •

  0<𝔼1​[θ1]<10<\mathbb{E}^{1}[\theta\_{1}]<1:
  In this regime, the agents are, on average, more risk-tolerant, and thus take larger positions as 𝔼1​[θ1]\mathbb{E}^{1}[\theta\_{1}]
  increases. In the limit 𝔼1​[θ1]→1\mathbb{E}^{1}[\theta\_{1}]\rightarrow 1, the aggregate risk tolerance and hence the stock position diverge,
  becoming a singular point within the current setup. This is caused by the divergence of the feedback loop
  of relative performance concerns, represented by the series 1+𝔼1​[θ1]+(𝔼1​[θ1])2+⋯1+\mathbb{E}^{1}[\theta\_{1}]+(\mathbb{E}^{1}[\theta\_{1}])^{2}+\cdots,
  i.e., an agent is concerned with the performance of peers, while each peer is, in turn, concerned with the performance of others, ….
* •

  𝔼1​[θ1]>1\mathbb{E}^{1}[\theta\_{1}]>1:
  In this regime, the relative performance concern becomes too large to hedge in the conventional manner.
  From ([2.8](https://arxiv.org/html/2512.21621v1#S2.E8 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-exp}), we observe that the sign of the average stock position flips.
  Suppose, for example, the transition probability for the up-move, pn−1​(s,y)p\_{n-1}(s,y), is significantly higher than qn−1​(s,y)q\_{n-1}(s,y).
  If we can neglect the contribution from fn−1f\_{n-1}, then agents would typically take a long position in the stock in the first two regimes.
  However, this is not the case here. Although a long strategy is likely to produce a positive gain,
  the gain of peers, when multiplied by a large θ>1\theta>1, would reduce the agents’ utility significantly more.
  Thus, agents, on average, take a short position, bearing a loss from the stock trade but deriving
  a higher utility gain from the loss of their peers, which is multiplied by a large θ>1\theta>1.
  Consider an agent who deviates from the majority and takes a long position.
  If the stock price rises, the agent would enjoy a positive gain from the stock position as well as a significant utility gain derived from the loss of peers.
  However, if the stock price falls, the agent would bear a loss from the stock position as well as a significant utility loss due to the gain of peers.
  Given the concavity of the utility function, such a deviation would not be optimal.
  In fact, the optimal strategy of each agent is characterized by ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp})
  regardless of the sign of Δn\Delta\_{n}.

### 2.4 Market-clearing mean-field equilibrium

In the previous subsection, assuming 𝔼1​[θ1]≠1\mathbb{E}^{1}[\theta\_{1}]\neq 1, we established
the unique existence of the RP-MFE and provided the explicit form of its solution pair (μ^,ϕ^i)(\widehat{\mu},\widehat{\phi}^{i}).
Importantly, the specific functional form of the transition probabilities (pn−1​(s,y),qn−1​(s,y))n=1N(p\_{n-1}(s,y),q\_{n-1}(s,y))\_{n=1}^{N}
did not play a decisive role. In this subsection, utilizing this degree of freedom, we show that it is possible to
choose an appropriate functional form for the stock price transition probabilities satisfying
Assumption [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (vi) so that the market-clearing mean-field equilibrium (MC-MFE)
is achieved while preserving the RP-MFE. Naturally, the market-clearing condition implies
that the agents’ stock positions must not diverge. Interestingly, this suggests that the appropriate choice
of transition probabilities that clears the market may eliminate the singularity at 𝔼1​[θ1]=1\mathbb{E}^{1}[\theta\_{1}]=1
observed in the relative performance game.
We shall show that this is indeed the case.

As in [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)], we incorporate an external stochastic order flow, Ln−1​(Sn−1,Yn−1)L\_{n-1}(S\_{n-1},Y\_{n-1}),
which represents the aggregate net stock supply per capita at each time t=tn−1t=t\_{n-1}, for 1≤n≤N1\leq n\leq N.
The external order flow is intended to model the aggregate contribution from other populations. In particular, it can be used to represent the
aggregate net supply from individual investors, whose behavior is often difficult to model via rigorous
optimization, or the supply from a major financial institution such as a central bank.

###### Assumption 2.3.

For every 1≤n≤N1\leq n\leq N, Ln−1:𝒮n−1×𝒴n−1→ℝL\_{n-1}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R} is a bounded measurable function.

###### Definition 2.2.

We say that the RP-MFE defined in Definition [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") constitutes a market-clearing
mean-field equilibrium (MC-MFE) if

|  |  |  |
| --- | --- | --- |
|  | limNp→∞1Np​∑i=1Npϕ^n−1i=Ln−1​(Sn−1,Yn−1),\lim\_{N\_{p}\rightarrow\infty}\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\widehat{\phi}\_{n-1}^{i}=L\_{n-1}(S\_{n-1},Y\_{n-1}), |  |

ℙ\mathbb{P}-a.s. for every 1≤n≤N1\leq n\leq N.

This condition implies that the excess demand/supply
per capita converges to zero in the large population limit.

###### Remark 2.4.

We often consider the baseline case Ln−1≡0L\_{n-1}\equiv 0, which corresponds to a net zero position among the agents.
The special case Ln−1​(s,y)=N#​sL\_{n-1}(s,y)=N^{\#}s, 1≤n≤N1\leq n\leq N, corresponds to the situation
where the supply is given by a constant number of shares N#N^{\#} per agent.
In a closed market setting, this implies that the net initial number of shares per capita is N#N^{\#}.
Note that, in our formulation, LL represents the monetary value of the supply per capita.

###### Theorem 2.2.

Let Assumptions [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [2.3](https://arxiv.org/html/2512.21621v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") be in force.
Then there exists a unique MC-MFE. The associated equilibrium transition probabilities of the stock price are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn−1​(s,y):=ℙ0​(Sn=u~​Sn−1|(Sn−1,Yn−1)=(s,y))=(−d)/{u​exp⁡(1𝔼1​[1/γn1]​{𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]−(1−𝔼1​[θ1])​(u−d)​Ln−1​(s,y)})−d}\begin{split}&p\_{n-1}(s,y):=\mathbb{P}^{0}\Bigl(S\_{n}=\widetilde{u}S\_{n-1}|(S\_{n-1},Y\_{n-1})=(s,y)\Bigr)\\ &=(-d)\Big/\left\{u\exp\left(\frac{1}{\mathbb{E}^{1}[1/\gamma\_{n}^{1}]}\Bigl\{\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]-(1-\mathbb{E}^{1}[\theta\_{1}])(u-d)L\_{n-1}(s,y)\Bigr\}\right)-d\right\}\end{split} |  | ( 2.13) |

for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
Here, the functions fn−1:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝf\_{n-1}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N
are measurable functions satisfying the uniform bounds 0<c¯n≤fn−1≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}\leq\overline{C}\_{n}<\infty
on their respective domains with some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}.
They are determined via the backward induction in Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), with transition probabilities replaced by those given above at each step.
Under the equilibrium transition probabilities,
the optimal strategy ϕ^n−1i\widehat{\phi}^{i}\_{n-1} of agent-ii is given by, for each (s,y,zi,ϱi)∈𝒮n−1×𝒴n−1×𝒵n−1×Γ(s,y,z^{i},\varrho\_{i})\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i​(s,y,zi,ϱi)=1𝔼1​[1/γn1]​(1−𝔼1​[θ1]γni+θi​𝔼1​[1γn1])​Ln−1​(s,y)+1u−d​{log⁡fn−1​(s,y,zi,ϱi)γni−1𝔼1​[1/γn1]​1γni​𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]}.\begin{split}\widehat{\phi}^{i}\_{n-1}(s,y,z^{i},\varrho\_{i})&=\frac{1}{\mathbb{E}^{1}[1/\gamma\_{n}^{1}]}\Bigl(\frac{1-\mathbb{E}^{1}[\theta\_{1}]}{\gamma\_{n}^{i}}+\theta\_{i}\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]\Bigr)L\_{n-1}(s,y)\\ &+\frac{1}{u-d}\Bigl\{\frac{\log f\_{n-1}(s,y,z^{i},\varrho\_{i})}{\gamma\_{n}^{i}}-\frac{1}{\mathbb{E}^{1}[1/\gamma\_{n}^{1}]}\frac{1}{\gamma\_{n}^{i}}\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr\}.\end{split} |  | ( 2.14) |

Moreover, there exists a positive constant 𝒞n−1{\cal C}\_{n-1} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|1Np​∑i=1Npϕ^n−1i​(Sn−1,Yn−1,Zn−1i,ϱi)−Ln−1​(Sn−1,Yn−1)|2≤𝒞n−1Np\mathbb{E}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i}\_{n-1}(S\_{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i})-L\_{n-1}(S\_{n-1},Y\_{n-1})\Bigr|^{2}\leq\frac{{\cal C}\_{n-1}}{N\_{p}} |  |

for every 1≤n≤N1\leq n\leq N, which establishes the convergence rate in the large population limit.

###### Remark.

Recall that the definition ϱi:=(γi,θi)\varrho\_{i}:=(\gamma\_{i},\theta\_{i}) that incorporates the θi\theta\_{i}-dependence.

###### Proof.

(Step 1): We first assume that 𝔼1​[θ1]≠1\mathbb{E}^{1}[\theta\_{1}]\neq 1.
  
In this case, we can directly use the result of Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
Since the sequence {(Zi,ϱi),i∈ℕ}\{(Z^{i},\varrho\_{i}),i\in\mathbb{N}\} is i.i.d. and also independent of the process (S,Y)(S,Y), the market-clearing condition
in Definition [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmdefinition2 "Definition 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") is equivalently given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼1​[ϕ^n−11​(s,y,Zn−11,ϱ1)]=Ln−1​(s,y)\mathbb{E}^{1}\bigl[\widehat{\phi}\_{n-1}^{1}(s,y,Z\_{n-1}^{1},\varrho\_{1})\bigr]=L\_{n-1}(s,y) |  | ( 2.15) |

for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
The expression for the transition probabilities ([2.13](https://arxiv.org/html/2512.21621v1#S2.E13 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-transition})
is a direct consequence of ([2.8](https://arxiv.org/html/2512.21621v1#S2.E8 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-exp}) in Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
and the market-clearing condition ([2.15](https://arxiv.org/html/2512.21621v1#S2.E15 "In Proof. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-MFE-eq}). By substituting the resulting expression for pn−1​(s,y)p\_{n-1}(s,y)
(and qn−1​(s,y)q\_{n-1}(s,y)) into ([2.6](https://arxiv.org/html/2512.21621v1#S2.E6 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal}), we obtain ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}).

To establish the first claim, it suffices to verify that the family of transition probabilities (pn−1​(s,y))n=1N(p\_{n-1}(s,y))\_{n=1}^{N}
defined in ([2.13](https://arxiv.org/html/2512.21621v1#S2.E13 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-transition}) satisfies the bound specified in (v​i)(vi) in Assumption [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"),
while updating the functions (fn−1)(f\_{n-1}) via the backward induction process described in Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
At t=tN−1t=t\_{N-1}, fN−1f\_{N-1} is a measurable function satisfying the uniform bounds c¯N≤fN−1≤C¯N\overline{c}\_{N}\leq f\_{N-1}\leq\overline{C}\_{N}
on its domain for some positive constants c¯N\overline{c}\_{N} and C¯N\overline{C}\_{N} due to the boundedness assumption on FF.
Combined with d<0<ud<0<u and the boundedness of other variables, such as (γi,θi,L)(\gamma\_{i},\theta\_{i},L),
we can confirm that pN−1p\_{N-1} (and hence qN−1q\_{N-1}) given by ([2.13](https://arxiv.org/html/2512.21621v1#S2.E13 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-transition}) satisfies 0<pN−1​(s,y),qN−1​(s,y)<10<p\_{N-1}(s,y),q\_{N-1}(s,y)<1
for every (s,y)∈𝒮N−1×𝒴N−1(s,y)\in{\cal S}\_{N-1}\times{\cal Y}\_{N-1}, and is thus consistent with the condition.
Moreover, ϕ^N−1i\widehat{\phi}^{i}\_{N-1} in ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}) is a bounded function on its domain
due to the uniform bounds of fN−1f\_{N-1}. It follows that VN−1V\_{N-1} defined by ([2.9](https://arxiv.org/html/2512.21621v1#S2.E9 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-Vnm1})
is a measurable function satisfying the uniform bounds cN−1≤VN−1≤CN−1c\_{N-1}\leq V\_{N-1}\leq C\_{N-1}
on its domain for some positive constants cN−1c\_{N-1} and CN−1C\_{N-1}.
This, in turn, ensures that fN−2f\_{N-2} once again satisfies the desired uniform bounds, and so do (pN−2​(s,y),qN−2​(s,y))(p\_{N-2}(s,y),q\_{N-2}(s,y)),
(s,y)∈𝒮N−2×𝒴N−2(s,y)\in{\cal S}\_{N-2}\times{\cal Y}\_{N-2}. Proceeding in this way, by backward induction, we establish the desired
consistency for every time step.

To establish the second claim, it is enough to show that, for 1≤n≤N1\leq n\leq N, there exists a positive constant 𝒞n−1{\cal C}\_{n-1} such that
the inequality

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|1Np​∑i=1Npϕ^n−1i​(s,y,Zn−1i,ϱi)−Ln−1​(s,y)|2≤𝒞n−1Np\mathbb{E}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i}\_{n-1}(s,y,Z\_{n-1}^{i},\varrho\_{i})-L\_{n-1}(s,y)\Bigr|^{2}\leq\frac{{\cal C}\_{n-1}}{N\_{p}} |  |

holds uniformly for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}.
Using the i.i.d. property of (γni,θi,Zi)(\gamma\_{n}^{i},\theta\_{i},Z^{i}) as well as the boundedness of (1/γni,θi,fn−1,Ln−1)(1/\gamma\_{n}^{i},\theta\_{i},f\_{n-1},L\_{n-1})
and 𝔼1​[θ1]≠1\mathbb{E}^{1}[\theta\_{1}]\neq 1, we can show that there exists some constant 𝒞n−1{\cal C}\_{n-1}
by rearranging the expression ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}) as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝔼|1Np∑i=1Npϕ^n−1i(s,y,Zn−1i,ϱi)−Ln−1(s,y)|2≤𝒞n−1Np2𝔼[|∑i=1Np(1γni−𝔼1[1γn1])|2+|∑i=1Np(θi−𝔼1[θ1])|2+|∑i=1Np(log⁡fn−1​(s,y,Zn−1i,ϱi)γni−𝔼1[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1])|2]≤𝒞n−1Np​𝔼1​[|1γn1−𝔼1​[1γn1]|2+|θ1−𝔼1​[θ1]|2+|log⁡fn−1​(s,y,Zn−11,ϱ1)γn1−𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]|2].\begin{split}&\mathbb{E}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i}\_{n-1}(s,y,Z\_{n-1}^{i},\varrho\_{i})-L\_{n-1}(s,y)\Bigr|^{2}\leq\frac{{\cal C}\_{n-1}}{N\_{p}^{2}}\mathbb{E}\Bigl[\Bigl|\sum\_{i=1}^{N\_{p}}\Bigl(\frac{1}{\gamma\_{n}^{i}}-\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]\Bigr)\Bigr|^{2}+\Bigl|\sum\_{i=1}^{N\_{p}}(\theta\_{i}-\mathbb{E}^{1}[\theta\_{1}])\Bigr|^{2}\\ &\qquad+\Bigl|\sum\_{i=1}^{N\_{p}}\Bigl(\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{i},\varrho\_{i})}{\gamma\_{n}^{i}}-\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr)\Bigr|^{2}\Bigr]\\ &\leq\frac{{\cal C}\_{n-1}}{N\_{p}}\mathbb{E}^{1}\Bigl[\Bigl|\frac{1}{\gamma\_{n}^{1}}-\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]\Bigr|^{2}+\bigl|\theta\_{1}-\mathbb{E}^{1}[\theta\_{1}]\bigr|^{2}+\Bigl|\frac{\log f\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{n}^{1}}-\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr|^{2}\Bigr].\end{split} |  |

Since the last variance terms are finite, this estimate establishes the desired result.
Note that the cross terms appearing in the second line vanish
due to the mutual independence of (γni,θi,Zi)i∈ℕ(\gamma\_{n}^{i},\theta\_{i},Z^{i})\_{i\in\mathbb{N}}.

(Step 2): We now consider the special case 𝔼1​[θ1]=1\mathbb{E}^{1}[\theta\_{1}]=1.
  
In this case, the equation ([2.11](https://arxiv.org/html/2512.21621v1#S2.E11 "In Proof. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-Deln-consistency}), which is the consistency (i.e., fixed point) condition for the RP-MFE,
can be satisfied if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | {log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)​𝔼1​[1γn1]+𝔼1​[log⁡fn−1​(s,y,Zn−11,ϱ1)γn1]}=0\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{n}^{1}}\Bigr]+\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{n}^{1}}\Bigr]\Bigr\}=0 |  | ( 2.16) |

for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}.
This equality determines the transition probabilities uniquely, and they are
given by the same expression ([2.13](https://arxiv.org/html/2512.21621v1#S2.E13 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-transition}) with 𝔼1​[θ1]=1\mathbb{E}^{1}[\theta\_{1}]=1.

If the above equality holds, then Δn​(𝐬,𝐲)\Delta\_{n}({\bf{s}},{\bf{y}}) and hence also
the optimal control ϕn−1i,∗\phi^{i,\*}\_{n-1} in ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp}) would
remain undetermined if we were to consider the problem solely within the RP-MFE framework.
However, if we impose the market-clearing condition, the optimal control ϕ^n−1i\widehat{\phi}^{i}\_{n-1} and Δn​(𝐬,𝐲)\Delta\_{n}({\bf{s}},{\bf{y}})
are determined uniquely. Specifically, under the condition ([2.16](https://arxiv.org/html/2512.21621v1#S2.E16 "In Proof. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{theta-1-condition}),
the equations ([2.15](https://arxiv.org/html/2512.21621v1#S2.E15 "In Proof. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-MFE-eq}) and ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp}) imply

|  |  |  |
| --- | --- | --- |
|  | Δn​(𝐬,𝐲)=(u−d)​Ln−1​(s,y),\Delta\_{n}({\bf{s}},{\bf{y}})=(u-d)L\_{n-1}(s,y), |  |

which only depends on the last elements of (𝐬,𝐲)({\bf{s}},{\bf{y}}), i.e., (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}.
Thus, once again by ([2.3](https://arxiv.org/html/2512.21621v1#S2.E3 "In Lemma 2.1. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-optimal-tmp}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i​(s,y,zi,ϱi)=θi​Ln−1​(s,y)+1γni​(u−d)​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)+log⁡fn−1​(s,y,zi,ϱi)}\widehat{\phi}^{i}\_{n-1}(s,y,z^{i},\varrho\_{i})=\theta\_{i}L\_{n-1}(s,y)+\frac{1}{\gamma\_{n}^{i}(u-d)}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)+\log f\_{n-1}(s,y,z^{i},\varrho\_{i})\Bigr\} |  | ( 2.17) |

with the transition probabilities derived above. This is also consistent with the expression in ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}) when 𝔼1​[θ1]=1\mathbb{E}^{1}[\theta\_{1}]=1.
Given that VnV\_{n} satisfies the uniform bounds 0<cn≤Vn≤Cn<∞0<c\_{n}\leq V\_{n}\leq C\_{n}<\infty on its domain for some positive constants cnc\_{n} and CnC\_{n},
the control ϕ^n−1i\widehat{\phi}^{i}\_{n-1} is bounded and measurable. Thus, under the assumption that
𝔼0,1​[Xn−11,∗|𝐬,𝐲]=μn−1​(𝐬,𝐲−)\mathbb{E}^{0,1}[X\_{n-1}^{1,\*}|{\bf{s}},{\bf{y}}]=\mu\_{n-1}({\bf{s}},{\bf{y}}^{-}) with some bounded measurable
function μn−1\mu\_{n-1}, ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}) and ([2.7](https://arxiv.org/html/2512.21621v1#S2.E7 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-rp-mfe})
with transition probabilities ([2.13](https://arxiv.org/html/2512.21621v1#S2.E13 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-transition}) with (𝔼1​[θ1]=1)(\mathbb{E}^{1}[\theta\_{1}]=1)
provide a unique candidate for the solution to the MC-MFE (and hence the RP-MFE) for the interval [tn−1,tn][t\_{n-1},t\_{n}].

In order to complete the proof, it suffices to show that this procedure can be repeated backward from the last interval [tN−1,tN][t\_{N-1},t\_{N}]
to the first one [t0,t1][t\_{0},t\_{1}]. The value function Vn−1V\_{n-1} for agent-ii at tn−1t\_{n-1}, which serves as the objective function for the
optimization for the period [tn−2,tn−1][t\_{n-2},t\_{n-1}], is given by ([2.9](https://arxiv.org/html/2512.21621v1#S2.E9 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-Vnm1}) with ϕ^i\widehat{\phi}^{i} obtained above.
It once again satisfies the desired uniform bounds for some positive constants cn−1c\_{n-1} and Cn−1C\_{n-1}.
Thus we can proceed with the backward induction one step further.
The condition for μn−1\mu\_{n-1} is reduced to the initial condition μ0:=𝔼1​[ξ1]\mu\_{0}:=\mathbb{E}^{1}[\xi\_{1}]
and is satisfied trivially. The second claim on the convergence rate can be shown as in (Step 1).
∎

###### Remark 2.5.

Theorem [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") shows that there is no singularity at 𝔼1​[θ1]=1\mathbb{E}^{1}[\theta\_{1}]=1
and the three regimes (𝔼1​[θ1]≤0,0<𝔼1​[θ1]<1,𝔼1​[θ1]>1)(\mathbb{E}^{1}[\theta\_{1}]\leq 0,0<\mathbb{E}^{1}[\theta\_{1}]<1,\mathbb{E}^{1}[\theta\_{1}]>1)
are continuously connected. Let us give some remarks on the behavior of the equilibrium transition probabilities.
The economic interpretation when there is no relative performance concern θ≡0\theta\equiv 0
is detailed in Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)][Section 2.4], in particular, on the effects from the liabilities (or negative of the endowments).
Recall that the transition probability of the up-move under the risk-neutral measure ℚ\mathbb{Q}
is given by pℚ=(−d)/(u−d)p^{\mathbb{Q}}=(-d)/(u-d). Thus pn−1​(s,y)>pℚp\_{n-1}(s,y)>p^{\mathbb{Q}} denotes
a positive excess return (at the node (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}).
Suppose, for simplicity, the hedge needs for the effective liability are negligible, i.e., log⁡fn−1≈0\log f\_{n-1}\approx 0.
In this case, when 𝔼1​[θ1]<1\mathbb{E}^{1}[\theta\_{1}]<1, the positive stock supply Ln−1​(s,y)L\_{n-1}(s,y) implies that a positive excess
return is required by the agents to compensate for their risk of taking long positions for market clearing.
As 𝔼1​[θ1]\mathbb{E}^{1}[\theta\_{1}] approaches 11, the effective risk-tolerance 𝒯n{\cal T}\_{n} becomes larger, which
reduces the required excess return. The agents become totally indifferent to the stock size they absorb
at the critical point 𝔼1​[θ1]=1\mathbb{E}^{1}[\theta\_{1}]=1.
Conversely, when 𝔼1​[θ1]>1\mathbb{E}^{1}[\theta\_{1}]>1, the effective risk aversion of the agents becomes negative due to extremely
strong relative performance concerns. In order to clear the market, the excess return turns negative pn−1​(s,y)<pℚp\_{n-1}(s,y)<p^{\mathbb{Q}}.
With the negative effective risk aversion, a negative excess return is required to induce agents to hold a long position
to balance the positive market supply.

## 3 A network of relative performance concerns among multiple populations

### 3.1 The setup and notation

A primary limitation of the previous framework lies in their restriction to a single homogeneous population,
where all agents share identical liability functions FF, distributions of i.i.d. idiosyncratic shocks ZiZ^{i}, initial wealth ξi\xi\_{i},
risk aversion γi\gamma\_{i}, and relative performance concern θi\theta\_{i}. Crucially, the relative performance concern θi\theta\_{i} was constrained to
reference solely the aggregate wealth of the entire population. This simplified structure fails to capture more realistic scenarios
where agents benchmark their performance against specific peer groups or competitors rather than the market average as a whole.

To address this limitation, we consider a more generalized setting where
agents (i.e., financial firms) belong to distinct sectors or groups p=1,2,…,mp=1,2,\ldots,m.
Agents in different populations are assumed to have distinct liability functions FpF^{p} and
distributions of idiosyncratic factors, characterized by ξip,γip\xi\_{i}^{p},\gamma\_{i}^{p}, and Zi,pZ^{i,p}.
Most importantly, we introduce a heterogeneous network of relative performance concerns
represented by θp,ki\theta^{i}\_{p,k}, which denotes the sensitivity
of agent-ii in population pp (denoted by agent-(i,p)(i,p) hereafter) relative to the performance of population kk, for k=1,…,mk=1,\ldots,m.
Moreover, we allow the liability function FpF^{p} to be path-dependent on the stock price,
which is a natural extension of the previous case. As we will see, this generalization necessitates that the stock price transition probabilities also
become path-dependent to achieve the MC-MFE.
Note that, without loss of generality, we can assume that the liability depends only on the terminal values of (YN,ZNi,p)(Y\_{N},Z\_{N}^{i,p}), unlike the stock price.
This simplification is justified because any path-dependent effects involving these factors can always be incorporated
by lifting the underlying processes to higher dimensions.

Let us start by preparing the appropriate probability spaces. We use the same setup and notation as in Section [2.1](https://arxiv.org/html/2512.21621v1#S2.SS1 "2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"),
for the complete filtered probability space (Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)(\Omega^{0},{\cal F}^{0},({\cal F}^{0}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{0}).
The filtration (ℱtn0)n=0N({\cal F}^{0}\_{t\_{n}})\_{n=0}^{N} is generated by the stock price process S:=(Sn:=S​(tn))n=0NS:=(S\_{n}:=S(t\_{n}))\_{n=0}^{N}
and the common noise process Y:=(Yn:=Y​(tn))n=0NY:=(Y\_{n}:=Y(t\_{n}))\_{n=0}^{N}. The notations for their ranges (𝒮n,𝒮n,𝒴n,𝒴n)({\cal S}\_{n},{\cal S}^{n},{\cal Y}\_{n},{\cal Y}^{n}),
0≤n≤N0\leq n\leq N, remain identical to those defined in Section [2.1](https://arxiv.org/html/2512.21621v1#S2.SS1 "2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). Specifically, we continue to assume
that the trajectories of the stock price are confined to the binomial tree, and that the process YY possesses a finite state space.
We also use the same notation R~n:=Sn/Sn−1\widetilde{R}\_{n}:=S\_{n}/S\_{n-1}, Rn:=R~n−exp⁡(r​Δ)R\_{n}:=\widetilde{R}\_{n}-\exp(r\Delta), u:=u~−exp⁡(r​Δ)u:=\widetilde{u}-\exp(r\Delta), d:=d~−exp⁡(r​Δ)d:=\widetilde{d}-\exp(r\Delta),
and β:=exp⁡(r​Δ)\beta:=\exp(r\Delta) as before. To model heterogeneity across the populations, we introduce a countably infinite number of
complete filtered probability spaces (Ωi,p,ℱi,p,(ℱtni,p)n=0N,ℙi,p),i=1,2,…(\Omega^{i,p},{\cal F}^{i,p},({\cal F}^{i,p}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{i,p}),i=1,2,\ldots
for each population p=1,2,…,mp=1,2,\ldots,m. Here, (Ωi,p,ℱi,p,(ℱtni,p)n=0N,ℙi,p)(\Omega^{i,p},{\cal F}^{i,p},({\cal F}^{i,p}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{i,p})
is the space modeling the idiosyncratic variables and shocks specific to agent-(i,p)(i,p):
ξip\xi\_{i}^{p} is the initial wealth and γip\gamma\_{i}^{p} is the risk aversion of the agent,
both of which are ℱ0i,p{\cal F}^{i,p}\_{0}-measurable. We also define γni,p:=(βN/βn)​γip\gamma\_{n}^{i,p}:=(\beta^{N}/\beta^{n})\gamma\_{i}^{p}, 0≤n≤N0\leq n\leq N, for notational simplicity;
Zi,p:=(Zni,p:=Zi,p​(tn))n=0NZ^{i,p}:=(Z^{i,p}\_{n}:=Z^{i,p}(t\_{n}))\_{n=0}^{N} denotes the dZpd\_{Z^{p}}-dimensional (ℱtni,p)n=0N({\cal F}^{i,p}\_{t\_{n}})\_{n=0}^{N}-adapted idiosyncratic shock process to the agent.
We denote the range of Zni,pZ\_{n}^{i,p} by 𝒵np(⊂ℝdZp){\cal Z}\_{n}^{p}~(\subset\mathbb{R}^{d\_{Z^{p}}}).
To represent a network of relative performance concerns, we introduce ℱ0i,p{\cal F}^{i,p}\_{0}-measurable
real random variables θp,ki\theta^{i}\_{p,k}, k=1,2,…,mk=1,2,\ldots,m. Here, θp,ki\theta^{i}\_{p,k} denotes
the relative concern of agent-(i,p)(i,p) in population pp regarding the average performance of population kk.

By standard procedures, we define

|  |  |  |
| --- | --- | --- |
|  | (Ω,ℱ,(ℱtn)n=0N,ℙ):=(Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)⊗p=1m⊗i=1∞(Ωi,p,ℱi,p,(ℱtni,p)n=0N,ℙi,p)(\Omega,{\cal F},({\cal F}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}):=(\Omega^{0},{\cal F}^{0},({\cal F}^{0}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{0})\otimes\_{p=1}^{m}\otimes\_{i=1}^{\infty}(\Omega^{i,p},{\cal F}^{i,p},({\cal F}^{i,p}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{i,p}) |  |

as the complete filtered probability space describing the entire environment of the mm-population model.
On the other hand, the relevant probability space for each agent-(i,p)(i,p) is given by

|  |  |  |
| --- | --- | --- |
|  | (Ω0,(i,p),ℱ0,(i,p),(ℱtn0,(i,p))n=0N,ℙ0,(i,p)):=(Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)⊗(Ωi,p,ℱi,p,(ℱtni,p)n=0N,ℙi,p).(\Omega^{0,(i,p)},{\cal F}^{0,(i,p)},({\cal F}\_{t\_{n}}^{0,(i,p)})\_{n=0}^{N},\mathbb{P}^{0,(i,p)}):=(\Omega^{0},{\cal F}^{0},({\cal F}^{0}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{0})\otimes(\Omega^{i,p},{\cal F}^{i,p},({\cal F}^{i,p}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{i,p}). |  |

Expectations with respect to ℙ0\mathbb{P}^{0}, ℙi,p\mathbb{P}^{i,p}, ℙ0,(i,p)\mathbb{P}^{0,(i,p)} and ℙ\mathbb{P}
are denoted by 𝔼0​[⋅]\mathbb{E}^{0}[\cdot], 𝔼i,p​[⋅]\mathbb{E}^{i,p}[\cdot], 𝔼0,(i,p)\mathbb{E}^{0,(i,p)} and 𝔼​[⋅]\mathbb{E}[\cdot], respectively.
We use the same conventions for conditional expectations as in Section [2.1](https://arxiv.org/html/2512.21621v1#S2.SS1 "2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

###### Assumption 3.1.

(i): u~\widetilde{u} and d~\widetilde{d} are real constants satisfying 0<d~<exp⁡(r​Δ)<u~<∞0<\widetilde{d}<\exp(r\Delta)<\widetilde{u}<\infty.
  
(ii): The variables (ξip,γip,(θp,ki)k=1m,Zi,p)(\xi\_{i}^{p},\gamma\_{i}^{p},(\theta^{i}\_{p,k})\_{k=1}^{m},Z^{i,p}) are identically distributed across all agents i=1,2,…i=1,2,\ldots
within each population p=1,…,mp=1,\ldots,m.
  
(iii): For each population p=1,…,mp=1,\ldots,m, there exist real constants ξ¯p,ξ¯p,γ¯p,γ¯p\underline{\xi}^{p},\overline{\xi}^{p},\underline{\gamma}^{p},\overline{\gamma}^{p},
and θ¯p,θ¯p\underline{\theta}^{p},\overline{\theta}^{p} such that for every i∈ℕi\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | ξip∈[ξ¯p,ξ¯p]⊂ℝ,ϱip:=(γip,(θp,ki)k=1m)∈Γp:=[γ¯p,γ¯p]×[θ¯p,θ¯p]m⊂(0,∞)×ℝm.\xi\_{i}^{p}\in[\underline{\xi}^{p},\overline{\xi}^{p}]\subset\mathbb{R},\qquad\varrho\_{i}^{p}:=(\gamma\_{i}^{p},(\theta^{i}\_{p,k})\_{k=1}^{m})\in\Gamma^{p}:=[\underline{\gamma}^{p},\overline{\gamma}^{p}]\times[\underline{\theta}^{p},\overline{\theta}^{p}]^{m}\subset(0,\infty)\times\mathbb{R}^{m}. |  |

(iv): For each (i,p)(i,p), i∈ℕ,p=1,…,mi\in\mathbb{N},p=1,\ldots,m, the process Zi,pZ^{i,p} is Markovian, i.e.,
𝔼i,p​[f​(Zni,p)|ℱtki,p]=𝔼i,p​[f​(Zni,p)|Zki,p]\mathbb{E}^{i,p}[f(Z^{i,p}\_{n})|{\cal F}^{i,p}\_{t\_{k}}]=\mathbb{E}^{i,p}[f(Z^{i,p}\_{n})|Z^{i,p}\_{k}] for every bounded measurable function ff on 𝒵np{\cal Z}\_{n}^{p}
and k≤nk\leq n.
  
(v): The process YY is Markovian i.e., 𝔼0​[f​(Yn)|ℱtk0]=𝔼0​[f​(Yn)|Yk]\mathbb{E}^{0}[f(Y\_{n})|{\cal F}^{0}\_{t\_{k}}]=\mathbb{E}^{0}[f(Y\_{n})|Y\_{k}] for every bounded measurable
function ff on 𝒴n{\cal Y}\_{n} and k≤nk\leq n.
  
(vi): The transition probabilities of S=(Sn)n=0NS=(S\_{n})\_{n=0}^{N} satisfy, for every 0≤n≤N−10\leq n\leq N-1, a.s.,

|  |  |  |
| --- | --- | --- |
|  | ℙ0(Sn+1=u~Sn|ℱtn0)=ℙ0(Sn+1=u~Sn|𝐒n,Yn)=:pn(𝐒n,Yn),ℙ0(Sn+1=d~Sn|ℱtn0)=ℙ0(Sn+1=d~Sn|𝐒n,Yn)=:qn(𝐒n,Yn),\begin{split}&\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|{\cal F}^{0}\_{t\_{n}})=\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|{\bf{S}}^{n},Y\_{n})=:p\_{n}({\bf{S}}^{n},Y\_{n}),\\ &\mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|{\cal F}^{0}\_{t\_{n}})=\mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|{\bf{S}}^{n},Y\_{n})=:q\_{n}({\bf{S}}^{n},Y\_{n}),\end{split} |  |

where pn,qn(:=1−pn):𝒮n×𝒴n→ℝp\_{n},q\_{n}~(:=1-p\_{n}):{\cal S}^{n}\times{\cal Y}\_{n}\rightarrow\mathbb{R}, 0≤n≤N−10\leq n\leq N-1 are bounded measurable
functions satisfying

|  |  |  |
| --- | --- | --- |
|  | 0<pn​(𝐬,y),qn​(𝐬,y)<10<p\_{n}({\bf{s}},y),q\_{n}({\bf{s}},y)<1 |  |

for every (𝐬,y)∈𝒮n×𝒴n({\bf{s}},y)\in{\cal S}^{n}\times{\cal Y}\_{n}.

The transition probabilities of the stock price are now allowed to depend on its past trajectory.
Under conditions (v) and (vi) above, (Sn+1,Yn+1)(S\_{n+1},Y\_{n+1}) now satisfy the property:

|  |  |  |
| --- | --- | --- |
|  | 𝔼0[f(Sn+1)g(Yn+1)|ℱtn0]=𝔼0[f(Sn+1)|𝐒n,Yn]𝔼0[g(Yn+1)|Yn]a.s.,0≤n≤N−1,\mathbb{E}^{0}[f(S\_{n+1})g(Y\_{n+1})|{\cal F}^{0}\_{t\_{n}}]=\mathbb{E}^{0}[f(S\_{n+1})|{\bf{S}}^{n},Y\_{n}]\mathbb{E}^{0}[g(Y\_{n+1})|Y\_{n}]~{\rm a.s.,}\quad 0\leq n\leq N-1, |  |

for any bounded measurable functions f:𝒮n+1→ℝf:{\cal S}\_{n+1}\rightarrow\mathbb{R} and g:𝒴n+1→ℝg:{\cal Y}\_{n+1}\rightarrow\mathbb{R}.

###### Remark 3.1.

The risk-neutral measure ℚ\mathbb{Q} remains the same as in the previous section, in which
the transition probability of the up-move is pℚ=(−d)/(u−d)p^{\mathbb{Q}}=(-d)/(u-d) and the down-move qℚ=u/(u−d)q^{\mathbb{Q}}=u/(u-d).
The bound on the transition probabilities in Assumption [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (vi)
guarantees that the probability measures ℙ0∘S−1\mathbb{P}^{0}\circ S^{-1} and ℚ∘S−1\mathbb{Q}\circ S^{-1} are equivalent.
Hence our system is arbitrage free.

### 3.2 Optimization problem

We now formulate the optimization problem for each agent. Each agent-(i,p)(i,p) in population pp,
with initial wealth ξip\xi\_{i}^{p}, engages in self-financing trading with the risk-free money market account and
the single risky stock. The agent adopts an (ℱtn0,(i,p))n=0N({\cal F}^{0,(i,p)}\_{t\_{n}})\_{n=0}^{N}-adapted trading strategy (ϕni,p)n=0N−1(\phi^{i,p}\_{n})\_{n=0}^{N-1},
representing the cash amount invested in the stock at time tnt\_{n}.
The associated wealth process of agent-(i,p)(i,p), Xi,p:=(Xni,p:=Xi,p​(tn))n=0NX^{i,p}:=(X\_{n}^{i,p}:=X^{i,p}(t\_{n}))\_{n=0}^{N}, follows the dynamics

|  |  |  |
| --- | --- | --- |
|  | Xn+1i,p=exp⁡(r​Δ)​(Xni,p−ϕni,p)+ϕni,p​R~n+1=β​Xni,p+ϕni,p​Rn+1,\begin{split}X^{i,p}\_{n+1}&=\exp(r\Delta)(X\_{n}^{i,p}-\phi^{i,p}\_{n})+\phi^{i,p}\_{n}\widetilde{R}\_{n+1}\\ &=\beta X\_{n}^{i,p}+\phi^{i,p}\_{n}R\_{n+1},\end{split} |  |

with X0i,p=ξipX\_{0}^{i,p}=\xi\_{i}^{p}.

We suppose that each agent-(i,p)(i,p) solves the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(ϕni,p)n=0N−1∈𝔸i,p𝔼0,(i,p)​[−exp⁡(−γip​(XNi,p−∑k=1mθp,ki​μNk​(𝐒N,𝐘N−1)−Fp​(𝐒N,YN,ZNi,p)))|ℱ00,(i,p)],\sup\_{(\phi^{i,p}\_{n})\_{n=0}^{N-1}\in\mathbb{A}^{i,p}}\mathbb{E}^{0,(i,p)}\left[-\exp\Bigl(-\gamma\_{i}^{p}\Bigl(X\_{N}^{i,p}-\sum\_{k=1}^{m}\theta^{i}\_{p,k}\mu\_{N}^{k}({\bf{S}}^{N},{\bf{Y}}^{N-1})-F^{p}({\bf{S}}^{N},Y\_{N},Z\_{N}^{i,p})\Bigr)\Bigr)\bigg|{\cal F}\_{0}^{0,(i,p)}\right], |  | ( 3.1) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝔸i,p:={(ϕni,p)n=0N−1:ϕni,p​is an ℱtn0,(i,p)-measurable real-valued random variable}\mathbb{A}^{i,p}:=\{(\phi^{i,p}\_{n})\_{n=0}^{N-1}:\phi^{i,p}\_{n}~\text{is an ${\cal F}^{0,(i,p)}\_{t\_{n}}$-measurable real-valued random variable}\} |  |

denotes the admissible control space.
μNp:𝒮N×𝒴N−1→ℝ\mu^{p}\_{N}:{\cal S}^{N}\times{\cal Y}^{N-1}\rightarrow\mathbb{R}, p=1,…,mp=1,\ldots,m, are measurable functions
denoting the average wealth of the population pp. We seek to find a fixed point (μnp)n=0N(\mu\_{n}^{p})\_{n=0}^{N} with μ0p:=𝔼i,p​[ξip]\mu\_{0}^{p}:=\mathbb{E}^{i,p}[\xi\_{i}^{p}]
and μnp:𝒮n×𝒴n−1→ℝ\mu\_{n}^{p}:{\cal S}^{n}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N,
satisfying

|  |  |  |
| --- | --- | --- |
|  | μnp​(𝐒n,𝐘n−1)=𝔼0,(i,p)​[Xni,p|ℱtn0]​a.s.\mu\_{n}^{p}({\bf{S}}^{n},{\bf{Y}}^{n-1})=\mathbb{E}^{0,(i,p)}\bigl[X\_{n}^{i,p}|{\cal F}^{0}\_{t\_{n}}\bigr]~{\rm a.s.} |  |

for every population p=1,…,mp=1,\ldots,m.

For notational convenience in the subsequent analysis, let us introduce matrix notations.
We define the interaction matrix Θ∈ℝm×m\Theta\in\mathbb{R}^{m\times m} representing a network of
aggregate relative performance concerns among populations, whose (p,k)(p,k)-th entry is given by the expected concern:

|  |  |  |
| --- | --- | --- |
|  | Θp,k:=𝔼i,p​[θp,ki],1≤p,k≤m,\Theta\_{p,k}:=\mathbb{E}^{i,p}[\theta^{i}\_{p,k}],\quad 1\leq p,k\leq m, |  |

which is independent of the specific agent i∈ℕi\in\mathbb{N} due to the i.i.d. assumption.
For any mm-dimensional vector 𝝁=(μ1,…,μm)⊤∈ℝm\bm{\mu}=(\mu^{1},\ldots,\mu^{m})^{\top}\in\mathbb{R}^{m},
we adopt the notation:

|  |  |  |
| --- | --- | --- |
|  | (θi​𝝁)p:=∑k=1mθp,ki​μk,(Θ​𝝁)p:=∑k=1mΘp,k​μk.\bigl(\theta^{i}\bm{\mu}\bigr)\_{p}:=\sum\_{k=1}^{m}\theta^{i}\_{p,k}\mu^{k},\quad\bigl(\Theta\bm{\mu}\bigr)\_{p}:=\sum\_{k=1}^{m}\Theta\_{p,k}\mu^{k}. |  |

###### Assumption 3.2.

For each 1≤p≤m1\leq p\leq m, the following conditions hold:
  
(i): The function Fp:𝒮N×𝒴N×𝒵Np→ℝF^{p}:{\cal S}^{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}^{p}\rightarrow\mathbb{R} is measurable and bounded.
  
(ii): Every agent-(i,p)(i,p), i=1,2,…i=1,2,\ldots, is a price-taker in the sense that they consider the stock price process (and
hence its transition probabilities specified in Assumption [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (vi)) to be exogenously determined by
the collective actions of the others and unaffected by the agent’s own trading strategies.
  
(iii): Every agent-(i,p)(i,p), i=1,2,…i=1,2,\ldots, treats the mean-field terms (μnk)n=0N,k=1,…,m(\mu\_{n}^{k})\_{n=0}^{N},k=1,\ldots,m,
where μnk:𝒮n×𝒴n−1→ℝ\mu\_{n}^{k}:{\cal S}^{n}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, as exogenous bounded measurable functions, believing that
they are determined by the collective actions of the agents in the population kk and unaffected by the agent’s
own trading strategies.444As noted in Assumption [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), since the domains are finite,
the boundedness assumption is theoretically redundant but kept for clarity.

Following the approach in the previous section, for 1≤n≤N1\leq n\leq N, we analyze the one-period problem at t=tn−1t=t\_{n-1}
for the interval [tn−1,tn][t\_{n-1},t\_{n}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supϕn−1i,p𝔼0,(i,p)​[−exp⁡(−γni,p​(Xni,p−(θi​𝝁n)p​(𝐒n,𝐘n−1)))​Vnp​(𝐒n,Yn,Zni,p,ϱip)|ℱtn−10,(i,p)]\sup\_{\phi^{i,p}\_{n-1}}\mathbb{E}^{0,(i,p)}\left[-\exp\Bigl(-\gamma\_{n}^{i,p}\bigl(X\_{n}^{i,p}-(\theta^{i}\bm{\mu}\_{n})\_{p}({\bf{S}}^{n},{\bf{Y}}^{n-1})\bigr)\Bigr)V\_{n}^{p}({\bf{S}}^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})\bigg|{\cal F}\_{t\_{n-1}}^{0,(i,p)}\right] |  | ( 3.2) |

where the supremum is taken over the ℱtn−10,(i,p){\cal F}^{0,(i,p)}\_{t\_{n-1}}-measurable real-valued random variables.
We recall that γni,p:=(βN/βn)​γip\gamma\_{n}^{i,p}:=(\beta^{N}/\beta^{n})\gamma\_{i}^{p} and ϱip:=(γip,(θp,ki)k=1m)\varrho\_{i}^{p}:=(\gamma\_{i}^{p},(\theta^{i}\_{p,k})\_{k=1}^{m}).

###### Lemma 3.1.

Suppose that Assumption [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and Assumption [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (ii) and (iii) hold.
Furthermore, assume that Vnp:𝒮n×𝒴n×𝒵np×Γp→ℝV\_{n}^{p}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
is a measurable function satisfying the uniform bounds 0<cn≤Vnp≤Cn<∞0<c\_{n}\leq V\_{n}^{p}\leq C\_{n}<\infty on its
domain with some positive constants cnc\_{n} and CnC\_{n}.
Then, for every p=1,…,mp=1,\ldots,m, the problem ([3.2](https://arxiv.org/html/2512.21621v1#S3.E2 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi-tmp}) admits a unique optimal solution ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1}
given by a bounded measurable function ϕn−1(i,p),∗:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝ\phi^{(i,p),\*}\_{n-1}:{\cal S}^{n-1}\times{\cal Y}^{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, such that ϕn−1(i,p),∗:=ϕn−1(i,p),∗​(𝐒n−1,𝐘n−1,Zn−1i,p,ϱip)\phi^{(i,p),\*}\_{n-1}:=\phi^{(i,p),\*}\_{n-1}({\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i,p},\varrho\_{i}^{p}) a.s., where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1(i,p),∗​(𝐬,𝐲,zi,p,ϱip):=(θi​𝚫n)p​(𝐬,𝐲)u−d+1γni,p​(u−d)​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)+log⁡fn−1p​(𝐬,y,zi,p,ϱip)}.\begin{split}\phi^{(i,p),\*}\_{n-1}({\bf{s}},{\bf{y}},z^{i,p},\varrho\_{i}^{p})&:=\frac{(\theta^{i}\bm{\Delta}\_{n})\_{p}({\bf{s}},{\bf{y}})}{u-d}+\frac{1}{\gamma\_{n}^{i,p}(u-d)}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)+\log f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\Bigr\}.\end{split} |  | ( 3.3) |

Here, y=yn−1∈𝒴n−1y=y\_{n-1}\in{\cal Y}\_{n-1} is the last element of 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1}.
Furthermore, fn−1p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝf\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
is a measurable function satisfying the uniform bounds 0<c¯n≤fn−1p≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n}<\infty
on its domain for some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}, and 𝚫n:=(Δnk)k=1m\bm{\Delta}\_{n}:=(\Delta\_{n}^{k})\_{k=1}^{m}, Δnk:𝒮n−1×𝒴n−1→ℝ\Delta\_{n}^{k}:{\cal S}^{n-1}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, 1≤k≤m1\leq k\leq m are bounded measurable functions. They are defined respectively by

|  |  |  |
| --- | --- | --- |
|  | fn−1p​(𝐬,y,zi,p,ϱip):=𝔼0,(i,p)​[Vnp​((𝐬​u~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]𝔼0,(i,p)​[Vnp​((𝐬​d~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip],Δnk​(𝐬,𝐲):=μnk​((𝐬​u~)n,𝐲)−μnk​((𝐬​d~)n,𝐲).\begin{split}&f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho^{p}\_{i}):=\frac{\mathbb{E}^{0,(i,p)}[V\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}]}{\mathbb{E}^{0,(i,p)}[V\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}]},\\ &\Delta\_{n}^{k}({\bf{s}},{\bf{y}}):=\mu\_{n}^{k}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})-\mu\_{n}^{k}(({\bf{s}}\widetilde{d})^{n},{\bf{y}}).\end{split} |  |

###### Proof.

We solve the problem on each set {ω0,(i,p)∈Ω0,(i,p):(Xn−1i,p,𝐒n−1,𝐘n−1,Zn−1i,p,ϱip)=(xi,p,𝐬,𝐲,zi,p,ϱip)}\{\omega^{0,(i,p)}\in\Omega^{0,(i,p)}:(X\_{n-1}^{i,p},{\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i,p},\varrho\_{i}^{p})=(x^{i,p},{\bf{s}},{\bf{y}},z^{i,p},\varrho\_{i}^{p})\}.
Here, with a slight abuse of notation, we use the same symbols for the realizations of ℱ0i,p{\cal F}^{i,p}\_{0}-measurable
random variables. We also set y=yn−1y=y\_{n-1}, i.e., the last element of 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1}.
The problem ([3.2](https://arxiv.org/html/2512.21621v1#S3.E2 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi-tmp}) can be rewritten equivalently as

|  |  |  |  |
| --- | --- | --- | --- |
|  | infϕi,p∈ℝ𝔼0,(i,p)[exp(−γni,p(βxi,p+ϕi,pRn−(θi𝝁n)p(𝐒n,𝐘n−1))Vnp(𝐒n,Yn,Zni,p,ϱip)|𝐬,𝐲,zi,p,ϱip]=exp(−γn−1i,pxi,p)infϕi,p{pn−1​(𝐬,y)​exp⁡(−γni,p​(ϕi,p​u−(θi​𝝁n)p​((𝐬​u~)n,𝐲)))​𝔼0,(i,p)​[Vnp​((𝐬​u~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]+qn−1(𝐬,y)exp(−γni,p(ϕi,pd−(θi𝝁n)p((𝐬d~)n,𝐲)))𝔼0,(i,p)[Vnp((𝐬d~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]},\begin{split}&\hskip-14.22636pt\inf\_{\phi^{i,p}\in\mathbb{R}}\mathbb{E}^{0,(i,p)}\Bigl[\exp\Bigl(-\gamma\_{n}^{i,p}(\beta x^{i,p}+\phi^{i,p}R\_{n}-(\theta^{i}\bm{\mu}\_{n})\_{p}({\bf{S}}^{n},{\bf{Y}}^{n-1})\Bigr)V\_{n}^{p}({\bf{S}}^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|{\bf{s}},{\bf{y}},z^{i,p},\varrho\_{i}^{p}\Bigr]\\ &=\exp\bigl(-\gamma\_{n-1}^{i,p}x^{i,p}\bigr)\inf\_{\phi^{i,p}}\Bigl\{\\ &p\_{n-1}({\bf{s}},y)\exp\Bigl(-\gamma\_{n}^{i,p}\bigl(\phi^{i,p}u-(\theta^{i}\bm{\mu}\_{n})\_{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\\ &\hskip-8.53581pt+q\_{n-1}({\bf{s}},y)\exp\Bigl(-\gamma\_{n}^{i,p}\bigl(\phi^{i,p}d-(\theta^{i}\bm{\mu}\_{n})\_{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\Bigr\},\end{split} |  | ( 3.4) |

where we have used property (vi) in Assumption [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). Given that γni,p>0\gamma\_{n}^{i,p}>0
and d<0<ud<0<u, the optimal trade position ϕ(i,p),∗\phi^{(i,p),\*} is uniquely characterized by the first-order condition:

|  |  |  |
| --- | --- | --- |
|  | pn−1​(𝐬,y)​u​exp⁡(−γni,p​(ϕi,p​u−(θi​𝝁n)p​((𝐬​u~)n,𝐲)))​𝔼0,(i,p)​[Vnp​((𝐬​u~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]+qn−1​(𝐬,y)​d​exp⁡(−γni,p​(ϕi,p​d−(θi​𝝁n)p​((𝐬​d~)n,𝐲)))​𝔼0,(i,p)​[Vnp​((𝐬​d~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]=0,\begin{split}&p\_{n-1}({\bf{s}},y)u\exp\Bigl(-\gamma\_{n}^{i,p}\bigl(\phi^{i,p}u-(\theta^{i}\bm{\mu}\_{n})\_{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\\ &\quad+q\_{n-1}({\bf{s}},y)d\exp\Bigl(-\gamma\_{n}^{i,p}\bigl(\phi^{i,p}d-(\theta^{i}\bm{\mu}\_{n})\_{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})\bigr)\Bigr)\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]=0,\end{split} |  |

which yields the desired result. The existence of the uniform bounds on fn−1pf\_{n-1}^{p} is
a direct consequence of its definition and the uniform bounds on VnpV\_{n}^{p}.
∎

### 3.3 Relative performance mean-field equilibrium

We now study the mean-field equilibrium in a network of relative performance concerns among the mm populations.

###### Definition 3.1.

We say that the system is in the relative performance mean-field equilibrium (RP-MFE) if the problem ([3.1](https://arxiv.org/html/2512.21621v1#S3.E1 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi})
admits an optimal solution (ϕn−1(i,p),∗)n=1N(\phi^{(i,p),\*}\_{n-1})\_{n=1}^{N}, 1≤p≤m1\leq p\leq m, i=1,2,…i=1,2,\ldots,
for agents satisfying Assumptions [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (ii) and (iii), such that,
with μ0p:=𝔼i,p​[ξip]\mu\_{0}^{p}:=\mathbb{E}^{i,p}[\xi\_{i}^{p}], the bounded measurable functions
μnp:𝒮n×𝒴n−1→ℝ\mu\_{n}^{p}:{\cal S}^{n}\times{\cal Y}^{n-1}\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N, satisfy
the fixed point condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μnp(𝐒n,𝐘n−1)=𝔼0,(i,p)[Xn(i,p),∗|ℱtn0]a.s.,1≤n≤N,\mu\_{n}^{p}({\bf{S}}^{n},{\bf{Y}}^{n-1})=\mathbb{E}^{0,(i,p)}\bigl[X\_{n}^{(i,p),\*}|{\cal F}^{0}\_{t\_{n}}\bigr]~{\rm a.s.,}\quad 1\leq n\leq N, |  | ( 3.5) |

for every population p=1,…,mp=1,\ldots,m. Here, X(i,p),∗X^{(i,p),\*} denotes the wealth process of agent-(i,p)(i,p) associated with the optimal control ϕ(i,p),∗\phi^{(i,p),\*}.
Moreover, we denote the associated processes in the RP-MFE by (μ^p,ϕ^i,p)(\widehat{\mu}^{p},\widehat{\phi}^{i,p}), 1≤p≤m1\leq p\leq m, and refer to them
as the solution pairs of the RP-MFE.
For each p=1,…,mp=1,\ldots,m and i=1,2,…i=1,2,\ldots, we also use the symbol X^i,p\widehat{X}^{i,p} to
represent the wealth process of agent-(i,p)(i,p) associated with ϕ^i,p\widehat{\phi}^{i,p} and the initial condition ξip\xi\_{i}^{p}.

Since we are dealing with a symmetric problem with i.i.d. variables and processes (ξip,γip,θp,ki,Zi,p)(\xi\_{i}^{p},\gamma\_{i}^{p},\theta^{i}\_{p,k},Z^{i,p}), i∈ℕi\in\mathbb{N},
the choice of a representative agent-(i,p)(i,p) in each population p=1,…,mp=1,\ldots,m is arbitrary.
Given that filtration (ℱtk0)k=0N({\cal F}^{0}\_{t\_{k}})\_{k=0}^{N} is generated by (S,Y)(S,Y), the fixed-point condition ([3.5](https://arxiv.org/html/2512.21621v1#S3.E5 "In Definition 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-multi-mu})
can be equivalently represented by using agent-(1,p)(1,p) as the representative:

|  |  |  |
| --- | --- | --- |
|  | μnp​(𝐬,𝐲−)=𝔼1,p​[Xn(1,p),∗|𝐬,𝐲]=𝔼1,p​[Xn(1,p),∗|𝐬,𝐲−],\mu\_{n}^{p}({\bf{s}},{\bf{y}}^{-})=\mathbb{E}^{1,p}\bigl[X\_{n}^{(1,p),\*}|{\bf{s}},{\bf{y}}\bigr]=\mathbb{E}^{1,p}\bigl[X\_{n}^{(1,p),\*}|{\bf{s}},{\bf{y}}^{-}\bigr], |  |

for every (𝐬,𝐲−)∈𝒮n×𝒴n−1({\bf{s}},{\bf{y}}^{-})\in{\cal S}^{n}\times{\cal Y}^{n-1}. Here, 𝐲=(𝐲−,yn)∈𝒴n{\bf{y}}=({\bf{y}}^{-},y\_{n})\in{\cal Y}^{n}.
In the following, we prove the existence and uniqueness of the RP-MFE. We will show that the
path-dependence of ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} on 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1} in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") reduces to a dependence
on the current state y=yn−1∈𝒴n−1y=y\_{n-1}\in{\cal Y}\_{n-1} in the RP-MFE.

###### Theorem 3.1.

Suppose that Assumptions [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") hold.
We also assume that the m×mm\times m matrix (I−Θ)(I-\Theta), with entries defined by
{(I−Θ)p,k:=(δp,k−𝔼1,p​[θp,k1]),1≤p,k≤m}\{(I-\Theta)\_{p,k}:=(\delta\_{p,k}-\mathbb{E}^{1,p}[\theta^{1}\_{p,k}]),1\leq p,k\leq m\}, has a bounded inverse (I−Θ)−1(I-\Theta)^{-1}.
Then, the problem ([3.1](https://arxiv.org/html/2512.21621v1#S3.E1 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi}) admits a unique RP-MFE with the solution
pairs (μ^p,ϕ^i,p)p=1m(\widehat{\mu}^{p},\widehat{\phi}^{i,p})\_{p=1}^{m}. For each population p=1,…,mp=1,\ldots,m, the associated optimal strategy (ϕ^n−1i,p)n=1N(\widehat{\phi}^{i,p}\_{n-1})\_{n=1}^{N}
is given by the bounded measurable function ϕ^n−1i,p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝ\widehat{\phi}^{i,p}\_{n-1}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i,p​(𝐬,y,zi,p,ϱip):=1γni,p​(u−d)​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)+log⁡fn−1p​(𝐬,y,zi,p,ϱip)}+1u−d​∑k=1m(θi​(I−Θ)−1)p,k​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​𝔼1,k​[1γn1,k]+𝔼1,k​[log⁡fn−1k​(𝐬,y,Zn−11,k,ϱik)γn1,k]}\begin{split}&\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\frac{1}{\gamma\_{n}^{i,p}(u-d)}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)+\log f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\Bigr\}\\ &\hskip-22.76219pt+\frac{1}{u-d}\sum\_{k=1}^{m}(\theta^{i}(I-\Theta)^{-1})\_{p,k}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)\mathbb{E}^{1,k}\Bigl[\frac{1}{\gamma\_{n}^{1,k}}\Bigr]+\mathbb{E}^{1,k}\Bigl[\frac{\log f\_{n-1}^{k}({\bf{s}},y,Z\_{n-1}^{1,k},\varrho\_{i}^{k})}{\gamma\_{n}^{1,k}}\Bigr]\Bigr\}\end{split} |  | ( 3.6) |

and the dynamics of the associated mean-field terms (μ^np)n=1N(\widehat{\mu}\_{n}^{p})\_{n=1}^{N} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^np​((𝐬​u~)n,𝐲)=β​μ^n−1p​(𝐬,𝐲−)+u​𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)],μ^np​((𝐬​d~)n,𝐲)=β​μ^n−1p​(𝐬,𝐲−)+d​𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)],\begin{split}&\widehat{\mu}\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})=\beta\widehat{\mu}^{p}\_{n-1}({\bf{s}},{\bf{y}}^{-})+u\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\\ &\widehat{\mu}\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})=\beta\widehat{\mu}^{p}\_{n-1}({\bf{s}},{\bf{y}}^{-})+d\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\end{split} |  | ( 3.7) |

with the initial condition μ^0p:=𝔼1,p​[ξ1p]\widehat{\mu}^{p}\_{0}:=\mathbb{E}^{1,p}[\xi\_{1}^{p}] and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)]=1u−d​∑k=1m(I−Θ)p,k−1​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​𝔼1,k​[1γn1,k]+𝔼1,k​[log⁡fn−1k​(𝐬,y,Zn−11,k,ϱ1k)γn1,k]}.\begin{split}&\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr]\\ &\quad=\frac{1}{u-d}\sum\_{k=1}^{m}(I-\Theta)^{-1}\_{p,k}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)\mathbb{E}^{1,k}\Bigl[\frac{1}{\gamma\_{n}^{1,k}}\Bigr]+\mathbb{E}^{1,k}\Bigl[\frac{\log f\_{n-1}^{k}({\bf{s}},y,Z\_{n-1}^{1,k},\varrho\_{1}^{k})}{\gamma\_{n}^{1,k}}\Bigr]\Bigr\}.\end{split} |  | ( 3.8) |

Here, y:=yn−1y:=y\_{n-1} is the last element of 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1},
and 𝐲−{\bf{y}}^{-} denotes the history up to tn−2t\_{n-2} such that (𝐲−,yn−1)=𝐲({\bf{y}}^{-},y\_{n-1})={\bf{y}}.
For each p=1,…,mp=1,\ldots,m, the function fn−1p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝf\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
is defined as in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). It satisfies the uniform bounds 0<c¯n≤fn−1p≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n}<\infty
on its domain for some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}, and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn−1p​(𝐬,y,zi,p,ϱip):=𝔼0,(i,p)​[Vnp​((𝐬​u~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]𝔼0,(i,p)​[Vnp​((𝐬​d~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip].f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\frac{\mathbb{E}^{0,(i,p)}[V\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}]}{\mathbb{E}^{0,(i,p)}[V\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}]}. |  | ( 3.9) |

Here, for each p=1,…,mp=1,\ldots,m, Vnp:𝒮n×𝒴n×𝒵np×Γp→ℝV\_{n}^{p}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, 0≤n≤N0\leq n\leq N,
are measurable functions satisfying the uniform bounds 0<cn≤Vnp≤Cn<∞0<c\_{n}\leq V\_{n}^{p}\leq C\_{n}<\infty on their respective domains
with some positive constants cnc\_{n} and CnC\_{n}.
They are defined recursively by
VNp​(𝐬,y,zi,p,ϱip):=exp⁡(γip​Fp​(𝐬,y,zi,p)),V\_{N}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\exp\bigl(\gamma\_{i}^{p}F^{p}({\bf{s}},y,z^{i,p})\bigr),
for each (𝐬,y,zi,p,ϱip)∈𝒮N×𝒴N×𝒵Np×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}^{p}\times\Gamma^{p}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn−1p​(𝐬,y,zi,p,ϱip)=pn−1​(𝐬,y)​exp⁡(−γni,p​u​(ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)−∑k=1mθp,ki​𝔼1,k​[ϕ^n−11,k​(𝐬,y,Zn−11,k,ϱ1k)]))×𝔼0,(i,p)​[Vnp​((𝐬​u~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]+qn−1​(𝐬,y)​exp⁡(−γni,p​d​(ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)−∑k=1mθp,ki​𝔼1,k​[ϕ^n−11,k​(𝐬,y,Zn−11,k,ϱ1k)]))×𝔼0,(i,p)​[Vnp​((𝐬​d~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]\begin{split}V\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})&=p\_{n-1}({\bf{s}},y)\exp\Bigl(-\gamma\_{n}^{i,p}u\bigl(\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})-\sum\_{k=1}^{m}\theta^{i}\_{p,k}\mathbb{E}^{1,k}[\widehat{\phi}^{1,k}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,k},\varrho\_{1}^{k})]\bigr)\Bigr)\\ &\qquad\qquad\times\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\\ &+q\_{n-1}({\bf{s}},y)\exp\Bigl(-\gamma\_{n}^{i,p}d\bigl(\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})-\sum\_{k=1}^{m}\theta^{i}\_{p,k}\mathbb{E}^{1,k}[\widehat{\phi}^{1,k}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,k},\varrho\_{1}^{k})]\bigr)\Bigr)\\ &\qquad\qquad\times\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\end{split} |  | ( 3.10) |

for each (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}, 1≤n≤N1\leq n\leq N.

###### Remark.

Note that (1/γni,p)​log⁡Vnp(1/\gamma\_{n}^{i,p})\log V\_{n}^{p} represents the effective liability for agent-(i,p)(i,p) at t=tnt=t\_{n}.

###### Proof.

Suppose that, for every p=1,…,mp=1,\ldots,m, the problem for agent-(i,p)(i,p) at tn−1t\_{n-1} for the period [tn−1,tn][t\_{n-1},t\_{n}] takes the
form ([3.2](https://arxiv.org/html/2512.21621v1#S3.E2 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi-tmp}). To apply Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we hypothesize that Vnp:𝒮n×𝒴n×𝒵np×Γp→ℝV\_{n}^{p}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
is a measurable function satisfying the uniform bounds cn≤Vnp≤Cnc\_{n}\leq V\_{n}^{p}\leq C\_{n} on its domain
for some positive constants cnc\_{n} and CnC\_{n}. This clearly holds at t=tN−1t=t\_{N-1} for the last interval [tN−1,tN][t\_{N-1},t\_{N}]
with VNp​(𝐬,y,zi,p,ϱip):=exp⁡(γip​Fp​(𝐬,y,zi,p))V\_{N}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\exp\bigl(\gamma\_{i}^{p}F^{p}({\bf{s}},y,z^{i,p})\bigr).

Using ([3.3](https://arxiv.org/html/2512.21621v1#S3.E3 "In Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal-tmp}) in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), the evolution of the wealth process of agent-(i,p)(i,p)
under the optimal strategy ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} is given by

|  |  |  |
| --- | --- | --- |
|  | Xn(i,p),∗=β​Xn−1(i,p),∗+ϕn−1(i,p),∗​(𝐒n−1,𝐘n−1,Zn−1i,p,ϱip)​Rn.X\_{n}^{(i,p),\*}=\beta X\_{n-1}^{(i,p),\*}+\phi^{(i,p),\*}\_{n-1}({\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i,p},\varrho\_{i}^{p})R\_{n}. |  |

Consider the problem conditioned on the event {(𝐒n−1,𝐘n−1)=(𝐬,𝐲)}\{({\bf{S}}^{n-1},{\bf{Y}}^{n-1})=({\bf{s}},{\bf{y}})\} in ℱtn−10{\cal F}^{0}\_{t\_{n-1}}.
Under the induction hypothesis that 𝔼0,(1,p)​[Xn−1(1,p),∗|𝐬,𝐲]\mathbb{E}^{0,(1,p)}[X^{(1,p),\*}\_{n-1}|{\bf{s}},{\bf{y}}] is given by the form μn−1p​(𝐬,𝐲−)\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-})
with (𝐬,𝐲−)∈𝒮n−1×𝒴n−2({\bf{s}},{\bf{y}}^{-})\in{\cal S}^{n-1}\times{\cal Y}^{n-2} (when n=1n=1, we simply set μ0p=𝔼1,p​[ξ1p]\mu\_{0}^{p}=\mathbb{E}^{1,p}[\xi\_{1}^{p}]),
and using the i.i.d. property of the variables (ϱip,Zi,p),i=1,2,…(\varrho\_{i}^{p},Z^{i,p}),i=1,2,\ldots, the fixed point condition ([3.5](https://arxiv.org/html/2512.21621v1#S3.E5 "In Definition 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-multi-mu})
for the RP-MFE for the period [tn−1,tn][t\_{n-1},t\_{n}] is equivalently given by the following
evolution equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μnp​((𝐬​u~)n,𝐲)=β​μn−1p​(𝐬,𝐲−)+u​𝔼1,p​[ϕn−1(1,p),∗​(𝐬,𝐲,Zn−11,p,ϱ1p)],μnp​((𝐬​d~)n,𝐲)=β​μn−1p​(𝐬,𝐲−)+d​𝔼1,p​[ϕn−1(1,p),∗​(𝐬,𝐲,Zn−11,p,ϱ1p)],\begin{split}&\mu\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})=\beta\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-})+u\mathbb{E}^{1,p}\bigl[\phi^{(1,p),\*}\_{n-1}({\bf{s}},{\bf{y}},Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\\ &\mu\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})=\beta\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-})+d\mathbb{E}^{1,p}\bigl[\phi^{(1,p),\*}\_{n-1}({\bf{s}},{\bf{y}},Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\end{split} |  | ( 3.11) |

for p=1,…,mp=1,\ldots,m. To solve the above equations, notice that ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} in ([3.3](https://arxiv.org/html/2512.21621v1#S3.E3 "In Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal-tmp})
depends on the mean-field terms μnk,k=1,…​m\mu\_{n}^{k},k=1,\ldots m only through their differences Δnk​(𝐬,𝐲),k=1,…,m\Delta\_{n}^{k}({\bf{s}},{\bf{y}}),k=1,\ldots,m.
Taking the difference in ([3.11](https://arxiv.org/html/2512.21621v1#S3.E11 "In Proof. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-RP-MFE-eq}), we obtain the simultaneous equations for (Δnp​(𝐬,𝐲))p=1m(\Delta\_{n}^{p}({\bf{s}},{\bf{y}}))\_{p=1}^{m} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δnp​(𝐬,𝐲)=∑k=1mΘp,k​Δnk​(𝐬,𝐲)+{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​𝔼1,p​[1γn1,p]+𝔼1,p​[log⁡fn−1p​(𝐬,y,Zn−11,p,ϱ1p)γn1,p]}.\begin{split}\Delta\_{n}^{p}({\bf{s}},{\bf{y}})&=\sum\_{k=1}^{m}\Theta\_{p,k}\Delta\_{n}^{k}({\bf{s}},{\bf{y}})\\ &+\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)\mathbb{E}^{1,p}\Bigl[\frac{1}{\gamma\_{n}^{1,p}}\Bigr]+\mathbb{E}^{1,p}\Bigl[\frac{\log f\_{n-1}^{p}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})}{\gamma\_{n}^{1,p}}\Bigr]\Bigr\}.\end{split} |  | ( 3.12) |

Since (I−Θ)(I-\Theta) is invertible by assumption, this equation determines (Δnp)p=1m(\Delta\_{n}^{p})\_{p=1}^{m} uniquely as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δnp​(𝐬,y)=∑k=1m(I−Θ)p,k−1​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​𝔼1,k​[1γn1,k]+𝔼1,k​[log⁡fn−1k​(𝐬,y,Zn−11,k,ϱ1k)γn1,k]}\Delta\_{n}^{p}({\bf{s}},y)=\sum\_{k=1}^{m}(I-\Theta)^{-1}\_{p,k}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)\mathbb{E}^{1,k}\Bigl[\frac{1}{\gamma\_{n}^{1,k}}\Bigr]+\mathbb{E}^{1,k}\Bigl[\frac{\log f\_{n-1}^{k}({\bf{s}},y,Z\_{n-1}^{1,k},\varrho\_{1}^{k})}{\gamma\_{n}^{1,k}}\Bigr]\Bigr\} |  | ( 3.13) |

for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}, p=1,…,mp=1,\ldots,m. Note that 𝚫n\bm{\Delta}\_{n} turns out to be independent of the
entire trajectory of YY up to time tn−2t\_{n-2}, depending only on the current state y=yn−1y=y\_{n-1}.
By substituting 𝚫n​(𝐬,𝐲)\bm{\Delta}\_{n}({\bf{s}},{\bf{y}}) in ([3.3](https://arxiv.org/html/2512.21621v1#S3.E3 "In Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal-tmp}) with 𝚫n​(𝐬,y)\bm{\Delta}\_{n}({\bf{s}},y) in ([3.13](https://arxiv.org/html/2512.21621v1#S3.E13 "In Proof. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-Deln}),
we obtain the desired expression ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} as in ([3.6](https://arxiv.org/html/2512.21621v1#S3.E6 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal})
and hence its expectation as in ([3.8](https://arxiv.org/html/2512.21621v1#S3.E8 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-exp}), which are also independent of the trajectory of YY up to time tn−2t\_{n-2}.
The measurable functions fn−1p,p=1,…​mf\_{n-1}^{p},p=1,\ldots m defined by ([3.9](https://arxiv.org/html/2512.21621v1#S3.E9 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-fnm1-update}) satisfy
the uniform bounds c¯n≤fn−1p≤C¯n\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n} for some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}
due to the uniform bounds on (Vnp)p=1m(V\_{n}^{p})\_{p=1}^{m}.
Hence ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1}, p=1,…,mp=1,\ldots,m with expression of ([3.6](https://arxiv.org/html/2512.21621v1#S3.E6 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal})
are bounded and measurable, and from ([3.11](https://arxiv.org/html/2512.21621v1#S3.E11 "In Proof. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-RP-MFE-eq}),
μnp\mu\_{n}^{p}, p=1,…,mp=1,\ldots,m are also bounded and measurable as long as μn−1p\mu\_{n-1}^{p}, p=1,…,mp=1,\ldots,m are.
Thus, under the assumption that 𝔼0,(1,p)​[Xn−1(1,p),∗|𝐬,𝐲]=μn−1p​(𝐬,𝐲−)\mathbb{E}^{0,(1,p)}[X\_{n-1}^{(1,p),\*}|{\bf{s}},{\bf{y}}]=\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-}) with some bounded measurable
functions μn−1p\mu\_{n-1}^{p}, ([3.6](https://arxiv.org/html/2512.21621v1#S3.E6 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal}) and ([3.7](https://arxiv.org/html/2512.21621v1#S3.E7 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-mfe}) provide a unique candidate
for the solution pairs of RP-MFE for the interval [tn−1,tn][t\_{n-1},t\_{n}].

It remains to show that this procedure can be repeated backward from the last interval [tN−1,tN][t\_{N-1},t\_{N}]
to the first one [t0,t1][t\_{0},t\_{1}]. It follows from (LABEL:multi-value-tmp)(\ref{multi-value-tmp}) that the value function for agent-(i,p)(i,p) at tn−1t\_{n-1} is

|  |  |  |
| --- | --- | --- |
|  | −exp(−γn−1i,pxi,p){pn−1(𝐬,y)e−γni,p​(ϕn−1(i,p),∗​u−(θi​𝝁n)p​((𝐬​u~)n,𝐲))𝔼0,(i,p)[Vnp((𝐬u~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]+qn−1(𝐬,y)e−γni,p​(ϕn−1(i,p),∗​d−(θi​𝝁n)p​((𝐬​d~)n,𝐲))𝔼0,(i,p)[Vnp((𝐬d~)n,Yn,Zni,p,ϱip)|y,zi,p,ϱip]},\begin{split}&-\exp\bigl(-\gamma\_{n-1}^{i,p}x^{i,p}\bigr)\Bigl\{p\_{n-1}({\bf{s}},y)e^{-\gamma\_{n}^{i,p}\bigl(\phi^{(i,p),\*}\_{n-1}u-(\theta^{i}\bm{\mu}\_{n})\_{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})\bigr)}\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\\ &\qquad+q\_{n-1}({\bf{s}},y)e^{-\gamma\_{n}^{i,p}\bigl(\phi^{(i,p),\*}\_{n-1}d-(\theta^{i}\bm{\mu}\_{n})\_{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})\bigr)}\mathbb{E}^{0,(i,p)}\bigl[V\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i,p},\varrho\_{i}^{p})|y,z^{i,p},\varrho\_{i}^{p}\bigr]\Bigr\},\end{split} |  |

for each realization (xi,p,𝐬,𝐲,zi,p,ϱip)(x^{i,p},{\bf{s}},{\bf{y}},z^{i,p},\varrho\_{i}^{p}) of (Xn−1(i,p),∗,𝐒n−1,𝐘n−1,Zn−1i,p,ϱip)(X^{(i,p),\*}\_{n-1},{\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z^{i,p}\_{n-1},\varrho\_{i}^{p})
with y=yn−1y=y\_{n-1}. From ([3.7](https://arxiv.org/html/2512.21621v1#S3.E7 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-mfe}), the above value function becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | −exp⁡(−γn−1i,p​(xi,p−(θi​𝝁n−1)p​(𝐬,𝐲−)))​Vn−1p​(𝐬,y,zi,p,ϱip),-\exp\Bigl(-\gamma\_{n-1}^{i,p}\bigl(x^{i,p}-(\theta^{i}\bm{\mu}\_{n-1})\_{p}({\bf{s}},{\bf{y}}^{-})\bigr)\Bigr)V\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}), |  | ( 3.14) |

where Vn−1pV\_{n-1}^{p} is given by ([3.10](https://arxiv.org/html/2512.21621v1#S3.E10 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-Vnm1}), which once again satisfies the uniform bounds cn−1≤Vn−1p≤Cn−1c\_{n-1}\leq V\_{n-1}^{p}\leq C\_{n-1}
for some positive constants cn−1c\_{n-1} and Cn−1C\_{n-1}. Therefore, we reproduce the problem for [tn−2,tn−1][t\_{n-2},t\_{n-1}]
of the same form as in ([3.2](https://arxiv.org/html/2512.21621v1#S3.E2 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi-tmp}) used in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
Thus the boundedness condition on the mean-field terms (μnp)n=1N(\mu\_{n}^{p})\_{n=1}^{N}, p=1,…,mp=1,\ldots,m
is reduced to that of μ0p:=𝔼1,p​[ξ1p]\mu\_{0}^{p}:=\mathbb{E}^{1,p}[\xi\_{1}^{p}], p=1,…,mp=1,\ldots,m.
Since ξip∈[ξ¯p,ξ¯p],p=1,…,m\xi\_{i}^{p}\in[\underline{\xi}^{p},\overline{\xi}^{p}],p=1,\ldots,m are bounded, all the processes μp,p=1,…,m\mu^{p},p=1,\ldots,m
are now bounded and become consistent with our assumption.
Thus we conclude that the above constructed mean-field μp\mu^{p} and the optimal strategy ϕ(i,p),∗\phi^{(i,p),\*}
satisfy the fixed point condition ([3.5](https://arxiv.org/html/2512.21621v1#S3.E5 "In Definition 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-multi-mu}), and hence (μp)(\mu^{p}) and (ϕ(i,p),∗)(\phi^{(i,p),\*})
constitute the RP-MFE solution pairs, which we denote by (μ^p,ϕ^i,p)(\widehat{\mu}^{p},\widehat{\phi}^{i,p}) for the problem ([3.1](https://arxiv.org/html/2512.21621v1#S3.E1 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi}).

The uniqueness of RP-MFE immediately follows from construction: firstly, the optimal control in each interval by Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
for given (μnp)(\mu\_{n}^{p}) is unique; secondly, the dynamics of the mean-field terms (μnp)n≥1,p=1,…,m(\mu\_{n}^{p})\_{n\geq 1},p=1,\ldots,m
is uniquely determined by the evolution equations ([3.7](https://arxiv.org/html/2512.21621v1#S3.E7 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-mfe})
with a given set of initial conditions μ0p∈ℝ\mu\_{0}^{p}\in\mathbb{R}, p=1,…,mp=1,\ldots,m.
∎

### 3.4 Market-clearing mean-field equilibrium

As in Section [2.4](https://arxiv.org/html/2512.21621v1#S2.SS4 "2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we leverage the degrees of freedom in the transition probabilities (pn−1​(𝐬,y),qn−1​(𝐬,y))(p\_{n-1}({\bf{s}},y),q\_{n-1}({\bf{s}},y)),
1≤n≤N1\leq n\leq N, to establish the market-clearing mean-field equilibrium (MC-MFE).
This equilibrium analysis reveals how the inter-population network of relative performance concerns,
characterized by the matrix Θ\Theta,
affects the equilibrium stock price transition probabilities, and more specifically, the equilibrium
excess return required by the agents to compensate for their risk.
In this section, we allow the external stochastic order flow at each t=tn−1t=t\_{n-1}
to depend on the stock price trajectory up to tn−1t\_{n-1}, taking the form Ln−1​(𝐒n−1,Yn−1)L\_{n-1}({\bf{S}}^{n-1},Y\_{n-1}).

###### Assumption 3.3.

For every 1≤n≤N1\leq n\leq N, Ln−1:𝒮n−1×𝒴n−1→ℝL\_{n-1}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R} is a bounded
measurable function.

As in Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)], we study the mean-field market clearing as the
large population limit while keeping the ratios of relative population size constant.
Let us denote the number of agents in population pp by NpN\_{p} and set
𝒩:=N1+⋯+Nm{\cal N}:=N\_{1}+\cdots+N\_{m} as the total population size.
We use wp:=Np/𝒩w\_{p}:=N\_{p}/{\cal N} to denote the relative size of population pp.
Observe that we have the relation:

|  |  |  |
| --- | --- | --- |
|  | 1𝒩​∑p=1m∑i=1Npϕ^n−1i,p=∑p=1mwp​(1Np​∑i=1Npϕ^n−1i,p).\frac{1}{{\cal N}}\sum\_{p=1}^{m}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}=\sum\_{p=1}^{m}w\_{p}\Bigl(\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}\Bigr). |  |

###### Definition 3.2.

We say that the RP-MFE defined in Definition [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") constitutes a market-clearing
mean-field equilibrium (MC-MFE) if

|  |  |  |
| --- | --- | --- |
|  | lim𝒩→∞1𝒩​∑p=1m∑i=1Npϕ^n−1i,p=Ln−1​(𝐒n−1,Yn−1),\lim\_{{\cal N}\rightarrow\infty}\frac{1}{{\cal N}}\sum\_{p=1}^{m}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}=L\_{n-1}({\bf{S}}^{n-1},Y\_{n-1}), |  |

ℙ\mathbb{P}-a.s. for every 1≤n≤N1\leq n\leq N, where the large population limit is taken with
the population ratios (wp)p=1m(w\_{p})\_{p=1}^{m} kept constant.

Let fn−1p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝf\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, p=1,…,mp=1,\ldots,m,
1≤n≤N1\leq n\leq N be the functions defined in Theorem [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
To simplify the notation and facilitate the subsequent discussion, we introduce the following effective variables,
assuming that the matrix (I−Θ)(I-\Theta) has a bounded inverse:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯ni,p:=1γni,p+∑k=1m(θi​(I−Θ)−1)p,k​𝔼1,k​[1γn1,k],𝒯n:=∑p,k=1mwp​(I−Θ)p,k−1​𝔼1,k​[1γn1,k],𝒱n−1i,p​(𝐬,y,zi,p,ϱip):=log⁡fn−1p​(𝐬,y,zi,p,ϱip)γni,p+∑k=1m(θi​(I−Θ)−1)p,k​𝔼1,k​[log⁡fn−1k​(𝐬,y,Zn−11,k,ϱ1k)γn1,k],𝒱n−1​(𝐬,y):=∑p,k=1mwp​(I−Θ)p,k−1​𝔼1,k​[log⁡fn−1k​(𝐬,y,Zn−11,k,ϱ1k)γn1,k].\begin{split}&{\cal T}^{i,p}\_{n}:=\frac{1}{\gamma\_{n}^{i,p}}+\sum\_{k=1}^{m}\bigl(\theta^{i}(I-\Theta)^{-1}\bigr)\_{p,k}\mathbb{E}^{1,k}\Bigl[\frac{1}{\gamma\_{n}^{1,k}}\Bigr],\\ &{\cal T}\_{n}:=\sum\_{p,k=1}^{m}w\_{p}(I-\Theta)^{-1}\_{p,k}\mathbb{E}^{1,k}\Bigl[\frac{1}{\gamma\_{n}^{1,k}}\Bigr],\\ &{\cal V}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\frac{\log f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})}{\gamma\_{n}^{i,p}}+\sum\_{k=1}^{m}\bigl(\theta^{i}(I-\Theta)^{-1})\_{p,k}\mathbb{E}^{1,k}\Bigl[\frac{\log f\_{n-1}^{k}({\bf{s}},y,Z^{1,k}\_{n-1},\varrho\_{1}^{k})}{\gamma\_{n}^{1,k}}\Bigr],\\ &{\cal V}\_{n-1}({\bf{s}},y):=\sum\_{p,k=1}^{m}w\_{p}(I-\Theta)^{-1}\_{p,k}\mathbb{E}^{1,k}\Bigl[\frac{\log f\_{n-1}^{k}({\bf{s}},y,Z\_{n-1}^{1,k},\varrho\_{1}^{k})}{\gamma\_{n}^{1,k}}\Bigr].\end{split} |  | ( 3.15) |

We recall that γni,p:=(βN/βn)​γip\gamma\_{n}^{i,p}:=(\beta^{N}/\beta^{n})\gamma\_{i}^{p} and ϱip:=(γip,(θp,ki)k=1m)\varrho\_{i}^{p}:=(\gamma\_{i}^{p},(\theta^{i}\_{p,k})\_{k=1}^{m}).
Here, 𝒯ni,p{\cal T}^{i,p}\_{n}, which is ℱ0i,p{\cal F}^{i,p}\_{0}-measurable, represents the effective risk tolerance of agent-(i,p)(i,p) at tnt\_{n}.
Note that 𝒯n{\cal T}\_{n} corresponds to the aggregate risk tolerance of the market, satisfying the relation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯n=∑p=1mwp​𝔼1,p​[𝒯n1,p].{\cal T}\_{n}=\sum\_{p=1}^{m}w\_{p}\mathbb{E}^{1,p}[{\cal T}\_{n}^{1,p}]. |  | ( 3.16) |

Similarly, 𝒱n−1i,p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝ{\cal V}\_{n-1}^{i,p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
is a measurable function representing the sensitivity of the effective liability at tn−1t\_{n-1} for agent-(i,p)(i,p),
where the dependence on γni,p\gamma\_{n}^{i,p} is incorporated by the argument ϱip\varrho\_{i}^{p}. Thus, strictly speaking,
the superscript ii in 𝒱n−1i,p{\cal V}^{i,p}\_{n-1} is redundant, but we retain it to clearly associate the variable
with the relevant agent.
Note also that 𝒱n−1:𝒮n−1×𝒴n−1→ℝ{\cal V}\_{n-1}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R} corresponds to the aggregate
sensitivity of the effective liability, which satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱n−1​(𝐬,y)=∑p=1mwp​𝔼1,p​[𝒱n−11,p​(𝐬,y,Zn−11,p,ϱ1p)].{\cal V}\_{n-1}({\bf{s}},y)=\sum\_{p=1}^{m}w\_{p}\mathbb{E}^{1,p}\bigl[{\cal V}\_{n-1}^{1,p}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr]. |  | ( 3.17) |

With these effective variables, the optimal control ([3.6](https://arxiv.org/html/2512.21621v1#S3.E6 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal}) in the RP-MFE
can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)=1u−d​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​𝒯ni,p+𝒱n−1i,p​(𝐬,y,zi,p,ϱip)}.\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})=\frac{1}{u-d}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr){\cal T}\_{n}^{i,p}+{\cal V}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\Bigr\}. |  | ( 3.18) |

###### Theorem 3.2.

Suppose that Assumptions [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmassumption3 "Assumption 3.3. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") hold.
Furthermore, we assume that the matrix (I−Θ)(I-\Theta) has a bounded inverse and that 𝒯N≠0{\cal T}\_{N}\neq 0 (which implies 𝒯n≠0{\cal T}\_{n}\neq 0
for all 1≤n≤N1\leq n\leq N). Then there exists a
unique MC-MFE. The associated equilibrium transition probabilities of the stock price are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn−1​(𝐬,y)=(−d)/{u​exp⁡(𝒱n−1​(𝐬,y)−(u−d)​Ln−1​(𝐬,y)𝒯n)−d}\begin{split}p\_{n-1}({\bf{s}},y)=(-d)\Big/\left\{u\exp\left(\frac{\displaystyle{\cal V}\_{n-1}({\bf{s}},y)-(u-d)L\_{n-1}({\bf{s}},y)}{\displaystyle{\cal T}\_{n}}\right)-d\right\}\end{split} |  | ( 3.19) |

for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N. Here, for each 1≤n≤N1\leq n\leq N,
the functions fn−1p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝf\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, p=1,…,mp=1,\ldots,m,
which are components of (𝒱n−1i,k,𝒱n−1)({\cal V}\_{n-1}^{i,k},{\cal V}\_{n-1}),
are measurable functions satisfying the uniform bounds 0<c¯n≤fn−1p≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n}<\infty
on their respective domains for some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}.
They are determined by the backward induction in Theorem [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"),
with the transition probabilities replaced by those given above at each step.
Under the equilibrium transition probabilities, the optimal strategy of agent-(i,p)(i,p) is given by, for each
(𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)=𝒯ni,p𝒯n​Ln−1​(𝐬,y)+1u−d​(𝒱n−1i,p​(𝐬,y,zi,p,ϱip)−𝒯ni,p𝒯n​𝒱n−1​(𝐬,y)).\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})=\frac{{\cal T}\_{n}^{i,p}}{{\cal T}\_{n}}L\_{n-1}({\bf{s}},y)+\frac{1}{u-d}\Bigl({\cal V}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})-\frac{{\cal T}\_{n}^{i,p}}{{\cal T}\_{n}}{\cal V}\_{n-1}({\bf{s}},y)\Bigr). |  | ( 3.20) |

Moreover, there exists a positive constant 𝒞n−1{\cal C}\_{n-1} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|1𝒩​∑p=1m∑i=1Npϕ^n−1i,p​(𝐒n−1,Yn−1,Zn−1i,p,ϱip)−Ln−1​(𝐒n−1,Yn−1)|2≤𝒞n−1𝒩\mathbb{E}\Bigl|\frac{1}{{\cal N}}\sum\_{p=1}^{m}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}({\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i,p},\varrho\_{i}^{p})-L\_{n-1}({\bf{S}}^{n-1},Y\_{n-1})\Bigr|^{2}\leq\frac{{\cal C}\_{n-1}}{{\cal N}} |  |

for every 1≤n≤N1\leq n\leq N, which establishes the convergence rate in the large population limit.

###### Proof.

Since, for each p=1,…,mp=1,\ldots,m, (Zi,p,ϱip),i∈ℕ(Z^{i,p},\varrho\_{i}^{p}),i\in\mathbb{N} are i.i.d. and also independent of (S,Y)(S,Y),
the market-clearing condition in Definition [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmdefinition2 "Definition 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") is equivalently given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑p=1mwp​𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)]=Ln−1​(𝐬,y)\sum\_{p=1}^{m}w\_{p}\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z^{1,p}\_{n-1},\varrho\_{1}^{p})\bigr]=L\_{n-1}({\bf{s}},y) |  | ( 3.21) |

for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N. The expression for the transition
probabilities ([3.19](https://arxiv.org/html/2512.21621v1#S3.E19 "In Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-transition}) is a direct consequence of ([3.8](https://arxiv.org/html/2512.21621v1#S3.E8 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-exp}) in Theorem [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
and the market-clearing condition ([3.21](https://arxiv.org/html/2512.21621v1#S3.E21 "In Proof. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-condition}).
By substituting the resulting expression for pn−1​(𝐬,y)p\_{n-1}({\bf{s}},y) (and qn−1​(𝐬,y)q\_{n-1}({\bf{s}},y)) into ([3.6](https://arxiv.org/html/2512.21621v1#S3.E6 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal})
(or equivalently ([3.18](https://arxiv.org/html/2512.21621v1#S3.E18 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{optimal-with-effective})), we obtain the desired equality ([3.20](https://arxiv.org/html/2512.21621v1#S3.E20 "In Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-optimal}).

To establish the first claim, it suffices to verify that the family of transition probabilities
(pn−1​(𝐬,y))n=1N(p\_{n-1}({\bf{s}},y))\_{n=1}^{N} defined in ([3.19](https://arxiv.org/html/2512.21621v1#S3.E19 "In Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-transition}) satisfies the bound given by (vi)
in Assumption [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), while updating the functions (fn−1p)(f\_{n-1}^{p}) via the backward induction
process described in Theorem [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). At t=tN−1t=t\_{N-1}, fN−1p,p=1,…,mf\_{N-1}^{p},p=1,\ldots,m
are measurable functions satisfying the uniform bounds c¯N≤fN−1p≤C¯N\overline{c}\_{N}\leq f\_{N-1}^{p}\leq\overline{C}\_{N}
on their respective domains for some positive constants c¯N\overline{c}\_{N} and C¯N\overline{C}\_{N} due to the
boundedness assumption on FpF^{p}. This makes 𝒱N−1{\cal V}\_{N-1} a bounded function on 𝒮N−1×𝒴N−1{\cal S}^{N-1}\times{\cal Y}\_{N-1}.
Moreover, LN−1L\_{N-1} and 1/𝒯N1/{\cal T}\_{N} are bounded. Combined with the fact d<0<ud<0<u, we can confirm
that pN−1p\_{N-1} (and hence qN−1q\_{N-1}) given by ([3.19](https://arxiv.org/html/2512.21621v1#S3.E19 "In Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-transition}) satisfies
0<pN−1​(𝐬,y),qN−1​(𝐬,y)<10<p\_{N-1}({\bf{s}},y),q\_{N-1}({\bf{s}},y)<1 for every (𝐬,y)∈𝒮N−1×𝒴N−1({\bf{s}},y)\in{\cal S}^{N-1}\times{\cal Y}\_{N-1}, and is thus consistent with
Assumption [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") (vi).
Then it is easy to observe that ϕ^N−1i,p\widehat{\phi}\_{N-1}^{i,p} is bounded on its domain by the expression ([3.18](https://arxiv.org/html/2512.21621v1#S3.E18 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{optimal-with-effective}).
Then, using the formula ([3.10](https://arxiv.org/html/2512.21621v1#S3.E10 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-Vnm1}), VN−1p,p=1,…,mV\_{N-1}^{p},p=1,\ldots,m are shown to
satisfy the uniform bounds cN−1≤VN−1p≤CN−1c\_{N-1}\leq V\_{N-1}^{p}\leq C\_{N-1} on their respective domains
for some positive constants cN−1c\_{N-1} and CN−1C\_{N-1}.
This in turn ensures that fN−2p,p=1,…,mf\_{N-2}^{p},p=1,\ldots,m once again satisfy the desired properties, and so do
(pN−2​(𝐬,y),qN−2​(𝐬,y))(p\_{N-2}({\bf{s}},y),q\_{N-2}({\bf{s}},y)), (𝐬,y)∈𝒮N−2×𝒴N−2({\bf{s}},y)\in{\cal S}^{N-2}\times{\cal Y}\_{N-2}. Proceeding in this way,
by backward induction, we establish the desired consistency for every time step.

To establish the second claim, it suffices to prove that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|1𝒩​∑p=1m∑i=1Npϕ^n−1i,p​(𝐬,y,Zn−1i,p,ϱip)−Ln−1​(𝐬,y)|2≤𝒞n−1𝒩\mathbb{E}\Bigl|\frac{1}{{\cal N}}\sum\_{p=1}^{m}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{i,p},\varrho\_{i}^{p})-L\_{n-1}({\bf{s}},y)\Bigr|^{2}\leq\frac{{\cal C}\_{n-1}}{{\cal N}} |  |

holds uniformly for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}.
Using the equilibrium condition ([3.21](https://arxiv.org/html/2512.21621v1#S3.E21 "In Proof. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-condition}), it is useful to observe that

|  |  |  |
| --- | --- | --- |
|  | 1𝒩​∑p=1m∑i=1Npϕ^n−1i,p​(𝐬,y,Zn−1i,p,ϱip)−Ln−1​(𝐬,y)=∑p=1mwp​(1Np​∑i=1Npϕ^n−1i,p​(𝐬,y,Zn−1i,p,ϱip)−𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)]).\begin{split}&\frac{1}{{\cal N}}\sum\_{p=1}^{m}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,Z^{i,p}\_{n-1},\varrho\_{i}^{p})-L\_{n-1}({\bf{s}},y)\\ &=\sum\_{p=1}^{m}w\_{p}\left(\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,Z^{i,p}\_{n-1},\varrho\_{i}^{p})-\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr]\right).\end{split} |  |

Since the term inside the parenthesis for each pp is the average of centered i.i.d. random variables with finite variance
(guaranteed by the boundedness of the effective variables), the desired convergence rate follows from
the standard law of large numbers arguments used in Theorem [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). Equivalently, one can also use the expression
([3.20](https://arxiv.org/html/2512.21621v1#S3.E20 "In Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-optimal}) with the relations ([3.16](https://arxiv.org/html/2512.21621v1#S3.E16 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{effective-conv-1}) and ([3.17](https://arxiv.org/html/2512.21621v1#S3.E17 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{effective-conv-2}).
∎

###### Remark 3.2 (Economic Interpretation of the Equilibrium Strategy).

The expression ([3.20](https://arxiv.org/html/2512.21621v1#S3.E20 "In Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-mc-optimal}) provides a clear economic interpretation of the equilibrium strategy.
It can be decomposed into two distinct components:

|  |  |  |
| --- | --- | --- |
|  | ϕ^n−1i,p=𝒯ni,p𝒯n​Ln−1⏟(I) Supply Distribution+1u−d​(𝒱n−1i,p−𝒯ni,p𝒯n​𝒱n−1)⏟(II) Hedge Distribution.\widehat{\phi}^{i,p}\_{n-1}=\underbrace{\frac{{\cal T}\_{n}^{i,p}}{{\cal T}\_{n}}L\_{n-1}}\_{\text{(I) Supply Distribution}}+\underbrace{\frac{1}{u-d}\Bigl({\cal V}\_{n-1}^{i,p}-\frac{{\cal T}\_{n}^{i,p}}{{\cal T}\_{n}}{\cal V}\_{n-1}\Bigr)}\_{\text{(II) Hedge Distribution}}. |  |

* (I)

  The first term represents the sharing of the external supply Ln−1L\_{n-1}.
  Each agent absorbs a portion of the supply proportional to their effective risk tolerance 𝒯ni,p{\cal T}\_{n}^{i,p}
  relative to the market aggregate 𝒯n{\cal T}\_{n}. Note that the network effect Θ\Theta modifies the
  effective tolerance.
* (II)

  The second term corresponds to the hedging demand against the effective liability at tnt\_{n}.
  Since 𝒱n−1i,p{\cal V}\_{n-1}^{i,p} represents the sensitivity of the liability (normalized by risk aversion),
  the term 𝒱n−1i,p/(u−d){\cal V}\_{n-1}^{i,p}/(u-d) essentially corresponds to the Delta hedge required for agent-(i,p)(i,p).
  However, since the market must clear, agents cannot simply hold their desired hedge.
  Instead, the aggregate hedging demand of the market, 𝒱n−1/(u−d){\cal V}\_{n-1}/(u-d), is redistributed back to the agents
  according to their risk tolerance shares.

This decomposition of the equilibrium strategy is universal: one can confirm that the same relation holds
for ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}) in Theorem [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), although the θ\theta-dependent terms in (II)
cancel out in the single population case.

### 3.5 Market-clearing mean-field equilibrium when dim​Ker​(I−Θ)=1\mathrm{dim}~\mathrm{Ker}(I-\Theta)=1

From the definition of the effective variables in ([3.15](https://arxiv.org/html/2512.21621v1#S3.E15 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-effective-variables}), if some eigenvalues
(λk,1≤k≤m)(\lambda\_{k},1\leq k\leq m) of (I−Θ)(I-\Theta) approach zero, we can reasonably expect that the effective
risk tolerance diverges, rendering the relative performance game ill-defined.
However, as observed in the single-population case (Theorem [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")),
we may recover the equilibrium with appropriate transition probabilities of the stock price
by imposing the market-clearing condition, which precludes the divergence of the agents’ positions.
In this subsection, we demonstrate that this is indeed the case when dim​Ker​(I−Θ)=1{\rm dim}~{\rm Ker}(I-\Theta)=1.
This single dimension of the kernel corresponds to the existence of only one closed loop
(e.g., population-a→a\to population-b→…→b\to\dots\to population-aa)
where the feedback effect of relative performance concerns diverges.
We also show that there is generally no RP-MFE when dim​Ker​(I−Θ)≥2{\rm dim}~{\rm Ker}(I-\Theta)\geq 2.
Let us recall the definition of the pseudo inverse, (I−Θ)†(I-\Theta)^{\dagger}:

|  |  |  |
| --- | --- | --- |
|  | (I−Θ)†:=((I−Θ)|Ker​(I−Θ)⟂)−1:Im​(I−Θ)→Ker​(I−Θ)⟂.(I-\Theta)^{\dagger}:=\Bigl((I-\Theta)\bigr|\_{\mathrm{Ker}(I-\Theta)^{\perp}}\Bigr)^{-1}:\mathrm{Im}(I-\Theta)\rightarrow\mathrm{Ker}(I-\Theta)^{\perp}. |  |

In general, for a matrix AA and 𝒙∈Im​(A)\bm{x}\in\mathrm{Im}(A), A†​𝒙A^{\dagger}\bm{x} is the minimal
norm solution to the equation A​𝒚=𝒙A\bm{y}=\bm{x} and we clearly have A​A†​x=xAA^{\dagger}x=x.
On the other hand, A†​A​𝒙A^{\dagger}A\bm{x} gives the projection of 𝒙\bm{x} onto Ker​(A)⟂\mathrm{Ker}(A)^{\perp} for any 𝒙\bm{x}.
For general properties of pseudo inverse operators, see, e.g., [[42](https://arxiv.org/html/2512.21621v1#bib.bib42)][Appendix C].

We introduce the following notation for 1≤p≤m1\leq p\leq m and i∈ℕi\in\mathbb{N}, which is slightly different from that defined in
([3.15](https://arxiv.org/html/2512.21621v1#S3.E15 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-effective-variables}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯̊ni,p:=1γni,p,𝒯̊np:=𝔼1,p​[1γn1,p],𝒱̊n−1i,p​(𝐬,y,zi,p,ϱip):=log⁡fn−1p​(𝐬,y,zi,p,ϱip)γni,p,𝒱̊n−1p​(𝐬,y):=𝔼1,p​[log⁡fn−1p​(𝐬,y,Zn−11,p,ϱ1p)γn1,p],\begin{split}&\mathring{{\cal T}}\_{n}^{i,p}:=\frac{1}{\gamma\_{n}^{i,p}},\hskip 56.9055pt\mathring{{\cal T}}\_{n}^{p}:=\mathbb{E}^{1,p}\Bigl[\frac{1}{\gamma\_{n}^{1,p}}\Bigr],\\ &\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\frac{\log f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})}{\gamma\_{n}^{i,p}},\quad\mathring{{\cal V}}\_{n-1}^{p}({\bf{s}},y):=\mathbb{E}^{1,p}\Bigl[\frac{\log f\_{n-1}^{p}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})}{\gamma\_{n}^{1,p}}\Bigr],\end{split} |  | ( 3.22) |

for each (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}.
The functions fn−1p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝf\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, p=1,…,mp=1,\ldots,m
are defined as in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). Their complete determination by backward induction will be
detailed in the following theorem. The functions 𝒱̊n−1:𝒮n−1×𝒴n−1→ℝ\mathring{{\cal V}}\_{n-1}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R}
and 𝒱̊n−1i,p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝ\mathring{{\cal V}}\_{n-1}^{i,p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
are bounded measurable functions. Although the superscript ii in 𝒱̊n−1i,p\mathring{{\cal V}}\_{n-1}^{i,p} is redundant,
since the dependence on γni,p\gamma\_{n}^{i,p} is incorporated by the argument ϱip:=(γip,(θp,ki)k=1m)\varrho\_{i}^{p}:=(\gamma\_{i}^{p},(\theta^{i}\_{p,k})\_{k=1}^{m}),
we retain it to clearly associate the variable with the relevant agent as before.
We also introduce the vector notations 𝓣̊n:=(𝒯̊np)p=1m\mathring{\bm{{\cal T}}}\_{n}:=(\mathring{{\cal T}}\_{n}^{p})\_{p=1}^{m} and
𝓥̊n−1​(𝐬,y):=(𝒱̊n−1p​(𝐬,y))p=1m\mathring{\bm{{\cal V}}}\_{n-1}(\mathbf{s},y):=(\mathring{{\cal V}}\_{n-1}^{p}(\mathbf{s},y))\_{p=1}^{m}.
In addition to the matrix notation explained in the previous subsection, we use the notation (𝒖,𝒗)(\bm{u},\bm{v})
to denote the inner product between any mm-dimensional vectors 𝒖\bm{u} and 𝒗\bm{v}.
We use 𝒘=(wp)p=1m∈ℝm\bm{w}=(w\_{p})\_{p=1}^{m}\in\mathbb{R}^{m} to denote the vector of relative population size.

###### Theorem 3.3.

Suppose that Assumptions [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmassumption3 "Assumption 3.3. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") hold.
Furthermore, we assume that dimKer​(I−Θ)=1\dim\mathrm{Ker}(I-\Theta)=1.
Let 𝐯\bm{v} and 𝛋\bm{\kappa} be unit vectors such that 𝐯∈Ker​((I−Θ)⊤)\bm{v}\in{\rm Ker}((I-\Theta)^{\top}) and 𝛋∈Ker​(I−Θ)\bm{\kappa}\in\mathrm{Ker}(I-\Theta), respectively.
We assume that they satisfy the non-degeneracy conditions (𝐯,𝓣̊N)≠0(\bm{v},\mathring{\bm{{\cal T}}}\_{N})\neq 0 and (𝐰,𝛋)≠0(\bm{w},\bm{\kappa})\neq 0.
Then there exists a unique MC-MFE. The associated equilibrium transition probabilities of the stock price are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn−1​(𝐬,y)=(−d)/{u​exp⁡((𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n))−d}p\_{n-1}({\bf{s}},y)=(-d)\Big/\left\{u\exp\left(\frac{\bigl(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)\bigr)}{\bigl(\bm{v},\mathring{\bm{{\cal T}}}\_{n}\bigr)}\right)-d\right\} |  | ( 3.23) |

for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
For each population p=1,…,mp=1,\ldots,m, the equilibrium strategy of agent-(i,p)(i,p), (ϕ^n−1i,p)n=1N(\widehat{\phi}^{i,p}\_{n-1})\_{n=1}^{N},
is given by the bounded measurable function ϕ^i,p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝ\widehat{\phi}^{i,p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)=(θi​𝜿)p(𝒘,𝜿)​Ln−1​(𝐬,y)+1u−d​{𝒰n−1i,p​(𝐬,y,zi,p,ϱip)+(θi​(I−Θ)†​𝓤n−1​(𝐬,y))p−(θi​𝜿)p(𝒘,𝜿)​𝒘⊤​(I−Θ)†​𝓤n−1​(𝐬,y)},\begin{split}&\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})=\frac{(\theta^{i}\bm{\kappa})\_{p}}{(\bm{w},\bm{\kappa})}L\_{n-1}({\bf{s}},y)\\ &+\frac{1}{u-d}\Bigl\{{\cal U}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})+\bigl(\theta^{i}(I-\Theta)^{\dagger}\bm{{\cal U}}\_{n-1}({\bf{s}},y)\bigr)\_{p}-\frac{(\theta^{i}\bm{\kappa})\_{p}}{(\bm{w},\bm{\kappa})}\bm{w}^{\top}(I-\Theta)^{\dagger}\bm{{\cal U}}\_{n-1}({\bf{s}},y)\Bigr\},\end{split} |  | ( 3.24) |

where 𝐰=(wp)p=1m∈ℝm\bm{w}=(w\_{p})\_{p=1}^{m}\in\mathbb{R}^{m} is the vector of relative population size. The bounded measurable
functions 𝒰n−1i,p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝ{\cal U}\_{n-1}^{i,p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
and 𝒰n−1p:𝒮n−1×𝒴n−1→ℝ{\cal U}\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R}, p=1,…,mp=1,\ldots,m are defined by

|  |  |  |
| --- | --- | --- |
|  | 𝒰n−1i,p​(𝐬,y,zi,p,ϱip):=𝒱̊n−1i,p​(𝐬,y,zi,p,ϱip)−(𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n)​𝒯̊ni,p,𝒰n−1p​(𝐬,y):=𝒱̊n−1p​(𝐬,y)−(𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n)​𝒯̊np.\begin{split}{\cal U}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})&:=\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{{\cal T}}\_{n}^{i,p},\\ {\cal U}\_{n-1}^{p}({\bf{s}},y)&:=\mathring{{\cal V}}\_{n-1}^{p}({\bf{s}},y)-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{{\cal T}}\_{n}^{p}.\end{split} |  |

We denote the vector formed by the latter components as 𝓤n−1​(𝐬,y):=(𝒰n−1p​(𝐬,y))p=1m\bm{\mathcal{U}}\_{n-1}(\mathbf{s},y):=(\mathcal{U}\_{n-1}^{p}(\mathbf{s},y))\_{p=1}^{m}.
Here, for each 1≤n≤N1\leq n\leq N, the functions fn−1p:𝒮n−1×𝒴n−1×𝒵n−1p×Γp→ℝf\_{n-1}^{p}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}\rightarrow\mathbb{R},
p=1,…,mp=1,\ldots,m, which are components of (𝒱̊n−1i,k,𝒱̊n−1k,𝒰n−1i,k,𝒰n−1k)(\mathring{{\cal V}}^{i,k}\_{n-1},\mathring{{\cal V}}^{k}\_{n-1},{\cal U}\_{n-1}^{i,k},{\cal U}\_{n-1}^{k}),
are measurable functions satisfying the uniform bounds 0<c¯n≤fn−1p≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n}<\infty
for some positive constants c¯n\overline{c}\_{n} and C¯n\overline{C}\_{n}. They are determined by the backward induction as in Theorem [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"):
We use the same terminal condition VNp​(𝐬,y,zi,p,ϱip):=exp⁡(γip​Fp​(𝐬,y,zi,p))V\_{N}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\exp\bigl(\gamma\_{i}^{p}F^{p}({\bf{s}},y,z^{i,p})\bigr)
and the formulas ([3.9](https://arxiv.org/html/2512.21621v1#S3.E9 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-fnm1-update}) and ([3.10](https://arxiv.org/html/2512.21621v1#S3.E10 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-Vnm1}),
replacing the transition probabilities (pn−1​(𝐬,y),qn−1​(𝐬,y))n=1N(p\_{n-1}({\bf{s}},y),q\_{n-1}({\bf{s}},y))\_{n=1}^{N} and the optimal control (ϕ^n−1i,p)n=1N(\widehat{\phi}^{i,p}\_{n-1})\_{n=1}^{N}
with those given above at each step.
The dynamics of the associated mean-field terms (μ^np)n=1N(\widehat{\mu}\_{n}^{p})\_{n=1}^{N} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^np​((𝐬​u~)n,𝐲)=β​μ^n−1p​(𝐬,𝐲−)+u​𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)],μ^np​((𝐬​d~)n,𝐲)=β​μ^n−1p​(𝐬,𝐲−)+d​𝔼1,p​[ϕ^n−11,p​(𝐬,y,Zn−11,p,ϱ1p)],\begin{split}&\widehat{\mu}\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})=\beta\widehat{\mu}^{p}\_{n-1}({\bf{s}},{\bf{y}}^{-})+u\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\\ &\widehat{\mu}\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})=\beta\widehat{\mu}^{p}\_{n-1}({\bf{s}},{\bf{y}}^{-})+d\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\end{split} |  | ( 3.25) |

with

|  |  |  |
| --- | --- | --- |
|  | 𝔼1,p​[ϕ^1,p​(𝐬,y,Zn−11,p,ϱ1p)]=κp(𝒘,𝜿)​Ln−1​(𝐬,y)+1u−d​{((I−Θ)†​𝒰n−1​(𝐬,y))p−κp(𝒘,𝜿)​𝒘⊤​(I−Θ)†​𝒰n−1​(𝐬,y)}.\begin{split}&\mathbb{E}^{1,p}\bigl[\widehat{\phi}^{1,p}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr]\\ &\quad=\frac{\kappa\_{p}}{(\bm{w},\bm{\kappa})}L\_{n-1}({\bf{s}},y)+\frac{1}{u-d}\Bigl\{\bigl((I-\Theta)^{\dagger}{\cal U}\_{n-1}({\bf{s}},y)\bigr)\_{p}-\frac{\kappa\_{p}}{(\bm{w},\bm{\kappa})}\bm{w}^{\top}(I-\Theta)^{\dagger}{\cal U}\_{n-1}({\bf{s}},y)\Bigr\}.\end{split} |  |

under the initial condition μ0p:=𝔼1,p​[ξ1p]\mu\_{0}^{p}:=\mathbb{E}^{1,p}[\xi\_{1}^{p}].
Moreover, there exists a positive constant 𝒞n−1{\cal C}\_{n-1} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|1𝒩​∑p=1m∑i=1Npϕ^n−1i,p​(𝐒n−1,Yn−1,Zn−1i,p,ϱip)−Ln−1​(𝐒n−1,Yn−1)|2≤𝒞n−1𝒩\mathbb{E}\Bigl|\frac{1}{{\cal N}}\sum\_{p=1}^{m}\sum\_{i=1}^{N\_{p}}\widehat{\phi}^{i,p}\_{n-1}({\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i,p},\varrho\_{i}^{p})-L\_{n-1}({\bf{S}}^{n-1},Y\_{n-1})\Bigr|^{2}\leq\frac{{\cal C}\_{n-1}}{{\cal N}} |  |

for every 1≤n≤N1\leq n\leq N, which establishes the convergence rate in the large population limit.

###### Proof.

We proceed as in the proof for Theorem [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
We suppose that, for every p=1,…,mp=1,\ldots,m, the problem for agent-(i,p)(i,p) at tn−1t\_{n-1} for the period [tn−1,tn][t\_{n-1},t\_{n}] is given by the
form ([3.2](https://arxiv.org/html/2512.21621v1#S3.E2 "In 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{problem-multi-tmp}). To apply Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we hypothesize
that the measurable function Vnp:𝒮n×𝒴n×𝒵np×Γp→ℝV\_{n}^{p}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}^{p}\times\Gamma^{p}\rightarrow\mathbb{R}
satisfies the uniform bounds cn≤Vnp≤Cnc\_{n}\leq V\_{n}^{p}\leq C\_{n} for some positive constants cnc\_{n} and CnC\_{n}.
This ensures that the function fn−1pf\_{n-1}^{p} also satisfies the desired uniform bounds.
This clearly holds at t=tN−1t=t\_{N-1} for the last interval [tN−1,tN][t\_{N-1},t\_{N}]
with VNp​(𝐬,y,zi,p,ϱip):=exp⁡(γip​Fp​(𝐬,y,zi,p))V\_{N}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}):=\exp\bigl(\gamma\_{i}^{p}F^{p}({\bf{s}},y,z^{i,p})\bigr).

Using ([3.3](https://arxiv.org/html/2512.21621v1#S3.E3 "In Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal-tmp}) in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), the evolution of the wealth process of agent-(i,p)(i,p)
under the optimal strategy ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} is given by

|  |  |  |
| --- | --- | --- |
|  | Xn(i,p),∗=β​Xn−1(i,p),∗+ϕn−1(i,p),∗​(𝐒n−1,𝐘n−1,Zn−1i,p,ϱip)​Rn.X\_{n}^{(i,p),\*}=\beta X\_{n-1}^{(i,p),\*}+\phi^{(i,p),\*}\_{n-1}({\bf{S}}^{n-1},{\bf{Y}}^{n-1},Z\_{n-1}^{i,p},\varrho\_{i}^{p})R\_{n}. |  |

Consider the problem conditioned on the event {(𝐒n−1,𝐘n−1)=(𝐬,𝐲)}\{({\bf{S}}^{n-1},{\bf{Y}}^{n-1})=({\bf{s}},{\bf{y}})\} in ℱtn−10{\cal F}^{0}\_{t\_{n-1}}.
Under the induction hypothesis that 𝔼0,(1,p)​[Xn−1(1,p),∗|𝐬,𝐲]\mathbb{E}^{0,(1,p)}[X^{(1,p),\*}\_{n-1}|{\bf{s}},{\bf{y}}] is given by the form μn−1p​(𝐬,𝐲−)\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-})
with (𝐬,𝐲−)∈𝒮n−1×𝒴n−2({\bf{s}},{\bf{y}}^{-})\in{\cal S}^{n-1}\times{\cal Y}^{n-2} (when n=1n=1, we simply set μ0p=𝔼1,p​[ξ1p]\mu\_{0}^{p}=\mathbb{E}^{1,p}[\xi\_{1}^{p}]),
using the i.i.d. property of the variables (ϱip,Zi,p),i=1,2,…(\varrho\_{i}^{p},Z^{i,p}),i=1,2,\ldots, the fixed point condition ([3.5](https://arxiv.org/html/2512.21621v1#S3.E5 "In Definition 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-multi-mu})
for the RP-MFE for the period [tn−1,tn][t\_{n-1},t\_{n}] is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μnp​((𝐬​u~)n,𝐲)=β​μn−1p​(𝐬,𝐲−)+u​𝔼1,p​[ϕn−1(1,p),∗​(𝐬,𝐲,Zn−11,p,ϱ1p)],μnp​((𝐬​d~)n,𝐲)=β​μn−1p​(𝐬,𝐲−)+d​𝔼1,p​[ϕn−1(1,p),∗​(𝐬,𝐲,Zn−11,p,ϱ1p)],\begin{split}&\mu\_{n}^{p}(({\bf{s}}\widetilde{u})^{n},{\bf{y}})=\beta\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-})+u\mathbb{E}^{1,p}\bigl[\phi^{(1,p),\*}\_{n-1}({\bf{s}},{\bf{y}},Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\\ &\mu\_{n}^{p}(({\bf{s}}\widetilde{d})^{n},{\bf{y}})=\beta\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-})+d\mathbb{E}^{1,p}\bigl[\phi^{(1,p),\*}\_{n-1}({\bf{s}},{\bf{y}},Z\_{n-1}^{1,p},\varrho\_{1}^{p})\bigr],\end{split} |  | ( 3.26) |

which is equal to ([3.11](https://arxiv.org/html/2512.21621v1#S3.E11 "In Proof. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-RP-MFE-eq}).
Taking the difference on both sides,
and defining the vectors 𝓣̊n:=(𝒯̊np)p=1m\mathring{\bm{{\cal T}}}\_{n}:=(\mathring{{\cal T}}\_{n}^{p})\_{p=1}^{m}
and 𝓥̊n−1​(𝐬,y):=(𝒱̊n−1p​(𝐬,y))p=1m\mathring{\bm{{\cal V}}}\_{n-1}(\mathbf{s},y):=(\mathring{{\cal V}}\_{n-1}^{p}(\mathbf{s},y))\_{p=1}^{m},
we obtain ([3.12](https://arxiv.org/html/2512.21621v1#S3.E12 "In Proof. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-mfe-consistency}), or equivalently, for the relative performance equilibrium, the equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−Θ)​𝚫n​(𝐬,𝐲)=log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​𝓣̊n+𝓥̊n−1​(𝐬,y)(I-\Theta)\bm{\Delta}\_{n}({\bf{s}},{\bf{y}})=\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)\mathring{\bm{{\cal T}}}\_{n}+\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y) |  | ( 3.27) |

must hold for every (𝐬,𝐲)∈𝒮n−1×𝒴n−1({\bf{s}},{\bf{y}})\in{\cal S}^{n-1}\times{\cal Y}^{n-1}.
For this equation to have a solution, the right-hand side must be in Im​(I−Θ)\mathrm{Im}(I-\Theta).
By the Fredholm theorem, since Im​(I−Θ)=(Ker​(I−Θ)⊤)⟂\mathrm{Im}(I-\Theta)=\bigl(\mathrm{Ker}(I-\Theta)^{\top}\bigr)^{\perp},
this is the case if and only if

|  |  |  |
| --- | --- | --- |
|  | log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​(𝒗,𝓣̊n)+(𝒗,𝓥̊n−1​(𝐬,y))=0\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)(\bm{v},\mathring{\bm{{\cal T}}}\_{n})+(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))=0 |  |

for a vector 𝒗∈Ker​(I−Θ)⊤\bm{v}\in\mathrm{Ker}(I-\Theta)^{\top}. We normalize it as ‖𝒗‖=1\|\bm{v}\|=1.
Note that dimKer​(I−Θ)⊤=dimKer​(I−Θ)=1\dim\mathrm{Ker}(I-\Theta)^{\top}=\dim\mathrm{Ker}(I-\Theta)=1 since (I−Θ)(I-\Theta) is a square matrix.
This uniquely fixes the form of pn−1​(𝐬,y)p\_{n-1}({\bf{s}},y) (and hence qn−1​(𝐬,y)q\_{n-1}({\bf{s}},y)) as in ([3.23](https://arxiv.org/html/2512.21621v1#S3.E23 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-transition-kernel}).
Note that (𝒗,𝓣̊n)≠0(\bm{v},\mathring{\bm{{\cal T}}}\_{n})\neq 0 for every nn. The uniform bounds 0<c¯n≤fn−1p≤C¯n<∞0<\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n}<\infty ensure that
0<pn−1​(𝐬,y),qn−1​(𝐬,y)<10<p\_{n-1}({\bf{s}},y),q\_{n-1}({\bf{s}},y)<1 for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}.
In this case, a general solution to ([3.27](https://arxiv.org/html/2512.21621v1#S3.E27 "In Proof. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{eq-rp-condition}) can be written in the following form:

|  |  |  |
| --- | --- | --- |
|  | 𝚫n​(𝐬,𝐲)=(I−Θ)†​{𝓥̊n−1​(𝐬,y)−(𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n)​𝓣̊n}+δn​(𝐬,𝐲)​𝜿,\bm{\Delta}\_{n}({\bf{s}},{\bf{y}})=(I-\Theta)^{\dagger}\Bigl\{\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{\bm{{\cal T}}}\_{n}\Bigr\}+\delta\_{n}({\bf{s}},{\bf{y}})\bm{\kappa}, |  |

where δn:𝒮n−1×𝒴n−1→ℝ\delta\_{n}:{\cal S}^{n-1}\times{\cal Y}^{n-1}\rightarrow\mathbb{R} is an arbitrary (bounded) measurable function
and 𝜿∈ℝm\bm{\kappa}\in\mathbb{R}^{m} is a unit vector with 𝜿∈Ker​(I−Θ)\bm{\kappa}\in\mathrm{Ker}(I-\Theta).
Substituting these results into the optimal strategy ([3.3](https://arxiv.org/html/2512.21621v1#S3.E3 "In Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-optimal-tmp}) in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1(i,p),∗​(𝐬,𝐲,zi,p,ϱip)=1u−d​(θi​(I−Θ)†​{𝓥̊n−1​(𝐬,y)−(𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n)​𝓣̊n})p+1u−d​{𝒱̊n−1i,p​(𝐬,y,zi,p,ϱip)−(𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n)​𝒯̊ni,p}+δn​(𝐬,𝐲)​(θi​𝜿)pu−d.\begin{split}&\phi^{(i,p),\*}\_{n-1}({\bf{s}},{\bf{y}},z^{i,p},\varrho\_{i}^{p})=\frac{1}{u-d}\left(\theta^{i}(I-\Theta)^{\dagger}\Bigl\{\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{\bm{{\cal T}}}\_{n}\Bigr\}\right)\_{p}\\ &\quad+\frac{1}{u-d}\Bigl\{\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{{\cal T}}^{i,p}\_{n}\Bigr\}+\delta\_{n}({\bf{s}},{\bf{y}})\frac{(\theta^{i}\bm{\kappa})\_{p}}{u-d}.\end{split} |  | ( 3.28) |

Hence, with the transition probabilities given by ([3.23](https://arxiv.org/html/2512.21621v1#S3.E23 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-transition-kernel}),
the solution to the relative performance game for the period [tn−1,tn][t\_{n-1},t\_{n}] exists but it is not unique.
We also observe that the path-dependence 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1} in 𝚫n\bm{\Delta}\_{n} and ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} appears only through
the function δn​(𝐬,𝐲)\delta\_{n}({\bf{s}},{\bf{y}}).

The additional degree of freedom in the choice of δn\delta\_{n} is uniquely fixed by
imposing the market-clearing condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑p=1mwp​𝔼1,p​[ϕn−1(1,p),∗​(𝐬,y,Zn−11,p,ϱ1p)]=Ln−1​(𝐬,y).\sum\_{p=1}^{m}w\_{p}\mathbb{E}^{1,p}\bigl[\phi^{(1,p),\*}\_{n-1}({\bf{s}},y,Z^{1,p}\_{n-1},\varrho\_{1}^{p})\bigr]=L\_{n-1}({\bf{s}},y). |  | ( 3.29) |

From ([3.28](https://arxiv.org/html/2512.21621v1#S3.E28 "In Proof. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{optimal-kernel-1-tmp}) and ([3.29](https://arxiv.org/html/2512.21621v1#S3.E29 "In Proof. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-kernel-1-tmp}), it is straightforward to obtain

|  |  |  |
| --- | --- | --- |
|  | δn​(𝐬,y)=1(𝒘,𝜿)​{(u−d)​Ln−1​(𝐬,y)−𝒘⊤​(I−Θ)†​(𝓥̊n−1​(𝐬,y)−(𝒗,𝓥̊n−1​(𝐬,y))(𝒗,𝓣̊n)​𝓣̊n)},\begin{split}\delta\_{n}({\bf{s}},y)=\frac{1}{(\bm{w},\bm{\kappa})}\left\{(u-d)L\_{n-1}({\bf{s}},y)-\bm{w}^{\top}(I-\Theta)^{\dagger}\Bigl(\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{\bm{{\cal T}}}\_{n}\Bigr)\right\},\end{split} |  |

which only depends on the last element y∈𝒴n−1y\in{\cal Y}\_{n-1} in 𝐲∈𝒴n−1{\bf{y}}\in{\cal Y}^{n-1}.
Substituting this expression for δn\delta\_{n} into ([3.28](https://arxiv.org/html/2512.21621v1#S3.E28 "In Proof. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{optimal-kernel-1-tmp}),
we obtain ϕn−1(i,p),∗​(𝐬,y,zi,p,ϱip)\phi^{(i,p),\*}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}) in the form given in ([3.24](https://arxiv.org/html/2512.21621v1#S3.E24 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-optimal-kernel-1}).
Since (fn−1p)p=1m(f\_{n-1}^{p})\_{p=1}^{m} satisfies the uniform bounds c¯n≤fn−1p≤C¯n\overline{c}\_{n}\leq f\_{n-1}^{p}\leq\overline{C}\_{n}
due to the induction hypothesis on (Vnp)p=1m(V\_{n}^{p})\_{p=1}^{m},
the optimal control ϕn−1(i,p),∗\phi^{(i,p),\*}\_{n-1} and hence the mean-field term μnp\mu\_{n}^{p} are also given by bounded measurable functions.
Therefore, with a given bounded initial condition (μn−1p​(𝐬,𝐲−))p=1m(\mu\_{n-1}^{p}({\bf{s}},{\bf{y}}^{-}))\_{p=1}^{m},
the transition probabilities ([3.23](https://arxiv.org/html/2512.21621v1#S3.E23 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-transition-kernel}), the control ([3.24](https://arxiv.org/html/2512.21621v1#S3.E24 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-optimal-kernel-1}),
and the dynamics of the mean-field term ([3.25](https://arxiv.org/html/2512.21621v1#S3.E25 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-mu-kernel-1}) provide the unique solution
for MC-MFE for this period [tn−1,tn][t\_{n-1},t\_{n}].

In order to complete the proof, it suffices to show that this procedure can be repeated backward from the last interval [tN−1,tN][t\_{N-1},t\_{N}]
to the first one [t0,t1][t\_{0},t\_{1}]. The value function for the agent-(i,p)(i,p) at tn−1t\_{n-1}, which is the objective function
for the optimization for the period [tn−2,tn−1][t\_{n-2},t\_{n-1}], is given by the same formula ([3.14](https://arxiv.org/html/2512.21621v1#S3.E14 "In Proof. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{objective-tnm1})
with Vn−1pV\_{n-1}^{p} in ([3.10](https://arxiv.org/html/2512.21621v1#S3.E10 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-Vnm1}) with transition probabilities and ϕ^i,p\widehat{\phi}^{i,p} replaced by
those in ([3.23](https://arxiv.org/html/2512.21621v1#S3.E23 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-transition-kernel}) and ([3.24](https://arxiv.org/html/2512.21621v1#S3.E24 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-optimal-kernel-1}) derived above.
It is easy to confirm that Vn−1pV\_{n-1}^{p} once again satisfies the uniform bounds
cn−1≤Vn−1p≤Cn−1c\_{n-1}\leq V\_{n-1}^{p}\leq C\_{n-1} on its domain for some positive constants cn−1c\_{n-1} and Cn−1C\_{n-1}.
Hence we succeed in recovering the same form of problem as in Lemma [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3.2 Optimization problem ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
Hence we can proceed with the backward induction by one time step. The induction hypothesis of bounded measurability for μn−1p\mu\_{n-1}^{p} is reduced
to the constant μ0p:=𝔼1,p​[ξ1p]\mu\_{0}^{p}:=\mathbb{E}^{1,p}[\xi\_{1}^{p}] and is satisfied trivially.
The last claim on the convergence rate can be proved in the same way as in Theorem [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
∎

###### Remark 3.3.

From ([3.27](https://arxiv.org/html/2512.21621v1#S3.E27 "In Proof. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{eq-rp-condition}), one can observe that there is generally no equilibrium for
dK:=dimKer​(I−Θ)≥2d\_{K}:=\dim\mathrm{Ker}(I-\Theta)\geq 2. Specifically, in order to have a mean-field equilibrium,
we need to satisfy the solvability conditions for every basis vector 𝐯k∈Ker​((I−Θ)⊤)\bm{v}\_{k}\in\mathrm{Ker}((I-\Theta)^{\top}), 1≤k≤dK1\leq k\leq d\_{K}.
Since we only have a single scalar degree of freedom (the transition probability of the stock price)
to satisfy these dKd\_{K} independent constraints simultaneously, the system is overdetermined.
Thus, a solution exists only in highly degenerate cases where the vectors (𝓥̊n−1​(𝐬,y))(\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y))
coincidentally lie in the orthogonal complement of the kernel.
For instance, a trivial case is given where the liabilities (Fp)(F^{p}) and the external order flow (Ln)(L\_{n})
are independent of the stock price process. In this case, (fn−1p)(f^{p}\_{n-1}) and hence 𝓥̊n−1\mathring{\bm{{\cal V}}}\_{n-1} vanish,
and the transition probabilities become equal to those in the risk-neutral measure ℚ\mathbb{Q}, i.e.,

|  |  |  |
| --- | --- | --- |
|  | log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)=0.\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)=0. |  |

In this special situation, relative performance concerns become irrelevant due to the
independence of the mean-field term μ^\widehat{\mu} from the stock price.

###### Remark 3.4.

If we assume that the liabilities and external order flow depend only on the current state variables, i.e., take the form
Fp​(SN,YN,ZNi,p)F^{p}(S\_{N},Y\_{N},Z\_{N}^{i,p}) and Ln−1​(Sn−1,Yn−1)L\_{n-1}(S\_{n-1},Y\_{n-1}), then we can show that the equilibrium transition probabilities
and the controls in Theorems [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), and [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
become Markovian (path-independent) as shown in Theorems [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

### 3.6 Perturbation of the inverse (I−Θ​(ϵ))−1(I-\Theta(\epsilon))^{-1} around ϵ=0\epsilon=0

As observed in Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), a unique MC-MFE
exists when dim​Ker​(I−Θ)=1\mathrm{dim}~\mathrm{Ker}(I-\Theta)=1.
It is natural to expect that, similarly to the single-population case (Theorem [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")),
the market-clearing condition ensures that both the equilibrium transition probabilities (pn−1​(𝐬,y))(p\_{n-1}({\bf{s}},y))
and the equilibrium controls (ϕ^n−1i,p)(\widehat{\phi}^{i,p}\_{n-1}) exhibit continuous dependence
on the interaction matrix as it approaches the singular limit.
We assume that the unperturbed interaction matrix satisfies dim​Ker​(I−Θ)=1\mathrm{dim}~\mathrm{Ker}(I-\Theta)=1.
For simplicity, we consider a perturbation ϵ∈ℝ\epsilon\in\mathbb{R} of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θp,ki​(ϵ):=θp,ki−ϵ​δp,k,Θ​(ϵ):=Θ−ϵ​I\theta^{i}\_{p,k}(\epsilon):=\theta^{i}\_{p,k}-\epsilon\delta\_{p,k},\quad\Theta(\epsilon):=\Theta-\epsilon I |  | ( 3.30) |

for every p,k=1,…,mp,k=1,\ldots,m and i∈ℕi\in\mathbb{N}, where δp,k\delta\_{p,k} denotes the Kronecker delta . We need the following result:

###### Assumption 3.4.

dim​Ker​(I−Θ)=1\mathrm{dim}~\mathrm{Ker}(I-\Theta)=1 and the pole of the resolvent (I−Θ​(ϵ))−1(I-\Theta(\epsilon))^{-1} has a simple pole at ϵ=0\epsilon=0.

###### Lemma 3.2.

Let Assumption [3.4](https://arxiv.org/html/2512.21621v1#S3.Thmassumption4 "Assumption 3.4. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") be in force.
Let 𝐯\bm{v} and 𝛋\bm{\kappa} be mm-dimensional unit vectors satisfying 𝐯∈Ker​(I−Θ)⊤\bm{v}\in\mathrm{Ker}(I-\Theta)^{\top}
and 𝛋∈Ker​(I−Θ)\bm{\kappa}\in\mathrm{Ker}(I-\Theta).
Define the projection matrix PP and the pseudo inverse GG by

|  |  |  |
| --- | --- | --- |
|  | P:=I−𝜿​𝒗⊤(𝒗,𝜿),G:=(I−Θ)†.P:=I-\frac{\bm{\kappa}\bm{v}^{\top}}{(\bm{v},\bm{\kappa})},\quad G:=(I-\Theta)^{\dagger}. |  |

Then, for any ϵ\epsilon satisfying 0<|ϵ|<‖P​G‖−10<|\epsilon|<\|PG\|^{-1} and such that
(1+ϵ)(1+\epsilon) is in the resolvent set of Θ\Theta, the following expansion holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−Θ​(ϵ))−1=1ϵ​𝜿​𝒗⊤(𝒗,𝜿)+∑n=0∞(−ϵ)n​(P​G)n+1​P.(I-\Theta(\epsilon))^{-1}=\frac{1}{\epsilon}\frac{\bm{\kappa}\bm{v}^{\top}}{(\bm{v},\bm{\kappa})}+\sum\_{n=0}^{\infty}(-\epsilon)^{n}(PG)^{n+1}P. |  | ( 3.31) |

###### Remark.

Note that Assumption [3.4](https://arxiv.org/html/2512.21621v1#S3.Thmassumption4 "Assumption 3.4. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") implies (𝐯,𝛋)≠0(\bm{v},\bm{\kappa})\neq 0.

###### Proof.

Under Assumption [3.4](https://arxiv.org/html/2512.21621v1#S3.Thmassumption4 "Assumption 3.4. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), the resolvent has a simple pole at ϵ=0\epsilon=0.
Thus, we can postulate a Laurent expansion of the form:

|  |  |  |
| --- | --- | --- |
|  | (I−Θ​(ϵ))−1=1ϵ​R−1+R0+ϵ​R1+⋯.(I-\Theta(\epsilon))^{-1}=\frac{1}{\epsilon}R\_{-1}+R\_{0}+\epsilon R\_{1}+\cdots. |  |

We determine the coefficients (Ri)i=−1∞(R\_{i})\_{i=-1}^{\infty} using the identity (I−Θ​(ϵ))​(I−Θ​(ϵ))−1=I(I-\Theta(\epsilon))(I-\Theta(\epsilon))^{-1}=I.
Recall that I−Θ​(ϵ)=(I−Θ)+ϵ​II-\Theta(\epsilon)=(I-\Theta)+\epsilon I. Comparing terms of order ϵ−1\epsilon^{-1}, we get (I−Θ)​R−1=0(I-\Theta)R\_{-1}=0,
which implies R−1=𝜿​𝒄⊤R\_{-1}=\bm{\kappa}\bm{c}^{\top} for some vector 𝒄∈ℝm\bm{c}\in\mathbb{R}^{m}. Comparing terms of order ϵ0\epsilon^{0},
we have (I−Θ)​R0+R−1=I(I-\Theta)R\_{0}+R\_{-1}=I, or (I−Θ)​R0=I−R−1(I-\Theta)R\_{0}=I-R\_{-1}. Multiplying by 𝒗⊤\bm{v}^{\top} from the left,
and noting that 𝒗⊤​(I−Θ)=0\bm{v}^{\top}(I-\Theta)=0, we obtain 0=𝒗⊤−𝒗⊤​𝜿​𝒄⊤0=\bm{v}^{\top}-\bm{v}^{\top}\bm{\kappa}\bm{c}^{\top}.
This determines 𝒄⊤=𝒗⊤/(𝒗,𝜿)\bm{c}^{\top}=\bm{v}^{\top}/(\bm{v},\bm{\kappa}), yielding the residue R−1=(𝜿​𝒗⊤)/(𝒗,𝜿)R\_{-1}=(\bm{\kappa}\bm{v}^{\top})/(\bm{v},\bm{\kappa}).
Note that I−R−1=PI-R\_{-1}=P. Next, since R0R\_{0} is a solution to (I−Θ)​R0=P(I-\Theta)R\_{0}=P, it must take the form R0=G​P+𝜿​𝒄1⊤R\_{0}=GP+\bm{\kappa}\bm{c}\_{1}^{\top}
for some 𝒄1∈ℝm\bm{c}\_{1}\in\mathbb{R}^{m}. To determine 𝒄1\bm{c}\_{1}, we compare terms of order ϵ1\epsilon^{1}. We have (I−Θ)​R1+R0=0(I-\Theta)R\_{1}+R\_{0}=0,
or (I−Θ)​R1=−R0(I-\Theta)R\_{1}=-R\_{0}. Multiplying by 𝒗⊤\bm{v}^{\top} from the left yields the condition
𝒗⊤​R0=0\bm{v}^{\top}R\_{0}=0. Substituting the expression for R0R\_{0}, we obtain
𝒗⊤​(G​P+𝜿​𝒄1⊤)=0\bm{v}^{\top}(GP+\bm{\kappa}\bm{c}\_{1}^{\top})=0.
This uniquely determines 𝒄1⊤\bm{c}\_{1}^{\top} as 𝒄1⊤=−𝒗⊤​G​P(𝒗,𝜿)\bm{c}\_{1}^{\top}=-\frac{\bm{v}^{\top}GP}{(\bm{v},\bm{\kappa})}.
Substituting this back into the expression for R0R\_{0}, we obtain

|  |  |  |
| --- | --- | --- |
|  | R0=G​P−𝜿​𝒗⊤(𝒗,𝜿)​G​P=(I−𝜿​𝒗⊤(𝒗,𝜿))​G​P=P​G​P.R\_{0}=GP-\frac{\bm{\kappa}\bm{v}^{\top}}{(\bm{v},\bm{\kappa})}GP=\Bigl(I-\frac{\bm{\kappa}\bm{v}^{\top}}{(\bm{v},\bm{\kappa})}\Bigr)GP=PGP. |  |

Proceeding inductively, requiring the existence of higher-order terms leads to the relation Rn=(−1)n​(P​G)n+1​PR\_{n}=(-1)^{n}(PG)^{n+1}P.
The series converges in the operator norm under the condition |ϵ|​‖P​G‖<1|\epsilon|\|PG\|<1.
∎

Note that, for any 𝒙∈ℝm\bm{x}\in\mathbb{R}^{m}, we have (𝒗,P​𝒙)=0(\bm{v},P\bm{x})=0.
Since Im​(I−Θ)=(Ker​(I−Θ)⊤)⟂={𝒚∈ℝm∣(𝒗,𝒚)=0}\mathrm{Im}(I-\Theta)=(\mathrm{Ker}(I-\Theta)^{\top})^{\perp}=\{\bm{y}\in\mathbb{R}^{m}\mid(\bm{v},\bm{y})=0\},
the matrix PP serves as the projection operator onto the image space Im​(I−Θ)\mathrm{Im}(I-\Theta)
along the kernel direction 𝜿\bm{\kappa}.

###### Theorem 3.4.

Suppose that the assumptions of Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") hold.
Furthermore, let Assumption [3.4](https://arxiv.org/html/2512.21621v1#S3.Thmassumption4 "Assumption 3.4. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") be in force.
Choose η0>0\eta\_{0}>0 sufficiently small such that, for all |ϵ|∈(0,η0)|\epsilon|\in(0,\eta\_{0}), the matrix (I−Θ​(ϵ))(I-\Theta(\epsilon)) is invertible
and 𝒯n​(ϵ)≠0{\cal T}\_{n}(\epsilon)\neq 0, where 𝒯n​(ϵ){\cal T}\_{n}(\epsilon) is obtained from ([3.15](https://arxiv.org/html/2512.21621v1#S3.E15 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-effective-variables}) by replacing Θ\Theta with Θ​(ϵ)\Theta(\epsilon).
For |ϵ|∈(0,η0)|\epsilon|\in(0,\eta\_{0}), let us denote the unique solution for the MC-MFE associated with
the perturbed relative performance concerns (θp,ki​(ϵ),i∈ℕ)p,k=1m(\theta^{i}\_{p,k}(\epsilon),i\in\mathbb{N})\_{p,k=1}^{m}
by ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ)\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon) and pn−1​(𝐬,y)​(ϵ)p\_{n-1}({\bf{s}},y)(\epsilon)
for each (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}, 1≤n≤N1\leq n\leq N.
These solutions are determined by Theorems [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") with (θp,ki,Θ,ϱip)(\theta^{i}\_{p,k},\Theta,\varrho\_{i}^{p})
replaced by (θp,ki​(ϵ),Θ​(ϵ),ϱip​(ϵ))(\theta^{i}\_{p,k}(\epsilon),\Theta(\epsilon),\varrho\_{i}^{p}(\epsilon)), where we define ϱip​(ϵ):=(γip,(θp,ki​(ϵ))k=1m)\varrho\_{i}^{p}(\epsilon):=(\gamma\_{i}^{p},(\theta^{i}\_{p,k}(\epsilon))\_{k=1}^{m}).
Then we have the convergence

|  |  |  |
| --- | --- | --- |
|  | limϵ→0pn−1​(𝐬,y)​(ϵ)=pn−1​(𝐬,y),limϵ→0ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ)=ϕ^n−1i,p​(𝐬,y,zi,p,ϱip),i∈ℕ\begin{split}&\lim\_{\epsilon\rightarrow 0}p\_{n-1}({\bf{s}},y)(\epsilon)=p\_{n-1}({\bf{s}},y),\\ &\lim\_{\epsilon\rightarrow 0}\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon)=\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}),\quad i\in\mathbb{N}\end{split} |  |

for every (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}, 1≤n≤N1\leq n\leq N.
Here, pn−1​(𝐬,y)p\_{n-1}({\bf{s}},y) and ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}) are the solutions
established in Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") for the singular case.

###### Proof.

We proceed with backward induction. We define the following variables and functions
(See ([3.15](https://arxiv.org/html/2512.21621v1#S3.E15 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-effective-variables}) and ([3.22](https://arxiv.org/html/2512.21621v1#S3.E22 "In 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-effective-2})):

|  |  |  |
| --- | --- | --- |
|  | 𝒯̊ni,p:=1γni,p,𝒯̊np:=𝔼1,p​[1γn1,p],𝒱̊n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ):=log⁡fn−1p​(𝐬,y,zi,p,ϱip)​(ϵ)γni,p,𝒱̊n−1p​(𝐬,y)​(ϵ):=𝔼1,p​[𝒱̊n−11,p​(𝐬,y,Zn−11,p,ϱ1p)​(ϵ)],𝒯ni,p​(ϵ):=𝒯̊ni,p+(θi​(ϵ)​(I−Θ​(ϵ))−1​𝓣̊n)p,𝒯n​(ϵ):=𝒘⊤​(I−Θ​(ϵ))−1​𝓣̊n,𝒱n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ):=𝒱̊n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ)+(θi​(ϵ)​(I−Θ​(ϵ))−1​𝓥̊n−1​(𝐬,y)​(ϵ))p,𝒱n−1​(𝐬,y)​(ϵ):=𝒘⊤​(I−Θ​(ϵ))−1​𝓥̊n−1​(𝐬,y)​(ϵ),\begin{split}&\mathring{{\cal T}}\_{n}^{i,p}:=\frac{1}{\gamma\_{n}^{i,p}},\quad\mathring{{\cal T}}\_{n}^{p}:=\mathbb{E}^{1,p}\Bigl[\frac{1}{\gamma\_{n}^{1,p}}\Bigr],\\ &\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon):=\frac{\log f\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon)}{\gamma\_{n}^{i,p}},\quad\mathring{{\cal V}}\_{n-1}^{p}({\bf{s}},y)(\epsilon):=\mathbb{E}^{1,p}\bigl[\mathring{{\cal V}}\_{n-1}^{1,p}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1}^{p})(\epsilon)\bigr],\\ &{\cal T}\_{n}^{i,p}(\epsilon):=\mathring{{\cal T}}\_{n}^{i,p}+\bigl(\theta^{i}(\epsilon)(I-\Theta(\epsilon))^{-1}\mathring{\bm{{\cal T}}}\_{n}\bigr)\_{p},\quad{\cal T}\_{n}(\epsilon):=\bm{w}^{\top}(I-\Theta(\epsilon))^{-1}\mathring{\bm{{\cal T}}}\_{n},\\ &{\cal V}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon):=\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon)+\Bigl(\theta^{i}(\epsilon)(I-\Theta(\epsilon))^{-1}\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)(\epsilon)\Bigr)\_{p},\\ &{\cal V}\_{n-1}({\bf{s}},y)(\epsilon):=\bm{w}^{\top}(I-\Theta(\epsilon))^{-1}\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)(\epsilon),\end{split} |  |

for each (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}, i∈ℕi\in\mathbb{N}.
Here, 𝒘=(wp)p=1m\bm{w}=(w\_{p})\_{p=1}^{m} is the relative weight vector of populations.
Furthermore, the functions (fn−1p​(⋅)​(ϵ),p=1,…,m)(f\_{n-1}^{p}(\cdot)(\epsilon),p=1,\ldots,m) are those determined by Theorem [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
with perturbed interaction θi​(ϵ)\theta^{i}(\epsilon). We also employ vector notation, such as
𝓣̊n:=(𝒯̊np)p=1m\mathring{\bm{{\cal T}}}\_{n}:=(\mathring{{\cal T}}\_{n}^{p})\_{p=1}^{m} and 𝓥̊n−1​(𝐬,y)​(ϵ):=(𝒱̊n−1p​(𝐬,y)​(ϵ))p=1m\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)(\epsilon):=(\mathring{{\cal V}}\_{n-1}^{p}({\bf{s}},y)(\epsilon))\_{p=1}^{m}.
Let us also introduce the notation Vnp​(𝐬,y,zi,p,ϱip)​(ϵ),1≤n≤NV\_{n}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon),1\leq n\leq N to represent the exponential effective
liability for the ϵ\epsilon-perturbed setup defined by ([3.10](https://arxiv.org/html/2512.21621v1#S3.E10 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-Vnm1}) with θi​(ϵ),pn−1​(⋅)​(ϵ),ϕ^i,p​(⋅)​(ϵ)\theta^{i}(\epsilon),p\_{n-1}(\cdot)(\epsilon),\widehat{\phi}^{i,p}(\cdot)(\epsilon), etc.

With these variables,
the equilibrium control for θi​(ϵ)\theta^{i}(\epsilon) in Theorem [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ)=𝒯ni,p​(ϵ)𝒯n​(ϵ)​Ln−1​(𝐬,y)+1u−d​(𝒱n−1i,p​(𝐬,y,zi,p,ϱip)​(ϵ)−𝒯ni,p​(ϵ)𝒯n​(ϵ)​𝒱n−1​(𝐬,y)​(ϵ)).\widehat{\phi}^{i,p}\_{n-1}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon)=\frac{{\cal T}\_{n}^{i,p}(\epsilon)}{{\cal T}\_{n}(\epsilon)}L\_{n-1}({\bf{s}},y)+\frac{1}{u-d}\Bigl({\cal V}\_{n-1}^{i,p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon)-\frac{{\cal T}\_{n}^{i,p}(\epsilon)}{{\cal T}\_{n}(\epsilon)}{\cal V}\_{n-1}({\bf{s}},y)(\epsilon)\Bigr). |  | ( 3.32) |

As an induction hypothesis, we assume

|  |  |  |
| --- | --- | --- |
|  | limϵ→0Vnp​(𝐬n,yn,zni,p,ϱip)​(ϵ)=Vnp​(𝐬n,yn,zni,p,ϱip)limϵ→0𝒱̊n−1i,p​(𝐬n−1,yn−1,zn−1i,p,ϱip)​(ϵ)=𝒱̊n−1i,p​(𝐬n−1,yn−1,zn−1i,p,ϱip),\begin{split}&\lim\_{\epsilon\rightarrow 0}V\_{n}^{p}({\bf{s}}^{n},y\_{n},z\_{n}^{i,p},\varrho\_{i}^{p})(\epsilon)=V\_{n}^{p}({\bf{s}}^{n},y\_{n},z\_{n}^{i,p},\varrho\_{i}^{p})\\ &\lim\_{\epsilon\rightarrow 0}\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}}^{n-1},y\_{n-1},z\_{n-1}^{i,p},\varrho\_{i}^{p})(\epsilon)=\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}}^{n-1},y\_{n-1},z\_{n-1}^{i,p},\varrho\_{i}^{p}),\end{split} |  |

for every (𝐬n,𝐬n−1)∈𝒮n×𝒮n−1({\bf{s}}^{n},{\bf{s}}^{n-1})\in{\cal S}^{n}\times{\cal S}^{n-1}, (yn,yn−1)∈𝒴n×𝒴n−1(y\_{n},y\_{n-1})\in{\cal Y}\_{n}\times{\cal Y}\_{n-1},
(zni,p,zn−1i,p)∈𝒵np×𝒵n−1p(z\_{n}^{i,p},z\_{n-1}^{i,p})\in{\cal Z}\_{n}^{p}\times{\cal Z}\_{n-1}^{p}, ϱip∈Γp\varrho\_{i}^{p}\in\Gamma^{p},
where the limits Vnp​(𝐬n,yn,zni,p,ϱip)V\_{n}^{p}({\bf{s}}^{n},y\_{n},z\_{n}^{i,p},\varrho\_{i}^{p}) and 𝒱̊n−1i,p​(𝐬n−1,yn−1,zn−1i,p,ϱip)\mathring{{\cal V}}\_{n-1}^{i,p}({\bf{s}}^{n-1},y\_{n-1},z\_{n-1}^{i,p},\varrho\_{i}^{p}) in the right-hand sides
correspond to the functions defined in Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"). The convergence of 𝒱̊n−1i,p​(⋅)​(ϵ)\mathring{{\cal V}}\_{n-1}^{i,p}(\cdot)(\epsilon) also implies
the convergence of 𝓥̊n−1​(𝐬,y)​(ϵ)(:=(𝒱̊n−1p​(𝐬,y)​(ϵ))p=1m)→𝓥̊n−1​(𝐬,y)\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)(\epsilon)~(:=(\mathring{{\cal V}}^{p}\_{n-1}({\bf{s}},y)(\epsilon))\_{p=1}^{m})\to\mathring{\bm{{\cal V}}}\_{n-1}({\bf{s}},y)
as ϵ→0\epsilon\to 0 by the dominated convergence theorem. In particular, this implies that they remain bounded as ϵ→0\epsilon\rightarrow 0.
These convergences hold trivially at n=Nn=N since the function FpF^{p} is ϵ\epsilon-independent.
For notational simplicity, we fix the values of (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}
and suppress these arguments hereafter to focus on the dependence on ϵ\epsilon.

Using Lemma [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmlemma2 "Lemma 3.2. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), let R−1:=𝜿​𝒗⊤/(𝒗,𝜿)R\_{-1}:=\bm{\kappa}\bm{v}^{\top}/(\bm{v},\bm{\kappa})
and R0:=P​G​PR\_{0}:=PGP. We then have the expansion:

|  |  |  |
| --- | --- | --- |
|  | (θi​(ϵ)​(I−Θ​(ϵ))−1)=1ϵ​θi​R−1+(θi​R0−R−1)+𝒪​(ϵ).(\theta^{i}(\epsilon)(I-\Theta(\epsilon))^{-1})=\frac{1}{\epsilon}\theta^{i}R\_{-1}+(\theta^{i}R\_{0}-R\_{-1})+{\cal O}(\epsilon). |  |

Similarly, we obtain the expansions as

|  |  |  |
| --- | --- | --- |
|  | 𝒯ni,p​(ϵ)=1ϵ​(θi​R−1​𝓣̊n)p+𝒯̊ni,p+((θi​R0−R−1)​𝓣̊n)p+𝒪​(ϵ),𝒯n​(ϵ)=1ϵ​𝒘⊤​R−1​𝓣̊n+𝒘⊤​R0​𝓣̊n+𝒪​(ϵ),𝒱n−1i,p​(ϵ)=𝒱̊n−1i,p​(ϵ)+((1ϵ​θi​R−1+(θi​R0−R−1)+𝒪​(ϵ))​𝓥̊n−1​(ϵ))p𝒱n−1​(ϵ)=𝒘⊤​(1ϵ​R−1+R0+𝒪​(ϵ))​𝓥̊n−1​(ϵ).\begin{split}{\cal T}\_{n}^{i,p}(\epsilon)&=\frac{1}{\epsilon}(\theta^{i}R\_{-1}\mathring{\bm{{\cal T}}}\_{n})\_{p}+\mathring{{\cal T}}\_{n}^{i,p}+\bigl((\theta^{i}R\_{0}-R\_{-1})\mathring{\bm{{\cal T}}}\_{n}\bigr)\_{p}+{\cal O}(\epsilon),\\ {\cal T}\_{n}(\epsilon)&=\frac{1}{\epsilon}\bm{w}^{\top}R\_{-1}\mathring{\bm{{\cal T}}}\_{n}+\bm{w}^{\top}R\_{0}\mathring{\bm{{\cal T}}}\_{n}+{\cal O}(\epsilon),\\ {\cal V}\_{n-1}^{i,p}(\epsilon)&=\mathring{{\cal V}}\_{n-1}^{i,p}(\epsilon)+\Bigl(\Bigl(\frac{1}{\epsilon}\theta^{i}R\_{-1}+(\theta^{i}R\_{0}-R\_{-1})+{\cal O}(\epsilon)\Bigr)\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\Bigr)\_{p}\\ {\cal V}\_{n-1}(\epsilon)&=\bm{w}^{\top}\Bigl(\frac{1}{\epsilon}R\_{-1}+R\_{0}+{\cal O}(\epsilon)\Bigr)\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon).\end{split} |  |

Firstly, it is easy to confirm that

|  |  |  |
| --- | --- | --- |
|  | 𝒯ni,p​(ϵ)𝒯n​(ϵ)=ρi,p−ϵ​1(𝒘,𝜿)​{κp−(𝒗,𝜿)(𝒗,𝓣̊n)​(𝒯̊ni,p+(θi​R0​𝓣̊n)p−ρi,p​𝒘⊤​R0​𝓣̊n)}+𝒪​(ϵ2),\begin{split}\frac{{\cal T}\_{n}^{i,p}(\epsilon)}{{\cal T}\_{n}(\epsilon)}=\rho^{i,p}-\epsilon\frac{1}{(\bm{w},\bm{\kappa})}\Bigl\{\kappa\_{p}-\frac{(\bm{v},\bm{\kappa})}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\bigl(\mathring{{\cal T}}\_{n}^{i,p}+(\theta^{i}R\_{0}\mathring{\bm{{\cal T}}}\_{n})\_{p}-\rho^{i,p}\bm{w}^{\top}R\_{0}\mathring{\bm{{\cal T}}}\_{n}\bigr)\Bigr\}+{\cal O}(\epsilon^{2}),\end{split} |  |

where ρi,p:=(θi​𝜿)p/(𝒘,𝜿)\rho^{i,p}:=(\theta^{i}\bm{\kappa})\_{p}/(\bm{w},\bm{\kappa}).
This establishes the desired convergence of the first term in ([3.32](https://arxiv.org/html/2512.21621v1#S3.E32 "In Proof. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{eq-phi-ep}).

Next, we consider the convergence for the second term of ϕ^n−1i,p​(ϵ)\widehat{\phi}^{i,p}\_{n-1}(\epsilon). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱n−1i,p​(ϵ)−𝒯ni,p​(ϵ)𝒯n​(ϵ)​𝒱n−1​(ϵ)=1ϵ​{(θi​R−1​𝓥̊n−1​(ϵ))p−ρi,p​𝒘⊤​R−1​𝓥̊n−1​(ϵ)}+𝒱̊n−1i,p​(ϵ)+((θi​R0−R−1)​𝓥̊n−1​(ϵ))p−ρi,p​𝒘⊤​R0​𝓥̊n−1​(ϵ)+1(𝒘,𝜿)​{κp−(𝒗,𝜿)(𝒗,𝓣̊n)​(𝒯̊ni,p+(θi​R0​𝓣̊n)p−ρi,p​𝒘⊤​R0​𝓣̊n)}​𝒘⊤​R−1​𝓥̊n−1​(ϵ)+𝒪​(ϵ).\begin{split}&{\cal V}\_{n-1}^{i,p}(\epsilon)-\frac{{\cal T}\_{n}^{i,p}(\epsilon)}{{\cal T}\_{n}(\epsilon)}{\cal V}\_{n-1}(\epsilon)=\frac{1}{\epsilon}\Bigl\{(\theta^{i}R\_{-1}\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon))\_{p}-\rho^{i,p}\bm{w}^{\top}R\_{-1}\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\Bigr\}\\ &\qquad+\mathring{{\cal V}}\_{n-1}^{i,p}(\epsilon)+\bigl((\theta^{i}R\_{0}-R\_{-1})\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\bigr)\_{p}-\rho^{i,p}\bm{w}^{\top}R\_{0}\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\\ &\qquad+\frac{1}{(\bm{w},\bm{\kappa})}\Bigl\{\kappa\_{p}-\frac{(\bm{v},\bm{\kappa})}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\bigl(\mathring{{\cal T}}\_{n}^{i,p}+(\theta^{i}R\_{0}\mathring{\bm{{\cal T}}}\_{n})\_{p}-\rho^{i,p}\bm{w}^{\top}R\_{0}\mathring{\bm{{\cal T}}}\_{n}\bigr)\Bigr\}\bm{w}^{\top}R\_{-1}\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)+{\cal O}(\epsilon).\end{split} |  | ( 3.33) |

Note that the potentially diverging terms as ϵ→0\epsilon\to 0 given by the first line vanish completely by
the equality

|  |  |  |
| --- | --- | --- |
|  | (θi​R−1​𝓥̊n−1​(ϵ))p−ρi,p​𝒘⊤​R−1​𝓥̊n−1​(ϵ)≡0.\bigl(\theta^{i}R\_{-1}\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\bigr)\_{p}-\rho^{i,p}\bm{w}^{\top}R\_{-1}\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\equiv 0. |  |

By expanding the left matrix PP in R0:=P​G​PR\_{0}:=PGP, ([3.33](https://arxiv.org/html/2512.21621v1#S3.E33 "In Proof. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{ep-calv}) can be simplified, due to significant cancellations, to

|  |  |  |
| --- | --- | --- |
|  | 𝒱n−1i,p​(ϵ)−𝒯ni,p​(ϵ)𝒯n​(ϵ)​𝒱n−1​(ϵ)=𝒱̊n−1i,p​(ϵ)+(θi​G​P​𝓥̊n−1​(ϵ))p−ρi,p​𝒘⊤​G​P​𝓥̊n−1​(ϵ)−(𝒗,𝓥̊n−1​(ϵ))(𝒗,𝓣̊n)​(𝒯̊ni,p+(θi​G​P​𝓣̊n)p−ρi,p​𝒘⊤​G​P​𝓣̊n)+𝒪​(ϵ).\begin{split}{\cal V}\_{n-1}^{i,p}(\epsilon)-\frac{{\cal T}\_{n}^{i,p}(\epsilon)}{{\cal T}\_{n}(\epsilon)}{\cal V}\_{n-1}(\epsilon)&=\mathring{{\cal V}}\_{n-1}^{i,p}(\epsilon)+(\theta^{i}GP\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon))\_{p}-\rho^{i,p}\bm{w}^{\top}GP\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon)\\ &-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\Bigl(\mathring{{\cal T}}\_{n}^{i,p}+(\theta^{i}GP\mathring{\bm{{\cal T}}}\_{n})\_{p}-\rho^{i,p}\bm{w}^{\top}GP\mathring{\bm{{\cal T}}}\_{n}\Bigr)+{\cal O}(\epsilon).\end{split} |  |

Finally, using the induction hypothesis on the convergence of 𝒱̊n−1i,p​(ϵ)\mathring{{\cal V}}\_{n-1}^{i,p}(\epsilon) and 𝓥̊n−1​(ϵ)\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon), we obtain

|  |  |  |
| --- | --- | --- |
|  | limϵ→0(𝒱n−1i,p​(ϵ)−𝒯ni,p​(ϵ)𝒯n​(ϵ)​𝒱n−1​(ϵ))=𝒰n−1i,p+(θi​G​𝓤̊n−1)p−ρi,p​𝒘⊤​G​𝓤̊n−1.\begin{split}\lim\_{\epsilon\rightarrow 0}\Bigl({\cal V}\_{n-1}^{i,p}(\epsilon)-\frac{{\cal T}\_{n}^{i,p}(\epsilon)}{{\cal T}\_{n}(\epsilon)}{\cal V}\_{n-1}(\epsilon)\Bigr)={\cal U}\_{n-1}^{i,p}+(\theta^{i}G\mathring{\bm{{\cal U}}}\_{n-1})\_{p}-\rho^{i,p}\bm{w}^{\top}G\mathring{\bm{{\cal U}}}\_{n-1}.\end{split} |  |

Here, we have recalled the definition:

|  |  |  |
| --- | --- | --- |
|  | 𝒰n−1i,p=𝒱̊n−1i,p−(𝒗,𝓥̊n−1)(𝒗,𝓣̊n)​𝒯̊ni,p𝒰n−1p=𝒱̊n−1p−(𝒗,𝓥̊n−1)(𝒗,𝓣̊n)​𝒯̊np,\begin{split}{\cal U}\_{n-1}^{i,p}=\mathring{{\cal V}}\_{n-1}^{i,p}-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1})}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{{\cal T}}\_{n}^{i,p}\quad{\cal U}\_{n-1}^{p}=\mathring{{\cal V}}\_{n-1}^{p}-\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1})}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}\mathring{{\cal T}}\_{n}^{p},\end{split} |  |

and used the fact that P​𝓤̊n−1=𝓤̊n−1P\mathring{\bm{{\cal U}}}\_{n-1}=\mathring{\bm{{\cal U}}}\_{n-1}, which holds because 𝓤̊n−1∈Im​(I−Θ)\mathring{\bm{{\cal U}}}\_{n-1}\in\mathrm{Im}(I-\Theta).

Consequently, ([3.32](https://arxiv.org/html/2512.21621v1#S3.E32 "In Proof. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{eq-phi-ep}) can be expressed as

|  |  |  |
| --- | --- | --- |
|  | ϕ^n−1i,p​(ϵ)=ρi,p​Ln−1+1u−d​(𝒰n−1i,p+(θi​G​𝓤̊n−1)p−ρi,p​𝒘⊤​G​𝓤̊n−1)+𝒪​(ϵ).\widehat{\phi}^{i,p}\_{n-1}(\epsilon)=\rho^{i,p}L\_{n-1}+\frac{1}{u-d}\Bigl({\cal U}\_{n-1}^{i,p}+(\theta^{i}G\mathring{\bm{{\cal U}}}\_{n-1})\_{p}-\rho^{i,p}\bm{w}^{\top}G\mathring{\bm{{\cal U}}}\_{n-1}\Bigr)+{\cal O}(\epsilon). |  |

This establishes the desired convergence of ϕ^n−1i,p\widehat{\phi}^{i,p}\_{n-1}.
The convergence of the transition probabilities is straightforward to verify by noting that

|  |  |  |
| --- | --- | --- |
|  | 𝒱n−1​(ϵ)𝒯n​(ϵ)=(𝒗,𝓥̊n−1​(ϵ))(𝒗,𝓣̊n)+𝒪​(ϵ)\frac{{\cal V}\_{n-1}(\epsilon)}{{\cal T}\_{n}(\epsilon)}=\frac{(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}(\epsilon))}{(\bm{v},\mathring{\bm{{\cal T}}}\_{n})}+{\cal O}(\epsilon) |  |

and the boundedness of the external order flow Ln−1L\_{n-1}.

From ([3.10](https://arxiv.org/html/2512.21621v1#S3.E10 "In Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{multi-rp-Vnm1}) and the dominated convergence theorem, the convergence established above
as well as the induction hypothesis Vnp​(ϵ)→VnpV\_{n}^{p}(\epsilon)\to V\_{n}^{p} imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limϵ→0Vn−1p​(𝐬,y,zi,p,ϱip)​(ϵ)→Vn−1p​(𝐬,y,zi,p,ϱip)\lim\_{\epsilon\to 0}V\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})(\epsilon)\rightarrow V\_{n-1}^{p}({\bf{s}},y,z^{i,p},\varrho\_{i}^{p}) |  | ( 3.34) |

for every (𝐬,y,zi,p,ϱip)∈𝒮n−1×𝒴n−1×𝒵n−1p×Γp({\bf{s}},y,z^{i,p},\varrho\_{i}^{p})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}^{p}\times\Gamma^{p}.
Since (Vn−1p)p=1m(V\_{n-1}^{p})\_{p=1}^{m} satisfy the uniform bounds 0<cn−1≤Vn−1p≤Cn−1<∞0<c\_{n-1}\leq V\_{n-1}^{p}\leq C\_{n-1}<\infty,
the above convergence of Vn−1p​(ϵ)V\_{n-1}^{p}(\epsilon) also implies the convergence of fn−2p​(ϵ)f\_{n-2}^{p}(\epsilon) and hence 𝒱n−2i,p​(ϵ){\cal V}\_{n-2}^{i,p}(\epsilon).
Therefore, we recover the induction hypothesis for the previous time tn−2t\_{n-2}, which establishes the claim.
∎

###### Remark 3.5.

The continuity established in Theorem [3.4](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") relies on the assumption that (I−Θ​(ϵ))−1(I-\Theta(\epsilon))^{-1}
has a simple pole. Note, however, that the equilibrium existence result in Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
does not require this condition.
The asymptotic behavior for higher-order poles and more general forms of perturbation Θ​(ϵ)\Theta(\epsilon)
can possibly be analyzed using the methods described in Kato [[37](https://arxiv.org/html/2512.21621v1#bib.bib37)].

## 4 Numerical examples

In this section, we provide numerical examples for the models studied in
Sections [2](https://arxiv.org/html/2512.21621v1#S2 "2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [3](https://arxiv.org/html/2512.21621v1#S3 "3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
To reduce computational cost, following Fujii [[18](https://arxiv.org/html/2512.21621v1#bib.bib18)], we assume that YY and Zi,pZ^{i,p} are one-dimensional discrete processes
taking values on binomial trees, and that θp,ki\theta^{i}\_{p,k} are
independent of ii, i.e., they are constants common
across all the agents
in each population pp. Moreover, we assume that ℱ0i,p{\cal F}^{i,p}\_{0}-measurable random variables γip\gamma\_{i}^{p} are uniformly
distributed over finite sets. Since the cases without relative performance concerns (i.e., θi≡0\theta^{i}\equiv 0) have been studied in
[[18](https://arxiv.org/html/2512.21621v1#bib.bib18)] in detail, we focus here on providing illustrative examples
that highlight the impact of θ\theta on the equilibrium price distribution and the optimal trading position size.

### 4.1 Single population

We first consider the model discussed in Section [2](https://arxiv.org/html/2512.21621v1#S2 "2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
γi\gamma\_{i} is assumed to be uniformly distributed over the (Nγ+1)(N\_{\gamma}+1) discrete values given by

|  |  |  |
| --- | --- | --- |
|  | γi​(kγ):=γ¯+(γ¯−γ¯)​kγ/Nγ,kγ=0,…,Nγ.\gamma\_{i}(k\_{\gamma}):=\underline{\gamma}+(\overline{\gamma}-\underline{\gamma})k\_{\gamma}/N\_{\gamma},\quad k\_{\gamma}=0,\ldots,N\_{\gamma}. |  |

We assume that the coefficient of relative performance concerns θi\theta^{i} is common across all the agents, i.e.,
θi=θ∈ℝ,∀i∈ℕ\theta^{i}=\theta\in\mathbb{R},~\forall i\in\mathbb{N}.
The process (Zni)n=0N(Z\_{n}^{i})\_{n=0}^{N} is modeled as a one-dimensional binomial process defined by

|  |  |  |
| --- | --- | --- |
|  | Zn+1i=Zni​Rn+1i,Z\_{n+1}^{i}=Z\_{n}^{i}R\_{n+1}^{i}, |  |

where (Rni)(R\_{n}^{i}) is an (ℱtni)({\cal F}^{i}\_{t\_{n}})-adapted process taking values either uzu\_{z} or dzd\_{z}.
Specifically, Rni=uzR\_{n}^{i}=u\_{z} occurs with probability pzp\_{z} and Rni=dzR\_{n}^{i}=d\_{z} with qz:=1−pzq\_{z}:=1-p\_{z}.
We take uz=(dz)−1=exp⁡(σz​Δ)u\_{z}=(d\_{z})^{-1}=\exp(\sigma\_{z}\sqrt{\Delta}). We also assume Z0i=z0∈(0,∞)Z\_{0}^{i}=z\_{0}\in(0,\infty) is common for all the agents to reduce
computational cost. We model the process (Yn)n=0N(Y\_{n})\_{n=0}^{N} similarly but assume it follows an approximate Gaussian process:

|  |  |  |
| --- | --- | --- |
|  | Yn+1=Yn+Rn+1y,Y\_{n+1}=Y\_{n}+R\_{n+1}^{y}, |  |

where (Rny)(R\_{n}^{y}) is an (ℱtn0)({\cal F}^{0}\_{t\_{n}})-adapted process taking values of either uyu\_{y} or dyd\_{y}.
Specifically, RnyR\_{n}^{y} takes the value uyu\_{y} with probability pyp\_{y} and dyd\_{y} with probability qy:=1−pyq\_{y}:=1-p\_{y}.
We take uy=(−dy)=σy​Δu\_{y}=(-d\_{y})=\sigma\_{y}\sqrt{\Delta}.
Finally, for the stock-price process (Sn)(S\_{n}), we set u~=(d~)−1=exp⁡(σ​Δ)\widetilde{u}=(\widetilde{d})^{-1}=\exp(\sigma\sqrt{\Delta}) and S0=1.0S\_{0}=1.0.
From Theorems [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), one can see that there is no need to track the evolution of the path-dependent mean-field term μn\mu\_{n} for obtaining the equilibrium price distributions (pn−1​(s,y))(p\_{n-1}(s,y)) and the optimal strategies ϕ^n−1i\widehat{\phi}\_{n-1}^{i}. We only need its difference, i.e., Δn\Delta\_{n}, which is fixed by the market-clearing condition.

As an example for a terminal liability, we adopt the parameterization

|  |  |  |
| --- | --- | --- |
|  | F​(SN,YN,ZNi):=C−fa​SN​YN​ZNi,F(S\_{N},Y\_{N},Z\_{N}^{i}):=C-f\_{a}S\_{N}Y\_{N}Z\_{N}^{i}, |  |

where C∈ℝC\in\mathbb{R} is an arbitrary real constant. Since the result is invariant under a constant shift, one may adjust the constant CC, if necessary,
to make the liability positive. fa∈ℝf\_{a}\in\mathbb{R} is a parameter determining the sensitivity of the liability.
We model the external order flow as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ln−1​(Sn−1,Yn−1)=la​(1+lb​Yn−1)​Sn−1,L\_{n-1}(S\_{n-1},Y\_{n-1})=l\_{a}(1+l\_{b}Y\_{n-1})S\_{n-1}, |  | ( 4.1) |

with some real constants la,lb∈ℝl\_{a},l\_{b}\in\mathbb{R}.
Table [1](https://arxiv.org/html/2512.21621v1#S4.T1 "Table 1 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") summarizes the parameters to be used in Figures [2](https://arxiv.org/html/2512.21621v1#S4.F2 "Figure 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [2](https://arxiv.org/html/2512.21621v1#S4.F2 "Figure 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
We recall that the initial wealth ξi\xi\_{i} is irrelevant to our analysis.

| parameter | γ¯\underline{\gamma} | γ¯\overline{\gamma} | NγN\_{\gamma} | z0z\_{0} | σz\sigma\_{z} | pzp\_{z} | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN | faf\_{a} | lal\_{a} | lbl\_{b} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.5 | 1.5 | 4 | 1.0 | 12% | 0.5 | 1.0 | 12% | 0.5 | 1.0 | 15% | 2.5% | 2yr | 48 | 1.5 | 1 | 1 |

Table 1:  parameter values

In Figure [2](https://arxiv.org/html/2512.21621v1#S4.F2 "Figure 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we present the equilibrium distribution of the stock price at the 2-year horizon
for six different values of θ∈{−0.2,0.1,0.4,0.7,1.0,1.3}\theta\in\{-0.2,0.1,0.4,0.7,1.0,1.3\}. One can observe that the price distribution
changes smoothly. More specifically, it monotonically shifts leftward as θ\theta increases, which implies that a lower excess
return is demanded when there exists a strong relative performance concern.
In Figure [2](https://arxiv.org/html/2512.21621v1#S4.F2 "Figure 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we plot 𝔼​[|ϕ^1​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{1}(t\_{n})|^{2}]^{\frac{1}{2}} for the corresponding values of
θ\theta at three different times tn∈{0.5,1.0,1.5}t\_{n}\in\{0.5,1.0,1.5\} years. As expected, there is no irregularity around θ=1\theta=1.

![Refer to caption](RPG-single-1.png)


Figure 1: The equilibrium stock price distribution at the 2-year horizon for six different values of θ\theta.

![Refer to caption](RPG-single-2.png)


Figure 2: The root mean square of the equilibrium optimal strategy
𝔼​[|ϕ^1​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{1}(t\_{n})|^{2}]^{\frac{1}{2}} as a function of θ\theta at tn∈{0.5,1.0,1.5}t\_{n}\in\{0.5,1.0,1.5\}.

In the next example, we set fa=0f\_{a}=0 to eliminate the terminal liability and use a larger value for lal\_{a} to emphasize
the effect of θ\theta on the equilibrium price distribution.
The parameters are summarized in Table [2](https://arxiv.org/html/2512.21621v1#S4.T2 "Table 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

| parameter | γ¯\underline{\gamma} | γ¯\overline{\gamma} | NγN\_{\gamma} | z0z\_{0} | σz\sigma\_{z} | pzp\_{z} | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN | faf\_{a} | lal\_{a} | lbl\_{b} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.5 | 1.5 | 4 | 1.0 | 12% | 0.5 | 1.0 | 12% | 0.5 | 1.0 | 15% | 2.5% | 2yr | 48 | 0 | 3 | 1 |

Table 2:  parameter values

In Figure [3](https://arxiv.org/html/2512.21621v1#S4.F3 "Figure 3 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we plot the time evolution of the expected stock price 𝔼​[S​(tn)]\mathbb{E}[S(t\_{n})] in equilibrium
for five different values of θ∈{0.4,0.7,1.0,1.3,1.6}\theta\in\{0.4,0.7,1.0,1.3,1.6\}, based on the parameters in Table [2](https://arxiv.org/html/2512.21621v1#S4.T2 "Table 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
The risk-free interest rate is r=2.5%r=2.5\%, which coincides with the expected growth rate of the stock when θ=1.0\theta=1.0.
This is consistent with the discussion in Remark [2.5](https://arxiv.org/html/2512.21621v1#S2.Thmremark5 "Remark 2.5. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
We can also observe that cases with θ>1\theta>1 yield a negative excess return.
It is interesting to note that, when θ=1.0\theta=1.0, the equilibrium price distribution coincides exactly with
the distribution under the risk-neutral measure. Using ([2.14](https://arxiv.org/html/2512.21621v1#S2.E14 "In Theorem 2.2. ‣ 2.4 Market-clearing mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-MC-position}) and ([2.9](https://arxiv.org/html/2512.21621v1#S2.E9 "In Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-Vnm1}),
a simple induction argument shows that fn−1≡1f\_{n-1}\equiv 1 and ϕ^n−1i​(s,y)=Ln−1​(s,y)\widehat{\phi}^{i}\_{n-1}(s,y)=L\_{n-1}(s,y) for all 1≤n≤N1\leq n\leq N.
Since the effective risk tolerance is now +∞+\infty, there is no required risk premium regardless
of the size of Ln−1L\_{n-1}.

![Refer to caption](RPG-single-3.png)


Figure 3: The evolution of 𝔼​[S​(t)]\mathbb{E}[S(t)] for θ∈{0.4,0.7,1.0,1.3,1.6}\theta\in\{0.4,0.7,1.0,1.3,1.6\} with parameters in Table [2](https://arxiv.org/html/2512.21621v1#S4.T2 "Table 2 ‣ 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

### 4.2 Multiple populations

We next provide numerical examples for the multi-population model studied in Section [3](https://arxiv.org/html/2512.21621v1#S3 "3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
For simplicity, we focus on the two-population model (m=2)(m=2) with relative population weights wp,p∈{1,2}w\_{p},p\in\{1,2\}.
As in the previous case, γip\gamma\_{i}^{p} is assumed to be uniformly distributed over the (Nγp+1)(N\_{\gamma}^{p}+1) discrete values:

|  |  |  |
| --- | --- | --- |
|  | γip​(kγ)=γ¯p+(γ¯p−γ¯p)​kγ/Nγp,p∈{1,2},kγ=0,…,Nγp.\gamma\_{i}^{p}(k\_{\gamma})=\underline{\gamma}^{p}+(\overline{\gamma}^{p}-\underline{\gamma}^{p})k\_{\gamma}/N\_{\gamma}^{p},\quad p\in\{1,2\},\quad k\_{\gamma}=0,\ldots,N\_{\gamma}^{p}. |  |

As mentioned at the beginning of this section, we assume that {(θp,ki),p,k∈{1,2}}\{(\theta^{i}\_{p,k}),p,k\in\{1,2\}\} are independent of the agent-ii, i.e.,
θp,ki=Θp,k\theta^{i}\_{p,k}=\Theta\_{p,k} for every p,k∈{1,2}p,k\in\{1,2\}.
The processes (Zni,p)n=0N(Z\_{n}^{i,p})\_{n=0}^{N} for p∈{1,2}p\in\{1,2\} are modeled in the same way as before:

|  |  |  |
| --- | --- | --- |
|  | Zn+1i,p=Zni,p​Rn+1i,p,Z\_{n+1}^{i,p}=Z\_{n}^{i,p}R\_{n+1}^{i,p}, |  |

where (Rni,p)(R\_{n}^{i,p}) is an (ℱtni,p)({\cal F}^{i,p}\_{t\_{n}})-adapted process taking values in {uzp,dzp}\{u\_{z}^{p},d\_{z}^{p}\}.
Specifically, Rni,pR\_{n}^{i,p} takes the value uzpu\_{z}^{p} with probability pzpp\_{z}^{p} and dzpd\_{z}^{p} with probability
qzp:=1−pzpq\_{z}^{p}:=1-p\_{z}^{p}.
We take uzp=(dzp)−1=exp⁡(σzp​Δ)u\_{z}^{p}=(d\_{z}^{p})^{-1}=\exp(\sigma\_{z}^{p}\sqrt{\Delta}). We also assume that Z0i,p=z0p∈(0,∞)Z\_{0}^{i,p}=z\_{0}^{p}\in(0,\infty) is common to all the agents
in each population pp. The dynamics of the stock price process (Sn)(S\_{n}) as well as the common noise process (Yn)(Y\_{n})
are exactly the same as in the previous example.

For each population pp, the terminal liability is assumed to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fp​(SN,YN,ZNi,p):=Cp−fap​SN​YN​ZNi,p,p∈{1,2},F^{p}(S\_{N},Y\_{N},Z\_{N}^{i,p}):=C^{p}-f\_{a}^{p}S\_{N}Y\_{N}Z\_{N}^{i,p},\quad p\in\{1,2\}, |  | ( 4.2) |

where CpC^{p} is an arbitrary real constant and fapf\_{a}^{p} is a parameter determining the level of sensitivity.
The external order flow (Ln−1)(L\_{n-1}) is modeled by ([4.1](https://arxiv.org/html/2512.21621v1#S4.E1 "In 4.1 Single population ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{numerical-L}) as before.
As mentioned in Remark [3.4](https://arxiv.org/html/2512.21621v1#S3.Thmremark4 "Remark 3.4. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), since both the terminal liability
and the external order flow are independent of the past history of the stock price,
the equilibrium transition probabilities and the associated optimal controls also become path-independent.
In this case, the solutions given in Theorems [3.1](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Relative performance mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), and [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
hold by replacing 𝐬∈𝒮n−1{\bf{s}}\in{\cal S}^{n-1} with s∈𝒮n−1s\in{\cal S}\_{n-1}, the last element of 𝐬{\bf{s}}.

In the first example, we consider the matrix of relative performance concerns with the following parametrization:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(a):=(a0.40.4a),\Theta(a):=\begin{pmatrix}a&0.4\\ 0.4&a\end{pmatrix}, |  | ( 4.3) |

with aa chosen around the value 0.60.6, which makes (I−Θ)(I-\Theta) singular.
When a=0.6a=0.6, we have

|  |  |  |
| --- | --- | --- |
|  | (I−Θ​(0.6))†=58​(1−1−11),𝒗=𝜿=12​(1,1)⊤.(I-\Theta(0.6))^{\dagger}=\frac{5}{8}\begin{pmatrix}1&-1\\ -1&1\end{pmatrix},\bm{v}=\bm{\kappa}=\frac{1}{\sqrt{2}}(1,1)^{\top}. |  |

Recall that (I−Θ​(0.6))†(I-\Theta(0.6))^{\dagger} denotes the pseudo inverse defined on the span​{(1,−1)⊤}\mathrm{span}\{(1,-1)^{\top}\}
and 𝒗\bm{v} and 𝜿\bm{\kappa} are unit vectors satisfying 𝒗∈Ker​(I−Θ​(0.6))⊤\bm{v}\in\mathrm{Ker}(I-\Theta(0.6))^{\top} and 𝜿∈Ker​(I−Θ​(0.6))\bm{\kappa}\in\mathrm{Ker}(I-\Theta(0.6)).
It is easy to see that a=0.6a=0.6 is a first-order pole. In fact, setting a=0.6−ϵa=0.6-\epsilon, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−Θ​(a))−1=1ϵ​(0.8+ϵ)​(0.4+ϵ0.40.40.4+ϵ).(I-\Theta(a))^{-1}=\frac{1}{\epsilon(0.8+\epsilon)}\begin{pmatrix}0.4+\epsilon&0.4\\ 0.4&0.4+\epsilon\end{pmatrix}. |  | ( 4.4) |

The remaining parameters for this example are summarized in Table [3](https://arxiv.org/html/2512.21621v1#S4.T3 "Table 3 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

| parameter | w1w\_{1} | w2w\_{2} | γ¯1\underline{\gamma}^{1} | γ¯1\overline{\gamma}^{1} | γ¯2\underline{\gamma}^{2} | γ¯2\overline{\gamma}^{2} | Nγ1N\_{\gamma}^{1} | Nγ2N\_{\gamma}^{2} | z01z\_{0}^{1} | z02z\_{0}^{2} | σz1\sigma\_{z}^{1} | σz2\sigma\_{z}^{2} | pz1p\_{z}^{1} | pz2p\_{z}^{2} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.3 | 0.7 | 0.5 | 1.5 | 0.2 | 1.2 | 4 | 4 | 1.0 | 1.0 | 12% | 12% | 0.5 | 0.5 |

| parameter | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN | fa1f\_{a}^{1} | fa2f\_{a}^{2} | lal\_{a} | lbl\_{b} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 1.0 | 12% | 0.5 | 1.0 | 15% | 2.5% | 2yr | 48 | 1.2 | 2.4 | 1.5 | 1.5 |

Table 3: parameter values



![Refer to caption](RPG-multi-1.png)


Figure 4: The equilibrium stock price distributions at the 2-year horizon for five different values of aa.

![Refer to caption](RPG-multi-2.png)


Figure 5: The root mean square of the equilibrium optimal strategy 𝔼​[|ϕ^p​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{p}(t\_{n})|^{2}]^{\frac{1}{2}} for p∈{1,2}p\in\{1,2\}
as a function of aa at tn∈{0.5,1.0,1.5}t\_{n}\in\{0.5,1.0,1.5\}.

In Figure [5](https://arxiv.org/html/2512.21621v1#S4.F5 "Figure 5 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we plot the equilibrium stock price distributions at the 2-year horizon
for Θ\Theta in ([4.3](https://arxiv.org/html/2512.21621v1#S4.E3 "In 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{example-theta-1}) and the parameters in Table [3](https://arxiv.org/html/2512.21621v1#S4.T3 "Table 3 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
with five different values of a∈{0,0.2,0.4,0.6,0.8}a\in\{0,0.2,0.4,0.6,0.8\}. The distribution at the singular point (a=0.6)(a=0.6)
is calculated using the results in Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), while the others are based on Theorem [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
In Figure [5](https://arxiv.org/html/2512.21621v1#S4.F5 "Figure 5 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we present the root mean square of the equilibrium optimal strategy 𝔼​[|ϕ^p​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{p}(t\_{n})|^{2}]^{\frac{1}{2}}
for each population p∈{1,2}p\in\{1,2\} as a function of aa at tn∈{0.5,1.0,1.5}t\_{n}\in\{0.5,1.0,1.5\} years.
We evaluate ten cases with {a=(0.1)​k:k=0,1,…,9}\{a=(0.1)k:k=0,1,\ldots,9\}.
Consistent with the results in Section [3.6](https://arxiv.org/html/2512.21621v1#S3.SS6 "3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"),
both the equilibrium price distributions and the optimal position sizes appear to change continuously with the parameter aa.
Figure [5](https://arxiv.org/html/2512.21621v1#S4.F5 "Figure 5 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") shows that
𝔼​[|ϕ^2​(tn)|2]12>𝔼​[|ϕ^1​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{2}(t\_{n})|^{2}]^{\frac{1}{2}}>\mathbb{E}[|\widehat{\phi}^{1}(t\_{n})|^{2}]^{\frac{1}{2}} for small values of aa, but this relationship reverses
for a>0.6a>0.6.
Since the second population has a larger risk tolerance (γ2≤γ1\gamma^{2}\leq\gamma^{1} on average)
and higher hedging needs (fa1≤fa2f\_{a}^{1}\leq f\_{a}^{2}), it is natural that they hold larger positions
than the first population when the effects of relative performance concerns are sufficiently small.
The significant change around a=0.6a=0.6 is attributable to the sign flip in (I−Θ​(ϵ))−1(I-\Theta(\epsilon))^{-1}
from ([4.4](https://arxiv.org/html/2512.21621v1#S4.E4 "In 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{theta-ep-1}) and the resulting impact on both the effective risk tolerance
and the sensitivity of the effective liability defined in ([3.15](https://arxiv.org/html/2512.21621v1#S3.E15 "In 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{def-effective-variables}).

In the second example, we consider the matrix of relative performance concerns
of the following form:

|  |  |  |
| --- | --- | --- |
|  | Θ​(a):=(a0.10a)\Theta(a):=\begin{pmatrix}a&0.1\\ 0&a\end{pmatrix} |  |

with a∈ℝa\in\mathbb{R} as a parameter. This asymmetric matrix has a second-order pole at a=1a=1
and hence this model is not covered by the analysis in Section [3.6](https://arxiv.org/html/2512.21621v1#S3.SS6 "3.6 Perturbation of the inverse (𝐼-Θ⁢(ϵ))⁻¹ around ϵ=0 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
By setting a=1−ϵa=1-\epsilon, we obtain

|  |  |  |
| --- | --- | --- |
|  | (I−Θ​(a))−1=(1/ϵ0.1/ϵ201/ϵ).(I-\Theta(a))^{-1}=\begin{pmatrix}1/\epsilon&0.1/\epsilon^{2}\\ 0&1/\epsilon\end{pmatrix}. |  |

When a=1a=1, it is not difficult to see that

|  |  |  |
| --- | --- | --- |
|  | (I−Θ​(1))†=(00−100),𝒗=(0,1)⊤,𝜿=(1,0)⊤,(I-\Theta(1))^{\dagger}=\begin{pmatrix}0&0\\ -10&0\end{pmatrix},\quad\bm{v}=(0,1)^{\top},\quad\bm{\kappa}=(1,0)^{\top}, |  |

where (I−Θ​(1))†(I-\Theta(1))^{\dagger} is the pseudo inverse defined on span​{(1,0)⊤}\mathrm{span}\{(1,0)^{\top}\}
and 𝒗\bm{v} and 𝜿\bm{\kappa} are unit vectors satisfying 𝒗∈Ker​(I−Θ​(1))⊤\bm{v}\in\mathrm{Ker}(I-\Theta(1))^{\top} and 𝜿∈Ker​(I−Θ​(1))\bm{\kappa}\in\mathrm{Ker}(I-\Theta(1)).
The remaining parameters for this example are summarized in Table [4](https://arxiv.org/html/2512.21621v1#S4.T4 "Table 4 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

| parameter | w1w\_{1} | w2w\_{2} | γ¯1\underline{\gamma}^{1} | γ¯1\overline{\gamma}^{1} | γ¯2\underline{\gamma}^{2} | γ¯2\overline{\gamma}^{2} | Nγ1N\_{\gamma}^{1} | Nγ2N\_{\gamma}^{2} | z01z\_{0}^{1} | z02z\_{0}^{2} | σz1\sigma\_{z}^{1} | σz2\sigma\_{z}^{2} | pz1p\_{z}^{1} | pz2p\_{z}^{2} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.5 | 0.5 | 0.5 | 1.5 | 0.5 | 1.5 | 4 | 4 | 1.0 | 1.0 | 12% | 12% | 0.5 | 0.5 |

| parameter | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN | fa1f\_{a}^{1} | fa2f\_{a}^{2} | lal\_{a} | lbl\_{b} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 1.0 | 12% | 0.5 | 1.0 | 15% | 2.5% | 2yr | 48 | 0 | 0 | 2 | 2 |

Table 4: parameter values

In Figure [7](https://arxiv.org/html/2512.21621v1#S4.F7 "Figure 7 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we plot the equilibrium stock price distributions at the 2-year horizon
for six different values of a∈{0.4,0.6,0.78,1.0,1.2,1.4}a\in\{0.4,0.6,0.78,1.0,1.2,1.4\},
and in Figure [7](https://arxiv.org/html/2512.21621v1#S4.F7 "Figure 7 ‣ 4.2 Multiple populations ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"), we plot the root mean square of the equilibrium
optimal strategy 𝔼​[|ϕ^p​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{p}(t\_{n})|^{2}]^{\frac{1}{2}} for each population p∈{1,2}p\in\{1,2\}
at tn∈{0.5,1.0,1.5}t\_{n}\in\{0.5,1.0,1.5\} years. For this figure, we evaluate nine different values of a∈{0.4,0.5,0.6,0.7,0.78,1.0,1.2,1.3,1.4}a\in\{0.4,0.5,0.6,0.7,0.78,1.0,1.2,1.3,1.4\}.
At the singular point (a=1.0)(a=1.0), the results in Theorem [3.3](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") are used,
while the others are based on Theorem [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
We could not obtain stable numerical results near the singular point a=1.0a=1.0 using Theorem [3.2](https://arxiv.org/html/2512.21621v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.4 Market-clearing mean-field equilibrium ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns")
due to numerical overflow arising from (Vn−1p)(V\_{n-1}^{p}), which are exponentials of the effective
liabilities. Although the equilibrium price distributions still appear to shift monotonically leftward as aa increases,
the root mean square of the optimal strategies 𝔼​[|ϕ^p​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{p}(t\_{n})|^{2}]^{\frac{1}{2}} exhibit distinctive behavior around the singular point.
In particular, the optimal strategy of the second population 𝔼​[|ϕ^2​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{2}(t\_{n})|^{2}]^{\frac{1}{2}} decreases
toward zero at a=1.0a=1.0. Since there is no liability and (Θ​κ)2=0(\Theta\kappa)\_{2}=0,
we can show, by a simple induction, that ϕ^2≡0\widehat{\phi}^{2}\equiv 0 from ([3.24](https://arxiv.org/html/2512.21621v1#S3.E24 "In Theorem 3.3. ‣ 3.5 Market-clearing mean-field equilibrium when dim⁢Ker⁢(𝐼-Θ)=1 ‣ 3 A network of relative performance concerns among multiple populations ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{mc-optimal-kernel-1}) when a=1.0a=1.0.
Furthermore, since an induction argument shows 𝒱̊2≡0\mathring{{\cal V}}^{2}\equiv 0 and we have
(𝒗,𝓥̊n−1)=𝒱̊n−12\bigl(\bm{v},\mathring{\bm{{\cal V}}}\_{n-1}\bigr)=\mathring{{\cal V}}^{2}\_{n-1},
the equilibrium price distribution at a=1.0a=1.0 coincides with that under the risk-neutral measure.

![Refer to caption](RPG-multi-3.png)


Figure 6: The equilibrium stock price distributions at the 2-year horizon for six different values of aa.

![Refer to caption](RPG-multi-4.png)


Figure 7: The root mean square of the equilibrium optimal strategy 𝔼​[|ϕ^p​(tn)|2]12\mathbb{E}[|\widehat{\phi}^{p}(t\_{n})|^{2}]^{\frac{1}{2}}
for p∈{1,2}p\in\{1,2\} as a function of aa at tn∈{0.5,1.0,1.5}t\_{n}\in\{0.5,1.0,1.5\}.

## 5 Concluding remarks

In this paper, we have investigated the mean-field equilibrium price formation in a discrete-time
market populated by agents with exponential utility and relative performance concerns. By extending the tractable binomial tree framework,
we were able to impose the market-clearing condition explicitly, thereby determining the asset price dynamics
endogenously rather than treating it as exogenous. We established the existence and uniqueness of the Market-Clearing Mean-Field
Equilibrium (MC-MFE) for both single-population and multi-population settings, characterizing how
the network of relative concerns impacts the risk premium and trading strategies.
Furthermore, using resolvent expansion techniques,
we demonstrated that the equilibrium solutions depend continuously on the interaction matrix, even around the points
where (I−Θ)(I-\Theta) exhibits a first-order singularity.

### Declarations of Interest and AI use

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
There is no competing interests to declare.
The author acknowledges the use of the large language model Gemini
to refine the English clarity and style in the manuscript. After using this tool, the author reviewed and
edited the content as needed and takes full responsibility for the content of the published article.

## Appendix A Connection to the finite population game

We briefly comment on the connection to the finite population game with agent-ii, 1≤i≤Np1\leq i\leq N\_{p}.
Due to the symmetry of the problem, we focus on the optimization problem for the agent-11.
Let us define the empirical expectation of the wealth as

|  |  |  |
| --- | --- | --- |
|  | μ¯NNp:=1Np−1​∑j=2NpX^Nj,\overline{\mu}^{N\_{p}}\_{N}:=\frac{1}{N\_{p}-1}\sum\_{j=2}^{N\_{p}}\widehat{X}\_{N}^{j}, |  |

where X^j\widehat{X}^{j} denotes the wealth process of agent-jj associated with the mean-field optimal control
ϕ^j:=(ϕ^n−1j)n=1N\widehat{\phi}^{j}:=(\widehat{\phi}^{j}\_{n-1})\_{n=1}^{N} given in Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

Suppose that agent-11 adopts an arbitrary admissible control ϕ1:=(ϕn−11)n=1N\phi^{1}:=(\phi^{1}\_{n-1})\_{n=1}^{N} in 𝔸1\mathbb{A}^{1} and set

|  |  |  |
| --- | --- | --- |
|  | JNp,1(ϕ1,ϕ^2,…,ϕ^Np):=𝔼[−exp(−γ1(XN1−θ1μ¯NNp−F(SN,YN,ZN1))|ℱ00,1],J^{N\_{p},1}(\phi^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}}):=\mathbb{E}\Bigl[-\exp\Bigl(-\gamma\_{1}(X\_{N}^{1}-\theta\_{1}\overline{\mu}\_{N}^{N\_{p}}-F(S\_{N},Y\_{N},Z\_{N}^{1})\Bigr)|{\cal F}\_{0}^{0,1}\Bigr], |  |

where X1X^{1} is the wealth process of agent-11 associated with the control ϕ1\phi^{1}.
We also define the value function in the large population limit:

|  |  |  |
| --- | --- | --- |
|  | 𝒥1(ϕ1,(ϕ^j)j=2∞):=𝔼0,1[−exp(−γ1(XN1−θ1μ^N(𝐒N,𝐘N−1)−F(SN,YN,ZN1))|ℱ00,1],\begin{split}{\cal J}^{1}(\phi^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty}):=\mathbb{E}^{0,1}\Bigl[-\exp\Bigl(-\gamma\_{1}(X\_{N}^{1}-\theta\_{1}\widehat{\mu}\_{N}({\bf{S}}^{N},{\bf{Y}}^{N-1})-F(S\_{N},Y\_{N},Z\_{N}^{1})\Bigr)|{\cal F}\_{0}^{0,1}\Bigr],\end{split} |  |

where μ^\widehat{\mu} is the solution to the RP-MFE given in Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").
Note that 𝒥1​(ϕ^1,(ϕ^j)j=2∞){\cal J}^{1}(\widehat{\phi}^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty}) corresponds to the value function in the RP-MFE
studied in Theorem [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.3 Relative performance mean-field equilibrium ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns").

Since (X^j)j≥2(\widehat{X}^{j})\_{j\geq 2} are ℱ0{\cal F}^{0}-conditionally i.i.d., we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[|μ¯Np−μ^N(𝐒N,𝐘N−1)|2|𝐬,𝐲]=1Np−1𝔼0,j[|X^Nj−𝔼0,j[X^Nj|𝐬,𝐲−]|2|𝐬,𝐲−]≤CNp,\begin{split}&\mathbb{E}\Bigl[\Bigl|\overline{\mu}^{N\_{p}}-\widehat{\mu}\_{N}({\bf{S}}^{N},{\bf{Y}}^{N-1})\Bigr|^{2}\Bigl|{\bf{s}},{\bf{y}}\Bigr]=\frac{1}{N\_{p}-1}\mathbb{E}^{0,j}\Bigl[\Bigl|\widehat{X}\_{N}^{j}-\mathbb{E}^{0,j}[\widehat{X}\_{N}^{j}|{\bf{s}},{\bf{y}}^{-}]\Bigr|^{2}\Bigr|{\bf{s}},{\bf{y}}^{-}\Bigr]\leq\frac{C}{N\_{p}},\end{split} |  | (A.1) |

uniformly in (𝐬,𝐲)∈𝒮N×𝒴N({\bf{s}},{\bf{y}})\in{\cal S}^{N}\times{\cal Y}^{N} with some positive constant CC.
Note that the conditional variance is finite due to the boundedness of X^j\widehat{X}^{j}, which follows from
the boundedness of ξj\xi\_{j} and ϕ^j\widehat{\phi}^{j}.

###### Theorem A.1.

Let Assumptions [2.1](https://arxiv.org/html/2512.21621v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") and [2.2](https://arxiv.org/html/2512.21621v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 Optimization problem ‣ 2 Single population with relative performance concerns ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") be in force. We also assume that 𝔼1​[θ1]≠1\mathbb{E}^{1}[\theta\_{1}]\neq 1.
For any admissible control ϕ1∈𝔸1\phi^{1}\in\mathbb{A}^{1}, there exists ϵNp>0\epsilon\_{N\_{p}}>0 such that

|  |  |  |
| --- | --- | --- |
|  | JNp,1​(ϕ1,ϕ^2,…,ϕ^Np)≤JNp,1​(ϕ^1,ϕ^2,…,ϕ^Np)+ϵNp,J^{N\_{p},1}(\phi^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})\leq J^{N\_{p},1}(\widehat{\phi}^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})+\epsilon\_{N\_{p}}, |  |

and ϵNp→0\epsilon\_{N\_{p}}\rightarrow 0 as Np→∞N\_{p}\rightarrow\infty.

###### Proof.

It is enough to constrain the admissible control space 𝔸1\mathbb{A}^{1} so that
JNp,1​(ϕ1,ϕ^2,…,ϕ^Np)∧𝒥1​(ϕ1,(ϕ^j)j=2∞)>−MJ^{N\_{p},1}(\phi^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})\wedge{\cal J}^{1}(\phi^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})>-M
for sufficiently large M>0M>0. Then we have

|  |  |  |
| --- | --- | --- |
|  | |JNp,1​(ϕ1,ϕ^2,…,ϕ^Np)−𝒥1​(ϕ1,(ϕ^j)j=2∞)|≤M​𝔼​[exp⁡(γ1​|θ1|​|μ^N​(𝐒N,𝐘N−1)−μ¯NNp|)−1]≤C​M​𝔼​[|μ^N​(𝐒N,𝐘N−1)−μ¯NNp|].\begin{split}&|J^{N\_{p},1}(\phi^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})-{\cal J}^{1}(\phi^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})|\\ &\quad\leq M\mathbb{E}\Bigl[\exp\Bigl(\gamma\_{1}|\theta\_{1}|\bigl|\widehat{\mu}\_{N}({\bf{S}}^{N},{\bf{Y}}^{N-1})-\overline{\mu}\_{N}^{N\_{p}}\bigr|\Bigr)-1\Bigr]\leq CM\mathbb{E}\bigl[|\widehat{\mu}\_{N}({\bf{S}}^{N},{\bf{Y}}^{N-1})-\overline{\mu}\_{N}^{N\_{p}}|\bigr].\end{split} |  |

where CC is some positive constant depending on the bounds of γ1,θ1,μ^N\gamma\_{1},\theta\_{1},\widehat{\mu}\_{N}, and μ¯NNp\overline{\mu}\_{N}^{N\_{p}}.
Recall that the wealth process X^j\widehat{X}^{j} associated with ϕ^j\widehat{\phi}^{j} is a bounded process, and so are μ^N\widehat{\mu}\_{N} and μ¯NNp\overline{\mu}\_{N}^{N\_{p}}.
In particular, CC can be taken independent of NpN\_{p}. It thus follows from the estimate ([A.1](https://arxiv.org/html/2512.21621v1#A1.E1 "In Appendix A Connection to the finite population game ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{single-LLN}) and Jensen’s
inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |JNp,1​(ϕ1,ϕ^2,…,ϕ^Np)−𝒥1​(ϕ1,(ϕ^j)j=2∞)|≤C/Np|J^{N\_{p},1}(\phi^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})-{\cal J}^{1}(\phi^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})|\leq C/\sqrt{N\_{p}} |  | (A.2) |

with some constant CC independent of NpN\_{p}.

On the other hand, by definition of ϕ^1\widehat{\phi}^{1},
𝒥1​(ϕ1,(ϕ^j)j=2∞)≤𝒥1​(ϕ^1,(ϕ^j)j=2∞){\cal J}^{1}(\phi^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})\leq{\cal J}^{1}(\widehat{\phi}^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})
for any admissible control ϕ1\phi^{1}. Therefore, using the estimate in ([A.2](https://arxiv.org/html/2512.21621v1#A1.E2 "In Proof. ‣ Appendix A Connection to the finite population game ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns"))(\ref{epsilon-Nash-tmp}),

|  |  |  |
| --- | --- | --- |
|  | JNp,1​(ϕ1,ϕ^2,…,ϕ^Np)≤𝒥1​(ϕ1,(ϕ^j)j=2∞)+C/Np≤𝒥1​(ϕ^1,(ϕ^j)j=2∞)+C/Np≤JNp,1​(ϕ^1,ϕ^2,…,ϕ^Np)+2​C/Np,\begin{split}&J^{N\_{p},1}(\phi^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})\leq{\cal J}^{1}(\phi^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})+C/\sqrt{N\_{p}}\\ &\quad\leq{\cal J}^{1}(\widehat{\phi}^{1},(\widehat{\phi}^{j})\_{j=2}^{\infty})+C/\sqrt{N\_{p}}\leq J^{N\_{p},1}(\widehat{\phi}^{1},\widehat{\phi}^{2},\ldots,\widehat{\phi}^{N\_{p}})+2C/\sqrt{N\_{p}},\end{split} |  |

which proves the claim with ϵNp=2​C/Np\epsilon\_{N\_{p}}=2C/\sqrt{N\_{p}}.
∎

###### Remark A.1.

Theorem [A.1](https://arxiv.org/html/2512.21621v1#A1.Thmtheorem1 "Theorem A.1. ‣ Appendix A Connection to the finite population game ‣ Mean-Field Price Formation on Trees with a Network of Relative Performance Concerns") implies that the optimal controls (ϕ^i)i≥1(\widehat{\phi}^{i})\_{i\geq 1} constitute
an (open loop) ϵ\epsilon-Nash equilibrium for the relative performance game.

## References

* [1]

  Achdou, Y., Han, J., Lasry, J., Lions, P. and Moll, B., Partial differential equation models
  in macroeconomics, Philosophical Transactions of The Royal Society, 2014, A 372:20130397.
* [2]

  Achdou, Y., Han, J., Lasry, J., Lions, P. and Moll, B., Income and wealth distributions in
  macroeconomics: A continuous-time approach, The Review of Economic Studies, 2021, Vol. 89, Issue 1, pp. 45-86.
* [3]

  Aïd, R., Possamaï, D., Touzi, N., Optimal electricity demand response contracting with responsiveness incentives,
  Mathematics of Operations Research, 2022, Vol. 47, No. 3, pp. 2112-2137.
* [4]

  Aïd, R., Bonesini, O., Callegaro, G., and Campi, L., Continuous-time persuasion by filtering,
  Journal of Economic Dynamics and Control, 2025, Vol. 176, 105100.
* [5]

  Ashrafyan, Y., Bakaryan, T., Gomes, D. and Gutierrez, J., A duality approach to a price formation MFG model,
  Minimax Theory and its Applications, 2023, Vol. 8, pp. 1-36.
* [6]

  Bayraktar, E., Mitra, I., Zhang, J., Countercyclical unemployment benefits: a general equilibrium analysis of transition
  dynamics, Mathematics and Financial Economics, 2024, Vol. 18, pp. 213-232.
* [7]

  Cox, J.C., Ross, S.A. and Rubinstein, M., Option Pricing: a simplified approach,
  Journal of Financial Economics, 1979, Vol. 7, pp. 229-263.
* [8]

  Derman, E., and Kani, I., Riding on a smile, RISK, 1994, July, no.3, 32-39.
* [9]

  Dianetti, J., Riedel, F. and Stanca. L., Optimal consumption and investment under relative performance
  criteria with Epstein-Zin utility, 2024, preprint arXiv:2402.07698.
* [10]

  dos Reis, G. and Platonov, V., Forward utilities and mean-field games under relative performance
  concerns, Particle Systems and Partial Differential Equations, 2021, VI, VII, VIII.
* [11]

  dos Reis, G. and Platonov, V., Forward utility and market adjustments in relative investment consumption
  games of many players, SIAM Journal on Financial Mathematics, 2022, 13(3):844–876.
* [12]

  Espinosa, G and Touzi, N., Optimal investment under relative performance concerns, Mathematical
  Finance, 2015, 25 (2): 221–257.
* [13]

  Féron, O., Tankov, P. and Tinsi, L., Price formation and optimal trading in intraday electricity markets,
  Mathematics and Financial Economics, 2022, Vol. 16, pp. 205-237.
* [14]

  Frei, C and dos Reis, G., A financial market with interacting investors: does an equilibrium exist?,
  Mathematics and Financial Economics, 2011, 4:161–182.
* [15]

  Fu, G., Mean field portfolio games with consumption, Mathematics and Financial Economics, 2023,
  17(1):79–99.
* [16]

  Fu, G. and Zhou, C., Mean field portfolio games, Finance and Stochastics, 2023, 27:189–23.
* [17]

  Fu, G., and Horst, U., Mean field portfolio games with Epstein-Zin Preferences,
  2025, preprint: arXiv:25050723.
* [18]

  Fujii, M., Mean-field price formation on trees: with multi-population and
  non-rational agents,
  preprint, arXiv:2510.11261.
* [19]

  Fujii, M., Equilibrium pricing of securities in the co-presence of cooperative and non-cooperative populations,
  ESAIM: Control, Optimization and Calculus of Variations, 2023, Vol. 29, 56.
* [20]

  Fujii, M., Sekine, M., Mean-field equilibrium price formation with exponential utility,
  Stochastics and Dynamics, 2025, Vol. 24, No.8, 255001-36.
* [21]

  Fujii, M., Sekine, M., Mean field equilibrium asset pricing model with habit formation,
  Asia-Pacific Financial Markets, published online in 2025,
* [22]

  Fujii, M., and Takahashi, A., A mean field game approach to equilibrium pricing with market clearing condition,
  SIAM J. Control. Optim. , 2022, Vol. 1, pp. 259-279.
* [23]

  Fujii, M., and Takahashi, A., Strong convergence to the mean-field limit of a finite agent equilibrium,
  SIAM J. Financial Math. , 2022, Vol. 13, No. 2, pp. 459-490.
* [24]

  Fujii, M. and Takahashi, A., Equilibrium price formation with a major player and its mean field limit,
  ESAIM: Control, Optimization and Calculus of Variations, 2022, Vol. 28, 21.
* [25]

  Gabaix, X, Lasry, J.M. , Lions, P.L. and Moll, B.,The dynamics of inequality,
  Econometrica, 2016, Vol. 84, No. 6, 2071-2111.
* [26]

  Gomes, D.A., Gutierrez, J., and Ribeiro, R., A random-supply mean field game price model,
  SIAM J. Financial Math., 2023, Vol. 14, No. 1, pp. 1888-222.
* [27]

  Gomes, D.A. and Saúde, J., A mean-field game approach to price formation,
  Dyn Games Appl, 2020, https://doi.org/10.1007/s13235-020-00348-x.
* [28]

  Hu, Y., Imkeller, P. and Müller, M., Utility maximization in incomplete markets,
  The Annals of Applied Probability, 2005, 15 (3) : 1691-1712.
* [29]

  Hu, R. and Zariphopoulou, T., N-player and mean-field games in Itˆo-diffusion markets with competitive
  or homophilous interaction, Stochastic Analysis, Filtering, and Stochastic Optimization: A
  Commemorative Volume to Honor Mark HA Davis’s Contributions, 2022.
* [30]

  Lacker, D. and Zariphopoulou, T., Mean field and n-agent games for optimal investment under
  relative performance criteria, Mathematical Finance, 2019, 29 (4):1003–1038.
* [31]

  Lacker, D. and Soret, A., Many-player games of optimal consumption and investment under relative
  performance criteria, Mathematics and Financial Economics, 2020, 14(2):263–281.
* [32]

  Sarto, G.D., Leocata, M. and Livieri, G., A mean field game approach for pollution regulation of competitive firms,
  2024, preprint, arXiv:2407.1275.
* [33]

  Shrivats, A., Firoozi, D. and Jaimungal, S., A mean-field game approach to equilibrium pricing,
  optimal generation, and trading in solar renewable energy certificate markets,
  Mathematical Finance, 2020, Vol. 32, Issue 3, pp. 779-824.
* [34]

  Huang, M., Malhame, R. and Caines, P.E., Large population stochastic dynamic games:
  closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle, Commun. Inf. Syst., 2006,
  Vol. 6, No. 3, pp.221-252.
* [35]

  Huang, M., Malhame, R. and Caines, P.E., An invariance principle in large population stochastic dynamics games, Jrl Syst Sci & Complexity,
  2007, Vol. 20, pp. 162-172.
* [36]

  Huang, M., Malhame, R. and Caines, P.E., Large-population cost-coupled LQG problems with nonuniform agents:
  individual-mass behavior and decentralized ϵ\epsilon-Nash equilibria, IEEE Transactions on Automatic Control, 2007, Vol. 52, No. 9, pp. 1560-1571.
* [37]

  Kato, T., Perturbation Theory for Linear Operators,
  Springer, 1995, NY.
* [38]

  Klenke, A., Probability Theorey: A comprehensive course, Third Edition, 2020, Springer Switzerland.
* [39]

  Lasry, J. M. and Lions, P.L., Jeux a champ moyen I. Le cas stationnaire, C. R. Sci. Math. Acad. Paris, 2006,
  343 pp. 619-625.
* [40]

  Lasry, J. M. and Lions, P.L., Jeux a champ moyen II. Horizon fini et controle optimal,
  C. R. Sci. Math. Acad. Paris, 2006, 343, pp. 679-684.
* [41]

  Lasry, J.M. and Lions, P.L., Mean field games, Jpn. J. Math., 2007, Vol. 2, pp. 229-260.
* [42]

  Liu, W. and Röckner, M., Stochastic Partial Differential Equations: An Introduction,
  Springer, Universitext, 2015, NY.
* [43]

  Sharpe, W.F., 1978, Investments (Prentice-Hall, Englewood Chffs, NJ)