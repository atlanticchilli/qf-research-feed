---
authors:
- Jiacheng Wu
doc_id: arxiv:2511.11909v1
family_id: arxiv:2511.11909
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory
url_abs: http://arxiv.org/abs/2511.11909v1
url_html: https://arxiv.org/html/2511.11909v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jiacheng Wu

## Abstract

A theoretical model of systemic-risk propagation of financial market is analyzed for stability. The state equation is an unsteady diffusion equation with a nonlinear logistic growth term, where the diffusion process captures the spread of default stress between interconnected financial entities and the reaction term captures the local procyclicality of financial stress. The stabilizing controller synthesis includes three steps: First, the algebraic Riccati equation is derived for the linearized system equation, the solution of which provides an exponentially stabilizing controller. Second, the nonlinear system is treated as a linear system with the nonlinear term as its forcing term. Based on estimation of the solutions for linearized equations and the contraction mapping theorem, unique existence of the solution for the nonlinear system equation is proved. Third, local asymptotic stability of the nonlinear system is obtained by considering the corresponding Hamilton-Jacobi equation. In both the linearized and nonlinear systems, the resulting controllers ensure that the H∞H^{\infty} norms of the mappings from disturbance to the output are less than a predefined constant. Stabilizing conditions provide a new framework of achieving system-level financial risk managing goals via the synergy of decentralized components, which offers policy-relevant insights for governments, regulators and central banks to mitigate financial crises.

## 1 Introduction

Financial systems are complex networks of financial institutions and market participants where shocks of distress can propagate through dense webs of interconnections, amplifying localized disturbances into global crises [acemoglu2015systemic]. The 2008 global financial crisis and the subsequent contagion reaction underscores how seemingly uncorrelated financial entities can become deeply coupled via inter-bank exposure, linked balance-sheet and correlated asset holdings. Therefore, understanding the mechanism of risk propagation dynamics in terms of how distress spreads, amplifies, and potentially stabilizes [haldane2011systemic, battiston2012debtrank], is of great importance for policy-level risk mitigation and society-level financial security.

Traditional network-contagion model captures some features of financial systems by a network with financial institutions as nodes and exposure as weighed edge [gai2010contagion, allen2000financial]. However, such models often lack an explicit treatment of continuous time and spatial propagation mechanisms, which potentially poses difficulties for application of advanced mathematical tools to model the unsteady dynamics. Borrowing the ideas from information theory and epidemiology, diffusion is a natural mechanism to model the spread of financial stress across sectors, geographies, and asset classes through liquidity flows, information channels, and overlapping portfolios. On the other hand, local dynamics such as leverage feedback, liquidity spirals and credit contagion can further amplify the distress, which is also a key component to model financial networks [adrian2010liquidity, brunnermeier2009market, diamond1983bank].

To capture these dual features of diffusion and local dynamics, the following diffusion-reaction partial differential equation is used to model the time evolution of financial stress and its propagation through financial networks,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂t​s​(x,t)=Ds​∇2s+c2​s​(1−sS),\frac{\partial}{\partial t}s(x,t)=D\_{s}\nabla^{2}s+c\_{2}s\left(1-\frac{s}{S}\right), |  | (1) |

where s​(x,t)s(x,t) is the financial stress level at location xx and time tt, DsD\_{s} is the diffusion coefficient represents how tightly different financial institution is connected, and c2c\_{2} is the growth coefficient. Note that xx here represents spatial dimensions beyond geographic locations, and it can also represent generic distance between financial entities in the network. The first term on the right-hand side of equation ([1](https://arxiv.org/html/2511.11909v1#S1.E1 "In 1 Introduction ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) describes distress propagation through financial interconnections. The second term corresponds to local amplification of distress even without contagion. SS is the saturated value for the distress s​(x,t)s(x,t). The state equation ([1](https://arxiv.org/html/2511.11909v1#S1.E1 "In 1 Introduction ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) has two fixed points s​(x,t)=0s(x,t)=0 and s​(x,t)=Ss(x,t)=S. The equilibrium point s​(x,t)=0s(x,t)=0 corresponds to zero distress, which is desired but unstable, while s​(x,t)=Ss(x,t)=S corresponds to complete liquidation corresponding to financial crisis and this equilibrium is stable without intervention. Therefore, the goal is to stabilize the system equation ([1](https://arxiv.org/html/2511.11909v1#S1.E1 "In 1 Introduction ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) about its zero state to attenuate systemic financial distress.

Stability of linear partial differential equations is well understood using semigroup theory [hille1996functional, pazy2012semigroups]. The key idea is to consider the partial differential equation as an ordinary differential equation in a functional space and prove that the corresponding spatial operator generates an exponentially stable semigroup. In the case of nonlinear systems, stability properties usually need to leverage Lyapunov indirect method [lyapunov1992general, justus2008ecological, wu2016stability]. However, the theory is less well developed there, in particular for the case of partial differential state equations. Here, a novel method is proposed to handle the stabilizing controller synthesis problem for the specific nonlinear growth term in equation ([1](https://arxiv.org/html/2511.11909v1#S1.E1 "In 1 Introduction ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) by making use of the relationship between the nonlinear state equation and its linearized version. Optimal control theory is used to give the mathematical form of the stabilizing controller.

After formulating the control problem in Section [2](https://arxiv.org/html/2511.11909v1#S2 "2 Formulation of the control problem ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory"), the optimal control problem for the linearized system is considered in Section [3](https://arxiv.org/html/2511.11909v1#S3 "3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory"). Pontryagin’s minimum principle [pontryagin1962] is used to derive the algebraic Riccati equation, the solution of which gives the exact form of the stabilizing controller. Based on the resulting controller, it is proved that the H∞H^{\infty} norm of the mapping from the disturbance to the output is less than a preset constant. In section [4](https://arxiv.org/html/2511.11909v1#S4 "4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory"), the linearized system with additional forcing terms is considered. Second, the norm estimation for the solution is obtained with respect to the norm of the forcing terms. Third, by setting the nonlinear term in the state equation ([1](https://arxiv.org/html/2511.11909v1#S1.E1 "In 1 Introduction ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) to be the forcing term, the existence and uniqueness of the solution for the nonlinear state equation is proved based on the contraction mapping theorem. Finally, Pontryagin’s minimum problem is used again for the nonlinear optimal control problem to obtain the Hamilton-Jacobi equation, which is a nonlinear version of the Riccati equation. The feedback controller is synthesized based on the solution of the Hamilton-Jacobi equation, and local asymptotic stability is proved.

## 2 Formulation of the control problem

Consider the controlled state equation with control input u​(x,t)u(x,t) and disturbance w​(x,t)w(x,t),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂t​s​(x,t)=Ds​∇2s+c2​s​(1−sS)+B1​w​(x,t)+B2​u​(x,t),\frac{\partial}{\partial t}s(x,t)=D\_{s}\nabla^{2}s+c\_{2}s\left(1-\frac{s}{S}\right)+B\_{1}w(x,t)+B\_{2}u(x,t), |  | (2) |

where s​(x)∈H01​(Ω)s(x)\in H\_{0}^{1}(\Omega), and B1B\_{1} and B2B\_{2} are input operators of the disturbance and control input, respectively. Note that Ω\Omega is the control domain, which in this case is the landscape of distributed financial entities. The Neumann boundary conditions are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇s​x|x|​(x,t)|x∈Γ=0,\nabla s\left.\frac{x}{|x|}(x,t)~\right|\_{x\in\Gamma}=0, |  | (3) |

where Γ\Gamma is the boundary of the domain Ω\Omega. The homogeneous Neumann boundary condition enforces that there is no distress flux across the boundary. The initial condition is

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(x,0)=s0​(x),s(x,0)=s\_{0}(x), |  | (4) |

where s0s\_{0} represents the initial level of financial stress.

The partial differential system equation ([2](https://arxiv.org/html/2511.11909v1#S2.E2 "In 2 Formulation of the control problem ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) may be considered to an ordinary differential equation in the Sobolev space H01​(Ω)H\_{0}^{1}(\Omega), with w​(t)w(t) as the disturbance and u​(t)u(t) as the control input according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​s​(t)+Ds​A​s​(t)+F​(s​(t))=B1​w​(t)+B2​u​(t),\frac{d}{dt}s(t)+D\_{s}As(t)+F(s(t))=B\_{1}w(t)+B\_{2}u(t), |  | (5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​s:=−∇2s,As:=-\nabla^{2}s, |  | (6) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(s​(t))=F0​s​(t)+FN​(s​(t))=−c2​s+c2S​s2.F(s(t))=F\_{0}s(t)+F\_{N}(s(t))=-c\_{2}s+\frac{c\_{2}}{S}s^{2}. |  | (7) |

F0​s​(t)F\_{0}s(t) is the linear part of the function F​(s​(t))F(s(t)), and FN​(s​(t))F\_{N}(s(t)) is the nonlinear part. Therefore, the linearized state equation about the state s​(t)=0s(t)=0 is

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​s​(t)+Ds​A​s​(t)+F0​s​(t)=B1​w​(t)+B2​u​(t).\frac{d}{dt}s(t)+D\_{s}As(t)+F\_{0}s(t)=B\_{1}w(t)+B\_{2}u(t). |  | (8) |

Note that B1B\_{1} and B2B\_{2} are assumed to be bounded linear operators, and the operator AA with corresponding homogeneous Neumann boundary condition is a self-adjoint operator.

## 3 Optimal control for the linearized system

Before considering the full nonlinear state equation, a stability analysis of the corresponding linearized equation is carried out, the results of which will give one of the conditions of the controller synthesis for the nonlinear system.

### 3.1 Algebraic Riccatti equation

The linearized system is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​s​(t)+Ds​A​s​(t)+F0​s​(t)=B1​w​(t)+B2​u​(t),\frac{d}{dt}s(t)+D\_{s}As(t)+F\_{0}s(t)=B\_{1}w(t)+B\_{2}u(t), |  | (9) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(t)=C​s​(t)+D​u​(t).y(t)=Cs(t)+Du(t). |  | (10) |

Here, y​(t)y(t) denotes the output of the system, and CC and DD are bounded linear operators.
We construct the LQ optimal control problem for the linear system as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | supwinfu12​∫0+∞(|y​(t)|2−γ2​|w​(t)|2)​𝑑t​subject to equations ([9](https://arxiv.org/html/2511.11909v1#S3.E9 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and ([10](https://arxiv.org/html/2511.11909v1#S3.E10 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")),\sup\limits\_{w}\inf\limits\_{u}\frac{1}{2}\int\limits\_{0}^{+\infty}(|y(t)|^{2}-\gamma^{2}|w(t)|^{2})dt~~~\mbox{subject to~equations (\ref{eq:linear\_state}) and (\ref{eq:linear\_output})}, |  | (11) |

where γ\gamma is a weight coefficient. Roughly speaking, the cost functional minimizes the influence from the disturbance on the output. Without loss of generality, we can set |y​(t)|2=|C​s​(t)|2+|u​(t)|2|y(t)|^{2}=|Cs(t)|^{2}+|u(t)|^{2}.

Now construct Pontryagin’s Hamiltonian for the system ([9](https://arxiv.org/html/2511.11909v1#S3.E9 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and ([10](https://arxiv.org/html/2511.11909v1#S3.E10 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(s,p,u,w)=⟨B1​w+B2​u−Ds​A​s−F0​s,p⟩−12​(|C​s|2+|u|2−γ2​|w|2),H(s,p,u,w)=\langle B\_{1}w+B\_{2}u-D\_{s}As-F\_{0}s,p\rangle-\frac{1}{2}(|Cs|^{2}+|u|^{2}-\gamma^{2}|w|^{2}), |  | (12) |

where ⟨⋅,⋅⟩\left<\cdot,\cdot\right> represents the inner product, and p​(t)p(t) is the Lagrange multiplier used to adjoin the state equation ([9](https://arxiv.org/html/2511.11909v1#S3.E9 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) to the cost functional ([11](https://arxiv.org/html/2511.11909v1#S3.E11 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")).
Based on Pontryagin’s minimum principle, an extremum is reached when

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂H∂u=0\displaystyle\frac{\partial H}{\partial u}=0 | ∂H∂w=0,\displaystyle\displaystyle\frac{\partial H}{\partial w}=0, |  |  | (13) |

which yields

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | u=B2∗​p,\displaystyle u=B\_{2}^{\*}p, | w=−1γ2​B1∗​p,\displaystyle\displaystyle w=-\frac{1}{\gamma^{2}}B\_{1}^{\*}p, |  |  | (14) |

respectively, where asterisks denote adjoint operators. The state equation and adjoint equation can be obtained from

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂H∂p=s˙,∂H∂s=−p˙,\frac{\partial H}{\partial p}=\dot{s},~~~~\frac{\partial H}{\partial s}=-\dot{p}, |  | (15) |

respectively. Therefore, the Hamiltonian system is formulated as

|  |  |  |
| --- | --- | --- |
|  | s˙+Ds​A​s+F0​s=B1​w+B2​u,\displaystyle\dot{s}+D\_{s}As+F\_{0}s=B\_{1}w+B\_{2}u, |  |
|  |  |  |
| --- | --- | --- |
|  | p˙−Ds​A​p−F0∗​p=C∗​C​s,\displaystyle\dot{p}-D\_{s}Ap-F\_{0}^{\*}p=C^{\*}Cs, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(0)=s0,p​(+∞)=0.\displaystyle s(0)=s\_{0},~~p(+\infty)=0. |  | (16) |

Because the system is linear, assume the invariant manifolds of the Hamiltonian system are such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(t)=−P​s​(t),p(t)=-Ps(t), |  | (17) |

where P>0P>0 and is a self-adjoint bounded operator.

Because the system is autonomous, and the terminal time is not specified, H​(s,p)=0H(s,p)=0 for t>0t>0. Substituting equations ([14](https://arxiv.org/html/2511.11909v1#S3.E14 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and ([17](https://arxiv.org/html/2511.11909v1#S3.E17 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) into H​(s,p)=0H(s,p)=0 from equation ([12](https://arxiv.org/html/2511.11909v1#S3.E12 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨P​(Ds​A+F0)​s−12​C∗​C​s+12​P​B2​B2∗​P​s−12​γ2​P​B1​B1∗​P​s,s⟩=0,\left\langle P(D\_{s}A+F\_{0})s-\frac{1}{2}C^{\*}Cs+\frac{1}{2}PB\_{2}B\_{2}^{\*}Ps-\frac{1}{2\gamma^{2}}PB\_{1}B\_{1}^{\*}Ps,s\right\rangle=0, |  | (18) |

which gives the algebraic Riccati equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Ds​A+F0)−12​C∗​C+12​P​B2​B2∗​P−12​γ2​P​B1​B1∗​P=0.P(D\_{s}A+F\_{0})-\frac{1}{2}C^{\*}C+\frac{1}{2}PB\_{2}B\_{2}^{\*}P-\frac{1}{2\gamma^{2}}PB\_{1}B\_{1}^{\*}P=0. |  | (19) |

The solution for P>0P>0 defines the mathematical form of the stabilizing feedback controller u=−B2∗​P​su=-B\_{2}^{\*}Ps.

### 3.2 Stability of the linearized system with no disturbances

In order to prove stability of the linearized system with the no disturbances, that is, w=0w=0, first construct the Lyapunov function from the solution to the algebraic Riccati equation as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(s​(t))=12​⟨s,P​s⟩≥0.V(s(t))=\frac{1}{2}\left<s,Ps\right>\geq 0. |  | (20) |

Taking the time derivative of V​(s​(t))V(s(t)) along the trajectory of the linearized system gives

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​V​(s​(t))d​t\displaystyle\frac{dV(s(t))}{dt} | =\displaystyle= | ⟨s˙,d​V​(s)d​s⟩\displaystyle\left\langle\dot{s},\frac{dV(s)}{ds}\right\rangle |  | (21) |
|  |  | =\displaystyle= | ⟨B2​u−(Ds​A+F0)​s,P​s⟩\displaystyle\langle B\_{2}u-(D\_{s}A+F\_{0})s,Ps\rangle |  |
|  |  | =\displaystyle= | ⟨P​B2​u−P​(Ds​A+F0)​s,s⟩.\displaystyle\langle PB\_{2}u-P(D\_{s}A+F\_{0})s,s\rangle. |  |

Substituting u=B2∗​p=−B2∗​P​su=B\_{2}^{\*}p=-B\_{2}^{\*}Ps and the algebraic Riccati equation ([19](https://arxiv.org/html/2511.11909v1#S3.E19 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) into this equation requires

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​V​(s​(t))d​t\displaystyle\frac{dV(s(t))}{dt} | =\displaystyle= | ⟨−12​P​B2​B2∗​P​s−12​γ2​P​B1​B1∗​P​s−12​C∗​C​s,s⟩\displaystyle\left\langle-\frac{1}{2}PB\_{2}B\_{2}^{\*}Ps-\frac{1}{2\gamma^{2}}PB\_{1}B\_{1}^{\*}Ps-\frac{1}{2}C^{\*}Cs,s\right\rangle |  | (22) |
|  |  | =\displaystyle= | −12​|B2∗​P​s|2−12​γ2​|B1∗​P​s|2−12​|C​s|2\displaystyle-\frac{1}{2}|B\_{2}^{\*}Ps|^{2}-\frac{1}{2\gamma^{2}}|B\_{1}^{\*}Ps|^{2}-\frac{1}{2}|Cs|^{2} |  |
|  |  | ≤\displaystyle\leq | −m​|s|2,\displaystyle-m|s|^{2}, |  |

where m>0m>0. This result demonstrates the global exponential stability of the linearized system with w=0w=0
via the state feedback controller u=−B2∗​P​su=-B\_{2}^{\*}Ps, and that the operator −(Ds​A+F0+B2​B2∗​P)-(D\_{s}A+F\_{0}+B\_{2}B\_{2}^{\*}P) generates an exponentially stable semigroup. This result ensures the unique existence of the solution for the linearized system and will be used later to prove asymptotic stability of the nonlinear system.

### 3.3 Boundedness of the H∞H^{\infty} norm of the mapping from ww to yy

Once stability is assured for the linearized system with no disturbances, it is sought to demonstrate that the influence from disturbances on the output is smaller that γ\gamma. Consider the linearized system with zero initial condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​s​(t)+Ds​A​s​(t)+F0​s​(t)=B1​w​(t)+B2​u​(t),s​(0)=0.\frac{d}{dt}s(t)+D\_{s}As(t)+F\_{0}s(t)=B\_{1}w(t)+B\_{2}u(t),~~s(0)=0. |  | (23) |

Taking the time derivative of the Lyapunov function V​(s​(t))=12​⟨s,P​s⟩V(s(t))=\frac{1}{2}\langle s,Ps\rangle along the trajectory of equation ([23](https://arxiv.org/html/2511.11909v1#S3.E23 "In 3.3 Boundedness of the 𝐻^∞ norm of the mapping from 𝑤 to 𝑦 ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) gives

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​V​(s​(t))d​t\displaystyle\frac{dV(s(t))}{dt} | =\displaystyle= | ⟨s˙,P​s⟩\displaystyle\left\langle\dot{s},Ps\right\rangle |  | (24) |
|  |  | =\displaystyle= | ⟨B1​w+B2​u−(Ds​A+F0)​s,P​s⟩\displaystyle\langle B\_{1}w+B\_{2}u-(D\_{s}A+F\_{0})s,Ps\rangle |  |
|  |  | =\displaystyle= | ⟨P​B1​w+P​B2​u−P​(Ds​A+F0)​s,s⟩.\displaystyle\langle PB\_{1}w+PB\_{2}u-P(D\_{s}A+F\_{0})s,s\rangle. |  |

Substituting u=B2∗​p=−B2∗​P​su=B\_{2}^{\*}p=-B\_{2}^{\*}Ps and the algebraic Riccati equation ([19](https://arxiv.org/html/2511.11909v1#S3.E19 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) into this equation lead to
(note that we do not set w=−1γ2​B1∗​pw=-\frac{1}{\gamma^{2}}B\_{1}^{\*}p)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​V​(s​(t))d​t\displaystyle\frac{dV(s(t))}{dt} | =\displaystyle= | ⟨P​B1​w−12​P​B2​B2∗​P​s−12​γ2​P​B1​B1∗​P​s−12​C∗​C​s,s⟩\displaystyle\left\langle PB\_{1}w-\frac{1}{2}PB\_{2}B\_{2}^{\*}Ps-\frac{1}{2\gamma^{2}}PB\_{1}B\_{1}^{\*}Ps-\frac{1}{2}C^{\*}Cs,s\right\rangle |  | (25) |
|  |  | =\displaystyle= | ⟨P​B1​w,s⟩−12​|B2∗​P​s|2−12​γ2​|B1∗​P​s|2−12​|C​s|2\displaystyle\langle PB\_{1}w,s\rangle-\frac{1}{2}|B\_{2}^{\*}Ps|^{2}-\frac{1}{2\gamma^{2}}|B\_{1}^{\*}Ps|^{2}-\frac{1}{2}|Cs|^{2} |  |
|  |  | =\displaystyle= | −12​γ2​|w|2+⟨w,B1∗​P​s⟩−12​γ2​|B1∗​P​s|2+12​γ2​|w|2−12​|C​s|2−12​|u|2\displaystyle-\frac{1}{2}\gamma^{2}|w|^{2}+\langle w,B\_{1}^{\*}Ps\rangle-\frac{1}{2\gamma^{2}}|B\_{1}^{\*}Ps|^{2}+\frac{1}{2}\gamma^{2}|w|^{2}-\frac{1}{2}|Cs|^{2}-\frac{1}{2}|u|^{2} |  |
|  |  | =\displaystyle= | −12​γ2​|w−1γ2​B1∗​P​s|2+12​γ2​|w|2−12​|C​s|2−12​|u|2\displaystyle-\frac{1}{2}\gamma^{2}\left|w-\frac{1}{\gamma^{2}}B\_{1}^{\*}Ps\right|^{2}+\frac{1}{2}\gamma^{2}|w|^{2}-\frac{1}{2}|Cs|^{2}-\frac{1}{2}|u|^{2} |  |
|  |  | ≤\displaystyle\leq | 12​γ2​|w|2−12​|C​s|2−12​|u|2.\displaystyle\frac{1}{2}\gamma^{2}|w|^{2}-\frac{1}{2}|Cs|^{2}-\frac{1}{2}|u|^{2}. |  |

Integrate the equation above from t=0t=0 to t=+∞t=+\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(s​(+∞))−V​(s0)<∫0+∞(12​γ2​|w|2−12​|C​s|2−12​|u|2)​𝑑t.V(s(+\infty))-V(s\_{0})<\int\limits\_{0}^{+\infty}\left(\frac{1}{2}\gamma^{2}|w|^{2}-\frac{1}{2}|Cs|^{2}-\frac{1}{2}|u|^{2}\right)dt. |  | (26) |

For the initial condition s0=0s\_{0}=0, V​(s0)=0V(s\_{0})=0. Also, because V​(s​(+∞))≥0V(s(+\infty))\geq 0, it can be concluded that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0+∞(|C​s|2+|u|2)​𝑑t<γ2​∫0+∞|w|2​𝑑t.\int\limits\_{0}^{+\infty}(|Cs|^{2}+|u|^{2})dt<\gamma^{2}\int\limits\_{0}^{+\infty}|w|^{2}dt. |  | (27) |

This demonstrates that the H∞H^{\infty} norm of the mapping from the disturbance ww to the output yy is less than γ\gamma, which is the weight coefficient in the cost functional ([11](https://arxiv.org/html/2511.11909v1#S3.E11 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")).

## 4 Optimal control for the nonlinear system

In the linear case, the fact that the operator −(Ds​A+F0+B2​B2∗​P)-(D\_{s}A+F\_{0}+B\_{2}B\_{2}^{\*}P) generates an exponentially stable semigroup ensures the unique existence of the solution for the linearized state equation. However, this is generally not the case for the nonlinear situation. Therefore, the contraction mapping theorem will be used to prove existence and uniqueness of the solution for the nonlinear state equation.

### 4.1 Construct a linearized system with a forcing term and no disturbances

The idea here is to treat the nonlinear term as an additional forcing term in the linearized system. Adding a forcing term f​(t)f(t)
to the linearized state equation considered in the previous section gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​s​(t)+Ds​A​s​(t)+F0​s​(t)=B2​u​(t)+f​(t).\frac{d}{dt}s(t)+D\_{s}As(t)+F\_{0}s(t)=B\_{2}u(t)+f(t). |  | (28) |

Consider the following optimal control problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | infu12​∫0+∞(|C​s|2+|u|2+2​⟨g,s⟩)​𝑑t​subject to equation​([28](https://arxiv.org/html/2511.11909v1#S4.E28 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")),\inf\limits\_{u}\frac{1}{2}\int\limits\_{0}^{+\infty}(|Cs|^{2}+|u|^{2}+2\langle g,s\rangle)dt~~~\mbox{subject to~equation}~(\ref{eq:linear\_force\_state}), |  | (29) |

where g​(t)g(t) will be a forcing term in the differential adjoint equation.

Constructing the Pontryagin Hamiltonian yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(s,p,u)=⟨B2​u−Ds​A​s−F0​s+f,p⟩−12​(|C​s|2+|u|2+2​⟨g,s⟩).H(s,p,u)=\langle B\_{2}u-D\_{s}As-F\_{0}s+f,p\rangle-\frac{1}{2}(|Cs|^{2}+|u|^{2}+2\langle g,s\rangle). |  | (30) |

Note that the function g​(t)g(t) will show up as a forcing term in the adjoint equation.

From Pontryagin’s minimum principle, an extremum is reached when

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂H∂u=0;\frac{\partial H}{\partial u}=0; |  | (31) |

thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | u=B2∗​p,u=B\_{2}^{\*}p, |  | (32) |

and the Hamiltonian system corresponding to the optimal control problem ([29](https://arxiv.org/html/2511.11909v1#S4.E29 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) is

|  |  |  |
| --- | --- | --- |
|  | s˙+Ds​A​s+F0​s=B2​u+f,\displaystyle\dot{s}+D\_{s}As+F\_{0}s=B\_{2}u+f, |  |
|  |  |  |
| --- | --- | --- |
|  | p˙−Ds​A​p−F0∗​p=C∗​C​s+g,\displaystyle\dot{p}-D\_{s}Ap-F\_{0}^{\*}p=C^{\*}Cs+g, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(0)=s0,p​(+∞)=0.\displaystyle s(0)=s\_{0},~~p(+\infty)=0. |  | (33) |

The Hamiltonian system is written in the following form

|  |  |  |
| --- | --- | --- |
|  | s˙+(Ds​A+F0+B2​B2∗​P)​s=f,\displaystyle\dot{s}+(D\_{s}A+F\_{0}+B\_{2}B\_{2}^{\*}P)s=f, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p˙−(Ds​A+F0+B2​B2∗​P)∗​p=C∗​C​s−P​B2​B2∗​p+g.\displaystyle\dot{p}-(D\_{s}A+F\_{0}+B\_{2}B\_{2}^{\*}P)^{\*}p=C^{\*}Cs-PB\_{2}B\_{2}^{\*}p+g. |  | (34) |

Because it has been proved that the operator −(Ds​A+F0+B2​B2∗​P)-(D\_{s}A+F\_{0}+B\_{2}B\_{2}^{\*}P) generates an exponentially stable semigroup, then ∃a>0\exists~a>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |s​(t)|≤|s0|​e−a​t+∫0te−a​(t−r)​|f​(r)|​𝑑r,|s(t)|\leq|s\_{0}|e^{-at}+\int\limits\_{0}^{t}e^{-a(t-r)}|f(r)|dr, |  | (35) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |p​(t)|≤C​∫t+∞e−a​(r−t)​(|C​s​(r)|+|B2∗​p​(r)|+|g​(r)|)​𝑑r.|p(t)|\leq C\int\limits\_{t}^{+\infty}e^{-a(r-t)}(|Cs(r)|+|B\_{2}^{\*}p(r)|+|g(r)|)dr. |  | (36) |

Let us first calculate the estimate for the norm of s​(t)s(t) in the space L2​(0,∞;L2​(Ω))L^{2}(0,\infty;L^{2}(\Omega)), denoted by ∥⋅∥\|\cdot\|,
by integrating the square of equation ([35](https://arxiv.org/html/2511.11909v1#S4.E35 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) from 0 to +∞+\infty

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖s​(t)‖2\displaystyle\|s(t)\|^{2} | =\displaystyle= | ∫0+∞|s​(t)|2​𝑑t\displaystyle\int\limits\_{0}^{+\infty}|s(t)|^{2}dt |  | (37) |
|  |  | ≤\displaystyle\leq | |s0|2​∫0+∞e−2​a​t​𝑑t+‖e−a​t∗|f​(t)|‖2\displaystyle|s\_{0}|^{2}\int\limits\_{0}^{+\infty}e^{-2at}dt+\left\|e^{-at}\*|f(t)|\right\|^{2} |  |
|  |  | ≤\displaystyle\leq | |s0|2​∫0+∞e−2​a​t​𝑑t+(∫0+∞|e−a​t|​𝑑t)2​‖f​(t)‖2\displaystyle|s\_{0}|^{2}\int\limits\_{0}^{+\infty}e^{-2at}dt+\left(\int\limits\_{0}^{+\infty}\left|e^{-at}\right|dt\right)^{2}\left\|f(t)\right\|^{2} |  |
|  |  | ≤\displaystyle\leq | C​(|s0|2+‖f​(t)‖2).\displaystyle C\left(|s\_{0}|^{2}+\|f(t)\|^{2}\right). |  |

The derivation of this inequality has made use of Young’s inequality for convolution. Similarly, from equation ([36](https://arxiv.org/html/2511.11909v1#S4.E36 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")),
the estimate for the norm of s​(t)s(t) in the space L2​(0,∞;L2​(Ω))L^{2}(0,\infty;L^{2}(\Omega)) is

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖p​(t)‖2\displaystyle\|p(t)\|^{2} | ≤\displaystyle\leq | C​‖|C​s|+|B2∗​p|+|g|‖2\displaystyle C\left\||Cs|+|B\_{2}^{\*}p|+|g|\right\|^{2} |  | (38) |
|  |  | ≤\displaystyle\leq | C​(∫0+∞(|C​s|2+|B2∗​p|2)​𝑑t+‖g‖2).\displaystyle C\left(\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}\right)dt+\|g\|^{2}\right). |  |

From equation ([34](https://arxiv.org/html/2511.11909v1#S4.E34 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")),

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | |C​s|2+|B2∗​p|2\displaystyle|Cs|^{2}+|B\_{2}^{\*}p|^{2} | =\displaystyle= | ⟨C∗​C​s,s⟩+⟨B2​B2∗​p,p⟩\displaystyle\langle C^{\*}Cs,s\rangle+\langle B\_{2}B\_{2}^{\*}p,p\rangle |  | (39) |
|  |  | =\displaystyle= | ⟨p˙−(Ds​A+F0)∗​p−g,s⟩+⟨B2​B2∗​p,p⟩\displaystyle\left\langle\dot{p}-(D\_{s}A+F\_{0})^{\*}p-g,s\right\rangle+\left\langle B\_{2}B\_{2}^{\*}p,p\right\rangle |  |
|  |  | =\displaystyle= | ⟨p˙,s⟩−⟨g,s⟩+⟨p,−(Ds​A+F0)​s+B2​B2∗​p⟩\displaystyle\left\langle\dot{p},s\right\rangle-\langle g,s\rangle+\left\langle p,-(D\_{s}A+F\_{0})s+B\_{2}B\_{2}^{\*}p\right\rangle |  |
|  |  | =\displaystyle= | ⟨p˙,s⟩−⟨g,s⟩+⟨p,s˙−f⟩\displaystyle\left\langle\dot{p},s\right\rangle-\langle g,s\rangle+\left\langle p,\dot{s}-f\right\rangle |  |
|  |  | =\displaystyle= | dd​t​⟨p,s⟩−⟨g,s⟩−⟨p,f⟩.\displaystyle\frac{d}{dt}\langle p,s\rangle-\langle g,s\rangle-\langle p,f\rangle. |  |

Integrating this from 0 to +∞+\infty, it is found that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∫0+∞(|C​s|2+|B2∗​p|2)​𝑑t\displaystyle\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}\right)dt | =\displaystyle= | −⟨p​(0),s​(0)⟩−∫0∞⟨g,s⟩​𝑑t−∫0∞⟨p,f⟩​𝑑t\displaystyle-\langle p(0),s(0)\rangle-\int\limits\_{0}^{\infty}\langle g,s\rangle dt-\int\limits\_{0}^{\infty}\langle p,f\rangle dt |  | (40) |
|  |  | ≤\displaystyle\leq | ⟨|p​(0)|,|s0|⟩+∫0+∞|⟨g,s⟩|​𝑑t+∫0+∞|⟨p,f⟩|​𝑑t.\displaystyle\langle|p(0)|,|s\_{0}|\rangle+\int\limits\_{0}^{+\infty}|\langle g,s\rangle|dt+\int\limits\_{0}^{+\infty}|\langle p,f\rangle|dt. |  |

Substituting t=0t=0 into equation ([36](https://arxiv.org/html/2511.11909v1#S4.E36 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) gives the following estimate for |p​(0)||p(0)|:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |p​(0)|≤C​∫0+∞e−a​r​(|C​s​(r)|+|B2∗​p​(r)|+|g​(r)|)​𝑑r.|p(0)|\leq C\int\limits\_{0}^{+\infty}e^{-ar}(|Cs(r)|+|B\_{2}^{\*}p(r)|+|g(r)|)dr. |  | (41) |

Therefore,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∫0+∞(|C​s|2+|B2∗​p|2)​𝑑t\displaystyle\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}\right)dt | ≤\displaystyle\leq | C​⟨∫0+∞e−a​r​(|C​s​(r)|+|B2∗​p​(r)|+|g​(r)|)​𝑑r,|s0|⟩\displaystyle C\left\langle\int\limits\_{0}^{+\infty}e^{-ar}(|Cs(r)|+|B\_{2}^{\*}p(r)|+|g(r)|)dr,|s\_{0}|\right\rangle |  | (42) |
|  |  |  | +∫0+∞|⟨g,s⟩|​𝑑t+∫0+∞|⟨p,f⟩|​𝑑t\displaystyle+\int\limits\_{0}^{+\infty}|\langle g,s\rangle|dt+\int\limits\_{0}^{+\infty}|\langle p,f\rangle|dt |  |
|  |  | ≤\displaystyle\leq | C​∫0+∞⟨|C​s​(r)|+|B2∗​p​(r)|+|g​(r)|,e−a​r​|s0|⟩​𝑑r\displaystyle C\int\limits\_{0}^{+\infty}\left\langle|Cs(r)|+|B\_{2}^{\*}p(r)|+|g(r)|,e^{-ar}|s\_{0}|\right\rangle dr |  |
|  |  |  | +∫0+∞|⟨g,s⟩|​𝑑t+∫0+∞|⟨p,f⟩|​𝑑t.\displaystyle+\int\limits\_{0}^{+\infty}|\langle g,s\rangle|dt+\int\limits\_{0}^{+\infty}|\langle p,f\rangle|dt. |  |

Applying Young’s inequality with ϵ\epsilon

|  |  |  |  |
| --- | --- | --- | --- |
|  | k1​k2≤12​ϵ​k12+ϵ2​k22k\_{1}k\_{2}\leq\frac{1}{2\epsilon}k\_{1}^{2}+\frac{\epsilon}{2}k\_{2}^{2} |  | (43) |

to the three terms on the right hand side of inequality ([42](https://arxiv.org/html/2511.11909v1#S4.E42 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) yields

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∫0+∞(|C​s|2+|B2∗​p|2)​𝑑t\displaystyle\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}\right)dt | ≤\displaystyle\leq | ϵ​∫0+∞(|C​s|+|B2∗​p|+|g|)2​𝑑t+Cϵ​|s0|2\displaystyle\epsilon\int\limits\_{0}^{+\infty}\left(|Cs|+|B\_{2}^{\*}p|+|g|\right)^{2}dt+C\_{\epsilon}|s\_{0}|^{2} |  | (44) |
|  |  |  | +ϵ​(‖s‖2+‖p‖2)+Cϵ​(‖g‖2+‖f‖2)\displaystyle+\epsilon\left(\|s\|^{2}+\|p\|^{2}\right)+C\_{\epsilon}\left(\|g\|^{2}+\|f\|^{2}\right) |  |
|  |  | ≤\displaystyle\leq | ϵ​(∫0+∞(|C​s|2+|B2∗​p|2)​𝑑t+‖s‖2+‖p‖2)\displaystyle\epsilon\left(\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}\right)dt+\|s\|^{2}+\|p\|^{2}\right) |  |
|  |  |  | +Cϵ​(|s0|2+‖g‖2+‖f‖2).\displaystyle+C\_{\epsilon}\left(|s\_{0}|^{2}+\|g\|^{2}+\|f\|^{2}\right). |  |

This is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0+∞(|C​s|2+|B2∗​p|2)​𝑑t≤ϵ​(‖s‖2+‖p‖2)+Cϵ​(|s0|2+‖g‖2+‖f‖2).\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}\right)dt\leq\epsilon\left(\|s\|^{2}+\|p\|^{2}\right)+C\_{\epsilon}\left(|s\_{0}|^{2}+\|g\|^{2}+\|f\|^{2}\right). |  | (45) |

Substituting this inequality into inequality ([38](https://arxiv.org/html/2511.11909v1#S4.E38 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖p​(t)‖2≤ϵ​(‖s‖2+‖p‖2)+Cϵ​(|s0|2+‖g‖2+‖f‖2).\|p(t)\|^{2}\leq\epsilon\left(\|s\|^{2}+\|p\|^{2}\right)+C\_{\epsilon}\left(|s\_{0}|^{2}+\|g\|^{2}+\|f\|^{2}\right). |  | (46) |

Now combine with inequality ([37](https://arxiv.org/html/2511.11909v1#S4.E37 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s​(t)‖+‖p​(t)‖2≤ϵ​(‖s‖2+‖p‖2)+Cϵ​(|s0|2+‖g‖2+‖f‖2),\|s(t)\|+\|p(t)\|^{2}\leq\epsilon\left(\|s\|^{2}+\|p\|^{2}\right)+C\_{\epsilon}\left(|s\_{0}|^{2}+\|g\|^{2}+\|f\|^{2}\right), |  | (47) |

which is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s​(t)‖2+‖p​(t)‖2≤C​(|s0|2+‖g‖2+‖f‖2).\|s(t)\|^{2}+\|p(t)\|^{2}\leq C\left(|s\_{0}|^{2}+\|g\|^{2}+\|f\|^{2}\right). |  | (48) |

Then, with some algebraic manipulations, it can be concluded that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s​(t)‖+‖p​(t)‖≤C​(|s0|+‖g‖+‖f‖).\|s(t)\|+\|p(t)\|\leq C\left(|s\_{0}|+\|g\|+\|f\|\right). |  | (49) |

This estimation is of great significance because it enables us to bound the norm of the solution by the norm of the initial condition and the additional forcing term. By choosing the forcing term in a special form, the nonlinear state equation can be readily connected to the linearized state equation.

### 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances

Now consider the optimal control problem for the original nonlinear system ([5](https://arxiv.org/html/2511.11909v1#S2.E5 "In 2 Formulation of the control problem ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) once again and define the cost functional in the form ([11](https://arxiv.org/html/2511.11909v1#S3.E11 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")),
then the optimal control problem is formulated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supwinfu\displaystyle\sup\limits\_{w}\inf\limits\_{u} |  | J​(s0)=12​∫0+∞(|C​s|2+|u|2−γ2​|w|2)​𝑑t,\displaystyle J(s\_{0})=\frac{1}{2}\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|u|^{2}-\gamma^{2}|w|^{2}\right)dt, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | subject to |  | dd​t​s​(t)+Ds​A​s​(t)+F​(s​(t))=B1​w​(t)+B2​u​(t),\displaystyle\frac{d}{dt}s(t)+D\_{s}As(t)+F(s(t))=B\_{1}w(t)+B\_{2}u(t), |  | (50) |

where F​(s​(t))F(s(t)) is given by ([7](https://arxiv.org/html/2511.11909v1#S2.E7 "In 2 Formulation of the control problem ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), which includes the nonlinear term.

Once again the Pontryagin Hamiltonian is constructed in the following way

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(s,p,u,w)=⟨B1​w+B2​u−Ds​A​s−F​(s),p⟩−12​(|C​s|2+|u|2−γ2​|w|2).H(s,p,u,w)=\left\langle B\_{1}w+B\_{2}u-D\_{s}As-F(s),p\right\rangle-\frac{1}{2}\left(|Cs|^{2}+|u|^{2}-\gamma^{2}|w|^{2}\right). |  | (51) |

Based on Pontryagin’s minimum principle, an extremum is reached, as in equation ([14](https://arxiv.org/html/2511.11909v1#S3.E14 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), when

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂H∂u=0\displaystyle\frac{\partial H}{\partial u}=0 | ∂H∂w=0,\displaystyle\displaystyle\frac{\partial H}{\partial w}=0, |  |  | (52) |

which yields

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | u=B2∗​p,\displaystyle u=B\_{2}^{\*}p, | w=−1γ2​B1∗​p,\displaystyle\displaystyle w=-\frac{1}{\gamma^{2}}B\_{1}^{\*}p, |  |  | (53) |

respectively. The corresponding Hamiltonian system is now

|  |  |  |
| --- | --- | --- |
|  | s˙+Ds​A​s+F​(s)=B1​w+B2​u,\displaystyle\dot{s}+D\_{s}As+F(s)=B\_{1}w+B\_{2}u, |  |
|  |  |  |
| --- | --- | --- |
|  | p˙−Ds​A​p−(∇F​(s))∗​p=C∗​C​s,\displaystyle\dot{p}-D\_{s}Ap-(\nabla F(s))^{\*}p=C^{\*}Cs, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(0)=s0,p​(+∞)=0.\displaystyle s(0)=s\_{0},~~p(+\infty)=0. |  | (54) |

Recall that F​(s)=F0​s+FN​(s)F(s)=F\_{0}s+F\_{N}(s) in the nonlinear case; therefore, this becomes

|  |  |  |
| --- | --- | --- |
|  | s˙+Ds​A​s+F0​s=B2​u−FN​(s),\displaystyle\dot{s}+D\_{s}As+F\_{0}s=B\_{2}u-F\_{N}(s), |  |
|  |  |  |
| --- | --- | --- |
|  | p˙−Ds​A​p−F0∗​p=C∗​C​s+(∇FN​(s))∗​p,\displaystyle\dot{p}-D\_{s}Ap-F\_{0}^{\*}p=C^{\*}Cs+\left(\nabla F\_{N}(s)\right)^{\*}p, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(0)=s0,p​(+∞)=0.\displaystyle s(0)=s\_{0},~~p(+\infty)=0. |  | (55) |

This is the same as the linear system with forcing ([33](https://arxiv.org/html/2511.11909v1#S4.E33 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), but now with

|  |  |  |  |
| --- | --- | --- | --- |
|  | f=−FN​(s)=c2S​s2,g=(∇FN​(s))∗​p=2​c2S​s​p.f=-F\_{N}(s)=\frac{c\_{2}}{S}s^{2},~~g=\left(\nabla F\_{N}(s)\right)^{\*}p=\frac{2c\_{2}}{S}sp. |  | (56) |

Let us define the mapping from the solution pair (s,p)(s,p) to the forcing terms (f,g)(f,g) through the nonlinear term as ℳ1\mathcal{M}\_{1}. Similarly, the mapping from the forcing terms (f,g)(f,g) to the solution pair (s,p)(s,p) through the linearized system with forcing terms ([33](https://arxiv.org/html/2511.11909v1#S4.E33 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) is ℳ2\mathcal{M}\_{2}. The composite mapping is denoted by ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1}. If (s,p)(s,p) is a solution to the nonlinear system, then (s,p)=ℳ2∘ℳ1​(s,p)(s,p)=\mathcal{M}\_{2}\circ\mathcal{M}\_{1}(s,p). Then if the composite mapping ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1} is a contraction, the solution (s,p)(s,p) uniquely exists.

Let Σμ\Sigma\_{\mu} be a subset of H×HH\times H defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σμ={(s,p)|‖s‖+‖p‖≤μ}.\Sigma\_{\mu}=\{(s,p)\left|\|s\|+\|p\|\leq\mu\right.\}. |  | (57) |

Then for (s,p)∈Σμ(s,p)\in\Sigma\_{\mu}, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖f‖+‖g‖\displaystyle\|f\|+\|g\| | =\displaystyle= | ‖c2S​s2‖+‖2​c2S​s​p‖\displaystyle\left\|\frac{c\_{2}}{S}s^{2}\right\|+\left\|\frac{2c\_{2}}{S}sp\right\| |  | (58) |
|  |  | ≤\displaystyle\leq | 2​c2S​‖s‖​(‖s‖+‖p‖)\displaystyle\frac{2c\_{2}}{S}\|s\|\left(\|s\|+\|p\|\right) |  |
|  |  | ≤\displaystyle\leq | 2​c2S​μ2.\displaystyle\frac{2c\_{2}}{S}\mu^{2}. |  |

From the inequality ([49](https://arxiv.org/html/2511.11909v1#S4.E49 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), it is observed that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s‖+‖p‖≤C​(|s0|+‖f‖+‖g‖)≤|s0|+2​c2S​μ2.\|s\|+\|p\|\leq C\left(|s\_{0}|+\|f\|+\|g\|\right)\leq|s\_{0}|+\frac{2c\_{2}}{S}\mu^{2}. |  | (59) |

In order to make Σμ\Sigma\_{\mu} invariant with respect to the composite mapping ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1}, it is necessary to set

|  |  |  |  |
| --- | --- | --- | --- |
|  | |s0|+2​c2S​μ2≤μ.|s\_{0}|+\frac{2c\_{2}}{S}\mu^{2}\leq\mu. |  | (60) |

Therefore, if

|  |  |  |  |
| --- | --- | --- | --- |
|  | |s0|<S8​c2​C2,|s\_{0}|<\frac{S}{8c\_{2}C^{2}}, |  | (61) |

then

|  |  |  |  |
| --- | --- | --- | --- |
|  | S−S2−8​c2​C2​S​|s0|4​c2​C≤μ≤S+S2−8​c2​C2​S​|s0|4​c2​C,\frac{S-\sqrt{S^{2}-8c\_{2}C^{2}S|s\_{0}|}}{4c\_{2}C}\leq\mu\leq\frac{S+\sqrt{S^{2}-8c\_{2}C^{2}S|s\_{0}|}}{4c\_{2}C}, |  | (62) |

and Σμ\Sigma\_{\mu} is invariant with respect to ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1}.

As one can see, if (s,p)(s,p) is a solution to the nonlinear system ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), then (s,p)(s,p) is a fixed point of the composite mapping ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1}. Hence, in order to show that the nonlinear system ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) has a unique solution, it is necessary to prove that ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1} is a contraction mapping.

To do so, assume there are two different groups of forcing terms (f1,g1)(f\_{1},g\_{1}) and (f2,g2)(f\_{2},g\_{2}), and the corresponding solutions of ([33](https://arxiv.org/html/2511.11909v1#S4.E33 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) are (s1,g1)(s\_{1},g\_{1}) and (s2,g2)(s\_{2},g\_{2}), which satisfy the following systems of equations

|  |  |  |
| --- | --- | --- |
|  | s1˙+Ds​A​s1+F0​s1=B2​B2∗​p1+f1,\displaystyle\dot{s\_{1}}+D\_{s}As\_{1}+F\_{0}s\_{1}=B\_{2}B\_{2}^{\*}p\_{1}+f\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | p1˙−Ds​A​p1−F0∗​p1=C∗​C​s1+g1,\displaystyle\dot{p\_{1}}-D\_{s}Ap\_{1}-F\_{0}^{\*}p\_{1}=C^{\*}Cs\_{1}+g\_{1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s1​(0)=s0,p1​(+∞)=0,\displaystyle s\_{1}(0)=s\_{0},~~p\_{1}(+\infty)=0, |  | (63) |

and

|  |  |  |
| --- | --- | --- |
|  | s2˙+Ds​A​s2+F0​s2=B2​B2∗​p2+f2,\displaystyle\dot{s\_{2}}+D\_{s}As\_{2}+F\_{0}s\_{2}=B\_{2}B\_{2}^{\*}p\_{2}+f\_{2}, |  |
|  |  |  |
| --- | --- | --- |
|  | p2˙−Ds​A​p2−F0∗​p2=C∗​C​s2+g2,\displaystyle\dot{p\_{2}}-D\_{s}Ap\_{2}-F\_{0}^{\*}p\_{2}=C^{\*}Cs\_{2}+g\_{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s2​(0)=s0,p2​(+∞)=0,\displaystyle s\_{2}(0)=s\_{0},~~p\_{2}(+\infty)=0, |  | (64) |

respectively. By linearity of the above equations, superposition leads to

|  |  |  |
| --- | --- | --- |
|  | dd​t​(s1−s2)+Ds​A​(s1−s2)+F0​(s1−s2)=B2​B2∗​(p1−p2)+(f1−f2),\displaystyle\frac{d}{dt}(s\_{1}-s\_{2})+D\_{s}A(s\_{1}-s\_{2})+F\_{0}(s\_{1}-s\_{2})=B\_{2}B\_{2}^{\*}(p\_{1}-p\_{2})+(f\_{1}-f\_{2}), |  |
|  |  |  |
| --- | --- | --- |
|  | dd​t​(p1−p2)−Ds​A​(p1−p2)−F0∗​(p1−p2)=C∗​C​(s1−s2)+(g1−g2),\displaystyle\frac{d}{dt}(p\_{1}-p\_{2})-D\_{s}A(p\_{1}-p\_{2})-F\_{0}^{\*}(p\_{1}-p\_{2})=C^{\*}C(s\_{1}-s\_{2})+(g\_{1}-g\_{2}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (s1−s2)​(0)=0,(p1−p2)​(+∞)=0.\displaystyle(s\_{1}-s\_{2})(0)=0,~~(p\_{1}-p\_{2})(+\infty)=0. |  | (65) |

Applying relation ([49](https://arxiv.org/html/2511.11909v1#S4.E49 "In 4.1 Construct a linearized system with a forcing term and no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), requires that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s1−s2‖+‖p1−p2‖≤C​(‖g1−g2‖+‖f1−f2‖),\|s\_{1}-s\_{2}\|+\|p\_{1}-p\_{2}\|\leq C\left(\|g\_{1}-g\_{2}\|+\|f\_{1}-f\_{2}\|\right), |  | (66) |

which demonstrates that the mapping ℳ2\mathcal{M}\_{2} is Lipschitz continuous.

Now consider the mapping ℳ1\mathcal{M}\_{1} from (s,p)(s,p) to (f,g)(f,g), for which

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ‖f1−f2‖+‖g1−g2‖\displaystyle\|f\_{1}-f\_{2}\|+\|g\_{1}-g\_{2}\| | =\displaystyle= | ‖c2S​(s12−s22)‖+‖2​c2S​(s1​p1−s2​p2)‖\displaystyle\left\|\frac{c\_{2}}{S}\left(s\_{1}^{2}-s\_{2}^{2}\right)\right\|+\left\|\frac{2c\_{2}}{S}\left(s\_{1}p\_{1}-s\_{2}p\_{2}\right)\right\| |  | (67) |
|  |  | ≤\displaystyle\leq | c2S​(‖s1‖+‖s2‖)​‖s1−s2‖\displaystyle\frac{c\_{2}}{S}\left(\|s\_{1}\|+\|s\_{2}\|\right)\|s\_{1}-s\_{2}\| |  |
|  |  |  | +2​c2S​‖s1​p1−s1​p2+s1​p2−s2​p2‖\displaystyle+\frac{2c\_{2}}{S}\|s\_{1}p\_{1}-s\_{1}p\_{2}+s\_{1}p\_{2}-s\_{2}p\_{2}\| |  |
|  |  | ≤\displaystyle\leq | c2S​(‖s1‖+‖s2‖+2​‖p2‖)​‖s1−s2‖\displaystyle\frac{c\_{2}}{S}\left(\|s\_{1}\|+\|s\_{2}\|+2\|p\_{2}\|\right)\|s\_{1}-s\_{2}\| |  |
|  |  |  | +2​c2S​‖s1‖​‖p1−p2‖.\displaystyle+\frac{2c\_{2}}{S}\|s\_{1}\|\|p\_{1}-p\_{2}\|. |  |

If the mapping is considered to be within Σμ\Sigma\_{\mu}, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f1−f2‖+‖g1−g2‖≤4​c2​μS​(‖s1−s2‖+‖p1−p2‖),\|f\_{1}-f\_{2}\|+\|g\_{1}-g\_{2}\|\leq\frac{4c\_{2}\mu}{S}\left(\|s\_{1}-s\_{2}\|+\|p\_{1}-p\_{2}\|\right), |  | (68) |

then this relation can be combined with ([66](https://arxiv.org/html/2511.11909v1#S4.E66 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) to yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s1−s2‖+‖p1−p2‖≤4​c2​C​μS​(‖s1−s2‖+‖p1−p2‖).\|s\_{1}-s\_{2}\|+\|p\_{1}-p\_{2}\|\leq\frac{4c\_{2}C\mu}{S}\left(\|s\_{1}-s\_{2}\|+\|p\_{1}-p\_{2}\|\right). |  | (69) |

Therefore, for the Lipschitz constant to be less than one, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 4​c2​C​μS<1,\displaystyle\frac{4c\_{2}C\mu}{S}<1, |  | (70) |

which requires that

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ<S4​c2​C,\displaystyle\mu<\frac{S}{4c\_{2}C}~, |  | (71) |

then the composite mapping ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1} is a contraction mapping.
This ensures the existence and uniqueness of the solution (s,p)(s,p) to the nonlinear system ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), which is a fixed point of ℳ2∘ℳ1\mathcal{M}\_{2}\circ\mathcal{M}\_{1}.

### 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system

Thus far, the contraction mapping theorem has been used to prove existence and uniqueness of the solution for the controlled nonlinear system equation. Next, the mathematical form of the stabilizing controller for the nonlinear system is obtained via the Hamilton-Jacobi equation.

Recall that the Hamiltonian for the nonlinear system ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(s,p,u,w)=⟨B1​w+B2​u−Ds​A​s−F​(s),p⟩−12​(|C​s|2+|u|2−γ2​|w|2).H(s,p,u,w)=\left\langle B\_{1}w+B\_{2}u-D\_{s}As-F(s),p\right\rangle-\frac{1}{2}\left(|Cs|^{2}+|u|^{2}-\gamma^{2}|w|^{2}\right). |  | (72) |

Because the system is nonlinear, assume that the mapping from s0s\_{0} to p​(0)p(0) has the nonlinear form

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(0)=−G​(s0).p(0)=-G(s\_{0}). |  | (73) |

Because the uniqueness of the solution for the nonlinear system ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) has been proved,
the invariant manifold of the Hamiltonian system also takes the same nonlinear form according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(t)=−G​(s​(t)).p(t)=-G(s(t)). |  | (74) |

The terminal time of the optimal control problem ([50](https://arxiv.org/html/2511.11909v1#S4.E50 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) is not specified; therefore, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(s,p,u,w)=0.H(s,p,u,w)=0. |  | (75) |

Substituting the invariant manifolds gives,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | H​(s,p,u,w)\displaystyle H(s,p,u,w) | =\displaystyle= | ⟨1γ2​B1​B1∗​G​(s​(t))−B2​B2∗​G​(s​(t))−Ds​A​s​(t)−F​(s​(t)),−G​(s​(t))⟩\displaystyle\left\langle\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}G(s(t))-B\_{2}B\_{2}^{\*}G(s(t))-D\_{s}As(t)-F(s(t)),-G(s(t))\right\rangle |  | (76) |
|  |  |  | −12​(|C​s​(t)|2+|B2∗​G​(s​(t))|2−1γ2​|B1∗​G​(s​(t))|2)\displaystyle-\frac{1}{2}\left(|Cs(t)|^{2}+|B\_{2}^{\*}G(s(t))|^{2}-\frac{1}{\gamma^{2}}|B\_{1}^{\*}G(s(t))|^{2}\right) |  |
|  |  | =\displaystyle= | ⟨Ds​A​s+F​(s),G​(s)⟩−12​γ2​|B1∗​G​(s)|2+12​|B2∗​G​(s)|2−12​|C​s|2.\displaystyle\left\langle D\_{s}As+F(s),G(s)\right\rangle-\frac{1}{2\gamma^{2}}|B\_{1}^{\*}G(s)|^{2}+\frac{1}{2}|B\_{2}^{\*}G(s)|^{2}-\frac{1}{2}|Cs|^{2}. |  |

Therefore, the Hamilton-Jacobi equation for the nonlinear mapping G​(⋅)G(\cdot) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Ds​A​s+F​(s),G​(s)⟩−12​γ2​|B1∗​G​(s)|2+12​|B2∗​G​(s)|2−12​|C​s|2=0.\left\langle D\_{s}As+F(s),G(s)\right\rangle-\frac{1}{2\gamma^{2}}|B\_{1}^{\*}G(s)|^{2}+\frac{1}{2}|B\_{2}^{\*}G(s)|^{2}-\frac{1}{2}|Cs|^{2}=0. |  | (77) |

From equations ([53](https://arxiv.org/html/2511.11909v1#S4.E53 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), if s=0s=0, then p=0p=0, which yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(0)=0.G(0)=0. |  | (78) |

To see the relationship between the Hamilton-Jacobi equation ([77](https://arxiv.org/html/2511.11909v1#S4.E77 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and the algebraic Riccati equation ([19](https://arxiv.org/html/2511.11909v1#S3.E19 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), first consider the relationship between the cost function J​(s0)J(s\_{0}) and the nonlinear mapping GG.
Because the cost functional J​(s0)J(s\_{0}) can be treated as a function of the initial condition s0s\_{0},
consider how perturbation of the initial condition will influence the solution of the nonlinear Hamiltonian system ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")).

Assume δ\delta is a small perturbation on the initial condition of ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), that is, (s+sδ)​(0)=s0+δ(s+s\_{\delta})(0)=s\_{0}+\delta, and the solution becomes
(s+sδ,p+pδ)(s+s\_{\delta},p+p\_{\delta}). Both sδs\_{\delta} and pδp\_{\delta} are on the scale of O​(δ)O(\delta).

|  |  |  |
| --- | --- | --- |
|  | dd​t​(s+sδ)+Ds​A​(s+sδ)+F​(s+sδ)=(B2​B2∗−1γ2​B1​B1∗)​(p+pδ),\displaystyle\frac{d}{dt}(s+s\_{\delta})+D\_{s}A(s+s\_{\delta})+F(s+s\_{\delta})=\left(B\_{2}B\_{2}^{\*}-\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}\right)(p+p\_{\delta}), |  |
|  |  |  |
| --- | --- | --- |
|  | dd​t​(p+pδ)−Ds​A​(p+pδ)−(∇F​(s+sδ))∗​(p+pδ)=C∗​C​(s+sδ),\displaystyle\frac{d}{dt}(p+p\_{\delta})-D\_{s}A(p+p\_{\delta})-(\nabla F(s+s\_{\delta}))^{\*}(p+p\_{\delta})=C^{\*}C(s+s\_{\delta}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (s+sδ)​(0)=s0+δ,(p+pδ)​(+∞)=0.\displaystyle(s+s\_{\delta})(0)=s\_{0}+\delta,~~(p+p\_{\delta})(+\infty)=0. |  | (79) |

Canceling the O​(1)O(1) terms by substituting ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and neglecting O​(δ2)O(\delta^{2}) terms leaves the following equations for the perturbations

|  |  |  |
| --- | --- | --- |
|  | sδ˙+Ds​A​sδ+∇F​(s)​sδ=(B2​B2∗−1γ2​B1​B1∗)​pδ,\displaystyle\dot{s\_{\delta}}+D\_{s}As\_{\delta}+\nabla F(s)s\_{\delta}=\left(B\_{2}B\_{2}^{\*}-\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}\right)p\_{\delta}, |  |
|  |  |  |
| --- | --- | --- |
|  | pδ˙−Ds​A​pδ−(∇F​(s))∗​pδ−(∇2F​(s)​sδ)∗​p=C∗C​pδ,\displaystyle\dot{p\_{\delta}}-D\_{s}Ap\_{\delta}-\left(\nabla F(s)\right)^{\*}p\_{\delta}-\left(\nabla^{2}F(s)s\_{\delta}\right)^{\*}p=C\*Cp\_{\delta}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | sδ​(0)=δ,pδ​(+∞)=0.\displaystyle s\_{\delta}(0)=\delta,~~p\_{\delta}(+\infty)=0. |  | (80) |

Define the mapping from s0s\_{0} to (s,p)(s,p) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(s0)=(s,p).\Phi(s\_{0})=(s,p). |  | (81) |

Then from the definition of (sδ,pδ)(s\_{\delta},p\_{\delta}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨∇Φ​(s0),δ⟩=(sδ,pδ).\left\langle\nabla\Phi(s\_{0}),\delta\right\rangle=(s\_{\delta},p\_{\delta}). |  | (82) |

Because J​(s0)=J​(s​(s0),p​(s0))J(s\_{0})=J(s(s\_{0}),p(s\_{0})),

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ⟨∇J​(s0),δ⟩\displaystyle\left\langle\nabla J(s\_{0}),\delta\right\rangle | =\displaystyle= | ⟨(δ​Jδ​s,δ​Jδ​p),(sδ,pδ)T⟩\displaystyle\left\langle\left(\frac{\delta J}{\delta s},\frac{\delta J}{\delta p}\right),\left(s\_{\delta},p\_{\delta}\right)^{T}\right\rangle |  | (83) |
|  |  | =\displaystyle= | ∫0+∞(⟨C∗​C​s,sδ⟩+⟨B2​B2∗​p,pδ⟩−⟨1γ2​B1​B1∗​p,pδ⟩)​𝑑t.\displaystyle\int\limits\_{0}^{+\infty}\left(\langle C^{\*}Cs,s\_{\delta}\rangle+\langle B\_{2}B\_{2}^{\*}p,p\_{\delta}\rangle-\left\langle\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}p,p\_{\delta}\right\rangle\right)dt. |  |

Substituting ([54](https://arxiv.org/html/2511.11909v1#S4.E54 "In 4.2 Uniqueness and existence of the solution of the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and ([80](https://arxiv.org/html/2511.11909v1#S4.E80 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) yields

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ⟨∇J​(s0),δ⟩\displaystyle\left\langle\nabla J(s\_{0}),\delta\right\rangle | =\displaystyle= | ∫0+∞(⟨p˙−Ds​A​p−(∇F​(s))∗​p,sδ⟩+⟨B2​B2∗​p−1γ2​B1​B1∗​p,pδ⟩)​𝑑t\displaystyle\int\limits\_{0}^{+\infty}\left(\left\langle\dot{p}-D\_{s}Ap-(\nabla F(s))^{\*}p,s\_{\delta}\right\rangle+\left\langle B\_{2}B\_{2}^{\*}p-\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}p,p\_{\delta}\right\rangle\right)dt |  | (84) |
|  |  | =\displaystyle= | ∫0+∞(⟨p˙,sδ⟩−⟨p,Ds​A​sδ+(∇F​(s))​sδ⟩+⟨p,B2​B2∗​p−1γ2​B1​B1∗​pδ⟩)​𝑑t\displaystyle\int\limits\_{0}^{+\infty}\left(\left\langle\dot{p},s\_{\delta}\right\rangle-\left\langle p,D\_{s}As\_{\delta}+(\nabla F(s))s\_{\delta}\right\rangle+\left\langle p,B\_{2}B\_{2}^{\*}p-\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}p\_{\delta}\right\rangle\right)dt |  |
|  |  | =\displaystyle= | ∫0+∞dd​t​⟨p,sδ⟩​𝑑t\displaystyle\int\limits\_{0}^{+\infty}\frac{d}{dt}\left\langle p,s\_{\delta}\right\rangle dt |  |
|  |  | =\displaystyle= | −⟨p​(0),δ⟩.\displaystyle-\langle p(0),\delta\rangle. |  |

Because p​(0)=−G​(s0)p(0)=-G(s\_{0}), then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇J​(s0)=G​(s0).\nabla J(s\_{0})=G(s\_{0}). |  | (85) |

Now consider the case when s0=0s\_{0}=0, then the corresponding solution of the nonlinear system is (s,p)=(0,0)(s,p)=(0,0).
Substituting (s,p)=(0,0)(s,p)=(0,0) into ([80](https://arxiv.org/html/2511.11909v1#S4.E80 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), the equations are satisfied by the perturbation about the zero solution (s,p)=(0,0)(s,p)=(0,0) as follows:

|  |  |  |
| --- | --- | --- |
|  | sδ˙+Ds​A​sδ+F0​sδ=(B2​B2∗−1γ2​B1​B1∗)​pδ,\displaystyle\dot{s\_{\delta}}+D\_{s}As\_{\delta}+F\_{0}s\_{\delta}=\left(B\_{2}B\_{2}^{\*}-\frac{1}{\gamma^{2}}B\_{1}B\_{1}^{\*}\right)p\_{\delta}, |  |
|  |  |  |
| --- | --- | --- |
|  | pδ˙−Ds​A​pδ−F0∗​pδ=C∗C​pδ,\displaystyle\dot{p\_{\delta}}-D\_{s}Ap\_{\delta}-F\_{0}^{\*}p\_{\delta}=C\*Cp\_{\delta}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | sδ​(0)=δ,pδ​(+∞)=0,\displaystyle s\_{\delta}(0)=\delta,~~p\_{\delta}(+\infty)=0, |  | (86) |

which have the same form as the linear Hamiltonian system ([16](https://arxiv.org/html/2511.11909v1#S3.E16 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")). Therefore, the invariant manifold for ([86](https://arxiv.org/html/2511.11909v1#S4.E86 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory"))
is the same as for ([16](https://arxiv.org/html/2511.11909v1#S3.E16 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")), which is

|  |  |  |  |
| --- | --- | --- | --- |
|  | pδ=−P​sδ,p\_{\delta}=-Ps\_{\delta}, |  | (87) |

where PP is the solution to the algebraic Riccati equation ([19](https://arxiv.org/html/2511.11909v1#S3.E19 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")). Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨∇Φ​(s0),δ⟩=(sδ,pδ)=(sδ,−P​sδ).\left\langle\nabla\Phi(s\_{0}),\delta\right\rangle=(s\_{\delta},p\_{\delta})=(s\_{\delta},-Ps\_{\delta}). |  | (88) |

On the other hand, because Φ​(s0)=(s,p)=(s,−G​(s))\Phi(s\_{0})=(s,p)=(s,-G(s)),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨∇Φ​(s0),δ⟩=(sδ,−∇G​(s)​sδ).\left\langle\nabla\Phi(s\_{0}),\delta\right\rangle=(s\_{\delta},-\nabla G(s)s\_{\delta}). |  | (89) |

Setting s0=0s\_{0}=0, the relationship between the solutions to the algebraic Riccati equation ([19](https://arxiv.org/html/2511.11909v1#S3.E19 "In 3.1 Algebraic Riccatti equation ‣ 3 Optimal control for the linearized system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and Hamilton-Jacobi equation ([77](https://arxiv.org/html/2511.11909v1#S4.E77 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇G​(0)=P.\nabla G(0)=P. |  | (90) |

Hence, it is concluded that the nonlinear mapping G​(⋅)G(\cdot) needs to satisfy the following four conditions:

* i)

  ⟨Ds​A​s+F​(s),G​(s)⟩−12​γ2​|B1∗​G​(s)|2+12​|B2∗​G​(s)|2−12​|C​s|2=0\left\langle D\_{s}As+F(s),G(s)\right\rangle-\frac{1}{2\gamma^{2}}|B\_{1}^{\*}G(s)|^{2}+\frac{1}{2}|B\_{2}^{\*}G(s)|^{2}-\frac{1}{2}|Cs|^{2}=0,
* ii)

  G​(0)=0G(0)=0,
* iii)

  ∇J​(s0)=G​(s0)\nabla J(s\_{0})=G(s\_{0}),
* iv)

  ∇G​(0)=P\nabla G(0)=P.

From the last two conditions, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇J​(0)=G​(0)=0,∇2J​(0)=∇G​(0)=P>0.\nabla J(0)=G(0)=0,~~\nabla^{2}J(0)=\nabla G(0)=P>0. |  | (91) |

Therefore, in some neighborhood of s0=0s\_{0}=0, the cost functional J​(s0)J(s\_{0}) can be bounded by a convex function of s0s\_{0}, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∃k>0,such that​J​(s0)≤k​|s0|2.\exists~k>0,~~\mbox{such that}~~J(s\_{0})\leq k|s\_{0}|^{2}. |  | (92) |

This result will be employed in the following subsection.

### 4.4 Optimal control for the nonlinear system

Recalling that u=B2∗​pu=B\_{2}^{\*}p, the cost functional J​(⋅)J(\cdot) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(s)=∫t+∞(|C​s|2+|B2∗​p|2−γ2​|w|2)​𝑑t,J(s)=\int\limits\_{t}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}p|^{2}-\gamma^{2}|w|^{2}\right)dt, |  | (93) |

where s​(t)s(t) is taken as the initial value. Taking the time derivative gives

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | dd​t​J​(s)\displaystyle\frac{d}{dt}J(s) | =\displaystyle= | ⟨∇J​(s),s˙⟩=⟨G​(s),s˙⟩\displaystyle\left\langle\nabla J(s),\dot{s}\right\rangle=\left\langle G(s),\dot{s}\right\rangle |  | (94) |
|  |  | =\displaystyle= | ⟨G​(s),B1​w⟩−⟨G​(s),Ds​A​s+F​(s)+B2​B2∗​G​(s)⟩\displaystyle\langle G(s),B\_{1}w\rangle-\left\langle G(s),D\_{s}As+F(s)+B\_{2}B\_{2}^{\*}G(s)\right\rangle |  |
|  |  | =\displaystyle= | ⟨B1∗​G​(s),w⟩−12​γ2​|B1∗G​(s)|2−12​|B2∗​G​(s)|2−12​|C​s|2\displaystyle\langle B\_{1}^{\*}G(s),w\rangle-\frac{1}{2\gamma^{2}}|B\_{1}\*G(s)|^{2}-\frac{1}{2}|B\_{2}^{\*}G(s)|^{2}-\frac{1}{2}|Cs|^{2} |  |
|  |  | ≤\displaystyle\leq | γ22​|w|2+12​γ2​|B1∗G​(s)|2−12​γ2​|B1∗G​(s)|2−12​|B2∗​G​(s)|2−12​|C​s|2\displaystyle\frac{\gamma^{2}}{2}|w|^{2}+\frac{1}{2\gamma^{2}}|B\_{1}\*G(s)|^{2}-\frac{1}{2\gamma^{2}}|B\_{1}\*G(s)|^{2}-\frac{1}{2}|B\_{2}^{\*}G(s)|^{2}-\frac{1}{2}|Cs|^{2} |  |
|  |  | =\displaystyle= | γ22​|w|2−12​|B2∗​G​(s)|2−12​|C​s|2.\displaystyle\frac{\gamma^{2}}{2}|w|^{2}-\frac{1}{2}|B\_{2}^{\*}G(s)|^{2}-\frac{1}{2}|Cs|^{2}. |  |

Integrating the inequality from 0 to +∞+\infty yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(+∞)−J​(s0)<γ22​∫0+∞|w|2​𝑑t−12​∫0+∞(|C​s|2+|B2∗​G|2)​𝑑t.J(+\infty)-J(s\_{0})<\frac{\gamma^{2}}{2}\int\limits\_{0}^{+\infty}|w|^{2}dt-\frac{1}{2}\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}G|^{2}\right)dt. |  | (95) |

Based on the fact that J​(+∞)=0J(+\infty)=0 and the relation ([92](https://arxiv.org/html/2511.11909v1#S4.E92 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​∫0+∞(|C​s|2+|B2∗​G|2)​𝑑t−γ22​∫0+∞|w|2​𝑑t<k​|s0|2.\frac{1}{2}\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}G|^{2}\right)dt-\frac{\gamma^{2}}{2}\int\limits\_{0}^{+\infty}|w|^{2}dt<k|s\_{0}|^{2}. |  | (96) |

When calculating the H∞H^{\infty} problem, the initial condition s0s\_{0} needs to be set to zero; therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0+∞(|C​s|2+|B2∗​G|2)​𝑑t<γ2​∫0+∞|w|2​𝑑t.\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}G|^{2}\right)dt<\gamma^{2}\int\limits\_{0}^{+\infty}|w|^{2}dt. |  | (97) |

Hence, the H∞H^{\infty} norm of the mapping from the disturbance w​(t)w(t) to the output of the system is less than γ\gamma, just as in the linear case.

### 4.5 Stability analysis for the nonlinear system with no disturbances

Now the stability analysis for the original nonlinear state equations is the only remaining issue. The objective here is to show that the norm of s​(t)s(t) in the space L2​(0,∞;L2​(Ω))L^{2}(0,\infty;L^{2}(\Omega)) is bounded.

Consider the nonlinear equation without disturbances but with feedback control u=−B2∗​G​(s)u=-B\_{2}^{\*}G(s)

|  |  |  |  |
| --- | --- | --- | --- |
|  | s˙+Ds​A​s+F0​s+FN​(s)+B2​B2∗​G​(s)=0.\dot{s}+D\_{s}As+F\_{0}s+F\_{N}(s)+B\_{2}B\_{2}^{\*}G(s)=0. |  | (98) |

Because it is assumed that the pair (Ds​A+F0,C)(D\_{s}A+F\_{0},C) is detectable, then there exists a bounded operator DD, such that
−(Ds​A+F0+D​C)-(D\_{s}A+F\_{0}+DC) generates an exponentially stable semigroup. Rewrite equation ([98](https://arxiv.org/html/2511.11909v1#S4.E98 "In 4.5 Stability analysis for the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | s˙+(Ds​A+F0+D​C)​s=D​C​s−B2​B2∗​G​(s)−FN​(s).\dot{s}+(D\_{s}A+F\_{0}+DC)s=DCs-B\_{2}B\_{2}^{\*}G(s)-F\_{N}(s). |  | (99) |

Then there exists a constant b>0b>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |s​(t)|≤e−b​t​|s0|+∫0te−b​(t−r)​|D​C​s−B2​B2∗​G​(s)−FN​(s)|​𝑑r.|s(t)|\leq e^{-bt}|s\_{0}|+\int\limits\_{0}^{t}e^{-b(t-r)}|DCs-B\_{2}B\_{2}^{\*}G(s)-F\_{N}(s)|dr. |  | (100) |

Integrating from 0 to +∞+\infty and applying Young’s inequality for convolution yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s​(t)‖2=∫0+∞|s​(t)|2​𝑑t≤C​|s0|2+C​∫0+∞(|C​s|2+|B2∗​G|2+|FN​(s)|2)​𝑑t.\|s(t)\|^{2}=\int\limits\_{0}^{+\infty}|s(t)|^{2}dt\leq C|s\_{0}|^{2}+C\int\limits\_{0}^{+\infty}\left(|Cs|^{2}+|B\_{2}^{\*}G|^{2}+|F\_{N}(s)|^{2}\right)dt. |  | (101) |

Applying relation ([92](https://arxiv.org/html/2511.11909v1#S4.E92 "In 4.3 Conditions for the solution to the Hamilton-Jacobi equation for the nonlinear system ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) and substituting w​(t)=0w(t)=0 gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s​(t)‖2≤(C+k)​|s0|2+C​∫0+∞|FN​(s)|2​𝑑t.\|s(t)\|^{2}\leq(C+k)|s\_{0}|^{2}+C\int\limits\_{0}^{+\infty}|F\_{N}(s)|^{2}dt. |  | (102) |

If (s,p)∈Σμ(s,p)\in\Sigma\_{\mu}, that is, ‖s​(t)‖≤μ\|s(t)\|\leq\mu, the following quadratic estimate for |FN​(s)|2=|c2S​s2|2|F\_{N}(s)|^{2}=\left|\frac{c\_{2}}{S}s^{2}\right|^{2} holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |FN​(s)|2≤C​|s​(t)|4≤C​μ2​|s​(t)|2.|F\_{N}(s)|^{2}\leq C|s(t)|^{4}\leq C\mu^{2}|s(t)|^{2}. |  | (103) |

Substituting this inequality into equation ([102](https://arxiv.org/html/2511.11909v1#S4.E102 "In 4.5 Stability analysis for the nonlinear system with no disturbances ‣ 4 Optimal control for the nonlinear system ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−C​μ2)​‖s​(t)‖2≤(C+k)​|s0|2.(1-C\mu^{2})\|s(t)\|^{2}\leq(C+k)|s\_{0}|^{2}. |  | (104) |

If it is then required that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−C​μ2>0,1-C\mu^{2}>0, |  | (105) |

in which case

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ<1C.\mu<\frac{1}{\sqrt{C}}. |  | (106) |

This provides the following sufficient condition on the solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖s​(t)‖2≤C+k1−C​μ2​|s0|2<∞,\|s(t)\|^{2}\leq\frac{C+k}{1-C\mu^{2}}|s\_{0}|^{2}<\infty, |  | (107) |

from which we can conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→+∞|s​(t)|=0.\lim\limits\_{t\rightarrow+\infty}|s(t)|=0. |  | (108) |

Therefore, the nonlinear system is locally asymptotically stable.

## 5 Conclusions

A nonlinear partial differential reaction-diffusion equation is used to describe the evolution of financial distress in financial networks. The equation includes a diffusion term capturing the distress propagation and a reaction term capturing local amplification of stress level. Because s​(x)=0s(x)=0 corresponds to the case with zero stress level, it is sought to stabilize the system about this state. A stabilizing feedback controller of the corresponding linearized system is constructed based on the solution to the algebraic Riccati equation, and norm estimation of the linearized system with forcing terms is obtained via semi-group theory. Based on this norm estimation, unique existence of the solution to the controlled nonlinear system equation is proved by showing that the solution is a fixed point of a contraction mapping. Finally, the nonlinear state equation describing financial distress propagation and amplification is then stabilized about s​(x)=0s(x)=0 via a feedback controller given by the solution of the Hamilton-Jacobi equation.

The resulted control u​(x,t)u(x,t) is a state feedback that depends on financial distress diffusion coefficient and the nonlinear local amplification term. In this setting, the distress levels are measured spatially (across different geographical regions or across sectors), and the spatial distribution of control input is computed at government or regulator level. Then local value of control input u​(x)u(x) for a given time tt is sent to location xx to execute locally. The spatial distribution of the control input u​(x,t)u(x,t) also helps to identify the sub-areas like a specific region or sector that needs financial intervention most.
The local control input mapped to real world can take the forms of Bank-specific liquidity assistance or recapitalization programs, targeted purchase programs for specific markets, emergency credit facilities directed at key sectors, etc. With the collaboration of all local decentralized executions of control inputs u​(x,t)u(x,t), the overall financial system will achieve stability as a whole. This approach fits well into the new modern financial policy making paradigm where global financial goals are achieved by the synergy of multiple policy-guided decentralized efforts.

Beyond the applications in financial distress control, because equation ([1](https://arxiv.org/html/2511.11909v1#S1.E1 "In 1 Introduction ‣ Modeling and Stabilizing Financial Systemic Risk Using Optimal Control Theory")) is a generic reaction-diffusion equation, with the reaction being modeled as a nonlinear logistic growth term, the presented results may suggest approaches to be applied to similar mathematical models in other physical applications.