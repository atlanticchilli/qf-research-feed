---
authors:
- Kim Weston
doc_id: arxiv:2601.07626v1
family_id: arxiv:2601.07626
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2601.07626v1
url_html: https://arxiv.org/html/2601.07626v1
venue: arXiv q-fin
version: 1
year: 2026
---

Universal basic income in a financial equilibrium

Kim Weston111Department of Mathematics, Rutgers University, Piscataway, NJ, 08854 USA (kw552@rutgers.edu).

Rutgers University

January 12, 2026

###### Abstract

Universal basic income (UBI) is a tax scheme that uniformly redistributes aggregate income amongst the entire population of an economy. We prove the existence of an equilibrium in a model that implements universal basic income. The economic agents choose the proportion of their time to work and earn wages that can be used towards consumption and investment in a financial market with a traded stock and annuity. A proportion of the earned wages is uniformly distributed amongst all agents, leading to interconnectedness of the agents’ decision problems, which are already dependent on one another through the financial market. The decision problems are further entangled by Nash perceptions of labor; the agents respond to the labor choices of others and act upon their perceived income in their decision problems. The equilibrium is constructed and proven to exist using a backward stochastic differential equation (BSDE) approach for a BSDE system with a quadratic structure that decouples. We analyze the effects of a universal basic income policy on labor market participation, the stock market, and welfare. While universal basic income policies affect labor market participation and welfare monotonically, its effects on the stock market are nontrivial and nonmonotone.

Keywords: Universal basic income; Financial equilibrium; Nash response functions; Labor-leisure choice problem; Backward stochastic differential equations

Mathematics Subject Classification (2020): 60G99, 60H30, 91B70, 91G80

JEL Classification: G12, D52, H23

## 1 Introduction

Universal basic income (UBI) policies are tax schemes that redistribute income amongst an entire population so that everyone receives an equal portion of aggregate income. Many local and regional governments have sought to alleviate poverty, encourage upward socioeconomic mobility, and dampen the effects of technological automation by means of UBI experiments222See for example, the works of Peetz et. al. [[11](https://arxiv.org/html/2601.07626v1#bib.bib48 "The role of income volatility and perceived locus of control in financial planning decisions")], Yang [[17](https://arxiv.org/html/2601.07626v1#bib.bib61 "The war on normal people: the truth about America’s disappearing jobs and why universal basic income is our future")], and Hughes [[6](https://arxiv.org/html/2601.07626v1#bib.bib34 "Fair shot: rethinking inequality and how we earn")].. Over the last two decades, notable trials of UBI have played out across dozens of regions across the globe with a high concentration of experiments in the US.

While economists, sociologists, and policy makers have overseen and analyzed UBI experiments, current research is limited to understanding individual impacts and region-wide questions of budgeting; see, for example, West et. al. [[14](https://arxiv.org/html/2601.07626v1#bib.bib8 "Recurring cash transfers to enhance the mental wellbeing of Americans")], Gertler et. al. [[5](https://arxiv.org/html/2601.07626v1#bib.bib30 "Investing cash transfers to raise long-term living standards")], and Kueng [[10](https://arxiv.org/html/2601.07626v1#bib.bib45 "Excess sensitivity of high-income consumers")]. UBI experiments suffer from three critical flaws: they are expensive, they take many months or years to play out, and they are small in scale. In particular, the expense leads to their small-scale nature, forcing UBI experiments to only directly benefit the sliver of low income individuals who win a lottery in order to receive basic income allotments. Such experiments are not truly universal, and they cannot address broader financial economic concerns. This work models universal basic income within a financial equilibrium in order to address questions that were previously unanswerable due to experimental limitations.

We propose a financial equilibrium model to study UBI with agents optimizing their labor market participation, running consumption, and investment in the stock market. The financial market consists of a stock with continuous stochastic dividends and an annuity with a continuous constant dividend stream of one. The presence of a traded annuity builds off the financial equilibrium work of Christensen and Larsen [[4](https://arxiv.org/html/2601.07626v1#bib.bib18 "Incomplete continuous-time securities markets with stochastic income volatility")], Weston and Žitković [[15](https://arxiv.org/html/2601.07626v1#bib.bib58 "An incomplete equilibrium with a stochastic annuity")], and Weston [[16](https://arxiv.org/html/2601.07626v1#bib.bib57 "Existence of an equilibrium with limited participation")].

The agents earn income by participating in the labor market with exogenously-specified wage rates. The labor choices of others impact all agents in two ways. First, they determine the aggregate income, which is partially redistributed to everyone as universal basic income. Second, the agents respond to others’ labor choices through Nash response functions, similar to those originally proposed for trading responses in Vayanos [[13](https://arxiv.org/html/2601.07626v1#bib.bib53 "Strategic trading and welfare in a dynamic market")] and used subsequently in Choi et. al. [[3](https://arxiv.org/html/2601.07626v1#bib.bib12 "Price impact in Nash equilibria")]. Response functions provide the mechanism for the agents to perceive how others will respond to their labor efforts. From perceived labor choices, the corresponding perceived income streams enter into each agent’s investment and consumption choice problem. Our response functions contain a free parameter, called the influence parameter, describing the influence of others on labor choices. The sign of the influence parameter impacts labor participation, the financial market, and welfare, showing that the Nash structure and its perceptions matter for the impact of UBI policies on equilibrium.

Labor-leisure problems study the trade-off between earning income by working in the labor market versus deriving pleasure from leisure time. Bodie et. al. [[2](https://arxiv.org/html/2601.07626v1#bib.bib3 "Labour supply flexibility and portfolio choice in a life cycle model")] studied the labor-leisure problem in a continuous-time single agent model, where the agent maximized expected utility from running consumption and leisure from not working. Basak [[1](https://arxiv.org/html/2601.07626v1#bib.bib1 "On the fluctuations in consumption and market returns in the presence of labor and human capital: an equilibrium analysis")] extended the work of Bodie et. al. [[2](https://arxiv.org/html/2601.07626v1#bib.bib3 "Labour supply flexibility and portfolio choice in a life cycle model")], placing labor-leisure problems in the context of a complete market financial equilibrium. The setting of Basak [[1](https://arxiv.org/html/2601.07626v1#bib.bib1 "On the fluctuations in consumption and market returns in the presence of labor and human capital: an equilibrium analysis")] is the most similar setting to this work, although it does not consider tax schemes like UBI or a Nash component to the labor choice problem. Kenc [[9](https://arxiv.org/html/2601.07626v1#bib.bib42 "Taxation, risk-taking and growth: a continuous-time stochastic general equilibrium analysis with labor-leisure choice")] studied the labor-leisure choice problem in a general equilibrium from the supply side and included tax scheme modeling.

The construction of an equilibrium relies on solving a characterizing BSDE system, similar to Weston and Žitković [[15](https://arxiv.org/html/2601.07626v1#bib.bib58 "An incomplete equilibrium with a stochastic annuity")] and Weston [[16](https://arxiv.org/html/2601.07626v1#bib.bib57 "Existence of an equilibrium with limited participation")]. We focus on a financial market that is essentially complete, so even though the characterizing BSDE system is coupled and quadratic, the quadratic terms are not coupled. This BSDE system is readily solvable using existing results.

We analyze the effects of universal basic income policies on labor participation, stock market effects, and welfare, and we compare pure socialist and pure communist economies in Section [4](https://arxiv.org/html/2601.07626v1#S4 "4 Universal Basic Income Effects"). The effects depend on both the amount of redistribution of income and the influence parameter that describes the agents’ labor perceptions. For a positive influence parameter, labor market participation decreases as income redistribution increases, but for negative influence parameter values, the opposite effect is achieved. Welfare effects are studied for the case when wage rates are positive constants. In this case, welfare behaves similarly to labor market participation; it is decreasing (increasing) when the amount of redistribution of income is increasing for positive (negative) influence parameter values.

The stock market effects are the most subtle. While closed-form expressions are provided to describe the market price of risk and interest rate coefficients that appear in a state price deflator, they are nonmonotone and highly nontrivial. An example is provided, highlighting some of the subtle variations in stock market effects due to UBI parameters.

The structure of the paper is as follows. Section [2](https://arxiv.org/html/2601.07626v1#S2 "2 Model setting") sets up the model and states the main theorem, Theorem [2.3](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Model setting"). Section [3](https://arxiv.org/html/2601.07626v1#S3 "3 Equilibrium construction") constructs an equilibrium by defining response functions, defining the characterizing BSDE system, and postulating optimal strategies. Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction") is a restatement of Theorem [2.3](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Model setting"), which states that an equilibrium exists and provides the details of its construction. Section [4](https://arxiv.org/html/2601.07626v1#S4 "4 Universal Basic Income Effects") describes the effects of universal basic income on labor market participation, the financial market, and welfare. Section [5](https://arxiv.org/html/2601.07626v1#S5 "5 Proofs") provides the proofs.

## 2 Model setting

We study a continuous-time financial equilibrium in a pure exchange economy with a fixed finite time horizon T<∞T<\infty. We let B=(Bt)t∈[0,T]B=(B\_{t})\_{t\in[0,T]} be a one-dimensional Brownian motion on the probability space (Ω,ℱ,ℙ)(\Omega,{\mathcal{F}},\mathbb{P}) equipped with the augmented Brownian filtration 𝔽=(ℱt)t∈[0,T]\mathbb{F}=({\mathcal{F}}\_{t})\_{t\in[0,T]}. We assume that ℱT=ℱ{\mathcal{F}}\_{T}={\mathcal{F}}. Throughout this work, equality (and inequality) between random variables is assumed to hold ℙ\mathbb{P}-a.s., and we suppress time from the notation when possible.

The set of all adapted, continuous, uniformly bounded processes is denoted by 𝒮∞{\mathcal{S}}^{\infty}. A martingale MM is said to be a BMO-martingale if there exists a constant C>0C>0 such that for all stopping times τ≤T\tau\leq T, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨M⟩T−⟨M⟩τ|ℱτ]≤C.\mathbb{E}\left[\langle M\rangle\_{T}-\langle M\rangle\_{\tau}\,|\,{\mathcal{F}}\_{\tau}\right]\leq C. |  |

In this case, we write M∈BMOM\in\text{BMO}. The collection of progressively measurable processes σ\sigma for which ∫0⋅σ​𝑑B\int\_{0}^{\cdot}\sigma dB is a BMO martingale is denoted by bmo. Background and details on BMO martingales can be found in Kazamaki [[8](https://arxiv.org/html/2601.07626v1#bib.bib41 "Continuous exponential martingales and bmo")].

Economic agents.
The economy consists of I<∞I<\infty agents who have the choice between consumption of the real good, investment in the financial market, and working (or not) in the formal labor workforce in order to earn income. Each agent faces a decision problem to decide simultaneously how much to consume, invest, and work. Consumption and labor occur at rates c=(ct)t∈[0,T]c=(c\_{t})\_{t\in[0,T]} and L=(Lt)t∈[0,T]L=(L\_{t})\_{t\in[0,T]}, respectively, per unit time and in a lump sum at time TT.

We model the agents’ decision problems using Cobb-Douglas utility functions. Each agent i=1,…,Ii=1,\ldots,I has constant parameters for risk aversion αi>0\alpha\_{i}>0, time preference ρi≥0\rho\_{i}\geq 0, and labor/leisure preferences ui:(0,1)→(0,∞)u\_{i}:(0,1)\rightarrow(0,\infty) that factor into the utility functions UiU\_{i} through

|  |  |  |
| --- | --- | --- |
|  | Ui​(t,c,l):=−exp⁡(−ρi​t−αi​c)​ui​(l),t∈[0,T],c∈ℝ,l∈(0,1).U\_{i}(t,c,l):=-\exp\left(-\rho\_{i}t-\alpha\_{i}c\right)u\_{i}(l),\quad t\in[0,T],\ c\in\mathbb{R},\ l\in(0,1). |  |

The labor/leisure preferences are given by ui​(l)=lβi​(1−l)γiu\_{i}(l)=l^{\beta\_{i}}(1-l)^{\gamma\_{i}} for l∈(0,1)l\in(0,1), where βi,γi<0\beta\_{i},\gamma\_{i}<0 so that uiu\_{i} is strictly convex (so that −ui-u\_{i} is strictly concave).

Consumption cc is allowed to be positive or negative, due to the exponential preferences for consumption. The proportion of time spent on labor must be valued in (0,1)(0,1). For every labor proportion l∈(0,1)l\in(0,1), the proportion of time spent on leisure is 1−l∈(0,1)1-l\in(0,1).

When an agent works in the labor market, she earns a wage that contributes to her total wealth. However, some of her wage is taxed, which is centrally collected and uniformly redistributed to everyone. The uniform redistribution of taxed funds is what we refer to as universal basic income. It is universal because everyone receives it and basic because nobody needs to work in the labor market in order to receive it. Every agent will keep the proportion λk​e​e​p∈[0,1]\lambda\_{keep}\in[0,1] of their earned labor income, and every agent will receive the proportion λu​b​iI\frac{\lambda\_{ubi}}{I} of the aggregate income, where λu​b​i∈[0,1−λk​e​e​p]\lambda\_{ubi}\in[0,1-\lambda\_{keep}]. We note that λk​e​e​p+λu​b​i≤1\lambda\_{keep}+\lambda\_{ubi}\leq 1. If λk​e​e​p+λu​b​i<1\lambda\_{keep}+\lambda\_{ubi}<1, then some of the economy’s earned labor income is lost, presumably as frictions or administrative costs that are not recycled back into the economy.

For each i=1,…,Ii=1,\ldots,I, agent ii has the ability to earn the wage wi=(wi,t)t∈[0,T]w\_{i}=(w\_{i,t})\_{t\in[0,T]} per unit time and in a lump sum at time TT. The wage rate wiw\_{i} has dynamics

|  |  |  |
| --- | --- | --- |
|  | d​wi=μwi​d​t+σwi​d​B,dw\_{i}=\mu\_{w\_{i}}dt+\sigma\_{w\_{i}}dB, |  |

where μwi,σwi∈𝒮∞\mu\_{w\_{i}},\sigma\_{w\_{i}}\in{\mathcal{S}}^{\infty}, are progressively measurable and uniformly bounded. The wage rate wiw\_{i} is assumed to be nonzero for all t∈[0,T]t\in[0,T] with probability one.

For each j=1,…,Ij=1,\ldots,I, we denote agent jj’s labor proportion as Lj=(Lj,t)t∈[0,T]L\_{j}=(L\_{j,t})\_{t\in[0,T]}, so agent ii’s income rate at time t∈[0,T]t\in[0,T] is

|  |  |  |
| --- | --- | --- |
|  | λk​e​e​p​wi,t​Li,t+λu​b​iI​∑j=1Iwj,t​Lj,t.\lambda\_{keep}w\_{i,t}L\_{i,t}+\frac{\lambda\_{ubi}}{I}\sum\_{j=1}^{I}w\_{j,t}L\_{j,t}. |  |

Labor response functions. We employ a Nash equilibrium concept in which markets must clear and the agents will act optimally, but the agents will also take into consideration others’ perceptions of their the labor choices when making their own choices. Each agent earns income by working, but a portion of that income is siphoned off and redistributed to everybody as UBI. Though the agents benefit from their own additional earnings, they also benefit from the labor earnings of others. Thus, others’ labor choices should have an impact on labor decisions. We model this impact by using exogenously defined response functions, similar to Vayanos [[13](https://arxiv.org/html/2601.07626v1#bib.bib53 "Strategic trading and welfare in a dynamic market")] and Chen et. al. [[3](https://arxiv.org/html/2601.07626v1#bib.bib12 "Price impact in Nash equilibria")]. Response functions provide one way of making others’ impact precise.

For each i,j=1,…,Ii,j=1,\ldots,I and j≠ij\neq i, the response function Λji=Λj,ti​(l)\Lambda^{i}\_{j}=\Lambda^{i}\_{j,t}(l) describes how agent ii perceives that agent jj’s labor choice changes according to agent ii’s choice of labor l∈(0,1)l\in(0,1) at time t∈[0,T]t\in[0,T]. We assume that Λji:[0,T]×(0,1)→ℝ\Lambda^{i}\_{j}:[0,T]\times(0,1)\rightarrow\mathbb{R} is measurable. Then, agent ii’s perceived income, based on agent ii’s choice of labor for l∈(0,1)l\in(0,1), is given by εi=εi​(l)\varepsilon\_{i}=\varepsilon\_{i}(l),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | εi,t​(l):=λk​e​e​p​wi,t​l\displaystyle\varepsilon\_{i,t}(l):=\lambda\_{keep}w\_{i,t}l | +λu​b​iI​(wi,t​l+∑j≠iwj,t​Λj,ti​(l)),t∈[0,T].\displaystyle+\frac{\lambda\_{ubi}}{I}\left(w\_{i,t}l+\sum\_{j\neq i}w\_{j,t}\Lambda^{i}\_{j,t}(l)\right),\quad t\in[0,T]. |  | (2.1) |

Below, in Definition [3.2](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem2 "Definition 3.2. ‣ 3 Equilibrium construction"), we consider affine responses.

The financial market.
The financial market consists of two securities: a stock and an annuity. Both securities are in one-net supply, and their prices are denominated in units of a single consumption good. The annuity pays a constant dividend stream of 11 per unit time and a lump sum of 11 at time TT. The stock pays a dividend of DtD\_{t} per unit time and a lump sum of DTD\_{T} at time TT. The dividend stream DD is an Itô process with dynamics given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Dt=μD​d​t+σD​d​B,D0∈ℝ,dD\_{t}=\mu\_{D}dt+\sigma\_{D}dB,\quad D\_{0}\in\mathbb{R}, |  | (2.2) |

where μD,σD∈𝒮∞\mu\_{D},\sigma\_{D}\in{\mathcal{S}}^{\infty}.

The stock and annuity prices will be determined endogenously in equilibrium as continuous semimartingles S=(St)t∈[0,T]S=(S\_{t})\_{t\in[0,T]} and A=(At)t∈[0,T]A=(A\_{t})\_{t\in[0,T]}, respectively. Their terminal values are their dividends

|  |  |  |
| --- | --- | --- |
|  | ST=DTandAT=1.S\_{T}=D\_{T}\quad\text{and}\quad A\_{T}=1. |  |

Our equilibrium prices AA and SS have dynamics of the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​A\displaystyle dA | =−d​t+A​(μA​d​t+σA​d​B),AT=1,\displaystyle=-dt+A\left(\mu\_{A}\,dt+\sigma\_{A}\,dB\right),\quad A\_{T}=1, |  | (2.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​S\displaystyle dS | =−Dt​d​t+(μS+S​μA)​d​t+(σS+S​σA)​d​B,ST=DT.\displaystyle=-D\_{t}\,dt+\left(\mu\_{S}+S\mu\_{A}\right)dt+\left(\sigma\_{S}+S\sigma\_{A}\right)dB,\quad S\_{T}=D\_{T}. |  | (2.4) |

The price processes and their dynamics are outputs of equilibrium. The coefficients μA\mu\_{A}, σA\sigma\_{A}, μS\mu\_{S}, and σS\sigma\_{S} must be progressively measurable and will be proven to have sufficient regularity for ([2.3](https://arxiv.org/html/2601.07626v1#S2.E3 "In 2 Model setting")) and ([2.4](https://arxiv.org/html/2601.07626v1#S2.E4 "In 2 Model setting")) to be well-defined.

The annuity plays the role of a zero-coupon bond when a zero-coupon bond trades in an economy with only terminal consumption. When the annuity’s volatility is zero, it can replicate a locally riskless security.

The number of shares held in the stock over time is denoted π=(πt)t∈[0,T]\pi=(\pi\_{t})\_{t\in[0,T]}, and number of shares held in the annuity over time is denoted θ=(θt)t∈[0,T]\theta=(\theta\_{t})\_{t\in[0,T]}. For given price processes SS and AA and a pair of positions (π,θ)(\pi,\theta), the associated wealth process X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} is defined by

|  |  |  |
| --- | --- | --- |
|  | X:=θ​A+π​S.X:=\theta A+\pi S. |  |

The agents can trade in both the stock and the annuity and are endowed with πi,0−∈ℝ\pi\_{i,0-}\in\mathbb{R} shares in the stock and θi,0−∈ℝ\theta\_{i,0-}\in\mathbb{R} shares in the annuity, i=1,…,Ii=1,\ldots,I. Since the stock and annuity are in one-net supply, we assume that ∑i=1Iθi,0−=1\sum\_{i=1}^{I}\theta\_{i,0-}=1 and ∑i=1Iπi,0−=1\sum\_{i=1}^{I}\pi\_{i,0-}=1.

###### Definition 2.1.

Let i∈{1,…,I}i\in\{1,\ldots,I\} be given. For a given labor process LL that is progressively measurable and (0,1)(0,1)-valued, we say that the triple of strategies (π,θ,c)(\pi,\theta,c) is admissible for agent ii with labor process LL if π\pi, θ\theta, and cc are progressively measurable and

1. 1.

   The processes LL, π\pi, θ\theta, and cc satisfy

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫0T\displaystyle\int\_{0}^{T} | (|πt|​(|μS,t|+|St​μA,t|)+|πt|2​(|σS,t|2+|St​σA,t|2))​d​t<∞,and\displaystyle\big(|\pi\_{t}|\left(|\mu\_{S,t}|+|S\_{t}\mu\_{A,t}|\right)+|\pi\_{t}|^{2}\left(|\sigma\_{S,t}|^{2}+|S\_{t}\sigma\_{A,t}|^{2}\right)\big)dt<\infty,\quad\text{and} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫0T\displaystyle\int\_{0}^{T} | (|μA,tθt|+|σA,tθt|2+|ct|+|εi,t(Lt)|)dt<∞.\displaystyle\big(|\mu\_{A,t}\theta\_{t}|+|\sigma\_{A,t}\theta\_{t}|^{2}+|c\_{t}|+|\varepsilon\_{i},t(L\_{t})|\big)dt<\infty. |  |
2. 2.

   The associated wealth process X:=θ​A+π​SX:=\theta A+\pi S satisfies the self-financing condition:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | d​X=θ​(d​A+d​t)+π​(d​S+D​d​t)+εi​(L)​d​t−c​d​t.\displaystyle dX=\theta(dA+dt)+\pi(dS+D\,dt)+\varepsilon\_{i}(L)\,dt-c\,dt. |  | (2.5) |
3. 3.

   The process V=(Vt)t∈[0,T]V=(V\_{t})\_{t\in[0,T]} given by
   Vt=−exp⁡(−ρi​t−αi​(Xt/At+Yi,t))−∫0te−ρi​s−αi​cs​ui​(Ls)​𝑑sV\_{t}=-\exp\big(-\rho\_{i}t-\alpha\_{i}\big(X\_{t}/A\_{t}+Y\_{i,t})\big)-\int\_{0}^{t}e^{-\rho\_{i}s-\alpha\_{i}c\_{s}}u\_{i}(L\_{s})ds is an Itô process, and its local martingale component is a martingale. Here, the process YiY\_{i} is a component of the unique solution to the BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")) below.

If (π,θ,c)(\pi,\theta,c) is admissible for agent ii with labor process LL, then we write (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L).

###### Definition 2.2.

Let λk​e​e​p∈[0,1]\lambda\_{keep}\in[0,1], λu​b​i∈[0,1−λk​e​e​p]\lambda\_{ubi}\in[0,1-\lambda\_{keep}] be given. Strategies πi,θi,ci,Li\pi\_{i},\theta\_{i},c\_{i},L\_{i}, i=1,…,Ii=1,\ldots,I, response functions Λji\Lambda^{i}\_{j}, i,j=1,…,Ii,j=1,\ldots,I with i≠ji\neq j, and continuous semimartingales AA and SS form an equilibrium if

1. 1.

   Optimality: For each i=1,…,Ii=1,\ldots,I, we have that πi\pi\_{i}, θi\theta\_{i}, cic\_{i}, and LiL\_{i} solve

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supπ,θ,c,L𝔼​[∫0TUi​(t,ct,Lt)​𝑑t+Ui​(T,XT+εi,T​(LT),LT)],\displaystyle\sup\_{\pi,\theta,c,L}\mathbb{E}\left[\int\_{0}^{T}U\_{i}(t,c\_{t},L\_{t})dt+U\_{i}\big(T,X\_{T}+\varepsilon\_{i,T}(L\_{T}),L\_{T}\big)\right], |  | (2.6) |

   where the supremum is taken over progressively measurable (0,1)(0,1)-valued processes LL and (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L). Here, the perceived income process εi​(L)\varepsilon\_{i}(L) is given by ([2.1](https://arxiv.org/html/2601.07626v1#S2.E1 "In 2 Model setting")).
2. 2.

   Consistency of optimizers: For all t∈[0,T]t\in[0,T] and each i,j=1,…,Ii,j=1,\ldots,I with i≠ji\neq j, we have Λj,ti​(Li,t)=Lj,t\Lambda^{i}\_{j,t}(L\_{i,t})=L\_{j,t}.
3. 3.

   On-equilibrium perceptions align with reality:
   For all t∈[0,T]t\in[0,T],

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1Iεi,t​(Li,t)=(λk​e​e​p+λu​b​i)​∑i=1Iwi,t​Li,t.\sum\_{i=1}^{I}\varepsilon\_{i,t}(L\_{i,t})=\left(\lambda\_{keep}+\lambda\_{ubi}\right)\sum\_{i=1}^{I}w\_{i,t}L\_{i,t}. |  |
4. 4.

   Market clearing: For all t∈[0,T]t\in[0,T], we have

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1Iπi,t=1,∑i=1Iθi,t=1,and∑i=1Ici,t=1+Dt+∑i=1Iεi,t​(Li,t).\displaystyle\sum\_{i=1}^{I}\pi\_{i,t}=1,\quad\sum\_{i=1}^{I}\theta\_{i,t}=1,\quad\text{and}\quad\sum\_{i=1}^{I}c\_{i,t}=1+D\_{t}+\sum\_{i=1}^{I}\varepsilon\_{i,t}(L\_{i,t}). |  |

The definition of equilibrium incorporates optimally choosing a proportion of time to work in the labor market with optimizing holdings in the financial market and running consumption, where income earned via wages from the labor market is treated as income available in the financial market. In the optimization problem ([2.6](https://arxiv.org/html/2601.07626v1#S2.E6 "In item 1 ‣ Definition 2.2. ‣ 2 Model setting")), requiring (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L) means that the income stream being optimized over is εi​(L)\varepsilon\_{i}(L).

The labor perceptions Λji​(l)\Lambda\_{j}^{i}(l) are agent ii’s perception of jj’s reaction to ii’s choice of labor. The consistency requirement Λji​(Li)=Lj\Lambda^{i}\_{j}(L\_{i})=L\_{j} means that agent ii perceives that jj responds to ii’s optimal labor choice with his own optimal labor choice. The consistency requirement also guarantees that the on-equilibrium labor choice Λji​(Li)\Lambda\_{j}^{i}(L\_{i}) is (0,1)(0,1)-valued, whereas there is no such requirement off-equilibrium.

Our main result is Theorem [2.3](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Model setting"), which establishes the existence of an equilibrium. The equilibrium construction is contained in Section [3](https://arxiv.org/html/2601.07626v1#S3 "3 Equilibrium construction"), culminating in Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction"), which implements Theorem [2.3](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Model setting"). The proof is in Section [5](https://arxiv.org/html/2601.07626v1#S5 "5 Proofs").

###### Theorem 2.3.

Assume that the wage rates are nonzero for all t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s., and that for the dividend and wage rate dynamics coefficients, we have μD,σD,μwi,σwi∈𝒮∞\mu\_{D},\sigma\_{D},\mu\_{w\_{i}},\sigma\_{w\_{i}}\in{\mathcal{S}}^{\infty} for i=1,…,Ii=1,\ldots,I. For any λk​e​e​p∈[0,1]\lambda\_{keep}\in[0,1] and λu​b​i∈[0,1−λk​e​e​p]\lambda\_{ubi}\in[0,1-\lambda\_{keep}], there exists an equilibrium.

## 3 Equilibrium construction

To construct an equilibrium, we begin by making two conjectures. First, we conjecture the agents’ optimal labor proportions using only model input paramenters. Second, we conjecture that affine response functions are sufficient for constructing and proving the existence of an equilibrium. Given the candidate optimal labor proportions and their corresponding income streams, we construct the equilibrium financial market. Finally, using these conjectures, we prove in Section [5](https://arxiv.org/html/2601.07626v1#S5 "5 Proofs") that equilibrium exists by solving a characterizing BSDE system and perform verification.

The labor market. The candidate labor proportion processes L1,…,LIL\_{1},\ldots,L\_{I} are defined below and depend only on input parameters and a constant free parameter δ∈ℝ\delta\in\mathbb{R}, called the influence parameter.

###### Definition 3.1.

For δ∈ℝ\delta\in\mathbb{R} and for each i=1,…,Ii=1,\ldots,I, the process Li=(Li,t)t∈[0,T]L\_{i}=(L\_{i,t})\_{t\in[0,T]} is chosen for each t∈[0,T]t\in[0,T] as the unique value in (0,1)(0,1) such that

|  |  |  |
| --- | --- | --- |
|  | αi​wi,t​(λk​e​e​p+λu​b​iI​(1+δ​(I−1)))=ui′​(Li,t)ui​(Li,t).\alpha\_{i}w\_{i,t}\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}\big(1+\delta(I-1)\big)\right)=\frac{u\_{i}^{\prime}(L\_{i,t})}{u\_{i}(L\_{i,t})}. |  |

For each i=1,…,Ii=1,\ldots,I, the process LiL\_{i} is an Itô process with dynamics

|  |  |  |
| --- | --- | --- |
|  | d​Li=μLi​d​t+σLi​d​B.dL\_{i}=\mu\_{L\_{i}}dt+\sigma\_{L\_{i}}dB. |  |

Furthermore, we denote the processes ℒi{\mathcal{L}}\_{i} and ℒΣ{\mathcal{L}}\_{\Sigma} by ℒi:=1αi​log⁡ui​(Li){\mathcal{L}}\_{i}:=\frac{1}{\alpha\_{i}}\log u\_{i}(L\_{i}) and ℒΣ:=∑i=1Iℒi{\mathcal{L}}\_{\Sigma}:=\sum\_{i=1}^{I}{\mathcal{L}}\_{i}. ℒi{\mathcal{L}}\_{i} and ℒΣ{\mathcal{L}}\_{\Sigma} are Itô processes with dynamics denoted by

|  |  |  |
| --- | --- | --- |
|  | d​ℒi=μℒi​d​t+σℒi​d​Bandd​ℒΣ=μℒ​d​t+σℒ​d​B.d{\mathcal{L}}\_{i}=\mu\_{{\mathcal{L}}\_{i}}dt+\sigma\_{{\mathcal{L}}\_{i}}dB\quad\text{and}\quad d{\mathcal{L}}\_{\Sigma}=\mu\_{\mathcal{L}}dt+\sigma\_{\mathcal{L}}dB. |  |

Next, we define candidate labor response functions, which are affine in ll.

###### Definition 3.2.

For each i,j=1,…,Ii,j=1,\ldots,I with j≠ij\neq i and δ∈ℝ\delta\in\mathbb{R}, Λji:[0,T]×(0,1)→ℝ\Lambda\_{j}^{i}:[0,T]\times(0,1)\rightarrow\mathbb{R} is defined by

|  |  |  |
| --- | --- | --- |
|  | Λj,ti​(l):=δ​wi,twj,t​(l−Li,t)+Lj,t,l∈(0,1).\Lambda\_{j,t}^{i}(l):=\delta\frac{w\_{i,t}}{w\_{j,t}}(l-L\_{i,t})+L\_{j,t},\quad l\in(0,1). |  |

We recall that the wage rates are nonzero for all t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s., and we define Λj,ti​(l)=Lj,t\Lambda^{i}\_{j,t}(l)=L\_{j,t} when wj,t=0w\_{j,t}=0. For each t∈[0,T]t\in[0,T], Λj,ti\Lambda^{i}\_{j,t} is affine in ll. The response function Λj,ti​(l)\Lambda^{i}\_{j,t}(l) describes how agent ii perceives agent jj to respond to ii’s choice of labor ll. The influence parameter δ\delta is chosen to be the same across all agents, and the sign of δ\delta describes the overall attitude of perceptions of the economic agents. We call δ>0\delta>0 the greater good scenario because the agents perceive that the other agents respond positively to their hard work (labor). Everybody’s perceived income increases in the greater good scenario. Conversely, we call the δ<0\delta<0 case the freeloader scenario because the agents perceive a negative response from others, and everybody’s perceived income suffers as a result. Finally, δ=0\delta=0 is the competitive scenario, in which the agents perceive no response to the labor choices of others.

For a fixed i=1,…,Ii=1,\ldots,I, using the labor response functions Λj,ti\Lambda^{i}\_{j,t} in Definition [3.2](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem2 "Definition 3.2. ‣ 3 Equilibrium construction") and by ([2.1](https://arxiv.org/html/2601.07626v1#S2.E1 "In 2 Model setting")), agent ii’s perceived income for l∈(0,1)l\in(0,1) and t∈[0,T]t\in[0,T] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | εi,t​(l)=wi,t​(λk​e​e​p+λu​b​iI​(1+δ​(I−1)))​l+λu​b​iI​(∑j≠iwj,t​Lj,t−δ​(I−1)​wi,t​Li,t).\displaystyle\varepsilon\_{i,t}(l)=w\_{i,t}\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}\big(1+\delta(I-1)\big)\right)l+\frac{\lambda\_{ubi}}{I}\left(\sum\_{j\neq i}w\_{j,t}L\_{j,t}-\delta(I-1)w\_{i,t}L\_{i,t}\right). |  | (3.1) |

Based on the processes LiL\_{i} from Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction") for agent ii’s candidate optimal labor proportion, we denote the candidate aggregate income stream by εΣ:=∑i=1Iεi​(Li)\varepsilon\_{\Sigma}:=\sum\_{i=1}^{I}\varepsilon\_{i}(L\_{i}). Since εi​(Li)\varepsilon\_{i}(L\_{i}) and εΣ\varepsilon\_{\Sigma} are Itô processes, we write their dynamics as

|  |  |  |
| --- | --- | --- |
|  | d​εi​(Li)=μεi​d​t+σεi​d​Bandd​εΣ=με​d​t+σε​d​B.d\varepsilon\_{i}(L\_{i})=\mu\_{\varepsilon\_{i}}dt+\sigma\_{\varepsilon\_{i}}dB\quad\text{and}\quad d\varepsilon\_{\Sigma}=\mu\_{\varepsilon}dt+\sigma\_{\varepsilon}dB. |  |

Proposition [3.3](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3 Equilibrium construction") establishes uniform boundedness of several drift and volatility terms related to labor and income, which will be needed for the construction and verification of equilibrium. The proof of Proposition [3.3](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3 Equilibrium construction") is in Section [5](https://arxiv.org/html/2601.07626v1#S5 "5 Proofs") below.

###### Proposition 3.3.

For each i=1,…,Ii=1,\ldots,I, assume that the wage rates are nonzero for all t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s., and that for the wage rate dynamics coefficients, we have μwi,σwi∈𝒮∞\mu\_{w\_{i}},\sigma\_{w\_{i}}\in{\mathcal{S}}^{\infty}. The progressively measurable processes μLi\mu\_{L\_{i}}, μℒi\mu\_{{\mathcal{L}}\_{i}}, μεi\mu\_{\varepsilon\_{i}}, σLi\sigma\_{L\_{i}}, σℒi\sigma\_{{\mathcal{L}}\_{i}}, and σεi\sigma\_{\varepsilon\_{i}} are uniformly bounded. Moreover, the drift and volatility dynamics coefficients of Li​wiL\_{i}w\_{i} are also uniformly bounded.

We construct a financial market and determine the agents’ consumption and investment strategies in terms of the optimal labor proportion and income streams with the help of the solution ((a,Za),(Yi,Zi)1≤i≤I)\big((a,Z\_{a}),(Y\_{i},Z\_{i})\_{1\leq i\leq I}\big) to the BSDE system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​a=Za​d​B+(ρΣ+αΣ​(μD+με−μℒ)−12​(αΣ​(σD+σε−σℒ)−Za)2−exp⁡(−a))​d​t,d​Yi=ZidB+1αi(−ρi+1+a+αi​(Yi−εi​(Li)+ℒi)exp⁡(a)−12(αΣ(σD+σε−σℒ)−Za)2+αiZi(αΣ(σD+σε−σℒ)−Za))dt,aT=0,Yi,T=εi,T​(Li,T)−ℒi,T,1≤i≤I,\displaystyle\begin{split}da&=Z\_{a}\,dB+\left(\rho\_{\Sigma}+\alpha\_{\Sigma}(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}})-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)^{2}-\exp(-a)\right)dt,\\ dY\_{i}&=Z\_{i}\,dB+\frac{1}{\alpha\_{i}}\left(-\rho\_{i}+\frac{1+a+\alpha\_{i}(Y\_{i}-\varepsilon\_{i}(L\_{i})+{\mathcal{L}}\_{i})}{\exp(a)}-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)^{2}\right.\\ &\quad\quad\quad\quad\quad\quad\left.\phantom{\frac{(Y\_{i})}{A}}+\alpha\_{i}Z\_{i}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)\right)dt,\\ a\_{T}&=0,\quad Y\_{i,T}=\varepsilon\_{i,T}(L\_{i,T})-{\mathcal{L}}\_{i,T},\quad 1\leq i\leq I,\end{split} | |  | (3.2) |

where αΣ:=(∑i=1I1αi)−1\alpha\_{\Sigma}:=\left(\sum\_{i=1}^{I}\frac{1}{\alpha\_{i}}\right)^{-1} and ρΣ:=αΣ​∑i=1Iρiαi\rho\_{\Sigma}:=\alpha\_{\Sigma}\sum\_{i=1}^{I}\frac{\rho\_{i}}{\alpha\_{i}} are constants. The BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")) is (I+1)(I+1)-dimensional, quadratic, and coupled. However, the (a,Za)(a,Z\_{a}) equation decouples from the system, and the coupling is not quadratic.

Proposition [3.4](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 Equilibrium construction") establishes the existence and uniqueness of a solution to BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")), which will pave the way for the financial market’s equilibrium construction. The proof is provided below in Section [5](https://arxiv.org/html/2601.07626v1#S5 "5 Proofs").

###### Proposition 3.4.

Assume that the wage rates are nonzero for all t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s., and that for the dividend and wage rate dynamics coefficients, we have μD,σD,μwi,σwi∈𝒮∞\mu\_{D},\sigma\_{D},\mu\_{w\_{i}},\sigma\_{w\_{i}}\in{\mathcal{S}}^{\infty} for i=1,…,Ii=1,\ldots,I. Then, there exists a unique solution ((a,Za),(Yi,Zi)1≤i≤I)\big((a,Z\_{a}),(Y\_{i},Z\_{i})\_{1\leq i\leq I}\big) to the BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")) with (a,Za)∈𝒮∞×bmo(a,Z\_{a})\in{\mathcal{S}}^{\infty}\times\text{bmo} and Yi−εi​(Li)+ℒi∈𝒮∞Y\_{i}-\varepsilon\_{i}(L\_{i})+{\mathcal{L}}\_{i}\in{\mathcal{S}}^{\infty} and Zi∈bmoZ\_{i}\in\text{bmo}.

Let ((a,Za),(Yi,Zi)1≤i≤I)\big((a,Z\_{a}),(Y\_{i},Z\_{i})\_{1\leq i\leq I}\big) be the unique solution to the BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")) guaranteed by Proposition [3.4](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 Equilibrium construction"). Using this solution, we construct our remaining candidate equilibrium quantities: the stock price, the annuity price, optimal investment policies, optimal wealth processes, and optimal consumption policies. First, we denote YΣ:=∑i=1IYiY\_{\Sigma}:=\sum\_{i=1}^{I}Y\_{i} and ZΣ:=∑i=1IZiZ\_{\Sigma}:=\sum\_{i=1}^{I}Z\_{i} and observe that (YΣ,ZΣ)(Y\_{\Sigma},Z\_{\Sigma}) is the unique solution to the BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​YΣ\displaystyle dY\_{\Sigma} | =ZΣdB+1αΣ(−ρΣ+1+a+αΣ​(YΣ−εΣ+ℒΣ)A−αΣ22(σD+σε−σℒ)2\displaystyle=Z\_{\Sigma}dB+\frac{1}{\alpha\_{\Sigma}}\left(-\rho\_{\Sigma}+\frac{1+a+\alpha\_{\Sigma}(Y\_{\Sigma}-\varepsilon\_{\Sigma}+{\mathcal{L}}\_{\Sigma})}{A}-\frac{\alpha\_{\Sigma}^{2}}{2}\left(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}}\right)^{2}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +αΣ2ZΣ(σD+σε−σℒ−ZaαΣ))dt,\displaystyle\quad\quad\quad\quad\quad\quad\left.\phantom{\frac{Y\_{\Sigma}}{A}}+\alpha\_{\Sigma}^{2}Z\_{\Sigma}\left(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}}-\frac{Z\_{a}}{\alpha\_{\Sigma}}\right)\right)dt, |  |

with YΣ,T=εΣ,T−ℒΣ,TY\_{\Sigma,T}=\varepsilon\_{\Sigma,T}-{\mathcal{L}}\_{\Sigma,T}, where YΣ−εΣ+ℒΣ∈𝒮∞Y\_{\Sigma}-\varepsilon\_{\Sigma}+{\mathcal{L}}\_{\Sigma}\in{\mathcal{S}}^{\infty} and ZΣ∈bmoZ\_{\Sigma}\in\text{bmo}.

Next, we define the annuity and stock price processes by

|  |  |  |  |
| --- | --- | --- | --- |
|  | A:=exp⁡(a)andS:=A​(D+εΣ−aαΣ−YΣ−ℒΣ).A:=\exp(a)\quad\text{and}\quad S:=A\left(D+\varepsilon\_{\Sigma}-\frac{a}{\alpha\_{\Sigma}}-Y\_{\Sigma}-{\mathcal{L}}\_{\Sigma}\right). |  | (3.3) |

AA and SS satisfy the dynamics conjectured in ([2.3](https://arxiv.org/html/2601.07626v1#S2.E3 "In 2 Model setting")) and ([2.4](https://arxiv.org/html/2601.07626v1#S2.E4 "In 2 Model setting")) with μA\mu\_{A}, σA\sigma\_{A}, μS\mu\_{S}, σS\sigma\_{S}, and κ\kappa defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | κ:=αΣ​(σD+σε−σℒ),σA:=Za,μA:=ρΣ+αΣ​(μD+με−μℒ)−κ22+κ​σA,σS:=AαΣ​(κ−σA−αΣ​ZΣ),μS:=κ​σS.\displaystyle\begin{split}\kappa&:=\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}}),\\ \sigma\_{A}&:=Z\_{a},\\ \mu\_{A}&:=\rho\_{\Sigma}+\alpha\_{\Sigma}(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}})-\frac{\kappa^{2}}{2}+\kappa\sigma\_{A},\\ \sigma\_{S}&:=\frac{A}{\alpha\_{\Sigma}}\left(\kappa-\sigma\_{A}-\alpha\_{\Sigma}Z\_{\Sigma}\right),\\ \mu\_{S}&:=\kappa\sigma\_{S}.\end{split} | |  | (3.4) |

The process κ\kappa can be interpretted as the market price of risk and is discussed below in Section [4.2](https://arxiv.org/html/2601.07626v1#S4.SS2 "4.2 Stock Market Effects ‣ 4 Universal Basic Income Effects").

Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction") is the main result of this work and is the implementation of Theorem [2.3](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Model setting"). The proof of Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction") is contained in Section [5](https://arxiv.org/html/2601.07626v1#S5 "5 Proofs").

###### Theorem 3.5.

Assume that the wage rates are nonzero for all t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s., and that for the dividend and wage rate dynamics coefficients, we have μD,σD,μwi,σwi∈𝒮∞\mu\_{D},\sigma\_{D},\mu\_{w\_{i}},\sigma\_{w\_{i}}\in{\mathcal{S}}^{\infty} for i=1,…,Ii=1,\ldots,I. Let λk​e​e​p∈[0,1]\lambda\_{keep}\in[0,1], λu​b​i∈[0,1−λk​e​e​p]\lambda\_{ubi}\in[0,1-\lambda\_{keep}], and δ∈ℝ\delta\in\mathbb{R} be given. Let ((a,Za),(Yi,Zi)1≤i≤I)\big((a,Z\_{a}),(Y\_{i},Z\_{i})\_{1\leq i\leq I}\big) be the unique solution to the BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")) guaranteed by Proposition [3.4](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 Equilibrium construction"). There exists an equilibrium with annuity and stock price processes given by ([3.3](https://arxiv.org/html/2601.07626v1#S3.E3 "In 3 Equilibrium construction")) and labor response functions given by Definition [3.2](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem2 "Definition 3.2. ‣ 3 Equilibrium construction") using the parameter δ∈ℝ\delta\in\mathbb{R}. For κ\kappa, σA\sigma\_{A}, μA\mu\_{A}, σS\sigma\_{S}, and μS\mu\_{S} given in ([3.4](https://arxiv.org/html/2601.07626v1#S3.E4 "In 3 Equilibrium construction")), AA and SS satisfy the dynamics conjectured in ([2.3](https://arxiv.org/html/2601.07626v1#S2.E3 "In 2 Model setting")) and ([2.4](https://arxiv.org/html/2601.07626v1#S2.E4 "In 2 Model setting")). The agents’ optimal labor proportions are the processes L1,…,LIL\_{1},\ldots,L\_{I} defined in Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction"). For i=1,…,Ii=1,\ldots,I, agent ii’s optimal number of stock shares πi\pi\_{i} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi={Aαi​σS​(κ−σA−αi​Zi),if ​σS≠0πi,0,otherwise.\pi\_{i}=\begin{cases}\frac{A}{\alpha\_{i}\sigma\_{S}}\left(\kappa-\sigma\_{A}-\alpha\_{i}Z\_{i}\right),&\text{if }\sigma\_{S}\neq 0\\ \pi\_{i,0},&\text{otherwise}\end{cases}. |  | (3.5) |

Agent ii’s optimal wealth process is given by Xi,0−=Xi,0=θi,0−​A0+πi,0−​S0X\_{i,0-}=X\_{i,0}=\theta\_{i,0-}A\_{0}+\pi\_{i,0-}S\_{0} and for t∈[0,T]t\in[0,T] by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xi,t=At​(Xi,0−A0+∫0t(πi,sAs​(μS,s−σA,s​σS,s)−a+αi​(Yi,s−εi,s​(Li,s)+ℒi,s)αi​As)​𝑑s+∫0tπi,s​σS,sAs​𝑑Bs).\displaystyle\begin{split}X\_{i,t}&=A\_{t}\left(\tfrac{X\_{i,0-}}{A\_{0}}+\int\_{0}^{t}\left(\tfrac{\pi\_{i,s}}{A\_{s}}(\mu\_{S,s}-\sigma\_{A,s}\sigma\_{S,s})-\tfrac{a+\alpha\_{i}(Y\_{i,s}-\varepsilon\_{i,s}(L\_{i,s})+{\mathcal{L}}\_{i,s})}{\alpha\_{i}A\_{s}}\right)ds+\int\_{0}^{t}\tfrac{\pi\_{i,s}\sigma\_{S,s}}{A\_{s}}dB\_{s}\right).\end{split} | |  | (3.6) |

Agent ii’s optimal consumption rate is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ci=XiA+aαi+Yi+ℒi,c\_{i}=\frac{X\_{i}}{A}+\frac{a}{\alpha\_{i}}+Y\_{i}+{\mathcal{L}}\_{i}, |  | (3.7) |

and the optimal annuity holdings are determined by θi=Xi−πi​SA\theta\_{i}=\frac{X\_{i}-\pi\_{i}S}{A}. Agent ii’s triple of strategies is admissible with (πi,θi,ci)∈𝒜i​(Li)(\pi\_{i},\theta\_{i},c\_{i})\in{\mathcal{A}}\_{i}(L\_{i}) and solves ([2.6](https://arxiv.org/html/2601.07626v1#S2.E6 "In item 1 ‣ Definition 2.2. ‣ 2 Model setting")).

## 4 Universal Basic Income Effects

We study the impact of a UBI policy on the economy in terms of labor market participation, stock market effects, and welfare. Throughout this section, we assume that all wage rate processes wi=(wi)t∈[0,T]w\_{i}=(w\_{i})\_{t\in[0,T]}, i=1,…,Ii=1,\ldots,I are positive. Although the construction and existence of a universal basic income equilibrium does not rely on positivity of wage rates, drawing sensible and applicable conclusions about such equilibria does require wage rates to be positive.

### 4.1 Labor Market Participation

By Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction"), for each i=1,…,Ii=1,\ldots,I, LiL\_{i} is (0,1)(0,1)-valued and determined by

|  |  |  |
| --- | --- | --- |
|  | Ψi​(Li)=αi​wi​(λk​e​e​p+λu​b​iI​(1+δ​(I−1))),\Psi\_{i}(L\_{i})=\alpha\_{i}w\_{i}\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}\big(1+\delta(I-1)\big)\right), |  |

where Ψi​(l):=ui′​(l)ui​(l)\Psi\_{i}(l):=\frac{u\_{i}^{\prime}(l)}{u\_{i}(l)} for l∈(0,1)l\in(0,1). We denote λ:=(λk​e​e​p+λu​b​iI​(1+δ​(I−1)))\lambda:=\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}\big(1+\delta(I-1)\big)\right). By Itô’s Lemma, we determine the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Li\displaystyle dL\_{i} | =(αi​λ​μwiΨi′​(Li)−αi2​λ2​σwi22⋅Ψi′′​(Li)(Ψi′​(Li))3)​d​t+αi​λ​σwiΨi′​(Li)​d​B,\displaystyle=\left(\frac{\alpha\_{i}\lambda\mu\_{w\_{i}}}{\Psi\_{i}^{\prime}(L\_{i})}-\frac{\alpha\_{i}^{2}\lambda^{2}\sigma\_{w\_{i}}^{2}}{2}\cdot\frac{\Psi\_{i}^{\prime\prime}(L\_{i})}{\left(\Psi\_{i}^{\prime}(L\_{i})\right)^{3}}\right)dt+\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}}{\Psi\_{i}^{\prime}(L\_{i})}dB, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℒi\displaystyle d{\mathcal{L}}\_{i} | =1αi​d​(log⁡ui​(Li))\displaystyle=\tfrac{1}{\alpha\_{i}}d\left(\log u\_{i}(L\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(λ​μwi⋅Ψi​(Li)Ψi′​(Li)−αi​λ2​σwi22⋅Ψi′′​(Li)​Ψi​(Li)(Ψi′​(Li))3+αi​λ2​σwi22​Ψi′​(Li))​d​t+λ​σwi​Ψi​(Li)Ψi′​(Li)​d​B,\displaystyle=\left(\lambda\mu\_{w\_{i}}\cdot\frac{\Psi\_{i}(L\_{i})}{\Psi\_{i}^{\prime}(L\_{i})}-\frac{\alpha\_{i}\lambda^{2}\sigma\_{w\_{i}}^{2}}{2}\cdot\frac{\Psi\_{i}^{\prime\prime}(L\_{i})\Psi\_{i}(L\_{i})}{(\Psi\_{i}^{\prime}(L\_{i}))^{3}}+\frac{\alpha\_{i}\lambda^{2}\sigma\_{w\_{i}}^{2}}{2\Psi^{\prime}\_{i}(L\_{i})}\right)dt+\frac{\lambda\sigma\_{w\_{i}}\Psi\_{i}(L\_{i})}{\Psi^{\prime}\_{i}(L\_{i})}dB, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(wi​Li)\displaystyle d\big(w\_{i}L\_{i}) | =(μwi​Li+αi​λ​σwi2+μwi​Ψi​(Li)Ψi′​(Li)−αi​λ​σwi22⋅Ψi​(Li)​Ψi′′​(Li)(Ψi′​(Li))3)​d​t\displaystyle=\left(\mu\_{w\_{i}}L\_{i}+\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}^{2}+\mu\_{w\_{i}}\Psi\_{i}(L\_{i})}{\Psi^{\prime}\_{i}(L\_{i})}-\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}^{2}}{2}\cdot\frac{\Psi\_{i}(L\_{i})\Psi^{\prime\prime}\_{i}(L\_{i})}{(\Psi\_{i}^{\prime}(L\_{i}))^{3}}\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(σwi​Li+σwi​Ψi​(Li)Ψi′​(Li))​d​B,\displaystyle\quad\quad+\left(\sigma\_{w\_{i}}L\_{i}+\frac{\sigma\_{w\_{i}}\Psi\_{i}(L\_{i})}{\Psi^{\prime}\_{i}(L\_{i})}\right)dB, |  |

which by the consistency requirement of Definition [2.2](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Model setting"), leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​εΣ\displaystyle d\varepsilon\_{\Sigma} | =(λk​e​e​p+λu​b​i)​∑i=1Id​(wi​Li).\displaystyle=(\lambda\_{keep}+\lambda\_{ubi})\sum\_{i=1}^{I}d\big(w\_{i}L\_{i}\big). |  |

By the invertibility of Ψi:(0,1)→ℝ\Psi\_{i}:(0,1)\rightarrow\mathbb{R}, we can express Li=Ψi−1​(αi​λ​wi)L\_{i}=\Psi\_{i}^{-1}(\alpha\_{i}\lambda w\_{i}), allowing us to express all of the terms and dynamics coefficients above as functions of λ\lambda or wage rates.

For each i=1,…,Ii=1,\ldots,I, since Ψi−1\Psi\_{i}^{-1} is strictly increasing and wiw\_{i} is positive, LiL\_{i} is strictly increasing in the parameter λ=(λk​e​e​p+λu​b​iI​(1+δ​(I−1)))\lambda=\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}\big(1+\delta(I-1)\big)\right) for λ>0\lambda>0. Thus, LiL\_{i}, ℒi{\mathcal{L}}\_{i}, wi​Liw\_{i}L\_{i}, εi​(Li)\varepsilon\_{i}(L\_{i}), and εΣ\varepsilon\_{\Sigma} are all strictly increasing in λ\lambda for λ>0\lambda>0. When δ>−1I−1​(1+λk​e​e​p⋅Iλu​b​i)\delta>-\frac{1}{I-1}\left(1+\tfrac{\lambda\_{keep}\cdot I}{\lambda\_{ubi}}\right), λ\lambda is positive.

For −1I−1​(1+λk​e​e​p⋅Iλu​b​i)<δ<0-\frac{1}{I-1}\left(1+\tfrac{\lambda\_{keep}\cdot I}{\lambda\_{ubi}}\right)<\delta<0, workforce participation and the income it generates benefit from larger values of λk​e​e​p\lambda\_{keep} and smaller values of λu​b​i\lambda\_{ubi}. Under this scenario for δ\delta values, implementing a universal basic income policy by increasing λu​b​i\lambda\_{ubi} causes a decrease in labor market participation and income.

For δ>0\delta>0, workforce participation and the income it generates benefit from universal basic income friendly policies, meaning larger λu​b​i\lambda\_{ubi} and smaller λk​e​e​p\lambda\_{keep}. Redistributing the aggregate income more by choosing larger values of λu​b​i\lambda\_{ubi} leads to higher individual labor market participation, individual income, and aggregate income.

### 4.2 Stock Market Effects

How does the equilibrium financial market respond to changes in universal basic income policy? We investigate these changes through the market-price-of-risk and interest rate, which we define via a state price deflator. A state price deflator is a strictly positive Itô process ξ\xi with dynamics

|  |  |  |
| --- | --- | --- |
|  | d​ξ=ξ​(κ​d​B+r​d​t),ξ0>0,d\xi=\xi\big(\kappa\,dB+r\,dt\big),\quad\xi\_{0}>0, |  |

such that (ξ​A+∫0⋅ξs​𝑑s)\left(\xi A+\int\_{0}^{\cdot}\xi\_{s}ds\right) and (ξ​S+∫0⋅ξs​Ds​𝑑s)\left(\xi S+\int\_{0}^{\cdot}\xi\_{s}D\_{s}ds\right) are local martingales. Given a state price deflator ξ\xi for the equilibrium financial market, ξ\xi’s dynamics are constrained so that its market-price-of-risk κ\kappa and interest rate rr satisfy

|  |  |  |
| --- | --- | --- |
|  | μS=κ​σSandr=μA−κ​σA.\mu\_{S}=\kappa\sigma\_{S}\quad\text{and}\quad r=\mu\_{A}-\kappa\sigma\_{A}. |  |

In our setting, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ\displaystyle\kappa | =αΣ​(σD+σε−σℒ),\displaystyle=\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{{\mathcal{L}}}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | r\displaystyle r | =ρΣ+αΣ​(μD+με−μℒ)−12​κ2.\displaystyle=\rho\_{\Sigma}+\alpha\_{\Sigma}(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{{\mathcal{L}}})-\frac{1}{2}\kappa^{2}. |  |

We call rr an interest rate, even though the financial market does not necessarily have an interest rate since it is unclear whether σS\sigma\_{S} is nonzero for all time with probability one. However, should there be an interest rate in the usual sense, it would be our rr.

As seen above in Section [4.1](https://arxiv.org/html/2601.07626v1#S4.SS1 "4.1 Labor Market Participation ‣ 4 Universal Basic Income Effects"), for each i=1,…,Ii=1,\ldots,I, the terms LiL\_{i}, ℒi{\mathcal{L}}\_{i}, and wi​Liw\_{i}L\_{i} are strictly increasing in λ\lambda and wiw\_{i} since Ψi−1\Psi\_{i}^{-1} is strictly increasing and wiw\_{i} is strictly positive, but their dynamics coefficients are not. Even though we have closed-form expressions for all dynamics coefficients in terms of input parameters, these terms are nonmonotone in the input parameters. The market price of risk and interest rate depend on those dynamics coefficients, and thus, they depend in a complex, nonmonotone manner on the input parameters: λk​e​e​p\lambda\_{keep}, λu​b​i\lambda\_{ubi}, and δ\delta.

![Refer to caption](4-mpr.png)![Refer to caption](4-rates.png)![Refer to caption](legend.png)\begin{array}[]{ccc}\includegraphics[width=137.9979pt]{4-mpr}&\includegraphics[width=137.9979pt]{4-rates}&\includegraphics[width=51.7479pt]{legend}\\
\end{array}

  


Figure 1: Graphs of the market price of risk and interest rate as a function of the wage rate ww for varying δ\delta. The common set of parameters are λk​e​e​p=0.7\lambda\_{keep}=0.7, λu​b​i=0.2\lambda\_{ubi}=0.2, I=2I=2, α1=α2=0.2\alpha\_{1}=\alpha\_{2}=0.2, ρ1=ρ2=1\rho\_{1}=\rho\_{2}=1, β1=−0.2\beta\_{1}=-0.2, β2=−0.4\beta\_{2}=-0.4, μw1=0.1\mu\_{w\_{1}}=0.1, μw2=0.2\mu\_{w\_{2}}=0.2, σw1=0.1\sigma\_{w\_{1}}=0.1, σw2=−0.05\sigma\_{w\_{2}}=-0.05, μD=01\mu\_{D}=01, and σD=0.5\sigma\_{D}=0.5.

Figure [1](https://arxiv.org/html/2601.07626v1#S4.F1 "Figure 1 ‣ 4.2 Stock Market Effects ‣ 4 Universal Basic Income Effects") plots the market price of risk and interest rate as functions of the wage rate across a common set of parameters λk​e​e​p=0.7\lambda\_{keep}=0.7, λu​b​i=0.2\lambda\_{ubi}=0.2, I=2I=2, α1=α2=0.2\alpha\_{1}=\alpha\_{2}=0.2, ρ1=ρ2=1\rho\_{1}=\rho\_{2}=1, β1=−0.2\beta\_{1}=-0.2, β2=−0.4\beta\_{2}=-0.4, μw1=0.1\mu\_{w\_{1}}=0.1, μw2=0.2\mu\_{w\_{2}}=0.2, σw1=0.1\sigma\_{w\_{1}}=0.1, σw2=−0.05\sigma\_{w\_{2}}=-0.05, μD=0.1\mu\_{D}=0.1, and σD=0.5\sigma\_{D}=0.5. The initial wage rate is taken to be the same for both agents in the plots, and the graphs plot the market price of risk and interest rate as functions of the shared initial wage rate. Nontrivial behavior is also observed with respect to the influence parameter, δ\delta. For example, as δ\delta increases in Figure [1](https://arxiv.org/html/2601.07626v1#S4.F1 "Figure 1 ‣ 4.2 Stock Market Effects ‣ 4 Universal Basic Income Effects"), the market price of risk switches from increasing to developing nonmonotone behavior in the wage rate. The interest rate plots also show nonmonotone behavior with respect to δ\delta.

### 4.3 Welfare

We study the welfare of the economy using aggregate certainty equivalents in the simple case of constant wage rates. Assume in this subsection that w1,…,wIw\_{1},\ldots,w\_{I} are positive constants. Since wage rates are constant, the optimal labor proportions L1,…,LIL\_{1},\ldots,L\_{I} and the corresponding income streams are also constant.

For i=1,…,Ii=1,\ldots,I, the certainty equivalent for agent ii is defined as the constant value C​EiCE\_{i} such that

|  |  |  |
| --- | --- | --- |
|  | ∫0TUi​(t,C​Ei,Li)​𝑑t+Ui​(T,C​Ei,Li)=𝔼​[∫0TUi​(t,ci,t,Li)​𝑑t+Ui​(T,Xi,T+εi​(Li),Li)],\int\_{0}^{T}U\_{i}(t,CE\_{i},L\_{i})dt+U\_{i}\big(T,CE\_{i},L\_{i}\big)=\mathbb{E}\left[\int\_{0}^{T}U\_{i}(t,c\_{i,t},L\_{i})dt+U\_{i}\big(T,X\_{i,T}+\varepsilon\_{i}(L\_{i}),L\_{i}\big)\right], |  |

where cic\_{i}, XiX\_{i}, and LiL\_{i} are optimal for agent ii in ([2.6](https://arxiv.org/html/2601.07626v1#S2.E6 "In item 1 ‣ Definition 2.2. ‣ 2 Model setting")). The time dependence on εi\varepsilon\_{i} and LiL\_{i} is dropped due to constant wage rates.

The certainty equivalent represents the constant consumption stream level that an agent is willing to exchange for her optimal (stochastic) consumption stream. For i=1,…,Ii=1,\ldots,I, the certainty equivalent is given by

|  |  |  |
| --- | --- | --- |
|  | C​Ei=1αi​log⁡(ui​(Li))−1αi​log⁡(1ρi​(1−e−ρi​T)+e−ρi​T)+Xi,0A0+Yi,0.CE\_{i}=\frac{1}{\alpha\_{i}}\log(u\_{i}(L\_{i}))-\frac{1}{\alpha\_{i}}\log\left(\frac{1}{\rho\_{i}}\left(1-e^{-\rho\_{i}T}\right)+e^{-\rho\_{i}T}\right)+\frac{X\_{i,0}}{A\_{0}}+Y\_{i,0}. |  |

We measure welfare by the aggregate certainty equivalent and use clearing in the stock market via ([3.3](https://arxiv.org/html/2601.07626v1#S3.E3 "In 3 Equilibrium construction")) to obtain

|  |  |  |
| --- | --- | --- |
|  | ∑i=1IC​Ei=1+D0+εΣ,0−a0αΣ−∑i=1I1αi​log⁡(1ρi​(1−e−ρi​T)+e−ρi​T).\sum\_{i=1}^{I}CE\_{i}=1+D\_{0}+\varepsilon\_{\Sigma,0}-\frac{a\_{0}}{\alpha\_{\Sigma}}-\sum\_{i=1}^{I}\frac{1}{\alpha\_{i}}\log\left(\frac{1}{\rho\_{i}}\left(1-e^{-\rho\_{i}T}\right)+e^{-\rho\_{i}T}\right). |  |

Within the welfare representation, due to the constant wage rates, the universal basic income parameters (λk​e​e​p\lambda\_{keep}, λu​b​i\lambda\_{ubi}, and δ\delta) only appear in εΣ,0\varepsilon\_{\Sigma,0}, which as in Section [4.1](https://arxiv.org/html/2601.07626v1#S4.SS1 "4.1 Labor Market Participation ‣ 4 Universal Basic Income Effects"), is increasing in λ=(λk​e​e​p+λu​b​iI​(1+δ​(I−1)))\lambda=\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}\left(1+\delta(I-1)\right)\right), so long as λ>0\lambda>0.

For λ>0\lambda>0, since εΣ,0=(λk​e​e​p+λu​b​i)​∑i=1Iwi​Li\varepsilon\_{\Sigma,0}=(\lambda\_{keep}+\lambda\_{ubi})\sum\_{i=1}^{I}w\_{i}L\_{i} is increasing in its λ\lambda dependence, the welfare of the economy is also increasing in λ\lambda. Similar to the analysis of labor market participation in Section [4.1](https://arxiv.org/html/2601.07626v1#S4.SS1 "4.1 Labor Market Participation ‣ 4 Universal Basic Income Effects"), for −1I−1​(1+λk​e​e​pλu​b​i​I)<δ<0\frac{-1}{I-1}\left(1+\tfrac{\lambda\_{keep}}{\lambda\_{ubi}}I\right)<\delta<0, the corresponding λ\lambda is positive, and welfare responds negatively to universal basic income policies. Increasing λu​b​i\lambda\_{ubi} or decreasing λk​e​e​p\lambda\_{keep} causes a decrease in welfare.

Conversely, for δ>0\delta>0, the corresponding λ\lambda is negative, and welfare responds positively to universal basic income policies. Increasing λu​b​i\lambda\_{ubi} or decreasing λk​e​e​p\lambda\_{keep} causes an increase in welfare.

### 4.4 Socialism versus Communism

We compare two extreme scenarios in our model: pure socialism versus pure communism. In both pure communistic and pure socialistic economies, agents keep none of their individual earnings (λk​e​e​p=0\lambda\_{keep}=0) and all earnings are redistributed (λu​b​i=1\lambda\_{ubi}=1). Pure communism assumes the perceived incomes equal actual incomes (δ=0\delta=0), whereas pure socialism allows for perceptions to deviate from actual incomes (δ∈ℝ\delta\in\mathbb{R}). Under a socialistic economic setting, agents still give up all of their individual earnings to the greater economy like in communism, but the agents perceive this usurping of their income differently in their labor choice problem, ([3.1](https://arxiv.org/html/2601.07626v1#S3.E1 "In 3 Equilibrium construction")) and ([2.6](https://arxiv.org/html/2601.07626v1#S2.E6 "In item 1 ‣ Definition 2.2. ‣ 2 Model setting")).

In either scenario, labor choices using Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction") are determined by

|  |  |  |
| --- | --- | --- |
|  | ui′​(Li)ui​(Li)=αi​wi​(λu​b​iI​(1+δ​(I−1))).\frac{u\_{i}^{\prime}(L\_{i})}{u\_{i}(L\_{i})}=\alpha\_{i}w\_{i}\left(\frac{\lambda\_{ubi}}{I}(1+\delta(I-1))\right). |  |

Hence, optimal labor proportions LiL\_{i} are increasing as a function of the influence parameter δ\delta. In socialistic economies, labor force participation is greater (less) than that of a communistic economy depending on whether δ\delta is positive (negative).

In both socialistic and communistic economies, the total income of the economy is εΣ=(λk​e​e​p+λu​b​i)​∑i=1Iwi​Li=∑i=1Iwi​Li\varepsilon\_{\Sigma}=(\lambda\_{keep}+\lambda\_{ubi})\sum\_{i=1}^{I}w\_{i}L\_{i}=\sum\_{i=1}^{I}w\_{i}L\_{i} by Defintion [2.2](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Model setting") item [3](https://arxiv.org/html/2601.07626v1#S2.I2.i3 "item 3 ‣ Definition 2.2. ‣ 2 Model setting"). Since each LiL\_{i} fluctuates depending on the influence parameter δ\delta and whether wage rates are positive, the total income of the economy increases in δ\delta.

Therefore, if a pure socialistic economy has δ>0\delta>0, then its labor market participation rate and total income is higher than that of a pure communistic economy.

## 5 Proofs

###### Proof of Proposition [3.3](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3 Equilibrium construction").

Let i∈{1,…,I}i\in\{1,\ldots,I\} be given. For l∈(0,1)l\in(0,1), we define Ψi​(l):=ui′​(l)ui​(l)\Psi\_{i}(l):=\frac{u^{\prime}\_{i}(l)}{u\_{i}(l)} and denote

|  |  |  |
| --- | --- | --- |
|  | λ=λk​e​e​p+λu​b​iI​(1+δ​(I−1)).\lambda=\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}(1+\delta(I-1)). |  |

Then, the process LiL\_{i} satisfies Ψi​(Li)=αi​λ​wi\Psi\_{i}(L\_{i})=\alpha\_{i}\lambda w\_{i} and has dynamics d​Li=μLi​d​t+σLi​d​BdL\_{i}=\mu\_{L\_{i}}dt+\sigma\_{L\_{i}}dB with

|  |  |  |  |
| --- | --- | --- | --- |
|  | μLi=αi​λ​μwiΨi′​(Li)−αi2​λ2​σwi22⋅Ψi′′​(Li)(Ψi′​(Li))3 and σLi=αi​λ​σwiΨi′​(Li).\mu\_{L\_{i}}=\frac{\alpha\_{i}\lambda\mu\_{w\_{i}}}{\Psi\_{i}^{\prime}(L\_{i})}-\frac{\alpha\_{i}^{2}\lambda^{2}\sigma\_{w\_{i}}^{2}}{2}\cdot\frac{\Psi\_{i}^{\prime\prime}(L\_{i})}{\left(\Psi\_{i}^{\prime}(L\_{i})\right)^{3}}\quad\text{ and }\quad\sigma\_{L\_{i}}=\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}}{\Psi\_{i}^{\prime}(L\_{i})}. |  | (5.1) |

The functions l↦1Ψi′​(l)l\mapsto\frac{1}{\Psi\_{i}^{\prime}(l)} and l↦Ψi′′​(l)(Ψi′​(l))3l\mapsto\frac{\Psi\_{i}^{\prime\prime}(l)}{(\Psi\_{i}^{\prime}(l))^{3}} are uniformly bounded for l∈(0,1)l\in(0,1) since they are continuous on (0,1)(0,1) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | liml→0+1Ψi′​(l)\displaystyle\lim\_{l\rightarrow 0+}\frac{1}{\Psi\_{i}^{\prime}(l)} | =liml→1−1Ψi′​(l)=0,\displaystyle=\lim\_{l\rightarrow 1-}\frac{1}{\Psi\_{i}^{\prime}(l)}=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | liml→0+Ψi′′​(l)(Ψi′​(l))3\displaystyle\lim\_{l\rightarrow 0+}\frac{\Psi^{\prime\prime}\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}} | =liml→1−Ψi′′​(l)(Ψi′​(l))3=0.\displaystyle=\lim\_{l\rightarrow 1-}\frac{\Psi^{\prime\prime}\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}}=0. |  |

Since μwi\mu\_{w\_{i}} and σwi\sigma\_{w\_{i}} are uniformly bounded, we conclude that μLi\mu\_{L\_{i}} and σLi\sigma\_{L\_{i}} are also uniformly bounded.

Next, we verify the uniform boundedness of μℒi\mu\_{{\mathcal{L}}\_{i}} and σℒi\sigma\_{{\mathcal{L}}\_{i}}, where we recall that ℒi=1αi​log⁡ui​(Li){\mathcal{L}}\_{i}=\frac{1}{\alpha\_{i}}\log u\_{i}(L\_{i}). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​log⁡ui​(Li)\displaystyle d\log u\_{i}(L\_{i}) | =(αi​λ​μwi⋅Ψi​(Li)Ψi′​(Li)−αi2​λ2​σwi22⋅Ψi′′​(Li)​Ψi​(Li)(Ψi′​(Li))3+12⋅αi2​λ2​σwi2Ψi′​(Li))​d​t\displaystyle=\left(\alpha\_{i}\lambda\mu\_{w\_{i}}\cdot\frac{\Psi\_{i}(L\_{i})}{\Psi\_{i}^{\prime}(L\_{i})}-\frac{\alpha\_{i}^{2}\lambda^{2}\sigma\_{w\_{i}}^{2}}{2}\cdot\frac{\Psi\_{i}^{\prime\prime}(L\_{i})\Psi\_{i}(L\_{i})}{(\Psi\_{i}^{\prime}(L\_{i}))^{3}}+\frac{1}{2}\cdot\frac{\alpha\_{i}^{2}\lambda^{2}\sigma\_{w\_{i}}^{2}}{\Psi^{\prime}\_{i}(L\_{i})}\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +αi​λ​σwi​Ψi​(Li)Ψi′​(Li)​d​B.\displaystyle\quad\quad\quad\quad+\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}\Psi\_{i}(L\_{i})}{\Psi^{\prime}\_{i}(L\_{i})}dB. |  |

Continuity of l↦Ψi​(l)Ψi′​(l)l\mapsto\frac{\Psi\_{i}(l)}{\Psi^{\prime}\_{i}(l)} and l↦Ψi′′​(l)​Ψi​(l)(Ψi′​(l))3l\mapsto\frac{\Psi\_{i}^{\prime\prime}(l)\Psi\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}} for l∈(0,1)l\in(0,1) and the limits

|  |  |  |  |
| --- | --- | --- | --- |
|  | liml→0+Ψi​(l)Ψi′​(l)\displaystyle\lim\_{l\rightarrow 0+}\frac{\Psi\_{i}(l)}{\Psi\_{i}^{\prime}(l)} | =liml→1−Ψi​(l)Ψi′​(l)=0,\displaystyle=\lim\_{l\rightarrow 1-}\frac{\Psi\_{i}(l)}{\Psi\_{i}^{\prime}(l)}=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | liml→0+Ψi′′​(l)​Ψi​(l)(Ψi′​(l))3\displaystyle\lim\_{l\rightarrow 0+}\frac{\Psi^{\prime\prime}\_{i}(l)\Psi\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}} | =liml→1−Ψi′′​(l)​Ψi​(l)(Ψi′​(l))3=0,\displaystyle=\lim\_{l\rightarrow 1-}\frac{\Psi^{\prime\prime}\_{i}(l)\Psi\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}}=0, |  |

imply that the functions l↦Ψi​(l)Ψi′​(l)l\mapsto\frac{\Psi\_{i}(l)}{\Psi^{\prime}\_{i}(l)} and l↦−Ψi′′​(l)​Ψi​(l)(Ψi′​(l))3l\mapsto\frac{-\Psi\_{i}^{\prime\prime}(l)\Psi\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}} are uniformly bounded on (0,1)(0,1). Together with the boundedness of μwi\mu\_{w\_{i}} and σwi\sigma\_{w\_{i}}, we conclude that μℒi\mu\_{{\mathcal{L}}\_{i}} and σℒi\sigma\_{{\mathcal{L}}\_{i}} are uniformly bounded.

By ([3.1](https://arxiv.org/html/2601.07626v1#S3.E1 "In 3 Equilibrium construction")), the uniform boundedness of μεi\mu\_{\varepsilon\_{i}} and σεi\sigma\_{\varepsilon\_{i}} relies on the boundedness of the drift and volatility of wi​Liw\_{i}L\_{i}. The product wi​Liw\_{i}L\_{i} is an Itô process with drift coefficient (wi​μLi+μwi​Li+σwi​σLi)\big(w\_{i}\mu\_{L\_{i}}+\mu\_{w\_{i}}L\_{i}+\sigma\_{w\_{i}}\sigma\_{L\_{i}}\big) and volatility coefficient (wi​σLi+σwi​Li)\big(w\_{i}\sigma\_{L\_{i}}+\sigma\_{w\_{i}}L\_{i}\big). By the measurability and boundedness of μwi\mu\_{w\_{i}}, μLi\mu\_{L\_{i}}, σwi\sigma\_{w\_{i}}, σLi\sigma\_{L\_{i}}, and LiL\_{i}, we only need to verify the boundedness of wi​σLiw\_{i}\sigma\_{L\_{i}} and wi​μLiw\_{i}\mu\_{L\_{i}}.

For wi​σLiw\_{i}\sigma\_{L\_{i}}, we use Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction") for LiL\_{i} and the dynamics ([5.1](https://arxiv.org/html/2601.07626v1#S5.E1 "In Proof of Proposition 3.3. ‣ 5 Proofs")) to obtain

|  |  |  |
| --- | --- | --- |
|  | wi​σLi=αi​λ​σwi​wiΨi′​(Li)=σwi​Ψi​(Li)Ψi′​(Li),w\_{i}\sigma\_{L\_{i}}=\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}w\_{i}}{\Psi^{\prime}\_{i}(L\_{i})}=\frac{\sigma\_{w\_{i}}\Psi\_{i}(L\_{i})}{\Psi^{\prime}\_{i}(L\_{i})}, |  |

where the above boundedness of l↦Ψi​(l)Ψi′​(l)l\mapsto\frac{\Psi\_{i}(l)}{\Psi^{\prime}\_{i}(l)} for l∈(0,1)l\in(0,1)
implies uniform boundedness of wi​σLiw\_{i}\sigma\_{L\_{i}}.

Similarly for wi​μLiw\_{i}\mu\_{L\_{i}}, we use Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction") and dynamics ([5.1](https://arxiv.org/html/2601.07626v1#S5.E1 "In Proof of Proposition 3.3. ‣ 5 Proofs")) to obtain

|  |  |  |
| --- | --- | --- |
|  | wi​μLi=μwi​Ψi​(Li)Ψi′​(Li)−αi​λ​σwi22⋅Ψi​(Li)​Ψi′′​(Li)(Ψi′​(Li))3,w\_{i}\mu\_{L\_{i}}=\frac{\mu\_{w\_{i}}\Psi\_{i}(L\_{i})}{\Psi^{\prime}\_{i}(L\_{i})}-\frac{\alpha\_{i}\lambda\sigma\_{w\_{i}}^{2}}{2}\cdot\frac{\Psi\_{i}(L\_{i})\Psi^{\prime\prime}\_{i}(L\_{i})}{(\Psi\_{i}^{\prime}(L\_{i}))^{3}}, |  |

where the above boundedness of l↦Ψi​(l)Ψi′​(l)l\mapsto\frac{\Psi\_{i}(l)}{\Psi^{\prime}\_{i}(l)} and l↦Ψi​(l)​Ψi′′​(l)(Ψi′​(l))3l\mapsto\frac{\Psi\_{i}(l)\Psi^{\prime\prime}\_{i}(l)}{(\Psi\_{i}^{\prime}(l))^{3}} for l∈(0,1)l\in(0,1) imply that wi​μLiw\_{i}\mu\_{L\_{i}} is uniformly bounded.

∎

###### Proof of Proposition [3.4](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 Equilibrium construction").

We consider the secondary BSDE system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​a=Za​d​B+(ρΣ+αΣ​(μD+με−μℒ)−12​(αΣ​(σD+σε−σℒ)−Za)2−exp⁡(−a))​d​t,d​Y¯i=Z¯idB+1αi(−ρi+αi(μℒi−μεi)+1+a+αi​Yi¯exp⁡(a)−12(αΣ(σD+σε−σℒ)−Za)2+αi(Zi¯+σεi−σℒi)(αΣ(σD+σε−σℒ)−Za))dt,aT=0,Y¯i,T=0,1≤i≤I.\displaystyle\begin{split}da&=Z\_{a}\,dB+\left(\rho\_{\Sigma}+\alpha\_{\Sigma}(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}})-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)^{2}-\exp(-a)\right)dt,\\ d\overline{Y}\_{i}&=\overline{Z}\_{i}\,dB+\frac{1}{\alpha\_{i}}\left(-\rho\_{i}+\alpha\_{i}(\mu\_{{\mathcal{L}}\_{i}}-\mu\_{\varepsilon\_{i}})+\frac{1+a+\alpha\_{i}\overline{Y\_{i}}}{\exp(a)}-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)^{2}\right.\\ &\quad\quad\quad\quad\quad\quad\left.\phantom{\frac{(Y\_{i})}{A}}+\alpha\_{i}\left(\overline{Z\_{i}}+\sigma\_{\varepsilon\_{i}}-\sigma\_{{\mathcal{L}}\_{i}}\right)\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)\right)dt,\\ a\_{T}&=0,\quad\overline{Y}\_{i,T}=0,\quad 1\leq i\leq I.\end{split} | |  | (5.2) |

We will show that there exists an 𝒮∞×bmo{\mathcal{S}}^{\infty}\times\text{bmo} solution to ([5.2](https://arxiv.org/html/2601.07626v1#S5.E2 "In Proof of Proposition 3.4. ‣ 5 Proofs")). Then for each i=1,…,Ii=1,\ldots,I, taking Yi:=Y¯i+εi​(Li)−ℒiY\_{i}:=\overline{Y}\_{i}+\varepsilon\_{i}(L\_{i})-{\mathcal{L}}\_{i} and Zi:=Z¯i+σεi−σℒiZ\_{i}:=\overline{Z}\_{i}+\sigma\_{\varepsilon\_{i}}-\sigma\_{{\mathcal{L}}\_{i}} gives us the solution ((a,Za),(Yi,Zi)1≤i≤I)\big((a,Z\_{a}),(Y\_{i},Z\_{i})\_{1\leq i\leq I}\big) to the BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")). The uniform boundedness of σεi\sigma\_{\varepsilon\_{i}} and σℒi\sigma\_{{\mathcal{L}}\_{i}} established in Proposition [3.3](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3 Equilibrium construction") ensures that Zi∈bmoZ\_{i}\in\text{bmo} if and only if Z¯i∈bmo\overline{Z}\_{i}\in\text{bmo}.

Since the (a,Za)(a,Z\_{a}) equation decouples, we prove the existence of its solution first. For each N≥1N\geq 1, we consider a truncated equation,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​a(N)=Za(N)dB+(ρΣ+αΣ(μD+με−μℒ)−12(αΣ(σD+σε−σℒ)−Za(N))2−exp(−max(a,−N)))dt,aT(N)=0.\displaystyle\begin{split}da^{(N)}&=Z\_{a}^{(N)}\,dB+\left(\rho\_{\Sigma}+\alpha\_{\Sigma}(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}})-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}^{(N)}\big)^{2}\right.\\ &\left.\quad\quad\quad\quad\quad\quad\phantom{\frac{1}{2}}-\exp(-\max(a,-N))\right)dt,\\ a^{(N)}\_{T}&=0.\end{split} | |  | (BSDEN) |

Proposition 2 of Tevzadze [[12](https://arxiv.org/html/2601.07626v1#bib.bib50 "Solvability of backward stochastic differential equations with quadratic growth")] implies that there exists a unique 𝒮∞×bmo{\mathcal{S}}^{\infty}\times\text{bmo} solution (a(N),Za(N))\big(a^{(N)},Z\_{a}^{(N)}\big). Since (a(N)−∫0⋅(ρΣ​αΣ​(μD+με−μℒ)))\big(a^{(N)}-\int\_{0}^{\cdot}\left(\rho\_{\Sigma}\alpha\_{\Sigma}\left(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}}\right)\right)\big) is a supermartingale, for each t∈[0,T]t\in[0,T], we have

|  |  |  |
| --- | --- | --- |
|  | at(N)≥𝔼​[aT(N)−∫tT(ρΣ+αΣ​(μD+με−μℒ))​𝑑t|ℱt]≥−C,a^{(N)}\_{t}\geq\mathbb{E}\left[a^{(N)}\_{T}-\int\_{t}^{T}\big(\rho\_{\Sigma}+\alpha\_{\Sigma}\left(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}}\right)\big)dt\,\Big|\,{\mathcal{F}}\_{t}\right]\geq-C, |  |

where CC is a constant that is independent of NN. We derive CC by using bounds on με\mu\_{\varepsilon} and μℒ\mu\_{\mathcal{L}} guaranteed by Proposition [3.3](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3 Equilibrium construction"). For N≥CN\geq C and x≥−Cx\geq-C, we have −exp⁡(−max⁡(x,−N))=−e−x-\exp(-\max(x,-N))=-e^{-x}, so the lower bound on a(N)a^{(N)} guarantees that (a(N),Za(N))\big(a^{(N)},Z^{(N)}\_{a}\big) solves (BSDEC\text{BSDE}\_{C}). Moreover, uniqueness of (a(N),Za(N))\big(a^{(N)},Z^{(N)}\_{a}\big) as a solution to (BSDEC\text{BSDE}\_{C}) implies that (a(N),Za(N))=(a(C),Za(C))\big(a^{(N)},Z^{(N)}\_{a}\big)=\big(a^{(C)},Z^{(C)}\_{a}\big) for every N≥CN\geq C and (a(C),Za(C))\big(a^{(C)},Z^{(C)}\_{a}\big) solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​a=Za​d​B+(ρΣ+αΣ​(μD+με−μℒ)−12​(αΣ​(σD+σε−σℒ)−Za)2−exp⁡(−a))​d​t,da=Z\_{a}\,dB+\left(\rho\_{\Sigma}+\alpha\_{\Sigma}(\mu\_{D}+\mu\_{\varepsilon}-\mu\_{\mathcal{L}})-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)^{2}-\exp(-a)\right)dt, |  | (5.3) |

with aT=0a\_{T}=0. Thus, (a(C),Za(C))\big(a^{(C)},Z^{(C)}\_{a}\big) is the unique 𝒮∞×bmo{\mathcal{S}}^{\infty}\times\text{bmo} solution to ([5.3](https://arxiv.org/html/2601.07626v1#S5.E3 "In Proof of Proposition 3.4. ‣ 5 Proofs")) with aT=0a\_{T}=0.

Let (a,Za)(a,Z\_{a}) be the unique 𝒮∞×bmo{\mathcal{S}}^{\infty}\times\text{bmo} solution to ([5.3](https://arxiv.org/html/2601.07626v1#S5.E3 "In Proof of Proposition 3.4. ‣ 5 Proofs")) with aT=0a\_{T}=0. Most standard BSDE existence results require boundedness of the (t,ω)(t,\omega)-dependent driver terms. For the driver of (Y¯i,Z¯i)(\overline{Y}\_{i},\overline{Z}\_{i}) in ([5.2](https://arxiv.org/html/2601.07626v1#S5.E2 "In Proof of Proposition 3.4. ‣ 5 Proofs")), Za∈bmoZ\_{a}\in\text{bmo} cannot be guaranteed to be bounded. We apply the linear BSDE results of Jackson and Žitković [[7](https://arxiv.org/html/2601.07626v1#bib.bib36 "Existence and uniqueness for non-Markovian triangular quadratic BSDEs")] to obtain the existence and uniqueness of (Y¯i,Z¯i)(\overline{Y}\_{i},\overline{Z}\_{i}) in

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Y¯i\displaystyle d\overline{Y}\_{i} | =Z¯idB+1αi(−ρi+αi(μℒi−μεi)+1+a+αi​Yi¯exp⁡(a)−12(αΣ(σD+σε−σℒ)−Za)2\displaystyle=\overline{Z}\_{i}\,dB+\frac{1}{\alpha\_{i}}\left(-\rho\_{i}+\alpha\_{i}(\mu\_{{\mathcal{L}}\_{i}}-\mu\_{\varepsilon\_{i}})+\frac{1+a+\alpha\_{i}\overline{Y\_{i}}}{\exp(a)}-\frac{1}{2}\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)^{2}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +αi(Zi¯+σεi−σℒi)(αΣ(σD+σε−σℒ)−Za))dt\displaystyle\quad\quad\quad\quad\quad\quad\left.\phantom{\frac{(Y\_{i})}{A}}+\alpha\_{i}\left(\overline{Z\_{i}}+\sigma\_{\varepsilon\_{i}}-\sigma\_{{\mathcal{L}}\_{i}}\right)\big(\alpha\_{\Sigma}(\sigma\_{D}+\sigma\_{\varepsilon}-\sigma\_{\mathcal{L}})-Z\_{a}\big)\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Y¯i,T\displaystyle\overline{Y}\_{i,T} | =0.\displaystyle=0. |  |

Using the notation “α\alpha” of Jackson and Žitković [[7](https://arxiv.org/html/2601.07626v1#bib.bib36 "Existence and uniqueness for non-Markovian triangular quadratic BSDEs")], we have that α=exp⁡(−a)\alpha=\exp(-a) is sliceable due to its boundedness. Since our BSDE is of dimension one, Jackson and Žitković [[7](https://arxiv.org/html/2601.07626v1#bib.bib36 "Existence and uniqueness for non-Markovian triangular quadratic BSDEs")] Proposition 2.4 and Corollary 2.10 (item 2) imply that there exists a unique solution (Y¯i,Z¯i)∈𝒮∞×bmo(\overline{Y}\_{i},\overline{Z}\_{i})\in{\mathcal{S}}^{\infty}\times\text{bmo}.

Therefore, combining the existence and uniqueness for these uncoupled, one-dimensional BSDEs, we have that there exists a unique 𝒮∞×bmo{\mathcal{S}}^{\infty}\times\text{bmo} solution to ([5.2](https://arxiv.org/html/2601.07626v1#S5.E2 "In Proof of Proposition 3.4. ‣ 5 Proofs")), as desired.

∎

Lemma [5.1](https://arxiv.org/html/2601.07626v1#S5.Thmtheorem1 "Lemma 5.1. ‣ 5 Proofs") will be used below in the proof of Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction").

###### Lemma 5.1.

For i=1,…,Ii=1,\ldots,I, let LL be a (0,1)(0,1)-valued progressively measurable process and (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L) be admissible strategies with the corresponding wealth process X=θ​A+π​SX=\theta A+\pi S. For t∈[0,T]t\in[0,T], we let

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Wt:=−exp⁡(−ρi​t−αi​(XtAt+Yi,t)),Vt:=−∫0te−ρi​s−αi​cs​ui​(Ls)​𝑑s+Wt.\displaystyle\begin{split}W\_{t}&:=-\exp\left(-\rho\_{i}t-\alpha\_{i}\left(\frac{X\_{t}}{A\_{t}}+Y\_{i,t}\right)\right),\\ V\_{t}&:=-\int\_{0}^{t}e^{-\rho\_{i}s-\alpha\_{i}c\_{s}}u\_{i}(L\_{s})ds+W\_{t}.\end{split} | |  | (5.4) |

Then, VV is a supermartingale. Moveover, for LiL\_{i} defined in Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction") and (πi,θi,ci)(\pi\_{i},\theta\_{i},c\_{i}) given in Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction"), we have (πi,θi,ci)∈𝒜i​(Li)(\pi\_{i},\theta\_{i},c\_{i})\in{\mathcal{A}}\_{i}(L\_{i}) and the corresponding process VV is a martingale.

###### Proof.

Let (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L) be given. The dynamics of VV can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt=μV,t​d​t+σV,t​d​B,t∈[0,T],\displaystyle dV\_{t}=\mu\_{V,t}dt+\sigma\_{V,t}dB,\quad t\in[0,T], |  | (5.5) |

where μV,t=(𝖨)+(𝖨𝖨)+(𝖨𝖨𝖨)\mu\_{V,t}=(\mathsf{I})+(\mathsf{II})+(\mathsf{III}) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝖨)\displaystyle(\mathsf{I}) | =−WtAt​(1+at+αi​(Yi,t−ct+XtAt)+log⁡(ui​(Lt)))−e−ρi​t−αi​ct​ui​(Lt),\displaystyle=-\frac{W\_{t}}{A\_{t}}\left(1+a\_{t}+\alpha\_{i}\left(Y\_{i,t}-c\_{t}+\frac{X\_{t}}{A\_{t}}\right)+\log(u\_{i}(L\_{t}))\right)-e^{-\rho\_{i}t-\alpha\_{i}c\_{t}}u\_{i}(L\_{t}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝖨𝖨)\displaystyle(\mathsf{II}) | =αi​WtAt​(εi,t​(Li,t)−εi,t​(Lt)−1αi​log⁡(ui​(Li,t))+1αi​log⁡(ui​(Lt))),\displaystyle=\frac{\alpha\_{i}W\_{t}}{A\_{t}}\left(\varepsilon\_{i,t}(L\_{i,t})-\varepsilon\_{i,t}(L\_{t})-\frac{1}{\alpha\_{i}}\log(u\_{i}(L\_{i,t}))+\frac{1}{\alpha\_{i}}\log(u\_{i}(L\_{t}))\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝖨𝖨𝖨)\displaystyle(\mathsf{III}) | =Wt2​(κt−Za,t−αi​Zi,t−αi​πt​σS,tAt)2.\displaystyle=\frac{W\_{t}}{2}\left(\kappa\_{t}-Z\_{a,t}-\alpha\_{i}Z\_{i,t}-\frac{\alpha\_{i}\pi\_{t}\sigma\_{S,t}}{A\_{t}}\right)^{2}. |  |

By Fenchel’s inequality, for all x∈ℝx\in\mathbb{R} and y>0y>0,

|  |  |  |
| --- | --- | --- |
|  | −e−αi​x≤yαi​(log⁡(yαi)−1)+x​y.-e^{-\alpha\_{i}x}\leq\frac{y}{\alpha\_{i}}\left(\log\left(\frac{y}{\alpha\_{i}}\right)-1\right)+xy. |  |

By taking x=ct+ρiαi​t−1αi​log⁡(ui​(Lt))x=c\_{t}+\frac{\rho\_{i}}{\alpha\_{i}}t-\frac{1}{\alpha\_{i}}\log(u\_{i}(L\_{t})) and y=−αi​WtAty=-\frac{\alpha\_{i}W\_{t}}{A\_{t}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −e−αi​x\displaystyle-e^{-\alpha\_{i}x} | =−e−αi​ct−ρi​t​ui​(Lt),\displaystyle=-e^{-\alpha\_{i}c\_{t}-\rho\_{i}t}u\_{i}(L\_{t}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(yαi)\displaystyle\log\left(\frac{y}{\alpha\_{i}}\right) | =−at−ρi​t−αi​(XtAt+Yi,t).\displaystyle=-a\_{t}-\rho\_{i}t-\alpha\_{i}\left(\frac{X\_{t}}{A\_{t}}+Y\_{i,t}\right). |  |

Putting this together yields (𝖨)≤0(\mathsf{I})\leq 0 with (𝖨)=0(\mathsf{I})=0 when ct=ci,tc\_{t}=c\_{i,t}, as defined in ([3.7](https://arxiv.org/html/2601.07626v1#S3.E7 "In Theorem 3.5. ‣ 3 Equilibrium construction")) and Lt=Li,tL\_{t}=L\_{i,t}, as in Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction").

In Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction"), Li,tL\_{i,t} is chosen to maximize l↦αi​εi,t​(l)−log⁡(ui​(l))l\mapsto\alpha\_{i}\varepsilon\_{i,t}(l)-\log\big(u\_{i}(l)\big) over l∈(0,1)l\in(0,1). Thus, for all l∈(0,1)l\in(0,1), we have

|  |  |  |
| --- | --- | --- |
|  | εi,t​(Li,t)−1αi​log⁡(ui​(Li,t))≥εi,t​(l)−1αi​log⁡(ui​(l)).\varepsilon\_{i,t}(L\_{i,t})-\frac{1}{\alpha\_{i}}\log\big(u\_{i}(L\_{i,t})\big)\geq\varepsilon\_{i,t}(l)-\frac{1}{\alpha\_{i}}\log\big(u\_{i}(l)\big). |  |

Since WW takes negative values, (𝖨𝖨)≤0(\mathsf{II})\leq 0. We have (𝖨𝖨)=0(\mathsf{II})=0 when Lt=Li,tL\_{t}=L\_{i,t}, as in Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction").

Since WW takes negative values, (𝖨𝖨𝖨)≤0(\mathsf{III})\leq 0. Moreover, (𝖨𝖨𝖨)=0(\mathsf{III})=0 exactly when

|  |  |  |
| --- | --- | --- |
|  | κt−Za,t−αi​Zi,t−αi​πt​σS,tAt=0,\kappa\_{t}-Z\_{a,t}-\alpha\_{i}Z\_{i,t}-\frac{\alpha\_{i}\pi\_{t}\sigma\_{S,t}}{A\_{t}}=0, |  |

which is satisfied by πt=πi,t\pi\_{t}=\pi\_{i,t}, as in ([3.5](https://arxiv.org/html/2601.07626v1#S3.E5 "In Theorem 3.5. ‣ 3 Equilibrium construction")).

Thus, VV is a local supermartingale for every labor proportion LL and (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L). By item [3](https://arxiv.org/html/2601.07626v1#S2.I1.i3 "item 3 ‣ Definition 2.1. ‣ 2 Model setting") of Definition [2.1](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Model setting") of admissibility, the local martinagle component ∫0⋅σV​𝑑B\int\_{0}^{\cdot}\sigma\_{V}dB is a martinagle, which ensures that the local supermartingale VV is, in fact, a supermartingale.

It remains to be shown that (πi,θi,ci)∈𝒜i​(Li)(\pi\_{i},\theta\_{i},c\_{i})\in{\mathcal{A}}\_{i}(L\_{i}), meaning that the proposed optimal strategies are admissible. Item [1](https://arxiv.org/html/2601.07626v1#S2.I1.i1 "item 1 ‣ Definition 2.1. ‣ 2 Model setting") in Definition [2.1](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Model setting") is readily checked, and verifying item [2](https://arxiv.org/html/2601.07626v1#S2.I1.i2 "item 2 ‣ Definition 2.1. ‣ 2 Model setting") uses ([2.3](https://arxiv.org/html/2601.07626v1#S2.E3 "In 2 Model setting")) and ([3.6](https://arxiv.org/html/2601.07626v1#S3.E6 "In Theorem 3.5. ‣ 3 Equilibrium construction")) to calculate the dynamics of XiX\_{i} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xi\displaystyle dX\_{i} | =A​d​(XiA)+XiA​d​A+d​⟨XiA,A⟩\displaystyle=A\,d\left(\frac{X\_{i}}{A}\right)+\frac{X\_{i}}{A}dA+d\left\langle\frac{X\_{i}}{A},A\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(πi​μS+Xi​μA+εi​(Li)−ci)​d​t+πi​σS​d​B\displaystyle=\big(\pi\_{i}\mu\_{S}+X\_{i}\mu\_{A}+\varepsilon\_{i}(L\_{i})-c\_{i}\big)dt+\pi\_{i}\sigma\_{S}dB |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =πi​(d​S+D​d​t)+θi​(d​A+d​t)+(εi​(Li)−ci)​d​t.\displaystyle=\pi\_{i}\big(dS+D\,dt\big)+\theta\_{i}\big(dA+dt\big)+(\varepsilon\_{i}(L\_{i})-c\_{i})dt. |  |

The delicate point is to check the integrability in item [3](https://arxiv.org/html/2601.07626v1#S2.I1.i3 "item 3 ‣ Definition 2.1. ‣ 2 Model setting") Definition [2.1](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Model setting"). For t∈[0,T]t\in[0,T], we let

|  |  |  |
| --- | --- | --- |
|  | Wi,t:=−exp⁡(−ρi​t−αi​(Xi,tAt+Yi,t))andVi,t:=−∫0te−ρi​s−αi​ci,s​ui​(Li,s)​𝑑s+Wi,t.W\_{i,t}:=-\exp\left(-\rho\_{i}t-\alpha\_{i}\left(\frac{X\_{i,t}}{A\_{t}}+Y\_{i,t}\right)\right)\quad\text{and}\quad V\_{i,t}:=-\int\_{0}^{t}e^{-\rho\_{i}s-\alpha\_{i}c\_{i,s}}u\_{i}(L\_{i,s})ds+W\_{i,t}. |  |

By Itô’s Lemma and ([3.7](https://arxiv.org/html/2601.07626v1#S3.E7 "In Theorem 3.5. ‣ 3 Equilibrium construction")), we observe that

|  |  |  |
| --- | --- | --- |
|  | d​Vi=e−∫0⋅1As​𝑑s​d​(Wi​e∫0⋅1As​𝑑s)andd​(Wi​e∫0⋅1As​𝑑s)=Wi​e∫0⋅1As​𝑑s​(αi​(πi​σSA+Zi))​d​B.dV\_{i}=e^{-\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds}d\left(W\_{i}e^{\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds}\right)\quad\text{and}\quad d\left(W\_{i}e^{\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds}\right)=W\_{i}e^{\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds}\left(\alpha\_{i}\left(\frac{\pi\_{i}\sigma\_{S}}{A}+Z\_{i}\right)\right)dB. |  |

Since αi​(πi​σSA+Zi)∈bmo\alpha\_{i}\left(\frac{\pi\_{i}\sigma\_{S}}{A}+Z\_{i}\right)\in\text{bmo}, Theorem 3.2 of Kazamaki [[8](https://arxiv.org/html/2601.07626v1#bib.bib41 "Continuous exponential martingales and bmo")] implies that Wi​e∫0⋅1As​𝑑sW\_{i}e^{\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds} is a martingale with 𝔼​[⟨Wi​e∫0⋅1As​𝑑s⟩T]<∞\mathbb{E}\left[\sqrt{\left<W\_{i}e^{\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds}\right>\_{T}}\,\right]<\infty. The uniform boundedness of e−∫0⋅1As​𝑑se^{-\int\_{0}^{\cdot}\frac{1}{A\_{s}}ds}, implies that 𝔼​[⟨Vi⟩T]<∞\mathbb{E}\left[\sqrt{\left<V\_{i}\right>\_{T}}\,\right]<\infty. Thus, the local martingale ViV\_{i} is a martingale, as desired.

∎

###### Proof of Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction").

We fix λk​e​e​p∈[0,1]\lambda\_{keep}\in[0,1], λu​b​i∈[0,1−λk​e​e​p]\lambda\_{ubi}\in[0,1-\lambda\_{keep}], and δ∈ℝ\delta\in\mathbb{R}. Let the labor proportions LiL\_{i} for 1≤i≤I1\leq i\leq I be defined by Definition [3.1](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Equilibrium construction") and labor response functions Λji\Lambda^{i}\_{j} for 1≤i,j≤I1\leq i,j\leq I with j≠ij\neq i be defined by Definition [3.2](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem2 "Definition 3.2. ‣ 3 Equilibrium construction"). By applying Proposition [3.4](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 Equilibrium construction"), we obtain the unique solution ((a,Za),(Yi,Zi)1≤i≤I)\big((a,Z\_{a}),(Y\_{i},Z\_{i})\_{1\leq i\leq I}\big) to the BSDE system ([3.2](https://arxiv.org/html/2601.07626v1#S3.E2 "In 3 Equilibrium construction")). Define the equilibrium price processes, strategies, and dynamics terms as in the statement of Theorem [3.5](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Equilibrium construction").

We must check that all of the conditions from Definition [2.2](https://arxiv.org/html/2601.07626v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2 Model setting") are satisfied.

Optimality. Let i∈{1,…,I}i\in\{1,\ldots,I\} be given. Lemma [5.1](https://arxiv.org/html/2601.07626v1#S5.Thmtheorem1 "Lemma 5.1. ‣ 5 Proofs") proves that (πi,θi,ci)∈𝒜i​(Li)(\pi\_{i},\theta\_{i},c\_{i})\in{\mathcal{A}}\_{i}(L\_{i}).

Suppose that LL is a progressively measurable (0,1)(0,1)-valued process, and (π,θ,c)∈𝒜i​(L)(\pi,\theta,c)\in{\mathcal{A}}\_{i}(L). Let X=θ​A+π​SX=\theta A+\pi S denote the wealth process formed from the admissible triple of strategies (π,θ,c)(\pi,\theta,c) with the perceived income process εi​(L)\varepsilon\_{i}(L). Define VV and WW as in ([5.4](https://arxiv.org/html/2601.07626v1#S5.E4 "In Lemma 5.1. ‣ 5 Proofs")), and let ViV\_{i} be defined for t∈[0,T]t\in[0,T] by

|  |  |  |
| --- | --- | --- |
|  | Vi,t:=−∫0te−ρi​s−αi​ci,s​ui​(Li,s)​𝑑s−exp⁡(−ρi​t−αi​(Xi,tAt+Yi,t)).V\_{i,t}:=-\int\_{0}^{t}e^{-\rho\_{i}s-\alpha\_{i}c\_{i,s}}u\_{i}(L\_{i,s})ds-\exp\left(-\rho\_{i}t-\alpha\_{i}\left(\frac{X\_{i,t}}{A\_{t}}+Y\_{i,t}\right)\right). |  |

Lemma [5.1](https://arxiv.org/html/2601.07626v1#S5.Thmtheorem1 "Lemma 5.1. ‣ 5 Proofs") tells us that VV is a supermartingale and ViV\_{i} is a martingale. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼\displaystyle\mathbb{E} | [−∫0Te−ρi​t−αi​ct​ui​(Lt)​𝑑t−e−ρi​T−αi​(XT+εi,T​(Li,T))​ui​(LT)]\displaystyle\left[-\int\_{0}^{T}e^{-\rho\_{i}t-\alpha\_{i}c\_{t}}u\_{i}(L\_{t})dt-e^{-\rho\_{i}T-\alpha\_{i}(X\_{T}+\varepsilon\_{i,T}(L\_{i,T}))}u\_{i}(L\_{T})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[VT]≤V0=−exp⁡(−αi​(X0A0+Yi,0))\displaystyle=\mathbb{E}[V\_{T}]\leq V\_{0}=-\exp\left(-\alpha\_{i}\left(\tfrac{X\_{0}}{A\_{0}}+Y\_{i,0}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Vi,0=𝔼​[Vi,T]\displaystyle=V\_{i,0}=\mathbb{E}[V\_{i,T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[−∫0Te−ρi​t−αi​ci,t​ui​(Li,t)​𝑑t−e−ρ​T−αi​(Xi,T+εi,T​(Li,T))​ui​(Li,T)].\displaystyle=\mathbb{E}\left[-\int\_{0}^{T}e^{-\rho\_{i}t-\alpha\_{i}c\_{i,t}}u\_{i}(L\_{i,t})dt-e^{-\rho T-\alpha\_{i}(X\_{i,T}+\varepsilon\_{i,T}(L\_{i,T}))}u\_{i}(L\_{i,T})\right]. |  |

Therefore, the triple of strategies (πi,θi,ci)∈𝒜i​(Li)(\pi\_{i},\theta\_{i},c\_{i})\in{\mathcal{A}}\_{i}(L\_{i}) with labor proportion LiL\_{i} is optimal for agent ii.

Consistency. By Definition [3.2](https://arxiv.org/html/2601.07626v1#S3.Thmtheorem2 "Definition 3.2. ‣ 3 Equilibrium construction"), for 1≤i,j≤I1\leq i,j\leq I with i≠ji\neq j, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λji​(Li)=δ​wiwj​(Li−Li)+Lj=Lj,\displaystyle\Lambda^{i}\_{j}(L\_{i})=\delta\frac{w\_{i}}{w\_{j}}(L\_{i}-L\_{i})+L\_{j}=L\_{j}, |  | (5.6) |

as desired. Recall that wjw\_{j} is nonzero for all t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s. In that case, Λji​(Li)\Lambda^{i}\_{j}(L\_{i}) is defined to be LjL\_{j} and, thus, satisfies the consistency condition.

On-equilibrium perceptions align with reality. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Iεi​(Li)\displaystyle\sum\_{i=1}^{I}\varepsilon\_{i}(L\_{i}) | =∑i=1I(λk​e​e​p​wi​Li+λu​b​iI​(wi​Li+∑j≠iwj​Λji​(Li)))by ([2.1](https://arxiv.org/html/2601.07626v1#S2.E1 "In 2 Model setting"))\displaystyle=\sum\_{i=1}^{I}\left(\lambda\_{keep}w\_{i}L\_{i}+\frac{\lambda\_{ubi}}{I}\left(w\_{i}L\_{i}+\sum\_{j\neq i}w\_{j}\Lambda^{i}\_{j}(L\_{i})\right)\right)\quad\text{by \eqref{def:preceived-income}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1I(λk​e​e​p​wi​Li+λu​b​iI​(wi​Li+∑j≠iwj​Lj))by ([5.6](https://arxiv.org/html/2601.07626v1#S5.E6 "In Proof of Theorem 3.5. ‣ 5 Proofs"))\displaystyle=\sum\_{i=1}^{I}\left(\lambda\_{keep}w\_{i}L\_{i}+\frac{\lambda\_{ubi}}{I}\left(w\_{i}L\_{i}+\sum\_{j\neq i}w\_{j}L\_{j}\right)\right)\quad\text{by \eqref{calc:delta}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(∑i=1Iwi​Li)​(λk​e​e​p+λu​b​iI+(I−1)​λu​b​iI)\displaystyle=\left(\sum\_{i=1}^{I}w\_{i}L\_{i}\right)\left(\lambda\_{keep}+\frac{\lambda\_{ubi}}{I}+(I-1)\frac{\lambda\_{ubi}}{I}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(λk​e​e​p+λu​b​i)​∑i=1Iwi​Li.\displaystyle=\left(\lambda\_{keep}+\lambda\_{ubi}\right)\sum\_{i=1}^{I}w\_{i}L\_{i}. |  |

Market clearing. For the stock market, on {σS=0}\{\sigma\_{S}=0\}, we have ∑i=1Iπi=∑i=1Iπi,0−=1\sum\_{i=1}^{I}\pi\_{i}=\sum\_{i=1}^{I}\pi\_{i,0-}=1, while when σS≠0\sigma\_{S}\neq 0,

|  |  |  |
| --- | --- | --- |
|  | ∑i=1Iπi​σS=∑i=1IAαi​(κ−σA−αi​Zi)=AαΣ​(κ−σA−αΣ​ZΣ)=σS,\sum\_{i=1}^{I}\pi\_{i}\sigma\_{S}=\sum\_{i=1}^{I}\frac{A}{\alpha\_{i}}(\kappa-\sigma\_{A}-\alpha\_{i}Z\_{i})=\frac{A}{\alpha\_{\Sigma}}(\kappa-\sigma\_{A}-\alpha\_{\Sigma}Z\_{\Sigma})=\sigma\_{S}, |  |

by ([3.5](https://arxiv.org/html/2601.07626v1#S3.E5 "In Theorem 3.5. ‣ 3 Equilibrium construction")) and ([3.4](https://arxiv.org/html/2601.07626v1#S3.E4 "In 3 Equilibrium construction")).

To see that we have clearing in the annuity and real goods market, we will prove that ∑i=1IXi=S+A\sum\_{i=1}^{I}X\_{i}=S+A. If ∑i=1IXi=S+A\sum\_{i=1}^{I}X\_{i}=S+A holds, then the annuity market clears using that Xi=θi​A+πi​SX\_{i}=\theta\_{i}A+\pi\_{i}S for i=1,…,Ii=1,\ldots,I, and the real goods market clears by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Ici\displaystyle\sum\_{i=1}^{I}c\_{i} | =1A​∑i=1IXi+aαΣ+YΣ+ℒΣ\displaystyle=\frac{1}{A}\sum\_{i=1}^{I}X\_{i}+\frac{a}{\alpha\_{\Sigma}}+Y\_{\Sigma}+{\mathcal{L}}\_{\Sigma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =SA+1+aαΣ+YΣ+ℒΣusing that ∑i=1IXi=S+A\displaystyle=\frac{S}{A}+1+\frac{a}{\alpha\_{\Sigma}}+Y\_{\Sigma}+{\mathcal{L}}\_{\Sigma}\quad\text{using that $\sum\_{i=1}^{I}X\_{i}=S+A$} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1+D+∑i=1Iεi​(Li)by definition of S in ([3.3](https://arxiv.org/html/2601.07626v1#S3.E3 "In 3 Equilibrium construction")).\displaystyle=1+D+\sum\_{i=1}^{I}\varepsilon\_{i}(L\_{i})\quad\text{by definition of $S$ in \eqref{def:prices}}. |  |

We proceed to prove that ∑i=1IXi=S+A\sum\_{i=1}^{I}X\_{i}=S+A. One can verify by using the dynamics of XiA\frac{X\_{i}}{A} from ([3.6](https://arxiv.org/html/2601.07626v1#S3.E6 "In Theorem 3.5. ‣ 3 Equilibrium construction")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(∑i=1IXiA)\displaystyle d\left(\sum\_{i=1}^{I}\frac{X\_{i}}{A}\right) | =1A​((εΣ−aαΣ−YΣ−ℒΣ)+μS−σA​σS)​d​t+σSA​d​B\displaystyle=\frac{1}{A}\left(\left(\varepsilon\_{\Sigma}-\frac{a}{\alpha\_{\Sigma}}-Y\_{\Sigma}-{\mathcal{L}}\_{\Sigma}\right)+\mu\_{S}-\sigma\_{A}\sigma\_{S}\right)dt+\frac{\sigma\_{S}}{A}dB |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1A​(SA−D+μS−σA​σS)​d​t+σSA​d​B\displaystyle=\frac{1}{A}\left(\frac{S}{A}-D+\mu\_{S}-\sigma\_{A}\sigma\_{S}\right)dt+\frac{\sigma\_{S}}{A}dB |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d​(SA)=d​(S+AA).\displaystyle=d\left(\frac{S}{A}\right)=d\left(\frac{S+A}{A}\right). |  |

Since the processes XiX\_{i} are continuous and have ∑i=1IXi,0=∑i=1I(θi,0−​A0+πi,0−​S0)=A0+S0\sum\_{i=1}^{I}X\_{i,0}=\sum\_{i=1}^{I}\left(\theta\_{i,0-}A\_{0}+\pi\_{i,0-}S\_{0}\right)=A\_{0}+S\_{0}, we have that

|  |  |  |
| --- | --- | --- |
|  | 1A​∑i=1IXi=S+AA.\frac{1}{A}\sum\_{i=1}^{I}X\_{i}=\frac{S+A}{A}. |  |

Thus, ∑i=1IXi=S+A\sum\_{i=1}^{I}X\_{i}=S+A.
∎

Funding: No funding, grants, or other support was received to assist with the preparation of this manuscript.

Competing Interests: The author has no relevant financial or non-financial interests to disclose.

Data availability statement: No new data were created or analyzed in this study. Data sharing is not applicable to this article.

## References

* [1]
  S. Basak (1999)
  On the fluctuations in consumption and market returns in the presence of labor and human capital: an equilibrium analysis.
  Journal of Economic Dynamics and Control 23 (7),  pp. 1029–1064.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p5.1 "1 Introduction").
* [2]
  Z. Bodie, R. C. Merton, and W. F. Samuelson (1992)
  Labour supply flexibility and portfolio choice in a life cycle model.
  Journal of Economic Dynamics & Control 16 (3-4),  pp. 427–449.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p5.1 "1 Introduction").
* [3]
  X. Chen, J. H. Choi, K. Larsen, and D. J. Seppi (2023)
  Price impact in Nash equilibria.
  Finance and Stochastics 27,  pp. 305–340.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p4.1 "1 Introduction"),
  [§2](https://arxiv.org/html/2601.07626v1#S2.p9.1 "2 Model setting").
* [4]
  P. O. Christensen and K. Larsen (2014)
  Incomplete continuous-time securities markets with stochastic income volatility.
  Review of Asset Pricing Studies 4 (2),  pp. 247–285.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p3.1 "1 Introduction").
* [5]
  P. J. Gertler, S. W. Martinez, and M. Rubio-Codina (2012-01)
  Investing cash transfers to raise long-term living standards.
  American Economic Journal: Applied Economics 4 (1),  pp. 164–92.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p2.1 "1 Introduction").
* [6]
  C. Hughes (2018)
  Fair shot: rethinking inequality and how we earn.
   St. Martin’s Books, New York.
  Cited by: [footnote 2](https://arxiv.org/html/2601.07626v1#footnote2 "In 1 Introduction").
* [7]
  J. Jackson and G. Žitković (2022)
  Existence and uniqueness for non-Markovian triangular quadratic BSDEs.
  SIAM Journal on Control and Optimization 60 (3),  pp. 1642–1666.
  Cited by: [§5](https://arxiv.org/html/2601.07626v1#S5.10.p4.3 "Proof of Proposition 3.4. ‣ 5 Proofs"),
  [§5](https://arxiv.org/html/2601.07626v1#S5.9.p3.7 "Proof of Proposition 3.4. ‣ 5 Proofs").
* [8]
  N. Kazamaki (1994)
  Continuous exponential martingales and bmo.
   Springer-Verlag.
  Cited by: [§2](https://arxiv.org/html/2601.07626v1#S2.p2.10 "2 Model setting"),
  [§5](https://arxiv.org/html/2601.07626v1#S5.18.p6.7 "Proof. ‣ 5 Proofs").
* [9]
  T. Kenc (2004)
  Taxation, risk-taking and growth: a continuous-time stochastic general equilibrium analysis with labor-leisure choice.
  Journal of Economic Dynamics & Control 28,  pp. 1511–1539.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p5.1 "1 Introduction").
* [10]
  L. Kueng (2018-11)
  Excess sensitivity of high-income consumers.
  The Quarterly Journal of Economics 133 (4),  pp. 1693–1751.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p2.1 "1 Introduction").
* [11]
  J. Peetz and J. R. S. Xuereb (2021-05)
  The role of income volatility and perceived locus of control in financial planning decisions.
  Frontiers in Psychology 12.
  Cited by: [footnote 2](https://arxiv.org/html/2601.07626v1#footnote2 "In 1 Introduction").
* [12]
  R. Tevzadze (2008)
  Solvability of backward stochastic differential equations with quadratic growth.
  Stochastic Processes and their Applications 118,  pp. 503–515.
  Cited by: [§5](https://arxiv.org/html/2601.07626v1#S5.8.p2.6 "Proof of Proposition 3.4. ‣ 5 Proofs").
* [13]
  D. Vayanos (1999)
  Strategic trading and welfare in a dynamic market.
  Review of Economic Studies 66,  pp. 219–254.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p4.1 "1 Introduction"),
  [§2](https://arxiv.org/html/2601.07626v1#S2.p9.1 "2 Model setting").
* [14]
  S. West, A. Castro, and P. M. Doraiswamy (2023-03)
  Recurring cash transfers to enhance the mental wellbeing of Americans.
  Nature Mental Health 1,  pp. 148–150.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p2.1 "1 Introduction").
* [15]
  K. Weston and G. Žitković (2020)
  An incomplete equilibrium with a stochastic annuity.
  Finance and Stochastics 24,  pp. 359–382.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p3.1 "1 Introduction"),
  [§1](https://arxiv.org/html/2601.07626v1#S1.p6.1 "1 Introduction").
* [16]
  K. Weston (2024-02)
  Existence of an equilibrium with limited participation.
  Finance and Stochastics 28 (2),  pp. 329–361.
  Cited by: [§1](https://arxiv.org/html/2601.07626v1#S1.p3.1 "1 Introduction"),
  [§1](https://arxiv.org/html/2601.07626v1#S1.p6.1 "1 Introduction").
* [17]
  A. Yang (2018)
  The war on normal people: the truth about America’s disappearing jobs and why universal basic income is our future.
   Hachette Books, New York.
  Cited by: [footnote 2](https://arxiv.org/html/2601.07626v1#footnote2 "In 1 Introduction").