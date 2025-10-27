---
authors:
- Emilio Barucci
- Andrea Gurgone
- Giulia Iori
- Michele Azzone
doc_id: arxiv:2510.21071v1
family_id: arxiv:2510.21071
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based
  Model
url_abs: http://arxiv.org/abs/2510.21071v1
url_html: https://arxiv.org/html/2510.21071v1
venue: arXiv q-fin
version: 1
year: 2025
---


Emilio Barucci
Department of Mathematics, Politecnico di Milano, emilio.barucci@polimi.it 

Andrea Gurgone111The support from the UKRI Grant entitled ”The Large Agent Collider: Robust agent-based modelling as scale” awarded to Prof. Wooldridge (reference EP/W002949/1) is gratefully acknowledged. In addition, the authors would like to acknowledge the use of the University of Oxford Advanced Research Computing (ARC) facility in carrying out this work. <http://dx.doi.org/10.5281/zenodo.22558>
Department of Computer Science, University of Oxford, andrea.gurgone@cs.ox.ac.uk
Institute for New Economic Thinking, University of Oxford

Giulia Iori
Department of Economics, Ca’ Foscari University of Venice, giulia.iori@unive.it
Department of Economics, City St. George’s, University of London

Michele Azzone
Department of Mathematics, Politecnico di Milano, emilio.barucci@polimi.it

###### Abstract

We analyze financial stability and welfare impacts associated with the introduction of a Central Bank Digital Currency (CBDC) in a macroeconomic agent-based model. The model considers firms, banks, and households interacting on labour, goods, credit, and interbank markets. Households move their liquidity from deposits to CBDC based on the perceived riskiness of their banks.
We find that the introduction of CBDC exacerbates bank-runs and may lead to financial instability phenomena. The effect can be changed by introducing a limit on CBDC holdings. The adoption of CBDC has little effect on macroeconomic variables but the interest rate on loans to firms goes up and credit goes down in a limited way. CBDC leads to a redistribution of wealth from firms and banks to households with a higher bank default rate.
CBDC may have negative welfare effects, but a bound on holding enables a welfare improvement.

Keywords:Agent-Based Model; Central Bank Digital Currency; Financial Stability, Bank-run.

JEL Classification: E42, E44, E47, E52, E58, G01, G21, G28

††Corresponding author andrea.gurgone@cs.ox.ac.uk

## 1 Introduction

The debate on issuing retail Central Bank Digital Currency (CBDC) focuses primarily on welfare and financial stability implications.
The literature has highlighted the main trade-off. On one hand, CBDC aligns with citizens’ preferences for digital payments with more efficient exchanges; on the other hand, there are concerns regarding the substitution of deposits with digital money, which may lead to financial disintermediation, negative effects for the real economy, and instability under stress.

The existing literature on CBDC highlights that a careful design is required to find the balance along the above trade-off, see Agur et al.,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib2)); Andolfatto,  ([2021](https://arxiv.org/html/2510.21071v1#bib.bib4)); Assenmacher et al.,  ([2021](https://arxiv.org/html/2510.21071v1#bib.bib5)); Brunnermeier and Niepelt,  ([2019](https://arxiv.org/html/2510.21071v1#bib.bib11)); Keister and Monnet,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib24)); Keister and Sanches,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib25)); Kim and Kwon,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib26)); [Williamson, 2022b](https://arxiv.org/html/2510.21071v1#bib.bib34) ; [Williamson, 2022a](https://arxiv.org/html/2510.21071v1#bib.bib33) . In this paper, we contribute to this debate through the analysis of an agent-based model inspired by Delli Gatti et al.,  ([2011](https://arxiv.org/html/2510.21071v1#bib.bib14)), see also Gurgone and Iori,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib21)); Gurgone et al.,  ([2018](https://arxiv.org/html/2510.21071v1#bib.bib22)).
We focus on flight-to-quality by households who may substitute deposits with CBDC. They substitute deposits with CBDC on the basis of the riskiness of their banks, fearing that they may default. Unlike the analysis provided in the above papers, the agent-based model allows us, at the same time, to endogenously determine the riskiness of banks, the bank-run of depositors switching from deposits to CBDC, and the default of banks. This feature of the model allows us to evaluate the financial stability and welfare implications associated with CBDC in a more comprehensive way than the previous literature.

Extensive household adoption of CBDC could cause financial disintermediation, resulting in negative welfare effects.
Remuneration of CBDC and bounds to its adoption play a key role in keeping this potential problem under control.
Agur et al.,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib2)); Keister and Sanches,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib25)) show that non positive remuneration can help mitigate financial disintermediation. Andolfatto,  ([2021](https://arxiv.org/html/2510.21071v1#bib.bib4)) predicts a zero uptake of CBDC if its remuneration is below that of reserves held by the Central Bank (CB).
In the Euro area, Burlon et al.,  ([2024](https://arxiv.org/html/2510.21071v1#bib.bib12)) estimate that the welfare-maximizing amount of CBDC lies between 15 and 45% of quarterly GDP in equilibrium, assuming a non positive remuneration scheme and holding bounds.
Adalid et al.,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib1)) demonstrate that introducing a holding limit – such as the €3,000 cap per CBDC account currently envisaged for the digital euro – would allow aggregate CBDC holdings to reach an amount comparable to the current stock of cash (approximately one trillion euros) without generating significant disruptions to the banking system or the broader economy. Commercial banks could meet the resulting demand for CBDC by utilizing their existing reserves and by adjusting their liquidity positions through the interbank market.
The need to impose a bound on holdings seems to be a key ingredient for a safe introduction of CBDC with a limited effect on bank profitability, see Azzone and Barucci,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib7)); Nyffenegger,  ([2024](https://arxiv.org/html/2510.21071v1#bib.bib29)).

As far as financial stability is concerned, several papers point out that CBDC effectively increases the probability of a bank-run because depositors may easily switch to a safe asset under financial stress, but the welfare consequences are not so obvious.
[Williamson, 2022a](https://arxiv.org/html/2510.21071v1#bib.bib33)  shows that a bank-run with CBDC is more likely but it will hurt households less than in the case where only physical currency is in place because households can use CBDC to perform transactions in more situations. In other words, banking panics are more frequent but are less disruptive.
Keister and Monnet,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib24)) show that the increased risk of bank-runs associated with CBDC introduction can be mitigated by two mechanisms. First, banks are likely to reduce their maturity transformation, making them less vulnerable to runs. Second, by monitoring the flow of funds into CBDC, policymakers can identify and intervene in weak banks at an earlier stage.
Kim and Kwon,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib26)) show that CBDC may lead to a more resilient financial system if the CB lends the deposits in the CBDC account to banks. In a bank-run model, Fernández-Villaverde et al.,  ([2021](https://arxiv.org/html/2510.21071v1#bib.bib18)) show that the CB has the capability to deter runs and may become a monopolist for deposits, endangering credit supply to the real economy.
Ahnert et al.,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib3)) extend the Diamond and Dybvig,  ([1983](https://arxiv.org/html/2510.21071v1#bib.bib15)) model to a setting including the CBDC. The bank-run analysis is performed through a global games approach showing that the relationship between bank fragility and CBDC remuneration is U-shaped.

In our model, we abstract from remuneration of CBDC, which is set to be equal to the deposit rate and we also abstract from anonymity/digitalization features and network effects of CBDC as modeled in Barucci et al.,  ([2025](https://arxiv.org/html/2510.21071v1#bib.bib8)). We concentrate on the flight-to-quality phenomenon, with depositors transferring their liquidity to CBDC depending on the riskiness of their banks. As far as we know, this is the first paper addressing the connection between bank specific riskiness and adoption of CBDC in an endogenous way. In the existing literature, a bank-run is considered in the spirit of Diamond and Dybvig,  ([1983](https://arxiv.org/html/2510.21071v1#bib.bib15)): Fernández-Villaverde et al.,  ([2021](https://arxiv.org/html/2510.21071v1#bib.bib18)); [Williamson, 2022b](https://arxiv.org/html/2510.21071v1#bib.bib34)  consider bank-run as a self-fulfilling prophecy; in Keister and Monnet,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib24)); Kim and Kwon,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib26)); Ahnert et al.,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib3)) bank weakness is driven by an exogenous variable. In all of these papers, withdrawal of deposits is not related to the real economy. Instead, in our setting, a bank-run towards CBDC is motivated by the riskiness of banks which reflects conditions of the whole economy.

Adalid et al.,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib1)) provides the most similar analysis to ours simulating the introduction of CBDC on real data for the Euro area. They assume that when the run has been triggered, citizens substitute some of their deposits with CBDC. The decision is 0−10-1 and the probability of bank default, which is exogenous, increases over time. Heterogeneity is introduced assuming a normally distributed idiosyncratic component specific to each agent.
If demand of CBDC is unconstrained, then the scale and the speed of a system wide bank-run would increase. A hard limit on individual CBDC holdings would avoid the rise of a system wide bank-run.

In our setting, we investigate whether the possibility to substitute deposits for CBDC may ignite a system wide bank-run with a cascade of bank defaults and negative welfare implications.

We consider five different rules determining the fraction of deposits converted into CBDC: flat fraction (CBDC0 rule), fraction dependent on bank’s riskiness with a loose upper-bound (CBDC1 rule) yielding almost unconstrained substitution, fraction dependent on bank’s riskiness with a tight upper-bound (CBDC2 and 3 rule) and a deposit insurance scheme (CBDC4 rule).
The first two rules represent our central scenarios: fixed fraction (an amount of CBDC similar to cash) and conversion driven by a flight-to-quality fearing the default of banks.
CBDC2-4 rules allow us to investigate the role played by bounds on the adoption of CBDC and deposit insurance schemes. The model is calibrated for the Euro area.

Assuming a fixed 10% fraction of deposits converted into CBDC (CBDC0 rule), the substitution of deposits for CBDC has limited effects on the macroeconomy (real GDP and unemployment), but the interest rate of loans of banks to firms goes up and credit to firms goes down in a limited way.
When deposits are substituted based on banks’ risk profiles and a relatively loose upper bound is applied (CBDC1 rule), the model yields, on average, pronounced negative effects and heightened volatility.
Introducing a bound on CBDC adoption, together with a deposit insurance scheme, effectively mitigates these effects, producing outcomes similar to those observed under the CBDC0 rule.

CBDC leads to a redistribution of wealth from firms and banks to households, and to a higher banks’ default rate. Banks cope with households’ requests by exchanging liquidity among themselves in the interbank market and interbank lending goes up significantly. The increase of bank defaults is due to a stronger transmission in the interbank market (banks-banks default) and the liquidation of assets by banks.

Our analysis shows that unconstrained CBDC adoption may significantly hinder the economy with a lower growth rate and more pronounced fluctuations. CBDC may ignite a digital bank-run hampering financial stability. However, a reasonable bound on CBDC adoption (30% of deposits) renders almost no effect in comparison to the economy without CBDC.

The optimal amount of CBDC intake by households is evaluated through a social welfare analysis. Varying the upper-bound on CBDC adoption, we are able to show that a 40% bound on the fraction of deposits converted into CBDC seems to be the optimal choice. It seems that social welfare is negatively affected only in case of a massive conversion of deposits into CBDC.

The paper is organized as follows. In Section [2](https://arxiv.org/html/2510.21071v1#S2 "2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we present the model with five subsections dealing with households, labour market, government and central bank, business sector, banking sector.
In Section [3](https://arxiv.org/html/2510.21071v1#S3 "3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we consider different rules concerning the adoption of CBDC. In Section [4](https://arxiv.org/html/2510.21071v1#S4 "4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we provide and discuss the simulations. In Section [5](https://arxiv.org/html/2510.21071v1#S5 "5 Social Welfare Evaluation ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we develop the social welfare analysis. In Section [7](https://arxiv.org/html/2510.21071v1#S7 "7 Conclusions ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we draw our conclusions.

## 2 The model

The model builds on the one proposed in Gurgone and Iori,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib21)). The main differences are related to the introduction of CBDC which affects the allocation of wealth by households and the balance sheets of banks and CB.

The economy consists of five types of agents: households, firms, banks, government, and CB. Interactions occur in different markets: firms and households meet in the goods and labour markets; firms borrow from banks in the credit market; banks exchange liquidity in the interbank market. The CB buys government-issued debt securities (bonds) in the bond market. The government’s role is limited to making transfer payments to households, funded by taxes, or issuing government bonds. The CB creates liquidity by purchasing government bonds. On the liability side it holds bank reserves and CBDC. Households earn income from wages, assets, and transfers, which they use for consumption, asset accumulation (deposits and CBDC), and to pay taxes. They are represented by a trade union in wage negotiations and own shares of firms and banks, receiving dividends as asset income. Firms borrow from banks to pay wages, hire workers, produce, and sell goods. Banks hold government bonds, provide credit under regulatory constraints and manage liquidity through the interbank market.

### 2.1 Households

The household sector is made up of NHN^{H} units indexed by ii. The net wealth (n​wnw) of the ii-th household consists of its holdings of deposits and CBDC:

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​wi,tH=Di,tH+C​B​D​Ci,t,nw^{H}\_{i,t}=D\_{i,t}^{H}+CBDC\_{i,t}\;\;, |  | (1) |

The law of motion of net wealth is

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​wi,tH=n​wi,t−1H+Si,tH,nw^{H}\_{i,t}=nw^{H}\_{i,t-1}+S\_{i,t}^{H}\;\;, |  | (2) |

where saving Si,tHS\_{i,t}^{H} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Si,tH\displaystyle S\_{i,t}^{H} | =Di,t−1H​rD+C​B​D​Ci,t−1​rC​B​D​C\displaystyle=D\_{i,t-1}^{H}r^{D}+CBDC\_{i,t-1}r^{CBDC} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−θH)​(Wt−1​Ni,t−1H+∑k=f,bδtk​Πi,t−1k)−Ci,t−1+GtNH.\displaystyle+(1-\theta^{H})\left(W\_{t-1}N^{H}\_{i,t-1}+\sum\_{k=f,b}\delta^{k}\_{t}\Pi^{k}\_{i,t-1}\right)-C\_{i,t-1}+\frac{G\_{t}}{N^{H}}. |  | (3) |

The disposable income of households at the beginning of period tt is given by the flow of interest on deposits held in the previous period (Di,t−1H​rDD\_{i,t-1}^{H}r^{D}), interest on CBDC held in the previous period (C​B​D​Ci,t−1​rC​B​D​CCBDC\_{i,t-1}r^{CBDC}), the income available at the end of the period t−1t-1 taxed at the rate θH\theta^{H} plus the government transfers to households in tt (GtNH\frac{G\_{t}}{N^{H}}).
Income at time t−1t-1 is made up of worked hours NHN^{H} multiplied by the wage rate WW plus the dividend
share δk\delta^{k} of net profits of firms and
banks Πk\Pi^{k}, k=f,bk=f,b, where ff and bb respectively refer to firms and banks. Saving at the beginning of period tt is given by disposable income minus consumption at the end of period t−1t-1 (Ci,t−1C\_{i,t-1}).

As far as consumption is concerned, a permanent income rule is considered: household ii wants to consume a fraction c1c\_{1} of labour income plus government transfers and a fraction c2c\_{2} of wealth:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci,td=c1​[(1−θH)​Wt​Ni,tH+GtNH]+c2​n​wi,tH.C\_{i,t}^{d}=c\_{1}\left[(1-\theta^{H})W\_{t}N^{H}\_{i,t}+\frac{G\_{t}}{N^{H}}\right]+c\_{2}nw^{H}\_{i,t}\;\;. |  | (4) |

Consumption in ([4](https://arxiv.org/html/2510.21071v1#S2.E4 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) represents the desired spending level for the household. If they are rationed in the goods market, see Section [2.3](https://arxiv.org/html/2510.21071v1#S2.SS3 "2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), then they are left with involuntary saving, which is added to their stock of deposits and CBDC.

Each household is matched to several banks, see Section [D.2](https://arxiv.org/html/2510.21071v1#A4.SSS2 "D.2 Networks topology ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"). The amount of net wealth that household ii allocates to bank hh is given by the fraction wihw\_{i}^{h}; the weights are constant over time and sum to 11, ∑hwih=1\sum\_{h}w\_{i}^{h}=1.
A fraction of the deposits in bank hh is converted to CBDC according to a rule that depends on the leverage of the bank:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​B​D​Ci,th=ψ​(R​Mh,t)​wih​n​wi,tH.CBDC^{h}\_{i,t}=\psi(RM\_{h,t})w\_{i}^{h}nw^{H}\_{i,t}\;\;. |  | (5) |

where R​Mh,tRM\_{h,t} is a leverage risk measure of the bank hh to which the household ii is matched as depositor, see Section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"):
222The leverage ratio is defined as assets divided by equity, in our setting bank’s equity is n​wh,tBnw^{B}\_{h,t}, assets are
Rh,t+∑j=1NFLh​j,t−1+∑q=1NBIh​q,t−1l+BthR\_{h,t}+\sum\_{j=1}^{N^{F}}L\_{hj,t-1}+\sum\_{q=1}^{N^{B}}I^{l}\_{hq,t-1}+B\_{t}^{h}. Then R​Mh,tRM\_{h,t} is the leverage ratio minus 1.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​Mh,t=Dh,tB+∑z=1ZIz​h,t−1bn​wh,tB,RM\_{h,t}=\frac{D\_{h,t}^{B}+\sum\_{z=1}^{Z}I^{b}\_{zh,t-1}}{nw^{B}\_{h,t}}\;\;, |  | (6) |

C​B​D​Ci,thCBDC^{h}\_{i,t} denotes the amount of liquidity withdrawn from bank hh by household ii and converted into CBDC. The holding of CBDC by household ii is

|  |  |  |
| --- | --- | --- |
|  | C​B​D​Ci,t=∑hC​B​D​Ci,th.CBDC\_{i,t}=\sum\_{h}CBDC^{h}\_{i,t}\;\;. |  |

Notice that the allocation between deposits and CBDC concerns the wealth stock and not saving. In Section [4](https://arxiv.org/html/2510.21071v1#S4 "4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we provide a detailed description of the function ψ​(R​Mh,t)\psi(RM\_{h,t}) in ([5](https://arxiv.org/html/2510.21071v1#S2.E5 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), which governs the transfer of liquidity to CBDC.
The hypothesis that the substitution of deposits with CBDC is driven by the leverage ratio of the bank is inspired by bank-run models such as Gertler and Kiyotaki,  ([2015](https://arxiv.org/html/2510.21071v1#bib.bib19)).

#### 2.1.1 The labour market

The labour supply is given by the number of households. Each of them provides one unit of labour inelastically, and, therefore, each household corresponds to one worker. As the labour supply is perfectly inelastic, employment is determined by the demand of firms. Workers are homogeneous, they share the same skills and productivity.

Firms adjust their labour input to their target labour demand defined in ([13](https://arxiv.org/html/2510.21071v1#S2.E13 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) by hiring or firing workers.
Firms and workers are matched at t=0t=0, then firms seeking to expand the workforce retain all current employed workers and try to hire additional ones from the pool of unemployed workers. In case of excess aggregate labour demand, available workers are hired proportionally to firms’ individual demands.
If labour demand falls short of the current number of employed workers, firms fire workers, who become job seekers. Job seekers strive to return to employment by applying for new jobs.

The matching mechanism regulating the transition from unemployment to employment follows a binomial probability model by which a job seeker can successfully secure a new job within a predetermined number of attempts per unit of time, see Section [A.3](https://arxiv.org/html/2510.21071v1#A1.SSS3 "A.3 Labour market ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"). The same mechanism applies for the matching at t=0t=0. The mechanism creates involuntary unemployment as not all job seekers return to employment immediately, preventing the unemployment rate from unrealistically dropping to zero.

The wage rate WW is determined by a representative trade union of all workers. We assume that the wage rate adjusts sluggishly, based on an adaptive mechanism, to prevent the wage from jumping up or down sharply: the wage decreases (increases) when unemployment is above (below) a target unemployment rate u⋆u^{\star}. The mechanism is a stylized representation of wage dynamics,
wages move upward when the economy tends to full employment and downward when the unemployment rate is high.

We assume that the wage rate evolves as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt={Wt−1​(1+γW)if​ut<u⋆Wt−1​(1−γW)if​ut≥u⋆,W\_{t}=\begin{cases}W\_{t-1}(1+\gamma^{W})&\mbox{if}\ u\_{t}<u^{\star}\\ W\_{t-1}(1-\gamma^{W})&\mbox{if}\ u\_{t}\geq u^{\star}\\ \end{cases}\;\;, |  | (7) |

where utu\_{t} is the unemployment rate and γW\gamma^{W} is a random variable uniformly distributed between 0 and wbw\_{b}.

### 2.2 Government and Central Bank

The government collects taxes and CB’s profits, issues debt, and distributes lump sum transfers to households.

Government bonds are acquired by the CB and banks.
Bonds have a one-period maturity, are issued at par (with unitary face value) and pay an interest rate rBr^{B}. The government’s budget constraint is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Bt=rB​Bt+Gt−Tt−ΠtC​B,\Delta B\_{t}=r^{B}B\_{t}+G\_{t}-T\_{t}-\Pi\_{t}^{CB}\;\;, |  | (8) |

where BtB\_{t} is the outstanding stock of government bonds, GtG\_{t} denotes public transfers to households, TtT\_{t} denotes tax revenues and ΠtC​B\Pi^{CB}\_{t} is the profit of the CB, repatriated to the government.

To concentrate our attention on the effects associated with the introduction of CBDC, we assume a zero balance for the government budget (Δ​Bt=0\Delta B\_{t}=0) and, therefore, GtG\_{t} is such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=Tt+ΠtC​B−rB​Bt.G\_{t}=T\_{t}+\Pi\_{t}^{CB}-r^{B}B\_{t}\;\;. |  | (9) |

Note that the transfers to households GtG\_{t} can be positive or negative depending on whether government interest expenses are below or above revenues. GtG\_{t} is distributed to all households in the same way (GtnH\frac{G\_{t}}{n^{H}}).

The profit of the CB is given by interest payments on bonds (BtC​B{B}\_{t}^{CB}) minus remuneration of banks’ reserves RtR\_{t} and of C​B​D​CtCBDC\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠtC​B=Bt−1C​B​rB−Rt−1​rL−C​B​D​Ct−1​rC​B​D​C.\Pi\_{t}^{CB}={B}\_{t-1}^{CB}r^{B}-R\_{t-1}r^{L}-CBDC\_{t-1}r^{CBDC}\;\;. |  | (10) |

C​B​D​Ct−1CBDC\_{t-1} denotes the aggregate volume of CBDC at time t−1t-1 and rC​B​D​Cr^{CBDC} is its remuneration rate.
The interest rates on reserves (rLr^{L}) and on CBDC (rC​B​D​Cr^{CBDC}) are kept constant over time.

The CB retains all government bonds except those acquired by commercial banks:
BtC​B=Bt−∑hBth{B}\_{t}^{CB}=B\_{t}-\sum\_{h}B\_{t}^{h}, where BthB\_{t}^{h} is the quantity of government bonds owned by bank hh which is determined by the rule described in Section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

According to the aggregate balance sheet identity for the whole economy, the negative net wealth of the government is balanced by the positive net wealth of the private sector so that aggregate net wealth is zero, see Appendix [C.1](https://arxiv.org/html/2510.21071v1#A3.SSS1 "C.1 Aggregate balance sheet and transactions matrix ‣ Appendix C Accounting ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") for further details:

|  |  |  |
| --- | --- | --- |
|  | ∑i=1NHn​wi,tH+∑j=1NFn​wj,tF+∑h=1NBn​wh,tB+n​wtG=0.\sum\_{i=1}^{N^{H}}nw^{H}\_{i,t}+\sum\_{j=1}^{N^{F}}nw^{F}\_{j,t}+\sum\_{h=1}^{N^{B}}nw^{B}\_{h,t}+nw^{G}\_{t}=0\;\;. |  |

### 2.3 The business sector

There are NFN^{F} firms, indexed by jj, producing a homogeneous good using only labour as input.
In order to hire workers, firms need to pay the wage bill in advance. This cash-in-advance constraint is binding, so firms can only hire workers up to the available liquidity.

The balance sheet of a firm is made up of bank deposits DFD^{F} on the asset side and liabilities consisting of loans LFL^{F}. The net wealth is provided by:333Inventories are perishable as goods are assumed to fully depreciate each period. This assumption rules out business cycles driven by the accumulation of inventory. However, business cycles can arise from variations in business expectations driven by variations in sales.

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​wj​tF=Dj​tF−Lj​tF.nw\_{jt}^{F}=D\_{jt}^{F}-L\_{jt}^{F}\;\;. |  | (11) |

In each period, firms make their decisions in the following sequence:

1. 1.

   Set an output target from which they derive the labour target.
2. 2.

   Seek financing in order to meet the expected wage bill by borrowing if needed.
3. 3.

   Hire workers until the wage bill is met or no further employable workers can be found, then produce.
4. 4.

   Set a price for their output and sell it in the market.

We follow Delli Gatti et al.,  ([2011](https://arxiv.org/html/2510.21071v1#bib.bib14), see Figure 3.1, p. 57), assuming that firms set target quantities ([12](https://arxiv.org/html/2510.21071v1#S2.E12 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) and prices ([19](https://arxiv.org/html/2510.21071v1#S2.E19 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) considering the un-sold production (inventory) and firm specific mark-ups.

Firm jj’s output target Yj,tt​a​r​g​e​tY^{target}\_{j,t} at time tt is determined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yj,tt​a​r​g​e​t={Yj,t−1s​(1−χjq) if​I​N​Vj,t−1≥γq​Yj,t−1s​ and​Pj,t−1≤γp​P¯t−1Yj,t−1s​(1+χjq)if​I​N​Vj,t−1​<γq​Yj,t−1s​ and​Pj,t−1>​γp​P¯t−1,Y^{target}\_{j,t}=\begin{cases}Y^{s}\_{j,t-1}(1-\chi^{q}\_{j})&\mbox{ if}\ INV\_{j,t-1}\geq\gamma\_{q}Y^{s}\_{j,t-1}\mbox{ and}\ P\_{j,t-1}\leq\gamma\_{p}\bar{P}\_{t-1}\\ Y^{s}\_{j,t-1}(1+\chi^{q}\_{j})&\mbox{if}\ INV\_{j,t-1}<\gamma\_{q}Y^{s}\_{j,t-1}\mbox{ and}\ P\_{j,t-1}>\gamma\_{p}\bar{P}\_{t-1}\end{cases}\;\;, |  | (12) |

where Yj,tt​a​r​g​e​tY^{target}\_{j,t} is the target output of firm jj at time tt, Yj,t−1sY^{s}\_{j,t-1} is the output produced in t−1t-1, Yj,t−1Y\_{j,t-1} is the output sold in t−1t-1, and χjq∼U​(0,qb)\chi^{q}\_{j}\sim U(0,\ q\_{b}) is a uniform random variable, I​N​Vj,t−1INV\_{j,t-1} is the inventory in t−1t-1, γq\gamma\_{q} is a calibrated threshold, Pj,t−1P\_{j,t-1} is the price set by firm jj, and P¯t−1\bar{P}\_{t-1} is the average market price at t−1t-1.

The rule establishes that if a firm succeeds in selling at least a fraction 1−γq1-\gamma\_{q} of its output, and the price set is greater than γp\gamma\_{p} of the market price, then the one-step ahead target is revised to be above the actual output.
In case the firm has not sold at least a fraction 1−γq1-\gamma\_{q} of its output and its price is lower than or equal to γp\gamma\_{p} of the market price, then the target is revised to be below the actual output. In the remaining two cases, the target is left unchanged.

The firm’s labour target directly follows from the output target:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nj,tt​a​r​g​e​t=1α​Yj,tt​a​r​g​e​t,N^{target}\_{j,t}=\frac{1}{\alpha}Y^{target}\_{j,t}\;\;, |  | (13) |

where α\alpha is labour productivity, each worker produces α\alpha units of goods.

The main issue for the firm is whether and how this labour demand is financed under the cash-in-advance constraint.
On the basis of the target output and employment, each firm computes a target wage bill and tries to ensure the liquidity to finance it. To this end, the company uses first its own available resources and then goes to the credit market to borrow any additional need.
Therefore, the loan target is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lj,tt​a​r​g​e​t=max⁡(0,Wt​Nj,tt​a​r​g​e​t−ζ​n​wj,tF),L^{target}\_{j,t}=\max(0,\;W\_{t}N^{target}\_{j,t}-\zeta nw^{F}\_{j,t})\;\;, |  | (14) |

where n​wFnw^{F} is the net wealth of the firm. ζ∈[0,1]\zeta\in[0,1] is a parameter that weighs the relative priority given to internal finance (ζ=1\zeta=1) over borrowing (ζ=0\zeta=0) to meet operational needs.

As a firm might be rationed in the credit market, its actual loan Lj,tL\_{j,t} might be smaller than its loan target

|  |  |  |
| --- | --- | --- |
|  | Lj,t≤Lj,tt​a​r​g​e​t.L\_{j,t}\leq L^{target}\_{j,t}\;\;. |  |

In Section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we detail how the credit market works and, therefore, why not all the demand for credit may be fulfilled. Once the loan has been obtained, it is added to the firm’s deposit account and the funds are immediately available. The loans last only one period.

Once the firm has secured a loan and updated its liquidity, it determines the expected wage bill Ω\Omega by balancing its target output against the available funds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωj,t=min​[Dj,tF,Wt​Nj,tt​a​r​g​e​t].\Omega\_{j,t}=\mbox{min}\left[D^{F}\_{j,t},W\_{t}N^{target}\_{j,t}\right]\;\;. |  | (15) |

As described in Section [2.1.1](https://arxiv.org/html/2510.21071v1#S2.SS1.SSS1 "2.1.1 The labour market ‣ 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), in case the labour supply is lower than the demand, the firm can hire workers proportionally to its demand compared to the total demand.
As a consequence, the number of employed people Nj,tN\_{j,t} of firm jj satisfies the condition

|  |  |  |
| --- | --- | --- |
|  | Nj,t≤Ωj,tWt.N\_{j,t}\leq\frac{\Omega\_{j,t}}{W\_{t}}. |  |

and the actual supply of the firm is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yj,ts=α​Nj,t.Y\_{j,t}^{s}=\alpha N\_{j,t}. |  | (16) |

The price of the goods produced by firm jj is determined as a mark-up μj,t\mu\_{j,t} on the unit cost, due to its monopolist power:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj,t=(1+μj,t)​u​cj,t.P\_{j,t}=(1+\mu\_{j,t})uc\_{j,t}\;\;. |  | (17) |

The cost of producing one unit of good is u​cj,tuc\_{j,t} and is defined as the ratio of the wage bill plus the cost of borrowing to the actual output of the company:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​cj,t=(Wt​Nj,t+rj,tf​Lj,t)Yj,ts,uc\_{j,t}=\frac{(W\_{t}N\_{j,t}+r^{f}\_{j,t}L\_{j,t})}{Y^{s}\_{j,t}}\;\;, |  | (18) |

where LL represents the total amount of bank borrowing and rfr^{f} is the associated interest rate.

Similarly to quantity adjustment, firms revise their mark-ups after observing the inventory-to-production and price-to-market price ratio.
The mark-up of a firm is bounded from above and below and it goes up (or down) depending on the inventory being below (above) a certain threshold γq\gamma\_{q} of production and past price being below (above) a threshold γp\gamma\_{p} of the market price. In the remaining two cases, the mark-up doesn’t change. Specifically, the mark-up charged by firm jj at time tt follows the rule

|  |  |  |  |
| --- | --- | --- | --- |
|  | μj,t={min⁡[μm​a​x,μj,t−1​(1+χjμ)] if​I​N​Vj,t−1≤γq​Yj,t−1s​ and​Pj,t−1≤γp​P¯t−1max⁡[μm​i​n,μj,t−1​(1−χjμ)] if​I​N​Vj,t−1>γq​Yj,t−1s​ and​Pj,t−1>γp​P¯t−1,\mu\_{j,t}=\begin{cases}\min[\mu\_{max},\mu\_{j,t-1}(1+\chi^{\mu}\_{j})]&\mbox{ if}\ INV\_{j,t-1}\leq\gamma\_{q}Y^{s}\_{j,t-1}\mbox{ and}\ P\_{j,t-1}\leq\gamma\_{p}\bar{P}\_{t-1}\\ \max[\mu\_{min},\mu\_{j,t-1}(1-\chi^{\mu}\_{j})]&\mbox{ if}\ INV\_{j,t-1}>\gamma\_{q}Y^{s}\_{j,t-1}\mbox{ and}\ P\_{j,t-1}>\gamma\_{p}\bar{P}\_{t-1}\end{cases}\;\;, |  | (19) |

where χjμ∼U​(0,μb)\chi^{\mu}\_{j}\sim U(0,\ \mu\_{b}) is a uniform random variable.

After production and pricing have been determined, the goods market opens and consumers spend their consumption budget Ci,tdC^{d}\_{i,t} in ([4](https://arxiv.org/html/2510.21071v1#S2.E4 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) following the matching mechanism described in Gurgone et al.,  ([2018](https://arxiv.org/html/2510.21071v1#bib.bib22)).

Rationing can occur in the goods market and, therefore, actual sales can be smaller than the actual output (Yj,t≤Yj,tsY\_{j,t}\leq Y^{s}\_{j,t}).

Given the output Yj,tY\_{j,t} sold by firm jj, the firm’s gross profits Πj,tF\Pi^{F}\_{j,t} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πj,tF=Pj,t​Yj,t−Wt​Nj,t+Dj,t−1F​rD−∑h=1Nbrj​h,t−1f​Lj​h,t−1.\Pi\_{j,t}^{F}=P\_{j,t}{Y\_{j,t}}-W\_{t}N\_{j,t}+D\_{j,t-1}^{F}r^{D}-\sum\_{h=1}^{N^{b}}r^{f}\_{jh,t-1}L\_{jh,t-1}\;\;. |  | (20) |

Gross profits are given by sales revenues minus wage costs (associated with the actual output) and interest charges (deposits and loans).

If Πj,tF>0\Pi^{F}\_{j,t}>0, then the firm pays taxes and dividends, otherwise it absorbs the losses through its bank deposits.
If the gross profits are positive, then net profits are given by gross profits minus taxes imposed at the rate θF\theta^{F}.

A share δtf\delta^{f}\_{t} of net profits is distributed as dividends. The share is made up of two parts: a fixed component δF\delta^{F} and a component that depends on the net wealth of the firm relative to its after-tax profits that depends on an additional parameter dFd^{F}:

|  |  |  |
| --- | --- | --- |
|  | δtf=δF+dF​n​wj,tF(1−θF)​Πj,tF.\delta^{f}\_{t}=\delta^{F}+d^{F}\frac{nw^{F}\_{j,t}}{(1-\theta^{F})\Pi^{F}\_{j,t}}\;\;. |  |

This dividend policy prevents firms becoming too large on the basis of retained earnings. As a matter of fact, dividends increase (decrease) when net wealth goes up (falls).
The firm’s net wealth evolves as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​wj,tF={(1−dF)​n​wj,t−1F+(1−θF)​(1−δF)​Πj,t−1FifΠj,t−1F>0n​wj,t−1F+Πj,t−1FifΠj,t−1F≤0.nw^{F}\_{j,t}=\begin{cases}(1-d^{F})nw\_{j,t-1}^{F}+(1-\theta^{F})(1-\delta^{F})\Pi\_{j,t-1}^{F}\quad\quad&\text{if}\quad\quad\Pi\_{j,t-1}^{F}>0\\ nw\_{j,t-1}^{F}+\Pi\_{j,t-1}^{F}\quad\quad&\text{if}\quad\quad\Pi\_{j,t-1}^{F}\leq 0\end{cases}\;\;. |  | (21) |

If n​wj,tF≥0nw\_{j,t}^{F}\geq 0, then the firm’s debt is serviced, otherwise the firm becomes insolvent and bankruptcy occurs.

From tt to t+1t+1 the outgoings of the company consist of wage payments, taxes, dividends, and interest payments on the loan. These payments are settled at the end of period tt.

### 2.4 The banking sector

There are NBN^{B} banks, indexed by hh. They fund themselves through short-term unsecured liabilities and extend loans to firms. In the event of excess liquidity or shortages, they either exchange liquidity in the interbank market or, if they are rationed in that market, sell assets to adjust their liquidity position.

#### 2.4.1 Balance sheet

The asset side of the balance sheet of banks includes outstanding loans to firms, indexed by jj and to banks, indexed by qq, denoted respectively by LL and IlI^{l}, plus reserves RR detained at the CB and government bonds BB444RhR\_{h} is the total reserves held at the CB. It includes the required reserves computed using a constant regulatory reserve ratio r​rrr applied to total deposits of banks, r​r​DhBrrD^{B}\_{h}, and any excess reserves, Rh−r​r​DhBR\_{h}-rrD^{B}\_{h}.. Liabilities include interbank borrowing IbI^{b} from other banks, indexed by zz, and deposits DBD^{B}. Bank hh’s net wealth is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​wh,tB=Rh,t+∑j=1NFLh​j,t−1+∑q=1NBIh​q,t−1l+Bh,t−Dh,tB−∑z=1NBIz​h,t−1b.nw\_{h,t}^{B}=R\_{h,t}+\sum\_{j=1}^{N^{F}}L\_{hj,t-1}+\sum\_{q=1}^{N^{B}}I^{l}\_{hq,t-1}+B\_{h,t}-D\_{h,t}^{B}-\sum\_{z=1}^{N^{B}}I^{b}\_{zh,t-1}\;\;. |  | (22) |

Banks buy government bonds proportionally to their deposits: Bh,t=ϕe​x​t​Dh,tB\_{h,t}=\phi\_{ext}D\_{h,t}, where we set ϕe​x​t=10%\phi\_{ext}=10\%. Without prejudice to the main results, we assume that the bank cannot get liquidity from the CB.

#### 2.4.2 Credit supply

At the beginning of each period, banks face credit requests from firms and try to serve them in full, while respecting regulatory constraints and internal risk management standards.
Prudential regulation imposes minimum capital requirements, by which the net wealth of a bank should be greater or equal than a fraction 1/λ1/\lambda of the risk-weighted assets (RWA) computed according to the Standard approach in the spirit of Basel II and III regulation:

|  |  |  |
| --- | --- | --- |
|  | n​wh,tB≥1λ​RWAh,t,nw^{B}\_{h,t}\geq\frac{1}{\lambda}\text{RWA}\_{h,t}\;\;, |  |

where R​W​Ah=ω1​∑Lh+ω2​∑IhlRWA\_{h}=\omega\_{1}\sum L\_{h}+\omega\_{2}\sum I^{l}\_{h}, while the weight for cash and bonds is set at 0.

Moreover, we assume that banks hedge against risk in their exposures by keeping a level of net wealth that is able to absorb potential losses under a worst-case scenario. Losses in the worst-case scenario are assessed as a time-varying fraction of total exposures

|  |  |  |
| --- | --- | --- |
|  | n​wh,tB≥V​a​Rh,tt​a​i​l​(Lh,t+Ih,tl),nw^{B}\_{h,t}\geq VaR^{tail}\_{h,t}(L\_{h,t}+I^{l}\_{h,t})\;\;, |  |

where V​a​Rh,tt​a​i​lVaR^{tail}\_{h,t} is computed as a parametric Gaussian Value at Risk (VaR) at tail probability t​a​i​l=0.99tail=0.99 where the mean and variance parameters are estimated from the historical losses of the loan portfolio.

These two constraints jointly determine the total bank credit supply in the model. Accordingly, bank hh supplies credit up to the lowest amount allowed by prudential regulation and portfolio-risk management:555The expression for the credit supply in ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) is obtained by solving n​wB≥1λ​(ω1​L+ω2​Il)nw^{B}\geq\frac{1}{\lambda}(\omega\_{1}L+\omega\_{2}I^{l}) and n​wB≥V​a​Rt​a​i​l​(L+Il)nw^{B}\geq VaR^{tail}(L+I^{l}) for LL, where the loan maturity is one time unit.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lh,ts=min⁡(λ​n​wh,tBω1−ω2​Ih,tlω1,n​wh,tBV​a​Rh,tt​a​i​l−Ih,tl).L^{s}\_{h,t}=\min\left(\lambda\frac{nw^{B}\_{h,t}}{\omega\_{1}}-\omega\_{2}\frac{I^{l}\_{h,t}}{\omega\_{1}},\frac{nw^{B}\_{h,t}}{VaR^{tail}\_{h,t}}-I^{l}\_{h,t}\right)\;\;. |  | (23) |

Besides complying with ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), banks manage firm-specific risk so that the exposure to a single firm jj is capped at ς=0.15\varsigma=0.15 of the bank net wealth, which determines the maximum of equity loss the bank is willing to bear per loan.
Therefore, the credit supplied to firm jj by bank hh is up to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lh​j,ts≤ς​n​wh,tBρj,tf,L^{s}\_{hj,t}\leq\frac{\varsigma nw^{B}\_{h,t}}{\rho^{f}\_{j,t}}\;\;, |  | (24) |

where ρf\rho^{f} is the probability of default of firm jj, that we will define in ([25](https://arxiv.org/html/2510.21071v1#S2.E25 "In 2.4.4 Interest rate ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")).

#### 2.4.3 Banks-firms matching

Firms are matched to banks in the credit market via a preferential attachment mechanism with probabilistic switching, by which firms can switch between lenders with a predetermined probability, see also Section [D.1](https://arxiv.org/html/2510.21071v1#A4.SSS1 "D.1 The matching mechanism ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").
Each bank charges an interest rate, taking into account its counterparty credit risk and its own cost of funding, leading to heterogeneous interest rates.
Banks rank firms in ascending order based on their credit merit.
They then begin by fully satisfying the loan requests of the least risky firms up to the constraint ([24](https://arxiv.org/html/2510.21071v1#S2.E24 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), continuing in this manner until their total credit supply in ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) or demand is exhausted. In this way, risky firms are more likely to be rationed. If a firm is rationed by its preferred bank, then it can seek credit from some other banks, repeating this process until its demand is fully met or all connected banks deny the loan.

#### 2.4.4 Interest rate

The default risk ρt,h​jf\rho^{f}\_{t,hj} perceived by bank hh concerning firm jj is inspired by Delli Gatti et al.,  ([2011](https://arxiv.org/html/2510.21071v1#bib.bib14)) and is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt,h​jf=v0​ev1​(ljl⋆−1),\rho^{f}\_{t,hj}=v\_{0}e^{v\_{1}\left(\frac{l\_{j}}{l\star}-1\right)}\;\;, |  | (25) |

where ljl\_{j} is the loan demand to net wealth ratio of jj, v0v\_{0}, and v1v\_{1}, l⋆l^{\star} are parameters to be calibrated.

The interest rate at which bank hh offers a loan to firm jj is denoted by rt,h​jfr\_{t,hj}^{f}. The rate is a function of its cost of funding and jj’s specific risk of default:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rh​j,tf=1+c​fh,t1−ρj,tf−1,r^{f}\_{hj,t}=\frac{1+cf\_{h,t}}{1-\rho^{f}\_{j,t}}-1\;\;, |  | (26) |

where c​fh,tcf\_{h,t} is the bank h′​sh^{\prime}s cost of funds, and is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​fh,t=ωh,tD​rD+ωh,tI​rt−1,hb,cf\_{h,t}=\omega^{D}\_{h,t}r^{D}+\omega^{I}\_{h,t}{r}\_{t-1,h}^{b}\;\;, |  | (27) |

where ωh,ti\omega\_{h,t}^{i} represents the share of each source of liquidity of the bank (ii represents deposits and interbank borrowing) over liabilities.

By design, the lending rate in ([26](https://arxiv.org/html/2510.21071v1#S2.E26 "In 2.4.4 Interest rate ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) is set to be greater than or equal to the bank’s funding cost and increases with the probability of default of the firm jj.

#### 2.4.5 Interbank market

Banks mitigate the risk of illiquidity by trading on the interbank market.
We slightly depart from the original framework in Gurgone et al.,  ([2018](https://arxiv.org/html/2510.21071v1#bib.bib22)); Gurgone and Iori,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib21)) by limiting the maximum amount that a bank can borrow to the risk-weighted value of its assets, which provides a collateralization of interbank borrowing.

Banks aim to set aside a sufficient buffer of liquidity to hedge against changes in the balance sheets of other agents, e.g. withdrawals and defaults.
This approach results in banks forming an internal liquidity coverage ratio which determines demand and supply of interbank funds.666Banks may alternatively participate in the interbank market to meet the prudential liquidity coverage ratio mandated by Basel III as in Popoyan et al.,  ([2017](https://arxiv.org/html/2510.21071v1#bib.bib31)).

To enhance realism in terms of interlocked balance sheets, we assume that there are three sessions of the interbank market for each time iteration: i) after lending to firms, ii) after firms sell their production on the goods market, iii) after factoring defaults and losses of firms and other banks. At the end of each session, banks settle their positions. If a bank does not satisfy its liquidity coverage ratio, it liquidates part of its assets through the mechanism in ([37](https://arxiv.org/html/2510.21071v1#S2.E37 "In 2.4.6 Liquidation of assets ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")).

In agreement with the regulation, bank hh computes a liquidity coverage ratio given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​Rh,t=Rh,t−r​r​Dh,tBo​u​th,tE−i​nh,tE≥1,LR\_{h,t}=\frac{R\_{h,t}-rrD\_{h,t}^{B}}{out^{E}\_{h,t}-in^{E}\_{h,t}}\geq 1\;\;, |  | (28) |

where the numerator captures the bank’s reserves detained at the CB, adjusted for the required reserve ratio on deposits. The denominator represents the expected gap between expected cash outflows o​u​tEout^{E} and inflows i​nEin^{E} over a single period of time.777As banks anticipate their liquidity requirements based on economic conditions, shown by borrowers’ default risks, they require a greater cash level during periods of substantial losses compared to stable times.
For the bank to be considered sufficiently liquid, the liquidity ratio must be greater than one.
The expected cash outflows consist of interest payments on deposits and interbank borrowing c​i​bEcib^{E}, and the expected amount of lending to firms LEL^{E}:

|  |  |  |
| --- | --- | --- |
|  | o​u​th,tE=rD​Dh,tB+c​i​bh,tE+Lh,tE,out^{E}\_{h,t}=r^{D}D\_{h,t}^{B}+cib^{E}\_{h,t}+L^{E}\_{h,t}\;\;, |  |

where Lh,tE=aL​Lh,t+(1−aL)​Lh,t−1EL^{E}\_{h,t}=a^{L}L\_{h,t}+(1-a^{L})L^{E}\_{h,t-1} and c​i​bEcib^{E} is constructed as the weighted average of the interest rate on interbank borrowing for the borrowed amount during the last τ\tau periods in the bank’s memory.

The expected cash inflows i​nEin^{E} include the total amount of interest payments on loans to firms from the subset of borrowers JJ, along with the principal amount to be repaid at the end of period tt, adjusted for the probability of default of borrowers, together with the interest paid by the CB on reserves and bonds:

|  |  |  |
| --- | --- | --- |
|  | i​nh,tE=∑j∈JLh​j,t​(rh​j,t−1f+1−ρh​j,tf)+rL​Rh,t+rB​Bh,t.in^{E}\_{h,t}=\sum\_{j\in J}L\_{hj,t}(r^{f}\_{hj,t-1}+1-\rho^{f}\_{hj,t})+r^{L}R\_{h,t}+r^{B}B\_{h,t}\;. |  |

If the liquidity coverage ratio is lower than one, meaning that the expected cash outflows net of inflows are greater than bank reserves net of required reserves, then bank hh demands interbank liquidity (IdI^{d}) to close the gap.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ih,td=o​u​tt,hE−i​nt,hE−(Rh,t−r​r​Dh,tB).I^{d}\_{h,t}=out^{E}\_{t,h}-in^{E}\_{t,h}-(R\_{h,t}-rrD\_{h,t}^{B})\;\;. |  | (29) |

Otherwise, the bank supplies its excess liquidity (IsI^{s}) on the interbank market, subject to its total loan supply in ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) net of outstanding loans:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ih,ts=min⁡[Rh,t−r​r​Dh,tB−(o​u​tt,hE−i​nt,hE),Lh,ts−∑j∈JLh​j,t−kF].I^{s}\_{h,t}=\min\left[\vphantom{\sum\_{a}^{b}}R\_{h,t}-rrD\_{h,t}^{B}-(out^{E}\_{t,h}-in^{E}\_{t,h}),\ L^{s}\_{h,t}-\sum\_{j\in J}L^{F}\_{hj,t-k}\right]\;\;. |  | (30) |

Furthermore, we assume that the liquidity supplied by a bank hh to any bank zz cannot exceed the value of the illiquid assets of zz:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ih​z,ts≤∑j∈JLz​j,t​(1−ρz​j,tf)+Bz,t,I^{s}\_{hz,t}\leq\sum\_{j\in J}L\_{zj,t}(1-\rho^{f}\_{zj,t})+B\_{z,t}\;\;, |  | (31) |

where JJ is the subset of firms that borrow from the bank zz and ρf\rho^{f} is the default probability of these firms.

Banks trade in a decentralized interbank market.
Banks in demand of liquidity enter one-by-one in a random order and are matched to a randomly selected bank offering a positive supply of interbank funds. This process is repeated ni​b​t​e​n​tn^{ibtent} times for all potential borrowers.
Borrowers place a bid rb​i​dr^{bid} reflecting how much they are willing to pay on borrowed funds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rz,tbid=rH+rL2​(1+εz,t),rz,tbid∈[rL,rH].r\_{z,t}^{\text{bid}}=\frac{r^{H}+r^{L}}{2}(1+\varepsilon\_{z,t}),\quad r\_{z,t}^{\text{bid}}\in[r^{L},r^{H}]\;\;. |  | (32) |

Since they do not know lenders’ reservation rates, borrowers initially bid in the middle of the corridor determined by lower and upper-bounds, which are set by the CB and are respectively the rate paid on excess funds rLr^{L} (lower-bound) and the rate of a fictitious marginal lending facility rHr^{H} (higher bound).888Although the interest rate on interbank loans is set around the mid-corridor, this model assumes that banks cannot access the marginal lending facility. As a result, unmet funding needs are covered by the liquidation of assets.

If demand is not entirely satisfied, the borrowers increase the bid by a mark-up ε\varepsilon, whereas they decrease it by the same amount if a lender accepts their bid:

|  |  |  |  |
| --- | --- | --- | --- |
|  | εz,o+1={εz,o+γi​bif ​Iz,od>Iz,obandrz,ob​i​d≤rHεz,o−γi​bif ​Iz,od=Iz,obandrz,ob​i​d≥rL,\varepsilon\_{z,o+1}=\begin{cases}\varepsilon\_{z,o}+\gamma^{ib}&\text{if }I^{d}\_{z,o}>I^{b}\_{z,o}\quad\text{and}\quad r^{bid}\_{z,o}\leq r^{H}\\ \varepsilon\_{z,o}-\gamma^{ib}&\text{if }I^{d}\_{z,o}=I^{b}\_{z,o}\quad\text{and}\quad r^{bid}\_{z,o}\geq r^{L}\end{cases}\;\;, |  | (33) |

where o∈[1,ni​b​t​e​n​t]o\in[1,n^{ibtent}] denotes the sequence of borrowing attempts and γi​b∼U​(0,bidb)\gamma^{ib}\sim U(0,\ \text{bid}\_{b}) is a uniform random variable.
It should be noted that the last value of ε\varepsilon is retained in the bank’s memory at the beginning of a new interbank session.

The reservation rate of lenders rr​e​sr^{res} is determined by a risk premium for the probability of default of borrowers relative to the rate on excess funds rLr^{L}. For a lender hh and a borrower zz, it is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rh​z,tr​e​s=1+rL1−ρh​z,tb−1,r\_{hz,t}^{res}=\frac{1+r^{L}}{1-\rho^{b}\_{hz,t}}-1\;\;, |  | (34) |

where the default probability

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρz,tb=v0​exp⁡[v1​(lzblb⁣⋆−1)]\rho\_{z,t}^{b}=v\_{0}\exp\left[v\_{1}\left(\frac{l^{b}\_{z}}{l^{b\star}}-1\right)\right] |  | (35) |

grows with lzbl^{b}\_{z}, the total exposures to equity ratio of bank zz. v0v\_{0}, v1v\_{1}, and lb⁣⋆l^{b\star} are parameters to be calibrated.

The amount borrowed (lent) at time tt by zz (hh) is Ih​z,t=min⁡(Iz,td,Ih​z,ts)I\_{hz,t}=\min(I^{d}\_{z,t},I^{s}\_{hz,t}) and takes place at an interest rate where the borrower’s bid rate is greater or equal than the lender’s reservation rate.

|  |  |  |  |
| --- | --- | --- | --- |
|  | rh​z,tb=rz,tb​i​dif ​rz,tb​i​d≥rh​z,tr​e​s.r^{b}\_{hz,t}=r^{bid}\_{z,t}\quad\mbox{if }\;\;r^{bid}\_{z,t}\geq r^{res}\_{hz,t}. |  | (36) |

#### 2.4.6 Liquidation of assets

When banks run out of liquidity or need to settle creditors’ claims following bankruptcy, they sell off assets (government bonds and loans to firms). The liquidation process is handled by a special agency. The index o=1,…,NBo=1,\dots,N^{B} tracks the order of sellers within each time unit, as more than one bank can sell assets at time tt. Sellers enter the market in random order: the first one sells at the most favourable price p1>p2p\_{1}>p\_{2} per unit of bond or loan, the second at p2>p3p\_{2}>p\_{3} and so on. At the end of period tt, the asset price is reset to its initial value p0=1p\_{0}=1. As in Cifuentes et al.,  ([2005](https://arxiv.org/html/2510.21071v1#bib.bib13)); Varaart,  ([2025](https://arxiv.org/html/2510.21071v1#bib.bib32)); Zachary et al.,  ([2025](https://arxiv.org/html/2510.21071v1#bib.bib35)), we assume that banks begin by selling the most liquid assets, i.e., government bonds, that are more liquid than loans (ϵb​o​n​d​s>ϵl​o​a​n​s\epsilon^{bonds}>\epsilon^{loans}), and stop when their liquidity needs are met. The special agency purchases assets at the price pop\_{o}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | poi=max⁡[0.5,po−1i​(1−qoiQi​1ϵi)],i={b​o​n​d​s,l​o​a​n​s},p^{i}\_{o}=\max\left[0.5,\;p^{i}\_{o-1}\left(1-\frac{q^{i}\_{o}}{Q^{i}}\frac{1}{\epsilon^{i}}\right)\right],\quad\quad i=\{bonds,\ loans\}\;\;, |  | (37) |

where qoiq^{i}\_{o} is the amount that a bank in rank oo needs to liquidate, QiQ^{i} is the total amount of asset ii in the economy, and ϵi\epsilon^{i} is the price elasticity of asset ii.
The lower-bound on pp is set to 0.50.5 to reflect the upper-bound on the loss given default of assets and the role of arbitrageurs, who would purchase underpriced assets at a discount to make profits, thus preventing prices from dropping further.
The assets acquired by the agency are held to maturity and any profit or loss is transferred to the government. Liquidation has a price impact only on the balance sheet of the seller.
The lower-bound can also be interpreted as a bail-out of banks in very difficult conditions.

#### 2.4.7 Profits and losses

Gross profits for bank hh are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πh,tB=\displaystyle\Pi\_{h,t}^{B}= | Rh,t−1​rL+Bh,t−1​rB+∑j=1NFLh​j,t−1​rh​j,t−1f+\displaystyle R\_{h,t-1}r^{L}+B\_{h,t-1}r^{B}+\sum\_{j=1}^{N^{F}}{L}\_{hj,t-1}r\_{hj,t-1}^{f}+ |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑q=1NBIh​q,t−1l​rh​q,t−1b−∑z=1NBIz​h,t−1b​rz​h,t−1b−Dh,t−1​rD−l​o​s​s​e​sh,t.\displaystyle+\sum\_{q=1}^{N^{B}}I^{l}\_{hq,t-1}r^{b}\_{hq,t-1}-\sum\_{z=1}^{N^{B}}I^{b}\_{zh,t-1}r^{b}\_{zh,t-1}-D\_{h,t-1}r^{D}-losses\_{h,t}\;\;. |  | (38) |

If positive, profits are taxed at rate θB\theta^{B} and a share δB\delta^{B} is distributed to shareholders, what is left is retained by the bank.

Losses arise from three different sources: defaults on loans to firms, defaults on interbank loans, and liquidation of assets:

* •

  Losses from defaults on loans to firms are given by the stock of loans outstanding to insolvent firms, minus their deposits, which are seized in case of default. In other words, losses are provided by the negative net wealth of firms defaulting on loans. If an insolvent firm borrowed from more than one bank, then the loss borne by creditors is distributed proportionally to the amount lent by each bank.
* •

  Banks defaulting on interbank loans are another potential source of losses. If a bank defaults, then creditors recover their share of residual assets in proportion to their claims on the defaulter’s liabilities.
  As claimants include households, firms, and other banks, we assume that under bankruptcy law, depositors (households and firms) are the most guaranteed type of creditors. Their claims are therefore prioritized over interbank claims, which are settled on any residual asset after depositors have been repaid.
  Notice that contagion can arise. If a borrower defaults, then the creditor bank can become insolvent and go into bankruptcy as well, triggering a cascade of bankruptcies or losses on the interbank and credit market.
* •

  Losses from asset liquidation are provided by the difference between net wealth before and after liquidation.

At the end of each period, the net wealth of bank hh is updated by net profits: the bank retains profits after taxes, distributes dividends if gross profits are positive and absorbs losses otherwise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​wh,tB={n​wh,t−1B+(1−θB)​(1−δB)​Πh,tB,if ​Πh,tB>0n​wh,t−1B+Πh,tBif ​Πh,tB≤0.\displaystyle nw\_{h,t}^{B}=\begin{cases}nw\_{h,t-1}^{B}+(1-\theta^{B})(1-\delta^{B})\Pi\_{h,t}^{B},&\text{if }\Pi\_{h,t}^{B}>0\\ nw\_{h,t-1}^{B}+\Pi\_{h,t}^{B}&\text{if }\Pi\_{h,t}^{B}\leq 0\\ \end{cases}\;\;. |  | (39) |

The end-of-period change in reserves held by bank hh with the CB is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Rh,t=Δ​Dh,tB−Δ​Lh,t+Δ​n​wh,tB\Delta R\_{h,t}=\Delta D^{B}\_{h,t}-\Delta L\_{h,t}+\Delta nw\_{h,t}^{B} |  | (40) |

where Δ\Delta is the first difference operator.

### 2.5 Bankruptcy and new entrants

If a firm or bank’s net wealth becomes negative, it goes bankrupt. The resulting losses are absorbed by its creditors’ balance sheets, potentially triggering further defaults.

Households act as shareholders of both firms and banks, receiving dividends as part of their participation in profits. For simplicity, we assume that each firm or bank is equally owned by a fixed number of households, who are equivalent to depositors in the case of banks.

#### 2.5.1 Firms

Banks do not lose the entire loan amount when a firm defaults on its loans. Instead, the firm’s remaining assets (which are equivalent to deposits) are distributed among creditors. The actual loss corresponds to the firm’s negative net wealth which is shared proportionally among creditors.

Consequently, if a defaulting firm has more than one creditor, the actual loss is distributed across all creditors, with each creditor bearing a loss proportional to the size of its loan relative to the borrower’s total debt. After default, firms exit the market and are replaced after r​e​c​a​pF=2recap^{F}=2 periods by new firms. These entrants begin with no liabilities and positive deposits, funded by a randomly determined share of their shareholders’ wealth.

#### 2.5.2 Banks

A bank in default typically has multiple creditors, as its liabilities include deposits from firms and households, as well as interbank loans. In the event of default, the bank’s creditors absorb its negative net wealth until it is fully depleted. All creditors incur losses; however, depositors — especially households — are the most protected. They only bear the portion of losses not already absorbed by other creditors, as they rank last in the loss hierarchy. After default, the only remaining items on the bank’s balance sheet are deposits and a corresponding amount of reserves. Households and firms retain access to their deposits even if the bank is no longer active and they can still use them for consumption and to pay wages. The bank is not replaced by another institution but is instead recapitalized with fresh capital from its shareholders, either after a minimum period r​e​c​a​pB=4recap^{B}=4 out of operation or once it becomes viable for recapitalization.

The recapitalization is deemed successful only if shareholders possess enough capital to satisfy the required asset-to-liability ratio; otherwise, the bank remains inactive until its shareholders can finance the operations.

It is important to note that a bank’s default may trigger the default of its creditors, which include firms and other banks. Households are exposed only through their deposits and, in the worst-case scenario, may lose their entire net wealth. If a firm loses part of its deposits, it may become unable to repay its loans and consequently goes bankrupt. A similar mechanism applies to banks, whose balance sheets contain interbank loans that can transmit financial distress throughout the system.

## 3 CBDC adoption

We set different rules for the portion of liquidity held by household ii in bank hh to be converted in CBDC. We assume that

|  |  |  |
| --- | --- | --- |
|  | C​B​D​Ci​h,t=ψ​(R​Mh,t)​wi​h​n​wi,tH,CBDC\_{ih,t}=\psi(RM\_{h,t})w\_{ih}nw^{H}\_{i,t}\;\;, |  |

where R​MhRM\_{h}, as defined in ([6](https://arxiv.org/html/2510.21071v1#S2.E6 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), is the riskiness of bank hh (bank liabilities/net wealth ratio) to which the household is matched.
Households are matched to more than one bank and therefore the total amount of CBDC of household ii is

|  |  |  |
| --- | --- | --- |
|  | C​B​D​Ci,t=∑hC​B​D​Ci​h,t.CBDC\_{i,t}=\sum\_{h}CBDC\_{ih,t}. |  |

Our hypothesis is that banks’ balance sheets are observable and households base their conversion decision on their riskiness which is proxied by the leverage ratio.

![Refer to caption](figures/cbdc_rules.png)


Figure 1: Share of households’ liquidity converted into CBDC by adoption rules.

We consider five different rules determining the fraction of liquidity to be converted in CBDC: flat fraction (CBDC0), loose bound on deposit withdrawal dependent on bank’s riskiness (CBDC1), fraction dependent on bank’s riskiness with a tight bound (CBDC2 and 3), fraction dependent on bank’s riskiness and deposit insurance scheme (CBDC4).

The rules are as follows, see Figure [1](https://arxiv.org/html/2510.21071v1#S3.F1 "Figure 1 ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") for a graphical representation:

* •

  CBDC0: Households convert a1a\_{1} of their liquidity into CBDC independently of the riskiness of the bank:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψ​(R​Mh,t)=a1.\psi(RM\_{h,t})=a\_{1}. |  | (41) |

  In the simulations we set a1=0.1a\_{1}=0.1.
* •

  CBDC1:
  Households convert a fixed quota of their liquidity into CBDC if the riskiness of the bank is below R​M∗RM^{\*} and an increasing linear function of the riskiness if it is above R​M∗RM^{\*}.
  The bound on conversion is loose, the upper-bound is set at a4=80%a\_{4}=80\% of deposits if bank’s riskiness is above R​M∗+R​Ml​i​mRM^{\*}+RM^{lim} (almost unconstrained substitution):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψ​(R​Mh,t)={a1R​Mh,t≤R​M∗a1+(a4−a1)​R​Mh,t−R​M∗R​Ml​i​mR​M∗<R​Mh,t<R​M∗+R​Ml​i​ma4R​Mh,t≥R​M∗+R​Ml​i​m.\psi(RM\_{h,t})=\begin{cases}a\_{1}&RM\_{h,t}\leq RM^{\*}\\ a\_{1}+(a\_{4}-a\_{1})\dfrac{RM\_{h,t}-RM^{\*}}{RM^{lim}}&RM^{\*}<RM\_{h,t}<RM^{\*}+RM^{lim}\\ a\_{4}&RM\_{h,t}\geq RM^{\*}+RM^{lim}.\end{cases} |  | (42) |

  Coherently with the regulation, the risk measure threshold is R​M∗=6RM^{\*}=6 and R​Ml​i​m=7.6RM^{lim}=7.6.
* •

  CBDC2: Households convert a fraction of liquidity into CBDC depending on the riskiness of the bank.
  The quota converted into CBDC is up to a cap a2<a4a\_{2}<a\_{4}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψ​(R​Mh,t)={a1R​Mh,t≤R​M∗a1+(a2−a1)​R​Mh,t−R​M∗R​Ml​i​mR​M∗<R​Mh,t<R​M∗+R​Ml​i​ma2R​Mh,t≥R​M∗+R​Ml​i​m.\psi(RM\_{h,t})=\begin{cases}a\_{1}&RM\_{h,t}\leq RM^{\*}\\ a\_{1}+(a\_{2}-a\_{1})\dfrac{RM\_{h,t}-RM^{\*}}{RM^{lim}}&RM^{\*}<RM\_{h,t}<RM^{\*}+RM^{lim}\\ a\_{2}&RM\_{h,t}\geq RM^{\*}+RM^{lim}.\end{cases} |  | (43) |

  In what follows, we set a2=0.3a\_{2}=0.3, that is, depositors convert at most 30%30\% of their deposits into CBDC.
* •

  CBDC3: Households convert a fixed quota of their liquidity into CBDC, depending on bank’s riskiness. If the risk threshold R​M∗RM^{\*} is exceeded, households convert the fraction a2a\_{2} of wealth, otherwise they convert the fraction a1a\_{1}, with a1<a2<a4a\_{1}<a\_{2}<a\_{4}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψ​(R​Mh,t)={a1,R​Mh,t≤R​M∗a2,R​Mh,t>R​M∗.\psi(RM\_{h,t})=\begin{cases}a\_{1},&RM\_{h,t}\leq RM^{\*}\\[6.0pt] a\_{2},&RM\_{h,t}>RM^{\*}.\end{cases} |  | (44) |
* •

  CBDC4: Households convert a fixed quota of liquidity into CBDC, the quota depends on the riskiness of the bank. If riskiness is below R​M∗RM^{\*}, then the quota is a1a\_{1}; if it is above R​M∗RM^{\*} and deposits are below the insurance deposit threshold (I​T∗IT^{\*}), then the quota is a2≥a1a\_{2}\geq a\_{1}; if it is above R​M∗RM^{\*} and deposits are larger than I​T∗IT^{\*}, then the quota is
  a2a\_{2} plus a linear term that depends upon wi​h​n​wiH−I​T∗wi​h​n​wiH\frac{w\_{ih}nw^{H}\_{i}-IT^{\*}}{w\_{ih}nw^{H}\_{i}}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψ​(R​Mh,t)={a1if ​R​Mh,t≤R​M∗a2,if ​R​Mh,t>R​M∗​ and ​wi​h​n​wiH≤I​T∗a2+a3​wi​h​n​wiH−I​T∗wi​h​n​wiH,if ​R​Mh,t>R​M∗​ and ​wi​h​n​wiH>I​T∗,\displaystyle\psi(RM\_{h,t})=\begin{cases}a\_{1}&\text{if }RM\_{h,t}\leq RM^{\*}\\ a\_{2},&\text{if }RM\_{h,t}>RM^{\*}\,\mbox{ and }\,w\_{ih}nw^{H}\_{i}\leq IT^{\*}\\ a\_{2}+a\_{3}\frac{w\_{ih}nw^{H}\_{i}-IT^{\*}}{w\_{ih}nw^{H}\_{i}},&\text{if }RM\_{h,t}>RM^{\*}\,\mbox{ and }\,w\_{ih}nw^{H}\_{i}>IT^{\*},\end{cases} |  | (45) |

  where a2+a3=1a\_{2}+a\_{3}=1. Insurance is provided by the government and is funded by public funds.
  Conditional on the default of bank hh, the government compensates depositor ii according to the following scheme:

  |  |  |  |
  | --- | --- | --- |
  |  | c​o​m​p​e​n​s​a​t​i​o​ni|d​e​f​a​u​l​th=min⁡(wi​h​n​wiH,I​T∗)⋅[1−ψ​(R​Mh,t)]⋅(1−ξi,hr​e​c),compensation\_{i|default\_{h}}=\min(w\_{ih}nw^{H}\_{i},\;IT^{\*})\cdot\left[1-\psi(RM\_{h,t})\right]\cdot(1-\xi^{rec}\_{i,h})\;\;, |  |

  where ξi,hr​e​c\xi^{rec}\_{i,h} is the recovery rate associated to the default of bank hh.999The recovery rate follows from the bankruptcy law, by which depositors are the most guaranteed type of creditors, see Section [2.4.7](https://arxiv.org/html/2510.21071v1#S2.SS4.SSS7 "2.4.7 Profits and losses ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") for further details.

CBDC0 and CBDC1 rules describe the two central scenarios of our analysis.
In the first, households hold a fixed amount of their liquidity as CBDC (10%), the amount is calibrated to be similar to the amount of cash. In the second scenario, we consider the extreme case in which a massive conversion of deposits into CBDC can occur depending on bank’s riskiness. This scenario allows for a bank-run to be ignited by the conversion of deposits into CBDC when default of the bank is feared.

CBDC2 and CBDC3 rules allow us to evaluate the effects of tight bounds on the amount of CBDC with households switching from 1010 to 30%30\% in case the bank becomes risky (its leverage triggers a certain threshold); CBDC2 rule allows for a smooth conversion, CBDC3 rule considers an abrupt conversion.
The CBDC4 rule models deposit insurance: households substitute deposits with CBDC in a limited way if the bank is risky and deposits are below a certain threshold and substitution goes up if deposits are above the deposit insurance threshold (100,000100,000 euro in the Euro area).

## 4 Simulation results

The model is calibrated as discussed in Appendix [A](https://arxiv.org/html/2510.21071v1#A1 "Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") while the Bayesian estimation procedure is reported in Appendix [B](https://arxiv.org/html/2510.21071v1#A2 "Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"). In short, the calibration relies on macroeconomic and financial data from the European Union (EU) and the Euro area. To ensure computational tractability, the number of agents is scaled down from real-world statistics, resulting in 500 firms, 2,500 households, and 10 banks preserving ratios observed empirically.
The initial values of net wealth are derived from the deposit-to-GDP ratio reported by the European Central Bank. The nominal wage serves as a numéraire to scale monetary quantities, and the unemployment rate is calibrated to the long-term Euro area average. Transition in the labour market is modeled using a binomial distribution which is matched to observed EU labour market flows.
The Bayesian estimation targets the first two moments (mean and standard deviation) of key economic time series (change in consumer prices, credit to GDP, unemployment rate, and CET1 ratio capital of banks) to align simulated to real data. Parameters are calibrated to closely match the mean of macroeconomic variables minimizing the variability. Table [11](https://arxiv.org/html/2510.21071v1#S8.T11 "Table 11 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") reports the time series and target moments for the 2000-2019 period (except CET1 ratio for 2015-2019).

Once the model is calibrated, we analyze the impact of introducing a CBDC through simulations. Each simulation runs for 1,000 time steps, but only the last 500 iterations are considered to avoid the influence of initial conditions. To ensure comparability, the network structure and the random seed are held constant across all simulations.

In Table [1](https://arxiv.org/html/2510.21071v1#S4.T1 "Table 1 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), for the baseline scenario (no CBDC), we report the mean, median, standard deviation, 1%1\% and 99%99\% percentile (P01P\_{01} and P99P\_{99}) for each variable. In Figure [2](https://arxiv.org/html/2510.21071v1#S4.F2 "Figure 2 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we report the cross-correlation heatmap highlighting the main relationships among the variables. We observe a strong positive correlation between output/real GDP and credit and sales. On average, the share of wealth retained as CBDC is 7.2, 41.2, 14.9, 17.6,and​ 19.5%7.2,\ 41.2,\ 14.9,\ 17.6,\ \text{and}\ 19.5\% according to the five conversion rules.

![Refer to caption](figures/cross_correlation_heatmap.png)


Figure 2: Cross-correlation between main variables for the baseline model.

Comparing the economy with CBDC to one without it, we develop the analysis in two directions through two sets of indicators. The first set of indicators includes mean, standard deviation, and median values, and the second the extreme values (percentiles 1% and 99%). The first set allows us to investigate the performance of the economy in normal times, and the other under extreme conditions.
In Table [2](https://arxiv.org/html/2510.21071v1#S4.T2 "Table 2 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")-[6](https://arxiv.org/html/2510.21071v1#S4.T6 "Table 6 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we report the statistics for each variable considering the five rules determining the amount of CBDC.
In Figure [3](https://arxiv.org/html/2510.21071v1#S4.F3 "Figure 3 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we present the median values over time for the main variables considering the baseline scenario (no CBDC) and those with CBDC according to the different rules.
In Figure [4](https://arxiv.org/html/2510.21071v1#S4.F4 "Figure 4 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we report the complementary cumulative distribution functions of the same variables.
The figure describes how often, in the simulated data, a variable is above the value reported on the x-axis, providing a comprehensive description of the probability distribution of the different variables in the simulations.

|  | Base | | | | |
| --- | --- | --- | --- | --- | --- |
| Variable | mean | sd | med | 𝐏𝟎𝟏\mathbf{P\_{01}} | 𝐏𝟗𝟗\mathbf{P\_{99}} |
| Output | 1630.948 | 135.013 | 1641.005 | 1258.074 | 1895.049 |
| Real GDP | 1596.738 | 107.540 | 1614.895 | 1258.074 | 1772.049 |
| Unemployment rate (%) | 9.832 | 2.597 | 9.560 | 5.240 | 17.440 |
| Inflation rate (%) | 0.002 | 1.071 | 0.006 | -2.419 | 2.442 |
| Interest rate to firms (%) | 3.149 | 0.218 | 3.142 | 2.645 | 3.713 |
| Credit to GDP (%) | 69.886 | 3.747 | 69.770 | 61.966 | 77.954 |
| CET1 to RWA (%) | 14.877 | 5.935 | 14.014 | 8.303 | 29.084 |
| Interbank lending | 211.390 | 225.910 | 147.785 | 0.000 | 874.715 |
| Net wealth of firms (% share) | 16.352 | 0.975 | 16.424 | 13.433 | 18.304 |
| Net wealth of banks (% share) | 3.530 | 1.124 | 3.371 | 1.681 | 7.058 |
| Net wealth of households (% share) | 80.118 | 1.180 | 80.130 | 77.209 | 82.971 |
| Default rate of firms (%) | 9.831 | 7.301 | 9.600 | 0.000 | 29.200 |
| Default rate of banks (%) | 1.226 | 4.787 | 0.000 | 0.000 | 20.000 |
| Liquidation default rate (%) | 0.002 | 0.134 | 0.000 | 0.000 | 0.000 |
| Firms-banks default rate (%) | 1.211 | 4.394 | 0.000 | 0.000 | 20.000 |
| Banks-banks default rate (%) | 0.086 | 1.697 | 0.000 | 0.000 | 0.000 |
| Banks-firms default rate (%) | 0.002 | 0.038 | 0.000 | 0.000 | 0.000 |
| Liquidation losses of banks to gdp (%) | 0.351 | 0.081 | 0.341 | 0.196 | 0.578 |
| Firms-banks losses to gdp (%) | 0.846 | 0.062 | 0.839 | 0.708 | 1.000 |
| Banks-banks losses to gdp (%) | 0.196 | 0.077 | 0.187 | 0.063 | 0.424 |
| Banks-firms losses to gdp (%) | 0.151 | 0.036 | 0.147 | 0.080 | 0.248 |

Table 1: Summary statistics for baseline scenario. Mean (mean), standard deviation (sd), median (med), 1st (P01P\_{01}) and 99th (P99P\_{99}) percentile).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CBDC0 | | | | | |
| Variable | dev | mean | sd | med | 𝐏𝟎𝟏\mathbf{P\_{01}} | 𝐏𝟗𝟗\mathbf{P\_{99}} |
| Output | -0.149 | 1628.524∗∗∗ | 144.095 | 1642.046 | 1151.578 | 1896.318 |
| Real GDP | -0.099 | 1595.150∗∗{}^{\*\*\phantom{\*}} | 118.797 | 1616.272 | 1151.578 | 1778.701 |
| Unemployment rate (%) | 0.083 | 9.914∗∗∗ | 2.786 | 9.600 | 5.240 | 19.360 |
| Inflation rate (%) | -0.000 | 0.002{}^{\phantom{\*\*\*}} | 1.078 | 0.011 | -2.454 | 2.445 |
| Interest rate to firms (%) | 0.057 | 3.206∗∗∗ | 0.204 | 3.200 | 2.738 | 3.720 |
| Credit to GDP (%) | 0.034 | 69.920{}^{\phantom{\*\*\*}} | 3.920 | 69.880 | 60.538 | 78.222 |
| CET1 to RWA (%) | -0.956 | 13.921∗∗∗ | 6.442 | 12.853 | 8.023 | 31.435 |
| Interbank lending | 44.641 | 305.756∗∗∗ | 240.552 | 280.539 | 0.000 | 937.113 |
| Net wealth of firms (% share) | -0.121 | 16.231∗∗∗ | 1.059 | 16.334 | 12.601 | 18.246 |
| Net wealth of banks (% share) | -0.183 | 3.348∗∗∗ | 1.150 | 3.151 | 1.536 | 7.446 |
| Net wealth of households (% share) | 0.304 | 80.422∗∗∗ | 1.173 | 80.423 | 77.560 | 83.318 |
| Default rate of firms (%) | -0.156 | 9.675∗∗∗ | 7.267 | 9.400 | 0.000 | 29.000 |
| Default rate of banks (%) | 0.060 | 1.286∗{}^{\*\phantom{\*\*}} | 5.103 | 0.000 | 0.000 | 30.000 |
| Liquidation default rate (%) | 0.004 | 0.006∗∗∗ | 0.264 | 0.000 | 0.000 | 0.000 |
| Firms-banks default rate (%) | -0.035 | 1.177{}^{\phantom{\*\*\*}} | 4.236 | 0.000 | 0.000 | 20.000 |
| Banks-banks default rate (%) | 0.071 | 0.156∗∗∗ | 2.307 | 0.000 | 0.000 | 0.000 |
| Banks-firms default rate (%) | 0.000 | 0.002{}^{\phantom{\*\*\*}} | 0.044 | 0.000 | 0.000 | 0.000 |
| Liquidation losses of banks to gdp (%) | 0.034 | 0.385∗∗∗ | 0.096 | 0.372 | 0.219 | 0.660 |
| Firms-banks losses to gdp (%) | -0.013 | 0.833∗∗∗ | 0.062 | 0.823 | 0.731 | 1.000 |
| Banks-banks losses to gdp (%) | 0.068 | 0.264∗∗∗ | 0.089 | 0.250 | 0.112 | 0.522 |
| Banks-firms losses to gdp (%) | 0.018 | 0.169∗∗∗ | 0.041 | 0.163 | 0.093 | 0.288 |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Table 2: Comparison of scenarios: CBDC0 rule. Deviation from baseline mean (dev), mean (mean), standard deviation (sd), median (med), 1st (P01P\_{01}) and 99th (P99P\_{99}) percentile. The deviation from the baseline is expressed in percentage points for rates and ratios or as percentage change for variables in level (real GDP, interbank lending).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CBDC1 | | | | | |
| Variable | dev | mean | sd | med | 𝐏𝟎𝟏\mathbf{P\_{01}} | 𝐏𝟗𝟗\mathbf{P\_{99}} |
| Output | -0.905 | 1616.192∗∗∗ | 212.428 | 1653.007 | 643.733 | 1952.144 |
| Real GDP | -0.517 | 1588.490∗∗∗ | 193.505 | 1632.796 | 643.733 | 1849.405 |
| Unemployment rate (%) | 0.587 | 10.419∗∗∗ | 4.108 | 9.600 | 4.720 | 29.760 |
| Inflation rate (%) | 0.002 | 0.003{}^{\phantom{\*\*\*}} | 1.156 | 0.031 | -2.564 | 2.549 |
| Interest rate to firms (%) | 0.113 | 3.262∗∗∗ | 0.186 | 3.256 | 2.844 | 3.721 |
| Credit to GDP (%) | -0.366 | 69.520∗∗∗ | 5.909 | 69.809 | 50.781 | 80.488 |
| CET1 to RWA (%) | -1.923 | 12.954∗∗∗ | 15.631 | 10.201 | 7.667 | 58.776 |
| Interbank lending | 70.852 | 361.163∗∗∗ | 237.783 | 341.688 | 0.000 | 963.070 |
| Net wealth of firms (% share) | -0.968 | 15.384∗∗∗ | 1.578 | 15.670 | 9.171 | 17.832 |
| Net wealth of banks (% share) | -0.675 | 2.855∗∗∗ | 1.294 | 2.507 | 1.131 | 8.323 |
| Net wealth of households (% share) | 1.643 | 81.761∗∗∗ | 1.363 | 81.690 | 78.816 | 85.717 |
| Default rate of firms (%) | -1.350 | 8.480∗∗∗ | 7.462 | 7.800 | 0.000 | 29.600 |
| Default rate of banks (%) | 0.235 | 1.461∗∗∗ | 6.121 | 0.000 | 0.000 | 30.000 |
| Liquidation default rate (%) | 0.043 | 0.044∗∗∗ | 0.760 | 0.000 | 0.000 | 0.000 |
| Firms-banks default rate (%) | -0.140 | 1.072∗∗∗ | 3.993 | 0.000 | 0.000 | 20.000 |
| Banks-banks default rate (%) | 0.282 | 0.368∗∗∗ | 3.523 | 0.000 | 0.000 | 10.000 |
| Banks-firms default rate (%) | 0.010 | 0.012∗∗∗ | 0.222 | 0.000 | 0.000 | 0.200 |
| Liquidation losses of banks to gdp (%) | 0.007 | 0.358∗∗∗ | 0.094 | 0.342 | 0.213 | 0.638 |
| Firms-banks losses to gdp (%) | -0.095 | 0.751∗∗∗ | 0.072 | 0.739 | 0.624 | 0.941 |
| Banks-banks losses to gdp (%) | 0.031 | 0.227∗∗∗ | 0.088 | 0.215 | 0.090 | 0.529 |
| Banks-firms losses to gdp (%) | 0.032 | 0.183∗∗∗ | 0.045 | 0.178 | 0.111 | 0.316 |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Table 3: Comparison of scenarios: CBDC1 rule. Deviation from baseline mean (dev), mean (mean), standard deviation (sd), median (med), 1st (P01P\_{01}) and 99th (P99P\_{99}) percentile. The deviation from the baseline is expressed in percentage points for rates and ratios or as percentage change for variables in level (real GDP, interbank lending).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CBDC2 | | | | | |
| Variable | dev | mean | sd | med | 𝐏𝟎𝟏\mathbf{P\_{01}} | 𝐏𝟗𝟗\mathbf{P\_{99}} |
| Output | -0.090 | 1629.480∗{}^{\*\phantom{\*\*}} | 141.301 | 1642.179 | 1183.503 | 1891.873 |
| Real GDP | -0.015 | 1596.497{}^{\phantom{\*\*\*}} | 116.113 | 1616.488 | 1183.503 | 1773.615 |
| Unemployment rate (%) | 0.065 | 9.897∗∗∗ | 2.739 | 9.600 | 5.280 | 18.800 |
| Inflation rate (%) | -0.002 | -0.001{}^{\phantom{\*\*\*}} | 1.068 | 0.004 | -2.411 | 2.433 |
| Interest rate to firms (%) | 0.046 | 3.195∗∗∗ | 0.212 | 3.187 | 2.713 | 3.722 |
| Credit to GDP (%) | -0.036 | 69.850{}^{\phantom{\*\*\*}} | 3.945 | 69.803 | 61.293 | 78.018 |
| CET1 to RWA (%) | -1.310 | 13.567∗∗∗ | 6.549 | 12.590 | 8.016 | 30.054 |
| Interbank lending | 31.021 | 276.965∗∗∗ | 239.211 | 240.123 | 0.000 | 901.990 |
| Net wealth of firms (% share) | -0.086 | 16.266∗∗∗ | 1.023 | 16.358 | 12.912 | 18.219 |
| Net wealth of banks (% share) | -0.296 | 3.234∗∗∗ | 1.071 | 3.066 | 1.560 | 7.116 |
| Net wealth of households (% share) | 0.383 | 80.500∗∗∗ | 1.123 | 80.497 | 77.748 | 83.239 |
| Default rate of firms (%) | -0.166 | 9.665∗∗∗ | 7.254 | 9.400 | 0.000 | 29.000 |
| Default rate of banks (%) | 0.127 | 1.353∗∗∗ | 5.107 | 0.000 | 0.000 | 20.000 |
| Liquidation default rate (%) | 0.003 | 0.004∗∗{}^{\*\*\phantom{\*}} | 0.210 | 0.000 | 0.000 | 0.000 |
| Firms-banks default rate (%) | 0.080 | 1.291∗∗∗ | 4.500 | 0.000 | 0.000 | 20.000 |
| Banks-banks default rate (%) | 0.033 | 0.119∗∗∗ | 2.029 | 0.000 | 0.000 | 0.000 |
| Banks-firms default rate (%) | 0.001 | 0.002∗∗{}^{\*\*\phantom{\*}} | 0.050 | 0.000 | 0.000 | 0.000 |
| Liquidation losses of banks to gdp (%) | 0.002 | 0.353∗∗∗ | 0.080 | 0.343 | 0.212 | 0.587 |
| Firms-banks losses to gdp (%) | -0.016 | 0.830∗∗∗ | 0.063 | 0.820 | 0.722 | 0.994 |
| Banks-banks losses to gdp (%) | -0.009 | 0.187∗∗∗ | 0.071 | 0.177 | 0.045 | 0.407 |
| Banks-firms losses to gdp (%) | 0.006 | 0.157∗∗∗ | 0.038 | 0.151 | 0.093 | 0.272 |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Table 4: Comparison of scenarios: CBDC2 rule. Deviation from baseline mean (dev), mean (mean), standard deviation (sd), median (med), 1st (P01P\_{01}) and 99th (P99P\_{99}) percentile. The deviation from the baseline is expressed in percentage points for rates and ratios or as percentage change for variables in level (real GDP, interbank lending).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CBDC3 | | | | | |
| Variable | dev | mean | sd | med | 𝐏𝟎𝟏\mathbf{P\_{01}} | 𝐏𝟗𝟗\mathbf{P\_{99}} |
| Output | -0.363 | 1625.032∗∗∗ | 163.756 | 1644.434 | 980.881 | 1908.625 |
| Real GDP | -0.237 | 1592.957∗∗∗ | 141.114 | 1619.662 | 980.881 | 1793.195 |
| Unemployment rate (%) | 0.205 | 10.037∗∗∗ | 3.173 | 9.560 | 5.120 | 22.840 |
| Inflation rate (%) | -0.003 | -0.001{}^{\phantom{\*\*\*}} | 1.096 | 0.009 | -2.481 | 2.482 |
| Interest rate to firms (%) | 0.088 | 3.236∗∗∗ | 0.208 | 3.228 | 2.774 | 3.747 |
| Credit to GDP (%) | -0.104 | 69.782∗∗∗ | 4.658 | 69.900 | 58.324 | 78.635 |
| CET1 to RWA (%) | -1.421 | 13.456∗∗∗ | 9.682 | 11.840 | 7.855 | 37.878 |
| Interbank lending | 65.286 | 349.398∗∗∗ | 256.957 | 321.721 | 0.000 | 993.164 |
| Net wealth of firms (% share) | -0.262 | 16.090∗∗∗ | 1.185 | 16.236 | 11.424 | 18.173 |
| Net wealth of banks (% share) | -0.353 | 3.178∗∗∗ | 1.225 | 2.925 | 1.448 | 8.175 |
| Net wealth of households (% share) | 0.614 | 80.732∗∗∗ | 1.183 | 80.731 | 77.881 | 83.686 |
| Default rate of firms (%) | -0.377 | 9.454∗∗∗ | 7.312 | 9.200 | 0.000 | 29.200 |
| Default rate of banks (%) | 0.139 | 1.365∗∗∗ | 5.456 | 0.000 | 0.000 | 30.000 |
| Liquidation default rate (%) | 0.011 | 0.013∗∗∗ | 0.384 | 0.000 | 0.000 | 0.000 |
| Firms-banks default rate (%) | -0.037 | 1.175{}^{\phantom{\*\*\*}} | 4.175 | 0.000 | 0.000 | 20.000 |
| Banks-banks default rate (%) | 0.140 | 0.226∗∗∗ | 2.816 | 0.000 | 0.000 | 0.000 |
| Banks-firms default rate (%) | 0.001 | 0.003∗∗∗ | 0.063 | 0.000 | 0.000 | 0.000 |
| Liquidation losses of banks to gdp (%) | 0.035 | 0.386∗∗∗ | 0.118 | 0.365 | 0.195 | 0.760 |
| Firms-banks losses to gdp (%) | -0.041 | 0.804∗∗∗ | 0.065 | 0.794 | 0.693 | 0.982 |
| Banks-banks losses to gdp (%) | 0.076 | 0.272∗∗∗ | 0.101 | 0.257 | 0.092 | 0.600 |
| Banks-firms losses to gdp (%) | 0.027 | 0.177∗∗∗ | 0.051 | 0.169 | 0.090 | 0.330 |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Table 5: Comparison of scenarios: CBDC3 rule. Deviation from baseline mean (dev), mean (mean), standard deviation (sd), median (med), 1st (P01P\_{01}) and 99th (P99P\_{99}) percentile. The deviation from the baseline is expressed in percentage points for rates and ratios or as percentage change for variables in level (real GDP, interbank lending).



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CBDC4 | | | | | |
| Variable | dev | mean | sd | med | 𝐏𝟎𝟏\mathbf{P\_{01}} | 𝐏𝟗𝟗\mathbf{P\_{99}} |
| Output | -0.484 | 1623.055∗∗∗ | 168.617 | 1644.334 | 940.086 | 1904.701 |
| Real GDP | -0.350 | 1591.144∗∗∗ | 146.483 | 1619.531 | 940.086 | 1791.149 |
| Unemployment rate (%) | 0.258 | 10.090∗∗∗ | 3.277 | 9.600 | 5.240 | 23.660 |
| Inflation rate (%) | 0.001 | 0.003{}^{\phantom{\*\*\*}} | 1.104 | 0.011 | -2.477 | 2.489 |
| Interest rate to firms (%) | 0.091 | 3.240∗∗∗ | 0.201 | 3.232 | 2.779 | 3.729 |
| Credit to GDP (%) | -0.057 | 69.829∗∗{}^{\*\*\phantom{\*}} | 4.794 | 69.948 | 57.865 | 78.864 |
| CET1 to RWA (%) | -1.393 | 13.484∗∗∗ | 10.340 | 11.737 | 7.848 | 41.158 |
| Interbank lending | 64.781 | 348.329∗∗∗ | 247.554 | 328.603 | 0.000 | 973.072 |
| Net wealth of firms (% share) | -0.337 | 16.014∗∗∗ | 1.243 | 16.194 | 11.076 | 18.127 |
| Net wealth of banks (% share) | -0.365 | 3.165∗∗∗ | 1.244 | 2.896 | 1.452 | 8.397 |
| Net wealth of households (% share) | 0.702 | 80.820∗∗∗ | 1.198 | 80.790 | 77.992 | 84.177 |
| Default rate of firms (%) | -0.437 | 9.394∗∗∗ | 7.330 | 9.000 | 0.000 | 29.700 |
| Default rate of banks (%) | 0.213 | 1.439∗∗∗ | 5.719 | 0.000 | 0.000 | 30.000 |
| Liquidation default rate (%) | 0.017 | 0.019∗∗∗ | 0.472 | 0.000 | 0.000 | 0.000 |
| Firms-banks default rate (%) | 0.002 | 1.214{}^{\phantom{\*\*\*}} | 4.300 | 0.000 | 0.000 | 20.000 |
| Banks-banks default rate (%) | 0.169 | 0.255∗∗∗ | 2.995 | 0.000 | 0.000 | 10.000 |
| Banks-firms default rate (%) | 0.002 | 0.004∗∗∗ | 0.100 | 0.000 | 0.000 | 0.000 |
| Liquidation losses of banks to gdp (%) | 0.036 | 0.387∗∗∗ | 0.098 | 0.380 | 0.185 | 0.652 |
| Firms-banks losses to gdp (%) | -0.048 | 0.798∗∗∗ | 0.062 | 0.788 | 0.686 | 0.961 |
| Banks-banks losses to gdp (%) | 0.087 | 0.283∗∗∗ | 0.098 | 0.280 | 0.080 | 0.580 |
| Banks-firms losses to gdp (%) | 0.027 | 0.177∗∗∗ | 0.044 | 0.175 | 0.081 | 0.297 |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Table 6: Comparison of scenarios: CBDC4 rule. Deviation from baseline mean (dev), mean (mean), standard deviation (sd), median (med), 1st (P01P\_{01}) and 99th (P99P\_{99}) percentile. The deviation from the baseline is expressed in percentage points for rates and ratios or as percentage change for variables in level (real GDP, interbank lending).

Assuming a flat 10% conversion rule of deposits in CBDC (CBDC0 rule), we observe an average negative effect on output and real GDP. Unemployment goes up but in a limited way. Although the differences with respect to the baseline model are small, they turn out to be statistically significant.
A different outcome is observed with the CBDC1 rule that allows for the substitution up to 80%80\% of deposits.
On average, the reduction of GDP and the increase in unemployment are around 0.5%0.5\%.
By construction the amount of money is fixed, and therefore almost no effect is observed on inflation in both scenarios.

In extreme events, limited effects are observed for a flat scenario (CBDC0 rule).
Instead, the CBDC1 rule produces significant effects: GDP could reduce to 51%51\% of the baseline scenario (1st percentile) and unemployment could go up to 29.7%29.7\% (from 17.4%17.4\%) (99th percentile).
The results show that allowing for large withdrawals of deposits may exacerbate fluctuations in the economy.
A tight cap on CBDC adoption and a deposit insurance scheme (CBDC2-4 rules) produce macroeconomic effects only marginally stronger than those observed under the CBDC0 rule.

The CBDC adoption affects the credit intermediation of banks. In all scenarios, the average interest rate on loans to firms goes up but for a limited amount (up to 11 basis points). Also, the credit in the economy on average displays a limited reduction (non significant in case of CBDC0 rule). It is interesting to notice that even in the high-substitution scenario (CBDC1 rule) the average effects are limited, half the effect estimated for the US in Nyffenegger,  ([2024](https://arxiv.org/html/2510.21071v1#bib.bib29)).

CBDC affects the balance sheet of banks.
As suggested in Adalid et al.,  ([2022](https://arxiv.org/html/2510.21071v1#bib.bib1)), in all scenarios, banks rely on the interbank market to meet liquidity needs due to substitution of deposits with CBDC.
The effect turns out to be the strongest under the CBDC1 rule both on average and in extreme events.
The substitution of deposits with CBDC renders banks less capitalized (CET1 ratio decreases on average) with an increase in bank defaults.
This leads to more frequent liquidation of assets with larger losses for banks.
The phenomena are more pronounced in the large substitution scenario (CBDC1 rule).

Substitution of deposits into CBDC induces a redistribution of wealth, from firms and banks to households.
The redistribution is a consequence of the increased financial instability associated with the introduction of CBDC. Bank defaults triggered by the substitution of deposits with CBDC have asymmetric effects on banks, firms and households.
By diverting wealth to CBDC households are less vulnerable when banks default which prevents losses on bank deposits. As suggested in [Williamson, 2022a](https://arxiv.org/html/2510.21071v1#bib.bib33) , bank defaults are more frequent with CBDC but they hurt households less.
Instead, banks’ wealth decreases and defaults go up, while firms’ deposits are more exposed to second-round effects of financial contagion (banks-firms defaults and banks-firms losses to GDP go up).

The introduction of a CBDC tends to lower the default rate among firms. This result can be explained by the higher funding costs faced by banks, which, due to increased reliance on interbank borrowing, are passed on to firms through higher lending rates. As a consequence, firms experience lower profits and a tighter supply of credit, which limits their ability to fully implement production plans. While this leads to reduced output, it also decreases the likelihood of default. In practice, contagion from banks plays only a minor role in firm failures; most defaults originate from systematic errors in firms’ price and quantity adjustments. When credit becomes more constrained, such mistakes are less likely to result in insolvency, since firms depend more on their own resources to finance production. These dynamics are especially evident under the CBDC1 rule: the possibility of replacing a significant share of deposits with CBDC reduces firms’ net wealth and growth but also lowers their default rates. Overall, in a CBDC environment, firms tend to be smaller but financially sounder.

![Refer to caption](figures/CBDC_ts.png)


Figure 3: Median values for the time series.

![Refer to caption](figures/CBDC_cdf.png)


Figure 4: Complementary cumulative distribution functions (CCDFs) of selected variables, CCDF is defined as 1−F​(x)1-F(x), where F​(x)F(x) is the cumulative distribution function of xx.

The conversion of deposits into CBDC plays a relevant role in driving bank defaults.
In Figure [5](https://arxiv.org/html/2510.21071v1#S4.F5 "Figure 5 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we report the average probability across banks and simulations of bank’s default ignited by the conversion of deposits into CBDC (Cumulative Default Probability, CDP).
We define this specific type of bank default as a *"bank-run"*. A bank-run is characterized by the occurrence of the following events: (i) decline in bank’s deposits due to conversion into CBDC;
(ii) the bank becomes illiquid (L​R<1LR<1) and cannot borrow funds on the interbank market;
(iii) the bank’s net wealth becomes negative as the result of asset liquidation.
The probability of bank-run defaults is below 7%7\% for the conversion rules CBDC0, CBDC2-CBDC4. However, with a loose bound on the substitution of deposits (CBDC1 rule), the average cumulative probability of default of a bank after 1,000 iterations is roughly 12%12\%.
It seems that, as the share of deposits that can be converted in CBDC increases, the interbank market becomes unable to allocate liquidity among banks, mostly because shortages are more severe and the liquidity in the system is kept constant.
Allowing for a high upper-bound on the conversion of deposits into CBDC, a flight-to-quality bank-run is more frequent leading to financial instability.

![Refer to caption](figures/CBDC_tsbank_runs_allflags.png)


Figure 5: Average bank-run CDP of banks, log scale. The CDP represents the average probability (across banks and simulations) that a bank defaults by time tt.

Contagion in the financial system occurs through four channels. We assess their relevance under the different scenarios.

1. 1.

   *Losses (defaults) from liquidation* occur when the loss incurred by a bank selling its assets below their face values reduces the net wealth of the bank, eventually to a negative level which causes default.
   In the baseline model, CBDC0 and CBDC2-CBDC4 rules, both losses and defaults from banks’ liquidation are limited on average and in the extreme events.
   In contrast, the possibility of a significant withdrawal rate of deposits (CBDC1 rule) leads to an increase both of banks’ losses and defaults.
2. 2.

   *Firms-banks losses (defaults)* occur when the default of a firm on loans reduces the net wealth of the bank. The different models (baseline, CBDC0-CBDC4 rule) show similar results (on average and in extreme events).
3. 3.

   *Banks-banks, or interbank, losses (defaults)* occur when a bank’s counterparty is unable to repay its interbank obligations due to insolvency, thus reducing the net wealth of the lender banks. This channel presents similar results in the baseline model, CBDC0, CBDC2-CBDC4 rules. The magnitude is much stronger in the case when the CBDC1 rule is applied.
4. 4.

   *Banks-firms losses (defaults)* occur when the default of a bank leads to the default of one or more firms.
   When the bank’s net wealth becomes negative, it becomes insolvent and therefore may default on its deposits, thus reducing the net wealth of depositor firms.
   This channel is stronger, although to a limited extent, in the scenarios with adoption of CBDC.

In Figure [6](https://arxiv.org/html/2510.21071v1#S4.F6 "Figure 6 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we provide a representation of the CDP of a bank for the four channels. We confirm the above results. The firms-banks channel, which relates the firm default to the bank balance sheet, is by far the most relevant in all scenarios. The second and fourth channels (banks-banks and banks-firms) play a significant role in all scenarios.
A more relevant effect is observed in the case when there is a large substitution of deposits with CBDC. The channel associated with the liquidation of assets plays a small role in the baseline scenario and a limited one in those with a low upper-bound conversion rate of deposits. When a large share of withdrawal is allowed, the effect turns out to be much more relevant.
This evidence confirms that the adoption of CBDC by households with few restrictions can cause financial instability.

![Refer to caption](figures/CBDC_tscdp.png)


Figure 6: Average CDP of banks by type of default (firms-banks, banks-banks, liquidation, banks-firms). The (CDP) represents the average probability (across banks and simulations) that a bank defaults by time tt.

It is interesting to notice that financial instability implications are not only affected by the amount of CBDC but also by the smoothness of the conversion mechanism.
Under the CBDC2 scenario, the average share of wealth held in CBDC is 14.9%, compared to 7.2% under CBDC0. Nevertheless, financial instability is less pronounced in the CBDC2 scenario than in CBDC0. Figures [3](https://arxiv.org/html/2510.21071v1#S4.F3 "Figure 3 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") and [4](https://arxiv.org/html/2510.21071v1#S4.F4 "Figure 4 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") show that defaults of banks driven by two key channels (liquidation of assets and interbank defaults) with the CBDC2 rule are the closest to those observed in the baseline scenario. The observation is confirmed in Figure [5](https://arxiv.org/html/2510.21071v1#S4.F5 "Figure 5 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") for bank-run CDP, and in Figure [6](https://arxiv.org/html/2510.21071v1#S4.F6 "Figure 6 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") for both banks-banks and liquidation CDP. For ease of comparison, Table [7](https://arxiv.org/html/2510.21071v1#S4.T7 "Table 7 ‣ 4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") reports the mean values across scenarios.
These findings suggest that, from a macro-financial perspective, a smooth conversion mechanism dependent on the perceived riskiness of banks (CBDC2 rule) is less unstable than a flat rule (CBDC0 rule) or a 0-1 choice (CBDC3 and CBDC4 rule) dependent on the riskiness of banks even though it leads to the withdraw, on average, of more liquidity from the banking sector.
This observation leads us to investigate the social welfare implications and the optimal quantity of CBDC in Section [5](https://arxiv.org/html/2510.21071v1#S5 "5 Social Welfare Evaluation ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Base | CBDC0 | CBDC1 | CBDC2 | CBDC3 | CBDC4 |
| Output | 1630.948 | 1628.524∗∗∗ | 1616.192∗∗∗ | 1629.480∗{}^{\*\phantom{\*\*}} | 1625.032∗∗∗ | 1623.055∗∗∗ |
| Real GDP | 1596.738 | 1595.150∗∗{}^{\*\*\phantom{\*}} | 1588.490∗∗∗ | 1596.497{}^{\phantom{\*\*\*}} | 1592.957∗∗∗ | 1591.144∗∗∗ |
| Unemployment rate (%) | 9.832 | 9.914∗∗∗ | 10.419∗∗∗ | 9.897∗∗∗ | 10.037∗∗∗ | 10.090∗∗∗ |
| Inflation rate (%) | 0.002 | 0.002{}^{\phantom{\*\*\*}} | 0.003{}^{\phantom{\*\*\*}} | -0.001{}^{\phantom{\*\*\*}} | -0.001{}^{\phantom{\*\*\*}} | 0.003{}^{\phantom{\*\*\*}} |
| Interest rate to firms (%) | 3.149 | 3.206∗∗∗ | 3.262∗∗∗ | 3.195∗∗∗ | 3.236∗∗∗ | 3.240∗∗∗ |
| Credit to GDP (%) | 69.886 | 69.920{}^{\phantom{\*\*\*}} | 69.520∗∗∗ | 69.850{}^{\phantom{\*\*\*}} | 69.782∗∗∗ | 69.829∗∗{}^{\*\*\phantom{\*}} |
| CET1 to RWA (%) | 14.877 | 13.921∗∗∗ | 12.954∗∗∗ | 13.567∗∗∗ | 13.456∗∗∗ | 13.484∗∗∗ |
| Interbank lending | 211.390 | 305.756∗∗∗ | 361.163∗∗∗ | 276.965∗∗∗ | 349.398∗∗∗ | 348.329∗∗∗ |
| Net wealth of firms (% share) | 16.352 | 16.231∗∗∗ | 15.384∗∗∗ | 16.266∗∗∗ | 16.090∗∗∗ | 16.014∗∗∗ |
| Net wealth of banks (% share) | 3.530 | 3.348∗∗∗ | 2.855∗∗∗ | 3.234∗∗∗ | 3.178∗∗∗ | 3.165∗∗∗ |
| Net wealth of households (% share) | 80.118 | 80.422∗∗∗ | 81.761∗∗∗ | 80.500∗∗∗ | 80.732∗∗∗ | 80.820∗∗∗ |
| Default rate of firms (%) | 9.831 | 9.675∗∗∗ | 8.480∗∗∗ | 9.665∗∗∗ | 9.454∗∗∗ | 9.394∗∗∗ |
| Default rate of banks (%) | 1.226 | 1.286∗{}^{\*\phantom{\*\*}} | 1.461∗∗∗ | 1.353∗∗∗ | 1.365∗∗∗ | 1.439∗∗∗ |
| Liquidation default rate (%) | 0.002 | 0.006∗∗∗ | 0.044∗∗∗ | 0.004∗∗{}^{\*\*\phantom{\*}} | 0.013∗∗∗ | 0.019∗∗∗ |
| Firms-banks default rate (%) | 1.211 | 1.177{}^{\phantom{\*\*\*}} | 1.072∗∗∗ | 1.291∗∗∗ | 1.175{}^{\phantom{\*\*\*}} | 1.214{}^{\phantom{\*\*\*}} |
| Banks-banks default rate (%) | 0.086 | 0.156∗∗∗ | 0.368∗∗∗ | 0.119∗∗∗ | 0.226∗∗∗ | 0.255∗∗∗ |
| Banks-firms default rate (%) | 0.002 | 0.002{}^{\phantom{\*\*\*}} | 0.012∗∗∗ | 0.002∗∗{}^{\*\*\phantom{\*}} | 0.003∗∗∗ | 0.004∗∗∗ |
| Liquidation losses of banks to gdp (%) | 0.351 | 0.385∗∗∗ | 0.358∗∗∗ | 0.353∗∗∗ | 0.386∗∗∗ | 0.387∗∗∗ |
| Firms-banks losses to gdp (%) | 0.846 | 0.833∗∗∗ | 0.751∗∗∗ | 0.830∗∗∗ | 0.804∗∗∗ | 0.798∗∗∗ |
| Banks-banks losses to gdp (%) | 0.196 | 0.264∗∗∗ | 0.227∗∗∗ | 0.187∗∗∗ | 0.272∗∗∗ | 0.283∗∗∗ |
| Banks-firms losses to gdp (%) | 0.151 | 0.169∗∗∗ | 0.183∗∗∗ | 0.157∗∗∗ | 0.177∗∗∗ | 0.177∗∗∗ |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | |  |

Table 7: Mean values by scenario with statistical significance compared to Base.

## 5 Social Welfare Evaluation

The adoption of CBDC by households leads to a redistribution of wealth from firms and banks to households.
We observe an increase in the quota of wealth retained by households mostly because defaults of banks go up, firms are strongly affected by banks’ defaults and households are less affected as they retain part of their wealth as CBDC.

We investigate the welfare implications of CBDC adoption by evaluating the distribution of wealth through a social welfare function.
We consider two different social welfare functions, namely the Atkinson (SWFa​t​k\text{SWF}^{atk}) function (Atkinson et al., , [1970](https://arxiv.org/html/2510.21071v1#bib.bib6)) and the mean-variance (SWFm​v\text{SWF}^{mv}) function.
Both functions return a score that takes into account relative wealth, compared to the average level, and its dispersion. The highest social welfare is achieved when the score is equal to one.

The Atkinson social welfare function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | SWFa​t​k={[1N​∑i=1N(xix¯)1−ε]11−εif ​ε≠1∏i=1N(xix¯)1/Nif ​ε=1,\text{SWF}^{atk}=\begin{cases}\left[\frac{1}{N}\sum\_{i=1}^{N}\left(\frac{x\_{i}}{\bar{x}}\right)^{1-\varepsilon}\right]^{\tfrac{1}{1-\varepsilon}}&\text{if }\varepsilon\neq 1\\[10.00002pt] \prod\_{i=1}^{N}\left(\frac{x\_{i}}{\bar{x}}\right)^{1/N}&\text{if }\varepsilon=1\;\;,\end{cases} |  | (46) |

where NN is the number of observations, x¯\bar{x} is the mean value of the observations, and the parameter ε\varepsilon represents the aversion to inequality (higher values give more weight to lower wealth).

The mean-variance social welfare function is the arithmetic mean across households minus the variance multiplied by a parameter λ\lambda that captures inequality aversion.

|  |  |  |  |
| --- | --- | --- | --- |
|  | SWFm​v=1N​∑i=1N(xix¯)−λN​∑i=1N(xi−x¯x¯)2=1−λN​∑i=1N(xix¯−1)2.\text{SWF}^{mv}=\frac{1}{N}\sum\_{i=1}^{N}\left(\frac{x\_{i}}{\bar{x}}\right)-\frac{\lambda}{N}\sum\_{i=1}^{N}\left(\frac{x\_{i}-\bar{x}}{\bar{x}}\right)^{2}=1-\frac{\lambda}{N}\sum\_{i=1}^{N}\left(\frac{x\_{i}}{\bar{x}}-1\right)^{2}\;\;. |  | (47) |

Table [8](https://arxiv.org/html/2510.21071v1#S5.T8 "Table 8 ‣ 5 Social Welfare Evaluation ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") reports the social welfare scores evaluated on net wealth of households for the baseline scenario and the five CBDC rules.
The columns show social welfare scores for different inequality aversion parameters; the parameters for the least inequality-averse society are ε=0.5\varepsilon=0.5 and λ=0.25\lambda=0.25, while those for the most inequality-averse society are ε=2\varepsilon=2 and λ=1\lambda=1. Notice that the social welfare function levels are quite similar because the model presents very little heterogeneity (consumers share the same productivity, wages, government transfers, and initial wealth).

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scenario | Atkinson | | | | Mean-variance | | | |
|  | ε=0.5\varepsilon=0.5 | ε=1\varepsilon=1 | ε=1.5\varepsilon=1.5 | ε=2\varepsilon=2 | λ=0.25\lambda=0.25 | λ=0.5\lambda=0.5 | λ=0.75\lambda=0.75 | λ=1\lambda=1 |
| Base | 0.9937{}^{\phantom{\*\*\*}} | 0.9871{}^{\phantom{\*\*\*}} | 0.9797{}^{\phantom{\*\*\*}} | 0.9666{}^{\phantom{\*\*\*}} | 0.9938{}^{\phantom{\*\*\*}} | 0.9877{}^{\phantom{\*\*\*}} | 0.9815{}^{\phantom{\*\*\*}} | 0.9753{}^{\phantom{\*\*\*}} |
| CBDC0 | 0.9938∗∗{}^{\*\*\phantom{\*}} | 0.9873∗∗{}^{\*\*\phantom{\*}} | 0.9801∗∗{}^{\*\*\phantom{\*}} | 0.9666{}^{\phantom{\*\*\*}} | 0.9939∗{}^{\*\phantom{\*\*}} | 0.9878∗{}^{\*\phantom{\*\*}} | 0.9817∗{}^{\*\phantom{\*\*}} | 0.9756∗{}^{\*\phantom{\*\*}} |
| CBDC1 | 0.9934∗∗∗ | 0.9866∗∗∗ | 0.9793∗∗{}^{\*\*\phantom{\*}} | 0.9672{}^{\phantom{\*\*\*}} | 0.9934∗∗∗ | 0.9868∗∗∗ | 0.9801∗∗∗ | 0.9735∗∗∗ |
| CBDC2 | 0.9938∗∗∗ | 0.9874∗∗∗ | 0.9802∗∗∗ | 0.9668{}^{\phantom{\*\*\*}} | 0.9940∗∗∗ | 0.9879∗∗∗ | 0.9819∗∗∗ | 0.9759∗∗∗ |
| CBDC3 | 0.9937{}^{\phantom{\*\*\*}} | 0.9872{}^{\phantom{\*\*\*}} | 0.9799{}^{\phantom{\*\*\*}} | 0.9672{}^{\phantom{\*\*\*}} | 0.9938{}^{\phantom{\*\*\*}} | 0.9876{}^{\phantom{\*\*\*}} | 0.9815{}^{\phantom{\*\*\*}} | 0.9753{}^{\phantom{\*\*\*}} |
| CBDC4 | 0.9937{}^{\phantom{\*\*\*}} | 0.9871{}^{\phantom{\*\*\*}} | 0.9797{}^{\phantom{\*\*\*}} | 0.9676{}^{\phantom{\*\*\*}} | 0.9938{}^{\phantom{\*\*\*}} | 0.9876{}^{\phantom{\*\*\*}} | 0.9814{}^{\phantom{\*\*\*}} | 0.9752{}^{\phantom{\*\*\*}} |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Table 8: Social welfare scores for the distribution of net wealth varying the conversion rule and different inequality aversion parameter (ϵ\epsilon and λ\lambda).



|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scenario |  | Atkinson | | | | Mean-variance | | | |
|  | unemp | ε=0.5\varepsilon=0.5 | ε=1.0\varepsilon=1.0 | ε=1.5\varepsilon=1.5 | ε=2.0\varepsilon=2.0 | λ=0.25\lambda=0.25 | λ=0.50\lambda=0.50 | λ=0.75\lambda=0.75 | λ=1.00\lambda=1.00 |
| Base | 0.0980 | 0.9937 | 0.9871 | 0.9797 | 0.9666 | 0.9938 | 0.9877 | 0.9815 | 0.9753 |
| a2=0.10a\_{2}=0.10 | 0.0983 | 0.9938\*\* | 0.9873\*\* | 0.9801\*\* | 0.9666 | 0.9939\* | 0.9878\* | 0.9817\* | 0.9756\* |
| a2=0.20a\_{2}=0.20 | 0.0986\*\*\* | 0.9938\*\* | 0.9873\*\* | 0.9800\*\* | 0.9673 | 0.9939\* | 0.9878\* | 0.9817\* | 0.9756\* |
| a2=0.30a\_{2}=0.30 | 0.0987\*\*\* | 0.9938\*\*\* | 0.9874\*\*\* | 0.9802\*\*\* | 0.9668 | 0.9940\*\*\* | 0.9879\*\*\* | 0.9819\*\*\* | 0.9759\*\*\* |
| a2=0.40a\_{2}=0.40 | 0.0993\*\*\* | 0.9939\*\*\* | 0.9875\*\*\* | 0.9804\*\*\* | 0.9685 | 0.9940\*\*\* | 0.9880\*\*\* | 0.9820\*\*\* | 0.9759\*\*\* |
| a2=0.50a\_{2}=0.50 | 0.0996\*\*\* | 0.9939\*\*\* | 0.9874\*\*\* | 0.9804\*\*\* | 0.9666 | 0.9940\*\*\* | 0.9879\*\*\* | 0.9819\*\*\* | 0.9759\*\*\* |
| a2=0.60a\_{2}=0.60 | 0.1007\*\*\* | 0.9938\*\* | 0.9873\*\* | 0.9802\*\*\* | 0.9684 | 0.9939 | 0.9877 | 0.9816 | 0.9755 |
| a2=0.70a\_{2}=0.70 | 0.1017\*\*\* | 0.9937 | 0.9871 | 0.9800\* | 0.9693\*\*\* | 0.9937\*\* | 0.9874\*\* | 0.9812\*\* | 0.9749\*\* |
| a2=0.80a\_{2}=0.80 | 0.1041\*\*\* | 0.9934\*\*\* | 0.9866\*\*\* | 0.9793\*\* | 0.9672 | 0.9934\*\*\* | 0.9868\*\*\* | 0.9801\*\*\* | 0.9735\*\*\* |
| Significance levels: \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Table 9: Social welfare scores for the distribution of net wealth varying a2a\_{2} and different inequality aversion parameter (ϵ\epsilon and λ\lambda).

The results suggest that a limited amount of CBDC (CBDC0, CBDC2-4 rules) does not harm the economy and may produce small welfare improvements.
The welfare gains from the CBDC3 and CBDC4 rule are small and not statistically significant compared to the baseline model.
When the degree of inequality aversion is high (ϵ=2\epsilon=2 or λ=1\lambda=1), the welfare improvement is limited and in most of the scenarios is not statistically significant.
Confirming the analysis in Section [4](https://arxiv.org/html/2510.21071v1#S4 "4 Simulation results ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), the smooth CBDC2 rule seems to perform the best in providing a social welfare improvement.

Excluding values reported in the column for ϵ=2\epsilon=2, we always observe a lower social welfare for the CBDC1 rule compared to the no CBDC scenario. We can conclude that adoption of CBDC with a loose upper-bound harms the welfare of the economy.

In Table [9](https://arxiv.org/html/2510.21071v1#S5.T9 "Table 9 ‣ 5 Social Welfare Evaluation ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), we investigate the optimal amount of CBDC varying a2a\_{2} in CBDC2. We allow a fixed amount of CBDC (10% of deposits) and the possibility for consumers to substitute their deposits up to the fraction a2a\_{2} depending on the riskiness of the bank.
We report the social welfare scores varying a2∈[0.1, 0.8]a\_{2}\in[0.1,\ 0.8] considering the distribution of net wealth. Notice that a4=0.8a\_{4}=0.8.
As a2a\_{2} increases, we observe that unemployment goes up.
According to the Atkinson and mean-variance social welfare functions, adoption of CBDC leads to a welfare improvement in most of the cases, unless the upper-bound rate to the conversion of CBDC is above 0.60.6.
The upper-bound of the conversion rate that leads to the highest improvement of the social welfare function is around 0.40.4.

## 6 Acknowledgments

The support from the UKRI Grant entitled "The Large Agent Collider: Robust agent-based modelling as scale" awarded to Prof. Wooldridge (reference EP/W002949/1) is gratefully acknowledged.
In addition, the authors would like to acknowledge the use of the University of Oxford Advanced Research Computing (ARC) facility in carrying out this work. <http://dx.doi.org/10.5281/zenodo.22558>.
The authors acknowledge the support from the European Union - Next Generation EU - Project ‘GRINS - Growing Resilient, INclusive and Sustainable’ project (PE0000018); the National Recovery and Resilience Plan (NRRP) Spoke 4. The views and opinions expressed are only those of the authors and do not necessarily reflect those of the European Union or the European Commission.

## 7 Conclusions

Households may substitute deposits with CBDC that can be used for payments. The appealing feature for them is that, being a liability of the CB, CBDC is a safe asset. The chance to adopt it changes structurally financial intermediation in two directions: it reduces the deposits of banks and, therefore, their capability to lend to the economy, and it may exacerbate bank-runs in the case where risky banks ignite a flight-to-quality by households.
Welfare and financial stability effects associated with CBDC have not been fully analysed mostly because the existing literature focuses on exogenous bank-runs. The agent-based model proposed in this paper permits us to consider together the decision to substitute deposits with CBDC and the riskiness of banks.
In this way, we are able to properly assess the implications of CBDC introduction for systemic financial stability and the potential for digital bank-runs.
The paper contributes to the debate on CBDC in two ways: the assessment of disintermediation associated with the issuance of CBDC; and the optimal amount of CBDC.

We show that the possibility of converting deposits into CBDC may ignite a flight-to-quality bank-run, if households are allowed to convert a large fraction of liquidity into CBDC. The effect on the economy is significant with lower growth and larger fluctuations. A 30% deposit cap, alongside deposit insurance, would mitigate potential adverse effects on the broader economy.

CBDC leads to a redistribution of wealth from firms to households, with a higher default rate of banks. Banks cope with agents’ requests for liquidity by exchanging liquidity among themselves in the interbank market.
Macroeconomic and instability effects turn out to be significant only in the case where the maximum CBDC holding is set very high (80% of deposits).
We find evidence that social welfare improves when the CBDC holdings are bounded at approximately 40% of deposits. For larger holdings, the introduction of CBDC negatively affects the social welfare of the economy.

We can conclude that the fear of disintermediation associated with CBDC is largely exaggerated. The effects on the real economy due to financial disintermediation can be effectively mitigated by imposing a reasonable cap to the adoption of CBDC. The economy turns out to be resilient to a non insignificant adoption of CBDC.

## References

* Adalid et al., (2022)

  Adalid, R., Álvarez-Blázquez, Á., Assenmacher, K., Burlon, L., Dimou, M., López-Quiles, C., Fuentes, N. M., Meller, B., Muñoz, M., Radulova, P., et al. (2022).
  Central bank digital currency and bank intermediation.
  ECB Occasional Paper 2022/293, European Central Bank.
* Agur et al., (2022)

  Agur, I., Ari, A., and Dell’Ariccia, G. (2022).
  Designing central bank digital currencies.
  Journal of Monetary Economics, 125:62–79.
* Ahnert et al., (2023)

  Ahnert, T., Hoffman, P., Leonello, A., and Porcellacchia, D. (2023).
  Central bank digital currency and financial stability.
  Technical report, ECB Occasional Paper, 2023/2783.
* Andolfatto, (2021)

  Andolfatto, D. (2021).
  Assessing the impact of central bank digital currency on private banks.
  The Economic Journal, 131:525–540.
* Assenmacher et al., (2021)

  Assenmacher, K., Berentsen, A., Brand, C., and Lamersdorf, N. (2021).
  A unified framework for cbdc design: remuneration, collateral haircuts and quantity constraints.
  Technical report, European Central Bank working paper series no.2578.
* Atkinson et al., (1970)

  Atkinson, A. B. et al. (1970).
  On the measurement of inequality.
  Journal of economic theory, 2(3):244–263.
* Azzone and Barucci, (2023)

  Azzone, M. and Barucci, E. (2023).
  Evaluation of sight deposits and central bank digital currency.
  Journal of International Financial Markets, Institutions and Money, 88:101841.
* Barucci et al., (2025)

  Barucci, E., Brachetta, M., and Marazzina, D. (2025).
  The adoption of central bank digital currency.
  Management Science.
* Beaumont, (2019)

  Beaumont, M. A. (2019).
  Approximate Bayesian computation.
  Annual review of statistics and its application, 6(1):379–403.
* Brei et al., (2023)

  Brei, M., Gambacorta, L., Lucchetta, M., and Parigi, B. M. (2023).
  How effective are bad bank resolutions? New evidence from Europe.
  Journal of Financial Stability, 67:101153.
* Brunnermeier and Niepelt, (2019)

  Brunnermeier, M. K. and Niepelt, D. (2019).
  On the equivalence of private and public money.
  Journal of Monetary Economics, 106:27–41.
* Burlon et al., (2024)

  Burlon, L., Muñoz, M. A., and Smets, F. (2024).
  The optimal quantity of cbdc in a bank-based economy.
  American Economic Journal: Macroeconomics, 16(4):172–217.
* Cifuentes et al., (2005)

  Cifuentes, R., Ferrucci, G., and Shin, H. S. (2005).
  Liquidity risk and contagion.
  Journal of the European Economic Association, 3(2/3):556–566.
* Delli Gatti et al., (2011)

  Delli Gatti, D., Desiderio, S., Gaffeo, E., Cirillo, P., and Gallegati, M. (2011).
  Macroeconomics from the Bottom-up.
  Milano: Springer Milan.
* Diamond and Dybvig, (1983)

  Diamond, D. and Dybvig, P. (1983).
  Bank runs, deposit insurance, and liquidity.
  Journal of Political Economy, 91:401–419.
* Dyer et al., (2024)

  Dyer, J., Cannon, P., Farmer, J. D., and Schmon, S. M. (2024).
  Black-box Bayesian inference for agent-based models.
  Journal of Economic Dynamics and Control, 161:104827.
* European Banking Federation, (2024)

  European Banking Federation (2024).
  Banking in Europe: EBF facts & figures 2024.
  Technical report, European Banking Federation.
  Accessed: 2025-02-10.
* Fernández-Villaverde et al., (2021)

  Fernández-Villaverde, J., Sanches, D., Schilling, L., and Uhlig, H. (2021).
  Central bank digital currency: Central banking for all?
  Review of Economic Dynamics, 41:225–242.
* Gertler and Kiyotaki, (2015)

  Gertler, M. and Kiyotaki, N. (2015).
  Banking, liquidity, and bank runs in an infinite horizon economy.
  American Economic Review, 105(7):2011–43.
* Grazzini et al., (2017)

  Grazzini, J., Richiardi, M. G., and Tsionas, M. (2017).
  Bayesian estimation of agent-based models.
  Journal of Economic Dynamics and Control, 77:26–47.
* Gurgone and Iori, (2022)

  Gurgone, A. and Iori, G. (2022).
  Macroprudential capital buffers in heterogeneous banking networks: insights from an abm with liquidity crises.
  The European Journal of Finance, 28(13-15):1399–1445.
* Gurgone et al., (2018)

  Gurgone, A., Iori, G., and Jafarey, S. (2018).
  The effects of interbank networks on efficiency and stability in a macroeconomic agent-based model.
  Journal of Economic Dynamics and Control, 91:257–288.
* Herbst and Schorfheide, (2016)

  Herbst, E. P. and Schorfheide, F. (2016).
  Bayesian estimation of DSGE models.
  Princeton University Press.
* Keister and Monnet, (2022)

  Keister, T. and Monnet, C. (2022).
  Central bank digital currency: Stability and information.
  Journal of Economic Dynamics and Control, 142:104501.
* Keister and Sanches, (2023)

  Keister, T. and Sanches, D. (2023).
  Should central banks issue digital currency?
  The Review of Economic Studies, 90(1):404–431.
* Kim and Kwon, (2023)

  Kim, Y. S. and Kwon, O. (2023).
  Central bank digital currency, credit supply, and financial stability.
  Journal of Money, Credit and Banking, 55(1):297–321.
* Lenormand et al., (2013)

  Lenormand, M., Jabot, F., and Deffuant, G. (2013).
  Adaptive approximate Bayesian computation for complex models.
  Computational Statistics, 28(6):2777–2796.
* Lux, (2022)

  Lux, T. (2022).
  Bayesian estimation of agent-based models via adaptive particle Markov chain Monte Carlo.
  Computational Economics, 60(2):451–477.
* Nyffenegger, (2024)

  Nyffenegger, R. (2024).
  Central bank digital currency and bank intermediation: Medium of exchange vs. savings vehicle.
  European Economic Review, 170:104890.
* Platt, (2020)

  Platt, D. (2020).
  A comparison of economic agent-based model calibration methods.
  Journal of Economic Dynamics and Control, 113:103859.
* Popoyan et al., (2017)

  Popoyan, L., Napoletano, M., and Roventini, A. (2017).
  Taming macroeconomic instability: Monetary and macro-prudential policy interactions in an agent-based model.
  Journal of Economic Behavior & Organization, 134:117–140.
* Varaart, (2025)

  Varaart, L. A. M. (2025).
  Modelling contagious bank runs.
* (33)

  Williamson, S. (2022a).
  Central bank digital currency: Welfare and policy implications.
  Journal of Political Economy, 130(11):2829–2861.
* (34)

  Williamson, S. D. (2022b).
  Central bank digital currency and flight to safety.
  Journal of Economic Dynamics and Control, 142:104146.
* Zachary et al., (2025)

  Zachary, F., Grzegorz, H., and Andreas, S. (2025).
  The not-so-hidden risks of ’hidden-to-maturity’ accounting: on depositor runs and bank resilience.

## 8 Appendix

## Appendix A Model calibration

#### A.1 Number of agents

The number of agents is calibrated on the statistics for the 27 countries belonging to the European Union (EU).
Eurostat reports 32,721,956 enterprises operating in the EU in 2023, with a ratio of 5 persons employed per enterprise.101010Enterprise statistics by size class and NACE Rev. 2 activity (from 2021 onward), <https://doi.org/10.2908/SBS_SC_OVW> The number of employees per worker was approximately 0.84 in 2022.
For the sake of simplicity, we assume all employed workers are employees and that one household in the model corresponds to one employee. Guided by these ratios, we set the number of agents to 500 firms and 2500 households. The cardinality aims to reduce the computational burden while maintaining a reasonable number of agents to ensure meaningful interactions in the markets. Data from the European Banking Federation,  ([2024](https://arxiv.org/html/2510.21071v1#bib.bib17)) show that, at the end of 2023, there were 4,297 credit institutions, which means that the ratio of enterprises per credit institution was around 7,615. According to these ratios, considering 10 banks, we should scale up the number of firms to approximately 76,000 and the number of households to about 380,000. This would transform the model to a large-scale one, which is outside the scope of this work and would require a substantial increase in computational power and modifications to the code. We assume a 50:1 ratio, resulting in a number of 10 banks which is enough to ensure a meaningful interaction among them, especially in the interbank market, and among banks, firms, and households.

#### A.2 Initial values

The initial net wealth of the agents is derived from the data of the 20 countries in the Euro area.111111We consider 20 countries instead of 27 in the EU as aggregate monetary data are only available for the 20 country in the currency union in 2024. The net wealth of households and firms, which corresponds to deposits by assuming no liabilities, is determined from the ratios to the nominal GDP of deposits of employees and deposits of non-financial corporations. We first compute the actual ratios of deposits to GDP based on the data from the European Central Bank (ECB), which are, respectively, around 1.06 for employees and 0.90 for non-financial corporations in 2024.121212See <data.ecb.europa.eu>

•

Series key: <DWA.Q.I9.S14.A.LE.F2M.WSE.EUR.S.N> (deposits of employees)
•

Series key: <QSA.Q.N.I9.W0.S11.S1.N.A.LE.F2M.T._Z.XDC._T.S.V.N._T> (deposits placed by non-financial corporations)
•

Series key: <MNA.Q.Y.I9.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N> (GDP at market prices).
Then, we set the initial values of deposits by multiplying these ratios by the initial value of potential GDP in the model.131313Potential GDP is given by the product of the initial values of the price mark-up 1+μ01+\mu\_{0}, the wage rate W0W\_{0}, the number of households NHN^{H}, one minus a measure of the natural unemployment rate u⋆u^{\star}, and the maximum quantity of labour supplied by each household normalized to 1.

G​D​P0≡P0​Y0=(1+μ0)​W0​(1−u⋆)​NH.GDP\_{0}\equiv P\_{0}Y\_{0}=(1+\mu\_{0})W\_{0}(1-u^{\star})N^{H}.
The net wealth of banks is set at 10%10\% of the sum of households’ and firms’ deposits, i.e., the total deposits held by banks, drawn from the supervisory banking statistics for significant credit institutions directly supervised by the ECB.141414See statistics on balance sheet composition and profitability of banks in the Euro area <https://data.ecb.europa.eu/main-figures/supervisory-banking-data/balance-sheet-composition-and-profitability>.
Following this approach, the wage rate at time 0 (W0W\_{0}) works as a numéraire upon which the other monetary quantities scale.
By design, the total net wealth of agents corresponds to the total quantity of money in the system. Therefore, W0W\_{0} determines the nominal money balance and the aggregate stock of money in the economy.

#### A.3 Labour market

The unemployment rate u⋆u^{\star} is the long-term average calibrated on data for the Euro area, see Table [11](https://arxiv.org/html/2510.21071v1#S8.T11 "Table 11 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), and it is assumed to correspond to the natural rate of unemployment.

The mechanism for transitioning out of involuntary unemployment described in Section [2.1.1](https://arxiv.org/html/2510.21071v1#S2.SS1.SSS1 "2.1.1 The labour market ‣ 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") is modelled through a binomial model in which job seekers have a probability p​(s)p(s) of a successful match with a firm in nn trials:

|  |  |  |
| --- | --- | --- |
|  | p​(s)=n!k!​(n−k)!​pk​(1−p)n−k.p(s)=\frac{n!}{k!(n-k)!}p^{k}(1-p)^{n-k}\;\;. |  |

We set n=2n=2, k=1k=1, and p=0.5p=0.5, resulting in p​(s)=0.5p(s)=0.5 to match the quarterly transition probability from unemployment observed in the EU labour markets, assuming that unemployed can only move to employment but cannot leave the labour force.151515See labour market flow statistics, <https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Labour_market_flow_statistics_in_the_EU>.

#### A.4 Calibrated model parameters

Parameter values are reported in Table [10](https://arxiv.org/html/2510.21071v1#S8.T10 "Table 10 ‣ A.4 Calibrated model parameters ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

|  |  |  |
| --- | --- | --- |
| Parameter | Value | Description |
| TT | 1,0001,000 | Time length of the simulation |
| NHN^{H} | 2,5002,500 | Number of households (section [A.1](https://arxiv.org/html/2510.21071v1#A1.SSS1 "A.1 Number of agents ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| NFN^{F} | 500500 | Number of firms (section [A.1](https://arxiv.org/html/2510.21071v1#A1.SSS1 "A.1 Number of agents ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| NBN^{B} | 1010 | Number of banks (section [A.1](https://arxiv.org/html/2510.21071v1#A1.SSS1 "A.1 Number of agents ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| θH\theta^{H} | 0.30.3 | Household income tax rate ([1](https://arxiv.org/html/2510.21071v1#S2.E1 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| θF\theta^{F} | 0.30.3 | Tax rate for firms ([21](https://arxiv.org/html/2510.21071v1#S2.E21 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| θB\theta^{B} | 0.30.3 | Tax rate for banks ([39](https://arxiv.org/html/2510.21071v1#S2.E39 "In 2.4.7 Profits and losses ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| dFd^{F} | 0.06†0.06^{\dagger} | Variable component in firms’ dividends ([21](https://arxiv.org/html/2510.21071v1#S2.E21 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| δF\delta^{F} | 0.25†0.25^{\dagger} | Dividend share of firms ([21](https://arxiv.org/html/2510.21071v1#S2.E21 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| δB\delta^{B} | 0.49†0.49^{\dagger} | Dividend share of banks ([39](https://arxiv.org/html/2510.21071v1#S2.E39 "In 2.4.7 Profits and losses ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| α\alpha | 11 | Labour productivity ([13](https://arxiv.org/html/2510.21071v1#S2.E13 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| c1c\_{1} | 0.80.8 | Marginal propensity to consume out of income ([4](https://arxiv.org/html/2510.21071v1#S2.E4 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| c2c\_{2} | 0.20.2 | Marginal propensity to consume out of wealth ([4](https://arxiv.org/html/2510.21071v1#S2.E4 "In 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| nc​r​e​dn^{cred} | 3 | Maximum number of attempts to borrow on the credit market (section [D.1](https://arxiv.org/html/2510.21071v1#A4.SSS1 "D.1 The matching mechanism ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ni​b​t​e​n​tn^{ibtent} | 5 | Maximum number of attempts to borrow on the interbank market (section [D.1](https://arxiv.org/html/2510.21071v1#A4.SSS1 "D.1 The matching mechanism ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| nt​e​n​tn^{tent} | 2 | Number of times consumers visit the goods market (section [D.1](https://arxiv.org/html/2510.21071v1#A4.SSS1 "D.1 The matching mechanism ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| rLr^{L} | 0.03 | Lower bound of interest rate, paid by the Central Bank on bank reserves (yearly) (section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| rDr^{D} | 0.03 | Interest rate paid by banks on deposits (yearly) (section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| rBr^{B} | 0.03 | Interest rate paid by government on bonds (yearly) (section [2.2](https://arxiv.org/html/2510.21071v1#S2.SS2 "2.2 Government and Central Bank ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| rC​B​D​Cr^{CBDC} | 0.03 | Interest rate paid by central bank on CBDC (yearly) (section [2.2](https://arxiv.org/html/2510.21071v1#S2.SS2 "2.2 Government and Central Bank ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")). |
| rHr^{H} | 0.04 | Upper bound of the interest rate (yearly) (section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| r​rrr | 0.10 | Regulatory reserve ratio, (section [2.4.1](https://arxiv.org/html/2510.21071v1#S2.SS4.SSS1 "2.4.1 Balance sheet ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| v0v\_{0} | 1−1+rL1+rH1-\frac{1+r^{L}}{1+r^{H}} | Composite parameter ([25](https://arxiv.org/html/2510.21071v1#S2.E25 "In 2.4.4 Interest rate ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), ([35](https://arxiv.org/html/2510.21071v1#S2.E35 "In 2.4.5 Interbank market ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| v1v\_{1} | 2†2^{\dagger} | Sensitivity of rfr^{f} to default probability ([25](https://arxiv.org/html/2510.21071v1#S2.E25 "In 2.4.4 Interest rate ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), ([35](https://arxiv.org/html/2510.21071v1#S2.E35 "In 2.4.5 Interbank market ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| l⋆l^{\star} | 4.4†4.4^{\dagger} | Scale parameter for leverage ([25](https://arxiv.org/html/2510.21071v1#S2.E25 "In 2.4.4 Interest rate ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| lb⁣⋆l^{b\star} | 2 | Scale parameter for leverage ([35](https://arxiv.org/html/2510.21071v1#S2.E35 "In 2.4.5 Interbank market ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| λ\lambda | 1/0.07 | Inverse CET1 ratio (regulatory leverage ratio) ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ω1\omega\_{1} | 1 | Risk weight on loans to firms ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ω2\omega\_{2} | 0.3 | Risk weight on interbank loans ([23](https://arxiv.org/html/2510.21071v1#S2.E23 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| m​a​t​u​rmatur | 1 | Loan maturity |
| τ\tau | 20 | Length of firms’ and banks’ memory and banks’ VaR horizon |
| t​a​i​ltail | 0.99 | VaR tail probability (section [2.4.2](https://arxiv.org/html/2510.21071v1#S2.SS4.SSS2 "2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| p0p\_{0} | 1 | Asset price (bonds and loans) at the beginning of each time unit ([2.4.6](https://arxiv.org/html/2510.21071v1#S2.SS4.SSS6 "2.4.6 Liquidation of assets ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ϵl​o​a​n​s\epsilon^{loans} | -0.9 | Price elasticity of loans |
| ϵb​o​n​d​s\epsilon^{bonds} | -1.5 | Price elasticity of bonds |
| aLa^{L} | 0.8 | Weight of current vs past loans in LEL^{E} (section [2.4.5](https://arxiv.org/html/2510.21071v1#S2.SS4.SSS5 "2.4.5 Interbank market ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| γq\gamma\_{q} | 0.1 | Threshold for quantity adjustment ([12](https://arxiv.org/html/2510.21071v1#S2.E12 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), ([19](https://arxiv.org/html/2510.21071v1#S2.E19 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| γp\gamma\_{p} | 0.87†0.87^{\dagger} | Threshold for price adjustment ([12](https://arxiv.org/html/2510.21071v1#S2.E12 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")), ([19](https://arxiv.org/html/2510.21071v1#S2.E19 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| qbq\_{b} | 0.4†0.4^{\dagger} | Quantity adjustment, upper bound ([12](https://arxiv.org/html/2510.21071v1#S2.E12 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| μm​a​x\mu\_{max} | 0.25 | Maximum mark-up ([19](https://arxiv.org/html/2510.21071v1#S2.E19 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| μm​i​n\mu\_{min} | 0.01 | Minimum mark-up ([19](https://arxiv.org/html/2510.21071v1#S2.E19 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| μa\mu\_{a} | 0.78†0.78^{\dagger} | Mark-up adjustment, upper bound ([19](https://arxiv.org/html/2510.21071v1#S2.E19 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| μ0\mu\_{0} | 0.19†0.19^{\dagger} | Initial mark-up on prices ([17](https://arxiv.org/html/2510.21071v1#S2.E17 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| wbw\_{b} | 0.01†0.01^{\dagger} | Wage rate adjustment, upper bound ([7](https://arxiv.org/html/2510.21071v1#S2.E7 "In 2.1.1 The labour market ‣ 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| u⋆u^{\star} | 0.0940.094 | Long-term rate of unemployment ([7](https://arxiv.org/html/2510.21071v1#S2.E7 "In 2.1.1 The labour market ‣ 2.1 Households ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| FhF\_{h} | 0.3†0.3^{\dagger} | Share of firms observed by a consumer on the goods market (section [D.1](https://arxiv.org/html/2510.21071v1#A4.SSS1 "D.1 The matching mechanism ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| bidb\text{bid}\_{b} | 0.150.15 | Mark-up adjustment on the interbank bid rate, upper bound ([32](https://arxiv.org/html/2510.21071v1#S2.E32 "In 2.4.5 Interbank market ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| r​e​c​a​pFrecap^{F} | 22 | Minimum time between default and recapitalization (firms) (section [2.5](https://arxiv.org/html/2510.21071v1#S2.SS5 "2.5 Bankruptcy and new entrants ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| r​e​c​a​pBrecap^{B} | 44 | Minimum time between default and recapitalization (banks) (section [2.5](https://arxiv.org/html/2510.21071v1#S2.SS5 "2.5 Bankruptcy and new entrants ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ϕe​x​t\phi\_{ext} | 0.10.1 | Share of banks’ deposits invested in bonds (section [2.4.1](https://arxiv.org/html/2510.21071v1#S2.SS4.SSS1 "2.4.1 Balance sheet ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ς\varsigma | 0.150.15 | Maximum equity loss for a lender ([24](https://arxiv.org/html/2510.21071v1#S2.E24 "In 2.4.2 Credit supply ‣ 2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| ζ\zeta | 0.16†0.16^{\dagger} | Priority given to internal finance over borrowing ([14](https://arxiv.org/html/2510.21071v1#S2.E14 "In 2.3 The business sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| R​M∗RM^{\*} | 66 | Threshold risk measure for CBDC ([43](https://arxiv.org/html/2510.21071v1#S3.E43 "In 3rd item ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| R​Ml​i​mRM^{lim} | 7.67.6 | Maximum leverage for CBDC ([44](https://arxiv.org/html/2510.21071v1#S3.E44 "In 4th item ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| a​1a1 | 0.1 | CBDC share of deposits, ([42](https://arxiv.org/html/2510.21071v1#S3.E42 "In 2nd item ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| a​2a2 | 0.3 | CBDC share of deposits, ([43](https://arxiv.org/html/2510.21071v1#S3.E43 "In 3rd item ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| a​3a3 | 0.7 | CBDC share of deposits, ([44](https://arxiv.org/html/2510.21071v1#S3.E44 "In 4th item ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |
| I​T∗IT^{\*} | 5.45.4 | Insured value of deposits ([45](https://arxiv.org/html/2510.21071v1#S3.E45 "In 5th item ‣ 3 CBDC adoption ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) |

Table 10: Model parameters and calibrated values. Those values estimated by Bayesian inference are denoted by †{\dagger}.

## Appendix B Bayesian estimation

The intrinsic complexity of agent-based models makes it challenging to derive and estimate closed-form solutions of the model and requires simulation-based techniques to match real-world data. Platt,  ([2020](https://arxiv.org/html/2510.21071v1#bib.bib30)) shows that Bayesian estimation can outperform frequentist approaches for the calibration of these models. Bayesian methods are also commonly used in macroeconomics for the estimation of Dynamic Stochastic General Equilibrium (DSGE) models, see (Herbst and Schorfheide, , [2016](https://arxiv.org/html/2510.21071v1#bib.bib23)), and are increasingly adopted in the estimation of agent-based models, see (Grazzini et al., , [2017](https://arxiv.org/html/2510.21071v1#bib.bib20); Lux, , [2022](https://arxiv.org/html/2510.21071v1#bib.bib28); Dyer et al., , [2024](https://arxiv.org/html/2510.21071v1#bib.bib16)).

In our calibration, we use Bayesian inference to fit the model to the data. In other words, while some parameters in Table [10](https://arxiv.org/html/2510.21071v1#S8.T10 "Table 10 ‣ A.4 Calibrated model parameters ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") are set from the data, such as the number of households and the interest rates, other parameters, e.g. those governing the adjustment of price and production, are estimated by Bayesian inference in order to match the summary statistics of selected real-world time series.

We focus on capturing the first two statistical moments of selected time series through Bayesian inference to find a reasonable match between key simulated time series and their real-world counterparts, thus restricting the estimation scope. The description of real-world time series with their target moments is presented in Table [11](https://arxiv.org/html/2510.21071v1#S8.T11 "Table 11 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"). Means and standard deviations are computed over the same time range in which bank default data are available, except for the CET1 ratio, which is unavailable before 2015.

We cannot use Bayesian estimation to match the default rate of banks in Table [11](https://arxiv.org/html/2510.21071v1#S8.T11 "Table 11 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") as the standard deviation is not available from Brei et al.,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib10)). Still, reproducing plausible summary statistics for the the variable is relevant to this study. Therefore, we match ex post its first moment by choosing an appropriate combination of the estimated parameters among those in the acceptable set that produces a mean close to the simulated series (see Table [12](https://arxiv.org/html/2510.21071v1#S8.T12 "Table 12 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")).

| Series | Mean | Std | Range | Source |
| --- | --- | --- | --- | --- |
| Unemployment rate | 0.095 | 0.013 | 2000Q1-2019Q4 | <data.ecb.europa.eu>161616Series key: <LFSI.Q.I9.S.UNEHRT.TOTAL0.15_74.T> |
| Inflation rate (demeaned) | 0 | 0.009 | 2000Q1-2019Q4 | <data.ecb.europa.eu>171717Series key: <ICP.M.U2.N.000000.4.INX> |
| Credit to GDP | 0.713 | 0.064 | 2000Q1-2019Q4 | <data.ecb.europa.eu>181818Series key: <QSA.Q.N.I9.W0.S11.S1.C.L.LE.F3T4.T._Z.XDC_R_B1GQ_CY._T.S.V.N._T> |
| CET1 ratio | 0.150 | 0.007 | 2015Q2-2019Q4 | <data.ecb.europa.eu>191919Series key: <SUP.Q.B01.W0._Z.I4002._T.SII._Z._Z._Z.PCT.C> |
| Default rate of banks | 0.009 | na | 2000-2019 | Brei et al.,  ([2023](https://arxiv.org/html/2510.21071v1#bib.bib10)), Table 1202020We consider the ratio of recapitalized and restructured banks to the total number of banks. The standard deviation of real-world data is not available (na). |

Table 11: Target moments for the Bayesian estimation. Mean and standard deviations refer to quarterly data. Inflation is computed year-over-year. Standard deviation for the default rate of banks is not available (na).

Bayesian inference aims to find the posterior distribution of the parameters. By Bayes’ theorem, the posterior is proportional to the likelihood multiplied by the prior

|  |  |  |
| --- | --- | --- |
|  | p​(𝜽|𝐲)=p​(𝐲|𝜽)​p​(𝜽)p​(𝐲)∝p​(𝐲|𝜽)​p​(𝜽),p(\boldsymbol{\theta}|\mathbf{y})=\frac{p(\mathbf{y}|\boldsymbol{\theta})p(\boldsymbol{\theta})}{p(\mathbf{y})}\propto p(\mathbf{y}|\boldsymbol{\theta})p(\boldsymbol{\theta})\;\;, |  |

where 𝜽\boldsymbol{\theta} is an unknown parameter vector;
p​(𝜽|𝐲)p(\boldsymbol{\theta}|\mathbf{y}) is the posterior distribution of 𝜽\boldsymbol{\theta} given the observed data
𝐲=y1,⋯,yn\mathbf{y}={y\_{1},\cdots,y\_{n}}; p​(𝜽)p(\boldsymbol{\theta}) is the prior distribution of the parameters 𝜽\boldsymbol{\theta}, namely the belief about the distribution before observing the data;
p​(𝐲)=∫p​(𝐲|𝜽)​p​(𝜽)​𝑑𝜽p(\mathbf{y})=\int p(\mathbf{y}|\boldsymbol{\theta})p(\boldsymbol{\theta})d\boldsymbol{\theta} is the the marginal probability of 𝐲\mathbf{y}. The likelihood function p​(𝐲|𝜽)p(\mathbf{y}|\boldsymbol{\theta}) represents the conditional probability of 𝐲\mathbf{y} given that the parameter vector 𝜽\boldsymbol{\theta} is true.

Although conceptually simple, estimation of the likelihood presents significant computational obstacles. Instead of computing or estimating the likelihood function, we use an estimation algorithm that produces an approximate estimate of the posterior distribution of parameters. In other words, we resort to a likelihood-free method belonging to the Approximate Bayesian Computation (ABC) family (for an overview on ABC, see Beaumont, , [2019](https://arxiv.org/html/2510.21071v1#bib.bib9)).

Instead of evaluating likelihood, ABC methods use the concept of rejection sampling. A set of parameters drawn from the prior is accepted if the distance between summary statistics of some kind of simulated and real data falls below a given threshold and is rejected otherwise. In other words, if the model outcome is close enough to the data, the set of parameters is deemed satisfactory to approximate the true posterior and so to reproduce the target data via ABM simulations.

The chosen summary statistic is the mean of simulated time series, computed after removing the first 500 transient periods. The distance function dd measures the deviation between the summary statistics of the simulated time series and the real data. For this estimation problem, we use the Euclidean norm of the difference between the mean of the simulated time series (μs​i​m\mu\_{sim}) and the mean of real data (μo​b​s\mu\_{obs}), normalized by the standard deviation of real data (σo​b​s\sigma\_{obs}):

|  |  |  |
| --- | --- | --- |
|  | d=[∑kK(μs​i​m,k−μo​b​s,kσo​b​s,k)2]1/2.d=\left[\sum\_{k}^{K}\left(\frac{\mu\_{sim,k}-\mu\_{obs,k}}{\sigma\_{obs,k}}\right)^{2}\right]^{1/2}\;\;. |  |

Computing the posterior distribution requires sampling many times from the prior and retaining those samples whose distance falls below a tolerance threshold. The strategy for computing the posterior is known as the sampling scheme. We implement an efficient sampling scheme based on the algorithm proposed in Lenormand et al.,  ([2013](https://arxiv.org/html/2510.21071v1#bib.bib27)), defined as Adaptive Population Monte Carlo (APMC). In a nutshell, APMC refines the classical Sequential Monte Carlo (SMC) scheme by producing unbiased estimates of the posterior, providing an adaptive tolerance threshold and a stop criterion, and reducing the computational cost compared to other SMC schemes.212121The authors show that the performance of APMC is higher when compared to a Population Sequential Monte Carlo, Replenishment Sequential Monte Carlo, Adaptive Sequential Monte Carlo, and a Rejection-based ABC.

In our implementation, the key steps of the algorithm are as follows.

1. 0.

   Set the initial values: number of combinations of parameter values (particles) N=200N=200,
   weights of all particles ωi=1/N, 1≤i≤N\omega\_{i}=1/N,\;1\leq i\leq N, minimum acceptance level ρa​c​cm​i​n=0.05\rho\_{acc\_{min}}=0.05, and the quantile α=0.5\alpha=0.5.
2. 1.

   Sample NN particles (θ)i=1,…,N(\theta)\_{i=1,\dots,N} from the prior distribution p​(θ)p(\mathbf{\theta}) with a Latin hypercube.
3. 2.

   For each particle, simulate M​CMC replicates of the model (Monte Carlo) of length T=1,000T=1,000 under a set of random seeds of length M​CMC.
4. 3.

   Discard burn-in time Tb​u​r​n​i​n=500T\_{burnin}=500 from the simulated series, merge them across Monte Carlo simulations, and compute summary statistics.
5. 4.

   Compute the distance dd between summary statistics from the simulated and real data.
6. 5.

   Retain the α​N\alpha N particles whose distance is below a tolerance threshold defined as the α\alpha-quantile of distances.
7. 6.

   Resample N−α​NN-\alpha N new particles from a Gaussian probability density function, whose parameters are estimated from the retained particles and assign them weights.
8. 7.

   Concatenate the retained particles α​N\alpha N and the newly sampled particles N−α​NN-\alpha N
9. 8.

   Repeat 2.-7.
10. 9.

    Stop when the proportion of newly sampled particles N−α​NN-\alpha N whose distance is below the threshold level ε\varepsilon is less than the minimum acceptance level ρa​c​cm​i​n\rho\_{acc\_{min}} or the maximum number of iterations is reached.

We start from a set of N=2,000N=2,000 particles for 14 free parameters. Each particle is simulated M​C=5MC=5 times. The APMC algorithm is repeated 50 times, resulting in a total number of simulations of 500,000. The computations were performed using MATLAB’s parallel parfor loop on a 48 multicore high-performance computing cluster, for which we acknowledge the use of the University of Oxford Advanced Research Computing (ARC) facility in carrying out this work. The accepted distances and the minimum acceptance rates in simulations are represented in Figure [7](https://arxiv.org/html/2510.21071v1#S8.F7 "Figure 7 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

![Refer to caption](figures/posterior_quality_vs_cost.png)


Figure 7: Accepted distances (left) and acceptance rates (right) for the Adaptive Population Monte Carlo estimation.

The estimation results satisfactorily replicate the key properties observed in real-world data.
The root mean square deviations (RMSD) for the mean and standard deviation from the target real-world series are reported in Table [12](https://arxiv.org/html/2510.21071v1#S8.T12 "Table 12 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model"), where the simulated model uses the estimated parameters.
Kernel density estimates of the probability distribution function of simulated and real-world series are in Figure [8](https://arxiv.org/html/2510.21071v1#S8.F8 "Figure 8 ‣ Appendix B Bayesian estimation ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").
The simulated time series show small deviations from the target series for mean and the standard deviation of the unemployment and inflation rate, while the standard deviation of the simulated CET1 ratio is around one order of magnitude above the target.
The estimated parameters are reported in Table [10](https://arxiv.org/html/2510.21071v1#S8.T10 "Table 10 ‣ A.4 Calibrated model parameters ‣ Appendix A Model calibration ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

|  | Mean | | | Std | | |
| --- | --- | --- | --- | --- | --- | --- |
| Variable | Simulated | Target | RMSD | Simulated | Target | RMSD |
| Unemployment rate | 0.098 | 0.095 | 0.003 | 0.026 | 0.013 | 0.013 |
| Inflation rate | 0.000 | 0.000 | 0.000 | 0.011 | 0.009 | 0.001 |
| Credit to GDP | 0.699 | 0.713 | 0.014 | 0.037 | 0.064 | 0.027 |
| CET1 ratio | 0.149 | 0.150 | 0.001 | 0.059 | 0.007 | 0.052 |
| Bank default rate | 0.012 | 0.007 | 0.005 | 0.048 | 0.004 | 0.044 |

Table 12: Root Mean Square Deviation (RMSD) for mean and standard deviation of simulated time series compared to real-world targets. Statistics are computed on 100 replicates.

![Refer to caption](figures/estimation_density_comparison.png)


Figure 8: 
Kernel density estimates for probability distribution functions simulated series (Model, blue) and real-world data (Data, red). Means (dashed lines) and standard deviations (dotted lines) are shown in their respective colours.

## Appendix C Accounting

The model’s equations are classified into behavioural and accounting equations.
The model includes both *stock* and *flow* variables. Consistency across the equations is verified through a stock-flow consistent accounting system. It is composed of a *transactions flow matrix* (Tab. [13](https://arxiv.org/html/2510.21071v1#S8.T13 "Table 13 ‣ C.1 Aggregate balance sheet and transactions matrix ‣ Appendix C Accounting ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")) and a *balance sheet matrix* (Tab. [14](https://arxiv.org/html/2510.21071v1#S8.T14 "Table 14 ‣ C.1 Aggregate balance sheet and transactions matrix ‣ Appendix C Accounting ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model")). The former captures the changes in stock variables between the beginning and the end of each period, while the latter shows the level of these variables at a given point in time, providing an accountancy-based representation of the model.

#### C.1 Aggregate balance sheet and transactions matrix

Table [13](https://arxiv.org/html/2510.21071v1#S8.T13 "Table 13 ‣ C.1 Aggregate balance sheet and transactions matrix ‣ Appendix C Accounting ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") represents the aggregate balance sheet of the economic system. Each row and column sums to zero, ensuring that every transaction recorded for one class of agents is offset by an equivalent entry for the corresponding counterpart.

Since it is assumed that (i) there is no physical capital and (ii) inventories are perishable, the firms’ accounts sum to zero and the sum of all the net wealth is zero, so that the government has a negative net wealth:222222In a model with physical capital and/or inventories the sum of the latter plus the sum of the net wealth should be zero.

|  |  |  |
| --- | --- | --- |
|  | ∑i∈NHn​wiH+∑j∈NFn​wjF+∑h∈NBn​whB+n​wG=0.\sum\_{i\in N^{H}}nw^{H}\_{i}+\sum\_{j\in N^{F}}nw^{F}\_{j}+\sum\_{h\in N^{B}}nw^{B}\_{h}+nw^{G}=0\;\;. |  |

Table [14](https://arxiv.org/html/2510.21071v1#S8.T14 "Table 14 ‣ C.1 Aggregate balance sheet and transactions matrix ‣ Appendix C Accounting ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model") captures the aggregate exchanges taking place in the system. Each flow originates from one class of agents and is directed toward another, while intra-class flows are omitted at the aggregate level. These flows are reported in the rows of the matrix.
The aggregate flows associated with each class of agents are represented in the columns and can be divided into current accounts (CA) and capital accounts (KA). The current account records the inflows and outflows arising from payments and earnings, whereas the capital account captures changes in the agents’ balance sheets, that is, variations in their assets and liabilities.

|  | HH | FF | BB | CB | Gov | ∑\sum |
| --- | --- | --- | --- | --- | --- | --- |
| Deposits | +DH+D^{H} | +DF+D^{F} | −DB-D^{B} |  |  | 0 |
| Loans |  | −LF-L^{F} | +LF+L^{F} |  |  | 0 |
| Bonds |  |  | +BB+B^{B} | +BC​B+B^{CB} | −B-B | 0 |
| Reserves |  |  | +R+R | −R-R |  | 0 |
| CBDC | +C​B​D​C+CBDC |  |  | −C​B​D​C-CBDC |  | 0 |
| Net Worth | −n​wH-nw^{H} | −n​wF-nw^{F} | −n​wB-nw^{B} | −n​wC​B-nw^{CB} | −n​wG-nw^{G} | 0 |
| ∑\sum | 0 | 0 | 0 | 0 | 0 | 0 |

Table 13: Aggregate Balance Sheet

Variables measured at current prices. Assets (+), liabilities (-).
  
HH = Households, FF = Firms, BB = Banks, CB = Central Bank, Gov = Government.

|  | HH | FF | | BB | | CB | | Gov | ∑\sum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | CA | KA | CA | KA | CA | KA |  |  |
| Consumption | −C-C | +C+C |  |  |  |  |  |  | 0 |
| Transfers | +G+G |  |  |  |  |  |  | −G-G | 0 |
| Production |  | +P​Y+PY |  |  |  |  |  |  | 0 |
| Wages | +W​N+WN | −W​N-WN |  |  |  |  |  |  | 0 |
| Taxes | −TH-T^{H} | −TF-T^{F} |  | −TB-T^{B} |  |  |  | +T+T | 0 |
| Profits Firms | +δ​ΠF+\delta\Pi^{F} | −ΠF-\Pi^{F} | +(1−δ)​ΠF+(1-\delta)\Pi^{F} |  |  |  |  |  | 0 |
| Profits Banks | +δ​ΠB+\delta\Pi^{B} |  |  | −ΠB-\Pi^{B} | +(1−δ)​ΠB+(1-\delta)\Pi^{B} |  |  |  | 0 |
| Profits CB |  |  |  |  |  | −ΠC​B-\Pi^{CB} |  | +ΠC​B+\Pi^{CB} | 0 |
| Deposits Interest | +rD​DH+r^{D}D^{H} | +rD​DF+r^{D}D^{F} |  | −rD​D-r^{D}D |  |  |  |  | 0 |
| Loans Interest |  | −rf​Lf-r^{f}{L}^{f} |  | +rf​Lf+r^{f}{L}^{f} |  |  |  |  | 0 |
| Bonds Interest |  |  |  |  |  | +rB​B+r^{B}B |  | −rB​B-r^{B}B | 0 |
| Reserves Interest |  |  |  | +rR​R+r^{R}R |  | −rR​R-r^{R}R |  |  | 0 |
| Δ\Delta Loans |  |  | +Δ​L+\Delta L |  | −Δ​L-\Delta L |  |  |  | 0 |
| Δ\Delta Bonds |  |  |  |  |  |  | −Δ​B-\Delta B | +Δ​B+\Delta B | 0 |
| Δ\Delta Reserves |  |  |  |  | −Δ​R-\Delta R |  | +Δ​R+\Delta R |  | 0 |
| Δ\Delta Deposits | −Δ​DH-\Delta D^{H} |  | −Δ​DF-\Delta D^{F} |  | +Δ​D+\Delta D |  |  |  | 0 |
| ∑\sum | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Table 14: Aggregate Transactions Flow Matrix

Variables measured at current prices. Sources of funds (+), uses of funds (-).
  
HH = Households, FF = Firms, BB = Banks, CB = Central Bank, Gov = Government.

## Appendix D Matching and networks structures

#### D.1 The matching mechanism

A matching mechanism governs interactions in the goods market. At each time step, households observe a randomly selected subset of firms, rank them in ascending order based on prices, and allocate their consumption budget prioritising the lowest-priced firms. This process, which can be repeated nt​e​n​tn^{tent} times by each household, continues until either the consumption budget is fully spent or all firms in the observed subsets have been visited.
Although any household can potentially visit any firm in the market, it can interact with only a fraction Fh∈(0,1]F\_{h}\in(0,1] of them in each time period. This friction is introduced to capture the presence of search costs. If Fh=1F\_{h}=1, then households can access all firms and consequently are likely to allocate their entire consumption budget to the lowest priced sellers, leaving the higher priced firms unable to sell their output. Instead, for lower values of FhF\_{h}, where households can visit only a limited subset of firms, buyers may fail to exhaust their budgets, even though higher-priced sellers might experience higher sales than in the full-access scenario. This dynamic reveals a trade-off between demand rationing and unsold output, contingent upon the value of FhF\_{h}.

In the credit market, each borrower is initially matched with a lender based on a predetermined credit fitness value.
Borrowers are sorted in ascending order by probability of default so that riskier firms are the first to be rationed when the available credit supply falls short of aggregate demand. This rule reflects the principle that, under credit supply constraints, banks aim to mitigate exposure by prioritizing lending to less risky counterparties.
Firms enter the market one by one. A borrower firm jj can switch from lender bb to zz, among those with positive credit supply, through a sampling mechanism with replacement with probability

|  |  |  |
| --- | --- | --- |
|  | pj​bswitch=11+exp⁡[−κ​(νb−νz)]p\_{jb}^{\text{switch}}=\frac{1}{1+\exp\left[-\kappa(\nu\_{b}-\nu\_{z})\right]} |  |

where weights vbv\_{b} and vzv\_{z} are determined from the credit fitness xx of each bank, v=x∑xv=\frac{x}{\sum{x}}.
If the credit demand of one firm cannot be satisfied by the lender to which it is attached, it is assigned to a random new lender. Each borrower can make nc​r​e​dn^{cred} attempts to borrow.

The interbank network is fully connected, meaning that any bank can visit any other.
The reservation rate for a borrower is the same among all banks.
Borrowers enter the market in random order and bid a rate to a random seller. If the bid rate is greater than the reservation rate, borrowers can borrow the desired amount and adjust the bid rate downward, otherwise they revise the bid rate upward and try again with the next lender. All borrowers are allowed to make ni​b​t​e​n​tn^{ibtent} offers in each session of the interbank market. Further details are described in Section [2.4](https://arxiv.org/html/2510.21071v1#S2.SS4 "2.4 The banking sector ‣ 2 The model ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

#### D.2 Networks topology

The financial architecture of the system is represented by a set of interconnected networks.
We model the deposit and shareholder networks, firm-bank credit network, and the interbank network.

The first two networks are static, i.e. links are predetermined at the model initialization stage and do not change, while the firm-bank credit network and the interbank network are dynamic, i.e. links change throughout the simulation.

1. 1.

   Deposit networks specify the allocation of deposits by households and firms across banks. They are constructed through the following steps. For each agent, we draw the number of bank accounts from a Poisson distribution with parameter μ=2\mu=2. We set the minimum number of links to one to ensure that everyone is connected to a bank. Next, households or firms are matched one by one to a set of randomly selected banks. Deposits are equally divided over links. Summary statistics for the deposit networks are reported in Table [15](https://arxiv.org/html/2510.21071v1#S8.T15 "Table 15 ‣ item 1 ‣ D.2 Networks topology ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

   |  | mean | std | median | min | max |
   | --- | --- | --- | --- | --- | --- |
   | firms links to banks | 2.1668 | 1.2495 | 2.0000 | 1.0000 | 9.0000 |
   | households links to banks | 2.1172 | 1.2599 | 2.0000 | 1.0000 | 8.0000 |
   | banks links to firms | 108.3400 | 8.0982 | 109.0000 | 90.0000 | 132.0000 |
   | banks links to households | 531.9500 | 21.8120 | 535.0000 | 478.0000 | 598.0000 |

   Table 15: Summary statistics of the depositors’ network. Statistics are computed for 10 independent random realizations of the networks.
2. 2.

   The shareholders’ network identifies the shareholders of firms and banks. Shareholders earn dividends from their affiliated firms and banks and bear bail-in responsibilities in case of bankruptcy. To match households and firms, we follow a similar mechanism as in the depositors’ network, but allow only half of the households to be shareholders, while the other half have zero links because they do not participate in the stock market.
   For banks, we create a network where the number of shareholders is proportional to a credit fitness parameters. This reflects the idea that banks with the best lending opportunities, measured by the credit fitness, are those that are more likely to grow in size and, therefore, have the largest number of shareholders. Summary statistics for the shareholders’ networks are reported in Table [16](https://arxiv.org/html/2510.21071v1#S8.T16 "Table 16 ‣ item 2 ‣ D.2 Networks topology ‣ Appendix D Matching and networks structures ‣ 8 Appendix ‣ Central Bank Digital Currency, Flight-to-Quality, and Bank-Runs in an Agent-Based Model").

   |  | mean | std | median | min | max |
   | --- | --- | --- | --- | --- | --- |
   | households links to firms | 1.0583 | 1.3736 | 0.5000 | 0.0000 | 8.0000 |
   | households links to banks | 1.0683 | 1.3817 | 1.0000 | 0.0000 | 9.0000 |
   | firms links to households | 5.2916 | 2.2500 | 5.0000 | 1.0000 | 14.0000 |
   | banks links to households | 267.0800 | 302.3296 | 140.5000 | 53.0000 | 1144.0000 |

   Table 16: Summary statistics of the shareholders’ networks. Statistics are computed on 10 independent random realizations of the networks.
3. 3.

   The firm-bank credit network captures the credit relationships between firms and banks. The network dynamically develops when banks and firms are matched in the credit market via a preferential attachment mechanism. This mechanism operates on the basis of a constant fitness score which determines attachment probabilities, and is randomly assigned to the banks at the initialization of the model, and remains fixed throughout the simulation. Credit fitness is generated from a power law distribution with an exponential cut-off, with probability density function and parameters γ=3\gamma=3 and λ=0.01\lambda=0.01:

   |  |  |  |
   | --- | --- | --- |
   |  | p​(x)=x−γ​exp⁡(−λ​x).p(x)=x^{-\gamma}\exp{(-\lambda x)}. |  |

   As a result, the firm–bank network exhibits disassortative mixing, whereby a few highly connected nodes (banks) tend to link with many nodes (firms) that have low connectivity.
4. 4.

   Banks trade funds within a fully-connected interbank network. Although the network arises endogenously through the interbank matching mechanism, it is strongly affected by the structure of the credit market. Banks are heterogeneous in their credit fitness parameter, which affects their lending opportunities to firms. As a result, the demand for interbank funds is proportional to the amount of credit lent to the real economy. This determines a topology where a few high-fitness banks demand interbank liquidity, while the remaining banks acts mostly as suppliers.