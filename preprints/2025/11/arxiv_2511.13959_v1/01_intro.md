---
authors:
- Jan Maelger
doc_id: arxiv:2511.13959v1
family_id: arxiv:2511.13959
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Opportunity Cost in Insurance
url_abs: http://arxiv.org/abs/2511.13959v1
url_html: https://arxiv.org/html/2511.13959v1
venue: arXiv q-fin
version: 1
year: 2025
---


\fnmDr. Jan \surMaelger
[jan.maelger@t-online.de](mailto:jan.maelger@t-online.de)
[

###### Abstract

We develop a formalism for insurance profit optimisation for the in-force business constraint by regulatory and risk policy related requirements. This approach is applicable to Life, P&C and Reinsurance businesses and applies in all regulatory frameworks with a solvency requirement defined in the form of a solvency ratio, notably Solvency II and the Swiss Solvency Test. We identify the optimal asset allocation for profit maximisation within a pre-defined risk appetite and deduce the annual opportunity cost faced by the insurance company.

###### keywords:

Insurance, Actuarial Business Steering, Opportunity Cost, Solvency, Asset Allocation

## 1 Introduction

The goal of the senior management of any company ought to be to maximize shareholder value, achieved by maximizing long-term profits. Insurance companies are a priori no exception, but they do come with two special features. The first of which is that insurance is a heavily regulated industry, imposing many financial limits and constraints.
The second is the role of the actuary, sitting in the extended management circle, equiped with veto rights and lawfully mandated to ensure sufficient levels of prudency. From a purist actuarial perspective, a too much in prudency buffers does not exist, causing from the outset a conflict of interest with the Finance and Investment departments. Qualitatively, the higher the prudency buffers, the higher the opportunity costs in foregone P&L profits. With quantifications difficult, compromisary discussions are often vague, and a commercially-accessible concept of opportunity cost would prove useful.

As seen from the viewpoint of a single insurance contract, its lifecycle can be split into the writing phase and its run-off phase. Similarly the business view separates the Underwriting from the management of the in-force portfolio, which require separate skills and have separate success factors. While insurance companies need to master both to prevail, it is viable to consider their optimization individually.
On the Underwriting side, profitability is mainly driven by Pricing, on the optimization of which many studies have been performed [Bauer2025, HenrietKlimenko, Harrington2013]. Contrarily, on the management of the in-force business the field is largely unexplored.

There are papers in the literatue on asset allocation optimization under insurance specific constraints, but they differ from our study by not deriving a concept of opportunity cost and in either restricting to only solvency constraints or in optimizing for individual stock selections instead of the entire SAA. For example, in [SchluetterFianuGruendl] the authors study an optimal stock portfolio selection under general solvency constraints and in the context of ESG-investing. In [BraunSchmeiserSchreiber] the insurance asset allocation is optimized across all major asset classes under the constraint of adhering to Solvency II market risk capital requirements.

The approach developed here is interesting for institutional investors, who have the means to run the analysis on a large scale gauging an insurance companies‘ potential foregone growth due to sub-optimally chosen metrics, or the insurance companies themselves, looking to gain further insight into either their own or a competitor‘s strategy.

Following the school of Carl Bender and Steven Orszag [BenderOrszag] to prioritize approximative answers over exact non-answers, we abstain from rigorous definitions and a theorem-proof-style discussion. Instead, we focus on practical applicability and always assume sufficient smoothness. The more notions are kept vague, the more powerful the approach, and so this study is meant as a fall-back blue-print for practicioners of either insurance companies or institutional investors attempting to better understand the business at hand.

In section [2](https://arxiv.org/html/2511.13959v1#S2 "2 Generic Formalism ‣ Opportunity Cost in Insurance") we develop the formalism to compute the opportuntiy cost faced by an insurance company for generic profit functions and a generic set of constraints. In section [3](https://arxiv.org/html/2511.13959v1#S3 "3 Choosing a Profit Function ‣ Opportunity Cost in Insurance") we discuss various choices of profit functions and in section [4](https://arxiv.org/html/2511.13959v1#S4 "4 Constraints ‣ Opportunity Cost in Insurance") we give an overview of the most common constraint types. Section [5](https://arxiv.org/html/2511.13959v1#S5 "5 Time-dependence ‣ Opportunity Cost in Insurance") explains how time-dependence enters the equations and in section [6](https://arxiv.org/html/2511.13959v1#S6 "6 Local Taylor expansion ‣ Opportunity Cost in Insurance") we comment on local approximations. Some concluding remarks are made in section [7](https://arxiv.org/html/2511.13959v1#S7 "7 Conclusion ‣ Opportunity Cost in Insurance").

## 2 Generic Formalism

Let PP denote the profit of an insurance company in a given reporting cycle, typically a year or a quarter, in dependence of some vector of variables x¯\underline{x} and external parameters τ¯\underline{\tau}: P​(x¯,τ¯)P(\underline{x},\underline{\tau}), subject to a set of constraints cc with

|  |  |  |
| --- | --- | --- |
|  | ci​(x¯,τ¯)=0andcj​(x¯,τ¯)≥hj⇔c~j​(x¯,τ¯)≡hj−cj​(x¯,τ¯)≤0c\_{i}(\underline{x},\underline{\tau})=0\quad\text{and}\quad c\_{j}(\underline{x},\underline{\tau})\geq h\_{j}\Leftrightarrow\tilde{c}\_{j}(\underline{x},\underline{\tau})\equiv h\_{j}-c\_{j}(\underline{x},\underline{\tau})\leq 0 |  |

for some indices i,j∈ℕi,j\in\mathbb{N} and thresholds hj∈ℝ+h\_{j}\in\mathbb{R}^{+}. The constraints may be of regulatory nature, eg. on solvency or liquidity, or internally set limits within a risk appetite statement. A more detailed discussion of the constraints can be found in section [4](https://arxiv.org/html/2511.13959v1#S4 "4 Constraints ‣ Opportunity Cost in Insurance"). Denote by nn the total number of constraints.

All quantities immediately controllable by the management of the company constiute the variables x¯\underline{x}, in particular the strategic asset allocation (SAA), and all quantities outside the influence of the management give the set of external parameters τ¯\underline{\tau}, e.g. the yield curve, credit spreads or reserving assumption parameters.
With the x¯\underline{x} being the asset class allocations, they range from 0 to 1, ie x¯∈[0;1]|x|\underline{x}\in[0;1]^{|x|}, and they must sum to 1 for consistency, creating the additional constraint

|  |  |  |
| --- | --- | --- |
|  | ∑kxk−1=0.\sum\_{k}x\_{k}-1=0. |  |

Since we consider the situation of in-force business instead of underwriting new one, the contractual terms of the in-force policies are also seen as external paramters. In particular, we disregard Pricing effects on profit optimisation in this study and refer interested readers to a small selection of the vast literature available [Bauer2025, HenrietKlimenko, Harrington2013]. Similarly we also regard process operations in the Claims department as given constants. While efficiency gains in claims handling obviously reduce costs and increase profits, such undertakings are typically multi-year projects and not immediate levers for the senior management to pull.

Mathematically, the constraint profit optimisation problem can be formulated via Lagrange multipliers [Beavis\_Dobbs\_1990, ProtterIntermediateCalc] under Karush-Kuhn-Tucker (KKT) conditions [Karush2014MinimaOF, Tind2009, Lange2013, walsh1975methods]. We identify the insurance Lagrangian function as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(x¯,τ¯,λ¯)=P​(x¯,τ¯)−∑iλi​ci​(x¯,τ¯)−∑jλ~j​c~j​(x¯,τ¯)−μ​(∑kxk−1),\mathcal{L}(\underline{x},\underline{\tau},\underline{\lambda})=P(\underline{x},\underline{\tau})-\sum\_{i}\lambda\_{i}\,c\_{i}(\underline{x},\underline{\tau})-\sum\_{j}\tilde{\lambda}\_{j}\,\tilde{c}\_{j}(\underline{x},\underline{\tau})-\mu\big(\sum\_{k}x\_{k}-1\big), |  | (1) |

for some multipliers λi,λ~j,μ∈ℝ\lambda\_{i},\tilde{\lambda}\_{j},\mu\in\mathbb{R} and
λ¯=(λiλ~jμ)\underline{\lambda}=\begin{pmatrix}\lambda\_{i}\\
\tilde{\lambda}\_{j}\\
\mu\end{pmatrix}.
By the KKT theorem, any saddle point111Maximum over x¯\underline{x}, but could be a maximum or minimum over λ¯\underline{\lambda}. of the Lagrangian over x¯⊕λ¯\underline{x}\oplus\underline{\lambda} is also an optimal solution over x¯\underline{x} to the profit function subjet to the above constraints [walsh1975methods, Kalman01062009, Fuente\_2000].
Reformulated as a KKT problem, we have the following necessary conditions for an optimal solution [Ruszczynski]:

* •

  Stationarity condition:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∇xP​(x¯,τ¯)−∑iλi​∇xci​(x¯,τ¯)−∑jλ~j​∇xc~j​(x¯,τ¯)−μ=0¯\displaystyle\nabla\_{x}P(\underline{x},\underline{\tau})-\sum\_{i}\lambda\_{i}\,\nabla\_{x}c\_{i}(\underline{x},\underline{\tau})-\sum\_{j}\tilde{\lambda}\_{j}\,\nabla\_{x}\tilde{c}\_{j}(\underline{x},\underline{\tau})-\mu=\underline{0} |  | (2) |
* •

  Primal feasability conditions (original constraints):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑kxk−1=0andci​(x¯,τ¯)=0andc~j​(x¯,τ¯)≤0∀i,j\displaystyle\sum\_{k}x\_{k}-1=0\quad\text{and}\quad c\_{i}(\underline{x},\underline{\tau})=0\quad\text{and}\quad\tilde{c}\_{j}(\underline{x},\underline{\tau})\leq 0\quad\forall i,j |  | (3) |
* •

  Dual feasability condition:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | λ~j≥0∀j\tilde{\lambda}\_{j}\geq 0\quad\forall j |  | (4) |
* •

  Complementary Slackness condition:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑jλ~j​c~j​(x¯,τ¯)=0\displaystyle\sum\_{j}\tilde{\lambda}\_{j}\,\tilde{c}\_{j}(\underline{x},\underline{\tau})=0 |  | (5) |

The notation ∇x\nabla\_{x} stands for a vector of partial derivatives over all elements of the vector x¯\underline{x}.
The sufficient conditions for an optimal solution can be expressed via the determinant of the Hessian matrix [Boyd\_Vandenberghe\_2004, silberberg2001structure] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | det∇x​x2ℒ​(x¯,τ¯,λ¯)<0.\det\nabla^{2}\_{xx}\mathcal{L}(\underline{x},\underline{\tau},\underline{\lambda})<0. |  | (6) |

To give some intuition, the potential candidates (ie stationary points) for a global maximum of the Lagrangian in Eq.([1](https://arxiv.org/html/2511.13959v1#S2.E1 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) are found by the solutions of Eqs.([2](https://arxiv.org/html/2511.13959v1#S2.E2 "In 1st item ‣ 2 Generic Formalism ‣ Opportunity Cost in Insurance"))-([5](https://arxiv.org/html/2511.13959v1#S2.E5 "In 4th item ‣ 2 Generic Formalism ‣ Opportunity Cost in Insurance")). These stationary points could correspond to either local maxima, minima or saddle points over x¯\underline{x}. Eq.([6](https://arxiv.org/html/2511.13959v1#S2.E6 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) then sorts out the local maxima from the pool of candidate solutions. To identify the global maximum x¯∗\underline{x}\_{\ast}, one has to manually compare all local maxima such that ℒ​(x¯∗)≥ℒ​(x¯m)\mathcal{L}(\underline{x}\_{\ast})\geq\mathcal{L}(\underline{x}\_{m}) for all x¯m\underline{x}\_{m} satisfying Eqs.([2](https://arxiv.org/html/2511.13959v1#S2.E2 "In 1st item ‣ 2 Generic Formalism ‣ Opportunity Cost in Insurance")) to ([6](https://arxiv.org/html/2511.13959v1#S2.E6 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")). In case there are no candidate solutions x¯m\underline{x}\_{m}, then the global maximum x¯∗\underline{x}\_{\ast} sits on the boundary of the variable space [0;1]|x|[0;1]^{|x|}.

The difference bewtween the profits generated from the optimal target SAA values and the actuals is the opportunity cost faced by the insurance company:

|  |  |  |  |
| --- | --- | --- | --- |
|  | O​p​C​(x¯,τ¯)≡P​(x¯∗,τ¯)−P​(x¯,τ¯).OpC(\underline{x},\underline{\tau})\equiv P(\underline{x}\_{\ast},\underline{\tau})-P(\underline{x},\underline{\tau}). |  | (7) |

It is remarked that the optimization problem in Eqs ([2](https://arxiv.org/html/2511.13959v1#S2.E2 "In 1st item ‣ 2 Generic Formalism ‣ Opportunity Cost in Insurance")) to ([6](https://arxiv.org/html/2511.13959v1#S2.E6 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) is always well-defined for any chosen number of constraints ncn\_{c} and nc~n\_{\tilde{c}} and for any chosen granularity222For example SAA={Cash, RE, Equities, Alternatives, Govies, Coprorate  bonds}\text{SAA}=\big\{\text{Cash, RE, Equities, Alternatives, Govies, Coprorate\, bonds}\big\}. of the SAA, with the number of classes denoted by nxn\_{x}. The number of equations and the number of unknowns are both nc+nc~+nxn\_{c}+n\_{\tilde{c}}+n\_{x}.

In general, it is not possible to solve the set of Eqs. ([2](https://arxiv.org/html/2511.13959v1#S2.E2 "In 1st item ‣ 2 Generic Formalism ‣ Opportunity Cost in Insurance")) to ([6](https://arxiv.org/html/2511.13959v1#S2.E6 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) analytically and one resorts to numerical methods. A vast array of techniques are available in the literature, and the reader is referred to [Boyd\_Vandenberghe\_2004] for an introduction to nonlinear optimization and to [MOHAMMADI2023106959, NeculaiAndrei] for a review of the more recent developments. Finally, the advent of commercially viable quantum computing may bring further capabilities to real-time financial optimization [Abbasetal, WilkensMoorhouse].

## 3 Choosing a Profit Function

Insurance profits can be split in many ways, and accounting nomenclature can become highly involved. However, at lowest granularity, one way to determine profits is via the value of the new business written (N​B​VNBV), the change in existing assets on the balance sheet from one period to the next, i.e. the investment returns (I​n​v​RInvR), both realized and unrealized, and the change in liabilities during the same time period (Δ​l​i​a​b\Delta liab):

|  |  |  |  |
| --- | --- | --- | --- |
|  | P=NBV+InvR−Δ​liab.P=\textit{NBV}+\textit{InvR}-\Delta\textit{liab}. |  | (8) |

In itself, each of these components is a complex function of many stochastic drivers. Eg. the InvR depend heavily on the SAA and the market developments. Similarly the movements of the liabilities depends on the market developments and the change in technical reserving assumptions and parameters. Additionally, via measures such as Asset Liability Management (ALM), the adverse changes in liabilities can be mitigated by mirroring changes in assets, adding a further layer of complexity onto the business.

We disregard N​B​VNBV at this point, since it is primarily determined by Pricing and thus out of scope for this study. The change in liabilities is itself composed of several parts, most of which are outside the sphere of influence of the senior management, eg the change in reserving assumptions, with an exception of operational or one-off reserve releases. However, the former is simply balancing items and the latter can be seen as deferred profits from the past. The term Δ​liab\Delta\textit{liab} also contains a contribution from the difference in actual claims incurred vs the reserved forecast from the previous reporting date. This is largely due to the random claims experience during the reporting period. However a small part is influencable by the senior management via efficient internal processes and good preventive communication to the customers, eg early hail warnings to motor customers. Nonetheless, in the spirit of this paper, these effects are attributed in its entirety to the external parameters τ¯\underline{\tau}.

For the investment returns, they can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | InvR=∑k|x|Rk​xk\textit{InvR}=\sum\_{k}^{|x|}R\_{k}x\_{k} |  | (9) |

with RkR\_{k} a random variable for the investment returns of asset class xkx\_{k} over a given time period, which can be expressed as Rk=𝔼​[Rk]+vkR\_{k}=\mathbb{E}[R\_{k}]+v\_{k} with the volatility vkv\_{k} a stochastic noise around 0. At first order, one may set vk=0v\_{k}=0, when considering long-term over short-term profits. Since the market returns are outside the influence of the management, the RkR\_{k} are part of the set of external parameters, Rk∈τ¯R\_{k}\in\underline{\tau}.

Looking at profit functions in more detail, there is a whole plethora of metrics available, for instance

* •

  Business Operating Profit (BOP)
* •

  Net income before interest and tax (NIBIT)
* •

  Net income after tax (NIAT)
* •

  Return on Equity (ROE)
* •

  Return on Capital (ROC)
* •

  Risk-adjusted return on capital (RAROC)
* •

  Return on risk-adjusted capital (RORAC)
* •

  Risk-adjusted return on risk-adjusted capital (RARORAC)

These profit metrics can be applied to balance sheets under different accounting standards, either statutory (eg. US GAAP, Swiss GAAP etc.) or market consistent (eg. IFRS, Swiss GAAP FER, SII etc.)

All of these choices hold merit in their own right and will ultimately lead to different opportunity costs. For example, choosing to consider BOP on an IFRS balance sheet yields a respective opportunity cost
O​p​CIFRS BOPOpC\_{\text{IFRS BOP}}.

## 4 Constraints

Insurance is a heavily regulated industry and the list of constraints imposed by the regulator is long. Many of the regulatory constraints are superimposed by internally set confidence (amber/red) limits, specified in risk appetite statements, to ensure sufficient early warning indicators before any regulatory breaches.
We list below some of the most common limit types, without any claim to even near exhaustion.

1. 1.

   Cash requirement:

   |  |  |  |
   | --- | --- | --- |
   |  | xCash≥lCash,x\_{\text{Cash}}\geq l\_{\text{Cash}}, |  |

   with xcashx\_{\text{cash}} the SAA component for cash and cash equivalents, and lCashl\_{\text{Cash}} the short-term cash limit.
2. 2.

   Liquidity strain requirement:

   |  |  |  |
   | --- | --- | --- |
   |  | ∑j∈liquidxj​hj≥lliquid\sum\_{j\in\text{liquid}}x\_{j}h\_{j}\geq l\_{\text{liquid}} |  |

   The quantity lliquidl\_{\text{liquid}} is the long-term lower liquidity threshold, and the {hj|j∈liquid}\big\{h\_{j}|j\in{\text{liquid}}\big\} are haircuts on the market values of asset classes {xj|j∈liquid}⊂x¯\big\{x\_{j}|j\in\text{liquid}\big\}\subset\underline{x}, inserted to account for potential losses realized during the sale of liquid assets in stress situations.
3. 3.

   Solvency requirement:

   |  |  |  |
   | --- | --- | --- |
   |  | S​R​(x¯)≡A​F​R​(x¯)/S​C​R​(x¯)≥TSR(\underline{x})\equiv AFR(\underline{x})\big/SCR(\underline{x})\geq T |  |

   The solvency constraint is in the usual form of a solvency ratio (S​RSR) with A​F​RAFR are the available financial ressources, S​C​RSCR the solvency acapital requirement333The A​F​RAFR is called Basic Own Funds (B​O​FBOF) under SII and Risk Bearing Capital (R​B​CRBC) under SST. The SII wording of SCR corresponds to the Target Capital (T​CTC) under SST. Conceptually, for our purposes, these terms are interchangeable. and the parameter TT either the minimum regulatory threshold or an internally set target solvency ratio.

Further typical constraints include thresholds for the following quantities.

1. 4.

   Shareholder Equity
2. 5.

   Tied Assets
3. 6.

   FX Exposure
4. 7.

   Counterparty Exposure
5. 8.

   ALM or Hedging requirements
6. 9.

   Usage of derivative instruments
7. 10.

   Cash pooling limits

While asset class exposure limits may already be in place in the company, such as xEquities≤lEquitiesx\_{\text{Equities}}\leq l\_{\text{Equities}} or xRE≤lREx\_{\text{RE}}\leq l\_{\text{RE}} etc, one should be careful in modelling them as constraints in Eq.([1](https://arxiv.org/html/2511.13959v1#S2.E1 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")), since they artificially restrict the optimizable variable space. If these asset class limits are rooted in regulatory requirements, they must of course be adhered to. Contrarily, if they merely stem from the current SAA, then this is in fact the setup to be challenged by Eqs.([2](https://arxiv.org/html/2511.13959v1#S2.E2 "In 1st item ‣ 2 Generic Formalism ‣ Opportunity Cost in Insurance"))-([6](https://arxiv.org/html/2511.13959v1#S2.E6 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) and their inclusion as constraints leads to a misinterpretation of the true maximum x∗x\_{\ast}.

## 5 Time-dependence

Investigating the time-dependence of Eq.([1](https://arxiv.org/html/2511.13959v1#S2.E1 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")), the only quantities which change with time are the external parameters, τ¯​(t)\underline{\tau}(t). There is no explicit time-dependence of the profit function PP or the variables x¯\underline{x}, such that ∂P∂t=0\frac{\partial P}{\partial t}=0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Pd​t=∑k=1|τ|∂P∂τk​d​τkd​t.\frac{\text{d}P}{\text{d}t}=\sum\_{k=1}^{|\tau|}\frac{\partial P}{\partial\tau\_{k}}\frac{\text{d}\tau\_{k}}{\text{d}t}. |  | (10) |

Similarly for the constraints ci​(x¯,τ¯)c\_{i}(\underline{x},\underline{\tau}) and c~j​(x¯,τ¯)\tilde{c}\_{j}(\underline{x},\underline{\tau}).
In a strict sense, the time-dependence turns Eqs.([1](https://arxiv.org/html/2511.13959v1#S2.E1 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) to ([6](https://arxiv.org/html/2511.13959v1#S2.E6 "In 2 Generic Formalism ‣ Opportunity Cost in Insurance")) into a real-life optimisation problem to be solved. However, while market data indeed changes in real-time, most of the external paramters, ie reserving assumptions or yield curves, are more stable, rendering quarterly updates sufficient in most scenarios.

## 6 Local Taylor expansion

By standard Taylor expansion, around any point x¯0\underline{x}\_{0}, the |x||x|-dimensional hypersurface ℒ​(x¯)\mathcal{L}(\underline{x}) can be approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(x¯,τ¯)=ℒ​(x¯0,τ¯)+∑k=1∞∇xkℒ​(x¯0,τ¯)⋅(x¯−x¯0)k,\mathcal{L}(\underline{x},\underline{\tau})=\mathcal{L}(\underline{x}\_{0},\underline{\tau})+\sum\_{k=1}^{\infty}\nabla\_{x}^{k}\mathcal{L}(\underline{x}\_{0},\underline{\tau})\cdot(\underline{x}-\underline{x}\_{0})^{k}, |  | (11) |

which is valid for any x¯\underline{x} in sufficient proximity of x¯0\underline{x}\_{0}.
With a closed form not known for ℒ\mathcal{L}, decision making processes between a handful of alternatives typically assess their impacts on the profits PP, accompanied by impact estimates on other KPIs. Implicitly, such impact assessments correspond to a subset of the linear terms ∇xℒ​(x¯0,τ¯)\nabla\_{x}\mathcal{L}(\underline{x}\_{0},\underline{\tau}). In rare cases, second order effects are accounted for to enhance decision quality.
While this approach is practical, it only gives direction for a small set of possible choices, without clear identification of true maxima.
At any point x¯0\underline{x}\_{0}, the best choice is the one that follows the gradient of the surface, ∇xℒ​(x¯0,τ¯)\nabla\_{x}\mathcal{L}(\underline{x}\_{0},\underline{\tau}).

## 7 Conclusion

We have set up a universal formalism for any insurance company to tune its strategic asset allocation for profit maximization, or at least to better understand the opportunity costs associated with differing strategies. The equations in this conceptual first study remain at high-level, but can be tailored to fit specific business needs and with some ressource investment can be turned into regular reporting outputs.

While the formalism developed allows to identify the optimal strategic asset allocation for maximum profits within any set of constraining limit thresholds, it does not make any claim how to best set the limits themselves. This remains for a future study.

\bmhead

Acknowledgements

The author would like to thank James Richardson for mentorship and practical insights into the steering of an insurance company as seen from an actuarial background. This publication did not receive any financial support.