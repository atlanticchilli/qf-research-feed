---
authors:
- Yijie Huang
- Mengge Li
- Xiang Yu
- Zhou Zhou
doc_id: arxiv:2512.04697v1
family_id: arxiv:2512.04697
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Continuous-time reinforcement learning for optimal switching over multiple
  regimes
url_abs: http://arxiv.org/abs/2512.04697v1
url_html: https://arxiv.org/html/2512.04697v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yijie Huang
Department of Applied Mathematics, The Hong Kong Polytechnic University, Kowloon, Hong Kong. Email:<yijie.huang@polyu.edu.hk>
  
Mengge Li
Department of Applied Mathematics, The Hong Kong Polytechnic University, Kowloon, Hong Kong. Email:<meng-ge.li@polyu.edu.hk>
  
Xiang Yu
Department of Applied Mathematics, The Hong Kong Polytechnic University, Kowloon, Hong Kong. Email:<xiang.yu@polyu.edu.hk>
  
Zhou Zhou
School of Mathematics and Statistics, University of Sydney, Sydney, Australia. Email:<zhou.zhou@sydney.edu.au>

###### Abstract

This paper studies the continuous-time reinforcement learning (RL) for optimal switching problems across multiple regimes. We consider a type of exploratory formulation under entropy regularization where the agent randomizes both the timing of switches and the selection of regimes through the generator matrix of an associated continuous-time finite-state Markov chain. We establish the well-posedness of the associated system of Hamilton-Jacobi-Bellman (HJB) equations and provide a characterization of the optimal policy. The policy improvement and the convergence of the policy iterations are rigorously established by analyzing the system of equations. We also show the convergence of the value function in the exploratory formulation towards the value function in the classical formulation as the temperature parameter vanishes. Finally, a reinforcement learning algorithm is devised and implemented by invoking the policy evaluation based on the martingale characterization. Our numerical examples with the aid of neural networks illustrate the effectiveness of the proposed RL algorithm.

Keywords: Optimal regime switching, multiple regimes, continuous-time reinforcement learning, system of HJB equations, policy improvement, policy iteration convergence

## 1 Introduction

The optimal switching problem across multiple regimes entails solving a stochastic optimization problem in which the admissible strategies are formalized by sequences of discrete interventions. A decision-maker in this context faces two basic questions: (i) when to switch from the current regime to another, and (ii) which regime to select when the decision of switching is made. These problems are characterized by their hybrid nature, combining continuous state dynamics with discrete control actions, where each switch between regimes typically incurs a cost while different regimes yield different reward outcomes. Over recent decades, the optimal switching problem has found extensive applications across different fields. Seminal work includes carmona2008pricing on pricing asset scheduling, carmona2010valuation on energy storage valuation, porchet2009valuation on power plant valuation, and olofsson2022management on hydropower production planning, among others.

The classical stochastic control problem typically assumes a fully known and accurate underlying model. However, this assumption of complete model knowledge often turns out to be unrealistic in practical applications. RL offers a powerful framework for learning optimal strategies in the unknown environment through trial-and-error interactions. While most conventional RL algorithms are designed in discrete-time settings, many real-world applications evolve continuously in time, motivating a systemic study in theories and algorithms for the continuous-time RL approach. Within the continuous-time framework, decision-makers face the fundamental exploration-exploitation trade-off in a continuous-time manner: whether to exploit current knowledge by executing the best-known policy or to explore alternative actions to gather information for potential long-term improvement. wang2020reinforcement addressed this problem by introducing an entropy-regularization on the randomized policy to encourage the exploration. This fundamental study spurred further pioneer studies of theories and algorithms in the continuous-time exploratory framework including jia2022policy; jia2022gradient; jia2023q, laying the foundations for the policy evaluation, the policy gradient, and the continuous-time q-learning, respectively. Later, the well-posedness of the exploratory HJB equation, the convergence of policy iterations and the regret analysis have also been examined in tang2022exploratory; huang2025convergence; tran2025policy; t-z-regret.

In addition, vast extensions and applications of continuous-time RL algorithms in various context have been considered in the recent literature. To name a few, wu2024reinforcement addressed the continuous-time mean-variance portfolio selection problem in regime-switching markets with unobservable states using reinforcement learning approach; bo2025optimal extended the q-learning theory in the model of reflected diffusion processes and applied it to learn the optimal tracking portfolio in incomplete markets; wei2025continuous generalized the continuous-time q-learning to mean-field control problems within McKean-Vlasov diffusion models; wyy2024 further developed the continuous-time q-learning for both mean-field control and mean-field game problems from the perspective of the representative agent; gao2024reinforcement studied the extension of q-learning in jump-diffusion models; bo2024continuous examined the same jump-diffusion model by invoking the Tsallis entropy; dong2024randomized investigated the optimal stopping in an exploratory framework by considering the randomization of stopping time via the intensity control; dianetti2024exploratory utilized the randomization of stopping times as singular control and studied its exploratory formulation under residual entropy regularization; dai2024learning exploited the penalization method to transform the optimal stopping problem to an optimal control problem for which the entropy regularization is formalized; liang2025reinforcement proposed a continuous-time RL framework for singular stochastic control problems without entropy regularization, characterizing the optimal control through singular control laws; liang2025reinforcement-2 further proposed a type of randomization of the singular control laws in liang2025reinforcement by considering an auxiliary singular control and entropy regularization, which lead to a time-inconsistent two-stage optimal control problem such that the task is to learn the time-consistent equilibrium.

Despite these advancements of continuous-time RL in different model setups, its application to optimal regime switching problems remains relatively underexplored. This paper studies the exploratory formulation of the optimal regime switching with multiple regimes and bridges its connection to the classical optimal switching problem as the entropy regularization vanishes. To this end, we propose a type of exploratory formulation where the decision-maker randomizes both switching time and the selection of the targeted regime state by invoking a generator matrix of an associated continuous-time Markov chain (CTMC) defined on finite state space. The entropy regularization on the generator is imposed to encourage the exploration. Specifically, we utilize the inherent property of the CTMC—particularly its jump times and state transitions—to determine the switching decision. This formulation, governed by the control of the CTMC’s generator matrix, transformed the randomized switching problem into an optimal control problem.

We summarize the main contributions of the present paper as follows:

* (i)

  We derive the system of exploratory HJB equations and establish the existence of a bounded classical solution to this system (see Lemma [3.2](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) by resorting to some established partial differential equation (PDE) theories together with a tailor-made truncation argument. Furthermore, we prove its uniqueness and demonstrate through a verification theorem (see Proposition [3.3](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem3 "Proposition 3.3 (Verification Theorem). ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) that this solution coincides with the value function.
* (ii)

  We employ the policy iteration (PI) method to learn the optimal strategy through iterative updates and prove the policy improvement result in Proposition [4.1](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"). As the main result of this paper, in the context of PDE system, we establish the convergence result of the policy iteration in Theorem [4.2](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") with an explicit convergence rate, which is new to the literature.
* (iii)

  We also draw the connection to the classical optimal switching problem by establishing the convergence of the value function in the exploratory formulation towards the value function of the classical optimal switching problem as the temperature parameter approaches zero. To this end, we resort to some delicate stability analysis of viscosity solutions of the PDE system, see Lemma [4.3](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and Theorem [4.4](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"). In particular, it is shown that the solution of the system of PDEs will converge to the solution of the system of variational inequalities as the temperature parameter tends to zero.
* (iv)

  We develop a reinforcement learning algorithm by implementing a policy evaluation method based on martingale characterization, which calls for the stochastic approximation when using the martingale orthogonality condition. We obtain an explicit error analysis for the convergence of this stochastic approximation method in Theorem [5.4](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem4 "Theorem 5.4. ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"). To illustrate the effectiveness of our proposed RL algorithm, we conducted numerical experiments in two examples with satisfactory iteration convergence, both necessitate the application of neural networks to parameterize the targeted functions.

Let us also briefly compare the present work with three recent related studies. denkert2025control introduced a control randomization method without entropy regularization in continuous-time RL with the application to optimal switching problems. They developed an Actor-Critic policy gradient algorithm that alternately learns the value function and the optimal intensity policy. In contrast, our paper propose a different randomization approach for the optimal switching problem, utilizing the generator matrix of a CTMC and incorporating entropy regularization to encourage the exploration. A key advantage of our formulation is that the optimal policy depends explicitly on the value function itself, without requiring any of its derivatives. This allows us to parameterize both the policy and the value function using the same set of parameters. More recently, dai2025reinforcement developed a RL approach to identify arbitrage strategies in stock index futures. Following the randomization method in dong2024randomized, they randomized the switching times in dai2025reinforcement using the Cox processes and formulated the problem as an optimal switching problem with three regimes where the state process is independent of the regimes. In comparison, we consider an exploratory framework for a more general multi-regime optimal switching problem, where the state process dynamics can also depend on the regime states. Furthermore, we rigorously establish the convergence of the policy iterations with an explicit convergence rate and also show the convergence as the entropy regularization vanishes. Finally, our work differs from cao2025two, which studied a randomization scheme for impulse control problems characterized by fixed points of compound operators combining regularized nonlocal and stopping operators. In contrast, our distinct exploratory formulation leads to the study of PDE system instead of a single PDE problem, for which we need to develop some delicate analysis for the system of equations to deduce some desired convergence results.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2512.04697v1#S2 "2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") reviews the classical optimal switching problem and presents preliminary results on viscosity solutions to the associated system of HJB variational inequalities. Section [3](https://arxiv.org/html/2512.04697v1#S3 "3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") introduces the exploratory formulation of the optimal switching problem, providing a regularity analysis of the value function and the characterization of the optimal policy. Section [4](https://arxiv.org/html/2512.04697v1#S4 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") establishes both policy improvement and the convergence result of the policy iteration. Moreover, the convergence behavior of the exploratory solution as the temperature parameter vanishes is also discusses therein. Section [5](https://arxiv.org/html/2512.04697v1#S5 "5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") develops a reinforcement learning algorithm that implements the martingale-based policy evaluation and the previous policy iteration, accompanied by an error analysis for the proposed algorithm. Finally, Section [6](https://arxiv.org/html/2512.04697v1#S6 "6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") presents some numerical examples demonstrating the satisfactory performance of our proposed RL algorithm.

Notations. We specify the following list of notations for the rest of this paper.

* •

  ℝn\mathds{R}^{n} denotes the nn-dimensional Euclidean space. For all x=(x1,⋯,xn),y=(y1,⋯,yn)∈ℝnx=(x\_{1},\cdots,x\_{n}),y=(y\_{1},\cdots,y\_{n})\in\mathds{R}^{n}, we denote by ⋅\cdot the scalar product and by |⋅||\cdot| the Euclidean norm:

  |  |  |  |
  | --- | --- | --- |
  |  | x⋅y=∑i=1nxi​yi,|x|=x⋅x=∑i=1nxi2.\displaystyle x\cdot y=\sum\_{i=1}^{n}x\_{i}y\_{i},\quad|x|=\sqrt{x\cdot x}=\sqrt{\sum\_{i=1}^{n}x\_{i}^{2}}. |  |
* •

  ℝn×d\mathds{R}^{n\times d} is the set of real-valued n×dn\times d matrices. For σ∈ℝn×d\sigma\in\mathds{R}^{n\times d}, we denote by σ⊤\sigma^{\top} the transpose matrix of σ\sigma. For A=(ai​j)1≤i,j≤n∈ℝn×nA=(a\_{ij})\_{1\leq i,j\leq n}\in\mathds{R}^{n\times n}, tr​(A)=∑i=1nai​i\text{tr}(A)=\sum\_{i=1}^{n}a\_{ii} is the trace of AA. We define the matrix norm on ℝn×d\mathds{R}^{n\times d} as |σ|=(tr​(σ​σ⊤))12|\sigma|=(\text{tr}(\sigma\sigma^{\top}))^{\frac{1}{2}}.
* •

  For 𝒪⊂ℝn{\cal O}\subset\mathds{R}^{n}, Ck​(𝒪)C^{k}({\cal O}) is the space of all real-valued continuous functions on 𝒪{\cal O} with continuous derivatives up to order kk. For T≥0T\geq 0, C1,2​([0,T]×𝒪)C^{1,2}([0,T]\times{\cal O}) is the space of real-valued functions uu on [0,T]×𝒪[0,T]\times{\cal O} whose partial derivatives ∂u∂t,∂u∂xi,∂2u∂xi​xj\frac{\partial u}{\partial t},\frac{\partial u}{\partial x\_{i}},\frac{\partial^{2}u}{\partial x\_{i}x\_{j}}, 1≤i,j≤n1\leq i,j\leq n, exist and are continuous on [0,T]×𝒪[0,T]\times{\cal O}. For u∈C2​(𝒪)u\in C^{2}({\cal O}), we denote by Dx​uD\_{x}u the gradient vector of uu and Dx2​uD\_{x}^{2}u the Hessian matrix of uu.
* •

  For points P=(t,x),P′=(t,x)∈[0,T]×ℝnP=(t,x),P^{\prime}=(t,x)\in[0,T]\times\mathds{R}^{n}, we define the parabolic distance between PP and P′P^{\prime} by

  |  |  |  |
  | --- | --- | --- |
  |  | d​(P,P′)=(|t−t′|+|x−x′|2)12.\displaystyle d(P,P^{\prime})=(|t-t^{\prime}|+|x-x^{\prime}|^{2})^{\frac{1}{2}}. |  |
* •

  For 𝒟⊂[0,T]×ℝn{\cal D}\subset[0,T]\times\mathds{R}^{n} and α∈(0,1)\alpha\in(0,1) we introduce the following norms for functions defined on 𝒟{\cal D}:

  |  |  |  |
  | --- | --- | --- |
  |  | ‖u‖C0​(𝒟)=supP∈𝒟|f​(P)|,‖u‖Cα​(𝒟)=‖u‖C0​(𝒟)+supP,P′∈𝒟,P≠P′|u​(P)−u​(P′)|d​(P,P′)α,\displaystyle||u||\_{C^{0}({\cal D})}=\sup\_{P\in{\cal D}}|f(P)|,\quad||u||\_{C^{\alpha}({\cal D})}=||u||\_{C^{0}({\cal D})}+\sup\_{P,P^{\prime}\in{\cal D},P\neq P^{\prime}}\frac{|u(P)-u(P^{\prime})|}{d(P,P^{\prime})^{\alpha}}, |  |
  |  |  |  |
  | --- | --- | --- |
  |  | ‖u‖C1​(𝒟)=‖u‖C0​(𝒟)+∑i=1n‖∂u∂xi‖C0​(𝒟),‖u‖C1+α​(𝒟)=‖u‖Cα​(𝒟)+∑i=1n‖∂u∂xi‖Cα​(𝒟),\displaystyle||u||\_{C^{1}({\cal D})}=||u||\_{C^{0}({\cal D})}+\sum\_{i=1}^{n}\left|\left|\frac{\partial u}{\partial x\_{i}}\right|\right|\_{C^{0}({\cal D})},\quad||u||\_{C^{1+\alpha}({\cal D})}=||u||\_{C^{\alpha}({\cal D})}+\sum\_{i=1}^{n}\left|\left|\frac{\partial u}{\partial x\_{i}}\right|\right|\_{C^{\alpha}({\cal D})}, |  |
  |  |  |  |
  | --- | --- | --- |
  |  | ‖u‖C2​(𝒟)=‖u‖C1​(𝒟)+∑i=1n‖∂u∂xi‖C1​(𝒟)+‖∂u∂t‖C0​(𝒟),\displaystyle||u||\_{C^{2}({\cal D})}=||u||\_{C^{1}({\cal D})}+\sum\_{i=1}^{n}\left|\left|\frac{\partial u}{\partial x\_{i}}\right|\right|\_{C^{1}({\cal D})}+\left|\left|\frac{\partial u}{\partial t}\right|\right|\_{C^{0}({\cal D})}, |  |
  |  |  |  |
  | --- | --- | --- |
  |  | ‖u‖C2+α​(𝒟)=‖u‖C1+α​(𝒟)+∑i=1n‖∂u∂xi‖C1+α​(𝒟)+‖∂u∂t‖Cα​(𝒟).\displaystyle||u||\_{C^{2+\alpha}({\cal D})}=||u||\_{C^{1+\alpha}({\cal D})}+\sum\_{i=1}^{n}\left|\left|\frac{\partial u}{\partial x\_{i}}\right|\right|\_{C^{1+\alpha}({\cal D})}+\left|\left|\frac{\partial u}{\partial t}\right|\right|\_{C^{\alpha}({\cal D})}. |  |

  We shall say that function u​(t,x)u(t,x) is in Cq​(𝒟)C^{q}({\cal D}) if ‖u‖Cq​(𝒟)||u||\_{C^{q}({\cal D})} is finite (q=0,α,1+α,2+αq=0,\alpha,1+\alpha,2+\alpha).

## 2 Classical Optimal Switching Problem

This section first reviews the classical optimal switching problem and introduce some preliminary results on viscosity solutions to the associated system of HJB variational inequalities.

We fix a complete probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), supporting a dd-dimensional standard Brownian motion W=(Wt)t≥0W=(W\_{t})\_{t\geq 0}. We denote by 𝔽\mathbb{F} the complete and right continuous filtration generated by WW. The terminal time is denoted by T>0T>0. Let us introduce the domain 𝒟:=[0,T)×ℝn{\cal D}:=[0,T)\times\mathds{R}^{n}, then the closure of 𝒟{\cal D} is given by 𝒟¯=[0,T]×ℝn\overline{{\cal D}}=[0,T]\times\mathds{R}^{n}.

We then define the set 𝒜t\mathcal{A}\_{t} of admissible switching controls at time t∈[0,T]t\in[0,T] as the set of double sequences α=(τk,κk)k≥0\alpha=(\tau\_{k},\kappa\_{k})\_{k\geq 0}, where (τk)k≥0\left(\tau\_{k}\right)\_{k\geq 0} is a non-decreasing sequence of 𝔽\mathbb{F}-stopping times with τ0=t\tau\_{0}=t and limk→∞τk>T\lim\_{k\rightarrow\infty}\tau\_{k}>T; κk\kappa\_{k} is an ℱτk\mathcal{F}\_{\tau\_{k}}-measurable random variable valued in the set 𝕀m={1,2,⋯,m}\mathbb{I}\_{m}=\{1,2,\cdots,m\}. With a strategy α=(τk,κk)k≥0∈𝒜t\alpha=\left(\tau\_{k},\kappa\_{k}\right)\_{k\geq 0}\in\mathcal{A}\_{t} and an initial regime value i∈𝕀mi\in\mathbb{I}\_{m}, we associate the process (Ist,i)s≥t(I\_{s}^{t,i})\_{s\geq t} defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ist,i=∑k≥0κk​𝟏s∈[τk,τk+1),s≥t,It−t,i=κ0=i.\displaystyle I\_{s}^{t,i}=\sum\_{k\geq 0}\kappa\_{k}{\bf 1}\_{s\in[\tau\_{k},\tau\_{k+1})},\penalty 10000\ s\geq t,\quad I^{t,i}\_{t-}=\kappa\_{0}=i. |  | (2.1) |

Given (t,x,i)∈[0,T]×ℝn×𝕀m(t,x,i)\in[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}, and a switching control α∈𝒜t\alpha\in\mathcal{A}\_{t}, we consider the controlled diffusion Xt,x,i,α=(Xst,x,i,α)s∈[t,T]X^{t,x,i,\alpha}=(X\_{s}^{t,x,i,\alpha})\_{s\in[t,T]} governed by the SDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​Xst,x,i,α=μ​(s,Xst,x,i,α,Ist,i)​d​s+σ​(s,Xst,x,i,α,Ist,i)​d​Ws,s∈(t,T].\displaystyle dX^{t,x,i,\alpha}\_{s}=\mu(s,X^{t,x,i,\alpha}\_{s},I\_{s}^{t,i})ds+\sigma(s,X^{t,x,i,\alpha}\_{s},I\_{s}^{t,i})dW\_{s},\quad s\in(t,T]. |  | (2.2) |

with Xtt,x,i,α=xX\_{t}^{t,x,i,\alpha}=x. We have the following assumptions for the model coefficients.

###### Assumption 2.1.

* (i)

  The drift μ​(⋅,⋅,⋅):[0,T]×ℝn×𝕀m→ℝn\mu(\cdot,\cdot,\cdot):[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}\to\mathds{R}^{n} and volatility σ​(⋅,⋅,⋅):[0,T]×ℝn×𝕀m→ℝn×d\sigma(\cdot,\cdot,\cdot):[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}\to\mathds{R}^{n\times d} are
  uniformly Lipschitz continuous with respect to xx, that is, there exists a constant L>0L>0 such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |μ​(s,x1,i)−μ​(s,x2,i)|+|σ​(s,x1,i)−σ​(s,x2,i)|≤L​|x1−x2|\displaystyle|\mu(s,x\_{1},i)-\mu(s,x\_{2},i)|+|\sigma(s,x\_{1},i)-\sigma(s,x\_{2},i)|\leq L|x\_{1}-x\_{2}| |  | (2.3) |

  for all (s,x1,x2,i)∈[0,T]×ℝ2​n×𝕀m(s,x\_{1},x\_{2},i)\in[0,T]\times\mathds{R}^{2n}\times\mathbb{I}\_{m}.
* (ii)

  There exist some constant σ0>0\sigma\_{0}>0 such that, for all (t,x,i)∈𝒟¯×𝕀m(t,x,i)\in\overline{{\cal D}}\times\mathbb{I}\_{m} and ξ∈ℝn\xi\in\mathds{R}^{n},

  |  |  |  |
  | --- | --- | --- |
  |  | ξ​σ​(t,x,i)​σ⊤​(t,x,i)​ξ⊤≥σ0​ξ​ξ⊤.\displaystyle\xi\sigma(t,x,i)\sigma^{\top}(t,x,i)\xi^{\top}\geq\sigma\_{0}\xi\xi^{\top}. |  |

The expected total profit with the initial state (t,x,i)(t,x,i) and the impulse control α=(τk,κk)k≥0∈𝒜t\alpha=\left(\tau\_{k},\kappa\_{k}\right)\_{k\geq 0}\in\mathcal{A}\_{t} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ji​(t,x;α)=𝔼​[∫tTf​(s,Xst,x,i,α,Ist,i)​𝑑s−∑k=1∞gκk−1​κk​𝟏{τk≤T}+h​(XTt,x,i,α)],\displaystyle J\_{i}(t,x;\alpha)=\mathbb{E}\bigg[\int\_{t}^{T}f(s,X\_{s}^{t,x,i,\alpha},I\_{s}^{t,i})ds-\sum\limits\_{k=1}^{\infty}g\_{\kappa\_{k-1}\kappa\_{k}}{\bf 1}\_{\{\tau\_{k}\leq T\}}+h(X\_{T}^{t,x,i,\alpha})\bigg], |  | (2.4) |

where f​(⋅,⋅,⋅):[0,T]×ℝn×𝕀m→ℝf(\cdot,\cdot,\cdot):[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}\to\mathds{R} is the running profit function, h​(⋅):ℝn→ℝh(\cdot):\mathds{R}^{n}\to\mathds{R} is the terminal reward function, and the constant gi​jg\_{ij} denotes the cost for switching from regime ii to jj for all i≠ji\neq j. We also impose the following assumptions.

###### Assumption 2.2.

* (i)

  For i∈𝕀mi\in\mathbb{I}\_{m}, the running profit f​(⋅,⋅,i)f(\cdot,\cdot,i) and terminal reward h​(⋅)h(\cdot) are assumed to be continuous. Furthermore, there exists a constant Kf,h>0K\_{f,h}>0 such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |f​(t,x,i)|+|h​(x)|≤Kf,h,∀(t,x,i)∈[0,T]×ℝn×𝕀m.\displaystyle|f(t,x,i)|+|h(x)|\leq K\_{f,h},\quad\forall(t,x,i)\in[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}. |  | (2.5) |
* (ii)

  For i,j∈𝕀mi,j\in\mathbb{I}\_{m} with j≠ij\neq i, the cost for switching from regime ii to jj is positive, that is, gi​j>0g\_{ij}>0, with the convention gi​i=0g\_{ii}=0. For i,j,k∈𝕀mi,j,k\in\mathbb{I}\_{m} with j≠i,kj\neq i,k, it is less expensive to switch directly in one step from regime ii to kk than in two steps via an intermediate regime jj, that is, gi​k<gi​j+gj​kg\_{ik}<g\_{ij}+g\_{jk}.

The objective is to maximize the expected total profit over all strategies α\alpha.
Accordingly, the classical value functions is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi​(t,x)=supα∈𝒜tJi​(t,x;α),(t,x,i)∈[0,T]×ℝn×𝕀m.\displaystyle V\_{i}(t,x)=\sup\limits\_{\alpha\in\mathcal{A}\_{t}}J\_{i}(t,x;\alpha),\quad(t,x,i)\in[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}. |  | (2.6) |

We now consider the following system of HJB variational inequalities, for i∈𝕀mi\in\mathbb{I}\_{m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | {min⁡{−∂Vi​(t,x)∂t−ℒxi​Vi​(t,x)−f​(t,x,i),Vi​(t,x)−maxj≠i⁡(Vj​(t,x)−gi​j)}=0,(t,x)∈𝒟,Vi​(T,x)=h​(x),x∈ℝn,\displaystyle\begin{cases}\displaystyle\min\left\{-\frac{\partial V\_{i}(t,x)}{\partial t}-\mathcal{L}^{i}\_{x}V\_{i}(t,x)-f(t,x,i),V\_{i}(t,x)-\max\_{j\neq i}(V\_{j}(t,x)-g\_{ij})\right\}=0,\quad(t,x)\in{\cal D},\\ \displaystyle V\_{i}(T,x)=h(x),\quad x\in\mathds{R}^{n},\end{cases} |  | (2.7) |

where the operator ℒxi\mathcal{L}\_{x}^{i} with i∈𝕀mi\in\mathbb{I}\_{m} is defined by

|  |  |  |
| --- | --- | --- |
|  | ℒxi​l​(t,x):=μ​(t,x,i)​Dx​l​(t,x)+12​tr​(σ​σ⊤​(t,x,i)​Dx2​l​(t,x)),for​l​(t,⋅)∈C2​(ℝn).\displaystyle\mathcal{L}\_{x}^{i}l(t,x):=\mu(t,x,i)D\_{x}l(t,x)+\frac{1}{2}\text{tr}(\sigma\sigma^{\top}(t,x,i)D\_{x}^{2}l(t,x)),\quad\text{for}\penalty 10000\ l(t,\cdot)\in C^{2}(\mathds{R}^{n}). |  |

The value function (V1,⋯,Vm)(V\_{1},\cdots,V\_{m}) can be characterized as the viscosity solution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), which is defined as below.

###### Definition 2.1.

Let (u1,⋯,um)(u\_{1},\cdots,u\_{m}) be a mm-uplet of functions defined on 𝒟¯\overline{{\cal D}}, ℝ\mathds{R}-valued and such that ui​(T,x)=h​(x)u\_{i}(T,x)=h(x) for any (i,x)∈𝕀m×ℝn(i,x)\in\mathbb{I}\_{m}\times\mathds{R}^{n}. The mm-uplet (u1,⋯,um)(u\_{1},\cdots,u\_{m}) is called:

* (i)

  a viscosity supersolution (respectively, subsolution) of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) if, for each i∈𝕀mi\in\mathbb{I}\_{m}, uiu\_{i} is lower-semicontinuous (respectively, upper-semicontinuous) on 𝒟{\cal D} and for any (t0,x0)∈𝒟(t\_{0},x\_{0})\in{\cal D} and any test function φi∈C1,2​(𝒟)\varphi\_{i}\in C^{1,2}({\cal D}) such that (t0,x0)(t\_{0},x\_{0}) is a local minimum point of ui−φiu\_{i}-\varphi\_{i} (respectively, maximum), we have

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | min{\displaystyle\min\Bigg\{ | −∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i),\displaystyle-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ui(t0,x0)−maxj≠i(uj(t0,x0)−gi​j)}≥0(respectively, ≤0);\displaystyle\qquad\qquad\quad u\_{i}(t\_{0},x\_{0})-\max\_{j\neq i}(u\_{j}(t\_{0},x\_{0})-g\_{ij})\Bigg\}\geq 0\penalty 10000\ \text{(respectively, $\leq 0$)}; |  |
* (ii)

  a viscosity solution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) if it both a viscosity supersolution and subsolution.

By using a similar proof of Theorem 5.1 in el2013stochastic, we have the comparison principle for the system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")).

###### Lemma 2.3 (Comparison Principle).

Suppose Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Let (u1,⋯,um)(u\_{1},\cdots,u\_{m}) be a bounded viscosity supersolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and (v1,⋯,vm)(v\_{1},\cdots,v\_{m}) be a bounded viscosity subsolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Then vi​(t,x)≤ui​(t,x)v\_{i}(t,x)\leq u\_{i}(t,x) for all (t,x,i)∈𝒟¯×𝕀m(t,x,i)\in\overline{{\cal D}}\times\mathbb{I}\_{m}.

Lemma [2.3](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem3 "Lemma 2.3 (Comparison Principle). ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") will help the proof of uniqueness of viscosity solution. The next result relates the value function (V1,⋯,Vm)(V\_{1},\cdots,V\_{m}) to the system of variational inequalities.

###### Theorem 2.4.

Under Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), the value function (V1,⋯,Vm)(V\_{1},\cdots,V\_{m}) given by ([2.6](https://arxiv.org/html/2512.04697v1#S2.E6 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) is the unique bounded viscosity solution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")).

###### Proof.

We begin by proving that the value function (V1,⋯,Vm)(V\_{1},\cdots,V\_{m}) defined by ([2.6](https://arxiv.org/html/2512.04697v1#S2.E6 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) is bounded. By Assumption [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), for any (i,t,x)∈𝕀m×𝒟¯(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}} and α∈𝒜t\alpha\in{\cal A}\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ji​(t,x,α)\displaystyle J\_{i}(t,x,\alpha) | ≤𝔼​[∫tTf​(s,Xst,x,i,α,Ist,i)​𝑑s+h​(XTt,x,i,α)]\displaystyle\leq\mathbb{E}\bigg[\int\_{t}^{T}f(s,X\_{s}^{t,x,i,\alpha},I\_{s}^{t,i})ds+h(X\_{T}^{t,x,i,\alpha})\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(T−t)​Kf,h+Kf,h,\displaystyle\leq(T-t)K\_{f,h}+K\_{f,h}, |  |

which implies Vi​(t,x)≤(T−t)​Kf,h+Kf,hV\_{i}(t,x)\leq(T-t)K\_{f,h}+K\_{f,h}. For the lower bound, consider the no-switching control τn=∞\tau\_{n}=\infty, n≥1n\geq 1, i.e., Ist,i=iI\_{s}^{t,i}=i, s≥ts\geq t. Applying Assumption [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") again yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi​(t,x)\displaystyle V\_{i}(t,x) | ≥𝔼​[∫tTf​(s,Xst,x,i,α,Ist,i)​𝑑s+h​(XTt,x,i,α)]\displaystyle\geq\mathbb{E}\bigg[\int\_{t}^{T}f(s,X\_{s}^{t,x,i,\alpha},I\_{s}^{t,i})ds+h(X\_{T}^{t,x,i,\alpha})\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥−(T−t)​Kf,h−Kf,h.\displaystyle\geq-(T-t)K\_{f,h}-K\_{f,h}. |  |

Therefore, the value function is bounded. As it is bounded, it follows from Proposition 4.2 in bouchard2009stochastic and Lemma [2.3](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem3 "Lemma 2.3 (Comparison Principle). ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") that the value function (V1,⋯,Vm)(V\_{1},\cdots,V\_{m}) is the unique bounded viscosity solution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")).
∎

## 3 Exploratory Formulation under Entropy Regularization

In this section, we introduce our exploratory formulation of the optimal switching problem, and study the well-posedness of the associated exploratory HJB system as well as the verification theorem.

To explore the system and reward, we let the agent randomize the choice of the stopping times and the regimes that she would like to switch to. Let I:=(It)t≥0I:=(I\_{t})\_{t\geq 0} denote a continuous-time finite-state Markov chain with state space 𝕀m\mathbb{I}\_{m}, which is independent of the Brownian motion WW. The randomization is achieved by considering the choice of the generator, 𝝅=(πti​j)i,j∈𝕀m,t∈[0,T]{\bm{\pi}}=(\pi^{ij}\_{t})\_{i,j\in\mathbb{I}\_{m},t\in[0,T]}, of the Markov chain II. For i≠ji\neq j, πti​j\pi\_{t}^{ij} is the instantaneous intensity of the transition of II from state ii to state jj at time tt. Here, for each t∈[0,T]t\in[0,T], πti​j≥0\pi^{ij}\_{t}\geq 0, for i≠ji\neq j and ∑j=1mπti​j=0\sum\_{j=1}^{m}\pi\_{t}^{ij}=0.

Given (t,x,i)∈[0,T]×ℝn×𝕀m(t,x,i)\in[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m}, we consider the controlled diffusion X=(Xs)s∈[t,T]X=(X\_{s})\_{s\in[t,T]} defined by the following SDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​Xs=μ​(s,Xs,Is)​d​s+σ​(s,Xs,Is)​d​Ws,s∈(t,T].\displaystyle dX\_{s}=\mu(s,X\_{s},I\_{s})ds+\sigma(s,X\_{s},I\_{s})dW\_{s},\quad s\in(t,T]. |  | (3.1) |

with Xt=xX\_{t}=x and It=iI\_{t}=i. For k≥1k\geq 1, denote by τk\tau\_{k} the kk-th jump time of process II with τ0=0\tau\_{0}=0 and κk:=Iτk\kappa\_{k}:=I\_{\tau\_{k}}. For t≥0t\geq 0, let 𝕌t\mathbb{U}\_{t} be the set of all admissable policies (πi​j)i,j∈𝕀m(\pi^{ij})\_{i,j\in\mathbb{I}\_{m}} such that for every i,j∈𝕀mi,j\in\mathbb{I}\_{m}, the process πi​j=(πsi​j)s∈[t,T]\pi^{ij}=(\pi^{ij}\_{s})\_{s\in[t,T]} is 𝔽\mathbb{F}-adapted and satisfies (i) for i≠ji\neq j, πsi​j≥0\pi^{ij}\_{s}\geq 0 for all s∈[t,T]s\in[t,T]; (ii) for every i∈𝕀mi\in\mathbb{I}\_{m}, ∑j=1mπsi​j=0\sum\_{j=1}^{m}\pi\_{s}^{ij}=0, for all s∈[t,T]s\in[t,T].

For 𝝅∈𝕌t{\bm{\pi}}\in\mathbb{U}\_{t}, denote by 𝝅i=(πi​j)j∈𝕀m{\bm{\pi}}^{i}=(\pi^{ij})\_{j\in\mathbb{I}\_{m}} for i∈𝕀mi\in\mathbb{I}\_{m}. To encourage the exploration, we adopt the normalized entropy similar to dong2024randomized that R​(𝝅,i):=∑j≠iπi​j−πi​j​log⁡πi​jR({\bm{\pi}},i):=\sum\_{j\neq i}\pi^{ij}-\pi^{ij}\log\pi^{ij} for i∈𝕀mi\in\mathbb{I}\_{m}. The exploratory formulation of objective functional under entropy regularizer is given by, for (t,x,i)∈[0,T]×ℝn×𝕀m(t,x,i)\in[0,T]\times\mathds{R}^{n}\times\mathbb{I}\_{m} and 𝝅=(πsi​j)i,j∈𝕀m,s∈[t,T]∈𝕌t{\bm{\pi}}=(\pi^{ij}\_{s})\_{i,j\in\mathbb{I}\_{m},s\in[t,T]}\in\mathbb{U}\_{t},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Jiλ​(t,x;𝝅):=𝔼t,x,i​[∫tTf​(s,Xs,Is)​𝑑s−∑k=1∞gκk−1​κk​𝟏{τk≤T}+λ​∫tTR​(𝝅s,Is)​𝑑s+h​(XT)],\displaystyle J\_{i}^{\lambda}(t,x;{\bm{\pi}}):=\mathbb{E}\_{t,x,i}\bigg[\int^{T}\_{t}f(s,X\_{s},I\_{s})ds-\sum\_{k=1}^{\infty}g\_{\kappa\_{k-1}\kappa\_{k}}{\bf 1}\_{\{\tau\_{k}\leq T\}}+\lambda\int^{T}\_{t}R({\bm{\pi}}\_{s},I\_{s})ds+h(X\_{T})\bigg], |  | (3.2) |

where 𝔼t,x,i[⋅]:=𝔼[⋅|Xt=x,It=i]\mathbb{E}\_{t,x,i}[\cdot]:=\mathbb{E}[\cdot|X\_{t}=x,I\_{t}=i], and λ>0\lambda>0 is the temperature parameter. Furthermore, the optimal value function is denoted by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Viλ​(t,x)=sup𝝅∈𝕌tJiλ​(t,x;𝝅).\displaystyle V\_{i}^{\lambda}(t,x)=\sup\_{{\bm{\pi}}\in\mathbb{U}\_{t}}J\_{i}^{\lambda}(t,x;{\bm{\pi}}). |  | (3.3) |

Applying the dynamic programming arguments (c.f. Section 5.3.2 in pham2009continuous), we derive the system of coupled HJB equations as follows: for i∈𝕀mi\in\mathbb{I}\_{m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂Viλ​(t,x)∂t+ℒxi​Viλ​(t,x)+f​(t,x,i)+sup𝝅i{∑j≠iπi​j​(Vjλ​(t,x)−gi​j−Viλ​(t,x))+λ​∑j≠i(πi​j−πi​j​log⁡πi​j)}=0,(t,x)∈𝒟,Viλ​(T,x)=h​(x),x∈ℝn.\displaystyle\begin{cases}\displaystyle\frac{\partial V^{\lambda}\_{i}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}V^{\lambda}\_{i}(t,x)+f(t,x,i)\\ \displaystyle\qquad\quad+\sup\_{{\bm{\pi}}\_{i}}\left\{\sum\_{j\neq i}\pi\_{ij}(V^{\lambda}\_{j}(t,x)-g\_{ij}-V^{\lambda}\_{i}(t,x))+\lambda\sum\_{j\neq i}(\pi\_{ij}-\pi\_{ij}\log\pi\_{ij})\right\}=0,\penalty 10000\ (t,x)\in{\cal D},\\ \displaystyle V^{\lambda}\_{i}(T,x)=h(x),\penalty 10000\ x\in\mathds{R}^{n}.\end{cases} |  | (3.4) |

Using the first-order condition, we arrive at the characterization of the optimal feedback policy by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​j∗​(t,x)=exp⁡(Vjλ​(t,x)−gi​j−Viλ​(t,x)λ),j∈𝕀m∖{i},(t,x)∈𝒟¯.\displaystyle\pi\_{ij}^{\*}(t,x)=\exp\left(\frac{V^{\lambda}\_{j}(t,x)-g\_{ij}-V^{\lambda}\_{i}(t,x)}{\lambda}\right),\quad j\in\mathbb{I}\_{m}\setminus\{i\},\penalty 10000\ (t,x)\in\overline{{\cal D}}. |  | (3.5) |

Plugging ([3.5](https://arxiv.org/html/2512.04697v1#S3.E5 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) into ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Viλ​(t,x)∂t+ℒxi​Viλ​(t,x)+f​(t,x,i)+λ​∑j≠iexp⁡(Vjλ​(t,x)−gi​j−Viλ​(t,x)λ)=0,(t,x)∈𝒟,\displaystyle\frac{\partial V^{\lambda}\_{i}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}V^{\lambda}\_{i}(t,x)+f(t,x,i)+\lambda\sum\_{j\neq i}\exp\left(\frac{V^{\lambda}\_{j}(t,x)-g\_{ij}-V^{\lambda}\_{i}(t,x)}{\lambda}\right)=0,\penalty 10000\ (t,x)\in{\cal D}, |  | (3.6) |

with the terminal condition Viλ​(T,x)=h​(x)V^{\lambda}\_{i}(T,x)=h(x) for x∈ℝnx\in\mathds{R}^{n}.

To establish the well-posedness of the HJB system ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we impose the following assumption.

###### Assumption 3.1.

The running reward function f​(⋅,⋅,i)∈Cα​(𝒟)f(\cdot,\cdot,i)\in C^{\alpha}({\cal D}) for i∈𝕀mi\in\mathbb{I}\_{m} and terminal reward function h​(⋅)∈C2+α​(𝒟)h(\cdot)\in C^{2+\alpha}({\cal D}).

###### Lemma 3.2.

Let Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and [3.1](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Then for any λ>0\lambda>0, the system of HJB equations ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) has a classical solution (V1λ,V2λ,⋯,Vmλ)(V^{\lambda}\_{1},V^{\lambda}\_{2},\cdots,V^{\lambda}\_{m}) with Viλ∈C1,2​(𝒟)∩C​(𝒟¯)V^{\lambda}\_{i}\in C^{1,2}({\cal D})\cap C(\overline{{\cal D}}) for i∈𝕀mi\in\mathbb{I}\_{m}.

###### Proof.

Given M>0M>0, consider a smooth and non-decreasing cut-off function ϕM\phi\_{M} such that ϕM​(x)=ex\phi\_{M}(x)=e^{x} for x≤Mx\leq M, ϕM​(x)≤ex\phi\_{M}(x)\leq e^{x} for x∈(M,M+1)x\in(M,M+1) and ϕM​(x)=eM+1\phi\_{M}(x)=e^{M+1} for x≥M+1x\geq M+1. Hence, ϕM\phi\_{M} is bounded and Lipschitz continuous. Denote 𝒟N:={(t,x):(t,x)∈𝒟,|x|<N}{\cal D}\_{N}:=\{(t,x):(t,x)\in{\cal D},|x|<N\}. First, we will solve the following partial differential equation (PDE) systems: for i∈𝕀mi\in\mathbb{I}\_{m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂ViM,N​(t,x)∂t+ℒxi​ViM,N​(t,x)+f​(t,x,i)+λ​∑j≠iϕM​(VjM,N​(t,x)−ViM,N​(t,x)−gi​jλ)=0,(t,x)∈𝒟N,ViM,N​(t,x)=K​(T−t)+h​(x),(t,x)∈∂𝒟N,\displaystyle\begin{cases}\displaystyle\frac{\partial V\_{i}^{M,N}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}V\_{i}^{M,N}(t,x)+f(t,x,i)+\lambda\sum\_{j\neq i}\phi\_{M}\left(\frac{V^{M,N}\_{j}(t,x)-V^{M,N}\_{i}(t,x)-g\_{ij}}{\lambda}\right)=0,\\[10.00002pt] \displaystyle\hfill(t,x)\in{\cal D}\_{N},\\[10.00002pt] \displaystyle V\_{i}^{M,N}(t,x)=K(T-t)+h(x),\quad(t,x)\in\partial{\cal D}\_{N},\end{cases} |  | (3.7) |

where the constant K>0K>0 is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K:=Kf,h+λ​supi∈𝕀m(∑j≠iexp⁡(−gi​jλ)).\displaystyle K:=K\_{f,h}+\lambda\sup\_{i\in\mathbb{I}\_{m}}\left(\sum\_{j\neq i}\exp\left(-\frac{g\_{ij}}{\lambda}\right)\right). |  | (3.8) |

For i∈𝕀mi\in\mathbb{I}\_{m}, let us introduce the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | ui​(t,x)\displaystyle u\_{i}(t,x) | =K​(T−t)+Kf,h,(t,x)∈𝒟¯N.\displaystyle=K(T-t)+K\_{f,h},\quad(t,x)\in\overline{{\cal D}}\_{N}. |  |

It follows from assumption [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") that

|  |  |  |
| --- | --- | --- |
|  | ∂ui​(t,x)∂t+ℒxi​ui​(t,x)+f​(t,x,i)+λ​∑j≠iϕM​(uj​(t,x)−ui​(t,x)−gi​jλ)\displaystyle\frac{\partial u\_{i}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}u\_{i}(t,x)+f(t,x,i)+\lambda\sum\_{j\neq i}\phi\_{M}\left(\frac{u\_{j}(t,x)-u\_{i}(t,x)-g\_{ij}}{\lambda}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =K+f​(t,x,i)+λ​∑j≠iϕM​(−gi​jλ)≥0,∀(t,x)∈𝒟N,\displaystyle=K+f(t,x,i)+\lambda\sum\_{j\neq i}\phi\_{M}\left(-\frac{g\_{ij}}{\lambda}\right)\geq 0,\quad\forall(t,x)\in{\cal D}\_{N}, |  | (3.9) |

and ui​(t,x)≥Viλ​(t,x)u\_{i}(t,x)\geq V^{\lambda}\_{i}(t,x) for all (t,x)∈∂𝒟N(t,x)\in\partial{\cal D}\_{N}. Similarly, we have

|  |  |  |
| --- | --- | --- |
|  | ∂(−ui​(t,x))∂t+ℒxi​(−ui​(t,x))+f​(t,x,i)+λ​∑j≠iϕM​((−uj​(t,x))−(−ui​(t,x))−gi​jλ)\displaystyle\frac{\partial(-u\_{i}(t,x))}{\partial t}+\mathcal{L}^{i}\_{x}(-u\_{i}(t,x))+f(t,x,i)+\lambda\sum\_{j\neq i}\phi\_{M}\left(\frac{(-u\_{j}(t,x))-(-u\_{i}(t,x))-g\_{ij}}{\lambda}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =−K+f​(t,x,i)+λ​∑j≠iϕM​(−gi​jλ)≤0,∀(t,x)∈𝒟N,\displaystyle=-K+f(t,x,i)+\lambda\sum\_{j\neq i}\phi\_{M}\left(-\frac{g\_{ij}}{\lambda}\right)\leq 0,\quad\forall(t,x)\in{\cal D}\_{N}, |  | (3.10) |

and −ui​(t,x)≤Viλ​(t,x)-u\_{i}(t,x)\leq V\_{i}^{\lambda}(t,x) for all (t,x)∈∂𝒟N(t,x)\in\partial{\cal D}\_{N}. Invoking Theorem 2.1 in kusano1965first, we obtain that system ([3.7](https://arxiv.org/html/2512.04697v1#S3.E7 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) has a classical solution (V1M,N,⋯,VmM,N)(V\_{1}^{M,N},\cdots,V\_{m}^{M,N}), with ViM,N∈C1+δ​(𝒟¯N)V\_{i}^{M,N}\in C^{1+\delta}(\overline{{\cal D}}\_{N}) for any δ∈(0,1)\delta\in(0,1) and ViM,N∈C2+α​(𝒟¯N)V\_{i}^{M,N}\in C^{2+\alpha}(\overline{{\cal D}}\_{N}). Furthermore, we deduce from the comparison theorem (Theorem 1.3 in kusano1965first) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ViM,N​(t,x)|≤ui​(t,x)=K​(T−t)+Kf,h,∀(i,t,x)∈𝕀m×𝒟¯N,\displaystyle|V\_{i}^{M,N}(t,x)|\leq u\_{i}(t,x)=K(T-t)+K\_{f,h},\quad\forall(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}}\_{N}, |  | (3.11) |

which implies that ViM,N​(t,x)V\_{i}^{M,N}(t,x) is bounded. Thus, by choosing some MM large enough, for each i∈𝕀mi\in\mathbb{I}\_{m}, ViN:=ViM,NV^{N}\_{i}:=V^{M,N}\_{i} solves the following PDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂ViN​(t,x)∂t+ℒxi​ViN​(t,x)+f​(t,x,i)+λ​∑j≠iexp⁡(VjN​(t,x)−ViN​(t,x)−gi​jλ)=0,(t,x)∈𝒟N,ViN​(t,x)=K​(T−t)+h​(x),(t,x)∈∂𝒟N.\displaystyle\begin{cases}\displaystyle\frac{\partial V\_{i}^{N}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}V\_{i}^{N}(t,x)+f(t,x,i)+\lambda\sum\_{j\neq i}\exp\left(\frac{V^{N}\_{j}(t,x)-V^{N}\_{i}(t,x)-g\_{ij}}{\lambda}\right)=0,\quad(t,x)\in{\cal D}\_{N},\\[10.00002pt] \displaystyle V\_{i}^{N}(t,x)=K(T-t)+h(x),\quad(t,x)\in\partial{\cal D}\_{N}.\end{cases} |  | (3.12) |

First, we apply Lemma 2 in kusano1965first to the problem ([3.12](https://arxiv.org/html/2512.04697v1#S3.E12 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) to derive for any δ∈(0,1)\delta\in(0,1),

|  |  |  |
| --- | --- | --- |
|  | ‖ViN‖C1+δ​(𝒟N)≤C​(1+‖f​(⋅,⋅,i)‖C0​(𝒟N)+‖h‖C2​(𝒟N)).\displaystyle||V\_{i}^{N}||\_{C^{1+\delta}({\cal D}\_{N})}\leq C\left(1+||f(\cdot,\cdot,i)||\_{C^{0}({\cal D}\_{N})}+||h||\_{C^{2}({\cal D}\_{N})}\right). |  |

In particular, ‖ViN‖Cα​(𝒟N)||V\_{i}^{N}||\_{C^{\alpha}({\cal D}\_{N})} are bounded independently of NN. We then apply Lemma 1 in kusano1965first to the problem ([3.12](https://arxiv.org/html/2512.04697v1#S3.E12 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), obtaining

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ViN‖C2+α​(𝒟N)\displaystyle||V\_{i}^{N}||\_{C^{2+\alpha}({\cal D}\_{N})} | ≤C​(1+‖f​(⋅,⋅,i)‖Cα​(𝒟N)+‖h‖C2+α​(𝒟N))\displaystyle\leq C\left(1+||f(\cdot,\cdot,i)||\_{C^{\alpha}({\cal D}\_{N})}+||h||\_{C^{2+\alpha}({\cal D}\_{N})}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(1+‖f​(⋅,⋅,i)‖Cα​(𝒟)+‖h‖C2+α​(𝒟)).\displaystyle\leq C\left(1+||f(\cdot,\cdot,i)||\_{C^{\alpha}({\cal D})}+||h||\_{C^{2+\alpha}({\cal D})}\right). |  |

Consequently, we can extract from {ViN​(t,x)}\{V\_{i}^{N}(t,x)\} a subsequence converging uniformly in 𝒟¯\overline{{\cal D}} together with the first xx , tt-derivatives and second xx-derivatives to a limit function ViλV\_{i}^{\lambda}, which is a solution to the HJB system ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). The uniqueness of the solution follows from Theorem 1.3 in kusano1965first. Thus, we complete the proof of the theorem.
∎

By the proof of Lemma [3.2](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), for any λ>0\lambda>0, the system of HJB equations ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) admits a classical solution (V1λ,V2λ,⋯,Vmλ)(V^{\lambda}\_{1},V^{\lambda}\_{2},\cdots,V^{\lambda}\_{m}) satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Viλ​(t,x)|≤K​(T−t)+Kf,h,∀(i,t,x)∈𝕀m×𝒟¯,\displaystyle|V\_{i}^{\lambda}(t,x)|\leq K(T-t)+K\_{f,h},\quad\forall(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}}, |  | (3.13) |

where the constant K>0K>0 is given by ([3.8](https://arxiv.org/html/2512.04697v1#S3.E8 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). We now prove that this bounded classical solution is unique and coincides with the value function.

###### Proposition 3.3 (Verification Theorem).

Suppose Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), and [3.1](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold, and let (V1λ,V2λ,⋯,Vmλ)(V\_{1}^{\lambda},V\_{2}^{\lambda},\cdots,V\_{m}^{\lambda}) be a bounded classical solution to system ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), as provided by Lemma [3.2](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"). We define a set of feedback functions by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​j∗​(t,x)=exp⁡(Vjλ​(t,x)−gi​j−Viλ​(t,x)λ),j∈𝕀m∖{i},(t,x)∈𝒟¯,\displaystyle\pi\_{ij}^{\*}(t,x)=\exp\left(\frac{V^{\lambda}\_{j}(t,x)-g\_{ij}-V^{\lambda}\_{i}(t,x)}{\lambda}\right),\quad j\in\mathbb{I}\_{m}\setminus\{i\},\penalty 10000\ (t,x)\in\overline{{\cal D}}, |  | (3.14) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​i∗​(t,x)=−∑j≠iπi​j∗​(t,x),(t,x)∈𝒟¯.\displaystyle\pi\_{ii}^{\*}(t,x)=-\sum\_{j\neq i}\pi\_{ij}^{\*}(t,x),\quad(t,x)\in\overline{{\cal D}}. |  | (3.15) |

Consider the process X∗X^{\*} governed by the dynamics ([3.1](https://arxiv.org/html/2512.04697v1#S3.E1 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), where the generator of the process I∗I^{\*} is given by 𝛑∗=(πti​j,∗)i,j∈𝕀m,t∈[0,T]{\bm{\pi}}^{\*}=(\pi^{ij,\*}\_{t})\_{i,j\in\mathbb{I}\_{m},t\in[0,T]} and πti​j,∗=πi​j∗​(t,Xt∗)\pi\_{t}^{ij,\*}=\pi\_{ij}^{\*}(t,X\_{t}^{\*}). Then, for each i∈𝕀mi\in\mathbb{I}\_{m}, the function ViλV\_{i}^{\lambda} is the value function for problem ([3.3](https://arxiv.org/html/2512.04697v1#S3.E3 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), and the policy 𝛑∗{\bm{\pi}}^{\*} is optimal.

###### Proof.

For (i,t,x)∈𝕀m×𝒟¯(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}}, 𝝅∈𝕌t{\bm{\pi}}\in\mathbb{U}\_{t} and s∈[t,T]s\in[t,T], using Itô’s rule, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIsλ​(s,Xs)\displaystyle V\_{I\_{s}}^{\lambda}(s,X\_{s}) | =Viλ​(t,x)+∫ts(∂VIℓλ​(ℓ,Xℓ)∂t+ℒxi​VIℓλ​(ℓ,Xℓ))​𝑑ℓ+∫ts(Dx​VIℓλ​(ℓ,Xℓ))⊤​σ​(ℓ,Xℓ,Iℓ)​𝑑Wℓ\displaystyle=V\_{i}^{\lambda}(t,x)+\int\_{t}^{s}\left(\frac{\partial V\_{I\_{\ell}}^{\lambda}(\ell,X\_{\ell})}{\partial t}+\mathcal{L}^{i}\_{x}V\_{I\_{\ell}}^{\lambda}(\ell,X\_{\ell})\right)d\ell+\int\_{t}^{s}(D\_{x}V\_{I\_{\ell}}^{\lambda}(\ell,X\_{\ell}))^{\top}\sigma(\ell,X\_{\ell},I\_{\ell})dW\_{\ell} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫ts∑j≠Iℓ(πℓi​j​(Vjλ​(ℓ,Xℓ)−VIℓλ​(ℓ,Xℓ)))​d​ℓ.\displaystyle\quad+\int\_{t}^{s}\sum\_{j\neq I\_{\ell}}\left(\pi\_{\ell}^{ij}(V^{\lambda}\_{j}(\ell,X\_{\ell})-V^{\lambda}\_{I\_{\ell}}(\ell,X\_{\ell}))\right)d\ell. |  | (3.16) |

Taking the expectation on both sides of Eq. ([3](https://arxiv.org/html/2512.04697v1#S3.Ex7 "3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), it follows from ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Viλ​(t,x)≥𝔼t,x,i​[∫tsf​(ℓ,Xℓ,Iℓ)​𝑑s−∑k=1∞gκk−1​κk​𝟏{τk≤s}+λ​∫tsR​(𝝅ℓ,Iℓ)​𝑑s+VIsλ​(s,Xs)]\displaystyle V\_{i}^{\lambda}(t,x)\geq\mathbb{E}\_{t,x,i}\bigg[\int^{s}\_{t}f(\ell,X\_{\ell},I\_{\ell})ds-\sum\_{k=1}^{\infty}g\_{\kappa\_{k-1}\kappa\_{k}}{\bf 1}\_{\{\tau\_{k}\leq s\}}+\lambda\int^{s}\_{t}R({\bm{\pi}}\_{\ell},I\_{\ell})ds+V\_{I\_{s}}^{\lambda}(s,X\_{s})\bigg] |  | (3.17) |

Letting s→Ts\to T in ([3.17](https://arxiv.org/html/2512.04697v1#S3.E17 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we get from Viλ=h​(i,t,x)V\_{i}^{\lambda}=h(i,t,x) and the dominated convergence theorem that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Viλ​(t,x)≥𝔼t,x,i​[∫tTf​(ℓ,Xℓ,Iℓ)​𝑑s−∑k=1∞gκk−1​κk​𝟏{τk≤T}+λ​∫tTR​(𝝅ℓ,Iℓ)​𝑑s+h​(XT)].\displaystyle V\_{i}^{\lambda}(t,x)\geq\mathbb{E}\_{t,x,i}\bigg[\int^{T}\_{t}f(\ell,X\_{\ell},I\_{\ell})ds-\sum\_{k=1}^{\infty}g\_{\kappa\_{k-1}\kappa\_{k}}{\bf 1}\_{\{\tau\_{k}\leq T\}}+\lambda\int^{T}\_{t}R({\bm{\pi}}\_{\ell},I\_{\ell})ds+h(X\_{T})\bigg]. |  | (3.18) |

The inequality ([3.18](https://arxiv.org/html/2512.04697v1#S3.E18 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) holds for any 𝝅∈𝕌t{\bm{\pi}}\in\mathbb{U}\_{t} and becomes an equality when 𝝅=𝝅∗{\bm{\pi}}={\bm{\pi}^{\*}}. Furthermore, Theorem 2.6 in nguyen2025hybrid guarantees the existence and uniqueness of the strong solution (X∗,I∗)(X^{\*},I^{\*}) to the SDE ([3.1](https://arxiv.org/html/2512.04697v1#S3.E1 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Thus, we complete the proof of the theorem.
∎

## 4 Policy Iteration and Convergence

The goal of this section is to study the policy iteration using the characterization in ([3.5](https://arxiv.org/html/2512.04697v1#S3.E5 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). In particular, in the context of optimal regime switching, we aim to show the policy improvement and the convergence of policy iterations, which demonstrate that each policy update guarantees the performance enhancement and the repeated iterations will lead to the desired optimal policy when the model is known. We also examine the connection between our exploratory formulation and the classical optimal switching problem by analyzing the limit of the vanishing regularization.

We first focus on the rule of policy iteration. Given a feedback strategy 𝝅n​(t,x)=(πi​jn​(t,x))i,j∈𝕀m{\bm{\pi}}^{n}(t,x)=(\pi\_{ij}^{n}(t,x))\_{i,j\in\mathbb{I}\_{m}}, the corresponding value function (V1n,⋯,Vmn)(V^{n}\_{1},\cdots,V^{n}\_{m}) satisfies the following PDE system: for i∈𝕀mi\in\mathbb{I}\_{m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂Vin​(t,x)∂t+ℒxi​Vin​(t,x)+f​(t,x,i)+Hi​(𝝅in​(t,x),V1n​(t,x),⋯,Vmn​(t,x))=0,Vin​(T,x)=h​(x),\displaystyle\begin{cases}\displaystyle\frac{\partial V\_{i}^{n}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}V\_{i}^{n}(t,x)+f(t,x,i)+H\_{i}({\bm{\pi}}^{n}\_{i}(t,x),V\_{1}^{n}(t,x),\cdots,V\_{m}^{n}(t,x))=0,\\ \displaystyle V\_{i}^{n}(T,x)=h(x),\end{cases} |  | (4.1) |

Here, the Hamiltomian Hi​(𝝅i,𝒚):ℝm×ℝm→ℝH\_{i}({\bm{\pi}}\_{i},{\bm{y}}):\mathds{R}^{m}\times\mathds{R}^{m}\to\mathds{R} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hi​(𝝅i,𝒚)=∑j≠iπi​j​(yj−gi​j−yi)+λ​∑j≠i(πi​j−πi​j​log⁡πi​j).\displaystyle H\_{i}({\bm{\pi}}\_{i},{\bm{y}})=\sum\_{j\neq i}\pi\_{ij}(y\_{j}-g\_{ij}-y\_{i})+\lambda\sum\_{j\neq i}(\pi\_{ij}-\pi\_{ij}\log\pi\_{ij}). |  | (4.2) |

Having the value function pair (V1n,⋯,Vmn)(V^{n}\_{1},\cdots,V\_{m}^{n}), one can construct a feedback strategy 𝝅n+1{\bm{\pi}}^{n+1} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​jn+1​(t,x)=exp⁡(Vjn​(t,x)−gi​j−Vin​(t,x)λ),i,j∈𝕀m,j≠i.\displaystyle\pi\_{ij}^{n+1}(t,x)=\exp\left(\frac{V^{n}\_{j}(t,x)-g\_{ij}-V^{n}\_{i}(t,x)}{\lambda}\right),\penalty 10000\ i,j\in\mathbb{I}\_{m},j\neq i. |  | (4.3) |

We continue this iteration, generating a sequence of strategy-value function pairs. The following theorem states that each iteration improves the value function.

###### Proposition 4.1.

Let Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and [3.1](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Give any initial guess (V10,⋯,Vm0)(V^{0}\_{1},\cdots,V^{0}\_{m}) with Vi0∈C0​(𝒟¯)V^{0}\_{i}\in C^{0}(\overline{{\cal D}}) for i∈𝕀mi\in\mathbb{I}\_{m}. {(Vin,πi​jn)i,j∈𝕀m}n=1,2,…\{(V^{n}\_{i},\pi^{n}\_{ij})\_{i,j\in\mathbb{I}\_{m}}\}\_{n=1,2,\ldots} are defined iteratively according to ([4.1](https://arxiv.org/html/2512.04697v1#S4.E1 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.3](https://arxiv.org/html/2512.04697v1#S4.E3 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Then, we have that Vin≤Vin+1≤ViλV^{n}\_{i}\leq V^{n+1}\_{i}\leq V\_{i}^{\lambda} for i∈𝕀mi\in\mathbb{I}\_{m} and n=1,2,…n=1,2,\ldots.

###### Proof.

For n≥1n\geq 1, let Δin​(t,x):=Vin+1​(t,x)−Vin​(t,x)\Delta\_{i}^{n}(t,x):=V\_{i}^{n+1}(t,x)-V\_{i}^{n}(t,x), for i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}}. By using ([4.1](https://arxiv.org/html/2512.04697v1#S4.E1 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), Δin​(t,x)\Delta\_{i}^{n}(t,x) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Δin​(t,x)∂t+ℒxi​Δiλ​(t,x)+\displaystyle\frac{\partial\Delta\_{i}^{n}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}\Delta\_{i}^{\lambda}(t,x)+ | Hi​(𝝅in+1​(t,x),V1n+1​(t,x),⋯,Vmn+1​(t,x))\displaystyle H\_{i}({\bm{\pi}}^{n+1}\_{i}(t,x),V\_{1}^{n+1}(t,x),\cdots,V\_{m}^{n+1}(t,x)) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −\displaystyle- | Hi​(𝝅in​(t,x),V1n​(t,x),⋯,Vmn​(t,x))=0,for​(t,x)∈𝒟,\displaystyle H\_{i}({\bm{\pi}}^{n}\_{i}(t,x),V\_{1}^{n}(t,x),\cdots,V\_{m}^{n}(t,x))=0,\quad\text{for}\penalty 10000\ (t,x)\in{\cal D}, |  | (4.4) |

with the terminal condition Δin​(T,x)=0\Delta\_{i}^{n}(T,x)=0 for x∈ℝnx\in\mathds{R}^{n}. From ([4.3](https://arxiv.org/html/2512.04697v1#S4.E3 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we can see

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅in+1​(t,x)=arg​max𝝅i​Hi​(𝝅i,V1n​(t,x),⋯,Vmn​(t,x)).\displaystyle{\bm{\pi}}\_{i}^{n+1}(t,x)=\underset{{\bm{\pi}}\_{i}}{\mathrm{arg\,max\,}}H\_{i}({\bm{\pi}}\_{i},V\_{1}^{n}(t,x),\cdots,V\_{m}^{n}(t,x)). |  | (4.5) |

It follows from ([4](https://arxiv.org/html/2512.04697v1#S4.Ex1 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.5](https://arxiv.org/html/2512.04697v1#S4.E5 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) that, for (t,x)∈𝒟(t,x)\in{\cal D},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Δin​(t,x)∂t+ℒxi​Δin​(t,x)+∑j≠iπi​jn+1​(t,x)​Δjn​(t,x)−∑j≠iπi​jn+1​(t,x)​Δin​(t,x)\displaystyle\frac{\partial\Delta\_{i}^{n}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}\Delta\_{i}^{n}(t,x)+\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)\Delta\_{j}^{n}(t,x)-\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)\Delta\_{i}^{n}(t,x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Hi​(𝝅in+1​(t,x),V1n+1​(t,x),⋯,Vmn+1​(t,x))−∑j≠iπi​jn+1​(t,x)​(Δjn​(t,x)−Δin​(t,x))\displaystyle=-H\_{i}({\bm{\pi}}\_{i}^{n+1}(t,x),V\_{1}^{n+1}(t,x),\cdots,V\_{m}^{n+1}(t,x))-\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)(\Delta\_{j}^{n}(t,x)-\Delta\_{i}^{n}(t,x)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Hi​(𝝅in​(t,x),V1n​(t,x),⋯,Vmn​(t,x))\displaystyle\quad+H\_{i}({\bm{\pi}}^{n}\_{i}(t,x),V\_{1}^{n}(t,x),\cdots,V\_{m}^{n}(t,x)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Hi​(𝝅in​(t,x),V1n​(t,x),⋯,Vmn​(t,x))−Hi​(𝝅in+1​(t,x),V1n​(t,x),⋯,Vmn​(t,x))\displaystyle=H\_{i}({\bm{\pi}}^{n}\_{i}(t,x),V\_{1}^{n}(t,x),\cdots,V\_{m}^{n}(t,x))-H\_{i}({\bm{\pi}}^{n+1}\_{i}(t,x),V\_{1}^{n}(t,x),\cdots,V\_{m}^{n}(t,x)) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤0.\displaystyle\leq 0. |  | (4.6) |

By applying Theorem 1.3 in kusano1965first, we deduce that Δin​(t,x)≥0\Delta^{n}\_{i}(t,x)\geq 0, that is, Vin+1​(t,x)≥Vin​(t,x)V\_{i}^{n+1}(t,x)\geq V\_{i}^{n}(t,x), for all i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}}.

On the other hand, for n≥1n\geq 1, let Δ~in​(t,x):=Viλ​(t,x)−Vin​(t,x)\tilde{\Delta}\_{i}^{n}(t,x):=V\_{i}^{\lambda}(t,x)-V\_{i}^{n}(t,x), for i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}}. In a similar fashion, it can be shown that, for (t,x)∈𝒟(t,x)\in{\cal D},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Δ~in​(t,x)∂t+ℒxi​Δ~in​(t,x)+∑j≠iπi​jn+1​(t,x)​Δ~jn​(t,x)−∑j≠iπi​jn+1​(t,x)​Δ~in​(t,x)\displaystyle\frac{\partial\tilde{\Delta}\_{i}^{n}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}\tilde{\Delta}\_{i}^{n}(t,x)+\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)\tilde{\Delta}\_{j}^{n}(t,x)-\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)\tilde{\Delta}\_{i}^{n}(t,x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Hi​(𝝅in​(t,x),V1λ​(t,x),⋯,Vmλ​(t,x))−Hi​(𝝅i∗​(t,x),V1λ​(t,x),⋯,Vmλ​(t,x))\displaystyle=H\_{i}({\bm{\pi}}^{n}\_{i}(t,x),V\_{1}^{\lambda}(t,x),\cdots,V\_{m}^{\lambda}(t,x))-H\_{i}({\bm{\pi}}^{\*}\_{i}(t,x),V\_{1}^{\lambda}(t,x),\cdots,V\_{m}^{\lambda}(t,x)) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤0,\displaystyle\leq 0, |  | (4.7) |

and Δ~in​(T,x)=0\tilde{\Delta}\_{i}^{n}(T,x)=0 for x∈ℝnx\in\mathds{R}^{n}. By applying Theorem 1.3 in kusano1965first again, Δ~in​(t,x)≥0\tilde{\Delta}\_{i}^{n}(t,x)\geq 0, i.e., Viλ​(t,x)≥Vin​(t,x)V\_{i}^{\lambda}(t,x)\geq V\_{i}^{n}(t,x), for all i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}}, which then completes the proof.
∎

The following theorem, as the first main result of this paper, establishes a fundamental convergence guarantee for our policy iteration method, demonstrating that the sequence of value functions (V1n,⋯,Vmn)(V\_{1}^{n},\cdots,V\_{m}^{n}) generated through successive iterations converges uniformly to the optimal value functions (V1λ​⋯,Vmλ)(V\_{1}^{\lambda}\cdots,V^{\lambda}\_{m}) of our exploratory optimal switching problem. Moreover, we can obtain the explicit convergence rate for the policy iteration.

###### Theorem 4.2.

Let Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and [3.1](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Give any initial guess (V10,⋯,Vm0)(V^{0}\_{1},\cdots,V^{0}\_{m}) with Vi0∈C0​(𝒟¯)V^{0}\_{i}\in C^{0}(\overline{{\cal D}}) for i∈𝕀mi\in\mathbb{I}\_{m}. {(Vin,πi​jn)i,j∈𝕀m}n=1,2,…\{(V^{n}\_{i},\pi^{n}\_{ij})\_{i,j\in\mathbb{I}\_{m}}\}\_{n=1,2,\ldots} are defined iteratively according to ([4.1](https://arxiv.org/html/2512.04697v1#S4.E1 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.3](https://arxiv.org/html/2512.04697v1#S4.E3 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Then, we have that, for all n≥1n\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supi∈𝕀msup(t,x)∈𝒟¯|Vin​(t,x)−Viλ​(t,x)|≤C1​C2nn!,\displaystyle\sup\_{i\in\mathbb{I}\_{m}}\sup\_{(t,x)\in\overline{{\cal D}}}|V\_{i}^{n}(t,x)-V\_{i}^{\lambda}(t,x)|\leq C\_{1}\frac{C\_{2}^{n}}{n!}, |  | (4.8) |

where C1,C2>0C\_{1},C\_{2}>0 are constants independent of nn.

###### Proof.

For n≥0n\geq 0, let us introduce the function Fn:[0,T]→ℝ+F^{n}:[0,T]\to\mathds{R}\_{+} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fn​(t):=supi∈𝕀msupx∈ℝn|Vin​(t,x)−Viλ​(t,x)|.\displaystyle F^{n}(t):=\sup\_{i\in\mathbb{I}\_{m}}\sup\_{x\in\mathds{R}^{n}}|V\_{i}^{n}(t,x)-V\_{i}^{\lambda}(t,x)|. |  | (4.9) |

By the proof of Lemma [3.2](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Viλ​(t,x)|≤K​(T−t)+Kf,h≤K​T+Kf,h,∀(i,t,x)∈𝕀m×𝒟¯,\displaystyle|V\_{i}^{\lambda}(t,x)|\leq K(T-t)+K\_{f,h}\leq KT+K\_{f,h},\quad\forall(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}}, |  | (4.10) |

where the constant KK is given by ([3.8](https://arxiv.org/html/2512.04697v1#S3.E8 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). This implies the boundedness of Viλ​(t,x)V\_{i}^{\lambda}(t,x), which in turn implies that the policy 𝝅∗{\bm{\pi}}^{\*} from ([3.5](https://arxiv.org/html/2512.04697v1#S3.E5 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) is bounded. Similarly, by using Theorem [4.1](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and ([4.3](https://arxiv.org/html/2512.04697v1#S4.E3 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we can deduce that the sequence of functions Vin​(t,x)V^{n}\_{i}(t,x) and the corresponding policies 𝝅n​(t,x){\bm{\pi}}^{n}(t,x) are uniformly bounded for n≥1n\geq 1. Then, it follows from ([3.5](https://arxiv.org/html/2512.04697v1#S3.E5 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), ([4.2](https://arxiv.org/html/2512.04697v1#S4.E2 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.3](https://arxiv.org/html/2512.04697v1#S4.E3 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |Hi​(𝝅in+1,V1λ,⋯,Vmλ)−Hi​(𝝅i∗,V1λ,⋯,Vmλ)|\displaystyle\left|H\_{i}({\bm{\pi}}\_{i}^{n+1},V\_{1}^{\lambda},\cdots,V\_{m}^{\lambda})-H\_{i}({\bm{\pi}}\_{i}^{\*},V\_{1}^{\lambda},\cdots,V\_{m}^{\lambda})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|∑j≠iπi​jn​(Vjλ−gi​j−Viλ)+λ​∑j≠i(πi​jn−πi​jn​log⁡πi​jn)|\displaystyle\leq\left|\sum\_{j\neq i}\pi\_{ij}^{n}(V\_{j}^{\lambda}-g\_{ij}-V\_{i}^{\lambda})+\lambda\sum\_{j\neq i}(\pi\_{ij}^{n}-\pi\_{ij}^{n}\log\pi\_{ij}^{n})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|(∑j≠iπi​j∗​(Vjλ−gi​j−Viλ)+λ​∑j≠i(πi​j∗−πi​j∗​log⁡πi​j∗))|\displaystyle\quad+\left|\left(\sum\_{j\neq i}\pi\_{ij}^{\*}(V\_{j}^{\lambda}-g\_{ij}-V\_{i}^{\lambda})+\lambda\sum\_{j\neq i}(\pi\_{ij}^{\*}-\pi\_{ij}^{\*}\log\pi\_{ij}^{\*})\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑j≠iπi​jn​|Vjλ−Vjn|+|Viλ−Vin|​∑j≠iπi​jn\displaystyle\leq\sum\_{j\neq i}\pi^{n}\_{ij}|V\_{j}^{\lambda}-V\_{j}^{n}|+|V\_{i}^{\lambda}-V\_{i}^{n}|\sum\_{j\neq i}\pi^{n}\_{ij} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​∑j≠i|exp⁡(Vjn−gi​j−Vinλ)−exp⁡(Vjλ−gi​j−Viλλ)|\displaystyle\quad+\lambda\sum\_{j\neq i}\left|\exp\left(\frac{V^{n}\_{j}-g\_{ij}-V^{n}\_{i}}{\lambda}\right)-\exp\left(\frac{V\_{j}^{\lambda}-g\_{ij}-V\_{i}^{\lambda}}{\lambda}\right)\right| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤C∗​Fn​(t),\displaystyle\leq C^{\*}F^{n}(t), |  | (4.11) |

where C∗>0C^{\*}>0 is a constant independent of nn. For n≥0n\geq 0, we define the function win:𝒟¯→ℝw\_{i}^{n}:\overline{{\cal D}}\to\mathds{R} for i∈𝕀mi\in\mathbb{I}\_{m} as

|  |  |  |
| --- | --- | --- |
|  | win​(t,x):=Viλ​(t,x)−Vin+1​(t,x)−C∗​∫tTFn​(s)​𝑑s,(t,x)∈𝒟¯.\displaystyle w\_{i}^{n}(t,x):=V\_{i}^{\lambda}(t,x)-V\_{i}^{n+1}(t,x)-C^{\*}\int\_{t}^{T}F^{n}(s)ds,\quad(t,x)\in\overline{{\cal D}}. |  |

By using ([4](https://arxiv.org/html/2512.04697v1#S4.Ex8 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), it holds that for any (t,x)∈𝒟(t,x)\in{\cal D},

|  |  |  |
| --- | --- | --- |
|  | ∂win​(t,x)∂t+ℒxi​win​(t,x)+∑j≠iπi​jn+1​(t,x)​wjn​(t,x)−∑j≠iπi​jn+1​(t,x)​win​(t,x)\displaystyle\frac{\partial w\_{i}^{n}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}w\_{i}^{n}(t,x)+\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)w\_{j}^{n}(t,x)-\sum\_{j\neq i}\pi\_{ij}^{n+1}(t,x)w\_{i}^{n}(t,x) |  |
|  |  |  |
| --- | --- | --- |
|  | =Hi​(𝝅in+1​(t,x),V1λ​(t,x),⋯,Vmλ​(t,x))−Hi​(𝝅i∗​(t,x),V1λ​(t,x),⋯,Vmλ​(t,x))+C∗​Fn​(t)≥0,\displaystyle=H\_{i}({\bm{\pi}}\_{i}^{n+1}(t,x),V\_{1}^{\lambda}(t,x),\cdots,V\_{m}^{\lambda}(t,x))-H\_{i}({\bm{\pi}}^{\*}\_{i}(t,x),V\_{1}^{\lambda}(t,x),\cdots,V\_{m}^{\lambda}(t,x))+C^{\*}F^{n}(t)\geq 0, |  |

and win​(T,x)≥0w\_{i}^{n}(T,x)\geq 0 for x∈ℝnx\in\mathds{R}^{n}. By virtue of Theorem 1.3 in kusano1965first, we deduce win​(t,x)≥0w^{n}\_{i}(t,x)\geq 0. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Viλ​(t,x)−Vin+1​(t,x)≤C∗​∫tTFn​(s)​𝑑s,∀(i,t,x)∈𝕀m×𝒟¯.\displaystyle V\_{i}^{\lambda}(t,x)-V\_{i}^{n+1}(t,x)\leq C^{\*}\int\_{t}^{T}F^{n}(s)ds,\quad\forall(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}}. |  | (4.12) |

This yields the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fn+1​(t)≤C∗​∫tTFn​(s)​𝑑s,∀t∈[0,T],\displaystyle F^{n+1}(t)\leq C^{\*}\int\_{t}^{T}F^{n}(s)ds,\quad\forall t\in[0,T], |  | (4.13) |

from which we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fn​(t)≤(C∗)n​Tnn!​F1​(t),∀t∈[0,T].\displaystyle F^{n}(t)\leq\frac{(C^{\*})^{n}T^{n}}{n!}F^{1}(t),\quad\forall t\in[0,T]. |  | (4.14) |

Because F1​(t)F^{1}(t) is bounded, let C1=C∗​TC\_{1}=C^{\*}T and C2=supt∈[0,T]F1​(t)C\_{2}=\sup\_{t\in[0,T]}F^{1}(t). Then we obtain that desired result.
∎

To establish a connection between our exploratory formulation and the classical optimal switching problem, we next rigorously analyze the convergence result of the exploratory solution as the temperature parameter λ\lambda approaches zero. Unlike the existing results in tang2022exploratory for regular control problem that focus on a single PDE problem, the nature of problem with multiple regime states calls for some distinct analysis to investigate the system of PDEs in our setting.
In particular, we employ some stability analysis of viscosity solutions to the PDE system to examine the limit of vanishing entropy regularization. The mathematical goal is to show that the solution of the system of PDE will converge to the solution of the system of variational inequalities as λ→0\lambda\rightarrow 0.

Let us introduce the upper and lower weak limits of functions (V1λ,⋯,Vmλ)(V\_{1}^{\lambda},\cdots,V\_{m}^{\lambda}) defined as follows: for i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯i​(t,x):={lim supλ→0(s,y)→(t,x),(s,y)∈𝒟Viλ​(s,y),(t,x)∈𝒟,h​(x),t=T,x∈ℝn,\displaystyle\overline{V}\_{i}(t,x):=\begin{cases}\displaystyle\limsup\_{\lambda\to 0\atop(s,y)\to(t,x),(s,y)\in{\cal D}}V\_{i}^{\lambda}(s,y),&(t,x)\in{\cal D},\\[10.00002pt] \displaystyle\qquad h(x),&t=T,\penalty 10000\ x\in\mathds{R}^{n},\end{cases} |  | (4.15) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯i​(t,x):={lim infλ→0,(s,y)→(t,x),(s,y)∈𝒟Viλ​(s,y),(t,x)∈𝒟,h​(x),t=T,x∈ℝn.\displaystyle\underline{V}\_{i}(t,x):=\begin{cases}\displaystyle\liminf\_{\lambda\to 0,\atop(s,y)\to(t,x),(s,y)\in{\cal D}}V\_{i}^{\lambda}(s,y),&(t,x)\in{\cal D},\\[10.00002pt] \displaystyle\qquad h(x),&t=T,\penalty 10000\ x\in\mathds{R}^{n}.\end{cases} |  | (4.16) |

The next lemma plays a crucial role in establishing the convergence of the value functions (V1λ,⋯,Vmλ)(V\_{1}^{\lambda},\cdots,V\_{m}^{\lambda}) as the temperature parameter λ\lambda tends to zero. By defining the upper and lower weak limits, we capture the limiting behavior of these functions. The result asserts that these limits are bounded and satisfy the viscosity solution properties for the system of HJB equations ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Specifically, the upper weak limits form a viscosity subsolution, and the lower weak limits form a viscosity supersolution.

###### Lemma 4.3.

Let Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), and [3.1](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Consider the upper and lower weak limits of the functions (V1λ,⋯,Vmλ)(V\_{1}^{\lambda},\cdots,V\_{m}^{\lambda}), defined by ([4.15](https://arxiv.org/html/2512.04697v1#S4.E15 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.16](https://arxiv.org/html/2512.04697v1#S4.E16 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), respectively. Then the tuple of upper weak limits (V¯1,⋯,V¯m)(\overline{V}\_{1},\cdots,\overline{V}\_{m}) is a bounded viscosity subsolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), while the tuple of lower weak limits (V¯1,⋯,V¯m)(\underline{V}\_{1},\cdots,\underline{V}\_{m}) is a bounded viscosity supersolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")).

###### Proof.

It follows from ([3.13](https://arxiv.org/html/2512.04697v1#S3.E13 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and Assumption [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")-(ii) that

|  |  |  |
| --- | --- | --- |
|  | |Viλ​(t,x)|≤Kf,h​(1+T)+λ​supi∈𝕀m(∑j≠iexp⁡(−gi​jλ))​T≤Kf,h​(1+T)+λ​(m−1)​T\displaystyle|V\_{i}^{\lambda}(t,x)|\leq K\_{f,h}(1+T)+\lambda\sup\_{i\in\mathbb{I}\_{m}}\left(\sum\_{j\neq i}\exp\left(-\frac{g\_{ij}}{\lambda}\right)\right)T\leq K\_{f,h}(1+T)+\lambda(m-1)T |  |

for all λ>0\lambda>0 and (i,t,x)∈𝕀m×𝒟¯(i,t,x)\in\mathbb{I}\_{m}\times\overline{{\cal D}}.
This implies that V¯i\overline{V}\_{i} and V¯i\underline{V}\_{i} for i∈𝕀mi\in\mathbb{I}\_{m} are bounded functions. Applying Lemma 1.5 in Chapter V of bardi1997optimal, V¯i\overline{V}\_{i} is upper-semicontinuous on 𝒟{\cal D} while V¯i\underline{V}\_{i} is lower-semicontinuous on 𝒟{\cal D} for every i∈𝕀mi\in\mathbb{I}\_{m}.

We next show that the tuple of upper weak limits (V¯1,⋯,V¯m)(\overline{V}\_{1},\cdots,\overline{V}\_{m}) is a viscosity subsolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) using the contradiction argument. For i∈𝕀mi\in\mathbb{I}\_{m}, let (t0,x0)∈𝒟(t\_{0},x\_{0})\in{\cal D} and the test function φi∈C1,2​(𝒟)\varphi\_{i}\in C^{1,2}({\cal D}) such that (t0,x0)(t\_{0},x\_{0}) is a local maximum of V¯i−φi\overline{V}\_{i}-\varphi\_{i}. Assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | min{\displaystyle\min\Bigg\{ | −∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i),\displaystyle-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V¯i(t0,x0)−maxj≠i(V¯j(t0,x0)−gi​j)}>0.\displaystyle\qquad\qquad\quad\overline{V}\_{i}(t\_{0},x\_{0})-\max\_{j\neq i}(\overline{V}\_{j}(t\_{0},x\_{0})-g\_{ij})\Bigg\}>0. |  | (4.17) |

That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ:=−∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i)>0,\displaystyle\delta:=-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i)>0, |  | (4.18) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ε:=V¯i​(t0,x0)−maxj≠i⁡(V¯j​(t0,x0)−gi​j)>0.\displaystyle\varepsilon:=\overline{V}\_{i}(t\_{0},x\_{0})-\max\_{j\neq i}(\overline{V}\_{j}(t\_{0},x\_{0})-g\_{ij})>0. |  | (4.19) |

In view of Lemma 1.6 in Chapter V of bardi1997optimal, there exists a sequence {(tn,xn)}n≥1\{(t\_{n},x\_{n})\}\_{n\geq 1} with (tn,xn)∈𝒟(t\_{n},x\_{n})\in{\cal D} and a sequence {λn}n≥1\{\lambda\_{n}\}\_{n\geq 1} with λn>0\lambda\_{n}>0, limn→∞λn=0\lim\_{n\to\infty}\lambda\_{n}=0 such that (tn,xn)(t\_{n},x\_{n}) is a local maximum point of Viλn−φiV^{\lambda\_{n}}\_{i}-\varphi\_{i} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞(tn,xn)=(t0,x0),limn→∞Viλn​(tn,xn)=V¯i​(t0,x0).\displaystyle\lim\_{n\to\infty}(t\_{n},x\_{n})=(t\_{0},x\_{0}),\quad\lim\_{n\to\infty}V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})=\overline{V}\_{i}(t\_{0},x\_{0}). |  | (4.20) |

Lemma [3.2](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") implies that for any λ>0\lambda>0, (V1λ,V2λ,⋯,Vmλ)(V^{\lambda}\_{1},V^{\lambda}\_{2},\cdots,V^{\lambda}\_{m}) is a classical solution to the system of of HJB equations ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), thus ViλnV^{\lambda\_{n}}\_{i} is a viscosity subsolution of the following PDE:

|  |  |  |
| --- | --- | --- |
|  | −∂Viλn​(t,x)∂t−ℒxi​Viλn​(t,x)−f​(t,x,i)−λ​∑j≠iexp⁡(Vjλn​(t,x)−gi​j−Viλn​(t,x)λ)=0.\displaystyle-\frac{\partial V^{\lambda\_{n}}\_{i}(t,x)}{\partial t}-\mathcal{L}^{i}\_{x}V^{\lambda\_{n}}\_{i}(t,x)-f(t,x,i)-\lambda\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t,x)-g\_{ij}-V^{\lambda\_{n}}\_{i}(t,x)}{\lambda}\right)=0. |  |

Consequently, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)−λn​∑j≠iexp⁡(Vjλn​(tn,xn)−gi​j−Viλn​(tn,xn)λ)≤0\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)-\lambda\_{n}\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t\_{n},x\_{n})-g\_{ij}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})}{\lambda}\right)\leq 0 |  | (4.21) |

for any n≥1n\geq 1.

From ([4.18](https://arxiv.org/html/2512.04697v1#S4.E18 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), ([4.19](https://arxiv.org/html/2512.04697v1#S4.E19 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.20](https://arxiv.org/html/2512.04697v1#S4.E20 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), it follows that there exists some n1>0n\_{1}>0 such that for all n≥n1n\geq n\_{1},

|  |  |  |
| --- | --- | --- |
|  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)≥δ2,\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)\geq\frac{\delta}{2}, |  |

and for any j∈𝕀m,j≠ij\in\mathbb{I}\_{m},j\neq i,

|  |  |  |
| --- | --- | --- |
|  | Vjλn​(tn,xn)−gi​j−Viλn​(tn,xn)≤−ε2.\displaystyle V^{\lambda\_{n}}\_{j}(t\_{n},x\_{n})-g\_{ij}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})\leq-\frac{\varepsilon}{2}. |  |

Selecting n2n\_{2} such that for all n≥n2n\geq n\_{2}, λn​exp⁡(−ε2​λn)<δ2​(m−1)\lambda\_{n}\exp(-\frac{\varepsilon}{2\lambda\_{n}})<\frac{\delta}{2(m-1)}, then for n≥max⁡{n1,n2}n\geq\max\{n\_{1},n\_{2}\}, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)−λn​∑j≠iexp⁡(Vjλn​(tn,xn)−gi​j−Viλn​(tn,xn)λ)\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)-\lambda\_{n}\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t\_{n},x\_{n})-g\_{ij}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})}{\lambda}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥−∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)−λn​∑j≠iexp⁡(−ε2​λn)\displaystyle\geq-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)-\lambda\_{n}\sum\_{j\neq i}\exp\left(-\frac{\varepsilon}{2\lambda\_{n}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥δ2−λn​(m−1)​exp⁡(−ε2​λn)>0.\displaystyle\geq\frac{\delta}{2}-\lambda\_{n}(m-1)\exp\left(-\frac{\varepsilon}{2\lambda\_{n}}\right)>0. |  | (4.22) |

The inequalities ([4.21](https://arxiv.org/html/2512.04697v1#S4.E21 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4](https://arxiv.org/html/2512.04697v1#S4.Ex21 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) are contradictory. Therefore, we conclude that the assumption ([4](https://arxiv.org/html/2512.04697v1#S4.Ex17 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) is note true, which implies that (V¯1,⋯,V¯m)(\overline{V}\_{1},\cdots,\overline{V}\_{m}) is a viscosity subsolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")).

We next show that the tuple of lower weak limits (V¯1,⋯,V¯m)(\underline{V}\_{1},\cdots,\underline{V}\_{m}) is a viscosity supersolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) by contradiction. For i∈𝕀mi\in\mathbb{I}\_{m}, let (t0,x0)∈𝒟(t\_{0},x\_{0})\in{\cal D} and the test function φi∈C1,2​(𝒟)\varphi\_{i}\in C^{1,2}({\cal D}) such that (t0,x0)(t\_{0},x\_{0}) is a local minimum of V¯i−φi\overline{V}\_{i}-\varphi\_{i}. Assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | min{\displaystyle\min\Bigg\{ | −∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i),\displaystyle-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V¯i(t0,x0)−maxj≠i(V¯j(t0,x0)−gi​j)}<0.\displaystyle\qquad\qquad\quad\underline{V}\_{i}(t\_{0},x\_{0})-\max\_{j\neq i}(\underline{V}\_{j}(t\_{0},x\_{0})-g\_{ij})\Bigg\}<0. |  | (4.23) |

Using Lemma 1.6 in Chapter V of bardi1997optimal again, there exists a sequence {(tn,xn)}n≥1\{(t\_{n},x\_{n})\}\_{n\geq 1} with (tn,xn)∈𝒟(t\_{n},x\_{n})\in{\cal D} and a sequence {λn}n≥1\{\lambda\_{n}\}\_{n\geq 1} with λn>0\lambda\_{n}>0, limn→∞λn=0\lim\_{n\to\infty}\lambda\_{n}=0 such that (tn,xn)(t\_{n},x\_{n}) is a local minimum point of Viλn−φiV^{\lambda\_{n}}\_{i}-\varphi\_{i} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞(tn,xn)=(t0,x0),limn→∞Viλn​(tn,xn)=V¯i​(t0,x0).\displaystyle\lim\_{n\to\infty}(t\_{n},x\_{n})=(t\_{0},x\_{0}),\quad\lim\_{n\to\infty}V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})=\underline{V}\_{i}(t\_{0},x\_{0}). |  | (4.24) |

By Lemma [3.2](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), for any λ>0\lambda>0, (V1λ,V2λ,⋯,Vmλ)(V^{\lambda}\_{1},V^{\lambda}\_{2},\cdots,V^{\lambda}\_{m}) is a classical solution to the system of of HJB equations ([3.4](https://arxiv.org/html/2512.04697v1#S3.E4 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), thus ViλnV^{\lambda\_{n}}\_{i} is a viscosity supersolution of the following PDE:

|  |  |  |
| --- | --- | --- |
|  | −∂Viλn​(t,x)∂t−ℒxi​Viλn​(t,x)−f​(t,x,i)−λ​∑j≠iexp⁡(Vjλn​(t,x)−gi​j−Viλn​(t,x)λ)=0.\displaystyle-\frac{\partial V^{\lambda\_{n}}\_{i}(t,x)}{\partial t}-\mathcal{L}^{i}\_{x}V^{\lambda\_{n}}\_{i}(t,x)-f(t,x,i)-\lambda\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t,x)-g\_{ij}-V^{\lambda\_{n}}\_{i}(t,x)}{\lambda}\right)=0. |  |

Therefore we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)−λn​∑j≠iexp⁡(Vjλn​(tn,xn)−gi​j−Viλn​(tn,xn)λ)≥0\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)-\lambda\_{n}\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t\_{n},x\_{n})-g\_{ij}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})}{\lambda}\right)\geq 0 |  | (4.25) |

for any n≥1n\geq 1. We consider two cases for the inequality ([4](https://arxiv.org/html/2512.04697v1#S4.Ex23 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")).

Case 1. Assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i)<0.\displaystyle-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i)<0. |  | (4.26) |

By ([4.25](https://arxiv.org/html/2512.04697v1#S4.E25 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we have

|  |  |  |
| --- | --- | --- |
|  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)≥λn​∑j≠iexp⁡(Vjλn​(tn,xn)−gi​j−Viλn​(tn,xn)λ)≥0,\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)\geq\lambda\_{n}\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t\_{n},x\_{n})-g\_{ij}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})}{\lambda}\right)\geq 0, |  |

which yields

|  |  |  |
| --- | --- | --- |
|  | −∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i)\displaystyle-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i) |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞(−∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i))≥0.\displaystyle=\lim\_{n\to\infty}\left(-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)\right)\geq 0. |  |

Thus, we obtain a contradiction.

Case 2. Assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ:=−∂φi​(t0,x0)∂t−ℒxi​φi​(t0,x0)−f​(t0,x0,i)≥0,\displaystyle\delta:=-\frac{\partial\varphi\_{i}(t\_{0},x\_{0})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{0},x\_{0})-f(t\_{0},x\_{0},i)\geq 0, |  | (4.27) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε:=−(V¯i​(t0,x0)−maxj≠i⁡(V¯j​(t0,x0)−gi​j))=V¯k​(t0,x0)−gi​k−V¯i​(t0,x0)>0.\displaystyle\varepsilon:=-(\underline{V}\_{i}(t\_{0},x\_{0})-\max\_{j\neq i}(\underline{V}\_{j}(t\_{0},x\_{0})-g\_{ij}))=\underline{V}\_{k}(t\_{0},x\_{0})-g\_{ik}-\underline{V}\_{i}(t\_{0},x\_{0})>0. |  | (4.28) |

By ([4.24](https://arxiv.org/html/2512.04697v1#S4.E24 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), ([4.27](https://arxiv.org/html/2512.04697v1#S4.E27 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4.28](https://arxiv.org/html/2512.04697v1#S4.E28 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), there exists some n1>0n\_{1}>0 such that for all n≥n1n\geq n\_{1},

|  |  |  |
| --- | --- | --- |
|  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)≤3​δ2,\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)\leq\frac{3\delta}{2}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Vkλn​(tn,xn)−gi​k−Viλn​(tn,xn)≥ε2.\displaystyle V^{\lambda\_{n}}\_{k}(t\_{n},x\_{n})-g\_{ik}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})\geq\frac{\varepsilon}{2}. |  |

Selecting n2n\_{2} such that for all n≥n2n\geq n\_{2}, λn​exp⁡(ε2​λn)>3​δ2\lambda\_{n}\exp(\frac{\varepsilon}{2\lambda\_{n}})>\frac{3\delta}{2}, then for n≥max⁡{n1,n2}n\geq\max\{n\_{1},n\_{2}\}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)−λn​∑j≠iexp⁡(Vjλn​(tn,xn)−gi​j−Viλn​(tn,xn)λ)\displaystyle-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)-\lambda\_{n}\sum\_{j\neq i}\exp\left(\frac{V^{\lambda\_{n}}\_{j}(t\_{n},x\_{n})-g\_{ij}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})}{\lambda}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−∂φi​(tn,xn)∂t−ℒxi​φi​(tn,xn)−f​(tn,xn,i)−λn​exp⁡(Vkλn​(tn,xn)−gi​k−Viλn​(tn,xn)λ)\displaystyle\leq-\frac{\partial\varphi\_{i}(t\_{n},x\_{n})}{\partial t}-\mathcal{L}^{i}\_{x}\varphi\_{i}(t\_{n},x\_{n})-f(t\_{n},x\_{n},i)-\lambda\_{n}\exp\left(\frac{V^{\lambda\_{n}}\_{k}(t\_{n},x\_{n})-g\_{ik}-V^{\lambda\_{n}}\_{i}(t\_{n},x\_{n})}{\lambda}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤3​δ2−λn​exp⁡(ε2​λn)<0.\displaystyle\leq\frac{3\delta}{2}-\lambda\_{n}\exp\left(\frac{\varepsilon}{2\lambda\_{n}}\right)<0. |  | (4.29) |

The inequalities ([4.25](https://arxiv.org/html/2512.04697v1#S4.E25 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([4](https://arxiv.org/html/2512.04697v1#S4.Ex30 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) are contradictory.

Combining the arguments in two cases above, we conclude that assertion ([4](https://arxiv.org/html/2512.04697v1#S4.Ex23 "4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) does not hold. This implies that (V¯1,⋯,V¯m)(\overline{V}\_{1},\cdots,\overline{V}\_{m}) is a viscosity supersolution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), which completes the proof.
∎

As the second main result of this paper, the next theorem
shows the convergence result towards the classical optimal switching problem as the entropy regularization vanishes.

###### Theorem 4.4.

Let Assumptions [2.1](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), [2.2](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem2 "Assumption 2.2. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and [3.1](https://arxiv.org/html/2512.04697v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Consider the value functions (V1,⋯,Vm)(V\_{1},\cdots,V\_{m}) of the classical optimal switching problem defined by ([2.6](https://arxiv.org/html/2512.04697v1#S2.E6 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), and the value functions (V1λ,⋯,Vmλ)(V\_{1}^{\lambda},\cdots,V\_{m}^{\lambda}) of the exploratory optimal switching problem defined by ([3.3](https://arxiv.org/html/2512.04697v1#S3.E3 "In 3 Exploratory Formulation under Entropy Regularization ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Then for any i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | limλ→0Viλ​(t,x)=Vi​(t,x).\displaystyle\lim\_{\lambda\to 0}V\_{i}^{\lambda}(t,x)=V\_{i}(t,x). |  | (4.30) |

###### Proof.

By using Lemma [4.3](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and Lemma [2.3](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem3 "Lemma 2.3 (Comparison Principle). ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), we have

|  |  |  |
| --- | --- | --- |
|  | V¯i​(t,x)≤V¯i​(t,x),∀i∈𝕀m,(t,x)∈𝒟¯.\displaystyle\overline{V}\_{i}(t,x)\leq\underline{V}\_{i}(t,x),\quad\forall i\in\mathbb{I}\_{m},(t,x)\in\overline{{\cal D}}. |  |

On the other hand, it follows from the definition of upper and lower weak limits that V¯i​(t,x)≥V¯i​(t,x)\overline{V}\_{i}(t,x)\geq\underline{V}\_{i}(t,x), for any i∈𝕀mi\in\mathbb{I}\_{m} and (t,x)∈𝒟¯(t,x)\in\overline{{\cal D}}. Thus, V¯i​(t,x)=V¯i​(t,x)\overline{V}\_{i}(t,x)=\underline{V}\_{i}(t,x), then denotes by

|  |  |  |
| --- | --- | --- |
|  | Vi∗​(t,x)=V¯i​(t,x)=V¯i​(t,x)for​i∈𝕀m,(t,x)∈𝒟¯.\displaystyle V^{\*}\_{i}(t,x)=\overline{V}\_{i}(t,x)=\underline{V}\_{i}(t,x)\quad\text{for}\penalty 10000\ i\in\mathbb{I}\_{m},(t,x)\in\overline{{\cal D}}. |  |

It follows from ([4.15](https://arxiv.org/html/2512.04697v1#S4.E15 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), ([4.16](https://arxiv.org/html/2512.04697v1#S4.E16 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and Lemma [4.3](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") that (V1∗,⋯,Vm∗)(V\_{1}^{\*},\cdots,V\_{m}^{\*}) is a bounded viscosity solution of system ([2.7](https://arxiv.org/html/2512.04697v1#S2.E7 "In 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) satisfying Vi∗​(t,x)=limλ→0Viλ​(t,x)V^{\*}\_{i}(t,x)=\lim\_{\lambda\to 0}V\_{i}^{\lambda}(t,x). We deduce from Theorem [2.4](https://arxiv.org/html/2512.04697v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Classical Optimal Switching Problem ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi​(t,x)=Vi∗​(t,x)=limλ→0Viλ​(t,x).\displaystyle V\_{i}(t,x)=V^{\*}\_{i}(t,x)=\lim\_{\lambda\to 0}V\_{i}^{\lambda}(t,x). |  | (4.31) |

Thus, we complete the proof of the theorem.
∎

Theorem [4.4](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") justifies the use of the exploratory formulation as a well-founded mathematical relaxation: as the exploration effect diminishes (as the temperature parameter λ→0\lambda\to 0), the value function of the exploratory formulation indeed converges towards the value function of the classical optimal switching problem. Mathematically speaking, it is interesting to observe that the solution to the system of PDEs will converge to the solution of system of variational inequalities. Therefore, our exploratory formulation can also be regarded as a penalization approach to study a system of variational inequalities, under which we only need to handle the existence and regularity of solution to a system of PDEs.

## 5 Reinforcement Learning Algorithm

In this section, we design a RL algorithm to solve the exploratory optimal switching problem when the model is unknown. The core of our approach lies in a key reformulation: we have transformed the original optimal switching problem into a standard optimal control problem where we control the generator of the finite-state Markov chain that characterizes the switching regimes. The primary distinction from classical problems is that the agent now actively controls the transition rates between regimes, adding a continuous layer of decision-making on top of the discrete switching choices.

Our choice of the randomization and the exploratory form leads to an explicit characterization of the optimal policy that depends on the value functions, without involving their derivatives. Leveraging this solution structure, we adopt the policy evaluation (PE) method based on the martingale characterization method similar to jia2022policy, which consider two alternative methods based on a martingale characterization: minimizing a martingale loss function, which provides the best mean-square approximation of the true value function, and solving a system of martingale orthogonality condition with test functions. In what follows, we design the PE algorithm by the martingale orthogonality condition and the established policy improvement result in Proposition [4.1](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes").

Recall that given a feedback strategy 𝝅​(t,x)=(πi​j​(t,x))i,j∈𝕀m{\bm{\pi}}(t,x)=(\pi\_{ij}(t,x))\_{i,j\in\mathbb{I}\_{m}}, then the corresponding value function (v1𝝅,⋯,vm𝝅)(v\_{1}^{{\bm{\pi}}},\cdots,v\_{m}^{{\bm{\pi}}}) satisfies the PDE system that for i∈𝕀mi\in\mathbb{I}\_{m},

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂vi𝝅​(t,x)∂t+ℒxi​vi𝝅​(t,x)+f​(t,x,i)+Hi​(𝝅i​(t,x),v1𝝅​(t,x),⋯,vm𝝅​(t,x))=0,vi𝝅​(T,x)=h​(x),\displaystyle\begin{cases}\displaystyle\frac{\partial v\_{i}^{{\bm{\pi}}}(t,x)}{\partial t}+\mathcal{L}^{i}\_{x}v\_{i}^{{\bm{\pi}}}(t,x)+f(t,x,i)+H\_{i}({\bm{\pi}}\_{i}(t,x),v\_{1}^{{\bm{\pi}}}(t,x),\cdots,v^{{\bm{\pi}}}\_{m}(t,x))=0,\\ \displaystyle v^{{\bm{\pi}}}\_{i}(T,x)=h(x),\end{cases} |  | (5.1) |

where the the Hamiltomian HiH\_{i} is given by ([4.2](https://arxiv.org/html/2512.04697v1#S4.E2 "In 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). For simplicity, we omit the superscript 𝝅{{\bm{\pi}}} and denote the value function as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,i)=vi𝝅​(t,x),for ​i∈𝕀m,(t,x)∈𝒟¯,\displaystyle v(t,x,i)=v^{{\bm{\pi}}}\_{i}(t,x),\quad\text{for }i\in\mathbb{I}\_{m},\penalty 10000\ (t,x)\in\overline{{\cal D}}, |  | (5.2) |

and denote by I=(It)​t≥0I=(I\_{t}){t\geq 0} a continuous-time finite-state Markov chain with generator 𝝅=(πi​j)i,j∈𝕀m{\bm{\pi}}=(\pi^{ij})\_{i,j\in\mathbb{I}\_{m}}. Let us introduce the process M=(Mt)t∈[0,T]M=(M\_{t})\_{t\in[0,T]} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mt:=v​(t,Xt,It)+∫0t(f​(s,Xs,Is)+λ​R​(𝝅s,Is))​𝑑s−∑k=1∞gκk−1​κk​𝟏{τk≤t},t∈[0,T].\displaystyle M\_{t}:=v(t,X\_{t},I\_{t})+\int\_{0}^{t}\left(f(s,X\_{s},I\_{s})+\lambda R({\bm{\pi}}\_{s},I\_{s})\right)ds-\sum\_{k=1}^{\infty}g\_{\kappa\_{k-1}\kappa\_{k}}{\bf 1}\_{\{\tau\_{k}\leq t\}},\quad t\in[0,T]. |  | (5.3) |

The next lemma gives the martingale characterization that lays the foundation for the loss function and the policy evaluation RL algorithm.

###### Lemma 5.1.

Let 𝛑​(t,x)=(πi​j​(t,x))i,j∈𝕀m{\bm{\pi}}(t,x)=(\pi\_{ij}(t,x))\_{i,j\in\mathbb{I}\_{m}} be a feedback strategy and v​(t,x,i)v(t,x,i) be the corresponding value function given by ([5.2](https://arxiv.org/html/2512.04697v1#S5.E2 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). Then the process M=(Mt)t∈[0,T]M=(M\_{t})\_{t\in[0,T]} given by ([5.3](https://arxiv.org/html/2512.04697v1#S5.E3 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) is a squar-intergrable martingale.

###### Proof.

Using Itô’s rule to v​(s,Xs,Is)v(s,X\_{s},I\_{s}) from t′t^{\prime} to tt, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,Xt,It)\displaystyle v(t,X\_{t},I\_{t}) | =v​(t′,Xt′,It′)+∫t′t(Dx​v​(s,Xs,Is))⊤​σ​(s,Xs,Is)​𝑑Ws\displaystyle=v(t^{\prime},X\_{t^{\prime}},I\_{t^{\prime}})+\int\_{t^{\prime}}^{t}(D\_{x}v(s,X\_{s},I\_{s}))^{\top}\sigma(s,X\_{s},I\_{s})dW\_{s} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫t′t(∂v​(s,Xs,Is)∂t+ℒxIs​v​(s,Xs,Is)+∑j≠Is(πsIs​j​(v​(s,Xs,j)−v​(s,Xs,Is))))​𝑑s.\displaystyle\qquad+\int\_{t^{\prime}}^{t}\left(\frac{\partial v(s,X\_{s},I\_{s})}{\partial t}+\mathcal{L}^{I\_{s}}\_{x}v(s,X\_{s},I\_{s})+\sum\_{j\neq I\_{s}}\left(\pi\_{s}^{I\_{s}j}(v(s,X\_{s},j)-v(s,X\_{s},I\_{s}))\right)\right)ds. |  | (5.4) |

It follows from ([5.1](https://arxiv.org/html/2512.04697v1#S5.E1 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), ([5](https://arxiv.org/html/2512.04697v1#S5.Ex1 "5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) and ([5.3](https://arxiv.org/html/2512.04697v1#S5.E3 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Mt|ℱt′]\displaystyle\mathbb{E}[M\_{t}|\mathcal{F}\_{t^{\prime}}] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​[v​(t,Xt,It)+∫0t(f​(s,Xs,Is)+λ​R​(𝝅s,Is))​𝑑s−∑k=1∞gκk−1​κk​𝟏{τk≤t}|ℱt′]\displaystyle=\mathbb{E}\left[v(t,X\_{t},I\_{t})+\int\_{0}^{t}\left(f(s,X\_{s},I\_{s})+\lambda R({\bm{\pi}}\_{s},I\_{s})\right)ds-\sum\_{k=1}^{\infty}g\_{\kappa\_{k-1}\kappa\_{k}}{\bf 1}\_{\{\tau\_{k}\leq t\}}\Big|\mathcal{F}\_{t^{\prime}}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =Mt′+𝔼​[v​(t,Xt,It)−v​(t′,Xt′,It′)+∫t′t(f​(s,Xs,Is)+λ​R​(𝝅s,Is))​𝑑s−∫t′t∑j≠IsgIs​j​πsIs​j​d​s|ℱt′]\displaystyle=M\_{t^{\prime}}+\mathbb{E}\left[v(t,X\_{t},I\_{t})-v(t^{\prime},X\_{t^{\prime}},I\_{t^{\prime}})+\int\_{t^{\prime}}^{t}\left(f(s,X\_{s},I\_{s})+\lambda R({\bm{\pi}}\_{s},I\_{s})\right)ds-\int\_{t^{\prime}}^{t}\sum\_{j\neq I\_{s}}g\_{I\_{s}j}\pi\_{s}^{I\_{s}j}ds\Big|\mathcal{F}\_{t^{\prime}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =Mt′+𝔼​[∫t′t∫t′t(Dx​v​(s,Xs,Is))⊤​σ​(s,Xs,Is)​𝑑Ws|ℱt′]=Mt′.\displaystyle=M\_{t^{\prime}}+\mathbb{E}\left[\int\_{t^{\prime}}^{t}\int\_{t^{\prime}}^{t}(D\_{x}v(s,X\_{s},I\_{s}))^{\top}\sigma(s,X\_{s},I\_{s})dW\_{s}\Big|\mathcal{F}\_{t^{\prime}}\right]=M\_{t^{\prime}}. |  | (5.5) |

Thus, we get the desired result.
∎

Let us introduce the notation L2​([0,T])L^{2}([0,T]) as the space of all processes K=(Kt)t∈[0,T]K=(K\_{t})\_{t\in[0,T]} that KK is 𝔽\mathbb{F}-progressively measurable and satisfies 𝔼​[∫0T|Kt|2​𝑑t]<∞\mathbb{E}[\int\_{0}^{T}|K\_{t}|^{2}dt]<\infty. For any semimartingale N=(Ns)s∈[0,T]N=(N\_{s})\_{s\in[0,T]}, we denote L2​([0,T];N)L^{2}([0,T];N) the space of all processes K=(Kt)t∈[0,T]K=(K\_{t})\_{t\in[0,T]} that KK is 𝔽\mathbb{F}-progressively measurable and satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Kt|2​d​⟨N⟩t]<∞,\displaystyle\mathbb{E}\left[\int\_{0}^{T}|K\_{t}|^{2}d\left<N\right>\_{t}\right]<\infty, |  |

where ⟨N⟩t\left<N\right>\_{t} is the quadratic variation process of NN. It follows from the martingale orthogonality condition that, for any test process ς=(ςt)t∈[0,T]∈L2​([0,T];M)\varsigma=(\varsigma\_{t})\_{t\in[0,T]}\in L^{2}([0,T];M),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0∞ςt​𝑑Mt]=0.\displaystyle\mathbb{E}\left[\int\_{0}^{\infty}\varsigma\_{t}dM\_{t}\right]=0. |  | (5.6) |

In fact, the following result shows that this is a necessary and sufficient condition for martingale.

###### Proposition 5.2 (Proposition 4 in jia2022policy).

A diffusion process NN is a martingale if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0∞ςt​𝑑Nt]=0\displaystyle\mathbb{E}\left[\int\_{0}^{\infty}\varsigma\_{t}dN\_{t}\right]=0 |  | (5.7) |

for any ς∈L2​([0,T];N)\varsigma\in L^{2}([0,T];N).

Given a feedback strategy 𝝅​(t,x)=(πi​j​(t,x))i,j∈𝕀m{\bm{\pi}}(t,x)=(\pi\_{ij}(t,x))\_{i,j\in\mathbb{I}\_{m}}, we parameterize the value function using a family of functions vξ​(t,x,i)v^{\xi}(t,x,i) satisfying vξ​(T,x,i)=h​(x)v^{\xi}(T,x,i)=h(x), where ξ∈Θ⊂ℝLξ\xi\in\Theta\subset\mathbb{R}^{L\_{\xi}} and LξL\_{\xi} is the dimension of the parameter vector. Let Mξ=(Mtξ)t∈[0,T]M^{\xi}=(M\_{t}^{\xi})\_{t\in[0,T]} be the parameterized version of the martingale process MM. Proposition [5.2](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem2 "Proposition 5.2 (Proposition 4 in jia2022policy). ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") establishes that finding the optimal parameters ξ\xi reduces to solving the martingale orthogonality equation ([5.7](https://arxiv.org/html/2512.04697v1#S5.E7 "In Proposition 5.2 (Proposition 4 in jia2022policy). ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). This can be implemented through stochastic approximation with the parameter update:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ←ξ+αξ​∫0Tςs​𝑑Msξ,\displaystyle\xi\leftarrow\xi+\alpha\_{\xi}\int\_{0}^{T}\varsigma\_{s}dM\_{s}^{\xi}, |  | (5.8) |

where αξ>0\alpha\_{\xi}>0 is the learning rate.

However, the update rule ([5.8](https://arxiv.org/html/2512.04697v1#S5.E8 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) involves a continuous-time integral that cannot be directly implemented computationally. To address this, we develop a discrete-time approximation of the martingale orthogonality condition. Let K∈ℕK\in\mathbb{N} be the number of time intervals and Δ​t=T/K\Delta t=T/K be the step size. Consider the discrete partition 0=t0<t1<t2<⋯<tK=T0=t\_{0}<t\_{1}<t\_{2}<\cdots<t\_{K}=T with tk−tk−1=Δ​tt\_{k}-t\_{k-1}=\Delta t for k=1,…,Kk=1,\dots,K. Motivated by the continuous-time update ([5.8](https://arxiv.org/html/2512.04697v1#S5.E8 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")), we choose the test process ςt=∂vξ∂ξ​(t,Xt,It)\varsigma\_{t}=\frac{\partial v^{\xi}}{\partial\xi}(t,X\_{t},I\_{t}) and propose the following discretized update rule to update parameters after a whole episode (offline):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ←ξ+αξ​∑k=0K−1∂vξ∂ξ​(tk,Xtk,Itk)​Δ​ξk\displaystyle\xi\leftarrow\xi+\alpha\_{\xi}\sum\_{k=0}^{K-1}\frac{\partial v^{\xi}}{\partial\xi}(t\_{k},X\_{t\_{k}},I\_{t\_{k}})\Delta\xi\_{k} |  | (5.9) |

or to update parameters at every time step (online):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ←ξ+αξ​∂vξ∂ξ​(tk,Xtk,Itk)​Δ​ξk.\displaystyle\xi\leftarrow\xi+\alpha\_{\xi}\frac{\partial v^{\xi}}{\partial\xi}(t\_{k},X\_{t\_{k}},I\_{t\_{k}})\Delta\xi\_{k}. |  | (5.10) |

Here Δ​ξk\Delta\xi\_{k} for k=0,1,,..,K−1k=0,1,,..,K-1 is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ξk=vξ​(tk+1,Xtk+1,Itk+1)−vξ​(tk,Xtk,Itk)+(f​(tk,Xtk,Itk)+λ​R​(𝝅tkξ,Itk))​Δ​t−gItk​Itk+1,\displaystyle\Delta\xi\_{k}=v^{\xi}(t\_{k+1},X\_{t\_{k+1}},I\_{t\_{k+1}})-v^{\xi}(t\_{k},X\_{t\_{k}},I\_{t\_{k}})+\left(f(t\_{k},X\_{t\_{k}},I\_{t\_{k}})+\lambda R({\bm{\pi}}^{\xi}\_{t\_{k}},I\_{t\_{k}})\right)\Delta t-g\_{I\_{t\_{k}}I\_{t\_{k+1}}}, |  | (5.11) |

where the parameterized strategy 𝝅ξ​(t,x)=(πi​jξ​(t,x))i,j∈𝕀m{\bm{\pi}}^{\xi}(t,x)=(\pi^{\xi}\_{ij}(t,x))\_{i,j\in\mathbb{I}\_{m}} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​jξ​(t,x)=exp⁡(vξ​(t,x,j)−gi​j−vξ​(t,x,i)λ),j≠i,\displaystyle\pi\_{ij}^{\xi}(t,x)=\exp\left(\frac{v^{\xi}(t,x,j)-g\_{ij}-v^{\xi}(t,x,i)}{\lambda}\right),\penalty 10000\ j\neq i, |  | (5.12) |

and πi​iξ​(t,x)=−∑j≠iπi​jξ​(t,x)\pi\_{ii}^{\xi}(t,x)=-\sum\_{j\neq i}\pi\_{ij}^{\xi}(t,x).

Based on the above updating rules, we can present the pseudo-code of the offline PE algorithm in Algorithm [1](https://arxiv.org/html/2512.04697v1#alg1 "Algorithm 1 ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"). The online PE algorithm can be devised in a similar fashion and is omitted.

Algorithm 1  Policy Evaluation Algorithm (Offline)

Input:
Initial state (x0,i0)(x\_{0},i\_{0}), horizon TT, number of regimes mm, time step Δ​t\Delta t, number of episodes NN, number of mesh grids KK, initial learning rates αξ​(⋅)\alpha\_{\xi}(\cdot) (a function of the number of episodes), functional forms of parameterized value function vξ​(⋅)v^{\xi}(\cdot), policy 𝝅ξ​(⋅)\bm{\pi}^{\xi}(\cdot), regime switching costs (gi​j)i,j∈𝕀m(g\_{ij})\_{i,j\in\mathbb{I}\_{m}} and temperature parameter λ\lambda.
  
  Required Program: an environment simulator (x′,i′,f′)=(x^{\prime},i^{\prime},f^{\prime})= Environment (t,x,i,j)Δ​t{}\_{\Delta t}(t,x,i,j) that takes current time-state pair (t,x,i)(t,x,i) and action jj (the regime to switch to; if j=ij=i, no switching occurs) as inputs and generates state x′x^{\prime}, i′=ji^{\prime}=j and reward f′f^{\prime} at time t+Δ​tt+\Delta t as outputs .
  
  Learning Procedure:

  

1:Initialize ξ\xi, and ℓ=1\ell=1.

2:while ℓ<N\ell<N do

3:  Initialize k=0k=0. Observe initial state x0,i0x\_{0},i\_{0} and store (xt0,it0)←(x0,i0)(x\_{t\_{0}},i\_{t\_{0}})\leftarrow(x\_{0},i\_{0}).

4:  while k<Kk<K do

5:    Generate action jtkj\_{t\_{k}} by 𝝅ξ​(tk,xtk)\bm{\pi}^{\xi}\left(t\_{k},x\_{t\_{k}}\right).

6:    Apply jtkj\_{t\_{k}} to environment simulator (x,i,f)=(x,i,f)= Environment (tk,xtk,itk,jtk)Δ​t{}\_{\Delta t}(t\_{k},x\_{t\_{k}},i\_{t\_{k}},j\_{t\_{k}}).

7:    Observe new state xx and ii as output. Store xtk+1←xx\_{t\_{k+1}}\leftarrow x, itk+1←ii\_{t\_{k+1}}\leftarrow i and ftk←ff\_{t\_{k}}\leftarrow f.

8:    Update k←k+1k\leftarrow k+1.

9:  end while

10:  For every k=0,1,…,K−1k=0,1,...,K-1, compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ξk\displaystyle\Delta\xi\_{k} | =vξ​(tk+1,xtk+1,itk+1)−vξ​(tk,xtk,itk)+(ftk+λ​R​(𝝅ξ​(tk,xtk),itk))​Δ​t−gitk​itk+1.\displaystyle=v^{\xi}(t\_{k+1},x\_{t\_{k+1}},i\_{t\_{k+1}})-v^{\xi}(t\_{k},x\_{t\_{k}},i\_{t\_{k}})+\left(f\_{t\_{k}}+\lambda R({\bm{\pi}}^{\xi}(t\_{k},x\_{t\_{k}}),i\_{t\_{k}})\right)\Delta t-g\_{i\_{t\_{k}}i\_{t\_{k+1}}}. |  |

11:  Update ξ\xi by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ\displaystyle\xi | ←ξ+αξ​(ℓ)​∑k=0K−1∂vξ∂ξ​(tk,xtk,itk)​Δ​ξk,\displaystyle\leftarrow\xi+\alpha\_{\xi}(\ell)\sum\_{k=0}^{K-1}\frac{\partial v^{\xi}}{\partial\xi}\left(t\_{k},x\_{t\_{k}},i\_{t\_{k}}\right)\Delta\xi\_{k}, |  |

12:  Update ℓ←ℓ+1\ell\leftarrow\ell+1.

13:end while

Proposition [4.1](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and Theorem [4.2](https://arxiv.org/html/2512.04697v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Policy Iteration and Convergence ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") confirm the improvement and convergence results of the policy iteration. Meanwhile, Lemma [5.1](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem1 "Lemma 5.1. ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") and Proposition [5.2](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem2 "Proposition 5.2 (Proposition 4 in jia2022policy). ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") show that policy evaluation can be performed by solving the martingale orthogonality condition via stochastic approximation. A natural question arises: what can be said about the convergence of Algorithm [1](https://arxiv.org/html/2512.04697v1#alg1 "Algorithm 1 ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")? To address this, we next turn to an analysis of the error estimates for Algorithm [1](https://arxiv.org/html/2512.04697v1#alg1 "Algorithm 1 ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes").

We reformulate the update rule in equation ([5.9](https://arxiv.org/html/2512.04697v1#S5.E9 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξi+1←ξi+αξ​(i)​Ψ​(ξi;X,I,𝝅ξi),i≥1,\displaystyle\xi\_{i+1}\leftarrow\xi\_{i}+\alpha\_{\xi}(i)\Psi(\xi\_{i};X,I,{\bm{\pi}}^{\xi\_{i}}),\quad i\geq 1, |  | (5.13) |

where

|  |  |  |
| --- | --- | --- |
|  | Ψ​(ξi;X,I,𝝅ξi)=∑k=0K−1∂vξ∂ξ​(tk,Xtk,Itk)​Δ​ξk,\displaystyle\Psi(\xi\_{i};X,I,{\bm{\pi}}^{\xi\_{i}})=\sum\_{k=0}^{K-1}\frac{\partial v^{\xi}}{\partial\xi}(t\_{k},X\_{t\_{k}},I\_{t\_{k}})\Delta\xi\_{k}, |  |

with Δ​ξk\Delta\xi\_{k} defined in equation ([5.11](https://arxiv.org/html/2512.04697v1#S5.E11 "In 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")). For notational convenience, we introduce the shorthand Yi+1=(X,I,𝝅ξi)Y\_{i+1}=(X,I,{\bm{\pi}}^{\xi\_{i}}) for i≥1i\geq 1. We further define the expected update function as ψ​(ξ):=𝔼​[Ψ​(ξ;Y)]\psi(\xi):=\mathbb{E}[\Psi(\xi;Y)]. To establish convergence guarantees, we make the following technical assumptions.

###### Assumption 5.3.

* (i)

  The ordinary differential equation ξ′​(t)=ψ​(ξ​(t))\xi^{\prime}(t)=\psi(\xi(t)) has a unique stable equilibrium point ξ∗\xi^{\*}.
* (ii)

  There exists a constant C>0C>0 such that 𝔼​[|Ψ​(ξi;Yi+1)|2|ξi]≤C​(1+|ξi|2)\mathbb{E}[|\Psi(\xi\_{i};Y\_{i+1})|^{2}|\xi\_{i}]\leq C(1+|\xi\_{i}|^{2}) for all iterations.
* (iii)

  There exists κ>0\kappa>0 such that (ξ−ξ∗)⋅ψ​(ξ)≤−κ​|ξ−ξ∗|2(\xi-\xi^{\*})\cdot\psi(\xi)\leq-\kappa|\xi-\xi^{\*}|^{2} for all ξ∈ℝLξ\xi\in\mathbb{R}^{L\_{\xi}}.
* (iv)

  There exist constants ρ,C>0\rho,C>0 such that supj∈𝕀m|vξ​(⋅,j)−vξ∗​(⋅,j)|C0​(𝒟¯)≤C​|ξ−ξ∗|ρ\sup\_{j\in\mathbb{I}\_{m}}|v^{\xi}(\cdot,j)-v^{\xi^{\*}}(\cdot,j)|\_{C^{0}(\overline{{\cal D}})}\leq C|\xi-\xi^{\*}|^{\rho} for all ξ∈ℝLξ\xi\in\mathbb{R}^{L\_{\xi}}.

Under these conditions, we now present the main convergence result, which provides the explicit error bound for Algorithm [1](https://arxiv.org/html/2512.04697v1#alg1 "Algorithm 1 ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes").

###### Theorem 5.4.

Let Assumption [5.3](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem3 "Assumption 5.3. ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") hold. Set αξ​(i)=Aiν+B\alpha\_{\xi}(i)=\frac{A}{i^{\nu}+B} for some ν≤1\nu\leq 1, A>ν2​κA>\frac{\nu}{2\kappa} and B>0B>0, and let ϵ>0\epsilon>0. Then there exists C>0C>0 (independent of n,ϵn,\epsilon) such that with probability of at least 1−ϵ1-\epsilon,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supj∈𝕀m|vξi​(⋅,j)−v​(⋅,j)|C0​(𝒟¯)≤supj∈𝕀m|v​(⋅,j)−vξ∗​(⋅,j)|C0​(𝒟¯)+Cϵρξ/2​i−ν​ρξ2.\displaystyle\sup\_{j\in\mathbb{I}\_{m}}|v^{\xi\_{i}}(\cdot,j)-v(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})}\leq\sup\_{j\in\mathbb{I}\_{m}}|v(\cdot,j)-v^{\xi^{\*}}(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})}+\frac{C}{\epsilon^{\rho\_{\xi}/2}}i^{-\frac{\nu\rho\_{\xi}}{2}}. |  | (5.14) |

###### Proof.

Under Assumptions [5.3](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem3 "Assumption 5.3. ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") (i)–(iii) and the step-size condition on αξ​(i)\alpha\_{\xi}(i), an application of Theorem 22 in benveniste2012adaptive yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|ξi−ξ∗|2]≤C​i−ν\displaystyle\mathbb{E}[|\xi\_{i}-\xi^{\*}|^{2}]\leq Ci^{-\nu} |  |

where C>0C>0 is a constant independent of nn. This bound in turn implies that

|  |  |  |
| --- | --- | --- |
|  | |ξi−ξ∗|2≤C​ϵ−12​i−ν2\displaystyle|\xi\_{i}-\xi^{\*}|^{2}\leq C\epsilon^{-\frac{1}{2}}i^{-\frac{\nu}{2}} |  |

with probability at least 1−ϵ1-\epsilon. Then, invoking Assumption [5.3](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem3 "Assumption 5.3. ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") (iv), we deduce that with probability at least 1−ϵ1-\epsilon,

|  |  |  |
| --- | --- | --- |
|  | supj∈𝕀m|vξi​(⋅,j)−v​(⋅,j)|C0​(𝒟¯)\displaystyle\sup\_{j\in\mathbb{I}\_{m}}|v^{\xi\_{i}}(\cdot,j)-v(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤supj∈𝕀m|v​(⋅,j)−vξ∗​(⋅,j)|C0​(𝒟¯)+supj∈𝕀m|vξ∗​(⋅,j)−vξi​(⋅,j)|C0​(𝒟¯)\displaystyle\leq\sup\_{j\in\mathbb{I}\_{m}}|v(\cdot,j)-v^{\xi^{\*}}(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})}+\sup\_{j\in\mathbb{I}\_{m}}|v^{\xi^{\*}}(\cdot,j)-v^{\xi\_{i}}(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤supj∈𝕀m|vξ∗(⋅,)−v(⋅,j)|C0​(𝒟¯)+Cϵρξ/2i−ν​ρξ2.\displaystyle\leq\sup\_{j\in\mathbb{I}\_{m}}|v^{\xi^{\*}}(\cdot,)-v(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})}+\frac{C}{\epsilon^{\rho\_{\xi}/2}}i^{-\frac{\nu\rho\_{\xi}}{2}}. |  |

This completes the proof of the theorem.
∎

Theorem [5.4](https://arxiv.org/html/2512.04697v1#S5.Thmtheorem4 "Theorem 5.4. ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") establishes a comprehensive error analysis for Algorithm [1](https://arxiv.org/html/2512.04697v1#alg1 "Algorithm 1 ‣ 5 Reinforcement Learning Algorithm ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), providing both theoretical guarantees and practical insights into its convergence behavior. The result demonstrates that the policy evaluation error can be systematically decomposed into two distinct components: the approximation error of the parametric function class and the algorithmic error arising from the stochastic approximation procedure. The first term, supj∈𝕀m|v​(⋅,j)−vξ∗​(⋅,j)|C0​(𝒟¯)\sup\_{j\in\mathbb{I}\_{m}}|v(\cdot,j)-v^{\xi^{\*}}(\cdot,j)|\_{C^{0}({\overline{{\cal D}}})}, represents the inherent approximation capability of our chosen parametric family. This bias term is independent of the learning algorithm and reflects how well the optimal parameter ξ∗\xi^{\*} can approximate the true value function within the selected function class. The second term, C​i−ν​ρξ2/ϵρξ/2Ci^{-\frac{\nu\rho\_{\xi}}{2}}/\epsilon^{\rho\_{\xi}/2}, exhibits a polynomial decay with respect to the iteration number ii and vanishes asymptotically as the number of iterations increases, demonstrating the algorithm’s convergence to the optimal parameter configuration within the chosen function class.

## 6 Numerical Examples

This section presents some numerical experiments to demonstrate the practical efficacy of the proposed RL algorithm. We first examine a bounded regulator problem to analyze the algorithm’s convergence property and policy behavior. Subsequently, we apply the algorithm to a put option selection problem involving the optimal switching between risky assets, showcasing its effectiveness in a more complex, multi-regime setting with some financial interpretations.

### 6.1 Bounded Regulator Problem

To establish a performance benchmark for our algorithm, we consider a finite-horizon optimal switching problem with two regimes, conceptualized as a bounded regulator. This classic problem provides a tractable yet non-trivial testbed where the optimal policy has an intuitive structure, allowing for clear interpretation of the algorithm’s learned strategy.

The system state X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} evolves according to regime-specific stochastic dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=μi​d​t+σ​d​Wt,i∈{0,1},t∈[0,T],\displaystyle dX\_{t}=\mu\_{i}dt+\sigma dW\_{t},\quad i\in\{0,1\},\penalty 10000\ t\in[0,T], |  | (6.1) |

with initial condition X0=x∈ℝX\_{0}=x\in\mathbb{R}. Here, W=(Wt)t∈[0,T]W=(W\_{t})\_{t\in[0,T]} is a standard Brownian motion. The parameters are chosen with symmetry: the drift coefficients are μ0=−2\mu\_{0}=-2 and μ1=2\mu\_{1}=2, and the volatility is σ=0.5\sigma=0.5. This symmetric setup induces a natural switching logic to correct the state’s deviation.

The controller’s objective is to maximize the expected total reward over the horizon [0,T][0,T], which comprises a running reward and a terminal reward:

|  |  |  |
| --- | --- | --- |
|  | f​(x)=2​e−2​x2−0.1,h​(x)=2​e−2​x2,x∈ℝ.\displaystyle f(x)=2e^{-2x^{2}}-0.1,\quad h(x)=2e^{-2x^{2}},\quad x\in\mathds{R}. |  |

The Gaussian bump shape of the functions ff and hh creates a strong incentive to maintain the state XtX\_{t} near zero, as the reward attains its maximum value at x=0x=0. Each switch between regimes incurs a cost, specified as g01=g10=0.5g\_{01}=g\_{10}=0.5. This cost penalizes excessive control actions, forcing the optimal policy to strategically balance the benefit of corrective switching against the incurred cost.

We use a discrete version of ([6.1](https://arxiv.org/html/2512.04697v1#S6.E1 "In 6.1 Bounded Regulator Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")) for t=0,Δ​t,…,K​Δ​tt=0,\Delta t,...,K\Delta t with K=100K=100 and Δ​t=T/K\Delta t=T/K. The value function and policy are approximated by a neural network in the PyTorch framework
with the architecture and parameters summarized in Table [1](https://arxiv.org/html/2512.04697v1#S6.T1 "Table 1 ‣ 6.1 Bounded Regulator Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes").

Table 1: Neural Network Architecture and Training Parameters for the Regulator Problem

|  |  |
| --- | --- |
| Component | Specification |
| Network Architecture | 2 hidden layers |
| Activation Functions | ReLU (Layer 1), Tanh (Layer 2) |
| Hidden Dimension | 128 |
| Batch Size | 64 |
| Optimizer | Adam |
| Learning Rate | 1×10−31\times 10^{-3} |
| Training Episodes | 1000 |

The training progression under the temperature parameter λ=0.2\lambda=0.2 is shown in Figure [1](https://arxiv.org/html/2512.04697v1#S6.F1 "Figure 1 ‣ 6.1 Bounded Regulator Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")-(a). The loss function decreases efficiently and stabilizes after approximately 400 episodes, indicating the robust convergence of the policy iteration in the RL algorithm. Figure [1](https://arxiv.org/html/2512.04697v1#S6.F1 "Figure 1 ‣ 6.1 Bounded Regulator Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes")-(b) depicts the learned value functions and the corresponding switching probabilities at t=0.5t=0.5. The near symmetry between the value functions for regime 0 (blue line) and regime 1 (orange line) is a direct consequence of the symmetric problem parameters. The switching probabilities—from regime 0 to 1 (green line) and from regime 1 to 0 (yellow line)—are calculated from the optimal intensity π\pi.

![Refer to caption](convergence.png)

![Refer to caption](value.png)

Figure 1: (a): Convergence of the training loss for the bounded regulator problem with λ=0.2\lambda=0.2. (b): Learned value functions and switching probabilities at t=0.5t=0.5 for λ=0.2\lambda=0.2.

A central theoretical result is the convergence of the exploratory solution to the classical optimal switching policy as the temperature parameter λ\lambda tends to zero. We validate this numerically.
Figure [2](https://arxiv.org/html/2512.04697v1#S6.F2 "Figure 2 ‣ 6.1 Bounded Regulator Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") shows that the training loss decreases for different values of λ\lambda, with convergence achieved in all cases. More importantly, Figure [3](https://arxiv.org/html/2512.04697v1#S6.F3 "Figure 3 ‣ 6.1 Bounded Regulator Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") illustrates the fundamental transformation of the optimal policy. For a larger λ\lambda (e.g., 0.2), the switching probability is a smooth function of the state, reflecting exploratory randomization. As λ\lambda decreases to 0.01, the probability curve becomes sharp and nearly binary, approaching a deterministic threshold-based policy. This visual evidence strongly supports the theoretical finding that the solutions of the exploratory HJB equations converge to the solution of the classical variational inequalities as λ→0\lambda\to 0.

![Refer to caption](compare_lambda_convergence.png)


Figure 2: Training convergence for different temperature parameters λ\lambda.

![Refer to caption](compare_lambda_probability.png)


Figure 3: Evolution of the switching probability from regime 0 to 1 as λ\lambda decreases.

### 6.2 Put Option Selection Problem

To demonstrate the algorithm’s applicability in finance, we model an investor who aims to optimally switch an investment decision between three regimes: two European put options on different assets and a risk-free savings account. The investor’s wealth can be allocated to one of three regimes during the finite horizon [0,T][0,T]:

* •

  regime 0: a put option on Stock AA.
* •

  regime 1: a put option on Stock BB.
* •

  regime 2: the risk-free savings account.

The underlying stock prices follow the geometric Brownian motion:

|  |  |  |
| --- | --- | --- |
|  | d​StA=μA​StA​d​t+σA​StA​d​Wt,d​StB=μB​StB​d​t+σB​StB​d​Wt,t∈(0,T],\displaystyle dS^{A}\_{t}=\mu^{A}S^{A}\_{t}dt+\sigma^{A}S^{A}\_{t}dW\_{t},\quad dS^{B}\_{t}=\mu^{B}S^{B}\_{t}dt+\sigma^{B}S^{B}\_{t}dW\_{t},\quad t\in(0,T], |  |

with S0A=sA∈[0,∞),S0B=sB∈[0,∞)S^{A}\_{0}=s^{A}\in[0,\infty),S^{B}\_{0}=s^{B}\in[0,\infty). Here the parameters are set by (μA,σA)=(0.1,0.2)(\mu^{A},\sigma^{A})=(0.1,0.2) and (μB,σB)=(0.05,0.1)(\mu^{B},\sigma^{B})=(0.05,0.1), and W=(Wt)t∈[0,T]W=(W\_{t})\_{t\in[0,T]} is a standard Brownian motion. The risk free rate is r=0.05r=0.05. For any time t∈[0,T]t\in[0,T], the investor decides a action It∈{0,1,2}I\_{t}\in\{0,1,2\}, which determines the regime in which the investor’s wealth is allocated. Switching between regimes incurs transaction costs given by the matrix:

|  |  |  |
| --- | --- | --- |
|  | G=(gi​j)0≤i,j≤2=[00.020.010.0200.010.020.020].\displaystyle G=(g\_{ij})\_{0\leq i,j\leq 2}=\begin{bmatrix}0&0.02&0.01\\ 0.02&0&0.01\\ 0.02&0.02&0\end{bmatrix}. |  |

The investor’s objective is to maximize the expected total reward over the horizon [0,T][0,T], where the running reward function is given by

|  |  |  |
| --- | --- | --- |
|  | f​(sA,sB,i)={(SK−sA)+,i=0,(SK−sB)+,i=1,r​SK,i=2,\displaystyle f(s^{A},s^{B},i)=\begin{cases}(S\_{K}-s^{A})^{+},&i=0,\\ (S\_{K}-s^{B})^{+},&i=1,\\ rS\_{K},&i=2,\end{cases} |  |

with the strike price SK=1S\_{K}=1 and (x)+:=max⁡{x,0}(x)^{+}:=\max\{x,0\} for x∈ℝx\in\mathds{R}. The terminal reward function is assumed to be 0.

We set the time horizon T=1T=1, the number of time intervals K=50K=50, the step size Δ​t=T/K=0.02\Delta t=T/K=0.02, and the temperature parameter λ=0.1\lambda=0.1. The value function and policy are approximated by a neural network with the architecture and parameters summarized in Table [2](https://arxiv.org/html/2512.04697v1#S6.T2 "Table 2 ‣ 6.2 Put Option Selection Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"). The model was implemented within the PyTorch framework.

Table 2: Neural Network Architecture and Training Parameters for the Regulator Problem

|  |  |
| --- | --- |
| Component | Specification |
| Network Architecture | 2 hidden layers |
| Activation Functions | Tanh (Layer 1), Tanh (Layer 2) |
| Hidden Dimension | 128 |
| Batch Size | 512 |
| Optimizer | Adam |
| Learning Rate | 1×10−41\times 10^{-4} |
| Training Episodes | 1000 |

According to Figure [4](https://arxiv.org/html/2512.04697v1#S6.F4 "Figure 4 ‣ 6.2 Put Option Selection Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes"), at the beginning of training, the loss exhibits a oscillation, and the convergence is very pronounced. It becomes stable when the number of episodes exceeds 800. Figure [5](https://arxiv.org/html/2512.04697v1#S6.F5 "Figure 5 ‣ 6.2 Put Option Selection Problem ‣ 6 Numerical Examples ‣ Continuous-time reinforcement learning for optimal switching over multiple regimes") shows the allocation of the asset at time t=0.5t=0.5. We can find that, when stock price of AA and BB large enough, the investor will put all in bank. When stock B has lower price, she tends to hold put AA; When stock AA has lower price, she tends to hold put BB.

![Refer to caption](loss_option.png)


Figure 4: The training loss for the put option selection problem.

![Refer to caption](asset_allocation.png)


Figure 5: The optimal asset allocation policy at t=0.5t=0.5 as a function of stock prices SAS^{A} and SBS^{B}.

Acknowledgements: Yijie Huang, Mengge Li and Xiang Yu are supported by the Hong Kong RGC General Research Fund (GRF) under grant no. 15211524 and the Hong Kong Polytechnic University research grant under no. P0045654.