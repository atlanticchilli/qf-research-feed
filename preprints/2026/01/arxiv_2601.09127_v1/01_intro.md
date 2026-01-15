---
authors:
- Tomasz R. Bielecki
- Igor Cialenco
doc_id: arxiv:2601.09127v1
family_id: arxiv:2601.09127
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Robo-Advising in Motion: A Model Predictive Control Approach'
url_abs: http://arxiv.org/abs/2601.09127v1
url_html: https://arxiv.org/html/2601.09127v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tomasz R. Bielecki
Department of Applied Mathematics, Illinois Institute of Technology
  
    10 W 32nd Str, Building RE, Room 220, Chicago, IL 60616, USA
  
    Emails: <tbielecki@illinoistech.edu> (T. R. Bielecki), and <cialenco@illinoistech.edu> (I. Cialenco)
  
    URLs: <http://math.iit.edu/~bielecki> and <http://cialenco.com>
  
Igor Cialenco 11footnotemark: 1

( First circulated and this version: January 11, 2026
  
)

Abstract:

Robo-advisors (RAs) are automated portfolio management systems that complement traditional financial advisors by
offering lower fees and smaller initial investment requirements. While most existing RAs rely on static,
one-period allocation methods, we propose a dynamic, multi-period asset-allocation framework that leverages Model
Predictive Control (MPC) to generate suboptimal but practically effective strategies. Our approach combines a Hidden
Markov Model with Black–Litterman (BL) methodology to forecast asset returns and covariances, and incorporates
practically important constraints, including turnover limits, transaction costs, and target portfolio allocations.
We study two predominant optimality criteria in wealth management: dynamic mean–variance (MV) and dynamic
risk-budgeting (MRB). Numerical experiments demonstrate that MPC-based strategies consistently outperform myopic
approaches, with MV providing flexible and diversified portfolios, while MRB delivers smoother allocations less
sensitive to key parameters. These findings highlight the trade-offs between adaptability and stability in
practical robo-advising design.

Keywords:

robo advising, model predictive control, dynamic asset allocation, mean-variance optimization,
risk-budgeting, Black–Litterman model, Hidden Markov Model, wealth management, rolling horizon optimization

MSC2020:

Primary 91G10; Secondary 91G60

JEL:

Primary G11; Secondary G17

## 1 Introduction

Robo-advisors (RAs) are fully or semi-automated portfolio management systems designed for individual investors, complementing traditional human financial advisors by offering lower fees and requiring smaller initial investments. These systems are becoming increasingly prevalent and influential in the wealth and asset management industry. For a comprehensive review and analysis of various aspects of robo-advisors, we refer to the extensive literature, including the works of Beketov et al. [[BLW18](https://arxiv.org/html/2601.09127v1#bib.bibx7)], Rossi and Utkus [[RU20](https://arxiv.org/html/2601.09127v1#bib.bibx32)], D’Acunto and Rossi [[DR21](https://arxiv.org/html/2601.09127v1#bib.bibx15)], Helms et al. [[HHN21](https://arxiv.org/html/2601.09127v1#bib.bibx18)], Alsabah et al. [[ACRLS20](https://arxiv.org/html/2601.09127v1#bib.bibx2)], Capponi et al. [[CÓZ22](https://arxiv.org/html/2601.09127v1#bib.bibx13)] and the recent literature survey by Akhtar et al. [[AAL25](https://arxiv.org/html/2601.09127v1#bib.bibx1)].

The key components of any robo-advising system are its portfolio selection methodology (asset allocation or management) and the interface through which the investor’s risk–return profile is elicited. To the best of our knowledge, all currently operating RAs rely on static, one-period portfolio allocation frameworks; see Beketov et al. [[BLW18](https://arxiv.org/html/2601.09127v1#bib.bibx7)] for a discussion of this point.
While the elicitation of an investor’s risk–return profile is extensively studied in the behavioral finance literature, its implementation in robo-advising is constrained by strict regulatory requirements, and in practice is typically carried out through standardized questionnaires; for more details cf. [[CÓZ22](https://arxiv.org/html/2601.09127v1#bib.bibx13)] and reference therein.

In this work, we primarily focus on building an asset-allocation engine and consider several heterogeneous risk-return profiles representing standard investor types. We propose a dynamic (multi-period) framework for designing the asset-allocation engine of a robo-advisor. Motivated by insights from the broader literature on dynamic decision-making, we argue that a dynamic asset-management approach offers meaningful advantages over static (myopic) allocation methods in terms of overall portfolio performance.

Extending existing RA systems directly to a fully stochastic dynamic framework–whether in discrete or continuous time–is computationally infeasible. The main challenge lies in the fact that the underlying optimization criteria, together with practical constraints, lead to a time-inconsistent problem that cannot be efficiently solved over multiple periods. One approach to addressing such dynamic problems is to consider subgame-perfect (time-consistent) solutions (cf. [[BM14](https://arxiv.org/html/2601.09127v1#bib.bibx8)]), or alternatively to construct a simplified approximate formulation that yields a suboptimal yet practically effective dynamic strategy.
Subgame-perfect solutions remain computationally demanding and, by their very nature, depend on the investment horizon; moreover, they must be reconstructed from scratch whenever the investor updates their risk attitude, making them less suitable for large-scale applications such as robo-advisors. Moreover, subgame-perfect solutions assume that the investor’s risk–return profile is known for all future times, which makes the resulting allocations harder to interpret and less practical for large-scale applications like robo-advisors.

Our proposed suboptimal approach is rooted in Model Predictive Control (MPC), a methodology widely used in engineering for dynamic decision problems under uncertainty (stochastic control problems). Rather than seeking a globally optimal solution, the essence of MPC is to approximate a stochastic control problem through a sequence of deterministic problems, solving only for the next few steps and updating as new information becomes available. This also means that the investor’s risk–return profile needs to be known only over a short-term horizon, with the allocation updated dynamically at each step. MPC is particularly suitable for robo-advisors primarily because the optimization problems it requires are numerically fast and tractable, often taking the form of convex programs. A key ingredient of any MPC algorithm is the forecasting module. In our implementation, we combine a Hidden Markov Model (HMM) with elements of the Black-Litterman (BL) methodology to forecast mean returns and covariances for portfolio assets. The inclusion of a BL based component is inspired by Wealthfront, one of the earliest and most prominent robo-advisors, which uses BL estimates in its static asset-allocation engine. For background on HMM and BL methodologies, see, e.g., [[ZMZ09](https://arxiv.org/html/2601.09127v1#bib.bibx35)] and [[Meu08](https://arxiv.org/html/2601.09127v1#bib.bibx24)], respectively. Our numerical experiments show that this suboptimal MPC-based approach outperforms traditional myopic strategies.

We conduct our study of dynamic asset-allocation systems for RAs using two alternative optimality criteria: the dynamic mean–variance (MV) criterion and the dynamic risk-budgeting (MRB) criterion, which are among the predominant approaches in current wealth management. Unlike traditional utility-maximization frameworks, which are rarely applied in practical robo-advising, these criteria allow for straightforward and interpretable portfolio decisions. In our analysis, we also incorporate practically important constraints such as turnover limits, transaction costs, and target portfolio allocations to ensure realistic and implementable strategies.

The results indicate that the MPC-based suboptimal strategies consistently outperform myopic strategies, with particularly strong improvements under the MV criterion. In contrast to typical engineering applications, where MPC performance is highly sensitive to the key rolling-horizon parameter, we find that in our asset-allocation setup the results are much less sensitive, especially under the MRB criterion, where its inherent structure makes portfolio outcomes relatively stable across variations in this parameter.

The obtained results indicate that MPC-based suboptimal strategies consistently outperform myopic strategies, with particularly strong improvements under the MV criterion combined with BL framework by producing a more diversified and stable portfolios than classical estimated MV approaches. Nevertheless, MV with BL remains sensitive to noisy or rapidly changing risk profiles, making explicit turnover, transaction cost, and target portfolio constraints essential for stabilizing portfolio dynamics in practical robo-advising applications. In contrast, the MRB with strategy generates markedly smoother and more stable allocations across a wide range of parameters, including risk-aversion, transaction cost, and MPC horizon, reflecting its inherent robustness. While this stability reduces turnover, it also limits responsiveness to market forecasts, and soft transaction cost penalties are often ineffective, requiring hard constraints when trading activity must be controlled. Overall, these findings suggest that effective RA design should carefully align the choice of optimization criterion and structure of the imposed constraints.

The paper is organized as follows. In Section [2](https://arxiv.org/html/2601.09127v1#S2 "2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we review relevant background material on MPC. Section [3](https://arxiv.org/html/2601.09127v1#S3 "3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach") formulates SMPC problems tailored to the operations of RAs. Our approach for forecasting the conditional moments of asset returns is presented in Section [4](https://arxiv.org/html/2601.09127v1#S4 "4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). In Section [5.1](https://arxiv.org/html/2601.09127v1#S5.SS1 "5.1 Risk profiling ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we discuss the modeling of parameters related to the investor’s risk profile and trading constraints. Finally, in Section [6](https://arxiv.org/html/2601.09127v1#S6 "6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we illustrate the proposed robo-advising methodology through a numerical example based on market data. Concluding remarks are detailed in Section [7](https://arxiv.org/html/2601.09127v1#S7 "7 Concluding remarks ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

## 2 Preliminaries on Model Predictive Control

Model Predictive Control (MPC) is a methodology designed to provide sub-optimal, yet computationally efficient, solutions to a wide range of control problems. Numerical evidence widely demonstrates that the resulting loss of optimality is typically modest and represents an acceptable trade-off for the gain in computational efficiency. Extensive practical applications of MPC, particularly in engineering, demonstrated its strong empirical performance. To the best of our knowledge, there are currently no theoretical results that quantify the degree of sub-optimality of MPC.

Model Predictive Control (MPC) should be viewed as a general framework rather than a single, uniquely defined method. It admits a wide range of formulations and implementations, differing in modeling assumptions, objective functions, and constraints handling. We refer the reader to the literature for representative treatments and discussions; see, for example, [[Yan21](https://arxiv.org/html/2601.09127v1#bib.bibx34)], [[Hew20](https://arxiv.org/html/2601.09127v1#bib.bibx17)], [[RMD20](https://arxiv.org/html/2601.09127v1#bib.bibx30)], [[RL19](https://arxiv.org/html/2601.09127v1#bib.bibx29)], [[KC16](https://arxiv.org/html/2601.09127v1#bib.bibx20)], and references therein.

Here we present a tentative description of what can be considered Stochastic MPC (SMPC), which addresses stochastic control problems within the MPC framework. We need to stress though that the terminology “stochastic model predictive control” is not uniquely defined in the MPC universe. Following the existing literature, we focus on the discrete-time setting.

On a given probability space (Ω,ℱ,P)(\Omega,\mathcal{F},P), let us consider a prototypical discrete time controlled stochastic dynamical system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xτ+1=f​(Xτ,Uτ,ϵτ),τ=0,1,2,…,\displaystyle X\_{\tau+1}=f(X\_{\tau},U\_{\tau},\epsilon\_{\tau}),\ \tau=0,1,2,\ldots, |  | (2.1) |

where XX is a ℝn\mathbb{R}^{n}-valued state process, UU is a ℝm\mathbb{R}^{m}-valued control process, and ϵ\epsilon is a ℝk\mathbb{R}^{k}-valued driving, underlying random process. As is customary, we assume that additional constraints are imposed on the controls

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uτ∈𝒰τ,τ=0,1,2,…,\displaystyle U\_{\tau}\in\mathcal{U}\_{\tau},\ \tau=0,1,2,\ldots, |  | (2.2) |

where 𝒰τ=𝐔τ​(Xτ)⊂ℝm\mathcal{U}\_{\tau}=\mathbf{U}\_{\tau}(X\_{\tau})\subset\mathbb{R}^{m} for some measurable multifunction 𝐔τ\mathbf{U}\_{\tau}.

Fix a time horizon T>0T>0 and define a (running) optimization criterion

|  |  |  |
| --- | --- | --- |
|  | Jt​(X,U,T)=∑τ=tTF​(Xτ,Uτ),t=0,…,T,J\_{t}(X,U,T)=\sum\_{\tau=t}^{T}F(X\_{\tau},U\_{\tau}),\quad t=0,\ldots,T, |  |

where FF is an appropriate real-valued function. This criterion forms the basis of the objective that we aim to optimize within the MPC.

Let 𝔽=(ℱτ)τ=0,1,2,…\mathbb{F}=(\mathcal{F}\_{\tau})\_{\tau=0,1,2,...} denote some relevant filtration modeling the flow of information available to the controller, which is non-anticipative w.r.t. process ϵ\epsilon. Typically, ℱτ=σ(Xs,s=0,1,…,τ)\mathcal{F}\_{\tau}=\sigma(X\_{s},\,s=0,1,\ldots,\tau), but not necessarily - see Remark [3.1](https://arxiv.org/html/2601.09127v1#S3.Thmtheorem1 "Remark 3.1. ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). We write Yτ∈ℱtY\_{\tau}\in\mathcal{F}\_{t} to indicate that the random variable YτY\_{\tau} is ℱt\mathcal{F}\_{t}-measurable. Throughout, EE will denote the expectation under PP, and we put Eτ[⋅]:=E[⋅|ℱτ]E\_{\tau}[\cdot]:=E[\cdot\;|\;\mathcal{F}\_{\tau}]. Respectively, Var\operatorname{\mathrm{Var}} and Varτ\operatorname{\mathrm{Var}}\_{\tau} will denote the variance and conditional variance.

The classical exemplary stochastic control problem takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | V0:=supUτ∈𝒢τ,τ=0,1,2,…,T−1E​[J0​(X,U,T)|ℱ0],\displaystyle V\_{0}:=\sup\_{U\_{\tau}\in\mathcal{G}\_{\tau},\,\tau=0,1,2,...,T-1}E[J\_{0}(X,U,T)|\mathcal{F}\_{0}], |  | (2.3) |

subject to ([2.1](https://arxiv.org/html/2601.09127v1#S2.E1 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) and ([2.2](https://arxiv.org/html/2601.09127v1#S2.E2 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")).

Throughout, we assume that the necessary conditions are satisfied by the model primitives, such as measurability, and that all processes are adapted to 𝔽\mathbb{F}. We further assume the existence of an optimal control sequence U∗U^{\*} for the above problem, so that

|  |  |  |
| --- | --- | --- |
|  | V0=E​[J0​(X,U∗,T)|ℱ0].V\_{0}={E}\big[J\_{0}(X,U^{\*},T)\;|\;\mathcal{F}\_{0}\big]. |  |

We refer to [[BS78](https://arxiv.org/html/2601.09127v1#bib.bibx9)] for a general treatment of stochastic control problems in discrete time.

A well-founded theoretical way to solve the above problem is to use dynamic programming (DP), for problems that satisfy the dynamic programming principle, also called time consistent problems. As it is well documented though, practical application of dynamic programming is typically prohibited by the so called ”curse of dimensionality,” which leads to formidable computational difficulties. In case of problems that do not satisfy the dynamic programming principle, the dynamic programming will not work as a method for delivering the optimal solution.

A theoretically well-founded approach to solve the above problem is dynamic programming (DP), applicable to problems that satisfy the dynamic programming principle, also referred to as time-consistent problems. However, as widely documented, practical application of DP is often limited by the so-called “curse of dimensionality,” which results in formidable computational challenges. For time-inconsistent problems, the DP cannot be used in principle to obtain the optimal solution, and usually some other methods are employed such as sub-game perfect solutions, or adaptive change of the criteria.

MPC was introduced as a methodology to generate sub-optimal solutions to the above stochastic control problem that can be computed efficiently, either in cases where dynamic programming is inapplicable or where its application is hindered by the curse of dimensionality.

Next, we introduce the SMPC formulation for the problem ([2.1](https://arxiv.org/html/2601.09127v1#S2.E1 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))–([2.3](https://arxiv.org/html/2601.09127v1#S2.E3 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")), suitable for our robo-advising applications, and consider a receding-horizon approach, where the initial time and horizon advance sequentially. Specifically, one chooses a rolling horizon H>0H>0,111Typically, H≤TH\leq T. and for t=0,1,…,T−1,t=0,1,\ldots,T-1, one solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | supUτ∈𝒢t,τ=t,t+1,…,t+H−1∑τ=tt+H−1F^t​(Ut,…,Uτ),\displaystyle\sup\_{U\_{\tau}\in\mathcal{G}\_{t},\,\tau=t,t+1,...,t+H-1}\sum\_{\tau=t}^{t+H-1}\widehat{F}\_{t}(U\_{t},\ldots,U\_{\tau}), |  | (2.4) |

subject to ([2.1](https://arxiv.org/html/2601.09127v1#S2.E1 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) and ([2.2](https://arxiv.org/html/2601.09127v1#S2.E2 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")), where F^t​(Ut,…,Uτ)\widehat{F}\_{t}(U\_{t},\ldots,U\_{\tau}) is the prediction (or forecast) of F​(Xτ,Uτ)F(X\_{\tau},U\_{\tau}) based on the information carried by ℱt\mathcal{F}\_{t}. Thus, the problem ([2.4](https://arxiv.org/html/2601.09127v1#S2.E4 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) is essentially a deterministic and open-loop control problem in discrete time as all the controls UτU\_{\tau} are constrained to be measurable with respect to the initial information ℱt\mathcal{F}\_{t}. Once the optimal controls, say Ut,τ∗,τ=t,t+1,…,t+H−1,U^{\*}\_{t,\tau},\,\tau=t,t+1,...,t+H-1, are computed at time tt, only the control Ut,t∗U^{\*}\_{t,t} is implemented at time tt. Then, the process repeats at time t+1t+1, and so on. The model predictive controls generated in this way are

|  |  |  |
| --- | --- | --- |
|  | UτMPC:=Uτ,τ∗,τ=0,1,…,T−1.U^{\textrm{MPC}}\_{\tau}:=U^{\*}\_{\tau,\tau},\ \tau=0,1,\ldots,T-1. |  |

With additional structure imposed on F^t\widehat{F}\_{t}, such as convexity, the SMPC solution reduces to a sequence of deterministic optimization problems that are relatively easy to solve and can, in practice, be computed on the fly.

## 3 SMPC for Robo-Advisors

An RA, as an automated system, aims to manage a portfolio of financial assets either fully autonomously or semi-autonomously on behalf of the investor, with the objective of optimizing the investor’s risk–reward profile. This process typically involves periodic interactions between the RA (machine) and the investor, primarily to calibrate the risk–reward criterion in a way that best aligns with the investor’s preferences.

We propose to cast the RA’s automated decision-making within the SMPC framework.
There are three key components of such framework:

* •

  Risk-reward criterion, which in turn involves selection of a) investment horizon; b) investor’s risk profile; c) RA’s attitude towards transaction costs or turn-over. We consider two main criteria: the mean-variance criterion, and the mean-risk-budgeting criterion.
* •

  Forecasts related to the asset returns. We will use a combination of Hidden Markov Model and Black-Litterman methodologies for this purpose.
* •

  Constraints imposed on the composition and re-balancing of the asset portfolio. The main constraints we consider are the long-only positions, self-financing and turn-over limits.

We assume that the RA invests in a portfolio consisting of NN assets. We denote by π0\pi\_{0} the vector of holding proportions (portfolio weights) at time 0 (before re-balancing at time 0), and for τ=0,1,…\tau=0,1,\dots we denote by πτ+1\pi\_{\tau+1} the vector of holding proportions at time τ\tau after re-balancing. Thus, for τ=0,1,…\tau=0,1,\dots,

|  |  |  |
| --- | --- | --- |
|  | ∑i=1Nπτi=1.\sum\_{i=1}^{N}\pi\_{\tau}^{i}=1. |  |

Additionally, for τ=0,1,…\tau=0,1,\dots, we consider two trading constraints that are often used in practice:

* •

  The long only constraint, that is πτ≥0\pi\_{\tau}\geq 0.
* •

  The turnover constraint ‖πτ+1−πτ‖1=∑i=1N|πτ+1i−πτi|≤δ\|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}=\sum\_{i=1}^{N}|\pi^{i}\_{\tau+1}-\pi^{i}\_{\tau}|\leq\delta for some positive constant δ\delta.

We denote by rτ=(rτ1,…,rτN)r\_{\tau}=(r^{1}\_{\tau},\ldots,r^{N}\_{\tau}) the (a priori) random vector of returns on the NN assets between times τ\tau and τ+1\tau+1, τ=0,1,…\tau=0,1,\ldots\,. That is,

|  |  |  |
| --- | --- | --- |
|  | rτi=Pτ+1i−PτiPτi,r^{i}\_{\tau}=\frac{P^{i}\_{\tau+1}-P^{i}\_{\tau}}{P^{i}\_{\tau}}, |  |

where PτiP^{i}\_{\tau} and Pτ+1iP^{i}\_{\tau+1} are the prices of asset ii at time τ\tau and τ+1\tau+1, respectively.

We denote by 𝔽=(ℱτ,τ=0,1,…)\mathbb{F}=(\mathcal{F}\_{\tau},\ \tau=0,1,\ldots) the filtration given as: ℱ0={∅,Ω}\mathcal{F}\_{0}=\{\emptyset,\Omega\} and ℱτ=σ​(r0,…,rτ−1)\mathcal{F}\_{\tau}=\sigma(r\_{0},\ldots,r\_{\tau-1}) for τ=1,2,…\tau=1,2,\ldots.

Let WτW\_{\tau} denote the wealth of the portfolio as time τ=0,1,…\tau=0,1,\dots. Under the self-financing constraint we have

|  |  |  |
| --- | --- | --- |
|  | Wτ=∑i=1Nπτi​Pτi=∑i=1Nπτ+1i​Pτi.W\_{\tau}=\sum\_{i=1}^{N}{\pi}^{i}\_{\tau}P^{i}\_{\tau}=\sum\_{i=1}^{N}{\pi}^{i}\_{\tau+1}P^{i}\_{\tau}. |  |

In addition, if the trading is self-financing then the following relationship holds between return on the portfolio and the returns on the portfolio constituents

|  |  |  |
| --- | --- | --- |
|  | Wτ+1−WτWτ=∑i=1Nrτi​πτ+1i=rτ⊺​πτ+1.\frac{W\_{\tau+1}-W\_{\tau}}{W\_{\tau}}=\sum\_{i=1}^{N}r^{i}\_{\tau}\pi^{i}\_{\tau+1}=r\_{\tau}^{\intercal}\pi\_{\tau+1}. |  |

### 3.1 Mean-variance portfolio selection problem

One of the cornerstone risk-reward criteria used in financial markets is the classical mean-variance (MV) problem pioneered by Harry Markowitz, and later modified by Fisher Black and Robert Litterman. It is well-known that the stochastic mean-variance problems are time inconsistent, and do not satisfy the dynamic principles (cf. [[BM14](https://arxiv.org/html/2601.09127v1#bib.bibx8), [LN00](https://arxiv.org/html/2601.09127v1#bib.bibx22), [BCC21](https://arxiv.org/html/2601.09127v1#bib.bibx5)] for a comprehensive treatment). Moreover, for mean-variance problems with short-selling constraints does not have an explicit solution even in one-period time setup. Nevertheless, this criterion remains widely used by wealth managers, typically in a myopic setting, where optimization is performed at each time step using a one-period objective. In this work, we propose an RA that adopts a dynamic mean–variance criterion integrated with the Black–Litterman methodology within a SMPC framework.

For motivational purposes, we first consider a one-period investment problem defined over the interval from the initial time time τ=0\tau=0 and the terminal time T=τ+1=1T=\tau+1=1. Let π0\pi\_{0} be the ℱ0\mathcal{F}\_{0} measurable vector of portfolio weights at time 0 (before rebalancing at time 0), so that 𝟙⊺​π0=1\mathbbm{1}^{\intercal}\pi\_{0}=1, and let π1\pi\_{1} be a ℱ0\mathcal{F}\_{0} measurable vector of portfolio weights at time 11 (after rebalancing at time 0), so that 𝟙⊺​π1=1\mathbbm{1}^{\intercal}\pi\_{1}=1. Without loss of generality we assume that ℱ0\mathcal{F}\_{0} is trivial. The (random) return on the portfolio between times 0 and 11 is r0⊺​π1r\_{0}^{\intercal}\pi\_{1}. Note that π0\pi\_{0} and π1\pi\_{1} are deterministic here, and π1\pi\_{1} is chosen at time τ=0\tau=0, without knowledge of r0r\_{0}.

The the classical MV criteria amounts to

|  |  |  |
| --- | --- | --- |
|  | E0​[r0⊺​π1]−γ0​Var0⁡[r0⊺​π1],E\_{0}[r\_{0}^{\intercal}\pi\_{1}]-\gamma\_{0}\operatorname{\mathrm{Var}}\_{0}[r\_{0}^{\intercal}\pi\_{1}], |  |

for some constant γ0>0\gamma\_{0}>0, that quantifies the risk attitude of the investor at time τ=0\tau=0.

To account for trading costs, the first level modification of this criterion is

|  |  |  |
| --- | --- | --- |
|  | E0​[r0⊺​π1]−γ0​Var0⁡[r0⊺​π1]−η0​T​C​(π1−π0),E\_{0}[r\_{0}^{\intercal}\pi\_{1}]-\gamma\_{0}\operatorname{\mathrm{Var}}\_{0}[r\_{0}^{\intercal}\pi\_{1}]-\eta\_{0}TC\left(\pi\_{1}-\pi\_{0}\right), |  |

where T​CTC is a function representing trading costs,222The trading costs are comprehensively described in terms of a trading cost function, say T​CTC. The form of this function may vary between specific applications. and η0>0\eta\_{0}>0 is the trading-costs sensitivity factor.

Since E0​[r0⊺​π1]=E0​[r0]⊺​π1E\_{0}[r\_{0}^{\intercal}\pi\_{1}]=E\_{0}[r\_{0}]^{\intercal}\pi\_{1}, and Var0⁡[r0⊺​π1]=π1⊺​Σ0​π1,\operatorname{\mathrm{Var}}\_{0}[r\_{0}^{\intercal}\pi\_{1}]=\pi^{\intercal}\_{1}\Sigma\_{0}\pi\_{1},, with Σ0=Var0⁡[r0]\Sigma\_{0}=\operatorname{\mathrm{Var}}\_{0}[r\_{0}], the corresponding one-period MV asset management problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ1∈ℱ0(E0​[r0]⊺​π1−γ0​π1⊺​Σ0​π1−η0​T​C​(π1−π0)),\sup\_{\pi\_{1}\in\mathcal{F}\_{0}}\Big(E\_{0}[r\_{0}]^{\intercal}\pi\_{1}-\gamma\_{0}\pi^{\intercal}\_{1}\Sigma\_{0}\pi\_{1}-\eta\_{0}TC\left(\pi\_{1}-\pi\_{0}\right)\Big), |  | (3.1) |

subject to constraints on π1\pi\_{1}: π1≥0\pi\_{1}\geq 0, 𝟙⊺​π1=1\mathbbm{1}^{\intercal}\pi\_{1}=1, and ‖π1−π0‖1≤δ\|\pi\_{1}-\pi\_{0}\|\_{1}\leq\delta.

The generalization of the above single-period problem to the multi-period case is straightforward. For τ=0,1,…\tau=0,1,\ldots, let ℱτ\mathcal{F}\_{\tau} be the information used by an investor at time τ\tau to rebalance their portfolios from πτ\pi\_{\tau} to πτ+1\pi\_{\tau+1} at time τ\tau. Thus πτ,τ=0,1,…,\pi\_{\tau},\,\tau=0,1,\ldots, is a random process adapted to filtration 𝔽\mathbb{F}.

An important consideration needs to be given to the portfolio rebalancing frequency. In this paper we assume that portfolio can be rebalanced on a fixed set of deterministic dates. Denote the set of rebalancing dates staring at time τ=0\tau=0 as 𝐑​(0)\mathbf{R}(0). For example, if τ\tau is a daily time scale, and 𝐑​(0)={0,7,14,21,…}\mathbf{R}(0)=\{0,7,14,21,\ldots\} then rebalancing takes place every seven days. By 𝐍𝐑​(0)\mathbf{NR}(0) we denote the set of non-rebalancing dates starting at time τ=0\tau=0. In the example above 𝐍𝐑​(0)={1,2,3,4,5,6,8,9,10,…,13,15,…}\mathbf{NR}(0)=\{1,2,3,4,5,6,8,9,10,\ldots,13,15,\ldots\}.

The multi-period MV problem (referring to the portfolio returns) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπτ+1∈ℱτ,τ=0,…,T−1∑τ=0T−1(E0​[rτ⊺​πτ+1]−γ0​Var0⁡[rτ⊺​πτ+1]−η0​E0​[T​C​(πτ+1−πτ)]),\displaystyle\sup\_{\pi\_{\tau+1}\in\mathcal{F}\_{\tau},\,\tau=0,\ldots,T-1}\sum\_{\tau=0}^{T-1}\Big(E\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]-\gamma\_{0}\operatorname{\mathrm{Var}}\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]-\eta\_{0}E\_{0}[TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right)]\Big), |  | (3.2) |

where π0\pi\_{0} is given and satisfies 𝟙⊺​π0=1,π0≥0,\mathbbm{1}^{\intercal}\pi\_{0}=1,\ \pi\_{0}\geq 0, and subject to constraints on π1,…,πT\pi\_{1},\ldots,\pi\_{T},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1≥0, 1⊺​πτ+1=1,‖πτ+1−πτ‖1≤δ,τ=0,…,T−1,\displaystyle\pi\_{\tau+1}\geq 0,\ \mathbbm{1}^{\intercal}\pi\_{\tau+1}=1,\ \|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}\leq\delta,\ \tau=0,...,T-1, |  | (3.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1=πτ,τ∈𝐍𝐑​(0).\displaystyle\pi\_{\tau+1}=\pi\_{\tau},\ \tau\in\mathbf{NR}(0). |  | (3.4) |

Additional trading constraints, such as turn-over budget or target portfolio and we refer to [[BBD+17](https://arxiv.org/html/2601.09127v1#bib.bibx4)] for a comprehensive discussion; specifically, see Section 4.4 (the set 𝒲t\mathcal{W}\_{t} of holding constraints), Section 4.5 (the set 𝒵t\mathcal{Z}\_{t} of trading constraints), and Section 4.6 (soft constraints). These include a wide range of constraints and costs, many of which are also discussed in, for example, Roncalli [[Ron16](https://arxiv.org/html/2601.09127v1#bib.bibx31)]. In this work, we deliberately restrict attention to a limited but fundamental set of trading constraints, corresponding to those most commonly implemented in practical robo-advisor systems. In addition to turn-over constraint, in Section [5.2](https://arxiv.org/html/2601.09127v1#S5.SS2 "5.2 Allocation target constraints ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach") we also consider target portfolio constraint.

###### Remark 3.1.

Note that the problem ([3.2](https://arxiv.org/html/2601.09127v1#S3.E2 "In 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))-([3.4](https://arxiv.org/html/2601.09127v1#S3.E4 "In 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) can be written as ([2.3](https://arxiv.org/html/2601.09127v1#S2.E3 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")), by taking
ϵτ=rτ+1\epsilon\_{\tau}=r\_{\tau+1}, Uτ=πτ+1U\_{\tau}=\pi\_{\tau+1}, X0=r0X\_{0}=r\_{0},
f​(Xτ,Uτ,ϵτ)=ϵτf(X\_{\tau},U\_{\tau},\epsilon\_{\tau})=\epsilon\_{\tau},
𝒢τ=ℱτ,\mathcal{G}\_{\tau}=\mathcal{F}\_{\tau},

|  |  |  |
| --- | --- | --- |
|  | Fτ(Xτ,Uτ)=E0[Xτ⊺Uτ]−γ0Var0[Xτ⊺Uτ)]−η0TC(Uτ−Uτ−1),F\_{\tau}(X\_{\tau},U\_{\tau})=E\_{0}[X\_{\tau}^{\intercal}U\_{\tau}]-\gamma\_{0}\operatorname{\mathrm{Var}}\_{0}[X\_{\tau}^{\intercal}U\_{\tau})]-\eta\_{0}TC\left(U\_{\tau}-U\_{\tau-1}\right), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝐔τ​(Xτ)={Uτ≥0, 1⊺​Uτ=1,‖Uτ−Uτ−1‖1≤δ,Uτ=Uτ−1,τ∈𝐍𝐑​(0)},{\mathbf{U}}\_{\tau}(X\_{\tau})=\{U\_{\tau}\geq 0,\ \mathbbm{1}^{\intercal}U\_{\tau}=1,\ \|U\_{\tau}-U\_{\tau-1}\|\_{1}\leq\delta,\ U\_{\tau}=U\_{\tau-1},\ \tau\in\mathbf{NR}(0)\}, |  |

for τ=0,1,…​T−1,\tau=0,1,\ldots T-1, where U−1=π0U\_{-1}=\pi\_{0}.

#### 3.1.1 MV receding horizon SMPC

Assume that the RA has a methodology to predict or forest the returns and variance at each time instant, and we denote by r^τ|t\widehat{r}\_{\tau|t} the forecast of the mean of rτr\_{\tau}, and by Σ^τ|t\widehat{\Sigma}\_{\tau|t} the forecast of the variance-covariance matrix of rτr\_{\tau} based on the information available to the RA at time t≤τt\leq\tau. As mentioned earlier, the used forecasting methodologies is a key component in our framework, and we study it in Section [4](https://arxiv.org/html/2601.09127v1#S4 "4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

We fix an integer valued SMPC rolling horizon H>0H>0. The receding horizon SMPC corresponding to problem ([3.2](https://arxiv.org/html/2601.09127v1#S3.E2 "In 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))-([3.4](https://arxiv.org/html/2601.09127v1#S3.E4 "In 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) is then stated as follows:

Step A. Set t=min⁡𝐑​(0)t=\min\mathbf{R}(0) to be the smallest element of the set of rebalancing dates 𝐑​(0)\mathbf{R}(0). Go to Step B.

Step B. Choose γt\gamma\_{t} and ηt\eta\_{t}333We refer to Section [5.1](https://arxiv.org/html/2601.09127v1#S5.SS1 "5.1 Risk profiling ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach") for a discussion of the choice of γt\gamma\_{t} and ηt\eta\_{t}., and solve the following problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπτ+1∈ℱt,τ=t:t+H−1∑τ=tt+H−1(r^τ|t⊺​πτ+1−γt​πτ+1⊺​Σ^τ|t​πτ+1−ηt​T​C​(πτ+1−πτ)),\displaystyle\sup\_{\pi\_{\tau+1}\in\mathcal{F}\_{t},\,\tau=t:t+H-1}\sum\_{\tau=t}^{t+H-1}\Big(\widehat{r}\_{\tau|t}^{\intercal}\pi\_{\tau+1}-\gamma\_{t}\pi\_{\tau+1}^{\intercal}\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1}-\eta\_{t}TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right)\Big), |  | (3.5) |

where πt\pi\_{t} is given and satisfies 𝟙⊺​πt=1,πt≥0\mathbbm{1}^{\intercal}\pi\_{t}=1,\ \pi\_{t}\geq 0, and subject to constraints on πt+1,…,πt+H\pi\_{t+1},\ldots,\pi\_{t+H},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1≥0, 1⊺​πτ+1=1,‖πτ+1−πτ‖1≤δ,τ=t,…,t+H−1,\displaystyle\pi\_{\tau+1}\geq 0,\ \mathbbm{1}^{\intercal}\pi\_{\tau+1}=1,\ \|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}\leq\delta,\ \tau=t,...,t+H-1, |  | (3.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1=πτ,τ∈𝐍𝐑​(t),\displaystyle\pi\_{\tau+1}=\pi\_{\tau},\ \tau\in\mathbf{NR}(t), |  | (3.7) |

where 𝐍𝐑​(t)\mathbf{NR}(t) is the set of no-rebalancing dates consistent with 𝐍𝐑​(0)\mathbf{NR}(0) in the sense that 𝐍𝐑​(t)=𝐍𝐑​(0)∩𝐍𝐑​(t)\mathbf{NR}(t)=\mathbf{NR}(0)\cap\mathbf{NR}(t).

Denote by πτ+1|t∗,τ=t,…,t+H−1,\pi^{\*}\_{\tau+1|t},\ \tau=t,...,t+H-1, the optimal controls for problem ([3.5](https://arxiv.org/html/2601.09127v1#S3.E5 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))–([3.6](https://arxiv.org/html/2601.09127v1#S3.E6 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")). Define the model predictive control for time tt as

|  |  |  |
| --- | --- | --- |
|  | πt+1M​P​C:=πτ+1|t∗,\pi^{MPC}\_{t+1}:=\pi^{\*}\_{\tau+1|t}, |  |

and apply this control to the system at time tt. That is, chose your rebalanced portfolio at time tt according to πt+1M​P​C\pi^{MPC}\_{t+1}. Go to Step C.

Step C. Set t:=min⁡𝐑​(t+1)t:=\min\mathbf{R}(t+1). If t≤T−1t\leq T-1 then go to Step B. If t>T−1t>T-1 then stop.

If the rebalancing is done monthly, say every 30 days, then min⁡𝐑​(t+1)=t+30\min\mathbf{R}(t+1)=t+30. Of course, in applications a more adequate rebalancing tenor must be applied, consistent with the calendar of trading days.

We remark that similar to one-period problem, since it is required that πt+1,…,πt+H\pi\_{t+1},\ldots,\pi\_{t+H} are all ℱ𝐭\mathcal{F}\_{\mathbf{t}} measurable, the above SMPC procedure is a sequence of open-loop control problems. Moreover, if one takes the function T​CTC to be convex, then the control problems in Step B are (static) convex optimization problems are static convex optimization problems for which highly efficient off-the-shelf solvers are available.

Note that in the above SMPC the counterpart of F^t​(Ut,…,Uτ)\widehat{F}\_{t}(U\_{t},\ldots,U\_{\tau}) showing in ([2.4](https://arxiv.org/html/2601.09127v1#S2.E4 "In 2 Preliminaries on Model Predictive Control ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) is

|  |  |  |
| --- | --- | --- |
|  | r^τ|t⊺​πτ+1−γt​πτ+1⊺​Σ^τ|t​πτ+1−ηt​T​C​(πτ+1−πτ).\widehat{r}\_{\tau|t}^{\intercal}\pi\_{\tau+1}-\gamma\_{t}\pi\_{\tau+1}^{\intercal}\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1}-\eta\_{t}TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right). |  |

### 3.2 Mean-risk-budgeting (MRB) portfolio selection

Another widely studied approach to portfolio construction is risk budgeting, including its special case of risk parity, in which portfolio weights are determined so that each asset or asset class contributes a predetermined proportion of total portfolio risk; cf. [[Ron16](https://arxiv.org/html/2601.09127v1#bib.bibx31)]. We adapt this approach to the SMPC setting.

Let ρ\rho be a risk measure assessing the risk of portfolio πτ+1\pi\_{\tau+1}. Specifically, we take the standard deviation based risk measure

|  |  |  |
| --- | --- | --- |
|  | ρ​(πτ+1)=Var0⁡[rτ⊺​πτ+1].\rho(\pi\_{\tau+1})=\sqrt{\operatorname{\mathrm{Var}}\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]}. |  |

It is well known that this risk measure satisfies the Euler risk allocation principle, under which the contribution of the ii-th asset to the total aggregated risk is given by

|  |  |  |
| --- | --- | --- |
|  | ℛ​𝒞τi=πτ+1i​∂iρ​(πτ+1).{\mathcal{RC}}^{i}\_{\tau}=\pi\_{\tau+1}^{i}\partial\_{i}\rho(\pi\_{\tau+1}). |  |

In the risk budgeting paradigm, the risk contributions are required to match prescribed proportions; thus, for each asset i=1,…,Ni=1,\ldots,N, we aim to achieve

|  |  |  |
| --- | --- | --- |
|  | ℛ​𝒞τi=bi​ρ​(πτ+1)=bi​Var0⁡[rτ⊺​πτ+1],{\mathcal{RC}}^{i}\_{\tau}=b\_{i}\rho(\pi\_{\tau+1})=b\_{i}\sqrt{\operatorname{\mathrm{Var}}\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]}, |  |

or, equivalently,

|  |  |  |
| --- | --- | --- |
|  | ℳ​ℛ​ℬτi:=πτ+1i​∂iρ​(πτ+1)Var0⁡[rτ⊺​πτ+1]=bi,{\mathcal{MRB}}^{i}\_{\tau}:=\frac{\pi\_{\tau+1}^{i}\partial\_{i}\rho(\pi\_{\tau+1})}{\sqrt{\operatorname{\mathrm{Var}}\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]}}=b\_{i}, |  |

where bi>0b\_{i}>0 are given and such that ∑i=1Nbi=1\sum\_{i=1}^{N}b\_{i}=1.

###### Remark 3.2.

(i) By analogy to the mean-variance criteria, we propose to parameterize the risk-budgeting weights bib\_{i} by a risk attitude parameter γR\gamma\_{R} as follows.
Divide the assets in two classes by their riskiness, e.g. bonds and equity. Denote by NBN\_{B} the number of assets in the first class, and assign equal risk-budget weights bi=γR/(NB​(1+γR))b\_{i}=\gamma\_{R}/(N\_{B}(1+\gamma\_{R})) to all assets in the first class, and correspondingly, bi=1/((N−NB)​(1+γR))b\_{i}=1/((N-N\_{B})(1+\gamma\_{R})) for the assets in the second class. Thus if the second class will contain riskier assets, then a larger γR\gamma\_{R} will budget smaller weight on the risky assets, and thus indeed the coefficient γR\gamma\_{R} plays the role of the attitude-aversion or risk-tolerance coefficient of the investor. We use this approach in defining the risk-budgeting weights bib\_{i} in Section [6](https://arxiv.org/html/2601.09127v1#S6 "6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), and show how γR\gamma\_{R} changes the structure of the portfolio and its characteristics.

By similarity, assets may be partitioned into several classes, with weights assigned at the class level and equal weights within each class.

(ii)
A special case of the risk-budgeting method, the so called risk parity paradigm, is to assign equal risk weights to all assets, that is for each i=1,…,N,i=1,\ldots,N,

|  |  |  |
| --- | --- | --- |
|  | πτ+1i​∂iρ​(πτ+1)Var0⁡[rτ⊺​πτ+1]=1N.\frac{\pi\_{\tau+1}^{i}\partial\_{i}\rho(\pi\_{\tau+1})}{\sqrt{\operatorname{\mathrm{Var}}\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]}}=\frac{1}{N}. |  |

In particular, note that γR=(N−NB)/NB\gamma\_{R}=(N-N\_{B})/N\_{B} corresponds to the risk-parity case.
∎

The multi-period MRB problem (referring to the portfolio returns) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπτ+1∈ℱτ,τ=0,…,T−1∑τ=0T−1(E0​[rτ⊺​πτ+1]−ϕτ​∑i=1N(ℳ​ℛ​ℬτi−bi)2−ητ​E0​[T​C​(πτ+1−πτ)]),\displaystyle\sup\_{\pi\_{\tau+1}\in\mathcal{F}\_{\tau},\,\tau=0,\ldots,T-1}\sum\_{\tau=0}^{T-1}\Big(E\_{0}[r\_{\tau}^{\intercal}\pi\_{\tau+1}]-{\phi\_{\tau}}\sum\_{i=1}^{N}({\mathcal{MRB}}^{i}\_{\tau}-b\_{i})^{2}-\eta\_{\tau}E\_{0}[TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right)]\Big), |  | (3.8) |

where π0\pi\_{0} is given and satisfies
𝟙⊺​π0=1,π0≥0,\mathbbm{1}^{\intercal}\pi\_{0}=1,\ \pi\_{0}\geq 0, and subject constraints on π1,…,πT\pi\_{1},\ldots,\pi\_{T},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1≥0, 1⊺​πτ+1=1,‖πτ+1−πτ‖1≤δ,τ=0,…,T−1,\displaystyle\pi\_{\tau+1}\geq 0,\ \mathbbm{1}^{\intercal}\pi\_{\tau+1}=1,\ \|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}\leq\delta,\ \tau=0,...,T-1, |  | (3.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1=πτ,τ∈𝐍𝐑​(0).\displaystyle\pi\_{\tau+1}=\pi\_{\tau},\ \tau\in\mathbf{NR}(0). |  | (3.10) |

We emphasis that while the mean–variance optimization balances expected return against overall portfolio risk (measured as variance), the risk-budgeting allocates portfolio weights so that each asset contributes proportionally to total risk. The coefficient ϕτ\phi\_{\tau}, called the risk-budgeting sensitivity coefficient, is not directly tied to the investor’s risk profile; rather, it quantifies the degree to which the risk-budgeting allocation is enforced.

#### 3.2.1 MRB receding horizon SMPC

Let ρ^​(πτ+1|t)\widehat{\rho}(\pi\_{\tau+1}|t) be a forecasted value of the risk measure assessing the risk of portfolio πτ+1\pi\_{\tau+1}, based on information in ℱt\mathcal{F}\_{t}. Specifically, postulating that πτ+1∈ℱt\pi\_{\tau+1}\in\mathcal{F}\_{t}, we take ρ^​(πτ+1|t)=πτ+1⊺​Σ^τ|t​πτ+1\widehat{\rho}(\pi\_{\tau+1}|t)=\sqrt{\pi^{\intercal}\_{\tau+1}\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1}}. Consequently, the forecasted Euler contribution of the ii-th asset to the total risk is given as

|  |  |  |
| --- | --- | --- |
|  | ℛ​𝒞^τ|ti=(πτ+1)i​(Σ^τ|t​πτ+1)iπτ+1⊺​Σ^τ|t​πτ+1.\widehat{\mathcal{RC}}^{i}\_{\tau|t}=\frac{(\pi\_{\tau+1})^{i}(\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1})^{i}}{\sqrt{\pi^{\intercal}\_{\tau+1}\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1}}}. |  |

Accordingly, the forecasted risk-budgeting term is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​ℛ​ℬ^τ|ti=(πτ+1)i​(Σ^τ|t​πτ+1)iπτ+1⊺​Σ^τ|t​πτ+1=πτ+1⊺​Σ^τ|t(i)​πτ+1πτ+1⊺​Σ^τ|t​πτ+1,\widehat{\mathcal{MRB}}^{i}\_{\tau|t}=\frac{(\pi\_{\tau+1})^{i}(\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1})^{i}}{\pi^{\intercal}\_{\tau+1}\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1}}=\frac{\pi\_{\tau+1}^{\intercal}\widehat{\Sigma}^{(i)}\_{\tau|t}\pi\_{\tau+1}}{\pi^{\intercal}\_{\tau+1}\widehat{\Sigma}\_{\tau|t}\pi\_{\tau+1}}, |  | (3.11) |

where as before the super index ii indicates the ii-th coordinate of a vector, and where Στ|t(i)\Sigma^{(i)}\_{\tau|t} is the matrix obtained from Στ|t\Sigma\_{\tau|t} by leaving the ii-th row intact and replacing all other elements in Στ|t\Sigma\_{\tau|t} by zeros.

The time tt optimization problem becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπτ∈ℱt,τ=t+1,…,t+H∑τ=tt+H−1(r^τ|t⊺​(πτ+1)−ϕt​∑i=1N(ℳ​ℛ​ℬ^τ|ti−bi)2−ηt​T​C​(πτ+1−πτ)),\displaystyle\sup\_{\pi\_{\tau}\in\mathcal{F}\_{t},\,\tau=t+1,\ldots,t+H}\sum\_{\tau=t}^{t+H-1}\Big(\widehat{r}\_{\tau|t}^{\intercal}(\pi\_{\tau+1})-\phi\_{t}\sum\_{i=1}^{N}(\widehat{\mathcal{MRB}}^{i}\_{\tau|t}-b\_{i})^{2}-\eta\_{t}TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right)\Big), |  | (3.12) |

subject to the same constraints ([3.6](https://arxiv.org/html/2601.09127v1#S3.E6 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))-([3.7](https://arxiv.org/html/2601.09127v1#S3.E7 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")).

The MBR receding horizon SMPC procedure follows the same steps as in MV case detailed in Section [3.1.1](https://arxiv.org/html/2601.09127v1#S3.SS1.SSS1 "3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), with ([3.5](https://arxiv.org/html/2601.09127v1#S3.E5 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) replaced by ([3.12](https://arxiv.org/html/2601.09127v1#S3.E12 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")).

#### 3.2.2 Convex approximation to the MRB criterion

The criterion in ([3.12](https://arxiv.org/html/2601.09127v1#S3.E12 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) is generally non-convex. To enable efficient numerical solution, following [[LUM21](https://arxiv.org/html/2601.09127v1#bib.bibx23)], we introduce a convex approximation of this criterion, which retains the essential features of ([3.12](https://arxiv.org/html/2601.09127v1#S3.E12 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) while allowing for tractable optimization.

Towards this end, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | dτ|t,i​(πτ+1)\displaystyle d\_{\tau|t,i}(\pi\_{\tau+1}) | :=ℳ​ℛ​ℬ^τ|ti−bi,\displaystyle:=\widehat{\mathcal{MRB}}^{i}\_{\tau|t}-b\_{i}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | dτ|t​(πτ+1)\displaystyle d\_{\tau|t}(\pi\_{\tau+1}) | :=[dτ|t,1​(πτ+1),…,dτ|t,N​(πτ+1)]⊺,\displaystyle:=[d\_{\tau|t,1}(\pi\_{\tau+1}),\ldots,d\_{\tau|t,N}(\pi\_{\tau+1})]^{\intercal}, |  |

and we proceed according to the following recursion:
  
Iteration k=0k=0. Initialize an arbitrary allocation π0=(πτ0,τ=t+1,…,t+H)\pi^{0}=(\pi^{0}\_{\tau},\,\tau=t+1,\ldots,t+H), and fix ρ0=[0,1]\rho^{0}=[0,1] and a tolerance t​o​l>0tol>0.

Iteration kk.
For any iteration k=0,1,…k=0,1,\ldots we expand dτ|t,i​(πτ+1)d\_{\tau|t,i}(\pi\_{\tau+1}) around πk\pi^{k}:

|  |  |  |
| --- | --- | --- |
|  | dτ|t,i​(πτ+1)≈dτ|t,i​(πτ+1k)+(∇dτ|t,i​(πτ+1k))T​(πτ+1−πτ+1k),d\_{\tau|t,i}(\pi\_{\tau+1})\approx d\_{\tau|t,i}(\pi^{k}\_{\tau+1})+\left(\nabla d\_{\tau|t,i}(\pi^{k}\_{\tau+1})\right)^{T}\left(\pi\_{\tau+1}-\pi^{k}\_{\tau+1}\right), |  |

where ∇dτ|t,i\nabla d\_{\tau|t,i} is the gradient. The convex approximation to the criterion ([3.12](https://arxiv.org/html/2601.09127v1#S3.E12 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπτ∈ℱt,τ=t+1,…,t+H\displaystyle\sup\_{\pi\_{\tau}\in\mathcal{F}\_{t},\,\tau=t+1,\ldots,t+H} | ∑τ=tt+H−1[r^τ|t⊺πτ+1−ϕt{∑i=1N(dτ|t,i(πτ+1k)+(∇dτ|t,i(πτ+1k))T(πτ+1−πτ+1k))2\displaystyle\sum\_{\tau=t}^{t+H-1}\Bigg[\widehat{r}\_{\tau|t}^{\intercal}\pi\_{\tau+1}-\phi\_{t}\Bigg\{\sum\_{i=1}^{N}\Bigg(d\_{\tau|t,i}(\pi^{k}\_{\tau+1})+\left(\nabla d\_{\tau|t,i}(\pi^{k}\_{\tau+1})\right)^{T}\left(\pi\_{\tau+1}-\pi^{k}\_{\tau+1}\right)\Bigg)^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +κτ2∥πτ+1−πτ+1k∥22}−ηtTC(πτ+1−πτ)],\displaystyle\qquad\qquad+\frac{\kappa\_{\tau}}{2}\|\pi\_{\tau+1}-\pi^{k}\_{\tau+1}\|^{2}\_{2}\Bigg\}-\eta\_{t}TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right)\Bigg], |  | (3.13) |

where κτ2​‖πτ+1−πτ+1k‖22\frac{\kappa\_{\tau}}{2}\|\pi\_{\tau+1}-\pi^{k}\_{\tau+1}\|^{2}\_{2} is a regularization term with some κτ>0\kappa\_{\tau}>0, and where we take
T​CTC to be convex, e.g. T​C​(πτ+1−πτ)=‖πτ+1−πτ‖1TC\left(\pi\_{\tau+1}-\pi\_{\tau}\right)=\|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1} and see Section [5.3](https://arxiv.org/html/2601.09127v1#S5.SS3 "5.3 Transaction costs ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

We will now proceed to rewrite the criterion in ([3.13](https://arxiv.org/html/2601.09127v1#S3.E13 "In 3.2.2 Convex approximation to the MRB criterion ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) in a more convenient way, for which we note that

|  |  |  |
| --- | --- | --- |
|  | ∑i=1N(dτ|t,i​(πτ+1k)+(∇dτ|t,i​(πτ+1k))T​(πτ+1−πτ+1k))2+κτ2​‖πτ+1−πτ+1k‖22\displaystyle\sum\_{i=1}^{N}\left(d\_{\tau|t,i}(\pi^{k}\_{\tau+1})+\left(\nabla d\_{\tau|t,i}(\pi^{k}\_{\tau+1})\right)^{T}\left(\pi\_{\tau+1}-\pi^{k}\_{\tau+1}\right)\right)^{2}+\frac{\kappa\_{\tau}}{2}\|\pi\_{\tau+1}-\pi^{k}\_{\tau+1}\|^{2}\_{2} |  |
|  |  |  |
| --- | --- | --- |
|  | =12​π⊺​(τ+1)​Qτ+1|tk​πτ+1+π⊺​(τ+1)​qτ+1|tk+constant,\displaystyle\qquad\qquad=\frac{1}{2}\pi^{\intercal}(\tau+1)Q^{k}\_{\tau+1|t}\pi\_{\tau+1}+\pi^{\intercal}(\tau+1)q^{k}\_{\tau+1|t}+\textrm{constant}, |  |

where (cf. [[LUM21](https://arxiv.org/html/2601.09127v1#bib.bibx23)], Section 4.2.1)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qτ+1|tk\displaystyle Q^{k}\_{\tau+1|t} | =2​(Aτ+1|tk)⊺​Aτ+1|tk+κτ​I,\displaystyle=2(A^{k}\_{\tau+1|t})^{\intercal}A^{k}\_{\tau+1|t}+\kappa\_{\tau}I, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | qτ+1|tk\displaystyle q^{k}\_{\tau+1|t} | =2​(Aτ+1|tk)⊺​dτ|t​(πτ+1k)−Qτ+1|tk​πτ+1k,\displaystyle=2(A^{k}\_{\tau+1|t})^{\intercal}d\_{\tau|t}(\pi^{k}\_{\tau+1})-Q^{k}\_{\tau+1|t}\pi^{k}\_{\tau+1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Aτ+1|tk\displaystyle A^{k}\_{\tau+1|t} | =[∇dτ|t,1​(πτ+1k),…,∇dτ|t,N​(πτ+1k)]⊺\displaystyle=[\nabla d\_{\tau|t,1}(\pi^{k}\_{\tau+1}),\ldots,\nabla d\_{\tau|t,N}(\pi^{k}\_{\tau+1})]^{\intercal} |  |

|  |  |  |
| --- | --- | --- |
|  | ∇dτ|t,i​(πτ+1k)=(πτ+1k)⊺​Σ^τ|t​πτ+1k​(Σ^τ|t(i)+(Σ^τ|t(i))⊺)​πτ+1k((πτ+1k)⊺​Σ^τ|t​πτ+1k)2\displaystyle\nabla d\_{\tau|t,i}(\pi^{k}\_{\tau+1})=\frac{(\pi^{k}\_{\tau+1})^{\intercal}\widehat{\Sigma}\_{\tau|t}\pi^{k}\_{\tau+1}\left(\widehat{\Sigma}^{(i)}\_{\tau|t}+\left(\widehat{\Sigma}^{(i)}\_{\tau|t}\right)^{\intercal}\right)\pi^{k}\_{\tau+1}}{\left((\pi^{k}\_{\tau+1})^{\intercal}\widehat{\Sigma}\_{\tau|t}\pi^{k}\_{\tau+1}\right)^{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | −2​(πτ+1k)⊺​Σ^τ|t(i)​πτ+1k​Σ^τ|t​πτ+1k((πτ+1k)⊺​Σ^τ|t​πτ+1k)2,\displaystyle-2\frac{(\pi^{k}\_{\tau+1})^{\intercal}\widehat{\Sigma}^{(i)}\_{\tau|t}\pi^{k}\_{\tau+1}\widehat{\Sigma}\_{\tau|t}\pi^{k}\_{\tau+1}}{\left((\pi^{k}\_{\tau+1})^{\intercal}\widehat{\Sigma}\_{\tau|t}\pi^{k}\_{\tau+1}\right)^{2}}, |  |

and where Σ^τ|t(i)\widehat{\Sigma}^{(i)}\_{\tau|t} is defined right below ([3.11](https://arxiv.org/html/2601.09127v1#S3.E11 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))

Now, restate the problem ([3.12](https://arxiv.org/html/2601.09127v1#S3.E12 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supπτ∈ℱt,τ=t+1,…,t+H\displaystyle\sup\_{\pi\_{\tau}\in\mathcal{F}\_{t},\,\tau=t+1,\ldots,t+H} | ∑τ=tt+H−1−ϕt​(12​πτ+1⊺​Qτ+1|tk​πτ+1+πτ+1⊺​qτ+1|tk)\displaystyle\sum\_{\tau=t}^{t+H-1}-\phi\_{t}\Big(\frac{1}{2}\pi^{\intercal}\_{\tau+1}Q^{k}\_{\tau+1|t}\pi\_{\tau+1}+\pi^{\intercal}\_{\tau+1}q^{k}\_{\tau+1|t}\Big) |  | (3.14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −ηt​‖πτ+1−πτ‖1+πτ+1⊺​r^τ|t,\displaystyle-\eta\_{t}\|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}+\pi^{\intercal}\_{\tau+1}\widehat{r}\_{\tau|t}, |  |

subject to constraints on πt+1,…,πt+H\pi\_{t+1},\ldots,\pi\_{t+H}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1≥0, 1⊺​πτ+1=1,‖πτ+1−πτ‖1≤δ,τ=t,…,t+H−1,\displaystyle\pi\_{\tau+1}\geq 0,\ \mathbbm{1}^{\intercal}\pi\_{\tau+1}=1,\ \|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}\leq\delta,\ \tau=t,...,t+H-1, |  | (3.15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | πτ+1=πτ,τ∈𝐍𝐑​(t).\displaystyle\pi\_{\tau+1}=\pi\_{\tau},\ \tau\in\mathbf{NR}(t). |  | (3.16) |

Denote by πτ|t∗,k,τ=t+1,…,t+H,\pi^{\*,k}\_{\tau|t},\ \tau=t+1,...,t+H, the optimal controls for problem ([3.14](https://arxiv.org/html/2601.09127v1#S3.E14 "In 3.2.2 Convex approximation to the MRB criterion ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))– ([3.16](https://arxiv.org/html/2601.09127v1#S3.E16 "In 3.2.2 Convex approximation to the MRB criterion ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")).
Check stopping criterion: if

|  |  |  |
| --- | --- | --- |
|  | the improvement in the objective of Problem ([3.12](https://arxiv.org/html/2601.09127v1#S3.E12 "In 3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")), ([3.6](https://arxiv.org/html/2601.09127v1#S3.E6 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))-([3.7](https://arxiv.org/html/2601.09127v1#S3.E7 "In 3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"))≤t​o​l,\textrm{the improvement in the objective of Problem \eqref{SMPC1-new-trb-MRB}, \eqref{SMPC3-trb}-\eqref{SMPC4-trb}}\leq\ tol, |  |

then
declare the model predictive control for time tt as

|  |  |  |
| --- | --- | --- |
|  | πt+1|tM​P​C−M​R​B:=πt+1|t∗,k,\pi^{MPC-MRB}\_{t+1|t}:=\pi^{\*,k}\_{t+1|t}, |  |

and apply this control at time tt.

Otherwise,

* •

  Set πτk+1=πτk+ρk​(πτ|t∗,k−πτk),τ=t+1,…,t+H,\pi^{k+1}\_{\tau}=\pi^{k}\_{\tau}+\rho^{k}(\pi^{\*,k}\_{\tau|t}-\pi^{k}\_{\tau}),\ \tau=t+1,...,t+H,
* •

  update ρk\rho^{k} to ρk+1\rho^{k+1}: ρk+1=ρk​(1−ξ​ρk)\rho^{k+1}=\rho^{k}(1-\xi\rho^{k}) where ξ∈[0,1]\xi\in[0,1],
* •

  set k←k+1k\leftarrow k+1, and go to Iteration kk.

## 4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods

This section addresses the computation of the forecasts r^τ|t\widehat{r}\_{\tau|t} and Σ^τ|t\widehat{\Sigma}\_{\tau|t}, emphasizing methods that are both computationally efficient and practically accurate. Our approach is based on ideas from the theory of Hidden Markov Models (HMM) and from the Black-Litterman (BL) methodology frequently used in financial asset management.
There are a plethora of references regarding both HMM and Black-Litterman methodologies, and we refer to [[NML17](https://arxiv.org/html/2601.09127v1#bib.bibx26), [NBLM18](https://arxiv.org/html/2601.09127v1#bib.bibx25)] for the discussion of HMM relevant to our work, and to [[Meu08](https://arxiv.org/html/2601.09127v1#bib.bibx24)] for a discussion of the Black-Litterman model.

We deviate from the BL methodology by dispensing with the reverse optimization part that in the original BL model computes the expectation vector of the prior distribution of the portfolio means by backing it up from the market weights (see, e.g., [[Meu08](https://arxiv.org/html/2601.09127v1#bib.bibx24)] formula (5)). Instead, we take as the expectation vectors of the prior distribution of the portfolio means, in each regime, the means vectors generated by the HHM module of our methodology.

As before, we assume that the coefficients γt\gamma\_{t}, ϕt\phi\_{t} and ηt\eta\_{t} are given. The forecasting procedure proceeds according to the following stages.

HMM forecasts of moments of asset returns.
Our HMM forecasts are done using daily data. The asset management is done on the 𝐑​(0)\mathbf{R}(0) basis. In particular, portfolio rebalancing is done on the dates from the set 𝐑​(0)\mathbf{R}(0).

We assume that the vectors of returns rt,t=0,1,2,…,r\_{t},\ t=0,1,2,..., follow multivariate normal distributions. As in [[LUM21](https://arxiv.org/html/2601.09127v1#bib.bibx23)] we consider two regimes of the economy: normal regime and contraction regime, with the respective prior distributions of returns being 𝒩​(μn,Σn)\mathcal{N}(\mu\_{n},\Sigma\_{n}) and 𝒩​(μc,Σc)\mathcal{N}(\mu\_{c},\Sigma\_{c}). We take a HMM (Rt,rt)(R\_{t},r\_{t}), t=0,1,2,…,t=0,1,2,..., where RtR\_{t} is the unobserved economy regime at time tt, and rtr\_{t} is the observed vector of returns at time tt. Correspondingly, we assume that RR is a time-homogeneous Markov chain with the state space {n,c}\{n,c\}, and with transition probability matrix

|  |  |  |
| --- | --- | --- |
|  | Λ=[pn​n1−pn​n1−pc​cpc​c].\Lambda=\begin{bmatrix}p\_{nn}&1-p\_{nn}\\ 1-p\_{cc}&p\_{cc}\\ \end{bmatrix}. |  |

The forecasts related to asset returns will be needed at each date tt. Accordingly, the HMM parameters pn​np\_{nn}, pc​cp\_{cc}, μn\mu\_{n}, μc\mu\_{c}, Σn\Sigma\_{n} and Σc\Sigma\_{c} can and will be updated at any time tt, as new observations come between time t−1t-1 and time tt. We denote these updates as pn​n​(t)p\_{nn}(t), pc​c​(t)p\_{cc}(t), μn​(t)\mu\_{n}(t), μc​(t)\mu\_{c}(t), Σn​(t)\Sigma\_{n}(t) and Σc​(t)\Sigma\_{c}(t). Then, the first two moments of the asset returns are estimated for future periods τ=t+1,…,t+H\tau=t+1,\ldots,t+H, by considering that model parameters are constant in τ\tau (for a given tt). For instance, [[NBLM18](https://arxiv.org/html/2601.09127v1#bib.bibx25)] considered time-dd dependent HMM parameter estimated using an online version of the expectation-maximization algorithm introduced by Stenger et al. (2001). Whereas in [[LUM21](https://arxiv.org/html/2601.09127v1#bib.bibx23)], HMM parameters are fitted at every time dd based on returns of past 2000 days.

Now, given the information available at time tt, i.e. on day tt, we can update (or train) the HMM to obtain the probability qtq\_{t} that the market is in the normal regime at time tt. Based on that, and based on the time-dd fitted HMM parameters, we compute the forecasts of the moments of prior distributions of returns. These forecasts are computed based on the postulate that the distribution of r​(τ)r(\tau), given the information available at time tt, is a mixture of distributions 𝒩​(μn,Σn)\mathcal{N}(\mu\_{n},\Sigma\_{n}) and 𝒩​(μc,Σc)\mathcal{N}(\mu\_{c},\Sigma\_{c}) with weights qτ|tq\_{\tau|t} and 1−qτ|t1-q\_{\tau|t}, where qτ|tq\_{\tau|t} is the probability that the market is in the normal regime on day τ\tau given the information available on day tt. Thus, we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | qτ|t\displaystyle q\_{\tau|t} | =qτ−1|t​pn​n​(t)+(1−qτ−1|t)​(1−pc​c​(t)),τ=t+1,…,qt|t=qt,τ=t,t+1,…,.\displaystyle=q\_{\tau-1|t}p\_{nn}(t)+(1-q\_{\tau-1|t})(1-p\_{cc}(t)),\ \tau=t+1,\ldots,\ q\_{t|t}=q\_{t},\ \tau=t,t+1,\ldots,. |  |

In addition, for τ=t,t+1,…,\tau=t,t+1,\ldots, the first two forecasted moments of the mixture distribution are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μτ|t\displaystyle\mu\_{\tau|t} | =qτ|t​μn​(t)+(1−qτ|t)​μc​(t),\displaystyle=q\_{\tau|t}\mu\_{n}(t)+(1-q\_{\tau|t})\mu\_{c}(t), |  | (4.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Στ|t\displaystyle\Sigma\_{\tau|t} | =qτ|t​Σn+(1−qτ|t)​Σc+qτ|t​(μn​(t)​μn⊺​(t)−μτ|t​μτ|t⊺)\displaystyle=q\_{\tau|t}\Sigma\_{n}+(1-q\_{\tau|t})\Sigma\_{c}+q\_{\tau|t}(\mu\_{n}(t)\mu^{\intercal}\_{n}(t)-\mu\_{\tau|t}\mu^{\intercal}\_{\tau|t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−qτ|t)​(μc​(t)​μc⊺​(t)−μτ|t​μτ|t⊺).\displaystyle+(1-q\_{\tau|t})(\mu\_{c}(t)\mu^{\intercal}\_{c}(t)-\mu\_{\tau|t}\mu^{\intercal}\_{\tau|t}). |  |

Note that the distribution of rτr\_{\tau}, given the information available at time tt, is not a Gaussian distribution, as it is a mixture of two Gaussians. We denote by rτ|tr\_{\tau|t} a random variable with the mixed Gaussians distribution as above.

BL-like prior means of asset returns. We now take the Bayesian view and we postulate that the means in each leg of the distribution of rτ|tr\_{\tau|t}, given the information available at time tt, are random and distributed according to normal distributions. Specifically, to model the prior means
we let w​(t)\textbf{w}(t) be the vector of equilibrium weights at time tt, and we let λ¯n/c​(t)\bar{\lambda}\_{n/c}(t) be the average normal market risk-aversion as seen at time tt in regime n/cn/c. Then, we postulate that for
τ=t,…,t+H−1,\tau=t,\ldots,t+H-1, the prior means of the asset returns are444See e.g. [[Meu08](https://arxiv.org/html/2601.09127v1#bib.bibx24)] equations (2) and (5) for motivation.

|  |  |  |  |
| --- | --- | --- | --- |
|  | μτ|tB​L,c=2​λ¯c​(t)​Στ|t​w​(t)+εμ,c​(τ|t),μτ|tB​L,n=2​λ¯n​(t)​Στ|t​w​(t)+ετ|tμ,n,\mu^{BL,c}\_{\tau|t}=2\bar{\lambda}\_{c}(t)\Sigma\_{\tau|t}\textbf{w}(t)+\varepsilon^{\mu,c}(\tau|t),\ \mu^{BL,n}\_{\tau|t}=2\bar{\lambda}\_{n}(t)\Sigma\_{\tau|t}\textbf{w}(t)+\varepsilon^{\mu,n}\_{\tau|t}, |  | (4.2) |

where ετ|tμ,c/n\varepsilon^{\mu,c/n}\_{\tau|t}, τ=t,…,t+H−1\tau=t,\ldots,t+H-1 are independent noises, with ετ|tμ,c/d∼𝒩​(0,ιc/n​Στ|t)\varepsilon^{\mu,c/d}\_{\tau|t}\sim\mathcal{N}(0,\iota\_{c/n}{\Sigma}\_{\tau|t}), and fixed parameters ιc/n>0.\iota\_{c/n}>0.

We remark that in Black and Litterman paper [[BL92](https://arxiv.org/html/2601.09127v1#bib.bibx6)] the counterpart of ιc/n\iota\_{c/n} is denoted by τ\tau and indicates the uncertainty of the CAPM prior and ranges between 0.01 and 0.05. Other authors recommend choosing τ∈(0,1).\tau\in(0,1). See the discussion in [[Meu08](https://arxiv.org/html/2601.09127v1#bib.bibx24)] regarding the value assigned to τ\tau. The extreme value 0 of ιc/n\iota\_{c/n} reflects degenerate prior: no uncertainty about the market implied prior.

BL views. In the spirit of the Black-Litterman methodology we now introduce the RA’s views regarding the future values of expected returns on the NN assets included in our portfolios. The views are represented by deterministic 1×K1\times K vectors denoted as

|  |  |  |
| --- | --- | --- |
|  | vτ|tB​L,c​and​vτ|tB​L,n.\displaystyle v^{BL,c}\_{\tau|t}\ \textrm{and}\ v^{BL,n}\_{\tau|t}. |  |

To simplify the set-up we have assumed that the number KK of views does not depend either on tt or τ\tau. Again, in the spirit of the Black-Litterman methodology that relationship between the views and the BL prior means of asset returns is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pc​μτ|tB​L,c\displaystyle P\_{c}\mu^{BL,c}\_{\tau|t} | =vτ|tB​L,c+ετ|tv,c,\displaystyle=v^{BL,c}\_{\tau|t}+\varepsilon^{v,c}\_{\tau|t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn​μτ|tB​L,n\displaystyle P\_{n}\mu^{BL,n}\_{\tau|t} | =vτ|tB​L,n+ετ|tv,n,\displaystyle=v^{BL,n}\_{\tau|t}+\varepsilon^{v,n}\_{\tau|t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | τ\displaystyle\tau | =t,…,t+H−1,\displaystyle=t,\ldots,t+H-1, |  |

where PcP\_{c} and PnP\_{n} are K×NK\times N pick matrices, and where ετ|tv,c/n\varepsilon^{v,c/n}\_{\tau|t}, τ=t,…,t+H−1\tau=t,\ldots,t+H-1 are independent noises, representing the degree of confidence granted to the view, with ετ|tv∼𝒩​(0,αc/n​Στ|t)\varepsilon^{v}\_{\tau|t}\sim\mathcal{N}(0,\alpha\_{c/n}{\Sigma}\_{\tau|t}). To simplify the set-up we have assumed that the pick matrices PcP\_{c} and PnP\_{n} do not depend either on tt or on τ\tau.

We note that αc/n​Στ|t\alpha\_{c/n}{\Sigma}\_{\tau|t} corresponds to Ω\Omega, and αc/n\alpha\_{c/n} corresponds to 1c\frac{1}{c} in [[Meu08](https://arxiv.org/html/2601.09127v1#bib.bibx24)], where c∈(0,∞)c\in(0,\infty). Two extreme values of αc/n\alpha\_{c/n} are 0 and ∞\infty. The value 0 reflects total confidence in the views, whereas ∞\infty reflects total lack of confidence in the views.

There is vast literature regarding generating views for the purpose of the classical Black-Litterman model. See e.g. [[WSK16](https://arxiv.org/html/2601.09127v1#bib.bibx33), [GL16](https://arxiv.org/html/2601.09127v1#bib.bibx16), [KUA19](https://arxiv.org/html/2601.09127v1#bib.bibx21), [RFM21](https://arxiv.org/html/2601.09127v1#bib.bibx28), [BS22](https://arxiv.org/html/2601.09127v1#bib.bibx10)] and the references therein.
We will illustrate our approach with very special choices for the views and the pick matrices. Specifically, we consider the case of total absolute views where K=NK=N, Pc=Pn=IN×NP\_{c}=P\_{n}=I\_{N\times N}, with views chosen as

|  |  |  |  |
| --- | --- | --- | --- |
|  | vB​L,c​(τ|t)=vB​L,n​(τ|t)=μ​(τ|t).v\_{BL,c}(\tau|t)=v\_{BL,n}(\tau|t)=\mu(\tau|t). |  | (4.3) |

Other choices for the views and the pick matrices will be studied in a follow-up work.

Posterior forecasts of the moments through Bayesian updating. In the first step, we do the Bayesian updating on each leg cc and nn for time τ\tau. Let us take the cc leg.555Analogous formulae and remarks will apply to the nn leg. Given the prior as in ([4.2](https://arxiv.org/html/2601.09127v1#S4.E2 "In 4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) and the value of the views is vτ|tB​L,cv^{BL,c}\_{\tau|t} the posterior for this leg is Gaussian with mean

|  |  |  |  |
| --- | --- | --- | --- |
|  | r^τ|tB​L,c\displaystyle\widehat{r}^{BL,c}\_{\tau|t} | =2​λ¯c​(t)​Στ|t​w​(t)\displaystyle=2\bar{\lambda}\_{c}(t)\Sigma\_{\tau|t}\textbf{w}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ιB​L,cιB​L,c+αc​Στ|t​Pc⊺​(Pc​Στ|t​Pc⊺)−1​(vτ|tB​L,c−Pc​2​λ¯c​(t)​Στ|t​w​(t))\displaystyle\qquad+\frac{\iota\_{BL,c}}{\iota\_{BL,c}+\alpha\_{c}}{\Sigma}\_{\tau|t}P^{\intercal}\_{c}\Bigg(P\_{c}{\Sigma}\_{\tau|t}P^{\intercal}\_{c}\Bigg)^{-1}\Bigg(v^{BL,c}\_{\tau|t}-P\_{c}2\bar{\lambda}\_{c}(t)\Sigma\_{\tau|t}\textbf{w}(t)\Bigg) |  |

and variance-covariance matrix

|  |  |  |
| --- | --- | --- |
|  | Σ^τ|tB​L,c=(1+ιB​L,c)Στ|t−ιB​L,c2ιB​L,c+αcΣτ|tPc⊺(PcΣτ|tPc⊺)−1PcΣτ|t).\displaystyle\widehat{\Sigma}^{BL,c}\_{\tau|t}=(1+\iota\_{BL,c}){\Sigma}\_{\tau|t}-\frac{\iota^{2}\_{BL,c}}{\iota\_{BL,c}+\alpha\_{c}}{\Sigma}\_{\tau|t}P^{\intercal}\_{c}\Bigg(P\_{c}{\Sigma}\_{\tau|t}P^{\intercal}\_{c}\Bigg)^{-1}P\_{c}{\Sigma}\_{\tau|t}). |  |

###### Remark 4.1.

Consider the prior as in ([4.2](https://arxiv.org/html/2601.09127v1#S4.E2 "In 4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach")). Then:

1. (i)

   In the case of no uncertainty of the prior, that is ιB​L,c=0\iota\_{BL,c}=0, we have that r^τ|tB​L,c=2​λ¯c​(t)​Στ|t​w​(t)\widehat{r}^{BL,c}\_{\tau|t}=2\bar{\lambda}\_{c}(t)\Sigma\_{\tau|t}\textbf{w}(t), and Σ^τ|tB​Lc=Στ|t\widehat{\Sigma}^{BL\_{c}}\_{\tau|t}={\Sigma}\_{\tau|t}.
2. (ii)

   In the case of total lack of confidence in the views, that is αc=∞\alpha\_{c}=\infty we have r^τ|tB​L,c=2​λ¯c​(t)​Στ|t​w​(t)\widehat{r}^{BL,c}\_{\tau|t}=2\bar{\lambda}\_{c}(t)\Sigma\_{\tau|t}\textbf{w}(t) , and Σ^τ|tB​Lc=(1+ιB​L,c)​Στ|t\widehat{\Sigma}^{BL\_{c}}\_{\tau|t}=(1+\iota\_{BL,c}){\Sigma}\_{\tau|t}. The presence of the factor (1+ιB​L,c)(1+\iota\_{BL,c}) reflects the estimation bias (error) in the prior.
3. (iii)

   In the case of complete confidence in the absolute views, that is αc=0\alpha\_{c}=0 and Pc=I​dP\_{c}=Id, we have r^τ|tB​L,c=vτ|tB​L,c\widehat{r}^{BL,c}\_{\tau|t}=v^{BL,c}\_{\tau|t} and Σ^τ|tB​Lc=Στ|t\widehat{\Sigma}^{BL\_{c}}\_{\tau|t}={\Sigma}\_{\tau|t}.

In the next step, we mix the two posteriors to get the posterior forecasts of the moments of r​(τ)r(\tau) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | r^τ|tB​L\displaystyle\widehat{r}^{BL}\_{\tau|t} | =qτ|t​r^τ|tB​L,n+(1−qτ|t)​rτ|tB​L,c,\displaystyle=q\_{\tau|t}\widehat{r}^{BL,n}\_{\tau|t}+(1-q\_{\tau|t})r^{BL,c}\_{\tau|t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ^τ|tB​L\displaystyle\widehat{\Sigma}^{BL}\_{\tau|t} | =qτ|t​Σ^τ|tB​L,n+(1−qτ|t)​Σ^τ|tB​L,c\displaystyle=q\_{\tau|t}\widehat{\Sigma}^{BL,n}\_{\tau|t}+(1-q\_{\tau|t})\widehat{\Sigma}^{BL,c}\_{\tau|t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +qτ|t​(r^τ|tB​L,n​(r^τ|tB​L,n)⊺−r^τ|tB​L​(r^τ|tB​L)⊺)\displaystyle+q\_{\tau|t}(\widehat{r}^{BL,n}\_{\tau|t}(\widehat{r}^{BL,n}\_{\tau|t})^{\intercal}-\widehat{r}^{BL}\_{\tau|t}(\widehat{r}^{BL}\_{\tau|t})^{\intercal}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−qτ|t)​(r^τ|tB​L,c​(r^τ|tB​L,c)⊺−r^τ|tB​L​(r^τ|tB​L)⊺).\displaystyle+(1-q\_{\tau|t})(\widehat{r}^{BL,c}\_{\tau|t}(\widehat{r}^{BL,c}\_{\tau|t})^{\intercal}-\widehat{r}^{BL}\_{\tau|t}(\widehat{r}^{BL}\_{\tau|t})^{\intercal}). |  |

###### Remark 4.2.

With these forecasting methodologies at hand, we conclude with the refined formulation of the MV and MRB approaches to RA using SMPC with HMM-BL. For the MV criterion (Section [3.1.1](https://arxiv.org/html/2601.09127v1#S3.SS1.SSS1 "3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) and, respectively, for the MRB criterion (Section [3.2.1](https://arxiv.org/html/2601.09127v1#S3.SS2.SSS1 "3.2.1 MRB receding horizon SMPC ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")), we replace r^τ|t\widehat{r}\_{\tau|t} and Σ^τ|t\widehat{\Sigma}\_{\tau|t} with the BL forecasts r^B​L​τ|t\widehat{r}^{BL}{\tau|t} and Σ^B​L​τ|t\widehat{\Sigma}^{BL}{\tau|t}, respectively.

## 5 Risk profiling, allocation targets and trading constraints

In this section we discuss how to model parameters related the investor’s risk profile and the trading constraints.

### 5.1 Risk profiling

One of the key features of a robo-advisor system is the possibility for the agent to interact with the robot on regular basis and reveal or update to the robot her current risk-reward preferences that the robot has to use for future portfolio re-balances. There is a growing literature on how to elicit the risk preferences of an agent, and we refer to e.g. [[DJKX21](https://arxiv.org/html/2601.09127v1#bib.bibx14), [ACRLS20](https://arxiv.org/html/2601.09127v1#bib.bibx2), [CÓZ22](https://arxiv.org/html/2601.09127v1#bib.bibx13), [CLQS22](https://arxiv.org/html/2601.09127v1#bib.bibx12)] and references therein. However, traditionally, but also following the regulatory frameworks requirements666In US under the SEC guidelines (SEC, 2006; SEC, 2019), and in Europe under MiFID (Markets in Financial Instruments Directive) regulation. the advisors are required to risk profile the investors through a questionnaire. The outcome of such questionnaire is mapped to a numerical score, that we will identify in our model as the risk aversion coefficient denoted by γt\gamma\_{t}, for t∈𝒯t\in\mathcal{T}. We assume that γ~t\widetilde{\gamma}\_{t} can take a finite number of values Γ={γ1,γ~2,…,γN}\Gamma=\{\gamma^{1},\widetilde{\gamma}^{2},\ldots,\gamma^{N}\}, where we assume that γ1<γ2<⋯<γN\gamma^{1}<\gamma^{2}<\cdots<\gamma^{N}.

For the MV criterion, risk preferences are encoded by the coefficient γt∈Γ\gamma\_{t}\in\Gamma, which directly parametrizes the risk–return trade-off in the objective. For the MRB criterion, investor risk preferences are specified through the enforcement parameter ϕt\phi\_{t} and the risk-budgeting weights bib\_{i}, with bib\_{i} parametrized by the coefficient γR\gamma\_{R} as described in Remark [3.2](https://arxiv.org/html/2601.09127v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach").
The parameter ϕt\phi\_{t} governs the penalization strength of deviations from the prescribed risk budgets and is typically assumed constant over time.
The effective risk mapping in the MRB formulation is induced by γR∈ΓR\gamma\_{R}\in\Gamma\_{R}, which determines the allocation of aggregate risk across asset classes. The admissible set ΓR\Gamma\_{R} is defined as a mapping of Γ\Gamma, ensuring consistency between the MV and MRB risk parametrizations.

In the numerical experiments, we consider several specifications for the risk-profile processes γt\gamma\_{t} and γR,t\gamma\_{R,t}, which in a robo-advisory context represent the time evolution of the client’s risk profile as inferred by the platform:

* •

  *Static profile*: γt=γR,t=γ\gamma\_{t}=\gamma\_{R,t}=\gamma for all t∈𝒯t\in\mathcal{T}. This specification corresponds to a client with a fixed risk profile and is used for most of the strategy comparison results;
* •

  *Lifecycle profile*: γt≤γt+1\gamma\_{t}\leq\gamma\_{t+1} and γR,t≤γR,t+1\gamma\_{R,t}\leq\gamma\_{R,t+1}, capturing age-based de-risking commonly implemented in robo-advisors, whereby inferred risk tolerance decreases monotonically over time. In this study we use a linear decreasing function;
* •

  *Noisy profile*: γt∼Uniform​(Γ)\gamma\_{t}\sim\mathrm{Uniform}(\Gamma) and γR,t∼Uniform​(Γ′)\gamma\_{R,t}\sim\mathrm{Uniform}(\Gamma^{\prime}), mimicking an inconsistent or unstable client profile arising from noisy questionnaires, behavioral biases, or frequent reassessment.

Other modeling approaches for the risk-aversion coefficient, including stochastic or learning-based methods, could also be considered but are beyond the scope of this study.

### 5.2 Allocation target constraints

Another popular approach among financial advisors is to design a strategy that targets a specified portfolio at maturity, matching the investor’s goal or target, with a specific maturity time. Usually, a more conservative portfolio the longer the horizon. Instead of targeting individual assets, we adopt a class-level approach: only the aggregate weights of asset classes, defined by risk profile, are constrained.
For instance, we partition the assets into two groups: GBG\_{B} consisting of fixed-income or lower-risk assets, and GSG\_{S} consisting of higher-risk assets such as equities.
We then specify target weights for each class, wBw\_{B} and wSw\_{S}.
The target portfolio must satisfy the constraints777If there are only two groups, a single group constraint suffices since portfolio weights sum to one.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i∈GBπτi=wB,∑i∈GSπτi=wS.\sum\_{i\in G\_{B}}\pi\_{\tau}^{i}=w\_{B},\quad\sum\_{i\in G\_{S}}\pi\_{\tau}^{i}=w\_{S}. |  | (5.1) |

The class weights wBw\_{B} and wSw\_{S} are computed analogously to the MRB group weights (Remark [3.2](https://arxiv.org/html/2601.09127v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")), i.e.,

|  |  |  |
| --- | --- | --- |
|  | wB=γtarget1+γtarget,wS=11+γtarget.w\_{B}=\frac{\gamma\_{\text{target}}}{1+\gamma\_{\text{target}}},\quad w\_{S}=\frac{1}{1+\gamma\_{\text{target}}}. |  |

To avoid abrupt adjustments, these constraints are enforced gradually rather than only at the final step τ=T−1\tau=T-1.
This is achieved by linearly interpolating the risk-profile coefficient from the initial γ\gamma to the target γtarget\gamma\_{\text{target}} and imposing ([5.1](https://arxiv.org/html/2601.09127v1#S5.E1 "In 5.2 Allocation target constraints ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach")) for τ=T′,…,T\tau=T^{\prime},\ldots,T, where T′T^{\prime} is chosen appropriately.

### 5.3 Transaction costs

Transaction costs are a critical consideration in portfolio management, especially for algorithmic or robo-advising strategies.
They can be controlled through two complementary mechanisms.

First, through the soft penalty term TC\mathrm{TC} that we included in the objective function to discourage excessive trading. In this study, we take T​C​(z)=‖z‖1TC(z)=||z||\_{1}, with various values for the scale parameters η\eta.
A more comprehensive transaction cost function TC is a version of the formula given in [[BBD+17](https://arxiv.org/html/2601.09127v1#bib.bibx4)],
T​C​(z)=∑i=1NT​Ci​(zi),TC(z)=\sum\_{i=1}^{N}TC\_{i}(z\_{i}), where
T​Ci​(zi)=ai​|zi|+ci​ziTC\_{i}(z\_{i})=a\_{i}|z\_{i}|+c\_{i}z\_{i}, that allows to account for asymmetry in trading. We did not find significant qualitative changes in our numerical experiment when using more complicated TC functions, and we do not report these results here.

Second, hard constraints on portfolio turnover can is imposed to explicitly limit the magnitude of changes in positions between consecutive periods, ∑i=1N|πτ+1i−πτi|≤δ\sum\_{i=1}^{N}|\pi\_{\tau+1}^{i}-\pi\_{\tau}^{i}|\leq\delta, τ=0,…,T−1\tau=0,\ldots,T-1, where δ>0\delta>0 is the turnover bound. This combined approach allows the strategy to balance portfolio adjustments with the cost of trading, which is essential for realistic implementation in a robo-advisory framework.

A less common approach among robo-advisors, though occasionally used by portfolio managers, is a *turnover-budget constraint*, which limits the total amount of transaction costs over the investment horizon.
We omit this feature in the present study, as we consider the two mechanisms discussed above–soft penalty term TC\mathrm{TC} and hard turnover constraints–sufficient for practical transaction-cost management.
Nevertheless, given the path-dependent nature of turnover-budget constraints, their theoretical analysis could provide valuable insights.

### 5.4 Initial portfolio

There is no canonical method to specify the initial portfolio, and in the literature common choices include equal weights, random weights and then ignoring several initial trades.
For concreteness, we construct the initial portfolio based on an initial risk-profile coefficient, denoted γIW\gamma\_{\text{IW}}, by setting
π0i=bi\pi\_{0}^{i}=b\_{i}, where bib\_{i} are defined as in the MRB approach (Remark [3.2](https://arxiv.org/html/2601.09127v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")).
In most experiments, we take γIW=γ0\gamma\_{\text{IW}}=\gamma\_{0}.

## 6 Numerical experiment on market data

In this section, we examine the proposed robo-advising methodology through a numerical example using market data. For our portfolio, we include eight Exchange-Traded Funds (ETFs), as detailed in Table [1](https://arxiv.org/html/2601.09127v1#S6.T1 "Table 1 ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Common to mainstream robo-advisors, we have chosen a diversified portfolio of ETFs that spans various financial instruments (stocks, bonds, real estate) and different markets (developed, emerging). The data sets consist of daily closing asset prices (source: Yahoo! Finance) and daily total assets under management (source: ycharts.com) from January 2009 to December 2024, total 3268 data in the time series. The data were cleaned for outliers, and the time series were aligned to match dates with missing values accounted for. Historical asset prices are shown in Figure [1](https://arxiv.org/html/2601.09127v1#S6.F1 "Figure 1 ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). The key statistics for each included asset and S&P500 market index are displayed in Table [2](https://arxiv.org/html/2601.09127v1#S6.T2 "Table 2 ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), and Table [3](https://arxiv.org/html/2601.09127v1#S6.F3 "Table 3 ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach")

For these experiments, we fix January 2, 2020 as the starting trading day when the hypothetical client enters the market and first interacts with the RA. The RA re-balances portfolios monthly (every 22 days), for 56 periods of time; see gray shaded area in Figure [1](https://arxiv.org/html/2601.09127v1#S6.F1 "Figure 1 ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Historical data from the past five years is utilized for calibration and estimation, applying a rolling window approach.

|  |  |  |
| --- | --- | --- |
| Stocks | VTI | Vanguard Total Stock Market ETF |
|  | VEA | Vanguard FTSE Developed Markets ETF |
|  | VWO | Vanguard FTSE Emerging Markets ETF |
| Bonds | BND | Vanguard Total Bond Market ETF |
|  | EMB | iShares J.P. Morgan USD Emerging Markets Bond ETF |
|  | MUB | iShares National Muni Bond ETF |
|  | LQD | iShares iBoxx $ Investment Grade Corporate Bond ETF |
| Alternatives | VNQ | Vanguard Real Estate ETF |

Table 1: List of included ETFs, by category.

![Refer to caption](x1.png)


Figure 1: Historical asset prices, scaled to 100 at the first observation. The shaded area represents the trading period, January 16 2020 to December 31, 2024.



|  | BND | EMB | LQD | MUB | VEA | VNQ | VTI | VWO | SPX |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mean | 0.025 | 0.049 | 0.044 | 0.032 | 0.084 | 0.131 | 0.151 | 0.088 | 0.133 |
| St. Dev. | 0.049 | 0.099 | 0.078 | 0.050 | 0.196 | 0.257 | 0.182 | 0.223 | 0.180 |
| Median | 0.059 | 0.093 | 0.106 | 0.046 | 0.185 | 0.208 | 0.207 | 0.182 | 0.179 |
| 75% quant. | 0.424 | 0.708 | 0.654 | 0.326 | 1.646 | 1.859 | 1.531 | 1.944 | 1.467 |
| 25% quant. | -0.344 | -0.569 | -0.542 | -0.238 | -1.339 | -1.525 | -1.009 | -1.745 | -0.978 |

Table 2: Annualized key statistics for ETFs and S&P500 returns.

![Refer to caption](corr-matrix.jpg)


Table 3: Correlation matrix of asset returns.

### 6.1 Computational Methods

The computational experiments and the development of the RA platform were done using Python 3 (version 3.13.7) programming language, on a PC (Core Ultra 7 165H, 1.40 GHz, with 32 GB RAM, 16 Cores) running Windows 11 Pro.

For estimation and calibration of HMM model, we used hmmlearn (version 0.3.2) library, which uses the Viterbi algorithm to forecast the hidden states and the Baum-Welch algorithm to estimate the model parameters. Specifically, in line with our Gaussian model assumptions, see Section [4](https://arxiv.org/html/2601.09127v1#S4 "4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we use hmm.GaussianHMM class to fit a two state HMM. For this step, we used past five years of historical daily data with rolling window. In Figure [2](https://arxiv.org/html/2601.09127v1#S6.F2 "Figure 2 ‣ 6.1 Computational Methods ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we display the HMM predicted states of the economy. The vertically shaded gray area corresponds to the cc regime, namely the contraction economy phase. By visual inspection, we note that indeed sharp declines in the prices where picked up by the algorithm.

![Refer to caption](hmm.png)


Figure 2: Forecasted market regimes by HMM model, gray shaded area corresponds to ‘contraction’ regime. Dark blue curve represents the average prices of all assets.

We note that all optimization problems are convex, particularly due to the convex approximation for risk budgeting criteria (Section [3.2.2](https://arxiv.org/html/2601.09127v1#S3.SS2.SSS2 "3.2.2 Convex approximation to the MRB criterion ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach")). This allows the use of computationally efficient open-source optimization routines. We use the Python-embedded modeling language cvxpy (version 1.5) for all optimization problems. Thanks to the computational efficiency of the MPC methodology, the computation time for a single strategy is on the order of milliseconds, making it scalable for managing portfolios across a large number of investors.

### 6.2 Set of parameters

We ran a wide range of combinations of model parameters, within ranges found in existing literature [[CK18](https://arxiv.org/html/2601.09127v1#bib.bibx11), [LUM21](https://arxiv.org/html/2601.09127v1#bib.bibx23), [HST17](https://arxiv.org/html/2601.09127v1#bib.bibx19), [AS22](https://arxiv.org/html/2601.09127v1#bib.bibx3), [OK21](https://arxiv.org/html/2601.09127v1#bib.bibx27)] but adjusted to our modeling scales:

* •

  Number of assets N=8N=8;
* •

  MPC rolling horizon H∈{1,2,3,5,7,10,15,20}H\in\{1,2,3,5,7,10,15,20\};
* •

  Transaction costs sensitivity factor η∈{0,0.0001,0.001,0.005,0.007,0.01,0.05,0.1,0.5,1}\eta\in\{0,0.0001,0.001,0.005,0.007,0.01,0.05,0.1,0.5,1\},
* •

  Turnover constraint bound δ∈{0.001,0.003,0.005,0.008,0.01,0.03,0.05,0.08,0.1,0.15,+∞}\delta\in\{0.001,0.003,0.005,0.008,0.01,0.03,0.05,0.08,0.1,0.15,+\infty\};
* •

  Risk attitude parameter in MV problem γ∈{0.001,0.01,0.1,0.5,1,3,5,10,25}\gamma\in\{0.001,0.01,0.1,0.5,1,3,5,10,25\};
* •

  Risk-budgeting parameters:

  + –

    sensitivity coefficient ϕ∈{0.01,0.02,0.05,0.08,0.1,0.15,0.2,0.3,0.5,0.7,1}\phi\in\{0.01,0.02,0.05,0.08,0.1,0.15,0.2,0.3,0.5,0.7,1\};
  + –

    the risk attitude coefficient γR\gamma\_{R} is chosen following Remark [3.2](https://arxiv.org/html/2601.09127v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2 Mean-risk-budgeting (MRB) portfolio selection ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach").(i), by dividing the assets in two groups: the risky assets VTI, VEA, VWO, VNQ and less risky assets BND, MUB, LQD, EMB. We consider γR∈{0.001,0.005,0.01,0.1,0.5,1,1.5,2,5,10}\gamma\_{R}\in\{0.001,0.005,0.01,0.1,0.5,1,1.5,2,5,10\}.
  + –

    initial value ρ0=0.6∈(0,1)\rho^{0}=0.6\in(0,1) in the recursion computation of ρk\rho^{k};
  + –

    regularization coefficient in convexification, κ=0.5∈(0,1)\kappa=0.5\in(0,1);
  + –

    iterative weight coefficient ξ=0.5∈(0,1)\xi=0.5\in(0,1);
  + –

    error tolerance ε=0.01\varepsilon=0.01;
* •

  Black-Litterman:

  + –

    average market risk-aversion in two regimes, λ¯0∈{0.1,0.3,0.5,1,1.5,2,2.5,3,3.5,4,5}\overline{\lambda}\_{0}\in\{0.1,0.3,0.5,1,1.5,2,2.5,3,3.5,4,5\} and λ¯n=1.2⋅λ0\overline{\lambda}\_{n}=1.2\cdot\lambda\_{0}, λ¯c=0.8⋅λ0\overline{\lambda}\_{c}=0.8\cdot\lambda\_{0};
  + –

    uncertainty of CAPM as scaling coefficients of the covariance matrix in the priors, ιB​L,n∈{0.01,0.03,0.05,0.1,0.5,1}\iota\_{BL,n}\in\{0.01,0.03,0.05,0.1,0.5,1\} and ιB​L,c=0.9⋅ιB​L,n\iota\_{BL,c}=0.9\cdot\iota\_{BL,n};
  + –

    confidence in the views, αn=αc∈{0.01,0.1,0.5,1,5,10}\alpha\_{n}=\alpha\_{c}\in\{0.01,0.1,0.5,1,5,10\}.
* •

  Target portfolio risk attitude coefficient γtarget∈{0.5,1,2}\gamma\_{\textrm{target}}\in\{0.5,1,2\}; see also Section [5.2](https://arxiv.org/html/2601.09127v1#S5.SS2 "5.2 Allocation target constraints ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

We focus our analysis on the following parameters γ\gamma, γR​P\gamma\_{RP}, η\eta, ϕ\phi, HH, δ\delta, and γtarget\gamma\_{\textrm{target}}.
We noticed that values around the specific values of ρ0,κ,ξ,ε\rho^{0},\kappa,\xi,\varepsilon we consider do not significantly change the overall portfolio performance. Therefore, for tractability, we fix their values. As mentioned earlier, we consider total absolute views with K=NK=N, Pc=Pn=IN×NP\_{c}=P\_{n}=I\_{N\times N}, and the views given by ([4.3](https://arxiv.org/html/2601.09127v1#S4.E3 "In 4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach")). Additionally, for most of our experiments, we choose αc/n=1\alpha\_{c/n}=1, λ¯0=1\overline{\lambda}\_{0}=1, ιB​L,n=0.03\iota\_{BL,n}=0.03. Calibration to these parameters is more of an art. Our choices were based on overall performance of the portfolios and extensive numerical runs.

### 6.3 Employed RA strategies and benchmarks portfolios

MV-BL will denote the RA strategy with mean-variance criteria in the context of SMPC and using HMM combined with Black-Litterman methodology; see Section [4](https://arxiv.org/html/2601.09127v1#S4 "4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), and in particular Remark [4.2](https://arxiv.org/html/2601.09127v1#S4.Thmtheorem2 "Remark 4.2. ‣ 4 Forecasting of conditional moments of asset returns via Hidden Markov Models and the Black-Litterman Methods ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Correspondingly, MRB-BL stands for mean-risk-budgeting criterion, with SMPC, HMM and Black-Litterman elements. Along these two main RA strategies developed in this paper, for comparison, we also present the results for some traditional or benchmark strategies, described next.

MV-Est-myopic strategy uses mean-variance criteria, with mean and variance estimated using sample mean and sample variance. The optimization horizon is equal to one rebalancing period, H=1H=1, hence myopic. This is the approach mostly used in financial advising industry. MV-Est-MPC, similar to MV-EST-myopic approach, uses mean-variance criteria with sample mean and variance, but combined with MPC approach by taking a longer horizon H>1H>1; see Section [3.1.1](https://arxiv.org/html/2601.09127v1#S3.SS1.SSS1 "3.1.1 MV receding horizon SMPC ‣ 3.1 Mean-variance portfolio selection problem ‣ 3 SMPC for Robo-Advisors ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). This approach can be termed as traditional MPC as appearing in engineering contexts.

Additionally, we list the market portfolio SP500 equal to the Standard & Poor’s 500 Index, as well as the equal weighted portfolio 1/N.

We display the dynamics of weights πτ\pi\_{\tau}, and the wealth process of the RA strategies scaled to 100 at the starting time t=0t=0, January 2, 2020. In all figures, brighter-colored labels indicate riskier assets. Whenever necessary, we also report some annualized key performance metrics, computed using daily portfolio returns. In particular, we compute the mean return, the standard deviation of the returns (StDev), the maximum drawdown (MaxDD), Sharpe Ratio (SR), Gains-to-Loss ratio (GLR), Calmman Ratio (CR), and turnover. We recall that GLR​(X)=𝔼​[X]/𝔼​[X−]\textrm{GLR}(X)=\mathbb{E}[X]/\mathbb{E}[X^{-}] and SR​(X)=𝔼​[X]/StDev​(X)\textrm{SR}(X)=\mathbb{E}[X]/\textrm{StDev}(X). With Mt=max0≤s≤t⁡XtM\_{t}=\max\_{0\leq s\leq t}X\_{t} denoting the running maximum, the maximum drawdown is defined as
MaxDD​(X)=max0≤t≤T⁡(Mt−Xt)/Xt\textrm{MaxDD}(X)=\max\_{0\leq t\leq T}(M\_{t}-X\_{t})/X\_{t}, and then CR​(X)=𝔼​[X]/MaxDD​(X)\textrm{CR}(X)=\mathbb{E}[X]/\textrm{MaxDD}(X). Turnover is defined as

|  |  |  |
| --- | --- | --- |
|  | Turnover​(π)=12⋅252⋅∑t=2T∑i=1N|πi,t−πi,t−1|T−1\text{Turnover}(\pi)=\frac{1}{2}\cdot 252\cdot\frac{\displaystyle\sum\_{t=2}^{T}\sum\_{i=1}^{N}\bigl|\pi\_{i,t}-\pi\_{i,t-1}\bigr|}{T-1} |  |

### 6.4 Analysis of results

We present a series of results on the sensitivity of the studied RA systems to different parameter sets, structured across several subsections.
Unless otherwise noted, all other constraints and parameters are taken the same for all strategies.

#### 6.4.1 Risk attitude parameter γ\gamma in MV criteria

We start with the risk aversion parameter γ\gamma appearing in the mean-variance criteria. We fix H=7,δ=+∞,η=0H=7,\delta=+\infty,\eta=0. In Figure [3](https://arxiv.org/html/2601.09127v1#S6.F3a "Figure 3 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach") and Figure [4](https://arxiv.org/html/2601.09127v1#S6.F4 "Figure 4 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach") we display the portfolios’ structure for a wide range of values of parameter γ\gamma for MV-Est-myopic, MV-Est-MPC and MV-BL strategies, starting with a coarser grid in Figure [3](https://arxiv.org/html/2601.09127v1#S6.F3a "Figure 3 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), and focusing on γ\gamma values around one in Figure [4](https://arxiv.org/html/2601.09127v1#S6.F4 "Figure 4 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), for which we see a shift in portfolio composition for MV-Est-MPC around γ=1.5\gamma=1.5, and for MV-BL around γ=1\gamma=1. As expected, for larger γ\gamma, all three strategies become more conservative, investing mostly in bonds. We note that the developed strategy MV-BL yields a more diversified portfolio overall, while MV-Est-myopic and MV-Est-MPC exhibit a well-documented drawback of classical mean-variance analysis–namely, investing in a few assets, with a sharp transition between being too conservative (all in cash or a few bonds) and too risky (all in a few risky assets). In Figure [5](https://arxiv.org/html/2601.09127v1#S6.F5 "Figure 5 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach") we display the wealth process for these strategies, along with the equally weighted strategy 1/N. Key performance metrics are presented in Table [4](https://arxiv.org/html/2601.09127v1#S6.T4 "Table 4 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). As expected, smaller γ\gamma (less risk averse investing profile), yields larger returns but also larger standard deviations of the returns. The Sharpe Ratio and Gain-to-Loss ratio both decrease as γ\gamma increases.

The myopic strategy, MV-Est-myopic, exhibits the least desirable behavior from a robo-advising perspective, shifting from an “all-in-one” risky asset allocation to just a few assets within a narrow range of the risk-tolerance parameter γ\gamma. This behavior was consistently observed across other parameter sets. Consequently, we exclude this strategy from the analysis presented below and do not recommend it for any robo-advisor aiming to implement a robust and comprehensive system.

![Refer to caption](weights_gamma2025-12-29-19-34.png)


Figure 3: Portfolio weights for the mean-variance strategies MV-Est-MPC (top row) and MV-BL (bottom row) with risk aversion coefficient γ∈{0.01,0.1,1,5,10}\gamma\in\{0.01,0.1,1,5,10\}.

![Refer to caption](weights_gamma2025-12-29-19-41.png)


Figure 4: Portfolio weights for the mean-variance strategies MV-Est-MPC (top row) and MV-BL (bottom row) with risk aversion coefficient γ∈{0.5,0.7,1,1.5,2}\gamma\in\{0.5,0.7,1,1.5,2\}.

![Refer to caption](wealths_gamma2025-12-29-19-41.png)


Figure 5: Portfolio wealth for the mean-variance strategies MV-EST-MPC (left panel) and MV-BL (right panel) with γ∈{0.5,0.7,1,1.5,2}\gamma\in\{0.5,0.7,1,1.5,2\}, and for equally weighted portfolio 1/N.



|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mean | StDev | MaxDD | SR | GLR | CalmR | Turnover |
| γ=0.5\gamma=0.5 | | | | | | |  |
| M-BL | 0.121 | 0.166 | 0.279 | 0.724 | 0.151 | 0.431 | 0.887 |
| MV-Est-myopic | 0.161 | 0.217 | 0.350 | 0.743 | 0.137 | 0.461 | 0.190 |
| MV-Est-MPC | 0.152 | 0.210 | 0.344 | 0.723 | 0.135 | 0.441 | 0.416 |
| 1/N | 0.051 | 0.129 | 0.240 | 0.398 | 0.094 | 0.214 | – |
| SP500 | 0.150 | 0.215 | 0.339 | 0.701 | 0.137 | 0.443 | – |
| γ=0.7\gamma=0.7 | | | | | | |  |
| M-BL | 0.095 | 0.137 | 0.234 | 0.693 | 0.155 | 0.405 | 0.988 |
| MV-Est-myopic | 0.161 | 0.217 | 0.350 | 0.742 | 0.136 | 0.460 | 0.207 |
| MV-Est-MPC | 0.124 | 0.189 | 0.334 | 0.656 | 0.130 | 0.372 | 0.845 |
| γ=1\gamma=1 | | | | | | |  |
| M-BL | 0.065 | 0.106 | 0.188 | 0.615 | 0.141 | 0.346 | 0.733 |
| MV-Est-myopic | 0.152 | 0.210 | 0.344 | 0.723 | 0.135 | 0.441 | 0.431 |
| MV-Est-MPC | 0.093 | 0.161 | 0.336 | 0.580 | 0.129 | 0.278 | 1.134 |
| γ=1.5\gamma=1.5 | | | | | | |  |
| M-BL | 0.040 | 0.085 | 0.165 | 0.468 | 0.115 | 0.240 | 0.644 |
| MV-Est-myopic | 0.116 | 0.183 | 0.334 | 0.635 | 0.128 | 0.348 | 0.979 |
| MV-Est-MPC | 0.058 | 0.138 | 0.337 | 0.418 | 0.106 | 0.171 | 1.501 |
| γ=2\gamma=2 | | | | | | |  |
| M-BL | 0.030 | 0.078 | 0.157 | 0.381 | 0.098 | 0.190 | 0.569 |
| MV-Est-myopic | 0.093 | 0.161 | 0.336 | 0.577 | 0.128 | 0.277 | 1.155 |
| MV-Est-MPC | 0.041 | 0.119 | 0.310 | 0.345 | 0.093 | 0.133 | 1.299 |

Table 4: Performance metrics for the MV strategies with various γ\gamma.

#### 6.4.2 Risk attitude parameter γR\gamma\_{R} in MRB and impact coefficient ϕ\phi

The sensitivity coefficient ϕ\phi aims to capture the level at which the penalty term in the MRB is enforced. In Figure [6](https://arxiv.org/html/2601.09127v1#S6.F6 "Figure 6 ‣ 6.4.2 Risk attitude parameter 𝛾_𝑅 in MRB and impact coefficient ϕ ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach") we present the optimal portfolio weights for a series of values of ϕ\phi, and fixed γR=0.5\gamma\_{R}=0.5. While there is some variability in the portfolio composition for smaller values of ϕ\phi, the results stabilize for ϕ>0.05\phi>0.05. In what follows, we take ϕ=0.1\phi=0.1 or ϕ=0.05\phi=0.05.

![Refer to caption](weights_phi2025-12-29-22-18.png)


Figure 6: Portfolio weights for the MRB-BL for various sensitivity coefficient ϕ\phi.

We recall that in the MRB-BL strategy the parameter γR\gamma\_{R} plays the role of a risk attitude coefficient, by shifting the risk in the weights bib\_{i} appearing the MRB penalty term towards bonds with increasing values of γR\gamma\_{R}. This characteristic feature is confirmed in Figure [3](https://arxiv.org/html/2601.09127v1#S6.F3a "Figure 3 ‣ 6.4.1 Risk attitude parameter 𝛾 in MV criteria ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach") for a wide range of values γR∈{0.001,0.005,0.01,0.1,0.05,1,1.5,2,5,10}\gamma\_{R}\in\{0.001,0.005,0.01,0.1,0.05,1,1.5,2,5,10\}. By visual inspection, we note that the portfolios’ composition varies for γR\gamma\_{R} in the range (0.01,1)(0.01,1), while remains stable for smaller or larger values. Optimal portfolio weights for γR\gamma\_{R} on a finer grid around 0.5 are presented in Figure [8](https://arxiv.org/html/2601.09127v1#S6.F8 "Figure 8 ‣ 6.4.2 Risk attitude parameter 𝛾_𝑅 in MRB and impact coefficient ϕ ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), along the wealth process of these portfolio shown in Figure [9](https://arxiv.org/html/2601.09127v1#S6.F9 "Figure 9 ‣ 6.4.2 Risk attitude parameter 𝛾_𝑅 in MRB and impact coefficient ϕ ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Key performance metrics are presented in Table [5](https://arxiv.org/html/2601.09127v1#S6.T5 "Table 5 ‣ 6.4.2 Risk attitude parameter 𝛾_𝑅 in MRB and impact coefficient ϕ ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Sharpe Ratio and GLR are decreasing in γR\gamma\_{R}. Calman Ratio also decreases with few exceptions.

Similar to the MV strategies, portfolio wealth decreases as γR\gamma\_{R} increases, reflecting higher investor risk aversion. However, the magnitude of these changes is substantially smaller. We further emphasize that the optimal weights πτ\pi\_{\tau} under MRB–BL exhibit significantly less time variation compared to MV–BL. This is a distinctive feature of the method, stemming from the fact that the risk profiles of individual assets remain relatively stable over the investment horizon and that risk allocation in MRB is enforced at the individual-asset level. Consequently, for a fixed γR\gamma\_{R}, the portfolio structure remains largely stable over time.

From a robo-advising perspective, this relative stability has mixed implications. On the one hand, slowly varying portfolio weights may reduce portfolio turnover or transaction costs. We argue that these type of properties are better incorporated directly through the optimization criterion or via hard constraints; see Section [5.3](https://arxiv.org/html/2601.09127v1#S5.SS3 "5.3 Transaction costs ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach") and [6.4.3](https://arxiv.org/html/2601.09127v1#S6.SS4.SSS3 "6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Moreover, reduced sensitivity to changing forecasts may limit the responsiveness of the allocation to evolving market conditions. These considerations suggest that, while MRB-SMPC strategy exhibit appealing structural properties, they should be combined with other mechanism when deployed in practical robo-advising systems.

![Refer to caption](weights_gammaRP2025-12-29-19-54.png)


Figure 7: Portfolio weights for the MRB-BL strategy for risk attitude coefficient γR∈{0.001,0.005,0.01,0.1,0.5,1,1.5,2,5,10}\gamma\_{R}\in\{0.001,0.005,0.01,0.1,0.5,1,1.5,2,5,10\}.

![Refer to caption](weights_gammaRP2025-12-29-20-10.png)


Figure 8: Portfolio weights for the MRB-BL strategy for risk attitude coefficient γR∈{0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1}\gamma\_{R}\in\{0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1\}.

![Refer to caption](wealths_gammaRP2025-12-29-20-10.png)


Figure 9: Portfolio wealth for the MRB-BL strategy with γR∈{0.5,0.7,1.5,2}\gamma\_{R}\in\{0.5,0.7,1.5,2\}, and for equally weighted portfolio 1/N.



| γR\gamma\_{R} | Mean | StDev | MaxDD | SR | GLR | CalmR | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.001 | 0.087 | 0.184 | 0.327 | 0.471 | 0.107 | 0.266 | 0.311 |
| 0.005 | 0.086 | 0.184 | 0.325 | 0.466 | 0.106 | 0.264 | 0.321 |
| 0.01 | 0.085 | 0.184 | 0.328 | 0.459 | 0.106 | 0.258 | 0.334 |
| 0.1 | 0.077 | 0.169 | 0.306 | 0.455 | 0.105 | 0.251 | 0.299 |
| 0.3 | 0.062 | 0.146 | 0.276 | 0.422 | 0.099 | 0.223 | 0.222 |
| 0.5 | 0.055 | 0.133 | 0.248 | 0.413 | 0.098 | 0.222 | 0.176 |
| 0.7 | 0.048 | 0.126 | 0.233 | 0.382 | 0.093 | 0.206 | 0.270 |
| 0.9 | 0.044 | 0.119 | 0.229 | 0.368 | 0.091 | 0.192 | 0.289 |
| 1 | 0.045 | 0.115 | 0.216 | 0.394 | 0.096 | 0.211 | 0.239 |
| 1.5 | 0.036 | 0.106 | 0.210 | 0.337 | 0.082 | 0.170 | 0.218 |
| 2 | 0.032 | 0.101 | 0.208 | 0.316 | 0.077 | 0.154 | 0.181 |
| 5 | 0.024 | 0.092 | 0.205 | 0.257 | 0.063 | 0.115 | 0.182 |
| 10 | 0.020 | 0.087 | 0.203 | 0.223 | 0.056 | 0.096 | 0.170 |

Table 5: Performance metrics for the MRB-BL strategy with various γR\gamma\_{R}.

#### 6.4.3 Transaction cost coefficient η\eta and turnover constraint bound δ\delta

We recall that both the transaction cost penalty term η⋅T​C​(z)\eta\cdot TC(z) in the criteria and the turnover constraint ‖πτ+1−πτ‖1≤δ\|\pi\_{\tau+1}-\pi\_{\tau}\|\_{1}\leq\delta are
meant to control the magnitude of the overall transaction costs; see Section [5.3](https://arxiv.org/html/2601.09127v1#S5.SS3 "5.3 Transaction costs ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

We start by analyzing the effect of the transaction cost scaling factor η\eta in the criteria, while keeping δ=+∞\delta=+\infty. In Figure [10](https://arxiv.org/html/2601.09127v1#S6.F10 "Figure 10 ‣ 6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we present the portfolio weights for different values of η\eta, while in Figure [12](https://arxiv.org/html/2601.09127v1#S6.F12 "Figure 12 ‣ 6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), left panel, we plot the total turnover for this strategy as function of η\eta.
With increasing η\eta, the portfolio structure changes less in time, and the total turnover decreases and vanishing for η>0.05\eta>0.05.

On the other hand, as illustrated in Figure [11](https://arxiv.org/html/2601.09127v1#S6.F11 "Figure 11 ‣ 6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), the portfolio weights under the MRB-BL strategy–and the corresponding turnover shown in the right panel of Figure [12](https://arxiv.org/html/2601.09127v1#S6.F12 "Figure 12 ‣ 6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach")–remain essentially unchanged as η\eta varies.

![Refer to caption](weights_eta_etaMV2025-12-29-23-08.png)


Figure 10: Portfolio weights for the MV-BL strategy with
  
η∈{0,10−6,10−4,0.001,0.003,0.005,0.007,0.01,0.03,0.05}\eta\in\{0,10^{-6},10^{-4},0.001,0.003,0.005,0.007,0.01,0.03,0.05\}.

![Refer to caption](weights_eta_etaRP2025-12-29-23-08.png)


Figure 11: Portfolio weights for the MRB-BL strategy with
  
η∈{0,0.1,1,5,10,50,100,500,1000,2000}\eta\in\{0,0.1,1,5,10,50,100,500,1000,2000\}.



![Refer to caption](weights_etaeta_turnoverMV2025-12-29-23-08.png)

![Refer to caption](weights_etaeta_turnoverRP2025-12-29-23-08.png)

Figure 12: Turnover for MV-BL (left) and MRB-BL (righ) as function of η\eta.

Next, we examine sensitivity with respect to δ\delta, while fixing η=0\eta=0. In both strategies, the profile is similar: as δ\delta decreases, turnover declines and the portfolio gradually converges to a static allocation. Conversely, as δ\delta increases, the portfolio in both cases progressively approaches the unconstrained allocation; see Figures [13](https://arxiv.org/html/2601.09127v1#S6.F13 "Figure 13 ‣ 6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach")–[14](https://arxiv.org/html/2601.09127v1#S6.F14 "Figure 14 ‣ 6.4.3 Transaction cost coefficient 𝜂 and turnover constraint bound 𝛿 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

In the context of robo-advising, these results suggest that for the MV-BL strategy, either soft transaction cost penalties or turnover constraints can be used effectively to control trading activity, as both approaches lead to similar portfolio behavior. In contrast, for the MRB-BL strategy, soft constraints are largely ineffective, and one must rely on hard constraints on turnover. This highlights the importance of selecting constraint types that are compatible with the underlying optimization objective when designing automated portfolio management rules.

![Refer to caption](weights_delta_deltaMV2025-12-29-23-23.png)


Figure 13: Portfolio weights for the mean-variance strategy MV-BL with
  
δ∈{0.001,0.003,0.005,0.008,0.01,0.03,0.05,0.08,0.1,0.15}\delta\in\{0.001,0.003,0.005,0.008,0.01,0.03,0.05,0.08,0.1,0.15\}.

![Refer to caption](weights_delta_deltaRP2025-12-29-23-23.png)


Figure 14: Portfolio weights for the mean-risk-budgeting strategy MRB-BL with
  
δ∈{0.001,0.003,0.005,0.008,0.01,0.03,0.05,0.08,0.1,0.15}\delta\in\{0.001,0.003,0.005,0.008,0.01,0.03,0.05,0.08,0.1,0.15\}.



![Refer to caption](weights_deltadelta_turnoverMV2025-12-29-23-23.png)

![Refer to caption](weights_deltadelta_turnoverRP2025-12-29-23-23.png)

Figure 15: Turnover for MV-BL (left) and MRB-BL (righ) as function of δ\delta.

#### 6.4.4 SMPC rolling horizon parameter HH

We now turn our attention to the rolling horizon parameter HH—one of the central components of the SMPC methodology—which is frequently claimed in applied studies to play a critical role in the performance of the underlying controlled system.

In Figure [16](https://arxiv.org/html/2601.09127v1#S6.F16 "Figure 16 ‣ 6.4.4 SMPC rolling horizon parameter 𝐻 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), we display the portfolio weights for the MV-BL and MRB-BL strategies for values of HH ranging from 1 to 25, with γ=0.75\gamma=0.75, γR=0.5\gamma\_{R}=0.5, ϕ=0.1\phi=0.1, δ=∞\delta=\infty, and η=0\eta=0. Similar outcomes were consistently observed for other parameter configurations of γ\gamma, γR\gamma\_{R}, δ\delta, η\eta, and ϕ\phi. For the MV-BL strategy, performance is stable and optimized for HH in the range 5–7, with no meaningful improvements for H>7H>7.

For larger values of HH, the optimization problem at each rebalancing step involves more decision variables and therefore requires additional computation time. While this increase in complexity is negligible for a single portfolio, it may become relevant when deploying the strategy across a large number of portfolios, as is typically the case in large-scale robo-advisory systems. For this reason, we fix H=7H=7 as the default value in all subsequent experiments.

In contrast, the performance of the MRB-BL strategy remains essentially unchanged across all considered values of HH, including the myopic case H=1H=1. This indicates that, while the MPC framework combined with HMM and BL forecasts enhances performance under the MV criterion, it provides limited additional benefit for the MRB objective.

![Refer to caption](weights_H_HMV2025-12-29-23-36.png)

![Refer to caption](weights_H_HRP2025-12-29-23-36.png)

Figure 16: Portfolio weights for MV-BL (top two rows) and MRB-BL (bottom two rows) for H=1,3,5,7,9,10,12,15,20,25.H=1,3,5,7,9,10,12,15,20,25.

#### 6.4.5 Time changing risk attitude parameters γ\gamma and γR\gamma\_{R}

In this section we illustrate how time varying risk attitude parameter affects the portfolios’ weights; see also Section [5.1](https://arxiv.org/html/2601.09127v1#S5.SS1 "5.1 Risk profiling ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). We take ϕ=0.01,η=0,δ=+∞\phi=0.01,\eta=0,\delta=+\infty.
Static profiles, with γt,γR,t\gamma\_{t},\gamma\_{R,t} constant in time, have been displayed in the previous section. The lifecyle profile starts with risk tolerance parameters γ0=0.5\gamma\_{0}=0.5 and γR,0=0.1\gamma\_{R,0}=0.1 and increases them linearly to γT−1=γR,T−1=2\gamma\_{T-1}=\gamma\_{R,T-1}=2. The portfolios’ dynamics are shown in Figure [17](https://arxiv.org/html/2601.09127v1#S6.F17 "Figure 17 ‣ 6.4.5 Time changing risk attitude parameters 𝛾 and 𝛾_𝑅 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). As expected, in both cases the porfolios shift toward a more risk averse one. Notably, MV-BL just increases the weights of one MUB while decreasing the holding of VTI, visably linearly, while MRB-BL rembalences all assets, putting more weights on all four bonds.

In this section, we illustrate how time-varying risk attitude parameters affect portfolio weights; see also Section [5.1](https://arxiv.org/html/2601.09127v1#S5.SS1 "5.1 Risk profiling ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). Throughout this experiment, we set ϕ=0.01\phi=0.01, η=0\eta=0, and δ=+∞\delta=+\infty. Static profiles, in which γt\gamma\_{t} and γR,t\gamma\_{R,t} are constant over time, were analyzed in the previous section.

The lifecycle profile starts with risk tolerance parameters γ0=0.5\gamma\_{0}=0.5 and γR,0=0.1\gamma\_{R,0}=0.1, which are then increased linearly to γT−1=γR,T−1=2\gamma\_{T-1}=\gamma\_{R,T-1}=2. The resulting portfolio dynamics are shown in Figure [17](https://arxiv.org/html/2601.09127v1#S6.F17 "Figure 17 ‣ 6.4.5 Time changing risk attitude parameters 𝛾 and 𝛾_𝑅 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). As expected, both strategies shift toward more risk-averse allocations over time. Notably, the MV-BL strategy adjusts primarily along a single dimension, gradually increasing the allocation to MUB while correspondingly reducing exposure to VTI in an almost linear fashion. In contrast, the MRB-BL strategy actively rebalances across all assets, systematically increasing allocations to all bond instruments.

We also conduct an experiment under a noisy risk-attitude profile, where γ\gamma is sampled independently at each time step from the set {0.5,0.7,1,1.5,2}\{0.5,0.7,1,1.5,2\} and, correspondingly, γR\gamma\_{R} from the set {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1}\{0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1\}. The results are shown in Figure [18](https://arxiv.org/html/2601.09127v1#S6.F18 "Figure 18 ‣ 6.4.5 Time changing risk attitude parameters 𝛾 and 𝛾_𝑅 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach").

In the absence of trading constraints, the portfolio weights fluctuate erratically and lack a coherent structure. Imposing a moderate turnover constraint (δ=0.05\delta=0.05) significantly stabilizes the dynamics: the MRB-BL strategy behaves comparably to the case of a fixed risk attitude, indicating robustness to preference noise. In contrast, the MV-BL strategy remains highly sensitive to past realizations of γ\gamma, exhibiting no clear or stable pattern and instead reflecting persistent time spillover effects.

![Refer to caption](weights_time-var-gamma-linear-11_gamma-linear.png)


Figure 17: Portfolio weights for the MV-BL and MRB-BL strategies under a linearly time-varying risk attitude parameter γ\gamma.



![Refer to caption](weights_time-var-gamma-random-11_gamma-linear.png)

![Refer to caption](weights_time-var-gamma-random-11_gamma-linear-delta5.png)

Figure 18: Portfolio weights for the MV-BL and MRB-BL strategies under a randomly varying risk attitude parameter γ\gamma. Top panel: unconstrained trading (δ=+∞\delta=+\infty); bottom panel: turnover-constrained case with δ=0.05\delta=0.05.

#### 6.4.6 Target portfolio

We also perform a series of experiments imposing a practically relevant target portfolio constraint; see Section [5.2](https://arxiv.org/html/2601.09127v1#S5.SS2 "5.2 Allocation target constraints ‣ 5 Risk profiling, allocation targets and trading constraints ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). As in the previous section, we set the target risk attitude coefficient to γtarget=0\gamma\_{\mathrm{target}}=0, with all other parameters as in Section [6.4.5](https://arxiv.org/html/2601.09127v1#S6.SS4.SSS5 "6.4.5 Time changing risk attitude parameters 𝛾 and 𝛾_𝑅 ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"). The target constraint is activated over the final 14 rebalancing steps (=2​H=2H).

The results are presented in Figure [19](https://arxiv.org/html/2601.09127v1#S6.F19 "Figure 19 ‣ 6.4.6 Target portfolio ‣ 6.4 Analysis of results ‣ 6 Numerical experiment on market data ‣ Robo-Advising in Motion: A Model Predictive Control Approach"), where γ\gamma and γR\gamma\_{R} are either held constant (top panel) or vary linearly over time (bottom panel). For the static risk profile, the effect of the constraint is clearly visible: as maturity approaches, the portfolio weights adjust smoothly and monotonically to reach the prescribed target allocation.

In contrast, under a lifecycle profile for γ\gamma, the MV-BL strategy yields a portfolio that remains more diversified than in the unconstrained case, indicating a nontrivial interaction between time-varying risk attitudes and the target portfolio constraint. From a robo-advising perspective, this suggests that a prudent modeling approach is to combine the MV-BL framework with explicit target portfolio constraints and time-varying risk preferences, allowing for gradual risk de-risking while maintaining diversification and control near the investment horizon.

![Refer to caption](weights_time-var-gamma-target-constantt-constant-gamma.png)

![Refer to caption](weights_time-var-gamma-target-linearget-linear-gamma.png)

Figure 19: The weights for the MV-BL and MRB-BL strategies, under target portfolio and time varying risk attitude coefficient. Top panel: unconstrained trading (δ=+∞\delta=+\infty); bottom panel: turnover-constrained case with δ=0.05\delta=0.05.

## 7 Concluding remarks

Overall, the numerical analysis highlights substantial differences in how MV-Est-myopic, MV-Est-MPC, MV-BL and MRB-BL strategies respond to changes in risk attitudes, transaction cost controls, and MPC design parameters. Within the mean–variance framework, incorporating BL views and SMPC leads to more diversified and stable portfolios compared to classical estimated MV approaches, which exhibit sharp allocation switches and poor robustness with respect to the risk aversion parameter. At the same time, MV-BL remains sensitive to noisy or rapidly changing risk profiles, making explicit turnover constraints and target portfolio mechanisms essential for stabilizing portfolio dynamics in practical robo-advising implementations.

In contrast, the MRB-BL strategy produces markedly smoother and more stable allocations across a wide range of parameter choices, including γR\gamma\_{R}, η\eta, and HH. While this structural stability may reduce turnover, it also limits responsiveness to market forecasts and renders soft transaction cost penalties largely ineffective, necessitating the use of hard constraints when trading activity must be controlled. Moreover, the limited sensitivity of MRB-BL to the MPC horizon suggests that the additional modeling and computational complexity of SMPC delivers relatively modest gains under risk-budgeting objectives.

Taken together, these findings suggest that a prudent robo-advising design should align the choice of optimization criterion, constraint structure, and preference modeling with the desired balance between adaptability and stability. In particular, MV-BL combined with explicit turnover or target portfolio constraints and time-varying risk attitudes offers a flexible and controllable framework, while MRB-based approaches may be better suited to settings where portfolio stability is prioritized and preference dynamics are slow or tightly regulated.

## Acknowledgments

The authors express their sincere gratitude to Tao Chen and Areski Cousin for their valuable input and support during the early phases of developing this manuscript and the underlying Python code. The authors acknowledge support from the National Science Foundation grant DMS-1907568. IC also acknowledges partial support from the National Science Foundation grant DMS-2407549.

## References

* [AAL25]

  Farida Akhtar, Shumi Akhtar, and Maryam Laeeq.
  Evolution of Robo-Advisors: A literature review and future
  research agenda.
  International Journal of Consumer Studies, 49(6), October 2025.
* [ACRLS20]

  Humoud Alsabah, Agostino Capponi, Octavio Ruiz Lacedelli, and Matt Stern.
  Robo-advising: Learning investors risk preferences via portfolio
  choices.
  Journal of Financial Econometrics, 19(2):369–392, January
  2020.
* [AS22]

  Miquel Noguer i Alonso and Sonam Srivastava.
  Deep reinforcement learning for asset allocation in US equities.
  arXiv:2010.04404, October 2022.
* [BBD+17]

  Stephen Boyd, Enzo Busseti, Steven Diamond, Ronald N. Kahn, Kwangmoo Koh, Peter
  Nystrup, and Jan Speth.
  Multi-period trading via convex optimization.
  Foundations and Trends in Optimization, 3(1):1–76, 2017.
* [BCC21]

  Tomasz R. Bielecki, Tao Chen, and Igor Cialenco.
  Time-inconsistent Markovian control problems under model
  uncertainty with application to the mean-variance portfolio selection.
  International Journal of Theoretical and Applied Finance,
  24(01):2150003, feb 2021.
* [BL92]

  Fischer Black and Robert Litterman.
  Global portfolio optimization.
  Financial Analysts Journal, 48(5):28–43, sep 1992.
* [BLW18]

  Mikhail Beketov, Kevin Lehmann, and Manuel Wittke.
  Robo advisors: quantitative methods inside the robots.
  Journal of Asset Management, 19(6):363–370, September 2018.
* [BM14]

  Tomas Björk and Agatha Murgoci.
  A theory of Markovian time-inconsistent stochastic control in
  discrete time.
  Finance and Stochastics, 18(3):545–592, 2014.
* [BS78]

  Dimitri P. Bertsekas and Steven E. Shreve.
  Stochastic Optimal Control: The Discrete-Time Case.
  Academic Press, 1978.
* [BS22]

  Ronil Barua and Anil K. Sharma.
  Dynamic Black-Litterman portfolios with views derived via
  CNN-BiLSTM predictions.
  Finance Research Letters, 49:103111, oct 2022.
* [CK18]

  Giorgio Costa and Roy H. Kwon.
  Risk parity portfolio optimization under a Markov regime-switching
  framework.
  Quantitative Finance, 19(3):453–471, aug 2018.
* [CLQS22]

  Xiang-Yu Cui, Duan Li, Xiao Qiao, and Moris S. Strub.
  Risk and potential: An asset allocation framework with applications
  to robo-advising.
  Journal of the Operations Research Society of China,
  10(3):529–558, June 2022.
* [CÓZ22]

  Agostino Capponi, Sveinn Ólafsson, and Thaleia Zariphopoulou.
  Personalized Robo-Advising: Enhancing investment through client
  interaction.
  Management Science, 68(4):2485–2512, apr 2022.
* [DJKX21]

  Min Dai, Hanqing Jin, Steven Kou, and Yuhong Xu.
  Robo-advising: a dynamic mean-variance approach.
  Digital Finance, 3(2):81–97, jun 2021.
* [DR21]

  Francesco D’Acunto and Alberto G. Rossi.
  Robo-Advising, pages 725–749.
  Springer International Publishing, Cham, 2021.
* [GL16]

  Alois Geyer and Katarína Lucivjanská.
  The Black-Litterman approach and views from predictive
  regressions: Theory and implementation.
  The Journal of Portfolio Management, 42(4):38–48, may 2016.
* [Hew20]

  Lukas Hewing.
  Predictive Control of Uncertain Systems: Learning-based
  and Stochastic Model Predictive Control.
  PhD thesis, ETH Zurich, 2020.
* [HHN21]

  Nils Helms, Reinhold Hölscher, and Matthias Nelde.
  Automated investment management: Comparing the design and performance
  of international robo-managers.
  European Financial Management, 28(4):1028–1078, September
  2021.
* [HST17]

  Richard D.F. Harris, Evarist Stoja, and Linzhi Tan.
  The dynamic Black-Litterman approach to asset allocation.
  European Journal of Operational Research, 259(3):1085–1096,
  jun 2017.
* [KC16]

  Basil Kouvaritakis and Mark Cannon.
  Model Predictive Control.
  Springer International Publishing, 2016.
* [KUA19]

  Mahmut Kara, Aydin Ulucan, and Kazim Baris Atici.
  A hybrid approach for generating investor views in
  Black–Litterman model.
  Expert Systems with Applications, 128:256–270, aug 2019.
* [LN00]

  Duan Li and Wan-Lung Ng.
  Optimal dynamic portfolio selection: Multiperiod mean-variance
  formulation.
  Mathematical Finance, 10(3):387–406, July 2000.
* [LUM21]

  Xiaoyue Li, A. Sinem Uysal, and John M. Mulvey.
  Multi-period portfolio optimization using model predictive control
  with mean-variance and risk parity frameworks.
  European Journal of Operational Research, 299(3):1158–1176,
  June 2021.
* [Meu08]

  Attilio Meucci.
  The Black-Litterman approach: Original model and extensions.
  SSRN Electronic Journal, 2008.
* [NBLM18]

  Peter Nystrup, Stephen Boyd, Erik Lindström, and Henrik Madsen.
  Multi-period portfolio selection with drawdown control.
  Annals of Operations Research, 282(1-2):245–271, jun 2018.
* [NML17]

  Peter Nystrup, Henrik Madsen, and Erik Lindström.
  Dynamic portfolio optimization across hidden market regimes.
  Quantitative Finance, 18(1):83–95, jul 2017.
* [OK21]

  Razvan Oprisor and Roy Kwon.
  Multi-period portfolio optimization with investor views under regime
  switching.
  Journal of Risk and Financial Management, 14(1):3, December
  2021.
* [RFM21]

  Hadi Rezaei, Hamidreza Faaljou, and Gholamreza Mansourfar.
  Intelligent asset allocation using predictions of deep frequency
  decomposition.
  Expert Systems with Applications, 186:115715, dec 2021.
* [RL19]

  Saša V. Raković and William S. Levine, editors.
  Handbook of Model Predictive Control.
  Springer International Publishing, 2019.
* [RMD20]

  James B. Rawlings, David Q. Mayne, and Moritz M. Diehl.
  Model Predictive Control Theory, Computation, and Design.
  Nob Hill Publishing, Santa Barbara, California, 2020.
* [Ron16]

  Thierry Roncalli.
  Introduction to Risk Parity and Budgeting.
  Taylor & Francis Group, 2016.
* [RU20]

  Alberto G. Rossi and Stephen P. Utkus.
  The needs and wants in financial advice: Human versus robo-advising.
  SSRN Electronic Journal, 2020.
* [WSK16]

  Dhoriva Urwatul Wutsqa, Retno Subekti, and Rosita Kusumawati.
  Radial basis function neural network for views prediction on
  Black-Litterman model.
  Journal of Innovative Technology and Education, 3:71–78, 2016.
* [Yan21]

  Shuhao Yan.
  Robust and Stochastic Receding Horizon Control.
  PhD thesis, University of Oxford, 2021.
* [ZMZ09]

  W. Zucchini, Iain L. MacDonald, and Walter Zucchini.
  Hidden Markov Models for Time Series An Introduction Using R.
  Taylor & Francis Group, 2009.