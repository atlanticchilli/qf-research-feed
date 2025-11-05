---
authors:
- Hamza Hanbali
- Gaurav Khemka
- Himasha Warnakulasooriya
doc_id: arxiv:2511.01133v1
family_id: arxiv:2511.01133
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension
  Withdrawals and Reduced Deposit'
url_abs: http://arxiv.org/abs/2511.01133v1
url_html: https://arxiv.org/html/2511.01133v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hamza Hanbali
  
Department of Economics, Centre for Actuarial Studies
  
University of Melbourne
  
hamza.hanbali@unimelb.edu.au 
  
Gaurav Khemka
  
Research School of Finance, Actuarial Studies & Statistics
  
Australian National University
  
gaurav.khemka@anu.edu.au 
  
Himasha Warnakulasooriya
  
Department of Econometrics and Business Statistics
  
Monash University
  
himasha.warnakulasooriya@monash.edu

(Version: November 3, 2025)

###### Abstract

The paper analyzes two government policies affecting housing demand: early withdrawal from pension savings (EW), and reduction of loan deposit (RD). A model incorporating demand feedback on housing prices using Australian data shows both policies raise prices in the short run. RD delays or prevents access for low-income households, particularly in supply-constrained markets. EW improves accessibility across groups and is most efficient when full withdrawal is permitted, but can reduce retirement security if pension grows faster than property prices. The results also indicate that unequal outcomes stem not from price surges themselves but from pre-existing market disparities.
  
Keywords: Housing policy; Housing demand; Inequality; Government budget; Supply-constrained housing market;
  
JEL codes: C53, R31, R38

  

## 1 Introduction

Homeownership is elusive for many households despite being a central pillar of wealth accumulation and financial security (Atalay and Edwards, [2022](https://arxiv.org/html/2511.01133v1#bib.bib5), Sodini et al., [2023](https://arxiv.org/html/2511.01133v1#bib.bib23)). Governments worldwide have implemented various subsidies and tax incentives to facilitate access to homeownership. Some of the most popular programs include tax credits or interest deductions, which are known for driving up house prices, and benefiting sellers rather than improving homeownership (Vigdor, [2006](https://arxiv.org/html/2511.01133v1#bib.bib27), Bourassa et al., [2013](https://arxiv.org/html/2511.01133v1#bib.bib9), Fetter, [2013](https://arxiv.org/html/2511.01133v1#bib.bib15), Hilber and Turner, [2014](https://arxiv.org/html/2511.01133v1#bib.bib17), Sommer and Sullivan, [2018](https://arxiv.org/html/2511.01133v1#bib.bib24), Berger et al., [2020](https://arxiv.org/html/2511.01133v1#bib.bib7), Krolage, [2023](https://arxiv.org/html/2511.01133v1#bib.bib20)). This price inflation arises because demand-side interventions increase purchasing power without necessarily increasing supply, particularly in housing markets characterized by inelastic supply (Favara, [2015](https://arxiv.org/html/2511.01133v1#bib.bib14), Carozzi et al., [2024](https://arxiv.org/html/2511.01133v1#bib.bib10)). What remains underexplored is the distributional impact of these policies: Do liquidity shocks that facilitate home purchases exacerbate inequality rather than alleviate it?

The present paper considers two housing policies designed to reduce the upfront cost of homeownership. The first is a reduction in the minimum deposit requirement, supported by a government guarantee (henceforth reduced deposit, or RD). The second combines a reduced deposit threshold with early withdrawal from pension savings to cover the remaining amount (henceforth early withdrawal, or EW). Both policies can be understood as liquidity shocks, though of a different nature from traditional government- or tax-funded subsidies. Importantly, they do not directly increase households’ total wealth, but instead relax liquidity constraints by either reducing the required cash contribution (RD) or unlocking otherwise illiquid retirement savings (EW).

Specifically, the RD policy lowers the immediate liquidity requirement for homeownership by reducing the deposit from the standard 20% (a common benchmark in countries such as Australia, Canada, the United Kingdom, and the United States) to just 5%. While low-deposit mortgages (5% or less) are available in these countries, they typically come at a cost, such as mortgage insurance premiums or higher interest rates. In contrast, the RD policy considered in this paper assumes a government guarantee and imposes no additional borrowing costs on the household.

On the other hand, the EW policy grants individuals access to their own tax-advantaged retirement savings. These savings are typically locked until retirement, but since homeownership itself reduces housing costs in old age, this policy could accelerate that benefit by enabling earlier access to secure housing now rather than later. Early access to pension savings for housing is only feasible within pension systems that assign a specific account balance to each individual, typically Defined Contribution (DC) systems. Unlike Pay-As-You-Go (PAYG) schemes, where current contributions fund current retirees, DC systems accumulate savings in individual accounts that can be accessed under certain conditions. Some countries with mandatory or large-scale DC systems allow housing-related pension withdrawals. This includes Kazakhstan and Singapore, as well as Switzerland, where a legally Defined Benefit (DB) system functions in practice like a DC scheme by allocating individual balances and permitting early withdrawals for homeownership. Other countries, including Canada, New Zealand, and the United States, have shifted towards DC arrangements but have not fully mandated them at the national level. These three countries also allow pension withdrawal under some restrictions. As more countries transition towards hybrid or mandatory DC models, the debate over whether pension savings should be accessible for homeownership is becoming increasingly relevant (Mercer CFA Institute, [2025](https://arxiv.org/html/2511.01133v1#bib.bib22)).

The present paper develops a model of a cohort of renters, segmented by income percentiles, who accumulate savings and pension balances over time in order to purchase a home. A household purchases a property once it can afford the required minimum, which includes the deposit, property transfer taxes, and an additional financial buffer. Affordability is evaluated under each policy scenario (EW or RD) and compared to a benchmark scenario in which households rely solely on savings with a standard deposit requirement. The policies are analyzed under two housing market structures: an equal-affordability market, where all income groups can access properties priced at the same income multiple, and a supply-constrained market, where higher-income households have proportionally greater access to affordable properties than lower-income groups.

The model incorporates an econometric framework for key economic variables (house prices, rent, wages, inflation, borrowing rates, savings rates, and pension returns) which interacts with the lifecycle model through a demand variable. The present study does not aim to assess whether housing policies affect demand; instead, consistent with existing research on demand-side interventions, it assumes that the policies affect demand and, consequently, house prices. The effect of demand is estimated using historical data. Based on this estimated relationship, demand patterns from the simulated population at each period feed into the econometric model, which then adjusts housing prices, creating a feedback loop between household behavior in the lifecycle model and market conditions in the econometric model. The model is calibrated using Australian data and tracks a cohort of 25-year-old employed renters with no savings. The model does not allow inheritance or external financial support and neither accounts for multiple cohorts nor the advantage of those with higher existing savings at the time of implementation. As a result, the model isolates the effect of the policy on a cohort with existing income disparities.

The policy’s effects are evaluated across three dimensions: (i) household financial outcomes, including the likelihood of purchase, the timing of home purchases, and retirement financial security (i.e. retirement income net of housing); (ii) distributional impacts, measured by changes in homeownership access inequality and post-retirement financial security using Gini coefficients; and (iii) fiscal implications for governments, assessed through the net present value of tax revenues and government expenditures.

The focus on Australia in this paper is motivated by two main factors. First, Australia’s retirement system, known as superannuation, is one of the largest and most mature DC systems in the world (Eslake, [2024](https://arxiv.org/html/2511.01133v1#bib.bib13), Mercer CFA Institute, [2025](https://arxiv.org/html/2511.01133v1#bib.bib22)). Second, both housing policies analyzed here were prominent in the lead-up to the 2025 federal election. An EW policy was first introduced by the Liberal-National Coalition in 2022 and re-emerged during the 2025 campaign alongside proposals for mortgage interest deductibility. Supporters argue that EW promotes financial autonomy, supports homeownership, and reduces housing costs in retirement. Critics argue that it contributes to housing price inflation and compromises long-term retirement adequacy by diverting savings toward current homeowners and developers (Eslake, [2024](https://arxiv.org/html/2511.01133v1#bib.bib13), Super Members Council, [2025](https://arxiv.org/html/2511.01133v1#bib.bib25)). The RD policy was proposed by the Labor Party, which won the 2025 election. While both policies aim to lower the effective deposit barrier, EW still requires a top-up from accumulated superannuation savings, making it more restrictive. As a result, RD is expected to exert an upward pressure on housing prices earlier than EW, given its more immediate reduction in liquidity constraints.

The paper finds that, as expected, both policies raise property prices, with a higher peak under EW, but earlier surge under RD. Under the benchmark EW design, modelled on Australian settings (allowing up to 40% withdrawal with a 5% savings contribution), results indicate a modest reduction in the average age of purchase and an increase in purchase probability. By contrast, RD lowers purchase probabilities for lower-income households and widens disparities in entry timing, with particularly adverse effects under supply constraints. These findings remain robust when demand sensitivity in the price equation is doubled or halved. Boundary EW designs (i.e. full withdrawal or no required savings contribution) substantially improve housing accessibility. Restricting access to below-median or bottom-quartile incomes does not materially change outcomes for the unrestricted group. Retirement outcomes depend critically on pension returns. When, as observed historically, pension returns exceed house price growth, retirement security declines under EW. When the two rates are equal, both policies improve retirement outcomes. Overall, RD worsens accessibility by reinforcing inequality and pricing out lower-income households, whereas EW enhances accessibility without disadvantaging low-income groups and is most effective when full withdrawal is permitted. However, allowing full withdrawal may jeopardise retirement security if pension returns substantially exceed property growth.

This paper contributes to the existing studies on EW policies in DC pension systems. The closest related analysis is the report by The Mckell Institute ([2021](https://arxiv.org/html/2511.01133v1#bib.bib26)), which warns that allowing superannuation withdrawals for housing in Australia would primarily inflate property prices without meaningfully increasing homeownership rates. The findings in this paper do not support that conclusion, and instead show that despite the feedback effect between property price and demand, EW can improves housing accessibility without disadvantaging low-income groups. Qualitative discussions in Eslake ([2024](https://arxiv.org/html/2511.01133v1#bib.bib13)) and Super Members Council ([2025](https://arxiv.org/html/2511.01133v1#bib.bib25)), including comparisons with New Zealand’s experience, raise concerns that such policies may exacerbate inequality due to unequal pension balances. The present paper finds that the negative effect on retirement financial security depends on future pension results, and that the Coalition’s EW design does not lead to substantial inequality shifts.

This paper adds to the extensive literature examining the impact of liquidity shocks and housing subsidies on homeownership and property prices. Prior studies have shown that demand-side interventions, such as mortgage credit expansions (Vigdor, [2006](https://arxiv.org/html/2511.01133v1#bib.bib27), Favara, [2015](https://arxiv.org/html/2511.01133v1#bib.bib14)), government-backed homebuyer subsidies (Berger et al., [2020](https://arxiv.org/html/2511.01133v1#bib.bib7), Krolage, [2023](https://arxiv.org/html/2511.01133v1#bib.bib20), Carozzi et al., [2024](https://arxiv.org/html/2511.01133v1#bib.bib10)), and tax incentives like mortgage interest deductions (Bourassa et al., [2013](https://arxiv.org/html/2511.01133v1#bib.bib9), Hilber and Turner, [2014](https://arxiv.org/html/2511.01133v1#bib.bib17), Binner and Day, [2015](https://arxiv.org/html/2511.01133v1#bib.bib8)), tend to increase housing prices without significantly improving homeownership rates, especially in supply-constrained markets. The present paper contributes to this discussion by showing that EW belongs to the class of policies that inflate prices while significantly improving access, whereas RD policies not only increase prices but also reduce the likelihood and delay the timing of homeownership for low-income households.

While many existing studies focus primarily on house price response, this paper goes further by quantifying the distributional consequences that arise through feedback loops between household demand and macroeconomic variables. Among the closest studies in the literature, Hilber and Turner ([2014](https://arxiv.org/html/2511.01133v1#bib.bib17)) show that mortgage interest deductions (MID) disproportionately benefit higher-income households and, in supply-constrained markets, are fully capitalized into house prices, reducing accessibility for lower-income groups. Similarly, Sommer and Sullivan ([2018](https://arxiv.org/html/2511.01133v1#bib.bib24)), which is closest to the present paper in their methodology, demonstrate that removing the MID leads to lower prices and higher homeownership rates, particularly for lower-income households.

The present paper extends Hilber and Turner ([2014](https://arxiv.org/html/2511.01133v1#bib.bib17)) and Sommer and Sullivan ([2018](https://arxiv.org/html/2511.01133v1#bib.bib24)) in several respects. First, it studies policies that differ meaningfully from the MID by operating before purchase and relaxing upfront liquidity constraints, and it examines cases where access is restricted by income. The results show that RD’s distributional effects resemble those of the MID (i.e. reinforcing inequality under supply constraints), whereas EW can be beneficial. This distinction refines the understanding of how price-inflating housing policies affect welfare, by showing that rising prices are not uniformly harmful. Specifically, although both RD and EW raise prices in the short run, RD delays or prevents access for lower-income households, and EW advances purchase timing across groups with limited downside for inequality. More importantly, the findings show that market structure is in large part responsible for the incidence on inequality, not the price surge itself. Equal-affordability versus supply-constrained environments produce different shifts, indicating that pre-existing market disparities drive unequal outcomes. This conclusion is reinforced by robustness to doubling or halving the demand parameter in the price equation.

The remainder of the paper is structured as follows. Section [2](https://arxiv.org/html/2511.01133v1#S2 "2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") presents the general life-cycle model. Without relying on country-specific details, it focuses on the general mechanics linking household decisions to economic inputs and outcomes. Section [3](https://arxiv.org/html/2511.01133v1#S3 "3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") introduces the assumptions applied to input variables, covering taxes, the pension system, and macroeconomic dynamics, as well as the policy scenarios. These assumptions are grounded in the Australian institutional context, and the housing policies reflect the Liberal-Nationals Coalition’s proposal for early superannuation withdrawal, and the Labor Party’s proposal for a reduced deposit. Section [4](https://arxiv.org/html/2511.01133v1#S4 "4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") presents the results under the baseline modeling assumptions, as well as robustness tests under different assumptions on the effect of demand and pension returns. Section [5](https://arxiv.org/html/2511.01133v1#S5 "5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") explores the case where the policies’ access is restricted by income, as well as boundary cases for EW where households can withdraw all the pension balance, or where no savings contribution is required from the household. Section [6](https://arxiv.org/html/2511.01133v1#S6 "6 Conclusion ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") concludes.

## 2 General life-cycle model

This section presents a life-cycle model designed to be general and applicable across different countries. Country-specific assumptions are introduced in Section [3](https://arxiv.org/html/2511.01133v1#S3 "3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit"), where the model is calibrated to the Australian case.

The structure of this section is as follows. Section [2.1](https://arxiv.org/html/2511.01133v1#S2.SS1 "2.1 Preliminaries ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") defines preliminary time and population variables. Section [2.2](https://arxiv.org/html/2511.01133v1#S2.SS2 "2.2 Model dynamics ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") introduces the core equations governing the evolution of savings and pension account balances, along with other related variables. Section [2.3](https://arxiv.org/html/2511.01133v1#S2.SS3 "2.3 Model output ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") defines the purchase time and provides the corresponding withdrawal rules for the savings and pension accounts.

### 2.1 Preliminaries

Time is modeled as discrete and denoted by tt, where period tt represents the interval [t,t+1)[t,t+1). Without loss of generality, all variables are assumed to remain constant within each period. Transactions occur at the beginning of each period. Households exit the population either due to death or default, both of which are assumed to occur at the end of the period.

Retirement time is denoted by TrT\_{r}, and property purchases are funded through loans with a fixed term TlT\_{l}. Time of death is denoted by TσT\_{\sigma}. Default time is denoted by TdT\_{d}, and is formally introduced in Section [2.2](https://arxiv.org/html/2511.01133v1#S2.SS2 "2.2 Model dynamics ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit"). Purchase time, denoted by TpT\_{p}, is an outcome of the model defined in Subsection [2.3](https://arxiv.org/html/2511.01133v1#S2.SS3 "2.3 Model output ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit").

The population consists of N​(0)N(0) households at the start of the analysis. The survival status of household i=1,…,N​(0)i=1,...,N(0) at time tt is denoted by σ(i)​(t)\sigma^{(i)}(t), and is equal to 1 if at least one member is still alive, and to 0 otherwise. The default status of household ii at time tt is denoted by d(i)​(t)d^{(i)}(t), and is equal to 1 if the household has defaulted before time tt, and to 0 otherwise. Default is assumed to occur when household’s savings reach zero, where savings include equity (the paid proportion of the home loan), but exclude pension fund balance. The number of households in the population at time tt is denoted by N​(t)N(t):

|  |  |  |
| --- | --- | --- |
|  | N​(t)=∑i=1N​(0)σ(i)​(t)×(1−d(i)​(t)).N(t)=\sum\_{i=1}^{N(0)}\sigma^{(i)}(t)\times(1-d^{(i)}(t)). |  |

Households are planning for homeownership by accumulating a minimum deposit required for a home loan. The population operates under one of three policy environments, a baseline scenario, a reduced deposit scenario (RD) and an early withdrawal scenario (EW). The only difference between the baseline and the RD scenarios is the minimum deposit required. Hence both these scenarios are characterized under Option 1. The EW scenario allows for early pension withdrawal for homeownership, that is, households are permitted to combine savings with part of their pension account. This leads to changes in the dynamics, and hence is characterized as Option 2.
The analysis compares how the population fares under each policy framework, as well as under a reduction in the required minimum deposit.

Model variables depend on several household-specific characteristics, including survival status, household structure (single vs. couple), income percentile (e.g. affecting pension contributions), and target property price (e.g. determining the required deposit threshold). Additionally, the policy governing pension withdrawals for housing impacts broader economic variables such as house price and rent inflation, as well as pension account balance. For brevity, these dependencies are not explicitly reflected in the notation within this section, except in the definition of the number of homeowners.

### 2.2 Model dynamics

At time t=0t=0, all households plan for a specific target property characterized by certain attributes (e.g. size, location) and an initial price P​(0)P(0). The price of this target property evolves over time, with value at time tt denoted by P​(t)P(t). Households maintain a fixed preference for properties with these characteristics.

The balance at time tt on the savings and pension accounts are denoted by A​(t)A(t) and F​(t)F(t), respectively. The savings account balance earns a return at rate rA​(t−1)r\_{A}(t-1) over [t−1,t)[t-1,t) and is affected by disposable income I​(t)I(t) (net of pension contributions and income taxes), non-housing consumption C​(t)C(t), and housing consumption H​(t)H(t), all associated with period [t,t+1)[t,t+1). The pension account balance earns a return at rate rF​(t−1)r\_{F}(t-1) over [t−1,t)[t-1,t), and increases through pension contributions M​(t)M(t) over [t,t+1)[t,t+1) before retirement, or decreases by the pension benefit withdrawal B​(t)B(t) over [t,t+1)[t,t+1) after retirement. Taxes on returns over [t−1,t)[t-1,t) on the savings and pension account are denoted by τA​(t)\tau\_{A}(t) and τF​(t)\tau\_{F}(t), and are assumed to be paid at time tt.

The savings and pension account balances are also reduced by withdrawal amounts DA​(t)≥0D\_{A}(t)\geq 0 and DF​(t)≥0D\_{F}(t)\geq 0, respectively. These amounts are used to finance the home purchase and are equal to zero for all tt except at the purchase time TpT\_{p}. At t=Tpt=T\_{p}, the combined withdrawal must be sufficient to cover the required home loan deposit, property transfer tax, and an additional buffer for other purchase-related expenses. Specifically, for t≠Tpt\neq T\_{p}, DA​(t)=DF​(t)=0D\_{A}(t)=D\_{F}(t)=0, while at t=Tpt=T\_{p}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DA​(Tp)+DF​(Tp)=(δ+ϵ)​P​(Tp)+τP​(Tp),D\_{A}(T\_{p})+D\_{F}(T\_{p})=\left(\delta+\epsilon\right)P(T\_{p})+\tau\_{P}(T\_{p}), |  | (2.1) |

where δ\delta and ϵ\epsilon represent the required deposit and buffer as fractions of the property price P​(Tp)P(T\_{p}), and τP​(Tp)\tau\_{P}(T\_{p}) denotes the property transfer tax. Under Option 1, where pension withdrawals are not allowed, DF​(Tp)=0D\_{F}(T\_{p})=0, meaning that the entire amount must be withdrawn from savings. Under Option 2, which allows early pension withdrawal for homeownership, DA​(Tp)D\_{A}(T\_{p}) and DF​(Tp)D\_{F}(T\_{p}) must satisfy specific policy constraints. The exact expressions for these withdrawals under Option 2 are provided in Section [2.3](https://arxiv.org/html/2511.01133v1#S2.SS3 "2.3 Model output ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit"), as they are closely tied to the definition of the purchase time.

The savings and pension account balances at time tt are given by:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | A​(t)\displaystyle A(t) | =\displaystyle= | Aa​c​c​(t)+I​(t)−C​(t)−H​(t)−DA​(t),\displaystyle A\_{acc}(t)+I(t)-C(t)-H(t)-D\_{A}(t), |  | (2.2) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | F​(t)\displaystyle F(t) | =\displaystyle= | Fa​c​c​(t)+M​(t)−B​(t)−DF​(t),\displaystyle F\_{acc}(t)+M(t)-B(t)-D\_{F}(t), |  | (2.3) |

where Aa​c​c​(t)A\_{acc}(t) and Fa​c​c​(t)F\_{acc}(t) represent the accumulated savings and pension accounts net of previous period’s taxes:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Aa​c​c​(t)\displaystyle A\_{acc}(t) | =\displaystyle= | A​(t−1)​(1+rA​(t−1))−τA​(t),\displaystyle A(t-1)(1+r\_{A}(t-1))-\tau\_{A}(t), |  | (2.4) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Fa​c​c​(t)\displaystyle F\_{acc}(t) | =\displaystyle= | F​(t−1)​(1+rF​(t−1))−τF​(t),\displaystyle F(t-1)(1+r\_{F}(t-1))-\tau\_{F}(t), |  | (2.5) |

with initial values Aa​c​c​(0)A\_{acc}(0) and Fa​c​c​(0)F\_{acc}(0).

The disposable income I​(t)I(t) is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(t)={S​(t)−τS​(t),for ​t<Tr,B​(t)+G​(t),for ​t≥Tr,I(t)=\left\{\begin{array}[]{ll}S(t)-\tau\_{S}(t),&\text{for }t<T\_{r},\\ B(t)+G(t),&\text{for }t\geq T\_{r},\end{array}\right. |  | (2.6) |

where S​(t)S(t) is the gross income earned over [t,t+1)[t,t+1) after pension contributions, τS​(t)\tau\_{S}(t) is the income tax assumed to be deducted directly from salary, and G​(t)G(t) is the guaranteed state pension received after retirement. Thus, pre-retirement income is the net earnings after tax and pension contribution, while post-retirement income consists of pension withdrawals B​(t)B(t) and state benefits G​(t)G(t) (e.g. social security).

Pension contribution M​(t)M(t) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(t)={(1−τγ​(t))​γ​S​(t),for ​t<Tr,0,for ​t≥Tr,M(t)=\left\{\begin{array}[]{ll}(1-\tau\_{\gamma}(t))\gamma S(t),&\text{for }t<T\_{r},\\ 0,&\text{for }t\geq T\_{r},\end{array}\right. |  | (2.7) |

where γ\gamma is the contribution rate to the pension fund and τγ​(t)\tau\_{\gamma}(t) is the tax rate on contributions.

The housing consumption H​(t)H(t) evolves as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(t)={R​(t), for ​t<Tp,μ​(t)+π​(t), for ​Tp≤t<Tp+Tl,μ​(t), for ​t≥Tl+Tp,H(t)=\left\{\begin{array}[]{ll}R(t),&\text{ for }t<T\_{p},\\ \mu(t)+\pi(t),&\text{ for }T\_{p}\leq t<T\_{p}+T\_{l},\\ \mu(t),&\text{ for }t\geq T\_{l}+T\_{p},\end{array}\right. |  | (2.8) |

where R​(t)R(t) is the rent paid before property purchase, μ​(t)\mu(t) captures ongoing property-related costs (e.g. maintenance, local property tax) after purchase, and π​(t)\pi(t) are the mortgage repayments made at the beginning of each period until the loan is repaid by term TlT\_{l}.

The mortgage repayments follow standard actuarial formulas for loans payable in advance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(t)=L​(t)​rB​(t)1−(1+rB​(t))−(Tl+Tp−t), for ​t=Tp,…,Tp+Tl−1,\pi(t)=\frac{L(t)r\_{B}(t)}{1-\left(1+r\_{B}(t)\right)^{-(T\_{l}+T\_{p}-t)}},\quad\text{ for }t=T\_{p},...,T\_{p}+T\_{l}-1, |  | (2.9) |

where rB​(t)r\_{B}(t) is the time-varying borrowing rate, and L​(t)L(t) is the outstanding loan balance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(t)={0, for ​t<Tp,(1−δ)​P​(Tp), for ​t=Tp,(L​(t−1)−π​(t−1))​(1+rB​(t−1)), for ​Tp+1≤t≤Tp+Tl−1.0, for ​t≥Tp+Tl.L(t)=\left\{\begin{array}[]{ll}0,&\text{ for }t<T\_{p},\\ (1-\delta)P(T\_{p}),&\text{ for }t=T\_{p},\\ \left(L(t-1)-\pi(t-1)\right)(1+r\_{B}(t-1)),&\text{ for }T\_{p}+1\leq t\leq T\_{p}+T\_{l}-1.\\ 0,&\text{ for }t\geq T\_{p}+T\_{l}.\end{array}\right. |  | (2.10) |

Specifically, the household has no mortgage debt before property purchase. At the purchase time TpT\_{p}, the outstanding loan equals the property price minus the deposit. During the loan term, the balance decreases with repayments and increases with interest. After Tp+TlT\_{p}+T\_{l}, the loan is fully repaid.

For homeowners, it is assumed that at the first time t⋆t^{\star} such that Aa​c​c​(t⋆)≤0A\_{acc}(t^{\star})\leq 0 and t⋆≥Tpt^{\star}\geq T\_{p}, the household’s property is liquidated, meaning that accumulated savings are increased by P​(t⋆)−L​(t⋆)P(t^{\star})-L(t^{\star}), where the property is sold at the prevailing market price and net of the outstanding loan balance. In this case, the property purchase status and time are reset, and the household starts paying rent again, and may re-purchase a property later on.

The default time TdT\_{d} is defined as the first time tt such that A​(t)≤0A(t)\leq 0 and the household does not own property. Upon default, the household exits the model, and its default status is set to d​(t)=1d(t)=1 for t≥Tdt\geq T\_{d}.

Before defining the model’s output, it is relevant to note that temporary income loss due to unemployment or disability is not explicitly modeled. However, many pension funds offer income protection and total permanent disability insurance, which offset this omission. Additionally, for simplicity, the analysis excludes death benefits that can be provided by pension funds.

### 2.3 Model output

The primary output of the life-cycle model is the purchase time, which is the time (or period [Tp,Tp+1)[T\_{p},T\_{p}+1)) when the household acquires a property. Under Option 1, households rely solely on accumulated savings, and the purchase occurs at the first time tt when the accumulated savings balance Aa​c​c​(t)A\_{acc}(t) meets or exceeds the required amount (δ+ϵ)​P​(t)+τP​(t)(\delta+\epsilon)P(t)+\tau\_{P}(t). Under Option 2, households can supplement their savings with withdrawals from their pension account, and the purchase occurs at the first time tt when an admissible combination of accumulated savings Aa​c​c​(t)A\_{acc}(t) and accumulated pension account Fa​c​c​(t)F\_{acc}(t) meets or exceeds the required amount. Under either option, the household’s income net of taxes and consumption must exceed the repayment at the time of purchase.

In Option 2 considered in this paper, the policy parameters are defined as follows: a minimum proportion α\alpha of the property price must be covered by savings; a maximum allowable withdrawal proportion β\beta from the pension account; and an absolute cap FmaxF^{\max} on pension withdrawals. Additionally, pension withdrawals can only be used toward the home loan deposit, meaning that savings must still meet the remaining deposit requirement. These policy parameters align with the regulatory framework proposed by the Australian Coalition, but they can be tuned to match other more general policies. To simplify the decision-making process, the model assumes that households withdraw the full permissible amount from their pension accounts and use savings to cover any remaining shortfall.

Therefore, the purchase time is the first time when two conditions are met. First, the household’s accumulated savings must meet the deposit affordability threshold, that is, Aa​c​c​(t)≥(δ+ϵ)​P​(t)+τP​(t)−DF​(t)A\_{acc}(t)\geq(\delta+\epsilon)P(t)+\tau\_{P}(t)-D\_{F}(t)). Second, the household’s disposable income must meet the repayment affordability threshold, that is, I​(t)≥πr​e​f​(t)I(t)\geq\pi^{ref}(t) where πr​e​f​(t)=(1−δ)​P​(t)​rB​(t)1−(1+rB​(t))−Tl\pi^{ref}(t)=\frac{(1-\delta)P(t)r\_{B}(t)}{1-\left(1+r\_{B}(t)\right)^{-T\_{l}}} is the first repayment that would apply in case of purchase at time tt. Thus, TpT\_{p} under either policy scenario satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Tp=inf{t≤min⁡{Tσ,Td}​ ∣ ​I​(t)≥πr​e​f​(t)​ and ​Aa​c​c​(t)≥(δ+ϵ)​P​(t)+τP​(t)−DF​(t)}.T\_{p}=\inf\left\{t\leq\min\{T\_{\sigma},T\_{d}\}\text{ }\mid\text{ }I(t)\geq\pi^{ref}(t)\text{ and }A\_{acc}(t)\geq(\delta+\epsilon)P(t)+\tau\_{P}(t)-D\_{F}(t)\right\}. |  | (2.11) |

The withdrawals from savings and pension accounts at time TpT\_{p} are given by:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | DF​(Tp)\displaystyle D\_{F}(T\_{p}) | =\displaystyle= | min⁡{β​Fa​c​c​(Tp),Fmax,(δ−α)​P​(Tp)},\displaystyle\min\left\{\beta F\_{acc}(T\_{p}),F^{\max},(\delta-\alpha)P(T\_{p})\right\}, |  | (2.12) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | DA​(Tp)\displaystyle D\_{A}(T\_{p}) | =\displaystyle= | (δ+ϵ)​P​(Tp)+τP​(Tp)−DF​(Tp).\displaystyle(\delta+\epsilon)P(T\_{p})+\tau\_{P}(T\_{p})-D\_{F}(T\_{p}). |  | (2.13) |

Under Option 2, the accumulated savings must exceed a reduced required amount, with a reduction of DF​(Tp)D\_{F}(T\_{p}) used from the pension account. The reduction is equal to the proportion β​Fa​c​c​(t)\beta F\_{acc}(t), but cannot exceed the maximum withdrawable amount FmaxF^{\max}. Furthermore, the reduction can only be used towards the deposit while allowing for a minimum α​P​(t)\alpha P(t) from the savings, meaning that the reduction cannot exceed (δ−α)​P​(t)(\delta-\alpha)P(t). Notice that in all cases, DF​(Tp),DA​(Tp)≥0D\_{F}(T\_{p}),D\_{A}(T\_{p})\geq 0 and DA​(Tp)+DF​(Tp)=(δ+ϵ)​P​(Tp)+τP​(Tp)D\_{A}(T\_{p})+D\_{F}(T\_{p})=(\delta+\epsilon)P(T\_{p})+\tau\_{P}(T\_{p}). Additionally, under Option 1 where α=β=Fmax=0\alpha=\beta=F^{\max}=0, it follows that DF​(Tp)=0D\_{F}(T\_{p})=0 and DA​(Tp)=(δ+ϵ)​P​(Tp)+τP​(Tp)D\_{A}(T\_{p})=(\delta+\epsilon)P(T\_{p})+\tau\_{P}(T\_{p}).

A second key output of the model is the number of homeowners at time tt, and is denoted by NH​(t)N\_{H}(t). Introducing household superscripts, the purchase time of household i∈𝒦i\in\mathcal{K} is Tp(i)T\_{p}^{(i)}, where 𝒦\mathcal{K} may refer to the entire population or to a specific income percentile, and NH​(t)N\_{H}(t) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NH​(t)=∑i∈𝒦​σ(i)​(t)​(1−d(i)​(t))​𝕀​(Tp(i)≤t),N\_{H}(t)=\underset{i\in\mathcal{K}}{\sum}\sigma^{(i)}(t)(1-d^{(i)}(t))\mathbb{I}\left(T\_{p}^{(i)}\leq t\right), |  | (2.14) |

where 𝕀​(Tp(i)≥t)\mathbb{I}\left(T\_{p}^{(i)}\geq t\right) equals 1 if household ii has purchased by time tt.

Table [1](https://arxiv.org/html/2511.01133v1#S2.T1 "Table 1 ‣ 2.3 Model output ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") classifies all variables in the model into input or output variables. Input variables (e.g. tax rules, macroeconomic variables, financial market parameters) are exogenous determinants that may be fixed or modeled as stochastic processes estimated from historical data. These variables are specified in Section [3](https://arxiv.org/html/2511.01133v1#S3 "3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") for the Australian case. Output variables are determined endogenously based on the input variables (e.g. savings and pension account balances, disposable income, time of purchase).

|  |  |  |
| --- | --- | --- |
| Input variables | | |
| Population variables | | |
|  | TσT\_{\sigma} | Time of exit due to death |
|  | TdT\_{d} | Time of exit due to default |
| Tax variables | | |
|  | τP​(t)\tau\_{P}(t) | Property transfer tax upon purchase |
|  | τI​(t)\tau\_{I}(t) | Income tax |
|  | τγ\tau\_{\gamma} | Tax rate on employer’s pension contributions |
|  | τA​(t)\tau\_{A}(t), τF​(t)\tau\_{F}(t) | Taxes on savings and pension investment returns |
| Pension variables | | |
|  | TrT\_{r} | Time of retirement |
|  | γ\gamma | Employer’s mandatory pension contribution rate (proportion of gross salary) |
|  | B​(t)B(t) | Pension withdrawal benefit |
|  | G​(t)G(t) | Social Security benefit |
| Households variables | | |
|  | δ\delta | Home loan deposit rate |
|  | ϵ\epsilon | Buffer rate for additional costs |
|  | TlT\_{l} | Loan term |
|  | μ​(t)\mu(t) | Property maintenance costs |
|  | C​(t)C(t) | Non-housing consumption |
| Stochastic input variables | | |
|  | N​(t)N(t) | Number of surviving households |
|  | σ​(t)\sigma(t) | Survival status |
|  | P​(t)P(t) | Target property price |
|  | R​(t)R(t) | Rent |
|  | S​(t)S(t) | Gross salary |
|  | rB​(t)r\_{B}(t) | Borrowing rate |
|  | rA​(t)r\_{A}(t) | Savings account return |
|  | rF​(t)r\_{F}(t) | Pension account return |
| Pension withdrawal policy rules | | |
|  | α\alpha | Minimum proportion of the property price financed using savings account |
|  | β\beta | Maximum proportion withdrawn from the pension account |
|  | FmaxF^{\max} | Maximum amount withdrawn from the pension account |
| Output variables | | |
|  | TpT\_{p} | Time of property purchase |
|  | NH​(t)N\_{H}(t) | Number of homeowners in the population |
|  | d(i)​(t)d^{(i)}(t) | Default status |
|  | A​(t)A(t), F​(t)F(t) | Savings and pension account balance |
|  | DA​(t)D\_{A}(t), DF​(t)D\_{F}(t) | Amounts withdrawn from savings and pension account at the purchase time |
|  | H​(t)H(t) | Housing consumption |
|  | I​(t)I(t) | Disposable income |
|  | M​(t)M(t) | Mandatory employers pension contribution |
|  | π​(t)\pi(t) | Loan repayment |
|  | L​(t)L(t) | Outstanding loan debt |

Table 1: Summary of notations of the general life-cycle model.  The top panel lists the input variables which may be fixed by law, or modeled as stochastic processes estimated from historical data. The bottom panel lists the model output variables, which are determined endogenously based on the input variables.

## 3 Input variables for Australia and simulation design

Australia was one of the first countries to introduce a mandatory DC system, the Superannuation Guarantee (SG), which requires employer contributions into privately managed accounts. These accounts supplement a means-tested public Age Pension (Commonwealth Treasury of Australia, [2001](https://arxiv.org/html/2511.01133v1#bib.bib12), Mercer CFA Institute, [2025](https://arxiv.org/html/2511.01133v1#bib.bib22)). Superannuation assets now exceed AUD 3.5 trillion, making super the second-largest source of household wealth after owner-occupied housing (Eslake, [2024](https://arxiv.org/html/2511.01133v1#bib.bib13)). Australia’s SG is most similar to Switzerland’s Occupational Pension scheme, Kazakhstan’s Unified Accumulative Pension Fund, and Singapore’s Central Provident Fund (McCarthy et al., [2002](https://arxiv.org/html/2511.01133v1#bib.bib21), Akhmedyarova, [2023](https://arxiv.org/html/2511.01133v1#bib.bib3), Mercer CFA Institute, [2025](https://arxiv.org/html/2511.01133v1#bib.bib22)). Other countries, such as New Zealand and the UK, have introduced opt-out systems with lower contribution rates, while Canada and the US have increasingly shifted toward voluntary DC schemes without making them fully mandatory.

The SG was designed with the assumption that most retirees would be homeowners. However, as in most countries, homeownership rates have declined, particularly among younger and lower-income households (Yates and Bradbury, [2010](https://arxiv.org/html/2511.01133v1#bib.bib28), The Mckell Institute, [2021](https://arxiv.org/html/2511.01133v1#bib.bib26), Eslake, [2024](https://arxiv.org/html/2511.01133v1#bib.bib13)). In response, Australian governments have introduced demand-side housing policies, such as stamp duty exemptions and first-home buyer incentives, which have drawn criticism for inflating prices rather than improving accessibility (The Mckell Institute, [2021](https://arxiv.org/html/2511.01133v1#bib.bib26), Agarwal et al., [2023](https://arxiv.org/html/2511.01133v1#bib.bib2)). Similar issues have been observed internationally in the context of Mortgage Interest Deductions (MID) and housing subsidies across Germany, the UK, and the US (Vigdor, [2006](https://arxiv.org/html/2511.01133v1#bib.bib27), Bourassa et al., [2013](https://arxiv.org/html/2511.01133v1#bib.bib9), Berger et al., [2020](https://arxiv.org/html/2511.01133v1#bib.bib7), Krolage, [2023](https://arxiv.org/html/2511.01133v1#bib.bib20), Carozzi et al., [2024](https://arxiv.org/html/2511.01133v1#bib.bib10)).

Two recent housing policy proposals in Australia are of interest: the Reduced Deposit (RD) policy and Early Withdrawal (EW) from superannuation accounts. The Labor Party, which won the election, proposed a RD policy that lowers the required deposit from the typical 20% to 5%, backed by a government guarantee. This guarantee removes the need for Lenders Mortgage Insurance, which is often required for loans with deposits under 20%. EW, originally proposed by the Liberal-National Coalition in 2022 and reiterated during the 2025 campaign, allows eligible first-home buyers to withdraw 40% of the superannuation balance to help cover their deposit. Households cannot withdraw more than AUD 50,000, and must contribute 5% of the property price from their savings account.

These proposals are evaluated relative to a benchmark with a standard deposit requirement. In the notations of Section [2](https://arxiv.org/html/2511.01133v1#S2 "2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit"), the benchmark corresponds to Option 1 with δ=20%\delta=20\%, and α=β=Fmax=0\alpha=\beta=F^{\max}=0. The RD policy corresponds to Option 1 but with a reduced deposit δ=5%\delta=5\%. The EW policy corresponds to Option 2, with δ=20%\delta=20\%, a minimum savings contribution of α=5%\alpha=5\% of the property price, a maximum withdrawal of β=40%\beta=40\%, and an absolute withdrawal cap of Fmax=50,000F^{\max}=50{,}000.

The rest of this section is structured as follows. Section [3.1](https://arxiv.org/html/2511.01133v1#S3.SS1 "3.1 Policy context ‣ 3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") provides additional background on these housing policy proposals and similar schemes in other countries. Section [3.2](https://arxiv.org/html/2511.01133v1#S3.SS2 "3.2 Input variables ‣ 3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") outlines the fixed input parameters at t=0t=0, including tax, pension, and household assumptions based on the Australian context. It also presents the econometric framework for simulating stochastic variables. Section [3.3](https://arxiv.org/html/2511.01133v1#S3.SS3 "3.3 Simulation design ‣ 3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") details the simulation procedure. Section [3.4](https://arxiv.org/html/2511.01133v1#S3.SS4 "3.4 Evaluation metrics ‣ 3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") introduces the outcome metrics used to assess the policy effects.

### 3.1 Policy context

Both EW and RD policies aim to improve homeownership accessibility by lowering the upfront savings threshold to 5% of the property price. However, they differ in their mechanics and distributional implications. EW allows individuals to draw on their own retirement savings, raising concerns about reduced pension balances. Yet its effect on retirement security is ambiguous, as converting super into housing may reduce post-retirement housing expenses (Hand, [2023](https://arxiv.org/html/2511.01133v1#bib.bib16)). RD, by contrast, avoids pension withdrawals but increases loan sizes, shifting the constraint from savings to income.

Both policies can reinforce inequality by benefiting those already better positioned to buy. Under EW, high-income earners accumulate pension faster and can meet the 5% cash requirement sooner. Low-income earners may lack sufficient balances and be priced out. Under RD, high-income households are less likely to be bound by income-based lending constraints. Lower-income earners remain constrained by repayment limits and must accumulate more than 5% to meet income affordability thresholds, which becomes increasingly difficult as prices rise.

EW has faced strong criticism from economists and policy commentators, who argue that it inflates prices and undermines retirement adequacy (Super Members Council, [2025](https://arxiv.org/html/2511.01133v1#bib.bib25)). RD has attracted less scrutiny, possibly due to its framing as a cost-reducing measure. Internationally, similar policies exist. Countries like Singapore, Switzerland, and Kazakhstan allow EW for housing under mandatory DC schemes, while Canada, the US, and New Zealand permit restricted access. Yet few studies quantify their welfare impacts. Notably, under EW, The Mckell Institute ([2021](https://arxiv.org/html/2511.01133v1#bib.bib26)) project minimal homeownership gains and rising prices in Australia, while Akhmedyarova ([2023](https://arxiv.org/html/2511.01133v1#bib.bib3)) find negligible price effects in Kazakhstan.

### 3.2 Input variables

All monetary figures are in Australian dollars (AUD), with AUD 1 ≈\approx USD 0.60 at the time of writing. Time tt is measured in quarters to match the data frequency. Each household enters the model at age 25 (t=0t=0). Households start with no initial assets (Aa​c​c​(0)=Fa​c​c​(0)=0A\_{acc}(0)=F\_{acc}(0)=0) and no inheritance or external financial support. The model tracks their wealth accumulation and housing decisions over time. While household composition (e.g. singles vs. couples) affects the level of income and consumption, what substantially matters for affordability when Aa​c​c​(0)=Fa​c​c​(0)=0A\_{acc}(0)=F\_{acc}(0)=0 is the ratio of house prices to disposable income. To simplify the analysis, all households are modelled as singles, while differences in affordability are captured by varying the house-price-to-income ratio through two market settings: an equal-affordability market and a supply-constrained market, as detailed later in this section.

#### 3.2.1 Constant input variables: tax rules, pension rules, and household variables

The five tax functions τP​(t)\tau\_{P}(t), τI​(t)\tau\_{I}(t), τA​(t)\tau\_{A}(t), τF​(t)\tau\_{F}(t) and τγ​(t)\tau\_{\gamma}(t) are based on rates and thresholds from the Victoria’s State Revenue Office ([link](https://www.sro.vic.gov.au/rates-taxes-duties-and-levies/general-land-transfer-duty-property-current-rates)) and the Australian Taxation Office (ATO) ([link](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents#ato-Australianresidenttaxrates2020to2025)). First-home buyer concessions and exemptions are excluded from τP​(t)\tau\_{P}(t) as they are temporary and subject to policy changes. Australian income tax applies to both salary and investment returns and operates on an annual basis while the analysis is conducted quarterly. Two simplifications are made to avoid unnecessary end-of-year adjustments. First, τI​(t)\tau\_{I}(t) is applied only to salary with official tax thresholds divided by four to approximate quarterly taxation. Second, τA​(t)\tau\_{A}(t) is adjusted separately to account for savings returns. Appendix [A.1](https://arxiv.org/html/2511.01133v1#A1.SS1 "A.1 More details on tax rules ‣ Appendix A Appendix ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") provides details on the tax functions and their numerical values.

The pension-related variables TrT\_{r}, γ\gamma, B​(t)B(t), and G​(t)G(t) are sourced from the Australian Taxation Office (ATO) ([link](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds)) and Services Australia ([link](https://www.servicesaustralia.gov.au/age-pension)). Retirement age is set at 67 (Tr=168T\_{r}=168 quarters), which is the official retirement age in Australia. The superannuation contribution rate is fixed at γ=12%\gamma=12\%, in line with the rate in force since July 2025. While pension withdrawals B​(t)B(t) are discretionary, they are assumed to follow the ATO’s minimum required withdrawal rates for simplicity. These rates are adjusted to a quarterly basis by dividing the annual values by four. The state-guaranteed pension G​(t)G(t) comprises a base amount, supplements, and rental assistance. Eligibility and benefit levels depend on income and asset tests, with different thresholds for homeowners and non-homeowners. Detailed formulas and parameter values for the pension-related variables are provided in Appendix [A.2](https://arxiv.org/html/2511.01133v1#A1.SS2 "A.2 More details on pension rules ‣ Appendix A Appendix ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit").

The loan term is fixed at 30 years (Tl=120T\_{l}=120 quarters). The buffer ϵ\epsilon is fixed at 1%1\% of the property purchase price, and is assumed to cover costs such as legal fees, mortgage fees and furniture purchase. Government support schemes, such as the First Home Guarantee and First Home Owner Grant, are temporary measures and are not incorporated into the analysis.

The quarterly property maintenance cost μp​(t)\mu\_{p}(t) depends on factors such as location, type, age, and size of the property, as well as household behavior. For simplicity, it is assumed to be 0.25% of the property price P​(t)P(t), following guidelines from the Home Owners Association ([link](https://www.homeownersassociation.com.au/how-to-estimate-your-annual-home-maintenance-costs/#:~:text=The%201%25%20rule%20serves%20as,and%20%2420%2C000%20annually%20for%20upkeep.)).

Households allocate a proportion ν​(t)\nu(t) of their disposable income net of housing to non-housing consumption, such that C​(t)=ν​(t)​I​(t)C(t)=\nu(t)I(t). The values of ν​(t)\nu(t) are informed by estimates from an RBA study (Beech et al., [2014](https://arxiv.org/html/2511.01133v1#bib.bib6)), which reports the share of disposable income allocated to total consumption for each age group, as well as the share of consumption devoted to non-housing items. Combining these figures yields an estimate of non-housing consumption as a proportion of income net of taxes and housing costs. Due to data limitations, ν​(t)\nu(t) is assumed to be constant across income percentiles. The proportion ν​(t)\nu(t) is set to 61.1% for t∈[0,39]t\in[0,39] (ages 25-34), 59.3% for t∈[40,79]t\in[40,79] (ages 35-44), 58.2% for t∈[80,119]t\in[80,119] (ages 45-54), 60.5% for t∈[120,159]t\in[120,159] (ages 55-64), 84.4% for t≥160t\geq 160 (ages 65 and above). A minimum quarterly consumption level of $1,200 (2025 dollars) is imposed and indexed to inflation, ensuring that basic consumption needs are met regardless of income.

#### 3.2.2 Stochastic variables

The study models a population of N​(0)=10,000N(0)=10,000 individuals. At time 0, all households are initially alive and aged 25, i.e. σ(i)​(0)=1\sigma^{(i)}(0)=1 for i=1,…,N​(0)i=1,...,N(0). The survival paths σ(i)​(t)\sigma^{(i)}(t) are simulated from Bernouilli distributions based on the latest 2020-24 male and female survival probabilities published by the Australian Government Actuary ([link](https://aga.gov.au/publications/life-tables/australian-life-tables-2020-22)). The maximum age is 100.

The initial values of all macroeconomic and financial variables are fixed across households, except for initial income S​(0)S(0) and rent R​(0)R(0), which vary by income group. Income determines household percentile. Initial rent is different for each income group, and is set at 30% of S​(0)S(0).

The evolution of economic variables is modelled using quarterly data from Q4 2002 to Q4 2022, chosen to align with the available property price series. The modelling approach broadly follows the cascade structure developed by Khemka et al. ([2024](https://arxiv.org/html/2511.01133v1#bib.bib19)), with some important modifications.

First, this study uses more recent data and re-estimates the coefficients for key economic series, including the Consumer Price Index (CPI), real cash rate, borrowing spread, rent, and superannuation returns. Consistent with Khemka et al. ([2024](https://arxiv.org/html/2511.01133v1#bib.bib19)), CPI growth and the cash rate (assumed to equal the savings rate rA​(t)r\_{A}(t)) are modelled as AR(1) processes, while the spread between borrowing and savings rates (i.e. rB​(t)−rA​(t)r\_{B}(t)-r\_{A}(t)) follows a random walk. Superannuation returns are modelled as the savings rate plus a 1% constant equity risk premium, with random variation. The CPI index is normalised at 1 at time 0. Initial values are set to rA​(0)=(1.0435)1/4−1r\_{A}(0)=(1.0435)^{1/4}-1 (RBA cash rate, Dec 2024), rB​(0)=(1.0599)1/4−1r\_{B}(0)=(1.0599)^{1/4}-1 (lowest available borrowing rate, Dec 2024; [link](https://www.comparethemarket.com.au/)), and rF​(0)=rA​(0)+0.01r\_{F}(0)=r\_{A}(0)+0.01. Rent growth is estimated via an AR(2) model with an error correction component applied to the first difference of the rental price index. Model coefficients are provided in Table [2](https://arxiv.org/html/2511.01133v1#S3.T2 "Table 2 ‣ 3.2.2 Stochastic variables ‣ 3.2 Input variables ‣ 3 Input variables for Australia and simulation design ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit").

Second, residual treatment deviates from Khemka et al. ([2024](https://arxiv.org/html/2511.01133v1#bib.bib19)), who used parametric and independent residuals. Here, residuals for each variable are modelled empirically, transformed into pseudo-observations, and jointly modelled using a vine copula. This allows for contemporaneous dependence between shocks in macro-financial variables, and captures co-movement not explained by covariates.

The salary process also differs. Salaries evolve according to S​(t)=S​(t−1)​(1+xs​(t))​(1+a​w​e​(t))S(t)=S(t-1)(1+x\_{s}(t))(1+awe(t)), where a​w​e​(t)awe(t) is wage growth, modelled as AR(1), and xs​(t)x\_{s}(t) captures the deterministic age profile, calibrated as xs​(t)=exp⁡(0.033091−0.001462×t/4)−1x\_{s}(t)=\exp(0.033091-0.001462\times t/4)-1 from HILDA survey data in Khemka et al. ([2021](https://arxiv.org/html/2511.01133v1#bib.bib18)). Initial salaries S​(0)S(0) reflect five interpolated income percentiles from the ABS census data for age 25: $3,250, $7,937.50, $12,625, $17,312.50, and $22,000. For reference, the 2024 ABS quarterly median income across the entire population is $18,148 (i.e. $1,396 per week). At age 25, only the top income group exceeds this median. Ignoring wage inflation a​w​e​(t)awe(t), the second group surpasses the median after 2 quarters, the third after 3 years, the fourth after 6.75 years, and the fifth after 15.75 years.

The most significant modelling difference from Khemka et al. ([2024](https://arxiv.org/html/2511.01133v1#bib.bib19)) lies in the treatment of property prices. In this paper, the property price index explicitly incorporates endogenous demand from the life-cycle model (Section [2](https://arxiv.org/html/2511.01133v1#S2 "2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit")) as a covariate. This interaction is crucial because the housing policies considered in this paper are expected to increase home affordability in the short-run, leading to more purchases, and in turn, higher demand that inflates property prices.

Specifically, at each time tt, for given realizations of all variables, the housing demand growth yd​(t)y\_{d}(t) is determined endogenously as:

|  |  |  |
| --- | --- | --- |
|  | yd​(t)=log⁡(1+η​(t))−log⁡(1+η​(t−1)),y\_{d}(t)=\log(1+\eta(t))-\log(1+\eta(t-1)), |  |

with yd​(0)=0y\_{d}(0)=0, where η​(t)=max⁡(0,NH​(t)−NH​(t−1))\eta(t)=\max(0,N\_{H}(t)-N\_{H}(t-1)) is the number of new homeowners over [t−1,t)[t-1,t), and NH​(t)N\_{H}(t) is defined in ([2.14](https://arxiv.org/html/2511.01133v1#S2.E14 "In 2.3 Model output ‣ 2 General life-cycle model ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit")). The variable η​(t)\eta(t) is restricted to be non-negative to avoid numerical issues arising in case of households’ default.

To ensure empirical validity, the effect of ydy\_{d} on the property price index is estimated using historical data that aligns with model-derived measurements. The time series of homeownership rates η​(t)\eta(t) is constructed using ABS data on the number of new home loans, measured using the sum of Victoria’s quarterly data (June 2002 - September 2024) for owner-occupied construction, newly built purchases, and existing dwelling purchases. Property price growth ypy\_{p}, which is obtained as yp​(t)=log⁡(P​(t))−log⁡(P​(t−1))y\_{p}(t)=\log(P(t))-\log(P(t-1)), is modeled as follows:

|  |  |  |
| --- | --- | --- |
|  | yp​(t)−0.01=0.6988(s.e. ​0.067)⋅(yp​(t−1)−0.01)+0.1293(s.e. ​0.022)⋅yd​(t−1)+ϵt(p),y\_{p}(t)-0.01=\underset{(\text{s.e. }0.067)}{0.6988}\cdot\left(y\_{p}(t-1)-0.01\right)+\underset{(\text{s.e. }0.022)}{0.1293}\cdot y\_{d}(t-1)+\epsilon\_{t}^{(p)}, |  |

where ϵt(p)\epsilon\_{t}^{(p)} is the error term. The equation’s R2 is 0.68.

At time 0, the target property price P​(0)P(0) is fixed, and households are assumed to maintain a consistent preference for the type of property they aim to purchase. The value of P​(0)P(0) is income-dependent, and two housing market structures are considered.

The first is the equal-affordability market, in which the target property price at time 0 is set to approximately 61.5 times the household’s quarterly income at age 25, i.e. 15.25 times the yearly income. This specification assumes that a suitably priced property exists for every income level. As a result, P​(0)P(0) ranges from $200,000 to $1,350,000 across the income distribution. However, this market is idealized and not fully representative of the Australian context, where properties priced around $200,000 are rare, even in rural areas.

The second is the supply-constrained market, where target property prices at time 0 are restricted to a fixed range between $300,000 and $1,000,000. This setup reflects more realistic supply-side constraints in the Australian housing market. Under this scenario, housing affordability varies across income groups: for high-income households, the target property price represents approximately 45.5 times their quarterly income, while for low-income households it is around 92 times. These values reflect the relative scarcity of low-priced housing and the greater feasibility for high-income earners to purchase homes in the upper range. For example, $300,000 properties are generally limited to outer suburban or rural areas, while $1,000,000 properties correspond to typical two- to three-bedroom apartments or townhouses in metropolitan locations.

| Variable | Modelling Equation |
| --- | --- |
| CPI growth | c​p​i​(t)=0.0065+0.2897⋅(c​p​i​(t−1)−0.0065)+εt(c​p​i)cpi(t)=0.0065+0.2897\cdot(cpi(t-1)-0.0065)+\varepsilon^{(cpi)}\_{t} |
| AWE growth | a​w​e​(t)=0.0021+0.5716⋅a​w​e​(t−1)+0.2500⋅c​p​i​(t−1)+εt(a​w​e)awe(t)=0.0021+0.5716\cdot awe(t-1)+0.2500\cdot cpi(t-1)+\varepsilon^{(awe)}\_{t} |
| Real cash rate | r​rA​(t)=0.6080⋅r​rA​(t−1)+εt(r)rr\_{A}(t)=0.6080\cdot rr\_{A}(t-1)+\varepsilon^{(r)}\_{t} |
| Nominal cash rate | rA​(t)=max⁡(0,exp⁡(r​rA​(t)+c​p​i​(t))−1)r\_{A}(t)=\max\left(0,\exp(rr\_{A}(t)+cpi(t))-1\right) |
| Borrowing spread | sB​(t)=max⁡(0.0034,min⁡(0.011,sB​(t−1)+εt(s)))s\_{B}(t)=\max(0.0034,\min(0.011,s\_{B}(t-1)+\varepsilon^{(s)}\_{t})) |
| Borrowing rate | rB​(t)=max⁡(0,exp⁡(sB​(t)+rA​(t))−1)r\_{B}(t)=\max(0,\exp(s\_{B}(t)+r\_{A}(t))-1) |
| Superannuation return | rF​(t)=rA​(t)+0.01+εt(f)r\_{F}(t)=r\_{A}(t)+0.01+\varepsilon^{(f)}\_{t} |
| Error correction term for rent | ECMr​(t−1)=R​(t−1)−0.1386+0.2336⋅P​(t−1)−1.0943⋅a​w​e​(t−1)\text{ECM}\_{r}(t-1)=R(t-1)-0.1386+0.2336\cdot P(t-1)-1.0943\cdot awe(t-1) |
| Rent growth | yR​(t)=0.007+0.6533⋅(yR​(t−1)−0.007)+0.2832⋅(yR​(t−2)−0.007)y\_{R}(t)=0.007+0.6533\cdot(y\_{R}(t-1)-0.007)+0.2832\cdot(y\_{R}(t-2)-0.007) |
|  | −0.0117⋅ECMr​(t−1)+εt(R)-0.0117\cdot\text{ECM}\_{r}(t-1)+\varepsilon^{(R)}\_{t} |
| Property price growth | yP​(t)−0.01=0.6988⋅(yP​(t−1)−0.01)+0.1293⋅yd​(t−1)+εt(P)y\_{P}(t)-0.01=0.6988\cdot(y\_{P}(t-1)-0.01)+0.1293\cdot y\_{d}(t-1)+\varepsilon^{(P)}\_{t} |

Table 2: Macroeconomic and financial variable dynamics used in the simulation model. Equations follow the cascade framework of Khemka et al. ([2024](https://arxiv.org/html/2511.01133v1#bib.bib19)) with updated parameters based on Q4 2002–Q4 2022 Australian data.

### 3.3 Simulation design

The simulation framework consists of me​c​o=1,000m^{eco}=1,000 economic scenarios, indexed by m=1,…,me​c​om=1,...,m^{eco}, where each economic scenario corresponds to a different set of dependent residuals of the macroeconomic and financial variable paths, generated from the estimated econometric model, and applied uniformly across all households. Dependence between the residuals is incorporated using a vine copula.

To maintain heterogeneity across the population, each of the me​c​om^{eco} scenarios also includes a household-specific error term applied to salary growth. The variance of the common salary residual is reduced by half, and the remaining half of the variance is attributed to this household-specific error term, which is sampled from the simulated residuals of the salary growth.

The initial values and simulated residuals plugged into the econometric model lead to the first-period realizations of property prices P​(1)P(1), rent R​(1)R(1), income S​(1)S(1), borrowing rates rB​(1)r\_{B}(1), savings rates rA​(1)r\_{A}(1), and superannuation returns rF​(1)r\_{F}(1). These values, in combination with tax rules and pension regulations, are used within the life-cycle model to determine each household’s financial position and home purchase decision. This leads to the change in homeownership η​(1)\eta(1), which in turn leads to the demand growth yd​(1)y\_{d}(1). The simulation proceeds iteratively: in each period tt, the macroeconomic and financial variables are updated using the estimated econometric model, incorporating the endogenous demand function yd​(t−1)y\_{d}(t-1). These updated values are fed into the life-cycle model to determine household decisions and extract yd​(t)y\_{d}(t) for the next period. This iterative process continues until all households have exited the model due to default or death.

The entire process is repeated for the three competing settings, Option 1 with required deposit of δ=20%\delta=20\% (i.e. benchmark), Option 2 where early pension withdrawal is allowed with required deposit δ=20%\delta=20\% (i.e. Coalition’s proposal), and Option 1 with δ=5%\delta=5\% (i.e. Labor’s proposal with reduced deposit). The same simulated residuals are used to ensure comparability.

Repeating the procedure for each economic scenario m=1,…,me​c​om=1,...,m^{eco} yields realizations of the key output variables. Namely, for each household i=1,…,N​(0)i=1,...,N(0): the purchase time Tp(i)T\_{p}^{(i)}, the savings account balance at retirement A(i)​(Tr)A^{(i)}(T\_{r}), the disposable income net of housing costs I(i)​(t)−H(i)​(t)I^{(i)}(t)-H^{(i)}(t) at each time t≥Trt\geq T\_{r}, the time death Tσ(i)T\_{\sigma}^{(i)}, the salary S(i)S^{(i)}, the guaranteed pension income G(i)​(t)G^{(i)}(t), the property maintenance fees μp(j)​(t)\mu\_{p}^{(j)}(t), and all tax functions. All these output variables are synthesized into the evaluation metrics described in the next subsection.

Note that the time of default is not used in the metrics because none of the households in the population exits due to default. This is explained by two features of the model. The first feature is that property purchase is subject to the affordability constraint, where purchase is permitted only when disposable income exceeds repayments. The second is that non-housing consumption is expressed as a deterministic percentage of disposable income net of housing, with a lower bound. This means that households cannot spend more than their disposable income on non-housing consumption. This is in general not the case, as non-housing consumption of low-income groups tends to exceed disposable income. In particular, low-income groups in the model of the present analysis are more likely to access the property market than in real life.

### 3.4 Evaluation metrics

This subsection introduces seven metrics used to evaluate the two policies. The first three metrics assess the impact on household financial outcomes, measuring housing accessibility (probability of remaining a renter, and time of purchase), and retirement financial security. The next two metrics evaluate distributional effects across income percentiles, focusing on the Gini coefficients of the time of homeownership access and post-retirement financial security. The final two metrics take the government perspective by looking into the net present value of tax revenue minus government subsidies for both the federal and state (local) governments.

Throughout this section, all expectations and probabilities are taken over economic scenarios. Additionally, the tilde notation refers to quantities for the policy being evaluated, while the bar notation refers to those determined under the benchmark Option 1 with δ=20%\delta=20\%. The notation 𝒦k\mathcal{K}\_{k} corresponds to the set of individuals ii in income group k=1,…,5k=1,...,5 at time 0.

Housing accessibility is measured by Δa(k)\Delta\_{a}^{(k)} and Δp(k)\Delta\_{p}^{(k)}, which represent the difference in the probability of purchase, and the expected purchase age (in years starting from age 25), respectively. When computed at the population level rather than for a specific income percentile, the notations Δa(∙)\Delta\_{a}^{(\bullet)} and Δp(∙)\Delta\_{p}^{(\bullet)} are used. The two metrics are defined as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δa(k)\displaystyle\Delta\_{a}^{(k)} | =\displaystyle= | 1|𝒦k|​∑i∈𝒦k(ℙ​[T~p(i)<Tσ(i)]−ℙ​[T¯p(i)<Tσ(i)]),\displaystyle\frac{1}{|\mathcal{K}\_{k}|}\sum\_{i\in\mathcal{K}\_{k}}\left(\mathbb{P}\left[\tilde{T}^{(i)}\_{p}<T\_{\sigma}^{(i)}\right]-\mathbb{P}\left[\bar{T}^{(i)}\_{p}<T\_{\sigma}^{(i)}\right]\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δp(k)\displaystyle\Delta\_{p}^{(k)} | =\displaystyle= | 1|𝒦k|​∑i∈𝒦k𝔼​[25+T~p(i)4]−𝔼​[25+T¯p(i)4].\displaystyle\frac{1}{|\mathcal{K}\_{k}|}\sum\_{i\in\mathcal{K}\_{k}}\mathbb{E}\left[25+\frac{\tilde{T}\_{p}^{(i)}}{4}\right]-\mathbb{E}\left[25+\frac{\bar{T}\_{p}^{(i)}}{4}\right]. |  |

The difference Δa(k)\Delta\_{a}^{(k)} evaluates the impact of a policy on the likelihood of purchasing, and positive values imply that the policy improves accessibility to homeownership. The difference Δp(k)\Delta\_{p}^{(k)} evaluates the impact of a policy on the age of purchase for those who purchase. Negative values indicates that the policy reduces the time to homeownership. Note that comparing the age of purchase across policies is challenging because some households may never purchase under one policy, leaving their purchase age undefined. Moreover, conditioning on purchase can be misleading, as a policy that enables more households to buy, albeit at older ages, may suggest an increase in conditional time of purchase despite being effective. To address this, households who do not purchase under a given policy are assigned a purchase time equal to the maximum survival horizon of 300 quarters. Under this convention, negative values of Δp(k)\Delta^{(k)}\_{p} indicate that the policy leads to earlier or more frequent purchases, capturing its positive impact.

The impact on retirement security is quantified using the relative difference Δs(k)\Delta\_{s}^{(k)} for income percentile kk and Δs(∙)\Delta\_{s}^{(\bullet)} at the population level. This metric measures the expected present value of post-retirement disposable income, net of housing consumption, along with accumulated savings at the time of retirement. It reflects a household’s ability to sustain consumption and maintain financial stability throughout retirement. Negative values indicate that retirement security deteriorates under a given policy. The relative difference Δs(k)\Delta\_{s}^{(k)} is defined as:

|  |  |  |
| --- | --- | --- |
|  | Δs(k)=1|𝒦k|​∑i∈𝒦k𝔼​[ℐ~(i)ℐ¯(i)−1],\Delta\_{s}^{(k)}=\frac{1}{|\mathcal{K}\_{k}|}\sum\_{i\in\mathcal{K}\_{k}}\mathbb{E}\left[\frac{\tilde{\mathcal{I}}^{(i)}}{\bar{\mathcal{I}}^{(i)}}-1\right], |  |

where ℐ¯(i)\bar{\mathcal{I}}^{(i)} and ℐ~(i)\tilde{\mathcal{I}}^{(i)} represent the post-retirement disposable income net of housing consumption of household ii under one of the two proposed policy and under the benchmark, respectively, with:

|  |  |  |
| --- | --- | --- |
|  | ℐ(i)=A(i)​(Tr)+∑t≥Trσ(i)​(t)​(1−d(i)​(t))​v​(Tr,t)​(I(i)​(t)−H(i)​(t)),\mathcal{I}^{(i)}=A^{(i)}(T\_{r})+\sum\_{t\geq T\_{r}}\sigma^{(i)}(t)(1-d^{(i)}(t))v(T\_{r},t)\left(I^{(i)}(t)-H^{(i)}(t)\right), |  |

with v​(Tr,t)v(T\_{r},t) being the discounting factor from time tt to retirement time TrT\_{r}, determined using the cash-rate and inflation. The income measure ℐ(i)\mathcal{I}^{(i)} allows for the savings account balance at the time of retirement (A(i)​(Tr)A^{(i)}(T\_{r})) and captures the effect of homeownership or renting on post-retirement income through the H(i)​(t)H^{(i)}(t) term, while both the social security payments and the pension fund balance are implicitly reflected through the I(i)​(t)I^{(i)}(t) term. The measure ignores bequest in the form of any unused funds in the pension fund and the housing wealth at death of the household.

The impact of the housing policies on inequality is assessed through two Gini-based metrics, one for purchase time inequality denoted by Δ𝒢|p\Delta\_{\mathcal{G}|p}, and another for retirement security inequality denoted by Δ𝒢|s\Delta\_{\mathcal{G}|s}. These metrics measure how a policy affects disparities in homeownership access and post-retirement financial stability, and they are defined as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ𝒢|p\displaystyle\Delta\_{\mathcal{G}|p} | =\displaystyle= | 𝒢~p−𝒢¯p,\displaystyle\tilde{\mathcal{G}}\_{p}-\bar{\mathcal{G}}\_{p}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ𝒢|s\displaystyle\Delta\_{\mathcal{G}|s} | =\displaystyle= | 𝒢~s−𝒢¯s,\displaystyle\tilde{\mathcal{G}}\_{s}-\bar{\mathcal{G}}\_{s}, |  |

where 𝒢¯p\bar{\mathcal{G}}\_{p} and 𝒢~p\tilde{\mathcal{G}}\_{p} denote the expected Gini coefficients for purchase time inequality under a housing policy and the benchmark, respectively, and 𝒢¯s\bar{\mathcal{G}}\_{s} and 𝒢~s\tilde{\mathcal{G}}\_{s} represent the corresponding expected Gini coefficients for retirement security. Specifically:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒢p\displaystyle\mathcal{G}\_{p} | =\displaystyle= | 𝔼​[(∑i=1N​(0)​∑i′=1N​(0)​|Tp(i)−Tp(i′)|)/(2​N​(0)​∑i=1N​(0)​Tp(i))],\displaystyle\mathbb{E}\left[\left(\underset{i=1}{\overset{N(0)}{\sum}}\underset{i^{\prime}=1}{\overset{N(0)}{\sum}}|T\_{p}^{(i)}-T\_{p}^{(i^{\prime})}|\right)/\left(2N(0)\underset{i=1}{\overset{N(0)}{\sum}}T\_{p}^{(i)}\right)\right], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒢s\displaystyle\mathcal{G}\_{s} | =\displaystyle= | 𝔼​[(∑i=1N​(0)​∑i′=1N​(0)​|ℐ(i)−ℐ(i′)|)/(2​N​(0)​∑i=1N​(0)​ℐ(i))].\displaystyle\mathbb{E}\left[\left(\underset{i=1}{\overset{N(0)}{\sum}}\underset{i^{\prime}=1}{\overset{N(0)}{\sum}}|\mathcal{I}^{(i)}-\mathcal{I}^{(i^{\prime})}|\right)/\left(2N(0)\underset{i=1}{\overset{N(0)}{\sum}}\mathcal{I}^{(i)}\right)\right]. |  |

The Gini coefficient for purchase time 𝒢p\mathcal{G}\_{p} measures the dispersion of home acquisition timing across individuals, while the Gini coefficient of post-retirement financial stability captures disparities in the present value of post-retirement disposable income net of housing costs. Negative values of Δ𝒢|p\Delta\_{\mathcal{G}|p} and Δ𝒢|s\Delta\_{\mathcal{G}|s} suggest a reduction in disparties due to the introduction of the housing policy under interest.

The last two metrics evaluate the effect of a housing policy on government finances by comparing the net expected present value (NPV) of government revenues and expenditures under both policy settings. Specifically, ΔF​e​d​e​r​a​l\Delta\_{Federal} and ΔL​o​c​a​l\Delta\_{Local} measure the impact on the federal and local (state/council) governments, respectively, such that:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΔF​e​d​e​r​a​l\displaystyle\Delta\_{Federal} | =\displaystyle= | V~F​e​d​e​r​a​l−V¯F​e​d​e​r​a​l,\displaystyle\tilde{V}\_{Federal}-\bar{V}\_{Federal}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΔL​o​c​a​l\displaystyle\Delta\_{Local} | =\displaystyle= | V~L​o​c​a​l−V¯L​o​c​a​l,\displaystyle\tilde{V}\_{Local}-\bar{V}\_{Local}, |  |

where V¯F​e​d​e​r​a​l\bar{V}\_{Federal} and V~F​e​d​e​r​a​l\tilde{V}\_{Federal} are the NPV’s of the federal government, while V¯L​o​c​a​l\bar{V}\_{Local} and V~L​o​c​a​l\tilde{V}\_{Local} are the corresponding NPV’s of the local government. In this model, federal government income consists of income tax (τI\tau\_{I}), taxes on savings and pension returns (τA\tau\_{A} and τF\tau\_{F}), and taxes on employer superannuation contributions (τγ​γ​S​(t)\tau\_{\gamma}\gamma S(t)). The federal government’s expenditure is the Age Pension payments (G​(t)G(t)). For the local government, revenue comes from the property transfer tax (τP​(Tp)\tau\_{P}(T\_{p})) at the time of purchase, as well as ongoing council rates, which are assumed to be 40% of property maintenance costs μp​(t)\mu\_{p}(t) post-purchase. Thus, VF​e​d​e​r​a​l=1N​(0)​∑i=1N​(0)​𝔼​[𝒱F​e​d​e​r​a​l(i)]V\_{Federal}=\frac{1}{N(0)}\underset{i=1}{\overset{N(0)}{\sum}}\mathbb{E}\left[\mathcal{V}^{(i)}\_{Federal}\right] and VL​o​c​a​l=1N​(0)​∑i=1N​(0)​𝔼​[𝒱L​o​c​a​l(i)]V\_{Local}=\frac{1}{N(0)}\underset{i=1}{\overset{N(0)}{\sum}}\mathbb{E}\left[\mathcal{V}^{(i)}\_{Local}\right], with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱F​e​d​e​r​a​l(i)\displaystyle\mathcal{V}^{(i)}\_{Federal} | =\displaystyle= | ∑t≥0​σ(i)​(t)​(1−d(i)​(t))​v​(0,t)​(τI(i)​(t)+τA(i)​(t)+τF(i)​(t)+τγ​γ​S(i)​(t)​𝕀​[t<Tr]−G(i)​(t)),\displaystyle\underset{t\geq 0}{\sum}\sigma^{(i)}(t)(1-d^{(i)}(t))v(0,t)\left(\tau\_{I}^{(i)}(t)+\tau\_{A}^{(i)}(t)+\tau\_{F}^{(i)}(t)+\tau\_{\gamma}\gamma S^{(i)}(t)\mathbb{I}\left[t<T\_{r}\right]-G^{(i)}(t)\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱L​o​c​a​l(i)\displaystyle\mathcal{V}^{(i)}\_{Local} | =\displaystyle= | ∑t≥0​σ(i)​(t)​(1−d(i)​(t))​v​(0,t)​(τP​(t)​𝕀​[t=Tp(i)]+0.4​μp​(t)​𝕀​[t≥Tp(i)]).\displaystyle\underset{t\geq 0}{\sum}\sigma^{(i)}(t)(1-d^{(i)}(t))v(0,t)\left(\tau\_{P}(t)\mathbb{I}\left[t=T\_{p}^{(i)}\right]+0.4\mu\_{p}(t)\mathbb{I}\left[t\geq T\_{p}^{(i)}\right]\right). |  |

The effect on total government revenue is given by Δg​o​v​e​r​n​m​e​n​t=ΔF​e​d​e​r​a​l+ΔL​o​c​a​l\Delta\_{government}=\Delta\_{Federal}+\Delta\_{Local}.

## 4 Results

### 4.1 Impact of policies on property price

![Refer to caption](x1.png)


Figure 1: Impact of housing policies on property price dynamics – Ratio of the property price index under each policy to the baseline scenario with no policy. Results are shown under two market assumptions: equal-affordability (left) and supply-constrained (right). The blue line corresponds to the Early Withdrawal policy, while the red line corresponds to the Reduced Deposit policy. Values above 1 mean that property price increase due to the introduction of the policy.

Figure [1](https://arxiv.org/html/2511.01133v1#S4.F1 "Figure 1 ‣ 4.1 Impact of policies on property price ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") displays the impact of the two housing policies on property prices, expressed as the ratio of the simulated property price index under each policy to the baseline scenario with no policy. Results are shown for both the equal-affordability (left panel) and supply-constrained market assumptions (right panel).

The estimates in Figure [1](https://arxiv.org/html/2511.01133v1#S4.F1 "Figure 1 ‣ 4.1 Impact of policies on property price ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") are consistent in direction to the research of Super Members Council ([2025](https://arxiv.org/html/2511.01133v1#bib.bib25)), but the magnitudes are higher. Specifically, Super Members Council ([2025](https://arxiv.org/html/2511.01133v1#bib.bib25)) suggests an average increase of 9% across the capital cities, whereas Figure [1](https://arxiv.org/html/2511.01133v1#S4.F1 "Figure 1 ‣ 4.1 Impact of policies on property price ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") suggests peaks around 20%, which are especially more pronounced in the supply-constrained market.

Under both policy regimes, EW leads to a slightly higher peak in the property price index compared to RD. RD policy generates an earlier price response, due to its lower liquidity requirement. While both policies aim to reduce the deposit constraint, the EW policy requires a 5% deposit from savings and 15% from superannuation, whereas the RD policy requires only a 5% deposit, with the remainder guaranteed by the government. Consequently, under the RD policy, buyers can enter the market more rapidly, which drives prices up sooner.

Under both policies and across both market assumptions, the property price index ratio converges to 1 in the long run. This indicates that the demand shock introduced by each policy is largely a temporal reallocation rather than a structural increase in total purchasing power. The implication is that, in the absence of ongoing new entrants, the long-term equilibrium price is not permanently shifted; only the timing of demand is altered. This provides a preliminary inference on the inefficiency of both housing policies.

Note that the absence of new entrants in the simulation design, Figure [1](https://arxiv.org/html/2511.01133v1#S4.F1 "Figure 1 ‣ 4.1 Impact of policies on property price ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") exhibits two features that are unlikely in practice. The first feature is the temporary dip around age 35, which is due to the fact that once the initial wave of buyers enters the market earlier than they would under the baseline, the pool of new entrants dries up, creating downward pressure on prices. The second feature is the smaller peak is observed around retirement age under the EW policy, which appears because households who were unable to purchase earlier accumulate sufficient superannuation to enter the market later in life.

### 4.2 Impact of policies on households and government income

The impact of the two housing policies on home purchase outcomes is presented in Figure [2](https://arxiv.org/html/2511.01133v1#S4.F2 "Figure 2 ‣ 4.2 Impact of policies on households and government income ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") for the equal-affordability property market, and Figure [3](https://arxiv.org/html/2511.01133v1#S4.F3 "Figure 3 ‣ 4.2 Impact of policies on households and government income ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") under the supply-constrained market.

![Refer to caption](x2.png)


Figure 2: Impact of housing policies on households and government income in the Equal-Affordability property market – 
Top two rows show effects on (i) the probability of purchase in percent, (ii) average age at purchase in years, and (iii) retirement financial security in million dollars, by income group 𝒦1\mathcal{K}\_{1} (lowest percentile) to 𝒦5\mathcal{K}\_{5} (highest percentile), with 𝒦0\mathcal{K}\_{0} (dashed bars) representing the full population. Results on the first row represent those of the early withdrawal policy (E.W.), and on the second row represent those of the reduced deposit policy (R.D.).
Middle row reports the Gini indices in percent of purchase timing and retirement security.
Bottom row presents the effect on the present value of federal government income in billion dollars (left), state government income in hundred million dollars (middle), and combined government income in billion dollars (right). For all panel, black bars represent baseline values under no policy, and coloured annotations reflect changes induced by the corresponding policy. Differences in green indicate a favourable outcome from the implementation of the policy, whereas differences in red indicate unfavourable one.

![Refer to caption](x3.png)


Figure 3: Impact of housing policies on households and government income in the Supply-Constrained property market – 
Top two rows show effects on (i) the probability of purchase in percent, (ii) average age at purchase in years, and (iii) retirement financial security in million dollars, by income group 𝒦1\mathcal{K}\_{1} (lowest percentile) to 𝒦5\mathcal{K}\_{5} (highest percentile), with 𝒦0\mathcal{K}\_{0} (dashed bars) representing the full population. Results on the first row represent those of the early withdrawal policy (E.W.), and on the second row represent those of the reduced deposit policy (R.D.).
Middle row reports the Gini indices in percent of purchase timing and retirement security.
Bottom row presents the effect on the present value of federal government income in billion dollars (left), state government income in hundred million dollars (middle), and combined government income in billion dollars (right). For all panel, black bars represent baseline values under no policy, and coloured annotations reflect changes induced by the corresponding policy. Differences in green indicate a favourable outcome from the implementation of the policy, whereas differences in red indicate unfavourable one.

Beginning with the probability of purchase, the EW policy leads to a modest increase across the population, with gains below 1% observed among all groups, mostly due to the fact that all households have an already high probability of purchase. In contrast, the RD policy consistently lowers that probability. In the equal-affordability market, the RD policy reduces accessibility for high-income earners more than low-income ones, whereas in the supply-constrained market, low-income earners experience the strongest negative effect with a 4.3% decline in accessibility. This decline is due to the fact RD pushes prices up earlier than EW, and the income required to meet repayments is higher.

In terms of timing, EW shifts purchases earlier for all income groups, with lower gains for low-income groups (0.6 years), and higher gains for second and third income groups (1-1.1 years). RD leads to different effect. In the equal-affordability market, households from all income groups are expected to purchase about 0.9 to 2 years later, whereas in the supply-constrained market, high-income groups buy 1.2 years earlier and low-income groups buy 4.7 years later. These shifts in timing are reflected in the Gini index of the age of purchase. Specifically, both policies lead to marginal increases in inequality in the equal-affordability market, but in the supply-constrained market, RD leads to an increase of 6.5% in the Gini index of accessibility, while EW leads to an increase of 1.4%. The differing outcomes between the equal-affordability and supply-constrained markets indicate that these housing policies do not create inequality by themselves, but they tend to exacerbate inequalities that already exist in the housing market, with RD having the strongest effect.

Retirement security is adversely affected by the EW policy for all groups, especially in the supply-constrained markets, where losses range from -3.6% for the second lowest-income households to -1.5% for the highest group. This reflects the lower long-term returns from early property investment compared to retaining funds in superannuation. RD, by contrast, improves retirement outcomes across the board, with gains of 3.3–8.5% depending on the income group and the property market setup. Gains in retirement security are largest for households who forego purchasing and benefit from compounding superannuation returns. None of the policies affects the Gini index of retirement security, with changes between -0.6% and 0.2% indicating that the gains do not significantly improve existing inequality.

Under EW, federal government income remains largely unchanged, while state government revenue increases by approximately 2.1% in the equal-affordability setting and 3.5% in the supply-constrained setting. This is driven by earlier home purchases, which increases the present value of property transfer tax and longer collection of council rates. In contrast, RD leads to a small increase in federal government income around 2%, reflecting stronger superannuation balances that reduce long-term Age Pension liabilities. However, state government revenue declines by 8.1% under equal-affordability and 1.2% under supply constrained, which is due to reduced transaction volumes and delayed purchases. Since the total government revenue in this setup is largely influenced by the revenue from the federal level, the combined figures for the total government revenue reflect the effect of the revenue from the federal level.

Overall, the RD policy undermines housing accessibility and exacerbates existing inequalities in supply-constrained markets, where it lowers the likelihood of purchase for low-income households and delays their market entry. In contrast, the EW policy facilitates earlier purchases across all income groups, though not uniformly. Its effectiveness in improving housing access comes at the cost of reduced retirement security for all households, given the lower long-term returns on housing relative to superannuation. Conversely, RD enhances retirement outcomes, but this improvement is incidental to its purpose and highlights a mismatch between intent and effect. From a public finance perspective, neither policy generates a clear fiscal benefit; EW marginally increases local government revenue via earlier stamp duty payments, while RD slightly improves federal government balances but reduces local government income.

### 4.3 Effect of price sensitivity to demand

Sensitivity to demand was examined by varying the property-price growth coefficient in two directions, either a high-demand case (coefficient doubled) or a low-demand case (coefficient halved); see Table [3](https://arxiv.org/html/2511.01133v1#A1.T3 "Table 3 ‣ A.2 More details on pension rules ‣ Appendix A Appendix ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") for the baseline parameter. Results are not reported because these changes do not materially alter the magnitude of policy effects under either market structure.

As expected, unreported figures show a larger surge of about 60% when the coefficient is doubled and a smaller surge of about 10% when it is halved. However, household and gorvernment revenue outcomes are largely unaffected. In the equal-affordability market, doubling or halving the coefficient changes purchase probability, retirement security, Gini indices, and government revenue by roughly 0.1%, and shifts the purchase age by about 0.1 years. In the supply-constrained market, differences are similarly small when comparing low- and high-demand cases, except for retirement security. The response is mildly nonlinear, where both EW and RD improve when the coefficient is either doubled or halved, but the gains do not exceed 2%. Overall, a stronger or weaker demand sensitivity shifts both the benchmark and the policy paths in the same direction, but leaves the relative policy effects essentially unchanged.

### 4.4 Effect of superannuation return

Superannuation returns influence the model through two main channels. First, they affect the timing and likelihood of home purchase. Under the EW policy, lower returns reduce the future pension balance available for withdrawal, potentially delaying purchase. Under both EW and RD, super returns also affect purchase probability and timing for households that can afford buying until after retirement. Second, superannuation returns directly impact retirement financial security. In the baseline calibration, superannuation outperforms housing investment, meaning early purchase leads to forgone pension returns, which in turn reduces retirement security. This trade-off is most evident under the RD policy in the baseline, which delays or prevents purchase and thereby improves retirement outcomes.

The average superannuation return was reduced to match the average growth rate of property prices. Unreported results show that this adjustment had minimal impact on the property price path under RD but attenuated the price surge under EW. Specifically, whereas Figure [1](https://arxiv.org/html/2511.01133v1#S4.F1 "Figure 1 ‣ 4.1 Impact of policies on property price ‣ 4 Results ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") showed peak price increases of 18% (equal-affordability) and 26% (supply-constrained) under EW, these peaks declined to approximately 13% and 23%, respectively. In terms of household outcomes and government revenue, lowering the superannuation return led to negligible differences. Compared to the baseline, relative changes in purchase probability are below 1% compared to the baseline, and average purchase ages are around ±\pm0.2 years. The impact on retirement financial security was more pronounced. Under EW, the effect turned slightly positive (compared to negative in the baseline), while under RD, the gains in retirement security roughly doubled.

## 5 Policy alternatives

This section explores two alternative designs of the EW and RD policies. The first subsection examines the effects of restricting policy access to lower income households only. The second subsection analyzes extreme parameter settings for the EW policy: one in which households can withdraw up to 100% of their superannuation balance (i.e. β=100%\beta=100\%), and another where no savings contribution is required from the household (i.e. α=0%\alpha=0\%), meaning the entire 40% withdrawn amount can be used toward the deposit.

### 5.1 Impact of restricted policies

Figures [4](https://arxiv.org/html/2511.01133v1#S5.F4 "Figure 4 ‣ 5.1 Impact of restricted policies ‣ 5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") and [5](https://arxiv.org/html/2511.01133v1#S5.F5 "Figure 5 ‣ 5.1 Impact of restricted policies ‣ 5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") report the main metrics for the equal-affordability and supply-constrained markets when policy access is limited to households below the all-age population median income. This restriction initially excludes only the top income percentile among 25-year-olds. Ignoring salary inflation a​w​e​(t)awe(t), the age profile implies that the lowest-income group at age 25 exceeds the population median by about age 40.

Restricting access below the median changes the distribution of outcomes only marginally and preserves the qualitative differences between policies. For EW, low income groups benefit as they would have under the unconstraint policy setup, although the gain in purchase age is lower in the supply-constrained market. Effects on the Gini indices and government revenue are not significant. For RD, the pattern also mirrors the universally accessible case, with attenuated effects for higher-income groups and amplified adverse effects for lower-income groups despite the policy being restricted. This occurs because the highest earners within the lower-income segment bid up property prices, leaving the least affluent households unable to meet the affordability constraint.

Overall, restricting EW to low income earners does not improve its efficiency, while a restricted RD does not improve accessibility for its intended beneficiaries and still increases inequality in purchase timing, especially under supply constraints. Unreported results with access restricted to the lowest 25th percentile show both policies leading to near-zero differences relative to the benchmark.

![Refer to caption](x4.png)


Figure 4: Impact of restricted housing policies (access only to below all-ages population median income) on households and government income in the Equal-Affordability property market – 
Top two rows show effects on (i) the probability of purchase in percent, (ii) average age at purchase in years, and (iii) retirement financial security in million dollars, by income group 𝒦1\mathcal{K}\_{1} (lowest percentile) to 𝒦5\mathcal{K}\_{5} (highest percentile), with 𝒦0\mathcal{K}\_{0} (dashed bars) representing the full population. Results on the first row represent those of the early withdrawal policy (E.W.), and on the second row represent those of the reduced deposit policy (R.D.).
Middle row reports the Gini indices in percent of purchase timing and retirement security.
Bottom row presents the effect on the present value of federal government income in billion dollars (left), state government income in hundred million dollars (middle), and combined government income in billion dollars (right). For all panel, black bars represent baseline values under no policy, and coloured annotations reflect changes induced by the corresponding policy. Differences in green indicate a favourable outcome from the implementation of the policy, whereas differences in red indicate unfavourable one.

![Refer to caption](x5.png)


Figure 5: Impact of restricted housing policies (access only to below all-ages population median income) on households and government income in the Supply-Constrained property market – 
Top two rows show effects on (i) the probability of purchase in percent, (ii) average age at purchase in years, and (iii) retirement financial security in million dollars, by income group 𝒦1\mathcal{K}\_{1} (lowest percentile) to 𝒦5\mathcal{K}\_{5} (highest percentile), with 𝒦0\mathcal{K}\_{0} (dashed bars) representing the full population. Results on the first row represent those of the early withdrawal policy (E.W.), and on the second row represent those of the reduced deposit policy (R.D.).
Middle row reports the Gini indices in percent of purchase timing and retirement security.
Bottom row presents the effect on the present value of federal government income in billion dollars (left), state government income in hundred million dollars (middle), and combined government income in billion dollars (right). For all panel, black bars represent baseline values under no policy, and coloured annotations reflect changes induced by the corresponding policy. Differences in green indicate a favourable outcome from the implementation of the policy, whereas differences in red indicate unfavourable one.

### 5.2 Boundary cases of the EW policy

The baseline EW design allows withdrawals up to 40%40\% of the pension balance, subject to an absolute cap of $50,000, and requires a minimum 5%5\% contribution from the savings account (β=40%\beta=40\%, Fmax=50,000F^{\max}=50{,}000, α=5%\alpha=5\%). Two boundary cases are considered. In the first, households may withdraw their entire pension balance with the same 5%5\% savings contribution (β=100%\beta=100\%, Fmax=∞F^{\max}=\infty, α=5%\alpha=5\%). In the second, withdrawals remain capped at 40%40\% but no savings contribution is required (β=40%\beta=40\%, Fmax=50,000F^{\max}=50{,}000, α=0%\alpha=0\%). Unreported results indicate that both boundary cases generate larger property price surges than the baseline, with surges reaching 40% when β=100%\beta=100\% in the supply-constrained market.

Figures [6](https://arxiv.org/html/2511.01133v1#S5.F6 "Figure 6 ‣ 5.2 Boundary cases of the EW policy ‣ 5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") and [7](https://arxiv.org/html/2511.01133v1#S5.F7 "Figure 7 ‣ 5.2 Boundary cases of the EW policy ‣ 5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") present the main metrics for the equal-affordability and supply-constrained markets under the two boundary cases. Both policies increase the probability of purchase relative to the baseline across market types. In the equal-affordability market, the rise is more pronounced among high-income households, whereas in the supply-constrained market, it is greater for low-income households, reaching up to 5.5%5.5\% when β=100%\beta=100\%. Boundary cases also lead to earlier purchases compared to the baseline, particularly for β=100%\beta=100\%. The largest shift in the equal-affordability market occurs among high-income households (3.1 years earlier), while in the supply-constrained market the improvement is relatively uniform across income groups (2.4 years earlier on average). The Gini index of purchase timing increases substantially in the supply-constrained market, but in this case, the inequality appears to benefit lower-income households.

Retirement security declines more sharply in the boundary cases, deteriorating by up to 11% for low-income groups under β=100%\beta=100\%. By the return comparison logic, when pension returns exceed property price growth (as in the baseline), increasing purchases shifts wealth from the higher-return pension account to housing, thereby reducing retirement security. Because both boundary designs raise the probability of purchase, the deterioration is larger than under the baseline. The figures also show a pronounced rise in state government revenue from stamp duty, reflecting higher purchase activity. Total government revenue, however, remains essentially unchanged.

Note that consistent with Figures [4](https://arxiv.org/html/2511.01133v1#S5.F4 "Figure 4 ‣ 5.1 Impact of restricted policies ‣ 5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit") and [5](https://arxiv.org/html/2511.01133v1#S5.F5 "Figure 5 ‣ 5.1 Impact of restricted policies ‣ 5 Policy alternatives ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit"), unreported simulations that restrict boundary-case access to low-income households yield only modest changes, indicating limited gains when targeting alone is used to mitigate adverse effects.

Overall, the boundary designs generate stronger effects than the baseline. Low-income households experience higher purchase probabilities, and all income groups are able to buy earlier. These results suggest that a social planner aiming to improve housing accessibility should permit full pension withdrawals, as this can increase market participation without worsening inequality among lower-income groups. However, such a strategy can undermine retirement security when pension returns substantially exceed property growth. This trade-off highlights the need for coordinated policy design that balances immediate housing accessibility with long-term financial sustainability, ensuring that short-term equity gains do not come at the cost of future welfare.

![Refer to caption](x6.png)


Figure 6: Impact of EW on households and government income in the Equal-Affordability property market in the boundary cases where either β=100%\beta=100\% and α=5%\alpha=5\%, or β=40%\beta=40\% and α=0%\alpha=0\% – 
Top two rows show effects on (i) the probability of purchase in percent, (ii) average age at purchase in years, and (iii) retirement financial security in million dollars, by income group 𝒦1\mathcal{K}\_{1} (lowest percentile) to 𝒦5\mathcal{K}\_{5} (highest percentile), with 𝒦0\mathcal{K}\_{0} (dashed bars) representing the full population. Results on the first row represent those where β=100%\beta=100\% and α=5%\alpha=5\%, and on the second row represent those where β=40%\beta=40\% and α=0%\alpha=0\%.
Middle row reports the Gini indices in percent of purchase timing and retirement security.
Bottom row presents the effect on the present value of federal government income in billion dollars (left), state government income in hundred million dollars (middle), and combined government income in billion dollars (right). For all panel, black bars represent baseline values under no policy, and coloured annotations reflect changes induced by the corresponding policy. Differences in green indicate a favourable outcome from the implementation of the policy, whereas differences in red indicate unfavourable one.

![Refer to caption](x7.png)


Figure 7: Impact of EW on households and government income in the Supply-Constrained property market in the boundary cases where either β=100%\beta=100\% and α=5%\alpha=5\%, or β=40%\beta=40\% and α=0%\alpha=0\% – 
Top two rows show effects on (i) the probability of purchase in percent, (ii) average age at purchase in years, and (iii) retirement financial security in million dollars, by income group 𝒦1\mathcal{K}\_{1} (lowest percentile) to 𝒦5\mathcal{K}\_{5} (highest percentile), with 𝒦0\mathcal{K}\_{0} (dashed bars) representing the full population. Results on the first row represent those where β=100%\beta=100\% and α=5%\alpha=5\%, and on the second row represent those where β=40%\beta=40\% and α=0%\alpha=0\%.
Middle row reports the Gini indices in percent of purchase timing and retirement security.
Bottom row presents the effect on the present value of federal government income in billion dollars (left), state government income in hundred million dollars (middle), and combined government income in billion dollars (right). For all panel, black bars represent baseline values under no policy, and coloured annotations reflect changes induced by the corresponding policy. Differences in green indicate a favourable outcome from the implementation of the policy, whereas differences in red indicate unfavourable one.

## 6 Conclusion

This paper examines two housing policy proposals put forward in Australia in the lead-up to the 2025 federal election. Both policies aim to relax liquidity constraints on first-home buyers, thereby affecting the demand for housing. To evaluate their impact, a model is developed that links housing demand to housing prices for a cohort of 25-year-old with no initial savings, full employment throughout their working years, and no external financial support.

Both policies significantly increase property prices in the short term, with effects that would be amplified in a multi-cohort setting over the long term. RD is detrimental to housing accessibility of low-income groups, especially in supply-constrained markets. EW improves accessibility for all groups but raises a trade-off with retirement financial security when pension returns are substiantially high. Restricting access to below-median or bottom-quartile income groups does not materially alter the outcomes for unrestricted groups. Fiscal impacts are minor in both cases. The results are robust to doubling or halving the price sensitivity to demand. Boundary EW cases amplify purchase probabilities and price levels, and suggest that a social planner aiming at improving housing accessibility only should allow full pension withdrawal.

The paper also sharpens how price-inflating housing policies are interpreted, and derives broader results on liquidity shocks. Rising prices aren’t always harmful. Both RD and EW raise prices in the short run, but RD delays or prevents access for lower-income households, whereas EW can significantly improve accessibility with little downside for inequality. Crucially, the results from RD’s distributional effects are in large part driven by market structure, not by the price surge itself. In equal-affordability versus supply-constrained settings, low-income purchase timing shifts in opposite directions, indicating that pre-existing market disparities produce the unequal outcomes.

Future research could incorporate supply-side interventions from international experience, allowing for a deeper understanding of how to mitigate inequality in market structure. A further extension is to model multiple cohorts of new entrants so that feedback from repeated policy exposure, cross-cohort price dynamics, and intergenerational inequalities can be quantified.

## References

* (1)
* Agarwal et al. (2023)

  Agarwal, S., Hu, M. R. and Lee, A. D. (2023), ‘Market impacts and unintended consequences of
  housing assistance policies with price threshold’, Available at SSRN .
* Akhmedyarova (2023)

  Akhmedyarova, A. (2023), ‘Housing market
  dynamics in Kazakhstan: An estimated DSGE model’, International Real
  Estate Review 26, 420–462.
* Andréasson and Shevchenko (2024)

  Andréasson, J. G. and Shevchenko, P. V. (2024), ‘Optimal annuitisation, housing and reverse mortgage
  in retirement in the presence of a means-tested public pension’, European Actuarial Journal 14, 871–904.
* Atalay and Edwards (2022)

  Atalay, K. and Edwards, R. (2022),
  ‘House prices, housing wealth and financial well-being’, Journal of
  Urban Economics p. 103438.
* Beech et al. (2014)

  Beech, A., Dollman, R., Finlay, R. and La Cava, G. (2014), ‘The distribution of household spending in
  Australia’, March 2014 Bulletin of the Reserve Bank of Australia
  pp. 1–10.
* Berger et al. (2020)

  Berger, D., Turner, N. and Zwick, E. (2020), ‘Stimulating housing markets’, Journal of
  Finance 75, 277–321.
* Binner and Day (2015)

  Binner, A. and Day, B. (2015),
  ‘Exploring mortgage interest deduction reforms: an equilibrium sorting model
  with endogenous tenure choice’, Journal of Public Economics pp. 40–54.
* Bourassa et al. (2013)

  Bourassa, S., Haurin, D., Hendershott, P. and Hoesli, M.
  (2013), ‘Mortgage interest deductions and
  homeownership: An international survey’, Journal of Real Estate
  Literature 21, 181–203.
* Carozzi et al. (2024)

  Carozzi, F., Hilber, Christian, A. and Yu, X. (2024), ‘On the economic impacts of mortgage credit expansion
  policies: Evidence from help to buy’, Journal of Urban Economics 139, 103611.
* Cho and Sane (2013)

  Cho, S.-W. S. and Sane, R. (2013),
  ‘Means-tested age pensions and homeownership: Is there a link?’, Macroeconomic Dynamics 17, 1281–1310.
* Commonwealth Treasury of Australia (2001)

  Commonwealth Treasury of Australia (2001),
  ‘Towards higher retirement incomes for australians: a history of the
  australian retirement income system since federation’, Economic Roundup
  pp. 65–92.
* Eslake (2024)

  Eslake, S. (2024), “Super for housing’ -
  will it help solve or exacerbate the housing affordability crisis?’, Corinna Economic Advisory repot .
* Favara (2015)

  Favara, G. (2015), ‘Credit supply and the
  price of housing’, American Economic Review 105, 958–992.
* Fetter (2013)

  Fetter, D. K. (2013), ‘How do mortgage
  subsidies affect home ownership? evidence from the mid-century GI bills’,
  American Economic Journal: Economic Policy 5, 111–147.
* Hand (2023)

  Hand, G. (2023), ‘10 reasons owning your home
  beats super in retirement’, Firtlinks, 5th April .
* Hilber and Turner (2014)

  Hilber, C. A. L. and Turner, T. M. (2014), ‘The mortgage interest deduction and its impact on
  homeownership’, Review of Economics and Statistics 96, 618–637.
* Khemka et al. (2021)

  Khemka, G., Tang, Y. and Warren, G. J. (2021), ‘The ‘right’ level for the superannuation
  guarantee: identifying the key considerations’, Accounting & Finance
  61(3), 4435–4474.
* Khemka et al. (2024)

  Khemka, G., Tang, Y. and Warren, G. J. (2024), ‘Cascade model for Australian housing’, Australian Economic Papers 63, 406–426.
* Krolage (2023)

  Krolage, C. (2023), ‘The effect of real
  estate purchase subsidies on property prices’, International Tax and
  Public Finance 30, 215–246.
* McCarthy et al. (2002)

  McCarthy, D., Mitchell, O. S. and Piggott, J. (2002), ‘Asset rich and cash poor: retirement provision and
  housing policy in singapore’, Journal of Pension Economics and Finance
  1, 197–222.
* Mercer CFA Institute (2025)

  Mercer CFA Institute (2025), ‘Mercer cfa
  institute global pension index’.
* Sodini et al. (2023)

  Sodini, P., Van Nieuwerburgh, S., Vestman, R. and von Lilienfeld-Toal,
  U. (2023), ‘Identifying the benefits from
  homeownership: A Swedish experiment’, American Economic Review 113, 3173–3212.
* Sommer and Sullivan (2018)

  Sommer, K. and Sullivan, P. (2018),
  ‘Implications of US tax policy for house prices, rents, and homeownership’,
  American Economic Review 108, 241–274.
* Super Members Council (2025)

  Super Members Council (2025), ‘Home truths:
  the KiwiSaver experience’, Super Members Council report .
* The Mckell Institute (2021)

  The Mckell Institute (2021), ‘Mortgaging
  our future: the effects of super for housing policies on Australian
  property prices and financial health in retirement’, Report of The
  Mckell Institute pp. 1–24.
* Vigdor (2006)

  Vigdor, J. L. (2006), ‘Liquidity constraints
  and housing prices: Theory and evidence from the VA mortgage program’, Journal of Public Economics 90, 1579–1600.
* Yates and Bradbury (2010)

  Yates, J. and Bradbury, B. (2010),
  ‘Home ownership as a (crumbling) fourth pillar of social insurance in
  australia’, Journal of Housing and the Built Environment 25, 193–211.

## Appendix A Appendix

### A.1 More details on tax rules

The property transfer tax τP​(t)\tau\_{P}(t) follows the rates applicable in the state of Victoria and is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τP​(t)={1.4%​P​(t),if ​P​(t)≤25,000,350+2.4%​(P​(t)−25,000),if ​25,000<P​(t)≤130,000,2,870+6%​(P​(t)−130,000),if ​130,000<P​(t)≤960,000,5.5%​P​(t),if ​960,000<P​(t)≤2,000,000,110,000+6.5%​(P​(t)−2,000,000),if ​P​(t)>2,000,000.\tau\_{P}\left(t\right)=\left\{\begin{array}[]{ll}1.4\%P(t),&\text{if }P(t)\leq 25,000,\\ 350+2.4\%\left(P(t)-25,000\right),&\text{if }25,000<P(t)\leq 130,000,\\ 2,870+6\%\left(P(t)-130,000\right),&\text{if }130,000<P(t)\leq 960,000,\\ 5.5\%P(t),&\text{if }960,000<P(t)\leq 2,000,000,\\ 110,000+6.5\%\left(P(t)-2,000,000\right),&\text{if }P(t)>2,000,000.\end{array}\right. |  | (A.1) |

In Australia, income tax applies to both gross salary and returns on savings, inherently linking the functions τI​(t)\tau\_{I}(t) and τA​(t)\tau\_{A}(t). The total income tax is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τS​(t)+τA​(t)={fincome tax​(S​(t)+rA​(t−1)​A​(t−1)),for ​t<Tr,fincome tax​(rA​(t−1)​A​(t−1)),for ​t≥Tr,\tau\_{S}(t)+\tau\_{A}(t)=\left\{\begin{array}[]{ll}f\_{\text{income tax}}\left(S(t)+r\_{A}(t-1)A(t-1)\right),&\text{for }t<T\_{r},\\ f\_{\text{income tax}}\left(r\_{A}(t-1)A(t-1)\right),&\text{for }t\geq T\_{r},\end{array}\right. |  | (A.2) |

which reflects the fact that taxable income after retirement comes from investment returns only.

Since income tax is assessed annually, but this study operates on a quarterly basis, tax thresholds in the function fincome taxf\_{\text{income tax}} are divided by four:

|  |  |  |
| --- | --- | --- |
|  | fincome tax​(x)={0,if ​x≤18,2004,0.16×(x−18,2004),if ​18,2004<x≤45,0004,4,2884+0.30×(x−45,0004),if ​45,0004<x≤135,0004,31,2884+0.37×(x−135,0004),if ​135,0004<x≤190,0004,51,6384+0.45×(x−190,0004),if ​x>190,0004.f\_{\text{income tax}}(x)=\left\{\begin{array}[]{ll}0,&\text{if }x\leq\frac{18,200}{4},\\ 0.16\times\left(x-\frac{18,200}{4}\right),&\text{if }\frac{18,200}{4}<x\leq\frac{45,000}{4},\\ \frac{4,288}{4}+0.30\times\left(x-\frac{45,000}{4}\right),&\text{if }\frac{45,000}{4}<x\leq\frac{135,000}{4},\\ \frac{31,288}{4}+0.37\times\left(x-\frac{135,000}{4}\right),&\text{if }\frac{135,000}{4}<x\leq\frac{190,000}{4},\\ \frac{51,638}{4}+0.45\times\left(x-\frac{190,000}{4}\right),&\text{if }x>\frac{190,000}{4}.\end{array}\right. |  |

For identification purposes, τS​(t)\tau\_{S}(t) is set to fincome tax​(S​(t))f\_{\text{income tax}}(S(t)), and τA​(t)\tau\_{A}(t) is obtained from equation ([A.2](https://arxiv.org/html/2511.01133v1#A1.E2 "In A.1 More details on tax rules ‣ Appendix A Appendix ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit")). Note that income tax thresholds are not indexed in Australia.

The tax rate on superannuation returns is 15% before retirement and 0% after retirement. Thus:

|  |  |  |
| --- | --- | --- |
|  | τF​(t)={15%​rF​(t)​F​(t−1),if ​t<Tr,0,if ​t≥Tr.\tau\_{F}(t)=\left\{\begin{array}[]{ll}15\%r\_{F}(t)F(t-1),&\text{if }t<T\_{r},\\ 0,&\text{if }t\geq T\_{r}.\end{array}\right. |  |

Finally, the superannuation contribution tax rate is set at 15%15\%, but the Low Income Super Tax Offset refund applies for yearly incomes below 37,000. Thus, the function τγ​(t)\tau\_{\gamma}(t) is equal to 0 for S​(t)≤37,0004S(t)\leq\frac{37,000}{4}, and to 15% otherwise.

### A.2 More details on pension rules

During the accumulation phase, the only superannuation contributions considered are employer’s mandatory contributions, fixed at rate γ\gamma. Voluntary contributions are excluded. The employer’s compulsory contribution, known as the superannuation guarantee, is γ=12%\gamma=12\%, consistent with the recent update in July 2025.

During the decumulation phase, pension withdrawals B​(t)B(t) are at the household’s discretion. For simplicity, it is assumed that households withdraw the minimum required amount set by the government, given by:

|  |  |  |
| --- | --- | --- |
|  | B​(t)={0, for ​t<Tr,b​(t)​Fa​c​c​(t), for ​t≥Tr,B(t)=\left\{\begin{array}[]{ll}0,&\text{ for }t<T\_{r},\\ b(t)F\_{acc}(t),&\text{ for }t\geq T\_{r},\end{array}\right. |  |

where the function b​(t)b(t) corresponds to the ATO’s minimum drawdown rates, adjusted to quarterly frequency:

|  |  |  |
| --- | --- | --- |
|  | b​(t)={54%, for ​168≤t≤199,64%, for ​200≤t≤219,74%, for ​220≤t≤239,94%, for ​240≤t≤259,114%, for ​t≥260.b(t)=\left\{\begin{array}[]{ll}\frac{5}{4}\%,&\text{ for }168\leq t\leq 199,\\ \frac{6}{4}\%,&\text{ for }200\leq t\leq 219,\\ \frac{7}{4}\%,&\text{ for }220\leq t\leq 239,\\ \frac{9}{4}\%,&\text{ for }240\leq t\leq 259,\\ \frac{11}{4}\%,&\text{ for }t\geq 260.\end{array}\right. |  |

For households with insufficient assets and income, the government provides a pension income G​(t)G(t), known as the Age Pension. It includes three components: the basic age pension Gb​a​s​e​(t)G\_{base}(t), pension supplements Gs​u​p​p​(t)G\_{supp}(t), and rental assistance Gr​e​n​t​(t)G\_{rent}(t) for non-homeowners. Eligibility and benefit amounts are determined by income and asset tests, with thresholds based on homeownership status and household composition (single vs. couple). Notably, a positive base age pension is required for pension supplements and rental assistance. Further details on the Australian age pension can be found in Cho and Sane ([2013](https://arxiv.org/html/2511.01133v1#bib.bib11)) and Andréasson and Shevchenko ([2024](https://arxiv.org/html/2511.01133v1#bib.bib4)).

The total guaranteed pension benefit is given by:

|  |  |  |
| --- | --- | --- |
|  | G​(t)={0,for ​t<Tr,Gb​a​s​e​(t)+Gs​u​p​p​(t)+Gr​e​n​t​(t),for ​t≥Tr, for non-home owners, provided ​Gb​a​s​e​(t)>0,Gb​a​s​e​(t)+Gs​u​p​p​(t),for ​t≥Tr, for home owners, provided ​Gb​a​s​e​(t)>0,G(t)=\left\{\begin{array}[]{ll}0,&\text{for }t<T\_{r},\\ G\_{base}(t)+G\_{supp}(t)+G\_{rent}(t),&\text{for }t\geq T\_{r},\text{ for non-home owners, provided }G\_{base}(t)>0,\\ G\_{base}(t)+G\_{supp}(t),&\text{for }t\geq T\_{r},\text{ for home owners, provided }G\_{base}(t)>0,\\ \end{array}\right. |  |

The three components Gb​a​s​e​(t)G\_{base}(t), Gs​u​p​p​(t)G\_{supp}(t) and Gr​e​n​t​(t)G\_{rent}(t) are the basic age pension, the supplements and rental assistance, respectively. They are given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gb​a​s​e​(t)\displaystyle G\_{base}(t) | =\displaystyle= | 6.5×min⁡{Gb​a​s​emax,Ga​s​s​e​t​(t),Gi​n​c​o​m​e​(t)},\displaystyle 6.5\times\min\{G^{\max}\_{base},G\_{asset}(t),G\_{income}(t)\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gs​u​p​p​(t)\displaystyle G\_{supp}(t) | =\displaystyle= | 6.5×max⁡{GSmin​(t),Gb​a​s​e​(t)GBmax​(t)​GSmax​(t)},\displaystyle 6.5\times\max\left\{G^{\min}\_{S}(t),\frac{G\_{base}(t)}{G^{\max}\_{B}(t)}G^{\max}\_{S}(t)\right\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gr​e​n​t​(t)\displaystyle G\_{rent}(t) | =\displaystyle= | 6.5×min⁡{max⁡{0,ωR×(R​(t)−Rmin​(t))},Rmax​(t)},\displaystyle 6.5\times\min\left\{\max\left\{0,\omega\_{R}\times(R(t)-R^{\min}(t))\right\},R^{\max}(t)\right\}, |  |

where the multiplication by 6.5 reflects quarterly payments, as all thresholds are given on a fortnightly basis. The functions Ga​s​s​e​t​(t)G\_{asset}(t) and Gi​n​c​o​m​e​(t)G\_{income}(t) are the asset and income tests determining the fortnightly pension reduction, and are defined as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ga​s​s​e​t​(t)\displaystyle G\_{asset}(t) | =\displaystyle= | max⁡{0,GBmax​(t)−ωA×(Aa​c​c​(t)+Fa​c​c​(t)−WA∗​(t))},\displaystyle\max\left\{0,G^{\max}\_{B}(t)-\omega\_{A}\times\left(A\_{acc}(t)+F\_{acc}(t)-W^{\*}\_{A}(t)\right)\right\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gi​n​c​o​m​e​(t)\displaystyle G\_{income}(t) | =\displaystyle= | max⁡{0,GBmax​(t)−ωI×(Ia​s​s​e​s​s​e​d​(t)−WI∗​(t))},\displaystyle\max\left\{0,G^{\max}\_{B}(t)-\omega\_{I}\times\left(I\_{assessed}(t)-W^{\*}\_{I}(t)\right)\right\}, |  |

where assessed income Ia​s​s​e​s​s​e​d​(t)I\_{assessed}(t) is given by:

|  |  |  |
| --- | --- | --- |
|  | Ia​s​s​e​s​s​e​d​(t)=ζ1​min⁡{Aa​c​c​(t)+Fa​c​c​(t),WD∗​(t)}+ζ2​max⁡{0,Aa​c​c​(t)+Fa​c​c​(t)−WD∗​(t)}.I\_{assessed}(t)=\zeta\_{1}\min\{A\_{acc}(t)+F\_{acc}(t),W^{\*}\_{D}(t)\}+\zeta\_{2}\max\{0,A\_{acc}(t)+F\_{acc}(t)-W^{\*}\_{D}(t)\}. |  |

The functions GBmax​(t)G^{\max}\_{B}(t), WA∗​(t)W^{\*}\_{A}(t), WI∗​(t)W^{\*}\_{I}(t), WD∗​(t)W^{\*}\_{D}(t), GSmin​(t)G^{\min}\_{S}(t), GSmax​(t)G^{\max}\_{S}(t), Rmin​(t)R^{\min}(t) and Rmax​(t)R^{\max}(t) are the thresholds that depend on household composition (single vs. couple), with WA∗​(t)W^{\*}\_{A}(t) also depend on homeownership status. Their initial values, along with the rates ωa​s​s​e​t\omega\_{asset}, ωi​n​c​o​m​e\omega\_{income}, ωr​e​n​t\omega\_{rent}, ζ1\zeta\_{1} and ζ2\zeta\_{2}, are provided in Table [3](https://arxiv.org/html/2511.01133v1#A1.T3 "Table 3 ‣ A.2 More details on pension rules ‣ Appendix A Appendix ‣ Liquidity Shocks, Homeownership, and Income Inequality: Impact of Early Pension Withdrawals and Reduced Deposit"), and the time-tt values are the inflation-adjusted time-0 values.

| Notation | Singles | Couples |
| --- | --- | --- |
| GBmax​(0)G^{\max}\_{B}(0) | 1,051.31,051.3 | 1,5851,585 |
| WA∗​(0)W^{\*}\_{A}(0) (non-homeowners) | 566,000566,000 | 722,000722,000 |
| WA∗​(0)W^{\*}\_{A}(0) (homeowners) | 314,000314,000 | 470,000470,000 |
| WI∗​(0)W^{\*}\_{I}(0) | 212212 | 372372 |
| WD∗​(0)W^{\*}\_{D}(0) | 62,60062,600 | 103,800103,800 |
| GSmin​(0)G^{\min}\_{S}(0) | 59.159.1 | 8989 |
| GSmax​(0)G^{\max}\_{S}(0) | 97.797.7 | 147.2147.2 |
| Rmin​(0)R^{\min}(0) | 149.6149.6 | 242.4242.4 |
| Rmax​(0)R^{\max}(0) | 432.27432.27 | 508.8508.8 |
| ωI\omega\_{I} | 50%50\% | 25%25\% |
| ωA\omega\_{A} | 0.3%0.3\% | |
| ωR\omega\_{R} | 75%75\% | |
| ζ1\zeta\_{1} | 0.25%0.25\% | |
| ζ2\zeta\_{2} | 2.25%2.25\% | |

Table 3: Thresholds and rates used to determine the guaranteed pension income G​(t)G(t).  The top panel provides the thresholds, and the bottom panel provides the rates. All numerical values were obtained from the Australian Tax Office’s website; see the main text for details. We note that all of the above values, in the top panel, are indexed by CPI.