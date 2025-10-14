---
authors:
- Masaaki Fujii
doc_id: arxiv:2510.11261v1
family_id: arxiv:2510.11261
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible
  in any manner for any losses caused by the use of any contents in this research.
url_abs: http://arxiv.org/abs/2510.11261v1
url_html: https://arxiv.org/html/2510.11261v1
venue: arXiv q-fin
version: 1
year: 2025
---


Masaaki Fujii222mfujii@e.u-tokyo.ac.jp, Graduate School of Economics, The University of Tokyo, Tokyo, Japan

(
First version: October 13, 2025
  
)

###### Abstract

In this work, we combine the mean-field game theory with the classical idea of binomial tree framework, pioneered by Sharpe and Cox, Ross & Rubinstein, to solve the equilibrium price formation problem for the stock.
For agents with exponential utilities
and recursive utilities of exponential type, we prove the existence of a unique mean-field equilibrium and derive an explicit formula for equilibrium transition probabilities of the stock price by restricting its trajectories onto a binomial tree.
The agents are subject to stochastic terminal liabilities and incremental endowments, both of which are dependent on unhedgeable common and idiosyncratic factors, in addition to the stock price path. Finally, we provide numerical examples to illustrate the qualitative effects of these components on the equilibrium price distribution.

Keywords:
mean-field game theory, multi-population, equilibrium price formation, exponential utility, recursive utility, binomial tree

## 1 Introduction

The mean-field game (MFG) theory was pioneered independently by the seminal works
of Lasry & Lions [[33](https://arxiv.org/html/2510.11261v1#bib.bib33), [34](https://arxiv.org/html/2510.11261v1#bib.bib34), [35](https://arxiv.org/html/2510.11261v1#bib.bib35)] and Huang et al. [[27](https://arxiv.org/html/2510.11261v1#bib.bib27), [28](https://arxiv.org/html/2510.11261v1#bib.bib28), [29](https://arxiv.org/html/2510.11261v1#bib.bib29)] in the mid- to late-2000s.
These works are based on analytic methods using coupled Hamilton-Jacobi-Bellman and Kolmogorov equations.
Later, the probabilistic approach to the MFG theory based on forward-backward stochastic differential equations (FBSDEs)
of McKean-Vlasov type was established by Carmona & Delarue [[9](https://arxiv.org/html/2510.11261v1#bib.bib9), [10](https://arxiv.org/html/2510.11261v1#bib.bib10)].
The two volumes, [[11](https://arxiv.org/html/2510.11261v1#bib.bib11)] and [[12](https://arxiv.org/html/2510.11261v1#bib.bib12)] , by the same authors,
provide full details on the probabilistic approach and its applications.

The greatest advantage of the MFG theory is that it can convert a complex problem of stochastic differential games
among many agents into a standard optimization problem and a fixed-point problem.
There is a growing number of studies in the literature attempting to solve many-agent problems
by the MFG technique. The MFG theory requires, in principle, symmetric interactions among the agents.
We can find a particularly large number of applications of MFGs in financial and energy markets
because symmetric interactions are standard in these settings.
There are also many economic applications of mean field games, in particular, those focusing on general equilibrium models on growth, inequality and unemployment, dynamic demand response and persuasion problems, etc. See, for example, [[1](https://arxiv.org/html/2510.11261v1#bib.bib1), [2](https://arxiv.org/html/2510.11261v1#bib.bib2), [3](https://arxiv.org/html/2510.11261v1#bib.bib3), [4](https://arxiv.org/html/2510.11261v1#bib.bib4), [5](https://arxiv.org/html/2510.11261v1#bib.bib5), [22](https://arxiv.org/html/2510.11261v1#bib.bib22)] and the references therein.

In recent years, there have also been major advances in MFG theory for applications in the equilibrium price-formation problem,
where the asset price process is constructed endogenously to ensure that the asset’s supply and demand always balance among the heterogeneous
but exchangeable agents, rather than being exogenously given.
Gomes & Saúde [[24](https://arxiv.org/html/2510.11261v1#bib.bib24)] present a deterministic model
of electricity price. Its extension with random supply is given by Gomes et al.[[23](https://arxiv.org/html/2510.11261v1#bib.bib23)].
Ashrafyan et.al. [[6](https://arxiv.org/html/2510.11261v1#bib.bib6)] propose a duality approach transforming these problems
into variational ones that are numerically more tractable.
Shrivats et al. [[39](https://arxiv.org/html/2510.11261v1#bib.bib39)] deal with a price formation problem for
the solar renewable energy certificate (SREC) by solving FBSDEs of McKean-Vlasov type.
Féron et.al. [[15](https://arxiv.org/html/2510.11261v1#bib.bib15)] develop a tractable equilibrium model for intraday electricity markets.
Sarto et.al. [[36](https://arxiv.org/html/2510.11261v1#bib.bib36)] study cap-and-trade pollution regulation and derive
the equilibrium price for the carbon emission.
Regarding the price formation of securities, Fujii & Takahashi [[16](https://arxiv.org/html/2510.11261v1#bib.bib16)] show
that the equilibrium price process can be characterized by FBSDEs of conditional
McKean-Vlasov type. Its strong convergence to the mean-field limit from a finite-agent setting
is proved in [[17](https://arxiv.org/html/2510.11261v1#bib.bib17)], and its extension to the presence of a major player is given in [[18](https://arxiv.org/html/2510.11261v1#bib.bib18)] by the same authors.
Fujii [[19](https://arxiv.org/html/2510.11261v1#bib.bib19)] develops a model that allows the co-presence of cooperative and non-cooperative populations to
learn how the price process is formed when the agents in one population act in a coordinated manner.

There remain two limitations in the above results: firstly, the
relevant control of each agent is the trading rate and hence her asset position is constrained to follow an absolutely continuous process with
respect to the Lebesgue measure d​tdt; secondly, the cost function of each agent consists of penalties on the
trading speed and on the inventory size of the assets. Therefore, the above
frameworks cannot deal with the general self-financing trading strategies nor the utility functions defined directly in terms of the
wealth process of the portfolio. A major obstacle in dealing with a utility function of the wealth resides in the difficulty of guaranteeing
the convexity of the Hamiltonian associated with the Pontryagin’s maximum principle and in the difficulty of getting
enough regularity to prove the well-posedness of the associated FBSDEs.
These problems are solved by Fujii & Sekine [[20](https://arxiv.org/html/2510.11261v1#bib.bib20), [21](https://arxiv.org/html/2510.11261v1#bib.bib21)] for the agents with exponential utilities by applying the method of Hu, Imkeller & Müller [[26](https://arxiv.org/html/2510.11261v1#bib.bib26)]
based on the martingale optimality principle. An extension to the setting with partial information is studied by Sekine [[37](https://arxiv.org/html/2510.11261v1#bib.bib37)].
They find that a novel quadratic-growth backward SDE (qg-BSDE) of conditional McKean-Vlasov type characterizes the equilibrium risk-premium process. Unfortunately, however, the existence of the solution of this mean-field qg-BSDE has been proved
only under rather restrictive conditions. This is because the conditional McKean-Vlasov nature of the equation
makes the traditional approach of Kobylanski [[32](https://arxiv.org/html/2510.11261v1#bib.bib32)] inapplicable anymore.
Moreover, even if the well-posedness of the equation were to be completely solved, its
numerical evaluation would continue to remain a highly challenging problem.

In this work, we study the price-formation problem for the risky stock.
In order to understand how the equilibrium price process changes its behavior due to the market environment
and the differences in the distribution of characteristics among the agents,
it is necessary to get more explicit and more numerically tractable solutions than those in the existing literature.
For proceeding toward this goal, in this paper, we propose an approach to combine the MFG theory with a
classical idea of binomial trees, first proposed by Sharpe [[38](https://arxiv.org/html/2510.11261v1#bib.bib38)] and formalized by Cox, Ross & Rubinstein [[13](https://arxiv.org/html/2510.11261v1#bib.bib13)].
By restricting the stock price trajectories onto a binomial tree,
we can search, in a rather straightforward manner, an appropriate set of transition probabilities so that the stock market clears.
The agents, which are mainly intended to be financial and investment firms,
are supposed to have standard exponential utilities or recursive utilities of exponential type.
We allow the presence of terminal liability and incremental endowments,
both of which are stochastic due to unhedgeable common factors YY as well as idiosyncratic factors ZiZ^{i} in addition to the
stock price dependence. Since we are focusing on a trading desk of each firm, the incremental endowments
represent non-tradable incomes originating from the firm’s other business activities.
We also study the impacts of external order flow from outside groups
or possibly from a major financial player.
Simple and explicit expressions for the equilibrium transition probabilities allow us to numerically evaluate the marginal
equilibrium price distributions as well as conditional distributions with respect to the common factors YY
and to study their qualitative behaviors with respect to the components just mentioned above.
Moreover, our scheme can be readily extended to multi-population equilibrium problems.
This is clear contrast to the continuous-time setting as in [[20](https://arxiv.org/html/2510.11261v1#bib.bib20), [21](https://arxiv.org/html/2510.11261v1#bib.bib21)], where the extension
would require to solve a coupled system of complex mean-field qg-BSDEs, whose
well-posedness would be much more challenging than a single population case.

We structure the rest of the paper as follows: Section [2](https://arxiv.org/html/2510.11261v1#S2 "2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") investigates the mean-field equilibrium
among the agents with exponential utilities subject to terminal liabilities. Section [3](https://arxiv.org/html/2510.11261v1#S3 "3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") deals with an extension
to recursive utilities and also introduces cash spending (i.e. nominal consumption) and incremental endowments.
Section [4](https://arxiv.org/html/2510.11261v1#S4 "4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") provides several illustrative numerical examples and examines their implications.
Section [5](https://arxiv.org/html/2510.11261v1#S5 "5 Concluding remarks and future research directions ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") summarizes our findings and discusses possible directions for future research.

## 2 Utility optimization for terminal wealth

We start our investigation into the mean-field price formation from a simple model where a countable number of agents,
whose utilities are exponential type,
are optimizing their terminal wealth by carrying out self-financing trading strategies on a deterministic money market account
and a single risky stock.
Each agent has to manage financial risk arising from the common market shocks as well as her own idiosyncratic shocks.
Note that, in addition to the shocks from the stock price process, our model incorporates non-tradable macro-economic and/or environmental shocks that affect all agents.

### 2.1 The setup and notation

Let us start from explaining the relevant probability spaces.
(Ω0,ℱ0,(ℱtn0)n=1N,ℙ0)(\Omega^{0},{\cal F}^{0},({\cal F}\_{t\_{n}}^{0})\_{n=1}^{N},\mathbb{P}^{0}) is a complete filtered probability space, where 0=t0<t1<⋯<tN=T0=t\_{0}<t\_{1}<\cdots<t\_{N}=T
is an equally spaced time sequence using a time step Δ:=T/N\Delta:=T/N where T<∞T<\infty and N∈ℕN\in\mathbb{N} are given constants.
The filtration (ℱtn0)n=0N({\cal F}\_{t\_{n}}^{0})\_{n=0}^{N} is generated by two stochastic processes, one is a strictly positive process (Sn:=S​(tn))n=0N(S\_{n}:=S(t\_{n}))\_{n=0}^{N}
and the other is a dYd\_{Y}-dimensional process (Yn=Y​(tn))n=0N(Y\_{n}=Y(t\_{n}))\_{n=0}^{N}, i.e. ℱtn0:=σ​{Sk,Yk,0≤k≤n}{\cal F}\_{t\_{n}}^{0}:=\sigma\{S\_{k},Y\_{k},0\leq k\leq n\}.
In the model below, we shall use SnS\_{n} to denote the stock price at tnt\_{n} and YnY\_{n} the common shocks affecting all the agents at tnt\_{n}.
S0>0S\_{0}>0 and Y0∈ℝdYY\_{0}\in\mathbb{R}^{d\_{Y}} are given constants and thus ℱ00{\cal F}\_{0}^{0} is trivial.

In addition to the above space,
we consider a countable set of complete filtered probability spaces (Ωi,ℱi,(ℱtni)n=0N,ℙi),i∈ℕ(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}),~i\in\mathbb{N}.
For each ii, (Ωi,ℱi,(ℱtni)n=0N,ℙi)(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}) is endowed with
ℱ0i{\cal F}^{i}\_{0}-measurable random variables (ξi,γi)(\xi^{i},\gamma\_{i}) as well as (ℱtni)n=0N({\cal F}^{i}\_{t\_{n}})\_{n=0}^{N}-adapted
stochastic process (Zni=Zi​(tn))n=0N(Z\_{n}^{i}=Z^{i}(t\_{n}))\_{n=0}^{N}. Here, ξi,γi\xi\_{i},\gamma\_{i} are both ℝ\mathbb{R}-valued
and ξi\xi\_{i} is used to represent the initial wealth and γi\gamma\_{i} the size of absolute risk aversion
of agent-ii. The dZd\_{Z}-dimensional process (Zni)n=0N(Z\_{n}^{i})\_{n=0}^{N} is used to model idiosyncratic shocks to each agent.
The fact that (ξi,γi)(\xi^{i},\gamma\_{i}) are ℱ0i{\cal F}\_{0}^{i}-measurable means that the agent-ii knows her
initial wealth and the size of risk aversion at time zero.

By the standard procedures (see, for example, Klenke [[31](https://arxiv.org/html/2510.11261v1#bib.bib31), Chapter 14]), the complete filtered probability space
(Ω,ℱ,(ℱtn)n=0N,ℙ)(\Omega,{\cal F},({\cal F}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}) is defined as the product of all the above spaces

|  |  |  |
| --- | --- | --- |
|  | (Ω,ℱ,(ℱtn)n=0N,ℙ):=(Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)⊗i=1∞(Ωi,ℱi,(ℱtni)n=0N,ℙi)(\Omega,{\cal F},({\cal F}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}):=(\Omega^{0},{\cal F}^{0},({\cal F}\_{t\_{n}}^{0})\_{n=0}^{N},\mathbb{P}^{0})\otimes\_{i=1}^{\infty}(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}) |  |

which denotes the full probability space containing the entire environment of our model.
Therefore, by construction, ((Sn),(Yn))((S\_{n}),(Y\_{n})) and (ξi,γi,(Zni)),i∈ℕ(\xi^{i},\gamma\_{i},(Z\_{n}^{i})),~i\in\mathbb{N} are mutually independent.
On the other hand, the relevant probability space for each agent-ii is the product probability space defined by

|  |  |  |
| --- | --- | --- |
|  | (Ω0,i,ℱ0,i,(ℱtn0,i)n=0N,ℙ0,i):=(Ω0,ℱ0,(ℱtn0)n=0N,ℙ0)⊗(Ωi,ℱi,(ℱtni)n=0N,ℙi),(\Omega^{0,i},{\cal F}^{0,i},({\cal F}\_{t\_{n}}^{0,i})\_{n=0}^{N},\mathbb{P}^{0,i}):=(\Omega^{0},{\cal F}^{0},({\cal F}\_{t\_{n}}^{0})\_{n=0}^{N},\mathbb{P}^{0})\otimes(\Omega^{i},{\cal F}^{i},({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N},\mathbb{P}^{i}), |  |

which reflects our assumption that common shocks are public knowledge, but the idiosyncratic shocks are private to
each agent.
We shall use the same symbols, such as (Sn,Yn,γi,⋯)(S\_{n},Y\_{n},\gamma\_{i},\cdots), if they are
defined as trivial extensions on larger product probability spaces.
Expectations with respect to ℙ0\mathbb{P}^{0}, ℙ0,i\mathbb{P}^{0,i} and ℙ\mathbb{P} are denoted by 𝔼0​[⋅]\mathbb{E}^{0}[\cdot], 𝔼0,i​[⋅]\mathbb{E}^{0,i}[\cdot]
and 𝔼​[⋅]\mathbb{E}[\cdot], respectively. We also denote by E¯​[⋅]\overline{E}[\cdot] the expectation with respect to the product measure
⊗i=1∞ℙi\otimes\_{i=1}^{\infty}\mathbb{P}^{i}.

In this work, we restrict the trajectories of (Sn)n=0N(S\_{n})\_{n=0}^{N} on a recombining binomial tree. For each n=1,⋯,Nn=1,\cdots,N,
the random variable R~n:=Sn/Sn−1\widetilde{R}\_{n}:=S\_{n}/S\_{n-1} takes only the two possible values, either u~\widetilde{u} or d~\widetilde{d}.
This means that the set of all possible values taken by SnS\_{n} is given by 𝒮n:={S0​u~k​d~n−k,0≤k≤n}{\cal S}\_{n}:=\{S\_{0}\widetilde{u}^{k}\widetilde{d}^{n-k},0\leq k\leq n\},
which is a finite subset of (0,∞)(0,\infty).
Let 𝒮n:=𝒮0×𝒮1×𝒮2×⋯×𝒮n{\cal S}^{n}:={\cal S}\_{0}\times{\cal S}\_{1}\times{\cal S}\_{2}\times\cdots\times{\cal S}\_{n}
be the set of all values taken by the stock price trajectory (Sk)k=0n(S\_{k})\_{k=0}^{n}.
Moreover, in order to avoid technicalities regarding the conditional probabilities, we also assume that
the process YY takes only a finite number of values at every tnt\_{n}. We use 𝒴n{\cal Y}\_{n}, which is a
finite subset of ℝdY\mathbb{R}^{d\_{Y}}, to denote the set of all values taken by YnY\_{n}.
We use, for each 0≤n≤N0\leq n\leq N, 𝒴n:=𝒴0×𝒴1×⋯×𝒴n{\cal Y}^{n}:={\cal Y}\_{0}\times{\cal Y}\_{1}\times\cdots\times{\cal Y}\_{n} to represent the set of all values in
ℝdY×(n+1)\mathbb{R}^{d\_{Y}\times(n+1)} taken by the trajectory (Yk)k=0n(Y\_{k})\_{k=0}^{n}.
In a similar manner, we denote the support of the random variable ZniZ\_{n}^{i} by 𝒵n{\cal Z}\_{n}
and define 𝒵n:=𝒵0×𝒵1×⋯×𝒵n{\cal Z}^{n}:={\cal Z}\_{0}\times{\cal Z}\_{1}\times\cdots\times{\cal Z}\_{n} as the support of (Zki)k=0n(Z\_{k}^{i})\_{k=0}^{n}.
The time-tnt\_{n} value of the risk-free money market account is given by exp⁡(r​n​Δ)\exp\bigl(rn\Delta\bigr)
where r>0r>0 is a positive constant denoting the risk-free (nominal) interest rate. We also use the symbol β:=exp⁡(r​Δ)\beta:=\exp(r\Delta).
For later use, let us also define

|  |  |  |
| --- | --- | --- |
|  | u:=u~−exp⁡(r​Δ),d:=d~−exp⁡(r​Δ)u:=\widetilde{u}-\exp(r\Delta),\quad d:=\widetilde{d}-\exp(r\Delta) |  |

and

|  |  |  |
| --- | --- | --- |
|  | Rn:=R~n−exp⁡(r​Δ),1≤n≤N.R\_{n}:=\widetilde{R}\_{n}-\exp(r\Delta),~1\leq n\leq N. |  |

The random variable RnR\_{n} takes the values either uu or dd.

In the following, to lighten the notational burden, we use 𝔼0,i[⋅|s,y,zi,γi]\mathbb{E}^{0,i}\bigl[~\cdot~|s,y,z^{i},\gamma\_{i}\bigr] to denote
𝔼0,i[⋅|Sn−1=s,Yn−1=y,Zn−1i=zi,γi=γi]\mathbb{E}^{0,i}\bigl[~\cdot~|S\_{n-1}=s,Y\_{n-1}=y,Z\_{n-1}^{i}=z^{i},\gamma\_{i}=\gamma\_{i}\bigr] for (s,y,zi)∈𝒮n−1×𝒴n−1×𝒵n−1(s,y,z^{i})\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}.
With slight abuse of notation, we shall use the same symbols for the realizations of ℱ0i{\cal F}^{i}\_{0}-measurable random variables
(γi\gamma\_{i} in the above example).

###### Assumption 2.1.

(i): u~\widetilde{u} and d~\widetilde{d} are real constants satisfying

|  |  |  |
| --- | --- | --- |
|  | 0<d~<exp⁡(r​Δ)<u~<∞.0<\widetilde{d}<\exp(r\Delta)<\widetilde{u}<\infty. |  |

(ii): Every (ξi,γi,(Zni)n=0N),i=1,2,…(\xi^{i},\gamma\_{i},(Z\_{n}^{i})\_{n=0}^{N}),i=1,2,\ldots has the same distribution.
  
(iii): There exist constants ξ¯,ξ¯\underline{\xi},\overline{\xi} and γ¯,γ¯\underline{\gamma},\overline{\gamma} so that for every i∈ℕi\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | ξi∈[ξ¯,ξ¯]⊂ℝ,γi∈Γ:=[γ¯,γ¯]⊂(0,∞).\xi\_{i}\in[\underline{\xi},\overline{\xi}]\subset\mathbb{R},\quad\gamma\_{i}\in\Gamma:=[\underline{\gamma},\overline{\gamma}]\subset(0,\infty). |  |

(iv): For every 0≤n≤N0\leq n\leq N, 𝒵n{\cal Z}\_{n} is a bounded subset
of ℝdZ\mathbb{R}^{d\_{Z}}.
  
(v): For each ii, (Zni)n=0N(Z\_{n}^{i})\_{n=0}^{N} is a Markov process i.e. 𝔼i​[f​(Zni)|ℱtmi]=𝔼i​[f​(Zni)|Zmi]\mathbb{E}^{i}[f(Z\_{n}^{i})|{\cal F}\_{t\_{m}}^{i}]=\mathbb{E}^{i}[f(Z\_{n}^{i})|Z\_{m}^{i}]
for every bounded measurable function ff on 𝒵n{\cal Z}\_{n} and m≤nm\leq n.
  
(vi): (Yn)n=0N(Y\_{n})\_{n=0}^{N} is a Markov process i.e. 𝔼0​[f​(Yn)|ℱtm0]=𝔼0​[f​(Yn)|Ym]\mathbb{E}^{0}[f(Y\_{n})|{\cal F}\_{t\_{m}}^{0}]=\mathbb{E}^{0}[f(Y\_{n})|Y\_{m}]
for every bounded measurable function ff on 𝒴n{\cal Y}\_{n} and m≤nm\leq n.
  
(vii): The transition probabilities of (Sn)n=0N(S\_{n})\_{n=0}^{N} satisfy, for every 0≤n≤N−10\leq n\leq N-1,

|  |  |  |
| --- | --- | --- |
|  | ℙ0​(Sn+1=u~​Sn|ℱtn0)=ℙ0​(Sn+1=u~​Sn|Sn,Yn)=pn​(Sn,Yn),ℙ0​(Sn+1=d~​Sn|ℱtn0)=ℙ0​(Sn+1=d~​Sn|Sn,Yn)=qn​(Sn,Yn):=1−pn​(Sn,Yn),\begin{split}\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|{\cal F}\_{t\_{n}}^{0})&=\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|S\_{n},Y\_{n})=p\_{n}(S\_{n},Y\_{n}),\\ \mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|{\cal F}\_{t\_{n}}^{0})&=\mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|S\_{n},Y\_{n})=q\_{n}(S\_{n},Y\_{n}):=1-p\_{n}(S\_{n},Y\_{n}),\end{split} |  |

where pn,qn:𝒮n×𝒴n→ℝ,0≤n≤N−1p\_{n},q\_{n}:{\cal S}\_{n}\times{\cal Y}\_{n}\rightarrow\mathbb{R},~0\leq n\leq N-1 are bounded measurable functions
satisfying

|  |  |  |
| --- | --- | --- |
|  | 0<pn​(s,y),qn​(s,y)<10<p\_{n}(s,y),q\_{n}(s,y)<1 |  |

for every (s,y)∈𝒮n×𝒴n(s,y)\in{\cal S}\_{n}\times{\cal Y}\_{n}.

Let us give some remarks on the above assumptions.
Firstly, by the condition (i), we have d<0<ud<0<u.
It is well-known that the transition probabilities under the risk-neutral measure ℚ\mathbb{Q}
for the classical binomial framework are given by pℚ:=−du−dp^{\mathbb{Q}}:=\frac{-d}{u-d} for the up-move and qℚ:=1−pℚq^{\mathbb{Q}}:=1-p^{\mathbb{Q}} for the down-move.
These probabilities are uniquely determined by the parameters (u~,d~)(\widetilde{u},\widetilde{d}) and the risk-free interest rate.
In this paper, we fix the relative jump size (u~,d~)(\widetilde{u},\widetilde{d}) to be constant across all nodes; however this is done merely for simplicity.
The entire discussion of our paper still holds even if (u~,d~)(\widetilde{u},\widetilde{d}) varies from node to node.
In fact, the method works even for general non-recombining binomial trees.
Moreover, thanks to the famous result by Derman & Kani (1994) [[14](https://arxiv.org/html/2510.11261v1#bib.bib14)], one can construct so-called “implied binomial trees”
by adjusting the position (u~,d~)(\widetilde{u},\widetilde{d}) node by node to reproduce implied volatility surface
in the market, while keeping the recombining property of binomial trees intact.
Therefore, if necessary, our discussion below can be applied to a binomial tree whose risk-neutral distribution is consistent with the option market.
The boundedness assumption in (iii) and (iv) is not crucial. One can relax it by adding appropriate integrability conditions.

Our goal in this section is to find a set of transition probabilities of the form (pn​(s,y))n=0N−1\bigl(p\_{n}(s,y))\_{n=0}^{N-1} so that the demand and
supply of the stock are balanced among the agents at every node (s,y)∈𝒮n×𝒴n,0≤n≤N−1(s,y)\in{\cal S}\_{n}\times{\cal Y}\_{n},0\leq n\leq N-1.
Note that we can assume, without any loss of generality, that the process (Yn)n=0N(Y\_{n})\_{n=0}^{N} and (Zni)n=0N(Z\_{n}^{i})\_{n=0}^{N}
are Markov, since, if necessary, we can recover Markovian property by lifting Y,ZiY,Z^{i} to higher dimensional processes.
However, the condition (vii) is not trivial. In fact, in the next section, we shall study more general
situations where the transition probability must be dependent on the past history of the stock price to achieve the market-clearing equilibrium.
Under the current condition (vi) and (vii), (Sn+1,Yn+1)(S\_{n+1},Y\_{n+1}) satisfy the property:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼0​[f​(Sn+1)​g​(Yn+1)|ℱtn0]=𝔼0​[f​(Sn+1)|Sn,Yn]​𝔼0​[g​(Yn+1)|Yn],0≤n≤N−1,\mathbb{E}^{0}[f(S\_{n+1})g(Y\_{n+1})|{\cal F}\_{t\_{n}}^{0}]=\mathbb{E}^{0}[f(S\_{n+1})|S\_{n},Y\_{n}]\mathbb{E}^{0}[g(Y\_{n+1})|Y\_{n}],\quad 0\leq n\leq N-1, |  | ( 2.1) |

for any bounded measurable functions ff and gg.
We can interpret that the process (Yn)n=0N(Y\_{n})\_{n=0}^{N} represents some standalone macro-economic and/or environmental factors
which are not influenced by the agents’ trading activities. It may naturally serve as a state process in regime switching models.

###### Remark 2.1.

Note that the bound for the transition probabilities in (vii) guarantees the equivalence of probability measures ℙ0∘Sn−1\mathbb{P}^{0}\circ S\_{n}^{-1} and
ℚ∘Sn−1\mathbb{Q}\circ S\_{n}^{-1}. Hence, our system is arbitrage free.

### 2.2 The individual optimization problem

We now explain the optimization problem for each agent. Agent-ii, i∈ℕi\in\mathbb{N}, endowed with an initial wealth ξi\xi\_{i},
engages in self-financing trading involving the risk-free money market account and the risky stock.
She adopts an (ℱtn0,i)n=0N−1({\cal F}\_{t\_{n}}^{0,i})\_{n=0}^{N-1}-adapted trading strategy (ϕni)n=0N−1(\phi\_{n}^{i})\_{n=0}^{N-1} denoting the
invested amount of cash in the stock at time t=tnt=t\_{n}. The associated wealth process of agent-ii
is denoted by (Xni=Xi​(tn))n=0N(X\_{n}^{i}=X^{i}(t\_{n}))\_{n=0}^{N} and follows the dynamics

|  |  |  |
| --- | --- | --- |
|  | Xn+1i=exp⁡(r​Δ)​(Xni−ϕni)+ϕni​R~n+1=β​Xni+ϕni​Rn+1,\begin{split}X\_{n+1}^{i}&=\exp(r\Delta)(X\_{n}^{i}-\phi\_{n}^{i})+\phi\_{n}^{i}\widetilde{R}\_{n+1}\\ &=\beta X\_{n}^{i}+\phi\_{n}^{i}R\_{n+1},\end{split} |  |

where X0i=ξiX\_{0}^{i}=\xi\_{i} and β=exp⁡(r​Δ)\beta=\exp(r\Delta). Recall that Rn+1:=R~n+1−exp⁡(r​Δ)R\_{n+1}:=\widetilde{R}\_{n+1}-\exp(r\Delta).

Each agent-ii is supposed to solve the optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(ϕni)n=0N−1∈𝔸i𝔼0,i​[−exp⁡(−γi​(XNi−F​(SN,YN,ZNi)))|ℱ00,i],\begin{split}\sup\_{(\phi\_{n}^{i})\_{n=0}^{N-1}\in\mathbb{A}^{i}}\mathbb{E}^{0,i}\Bigl[-\exp\Bigl(-\gamma\_{i}\bigl(X\_{N}^{i}-F(S\_{N},Y\_{N},Z\_{N}^{i})\bigr)\Bigr)|{\cal F}\_{0}^{0,i}\Bigr],\end{split} |  | ( 2.2) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝔸i:={(ϕni)n=0N−1;ϕni​ is ℱtn0,i-measurable real random variable}\mathbb{A}^{i}:=\bigl\{(\phi\_{n}^{i})\_{n=0}^{N-1};\phi\_{n}^{i}\text{ is ${\cal F}\_{t\_{n}}^{0,i}$-measurable real random variable}\bigr\} |  |

denotes the admissible control space.
Here, we assume that agent-ii has full knowledge of the common market information and her own private idiosyncratic information,
but no knowledge of the private idiosyncratic information of the other agents.

###### Assumption 2.2.

(i): F:𝒮N×𝒴N×𝒵N→ℝF:{\cal S}\_{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}\rightarrow\mathbb{R} is a bounded measurable function.
  
(ii): Every agent is a price-taker in the sense that she considers that the stock price process (and hence its transition
probability specified in Assumption [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") (vii)) to be exogenously given and unaffected by her trading strategies.

Here, the term F​(SN,YN,ZNi)F(S\_{N},Y\_{N},Z\_{N}^{i}) denotes the stochastic liability ((−1)×(-1)\times stochastic endowment) at the terminal time,
which depends on SN,YNS\_{N},Y\_{N} and ZNiZ\_{N}^{i}.
Under the exponential utilities, the constant shift F→F+cF\rightarrow F+c
does not change the optimization problem; only the dependence on (SN,YN,ZNi)(S\_{N},Y\_{N},Z\_{N}^{i})
in the function FF is relevant.
The condition (ii) is a plausible assumption since every agent naturally knows her trading share is negligible in the market.
This is also a key assumption for the standard MFG technique, in which we first solve a simple optimization problem with a given
candidate for the equilibrium distribution, and then check its consistency with the obtained optimal solution.

###### Remark 2.2.

Before going to solve the optimization problem, we give some economic motivations to include the stochastic terminal liability
F​(SN,YN,ZNi)F(S\_{N},Y\_{N},Z\_{N}^{i}). Since we primarily want to model various financial firms by our agents,
it is natural to suppose that they are subject to stochastic liabilities (such as portfolio of derivative contracts) dependent on the stock price.
It is also very plausible that the size of liability varies from agent to agent by their idiosyncratic factors (ZNi)(Z\_{N}^{i})
as well as the common macro-economic/environmental factors (YN)(Y\_{N}). This structure would naturally hold for non-financial firms, too.

We now characterize the optimal trading strategy for each agent.
Applying the well-known scheme of backward induction for discrete-time models, we establish the following result.
We shall see that the initial wealth ξi\xi\_{i} does not play any role, which is an important characteristic
of exponential-type utilities.

###### Theorem 2.1.

Let Assumptions [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") be in force.
Then the problem ([2.2](https://arxiv.org/html/2510.11261v1#S2.E2 "In 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{problem-terminal}) has a unique optimal solution (ϕn−1i,∗)n=1N(\phi^{i,\*}\_{n-1})\_{n=1}^{N},
which is an a.s. bounded process defined by a
measurable function ϕn−1i,∗:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝ\phi\_{n-1}^{i,\*}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}
as ϕn−1i,∗:=ϕn−1i,∗​(Sn−1,Yn−1,Zn−1i,γi)\phi\_{n-1}^{i,\*}:=\phi\_{n-1}^{i,\*}(S\_{n-1},Y\_{n-1},Z\_{n-1}^{i},\gamma\_{i}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1i,∗​(s,y,zi,γi):=1γi​(u−d)​βnβN​{log⁡(−pn−1​(s,y)​uqn−1​(s,y)​d)+log⁡(fn−1​(s,y,zi,γi))},fn−1​(s,y,zi,γi):=𝔼0,i​[Vn​(s​u~,Yn,Zni,γi)|y,zi,γi]𝔼0,i​[Vn​(s​d~,Yn,Zni,γi)|y,zi,γi].\begin{split}&\phi\_{n-1}^{i,\*}(s,y,z^{i},\gamma\_{i}):=\frac{1}{\gamma\_{i}(u-d)}\frac{\beta^{n}}{\beta^{N}}\Bigl\{\log\Bigl(-\frac{p\_{n-1}(s,y)u}{q\_{n-1}(s,y)d}\Bigr)+\log\bigl(f\_{n-1}(s,y,z^{i},\gamma\_{i})\bigr)\Bigr\},\\ &f\_{n-1}(s,y,z^{i},\gamma\_{i}):=\frac{\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]}{\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]}.\end{split} |  | ( 2.3) |

Here, fn−1:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝf\_{n-1}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R} and
Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}\_{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R}, 1≤n≤N1\leq n\leq N are a.s.​ strictly positive
bounded measurable functions defined recursively by

|  |  |  |
| --- | --- | --- |
|  | VN​(s,y,zi,γi):=exp⁡(γi​F​(s,y,zi)),V\_{N}(s,y,z^{i},\gamma\_{i}):=\exp\bigl(\gamma\_{i}F(s,y,z^{i})\bigr), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn−1​(s,y,zi,γi):=pn−1​(s,y)​e−γi​βNβn​ϕn−1i,∗​(s,y,zi,γi)​u​𝔼0,i​[Vn​(s​u~,Yn,Zni,γi)|y,zi,γi]+qn−1​(s,y)​e−γi​βNβn​ϕn−1i,∗​(s,y,zi,γi)​d​𝔼0,i​[Vn​(s​d~,Yn,Zni,γi)|y,zi,γi].\begin{split}V\_{n-1}(s,y,z^{i},\gamma\_{i})&:=p\_{n-1}(s,y)e^{-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}\phi^{i,\*}\_{n-1}(s,y,z^{i},\gamma\_{i})u}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]\\ &+q\_{n-1}(s,y)e^{-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}\phi^{i,\*}\_{n-1}(s,y,z^{i},\gamma\_{i})d}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}].\end{split} |  | ( 2.4) |

###### Proof.

With VN:𝒮N×𝒴N×𝒵N×Γ→ℝV\_{N}:{\cal S}\_{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}\times\Gamma\rightarrow\mathbb{R}
defined by VN​(s,y,zi,γi)=exp⁡(γi​F​(s,y,zi))V\_{N}(s,y,z^{i},\gamma\_{i})=\exp\bigl(\gamma\_{i}F(s,y,z^{i})\bigr), we temporarily suppose that
the problem of agent-ii at t=tn−1t=t\_{n-1}, 1≤n≤N1\leq n\leq N,
is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | supϕi𝔼0,i​[−exp⁡(−γi​βNβn​Xni)​Vn​(Sn,Yn,Zni,γi)|ℱtn−10,i],\sup\_{\phi^{i}}\mathbb{E}^{0,i}\Bigl[-\exp\Bigl(-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}X\_{n}^{i}\Bigr)V\_{n}(S\_{n},Y\_{n},Z\_{n}^{i},\gamma\_{i})|{\cal F}\_{t\_{n-1}}^{0,i}\Bigr], |  | ( 2.5) |

with some a.s. strictly positive bounded measurable function Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}\_{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R}.
Here, the supremum is taken over ℱn−10,i{\cal F}\_{n-1}^{0,i}-measurable real random variables.
Let us solve the above problem on the set {(Xn−1i,Sn−1,Yn−1,Zn−1i,γi)=(xi,s,y,zi,γi)}\{(X^{i}\_{n-1},S\_{n-1},Y\_{n-1},Z\_{n-1}^{i},\gamma\_{i})=(x^{i},s,y,z^{i},\gamma\_{i})\}333With slight
abuse of notation, we use the same symbols for the realizations of ℱ0i{\cal F}^{i}\_{0}-measurable random variables..
Then the above problem is equivalent to

|  |  |  |
| --- | --- | --- |
|  | infϕi∈ℝ𝔼0,i​[exp⁡(−γi​βNβn​(β​xi+ϕi​Rn))​Vn​(s​R~n,Yn,Zni,γi)|xi,y,zi,γi]=exp(−γiβNβn−1xi)infϕi∈ℝ{pn−1(s,y)e−γi​βNβn​ϕi​u𝔼0,i[Vn(su~,Yn,Zni,γi)|y,zi,γi]+qn−1(s,y)e−γi​βNβn​ϕi​d𝔼0,i[Vn(sd~,Yn,Zni,γi)|y,zi,γi]},\begin{split}&\inf\_{\phi^{i}\in\mathbb{R}}\mathbb{E}^{0,i}\Bigl[\exp\Bigl(-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}(\beta x^{i}+\phi^{i}R\_{n})\Bigr)V\_{n}(s\widetilde{R}\_{n},Y\_{n},Z\_{n}^{i},\gamma\_{i})\bigr|x^{i},y,z^{i},\gamma\_{i}\Bigr]\\ &=\exp\Bigl(-\gamma\_{i}\frac{\beta^{N}}{\beta^{n-1}}x^{i}\Bigr)\inf\_{\phi^{i}\in\mathbb{R}}\Bigl\{p\_{n-1}(s,y)e^{-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}\phi^{i}u}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]\\ &\qquad\qquad+q\_{n-1}(s,y)e^{-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}\phi^{i}d}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]\Bigr\},\end{split} |  |

where we have used the property given in Assumption [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") (vii).
Since d<0<ud<0<u, the optimal position ϕi,∗\phi^{i,\*} is a.s. uniquely characterized by

|  |  |  |
| --- | --- | --- |
|  | pn−1​(s,y)​u​e−γi​βNβn​ϕi,∗​u​𝔼0,i​[Vn​(s​u~,Yn,Zni,γi)|y,zi,γi]+qn−1​(s,y)​d​e−γi​βNβn​ϕi,∗​d​𝔼0,i​[Vn​(s​d~,Yn,Zni,γi)|y,zi,γi]=0.\begin{split}&p\_{n-1}(s,y)ue^{-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}\phi^{i,\*}u}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{u},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]\\ &\quad+q\_{n-1}(s,y)de^{-\gamma\_{i}\frac{\beta^{N}}{\beta^{n}}\phi^{i,\*}d}\mathbb{E}^{0,i}[V\_{n}(s\widetilde{d},Y\_{n},Z\_{n}^{i},\gamma\_{i})|y,z^{i},\gamma\_{i}]=0.\end{split} |  |

This gives the results given in ([2.3](https://arxiv.org/html/2510.11261v1#S2.E3 "In Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t1-eq1}), which is well-defined and bounded since VnV\_{n} is a strictly positive and bounded,
and 0<pn−1,qn−1<10<p\_{n-1},q\_{n-1}<1 by our assumption.

It follows that the function Vn−1V\_{n-1} defined by ([2.4](https://arxiv.org/html/2510.11261v1#S2.E4 "In Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t1-eq2}) becomes once again a.s. strictly positive and bounded
on 𝒮n−1×𝒴n−1×𝒵n−1×Γ{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma.
The value function at the next step tn−1t\_{n-1} is now defined by

|  |  |  |
| --- | --- | --- |
|  | −exp⁡(−γi​βNβn−1​Xn−1i)​Vn−1​(Sn−1,Yn−1,Zn−1i,γi)-\exp\Bigl(-\gamma\_{i}\frac{\beta^{N}}{\beta^{n-1}}X\_{n-1}^{i}\Bigr)V\_{n-1}(S\_{n-1},Y\_{n-1},Z\_{n-1}^{i},\gamma\_{i}) |  |

and we have recovered the problem of the same form as in ([2.5](https://arxiv.org/html/2510.11261v1#S2.E5 "In Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t1-temp1}).
Thus the repeat of the above procedures NN times yields the desired conclusion.
∎

### 2.3 Mean-field equilibrium under stochastic order flow

Our goal is to find a set of functions pn​(s,y),(s,y)∈𝒮n×𝒴n,0≤n≤N−1p\_{n}(s,y),(s,y)\in{\cal S}\_{n}\times{\cal Y}\_{n},0\leq n\leq N-1 that specify the transition probabilities at every node
so that supply and demand match among the agents.
To ensure generality, we also incorporate an external stochastic order flow, Ln−1​(Sn−1,Yn−1)L\_{n-1}(S\_{n-1},Y\_{n-1}),
which represents the stock supply per capita at each time t=tn−1t=t\_{n-1}, for 1≤n≤N1\leq n\leq N.
The external order flow serves to model the net contribution from other populations or from a major financial institution,
such as a central bank.

###### Assumption 2.3.

For every 1≤n≤N1\leq n\leq N, Ln−1:𝒮n−1×𝒴n−1→ℝL\_{n-1}:{\cal S}\_{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R}
is a bounded measurable function.

###### Definition 2.1.

We say that the system is in the mean-field equilibrium if

|  |  |  |
| --- | --- | --- |
|  | limNp→∞1Np​∑i=1Npϕn−1i,∗​(Sn−1,Yn−1,Zn−1i,γi)=Ln−1​(Sn−1,Yn−1),\lim\_{N\_{p}\rightarrow\infty}\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\phi^{i,\*}\_{n-1}(S\_{n-1},Y\_{n-1},Z\_{n-1}^{i},\gamma\_{i})=L\_{n-1}(S\_{n-1},Y\_{n-1}), |  |

ℙ\mathbb{P}-a.s. for every 1≤n≤N1\leq n\leq N with ϕn−1i,∗\phi^{i,\*}\_{n-1} defined by ([2.3](https://arxiv.org/html/2510.11261v1#S2.E3 "In Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t1-eq1}).

Since (Zi,γi),i∈ℕ(Z^{i},\gamma\_{i}),i\in\mathbb{N} are independent and identically distributed and also independent of the process (S,Y)(S,Y), the above condition for the mean-field equilibrium is equivalently expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼1​[ϕn−11,∗​(s,y,Zn−11,γ1)]=Ln−1​(s,y)\mathbb{E}^{1}\bigl[\phi^{1,\*}\_{n-1}(s,y,Z\_{n-1}^{1},\gamma\_{1})\bigr]=L\_{n-1}(s,y) |  | ( 2.6) |

for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
Under the mean-field equilibrium, the excess demand/supply per capita converges to zero as the population size tends to infinity. Our first main result for this paper is then established as follows.
One can observe conditional McKean-Vlasov nature
as expected from the result in Fujii & Sekine [[20](https://arxiv.org/html/2510.11261v1#bib.bib20)].

###### Theorem 2.2.

Let Assumptions [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [2.3](https://arxiv.org/html/2510.11261v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") be in force.
Then there exists a unique mean-field equilibrium and the associated transition probabilities of the stock are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn−1​(s,y):=ℙ0​(Sn=u~​Sn−1|(Sn−1,Yn−1)=(s,y))=(−d)/{u​exp⁡(1𝔼1​[1/γ1]​[𝔼1​(log⁡(fn−1​(s,y,Zn−11,γ1))γ1)−(u−d)​βNβn​Ln−1​(s,y)])−d},\begin{split}&p\_{n-1}(s,y):=\mathbb{P}^{0}\Bigl(S\_{n}=\widetilde{u}S\_{n-1}|(S\_{n-1},Y\_{n-1})=(s,y)\Bigr)\\ &=(-d)\Big/\Bigl\{u\exp\Bigl(\frac{1}{\mathbb{E}^{1}[1/\gamma\_{1}]}\Bigl[\mathbb{E}^{1}\Bigl(\frac{\log(f\_{n-1}(s,y,Z\_{n-1}^{1},\gamma\_{1}))}{\gamma\_{1}}\Bigr)-(u-d)\frac{\beta^{N}}{\beta^{n}}L\_{n-1}(s,y)\Bigr]\Bigr)-d\Bigr\},\end{split} |  | ( 2.7) |

for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
Moreover, under the above transition probabilities, there exists some positive constant Cn−1C\_{n-1} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​|1Np​∑i=1Npϕn−1i,∗​(Sn−1,Yn−1,Zn−1i,γi)−Ln−1​(Sn−1,Yn−1)|2≤Cn−1Np\mathbb{E}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\phi^{i,\*}\_{n-1}(S\_{n-1},Y\_{n-1},Z\_{n-1}^{i},\gamma\_{i})-L\_{n-1}(S\_{n-1},Y\_{n-1})\Bigr|^{2}\leq\frac{C\_{n-1}}{N\_{p}} |  | ( 2.8) |

for every 1≤n≤N1\leq n\leq N, which gives the convergence rate in the large population limit.

###### Proof.

The first claim ([2.7](https://arxiv.org/html/2510.11261v1#S2.E7 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq1}) is a direct consequence of ([2.3](https://arxiv.org/html/2510.11261v1#S2.E3 "In Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t1-eq1}). The form of (pn−1​(s,y))(p\_{n-1}(s,y)) is uniquely determined by
the condition ([2.6](https://arxiv.org/html/2510.11261v1#S2.E6 "In 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{def-mfe-t}). We only need to verify that it satisfies the condition (vii) in Assumption [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
At t=N−1t=N-1, fN−1f\_{N-1} is an a.s. strictly positive and bounded function on 𝒮N−1×𝒴N−1×𝒵N−1×Γ{\cal S}\_{N-1}\times{\cal Y}\_{N-1}\times{\cal Z}\_{N-1}\times\Gamma
by the corresponding assumption on FF. Since d<0<ud<0<u, it is easy to see 0<pN−1​(s,y),qN−1​(s,y)<10<p\_{N-1}(s,y),q\_{N-1}(s,y)<1 for every (s,y)∈𝒮N−1×𝒴N−1(s,y)\in{\cal S}\_{N-1}\times{\cal Y}\_{N-1},
and hence consistent with the condition. This then implies that ϕN−1i,∗\phi^{i,\*}\_{N-1} is an a.s. bounded function on 𝒮N−1×𝒴N−1×𝒵N−1×Γ{\cal S}\_{N-1}\times{\cal Y}\_{N-1}\times{\cal Z}\_{N-1}\times\Gamma, which results in a.s. strictly positive and bounded VN−1V\_{N-1} given by ([2.4](https://arxiv.org/html/2510.11261v1#S2.E4 "In Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t1-eq2})
on 𝒮N−1×𝒴N−1×𝒵N−1×Γ{\cal S}\_{N-1}\times{\cal Y}\_{N-1}\times{\cal Z}\_{N-1}\times\Gamma. This in turn ensures that fN−2f\_{N-2} satisfies the desired properties,
and so do (pN−2​(s,y),qN−2​(s,y))(p\_{N-2}(s,y),q\_{N-2}(s,y)), (s,y)∈𝒮N−2×𝒴N−2(s,y)\in{\cal S}\_{N-2}\times{\cal Y}\_{N-2}. By simple induction, we get the desired consistency
for every time step.

For the second claim, it suffices to show that there is some constant Cn−1C\_{n-1} such that an inequality

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯​|1Np​∑i=1Npϕn−1i,∗​(s,y,Zn−1i,γi)−Ln−1​(s,y)|2≤Cn−1Np\overline{\mathbb{E}}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\phi^{i,\*}\_{n-1}(s,y,Z\_{n-1}^{i},\gamma\_{i})-L\_{n-1}(s,y)\Bigr|^{2}\leq\frac{C\_{n-1}}{N\_{p}} |  |

holds for every (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
With the equilibrium transition probabilities given by ([2.7](https://arxiv.org/html/2510.11261v1#S2.E7 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq1}), one can show that the optimal position for agent-ii is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1i,∗​(s,y,Zn−1i,γi)=1(u−d)​βnβN​{log⁡fn−1​(s,y,Zn−1i,γi)γi−1/γi𝔼1​[1/γ1]​𝔼1​[log⁡fn−1​(s,y,Zn−11,γ1)γ1]}+1/γi𝔼1​[1/γ1]​Ln−1​(s,y).\begin{split}\phi\_{n-1}^{i,\*}(s,y,Z\_{n-1}^{i},\gamma\_{i})&=\frac{1}{(u-d)}\frac{\beta^{n}}{\beta^{N}}\Bigl\{\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{i},\gamma\_{i})}{\gamma\_{i}}-\frac{1/\gamma\_{i}}{\mathbb{E}^{1}[1/\gamma\_{1}]}\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\gamma\_{1})}{\gamma\_{1}}\Bigr]\Bigr\}\\ &+\frac{1/\gamma\_{i}}{\mathbb{E}^{1}[1/\gamma\_{1}]}L\_{n-1}(s,y).\end{split} |  | ( 2.9) |

Thanks to the i.i.d. property of (Zn−1i,γi)(Z\_{n-1}^{i},\gamma\_{i}) and the boundedness of fn−1,Ln−1f\_{n-1},L\_{n-1} and 1/γi1/\gamma\_{i},
it is easy to see that there exists some constant Cn−1C\_{n-1} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼¯​|1Np​∑i=1Npϕn−1i,∗​(s,y,Zn−1i,γi)−Ln−1​(s,y)|2≤Cn−1Np​𝔼1​[|1γ1−𝔼1​(1γ1)|2+|log⁡fn−1​(s,y,Zn−11,γ1)γ1−𝔼1​[log⁡fn−1​(s,y,Zn−11,γ1)γ1]|2]\begin{split}&\overline{\mathbb{E}}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\phi^{i,\*}\_{n-1}(s,y,Z\_{n-1}^{i},\gamma\_{i})-L\_{n-1}(s,y)\Bigr|^{2}\\ &\leq\frac{C\_{n-1}}{N\_{p}}\mathbb{E}^{1}\left[\Bigl|\frac{1}{\gamma\_{1}}-\mathbb{E}^{1}\Bigl(\frac{1}{\gamma\_{1}}\Bigr)\Bigr|^{2}+\Bigl|\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\gamma\_{1})}{\gamma\_{1}}-\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}(s,y,Z\_{n-1}^{1},\gamma\_{1})}{\gamma\_{1}}\Bigr]\Bigr|^{2}\right]\end{split} |  |

which gives the desired result. Note that the variances in the left-hand side
are finite uniformly in (s,y)∈𝒮n−1×𝒴n−1(s,y)\in{\cal S}\_{n-1}\times{\cal Y}\_{n-1} thanks to the boundedness of functions fn−1f\_{n-1} and 1/γi1/\gamma\_{i}.
∎

### 2.4 Some implications

Let us consider some implications of the above findings. For simplicity, assume first that there is no external order flow L≡0L\equiv 0.
Recalling that the risk-neutral probability of the up-move at each node is pℚ=(−d)u−dp^{\mathbb{Q}}=\frac{(-d)}{u-d},
one can see from ([2.7](https://arxiv.org/html/2510.11261v1#S2.E7 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq1}) that pn−1​(s,y)>pℚp\_{n-1}(s,y)>p^{\mathbb{Q}} (i.e. positive excess return at this node)
occurs if and only if 𝔼1​[log⁡(fn−1​(s,y,Zn−11,γ1))/γ1]<0\mathbb{E}^{1}[\log(f\_{n-1}(s,y,Z\_{n-1}^{1},\gamma\_{1}))/\gamma\_{1}]<0.
This happens if VnV\_{n}, which is determined by the function FF,
is a decreasing function of ss. In Section [4](https://arxiv.org/html/2510.11261v1#S4 "4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we shall see numerical examples confirming this point.
The corresponding situation occurs when the agents’ liability ((−1)×(-1)\times endowment) decreases when the stock price goes up.
In this case, adding to the long position in the stock increases the risk, and hence the agents require higher risk premium.
Therefore, for a liability whose size varies countercyclically, the more levered financial and investment firms are, the higher the risk premium is demanded.Suppose, on the other hand, that the agents’ liability increases when the stock price goes up.
For example, imagine that agents have net short position in call options on the stock.
Then, the agents have a strong incentive to increase the long position in the same stock, and hence may accept even a negative risk premium.

As one can see from ([2.7](https://arxiv.org/html/2510.11261v1#S2.E7 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq1}), there is no need to add idiosyncratic shocks to control the size of risk premium,
which is mainly determined by the sensitivity of the liability to the stock price.
However, the absence of idiosyncratic shocks gives rise to a very unrealistic market
where there is no trade among the agents. From the expression of the optimal position in ([2.9](https://arxiv.org/html/2510.11261v1#S2.E9 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq3}),
we can observe that the trading volume per capita
𝔼​[|ϕn1,∗|2]12\mathbb{E}[|\phi^{1,\*}\_{n}|^{2}]^{\frac{1}{2}} in the market is dictated by the variation of the idiosyncratic factors.
Note that, by the definition of the mean-field equilibrium, 𝔼​[ϕni,∗]=0,∀i∈ℕ\mathbb{E}[\phi^{i,\*}\_{n}]=0,\forall i\in\mathbb{N} when Ln=0L\_{n}=0.
Therefore, 𝔼​[|ϕn1,∗|2]12\mathbb{E}[|\phi^{1,\*}\_{n}|^{2}]^{\frac{1}{2}} gives the standard deviation of the stock position among the agents
at time t=tnt=t\_{n}.

In addition to the condition L≡0L\equiv 0, let us now suppose that the function FF is independent of the stock price.
We then have fN−1=1f\_{N-1}=1 a.s. since VNV\_{N} is SNS\_{N}-independent and thus ϕN−1i,∗=0\phi^{i,\*}\_{N-1}=0 a.s. by ([2.9](https://arxiv.org/html/2510.11261v1#S2.E9 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq3}).
This in turn makes VN−1V\_{N-1} independent from SN−1S\_{N-1}.
In this way, a simple induction shows that fn−1=1f\_{n-1}=1 a.s. for every 1≤n≤N1\leq n\leq N
and the equilibrium price distribution becomes equal to the one in the risk-neutral measure.
In this case, there is no trade in the market although each agent has different risk aversion,
which corresponds to the classical (but a bit uninteresting) example of the representative agent with CARA utility.

Finally, let us turn on the external order flow. It is clearly seen from ([2.7](https://arxiv.org/html/2510.11261v1#S2.E7 "In Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-t2-eq1}), the positive inflow L>0L>0
to the stock market
increases the equilibrium risk premium. This may sound slightly counter intuitive since we think a big sell-off in the stock should lead to
a sharp decline in the stock price. In order to understand that there is no contradiction,
it is important to recall that what we have found above is the transition probabilities so that there exists equilibrium.
If there is positive supply of the stock, the agents must accept larger long position (and hence larger risk) in the stock to maintain
the balance of demand and supply. Thus the agents require higher risk premium to compensate this additional risk.
If the risk premium is not high enough, there would be no equilibrium and thus the stock market might crash.

## 3 Recursive utility optimization with path-dependent cash flows

In the previous section, we obtained mean-field equilibrium by choosing appropriate transition probabilities in the form of pn​(s,y)p\_{n}(s,y).
Suppose now that the stochastic liability (or (−1)(-1) endowment) FF is dependent
not only on the terminal stock price SNS\_{N} but also on the stock-price history (Sn)n=0N(S\_{n})\_{n=0}^{N},
which is just as plausible as the previous case. In this case, a quick inspection of the proofs for Theorems [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") shows that the transition probabilities of the simple form pn​(s,y)p\_{n}(s,y) can not clear the market anymore.
It strongly suggests that we need path-dependence also in the transition probabilities.
We also want to examine if we can include cash spending (i.e. nominal consumption) and to know its impact on the excess return.
In this section, we shall thus adopt recursive utility that incorporates
standard time-separable utility over nominal consumptions as its special case. We include a path-dependent terminal liability as well as
path-dependent incremental endowments in the model.

### 3.1 The setup and notation

In this section, for each i∈ℕi\in\mathbb{N},
we assume that the probability space (Ωi,ℱi,(ℱtni)n=0N,ℙi)(\Omega^{i},{\cal F}^{i},({\cal F}^{i}\_{t\_{n}})\_{n=0}^{N},\mathbb{P}^{i}) is
endowed with (ξi,γi,ζi,ψi,δi)(\xi\_{i},\gamma\_{i},\zeta\_{i},\psi\_{i},\delta\_{i}) as ℱ0i{\cal F}^{i}\_{0}-measurable random variables
in addition to (ℱtni)n=0N({\cal F}\_{t\_{n}}^{i})\_{n=0}^{N}-adapted stochastic process (Zni=Zi​(tn))n=0N(Z\_{n}^{i}=Z^{i}(t\_{n}))\_{n=0}^{N}.
Here, ζi\zeta\_{i} is the coefficient of absolute risk aversion for cash spending and the parameter ψi\psi\_{i} is used
to control the importance of the continuation utility relative to the current spending.
δi\delta\_{i} denotes the coefficient of time preference. We introduce an ℱ0i{\cal F}\_{0}^{i}-measurable 4-tuple
ϱi:=(γi,ζi,ψi,δi)\varrho\_{i}:=(\gamma\_{i},\zeta\_{i},\psi\_{i},\delta\_{i}) for simpler notation.
Let us also introduce the symbol 𝐒n:=(S0,S1,⋯,Sn){\bf{S}}^{n}:=(S\_{0},S\_{1},\cdots,S\_{n}) to denote a stock-price trajectory
and 𝐬n=(s0,⋯,sn)∈𝒮n{\bf{s}}^{n}=(s\_{0},\cdots,s\_{n})\in{\cal S}^{n} as its specific realization.
For 𝐬∈𝒮n−1{\bf{s}}\in{\cal S}^{n-1}, we also use the symbols (𝐬​u~)n:=(𝐬n−1,sn−1​u~)∈𝒮n({\bf{s}}\widetilde{u})^{n}:=({\bf{s}}^{n-1},s\_{n-1}\widetilde{u})\in{\cal S}^{n}
and (𝐬​d~)n:=(𝐬n−1,sn−1​d~)∈𝒮n({\bf{s}}\widetilde{d})^{n}:=({\bf{s}}^{n-1},s\_{n-1}\widetilde{d})\in{\cal S}^{n}.
As in the last section, we shall use the expressions such as
𝔼0,i[⋅|𝐬,y,zi,ϱi]\mathbb{E}^{0,i}[~\cdot~|{\bf{s}},y,z^{i},\varrho\_{i}] for (𝐬,y,zi)∈𝒮n−1×𝒴n−1×𝒵n−1({\bf{s}},y,z^{i})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}
to denote the conditional expectation 𝔼0,i[⋅|𝐒n−1=𝐬,Yn−1=y,Zn−1i=zi,ϱi=ϱi]\mathbb{E}^{0,i}[~\cdot~|{\bf{S}}^{n-1}={\bf{s}},Y\_{n-1}=y,Z\_{n-1}^{i}=z\_{i},\varrho\_{i}=\varrho\_{i}],
where, with the slight abuse of notation, the same symbol is used for a realization of ℱ0i{\cal F}^{i}\_{0}-measurable random variable ϱi\varrho\_{i}.
Except these points, we will use the same setup and notation given in Section [2.1](https://arxiv.org/html/2510.11261v1#S2.SS1 "2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
Now, let us update Assumption [2.1](https://arxiv.org/html/2510.11261v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") for this section.

###### Assumption 3.1.

(i): u~\widetilde{u} and d~\widetilde{d} are real constants satisfying

|  |  |  |
| --- | --- | --- |
|  | 0<d~<exp⁡(r​Δ)<u~<∞.0<\widetilde{d}<\exp(r\Delta)<\widetilde{u}<\infty. |  |

(ii): Every (ξi,γi,ζi,ψi,δi,(Zni)n=0N),i=1,2,…(\xi^{i},\gamma\_{i},\zeta\_{i},\psi\_{i},\delta\_{i},(Z\_{n}^{i})\_{n=0}^{N}),i=1,2,\ldots has the same distribution.
  
(iii): There exist real constants ξ¯,ξ¯\underline{\xi},\overline{\xi}, γ¯,γ¯\underline{\gamma},\overline{\gamma}, ζ¯,ζ¯\underline{\zeta},\overline{\zeta}, ψ¯,ψ¯\underline{\psi},\overline{\psi}
and δ¯,δ¯\underline{\delta},\overline{\delta} so that for every i∈ℕi\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | ξi∈[ξ¯,ξ¯]⊂ℝ,ϱi:=(γi,ζi,ψi,δi)∈Γ:=[γ¯,γ¯]×[ζ¯,ζ¯]×[ψ¯,ψ¯]×[δ¯,δ¯]⊂(0,∞)4.\begin{split}&\xi\_{i}\in[\underline{\xi},\overline{\xi}]\subset\mathbb{R},\\ &\varrho\_{i}:=(\gamma\_{i},\zeta\_{i},\psi\_{i},\delta\_{i})\in\Gamma:=[\underline{\gamma},\overline{\gamma}]\times[\underline{\zeta},\overline{\zeta}]\times[\underline{\psi},\overline{\psi}]\times[\underline{\delta},\overline{\delta}]\subset(0,\infty)^{4}.\end{split} |  |

(iv): For every 0≤n≤N0\leq n\leq N, 𝒵n{\cal Z}\_{n} is a bounded subset
of ℝdZ\mathbb{R}^{d\_{Z}}.
  
(v): For each ii, (Zni)n=0N(Z\_{n}^{i})\_{n=0}^{N} is a Markov process i.e. 𝔼i​[f​(Zni)|ℱtmi]=𝔼i​[f​(Zni)|Zmi]\mathbb{E}^{i}[f(Z\_{n}^{i})|{\cal F}\_{t\_{m}}^{i}]=\mathbb{E}^{i}[f(Z\_{n}^{i})|Z\_{m}^{i}]
for every bounded measurable function ff on 𝒵n{\cal Z}\_{n} and m≤nm\leq n.
  
(vi): (Yn)n=0N(Y\_{n})\_{n=0}^{N} is a Markov process i.e. 𝔼0​[f​(Yn)|ℱtm0]=𝔼0​[f​(Yn)|Ym]\mathbb{E}^{0}[f(Y\_{n})|{\cal F}\_{t\_{m}}^{0}]=\mathbb{E}^{0}[f(Y\_{n})|Y\_{m}]
for every bounded measurable function ff on 𝒴n{\cal Y}\_{n} and m≤nm\leq n.
  
(vii): The transition probabilities of (Sn)n=0N(S\_{n})\_{n=0}^{N} satisfy, for every 0≤n≤N−10\leq n\leq N-1,

|  |  |  |
| --- | --- | --- |
|  | ℙ0​(Sn+1=u~​Sn|ℱtn0)=ℙ0​(Sn+1=u~​Sn|𝐒n,Yn)=pn​(𝐒n,Yn),ℙ0​(Sn+1=d~​Sn|ℱtn0)=ℙ0​(Sn+1=d~​Sn|𝐒n,Yn)=qn​(𝐒n,Yn):=1−pn​(𝐒n,Yn),\begin{split}\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|{\cal F}\_{t\_{n}}^{0})&=\mathbb{P}^{0}(S\_{n+1}=\widetilde{u}S\_{n}|{\bf{S}}^{n},Y\_{n})=p\_{n}({\bf{S}}^{n},Y\_{n}),\\ \mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|{\cal F}\_{t\_{n}}^{0})&=\mathbb{P}^{0}(S\_{n+1}=\widetilde{d}S\_{n}|{\bf{S}}^{n},Y\_{n})=q\_{n}({\bf{S}}^{n},Y\_{n}):=1-p\_{n}({\bf{S}}^{n},Y\_{n}),\end{split} |  |

where pn,qn:𝒮n×𝒴n→ℝ,0≤n≤N−1p\_{n},q\_{n}:{\cal S}^{n}\times{\cal Y}\_{n}\rightarrow\mathbb{R},~0\leq n\leq N-1 are bounded measurable functions
satisfying

|  |  |  |
| --- | --- | --- |
|  | 0<pn​(𝐬,y),qn​(𝐬,y)<10<p\_{n}({\bf{s}},y),q\_{n}({\bf{s}},y)<1 |  |

for every (𝐬,y)∈𝒮n×𝒴n({\bf{s}},y)\in{\cal S}^{n}\times{\cal Y}\_{n}.

Under the above assumptions, we have, instead of ([2.1](https://arxiv.org/html/2510.11261v1#S2.E1 "In 2.1 The setup and notation ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Y-conditional-1}), the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼0​[f​(Sn+1)​g​(Yn+1)|ℱtn0]=𝔼0​[f​(Sn+1)|𝐒n,Yn]​𝔼0​[g​(Yn+1)|Yn],0≤n≤N−1,\mathbb{E}^{0}\bigl[f(S\_{n+1})g(Y\_{n+1})|{\cal F}\_{t\_{n}}^{0}]=\mathbb{E}^{0}[f(S\_{n+1})|{\bf{S}}^{n},Y\_{n}]\mathbb{E}^{0}[g(Y\_{n+1})|Y\_{n}],\quad 0\leq n\leq N-1, |  | ( 3.1) |

for any bounded measurable functions ff and gg.

###### Remark 3.1.

As in the last section, the condition 0<pn​(𝐬,y),qn​(𝐬,y)<1,∀(𝐬,y)∈𝒮n×𝒴n,0≤n≤N−10<p\_{n}({\bf{s}},y),q\_{n}({\bf{s}},y)<1,\forall({\bf{s}},y)\in{\cal S}^{n}\times{\cal Y}\_{n},0\leq n\leq N-1
guarantees the equivalence of ℙ0∘Sn−1\mathbb{P}^{0}\circ S\_{n}^{-1} and ℚ∘Sn−1\mathbb{Q}\circ S\_{n}^{-1}. Hence the
system is arbitrage free.

### 3.2 The individual optimization problem

In this section, as mentioned before, we assume that each agent-ii not only engages in self-financing trading
with the money-market account and the risky stock, but she is also allowed to spend some cash at the beginning of each period. Moreover,
she receives a stochastic endowment at each time tn,1≤n≤Nt\_{n},1\leq n\leq N.
Thus the wealth of the agent-ii (Xni:=Xi​(tn))n=0N(X^{i}\_{n}:=X^{i}(t\_{n}))\_{n=0}^{N} follows the dynamics

|  |  |  |
| --- | --- | --- |
|  | Xn+1i=exp⁡(r​Δ)​(Xni−cni​Δ−ϕni)+ϕni​R~n+1+gn+1​(𝐒n+1,Yn+1,Zn+1i)=β​(Xni−cni​Δ)+ϕni​Rn+1+gn+1​(𝐒n+1,Yn+1,Zn+1i),\begin{split}X\_{n+1}^{i}&=\exp(r\Delta)(X\_{n}^{i}-c\_{n}^{i}\Delta-\phi\_{n}^{i})+\phi\_{n}^{i}\widetilde{R}\_{n+1}+g\_{n+1}({\bf{S}}^{n+1},Y\_{n+1},Z\_{n+1}^{i})\\ &=\beta(X\_{n}^{i}-c\_{n}^{i}\Delta)+\phi\_{n}^{i}R\_{n+1}+g\_{n+1}({\bf{S}}^{n+1},Y\_{n+1},Z\_{n+1}^{i}),\end{split} |  |

where X0i=ξiX\_{0}^{i}=\xi\_{i}. Here, cni,0≤n≤N−1c\_{n}^{i},0\leq n\leq N-1 denotes the cash spending at tnt\_{n}, which is scaled to the period’s rate.
gn​(𝐒n,Yn,Zni),1≤n≤Ng\_{n}({\bf{S}}^{n},Y\_{n},Z\_{n}^{i}),1\leq n\leq N is the stochastic endowment (i.e. income originating from the agent’s other business lines)
paid at tnt\_{n}, which is dependent on the stock-price trajectory 𝐒n{\bf{S}}^{n}
in addition to the common and the idiosyncratic shocks (Yn,Zni)(Y\_{n},Z\_{n}^{i}). Recall that Rn:=R~n−exp⁡(r​Δ)R\_{n}:=\widetilde{R}\_{n}-\exp(r\Delta).
As discussed in Remark [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmremark2 "Remark 2.2. ‣ 2.2 The individual optimization problem ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), including such stochastic endowments appears
to be almost unavoidable for a realistic model of financial firms.

We suppose that the (ℱtn0,i)n=0N({\cal F}^{0,i}\_{t\_{n}})\_{n=0}^{N}-adapted process of utilities (Uni)n=0N(U\_{n}^{i})\_{n=0}^{N} are defined recursively by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uni:=−1ζi​log⁡{e−ζi​cni​Δ+δi​exp⁡(ψiγi​log⁡(𝔼0,i​[e−γi​Un+1i|ℱtn0,i]))},↔e−ζi​Uni=e−ζi​cni​Δ+δi​exp⁡(ψiγi​log⁡(𝔼0,i​[e−γi​Un+1i|ℱtn0,i])),\begin{split}&U\_{n}^{i}:=-\frac{1}{\zeta\_{i}}\log\Bigl\{e^{-\zeta\_{i}c\_{n}^{i}}\Delta+\delta\_{i}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\bigl(\mathbb{E}^{0,i}[e^{-\gamma\_{i}U\_{n+1}^{i}}|{\cal F}\_{t\_{n}}^{0,i}]\bigr)\Bigr)\Bigr\},\\ &\leftrightarrow e^{-\zeta\_{i}U\_{n}^{i}}=e^{-\zeta\_{i}c\_{n}^{i}}\Delta+\delta\_{i}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\bigl(\mathbb{E}^{0,i}[e^{-\gamma\_{i}U\_{n+1}^{i}}|{\cal F}\_{t\_{n}}^{0,i}]\bigr)\Bigr),\end{split} |  | ( 3.2) |

with the terminal condition

|  |  |  |
| --- | --- | --- |
|  | UNi:=XNi−F​(𝐒N,YN,ZNi).U\_{N}^{i}:=X\_{N}^{i}-F({\bf{S}}^{N},Y\_{N},Z\_{N}^{i}). |  |

Each agent-ii is supposed to solve the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(ϕni,cni)n=0N−1∈𝔸iU0i,\sup\_{(\phi\_{n}^{i},c\_{n}^{i})\_{n=0}^{N-1}\in\mathbb{A}^{i}}U^{i}\_{0}, |  | ( 3.3) |

over the admissible space defined by

|  |  |  |
| --- | --- | --- |
|  | 𝔸i:={(ϕni,cni)n=0N−1;(ϕni,cni)​ is an ℱn0,i-measurable ℝ2-valued random variable}.\mathbb{A}^{i}:=\bigl\{(\phi\_{n}^{i},c\_{n}^{i})\_{n=0}^{N-1};(\phi\_{n}^{i},c\_{n}^{i})\text{ is an ${\cal F}\_{n}^{0,i}$-measurable $\mathbb{R}^{2}$-valued random variable}\bigr\}. |  |

For simplicity, we do not restrict (cni)(c\_{n}^{i}) to non-negative values. One may interpret negative spending
as positive income from costly labor for the corresponding period.

###### Assumption 3.2.

(i): The function F:𝒮N×𝒴N×𝒵N→ℝF:{\cal S}^{N}\times{\cal Y}\_{N}\times{\cal Z}\_{N}\rightarrow\mathbb{R} is measurable and bounded.
  
(ii): For every 1≤n≤N1\leq n\leq N, the function gn:𝒮n×𝒴n×𝒵n→ℝg\_{n}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\rightarrow\mathbb{R}
is measurable and bounded.

Before going into the details, let us consider the special case: ζi=γi=ψi\zeta\_{i}=\gamma\_{i}=\psi\_{i}. In this case, we have

|  |  |  |
| --- | --- | --- |
|  | e−ζi​Uni=e−ζi​cni​Δ+δi​𝔼0,i​[e−ζi​Un+1i|ℱtn0,i]=e−ζi​cni​Δ+𝔼0,i​[δi​e−ζi​cn+1i​Δ|ℱtn0,i]+δi2​𝔼0,i​[e−ζi​Un+2i|ℱtn0,i]=⋯=e−ζi​cni​Δ+𝔼0,i​[∑k=n+1N−1δik−n​e−ζi​cki​Δ+δiN−n​e−ζi​UNi|ℱtn0,i],\begin{split}e^{-\zeta\_{i}U\_{n}^{i}}&=e^{-\zeta\_{i}c\_{n}^{i}}\Delta+\delta\_{i}\mathbb{E}^{0,i}[e^{-\zeta\_{i}U\_{n+1}^{i}}|{\cal F}\_{t\_{n}}^{0,i}]\\ &=e^{-\zeta\_{i}c\_{n}^{i}}\Delta+\mathbb{E}^{0,i}\bigl[\delta\_{i}e^{-\zeta\_{i}c\_{n+1}^{i}}\Delta|{\cal F}\_{t\_{n}}^{0,i}\bigr]+\delta\_{i}^{2}\mathbb{E}^{0,i}[e^{-\zeta\_{i}U\_{n+2}^{i}}|{\cal F}\_{t\_{n}}^{0,i}]\\ &=\cdots=e^{-\zeta\_{i}c\_{n}^{i}}\Delta+\mathbb{E}^{0,i}\Bigl[\sum\_{k=n+1}^{N-1}\delta\_{i}^{k-n}e^{-\zeta\_{i}c\_{k}^{i}}\Delta+\delta\_{i}^{N-n}e^{-\zeta\_{i}U\_{N}^{i}}|{\cal F}\_{t\_{n}}^{0,i}\Bigr],\end{split} |  |

which thus corresponds to the standard time-separable utility over nominal consumptions. One can see that the parameter ψi\psi\_{i}
determines the relative importance of the continuation utility.
We now derive the optimal strategy for each agent with respect to the above-defined recursive utility.

###### Theorem 3.1.

Let Assumptions [3.1](https://arxiv.org/html/2510.11261v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [3.2](https://arxiv.org/html/2510.11261v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") be in force.
Then the problem ([3.3](https://arxiv.org/html/2510.11261v1#S3.E3 "In 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{problem-R1}) has an unique optimal solution (ϕn−1i,∗,cn−1i,∗)n=1N(\phi\_{n-1}^{i,\*},c\_{n-1}^{i,\*})\_{n=1}^{N},
where (ϕn−1i,∗)n=1N(\phi\_{n-1}^{i,\*})\_{n=1}^{N} and (cn−1i,∗)n=1N(c\_{n-1}^{i,\*})\_{n=1}^{N} are a.s. bounded processes defined by
measurable functions ϕn−1i,∗:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝ\phi\_{n-1}^{i,\*}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}
and cn−1i,∗:ℝ×𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝc\_{n-1}^{i,\*}:\mathbb{R}\times{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R}
as ϕn−1i,∗:=ϕn−1i,∗​(𝐒n−1,Yn−1,Zn−1i,ϱi)\phi\_{n-1}^{i,\*}:=\phi^{i,\*}\_{n-1}({\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i})
and cn−1i,∗:=cn−1i,∗​(Xn−1i,𝐒n−1,Yn−1,Zn−1i,ϱi)c\_{n-1}^{i,\*}:=c^{i,\*}\_{n-1}(X\_{n-1}^{i},{\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i}) respectively,
where, for each (xi,𝐬,y,zi,ϱi)∈ℝ×𝒮n−1×𝒴n−1×𝒵n−1×Γ(x^{i},{\bf{s}},y,z^{i},\varrho\_{i})\in\mathbb{R}\times{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1i,∗​(𝐬,y,zi,ϱi):=1γi​ηni​(u−d)​{log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)+log⁡(fn−1​(𝐬,y,zi,ϱi))},\begin{split}\phi\_{n-1}^{i,\*}({\bf{s}},y,z^{i},\varrho\_{i}):=\frac{1}{\gamma\_{i}\eta\_{n}^{i}(u-d)}\Bigl\{\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)+\log\bigl(f\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\bigr)\Bigr\},\end{split} |  | ( 3.4) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | cn−1i,∗​(xi,𝐬,y,zi,ϱi):=ψi​ηni​βζi+Δ​ψi​ηni​β​xi−1ζi+Δ​ψi​ηni​β​log⁡{δi​ψi​ηni​βζi​exp⁡(ψiγi​log⁡V~n−1​(𝐬,y,zi,ϱi))}.\begin{split}c\_{n-1}^{i,\*}(x^{i},{\bf{s}},y,z^{i},\varrho\_{i}):=\frac{\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}x^{i}-\frac{1}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}\log\Bigl\{\frac{\delta\_{i}\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\Bigr)\Bigr\}.\end{split} |  | ( 3.5) |

fn−1:𝒮n−1×𝒴n−1×𝒵n−1×Γ→ℝf\_{n-1}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma\rightarrow\mathbb{R} is an a.s. strictly positive and bounded
measurable function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn−1​(𝐬,y,zi,ϱi):=𝔼0,i​[exp⁡(γi​[Vn​((𝐬​u~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​u~)n,Yn,Zni)])|y,zi,ϱi]𝔼0,i​[exp⁡(γi​[Vn​((𝐬​d~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​d~)n,Yn,Zni)])|y,zi,ϱi],f\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i}):=\frac{\mathbb{E}^{0,i}\bigl[\exp\bigl(\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i})]\bigr)|y,z^{i},\varrho\_{i}\bigr]}{\mathbb{E}^{0,i}\bigl[\exp\bigl(\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i})]\bigr)|y,z^{i},\varrho\_{i}\bigr]}, |  | ( 3.6) |

and Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R} is an a.s. bounded measurable function
defined recursively by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn−1​(𝐬,y,zi,ϱi):=ηn−1iηni​γi​β​log⁡V~n−1​(𝐬,y,zi,ϱi)+1ζi+Δ​ψi​ηni​β​log⁡(δi​ψi​ηni​βζi)−1ζi​log⁡(ηn−1i),\begin{split}&V\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i}):=\frac{\eta\_{n-1}^{i}}{\eta\_{n}^{i}\gamma\_{i}\beta}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})+\frac{1}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}\log\Bigl(\frac{\delta\_{i}\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}}\Bigr)-\frac{1}{\zeta\_{i}}\log(\eta\_{n-1}^{i}),\end{split} |  | ( 3.7) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~n−1​(𝐬,y,zi,ϱi):=pn−1​(𝐬,y)​e−γi​ηni​ϕn−1i,∗​u​𝔼0,i​[exp⁡(γi​[Vn​((𝐬​u~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​u~)n,Yn,Zni)])|y,zi,ϱi]+qn−1​(𝐬,y)​e−γi​ηni​ϕn−1i,∗​d​𝔼0,i​[exp⁡(γi​[Vn​((𝐬​d~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​d~)n,Yn,Zni)])|y,zi,ϱi],\begin{split}&\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\\ &\quad:=p\_{n-1}({\bf{s}},y)e^{-\gamma\_{i}\eta\_{n}^{i}\phi\_{n-1}^{i,\*}u}\mathbb{E}^{0,i}\bigl[\exp(\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i})])|y,z^{i},\varrho\_{i}]\\ &\quad+q\_{n-1}({\bf{s}},y)e^{-\gamma\_{i}\eta\_{n}^{i}\phi\_{n-1}^{i,\*}d}\mathbb{E}^{0,i}\bigl[\exp(\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i})])|y,z^{i},\varrho\_{i}],\end{split} |  | ( 3.8) |

starting from the terminal condition VN​(𝐒N,YN,ZNi,ϱi):=F​(𝐒N,YN,ZNi)V\_{N}({\bf{S}}^{N},Y\_{N},Z\_{N}^{i},\varrho\_{i}):=F({\bf{S}}^{N},Y\_{N},Z\_{N}^{i}). (ηni)n=0N(\eta\_{n}^{i})\_{n=0}^{N} are strictly positive and bounded
ℱ0i{\cal F}\_{0}^{i}-measurable random variables given by the recursive relation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηn−1i:=ψi​ηni​βζi+Δ​ψi​ηni​β,ηNi≡1.\eta\_{n-1}^{i}:=\frac{\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta},\quad\eta\_{N}^{i}\equiv 1. |  | ( 3.9) |

###### Proof.

We first hypothesize that the utility UniU\_{n}^{i} at t=tnt=t\_{n} is given by the following form:

|  |  |  |
| --- | --- | --- |
|  | Uni​(Xni,𝐒n,Yn,Zni,ϱi)=ηni​Xni−Vn​(𝐒n,Yn,Zni,ϱi),U\_{n}^{i}(X\_{n}^{i},{\bf{S}}^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})=\eta\_{n}^{i}X\_{n}^{i}-V\_{n}({\bf{S}}^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i}), |  |

where Vn:𝒮n×𝒴n×𝒵n×Γ→ℝV\_{n}:{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R}
is a measurable a.s. bounded function and ηni\eta\_{n}^{i} is ℱ0i{\cal F}\_{0}^{i}-measurable
strictly positive and bounded random variable. The hypothesis obviously holds at the terminal point
with VN​(𝐒N,YN,ZNi,ϱi)=F​(𝐒N,YN,ZNi)V\_{N}({\bf{S}}^{N},Y\_{N},Z\_{N}^{i},\varrho\_{i})=F({\bf{S}}^{N},Y\_{N},Z\_{N}^{i}) and ηNi≡1\eta\_{N}^{i}\equiv 1.
We shall show by induction that our hypothesis holds in every period.
Under the hypothesis, the problem for the agent-ii at tn−1t\_{n-1} becomes to find ℱn−10,i{\cal F}\_{n-1}^{0,i}-measurable strategy (ϕi,ci)(\phi^{i},c^{i})
that solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf(ϕi,ci){e−ζi​ci​Δ+δi​exp⁡(ψiγi​log⁡(𝔼0,i​[e−γi​Uni​(Xni,𝐒n,Yn,Zni,ϱi)|ℱn−10,i]))}.\inf\_{(\phi^{i},c^{i})}\Bigl\{e^{-\zeta\_{i}c^{i}}\Delta+\delta\_{i}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\Bigl(\mathbb{E}^{0,i}\bigl[e^{-\gamma\_{i}U\_{n}^{i}(X\_{n}^{i},{\bf{S}}^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})}|{\cal F}\_{n-1}^{0,i}\bigr]\Bigr)\Bigr)\Bigr\}. |  | ( 3.10) |

We consider the problem on the set {(Xn−1i,𝐒n−1,Yn−1,Zn−1i,ϱi)=(xi,𝐬,y,zi,ϱi)}\{(X\_{n-1}^{i},{\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i})=(x^{i},{\bf{s}},y,z^{i},\varrho\_{i})\}.
By Assumption [3.1](https://arxiv.org/html/2510.11261v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") (vii), ([3.1](https://arxiv.org/html/2510.11261v1#S3.E1 "In 3.1 The setup and notation ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Y-conditional-2}), and the above hypothesis, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼0,i​[e−γi​Uni​(Xni,𝐒n,Yn,Zni,ϱi)|xi,𝐬,yi,zi,ϱi]=𝔼0,i​[exp⁡(−γi​ηni​(β​(xi−ci​Δ)+ϕi​Rn+gn​(𝐒n,Yn,Zni))+γi​Vn​(𝐒n,Yn,Zni,ϱi))|𝐬,y,zi,ϱi]=e−γi​ηni​β​(xi−ci​Δ){pn−1(𝐬,y)e−γi​ηni​ϕi​u𝔼0,i[eγi​[Vn​((𝐬​u~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​u~)n,Yn,Zni)]|y,zi,ϱi]+qn−1(𝐬,y)e−γi​ηni​ϕi​d𝔼0,i[eγi​[Vn​((𝐬​d~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​d~)n,Yn,Zni)]|y,zi,ϱi]}.\begin{split}&\mathbb{E}^{0,i}\Bigl[e^{-\gamma\_{i}U\_{n}^{i}(X\_{n}^{i},{\bf{S}}^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})}|x^{i},{\bf{s}},y^{i},z^{i},\varrho\_{i}\Bigr]\\ &=\mathbb{E}^{0,i}\Bigl[\exp\Bigl(-\gamma\_{i}\eta\_{n}^{i}\bigl(\beta(x^{i}-c^{i}\Delta)+\phi^{i}R\_{n}+g\_{n}({\bf{S}}^{n},Y\_{n},Z\_{n}^{i})\bigr)+\gamma\_{i}V\_{n}({\bf{S}}^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})\Bigr)|{\bf{s}},y,z^{i},\varrho\_{i}\Bigr]\\ &=e^{-\gamma\_{i}\eta\_{n}^{i}\beta(x^{i}-c^{i}\Delta)}\Bigl\{p\_{n-1}({\bf{s}},y)e^{-\gamma\_{i}\eta\_{n}^{i}\phi^{i}u}\mathbb{E}^{0,i}\bigl[e^{\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i})]}|y,z^{i},\varrho\_{i}\bigr]\\ &\qquad\qquad+q\_{n-1}({\bf{s}},y)e^{-\gamma\_{i}\eta\_{n}^{i}\phi^{i}d}\mathbb{E}^{0,i}\bigl[e^{\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i})]}|y,z^{i},\varrho\_{i}\bigr]\Bigr\}.\end{split} |  |

Thus the problem ([3.10](https://arxiv.org/html/2510.11261v1#S3.E10 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{problem-R-intermediate}) can be restated as

|  |  |  |
| --- | --- | --- |
|  | inf(ϕi,ci){e−ζi​ciΔ+δie−ψi​ηni​β​(xi−ci​Δ)×exp(ψiγilog{pn−1(𝐬,y)e−γi​ηni​ϕi​u𝔼0,i[eγi​[Vn​((𝐬​u~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​u~)n,Yn,Zni)]|y,zi,ϱi]+qn−1(𝐬,y)e−γi​ηni​ϕi​d𝔼0,i[eγi​[Vn​((𝐬​d~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​d~)n,Yn,Zni)]|y,zi,ϱi]})}.\begin{split}&\inf\_{(\phi^{i},c^{i})}\Bigl\{e^{-\zeta\_{i}c^{i}}\Delta+\delta\_{i}e^{-\psi\_{i}\eta\_{n}^{i}\beta(x^{i}-c^{i}\Delta)}\\ &\times\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\Bigl\{p\_{n-1}({\bf{s}},y)e^{-\gamma\_{i}\eta\_{n}^{i}\phi^{i}u}\mathbb{E}^{0,i}\bigl[e^{\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i})]}|y,z^{i},\varrho\_{i}\bigr]\\ &\qquad\qquad+q\_{n-1}({\bf{s}},y)e^{-\gamma\_{i}\eta\_{n}^{i}\phi^{i}d}\mathbb{E}^{0,i}\bigl[e^{\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i})]}|y,z^{i},\varrho\_{i}\bigr]\Bigr\}\Bigr)\Bigr\}.\end{split} |  |

The optimization over (ϕi,ci)(\phi^{i},c^{i}) can now be solved separately. Since d<0<ud<0<u, the optimal ϕi,∗\phi^{i,\*}
is characterized uniquely by

|  |  |  |
| --- | --- | --- |
|  | 0=pn−1​(𝐬,y)​u​e−γi​ηni​ϕi​u​𝔼0,i​[eγi​[Vn​((𝐬​u~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​u~)n,Yn,Zni)]|y,zi,ϱi]+qn−1​(𝐬,y)​d​e−γi​ηni​ϕi​d​𝔼0,i​[eγi​[Vn​((𝐬​d~)n,Yn,Zni,ϱi)−ηni​gn​((𝐬​d~)n,Yn,Zni)]|y,zi,ϱi],\begin{split}0&=p\_{n-1}({\bf{s}},y)ue^{-\gamma\_{i}\eta\_{n}^{i}\phi^{i}u}\mathbb{E}^{0,i}\bigl[e^{\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{u})^{n},Y\_{n},Z\_{n}^{i})]}|y,z^{i},\varrho\_{i}\bigr]\\ &+q\_{n-1}({\bf{s}},y)de^{-\gamma\_{i}\eta\_{n}^{i}\phi^{i}d}\mathbb{E}^{0,i}\bigl[e^{\gamma\_{i}[V\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i},\varrho\_{i})-\eta\_{n}^{i}g\_{n}(({\bf{s}}\widetilde{d})^{n},Y\_{n},Z\_{n}^{i})]}|y,z^{i},\varrho\_{i}\bigr],\end{split} |  |

which gives the desired solution ([3.4](https://arxiv.org/html/2510.11261v1#S3.E4 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-phinm1}) for ϕn−1i,∗\phi^{i,\*}\_{n-1} with fn−1f\_{n-1} defined as in ([3.6](https://arxiv.org/html/2510.11261v1#S3.E6 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-fnm1}).
Thanks to the boundedness of gng\_{n} and our hypothesis on VnV\_{n}, fn−1f\_{n-1} is proved to be an a.s. strictly positive and bounded function
on 𝒮n−1×𝒴n−1×𝒵n−1×Γ{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma. Combined with the assumption on (pn−1,qn−1)(p\_{n-1},q\_{n-1})
and our hypothesis on ηni\eta\_{n}^{i}, ϕn−1i,∗\phi^{i,\*}\_{n-1} is also a.s. bounded on 𝒮n−1×𝒴n−1×𝒵n−1×Γ{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma.

With V~n−1\widetilde{V}\_{n-1} defined as in (LABEL:th-R1-Vtildenm1)(\ref{th-R1-Vtildenm1}), the optimization with respect to cic^{i} reduces to

|  |  |  |
| --- | --- | --- |
|  | infci{e−ζi​ci​Δ+δi​e−ψi​ηni​β​(xi−ci​Δ)​exp⁡(ψiγi​log⁡V~n−1​(𝐬,y,zi,ϱi))}.\inf\_{c^{i}}\Bigl\{e^{-\zeta\_{i}c^{i}}\Delta+\delta\_{i}e^{-\psi\_{i}\eta\_{n}^{i}\beta(x^{i}-c^{i}\Delta)}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\Bigr)\Bigr\}. |  |

Thus the optimal solution is characterized by the equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=−ζi​e−ζi​ci+δi​ψi​ηni​β​e−ψi​ηni​β​(xi−ci​Δ)​exp⁡(ψiγi​log⁡V~n−1​(𝐬,y,zi,ϱi)),0=-\zeta\_{i}e^{-\zeta\_{i}c^{i}}+\delta\_{i}\psi\_{i}\eta\_{n}^{i}\beta e^{-\psi\_{i}\eta\_{n}^{i}\beta(x^{i}-c^{i}\Delta)}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\Bigr), |  | ( 3.11) |

which gives the unique solution cn−1i,∗c\_{n-1}^{i,\*} in ([3.5](https://arxiv.org/html/2510.11261v1#S3.E5 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-cnm1}) as desired. Note that it is a.s. bounded if the wealth xix^{i}
at tn−1t\_{n-1} is bounded. Therefore, once our induction is complete, the spending process is shown to be a.s. bounded since ξi\xi\_{i} takes
values in a bounded interval [ξ¯,ξ¯][\underline{\xi},\overline{\xi}].

In order to complete the induction argument, we need to obtain the utility Un−1iU\_{n-1}^{i} for the next period.
By ([3.2](https://arxiv.org/html/2510.11261v1#S3.E2 "In 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{def-RU}), it satisfies

|  |  |  |
| --- | --- | --- |
|  | e−ζi​Un−1i=e−ζi​cn−1i,∗​Δ+δi​e−ψi​ηni​β​(xi−cn−1i,∗​Δ)​exp⁡(ψiγi​log⁡V~n−1​(𝐬,y,zi,ϱi)).e^{-\zeta\_{i}U\_{n-1}^{i}}=e^{-\zeta\_{i}c^{i,\*}\_{n-1}}\Delta+\delta\_{i}e^{-\psi\_{i}\eta\_{n}^{i}\beta(x^{i}-c^{i,\*}\_{n-1}\Delta)}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\Bigr). |  |

The right-hand side of the above equality can be evaluated by using ([3.11](https://arxiv.org/html/2510.11261v1#S3.E11 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-c\_dummy}) as

|  |  |  |
| --- | --- | --- |
|  | e−ζi​cn−1i,∗​Δ+1ψi​ηni​β​ζi​e−ζi​cn−1i,∗=ζi+Δ​ψi​ηni​βψi​ηni​β​e−ζi​cn−1i,∗=ζi+Δ​ψi​ηni​βψi​ηni​β​exp⁡{−ζi​ψi​ηni​βζi+Δ​ψi​ηni​β​xi+ζiζi+Δ​ψi​ηni​β​log⁡[δi​ψi​ηni​βζi​exp⁡(ψiγi​log⁡V~n−1​(𝐬,y,zi,ϱi))]}.\begin{split}&e^{-\zeta\_{i}c^{i,\*}\_{n-1}}\Delta+\frac{1}{\psi\_{i}\eta\_{n}^{i}\beta}\zeta\_{i}e^{-\zeta\_{i}c\_{n-1}^{i,\*}}=\frac{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}{\psi\_{i}\eta\_{n}^{i}\beta}e^{-\zeta\_{i}c\_{n-1}^{i,\*}}\\ &=\frac{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}{\psi\_{i}\eta\_{n}^{i}\beta}\exp\Bigl\{-\frac{\zeta\_{i}\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}x^{i}+\frac{\zeta\_{i}}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}\log\Bigl[\frac{\delta\_{i}\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\Bigr)\Bigr]\Bigr\}.\end{split} |  |

It follows that the utility Un−1iU\_{n-1}^{i}
is given by

|  |  |  |
| --- | --- | --- |
|  | Un−1i​(xi,𝐬,y,zi,ϱi)=ψi​ηni​βζi+Δ​ψi​ηni​β​xi−1ζi+Δ​ψi​ηni​β​log⁡{δi​ψi​ηni​βζi​exp⁡(ψiγi​log⁡V~n−1​(𝐬,y,zi,ϱi))}−1ζi​log⁡(ζi+Δ​ψi​ηni​βψi​ηni​β).\begin{split}U\_{n-1}^{i}(x^{i},{\bf{s}},y,z^{i},\varrho\_{i})&=\frac{\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}x^{i}-\frac{1}{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}\log\Bigl\{\frac{\delta\_{i}\psi\_{i}\eta\_{n}^{i}\beta}{\zeta\_{i}}\exp\Bigl(\frac{\psi\_{i}}{\gamma\_{i}}\log\widetilde{V}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})\Bigr)\Bigr\}\\ &-\frac{1}{\zeta\_{i}}\log\Bigl(\frac{\zeta\_{i}+\Delta\psi\_{i}\eta\_{n}^{i}\beta}{\psi\_{i}\eta\_{n}^{i}\beta}\Bigr).\end{split} |  |

on the set {(Xn−1i,𝐒n−1,Yn−1,Zn−1i,ϱi)=(xi,𝐬,y,zi,ϱi)}\{(X\_{n-1}^{i},{\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i})=(x^{i},{\bf{s}},y,z^{i},\varrho\_{i})\}.
By setting the right-hand side equal to ηn−1i​xi−Vn−1​(𝐬,y,zi,ϱi)\eta\_{n-1}^{i}x^{i}-V\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i}), we obtained the desired recursive relation
for ηni\eta\_{n}^{i} and VnV\_{n}. It is now clear that (ηni)n=1N(\eta\_{n}^{i})\_{n=1}^{N} are ℱ0i{\cal F}\_{0}^{i}-measurable, strictly positive and bounded,
and that VnV\_{n} is a bounded function on 𝒮n×𝒴n×𝒵n×Γ→ℝ{\cal S}^{n}\times{\cal Y}\_{n}\times{\cal Z}\_{n}\times\Gamma\rightarrow\mathbb{R}
for every 0≤n≤N0\leq n\leq N.
∎

### 3.3 Mean-field equilibrium among the agents with recursive utilities

Finally, as a main goal of this section, we shall derive a set of transition probabilities of the stock so that the mean-field equilibrium holds
among the agents with recursive utilities. As before, we incorporate the existence of stochastic external order flow LnL\_{n} at each tnt\_{n},
but it is now allowed to be path-dependent on the stock price:

###### Assumption 3.3.

For every 1≤n≤N1\leq n\leq N, Ln−1:𝒮n−1×𝒴n−1→ℝL\_{n-1}:{\cal S}^{n-1}\times{\cal Y}\_{n-1}\rightarrow\mathbb{R} is a bounded measurable function.

###### Definition 3.1.

We say that the system is in the mean-field equilibrium if

|  |  |  |
| --- | --- | --- |
|  | limNp→∞1Np​∑i=1Npϕn−1i,∗​(𝐒n−1,Yn−1,Zn−1i,ϱi)=Ln−1​(𝐒n−1,Yn−1),\lim\_{N\_{p}\rightarrow\infty}\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\phi^{i,\*}\_{n-1}({\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i})=L\_{n-1}({\bf{S}}^{n-1},Y\_{n-1}), |  |

ℙ\mathbb{P}-a.s. for every 1≤n≤N1\leq n\leq N with ϕn−1i,∗\phi^{i,\*}\_{n-1} defined by ([3.4](https://arxiv.org/html/2510.11261v1#S3.E4 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-phinm1}).

Since (Zi,ϱi),i∈ℕ(Z^{i},\varrho\_{i}),i\in\mathbb{N} are independent and identically distributed and also independent of the process (S,Y)(S,Y), the above condition for the mean-field equilibrium
can be represented by

|  |  |  |
| --- | --- | --- |
|  | 𝔼1​[ϕn−11,∗​(𝐬,y,Zn−11,ϱ1)]=Ln−1​(𝐬,y)\mathbb{E}^{1}\bigl[\phi^{1,\*}\_{n-1}({\bf{s}},y,Z^{1}\_{n-1},\varrho\_{1})\bigr]=L\_{n-1}({\bf{s}},y) |  |

for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N.
It is now straightforward to derive the counterpart of Theorem [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").

###### Theorem 3.2.

Let Assumptions [3.1](https://arxiv.org/html/2510.11261v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), [3.2](https://arxiv.org/html/2510.11261v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [3.3](https://arxiv.org/html/2510.11261v1#S3.Thmassumption3 "Assumption 3.3. ‣ 3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") be in force.
Then there exists a unique mean-field equilibrium and the associated transition probabilities of the stock are given by

|  |  |  |
| --- | --- | --- |
|  | pn−1​(𝐬,y):=ℙ0​(Sn=u~​Sn−1|(𝐒n−1,Yn−1)=(𝐬,y))=(−d)/{u​exp⁡(1𝔼1​[1/(γ1​ηn1)]​[𝔼1​(log⁡(fn−1​(𝐬,y,Zn−11,ϱ1))γ1​ηn1)−(u−d)​Ln−1​(𝐬,y)])−d}\begin{split}&p\_{n-1}({\bf{s}},y):=\mathbb{P}^{0}\Bigl(S\_{n}=\widetilde{u}S\_{n-1}|({\bf{S}}^{n-1},Y\_{n-1})=({\bf{s}},y)\Bigr)\\ &=(-d)\Big/\Bigl\{u\exp\Bigl(\frac{1}{\mathbb{E}^{1}[1/(\gamma\_{1}\eta\_{n}^{1})]}\Bigl[\mathbb{E}^{1}\Bigl(\frac{\log(f\_{n-1}({\bf{s}},y,Z^{1}\_{n-1},\varrho\_{1}))}{\gamma\_{1}\eta\_{n}^{1}}\Bigr)-(u-d)L\_{n-1}({\bf{s}},y)\Bigr]\Bigr)-d\Bigr\}\end{split} |  |

for every (𝐬,y)∈𝒮n−1×𝒴n−1({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}, 1≤n≤N1\leq n\leq N. Moreover, with the above transition probabilities,
there exists some positive constant Cn−1C\_{n-1} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|1Np​∑i=1Npϕn−1i,∗​(𝐒n−1,Yn−1,Zn−1i,ϱi)−Ln−1​(𝐒n−1,Yn−1)|2≤Cn−1Np\mathbb{E}\Bigl|\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}\phi^{i,\*}\_{n-1}({\bf{S}}^{n-1},Y\_{n-1},Z\_{n-1}^{i},\varrho\_{i})-L\_{n-1}({\bf{S}}^{n-1},Y\_{n-1})\Bigr|^{2}\leq\frac{C\_{n-1}}{N\_{p}} |  |

for every 1≤n≤N1\leq n\leq N, which gives the convergence rate in the large population limit.

###### Proof.

The proof is analogous to that of Theorem [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
The expression for the transition probabilities (pn−1​(𝐬,y))(p\_{n-1}({\bf{s}},y)) is a direct consequence of ([3.4](https://arxiv.org/html/2510.11261v1#S3.E4 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-phinm1}).
Assumptions [3.2](https://arxiv.org/html/2510.11261v1#S3.Thmassumption2 "Assumption 3.2. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [3.3](https://arxiv.org/html/2510.11261v1#S3.Thmassumption3 "Assumption 3.3. ‣ 3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") guarantees that fN−1f\_{N-1} is a.s. strictly positive and bounded
and hence the condition (vii) in Assumption [3.1](https://arxiv.org/html/2510.11261v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") is satisfied for (pN−1,qN−1)(p\_{N-1},q\_{N-1}).
It then makes ϕN−1i,∗\phi^{i,\*}\_{N-1} a.s. bounded and thus V~N−1\widetilde{V}\_{N-1} becomes a.s. strictly positive and bounded.
It then follows that VN−1V\_{N-1} and hence fN−2f\_{N-2} are a.s. bounded functions,
which shows that (pN−2,qN−2)(p\_{N-2},q\_{N-2}) satisfies the condition (vii).
In this way, a simple induction shows that the transition probabilities satisfy Assumption [3.1](https://arxiv.org/html/2510.11261v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.1 The setup and notation ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") (vii)
for every period. The second claim can be proved
by noticing that the optimal position ϕn−1i,∗\phi^{i,\*}\_{n-1} in the equilibrium is given by for (𝐬,y,zi,ϱi)∈𝒮n−1×𝒴n−1×𝒵n−1×Γ({\bf{s}},y,z^{i},\varrho\_{i})\in{\cal S}^{n-1}\times{\cal Y}\_{n-1}\times{\cal Z}\_{n-1}\times\Gamma,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕn−1i,∗​(𝐬,y,zi,ϱi)=1(u−d)​{log⁡fn−1​(𝐬,y,zi,ϱi)γi​ηni−1/(γi​ηni)𝔼1​[1/(γ1​ηn1)]​𝔼1​(log⁡fn−1​(𝐬,y,Zn−11,ϱ1)γ1​ηn1)}+1/(γi​ηni)𝔼1​[1/(γ1​ηn1)]​Ln−1​(𝐬,y),\begin{split}\phi^{i,\*}\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})&=\frac{1}{(u-d)}\Bigl\{\frac{\log f\_{n-1}({\bf{s}},y,z^{i},\varrho\_{i})}{\gamma\_{i}\eta\_{n}^{i}}-\frac{1/(\gamma\_{i}\eta\_{n}^{i})}{\mathbb{E}^{1}[1/(\gamma\_{1}\eta\_{n}^{1})]}\mathbb{E}^{1}\Bigl(\frac{\log f\_{n-1}({\bf{s}},y,Z\_{n-1}^{1},\varrho\_{1})}{\gamma\_{1}\eta\_{n}^{1}}\Bigr)\Bigr\}\\ &+\frac{1/(\gamma\_{i}\eta\_{n}^{i})}{\mathbb{E}^{1}[1/(\gamma\_{1}\eta\_{n}^{1})]}L\_{n-1}({\bf{s}},y),\end{split} |  | ( 3.12) |

and the fact that all the relevant components are bounded.
∎

###### Remark 3.2.

It is easy to check that the required time-horizon
of the path dependence in the transition probabilities is equal to that in the liability and the incremental endowments.
In particular, if FF and gng\_{n} depend only on SNS\_{N} and SnS\_{n} respectively as in the previous section,
the transition probabilities of the form (pn−1​(s,y),qn−1​(s,y))(p\_{n-1}(s,y),q\_{n-1}(s,y)) with s∈𝒮n−1s\in{\cal S}\_{n-1} are enough to achieve the equilibrium.
Simple replacement of 𝐬∈𝒮n−1{\bf{s}}\in{\cal S}^{n-1} by s∈𝒮n−1s\in{\cal S}\_{n-1}, we obtain the corresponding results for
Theorems [3.1](https://arxiv.org/html/2510.11261v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [3.2](https://arxiv.org/html/2510.11261v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").

On the relation between the mean-field price distribution and the one in the risk-neutral measure,
most of the discussions given in Section [2.4](https://arxiv.org/html/2510.11261v1#S2.SS4 "2.4 Some implications ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") still hold.
In particular, the situation pn−1​(𝐬,y)>pℚp\_{n-1}({\bf{s}},y)>p^{\mathbb{Q}} (i.e. positive excess return)
occurs if and only if
𝔼1​[log⁡(fn−1​(𝐬,y,Zn−11,ϱ1))γ1​ηn1]<0,\displaystyle\mathbb{E}^{1}\Bigl[\frac{\log(f\_{n-1}({\bf{s}},y,Z^{1}\_{n-1},\varrho\_{1}))}{\gamma\_{1}\eta\_{n}^{1}}\Bigr]<0,
when there is no external order flow Ln−1≡0L\_{n-1}\equiv 0.
As one can see from ([3.6](https://arxiv.org/html/2510.11261v1#S3.E6 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-fnm1}), fn−1f\_{n-1} has contributions from the liability VnV\_{n}
and the incremental endowment gng\_{n}. If the liability size decreases and the endowment size simultaneously increases as the stock price grows, both effects will amplify the deviations from the risk-neutral distribution toward a higher excess return.

Since the equilibrium price distribution of the stock is determined by the need for risk hedging, the relative importance of the continuation utility
with respect to the current nominal consumption is a crucial factor in controlling the size of the risk premium.
From the expressions in ([3.7](https://arxiv.org/html/2510.11261v1#S3.E7 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-Vnm1}) and (LABEL:th-R1-Vtildenm1)(\ref{th-R1-Vtildenm1}), one can expect that the ratio

|  |  |  |
| --- | --- | --- |
|  | ηn−1iηni\frac{\eta\_{n-1}^{i}}{\eta\_{n}^{i}} |  |

is the key value. Using β≃1\beta\simeq 1 and Δ≪1\Delta\ll 1, we have
ηn−1i/ηni≃ψi/ζi\eta\_{n-1}^{i}/\eta\_{n}^{i}\simeq\psi\_{i}/\zeta\_{i}
from ([3.9](https://arxiv.org/html/2510.11261v1#S3.E9 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-etanm1}). Therefore, if
ψi<ζi\psi\_{i}<\zeta\_{i} holds for the majority of agents, we expect that the relative importance of the continuation utility
quickly decays and we would have only a small impact from it for earlier periods. In this case, significant deviations from the risk-neutral price distribution can be observed only in the later periods near the maturity. On the other hand, in the case of ψi>ζi\psi\_{i}>\zeta\_{i},
we can expect to see significant deviations throughout the interval. We shall confirm this behavior in Section [4](https://arxiv.org/html/2510.11261v1#S4 "4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").

As for the expected trading volume 𝔼​[|ϕn1,∗|2]12\mathbb{E}[|\phi^{1,\*}\_{n}|^{2}]^{\frac{1}{2}}, which gives the standard deviation of the stock
position among the agents at t=tnt=t\_{n}, we have the consistent result as in Section [2.4](https://arxiv.org/html/2510.11261v1#S2.SS4 "2.4 Some implications ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
The expression for ϕn−1i,∗\phi^{i,\*}\_{n-1} in ([3.12](https://arxiv.org/html/2510.11261v1#S3.E12 "In Theorem 3.2. ‣ 3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R2-phinm1}) shows that its size is governed by the
variation of idiosyncratic factors defined on the space (Ωi,ℱi,ℙi)(\Omega^{i},{\cal F}^{i},\mathbb{P}^{i}).
It is also quite consistent with our intuition
that the agents’ heterogeneity in idiosyncratic factors is the origin of the trading activity in the market.
Moreover, we can make use of the degrees of freedom in the process (Zni)(Z\_{n}^{i}), in particular its volatility,
to obtain the desired trading volume. We shall confirm this claim in Section [4.2](https://arxiv.org/html/2510.11261v1#S4.SS2 "4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").

Finally, let us comment on the fact that the constant shifts in FF and gng\_{n}, i.e. F↦F+cF\mapsto F+c and gn↦gn+c′g\_{n}\mapsto g\_{n}+c^{\prime}
with some constants c,c′∈ℝc,c^{\prime}\in\mathbb{R} do not affect the equilibrium price distribution.
This property can be checked by a simple induction as follows:

* •

  By ([3.6](https://arxiv.org/html/2510.11261v1#S3.E6 "In Theorem 3.1. ‣ 3.2 The individual optimization problem ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{th-R1-fnm1}), the value of fN−1f\_{N-1} remains unchanged and so are pN−1​(𝐬,y)p\_{N-1}({\bf{s}},y) and ϕN−1i,∗\phi^{i,\*}\_{N-1}.
* •

  The value of V~N−1\widetilde{V}\_{N-1} is changed only by an ℱ0i{\cal F}^{i}\_{0}-measurable multiplicative factor.
* •

  The value of VN−1V\_{N-1} is only shifted by an ℱ0i{\cal F}^{i}\_{0}-measurable term.
* •

  Thus fN−2f\_{N-2} remains once again unchanged, and so are pN−2​(𝐬,y)p\_{N-2}({\bf{s}},y) and ϕN−2i,∗\phi^{i,\*}\_{N-2}. ⋯\cdots

Therefore, the signs of FF and gng\_{n} can be altered without affecting the equilibrium price distribution.
Note however that, the cash spending is affected by these shifts.

### 3.4 Mean-field equilibrium of multiple populations

Let us briefly mention the construction of the mean-field equilibrium for multiple populations.
The population ratio among the groups must be kept constant when the large population limit is taken.
Suppose, for example, that population ratio among the mm groups are given by wp∈(0,1),p=1,⋯,mw\_{p}\in(0,1),~p=1,\cdots,m satisfying
∑p=1mwp=1\sum\_{p=1}^{m}w\_{p}=1. We enlarge the product probability space by introducing (Ωi,p,ℱi,p,(ℱtni,p)n=0N,ℙi,p)(\Omega^{i,p},{\cal F}^{i,p},({\cal F}\_{t\_{n}}^{i,p})\_{n=0}^{N},\mathbb{P}^{i,p})
for every p=1,⋯,mp=1,\cdots,m and i∈ℕi\in\mathbb{N}. If we denote the optimal trade position of the agent-ii in the group pp by ϕn−1i,p,∗\phi^{i,p,\*}\_{n-1},
the condition for the mean-field equilibrium is, with obvious notation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑p=1mwp​𝔼1,p​[ϕn−11,p,∗​(𝐬,y,Zn−11,p,ϱ1,p)]=Ln−1​(𝐬,y)\sum\_{p=1}^{m}w\_{p}\mathbb{E}^{1,p}\bigl[\phi^{1,p,\*}\_{n-1}({\bf{s}},y,Z\_{n-1}^{1,p},\varrho\_{1,p})\bigr]=L\_{n-1}({\bf{s}},y) |  | ( 3.13) |

for every (𝐬,y)∈𝒮n−1×𝒴n−1,1≤n≤N({\bf{s}},y)\in{\cal S}^{n-1}\times{\cal Y}\_{n-1},1\leq n\leq N.
Since the factor log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)\displaystyle\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr) in the optimal position ϕn−1i,p,∗\phi\_{n-1}^{i,p,\*}
is the same across the populations, solving the equation ([3.13](https://arxiv.org/html/2510.11261v1#S3.E13 "In 3.4 Mean-field equilibrium of multiple populations ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{eq-multi-p}) is straightforward. We can even mix the populations
with standard exponential utilities and the recursive utilities just discussed.

As a simple example, consider the situation where the external order flow is absent L≡0L\equiv 0 and the agents discussed in Section [2](https://arxiv.org/html/2510.11261v1#S2 "2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.")
and those in Section [3](https://arxiv.org/html/2510.11261v1#S3 "3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") have the same population size in the market.
Distinguishing the expectations and variables for the first group by tilde (such as 𝔼~1​[⋅]\widetilde{\mathbb{E}}^{1}[\cdot] and γ~1\widetilde{\gamma}\_{1}) for simplicity,
the equation ([3.13](https://arxiv.org/html/2510.11261v1#S3.E13 "In 3.4 Mean-field equilibrium of multiple populations ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{eq-multi-p}) yields

|  |  |  |
| --- | --- | --- |
|  | 0=log⁡(−pn−1​(𝐬,y)​uqn−1​(𝐬,y)​d)​(𝔼1​[1γ1​ηn1]+βnβN​𝔼~1​[1γ~1])+𝔼1​[log⁡fn−1​(𝐬,y,Zn−11,ϱi)γ1​ηn1]+βnβN​𝔼~1​[log⁡f~n−1​(s,y,Z~n−11,γ~1)γ~1]\begin{split}0&=\log\Bigl(-\frac{p\_{n-1}({\bf{s}},y)u}{q\_{n-1}({\bf{s}},y)d}\Bigr)\Bigl(\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{1}\eta\_{n}^{1}}\Bigr]+\frac{\beta^{n}}{\beta^{N}}\widetilde{\mathbb{E}}^{1}\Bigl[\frac{1}{\widetilde{\gamma}\_{1}}\Bigr]\Bigr)\\ &+\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}({\bf{s}},y,Z\_{n-1}^{1},\varrho\_{i})}{\gamma\_{1}\eta\_{n}^{1}}\Bigr]+\frac{\beta^{n}}{\beta^{N}}\widetilde{\mathbb{E}}^{1}\Bigl[\frac{\log\widetilde{f}\_{n-1}(s,y,\widetilde{Z}\_{n-1}^{1},\widetilde{\gamma}\_{1})}{\widetilde{\gamma}\_{1}}\Bigr]\end{split} |  |

on the set {(𝐒n−1,Yn−1)=(𝐬,y)}\{({\bf{S}}^{n-1},Y\_{n-1})=({\bf{s}},y)\}, where s:=sn−1s:=s\_{n-1}. It is easy to solve this equation to get the equilibrium
transition probability as

|  |  |  |
| --- | --- | --- |
|  | pn−1​(𝐬,y)=ℙ0​(Sn=u~​Sn−1|(𝐒n−1,Yn−1)=(𝐬,y))=(−d)/{u​exp⁡(𝔼1​[log⁡fn−1​(𝐬,y,Zn−11,ϱ1)γ1​ηn1]+βnβN​𝔼~1​[log⁡f~n−1​(s,y,Z~n−11,γ~1)γ~1]𝔼1​[1γ1​ηn1]+βnβN​𝔼~1​[1γ~1])−d}.\begin{split}&p\_{n-1}({\bf{s}},y)=\mathbb{P}^{0}\bigl(S\_{n}=\widetilde{u}S\_{n-1}|({\bf{S}}^{n-1},Y\_{n-1})=({\bf{s}},y)\bigr)\\ &=(-d)\Big/\left\{u\exp\left(\frac{\mathbb{E}^{1}\Bigl[\frac{\log f\_{n-1}({\bf{s}},y,Z^{1}\_{n-1},\varrho\_{1})}{\gamma\_{1}\eta\_{n}^{1}}\Bigr]+\frac{\beta^{n}}{\beta^{N}}\widetilde{\mathbb{E}}^{1}\Bigl[\frac{\log\widetilde{f}\_{n-1}(s,y,\widetilde{Z}\_{n-1}^{1},\widetilde{\gamma}\_{1})}{\widetilde{\gamma}\_{1}}\Bigr]}{\mathbb{E}^{1}\Bigl[\frac{1}{\gamma\_{1}\eta\_{n}^{1}}\Bigr]+\frac{\beta^{n}}{\beta^{N}}\widetilde{\mathbb{E}}^{1}\Bigl[\frac{1}{\widetilde{\gamma}\_{1}}\Bigr]}\right)-d\right\}.\end{split} |  |

One can prove its well-posedness across the whole time interval in the same way as in Theorems [2.2](https://arxiv.org/html/2510.11261v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.3 Mean-field equilibrium under stochastic order flow ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [3.2](https://arxiv.org/html/2510.11261v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
Moreover, if we turn off the path-dependence in FF and gng\_{n} at least, the numerical evaluation of the equilibrium distribution can be
carried out in a simple manner as in the next section.

Note that these results are quite remarkable when compared with the
situation in the continuous-time setting. In fact, if we tries to solve the corresponding problem in the formulation of Fujii & Sekine [[20](https://arxiv.org/html/2510.11261v1#bib.bib20)],
we would obtain a coupled system of mean-field qg-BSDEs, whose well-posedness would be much harder than the
single population case, not to mention its numerical evaluation.

## 4 Numerical examples

In this section, we provide some numerical examples for the models introduced in Sections [2](https://arxiv.org/html/2510.11261v1#S2 "2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.")
and [3](https://arxiv.org/html/2510.11261v1#S3 "3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") but without path dependence.
Since the models are too flexible for through analysis, we focus only on a few simple setups
to grasp characteristic behaviors of the mean-field price distributions.
In order to reduce numerical cost, we assume that YY and ZiZ^{i} are also one-dimensional discrete processes taking values on binomial trees,
and that all the ℱ0i{\cal F}^{i}\_{0}-measurable random variables are uniformly distributed over finite sets.

### 4.1 Utility for terminal wealth

Let us first consider the model discussed in Section [2](https://arxiv.org/html/2510.11261v1#S2 "2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
γi\gamma\_{i} is assumed to have a uniform distribution over (Nγ+1)(N\_{\gamma}+1) discrete values given by

|  |  |  |
| --- | --- | --- |
|  | γi​(kγ):=γ¯+(γ¯−γ¯)​kγNγ,kγ=0,⋯,Nγ.\gamma\_{i}(k\_{\gamma}):=\underline{\gamma}+(\overline{\gamma}-\underline{\gamma})\frac{k\_{\gamma}}{N\_{\gamma}},\quad k\_{\gamma}=0,\cdots,N\_{\gamma}. |  |

The process (Zni)n=0N(Z\_{n}^{i})\_{n=0}^{N} is supposed to follow a one-dimensional binomial process modeled by

|  |  |  |
| --- | --- | --- |
|  | Zn+1i=Zni​Rn+1i,Z\_{n+1}^{i}=Z\_{n}^{i}R\_{n+1}^{i}, |  |

where (Rni)(R\_{n}^{i}) is an (ℱtni)({\cal F}^{i}\_{t\_{n}})-adapted process taking values either uzu\_{z} or dzd\_{z}, where Rn+1i=uzR\_{n+1}^{i}=u\_{z} occurs with probability pzp\_{z} and Rn+1i=dzR\_{n+1}^{i}=d\_{z} with qz:=1−pzq\_{z}:=1-p\_{z}.
We take uz=(dz)−1=exp⁡(σz​Δ)u\_{z}=(d\_{z})^{-1}=\exp(\sigma\_{z}\sqrt{\Delta}). We also assume Z0i=z0∈(0,∞)Z\_{0}^{i}=z\_{0}\in(0,\infty) common for all the agents in order to reduce
numerical costs. We model the process (Yn)n=0N(Y\_{n})\_{n=0}^{N} similarly but it is assumed to follow an approximate Gaussian process:

|  |  |  |
| --- | --- | --- |
|  | Yn+1=Yn+Rn+1y,Y\_{n+1}=Y\_{n}+R\_{n+1}^{y}, |  |

where (Rny)(R\_{n}^{y}) is an (ℱtn0)({\cal F}^{0}\_{t\_{n}})-adapted process taking values either uyu\_{y} or dyd\_{y},
where Rn+1y=uyR\_{n+1}^{y}=u\_{y} with probability pyp\_{y} and Rn+1y=dyR\_{n+1}^{y}=d\_{y} with qy:=1−pyq\_{y}:=1-p\_{y}.
We take uy=(−dy)=σy​Δu\_{y}=(-d\_{y})=\sigma\_{y}\sqrt{\Delta}.
Finally, for the stock-price process (Sn)(S\_{n}), we set u~=(d~)−1=exp⁡(σ​Δ)\widetilde{u}=(\widetilde{d})^{-1}=\exp(\sigma\sqrt{\Delta}).

The parameter values to be used throughout this subsection are summarized in Table [1](https://arxiv.org/html/2510.11261v1#S4.T1 "Table 1 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") below. Recall that the initial wealth ξi\xi\_{i}
is irrelevant for our analysis.

| parameter | γ¯\underline{\gamma} | γ¯\overline{\gamma} | NγN\_{\gamma} | z0z\_{0} | σz\sigma\_{z} | pzp\_{z} | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.5 | 1.5 | 4 | 1.0 | 12% | 0.5 | 1.0 | 12% | 0.5 | 1.0 | 15% | 3.3% | 3yr | 48 |

Table 1:  parameter values



![Refer to caption](p-T1-1yr-3yr.png)


Figure 1: Comparison of the marginal price distributions under the equilibrium measure (P)(P) and the risk-neutral measures (Q)(Q)
at 1-year and 3-year points for ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}).

![Refer to caption](p-T1-3yr-top-bottom.png)


Figure 2: Comparison of the marginal price distribution PP and the conditional price distributions P(⋅|Ytop−25%)P(\cdot|Y^{\rm top-25\%})
and P(⋅|Ybottom−25%)P(\cdot|Y^{\rm bottom-25\%}) at 3-year point for ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}).

![Refer to caption](p-T1-exp.png)


Figure 3: Comparison of the expected values of S​(tn)S(t\_{n}) under the equilibrium and the risk-neutral measures
for ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}).

![Refer to caption](p-T1-phi.png)


Figure 4: The time evolution of the expected trading volume 𝔼ℙ​[|ϕ1,∗​(t)|2]12\mathbb{E}^{\mathbb{P}}[|\phi^{1,\*}(t)|^{2}]^{\frac{1}{2}} of the optimal stock position for ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}).

Let us first assume that there is no external oder flow Ln≡0L\_{n}\equiv 0, and that the
terminal liability FF is given by the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(SN,YN,ZNi):=C−3​SN​YN​ZNi,F(S\_{N},Y\_{N},Z\_{N}^{i}):=C-3S\_{N}Y\_{N}Z\_{N}^{i}, |  | ( 4.1) |

where C∈ℝC\in\mathbb{R} is an arbitrary real constant. Since the result is unchanged by the constant shift,
one can adjust, if necessary, the constant CC to make the liability positive.
From the discussion in Section [2.4](https://arxiv.org/html/2510.11261v1#S2.SS4 "2.4 Some implications ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."),
we expect that the equilibrium price distribution for this liability has positive excess return.
We can check if this is actually the case by observing Figure [4](https://arxiv.org/html/2510.11261v1#S4.F4 "Figure 4 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."),
which presents the comparison of the marginal price distributions under the equilibrium measure (P)(P)
and the risk-neutral measure (Q)(Q) at 1-year and 3-year points.

We can also provide the conditional price distribution ℙ​(Sn∈A|Yn=y),∀A⊂𝒮n\mathbb{P}(S\_{n}\in A|Y\_{n}=y),~\forall A\subset{\cal S}\_{n} for each y∈𝒴ny\in{\cal Y}\_{n}.
At 3-year point, the value of YY that marks the top 25% (Ytop−25)(Y^{\rm top-25}) (resp. bottom 25% (Ybottom−25)(Y^{\rm bottom-25}))
is equivalent to a total of 36 up moves (resp. 12 up moves). Comparison of the conditional distributions
{ℙ​(Sn=s|Ytop−25),ℙ​(Sn=s|Ybottom−25),∀s∈𝒮n}\{\mathbb{P}(S\_{n}=s|Y^{\rm top-25}),~\mathbb{P}(S\_{n}=s|Y^{\rm bottom-25}),~\forall s\in{\cal S}\_{n}\} and the
marginal distribution at 3-year point (n=48)(n=48) is given in Figure [4](https://arxiv.org/html/2510.11261v1#S4.F4 "Figure 4 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
As expected from the functional form in ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}), the deviations from the risk-neutral distribution
are positive and become larger for the larger value of YY.
In Figure [4](https://arxiv.org/html/2510.11261v1#S4.F4 "Figure 4 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we provide the time-evolution of (𝔼ℙ​[S​(t)],𝔼ℚ​[S​(t)])(\mathbb{E}^{\mathbb{P}}[S(t)],\mathbb{E}^{\mathbb{Q}}[S(t)]),
the expected value of the stock price under the equilibrium measure and the risk-neutral measure, respectively.
Figure [4](https://arxiv.org/html/2510.11261v1#S4.F4 "Figure 4 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") gives the time-evolution of the expected trading volume 𝔼ℙ​[|ϕ1,∗​(t)|2]\sqrt{\mathbb{E}^{\mathbb{P}}[|\phi^{1,\*}(t)|^{2}]}.

In Figures [8](https://arxiv.org/html/2510.11261v1#S4.F8 "Figure 8 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), [8](https://arxiv.org/html/2510.11261v1#S4.F8 "Figure 8 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), [8](https://arxiv.org/html/2510.11261v1#S4.F8 "Figure 8 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") and [8](https://arxiv.org/html/2510.11261v1#S4.F8 "Figure 8 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we present
the corresponding results for the different liability function

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(SN,YN,ZNi):=C+3​SN​YN​ZNiF(S\_{N},Y\_{N},Z\_{N}^{i}):=C+3S\_{N}Y\_{N}Z\_{N}^{i} |  | ( 4.2) |

which exhibits the opposite sign of sensitivity to the stock price. We see that the excess return becomes negative in this case.

![Refer to caption](p-T2-1yr-3yr.png)


Figure 5: Comparison of the marginal price distributions under the equilibrium measure (P)(P) and the risk-neutral measures (Q)(Q)
at 1-year and 3-year points for ([4.2](https://arxiv.org/html/2510.11261v1#S4.E2 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F2}).

![Refer to caption](p-T2-3yr-top-bottom.png)


Figure 6: Comparison of the marginal price distribution PP and the conditional price distributions P(⋅|Ytop−25%)P(\cdot|Y^{\rm top-25\%})
and P(⋅|Ybottom−25%)P(\cdot|Y^{\rm bottom-25\%}) at 3-year point for ([4.2](https://arxiv.org/html/2510.11261v1#S4.E2 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F2}).

![Refer to caption](p-T2-exp.png)


Figure 7: Comparison of the expected values of S​(tn)S(t\_{n}) under the equilibrium and the risk-neutral measures
for ([4.2](https://arxiv.org/html/2510.11261v1#S4.E2 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F2}).

![Refer to caption](p-T2-phi.png)


Figure 8: The time evolution of the expected trading volume 𝔼ℙ​[|ϕ1,∗​(t)|2]12\mathbb{E}^{\mathbb{P}}[|\phi^{1,\*}(t)|^{2}]^{\frac{1}{2}} of the optimal stock position for ([4.2](https://arxiv.org/html/2510.11261v1#S4.E2 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F2}).

Now, let us turn on the external order flow. We continue to use the same parameter values in Table [1](https://arxiv.org/html/2510.11261v1#S4.T1 "Table 1 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.")
and the liability function defined by ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}), but now with external order flow (without yy-dependence):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ln​(s):=a​max⁡(s−c,0).L\_{n}(s):=a\max(s-c,0). |  | ( 4.3) |

We set c=1.75c=1.75 and consider two scenarios, one is a=7a=7 and the other is a=−7a=-7. In the former case, there is positive supply of the stock
when the stock price is very large s>1.75s>1.75, and in the latter case the positive demand (i.e. negative supply) for s>1.75s>1.75.
In Figure [9](https://arxiv.org/html/2510.11261v1#S4.F9 "Figure 9 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we compare the marginal as well as conditional price distribution as in Figure [4](https://arxiv.org/html/2510.11261v1#S4.F4 "Figure 4 ‣ 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.")
with the positive external order flow in the left panel and the negative one in the right panel.
We can clearly observe that the positive supply generates a heavy right tail in the equilibrium distributions
and that the positive demand causes the opposite. In order to absorb positive supply, higher excess return
is required by the agents.

![Refer to caption](p-T1-3yr-TB-Lplus.png)

![Refer to caption](p-T1-3yr-TB-Lminus.png)

Figure 9: Comparison of the marginal price distribution PP and the conditional price distributions P(⋅|Ytop−25%)P(\cdot|Y^{\rm top-25\%})
and P(⋅|Ybottom−25%)P(\cdot|Y^{\rm bottom-25\%}) at 3-year point. FF is given by ([4.1](https://arxiv.org/html/2510.11261v1#S4.E1 "In 4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{Terminal-F1}) and the
external order flow is equal to Ln​(s)=7​max⁡(s−1.75,0)L\_{n}(s)=7\max(s-1.75,0) (i.e. positive supply) in the left panel
and Ln​(s)=−7​max⁡(s−1.75,0)L\_{n}(s)=-7\max(s-1.75,0) (i.e. positive demand) in the right panel.

### 4.2 Recursive utility

We now consider the recursive utility model discussed in Section [3](https://arxiv.org/html/2510.11261v1#S3 "3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
For numerical ease, we assume no path-dependence.
The liability FF is then assumed to depend solely on the terminal stock price SNS\_{N},
while the incremental endowments gng\_{n} depend solely on the current price SnS\_{n}.
See Remark [3.2](https://arxiv.org/html/2510.11261v1#S3.Thmremark2 "Remark 3.2. ‣ 3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.")
for the corresponding results.
We use the same models for (Sn,Yn,Zni)n=0N(S\_{n},Y\_{n},Z\_{n}^{i})\_{n=0}^{N} and γi\gamma\_{i} as in Section [4.1](https://arxiv.org/html/2510.11261v1#S4.SS1 "4.1 Utility for terminal wealth ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
ψi\psi\_{i} is assumed to have a uniform distribution over (Nψ+1)(N\_{\psi}+1) discrete values given by

|  |  |  |
| --- | --- | --- |
|  | ψi​(kψ):=ψ¯+(ψ¯−ψ¯)​kψNψ,kψ=0,⋯,Nψ.\psi\_{i}(k\_{\psi}):=\underline{\psi}+(\overline{\psi}-\underline{\psi})\frac{k\_{\psi}}{N\_{\psi}},\quad k\_{\psi}=0,\cdots,N\_{\psi}. |  |

For simplicity, we assume that δi:=exp⁡(−ρ​Δ)\delta\_{i}:=\exp(-\rho\Delta) has a common value across the agents.
Moreover, we assume that ζi\zeta\_{i} and ψi\psi\_{i} are related by

|  |  |  |
| --- | --- | --- |
|  | ψi/ζi=aζ,\psi\_{i}/\zeta\_{i}=a\_{\zeta}, |  |

where aζa\_{\zeta} is a positive constant common across the agents. We shall use the parameter aζa\_{\zeta} to control the ratio ηn−1i/ηni\eta\_{n-1}^{i}/\eta\_{n}^{i}.
The parameter values to be used throughout this subsection (expect the last example) are summarized in Table [2](https://arxiv.org/html/2510.11261v1#S4.T2 "Table 2 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") below.

| parameter | γ¯\underline{\gamma} | γ¯\overline{\gamma} | NγN\_{\gamma} | ψ¯\underline{\psi} | ψ¯\overline{\psi} | NψN\_{\psi} | ρ\rho | z0z\_{0} | σz\sigma\_{z} | pzp\_{z} | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.4 | 1.6 | 3 | 0.5 | 1.5 | 2 | 5.0% | 1.0 | 12% | 0.5 | 1.0 | 12% | 0.5 | 1.0 | 15% | 3.3% | 3yr | 48 |

Table 2: parameter values



![Refer to caption](p-R1-1yr.png)

![Refer to caption](p-R1-3yr.png)

Figure 10: Comparison of the risk-neutral as well as the equilibrium marginal price distributions with aζ=0.9,0.95,1.0,1.05a\_{\zeta}=0.9,0.95,1.0,1.05 at 1-year (left panel) and 3-year (right panel) points.

![Refer to caption](p-R-exp.png)


Figure 11: Comparison of the expected values of S​(tn)S(t\_{n}) under the risk-neutral as well as the equilibrium price distributions with
aζ=0.9,0.95,1.0,1.05a\_{\zeta}=0.9,0.95,1.0,1.05.

Since the effects of the stochastic liability and incremental endowments on the equilibrium price distributions
are as expected from the results in the previous subsection, let us first concentrate on
the effects of the factor aζ=ψi/ζia\_{\zeta}=\psi\_{i}/\zeta\_{i}.
We set Ln≡0,∀nL\_{n}\equiv 0,~\forall n and define the liability function
and the incremental endowments in the following way:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(SN,YN,ZNi):=C−2​SN​YN​ZNi,\displaystyle F(S\_{N},Y\_{N},Z\_{N}^{i}):=C-2S\_{N}Y\_{N}Z\_{N}^{i}, |  | ( 4.4) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | gn​(Sn,Yn,Zni):=C′+1.5​Δ​Sn​Yn​Zni,1≤n≤N.\displaystyle g\_{n}(S\_{n},Y\_{n},Z\_{n}^{i}):=C^{\prime}+1.5\Delta S\_{n}Y\_{n}Z\_{n}^{i},\quad 1\leq n\leq N. |  | ( 4.5) |

Here, C,C′C,C^{\prime} are arbitrary constants irrelevant for the equilibrium distributions.
In Figure [11](https://arxiv.org/html/2510.11261v1#S4.F11 "Figure 11 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we plot the risk-neutral as well as the equilibrium marginal price distributions
with 4 different values of the ratio aζ=0.9,0.95,1.0,1.05a\_{\zeta}=0.9,0.95,1.0,1.05 at 1-year (left panel) and 3-year (right panel) points.
Figure [11](https://arxiv.org/html/2510.11261v1#S4.F11 "Figure 11 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") provides the time evolution of the expected value of the stock price S​(tn)S(t\_{n})
for each case. As inferred from the discussion in the last part of Section [3.3](https://arxiv.org/html/2510.11261v1#S3.SS3 "3.3 Mean-field equilibrium among the agents with recursive utilities ‣ 3 Recursive utility optimization with path-dependent cash flows ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."),
the deviations from the risk-neutral distribution become smaller as aζa\_{\zeta} decreases,
and this effect (smaller deviations) is more profound in earlier periods.
We can observe that the value of aζ=ψi/ζia\_{\zeta}=\psi\_{i}/\zeta\_{i} can efficiently control
the level of the risk-premium without changing the other parameters.

Next, let us turn off the incremental endowments gn≡0g\_{n}\equiv 0 while keeping the
liability function the same as in ([4.4](https://arxiv.org/html/2510.11261v1#S4.E4 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{num-functions}).
We are now going to study the effects of an external order flow defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(Sn)=8​max⁡(Sn−1.6,0)−8​max⁡(1.1−Sn,0),0≤n≤N−1.L(S\_{n})=8\max(S\_{n}-1.6,0)-8\max(1.1-S\_{n},0),\quad 0\leq n\leq N-1. |  | ( 4.6) |

to demonstrate how flexibly the shape of equilibrium distributions can change.
([4.6](https://arxiv.org/html/2510.11261v1#S4.E6 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{eq-Lext}) means that there is positive supply (i.e. sell orders from other groups) of the stock when the stock price is high
and positive demand (i.e. buy orders from other groups) when the stock price is low.
In Figure [12](https://arxiv.org/html/2510.11261v1#S4.F12 "Figure 12 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), with aζ=1.07a\_{\zeta}=1.07,
we compare the equilibrium price distribution at 3-year point with LnL\_{n} given by ([4.6](https://arxiv.org/html/2510.11261v1#S4.E6 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{eq-Lext})
and that with Ln≡0L\_{n}\equiv 0. It shows that the existence of the external order flow ([4.6](https://arxiv.org/html/2510.11261v1#S4.E6 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{eq-Lext})
makes the equilibrium distribution fat-tailed in both directions, which is as expected by the analysis
made in the last paragraph of Section [2.4](https://arxiv.org/html/2510.11261v1#S2.SS4 "2.4 Some implications ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
Corresponding modifications in the terminal liability FF and/or the incremental endowments gng\_{n} would yield similar results.

![Refer to caption](p-R1-L-nL.png)


Figure 12: Comparison of the stock price distributions at 3-year point with LnL\_{n} given by ([4.6](https://arxiv.org/html/2510.11261v1#S4.E6 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{eq-Lext}) and Ln≡0L\_{n}\equiv 0 .

In the last numerical example, we examine the effect of σz\sigma\_{z}, the volatility of the process (Zni)(Z^{i}\_{n}),
on trading volume. This volume is quantified by the standard deviation of the stock position among the agents
𝔼1​[|ϕti,∗|2]12\mathbb{E}^{1}[|\phi^{i,\*}\_{t}|^{2}]^{\frac{1}{2}}, as discussed in Section [2.4](https://arxiv.org/html/2510.11261v1#S2.SS4 "2.4 Some implications ‣ 2 Utility optimization for terminal wealth ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").
To highlight the effect of σz\sigma\_{z}, we reduce the variation in (γi,ψi,ζi)(\gamma\_{i},\psi\_{i},\zeta\_{i}).
The parameter values we use are summarized in Table [3](https://arxiv.org/html/2510.11261v1#S4.T3 "Table 3 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.") below:

| parameter | γ¯\underline{\gamma} | γ¯\overline{\gamma} | NγN\_{\gamma} | ψ¯\underline{\psi} | ψ¯\overline{\psi} | NψN\_{\psi} | ρ\rho | z0z\_{0} | aζa\_{\zeta} | pzp\_{z} | Y0Y\_{0} | σy\sigma\_{y} | pyp\_{y} | S0S\_{0} | σ\sigma | rr | TT | NN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value | 0.95 | 1.05 | 2 | 0.95 | 1.05 | 2 | 5.0% | 1.0 | 1.02 | 0.5 | 1.0 | 12% | 0.5 | 1.0 | 15% | 3.3% | 3yr | 48 |

Table 3: value of parameters for Figure [13](https://arxiv.org/html/2510.11261v1#S4.F13 "Figure 13 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research.").

We use the terminal liability and the incremental endowments defined by ([4.4](https://arxiv.org/html/2510.11261v1#S4.E4 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{num-functions}) and ([4.5](https://arxiv.org/html/2510.11261v1#S4.E5 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{num-endow}).
In the right panel of Figure [13](https://arxiv.org/html/2510.11261v1#S4.F13 "Figure 13 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we have plotted the evolution of the trading volume 𝔼ℙ​[|ϕ1,∗​(t)|2]12\mathbb{E}^{\mathbb{P}}[|\phi^{1,\*}(t)|^{2}]^{\frac{1}{2}}
for 5 different volatilities of the process (Zni)(Z^{i}\_{n}): σz=0%,5%,10%,15%,20%\sigma\_{z}=0\%,~5\%,~10\%,~15\%,~20\%.
We observe that the trading volume increases with the volatility σz\sigma\_{z}.
The non-zero trading volume, even when σz=0\sigma\_{z}=0, stems from the non-zero variation in the risk-aversion coefficients.
The near-identical trading volume
in the earliest period is a consequence of our assumption that the agents have the common initial value Z0i≡z0=1,∀i∈ℕZ\_{0}^{i}\equiv z\_{0}=1,~\forall i\in\mathbb{N}, an assumption made solely for numerical convenience.

![Refer to caption](p-R-sigma-Z-Exp.png)

![Refer to caption](p-R-sigma-Z-phi.png)

Figure 13: Left panel: Comparison of the expected value of S​(tn)S(t\_{n}) under the risk-neutral as well as the equilibrium price distributions with
σz=0%,5%,10%,15%,20%\sigma\_{z}=0\%,5\%,10\%,15\%,20\%.
Right panel: Comparison of the trading volumes 𝔼ℙ​[|ϕ1,∗​(t)|2]12\mathbb{E}^{\mathbb{P}}[|\phi^{1,\*}(t)|^{2}]^{\frac{1}{2}} with σz:=0%,5%,10%,15%,20%\sigma\_{z}:=0\%,5\%,10\%,15\%,20\%.

In the left panel of Figure [13](https://arxiv.org/html/2510.11261v1#S4.F13 "Figure 13 ‣ 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."), we have plotted the evolution of the expected value of S​(t)S(t) for each case of σz\sigma\_{z}.
(The result for the risk-neutral measure is also plotted for reference.)
From this result, we see that the size of excess return is almost unaffected by the volatility σz\sigma\_{z}.
This stems from the functional form of ([4.4](https://arxiv.org/html/2510.11261v1#S4.E4 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{num-functions}) and ([4.5](https://arxiv.org/html/2510.11261v1#S4.E5 "In 4.2 Recursive utility ‣ 4 Numerical examples ‣ Mean-Field Price Formation on Trees 11footnote 1The authors are not responsible in any manner for any losses caused by the use of any contents in this research."))(\ref{num-endow}), as well as the fact that the expectation value of ZniZ^{i}\_{n} remains nearly identical across all cases. These results suggest that we can control trading volume by changing σz\sigma\_{z} without significantly affecting the risk-premium.
Although trading volume is also significantly influenced by the variation in ℱ0i{\cal F}\_{0}^{i}-measurable random variables such as γi,ζi\gamma\_{i},\zeta\_{i} and
ψi\psi\_{i}, these variables may simultaneously induce a large change in the risk-premium.

## 5 Concluding remarks and future research directions

In this work, we have proved the existence of the unique mean-field equilibrium for agents with exponential-type utilities and derived an explicit formula for equilibrium transition probabilities of the stock price by restricting its trajectories onto a recombining binomial tree. The agents are supposed to have stochastic terminal liabilities and incremental endowments, both dependent on unhedgeable common and idiosyncratic factors in addition to the past trajectory of the stock price. We also examined the impacts of external order flow.
Finally, we provided numerical examples to illustrate qualitative effects of these components on the equilibrium price distributions. Our results clearly show that the equilibrium distributions can substantially change their shapes in response to these inputs. In particular, focusing on liabilities whose size changes countercyclically with market performance, we have found that the more levered financial firms and institutional investors are, the higher the risk premium is. The same observation also holds for cyclical endowments, i.e., non-tradable incomes originating from the firms’ other business lines. Empirical analysis regarding this finding would constitute an important research topic.
On the other hand, the trading volume per capita crucially depends on the variation in idiosyncratic factors.

Our method can also be applied to other asset classes, such as commodities and foreign exchanges, as long as they can be
modeled by binomial trees.
The Black-Derman-Toy model (BDG) [[8](https://arxiv.org/html/2510.11261v1#bib.bib8)], which is a famous short-rate model constructed on a binomial tree, may provide an
interesting framework to analyze a mean-field equilibrium for a risk-free interest rates.
Although many of them are becoming obsolete in today’s financial markets,
various techniques (such as “implied binomial trees”) have been developed by practitioners for tree-based derivative pricing
since its initial invention by Sharpe. These can now serve as valuable tools for investigating the mean-field equilibrium in our framework.
For a comprehensive overview of general Markov processes for financial applications,
see, for example, the textbooks by Bäuerle & Rieder [[7](https://arxiv.org/html/2510.11261v1#bib.bib7)] and Hernández-Lerma & Lasserre [[25](https://arxiv.org/html/2510.11261v1#bib.bib25)].

Extensions to general multinomial trees and multi-asset frameworks constitute interesting future research directions.
Although our framework remains conceptually the same, there appear several hurdles to be overcome.

* •

  Although it is not difficult to put appropriate assumptions so that there exists a unique optimal solution,
  its explicit form is generally unavailable.
* •

  There are more degrees of freedom in the transition probabilities than are imposed by the market-clearing
  conditions. This remaining freedom must be fixed by imposing an appropriate dependence structure among the assets.

Due to these issues, although the second point might be beneficial for flexibility,
numerical costs would be significantly higher than the single asset case, in particular, in the presence of
common noises. The fact that the market-clearing condition alone does not uniquely determine the asset price process
is already well known. (See, Karatzas & Shreve [[30](https://arxiv.org/html/2510.11261v1#bib.bib30), Chapter 4].)
This is because that one can build a equivalent set of mutual funds
from the original stocks without affecting the market-clearing condition.

Constructing mean-field equilibrium among agents with other utilities, such as power type, remains one of the most challenging problems.
This is a common issue, mirroring the challenge in the continuous-time setting. For utilities other than the exponential-type, the optimal
trade position ϕni,∗\phi^{i,\*}\_{n} is, in general, dependent on the size of weal at tnt\_{n}.
Since the wealth of each agent wniw\_{n}^{i} at tnt\_{n} depends on the trading strategy up to tnt\_{n},
the mean-field equilibrium condition leads to a complex fixed-point problem involving the backward ϕni,∗\phi^{i,\*}\_{n}
and forward wniw\_{n}^{i} discrete processes.
Although we can decouple the wealth process by deliberately constructing the model so that ϕni,∗≡0\phi^{i,\*}\_{n}\equiv 0,
the resulting model allows no trading activity in the market and is thus clearly unrealistic.

### Acknowledgements

The author would like to thank M. Sekine for useful discussions related to the earlier works.

## References

* [1]

  Achdou, Y., Han, J., Lasry, J., Lions, P. and Moll, B., Partial differential equation models
  in macroeconomics, Philosophical Transaction of The Royal Society, 2014, A 372:20130397.
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

  Bayraktar, E., Mitra, I., Zhang, J., Countercyclical unemployment benefits: a general equilibrium analysis of transition
  dynamics, Mathematics and Financial Economics, 2024, Vol. 18, pp. 213-232.
* [6]

  Ashrafyan, Y., Bakaryan, T., Gomes, D. and Gutierrez, J., A duality approach to a price formation MFG model,
  Minimax Theory and its Applications, 2023, Vol. 8, pp. 1-36.
* [7]

  Bäuerle, N. and Rieder, U., Markov decision processes with applications to finance,
  Universitext, 2011, Springer-Verlag Berlin.
* [8]

  Black, F., Derman, E. and Toy, W., A one-factor model of interest rates and its applications to treasury bond options,
  Financial Analysts Journal, 1990, pp. 24–32.
* [9]

  Carmona, R. and Delarue, F., Probabilistic analysis of mean-field games, SIAM J. Control. Optim.,
  2013, Vol. 51, No. 4, pp. 2705-2734.
* [10]

  Carmona, R. and Delarue, F., Forward-backward stochastic differential equations and
  controlled McKean-Vlasov dynamics, The Annals of Probability, 2015, Vol. 43, No. 5, pp. 2647-2700.
* [11]

  Carmona, R. and Delarue, F., Probabilistic theory of mean field games with applications I, 2018,
  Springer International Publishing, Switzerland.
* [12]

  Carmona, R. and Delarue, F., Probabilistic theory of mean field games with applications II, 2018,
  Springer International Publishing, Switzerland.
* [13]

  Cox, J.C., Ross, S.A. and Rubinstein, M., Option Pricing: a simplified approach,
  Journal of Financial Economics, 1979, Vol. 7, pp. 229-263.
* [14]

  Derman, E., and Kani, I., Riding on a smile, RISK, 1994, July, no.3, 32-39.
* [15]

  Féron, O., Tankov, P. and Tinsi, L., Price formation and optimal trading in intraday electricity markets,
  Mathematics and Financial Economics, 2022, Vol. 16, pp. 205-237.
* [16]

  Fujii, M., and Takahashi, A., A mean field game approach to equilibrium pricing with market clearing condition,
  SIAM J. Control. Optim. , 2022, Vol. 1, pp. 259-279.
* [17]

  Fujii, M., and Takahashi, A., Strong convergence to the mean-field limit of a finite agent equilibrium,
  SIAM J. Financial Math. , 2022, Vol. 13, No. 2, pp. 459-490.
* [18]

  Fujii, M. and Takahashi, A., Equilibrium price formation with a major player and its mean field limit,
  ESAIM: Control, Optimization and Calculus of Variations, 2022, Vol. 28, 21.
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

  Gabaix, X, Lasry, J.M. , Lions, P.L. and Moll, B.,The dynamics of inequality,
  Econometrica, 2016, Vol. 84, No. 6, 2071-2111.
* [23]

  Gomes, D.A., Gutierrez, J., and Ribeiro, R., A random-supply mean field game price model,
  SIAM J. Financial Math., 2023, Vol. 14, No. 1, pp. 1888-222.
* [24]

  Gomes, D.A. and Saúde, J., A mean-field game approach to price formation,
  Dyn Games Appl, 2020, https://doi.org/10.1007/s13235-020-00348-x.
* [25]

  Hernández-Lerma,O. and Lasserre,J. B. , Discrete-Time Markov Control Processes,
  Springer, 1996, NY.
* [26]

  Hu, Y., Imkeller, P. and Müller, M., Utility maximization in incomplete markets,
  The Annals of Applied Probability, 2005, 15 (3) : 1691-1712.
* [27]

  Huang, M., Malhame, R. and Caines, P.E., Large population stochastic dynamic games:
  closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle, Commun. Inf. Syst., 2006,
  Vol. 6, No. 3, pp.221-252.
* [28]

  Huang, M., Malhame, R. and Caines, P.E., An invariance principle in large population stochastic dynamics games, Jrl Syst Sci & Complexity,
  2007, Vol. 20, pp. 162-172.
* [29]

  Huang, M., Malhame, R. and Caines, P.E., Large-population cost-coupled LQG problems with nonuniform agents:
  individual-mass behavior and decentralized ϵ\epsilon-Nash equilibria, IEEE Transactions on Automatic Control, 2007, Vol. 52, No. 9, pp. 1560-1571.
* [30]

  Karatzas, I. and Shreve, S., Methods of mathematical finance,
  Springer NY, 1998.
* [31]

  Klenke, A., Probability Theorey: A comprehensive course, Third Edition, 2020, Springer Switzerland.
* [32]

  Kobylanski, A., Backward stochastic differential equations and partial differential equations with quadratic growth,
  The Annals of Probability, 2000, Vol. 28, pp. 558-602.
* [33]

  Lasry, J. M. and Lions, P.L., Jeux a champ moyen I. Le cas stationnaire, C. R. Sci. Math. Acad. Paris, 2006,
  343 pp. 619-625.
* [34]

  Lasry, J. M. and Lions, P.L., Jeux a champ moyen II. Horizon fini et controle optimal,
  C. R. Sci. Math. Acad. Paris, 2006, 343, pp. 679-684.
* [35]

  Lasry, J.M. and Lions, P.L., Mean field games, Jpn. J. Math., 2007, Vol. 2, pp. 229-260.
* [36]

  Sarto, G.D., Leocata, M. and Livieri, G., A mean field game approach for pollution regulation of competitive firms,
  2024, preprint, arXiv:2407.1275.
* [37]

  Sekine, M., Mean field equilibrium asset pricing model under partial observation: An exponential quadratic Gaussian approach,
  Japan Journal of Industrial and Applied Mathematics, 2025, No. 42, pp. 853-878.
* [38]

  Sharpe, W.F., 1978, Investments (Prentice-Hall, Englewood Chffs, NJ)
* [39]

  Shrivats, A., Firoozi, D. and Jaimungal, S., A mean-field game approach to equilibrium pricing,
  optimal generation, and trading in solar renewable energy certificate markets,
  Mathematical Finance, 2020, Vol. 32, Issue 3, pp. 779-824.