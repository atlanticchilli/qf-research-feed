---
authors:
- Gabriel D. Patrón
- Di Zhang
- Lavinia M. P. Ghilardi
- Evelin Blom
- Maldon Goodridge
- Erik Solis
- Hamidreza Jahangir
- Jorge Angarita
- Nandhini Ganesan
- Kevin West
- Nilay Shah
- Calvin Tsay
doc_id: arxiv:2510.27528v1
family_id: arxiv:2510.27528
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Risk-constrained stochastic scheduling of multi-market energy storage systems
url_abs: http://arxiv.org/abs/2510.27528v1
url_html: https://arxiv.org/html/2510.27528v1
venue: arXiv q-fin
version: 1
year: 2025
---


Gabriel D. Patrón

Di Zhang

Lavinia M.P. Ghilardi

Evelin Blom

Maldon Goodridge

Erik Solis

Hamidreza Jahangir

Jorge Angarita

Nandhini Ganesan

Kevin West

Nilay Shah

Calvin Tsay

###### Abstract

Energy storage can promote the integration of renewables by operating with charge and discharge policies that balance an intermittent power supply. This study investigates the scheduling of energy storage assets under energy price uncertainty, with a focus on electricity markets. A two-stage stochastic risk-constrained approach is employed, whereby electricity price trajectories or specific power markets are observed, allowing for recourse in the schedule. Conditional value-at-risk is used to quantify tail risk in the optimization problems; this allows for the explicit specification of a probabilistic risk limit. The proposed approach is tested in an integrated hydrogen system (IHS) and a battery energy storage system (BESS). In the joint design and operation context for the IHS, the risk constraint results in larger installed unit capacities, increasing capital cost but enabling more energy inventory to buffer price uncertainty. As shown in both case studies, there is an operational trade-off between risk and expected reward; this is reflected in higher expected costs (or lower expected profits) with increasing levels of risk aversion. Despite the decrease in expected reward, both systems exhibit substantial benefits of increasing risk aversion. This work provides a general method to address uncertainties in energy storage scheduling, allowing operators to input their level of risk tolerance on asset decisions.

###### keywords:

Battery energy storage systems , Conditional value-at-risk , Hydrogen , Stochastic programming

††journal: Elsevier

\affiliation

[label1]organization=Department of Computing, Imperial College London,
city=London,
postcode=SW7 2AZ,
country=United Kingdom
\affiliation[label2]organization=Centre for Process Systems Engineering, Imperial College London,
city=London,
postcode=SW7 2AZ,
country=United Kingdom
\affiliation[label3]organization=BP International Ltd,
city=Sunbury-on-Thames,
postcode=TW16 7BP,
country=United Kingdom

{graphicalabstract}

![[Uncaptioned image]](x1.png)

{highlights}

Two-stage stochastic optimization is proposed for scheduling energy storage systems

Multi-market participation is considered

Optimal unit capacities and charge/discharge decisions are determined

A conditional value-at-risk (CVaR) risk-constrained approach is employed

Scheme tested in integrated hydrogen and battery energy storage systems

## 1 Introduction

Worldwide renewable energy capacity is rapidly expanding, accounting for 38%38\% of the increase in global energy supply in 2024 [[1](https://arxiv.org/html/2510.27528v1#bib.bib1)]. For this transition to continue, energy storage systems will be key in abating intermittencies [[2](https://arxiv.org/html/2510.27528v1#bib.bib2)], which limit the uptake of renewable generation and necessitate polluting base load energy sources such as combined-cycle power plants. Among the storage methods that have been proposed [[3](https://arxiv.org/html/2510.27528v1#bib.bib3)], hydrogen and battery energy storage systems (BESSs) are prominent in various national clean energy action plans (e.g., EU [[4](https://arxiv.org/html/2510.27528v1#bib.bib4)], UK [[5](https://arxiv.org/html/2510.27528v1#bib.bib5)]).

Hydrogen produced using an electrolytic cell powered by renewable energy is referred to as “green hydrogen” owing to its low carbon intensity [[6](https://arxiv.org/html/2510.27528v1#bib.bib6)]. When supplied with electricity, an electrolyzer converts water to oxygen gas in the anode and hydrogen gas in the cathode. Hydrogen is a versatile energy carrier, with a variety of uses, and a potential to further integrate variable renewable renewable electricity into the grid [[7](https://arxiv.org/html/2510.27528v1#bib.bib7)]. In settings where the process is grid-connected, hydrogen can provide both short- and medium-term storage via a fuel cell or turbine (to convert hydrogen back to electricity) and pressurized storage, respectively. Further, excess hydrogen may potentially be used as a drop-in fuel [[8](https://arxiv.org/html/2510.27528v1#bib.bib8)] for transport applications or as a feed stock to ammonia [[9](https://arxiv.org/html/2510.27528v1#bib.bib9)] production. Note that, while pathways toward green grid-connected hydrogen have been investigated [[10](https://arxiv.org/html/2510.27528v1#bib.bib10)], the carbon intensity of grid-connected hydrogen production depends on the current associated generation mix.

In contrast to hydrogen storage, which has seen little uptake given its relatively high capital cost, battery energy storage system (BESS) processes have seen a larger installed capacity to date [[11](https://arxiv.org/html/2510.27528v1#bib.bib11)]. A BESS typically employs the electrolytic reduction of lithium ions to store electrical energy in a cell. This enables short-term storage enabled by fast charge/discharge cycles, which can satisfy electrical grid demand. Increasingly, these battery assets are being used for energy arbitrage between various electrical markets [[12](https://arxiv.org/html/2510.27528v1#bib.bib12), [13](https://arxiv.org/html/2510.27528v1#bib.bib13), [14](https://arxiv.org/html/2510.27528v1#bib.bib14)], where price spreads are leveraged to generate a profit. By responding to changing electricity prices, a BESS operator, or indeed any rapid-response storage medium operator, can capitalize on these arbitrage opportunities.

Demand response refers to the dynamic adjustment of power consumption by an electricity consumer according to the energy prices, which are time-varying (often called “indirect” demand response). To this end, optimal demand response scheduling has been applied in many system contexts including: residential buildings [[15](https://arxiv.org/html/2510.27528v1#bib.bib15)], water distribution systems [[16](https://arxiv.org/html/2510.27528v1#bib.bib16)], and industrial air separation units [[17](https://arxiv.org/html/2510.27528v1#bib.bib17)]. Energy storage further allows for effective demand response by purchasing and storing energy during periods of low prices, thereby allowing for grid curtailment and consumption of stored energy during periods of high prices [[18](https://arxiv.org/html/2510.27528v1#bib.bib18), [19](https://arxiv.org/html/2510.27528v1#bib.bib19), [20](https://arxiv.org/html/2510.27528v1#bib.bib20)]. Most of these approaches follow the so-called “price-taker” approach, relying on accurate forecasting of the markets involved as problem inputs, which are subject to uncertainties in practice. These uncertainties induce suboptimal scheduling of the demand response, which results in economic losses. The reader is referred to Silva et al. [[21](https://arxiv.org/html/2510.27528v1#bib.bib21)] for a review of uncertainty in demand response.

To abate the effect of these price uncertainties, the literature has turned to stochastic optimization [[22](https://arxiv.org/html/2510.27528v1#bib.bib22), [23](https://arxiv.org/html/2510.27528v1#bib.bib23)], which allows for a distribution over electricity price estimates to be embedded into the optimal demand response scheduling problem [[21](https://arxiv.org/html/2510.27528v1#bib.bib21)]. In particular, two-stage stochastic optimization, with several readily-deployable software packages [[24](https://arxiv.org/html/2510.27528v1#bib.bib24)], provides an attractive framework for demand response decisions to be segmented into here-and-now and wait-and-see decisions. The former are implemented immediately, while the latter can be made at later time when the uncertainties are realized. While a choice of single here-and-now decisions is actioned, a conditional distribution of wait-and-see decisions is obtained such that the demand response schedule is adjusted according to the realized prices. For instance, here-and-now decisions may correspond to capital installations that must be decided before electricity prices are known, while wait-and-see decisions may involve how those processes are scheduled. Despite the success of stochastic demand response, these methods optimize the wait-and-see decisions based on their expectation; this can potentially lead to poor outcomes if the price scenarios that correspond to the tails of the distribution are realized in practice. Accordingly, a risk measure such as conditional value-at-risk (CVaR) can be modelled [[25](https://arxiv.org/html/2510.27528v1#bib.bib25)], optimized as an objective (penalty), or constrained.

In the context of energy storage, the joint explicit optimization of expected cost and tails risk for energy storage systems has been explored in microgrids with BESS [[26](https://arxiv.org/html/2510.27528v1#bib.bib26), [27](https://arxiv.org/html/2510.27528v1#bib.bib27)] and natural gas storage [[28](https://arxiv.org/html/2510.27528v1#bib.bib28)] settings for a given single power market. Furthermore, this has been extended to BESS processes operating in multiple power markets [[14](https://arxiv.org/html/2510.27528v1#bib.bib14)]. The joint optimization of cost expectation and risk, however, results in a multi-objective optimization problem, which is subject to an operator-defined weighting between the two objectives. The heuristic nature of the objective weights results in a lack of probabilistic guarantees on the tail risk. Notably, Herding et al. [[27](https://arxiv.org/html/2510.27528v1#bib.bib27)] explored the use of CVaR constraints in single-market BESS to explicitly limit the tail risk as specified in Haimes [[29](https://arxiv.org/html/2510.27528v1#bib.bib29)]; this provides a more attractive proposition to system operators and arbitrageurs that desire precise control over their exposure.

In this work, we propose a general risk-constrained stochastic optimization approach for the scheduling of energy storage assets under electricity price uncertainty. The proposed approach is demonstrated using two prototypical energy storage sytems: integrated hydrogen system (IHS) and a BESS. Both systems are considered to participate in day-ahead (DA) and intraday (ID) power markets. While these selected storage systems are similar in their ability to charge and discharge from the grid, they provide distinct perspectives on the risk-constrained scheduling problem. The IHS system is subject to a cost minimization problem that features capital decisions (i.e., it is a joint design and operation problem). Conversely, fixed capacities are assumed for the BESS system in a profit maximization (arbitrage) context; the fixed capacities enable scheduling to be applied in both long-term scheduling and rolling horizon (i.e., feedback control) settings. For BESS, the former setting can be used determine the optimal dispatch for a flexible power purchasing agreement, while the latter setting can be used in live energy trading. The risk-reward trade-off, proportion of market participation, and choice of recourse variables are explored in both systems. The key contributions of this study are:

* 1.

  A risk-constrained stochastic optimization framework is proposed for the general class of energy storage systems.
* 2.

  Multiple market participation is explored in the risk-constrained stochastic optimization context.
* 3.

  The framework is applied to a novel IHS case study (design and scheduling) and a BESS (scheduling-only) benchmarks.
* 4.

  Use of the framework is shown in yearly optimization (open loop) and rolling horizon (closed loop) settings.

The remainder of this work is organized as follows: [section 2](https://arxiv.org/html/2510.27528v1#S2 "2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") details stochastic optimization, CVaR modelling, and the proposed risk constraining approach; [section 3](https://arxiv.org/html/2510.27528v1#S3 "3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") and [section 4](https://arxiv.org/html/2510.27528v1#S4 "4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") present the IHS and BESS case studies, respectively; [section 5](https://arxiv.org/html/2510.27528v1#S5 "5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") applies the proposed approach to the previously outlined case studies and provides analysis on its outcomes; [section 6](https://arxiv.org/html/2510.27528v1#S6 "6 Conclusion ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") outlines the key takeaways and future work directions for this field.

## 2 Methodology

Deterministic opimization problems often require inputs that are not precisely known a priori (i.e., they are uncertain). The solution to a deterministic programming problem can be suboptimal with respect to the real-life systems subject to these uncertainties, which can result in economic losses. Uncertain inputs are often forecasted at the time of optimization (t0t\_{0}) and revealed later (e.g., once a market auction occurs at tobst\_{\mathrm{obs}}). Stochastic programming [[22](https://arxiv.org/html/2510.27528v1#bib.bib22)] can be used to abate the effects of uncertainty and limit potential losses. In this section, we propose the use of a stochastic programming framework that can be used for the short- and long-term optimization of energy storage systems. Further, we present a formulation for constraining CVaR to ensure limited tail risk.

### 2.1 Two-stage stochastic optimization

![Refer to caption](Figures/Figure1.png)


Figure 1: Tree diagram for two-stage stochastic program.

Stochastic programs for energy systems optimization subject to uncertain time-dependent signals (e.g., electricity market prices) are often formulated as multi-stage problems [[30](https://arxiv.org/html/2510.27528v1#bib.bib30), [31](https://arxiv.org/html/2510.27528v1#bib.bib31)], where values of uncertain inputs are dynamically revealed; however, these require significant computational effort to solve (e.g., [[32](https://arxiv.org/html/2510.27528v1#bib.bib32)]). To abate the computational effort of a multi-stage problem, we propose a two-stage approximation of the stochastic program for the optimization of energy storage systems. The optimization horizon and timescale of the system determines how these formulations are deployed (e.g., longer time horizons are used for capacity planning). We formulate the problem generally as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐗∈𝒳,𝐘∈𝒴​(𝐗,ξ)⁡𝔼ξ​[ℒ​(𝐗,𝐘,ξ)]=min𝐗∈𝒳,𝐘∈𝒴​(𝐗,ξ)⁡𝐜⊤​𝐗+𝔼ξ​[V​(𝐗,𝐘,ξ)],\min\_{\mathbf{X}\in\mathcal{X},\mathbf{Y}\in\mathcal{Y(\mathbf{X},\mathbf{\xi})}}\mathbb{E}\_{\mathbf{\xi}}\left[\mathcal{L}(\mathbf{X},\mathbf{Y},\mathbf{\xi})\right]=\min\_{\mathbf{X}\in\mathcal{X},\mathbf{Y}\in\mathcal{Y(\mathbf{X},\mathbf{\xi})}}\mathbf{c}^{\top}\mathbf{X}+\mathbb{E}\_{\mathbf{\xi}}\left[V(\mathbf{X},\mathbf{Y},\mathbf{\xi})\right], |  | (1) |

where the expected value of the objective function ℒ:𝒳×𝒴​(𝐗,ξ)×Ψ→ℝ\mathcal{L}:\mathcal{X}\times\mathcal{Y(\mathbf{X},\mathbf{\xi})}\times\Psi\rightarrow\mathbb{R} distribution is conditioned on the uncertainty set ξ∈Ψ\mathbf{\xi}\in\Psi with distribution 𝒫\mathcal{P} and support Ψ\Psi. The objective is minimized by the first-stage 𝐗∈𝒳⊂ℝX\mathbf{X}\in\mathcal{X}\subset\mathbb{R}^{X} and second-stage 𝐘∈𝒴​(𝐗,ξ)⊂ℝY\mathbf{Y}\in\mathcal{Y(\mathbf{X},\mathbf{\xi})}\subset\mathbb{R}^{Y} decisions, the latter of which are dependent on the former and the uncertainty set. Assuming a linear first-stage objective (in general, we will deal with LPs herein), the LHS of [Equation 1](https://arxiv.org/html/2510.27528v1#S2.E1 "1 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") can be decomposed into first- and second-stage objectives, where 𝐜∈ℝX\mathbf{c}\in\mathbb{R}^{X} is the first-stage cost, and only the second-stage objective V:𝒳×𝒴​(𝐗,ξ)×Ψ→ℝV:\mathcal{X}\times\mathcal{Y(\mathbf{X},\mathbf{\xi})}\times\Psi\rightarrow\mathbb{R} is conditioned on ξ{\mathbf{\xi}}. This breakdown separates the ‘here-and-now’ decisions (𝐗\mathbf{X}) from the ‘wait-and-see’ decisions (𝐘\mathbf{Y}).

For this problem to be solved using standard optimization solvers, [Equation 1](https://arxiv.org/html/2510.27528v1#S2.E1 "1 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") must be formulated in a closed (i.e., solvable), deterministic form. Therefore, the conditional objective function term is often discretized into a finite set 𝒮={1,…,nS}\mathcal{S}=\{1,...,n\_{S}\} of nSn\_{S} realizations of uncertainty (i.e., scenarios)[[33](https://arxiv.org/html/2510.27528v1#bib.bib33)]. This produces a large, monolithic approximation of [Equation 1](https://arxiv.org/html/2510.27528v1#S2.E1 "1 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), referred to as the sample average approximation (SAA):

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐗∈𝒳,𝐘∈𝒴​(𝐗,ξ)⁡𝐜⊤​𝐗+∑s∈𝒮πs​v​(𝐗,𝐘s,ξs),\min\_{\mathbf{X}\in\mathcal{X},\mathbf{Y}\in\mathcal{Y(\mathbf{X},\mathbf{\xi})}}\mathbf{c}^{\top}\mathbf{X}+\sum\_{s\in\mathcal{S}}\pi\_{s}v(\mathbf{X},\mathbf{Y}\_{s},\mathbf{\xi}\_{s}), |  | (2) |

where πs∈ℝ\pi\_{s}\in\mathbb{R} represents the probability of scenario s∈𝒮s\in\mathcal{S} corresponding to a discrete realization of the second-stage objective vv. A schematic of the discretized two-stage decision structure is shown in [Figure 1](https://arxiv.org/html/2510.27528v1#S2.F1 "Figure 1 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") whereby the first- and second-stage decisions are made at t0t\_{0} and tobst\_{\mathrm{obs}}, respectively. The observation time tobst\_{\mathrm{obs}} denotes the time at which the values of uncertain variables are revealed, and thus the ‘wait-and-see’ decisions are actioned according to the scenario that is realized in practice.
Several alternatives to the SAA formulation have been proposed, such as by using dynamic optimization [[34](https://arxiv.org/html/2510.27528v1#bib.bib34)] or surrogate models for the second-stage objective [[35](https://arxiv.org/html/2510.27528v1#bib.bib35)].
For example, our recent work [[36](https://arxiv.org/html/2510.27528v1#bib.bib36)] explores surrogate models for integrated design and scheduling of a hydrogen process under uncertainty.

### 2.2 Conditional value-at-risk

The formulation presented in [Equation 1](https://arxiv.org/html/2510.27528v1#S2.E1 "1 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") (and approximated in [Equation 2](https://arxiv.org/html/2510.27528v1#S2.E2 "2 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems")) optimizes over the expected value of the conditional objective distribution; however, tail risk is another potential optimization objective to mitigate against extreme shortfall. In other words, decision makers may be concerned with the expected performance given likely circumstances, but also with worst-case performance given a more extreme scenario.
The conditional value-at-risk (CVaR) is a common tail risk metric used in optimization owing to its convexity and coherence (i.e., monotonicity, sub-additivity, homogeneity, translational invariance) [[37](https://arxiv.org/html/2510.27528v1#bib.bib37)]. For a conditional random variable such as the second-stage loss function VV with a cost minimization objective as in [Equation 1](https://arxiv.org/html/2510.27528v1#S2.E1 "1 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), the right-tail (i.e., tail cost) CVaR is expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(V)=𝔼ξ​[V|V≥ζ]\displaystyle\mathrm{CVaR}\_{\alpha}(V)=\mathbb{E}\_{\xi}[V|V\geq\zeta] |  | (3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ=inf{V∈ℝ:ℱV​(ξ)≥α},\displaystyle\zeta=\inf\{V\in\mathbb{R}:\mathcal{F}\_{V}(\xi)\geq\alpha\}, |  | (4) |

where ℱV\mathcal{F}\_{V} is the cumulative density function of VV, and α\alpha is a user-specified risk percentile. The variable ζ\zeta represents the value-at-risk (VaR), which is not used as an explicit risk metric because it is not coherent. Alternatives to using CVaR to mitigate risk in energy systems optimization include using other risk metrics or robust optimization-based formulations. The reader is referred to Rahim et al. [[38](https://arxiv.org/html/2510.27528v1#bib.bib38)] for an review of robust optimization in energy grid applications.

Nevertheless, CVaR remains a common choice of risk metric, as with the SAA in two-stage problem, CVaR can be reformulated into individual realizations of uncertainty to produce an explicit closed-form optimization formulation, as shown by Rockafellar and Uryasev [[39](https://arxiv.org/html/2510.27528v1#bib.bib39)]. This reformulation yields the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(v)=ζ+11−α​∑s∈𝒮πs​[v​(𝐗,𝐘s,ξs)−ζ]+,\mathrm{CVaR}\_{\alpha}(v)=\zeta+\frac{1}{1-\alpha}\sum\_{s\in\mathcal{S}}\pi\_{s}[v(\mathbf{X},\mathbf{Y}\_{s},\mathbf{\xi}\_{s})-\zeta]^{+}, |  | (5) |

where [Equation 5](https://arxiv.org/html/2510.27528v1#S2.E5 "5 ‣ 2.2 Conditional value-at-risk ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") sums the difference between the VaR and the objectives found in the SAA scenarios that exceed the VaR itself (i.e., using the positive part operator [⋅]+=max​{⋅,0}[\cdot]^{+}=\mathrm{max}\{\cdot,0\}). This expression can be further reformulated to avoid a bi-level optimization problem (i.e., including the max operator) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(v)≡ζ+11−α​∑s∈𝒮πs​ηs\displaystyle\mathrm{CVaR}\_{\alpha}(v)\equiv\zeta+\frac{1}{1-\alpha}\sum\_{s\in\mathcal{S}}\pi\_{s}\eta\_{s} |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(𝐗,𝐘s,ξs)−ζ≤ηs;∀s∈𝒮\displaystyle v(\mathbf{X},\mathbf{Y}\_{s},\mathbf{\xi}\_{s})-\zeta\leq\eta\_{s};\quad\forall s\in\mathcal{S} |  | (7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ηs≥0;∀s∈𝒮,\displaystyle\eta\_{s}\geq 0;\quad\forall s\in\mathcal{S}, |  | (8) |

where ηs\eta\_{s} is a non-negative auxiliary variable introduced in the reformulation.

### 2.3 Risk-constrained two-stage stochastic optimization

Combining the SAA objective in [Equation 2](https://arxiv.org/html/2510.27528v1#S2.E2 "2 ‣ 2.1 Two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") with the CVaR formulation in [Equation 6](https://arxiv.org/html/2510.27528v1#S2.E6 "6 ‣ 2.2 Conditional value-at-risk ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems")–[Equation 8](https://arxiv.org/html/2510.27528v1#S2.E8 "8 ‣ 2.2 Conditional value-at-risk ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") yields the resulting risk-constrained two-stage problem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min𝐗∈𝒳,𝐘s∈𝒴⁡𝐜⊤​𝐗+∑s∈𝒮πs​v​(𝐗,𝐘s,ξs)\displaystyle\min\_{\mathbf{X}\in\mathcal{X},\mathbf{Y}\_{s}\in\mathcal{Y}}\mathbf{c}^{\top}\mathbf{X}+\sum\_{s\in\mathcal{S}}\pi\_{s}v(\mathbf{X},\mathbf{Y}\_{s},\mathbf{\xi}\_{s}) |  |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | s.t.\displaystyle s.t. |  |  |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ζ+11−α​∑s∈𝒮πs​ηs≤ϵ\displaystyle\zeta+\frac{1}{1-\alpha}\sum\_{s\in\mathcal{S}}\pi\_{s}\eta\_{s}\leq\epsilon |  |  |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐟​(𝐗,𝐘s,ξs)≤0\displaystyle\mathbf{f}(\mathbf{X},\mathbf{Y}\_{s},\mathbf{\xi}\_{s})\leq 0 | ;∀s∈𝒮\displaystyle;\quad\forall s\in\mathcal{S} |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(𝐗,𝐘s,ξs)−ζ≤ηs\displaystyle v(\mathbf{X},\mathbf{Y}\_{s},\mathbf{\xi}\_{s})-\zeta\leq\eta\_{s} | ;∀s∈𝒮\displaystyle;\quad\forall s\in\mathcal{S} |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ηs≥0\displaystyle\eta\_{s}\geq 0 | ;∀s∈𝒮,\displaystyle;\quad\forall s\in\mathcal{S}, |  |  |

where the user-specified parameter ϵ\epsilon reflects risk aversion by providing an upper bound to CVaR. In practice, this upper bound represents the user-defined maximum allowable αt​h\alpha^{th} percentile tail loss, thus limiting the potential for extreme shortfall. To choose a value for ϵ\epsilon, the risk-neutral stochastic problem must be solved to determine the nominal CVaR; the operator can then choose to impose ϵ\epsilon value lower than the nominal CVaR to reflect the aggressiveness of their energy trading strategy. A trade-off exists between expected cost and CVaR, where a larger bound results in lower expected costs (i.e., a less conservative formulation introduces more risk, but a potentially higher expected reward). A risk-aware formulation where the CVaR expression is embedded into the objective function with a weighting factor is also used in the literature [[26](https://arxiv.org/html/2510.27528v1#bib.bib26), [28](https://arxiv.org/html/2510.27528v1#bib.bib28), [27](https://arxiv.org/html/2510.27528v1#bib.bib27), [14](https://arxiv.org/html/2510.27528v1#bib.bib14)]; however, this may be less useful from an operator’s perspective, as it does not directly enable specifying a probabilistic upper risk limit. The risk-constrained approach presented in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") provides an explicit risk bound, which provides a probabilities guarantee of limited shortfall. The general constraints 𝐟:𝒳×𝒴​(𝐗,ξ)×Ψ→ℝf\mathbf{f}:\mathcal{X}\times\mathcal{Y(\mathbf{X},\mathbf{\xi})}\times\Psi\rightarrow\mathbb{R}^{f} correspond to the system model, which further imposes operational constraints on the optimization problem and is instantiated in the scenario set 𝒮\mathcal{S}.

The formulation in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") is general and can be deployed in a variety of energy storage systems, operational settings, and uncertain inputs as will be shown in the forthcoming case studies. In this work, we take 𝐟​(⋅)\mathbf{f}(\cdot) to be a linear (or linearized) process model, thus all optimization problems are linear programs (LPs).

## 3 Integrated hydrogen system

![Refer to caption](x2.png)


Figure 2: Schematic of the integrated hydrogen system.

In this section, we adapt an integrated hydrogen system (IHS) case study based on Tsay and Qvist [[40](https://arxiv.org/html/2510.27528v1#bib.bib40)]. This system, shown in [Figure 2](https://arxiv.org/html/2510.27528v1#S3.F2 "Figure 2 ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), comprises an electrolyzer that generates hydrogen to heat an industrial steel-making furnace. Alternatively, the hydrogen can be compressed for storage, where it can later deployed in the steel-making process or converted back into electricity via a fuel cell. In this case, the electricity prices are unknown at the time the plant is built and are revealed when the IHS begins operation or some time thereafter. Accordingly, recourse allows for capital decisions to be robust to future unknown electricity prices at construction time.

The set of units in this system is denoted 𝒰={elec,stor,heat,comp,f​c}\mathcal{U}=\{\mathrm{elec},\mathrm{stor},\mathrm{heat},\mathrm{comp},fc\}. A fixed one-year operating horizon is assumed, which is discretized into hour-long intervals 𝒯={t0,…,tobs,…,tf}\mathcal{T}=\{t\_{0},...,t\_{\mathrm{obs}},...,t\_{f}\} where tf=8760t\_{f}=8760 hours. Further, we assume participation in the day-ahead and intraday power markets, denoted ℳ={D​A,I​D}\mathcal{M}=\{DA,ID\}. We assume that the true price signal is unknown at optimization time t0t\_{0}, but estimates/predicted scenarios are available, motivating a stochastic optimization approach. Although the multi-stage setting is the most accurate representation of the energy market (i.e., prices are revealed continually through time), we approximate this problem using two stages, where the true price trajectories are revealed at a single point in time. Accordingly, once sufficient time tobst\_{\mathrm{obs}} has elapsed, the true price trajectory is observed, allowing for recourse actions to be taken. We define the partitioned time periods as two sets 𝒯0={t0,…,tobs−1}\mathcal{T}\_{0}=\{t\_{0},...,t\_{\mathrm{obs}}-1\} and 𝒯obs=𝒯∖𝒯0\mathcal{T}\_{\mathrm{obs}}=\mathcal{T}\setminus\mathcal{T}\_{0} (i.e., 𝒯=𝒯0∪𝒯obs\mathcal{T}=\mathcal{T}\_{0}\cup\mathcal{T}\_{\mathrm{obs}}).

The risk-constrained two-stage problem for this system has the first-stage decisions 𝐗=[𝐂𝐝𝐭𝟎]⊤\mathbf{X}=\begin{bmatrix}\mathbf{C}&\mathbf{d\_{t\_{0}}}\end{bmatrix}^{\top}, where 𝐂∈𝒞⊂ℝ|𝒰|\mathbf{C}\in\mathcal{C}\subset\mathbb{R}^{|\mathcal{U}|} are the unit capacities and 𝐝𝐭𝟎∈𝒟t0⊂ℝ|𝒰×𝒯0×ℳ|\mathbf{d\_{t\_{0}}}\in\mathcal{D}\_{t\_{0}}\subset\mathbb{R}^{|\mathcal{U}\times\mathcal{T}\_{0}\times\mathcal{M}|} are the charge-discharge decisions from/to the grid before the price trajectory can be observed; positive and negative domains represent charging and discharging, respectively, as the default optimization convention in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") is cost minimization. The second stage decisions are the charge/discharge dispatch decision after price trajectory observation 𝐘=𝐝𝐭obs∈𝒟tobs​(𝐂,𝐝𝐭𝟎)⊂ℝ|𝒰×𝒯obs×ℳ|\mathbf{Y}=\mathbf{d\_{t\_{\mathrm{obs}}}}\in\mathcal{D}\_{t\_{\mathrm{obs}}}(\mathbf{C},\mathbf{d\_{t\_{0}}})\subset\mathbb{R}^{|\mathcal{U}\times\mathcal{T}\_{\mathrm{obs}}\times\mathcal{M}|}. The first-stage price vector is concatenated as 𝐜∈ℝ|𝒰|+|𝒰×𝒯0×ℳ|\mathbf{c}\in\mathbb{R}^{|\mathcal{U}|+|\mathcal{U}\times\mathcal{T}\_{0}\times\mathcal{M}|} where they are partitioned into capital and operating prices 𝐜=[𝐏𝐜𝐚𝐩𝐏𝐭𝟎]⊤\mathbf{c}=\begin{bmatrix}\mathbf{P\_{cap}}&\mathbf{P\_{t\_{0}}}\end{bmatrix}^{\top}. The second-stage uncertain price vector is the multivariate distribution ξ=𝐏obs∈Ψ⊂ℝ|𝒰×𝒯obs×ℳ|\mathbf{\xi}=\mathbf{P\_{\mathrm{obs}}}\in\Psi\subset\mathbb{R}^{|\mathcal{U}\times\mathcal{T}\_{\mathrm{obs}}\times\mathcal{M}|}.

The model 𝐟\mathbf{f} describing the system is outlined next; a detailed description of the model development can be found in Tsay and Qvist [[40](https://arxiv.org/html/2510.27528v1#bib.bib40)]. Model parameters are given in [Table 1](https://arxiv.org/html/2510.27528v1#S3.T1 "Table 1 ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Parameter | Symbol | Value | Units |
| Electrolyzer | Rectifier efficiency | LA​C/D​CL\_{AC/DC} | 1.05 | - |
|  | Auxilliary power consumption | LauxL\_{\mathrm{aux}} | 0.05 | - |
|  | Degradation factor | LelecdegL^{\mathrm{deg}}\_{\mathrm{elec}} | 0.9142 | - |
|  | Efficiency | LelecL\_{\mathrm{elec}} | 0.05 | MW/kg |
|  | Pressure | pelecp\_{\mathrm{elec}} | 1 | MPa |
| Storage | temperature | TstorT\_{\mathrm{stor}} | 298 | K |
|  | Lower pressure bound | pstorl​Bp^{lB}\_{\mathrm{stor}} | 2 | MPa |
|  | Upper pressure bound | pstorU​Bp^{UB}\_{\mathrm{stor}} | 20 | MPa |
|  | Compressibility factor | ZZ | 1.07 | - |
| Heater | Specific energy | epe\_{p} | 11.82 | MJ/kg |
|  | Heater efficiency | ηheat\eta\_{\mathrm{heat}} | 0.75 | - |
| Compressor | Efficiency | ηcomp\eta\_{\mathrm{comp}} | 0.7 | - |
| Fuel cell | Inverter efficiency | LD​C/A​CL\_{DC/AC} | 0.95 | - |
|  | Auxilliary power consumption | LauxL\_{\mathrm{aux}} | 0.05 | - |
|  | Degradation factor | LelecdegL^{\mathrm{deg}}\_{\mathrm{elec}} | 0.9142 | - |
|  | Voltage | VV | 0.7 | V |

Table 1: IHS model parameters.

### 3.1 Electrolyzer

The electrolyzer is parametrized using a linear scaling law to model the rectification between grid AC and plant DC current. Efficiency factors are used for the DC/AC conversion and auxilliary equipment DC power consumption:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈MdelecA​C​(t,m)=(LA​C/D​C+Laux)​delecD​C​(t);∀t∈𝒯,\sum\_{\forall m\in M}d\_{\mathrm{elec}}^{AC}(t,m)=(L\_{AC/DC}+L\_{\mathrm{aux}})d\_{\mathrm{elec}}^{DC}(t);\quad\forall t\in\mathcal{T}, |  | (10) |

where delecA​Cd\_{\mathrm{elec}}^{AC} and delecD​Cd\_{\mathrm{elec}}^{DC} (MW) are, respectively, the AC and DC electrolyzer power consumptions at hour tt and from market mm. Electrolyzer efficiency and degradation factors are used to model the conversion of DC electricity to hydrogen gas:

|  |  |  |  |
| --- | --- | --- | --- |
|  | FelecH2​(t)=Lelecdeg​delecD​C​(t)Lelec;∀t∈𝒯,F\_{\mathrm{elec}}^{H\_{2}}(t)=\frac{L\_{\mathrm{elec}}^{\mathrm{deg}}d\_{\mathrm{elec}}^{DC}(t)}{L\_{\mathrm{elec}}};\quad\forall t\in\mathcal{T}, |  | (11) |

where FelecH2F\_{\mathrm{elec}}^{H\_{2}} (kg/h) denotes the hydrogen production flowrate, which is split between the storage and heating units, i.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | FelecH2​(t)=Fstorin​(t)+Fheatin,elec​(t);∀t∈𝒯.F\_{\mathrm{elec}}^{H\_{2}}(t)=F\_{\mathrm{stor}}^{\mathrm{in}}(t)+F\_{\mathrm{heat}}^{\mathrm{in,elec}}(t);\quad\forall t\in\mathcal{T}. |  | (12) |

A constraint is imposed such that the DC power consumption of the electrolyzer does not exceed the unit capacity CelecC\_{\mathrm{elec}} (MW):

|  |  |  |  |
| --- | --- | --- | --- |
|  | delecD​C​(t)≤Celec;∀t∈𝒯.d\_{\mathrm{elec}}^{DC}(t)\leq C\_{\mathrm{elec}};\quad\forall t\in\mathcal{T}. |  | (13) |

Finally, a power rate-of-change constraint is imposed on the DC power hourly consumption:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |delecD​C​(t)−delecD​C​(t−1)|≤0.2​Celec;∀t∈𝒯∖{t0}.|d\_{\mathrm{elec}}^{DC}(t)-d\_{\mathrm{elec}}^{DC}(t-1)|\leq 0.2C\_{\mathrm{elec}};\quad\forall t\in\mathcal{T}\setminus\{t\_{0}\}. |  | (14) |

### 3.2 Storage

The storage inventory is modeled by mass balances from one time period to the next:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Istor​(t)=Istor​(t−1)+(Fstorin​(t)+Fstorout​(t))​Δ​t;∀t∈𝒯∖{t0},I\_{\mathrm{stor}}(t)=I\_{\mathrm{stor}}(t-1)+(F\_{\mathrm{stor}}^{\mathrm{in}}(t)+F\_{\mathrm{stor}}^{\mathrm{out}}(t))\Delta t;\quad\forall t\in\mathcal{T}\setminus\{t\_{0}\}, |  | (15) |

where IstorI\_{\mathrm{stor}} (kg), FstorinF^{\mathrm{in}}\_{\mathrm{stor}} (kg/h), and FstoroutF^{\mathrm{out}}\_{\mathrm{stor}} (kg/h) are the time-dependent hydrogen inventory, inlet flowrate, and outlet flowrate. The outlet storage flowrate is split between the fuel cell and heating units, giving the mass balance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fstorout​(t)=Ff​cH2​(t)+Fheatin,stor​(t);∀t∈𝒯.F\_{\mathrm{stor}}^{\mathrm{out}}(t)=F\_{fc}^{H\_{2}}(t)+F\_{\mathrm{heat}}^{\mathrm{in,stor}}(t);\quad\forall t\in\mathcal{T}. |  | (16) |

The ideal gas law is used to model storage pressure by incorporating a compressibility factor calculated at the centroid of the pressure bounds and at the isothermal storage temperature in [Table 1](https://arxiv.org/html/2510.27528v1#S3.T1 "Table 1 ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). We further assume that sufficient capacity is required to accommodate for the upper pressure bound at the storage temperature; this is reflected in the hydrogen density ρ\rho (kg/m3\mathrm{m^{3}}) term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pstor​(t)=pstorL​B+Z​Istor​(t)​ρ​(Tstor,pstorU​B)​R​TstorMH2​Cstor;∀t∈𝒯,p\_{\mathrm{stor}}(t)=p\_{\mathrm{stor}}^{LB}+Z\frac{I\_{\mathrm{stor}}(t)\rho(T\_{\mathrm{stor}},p\_{\mathrm{stor}}^{UB})RT\_{\mathrm{stor}}}{M\_{H\_{2}}C\_{\mathrm{stor}}};\quad\forall t\in\mathcal{T}, |  | (17) |

where RR (J/mol/K) is the ideal gas constant and MH2M\_{H\_{2}} (kg/mol) is the molar mass of hydrogen. The following bounds are placed on storage pressure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pstorL​B≤pstor​(t)≤pstorU​B;∀t∈𝒯.p\_{\mathrm{stor}}^{LB}\leq p\_{\mathrm{stor}}(t)\leq p\_{\mathrm{stor}}^{UB};\quad\forall t\in\mathcal{T}. |  | (18) |

### 3.3 Heater

The heater duty dheatd\_{\mathrm{heat}} (MW) is dependent on hydrogen throughput from both electrolyzer Fheatin,elecF^{\mathrm{in,elec}}\_{\mathrm{heat}} (kg/s) and storage Fheatin,storF^{\mathrm{in,stor}}\_{\mathrm{heat}} (kg/s) units whereby a unit-averaged specific energy epe\_{p} (MJ/kg) is used:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mdheat​(t,m)=1ηheat​∑i∈{elec,stor}Fheatin,i​(t)​ep;∀t∈𝒯.\sum\_{\forall m\in M}d\_{\mathrm{heat}}(t,m)=\frac{1}{\eta\_{\mathrm{heat}}}\sum\_{i\in\{\mathrm{elec,stor}\}}F\_{\mathrm{heat}}^{\mathrm{in},i}(t)e\_{p};\quad\forall t\in\mathcal{T}. |  | (19) |

A constraint is imposed on the inlet stream to the heater to ensure the DRI hydrogen demand is met:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fheatin,elec​(t)+Fheatin,stor​(t)≥150000;∀t∈𝒯.F\_{\mathrm{heat}}^{\mathrm{in,elec}}(t)+F\_{\mathrm{heat}}^{\mathrm{in,stor}}(t)\geq 150000;\quad\forall t\in\mathcal{T}. |  | (20) |

A constraint is imposed such that the heater energy consumption does not exceed its capacity CheatC\_{\mathrm{heat}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mdheat​(t,m)≤Cheat;∀t∈𝒯.\sum\_{\forall m\in M}d\_{\mathrm{heat}}(t,m)\leq C\_{\mathrm{heat}};\quad\forall t\in\mathcal{T}. |  | (21) |

### 3.4 Compressor

The compressor duty dcompd\_{\mathrm{comp}} is dependent on the hydrogen flowrate being processed assuming single-stage isothermal operation; this model is linearized using a first-order Taylor series expansion around F=storin0F\mathrm{{}\_{stor}^{in}}=0 at the centroid of the storage pressure bounds [[40](https://arxiv.org/html/2510.27528v1#bib.bib40)], which results in the following expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mdcomp​(t,m)=R​Telecηcomp​Fstorin​(t)​l​n​(pstorL​B+pstorU​B2​pelec);∀t∈𝒯.\sum\_{\forall m\in M}d\_{\mathrm{comp}}(t,m)=\frac{RT\_{\mathrm{elec}}}{\eta\_{\mathrm{comp}}}F\_{\mathrm{stor}}^{\mathrm{in}}(t)ln\left(\frac{p\_{\mathrm{stor}}^{LB}+p\_{\mathrm{stor}}^{UB}}{2p\_{\mathrm{elec}}}\right);\quad\forall t\in\mathcal{T}. |  | (22) |

The errors introduced by this approximation, and their effects on the optimization results, were found to be relatively small by [[40](https://arxiv.org/html/2510.27528v1#bib.bib40)].
A constraint is imposed such that the compressor duty does not exceed its capacity CcompC\_{\mathrm{comp}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mdcomp​(t,m)≤Ccomp;∀t∈𝒯.\sum\_{\forall m\in M}d\_{\mathrm{comp}}(t,m)\leq C\_{\mathrm{comp}};\quad\forall t\in\mathcal{T}. |  | (23) |

### 3.5 Fuel cell

The fuel cell energy output df​cD​Cd^{DC}\_{fc} (MW) is denoted as a negative value since the model convention is positive sign for charging and conversely negative for discharging. This output is approximated as a function the hydrogen feed Ff​cH2F\_{fc}^{H\_{2}} (kg/h):

|  |  |  |  |
| --- | --- | --- | --- |
|  | −df​cD​C​(t)=2​F​Ff​cH2​(t)MH2​V​Lf​cdeg;∀t∈𝒯,-d\_{fc}^{DC}(t)=2F\frac{F\_{fc}^{H\_{2}}(t)}{M^{H\_{2}}}VL\_{fc}^{\mathrm{deg}};\quad\forall t\in\mathcal{T}, |  | (24) |

where FF (C/mol) is Faraday’s constant and MH2M^{H\_{2}} (kg/mol) is the molar mass of hydrogen gas.

Conversely to the electrolyzer, an inverter is needed to convert DC df​cD​Cd\_{fc}^{DC} (MW) to AC df​cA​Cd\_{fc}^{AC} (MW) power in the fuel cell as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mdf​cA​C​(t,m)=(LD​C/A​C−La​u​x)​df​cD​C​(t);∀t∈𝒯.\sum\_{\forall m\in M}d\_{fc}^{AC}(t,m)=(L\_{DC/AC}-L\_{aux})d\_{fc}^{DC}(t);\quad\forall t\in\mathcal{T}. |  | (25) |

A constraint is imposed such that the fuel cell energy production does not exceed its capacity Cf​cC\_{fc} (MW):

|  |  |  |  |
| --- | --- | --- | --- |
|  | −df​cD​C​(t)≤Cf​c;∀t∈𝒯.-d\_{fc}^{DC}(t)\leq C\_{fc};\quad\forall t\in\mathcal{T}. |  | (26) |

### 3.6 Cost function

| Unit (i∈Ui\in U) | Pcap,iP\_{\mathrm{cap},i} | WiW\_{i} | OiO\_{i} |
| --- | --- | --- | --- |
| Electrolyzer stack | 150 $/kW | 0.13 | 2 $/kW/y |
| electrolyzer auxilliary | 250 $/kW | 0.08 | - |
| Storage | 1000 $/kg | 0.1 | 10 $/kg/y |
| Heater | 50 $/kW | 0.13 | 1 $/kW/y |
| Compressor | 50 $/kW | 0.13 | 1 $/kW/y |
| Fuel cell stack | 150 $/kW | 0.13 | 2 $/kW/y |
| Fuel cell auxilliary | 250 $/kW | 0.08 | - |

Table 2: IHS capital cost parameters.

The cost function for the hydrogen system defines the objective function and comprises capital and operating costs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒI​H​S​(𝐗,𝐘,𝐜,ξ)=Jcap​(𝐂,𝐏𝐜𝐚𝐩)+Jop​(𝐝𝐭𝟎,𝐝𝐭𝐨𝐛𝐬,𝐏𝐭𝟎,𝐏𝐭𝐨𝐛𝐬).\mathcal{L}\_{IHS}(\mathbf{X},\mathbf{Y},\mathbf{c},\xi)=J^{\mathrm{cap}}(\mathbf{C},\mathbf{P\_{cap}})+J^{\mathrm{op}}(\mathbf{d\_{t\_{0}}},\mathbf{d\_{t\_{obs}}},\mathbf{P\_{t\_{0}}},\mathbf{P\_{t\_{obs}}}). |  | (27) |

The capital cost is comprised of the unit capacity costs with a lifetime annualizing factor 𝐖∈ℝ|U|\mathbf{W}\in\mathbb{R}^{|U|} and equipment maintenance cost 𝐎∈ℝ|U|\mathbf{O}\in\mathbb{R}^{|U|}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jcap​(𝐂,𝐏𝐜𝐚𝐩)=(𝐏𝐜𝐚𝐩⊙𝐖+𝐎)⊤​𝐂,J^{\mathrm{cap}}(\mathbf{C},\mathbf{P\_{cap}})=(\mathbf{P\_{cap}}\odot\mathbf{W}+\mathbf{O})^{\top}\mathbf{C}, |  | (28) |

where capital cost factors are given in [Table 2](https://arxiv.org/html/2510.27528v1#S3.T2 "Table 2 ‣ 3.6 Cost function ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") and ⊙\odot denotes the Hadamard product.

The operating cost is the time-accrued product of the net charge/discharge of all units and the electricity prices in day-ahead and intraday markets:

|  |  |  |  |
| --- | --- | --- | --- |
|  | JI​H​So​p​(𝐝𝐭𝟎,𝐝𝐭𝐨𝐛𝐬,𝐏𝐭𝟎,𝐏𝐭𝐨𝐛𝐬)=𝐏𝐭𝟎⊤​𝐝𝐭𝟎+𝐏𝐭𝐨𝐛𝐬⊤​𝐝𝐭𝐨𝐛𝐬.J^{op}\_{IHS}(\mathbf{d\_{t\_{0}}},\mathbf{d\_{t\_{obs}}},\mathbf{P\_{t\_{0}}},\mathbf{P\_{t\_{obs}}})=\mathbf{P\_{t\_{0}}}^{\top}\mathbf{d\_{t\_{0}}}+\mathbf{P\_{t\_{obs}}}^{\top}\mathbf{d\_{t\_{obs}}}. |  | (29) |

When discretized in time, the overall sample-average approximation in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") for the IHS problem reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐏𝐜𝐚𝐩⊤​𝐂+∑m∈ℳ∑t∈𝒯0Pm,t​dm,t+∑m∈ℳ∑t∈𝒯obs∑s∈𝒮πs​Pm,t,s​dm,t,s.\mathbf{P\_{cap}}^{\top}\mathbf{C}+\sum\_{m\in\mathcal{M}}\sum\_{t\in\mathcal{T}\_{0}}P\_{m,t}d\_{m,t}+\sum\_{m\in\mathcal{M}}\sum\_{t\in\mathcal{T}\_{\mathrm{obs}}}\sum\_{s\in\mathcal{S}}\pi\_{s}P\_{m,t,s}d\_{m,t,s}. |  | (30) |

## 4 Battery Energy Storage System

![Refer to caption](x3.png)


Figure 3: Schematic of the battery energy storage system.

This section introduces a battery energy storage system (BESS) model as a second case study to further explore the advantages of the CVaR-constrained formulation in storage settings. The system, shown in [Figure 3](https://arxiv.org/html/2510.27528v1#S4.F3 "Figure 3 ‣ 4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), comprises a 50 MWh battery with fixed capacity that buys and sells electricity from the grid through an inverter/rectifier to convert current types. This battery system can be used in a variety of storage settings; however, we focus on the flexible power purchasing agreement (PPA) setting and live energy trading settings. These are discussed in [subsection 5.2](https://arxiv.org/html/2510.27528v1#S5.SS2 "5.2 Yearly optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") and [subsection 5.3](https://arxiv.org/html/2510.27528v1#S5.SS3 "5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), respectively, and have different mechanisms for revealing price uncertainties.

As with the IHS, a fixed one-year operating horizon is discretized into hour-long intervals 𝒯={t0,…,tobs,…,tf}\mathcal{T}=\{t\_{0},...,t\_{\mathrm{obs}},...,t\_{f}\} where tf=8760t\_{f}=8760 hours with participation in the day-ahead and intraday markets ℳ={D​A,I​D}\mathcal{M}=\{DA,ID\}. The true price signal is unknown at optimization time t0t\_{0} and once sufficient time tobst\_{\mathrm{obs}} has elapsed, the true price trajectory is observed, allowing for recourse to occur. For consistency, we again define the sets 𝒯0={t0,…,tobs−1}\mathcal{T}\_{0}=\{t\_{0},...,t\_{\mathrm{obs}}-1\} and 𝒯obs=𝒯∖𝒯0\mathcal{T}\_{\mathrm{obs}}=\mathcal{T}\setminus\mathcal{T}\_{0} (i.e., 𝒯=𝒯0∪𝒯obs\mathcal{T}=\mathcal{T}\_{0}\cup\mathcal{T}\_{\mathrm{obs}}).

The risk-constrained two-stage problem for this system has the first-stage decisions 𝐗=[𝐜𝐭𝟎𝐝𝐭𝟎]⊤\mathbf{X}=\begin{bmatrix}\mathbf{c\_{t\_{0}}}&\mathbf{d\_{t\_{0}}}\end{bmatrix}^{\top} where 𝐜𝐭𝟎∈𝒞t0⊂ℝ|𝒯0×ℳ|\mathbf{c\_{t\_{0}}}\in\mathcal{C}\_{t\_{0}}\subset\mathbb{R}^{|\mathcal{T}\_{0}\times\mathcal{M}|} are the charge and 𝐝𝐭𝟎∈𝒟t0⊂ℝ|𝒯0×ℳ|\mathbf{d\_{t\_{0}}}\in\mathcal{D}\_{t\_{0}}\subset\mathbb{R}^{|\mathcal{T}\_{0}\times\mathcal{M}|} are the discharge decisions from the grid before the price trajectory can be observed. The second stage decisions are the charge/discharge dispatch decision after price trajectory observation 𝐘=[𝐜𝐭𝐨𝐛𝐬𝐝𝐭𝐨𝐛𝐬]⊤\mathbf{Y}=\begin{bmatrix}\mathbf{c\_{t\_{obs}}}&\mathbf{d\_{t\_{obs}}}\end{bmatrix}^{\top} where 𝐜𝐭𝐨𝐛𝐬∈𝒞tobs​(𝐜𝐭𝟎,𝐝𝐭𝟎)⊂ℝ|𝒯obs×ℳ|\mathbf{c\_{t\_{obs}}}\in\mathcal{C}\_{t\_{\mathrm{obs}}}(\mathbf{c\_{t\_{0}}},\mathbf{d\_{t\_{0}}})\subset\mathbb{R}^{|\mathcal{T}\_{\mathrm{obs}}\times\mathcal{M}|} and 𝐝𝐭obs∈𝒟tobs​(𝐜𝐭𝟎,𝐝𝐭𝟎)⊂ℝ|𝒯obs×ℳ|\mathbf{d\_{t\_{\mathrm{obs}}}}\in\mathcal{D}\_{t\_{\mathrm{obs}}}(\mathbf{c\_{t\_{0}}},\mathbf{d\_{t\_{0}}})\subset\mathbb{R}^{|\mathcal{T}\_{\mathrm{obs}}\times\mathcal{M}|}. For convenience and, in contrast to the IHS, both charge and discharge variables have a positive convention. The first-stage price vector is 𝐜=𝐏𝐭𝟎∈ℝ|𝒯0×ℳ|\mathbf{c}=\mathbf{P\_{t\_{0}}}\in\mathbb{R}^{|\mathcal{T}\_{0}\times\mathcal{M}|} and second-stage uncertain price vector is the multivariate distribution ξ=𝐏obs∈Ψ⊂ℝ|𝒯obs×ℳ|\mathbf{\xi}=\mathbf{P\_{\mathrm{obs}}}\in\Psi\subset\mathbb{R}^{|\mathcal{T}\_{\mathrm{obs}}\times\mathcal{M}|}.

The model 𝐟\mathbf{f} describing the BESS is outlined next. For this case, the value of proprietary model parameters listed in [Table 3](https://arxiv.org/html/2510.27528v1#S4.T3 "Table 3 ‣ 4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") are not shared. However, similar linear models based on efficiency factors and Coulomb counting can be readily found in the literature (e.g., [[41](https://arxiv.org/html/2510.27528v1#bib.bib41), [42](https://arxiv.org/html/2510.27528v1#bib.bib42), [43](https://arxiv.org/html/2510.27528v1#bib.bib43)]).

| Parameter | Symbol | Units |
| --- | --- | --- |
| Battery hourly self-discharge | σbatt\sigma\_{\mathrm{batt}} | - |
| Round-trip efficiency | ηbatt\eta\_{\mathrm{batt}} | - |
| Inverter size | CinvC\_{\mathrm{inv}} | kW |
| Degradation constant | ηdeg\eta\_{\mathrm{deg}} | - |
| Maximum daily cycles | CmaxC\_{\mathrm{max}} | - |

Table 3: BESS model parameters.

### 4.1 State of charge

An energy balance is used to model the state of charge S​O​CSOC (kWh) of the battery system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​O​C​(t)=(1−σbatt)​S​O​C​(t−1)+ηbatt​∑m∈Mc​(t,m)−1ηbatt​∑m∈Md​(t,m);∀t∈𝒯∖{t0},SOC(t)=(1-\sigma\_{\mathrm{batt}})SOC(t-1)+\eta\_{\mathrm{batt}}\sum\_{m\in M}c(t,m)-\\ \frac{1}{\eta\_{\mathrm{batt}}}\sum\_{m\in M}d(t,m);\quad\forall t\in\mathcal{T}\setminus\{t\_{0}\}, |  | (31) |

where the charge and discharge decisions are denoted as cc and dd (k​WkW), respectively. Battery self-discharge as well as round-trip efficiency are modeled using linear factors. Furthermore, the battery degrades over time, and the state of charge cannot exceed the battery capacity, as defined by the state of health S​O​HSOH (kWh) at a given point in time:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤S​O​C​(t)≤S​O​H​(t);∀t∈𝒯.0\leq SOC(t)\leq SOH(t);\quad\forall t\in\mathcal{T}. |  | (32) |

### 4.2 Capacity

Bounds are imposed on the charge and discharge decisions at every time and in every market such that they are within the limits imposed by the inverter size:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤c​(t,m)≤Ic​(t,m)​Cinv;∀(t,m)∈𝒯×ℳ\displaystyle 0\leq c(t,m)\leq I\_{c}(t,m)C\_{\mathrm{inv}};\quad\forall(t,m)\in\mathcal{T}\times\mathcal{M} |  | (33) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤d​(t,m)≤Id​(t,m)​Cinv;∀(t,m)∈𝒯×ℳ,\displaystyle 0\leq d(t,m)\leq I\_{d}(t,m)C\_{\mathrm{inv}};\quad\forall(t,m)\in\mathcal{T}\times\mathcal{M}, |  | (34) |

where II are binary variables to enforce no simultaneous charging and discharging in a given market and time. As separate charging and discharging variables are introduced in the BESS model, we must enforce this condition as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ic​(t,m)+Id​(t,m)≤1;∀(t,m)∈𝒯×ℳ.I\_{c}(t,m)+I\_{d}(t,m)\leq 1;\quad\forall(t,m)\in\mathcal{T}\times\mathcal{M}. |  | (35) |

To ensure the total charge/discharge across all markets does not exceed the inverter/rectifier capacities, we impose the following constraints, which account for net charging or discharging:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mc​(t,m)−d​(t,m)≤Cinv;∀t∈𝒯\displaystyle\sum\_{\forall m\in M}c(t,m)-d(t,m)\leq C\_{\mathrm{inv}};\quad\forall t\in\mathcal{T} |  | (36) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑∀m∈Mc​(t,m)−d​(t,m)≤−Cinv;∀t∈𝒯.\displaystyle\sum\_{\forall m\in M}c(t,m)-d(t,m)\leq-C\_{\mathrm{inv}};\quad\forall t\in\mathcal{T}. |  | (37) |

### 4.3 State of health

With every cycle, the battery loses capacity, such that it is not able to return to its original maximum capacity; this degradation accrues over time as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​O​H​(t)=S​O​H​(t−1)−ηdeg​∑m∈Md​(t,m);∀t∈𝒯∖{t0}.SOH(t)=SOH(t-1)-\eta\_{\mathrm{deg}}\sum\_{m\in M}d(t,m);\quad\forall t\in\mathcal{T}\setminus\{t\_{0}\}. |  | (38) |

To limit degradation, a cycling constraint is imposed on the battery such that a pre-specified the number of cycles performed per year is bounded. This constrains the total discharge by imposing a cumulative hourly limit on the cycles as dictated by the S​O​HSOH:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1ηbatt​∑t∈𝒯∑m∈ℳd​(t,m)≤124​Cmax​∑t∈𝒯S​O​H​(t).\frac{1}{\eta\_{\mathrm{batt}}}\sum\_{t\in\mathcal{T}}\sum\_{m\in\mathcal{M}}d(t,m)\leq\frac{1}{24}C\_{\mathrm{max}}\sum\_{t\in\mathcal{T}}SOH(t). |  | (39) |

### 4.4 Cost function

For the BESS system, we aim to maximize system profits or, to follow convention from [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), minimize negative losses, i.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒB​E​S​S​(𝐗,𝐘,𝐜,ξ)=−(𝐏𝐭𝟎⊤​(𝐜𝐭𝟎−𝐝𝐭𝟎)+𝐏𝐭𝐨𝐛𝐬⊤​(𝐜𝐭𝐨𝐛𝐬−𝐝𝐭𝐨𝐛𝐬)).\mathcal{L}\_{BESS}(\mathbf{X,Y,c},\xi)=-(\mathbf{P\_{t\_{0}}}^{\top}(\mathbf{c\_{t\_{0}}}-\mathbf{d\_{t\_{0}}})+\mathbf{P\_{t\_{obs}}}^{\top}(\mathbf{c\_{t\_{obs}}}-\mathbf{d\_{t\_{obs}}})). |  | (40) |

This system does not contain a capital cost term, as we found capital cost problems to be unbounded toward maximizing battery capacity for this linear formulation in the absence of market feedback. Therefore, the capacity is fixed according to available resources, and we only consider the optimal stochastic scheduling problem.

When discretized in time, the overall sample-average approximation in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") for the BESS problem reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑m∈ℳ∑t∈𝒯0Pm,t​(cm,t−dm,t)+∑m∈ℳ∑t∈𝒯obs∑s∈𝒮πs​Pm,t,s​(cm,t,s−dm,t,s).\sum\_{m\in\mathcal{M}}\sum\_{t\in\mathcal{T}\_{0}}P\_{m,t}(c\_{m,t}-d\_{m,t})+\sum\_{m\in\mathcal{M}}\sum\_{t\in\mathcal{T}\_{\mathrm{obs}}}\sum\_{s\in\mathcal{S}}\pi\_{s}P\_{m,t,s}(c\_{m,t,s}-d\_{m,t,s}). |  | (41) |

## 5 Results

The formulation described in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") is deployed on the systems outlined in [section 3](https://arxiv.org/html/2510.27528v1#S3 "3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") with α=0.95\alpha=0.95. All optimization problems and data analysis were performed on an Apple M3 Pro CPU. In both case studies, we restrict ourselves to the "price-taker" assumption for simplicity; however, this has been shown to be detrimental to decision-making in energy settings at scale[[44](https://arxiv.org/html/2510.27528v1#bib.bib44), [45](https://arxiv.org/html/2510.27528v1#bib.bib45)]. Further, we use traditional stochastic optimization metrics like expected value of perfect information (EVPI) and value of stochastic solution (VSS) [[46](https://arxiv.org/html/2510.27528v1#bib.bib46)] to assess the impact of the proposed scheme on the respective systems. While these metrics do not explicitly account for the potential benefits of constraining tail risk, they can be used to quantify the sacrifice in expected cost induced by varying levels of risk aversion. To account for the benefit of constraining tail risk, we compute an adjusted VSSCVaR\mathrm{VSS}\_{\mathrm{CVaR}} metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VSSCVaR=VSS+(CVaRSP∞−CVaRSPϵ)+(E​[ℒSP∞]−E​[ℒSPϵ]),\mathrm{VSS}\_{\mathrm{CVaR}}=\mathrm{VSS}+(\mathrm{CVaR\_{SP\_{\infty}}}-\mathrm{CVaR}\_{\mathrm{SP}\_{\epsilon}})+(E[\mathcal{L}\_{\mathrm{SP}\_{\infty}}]-E[\mathcal{L}\_{\mathrm{SP}\_{\epsilon}}]), |  | (42) |

which penalizes losses induced on the expected cost by constraining CVaR, while also accounting for reductions in tail risk by computing the differences between a stochastic problem (SP) without an active CVaR constraint ϵ=∞\epsilon=\infty to those with a CVaR constraint with bound ϵ\epsilon. To compute these metrics, we also distinguish between the expected solution of the expected value problem (EEV) (i.e., optimizing the first stage subject to the expected value of uncertainty and providing the first stage-solution to solve a second stage problem) and the wait-and-see problem (WS) (i.e., the expected solution having perfect information of the uncertainties).

The two case studies outlined in [section 3](https://arxiv.org/html/2510.27528v1#S3 "3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") and [section 4](https://arxiv.org/html/2510.27528v1#S4 "4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") are used to test the proposed scheme. Both case studies are optimized on a yearly horizon where an averaged price trajectory is used for the first stage and second-stage price trajectories are sampled from the distribution ξ∼𝒩​(𝐏𝐨𝐛𝐬,𝐧𝐨𝐦,σobs2)\xi\sim\mathcal{N}(\mathbf{P\_{obs,nom}},\sigma\_{\mathrm{obs}}^{2}) as shown in [Figure 4](https://arxiv.org/html/2510.27528v1#S5.F4 "Figure 4 ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). Alternative scenario-generation methods (e.g., [[47](https://arxiv.org/html/2510.27528v1#bib.bib47)]) are also available in the literature.

![Refer to caption](Figures/Extra_traj_fix.png)


Figure 4: Two-stage stochastic price structure - first-stage (initial trajectory) deterministic, second-stage (latter trajectory) uncertain.

### 5.1 Yearly optimization of IHS

The process model 𝐟\mathbf{f}, which imposes physical constraints for optimization of the IHS, is outlined in [subsection 3.1](https://arxiv.org/html/2510.27528v1#S3.SS1 "3.1 Electrolyzer ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems")-[subsection 3.6](https://arxiv.org/html/2510.27528v1#S3.SS6 "3.6 Cost function ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). For this process, we aim to minimize capital and operating cost of the hydrogen production, storage, and conversion into electricity. Historical 2024 New England Independent Systems Operator (ISO-NE) hourly price data were retrieved from the United States Energy Information Administration [[48](https://arxiv.org/html/2510.27528v1#bib.bib48)] to be used as inputs for optimization. These represent the nominal electricity price trajectories 𝐏𝐭𝟎,𝐧𝐨𝐦\mathbf{P\_{t\_{0},nom}} and 𝐏𝐨𝐛𝐬,𝐧𝐨𝐦\mathbf{P\_{obs,nom}} denominated in $US/MWh. We assume a value of σobs=$​20\sigma\_{\mathrm{obs}}=\mathdollar 20/MWh as the price distribution standard deviation. This nominal and standard deviation parametrize the distribution of second-stage costs. The stochastic optimization of this system aims to optimally size the unit capacities at investment time, allowing for the operating decisions to be determined at a later time.

We conducted a sensitivity analysis to understand the scaling between the number of scenarios, CPU time, and stability of solution afforded by the SAA. For this, we assume that true price trajectories can be observed after optimization of the design variables (i.e., tobs=0t\_{\mathrm{obs}}=0 hours). This observation setting corresponds to the case where the price trajectories are revealed upon completion of the plant build and at the beginning of operation of the IHS. Observation settings where tobs>0t\_{\mathrm{obs}}>0 correspond to cases where the price trajectories (i.e., whether prices are rising or falling) are not precisely known when plant operation begins. The former setting is used for sensivitiy analysis as it produces the case with the most decision variables, and hence the most computational effort, as it requires no non-anticipativity constraints in the time domain. The results from this sensitivity analysis are displayed in [Figure 5](https://arxiv.org/html/2510.27528v1#S5.F5 "Figure 5 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems").

![Refer to caption](Figures/Figure4.png)


Figure 5: Scaling of computational effort with discretization quality for IHS.

Based on the trade-offs between computation requirements and solution quality shown in [Figure 5](https://arxiv.org/html/2510.27528v1#S5.F5 "Figure 5 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), we choose to formulate the SAA with ns=35n\_{s}=35 samples to balance computational load and approximation accuracy. In principle, many more scenarios can be used for a yearly optimization setting, as the solution does not need to be deployed online; however, this solution provides adequate solution stability to perform many optimization runs for comprehensive testing.

We proceed to explore the trade-off between tail-risk, as measured by operating CVaR, and expected IHS cost by performing sensitivity analyses on the observation time tobst\_{\mathrm{obs}} and the CVaR bound ϵ\epsilon. [Table 4](https://arxiv.org/html/2510.27528v1#S5.T4 "Table 4 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") and [Table 5](https://arxiv.org/html/2510.27528v1#S5.T5 "Table 5 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") summarize these results. As shown in [Table 4](https://arxiv.org/html/2510.27528v1#S5.T4 "Table 4 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), the solutions of all stochastic optimization problems, and that of the EEV problem, do note include building a fuel cell. The former can be attributed to the fact that the stochastic program must hedge against scenarios in which there are low energy prices, hence performing hydrogen arbitrage would be economically unfavorable given the capital expenditure (i.e., the possibility of low prices induces sunk cost risk aversion). In contrast, the solution to the EEV problem does not include a fuel cell, as the nominal energy price timeseries does not contain high enough values to offset hydrogen production costs by reconverting to energy. These are contrasted to the case of perfect information (WS), where a small fuel cell is built on expectation as the potential gains from the known high price scenarios outweigh the costs from the low price scenarios. Note these analyses may change for more efficient fuel cell technologies, which could vary the parameters in [Table 1](https://arxiv.org/html/2510.27528v1#S3.T1 "Table 1 ‣ 3 Integrated hydrogen system ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems").

Interestingly, the solutions to all optimization formulations aside from the WS problem and the stochastic problems with tobs=0t\_{\mathrm{obs}}=0 hours include a compressor capacity equal to its lower bound. In the SPs, this occurs as there is large time-dependent uncertainty in the electricity prices as a single averaged price is not used for any portion of the trajectory when tobs=0t\_{\mathrm{obs}}=0 hours, hence the compressor must over-build to accommodate for the possibility of supplying the DRI through the storage unit. As a fuel cell is built in the case of the WS case, more compression is required for supply to the cell.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tobst\_{\mathrm{obs}} | ϵ\epsilon | CelecC\_{\mathrm{elec}} | CstorC\_{\mathrm{stor}} | CheatC\_{\mathrm{heat}} | CcompC\_{\mathrm{comp}} | Cf​cC\_{fc} | JcapJ^{\mathrm{cap}} |
| (hr) | ($mn) | (GW) | (tn) | (MW) | (MW) | (MW) | ($k) |
| EEV | | 8.818.81 | 0.1710.171 | 656656 | 100100 | 0 | 353353 |
| WS | | 9.749.74 | 0.2260.226 | 680680 | 142142 | 483483 | 414414 |
| 0 | ∞\infty | 9.089.08 | 0.2190.219 | 723723 | 193193 | 0 | 369369 |
| 5.8005.800 | 9.929.92 | 0.2580.258 | 734734 | 196196 | 0 | 379379 |
| 5.7505.750 | 10.3510.35 | 0.5300.530 | 823823 | 221221 | 0 | 450450 |
| 5.7005.700 | 11.9211.92 | 0.8270.827 | 947947 | 254254 | 0 | 542542 |
| 22002200 | ∞\infty | 8.938.93 | 0.1960.196 | 708708 | 100100 | 0 | 360360 |
| 5.8005.800 | 9.199.19 | 0.2660.266 | 727727 | 100100 | 0 | 378378 |
| 5.7505.750 | 10.2910.29 | 0.5440.544 | 814814 | 100100 | 0 | 449449 |
| 5.7005.700 | 11.8611.86 | 0.8430.843 | 938938 | 100100 | 0 | 540540 |
| 44004400 | ∞\infty | 8.848.84 | 0.1780.178 | 682682 | 100100 | 0 | 355355 |
| 5.8005.800 | 9.189.18 | 0.2700.270 | 702702 | 100100 | 0 | 378378 |
| 5.7505.750 | 10.2710.27 | 0.5520.552 | 773773 | 100100 | 0 | 449449 |
| 5.7005.700 | 11.7911.79 | 0.8460.846 | 876876 | 100100 | 0 | 540540 |

Table 4: Expected design and capital decisions for varying IHS stochastic program hyperparameters.

Comparing across the stochastic problems, there is large upward monotonicity in the electrolyzer, storage, and heat capacities with increasing risk aversion (decreasing ϵ\epsilon). As CVaR is more constrained, the solutions to the stochastic program are more conservative, including increasing capacities to accommodate for extreme scenarios that could lead to high losses. Crucially, this overcapacity allows for larger hydrogen stores and heating supply to ensure that the DRI demand is met at all times. These overcapacities are all further reflected in increasing capital cost with increasing CVaR bound.

The observation time has a smaller, but opposite, effect to the risk aversion level. Increasingly delayed observations of the true price trajectories cause lower capacities to be built; this occurs as an averaged electricity price trajectory is used for the first stage, which the stochastic program takes as the “true” price. The use of a sample-averaged trajectory over long periods of time forces the solution of the stochastic program to include capacity that optimizes the sample-averaged objective, rather than to hedge against potential uncertainties by building overcapacity. The suboptimalities induced by this approximation are reflected in the operating costs outlined in [Table 5](https://arxiv.org/html/2510.27528v1#S5.T5 "Table 5 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems").

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tobst\_{\mathrm{obs}} | ϵ\epsilon | CVaR\mathrm{CVaR} | Eξ​[ℒ]E\_{\xi}[\mathcal{L}] | Eξ​[JI​Do​p]Eξ​[JD​Ao​p]\frac{E\_{\xi}[J^{op}\_{ID}]}{E\_{\xi}[J^{op}\_{DA}]} | EVPI | VSS | VSSCVaR\mathrm{VSS\_{CVaR}} |
| (hr) | ($mn) | ($mn) | ($mn) | −- | ($k) | ($k) | ($k) |
|  | WS | | 2.7162.716 | 1.2781.278 | −- | −- | −- |
| 0 | EEV | | 2.7992.799 | 1.2841.284 | 8383 | −- | −- |
| ∞\infty | 5.8105.810 | 2.7352.735 | 1.2991.299 | 1919 | 6363 | 6363 |
| 5.8005.800 | | 2.7362.736 | 1.3081.308 | 2020 | 6363 | 121121 |
| 5.7505.750 | | 2.7482.748 | 1.3631.363 | 3232 | 5050 | 146146 |
|  | 5.7005.700 | | 2.7762.776 | 1.4121.412 | 6060 | 2323 | 140140 |
| 22002200 | EEV | | 2.7992.799 | 1.2831.283 | 8383 | −- | −- |
| ∞\infty | 5.8505.850 | 2.7362.736 | 1.2901.290 | 2121 | 6262 | 6262 |
| 5.8005.800 | | 2.7382.738 | 1.3081.308 | 2222 | 6161 | 109109 |
| 5.7505.750 | | 2.7532.753 | 1.3621.362 | 3737 | 4646 | 129129 |
|  | 5.7005.700 | | 2.7852.785 | 1.4181.418 | 6969 | 1414 | 116116 |
| 44004400 | EEV | | 2.8002.800 | 1.2831.283 | 8383 | −- | −- |
| ∞\infty | 5.8505.850 | 2.7382.738 | 1.2891.289 | 2121 | 6262 | 6262 |
| 5.8005.800 | | 2.7402.740 | 1.3081.308 | 2424 | 5959 | 107107 |
| 5.7505.750 | | 2.7572.757 | 1.3641.364 | 4141 | 4242 | 123123 |
|  | 5.7005.700 | | 2.7922.792 | 1.4191.419 | 7676 | 77 | 103103 |

Table 5: Operating costs and stochastic summary metrics for varying IHS stochastic program hyperparameters.

As shown in [Table 5](https://arxiv.org/html/2510.27528v1#S5.T5 "Table 5 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), increasingly delayed observations correspond to larger expected costs. Intuitively, the earlier one can access true price information, the better decisions one can take.
This results in lower VSS (i.e., lower benefits in optimizing stochastically) but higher EVPI (i.e., more solution suboptimality with respect to the wait-and-see problem).

We found the ratio of ID to DA costs to increase with risk aversion (lower ϵ\epsilon). This may be attributed to the over-sized capacities shown in [Table 4](https://arxiv.org/html/2510.27528v1#S5.T4 "Table 4 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"); these enable the risk-averse solutions to store energy from periods of low ID prices, which have more volatility. The trade-off between risk aversion and expected cost is also shown in [Figure 6](https://arxiv.org/html/2510.27528v1#S5.F6 "Figure 6 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") for varying tobst\_{\mathrm{obs}}.

![Refer to caption](Figures/Figure5.png)


Figure 6: Trade-off between expected cost and risk aversion for IHS.

As shown in [Figure 6](https://arxiv.org/html/2510.27528v1#S5.F6 "Figure 6 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), there is a risk-reward trade-off between CVaR and expected IHS cost. Tighter CVaR bounds increase the expected cost of the system while limiting extreme losses. In general, the range of expected cost sacrifice is ≈$​60\approx\mathdollar 60k while the potential reductions in CVaR have a range of ≈$​150\approx\mathdollar 150k; hence the potential benefits outweigh the cost. The lowest expected cost occurs when CVaR is not constrained (i.e., ϵ=∞\epsilon=\infty); this results in CVaR≈$​5.85\mathrm{CVaR}\approx\mathdollar 5.85mn beyond which expected cost cannot be reduced to the level exhibited by the wait-and-see (perfect information) solution; this gap represents the EVPI. The largest expected costs occur when the CVaR bound is tightened to (i.e., ϵ=$​5.7\epsilon=\mathdollar 5.7mn), beyond which CVaR cannot be reduced. Nevertheless, these solutions with the tightest risk bounds outperform the EEV solutions; this gap represents the VSS. The benefits of modeling tail risk are evident in the VSSCVaR\mathrm{VSS\_{CVaR}} as VSSCVaR≥VSS\mathrm{VSS\_{CVaR}\geq VSS} for all risk-constrained scenarios; this means that the tail risk avoided is greater than the respective increase in expected cost incurred. That is, there is always an outsized benefit in the trade-off betweeen expected value and CVaR for the IHS case study.

### 5.2 Yearly optimization of BESS

The process model 𝐟\mathbf{f}, which imposes physical constraints for optimization of the BESS, is outlined in [subsection 4.1](https://arxiv.org/html/2510.27528v1#S4.SS1 "4.1 State of charge ‣ 4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems")-[subsection 4.3](https://arxiv.org/html/2510.27528v1#S4.SS3 "4.3 State of health ‣ 4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). For this process, we aim to maximize the operating profit of the energy arbitrage enabled by battery storage. Price data were generated based on in-house BP predictions to be used for optimization; these represent the nominal electricity price trajectories 𝐏𝐭𝟎,𝐧𝐨𝐦\mathbf{P\_{t\_{0},nom}} and 𝐏𝐨𝐛𝐬,𝐧𝐨𝐦\mathbf{P\_{obs,nom}} denominated in €/M​W​h/MWh. This yearly optimization setting corresponds to various potential power purchase agreements (PPAs) according to the observation time tobst\_{\mathrm{obs}}. Specifically, tobs=0t\_{\mathrm{obs}}=0 corresponds to a fixed PPA where the electricity prices are fixed at agreement time; conversely, tobs>0t\_{\mathrm{obs}}>0 corresponds to flexible PPAs where the prices are initially variable and then fixed (i.e., revealed) after a given amount of time.

Similarly to the IHS, we first conduct a sensitivity analysis to understand the scaling between the number of scenarios, CPU time, and stability of solution afforded by the SAA. σobs=\sigma\_{\mathrm{obs}}=\;€ 30\;30/MWh is assumed. The results from this sensitivity analysis are shown in [Figure 7](https://arxiv.org/html/2510.27528v1#S5.F7 "Figure 7 ‣ 5.2 Yearly optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems").

![Refer to caption](Figures/Figure6.png)


Figure 7: Scaling of computational effort with discretization quality for BESS.

Based on the scaling of computation requirements and solution quality, we again choose to formulate our SAA using ns=35n\_{s}=35 samples to balance computational load and approximation accuracy. Since this system is subject to the same uncertainties (i.e., energy prices) and solves the same energy allocation problem (albeit in a different system), the scaling of computational effort follows a similar trend as in the IHS ([Figure 5](https://arxiv.org/html/2510.27528v1#S5.F5 "Figure 5 ‣ 5.1 Yearly optimization of IHS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems")).

We examine the trade-off between the tail risk and expected arbitrage profit under various choices for tha values of optimization hyperparameters, as summarized in [Table 6](https://arxiv.org/html/2510.27528v1#S5.T6 "Table 6 ‣ 5.2 Yearly optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). We note that the expected costs are denoted with a negative sign (i.e., −Eξ​[ℒ]-E\_{\xi}[\mathcal{L}]) as the values correspond to profits, following the minimization convention in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), which is common in the literature. For the BESS case study, we again observe the expected profit to be more sensitive to risk bound than to observation time. Tightening risk bounds (i.e., constraining potential losses) and delaying observation times again both result in decreasing expected profits. The tail risks (CVaR) and risk bounds (ϵ\epsilon) all fall in the non-negative range, as the tail risk constitutes overall loss or break-even scenarios, respectively. With a tail risk range of ≈\approx\;€ 1.25\;1.25mn, using a risk-constrained approach can effectively eliminate the possibility of losses by sacrificing ≈\approx\;€ 506\;506k in the lowest profit scenario (i.e., a late observation time).

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tobst\_{\mathrm{obs}} | ϵ\epsilon | CVaR\mathrm{CVaR} | −Eξ​[ℒ]-E\_{\xi}[\mathcal{L}] | Eξ​[JI​Do​p]Eξ​[JD​Ao​p]\frac{E\_{\xi}[J^{op}\_{ID}]}{E\_{\xi}[J^{op}\_{DA}]} | EVPI | VSS | VSSCVaR\mathrm{VSS\_{CVaR}} |
| (hr) | (€mn) | (€mn) | (€mn) | −- | (€k) | (€k) | (€k) |
|  | WS | | 4.4674.467 | 293293 | −- | −- | −- |
| 0 | EEV | | 4.4674.467 | 299299 | 0.50.5 | −- | −- |
| ∞\infty | 1.251.25 | 4.4674.467 | 293293 | 0 | 0.50.5 | 0.50.5 |
| 1.001.00 | | 4.4654.465 | 469469 | 2.42.4 | −1.9-1.9 | 245.8245.8 |
| 0.750.75 | | 4.4554.455 | −419-419 | 12.412.4 | −11.9-11.9 | 475.7475.7 |
|  | 0.500.50 | | 4.4244.424 | −81-81 | 43.843.8 | −43.3-43.3 | 662.9662.9 |
|  | 0.250.25 | | 4.3434.343 | −36-36 | 124.5124.5 | −124.0-124.0 | 751.5751.5 |
|  | 0.000.00 | | 4.1124.112 | −16-16 | 355.2355.2 | −354.7-354.7 | 540.0540.0 |
| 22002200 | EEV | | 4.4644.464 | 296296 | 3.73.7 | −- | −- |
| ∞\infty | 1.251.25 | 4.4664.466 | 284284 | 1.81.8 | 2.02.0 | 2.02.0 |
| 1.001.00 | | 4.4614.461 | 457457 | 5.65.6 | −1.9-1.9 | 244.3244.3 |
| 0.750.75 | | 4.4454.445 | −189-189 | 21.921.9 | −18.1-18.1 | 461.8461.8 |
|  | 0.500.50 | | 4.4024.402 | −51-51 | 65.065.0 | −61.2-61.2 | 625.4625.4 |
|  | 0.250.25 | | 4.3024.302 | −24-24 | 165.1165.1 | −161.3-161.3 | 675.3675.3 |
|  | 0.000.00 | | 4.0464.046 | −14-14 | 421.3421.3 | −417.5-417.5 | 412.9412.9 |
| 44004400 | EEV | | 4.4574.457 | 411411 | 10.810.8 | −- | −- |
| ∞\infty | 1.251.25 | 4.4634.463 | 440440 | 4.64.6 | 6.26.2 | 6.26.2 |
| 1.001.00 | | 4.4564.456 | 898898 | 11.011.0 | −0.3-0.3 | 243.3243.3 |
| 0.750.75 | | 4.4324.432 | −113-113 | 35.435.4 | −24.6-24.6 | 444.6444.6 |
|  | 0.500.50 | | 4.3754.375 | −40-40 | 92.092.0 | −81.2-81.2 | 581.3581.3 |
|  | 0.250.25 | | 4.2574.257 | −20-20 | 210.2210.2 | −199.4-199.4 | 595.9595.9 |
|  | 0.000.00 | | 3.9613.961 | −13-13 | 506.1506.1 | −495.3-495.3 | 253.1253.1 |

Table 6: Operating costs and stochastic summary metrics for varying BESS stochastic program hyperparameters.

We note that the market participation ratio is negative in some settings, corresponding to when losses are incurred in the DA market and all profits are made from participation in the ID market. The majority of the expected profit comes from the ID market, because its large volatility produces the best buying and selling opportunities for arbitrage. However, the participation in the DA market increases with tightening risk bound as more overall energy is bought to increase the inventory over time. Intuitively, balancing participation in the more aggressive ID market and the more conservative DA market enables controlling the risk-reward tradeoff.

From a stochastic optimization perspective, the expected value of perfect information (EVPI) is very sensitive to the risk bound as the risk tolerance induces large gaps in profit with respect to the wait-and-see (WS) problem. Furthermore, the value of stochastic solution (VSS) in this case can be negative as the expected solution of the expected value problem (EEV) outperforms the risk-constrained stochastic problem (SP); this is owed to the expected profit reduction induced when constraining CVaR. However, when considering the potential for risk avoidance, the benefits for constraining risk as reflected in VSSCVaR\mathrm{VSS\_{CVaR}} are again significant, with maximum benefits of ≈\approx\;€ 675\;675k. Similarly to in the IHS case study, the potential losses incurred by limiting risk are outweighed by the benefit according to this metric.

![Refer to caption](Figures/Figure7.png)


Figure 8: Trade-off between expected cost and risk aversion for BESS.

The risk-reward trade-off for the BESS is shown in [Figure 8](https://arxiv.org/html/2510.27528v1#S5.F8 "Figure 8 ‣ 5.2 Yearly optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). All EEV, unbounded SP, and WS solutions have similar expected profits; this is reflective of the relatively low VSS and EVPI. Conversely, the large range of CVaR can also be observed, which reflects the high risk profile of the BESS arbitrage problem. Irrespective of the observation time, the CVaR can always be reduced to zero, which constitutes a break-even scenario. The ability constrain tail risk from a loss regime to a break-even regime is especially powerful for risk-averse operators, which elucidates the benefits afforded by CVaR-constrained optimization.

### 5.3 Rolling horizon optimization of BESS

As the BESS system does not require any capacity decisions, a risk-constrained formulation can also be deployed in a rolling horizon manner for online operation. As depicted in [Figure 9](https://arxiv.org/html/2510.27528v1#S5.F9 "Figure 9 ‣ 5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), a rolling horizon approach can continually re-optimize the charge/discharge policy of the system at a fixed time interval. By performing this re-optimization, updated price projections that comprise the scenario set can be incorporated into the stochastic optimization problem. Previous works also support that rolling-horizon optimization itself helps mitigate problem uncertainty [[49](https://arxiv.org/html/2510.27528v1#bib.bib49), [30](https://arxiv.org/html/2510.27528v1#bib.bib30), [50](https://arxiv.org/html/2510.27528v1#bib.bib50), [51](https://arxiv.org/html/2510.27528v1#bib.bib51)]. A rolling horizon stochastic optimization approach has been applied to energy storage systems previously [[52](https://arxiv.org/html/2510.27528v1#bib.bib52)] and can leverage market timings where DA prices are set through auction in advance of the energy actually being deployed while the intraday prices are determined in a spot market with a central tendency around the previously-set DA price.

This online setting corresponds to a live energy trading case in which DA comitments are made before DA prices are determined and ID prices follow a noisy distribution around the DA trajectories. Following the rolling-horizon approach, we forego the temporal partitioning of here-and-now and wait-and-see variables presented in [section 4](https://arxiv.org/html/2510.27528v1#S4 "4 Battery Energy Storage System ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") in order to exploit the market structure. The risk-constrained two-stage problem for this approach has the first-stage decisions 𝐗=[𝐜𝐃𝐀𝐝𝐃𝐀]⊤\mathbf{X}=\begin{bmatrix}\mathbf{c\_{DA}}&\mathbf{d\_{DA}}\end{bmatrix}^{\top}, where 𝐜𝐃𝐀∈𝒞D​A⊂ℝ|𝒯|\mathbf{c\_{DA}}\in\mathcal{C}\_{DA}\subset\mathbb{R}^{|\mathcal{T}|} are the charge and 𝐝𝐃𝐀∈𝒟D​A⊂ℝ|𝒯|\mathbf{d\_{DA}}\in\mathcal{D}\_{DA}\subset\mathbb{R}^{|\mathcal{T}|} are the discharge dispatch from the grid. This formulation determines a single dispatch for the DA actions that is optimal for the whole scenario set for as the prices have yet to be realized by auction. The second stage decisions are the charge/discharge dispatch decision in the intraday market 𝐘=[𝐜𝐈𝐃𝐝𝐈𝐃]⊤\mathbf{Y}=\begin{bmatrix}\mathbf{c\_{ID}}&\mathbf{d\_{ID}}\end{bmatrix}^{\top} where 𝐜𝐈𝐃∈𝒞I​D​(𝐜𝐃𝐀,𝐝𝐃𝐀)⊂ℝ|𝒯|\mathbf{c\_{ID}}\in\mathcal{C}\_{ID}(\mathbf{c\_{DA}},\mathbf{d\_{DA}})\subset\mathbb{R}^{|\mathcal{T}|} and 𝐝𝐈𝐃∈𝒟I​D​(𝐜𝐃𝐀,𝐝𝐃𝐀)⊂ℝ|𝒯|\mathbf{d\_{ID}}\in\mathcal{D}\_{ID}(\mathbf{c\_{DA}},\mathbf{d\_{DA}})\subset\mathbb{R}^{|\mathcal{T}|}. Noticing that, once the DA prices are revealed, the ID prices follow their general trend (albeit noisily), we assume that the decisions corresponding to one of the scenarios in the scenario set are implemented as recourse. Accordingly, the first-stage price vector is 𝐜=𝐏𝐃𝐀∈ℝ|𝒯|\mathbf{c}=\mathbf{P\_{DA}}\in\mathbb{R}^{|\mathcal{T}|} and second-stage uncertain price vector is the multivariate distribution ξ=𝐏𝐈𝐃∈Ψ⊂ℝ|𝒯|\mathbf{\xi}=\mathbf{P\_{ID}}\in\Psi\subset\mathbb{R}^{|\mathcal{T}|}. As implied by the dimensionality of the variables, the time horizon 𝒯\mathcal{T} is used, which corresponds to a year-long window. The charge and discharge decisions for each day are further constrained according to the previous day’s decisions by continually updating the S​O​CSOC and S​O​HSOH of the model. When discretized in time, the overall sample-average approximation in [subsection 2.3](https://arxiv.org/html/2510.27528v1#S2.Ex1 "2.3 Risk-constrained two-stage stochastic optimization ‣ 2 Methodology ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") for the BESS rolling horizon problem reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t∈𝒯PD​A,t​(cD​A,t−dD​A,t)+∑t∈𝒯∑s∈𝒮πs​PI​D,t,s​(cI​D,t,s−dI​D,t,s).\sum\_{t\in\mathcal{T}}P\_{DA,t}(c\_{DA,t}-d\_{DA,t})+\sum\_{t\in\mathcal{T}}\sum\_{s\in\mathcal{S}}\pi\_{s}P\_{ID,t,s}(c\_{ID,t,s}-d\_{ID,t,s}). |  | (43) |

![Refer to caption](x4.png)


Figure 9: Stochastic rolling horizon operation of BESS schedule.

We perform the rolling horizon optimization of a single week of BESS operation. As displayed in [Table 7](https://arxiv.org/html/2510.27528v1#S5.T7 "Table 7 ‣ 5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), we report cumulative metrics to account for each day optimized, and we impose risk constraints (ϵ\epsilon) that correspond to annualized values since a year-long window is used. In contrast to the year-long formulation without feedback, not all of the solutions to weekly optimization problems solved in the weekly operating period can limit the risk to a break-even (ϵ=0\epsilon=0) setting; hence, this row is omitted from [Table 7](https://arxiv.org/html/2510.27528v1#S5.T7 "Table 7 ‣ 5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). For the week considered, the optimal solutions do not involve participation in the DA market at all, and we therefore omit the market participation ratio. This corroborates the previous results in [subsection 5.2](https://arxiv.org/html/2510.27528v1#S5.SS2 "5.2 Yearly optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") where the optimal results involve very little participation in the DA market. In the current setting, where participation in the DA market is optimized as a here-and-now decision, the stochastic program chooses the best policy is to wholly adapt its dispatch to a given charge level that corresponds to an ID trajectory centered around the DA auction prices.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ϵ\epsilon | ∑CVaR\sum\mathrm{CVaR} | −∑Eξ​[ℒ]-\sum E\_{\xi}[\mathcal{L}] | ∑\sum EVPI | ∑\sum VSS | ∑VSSCVaR\sum\mathrm{VSS\_{CVaR}} |
| (€mn) | (€k) | (€k) | (€k) | (€k) | (€k) |
| WS | | 0.10.1 | −- | −- | −- |
| EEV | | −35.2-35.2 | 35.335.3 | −- | −- |
| ∞\infty | 3232 | −2.6-2.6 | 2.72.7 | 32.632.6 | 32.632.6 |
| 11 | 2828 | −2.5-2.5 | 2.62.6 | 32.732.7 | 32.832.8 |
| 0.750.75 | 2121 | −2.5-2.5 | 2.62.6 | 32.732.7 | 32.832.8 |
| 0.50.5 | 1919 | −1.9-1.9 | 2.02.0 | 33.233.2 | 33.933.9 |
| 0.250.25 | 1414 | −0.9-0.9 | 1.01.0 | 34.234.2 | 35.935.9 |

Table 7: Operating costs and stochastic summary metrics for varying BESS rolling horizon stochastic program hyperparameters. Sums (∑\sum) denote cumulative quantities for a week of operation.

As illustrated in [Figure 10](https://arxiv.org/html/2510.27528v1#S5.F10 "Figure 10 ‣ 5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") and summarized in [Table 7](https://arxiv.org/html/2510.27528v1#S5.T7 "Table 7 ‣ 5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"), the risk-constrained formulation outperforms the EEV solution, while only being slightly suboptimal to the WS solution (i.e., a high VSS and a low EVPI). In general, most of the VSS comes from the poor performance of the EEV problem, where the VSSCVaR\mathrm{VSS\_{CVaR}} is nearly equivalent. However, with longer operating periods, we expect for the performance of the EEV to average out and for the SP to provide more benefit owing to risk avoidance as in [subsection 5.2](https://arxiv.org/html/2510.27528v1#S5.SS2 "5.2 Yearly optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems"). Counterintuitively, the expected cost in this case is lower with tighter risk bounds. This is potentially a result of the week being optimized, where a more aggressive charging policy in fact constitutes the most risk-averse strategy. [Figure 10](https://arxiv.org/html/2510.27528v1#S5.F10 "Figure 10 ‣ 5.3 Rolling horizon optimization of BESS ‣ 5 Results ‣ Risk-constrained stochastic scheduling of multi-market energy storage systems") also shows some non-monotonicity in the expected profit as the risk bound approaches the non-constrained region. This occurs as limiting the CVaR does not guarantee overall monotonicity in the time domain, where several risk-averse problems are performed iteratively. In other words, the most conservative closed-loop (rolling horizon) solution does not necessarily correspond to the most conservative open-loop solution. Nevertheless, this operational scheme exhibits close performance to the perfect information (WS) solution despite the presence of uncertainty while also providing shorfall-limiting potential.

![Refer to caption](Figures/Figure9.png)


Figure 10: Trade-off between expected cost and risk aversion for BESS rolling horizon operation.

## 6 Conclusion

A risk-constrained stochastic approach was proposed for the scheduling optimization of energy storage systems under energy market uncertainty. The risk-constrained approach allows for explicit specification of the operator’s tolerance for risk rather than using a heuristic objective weight. This approach was tested in IHS and BESS case studies; the former includes capacity and dispatch decisions while the latter only involves dispatch but was also applied in a rolling horizon manner. Both systems were subject to DA and ID electricity markets whereby the optimizer determined the charge and discharge at each point in time to each market. This variety of settings across our case studies elucidates the flexibility of our framework to address uncertainty in scheduling for integrated design and operation, fixed or flexible PPA, and live trading uses.

Both systems exhibit a trade-off between the expected cost/profit and the tail risk. In the IHS cost minimization setting, higher expected costs resulted in an outsized constraining of the CVaRs. Further, a weaker correlation with the observation time of the true price signal was observed. The first-stage decisions are manifested in the IHS system through the unit sizes whereby large capacities were built for tighter risk bounds. This comes at the expense of capital cost but allows for larger inventories to be held at any given time; hence more participation in the ID market to take advantage of large price spreads. The relationship between expected operational profit and tail risk was evident to a larger extent on the BESS system, where profit was sacrificed to limit potential tail losses. Indeed, using an optimal risk-constrained schedule on the BESS system can shift the CVaR for a loss to a break-even regime. As in the IHS, the BESS arbitrage was observed to make an increasing amount of profit from the ID market with increasing risk aversion; this is reflected in order-of-magnitude larger ID profits and, in some cases, net losses to the DA market. As larger price spreads occur owed to ID volatility, this large proportion of ID market profit is appropriate in the arbitrage context. In a rolling horizon implementation, the stochastic optimization of the BESS system resulted in significant improvements over the expected value problem with only small deterioration with respect to the perfect information problem. Through both case studies, we show potential net benefits in design, open-loop scheduling, and closed-loop scheduling settings; this positions risk-constrained scheduling as a powerful option to abate risk in energy storage systems.

Despite the evident benefits of the risk-constrained optimization approach deployed herein, computational limitations remain in the scaling of computational effort and number of discretized price scenarios. This may be alleviated through the use of surrogates as done by Alcántara et al. [[53](https://arxiv.org/html/2510.27528v1#bib.bib53)], who used a quantile neural network to approximate second-stage expected value and CVaR in stochastic optimization. Using this approach can achieve a better balance between parsimony and distributional fidelity in future works. Further, we assumed herein that energy price uncertainty is Gaussian; however,the CVaR constrained approach by Rockafellar and Uryasev [[39](https://arxiv.org/html/2510.27528v1#bib.bib39)] is distribution-agnostic. Approaches for estimating skewed energy prices as in Matsumoto et al. [[54](https://arxiv.org/html/2510.27528v1#bib.bib54)] could be used to generate the price distributions for two-stage energy storage scheduling such that the effect of the energy price prior is better understood. Lastly, we assumed participation in the DA and ID market herein; ancillary markets such as frequency containment reserves and automatic frequency restoration reserves could be jointly considered in this formulation.

## Acknowledgments

The authors gratefully acknowledge funding from the bp International Centre for Advanced Materials (ICAM). LMPG and CT also acknowledge support from the EPSRC (grant EP/X025292/1). CT was supported by a BASF/Royal Academy of Engineering Senior Research Fellowship.

## References

* IEA [2025]

  IEA, Global energy review 2025, 2025. <https://www.iea.org/reports/global-energy-review-2025> [Acessed: 2025-06-16].
* Mallapragada et al. [2020]

  D. S. Mallapragada, N. A. Sepulveda, J. D. Jenkins,
  Long-run system value of battery energy storage in future grids with increasing wind and solar generation,
  Applied Energy 275 (2020) 115390.
* Koohi-Fayegh and Rosen [2020]

  S. Koohi-Fayegh, M. A. Rosen,
  A review of energy storage types, applications and recent developments,
  Journal of Energy Storage 27 (2020) 101047.
* European Commission [2023]

  European Commission, Energy storage - underpinning a decarbonised and secure eu energy system, 2023. <https://energy.ec.europa.eu/topics/research-and-technology/energy-storage_en> [Acessed: 2025-06-16].
* UK Department for Energy Security and Net Zero [2025]

  UK Department for Energy Security and Net Zero, Clean power 2030 action plan, 2025. <https://www.gov.uk/government/publications/clean-power-2030-action-plan> [Acessed: 2025-06-16].
* Ajanovic et al. [2022]

  A. Ajanovic, M. Sayer, R. Haas,
  The economics and the environmental benignity of different colors of hydrogen,
  International Journal of Hydrogen Energy 47 (2022) 24136–24154.
* Mallapragada et al. [2023]

  D. S. Mallapragada, Y. Dvorkin, M. A. Modestino, D. V. Esposito, W. A. Smith, B.-M. Hodge, M. P. Harold, V. M. Donnelly, A. Nuz, C. Bloomquist, et al.,
  Decarbonization of the chemical industry through electrification: Barriers and opportunities,
  Joule 7 (2023) 23–41.
* Ueckerdt et al. [2021]

  F. Ueckerdt, C. Bauer, A. Dirnaichner, J. Everall, R. Sacchi, G. Luderer,
  Potential and risks of hydrogen-based e-fuels in climate change mitigation,
  Nature Climate Change 11 (2021) 384–393.
* Lee et al. [2022]

  B. Lee, L. R. Winter, H. Lee, D. Lim, H. Lim, M. Elimelech,
  Pathways to a green ammonia future,
  ACS Energy Letters 7 (2022) 3032–3038.
* Ricks et al. [2023]

  W. Ricks, Q. Xu, J. D. Jenkins,
  Minimizing emissions from grid-based hydrogen production in the united states,
  Environmental Research Letters 18 (2023) 014025.
* Emrani and Berrada [2024]

  A. Emrani, A. Berrada,
  A comprehensive review on techno-economic assessment of hybrid energy storage systems integrated with renewable energy,
  Journal of Energy Storage 84 (2024) 111010.
* Pusceddu et al. [2021]

  E. Pusceddu, B. Zakeri, G. C. Gissey,
  Synergies between energy arbitrage and fast frequency response for battery energy storage systems,
  Applied Energy 283 (2021) 116274.
* Krishnamurthy et al. [2017]

  D. Krishnamurthy, C. Uckun, Z. Zhou, P. R. Thimmapuram, A. Botterud,
  Energy storage arbitrage under day-ahead and real-time price uncertainty,
  IEEE Transactions on Power Systems 33 (2017) 84–93.
* Nezamabadi and Vahidinasab [2020]

  H. Nezamabadi, V. Vahidinasab,
  Arbitrage strategy of renewable-based microgrids via peer-to-peer energy-trading,
  IEEE Transactions on Sustainable Energy 12 (2020) 1372–1382.
* Nan et al. [2018]

  S. Nan, M. Zhou, G. Li,
  Optimal residential community demand response scheduling in smart grid,
  Applied Energy 210 (2018) 1280–1289.
* Oikonomou et al. [2018]

  K. Oikonomou, M. Parvania, R. Khatami,
  Optimal demand response scheduling for water distribution systems,
  IEEE Transactions on Industrial Informatics 14 (2018) 5112–5122.
* Tsay et al. [2019]

  C. Tsay, A. Kumar, J. Flores-Cerrillo, M. Baldea,
  Optimal demand response scheduling of an industrial air separation unit using data-driven dynamic models,
  Computers & Chemical Engineering 126 (2019) 22–34.
* Li et al. [2023]

  J. Li, B. Yang, J. Huang, Z. Guo, J. Wang, R. Zhang, Y. Hu, H. Shu, Y. Chen, Y. Yan,
  Optimal planning of electricity–hydrogen hybrid energy storage system considering demand response in active distribution network,
  Energy 273 (2023) 127142.
* Zhang et al. [2020]

  L. Zhang, J. Kuang, B. Sun, F. Li, C. Zhang,
  A two-stage operation optimization method of integrated energy systems with demand response and energy storage,
  Energy 208 (2020) 118423.
* Tang and Wang [2019]

  R. Tang, S. Wang,
  Model predictive control for thermal energy storage and thermal comfort optimization of building demand response in smart grids,
  Applied Energy 242 (2019) 873–882.
* Silva et al. [2022]

  C. Silva, P. Faria, Z. Vale, J. Corchado,
  Demand response performance and uncertainty: A systematic literature review,
  Energy Strategy Reviews 41 (2022) 100857.
* Powell [2019]

  W. B. Powell,
  A unified framework for stochastic optimization,
  European journal of operational research 275 (2019) 795–821.
* Li and Grossmann [2021]

  C. Li, I. E. Grossmann,
  A review of stochastic programming methods for optimization of process systems under uncertainty,
  Frontiers in Chemical Engineering 2 (2021) 622241.
* Torres et al. [2022]

  J. J. Torres, C. Li, R. M. Apap, I. E. Grossmann,
  A review on the performance of linear and mixed integer two-stage stochastic programming software,
  Algorithms 15 (2022) 103.
* Filippi et al. [2020]

  C. Filippi, G. Guastaroba, M. G. Speranza,
  Conditional value-at-risk beyond finance: a survey,
  International Transactions in Operational Research 27 (2020) 1277–1319.
* Do Prado and Chikezie [2021]

  J. C. Do Prado, U. Chikezie,
  A decision model for an electricity retailer with energy storage and virtual bidding under daily and hourly cvar assessment,
  IEEE access 9 (2021) 106181–106191.
* Herding et al. [2024]

  R. Herding, E. Ross, W. R. Jones, E. Endler, V. M. Charitopoulos, L. G. Papageorgiou,
  Risk-aware microgrid operation and participation in the day-ahead electricity market,
  Advances in Applied Energy 15 (2024) 100180.
* Moradi et al. [2022]

  A. Moradi, J. Salehi, S. N. Ravadanagh,
  Risk-based optimal decision-making strategy of a power-to-gas integrated energy-hub for exploitation arbitrage in day-ahead electricity and natural gas markets,
  Sustainable Energy, Grids and Networks 31 (2022) 100781.
* Haimes [1971]

  Y. Haimes,
  On a bicriterion formulation of the problems of integrated system identification and system optimization,
  IEEE transactions on systems, man, and cybernetics (1971) 296–297.
* Wang et al. [2022]

  Y. Wang, W. Dong, Q. Yang,
  Multi-stage optimal energy management of multi-energy microgrid in deregulated electricity markets,
  Applied Energy 310 (2022) 118528.
* Barbar et al. [2022]

  M. Barbar, D. S. Mallapragada, R. Stoner,
  Decision making under uncertainty for deploying battery storage as a non-wire alternative in distribution networks,
  Energy Strategy Reviews 41 (2022) 100862.
* Al-Lawati et al. [2021]

  R. A. Al-Lawati, J. L. Crespo-Vazquez, T. I. Faiz, X. Fang, M. Noor-E-Alam,
  Two-stage stochastic optimization frameworks to aid in decision-making under uncertainty for variable resource generators participating in a sequential energy market,
  Applied Energy 292 (2021) 116882.
* Kim et al. [2014]

  S. Kim, R. Pasupathy, S. G. Henderson,
  A guide to sample average approximation,
  Handbook of simulation optimization (2014) 207–243.
* Tsay et al. [2017]

  C. Tsay, R. C. Pattison, M. Baldea,
  A dynamic optimization approach to probabilistic process design under uncertainty,
  Industrial & Engineering Chemistry Research 56 (2017) 8606–8621.
* Patel et al. [2022]

  R. M. Patel, J. Dumouchelle, E. Khalil, M. Bodur,
  Neur2sp: Neural two-stage stochastic programming,
  Advances in Neural Information Processing Systems 35 (2022) 23992–24005.
* Ghilardi et al. [2025]

  L. M. Ghilardi, G. D. Patrón, A. Alcántara, C. Tsay,
  Integrated design and scheduling of hydrogen processes under uncertainty: A quantile neural network approach,
  Industrial & Engineering Chemistry Research (2025).
* Artzner et al. [1999]

  P. Artzner, F. Delbaen, J.-M. Eber, D. Heath,
  Coherent measures of risk,
  Mathematical finance 9 (1999) 203–228.
* Rahim et al. [2022]

  S. Rahim, Z. Wang, P. Ju,
  Overview and applications of robust optimization in the avant-garde energy grid infrastructure: A systematic review,
  Applied Energy 319 (2022) 119140.
* Rockafellar and Uryasev [2000]

  R. T. Rockafellar, S. Uryasev,
  Optimization of conditional value-at-risk,
  Journal of Risk 2 (2000) 21–42.
* Tsay and Qvist [2023]

  C. Tsay, S. Qvist,
  Integrating process and power grid models for optimal design and demand response operation of giga-scale green hydrogen,
  AIChE Journal 69 (2023) e18268.
* Alavijeh et al. [2024]

  N. M. Alavijeh, R. Khezri, M. Mazidi, D. Steen, L. A. Tuan,
  Optimal scheduling of battery storage systems in the swedish multi-fcr market incorporating battery degradation and technical requirements,
  arXiv preprint arXiv:2406.07301 (2024).
* Nair et al. [2021]

  U. R. Nair, M. Sandelic, A. Sangwongwanich, T. Dragičević, R. Costa-Castello, F. Blaabjerg,
  An analysis of multi objective energy scheduling in pv-bess system under prediction uncertainty,
  IEEE Transactions on Energy Conversion 36 (2021) 2276–2286.
* Ng et al. [2009]

  K. S. Ng, C.-S. Moo, Y.-P. Chen, Y.-C. Hsieh,
  Enhanced coulomb counting method for estimating state-of-charge and state-of-health of lithium-ion batteries,
  Applied energy 86 (2009) 1506–1511.
* Gao et al. [2022]

  X. Gao, B. Knueven, J. D. Siirola, D. C. Miller, A. W. Dowling,
  Multiscale simulation of integrated energy system and electricity market interactions,
  Applied energy 316 (2022) 119017.
* Dowling et al. [2017]

  A. W. Dowling, R. Kumar, V. M. Zavala,
  A multi-scale optimization framework for electricity market participation,
  Applied Energy 190 (2017) 147–164.
* Birge [1982]

  J. R. Birge,
  The value of the stochastic solution in stochastic linear programs with fixed recourse,
  Mathematical programming 24 (1982) 314–325.
* Bounitsis et al. [2022]

  G. L. Bounitsis, L. G. Papageorgiou, V. M. Charitopoulos,
  Data-driven scenario generation for two-stage stochastic programming,
  Chemical Engineering Research and Design 187 (2022) 206–224.
* United States Energy Information Administration [2025]

  United States Energy Information Administration, Wholesale electricity market data by rto, 2025. <https://www.eia.gov/electricity/wholesalemarkets/data.php?rto=isone> [Acessed: 2025-04-29].
* Lejarza et al. [2022]

  F. Lejarza, M. T. Kelley, M. Baldea,
  Feedback-based deterministic optimization is a robust approach for supply chain management under demand uncertainty,
  Industrial & Engineering Chemistry Research 61 (2022) 12153–12168.
* McAllister et al. [2022]

  R. D. McAllister, J. B. Rawlings, C. T. Maravelias,
  The inherent robustness of closed-loop scheduling,
  Computers & Chemical Engineering 159 (2022) 107678.
* Risbeck and Rawlings [2019]

  M. J. Risbeck, J. B. Rawlings,
  Economic model predictive control for time-varying cost and peak demand charge optimization,
  IEEE Transactions on Automatic Control 65 (2019) 2957–2968.
* Kumar et al. [2019]

  R. Kumar, J. Jalving, M. J. Wenzel, M. J. Ellis, M. N. ElBsat, K. H. Drees, V. M. Zavala,
  Benchmarking stochastic and deterministic mpc: A case study in stationary battery systems,
  AIChE Journal 65 (2019) e16551.
* Alcántara et al. [2025]

  A. Alcántara, C. Ruiz, C. Tsay,
  A quantile neural network framework for two-stage stochastic optimization,
  Expert Systems with Applications (2025) 127876.
* Matsumoto et al. [2022]

  T. Matsumoto, D. Bunn, Y. Yamada,
  Pricing electricity day-ahead cap futures with multifactor skew-t densities,
  Quantitative Finance 22 (2022) 835–860.
* Núñez et al. [2022]

  F. Núñez, D. Canca, Á. Arcos-Vargas,
  An assessment of european electricity arbitrage using storage systems,
  Energy 242 (2022) 122916.