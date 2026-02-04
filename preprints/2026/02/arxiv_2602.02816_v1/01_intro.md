---
authors:
- Crisent Birungi
- Cody Hyndman
doc_id: arxiv:2602.02816v1
family_id: arxiv:2602.02816
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization
url_abs: http://arxiv.org/abs/2602.02816v1
url_html: https://arxiv.org/html/2602.02816v1
venue: arXiv q-fin
version: 1
year: 2026
---


Criscent Birungi
Department of Mathematics and Statistics
  
Concordia University
  
Montréal, QC, Canada

Cody Hyndman
Corresponding author. Emails:
[criscent.birungi@concordia.ca](mailto:criscent.birungi@concordia.ca),
[cody.hyndman@concordia.ca](mailto:cody.hyndman@concordia.ca)
Department of Mathematics and Statistics
  
Concordia University
  
Montréal, QC, Canada

(February 1, 2026)

###### Abstract

The decision to annuitize wealth in retirement planning has become increasingly complex due to rising longevity risk and changing retirement patterns, including increased labor force participation at older ages. While an extensive literature studies consumption, labor, and annuitization decisions, these elements are typically examined in isolation. This paper develops a unified stochastic control and optimal stopping framework in which habit formation and endogenous labor supply shape retirement and annuitization decisions under age-dependent mortality. We derive optimal consumption, labor, portfolio, and annuitization policies in a continuous-time lifecycle model. The solution is characterized via dynamic programming and a Hamilton–Jacobi–Bellman variational inequality. Our results reveal a rich sequence of retirement dynamics. When wealth is low relative to habit, labor is supplied defensively to protect consumption standards. As wealth increases, agents enter a work-to-retire phase in which labor is supplied at its maximum level to accelerate access to retirement. Human capital acts as a stabilizing asset, justifying a more aggressive pre-retirement investment portfolio, followed by abrupt de-risking upon annuitization. Subjective mortality beliefs are a key determinant in shaping retirement dynamics. Agents with pessimistic longevity beliefs rationally perceive annuities as unattractive, leading them to avoid or delay annuitization. This framework provides a behavior-based explanation for low annuity demand and offers guidance for retirement planning jointly linking labor supply, portfolio choice, and the timing of annuitization.

Keywords: Optimal annuitization; Habit formation; Labor supply; Lifecycle portfolio choice; Stochastic control; Optimal stopping; Dynamic programming; Gompertz law

Mathematics Subject Classification (2020): Primary 91G10; Secondary 93E20, 49L20

## 1 Introduction

An annuity is a contract that provides a buyer with a guaranteed, regular income. This conversion of an investment into a steady stream of payments is known as annuitization. As Buttarazzi et al. ([2025](https://arxiv.org/html/2602.02816v1#bib.bib6)) notes, this is a major retirement decision where individuals trade the potential for investment growth for the long-term financial stability of a guaranteed income for life. This decision is increasingly complex due to rising longevity risk, a demographic shift evidenced by growing labor force participation among older age groups as noted by Gao et al. ([2022](https://arxiv.org/html/2602.02816v1#bib.bib13)). For instance, the Bureau of Labor Statistics projects that by 2033, the labor participation rate will exceed 10%10\% for those aged 75 and older and surpass 30%30\% for those aged 65. The presence of flexible labor income, which can be used to bridge employment gaps or supplement retirement welfare (see Mutik, [2021](https://arxiv.org/html/2602.02816v1#bib.bib25); Lorenz and Zwick, [2021](https://arxiv.org/html/2602.02816v1#bib.bib22)), transforms conventional retirement planning.

The primary challenge is to determine how an agent can maximize lifetime utility from consumption and leisure, given deterministic age-dependent force of mortality, while managing wealth optimally. Formally, the problem is a coupled continuous-time stochastic control and optimal stopping problem, in which consumption, labor supply, portfolio choice, and the timing of irreversible annuitization are jointly determined. This study addresses this optimization problem within the framework of stochastic optimal control. The agent’s wealth, supplemented by wage income, is governed by a stochastic differential equation (SDE) influenced by their strategic choices in investment (πt\pi\_{t}), consumption (ctc\_{t}), and labor (btb\_{t}). The option to irrevocably annuitize wealth introduces an optimal stopping component that is jointly determined with consumption, labor, and portfolio decisions.

We employ the dynamic programming approach, specifically formulating the problem as a Hamilton-Jacobi-Bellman Variational Inequality (HJBVI), as the agent must simultaneously solve for the optimal policies and the optimal time to stop (i.e., to annuitize). This HJB approach, developed in the seminal works of Merton ([1969](https://arxiv.org/html/2602.02816v1#bib.bib23), [1971](https://arxiv.org/html/2602.02816v1#bib.bib24)) and extended to stopping problems by Karatzas and Shreve ([1998](https://arxiv.org/html/2602.02816v1#bib.bib16)), provides a natural framework for jointly characterizing optimal policies and annuitization timing. It complements alternative frameworks such as the duality and martingale methods, which have been foundational to modern portfolio and consumption/investment theory (Rockafellar and Wets, [1998](https://arxiv.org/html/2602.02816v1#bib.bib27); Karatzas and Wang, [2000](https://arxiv.org/html/2602.02816v1#bib.bib17); Gao et al., [2022](https://arxiv.org/html/2602.02816v1#bib.bib13)).

Our work builds on two rich streams of literature. The first explores optimal consumption, leisure, and investment choices (see Cvitanić and Karatzas, [1992](https://arxiv.org/html/2602.02816v1#bib.bib10); Labbé and Heunis, [2007](https://arxiv.org/html/2602.02816v1#bib.bib19); Choi et al., [2008](https://arxiv.org/html/2602.02816v1#bib.bib8); Barucci and Marazzina, [2012](https://arxiv.org/html/2602.02816v1#bib.bib3); Koo et al., [2013](https://arxiv.org/html/2602.02816v1#bib.bib18); Lee and Shin, [2015](https://arxiv.org/html/2602.02816v1#bib.bib20); Peng and Li, [2023](https://arxiv.org/html/2602.02816v1#bib.bib26)). A significant portion of this literature, including Gerrard et al. ([2012](https://arxiv.org/html/2602.02816v1#bib.bib14)) and Gao et al. ([2022](https://arxiv.org/html/2602.02816v1#bib.bib13)), simplifies the problem by assuming a constant mortality rate. This assumption, while tractable, abstracts from the strongly age-dependent nature of mortality risk. A second, parallel stream of literature incorporates the psychological realism of habit formation, where utility is derived not from the level of consumption, but from its level relative to an accustomed habit (Sundaresan, [1989](https://arxiv.org/html/2602.02816v1#bib.bib28); Constantinides, [1990](https://arxiv.org/html/2602.02816v1#bib.bib9); Detemple and Zapatero, [1991](https://arxiv.org/html/2602.02816v1#bib.bib11); Dybvig, [1995](https://arxiv.org/html/2602.02816v1#bib.bib12)). This feature introduces a powerful consumption-smoothing motive and a "defensive" demand for assets. However, these models often do not include the complexities of flexible labor supply or the optimal annuitization decision.

This paper bridges these gaps by characterizing a unified stochastic control and optimal stopping framework in which habit formation and endogenous labor supply generate state-dependent retirement and annuitization regimes. We derive the HJBVI for this problem and, by employing a dimensionality reduction technique, derive semi-analytical solutions for the value function and the corresponding optimal policies for consumption, labor supply, and investment. We then provide analysis with rigorous characterization of the interplay between consumption habits, mortality risk, labor-leisure trade-offs, and investment behavior under the option to annuitize.

The rest of this paper is structured as follows. Section [2](https://arxiv.org/html/2602.02816v1#S2 "2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") discusses the market model, including the economic background and mathematical formulations. Section [3](https://arxiv.org/html/2602.02816v1#S3 "3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") discusses the HJBVI and the proposed methods for determining optimality and provides rigorous proofs and characterizes semi-analytical solutions for the value function and the optimal policies. Section [4](https://arxiv.org/html/2602.02816v1#S4 "4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") presents numerical implementation results and key findings. Finally, Section [5](https://arxiv.org/html/2602.02816v1#S5 "5 Conclusion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") presents conclusions and recommendations for future research.

## 2 Economic background

This section presents the financial market, the key processes governing the agent’s decisions, and the formulation of the optimization problem.

### 2.1 The Financial Market

We consider a financial market on a filtered probability space (Ω,ℱ,{ℱt}t≥0,P)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\geq 0},P) satisfying the usual conditions and supporting a one-dimensional standard Brownian motion {Wt}t≥0\{W\_{t}\}\_{t\geq 0}. The market contains two continuously traded assets: a risk-free money market account, S0S^{0}, and a risky stock, S1S^{1}. Their prices evolve as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St0\displaystyle dS\_{t}^{0} | =r​St0​d​t,S00=1,\displaystyle=rS\_{t}^{0}\,dt,\qquad S\_{0}^{0}=1, |  | (2.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St1\displaystyle dS\_{t}^{1} | =μ​St1​d​t+σ​St1​d​Wt,S01>0,\displaystyle=\mu S\_{t}^{1}\,dt+\sigma S\_{t}^{1}\,dW\_{t},\qquad S\_{0}^{1}>0, |  | (2.2) |

where r>0r>0 is the constant risk-free rate, and μ∈ℝ\mu\in\mathbb{R} and σ>0\sigma>0 are the constant expected return and volatility of the risky asset, respectively. Let ϕt0\phi\_{t}^{0} and ϕt1\phi\_{t}^{1} denote the number of units held at time tt of the risk-free and risky assets, respectively. The total wealth is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=ϕt0​St0+ϕt1​St1.X\_{t}=\phi\_{t}^{0}S\_{t}^{0}+\phi\_{t}^{1}S\_{t}^{1}. |  | (2.3) |

In this framework, the agent makes decisions on consumption ct≥0c\_{t}\geq 0, investment, and labor supply bt≥0b\_{t}\geq 0. The labor supply generates income at a constant wage rate w>0w>0. We assume the agent holds a *self-financing* portfolio.
The self-financing condition is modified to include both consumption withdrawals and labor income infusions as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=ϕt0​d​St0+ϕt1​d​St1−ct​d​t+w​bt​Zt​d​tdX\_{t}=\phi\_{t}^{0}\,dS\_{t}^{0}+\phi\_{t}^{1}\,dS\_{t}^{1}-c\_{t}\,dt+wb\_{t}Z\_{t}\,dt |  | (2.4) |

where ZtZ\_{t} is the consumption habit. The condition in ([2.4](https://arxiv.org/html/2602.02816v1#S2.E4 "Equation 2.4 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) implies that changes in wealth arise only from capital gains, consumption, and labor income, with no other external infusion or withdrawal of funds. To derive the wealth dynamics, we define the *dollar amount* invested in the risky asset as πt:=ϕt1​St1\pi\_{t}:=\phi\_{t}^{1}S\_{t}^{1}. From the definition of total wealth ([2.3](https://arxiv.org/html/2602.02816v1#S2.E3 "Equation 2.3 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), the amount in the risk-free asset is ϕt0​St0=Xt−πt\phi\_{t}^{0}S\_{t}^{0}=X\_{t}-\pi\_{t}. Substituting the asset dynamics and these portfolio definitions into the self-financing condition ([2.4](https://arxiv.org/html/2602.02816v1#S2.E4 "Equation 2.4 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=[r​Xt+πt​(μ−r)−ct+w​bt​Zt]​d​t+σ​πt​d​Wt.dX\_{t}=\left[rX\_{t}+\pi\_{t}(\mu-r)-c\_{t}+wb\_{t}Z\_{t}\right]dt+\sigma\pi\_{t}\,dW\_{t}. |  | (2.5) |

For the remainder of the paper, we define the market price of risk as θ:=(μ−r)/σ\theta:=(\mu-r)/\sigma. Equation ([2.5](https://arxiv.org/html/2602.02816v1#S2.E5 "Equation 2.5 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) describes the evolution of the agent’s wealth over time, incorporating investment decisions (πt)(\pi\_{t}), consumption plans (ct)(c\_{t}), and labor income (w​bt​Zt)(wb\_{t}Z\_{t}).

### 2.2 Problem Formulation

We begin by establishing the foundational assumptions for the optimization problem.

###### Assumption 2.1.

We assume the following initial conditions and market structure

1. 1.

   Market Parameters: The financial market is complete and free of arbitrage. The parameters r,μ,σ,wr,\mu,\sigma,w are all positive constants.
2. 2.

   Initial Conditions: The retiree starts with an initial wealth X0=x>0X\_{0}=x>0 and an initial habit level Z0=z>0Z\_{0}=z>0.

#### 2.2.1 State Processes: Wealth and Habit

The agent’s financial journey is captured by two state variables: their wealth (XtX\_{t}) and their consumption habit (ZtZ\_{t}). The evolution of the agent’s wealth over time is governed by the SDE presented in ([2.5](https://arxiv.org/html/2602.02816v1#S2.E5 "Equation 2.5 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). The consumption habit, ZtZ\_{t}, models how the agent’s past spending influences their current consumption desires. Following the framework in Angoshtari et al. ([2023](https://arxiv.org/html/2602.02816v1#bib.bib1)), the dynamics of this habit formation process are described by the ordinary differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zt=ρ~​(ct−Zt)​d​t,dZ\_{t}=\tilde{\rho}(c\_{t}-Z\_{t})dt, |  | (2.6) |

where ctc\_{t} represents the agent’s consumption rate, while the parameter ρ~>0\tilde{\rho}>0 determines how quickly their habit adapts to changes in their spending. A central feature of this model is a floor on consumption, which prevents the agent from drastically reducing their spending. This constraint ensures that their consumption rate, ctc\_{t}, must always be greater than or equal to a specified proportion, α\alpha, of their habit level, ZtZ\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​Zt≤ct,for a constant ​α∈(0,1].\alpha Z\_{t}\leq c\_{t},\quad\text{for a constant }\alpha\in(0,1]. |  | (2.7) |

Here, the parameter α\alpha quantifies the addictiveness of the habit. As α\alpha approaches 1, the habit is considered completely addictive, compelling the agent to consume at a rate very close to their established habit. Conversely, a value of α\alpha near 0 corresponds to a non-addictive habit, granting the agent greater flexibility in their consumption choices.

###### Assumption 2.2 (Financial Viability).

The model parameters must satisfy the inequality r>ρ~​(1−α)r>\tilde{\rho}(1-\alpha). This assumption is necessary to guarantee that the minimum required consumption plan for the agent, where ct=α​Ztc\_{t}=\alpha Z\_{t} for all tt, is affordable.

#### 2.2.2 Deterministic force of mortality

Let nn denote the agent’s current age, and let TnT\_{n} represent the agent’s uncertain remaining lifetime. In Gao et al. ([2022](https://arxiv.org/html/2602.02816v1#bib.bib13)) and Gerrard et al. ([2012](https://arxiv.org/html/2602.02816v1#bib.bib14)), it is assumed that TnT\_{n} follows a distribution with a constant force of mortality δ>0\delta>0. Under this assumption, the probability of surviving tt years is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Tn>t)=exp⁡(−δ​t).P(T\_{n}>t)=\exp\left(-\delta t\right). |  | (2.8) |

However, a more realistic model would incorporate an age-dependent force of mortality, particularly one that increases with age. Following the argument in Ashraf ([2023](https://arxiv.org/html/2602.02816v1#bib.bib2)), we introduce an age-dependent force of mortality and assume the deterministic Gompertz mortality law. This law assumes the rate of change in the force of mortality, δt\delta\_{t}, is proportional to its current level, leading to exponential growth over time. Mathematically, δt\delta\_{t} follows the ordinary differential equation (ODE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​δt=θ~​δt​d​t.\mathrm{d}\delta\_{t}=\tilde{\theta}\delta\_{t}\,\mathrm{d}t. |  | (2.9) |

The solution to the ODE in ([2.9](https://arxiv.org/html/2602.02816v1#S2.E9 "Equation 2.9 ‣ 2.2.2 Deterministic force of mortality ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) yields the time-dependent force of mortality: δt=δ0​eθ~​t\delta\_{t}=\delta\_{0}e^{\tilde{\theta}t}. This functional form is consistent with the usual actuarial representation at age ntn\_{t} and time tt

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt=1λ​exp⁡(nt−mλ),\delta\_{t}=\frac{1}{\lambda}\exp\left(\frac{n\_{t}-m}{\lambda}\right), |  | (2.10) |

where ntn\_{t} is the age at time tt, mm is the modal value of life (in years), and λ\lambda is the dispersion parameter (in years). The term θ~\tilde{\theta} is referred to as the Gompertz aging rate and coincides with the inverse of the dispersion parameter (i.e., θ~=1/λ\tilde{\theta}=1/\lambda). In this age-dependent case, the deterministic probability of surviving tt years is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | \@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p=P​(Tn>t)=exp⁡(−∫0tδy​𝑑y),\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p=P(T\_{n}>t)=\exp\left(-\int\_{0}^{t}\delta\_{y}\,dy\right), |  | (2.11) |

where δy\delta\_{y} represents the force of mortality at time yy (age n+yn+y). The deterministic age-dependent force of mortality is independent of the fund’s level of evolution, simplifying the subsequent analysis.

The survival probability from time tt to ss (where s>ts>t) for an individual currently aged nn, denoted p​(t;s;δt)=P​(Tn>s−t​∣Tn>​t)p(t;s;\delta\_{t})=P(T\_{n}>s-t\mid T\_{n}>t), exhibits a key simplifying property under a deterministic force of mortality

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(t;s;δt)\displaystyle p(t;s;\delta\_{t}) | =exp⁡(−∫tsδy​𝑑y)=exp⁡(−∫0sδy​𝑑y)exp⁡(−∫0tδy​𝑑y)=p​(s;δ0)p​(t;δ0).\displaystyle=\exp\!\left(-\int\_{t}^{s}\delta\_{y}\,dy\right)=\frac{\exp\!\left(-\int\_{0}^{s}\delta\_{y}\,dy\right)}{\exp\!\left(-\int\_{0}^{t}\delta\_{y}\,dy\right)}=\frac{p(s;\delta\_{0})}{p(t;\delta\_{0})}. |  | (2.12) |

The identity in equation ([2.12](https://arxiv.org/html/2602.02816v1#S2.E12 "Equation 2.12 ‣ 2.2.2 Deterministic force of mortality ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) generally fails once the mortality intensity becomes stochastic. Nonetheless, since calibration is typically carried out at time 0, that is, only to p​(t;δ0)p(t;\delta\_{0}), this discrepancy does not pose practical difficulties.

#### 2.2.3 Admissible Strategies and the Optimization Problem

To ensure the optimization problem is well-posed, we must formally define the set of admissible control strategies. The agent selects a portfolio process (πt\pi\_{t}), a consumption rate (ctc\_{t}), and a labor supply rate (btb\_{t}), which are all assumed to be ℱt\mathcal{F}\_{t}-progressively measurable processes. Following the framework in Lee and Shin ([2015](https://arxiv.org/html/2602.02816v1#bib.bib20)), we define the sets of allowable control processes.

The set of admissible portfolio strategies Π\Pi is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π:={π:[0,∞)×Ω→ℝ|π is ℱt-prog. measurable and ∫0T∥πt∥2dt<∞, a.s. ∀T>0}.\Pi:=\left\{\pi:[0,\infty)\times\Omega\to\mathbb{R}\,\middle|\,\pi\text{ is }\mathcal{F}\_{t}\text{-prog. measurable and }\int\_{0}^{T}\|\pi\_{t}\|^{2}\,dt<\infty,\text{ a.s. }\forall T>0\right\}. |  | (2.13) |

The set of admissible consumption processes 𝒞\mathcal{C} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞:={c:[0,∞)×Ω→ℝ|c is ℱt-prog. measurable and ∫0Tctdt<∞ a.s. ∀T>0}.\mathcal{C}:=\left\{c:[0,\infty)\times\Omega\to\mathbb{R}\;\middle|\;c\text{ is }\mathcal{F}\_{t}\text{-prog. measurable and }\int\_{0}^{T}c\_{t}\,dt<\infty\text{ a.s. }\forall T>0\right\}. |  | (2.14) |

The set of admissible labor supply processes ℬ\mathcal{B} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ:={b:[0,∞)×Ω→[0,b¯]|b is ℱt-prog. measurable and ∫0Tbtdt<∞ a.s. ∀T>0}.\mathcal{B}:=\left\{b:[0,\infty)\times\Omega\to[0,\bar{b}]\;\middle|\;b\text{ is }\mathcal{F}\_{t}\text{-prog. measurable and }\int\_{0}^{T}b\_{t}\,dt<\infty\text{ a.s. }\forall T>0\right\}. |  | (2.15) |

Let 𝒯\mathcal{T} be the set of all ℱt\mathcal{F}\_{t}-stopping times. An admissible strategy is a tuple (π,c,b,τ)∈Π×𝒞×ℬ×𝒯(\pi,c,b,\tau)\in\Pi\times\mathcal{C}\times\mathcal{B}\times\mathcal{T} that satisfies several key conditions.

###### Assumption 2.3 (Admissibility).

A control strategy (π,c,b,τ)(\pi,c,b,\tau) is considered admissible for an initial state (x,z)(x,z) if it satisfies the following conditions

1. 1.

   Regularity: The control processes must belong to their respective admissible sets, i.e., (π,c,b)∈Π×𝒞×ℬ(\pi,c,b)\in\Pi\times\mathcal{C}\times\mathcal{B}.
2. 2.

   Habit Constraint: The consumption rate must remain above a minimum proportion α\alpha of the habit level: ct≥α​Ztc\_{t}\geq\alpha Z\_{t} for almost every (t,ω)∈[0,τ](t,\omega)\in[0,\tau].
3. 3.

   Solvency Constraint: The agent’s wealth process Xt(π,c,b)X\_{t}^{(\pi,c,b)} must remain non-negative throughout the investment horizon: Xt(π,c,b)≥0X\_{t}^{(\pi,c,b)}\geq 0 for all t∈[0,τ]t\in[0,\tau] almost surely. This prevents bankruptcy.
4. 4.

   Stopping Time: The time τ\tau must be an {ℱt}\{\mathcal{F}\_{t}\}-stopping time. This ensures that the decision to annuitize is non-anticipatory and based only on information available up to that time.

The set of all such admissible strategies for a given initial state (t,x,z)(t,x,z) is denoted by 𝒜​(t,x,z)\mathcal{A}(t,x,z).

#### 2.2.4 Leisure process

The consumer maximizes utility derived from consumption ctc\_{t} and leisure ltl\_{t}, subject to choices over consumption ctc\_{t}, portfolio allocation πt\pi\_{t}, and labor supply btb\_{t}. Retirement occurs at the optimally chosen stopping time τ\tau.

A consumer is endowed with two levels of leisure. We adopt a two-level leisure specification in which the agent enjoys a lower level of leisure before retirement and a higher level afterward, consistent with Huang et al. ([2012](https://arxiv.org/html/2602.02816v1#bib.bib15)) and Ashraf ([2023](https://arxiv.org/html/2602.02816v1#bib.bib2)). The leisure process is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | lt={l1,for ​0≤t<τ(pre-retirement),l¯,for ​t≥τ(post-retirement),l\_{t}=\begin{cases}l\_{1},&\text{for }0\leq t<\tau\quad\text{(pre-retirement)},\\ \bar{l},&\text{for }t\geq\tau\quad\text{(post-retirement)},\end{cases} |  | (2.16) |

where l¯>l1≥1\bar{l}>l\_{1}\geq 1 (following Choi et al. ([2008](https://arxiv.org/html/2602.02816v1#bib.bib8)) and Koo et al. ([2013](https://arxiv.org/html/2602.02816v1#bib.bib18))). Because labor is supplied only before retirement (t<τt<\tau), we set pre-retirement leisure to l1=1l\_{1}=1 and take post-retirement leisure to satisfy l¯>1\bar{l}>1. It is worth emphasizing that, in this setup, leisure is not expressed in units of time Ashraf ([2023](https://arxiv.org/html/2602.02816v1#bib.bib2)); rather, the parameter ltl\_{t} reflects the agent’s relative utility or enjoyment of consumption after retirement compared with the working phase.

The instantaneous utility function is multiplicatively separable and given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(ct,bt)=11−γ​(ct​(l¯−bt)ψ)1−γ,U(c\_{t},b\_{t})=\frac{1}{1-\gamma}\left(c\_{t}(\bar{l}-b\_{t})^{\psi}\right)^{1-\gamma}, |  | (2.17) |

where γ>0,γ≠1\gamma>0,\gamma\neq 1 is the coefficient of relative risk aversion over the composite consumption-leisure good, l¯−bt\bar{l}-b\_{t} is leisure, and ψ>0\psi>0 is the preference weight for leisure.

The agent’s objective is to maximize the total expected discounted utility. The objective function for any strategy (π,c,b,τ)∈𝒜​(t,x,z)(\pi,c,b,\tau)\in\mathcal{A}(t,x,z) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,x,z;π,c,b,τ)=𝔼t,x,z​[∫tτe−∫ts(β+δu)​𝑑u​U​(cs,bs)​𝑑s+e−∫tτ(β+δu)​𝑑u​G​(Xτ)],J(t,x,z;\pi,c,b,\tau)=\mathbb{E}\_{t,x,z}\left[\int\_{t}^{\tau}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s},b\_{s})ds+e^{-\int\_{t}^{\tau}(\beta+\delta\_{u})du}G(X\_{\tau})\right], |  | (2.18) |

where β>0\beta>0 is the subjective time preference rate and G​(Xτ)G(X\_{\tau}) is the post-annuitization value function. For the expectation in equation ([2.18](https://arxiv.org/html/2602.02816v1#S2.E18 "Equation 2.18 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) to be well-defined, we require that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x,z​[∫tτe−∫ts(β+δu)​𝑑u​U−​(cs,bs)​𝑑s+e−∫tτ(β+δu)​𝑑u​G−​(Xτ)]<∞,\mathbb{E}\_{t,x,z}\left[\int\_{t}^{\tau}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U^{-}(c\_{s},b\_{s})\,ds+e^{-\int\_{t}^{\tau}(\beta+\delta\_{u})du}G^{-}(X\_{\tau})\right]<\infty, |  | (2.19) |

where f−=max⁡(−f,0)f^{-}=\max(-f,0) denotes the negative part of a function ff. The optimization problem is to find the value function V​(t,x,z)V(t,x,z)

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x,z)=sup(π,c,b,τ)∈𝒜​(t,x,z)J​(t,x,z;π,c,b,τ).V(t,x,z)=\sup\_{(\pi,c,b,\tau)\in\mathcal{A}(t,x,z)}J(t,x,z;\pi,c,b,\tau). |  | (2.20) |

The expression in equation ([2.20](https://arxiv.org/html/2602.02816v1#S2.E20 "Equation 2.20 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) is a stochastic optimal control problem with state variables (Xt,Zt)(X\_{t},Z\_{t}) and control variables (πt,ct,bt,τ)(\pi\_{t},c\_{t},b\_{t},\tau). The solution involves finding the optimal policies (πt∗,ct∗,bt∗,τ∗)(\pi\_{t}^{\*},c\_{t}^{\*},b\_{t}^{\*},\tau^{\*}) that attain the supremum. The remainder of the paper is dedicated to solving this problem.

###### Remark 2.1.

We assume that V​(t,x,z)<∞V(t,x,z)<\infty for all (t,x,z)(t,x,z). As noted in Bertsekas and Shreve ([1996](https://arxiv.org/html/2602.02816v1#bib.bib4)), a sufficient condition for this is that the utility functions in equation ([2.18](https://arxiv.org/html/2602.02816v1#S2.E18 "Equation 2.18 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) satisfies a growth condition. For our problem, this would mean that

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{U​(c,b),G​(x)}≤K1+K2​(x+z)η^\max\{U(c,b),G(x)\}\leq K\_{1}+K\_{2}(x+z)^{\hat{\eta}} |  | (2.21) |

for some constants K1>0,K2>0K\_{1}>0,K\_{2}>0 and η^∈(0,1)\hat{\eta}\in(0,1).

## 3 Dynamic Programming and the HJB Variational Inequality

### 3.1 Dynamic Programming Principle

The Dynamic Programming Principle (DPP) is used to solve the problem in equation ([2.20](https://arxiv.org/html/2602.02816v1#S2.E20 "Equation 2.20 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). For a combined optimal control and stopping problem, the DPP asserts that at any point in time, the optimal strategy must be the better of two choices: either to stop immediately (i.e., annuitize) or to continue for an infinitesimal time period and then proceed optimally from the new state. The optimal path is thus composed of a series of such optimal decisions.

###### Proposition 3.1 (Dynamic Programming Principle).

The value function V​(t,x,z)V(t,x,z) satisfies the following dynamic programming equation for any small time interval Δ​t>0\Delta t>0

|  |  |  |  |
| --- | --- | --- | --- |
|  | V(t,x,z)=max{G(x),sup(π,c,b)𝔼t,x,z[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(cs,bs)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑uV(t+Δt,Xt+Δ​t,Zt+Δ​t)]}.\begin{split}V(t,x,z)=\max\Biggl\{G(x),\sup\_{(\pi,c,b)}\mathbb{E}\_{t,x,z}\biggl[&\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s},b\_{s})ds\\ &+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\biggr]\Biggr\}.\end{split} |  | (3.1) |

###### Proof.

See Appendix [A.1](https://arxiv.org/html/2602.02816v1#A1.SS1 "A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").
∎

### 3.2 The Hamilton-Jacobi-Bellman Variational Inequality

Since equation ([2.20](https://arxiv.org/html/2602.02816v1#S2.E20 "Equation 2.20 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) is a combined optimal control and stopping problem, the value function must satisfy the Hamilton-Jacobi-Bellman Variational Inequality (HJBVI). Let ηt=β+δt\eta\_{t}=\beta+\delta\_{t} be the instantaneous effective discount rate. The value function V​(t,x,z)V(t,x,z) must satisfy the HJBVI

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡(supπ,c≥α​z,b{U​(c,b)−ηt​V+ℒπ,c,b​V},G​(x)−V​(t,x,z))=0.\max\left(\sup\_{\pi,c\geq\alpha z,b}\left\{U(c,b)-\eta\_{t}V+\mathcal{L}^{\pi,c,b}V\right\},\quad G(x)-V(t,x,z)\right)=0. |  | (3.2) |

where the infinitesimal generator ℒπ,c,b\mathcal{L}^{\pi,c,b} for the state process (Xt,Zt)(X\_{t},Z\_{t}) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒπ,c,b​V=∂V∂t+[r​X+π​(μ−r)−c+w​b​Z]​∂V∂x+ρ~​(c−Z)​∂V∂z+12​σ2​π2​∂2V∂x2.\mathcal{L}^{\pi,c,b}V=\frac{\partial V}{\partial t}+\left[rX+\pi(\mu-r)-c+wbZ\right]\frac{\partial V}{\partial x}+\tilde{\rho}(c-Z)\frac{\partial V}{\partial z}+\frac{1}{2}\sigma^{2}\pi^{2}\frac{\partial^{2}V}{\partial x^{2}}. |  | (3.3) |

### 3.3 Dimensionality Reduction

Solving the HJBVI in equation ([3.2](https://arxiv.org/html/2602.02816v1#S3.E2 "Equation 3.2 ‣ 3.2 The Hamilton-Jacobi-Bellman Variational Inequality ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) as a free-boundary problem with two state variables can be challenging. We employ dimensionality reduction, leveraging the homothetic properties of the utility function. This allows us to reframe the stochastic optimal control problem in terms of a single state variable: the wealth-to-habit ratio, y=x/zy=x/z. We define this ratio as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt:=XtZt.y\_{t}:=\frac{X\_{t}}{Z\_{t}}. |  | (3.4) |

This reduction yields a one-dimensional free-boundary problem that admits semi-analytical solutions, with optimal policies characterized explicitly up to a finite set of constants determined by smooth-pasting conditions. The dynamics of yty\_{t}, which are central to the reformulation of the problem are obtained by Itô’s formula applied to the quotient of XtX\_{t} and ZtZ\_{t}.

###### Lemma 3.2 (SDE for the Wealth-to-Habit Ratio).

Let the agent’s wealth process XtX\_{t} and habit process ZtZ\_{t} be governed by the SDEs in equation ([2.5](https://arxiv.org/html/2602.02816v1#S2.E5 "Equation 2.5 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) and ([2.6](https://arxiv.org/html/2602.02816v1#S2.E6 "Equation 2.6 ‣ 2.2.1 State Processes: Wealth and Habit ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), respectively. Define the portfolio weight pt:=πt/Xtp\_{t}:=\pi\_{t}/X\_{t}, and the consumption-to-habit ratio κt:=ct/Zt\kappa\_{t}:=c\_{t}/Z\_{t}. Then, the SDE governing the wealth-to-habit ratio, yt:=Xt/Zty\_{t}:=X\_{t}/Z\_{t}, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yt=[(r+ρ~)​yt+pt​yt​(μ−r)−κt​(1+ρ~​yt)+w​bt]​d​t+σ​pt​yt​d​Wt,\mathrm{d}y\_{t}=\Big[(r+\tilde{\rho})y\_{t}+p\_{t}y\_{t}(\mu-r)-\kappa\_{t}(1+\tilde{\rho}y\_{t})+wb\_{t}\Big]\mathrm{d}t+\sigma p\_{t}y\_{t}\,\mathrm{d}W\_{t}, |  | (3.5) |

###### Proof.

To derive the SDE for yty\_{t}, we apply Itô’s lemma for a quotient. Since the habit process ZtZ\_{t} has dynamics governed only by a d​t\mathrm{d}t term, it is a process of finite variation, so the Itô quotient rule simplifies to

|  |  |  |
| --- | --- | --- |
|  | d​(XtZt)=1Zt​d​Xt−XtZt2​d​Zt.\mathrm{d}\left(\frac{X\_{t}}{Z\_{t}}\right)=\frac{1}{Z\_{t}}\mathrm{d}X\_{t}-\frac{X\_{t}}{Z\_{t}^{2}}\mathrm{d}Z\_{t}. |  |

Substituting the SDEs for d​Xt\mathrm{d}X\_{t} ([2.5](https://arxiv.org/html/2602.02816v1#S2.E5 "Equation 2.5 ‣ 2.1 The Financial Market ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) and d​Zt\mathrm{d}Z\_{t} ([2.6](https://arxiv.org/html/2602.02816v1#S2.E6 "Equation 2.6 ‣ 2.2.1 State Processes: Wealth and Habit ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​yt\displaystyle\mathrm{d}y\_{t} | =1Zt​[(r​Xt+πt​(μ−r)−ct+w​bt​Zt)​d​t+σ​πt​d​Wt]−XtZt2​[ρ~​(ct−Zt)​d​t]\displaystyle=\frac{1}{Z\_{t}}\left[(rX\_{t}+\pi\_{t}(\mu-r)-c\_{t}+wb\_{t}Z\_{t})\,\mathrm{d}t+\sigma\pi\_{t}\,\mathrm{d}W\_{t}\right]-\frac{X\_{t}}{Z\_{t}^{2}}\left[\tilde{\rho}(c\_{t}-Z\_{t})\,\mathrm{d}t\right] |  | (3.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =[r​XtZt+πtZt​(μ−r)−ctZt+w​bt−ρ~​XtZt​(ctZt−1)]​d​t+σ​πtZt​d​Wt.\displaystyle=\left[r\frac{X\_{t}}{Z\_{t}}+\frac{\pi\_{t}}{Z\_{t}}(\mu-r)-\frac{c\_{t}}{Z\_{t}}+wb\_{t}-\tilde{\rho}\frac{X\_{t}}{Z\_{t}}\left(\frac{c\_{t}}{Z\_{t}}-1\right)\right]\mathrm{d}t+\sigma\frac{\pi\_{t}}{Z\_{t}}\,\mathrm{d}W\_{t}. |  | (3.7) |

We now use the dimensionless ratios yt=Xt/Zty\_{t}=X\_{t}/Z\_{t}, pt=πt/Xtp\_{t}=\pi\_{t}/X\_{t}, and κt=ct/Zt\kappa\_{t}=c\_{t}/Z\_{t}. This implies πt/Zt=pt​Xt/Zt=pt​yt\pi\_{t}/Z\_{t}=p\_{t}X\_{t}/Z\_{t}=p\_{t}y\_{t}. Substituting these definitions into equation ([3.7](https://arxiv.org/html/2602.02816v1#S3.E7 "Equation 3.7 ‣ Proof. ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yt\displaystyle\mathrm{d}y\_{t} | =[r​yt+pt​yt​(μ−r)−κt+w​bt−ρ~​yt​(κt−1)]​d​t+σ​pt​yt​d​Wt\displaystyle=\left[ry\_{t}+p\_{t}y\_{t}(\mu-r)-\kappa\_{t}+wb\_{t}-\tilde{\rho}y\_{t}(\kappa\_{t}-1)\right]\mathrm{d}t+\sigma p\_{t}y\_{t}\mathrm{d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[r​yt+pt​yt​(μ−r)−κt−ρ~​yt​κt+ρ~​yt+w​bt]​d​t+σ​pt​yt​d​Wt\displaystyle=\left[ry\_{t}+p\_{t}y\_{t}(\mu-r)-\kappa\_{t}-\tilde{\rho}y\_{t}\kappa\_{t}+\tilde{\rho}y\_{t}+wb\_{t}\right]\mathrm{d}t+\sigma p\_{t}y\_{t}\mathrm{d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[(r+ρ~)​yt+pt​yt​(μ−r)−κt​(1+ρ~​yt)+w​bt]​d​t+σ​pt​yt​d​Wt.\displaystyle=\left[(r+\tilde{\rho})y\_{t}+p\_{t}y\_{t}(\mu-r)-\kappa\_{t}(1+\tilde{\rho}y\_{t})+wb\_{t}\right]\mathrm{d}t+\sigma p\_{t}y\_{t}\,\mathrm{d}W\_{t}. |  |

This completes the derivation.
∎

The dynamics for the habit process ZtZ\_{t} can also be rewritten in terms of κt\kappa\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zt=ρ~​(ct−Zt)​d​t=ρ~​Zt​(κt−1)​d​t.dZ\_{t}=\tilde{\rho}(c\_{t}-Z\_{t})dt=\tilde{\rho}Z\_{t}(\kappa\_{t}-1)dt. |  | (3.8) |

The utility function from ([2.17](https://arxiv.org/html/2602.02816v1#S2.E17 "Equation 2.17 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) can be written in terms of the consumption-to-habit ratio κt\kappa\_{t} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(ct,bt)=(Zt)1−γ1−γ​(κt​(l¯−bt)ψ)1−γ.U(c\_{t},b\_{t})=\frac{(Z\_{t})^{1-\gamma}}{1-\gamma}\left(\kappa\_{t}(\bar{l}-b\_{t})^{\psi}\right)^{1-\gamma}. |  | (3.9) |

We now formally define the agent’s utility-maximization problem, as in ([2.18](https://arxiv.org/html/2602.02816v1#S2.E18 "Equation 2.18 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). Following the framework of Gerrard et al. ([2012](https://arxiv.org/html/2602.02816v1#bib.bib14)), the agent controls the consumption rate, the portfolio allocation, and the timing of annuitization. A fund of size xx is converted into an annuity of k​xkx, where the annuity factor k>rk>r, and this decision is irreversible. If the fund is exhausted before this point, all economic activity, including further investment or withdrawal, ceases.

###### Remark 3.1 (Annuitization Value Function).

For the annuitization phase, we assume the value function at annuitization
is analogous to the value function from the classical Merton problem following Koo et al. ([2013](https://arxiv.org/html/2602.02816v1#bib.bib18)) framework. The terminal value in ([2.18](https://arxiv.org/html/2602.02816v1#S2.E18 "Equation 2.18 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(y,Z)=e−ρ​τρτ​(k​y​Z)1−γ1−γJ(y,Z)=\frac{e^{-\rho\tau}}{\rho\_{\tau}}\frac{(kyZ)^{1-\gamma}}{1-\gamma} |  | (3.10) |

By applying the homothetic transformation G​(y)=1−γZ1−γ​J​(y,Z)G(y)=\frac{1-\gamma}{Z^{1-\gamma}}J(y,Z) and substituting X=y​ZX=yZ, we derive the terminal condition for the transformed problem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(y)=1−γZ1−γ​(e−ρ​τρτ​(k​y​Z)1−γ1−γ)=e−ρ​τ​(k​y)1−γρτ.G(y)=\frac{1-\gamma}{Z^{1-\gamma}}\left(\frac{e^{-\rho\tau}}{\rho\_{\tau}}\frac{(kyZ)^{1-\gamma}}{1-\gamma}\right)=e^{-\rho\tau}\frac{(ky)^{1-\gamma}}{\rho\_{\tau}}. |  | (3.11) |

The agent’s problem is to choose the control processes (pt,κt,ct)t≥0(p\_{t},\kappa\_{t},c\_{t})\_{t\geq 0} to maximize the objective function. By defining an effective discount rate that incorporates both the subjective time preference β\beta and the age-dependent force of mortality δt\delta\_{t}, the value function in ([2.18](https://arxiv.org/html/2602.02816v1#S2.E18 "Equation 2.18 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(y)=sup(ps,κs,bs)s≥t𝔼​[∫0τe−(ρs)​s​U​(bs,cs)​𝑑s+G​(y)].V(y)=\sup\_{(p\_{s},\kappa\_{s},b\_{s})\_{s\geq t}}\mathbb{E}\left[\int\_{0}^{\tau}e^{-(\rho\_{s})s}U(b\_{s},c\_{s})ds+G(y)\right]. |  | (3.12) |

where ρs\rho\_{s} is the effective cumulative discount rate, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρs=∫0s(β+δu)​𝑑u.\rho\_{s}=\int\_{0}^{s}(\beta+\delta\_{u})\,du. |  | (3.13) |

and U​(cs,bs)U(c\_{s},b\_{s}) is the instantaneous utility function as defined in ([3.9](https://arxiv.org/html/2602.02816v1#S3.E9 "Equation 3.9 ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) and G​(y)G(y) is the value derived from the wealth annuitized at time τ\tau as defined in ([3.11](https://arxiv.org/html/2602.02816v1#S3.E11 "Equation 3.11 ‣ Remark 3.1 (Annuitization Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). The remainder of the paper, we focus on equation ([3.12](https://arxiv.org/html/2602.02816v1#S3.E12 "Equation 3.12 ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")).

###### Definition 3.1.

The optimal retirement wealth threshold, denoted by y∗y^{\*}, is the critical level of wealth at which an agent chooses to retire to maximize their lifetime utility.

###### Definition 3.2.

The labor constraint wealth threshold, denoted by y~\tilde{y}, is the level of wealth required to ensure the optimal labor supply b∗b^{\*} is strictly less than the upper limit b¯\bar{b}. For y~≤y≤y∗\tilde{y}\leq y\leq y^{\*}, the labor constraint is binding, b∗=b¯b^{\*}=\bar{b}.

Therefore, we’ll break this optimization problem into two interlinked problems: Continuation Region (0<y<y∗0<y<y^{\*}) and Stopping Region (y≥y∗y\geq y^{\*}). We will solve the optimization problem in ([3.12](https://arxiv.org/html/2602.02816v1#S3.E12 "Equation 3.12 ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) by separating it into two interconnected phases, distinguished by an optimal retirement wealth threshold, y∗y^{\*}. The decision to transition between phases occurs at the optimal stopping time, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | τy∗=inf{t≥0:yt≥y∗}.\tau\_{y}^{\*}=\inf\{t\geq 0:y\_{t}\geq y^{\*}\}. |  | (3.14) |

This framework establishes two distinct operational regions

* •

  Continuation Region (0<y<y∗0<y<y^{\*}): In this phase, the agent actively manages their consumption and investment portfolio while working. In this region, the HJB equation should hold as an equality.
* •

  Stopping Region (y≥y∗y\geq y^{\*}): Once the state variable reaches the threshold y∗y^{\*}, the process is terminated, and the agent annuitizes their wealth. This is also called full retirement period. Here, the value function V​(y)V(y) is equal to the terminal payoff.

###### Remark 3.2 (Stationary condition of the value function).

Let V​(t,y)V(t,y) be the value function in ([3.12](https://arxiv.org/html/2602.02816v1#S3.E12 "Equation 3.12 ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), this problem is an optimal stopping problem, and the value function must satisfy the HJB variational inequality. We solve this problem by treating the agent’s age tt as a fixed parameter. This makes the instantaneous force of mortality δt\delta\_{t} and the effective discount rate ηt=β+δt\eta\_{t}=\beta+\delta\_{t} constants for a given HJB equation. The resulting value function V​(y;t)V(y;t) is thus ’stationary’ with respect to the yy variable. For notational simplicity, we write V​(y)V(y) and ηt\eta\_{t}, where tt is implicit.

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{supp,κ,b[u1​(κ,b)+ℒp,κ,b​V​(y)]−ηt​V​(y),G​(y)−V​(y)}=0,\max\left\{\sup\_{p,\kappa,b}\left[u\_{1}(\kappa,b)+\mathcal{L}^{p,\kappa,b}V(y)\right]-\eta\_{t}\,V(y),\quad G(y)-V(y)\right\}=0, |  | (3.15) |

where the generator ℒp,κ,b​V​(y)\mathcal{L}^{p,\kappa,b}V(y) is defined as

|  |  |  |
| --- | --- | --- |
|  | ℒ​V​(y)=V′​(y)​[(r+ρ)​y+p​y​(μ−r)−κ​(1+ρ​y)+w​b]+12​V′′​(y)​σ2​p2​y2,\mathcal{L}V(y)=V^{\prime}(y)\left[(r+\rho)y+py(\mu-r)-\kappa(1+\rho y)+wb\right]+\frac{1}{2}V^{\prime\prime}(y)\sigma^{2}p^{2}y^{2}, |  |

and G​(y)G(y) is the value derived from annuitizing at wealth-to-habit ratio yy.

###### Remark 3.3 (Structure of the optimal strategy).

The HJB variational inequality in ([3.15](https://arxiv.org/html/2602.02816v1#S3.E15 "Equation 3.15 ‣ Remark 3.2 (Stationary condition of the value function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) partitions the state space (y≥0y\geq 0) into two distinct regions, separated by the optimal retirement wealth threshold y∗y^{\*}.

1. 1.

   Continuation Region (y<y∗y<y^{\*}): For wealth-to-habit ratios below the threshold, it is optimal to continue working. Here, V​(y)>G​(y)V(y)>G(y) and the value function solves the HJB equation

   |  |  |  |
   | --- | --- | --- |
   |  | ηt​V​(y)=supp,κ,b[u1​(κ,b)+ℒp,κ,b​V​(y)].\eta\_{t}V(y)=\sup\_{p,\kappa,b}\left[u\_{1}(\kappa,b)+\mathcal{L}^{p,\kappa,b}V(y)\right]. |  |
2. 2.

   Stopping (Annuitization) Region (y≥y∗y\geq y^{\*}): Once the ratio reaches or exceeds y∗y^{\*}, it is optimal to annuitize. The value function is equal to the annuitization value
   V​(y)=G​(y)V(y)=G(y).

###### Theorem 3.3 (Value Function).

Given that the wealth-to-habit ratio is yt=yy\_{t}=y, assume the necessary regularity conditions in [2.3](https://arxiv.org/html/2602.02816v1#S2.Thmassumption3 "Assumption 2.3 (Admissibility). ‣ 2.2.3 Admissible Strategies and the Optimization Problem ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") hold. The value function V​(y)V(y) is given by a piecewise function

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(y)={Vint​(y),if ​y<y~,Vb¯​(y),if ​y~≤y<y∗,G​(y),if ​y≥y∗,V(y)=\begin{cases}V\_{\mathrm{int}}(y),&\text{if }y<\tilde{y},\\ V\_{\bar{b}}(y),&\text{if }\tilde{y}\leq y<y^{\*},\\ G(y),&\text{if }y\geq y^{\*},\end{cases} |  | (3.16) |

where G​(y)G(y) is the value function in the annuitization region, given by ([3.11](https://arxiv.org/html/2602.02816v1#S3.E11 "Equation 3.11 ‣ Remark 3.1 (Annuitization Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). The functions Vint​(y)V\_{\mathrm{int}}(y) and Vb¯​(y)V\_{\bar{b}}(y) are the value functions corresponding to an interior solution for labor (b<b¯b<\bar{b}) and a corner solution for labor (b=b¯b=\bar{b}), respectively, in the continuation (working) region.

###### Proof.

See Appendix [A.2](https://arxiv.org/html/2602.02816v1#A1.SS2 "A.2 Proof of Theorem 3.3 (Value Function) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").
∎

Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") establishes the qualitative structure of the value function and identifies the continuation and stopping regions in terms of the wealth-to-habit ratio. The remaining results in this section build on this structure by determining the free-boundary thresholds and deriving the corresponding optimal controls within the continuation region. In particular, we first characterize the annuitization and labor-constraint boundaries, and then derive the optimal consumption, labor, and portfolio policies conditional on non-annuitization.

###### Proposition 3.4 (Optimal Retirement Wealth Threshold).

Let Vb¯​(y)V\_{\bar{b}}(y) and G​(y)G(y) be the value functions for an agent in the final working phase (with b=b¯b=\bar{b}) and the annuitized state, respectively, as defined in Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"). The optimal retirement wealth threshold, y∗y^{\*}, is determined by the value-matching and smooth-pasting conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb¯​(y∗)\displaystyle V\_{\bar{b}}(y^{\*}) | =G​(y∗),\displaystyle=G(y^{\*}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb¯′​(y∗)\displaystyle V\_{\bar{b}}^{\prime}(y^{\*}) | =G′​(y∗),\displaystyle=G^{\prime}(y^{\*}), |  |

The threshold y∗y^{\*} is the unique solution to the non-linear algebraic equation formed by substituting these conditions into the maximized HJB equation for the Vb¯V\_{\bar{b}} region, as detailed in Appendix [A.4](https://arxiv.org/html/2602.02816v1#A1.SS4 "A.4 Proof of Proposition 3.4 (Optimal Retirement Wealth Threshold 𝑦^∗) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").

###### Proof.

See Appendix [A.4](https://arxiv.org/html/2602.02816v1#A1.SS4 "A.4 Proof of Proposition 3.4 (Optimal Retirement Wealth Threshold 𝑦^∗) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").
∎

###### Proposition 3.5 (Threshold for the Labor Constraint).

Let Vint​(y)V\_{\mathrm{int}}(y) and Vb¯​(y)V\_{\bar{b}}(y) be the value functions for the interior and corner labor solutions, respectively. The boundary between these states is a unique wealth-to-habit ratio, y~\tilde{y}, determined by the C2C^{2} continuity conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vint​(y~)\displaystyle V\_{\mathrm{int}}(\tilde{y}) | =Vb¯​(y~),\displaystyle=V\_{\bar{b}}(\tilde{y}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vint′​(y~)\displaystyle V\_{\mathrm{int}}^{\prime}(\tilde{y}) | =Vb¯′​(y~),\displaystyle=V\_{\bar{b}}^{\prime}(\tilde{y}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vint′′​(y~)\displaystyle V\_{\mathrm{int}}^{\prime\prime}(\tilde{y}) | =Vb¯′′​(y~).\displaystyle=V\_{\bar{b}}^{\prime\prime}(\tilde{y}). |  |

This system of equations implicitly defines the threshold y~\tilde{y} and the corresponding integration constants (A2,B1,B2A\_{2},B\_{1},B\_{2}), as shown in Appendix [A.5](https://arxiv.org/html/2602.02816v1#A1.SS5 "A.5 Proof of Proposition 3.5 (Labor Constraint Threshold 𝑦̃) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").

###### Proof.

See Appendix [A.5](https://arxiv.org/html/2602.02816v1#A1.SS5 "A.5 Proof of Proposition 3.5 (Labor Constraint Threshold 𝑦̃) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").
∎

We now collect the preceding results to characterize the optimal consumption, labor, and portfolio controls conditional on non-annuitization. The following theorem summarizes the optimal policies within the continuation region y<y∗y<y^{\*}, taking the value function structure and free-boundary thresholds as given. The global optimality of these controls, together with the optimal stopping rule, is established subsequently via a verification argument.

###### Theorem 3.6 (Optimal Policies in the Continuation Region).

Let V​(y)V(y) in Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") be a twice-continuously differentiable solution to the HJB variational inequality in ([3.15](https://arxiv.org/html/2602.02816v1#S3.E15 "Equation 3.15 ‣ Remark 3.2 (Stationary condition of the value function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) for y<y∗y<y^{\*}. The optimal policies are given by the following first-order conditions

1. 1.

   Optimal Portfolio: The optimal portfolio weight invested in the risky asset is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | p∗​(y)=−μ−rσ2​V′​(y)y​V′′​(y).p^{\*}(y)=-\frac{\mu-r}{\sigma^{2}}\frac{V^{\prime}(y)}{yV^{\prime\prime}(y)}. |  | (3.17) |
2. 2.

   Optimal Consumption-to-Habit Ratio: The optimal ratio κ∗\kappa^{\*} is determined by the condition that its marginal utility equals the marginal value of wealth, adjusted for its impact on the state variable dynamics

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂u​(κ∗,b∗)∂κ=V′​(y)​(1+ρ​y).\frac{\partial u(\kappa^{\*},b^{\*})}{\partial\kappa}=V^{\prime}(y)(1+\rho y). |  | (3.18) |
3. 3.

   Optimal Labor: For an interior solution where 0<b∗<b¯0<b^{\*}<\bar{b}, the optimal labor supply b∗b^{\*} satisfies the condition that the marginal disutility of labor equals its marginal contribution to the value of wealth

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂u​(κ∗,b∗)∂b=−w​V′​(y).\frac{\partial u(\kappa^{\*},b^{\*})}{\partial b}=-wV^{\prime}(y). |  | (3.19) |

   If this condition cannot be satisfied for any b∈(0,b¯)b\in(0,\bar{b}), the optimum is a corner solution at the boundary, b∗=b¯b^{\*}=\bar{b}.
4. 4.

   Marginal Rate of Substitution: Combining the conditions for optimal consumption and labor for an interior solution yields the optimality condition where the marginal rate of substitution between consumption and leisure equals the wage rate, adjusted by a state-dependent factor

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂u​(κ∗,b∗)/∂b∂u​(κ∗,b∗)/∂κ=−w1+ρ​y.\frac{\partial u(\kappa^{\*},b^{\*})/\partial b}{\partial u(\kappa^{\*},b^{\*})/\partial\kappa}=-\frac{w}{1+\rho y}. |  | (3.20) |

###### Corollary 3.7 (Actuarially Fair Annuity Rate).

The parameter kk is the annuitization value function G​(y)G(y) in ([2.18](https://arxiv.org/html/2602.02816v1#S2.E18 "Equation 2.18 ‣ 2.2.4 Leisure process ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), which represents the optimal consumption-to-wealth ratio ct/Xtc\_{t}/X\_{t} upon retirement, can be interpreted as the actuarially fair annuity rate. For an agent of age tt, this rate is the reciprocal of the annuity present value a¨t\ddot{a}\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | k=1a¨t,k=\frac{1}{\ddot{a}\_{t}}, |  | (3.21) |

where a¨t\ddot{a}\_{t} is the present value of a continuous life annuity paying 1 unit per year, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | a¨t=∫0∞e−β​s​\@mathmeasure​\@mathmeasure​Θ​s​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p​𝑑s=∫0∞e−β​s​exp⁡(−∫tt+sδu​𝑑u)​𝑑s.\ddot{a}\_{t}=\int\_{0}^{\infty}e^{-\beta s}\,\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{s}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p\,ds=\int\_{0}^{\infty}e^{-\beta s}\exp\left(-\int\_{t}^{t+s}\delta\_{u}du\right)ds. |  | (3.22) |

Here, β>0\beta>0 is the subjective discount rate, \@mathmeasure​\@mathmeasure​Θ​s​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{s}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p is the survival probability for an individual aged tt to survive ss more years, and δu\delta\_{u} is the age-dependent force of mortality at age uu.

###### Corollary 3.8 (Optimal Annuity Payment).

Given optimal policies as in Theorem [3.9](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem9 "Theorem 3.9 (Optimal Policies). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), with the optimal retirement wealth threshold y∗y^{\*}, the optimal annuity payment rate k~t∗\tilde{k}\_{t}^{\*} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | kt∗={0,if ​y<y∗(working period),ϕ​y,if ​y≥y∗(full retirement period),k\_{t}^{\*}=\begin{cases}0,&\text{if }y<y^{\*}\quad\text{(working period)},\\[6.0pt] \phi y,&\text{if }y\geq y^{\*}\quad\text{(full retirement period)},\end{cases} |  | (3.23) |

where ϕ\phi is the endogenous withdrawal rate and satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ=κt∗y=k,\phi=\frac{\kappa\_{t}^{\*}}{y}=k, |  | (3.24) |

with κt∗\kappa\_{t}^{\*} given by the optimal consumption policy in ([3.25](https://arxiv.org/html/2602.02816v1#S3.E25 "Equation 3.25 ‣ Theorem 3.9 (Optimal Policies). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")).

We now state the main verification result, which combines the value function characterization, free-boundary conditions, and continuation-region controls to establish the globally optimal policies and stopping rule.

###### Theorem 3.9 (Optimal Policies).

Assume the value function V​(y)V(y) from Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") exists. The optimal policies are functions of the state variable yt=Xt/Zty\_{t}=X\_{t}/Z\_{t} and are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | κt∗\displaystyle\kappa\_{t}^{\*} | ={(Vint′​(y)​(1+ρ​y)((l¯−bt∗)ψ)1−γ)−1/γ,if ​y<y~,(Vb¯′​(y)​(1+ρ​y)((l¯−b¯)ψ)1−γ)−1/γ,if ​y~≤y<y∗,k​y,if ​y≥y∗,\displaystyle=\begin{cases}\left(\dfrac{V^{\prime}\_{\mathrm{int}}(y)(1+\rho y)}{((\bar{l}-b\_{t}^{\*})^{\psi})^{1-\gamma}}\right)^{-1/\gamma},&\text{if }y<\tilde{y},\\[8.61108pt] \left(\dfrac{V^{\prime}\_{\bar{b}}(y)(1+\rho y)}{((\bar{l}-\bar{b})^{\psi})^{1-\gamma}}\right)^{-1/\gamma},&\text{if }\tilde{y}\leq y<y^{\*},\\[8.61108pt] ky,&\text{if }y\geq y^{\*},\end{cases} |  | (3.25) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | bt∗\displaystyle b\_{t}^{\*} | ={(1−αw​α)​(k1−γηt)−1/γ​y,if ​y<y~,b¯,if ​y~≤y<y∗,0,if ​y≥y∗,\displaystyle=\begin{cases}\left(\dfrac{1-\alpha}{w\alpha}\right)\left(\dfrac{k^{1-\gamma}}{\eta\_{t}}\right)^{-1/\gamma}y,&\text{if }y<\tilde{y},\\[8.61108pt] \bar{b},&\text{if }\tilde{y}\leq y<y^{\*},\\[4.30554pt] 0,&\text{if }y\geq y^{\*},\end{cases} |  | (3.26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | pt∗\displaystyle p\_{t}^{\*} | ={−μ−rσ2​Vint′​(y)y​Vint′′​(y),if ​y<y~,−μ−rσ2​Vb¯′​(y)y​Vb¯′′​(y),if ​y~≤y<y∗,μ−rσ2​γ,if ​y≥y∗,\displaystyle=\begin{cases}-\dfrac{\mu-r}{\sigma^{2}}\dfrac{V^{\prime}\_{\mathrm{int}}(y)}{yV^{\prime\prime}\_{\mathrm{int}}(y)},&\text{if }y<\tilde{y},\\[8.61108pt] -\dfrac{\mu-r}{\sigma^{2}}\dfrac{V^{\prime}\_{\bar{b}}(y)}{yV^{\prime\prime}\_{\bar{b}}(y)},&\text{if }\tilde{y}\leq y<y^{\*},\\[8.61108pt] \dfrac{\mu-r}{\sigma^{2}\gamma},&\text{if }y\geq y^{\*},\end{cases} |  | (3.27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | τ∗\displaystyle\tau^{\*} | =inf{t≥0:yt≥y∗}.\displaystyle=\inf\{t\geq 0:y\_{t}\geq y^{\*}\}. |  | (3.28) |

where Vint′​(y)V^{\prime}\_{\mathrm{int}}(y), Vb¯′​(y)V^{\prime}\_{\bar{b}}(y), Vint′′​(y)V^{\prime\prime}\_{\mathrm{int}}(y) and Vb¯′′​(y)V^{\prime\prime}\_{\bar{b}}(y) represent the first and second derivatives of the transformed value function with respect to yy in the respective regions defined in Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").

###### Proof.

See Appendix [A.3](https://arxiv.org/html/2602.02816v1#A1.SS3 "A.3 Proof of Theorem 3.9 (Optimal Policies) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").
∎

Section [4](https://arxiv.org/html/2602.02816v1#S4 "4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") provides an economic interpretation of the optimal policies and illustrates the resulting lifecycle regimes numerically.

## 4 Numerical Results, Implementation, and Discussion

We focus on the continuation (working) region (y<y∗y<y^{\*}), where the value function V​(y)>G​(y)V(y)>G(y), and the stopping (annuitization) region (y≥y∗y\geq y^{\*}), where V​(y)=G​(y)V(y)=G(y). The value y∗y^{\*} represents the optimal retirement wealth threshold for the wealth-to-habit ratio. We numerically implement the optimal results derived in Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") (value function)and Theorem [3.9](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem9 "Theorem 3.9 (Optimal Policies). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") (optimal policies) and discuss their implications for retirement planning under habit formation.

We set the model parameters based on representative values in the literature (e.g., Birungi and Hyndman ([2025](https://arxiv.org/html/2602.02816v1#bib.bib5)), Li et al. ([2025](https://arxiv.org/html/2602.02816v1#bib.bib21)), Gao et al. ([2022](https://arxiv.org/html/2602.02816v1#bib.bib13)), Chen et al. ([2021](https://arxiv.org/html/2602.02816v1#bib.bib7)), and Gerrard et al. ([2012](https://arxiv.org/html/2602.02816v1#bib.bib14))), considering an agent aged 60 with an age-dependent force of mortality δt\delta\_{t}. Unless otherwise stated, the market parameters include a risk-free rate r=0.02r=0.02, a risky asset mean return μ=0.07\mu=0.07, and volatility σ=0.2\sigma=0.2, implying a market price of risk θ=(μ−r)/σ=0.25\theta=(\mu-r)/\sigma=0.25. The agent’s preference parameters are set as follows: a subjective discount rate β=0.03\beta=0.03 (though we may vary this for sensitivity analysis, e.g., in the range (0.01,0.055)(0.01,0.055)), a relative risk aversion coefficient γ=2.0\gamma=2.0, a leisure preference parameter ψ=0.5\psi=0.5, and a maximum leisure endowment l¯=1.0\bar{l}=1.0. Labor parameters include a wage rate w=10.0w=10.0 and a maximum labor supply b¯=0.8\bar{b}=0.8. The annuity consumption rate parameter kk is typically determined endogenously or via Corollary [3.7](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem7 "Corollary 3.7 (Actuarially Fair Annuity Rate). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"). Finally, mortality is modeled using an age-dependent force δt\delta\_{t} (e.g., following the Gompertz law in ([2.10](https://arxiv.org/html/2602.02816v1#S2.E10 "Equation 2.10 ‣ 2.2.2 Deterministic force of mortality ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"))), which combines with the subjective discount rate to form the effective discount rate ηt=β+δt\eta\_{t}=\beta+\delta\_{t}.

This section explores the optimal pre- and post-retirement strategies under CRRA utility functions defined over the consumption-to-habit ratio κt\kappa\_{t} and leisure (l¯−bt)(\bar{l}-b\_{t}) as described in ([3.9](https://arxiv.org/html/2602.02816v1#S3.E9 "Equation 3.9 ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). We analyze how habit formation influences the optimal policies; consumption (κt∗\kappa\_{t}^{\*}), labor (bt∗b\_{t}^{\*}), portfolio weight (pt∗p\_{t}^{\*}), and annuitization timing (τ∗\tau^{\*}).

![Refer to caption](Interior_labor.png)


Figure 1: Optimal Policy: Case I (Interior labor solution).

![Refer to caption](Corner_labor.png)


Figure 2: Optimal Policy: Case II (Corner labor solution).

[Figure 1](https://arxiv.org/html/2602.02816v1#S4.F1 "Figure 1 ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") and [Figure 2](https://arxiv.org/html/2602.02816v1#S4.F2 "Figure 2 ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") illustrate the interior and corner labor solutions, respectively, providing a schematic overview of the optimal policies, specifically the consumption-to-habit ratio κt∗\kappa\_{t}^{\*} and the labor supply bt∗b\_{t}^{\*}, for a given marginal value of wealth V′​(y)V^{\prime}(y). The tangency point of the interior labor solution occurs within the feasible labor set, indicating that the optimal labor supply bt∗b\_{t}^{\*} is less than the maximum b¯\bar{b}. In the case of the corner labor solution, the agent is constrained by the maximum labor supply b¯\bar{b}, which forces the optimal point to the boundary.

### 4.1 Policy Characterization

The optimal policies exhibit three economically distinct regimes: a habit-poor region in which labor is supplied defensively to protect consumption standards, a work-to-retire region characterized by maximal labor effort to accelerate annuitization, and a retirement region following irreversible annuitization. In this section, we interpret the behaviour of the optimal policies as functions of the agent’s age (tt) and wealth-to-habit ratio (yty\_{t}), as visualized in the Figures [3](https://arxiv.org/html/2602.02816v1#S4.F3 "Figure 3 ‣ 4.1.1 Optimal consumption to habit ratio (𝜅_𝑡^∗) ‣ 4.1 Policy Characterization ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), [4](https://arxiv.org/html/2602.02816v1#S4.F4 "Figure 4 ‣ 4.1.1 Optimal consumption to habit ratio (𝜅_𝑡^∗) ‣ 4.1 Policy Characterization ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), and [5](https://arxiv.org/html/2602.02816v1#S4.F5 "Figure 5 ‣ 4.1.1 Optimal consumption to habit ratio (𝜅_𝑡^∗) ‣ 4.1 Policy Characterization ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization").

The determination of these optimal policies involves plotting the utility surface u​(κt,bt)u(\kappa\_{t},b\_{t}) and finding the point of tangency with the plane derived from the maximization step of the HJBVI (Hamilton-Jacobi-Bellman Variational Inequality) in equation ([3.15](https://arxiv.org/html/2602.02816v1#S3.E15 "Equation 3.15 ‣ Remark 3.2 (Stationary condition of the value function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). This optimal tangency point defines (κt∗,bt∗)(\kappa\_{t}^{\*},b\_{t}^{\*}). In Case I (interior labor solution), this scenario occurs when the wealth-to-habit ratio yy lies below the labor-constrained threshold y~\tilde{y}, so that the optimal labor supply is unconstrained and satisfies bt∗<b¯b\_{t}^{\*}<\bar{b}. In Case II (corner labor solution) the labor constraint binds for y~≤y<y∗\tilde{y}\leq y<y^{\*}, in which case the optimal labor supply reaches the boundary bt∗=b¯b^{\*}\_{t}=\bar{b}

#### 4.1.1 Optimal consumption to habit ratio (κt∗\kappa\_{t}^{\*})

As illustrated in [Figure 3](https://arxiv.org/html/2602.02816v1#S4.F3 "Figure 3 ‣ 4.1.1 Optimal consumption to habit ratio (𝜅_𝑡^∗) ‣ 4.1 Policy Characterization ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), the optimal consumption-to-habit ratio κt∗\kappa\_{t}^{\*} exhibits clear dependencies on both state variables. In terms of wealth effect, κt∗\kappa\_{t}^{\*} is strongly increasing with respect to the wealth-to-habit ratio yty\_{t}. As the agent becomes wealthier relative to their habit (yty\_{t} increases), they optimally choose to consume a larger fraction of their habit level, reflecting the standard wealth effect under CRRA preferences. A noticeable change in slope or level occurs at the
optimal retirement wealth threshold y∗y^{\*}, where the policy transitions to the linear rule κt∗=k​y\kappa\_{t}^{\*}=ky.

![Refer to caption](kappa_star_surface.png)


Figure 3: Optimal consumption-to-habit surface as a function of age and the wealth-to-habit ratio.

![Refer to caption](b_star_surface.png)


Figure 4: Optimal labor supply surface as a function of age and the wealth-to-habit ratio.

![Refer to caption](p_star_surface.png)


Figure 5: Optimal portfolio weight surface as a function of age and the wealth-to-habit ratio.

In terms of age effect, the influence of age is primarily channelled through the effective discount rate ηt=β+δt\eta\_{t}=\beta+\delta\_{t}. If mortality δt\delta\_{t} increases significantly with age, ηt\eta\_{t} rises, making the agent more impatient. This may lead to a slight increase in κt∗\kappa\_{t}^{\*} with age for a given yty\_{t}, as the agent prioritizes current consumption due to a shorter expected horizon. However, this effect is generally less pronounced than the wealth effect.

#### 4.1.2 Optimal labor supply (bt∗b\_{t}^{\*})

[Figure 4](https://arxiv.org/html/2602.02816v1#S4.F4 "Figure 4 ‣ 4.1.1 Optimal consumption to habit ratio (𝜅_𝑡^∗) ‣ 4.1 Policy Characterization ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") illustrates the distinct regimes governing the optimal labor supply bt∗b\_{t}^{\*}. In terms of wealth effect, labor supply demonstrates a non-monotonic relationship with the wealth-to-habit ratio yty\_{t}. For low yy(y<y~y<\tilde{y}), bt∗b\_{t}^{\*} is positive and determined by the interior solution, potentially increasing with yty\_{t} as the agent works to accumulate wealth. At the subsistence consumption wealth threshold y~\tilde{y}, bt∗b\_{t}^{\*} jumps to its upper bound b¯\bar{b}, indicating maximal work effort for intermediate levels of yty\_{t}. Finally, upon reaching the optimal retirement wealth threshold y∗y^{\*}, bt∗b\_{t}^{\*} drops discontinuously to zero as the agent retires.

Age influences the decision to supply labor. As the agent ages and the force of mortality δt\delta\_{t} increases, the present value of future wage income decreases. This may reduce the incentive to work, potentially causing a slight decrease in the interior labor supply (for y<y~y<\tilde{y}) and possibly lowering the thresholds y~\tilde{y} and y∗y^{\*} over time, making retirement more attractive earlier.

#### 4.1.3 Optimal portfolio weight (pt∗p\_{t}^{\*})

The optimal fraction of wealth invested in the risky asset, pt∗p\_{t}^{\*}, is shown in [Figure 5](https://arxiv.org/html/2602.02816v1#S4.F5 "Figure 5 ‣ 4.1.1 Optimal consumption to habit ratio (𝜅_𝑡^∗) ‣ 4.1 Policy Characterization ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"). Under the assumption of CRRA utility, the optimal portfolio weight pt∗p\_{t}^{\*} is largely independent of the wealth-to-habit ratio yty\_{t} within the continuation region (y<y∗y<y^{\*}). It is approximately equal to the Merton ratio μ−r/σ2​γeff\mu-r/\sigma^{2}\gamma\_{\text{eff}}, (see Koo et al. ([2013](https://arxiv.org/html/2602.02816v1#bib.bib18))) where γeff\gamma\_{\text{eff}} is the effective risk aversion derived from the value function (−V′​(y)/y​V′′​(y)-V^{\prime}(y)/yV^{\prime\prime}(y)). While γeff\gamma\_{\text{eff}} might vary slightly between the VintV\_{\mathrm{int}} and Vb¯V\_{\bar{b}} regions, causing small shifts at y~\tilde{y}, the allocation remains relatively stable. In the full retirement region (y≥y∗y\geq y^{\*}), the policy becomes constant, pt∗=μ−r/σ2​γp\_{t}^{\*}=\mu-r/\sigma^{2}\gamma, consistent with the standard Merton problem (see Koo et al. ([2013](https://arxiv.org/html/2602.02816v1#bib.bib18)) and Remark 3.6.8 in Bertsekas and Shreve ([1996](https://arxiv.org/html/2602.02816v1#bib.bib4)))

In this model setup, where the primary age-dependent factor is mortality influencing impatience rather than risk aversion or investment opportunities, the optimal portfolio weight pt∗p\_{t}^{\*} is expected to be largely insensitive to age. The constant relative risk aversion implies a constant allocation fraction throughout the lifecycle.

### 4.2 Habit formation influences on optimal policies

To understand the impact of habit formation, the labor-leisure choice, and the annuitization option, [Figure 6](https://arxiv.org/html/2602.02816v1#S4.F6 "Figure 6 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), [Figure 7](https://arxiv.org/html/2602.02816v1#S4.F7 "Figure 7 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), and [Figure 8](https://arxiv.org/html/2602.02816v1#S4.F8 "Figure 8 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") compares the optimal policies derived from our model against a standard CRRA benchmark. The benchmark represents the simple post-annuitization policy (the case where y≥y∗y\geq y^{\*}). The comparison is shown across different levels of risk aversion (γ\gamma) as a function of the wealth-to-habit ratio (yty\_{t}). [Figure 6](https://arxiv.org/html/2602.02816v1#S4.F6 "Figure 6 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") reveal how the pre-annuitization phase or working period with its active labor-leisure trade-off and consumption-smoothing goals cause optimal policies to deviate significantly from this simple benchmark.

![Refer to caption](Optimal_Kappa.png)


Figure 6: Optimal consumption-to-habit ratio policy under deterministic force of mortality.

![Refer to caption](Optimal_labor_supply.png)


Figure 7: Optimal labor supply policy under a deterministic force of mortality.

![Refer to caption](optimal_portfolio_weight.png)


Figure 8: Optimal risky investment strategy under a deterministic force of mortality.

#### 4.2.1 Habit formation influences on optimal consumption to habit ratio

[Figure 6](https://arxiv.org/html/2602.02816v1#S4.F6 "Figure 6 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") shows the direct impact of consumption habits and the labor-leisure trade-off.

In the defensive consumption (y<y∗y<y^{\*}), optimal consumption to habit ratio policies derived from our model differ significantly from the simple benchmark (κt∗=k​y\kappa\_{t}^{\*}=ky). At low yy, the agent is “habit-poor” and fights to prevent κt∗\kappa\_{t}^{\*} from falling too low. They achieve this defensive consumption by supplementing wealth with wage income (from bt∗>0b\_{t}^{\*}>0). This is the core interplay of labor being sacrificed to protect the habit.

Another property of our policies is discontinuities: optimal strategies are functions of the state variable yt=Xt/Zty\_{t}=X\_{t}/Z\_{t} as seen in Theorem [3.9](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem9 "Theorem 3.9 (Optimal Policies). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"). The policy exhibits two sharp changes. The first is a jump at y=y~y=\tilde{y}, where the labor supply policy switches from interior to the corner solution b¯\bar{b}. The second is a kink at y=y∗y=y^{\*}, where the policy smoothly connects to the linear annuitization rule, demonstrating the smooth-pasting condition. And for risk aversion (γ\gamma), higher γ\gamma makes the agent become more careful and conservative in managing risk or uncertainty. They reduce consumption (i.e., exhibit a lower κt∗\kappa\_{t}^{\*}) across all levels of yy, thereby accumulating a larger buffer of precautionary savings against future uncertainty.

#### 4.2.2 Habit formation influences on optimal labor supply

[Figure 7](https://arxiv.org/html/2602.02816v1#S4.F7 "Figure 7 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") illustrates the labor-leisure trade-off as the primary engine of the pre-annuitization phase or working period. The benchmark is bt∗=0b\_{t}^{\*}=0 representing the post-annuitization state or full retirement period. In our model, the agent actively uses labor to manage their financial position relative to their habit.

When “habit-poor”, the agent’s wealth is low relative to their accustomed lifestyle. To protect their consumption habit, they sacrifice leisure and supply interior labor (bt∗>0b\_{t}^{\*}>0). This wage income provides a crucial buffer to supplement wealth.

In the  “work-to-retire” zone, the agent enters a phase of maximal work (bt∗=b¯b\_{t}^{\*}=\bar{b}). They are wealthy enough that the annuitization goal is in sight, but not so wealthy that they can stop. They work as hard as possible to bridge the gap and reach the full retirement threshold y∗y^{\*}.

In the full retirement period, the agent exercises their option to annuitize or retire. They have sufficient wealth to lock in a lifetime consumption stream. Labor immediately drops to zero, and they enter full retirement.

As for risk aversion (γ\gamma), higher γ\gamma (more cautious) agents supply more labor in the interior region (y<y~y<\tilde{y}). They prefer a certain income from labor over the uncertain returns from financial investment which they hold less of, ( see Figure [7](https://arxiv.org/html/2602.02816v1#S4.F7 "Figure 7 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). They work more to self-insure.

#### 4.2.3 Habit formation influences on optimal risky investment

[Figure 8](https://arxiv.org/html/2602.02816v1#S4.F8 "Figure 8 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") shows the optimal scaled risky investment, π^t∗​(y)=πt∗/Zt\hat{\pi}\_{t}^{\*}(y)=\pi\_{t}^{\*}/Z\_{t}, showing the interplay between financial risk taking and labor income. The slope of the line in this figure represents the optimal portfolio weight pt∗p\_{t}^{\*}. The benchmark policy is given by the line π^b​e​n​c​h∗​(y)=pb​e​n​c​h∗⋅y\hat{\pi}\_{bench}^{\*}(y)=p\_{bench}^{\*}\cdot y, where pb​e​n​c​h∗=(μ−r)/(σ2​γ)p\_{bench}^{\*}=(\mu-r)/(\sigma^{2}\gamma) is the constant Merton weight that represents the investment policy of a "pure" investor with no labor income. During the working period, the agent’s ability to work acts as a “human capital” buffer. This labor income allows the agent to take more risk in their financial portfolio. This is why the ’optimal’ line (γ=2.0\gamma=2.0) in [Figure 8](https://arxiv.org/html/2602.02816v1#S4.F8 "Figure 8 ‣ 4.2 Habit formation influences on optimal policies ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") has a steeper slope than its corresponding ’Benchmark’ line (γ=2.0\gamma=2.0) and the other ’optimal’ lines.

There is a discontinuity at full retirement (y=y∗y=y^{\*}), at this optimal retirement wealth threshold, the agent retires, and their labor income drops to zero. Their human capital vanishes instantly. To compensate for this loss of a "safe" asset, they immediately become more conservative in their financial portfolio. Their optimal portfolio weight pt∗p\_{t}^{\*} drops discontinuously to the lower Merton benchmark pb​e​n​c​h∗p\_{bench}^{\*}. This creates the distinct downward kink (a drop in the slope) in the scaled investment plot at y∗y^{\*}. As for risk aversion (γ\gamma), a higher γ\gamma (more risk-averse) means the agent is less willing to bear market risk. This lowers their optimal portfolio weight pt∗p\_{t}^{\*} in all regions, resulting in a flatter slope for both the ’optimal’ and ’benchmark’ lines.

### 4.3 Mortality risk and survival probability

[Figure 9](https://arxiv.org/html/2602.02816v1#S4.F9 "Figure 9 ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") illustrates the relationship between mortality risk and survival probability in the agent’s decision-making process from age 60. It shows that an agent’s subjective mortality risk (represented by the modal age of death, mm) has a significant impact on their optimal policies. The key mechanism is the agent’s effective discount rate, ηt=β+δt\eta\_{t}=\beta+\delta\_{t}, which is directly influenced by the force of mortality δt\delta\_{t}.

![Refer to caption](survival_probability.png)


Figure 9: Agent survival probabilities from age 60 (\@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​660​\@mathmeasure​8​(δ)​​p)\left(\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{60}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p\right) under the Gompertz law, characterized by the modal age of death (mm) and the dispersion parameter (λ\lambda). Results are shown for λ=10\lambda=10 and varying subjective modal ages (mm).

As seen in [Figure 9](https://arxiv.org/html/2602.02816v1#S4.F9 "Figure 9 ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"), the high mortality risk case (e.g., when m=60m=60), the survival probability, \@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p drops very quickly. The agent’s effective time horizon is very short. This affects the agent’s patience, that is because n=mn=m, the force of mortality δt\delta\_{t} is high from the beginning. This causes the effective discount rate ηt\eta\_{t} to be very high, making the agent impatient. For retirement and annuitization, the value of the lifelong income stream option declines substantially. If lifelong is expected to be very short (as the black line(m=60m=60) shows in [Figure 9](https://arxiv.org/html/2602.02816v1#S4.F9 "Figure 9 ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), there is minimal incentive to save for a future that is unlikely to occur. This implies the optimal retirement wealth threshold y∗y^{\*} will be very low. In terms of interplay of mortality risk with labor and consumption, because the future is so uncertain (per the m=60m=60 curve) and the annuitization prize has low value, the agent will work less (lower bt∗b\_{t}^{\*}) and consume more (higher κt∗\kappa\_{t}^{\*}) today. The labor-leisure trade-off shifts heavily towards current consumption and leisure.

There is low mortality risk (e.g., the m=80m=80). This shows that the survival probability, \@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p, declines very slowly. The agent perceives a long and probable future, as they are 20 years away from their modal age of death. Again, this affects the agent’s patience; that is, the force of mortality, δt\delta\_{t}, is low for many years. This keeps the effective discount rate ηt\eta\_{t} low, making the agent "patient." Annuitization becomes highly valuable since it represents a guaranteed, high-value income stream for decades. This creates a powerful incentive to work and save to achieve this goal. Regarding the interplay with labor and consumption, the agent is highly motivated to reach the optimal retirement wealth threshold y∗y^{\*}. This means the agent will work more (higher bt∗b\_{t}^{\*}) and save more by consuming less (lower κt∗\kappa\_{t}^{\*}) during their working years. The labor-leisure trade-off shifts towards labor to secure the valuable retirement prize.

In summary, the mortality risk and survival probability curve dictates the agent’s motivation. A steep curve (like m=60m=60) breaks the incentive to save, leading to less work, higher current consumption, and a lower annuitization target. A flat curve (like m=80m=80) strengthens the incentive to save, leading to more work, more saving, and a higher, more valuable annuitization goal.

#### 4.3.1 Mortality risk after retirement

[Figure 9](https://arxiv.org/html/2602.02816v1#S4.F9 "Figure 9 ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") and Table [1](https://arxiv.org/html/2602.02816v1#S4.T1 "Table 1 ‣ 4.3.1 Mortality risk after retirement ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") illustrate the effect of subjective mortality beliefs on the agent’s annuitization decision. The values in Table [1](https://arxiv.org/html/2602.02816v1#S4.T1 "Table 1 ‣ 4.3.1 Mortality risk after retirement ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") are calculated as a Normalized Premium Ratio (NPR). This ratio compares the agent’s perceived value of the annuity (Subjective Premium P~\tilde{P}) to the insurer’s market price (Objective Premium PobjP\_{\text{obj}}).

Table 1: Normalized subjective annuity premium P~0A\tilde{P}\_{0}^{A} for a 60-year-old agent,
given an objective premium P0A=1P\_{0}^{A}=1 based on an insurer’s modal age m=80.0m=80.0.

| Parameters | Subjective modal age m~\tilde{m} | Normalized annuity premium P~0A\tilde{P}\_{0}^{A} |
| --- | --- | --- |
| Case 1 | 60.0 | 0.3642 |
| Case 2 | 65.0 | 0.4913 |
| Case 3 | 70.0 | 0.6385 |
| Case 4 | 75.0 | 0.8066 |
| Case 5 | 80.0 | 1.0000 |

\*The second column represents the subjective modal age m~\tilde{m} for which the normalized annuity premium P~0A\tilde{P}\_{0}^{A} is computed.
\*\*Basic parameters:\*\* n=60n=60, λ=10\lambda=10, r=0.02r=0.02, and P0A=1P\_{0}^{A}=1.

The premium PP for a $1 continuous annuity is its actuarial present value, defined by the agent’s current age nn, modal age mm, dispersion λ\lambda, and the risk-free rate rr

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(m)=∫0∞e−r​t⋅\@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p​(m)​𝑑tP(m)=\int\_{0}^{\infty}e^{-rt}\cdot\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p(m)dt |  | (4.1) |

where \@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p​(m)\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p(m) is the Gompertz survival probability from equation ([2.11](https://arxiv.org/html/2602.02816v1#S2.E11 "Equation 2.11 ‣ 2.2.2 Deterministic force of mortality ‣ 2.2 Problem Formulation ‣ 2 Economic background ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")). The NPR is the ratio of the premium calculated using the agent’s subjective modal age, m~\tilde{m}, to the premium calculated using the insurer’s objective modal age, mobjm\_{\text{obj}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | NPR​(m~)=P~Pobj=P​(m~)P​(mobj)=∫0∞e−r​t⋅\@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p​(m)​𝑑t∫0∞e−r​t⋅\@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p​(mobj)​𝑑t\text{NPR}(\tilde{m})=\frac{\tilde{P}}{P\_{\text{obj}}}=\frac{P(\tilde{m})}{P(m\_{\text{obj}})}=\frac{\int\_{0}^{\infty}e^{-rt}\cdot\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p(m)\,dt}{\int\_{0}^{\infty}e^{-rt}\cdot\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p(m\_{\text{obj}})dt} |  | (4.2) |

We classify agents as pessimistic retirees, that is, pessimistic retirees (those with m~<80.0\tilde{m}<80.0), a group of individuals who believe they will die sooner than the "objective" insurer’s estimate of m=80m=80. Extreme pessimism (m~=60.0\tilde{m}=60.0), as shown in [Figure 9](https://arxiv.org/html/2602.02816v1#S4.F9 "Figure 9 ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") with m~=60.0\tilde{m}=60.0), this agent is already at their modal age of death. Their survival probability drops sharply.
Table [1](https://arxiv.org/html/2602.02816v1#S4.T1 "Table 1 ‣ 4.3.1 Mortality risk after retirement ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") shows their subjective premium is only 36.4% of the market price. For them, the annuity is perceived as an extremely bad deal. Moderate pessimism (m~=75.0\tilde{m}=75.0) refers to agents who expect to die 5 years earlier than the benchmark, still only valuing the annuity at 80.7% of its price.

The economic implication of all pessimistic agents, NPR<1\text{NPR}<1, is that they perceive the value of annuitization as low. This disincentivizes annuitization, which in our model translates to a higher annuitization threshold y∗y^{\*} , or, in extreme cases, to effectively avoiding annuitization altogether.

On the other hand, the neutral retiree (m~=80.0\tilde{m}=80.0), is an agent’s beliefs (illustrated by m~=80.0\tilde{m}=80.0 in [Figure 9](https://arxiv.org/html/2602.02816v1#S4.F9 "Figure 9 ‣ 4.3 Mortality risk and survival probability ‣ 4 Numerical Results, Implementation, and Discussion ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) align perfectly with the insurer’s. They perceive the annuity as fairly priced (NPR=1.0000\text{NPR}=1.0000). They will annuitize at the "baseline" threshold y∗y^{\*} calculated by the model, balancing current work and consumption against the fair value of a future income stream.

## 5 Conclusion

This paper studied a coupled stochastic optimal control and optimal stopping problem in which an agent jointly manages consumption relative to habit, flexible labor supply, portfolio choice, and an irreversible annuitization decision under age-dependent mortality. By formulating the problem as a Hamilton-Jacobi-Bellman variational inequality and exploiting homotheticity, we derived tractable semi-analytical solutions characterizing optimal policies across the lifecycle.

The model generates a rich sequence of retirement dynamics. When wealth is low relative to habit, labor is used defensively to protect consumption standards. As wealth accumulates, agents enter a work-to-retire phase in which labor is supplied at its maximum level to accelerate access to retirement and annuitization. Human capital acts as a stabilizing asset during working life, justifying more aggressive portfolio risk-taking, followed by an abrupt de-risking at annuitization when this asset vanishes.

Subjective mortality beliefs play a central role in shaping annuitization behavior. Agents with pessimistic longevity beliefs rationally perceive annuities as unattractive, leading them to delay or avoid annuitization since it requires higher retirement thresholds. In this way, the model provides a behavior-based explanation for low annuity demand without appealing to market frictions or irrationality.

Overall, the numerical analysis highlights how habit formation and endogenous labor supply fundamentally reshape retirement dynamics, portfolio risk-taking, and annuitization decisions. From a practical perspective, the results suggest that pre-retirement financial advice should account explicitly for labor flexibility and subjective longevity beliefs, supporting aggressive pre-retirement investment strategies followed by sharp de-risking at retirement.

Several extensions merit future investigation. Incorporating stochastic labor income or stochastic market volatility would introduce additional hedging motives. Allowing for partial annuitization rather than an all-or-nothing decision would add further realism. Modeling health status as a stochastic factor jointly affecting mortality and leisure preferences would also be a valuable extension, but is beyond the scope of this paper.

As populations age and defined-contribution retirement systems become increasingly prevalent, models that bridge psychological realism and financial optimization are essential for understanding retirement behavior and informing long-term financial planning.

## References

* Angoshtari et al. [2023]

  Bahman Angoshtari, Erhan Bayraktar, and Virginia R Young.
  Optimal consumption under a habit-formation constraint: The
  deterministic case.
  *SIAM Journal on Financial Mathematics*, 14(2):557–597, 2023.
* Ashraf [2023]

  Bushra Shehnam Ashraf.
  *Voluntary Retirement and Optimal Consumption in a Stochastic
  Mortality Environment*.
  PhD thesis, York University, Toronto, Canada, 2023.
* Barucci and Marazzina [2012]

  Emilio Barucci and Daniele Marazzina.
  Optimal investment, stochastic labor income and retirement.
  *Applied Mathematics and Computation*, 218(9):5588–5604, 2012.
* Bertsekas and Shreve [1996]

  Dimitri Bertsekas and Steven E Shreve.
  *Stochastic optimal control: the discrete-time case*, volume 5.
  Athena Scientific, Belmont, Massachusetts, 1996.
* Birungi and Hyndman [2025]

  Criscent Birungi and Cody Hyndman.
  Optimal annuitization with labor income under age-dependent force of
  mortality.
  *arXiv preprint arXiv:2510.10371*, 2025.
* Buttarazzi et al. [2025]

  Matteo Buttarazzi, Tiziano De Angelis, and Gabriele Stabile.
  Optimal annuitization with stochastic mortality: Piecewise
  deterministic mortality force.
  *arXiv preprint arXiv:2509.13091*, 2025.
* Chen et al. [2021]

  An Chen, Peter Hieber, and Manuel Rach.
  Optimal retirement products under subjective mortality beliefs.
  *Insurance: Mathematics and Economics*, 101:55–69,
  2021.
* Choi et al. [2008]

  Kyoung Jin Choi, Gyoocheol Shim, and Yong Hyun Shin.
  Optimal portfolio, consumption-leisure and retirement choice problem
  with CES utility.
  *Mathematical Finance*, 18(3):445–472,
  2008.
* Constantinides [1990]

  George M. Constantinides.
  Habit formation: A resolution of the equity premium puzzle.
  *Journal of Political Economy*, 98(3):519–543, 1990.
* Cvitanić and Karatzas [1992]

  Jakša Cvitanić and Ioannis Karatzas.
  Convex duality in constrained portfolio optimization.
  *The Annals of Applied Probability*, pages 767–818, 1992.
* Detemple and Zapatero [1991]

  Jérôme Detemple and Fernando Zapatero.
  Asset prices in an exchange economy with habit formation.
  *Econometrica*, 59(6):1633–1657, 1991.
* Dybvig [1995]

  Philip H. Dybvig.
  Duesenberry’s ratcheting of consumption: Optimal dynamic
  consumption and investment given intolerance for any decline in standard of
  living.
  *The Review of Economic Studies*, 62(2):287–313, 1995.
* Gao et al. [2022]

  Xiang Gao, Cody Hyndman, Traian A Pirvu, and Petar Jevtić.
  Optimal annuitization post-retirement with labor income.
  *arXiv preprint arXiv:2202.04220*, 2022.
* Gerrard et al. [2012]

  Russell Gerrard, Bjarne Højgaard, and Elena Vigna.
  Choosing the optimal annuitization time post-retirement.
  *Quantitative Finance*, 12(7):1143–1159,
  2012.
* Huang et al. [2012]

  Huaxiong Huang, Mooshe A Milevsky, and Thomas S Salisbury.
  Yaari’s lifecycle model in the 21st century: consumption under a
  stochastic force of mortality.
  In *Risk Theory Society Seminar paper*, March 2012.
* Karatzas and Shreve [1998]

  Ioannis Karatzas and Steven E. Shreve.
  *Methods of Mathematical Finance*, volume 39 of
  *Applications of Mathematics*.
  Springer, New York, 1998.
* Karatzas and Wang [2000]

  Ioannis Karatzas and Hui Wang.
  Utility maximization with discretionary stopping.
  *SIAM Journal on Control and Optimization*, 39(1):306–329, 2000.
* Koo et al. [2013]

  Jung Lim Koo, Byung Lim Koo, and Yong Hyun Shin.
  An optimal investment, consumption, leisure, and voluntary retirement
  problem with cobb–douglas utility: dynamic programming approaches.
  *Applied Mathematics Letters*, 26(4):481–486, 2013.
* Labbé and Heunis [2007]

  Chantal Labbé and Andrew J Heunis.
  Convex duality in constrained mean-variance portfolio optimization.
  *Advances in Applied Probability*, 39(1):77–104, 2007.
* Lee and Shin [2015]

  Ho-Seok Lee and Yong Hyun Shin.
  An optimal portfolio, consumption-leisure and retirement choice
  problem with ces utility: a dynamic programming approach.
  *Journal of Inequalities and Applications*, 2015:1–13, 2015.
* Li et al. [2025]

  Shuang Li, Hui Meng, and Ming Zhou.
  Optimal consumption-leisure-investment and retirement choices with
  nonconcave aspirational utility.
  *Insurance: Mathematics and Economics*, page 103165, 2025.
* Lorenz and Zwick [2021]

  Svenja Lorenz and Thomas Zwick.
  Money also is sunny in a retiree’s world: financial incentives and
  work after retirement.
  *Journal for Labour Market Research*, 55(1):1–17, 2021.
* Merton [1969]

  Robert C Merton.
  Lifetime portfolio selection under uncertainty: The continuous-time
  case.
  *The Review of Economics and Statistics*, pages 247–257, 1969.
* Merton [1971]

  Robert C. Merton.
  Optimum consumption and portfolio rules in a continuous-time model.
  *Journal of Economic Theory*, 3(4):373–413,
  1971.
* Mutik [2021]

  Aïssa Mutik.
  How to quit your job in the great resignation.
  Bloomberg Businessweek, May 2021.
* Peng and Li [2023]

  Xingchun Peng and Baihui Li.
  Optimal investment, consumption and life insurance purchase with
  learning about return predictability.
  *Insurance: Mathematics and Economics*, 113:70–95,
  2023.
* Rockafellar and Wets [1998]

  R. Tyrrell Rockafellar and Roger J.-B. Wets.
  *Variational Analysis*, volume 317 of *Grundlehren der
  mathematischen Wissenschaften*.
  Springer, Berlin, Heidelberg, 1998.
* Sundaresan [1989]

  Suresh M. Sundaresan.
  Intertemporally dependent preferences and the volatility of
  consumption and wealth.
  *The Review of Financial Studies*, 2(1):73–89, 1989.

## Appendix A Appendix: Detailed Proofs of Theorems

This appendix provides detailed derivations for the main results of the paper.

### A.1 Proof of Proposition [3.1](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem1 "Proposition 3.1 (Dynamic Programming Principle). ‣ 3.1 Dynamic Programming Principle ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"): Dynamic Programming Principle (DPP)

The proof of the Dynamic Programming Principle follows standard arguments for combined control and stopping problems and is included for completeness.

###### Proof.

Let the objective functional for an admissible strategy (π,c,b)(\pi,c,b) and a stopping time τ\tau be denoted by J​(t,x,z;π,c,b,τ)J(t,x,z;\pi,c,b,\tau). The value function is defined as the supremum over the set of all admissible strategies 𝒜\mathcal{A}, such that

|  |  |  |
| --- | --- | --- |
|  | V​(t,x,z)=sup(π,c,b,τ)∈𝒜J​(t,x,z;π,c,b,τ).V(t,x,z)=\sup\_{(\pi,c,b,\tau)\in\mathcal{A}}J(t,x,z;\pi,c,b,\tau). |  |

To prove the equality in ([3.1](https://arxiv.org/html/2602.02816v1#S3.E1 "Equation 3.1 ‣ Proposition 3.1 (Dynamic Programming Principle). ‣ 3.1 Dynamic Programming Principle ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), we will establish two inequalities. Let the right-hand side of ([3.1](https://arxiv.org/html/2602.02816v1#S3.E1 "Equation 3.1 ‣ Proposition 3.1 (Dynamic Programming Principle). ‣ 3.1 Dynamic Programming Principle ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) be denoted by RHS.

Part 1: Show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V(t,x,z)≥max{G(x),sup(π,c,b)𝔼t,x,z[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(cs,bs)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑uV(t+Δt,Xt+Δ​t,Zt+Δ​t)]}.\begin{split}V(t,x,z)\geq\max\Biggl\{G(x),\sup\_{(\pi,c,b)}\mathbb{E}\_{t,x,z}\biggl[&\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s},b\_{s})ds\\ &+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\biggr]\Biggr\}.\end{split} |  | (A.1) |

We write equation ([A.1](https://arxiv.org/html/2602.02816v1#A1.E1 "Equation A.1 ‣ Proof. ‣ A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) as V​(t,x,z)≥RHSV(t,x,z)\geq\text{RHS}. First, we show that V​(t,x,z)V(t,x,z) is greater than or equal to each term inside the max⁡(⋅,⋅)\max(\cdot,\cdot) operator.

1. 1.

   The strategy of stopping immediately at time τ=t\tau=t is admissible. This yields a value of G​(x)G(x). Since the value function is the supremum over all admissible strategies, it must be that V​(t,x,z)≥G​(x)V(t,x,z)\geq G(x).
2. 2.

   Next, consider an admissible strategy that applies an arbitrary control policy (π,c,b)(\pi,c,b) on the interval [t,t+Δ​t][t,t+\Delta t] and then proceeds optimally from time t+Δ​tt+\Delta t onwards. The value of this combined strategy is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼t,x,z[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(cs,bs)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑uV(t+Δt,Xt+Δ​t,Zt+Δ​t)].\begin{split}\mathbb{E}\_{t,x,z}\biggl[&\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s},b\_{s})ds\\ &\quad+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\biggr].\end{split} |  | (A.2) |

Because the value function V​(t,x,z)V(t,x,z) is the supremum over all admissible strategies, its value must be greater than or equal to the value of this specific strategy. This holds for any choice of (π,c,b)(\pi,c,b) on [t,t+Δ​t][t,t+\Delta t], and thus it must also hold for the supremum over all such choices. Therefore,

|  |  |  |
| --- | --- | --- |
|  | V​(t,x,z)≥sup(π,c,b)𝔼t,x,z​[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(cs,bs)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑u​V​(t+Δ​t,Xt+Δ​t,Zt+Δ​t)].\displaystyle V(t,x,z)\geq\sup\_{(\pi,c,b)}\mathbb{E}\_{t,x,z}\biggl[\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s},b\_{s})ds+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\biggr]. |  |

Since V​(t,x,z)V(t,x,z) is greater than or equal to both arguments of the max⁡(⋅,⋅)\max(\cdot,\cdot) operator, it must be greater than or equal to their maximum. Thus, we have established that V​(t,x,z)≥RHSV(t,x,z)\geq\text{RHS}.

Part 2: Show that V​(t,x,z)≤RHSV(t,x,z)\leq\text{RHS}. For any given ε>0\varepsilon>0, the definition of the value function guarantees the existence of an ε\varepsilon-optimal strategy (πε,cε,bε,τε)(\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon},\tau^{\varepsilon}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x,z)≤J​(t,x,z;πε,cε,bε,τε)+ε.\displaystyle V(t,x,z)\leq J(t,x,z;\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon},\tau^{\varepsilon})+\varepsilon. |  | (A.3) |

We consider two possibilities for the stopping time τε\tau^{\varepsilon}:

* 1.

  If τε=t\tau^{\varepsilon}=t, the strategy is to stop immediately, so

  |  |  |  |
  | --- | --- | --- |
  |  | J​(t,x,z;πε,cε,bε,t)=G​(x).J(t,x,z;\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon},t)=G(x). |  |

  Substituting this into ([A.3](https://arxiv.org/html/2602.02816v1#A1.E3 "Equation A.3 ‣ Proof. ‣ A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) gives
  V​(t,x,z)≤G​(x)+εV(t,x,z)\leq G(x)+\varepsilon.
  By definition, G​(x)≤RHSG(x)\leq\text{RHS}, which implies
  V​(t,x,z)≤RHS+εV(t,x,z)\leq\text{RHS}+\varepsilon.
* 2.

  If τε>t\tau^{\varepsilon}>t, we decompose the objective function. By the law of iterated expectations and by the definition of the value function, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | J\displaystyle J | (t,x,z;πε,cε,bε,τε)=𝔼t,x,z​[∫tτεe−∫ts(β+δu)​𝑑u​U​(csε,bsε)​𝑑s+e−∫tτε(β+δu)​𝑑u​G​(Xτε)]\displaystyle(t,x,z;\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon},\tau^{\varepsilon})=\mathbb{E}\_{t,x,z}\Biggl[\int\_{t}^{\tau^{\varepsilon}}e^{-\int\_{t}^{s}(\beta+\delta\_{u})\,du}U(c\_{s}^{\varepsilon},b\_{s}^{\varepsilon})\,ds+e^{-\int\_{t}^{\tau^{\varepsilon}}(\beta+\delta\_{u})\,du}G(X\_{\tau^{\varepsilon}})\Biggr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼t,x,z​[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(csε,bsε)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑u​J​(t+Δ​t,Xt+Δ​t,Zt+Δ​t;πε,cε,bε,τε)]\displaystyle=\mathbb{E}\_{t,x,z}\Biggl[\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})\,du}U(c\_{s}^{\varepsilon},b\_{s}^{\varepsilon})\,ds+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})\,du}J(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t};\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon},\tau^{\varepsilon})\Biggr] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤𝔼t,x,z​[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(csε,bsε)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑u​V​(t+Δ​t,Xt+Δ​t,Zt+Δ​t)].\displaystyle\leq\mathbb{E}\_{t,x,z}\Biggl[\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})\,du}U(c\_{s}^{\varepsilon},b\_{s}^{\varepsilon})\,ds+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})\,du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\Biggr]. |  | (A.4) |

The right-hand side of inequality ([A.4](https://arxiv.org/html/2602.02816v1#A1.E4 "Equation A.4 ‣ Proof. ‣ A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) is the expected value from following the specific policy
(πε,cε,bε)(\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon}) over the interval [t,t+Δ​t][t,t+\Delta t].
This value cannot exceed the supremum taken over all admissible policies on that interval. Therefore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t,x,z​[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(csε,bsε)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑u​V​(t+Δ​t,Xt+Δ​t,Zt+Δ​t)]≤sup(π,c,b)𝔼t,x,z​[∫tt+Δ​te−∫ts(β+δu)​𝑑u​U​(cs,bs)​𝑑s+e−∫tt+Δ​t(β+δu)​𝑑u​V​(t+Δ​t,Xt+Δ​t,Zt+Δ​t)]≤RHS.\displaystyle\begin{split}&\mathbb{E}\_{t,x,z}\Biggl[\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s}^{\varepsilon},b\_{s}^{\varepsilon})ds+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\Biggr]\\ &\quad\leq\sup\_{(\pi,c,b)}\mathbb{E}\_{t,x,z}\biggl[\int\_{t}^{t+\Delta t}e^{-\int\_{t}^{s}(\beta+\delta\_{u})du}U(c\_{s},b\_{s})ds+e^{-\int\_{t}^{t+\Delta t}(\beta+\delta\_{u})du}V(t+\Delta t,X\_{t+\Delta t},Z\_{t+\Delta t})\biggr]\\ &\quad\leq\text{RHS}.\end{split} | |  | (A.5) |

Combining ([A.3](https://arxiv.org/html/2602.02816v1#A1.E3 "Equation A.3 ‣ Proof. ‣ A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), ([A.4](https://arxiv.org/html/2602.02816v1#A1.E4 "Equation A.4 ‣ Proof. ‣ A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), and ([A.5](https://arxiv.org/html/2602.02816v1#A1.E5 "Equation A.5 ‣ Proof. ‣ A.1 Proof of Proposition 3.1: Dynamic Programming Principle (DPP) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), we find that

|  |  |  |
| --- | --- | --- |
|  | V​(t,x,z)≤J​(t,x,z;πε,cε,bε,τε)+ε≤RHS+ε.V(t,x,z)\leq J(t,x,z;\pi^{\varepsilon},c^{\varepsilon},b^{\varepsilon},\tau^{\varepsilon})+\varepsilon\leq\text{RHS}+\varepsilon. |  |

In both cases for τε\tau^{\varepsilon}, we conclude that V​(t,x,z)≤RHS+εV(t,x,z)\leq\text{RHS}+\varepsilon. Since this holds for any arbitrarily small ε>0\varepsilon>0, we must have V​(t,x,z)≤RHSV(t,x,z)\leq\text{RHS}. Combining the results from Part 1 and Part 2, we have proven the equality in ([3.1](https://arxiv.org/html/2602.02816v1#S3.E1 "Equation 3.1 ‣ Proposition 3.1 (Dynamic Programming Principle). ‣ 3.1 Dynamic Programming Principle ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")).
∎

### A.2 Proof of Theorem [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") (Value Function)

We analyze the pre-annuitization problem where the agent has not yet reached the optimal stopping boundary, i.e., y<y∗y<y^{\*}. In this continuation region, the value function V​(y)V(y) is greater than the annuitization value G​(y)G(y) and must satisfy the Hamilton-Jacobi-Bellman (HJB) equation. We analyze the problem by partitioning the continuation region based on the optimal labor supply b∗b^{\*}.

###### Proof.

The stationary value function V​(y)V(y) satisfies the HJB equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt​V​(y)=supp,κ,b[u1​(κ,b)+ℒ​V​(y)],\eta\_{t}V(y)=\sup\_{p,\kappa,b}\left[u\_{1}(\kappa,b)+\mathcal{L}V(y)\right], |  | (A.6) |

where u1​(κ,b)=(κ​(l¯−b)ψ)1−γ1−γu\_{1}(\kappa,b)=\frac{(\kappa(\bar{l}-b)^{\psi})^{1-\gamma}}{1-\gamma} and the generator is

|  |  |  |
| --- | --- | --- |
|  | ℒ​V​(y)=V′​(y)​[(r+ρ)​y+p​y​(μ−r)−κ​(1+ρ​y)+w​b]+12​V′′​(y)​σ2​p2​y2.\mathcal{L}V(y)=V^{\prime}(y)\left[(r+\rho)y+py(\mu-r)-\kappa(1+\rho y)+wb\right]+\frac{1}{2}V^{\prime\prime}(y)\sigma^{2}p^{2}y^{2}. |  |

Case I: y<y~y<\tilde{y} (Interior Labor Supply 0≤b∗<b¯0\leq b^{\*}<\bar{b}).

In this region, all controls are interior. We substitute the optimal portfolio p∗​(y)=−μ−rσ2​V′​(y)y​V′′​(y)p^{\*}(y)=-\frac{\mu-r}{\sigma^{2}}\frac{V^{\prime}(y)}{yV^{\prime\prime}(y)} into the HJB equation ([A.6](https://arxiv.org/html/2602.02816v1#A1.E6 "Equation A.6 ‣ Proof. ‣ A.2 Proof of Theorem 3.3 (Value Function) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) to get the maximized HJB for V​(y)=Vint​(y)V(y)=V\_{\mathrm{int}}(y)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt​Vint​(y)=u1​(κ∗,b∗)+Vint′​(y)​[(r+ρ)​y−κ∗​(1+ρ​y)+w​b∗]−12​(μ−rσ)2​(Vint′​(y))2Vint′′​(y).\eta\_{t}V\_{\mathrm{int}}(y)=u\_{1}(\kappa^{\*},b^{\*})+V^{\prime}\_{\mathrm{int}}(y)\left[(r+\rho)y-\kappa^{\*}(1+\rho y)+wb^{\*}\right]-\frac{1}{2}\left(\frac{\mu-r}{\sigma}\right)^{2}\frac{(V^{\prime}\_{\mathrm{int}}(y))^{2}}{V^{\prime\prime}\_{\mathrm{int}}(y)}. |  | (A.7) |

To solve this non-linear PDE, we use a dual method. We assume the optimal policy κ∗=Kint​(y)\kappa^{\*}=K\_{\mathrm{int}}(y) is invertible, with inverse y=Yint​(κ)y=Y\_{\mathrm{int}}(\kappa). The FOCs from Theorem [3.6](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem6 "Theorem 3.6 (Optimal Policies in the Continuation Region). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") relate the value function’s derivatives to the optimal controls

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vint′​(y)\displaystyle V^{\prime}\_{\mathrm{int}}(y) | =11+ρ​y​∂u1​(κ,b∗)∂κ,\displaystyle=\frac{1}{1+\rho y}\frac{\partial u\_{1}(\kappa,b^{\*})}{\partial\kappa}, |  | (A.8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vint′′​(y)\displaystyle V^{\prime\prime}\_{\mathrm{int}}(y) | =dd​y​(Vint′​(y)).\displaystyle=\frac{d}{dy}\left(V^{\prime}\_{\mathrm{int}}(y)\right). |  | (A.9) |

Substituting these back into the maximized HJB ([A.7](https://arxiv.org/html/2602.02816v1#A1.E7 "Equation A.7 ‣ Proof. ‣ A.2 Proof of Theorem 3.3 (Value Function) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) and differentiating the entire equation with respect to κ\kappa transforms the problem into a second-order linear ordinary differential equation (ODE) for the inverse function Yint​(κ)Y\_{\mathrm{int}}(\kappa)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜int​κ2​Yint′′​(κ)+ℬint​(κ,Y)​κ​Yint′​(κ)+𝒞int​(κ,Y)​Yint​(κ)=𝒟int​(κ,Y),\mathcal{A}\_{\mathrm{int}}\kappa^{2}Y^{\prime\prime}\_{\mathrm{int}}(\kappa)+\mathcal{B}\_{\mathrm{int}}(\kappa,Y)\kappa Y^{\prime}\_{\mathrm{int}}(\kappa)+\mathcal{C}\_{\mathrm{int}}(\kappa,Y)Y\_{\mathrm{int}}(\kappa)=\mathcal{D}\_{\mathrm{int}}(\kappa,Y), |  | (A.10) |

where the coefficients are functions of model parameters. The general solution is of the form Yint​(κ)=A1​κm1+A2​κm2+Yp​(κ)Y\_{\mathrm{int}}(\kappa)=A\_{1}\kappa^{m\_{1}}+A\_{2}\kappa^{m\_{2}}+Y\_{p}(\kappa). Economic boundary conditions typically ensure A1=0A\_{1}=0, leaving a solution dependent on one constant, A2A\_{2}.

Case II: y~≤y<y∗\tilde{y}\leq y<y^{\*} (Corner Labor Supply b=b¯b=\bar{b})

Here, b∗=b¯b^{\*}=\bar{b}. The maximized HJB equation for V​(y)=Vb¯​(y)V(y)=V\_{\bar{b}}(y) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt​Vb¯​(y)=u1​(κ∗,b¯)+Vb¯′​(y)​[(r+ρ)​y−κ∗​(1+ρ​y)+w​b¯]−12​(μ−rσ)2​(Vb¯′​(y))2Vb¯′′​(y).\eta\_{t}V\_{\bar{b}}(y)=u\_{1}(\kappa^{\*},\bar{b})+V^{\prime}\_{\bar{b}}(y)\left[(r+\rho)y-\kappa^{\*}(1+\rho y)+w\bar{b}\right]-\frac{1}{2}\left(\frac{\mu-r}{\sigma}\right)^{2}\frac{(V^{\prime}\_{\bar{b}}(y))^{2}}{V^{\prime\prime}\_{\bar{b}}(y)}. |  | (A.11) |

The procedure is analogous to Case I. We use the FOC for κ∗\kappa^{\*} with bb fixed at b¯\bar{b} to relate Vb¯′​(y)V^{\prime}\_{\bar{b}}(y) and Vb¯′′​(y)V^{\prime\prime}\_{\bar{b}}(y) to κ\kappa. This again transforms the HJB into a second-order linear ODE for the inverse function y=Yb¯​(κ)y=Y\_{\bar{b}}(\kappa)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜b¯​κ2​Yb¯′′​(κ)+ℬb¯​(κ,Y)​κ​Yb¯′​(κ)+𝒞b¯​(κ,Y)​Yb¯​(κ)=𝒟b¯​(κ,Y).\mathcal{A}\_{\bar{b}}\kappa^{2}Y^{\prime\prime}\_{\bar{b}}(\kappa)+\mathcal{B}\_{\bar{b}}(\kappa,Y)\kappa Y^{\prime}\_{\bar{b}}(\kappa)+\mathcal{C}\_{\bar{b}}(\kappa,Y)Y\_{\bar{b}}(\kappa)=\mathcal{D}\_{\bar{b}}(\kappa,Y). |  | (A.12) |

The general solution is Yb¯​(κ,B1,B2)=B1​κm1′+B2​κm2′+Yp,b¯​(κ)Y\_{\bar{b}}(\kappa,B\_{1},B\_{2})=B\_{1}\kappa^{m^{\prime}\_{1}}+B\_{2}\kappa^{m^{\prime}\_{2}}+Y\_{p,\bar{b}}(\kappa).

Annuitization Region: y≥y∗y\geq y^{\*}

In this region, it is optimal to stop. The value function is equal to the transformed annuitization value: V​(y)=G​(y)=(k​y)1−γηt​(1−γ)V(y)=G(y)=\frac{(ky)^{1-\gamma}}{\eta\_{t}(1-\gamma)}. The habit level ZZ is factored out via the homothetic transformation.

The constants of integration (A2,B1,B2A\_{2},B\_{1},B\_{2}) and the thresholds (y~,y∗\tilde{y},y^{\*}) are determined by imposing C2C^{2} continuity conditions at the boundaries y=y~y=\tilde{y} and y=y∗y=y^{\*}. This system of value-matching, smooth-pasting, and super-contact equations uniquely determines the constants and completes the proof.
∎

### A.3 Proof of Theorem [3.9](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem9 "Theorem 3.9 (Optimal Policies). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") (Optimal Policies)

This appendix provides the verification argument establishing that the candidate value function and policies characterized in Theorems [3.3](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem3 "Theorem 3.3 (Value Function). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") and [3.6](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem6 "Theorem 3.6 (Optimal Policies in the Continuation Region). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") are globally optimal and satisfy the Hamilton–Jacobi–Bellman variational inequality.

###### Proof.

The optimal policies are derived by applying the FOCs from Theorem [3.6](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem6 "Theorem 3.6 (Optimal Policies in the Continuation Region). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") to the value function V​(y)V(y) in each of the three regions defined by y~\tilde{y} and y∗y^{\*}.

1. 1.

   Optimal Investment pt∗p\_{t}^{\*} (Portfolio Weight):
   The FOC is p∗​(y)=−μ−rσ2​V′​(y)y​V′′​(y)p^{\*}(y)=-\frac{\mu-r}{\sigma^{2}}\frac{V^{\prime}(y)}{yV^{\prime\prime}(y)}.

   * •

     For y<y~y<\tilde{y}: pt∗=−μ−rσ2​Vint′​(y)y​Vint′′​(y)p\_{t}^{\*}=-\frac{\mu-r}{\sigma^{2}}\frac{V^{\prime}\_{\mathrm{int}}(y)}{yV^{\prime\prime}\_{\mathrm{int}}(y)}.
   * •

     For y~≤y<y∗\tilde{y}\leq y<y^{\*}: pt∗=−μ−rσ2​Vb¯′​(y)y​Vb¯′′​(y)p\_{t}^{\*}=-\frac{\mu-r}{\sigma^{2}}\frac{V^{\prime}\_{\bar{b}}(y)}{yV^{\prime\prime}\_{\bar{b}}(y)}.
   * •

     For y≥y∗y\geq y^{\*}: Here V​(y)=G​(y)=(k​y)1−γηt​(1−γ)V(y)=G(y)=\frac{(ky)^{1-\gamma}}{\eta\_{t}(1-\gamma)}. The derivatives are:

     |  |  |  |
     | --- | --- | --- |
     |  | G′​(y)=k1−γηt​y−γ,G′′​(y)=−γ​k1−γηt​y−γ−1.G^{\prime}(y)=\frac{k^{1-\gamma}}{\eta\_{t}}y^{-\gamma},\qquad G^{\prime\prime}(y)=-\frac{\gamma k^{1-\gamma}}{\eta\_{t}}y^{-\gamma-1}. |  |

     Substituting into the FOC for the portfolio weight gives a constant

     |  |  |  |
     | --- | --- | --- |
     |  | p∗​(y)=−μ−rσ2​G′​(y)y​G′′​(y)=−μ−rσ2​k1−γηt​y−γy​(−γ​k1−γηt​y−γ−1)=μ−rσ2​γ.p^{\*}(y)=-\frac{\mu-r}{\sigma^{2}}\frac{G^{\prime}(y)}{yG^{\prime\prime}(y)}=-\frac{\mu-r}{\sigma^{2}}\frac{\frac{k^{1-\gamma}}{\eta\_{t}}y^{-\gamma}}{y(-\frac{\gamma k^{1-\gamma}}{\eta\_{t}}y^{-\gamma-1})}=\frac{\mu-r}{\sigma^{2}\gamma}. |  |

     The total dollar amount in the risky asset is πt∗=pt∗​Xt=(μ−rσ2​γ)​yt​Zt\pi\_{t}^{\*}=p\_{t}^{\*}X\_{t}=\left(\frac{\mu-r}{\sigma^{2}\gamma}\right)y\_{t}Z\_{t}.
2. 2.

   Optimal Consumption-to-Habit Ratio κt∗\kappa\_{t}^{\*}:

   * •

     For y<y∗y<y^{\*}: The FOC is ∂u1∂κ=V′​(y)​(1+ρ​y)\frac{\partial u\_{1}}{\partial\kappa}=V^{\prime}(y)(1+\rho y). For our utility, the marginal utility is ∂u1∂κ=κ−γ​((l¯−b)ψ)1−γ\frac{\partial u\_{1}}{\partial\kappa}=\kappa^{-\gamma}((\bar{l}-b)^{\psi})^{1-\gamma}. Inverting this for κ∗\kappa^{\*} yields

     |  |  |  |
     | --- | --- | --- |
     |  | κ∗​(y)=(V′​(y)​(1+ρ​y)((l¯−b∗​(y))ψ)1−γ)−1/γ.\kappa^{\*}(y)=\left(\frac{V^{\prime}(y)(1+\rho y)}{((\bar{l}-b^{\*}(y))^{\psi})^{1-\gamma}}\right)^{-1/\gamma}. |  |

     Applying this to the VintV\_{\mathrm{int}} and Vb¯V\_{\bar{b}} regions confirms the results. The total consumption is ct∗=κt∗​Ztc\_{t}^{\*}=\kappa\_{t}^{\*}Z\_{t}.
   * •

     For y≥y∗y\geq y^{\*}: The agent is annuitized. The optimal consumption rule from a Merton-style problem is ct∗=k​Xtc\_{t}^{\*}=kX\_{t}. In our framework, this translates directly to the ratios: ct∗=κt∗​Ztc\_{t}^{\*}=\kappa\_{t}^{\*}Z\_{t} and Xt=yt​ZtX\_{t}=y\_{t}Z\_{t}. Therefore, κt∗​Zt=k​yt​Zt\kappa\_{t}^{\*}Z\_{t}=ky\_{t}Z\_{t}, which implies

     |  |  |  |
     | --- | --- | --- |
     |  | κt∗=k​yt.\kappa\_{t}^{\*}=ky\_{t}. |  |
3. 3.

   Optimal Labor Supply bt∗b\_{t}^{\*}:

   * •

     For y<y~y<\tilde{y}: Labor supply is interior, derived from the MRS condition. The explicit solution provided in the theorem arises from solving the system of FOCs for a utility function with specific properties relating consumption and leisure.
   * •

     For y~≤y<y∗\tilde{y}\leq y<y^{\*}: The constraint is binding, so bt∗=b¯b\_{t}^{\*}=\bar{b}.
   * •

     For y≥y∗y\geq y^{\*}: The agent is retired, so labor supply is zero, bt∗=0b\_{t}^{\*}=0.
4. 4.

   Optimal Annuitization Time τ∗\tau^{\*}: This is an optimal stopping problem. The agent chooses to stop working and annuitize their wealth when the state process yty\_{t} first reaches the optimal threshold y∗y^{\*}. This threshold is determined by the value-matching and smooth-pasting conditions, V​(y∗)=G​(y∗)V(y^{\*})=G(y^{\*}) and V′​(y∗)=G′​(y∗)V^{\prime}(y^{\*})=G^{\prime}(y^{\*}), ensuring an optimal transition. Therefore

   |  |  |  |
   | --- | --- | --- |
   |  | τ∗=inf{t≥0:yt≥y∗}.\tau^{\*}=\inf\{t\geq 0:y\_{t}\geq y^{\*}\}. |  |

This completes the detailed derivation of the optimal policies based on the value function structure.
∎

### A.4 Proof of Proposition [3.4](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem4 "Proposition 3.4 (Optimal Retirement Wealth Threshold). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") (Optimal Retirement Wealth Threshold y∗y^{\*})

###### Proof.

The optimal retirement wealth threshold y∗y^{\*} is determined by ensuring a smooth and optimal transition from the working phase (governed by Vb¯​(y)V\_{\bar{b}}(y)) to the annuitized phase (governed by G​(y)G(y)).

##### Boundary Conditions.

For the transition to be optimal, the value function must be C1C^{1} (continuously differentiable) across the boundary y∗y^{\*}. This imposes two conditions

1. 1.

   Value Matching (C0C^{0}): Vb¯​(y∗)=G​(y∗)V\_{\bar{b}}(y^{\*})=G(y^{\*})
2. 2.

   Smooth Pasting (C1C^{1}): Vb¯′​(y∗)=G′​(y∗)V^{\prime}\_{\bar{b}}(y^{\*})=G^{\prime}(y^{\*})

Optimality and C2C^{2} continuity also imply the super-contact condition Vb¯′′​(y∗)=G′′​(y∗)V^{\prime\prime}\_{\bar{b}}(y^{\*})=G^{\prime\prime}(y^{\*}).

##### The Maximized HJB Equation at the Boundary.

The maximized HJB equation for the region y~≤y<y∗\tilde{y}\leq y<y^{\*} must hold in the limit as y→y∗−y\to y^{\*-}. We evaluate the HJB at y=y∗y=y^{\*} and substitute the boundary conditions. The HJB is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt​Vb¯​(y∗)=u1​(κ∗,b¯)+Vb¯′​(y∗)​[(r+ρ)​y∗−κ∗​(1+ρ​y∗)+w​b¯]−12​θ2​(Vb¯′​(y∗))2Vb¯′′​(y∗),\eta\_{t}V\_{\bar{b}}(y^{\*})=u\_{1}(\kappa^{\*},\bar{b})+V^{\prime}\_{\bar{b}}(y^{\*})\left[(r+\rho)y^{\*}-\kappa^{\*}(1+\rho y^{\*})+w\bar{b}\right]-\frac{1}{2}\theta^{2}\frac{(V^{\prime}\_{\bar{b}}(y^{\*}))^{2}}{V^{\prime\prime}\_{\bar{b}}(y^{\*})}, |  | (A.13) |

where θ=(μ−r)/σ\theta=(\mu-r)/\sigma. The annuitization function G​(y)=(k​y)1−γηt​(1−γ)G(y)=\frac{(ky)^{1-\gamma}}{\eta\_{t}(1-\gamma)} and its derivatives at y∗y^{\*} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​(y∗)\displaystyle G(y^{\*}) | =(k​y∗)1−γηt​(1−γ),\displaystyle=\frac{(ky^{\*})^{1-\gamma}}{\eta\_{t}(1-\gamma)}, |  | (A.14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G′​(y∗)\displaystyle G^{\prime}(y^{\*}) | =k1−γηt​(y∗)−γ,\displaystyle=\frac{k^{1-\gamma}}{\eta\_{t}}(y^{\*})^{-\gamma}, |  | (A.15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G′′​(y∗)\displaystyle G^{\prime\prime}(y^{\*}) | =−γ​k1−γηt​(y∗)−γ−1.\displaystyle=-\gamma\frac{k^{1-\gamma}}{\eta\_{t}}(y^{\*})^{-\gamma-1}. |  | (A.16) |

The optimal consumption κ∗\kappa^{\*} at the boundary is determined by the FOC, using the smooth-pasting condition

|  |  |  |
| --- | --- | --- |
|  | ∂u1​(κ∗,b¯)∂κ=Vb¯′​(y∗)​(1+ρ​y∗)=G′​(y∗)​(1+ρ​y∗).\frac{\partial u\_{1}(\kappa^{\*},\bar{b})}{\partial\kappa}=V^{\prime}\_{\bar{b}}(y^{\*})(1+\rho y^{\*})=G^{\prime}(y^{\*})(1+\rho y^{\*}). |  |

By substituting Vb¯​(y∗)=G​(y∗)V\_{\bar{b}}(y^{\*})=G(y^{\*}), Vb¯′​(y∗)=G′​(y∗)V^{\prime}\_{\bar{b}}(y^{\*})=G^{\prime}(y^{\*}), Vb¯′′​(y∗)=G′′​(y∗)V^{\prime\prime}\_{\bar{b}}(y^{\*})=G^{\prime\prime}(y^{\*}), and the derived κ∗​(y∗)\kappa^{\*}(y^{\*}) into the HJB equation ([A.13](https://arxiv.org/html/2602.02816v1#A1.E13 "Equation A.13 ‣ The Maximized HJB Equation at the Boundary. ‣ A.4 Proof of Proposition 3.4 (Optimal Retirement Wealth Threshold 𝑦^∗) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")), the differential equation reduces to a single, non-linear algebraic equation. This equation provides one of the five constraints needed to solve for the system’s unknowns.
∎

### A.5 Proof of Proposition [3.5](https://arxiv.org/html/2602.02816v1#S3.Thmtheorem5 "Proposition 3.5 (Threshold for the Labor Constraint). ‣ 3.3 Dimensionality Reduction ‣ 3 Dynamic Programming and the HJB Variational Inequality ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization") (Labor Constraint Threshold y~\tilde{y})

###### Proof.

The threshold y~\tilde{y} marks the boundary between the interior labor region (VintV\_{\mathrm{int}}) and the corner labor region (Vb¯V\_{\bar{b}}). To ensure the overall value function is twice continuously differentiable (C2C^{2}), we must impose three continuity conditions at this boundary.

##### Boundary Conditions.

Let κ~\tilde{\kappa} be the consumption-to-habit ratio at the boundary y~\tilde{y}. The conditions are

1. 1.

   Value Matching (C0C^{0}): Vint​(y~)=Vb¯​(y~)V\_{\mathrm{int}}(\tilde{y})=V\_{\bar{b}}(\tilde{y})
2. 2.

   Smooth Pasting (C1C^{1}): Vint′​(y~)=Vb¯′​(y~)V^{\prime}\_{\mathrm{int}}(\tilde{y})=V^{\prime}\_{\bar{b}}(\tilde{y})
3. 3.

   Super-Contact (C2C^{2}): Vint′′​(y~)=Vb¯′′​(y~)V^{\prime\prime}\_{\mathrm{int}}(\tilde{y})=V^{\prime\prime}\_{\bar{b}}(\tilde{y})

These three equations form the first part of the complete system used to solve for the unknowns.

###### Remark A.1 (Characteristic Equations).

The characteristic equations arise from solving the second-order ordinary differential equations (ODEs) for the value function V​(y)V(y) in the continuation regions (y<y∗y<y^{\*}), as detailed in Appendix [A.2](https://arxiv.org/html/2602.02816v1#A1.SS2 "A.2 Proof of Theorem 3.3 (Value Function) ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"). Because the HJB equation and optimal controls are different for the interior labor region (VintV\_{\mathrm{int}}) and the corner labor region (Vb¯V\_{\bar{b}}), they each produce a distinct characteristic equation. These equations are more complex than the standard Merton [[1971](https://arxiv.org/html/2602.02816v1#bib.bib24)]’s form due to the state-dependent coefficients (e.g., the (1+ρ​y)(1+\rho y) term) in the HJB.

Nonetheless, each characteristic equation yields a set of distinct real roots (e.g., m1>0,m2<0m\_{1}>0,m\_{2}<0 for VintV\_{\mathrm{int}} and m1′>0,m2′<0m^{\prime}\_{1}>0,m^{\prime}\_{2}<0 for Vb¯V\_{\bar{b}}). The negative roots (m2,m2′m\_{2},m^{\prime}\_{2}) are particularly crucial for constructing the homogeneous solutions A2​ym2A\_{2}y^{m\_{2}} and B2​ym2′B\_{2}y^{m^{\prime}\_{2}} that satisfy the economic boundary conditions at y=0y=0.

∎

### A.6 System of Equations for Constants and Thresholds

The five unknowns of the free boundary problem– the integration constants A2,B1,B2A\_{2},B\_{1},B\_{2} and the thresholds y~,y∗\tilde{y},y^{\*}– are determined by solving the following system of five non-linear algebraic equations derived from the continuity conditions.

The general solutions for the value functions in the continuation regions are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vint​(y)\displaystyle V\_{\mathrm{int}}(y) | =A2​ym2+Vp,int​(y)\displaystyle=A\_{2}y^{m\_{2}}+V\_{p,\mathrm{int}}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vb¯​(y)\displaystyle V\_{\bar{b}}(y) | =B1​ym1′+B2​ym2′+Vp,b¯​(y)\displaystyle=B\_{1}y^{m^{\prime}\_{1}}+B\_{2}y^{m^{\prime}\_{2}}+V\_{p,\bar{b}}(y) |  |

where m2,m1′,m2′m\_{2},m^{\prime}\_{1},m^{\prime}\_{2} are the characteristic roots and Vp,int​(y),Vp,b¯​(y)V\_{p,\mathrm{int}}(y),V\_{p,\bar{b}}(y) are the particular solutions for the respective ODEs. Unlike simpler models without habit formation, the complexity of the particular solutions VpV\_{p} prevents an explicit algebraic derivation of the constants A2,B1,B2A\_{2},B\_{1},B\_{2}. The constants and thresholds are thus implicitly defined and solved for simultaneously.

##### Conditions at the Labor Constraint Boundary y~\tilde{y}.

The C2C^{2} continuity conditions at y=y~y=\tilde{y} provide the first three equations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A2​(y~)m2+Vp,int​(y~)\displaystyle A\_{2}(\tilde{y})^{m\_{2}}+V\_{p,\mathrm{int}}(\tilde{y}) | =B1​(y~)m1′+B2​(y~)m2′+Vp,b¯​(y~)\displaystyle=B\_{1}(\tilde{y})^{m^{\prime}\_{1}}+B\_{2}(\tilde{y})^{m^{\prime}\_{2}}+V\_{p,\bar{b}}(\tilde{y}) |  | (A.17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | m2​A2​(y~)m2−1+Vp,int′​(y~)\displaystyle m\_{2}A\_{2}(\tilde{y})^{m\_{2}-1}+V^{\prime}\_{p,\mathrm{int}}(\tilde{y}) | =m1′​B1​(y~)m1′−1+m2′​B2​(y~)m2′−1+Vp,b¯′​(y~)\displaystyle=m^{\prime}\_{1}B\_{1}(\tilde{y})^{m^{\prime}\_{1}-1}+m^{\prime}\_{2}B\_{2}(\tilde{y})^{m^{\prime}\_{2}-1}+V^{\prime}\_{p,\bar{b}}(\tilde{y}) |  | (A.18) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | m2​(m2−1)​A2​(y~)m2−2+Vp,int′′​(y~)\displaystyle m\_{2}(m\_{2}-1)A\_{2}(\tilde{y})^{m\_{2}-2}+V^{\prime\prime}\_{p,\mathrm{int}}(\tilde{y}) | =m1′​(m1′−1)​B1​(y~)m1′−2\displaystyle=m^{\prime}\_{1}(m^{\prime}\_{1}-1)B\_{1}(\tilde{y})^{m^{\prime}\_{1}-2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +m2′​(m2′−1)​B2​(y~)m2′−2+Vp,b¯′′​(y~)\displaystyle+m^{\prime}\_{2}(m^{\prime}\_{2}-1)B\_{2}(\tilde{y})^{m^{\prime}\_{2}-2}+V^{\prime\prime}\_{p,\bar{b}}(\tilde{y}) |  | (A.19) |

##### Conditions at the Annuitization Boundary y∗y^{\*}.

The C1C^{1} continuity conditions at y=y∗y=y^{\*} provide the final two equations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B1​(y∗)m1′+B2​(y∗)m2′+Vp,b¯​(y∗)\displaystyle B\_{1}(y^{\*})^{m^{\prime}\_{1}}+B\_{2}(y^{\*})^{m^{\prime}\_{2}}+V\_{p,\bar{b}}(y^{\*}) | =(k​y∗)1−γηt​(1−γ)\displaystyle=\frac{(ky^{\*})^{1-\gamma}}{\eta\_{t}(1-\gamma)} |  | (A.20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | m1′​B1​(y∗)m1′−1+m2′​B2​(y∗)m2′−1+Vp,b¯′​(y∗)\displaystyle m^{\prime}\_{1}B\_{1}(y^{\*})^{m^{\prime}\_{1}-1}+m^{\prime}\_{2}B\_{2}(y^{\*})^{m^{\prime}\_{2}-1}+V^{\prime}\_{p,\bar{b}}(y^{\*}) | =k1−γηt​(y∗)−γ\displaystyle=\frac{k^{1-\gamma}}{\eta\_{t}}(y^{\*})^{-\gamma} |  | (A.21) |

##### Solution.

The system of five non-linear equations ([A.17](https://arxiv.org/html/2602.02816v1#A1.E17 "Equation A.17 ‣ Conditions at the Labor Constraint Boundary 𝑦̃. ‣ A.6 System of Equations for Constants and Thresholds ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization"))-([A.21](https://arxiv.org/html/2602.02816v1#A1.E21 "Equation A.21 ‣ Conditions at the Annuitization Boundary 𝑦^∗. ‣ A.6 System of Equations for Constants and Thresholds ‣ Appendix A Appendix: Detailed Proofs of Theorems ‣ Habit Formation, Labor Supply, and the Dynamics of Retirement and Annuitization")) is solved numerically for the vector of unknowns (y~,y∗,A2,B1,B2)(\tilde{y},y^{\*},A\_{2},B\_{1},B\_{2}).