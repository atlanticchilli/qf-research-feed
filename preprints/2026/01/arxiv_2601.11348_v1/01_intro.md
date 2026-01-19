---
authors:
- Hansjoerg Albrecher
- Nora Muler
doc_id: arxiv:2601.11348v1
family_id: arxiv:2601.11348
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero
  Target
url_abs: http://arxiv.org/abs/2601.11348v1
url_html: https://arxiv.org/html/2601.11348v1
venue: arXiv q-fin
version: 1
year: 2026
---


Hansjörg Albrecher
Department of Actuarial Science, Faculty of
Business and Economics and Swiss
Finance Institute and Expertise Center for Climate Extremes, University of Lausanne, CH-1015 Lausanne. Email: hansjoerg.albrecher@unil.ch
  
Nora Muler
Departamento de Matematicas, Universidad
Torcuato Di Tella. Av. Figueroa Alcorta 7350 (C1428BIJ) Ciudad de Buenos
Aires, Argentina. Email: nmuler@utdt.edu

###### Abstract

> Achieving net-zero carbon emissions requires a transformation of energy systems, industrial processes, and consumption patterns. In particular, a transition towards that goal involves a gradual reduction of excess carbon emissions that are not essential for the well-functioning of society. In this paper we study this problem from a stochastic control perspective to identify the optimal gradual reduction of the emission rate, when an allocated excess carbon budget is used up over time. Assuming that updates of the available carbon budget follow a diffusion process, we identify the emission strategy that maximizes expected discounted emissions under the constraint of a non-increasing emission rate, with an additional term rewarding the amount of time for which the budget is not yet depleted. We establish a link of this topic to optimal dividend problems in insurance
> risk theory under ratcheting constraints and show that the value function is the unique viscosity solution of the associated Hamilton-Jacobi-Bellman equation. We provide numerical illustrations of the resulting optimal abatement schedule of emissions and a quantitative evaluation of the effect of the non-increasing rate constraint on the value function.

## 1 Introduction

Motivated by the Paris Agreement adopted within the United Nations Framework Convention on Climate Change (UNFCCC), whose objective is to curb global anthropogenic greenhouse gas (GHG) emissions (see, for example, Popovski [[24](https://arxiv.org/html/2601.11348v1#bib.bib24)]), many governments have recently announced commitments to reach net-zero carbon emissions by specified target dates.111Like many other authors, for simplicity we refer to GHG emissions as carbon emissions in this paper, as carbon dioxide and methane correspond to more than 90% of the GHG emissions. Such a goal can only be achieved by substantially reducing avoidable emissions and compensating for those that are unavoidable. Naturally, these reductions are difficult to realize in light of established consumption patterns and the significant inertia associated with behavioral change. This applies equally to individuals, firms, and society as a whole, and the political dimension of this question is at this point mainly on plans and rules for companies, and possibly the exertion of implicit and explicit pressure from governments through respective directives and laws.
  
This topic can be examined from multiple perspectives, see for instance Borissov and Bretschger [[12](https://arxiv.org/html/2601.11348v1#bib.bib12)] for an economic viewpoint on fair contributions across countries with heterogeneous wealth and pollution intensity level. Once a carbon emission target is set on a country level, its implementation as a tradeoff between emission trading and actual emission abatement is a non-trivial task, see for instance Aïd and Biagini [[1](https://arxiv.org/html/2601.11348v1#bib.bib1), [2](https://arxiv.org/html/2601.11348v1#bib.bib2)] and Biagini [[11](https://arxiv.org/html/2601.11348v1#bib.bib11)] for the study of this as a stochastic Stackelberg game between firms and the regulator, cf. also Wijk [[28](https://arxiv.org/html/2601.11348v1#bib.bib28)]. For an analysis and tracking of the transition path of an individual company towards a net-zero target, see for instance Chekriy et al. [[14](https://arxiv.org/html/2601.11348v1#bib.bib14)] and Saleh et al. [[26](https://arxiv.org/html/2601.11348v1#bib.bib26)]. Huang et al. [[21](https://arxiv.org/html/2601.11348v1#bib.bib21)] examine a stochastic control problem for carbon emission reduction and the purchase amount of carbon allowances as a bivariate control problem, see also Chen et al. [[15](https://arxiv.org/html/2601.11348v1#bib.bib15)].

For a profit-maximizing company the tradeoff between paying carbon taxes and investing into technologies to reduce carbon emissions can lead to an interesting stochastic control problem, see Colaneri et al. [[16](https://arxiv.org/html/2601.11348v1#bib.bib16)]. Bourgey et al. [[13](https://arxiv.org/html/2601.11348v1#bib.bib13)] study another dynamic control problem of maximizing profit (which is increasing with the intensity of carbon emission) when at the same time facing penalties as a function of the discrepancy between the actual emission rate and a target emission rate that reduces according to a given socio-economic pathway (SSP).

In many situations, it makes sense to assume that for reaching a net-zero target over time, one decides to compensate inevitable carbon emissions through the purchase of carbon allowances or other compensation mechanisms (like investing into carbon sequestration etc.), and then is left with a budget for (a priori) avoidable
excess emissions that can be used up until the time at which the net-zero goal should be achieved (or is politically enforced). These excess emissions could be linked to profit when considering a company, or may serve some personal utility if one has an individual in mind. The question is then the schedule according to which this excess emission budget shall optimally be consumed, and a profound understanding of such patterns could be helpful to develop appropriate incentives for successfully reaching net-zero goals. Such a budget may itself be subject to uncertainty over time (increases to due to technology advances in carbon capture facilities, decreases due to stronger political pressure etc., or simply noise), and it may be useful to model the available excess carbon emission budget as a stochastic process, for simplicity in terms of a diffusion process. Albrecher and Zhu [[6](https://arxiv.org/html/2601.11348v1#bib.bib6)] recently studied such a problem with techniques from stochastic control theory. Concretely, they looked at the problem of when and at which rates to optimally use up an available (excess) carbon budget, if one assigns value to the carbon emissions according to a linear utility function and expresses a preference for earlier emission by using a constant discount rate. Once the budget is depleted, there will be no future excess emissions. The availability of some carbon budget at future times is rewarded by a constant term Λ\Lambda that is also subject to the same discounting and is added to the value function whenever the process is not yet depleted. Hence, Λ\Lambda can be considered to represent a certain sustainability component in the optimization, or also a desire to leave some excess carbon emission for later (or even for future generations); see e.g. Korn [[22](https://arxiv.org/html/2601.11348v1#bib.bib22)], Korn and Nurkanovic [[23](https://arxiv.org/html/2601.11348v1#bib.bib23)] for other proposals to incorporate sustainability aspects in profitability considerations. In [[6](https://arxiv.org/html/2601.11348v1#bib.bib6)], the carbon budget was assumed to follow a diffusion process. For that situation, the optimal emission strategy was identified as a barrier strategy, with maximally allowed emission rate as soon as the available carbon budget exceeds the barrier, and no emissions below that barrier. The emphasis was then on effects of present-bias (linked to subjective discount rates) on respective emission decisions, and the corresponding efficiency of carbon taxation towards the net-zero target.

In the present paper we would like to take a different angle on identifying optimal excess carbon emission schedules. Even if a barrier strategy is optimal for maximizing the expected discounted excess emissions until depletion with a Λ\Lambda-reward on keeping the budget positive, its implementation results in a lot of variability in consumption patterns, as there is no emission below the barrier and maximally allowed emission above it. It may be easier (both psychologically and practically) to implement incentives or requirements that foresee a gradual reduction of the excess carbon emission of the entity (individuals, companies or the society at large) until the excess emission budget is used up. It is therefore of interest to consider the optimal emission problem with the constraint that emission rates can only decrease, and the challenge is then to find the strategy that optimizes emissions according to the above objective under this abatement constraint. In particular, it is desirable to quantify the efficiency loss which this constraint entails. From a methodological perspective, there is a certain degree of similarity of the present stochastic control problem with identifying optimal dividend payout strategies from an insurance portfolio in classical risk theory, when the goal is to maximize expected discounted dividends until ruin (see e.g. [[10](https://arxiv.org/html/2601.11348v1#bib.bib10)]). For this latter problem, in Albrecher et al. [[3](https://arxiv.org/html/2601.11348v1#bib.bib3), [4](https://arxiv.org/html/2601.11348v1#bib.bib4)] a ratcheting constraint was considered, where dividend rates can never be decreased. The setup of the present paper refers to the situation where such dividend rates (excess emission rates in the present context) can, in contrast, never be increased (which we also occasionally will refer to as ’down-ratcheting’ in the sequel). Certain parts of the proofs of our results correspondingly benefit from similarities to proofs that were developed in [[4](https://arxiv.org/html/2601.11348v1#bib.bib4)].

We define a performance criterion that accounts for expected
cumulative discounted excess emissions, together with a constant reward Λ\Lambda for
safeguarding unused carbon emission capacity, until the time of depletion of that excess carbon budget (the time when the
controlled surplus first becomes negative). The objective is to determine the
optimal excess emission strategy that maximizes this function under the down-ratcheting constraint, which we achieve by identifying the optimal strategy to be of threshold type for a discretized version of the problem and then showing uniform convergence of the discrete problem to the continuous one. This results into an optimal excess emission abatement schedule (or emission abatement curve), according to which emissions are permanently reduced to a lower level whenever new record lows of the still available carbon budget have been reached, until the (excess) emissions are reduced to zero. We also illustrate the approach for a few concrete numerical examples with positive, zero and negative drift of the carbon (excess) emission surplus process, and compare the optimal emission strategy to the one without the abatement constraint as well as to the situation where one simply applies a linear reduction of the excess emission rate over time. The latter helps to see the degree of performance increase that is possible through the application of the optimal excess emission abatement schedule.

The remainder of the paper is organized as follows. Section 2 introduces the
model and the detailed formulation of the problem. It also provides some first
basic results on properties of the value function under consideration. Section
3 derives the Hamilton-Jacobi-Bellman (HJB) equation and shows that the value function is a viscosity solution of the HJB equation, together with a verification theorem. In Section 4 we formulate the problem on a discrete set of admissible emission rates and in Section 5 we prove
that the value function of the problem for discrete sets convergences
to the one for a continuum of admissible emission rates as the mesh size of
the finite set tends to zero. The latter paves the way for establishing optimal solutions numerically in an efficient way. In Section 6 we show that for finitely many
admissible emission rates, there exists an optimal strategy for which the
change and non-change regions have only one connected component (this
corresponds to the extension of one-dimensional threshold strategies to the
two-dimensional case). We also provide an implicit equation defining the
optimal threshold function for this case. Section 7 then contains numerical
illustrations of the optimal strategy and comparisons to the unconstrained case as well as to the simpler strategy of linearly reducing emission rates over time. Section 8 concludes and identifies some future research directions of interest. Some technical proofs are delegated to an appendix.

## 2 Model and basic results

Assume that the (excess) carbon emission budget of an entity (a country, a company or even an individual person) available at time tt is modeled by a Brownian motion with drift:

|  |  |  |
| --- | --- | --- |
|  | Xt=x+μ​t+σ​Wt,X\_{t}=x+\mu t+\sigma W\_{t}, |  |

where WtW\_{t} is a standard Brownian motion, and σ>0,μ∈ℝ\sigma>0,\,\mu\in{\mathbb{R}} are given
constants.222As described above, XtX\_{t} refers to excess emissions that are a priori avoidable, so in the sequel the term ’emissions’ will always refer to these ’excess emissions’. The unit of XtX\_{t} could for e.g. be tCO2. Realistic parameter values for μ,σ\mu,\sigma and xx vary with the entity being considered. The entity uses this budget XtX\_{t} to emit carbon at rates
chosen from a set S⊂[0,c¯]S\subset[0,\overline{c}] , where c¯≥0\overline{c}\geq 0
is the maximum allowable emission rate.

Let (Ω,ℱ,(ℱt)t≥0,𝒫)(\Omega,\mathcal{F},\left(\mathcal{F}\_{t}\right)\_{t\geq 0},\mathcal{P}) be the complete probability space generated by the process
(Xt)t≥0(X\_{t})\_{t\geq 0}, and let CtC\_{t} denote the carbon emission rate at time tt. In this paper, we want to only consider emission patterns where the emission rate can not be increased beyond its current level anymore.
Given an initial budget X0=xX\_{0}=x
and an initial emission rate c∈Sc\in S at t=0t=0 (which typically will be equal to c¯\overline{c}), an admissible strategy is therefore a
process C=(Ct)t≥0C=\left(C\_{t}\right)\_{t\geq 0} that is non-increasing,
right-continuous and adapted to the filtration (ℱt)t≥0\left(\mathcal{F}\_{t}\right)\_{t\geq 0} with Ct∈SC\_{t}\in S for all tt. In other words, the
country is only allowed to reduce or maintain its emission rate over time, so admissible emission strategies are all of the ratcheting-down type. Under a given
strategy CC, the controlled carbon emission surplus process can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | XtC=Xt−∫0tCs​𝑑s.X\_{t}^{C}=X\_{t}-\int\_{0}^{t}C\_{s}ds. |  | (2.1) |

Define Πx,cS\Pi\_{x,c}^{S} as the set of all admissible ratcheting-down strategies with initial surplus x≥0x\geq 0 and initial emission
rate c∈Sc\in S. Given C∈Πx,cSC\in\Pi\_{x,c}^{S}, the value function of this
strategy that we consider in this paper includes a reward for not having exhausted the remaining budget too early and is given by

|  |  |  |
| --- | --- | --- |
|  | J​(x;C)=𝔼​[∫0τe−q​s​(Cs+Λ)​𝑑s],J(x;C)=\mathbb{E}\left[\int\_{0}^{\tau}e^{-qs}(C\_{s}+\Lambda)ds\right], |  |

where q>0q>0 is the discount factor, Λ>0\Lambda>0 is a fixed reward parameter. The quantity τ=inf{t≥0:XtC<0}\tau=\inf\left\{t\geq 0:X\_{t}^{C}<0\right\} is the depletion time,
i.e., the first time the controlled surplus becomes negative. Hence, for any
initial surplus x≥0x\geq 0 and initial emission rate cc, our aim is to maximize

|  |  |  |  |
| --- | --- | --- | --- |
|  | VS​(x,c)=supC∈Πx,cSJ​(x;C),V^{S}(x,c)=\sup\_{C\in\Pi\_{x,c}^{S}}J(x;C), |  | (2.2) |

which defines the optimal value function for initial surplus xx and initial emission rate cc.

From the Brownian motion assumption, it is immediate that VS​(0,c)=0V^{S}(0,c)=0 for all c∈Sc\in S, reflecting the
fact that no emissions can be sustained once the surplus is depleted.

###### Remark 2.1

Our optimal value function can be
interpreted as the one of an optimal dividend problem that accounts for the time of ruin
under bounded dividend rates, but incorporates a ratcheting-down strategy.
While such a restriction is not necessarily of immediate relevance in the traditional dividend context,
the formulation enables an interesting comparison with the classical problem of
maximizing bounded dividends until ruin, while rewarding a later time of ruin (cf. Thonhauser and Albrecher [[27](https://arxiv.org/html/2601.11348v1#bib.bib27)]). That latter problem is one-dimensional;
let us denote its value function for the same parameters μ,σ\mu,\sigma and Λ\Lambda by VD​(x)V\_{D}(x). We have that VS​(x,c)≤VD​(x)V^{S}(x,c)\leq V\_{D}(x) for all x≥0x\geq 0 and c∈S⊂[0,c¯]c\in S\subset[0,\overline{c}]. The
function VDV\_{D} is increasing, concave, twice continuously differentiable
with VD​(0)=0V\_{D}(0)=0, limx→∞VD​(x)=(c¯+Λ)/q\lim\_{x\rightarrow\infty}V\_{D}(x)=(\overline{c}+\Lambda)/q and VD′​(x)≤VD′​(0)V\_{D}^{\prime}(x)\leq V\_{D}^{\prime}(0) for all x≥0x\geq 0. ⋄\diamond

###### Remark 2.2

Our optimal stochastic control problem
is also related to the classical dividend optimization problem with a
ratcheting-up constraint in insurance surplus models (see Albrecher et al. [[4](https://arxiv.org/html/2601.11348v1#bib.bib4)] and Guan & Xu [[20](https://arxiv.org/html/2601.11348v1#bib.bib20)]). However, in contrast to these works, we consider here a ratcheting-down constraint and incorporate the reward term
Λ\Lambda. ⋄\diamond

We next establish a basic result concerning the boundedness and monotonicity
properties of the optimal value function.

###### Proposition 2.1

The optimal value function VS​(x,c)V^{S}(x,c)
is bounded above by (c¯+Λ)/q(\overline{c}+\Lambda)/q, and it is non-decreasing in
both the surplus xx and the emission rate c.c.

Proof. Since

|  |  |  |
| --- | --- | --- |
|  | VS​(x,c)≤VD​(x)≤c¯+Λq,V^{S}(x,c)\leq V\_{D}(x)\leq\frac{\overline{c}+\Lambda}{q}, |  |

we have the boundedness result.

To show monotonicity in cc, note that if c1<c2c\_{1}<c\_{2} then Πx,c1S⊂Πx,c2S\Pi\_{x,c\_{1}}^{S}\subset\Pi\_{x,c\_{2}}^{S} for any x≥0x\geq 0 and so VS​(x,c1)≤VS​(x,c2)V^{S}(x,c\_{1})\leq V^{S}(x,c\_{2}).

For monotonicity in xx, consider 0≤x1<x20\leq x\_{1}<x\_{2} and an admissible
ratcheting-down strategy C1∈Πx1,cSC^{1}\in\Pi\_{x\_{1},c}^{S} for any c∈Sc\in S, and let us
define C2∈Πx2,cSC^{2}\in\Pi\_{x\_{2},c}^{S} as Ct2=Ct1C\_{t}^{2}=C\_{t}^{1} until the
exhaustion time of the controlled process XtC1X\_{t}^{C^{1}}, and then setting
Ct2=0C\_{t}^{2}=0 (i.e. no emissions) afterwards. Clearly, J​(x;C1)≤J​(x;C2)J(x;C\_{1})\leq J(x;C\_{2}) and so VS​(x1,c)≤VS​(x2,c)V^{S}(x\_{1},c)\leq V^{S}(x\_{2},c). ■\blacksquare

The following proposition provides a global Lipschitz estimate for the optimal
value function. The proof is identical to the one of Proposition 2.2 in [[4](https://arxiv.org/html/2601.11348v1#bib.bib4)], with the obvious adaptations for the factor Λ\Lambda.

###### Proposition 2.2

There exists a constant K>0K>0 such
that

|  |  |  |
| --- | --- | --- |
|  | 0≤VS​(x2,c1)−VS​(x1,c2)≤K​[(x2−x1)+(c2−c1)]0\leq V^{S}(x\_{2},c\_{1})-V^{S}(x\_{1},c\_{2})\leq K\left[\left(x\_{2}-x\_{1}\right)+\left(c\_{2}-c\_{1}\right)\right] |  |

for all 0≤x1≤x20\leq x\_{1}\leq x\_{2} and c1,c2∈Sc\_{1},c\_{2}\in S with c1≤c2.c\_{1}\leq c\_{2}.

Finally, we state the Dynamic Programming Principle (DPP), its proof is
similar to the one of Lemma 1.2 in Azcue and Muler [[9](https://arxiv.org/html/2601.11348v1#bib.bib9)].

###### Lemma 2.3

Given any stopping time τ~\widetilde{\tau}, we can write

|  |  |  |
| --- | --- | --- |
|  | VS​(x,c)=supC∈Πx,cS𝔼​[∫0τ∧τ~e−q​s​(Cs+Λ)​𝑑s+e−q​(τ∧τ~)​VS​(Xτ∧τ~C,Cτ∧τ~)]​.V^{S}(x,c)=\sup\limits\_{C\in\Pi\_{x,c}^{S}}\mathbb{E}\left[\int\_{0}^{\tau\wedge\widetilde{\tau}}e^{-qs}(C\_{s}+\Lambda)ds+e^{-q(\tau\wedge\widetilde{\tau})}V^{S}(X\_{\tau\wedge\widetilde{\tau}}^{C},C\_{\tau\wedge\widetilde{\tau}})\right]\text{.} |  |

## 3 Hamilton-Jacobi-Bellman equations

In this section, we introduce the HJB equation
associated with the ratcheting-down emission control problem where
the set of possible emission rates is S:=[0,c¯]⊂[0,∞)S:=[0,\overline{c}]\subset[0,\infty) with c¯>0\overline{c}>0. We show that the optimal value function V,V,
defined in ([2.2](https://arxiv.org/html/2601.11348v1#S2.E2 "In 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), is the unique viscosity solution of
the corresponding HJB equation with boundary condition (c¯+Λ)/q(\overline{c}+\Lambda)/q when xx goes to infinity.

Consider the strategy that emits at a constant rate cc until the carbon budget is exhausted. The corresponding value function Wc​(x)W^{c}(x) is the
unique solution of the second-order differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒc​(W):=σ22​∂x​xW+(μ−c)​∂xW−q​W+c+Λ=0\mathcal{L}^{c}(W):=\frac{\sigma^{2}}{2}\partial\_{xx}W+(\mu-c)\partial\_{x}W-qW+c+\Lambda=0 |  | (3.1) |

with boundary conditions Wc​(0)=0W^{c}(0)=0 and limx→∞\lim\_{x\rightarrow\infty}
Wc​(x)=(c+Λ)/q.W^{c}(x)=(c+\Lambda)/q. The general solutions ℒc​(W)=0\mathcal{L}^{c}(W)=0 are of
the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | c+Λq+a1​eθ1​(c)​x+a2​eθ2​(c)​x​ with ​a1,a2∈ℝ,\frac{c+\Lambda}{q}+a\_{1}e^{\theta\_{1}(c)x}+a\_{2}e^{\theta\_{2}(c)x}\text{ with }a\_{1},a\_{2}\in{\mathbb{R}}, |  | (3.2) |

where θ1​(c)<0<θ2​(c)\theta\_{1}(c)<0<\theta\_{2}(c) are the roots of the characteristic
equation:

|  |  |  |
| --- | --- | --- |
|  | σ22​z2+(μ−c)​z−q=0\frac{\sigma^{2}}{2}z^{2}+(\mu-c)z-q=0 |  |

associated to the operator ℒc\mathcal{L}^{c}, and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ1​(c):=c−μ−(c−μ)2+2​q​σ2σ2,θ2​(c):=c−μ+(c−μ)2+2​q​σ2σ2.\theta\_{1}(c):=\frac{c-\mu-\sqrt{(c-\mu)^{2}+2q\sigma^{2}}}{\sigma^{2}},\quad\theta\_{2}(c):=\text{$\frac{c-\mu+\sqrt{(c-\mu)^{2}+2q\sigma^{2}}}{\sigma^{2}}$.} |  | (3.3) |

Since the value function must remain bounded we can discard the exponentially
growing term and the bounded solutions can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | c+Λq+a​eθ1​(c)​x​with ​a∈ℝ.\frac{c+\Lambda}{q}+ae^{\theta\_{1}(c)x}\ \text{with }a\in{\mathbb{R}}. |  | (3.4) |

From the boundary conditions, we then get

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wc​(x)=c+Λq​(1−eθ1​(c)​x).W^{c}(x)=\frac{c+\Lambda}{q}\left(1-e^{\theta\_{1}(c)x}\right). |  | (3.5) |

It
follows that Wc​(x)W^{c}(x) is increasing and concave.

###### Remark 3.1

Given a set S:=[0,c¯]⊂[0,∞)S:=[0,\overline{c}]\subset[0,\infty) , we have that

|  |  |  |
| --- | --- | --- |
|  | c¯+Λq≥VS​(x,c)≥Wc¯​(x)=V{c¯}​(x,c¯)=c¯+Λq​(1−eθ1​(c¯)​x)\frac{\overline{c}+\Lambda}{q}\geq V^{S}(x,c)\geq W^{\overline{c}}(x)=V^{\left\{\overline{c}\right\}}(x,\overline{c})=\frac{\overline{c}+\Lambda}{q}\left(1-e^{\theta\_{1}(\overline{c})x}\right) |  |

and, consequently, limx→∞VS​(x,c)=(c¯+Λ)/q\lim\_{x\rightarrow\infty}V^{S}(x,c)=(\overline{c}+\Lambda)/{q} for any c∈Sc\in S. ⋄\diamond

We now consider the general case where the admissible emission set is S=[0,c¯]S=[0,\overline{c}] for some c¯>0.\overline{c}>0. The HJB equation associated to
([2.2](https://arxiv.org/html/2601.11348v1#S2.E2 "In 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒc​(u)​(x,c),−∂cu​(x,c)}=0​ for ​x≥0​and ​0≤c≤c¯​,\max\{\mathcal{L}^{c}(u)(x,c),-\partial\_{c}u(x,c)\}=0\text{ for }x\geq 0\ \text{and }0\leq c\leq\overline{c}\text{,} |  | (3.6) |

where ℒc\mathcal{L}^{c} is defined in ([3.1](https://arxiv.org/html/2601.11348v1#S3.E1 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")).

We say that a function f:[0,∞)×[0,c¯)→ℝf:[0,\infty)\times[0,\overline{c})\rightarrow{\mathbb{R}} is (2,1)-differentiable if ff is continuously
differentiable and ∂xf​(⋅,c)\partial\_{x}f(\cdot,c) is continuously differentiable for
each c∈[0,c¯)c\in[0,\overline{c}). To solve the HJB equation, we work in the
framework of viscosity solutions.

###### Definition 3.1

(a) A locally Lipschitz function u¯:[0,∞)×[0,c¯]→ℝ\overline{u}:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}} is a viscosity supersolution of
([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c)∈(0,∞)×[0,c¯)(x,c)\in(0,\infty)\times[0,\overline{c}) if
any (2,1)-differentiable function φ:[0,∞)×[0,c¯]→ℝ\varphi:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}}\ with φ​(x,c)=u¯​(x,c)\varphi(x,c)=\overline{u}(x,c),
and such that u¯−φ\overline{u}-\varphi reaches the minimum at (x,c)\left(x,c\right), satisfies

|  |  |  |
| --- | --- | --- |
|  | max⁡{ℒc​(φ)​(x,c),−∂cφ​(x,c)}≤0.\max\left\{\mathcal{L}^{c}(\varphi)(x,c),-\partial\_{c}\varphi(x,c)\right\}\leq 0.\ |  |

The function φ\varphi is called a test function for supersolution at
(x,c)(x,c).

(b) A locally Lipschitz function u¯:\underline{u}: [0,∞)×[0,c¯]→ℝ[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}}\  is a viscosity subsolution
of ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c)∈(0,∞)×[0,c¯)(x,c)\in(0,\infty)\times[0,\overline{c}) if any (2,1)-differentiable function ψ:[0,∞)×[0,c¯]→ℝ\psi:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}}\ with ψ​(x,c)=u¯​(x,c)\psi(x,c)=\underline{u}(x,c), and such that u¯−ψ\underline{u}-\psi reaches the maximum at (x,c)\left(x,c\right), satisfies

|  |  |  |
| --- | --- | --- |
|  | max⁡{ℒc​(ψ)​(x,c),−∂cψ​(x,c)}≥0​.\max\left\{\mathcal{L}^{c}(\psi)(x,c),-\partial\_{c}\psi(x,c)\right\}\geq 0\text{.} |  |

The function ψ\psi is called a test function for subsolution at
(x,c)(x,c).

(c) A function u:[0,∞)×[0,c¯]→ℝu:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}} which is both a supersolution and subsolution at (x,c)∈[0,∞)×[0,c¯)(x,c)\in[0,\infty)\times[0,\overline{c}) is called a viscosity solution
of ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c)(x,c).

###### Remark 3.2

In order to simplify the notation, we define
V​(x,c):=VS​(x,c)V(x,c):=V^{S}(x,c). Because of the ratcheting-down constraint on the
emission rate, we have VS​(x,c)=V[0,c]​(x,c).V^{S}(x,c)=V^{[0,c]}(x,c). ⋄\diamond

We first prove that VV is a viscosity solution of the corresponding HJB
equation. The proof is in the appendix.

###### Proposition 3.1

VV is a viscosity solution of
([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) in (0,∞)×[0,c¯](0,\infty)\times[0,\overline{c}].

When c=0c=0, the ratcheting-down constraint implies that the emissions are stopped.
Hence, V​(x,0)V(x,0) corresponds to the value function of the strategy that does
not emit, with initial surplus xx. So, by ([3.5](https://arxiv.org/html/2601.11348v1#S3.E5 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x,0)=V{0}​(x,0)=Λq​(1−eθ1​(0)​x)=Λq​(1−e(−μ−μ2+2​q​σ2)​x/σ2).V(x,0)=V^{\{0\}}(x,0)=\frac{\Lambda}{q}\left(1-e^{\theta\_{1}(0)x}\right)=\frac{\Lambda}{q}\left(1-e^{(-\mu-\sqrt{\mu^{2}+2q\sigma^{2}})x/\sigma^{2}}\right). |  | (3.7) |

Let us now state the comparison result for viscosity solutions. The proof is
in the appendix.

###### Lemma 3.2

Assume that (i) u¯\underline{u} is a viscosity
subsolution and u¯\overline{u} is a viscosity supersolution of the HJB
equation ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) for all x>0x>0 and for all c∈[0,c¯]c\in[0,\overline{c}] (ii) u¯\underline{u} and u¯\overline{u} are non-decreasing in
the variable xx and in the variable cc, (iii) u¯​(0,c)=u¯​(0,c)=0\underline{u}(0,c)=\overline{u}(0,c)=0 for
c∈[0,c¯]c\in[0,\overline{c}], limx→∞u¯​(x,c)≤(c¯+Λ)/q≤limx→∞u¯​(x,c)\lim\_{x\rightarrow\infty}\underline{u}(x,c)\leq(\overline{c}+\Lambda)/q\leq\lim\_{x\rightarrow\infty}\overline{u}(x,c) and (iv) u¯​(x,0)≤u¯​(x,0)\underline{u}(x,0)\leq\overline{u}(x,0) for x≥0x\geq 0.
Then u¯≤u¯\underline{u}\leq\overline{u} in [0,∞)×[0,c¯).[0,\infty)\times[0,\overline{c}).

The following characterization theorem is a direct consequence of the previous
lemma, Remark [3.1](https://arxiv.org/html/2601.11348v1#S3.Thmremark1 "Remark 3.1 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") and Proposition [3.1](https://arxiv.org/html/2601.11348v1#theorem1a "Proposition 3.1 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target").

###### Theorem 3.3

The optimal value function VV is the unique
function non-decreasing in xx that is a viscosity solution of
([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) in (0,∞)×[0,c¯)(0,\infty)\times[0,\overline{c}) satisfying
V​(0,c)=0V(0,c)=0 and limx→∞\lim\_{x\rightarrow\infty} V​(x,c)=(c+Λ)/qV(x,c)=(c+\Lambda)/q for
c∈[0,c¯).c\in[0,\overline{c}).

The following proposition establishes conditions under which the current emission level is not lowered anymore, regardless the surplus level.

###### Proposition 3.4

If Λ≤μ2+2​q​σ2\Lambda\leq\sqrt{\mu^{2}+2q\sigma^{2}} and
Λ+μ>0\Lambda+\mu>0, then the optimal threshold is zero for all c∈[0,μ2+2​q​σ2−Λ22​(Λ+μ)]c\in[0,\frac{\mu^{2}+2q\sigma^{2}-\Lambda^{2}}{2(\Lambda+\mu)}] . If
Λ+μ≤0\Lambda+\mu\leq 0 , then the optimal threshold is equal to zero for all
c≥0c\geq 0.

Proof. Consider the value function corresponding to constant
emissions

|  |  |  |
| --- | --- | --- |
|  | u​(x,c)=Wc​(x)=c+Λq​(1−eθ1​(c)​x),u(x,c)=W^{c}(x)=\frac{c+\Lambda}{q}\left(1-e^{\theta\_{1}(c)x}\right), |  |

and substitute this function into the HJB equation ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")). Since
ℒc​(u)​(x,c)=0\mathcal{L}^{c}(u)(x,c)=0, in order for u​(x,c)u(x,c) to be a solution of ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), we must have ∂cu​(x,c)≥0\partial\_{c}u(x,c)\geq 0. A direct
computation yields

|  |  |  |
| --- | --- | --- |
|  | q​∂cu​(x,c)=1−eθ1​(c)​x​(1−θ1​(c)​c+Λ(c−μ)2+2​q​σ2​x).q\,\partial\_{c}u(x,c)=1-e^{\theta\_{1}(c)x}\left(1-\theta\_{1}(c)\frac{c+\Lambda}{\sqrt{(c-\mu)^{2}+2q\sigma^{2}}}\,x\right). |  |

To study the sign of this expression, consider

|  |  |  |
| --- | --- | --- |
|  | q​∂c​xu​(x,c)=−θ1​(c)​eθ1​(c)​x​(1−c+Λ(c−μ)2+2​q​σ2​(1+θ1​(c)​x)).q\,\partial\_{cx}u(x,c)=-\theta\_{1}(c)e^{\theta\_{1}(c)x}\left(1-\frac{c+\Lambda}{\sqrt{(c-\mu)^{2}+2q\sigma^{2}}}\left(1+\theta\_{1}(c)x\right)\right). |  |

Since θ1​(c)<0\theta\_{1}(c)<0 and c+Λ≥0c+\Lambda\geq 0, we have ∂c​xu​(x,c)≥0\partial\_{cx}u(x,c)\geq 0 if and only if

|  |  |  |
| --- | --- | --- |
|  | c+Λ(c−μ)2+2​q​σ2​(1+θ1​(c)​x)≤1.\frac{c+\Lambda}{\sqrt{(c-\mu)^{2}+2q\sigma^{2}}}\left(1+\theta\_{1}(c)x\right)\leq 1. |  |

The inequality holds for all x≥0x\geq 0 if and only if

|  |  |  |
| --- | --- | --- |
|  | c+Λ≤(c−μ)2+2​q​σ2,c+\Lambda\leq\sqrt{(c-\mu)^{2}+2q\sigma^{2}}, |  |

which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 2​c​(Λ+μ)+Λ2≤2​q​σ2+μ2.2c\left(\Lambda+\mu\right)+\Lambda^{2}\leq 2q\sigma^{2}+\mu^{2}. |  |

Assume first that Λ+μ>0\Lambda+\mu>0. Then the above inequality holds if and only
if

|  |  |  |
| --- | --- | --- |
|  | 0≤c≤2​q​σ2+μ2−Λ22​(Λ+μ).0\leq c\leq\frac{2q\sigma^{2}+\mu^{2}-\Lambda^{2}}{2\left(\Lambda+\mu\right)}\,. |  |

In particular, we need 2​q​σ2+μ2−Λ2≥02q\sigma^{2}+\mu^{2}-\Lambda^{2}\geq 0, that is
Λ≤μ2+2​q​σ2\Lambda\leq\sqrt{\mu^{2}+2q\sigma^{2}} in which case the optimal threshold
is identically zero. If instead μ+Λ≤0\mu+\Lambda\leq 0 (and hence μ2≥Λ2\mu^{2}\geq\Lambda^{2}), then

|  |  |  |
| --- | --- | --- |
|  | 2​c​(Λ+μ)≤0<2​q​σ2+μ2−Λ2.2c\left(\Lambda+\mu\right)\leq 0<2q\sigma^{2}+\mu^{2}-\Lambda^{2}. |  |

So the inequality holds for all c≥0c\geq 0, implying that the optimal threshold
is identically zero. Hence, we have the result. ■\blacksquare

###### Remark 3.3

The optimal threshold being zero for a certain cc means that one will
continue to emit at that rate cc until the entire carbon budget is depleted.
From the proof of Proposition [3.4](https://arxiv.org/html/2601.11348v1#theorem4 "Proposition 3.4 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), and assuming uniqueness of the
threshold curve, one observes that there are no open intervals of cc with
zero optimal threshold when c>μ2+2​q​σ2−Λ22​(Λ+μ)c>\frac{\mu^{2}+2q\sigma^{2}-\Lambda^{2}}{2(\Lambda+\mu)} provided that Λ≤μ2+2​q​σ2\Lambda\leq\sqrt{\mu^{2}+2q\sigma^{2}} and
Λ+μ>0\Lambda+\mu>0. Likewise, there are no open intervals with zero optimal
threshold for c>0c>0 when Λ>μ2+2​q​σ2\Lambda>\sqrt{\mu^{2}+2q\sigma^{2}} and
Λ+μ>0\Lambda+\mu>0. If, moreover, the optimal threshold curve is non-decreasing
in cc (as we observe in the numerical examples), this implies that, in case Λ+μ>0\Lambda+\mu>0, the
optimal threshold is strictly positive for c>μ2+2​q​σ2−Λ22​(Λ+μ)c>\frac{\mu^{2}+2q\sigma^{2}-\Lambda^{2}}{2(\Lambda+\mu)} whenever Λ≤μ2+2​q​σ2\Lambda\leq\sqrt{\mu^{2}+2q\sigma^{2}}, and the
optimal threshold is strictly positive for any cc >0>0 whenever Λ>μ2+2​q​σ2\Lambda>\sqrt{\mu^{2}+2q\sigma^{2}}.

In other words, if Λ\Lambda is sufficiently large, then under the optimal abatement strategy the emission rate will reach zero at a positive remaining surplus already. That is, the value of not reducing the carbon budget then exceeds the gain from emitting further. This suggests an interpretation of Λ\Lambda as a sort of sustainability parameter that counterbalances the appetite for immediate carbon budget emissions. The limiting value μ2+2​q​σ2\sqrt{\mu^{2}+2q\sigma^{2}} thus marks the regime in which the sustainability considerations becomes so dominant (relative to emitting) that emissions are halted even when a positive low budget remains. Note that, due to the diffusion properties of the surplus process, the budget may nevertheless be depleted subsequently.

At the same time, these considerations also clarify how the control problem studied in this paper (almost) degenerates when Λ=0\Lambda=0. Since Proposition [3.4](https://arxiv.org/html/2601.11348v1#theorem4 "Proposition 3.4 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") remains applicable in this case, we conclude that if μ≤0\mu\leq 0, the optimal threshold is always zero – so the initial carbon emission rate is never reduced – whereas if μ>0\mu>0, the emission rate is reduced only as long as c>(μ2+2​q​σ2)/(2​μ)c>(\mu^{2}+2q\sigma^{2})/(2\mu). See also Example [7.3](https://arxiv.org/html/2601.11348v1#S7.Thmexample3 "Example 7.3 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") below for an illustration.

⋄\diamond

###### Remark 3.4

Let us consider the limit case where σ=0\sigma=0 and
μ≥0\mu\geq 0. If c∈[0,μ]c\in[0,\mu], then the surplus is never depleted. So,
it is straightforward to verify that the optimal threshold in this case is
zero. Therefore, the corresponding optimal value function, which results from
emitting at the constant rate cc indefinitely, is given by

|  |  |  |
| --- | --- | --- |
|  | V​(x,c)=∫0∞(Λ+c)​e−q​s=(c+Λ)/q.V(x,c)=\int\_{0}^{\infty}(\Lambda+c)e^{-qs}=\left(c+\Lambda\right)/q. |  |

Now, consider the case c>μc>\mu and x>0x>0. An admissible strategy in this
setting is to maintain constant emissions at the maximum admissible level cc
while the surplus is positive, i.e. for 0≤t<0\leq t< T:=x/(c−μ)T:=x/(c-\mu). Once the
surplus hits zero at time TT, the emission rate is reduced to the (maximum possible) level μ≥0\mu\geq 0 which can be sustained indefinitely. The value
function for this strategy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(x,c)\displaystyle W(x,c) | =∫0x/(c−μ)(c+Λ)​e−q​s​𝑑s+e−q​x/(c−μ)​μ+Λq\displaystyle=\int\_{0}^{x/(c-\mu)}\left(c+\Lambda\right)e^{-qs}ds+e^{-qx/(c-\mu)}\frac{\mu+\Lambda}{q} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c+Λq−c−μq​e−q​x/(c−μ).\displaystyle=\frac{c+\Lambda}{q}-\frac{c-\mu}{q}e^{-qx/(c-\mu)}\,. |  |

Due to the discount factor q>0q>0 and the fact that the emission level can
be reduced to c0=μ≥0c\_{0}=\mu\geq 0 at zero surplus (the surplus can then not
become negative unlike in the Brownian setting), it is clear that this is the
optimal strategy and so WW is the optimal value function. We now relate this
result to the HJB framework. While a full proof of the HJB approach is
omitted in this simplified setting, we can infer that the corresponding HJB
equation is

|  |  |  |
| --- | --- | --- |
|  | max⁡{ℒ¯c​(W)​(x,c),−∂cW​(x,c)}=0\max\{\overline{\mathcal{L}}^{c}(W)(x,c),-\partial\_{c}W(x,c)\}=0 |  |

for (x,c)∈[0,∞)×(μ,c¯],(x,c)\in[0,\infty)\times(\mu,\overline{c}], where

|  |  |  |
| --- | --- | --- |
|  | ℒ¯c​(W)​(x,c):=(μ−c)​∂xW​(x,c)−q​W​(x,c)+c+Λ=0.\overline{\mathcal{L}}^{c}(W)(x,c):=(\mu-c)\partial\_{x}W(x,c)-qW(x,c)+c+\Lambda=0. |  |

This corresponds to put σ=0\sigma=0 in ℒc\mathcal{L}^{c} and the boundary
condition W​(0,c)=(μ+Λ)/q>0W(0,c)=\left(\mu+\Lambda\right)/q>0. The latter reflects the fact
that, even at zero surplus, it is possible to emit c=μ≥0c=\mu\geq 0 indefinitely.
WW satisfies the associated first-order HJB equation. To see this, it is
immediate to show that WW is a solution of ℒ¯c​(W)​(x,c)=0\overline{\mathcal{L}}^{c}(W)(x,c)=0. Additionally, differentiating WW with respect to cc
yields

|  |  |  |
| --- | --- | --- |
|  | ∂cW​(x,c)=1q​(1−e−q​x/(c−μ)​(1+q​xc−μ))\partial\_{c}W(x,c)=\frac{1}{q}\left(1-e^{-qx/(c-\mu)}\left(1+\frac{qx}{c-\mu}\right)\right) |  |

for (x,c)∈(μ,c¯]\left(x,c\right)\in(\mu,\overline{c}]. Setting a=q​x/(c−μ)≥0a=qx/(c-\mu)\geq 0, we get the inequality 1≥e−a​(1+a)1\geq e^{-a}\left(1+a\right), which implies
∂cW​(x,c)≥0.\partial\_{c}W(x,c)\geq 0. Hence, the usual verification condition holds. ⋄\diamond

## 4 Hamilton-Jacobi-Bellman equations for finite sets

Let us now restrict to the following finite set of possible emission rates:

|  |  |  |
| --- | --- | --- |
|  | S={c0,c1,c2,….,cn},S=\left\{c\_{0},c\_{1},c\_{2},....,c\_{n}\right\}, |  |

where 0=c0<c1<c2<….<cn=c¯0=c\_{0}<c\_{1}<c\_{2}<....<c\_{n}=\overline{c}. Note that VS​(x,ci)=V{0,c1,….,ci}​(x,ci)V^{S}(x,c\_{i})=V^{\left\{0,c\_{1},....,c\_{i}\right\}}(x,c\_{i}), i.e., it
depends only on the emission rates up to cic\_{i} and does not involve
ci+1,…,cnc\_{i+1},...,c\_{n}. To simplify the notation, we define the optimal value
function within the finite set SS

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vci​(x):=VS​(x,ci),V^{c\_{i}}(x):=V^{S}(x,c\_{i}), |  | (4.1) |

which represents the optimal value function corresponding to initial emission
level cic\_{i}. We then have the following inequalities:

|  |  |  |
| --- | --- | --- |
|  | Vci​(x)≥Vci−1​(x)≥…≥Vc0​(x)≥0,V^{c\_{i}}(x)\geq V^{c\_{i-1}}(x)\geq...\geq V^{c\_{0}}(x)\geq 0, |  |

where

|  |  |  |
| --- | --- | --- |
|  | V0​(x)=V{0}​(x,0)=Λq​(1−eθ1​(0)​x).V^{0}(x)=V^{\{0\}}(x,0)=\frac{\Lambda}{q}\left(1-e^{\theta\_{1}(0)x}\right). |  |

Assuming C2​([0,∞))C^{2}([0,\infty))-regularity for VciV^{c\_{i}}, we can heuristically
derive the HJB equation associated to the discrete optimal
value function ([4.1](https://arxiv.org/html/2601.11348v1#S4.E1 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒci​(v​(x)),Vci−1​(x)−Vci​(x)}=0​ for ​x≥0​ and ​i=1,…,n​,\max\left\{\mathcal{L}^{c\_{i}}(v(x)),V^{c\_{i-1}}(x)-V^{c\_{i}}(x)\right\}=0\text{ for }x\geq 0\text{ and }i=1,...,n\text{,} |  | (4.2) |

with Vci​(0)=0V^{c\_{i}}(0)=0 and limx→∞\lim\_{x\rightarrow\infty} Vci​(x)=(Λ+ci)/qV^{c\_{i}}(x)=(\Lambda+c\_{i})/q. Let us define

|  |  |  |
| --- | --- | --- |
|  | v0=V0=Λq​(1−eθ1​(0)​x)v^{0}=V^{0}=\frac{\Lambda}{q}\left(1-e^{\theta\_{1}(0)x}\right) |  |

and the system of ODE’s

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒci​(vi​(x)),vi−1​(x)−vi​(x)}=0​ for ​x≥0​ and ​i=1,…,n​,\max\left\{\mathcal{L}^{c\_{i}}(v^{i}(x)),v^{i-1}(x)-v^{i}(x)\right\}=0\text{ for }x\geq 0\text{ and }i=1,...,n\text{,} |  | (4.3) |

with vi​(0)=0v^{i}(0)=0 and limx→∞\lim\_{x\rightarrow\infty} vi​(x)=(Λ+ci)/qv^{i}(x)=(\Lambda+c\_{i})/q.

Let us now show that VciV^{c\_{i}} is the unique solution in the viscosity sense
to the ODE system ([4.3](https://arxiv.org/html/2601.11348v1#S4.E3 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")). For this purpose, let
us introduce first the definition of a viscosity solution in the
one-dimensional case.

###### Definition 4.1

(a) A locally Lipschitz function u¯:[0,∞)→ℝ\overline{u}:[0,\infty)\rightarrow{\mathbb{R}} is a viscosity supersolution of
([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at x∈(0,∞)x\in(0,\infty) if any twice continuously
differentiable function φ:[0,∞)→ℝ\varphi:[0,\infty)\rightarrow{\mathbb{R}}\ with
φ​(x)=u¯​(x)\varphi(x)=\overline{u}(x), such that u¯−φ\overline{u}-\varphi reaches the
minimum at xx, satisfies

|  |  |  |
| --- | --- | --- |
|  | max⁡{ℒci​(φ)​(x),Vci−1​(x)−φ​(x)}≤0.\max\left\{\mathcal{L}^{c\_{i}}(\varphi)(x),V^{c\_{i-1}}(x)-\varphi(x)\right\}\leq 0.\ |  |

The function φ\varphi is called a test function for supersolution at
xx.

(b) A locally Lipschitz function u¯:\underline{u}: [0,∞)→ℝ[0,\infty)\rightarrow{\mathbb{R}}\  is a viscosity subsolution of ([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at x∈(0,∞)x\in(0,\infty) if any twice continuously differentiable function
ψ:[0,∞)→ℝ\psi:[0,\infty)\rightarrow{\mathbb{R}} with ψ​(x)=u¯​(x)\psi(x)=\underline{u}(x), such
that u¯−ψ\underline{u}-\psi reaches the maximum at xx, satisfies

|  |  |  |
| --- | --- | --- |
|  | max⁡{ℒci​(ψ)​(x),Vci−1​(x)−ψ​(x)}≥0​.\max\left\{\mathcal{L}^{c\_{i}}(\psi)(x),V^{c\_{i-1}}(x)-\psi(x)\right\}\geq 0\text{.} |  |

The function ψ\psi is called a test function for subsolution at xx.

(c) A function u:[0,∞)→ℝu:[0,\infty)\rightarrow{\mathbb{R}} which is both a
supersolution and subsolution at x∈[0,∞)x\in[0,\infty) is called a viscosity
solution of ([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at xx.

The following characterization theorem is the discrete analogue of Theorem
[3.3](https://arxiv.org/html/2601.11348v1#theorem3a "Theorem 3.3 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"). The proof is omitted, as it follows similar
arguments to those in the continuous case but is technically simpler.

###### Theorem 4.1

The optimal value function Vci​(x)V^{c\_{i}}(x) for
1≤i<n1\leq i<n is the unique viscosity solution of the associated HJB equation
([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) with boundary condition Vci​(0)=0V^{c\_{i}}(0)=0 and
limx→∞Vci​(x)=(Λ+ci)/q.\lim\_{x\rightarrow\infty}V^{c\_{i}}(x)=(\Lambda+c\_{i})/q.

We also have the following alternative characterization theorem.

###### Theorem 4.2

The optimal value function Vci​(x)V^{c\_{i}}(x)
for 0≤i<n0\leq i<n is the smallest viscosity supersolution of the associated HJB
equation ([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) with boundary condition 0 at x=0x=0
and limit greater than or equal to (Λ+ci)/q(\Lambda+c\_{i})/q\ as xx goes to infinity.

Since for i≥1,i\geq 1, the optimal value function VciV^{c\_{i}} is a viscosity
solution of ([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), there are values of xx where
Vci​(x)=Vci−1​(x)V^{c\_{i}}(x)=V^{c\_{i-1}}(x) and values of xx where ℒci​(Vci)​(x)=0\mathcal{L}^{c\_{i}}(V^{c\_{i}})(x)=0. So for any i≥1i\geq 1, we can partition (0,∞)(0,\infty)
into the closed set 𝒟i={x:Vci​(x)=Vci−1​(x)}\mathcal{D}\_{i}=\{x:V^{c\_{i}}(x)=V^{c\_{i-1}}(x)\} and
the open set ℰi={x:Vci​(x)>Vci−1​(x)}.\mathcal{E}\_{i}=\{x:V^{c\_{i}}(x)>V^{c\_{i-1}}(x)\}. Moreover,
ℒci​(Vci)​(x)=0\mathcal{L}^{c\_{i}}(V^{c\_{i}})(x)=0 in ℰi\mathcal{E}\_{i} and the optimal
strategy is to emit at rate cic\_{i} when the current
surplus is in ℰi\mathcal{E}\_{i} and to decrease the emission rate when the
current surplus is in 𝒟i\mathcal{D}\_{i}.

## 5 Convergence of the optimal value functions from the discrete to the continuous case

In this section, we prove that the optimal value functions corresponding to
the (ratcheting-down) finite set of possible carbon emission rates, as
defined in the previous section, converge to the optimal value function of the
continuous case as the mesh size of the finite sets approaches zero. This is
achieved by considering a sequence of nested meshes.

Consider, for n≥0n\geq 0, a sequence of sets 𝒮n\mathcal{S}^{n} (each with
knk\_{n} elements) of the form

|  |  |  |
| --- | --- | --- |
|  | 𝒮n={c0n=0<ck1n<⋯<cknn=c¯}\mathcal{S}^{n}=\left\{c\_{0}^{n}=0<c\_{k\_{1}}^{n}<\cdots<c\_{k\_{n}}^{n}=\overline{c}\right\} |  |

satisfying the conditions 𝒮0={0,c¯}\mathcal{S}^{0}=\left\{0,\overline{c}\right\},
𝒮n⊂𝒮n+1\mathcal{S}^{n}\subset\mathcal{S}^{n+1} and mesh-size δ​(𝒮n):=maxk=1,kn⁡(ckn−ck−1n)↘0\delta(\mathcal{S}^{n}):=\max\_{k=1,k\_{n}}\left(c\_{k}^{n}-c\_{k-1}^{n}\right)\searrow 0 as nn
goes to infinity. We extend the definition of V𝒮nV^{\mathcal{S}^{n}} to a
function Vn:[0,∞)×[0,c¯]→ℝV^{n}:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn​(x,c)=V𝒮n​(x,c~n),V^{n}(x,c)=V^{\mathcal{S}^{n}}(x,\widetilde{c}^{n}), |  | (5.1) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | c~n=max⁡{cin∈𝒮n:cin≤c}.\widetilde{c}^{n}=\max\{c\_{i}^{n}\in\mathcal{S}^{n}:c\_{i}^{n}\leq c\}. |  | (5.2) |

We will prove that limn→∞Vn​(x,c)=V[0,c¯]​(x,c)\lim\_{n\rightarrow\infty}V^{n}(x,c)=V^{[0,\overline{c}]}(x,c) for any (x,c)∈[0,∞)×[0,c¯](x,c)\in[0,\infty)\times[0,\overline{c}] and we
will study the uniform convergence of this limit. Since 𝒮n⊂𝒮n+1\mathcal{S}^{n}\subset\mathcal{S}^{n+1}, it follows that c~n+1≤\widetilde{c}^{n+1}\leq
c~n∈𝒮n\widetilde{c}^{n}\in\mathcal{S}^{n} for each c∈[0,c¯]c\in[0,\overline{c}]. Then, by monotonicity of V𝒮n+1V^{\mathcal{S}^{n+1}} with
respect to its second variable,

|  |  |  |
| --- | --- | --- |
|  | V[0,c¯]​(x,c)≥Vn+1​(x,c)=V𝒮n+1​(x,c~n+1)≥V𝒮n+1​(x,c~n)≥V𝒮n​(x,c~n)=Vn​(x,c).V^{[0,\overline{c}]}(x,c)\geq V^{n+1}(x,c)=V^{\mathcal{S}^{n+1}}(x,\widetilde{c}^{n+1})\geq V^{\mathcal{S}^{n+1}}(x,\widetilde{c}^{n})\geq V^{\mathcal{S}^{n}}(x,\widetilde{c}^{n})=V^{n}(x,c). |  |

Therefore, the pointwise limit exists and we can define the limit function as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯​(x,c):=limn→∞Vn​(x,c).\overline{V}(x,c):=\lim\_{n\rightarrow\infty}V^{n}(x,c). |  | (5.3) |

Later on, we will show that V¯=V[0,c¯]\overline{V}=V^{[0,\overline{c}]}. Note that
V¯​(x,c)\overline{V}(x,c) is non-increasing in cc, satisfies V¯​(x,c¯)=V​(x,c¯)\overline{V}(x,\overline{c})=V(x,\overline{c}), and is non-decreasing in xx, with the
asymptotic behavior limx→∞\lim\_{x\rightarrow\infty} V¯​(x,c)=(c¯+Λ)/q\overline{V}(x,c)=(\overline{c}+\Lambda)/q.

Using the same arguments as in Proposition 6.1 of [[3](https://arxiv.org/html/2601.11348v1#bib.bib3)], we obtain the following result.

###### Proposition 5.1

The sequence VnV^{n} converges
uniformly to V¯.\overline{V}.

Note that for any (x,c)∈[0,∞)×[0,c¯](x,c)\in[0,\infty)\times[0,\overline{c}], we
have that Vn​(x,c)=V𝒮n​(x,c~n)V^{n}(x,c)=V^{\mathcal{S}^{n}}(x,\widetilde{c}^{n}) is a value
function corresponding to an admissible strategy in Πx,c~n𝒮n⊂Πx,c[0,c¯]\Pi\_{x,\widetilde{c}^{n}}^{\mathcal{S}^{n}}\subset\Pi\_{x,c}^{[0,\overline{c}]}. Hence
V¯​(x,c)=limn→∞Vn​(x,c)\overline{V}(x,c)=\lim\_{n\rightarrow\infty}V^{n}(x,c) is itself a limit of
value functions of admissible strategies in Πx,c[0,c¯]\Pi\_{x,c}^{[0,\overline{c}]}.
Moreover, by Proposition [2.2](https://arxiv.org/html/2601.11348v1#theorem2 "Proposition 2.2 ‣ 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"),

|  |  |  |
| --- | --- | --- |
|  | 0≤Vn​(x2,c1)−Vn​(x1,c2)≤K​[(x2−x1)+(c2−c1)]0\leq V^{n}(x\_{2},c\_{1})-V^{n}(x\_{1},c\_{2})\leq K\left[\left(x\_{2}-x\_{1}\right)+\left(c\_{2}-c\_{1}\right)\right] |  |

for all nn, with a constant KK independent on nn. Since VnV^{n} converges
uniformly to V¯\overline{V}, it follows that V¯\overline{V} is Lipschitz with
the same constant K.K.

With this result, we are now in a position to state the main result of this
section. We omit the proof, as it closely follows the one given in Theorem 4.2
of [[4](https://arxiv.org/html/2601.11348v1#bib.bib4)].

###### Theorem 5.2

The function V¯\overline{V} defined in
([5.3](https://arxiv.org/html/2601.11348v1#S5.E3 "In 5 Convergence of the optimal value functions from the discrete to the continuous case ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) is the optimal value function V[0,c¯]V^{[0,\overline{c}]}.

## 6 Optimal strategies for finite sets

Let us once again consider a finite set of possible
emissions rates:

|  |  |  |
| --- | --- | --- |
|  | S={c0,c1,c2,….,cn},S=\left\{c\_{0},c\_{1},c\_{2},....,c\_{n}\right\}, |  |

where 0=c0<c1<c2<….<cn=c¯0=c\_{0}<c\_{1}<c\_{2}<....<c\_{n}=\overline{c}. We first look for the
following particular strategies, which we call multi-threshold strategies.
These are defined as follows:

* •

  v0{v}^{0}(x):=V0​(x)=(x):=V^{0}(x)= Λq​(1−eθ1​(0)​x)\frac{\Lambda}{q}\left(1-e^{\theta\_{1}(0)x}\right)
* •

  For each i≥1i\geq 1 and thresholds z​(ci)≥0z(c\_{i})\geq 0, the value
  function vci​(x)v^{c\_{i}}(x) satisfies ℒci​(vci)​(x)=0\mathcal{L}^{c\_{i}}(v^{c\_{i}})(x)=0 for
  x∈(z​(ci),∞)x\in(z(c\_{i}),\infty) with limx→∞Wz​(x,ci)=ci+Λq\lim\_{x\rightarrow\infty}W^{z}(x,c\_{i})=\frac{c\_{i}+\Lambda}{q} and vci​(x)=vci−1​(x)v^{c\_{i}}(x)=v^{c\_{i-1}}(x) for x∈[0,z​(ci)]x\in[0,z(c\_{i})].

We will show in this section that the optimal discrete value functions
VciV^{c\_{i}} are indeed of this form. As a result, the optimal value function in
the continuous control setting can be seen as the limit of value functions
associated with multi-threshold strategies.

More precisely, let S~={c1,c2,….,cn}\widetilde{S}=\left\{c\_{1},c\_{2},....,c\_{n}\right\}
and consider a function z:S~→[0,∞)z:\widetilde{S}\rightarrow[0,\infty). We then
define a threshold strategy (which depends on both the current surplus xx and the emission rate ci∈Sc\_{i}\in S), recursively as a stationary strategy

|  |  |  |  |
| --- | --- | --- | --- |
|  | πz=(Cx,ci)(x,ci)∈[0,∞)×S​ where ​Cx,ci∈Πx,ciS\mathbf{\pi}^{z}=(C\_{x,c\_{i}})\_{(x,c\_{i})\in[0,\infty)\times S}\text{ where }C\_{x,c\_{i}}\in\Pi\_{x,c\_{i}}^{S} |  | (6.1) |

as follows:

* •

  If i=0i=0 (i.e. no carbon emission), then (Cx,cn)t=0(C\_{x,c\_{n}})\_{t}=0.
* •

  If 1≤i≤n1\leq i\leq n and x≤z​(ci)x\leq z(c\_{i}) with z​(ci)≥z​(ci−1)z(c\_{i})\geq z(c\_{i-1}),
  follow Cx,ci−1∈Πx,ci−1SC\_{x,c\_{i-1}}\in\Pi\_{x,c\_{i-1}}^{S}.
* •

  If 1≤i≤n1\leq i\leq n and x>z​(ci)x>z(c\_{i}) emit with rate cic\_{i} as
  long as the surplus exceeds z​(ci)z(c\_{i}); once the current surplus reaches
  z​(ci)z(c\_{i}), switch to Cx,ci−1∈Πx,ci−1SC\_{x,c\_{i-1}}\in\Pi\_{x,c\_{i-1}}^{S}. More precisely,

  |  |  |  |
  | --- | --- | --- |
  |  | (Cx,ci)t=ci​It<τ^+(Cz​(ci),ci−1)t​Iτ^≤t<τ,(C\_{x,c\_{i}})\_{t}=c\_{i}I\_{t<\widehat{\tau}}+(C\_{z(c\_{i}),c\_{i-1}})\_{t~}I\_{\widehat{\tau}\leq t<\tau}, |  |

  where τ^\widehat{\tau} is the first hitting time of the surplus process to
  the level z​(ci)z(c\_{i}) and τ\tau is the depletion time.

We refer to z​(ci)z(c\_{i}) as the threshold at emission rate level
cic\_{i} and the function z:S~→[0,∞)z:\widetilde{S}\rightarrow[0,\infty) as the
threshold function. The expected payoff of the multi-threshold
strategy πz\pi^{z} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wz​(x,ci):=J​(x;Cx,ci).W^{z}(x,c\_{i}):=J(x;C\_{x,c\_{i}}). |  | (6.2) |

Note that Wz​(x,ci)W^{z}(x,c\_{i}) only depends on the threshold values z​(ck)z(c\_{k}) for
1≤k≤i,1\leq k\leq i, that Wz​(0,ci)=0W^{z}(0,c\_{i})=0 and that Wz​(x,ci)=V0​(x)W^{z}(x,c\_{i})=V^{0}(x)
for 0≤x≤min⁡{z​(ck):1≤k≤i}.0\leq x\leq\min\{z(c\_{k}):1\leq k\leq i\}.

We next obtain a recursive formula for WzW^{z}.

###### Proposition 6.1

We have the following recursive
formula for WzW^{z}: Wz​(x,0)=Λ​(1−eθ1​(0)​x)/qW^{z}(x,0)=\Lambda\left(1-e^{\theta\_{1}(0)x}\right)/q, and for 1≤i≤n,1\leq i\leq n,

|  |  |  |
| --- | --- | --- |
|  | Wz​(x,ci)={Wz​(x,ci−1)ifx≤z​(ci)ci+Λq​(1−az​(ci)​eθ1​(ci)​x)ifx>z​(ci),W^{z}(x,c\_{i})=\left\{\begin{array}[c]{lll}W^{z}(x,c\_{i-1})&\text{if}&x\leq z(c\_{i})\\ \frac{c\_{i}+\Lambda}{q}\left(1-a^{z}(c\_{i})e^{\theta\_{1}(c\_{i})x}\right)&\text{if}&x>z(c\_{i}),\end{array}\right. |  |

where

|  |  |  |
| --- | --- | --- |
|  | az​(ci):=(1−qci+Λ​Wz​(z​(ci),ci−1))​e−θ1​(ci)​z​(ci)​ and ​eθ1​(ci)​z​(ci)>az​(ci)>0.a^{z}(c\_{i}):=\left(1-\frac{q}{c\_{i}+\Lambda}W^{z}(z(c\_{i}),c\_{i-1})\right)e^{-\theta\_{1}(c\_{i})z(c\_{i})}\text{ and }e^{\theta\_{1}(c\_{i})z(c\_{i})}>a^{z}(c\_{i})>0. |  |

Proof. By construction, the strategy πz\mathbf{\pi}^{z} emits at rate
cic\_{i} when the surplus exceeds z​(ci).z(c\_{i}). Hence,
ℒci​(Wz)​(x,ci)=0\mathcal{L}^{c\_{i}}(W^{z})(x,c\_{i})=0 for x∈(z​(ci),∞)x\in(z(c\_{i}),\infty). Since
limx→∞Wz​(x,ci)=(ci+Λ)/q\lim\_{x\rightarrow\infty}W^{z}(x,c\_{i})=(c\_{i}+\Lambda)/q and the
emission strategy switches to emit ci−1c\_{i-1} at the threshold z​(ci)z(c\_{i}), we
have Wz​(z​(ci),ci)=Wz​(z​(ci),ci−1)W^{z}(z(c\_{i}),c\_{i})=W^{z}(z(c\_{i}),c\_{i-1}). Also, Wz​(x,ci−1)<(ci+Λ)/qW^{z}(x,c\_{i-1})<(c\_{i}+\Lambda)/q, so we get the result. ■\blacksquare

Now, we aim to maximize Wz​(x,ci)W^{z}(x,c\_{i}) over all possible multi-threshold
functions z:S~→[0,∞)z:\widetilde{S}\rightarrow[0,\infty). We denote by
z∗:S~→[0,∞)z^{\ast}:\widetilde{S}\rightarrow[0,\infty) the optimal
multi-threshold function, which can equivalently be interpreted as the one
that minimizes az∗​(ci)​(ci)a^{z^{\ast}(c\_{i})}(c\_{i}) for each 1≤i≤n1\leq i\leq n. From Proposition [3.4](https://arxiv.org/html/2601.11348v1#theorem4 "Proposition 3.4 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), if Λ<μ2+2​q​σ2\Lambda<\sqrt{\mu^{2}+2q\sigma^{2}}, then z∗​(ci)=0z^{\ast}(c\_{i})=0 for all ci∈[0,μ2+2​q​σ2−Λ22​(Λ+μ)]c\_{i}\in[0,\frac{\mu^{2}+2q\sigma^{2}-\Lambda^{2}}{2(\Lambda+\mu)}] and z∗​(ci)>0z^{\ast}(c\_{i})>0 otherwise. Therefore, from now on we consider only the case
ci>μ2+2​q​σ2−Λ22​(Λ+μ)c\_{i}>\frac{\mu^{2}+2q\sigma^{2}-\Lambda^{2}}{2(\Lambda+\mu)} if this value
is positive. Note that, as a first step, we are maximizing the discounted
expected emissions only among multi-threshold strategies, not among all
admissible strategies, which could, in principle, have a more complex
structure. Later in this section (Theorem [6.2](https://arxiv.org/html/2601.11348v1#theorem2d "Theorem 6.2 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")),
we will show that the resulting value function coincides with the optimal
discrete value function VS​(x,ci)V^{S}(x,c\_{i}).

Since the initial function Wz​(x,0)W^{z}(x,0) in the recursive procedure is known,
we can interpret the optimization problem in two different ways.

1. 1.

   First Approach. Recursive One-Dimensional Optimization:

   We solve a sequence of nn one-dimensional optimization problems obtaining the
   minimum of az​(ci)a^{z}(c\_{i}). Suppose that Wz∗​(x,ck)W^{z^{\ast}}(x,c\_{k}) and z∗​(ck)z^{\ast}(c\_{k}) are known for k=1,…,i−1k=1,\ldots,i-1. Then, from the recursive formula
   (Proposition [6.1](https://arxiv.org/html/2601.11348v1#theorem1d "Proposition 6.1 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), we can
   compute Wz∗​(x,ci)W^{z^{\ast}}(x,c\_{i}) and z∗​(ci)z^{\ast}(c\_{i}) as follows. Define the
   continuous function Gi:[0,∞)→ℝG\_{i}:[0,\infty)\rightarrow\mathbb{R} as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Gi​(y):=(1−qci+Λ​Wz∗​(y,ci−1))​e−θ1​(ci)​y​ .G\_{i}(y):=\left(1-\frac{q}{c\_{i}+\Lambda}W^{z^{\ast}}(y,c\_{i-1})\right)e^{-\theta\_{1}(c\_{i})y}\text{ .} |  | (6.3) |

   We have Gi​(0)=1G\_{i}(0)=1 and since

   |  |  |  |
   | --- | --- | --- |
   |  | 0<limy→∞Wz∗​(y,ci−1)<ci−1+Λq0<\lim\_{y\rightarrow\infty}W^{z^{\ast}}(y,c\_{i-1})<\frac{c\_{i-1}+\Lambda}{q} |  |

   and θ1​(ci)<0\theta\_{1}(c\_{i})<0, we have 0<Gi​(y)0<G\_{i}(y) and limy→∞Gi​(y)=∞\lim\_{y\rightarrow\infty}G\_{i}(y)=\infty. As GiG\_{i} is continuous, it attains its minimum
   in [0,∞)[0,\infty). We define

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | z∗​(ci):=min⁡(arg⁡miny∈[0,∞)⁡Gi​(y)), ​a∗​(ci)=Gi​(z∗​(ci)).z^{\ast}(c\_{i}):=\min\left(\arg\min\_{y\in[0,\infty)}G\_{i}(y)\right),\text{ }a^{\ast}(c\_{i})=G\_{i}(z^{\ast}(c\_{i})). |  | (6.4) |

   The function Wz∗​(⋅,ci)W^{z^{\ast}}(\cdot,c\_{i}) satisfies ℒci​(Wz∗)​(x,ci)=0\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(x,c\_{i})=0 for x>z∗​(ci)x>z^{\ast}(c\_{i}) and Wz∗​(x,ci)=W^{z^{\ast}}(x,c\_{i})= Wz∗​(x,ci−1)W^{z^{\ast}}(x,c\_{i-1}) for x∈[0,z∗​(ci)].x\in[0,z^{\ast}(c\_{i})].
2. 2.

   Second Approach: Sequence of Obstacle Problems.

   This approach interprets the problem as a recursive sequence of
   one-dimensional obstacle problems. Assume that Wz∗​(x,ck)W^{z^{\ast}}(x,c\_{k}) and the
   optimal thresholds z∗​(ck)z^{\ast}(c\_{k}) are known for k=1,…,i−1k=1,\ldots,i-1. To find
   Wz∗​(x,ci)W^{z^{\ast}}(x,c\_{i}) and z∗​(ci)z^{\ast}(c\_{i}), consider the smallest solution
   U∗U^{\ast} of the differential equation ℒci​(U)=0\mathcal{L}^{c\_{i}}(U)=0 in
   [0,∞)[0,\infty) with boundary condition limx→∞U​(x)=ci+Λq\lim\_{x\rightarrow\infty}U(x)=\frac{c\_{i}+\Lambda}{q} such that U∗​(⋅)≥Wz∗​(⋅,ci−1)U^{\ast}(\cdot)\geq W^{z^{\ast}}(\cdot,c\_{i-1}). We define:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | z∗​(ci)={0if ​U∗​(⋅)>Wz∗​(⋅,ci−1)​in ​(0,∞)sup{y>0:U∗​(y)=Wz∗​(y,ci−1)}otherwise.z^{\ast}(c\_{i})=\left\{\begin{array}[c]{ll}0&\text{if }U^{\ast}(\cdot)>W^{z^{\ast}}(\cdot,c\_{i-1})\ \text{in }(0,\infty)\\ \sup\{y>0:U^{\ast}(y)=W^{z^{\ast}}(y,c\_{i-1})\}&\text{otherwise.}\end{array}\right. |  | (6.5) |

   In other words, z∗​(ci)z^{\ast}(c\_{i}) is the last point at which U∗U^{\ast} and
   Wz∗​(⋅,ci+1)W^{z^{\ast}}(\cdot,c\_{i+1}) coincide. If they only coincide at y=0y=0, then
   z∗​(ci)=0z^{\ast}(c\_{i})=0. We then have that Wz∗​(x,ci)=U∗​(x)W^{z^{\ast}}(x,c\_{i})=U^{\ast}(x) for
   x>z∗​(ci)x>z^{\ast}(c\_{i}) and Wz∗​(x,ci)=Wz∗​(x,ci−1)W^{z^{\ast}}(x,c\_{i})=W^{z^{\ast}}(x,c\_{i-1}) for
   x≤z∗​(ci)x\leq z^{\ast}(c\_{i}). To show that U∗U^{\ast} exists, note that by
   ([3.4](https://arxiv.org/html/2601.11348v1#S3.E4 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), the solutions UU of the
   differential equation ℒci​(U)=0\mathcal{L}^{c\_{i}}(U)=0 in [0,∞)[0,\infty) with boundary
   condition limx→∞U​(x)=(ci+Λ)/q\lim\_{x\rightarrow\infty}U(x)=(c\_{i}+\Lambda)/q are of the
   form

   |  |  |  |
   | --- | --- | --- |
   |  | Ua​(x)=ci+Λq​(1−a​eθ1​(ci)​x).U\_{a}(x)=\frac{c\_{i}+\Lambda}{q}\left(1-ae^{\theta\_{1}(c\_{i})x}\right). |  |

   So, U∗=Ua∗​(ci)U^{\ast}=U\_{a^{\ast}(c\_{i})} where a∗​(ci)a^{\ast}(c\_{i}) is defined in
   ([6.4](https://arxiv.org/html/2601.11348v1#S6.E4 "In item 1 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")).

###### Remark 6.1

If z∗​(ci)>0,z^{\ast}(c\_{i})>0, Uai∗​(z∗​(ci))=Wz∗​(z∗​(ci),ci−1)U\_{a\_{i}^{\ast}}(z^{\ast}(c\_{i}))=W^{z^{\ast}}(z^{\ast}(c\_{i}),c\_{i-1}), Uai∗​(x)≥Wz∗​(x,ci−1)U\_{a\_{i}^{\ast}}(x)\geq W^{z^{\ast}}(x,c\_{i-1}) for x≥0x\geq 0 and Uai∗​(x)>Wz∗​(x,ci+1)U\_{a\_{i}^{\ast}}(x)>W^{z^{\ast}}(x,c\_{i+1}) for x∈(z∗​(ci),∞)x\in(z^{\ast}(c\_{i}),\infty). Note that we
can show by a recursive argument that Wz∗​(x,ci)W^{z^{\ast}}(x,c\_{i}) is infinitely
continuously differentiable at all x∈[0,∞)∖{z∗​(ck):k=i,…,n}x\in[0,\infty)\setminus\{z^{\ast}(c\_{k}):k=i,\ldots,n\} and continuously differentiable at the points z∗​(ck)z^{\ast}(c\_{k})\ for k=i,…,n.k=i,\ldots,n. Indeed, Uai∗U\_{a\_{i}^{\ast}} and Wz∗​(⋅,0)W^{z^{\ast}}(\cdot,0) are infinitely continuously differentiable and Uai∗′​(z∗​(ci))−∂xWz∗​(z∗​(ci),ci−1)=0U\_{a\_{i}^{\ast}}^{\prime}(z^{\ast}(c\_{i}))-\partial\_{x}W^{z^{\ast}}(z^{\ast}(c\_{i}),c\_{i-1})=0 because Uai∗​(⋅)−Wz∗​(⋅,ci−1)U\_{a\_{i}^{\ast}}(\cdot)-W^{z^{\ast}}(\cdot,c\_{i-1})
reaches the minimum at z∗​(ci)z^{\ast}(c\_{i}). Moreover, since Wz∗​(x,ci)=Wz∗​(x,ci−1)​I{x<z∗​(ci)}+Uai∗​(x)​I{x≥z∗​(ci)}W^{z^{\ast}}(x,c\_{i})=W^{z^{\ast}}(x,c\_{i-1})I\_{\{x<z^{\ast}(c\_{i})\}}+U\_{a\_{i}^{\ast}}(x)I\_{\{x\geq z^{\ast}(c\_{i})\}},

|  |  |  |
| --- | --- | --- |
|  | ∂x​xWz∗​(z∗​(ci)+,ci)−∂x​xWz∗​(z∗​(ci)−,ci)=Uai∗′′​(z∗​(ci))−∂x​xWz∗​(z∗​(ci)−,ci−1)≥0.\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{+},c\_{i})-\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{-},c\_{i})=U\_{a\_{i}^{\ast}}^{\prime\prime}(z^{\ast}(c\_{i}))-\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{-},c\_{i-1})\geq 0. |  |

⋄\diamond

###### Remark 6.2

The function U0​(x)=(ci+Λ)/qU\_{0}(x)=(c\_{i}+\Lambda)/q is a constant
function. For a>0a>0, the function

|  |  |  |
| --- | --- | --- |
|  | Ua​(x)=ci+Λq​(1−a​eθ1​(ci)​x).U\_{a}(x)=\frac{c\_{i}+\Lambda}{q}\left(1-ae^{\theta\_{1}(c\_{i})x}\right). |  |

is strictly increasing and concave, with

|  |  |  |
| --- | --- | --- |
|  | ∂xUa​(x)=−θ1​(ci)​ci+Λq​a​eθ1​(ci)​x>0,∂x​xUa​(x)=−θ12​(ci)​ci+Λq​a​eθ1​(ci)​x<0,\partial\_{x}U\_{a}(x)=-\theta\_{1}(c\_{i})\frac{c\_{i}+\Lambda}{q}ae^{\theta\_{1}(c\_{i})x}>0,\quad\partial\_{xx}U\_{a}(x)=-\theta\_{1}^{2}(c\_{i})\frac{c\_{i}+\Lambda}{q}ae^{\theta\_{1}(c\_{i})x}<0, |  |

and it is bounded above by U0​(x).U\_{0}(x). ⋄\diamond

In the next theorem, we show that there exists an optimal strategy and it is
of threshold type. The proof is in the appendix.

###### Theorem 6.2

If z∗z^{\ast}\ is the optimal threshold
function, then Wz∗​(x,ci)W^{z^{\ast}}(x,c\_{i}) is the optimal function Vci​(x)V^{c\_{i}}(x)
defined in ([2.2](https://arxiv.org/html/2601.11348v1#S2.E2 "In 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) for i=1,…,ni=1,...,n.

###### Remark 6.3

By Remark [6.1](https://arxiv.org/html/2601.11348v1#S6.Thmremark1 "Remark 6.1 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), the
function GiG\_{i} defined in ([6.3](https://arxiv.org/html/2601.11348v1#S6.E3 "In item 1 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"))  is continuously
differentiable. If its minimum z∗​(ci)z^{\ast}(c\_{i}) is positive, the first-order
condition Gi′​(z∗​(ci))=0G\_{i}^{\prime}(z^{\ast}(c\_{i}))=0 implies that z∗​(ci)z^{\ast}(c\_{i}) satisfies the implicit equation

|  |  |  |
| --- | --- | --- |
|  | θ1​(ci)​Wz∗​(y,ci−1)−∂xWz∗​(y,ci−1)=θ1​(ci)​ci+Λq\theta\_{1}(c\_{i})W^{z^{\ast}}(y,c\_{i-1})-\partial\_{x}W^{z^{\ast}}(y,c\_{i-1})=\theta\_{1}(c\_{i})\frac{c\_{i}+\Lambda}{q} |  |

for i=1,…,n−1.i=1,\ldots,n-1. ⋄\diamond

###### Remark 6.4

Given z:S~→[0,∞)z:\widetilde{S}\rightarrow[0,\infty), we have defined in ([6.1](https://arxiv.org/html/2601.11348v1#S6.E1 "In 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) a threshold strategy
πz=(Cx,ci)(x,ci)∈[0,∞)×S\mathbf{\pi}^{z}=(C\_{x,c\_{i}})\_{(x,c\_{i})\in[0,\infty)\times S}, where
Cx,ci∈Πx,ciSC\_{x,c\_{i}}\in\Pi\_{x,c\_{i}}^{S} for i=1,…,ni=1,\ldots,n. We can extend this
threshold strategy to

|  |  |  |  |
| --- | --- | --- | --- |
|  | π~z=(Cx,c)(x,c)∈[0,∞)×[0,cn]​where ​Cx,c∈Πx,cS\widetilde{\mathbf{\pi}}^{z}=(C\_{x,c})\_{(x,c)\in[0,\infty)\times[0,c\_{n}]}~\text{where~}C\_{x,c}\in\Pi\_{x,c}^{S} |  | (6.6) |

as follows:

* •

  If c∈(ci,ci+1)c\in(c\_{i},c\_{i+1}) and x>z​(ci)x>z(c\_{i}), emit with rate cc while the
  current surplus is above z​(ci)z(c\_{i}). If the current surplus reaches
  z​(ci)z(c\_{i}), follow Cz​(ci),ci∈Πx,ciSC\_{z(c\_{i}),c\_{i}}\in\Pi\_{x,c\_{i}}^{S}.
* •

  If c∈(ci,ci+1)c\in(c\_{i},c\_{i+1}) and x≤z​(ci)x\leq z(c\_{i}) , follow Cx,ci∈Πx,ciS.C\_{x,c\_{i}}\in\Pi\_{x,c\_{i}}^{S}. More precisely, if (x,c)∈[z​(ci),∞)×(ci,ci+1),(x,c)\in[z(c\_{i}),\infty)\times(c\_{i},c\_{i+1}),
  then Cx,c∈Πx,cSC\_{x,c}\in\Pi\_{x,c}^{S} is defined as (Cx,c)t=c\left(C\_{x,c}\right)\_{t}=c
  and so XtCx,c=Xt−c​tX\_{t}^{C\_{x,c}}=X\_{t}-ct for t<τit<\tau\_{i} where

  |  |  |  |
  | --- | --- | --- |
  |  | τi:=min⁡{s:XtCx,c=z​(ci)},\tau\_{i}:=\min\{s:X\_{t}^{C\_{x,c}}=z(c\_{i})\}, |  |

  and (Cx,c)t=(Cz​(ci),ci)t−τi∈Πz​(ci),ciS\left(C\_{x,c}\right)\_{t}=\left(C\_{z(c\_{i}),c\_{i}}\right)\_{t-\tau\_{i}}\in\Pi\_{z(c\_{i}),c\_{i}}^{S} for t≥τit\geq\tau\_{i}. Finally,
  Cx,c=Cx,ciC\_{x,c}=C\_{x,c\_{i}} ∈Πx,ciS\in\Pi\_{x,c\_{i}}^{S} for (x,c)∈[0,z​(ci)]×(ci,ci+1).(x,c)\in[0,z(c\_{i})]\times(c\_{i},c\_{i+1}).

The value function of the stationary strategy π~z\widetilde{\mathbf{\pi}}^{z}
is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπ~z​(x,c):=J​(x;Cx,c):[0,∞)×[c0,cn]→[0,∞).J^{\widetilde{\mathbf{\pi}}^{z}}(x,c):=J(x;C\_{x,c}):[0,\infty)\times[c\_{0},c\_{n}]\rightarrow[0,\infty){.} |  | (6.7) |

⋄\diamond

## 7 Numerical Illustrations

In this section we present examples in which we approximate the optimal value
function by a multi-threshold strategy considering a discrete set of possible
emission rates. For a given nn, define the mesh-size as Δ​c=c¯/n\Delta c={\overline{c}}/{n} and consider the finite set

|  |  |  |
| --- | --- | --- |
|  | Sn={0,Δc,2Δc,3Δc,….,c¯}.S^{n}=\left\{0,\Delta c,2\Delta c,3\Delta c,....,\overline{c}\right\}. |  |

(1) We begin by defining

|  |  |  |
| --- | --- | --- |
|  | V0​(x)=Λq​(1−eθ1​(0)​x),V^{0}(x)=\frac{\Lambda}{q}\left(1-e^{\theta\_{1}(0)x}\right), |  |

which is the solution to the equation ℒ0​(W)=0\mathcal{L}^{0}(W)=0 with limit
boundary conditions limx→∞W​(x)=Λ/q\lim\_{x\rightarrow\infty}W(x)=\Lambda/q. Note that
V0V^{0} is not zero due to the positive reward Λ\Lambda.

(2) Recursive construction:

To compute Vk​Δ​c,V^{k\Delta c}, we consider value functions of strategies that
emit at a constant rate ck=k​Δ​cc\_{k}=k\Delta c when x≥xkx\geq x\_{k} and
switch to the lower rate value function V(k−1)​Δ​cV^{(k-1)\Delta c} when 0≤x<xk0\leq x<x\_{k}. To obtain this value function, we consider the solutions of equation
ℒk​Δ​c​(W1)=0\mathcal{L}^{k\Delta c}(W\_{1})=0 on (xk,∞](x\_{k},\infty] with boundary condition
at infinity limx→∞Wk​(x)=(k​Δ​c+Λ)/q.\lim\_{x\rightarrow\infty}W\_{k}(x)=(k\Delta c+\Lambda)/q. The
general solution is given by

|  |  |  |
| --- | --- | --- |
|  | Wk​(x)=k​Δ​c+Λq+ak​eθ1​(k​Δ​c)​x.W\_{k}(x)=\frac{k\Delta c+\Lambda}{q}+a\_{k}e^{\theta\_{1}(k\Delta c)x}. |  |

We then determine the constant aka\_{k} by matching this function continuously
to V(k−1)​Δ​c​(x)V^{(k-1)\Delta c}(x) at the threshold point xkx\_{k}. Finally, we optimize
over all possible switching points xkx\_{k} to obtain the optimal threshold
z∗​(ck)=xk∗..z^{\ast}(c\_{k})=x\_{k}^{\ast.}. It follows that Vk​Δ​c​(x)V^{k\Delta c}(x) is the
optimal value function corresponding to the optimal multi-threshold strategy
described above.

In each of the examples, we display VS​(x,c¯)V^{S}(x,\overline{c}) as a function of initial carbon budget xx. From the results of the
previous sections, we know that this function converges to the optimal value function of the
continuous case as n→∞n\rightarrow\infty (we choose n=500n=500 in each of the illustrations). We also depict the set {(z∗​(0),0),(z∗​(c1),c1),…,(z∗​(c¯),c¯)}\left\{(z^{\ast}(0),0),(z^{\ast}(c\_{1}),c\_{1}),...,(z^{\ast}(\overline{c}),\overline{c})\right\} corresponding to the optimal threshold points. These points
are taken as an approximation of the optimal strategy—hence of a curve—in
the continuous case. Roughly speaking, to the right of this curve, the optimal
strategy is to emit carbon at maximum rate allowed (which is the current emission level cc), whereas to the left of the curve, the
optimal policy is to immediately reduce the emission rate and move vertically downward
toward the curve.

###### Example 7.1

We consider in this example μ=3\mu=3, σ=2\sigma=2 and q=0.1,q=0.1, Λ=4\Lambda=4 for
S=[0,4]S=[0,4]. Figure [7.1(a)](https://arxiv.org/html/2601.11348v1#S7.F1.sf1 "In Figure 7.1 ‣ Example 7.1 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") shows VS​(x,4)V^{S}(x,4) (solid line), as a function of
initial carbon budget xx. The dashed line in the figure represents the classical optimal value function Vclass​(x,c)=Vclass​(x)V\_{\text{class}}(x,c)=V\_{\text{class}}(x) of the unconstrained case (that is, in the absence of downward ratcheting) for these parameters. One can see that the “cost” imposed by the downward ratcheting constraint is relatively limited. Moreover, a policy of continuous abatement is psychologically easier to implement than a strategy of remaining fully greedy and then abruptly reducing excess emissions to zero whenever the carbon budget falls below the fixed barrier—an approach that would maximize the value function in the unconstrained case. Figure [7.1(b)](https://arxiv.org/html/2601.11348v1#S7.F1.sf2 "In Figure 7.1 ‣ Example 7.1 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") depicts the optimal
abatement threshold as a function of current available excess carbon emission level xx. Since Λ=4>μ2+2​q​σ2≈3.1305\Lambda=4>\sqrt{\mu^{2}+2q\sigma^{2}}\approx 3.1305, the optimal threshold is positive for all
0≤c≤40\leq c\leq 4 (cf. Proposition
[3.4](https://arxiv.org/html/2601.11348v1#theorem4 "Proposition 3.4 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")). Note that the optimal constant barrier in the absence of a ratcheting-down constraint is 4.682 for the present example (which one can for instance calculate with the formulas from [[6](https://arxiv.org/html/2601.11348v1#bib.bib6)]). ⋄\diamond

![Refer to caption](x1.png)


(a) V​(x,4)V(x,4) and Vclass​(x,4)V\_{\text{class}}(x,4)

![Refer to caption](x2.png)


(b) z∗​(c)z^{\*}(c)

Figure 7.1: Optimal value function V​(x,4)V(x,4) (solid line) and unconstrained value function Vclass​(x)V\_{\text{class}}(x) (dashed line) as well as optimal threshold z∗​(c)z^{\*}(c) (right) for μ=3\mu=3, σ=2\sigma=2, q=0.1q=0.1, Λ=4\Lambda=4 and S=[0,4]S=[0,4].

###### Example 7.2

We now would like to focus on the effect of the drift μ\mu and choose σ=1\sigma=1, q=0.1,Λ=1.5q=0.1,\Lambda=1.5 and S=[0,2]S=[0,2]. Figure [7.2](https://arxiv.org/html/2601.11348v1#S7.F2 "Figure 7.2 ‣ Example 7.2 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") depicts V​(x,2)V(x,2) and the optimal abatement curve z∗​(c)z^{\*}(c) for various values of μ\mu (positive, zero and negative).
In this example Λ=1.5>μ2+2​q​σ2\Lambda=1.5>\sqrt{\mu^{2}+2q\sigma^{2}} and Λ+μ>0\Lambda+\mu>0 for all chosen values of μ\mu. Therefore, by Remark [3.3](https://arxiv.org/html/2601.11348v1#S3.Thmremark3 "Remark 3.3 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") and monotonicity of z∗​(c)z^{\*}(c), the optimal threshold is positive for all values of cc. One observes empirically that the threshold function z∗​(c)z^{\*}(c) is a convex function of cc for c<cec<c\_{e} for some critical value cec\_{e}, and a concave function for c>cec>c\_{e} (note that the cc-axis is the ordinate in that plot). Moreover, the plot suggests that ce=μc\_{e}=\mu for any μ≥0\mu\geq 0. We can not prove this latter claim with the techniques developed in this paper, but believe it to hold in general, and leave it as a conjecture for future research.

The optimal barrier without the abatement constraint is 2.997 for μ=1\mu=1, it is 4.0594.059 for μ=0.5\mu=0.5, 5.584 for μ=0\mu=0 and 6.110 for μ=−0.5\mu=-0.5, respectively. Especially for zero or negative drift, this means that in the unconstrained case one would not allow carbon emissions unless the carbon budget level is quite high, as the budget would be depleted too quickly and the Λ\Lambda-reward for the budget to last longer outweighs the immediate consumption benefit. Especially in such a situation, the abatement schedule is clearly preferable as it starts with consumption immediately and the efficiency loss (in terms of value function when compared to the unconstrained case) is still quite limited: for instance, for x=5x=5 and μ=0\mu=0 the threshold strategy with optimal barrier 5.584 (emissions at rate c¯=2\overline{c}=2 above the barrier and no emissions when the surplus is below the barrier) leads to a value function of 14.22, and for x=5x=5 and μ=−0.5\mu=-0.5 the threshold strategy with optimal barrier 6.110 leads to a value function of 8.71. In view of the values for x=5x=5 in Figure [7.2(a)](https://arxiv.org/html/2601.11348v1#S7.F2.sf1 "In Figure 7.2 ‣ Example 7.2 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), the efficiency loss from the non-ratcheting constraint is indeed quite small.

It is also a natural question to see by how much the optimal abatement strategy outperforms a simple (intuitive, but non-optimal) linear abatement schedule c​(t)=c¯−m​tc(t)=\overline{c}-m\,t over time, starting in c=c¯c=\overline{c} and decreasing at a slope mm such that the original budget xx is used up when c​(t)c(t) hits c=0c=0 (which we denote t∗t^{\*}; in case of σ=0\sigma=0 this would exactly mark the depletion time τ\tau). A simple calculation gives m=c¯2/(2​x)m=\overline{c}^{2}/(2x) and t∗=2​x/c¯t^{\*}=2x/\overline{c}. Since the initial budget xx will typically be given, a target time horizon for net-zero may determine the choice of the initial carbon emission rate c¯\overline{c}. For x=5x=5, the above choice c¯=2\overline{c}=2 gives for instance t∗=5t^{\*}=5 years. For the present parameters with μ=0\mu=0, a Monte Carlo simulation shows that such a linear abatement schedule would lead to a value function of 9.81​(±0.14)9.81(\pm 0.14), where here and throughout, the number in parentheses indicates the halfwidth of the asymptotic 95% confidence interval of the simulation.
The value of 9.81 is about 30% below the corresponding value contained in the dotted line in Figure [7.2(a)](https://arxiv.org/html/2601.11348v1#S7.F2.sf1 "In Figure 7.2 ‣ Example 7.2 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"). Figure [7.3](https://arxiv.org/html/2601.11348v1#S7.F3 "Figure 7.3 ‣ Example 7.2 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") illustrates both strategies for a sample path of the original surplus process XtX\_{t} for μ=0\mu=0. The black curve represents the surplus process XtCX\_{t}^{C} when applying the optimal abatement strategy z∗​(c)z^{\*}(c), which is the dotted line in Figure [7.2(b)](https://arxiv.org/html/2601.11348v1#S7.F2.sf2 "In Figure 7.2 ‣ Example 7.2 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), and the blue curve is the resulting abatement schedule for this sample path as a function of time. For this particular sample path, around t=10t=10 the controlled carbon emission budget undershoots x≈2.8x\approx 2.8 for the first time, which leads to c=0c=0 from then on, and the carbon budget remains positive for much longer (rewarded by the Λ\Lambda-term, capturing the value of retaining part of the carbon budget, for example for the next generation). The red dotted curve is the (non-adaptive) linear abatement schedule c​(t)=2−0.4​tc(t)=2-0.4\,t, which equals zero (and therefore stopping emissions completely) already after 5 years, and the associated surplus process XtCX\_{t}^{C} is depleted already much earlier than the one for the optimal strategy (a Monte Carlo simulation indicates that the expected depletion times under the two strategies are 38.50​(±1.37)38.50(\pm 1.37) and 9.83​(±0.70)9.83(\pm 0.70), respectively). ⋄\diamond

![Refer to caption](x3.png)


(a) V​(x,2)V(x,2)

![Refer to caption](x4.png)


(b) z∗​(c)z^{\*}(c)

Figure 7.2: Optimal value function V​(x,2)V(x,2) and optimal threshold z∗​(c)z^{\*}(c) for σ=1\sigma=1, q=0.1q=0.1, Λ=1.5\Lambda=1.5 and S=[0,2]S=[0,2] for μ=1\mu=1 (solid line), μ=0.5\mu=0.5 (dashed line), μ=0\mu=0 (dotted line) and μ=−0.5\mu=-0.5 (dash-dotted line).

![Refer to caption](x5.png)


Figure 7.3: Sample path XtCX\_{t}^{C} and resulting emission patterns for the parameters of Figure [7.2(a)](https://arxiv.org/html/2601.11348v1#S7.F2.sf1 "In Figure 7.2 ‣ Example 7.2 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") with μ=0\mu=0 for the optimal strategy according to z∗​(c)z^{\*}(c) and a linear decreasing emission rate c​(t)=2−0.4​tc(t)=2-0.4t.

Note that the numerical value of Λ\Lambda balances the importance of substantial early emissions against the desire to delay the depletion time. In the next example we therefore look at the sensitivity of the optimal strategy with respect to Λ\Lambda.

###### Example 7.3

We now vary the reward level Λ.\Lambda.
For the case σ=1\sigma=1, q=0.1,μ=1q=0.1,\mu=1 and S=[0,2]S=[0,2], Figure [7.4](https://arxiv.org/html/2601.11348v1#S7.F4 "Figure 7.4 ‣ Example 7.3 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") depicts the value function and optimal threshold strategy for Λ=1.5\Lambda=1.5 (solid line), Λ=1\Lambda=1 (dashed line), Λ=0.5\Lambda=0.5 (dotted line) and Λ=0\Lambda=0 (dash-dotted line). For Λ=1.5>μ2+2​q​σ2≈1.10\Lambda=1.5>\sqrt{\mu^{2}+2q\sigma^{2}}\approx 1.10, the optimal strategy for each value of cc involves a
positive threshold. In contrast, for the smaller rewards Λ=1,0.5\Lambda=1,0.5 and 0, respectively, the optimal threshold
is zero for all 0≤c≤2​q​σ2+μ2−Λ22​(Λ+μ)0\leq c\leq\frac{2q\sigma^{2}+\mu^{2}-\Lambda^{2}}{2\left(\Lambda+\mu\right)} and positive otherwise (cf. Proposition [3.4](https://arxiv.org/html/2601.11348v1#theorem4 "Proposition 3.4 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") and Remark [3.3](https://arxiv.org/html/2601.11348v1#S3.Thmremark3 "Remark 3.3 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")).

As Λ\Lambda decreases, the importance of prolonged carbon-budget availability diminishes, leading to lower surplus threshold levels for emission rate reductions. For the extreme case Λ=0\Lambda=0, corresponding to the absence of sustainability considerations, the limiting value of cc for which the threshold is positive becomes (μ2+2​q​σ2)/(2​μ)=0.6(\mu^{2}+2q\sigma^{2})/(2\mu)=0.6 for the present parameters (cf. Remark [3.3](https://arxiv.org/html/2601.11348v1#S3.Thmremark3 "Remark 3.3 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), which is precisely the value at which z∗​(c)z^{\*}(c) intersects the cc-axis in Figure [7.4(b)](https://arxiv.org/html/2601.11348v1#S7.F4.sf2 "In Figure 7.4 ‣ Example 7.3 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target").

In general, one observes from Figure [7.4](https://arxiv.org/html/2601.11348v1#S7.F4 "Figure 7.4 ‣ Example 7.3 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target") that the overall shape of the optimal curve z∗​(c)z^{\*}(c) is relatively robust w.r.t. the choice of Λ\Lambda (Figure [7.4(b)](https://arxiv.org/html/2601.11348v1#S7.F4.sf2 "In Figure 7.4 ‣ Example 7.3 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), but the value function itself is quite sensitive (Figure [7.4(a)](https://arxiv.org/html/2601.11348v1#S7.F4.sf1 "In Figure 7.4 ‣ Example 7.3 ‣ 7 Numerical Illustrations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")). In other words, for these parameter values the reward procedure (and thus the sustainability component) contributes substantially to the overall performance of the optimal strategy; however, the strategies themselves are largely insensitive to increases or decreases in the reward procedure. ⋄\diamond

![Refer to caption](x6.png)


(a) V​(x,2)V(x,2)

![Refer to caption](x7.png)


(b) z∗​(c)z^{\*}(c)

Figure 7.4: Optimal value function V​(x,2)V(x,2) and optimal threshold z∗z^{\*} as a function of cc for σ=1\sigma=1, q=0.1q=0.1, μ=1\mu=1 and S=[0,2]S=[0,2] for Λ=1.5\Lambda=1.5 (solid), Λ=1\Lambda=1 (dashed), Λ=0.5\Lambda=0.5 (dotted) and Λ=0\Lambda=0 (dash-dotted).

## 8 Conclusion

In this paper, we solved the control problem of identifying the optimal abatement schedule for excess carbon emissions under a diffusion-type carbon budget, where the objective function consists of the expected discounted cumulative emissions together with a reward accrued as long as the carbon budget remains undepleted. We then implemented the proposed numerical procedure to compute the abatement schedule across several concrete examples and compared the results with both the unconstrained solution (i.e., without abatement) and a benchmark policy featuring a simple linear reduction in the consumption rate over time. The results indicate that an optimal policy of gradual reduction in excess consumption entails only a moderate loss in the value function relative to the fully optimal emission schedule, which typically exhibits substantial fluctuations in the emission rate. These findings may inform the design of reduction pathways toward envisaged net-zero targets over fixed time horizons that are easier to implement from both psychological and practical perspectives. The numerical illustrations further reveal that the choice of the reward parameter Λ\Lambda has a significant impact on the resulting value function, while the optimal abatement schedule itself remains relatively robust. An interesting direction for future research is to refine the specification of the objective function for particular applications and to re-examine the associated optimal control problem.

In the numerical illustrations, we also observe that the optimal threshold function z∗​(c)z^{\*}(c) exhibits an inflection point which appears to lie exactly on the line c=μc=\mu for any drift parameter μ≥0\mu\geq 0. We believe this to hold in general and pose it as a conjecture for future research. Furthermore, it can be interesting to see how a relaxation of the ratcheting-down constraint to a drawdown constraint (under which one might still increase the emission rate by a certain percentage of its current value) would influence the results. In the context of dividend optimization, drawdown constraints have been studied as a generalization of ratcheting-up restrictions(cf. Albrecher et al. [[5](https://arxiv.org/html/2601.11348v1#bib.bib5)]), and the resulting analysis proved to be highly non-trivial. We therefore expect that the corresponding analysis in the present setting will be very intricate as well.

## 9 Appendix

Proof of Proposition [3.1](https://arxiv.org/html/2601.11348v1#theorem1a "Proposition 3.1 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"). The proof is an adapted version of the proof of [[4](https://arxiv.org/html/2601.11348v1#bib.bib4), Prop.3.1], tailored to the present situation of down-ratcheting (for self-containedness we give it in its complete form here again). Let us show first that VV is a viscosity supersolution in (0,∞)×[0,c¯)(0,\infty)\times[0,\overline{c}). By Proposition
[2.1](https://arxiv.org/html/2601.11348v1#theorem1 "Proposition 2.1 ‣ 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), ∂cV​(x,c)≥0\partial\_{c}V(x,c)\geq 0 in (0,∞)×[0,c¯)(0,\infty)\times[0,\overline{c}) in the viscosity sense.

Consider (x,c)∈(0,∞)×[0,c¯](x,c)\in(0,\infty)\times[0,\overline{c}] and the
admissible strategy C∈Πx,cSC\in\Pi\_{x,c}^{S}, which emits at constant rate cc up
to the depletion time τ\tau. Let XtCX\_{t}^{C} be the corresponding controlled
surplus process and suppose that there exists a test function φ\varphi for
supersolution ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c),(x,c), then φ≤V\varphi\leq V and
φ​(x,c)=V​(x,c)\varphi(x,c)=V(x,c). We want to prove that ℒc​(φ)​(x,c)≤0\mathcal{L}^{c}\mathcal{(}\varphi)(x,c)\leq 0. For that purpose, we consider an auxiliary test function
for the supersolution φ~\tilde{\varphi} in such a way that φ~≤φ≤V\tilde{\varphi}\leq\varphi\leq V in [0,∞)×[0,c¯][0,\infty)\times[0,\overline{c}],
φ~=φ\tilde{\varphi}=\varphi in [0,2​x]×[0,c¯][0,2x]\times[0,\overline{c}] (so
ℒc​(φ)​(x,c)=ℒc​(φ~)​(x,c)\mathcal{L}^{c}\mathcal{(}\varphi)(x,c)=\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(x,c)) and ℒc​(φ~)​(⋅,c)\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(\cdot,c) is bounded in [0,∞)[0,\infty). We introduce φ~\tilde{\varphi} because
ℒc​(φ)​(⋅,c)\mathcal{L}^{c}\mathcal{(}\varphi)(\cdot,c) could be unbounded in
[0,∞)[0,\infty). We construct φ~\tilde{\varphi} as follows: take g:[0,∞)→[0,1]g:[0,\infty)\rightarrow[0,1] twice continuously differentiable with g=0g=0 in
[2​x+1,∞)[2x+1,\infty) and g=1g=1 in [0,2​x][0,2x], and define φ~​(y,d)=\tilde{\varphi}(y,d)=
φ​(y,d)​g​(y)\varphi(y,d)g(y).
Using Lemma [2.3](https://arxiv.org/html/2601.11348v1#theorem3 "Lemma 2.3 ‣ 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), we obtain for h>0h>0

|  |  |  |
| --- | --- | --- |
|  | φ~​(x,c)=V​(x,c)≥𝔼​[∫0τ∧he−q​s​(c+Λ)​𝑑s]+𝔼​[e−q​(τ∧h)​φ~​(Xτ∧hC,c)]​.\begin{array}[c]{lll}\tilde{\varphi}(x,c)&=&V(x,c)\\ &\geq&\mathbb{E}\left[\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}\,(c+\Lambda)ds\right]+\mathbb{E}\left[e^{-q(\tau\wedge h)}\tilde{\varphi}(X\_{\tau\wedge h}^{C},c)\right]\text{.}\end{array} |  |

Hence, we get, using Itô’s formula,

|  |  |  |
| --- | --- | --- |
|  | 0≥𝔼​[∫0τ∧he−q​s​(c+Λ)​𝑑s]+𝔼​[e−q​(τ∧h)​φ~​(Xτ∧hC,c)−φ~​(x,c)]=𝔼​[∫0τ∧he−q​s​(c+Λ)​𝑑s]+𝔼​[∫0τ∧he−q​s​(σ22​∂x​xφ~​(XsC,c)+∂xφ~​(XsC,c)​(μ−c)−q​φ~​(XsC,c))​𝑑s]+𝔼​[∫0τ∧h∂xφ~​(XsC,c)​σ​d​W​s]=𝔼​[∫0τ∧he−q​s​ℒc​(φ~)​(XsC,c)​𝑑s]​.\begin{array}[c]{lll}0&\geq&\mathbb{E}\left[\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}\,(c+\Lambda)ds\right]+\mathbb{E}\left[e^{-q(\tau\wedge h)}\tilde{\varphi}(X\_{\tau\wedge h}^{C},c)-\tilde{\varphi}(x,c)\right]\\ &=&\mathbb{E}\left[\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}\,(c+\Lambda)ds\right]+\mathbb{E}\left[\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}(\frac{\sigma^{2}}{2}\partial\_{xx}\tilde{\varphi}(X\_{s}^{C},c)+\partial\_{x}\tilde{\varphi}(X\_{s}^{C},c)(\mu-c)-q\tilde{\varphi}(X\_{s}^{C},c))ds\right]\\ &&+\mathbb{E}\left[\int\_{0}^{\tau\wedge h}\partial\_{x}\tilde{\varphi}(X\_{s}^{C},c)\sigma dWs~\right]\\ &=&\mathbb{E}\left[\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(X\_{s}^{C},c)ds\right]\text{.}\end{array} |  |

Since τ>0\tau>0 a.s.,

|  |  |  |
| --- | --- | --- |
|  | |1h​∫0τ∧he−q​s​ℒc​(φ~)​(XsC,c)​𝑑s|≤supy∈[0,∞)|ℒc​(φ~)​(y,c)|,\left|\frac{1}{h}\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(X\_{s}^{C},c)ds\right|\leq\sup\_{y\in[0,\infty)}\left|\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(y,c)\right|, |  |

and

|  |  |  |
| --- | --- | --- |
|  | limh→0+1h​∫0τ∧he−q​s​ℒc​(φ~)​(XsC,c)​𝑑s=ℒ​(φ~)​(x,c)​a.s.;\lim\_{h\rightarrow 0^{+}}\frac{1}{h}\int\nolimits\_{0}^{\tau\wedge h}e^{-q\,s}\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(X\_{s}^{C},c)ds=\mathcal{L(}\tilde{\varphi})(x,c)~\text{a.s.;} |  |

we conclude, using the bounded convergence theorem, that ℒc​(φ)​(x,c)=ℒc​(φ~)​(x,c)≤0\mathcal{L}^{c}\mathcal{(}\varphi)(x,c)=\mathcal{L}^{c}\mathcal{(}\tilde{\varphi})(x,c)\leq 0; so VV is a viscosity supersolution at (x,c)(x,c).

Let us prove now that VV is a viscosity subsolution in (0,∞)×[0,c¯)(0,\infty)\times[0,\overline{c}). Assume first that VV is not a
subsolution of ([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c)∈(0,∞)×(0,c¯]\left(x,c\right)\in(0,\infty)\times(0,\overline{c}]. Then there exist ε>0\varepsilon>0, 0<h<min⁡{x/2,c/2}0<h<\min\left\{x/2,c/2\right\} and a (2,1)-differentiable function ψ\psi with
ψ​(x,c)=V​(x,c)\psi(x,c)=V(x,c) such that ψ≥V\psi\geq V,

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒc​(ψ)​(y,d),−∂cψ​(y,d)}≤−q​ε<0\max\{\mathcal{L}^{c}(\psi)(y,d),-\partial\_{c}\psi(y,d)\}\leq-q\varepsilon<0 |  | (9.1) |

for (y,d)∈\left(y,d\right)\in [x−h,x+h]×[c−h,c][x-h,x+h]\times[c-h,c] and

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(y,d)≤ψ​(y,d)−εV(y,d)\leq\psi(y,d)-\varepsilon |  | (9.2) |

for (y,d)∉[x−h,x+h]×[c−h,c]\left(y,d\right)\notin[x-h,x+h]\times[c-h,c]. Consider
the controlled risk process XtX\_{t} corresponding to an admissible strategy
C∈Πx,cSC\in\Pi\_{x,c}^{S} and define

|  |  |  |
| --- | --- | --- |
|  | τ∗=inf{t>0: ​(Xt,Ct)∉[x−h,x+h]×[c−h,c]}​.\tau^{\ast}=\inf\{t>0:\text{ }\left(X\_{t},C\_{t}\right)\notin[x-h,x+h]\times[c-h,c]\}\text{.} |  |

Since CtC\_{t} is non-increasing and right-continuous, it can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct=c+∫0t𝑑Csc​o−∑Cs<Cs−0≤s≤t(Cs−−Cs),C\_{t}=c+\int\nolimits\_{0}^{t}dC\_{s}^{co}-\sum\_{\begin{subarray}{c}C\_{s}<C\_{s^{-}}\\ 0\leq s\leq t\end{subarray}}(C\_{s^{-}}-C\_{s}), |  | (9.3) |

where Csc​oC\_{s}^{co} is a continuous and non-increasing function.

Take a (2,1)-differentiable function ψ:(0,∞)×[0,c¯]→[0,∞)\psi:(0,\infty)\times[0,\overline{c}]\rightarrow[0,\infty). Note that, by the
mean value theorem, we have in the case Cs<Cs−C\_{s}<C\_{s^{-}} that there
exists cs∈(Cs,Cs−){c}\_{s}\in(C\_{s},C\_{s^{-}}) with

|  |  |  |
| --- | --- | --- |
|  | ψ​(XsC,Cs−)−ψ​(XsC,Cs)=(Cs−−Cs)​∂cψ​(XsC,cs).\psi(X\_{s}^{C},C\_{s^{-}})-\psi(X\_{s}^{C},C\_{s})=(C\_{s^{-}}-C\_{s})\partial\_{c}\psi(X\_{s}^{C},{c}\_{s}). |  |

Using the expression ([9.3](https://arxiv.org/html/2601.11348v1#S9.E3 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) and the change of variables formula
(see for instance [[25](https://arxiv.org/html/2601.11348v1#bib.bib25)]), we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−q​τ∗​ψ​(Xτ∗C,C(τ∗)−)−ψ​(x,c)=∫0τ∗e−q​s​∂xψ​(XsC,Cs−)​(μ−Cs−)​d​s+∫0τ∗e−q​s​∂cψ​(XsC,Cs−)​d​Csc​o−∑Cs<Cs−0≤s<τ∗e−q​s​(Cs−−Cs)​∂cψ​(XsC,cs)+∫0τ∗e−q​s​(−q​ψ​(XsC,Cs−)+σ22​∂x​xψ​(XsC,Cs−))​𝑑s+∫0τ∗e−q​s​∂xψ​(XsC,Cs−)​σ​d​Ws.\begin{array}[c]{l}e^{-q\tau^{\ast}}\psi(X\_{\tau^{\ast}}^{C},C\_{{}^{{}^{{}^{(\tau^{\ast})^{-}}}}})-\psi(x,c)\\ \begin{array}[c]{ll}=&\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}\partial\_{x}\psi(X\_{s}^{C},C\_{s^{-}})(\mu-C\_{s^{-}})ds+\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}\partial\_{c}\psi(X\_{s}^{C},C\_{s^{-}})dC\_{s}^{co}\\ &-\sum\_{\begin{subarray}{c}C\_{s}<C\_{s^{-}}\\ 0\leq s<\tau^{\ast}\end{subarray}}e^{-qs}(C\_{s^{-}}-C\_{s})\partial\_{c}\psi(X\_{s}^{C},{c}\_{s})\\ &+\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}(-q\psi(X\_{s}^{C},C\_{s^{-}})+\frac{\sigma^{2}}{2}\partial\_{xx}\psi(X\_{s}^{C},C\_{s^{-}}))ds+\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}\partial\_{x}\psi(X\_{s}^{C},C\_{s^{-}})\sigma dW\_{s}.\end{array}\end{array} |  | (9.4) |

Hence, using ([9.1](https://arxiv.org/html/2601.11348v1#S9.E1 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) and that cs∈[Cs,Cs−]⊂[c−h,c]c\_{s}\in[C\_{s},C\_{s^{-}}]\subset[c-h,c] for s∈[0,τ∗)s\in[0,\tau^{\ast}), we can write

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[e−q​τ∗​ψ​(Xτ∗C,C(τ∗)−)]−ψ​(x,c)=𝔼​[∫0τ∗e−q​s​ℒCs−​(ψ)​(XsC,Cs−)​𝑑s−∫0τ∗e−q​s​(Cs−+Λ)​𝑑s]+𝔼​[∫0τ∗e−q​s​∂cψ​(XsC,Cs−)​d​Csc−∑Cs≠Cs−0≤s<τ∗e−q​s​(Cs−−Cs)​∂cψ​(XsC,cs)]≤𝔼​[ε​(e−q​τ∗−1)−∫0τ∗e−q​s​(Cs−+Λ)​𝑑s+q​ε​(∫0τ∗e−q​s​𝑑Cs)].\begin{array}[c]{l}\mathbb{E}\left[e^{-q\tau^{\ast}}\psi(X\_{\tau^{\ast}}^{C},C\_{{}^{{}^{{}^{(\tau^{\ast})^{-}}}}})\right]-\psi(x,c)\\ \begin{array}[c]{ll}=&\mathbb{E}\left[\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}\mathcal{L}^{C\_{s^{-}}}(\psi)(X\_{s}^{C},C\_{s^{-}})ds-\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}(C\_{s^{-}}+\Lambda)ds\right]\\ &+\mathbb{E}\left[\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}\partial\_{c}\psi(X\_{s}^{C},C\_{s^{-}})dC\_{s}^{c}-\sum\_{\begin{subarray}{c}C\_{s}\neq C\_{s^{-}}\\ 0\leq s<\tau^{\ast}\end{subarray}}e^{-qs}(C\_{s^{-}}-C\_{s})\partial\_{c}\psi(X\_{s}^{C},c\_{s})\right]\\ \leq&\mathbb{E}\left[\varepsilon\left(e^{-q\tau^{\ast}}-1\right)-\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}(C\_{s^{-}}+\Lambda)ds+q\varepsilon\left(\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}dC\_{s}\right)\right].\end{array}\end{array} |  |

From ([9.2](https://arxiv.org/html/2601.11348v1#S9.E2 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) and using that VV is a function that is non-decreasing in
the second variable as well as that CsC\_{s} is a non-increasing process,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[e−q​τ∗​V​(Xτ∗C,Cτ∗)]≤𝔼[e−q​τ∗(V(Xτ∗C,Cτ∗)−V(Xτ∗C,C(τ∗)−)]+𝔼[ψ(x,c)−e−q​τ∗ε]+𝔼[ψ(Xτ∗C,C(τ∗)−)e−q​τ∗−ψ(x,c)]≤ψ​(x,c)−ε−𝔼​(∫0τ∗e−q​s​(Cs−+Λ)​𝑑s).\begin{array}[c]{l}\mathbb{E}\left[e^{-q\tau^{\ast}}V(X\_{\tau^{\ast}}^{C},C\_{\tau^{\ast}})\right]\\ \begin{array}[c]{cl}\leq&\mathbb{E}\left[e^{-q\tau^{\ast}}\left(V(X\_{\tau^{\ast}}^{C},C\_{\tau^{\ast}})-V(X\_{\tau^{\ast}}^{C},C\_{{}^{{}^{{}^{(\tau^{\ast})^{-}}}}}\right)\right]+\mathbb{E}\left[\psi(x,c)-e^{-q\tau^{\ast}}\varepsilon\right]+\mathbb{E}\left[\psi(X\_{\tau^{\ast}}^{C},C\_{(\tau^{\ast})^{-}})e^{-q\tau^{\ast}}-\psi(x,c)\right]\\ \leq&\psi(x,c)-\varepsilon-\mathbb{E}(\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}(C\_{s^{-}}+\Lambda)ds).\end{array}\end{array} |  |

Hence, using Lemma [2.3](https://arxiv.org/html/2601.11348v1#theorem3 "Lemma 2.3 ‣ 2 Model and basic results ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), we have that

|  |  |  |
| --- | --- | --- |
|  | V​(x,c)=supC∈Πx,cS𝔼​(∫0τ∗e−q​s​(Cs−+Λ)​𝑑s+e−q​τ∗​V​(Xτ∗C,Cτ∗))≤ψ​(x,c)−ε.V(x,c)=\sup\limits\_{C\in\Pi\_{x,c}^{S}}\mathbb{E}\left(\int\nolimits\_{0}^{\tau^{\ast}}e^{-qs}(C\_{s^{-}}+\Lambda)ds+e^{-q\tau^{\ast}}V(X\_{\tau^{\ast}}^{C},C\_{\tau^{\ast}})\right)\leq\psi(x,c)-\varepsilon. |  |

But the latter is a contradiction because we have assumed that V​(x,c)=ψ​(x,c)V(x,c)=\psi(x,c).
When c=0c=0, V​(x,0)V(x,0) solves ℒ0​(V)​(x,0)=0\mathcal{L}^{0}(V)(x,0)=0, which gives the
result. ■\blacksquare

Proof of Lemma [3.2](https://arxiv.org/html/2601.11348v1#theorem2a "Lemma 3.2 ‣ 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target").
A locally Lipschitz function u¯\overline{u} :[0,∞)×[0,c¯]→ℝ:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}} is a viscosity supersolution of
([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c)∈(0,∞)×(0,c¯)(x,c)\in(0,\infty)\times(0,\overline{c}), if any
test function φ\varphi for supersolution at (x,c)(x,c) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒc​(φ)​(x,c),−∂cφ​(x,c)}≤0​,\max\{\mathcal{L}^{c}(\varphi)(x,c),-\partial\_{c}\varphi(x,c)\}\leq 0\text{,} |  | (9.5) |

and a locally Lipschitz function u¯:[0,∞)×[0,c¯]→ℝ\underline{u}:[0,\infty)\times[0,\overline{c}]\rightarrow{\mathbb{R}} is a viscosity subsolution of
([3.6](https://arxiv.org/html/2601.11348v1#S3.E6 "In 3 Hamilton-Jacobi-Bellman equations ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) at (x,c)∈(0,∞)×(0,c¯)(x,c)\in(0,\infty)\times(0,\overline{c}) if any
test function ψ\psi for subsolution at (x,c)(x,c) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒc​(ψ)​(x,c),−∂cψ​(x,c)}≥0.\max\{\mathcal{L}^{c}(\psi)(x,c),-\partial\_{c}\psi(x,c)\}\geq 0. |  | (9.6) |

Suppose that there is a point (x0,c0)∈[0,∞)×(0,c¯)(x\_{0},c\_{0})\in[0,\infty)\times(0,\overline{c}) such that u¯​(x0,c0)−u¯​(x0,c0)>0\underline{u}(x\_{0},c\_{0})-\overline{u}(x\_{0},c\_{0})>0. Let us define h​(c)=1+ec/c¯h(c)=1+e^{{c}/{{\overline{c}}}} and

|  |  |  |
| --- | --- | --- |
|  | u¯s​(x,c)=s​h​(c)​u¯​(x,c)\overline{u}^{s}(x,c)=s\,h(c)\,\overline{u}(x,c) |  |

for any s>1s>1. We have that φ\varphi is a test function for supersolution of
u¯\overline{u} at (x,c)(x,c) if and only if φs=s​h​(c)​φ\varphi^{s}=s\,h(c)\,\varphi is a
test function for supersolution of u¯s\overline{u}^{s} at (x,c)(x,c). By
([9.5](https://arxiv.org/html/2601.11348v1#S9.E5 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) and using 1−s​h​(c)<1−s<0,1-s\,h(c)<1-s<0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒc​(φs)​(x,c)=σ22​s​h​(c)​∂x​xφ​(x,c)+(μ−c)​s​h​(c)​∂xφ​(x,c)−q​s​h​(c)​φ​(x,c)+c+Λ=s​h​(c)​ℒc​(φ)​(x,c)+(c+Λ)​(1−s​h​(c))<0\begin{array}[c]{ccl}\mathcal{L}^{c}(\varphi^{s})(x,c)&=&\frac{\sigma^{2}}{2}\,s\,h(c)\,\partial\_{xx}\varphi\left(x,c\right)+(\mu-c)\,s\;h(c)\,\partial\_{x}\varphi\left(x,c\right)-qs\,h(c)\varphi\left(x,c\right)+c+\Lambda\\ &=&s\,h(c)\,\mathcal{L}^{c}(\varphi)(x,c)+(c+\Lambda)(1-s\,h(c))\\ &<&0\end{array} |  | (9.7) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂cφs​(x,c)≥sc¯​ec/c¯​φ​(x,c)>0\partial\_{c}\varphi^{s}(x,c)\geq\frac{s}{\overline{c}}\,e^{{c}/{\overline{c}}}\varphi(x,c)>0 |  | (9.8) |

for φ​(x,c)>0\varphi(x,c)>0. Take s0>1s\_{0}>1, then u¯​(x0,c0)−u¯s​(x0,c0)>0\underline{u}(x\_{0},c\_{0})-\overline{u}^{s}(x\_{0},c\_{0})>0. We define

|  |  |  |  |
| --- | --- | --- | --- |
|  | M=supx≥0,0≤c≤c¯(u¯​(x,c)−u¯s0​(x,c)).M=\sup\limits\_{x\geq 0,0\leq c\leq\overline{c}}\left(\underline{u}(x,c)-\overline{u}^{s\_{0}}(x,c)\right). |  | (9.9) |

Since limx→∞u¯​(x,c)≤(c¯+Λ)/q≤limx→∞u¯​(x,c)\lim\_{x\rightarrow\infty}\underline{u}(x,c)\leq(\overline{c}+\Lambda)/q\leq\lim\_{x\rightarrow\infty}\overline{u}(x,c), there exists a
b>x0b>x\_{0} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup0≤c≤c¯u¯​(x,c)−u¯s0​(x,c)<0​ for ​x≥b.\sup\limits\_{0\leq c\leq\overline{c}}\underline{u}(x,c)-\overline{u}^{s\_{0}}(x,c)<0\text{ for }x\geq b. |  | (9.10) |

From ([9.10](https://arxiv.org/html/2601.11348v1#S9.E10 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<u¯​(x0,c0)−u¯s0​(x0,c0)≤M:=maxx∈[0,b],0≤c≤c¯⁡(u¯​(x,c)−u¯s0​(x,c)).0<\underline{u}(x\_{0},c\_{0})-\overline{u}^{s\_{0}}(x\_{0},c\_{0})\leq M:=\max\limits\_{x\in\left[0,b\right],0\leq c\leq\overline{c}}\left(\underline{u}(x,c)-\overline{u}^{s\_{0}}(x,c)\right). |  | (9.11) |

Call (x∗,c∗):=arg⁡maxx∈[0,b],0≤c≤c¯⁡(u¯​(x,c)−u¯s0​(x,c))\left(x^{\ast},c^{\ast}\right):=\arg\max\limits\_{x\in\left[0,b\right],0\leq c\leq\overline{c}}\left(\underline{u}(x,c)-\overline{u}^{s\_{0}}(x,c)\right). Let us consider the set

|  |  |  |
| --- | --- | --- |
|  | 𝒜={(x,y,c,d):0≤x≤y≤b​, ​0≤c≤c¯​, ​0≤d≤c¯}\mathcal{A}=\left\{\left(x,y,c,d\right):0\leq x\leq y\leq b\text{, }0\leq\ c\leq\overline{c}\text{, }0\leq d\leq\overline{c}\right\} |  |

and, for all λ>0\lambda>0, the functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φλ​(x,y,c,d)=λ2​(x−y)2+λ2​(c−d)2+2​mλ2​(y−x)+λ,Σλ​(x,y,c,d)=u¯​(x,c)−u¯s0​(y,d)−Φλ​(x,y,c,d).\begin{array}[c]{l}\Phi^{\lambda}\left(x,y,c,d\right)=\dfrac{\lambda}{2}\left(x-y\right)^{2}+\dfrac{\lambda}{2}\left(c-d\right)^{2}+\frac{2m}{\lambda^{2}\left(y-x\right)+\lambda},\\ \Sigma^{\lambda}\left(x,y,c,d\right)=\underline{u}(x,c)-\overline{u}^{s\_{0}}(y,d)-\Phi^{\lambda}\left(x,y,c,d\right).\end{array} |  | (9.12) |

Calling Mλ=maxA⁡ΣλM^{\lambda}=\max\limits\_{A}\Sigma^{\lambda} and
(xλ,yλ,cλ,dλ)=arg⁡maxA⁡Σλ\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)=\arg\max\limits\_{A}\Sigma^{\lambda}, we obtain that

|  |  |  |
| --- | --- | --- |
|  | Mλ≥Σλ​(x∗,x∗,c∗,c∗)=M−2​mλ,M^{\lambda}\geq\Sigma^{\lambda}(x^{\ast},x^{\ast},c^{\ast},c^{\ast})=M-\frac{2m}{\lambda}, |  |

and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infλ→∞Mλ≥M.\liminf\limits\_{\lambda\rightarrow\infty}M^{\lambda}\geq M. |  | (9.13) |

There exists λ0\lambda\_{0} large enough and ss small enough such that if
λ≥λ0\lambda\geq\lambda\_{0}, then (xλ,yλ,cλ,dλ)\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right) ∉∂A\notin\partial A, the proof is similar to the one of
Lemma 4.5 of [[3](https://arxiv.org/html/2601.11348v1#bib.bib3)]. Using the inequality

|  |  |  |
| --- | --- | --- |
|  | Σλ​(xλ,xλ,cλ,cλ)+Σλ​(yλ,yλ,dλ,dλ)≤2​Σλ​(xλ,yλ,cλ,dλ),\Sigma^{\lambda}\left(x\_{\lambda},x\_{\lambda},c\_{\lambda},c\_{\lambda}\right)+\Sigma^{\lambda}\left(y\_{\lambda},y\_{\lambda},d\_{\lambda},d\_{\lambda}\right)\leq 2\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right), |  |

we obtain that

|  |  |  |
| --- | --- | --- |
|  | λ​‖(xλ−yλ,cλ−dλ)‖22≤u¯​(xλ,cλ)−u¯​(yλ,dλ)+u¯s0​(xλ,cλ)−u¯s0​(yλ,dλ)+4​m​(yλ−xλ).\lambda\left\|(x\_{\lambda}-y\_{\lambda},c\_{\lambda}-d\_{\lambda})\right\|\_{2}^{2}\leq\underline{u}(x\_{\lambda},c\_{\lambda})-\underline{u}(y\_{\lambda},d\_{\lambda})+\overline{u}^{s\_{0}}(x\_{\lambda},c\_{\lambda})-\overline{u}^{s\_{0}}(y\_{\lambda},d\_{\lambda})+4m(y\_{\lambda}-x\_{\lambda}). |  |

Consequently

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​‖(xλ−yλ,cλ−dλ)‖22≤6​m​‖(xλ−yλ,cλ−dλ)‖2.\lambda\left\|(x\_{\lambda}-y\_{\lambda},c\_{\lambda}-d\_{\lambda})\right\|\_{2}^{2}\leq 6m\left\|(x\_{\lambda}-y\_{\lambda},c\_{\lambda}-d\_{\lambda})\right\|\_{2}. |  | (9.14) |

We can find a sequence λn→∞\lambda\_{n}\rightarrow\infty such that (xλn,yλn,cλn,dλn)→(x^,y^,c^,d^)∈A\left(x\_{\lambda\_{n}},y\_{\lambda\_{n}},c\_{\lambda\_{n}},d\_{\lambda\_{n}}\right)\rightarrow\left(\widehat{x},\widehat{y},\widehat{c},\widehat{d}\right)\in A. From ([9.14](https://arxiv.org/html/2601.11348v1#S9.E14 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(xλn−yλn,cλn−dλn)‖2≤6​m/λn,\left\|(x\_{\lambda\_{n}}-y\_{\lambda\_{n}},c\_{\lambda\_{n}}-d\_{\lambda\_{n}})\right\|\_{2}\leq 6m/\lambda\_{n}, |  | (9.15) |

which gives x^=y^\widehat{x}=\widehat{y} and c^=d^\widehat{c}=\widehat{d}.

Since Σλ​(x,y,c,d)=u¯​(x,c)−u¯s0​(y,d)−Φλ​(x,y,c,d)\Sigma^{\lambda}\left(x,y,c,d\right)=\underline{u}(x,c)-\overline{u}^{s\_{0}}(y,d)-\Phi^{\lambda}\left(x,y,c,d\right) reaches the maximum
in (xλ,yλ,cλ,dλ)\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\ in the
interior of the set A,A, the function

|  |  |  |
| --- | --- | --- |
|  | ψ​(x,c)=Φλ​(x,yλ,c,dλ)−Φλ​(xλ,yλ,cλ,dλ)+u¯​(xλ,cλ)\psi(x,c)=\Phi^{\lambda}\left(x,y\_{\lambda},c,d\_{\lambda}\right)-\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)+\underline{u}\left(x\_{\lambda},c\_{\lambda}\right) |  |

is a test for subsolution for u¯\underline{u} of the HJB equation at the point
(xλ,cλ)\left(x\_{\lambda},c\_{\lambda}\right).

In addition, the function

|  |  |  |
| --- | --- | --- |
|  | φs0​(y,d)=−Φλ​(xλ,y,cλ,d)+Φλ​(xλ,yλ,cλ,dλ)+u¯s0​(yλ,dλ)\varphi^{s\_{0}}(y,d)=-\Phi^{\lambda}\left(x\_{\lambda},y,c\_{\lambda},d\right)+\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)+\overline{u}^{s\_{0}}\left(y\_{\lambda},d\_{\lambda}\right) |  |

is a test for supersolution for u¯s0\overline{u}^{s\_{0}} at (yλ,dλ)\left(y\_{\lambda},d\_{\lambda}\right) and so

|  |  |  |
| --- | --- | --- |
|  | ∂cφs0​(yλ,dλ)≥s0c¯​φ​(yλ,dλ)​ec/c¯>0,\partial\_{c}\varphi^{s\_{0}}(y\_{\lambda},d\_{\lambda})\geq\frac{s\_{0}}{\overline{c}}\varphi(y\_{\lambda},d\_{\lambda})e^{{c}/{\overline{c}}}>0, |  |

using yλ>0y\_{\lambda}>0. Consequently, ∂cψ​(xλ,cλ)=∂cφs0​(yλ,dλ)>0\partial\_{c}\psi(x\_{\lambda},c\_{\lambda})=\partial\_{c}\varphi^{s\_{0}}(y\_{\lambda},d\_{\lambda})>0, and so we have ℒcλ​(ψ)​(xλ,cλ)≥0.\mathcal{L}^{c\_{\lambda}}(\psi)(x\_{\lambda},c\_{\lambda})\geq 0.

Assume first that the functions u¯​(x,c)\underline{u}(x,c) and u¯s0​(y,d)\overline{u}^{s\_{0}}(y,d) are (2,1)-differentiable at (xλ,cλ)(x\_{\lambda},c\_{\lambda})\ and
(yλ,dλ)(y\_{\lambda},d\_{\lambda}) respectively. Since Σλ\Sigma^{\lambda} defined in
([9.12](https://arxiv.org/html/2601.11348v1#S9.E12 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) reaches a local maximum at (xλ,yλ,cλ,dλ)\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right) ∉∂A\notin\partial A,
we have that

|  |  |  |
| --- | --- | --- |
|  | ∂xΣλ​(xλ,yλ,cλ,dλ)=∂yΣλ​(xλ,yλ,cλ,dλ)=0\partial\_{x}\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)=\partial\_{y}\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)=0 |  |

and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂xu¯​(xλ,cλ)=∂xΦλ​(xλ,yλ,cλ,dλ)=λ​(xλ−yλ)+2​m(λ​(yλ−xλ)+1)2=−∂yΦλ​(xλ,yλ,cλ,dλ)=∂xu¯s0​(yλ,dλ).\begin{array}[c]{lll}\partial\_{x}\underline{u}(x\_{\lambda},c\_{\lambda})&=&\partial\_{x}\Phi^{\lambda}(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})\\ &=&\lambda\left(x\_{\lambda}-y\_{\lambda}\right)+\frac{2m}{\left(\lambda\left(y\_{\lambda}-x\_{\lambda}\right)+1\right)^{2}}\\ &=&-\partial\_{y}\Phi^{\lambda}(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})=\partial\_{x}\overline{u}^{s\_{0}}(y\_{\lambda},d\_{\lambda}).\end{array} |  | (9.16) |

Defining A=∂x​xu¯​(xλ,cλ)A=\partial\_{xx}\underline{u}(x\_{\lambda},c\_{\lambda}) and
B=∂x​xu¯s0​(yλ,dλ)B=\partial\_{xx}\overline{u}^{s\_{0}}(y\_{\lambda},d\_{\lambda}), we obtain

|  |  |  |
| --- | --- | --- |
|  | (∂x​xΣλ​(xλ,yλ,cλ,dλ)∂x​yΣλ​(xλ,yλ,cλ,dλ)∂x​yΣλ​(xλ,yλ,cλ,dλ)∂y​yΣλ​(xλ,yλ,cλ,dλ))=(A−∂x​xΦλ​(xλ,yλ,cλ,dλ)−∂x​yΦλ​(xλ,yλ,cλ,dλ)−∂x​yΦλ​(xλ,yλ,cλ,dλ)−B−∂y​yΦλ​(xλ,yλ,cλ,dλ))≤0.\begin{array}[c]{l}\left(\begin{array}[c]{ll}\partial\_{xx}\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)&\partial\_{xy}\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\\ \partial\_{xy}\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)&\partial\_{yy}\Sigma^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\end{array}\right)\\ \vskip 6.0pt plus 2.0pt minus 2.0pt=\left(\begin{array}[c]{ll}A-\partial\_{xx}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)&-\partial\_{xy}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\\ -\partial\_{xy}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)&-B-\partial\_{yy}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\end{array}\right)\leq 0.\end{array} |  |

It is hence a negative semi-definite matrix, and

|  |  |  |
| --- | --- | --- |
|  | (A00−B)≤H​(Φλ)​(xλ,yλ,cλ,dλ):=(∂x​xΦλ​(xλ,yλ,cλ,dλ)∂x​yΦλ​(xλ,yλ,cλ,dλ)∂x​yΦλ​(xλ,yλ,cλ,dλ)∂y​yΦλ​(xλ,yλ,cλ,dλ)).\begin{pmatrix}A&0\\ 0&-B\end{pmatrix}\leq H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}):=\left(\begin{array}[c]{ll}\partial\_{xx}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)&\partial\_{xy}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\\ \partial\_{xy}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)&\partial\_{yy}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\end{array}\right). |  |

In the case that u¯​(x,c)\underline{u}(x,c) and u¯s0​(y,d)\overline{u}^{s\_{0}}(y,d) are not
(2,1)-differentiable at (xλ,cλ)\left(x\_{\lambda},c\_{\lambda}\right)\ and
(yλ,dλ)(y\_{\lambda},d\_{\lambda}), respectively, we can resort to a more general
theorem to get a similar result. Using Theorem 3.2 of Crandall, Ishii and
Lions [[17](https://arxiv.org/html/2601.11348v1#bib.bib17)], it can be proved that for any δ>0\delta>0
there exist real numbers AδA\_{\delta} and BδB\_{\delta} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Aδ00−Bδ)≤H​(Φλ)​(xλ,yλ,cλ,dλ)+δ​(H​(Φλ)​(xλ,yλ,cλ,dλ))2\begin{pmatrix}A\_{\delta}&0\\ 0&-B\_{\delta}\end{pmatrix}\leq H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})+\delta\left(H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})\right)^{2} |  | (9.17) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ22​Aδ+(μ−cλ)​∂xψ​(xλ,cλ)−q​ψ​(xλ,cλ)+cλ+Λ≥0,σ22​Bδ+(μ−dλ)​∂xφs0​(yλ,dλ)−q​φs0​(yλ,dλ)+dλ+Λ≤0.\begin{array}[c]{c}\frac{\sigma^{2}}{2}A\_{\delta}+(\mu-c\_{\lambda})\partial\_{x}\psi(x\_{\lambda},c\_{\lambda})-q\psi(x\_{\lambda},c\_{\lambda})+c\_{\lambda}+\Lambda\geq 0,\\ \frac{\sigma^{2}}{2}B\_{\delta}+(\mu-d\_{\lambda})\partial\_{x}\varphi^{s\_{0}}(y\_{\lambda},d\_{\lambda})-q\varphi^{s\_{0}}(y\_{\lambda},d\_{\lambda})+d\_{\lambda}+\Lambda\leq 0.\end{array} |  | (9.18) |

The expression ([9.17](https://arxiv.org/html/2601.11348v1#S9.E17 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) implies that Aδ−Bδ≤0A\_{\delta}-B\_{\delta}\leq 0 because

|  |  |  |
| --- | --- | --- |
|  | H​(Φλ)​(xλ,yλ,cλ,dλ)=∂x​xΦλ​(xλ,yλ,cλ,dλ)​(1−1−11)H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})=\partial\_{xx}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\begin{pmatrix}1&-1\\ -1&1\end{pmatrix} |  |

and

|  |  |  |
| --- | --- | --- |
|  | (H​(Φλ)​(xλ,yλ,cλ,dλ))2=2​(∂x​xΦλ​(xλ,yλ,cλ,dλ))2​(1−1−11).\left(H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})\right)^{2}=2\left(\partial\_{xx}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)\right)^{2}\begin{pmatrix}1&-1\\ -1&1\end{pmatrix}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | Aδ−Bδ=(11)​(Aδ00−Bδ)​(11)≤(11)​(H​(Φλ)​(xλ,yλ,cλ,dλ)+δ​(H​(Φλ)​(xλ,yλ,cλ,dλ))2)​(11)=0.\begin{array}[c]{lll}A\_{\delta}-B\_{\delta}&=&\begin{pmatrix}1&1\end{pmatrix}\left(\begin{array}[c]{cc}A\_{\delta}&0\\ 0&-B\_{\delta}\end{array}\right)\left(\begin{array}[c]{c}1\\ 1\end{array}\right)\\ &\leq&\begin{pmatrix}1&1\end{pmatrix}\left(H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})+\delta\left(H\left(\Phi^{\lambda}\right)(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda})\right)^{2}\right)\left(\begin{array}[c]{c}1\\ 1\end{array}\right)\\ &=&0.\end{array} |  |

And so, since φs0​(yλ,dλ)=u¯s0​(yλ,dλ)\varphi^{s\_{0}}\left(y\_{\lambda},d\_{\lambda}\right)=\overline{u}^{s\_{0}}\left(y\_{\lambda},d\_{\lambda}\right), ψ​(xλ,cλ)=u¯​(xλ,cλ)\psi(x\_{\lambda},c\_{\lambda})=\underline{u}(x\_{\lambda},c\_{\lambda}) and

|  |  |  |
| --- | --- | --- |
|  | ∂xφs0​(yλ,dλ)=−∂yΦλ​(xλ,yλ,cλ,dλ)=∂xΦλ​(xλ,yλ,cλ,dλ)=∂xψ​(xλ,cλ),\partial\_{x}\varphi^{s\_{0}}\left(y\_{\lambda},d\_{\lambda}\right)=-\partial\_{y}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)=\partial\_{x}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right)=\partial\_{x}\psi(x\_{\lambda},c\_{\lambda}), |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯​(xλ,cλ)−u¯s0​(yλ,dλ)=ψ​(xλ,cλ)−φs0​(yλ,dλ)≤σ22​q​(Aδ−Bδ)+(cλq−dλq)​(1−∂xΦλ​(xλ,yλ,cλ,dλ))≤(cλq−dλq)​(1−λ​(xλ−yλ)−2​m(λ​(yλ−xλ)+1)2).\begin{array}[c]{lll}\underline{u}(x\_{\lambda},c\_{\lambda})-\overline{u}^{s\_{0}}\left(y\_{\lambda},d\_{\lambda}\right)&=&\psi(x\_{\lambda},c\_{\lambda})-\varphi^{s\_{0}}\left(y\_{\lambda},d\_{\lambda}\right)\\ &\leq&\frac{\sigma^{2}}{2q}(A\_{\delta}-B\_{\delta})\\ &&+\left(\frac{c\_{\lambda}}{q}-\frac{d\_{\lambda}}{q}\right)(1-\partial\_{x}\Phi^{\lambda}\left(x\_{\lambda},y\_{\lambda},c\_{\lambda},d\_{\lambda}\right))\\ &\leq&\left(\frac{c\_{\lambda}}{q}-\frac{d\_{\lambda}}{q}\right)\left(1-\lambda\left(x\_{\lambda}-y\_{\lambda}\right)-\frac{2m}{\left(\lambda\left(y\_{\lambda}-x\_{\lambda}\right)+1\right)^{2}}\right).\end{array} |  | (9.19) |

Hence, from ([9.15](https://arxiv.org/html/2601.11348v1#S9.E15 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")) and ([9.13](https://arxiv.org/html/2601.11348v1#S9.E13 "In 9 Appendix ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | <M≤lim infλ→∞Mλ≤limn→∞Mλn=limn→∞Σλn​(xλn,yλn,cλn,dλn)=u¯​(x^,c^)−u¯s0​(x^,c^)\displaystyle<M\leq\liminf\limits\_{\lambda\rightarrow\infty}M\_{\lambda}\leq\lim\limits\_{{}\_{n\rightarrow\infty}}M\_{\lambda\_{n}}=\lim\limits\_{{}\_{n\rightarrow\infty}}\Sigma^{\lambda\_{n}}(x\_{\lambda\_{n}},y\_{\lambda\_{n}},c\_{\lambda\_{n}},d\_{\lambda\_{n}})=\underline{u}(\widehat{x},\widehat{c})-\overline{u}^{s\_{0}}(\widehat{x},\widehat{c}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤limn⟶∞(cλnq−dλnq)​(1−λn​(xλn−yλn)−2​m(λn​(yλn−xλn)+1)2)\displaystyle\leq\lim\_{n\longrightarrow\infty}\left(\frac{c\_{\lambda\_{n}}}{q}-\frac{d\_{\lambda\_{n}}}{q}\right)(1-\lambda\_{n}\left(x\_{\lambda\_{n}}-y\_{\lambda\_{n}}\right)-\frac{2m}{\left(\lambda\_{n}\left(y\_{\lambda\_{n}}-x\_{\lambda\_{n}}\right)+1\right)^{2}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤.limn⟶∞|cλnq−dλnq|(1+λn∥(xλn−yλn,cλn−dλn)∥2+2​m(λn​(yλn−xλn)+1)2)\displaystyle\leq.\lim\_{n\longrightarrow\infty}\left|\frac{c\_{\lambda\_{n}}}{q}-\frac{d\_{\lambda\_{n}}}{q}\right|(1+\lambda\_{n}\left\|(x\_{\lambda\_{n}}-y\_{\lambda\_{n}},c\_{\lambda\_{n}}-d\_{\lambda\_{n}})\right\|\_{2}+\frac{2m}{\left(\lambda\_{n}\left(y\_{\lambda\_{n}}-x\_{\lambda\_{n}}\right)+1\right)^{2}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤limn⟶∞|cλnq−dλnq|​(1+8​m)=0.\displaystyle\leq\lim\_{n\longrightarrow\infty}\left|\frac{c\_{\lambda\_{n}}}{q}-\frac{d\_{\lambda\_{n}}}{q}\right|(1+8m)=0. |  |

This is a contradiction and so we get the result. ■\blacksquare

Proof of Theorem [6.2](https://arxiv.org/html/2601.11348v1#theorem2d "Theorem 6.2 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"). By definition Wz∗​(⋅,0)=Vc0.W^{z^{\ast}}(\cdot,0)=V^{c\_{0}}. Assuming that Wz∗​(⋅,ck)=VckW^{z^{\ast}}(\cdot,c\_{k})=V^{c\_{k}} for k=1,…,i−1k=1,...,i-1, by Theorem
[4.1](https://arxiv.org/html/2601.11348v1#theorem1b "Theorem 4.1 ‣ 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), it is enough to prove that Wz∗​(⋅,ci)W^{z^{\ast}}(\cdot,c\_{i}) is a viscosity solution of ([4.2](https://arxiv.org/html/2601.11348v1#S4.E2 "In 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target")). Since
by construction Vci−1−Wz∗​(⋅,ci)≤0V^{c\_{i-1}}-W^{z^{\ast}}(\cdot,c\_{i})\leq 0 and Vci−1​(x)−Wz∗​(x,ci)=0V^{c\_{i-1}}(x)-W^{z^{\ast}}(x,c\_{i})=0 for x≤z∗​(ci)x\leq z^{\ast}(c\_{i}), it remains to be
seen that ℒci​(Wz∗)​(x,ci)≤0\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(x,c\_{i})\leq 0 for x≤z∗​(ci)x\leq z^{\ast}(c\_{i}). By Remark [6.1](https://arxiv.org/html/2601.11348v1#S6.Thmremark1 "Remark 6.1 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), Wz∗​(⋅,ci)W^{z^{\ast}}(\cdot,c\_{i}) is continuously differentiable and it is piecewise infinitely
differentiable in open intervals in which it solves ℒcj​(Wz∗)​(x,ci)=0\mathcal{L}^{c\_{j}}(W^{z^{\ast}})(x,c\_{i})=0 for some j≤ij\leq i. Let us consider first the case
in which x≠z∗​(ck)x\neq z^{\ast}(c\_{k}) for k=1,..,i−1k=1,..,i-1, so xx belongs to one of
these open intervals. Hence,

|  |  |  |
| --- | --- | --- |
|  | ℒci​(Wz∗)​(x,ci)=ℒcj​(Wz∗)​(x,ci)+(ci−cj)​(1−∂xWz∗​(x,ci))=(ci−cj)​(1−∂xWz∗​(x,ci))≤0\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(x,c\_{i})=\mathcal{L}^{c\_{j}}(W^{z^{\ast}})(x,c\_{i})+(c\_{i}-c\_{j})(1-\partial\_{x}W^{z^{\ast}}(x,c\_{i}))=(c\_{i}-c\_{j})(1-\partial\_{x}W^{z^{\ast}}(x,c\_{i}))\leq 0 |  |

if and only if ∂xWz∗​(x,ci)≥1\partial\_{x}W^{z^{\ast}}(x,c\_{i})\geq 1. Let us prove the
result first for x=z∗​(ci)≠z∗​(ck)x=z^{\ast}(c\_{i})\neq z^{\ast}(c\_{k}) for k=1,..,i−1k=1,..,i-1.
That is, there exists δ>0\delta>0 and some j<ij<i such that ℒcj​(Wz∗)​(x,ci)=0\mathcal{L}^{c\_{j}}(W^{z^{\ast}})(x,c\_{i})=0 in (z∗​(ci)−δ,z∗​(ci))(z^{\ast}(c\_{i})-\delta,z^{\ast}(c\_{i})) and then

|  |  |  |
| --- | --- | --- |
|  | ℒcj​(Wz∗)​(z∗​(ci)−,ci)=0​, ​ℒci​(Wz∗)​(z∗​(ci)+,ci)=0,\mathcal{L}^{c\_{j}}(W^{z^{\ast}})(z^{\ast}(c\_{i})^{-},c\_{i})=0\text{, }\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(z^{\ast}(c\_{i})^{+},c\_{i})=0, |  |

so

|  |  |  |
| --- | --- | --- |
|  | 0=ℒci​(Wz∗)​(z∗​(ci)+,ci)−ℒcj​(Wz∗)​(z∗​(ci)−,ci)=σ22​(∂x​xWz∗​(z∗​(ci)+,ci)−∂x​xWz∗​(z∗​(ci)−,ci))+(ci−cj)​(1−∂xWz∗​(z∗​(ci),ci)).\begin{array}[c]{lll}0&=&\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(z^{\ast}(c\_{i})^{+},c\_{i})-\mathcal{L}^{c\_{j}}(W^{z^{\ast}})(z^{\ast}(c\_{i})^{-},c\_{i})\\ &=&\frac{\sigma^{2}}{2}(\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{+},c\_{i})-\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{-},c\_{i}))\\ &&+(c\_{i}-c\_{j})(1-\partial\_{x}W^{z^{\ast}}(z^{\ast}(c\_{i}),c\_{i})).\end{array} |  |

By Remark [6.1](https://arxiv.org/html/2601.11348v1#S6.Thmremark1 "Remark 6.1 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), ∂x​xWz∗​(z∗​(ci)+,ci)−∂x​xWz∗​(z∗​(ci)−,ci)≥0\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{+},c\_{i})-\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{i})^{-},c\_{i})\geq 0
and ci−cj>0,c\_{i}-c\_{j}>0, and we can conclude that ∂xWz∗(z∗(ci),ci))≥1\partial\_{x}W^{z^{\ast}}(z^{\ast}(c\_{i}),c\_{i}))\geq 1. It remains to prove that ∂xWz∗​(x,ci)≥1\partial\_{x}W^{z^{\ast}}(x,c\_{i})\geq 1 for x<z∗​(ci).x<z^{\ast}(c\_{i}).

If i=1i=1, by definition Wz∗​(x,c1)=Wz∗​(x,0)=Λq​(1−eθ1​(0)​x)W^{z^{\ast}}(x,c\_{1})=W^{z^{\ast}}(x,0)=\frac{\Lambda}{q}\left(1-e^{\theta\_{1}(0)x}\right) for x≤z∗​(c1)x\leq z^{\ast}(c\_{1}). By Remark [6.2](https://arxiv.org/html/2601.11348v1#S6.Thmremark2 "Remark 6.2 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), Wz∗​(⋅,0)W^{z^{\ast}}(\cdot,0) is concave and
so ∂xWz∗​(x,c1)=∂xWz∗​(x,0)≥∂xWz∗​(z∗​(c1),0)≥1\partial\_{x}W^{z^{\ast}}(x,c\_{1})=\partial\_{x}W^{z^{\ast}}(x,0)\geq\partial\_{x}W^{z^{\ast}}(z^{\ast}(c\_{1}),0)\geq 1 for x≤z∗​(c1)x\leq z^{\ast}(c\_{1});
hence we have the result. We need to prove now that ∂xWz∗​(x,ci)=∂xWz∗​(x,ci−1)≥1\partial\_{x}W^{z^{\ast}}(x,c\_{i})=\partial\_{x}W^{z^{\ast}}(x,c\_{i-1})\geq 1 for x<z∗​(ci)x<z^{\ast}(c\_{i})
and i>1.i>1. By the induction hypothesis, we know that ∂xWz∗​(x,ci−1)≥1\partial\_{x}W^{z^{\ast}}(x,c\_{i-1})\geq 1 for x≤z∗​(ci−1)x\leq z^{\ast}(c\_{i-1}). In the case that z∗​(ci)≤z∗​(ci−1),z^{\ast}(c\_{i})\leq z^{\ast}(c\_{i-1}), it is straightforward because x≤z∗​(ci)≤z∗​(ci−1)x\leq z^{\ast}(c\_{i})\leq z^{\ast}(c\_{i-1}) implies

|  |  |  |
| --- | --- | --- |
|  | ∂xWz∗​(x,ci)=∂xWz∗​(x,ci−1)≥1.\partial\_{x}W^{z^{\ast}}(x,c\_{i})=\partial\_{x}W^{z^{\ast}}(x,c\_{i-1})\geq 1. |  |

In the case that z∗​(ci)>z∗​(ci−1)z^{\ast}(c\_{i})>z^{\ast}(c\_{i-1}), it is enough to prove it
for x∈(z∗​(ci−1),z∗​(ci))x\in(z^{\ast}(c\_{i-1}),z^{\ast}(c\_{i})). Note that Wz∗​(x,ci)=Wz∗​(x,ci−1)W^{z^{\ast}}(x,c\_{i})=W^{z^{\ast}}(x,c\_{i-1}) for x∈(z∗​(ci−1),z∗​(ci))x\in(z^{\ast}(c\_{i-1}),z^{\ast}(c\_{i})), and Wz∗​(⋅,ci−1)W^{z^{\ast}}(\cdot,c\_{i-1}) is a solution of ℒci−1=0\mathcal{L}^{c\_{i-1}}=0 in [z∗​(ci−1),∞)[z^{\ast}(c\_{i-1}),\infty) with limx→∞Wz∗​(0,ci−1)=ci−1+Λq\lim\_{x\rightarrow\infty}{W^{z^{\ast}}(0,c\_{i-1})}=\frac{c\_{i-1}+\Lambda}{q}; so, by Remark
[6.2](https://arxiv.org/html/2601.11348v1#S6.Thmremark2 "Remark 6.2 ‣ 6 Optimal strategies for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), ∂xWz∗​(x,ci)\partial\_{x}W^{z^{\ast}}(x,c\_{i}) is decreasing in
the interval (z∗​(ci−1),z∗​(ci))(z^{\ast}(c\_{i-1}),z^{\ast}(c\_{i})). But ∂xWz∗​(z∗​(ci),ci)≥1\partial\_{x}W^{z^{\ast}}(z^{\ast}(c\_{i}),c\_{i})\geq 1, so we have the result.

Consider now the case x=z∗​(cj)x=z^{\ast}(c\_{j}) with j≤i−1j\leq i-1 and z∗​(cj)≤z∗​(ci)z^{\ast}(c\_{j})\leq z^{\ast}(c\_{i}). It could be the case that Wz∗​(x,ci)W^{z^{\ast}}(x,c\_{i}) is not twice
continuously differentiable at z∗​(cj),z^{\ast}(c\_{j}), so we prove that
ℒci​(Wz∗)​(z∗​(cj),ci)≤0\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(z^{\ast}(c\_{j}),c\_{i})\leq 0 in the
viscosity sense. Take a test function φ\varphi for supersolution at z∗​(cj).z^{\ast}(c\_{j}). From Definition [4.1](https://arxiv.org/html/2601.11348v1#S4.Thmdefinition1 "Definition 4.1 ‣ 4 Hamilton-Jacobi-Bellman equations for finite sets ‣ Optimal Abatement Schedules for Excess Carbon Emissions Towards a Net-Zero Target"), φ′​(z∗​(cj))=∂xWz∗​(z∗​(cj),ci)\varphi^{\prime}(z^{\ast}(c\_{j}))=\partial\_{x}W^{z^{\ast}}(z^{\ast}(c\_{j}),c\_{i}) and

|  |  |  |
| --- | --- | --- |
|  | φ′′​(z∗​(cj))≤min⁡{∂x​xWz∗​(z∗​(cj)+,ci),∂x​xWz∗​(z∗​(cj)−,ci)}.\varphi^{\prime\prime}(z^{\ast}(c\_{j}))\leq\min\{\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{j})^{+},c\_{i}),\partial\_{xx}W^{z^{\ast}}(z^{\ast}(c\_{j})^{-},c\_{i})\}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ℒci​(φ)​(z∗​(cj),ci)≤min⁡{ℒci​(Wz∗)​(z∗​(cj)+,ci),ℒci​(Wz∗)​(z∗​(cj)−,ci)},\mathcal{L}^{c\_{i}}(\varphi)(z^{\ast}(c\_{j}),c\_{i})\leq\min\{\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(z^{\ast}(c\_{j})^{+},c\_{i}),\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(z^{\ast}(c\_{j})^{-},c\_{i})\}, |  |

and since we already proved that ℒci​(Wz∗)​(⋅,ci)≤0\mathcal{L}^{c\_{i}}(W^{z^{\ast}})(\cdot,c\_{i})\leq 0 in (z∗​(cj)−δ,z∗​(cj))∪\left(z^{\ast}(c\_{j})-\delta,z^{\ast}(c\_{j})\right)\cup
(z∗​(cj),z∗​(cj)+δ)\left(z^{\ast}(c\_{j}),z^{\ast}(c\_{j})+\delta\right) for some δ>0,\delta>0,
we get the result by continuity. ■\blacksquare

## References

* [1]
  Aïd, R. and Biagini, S. (2023). Optimal dynamic regulation of carbon emissions market. Mathematical Finance 33, 1, 80–115.
* [2]
  Aïd, R. and Biagini, S. (2025). Stochastic carbon regulation in continuous time. In: Handbook of Quantitative Sustainable Finance, pp. 449-473, Chapman and Hall/CRC.
* [3]
  Albrecher, H., Azcue, P. and Muler, N. (2020), Optimal ratcheting
  of dividends in insurance.SIAM Journal on Control and Optimization,
  58, 4, 1822–1845.
* [4]
  Albrecher, H., Azcue, P. and Muler, N. (2022), Optimal
  ratcheting of dividends in a Brownian risk model. SIAM Journal
  on Financial Mathematics, 13, 3, 657–701.
* [5]
   Albrecher, H., Azcue, P., and Muler, N. (2023). Optimal dividends under a drawdown constraint and a curious square-root rule. Finance and Stochastics 27(2), 341-400.
* [6]
  Albrecher, H. and Zhu, J. (2025), On effects of present-bias on carbon emission patterns towards a net zero target.Preprint, arXiv:2510.27384.
* [7]
  Angoshtari, B., Bayraktar, E. and Young, V.R. (2019) Optimal
  dividend distribution under drawdown and ratcheting constraints on dividend
  rates. SIAM Journal on Financial Mathematics 10, 2, 547–577.
* [8]
  Angoshtari, B., Bayraktar, E. and Young, V.R. (2023) Optimal
  consumption under a habit-formation constraint: the deterministic case. SIAM Journal on Financial Mathematics, 14, 2, 557–597.
* [9]
  Azcue P. and Muler N. (2014). Stochastic
  Optimization in Insurance: a Dynamic Programming Approach. Springer Briefs in
  Quantitative Finance. Springer.
* [10]
  Albrecher, H. and Thonhauser, S. (2009). Optimality results for dividend problems in insurance. RACSAM - Revista de la Real Academia de Ciencias Exactas, Fisicas y Naturales. Serie A. Matematicas, 103, 2, 295–320.
* [11]
  Biagini, S. (2025). Carbon neutrality and net-zero regulation. SIAM Journal on Financial Mathematics 16, 3, 1028–1057.
* [12]
  Borissov, K. and Bretschger, L. (2022). Optimal carbon policies in a dynamic heterogeneous
  world. European Economic Review, 148:104253.
* [13]
  Bourgey, F., Gobet, E. and Jiao, Y. (2024). Bridging socioeconomic pathways of CO2 emission
  and credit risk. Annals of Operations Research, 336, 1, 1197–1218.
* [14]
  Chekriy, K., Kiesel, R. and Stahl, G. (2025). Probabilistic assessment of corporate net-zero
  transition. Available at SSRN 5255705.
* [15]
  Chen, X., Dong, Y., Huang, W. and Liang, J. (2024). Optimal Carbon Emission Control With Allowances Purchasing. arXiv preprint arXiv:2407.08477.
* [16]
   Colaneri, K., Frey, R., and Köck, V. (2024). Random carbon tax policy and investment into emission abatement technologies. arXiv preprint arXiv:2406.01088.
* [17]
  Crandall, M. G., Ishii, H. and Lions, P. L.
  (1992). User’s guide to viscosity solutions of second order partial
  differential equations. Bull. Amer. Math. Soc. (N.S.) 27, 1–67.
* [18]
  Claisse, J., Talay, D. and Tan, X. (2016), A pseudo-Markov
  property for controlled diffusion processes, SIAM Journal on Control Optimization, 54, 1017–1029.
* [19]
  Elie, R. and Touzi, N. (2008). Optimal lifetime consumption and
  investment under a drawdown constraint. Finance and Stochastics
  12, 3, 299–330.
* [20]
  Guan, C. and Quan Xu, Q. X. (2024). Optimal ratcheting of dividend payout
  under Brownian motion surplus. SIAM Journal on Control and
  Optimization 62, 5, 2590–2620.
* [21]
  Huang, W., Liang, J. and Dong, Y. (2023). Optimal stochastic control problem for a carbon emission reduction process. SIAM Journal on Applied Mathematics 83,3, 1272–1295.
* [22]
  Korn, R. (2025). A framework for optimal portfolios with sustainable assets and climate scenarios.
  European Actuarial Journal 15, 1, 1–13.
* [23]
  Korn, R. and Nurkanovic, A. (2025). Sustainable portfolio optimization and sustainable taxation.
  European Actuarial Journal, to appear.
* [24]
  Popovski, V. (2018). The implementation of the Paris agreement on climate change. Routledge, London.
* [25]
  Protter, P. (1992). Stochastic integration and
  differential equations. Springer Verlag, Berlin.
* [26]
  Saleh, H., Battiston, S., Monasterolo, I., Barreau, T. and Tankov, P. (2025). Estimating firms’
  emissions from asset level data helps revealing (mis)alignment to net zero targets. Available at SSRN 4661050.
* [27]
   Thonhauser, S. and Albrecher, H. (2007). Dividend maximization under consideration of the time value of ruin. Insurance: Mathematics and Economics, 41(1), 163-184.
* [28]
  Wijk, L.V. (2024). On Stochastic Control Theory for Dynamic Carbon Emission Reduction. Master Thesis, University of Utrecht.