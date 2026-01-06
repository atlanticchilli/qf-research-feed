---
authors:
- Marco Ioffredi
- Stefano Marmi
- Matteo Tanzi
doc_id: arxiv:2601.01505v1
family_id: arxiv:2601.01505
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic
  Risk with Coupled Unimodal Maps'
url_abs: http://arxiv.org/abs/2601.01505v1
url_html: https://arxiv.org/html/2601.01505v1
venue: arXiv q-fin
version: 1
year: 2026
---


Marco Ioffredi
[ioffredi@stanford.edu](mailto:ioffredi@stanford.edu)
Stanford University, 450 Jane Stanford Way, Stanford, CA 94305, United States
  
Stefano Marmi
Scuola Normale Superiore, Piazza dei Cavalieri, 7, 56126 Pisa PI, Italy
  
Matteo Tanzi
King’s College London, Strand, London WC2R 2LS, United Kingdom

(January 2, 2026)

###### Abstract

Systemic financial risk refers to the simultaneous failure or destabilization of multiple financial institutions, often triggered by contagion mechanisms or common exposures to shocks. In this paper, we present a dynamical model of bank leverage — the ratio of asset holdings to equity — a quantity that both reflects and drives risk dynamics. We model how banks, constrained by Value-at-Risk (VaR) regulations, adjust their leverage in response to changes in the price of a single asset, assumed to be held in fixed proportion across banks. This leverage-targeting behavior introduces a procyclical feedback loop between asset prices and leverage. In the dynamics, this can manifest as logistic-like behavior with a rich bifurcation structure across model parameters. By analyzing these coupled dynamics in both isolated and interconnected bank models, we outline a framework for understanding how systemic risk can emerge from seemingly rational micro-level behavior.

> Financial systemic risk refers to the event in which several institutions fail simultaneously, possibly leading to large financial crisis. To model the evolution of the level of risk associated with a system, it turns out to be crucial to look at the evolution of banks’ leverage ratios, quantities that can amplify both gains and losses.
> Building on the works lillo2023unimodalmazzarisi2014dynamicalcorsi2016micro, we propose a simple analytical dynamical model for the evolution of coupled leverages and explore
> how this can lead to complex behavior within the banking system.
> In particular, we investigate how the heterogeneity in bank size and strategies of single banks may impact the stability of the whole system.
> These insights contribute to a deeper understanding of the mechanisms that can precipitate systemic crises and inform strategies for enhancing financial resilience.

## I Introduction

Several mechanisms may be responsible for the emergence of systemic risk in a system of financial institutions (or banks for simplicity), such as informational contagion leading to bank runs and liquidity shortages, direct contagion in which banks fail to pay back loans to other banks, etc.
In a broad sense, systemic risk may also be considered to include the risk associated with a system collapsing simultaneously as a result of a shock, either endogenous or exogenous (de2000systemic). For instance, in the case in which multiple banks hold positions in the same asset, a severe loss of its value would cause all banks to fail together.

This paper will primarily focus on this broader definition of systemic risk.
As briefly explained below, the dynamics of the returns of the assets (and thus the evolution of the level of systemic risk in the “broad” sense) are intimately related to the evolution of the leverages of the banks.

The leverage λ\lambda of a market agent, such as a bank, is defined as the ratio between the value of the assets held AA, i.e. the economic resources the bank owns, and the value of its equity EE, i.e. what remains of the asset value after subtracting the liabilities to which the bank is subject to.
As the name itself suggests, a large leverage means an amplification of resources invested, which is made possible by the bank borrowing money to invest (a “pumping” of money from the creditors allows the bank to amplify its invested resources) and which translates into an amplification of gains, but also losses.

The relationship between leverage and risk has indeed already been suggested by many (acharya2016banks; adrian2010liquidity; adrian2014procyclical; fostel2008leverage; huizinga2012bank; nuno2017bank), and depends on the following mechanism.
In order to maximize gain, banks want to be as leveraged as possible, as a larger leverage will in general allow for more opportunities to make profit by buying on margin.
On the other hand, banks have to face limitations on the maximum attainable leverage imposed by financial regulations in order to make the financial system more robust and resilient.

In particular, regulators require banks to define a risk measure, the Value at Risk (VaR) ΛVaR\Lambda\_{\text{VaR}}, which is associated with a certain probability of loss PVaRP\_{\text{VaR}} and is implicitly defined by

|  |  |  |
| --- | --- | --- |
|  | ∫−∞−ΛVaRf​(rp)​𝑑rp=PVaR\int\_{-\infty}^{-\Lambda\_{\text{VaR}}}f(r^{p})dr^{p}=P\_{\text{VaR}} |  |

rpr^{p} being the portfolio return and ff its probability density function.
In other words, banks are required to loose more than ΛVaR\Lambda\_{\text{VaR}} with a probability smaller than PVaRP\_{\text{VaR}}.
Having defined ΛVaR\Lambda\_{\text{VaR}}, it is required that the maximum loss, ΛVaR\Lambda\_{\text{VaR}}, be smaller than the equity of the bank. This translates in a maximum leverage that banks are allowed to set, i.e. λ≤1ΛVaR\lambda\leq\frac{1}{\Lambda\_{\text{VaR}}}.

Notice that ΛVaR\Lambda\_{\text{VaR}} depends on the variance of rpr^{p}, i.e. on the volatility of asset prices. For example, for Gaussian returns with variance σ2\sigma^{2}, a probability of loss PVaR=5%P\_{\text{VaR}}=5\% would give ΛVaR≈1.64​σ\Lambda\_{\text{VaR}}\approx 1.64\sigma.
Banks will thus make an estimate of this variance and set a target leverage λ=11.64​σ\lambda=\frac{1}{1.64\sigma}.

This leverage-targeting strategy banks may adopt can
result, due to the finite liquidity of the market, in a positive feedback between leverages and asset prices (adrian2010liquidity), possibly leading to instabilities very much like what happens in physical systems with positive feedback.
Being concrete, what happens is that if things go well, in order to maintain a certain leverage level, banks are led to borrow more; while if things go bad banks will start selling assets. For example, consider a bank having a target leverage λ=10\lambda=10, which it realizes having an asset value equal to 100100 and an equity equal to 1010.
If there is a 1%1\% portfolio return, at the next time the bank will have an asset value of 101101 and an equity equal to 1111, with a resulting leverage 10111≈9.2\frac{101}{11}\approx 9.2, which is less than the target leverage. Thus, to increase its leverage, the bank will borrow some money and increase its asset value, determining as a consequence an increase in its price.

This is also known as procyclicality of the Value-at-Risk constraint and has the effect of amplifying prices movements, which is particularly relevant during a falling period of a financial crisis.

On top of the above described feedback mechanism, another positive feedback effect may play a role.
Indeed, many estimates of risk are based on observation of recent price movements. However, the choice of the time window in the past to consider to perform such an estimate is far from trivial, since there is a trade off between choosing a long temporal window in order to improve statistical precision and choosing a short window in order to capture a more timely measure of risk.
This choice, determining the future trading strategies, endogenously moves the asset prices, resulting in a second feedback effect.
The models developed here will take both of these feedback effects into account.

This being said, it should be clear that by looking at the evolution of the leverages one could get insights in the level of systemic risk of the system.

In the case in which the banks are “similar” in the sense that they have comparable sizes and risk estimation strategies, one can reduce to study the evolution of a “representative” leverage. This is what has been done for instance in a paper by Lillo et al.lillo2023unimodal, where they obtain a slow-fast deterministic-random dynamical system for the leverage of a bank investing in a single asset.
We take this model as a starting point, and introduce heterogeneity in the system, allowing the banks to have different asset sizes and different risk estimation strategies.
In this case, disregarding random fluctuations, the system can be modeled with a discrete time dynamical system consisting of unimodal maps coupled through a mean field (see equation [1](https://arxiv.org/html/2601.01505v1#S3.E1 "In III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps") below).

In most previous works considering the impact of risk management practices on the dynamical properties of the leverages, either a single bank was considered (lillo2023analysis; aymanns2016taming) or multiple banks and multiple assets (corsi2016micro; mazzarisi2019panic) but with all banks being in some sense equivalent (they all solved the same optimization problem and their portfolios were determined by random choices in a pool of equivalent assets; thus, in particular, their leverages were at all instants equal).
The models introduced here try to go towards a more realistic direction by differentiating banks on the basis of their capital size and their risk forecasting strategies.

Other works related to the dynamical modeling of systemic risk, following some different approaches, can be found in poledna2014leverage; castellacci2015modeling; choi2012financial; choi2013financial; geanakoplos2010leverage; awiszus2022market; capponi2020swing; thurner2011systemic.
However, for example, poledna2014leverage and thurner2011systemic consider an agent-based model in which the agents don’t determine their choices on the basis of a strategy (e.g. by solving an optimization problem) and are endowed with infinite capital, while capponi2020swing and awiszus2022market don’t take into account the feedback mechanism due to the estimations of risk by the banks.

Organization of the paper.
First, the case in which there is only one bank investing in a single asset (that is the case studied in lillo2023analysis; lillo2023unimodal) is recalled.
Then, the focus will be on the case in which there are two banks investing in a single common asset. Both numerical simulations and analytical results (for some special configurations) are provided.

## II Unimodal Evolution of the Leverage for One Bank Trading One Asset

In the case in which there is only one bank investing in a single asset, the evolution of its leverage λt\lambda\_{t}, with t∈ℕt\in\mathbb{N} (in the limit in which the time scale for the financial transactions is much faster than the one used to adjust the target leverage) will turn out to be describedlillo2023unimodal by the map T:[0,1+γ]→ℝT:[0,1+\gamma]\rightarrow\mathbb{R}:

|  |  |  |
| --- | --- | --- |
|  | T​(x)=(ωx2+(1−ω)​α2​γ2​Σϵ(1+γ−x)2)−12T(x)=\left(\frac{\omega}{x^{2}}+\frac{(1-\omega)\alpha^{2}\gamma^{2}\Sigma\_{\epsilon}}{(1+\gamma-x)^{2}}\right)^{-\frac{1}{2}} |  |

so that
λt+1=T​(λt)\lambda\_{t+1}=T(\lambda\_{t}).
Here ω∈[0,1]\omega\in[0,1] quantifies the “memory" of the bank in forecasting the risk of the asset it is trading (a larger ω\omega stands for a larger weight given to past observations of the asset), while α,γ,Σϵ\alpha,\gamma,\Sigma\_{\epsilon} are parameters whose meaning will be specified later and that we will assume to be fixed.
The map TT is a unimodal map on the interval [0,1+γ][0,1+\gamma] (see Fig.[1](https://arxiv.org/html/2601.01505v1#S2.F1 "Figure 1 ‣ II Unimodal Evolution of the Leverage for One Bank Trading One Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")).

![Refer to caption](Tsketch.png)


Figure 1: Map TT for ω=0.3\omega=0.3 (Blue), ω=0.5\omega=0.5 (Orange), ω=0.8\omega=0.8 (Green). Here α=1.64\alpha=1.64, Σϵ=0.00152\Sigma\_{\epsilon}=0.0015^{2}, γ=100\gamma=100

By varying ω\omega, several qualitatively different behaviors are observed for the system, as shown in Fig. [2](https://arxiv.org/html/2601.01505v1#S2.F2 "Figure 2 ‣ II Unimodal Evolution of the Leverage for One Bank Trading One Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps").

![Refer to caption](single.png)


Figure 2: Bifurcation diagrams for TT (obtained discarding the first 1000 values and considering the next 800) for Σϵ=0.00152\Sigma\_{\epsilon}=0.0015^{2}, γ=100\gamma=100, α=1.64\alpha=1.64.

Indeed, it is interesting to study how the behavior changes as ω\omega is varied, since this is a parameter the bank can directly control.
As for the values of the other parameters employed, we follow mazzarisi2014dynamical by setting
α=1.64\alpha=1.64 and γ=100\gamma=100; Σϵ\Sigma\_{\epsilon} has been put equal to 0.001520.0015^{2} (thus smaller than the
one in the cited reference, as it is nevertheless to be expected since there only the
map obtained in the γ≫1\gamma\gg 1 is simulated, which is different from TT). The choice of this value is not crucial, as the behavior of the system does not qualitatively change
for small variations of it. However, for significantly bigger values of this parameter
(e.g. ≳0.0152\gtrsim 0.015^{2}) the behavior becomes trivial and therefore not so interesting to investigate, with the leverage reaching a fixed point for every value of ω∈[0,1]\omega\in[0,1]. It is also the case that, for these choices of parameters (and for ω\omega in a subinterval of [0,1][0,1]), one can find an invariant interval in [1,1+γ][1,1+\gamma] and can thus guarantee that λt∈[1,1+γ]\lambda\_{t}\in[1,1+\gamma] for every t∈ℕt\in\mathbb{N}, as required by the interpretation of the quantity λt\lambda\_{t} as a financial leverage (see the supplementary material for more details on this). Lastly, these choices will be the “standard ones” in
numerical simulations in the following sections as well.
Coming back to the simulations, it is observed that for smaller values of the memory ω\omega the system becomes more unstable, as can also be seen by looking at the Lyapunov of the map TT varying ω\omega (see Fig. [3](https://arxiv.org/html/2601.01505v1#S2.F3 "Figure 3 ‣ II Unimodal Evolution of the Leverage for One Bank Trading One Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps"))

![Refer to caption](single_lyap.png)


Figure 3: Lyapunov exponent for the map TT (calculated over 100 time steps) for Σϵ=0.00152\Sigma\_{\epsilon}=0.0015^{2}, γ=100\gamma=100, α=1.64\alpha=1.64.

Further, it can be proven that the set of ω\omega for which TT is periodic is dense, and the set of ω\omega for which TT is chaotic has positive Lebesgue measure (see the supplementary material for theorems useful to get these results).

## III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset

Let’s from now on focus on the case in which there are NN banks investing in a single asset. This asset can be thought of as an index.
In this case the evolution of the leverages is given by (with i∈{1,…,N}i\in\{1,...,N\}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi,t=(ωiλi,t−12+(1−ωi)​α2​γ2​Σϵ(1+γ−∑i=12πi​λi,t−1)2)−12.\lambda\_{i,t}=\left(\frac{\omega\_{i}}{\lambda\_{i,t-1}^{2}}+\frac{(1-\omega\_{i})\alpha^{2}\gamma^{2}\Sigma\_{\epsilon}}{\left(1+\gamma-\sum\_{i=1}^{2}\pi\_{i}\lambda\_{i,t-1}\right)^{2}}\right)^{-\frac{1}{2}}. |  | (1) |

Here πi∈[0,1]\pi\_{i}\in[0,1] and ∑i=1Nπi=1\sum\_{i=1}^{N}\pi\_{i}=1. The π\pis may be given the interpretation of the “weights” of the banks in term of assets owned. A derivation of this model is presented in Section [III.1](https://arxiv.org/html/2601.01505v1#S3.SS1 "III.1 The Model ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps") below. But first, we are going to summarise our observations in the case N=2N=2.

For N=2N=2 and in the “homogeneous case” in which ω1=ω2\omega\_{1}=\omega\_{2}, the two leverages will completely synchronize (see Section [III.2](https://arxiv.org/html/2601.01505v1#S3.SS2 "III.2 Homogeneous case: sychronization ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")), and this happens regardless of π1\pi\_{1}.

![Refer to caption](nuova.png)


Figure 4: Leverages synchronization for ω1=ω2=0.8,0.6,0.3\omega\_{1}=\omega\_{2}=0.8,0.6,0.3 (top to bottom) and π1=0.5\pi\_{1}=0.5

The common behavior of the two leverages will depend on the value of ω1=ω2\omega\_{1}=\omega\_{2}.

If instead the heterogeneous case is considered, in which each bank has a possibly different memory ω\omega, then the behavior can vary nontrivially depending on the values of ω1\omega\_{1}, ω2\omega\_{2} and π1\pi\_{1}.

It is useful to start by considering the limiting case where bank 1 is much smaller than bank 2 to have, with good approximation, π1=0\pi\_{1}=0 (see Section [III.3.1](https://arxiv.org/html/2601.01505v1#S3.SS3.SSS1 "III.3.1 ’Big vs small’ bank: the skew-product case ‣ III.3 Heterogeneous case ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")). This may looked at as a forced-forcing system, where bank 2 forces bank 1.
Regardless of the initial conditions, it is observed and shown that if the forcing bank is periodic, the forced bank will also show periodic, while if the forcing bank leverage evolves chaotically, then the forced bank will behave in an irregular manner (in a sense that will be made precise later) .
Thus one may say that the behavior of the smaller bank will be determined by the larger one, whose choices thus have a crucial impact on the overall stability of the market.
This scenario generalizes to the case in which there are two groups of banks, each group with its own memory, and one of the two groups weighs significantly more than the other: in this case the memory of the group weighing more determines the nature of the evolution of the whole system.

Considering now the case in which π1≠0,1\pi\_{1}\neq 0,1, interesting bifurcation diagrams for the leverages of the two banks are observed as relevant parameters are changed.
In particular, by keeping ω1\omega\_{1} and ω2\omega\_{2} fixed and changing the weight π1\pi\_{1} one observes a bifurcation diagram which “connects” the behaviors one would have in the forced-forcing systems corresponding to π1=0\pi\_{1}=0 (where only ω2\omega\_{2} has a role in determining the nature of the behavior) and π1=1\pi\_{1}=1 (where now ω1\omega\_{1} is the relevant parameter).
Therefore, for example, there exist values for ω1\omega\_{1}, ω2\omega\_{2} for which there is a threshold value for π1\pi\_{1} above which both banks switch from a regular behavior to an aperiodic one (see Fig. [5](https://arxiv.org/html/2601.01505v1#S3.F5 "Figure 5 ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps"))

![Refer to caption](etero.png)


Figure 5: Example of asymptotic orbits for the two banks as π1\pi\_{1} varies and for different choices of ω1,ω2\omega\_{1},\omega\_{2}. Here ω1=0.5,ω2=0.3\omega\_{1}=0.5,\omega\_{2}=0.3. In doing the plot, the first 1000 values have been discarded and the next 500 plotted.

One could also look at what happens if π1\pi\_{1} is fixed and ω1,ω2\omega\_{1},\omega\_{2} are varied. This may be of particular interest as the memories can be more easily and directly controlled by the bank than the weights.
In this case, having fixed π1\pi\_{1}, one observes for example that for every ω2\omega\_{2} above a certain threshold, there is a critical ω1\omega\_{1} value above which the system is stable (i.e. both leverages reach a common fixed point) and below which one observes period doubling bifurcations leading to chaos (see Fig. [6](https://arxiv.org/html/2601.01505v1#S3.F6 "Figure 6 ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")). This critical value depends on π1\pi\_{1} in such a manner that as π1\pi\_{1} gets closer to one it becomes less and less dependent on ω2\omega\_{2}. Intuitively, for large π1\pi\_{1} the stability of the system depends almost exclusively on ω1\omega\_{1}. More plots from numerical simulations can be found in the supplementary material.

![Refer to caption](bif_su_w1_p05_w204.png)


Figure 6: Example of asymptotic orbits for the two banks as ω1\omega\_{1} varies for π1=0.5\pi\_{1}=0.5 and ω2=0.4\omega\_{2}=0.4. In doing the plot, the first 1000 values have been discarded and the next 800 plotted.

Next, it is also interesting to note that whenever the behavior of the two banks is aperiodic, there is not a functional asymptotic dependence between the two leverages.
Instead, for some choice of parameters, one observes in the λ1,λ2\lambda\_{1},\lambda\_{2} plane an Hénon-like attractor (see Fig. [7](https://arxiv.org/html/2601.01505v1#S3.F7 "Figure 7 ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps") and the supplementary material). Indeed this may not be so surprising as we are dealing with a system constituted of perturbed unimodal maps which, in certain limits, can indeed be looked at as a linear transformation of an Hénon system.
It is indeed found that the attractor has a nontrivial box counting dimension of ≈1.2\approx 1.2.
For other choices of parameters, one observes other kind of attractors, as shown for instance in Fig. [8](https://arxiv.org/html/2601.01505v1#S3.F8 "Figure 8 ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")

![Refer to caption](henon.png)


Figure 7: Hénon-like attractor in the λ1\lambda\_{1} vs λ2\lambda\_{2} plane. Here π1=0.5,ω1=0.5,ω2=0.3\pi\_{1}=0.5,\omega\_{1}=0.5,\omega\_{2}=0.3

![Refer to caption](attractors.png)


Figure 8: Attractor in the λ1\lambda\_{1} vs λ2\lambda\_{2} plane. From top to bottom, left to right, π1=0.8,ω1=0.5,ω2=0.3\pi\_{1}=0.8,\omega\_{1}=0.5,\omega\_{2}=0.3; π1=0.8,ω1=0.3,ω2=0.2\pi\_{1}=0.8,\omega\_{1}=0.3,\omega\_{2}=0.2; π1=0.2,ω1=0.6,ω2=0.3\pi\_{1}=0.2,\omega\_{1}=0.6,\omega\_{2}=0.3; π1=0.001,ω1=0.6,ω2=0.3\pi\_{1}=0.001,\omega\_{1}=0.6,\omega\_{2}=0.3

### III.1 The Model

In the case of a single bank, referring to the model introduced in corsi2016micro and further developed in lillo2023unimodal; mazzarisi2019panic,
the evolution of its leverage will be the result of the following main principles: 1) to increase profit,
a bank wants to maximize its leverage up to the limit imposed by regulations; 2) this limit depends on the risk associated to the asset that is estimated by the bank in a way that can vary from bank to bank; 3) the time evolution of the prices of the asset is characterized by an autoregressive process with a time scale faster than the one in which the banks update their leverage; 4) the relative size of the total assets detained by the banks (i.e. their weights πi\pi\_{i}) are approximately constant.

The last assumption simplifies the model making it tractable analytically and leading to the theorems below. Although not universally verified, we expect it to hold in the situations we study analytically: when banks have synchronized leverages due to the same risk estimation strategies, and when one bank is several orders of magnitude larger than the others (i.e. π1≈1\pi\_{1}\approx 1). We also expect it to hold more generally in the short term, or until large shocks perturb the system (which goes beyond the scope of our model).

This results in a slow-fast deterministic-random dynamical system with heteroschedastic noise. In the limit in which the fast time scale is much faster than the slow one, this reduces to a deterministic dynamical system given in ([1](https://arxiv.org/html/2601.01505v1#S3.E1 "In III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")).
We now show how to derive this expression by generalising the derivation given in lillo2023analysis to the case of multiple banks.

At each time t∈ℕt\in\mathbb{N}, bank ii has an equity Ei,tE\_{i,t} and an amount of the asset, Ai,tA\_{i,t}. The ratio λi,t=Ai,tEi,t≥1\lambda\_{i,t}=\frac{A\_{i,t}}{E\_{i,t}}\geq 1 is called the leverage of the bank.
Each bank will try to maximize its leverage (in order to increase gains), but it will have to face VaR type constraints imposed by financial institutions.
The dynamics of the leverages is determined by two main interactions between the banks and the asset prices. First, VaR constraint determine the leverage as a function of the behavior of asset prices.
Second, a given target leverage will determine a sequence of trading events which will impact the price of the asset.
Thus one sees that it is possible to “close the circle” and obtain a law for the time evolution of the leverages.

If σe,t\sigma\_{e,t} is an estimate of portfolio variance made at time tt, VaR constraints require that the leverage of bank ii should be such that α​σe,t​Ai,t≤Ei,t\alpha\sigma\_{e,t}A\_{i,t}\leq E\_{i,t}, where α\alpha depends on the distribution of the returns of the asset and on the strictness of the constraints (for instance, it is 1.641.64 for Gaussian returns and for a VaR probability of 5%5\%).
Thus one may assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi,t=1α​σe,t\lambda\_{i,t}=\frac{1}{\alpha\sigma\_{e,t}} |  | (2) |

Now consider how fixing a target leverage impacts the movement of the asset’s price.
Having set a value for the target leverage, the bank will trade the asset between time tt and t+1t+1 in order to keep its leverage equal to this target value.
This trading process takes places at a faster pace than the one in which the target leverage is updated (i.e. at every integer time). Let’s thus introduce a quantity 𝕟∈ℕ\mathbb{n}\in\mathbb{N} so that trading operations occur 𝕟\mathbb{n} times every integer time step.
Next, call rt+k𝕟r\_{t+\frac{k}{\mathbb{n}}}, with k=1,2,…,𝕟k=1,2,\dots,\mathbb{n} the returns on investments (i.e. the ratio between the gain/loss yielded by the investment and the initial cost of the investment). The dynamics of these returns can be thought of as made of two components:

|  |  |  |
| --- | --- | --- |
|  | rt+k𝕟=ϵt+k𝕟+et+k−1𝕟;r\_{t+\frac{k}{\mathbb{n}}}=\epsilon\_{t+\frac{k}{\mathbb{n}}}+e\_{t+\frac{k-1}{\mathbb{n}}}; |  |

the first term in the RHS is an exogenous component (depending on external, non modeled events) given by a white noise term with variance σϵ2\sigma^{2}\_{\epsilon}, while the second term in the RHS is instead an endogenous component, which is the one depending on the trading actions of the bank. More in detail, the endogenous component et+h/𝕟e\_{t+h/\mathbb{n}} depends on the demand for the asset arising from portfolio rebalancing of the bank.
Given a fractional time s=t+h𝕟,h=1,2,…,𝕟s=t+\frac{h}{\mathbb{n}},h=1,2,\dots,\mathbb{n}, let’s call the desired asset size for a generic bank ii Ai,s⋆≐λi,t​Ei,sA^{\star}\_{i,s}\doteq\lambda\_{i,t}E\_{i,s}. Therefore at ss bank ii rebalances its portfolio by trading the quantity

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai,s⋆−Ai,s\displaystyle A^{\star}\_{i,s}-A\_{i,s} | =λi,t​Ei,s−Ai,s−1𝕟⋆​(1+rs)\displaystyle=\lambda\_{i,t}E\_{i,s}-A^{\star}\_{i,s-\frac{1}{\mathbb{n}}}(1+r\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λi,t​(Ei,s−1𝕟+rs​Ai,s−1𝕟⋆)−Ai,s−1𝕟⋆​(1+rs)\displaystyle=\lambda\_{i,t}(E\_{i,s-\frac{1}{\mathbb{n}}}+r\_{s}A^{\star}\_{i,s-\frac{1}{\mathbb{n}}})-A^{\star}\_{i,s-\frac{1}{\mathbb{n}}}(1+r\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(λi,t−1)​rs​Ai,s−1𝕟⋆\displaystyle=(\lambda\_{i,t}-1)r\_{s}A^{\star}\_{i,s-\frac{1}{\mathbb{n}}} |  |

The total demand for the asset will be given by

|  |  |  |
| --- | --- | --- |
|  | Ds=∑i=1N(Ai,s⋆−Ai,s)D\_{s}=\sum\_{i=1}^{N}(A^{\star}\_{i,s}-A\_{i,s}) |  |

Assuming a standard linear price impact function, the endogenous component ese\_{s} for the return of the asset is given by

|  |  |  |
| --- | --- | --- |
|  | es=Dsγ​Cse\_{s}=\frac{D\_{s}}{\gamma C\_{s}} |  |

with γ\gamma quantifying the liquidity of the asset and where

|  |  |  |
| --- | --- | --- |
|  | Cs=∑i=1NAi,s−1𝕟⋆C\_{s}=\sum\_{i=1}^{N}A^{\star}\_{i,s-\frac{1}{\mathbb{n}}} |  |

is a proxy for market capitalization of the investment. Thus:

|  |  |  |
| --- | --- | --- |
|  | rs=∑i=1N(λi,t−1)​Ai,s−2𝕟⋆γ​∑i=1NAi,s−2𝕟⋆​rs−1𝕟+ϵsr\_{s}=\frac{\sum\_{i=1}^{N}(\lambda\_{i,t}-1)A^{\star}\_{i,s-\frac{2}{\mathbb{n}}}}{\gamma\sum\_{i=1}^{N}A^{\star}\_{i,s-\frac{2}{\mathbb{n}}}}r\_{s-\frac{1}{\mathbb{n}}}+\epsilon\_{s} |  |

Let’s put, for every i∈{1,2,…,N}i\in\{1,2,\dots,N\}, πi,s=Ai,s⋆∑a=1NAa,s⋆∈[0,1]\pi\_{i,s}=\frac{A\_{i,s}^{\star}}{\sum\_{a=1}^{N}A\_{a,s}^{\star}}\in[0,1], so that ∑i=1Nπi,s=1\sum\_{i=1}^{N}\pi\_{i,s}=1.

Now notice that (recall Ai,s⋆≐λi,t​Ei,sA^{\star}\_{i,s}\doteq\lambda\_{i,t}E\_{i,s} and Ei,s=∏q=0s(1+rq)​Ei,sE\_{i,s}=\prod\_{q=0}^{s}(1+r\_{q})E\_{i,s}) if the leverages were the same for all banks, then πi,s\pi\_{i,s} would not depend on the time ss. Thus, in the homogeneous case we can consider the weights as independent of ss. Moreover, numerical simulations show that the error made by considering the weights as independent of ss even in the heterogeneous case is small enough to make it reasonable to start by analyzing the simplest case in which the weights are constant in time.
All the more reason for the fact that for the cases studied analytically more in depth (i.e. the homogeneous case and the forced-forcing one) this approximation is exact.
Let’s therefore put πi=πi,s\pi\_{i}=\pi\_{i,s} and look at πi\pi\_{i} as a measure of the “size” of bank ii.
It is then possible to write:

|  |  |  |
| --- | --- | --- |
|  | rs=∑i=1N(λi,t​πi−1)γ​rs−1𝕟+ϵsr\_{s}=\frac{\sum\_{i=1}^{N}(\lambda\_{i,t}\pi\_{i}-1)}{\gamma}r\_{s-\frac{1}{\mathbb{n}}}+\epsilon\_{s} |  |

So that the dynamics of the returns of the asset for times in (t,t+1](t,t+1] may be modeled again as a AR(1) process with auto regressive parameter

|  |  |  |
| --- | --- | --- |
|  | ϕt=∑i=1N(λi,t​πi−1)γ\phi\_{t}=\frac{\sum\_{i=1}^{N}(\lambda\_{i,t}\pi\_{i}-1)}{\gamma} |  |

which now depends on a convex combination of the leverages of the NN banks λ1,λ2,…,λN\lambda\_{1},\lambda\_{2},\dots,\lambda\_{N} in a mean field fashion.
It now remains to provide an expression for the variance of the aggregate return of the asset σe,t\sigma\_{e,t}.
A reasonable hypothesis is to assume that the estimate made at time tt is a weighted average (ω∈[0,1]\omega\in[0,1] being the weight) of the previously made estimate of the same kind and a statistical estimate of aggregate returns made by observing the returns between t−1t-1 and tt. I.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σe,t2=ω​σe,t−12+(1−ω)​σ^e,t2\sigma\_{e,t}^{2}=\omega\sigma\_{e,t-1}^{2}+(1-\omega)\hat{\sigma}^{2}\_{e,t} |  | (3) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^e,t2\displaystyle\hat{\sigma}^{2}\_{e,t} | =Var^​[∑k=1𝕟rt−1+k𝕟]\displaystyle=\widehat{\text{Var}}\left[\sum\_{k=1}^{\mathbb{n}}r\_{t-1+\frac{k}{\mathbb{n}}}\right] |  |

which is the aggregated variance of the AR(1) taking place between t−1t-1 and tt as a function of the estimates of the parameters ϕt−1\phi\_{t-1} and σϵ2\sigma\_{\epsilon}^{2}, namely ϕ^t−1\hat{\phi}\_{t-1} and σ^ϵ2\hat{\sigma}^{2}\_{\epsilon}.
In the 𝕟→∞\mathbb{n}\rightarrow\infty limit, one has σ^e,t2≈𝕟​σ^ϵ2(1−ϕ^t−1)2\hat{\sigma}\_{e,t}^{2}\approx\frac{\mathbb{n}\hat{\sigma}^{2}\_{\epsilon}}{(1-\hat{\phi}\_{t-1})^{2}}, having introduced the ML estimates for σε\sigma\_{\varepsilon} and ϕt−1\phi\_{t-1}.
Moreover, in the 𝕟→∞\mathbb{n}\rightarrow\infty limit one expects the limit lim𝕟→∞𝕟​σϵ2≐Σϵ\lim\_{\mathbb{n}\rightarrow\infty}\mathbb{n}\sigma\_{\epsilon}^{2}\doteq\Sigma\_{\epsilon} to exists. Indeed, as already noticed one may consider the AR(1) as the discretization (with discretization step 1𝕟\frac{1}{\mathbb{n}}) of an Orstein-Uhlenbeck process, and so by a scaling argument the existence of the above limit may be deduced.
Combining [2](https://arxiv.org/html/2601.01505v1#S3.E2 "In III.1 The Model ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps") and [3](https://arxiv.org/html/2601.01505v1#S3.E3 "In III.1 The Model ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps") one thus has, in the 𝕟→∞\mathbb{n}\rightarrow\infty limit,
(for i∈{1,2,…,N}i\in\{1,2,\dots,N\})

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi,t=(ωλi,t−12+(1−ω)​α2​Σϵ(1−ϕ^t−1)2)−12\lambda\_{i,t}=\left(\frac{\omega}{\lambda\_{i,t-1}^{2}}+\frac{(1-\omega)\alpha^{2}\Sigma\_{\epsilon}}{(1-\hat{\phi}\_{t-1})^{2}}\right)^{-\frac{1}{2}} |  | (4) |

Further, for 𝕟\mathbb{n} large enough ϕ^t−1\hat{\phi}\_{t-1} is a Gaussian with mean ϕt−1\phi\_{t-1} and variance 1−ϕt−12𝕟\frac{1-\phi\_{t-1}^{2}}{\mathbb{n}}. Writing thus ϕ^t−1=ϕt−1+ηt−1\hat{\phi}\_{t-1}=\phi\_{t-1}+\eta\_{t-1} where ηt−1∼𝒩​(0,1−ϕt−12𝕟)\eta\_{t-1}\sim\mathcal{N}\left(0,\frac{1-\phi\_{t-1}^{2}}{\mathbb{n}}\right) and expanding Eq. [4](https://arxiv.org/html/2601.01505v1#S3.E4 "In III.1 The Model ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps") at zeroth order, it is possible to write, for (i∈{1,2,…,N}i\in\{1,2,\dots,N\})
for i=1,2,…,Ni=1,2,\dots,N:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi,t\displaystyle\lambda\_{i,t} | =(ωiλi,t−12+(1−ωi)​α2​Σϵ(1−ϕt−1)2)−12≐Ti​({λi,t−1}i=1,2,…,N)\displaystyle=\left(\frac{\omega\_{i}}{\lambda\_{i,t-1}^{2}}+\frac{(1-\omega\_{i})\alpha^{2}\Sigma\_{\epsilon}}{\left(1-\phi\_{t-1}\right)^{2}}\right)^{-\frac{1}{2}}\doteq T\_{i}(\{\lambda\_{i,t-1}\}\_{i=1,2,\dots,N}) |  | (5) |

which is the evolution law already introduced in the previous section.
Note that, should one have considered the first order term in the expansion above, one would have obtained a heteroschedastic noise term superimposed on the deterministic skeleton given by the maps TT. This kind of system has been studied in lillo2023analysis in case N=1N=1. Here, dealing with the more general case in which N≥1N\geq 1, we aim to first understand the behavior of the deterministic skeleton before considering the random system that is based on it.

In the following, we will be interested in studying how the deterministic dynamical system defined by the TTs behaves for different choices of the sets {ωi}\{\omega\_{i}\} and {πi}\{\pi\_{i}\}.
One last remark must be done before proceeding. From the definition of leverage it is required that λt≥1​∀t∈ℕ\lambda\_{t}\geq 1\ \forall t\in\mathbb{N} and from the stationarity of the AR(1) process for rsr\_{s} it is required that |ϕt|≤1|\phi\_{t}|\leq 1, i.e. ∑i=12πi​λi,t≤1+γ​∀t∈ℕ\sum\_{i=1}^{2}\pi\_{i}\lambda\_{i,t}\leq 1+\gamma\ \forall t\in\mathbb{N}. When performing numerical simulations, initial conditions have been chosen at random in the box [1,1+γ]2[1,1+\gamma]^{2} and the simulations leading to violations of the constraints at any greater tt have been discarded.
In the following, let 𝒱⊆ℝ2\mathcal{V}\subseteq\mathbb{R}^{2} the largest set such that (for all the values of the ω\omegas and π\pis considered and for the given choices of the other parameters) by choosing initial conditions in this set the above constraints are satisfied. At least for |ω1−ω2||\omega\_{1}-\omega\_{2}| sufficiently small, it can be shown that this set is nonempty (see the supplementary material).

### III.2 Homogeneous case: sychronization

When the two banks use the same strategy in forecasting the risk, we obtain the following result.

###### Theorem 1

(Synchronization in the Homogenous Case) If ω1=ω2\omega\_{1}=\omega\_{2}, ∀(λ1,0,λ2,0)∈𝒱\forall(\lambda\_{1,0},\lambda\_{2,0})\in\mathcal{V}

|  |  |  |
| --- | --- | --- |
|  | limn→∞|T1n​(λ1,0,λ2,0)−T2n​(λ1,0,λ2,0)|=0.\lim\_{n\rightarrow\infty}|T\_{1}^{n}(\lambda\_{1,0},\lambda\_{2,0})-T\_{2}^{n}(\lambda\_{1,0},\lambda\_{2,0})|=0. |  |

I.e. the leverages of different banks approach asymptotically the same orbit. This can be proven (see the supplementary material) by observing that the quantity |λ1,t−λ2,t|λ1,t+λ2,t\frac{|\lambda\_{1,t}-\lambda\_{2,t}|}{\lambda\_{1,t}+\lambda\_{2,t}} is strictly decreasing along the orbits.
Therefore in the homogenous case it doesn’t matter (as far as the behavior of the system is concerned) if a bank is larger than the other: the only relevant parameter to describe the evolution of the system is the common memory. This allows us to reduce this system to the one dimensional one already studied.
Lastly, this result can be easily generalized to the case in which N>2N>2, obtaining that even if all the memories are the same then there will be asymptotic synchronization among the NN orbits regardless of the weights.

### III.3 Heterogeneous case

Here the case in which ω1≠ω2\omega\_{1}\neq\omega\_{2} is analyzed.

As mentioned, if π1≠0,1\pi\_{1}\neq 0,1 the behavior of the system depends nontrivially on π1,ω1\pi\_{1},\omega\_{1}, and ω2\omega\_{2} with the overall behaviour described by an interpolation of the behaviours associated to the isolated banks with memory parameters ω1\omega\_{1} and ω2\omega\_{2}. This case won’t be explored further here, as a complete rigorous understanding seems out of reach. Still, it is worth to emphasise that for some choices of the parameters a Hénon-like attractor seems to appear in the λ1\lambda\_{1} vs λ2\lambda\_{2} plane.

The box counting dimension for the attractor shown above has been calculated to be equal to 1.203±0.0061.203\pm 0.006, thus confirming its apparently fractal nature (see the supplementary material for details).
Finally, the nature of the attractor led us to consider applying the main theorem in wang2008toward about the existence of an SRB measure supported on it.
However, it seems that not all of the hypotheses can be met in our case: The main issue is that for |ω1−ω2||\omega\_{1}-\omega\_{2}| going to zero, although the attractor becomes essentially one dimensional, there is no collapse of dimensionality for ω1=ω2\omega\_{1}=\omega\_{2} and initial conditions approach the diagonal only asymptotically; whereas, for the Hénon map, when the parameter usually denoted with “bb” is zero there is a collapse of the dimensionality and all initial conditions are mapped to a 1D segment.

#### III.3.1 ’Big vs small’ bank: the skew-product case

Let’s focus here on the case with π=0\pi=0. This case may be looked at as a forcing-forced system, in which the larger bank “drives” the smaller one.
Alternatively, one may say that the dynamics of the smaller one is described by a random process where the randomness is generated by a deterministic unimodal map.
This setting is indeed a subcase of the general “heterogeneous case” previously introduced, but the fact that several interesting results may be, even rigorously, obtained makes it an interesting case to study.

The dynamics of the leverage of the second bank (the forcing one) is described by the map TT. The dynamics of the leverage of bank 1 depends on the leverage of bank 22.
One could make this dependence explicit by introducing the family of maps fyf\_{y} so that

|  |  |  |
| --- | --- | --- |
|  | λ1,t+1=fλ2,t​(λ1,t)\lambda\_{1,t+1}=f\_{\lambda\_{2,t}}(\lambda\_{1,t}) |  |

with

|  |  |  |
| --- | --- | --- |
|  | fy​(x)=(ω1x2+(1−ω1)​γ2​α2​Σϵ(1+γ−y)2)−12f\_{y}(x)=\left(\frac{\omega\_{1}}{x^{2}}+\frac{(1-\omega\_{1})\gamma^{2}\alpha^{2}\Sigma\_{\epsilon}}{(1+\gamma-y)^{2}}\right)^{-\frac{1}{2}} |  |

the maps fyf\_{y} are concave, monotonically increasing with a horizontal asymptote for large values of the argument (see Fig. [9](https://arxiv.org/html/2601.01505v1#S3.F9 "Figure 9 ‣ III.3.1 ’Big vs small’ bank: the skew-product case ‣ III.3 Heterogeneous case ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps"))

![Refer to caption](mappefs.png)


Figure 9: Some maps from the family of maps fyf\_{y} with y=70y=70 (Orange), y=80y=80 (Green), y=90y=90 (Red). Here α=1.64,Σϵ=0.00152,γ=100,ω1=0.5\alpha=1.64,\Sigma\_{\epsilon}=0.0015^{2},\gamma=100,\omega\_{1}=0.5. The blue line is the bisector of the first quadrant.

This system is in fact a skew product system

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ1,t+1\displaystyle\lambda\_{1,t+1} | =fλ2,t​(λ1,t)\displaystyle=f\_{\lambda\_{2,t}(\lambda\_{1,t})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ2,t+1\displaystyle\lambda\_{2,t+1} | =T​(λ2,t).\displaystyle=T(\lambda\_{2,t}). |  |

To present some analytical results, it is useful to introduce the invertible extension of TT, T^:I^→I^\hat{T}:\hat{I}\rightarrow\hat{I} where

|  |  |  |
| --- | --- | --- |
|  | I^≐{(λ2,i)i∈ℤ:T​(λ2,i)=λ2,i+1​∀i∈ℤ}\hat{I}\doteq\{(\lambda\_{2,i})\_{i\in\mathbb{Z}}:T(\lambda\_{2,i})=\lambda\_{2,i+1}\forall i\in\mathbb{Z}\} |  |

and

|  |  |  |
| --- | --- | --- |
|  | T^​((λ2,i)i∈ℤ)=(λ2,i+1)i∈ℤ.\hat{T}((\lambda\_{2,i})\_{i\in\mathbb{Z}})=(\lambda\_{2,i+1})\_{i\in\mathbb{Z}}. |  |

Also, for 𝝀∈I^\boldsymbol{\lambda}\in\hat{I}, let’s write f𝝀n=fλ2,n−1∘fλ2,n−2∘⋯∘fλ2,1∘fλ2,0f^{n}\_{\boldsymbol{\lambda}}=f\_{\lambda\_{2,n-1}}\circ f\_{\lambda\_{2,n-2}}\circ\dots\circ f\_{\lambda\_{2,1}}\circ f\_{\lambda\_{2,0}}. (Let us stress once more that the evolution of the forcing bank does not depend on the forced bank and has already been discussed when dealing with the case N=1N=1.)
Let’s now give some analytical results (refer to supplementary material for further details and proofs).
To begin with, no matter the initial conditions, the leverages of the forced bank will always behave asymptotically in the same manner (determined by the initial condition of the large bank, as specified further in Theorem [6](https://arxiv.org/html/2601.01505v1#Thmtheorem6 "Theorem 6 ‣ III.3.1 ’Big vs small’ bank: the skew-product case ‣ III.3 Heterogeneous case ‣ III Coupled Unimodal Maps Model for the Leverage Evolution of Banks Trading a Common Asset ‣ Chaos and Synchronization in Financial Leverages Dynamics: Modeling Systemic Risk with Coupled Unimodal Maps")). This also means that if one has two or more banks with weights πi=0\pi\_{i}=0, their orbits will synchronize under the common forcing of the bigger bank.

###### Theorem 2

(Synchronization on the Fiber)
For any orbit 𝛌∈I^\boldsymbol{\lambda}\in\hat{I} of the forcing bank and for any initial conditions of the forced bank λ1,0,λ1,0′∈[1,∞)\lambda\_{1,0},\,\lambda\_{1,0}^{\prime}\in[1,\infty)

|  |  |  |
| --- | --- | --- |
|  | limn→∞|λ1,n−λ1,n′|=0.\lim\_{n\rightarrow\infty}|\lambda\_{1,n}-\lambda\_{1,n}^{\prime}|=0. |  |

The proof of the theorem above is of topological nature and exploits the “shape" of the functions fyf\_{y}. In addition, one can also show that the Lyapunov Exponent of the forced bank is negative:

###### Theorem 3

(Negative Lyapunov Exponent on the Fiber)
For any 𝛌∈I^\boldsymbol{\lambda}\in\hat{I} and λ1,0∈[1,∞)\lambda\_{1,0}\in[1,\infty)

|  |  |  |
| --- | --- | --- |
|  | Λ1​(λ1,0,𝝀)≐limn→∞1n​log⁡|(f𝝀n)′​(λ1,0)|<0.\Lambda\_{1}(\lambda\_{1,0},\boldsymbol{\lambda})\doteq\lim\_{n\rightarrow\infty}\frac{1}{n}\log{|(f^{n}\_{\boldsymbol{\lambda}})^{\prime}(\lambda\_{1,0})|}<0. |  |

From these results it looks like the dynamics of λ1\lambda\_{1} is determined by something from the “outside”. Not surprisingly, it is the large bank that determines the trajectory on which the leverage of the small bank will synchronize.
Let’s start by looking at what happens when λ2\lambda\_{2} reaches a periodic attractor

###### Theorem 4

(Periodic Forcing)
  
If the dynamics of the forcing bank is periodic, then the dynamics of the forced one will be periodic too (of the same period).

If instead the forcing is chaotic (meaning that it is topologically transitive on a finite union of intervals and that it has a unique a.c.i.p. with respect to Lebsegue), then the forced one shows some irregularity too:

###### Theorem 5

(Chaotic Forcing)
  
If the dynamics of the forcing bank is chaotic, then the dynamics of the forced one is topologically transitive on an open subset of [1,∞)[1,\infty).

We emphasize that the proof of this theorem relies on the fact that the Schwarzian derivative of the map TT is negative, and that this is the unique assumption we have verified only numerically.
These results show how the choices of even a single parameter (e.g. the memory ω2\omega\_{2}) made by a large bank may have an impact on the stability of the whole system. This may be of interest to policymakers, who may for example constrain the values of the memory of the large bank in a “safe” region.

Next, it is possible to provide an explicit characterization of the behavior of the leverage of the small bank as a function of the past orbit of the forcing leverage. In particular, one has:

###### Theorem 6

(Random Fixed Point)
  
Let x​(𝛌)x(\boldsymbol{\lambda}) be the random fixed point for bank 1, i.e. such that fλ2,0​(x​(𝛌))=x​(T^​(𝛌))f\_{\lambda\_{2,0}}(x(\boldsymbol{\lambda}))=x(\hat{T}(\boldsymbol{\lambda})). Then

|  |  |  |
| --- | --- | --- |
|  | x​(𝝀)=1∑i=0∞A​(λ2,−1−i)​ω1ix(\boldsymbol{\lambda})=\frac{1}{\sqrt{\sum\_{i=0}^{\infty}A(\lambda\_{2,-1-i})\omega\_{1}^{i}}} |  |

with A​(λ)≐γ2​α2​Σϵ(1+γ−λ)2A(\lambda)\doteq\frac{\gamma^{2}\alpha^{2}\Sigma\_{\epsilon}}{(1+\gamma-\lambda)^{2}}

Thus, for example, the fixed point depends
continuously on the parameters and the past orbit of the forcing bank (e.g. with respect to the sup norm in the space I^\hat{I}).
In principle, this expression may for example allow the large bank to make the leverage of the small one behave in a specific way, provided it knows ω1\omega\_{1}. This is another evidence of the control the large bank has on the system.
Lastly, it is possible to make some estimates on the frequency of visit of subsets of the domain by the orbit of the forced bank by exploiting the ergodicity on the base (see the supplementary material).

Acknowledgements : The authors thank Fabrizio Lillo, Fulvio Corsi, and Sebastian van Strien for useful conversations. MT acknowledges the support of EPSRC-FAPESP Grant No. 2023/13706 and EPSRC grant number UKRI1021. MT is very grateful to the Scuola Normale Superiore and the Centro di Ricerca Matematica Ennio De Giorgi for their hospitality during several visits in which this work was carried out.