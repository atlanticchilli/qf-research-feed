---
authors:
- Ricardo Alonzo Fernández Salguero
doc_id: arxiv:2510.16537v1
family_id: arxiv:2510.16537
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Crisis Simulator for Bolivia (KISr-p): An Empirically Grounded Modeling
  Framework'
url_abs: http://arxiv.org/abs/2510.16537v1
url_html: https://arxiv.org/html/2510.16537v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ricardo Alonzo Fernández Salguero

(October 18, 2025)

###### Abstract

\justify

This document presents a detailed technical report of the “Crisis Simulator for Bolivia (KISr-p),” a quarterly stochastic model designed to evaluate the impact of various macroeconomic policy strategies in an environment of high uncertainty and structural constraints. Unlike standard general equilibrium frameworks, this simulator is grounded in the consolidated empirical findings from a vast collection of meta-analyses, adopting a theoretical architecture of a Keynesian Intertemporal Synthesis (KIS) with a Constant Elasticity of Substitution (KIS-CES) production function. The calibration of each model block—real, fiscal, monetary, external, labor, and distributional—is described, justifying key parameters with quantitative evidence on the hierarchy of fiscal multipliers (Gechert and Rannenberg, [2018](https://arxiv.org/html/2510.16537v1#bib.bib107)), the complementarity of production factors (Gechert et al., [2022](https://arxiv.org/html/2510.16537v1#bib.bib105)), monopsony power in the labor market (Sokolova and Sorensen, [2021](https://arxiv.org/html/2510.16537v1#bib.bib216)), and the dynamics of exchange rate and interest rate pass-through. It is demonstrated how the model integrates these regularities to generate non-linear dynamics, such as the dependence of multipliers on the state of the business cycle and the asymmetric impact of shocks. The results of a set of simulated policy scenarios are presented, illustrating the trade-offs between fiscal adjustment, external financing, debt restructuring, and structural reforms, such as the aggressive restructuring of spending. The analysis concludes that a pragmatic policy approach, which prioritizes the composition of spending over its aggregate level and recognizes institutional frictions, offers superior macroeconomic and welfare outcomes compared to dogmatic solutions.

## 1 Introduction

Contemporary macroeconomics is at a crossroads, marked by a proliferation of empirical results that are often contradictory and context-dependent. This “cacophony of results,” as described by Doucouliagos and Stanley ([2013](https://arxiv.org/html/2510.16537v1#bib.bib66)), has hindered the formulation of economic policies based on a robust consensus, allowing debates to persist on an ideological plane. Economic liberalism, popularized through frameworks like the Washington Consensus, has traditionally advocated for deregulation, privatization, and market flexibility as paths to prosperity (De Haan et al., [2006](https://arxiv.org/html/2510.16537v1#bib.bib60); Fernández Salguero, [2025a](https://arxiv.org/html/2510.16537v1#bib.bib79)). However, aggregated evidence, once purged of publication bias and methodological heterogeneity, often challenges these dogmas, revealing a world with significant frictions, market power, and a crucial role for the state and institutions (Fernández Salguero, [2025g](https://arxiv.org/html/2510.16537v1#bib.bib85)).

Faced with this challenge, quantitative synthesis through meta-analysis has established itself as an indispensable tool for distilling robust signals from empirical noise (Stanley, [2001](https://arxiv.org/html/2510.16537v1#bib.bib220); Irsova et al., [2024](https://arxiv.org/html/2510.16537v1#bib.bib131)). By systematically analyzing thousands of estimates from primary studies, meta-analyses have revealed empirical regularities that demand a recalibration of our theoretical frameworks. Findings such as the superiority of investment spending multipliers in recessions (Gechert and Rannenberg, [2018](https://arxiv.org/html/2510.16537v1#bib.bib107)), the null effect of the minimum wage on employment due to monopsony power (Doucouliagos and Stanley, [2009](https://arxiv.org/html/2510.16537v1#bib.bib65); Sokolova and Sorensen, [2021](https://arxiv.org/html/2510.16537v1#bib.bib216); Fernández Salguero, [2025c](https://arxiv.org/html/2510.16537v1#bib.bib81)), and the elasticity of substitution between capital and labor consistently below unity (Gechert et al., [2022](https://arxiv.org/html/2510.16537v1#bib.bib105)), are not anomalies but structural features of modern economies.

This document presents the “Crisis Simulator for Bolivia (KISr-p),” a macroeconomic policy laboratory that takes this aggregated evidence as its foundation. Instead of starting from pure theoretical axioms, the simulator adopts the Keynesian Intertemporal Synthesis with CES production (KIS-CES) framework, a structure that reconciles intertemporal optimization with Keynesian frictions, and calibrates it directly with the consolidated parameters from the meta-analysis literature (Fernández Salguero, [2025h](https://arxiv.org/html/2510.16537v1#bib.bib86)). The objective is to build a bridge between the vast empirical evidence and the practical modeling of policies, offering a tool to analyze complex scenarios in a small, open economy subject to external shocks and structural constraints, as is the case of Bolivia (Fernández Salguero, [2025d](https://arxiv.org/html/2510.16537v1#bib.bib82), [e](https://arxiv.org/html/2510.16537v1#bib.bib83)).

The analysis was executed with the Bolivia Crisis Simulator KISr-p (Fernández Salguero, [2025](https://arxiv.org/html/2510.16537v1#bib.bib78)), available on [GitHub/RAFS20](https://github.com/RAFS20/Bolivia-Crisis-Simulator-KISr-p/tree/main).

## 2 Simulator Architecture and Methodology

The “Crisis Simulator for Bolivia (KISr-p)” is a macroeconomic policy laboratory that operates as a stochastic quarterly time-series model. Its purpose is not point forecasting, but the comparative risk analysis of different strategies over a medium-term horizon (40 quarters). The core methodology is simulation, where for each scenario, hundreds of possible trajectories (N\_PATHS) are generated, each subject to a different sequence of random shocks, allowing for the construction of distributions of future outcomes.

The model is not a computable general equilibrium (CGE) system but a recursive structural model with path-dependence. The state variables in a quarter t (debt, reserves, exchange rate gap) determine the conditions for quarter t+1, influencing multipliers and risk premia. This structure captures crucial non-linear dynamics, such as tipping points where a fall in reserves can trigger a currency crisis, or where an increase in debt can lead to a spiral of higher risk premia. The architecture is organized into interconnected blocks:

1. 1.

   Real and Fiscal Block: Determines GDP through an aggregate demand equation that incorporates the effects of fiscal policy (current spending, investment, transfers), global shocks, and the impact of monetary policy. The calibration of fiscal multipliers is state-dependent (boom, recession, crisis), reflecting the evidence from Gechert and Rannenberg ([2018](https://arxiv.org/html/2510.16537v1#bib.bib107)). The fiscal side is closed with an endogenously counter-cyclical primary balance rule and a revenue function sensitive to the business cycle and inflation.
2. 2.

   Prices, Monetary, and External Block: Models inflation with components of inertia, the output gap, and a pass-through channel from the parallel exchange rate, the magnitude of which is non-linear and dependent on reserves (Iorngurum, [2025a](https://arxiv.org/html/2510.16537v1#bib.bib129)). Monetary policy follows a Taylor rule, but its effect on the real economy is modest, consistent with the corrected evidence of Fernández Salguero ([2025i](https://arxiv.org/html/2510.16537v1#bib.bib87)). The external sector is modeled through a simplified balance of payments, where the capital account responds to the sovereign risk premium.
3. 3.

   Debt and Risk Block: The debt/GDP dynamic evolves according to the deficit, financial cost, and growth. The sovereign risk premium is a key variable, modeled endogenously as a non-linear function of debt, reserves, the exchange rate gap, and political instability, drawing lessons from the literature on debt crises and austerity (Fernández Salguero, [2025k](https://arxiv.org/html/2510.16537v1#bib.bib89)).
4. 4.

   Labor, Distributional, and Welfare Block: Includes a labor market with monopsony power, consistent with Sokolova and Sorensen ([2021](https://arxiv.org/html/2510.16537v1#bib.bib216)) and Fernández Salguero ([2025j](https://arxiv.org/html/2510.16537v1#bib.bib88)). This allows social policies (TR) to affect not only demand but also inequality (Gini) and a proxy for human capital/health. A synthetic welfare index is calculated for ranking scenarios.

This modular design allows for the simulation of a wide range of policies, from traditional spending cuts to reforms such as the implementation of a land value tax (LVT), whose feasibility is analyzed in Fernández Salguero ([2025b](https://arxiv.org/html/2510.16537v1#bib.bib80)), or the interaction with multilateral organization programs, whose impacts are a matter of debate (Fernández Salguero, [2025f](https://arxiv.org/html/2510.16537v1#bib.bib84)).

## 3 Foundations of the Real and Fiscal Block

The core of the simulator lies in its fiscal block, designed to capture the most robust empirical regularities on the effectiveness of spending and taxes. Neoclassical theory traditionally posits that tax cuts are more effective than spending and that public spending crowds out private investment. The aggregated evidence, however, tells a different story.

The meta-analysis by Gechert ([2015](https://arxiv.org/html/2510.16537v1#bib.bib102)) is fundamental to the model’s calibration. It finds that public spending multipliers are systematically larger than those for tax cuts (a difference of 0.3-0.4 points) and establishes a clear hierarchy: the multiplier for public investment (infrastructure, R&D) is approximately 0.5 points higher than that for current spending. This is because investment increases long-term productive capacity, an effect corroborated by Bom and Ligthart ([2014](https://arxiv.org/html/2510.16537v1#bib.bib33)). The analysis for Bolivia by Fernández Salguero ([2025d](https://arxiv.org/html/2510.16537v1#bib.bib82)) confirms this hierarchy, showing a strong crowding-in effect of infrastructure investment. The simulator implements this evidence by distinguishing between Current Spending (GC), Public Investment (GI), and Transfers (TR), with multipliers that respect the relationship mG​I>mT​R>mG​Cm\_{GI}>m\_{TR}>m\_{GC}.

The most influential finding post-2008 crisis is the business cycle dependency of fiscal effectiveness. The meta-analysis by Gechert and Rannenberg ([2018](https://arxiv.org/html/2510.16537v1#bib.bib107)) demonstrates that multipliers are significantly more potent in recessions (increasing by 0.7 to 0.9 points). The simulator captures this non-linearity through a regime-switching mechanism. In each quarter, the economy is classified as “Boom,” “Recession,” or “Crisis” based on the output gap and reserves. Depending on the regime, multipliers are drawn from a different distribution, being highest in a “Crisis.” This implies that the same austerity policy can have a devastating effect in a recession, a central result in the critique of such policies (Fernández Salguero, [2025k](https://arxiv.org/html/2510.16537v1#bib.bib89)). Table [1](https://arxiv.org/html/2510.16537v1#S3.T1 "Table 1 ‣ 3 Foundations of the Real and Fiscal Block ‣ The Crisis Simulator for Bolivia (KISr-p): An Empirically Grounded Modeling Framework") summarizes the base calibration.

Table 1: Calibration of Mean Quarterly Fiscal Multipliers by Regime

| Type of Spending | Boom | Recession | Crisis |
| --- | --- | --- | --- |
| Current Spending (GC) | 0.045 | 0.125 | 0.213 |
| Transfers (TR) | 0.075 | 0.200 | 0.263 |
| Public Investment (GI) | 0.175 | 0.388 | 0.525 |

\justify

Note: The values represent the mean quarterly impact of a fiscal impulse of 1% of GDP. The calibration follows the hierarchy and cycle dependency from Gechert ([2015](https://arxiv.org/html/2510.16537v1#bib.bib102)) and Gechert and Rannenberg ([2018](https://arxiv.org/html/2510.16537v1#bib.bib107)). The values are drawn from a t-Student distribution in each simulation.

## 4 Monetary, Exchange Rate, and External Sector Block

In a small, open economy like Bolivia, the monetary and external channels are crucial. The simulator models them with a pragmatic approach, anchored in the evidence that the power of conventional monetary policy is limited. The meta-analysis by Fernández Salguero ([2025i](https://arxiv.org/html/2510.16537v1#bib.bib87)), which reviews a vast literature, finds a publication bias that exaggerates the effects of monetary policy. Once corrected, the peak impact of a 100 bps interest rate shock on output is reduced from -1.0% to a modest -0.25%. Consequently, the simulator incorporates a transmission channel from the interest rate to aggregate demand that is deliberately weak.

The exchange rate channel is, in practice, more relevant. The model distinguishes between an official exchange rate (S\_off) and a parallel one (S\_par), generating an endogenous gap. The dynamics of the gap respond to balance of payments pressures (reflected in the level of reserves), the risk premium, and social unrest. Inflation, in turn, is sensitive to movements in the parallel exchange rate through a non-linear pass-through mechanism: the pass-through is greater when reserves are low, capturing the erosion of credibility. The evidence from Iorngurum ([2025a](https://arxiv.org/html/2510.16537v1#bib.bib129)) and Velickovski and Pugh ([2011](https://arxiv.org/html/2510.16537v1#bib.bib241)) on incomplete and asymmetric pass-through justifies this modeling.

The external sector is modeled with a simplified balance of payments. The current account (CA) responds to the real exchange rate and the business cycle, and the capital account (KA) to the risk premium. The change in reserves (Res) is the net result. A crucial element is the critical reserve threshold (RES\_CRIT). If reserves fall below this level, a “Crisis” regime is triggered, raising multipliers and risk, and increasing the probability of an exchange rate realignment. This mechanism is consistent with the literature on financial crises (Fernández Salguero, [2025k](https://arxiv.org/html/2510.16537v1#bib.bib89)). Table [2](https://arxiv.org/html/2510.16537v1#S4.T2 "Table 2 ‣ 4 Monetary, Exchange Rate, and External Sector Block ‣ The Crisis Simulator for Bolivia (KISr-p): An Empirically Grounded Modeling Framework") summarizes the main channels.

Table 2: Main Transmission Channels of the Monetary and External Block

| Channel | Mechanism and Empirical Justification |
| --- | --- |
| Interest Rate | An increase in the policy rate has a small contractionary effect on GDP and inflation. Transmission is attenuated by dollarization and the exchange rate gap. Calibration based on Fernández Salguero ([2025i](https://arxiv.org/html/2510.16537v1#bib.bib87)). |
| Exchange Rate Pass-through | Inflation responds to changes in the parallel exchange rate. The pass-through coefficient (ϕt\phi\_{t}) is non-linear: it increases as reserves fall below a critical threshold. Consistent with Iorngurum ([2025a](https://arxiv.org/html/2510.16537v1#bib.bib129)). |
| Sovereign Risk Premium | The spread (RP) is endogenous. It increases with debt/GDP and the gap; it decreases with reserves and institutional quality. This generates a feedback loop, as documented in Fernández Salguero ([2025k](https://arxiv.org/html/2510.16537v1#bib.bib89)). |
| Capital Account | Capital flows are volatile and pro-cyclical. They respond negatively to the risk premium (capital flight) and social unrest. Policies like temporary capital flow management (CFM) can moderate this volatility. |

## 5 Labor Market, Inequality, and Welfare

The KIS-CES simulator incorporates frictions and market power in the labor block, following the evidence from meta-analyses. The finding of a practically null effect of the minimum wage on employment (Doucouliagos and Stanley, [2009](https://arxiv.org/html/2510.16537v1#bib.bib65); Fernández Salguero, [2025c](https://arxiv.org/html/2510.16537v1#bib.bib81)) is consistent with a market with monopsony power, a widespread characteristic according to Sokolova and Sorensen ([2021](https://arxiv.org/html/2510.16537v1#bib.bib216)). The model implements a “monopsony-lite” version, where employment (Emp) co-evolves from demand and supply functions, allowing fiscal shocks to have a direct impact on employment, in line with the theoretical framework of Fernández Salguero ([2025j](https://arxiv.org/html/2510.16537v1#bib.bib88)).

The model also tracks distributional and social variables. Inequality (Gini) evolves in response to unemployment and fiscal progressivity. Social transfers (TR) reduce the Gini coefficient. In turn, inequality has feedback effects: the meta-analyses of Capretti and Tonni ([2025](https://arxiv.org/html/2510.16537v1#bib.bib41)) and Cipollina et al. ([2018](https://arxiv.org/html/2510.16537v1#bib.bib50)) find a negative relationship between inequality and growth. In the simulator, a higher Gini increases social unrest (Unrest) and reduces potential growth through its impact on human capital/health (Health).

The health/human capital index (Health) improves with employment and social investment, and deteriorates with inequality. This captures the findings of meta-analyses such as those by Kondo et al. ([2009](https://arxiv.org/html/2510.16537v1#bib.bib147)) and Shimonovich et al. ([2024](https://arxiv.org/html/2510.16537v1#bib.bib213)), which document a robust negative association between inequality and health. The inclusion of these variables allows for a more holistic evaluation of policies. The final welfare index aggregates these dimensions to provide a comparative ranking, as summarized in Table [3](https://arxiv.org/html/2510.16537v1#S5.T3 "Table 3 ‣ 5 Labor Market, Inequality, and Welfare ‣ The Crisis Simulator for Bolivia (KISr-p): An Empirically Grounded Modeling Framework").

Table 3: Components of the Synthetic Welfare Index

| Component | Weight | Justification and Link to Literature |
| --- | --- | --- |
| GDP Level | +0.30 | Proxy for aggregate income and consumption. |
| Employment Level | +0.15 | Captures the labor dimension of welfare. |
| Health Index | +0.10 | Represents human capital. Its link to inequality is based on Kondo et al. ([2009](https://arxiv.org/html/2510.16537v1#bib.bib147)). |
| Inflation | -0.15 | High inflation erodes purchasing power. |
| Debt/GDP | -0.10 | High debt implies vulnerability. |
| Exchange Rate Gap | -0.08 | Signal of imbalances and distortions. |
| Social Unrest | -0.07 | Proxy for political instability. |
| Gini Coefficient | -0.05 | Inequality has direct social costs. |

## 6 Mathematical Formalization of the Stochastic Model

The model simulates the trajectory of a small, open economy with external constraints and a dual exchange rate market. It is formulated in discrete time, with a period tt representing a quarter. The system is defined by a state vector that evolves stochastically over a time horizon of T=40T=40 quarters. The structural blocks that govern the model’s dynamics are detailed below. Table LABEL:tab:variables presents a summary of the main notation.

### 6.1 Real Sector: Output Dynamics and its Determinants

Aggregate output, YtY\_{t}, evolves as a function of fiscal policy, external shocks, and the endogenous dynamics of the system. The output gap, gtg\_{t}, is defined as the percentage deviation of observed output from its potential level, YtPY\_{t}^{P}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gt=Yt−YtPYtPg\_{t}=\frac{Y\_{t}-Y\_{t}^{P}}{Y\_{t}^{P}} |  | (1) |

The economy’s behavior is classified into one of three regimes, ℛt∈{Boom, Recession, Crisis}\mathcal{R}\_{t}\in\{\text{Boom, Recession, Crisis}\}, determined by the output gap and the level of international reserves, RtR\_{t}, relative to a critical threshold Rc​r​i​tR\_{crit}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛt={Crisisif ​(Rt≤Rc​r​i​t)∨(ℬt>ℬc​r​i​s​i​s)Recessionif ​(gt<0)∧(ℛt≠Crisis)Boomif ​(gt≥0)∧(ℛt≠Crisis)\mathcal{R}\_{t}=\begin{cases}\text{Crisis}&\text{if }(R\_{t}\leq R\_{crit})\lor(\mathcal{B}\_{t}>\mathcal{B}\_{crisis})\\ \text{Recession}&\text{if }(g\_{t}<0)\land(\mathcal{R}\_{t}\neq\text{Crisis})\\ \text{Boom}&\text{if }(g\_{t}\geq 0)\land(\mathcal{R}\_{t}\neq\text{Crisis})\end{cases} |  | (2) |

where ℬt=Stp​a​r/Sto​f​f\mathcal{B}\_{t}=S\_{t}^{par}/S\_{t}^{off} is the exchange rate gap.

The real output growth rate, Δ​ln⁡Yt+1\Delta\ln Y\_{t+1}, responds to fiscal impulses, shocks, and the monetary policy channel:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ln⁡Yt+1=−μtG​C​Δ​GtC+μtG​I​Δ​GtI+μtT​R​Δ​TtR+zt+mt+ϵtd\Delta\ln Y\_{t+1}=-\mu\_{t}^{GC}\Delta G\_{t}^{C}+\mu\_{t}^{GI}\Delta G\_{t}^{I}+\mu\_{t}^{TR}\Delta T\_{t}^{R}+z\_{t}+m\_{t}+\epsilon\_{t}^{d} |  | (3) |

where Δ​GtC\Delta G\_{t}^{C}, Δ​GtI\Delta G\_{t}^{I}, and Δ​TtR\Delta T\_{t}^{R} represent changes in current spending, public investment, and transfers as a proportion of GDP. The fiscal multipliers, μt(⋅)\mu\_{t}^{(\cdot)}, are stochastic and depend on the economic regime ℛt\mathcal{R}\_{t}, following a theoretical hierarchy where μtG​I>μtT​R>μtG​C\mu\_{t}^{GI}>\mu\_{t}^{TR}>\mu\_{t}^{GC} Gechert ([2015](https://arxiv.org/html/2510.16537v1#bib.bib102)); Alarcon Gambarte ([2020](https://arxiv.org/html/2510.16537v1#bib.bib4)). The magnitude of the multipliers increases significantly during recessions and crises, in line with empirical evidence highlighting the greater effectiveness of fiscal stimulus when there are idle resources Blanchard and Leigh ([2013](https://arxiv.org/html/2510.16537v1#bib.bib29)); Christiano et al. ([2011](https://arxiv.org/html/2510.16537v1#bib.bib48)); Gechert and Rannenberg ([2018](https://arxiv.org/html/2510.16537v1#bib.bib107)). The term ztz\_{t} is an autoregressive global shock, mtm\_{t} captures the modest impact of the interest rate channel, and ϵtd\epsilon\_{t}^{d} is an idiosyncratic demand shock with fat tails, distributed according to a t-Student.

Potential output, YtPY\_{t}^{P}, evolves at a base rate, gPg^{P}, but is adjusted by public capital accumulation, KtPK\_{t}^{P}, and by distributional factors. Public capital accumulation follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt+1P=(1−δp)​KtP+GtI​YtK\_{t+1}^{P}=(1-\delta\_{p})K\_{t}^{P}+G\_{t}^{I}Y\_{t} |  | (4) |

where δp\delta\_{p} is the quarterly depreciation rate. The dynamics of potential output are expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ln⁡Yt+1P=gP+αp​Δ​Kt+1PYt+βg​i​n​i​(G​i​n​it−G​i​n​i¯)\Delta\ln Y\_{t+1}^{P}=g^{P}+\alpha\_{p}\frac{\Delta K\_{t+1}^{P}}{Y\_{t}}+\beta\_{gini}(Gini\_{t}-\overline{Gini}) |  | (5) |

where αp\alpha\_{p} is the marginal productivity of public capital Bom and Ligthart ([2014](https://arxiv.org/html/2510.16537v1#bib.bib33)) and the last term introduces a channel through which higher income inequality (G​i​n​itGini\_{t}) can erode long-term growth Capretti and Tonni ([2025](https://arxiv.org/html/2510.16537v1#bib.bib41)); Cipollina et al. ([2018](https://arxiv.org/html/2510.16537v1#bib.bib50)).

### 6.2 Prices and Inflation

Quarterly inflation, πt\pi\_{t}, follows a process that combines inertia, a Phillips curve, an exchange rate pass-through channel, and an anchor to the inflation target, π∗\pi^{\*}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt=ρπ​πt−1+κ​gt+ϕ​(Rt)​Δ​ln⁡Stp​a​r+(1−ρπ)​(π∗)+ϵtπ\pi\_{t}=\rho\_{\pi}\pi\_{t-1}+\kappa g\_{t}+\phi(R\_{t})\Delta\ln S\_{t}^{par}+(1-\rho\_{\pi})(\pi^{\*})+\epsilon\_{t}^{\pi} |  | (6) |

The pass-through from the parallel exchange rate, Δ​ln⁡Stp​a​r\Delta\ln S\_{t}^{par}, to prices is non-linear, mediated by the function ϕ​(Rt)\phi(R\_{t}), which increases as liquid reserves, RtR\_{t}, fall below the critical threshold Rc​r​i​tR\_{crit}. This non-linearity captures the de-anchoring of inflation expectations in contexts of foreign currency scarcity Iorngurum ([2025a](https://arxiv.org/html/2510.16537v1#bib.bib129)); Velickovski and Pugh ([2011](https://arxiv.org/html/2510.16537v1#bib.bib241)). The pass-through function has a logistic form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(Rt)=ϕ¯1+exp⁡(kϕ​(RtRc​r​i​t−1))\phi(R\_{t})=\frac{\bar{\phi}}{1+\exp\left(k\_{\phi}\left(\frac{R\_{t}}{R\_{crit}}-1\right)\right)} |  | (7) |

where ϕ¯\bar{\phi} is the maximum pass-through and kϕk\_{\phi} modulates its sensitivity to reserve scarcity.

### 6.3 Public Finances and Fiscal Rule

Public revenues as a fraction of GDP, τt\tau\_{t}, are endogenous and depend on economic activity, inflation, and institutional credibility, C​r​e​dtCred\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τt=τ¯+βg​gt+βπ​πt+βc​r​e​d​(C​r​e​dt−C​r​e​d¯)\tau\_{t}=\bar{\tau}+\beta\_{g}g\_{t}+\beta\_{\pi}\pi\_{t}+\beta\_{cred}(Cred\_{t}-\overline{Cred}) |  | (8) |

The primary balance target, p​dt∗pd\_{t}^{\*}, follows a convergence path from an initial deficit to a medium-term surplus, p​dt​a​r​g​e​tpd\_{target}. Additionally, it incorporates a counter-cyclical fiscal rule that seeks to stabilize debt dynamics Heimberger ([2023b](https://arxiv.org/html/2510.16537v1#bib.bib121)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​dt∗=(1−at)​p​d0+at​p​dt​a​r​g​e​t−γ​(rte​f​f−g^t)​btpd\_{t}^{\*}=(1-a\_{t})pd\_{0}+a\_{t}pd\_{target}-\gamma(r\_{t}^{eff}-\hat{g}\_{t})b\_{t} |  | (9) |

where ata\_{t} is a logistic convergence factor, btb\_{t} is the debt-to-GDP ratio, rte​f​fr\_{t}^{eff} is the effective interest rate on debt, and g^t\hat{g}\_{t} is the nominal GDP growth rate. The coefficient γ\gamma is dependent on the regime ℛt\mathcal{R}\_{t}, being lower in crises to avoid excessive pro-cyclicality Blanchard and Leigh ([2013](https://arxiv.org/html/2510.16537v1#bib.bib29)).

The observed primary deficit, p​dtpd\_{t}, results from adjusting the target for discretionary spending and investment policies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​dt=p​dt∗+(Δ​GtC+Δ​GtI+Δ​TtR)−(τt−τ¯)pd\_{t}=pd\_{t}^{\*}+(\Delta G\_{t}^{C}+\Delta G\_{t}^{I}+\Delta T\_{t}^{R})-(\tau\_{t}-\bar{\tau}) |  | (10) |

### 6.4 Debt, Interest Rates, and Sovereign Risk

The law of motion for the debt-to-GDP ratio, btb\_{t}, is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bt+1=1+rte​f​f1+g^t​bt+p​dt+λtF​X​bt​(St+1o​f​fSto​f​f−1)b\_{t+1}=\frac{1+r\_{t}^{eff}}{1+\hat{g}\_{t}}b\_{t}+pd\_{t}+\lambda^{FX}\_{t}b\_{t}\left(\frac{S\_{t+1}^{off}}{S\_{t}^{off}}-1\right) |  | (11) |

The last term captures the valuation effect of foreign currency-denominated debt, whose proportion is λtF​X\lambda^{FX}\_{t}, in the event of a devaluation of the official exchange rate, Sto​f​fS\_{t}^{off} Krugman ([1999](https://arxiv.org/html/2510.16537v1#bib.bib150)).

The quarterly country risk, r​ptrp\_{t}, is a function of the debt level, reserves, the exchange rate gap, social unrest (U​n​r​e​s​ttUnrest\_{t}), and institutional quality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r​pt=ρr​p​r​pt−1+(1−ρr​p)​[f​(bt)+βR​Rt+βℬ​(ℬt−1)+βU​U​n​r​e​s​tt+βI​F​I​𝕀I​F​I+𝜷𝑰′​𝒁𝑰]rp\_{t}=\rho\_{rp}rp\_{t-1}+(1-\rho\_{rp})\left[f(b\_{t})+\beta\_{R}R\_{t}+\beta\_{\mathcal{B}}(\mathcal{B}\_{t}-1)+\beta\_{U}Unrest\_{t}+\beta\_{IFI}\mathbb{I}\_{IFI}+\bm{\beta\_{I}^{\prime}Z\_{I}}\right] |  | (12) |

where f​(bt)f(b\_{t}) is a logistic function increasing in the debt level Mendoza and Yue ([2012](https://arxiv.org/html/2510.16537v1#bib.bib172)), 𝕀I​F​I\mathbb{I}\_{IFI} is an indicator variable for the presence of a program with International Financial Institutions (IFIs), which can reduce perceived risk Vreeland ([2003](https://arxiv.org/html/2510.16537v1#bib.bib242)), and 𝒁𝑰\bm{Z\_{I}} is a vector of institutional quality variables (strength of fiscal rules, transparency). The model can incorporate debt restructuring events (PSI/OSI) that reduce the stock of debt and/or the interest burden, generating a discrete drop in r​ptrp\_{t}, although these events may have reputational costs Fernández Salguero ([2025f](https://arxiv.org/html/2510.16537v1#bib.bib84)). The effective interest rate, rte​f​fr\_{t}^{eff}, gradually adjusts towards the market rate (rtm​a​r​k​e​t=rf+r​ptr\_{t}^{market}=r\_{f}+rp\_{t}), reflecting the average maturity of the debt portfolio.

### 6.5 External Sector and Exchange Markets

The change in reserves as a proportion of GDP, Δ​Rt\Delta R\_{t}, is governed by the balance of payments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Rt=C​At+K​At\Delta R\_{t}=CA\_{t}+KA\_{t} |  | (13) |

The current account, C​AtCA\_{t}, depends on the real exchange rate, the output gap, and fiscal spending components, while the capital account, K​AtKA\_{t}, is sensitive to country risk, social unrest, and the exchange rate gap:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C​At\displaystyle CA\_{t} | =C​A¯+ηC​A,S​Δ​ln⁡Stp​a​r+ηC​A,g​gt+𝜼𝑪​𝑨,𝑮′​𝚫​𝑮𝒕+ϵtC​A\displaystyle=\bar{CA}+\eta\_{CA,S}\Delta\ln S\_{t}^{par}+\eta\_{CA,g}g\_{t}+\bm{\eta\_{CA,G}^{\prime}\Delta G\_{t}}+\epsilon\_{t}^{CA} |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K​At\displaystyle KA\_{t} | =ηK​A,r​p​r​pt+ηK​A,U​U​n​r​e​s​tt−fK​A,ℬ​(ℬt)+ϵtK​A\displaystyle=\eta\_{KA,rp}rp\_{t}+\eta\_{KA,U}Unrest\_{t}-f\_{KA,\mathcal{B}}(\mathcal{B}\_{t})+\epsilon\_{t}^{KA} |  | (15) |

where fK​A,ℬ​(⋅)f\_{KA,\mathcal{B}}(\cdot) is a non-linear function that captures the acceleration of capital flight as the exchange rate gap widens.

The exchange rate system is dual. The official exchange rate, Sto​f​fS\_{t}^{off}, can be fixed, follow a crawling peg, or undergo a discrete realignment (devaluation) if reserves fall below Rc​r​i​tR\_{crit}, a mechanism similar to first-generation crisis models Flood and Garber ([1984](https://arxiv.org/html/2510.16537v1#bib.bib92)); Kaminsky and Reinhart ([1999](https://arxiv.org/html/2510.16537v1#bib.bib138)). The parallel exchange rate, Stp​a​rS\_{t}^{par}, floats, and its dynamics determine the gap ℬt\mathcal{B}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ln⁡ℬt+1=αℬ,R​max⁡(0,Rc​r​i​tRt+1−1)+αℬ,r​p​r​pt+αℬ,U​U​n​r​e​s​tt−αℬ,c​r​e​d​C​r​e​dt+ϵtℬ\Delta\ln\mathcal{B}\_{t+1}=\alpha\_{\mathcal{B},R}\max\left(0,\frac{R\_{crit}}{R\_{t+1}}-1\right)+\alpha\_{\mathcal{B},rp}rp\_{t}+\alpha\_{\mathcal{B},U}Unrest\_{t}-\alpha\_{\mathcal{B},cred}Cred\_{t}+\epsilon\_{t}^{\mathcal{B}} |  | (16) |

This equation reflects that pressure on the parallel market increases with reserve scarcity, country risk, and social unrest, while greater policy credibility mitigates it.

### 6.6 Labor Market, Distribution, and Welfare

The level of employment, EtE\_{t} (as a fraction of the active population), is determined by a combination of demand and supply factors, approximating a market with monopsony power Sokolova and Sorensen ([2021](https://arxiv.org/html/2510.16537v1#bib.bib216)); Fernández Salguero ([2025j](https://arxiv.org/html/2510.16537v1#bib.bib88)).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Et+1=(1−ωE)​Et+ωE​(ϕd​gt−ϕr​(rte​f​f−g^t))+(1−ωE)​(ηs​Δ​wt)+ϵtEE\_{t+1}=(1-\omega\_{E})E\_{t}+\omega\_{E}(\phi\_{d}g\_{t}-\phi\_{r}(r\_{t}^{eff}-\hat{g}\_{t}))+(1-\omega\_{E})(\eta\_{s}\Delta w\_{t})+\epsilon\_{t}^{E} |  | (17) |

where wtw\_{t} is the real wage. Income inequality, measured by the Gini coefficient, responds negatively to progressive social transfers and positively to unemployment:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​i​n​it+1=G​i​n​it+βG,T​R​Δ​TtR+βG,E​(1−Et+1)+ϵtG​i​n​iGini\_{t+1}=Gini\_{t}+\beta\_{G,TR}\Delta T\_{t}^{R}+\beta\_{G,E}(1-E\_{t+1})+\epsilon\_{t}^{Gini} |  | (18) |

Finally, a social welfare index, 𝒲t\mathcal{W}\_{t}, is constructed as a weighted aggregate of macroeconomic and social variables, normalized for comparison.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲t=∑iwi⋅fi​(Xi,t)\mathcal{W}\_{t}=\sum\_{i}w\_{i}\cdot f\_{i}(X\_{i,t}) |  | (19) |

where Xi,tX\_{i,t} is a vector of key indicators (level of YtY\_{t}, EtE\_{t}, health, πt\pi\_{t}, btb\_{t}, ℬt\mathcal{B}\_{t}, U​n​r​e​s​ttUnrest\_{t}, G​i​n​itGini\_{t}) and wiw\_{i} are the weights assigned to each component. This index is an ad hoc tool for the comparative ranking of policy scenarios, not a cardinal measure of social utility. Its inclusion reflects the growing concern for the distributional and social effects of adjustment policies, often overlooked in traditional economic paradigms Stiglitz ([2005](https://arxiv.org/html/2510.16537v1#bib.bib225)); Fernández Salguero ([2025k](https://arxiv.org/html/2510.16537v1#bib.bib89)).

Table 4: Notation of the Main Variables and Parameters of the Model

| Symbol | Description |
| --- | --- |
| YtY\_{t} | Real Gross Domestic Product (GDP) in quarter tt. |
| YtPY\_{t}^{P} | Potential GDP. |
| gtg\_{t} | Output gap. |
| ℛt\mathcal{R}\_{t} | Economic regime (Boom, Recession, Crisis). |
| πt\pi\_{t} | Quarterly inflation rate. |
| π∗\pi^{\*} | Long-term inflation target. |
| btb\_{t} | Public debt to GDP ratio. |
| p​dtpd\_{t} | Primary deficit as a fraction of GDP. |
| rte​f​fr\_{t}^{eff} | Quarterly effective interest rate on debt. |
| g^t\hat{g}\_{t} | Nominal GDP growth rate. |
| r​ptrp\_{t} | Quarterly sovereign risk premium. |
| RtR\_{t} | Net international reserves as a fraction of GDP. |
| Rc​r​i​tR\_{crit} | Critical level of reserves. |
| Sto​f​fS\_{t}^{off} | Official nominal exchange rate. |
| Stp​a​rS\_{t}^{par} | Parallel nominal exchange rate. |
| ℬt\mathcal{B}\_{t} | Exchange rate gap (Stp​a​r/Sto​f​fS\_{t}^{par}/S\_{t}^{off}). |
| C​At,K​AtCA\_{t},KA\_{t} | Current account and capital account balances. |
| EtE\_{t} | Employment level (fraction of the active population). |
| wtw\_{t} | Real wage (index). |
| G​i​n​itGini\_{t} | Gini coefficient for income inequality. |
| U​n​r​e​s​ttUnrest\_{t} | Social unrest index. |
| C​r​e​dtCred\_{t} | Policy credibility index. |
| 𝒲t\mathcal{W}\_{t} | Synthetic social welfare index. |
| μt(⋅)\mu\_{t}^{(\cdot)} | Fiscal multipliers (GC: Current Spending, GI: Investment, TR: Transfers). |
| λtF​X\lambda\_{t}^{FX} | Proportion of debt denominated in foreign currency. |
| ϵt(⋅)\epsilon\_{t}^{(\cdot)} | Stochastic shocks with zero mean. |

## 7 Summary of Macroeconomic Simulation Results

A set of simulations (300 paths per strategy) was executed over a 40-quarter horizon (10 years) to evaluate the performance of 29 different macroeconomic strategies. The main objective is to compare the outcomes in terms of debt sustainability, economic growth, and social welfare. The key indicators at the end of the period (Quarter 40) are the median Debt/GDP ratio (Debt\_med), the median GDP level (GDP\_med) relative to the starting point, and a composite social welfare metric (Welfare\_med).

The results show a very significant divergence among the different families of strategies. On one hand, shock fiscal adjustment policies, especially those accompanied by an initial devaluation without a debt restructuring framework, lead to the worst outcomes, with a debt ratio exceeding 200% of GDP and a drastic fall in welfare. On the other hand, the most successful strategies are those that combine an aggressive fiscal restructuring with debt reprofiling, financing from international financial institutions (IFIs), and, crucially, the implementation of structural reforms like a land value tax (LVT). These strategies not only manage to contain but also reduce the debt ratio to below 110% of GDP, while maintaining a higher level of economic activity and achieving welfare levels that are double those of conventional strategies.

Between these two extremes lies a group of conventional strategies (gradual adjustments, standard IMF-type programs, and partial restructurings) that, while avoiding collapse, fail to stabilize debt dynamics, ending the period with ratios in the 160% to 170% of GDP range. Within this group, those that include debt relief (PSI/OSI) and IFI financing show a markedly superior performance to those based solely on fiscal adjustment, managing to reduce the final debt by approximately 30 percentage points of GDP and substantially improving welfare.

### 7.1 Comparative Table of Strategies (Median Results at T=40)

The following table presents a summary of the median results for all evaluated strategies at the end of the simulation horizon (Quarter 40). The strategies are ordered by their Debt/GDP level, from lowest to highest.

Table 5: Median Results at Quarter 40 by Strategy.

| Strategy | Median GDP | Median Debt (%) | Median Welfare |
| --- | --- | --- | --- |
| AggRecomp\_GI+TR\_modDebt\_MKT\_LVT | 98.35 | 106.25 | 20.63 |
| AggRecomp\_GI+TR\_modDebt\_IFI\_LVT | 99.24 | 107.46 | 21.44 |
| AggRecomp\_GI+TR\_lowDebt\_IFI\_LVT | 97.62 | 108.08 | 20.90 |
| AggRecomp\_GI+TR\_noDebt\_LVT | 97.93 | 108.24 | 20.27 |
| Aggressive-Recomp+PSI+OSI+IFI | 98.61 | 133.25 | 17.35 |
| Balanced-Recomp+PSI+OSI+IFI | 97.69 | 135.62 | 17.84 |
| PSI30+IFI1.5 | 98.70 | 150.15 | 16.35 |
| Minimal-Recomp | 100.21 | 157.62 | 14.78 |
| Gradual-1.5 | 98.58 | 159.26 | 12.77 |
| Gradual-3 | 98.76 | 159.58 | 12.74 |
| LMO-LCY-Shift | 96.43 | 161.39 | 13.20 |
| Balanced-Recomp | 99.22 | 161.50 | 15.52 |
| IMF-2025-base+SoftMonetary | 99.18 | 162.01 | 14.66 |
| SCD+IFI2 | 97.01 | 162.07 | 14.69 |
| IMF-no-IFI | 97.35 | 162.32 | 13.53 |
| IMF-2025-base | 98.23 | 163.26 | 14.77 |
| Swap+4pp | 98.59 | 164.49 | 13.50 |
| Loans-Only | 97.48 | 165.22 | 13.80 |
| Aggressive-Recomp | 97.25 | 165.55 | 14.95 |
| AggRecomp\_GI+TR\_lowDebt\_IFI\_noLVT | 98.13 | 167.12 | 13.95 |
| Shock-8 | 95.64 | 171.03 | 11.93 |
| Shock-12 | 93.48 | 171.26 | 11.19 |
| Crawl15%+CFM8q | 98.69 | 172.95 | 14.22 |
| AggRecomp\_GI+TR\_hiDebt\_IFI\_Deval | 98.18 | 196.42 | 11.44 |
| AggRecomp\_GI+TR\_hiDebt\_MKT\_Deval | 97.69 | 197.65 | 11.18 |
| AggRecomp\_GI+TR\_noDebt\_noDeval\_noLVT | 97.27 | 199.19 | 10.68 |
| AggRecomp\_GI+TR\_noDebt\_Deval\_noLVT | 96.87 | 199.79 | 10.24 |
| Shock-6+Deval | 96.66 | 201.38 | 9.53 |
| Shock-6+Deval+DebtMKT | 94.90 | 204.18 | 8.74 |
| Note: Strategy names are coded. "AggRecomp" denotes an aggressive spending recomposition towards Investment (GI) and Transfers (TR). "Balanced-Recomp" is a more moderate version. "LVT" indicates a Land Value Tax reform. "PSI/OSI" refers to debt restructuring with Private/Official Sector Involvement. "IFI" means financing from International Financial Institutions. | | | |

### 7.2 Ranking of Strategies by Highest Welfare

This table highlights the five strategies with the highest median welfare level at the end of the period, while also maintaining a relatively high GDP level. It is observed that strategies combining aggressive fiscal spending and structural restructuring (LVT) clearly dominate, followed by comprehensive packages that include debt restructuring (PSI/OSI) and IFI support.

Table 6: Top 5 Strategies by Welfare and GDP at T=40.

| Strategy | Median GDP | Debt (%) | Welfare | Reserves |
| --- | --- | --- | --- | --- |
| AggRecomp\_GI+TR\_modDebt\_IFI\_LVT | 99.24 | 107.46 | 21.44 | 3.97 |
| AggRecomp\_GI+TR\_lowDebt\_IFI\_LVT | 97.62 | 108.08 | 20.90 | 3.17 |
| AggRecomp\_GI+TR\_modDebt\_MKT\_LVT | 98.35 | 106.25 | 20.63 | 3.99 |
| AggRecomp\_GI+TR\_noDebt\_LVT | 97.93 | 108.24 | 20.27 | 2.00 |
| Balanced-Recomp+PSI+OSI+IFI | 97.69 | 135.62 | 17.84 | 21.21 |

### 7.3 Evolution of Key Indicators for Selected Strategies

To illustrate the divergence in trajectories, the following table shows the evolution of debt and welfare for four representative strategies: a high-performing one (with LVT), a well-performing one (with PSI/OSI), a conventional one (IMF), and a low-performing one (shock with devaluation).

Table 7: Median Trajectories of Debt and Welfare for Representative Strategies.

|  | Median Debt (%) | | | Median Welfare | | |
| --- | --- | --- | --- | --- | --- | --- |
| Strategy | T=0 | T=16 | T=40 | T=0 | T=16 | T=40 |
| AggRecomp\_GI+TR\_modDebt\_MKT\_LVT | 110.0 | 91.49 | 106.25 | 14.46 | 25.36 | 20.63 |
| Balanced-Recomp+PSI+OSI+IFI | 110.0 | 83.59 | 135.62 | 14.44 | 25.72 | 17.84 |
| IMF-base+SoftMonetary | 110.0 | 121.49 | 162.01 | 14.13 | 21.30 | 14.66 |
| Shock-6+Deval | 110.0 | 163.20 | 201.38 | 14.33 | 15.98 | 9.53 |

### 7.4 Graphical Analysis of Results

To complement the tabular analysis, the following figures visualize the key relationships between the main outcome variables at the end of the simulation period (T=40). These graphs help identify performance clusters and visualize the inherent trade-offs of the different policies.

![Refer to caption](1.png)


Figure 1: Relationship between GDP and Debt/GDP at the end of the period (T=40).

Figure 1 shows the relationship between the median GDP level and the median Debt/GDP ratio. The upper-left quadrant represents the most desirable outcome: high GDP with low debt. A clear segmentation of strategies is observed. An elite group, composed almost exclusively of strategies implementing a Land Value Tax (...LVT), is located in the top-left corner, achieving the lowest debt ratios (between 106% and 110%) without sacrificing the level of economic activity. At the opposite extreme, in the bottom-right corner, are the shock and fiscal adjustment strategies without debt relief (Shock-6+Deval, AggRecomp\_...\_noLVT), which result in explosive debt (over 195%) and a comparatively lower GDP. The vast majority of conventional strategies (IMF-base, Gradual, etc.) are clustered in an intermediate zone, with high debt levels (155%-175%) and a GDP that, while relatively high, does not compensate for fiscal unsustainability.

![Refer to caption](2.png)


Figure 2: Relationship between Welfare and Debt/GDP at the end of the period (T=40).

Figure 2 graphs the relationship between median welfare and debt. The negative correlation is even more pronounced than in the case of GDP. The results are stratified into four clear levels:

1. 1.

   Exceptional Performance (top left): Strategies with LVT achieve a much higher level of welfare (above 20), demonstrating that fiscal solvency achieved through structural reforms has a direct and massive impact on social welfare.
2. 2.

   Good Performance (upper center): Strategies that include significant debt relief (...PSI+OSI+IFI) are situated in a second tier, with high welfare (17-18) and debt contained around 135%. This underscores the importance of debt restructuring for social recovery.
3. 3.

   Mediocre Performance (lower center): The cluster of conventional strategies shows considerably lower welfare levels (12-15), indicating that the persistence of a high debt burden limits the ability to generate welfare, even with a stable GDP.
4. 4.

   Poor Performance (bottom right): Pure shock and adjustment strategies without debt relief cause welfare to collapse to levels below 12, confirming that severe austerity with rising debt is the worst combination for society.

![Refer to caption](3.png)


Figure 3: Median Debt/GDP Ratio at Q40 ordered by scenario.

Figure 3 offers an unequivocal ranking of all strategies based on their median debt outcome at the end of the horizon. This bar chart visually confirms the stratification observed in the scatter plots. Clear steps grouping families of policies are visible. The first group, with debt contained below 110%, corresponds to policies with LVT. It is followed by a second step with debt relief strategies (PSI/OSI) that stabilize around 135%-150%. Next, a long plateau of conventional policies is observed, which fail to break below the 157% debt floor. Finally, the graph shows a rapid ascent to unsustainable levels for strategies of severe adjustment without restructuring. Overall, this figure compellingly summarizes the main finding: without deep structural reforms or substantial debt relief, conventional policies are not sufficient to resolve the debt crisis.

## 8 Conclusions

The Crisis Simulator for Bolivia (KISr-p) represents an effort to build a policy analysis framework that is theoretically coherent, computationally robust, and, above all, disciplined by the vast empirical evidence consolidated through meta-analyses. By adopting a KIS-CES architecture that incorporates heterogeneity, frictions, and market power, the model is able to replicate the key empirical regularities that define modern macroeconomics.

The conclusions emerging from the analysis of the simulated scenarios challenge conventional narratives. First, the simulator’s evidence is clear: the composition of fiscal adjustment matters more than its aggregate magnitude. Strategies based on indiscriminate spending cuts tend to be contractionary and worsen debt sustainability. Conversely, strategies that reallocate resources from current spending to public investment in high-multiplier physical and human capital can be expansionary. This empirically validates the central pillar of evidence on the importance of productive investment as a dual engine of demand and supply.

Second, the model underscores that simple solutions are insufficient for complex problems. Neither fiscal adjustment alone, nor external financing, nor debt restructuring are panaceas. The most robust results are achieved through comprehensive policy packages that combine an intelligent fiscal adjustment (aggressive spending restructuring) with debt burden relief and structural reforms that strengthen institutional anchors. Pragmatism, based on a nuanced reading of the evidence, overcomes ideological dogmatism.

The modeling exercise demonstrates the urgency of integrating the findings of quantitative synthesis into the practice of economic policy. Ignoring the cycle-dependency of multipliers, the existence of monopsony power in the labor market, or the complementary nature of public and private capital is not a harmless simplification; it is an error that leads to suboptimal and harmful policy recommendations. The KIS-CES simulator offers a platform for a more informed policy dialogue, where decisions are based not on a single study or a single theory, but on the aggregated weight of decades of empirical research.

## References

* Abrahamsson (2003)

  Abrahamsson, H. (2003). Mozambique and the Washington Consensus. In Understanding World Order and Structural Change (pp. 58–80). Palgrave Macmillan UK. [doi:10.1057/9781403944054\_4](https://doi.org/10.1057/9781403944054_4).
* Afonso et al. (2014)

  Afonso, A., Zartaloudis, S., and Papadopoulos, Y. (2014). How party linkages shape austerity politics: clientelism and fiscal adjustment in Greece and Portugal during the eurozone crisis. Journal of European Public Policy, 22(3), 315-334. [doi:10.1080/13501763.2014.964644](https://doi.org/10.1080/13501763.2014.964644).
* Alao et al. (2021)

  Alao, R., Nur, H., Fivian, E., Shankar, B., Kadiyala, S., and Harris-Fry, H. (2021). Economic inequality in malnutrition: a global systematic review and meta-analysis. BMJ Global Health, 6(12), e006906.
* Alarcon Gambarte (2020)

  Alarcon Gambarte, S. (2020). Multiplicador de inversión pública durante el auge y declive de precios internacionales [Public investment multiplier during the boom and bust of international prices]. LAJED, (33), 79-104.
* Alinaghi and Reed (2018)

  Alinaghi, N., and Reed, W. R. (2018). Taxes and Economic Growth in OECD Countries: A Meta-Analysis. University of Canterbury, Department of Economics and Finance, Working Paper No. 9/2018.
* Angin and Naqvi (2024)

  Angin, M., and Naqvi, N. (2024). Winner Takes All? The Distributional Impact of IMF Privatization Conditionality. Working Paper.
* Antelo (2000)

  Antelo Callisperis, E. (2000). La capitalización en Bolivia [The capitalization in Bolivia]. Documento de Trabajo.
* Aponte Pinzón (2017)

  Aponte Pinzón, Á. (2017). El proceso de descentralización en América Latina: Balance y perspectivas [The decentralization process in Latin America: A balance and perspectives]. ECONÓMICAS CUC, 38(2), 9–20. [doi:10.17981/econcuc.38.2.2017.01](https://doi.org/10.17981/econcuc.38.2.2017.01).
* Arango-Lozano et al. (2024)

  Arango-Lozano, L., Menkhoff, L., Rodríguez-Novoa, D., and Villamizar-Villegas, M. (2024). The effectiveness of FX interventions: A meta-analysis. Journal of Financial Stability, 74, 100794.
* Araújo et al. (2025)

  Araújo, T., Afonso, Ó., Neves, P. C., and Sochirca, E. (2025). International spillovers of unconventional monetary policy: A meta-analysis. Portuguese Economic Journal, 24, 205-224.
* Archibong et al. (2020)

  Archibong, B., Coulibaly, B., and Okonjo-Iweala, N. (2020). Washington Consensus Reforms and Economic Performance in Sub-Saharan Africa: Lessons From the Past Four Decades. SSRN Electronic Journal. [doi:10.2139/ssrn.3780433](https://doi.org/10.2139/ssrn.3780433).
* Armendáriz et al. (2021)

  Armendáriz, E., Andrián, L., Contreras, E., y Hirs, J. (2021). Planificación y priorización ex ante de la inversión pública en los Países Andinos [Ex-ante planning and prioritization of public investment in the Andean Countries]. Nota Técnica N° IDB-TN-2171, Banco Interamericano de Desarrollo.
* Avramović and Đukić (2020)

  Avramović, N., and Đukić, S. (2020). Washington Consensus and choice of transition road. Bastina, (50), 133–146. [doi:10.5937/bastina30-25575](https://doi.org/10.5937/bastina30-25575).
* Babb (2013)

  Babb, S. (2013). The Washington Consensus as transnational policy paradigm: Its origins, trajectory and likely successor. Review of International Political Economy, 20(2), 268–297. [doi:10.1080/09692290.2011.640435](https://doi.org/10.1080/09692290.2011.640435).
* Babb and Kentikelenis (2021)

  Babb, S., and Kentikelenis, A. (2021). Markets Everywhere: The Washington Consensus and the Sociology of Global Institutional Change. Annual Review of Sociology, 47(1), 521–541. [doi:10.1146/annurev-soc-090220-025543](https://doi.org/10.1146/annurev-soc-090220-025543).
* Balima et al. (2020a)

  Balima, H. W., Kilama, E. G., and Tapsoba, R. (2020). Inflation targeting: Genuine effects or publication selection bias?. European Economic Review, 128, 103520.
* Ban (2020)

  Ban, C. (2020). Emergency Keynesianism 2.0: The political economy of fiscal policy in Europe during the Corona Crisis. Samfundsøkonomen, (4), 16-26. [doi:10.7146/samfundsokonomen.v0i4.123557](https://doi.org/10.7146/samfundsokonomen.v0i4.123557).
* Bansak et al. (2019)

  Bansak, K., Bechtel, M., and Margalit, Y. (2019). Why Austerity? The Mass Politics of a Contested Policy. SSRN. [doi:10.2139/ssrn.3486227](https://doi.org/10.2139/ssrn.3486227).
* Banzhaf and Lavery (2010)

  Banzhaf, H. S. and Lavery, N. (2010). Can the land tax help curb urban sprawl? Evidence from growth patterns in Pennsylvania. Journal of Urban Economics, 67(2), 169–179.
* Barro and Lee (2005)

  Barro, R. J., and Lee, J. W. (2005). IMF programs: Who is chosen and what are the effects? Journal of Monetary Economics, 52(7), 1245-1269.
* Bel and Esteve (2019)

  Bel, G., and Esteve, M. (2019). Is Private Production of Hospital Services Cheaper than Public Production? A Meta-Regression of Public Versus Private Costs and Efficiency for Hospitals. International Public Management Journal.
* Bel et al. (2010)

  Bel, G., Fageda, X., and Warner, M. E. (2010). Is private production of public services cheaper than public production? A meta-regression analysis of solid waste and water services. Journal of Policy Analysis and Management, 29(3), 553-577.
* Bergeron (2003)

  Bergeron, S. (2003). The Post-Washington Consensus and Economic Representations of Women in Development at the World Bank. International Feminist Journal of Politics, 5(3), 397–419. [doi:10.1080/1461674032000122759](https://doi.org/10.1080/1461674032000122759).
* Berr and Combarnous (2005)

  Berr, É., and Combarnous, F. (2005). Vingt ans d’application du consensus de Washington à l’épreuve des faits [Twenty years of applying the Washington Consensus put to the test of facts]. Économie appliquée, 58(2), 5–44. [doi:10.3406/ecoap.2005.3752](https://doi.org/10.3406/ecoap.2005.3752).
* Bianchi et al. (2019)

  Bianchi, J., Ottonello, P., and Presno, I. (2019). Fiscal Stimulus under Sovereign Risk. NBER. [doi:10.3386/w26307](https://doi.org/10.3386/w26307).
* Biderman and Batista (2018)

  Biderman, C. and Batista, Y. C. (2018). Is Progressive Property Tax Progressive? Evidences from São Paulo. Lincoln Institute of Land Policy.
* Biglaiser and McGauvran (2022)

  Biglaiser, G., and McGauvran, R. J. (2022). The effects of IMF loan conditions on poverty in the developing world. Journal of International Relations and Development, 25, 806-833.
* Bilbao-Ubillos and Fernández-Sainz (2014)

  Bilbao-Ubillos, J., and Fernández-Sainz, A. (2014). The impact of austerity policies in the Eurozone: fiscal multipliers and ’adjustment fatigue’. Applied Economics Letters, 21(14), 955-959. [doi:10.1080/13504851.2014.902013](https://doi.org/10.1080/13504851.2014.902013).
* Blanchard and Leigh (2013)

  Blanchard, O., and Leigh, D. (2013). Growth forecast errors and fiscal multipliers. American Economic Review, 103(3), 117-20.
* Blot et al. (2014)

  Blot, C., Cochard, M., Creel, J., Ducoudré, B., Schweisguth, D., and Timbeau, X. (2014). Fiscal consolidation in times of crisis: is the sooner really the better?. Revue de l’OFCE, N° 132(1), 159-192. [doi:10.3917/reof.132.0159](https://doi.org/10.3917/reof.132.0159).
* Blyth (2013)

  Blyth, M. (2013). Austerity: The History of a Dangerous Idea. Oxford University Press.
* Bolivar Rosales (2022)

  Bolivar Rosales, O. (2022). Efecto Multiplicador: Evidencia empírica para una asignación costo-efectiva de la inversión pública [Multiplier Effect: Empirical evidence for a cost-effective allocation of public investment]. Cuadernos de Investigación Económica Boliviana, 5(2), 7-64.
* Bom and Ligthart (2014)

  Bom, P. R. D., and Ligthart, J. E. (2014). What have we learned from three decades of research on the productivity of public capital?. Journal of Economic Surveys, 28(5), 889-916.
* Bonnet et al. (2021)

  Bonnet, O., Chapelle, G., Trannoy, A., and Wasmer, E. (2021). Land is back, it should be taxed, it can be taxed. European Economic Review, 134, 103696.
* Botta (2013)

  Botta, A. (2013). CARMEN REINHART AND KENNETH ROGOFF IN A TIME OF FISCAL AUSTERITY: A CRITICAL ANALYSIS OF THE EXPANSIONARY AUSTERITY THEORY. Istituto Lombardo - Accademia di Scienze e Lettere. [doi:10.4081/let.2013.215](https://doi.org/10.4081/let.2013.215).
* Bougrine (2012)

  Bougrine, H. (2012). Fiscal austerity, the Great Recession and the rise of new dictatorships. Review of Keynesian Economics, 1(0), 109-125. [doi:10.4337/roke.2012.01.07](https://doi.org/10.4337/roke.2012.01.07).
* Brada et al. (2021)

  Brada, J. C., Drabek, Z., and Iwasaki, I. (2021). Does Investor Protection Increase Foreign Direct Investment? A Meta-Analysis. Journal of Economic Surveys, 35(1), 34-70.
* Brito-Gaona and Iglesias (2017)

  Brito-Gaona, L. F., y Iglesias, E. M. (2017). Inversión privada, gasto público y presión tributaria en América Latina [Private investment, public spending, and tax burden in Latin America]. Estudios de Economía, 44(2), 131-156.
* Buettner (2003)

  Buettner, T. (2003). Tiebout visits germany: Land tax capitalization in a sample of german municipalities. CESifo Working Paper Series.
* Bumann et al. (2013)

  Bumann, S., Hermes, N., and Lensink, R. (2013). Financial liberalization and economic growth: a meta-analysis. Journal of International Money and Finance, 33, 255-281.
* Capretti and Tonni (2025)

  Capretti, L., and Tonni, L. (2025). Income Inequality and Economic Growth: A Meta-Analytic Approach. Working Paper, March 20, 2025 version.
* Card (2001)

  Card, D. (2001). Immigrant inflows, native outflows, and the local market impacts of higher immigration. Journal of Labor Economics, 19(1), 22-64.
* Card and Krueger (1995a)

  Card, D., and Krueger, A. B. (1995a). Time-series minimum-wage studies: A meta-analysis. American Economic Review, 85(2), 238–243.
* Castañeda Rodríguez and Díaz Bautista (2017)

  Castañeda Rodríguez, V., and Díaz Bautista, O. (2017). El Consenso de Washington: algunas implicaciones para América Latina [The Washington Consensus: some implications for Latin America]. Apuntes del Cenes, 36(63), 15–41. [doi:10.19053/01203053.v36.n63.2017.4425](https://doi.org/10.19053/01203053.v36.n63.2017.4425).
* Cepeda et al. (2025)

  Cepeda, V., Taboada, B., and Villamizar-Villegas, M. (2025). Can Central Bank Credibility Improve Monetary Policy? A Meta-Analysis. International Finance, 28, 115-140.
* Chaudhary et al. (2024)

  Chaudhary, N., Jones, M., Rice, S. P. M., Zeigen, L., and Thosar, S. S. (2024). Transitioning to Working from Home Due to the COVID-19 Pandemic Significantly Increased Sedentary Behavior and Decreased Physical Activity: A Meta-Analysis. International Journal of Environmental Research and Public Health, 21(7), 851.
* Chavez and Murcia (2023)

  Chavez, F. C., Jr., and Murcia, J. V. B. (2023). A Systematic Review and Meta-Analysis on the Association Between Remote Work Arrangements and Job Satisfaction of Employees in Private Firms. Southeast Asian Journal of Multidisciplinary Studies, 3(3).
* Christiano et al. (2011)

  Christiano, L. J., Eichenbaum, M., and Rebelo, S. (2011). When is the government spending multiplier large?. Journal of Political Economy, 119(1), 78-121.
* Churchill et al. (2016)

  Churchill, S. A., Ugur, M., and Yew, S. L. (2016). Does government size affect per-capita income growth? a hierarchical meta-regression analysis. Economic Record, 92(299), 551-571.
* Cipollina et al. (2018)

  Cipollina, M., Cuffaro, N., and D’Agostino, G. (2018). Land Inequality and Economic Growth: A Meta-Analysis. Sustainability, 10(12), 4655.
* Clapp and Lindenthal (2022)

  Clapp, J. M. and Lindenthal, T. (2022). Urban land valuation with bundled good and land residual assumptions. Journal of Housing Economics, 58, 101872.
* Coronado and Aguayo (2002)

  Coronado, P., y Aguayo, E. (2002). Inversión pública e inversión privada en Bolivia [Public investment and private investment in Bolivia]. Estudios Económicos de Desarrollo Internacional, 2(2), 71-94.
* Correa (2002)

  Correa, R. (2002). Reformas estructurales y crecimiento en América Latina: Un análisis de sensibilidad [Structural reforms and growth in Latin America: A sensitivity analysis]. Revista de la CEPAL, 2002(76), 89–107. [doi:10.18356/8b3b24b1-es](https://doi.org/10.18356/8b3b24b1-es).
* Crosta et al. (2025)

  Crosta, T., Karlan, D., Ong, F., Rüschenpöhler, J., and Udry, C. R. (2025). Unconditional cash transfers: a bayesian meta-analysis of randomized evaluations in low and middle income countries. NBER Working Paper Series, No. 32779.
* Crowley (2020)

  Crowley, N. (2020). Austerity and ethno-nationalism. In Mapping Populism (pp. 134-145). Routledge. [doi:10.4324/9780429295089-13](https://doi.org/10.4324/9780429295089-13).
* Cukrowska-Torzewska and Matysiak (2020)

  Cukrowska-Torzewska, E., and Matysiak, A. (2020). The motherhood wage penalty: A meta-analysis. Social Science Research, 88-89, 102416.
* Cypher (1998)

  Cypher, J. M. (1998). The Slow Death of the Washington Consensus on Latin America. Latin American Perspectives, 25(6), 47–51. [doi:10.1177/0094582x9802500609](https://doi.org/10.1177/0094582x9802500609).
* Daoud et al. (2017)

  Daoud, A., Nosrati, E., Reinsberg, B., Kentikelenis, A. E., Stubbs, T. H., and King, L. P. (2017). Impact of International Monetary Fund programs on child health. Proceedings of the National Academy of Sciences, 114(25), 6492-6497.
* De Grauwe and Costa Storti (2004)

  De Grauwe, P., and Costa Storti, C. (2004). The Effects of Monetary Policy: A Meta-Analysis. CESifo Working Paper No. 1224.
* De Haan et al. (2006)

  De Haan, J., Lundström, S., and Sturm, J. E. (2006). Market-oriented institutions and policies and economic growth: A critical survey. Journal of Economic Surveys, 20(2), 157-191.
* De Vogli (2013)

  De Vogli, R. (2013). Financial crisis, austerity, and health in Europe. The Lancet, 382(9890), 391. [doi:10.1016/s0140-6736(13)61662-1](https://doi.org/10.1016/s0140-6736(13)61662-1).
* Dellepiane-Avellaneda (2014)

  Dellepiane-Avellaneda, S. (2014). The Political Power of Economic Ideas: The Case of ‘Expansionary Fiscal Contractions’. The British Journal of Politics and International Relations, 17(3), 391-418. [doi:10.1111/1467-856x.12038](https://doi.org/10.1111/1467-856x.12038).
* Devereaux et al. (2002)

  Devereaux, P. J., Choi, P. T. L., Lacchetti, C., Weaver, B., Schünemann, H. J., Haines, T., … and Guyatt, G. H. (2002). A systematic review and meta-analysis of studies comparing mortality rates of private for-profit and private not-for-profit hospitals. CMAJ, 166(11), 1399-1406.
* Dosi et al. (2016)

  Dosi, G., Napoletano, M., Roventini, A., and Treibich, T. (2016). The Short- and Long-Run Damages of Fiscal Austerity: Keynes beyond Schumpeter. In Contemporary Issues in Macroeconomics (pp. 79-100). Palgrave Macmillan. [doi:10.1057/9781137529589\_9](https://doi.org/10.1057/9781137529589_9).
* Doucouliagos and Stanley (2009)

  Doucouliagos, H., and Stanley, T. D. (2009). Publication selection bias in minimum-wage research? A meta-regression analysis. British Journal of Industrial Relations, 47(2), 406–428.
* Doucouliagos and Stanley (2013)

  Doucouliagos, C., and Stanley, T. D. (2013). Are all economic facts greatly exaggerated? Theory competition and selectivity. Journal of Economic Surveys, 27(2), 316-339.
* Doucouliagos and Zigova (2025)

  Doucouliagos, H., and Zigova, K. (2025). Minimum Wages and Human Capital Investment: A Meta-Regression Analysis. British Journal of Industrial Relations, 0, 1-20.
* Dube and Zipperer (2024)

  Dube, A., and Zipperer, B. (2024). Own-wage elasticity: Quantifying the impact of minimum wages on employment. NBER Working Paper, No. 32925.
* Easterly (2019)

  Easterly, W. (2019). In Search of Reforms for Growth: New Stylized Facts on Policy and Growth Outcomes. National Bureau of Economic Research. [doi:10.3386/w26318](https://doi.org/10.3386/w26318).
* Echavarria and Monkkonen (2025)

  Echavarria, A. and Monkkonen, P. (2025). Challenges to equitable and effective land value capture: Lessons from Mexico City. Urban Affairs Review.
* Ehrenbergerova et al. (2021)

  Ehrenbergerova, D., Bajzik, J., and Havranek, T. (2021). When Does Monetary Policy Sway House Prices? A Meta-Analysis. ZBW - Leibniz Information Centre for Economics.
* Eicher et al. (2025)

  Eicher, T., Eskimez, R. K., and Sengar, G. (2025). Evaluating the Impact of IMF Programs on GDP Growth: A Synthetic Control Method Approach. Working Paper, version March 20, 2025.
* El-Shagi and Zheng (2022)

  El-Shagi, M., and Zheng, Y. (2022). Money Demand in China: A Meta Study. Emerging Markets Finance and Trade, 58(1), 145-163.
* Enzinger et al. (2025)

  Enzinger, M., Gechert, S., Heimberger, P., Prante, F., and Romero, D. F. (2025). The overstated effects of conventional monetary policy on output and prices. OSF Preprint. [doi:10.31219/osf.io/72cen\_v2](https://doi.org/10.31219/osf.io/72cen_v2).
* Estevadeordal and Taylor (2008)

  Estevadeordal, A., and Taylor, A. (2008). Is the Washington Consensus Dead? Growth, Openness, and the Great Liberalization, 1970s-2000s. National Bureau of Economic Research. [doi:10.3386/w14264](https://doi.org/10.3386/w14264).
* Ferchen (2013)

  Ferchen, M. (2013). Whose China Model is it anyway? The contentious search for consensus. Review of International Political Economy, 20(2), 390-420. [doi:10.1080/09692290.2012.660184](https://doi.org/10.1080/09692290.2012.660184).
* Fernández-Albertos and Kuo (2020)

  Fernandez-Albertos, J., and Kuo, A. (2020). Selling Austerity: Preferences for Fiscal Adjustment during the Eurozone Crisis. Comparative Politics, 52(2), 197-227. [doi:10.5129/001041520x15682460031849](https://doi.org/10.5129/001041520x15682460031849).
* Fernández Salguero (2025)

  Fernández Salguero, R. A. (2025). Bolivia Crisis Simulator KISr-p (v1.0) [Software]. Zenodo.
  Available at: <https://doi.org/10.5281/zenodo.17380797>
    
  Repository: <https://github.com/RAFS20/Bolivia-Crisis-Simulator-KISr-p/tree/main>
* Fernández Salguero (2025a)

  Fernández Salguero, R. A. (2025a). El Consenso de Washington: una revisión narrativa de su evidencia, impactos y transformaciones [The Washington Consensus: a narrative review of its evidence, impacts, and transformations]. OSF Preprint. [doi:10.31235/osf.io/krshu\_v1](https://doi.org/10.31235/osf.io/krshu_v1).
* Fernández Salguero (2025b)

  Fernández Salguero, R. A. (2025b). El impuesto sobre el valor del suelo: un análisis integral de su teoría, evidencia empírica y desafíos de implementación [The land value tax: a comprehensive analysis of its theory, empirical evidence, and implementation challenges]. Zenodo. [doi:10.5281/zenodo.17074415](https://doi.org/10.5281/zenodo.17074415).
* Fernández Salguero (2025c)

  Fernández Salguero, R. A. (2025c). Análisis, evidencia y teoría en la economía laboral: una síntesis de evidencia empírica [Analysis, evidence, and theory in labor economics: a synthesis of empirical evidence]. Zenodo. [doi:10.5281/zenodo.17266154](https://doi.org/10.5281/zenodo.17266154).
* Fernández Salguero (2025d)

  Fernández Salguero, R. A. (2025d). La Interacción entre la Inversión Pública y Privada en Bolivia: Una revisión y teoría a partir de la evidencia empírica [The Interaction between Public and Private Investment in Bolivia: A review and theory based on empirical evidence]. Zenodo. [doi:10.5281/zenodo.16786987](https://doi.org/10.5281/zenodo.16786987).
* Fernández Salguero (2025e)

  Fernández Salguero, R. A. (2025e). Análisis Crítico del Modelo Económico Social Comunitario Productivo [Critical Analysis of the Social Communitarian Productive Economic Model]. Zenodo. [doi:10.5281/zenodo.16879530](https://doi.org/10.5281/zenodo.16879530).
* Fernández Salguero (2025f)

  Fernández Salguero, R. A. (2025f). Análisis del impacto de los programas del Fondo Monetario Internacional [Analysis of the impact of International Monetary Fund programs]. Zenodo. [doi:10.5281/zenodo.17002359](https://doi.org/10.5281/zenodo.17002359).
* Fernández Salguero (2025g)

  Fernández Salguero, R. A. (2025g). Una Síntesis Intertemporal Keynesiana (KIS) para una Economía Abierta: Fundamentos empíricos desde los metaanálisis [A Keynesian Intertemporal Synthesis (KIS) for an Open Economy: Empirical foundations from meta-analyses]. Zenodo. [doi:10.5281/zenodo.16907905](https://doi.org/10.5281/zenodo.16907905).
* Fernández Salguero (2025h)

  Fernández Salguero, R. A. (2025h). A Keynesian Intertemporal Synthesis (KIS) Model: Towards a unified and empirically grounded framework for fiscal policy. arXiv preprint arXiv:2508.00224. [doi:10.48550/arXiv.2508.00224](https://doi.org/10.48550/arXiv.2508.00224).
* Fernández Salguero (2025i)

  Fernández Salguero, R. A. (2025i). An Analysis of Monetary Policy Evidence and Theory through Meta-Analyses. arXiv preprint arXiv:2509.19591. [doi:10.48550/arXiv.2509.19591](https://doi.org/10.48550/arXiv.2509.19591).
* Fernández Salguero (2025j)

  Fernández Salguero, R. A. (2025j). Integrated analysis of informality, minimum wage, and monopsony power: A synthesis of meta-analyses with unified theoretical underpinnings. arXiv preprint arXiv:2509.20465. [doi:10.48550/arXiv.2509.20465](https://doi.org/10.48550/arXiv.2509.20465).
* Fernández Salguero (2025k)

  Fernández Salguero, R. A. (2025k). Austerity in Crisis?: A Narrative Review of Its Economic, Social, and Political Effects in Times of Crisis. arXiv preprint arXiv:2510.10449. [doi:10.48550/arXiv.2510.10449](https://doi.org/10.48550/arXiv.2510.10449).
* Fidrmuc and Danišková (2020)

  Fidrmuc, J., and Danišková, K. (2020). Meta-Analysis of the New Keynesian Phillips Curve in Developed and Emerging Economies. Emerging Markets Finance and Trade, 56(1), 10-31.
* Filomena and Picchio (2022)

  Filomena, M., and Picchio, M. (2022). Are temporary jobs stepping stones or dead ends? A systematic review of the literature. International Journal of Manpower, 43(9), 60-74.
* Flood and Garber (1984)

  Flood, R. P., and Garber, P. M. (1984). Collapsing exchange-rate regimes: some linear examples. Journal of International Economics, 17(1-2), 1-13.
* Floridi et al. (2020)

  Floridi, A., Demena, B. A., and Wagner, N. (2020). Shedding light on the shadows of informality: A meta-analysis of formalization interventions targeted at informal firms. Labour Economics, 67, 101925.
* Floridi et al. (2021a)

  Floridi, A., Demena, B. A., and Wagner, N. (2021). The bright side of formalization policies! Meta-analysis of the benefits of policy-induced versus self-induced formalization. Applied Economics Letters, 28(20), 1807-1812.
* Fontana and Sau (2025)

  Fontana, O., and Sau, L. (2025). Expansionary austerity in Europe: finally an oxymoron?. European Journal of Economics and Economic Policies: Intervention, 1-26. [doi:10.4337/ejeep.2025.0152](https://doi.org/10.4337/ejeep.2025.0152).
* Forster et al. (2020)

  Forster, T., Kentikelenis, A. E., Stubbs, T. H., and King, L. P. (2020). Globalization and health equity: The impact of structural adjustment programs on developing countries. Social Science & Medicine, 267, 112496.
* Fraga (2004)

  Fraga, A. (2004). Latin America since the 1990s: Rising from the Sickbed? Journal of Economic Perspectives, 18(2), 89–106. [doi:10.1257/0895330041371204](https://doi.org/10.1257/0895330041371204).
* Fraile (2009)

  FRAILE, L. (2009). Lessons from Latin America’s neo-liberal experiment: An overview of labour and social policies since the 1980s. International Labour Review, 148(3), 215-233. [doi:10.1111/j.1564-913x.2009.00059.x](https://doi.org/10.1111/j.1564-913x.2009.00059.x).
* Franchino (2019)

  Franchino, F. (2019). In search of the ideational foundations of EU fiscal governance: standard ideas, imperfect rules. Journal of European Integration, 42(2), 179-194. [doi:10.1080/07036337.2019.1657858](https://doi.org/10.1080/07036337.2019.1657858).
* Galofré-Vilà et al. (2017)

  Galofré-Vilà, G., Meissner, C., McKee, M., and Stuckler, D. (2017). Austerity and the Rise of the Nazi party. NBER. [doi:10.3386/w24106](https://doi.org/10.3386/w24106).
* García-Cicco et al. (2010)

  García-Cicco, J., Pancrazi, R., and Uribe, M. (2010). Real business cycles in emerging countries?. American Economic Review, 100(5), 2510-31.
* Gechert (2015)

  Gechert, S. (2015). What fiscal policy is most effective? a meta-regression analysis. Oxford Economic Papers, 67(3), 553-580.
* Gechert (2023)

  Gechert, S. (2023). Fiscal policy: post- or new keynesian?. European Journal of Economics and Economic Policies: Intervention, 20(2), 338-355.
* Gechert et al. (2018)

  Gechert, S., Horn, G., and Paetz, C. (2018). Long-term Effects of Fiscal Stimulus and Austerity in Europe. Oxford Bulletin of Economics and Statistics, 81(3), 647-666. [doi:10.1111/obes.12287](https://doi.org/10.1111/obes.12287).
* Gechert et al. (2022)

  Gechert, S., Havranek, T., Irsova, Z., and Kolcunova, D. (2022). Measuring capital-labor substitution: the importance of method choices and publication bias. Review of Economic Dynamics, 45, 55-82.
* Gechert and Heimberger (2022)

  Gechert, S., and Heimberger, P. (2022). Do corporate tax cuts boost economic growth? European Economic Review, 147, 104157.
* Gechert and Rannenberg (2018)

  Gechert, S., and Rannenberg, A. (2018). Which fiscal multipliers are regime-dependent? a meta-regression analysis. Journal of Economic Surveys, 32(4), 1160-1182.
* Gilles (2025)

  Gilles, F. (2025). Marginal employment as an incentive to find a regular job? A meta-regression analysis approach. TEPP Working Paper, N° 2025-5.
* Gindelsky et al. (2023)

  Gindelsky, M., Moulton, J., Wentland, K., and Wentland, S. (2023). When do property taxes matter? tax salience and heterogeneous policy effects. Journal of Housing Economics, 61, 101951.
* Glinavos (2008)

  Glinavos, I. (2008). Neoliberal Law: unintended consequences of market-friendly law reforms. Third World Quarterly, 29(6), 1087–1099. [doi:10.1080/01436590802201055](https://doi.org/10.1080/01436590802201055).
* Goldfajn et al. (2021)

  Goldfajn, I., Martínez, L., and Valdés, R. O. (2021). Washington Consensus in Latin America: From Raw Model to Straw Man. Journal of Economic Perspectives, 35(3), 109–132. [doi:10.1257/jep.35.3.109](https://doi.org/10.1257/jep.35.3.109).
* Gregor et al. (2021)

  Gregor, J., Melecký, A., and Melecký, M. (2021). Interest Rate Pass-Through: A Meta-Analysis of the Literature. Journal of Economic Surveys, 35(1), 141-191.
* Grier and Grier (2021)

  Grier, K. B., and Grier, R. M. (2021). The Washington consensus works: Causal effects of reform, 1970-2015. Journal of Comparative Economics, 49(1), 59–72. [doi:10.1016/j.jce.2020.09.001](https://doi.org/10.1016/j.jce.2020.09.001).
* Gunn et al. (2025)

  Gunn, V., Matilla-Santander, N., Kreshpaj, B., et al. (2025). A Systematic Review of Evaluated Labor Market Initiatives Addressing Precarious Employment: Findings and Public Health Implications. International Journal of Social Determinants of Health and Health Services, 55(3), 268-288.
* Güven (2018)

  Güven, A. B. (2018). Whither the post-Washington Consensus? International financial institutions and development policy before and after the crisis. Review of International Political Economy, 25(3), 392–417. [doi:10.1080/09692290.2018.1459781](https://doi.org/10.1080/09692290.2018.1459781).
* Havranek et al. (2020)

  Havranek, T., Irsova, Z., Laslopova, L., and Zeynalova, O. (2020). The Elasticity of Substitution between Skilled and Unskilled Labor: A Meta-Analysis. Working Paper.
* Hayami (2003)

  HAYAMI, Y. (2003). From the Washington Consensus to the Post-Washington Consensus: Retrospect and Prospect. Asian Development Review, 20(02), 40–65. [doi:10.1142/s0116110503000071](https://doi.org/10.1142/s0116110503000071).
* Heimberger (2020)

  Heimberger, P. (2020). Does employment protection affect unemployment? A meta-analysis. Oxford Economic Papers, 72(4), 920-945.
* Heimberger (2021)

  Heimberger, P. (2021). Corporate tax competition: A meta-analysis. European Journal of Political Economy, 69, 102002.
* Heimberger (2023a)

  Heimberger, P. (2023). Do higher public debt levels reduce economic growth?. Journal of Economic Surveys, 37(4), 1061-1089.
* Heimberger (2023b)

  Heimberger, P. (2023). The cyclical behaviour of fiscal policy: a meta-analysis. Economic Modelling, 123, 106259.
* Helgason (2019)

  Helgason, A. (2019). The Political Economy of Crisis Responses. In Welfare and the Great Recession (pp. 43-58). Oxford University Press. [doi:10.1093/oso/9780198830962.003.0003](https://doi.org/10.1093/oso/9780198830962.003.0003).
* Herzog and Jankin Mikhaylov (2019)

  Herzog, A., and Jankin Mikhaylov, S. (2019). Intra-cabinet politics and fiscal governance in times of austerity. Political Science Research and Methods, 8(3), 409-424. [doi:10.1017/psrm.2019.40](https://doi.org/10.1017/psrm.2019.40).
* Hornuf and Vrankar (2022)

  Hornuf, L., and Vrankar, D. (2022). Hourly Wages in Crowdworking: A Meta-Analysis. Business & Information Systems Engineering, 64(5), 553-573.
* Howard-Jones and Hölscher (2020)

  Howard-Jones, P., and Hölscher, J. (2020). The influence of the Washington Consensus programme on the transitional economies of Eastern Europe - a firm-level analysis. Economic Annals, 65(226), 9–44. [doi:10.2298/eka2026009h](https://doi.org/10.2298/eka2026009h).
* Huebscher et al. (2018)

  Huebscher, E., Sattler, T., and Wagner, M. (2018). Voter Responses to Fiscal Austerity. SSRN. [doi:10.2139/ssrn.3289341](https://doi.org/10.2139/ssrn.3289341).
* Hughes et al. (2020)

  Hughes, C., Sayce, S., Shepherd, E., and Wyatt, P. (2020). Implementing a land value tax: Considerations on moving from theory to practice. Land Use Policy, 94, 104494.
* Hutchison (2001)

  Hutchison, M. M. (2001). A cure worse than the disease? Currency crises and the output costs of IMF-supported stabilization programs. NBER Working Paper, 8305.
* Iorngurum (2025a)

  Iorngurum, T. D. (2025a). The exchange rate pass-through to domestic prices: A meta-analysis. Journal of Economic Surveys, 39, 1092-1124.
* Iorngurum (2025b)

  Iorngurum, T. D. (2025b). Asymmetric overnight rate pass-through to bank loan rates: A meta-analysis. Economic Modelling, 151, 107198.
* Irsova et al. (2024)

  Irsova, Z., Doucouliagos, H., Havranek, T., and Stanley, T. D. (2024). Meta-analysis of social science research: a practitioner’s guide. Journal of Economic Surveys, 38(5), 1547-1566.
* Iwasaki and Uegaki (2017)

  Iwasaki, I., and Uegaki, A. (2017). Central Bank Independence and Inflation in Transition Economies: A Comparative Meta-Analysis with Developed and Developing Economies. Eastern European Economics, 55(3), 197-235.
* Jacques (2020)

  Jacques, O. (2020). Austerity and the path of least resistance: how fiscal consolidations crowd out long-term investments. Journal of European Public Policy, 28(4), 551-570. [doi:10.1080/13501763.2020.1737957](https://doi.org/10.1080/13501763.2020.1737957).
* Jessen and Kluve (2021)

  Jessen, J., and Kluve, J. (2021). The effectiveness of interventions to reduce informality in low-and middle-income countries. World Development, 138, 105256.
* Jiménez Martínez and Jiménez Martínez (2021)

  Jiménez Martínez, M., and Jiménez Martínez, M. (2021). Are the effects of minimum wage on the labour market the same across countries? A meta-analysis spanning a century. Economic Systems, 45(2), 100849.
* Jordà and Taylor (2013)

  Jordà, Ò., and Taylor, A. (2013). The Time for Austerity: Estimating the Average Treatment Effect of Fiscal Policy. NBER. [doi:10.3386/w19414](https://doi.org/10.3386/w19414).
* Kalabikhina et al. (2024)

  Kalabikhina, I. E., Kuznetsova, P. O., and Zhuravleva, S. A. (2024). Size and factors of the motherhood penalty in the labour market: A meta-analysis. Population and Economics, 8(2), 178-205.
* Kaminsky and Reinhart (1999)

  Kaminsky, G. L., and Reinhart, C. M. (1999). The twin crises: the causes of banking and balance-of-payments problems. American Economic Review, 89(3), 473-500.
* Karger (2014)

  Karger, H. (2014). The Bitter Pill: Austerity, Debt, and the Attack on Europe’s Welfare States. The Journal of Sociology & Social Welfare, 41(2). [doi:10.15453/0191-5096.3949](https://doi.org/10.15453/0191-5096.3949).
* Kass-Hanna et al. (2023)

  Kass-Hanna, T., Reynaud, J., y Walker, C. (2023). Estimating Fiscal Multipliers Under Alternative Exchange Rate Regimes: The Case of Bolivia. IMF Working Paper, WP/23/240.
* Katsikas (2020)

  Katsikas, D. (2020). Fiscal Governance in the Eurozone: From Maastricht to crisis and back again?\*. Region & Periphery, (9), 83. [doi:10.12681/rp.23780](https://doi.org/10.12681/rp.23780).
* Kelsall and Hennings (2015)

  Kelsall, D., and Hennings, C. (2015). Austerity and fiscal prudence are health issues. Canadian Medical Association Journal, 187(14), 1029. [doi:10.1503/cmaj.150950](https://doi.org/10.1503/cmaj.150950).
* Kitromilides (2011)

  Kitromilides, Y. (2011). Deficit reduction, the age of austerity, and the paradox of insolvency. Journal of Post Keynesian Economics, 33(3), 517-536. [doi:10.2753/pke0160-3477330306](https://doi.org/10.2753/pke0160-3477330306).
* Klein Martins (2024)

  Klein Martins, G. (2024). Long-run Effects of Austerity: An Analysis of Size Dependence and Persistence in Fiscal Multipliers. Oxford Bulletin of Economics and Statistics, 87(2), 330-356. [doi:10.1111/obes.12646](https://doi.org/10.1111/obes.12646).
* Knaisch and Pöschel (2024)

  Knaisch, J., and Pöschel, C. (2024). Wage response to corporate income taxes: A meta-regression analysis. Journal of Economic Surveys, 38(3), 852-876.
* Knell and Stix (2005)

  Knell, M., and Stix, H. (2005). The Income Elasticity of Money Demand: A Meta-Analysis of Empirical Results. Journal of Economic Surveys, 19(3), 513-533.
* Kondo et al. (2009)

  Kondo, N., Sembajwe, G., Kawachi, I., van Dam, R. M., Subramanian, S. V., and Yamagata, Z. (2009). Income inequality, mortality, and self rated health: meta-analysis of multilevel studies. BMJ, 339, b4471.
* Koráb et al. (2023)

  Koráb, P., Fidrmuc, J., and Dibooglu, S. (2023). Growth and inflation tradeoffs of dollarization: Meta-analysis evidence. Journal of International Money and Finance, 137, 102915.
* Krogstad (2007)

  Krogstad, E. (2007). The Post-Washington Consensus: Brand New Agenda or Old Wine in a New Bottle? Challenge, 50(2), 67–85. [doi:10.2753/0577-5132500205](https://doi.org/10.2753/0577-5132500205).
* Krugman (1999)

  Krugman, P. (1999). Balance sheets, the transfer problem, and financial crises. In International finance and financial crises: essays in honor of robert p. flood, jr. (pp. 31-55). Springer, Dordrecht.
* Kumar (2014)

  Kumar, S. (2014). Money demand income elasticity in advanced and developing countries: new evidence from meta-analysis. Applied Economics, 46(16), 1873-1882.
* Kushi and McManus (2021)

  Kushi, S., and McManus, I. (2021). Gender, austerity and the welfare state. In Handbook on Austerity, Populism and the Welfare State. Edward Elgar Publishing. [doi:10.4337/9781789906745.00033](https://doi.org/10.4337/9781789906745.00033).
* Labonté (2012)

  Labonté, R. (2012). The austerity agenda: how did we get here and where do we go next?. Critical Public Health, 22(3), 257-265. [doi:10.1080/09581596.2012.687508](https://doi.org/10.1080/09581596.2012.687508).
* Lang (2021)

  Lang, V. (2021). The economics of the democratic deficit: The effect of IMF programs on inequality. The Review of International Organizations, 16, 599-623.
* Larson and Shui (2021)

  Larson, W. D. and Shui, J. (2021). Land valuation using public records and kriging: Implications for land versus property taxation in cities. FHFA Staff Working Paper.
* Levy Yeyati et al. (2025)

  Levy Yeyati, E., Montané, M., Sartorio, L., and Gauna, A. (2025). What Works for Active Labor Market Policies? A Meta-Analysis of RCT Findings. Economía LACEA Journal, 24(1), 81-104.
* Libanio (2020)

  Libanio, G. (2020). CARDIM DE CARVALHO AND THE POST KEYNESIANS ON FISCAL POLICY: THE ECONOMIC CONSEQUENCES OF AUSTERITY. Revista de Economia Contemporânea, 24(2). [doi:10.1590/198055272429](https://doi.org/10.1590/198055272429).
* Lloyd-Sherlock (1997)

  Lloyd-Sherlock, P. (1997). Policy, Distribution, and Poverty in Argentina Since Redemocratization. Latin American Perspectives, 24(6), 22–55. [doi:10.1177/0094582x9702400602](https://doi.org/10.1177/0094582x9702400602).
* Longhi et al. (2005)

  Longhi, S., Nijkamp, P., and Poot, J. (2005). A meta-analytic assessment of the effect of immigration on wages. Journal of Economic Surveys, 19(3), 451-477.
* López-Morales et al. (2024)

  López-Morales, E., Herrera, N., and Garretón, M. (2024). Neoliberal urban segregation and property tax: A critical view of Santiago, Chile. EPA: Economy and Space, 56(6), 1820-1840.
* Lora and Olivera (2005)

  Lora, E., and Olivera, M. (2005). The Electoral Consequences of the Washington Consensus. Inter-American Development Bank. [doi:10.18235/0010841](https://doi.org/10.18235/0010841).
* Lusiani and Chaparro (2018)

  Lusiani, N., and Chaparro, S. (2018). Assessing Austerity: Monitoring the Human Rights Impacts of Fiscal Consolidation. SSRN. [doi:10.2139/ssrn.3218609](https://doi.org/10.2139/ssrn.3218609).
* Mabelini Batista et al. (2022)

  Mabelini Batista, M., Carnut, L., and Mendes, A. (2022). El Consenso de Washington, vulnerabilidad externa y sobreexplotación del trabajo en América Latina: un análisis a la luz de la Teoría Marxista de la Dependencia [The Washington Consensus, external vulnerability and overexploitation of labor in Latin America: an analysis in light of the Marxist Theory of Dependency]. De Raíz Diversa. Revista Especializada en Estudios Latinoamericanos, 8(15), 73–109. [doi:10.22201/ppela.24487988e.2021.15.79707](https://doi.org/10.22201/ppela.24487988e.2021.15.79707).
* Mandon and Cazals (2019)

  Mandon, P., and Cazals, A. (2019). Political budget cycles: Manipulation by leaders versus manipulation by researchers? Evidence from a meta-regression analysis. Journal of Economic Surveys, 33(1), 274-308.
* Marangos (2008)

  Marangos, J. (2008). The Evolution of the Anti-Washington Consensus Debate: From ’Post-Washington Consensus’ to ’After the Washington Consensus’. Competition & Change, 12(3), 227-244. [doi:10.1179/102452908x320400](https://doi.org/10.1179/102452908x320400).
* Marangos (2021)

  Marangos, J. (2021). The Troika’s conditionalities during the Greek financial crisis of 2010-2014: the Washington Consensus is alive, well, and here to stay. European Journal of Economics and Economic Policies: Intervention, 18(3), 379–403. [doi:10.4337/ejeep.2021.0075](https://doi.org/10.4337/ejeep.2021.0075).
* Massey et al. (2006)

  Massey, D. S., R, M. S., and Behrman, J. R. (2006). Chronicle of a Myth Foretold: The Washington Consensus in Latin America. The ANNALS of the American Academy of Political and Social Science, 606(1), 6–7. [doi:10.1177/0002716206288386](https://doi.org/10.1177/0002716206288386).
* McKay (2013)

  McKay, J. (2013). After the Washington Consensus: Rethinking Dominant Paradigms and Questioning ’One Size Fits All’ Orthodoxies. In Critical Reflections on Development (pp. 50-68). Palgrave Macmillan UK. [doi:10.1057/9780230389052\_4](https://doi.org/10.1057/9780230389052_4).
* McManus (2015)

  McManus, R. (2015). Austerity versus stimulus: the polarizing effect of fiscal policy. Oxford Economic Papers, 67(3), 581-597. [doi:10.1093/oep/gpv023](https://doi.org/10.1093/oep/gpv023).
* McManus et al. (2019)

  McManus, R., Ozkan, F., and Trzeciakiewicz, D. (2019). Fiscal consolidations and distributional effects: which form of fiscal austerity is least harmful?. Oxford Economic Papers, 73(1), 317-349. [doi:10.1093/oep/gpz065](https://doi.org/10.1093/oep/gpz065).
* McMenamin et al. (2014)

  McMenamin, I., Breen, M., and Muñoz-Portillo, J. (2014). Austerity and credibility in the Eurozone. European Union Politics, 16(1), 45-66. [doi:10.1177/1465116514553487](https://doi.org/10.1177/1465116514553487).
* Mendoza and Yue (2012)

  Mendoza, E. G., and Yue, V. Z. (2012). A general equilibrium model of sovereign default and business cycles. The Quarterly Journal of Economics, 127(2), 889-946.
* Mirrlees et al. (2011)

  Mirrlees, J., Adam, S., Besley, T., Blundell, R., Bond, S., Chote, R., Gammie, M., Johnson, P., Myles, G., and Poterba, J. (2011). Tax by Design: The Mirrlees Review. Oxford University Press.
* Molina Díaz and Cachaga Herrera (2018)

  Molina Díaz, R., y Cachaga Herrera, P. (2018). Efectos asimétricos de la inversión pública sectorial sobre el crecimiento económico [Asymmetric effects of sectoral public investment on economic growth]. Documento de trabajo N.º 02/2018, Banco Central de Bolivia.
* Muellbauer (2024)

  Muellbauer, J. (2024). Why we need a green land-value tax and how to design it. SUERF Policy Brief No 806.
* Müller (2014)

  Müller, G. (2014). Fiscal Austerity and the Multiplier in Times of Crisis. German Economic Review, 15(2), 243-258. [doi:10.1111/geer.12027](https://doi.org/10.1111/geer.12027).
* Murphy and Seegert (2024)

  Murphy, D. and Seegert, N. (2024). Implicit Land Taxes and Their Effect on the Real Economy. Working Paper.
* Naim (2000)

  Naim, M. (2000). Fads and fashion in economic reforms: Washington Consensus or Washington Confusion? Third World Quarterly, 21(3), 505–528. [doi:10.1080/01436590050057753](https://doi.org/10.1080/01436590050057753).
* Nedoncelle et al. (2025)

  Nedoncelle, C., Marchal, L., Aubry, A., and Héricourt, J. (2025). Does Immigration Affect Native Wages? A Meta-Analysis. CEPII Working Paper, 2025-07.
* Nekiplov (2000)

  Nekiplov, A. (2000). The Washington Consensus and Russian Economic Policy. International Social Science Journal, 52(166), 467–477. [doi:10.1111/1468-2451.00277](https://doi.org/10.1111/1468-2451.00277).
* Nguyen et al. (2021)

  Nguyen, T., Papyrakis, E., and van Bergeijk, P. (2021). Publication bias in the price effects of monetary policy: A meta-regression analysis for emerging and developing economies. International Review of Economics and Finance, 71, 567-583.
* Nie (2020)

  Nie, O. (2020). Expansionary Fiscal Austerity: New International Evidence. World Bank. [doi:10.1596/1813-9450-9344](https://doi.org/10.1596/1813-9450-9344).
* Nielsson et al. (2024)

  Nielsson, U., Wroblewski, C., and Yding, A. (2024). The Incidence and Efficiency of Land Value Taxation. Working Paper.
* Nijkamp and Poot (2004)

  Nijkamp, P., and Poot, J. (2004). Meta-analysis of the effect of fiscal policies on long-run growth. European Journal of Political Economy, 20(1), 91-124.
* Nikolaidi and Stockhammer (2017)

  Nikolaidi, M., and Stockhammer, E. (2017). Minsky models: a structured survey. Journal of Economic Surveys, 31(5), 1304-1339.
* Nooruddin and Simmons (2006)

  Nooruddin, I., and Simmons, J. W. (2006). The politics of hard choices: IMF programs and government spending. International Organization, 60(4), 1001-1033.
* Nosrati et al. (2022)

  Nosrati, E., Dowd, J. B., Marmot, M., and King, L. P. (2022). Structural adjustment programmes and infectious disease mortality. PLoS ONE, 17(7), e0270344.
* Ortiz and Cummins (2013)

  Ortiz, I., and Cummins, M. (2013). The Age of Austerity: A Review of Public Expenditures and Adjustment Measures in 181 Countries. SSRN. [doi:10.2139/ssrn.2260771](https://doi.org/10.2139/ssrn.2260771).
* Ortiz and Cummins (2021)

  Ortiz, I., and Cummins, M. (2021). Global Austerity Alert: Looming Budget Cuts in 2021-25 and Alternative Pathways. SSRN. [doi:10.2139/ssrn.3856299](https://doi.org/10.2139/ssrn.3856299).
* Ortiz et al. (2011)

  Ortiz, I., Chai, J., and Cummins, M. (2011). Austerity Measures Threaten Children and Poor Households: Recent Evidence in Public Expenditures from 128 Developing Countries. SSRN. [doi:10.2139/ssrn.1934510](https://doi.org/10.2139/ssrn.1934510).
* Pana et al. (2025)

  Pana, S. Y., King, L. P., and Nosrati, E. (2025). IMF, Structural Adjustment, and Poverty: A Cross-National Difference-in-Differences. Working Paper Series, No 620.
* Papadamou et al. (2019)

  Papadamou, S., Kyriazis, N. A., and Tzeremes, P. G. (2019). Unconventional monetary policy effects on output and inflation: A meta-analysis. International Review of Financial Analysis, 61, 295-305.
* Pedroni et al. (2022)

  Pedroni, F. V., Pesce, G., and Briozzo, A. (2022). Why do Firms Operate Informally? Insights from a Systematic Literature Review. Innovar, 32(83), 121-138.
* Pereira (2016)

  Pereira, J. M. M. (2016). Recycling and expansion: an analysis of the World Bank agenda (1989–2014). Third World Quarterly, 37(5), 818-839. [doi:10.1080/01436597.2015.1113871](https://doi.org/10.1080/01436597.2015.1113871).
* Perugini et al. (2018)

  Perugini, C., Žarković Rakić, J., and Vladisavljević, M. (2018). Austerity and gender inequalities in Europe in times of crisis. Cambridge Journal of Economics, 43(3), 733-767. [doi:10.1093/cje/bey044](https://doi.org/10.1093/cje/bey044).
* Pi Ferrer and Alasuutari (2019)

  Pi Ferrer, L., and Alasuutari, P. (2019). The Spread and Domestication of the Term “Austerity: Evidence from the Portuguese and Spanish Parliaments. Politics & Policy, 47(6), 1039-1065. [doi:10.1111/polp.12331](https://doi.org/10.1111/polp.12331).
* Picchio and Ubaldi (2024)

  Picchio, M., and Ubaldi, M. (2024). Unemployment and health: A meta-analysis. Journal of Economic Surveys, 38, 1437-1472.
* Pieper and Taylor (1998)

  Pieper, U., and Taylor, L. (1998). The revival of the liberal creed: the IMF, the World Bank, and inequality in a globalized economy. In Globalization and Progressive Economic Policy (pp. 37-63). Cambridge University Press. [doi:10.1017/cbo9780511599095.002](https://doi.org/10.1017/cbo9780511599095.002).
* Plummer (2010)

  Plummer, E. (2010). Evidence on the distributional effects of a land value tax on residential households. National Tax Journal, 63(1), 63–92.
* Prante et al. (2020)

  Prante, F., Bramucci, A., and Truger, A. (2020). Decades of Tight Fiscal Policy Have Left the Health Care System in Italy Ill-Prepared to Fight the COVID-19 Outbreak. Intereconomics, 55(3), 147-152. [doi:10.1007/s10272-2020-0886-0](https://doi.org/10.1007/s10272-020-0886-0).
* Raudla et al. (2015)

  Raudla, R., Douglas, J., Randma-Liiv, T., and Savi, R. (2015). The Impact of Fiscal Crisis on Decision-Making Processes in European Governments: Dynamics of a Centralization Cascade. Public Administration Review, 75(6), 842-852. [doi:10.1111/puar.12381](https://doi.org/10.1111/puar.12381).
* Rayl (2020)

  Rayl, N. (2020). Cost of Austerity: Effect of Fiscal Consolidation in Europe Post 2010. SSRN. [doi:10.2139/ssrn.3596470](https://doi.org/10.2139/ssrn.3596470).
* Rodrik (2008)

  Rodrik, D. (2008). Goodbye Washington Consensus, hello Washington confusion?: A review of the World Bank’s ’Economic growth in the 1990s: Learning from a decade of reform’. Panoeconomicus, 55(2), 135–156. [doi:10.2298/pan0802135r](https://doi.org/10.2298/pan0802135r).
* Rodríguez Echeverría (2008)

  Rodríguez Echeverría, M. Á. (2008). Menos pobres, más resistentes, pero falta mucho camino por andar. Los últimos 20 años de América Latina [Fewer poor, more resilient, but still a long way to go. The last 20 years of Latin America]. Revista de Ciencias Económicas. [doi:10.15517/rce.v26i1.7163](https://doi.org/10.15517/rce.v26i1.7163).
* Saltkjel et al. (2017b)

  Saltkjel, T., Holm Ingelsrud, M., Dahl, E., and Halvorsen, K. (2017b). A fuzzy set approach to economic crisis, austerity and public health. Part II: How are configurations of crisis and austerity related to changes in population health across Europe?. Scandinavian Journal of Public Health, 45(18\_suppl), 48-55. [doi:10.1177/1403494817707125](https://doi.org/10.1177/1403494817707125).
* Sambanis et al. (2022)

  Sambanis, N., Nikolova, E., and Schultz, A. (2022). The effects of economic austerity on prosociality: Evidence from Greece. European Union Politics, 23(4), 567-589. [doi:10.1177/14651165221120527](https://doi.org/10.1177/14651165221120527).
* Sapir (2000)

  Sapir, J. (2000). The Washington Consensus and Transition In Russia: History of a Failure. International Social Science Journal, 52(166), 479–491. [doi:10.1111/1468-2451.00278](https://doi.org/10.1111/1468-2451.00278).
* Saray (2019)

  Saray, M. O. (2019). Washington Uzlaşısı, Neo-Liberalizm ve Sonrası: Pekin Uzlaşısı Ezber mi Bozuyor? [The Washington Consensus, Neoliberalism and After: Is the Beijing Consensus Breaking the Mold?]. Journal of Yaşar University, 14(55), 299–317. [doi:10.19168/jyasar.540111](https://doi.org/10.19168/jyasar.540111).
* Schlosser (2019)

  Schlosser, P. (2019). Europe’s New Fiscal Union. Springer. [doi:10.1007/978-3-319-98636-4](https://doi.org/10.1007/978-3-319-98636-4).
* Schwerhoff et al. (2022)

  Schwerhoff, G., Edenhofer, O., and Fleurbaey, M. (2022). Equity and Efficiency Effects of Land Value Taxation. IMF Working Paper WP/22/263.
* Seidman (2012)

  Seidman, L. (2012). Keynesian stimulus versus classical austerity. Review of Keynesian Economics, 1(0), 77-92. [doi:10.4337/roke.2012.01.05](https://doi.org/10.4337/roke.2012.01.05).
* Semmler and Semmler (2013)

  Semmler, W., and Semmler, A. (2013). The Macroeconomics of Fiscal Consolidation in the European Union. SSRN. [doi:10.2139/ssrn.2320198](https://doi.org/10.2139/ssrn.2320198).
* Shimonovich et al. (2024)

  Shimonovich, M., Campbell, M., Thomson, R. M., Broadbent, P., Wells, V., Kopasker, D., and Katikireddi, S. V. (2024). Causal Assessment of Income Inequality on Self-Rated Health and All-Cause Mortality: A Systematic Review and Meta-Analysis. The Milbank Quarterly, 102(1), 141-182.
* Sindzingre (2014)

  Sindzingre, A. N. (2014). Whatever Inconsistencies and Effects? Explaining the Resilience of the Policy Reforms Applied to Developing Countries. Forum for Social Economics, 44(2), 159-178. [doi:10.1080/07360932.2014.951378](https://doi.org/10.1080/07360932.2014.951378).
* Sintos (2023)

  Sintos, A. (2023). Does inflation worsen income inequality? A meta-analysis. Economic Systems, 47, 101146.
* Sokolova and Sorensen (2021)

  Sokolova, A., and Sorensen, T. (2021). Monopsony in labor markets: A meta-analysis. ILR Review, 74(1), 27-55.
* Solimano (1999)

  Solimano, A. (1999). Beyond Unequal Development: An Overview. The World Bank. [doi:10.1596/1813-9450-2091](https://doi.org/10.1596/1813-9450-2091).
* Srinivasan (2000)

  Srinivasan, T. N. (2000). The Washington Consensus a Decade Later: Ideology and the Art and Science of Policy Advice. The World Bank Research Observer, 15(2), 265–270. [doi:10.1093/wbro/15.2.265](https://doi.org/10.1093/wbro/15.2.265).
* Stanley (1998)

  Stanley, T. D. (1998). New wine in old bottles: a meta-analysis of ricardian equivalence. Southern Economic Journal, 64(3), 713-727.
* Stanley (2001)

  Stanley, T. D. (2001). Wheat from chaff: Meta-analysis as quantitative literature review. Journal of Economic Perspectives, 15(3), 131–150.
* Stanley (2016)

  Stanley, L. (2016). Governing austerity in the United Kingdom: anticipatory fiscal consolidation as a variety of austerity governance. Economy and Society, 45(3-4), 303-324. [doi:10.1080/03085147.2016.1224145](https://doi.org/10.1080/03085147.2016.1224145).
* Stanley and Doucouliagos (2012)

  Stanley, T. D., and Doucouliagos, H. (2012). Meta-regression analysis in economics and business. Routledge.
* Steelman (2021)

  Steelman, T. (2021). Do Voters Support Austerity Measures in Times of Economic Crisis? For Many Voters, the Answer is Yes. Political Science Today, 1(3), 7. [doi:10.1017/psj.2021.52](https://doi.org/10.1017/psj.2021.52).
* Stiglitz (2000)

  Stiglitz, J. E. (2000). What I Learned at the World Economic Crisis. The New Republic.
* Stiglitz (2005)

  Stiglitz, J. E. (2005). More Instruments and Broader Goals: Moving toward the Post-Washington Consensus. In Wider Perspectives on Global Development (pp. 16–48). Palgrave Macmillan UK. [doi:10.1057/9780230501850\_2](https://doi.org/10.1057/9780230501850_2).
* Stournaras (2012)

  Stournaras, C. F. (2012). Fiscal Austerity as the Achilles’ Heel to Socio-Economic Prosperity. SSRN. [doi:10.2139/ssrn.2111896](https://doi.org/10.2139/ssrn.2111896).
* Stubbs et al. (2017)

  Stubbs, T., Kentikelenis, A., Stuckler, D., McKee, M., and King, L. (2017). The impact of IMF conditionality on government health expenditure: A cross-national analysis of 16 West African nations. Social Science & Medicine, 174, 220-227.
* Stubbs et al. (2020)

  Stubbs, T., Reinsberg, B., Kentikelenis, A., and King, L. (2020). How to evaluate the effects of IMF conditionality. The Review of International Organizations, 15, 29-73.
* Svampa (2015)

  Svampa, M. (2015). Commodities Consensus: Neoextractivism and Enclosure of the Commons in Latin America. South Atlantic Quarterly, 114(1), 65–82. [doi:10.1215/00382876-2831290](https://doi.org/10.1215/00382876-2831290).
* Szkup (2020)

  Szkup, M. (2020). Preventing Self-fulfilling Debt Crises: A Global Games Approach. SSRN. [doi:10.2139/ssrn.3527210](https://doi.org/10.2139/ssrn.3527210).
* Talving (2018)

  Talving, L. (2018). The electoral consequences of austerity: economic policy voting in Europe in times of crisis. In Electoral Rules and Electoral Behaviour (pp. 58-81). Routledge. [doi:10.4324/9781351273527-4](https://doi.org/10.4324/9781351273527-4).
* Tewari (2024)

  Tewari, S. (2024). The effect of telecommuting on productivity: a meta-analysis. Academy of Marketing Studies Journal, 27(4), 1-7.
* Thomson et al. (2017)

  Thomson, M., Kentikelenis, A., and Stubbs, T. (2017). Structural adjustment programmes adversely affect vulnerable populations: a systematic-narrative review of their effect on child and maternal health. Public Health Reviews, 38, 13.
* Tito Castillo (2024)

  Tito Castillo, P. E. (2024). Bolivia: Una mirada al rol de la inversión pública y su efecto sobre la inversión privada [Bolivia: A look at the role of public investment and its effect on private investment]. Tesis de Magíster, Universidad de Chile.
* Toffolutti and Suhrcke (2019)

  Toffolutti, V., and Suhrcke, M. (2019). Does austerity really kill?. SocArXiv. [doi:10.31235/osf.io/b2t4x](https://doi.org/10.31235/osf.io/b2t4x).
* Ulyssea (2020)

  Ulyssea, G. (2020). Informality: Causes and consequences for development. Annual Review of Economics, 12, 525-546.
* Unda and Moreno (2015)

  Unda, M. and Moreno, C. (2015). La recaudación del impuesto predial en México: un análisis de sus determinantes económicos en el período 1969-2010 [Property tax collection in Mexico: an analysis of its economic determinants in the period 1969-2010]. Revista Mexicana de Ciencias Políticas y Sociales, 60(225), 45–78.
* Valdivia Coria and Carlo Santos (2021)

  Valdivia Coria, J. D., y Carlo Santos, J. C. (2021). Efectos de la inversión pública y privada en el crecimiento económico de Bolivia [Effects of public and private investment on the economic growth of Bolivia]. Revista de Análisis, 34, 55-86.
* van der Hoeven and Saget (2004)

  van der Hoeven, R., and Saget, C. (2004). Labour Market Institutions and Income Inequality: What are the New Insights after the Washington Consensus? In Inequality, Growth and Poverty in an Era of Liberalization and Globalization (pp. 197–220). Oxford University Press. [doi:10.1093/0199271410.003.0008](https://doi.org/10.1093/0199271410.003.0008).
* Vegh and Vuletin (2014)

  Vegh, C., and Vuletin, G. (2014). Social Implications of Fiscal Policy Responses During Crises. NBER. [doi:10.3386/w19828](https://doi.org/10.3386/w19828).
* Velickovski and Pugh (2011)

  Velickovski, I., and Pugh, G. T. (2011). Constraints on exchange rate flexibility in transition economies: a meta-regression analysis of exchange rate pass-through. Applied Economics, 43(27), 4111-4125.
* Vreeland (2003)

  Vreeland, J. R. (2003). The IMF and Economic Development. Cambridge University Press.
* White (2019)

  White, H. (2019). The twenty-first century experimenting society: the four waves of the evidence revolution. Palgrave Communications, 5(1). [doi:10.1057/s41599-019-0253-6](https://doi.org/10.1057/s41599-019-0253-6).
* Williamson (1996)

  Williamson, J. (1996). Lowest Common Denominator or Neoliberal Manifesto? The Polemics of the Washington Consensus. In Challenging the Orthodoxies (pp. 13–22). Palgrave Macmillan UK. [doi:10.1007/978-1-349-13992-7\_2](https://doi.org/10.1007/978-1-349-13992-7_2).
* Zigraiova et al. (2021)

  Zigraiova, D., Havranek, T., Irsova, Z., and Novak, J. (2021). How puzzling is the forward premium puzzle? A meta-analysis. European Economic Review, 134, 103714.