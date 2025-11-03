---
authors:
- Hansjörg Albrecher
- Jinxia Zhu
doc_id: arxiv:2510.27384v1
family_id: arxiv:2510.27384
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On effects of present-bias on carbon emission patterns towards a net zero target
url_abs: http://arxiv.org/abs/2510.27384v1
url_html: https://arxiv.org/html/2510.27384v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hansjörg Albrecher111Department of Actuarial Science, Faculty of Business and Economics, and Expertise Center for Climate Extremes, University of Lausanne, and Swiss Finance Institute, Switzerland. Email: hansjoerg.albrecher@unil.ch
  
Jinxia Zhu222School of Risk and Actuarial Studies, University of New South Wales, Sydney, Australia.
Email: jinxia.zhu@unsw.edu.au. (Corresponding author).

###### Abstract

This paper explores the optimal policy for using an allocated carbon emission budget over time with the objective to maximize profit, by explicitly taking into account present-biased
preferences of decision-makers, accounting for time-inconsistent preferences. The setup can be adapted to be applicable for either a (present-biased) individual or also for a company which seeks a balance between production and emission schedules. In particular, we use and extend stochastic control techniques developed for optimal dividend strategies in insurance risk theory for the present purpose. The approach enables a quantitative analysis to assess the effects of present-bias, of sustainability awareness, and the efficiency of a potential carbon tax in a simplified model. In some numerical implementations, we illustrate in what way a higher degree of present-bias leads to excess emission patterns, while placing greater emphasis on sustainability reduces carbon emissions. Furthermore, we show that for low levels of carbon tax, its increase has a positive effect on curbing emissions, while beyond a certain threshold that marginal impact gets considerably weaker.

Keywords: Carbon emissions, present bias, stochastic quasi-hyperbolic discounting, sustainability, carbon tax, transition risk

## 1 Introduction

Following the Paris agreement within the United Nations Framework Convention on Climate Change (UNFCCC) aiming to reduce global greenhouse gas emissions (see e.g. Popovski, ([2018](https://arxiv.org/html/2510.27384v1#bib.bib37))), many countries have recently committed to set a time horizon until which a net zero target in terms of carbon emissions should be achieved. In order to reach such a target in a realistic way, companies and individuals will have to (and in some cases already do) receive carbon emission budgets over a given time horizon, and it is an interesting question how such budgets can and will influence the behaviour of individuals and companies which are a priori profit-maximizing entities. Concretely, how will a firm determine its production and – correspondingly – carbon emission schedule, if it is given an aggregate emission budget constraint? How will a (rational) individual decide on its carbon-intensive consumption pattern, if it is given an aggregate emission budget constraint? And how does a certain level of carbon tax enforced by a government steer or incentivize this process towards a net-zero target? There are many directions from which answers to such questions may be sought, and there is a strong need to increase the understanding of underlying mechanisms and incentives, see e.g. Saleh et al., ([2025](https://arxiv.org/html/2510.27384v1#bib.bib39)); Chekriy et al., ([2025](https://arxiv.org/html/2510.27384v1#bib.bib8)). In this paper we would like to contribute to this topic by relating it to optimal dividend/consumption problems in insurance and corporate finance, and adopt and extend techniques developed there for the present purpose. In particular, we want to address the above questions in a relatively simple model to better understand the effects of present-biasedness in this context. We provide a framework that allows to accommodate both the situation of a company (where monetary profitability is linked to the amount of carbon-intensive production) and the situation of an individual (where profitability is rather measured in terms of carbon-intensive consumption). In either case the decision-maker is given a finite ’budget’ of aggregate available carbon emissions and is subject to a certain degree of present-biasedness. By establishing and exploiting a link to stochastic control techniques for optimal dividend problems in insurance risk theory, we develop a framework that leads to quantitative results in terms of optimal behavior given the objective function and (carbon budget) constraint. Within the chosen simple model assumptions, this also allows to study the effect of the governmental measure of a carbon tax towards an aggregate carbon emission target. In particular, we intend to quantify the sensitivity of the results with respect to the degree of present-bias of the decision-maker, and compare it to the values in the absence of present-bias.
In terms of the maximization criterion, we consider the maximization of profit (or consumption benefit in the case of an individual), but also allow for a term in the objective function that reflects a certain degree of social responsibility and sustainability awareness (see e.g. Korn, ([2025](https://arxiv.org/html/2510.27384v1#bib.bib23)); Korn and Nurkanovic, ([2025](https://arxiv.org/html/2510.27384v1#bib.bib24)) for other ways to incorporate sustainability considerations in profitability criteria).

In any inter-temporal choice problem, discounting is one of the key factors that influence the optimal strategy. Traditionally, exponential discounting is used, where the time preference for a payment (or consumption token) occurring at time tt can be fully captured by a single discount rate at that time. In such a case, the optimization problem is time-consistent, and the optimal decision regarding actions at time tt will only depend on available resources at that moment, regardless of the time s<ts<t at which this decision was taken. That is, an ’optimal’ decision made at time s1s\_{1} for an action at a future time t>s1t>s\_{1} will be preferred by the decision maker at any later time s2>s1s\_{2}>s\_{1} as well.
Most of the literature in optimal control relies on exponential discounting to calculate the present value of future payments (or monetary translations of consumption opportunities). This is usually done by assuming time-consistent preferences and employing a constant discount rate (see e.g. Schmidli, ([2007](https://arxiv.org/html/2510.27384v1#bib.bib40)); Albrecher and Thonhauser, ([2009](https://arxiv.org/html/2510.27384v1#bib.bib2)); Azcue and Muler, ([2014](https://arxiv.org/html/2510.27384v1#bib.bib3)) for surveys in the field of dividend strategies). In rare cases, a stochastic discount rate (Eisenberg, ([2015](https://arxiv.org/html/2510.27384v1#bib.bib12)); Reppen et al., ([2020](https://arxiv.org/html/2510.27384v1#bib.bib38))) is employed.
However, empirical studies often observe patterns of preference reversals. Laibson, ([1998](https://arxiv.org/html/2510.27384v1#bib.bib26)) describes “a conflict between today’s preferences and the preferences which will be held in the future”, and the exponential discount functions cannot capture such a tendency. In many practical situations, decision-makers are present-biased, preferring smaller but earlier rewards to larger but later ones, in particular when such earlier rewards are near. Only when the time until such rewards is far distant, such preferences may be flipped, cf. for instance (Palacios-Huerta and Pèrez-Kakabadse, ([2011](https://arxiv.org/html/2510.27384v1#bib.bib34))). Laibson, ([1998](https://arxiv.org/html/2510.27384v1#bib.bib26)) noted already that hyperbolic discounting may be used to model such preferences, and it has been shown to outperform exponential discounting in certain empirical studies.
Laibson, ([1998](https://arxiv.org/html/2510.27384v1#bib.bib26)) used a quasi-hyperbolic discount function for discrete-time models, where an additional constant discount factor is introduced in the utility of all cash-flows in future periods regardless of timing, see also Phelps and Pollak, ([1968](https://arxiv.org/html/2510.27384v1#bib.bib36)).
Such a quasi-hyperbolic discount function mimics the quantitative properties of a hyperbolic discount function while maintaining analytical tractability. Harris and Laibson, ([2013](https://arxiv.org/html/2510.27384v1#bib.bib19)) then proposed a stochastic quasi-hyperbolic discount function as a continuous-time model of non-exponential discounting, where an additional discount factor is added for future periods. It is this latter model that we will adopt for our present study.

In this paper, we propose a simple continuous-time dynamic model framework based on a general linear diffusion to investigate the optimal production and carbon emission strategy for a firm with an allocated emission budget, taking present-bias into account. As mentioned above, the setup can also be interpreted for the situation of an individual taking decisions on carbon-intensive consumption, but we will formulate the paper for the context of a firm, and only add some interpretations for the situation of an individual in the concluding section.

Concretely, the remaining emission budget will be modeled as a stochastic process over time with a given initial allocation, a drift term representing a trend (e.g., projected unavoidable minimal emissions in the production process),
and a volatility term reflecting fluctuations (which may e.g. stem from remaining uncertainties in establishing the present carbon balance). Effective carbon emissions act as a deduction term from this process in the dynamics, reducing the available remaining budget as production continues. In the paper we consider a general form for the drift and volatility terms, allowing for various scenarios. The company develops a production/emission schedule aimed at maximizing the present value of total expected future profit up to a fixed terminal time, plus a term that rewards for not yet having used up the budget at any time until depletion, which can be interpreted as a contribution to sustainability considerations of society. In order to account for present-biased preferences, we use stochastic quasi-hyperbolic discounting rather than standard exponential discounting for determining the present value of future profits and the reward term. The weighting of the reward term in the objective function then formalizes the balancing between profit maximization and sustainability considerations.

Under time-inconsistent preferences (such as the stochastic quasi-hyperbolic discounting considered in this paper), there are typically two alternative assumptions about decision-makers: naive agents and sophisticated agents (Grenadier and Wang, ([2007](https://arxiv.org/html/2510.27384v1#bib.bib18))). The naive agent assumes that future selves act according to the preferences of the current self, which is possible if there is a commitment mechanism that ensures that future selves commit to the strategy chosen by the current self. The sophisticated agent, in contrast, “correctly foresees that their future selves act according to their own preferences” (Grenadier and Wang, ([2007](https://arxiv.org/html/2510.27384v1#bib.bib18))), see also Frederick et al., ([2002](https://arxiv.org/html/2510.27384v1#bib.bib13)). In the sophisticated agent case, there is no optimal solution, as a solution that is optimal in the eyes of the decision-maker at time tt
will not remain optimal later.
Conflicts arise unless there are pre-commitment mechanisms ensuring that an optimal decision made earlier will be upheld by future decision-makers, even if it is no longer optimal for them to do so (Strotz, ([1956](https://arxiv.org/html/2510.27384v1#bib.bib44))). In this paper, we consider sophisticated decision makers and assume that there are no commitment devices. In other words, we consider scenarios where the early selves do not have a technology to commit the actions of later selves. This is a common and realistic scenario, see e.g. Iverson and Karp, ([2021](https://arxiv.org/html/2510.27384v1#bib.bib22)).
Correspondingly, we formulate the control problem as an intra-personal subgame and seek equilibrium solutions (Harris and Laibson, ([2013](https://arxiv.org/html/2510.27384v1#bib.bib19)) and Maskin and Tirole, ([2001](https://arxiv.org/html/2510.27384v1#bib.bib32))).
We establish the existence of equilibrium strategies and equilibrium solutions theoretically and provide a procedure for determining an equilibrium solution and the associated equilibrium strategy. We further investigate the impact of the degree of present-bias on the agent’s behavior and the respective carbon emission consequences. We find the intuitive result that a higher degree of present-bias leads to higher emissions, and earlier depletion of the carbon allowance. Additionally, we analyze the role of the sustainability term in shaping the company’s carbon emission behavior and explore how a carbon tax might affect the company’s emission decisions.
Naturally, higher sustainability awareness curbs production and reduces carbon emissions, just as imposing a carbon tax does. The results of this paper contribute to understand how the two effects are related, and which level of carbon tax replaces which level of sustainability awareness to lead to the same result. In addition, it will turn out that once the carbon tax reaches a certain threshold, its effectiveness begins to decline.

We consider the carbon tax as being determined exogeneously by policymakers (social planners), and then the individual firms’ behavior is studied in response to that. The carbon tax can then be interpreted as the social cost of carbon. Various suggestions exist in the literature for determining the appropriate or optimal social cost of carbon, with a common approach based on well-established Integrated Assessment Models (IAMs), which integrate climate and economic systems. For example, one of the earliest and most frequently used IAMs for climate change is the DICE/RICE family of models (see Nordhaus, ([2018](https://arxiv.org/html/2510.27384v1#bib.bib33)) for details on its development). Most of these IAM studies assume exponential discounting, typically at a constant discount rate. Fries and Quante, ([2024](https://arxiv.org/html/2510.27384v1#bib.bib14)) extended the DICE model to incorporate a stochastic discount rate, which technically remains a form of exponential discounting. See also Colaneri et al., ([2024](https://arxiv.org/html/2510.27384v1#bib.bib11)) for another type of stochastic control problem where a company decides on investments in carbon abatement technologies in view of carbon tax costs, and Bourgey et al., ([2024](https://arxiv.org/html/2510.27384v1#bib.bib7)) for optimizing the emission level alongside constraints on emission mitigation scenarios, additionally taking into account credit risk. Our approach based on stochastic quasi-hyperbolic discounting can therefore also be interpreted as an extension of certain aspects of that literature to the explicit consideration of present-biasedness. Since stochastic quasi-hyperbolic discounting approximates hyperbolic discounting, and the latter is often empirically found to better represent individuals’ true time preferences, cf. Frederick et al., ([2002](https://arxiv.org/html/2510.27384v1#bib.bib13)), a contribution of this paper is also to offer a quantitative approach to systematically understand the effects of that deviation from exponential discounting for questions of that part of social planning.
Note that the choice of appropriate discount rates related to climate policy is a subject of on-going political debate, all the way since the Stern Review (Stern, ([2006](https://arxiv.org/html/2510.27384v1#bib.bib42))). We will not delve into respective discussions here, and the discount rate values applied in the numerical section are only for illustrative purposes. Our aim is to contribute – in a simplified model with explicit formulas for the optimal strategies – to the understanding of how present-biasedness affects the decision-making of profit-maximizing rational agents (who are not social planners), which may also provide insights for social planners to develop effective policies towards specific targets.

On the technical side, we deal with a regular control equilibrum problem with stochastic quasi-hyperbolic discounting under a general linear diffusion framework. For a similar problem with capital injections, but without a sustainability component and for a different type of discounting (pseudo-exponential discounting) as well as constant drift and volatility coefficients only, see Hu and Zhou, ([2025](https://arxiv.org/html/2510.27384v1#bib.bib20)). For singular control problems under other non-exponential discounting functions, see also Zhao et al., ([2014](https://arxiv.org/html/2510.27384v1#bib.bib46)) and Li et al., ([2016](https://arxiv.org/html/2510.27384v1#bib.bib28)), and for another way to formalize time-inconsistency see Strini and Thonhauser, ([2023](https://arxiv.org/html/2510.27384v1#bib.bib43)). Finally, equilibrium strategies for singular (rather than regular as in this paper) control under stochastic quasi-hyperbolic discounting have been identified in Chen et al., ([2014](https://arxiv.org/html/2510.27384v1#bib.bib9)) and Chen et al., ([2016](https://arxiv.org/html/2510.27384v1#bib.bib10)) for a compound Poisson model with negative jumps of exponential type, in Li et al., ([2015](https://arxiv.org/html/2510.27384v1#bib.bib29)) for a Brownian risk model, and in Zhu et al., ([2020](https://arxiv.org/html/2510.27384v1#bib.bib48)) for a linear growth restricted diffusion process.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.27384v1#S2 "2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target") defines the model setup, introduces exponential and quasi-hyperbolic discounting and defines the type of optimal strategies we are investigating. Section [3](https://arxiv.org/html/2510.27384v1#S3 "3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") derives these optimal strategies for exponential discounting, and spells out the explicit formulas for the Brownian model in more detail. Section [4](https://arxiv.org/html/2510.27384v1#S4 "4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") then establishes the equlibrium solution for the case of stochastic quasi-hyperbolic discounting, which is the core for the study of the present-bias effects considered in this paper. Section [5](https://arxiv.org/html/2510.27384v1#S5 "5 Probability of Early Depletion ‣ On effects of present-bias on carbon emission patterns towards a net zero target") deals with the determination of the probability of early depletion of the carbon budget when following the optimal strategy. Section [6](https://arxiv.org/html/2510.27384v1#S6 "6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") is then dedicated to numerical illustrations of the impact of present-bias, the level of social responsability and the amount of carbon tax on the emission schedule for a Brownian motion model with constant diffusion coefficients. Detailed interpretations of the interplay of various factors are given. In Section [7](https://arxiv.org/html/2510.27384v1#S7 "7 Numerical Illustrations for More General Models ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), it is then shown that the analysis can also be extended to more general diffusion models, including an Ornstein-Uhlenbeck type process for the time-development of the available carbon budget. Finally, Section [8](https://arxiv.org/html/2510.27384v1#S8 "8 Conclusion ‣ On effects of present-bias on carbon emission patterns towards a net zero target") concludes.
All mathematical derivations and proofs are moved to the Appendix.

## 2 Problem Formulation

Let (Ω,ℱ,{ℱt;t≥0},ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t};t\geq 0\},{\mathbb{P}}) be a filtered complete probability space with a right-continuous filtration {ℱt;t≥0}\{\mathcal{F}\_{t};t\geq 0\}. Consider a firm whose production depends on its energy consumption, and let PtP\_{t} represent the (monetary) instantaneous production profit at time tt. We assume that Pt=γ​(lt+l¯)P\_{t}=\gamma(l\_{t}+\underline{l}) for some γ>0\gamma>0, where lt+l¯l\_{t}+\underline{l} is the instantaneous emission rate at time tt, with l¯\underline{l} representing the baseline emission rate required to maintain minimal production activity, and ltl\_{t} representing the excess emission rate for additional production above that minimum level. Since the baseline emission rate l¯\underline{l} can not be avoided in any case, the control to be considered in this paper is the excess carbon emission L={Lt=∫0tls​ds;t≥0}L=\{L\_{t}=\int\_{0}^{t}l\_{s}\,\,\mathrm{d}s;t\geq 0\} up to time tt.
Let ci​n​d​Ptc\_{ind}\,P\_{t} represent the physical cost for producing PtP\_{t} and ct​a​x​(lt+l¯)c\_{tax}(l\_{t}+\underline{l}) the carbon tax paid for the resulting emission. Then the total cost, which equals the sum of production cost and carbon tax, is (ci​n​d​γ+ct​a​x)​(lt+l¯)(c\_{ind}\,\gamma+c\_{tax})(l\_{t}+\underline{l}). Assume now that the firm is allocated with a total (CO2) emission allowance (endowment)333The total emission allowance x0x\_{0} could for instance be the total emission budget allocated to the company according to a net-zero target around 2050 set by the Intergovernmental Panel on Climate Change. x0x\_{0} and let XtLX\_{t}^{L} represent the remaining emission allowance at time tt according to the general diffusion dynamics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | XtL\displaystyle X\_{t}^{L} | :=x0+∫0tμ¯​(Xs)​ds+∫0tσ​(Xs)​dWs−∫0t(l¯+ls)​ds,t≥0.\displaystyle:=x\_{0}+\int\_{0}^{t}\overline{\mu}(X\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(X\_{s})\,\mathrm{d}W\_{s}-\int\_{0}^{t}(\underline{l}+l\_{s})\,\mathrm{d}s,\ \ t\geq 0. |  | (2.1) |

The drift term μ¯​(⋅)\overline{\mu}(\cdot) could be zero, or negative in a deteriorating situation, or also positive, e.g. due to technological advances and increasing carbon capture capabilities over time. Here, WtW\_{t} is a standard Brownian motion. Let ℱW\mathcal{F}^{W} represent the filtration generated by {Wt;t≥0}\{W\_{t};t\geq 0\}.

The functions μ¯​(⋅)\overline{\mu}(\cdot) and the volatility σ​(⋅)\sigma(\cdot) are assumed to be Lipschitz continuous, satisfying a linear condition, that is, there exists a constant C>0C>0 such that μ¯2​(x)+σ2​(x)≤C​(1+x2)\overline{\mu}^{2}(x)+\sigma^{2}(x)\leq C(1+x^{2}) for all xx. As proven in Gikhman and Skorokhod, ([1972](https://arxiv.org/html/2510.27384v1#bib.bib16)), these conditions guarantee the existence and uniqueness of a strong solution to ([2.1](https://arxiv.org/html/2510.27384v1#S2.E1 "In 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) for each x0x\_{0} and each ℱW\mathcal{F}^{W}-adapted, nondecreasing, left-continuous process LL, see also Shreve et al., ([1984](https://arxiv.org/html/2510.27384v1#bib.bib41)).
We further assume that σ​(⋅)\sigma(\cdot) is non-vanishing and 0≤ls≤l¯0\leq l\_{s}\leq\bar{l}, where l¯\bar{l} is a positive constant. Additionally, we impose the restriction μ¯′​(x)≤δ\overline{\mu}^{\prime}(x)\leq\delta for x≥0x\geq 0, where δ>0\delta>0 is the exponential discount rate discussed further below. This latter assumption will serve mathematical tractability, but it also has practical relevance, as one would not expect the growth rate of available carbon allowance to increase significantly over time.

With
μ​(x)=μ¯​(x)−l¯\mu(x)=\overline{\mu}(x)-\underline{l}
we can simplify ([2.1](https://arxiv.org/html/2510.27384v1#S2.E1 "In 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | XtL\displaystyle X\_{t}^{L} | :=x0+∫0tμ​(Xs)​ds+∫0tσ​(Xs)​dWs−Lt,t≥0.\displaystyle:=x\_{0}+\int\_{0}^{t}{\mu}(X\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(X\_{s})\,\mathrm{d}W\_{s}-L\_{t},\ \ t\geq 0. |  | (2.2) |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | τL=inf{t≥0:XtL≤0}\displaystyle\tau^{L}=\inf\{t\geq 0:X\_{t}^{L}\leq 0\} |  | (2.3) |

denote the emission allowance depletion time when applying emission schedule LL.
In this paper we are interested in the optimal emission schedule for the company that maximizes the expected present value of profit. At time tt, the objective function to be maximized therefore is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒫E​(x,t;L)=\displaystyle\mathcal{P}^{E}(x,t;L)= | 𝔼​[∫tτLD​(t,s)​[(γ−β)​(ls+l¯)+Λ¯]​ds|Xt=x],\displaystyle\,{\mathbb{E}}\left[\left.\int\_{t}^{\tau^{L}}D(t,s)\big[(\gamma-\beta)(l\_{s}+\underline{l})+\overline{\Lambda}\big]\,\mathrm{d}s\right|X\_{t}=x\right], |  | (2.4) |

where D​(t,s)D(t,s) is the discounting function for calculating the present value at time tt of cashflows at future times s≥ts\geq t and β=ci​n​d​γ+ct​a​x\beta=c\_{ind}\,\gamma+c\_{tax}.
While the focus is on maximizing profit, we also introduce a constant rate Λ¯>0\overline{\Lambda}>0 that rewards for the carbon allowance to not be depleted early (i.e., having the depletion time τL\tau^{L} being larger). It can be interpreted as an intangible utility term (e.g., sustainability value). This will allow to consider the tradeoff between profitability, costs and ‘social responsibility’ represented through Λ¯\overline{\Lambda} (cf. Thonhauser and Albrecher, ([2007](https://arxiv.org/html/2510.27384v1#bib.bib45)) for the introduction of such a term for dividend problems). With Λ:=Λ¯+(γ−β)​l¯\Lambda:=\overline{\Lambda}+(\gamma-\beta)\underline{l},
we can simplify ([2.4](https://arxiv.org/html/2510.27384v1#S2.E4 "In 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒫E​(x,t;L)=\displaystyle\mathcal{P}^{E}(x,t;L)= | 𝔼​[∫tτLD​(t,s)​[(γ−β)​ls+Λ]​ds|Xt=x].\displaystyle\,{\mathbb{E}}\left[\left.\int\_{t}^{\tau^{L}}D(t,s)\big[(\gamma-\beta)l\_{s}+\Lambda\big]\,\mathrm{d}s\right|X\_{t}=x\right]. |  | (2.5) |

### 2.1 Exponential discounting

As a benchmark model, and also as an intermediate result needed in the derivations, we will first consider exponential discounting, that is D​(t,s)=e−δ​(s−t)D(t,s)=e^{-\delta(s-t)} for some constant rate δ>0\delta>0. In this case the objective function in ([2.5](https://arxiv.org/html/2510.27384v1#S2.E5 "In 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) at time 0 reads as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒫E​(x;L)=\displaystyle\mathcal{P}^{E}(x;L)= | 𝔼​[∫0τLe−δ​s​((γ−β)​ls+Λ)​ds|X0=x].\displaystyle{\mathbb{E}}\bigg[\left.\int\_{0}^{\tau^{L}}e^{-\delta s}((\gamma-\beta)l\_{s}+\Lambda)\,\mathrm{d}s\right|X\_{0}=x\bigg]. |  | (2.6) |

Correspondingly, the optimization goal is to look for a schedule of excess emissions LL that maximizes 𝒫E​(x;L)\mathcal{P}^{E}(x;L), leading to the value function

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VE​(x)=supL∈Π𝒫E​(x;L)=\displaystyle V^{E}(x)=\sup\_{L\in\Pi}\mathcal{P}^{E}(x;L)= | supL∈Π𝔼​[∫0τLe−δ​s​((γ−β)​ls+Λ)​ds|X0=x],\displaystyle\sup\_{L\in\Pi}{\mathbb{E}}\bigg[\left.\int\_{0}^{\tau^{L}}e^{-\delta s}((\gamma-\beta)l\_{s}+\Lambda)\,\mathrm{d}s\right|X\_{0}=x\bigg], |  | (2.7) |

where Π\Pi denotes the set of admissible strategies, which will be specified later.

### 2.2 Stochastic quasi-hyperbolic discounting

If the decision maker is present-biased, we use the following stochastic quasi-hyperbolic discount function introduced in Harris and Laibson, ([2013](https://arxiv.org/html/2510.27384v1#bib.bib19)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(t,s)={e−δ​(s−t),t<s<t+η,α​e−δ​(s−t),s≥t+η,\displaystyle D(t,s)=\begin{cases}e^{-\delta(s-t)},&t<s<t+\eta,\\ \alpha\,e^{-\delta(s-t)},&s\geq t+\eta,\end{cases} |  | (2.8) |

where η\eta represents the (random) duration of the current regime and 0≤α≤10\leq\alpha\leq 1 is a constant. That is, cashflows during the present period are valued using exponential discounting at force δ\delta, while cashflows emerging in the future period are discounted by a smaller value.

One can interpret this stochastic discounting framework in the way that there is a sequence of decision makers, to each of whom time is divided into two intervals, the present and the future, and each decision maker is present-biased. The present will last for a random length of time which we model as an exponential random variable with parameter λ>0\lambda>0, independent of the current carbon allowance. All cash-flows in the present period are discounted exponentially with force δ\delta and the cash-flows in the future period are then discounted more strongly with additional factor α\alpha. Assume that the decision maker at time 0 is called “self 0”. The present period for “self 0” starts at time 0 and ends at time η0\eta\_{0}. “Self 0” exercises control for her present period and is present-biased. At the end of “self 0”’s present period, a new self, “self 11”, starts to take over decision making. “Self 11” is also present-biased and she can only exercise control during her own present period, which lasts from time s1:=η0s\_{1}:=\eta\_{0} to s1+η1s\_{1}+\eta\_{1}. Acoordingly, the present period of “self nn” (n=1,2,3,⋯n=1,2,3,\cdots), also present-biased, is from time sns\_{n} to sn+ηns\_{n}+\eta\_{n}. Each self takes decisions according to D​(s,t)D(s,t) given in ([2.8](https://arxiv.org/html/2510.27384v1#S2.E8 "In 2.2 Stochastic quasi-hyperbolic discounting ‣ 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
More specifically, if we use Dn​(t)D\_{n}(t) to represent the present value at time sns\_{n} of one dollar payable at time tt from “self nn”’s perspective, then Dn​(t)=e−δ​(t−sn)D\_{n}(t)=e^{-\delta(t-s\_{n})} for sn≤t<sn+ηns\_{n}\leq t<s\_{n}+\eta\_{n} and Dn​(t)=α​e−δ​(t−sn)D\_{n}(t)=\alpha e^{-\delta(t-s\_{n})} for t≥sn+ηnt\geq s\_{n}+\eta\_{n}.

Although each self controls the emission schedule only during her present period, she does so keeping in mind the total production profit, i.e. the profit of the present period as well as the one in future periods. Different selves have conflicting preferences as they value the production profit and survival utility during a particular period differently.
We assume that there are no commitment mechanisms (in the sense that later selves are not committed to what earlier selves considered optimal), and that the decision-maker is sophisticated and rational. In addition, she can correctly foresee her future actions. For this intra-personal game we will consider Markov policies only, and seek a Markov-perfect equilibrium (MPE).
That is, we restrict the admissible strategies to stationary Markov-perfect equilibrium (MPE) policies. An emission schedule L={lt;t≥0}L=\{l\_{t};t\geq 0\} is said to be admissible if it is a Markov policy with 0≤ls≤l¯0\leq l\_{s}\leq\bar{l}. We use Π\Pi to denote the set of admissible strategies.

Let π(n,→)​(L,L~)\pi^{(n,\rightarrow)(L,\tilde{L})} represent the strategy where “self nn” adopts LL and the future selves adopt L~\tilde{L}. Let πt(n,→)​(L,L~)\pi^{(n,\rightarrow)(L,\tilde{L})}\_{t} represent the cumulative amount of emissions from time sns\_{n} to tt under π(n,→)​(L,L~)\pi^{(n,\rightarrow)(L,\tilde{L})}. Then, πsn−(n,→)​(L,L~)=0\pi^{(n,\rightarrow)(L,\tilde{L})}\_{s\_{n}-}=0, d​πt(n,→)​(L,L~)=lt​d​t\,\mathrm{d}\pi^{(n,\rightarrow)(L,\tilde{L})}\_{t}=l\_{t}\,\mathrm{d}t for t∈[sn,sn+1)t\in[s\_{n},s\_{n+1}) and d​πt(n,→)​(L,L~)=l~t​d​t\,\mathrm{d}\pi^{(n,\rightarrow)(L,\tilde{L})}\_{t}=\tilde{l}\_{t}\,\mathrm{d}t for t≥sn+1t\geq s\_{n+1}.
The reward to “self nn” is the expected present value at time sns\_{n} of the entire future net production profit up to the time of depletion plus the reward from the Λ\Lambda-term. Given Xsn−L=xX\_{s\_{n}-}^{L}=x, for any x≥0x\geq 0, the objective function for “self nn” with pair (L,L~)(L,\tilde{L}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝒫n​(x;L,L~)\displaystyle\mathcal{P}\_{n}(x;L,\tilde{L}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\; | 𝔼sn,x[∫snτsnπ(n,→)​(L,L~)∧(sn+ηn)e−δ​(t−sn)(γ−β)ltdt\displaystyle{\mathbb{E}}\_{s\_{n},x}\bigg[\int^{\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}}\wedge{(s\_{n}+\eta\_{n})}}\_{s\_{n}}e^{-\delta(t-s\_{n})}(\gamma-\beta)l\_{t}\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +I​{sn+ηn≤τsnπ(n,→)​(L,L~)}​∫sn+ηnτsnπ(n,→)​(L,L~)α​e−δ​(t−sn)​(γ−β)​l~t​dt\displaystyle+I\{s\_{n}+\eta\_{n}\leq\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}}\}\int\_{s\_{n}+\eta\_{n}}^{\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}}}\alpha e^{-\delta(t-s\_{n})}(\gamma-\beta)\tilde{l}\_{t}\,\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫snτsnπ(n,→)​(L,L~)∧(sn+ηn)e−δ​(t−sn)Λdt+I{sn+ηn≤τsnπ(n,→)​(L,L~)}∫sn+ηnτsnπ(n,→)​(L,L~)αe−δ​(t−sn)Λdt],\displaystyle+\int^{\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}}\wedge{(s\_{n}+\eta\_{n})}}\_{s\_{n}}e^{-\delta(t-s\_{n})}\Lambda\,\mathrm{d}t+I\{s\_{n}+\eta\_{n}\leq\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}}\}\int\_{s\_{n}+\eta\_{n}}^{\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}}}\alpha e^{-\delta(t-s\_{n})}\Lambda\,\mathrm{d}t\bigg], |  | (2.9) |

where I​{⋅}I\{\cdot\} is the indicator function and τsnπ(n,→)​(L,L~)\tau^{\pi^{(n,\rightarrow)(L,\tilde{L})}}\_{s\_{n}} is the (potential) depletion time during the active period of “self nn” when following the strategy (L,L~)(L,\tilde{L}).
The first term inside the expectation above represents the discounted net amount of production profit in the present period, where all the cashflows are discounted with force δ\delta, and the second term is the total discounted net amount of production profits in all the future periods up to the time of depletion, where all the cashflows are discounted by the force δ\delta and then further discounted by the factor α\alpha. The last two terms represent the benefit of surviving up to depletion time represented through the reward rate Λ\Lambda.

Let 𝒫​(x;L,L~):=𝒫0​(x;L,L~)\mathcal{P}(x;L,\tilde{L}):=\mathcal{P}\_{0}(x;L,\tilde{L}) and πL,L~:=π(0,→)​(L,L~)\pi^{L,\tilde{L}}:=\pi^{(0,\rightarrow)(L,\tilde{L})}. The objective of “self nn” is to find a Markov strategy L∗L^{\*} (a MPE policy that maximizes the above expected reward with respect to LL in the sense that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫n​(x;L∗,L∗)=supL∈Π𝒫n​(x;L,L∗)\displaystyle\mathcal{P}\_{n}(x;L^{\*},L^{\*})=\sup\_{L\in\Pi}\mathcal{P}\_{n}(x;L,L^{\*}) |  | (2.10) |

subject to the production constraint). Note the problem is stationary, although the preferences of the decision makers are time-inconsistent. Then we only need to solve the game problem based on the reward 𝒫=𝒫0\mathcal{P}=\mathcal{P}\_{0}. That is, we are seeking an admissible strategy L∗L^{\*} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫​(x;L∗,L∗)=supL∈Π𝒫​(x;L,L∗).\displaystyle\mathcal{P}(x;L^{\*},L^{\*})=\sup\_{L\in\Pi}\mathcal{P}(x;L,L^{\*}). |  | (2.11) |

Indeed, if a MPE strategy exists that satisfies ([2.10](https://arxiv.org/html/2510.27384v1#S2.E10 "In 2.2 Stochastic quasi-hyperbolic discounting ‣ 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) for all nn, then no self has an incentive to deviate from it, given that all future selves adopt it as well.

## 3 Optimal Solutions under Exponential Discounting

Under exponential discounting, the mathematical formulation of the optimization problem is similar to (and a slight extension of) the problem in Zhu, ([2015](https://arxiv.org/html/2510.27384v1#bib.bib47)), where there was no Λ\Lambda term. In the following we accordingly adapt the technique developed in that reference. One easily derives the Hamilton-Jacobi-Bellman (HJB) equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | supl∈[0,l¯](σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)+l​(γ−β−g′​(x))+Λ)=0,g​(0)=0.\displaystyle\sup\_{l\in[0,\bar{l}]}\left(\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)+{l}(\gamma-\beta-g^{\prime}(x))+\Lambda\right)=0,\quad g(0)=0. |  | (3.1) |

If the value function VEV^{E} is sufficiently smooth, then a standard verification theorem shows that VEV^{E} is a classical solution to the HJB equation ([3.1](https://arxiv.org/html/2510.27384v1#S3.E1 "In 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). We establish the existence of a classical solution by constructing one explicitly, using a class of auxiliary functions defined below. To that end, let us consider a threshold strategy for any given threshold b≥0b\geq 0 as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lb:={l¯⋅I​{Xt≥b};t≥0}\displaystyle L^{b}:=\{\bar{l}\cdot I\{X\_{t}\geq b\};t\geq 0\} |  | (3.2) |

and denote its corresponding value function under exponential discounting as

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE​(x):=𝒫E​(x;Lb).\displaystyle V\_{b}^{E}(x):=\mathcal{P}^{E}(x;L^{b}). |  | (3.3) |

The function VbE​(x)V\_{b}^{E}(x) will be instrumental in searching for a solution, both under exponential and stochastic quasi-hyperbolic discounting considered later.

###### Lemma 3.1

The function VbE​(x)V\_{b}^{E}(x) solves the initial value problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)+Λ=0​ for 0<x<b,\displaystyle\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)+\Lambda=0\mbox{ for $0<x<b$}, |  | (3.4) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)+l¯​(γ−β)+Λ=0​ for x≥b,\displaystyle\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)+\bar{l}(\gamma-\beta)+\Lambda=0\mbox{ for $x\geq b$}, |  | (3.5) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(0)=0,\displaystyle g(0)=0, |  | (3.6) |

and has the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE​(x)={C1​(b)​(v1​(x)−v2​(x))+B1​(x),0≤x<b,C3​(b)​v3​(x)+u​(x),x≥b,\displaystyle V\_{b}^{E}(x)=\left\{\begin{array}[]{ll}C\_{1}(b)(v\_{1}(x)-v\_{2}(x))+B\_{1}(x),&0\leq x<b,\\ C\_{3}(b)v\_{3}(x)+u(x),&x\geq b,\end{array}\right. |  | (3.9) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | C1​(b)=(B1​(b)−u​(b))​v3′​(b)−(B1′​(b)−u′​(b))​v3​(b)(v1′​(b)−v2′​(b))​v3​(b)−(v1​(b)−v2​(b))​v3′​(b),\displaystyle C\_{1}\,(b)=\frac{(B\_{1}(b)-u(b))v\_{3}^{\prime}(b)-(B\_{1}^{\prime}(b)-u^{\prime}(b))v\_{3}(b)}{(v\_{1}^{\prime}(b)-v\_{2}^{\prime}(b))v\_{3}(b)-(v\_{1}(b)-v\_{2}(b))v\_{3}^{\prime}(b)}, |  | (3.10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C3​(b)=(u′​(b)−B1′​(b))​(v1​(b)−v2​(b))−(u​(b)−B1​(b))​(v1′​(b)−v2′​(b))(v1′​(b)−v2′​(b))​v3​(b)−(v1​(b)−v2​(b))​v3′​(b).\displaystyle C\_{3}(b)=\frac{(u^{\prime}(b)-B\_{1}^{\prime}(b))(v\_{1}(b)-v\_{2}(b))-(u(b)-B\_{1}(b))(v\_{1}^{\prime}(b)-v\_{2}^{\prime}(b))}{(v\_{1}^{\prime}(b)-v\_{2}^{\prime}(b))v\_{3}(b)-(v\_{1}(b)-v\_{2}(b))v\_{3}^{\prime}(b)}. |  | (3.11) |

The functions v1​(⋅)v\_{1}(\cdot) and v2​(⋅)v\_{2}(\cdot) are the solutions to
σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)=0,\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)=0,
with the respective sets of initial conditions:
v1​(0)=1,v1′​(0)=1,and ​v2​(0)=1,v2′​(0)=−1.v\_{1}(0)=1,v\_{1}^{\prime}(0)=1,\mbox{and\ }v\_{2}(0)=1,v\_{2}^{\prime}(0)=-1.
The function u​(x)u(x) is the unique bounded solution to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)+Λ+(γ−β)​l¯=0,\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)+\Lambda+(\gamma-\beta)\bar{l}=0,
on [0,∞)[0,\infty) with initial condition g​(0)=0g(0)=0.
The function v3​(⋅)v\_{3}(\cdot) is the unique bounded solution to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)=0
on (0,∞)(0,\infty) with initial condition g​(0)=1g(0)=1.

Additionally, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | B1​(x)=2​Λ​∫0xv1​(x)​v2​(y)−v2​(x)​v1​(y)v1​(y)​v2′​(y)−v2​(y)​v1′​(y)​dy,\displaystyle B\_{1}(x)=2\Lambda\int\_{0}^{x}\frac{v\_{1}(x)v\_{2}(y)-v\_{2}(x)v\_{1}(y)}{v\_{1}(y)v\_{2}^{\prime}(y)-v\_{2}(y)v\_{1}^{\prime}(y)}\,\mathrm{d}y, |  | (3.12) |

which is the solution to σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)+Λ=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)+\Lambda=0 under B1​(0)=0B\_{1}(0)=0 and B1′​(0)=0B\_{1}^{\prime}(0)=0.

We can show that the value function VE​(x)V^{E}(x) has the following property.

###### Lemma 3.2

The function VE​(x)V^{E}(x) is nonnegative, increasing and has an upper bound (γ−β)​l¯+Λδ\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}.

Moreover, we can derive an expression for the value function under exponential discounting as follows.

###### Theorem 3.3

The value function under exponential discounting is given by:

|  |  |  |
| --- | --- | --- |
|  | VE​(x)={C1​(bE∗)​(v1​(x)−v2​(x))+B1​(x),0≤x<bE∗,C3​(bE∗)​v3​(x)+u​(x),x≥bE∗,\displaystyle V^{E}(x)=\left\{\begin{array}[]{ll}C\_{1}\,(b^{\*}\_{E})(v\_{1}(x)-v\_{2}(x))+B\_{1}(x),&0\leq x<b^{\*}\_{E},\\ C\_{3}(b^{\*}\_{E})v\_{3}(x)+u(x),&x\geq b^{\*}\_{E},\end{array}\right. |  |

where C1​(⋅)C\_{1}(\cdot), C3​(⋅)C\_{3}(\cdot), v1​(⋅)v\_{1}(\cdot), v2​(⋅)v\_{2}(\cdot), v3​(⋅)v\_{3}(\cdot), u​(⋅)u(\cdot), and B1​(⋅)B\_{1}(\cdot) are defined in
Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | bE∗=inf{b>0:C3​(b)​v3′​(b)+u′​(b)≤γ−β}.\displaystyle b^{\*}\_{E}=\inf\left\{b>0:C\_{3}(b)v\_{3}^{\prime}(b)+u^{\prime}(b)\leq\gamma-\beta\right\}. |  | (3.14) |

It can be shown that bE∗<∞b^{\*}\_{E}<\infty, and that if μ​(0)<0\mu(0)<0, then bE∗≤b0b^{\*}\_{E}\leq b\_{0}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | b0=inf{b≥0:C1​(b)+Λ2​μ​(0)>0}.\displaystyle b\_{0}=\inf\left\{b\geq 0:C\_{1}\,(b)+\frac{\Lambda}{2\mu(0)}>0\right\}. |  | (3.15) |

Finally, an optimal admissible strategy that attains the best performance according to the performance functional 𝒫E\mathcal{P}^{E} is LbE∗:={l¯⋅I​{Xt≥bE∗};t≥0}L^{b^{\*}\_{E}}:=\{\bar{l}\cdot I\{X\_{t}\geq b^{\*}\_{E}\};t\geq 0\}, where bE∗b^{\*}\_{E} is defined in ([3.14](https://arxiv.org/html/2510.27384v1#S3.E14 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

The above theorem shows how to determine the value function and the optimal strategy.
In this regard, the key is to compute the functions v1​(⋅)v\_{1}(\cdot), v2​(⋅)v\_{2}(\cdot), v3​(⋅)v\_{3}(\cdot), and u​(⋅)u(\cdot). Based on these functions, we then compute C1​(⋅)C\_{1}\,(\cdot), C3​(⋅)C\_{3}(\cdot), and B1​(⋅)B\_{1}(\cdot). Analytical solutions are available for some cases, while for others, numerical solutions are required.
Determining v1​(⋅)v\_{1}(\cdot) and v2​(⋅)v\_{2}(\cdot) numerically involves solving two second-order ordinary differential equations (ODEs) numerically.
Similarly, B1​(x)B\_{1}(x) is a particular solution to σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)+Λ=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)+\Lambda=0 with B1​(0)=0B\_{1}(0)=0 and B1′​(0)=0B\_{1}^{\prime}(0)=0, which again can be solved using standard numerical procedures. However, determining v3​(⋅)v\_{3}(\cdot) and u​(⋅)u(\cdot) numerically from the ODEs is more challenging because it involves finding bounded solutions on infinite intervals. To overcome this, we convert the problem to a bounded interval and identify the boundary values at both ends. The following result (with the proof provided in Appendix [A](https://arxiv.org/html/2510.27384v1#A1 "Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) is key to identifying the boundary values mentioned.

###### Lemma 3.4

For the functions, v3​(⋅)v\_{3}(\cdot) and u​(⋅)u(\cdot) defined in Theorem [3.3](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem3 "Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | v3​(x)=𝔼​[e−δ​T^x], and ​u​(x)=𝔼​[∫0T^xe−δ​s​((γ−β)​l¯+Λ)​ds],\displaystyle v\_{3}(x)={\mathbb{E}}\bigg[e^{-\delta\hat{T}^{x}}\bigg],\mbox{ and }u(x)={\mathbb{E}}\bigg[\int\_{0}^{\hat{T}^{x}}e^{-\delta s}((\gamma-\beta)\bar{l}+\Lambda)\,\mathrm{d}s\bigg], |  | (3.16) |

where YtxY\_{t}^{x} is a stochastic process and T^x\hat{T}^{x} is a stopping time defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ytx=x+∫0t(μ​(Ysx)−l¯)​𝑑s+∫0tσ​(Ysx)​𝑑s,s>0,\displaystyle Y\_{t}^{x}=x+\int\_{0}^{t}(\mu(Y\_{s}^{x})-\bar{l})ds+\int\_{0}^{t}\sigma(Y\_{s}^{x})ds,\quad s>0, |  | (3.17) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | T^x=inf{t≥0:Ytx≤0}.\displaystyle\hat{T}^{x}=\inf\{t\geq 0:Y\_{t}^{x}\leq 0\}. |  | (3.18) |

Moreover, the following limiting results hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→∞v3​(x)=0,limx→∞u​(x)=(γ−β)​l¯+Λδ.\displaystyle\lim\_{x\rightarrow\infty}v\_{3}(x)=0,\quad\lim\_{x\rightarrow\infty}u(x)=\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}. |  | (3.19) |

From Theorem [3.3](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem3 "Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we know that
uu is the unique bounded solution to σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)+l¯​(γ−β)+Λ=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)+\bar{l}(\gamma-\beta)+\Lambda=0 on (0,∞)(0,\infty) with the initial value g​(0)=0g(0)=0. This, combined with ([3.19](https://arxiv.org/html/2510.27384v1#S3.E19 "In Lemma 3.4 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), implies that u​(x)u(x) is the unique solution with
u​(0)=0u(0)=0 and limx→∞u​(x)=(γ−β)​l¯+Λδ\lim\_{x\rightarrow\infty}u(x)=\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}. Hence, uu can be numerically determined by choosing a sufficiently large number, say x¯\bar{x}, and then solving the second-order ODE
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)+l¯​(γ−β)+Λ=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)+\bar{l}(\gamma-\beta)+\Lambda=0 with boundary conditions g​(0)=0g(0)=0
and g​(x¯)=(γ−β)​l¯+Λδg(\bar{x})=\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}.
Similarly, v3v\_{3} can be computed by selecting a sufficiently large number, say y¯\bar{y}, and then solving the boundary value second order ODE
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)=0 with g​(0)=1g(0)=1 and g​(y¯)=0g(\bar{y})=0.

### 3.1 The Brownian motion model

If μ¯​(x)≡μ¯\overline{\mu}(x)\equiv\overline{\mu} and σ​(x)≡σ>0\sigma(x)\equiv\sigma>0 are constant, the expressions simplify. Indeed, applying the main theorems from above to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​XtL=(μ¯−l¯−lt)​d​t+σ​d​Wt,t≥0,\mathrm{d}X\_{t}^{L}=(\overline{\mu}-\underline{l}-l\_{t})\mathrm{d}t+\sigma\mathrm{d}W\_{t},\ t\geq 0, |  | (3.20) |

we obtain (see Appendix [B](https://arxiv.org/html/2510.27384v1#A2 "Appendix B Derivations for Subsection 3.1 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") for the derivations):

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE​(x)={(eθ1​x−e−θ2​x)I1(b)−2σ2eθ1​x−1θ1​(θ1+θ2)+2σ21−e−θ2​xθ2​(θ1+θ2))Λ+(eθ1​x−e−θ2​x)​I2​(b),0≤x<b,(e−θ4​x​I3​(b)+2σ2​1θ3​(θ3+θ4)+2σ2​1−e−θ4​xθ4​(θ3+θ4))​Λ+e−θ4​x​I4​(b)+2​((γ−β)​l¯)σ2​1θ3​(θ3+θ4)+2​((γ−β)​l¯)σ2​1−e−θ4​xθ4​(θ3+θ4),x≥b,V\_{b}^{E}(x)=\begin{cases}\left(e^{\theta\_{1}x}-e^{-\theta\_{2}x})I\_{1}(b)-\frac{2}{\sigma^{2}}\frac{e^{\theta\_{1}x}-1}{\theta\_{1}(\theta\_{1}+\theta\_{2})}+\frac{2}{\sigma^{2}}\frac{1-e^{-\theta\_{2}x}}{\theta\_{2}(\theta\_{1}+\theta\_{2})}\right)\Lambda\\ \ +(e^{\theta\_{1}x}-e^{-\theta\_{2}x})I\_{2}(b),&0\leq x<b,\\ \left(e^{-\theta\_{4}x}I\_{3}(b)+\frac{2}{\sigma^{2}}\frac{1}{\theta\_{3}(\theta\_{3}+\theta\_{4})}+\frac{2}{\sigma^{2}}\frac{1-e^{-\theta\_{4}x}}{\theta\_{4}(\theta\_{3}+\theta\_{4})}\right)\Lambda\\ \ +e^{-\theta\_{4}x}I\_{4}(b)+\frac{2((\gamma-\beta)\bar{l})}{\sigma^{2}}\frac{1}{\theta\_{3}(\theta\_{3}+\theta\_{4})}+\frac{2((\gamma-\beta)\bar{l})}{\sigma^{2}}\frac{1-e^{-\theta\_{4}x}}{\theta\_{4}(\theta\_{3}+\theta\_{4})},&x\geq b,\end{cases} |  | (3.21) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ1=−μ+μ2+2​σ2​δσ2,θ2=μ+μ2+2​σ2​δσ2,\displaystyle\theta\_{1}=\frac{-\mu+\sqrt{\mu^{2}+2\sigma^{2}\delta}}{\sigma^{2}},\quad\theta\_{2}=\frac{\mu+\sqrt{\mu^{2}+2\sigma^{2}\delta}}{\sigma^{2}}, |  | (3.22) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θ3=−(μ−l¯)+​(μ−l¯)2+2​σ2​δσ2,θ4=(μ−l¯)+​(μ−l¯)2+2​σ2​δσ2,\displaystyle\theta\_{3}=\frac{-(\mu-\bar{l})+\sqrt{\rule{0.0pt}{8.61108pt}(\mu-\bar{l})^{2}+2\sigma^{2}\delta}}{\sigma^{2}},\quad\theta\_{4}=\frac{(\mu-\bar{l})+\sqrt{\rule{0.0pt}{8.61108pt}(\mu-\bar{l})^{2}+2\sigma^{2}\delta}}{\sigma^{2}}, |  | (3.23) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | I1​(b)=2​(θ2​(θ1+θ4)​eθ1​b+θ1​(θ4−θ2)​e−θ2​b−θ4​(θ1+θ2))σ2​θ1​θ2​(θ1+θ2)+2σ2​θ3(θ1+θ4)​eθ1​b+(θ2−θ4)​e−θ2​b,\displaystyle I\_{1}(b)=\frac{\frac{2\left(\theta\_{2}(\theta\_{1}+\theta\_{4})e^{\theta\_{1}b}+\theta\_{1}(\theta\_{4}-\theta\_{2})e^{-\theta\_{2}b}-\theta\_{4}(\theta\_{1}+\theta\_{2})\right)}{\sigma^{2}\theta\_{1}\theta\_{2}(\theta\_{1}+\theta\_{2})}+\frac{2}{\sigma^{2}\theta\_{3}}}{(\theta\_{1}+\theta\_{4})e^{\theta\_{1}b}+(\theta\_{2}-\theta\_{4})e^{-\theta\_{2}b}}, |  | (3.24) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | I2​(b)=2​(γ−β)​l¯σ2​θ3(θ1+θ4)​eθ1​b+(θ2−θ4)​e−θ2​b,\displaystyle I\_{2}(b)=\frac{\frac{2(\gamma-\beta)\bar{l}}{\sigma^{2}\theta\_{3}}}{(\theta\_{1}+\theta\_{4})e^{\theta\_{1}b}+(\theta\_{2}-\theta\_{4})e^{-\theta\_{2}b}}, |  | (3.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | I3​(b)=2​(eθ1​b−e−θ2​b)σ2​(θ1+θ2)+2​e−θ4​bσ2​(θ3+θ4)−(θ1​eθ1​b+θ2​e−θ2​b)​I1​(b)θ4​e−θ4​b,\displaystyle I\_{3}(b)=\frac{\frac{2(e^{\theta\_{1}b}-e^{-\theta\_{2}b})}{\sigma^{2}(\theta\_{1}+\theta\_{2})}+\frac{2e^{-\theta\_{4}b}}{\sigma^{2}(\theta\_{3}+\theta\_{4})}-(\theta\_{1}e^{\theta\_{1}b}+\theta\_{2}e^{-\theta\_{2}b})I\_{1}(b)}{\theta\_{4}e^{-\theta\_{4}b}}, |  | (3.26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | I4​(b)=2​(γ−β)​l¯​e−θ4​bσ2​(θ3+θ4)−(θ1​eθ1​b+θ2​e−θ2​b)​I2​(b)θ4​e−θ4​b.\displaystyle I\_{4}(b)=\frac{\frac{2(\gamma-\beta)\bar{l}e^{-\theta\_{4}b}}{\sigma^{2}(\theta\_{3}+\theta\_{4})}-(\theta\_{1}e^{\theta\_{1}b}+\theta\_{2}e^{-\theta\_{2}b})I\_{2}(b)}{\theta\_{4}e^{-\theta\_{4}b}}. |  | (3.27) |

The optimal strategy under exponential discounting is LbE∗L^{b\_{E}^{\*}} with bE∗b\_{E}^{\*} determined by
bE∗=inf{b>0:C3​(b)​v3′​(b)+u′​(b)≤γ−β}b^{\*}\_{E}=\inf\{b>0:C\_{3}(b)v\_{3}^{\prime}(b)+u^{\prime}(b)\leq\gamma-\beta\}, cf. ([3.14](https://arxiv.org/html/2510.27384v1#S3.E14 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

## 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting

The equilibrium policy L∗={lt∗;t≥0}L^{\*}=\{l\_{t}^{\*};t\geq 0\} is subject to the carbon emission budget and is a function of the state variable XtX\_{t}.
This is a game with many players (the selves) where each self’s objective is to optimize the total future profits, composed by their own state and control as well as the ones of the future selves who value cash-flows in any specified period inconsistently due to present-bias. We look for a Markov equilibrium solution, which is the policy that achieves the best outcome for a self assuming that all the future selves taking the actions according to the same equilibrium policy (Harris and Laibson, ([2013](https://arxiv.org/html/2510.27384v1#bib.bib19))). We start with establishing an extended Hamilton-Jacobi-Bellman equation (Björk et al., ([2017](https://arxiv.org/html/2510.27384v1#bib.bib5))) for the game-theoretical problem and then construct solutions to the equation.

For any Markov strategies LL and L~\tilde{L} it follows by the Markov property and the definition of the objective function under exponential discounting 𝒫E\mathcal{P}^{E} in ([2.6](https://arxiv.org/html/2510.27384v1#S2.E6 "In 2.1 Exponential discounting ‣ 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫​(x;L,L~)=𝔼x​[∫0τπL,L~∧η0((γ−β)​lt+Λ)​dt+I​{τπL,L~>η0}​α​e−δ​η0​𝒫E​(Xη0πL,L~,L~)].\displaystyle\mathcal{P}(x;L,\tilde{L})={\mathbb{E}}\_{x}\left[\int\_{0}^{\tau^{\pi^{L,\tilde{L}}}\wedge\eta\_{0}}((\gamma-\beta)l\_{t}+\Lambda)\,\mathrm{d}t+I\{\tau^{\pi^{L,\tilde{L}}}>\eta\_{0}\}\alpha e^{-\delta\eta\_{0}}\mathcal{P}^{E}(X\_{\eta\_{0}}^{\pi^{L,\tilde{L}}},\tilde{L})\right]. |  | (4.1) |

As defined in ([2.11](https://arxiv.org/html/2510.27384v1#S2.E11 "In 2.2 Stochastic quasi-hyperbolic discounting ‣ 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), a strategy that attains

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫​(x;L∗,L∗)=supL∈Π𝒫​(x;L,L∗).\displaystyle\mathcal{P}(x;L^{\*},L^{\*})=\sup\_{L\in\Pi}\mathcal{P}(x;L,L^{\*}). |  | (4.2) |

is an equilibrium policy.

If the strategy L∗={l∗​(Xt);t≥0}L^{\*}=\{l^{\*}(X\_{t});t\geq 0\} is an equilibrium solution that satisfies ([4.1](https://arxiv.org/html/2510.27384v1#S4.E1 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and vv is the corresponding value function and is sufficiently smooth, by a standard differential argument for continuous stochastic processes, we can derive the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​v′′​(x)+(μ​(x)−l∗​(x))​v′​(x)−(λ+δ)​v​(x)+(γ−β)​l∗​(x)+Λ+λ​α​𝒫E​(x;L∗)=0,\displaystyle\frac{\sigma^{2}(x)}{2}v^{\prime\prime}(x)+(\mu(x)-l^{\*}(x))v^{\prime}(x)-(\lambda+\delta)v(x)+(\gamma-\beta)l^{\*}(x)+\Lambda+\lambda\alpha\mathcal{P}^{E}(x;L^{\*})=0, |  | (4.3) |

and look for

|  |  |  |
| --- | --- | --- |
|  | l∗(x)=argmaxl∈[0,l¯](σ2​(x)2(x)v′′(x)+(μ(x)−lv′(x)−(λ+δ)v(x)+(γ−β)l+Λ+λα𝒫E(x;L∗))\displaystyle l^{\*}(x)=\operatorname\*{argmax}\_{l\in[0,\bar{l}]}\left(\frac{\sigma^{2}(x)}{2}(x)v^{\prime\prime}(x)+(\mu(x)-lv^{\prime}(x)-(\lambda+\delta)v(x)+(\gamma-\beta)l+\Lambda+\lambda\alpha\mathcal{P}^{E}(x;L^{\*})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =argmaxl∈[0,l¯]((γ−β−v′​(x))​l).\displaystyle\quad\quad\quad=\operatorname\*{argmax}\_{l\in[0,\bar{l}]}\left((\gamma-\beta-v^{\prime}(x))l\right). |  | (4.4) |

Note that 𝒫E​(x;L∗)\mathcal{P}^{E}(x;L^{\*}) in ([4.3](https://arxiv.org/html/2510.27384v1#S4.E3 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) refers to the objective function under exponential discounting.

Let LbL^{b} denote the threshold strategy defined in ([3.2](https://arxiv.org/html/2510.27384v1#S3.E2 "In 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb​(x):=𝒫​(x,Lb,Lb).\displaystyle V\_{b}(x):=\mathcal{P}(x,L^{b},L^{b}). |  | (4.5) |

We can obtain the following key results.

###### Theorem 4.1

The threshold strategy
Lb∗:={lt=l⋅I​{Xt≥b∗};t≥0}L^{b^{\*}}:=\{l\_{t}=l\cdot{I}\{X\_{t}\geq b^{\*}\};\,t\geq 0\}
is a stationary MPE strategy, and the associated (equilibrium) value function is given by

|  |  |  |
| --- | --- | --- |
|  | Vb∗​(x)={C¯1​(b∗)​(v¯1​(x)−v¯2​(x))+B¯1​(x;b∗),0≤x<b∗,C¯3​(b∗)​v¯3​(x)+u¯b∗​(x),x≥b∗.V\_{b^{\*}}(x)=\begin{cases}\overline{C}\_{1}({b^{\*}})(\overline{v}\_{1}(x)-\overline{v}\_{2}(x))+\overline{B}\_{1}(x;b^{\*}),&0\leq x<{b^{\*}},\\[8.0pt] \overline{C}\_{3}({b^{\*}})\overline{v}\_{3}(x)+\overline{u}\_{b^{\*}}(x),&x\geq{b^{\*}}.\end{cases} |  |

Here, the functions v¯1​(⋅)\overline{v}\_{1}(\cdot) and v¯2​(⋅)\overline{v}\_{2}(\cdot) are solutions of the differential equation
σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−(λ+δ)​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-(\lambda+\delta)g(x)=0 for x∈[0,∞),x\in[0,\infty),
with the respective initial conditions:
v¯1​(0)=1\overline{v}\_{1}(0)=1 and v¯1′​(0)=1\overline{v}\_{1}^{\prime}(0)=1, and v¯2​(0)=1\overline{v}\_{2}(0)=1 and v¯2′​(0)=−1.\overline{v}\_{2}^{\prime}(0)=-1.
The function v¯3​(⋅)\overline{v}\_{3}(\cdot) is the bounded solution to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)=0 for x∈[0,∞)x\in[0,\infty)
with initial condition g​(0)=1g(0)=1. The function u¯b​(x)\overline{u}\_{b}(x) (for any b>0b>0) is the bounded solution to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ+(γ−β)​l¯=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+\Lambda+(\gamma-\beta)\bar{l}=0 for x∈[0,∞)x\in[0,\infty)
with initial condition g​(0)=0g(0)=0, and the coefficients C¯1​(b∗)\overline{C}\_{1}(b^{\*}) and C¯3​(b∗)\overline{C}\_{3}(b^{\*}) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯1​(b∗)\displaystyle\overline{C}\_{1}(b^{\*}) | =(B¯1​(b∗,b∗)−u¯b∗​(b∗))​v¯3′​(b∗)−(B¯1′​(b∗,b∗)−u¯b∗′​(b∗))​v¯3​(b∗)(v¯1′​(b∗)−v¯2′​(b∗))​v¯3​(b∗)−(v¯1​(b∗)−v¯2​(b∗))​v¯3′​(b∗),\displaystyle=\frac{\left(\overline{B}\_{1}(b^{\*},b^{\*})-\overline{u}\_{b^{\*}}(b^{\*})\right)\overline{v}\_{3}^{\prime}(b^{\*})-\left(\overline{B}\_{1}^{\prime}(b^{\*},b^{\*})-\overline{u}\_{b^{\*}}^{\prime}(b^{\*})\right)\overline{v}\_{3}(b^{\*})}{\left(\overline{v}\_{1}^{\prime}(b^{\*})-\overline{v}\_{2}^{\prime}(b^{\*})\right)\overline{v}\_{3}(b^{\*})-\left(\overline{v}\_{1}(b^{\*})-\overline{v}\_{2}(b^{\*})\right)\overline{v}\_{3}^{\prime}(b^{\*})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯3​(b∗)\displaystyle\overline{C}\_{3}(b^{\*}) | =(u¯b∗′​(b∗)−B¯1′​(b∗,b∗))​(v¯1​(b∗)−v¯2​(b∗))−(u¯b∗​(b∗)−B¯1​(b∗,b∗))​(v¯1′​(b∗)−v¯2′​(b∗))(v¯1′​(b∗)−v¯2′​(b∗))​v¯3​(b∗)−(v¯1​(b∗)−v¯2​(b∗))​v¯3′​(b∗).\displaystyle=\frac{\left(\overline{u}\_{b^{\*}}^{\prime}(b^{\*})-\overline{B}\_{1}^{\prime}(b^{\*},b^{\*})\right)(\overline{v}\_{1}(b^{\*})-\overline{v}\_{2}(b^{\*}))-\left(\overline{u}\_{b^{\*}}(b^{\*})-\overline{B}\_{1}(b^{\*},b^{\*})\right)(\overline{v}\_{1}^{\prime}(b^{\*})-\overline{v}\_{2}^{\prime}(b^{\*}))}{(\overline{v}\_{1}^{\prime}(b^{\*})-\overline{v}\_{2}^{\prime}(b^{\*}))\overline{v}\_{3}(b^{\*})-(\overline{v}\_{1}(b^{\*})-\overline{v}\_{2}(b^{\*}))\overline{v}\_{3}^{\prime}(b^{\*})}. |  |

Furthermore,
W¯1​(x)=v¯1​(x)​v¯2′​(x)−v¯2​(x)​v¯1′​(x)\overline{W}\_{1}(x)=\overline{v}\_{1}(x)\overline{v}\_{2}^{\prime}(x)-\overline{v}\_{2}(x)\overline{v}\_{1}^{\prime}(x) and B¯1​(x;b)=v¯1​(x)​∫0xv¯2​(y)W¯1​(y)​2​(Λ+λ​α​Vb∗E​(x))σ2​(y)​𝑑y−v¯2​(x)​∫0xv¯1​(y)W¯1​(y)​2​(Λ+λ​α​Vb∗E​(x))σ2​(y)​𝑑y.\overline{B}\_{1}(x;b)=\overline{v}\_{1}(x)\int\_{0}^{x}\frac{\overline{v}\_{2}(y)}{\overline{W}\_{1}(y)}\frac{2(\Lambda+\lambda\alpha V\_{b^{\*}}^{E}(x))}{\sigma^{2}(y)}\,dy-\overline{v}\_{2}(x)\int\_{0}^{x}\frac{\overline{v}\_{1}(y)}{\overline{W}\_{1}(y)}\frac{2(\Lambda+\lambda\alpha V\_{b^{\*}}^{E}(x))}{\sigma^{2}(y)}\,dy.
Here B¯1​(x;b)\overline{B}\_{1}(x;b) is a particular solution to σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+\Lambda=0 with B¯1​(0)=0\overline{B}\_{1}(0)=0 and B¯1′​(0)=0\overline{B}\_{1}^{\prime}(0)=0.

The threshold b∗b^{\*} is determined through

|  |  |  |  |
| --- | --- | --- | --- |
|  | b∗=inf{b>0:C¯3​(b)​v¯3′​(b)+u¯b′​(b)≤γ−β}.\displaystyle b^{\*}=\inf\left\{b>0:\overline{C}\_{3}(b)\overline{v}\_{3}^{\prime}(b)+\overline{u}\_{b}^{\prime}(b)\leq\gamma-\beta\right\}. |  | (4.6) |

The function Vb∗EV\_{b^{\*}}^{E} can be computed using ([3.9](https://arxiv.org/html/2510.27384v1#S3.E9 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), with bb replaced by b∗b^{\*}.
Finally, b∗≤bE∗<∞b^{\*}\leq b^{\*}\_{E}<\infty.

Theorem [4.1](https://arxiv.org/html/2510.27384v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") establishes the existence of equilibrium strategies and defines a rigorous procedure to determine them together with the associated value function. For their derivation, we need to compute the solutions to the given ODEs (whose existence and uniqueness are verified). As illustrated in later sections, in some cases these solutions can be determined explicitly. In other situations, numerical methods are required.

In the spirit of Lemma [3.4](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem4 "Lemma 3.4 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), the following alternative representations for v¯3​(⋅)\overline{v}\_{3}(\cdot) and u¯b​(⋅)\overline{u}\_{b}(\cdot) will be helpful later for numerical evaluations.

###### Lemma 4.2

For the functions, v¯3​(⋅)\overline{v}\_{3}(\cdot) and u¯b​(⋅)\overline{u}\_{b}(\cdot), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯3​(x)=𝔼​[e−(λ+δ)​T^x],\displaystyle\overline{v}\_{3}(x)={\mathbb{E}}\bigg[e^{-(\lambda+\delta)\hat{T}^{x}}\bigg], |  | (4.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯b​(x)=𝔼​[∫0T^x∧η0e−δ​s​((γ−β)​l¯+Λ)​ds+I​{T^x>η0}​α​e−δ​T^x​VbE​(YT^xx)],\displaystyle\overline{u}\_{b}(x)={\mathbb{E}}\bigg[\int\_{0}^{\hat{T}^{x}\wedge\eta\_{0}}e^{-\delta s}((\gamma-\beta)\overline{l}+\Lambda)\,\mathrm{d}s+I\{\hat{T}^{x}>\eta\_{0}\}\;\alpha\;e^{-\delta\hat{T}^{x}}\;V\_{b}^{E}(Y^{x}\_{\hat{T}^{x}})\bigg], |  | (4.8) |

where YtxY\_{t}^{x} is a stochastic process and T^x\hat{T}^{x} is a stopping time defined by
Ytx=x+∫0t(μ​(Ysx)−l¯)​𝑑s+∫0tσ​(Ysx)​𝑑sY\_{t}^{x}=x+\int\_{0}^{t}(\mu(Y\_{s}^{x})-\bar{l})ds+\int\_{0}^{t}\sigma(Y\_{s}^{x})ds for s>0\quad s>0, and T^x=inf{t≥0:Ytx≤0}\hat{T}^{x}=\inf\{t\geq 0:Y\_{t}^{x}\leq 0\}, respectively. Moreover, the following limiting results hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→∞v¯3​(x)=0,limx→∞u¯b​(x)=λ​α+δλ+δ​((γ−β)​l¯+Λ)δ.\displaystyle\lim\_{x\rightarrow\infty}\overline{v}\_{3}(x)=0,\quad\lim\_{x\rightarrow\infty}\overline{u}\_{b}(x)=\frac{\lambda\alpha+\delta}{\lambda+\delta}\frac{((\gamma-\beta)\bar{l}+\Lambda)}{\delta}. |  | (4.9) |

Similar to the last section, the two functions v¯3\bar{v}\_{3} and u¯b\bar{u}\_{b} can be computed numerically by selecting sufficiently large x¯\bar{x} and y¯\bar{y} and solving the following two boundary value ODEs, respectively:
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)=0 with g​(0)=1g(0)=1 and g​(x¯)=0g(\bar{x})=0,
and
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)+Λ+(γ−β)​l¯+λ​α​VbE​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)+\Lambda+(\gamma-\beta)\bar{l}+\lambda\alpha V\_{b}^{E}(x)=0
with g​(0)=0g(0)=0 and g​(y¯)=λ​α+δλ+δ​((γ−β)​l¯+Λ)δg(\bar{y})=\frac{\lambda\alpha+\delta}{\lambda+\delta}\frac{((\gamma-\beta)\bar{l}+\Lambda)}{\delta}.

### 4.1 The Brownian motion model

For the case ([3.20](https://arxiv.org/html/2510.27384v1#S3.E20 "In 3.1 The Brownian motion model ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) with constant coefficients, we obtain (cf. Appendix [D](https://arxiv.org/html/2510.27384v1#A4 "Appendix D Derivations for Subsection 4.1 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") for details)

|  |  |  |
| --- | --- | --- |
|  | Vb​(x)={N1​(b)​(eθ~1​x−e−θ~2​x)+P3​(x;b),0≤x<b,N4​(b)​e−θ~4​x+P5​(x;b),x≥b,V\_{b}(x)=\begin{cases}N\_{1}(b)(e^{\tilde{\theta}\_{1}x}-e^{-\tilde{\theta}\_{2}x})+P\_{3}(x;b),&0\leq x<b,\\ N\_{4}(b)e^{-\tilde{\theta}\_{4}x}+P\_{5}(x;b),&x\geq b,\end{cases} |  |

where

|  |  |  |
| --- | --- | --- |
|  | θ~1=−μ+μ2+2​σ2​(λ+δ)σ2,θ~2=μ+μ2+2​σ2​(λ+δ)σ2,\displaystyle\tilde{\theta}\_{1}=\frac{-\mu+\sqrt{\mu^{2}+2\sigma^{2}(\lambda+\delta)}}{\sigma^{2}},\quad\quad\tilde{\theta}\_{2}=\frac{\mu+\sqrt{\mu^{2}+2\sigma^{2}(\lambda+\delta)}}{\sigma^{2}}, |  |
|  |  |  |
| --- | --- | --- |
|  | θ~3=−(μ−l¯)+(μ−l¯)2+2​σ2​(λ+δ)σ2,θ~4=(μ−l¯)+(μ−l¯)2+2​σ2​(λ+δ)σ2,\displaystyle\tilde{\theta}\_{3}=\frac{-(\mu-\bar{l})+\sqrt{(\mu-\bar{l})^{2}+2\sigma^{2}(\lambda+\delta)}}{\sigma^{2}},\quad\quad\tilde{\theta}\_{4}=\frac{(\mu-\bar{l})+\sqrt{(\mu-\bar{l})^{2}+2\sigma^{2}(\lambda+\delta)}}{\sigma^{2}}, |  |
|  |  |  |
| --- | --- | --- |
|  | P3​(x;b)=−2​Λσ2​eθ~1​x−1θ~1​(θ~1+θ~2)+2​Λσ2​1−e−θ~2​xθ~2​(θ~1+θ~2)+2​λ​ασ2​θ~1​θ~2​M3​(b)\displaystyle P\_{3}(x;b)=-\frac{2\Lambda}{\sigma^{2}}\frac{e^{\tilde{\theta}\_{1}x}-1}{\tilde{\theta}\_{1}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}+\frac{2\Lambda}{\sigma^{2}}\frac{1-e^{-\tilde{\theta}\_{2}x}}{\tilde{\theta}\_{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}+\frac{2\lambda\alpha}{\sigma^{2}\tilde{\theta}\_{1}\tilde{\theta}\_{2}}M\_{3}(b) |  |
|  |  |  |
| --- | --- | --- |
|  | −2​λ​ασ2​(θ~1+θ~2)​[(M1​(b)θ~1−θ1+M2​(b)θ~1+θ2+M3​(b)θ~1)​eθ~1​x+(M1​(b)θ1+θ~2+M2​(b)θ~2−θ2+M3​(b)θ~2)​e−θ~2​x]\displaystyle-\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}\left[\left(\frac{M\_{1}(b)}{\tilde{\theta}\_{1}-\theta\_{1}}+\frac{M\_{2}(b)}{\tilde{\theta}\_{1}+\theta\_{2}}+\frac{M\_{3}(b)}{\tilde{\theta}\_{1}}\right)e^{\tilde{\theta}\_{1}x}+\left(\frac{M\_{1}(b)}{\theta\_{1}+\tilde{\theta}\_{2}}+\frac{M\_{2}(b)}{\tilde{\theta}\_{2}-\theta\_{2}}+\frac{M\_{3}(b)}{\tilde{\theta}\_{2}}\right)e^{-\tilde{\theta}\_{2}x}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +2​λ​ασ2​(θ~1+θ~2)​[(M1​(b)θ~1−θ1+M1​(b)θ1+θ~2)​eθ1​x+(M2​(b)θ~1+θ2+M2​(b)θ~2−θ2)​e−θ2​x],\displaystyle+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}\left[\left(\frac{M\_{1}(b)}{\tilde{\theta}\_{1}-\theta\_{1}}+\frac{M\_{1}(b)}{\theta\_{1}+\tilde{\theta}\_{2}}\right)e^{\theta\_{1}x}+\left(\frac{M\_{2}(b)}{\tilde{\theta}\_{1}+\theta\_{2}}+\frac{M\_{2}(b)}{\tilde{\theta}\_{2}-\theta\_{2}}\right)e^{-\theta\_{2}x}\right], |  | (4.10) |

|  |  |  |
| --- | --- | --- |
|  | P5​(x;b)=2​((γ−β)​l¯+Λ)σ2​1θ~3​(θ~3+θ~4)+2​((γ−β)​l¯+Λ)σ2​1−e−θ~4​xθ~4​(θ~3+θ~4)+2​λ​ασ2​θ~3​θ~4​M5​(b)\displaystyle P\_{5}(x;b)=\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{1}{\tilde{\theta}\_{3}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}+\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{1-e^{-\tilde{\theta}\_{4}x}}{\tilde{\theta}\_{4}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}+\frac{2\lambda\alpha}{\sigma^{2}\tilde{\theta}\_{3}\tilde{\theta}\_{4}}M\_{5}(b) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −2​λ​ασ2​(θ~3+θ~4)​(M4​(b)θ~4−θ4+M5​(b)θ~4)​e−θ~4​x+2​λ​ασ2​(θ~3+θ~4)​(M4​(b)θ~3+θ4+M4​(b)θ~4−θ4)​e−θ4​x,\displaystyle-\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{4}-\theta\_{4}}+\frac{M\_{5}(b)}{\tilde{\theta}\_{4}}\right)e^{-\tilde{\theta}\_{4}x}+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{3}+\theta\_{4}}+\frac{M\_{4}(b)}{\tilde{\theta}\_{4}-\theta\_{4}}\right)e^{-\theta\_{4}x}, |  | (4.11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N1​(b)=θ~4​(P5​(b;b)−P3​(b;b))+P5′​(b;b)−P3′​(b;b)(θ~1+θ~4)​eθ~1​b+(θ~2−θ~4)​e−θ~2​b,\displaystyle N\_{1}(b)=\frac{\tilde{\theta}\_{4}(P\_{5}(b;b)-P\_{3}(b;b))+P\_{5}^{\prime}(b;b)-P\_{3}^{\prime}(b;b)}{(\tilde{\theta}\_{1}+\tilde{\theta}\_{4})e^{\tilde{\theta}\_{1}b}+(\tilde{\theta}\_{2}-\tilde{\theta}\_{4})e^{-\tilde{\theta}\_{2}b}}, |  | (4.12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N4​(b)=N1​(b)​(eθ~1​b−e−θ~2​b)+P3​(b;b)−P5​(b;b)e−θ~4​b,\displaystyle N\_{4}(b)=\frac{N\_{1}(b)(e^{\tilde{\theta}\_{1}b}-e^{-\tilde{\theta}\_{2}b})+P\_{3}(b;b)-P\_{5}(b;b)}{e^{-\tilde{\theta}\_{4}b}}, |  | (4.13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | M1​(b)=K1​(b)−2​Λσ2​1θ1​(θ1+θ2),M2​(b)=−K1​(b)−2​Λσ2​1θ2​(θ1+θ2),\displaystyle M\_{1}(b)=K\_{1}(b)-\frac{2\Lambda}{\sigma^{2}}\frac{1}{\theta\_{1}(\theta\_{1}+\theta\_{2})},\quad M\_{2}(b)=-K\_{1}(b)-\frac{2\Lambda}{\sigma^{2}}\frac{1}{\theta\_{2}(\theta\_{1}+\theta\_{2})}, |  | (4.14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | M3​(b)=2​Λσ2​1θ1​θ2,M4​(b)=K4​(b)−2​((γ−β)​l¯+Λ)σ2​1θ4​(θ3+θ4),\displaystyle M\_{3}(b)=\frac{2\Lambda}{\sigma^{2}}\frac{1}{\theta\_{1}\theta\_{2}},\quad M\_{4}(b)=K\_{4}(b)-\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{1}{\theta\_{4}(\theta\_{3}+\theta\_{4})}, |  | (4.15) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | M5​(b)=2​((γ−β)​l¯+Λ)σ2​1θ3​θ4.\displaystyle M\_{5}(b)=\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{1}{\theta\_{3}\theta\_{4}}. |  | (4.16) |

Here b∗b^{\*} is the solution of −θ~4​N4​(b)​e−θ~4​b+P5′​(b;b)=γ−β-\tilde{\theta}\_{4}N\_{4}(b)e^{-\tilde{\theta}\_{4}b}+P\_{5}^{\prime}(b;b)=\gamma-\beta.

## 5 Probability of Early Depletion

A further quantity of interest is the probability of early depletion when implementing the optimal threshold strategy with and without taking into consideration the present-biasedness of the decision makers. For any threshold strategy LbL^{b} with (not necessarily optimal) threshold bb we define the time of depletion

|  |  |  |  |
| --- | --- | --- | --- |
|  | τb=inf{t≥0:Xtb=0},\tau^{b}=\inf\left\{t\geq 0:X\_{t}^{b}=0\right\}, |  | (5.1) |

where XtbX\_{t}^{b} follows the dynamics ([2.2](https://arxiv.org/html/2510.27384v1#S2.E2 "In 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) for the threshold strategy L=LtbL={L\_{t}^{b}}. Note that ℙ​(τb<∞)=1{\mathbb{P}}(\tau^{b}<\infty)=1, as soon as l¯≥μ​(x)\bar{l}\geq\mu(x) for all x≥0x\geq 0. Its Laplace transform Lb~​(x;s):=𝔼x​[e−s​τb]\widetilde{L^{b}}(x;s):={\mathbb{E}}\_{x}\left[e^{-s\tau^{b}}\right] is more amenable for analytical expressions (see e.g. Gerber and Shiu, ([1998](https://arxiv.org/html/2510.27384v1#bib.bib15)); Albrecher and Cani, ([2017](https://arxiv.org/html/2510.27384v1#bib.bib1))), and in the present case is given as follows (see Appendix [E](https://arxiv.org/html/2510.27384v1#A5 "Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") for the proof).

###### Theorem 5.1

For any b≥0b\geq 0 we have

|  |  |  |
| --- | --- | --- |
|  | Lb~​(x;s)={C4​(b;s)​v4​(x;s)+v5​(x;s),0≤x<b,C6​(b;s)​v6​(x;s)+u​(x;s),x≥b,\displaystyle\widetilde{L\_{b}}(x;s)=\left\{\begin{array}[]{ll}C\_{4}(b;s)v\_{4}(x;s)+v\_{5}(x;s),&0\leq x<b,\\ C\_{6}(b;s)v\_{6}(x;s)+u(x;s),&x\geq b,\end{array}\right. |  |

where
for v4​(⋅;s)v\_{4}(\cdot;s) and v5​(⋅;s)v\_{5}(\cdot;s) are the unique solutions to
σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−s​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-sg(x)=0 on [0,∞)[0,\infty) with initial values, respectively,
v4​(0;s)=0v\_{4}(0;s)=0 and v4′​(0;s)=1v\_{4}^{\prime}(0;s)=1, and
  
v5​(0;s)=1v\_{5}(0;s)=1 and v5′​(0;s)=1v\_{5}^{\prime}(0;s)=1.
Likewise, v6​(x;s)v\_{6}(x;s) and u​(x;s)u(x;s) are the unique bounded solutions to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−s​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-sg(x)=0 with initial value v6​(0;s)=0v\_{6}(0;s)=0 and u​(0;s)=1u(0;s)=1, respectively, and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C4​(b;s)\displaystyle C\_{4}(b;s) | =(u​(b;s)−v5​(b;s))​v6′​(b;s)−(u′​(b;s)−v5′​(b;s))​v6​(b;s)v4​(b;s)​v6′​(b;s)−v4′​(b;s)​v6​(b;s),\displaystyle=\frac{\left(u(b;s)-v\_{5}(b;s)\right)v\_{6}^{\prime}(b;s)-\left(u^{\prime}(b;s)-v\_{5}^{\prime}(b;s)\right)v\_{6}(b;s)}{v\_{4}(b;s)v\_{6}^{\prime}(b;s)-v\_{4}^{\prime}(b;s)v\_{6}(b;s)}, |  | (5.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C6​(b;s)\displaystyle C\_{6}(b;s) | =(u′​(b;s)−v5′​(b;s))​v4​(b;s)−(u​(b;s)−v5​(b;s))​v4′​(b;s)v4​(b;s)​v6′​(b;s)−v4′​(b;s)​v6​(b;s).\displaystyle=\frac{\left(u^{\prime}(b;s)-v\_{5}^{\prime}(b;s)\right)v\_{4}(b;s)-\left(u(b;s)-v\_{5}(b;s)\right)v\_{4}^{\prime}(b;s)}{v\_{4}(b;s)v\_{6}^{\prime}(b;s)-v\_{4}^{\prime}(b;s)v\_{6}(b;s)}. |  | (5.4) |

Define the finite-time depletion probability

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψb​(x;t)=ℙx​(τb≤t),x,t≥0.\displaystyle\psi\_{b}(x;t)={\mathbb{P}}\_{x}\left(\tau^{b}\leq t\right),\quad x,t\geq 0. |  | (5.5) |

Clearly, ψb​(x;t)\psi\_{b}(x;t) can be obtained as the inverse Laplace transform w.r.t. ss of Lb~​(x;s)/s\widetilde{L\_{b}}(x;s)/s. Finally, the finite-time depletion probability of the optimal strategy under exponential discounting is denoted by ψE​(x;t):=ψbE​(x;t)\psi^{E}(x;t):=\psi\_{b^{E}}(x;t) and under stochastic quasi-hyperbolic discounting by ψ∗​(x;t):=ψb∗​(x;t)\psi^{\*}(x;t):=\psi\_{b^{\*}}(x;t), where bEb^{E} and b∗b^{\*} are the optimal thresholds in the respective cases.

## 6 Numerical Illustrations for the Brownian Motion Model

In this section, we present a numerical illustration that allows quantitative insight into the impact of present-bias on the optimal production and emission strategies identified in the previous sections. We focus here on the Brownian model (a model with surplus-dependent diffusion coefficients will be considered in Section [7](https://arxiv.org/html/2510.27384v1#S7 "7 Numerical Illustrations for More General Models ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). We first need to choose numerical values for the involved parameters whose magnitudes are motivated by practical considerations, but naturally remain rough magnitudes. Suppose the total global remaining carbon budget until 2050 (as of 20252025) is 340​GtCO2340\ \text{GtCO}\_{2} (which is a rough estimate based on the Global Carbon Project, ([2022](https://arxiv.org/html/2510.27384v1#bib.bib17)).
If we consider the company under consideration to receive a share of 0.0001%0.0001\% of that amount, we have x0=34x\_{0}=34 (in units of 10410^{4} tCO2\text{tCO}\_{2})
to be used over the next 2525 years. In terms of the drift parameter, we may assume that the expected annual increase in capacity due to Direct Air Capture (DAC) and other carbon removal technology advancement could be set to μ¯=0.05\bar{\mu}=0.05.444Lebling et al., ([2025](https://arxiv.org/html/2510.27384v1#bib.bib27)) estimate that the total global CCUS (Carbon Capture, Utilization and Sequestration) capacity will reach between 416416 and 520520 MtCO2/yr. The above choice refers to the proportional share for the value 500500 MtCO2/yr. Furthermore we choose the volatility parameter to be σ=2\sigma=2.555One may justify such a magnitude as follows. The parameter σ\sigma captures uncertainties due to both earth system dynamics and technology development. One may want to use the concept of interannual variability (IAV) as a basis here.
In the context of the carbon cycle, IAV commonly describes annual variations in net ecosystem exchange (NEE), net primary production (NPP), or the carbon sink strength.
According to Marcolla et al., ([2017](https://arxiv.org/html/2510.27384v1#bib.bib31)), the average annual NEE globally is approximately 120​gC​m−2​yr−1120~\text{gC}~\text{m}^{-2}~\text{yr}^{-1}, which means terrestrial ecosystems absorb around 120120 grams of carbon per square meter each year. The reported IAV is about 1515–20​gC​m−2​yr−120~\text{gC}~\text{m}^{-2}~\text{yr}^{-1}, implying a relative fluctuation of 12%12\%–17%17\% of the mean capacity.
For simplicity, we assume the IAV to be 6%6\% of the initial capacity x0=34x\_{0}=34 (since the emission capacity declines as the budget is gradually depleted):
leading to σ=34⋅0.06=2\sigma=34\cdot 0.06=2.

### 6.1 Impact of present-bias on the emission schedule

Recall that the parameter λ\lambda (the arrival intensity of the future periods, and correspondingly the ‘disappearance intensity’ of the present period) and the discounting weight α\alpha capture the impatience of the decision-maker.
For any fixed α\alpha, a larger λ\lambda implies a higher intensity rate for eliminating the present period and transitioning to future periods. Since future periods are discounted further by the additional factor α<1\alpha<1, this leads to greater impatience and stronger present-bias.
At the same time, for any fixed λ>0\lambda>0, a smaller α\alpha places less weight on future cash flows, also indicating higher impatience. Note that either λ=0\lambda=0 or α=1\alpha=1 remove the present-bias.

Impact of λ\lambda. In addition to
x0=34x\_{0}=34, μ¯=0.05\bar{\mu}=0.05 and σ=2\sigma=2, we set l¯=1\underline{l}=1, δ=0.1\delta=0.1, α=0.9\alpha=0.9, γ=0.9\gamma=0.9, Λ¯=0.5\overline{\Lambda}=0.5, l¯=3\overline{l}=3, ci​n​d=0.1c\_{ind}\,=0.1 and ct​a​x=0.05c\_{tax}=0.05. Then β=ci​n​d​γ+ct​a​x=0.086\beta=c\_{ind}\,\gamma+c\_{tax}=0.086 and Λ=Λ¯+(γ−β)​l¯=1.344\Lambda=\overline{\Lambda}+(\gamma-\beta)\underline{l}=1.344. Note that with this choice l¯=1\underline{l}=1 of the baseline emission rate, we have a negative net drift μ​(0)=−0.95\mu(0)=-0.95 for the optimization problem.
The optimal threshold levels b∗b^{\*}, calculated using the formulas from Section [4](https://arxiv.org/html/2510.27384v1#S4 "4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") together with the resulting early depletion probabilities ψ∗​(34;25)\psi^{\*}(34;25) within the next 25 years, are given in the following tables for various combinations of λ\lambda and α\alpha.

| λ\lambda | 0 | 0.1 | 0.25 | 1 | 4 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| b∗b^{\*} | 5.51 | 5.08 | 4.68 | 3.86 | 3.06 | 2.58 |
| ψ∗​(34;25)\psi^{\*}(34;25) | 0.9968 | 0.9985 | 0.9993 | 0.9997 | 1 | 1 |

Table 1: Optimal b∗b^{\*} and ψ∗​(34;25)\psi^{\*}(34;25) for varying λ\lambda (α=0.9\alpha=0.9).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| α\alpha | 0.5 | 0.7 | 0.8 | 0.9 | 0.95 | 1.0 |
| b∗b^{\*} | 0.83 | 1.66 | 2.53 | 3.86 | 4.66 | 5.51 |
| ψ∗​(34;25)\psi^{\*}(34;25) | 1 | 1 | 1 | 0.9997 | 0.9994 | 0.9968 |

Table 2: Optimal b∗b^{\*} and ψ∗​(34;25)\psi^{\*}(34;25) for varying α\alpha (λ=1\lambda=1).

In Table [2](https://arxiv.org/html/2510.27384v1#S6.T2 "Table 2 ‣ 6.1 Impact of present-bias on the emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), we fix α=0.9\alpha=0.9 and vary λ\lambda within the interval [0,12][0,12] (recall that λ=0\lambda=0 refers to no present-bias, and larger values of λ\lambda indicate a higher degree of present-bias). Specifically, λ=1\lambda=1 implies that the expected duration of the “present” period is 1 year, λ=0.25\lambda=0.25 corresponds to an expected present period of 4 years, and λ=12\lambda=12 represents an extremely impatient case in which the present period lasts, on average, only 1 month. As expected, the optimal threshold for excess production/emission decreases with increasing present-bias from the exponential discounting case λ=0\lambda=0, implying earlier excess emissions and higher overall emission amounts. This suggests that if policies are made under the assumption that decision-makers are not present-biased, while in reality they are, the amount of resulting emissions is underestimated.

Although large values of λ\lambda are not central to our analysis,
we highlight an interesting phenomenon that may be of mathematical interest, particularly in theoretical studies of hyperbolic discounting. When λ\lambda is very large, the impact of increasing λ\lambda on strategies may become non-monotonic, cf. Figure [1](https://arxiv.org/html/2510.27384v1#S6.F1 "Figure 1 ‣ 6.1 Impact of present-bias on the emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target"). For α\alpha-values close to 1, the interaction between parameters can lead to higher threshold levels (i.e., lower emissions) as λ\lambda increases. This suggests that when the present period is extremely short but future profits are still significantly weighted, it may be optimal to prioritize maximizing total future benefits resulting in reduced present emissions, as reflected in a higher threshold. At the same time, for other large values of λ\lambda the threshold is smaller again, making it more beneficial to prioritize immediate gains. Such a non-monotonicity is noteworthy, although it only appears for certain specific parameter ranges.

![Refer to caption](x1.png)


Figure 1: Optimal threshold levels b∗b^{\*} as a function of λ\lambda for various values of α\alpha.

Impact of α\alpha. Table [2](https://arxiv.org/html/2510.27384v1#S6.T2 "Table 2 ‣ 6.1 Impact of present-bias on the emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") shows the results for λ=1\lambda=1 and variable values of α\alpha. One observes that the sensitivity of b∗b^{\*} to changing values of α\alpha is more pronounced (α=1\alpha=1 again refers to exponential discounting without present-bias).
As α\alpha decreases from 11, the present-bias is increased and the excess production threshold is lowered.

Comparison to Exponential Discounting. In line with Theorem [4.1](https://arxiv.org/html/2510.27384v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), we observe that the excess production threshold is lower under present bias than under exponential discounting, which results in increased emissions and a reduced budget, as illustrated in Figure [2](https://arxiv.org/html/2510.27384v1#S6.F2 "Figure 2 ‣ 6.1 Impact of present-bias on the emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") with a comparison of two sample paths generated with the same random seed. In both cases, the budget is fully depleted before time T=25T=25. Note also that for the concrete choice of parameters, the strategies conincide for the first seven years.

![Refer to caption](x2.png)


Figure 2: Comparison of two sample paths generated with the same random seed: optimal strategy under exponential discounting (with optimal threshold bE∗=3.86b\_{E}^{\*}=3.86) versus stochastic quasi-hyperbolic discounting (λ=1\lambda=1, α=0.9\alpha=0.9) with optimal threshold b∗=5.51b^{\*}=5.51.

In the exponential discounting case without present-bias, one should also expect a lower optimal threshold when increasing the discount rate δ\delta, which downgrades future contributions. Indeed, Figure [3](https://arxiv.org/html/2510.27384v1#S6.F3 "Figure 3 ‣ 6.1 Impact of present-bias on the emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") depicts the optimal threshold level under exponential discounting for the above parameters, now as a function of δ\delta.

![Refer to caption](x3.png)


Figure 3: Optimal threshold bE∗b\_{E}^{\*} as a function of δ\delta for exponential discounting (ct​a​x=0c\_{tax}=0).

It is of interest to compare which level of δ\delta without present-bias leads to the same optimal decisions (threshold levels) as the effect of present-bias for a lower level of δ\delta. Figure [5](https://arxiv.org/html/2510.27384v1#S6.F5 "Figure 5 ‣ 6.2 Impact of level of social responsibility on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") shows the optimal threshold for equilibrium strategies of various stochastic quasi-hyperbolic discounting settings (λ,α)(\lambda,\alpha) for δ=0.1\delta=0.1.
The dotted horizontal lines represent the optimal threshold levels bE∗b\_{E}^{\*} for exponential discounting for various other δ\delta-levels, so that one can identify which parameters in each of the two discounting regimes lead to the same eventual optimal strategy. For instance, the equilibrium strategy for δ=0.1\delta=0.1, λ=2\lambda=2 and α=0.9\alpha=0.9 under stochastic quasi-hyperbolic discounting leads to the same threshold (and hence value function) as exponential discounting with a discount rate around δ=0.15\delta=0.15 (Figure [5](https://arxiv.org/html/2510.27384v1#S6.F5 "Figure 5 ‣ 6.2 Impact of level of social responsibility on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") gives a more detailed account on matching levels).
In other words, the effect of present bias in this case is comparable to increasing the exponential discount rate δ\delta from
0.1 to 0.15. This raises the question of whether explicitly accounting for present bias could, in general, be replaced by using a higher discount rate within a standard exponential discounting model. The answer is no, and we will elaborate on this in Section [6.3](https://arxiv.org/html/2510.27384v1#S6.SS3 "6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (Remark [6.1](https://arxiv.org/html/2510.27384v1#S6.ThmRemark1 "Remark 6.1 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

### 6.2 Impact of level of social responsibility on emission schedule

Recall that the term Λ¯\overline{\Lambda} in the objective function rewards avoiding early depletion of the carbon budget.
We can interpret it as a measure of how much the company values preserving its emission budget, which can, to some extent, reflect its social responsibility and sustainability awareness.

We now examine how Λ¯\overline{\Lambda} affects decision-making by varying its value while keeping all other parameters fixed. Fixing again δ=0.1\delta=0.1, α=0.9\alpha=0.9, λ=1\lambda=1, we now vary Λ¯\bar{\Lambda} (and correspondingly Λ=Λ¯+(γ−β)​l¯\Lambda=\bar{\Lambda}+(\gamma-\beta)\underline{l}). Table [3](https://arxiv.org/html/2510.27384v1#S6.T3 "Table 3 ‣ 6.2 Impact of level of social responsibility on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") shows how
additional weight on sustainability increases the optimal excess production/emission threshold in the present-biased case. As expected, higher
sustainability awareness postpones emissions, resulting in lower overall emissions.
Figure [6](https://arxiv.org/html/2510.27384v1#S6.F6 "Figure 6 ‣ 6.2 Impact of level of social responsibility on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") gives a more detailed picture on how choices of present-bias parameters and the sustainability weight Λ¯\bar{\Lambda} affect the optimal emission schedule. It quantifies how b∗b^{\*} changes as a function of intensity λ\lambda of arrival for the future period, weight α\alpha for future profits and sustainability weight, Λ¯\bar{\Lambda}, respectively. Along the vertical axis, the probability of early depletion resulting from implementing b∗b^{\*} is also indicated.

![Refer to caption](x4.png)


Figure 4: Comparison of optimal threshold levels b∗b^{\*} for stochastic hyperbolic discounting (with δ=10%\delta=10\%) and for exponential discounting (for various δ\delta-values, indicated by black dotted horizontal lines), as a function of λ\lambda.

![Refer to caption](x5.png)


Figure 5: Pairs of λ\lambda and α\alpha that yield the same equilibrium threshold b∗b^{\*} for different target values b∗=b0,b1,b2b^{\*}=b\_{0},b\_{1},b\_{2}, or b3b\_{3}.



| Λ¯\overline{\Lambda} | 0.0 | 0.1 | 0.2 | 0.5 | 0.8 |
| --- | --- | --- | --- | --- | --- |
| b∗b^{\*} | 0 | 0.52 | 1.32 | 3.86 | 6.12 |

Table 3: Optimal threshold levels for varying Λ¯\bar{\Lambda}



![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 6: Optimal threshold b∗b^{\*} (and corresponding early depletion probability P=ψ∗​(34;25)P=\psi^{\*}(34;25)) of the equilibrium strategy under different behavioral parameters with α=0.9\alpha=0.9:
as a function of future arrival intensity λ\lambda and Λ¯\bar{\Lambda} (left) and as a function of the additional future period discount factor α\alpha and and the social responsibility factor Λ¯\bar{\Lambda} (right).

### 6.3 Impact of carbon tax on emission schedule

Finally, we want to examine how setting a carbon tax level ct​a​xc\_{tax} impacts decision-making by varying its value while keeping all other parameters fixed. Choosing again ci​n​d=0.1c\_{ind}\,=0.1, x0=34x\_{0}=34, μ¯=0.05\bar{\mu}=0.05, l¯=1\underline{l}=1, σ=2\sigma=2, δ=0.1\delta=0.1, γ=0.9\gamma=0.9, Λ¯=0.5\bar{\Lambda}=0.5, l¯=3\bar{l}=3 and α=0.9\alpha=0.9, we now vary ct​a​xc\_{tax}. Note that both β=ci​n​d​γ+ct​a​x\beta=c\_{ind}\,\gamma+c\_{tax} and Λ=Λ¯+(γ−β)​l¯\Lambda=\bar{\Lambda}+(\gamma-\beta)\underline{l} vary with ct​a​xc\_{tax}.

We calculate the optimal strategy for various levels of carbon tax and present the results for in Tables [4](https://arxiv.org/html/2510.27384v1#S6.T4 "Table 4 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") and [5](https://arxiv.org/html/2510.27384v1#S6.T5 "Table 5 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") for λ=1\lambda=1 and λ=12\lambda=12, respectively. Moreover, Figure [7](https://arxiv.org/html/2510.27384v1#S6.F7 "Figure 7 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") plots how b∗b^{\*} changes as the tax rate ct​a​xc\_{tax} increases, for various levels of present bias represented by different values of λ\lambda, with α\alpha fixed at 0.90.9. The probability indicated at the end of each horizontal dashed line represents the likelihood of early depletion if the production strategy or emission policy uses the maximal excess production threshold at that level. For example, the second dashed line from the bottom indicates that if the production policy begins maximal excess production when the budget exceeds 55, the probability of early depletion is 0.99790.9979.

| ct​a​xc\_{tax} | 0 | 0.05 | 0.1 | 0.3 | 0.5 | 0.7 | 0.8 | 0.802 | 0.803 | 0.804 | 0.805 | 0.809 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b∗b^{\*} | 3.36 | 3.58 | 3.83 | 5.21 | 7.72 | 13.71 | 22.47 | 22.79 | 22.95 | 23.12 | 23.29 | 23.99 |

Table 4: Optimal b∗b^{\*} for varying carbon tax levels (λ=1\lambda=1)



| ct​a​xc\_{tax} | 0 | 0.05 | 0.10 | 0.30 | 0.50 | 0.66 | 0.67 | 0.68 | 0.69 | 0.70 | 0.72 | 0.73 | 0.74 | 0.75 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b∗b^{\*} | 1.88 | 2.14 | 2.42 | 3.92 | 6.52 | 10.38 | 24.00 | 11.04 | 19.00 | 10.98 | 11.16 | 10.98 | 38.00 | 11.92 |
| ct​a​xc\_{tax} | 0.76 | 0.77 | 0.78 | 0.79 | 0.8 | 0.801 | 0.802 | 0.803 | 0.804 | 0.805 | 0.806 | 0.807 | 0.808 | 0.809 |
| b∗b^{\*} | 11.49 | 15.50 | 10.88 | 10.99 | 22.50 | 23.41 | 24.89 | 10.94 | 12.29 | 22.48 | 17.88 | 10.98 | 31.00 | 10.99 |

Table 5: Optimal b∗b^{\*} for varying carbon tax levels (λ=12\lambda=12)

![Refer to caption](x8.png)


Figure 7: Optimal threshold b∗b^{\*} as a function of tax rate ct​a​xc\_{tax} for various levels of λ\lambda (α=0.9\alpha=0.9).

One can observe that
without carbon tax (ct​a​x=0c\_{tax}=0) the excess production threshold b∗b^{\*} is at its lowest, indicating a strong desire for early consumption of the budget and higher production, which results in higher emissions. As carbon tax increases, the incentive for production and consumption decreases (reflected in an increased threshold b∗b^{\*}), lowering carbon emissions. The curbing effect strengthens as the carbon tax increases, up to certain turning points that will be discussed below.

Generally, for a higher present bias (larger λ\lambda), a larger tax rate is required to bring down the emission patterns to the same level as for lower present bias (at least as long as the tax rate is not excessively high).
The concrete needed trade-off can be spotted in Figure [7](https://arxiv.org/html/2510.27384v1#S6.F7 "Figure 7 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target").
Therefore, if carbon tax rates are designed ignoring present bias, they may fail to achieve their intended effect. For example, if a carbon policy is designed to restrict the probability of early depletion to around 96.74%96.74\%, and present-bias is ignored, ct​a​xc\_{tax} would be set around 0.40.4 (see the red curve).
However, if there is some level of present-bias (e.g., λ=1\lambda=1), to achieve that effect, the tax should have been set around 0.520.52.

However, beyond a certain threshold (indicated by the dots on the curves in Figure [7](https://arxiv.org/html/2510.27384v1#S6.F7 "Figure 7 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") and the first cell highlighted in gray in Table [5](https://arxiv.org/html/2510.27384v1#S6.T5 "Table 5 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") for the case λ=12\lambda=12) the impact of further increases in carbon tax ct​a​xc\_{tax} becomes more variable.
This suggests that excessively high carbon tax rates may be suboptimal, particularly when combined with stronger present bias (larger λ\lambda), which aligns with findings by MacKenzie and Ohndorf, ([2012](https://arxiv.org/html/2510.27384v1#bib.bib30)) that “revenue-raising instruments, such as carbon taxes, are suboptimal” (see also Borissov and Bretschger, ([2022](https://arxiv.org/html/2510.27384v1#bib.bib6))). One can observe in Figure [7](https://arxiv.org/html/2510.27384v1#S6.F7 "Figure 7 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that this phenomenon is more pronounced (and occurs at lower ct​a​xc\_{tax} levels) for higher degrees of present-biasedness (higher λ\lambda).

Figure [8](https://arxiv.org/html/2510.27384v1#S6.F8 "Figure 8 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target") shows the effect of carbon tax for a fixed λ>0\lambda>0 but varying α\alpha (which is another way to measure present-bias). It reveals similar patterns on the impact of carbon tax on production and emission strategies. If the tax rate is determined under the assumption that there is no present-bias, but in reality present-bias exists, then actual emissions will be higher than targeted. Specifically, if ct​a​xc\_{tax} is chosen using the curve corresponding to α=1\alpha=1 (no present bias) and based on a targeted probability of early depletion (e.g., P=80.17%P=80.17\%, indicated by the first dashed line from the top), then the tax rate ct​a​xc\_{tax} would be approximately 0.640.64. However, under present-biased preferences (e.g., α=0.9\alpha=0.9), the resulting production strategy under such a tax rate (around 0.640.64) yields a lower threshold b∗b^{\*}, leading to a higher probability of early depletion—around 86%86\%. This illustrates again that ignoring present-bias when setting policy negatively affects the achievement of emission targets set by social planners. Furthermore, present-bias may also undermine the effectiveness of carbon taxation, as higher tax rates do not necessarily lead to lower emissions— indicated at the dot on the curve for α=0.9\alpha=0.9 on the right-hand panel in Figure [8](https://arxiv.org/html/2510.27384v1#S6.F8 "Figure 8 ‣ 6.3 Impact of carbon tax on emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target").

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 8: Optimal threshold b∗b^{\*} as a function of tax rate ct​a​xc\_{tax} for various levels of α\alpha (λ=1\lambda=1 (left) and λ=12\lambda=12 (right))

In conclusion, the findings suggest that present-bias negatively impacts the effectiveness of carbon taxes, with stronger biases having a greater effect.
This highlights the importance for social planners and governments to account for present-biased behavior when designing effective carbon tax policies.

###### Remark 6.1

Finally, let us return to a question raised at the end of Section [6.1](https://arxiv.org/html/2510.27384v1#S6.SS1 "6.1 Impact of present-bias on the emission schedule ‣ 6 Numerical Illustrations for the Brownian Motion Model ‣ On effects of present-bias on carbon emission patterns towards a net zero target"). As it was shown there, the equilibrium strategy under stochastic quasi-hyperbolic discounting can match that of an exponential discounting model with a higher discount rate (in the example given there by an increase from δ=0.1\delta=0.1 to 0.150.15).
However, this does not mean that the effect of present-biasedness can be equivalently replaced by using an exponential discounting model with a suitably higher discount rate. In that example, without carbon tax the probability of early depletion was about 99%99\% for both cases.
Suppose we want to determine how much carbon tax should be imposed in order to reduce the probability of early depletion to about 90%90\%. If we ignore present-bias and instead adopt the exponential discounting model with the equivalent higher discount rate of 14.08%14.08\%, we would need to set the carbon tax instead at 0.6350.635. Under this increased carbon tax, the optimal strategy in the exponential discounting case corresponds to a threshold of 9.069.06.
However, if we apply the same carbon tax in the actual present-biased scenario, the resulting threshold becomes 8.198.19, and the early depletion probability is reduced only to about 93%93\%, missing the desired target.
This example illustrates that determining the carbon tax based on an exponential discounting model with an adjusted higher discount rate, calibrated to match the pre-tax equilibrium, results in a less effective policy when applied to agents exhibiting present-bias.

## 7 Numerical Illustrations for More General Models

Our general diffusion setup in this paper in principle also allows to study more involved stochastic processes for the carbon budget. As an alternative model, let us here briefly consider an Ornstein–Uhlenbeck type process with state-dependent volatility for the cumulative carbon emission budget available to a company over time. For instance, one could assume that the target atmospheric CO2 concentration in 20502050 is 450450 ppm (which translates to cumulative net emissions since pre-industrial times of approximately 1,3301,330 GtCO2, see e.g. Bennedsen et al., ([2023](https://arxiv.org/html/2510.27384v1#bib.bib4))). The aggregate carbon emission capacity available at any time tt is then linked to the difference between the target and the current concentration level, which evolves dynamically. Translating this into an individual target level θ\theta of the company may then justify an adaptive budget available at time tt of the form

|  |  |  |
| --- | --- | --- |
|  | d​XtL=κ​(θ−XtL)​d​t+(σ0+σ1​XtL)​d​Wt−(l0+lt)​d​t.\displaystyle dX\_{t}^{L}=\kappa(\theta-X\_{t}^{L})dt+(\sigma\_{0}+\sigma\_{1}X\_{t}^{L})dW\_{t}-(l\_{0}+l\_{t})dt. |  |

The volatility term σ0+σ1​XtL\sigma\_{0}+\sigma\_{1}X\_{t}^{L} may reflect policy uncertainty, technological change and estimation uncertainty, and ltl\_{t} is determined by the emission schedule LL. The choice θ=35\theta=35, σ0=0.5\sigma\_{0}=0.5, σ1=0.11\sigma\_{1}=0.11 leads to similar initial values as before, and according to Bennedsen et al., ([2023](https://arxiv.org/html/2510.27384v1#bib.bib4)), one may choose κ=0.018\kappa=0.018. The other parameters we choose again as l¯=3\underline{l}=3, δ=0.1\delta=0.1, γ=0.9\gamma=0.9, Λ¯=0.5\overline{\Lambda}=0.5, l¯=6\overline{l}=6, ci​n​d=0.1c\_{ind}\,=0.1 and ct​a​x=0.05c\_{tax}=0.05.

Impact of λ\lambda and α\alpha. We calculate
the optimal threshold b∗b^{\*} and the resulting probability of early depletion for various combinations of λ\lambda and α\alpha.

|  | λ=0.1\lambda=0.1 | λ=0.25\lambda=0.25 | λ=0.5\lambda=0.5 | λ=1\lambda=1 | λ=4\lambda=4 | λ=12\lambda=12 |
| --- | --- | --- | --- | --- | --- | --- |
| α=0.5\alpha=0.5 | 4.52 | 3.56 | 2.79 | 2.00 | 0.15 | 0.00 |
| α=0.6\alpha=0.6 | 4.81 | 4.00 | 3.37 | 2.70 | 0.62 | 0.00 |
| α=0.7\alpha=0.7 | 5.11 | 4.49 | 4.02 | 3.51 | 1.77 | 0.66 |
| α=0.8\alpha=0.8 | 5.43 | 5.01 | 4.70 | 4.37 | 3.13 | 2.32 |
| α=0.9\alpha=0.9 | 5.76 | 5.55 | 5.40 | 5.23 | 4.56 | 4.08 |
| α=0.95\alpha=0.95 | 5.92 | 5.82 | 5.75 | 5.66 | 5.31 | 5.05 |
| α=1\alpha=1 | 6.09 | 6.09 | 6.09 | 6.09 | 6.09 | 6.09 |

Table 6: Optimal threshold b∗b^{\*} for various combinations of λ\lambda and α\alpha

Impact of level of social responsibility on emission schedule.
Recall that the term Λ¯\overline{\Lambda} indicates how much the company values preserving its emission budget and reflect its social responsibility and sustainability awareness in some sense.
We now examine how Λ¯\overline{\Lambda} affects decision-making by varying its value while keeping all other parameters fixed.
Table [7](https://arxiv.org/html/2510.27384v1#S7.T7 "Table 7 ‣ 7 Numerical Illustrations for More General Models ‣ On effects of present-bias on carbon emission patterns towards a net zero target") shows how
additional weight on sustainability increases the optimal excess production/emission threshold and lowers the probability of early depletion in the present-biased case. As expected, higher
sustainability awareness postpones emissions, resulting in lower overall emissions.

| Λ¯\overline{\Lambda} | 0 | 0.1 | 0.2 | 0.5 | 0.8 |
| --- | --- | --- | --- | --- | --- |
| b∗b^{\*} | 3.00 | 3.52 | 4.00 | 5.23 | 6.25 |

Table 7: Optimal threshold levels and resulting early depletion probabilities for varying Λ¯\bar{\Lambda}

Figure [9](https://arxiv.org/html/2510.27384v1#S7.F9 "Figure 9 ‣ 7 Numerical Illustrations for More General Models ‣ On effects of present-bias on carbon emission patterns towards a net zero target") gives a more detailed picture on how choices of present-bias parameters and the sustainability weight Λ¯\bar{\Lambda} affect the optimal emission schedule. It quantifies how b∗b^{\*} changes as a function of intensity λ\lambda of arrival for the future period, weight α\alpha for future profits and sustainability weight, Λ¯\bar{\Lambda}, respectively.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 9: Optimal threshold b∗b^{\*} of the equilibrium strategy under different behavioral parameters: as a function of future arrival intensity λ\lambda and social responsibility factor Λ¯\bar{\Lambda} for α=0.9\alpha=0.9 (left) and as a function of the additional future period discount factor α\alpha and Λ¯\bar{\Lambda} for λ=1\lambda=1 (right).

## 8 Conclusion

In this paper, we provide a framework to study optimal carbon emission schedules for an agent aiming to maximize profit, while being subject to emission constraints and incorporating social responsibility awareness. In particular, we looked into the effects of present-biasedness on the optimal emission behavior. The problem was formulated as an intra-personal game, where the objective is to search for equilibrium solutions. We established the existence of these equilibrium solutions and provided detailed procedures for finding the equilibrium value function and equilibrium emission/production strategy in a general diffusion setup, under stochastic quasi-hyperbolic discounting.

In a detailed numerical illustration for the case of a diffusion setting with constant coefficients, we showed that present-bias leads companies to consume carbon emissions earlier and more aggressively. This behavior results in a higher probability of early depletion compared to the exponential discounting case (the case with no present-bias). Furthermore, the higher the degree of present-bias, the greater the impatience regarding the consumption of the emission budget. We also examined the impact of the level of sustainability preferences and showed in what way it has a positive effect on emission patterns and later depletion of the allocated carbon budget. We furthermore studied how carbon tax can provide incentives to an individual company’s reduced emission behavior. As the tax increases, the effect becomes more significant. However, when the tax reaches a certain level, the effect begins to diminish. A further insight provided to the social planners is that if policies (carbon tax levels in particular) are set ignoring present-bias of companies, the desired effects may not materialize.

As indicated in the introduction, while the exposition of the paper was formulated for the case of a firm looking for optimal production decisions with implied carbon emission patterns, the results may also be interpreted for rational individuals who decide about carbon-intensive consumption patterns when facing a carbon budget constraint and potential taxes on carbon-intensive activities or consumption goods.

A main purpose of this paper was to establish a link between the above questions and solution techniques developed in insurance risk theory, which enabled to determine the optimal production/consumption behavior, where the remaining surplus in a dividend-paying insurance company now took the role of the remaining carbon-budget to spend. We deliberately restricted the analysis to a simple diffusion dynamic, allowing a transparent view into the effects of some background parameters and the drivers of a certain optimal behavior. There are many ways in which this line of thinking can be extended to integrate further factors of real-life constraints and objectives into such a study. In particular, it can be interesting to also consider future-biased decision makers (i.e. α>1\alpha>1), and situations where the relationship between emission and profit is more complex than the linear relationship applied in the present study. We leave such extensions to future research.

## References

* Albrecher and Cani, (2017)

  Albrecher, H. and Cani, A. (2017).
  Risk theory with affine dividend payment strategies.
  In Number Theory–Diophantine Problems, Uniform Distribution and
  Applications: Festschrift in Honour of Robert F. Tichy’s 60th Birthday,
  pages 25–60. Springer.
* Albrecher and Thonhauser, (2009)

  Albrecher, H. and Thonhauser, S. (2009).
  Optimality results for dividend problems in insurance.
  Revista de la Real Academia de Ciencias Exactas, Fisicas y
  Naturales, 103(2):295.
* Azcue and Muler, (2014)

  Azcue, P. and Muler, N. (2014).
  Stochastic optimization in insurance: a dynamic programming
  approach.
  Springer.
* Bennedsen et al., (2023)

  Bennedsen, M., Hillebrand, E., and Koopman, S. J. (2023).
  A multivariate dynamic statistical model of the global carbon budget
  1959–2020.
  Journal of the Royal Statistical Society Series A: Statistics in
  Society, 186:20–42.
* Björk et al., (2017)

  Björk, T., Khapko, M., and Murgoci, A. (2017).
  Inconsistent stochastic control in continuous time: Theory and
  examples.
  Finance and Stochastics, 21:331–360.
* Borissov and Bretschger, (2022)

  Borissov, K. and Bretschger, L. (2022).
  Optimal carbon policies in a dynamic heterogeneous world.
  European Economic Review, 148:104253.
* Bourgey et al., (2024)

  Bourgey, F., Gobet, E., and Jiao, Y. (2024).
  Bridging socioeconomic pathways of CO2 emission and credit risk.
  Annals of Operations Research, 336(1):1197–1218.
* Chekriy et al., (2025)

  Chekriy, K., Kiesel, R., and Stahl, G. (2025).
  Probabilistic assessment of corporate net-zero transition.
  Available at SSRN 5255705.
* Chen et al., (2014)

  Chen, S., Li, Z., and Zeng, Y. (2014).
  Optimal dividend strategies with time-inconsistent preferences.
  Journal of Economic Dynamics and Control, 46:150 – 172.
* Chen et al., (2016)

  Chen, S., Wang, X., Deng, Y., and Zeng, Y. (2016).
  Optimal dividend-financing strategies in a dual risk model with
  time-inconsistent preferences.
  Insurance: Mathematics and Economics, 67:27 – 37.
* Colaneri et al., (2024)

  Colaneri, K., Frey, R., and Köck, V. (2024).
  Random carbon tax policy and investment into emission abatement
  technologies.
  arXiv preprint arXiv:2406.01088.
* Eisenberg, (2015)

  Eisenberg, J. (2015).
  Optimal dividends under a stochastic interest rate.
  Insurance: Mathematics and Economics, 65:259–266.
* Frederick et al., (2002)

  Frederick, S., Loewenstein, G., and O’Donoghue, T. (2002).
  Time discounting and time preference: A critical review.
  Journal of Economic Literature, 40(2):351–401.
* Fries and Quante, (2024)

  Fries, C. P. and Quante, L. (2024).
  Intergenerational equitable climate change mitigation: Negative
  effects of stochastic interest rates; positive effects of financing.
  SSRN.
* Gerber and Shiu, (1998)

  Gerber, H. U. and Shiu, E. S. (1998).
  On the time value of ruin.
  North American Actuarial Journal, 2(1):48–72.
* Gikhman and Skorokhod, (1972)

  Gikhman, I. I. and Skorokhod, A. V. (1972).
  Stochastic differential equations.
  Springer-Verlag, New York.
* Global Carbon Project, (2022)

  Global Carbon Project (2022).
  Global carbon budget 2022 highlights.
  <https://www.globalcarbonproject.org/carbonbudget/22/highlights.htm>.
  p. 1. Accessed on 20 June 2025.
* Grenadier and Wang, (2007)

  Grenadier, S. R. and Wang, N. (2007).
  Investment under uncertainty and time-inconsistent preferences.
  Journal of Financial Economics, 84:2–39.
* Harris and Laibson, (2013)

  Harris, C. and Laibson, D. (2013).
  Instantaneous gratification.
  Quarterly Journal of Economics, 128:205–248.
* Hu and Zhou, (2025)

  Hu, S. and Zhou, Z. (2025).
  Equilibrium policy on dividend and capital injection under
  time-inconsistent preferences.
  arXiv preprint arXiv:2505.23511.
* Ikeda and Watanabe, (1977)

  Ikeda, N. and Watanabe, S. (1977).
  A comparison theorem for solutions of stochastic differential
  equations and its applications.
  Osaka Journal of Mathematics, 14(3):619–633.
* Iverson and Karp, (2021)

  Iverson, T. and Karp, L. (2021).
  Carbon taxes and climate commitment with non-constant time
  preference.
  The Review of Economic Studies, 88(2):764–799.
* Korn, (2025)

  Korn, R. (2025).
  A framework for optimal portfolios with sustainable assets and
  climate scenarios.
  European Actuarial Journal, 15(1):1–13.
* Korn and Nurkanovic, (2025)

  Korn, R. and Nurkanovic, A. (2025).
  Sustainable portfolio optimization and sustainable taxation.
  European Actuarial Journal.
  to appear.
* Krylov, (1996)

  Krylov, N. V. (1996).
  Lectures on Elliptic and Parabolic Equations in Holder Spaces.
  The American Mathematical Society.
* Laibson, (1998)

  Laibson, D. (1998).
  Life-cycle consumption and hyperbolic discount functions.
  European Economic Review, 42(3):861 – 871.
* Lebling et al., (2025)

  Lebling, K., Gangotra, A., Hausker, K., and Byrum, Z. (2025).
  7 things to know about carbon capture, utilization and sequestration.
  World Resources Institute.
* Li et al., (2016)

  Li, Y., Li, Z., and Zeng, Y. (2016).
  Equilibrium dividend strategy with non-exponential discounting in a
  dual model.
  Journal of Optimization Theory and Applications,
  168(2):699–722.
* Li et al., (2015)

  Li, Z., Chen, S., and Zeng, Y. (2015).
  Optimal dividend strategy for a diffusion model with
  time-inconsistent preferences.
  Systems Engineering - Theory & Practice, 35(7):1633.
* MacKenzie and Ohndorf, (2012)

  MacKenzie, I. A. and Ohndorf, M. (2012).
  Cap-and-trade, taxes, and distributional conflict.
  Journal of Environmental Economics and Management,
  63(1):51–65.
* Marcolla et al., (2017)

  Marcolla, B., Rödenbeck, C., and Cescatti, A. (2017).
  Patterns and controls of inter-annual variability in the terrestrial
  carbon budget.
  Biogeosciences, 14:3815–3829.
* Maskin and Tirole, (2001)

  Maskin, E. and Tirole, J. (2001).
  Markov perfect equilibrium.
  Journal of Economic Theory, 100:191–219.
* Nordhaus, (2018)

  Nordhaus, W. (2018).
  Evolution of modeling of the economics of global warming: changes in
  the dice model, 1992-2017.
  Climatic Change, 148:623–640.
* Palacios-Huerta and Pèrez-Kakabadse,
  (2011)

  Palacios-Huerta, I. and Pèrez-Kakabadse, A. (2011).
  Consumption and portfolio rules with stochastic quasi-hyperbolic
  discounting.
  Working Paper.
* Pao, (1992)

  Pao, C. V. (1992).
  Nonlinear parabolic and elliptic equations.
  Plenum Press, New York.
* Phelps and Pollak, (1968)

  Phelps, E. S. and Pollak, R. A. (1968).
  On Second-Best National Saving and Game-Equilibrium Growth1.
  The Review of Economic Studies, 35(2):185–199.
* Popovski, (2018)

  Popovski, V. (2018).
  The implementation of the Paris agreement on climate change.
  Routledge.
* Reppen et al., (2020)

  Reppen, A. M., Rochet, J.-C., and Soner, H. M. (2020).
  Optimal dividend policies with random profitability.
  Mathematical Finance, 30(1):228–259.
* Saleh et al., (2025)

  Saleh, H., Battiston, S., Monasterolo, I., Barreau, T., and Tankov, P. (2025).
  Estimating firms’ emissions from asset level data helps revealing
  (mis) alignment to net zero targets.
  Available at SSRN 4661050.
* Schmidli, (2007)

  Schmidli, H. (2007).
  Stochastic control in insurance.
  Springer, Heidelberg.
* Shreve et al., (1984)

  Shreve, S. E., Lehoczky, J. P., and Gaver, D. P. (1984).
  Optimal consumption for general diffusions with absorbing and
  reflecting barriers.
  SIAM Journal of Control and Optimization, 22(1):55–75.
* Stern, (2006)

  Stern, N. (2006).
  The Stern Review: The economics of climate change.
  Technical report, HM Treasury, Government of the United Kingdom,
  London.
* Strini and Thonhauser, (2023)

  Strini, J. A. and Thonhauser, S. (2023).
  Time-inconsistent view on a dividend problem with penalty.
  Scandinavian Actuarial Journal, 2023(8):811–833.
* Strotz, (1956)

  Strotz, R. H. (1956).
  Myopia and inconsistency in dynamic utility maximization.
  The Review of Economic Studies, 23(3):165–180.
* Thonhauser and Albrecher, (2007)

  Thonhauser, S. and Albrecher, H. (2007).
  Dividend maximization under consideration of the time value of ruin.
  Insurance: Mathematics and Economics, 41(1):163–184.
* Zhao et al., (2014)

  Zhao, Q., Wei, J., and Wang, R. (2014).
  On dividend strategies with non-exponential discounting.
  Insurance: Mathematics and Economics, 58:1–13.
* Zhu, (2015)

  Zhu, J. (2015).
  Dividend optimization for general diffusions with restricted dividend
  payment rates.
  Scandinavian Actuarial Journal, 2015(7):592–615.
* Zhu et al., (2020)

  Zhu, J., Siu, T., and Yang, H. (2020).
  Singular dividend optimization for a linear diffusion model with
  time-inconsistent preferences.
  European Journal of Operational Research, 285(1):66–80.

## Appendix A Proofs of Section [3](https://arxiv.org/html/2510.27384v1#S3 "3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")

Proof of Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (i) We begin by proving the existence and uniqueness of a bounded solution that is continuously differentiable on (0,∞)(0,\infty) and twice continuously differentiable on (0,b)∪(b,∞)(0,b)\cup(b,\infty) to Equations ([3.4](https://arxiv.org/html/2510.27384v1#S3.E4 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))-([3.6](https://arxiv.org/html/2510.27384v1#S3.E6 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), through an explicit construction.
Let v1​(⋅)v\_{1}(\cdot) and v2​(⋅)v\_{2}(\cdot) be solutions to the initial value problems as defined in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") and B1​(x)B\_{1}(x) as defined in the same.
The existence and uniqueness of v1v\_{1} and v2v\_{2} are guaranteed by Theorem 5.4.2. of Krylov, ([1996](https://arxiv.org/html/2510.27384v1#bib.bib25)). It is clear that v1v\_{1} and v2v\_{2} are linearly independent. Denote their Wronskian by
Wv1,v2​(x)=v1​(x)​v2′​(x)−v2​(x)​v1′​(x).W\_{v\_{1},v\_{2}}(x)=v\_{1}(x)v\_{2}^{\prime}(x)-v\_{2}(x)v\_{1}^{\prime}(x). Then, B1​(x)B\_{1}(x) can be expressed as
B1​(x)=v1​(x)​∫0xv2​(y)Wv1,v2​(y)​2​Λσ2​(y)​dy−v2​(x)​∫0xv1​(y)Wv1,v2​(y)​2​Λσ2​(y)​dy,B\_{1}(x)=v\_{1}(x)\int\_{0}^{x}\frac{v\_{2}(y)}{W\_{v\_{1},v\_{2}}(y)}\frac{2\Lambda}{\sigma^{2}(y)}\,\mathrm{d}y-v\_{2}(x)\int\_{0}^{x}\frac{v\_{1}(y)}{W\_{v\_{1},v\_{2}}(y)}\frac{2\Lambda}{\sigma^{2}(y)}\,\mathrm{d}y, which implies that B1​(x)B\_{1}(x) is a particular solution to the differential equation σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)+Λ=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)+\Lambda=0 with initial value conditions B1​(0)=0B\_{1}(0)=0 and B1′​(0)=0B\_{1}^{\prime}(0)=0.
Let uu and v3v\_{3} be defined as in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"). The existence of v3v\_{3} and uu can be established by extending the differential equation to the domain (−∞,−1)∪(0,∞)(-\infty,-1)\cup(0,\infty), imposing the boundary condition g​(−1)=1g(-1)=1, and applying Corollary 8.1 of Pao, ([1992](https://arxiv.org/html/2510.27384v1#bib.bib35)).

Recall that v1v\_{1} and v2v\_{2} form a pair of independent solutions to σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−δ​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-\delta g(x)=0 on [0,∞)[0,\infty).
Then all the solutions to ([3.4](https://arxiv.org/html/2510.27384v1#S3.E4 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) can be expressed in the following general form: C1​v1​(x)+C2​v2​(x)+B1​(x)C\_{1}\,v\_{1}(x)+C\_{2}v\_{2}(x)+B\_{1}(x) where C1C\_{1} and C2C\_{2} are constants.
Recall v3​(⋅)v\_{3}(\cdot) and u​(⋅)u(\cdot) are both bounded solutions to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−δ​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-\delta g(x)=0 on (0,∞)(0,\infty).
Then, for any constant C3C\_{3}, the function C3​v3​(x)+u​(x)C\_{3}v\_{3}(x)+u(x) is a solution to ([3.5](https://arxiv.org/html/2510.27384v1#S3.E5 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). For b≥0b\geq 0, define a new function

|  |  |  |  |
| --- | --- | --- | --- |
|  | gb​(x)={C1​(b)​v1​(x)+C2​(b)​v2​(x)+B1​(x)0≤x<b,C3​(b)​v3​(x)+u​(x)x≥b,\displaystyle g\_{b}(x)=\left\{\begin{array}[]{ll}C\_{1}\,(b)v\_{1}(x)+C\_{2}(b)v\_{2}(x)+B\_{1}(x)&0\leq x<b,\\ C\_{3}(b)v\_{3}(x)+u(x)&x\geq b,\end{array}\right. |  | (A.3) |

where C1​(b)C\_{1}\,(b) and C3​(b)C\_{3}(b) are constants (depending on bb only) that satisfy the following:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | gb​(0)=0, i.e.,\displaystyle g\_{b}(0)=0,\mbox{ i.e.,} | C1​(b)​v1​(0)+C2​(b)​v2​(0)+B1​(0)=0\displaystyle C\_{1}\,(b)v\_{1}(0)+C\_{2}(b)v\_{2}(0)+B\_{1}(0)=0 |  | (A.4) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | gb​(b−)=gb​(b+), i.e.,\displaystyle g\_{b}(b-)=g\_{b}(b+),\mbox{ i.e.,} | C1​(b)​v1​(b)+C2​(b)​v2​(b)+B1​(b)=C3​(b)​v3​(b)+u​(b),b>0,\displaystyle C\_{1}\,(b)v\_{1}(b)+C\_{2}(b)v\_{2}(b)+B\_{1}(b)=C\_{3}(b)v\_{3}(b)+u(b),\ \ b>0, |  | (A.5) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | gb′​(b−)=gb′​(b+), i.e.,\displaystyle g\_{b}^{\prime}(b-)=g\_{b}^{\prime}(b+),\mbox{ i.e.,} | C1​(b)​v1′​(b)+C2​(b)​v2′​(b)+B1′​(b)=C3​(b)​v3′​(b)+u′​(b),b>0.\displaystyle C\_{1}\,(b)v\_{1}^{\prime}(b)+C\_{2}(b)v\_{2}^{\prime}(b)+B\_{1}^{\prime}(b)=C\_{3}(b)v\_{3}^{\prime}(b)+u^{\prime}(b),\ b>0. |  | (A.6) |

We can see that C1​(b)C\_{1}\,(b), C2​(b)C\_{2}(b) and C3​(b)C\_{3}(b) can be uniquely determined with C2​(b)=−C1​(b)C\_{2}(b)=-C\_{1}(b). Taking limb↓0\lim\_{b\downarrow 0} on both sides of ([A.5](https://arxiv.org/html/2510.27384v1#A1.E5 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), using v1​(0)=v2​(0)=v3​(0)=1v\_{1}(0)=v\_{2}(0)=v\_{3}(0)=1 and u​(0)=0u(0)=0, and noting B1​(0)=0B\_{1}(0)=0, we obtain limb↓0C3​(b)=0=C3​(0)\lim\_{b\downarrow 0}C\_{3}(b)=0=C\_{3}(0). The function gb​(x)g\_{b}(x) satisfies ([3.4](https://arxiv.org/html/2510.27384v1#S3.E4 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([3.5](https://arxiv.org/html/2510.27384v1#S3.E5 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and is bounded due to the boundedness of v3​(x)v\_{3}(x) and u​(x)u(x). From the structure of gbg\_{b} and noting ([A.4](https://arxiv.org/html/2510.27384v1#A1.E4 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))-([A.6](https://arxiv.org/html/2510.27384v1#A1.E6 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and C3​(0)=0C\_{3}(0)=0, we can find that gb​(0)=0g\_{b}(0)=0, and that when b>0b>0, gb​(b−)=gb​(b+)g\_{b}(b-)=g\_{b}(b+) and gb​(x)g\_{b}(x) is continuously differentiable in [0,∞)[0,\infty). We can also see that gb​(x)g\_{b}(x) is twice continuously differentiable except for x=bx=b. So gb​(x)g\_{b}(x) is the desired unique solution.
Since v1v\_{1}, v2v\_{2}, v3v\_{3} and uu are continuously differentiable functions, from ([A.4](https://arxiv.org/html/2510.27384v1#A1.E4 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) - ([A.6](https://arxiv.org/html/2510.27384v1#A1.E6 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) we can observe that C1​(b)C\_{1}\,(b), C2​(b)C\_{2}(b) and C3​(b)C\_{3}(b) are continuous functions.

(ii) We now proceed to prove that the above solution is unique and coincides with VbE​(x)V\_{b}^{E}(x). Let gg be any bounded solution that meets all the requirements in (i).
It follows by (Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Lemma A.1) that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼x​[e−δ​(τb∧τn∧t)​g​(Xτb∧τn∧tb)]\displaystyle{\mathbb{E}}\_{x}\left[e^{-\delta(\tau^{b}\wedge\tau\_{n}\wedge t)}g(X^{b}\_{\tau^{b}\wedge\tau\_{n}\wedge t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | g​(x)+𝔼x​[∫0τb∧τn∧te−δ​s​(12​σ2​(Xsb)​g′′​(Xsb)+(μ​(Xsb)−lsb)​g′​(Xsb)−δ​g​(Xsb))​ds],\displaystyle g(x)+{\mathbb{E}}\_{x}\left[\int^{\tau^{b}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}\left(\frac{1}{2}\sigma^{2}(X^{b}\_{s})g^{\prime\prime}(X^{b}\_{s})+(\mu(X^{b}\_{s})-l\_{s}^{b})g^{\prime}(X^{b}\_{s})-\delta g(X^{b}\_{s})\right)\,\mathrm{d}s\right], |  |

where {τn}\{\tau\_{n}\} is a sequence of stopping times converging to ∞\infty.
Note that lsb=l¯​I​{Xsb≥b}l\_{s}^{b}=\bar{l}I\{X^{b}\_{s}\geq b\} and that gg satisfies ([3.4](https://arxiv.org/html/2510.27384v1#S3.E4 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([3.5](https://arxiv.org/html/2510.27384v1#S3.E5 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and so we have

|  |  |  |
| --- | --- | --- |
|  | 12​σ2​(Xsb)​g′′​(Xsb)+(μ​(Xsb)−lsb)​g′​(Xsb)−δ​g​(Xsb)=−Λ−l¯​(γ−β)​I​{Xsb≥b}.\displaystyle\frac{1}{2}\sigma^{2}(X^{b}\_{s})g^{\prime\prime}(X^{b}\_{s})+(\mu(X^{b}\_{s})-l\_{s}^{b})g^{\prime}(X^{b}\_{s})-\delta g(X^{b}\_{s})=-\Lambda-\bar{l}(\gamma-\beta)I\{X^{b}\_{s}\geq b\}. |  |

Consequently,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(x)=\displaystyle g(x)= | 𝔼x​[e−δ​(τb∧τn∧t)​g​(Xτb∧τn∧tb)]+𝔼x​[∫0τb∧τn∧t(Λ+l¯​(γ−β)​I​{Xsb≥b})​ds],x≥0.\displaystyle{\mathbb{E}}\_{x}\left[e^{-\delta(\tau^{b}\wedge\tau\_{n}\wedge t)}g(X^{b}\_{\tau^{b}\wedge\tau\_{n}\wedge t})\right]+{\mathbb{E}}\_{x}\left[\int\_{0}^{\tau^{b}\wedge\tau\_{n}\wedge t}(\Lambda+\bar{l}(\gamma-\beta)I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s\right],\ \ x\geq 0. |  | (A.7) |

Since the function g​(⋅)g(\cdot) is bounded, using the dominated convergence twice we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞limn→∞𝔼x​[e−δ​(τb∧τn∧t)​g​(Xτb∧τn∧tb)]=𝔼x​[e−δ​τb​g​(Xτbb)]=0,\displaystyle\lim\_{t\rightarrow\infty}\lim\_{n\rightarrow\infty}{\mathbb{E}}\_{x}\left[e^{-\delta(\tau^{b}\wedge\tau\_{n}\wedge t)}g(X^{b}\_{\tau^{b}\wedge\tau\_{n}\wedge t})\right]={\mathbb{E}}\_{x}\left[e^{-\delta\tau^{b}}g(X^{b}\_{\tau^{b}})\right]=0, |  | (A.8) |

where the last equality follows by noticing Xτbb=0X^{b}\_{\tau^{b}}=0 and g​(0)=0g(0)=0.
By using the monotone convergence twice we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limt→∞limn→∞𝔼x​[∫0τb∧τn∧te−δ​s​(Λ+l¯​I​{Xsb≥b})​ds]=𝔼x​[∫0τbe−δ​s​(Λ+(γ−β)​l¯​I​{Xsb≥b})​ds]\displaystyle\lim\_{t\rightarrow\infty}\lim\_{n\rightarrow\infty}{\mathbb{E}}\_{x}\left[\int^{\tau^{b}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}(\Lambda+\bar{l}I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s\right]={\mathbb{E}}\_{x}\left[\int^{\tau^{b}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l}I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼x​[∫0τbe−δ​s​(γ−β)​lsb​ds+∫0τbe−δ​s​Λ​ds]=VbE​(x).\displaystyle{\mathbb{E}}\_{x}\left[\int^{\tau^{b}}\_{0}e^{-\delta s}(\gamma-\beta)l^{b}\_{s}\,\mathrm{d}s+\int^{\tau^{b}}\_{0}e^{-\delta s}\Lambda\,\mathrm{d}s\right]=V\_{b}^{E}(x). |  | (A.9) |

By letting t→∞t\rightarrow\infty and n→∞n\rightarrow\infty on both sides of ([A.7](https://arxiv.org/html/2510.27384v1#A1.E7 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and then using ([A.8](https://arxiv.org/html/2510.27384v1#A1.E8 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([A.9](https://arxiv.org/html/2510.27384v1#A1.E9 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we can obtain
g​(x)=VbE​(x)g(x)=V\_{b}^{E}(x) for x≥0x\geq 0.

(iii)
It follows immediately from the above derivations that

|  |  |  |
| --- | --- | --- |
|  | VbE​(x)={C1​(b)​v1​(x)−C1​(b)​v2​(x)+B1​(x)0≤x<b,C3​(b)​v3​(x)+u​(x)x≥b,\displaystyle V\_{b}^{E}(x)=\left\{\begin{array}[]{ll}C\_{1}\,(b)v\_{1}(x)-C\_{1}\,(b)v\_{2}(x)+B\_{1}(x)&0\leq x<b,\\ C\_{3}(b)v\_{3}(x)+u(x)&x\geq b,\end{array}\right. |  |

where C1​(b)C\_{1}\,(b) and C3​(b)C\_{3}(b) are determined by solving ([A.4](https://arxiv.org/html/2510.27384v1#A1.E4 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))-([A.6](https://arxiv.org/html/2510.27384v1#A1.E6 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). □\square

Proof of Lemma [3.2](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem2 "Lemma 3.2 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")
The non-negativity of VE​(x)V^{E}(x) is obvious from its definition in ([2.7](https://arxiv.org/html/2510.27384v1#S2.E7 "In 2.1 Exponential discounting ‣ 2 Problem Formulation ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
By noting that the excess emission rate for any admissible strategy is bounded by l¯\bar{l}, it follows that
  
VE​(x)=supL∈Π𝔼​[∫0τLe−δ​s​((γ−β)​ls+Λ)​ds|X0=x]≤∫0∞e−δ​s​((γ−β)​l¯+Λ)​ds=(γ−β)​l¯+ΛδV^{E}(x)=\sup\_{L\in\Pi}{\mathbb{E}}\left[\int\_{0}^{\tau^{L}}e^{-\delta s}((\gamma-\beta)l\_{s}+\Lambda)\,\mathrm{d}s|X\_{0}=x\right]\leq\int\_{0}^{\infty}e^{-\delta s}((\gamma-\beta)\bar{l}+\Lambda)\,\mathrm{d}s=\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}.

For any x>0x>0, let Xtx,bX\_{t}^{x,b} represent the controlled stochastic process d​Xtx,b=(μ​(Xtx,b)−l¯​I​{Xtx,b≥b})​d​t+σ​(Xt−x,b)​d​Wt\,\mathrm{d}X\_{t}^{x,b}=(\mu(X\_{t}^{x,b})-\bar{l}I\{X\_{t}^{x,b}\geq b\})\,\mathrm{d}t+\sigma(X\_{t-}^{x,b})\,\mathrm{d}W\_{t} with X0−x,b=xX\_{0-}^{x,b}=x. By adapting the comparison theorem (Theorem 1.1 in Ikeda and Watanabe, ([1977](https://arxiv.org/html/2510.27384v1#bib.bib21))), we can show that
with probability 11, Xtx+h,b≥Xtx,bX\_{t}^{x+h,b}\geq X\_{t}^{x,b} for all t≥0t\geq 0. This, along with the fact that, under LbL^{b}, excess emissions only occur when the controlled stochastic process is above bb, implies that when there are excess emissions (at rate l¯\bar{l}) at time tt under the process Xtx+h,bX\_{t}^{x+h,b}, there may or may not be excess emissions under Xtx,bX\_{t}^{x,b}. However, when there are excess emissions at time tt under Xtx,bX\_{t}^{x,b}, there will also be excess emissions at the same rate l¯\bar{l} under Xtx+h,bX\_{t}^{x+h,b} with probability 1.
As a result,
VbE​(x)≤VbE​(x+h)V\_{b}^{E}(x)\leq V\_{b}^{E}(x+h) for h>0h>0, and so VbE​(x)V\_{b}^{E}(x) is non-decreasing.
□\square

###### Lemma A.1

The function hE​(b):=VbE′​(b)h^{E}(b):={V\_{b}^{E}}^{\prime}(b) is continuous on [0,∞)[0,\infty) and the following holds: limb↓0VbE′′​(0+)=V0E′′​(0+)\lim\_{b\downarrow 0}{V\_{b}^{E}}^{\prime\prime}(0+)={V\_{0}^{E}}^{\prime\prime}(0+).

Proof.  From the proof of Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (i) and (ii) we know that VbE​(x)=gb​(x)V\_{b}^{E}(x)=g\_{b}(x) for x≥0x\geq 0 and b≥0b\geq 0. As mentioned there, C1​(b)C\_{1}\,(b) and C3​(b)C\_{3}(b) are continuous functions of bb for b≥0b\geq 0.
Consequently, the function hE​(b):=VbE′​(b)=gb′​(b)=C3​(b)​v3′​(b)+u′​(b)h^{E}(b):={V\_{b}^{E}}^{\prime}(b)=g\_{b}^{\prime}(b)=C\_{3}(b)v\_{3}^{\prime}(b)+u^{\prime}(b) is continuous in bb for b∈[0,∞)b\in[0,\infty).
It follows by ([A.3](https://arxiv.org/html/2510.27384v1#A1.E3 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limb↓0VbE′′​(0+)\displaystyle\lim\_{b\downarrow 0}{V\_{b}^{E}}^{\prime\prime}(0+) | =limb↓0gb′′​(0+)=limb↓0C1​(b)​(v1′′​(0)−v2′′​(0))=limb↓0(C1​(b)​(v1′′​(b)−v2′′​(b)))\displaystyle=\lim\_{b\downarrow 0}g\_{b}^{\prime\prime}(0+)=\lim\_{b\downarrow 0}C\_{1}\,(b)(v\_{1}^{\prime\prime}(0)-v\_{2}^{\prime\prime}(0))=\lim\_{b\downarrow 0}\left(C\_{1}\,(b)(v\_{1}^{\prime\prime}(b)-v\_{2}^{\prime\prime}(b))\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =limb↓0(C3​(b)​v3′′​(b)+u′′​(b))=limb↓0C3​(b)​v3′′​(0)+u′′​(0)\displaystyle=\lim\_{b\downarrow 0}\left(C\_{3}(b)v\_{3}^{\prime\prime}(b)+u^{\prime\prime}(b)\right)=\lim\_{b\downarrow 0}C\_{3}(b)v\_{3}^{\prime\prime}(0)+u^{\prime\prime}(0) |  | (A.11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C3​(0)​v3′′​(0)+u′′​(0)=V0E′′​(0+),\displaystyle=C\_{3}(0)v\_{3}^{\prime\prime}(0)+u^{\prime\prime}(0)={V\_{0}^{E}}^{\prime\prime}(0+), |  |

where the first equality in ([A.11](https://arxiv.org/html/2510.27384v1#A1.E11 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) is due to ([A.6](https://arxiv.org/html/2510.27384v1#A1.E6 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
□\square

###### Lemma A.2

(i) For b≥0b\geq 0, VbE′′​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)\leq 0 for x∈(b,∞)x\in(b,\infty).
(ii) For b≥0b\geq 0, if VbE′​(b)≥γ−β{V\_{b}^{E}}^{\prime}(b)\geq\gamma-\beta, then VbE′′​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)\leq 0 for x∈(0,b)x\in(0,b).
(iii) For b≥0b\geq 0, if μ​(0)<0\mu(0)<0 and C1​(b)>Λ−2​μ​(0)C\_{1}\,(b)>\frac{\Lambda}{-2\mu(0)}, then VbE′​(b)<γ−β{V\_{b}^{E}}^{\prime}(b)<\gamma-\beta and furthermore, VbE′​(x)<γ−β{V\_{b}^{E}}^{\prime}(x)<\gamma-\beta for x>bx>b. (iv) Moreover,
C1​(b)≥0​ for b≥0.C\_{1}\,(b)\geq 0\mbox{\ for $b\geq 0$}.

Proof.  (i) We proceed with an indirect proof. Suppose the statement in (i) is not true. Then VbE′′​(y0)>0{V\_{b}^{E}}^{\prime\prime}(y\_{0})>0 for some y0>by\_{0}>b. Since VbEV\_{b}^{E} is bounded and increasing, eventually VbE′′​(x)<0{V\_{b}^{E}}^{\prime\prime}(x)<0 for sufficiently large xx. Let y1y\_{1} represent the first point after y0y\_{0} such that the function, VbE′′​(x){V\_{b}^{E}}^{\prime\prime}(x), becomes concave. Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE′′​(y1)=0, and ​VbE′′​(x)>0​ for x∈(y0,y1).\displaystyle{V\_{b}^{E}}^{\prime\prime}(y\_{1})=0,\ \mbox{ and }{V\_{b}^{E}}^{\prime\prime}(x)>0\mbox{ for $x\in(y\_{0},y\_{1})$.} |  | (A.12) |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(x)​VbE′​(x)−δ​VbE​(x)+l¯​((γ−β)−VbE′​(x))+Λ=−σ2​(x)2​VbE′′​(x)<0​ for x∈(y0,y1),\displaystyle\mu(x){V\_{b}^{E}}^{\prime}(x)-\delta{V\_{b}^{E}}(x)+\bar{l}((\gamma-\beta)-{V\_{b}^{E}}^{\prime}(x))+\Lambda=-\frac{\sigma^{2}(x)}{2}{V\_{b}^{E}}^{\prime\prime}(x)<0\ \mbox{ for $x\in(y\_{0},y\_{1})$}, |  | (A.13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(y1)​VbE′​(y1)−δ​VbE​(y1)+l¯​((γ−β)−VbE′​(y1))+Λ=−σ2​(y1)2​VbE′′​(y1)=0.\displaystyle\mu(y\_{1}){V\_{b}^{E}}^{\prime}(y\_{1})-\delta{V\_{b}^{E}}(y\_{1})+\bar{l}((\gamma-\beta)-{V\_{b}^{E}}^{\prime}(y\_{1}))+\Lambda=-\frac{\sigma^{2}(y\_{1})}{2}{V\_{b}^{E}}^{\prime\prime}(y\_{1})=0. |  | (A.14) |

Also, (μ​(y1)​VbE′​(y1)−μ​(x)​VbE′​(x))−δ​(VbE​(y1)−VbE​(x))−l¯​(VbE′​(y1)−VbE′​(x))>0(\mu(y\_{1}){V\_{b}^{E}}^{\prime}(y\_{1})-\mu(x){V\_{b}^{E}}^{\prime}(x))-\delta({V\_{b}^{E}}(y\_{1})-{V\_{b}^{E}}(x))-\bar{l}({V\_{b}^{E}}^{\prime}(y\_{1})-{V\_{b}^{E}}^{\prime}(x))>0 for x∈(y0,y1)x\in(y\_{0},y\_{1}). As a result, by dividing both sides by y1−xy\_{1}-x, then taking the limit limx↑y1\lim\_{x\uparrow y\_{1}} and using VbE′′​(y1)=0{V\_{b}^{E}}^{\prime\prime}(y\_{1})=0 we obtain (μ′​(y1)−δ)​VbE′​(y1)≥0(\mu^{\prime}(y\_{1})-\delta){V\_{b}^{E}}^{\prime}(y\_{1})\geq 0. On the other hand, since μ′​(y1)<δ\mu^{\prime}(y\_{1})<\delta and VbE′​(y1)>0{V\_{b}^{E}}^{\prime}(y\_{1})>0 (by the increasing property of VbEV\_{b}^{E} and ([A.12](https://arxiv.org/html/2510.27384v1#A1.E12 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))), we have (μ′​(y1)−δ)​VbE′​(y1)<0(\mu^{\prime}(y\_{1})-\delta){V\_{b}^{E}}^{\prime}(y\_{1})<0, which is a contradiction.

(ii) Recall from Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we know that VbEV\_{b}^{E} satisfies ([3.4](https://arxiv.org/html/2510.27384v1#S3.E4 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE′′​(b−)\displaystyle{V\_{b}^{E}}^{\prime\prime}(b-) | =−2​(μ​(b)​VbE′​(b)−δ​VbE​(b)+Λ)σ2​(b)\displaystyle=-\frac{2(\mu(b){V\_{b}^{E}}^{\prime}(b)-\delta{V\_{b}^{E}}(b)+\Lambda)}{\sigma^{2}(b)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2(μ(b)VbE′(b)−δVbE(b)+l¯((γ−β)−VbE′(b))+Λ−l¯((γ−β)−VbE′(b))σ2​(b)\displaystyle=-\frac{2(\mu(b){V\_{b}^{E}}^{\prime}(b)-\delta{V\_{b}^{E}}(b)+\bar{l}((\gamma-\beta)-{V\_{b}^{E}}^{\prime}(b))+\Lambda-\bar{l}((\gamma-\beta)-{V\_{b}^{E}}^{\prime}(b))}{\sigma^{2}(b)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =VbE′′​(b+)+2​l¯​((γ−β)−VbE′​(b))σ2​(b)≤VbE′′​(b+)≤0,\displaystyle={V\_{b}^{E}}^{\prime\prime}(b+)+\frac{2\bar{l}((\gamma-\beta)-{V\_{b}^{E}}^{\prime}(b))}{\sigma^{2}(b)}\leq{V\_{b}^{E}}^{\prime\prime}(b+)\leq 0, |  | (A.15) |

where the second to the last inequality follows by noting VbE′​(b)≥γ−β{V\_{b}^{E}}^{\prime}(b)\geq\gamma-\beta and the last equality follows by the result in (i).
  
We use proof by contradiction again. Suppose there exists some y0∈(0,b)y\_{0}\in(0,b) such that VbE′′​(y0)>0{V\_{b}^{E}}^{\prime\prime}(y\_{0})>0. By noting VbE′′​(b−)≤0{V\_{b}^{E}}^{\prime\prime}(b-)\leq 0 (([A.15](https://arxiv.org/html/2510.27384v1#A1.E15 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))) and the continuity of VbE′′​(x){V\_{b}^{E}}^{\prime\prime}(x) on (0,b)(0,b), we know there exists a y1∈(y0,b)y\_{1}\in(y\_{0},b) such that VbE′′​(y1)=0{V\_{b}^{E}}^{\prime\prime}(y\_{1})=0 and VbE′′​(x)>0{V\_{b}^{E}}^{\prime\prime}(x)>0 for x∈(y0,y1)x\in(y\_{0},y\_{1}).
Following the same lines starting from ([A.13](https://arxiv.org/html/2510.27384v1#A1.E13 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) until the end of proof for (i) we can obtain a contradiction.

(iii) We now consider the situation where μ​(0)<0\mu(0)<0, and C1​(b)>Λ−2​μ​(0)C\_{1}\,(b)>\frac{\Lambda}{-2\mu(0)}. By using the expression for VbEV\_{b}^{E} in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we can obtain VbE′​(0+)=2​C1​(b)>Λ−μ​(0){V\_{b}^{E}}^{\prime}(0+)=2C\_{1}\,(b)>\frac{\Lambda}{-\mu(0)}.
Suppose the statement is not true, that is, VbE′​(b)≥γ−β{V\_{b}^{E}}^{\prime}(b)\geq\gamma-\beta. Then it follows by (ii) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE′′​(0+)≤0.\displaystyle{V\_{b}^{E}}^{\prime\prime}(0+)\leq 0. |  | (A.16) |

On the other hand, however,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −σ2​(0)2​VbE′′​(0+)\displaystyle-\frac{\sigma^{2}(0)}{2}{V\_{b}^{E}}^{\prime\prime}(0+) | =μ​(0)​VbE′​(0+)−δ​VbE​(0)+Λ=μ​(0)​VbE′​(0+)+Λ\displaystyle=\mu(0){V\_{b}^{E}}^{\prime}(0+)-\delta{V\_{b}^{E}}(0)+\Lambda=\mu(0){V\_{b}^{E}}^{\prime}(0+)+\Lambda |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <μ​(0)​Λ−μ​(0)+Λ=0,\displaystyle<\mu(0)\frac{\Lambda}{-\mu(0)}+\Lambda=0, |  | (A.17) |

where the last inequality follows by noting μ​(0)<0\mu(0)<0, and VbE′​(0+)>Λ−μ​(0){V\_{b}^{E}}^{\prime}(0+)>\frac{\Lambda}{-\mu(0)}. The inequality ([A.17](https://arxiv.org/html/2510.27384v1#A1.E17 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) implies that VbE′′​(0+)>0{V\_{b}^{E}}^{\prime\prime}(0+)>0, which is a contradiction to ([A.16](https://arxiv.org/html/2510.27384v1#A1.E16 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). Hence, VbE′​(b)<γ−β{V\_{b}^{E}}^{\prime}(b)<\gamma-\beta.
From (i) we know VbE′′​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)\leq 0 for x>bx>b. Therefore, Hence, VbE′​(x)≤VbE′​(b)<γ−β{V\_{b}^{E}}^{\prime}(x)\leq{V\_{b}^{E}}^{\prime}(b)<\gamma-\beta.

(iv) By using the expression for VbEV\_{b}^{E} in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we can obtain VbE′​(0+)=2​C1​(b){V\_{b}^{E}}^{\prime}(0+)=2C\_{1}\,(b). Further note from Lemma [3.2](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem2 "Lemma 3.2 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that VbE′​(0+)≥0{V\_{b}^{E}}^{\prime}(0+)\geq 0. From this we can conclude C1​(b)≥0C\_{1}\,(b)\geq 0, which completes the proof.
□\square

The following is an immediate consequence of Lemma [A.2](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem2 "Lemma A.2 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target").

###### Corollary A.3

If 0<bE∗<∞0<b^{\*}\_{E}<\infty, then VbE∗E′​(bE∗)=γ−β{V\_{b^{\*}\_{E}}^{E}}^{\prime}(b^{\*}\_{E})=\gamma-\beta, VbE∗E′′​(x)≤0{V\_{b^{\*}\_{E}}^{E}}^{\prime\prime}(x)\leq 0 for x≥0x\geq 0, VbE∗E′​(x)≥γ−β{V\_{b^{\*}\_{E}}^{E}}^{\prime}(x)\geq\gamma-\beta for 0≤x<bE∗0\leq x<b^{\*}\_{E} and VbE∗E′​(x)≤γ−β{V\_{b^{\*}\_{E}}^{E}}^{\prime}(x)\leq\gamma-\beta for x≥bE∗x\geq b^{\*}\_{E}. If bE∗=∞b^{\*}\_{E}=\infty, then for any b≥0b\geq 0, VbE′​(b)>γ−β{V\_{b}^{E}}^{\prime}(b)>\gamma-\beta and VbE′′​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)\leq 0 for x∈[0,b)x\in[0,b).

###### Lemma A.4

If bE∗=0b\_{E}^{\*}=0, then VbE∗E′​(x)≤γ−β{V\_{b^{\*}\_{E}}^{E}}^{\prime}(x)\leq\gamma-\beta for x≥0x\geq 0.

Proof.  From ([3.14](https://arxiv.org/html/2510.27384v1#S3.E14 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) we know that if bE∗=0b\_{E}^{\*}=0, V0E′​(0)≤γ−β{V\_{0}^{E}}^{\prime}(0)\leq\gamma-\beta. Since from Lemma [A.2](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem2 "Lemma A.2 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (i) we know V0E′′​(x)≤0{V\_{0}^{E}}^{\prime\prime}(x)\leq 0 for x>0x>0, we can obtain
VbE∗E′​(x)=V0E′​(x)≤V0E′​(0)≤γ−β{V\_{b^{\*}\_{E}}^{E}}^{\prime}(x)={V\_{0}^{E}}^{\prime}(x)\leq{V\_{0}^{E}}^{\prime}(0)\leq\gamma-\beta for x≥0x\geq 0.
□\square

Proof of Theorem [3.3](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem3 "Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") 
(i) We first use proof by contradiction to show bE∗<∞b\_{E}^{\*}<\infty.
Suppose bE∗=∞b\_{E}^{\*}=\infty. Then, from ([3.14](https://arxiv.org/html/2510.27384v1#S3.E14 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) we have
VbE′​(b)>γ−β{V\_{b}^{E}}^{\prime}(b)>\gamma-\beta for all b>0b>0, and thus by Lemma [A.2](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem2 "Lemma A.2 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")(ii) we can obtain VbE′′​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)\leq 0 for 0<x<b0<x<b and all b≥0b\geq 0. This implies VbE′​(x)≥VbE′​(b)>γ−β{V\_{b}^{E}}^{\prime}(x)\geq{V\_{b}^{E}}^{\prime}(b)>\gamma-\beta for all b>0b>0 and 0<x<b0<x<b. As a result, for all b≥0b\geq 0, VbE​(x)≥(γ−β)​xV\_{b}^{E}(x)\geq(\gamma-\beta)x for 0≤x≤b0\leq x\leq b. Thus, for any x≥0x\geq 0, lim supb↑∞VbE​(x)≥(γ−β)​x\limsup\_{b\uparrow\infty}V\_{b}^{E}(x)\geq(\gamma-\beta)x. However, according to Lemma [3.2](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem2 "Lemma 3.2 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we know VbE​(x)≤supL∈ΠVLE​(x)=VE​(x)≤(γ−β)​l¯+ΛδV\_{b}^{E}(x)\leq\sup\_{L\in\Pi}V^{E}\_{L}(x)=V^{E}(x)\leq\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}. This is a contradiction and completes the proof.

(ii) We now consider the case μ​(0)<0\mu(0)<0 and proceed to prove bE∗≤b0b\_{E}^{\*}\leq b\_{0}. If b0=∞b\_{0}=\infty, then this is obviously true. So we only need to consider the case b0<∞b\_{0}<\infty. Recall the definition b0=inf{b≥0:C1​(b)+Λ2​μ​(0)>0}b\_{0}=\inf\{b\geq 0:C\_{1}\,(b)+\frac{\Lambda}{2\mu(0)}>0\}.
Then C1​(b)≤−Λ2​μ​(0)C\_{1}\,(b)\leq-\frac{\Lambda}{2\mu(0)} for 0≤b≤b00\leq b\leq b\_{0},
C1​(b0)=−Λ2​μ​(0)C\_{1}\,(b\_{0})=-\frac{\Lambda}{2\mu(0)} and there exists a sequence bn↓b0b\_{n}\downarrow b\_{0} such that
C1​(bn)>−Λ2​μ​(0).C\_{1}\,(b\_{n})>-\frac{\Lambda}{2\mu(0)}.
It then follows from Lemma [A.2](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem2 "Lemma A.2 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (iii)) that VbnE′​(bn)<γ−β{V\_{b\_{n}}^{E}}^{\prime}(b\_{n})<\gamma-\beta.
Note that VbE{V\_{b}^{E}} is continuously differentiable, and VbE′​(b)=C3​(b)​VE′​(b)+u′​(b){V\_{b}^{E}}^{\prime}(b)=C\_{3}(b)V\_{E}^{\prime}(b)+u^{\prime}(b). Hence,
C3​(bn)​VbnE′​(bn)+u′​(bn)<γ−βC\_{3}(b\_{n}){V^{E}\_{b\_{n}}}^{\prime}(b\_{n})+u^{\prime}(b\_{n})<\gamma-\beta for all n≥1n\geq 1.
This combined with the definition for b∗b^{\*} (see ([3.14](https://arxiv.org/html/2510.27384v1#S3.E14 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))), bE∗=inf{b>0:C3​(b)​v3′​(b)+u′​(b)≤γ−β}b^{\*}\_{E}=\inf\{b>0:C\_{3}(b)v\_{3}^{\prime}(b)+u^{\prime}(b)\leq\gamma-\beta\}, and the fact that bn↓b0b\_{n}\downarrow b\_{0} implies bE∗≤b0b^{\*}\_{E}\leq b\_{0}.

(iii) Note we have already shown in (i) that bE∗b\_{E}^{\*} is finite, and in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that VbE∗EV^{E}\_{b^{\*}\_{E}} is continuously differentiable on [0,∞)[0,\infty) and twice continuously differentiable on (0,∞)(0,\infty). From (Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Lemma A.1) with gg there being set to VbE∗EV^{E}\_{b^{\*}\_{E}}, we obtain that for any L∈πL\in\pi and some positive sequence {τn}\{\tau\_{n}\} increasing to ∞\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼x​[e−δ​(τL∧τn∧t)​VbE∗E​(XτL∧τn∧tL)]\displaystyle{\mathbb{E}}\_{x}\left[e^{-\delta(\tau^{L}\wedge\tau\_{n}\wedge t)}V^{E}\_{b^{\*}\_{E}}(X^{L}\_{\tau^{L}\wedge\tau\_{n}\wedge t})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | VbE∗E​(x)+𝔼x​[∫0τL∧τn∧te−δ​s​(12​σ2​(XsL)​VbE∗E′′​(XsL)+(μ​(XsL)−ls)​VbE∗E′​(XsL)−δ​VbE∗E​(XsL))​ds].\displaystyle V^{E}\_{b^{\*}\_{E}}(x)+{\mathbb{E}}\_{x}\left[\int^{\tau^{L}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}\left(\frac{1}{2}\sigma^{2}(X^{L}\_{s}){V^{E}\_{b^{\*}\_{E}}}^{\prime\prime}(X^{L}\_{s})+(\mu(X^{L}\_{s})-{l\_{s}}){V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})-\delta V^{E}\_{b^{\*}\_{E}}(X^{L}\_{s})\right)\,\mathrm{d}s\right]. |  | (A.18) |

Since VbE∗E​(x)V^{E}\_{b^{\*}\_{E}}(x) is a solution to ([3.4](https://arxiv.org/html/2510.27384v1#S3.E4 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([3.5](https://arxiv.org/html/2510.27384v1#S3.E5 "In Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | σ2(XsL2)VEbE∗′′(XsL)+(μ(XsL)−ls)VEbE∗′(XsL)−δVEbE∗(XsL)\displaystyle\frac{\sigma^{2}(X^{L}\_{s}}{2}){V^{E}\_{b^{\*}\_{E}}}^{\prime\prime}(X^{L}\_{s})+(\mu(X^{L}\_{s})-{l\_{s}}){V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})-\delta V^{E}\_{b^{\*}\_{E}}(X^{L}\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (σ2​(XsL)2VbE∗E′′(XsL)+(μ(XsL)−l¯I{XsL≥bE∗})VbE∗E′(XsL)−δVbE∗E(XsL)+l¯(γ−β)I{XsL≥bE∗}\displaystyle\bigg(\frac{\sigma^{2}(X^{L}\_{s})}{2}{V^{E}\_{b^{\*}\_{E}}}^{\prime\prime}(X^{L}\_{s})+(\mu(X^{L}\_{s})-\bar{l}I\{X^{L}\_{s}\geq b^{\*}\_{E}\}){V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})-\delta V^{E}\_{b^{\*}\_{E}}(X^{L}\_{s})+\bar{l}(\gamma-\beta)I\{X^{L}\_{s}\geq b^{\*}\_{E}\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Λ)+(l¯I{XsL≥bE∗}−ls)VbE∗E′(XsL)−l¯(γ−β)I{XsL≥bE∗})−Λ\displaystyle+\Lambda\bigg)+(\bar{l}I\{X^{L}\_{s}\geq b^{\*}\_{E}\}-l\_{s}){V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})-\bar{l}(\gamma-\beta)I\{X^{L}\_{s}\geq b^{\*}\_{E}\})-\Lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 0+(l¯I{XsL≥bE∗}−ls)VbE∗E′(XsL)−l¯(γ−β)I{XsL≥bE∗})−Λ\displaystyle 0+(\bar{l}I\{X^{L}\_{s}\geq b^{\*}\_{E}\}-l\_{s}){V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})-\bar{l}(\gamma-\beta)I\{X^{L}\_{s}\geq b^{\*}\_{E}\})-\Lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (l¯−ls)VbE∗E′(XsL)I{XsL≥bE∗}−lsVbE∗E′(XsL)I{XsL<bE∗}−l¯(γ−β)I{XsL≥bE∗})−Λ\displaystyle(\bar{l}-l\_{s}){V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})I\{X^{L}\_{s}\geq b^{\*}\_{E}\}-l\_{s}{V^{E}\_{b^{\*}\_{E}}}^{\prime}(X^{L}\_{s})I\{X^{L}\_{s}<b^{\*}\_{E}\}-\bar{l}(\gamma-\beta)I\{X^{L}\_{s}\geq b^{\*}\_{E}\})-\Lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (l¯−ls)(γ−β)I{XsL≥bE∗}−ls(γ−β)I{XsL<bE∗}−l¯(γ−β)I{XsL≥bE∗})−Λ\displaystyle(\bar{l}-l\_{s})(\gamma-\beta)I\{X^{L}\_{s}\geq b^{\*}\_{E}\}-l\_{s}(\gamma-\beta)I\{X^{L}\_{s}<b^{\*}\_{E}\}-\bar{l}(\gamma-\beta)I\{X^{L}\_{s}\geq b^{\*}\_{E}\})-\Lambda |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | −(γ−β)​ls−Λ,\displaystyle-(\gamma-\beta)l\_{s}-\Lambda, |  | (A.19) |

where the last inequality follows by noting 0≤ls≤l¯0\leq l\_{s}\leq\bar{l}, VbE∗E′​(x)≤γ−β{V^{E}\_{b^{\*}\_{E}}}^{\prime}(x)\leq\gamma-\beta for x≥bE∗x\geq{b^{\*}\_{E}} and VbE∗E′​(x)≥γ−β{V^{E}\_{b^{\*}\_{E}}}^{\prime}(x)\geq\gamma-\beta for 0≤x<bE∗0\leq x<{b^{\*}\_{E}} (see Corollary [A.3](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem3 "Corollary A.3 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") and Lemma [A.4](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem4 "Lemma A.4 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
Combining ([A.18](https://arxiv.org/html/2510.27384v1#A1.E18 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([A.19](https://arxiv.org/html/2510.27384v1#A1.E19 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) yields:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VbE∗E​(x)≥\displaystyle V^{E}\_{b^{\*}\_{E}}(x)\geq | 𝔼x​[e−δ​(τL∧τn∧t)​VbE∗E​(XτL∧τn∧tL)+∫0τL∧τn∧te−δ​s​((γ−β)​ls+Λ)​ds],x≥0.\displaystyle{\mathbb{E}}\_{x}\left[e^{-\delta(\tau^{L}\wedge\tau\_{n}\wedge t)}V^{E}\_{b^{\*}\_{E}}(X^{L}\_{\tau^{L}\wedge\tau\_{n}\wedge t})+\int^{\tau^{L}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}((\gamma-\beta)l\_{s}+\Lambda)\,\mathrm{d}s\right],\ \ x\geq 0. |  | (A.20) |

Note that VbE∗EV^{E}\_{b^{\*}\_{E}} is a bounded function and VbE∗E​(XτLL)=VbE∗E​(0)=0V^{E}\_{b^{\*}\_{E}}(X^{L}\_{\tau^{L}})=V^{E}\_{b^{\*}\_{E}}(0)=0. By letting n→∞n\rightarrow\infty and t→∞t\rightarrow\infty on ([A.20](https://arxiv.org/html/2510.27384v1#A1.E20 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and applying dominated convergence and monotone convergence, we arrive at

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VbE∗E​(x)≥\displaystyle V^{E}\_{b^{\*}\_{E}}(x)\geq | 𝔼x​[∫0τLe−δ​s​((γ−β)​ls+Λ)​ds]=𝒫E​(x;L),x≥0.\displaystyle\;\;{\mathbb{E}}\_{x}\left[\int^{\tau^{L}}\_{0}e^{-\delta s}((\gamma-\beta)l\_{s}+\Lambda)\,\mathrm{d}s\right]=\mathcal{P}^{E}(x;L),\ \ x\geq 0. |  | (A.21) |

As the above inequality holds for all admissible strategies, VbE∗E​(x)≥supL∈Π𝒫E​(x;L)=VE​(x)V^{E}\_{b^{\*}\_{E}}(x)\geq\sup\_{L\in\Pi}\mathcal{P}^{E}(x;L)=V^{E}(x) for x≥0x\geq 0.
On the other hand, LbE∗L^{b^{\*}\_{E}} is an admissible strategy and so
VbE∗E​(x)=𝒫E​(x;LbE∗)≤supL∈Π𝒫E​(x;L)=VE​(x)V^{E}\_{b^{\*}\_{E}}(x)=\mathcal{P}^{E}(x;L^{b^{\*}\_{E}})\leq\sup\_{L\in\Pi}\mathcal{P}^{E}(x;L)=V^{E}(x) for x≥0x\geq 0. This implies LbE∗L^{b^{\*}\_{E}} is an optimal strategy. □\square

Proof to Lemma [3.4](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem4 "Lemma 3.4 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target").
It follows by
(Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Lemma A.1) that for any finite t>0t>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[e−δ​(T^x∧τn∧t)​v3​(YT^x∧τn∧tx)]\displaystyle{\mathbb{E}}\left[e^{-\delta(\hat{T}^{x}\wedge\tau\_{n}\wedge t)}v\_{3}(Y\_{\hat{T}^{x}\wedge\tau\_{n}\wedge t}^{x})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | v3​(x)+𝔼​[∫0T^x∧τn∧te−δ​s​(12​σ2​(Ysx)+(μ​(Ysx)−l¯)​v3′​(Ysx)−δ​v3​(Ysx))​ds].\displaystyle v\_{3}(x)+{\mathbb{E}}\left[\int^{\hat{T}^{x}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}\left(\frac{1}{2}\sigma^{2}(Y\_{s}^{x})+(\mu(Y\_{s}^{x})-\bar{l})v\_{3}^{\prime}(Y\_{s}^{x})-\delta v\_{3}(Y\_{s}^{x})\right)\,\mathrm{d}s\right]. |  |

Note that we have
12​σ2​(Ysx)​v3′′​(Ysx)+(μ​(Ysx)−l¯)​v3′​(Ysx)−δ​v3​(Ysx)=0.\frac{1}{2}\sigma^{2}(Y\_{s}^{x})v\_{3}^{\prime\prime}(Y\_{s}^{x})+(\mu(Y\_{s}^{x})-\bar{l})v\_{3}^{\prime}(Y\_{s}^{x})-\delta v\_{3}(Y\_{s}^{x})=0.
Therefore,
  
v3​(x)=𝔼​[e−δ​(T^x∧τn∧t)​v3​(YT^x∧τn∧tx)]v\_{3}(x)={\mathbb{E}}\left[e^{-\delta(\hat{T}^{x}\wedge\tau\_{n}\wedge t)}v\_{3}(Y\_{\hat{T}^{x}\wedge\tau\_{n}\wedge t}^{x})\right] for x≥0x\geq 0. Since the function v3​(⋅)v\_{3}(\cdot) is bounded, by using the dominated convergence twice we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞limt→∞𝔼​[e−δ​(T^x∧τn∧t)​v3​(YT^x∧τn∧tx)]=𝔼​[e−δ​T^x​v3​(YT^xx)]=𝔼​[e−δ​T^x],x≥0\displaystyle\lim\_{n\rightarrow\infty}\lim\_{t\rightarrow\infty}{\mathbb{E}}\left[e^{-\delta(\hat{T}^{x}\wedge\tau\_{n}\wedge t)}v\_{3}(Y\_{\hat{T}^{x}\wedge\tau\_{n}\wedge t}^{x})\right]={\mathbb{E}}\left[e^{-\delta\hat{T}^{x}}v\_{3}(Y\_{\hat{T}^{x}}^{x})\right]={\mathbb{E}}\left[e^{-\delta\hat{T}^{x}}\right],\quad x\geq 0 |  | (A.22) |

It then follows by ([3.16](https://arxiv.org/html/2510.27384v1#S3.E16 "In Lemma 3.4 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that
limx→∞v3​(x)=limx→∞E​[e−δ​T^x]=E​[limx→∞e−δ​T^x]=0,\lim\_{x\rightarrow\infty}v\_{3}(x)=\lim\_{x\rightarrow\infty}E\bigg[e^{-\delta\hat{T}^{x}}\bigg]=E\bigg[\lim\_{x\rightarrow\infty}e^{-\delta\hat{T}^{x}}\bigg]=0,
where the second-to-last equality follows from the dominated convergence theorem, and the last equality follows by noting
T^x→∞\hat{T}^{x}\rightarrow\infty as xx goes to ∞\infty.

Similarly, we know that for any finite t>0t>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[e−δ​(T^x∧τn∧t)​u​(YT^x∧τn∧tx)]\displaystyle{\mathbb{E}}\left[e^{-\delta(\hat{T}^{x}\wedge\tau\_{n}\wedge t)}u(Y\_{\hat{T}^{x}\wedge\tau\_{n}\wedge t}^{x})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | u​(x)+𝔼​[∫0T^x∧τn∧te−δ​s​(12​σ2​(Ysx)​u′′​(Ysx)+(μ​(Ysx)−l¯)​u′​(Ysx)−δ​u​(Ysx))​ds].\displaystyle\;u(x)+{\mathbb{E}}\left[\int^{\hat{T}^{x}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}\left(\frac{1}{2}\sigma^{2}(Y\_{s}^{x})u^{\prime\prime}(Y\_{s}^{x})+(\mu(Y\_{s}^{x})-\bar{l})u^{\prime}(Y\_{s}^{x})-\delta u(Y\_{s}^{x})\right)\,\mathrm{d}s\right]. |  |

Note we have
12​σ2​(Ysx)​u′′​(Ysx)+(μ​(Ysx)−l¯)​u′​(Ysx)−δ​u​(Ysx)+(l¯​(γ−β)+Λ)=0.\frac{1}{2}\sigma^{2}(Y\_{s}^{x})u^{\prime\prime}(Y\_{s}^{x})+(\mu(Y\_{s}^{x})-\bar{l})u^{\prime}(Y\_{s}^{x})-\delta u(Y\_{s}^{x})+(\bar{l}(\gamma-\beta)+\Lambda)=0.
Hence,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u​(x)=\displaystyle u(x)= | 𝔼​[e−δ​(T^x∧τn∧t)​u​(YT^x∧τn∧tx)]+𝔼​[∫0T^x∧τn∧te−δ​s​(l¯​(γ−β)+Λ)​ds],x≥0.\displaystyle{\mathbb{E}}\left[e^{-\delta(\hat{T}^{x}\wedge\tau\_{n}\wedge t)}u(Y\_{\hat{T}^{x}\wedge\tau\_{n}\wedge t}^{x})\right]+{\mathbb{E}}\left[\int^{\hat{T}^{x}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}\left(\bar{l}(\gamma-\beta)+\Lambda\right)\,\mathrm{d}s\right],\ \ x\geq 0. |  | (A.23) |

Since the function u​(⋅)u(\cdot) is bounded, by using the dominated convergence we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞limt→∞𝔼​[e−δ​(T^x∧τn∧t)​u​(YT^x∧τn∧tx)]=𝔼​[e−δ​T^x​u​(YT^xx)]=0,x≥0,\displaystyle\lim\_{n\rightarrow\infty}\lim\_{t\rightarrow\infty}{\mathbb{E}}\left[e^{-\delta(\hat{T}^{x}\wedge\tau\_{n}\wedge t)}u(Y\_{\hat{T}^{x}\wedge\tau\_{n}\wedge t}^{x})\right]={\mathbb{E}}\left[e^{-\delta\hat{T}^{x}}u(Y\_{\hat{T}^{x}}^{x})\right]=0,\quad x\geq 0, |  | (A.24) |

where the last equality follows by noticing YT^xx=0Y\_{\hat{T}^{x}}^{x}=0 and u​(0)=0u(0)=0.
Employing monotone convergence, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞limt→∞𝔼​[∫0T^x∧τn∧te−δ​s​(Λ+(γ−β)​l¯)​ds]=𝔼​[∫0T^xe−δ​s​(Λ+(γ−β)​l¯)​ds],x≥0.\displaystyle\lim\_{n\rightarrow\infty}\lim\_{t\rightarrow\infty}{\mathbb{E}}\left[\int^{\hat{T}^{x}\wedge\tau\_{n}\wedge t}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l})\,\mathrm{d}s\right]={\mathbb{E}}\left[\int^{\hat{T}^{x}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l})\,\mathrm{d}s\right],\quad x\geq 0. |  | (A.25) |

Combining ([A.23](https://arxiv.org/html/2510.27384v1#A1.E23 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), ([A.24](https://arxiv.org/html/2510.27384v1#A1.E24 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([A.25](https://arxiv.org/html/2510.27384v1#A1.E25 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) yields ([3.16](https://arxiv.org/html/2510.27384v1#S3.E16 "In Lemma 3.4 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
Then from ([3.16](https://arxiv.org/html/2510.27384v1#S3.E16 "In Lemma 3.4 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) we know that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limx→∞u​(x)\displaystyle\lim\_{x\rightarrow\infty}u(x) | =limx→∞𝔼​[∫0T^xe−δ​s​(Λ+(γ−β)​l¯)​ds]\displaystyle=\lim\_{x\rightarrow\infty}{\mathbb{E}}\left[\int^{\hat{T}^{x}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l})\,\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[limx→∞∫0T^xe−δ​s​(Λ+(γ−β)​l¯)​ds]=Λ+(γ−β)​l¯δ,\displaystyle={\mathbb{E}}\left[\lim\_{x\rightarrow\infty}\int^{\hat{T}^{x}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l})\,\mathrm{d}s\right]=\frac{\Lambda+(\gamma-\beta)\bar{l}}{\delta}, |  |

where the second to the last equality follows from the dominated convergence theorem, and the last equality follows by noting
T^x→∞\hat{T}^{x}\rightarrow\infty as xx goes to ∞\infty.
□\square

## Appendix B Derivations for Subsection [3.1](https://arxiv.org/html/2510.27384v1#S3.SS1 "3.1 The Brownian motion model ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")

Recall that VbE​(⋅)V^{E}\_{b}(\cdot) is the bounded and continuously differentiable
solution to the following equations:
σ22​g′′​(x)+μ​g′​(x)−δ​g​(x)+Λ=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+\mu g^{\prime}(x)-\delta g(x)+\Lambda=0 for 0<x<b,0<x<b, and σ22​g′′​(x)+(μ−l¯)​g′​(x)−δ​g​(x)+(γ−β)​l¯+Λ=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+(\mu-\bar{l})g^{\prime}(x)-\delta g(x)+(\gamma-\beta)\bar{l}+\Lambda=0 for x>bx>b with g​(0)=0g(0)=0. Here eθ1​xe^{\theta\_{1}x} and e−θ2​xe^{-\theta\_{2}x} form a set of linearly
independent solutions to σ22​g′′​(x)+μ​g′​(x)−δ​g​(x)=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+\mu g^{\prime}(x)-\delta g(x)=0 and have a Wronskian −(θ1+θ2)​e(θ1−θ2)​x-(\theta\_{1}+\theta\_{2})e^{(\theta\_{1}-\theta\_{2})x}, and
eθ3​xe^{\theta\_{3}x} and e−θ4​xe^{-\theta\_{4}x} form a set of
linearly independent solutions to σ22​g′′​(x)+(μ−l¯)​g′​(x)−δ​g​(x)=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+(\mu-\bar{l})g^{\prime}(x)-\delta g(x)=0 and have a Wronskian −(θ3+θ4)​e(θ3−θ4)​x-(\theta\_{3}+\theta\_{4})e^{(\theta\_{3}-\theta\_{4})x}.
By using the variation of parameters method, we obtain

|  |  |  |
| --- | --- | --- |
|  | VbE​(x)={K1​(b)​eθ1​x−K1​(b)​e−θ2​x−2​Λσ2​eθ1​x−1θ1​(θ1+θ2)+2​Λσ2​1−e−θ2​xθ2​(θ1+θ2),0≤x<b,K4​(b)​e−θ4​x−2​((γ−β)​l¯+Λ)σ2​−1θ3​(θ3+θ4)+2​((γ−β)​l¯+Λ)σ2​1−e−θ4​xθ4​(θ3+θ4),x≥b,V\_{b}^{E}(x)=\begin{cases}K\_{1}(b)e^{\theta\_{1}x}-K\_{1}(b)e^{-\theta\_{2}x}-\frac{2\Lambda}{\sigma^{2}}\frac{e^{\theta\_{1}x}-1}{\theta\_{1}(\theta\_{1}+\theta\_{2})}+\frac{2\Lambda}{\sigma^{2}}\frac{1-e^{-\theta\_{2}x}}{\theta\_{2}(\theta\_{1}+\theta\_{2})},&0\leq x<b,\\ K\_{4}(b)e^{-\theta\_{4}x}-\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{-1}{\theta\_{3}(\theta\_{3}+\theta\_{4})}+\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{1-e^{-\theta\_{4}x}}{\theta\_{4}(\theta\_{3}+\theta\_{4})},&x\geq b,\end{cases} |  |

where K1​(b)K\_{1}(b) and K4​(b)K\_{4}(b) are determined by VbE​(b−)=VbE​(b+){V\_{b}^{E}}(b-)={V\_{b}^{E}}(b+), VbE′​(b−)=VbE′​(b+){V\_{b}^{E}}^{\prime}(b-)={V\_{b}^{E}}^{\prime}(b+):

|  |  |  |  |
| --- | --- | --- | --- |
|  | K1​(b)\displaystyle K\_{1}(b) | =2​Λ​(θ2​(θ1+θ4)​eθ1​b+θ1​(θ4−θ2)​e−θ2​b−θ4​(θ1+θ2))σ2​θ1​θ2​(θ1+θ2)+2​((γ−β)​l¯+Λ)σ2​θ3(θ1+θ4)​eθ1​b+(θ2−θ4)​e−θ2​b≜I1​(b)​Λ+I2​(b),\displaystyle=\frac{\frac{2\Lambda\left(\theta\_{2}(\theta\_{1}+\theta\_{4})e^{\theta\_{1}b}+\theta\_{1}(\theta\_{4}-\theta\_{2})e^{-\theta\_{2}b}-\theta\_{4}(\theta\_{1}+\theta\_{2})\right)}{\sigma^{2}\theta\_{1}\theta\_{2}(\theta\_{1}+\theta\_{2})}+\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}\theta\_{3}}}{(\theta\_{1}+\theta\_{4})e^{\theta\_{1}b}+(\theta\_{2}-\theta\_{4})e^{-\theta\_{2}b}}\triangleq I\_{1}(b)\Lambda+I\_{2}(b), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K4​(b)\displaystyle K\_{4}(b) | =2​Λ​(eθ1​b−e−θ2​b)σ2​(θ1+θ2)+2​((γ−β)​l¯+Λ)​e−θ4​bσ2​(θ3+θ4)−(θ1​eθ1​b+θ2​e−θ2​b)​K1​(b)θ4​e−θ4​b≜I3​(b)​Λ+I4​(b),\displaystyle=\frac{\frac{2\Lambda(e^{\theta\_{1}b}-e^{-\theta\_{2}b})}{\sigma^{2}(\theta\_{1}+\theta\_{2})}+\frac{2((\gamma-\beta)\bar{l}+\Lambda)e^{-\theta\_{4}b}}{\sigma^{2}(\theta\_{3}+\theta\_{4})}-(\theta\_{1}e^{\theta\_{1}b}+\theta\_{2}e^{-\theta\_{2}b})K\_{1}(b)}{\theta\_{4}e^{-\theta\_{4}b}}\triangleq I\_{3}(b)\Lambda+I\_{4}(b), |  |

where I1​(b)I\_{1}(b)–I4​(b)I\_{4}(b) are given in ([3.24](https://arxiv.org/html/2510.27384v1#S3.E24 "In 3.1 The Brownian motion model ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))-([3.27](https://arxiv.org/html/2510.27384v1#S3.E27 "In 3.1 The Brownian motion model ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
This leads to ([3.21](https://arxiv.org/html/2510.27384v1#S3.E21 "In 3.1 The Brownian motion model ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

## Appendix C Proofs of Section [4](https://arxiv.org/html/2510.27384v1#S4 "4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")

###### Lemma C.1

For any strategy, the associated objective function is nonnegative and has an initial value 0 (the value when the initial state is 0), and has an upper bound ((γ−β)​l¯+Λ)δ​λ​α+δλ+δ\frac{((\gamma-\beta)\bar{l}+\Lambda)}{\delta}\frac{\lambda\alpha+\delta}{\lambda+\delta}.

Proof.  From its definition, we can see that for any L,L~∈ΠL,\tilde{L}\in\Pi, 𝒫0​(x;L,L~)≥0\mathcal{P}\_{0}(x;L,\tilde{L})\geq 0 for x≥0x\geq 0.
Note that for any admissible strategy, the excess emission rate has an upper bound l¯\bar{l}. So for any L,L~∈ΠL,\tilde{L}\in\Pi,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫​(x;L,L~)\displaystyle\mathcal{P}(x;L,\tilde{L}) | ≤𝔼x​[∫0η0e−δ​t​((γ−β)​l¯+Λ)​dt+∫η0∞α​e−δ​t​((γ−β)​l¯+Λ)​dt]\displaystyle\leq{\mathbb{E}}\_{x}\left[\int\_{0}^{\eta\_{0}}e^{-\delta t}((\gamma-\beta)\bar{l}+\Lambda)\,\mathrm{d}t+\int\_{\eta\_{0}}^{\infty}\alpha e^{-\delta t}((\gamma-\beta)\bar{l}+\Lambda)\,\mathrm{d}t\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(γ−β)​l¯+Λδ𝔼x[1−(1−α)e−δ​η0]=(γ−β)​l¯+Λδλ​α+δλ+δ,x≥0.□\displaystyle=\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}{\mathbb{E}}\_{x}[1-(1-\alpha)e^{-\delta\eta\_{0}}]=\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}\frac{\lambda\alpha+\delta}{\lambda+\delta},\ \ x\geq 0.\hskip 28.45274pt\hskip 28.45274pt\hskip 28.45274pt\square |  |

###### Lemma C.2

(i) For any b≥0b\geq 0,
there is a bounded function that is continuously differentiable on [0,∞)[0,\infty) and twice continuously differentiable on [0,b)∪(b,∞)[0,b)\cup(b,\infty), and satisfies the following equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ=0​ for 0<x<b,\displaystyle\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V^{E}\_{b}(x)+\Lambda=0\mbox{ for $0<x<b$}, |  | (C.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(0)=0,\displaystyle g(0)=0,\ \ |  | (C.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ+l¯​(γ−β)=0​ for x>b,\displaystyle\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V^{E}\_{b}(x)+\Lambda+\bar{l}(\gamma-\beta)=0\mbox{ for $x>b$}, |  | (C.3) |

(ii) The above solution is unique and equals Vb​(x)V\_{b}(x). (iii) The function h¯​(b):=Vb′​(b)\bar{h}(b):=V\_{b}^{\prime}(b) as a function of bb is continuous on [0,∞)[0,\infty), and limb↓0Vb′′​(0+)=V0′′​(0+)\lim\_{b\downarrow 0}V\_{b}^{\prime\prime}(0+)=V\_{0}^{\prime\prime}(0+).

Proof.  (i) This can be proven by employing arguments similar to the proof for Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"). Define
v¯1​(⋅)\overline{v}\_{1}(\cdot) and v¯2​(⋅)\overline{v}\_{2}(\cdot) to be the solutions to
σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−(λ+δ)​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-(\lambda+\delta)g(x)=0 on [0,∞)[0,\infty) with the following two sets of initial values respectively, v¯1​(0)=1\overline{v}\_{1}(0)=1 and v¯1′​(0)=1\overline{v}\_{1}^{\prime}(0)=1, and v¯2​(0)=1\overline{v}\_{2}(0)=1 and v¯2′​(0)=−1\overline{v}\_{2}^{\prime}(0)=-1. The existence and uniqueness of v¯1\overline{v}\_{1} and v¯2\overline{v}\_{2} are guaranteed by Theorem 5.4.2. of Krylov, ([1996](https://arxiv.org/html/2510.27384v1#bib.bib25)).
We can see that v¯1\overline{v}\_{1} and v¯2\overline{v}\_{2} are linearly independent.
Define

|  |  |  |
| --- | --- | --- |
|  | W¯1​(x)=v¯1​(x)​v¯2′​(x)−v¯2​(x)​v¯1′​(x),\displaystyle\overline{W}\_{1}(x)=\overline{v}\_{1}(x)\overline{v}\_{2}^{\prime}(x)-\overline{v}\_{2}(x)\overline{v}\_{1}^{\prime}(x), |  |
|  |  |  |
| --- | --- | --- |
|  | B¯1​(x)=v¯1​(x)​∫0xv¯2​(y)W¯1​(y)​2​(Λ+λ​α​VbE​(x))σ2​(y)​dy−v¯2​(x)​∫0xv¯1​(y)W¯1​(y)​2​(Λ+λ​α​VbE​(x))σ2​(y)​dy.\displaystyle\overline{B}\_{1}(x)=\overline{v}\_{1}(x)\int\_{0}^{x}\frac{\overline{v}\_{2}(y)}{\overline{W}\_{1}(y)}\frac{2(\Lambda+\lambda\alpha V\_{b}^{E}(x))}{\sigma^{2}(y)}\,\mathrm{d}y-\overline{v}\_{2}(x)\int\_{0}^{x}\frac{\overline{v}\_{1}(y)}{\overline{W}\_{1}(y)}\frac{2(\Lambda+\lambda\alpha V\_{b}^{E}(x))}{\sigma^{2}(y)}\,\mathrm{d}y. |  |

Then all the solutions to ([C.1](https://arxiv.org/html/2510.27384v1#A3.E1 "In Lemma C.2 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) have the following general form: c1​v¯1​(x)+c2​v¯2​(x)+B¯1​(x)c\_{1}\,\overline{v}\_{1}(x)+c\_{2}\overline{v}\_{2}(x)+\overline{B}\_{1}(x), where c1c\_{1}\, and c2c\_{2} are constants.
Here B¯1​(x)\overline{B}\_{1}(x) is a particular solution to σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ+l¯​(γ−β)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+\Lambda+\bar{l}(\gamma-\beta)=0 with B¯1​(0)=0\overline{B}\_{1}(0)=0 and B¯1′​(0)=0\overline{B}\_{1}^{\prime}(0)=0.

Let v¯3​(⋅)\overline{v}\_{3}(\cdot) be a bounded solution to
σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)=0 on [0,∞)[0,\infty) with initial value g​(0)=1g(0)=1. Let u¯b​(x)\overline{u}\_{b}(x) be a bounded solution to σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ+(γ−β)​l¯=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+\Lambda+(\gamma-\beta)\bar{l}=0 on [0,∞)[0,\infty) with initial value g​(0)=0g(0)=0. Note VbE​(x)V\_{b}^{E}(x) is bounded on [0,∞)[0,\infty) (see Lemma [3.2](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem2 "Lemma 3.2 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and VbE​(x)=0V\_{b}^{E}(x)=0 for x<0x<0. By extending the differential equation to (−∞,−1)∪(0,∞)(-\infty,-1)\cup(0,\infty) and adding the boundary condition g​(−1)=1g(-1)=1, and then using Corollary 8.1 of Pao, ([1992](https://arxiv.org/html/2510.27384v1#bib.bib35)) we can show v¯3\overline{v}\_{3} and u¯b\overline{u}\_{b} exist. Then, for any constant C3C\_{3}, the function C3​v¯3​(x)+u¯b​(x)C\_{3}\overline{v}\_{3}(x)+\overline{u}\_{b}(x) is a solution to ([C.3](https://arxiv.org/html/2510.27384v1#A3.E3 "In Lemma C.2 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). For b≥0b\geq 0, define a new function

|  |  |  |  |
| --- | --- | --- | --- |
|  | g¯b​(x)={C¯1​(b)​v¯1​(x)−C¯1​(b)​v¯2​(x)+B¯1​(x)0≤x<bC¯3​(b)​v¯3​(x)+u¯b​(x)x≥b,\displaystyle\overline{g}\_{b}(x)=\left\{\begin{array}[]{ll}\overline{C}\_{1}(b)\overline{v}\_{1}(x)-\overline{C}\_{1}(b)\overline{v}\_{2}(x)+\overline{B}\_{1}(x)&0\leq x<b\\ \overline{C}\_{3}(b)\overline{v}\_{3}(x)+\overline{u}\_{b}(x)&x\geq b,\end{array}\right. |  | (C.6) |

where C¯1​(b)\overline{C}\_{1}(b) and C¯3​(b)\overline{C}\_{3}(b) satisfy the following:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | when b>0b>0, | C¯1​(b)​v¯1​(b)−C¯1​(b)​v¯2​(b)+B¯1​(b)=C¯3​(b)​v¯3​(b)+u¯b​(b),\displaystyle\overline{C}\_{1}(b)\overline{v}\_{1}(b)-\overline{C}\_{1}(b)\overline{v}\_{2}(b)+\overline{B}\_{1}(b)=\overline{C}\_{3}(b)\overline{v}\_{3}(b)+\overline{u}\_{b}(b), |  | (C.8) |
|  |  |  | C¯1​(b)​v¯1′​(b)−C¯1​(b)​v¯2′​(b)+B¯1′​(b)=C¯3​(b)​v¯3′​(b)+u¯b′​(b),\displaystyle\overline{C}\_{1}(b)\overline{v}\_{1}^{\prime}(b)-\overline{C}\_{1}(b)\overline{v}\_{2}^{\prime}(b)+\overline{B}\_{1}^{\prime}(b)=\overline{C}\_{3}(b)\overline{v}\_{3}^{\prime}(b)+\overline{u}\_{b}^{\prime}(b), |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | and when b=0b=0, | C¯3​(0)=0.\displaystyle\overline{C}\_{3}(0)=0. |  | (C.9) |

All the arguments following ([A.6](https://arxiv.org/html/2510.27384v1#A1.E6 "In Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) in the proof of Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (i) can be adapted here after replacing vi​(x)v\_{i}(x) by v¯i​(x)\overline{v}\_{i}(x), B1​(x)B\_{1}(x) by B¯1​(x)\overline{B}\_{1}(x), Ci​(b)C\_{i}(b) by C¯i​(b)\overline{C}\_{i}(b) i=1,2,3i=1,2,3, and gb​(x)g\_{b}(x) by g¯b​(x)\overline{g}\_{b}(x), respectively.

(ii) Consider any fixed b≥0b\geq 0. It is sufficient to
show that any solution in (i) coincides with Vb​(x)V\_{b}(x) for x≥0x\geq 0. Let gg be any bounded solution that meets all the requirements in (i).
It follows by
(Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Lemma A.1) that for x≥0x\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼x​[e−(λ+δ)​(τb∧τn∧t)​g​(Xτb∧τn∧tb)]\displaystyle{\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)(\tau^{b}\wedge\tau\_{n}\wedge t)}g(X^{b}\_{\tau^{b}\wedge\tau\_{n}\wedge t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | g​(x)+𝔼x​[∫0τb∧τn∧te−(λ+δ)​s​(12​σ2​(Xsb)​g′′​(Xsb)+(μ​(Xsb)−lsb)​g′​(Xsb)−(λ+δ)​g​(Xsb))​ds].\displaystyle\;g(x)+{\mathbb{E}}\_{x}\left[\int^{\tau^{b}\wedge\tau\_{n}\wedge t}\_{0}e^{-(\lambda+\delta)s}\left(\frac{1}{2}\sigma^{2}(X^{b}\_{s})g^{\prime\prime}(X^{b}\_{s})+(\mu(X^{b}\_{s})-l\_{s}^{b})g^{\prime}(X^{b}\_{s})-(\lambda+\delta)g(X^{b}\_{s})\right)\,\mathrm{d}s\right]. |  |

Note that lsb=l¯​I​{Xsb≥b}l\_{s}^{b}=\bar{l}I\{X^{b}\_{s}\geq b\} and that gg satisfies ([C.1](https://arxiv.org/html/2510.27384v1#A3.E1 "In Lemma C.2 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([C.3](https://arxiv.org/html/2510.27384v1#A3.E3 "In Lemma C.2 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and so we have

|  |  |  |
| --- | --- | --- |
|  | 12​σ2​(Xsb)​g′′​(Xsb)+(μ​(Xsb)−lsb)​g′​(Xsb)−(λ+δ)​g​(Xsb)=−Λ−l¯​(γ−β)​I​{Xsb≥b}−λ​α​VbE​(x).\displaystyle\frac{1}{2}\sigma^{2}(X^{b}\_{s})g^{\prime\prime}(X^{b}\_{s})+(\mu(X^{b}\_{s})-l\_{s}^{b})g^{\prime}(X^{b}\_{s})-(\lambda+\delta)g(X^{b}\_{s})=-\Lambda-\bar{l}(\gamma-\beta)I\{X^{b}\_{s}\geq b\}-\lambda\alpha V\_{b}^{E}(x). |  |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)=\displaystyle g(x)= | 𝔼x​[e−(λ+δ)​(τb∧τn∧t)​g​(Xτb∧τn∧tb)]\displaystyle{\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)(\tau^{b}\wedge\tau\_{n}\wedge t)}g(X^{b}\_{\tau^{b}\wedge\tau\_{n}\wedge t})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼x​[∫0τb∧τn∧te−(λ+δ)​s​(Λ+l¯​(γ−β)​I​{Xsb≥b}+λ​α​VbE​(x))​ds].\displaystyle+{\mathbb{E}}\_{x}\left[\int\_{0}^{\tau^{b}\wedge\tau\_{n}\wedge t}e^{-(\lambda+\delta)s}(\Lambda+\bar{l}(\gamma-\beta)I\{X^{b}\_{s}\geq b\}+\lambda\alpha V\_{b}^{E}(x))\,\mathrm{d}s\right]. |  | (C.10) |

Since the function g​(⋅)g(\cdot) is bounded, using the dominated convergence twice we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞limn→∞𝔼x​[e−(λ+δ)​(τb∧τn∧t)​g​(Xτb∧τn∧tb)]=𝔼x​[e−(λ+δ)​τb​g​(Xτbb)]=0,\displaystyle\lim\_{t\rightarrow\infty}\lim\_{n\rightarrow\infty}{\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)(\tau^{b}\wedge\tau\_{n}\wedge t)}g(X^{b}\_{\tau^{b}\wedge\tau\_{n}\wedge t})\right]={\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)\tau^{b}}g(X^{b}\_{\tau^{b}})\right]=0, |  | (C.11) |

where the last equality follows by noticing Xτbb=0X^{b}\_{\tau^{b}}=0 and g​(0)=0g(0)=0.
By using the monotone convergence twice we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limt→∞limn→∞𝔼x​[∫0τb∧τn∧te−(λ+δ)​s​(Λ+(γ−β)​l¯​I​{Xsb≥b})​ds]\displaystyle\lim\_{t\rightarrow\infty}\lim\_{n\rightarrow\infty}{\mathbb{E}}\_{x}\left[\int^{\tau^{b}\wedge\tau\_{n}\wedge t}\_{0}e^{-(\lambda+\delta)s}(\Lambda+(\gamma-\beta)\bar{l}I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼x​[∫0τbe−(λ+δ)​s​(Λ+(γ−β)​l¯​I​{Xsb≥b})​ds]\displaystyle{\mathbb{E}}\_{x}\left[\int^{\tau^{b}}\_{0}e^{-(\lambda+\delta)s}(\Lambda+(\gamma-\beta)\bar{l}I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼x​[∫0τb∧η0e−δ​s​(Λ+(γ−β)​l¯​I​{Xsb≥b})​ds],\displaystyle{\mathbb{E}}\_{x}\left[\int^{\tau^{b}\wedge\eta\_{0}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l}I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s\right], |  | (C.12) |

where the last equality follows by using (Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Eq.(A.2)). We then have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x​[∫0τbλ​α​e−(λ+δ)​s​VbE​(Xsb)​ds]=𝔼x​[α​e−δ​η0​VbE​(Xη0b)​I​{η0≤τb}].\displaystyle{\mathbb{E}}\_{x}\left[\int^{\tau^{b}}\_{0}\lambda\alpha e^{-(\lambda+\delta)s}V\_{b}^{E}(X^{b}\_{s})\,\mathrm{d}s\right]={\mathbb{E}}\_{x}\left[\alpha e^{-\delta\eta\_{0}}V\_{b}^{E}(X^{b}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{b}\}\right]. |  | (C.13) |

By letting t→∞t\rightarrow\infty and n→∞n\rightarrow\infty on both sides of ([C.10](https://arxiv.org/html/2510.27384v1#A3.E10 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and then using ([C.11](https://arxiv.org/html/2510.27384v1#A3.E11 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) -([C.13](https://arxiv.org/html/2510.27384v1#A3.E13 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we conclude

|  |  |  |
| --- | --- | --- |
|  | g​(x)=𝔼x​[∫0τb∧η0e−δ​s​(Λ+(γ−β)​l¯​I​{Xsb≥b})​ds+α​e−δ​η0​VbE​(Xη0b)​I​{η0≤τb}]=Vb​(x),x≥0,g(x)={\mathbb{E}}\_{x}\left[\int^{\tau^{b}\wedge\eta\_{0}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{l}I\{X^{b}\_{s}\geq b\})\,\mathrm{d}s+\alpha e^{-\delta\eta\_{0}}V\_{b}^{E}(X^{b}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{b}\}\right]=V\_{b}(x),\ \ x\geq 0, |  |

where the last equality follows using the definition of VbV\_{b} in ([4.5](https://arxiv.org/html/2510.27384v1#S4.E5 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

(iii) This can be proven by following the same lines as in the proof of Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (iii). □\square

###### Remark C.1

From the last lemma it follows immediately that Vb​(x)V\_{b}(x) is continuously differentiable on [0,∞)[0,\infty) and twice continuously differentiable on [0,b)∪(b,∞)[0,b)\cup(b,\infty); additionally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​Vb′′​(x)+μ​(x)​Vb′​(x)−(λ+δ)​Vb​(x)+λ​α​VbE​(x)+Λ=0,0<x<b,\displaystyle\frac{\sigma^{2}(x)}{2}V\_{b}^{\prime\prime}(x)+\mu(x)V\_{b}^{\prime}(x)-(\lambda+\delta)V\_{b}(x)+\lambda\alpha V^{E}\_{b}(x)+\Lambda=0,\quad 0<x<b, |  | (C.14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​Vb′′​(x)+(μ​(x)−l¯)​Vb′​(x)−(λ+δ)​Vb​(x)+λ​α​VbE​(x)+l¯​(γ−β)+Λ=0,x>b,\displaystyle\frac{\sigma^{2}(x)}{2}V\_{b}^{\prime\prime}(x)+(\mu(x)-\bar{l})V\_{b}^{\prime}(x)-(\lambda+\delta)V\_{b}(x)+\lambda\alpha V^{E}\_{b}(x)+\bar{l}(\gamma-\beta)+\Lambda=0,\quad x>b, |  | (C.15) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb​(0)=0.\displaystyle V\_{b}(0)=0. |  | (C.16) |

Furthermore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb​(x)={C¯1​(b)​v¯1​(x)−C¯1​(b)​v¯2​(x)+B¯1​(x)0≤x<bC¯3​(b)​v¯3​(x)+u¯b​(x)x≥b,\displaystyle V\_{b}(x)=\left\{\begin{array}[]{ll}\overline{C}\_{1}(b)\overline{v}\_{1}(x)-\overline{C}\_{1}(b)\overline{v}\_{2}(x)+\overline{B}\_{1}(x)&0\leq x<b\\ \overline{C}\_{3}(b)\overline{v}\_{3}(x)+\overline{u}\_{b}(x)&x\geq b,\end{array}\right. |  | (C.19) |

where C¯1​(b)\overline{C}\_{1}(b) and C¯3​(b)\overline{C}\_{3}(b) are constants satisfying the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯1​(b)​v¯1​(b)−C¯1​(b)​v¯2​(b)+B1​(b)=C¯3​(b)​v¯3​(b)+ub​(b),\displaystyle\overline{C}\_{1}(b)\overline{v}\_{1}(b)-\overline{C}\_{1}(b)\overline{v}\_{2}(b)+B\_{1}(b)=\overline{C}\_{3}(b)\overline{v}\_{3}(b)+u\_{b}(b), |  | (C.20) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯1​(b)​v¯1′​(b)−C¯1​(b)​v¯2′​(b)+B¯1′​(b)=C¯3​(b)​v¯3′​(b)+u¯b′​(b),\displaystyle\overline{C}\_{1}(b)\overline{v}\_{1}^{\prime}(b)-\overline{C}\_{1}(b)\overline{v}\_{2}^{\prime}(b)+\overline{B}\_{1}^{\prime}(b)=\overline{C}\_{3}(b)\overline{v}\_{3}^{\prime}(b)+\overline{u}\_{b}^{\prime}(b), |  | (C.21) |

that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯1​(b)=(B¯1(b)−u¯b(b)v¯3′(b)−(B¯1′(b)−u¯b′(b)v¯3(b)(v¯1′(b)−v¯2′(b)v¯3(b)−(v¯1(b)−v¯2(b)v¯3′(b),\displaystyle\overline{C}\_{1}(b)=\frac{(\overline{B}\_{1}(b)-\overline{u}\_{b}(b)\overline{v}\_{3}^{\prime}(b)-(\overline{B}\_{1}^{\prime}(b)-\overline{u}\_{b}^{\prime}(b)\overline{v}\_{3}(b)}{(\overline{v}\_{1}^{\prime}(b)-\overline{v}\_{2}^{\prime}(b)\overline{v}\_{3}(b)-(\overline{v}\_{1}(b)-\overline{v}\_{2}(b)\overline{v}\_{3}^{\prime}(b)}, |  | (C.22) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯3​(b)=(u¯b′(b)−B¯1′(b)(v¯1(b)−v¯2(b)−(u¯b(b)−B¯1(b)(v¯1′(b)−v¯2′(b)(v¯1′(b)−v¯2′(b)v¯3(b)−(v¯1(b)−v¯2(b)v¯3′(b).\displaystyle\overline{C}\_{3}(b)=\frac{(\overline{u}\_{b}^{\prime}(b)-\overline{B}\_{1}^{\prime}(b)(\overline{v}\_{1}(b)-\overline{v}\_{2}(b)-(\overline{u}\_{b}(b)-\overline{B}\_{1}(b)(\overline{v}\_{1}^{\prime}(b)-\overline{v}\_{2}^{\prime}(b)}{(\overline{v}\_{1}^{\prime}(b)-\overline{v}\_{2}^{\prime}(b)\overline{v}\_{3}(b)-(\overline{v}\_{1}(b)-\overline{v}\_{2}(b)\overline{v}\_{3}^{\prime}(b)}. |  | (C.23) |

If Vb′​(b)=γ−βV\_{b}^{\prime}(b)=\gamma-\beta, then Vb​(x)V\_{b}(x) is twice continuously differentiable on [0,∞)[0,\infty).

Recall that VbEV\_{b}^{E} is the expected profit function associated with the threshold strategy, LbL^{b}, under the exponential discounting.
We can derive the following relationship between VbEV\_{b}^{E} and VbV\_{b}.

###### Lemma C.3

For any b≥0b\geq 0, α​VbE​(x)≤Vb​(x)≤VbE​(x)\alpha V\_{b}^{E}(x)\leq V\_{b}(x)\leq V\_{b}^{E}(x) and 0≤Vb′​(x)≤VbE′​(x)0\leq V\_{b}^{\prime}(x)\leq{V\_{b}^{E}}^{\prime}(x) for x≥0x\geq 0.

Proof.  It follows from the definitions of VbEV\_{b}^{E} in ([3.3](https://arxiv.org/html/2510.27384v1#S3.E3 "In 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and VbV\_{b} in ([4.5](https://arxiv.org/html/2510.27384v1#S4.E5 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that when 0<α<10<\alpha<1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb​(x)\displaystyle V\_{b}(x) | =𝔼x+h[∫0η0∧τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt\displaystyle={\mathbb{E}}\_{x+h}\bigg[\int\_{0}^{\eta\_{0}\wedge\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +I{η0<τb}∫η0τbαe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt]\displaystyle\quad\quad\quad\quad\quad\quad+I\{\eta\_{0}<\tau^{b}\}\int\_{\eta\_{0}}^{\tau^{b}}\alpha e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥α(𝔼x+h[∫0η0∧τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt\displaystyle\geq\alpha\left({\mathbb{E}}\_{x+h}\bigg[\int\_{0}^{\eta\_{0}\wedge\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫η0∧τbτbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt])=αVbE(x),x≥0,\displaystyle\quad\quad\quad\quad\quad\quad+\left.\int\_{\eta\_{0}\wedge\tau^{b}}^{\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg]\right)=\alpha V\_{b}^{E}(x),\ \ x\geq 0, |  | (C.24) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb​(x)=\displaystyle V\_{b}(x)= | 𝔼x+h[∫0η0∧τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt\displaystyle\;{\mathbb{E}}\_{x+h}\bigg[\int\_{0}^{\eta\_{0}\wedge\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +I{η0<τb}∫η0τbαe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt]\displaystyle\quad\quad\quad\quad+I\{\eta\_{0}<\tau^{b}\}\int\_{\eta\_{0}}^{\tau^{b}}\alpha e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼x+h[∫0η0∧τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt\displaystyle\;{\mathbb{E}}\_{x+h}\bigg[\int\_{0}^{\eta\_{0}\wedge\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +I{η0<τb}∫η0τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt]=VbE(x),x≥0,\displaystyle\quad\quad\quad\quad+I\{\eta\_{0}<\tau^{b}\}\int\_{\eta\_{0}}^{\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg]=V\_{b}^{E}(x),\ \ x\geq 0, |  | (C.25) |

where the last inequalities in ([C.24](https://arxiv.org/html/2510.27384v1#A3.E24 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([C.25](https://arxiv.org/html/2510.27384v1#A3.E25 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) both follow by noting α≤1\alpha\leq 1.

For any x>0x>0, let Xtx,bX\_{t}^{x,b} represent the controlled stochastic process d​Xtx,b=(μ​(Xtx,b)−l¯​I​{Xtx,b≥b})​d​t+σ​(Xt−x,b)​d​Wt\,\mathrm{d}X\_{t}^{x,b}=(\mu(X\_{t}^{x,b})-\bar{l}I\{X\_{t}^{x,b}\geq b\})\,\mathrm{d}t+\sigma(X\_{t-}^{x,b})\,\mathrm{d}W\_{t} with X0−x,b=xX\_{0-}^{x,b}=x. Now consider Xtx,bX\_{t}^{x,b} and Xtx+h,bX\_{t}^{x+h,b} with h>0h>0. By adapting the comparison theorem (Theorem 1.1 in Ikeda and Watanabe, ([1977](https://arxiv.org/html/2510.27384v1#bib.bib21))) we can show that with probability 11, Xtx+h,b≥Xtx,bX\_{t}^{x+h,b}\geq X\_{t}^{x,b} for all t≥0t\geq 0, and therefore, when Xtx+h,bX\_{t}^{x+h,b} produces excess emissions at the maximal rate l¯\bar{l}, Xtx,bX\_{t}^{x,b} may or may not produce excess emissions, and when it does, Xtx+h,bX\_{t}^{x+h,b} also generates excess emissiona at the same rate with probability 11.
As a result, by noting the expression of VbV\_{b} in terms of excess emission rates, we can observe Vb​(x)≤Vb​(x+h)V\_{b}(x)\leq V\_{b}(x+h) for h>0h>0 and thus, Vb′​(x)≥0V\_{b}^{\prime}(x)\geq 0 for x≥0x\geq 0.
It follows from ([3.3](https://arxiv.org/html/2510.27384v1#S3.E3 "In 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([4.5](https://arxiv.org/html/2510.27384v1#S4.E5 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (VbE​(x+h)−Vb​(x+h))−(VbE​(x)−Vb​(x))\displaystyle\left(V\_{b}^{E}(x+h)-V\_{b}(x+h)\right)-\left(V\_{b}^{E}(x)-V\_{b}(x)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (𝔼x+h[∫0τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt]\displaystyle\;\Bigg({\mathbb{E}}\_{x+h}\bigg[\int\_{0}^{\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼x+h[∫0η0∧τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt+∫η0∧τbτbαe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt])\displaystyle-{\mathbb{E}}\_{x+h}\bigg[\int\_{0}^{\eta\_{0}\wedge\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t+\int\_{\eta\_{0}\wedge\tau^{b}}^{\tau^{b}}\alpha e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg]\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(𝔼x[∫0τbe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt]\displaystyle-\Bigg({\mathbb{E}}\_{x}\bigg[\int\_{0}^{\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼x[∫0η0∧τbe−δ​t((γ−β)l¯I{Xtb≥b}dt+Λ)+∫η0∧τbτbαe−δ​t((γ−β)l¯I{Xtb≥b}+Λ)dt])\displaystyle-{\mathbb{E}}\_{x}\bigg[\int\_{0}^{\eta\_{0}\wedge\tau^{b}}e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}\,\mathrm{d}t+\Lambda)+\int\_{\eta\_{0}\wedge\tau^{b}}^{\tau^{b}}\alpha e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg]\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼x+h​[∫η0∧τbτb(1−α)​e−δ​t​((γ−β)​l¯​I​{Xtb≥b}+Λ)​dt]\displaystyle\;{\mathbb{E}}\_{x+h}\bigg[\int\_{\eta\_{0}\wedge\tau^{b}}^{\tau^{b}}(1-\alpha)e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼x​[∫η0∧τbτb(1−α)​e−δ​t​((γ−β)​l¯​I​{Xtb≥b}+Λ)​dt]\displaystyle-{\mathbb{E}}\_{x}\bigg[\int\_{\eta\_{0}\wedge\tau^{b}}^{\tau^{b}}(1-\alpha)e^{-\delta t}((\gamma-\beta)\bar{l}I\{X\_{t}^{b}\geq b\}+\Lambda)\,\mathrm{d}t\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (1−α)​(𝔼x+h​[e−δ​η0​I​{η0<τb}​VbE​(Xη0b)​d​t]−𝔼x​[e−δ​η0​I​{η0<τb}​VbE​(Xη0b)​d​t]),\displaystyle\;(1-\alpha)\left({\mathbb{E}}\_{x+h}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{b})\,\mathrm{d}t\bigg]-{\mathbb{E}}\_{x}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{b})\,\mathrm{d}t\bigg]\right), |  | (C.26) |

where the second to the last equality follows by first calculating the integrals into two mutually exclusive scenarios η0≥τb\eta\_{0}\geq\tau^{b} (which makes the integral 0) and η0<τb\eta\_{0}<\tau^{b}, and then applying the Markov property and using the definition for VbEV\_{b}^{E} in ([3.3](https://arxiv.org/html/2510.27384v1#S3.E3 "In 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

Let Xtx,bX\_{t}^{x,b} and Xtx+h,bX\_{t}^{x+h,b} be defined as before. We use τx,b\tau^{x,b} and τx+h,b\tau^{x+h,b} to represent the corresponding depletion times, respectively. We can observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x+h​[e−δ​η0​I​{η0<τb}​VbE​(Xη0b)​d​t]=𝔼​[e−δ​η0​I​{η0<τx+h,b}​VbE​(Xη0x+h,b)​d​t],\displaystyle{\mathbb{E}}\_{x+h}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{b})\,\mathrm{d}t\bigg]={\mathbb{E}}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{x+h,b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{x+h,b})\,\mathrm{d}t\bigg], |  | (C.27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x​[e−δ​η0​I​{η0<τb}​VbE​(Xη0b)​d​t]=𝔼​[e−δ​η0​I​{η0<τx,b}​VbE​(Xη0x,b)​d​t].\displaystyle{\mathbb{E}}\_{x}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{b})\,\mathrm{d}t\bigg]={\mathbb{E}}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{x,b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{x,b})\,\mathrm{d}t\bigg]. |  | (C.28) |

Using the same stochastic comparison argument as above, we know that
with probability 11, Xtx+h,b≥Xtx,bX\_{t}^{x+h,b}\geq X\_{t}^{x,b} for all t≥0t\geq 0, and thus τx+h,b≥τx,b\tau^{x+h,b}\geq\tau^{x,b} with probability 11. Note that η0\eta\_{0} is independent of {Xtx+h,b}\{X\_{t}^{x+h,b}\} and {Xtx,b}\{X\_{t}^{x,b}\} and thus, also independent of τx+h,b\tau^{x+h,b} and τx,b\tau^{x,b}. Further note that the function VbEV\_{b}^{E} is increasing. We can conclude that with probability 11, e−δ​η0​I​{η0<τx+h,b}​VbE​(Xη0x+h,b)≥e−δ​η0​I​{η0<τx,b}​VbE​(Xη0x,b)e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{x+h,b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{x+h,b})\geq e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{x,b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{x,b}). As a result,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[e−δ​η0​I​{η0<τx+h,b}​VbE​(Xη0x+h,b)​d​t]≥𝔼​[e−δ​η0​I​{η0<τx,b}​VbE​(Xη0x,b)​d​t].\displaystyle{\mathbb{E}}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{x+h,b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{x+h,b})\,\mathrm{d}t\bigg]\geq{\mathbb{E}}\bigg[e^{-\delta\eta\_{0}}I\{\eta\_{0}<\tau^{x,b}\}V\_{b}^{E}(X\_{\eta\_{0}}^{x,b})\,\mathrm{d}t\bigg]. |  | (C.29) |

This, along with ([C.26](https://arxiv.org/html/2510.27384v1#A3.E26 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))-([C.28](https://arxiv.org/html/2510.27384v1#A3.E28 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (VbE​(x+h)−Vb​(x+h))−(VbE​(x)−Vb​(x))≥0,x≥0,h>0,\displaystyle\left(V\_{b}^{E}(x+h)-V\_{b}(x+h)\right)-\left(V\_{b}^{E}(x)-V\_{b}(x)\right)\geq 0,\ \ x\geq 0,\ h>0, |  | (C.30) |

which further implies VbE′​(x)−Vb′​(x)≥0{V\_{b}^{E}}^{\prime}(x)-V\_{b}^{\prime}(x)\geq 0 for x≥0x\geq 0.
□\square

###### Lemma C.4

Let C1​(b)C\_{1}(b) be the same as that defined in ([C.22](https://arxiv.org/html/2510.27384v1#A3.E22 "In Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
For b≥0b\geq 0, suppose
either (a) μ​(0)≥0\mu(0)\geq 0, or (b) μ​(0)<0\mu(0)<0 and C1​(b)≤Λ−2​μ​(0)C\_{1}\,(b)\leq\frac{\Lambda}{-2\mu(0)}. (i) The function V0​(x)V\_{0}(x) is concave on [0,∞)[0,\infty). (ii) If Vb′​(b)=γ−βV\_{b}^{\prime}(b)=\gamma-\beta, then Vb​(x)V\_{b}(x) is concave on [0,∞)[0,\infty) and thus Vb′​(x)≥γ−βV\_{b}^{\prime}(x)\geq\gamma-\beta for x∈[0,b]x\in[0,b] and Vb′​(x)≤γ−βV\_{b}^{\prime}(x)\leq\gamma-\beta for x∈(b,∞)x\in(b,\infty).

Proof.  Note that Vb​(0)=0V\_{b}(0)=0, and Vb​(x)V\_{b}(x) is increasing and bounded.
We first show that there exists a positive sequence {xn}\{x\_{n}\} with limn→∞xn=∞\lim\_{n\rightarrow\infty}x\_{n}=\infty such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb′′​(xn)≤0.\displaystyle V^{\prime\prime}\_{b}(x\_{n})\leq 0. |  | (C.31) |

We follow the same idea as in Theorem 3.4 of Zhu, ([2015](https://arxiv.org/html/2510.27384v1#bib.bib47)), and use a proof by contradiction to prove ([C.31](https://arxiv.org/html/2510.27384v1#A3.E31 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
Suppose the contrary, that is, for some M>0M>0, Vb′′​(x)>0V\_{b}^{\prime\prime}(x)>0 for all x≥Mx\geq M. This implies Vb′​(x)>Vb′​(M)V\_{b}^{\prime}(x)>V\_{b}^{\prime}(M) for x>Mx>M and consequently, Vb​(x)>Vb​(M)+Vb′​(M)​(x−b)V\_{b}(x)>V\_{b}(M)+V\_{b}^{\prime}(M)(x-b) for x>Mx>M. By noting Vb′​(M)>0V\_{b}^{\prime}(M)>0 (due the strictly increasing property of VbV\_{b}), we conclude that Vb​(x)V\_{b}(x) converges to infinity when xx is infinitely large, which is a contradiction to the boundedness of VbV\_{b}.

Recall from ([C.14](https://arxiv.org/html/2510.27384v1#A3.E14 "In Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([C.15](https://arxiv.org/html/2510.27384v1#A3.E15 "In Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that for x≥0x\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​Vb′′​(x)+μ​(x)​Vb′​(x)−(λ+δ)​Vb​(x)+l¯​((γ−β)−Vb′​(x))​I​{x≥b}+λ​α​VbE​(x)+Λ=0.\displaystyle\frac{\sigma^{2}(x)}{2}V\_{b}^{\prime\prime}(x)+\mu(x)V\_{b}^{\prime}(x)-(\lambda+\delta)V\_{b}(x)+\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x\geq b\}+\lambda\alpha V^{E}\_{b}(x)+\Lambda=0. |  | (C.32) |

Letting x↓0x\downarrow 0 and noticing
Vb​(0)=0V\_{b}(0)=0 (see ([C.16](https://arxiv.org/html/2510.27384v1#A3.E16 "In Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))) and VbE​(0)=0V\_{b}^{E}(0)=0 (see Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")),we can obtain that for b≥0b\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(0)2​Vb′′​(0+)\displaystyle\frac{\sigma^{2}(0)}{2}V\_{b}^{\prime\prime}(0+) | =−μ​(0)​Vb′​(0+)−Λ\displaystyle=-\mu(0)V\_{b}^{\prime}(0+)-\Lambda |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤{0 if ​μ​(0)≥0,−μ​(0)​VbE′​(0+)−Λ≤0 if ​μ​(0)<0,ci​n​d​(b)≤Λ−2​μ​(0),\displaystyle\leq\begin{cases}0&\mbox{ if }\mu(0)\geq 0,\\ -\mu(0){V\_{b}^{E}}^{\prime}(0+)-\Lambda\leq 0&\mbox{ if }\mu(0)<0,c\_{ind}\,(b)\leq\frac{\Lambda}{-2\mu(0)},\end{cases} |  | (C.33) |

where the inequality in the first case above follows by the non-negativity of Vb′​(x)V\_{b}^{\prime}(x) due to the fact that VbV\_{b} is increasing, and in the second case, the second-to-last inequality follows by noting −μ​(0)>0-\mu(0)>0 and Vb′​(x)≤VbE′​(x)V\_{b}^{\prime}(x)\leq{V\_{b}^{E}}^{\prime}(x) for x>0x>0 (Lemma [C.3](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem3 "Lemma C.3 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and the last inequality follows by noticing VbE′​(0+)=2​C1​(b)≤Λ−μ​(0){V\_{b}^{E}}^{\prime}(0+)=2C\_{1}\,(b)\leq\frac{\Lambda}{-\mu(0)} (which can be obtained from the expression for VbEV\_{b}^{E} in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb′′​(0+)≤0,b≥0.\displaystyle V^{\prime\prime}\_{b}(0+)\leq 0,\ \ b\geq 0. |  | (C.34) |

Since Vb′​(b)=γ−βV\_{b}^{\prime}(b)=\gamma-\beta for b>0b>0, by Remark [C.1](https://arxiv.org/html/2510.27384v1#A3.ThmRemark1 "Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we know that for any b>0b>0,
Vb​(x)V\_{b}(x) is twice continuously differentiable on [0,∞)[0,\infty). For b=0b=0, we already know that V0​(x)V\_{0}(x) is twice continuously differentiable.

We now use proof by contradiction to show that for b≥0b\geq 0, Vb​(x)V\_{b}(x) is concave.
Suppose that the statement is not true. That is, for some b≥0b\geq 0, we can find y0>0y\_{0}>0 such that Vb′′​(y0)>0V^{\prime\prime}\_{b}(y\_{0})>0. Let {xn}\{x\_{n}\} be the sequence defined in the same way as before: limn→∞xn=∞\lim\_{n\rightarrow\infty}x\_{n}=\infty and Vb′′​(xn)≤0V^{\prime\prime}\_{b}(x\_{n})\leq 0. We can find a positive integer NN such that xN>y0x\_{N}>y\_{0}. By noting that Vb′′​(xN)≤0V^{\prime\prime}\_{b}(x\_{N})\leq 0, Vb′′​(0+)≤0V^{\prime\prime}\_{b}(0+)\leq 0 (from ([C.34](https://arxiv.org/html/2510.27384v1#A3.E34 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))), and Vb′′​(y0)>0V\_{b}^{\prime\prime}(y\_{0})>0 (the assumption made at the beginning of this proof by contradiction), and the continuity of Vb′′V\_{b}^{\prime\prime}, we conclude that there exists y1,y2y\_{1},y\_{2} with 0≤y1<y0<y2≤xN0\leq y\_{1}<y\_{0}<y\_{2}\leq x\_{N} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb′′​(y1)=0,Vb′′​(y2)=0,and ​Vb′′​(x)>0​ for x∈(y1,y2).\displaystyle V^{\prime\prime}\_{b}(y\_{1})=0,\ \ V^{\prime\prime}\_{b}(y\_{2})=0,\ \ \mbox{and }\ V^{\prime\prime}\_{b}(x)>0\ \mbox{ for $x\in(y\_{1},y\_{2})$.} |  | (C.35) |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb′​(y2)>Vb′​(y1).\displaystyle V^{\prime}\_{b}(y\_{2})>V^{\prime}\_{b}(y\_{1}). |  | (C.36) |

It follows by ([C.32](https://arxiv.org/html/2510.27384v1#A3.E32 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that for x≥0x\geq 0,

|  |  |  |
| --- | --- | --- |
|  | σ2​(x)2​Vb′′​(x)=((λ+δ)​Vb​(x)−μ​(x)​Vb′​(x)−l¯​((γ−β)−Vb′​(x))​I​{x≥b})−λ​α​VbE​(x)−Λ.\displaystyle\frac{\sigma^{2}(x)}{2}V\_{b}^{\prime\prime}(x)=\left((\lambda+\delta)V\_{b}(x)-\mu(x)V\_{b}^{\prime}(x)-\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x\geq b\}\right)-\lambda\alpha V\_{b}^{E}(x)-\Lambda. |  |

As Vb′​(b)=γ−βV\_{b}^{\prime}(b)=\gamma-\beta, we have l¯​((γ−β)−Vb′​(x))​I​{x≥b}=l¯​((γ−β)−Vb′​(x))​I​{x>b}\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x\geq b\}=\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x>b\}. Hence,
for x≥0x\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​Vb′′​(x)=((λ+δ)​Vb​(x)−μ​(x)​Vb′​(x)−l¯​((γ−β)−Vb′​(x))​I​{x>b})−λ​α​VbE​(x)−Λ.\displaystyle\frac{\sigma^{2}(x)}{2}V\_{b}^{\prime\prime}(x)=\left((\lambda+\delta)V\_{b}(x)-\mu(x)V\_{b}^{\prime}(x)-\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x>b\}\right)-\lambda\alpha V\_{b}^{E}(x)-\Lambda. |  | (C.37) |

By combining ([C.35](https://arxiv.org/html/2510.27384v1#A3.E35 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([C.37](https://arxiv.org/html/2510.27384v1#A3.E37 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we can obtain that for i=1,2i=1,2, and x∈(y1,y2)x\in(y\_{1},y\_{2}),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (λ+δ)​Vb​(yi)−μ​(yi)​Vb′​(yi)−l¯​((γ−β)−Vb′​(yi))​I​{yi>b}−λ​α​VbE​(yi)−Λ\displaystyle(\lambda+\delta)V\_{b}(y\_{i})-\mu(y\_{i})V\_{b}^{\prime}(y\_{i})-\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(y\_{i}))I\{y\_{i}>b\}-\lambda\alpha V\_{b}^{E}(y\_{i})-\Lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 12​σ2​(yi)​Vb′′​(yi)=0<12​σ2​(x)​Vb′′​(x),\displaystyle\frac{1}{2}\sigma^{2}(y\_{i})V\_{b}^{\prime\prime}(y\_{i})=0<\frac{1}{2}\sigma^{2}(x)V\_{b}^{\prime\prime}(x), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (λ+δ)​Vb​(x)−μ​(x)​Vb′​(x)−l¯​((γ−β)−Vb′​(x))​I​{x>b}−λ​α​VbE​(x)−Λ,\displaystyle(\lambda+\delta)V\_{b}(x)-\mu(x)V\_{b}^{\prime}(x)-\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x>b\}-\lambda\alpha V\_{b}^{E}(x)-\Lambda, |  | (C.38) |

which implies that for i=1,2i=1,2, and for x∈(y1,y2)x\in(y\_{1},y\_{2}),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (λ+δ)​Vb​(yi)−μ​(yi)​Vb′​(yi)−l¯​((γ−β)−Vb′​(yi))​I​{yi>b}−λ​α​VbE​(yi)\displaystyle(\lambda+\delta)V\_{b}(y\_{i})-\mu(y\_{i})V\_{b}^{\prime}(y\_{i})-\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(y\_{i}))I\{y\_{i}>b\}-\lambda\alpha V\_{b}^{E}(y\_{i}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | <\displaystyle< | (λ+δ)​Vb​(x)−μ​(x)​Vb′​(x)−l¯​((γ−β)−Vb′​(x))​I​{x>b}−λ​α​VbE​(x).\displaystyle(\lambda+\delta)V\_{b}(x)-\mu(x)V\_{b}^{\prime}(x)-\bar{l}((\gamma-\beta)-V\_{b}^{\prime}(x))I\{x>b\}-\lambda\alpha V\_{b}^{E}(x). |  | (C.39) |

By dividing ([C.39](https://arxiv.org/html/2510.27384v1#A3.E39 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) by x−yix-y\_{i} and rearranging the terms, it follows that for x∈(y1,y2)x\in(y\_{1},y\_{2}),

|  |  |  |
| --- | --- | --- |
|  | (λ+δ)​Vb​(x)−Vb​(y1)x−y1+−μ​(x)​Vb′​(x)+μ​(y1)​Vb′​(y1)x−y1\displaystyle(\lambda+\delta)\frac{V\_{b}(x)-V\_{b}(y\_{1})}{x-y\_{1}}+\frac{-\mu(x)V\_{b}^{\prime}(x)+\mu(y\_{1})V\_{b}^{\prime}(y\_{1})}{x-y\_{1}} |  |
|  |  |  |
| --- | --- | --- |
|  | +l¯​(Vb′​(x)−(γ−β))​I​{x>b}−(Vb′​(y1)−(γ−β))​I​{y1>b}x−y1−λ​α​VbE​(x)−VbE​(y1)x−y1>0,\displaystyle+\bar{l}\frac{(V\_{b}^{\prime}(x)-(\gamma-\beta))I\{x>b\}-(V\_{b}^{\prime}(y\_{1})-(\gamma-\beta))I\{y\_{1}>b\}}{x-y\_{1}}-\lambda\alpha\frac{V\_{b}^{E}(x)-V\_{b}^{E}(y\_{1})}{x-y\_{1}}>0, |  |
|  |  |  |
| --- | --- | --- |
|  | δ​Vb​(x)−Vb​(y2)x−y2+−μ​(x)​Vb′​(x)+μ​(y2)​Vb′​(y2)x−y2\displaystyle\delta\frac{V\_{b}(x)-V\_{b}(y\_{2})}{x-y\_{2}}+\frac{-\mu(x)V\_{b}^{\prime}(x)+\mu(y\_{2})V\_{b}^{\prime}(y\_{2})}{x-y\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +l¯​(Vb′​(x)−(γ−β))​I​{x>b}−(Vb′​(y2)−(γ−β))​I​{y2>b}x−y2−λ​α​VbE​(x)−VbE​(y2)x−y2<0.\displaystyle+\bar{l}\frac{(V\_{b}^{\prime}(x)-(\gamma-\beta))I\{x>b\}-(V\_{b}^{\prime}(y\_{2})-(\gamma-\beta))I\{y\_{2}>b\}}{x-y\_{2}}-\lambda\alpha\frac{V\_{b}^{E}(x)-V\_{b}^{E}(y\_{2})}{x-y\_{2}}<0. |  |

By letting x↓y1x\downarrow y\_{1} and x↑y2x\uparrow y\_{2} in the above two equations respectively, we can obtain

|  |  |  |
| --- | --- | --- |
|  | (λ+δ)​Vb′​(y1)−μ​(y1)​Vb′′​(y1)−μ′​(y1)​Vb′​(y1)+l¯​Vb′′​(y1)​I​{y1>b}−λ​α​VbE′​(y1)≥0,\displaystyle(\lambda+\delta)V\_{b}^{\prime}(y\_{1})-\mu(y\_{1})V\_{b}^{\prime\prime}(y\_{1})-\mu^{\prime}(y\_{1})V\_{b}^{\prime}(y\_{1})+\bar{l}V\_{b}^{\prime\prime}(y\_{1})I\{y\_{1}>b\}-\lambda\alpha{V\_{b}^{E}}^{\prime}(y\_{1})\geq 0, |  |
|  |  |  |
| --- | --- | --- |
|  | (λ+δ)​Vb′​(y2)−μ​(y2)​Vb′′​(y2)−μ′​(y2)​Vb′​(y2)+l¯​Vb′′​(y2)​I​{y2>b}−λ​α​VbE′​(y2)≤0.\displaystyle(\lambda+\delta)V\_{b}^{\prime}(y\_{2})-\mu(y\_{2})V\_{b}^{\prime\prime}(y\_{2})-\mu^{\prime}(y\_{2})V\_{b}^{\prime}(y\_{2})+\bar{l}V\_{b}^{\prime\prime}(y\_{2})I\{y\_{2}>b\}-\lambda\alpha{V\_{b}^{E}}^{\prime}(y\_{2})\leq 0. |  |

Therefore, by noting Vb′′​(y1)=0=Vb′′​(y2)V\_{b}^{\prime\prime}(y\_{1})=0=V\_{b}^{\prime\prime}(y\_{2}) (see ([C.35](https://arxiv.org/html/2510.27384v1#A3.E35 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (λ+δ−μ′​(y1))​Vb′​(y1)−λ​α​VbE′​(y1)≥0≥(λ+δ−μ′​(y2))​Vb′​(y2)−λ​α​VbE′​(y2).\displaystyle(\lambda+\delta-\mu^{\prime}(y\_{1}))V\_{b}^{\prime}(y\_{1})-\lambda\alpha{V\_{b}^{E}}^{\prime}(y\_{1})\geq 0\geq(\lambda+\delta-\mu^{\prime}(y\_{2}))V\_{b}^{\prime}(y\_{2})-\lambda\alpha{V\_{b}^{E}}^{\prime}(y\_{2}). |  | (C.40) |

Note that the increasing property of VbV\_{b} and ([C.36](https://arxiv.org/html/2510.27384v1#A3.E36 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤Vb′​(y1)<Vb′​(y2).\displaystyle 0\leq V\_{b}^{\prime}(y\_{1})<V\_{b}^{\prime}(y\_{2}). |  | (C.41) |

Recall that we are under the assumption that VbE′​(b)=γ−β{V\_{b}^{E}}^{\prime}(b)=\gamma-\beta for b>0b>0. It follows from Lemma [C.3](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem3 "Lemma C.3 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that VbE′​(b)≥Vb′​(b)=γ−β{V\_{b}^{E}}^{\prime}(b)\geq V\_{b}^{\prime}(b)=\gamma-\beta when b>0b>0, and then from Lemma [A.2](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem2 "Lemma A.2 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")(ii) that when b>0b>0, VbE′′​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)\leq 0 for x>0x>0. For b=0b=0, we know from Lemma [A.2](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem2 "Lemma A.2 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")(i) that VbE′′​(x)=V0E​(x)≤0{V\_{b}^{E}}^{\prime\prime}(x)=V\_{0}^{E}(x)\leq 0 for x>0x>0. These imply that for b≥0b\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VbE′​(y1)≥VbE′​(y2).\displaystyle{V\_{b}^{E}}^{\prime}(y\_{1})\geq{V\_{b}^{E}}^{\prime}(y\_{2}). |  | (C.42) |

Since μ′​(x)≤δ\mu^{\prime}(x)\leq\delta and μ\mu is concave, by using ([C.42](https://arxiv.org/html/2510.27384v1#A3.E42 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([C.41](https://arxiv.org/html/2510.27384v1#A3.E41 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we can obtain (λ+δ−μ′​(y1))​Vb′​(y1)−λ​α​VbE′​(y1)<(λ+δ−μ′​(y2))​Vb′​(y2)−λ​α​VbE′​(y2)(\lambda+\delta-\mu^{\prime}(y\_{1}))V\_{b}^{\prime}(y\_{1})-\lambda\alpha{V\_{b}^{E}}^{\prime}(y\_{1})<(\lambda+\delta-\mu^{\prime}(y\_{2}))V\_{b}^{\prime}(y\_{2})-\lambda\alpha{V\_{b}^{E}}^{\prime}(y\_{2}), which contradicts ([C.40](https://arxiv.org/html/2510.27384v1#A3.E40 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). This completes the proof of concavity of Vb​(x)V\_{b}(x) in (i) and (ii).

For b>0b>0, since Vb′​(b)=γ−βV\_{b}^{\prime}(b)=\gamma-\beta and Vb​(x)V\_{b}(x) has been shown to be concave on [0,∞)[0,\infty), we get Vb′​(x)≥Vb′​(b)=γ−βV\_{b}^{\prime}(x)\geq V\_{b}^{\prime}(b)=\gamma-\beta for x∈[0,b]x\in[0,b] and Vb′​(x)≤Vb′​(b)=γ−βV\_{b}^{\prime}(x)\leq V\_{b}^{\prime}(b)=\gamma-\beta for x∈(b,∞)x\in(b,\infty).
□\square

###### Lemma C.5

The following holds:
(i) 0≤b∗≤bE∗<∞0\leq b^{\*}\leq b^{\*}\_{E}<\infty, (ii) If b∗>0b^{\*}>0, then Vb∗′​(b∗)=γ−βV\_{b^{\*}}^{\prime}(b^{\*})=\gamma-\beta, Vb∗E′​(x)≥γ−β{V\_{b^{\*}}^{E}}^{\prime}(x)\geq\gamma-\beta for 0≤x<b∗0\leq x<b^{\*}, Vb∗E′​(x)≤γ−β{V\_{b^{\*}}^{E}}^{\prime}(x)\leq\gamma-\beta for x>b∗x>b^{\*}; and (iii) If b∗=0b^{\*}=0, then Vb∗′​(x)≤γ−βV\_{b^{\*}}^{\prime}(x)\leq\gamma-\beta for x≥0x\geq 0.

Proof.  (i) It is obvious from its definition that b∗≥0b^{\*}\geq 0. From Lemma [C.3](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem3 "Lemma C.3 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we know that Vb′​(x)≤VbE′​(x)V\_{b}^{\prime}(x)\leq{V\_{b}^{E}}^{\prime}(x) for x≥0x\geq 0. Hence, Vb′​(b)≤VbE′​(b)V\_{b}^{\prime}(b)\leq{V\_{b}^{E}}^{\prime}(b) for b≥0b\geq 0. Note that we have shown bE∗<∞b\_{E}^{\*}<\infty in Lemma [3.3](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem3 "Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") and so by the continuity of VbE′​(b){V\_{b}^{E}}^{\prime}(b) with respect to bb (see Lemma [A.1](https://arxiv.org/html/2510.27384v1#A1.ThmTheorem1 "Lemma A.1 ‣ Appendix A Proofs of Section 3 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and the definition of bE∗b\_{E}^{\*} in ([3.14](https://arxiv.org/html/2510.27384v1#S3.E14 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) we can obtain VbE∗E′​(bE∗)≤γ−β{V\_{b\_{E}^{\*}}^{E}}^{\prime}(b\_{E}^{\*})\leq\gamma-\beta. Therefore, VbE∗′​(bE∗)≤VbE∗E′​(bE∗)≤γ−βV\_{b\_{E}^{\*}}^{\prime}(b\_{E}^{\*})\leq{V\_{b\_{E}^{\*}}^{E}}^{\prime}(b\_{E}^{\*})\leq\gamma-\beta, which along with the definition of b∗b^{\*} in ([4.6](https://arxiv.org/html/2510.27384v1#S4.E6 "In Theorem 4.1 ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) implies b∗≤bE∗b^{\*}\leq b\_{E}^{\*}.

(ii)
Since b∗>0b^{\*}>0, it follows by its definition in ([4.6](https://arxiv.org/html/2510.27384v1#S4.E6 "In Theorem 4.1 ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and the continuity of Vb′​(b)V\_{b}^{\prime}(b) with respect to bb (see Lemma [C.2](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem2 "Lemma C.2 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")(iii)) that Vb∗′​(b∗)=γ−βV\_{b^{\*}}^{\prime}(b^{\*})=\gamma-\beta.

Note we have shown in Lemma [3.3](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem3 "Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that if μ​(0)<0\mu(0)<0, then bE∗≤b0b\_{E}^{\*}\leq b\_{0} and thus, in this case, b∗≤bE∗≤b0b^{\*}\leq b\_{E}^{\*}\leq b\_{0}. Recall the definition of b0b\_{0} in ([3.15](https://arxiv.org/html/2510.27384v1#S3.E15 "In Theorem 3.3 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")):
b0=inf{b≥0:C1​(b)+Λ2​μ​(0)>0}.b\_{0}=\inf\{b\geq 0:C\_{1}\,(b)+\frac{\Lambda}{2\mu(0)}>0\}. Hence,
C1​(b∗)+Λ2​μ​(0)≤0C\_{1}\,(b^{\*})+\frac{\Lambda}{2\mu(0)}\leq 0, that is, C1​(b∗)≤−Λ2​μ​(0)C\_{1}\,(b^{\*})\leq-\frac{\Lambda}{2\mu(0)}. In conclusion, in the case b∗>0b^{\*}>0, the following is guaranteed: either μ​(0)≥0\mu(0)\geq 0 or μ​(0)<0\mu(0)<0 and C1​(b∗)≤−Λ2​μ​(0)C\_{1}\,(b^{\*})\leq-\frac{\Lambda}{2\mu(0)}.
Then by applying Lemma [C.4](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem4 "Lemma C.4 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") (ii) we obtain Vb∗′​(x)≥γ−βV\_{b^{\*}}^{\prime}(x)\geq\gamma-\beta for x∈[0,b∗]x\in[0,b^{\*}] and Vb∗′​(x)<γ−βV\_{b^{\*}}^{\prime}(x)<\gamma-\beta for x∈[b∗,∞]x\in[b^{\*},\infty].

(iii) Since b∗=0b^{\*}=0, it follows by its definition in ([4.6](https://arxiv.org/html/2510.27384v1#S4.E6 "In Theorem 4.1 ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) that Vb∗′​(b∗)=V0′​(0)≤γ−βV\_{b^{\*}}^{\prime}(b^{\*})=V\_{0}^{\prime}(0)\leq\gamma-\beta. Note from Lemma [C.4](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem4 "Lemma C.4 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")(i) we know that Vb∗​(x)=V0​(x)V\_{b^{\*}}(x)=V\_{0}(x) is concave on [0,∞)[0,\infty). Therefore, Vb∗′​(x)≤Vb∗′​(0)≤γ−βV\_{b^{\*}}^{\prime}(x)\leq V\_{b^{\*}}^{\prime}(0)\leq\gamma-\beta for x≥0x\geq 0. □\square

Proof of Theorem [4.1](https://arxiv.org/html/2510.27384v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")
We have shown in Lemma [C.5](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem5 "Lemma C.5 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that 0≤b∗≤bE∗<∞0\leq b^{\*}\leq b^{\*}\_{E}<\infty.
Note 𝒫​(x;Lb∗,Lb∗)≤supL∈Π𝒫​(x;L,Lb∗)\mathcal{P}(x;L^{b^{\*}},L^{b^{\*}})\leq\sup\_{L\in\Pi}\mathcal{P}(x;L,L^{b^{\*}}). According to the definition of a MPE strategy, we can see that it is sufficient to show that
𝒫​(x;Lb∗,Lb∗)​(x)≥supL∈Π𝒫​(x;L,Lb∗),x≥0.\mathcal{P}(x;L^{b^{\*}},L^{b^{\*}})(x)\geq\sup\_{L\in\Pi}\mathcal{P}(x;L,L^{b^{\*}}),\ x\geq 0.

If b∗>0b^{\*}>0, then Vb∗′​(b∗)=γ−βV\_{b^{\*}}^{\prime}(b^{\*})=\gamma-\beta and thus by Remark [C.1](https://arxiv.org/html/2510.27384v1#A3.ThmRemark1 "Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we know that
Vb∗​(x)V\_{b^{\*}}(x) is twice continuously differentiable on [0,∞)[0,\infty), and it follows by Lemma [C.5](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem5 "Lemma C.5 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") that
Vb∗′​(x)≥γ−βV\_{b^{\*}}^{\prime}(x)\geq\gamma-\beta for x<b∗x<b^{\*} and Vb∗′​(x)≤γ−βV\_{b^{\*}}^{\prime}(x)\leq\gamma-\beta for x≥b∗x\geq b^{\*}.
If b∗=0b^{\*}=0, then Vb∗​(x)=V0​(x)V\_{b^{\*}}(x)=V\_{0}(x) is twice continuously differentiable. Moreover, by combining Lemma [C.5](https://arxiv.org/html/2510.27384v1#A3.ThmTheorem5 "Lemma C.5 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target") we have
V0′​(x)≤γ−βV\_{0}^{\prime}(x)\leq\gamma-\beta for x≥0x\geq 0. In summary, Vb∗​(x)V\_{b^{\*}}(x) is twice continuously differentiable on [0,∞)[0,\infty), and for b∗≥0b^{\*}\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb∗′​(x)≥γ−β​ for x<b∗,and ​Vb∗′​(x)≤γ−β​ for 0≤x≥b∗.\displaystyle V\_{b^{\*}}^{\prime}(x)\geq\gamma-\beta\mbox{ for $x<b^{\*}$},\quad\text{and\ \ }V\_{b^{\*}}^{\prime}(x)\leq\gamma-\beta\mbox{ for $0\leq x\geq b^{\*}$}. |  | (C.43) |

Let LL be any admissible strategy and define π¯sη0,L,Lb∗{\bar{\pi}^{\eta\_{0},L,L^{b^{\*}}}\_{s}} by d​π¯sη0,L,Lb∗=ls​I​{s<η0}​d​s+lsb∗​I​{s≥η0}​d​s\,\mathrm{d}{\bar{\pi}^{\eta\_{0},L,L^{b^{\*}}}\_{s}}=l\_{s}I\{s<\eta\_{0}\}\,\mathrm{d}s+l^{b^{\*}}\_{s}I\{s\geq\eta\_{0}\}\,\mathrm{d}s. For convenience, we use π¯{\bar{\pi}} to represent this strategy and use π¯s\bar{\pi}\_{s} to represent the excess emission rate throughout this proof. We can see that π¯{\bar{\pi}} is also admissible.
By applying Itô’s formula we can obtain that for any t>0t>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼x​[e−(λ+δ)​(τπ¯∧τn∧t)​Vb∗​(Xτπ¯∧τn∧tπ¯)]\displaystyle{\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)({\tau^{{\bar{\pi}}}\wedge\tau\_{n}\wedge t})}V\_{b^{\*}}(X^{{\bar{\pi}}}\_{\tau^{{\bar{\pi}}}\wedge\tau\_{n}\wedge t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Vb∗(x)+𝔼x[∫0τπ¯∧τn∧te−(λ+δ)​s(12σ2(Xsπ¯)Vb′′(Xsπ¯)+(μ(Xsπ¯)−π¯s)Vb∗′(Xsπ¯)\displaystyle V\_{b^{\*}}(x)+{\mathbb{E}}\_{x}\bigg[\int^{\tau^{{{\bar{\pi}}}}\wedge\tau\_{n}\wedge t}\_{0}e^{-(\lambda+\delta)s}\bigg(\frac{1}{2}\sigma^{2}(X^{{\bar{\pi}}}\_{s})V\_{b}^{\prime\prime}(X^{{\bar{\pi}}}\_{s})+\left(\mu(X^{{\bar{\pi}}}\_{s})-\bar{\pi}\_{s}\right)V\_{b^{\*}}^{\prime}(X^{{\bar{\pi}}}\_{s}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(λ+δ)Vb∗(Xsπ¯))ds].\displaystyle-(\lambda+\delta)V\_{b^{\*}}(X^{{\bar{\pi}}}\_{s})\bigg)\,\mathrm{d}s\bigg]. |  | (C.44) |

Since the function Vb∗V\_{b^{\*}} satisfies ([C.14](https://arxiv.org/html/2510.27384v1#A3.E14 "In Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([C.15](https://arxiv.org/html/2510.27384v1#A3.E15 "In Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 12​σ2​(Xsπ¯)​Vb∗′′​(Xsπ¯)+(μ​(Xsπ¯)−π¯s)​Vb∗′​(Xsπ¯)−(λ+δ)​Vb∗​(Xsπ¯)\displaystyle\frac{1}{2}\sigma^{2}(X^{{\bar{\pi}}}\_{s})V\_{b^{\*}}^{\prime\prime}(X^{{\bar{\pi}}}\_{s})+\left(\mu(X^{{\bar{\pi}}}\_{s})-\bar{\pi}\_{s}\right)V\_{b^{\*}}^{\prime}(X^{{\bar{\pi}}}\_{s})-(\lambda+\delta)V\_{b^{\*}}(X^{{\bar{\pi}}}\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | l¯​I​{Xsπ¯≥b∗}​Vb∗′​(Xsπ¯)−π¯s​Vb∗′​(Xsπ¯)−(γ−β)​l¯​I​{Xsπ¯≥b∗}−λ​α​Vb∗E​(Xsπ¯)−Λ\displaystyle\bar{l}I\{X^{{\bar{\pi}}}\_{s}\geq b^{\*}\}V\_{b^{\*}}^{\prime}(X^{{\bar{\pi}}}\_{s})-\bar{\pi}\_{s}V\_{b^{\*}}^{\prime}(X^{{\bar{\pi}}}\_{s})-(\gamma-\beta)\bar{l}I\{X^{{\bar{\pi}}}\_{s}\geq b^{\*}\}-\lambda\alpha V\_{b^{\*}}^{E}(X^{{\bar{\pi}}}\_{s})-\Lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (l¯−π¯s)​I​{Xsπ¯≥b∗}​Vb∗′​(Xsπ¯)−π¯s​Vb∗′​(Xsπ¯)​I​{Xsπ¯<b∗}−(γ−β)​l¯​I​{Xsπ¯≥b∗}−λ​α​Vb∗E​(Xsπ¯)−Λ\displaystyle(\bar{l}-\bar{\pi}\_{s})I\{X^{{\bar{\pi}}}\_{s}\geq b^{\*}\}V\_{b^{\*}}^{\prime}(X^{{\bar{\pi}}}\_{s})-\bar{\pi}\_{s}V\_{b^{\*}}^{\prime}(X^{{\bar{\pi}}}\_{s})I\{X^{{\bar{\pi}}}\_{s}<b^{\*}\}-(\gamma-\beta)\bar{l}I\{X^{{\bar{\pi}}}\_{s}\geq b^{\*}\}-\lambda\alpha V\_{b^{\*}}^{E}(X^{{\bar{\pi}}}\_{s})-\Lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (γ−β)​(l¯−π¯s)​I​{Xsπ¯≥b∗}−(γ−β)​π¯s​I​{Xsπ¯<b∗}−(γ−β)​l¯​I​{Xsπ¯≥b∗}−λ​α​Vb∗E​(Xsπ¯)−Λ\displaystyle(\gamma-\beta)(\bar{l}-\bar{\pi}\_{s})I\{X^{{\bar{\pi}}}\_{s}\geq b^{\*}\}-(\gamma-\beta)\bar{\pi}\_{s}I\{X^{{\bar{\pi}}}\_{s}<b^{\*}\}-(\gamma-\beta)\bar{l}I\{X^{{\bar{\pi}}}\_{s}\geq b^{\*}\}-\lambda\alpha V\_{b^{\*}}^{E}(X^{{\bar{\pi}}}\_{s})-\Lambda |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | −(γ−β)​π¯s−λ​α​Vb∗E​(Xsπ¯)−Λ,\displaystyle-(\gamma-\beta)\bar{\pi}\_{s}-\lambda\alpha V\_{b^{\*}}^{E}(X^{{\bar{\pi}}}\_{s})-\Lambda, |  | (C.45) |

where the last inequality follows by noting l¯−π¯s≥0\bar{l}-\bar{\pi}\_{s}\geq 0, Vb∗′​(x)≤(γ−β)V\_{b^{\*}}^{\prime}(x)\leq(\gamma-\beta) for x≥b∗x\geq b^{\*} and Vb∗′​(x)≥(γ−β)V\_{b^{\*}}^{\prime}(x)\geq(\gamma-\beta) for 0≤x<b∗0\leq x<b^{\*} (see ([C.43](https://arxiv.org/html/2510.27384v1#A3.E43 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))). Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb∗​(x)≥\displaystyle V\_{b^{\*}}(x)\geq | 𝔼x​[e−(λ+δ)​(τπ¯∧τn∧t)​Vb∗​(Xτπ¯∧τn∧tπ¯)]\displaystyle\;{\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)({\tau^{{\bar{\pi}}}\wedge\tau\_{n}\wedge t})}V\_{b^{\*}}(X^{{\bar{\pi}}}\_{\tau^{{\bar{\pi}}}\wedge\tau\_{n}\wedge t})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼x​[∫0τπ¯∧τn∧te−(λ+δ)​s​((γ−β)​π¯s+λ​α​Vb∗E​(Xsπ¯)+Λ)​ds].\displaystyle+{\mathbb{E}}\_{x}\bigg[\int^{\tau^{{{\bar{\pi}}}}\wedge\tau\_{n}\wedge t}\_{0}e^{-(\lambda+\delta)s}\bigg((\gamma-\beta)\bar{\pi}\_{s}+\lambda\alpha V\_{b^{\*}}^{E}(X^{{\bar{\pi}}}\_{s})+\Lambda\bigg)\,\mathrm{d}s\bigg]. |  | (C.46) |

Since the function Vb∗​(⋅)V\_{b^{\*}}(\cdot) is bounded, using dominated convergence twice we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞limn→∞𝔼x​[e−(λ+δ)​(τπ¯∧τn∧t)​Vb∗​(Xτπ¯∧τn∧tπ¯)]=𝔼x​[e−(λ+δ)​τπ¯​Vb∗​(Xτπ¯π¯)]=0,\displaystyle\lim\_{t\rightarrow\infty}\lim\_{n\rightarrow\infty}{\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)(\tau^{\bar{\pi}}\wedge\tau\_{n}\wedge t)}V\_{b^{\*}}(X^{\bar{\pi}}\_{\tau^{\bar{\pi}}\wedge\tau\_{n}\wedge t})\right]={\mathbb{E}}\_{x}\left[e^{-(\lambda+\delta)\tau^{\bar{\pi}}}V\_{b^{\*}}(X^{\bar{\pi}}\_{\tau^{\bar{\pi}}})\right]=0, |  | (C.47) |

where the last equality follows by noticing Xτπ¯π¯=0X^{{\bar{\pi}}}\_{\tau^{\bar{\pi}}}=0 and Vb∗​(0)=0V\_{b^{\*}}(0)=0.
By using the monotone convergence twice we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limt→∞limn→∞𝔼x​[∫0τπ¯∧τn∧te−(λ+δ)​s​(Λ+(γ−β)​π¯s)​ds]\displaystyle\lim\_{t\rightarrow\infty}\lim\_{n\rightarrow\infty}{\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}\wedge\tau\_{n}\wedge t}\_{0}e^{-(\lambda+\delta)s}(\Lambda+(\gamma-\beta)\bar{\pi}\_{s})\,\mathrm{d}s\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼x​[∫0τπ¯e−(λ+δ)​s​(Λ+(γ−β)​π¯s)​ds]=𝔼x​[∫0τπ¯∧η0e−δ​s​(Λ+(γ−β)​π¯s)​ds],\displaystyle\;{\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}}\_{0}e^{-(\lambda+\delta)s}(\Lambda+(\gamma-\beta)\bar{\pi}\_{s})\,\mathrm{d}s\right]={\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}\wedge\eta\_{0}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{\pi}\_{s})\,\mathrm{d}s\right], |  | (C.48) |

where the last equality follows from using (Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Eq.(A.1)). We then have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼x​[∫0τπ¯λ​α​e−(λ+δ)​s​Vb∗E​(Xsπ¯)​ds]=𝔼x​[α​e−δ​η0​Vb∗E​(Xη0π¯)​I​{η0≤τXπ¯}].\displaystyle{\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}}\_{0}\lambda\alpha e^{-(\lambda+\delta)s}V\_{b^{\*}}^{E}(X^{\bar{\pi}}\_{s})\,\mathrm{d}s\right]={\mathbb{E}}\_{x}\left[\alpha e^{-\delta\eta\_{0}}V\_{b^{\*}}^{E}(X^{\bar{\pi}}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{X^{\bar{\pi}}}\}\right]. |  | (C.49) |

By letting t→∞t\rightarrow\infty and n→∞n\rightarrow\infty on both sides of ([C.46](https://arxiv.org/html/2510.27384v1#A3.E46 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), and then using ([C.47](https://arxiv.org/html/2510.27384v1#A3.E47 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) - ([C.49](https://arxiv.org/html/2510.27384v1#A3.E49 "In Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we conclude
that for x≥0x\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb∗​(x)\displaystyle V\_{b^{\*}}(x) | ≥𝔼x​[∫0τπ¯∧η0e−δ​s​(Λ+(γ−β)​π¯s)​ds+α​e−δ​η0​Vb∗E​(Xη0π¯)​I​{η0≤τπ¯}]\displaystyle\geq{\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}\wedge\eta\_{0}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta)\bar{\pi}\_{s})\,\mathrm{d}s+\alpha e^{-\delta\eta\_{0}}V\_{b^{\*}}^{E}(X^{\bar{\pi}}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{\bar{\pi}}\}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼x​[∫0τπ¯∧η0e−δ​s​(Λ+(γ−β)​ls)​ds+α​e−δ​η0​Vb∗E​(Xη0π¯)​I​{η0≤τπ¯}]\displaystyle={\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}\wedge\eta\_{0}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta){l}\_{s})\,\mathrm{d}s+\alpha e^{-\delta\eta\_{0}}V\_{b^{\*}}^{E}(X^{\bar{\pi}}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{\bar{\pi}}\}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼x​[∫0τπ¯∧η0e−δ​s​(Λ+(γ−β)​ls)​ds+α​e−δ​η0​Vb∗E​(Xη0π¯)​I​{η0≤τπ¯}]\displaystyle={\mathbb{E}}\_{x}\left[\int^{\tau^{\bar{\pi}}\wedge\eta\_{0}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta){l}\_{s})\,\mathrm{d}s+\alpha e^{-\delta\eta\_{0}}V\_{b^{\*}}^{E}(X^{\bar{\pi}}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{\bar{\pi}}\}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼x​[∫0τL∧η0e−δ​s​(Λ+(γ−β)​ls)​ds+α​e−δ​η0​Vb∗E​(Xη0L)​I​{η0≤τL}]=𝒫​(x;L,Lb∗),\displaystyle={\mathbb{E}}\_{x}\left[\int^{\tau^{L\wedge\eta\_{0}}}\_{0}e^{-\delta s}(\Lambda+(\gamma-\beta){l}\_{s})\,\mathrm{d}s+\alpha e^{-\delta\eta\_{0}}V\_{b^{\*}}^{E}(X^{L}\_{\eta\_{0}})I\{\eta\_{0}\leq\tau^{L}\}\right]=\mathcal{P}(x;L,L^{b^{\*}}), |  |

where the second-to-last equality follows by noticing π¯s=ls\bar{\pi}\_{s}=l\_{s} for s<η0s<\eta\_{0} and the last equality by ([4.1](https://arxiv.org/html/2510.27384v1#S4.E1 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). By the arbitrariness of LL, we conclude Vb∗​(x)=𝒫​(x;L,Lb∗)V\_{b^{\*}}(x)=\mathcal{P}(x;L,L^{b^{\*}}) by virtue of Vb∗​(x)=𝒫​(x;Lb∗,Lb∗)​(x)V\_{b^{\*}}(x)=\mathcal{P}(x;L^{b^{\*}},L^{b^{\*}})(x) (see ([4.5](https://arxiv.org/html/2510.27384v1#S4.E5 "In 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))). Hence, the threshold strategy Lb∗L^{b^{\*}} is a Markov perfect equilibrium strategy, and the associated value function is Vb∗​(x){V\_{b^{\*}}}(x) for x≥0x\geq 0. The explicit expression for Vb∗​(x){V\_{b^{\*}}}(x) is readily available from Remark [C.1](https://arxiv.org/html/2510.27384v1#A3.ThmRemark1 "Remark C.1 ‣ Appendix C Proofs of Section 4 ‣ On effects of present-bias on carbon emission patterns towards a net zero target").
□\square

## Appendix D Derivations for Subsection [4.1](https://arxiv.org/html/2510.27384v1#S4.SS1 "4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")

Recall that Vb​(⋅)V\_{b}(\cdot) is the bounded and continuously differentiable
solution to the following equations:
σ22​g′′​(x)+μ​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+\mu g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+\Lambda=0 for 0<x<b,0<x<b, and σ22​g′′​(x)+(μ−l¯)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+(γ−β)​l¯+Λ=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+(\mu-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+(\gamma-\beta)\bar{l}+\Lambda=0 for
x>bx>b with g​(0)=0g(0)=0.
Note that eθ~1​xe^{\tilde{\theta}\_{1}x} and e−θ~2​xe^{-\tilde{\theta}\_{2}x} form a set of linearly independent solutions to σ22​g′′​(x)+μ​g′​(x)−(λ+δ)​g​(x)=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+\mu g^{\prime}(x)-(\lambda+\delta)g(x)=0.
Using the method of variation of parameters, we obtain P3​(x;b)P\_{3}(x;b) (see ([4.10](https://arxiv.org/html/2510.27384v1#S4.E10 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))) as a particular solution to σ22​g′′​(x)+μ​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+Λ=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+\mu g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+\Lambda=0:

|  |  |  |
| --- | --- | --- |
|  | P3​(x;b)=−eθ~1​x​2σ2​∫0x(λ​α​VbE​(s)+Λ)​e−θ~2​s(θ~1+θ~2)​e(θ~1−θ~2)​s​ds+e−θ~2​x​2σ2​∫0x(λ​α​VbE​(s)+Λ)​eθ~1​s(θ~1+θ~2)​e(θ~1−θ~2)​s​ds.P\_{3}(x;b)=-e^{\tilde{\theta}\_{1}x}\frac{2}{\sigma^{2}}\int\_{0}^{x}\frac{\left(\lambda\alpha V\_{b}^{E}(s)+\Lambda\right)e^{-\tilde{\theta}\_{2}s}}{(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})e^{(\tilde{\theta}\_{1}-\tilde{\theta}\_{2})s}}\mathrm{d}s+e^{-\tilde{\theta}\_{2}x}\frac{2}{\sigma^{2}}\int\_{0}^{x}\frac{\left(\lambda\alpha V\_{b}^{E}(s)+\Lambda\right)e^{\tilde{\theta}\_{1}s}}{(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})e^{(\tilde{\theta}\_{1}-\tilde{\theta}\_{2})s}}\mathrm{d}s. |  |

Similarly, a particular solution to σ22​g′′​(x)+(μ−l¯)​g′​(x)−(λ+δ)​g​(x)+λ​α​VbE​(x)+(γ−β)​l¯+Λ=0\frac{\sigma^{2}}{2}g^{\prime\prime}(x)+(\mu-\bar{l})g^{\prime}(x)-(\lambda+\delta)g(x)+\lambda\alpha V\_{b}^{E}(x)+(\gamma-\beta)\bar{l}+\Lambda=0 is given by P4​(x;b)P\_{4}(x;b):

|  |  |  |  |
| --- | --- | --- | --- |
|  | P4​(x;b)\displaystyle P\_{4}(x;b) | =−eθ~3​x​2σ2​∫0x(λ​α​VbE​(s)+Λ+(γ−β)​l¯)​e−θ~4​s(θ~3+θ~4)​e(θ~3−θ~4)​s​ds\displaystyle=-e^{\tilde{\theta}\_{3}x}\frac{2}{\sigma^{2}}\int\_{0}^{x}\frac{\left(\lambda\alpha V\_{b}^{E}(s)+\Lambda+(\gamma-\beta)\bar{l}\right)e^{-\tilde{\theta}\_{4}s}}{(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})e^{(\tilde{\theta}\_{3}-\tilde{\theta}\_{4})s}}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−θ~4​x​2σ2​∫0x(λ​α​VbE​(s)+Λ+(γ−β)​l¯)​eθ~3​s(θ~3+θ~4)​e(θ~3−θ~4)​s​ds.\displaystyle+e^{-\tilde{\theta}\_{4}x}\frac{2}{\sigma^{2}}\int\_{0}^{x}\frac{\left(\lambda\alpha V\_{b}^{E}(s)+\Lambda+(\gamma-\beta)\bar{l}\right)e^{\tilde{\theta}\_{3}s}}{(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})e^{(\tilde{\theta}\_{3}-\tilde{\theta}\_{4})s}}\mathrm{d}s. |  |

Therefore, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb​(x)={N1​(b)​eθ~1​x+N2​(b)​e−θ~2​x+P3​(x;b),0≤x<b,N3​(b)​eθ~3​x+N4​(b)​e−θ~4​x+P4​(x;b),x≥b,V\_{b}(x)=\begin{cases}N\_{1}(b)e^{\tilde{\theta}\_{1}x}+N\_{2}(b)e^{-\tilde{\theta}\_{2}x}+P\_{3}(x;b),&0\leq x<b,\\ N\_{3}(b)e^{\tilde{\theta}\_{3}x}+N\_{4}(b)e^{-\tilde{\theta}\_{4}x}+P\_{4}(x;b),&x\geq b,\end{cases} |  | (D.1) |

where N1​(b)−N4​(b)N\_{1}(b)-N\_{4}(b) are those fulfilling
Vb​(0)=N1​(b)+N2​(b)=0V\_{b}(0)=N\_{1}(b)+N\_{2}(b)=0 ,Vb​(b−)=Vb​(b+)V\_{b}(b-)=V\_{b}(b+), Vb′​(b−)=Vb′​(b+)V^{\prime}\_{b}(b-)=V^{\prime}\_{b}(b+), and Vb​(x)≤(γ−β)​l¯+Λδ​λ​α+δλ+δV\_{b}(x)\leq\frac{(\gamma-\beta)\bar{l}+\Lambda}{\delta}\frac{\lambda\alpha+\delta}{\lambda+\delta}.

From ([3.21](https://arxiv.org/html/2510.27384v1#S3.E21 "In 3.1 The Brownian motion model ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), we can rewrite VbE​(x)V\_{b}^{E}(x) as

|  |  |  |
| --- | --- | --- |
|  | VbE​(x)={M1​(b)​eθ1​x+M2​(b)​e−θ2​x+M3​(b),0≤x<b,M4​(b)​e−θ4​x+M5​(b),x≥b,V\_{b}^{E}(x)=\begin{cases}M\_{1}(b)e^{\theta\_{1}x}+M\_{2}(b)e^{-\theta\_{2}x}+M\_{3}(b),&0\leq x<b,\\ M\_{4}(b)e^{-\theta\_{4}x}+M\_{5}(b),&x\geq b,\end{cases} |  |

where M1​(b)−M5​(b)M\_{1}(b)-M\_{5}(b) are given in ([4.14](https://arxiv.org/html/2510.27384v1#S4.E14 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))-([4.16](https://arxiv.org/html/2510.27384v1#S4.E16 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). Note for 0≤x<b0\leq x<b,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0xVbE​(s)​e−θ~1​s​ds=\displaystyle\int\_{0}^{x}V\_{b}^{E}(s)e^{-\tilde{\theta}\_{1}s}\mathrm{d}s= | ∫0xM1​(b)​e−(θ~1−θ1)​s+M2​(b)​e−(θ~1+θ2)​s+M3​(b)​e−θ~1​s​d​s\displaystyle\int\_{0}^{x}M\_{1}(b)e^{-(\tilde{\theta}\_{1}-\theta\_{1})s}+M\_{2}(b)e^{-(\tilde{\theta}\_{1}+\theta\_{2})s}+M\_{3}(b)e^{-\tilde{\theta}\_{1}s}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | M1​(b)θ~1−θ1​(1−e−(θ~1−θ1)​x)+M2​(b)θ~1+θ2​(1−e−(θ~1+θ2)​x)+M3​(b)θ~1​(1−e−θ~1​x),\displaystyle\frac{M\_{1}(b)}{\tilde{\theta}\_{1}-\theta\_{1}}(1-e^{-(\tilde{\theta}\_{1}-\theta\_{1})x})+\frac{M\_{2}(b)}{\tilde{\theta}\_{1}+\theta\_{2}}(1-e^{-(\tilde{\theta}\_{1}+\theta\_{2})x})+\frac{M\_{3}(b)}{\tilde{\theta}\_{1}}(1-e^{-\tilde{\theta}\_{1}x}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0xVbE​(s)​eθ~2​s​ds=\displaystyle\int\_{0}^{x}V\_{b}^{E}(s)e^{\tilde{\theta}\_{2}s}\mathrm{d}s= | ∫0xM1​(b)​e(θ1+θ~2)​s+M2​(b)​e(θ~2−θ2)​s+M3​(b)​eθ~2​s​d​s\displaystyle\int\_{0}^{x}M\_{1}(b)e^{(\theta\_{1}+\tilde{\theta}\_{2})s}+M\_{2}(b)e^{(\tilde{\theta}\_{2}-\theta\_{2})s}+M\_{3}(b)e^{\tilde{\theta}\_{2}s}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | M1​(b)θ1+θ~2​(e(θ1+θ~2)​x−1)+M2​(b)θ~2−θ2​(e(θ~2−θ2)​x−1)+M3​(b)θ~2​(eθ~2​x−1).\displaystyle\frac{M\_{1}(b)}{\theta\_{1}+\tilde{\theta}\_{2}}(e^{(\theta\_{1}+\tilde{\theta}\_{2})x}-1)+\frac{M\_{2}(b)}{\tilde{\theta}\_{2}-\theta\_{2}}(e^{(\tilde{\theta}\_{2}-\theta\_{2})x}-1)+\frac{M\_{3}(b)}{\tilde{\theta}\_{2}}(e^{\tilde{\theta}\_{2}x}-1). |  |

Thus, we can obtain the expression for P3​(x;b)P\_{3}(x;b) as in ([4.10](https://arxiv.org/html/2510.27384v1#S4.E10 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), along with its derivative:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P3′​(x;b)=\displaystyle P\_{3}^{\prime}(x;b)= | 2​Λσ2​(θ~1+θ~2)​(−eθ~1​x+e−θ~2​x)−2​λ​ασ2​(θ~1+θ~2)​(θ~1​M1​(b)θ~1−θ1+θ~1​M2​(b)θ~1+θ2+M3​(b))​eθ~1​x\displaystyle\frac{2\Lambda}{\sigma^{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}(-e^{\tilde{\theta}\_{1}x}+e^{-\tilde{\theta}\_{2}x})-\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}\left(\frac{\tilde{\theta}\_{1}M\_{1}(b)}{\tilde{\theta}\_{1}-\theta\_{1}}+\frac{\tilde{\theta}\_{1}M\_{2}(b)}{\tilde{\theta}\_{1}+\theta\_{2}}+M\_{3}(b)\right)e^{\tilde{\theta}\_{1}x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​λ​ασ2​(θ~1+θ~2)​(θ~2​M1​(b)θ1+θ~2+θ~2​M2​(b)θ~2−θ2+M3​(b))​e−θ~2​x\displaystyle+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}\left(\frac{\tilde{\theta}\_{2}M\_{1}(b)}{\theta\_{1}+\tilde{\theta}\_{2}}+\frac{\tilde{\theta}\_{2}M\_{2}(b)}{\tilde{\theta}\_{2}-\theta\_{2}}+M\_{3}(b)\right)e^{-\tilde{\theta}\_{2}x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​λ​ασ2​(θ~1+θ~2)​[(M1​(b)θ~1−θ1+M1​(b)θ1+θ~2)​θ1​eθ1​x−(M2​(b)θ~1+θ2+M2​(b)θ~2−θ2)​θ2​e−θ2​x].\displaystyle+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{1}+\tilde{\theta}\_{2})}\left[\left(\frac{M\_{1}(b)}{\tilde{\theta}\_{1}-\theta\_{1}}+\frac{M\_{1}(b)}{\theta\_{1}+\tilde{\theta}\_{2}}\right)\theta\_{1}e^{\theta\_{1}x}-\left(\frac{M\_{2}(b)}{\tilde{\theta}\_{1}+\theta\_{2}}+\frac{M\_{2}(b)}{\tilde{\theta}\_{2}-\theta\_{2}}\right)\theta\_{2}e^{-\theta\_{2}x}\right]. |  |

In the same way, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | P4​(x;b)=\displaystyle P\_{4}(x;b)= | −2​((γ−β)​l¯+Λ)σ2​eθ~3​x−1θ~3​(θ~3+θ~4)+2​((γ−β)​l¯+Λ)σ2​1−e−θ~4​xθ~4​(θ~3+θ~4)+2​λ​ασ2​θ~3​θ~4​M5​(b)\displaystyle-\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{e^{\tilde{\theta}\_{3}x}-1}{\tilde{\theta}\_{3}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}+\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}}\frac{1-e^{-\tilde{\theta}\_{4}x}}{\tilde{\theta}\_{4}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}+\frac{2\lambda\alpha}{\sigma^{2}\tilde{\theta}\_{3}\tilde{\theta}\_{4}}M\_{5}(b) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −2​λ​ασ2​(θ~3+θ~4)​[(M4​(b)θ~3+θ4+M5​(b)θ~3)​eθ~3​x+(M4​(b)θ~4−θ4+M5​(b)θ~4)​e−θ~4​x]\displaystyle-\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left[\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{3}+\theta\_{4}}+\frac{M\_{5}(b)}{\tilde{\theta}\_{3}}\right)e^{\tilde{\theta}\_{3}x}+\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{4}-\theta\_{4}}+\frac{M\_{5}(b)}{\tilde{\theta}\_{4}}\right)e^{-\tilde{\theta}\_{4}x}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​λ​ασ2​(θ~3+θ~4)​(M4​(b)θ~3+θ4+M4​(b)θ~4−θ4)​e−θ4​x.\displaystyle+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{3}+\theta\_{4}}+\frac{M\_{4}(b)}{\tilde{\theta}\_{4}-\theta\_{4}}\right)e^{-\theta\_{4}x}. |  |

To ensure the boundedness of VbV\_{b}, we need the coefficient of eθ~3​xe^{\tilde{\theta}\_{3}x} in ([D.1](https://arxiv.org/html/2510.27384v1#A4.E1 "In Appendix D Derivations for Subsection 4.1 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) to be 0, which yields

|  |  |  |
| --- | --- | --- |
|  | N3​(b)=2​((γ−β)​l¯+Λ)σ2​θ~3​(θ~3+θ~4)+2​λ​ασ2​(θ~3+θ~4)​(M4​(b)θ~3+θ4+M5​(b)θ~3).N\_{3}(b)=\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}\tilde{\theta}\_{3}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{3}+\theta\_{4}}+\frac{M\_{5}(b)}{\tilde{\theta}\_{3}}\right). |  |

As a result, all the eθ~3​xe^{\tilde{\theta}\_{3}x} terms in VbV\_{b} disappear and the condition Vb​(0)=0V\_{b}(0)=0 implies N2​(b)=−N1​(b)N\_{2}(b)=-N\_{1}(b). Hence,

|  |  |  |
| --- | --- | --- |
|  | Vb​(x)={N1​(b)​eθ~1​x−N1​(b)​e−θ~2​x+P3​(x;b),0≤x<b,N4​(b)​e−θ~4​x+P5​(x;b),x≥b,V\_{b}(x)=\begin{cases}N\_{1}(b)e^{\tilde{\theta}\_{1}x}-N\_{1}(b)e^{-\tilde{\theta}\_{2}x}+P\_{3}(x;b),&0\leq x<b,\\ N\_{4}(b)e^{-\tilde{\theta}\_{4}x}+P\_{5}(x;b),&x\geq b,\end{cases} |  |

where P5​(x;b)P\_{5}(x;b) is given in ([4.11](https://arxiv.org/html/2510.27384v1#S4.E11 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).

With Vb​(b−)=Vb​(b+)V\_{b}(b-)=V\_{b}(b+) and Vb′​(b−)=Vb′​(b+)V\_{b}^{\prime}(b-)=V\_{b}^{\prime}(b+), we can solve N1​(b)N\_{1}(b) and N4​(b)N\_{4}(b) (see ([4.12](https://arxiv.org/html/2510.27384v1#S4.E12 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([4.13](https://arxiv.org/html/2510.27384v1#S4.E13 "In 4.1 The Brownian motion model ‣ 4 Equilibrium Solution under the Stochastic Quasi-Hyperbolic Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"))).
Note that

|  |  |  |
| --- | --- | --- |
|  | P5′​(x;b)=2​((γ−β)​l¯+Λ)σ2​(θ~3+θ~4)​e−θ~4​x+2​λ​ασ2​(θ~3+θ~4)​(θ~4​M4​(b)θ~4−θ4+M5​(b))​e−θ~4​x\displaystyle P\_{5}^{\prime}(x;b)=\frac{2((\gamma-\beta)\bar{l}+\Lambda)}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}e^{-\tilde{\theta}\_{4}x}+\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left(\frac{\tilde{\theta}\_{4}M\_{4}(b)}{\tilde{\theta}\_{4}-\theta\_{4}}+M\_{5}(b)\right)e^{-\tilde{\theta}\_{4}x} |  |
|  |  |  |
| --- | --- | --- |
|  | −2​λ​ασ2​(θ~3+θ~4)​(M4​(b)θ~3+θ4+M4​(b)θ~4−θ4)​θ4​e−θ4​x,\displaystyle\quad\quad\quad\quad\quad-\frac{2\lambda\alpha}{\sigma^{2}(\tilde{\theta}\_{3}+\tilde{\theta}\_{4})}\left(\frac{M\_{4}(b)}{\tilde{\theta}\_{3}+\theta\_{4}}+\frac{M\_{4}(b)}{\tilde{\theta}\_{4}-\theta\_{4}}\right)\theta\_{4}e^{-\theta\_{4}x}, |  |

and
Vb′​(b)=−θ~4​N4​(b)​e−θ~4​b+P5′​(b;b)V\_{b}^{\prime}(b)=-\tilde{\theta}\_{4}N\_{4}(b)e^{-\tilde{\theta}\_{4}b}+P\_{5}^{\prime}(b;b).
The threshold b∗b^{\*} can be obtained by solving −θ~4​N4​(b)​e−θ~4​b+P5′​(b;b)=γ−β-\tilde{\theta}\_{4}N\_{4}(b)e^{-\tilde{\theta}\_{4}b}+P\_{5}^{\prime}(b;b)={\gamma-\beta}.

## Appendix E Proofs of Section [5](https://arxiv.org/html/2510.27384v1#S5 "5 Probability of Early Depletion ‣ On effects of present-bias on carbon emission patterns towards a net zero target")

###### Lemma E.1

For any fixed ss, Lb~​(x;s)\widetilde{L^{b}}(x;s) is the unique continuously differentiable bounded solution to the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−s​g​(x)=0​ for 0<x<b∗,g​(0)=1,\displaystyle\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-sg(x)=0\mbox{ for $0<x<b^{\*}$},\quad g(0)=1, |  | (E.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−s​g​(x)+l¯​(γ−β)=0​ for x>b∗.\displaystyle\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-sg(x)+\bar{l}(\gamma-\beta)=0\mbox{ for $x>b^{\*}$}. |  | (E.2) |

Proof.  Following the same lines as in Lemma [3.1](https://arxiv.org/html/2510.27384v1#S3.ThmTheorem1 "Lemma 3.1 ‣ 3 Optimal Solutions under Exponential Discounting ‣ On effects of present-bias on carbon emission patterns towards a net zero target"), we can prove the existence and uniqueness of the stated solution by constructing a solution and then verifying its uniqueness.

Let gg represent the solution. Note that gg is continuously differentiable on (0,∞)(0,\infty) and it is not hard to see that gg is twice continuously differentiable on (0,b)∪(b,∞)(0,b)\cup(b,\infty) by expressing the second derivative in terms of the first derivative and the function itself by using ([E.1](https://arxiv.org/html/2510.27384v1#A5.E1 "In Lemma E.1 ‣ Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([E.2](https://arxiv.org/html/2510.27384v1#A5.E2 "In Lemma E.1 ‣ Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")). Recall that LbL^{b} represent the strategy with the production rate at time tt be ltb=l¯​I​{Xtb≥b}l\_{t}^{b}=\bar{l}I\{X\_{t}^{b}\geq b\}. Note the following dynamics for the optimally controlled process:
d​Xtb=(μ​(Xtb)−l¯​I​{Xtb≥b})​d​t+σ​(Xtb)​d​Wt\,\mathrm{d}X\_{t}^{b}=(\mu(X\_{t}^{b})-\bar{l}I\{X\_{t}^{b}\geq b\})\,\mathrm{d}t+\sigma(X\_{t}^{b})\,\mathrm{d}W\_{t} for t≥0.t\geq 0.
By applying (Zhu et al.,, [2020](https://arxiv.org/html/2510.27384v1#bib.bib48), Lemma A.1) we can obtain that for x≥0x\geq 0 and any t>0t>0, and for some sequence of stopping times {τn}\{\tau\_{n}\} with limn→∞τn=∞\lim\_{n\rightarrow\infty}\tau\_{n}=\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼x​[e−s​(τb∧t∧τn)​g​(Xτb∧t∧τnb)]\displaystyle\mathbb{E}\_{x}\bigg[e^{-s(\tau^{b}\wedge t\wedge{\tau\_{n}})}g(X^{b}\_{\tau^{b}\wedge t\wedge{\tau\_{n}}})\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | g​(x)+𝔼x​[∫0t∧τb∧tne−s​t​(12​σ2​(Xub)​g′′​(Xub)+(μ​(Xub)−l¯​I​{Xub≥bb})​g′​(Xub)−s​g​(Xub))​𝑑u]\displaystyle\;g(x)+\mathbb{E}\_{x}\bigg[\int\_{0}^{t\wedge\tau^{b}\wedge{t\_{n}}}e^{-st}\left(\frac{1}{2}\sigma^{2}(X\_{u}^{b})g^{\prime\prime}(X\_{u}^{b})+(\mu(X\_{u}^{b})-\bar{l}I\{X\_{u}^{b}\geq b^{b}\})g^{\prime}(X\_{u}^{b})-sg(X\_{u}^{b})\right)du\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | g​(x),\displaystyle\;g(x), |  | (E.3) |

where the last equality follows since gg satisfies ([E.1](https://arxiv.org/html/2510.27384v1#A5.E1 "In Lemma E.1 ‣ Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([E.2](https://arxiv.org/html/2510.27384v1#A5.E2 "In Lemma E.1 ‣ Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")).
Equation ([E.3](https://arxiv.org/html/2510.27384v1#A5.E3 "In Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)=\displaystyle g(x)= | 𝔼x​[e−s​τb​g​(Xτbb)​I​{t∧τn>τb}]+𝔼x​[e−s​(t∧τn)​g​(Xt∧τnb)​I​{t∧tn≤τb}]\displaystyle\mathbb{E}\_{x}\bigg[e^{-s\tau^{b}}g(X^{b}\_{\tau^{b}})I\{t\wedge\tau\_{n}>\tau^{b}\}\bigg]+\mathbb{E}\_{x}\bigg[e^{-s(t\wedge\tau\_{n})}g(X^{b}\_{t\wedge\tau\_{n}})I\{t\wedge t\_{n}\leq\tau^{b}\}\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼x​[e−s​τb​I​{t∧τn>τb}]+𝔼x​[e−s​(t∧τn)​g​(Xt∧τnb)​I​{t∧τn≤τb}],\displaystyle\mathbb{E}\_{x}\bigg[e^{-s\tau^{b}}I\{t\wedge\tau\_{n}>\tau^{b}\}\bigg]+\mathbb{E}\_{x}\bigg[e^{-s(t\wedge\tau\_{n})}g(X^{b}\_{t\wedge\tau\_{n}})I\{t\wedge\tau\_{n}\leq\tau^{b}\}\bigg], |  | (E.4) |

where the last equality is obtained by using g​(0)=1g(0)=1. Furthermore, gg is bounded and thus limn→∞limt→∞𝔼x​[e−s​(t∧τn)​g​(Xt∧τnb)​I​{t∧τn≤τb}]=0\lim\_{n\rightarrow\infty}\lim\_{t\rightarrow\infty}\mathbb{E}\_{x}\bigg[e^{-s(t\wedge\tau\_{n})}g(X^{b}\_{t\wedge\tau\_{n}})I\{t\wedge\tau\_{n}\leq\tau^{b}\}\bigg]=0. Therefore, by letting t→∞t\rightarrow\infty and n→∞n\rightarrow\infty (which implies τn→∞\tau\_{n}\rightarrow\infty) on both sides of ([E.4](https://arxiv.org/html/2510.27384v1#A5.E4 "In Appendix E Proofs of Section 5 ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) we arrive at g​(x)=𝔼x​[e−s​τb]=Lb​(x;s)g(x)=\mathbb{E}\_{x}\bigg[e^{-s\tau^{b}}\bigg]=L\_{b}(x;s) for x≥0.x\geq 0.
□\square

Proof of Theorem [5.1](https://arxiv.org/html/2510.27384v1#S5.ThmTheorem1 "Theorem 5.1 ‣ 5 Probability of Early Depletion ‣ On effects of present-bias on carbon emission patterns towards a net zero target").
For any ss, let v4​(⋅;s)v\_{4}(\cdot;s) and v5​(⋅;s)v\_{5}(\cdot;s) represent the solutions to
σ2​(x)2​g′′​(x)+μ​(x)​g′​(x)−s​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+\mu(x)g^{\prime}(x)-sg(x)=0, under the following two sets of initial values respectively,
v4​(0;s)=0v\_{4}(0;s)=0 and v4′​(0;s)=1v\_{4}^{\prime}(0;s)=1, and v5​(0;s)=1v\_{5}(0;s)=1, and v5′​(0;s)=1.v\_{5}^{\prime}(0;s)=1.
The existence and uniqueness of v4v\_{4} and v5v\_{5} are guaranteed by using Theorem 5.4.2. of Krylov, ([1996](https://arxiv.org/html/2510.27384v1#bib.bib25)).
Let v6​(x;s)v\_{6}(x;s) and u​(x;s)u(x;s) be bounded solutions to σ2​(x)2​g′′​(x)+(μ​(x)−l¯)​g′​(x)−s​g​(x)=0\frac{\sigma^{2}(x)}{2}g^{\prime\prime}(x)+(\mu(x)-\bar{l})g^{\prime}(x)-sg(x)=0 on [0,∞)[0,\infty) with initial value g​(0)=0g(0)=0 and g​(0)=1g(0)=1, respectively.
The existence of v6​(⋅;s)v\_{6}(\cdot;s) and u2​(⋅;s)u\_{2}(\cdot;s) can be proven by extending the differential equation to (−∞,−1)∪(0,∞)(-\infty,-1)\cup(0,\infty) and adding the boundary condition g​(−1)=1g(-1)=1, and then using Corollary 8.1 of Pao, ([1992](https://arxiv.org/html/2510.27384v1#bib.bib35)).
Therefore, Lb~​(x;s)\widetilde{L\_{b}}(x;s) can be determined by solving the above initial value problem, which has the following representation:

|  |  |  |
| --- | --- | --- |
|  | Lb~​(x;s)={C4​(b;s)​v4​(x;s)+C5​(b;s)​v5​(x;s)0≤x<b,C6​(b;s)​v6​(x;s)+u​(x;s)x≥b,\displaystyle\widetilde{L\_{b}}(x;s)=\left\{\begin{array}[]{ll}C\_{4}(b;s)v\_{4}(x;s)+C\_{5}(b;s)v\_{5}(x;s)&0\leq x<b,\\ C\_{6}(b;s)v\_{6}(x;s)+u(x;s)&x\geq b,\end{array}\right. |  |

where C4​(b;s)C\_{4}(b;s), C5​(b;s)C\_{5}(b;s), and C6​(b;s)C\_{6}(b;s)
are determined by solving the system
C4​(b;s)​v4​(0;s)+C5​(b;s)​v5​(0;s)=1C\_{4}(b;s)v\_{4}(0;s)+C\_{5}(b;s)v\_{5}(0;s)=1, C4​(b;s)​v4​(b;s)+C5​(b;s)​v5​(b;s)=C6​(b;s)​v6​(b;s)+u​(b;s)C\_{4}(b;s)v\_{4}(b;s)+C\_{5}(b;s)v\_{5}(b;s)=C\_{6}(b;s)v\_{6}(b;s)+u(b;s), and C4​(b;s)​v4′​(b;s)+C5​(b;s)​v5′​(b;s)=C6​(b;s)​v6′​(b;s)+u′​(b;s)C\_{4}(b;s)v\_{4}^{\prime}(b;s)+C\_{5}(b;s)v\_{5}^{\prime}(b;s)=C\_{6}(b;s)v\_{6}^{\prime}(b;s)+u^{\prime}(b;s), and we have the representations C5​(b;s)=1C\_{5}(b;s)=1, while the representations for C4​(b;s)C\_{4}(b;s) and C6​(b;s)C\_{6}(b;s) result from solving the system and are given in ([5.3](https://arxiv.org/html/2510.27384v1#S5.E3 "In Theorem 5.1 ‣ 5 Probability of Early Depletion ‣ On effects of present-bias on carbon emission patterns towards a net zero target")) and ([5.4](https://arxiv.org/html/2510.27384v1#S5.E4 "In Theorem 5.1 ‣ 5 Probability of Early Depletion ‣ On effects of present-bias on carbon emission patterns towards a net zero target")), respectively. □\square