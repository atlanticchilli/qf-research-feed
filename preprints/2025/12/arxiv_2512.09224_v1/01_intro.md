---
authors:
- Yuling Max Chen
- Bin Li
- David Saunders
doc_id: arxiv:2512.09224v1
family_id: arxiv:2512.09224
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Exploratory Mean-Variance with Jumps: An Equilibrium Approach'
url_abs: http://arxiv.org/abs/2512.09224v1
url_html: https://arxiv.org/html/2512.09224v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yuling Max Chen
Department of Statistics and Actuarial Science, University of
Waterloo, Waterloo ON N2L 3G1, Canada (yuling.chen@uwaterloo.ca)
  
Bin Li
Department of Statistics and Actuarial Science, University of
Waterloo, Waterloo ON N2L 3G1, Canada (bin.li@uwaterloo.ca)
  
David Saunders
Department of Statistics and Actuarial Science, University of
Waterloo, Waterloo ON N2L 3G1, Canada (dsaunder@uwaterloo.ca).

(December 10, 2025)

Revisiting the continuous-time Mean-Variance (MV) Portfolio Optimization problem, we model the market dynamics with a jump-diffusion process and apply Reinforcement Learning (RL) techniques to facilitate informed exploration within the control space. We recognize the time-inconsistency of the MV problem and adopt the time-inconsistent control (TIC) approach to analytically solve for an exploratory equilibrium investment policy, which is a Gaussian distribution centered on the equilibrium control of the classical MV problem. Our approach accounts for time-inconsistent preferences and actions, and our equilibrium policy is the best option an investor can take at any given time during the investment period.
Moreover, we leverage the martingale properties of the equilibrium policy, design a RL model, and propose an Actor-Critic RL algorithm.
All of our RL model parameters converge to the corresponding true values in a simulation study. Our numerical study on 24 years of real market data shows that the proposed RL model is profitable in 13 out of 14 tests, demonstrating its practical applicability in real world investment.

## 1 Introduction

The Mean-Variance (MV) portfolio optimization problem, first introduced by [markowitz1952portfolio], has been
the subject of extensive research.
In the continuous-time setting, an MV investor aims to optimize her financial outcome by pursuing the highest possible portfolio return with the lowest risk, measured by portfolio volatility, at the end of the investment horizon.
[jorion1992portfolio] investigated the practical challenges of implementing the MV investment policy in
real-world markets. [zhou2000continuous] studied the Lagrangian dual of the MV problem as a stochastic linear-quadratic optimal control problem.
Later on, [chiu2006asset] solved for the MV efficient frontier, and [xie2008continuous] derived the optimal investment policy in an incomplete market setting; see [zhang2018portfolio, kalayci2019comprehensive] for a broader overview of the the past studies of the MV problem.

In this paper, we take the stochastic control approach and extend the classical MV problem in two directions. In the first direction, we employ a Reinforcement Learning (RL) facilitated exploratory formulation of the MV problem.
In the recent stochastic control literature, there is an emerging trend of applying RL techniques to classical stochastic control problems [wang2020continuous, wang2020reinforcement, jiang2022reinforcement, jia2022policy, PE, jia2023q, dai2023learning, wu2024reinforcement, chen2025EMVRS].
The fundamental technique is to replace the optimal solution to the classical stochastic control problem with a probability distribution (centered around the original optimal solution), in light of the Stochastic RL Algorithm by [gullapalli1990stochastic].
Such a distribution-valued control is often called an exploratory control or a policy in the RL context. In this way, the exploratory control is capable of informed exploration within the control space, while maintaining greedy exploitation towards optimality.
We point out here that the major motivation for such an exploratory formulation is the lack of knowledge of the controlled dynamics. Taking portfolio optimization as an example, the controlled dynamics is the portfolio value process that depends on the market dynamics. However, the precise law of the market evolution is unknown, and even a simple diffusion model requires knowledge of the drift and diffusion terms.

[wang2020reinforcement] first introduced this “exploratory extension” to their controlled dynamics and solved for the optimal exploratory control of a linear-quadratic problem.
They also proved the asymptotic equivalence between the classical solution and the exploratory solution.
Later, [PE, jia2022policy, jia2023q] leveraged the martingale properties of the optimal solutions to the exploratory-extended stochastic control problems and developed effective learning algorithms for RL policy evaluation and policy updates.
[wang2020continuous] studied the Exploratory Mean-Variance (EMV) problem, which solves for a distribution-valued investment policy centered on the classical MV solution.
Since the EMV problem uses the Lagrangian dual of the classical MV problem, it is a time-consistent control problem and the proposed investment policy in [wang2020continuous] is only optimal at the beginning of the investment horizon.

In contrast, [dai2023learning] investigated the EMV problem as a time-inconsistent control (TIC) problem, as the time-inconsistency arises from the variance of terminal portfolio values, a quadratic function of the expected terminal portfolio value. Taking the TIC approach in [bjork2021time], [dai2023learning] solved the Extended Hamiltonian-Jacobi-Bellman (EHJB) equations for an equilibrium policy, which is a probability distribution centered around the classical TIC solution provided in [bjork2021time].
While [dai2023learning] incorporated an exogenous and hidden state to model the unobservable market regimes or economic conditions, [wu2024reinforcement] and [chen2025EMVRS] modeled the market regimes more directly with a time-homogeneous Markov chain and solved the EMV problem with regime-switching.
Moreover, [chen2025EMVRS] also pointed out the significance of model parameter convergence as an evaluation criterion for RL models.

Our second extension to the classical MV problem is the incorporation of a jump component in the controlled dynamics, which is used to account for sudden shocks in the market.
Jump-diffusion models have been widely applied to optimal stopping [pham1997optimal, mordecki2002optimal, bayraktar2008optimizing], option evaluation [amin1993jump, xu2009jump, andersen2000jump, carr2007numerical, clift2008numerical, toivanen2008numerical], and hedging problems [park1993optimal, he2006calibration, mina2015approximate].
The MV problem with jump-diffusion controlled dynamics is solved in [oksendal2005applied] in the classical stochastic control formulation. More recently, [gao2024reinforcement] introduced the exploratory formulation of stochastic control problems with jump-diffusion controlled dynamics. However, both of them considered the Lagrangian dual of the MV problem, hence following the time-consistent control approach.

Differing from [gao2024reinforcement] and [oksendal2005applied], this paper tackles the EMV problem for a jump-diffusion by considering it as a TIC problem and solving for an equilibrium solution, an approach adopted by [dai2023learning] and [bjork2021time]. We establish the exploratory formulation of the MV problem with jump-diffusion market dynamics, which we call the Exploratory Mean-Variance with Jumps (EMVJ) problem.
We derive the EHJB equations and solve for an equilibrium investment policy in explicit form. Our solution aligns with [bjork2021time] if we remove the exploration and the jumps in the dynamics. Following [PE], we then utilize the martingale properties of our analytical solutions and develop an Actor-Critic RL algorithm. Through iterative interactions with the market, our algorithm is able to gradually understand the market behavior and learn the equilibrium investment policy, without the knowledge of the underlying market dynamics.
Our numerical results demonstrates the effectiveness of our RL algorithm on simulated data, as well as the practical applicability of our RL model on real market data.

We make two main contributions to the literature. First, we fill a gap in the literature by solving the EMV problem with jump-diffusion dynamics via the TIC approach. We note that [gao2024reinforcement], as well as many other existing works [wang2020continuous, gao2024reinforcement, wu2024reinforcement, chen2025EMVRS], solved the Lagrangian dual of the MV problem. Their investment strategies are optimal at the beginning of an investment horizon subject to a prespecified investment target, disregarding the time-inconsistent preferences and actions an investor can have. Our equilibrium investment policy is a game-theoretical result, supposing an investor competes with her future incarnations throughout the investment horizon. Therefore, our equilibrium investment policy is the best action an investor can take, at any given time during the investment horizon.
Second, we fully leverage our analytical solutions in the design of a RL model, by parameterizing the RL model with market parameters that have practical meanings. Our choice of parameterization not only enables us to check whether the parameters have converged to the true values in our simulation study, but also significantly simplifies the RL model111As described in Section [4](https://arxiv.org/html/2512.09224v1#S4 "4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), our RL model has only 3 parameters.  without sacrificing its effectiveness.

The remainder of this paper is structured as follows. We review the necessary background and preliminaries in Section [2](https://arxiv.org/html/2512.09224v1#S2 "2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). In Section [3](https://arxiv.org/html/2512.09224v1#S3 "3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"),
we introduce the EMVJ problem and present the verification theorem and analytical solutions. We propose a RL algorithm in Section [4](https://arxiv.org/html/2512.09224v1#S4 "4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and present our numerical results in Section [5](https://arxiv.org/html/2512.09224v1#S5 "5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). Finally, we conclude in Section [6](https://arxiv.org/html/2512.09224v1#S6 "6 Conclusion ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").

## 2 Problem Formulation and Preliminaries

We adopt the notation from [oksendal2005applied].
Consider a finite decision horizon TT and a filtered probability space (Ω,ℱ,{ℱt}t∈[0,T],ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{P}).
Let L:={Lt}t∈[0,T]L:=\{L\_{t}\}\_{t\in[0,T]} be a Lévy process and Δ​Ls:=Ls−Ls−\Delta L\_{s}:=L\_{s}-L\_{s-} be the jump of LL at time ss. Denote by 𝑩0\boldsymbol{B}\_{0} the collection of Borel sets of ℝ\mathbb{R} whose closure does not contain 0. Then, for B∈𝑩0B\in\boldsymbol{B}\_{0}, define the Poisson random measure of LL as

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(t,B)=∑s:0≤s≤t1B​(Δ​Ls),N(t,B)=\sum\_{s:0\leq s\leq t}1\_{B}(\Delta L\_{s}), |  | (2.1) |

and the Lévy measure of LL as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν​(B)=𝔼​[N​(1,B)].\nu(B)=\mathbb{E}[N(1,B)]. |  | (2.2) |

Intuitively, N​(t,B)N(t,B) represents the number of jumps of sizes in a Borel set BB up to time tt, whereas ν​(B)\nu(B) measures the expected number of jumps of sizes in BB per unit time. For any B∈𝑩0,{N​(t,B):t∈[0,T]}B\in\boldsymbol{B}\_{0},\{N(t,B):t\in[0,T]\} is a Poisson process with intensity ν​(B)\nu(B).

Define the compensated Poisson random measure as

|  |  |  |  |
| --- | --- | --- | --- |
|  | N~​(d​t,d​z)=N​(d​t,d​z)−ν​(d​z)​d​t.\tilde{N}(dt,dz)=N(dt,dz)-\nu(dz)dt. |  | (2.3) |

We know from [oksendal2005applied] that for any B∈𝑩0,{N~​(t,B):t≥0}B\in\boldsymbol{B}\_{0},\{\tilde{N}(t,B):t\geq 0\} is a martingale. The Lévy measure is ν​(d​z)=ζJ​FJ​(d​z)\nu(dz)=\zeta\_{J}F\_{J}(dz),

where ζJ>0\zeta\_{J}>0 is the arrival rate of Poisson jumps per unit time and FJ​(z)F\_{J}(z) is the probability distribution of jump size zz.
Here, we require that the Lévy measure should satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝmin⁡(1,z2)​ν​(d​z)<∞ and ​∫ℝe2​z​ν​(d​z)<∞.\int\_{\mathbb{R}}\min(1,z^{2})\nu(dz)<\infty\quad\text{ and }\int\_{\mathbb{R}}e^{2z}\nu(dz)<\infty. |  | (2.4) |

For simplicity, we consider investing in a market with one risky asset (stock) and one risk-free asset. The risk-free rate is a constant r≥0r\geq 0.
The stock price is driven by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt−=μ​d​t+σ​d​Wt+∫ℝ(ez−1)​N~​(d​t,d​z),\frac{dS\_{t}}{S\_{t-}}=\mu dt+\sigma dW\_{t}+\int\_{\mathbb{R}}(e^{z}-1)\tilde{N}(dt,dz), |  | (2.5) |

where μ∈ℝ,σ>0\mu\in\mathbb{R},\sigma>0 are constant market parameters and {Wt}t∈[0,T]\{W\_{t}\}\_{t\in[0,T]} is a one-dimensional Brownian Motion on the filtered probability space.
Under the second condition of ([2.4](https://arxiv.org/html/2512.09224v1#S2.E4 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we have
that 𝔼​[St]\mathbb{E}[S\_{t}] and 𝔼​[St2]\mathbb{E}[S\_{t}^{2}] are finite for any t∈[0,T]t\in[0,T], according to [cont2003financial].

An investor controls the money (in dollar value) that she invests in the stock, reallocating the portfolio in response to the behavior of the market.
The discounted self-financing portfolio value X:={Xt}t∈[0,T]X:=\{X\_{t}\}\_{t\in[0,T]} follows the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtu=ut​(μ−r)​d​t+ut​σ​d​Wt+∫ℝut​(ez−1)​N~​(d​t,d​z),dX\_{t}^{u}=u\_{t}(\mu-r)dt+u\_{t}\sigma dW\_{t}+\int\_{\mathbb{R}}u\_{t}(e^{z}-1)\tilde{N}(dt,dz), |  | (2.6) |

where u:={ut:=u​(t,Xtu)}t∈[0,T]u:=\{u\_{t}:=u(t,X\_{t}^{u})\}\_{t\in[0,T]} denotes the control, i.e., money invested in the stock.

###### Remark 2.1

Note that in reality the market parameters, (μ,σ)(\mu,\sigma), and the jump parameters, including ζJ\zeta\_{J} and the parameters of FJ​(z)F\_{J}(z) (the jump size distribution), are unknown. So, investing under a control uu, as a deterministic function of time tt and wealth xx that depends on the market parameters and the jump parameters, is impractical. While one possible solution is to estimate the unknown parameters from the market data, for example using Maximum Likelihood Estimation, this method often suffers from estimation error as the observed market data is just one realization of the market dynamics; see [luenberger2013investment] for the mean-blur problem as a typical example.
Alternatively, we can adopt the idea of Stochastic Reinforcement Learning [gullapalli1990stochastic] that employs a random investor exploring for the optimal investment policy, within the control space. In this way, we avoid estimation error as there is no parameter estimation involved. Instead, the parameters are learned while the investor interacts with the dynamic market. In recent stochastic control literature, such an investor randomization is achieved by extending the classical control uu to a probability distribution valued policy, π\pi, often centered at uu; see [wang2020continuous, wang2020reinforcement, jiang2022reinforcement, chen2025EMVRS, gao2024reinforcement, jia2022policy, jia2023q] for examples of such extensions.

Furthermore, we recognize the difficulty of investing under a control uu in practice, as the market parameters, (μ,σ)(\mu,\sigma), and the jump parameters, including ζJ\zeta\_{J} and the parameters of FJ​(z)F\_{J}(z) (the jump size distribution), are unknown.
Henceforth, we consider an exploratory control, π:={πt,Xtπ​(u):=π​(u;t,Xtπ)}t∈[0,T]\pi:=\{\pi\_{t,X\_{t}^{\pi}}(u):=\pi(u;t,X\_{t}^{\pi})\}\_{t\in[0,T]}, that enables exploration within the control space.
Here, π:(t,x)∈[0,T]×ℝ↦πt,x∈𝒫​(ℝ)\pi:(t,x)\in[0,T]\times\mathbb{R}\mapsto\pi\_{t,x}\in\mathcal{P}(\mathbb{R}) is a stochastic feedback policy, which maps a time and portfolio value pair (t,x)(t,x) to a probability density function on the control space ℝ\mathbb{R}.
For each t∈[0,T]t\in[0,T], let utπ:=u​(t,Xtπ)u\_{t}^{\pi}:=u(t,X\_{t}^{\pi}) be the investment control sampled from πt,Xtπ​(u)\pi\_{t,X\_{t}^{\pi}}(u). Then, a sampled portfolio value process is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtπ=utπ​(μ−r)​d​t+utπ​σ​d​Wt+∫ℝutπ​(ez−1)​N~​(d​t,d​z).dX\_{t}^{\pi}=u\_{t}^{\pi}(\mu-r)dt+u\_{t}^{\pi}\sigma dW\_{t}+\int\_{\mathbb{R}}u\_{t}^{\pi}(e^{z}-1)\tilde{N}(dt,dz). |  | (2.7) |

To account for the stochasticity of the randomly sampled control, we consider an enlargement of the filtered probability space. Following [jia2022policy, jia2023q], we suppose that the probability space is rich enough to support mutually independent copies of a random variable, {Ut,t∈[0,T]}\{U\_{t},t\in[0,T]\}, each uniformly distributed on [0,1][0,1]. Denote by (Ω,ℱ,{𝒢t}t∈[0,T],ℙ¯)(\Omega,\mathcal{F},\{\mathcal{G}\_{t}\}\_{t\in[0,T]},\bar{\mathbb{P}}) the new filtered probability space.
Here, 𝒢s=ℱ∨σ​(Ut,0≤t≤s)\mathcal{G}\_{s}=\mathcal{F}\vee\sigma(U\_{t},0\leq t\leq s) is the σ\sigma-algebra generated by ℱs\mathcal{F}\_{s} and the uniform random variables up to time ss, and ℙ¯\bar{\mathbb{P}} is a product extension from ℙ\mathbb{P}, which is now defined on the extended σ\sigma-algebra 𝒢T\mathcal{G}\_{T}.
Following the arguments in [gao2024reinforcement], we also introduce an extended Poisson random measure, N′​(d​t,d​z,d​v)N^{\prime}(dt,dz,dv), on the product space [0,T]×ℝ×[0,1][0,T]\times\mathbb{R}\times[0,1], where vv is a realization of a Uniform random vector V∼UNIF​([0,1])V\sim\mbox{UNIF}([0,1]). The intensity measure of N′N^{\prime} is given by d​t​ν​(d​z)​d​vdt\,\nu(dz)dv and its compensator is N′~​(d​t,d​z,d​v):=N′​(d​t,d​z,d​v)−d​t​ν​(d​z)​d​v\tilde{N^{\prime}}(dt,dz,dv):=N^{\prime}(dt,dz,dv)-dt\nu(dz)dv.
Furthermore, given a distribution dd, denote Gd:[0,1]→ℝG^{d}:[0,1]\to\mathbb{R} by the quantile function of dd. Then, for some (t,x)(t,x), the policy distribution is πt,x\pi\_{t,x} and a sampled action uu from policy can be realized by sampling v∼UNIF​([0,1])v\sim\mbox{UNIF}([0,1]) and applying the quantile function, i.e., u=Gπt,x​(v)u=G^{\pi\_{t,x}}(v).

Therefore, as we randomly sample trajectories of a control uπu^{\pi} from a policy π\pi and take the average of the portfolio values across trajectories, the sampled portfolio value process in [2.7](https://arxiv.org/html/2512.09224v1#S2.E7 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") follows the same distribution as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtπ=∫ℝu​(μ−r)​πt,Xtπ​(u)​𝑑u​𝑑t+∫ℝu2​σ2​πt,Xtπ​(u)​𝑑u​d​Wt+∫ℝ×[0,1]Gπt,x​(v)​(ez−1)​N′~​(d​t,d​z,d​v),dX\_{t}^{\pi}=\int\_{\mathbb{R}}u(\mu-r)\pi\_{t,X\_{t}^{\pi}}(u)dudt+\sqrt{\int\_{\mathbb{R}}u^{2}\sigma^{2}\pi\_{t,X\_{t}^{\pi}}(u)du}dW\_{t}+\int\_{\mathbb{R}\times[0,1]}G^{\pi\_{t,x}}(v)(e^{z}-1)\tilde{N^{\prime}}(dt,dz,dv), |  | (2.8) |

which we refer to as the exploratory portfolio value process.

###### Definition 2.1 (Admissible Policy)

We say that π:={πt,x​(⋅)}t,x∈[0,T]×ℝ+\pi:=\{\pi\_{t,x}(\cdot)\}\_{t,x\in[0,T]\times\mathbb{R}\_{+}} is an admissible policy if the following conditions are satisfied:

1. (1)

   For any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R}, πt,x​(u)∈𝒫​(ℝ)\pi\_{t,x}(u)\in\mathcal{P}(\mathbb{R});
2. (2)

   ∫ℝu2​πt,x​(u)​𝑑u≤C1​(1+x2)\int\_{\mathbb{R}}u^{2}\pi\_{t,x}(u)du\leq C\_{1}(1+x^{2}), for any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R};
3. (3)

   |∫ℝu​(πt,x​(u)−πt,y​(u))​𝑑u|2+|∫ℝu2​πt,x​(u)​𝑑u−∫ℝu2​πt,y​(u)​𝑑u|2+∫[0,1]|Gπt,x​(v)−Gπt,y​(v)|2​𝑑v≤C2​|x−y|2\left|\int\_{\mathbb{R}}u(\pi\_{t,x}(u)-\pi\_{t,y}(u))du\right|^{2}+\left|\sqrt{\int\_{\mathbb{R}}u^{2}\pi\_{t,x}(u)du}-\sqrt{\int\_{\mathbb{R}}u^{2}\pi\_{t,y}(u)du}\right|^{2}+\int\_{[0,1]}|G^{\pi\_{t,x}}(v)-G^{\pi\_{t,y}}(v)|^{2}dv\\
   \leq C\_{2}|x-y|^{2}
   , for any t∈[0,T],x,y∈ℝt\in[0,T],x,y\in\mathbb{R};
4. (4)

   ∫ℝπt,x​(u)​|log⁡πt,x​(u)|​𝑑u<C3​(1+|x|2)\int\_{\mathbb{R}}\pi\_{t,x}(u)|\log\pi\_{t,x}(u)|du<C\_{3}(1+|x|^{2}), for any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R};

Here, C1,C2,C3C\_{1},C\_{2},C\_{3} are constants that are independent of tt and xx. The set of all admissible policies is denoted by 𝒜.\mathcal{A}.

We conclude this section with the following lemma, which connects the definition of an admissible policy to the solution of the SDE ([2.8](https://arxiv.org/html/2512.09224v1#S2.E8 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")). The proof is given in Appendix [A.1](https://arxiv.org/html/2512.09224v1#A1.SS1 "A.1 Proof of Lemma 2.1 ‣ Appendix A Proofs ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")

###### Lemma 2.1

Following an admissible policy π∈𝒜\pi\in\mathcal{A}, the exploratory portfolio value process ([2.8](https://arxiv.org/html/2512.09224v1#S2.E8 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) guarantees a unique cádlág adapted solution XπX^{\pi} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T](Xtπ)2]<∞.\mathbb{E}\left[\sup\_{t\in[0,T]}(X\_{t}^{\pi})^{2}\right]<\infty. |  |

## 3 Exploratory Mean-Variance with Jumps Problem

The mean-variance portfolio optimization problem aims to find an investment policy that achieves the highest return and the lowest portfolio volatility.
Since the investment control uu is randomly sampled from the exploratory control π\pi, we consider entropy regularization to encourage exploration within the control space. Denote by H​(π):=−∫ℝπ​(u)​log⁡π​(u)​𝑑uH(\pi):=-\int\_{\mathbb{R}}\pi(u)\log\pi(u)du the entropy of a distribution-valued exploratory policy π\pi.
The objective function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,x;π)=𝔼t,x​[XTπ+λ​∫tTH​(πs)​𝑑s]−γ2​V​a​rt,x​(XTπ)=𝔼t,x​[XTπ−γ2​(XTπ)2+λ​∫tTH​(πs)​𝑑s]+γ2​(𝔼t,x​[XTπ])2,\begin{split}J(t,x;\pi)&=\mathbb{E}\_{t,x}\left[X\_{T}^{\pi}+\lambda\int\_{t}^{T}H(\pi\_{s})ds\right]-\frac{\gamma}{2}Var\_{t,x}(X\_{T}^{\pi})\\ &=\mathbb{E}\_{t,x}\left[X\_{T}^{\pi}-\frac{\gamma}{2}(X\_{T}^{\pi})^{2}+\lambda\int\_{t}^{T}H(\pi\_{s})ds\right]+\frac{\gamma}{2}\left(\mathbb{E}\_{t,x}[X\_{T}^{\pi}]\right)^{2},\end{split} |  | (3.1) |

where λ>0\lambda>0 is the exploration weight and γ>0\gamma>0 is the risk aversion factor.
Additionally, 𝔼t,x​(⋅),V​a​rt,x​(⋅)\mathbb{E}\_{t,x}(\cdot),Var\_{t,x}(\cdot) respectively denote the expectation and variance conditioned on Xtπ=xX\_{t}^{\pi}=x, i.e., 𝔼(⋅|Xtπ=x)\mathbb{E}(\cdot|X\_{t}^{\pi}=x) and Var(⋅|Xtπ=x)Var(\cdot|X\_{t}^{\pi}=x). This means that the expectation is taken under the condition that the portfolio value process XtπX\_{t}^{\pi} starts from xx at time tt, following a given policy π\pi.
Hence, the Exploratory Mean-Variance with Jumps (EMVJ) portfolio optimization problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜J​(t,x;π).\sup\_{\pi\in\mathcal{A}}J(t,x;\pi). |  | (3.2) |

We point out here that following an admissible policy π∈𝒜\pi\in\mathcal{A} as mentioned in Definition [2.1](https://arxiv.org/html/2512.09224v1#S2.Thmdefinition1 "Definition 2.1 (Admissible Policy) ‣ 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") also ensures J​(t,x;π)<∞J(t,x;\pi)<\infty.

###### Remark 3.1

We note that the entropy regularization term in the objective function ([3.1](https://arxiv.org/html/2512.09224v1#S3.E1 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) plays a critical role in two major aspects. First, maximizing the classical mean-variance objective 𝔼t,x​[XTπ]−γ2​V​a​rt,x​(XTπ)\mathbb{E}\_{t,x}[X\_{T}^{\pi}]-\frac{\gamma}{2}Var\_{t,x}(X\_{T}^{\pi}) with an additional entropy term enforces the exploratory policy π\pi to avoid collapsing too quickly to a single deterministic control. This balances exploitation (picking known highly rewarding controls) with exploration (keeping the policy spread out), enabling possible discovery of outperforming controls that used to be unknown to the investor. More practically, the inclusion of an exploration weight λ\lambda also allows us to control the extent to which an investor explores in the control space.
Second, the entropy term acts as a convex regularizer and yields optimal policies that are Boltzmann-like [wang2020reinforcement]. It not only smooths the optimization landscape but also produces stochastic policy distributions (often Gaussian in Linear-Quadratic settings such as under our problem setup) that are easier to learn and evaluate.

The inclusion of the variance term 222Recall that V​a​rt,x​(X)=𝔼t,x​(X2)−(𝔼t,x​(X))2Var\_{t,x}(X)=\mathbb{E}\_{t,x}(X^{2})-(\mathbb{E}\_{t,x}(X))^{2}. in the objective function ([3.1](https://arxiv.org/html/2512.09224v1#S3.E1 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) introduces time-inconsistency, because it implies a nonlinear dependence on the conditional distribution of future wealth, violating Bellman’s principle of optimality [bjork2021time].
When the investor re-optimizes at a later time with updated wealth and conditional expectation, her objective changes because the square of a conditional expectation introduces nonseparability over time.
This leads to preference reversal, meaning that an investor who initially commits to an optimal strategy would deviate from it later in time once the optimization is recomputed. To address this, we can replace the classical notion of optimality with a game-theoretic equilibrium control, also known as a time-consistent equilibrium control, obtained by local (rather than global) optimality with respect to unilateral deviations in infinitesimal time. It is called an “equilibrium” because the investment strategy is characterized as a subgame perfect Nash equilibrium of an intra-personal game between the investor’s present and future selves. In this sense, under the equilibrium control, each future self has no incentive to deviate, though it is generally not globally optimal.
We next introduce a formal definition of an equilibrium investment policy.

###### Definition 3.1

Let π∗∈𝒜\pi^{\ast}\in\mathcal{A} be an admissible investment
policy. For any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R}, consider a perturbed policy πε:={πs,yε​(⋅)}(s,y)∈[t,T]×ℝ\pi^{\varepsilon}:=\{\pi\_{s,y}^{\varepsilon}(\cdot)\}\_{(s,y)\in[t,T]\times\mathbb{R}}, defined as

|  |  |  |
| --- | --- | --- |
|  | πs,yε(u),={υ​(u),(s,y)∈[t,t+ε)×ℝ,πs,y∗​(u),(s,y)∈[t+ε,T]×ℝ,\pi\_{s,y}^{\varepsilon}(u),=\begin{cases}\upsilon(u),&(s,y)\in[t,t+\varepsilon)\times\mathbb{R},\\ \pi\_{s,y}^{\ast}(u),&(s,y)\in[t+\varepsilon,T]\times\mathbb{R},\end{cases} |  |

where ε>0\varepsilon>0, and υ​(⋅)∈𝒫​(ℝ)\upsilon(\cdot)\in\mathcal{P}(\mathbb{R}) is an arbitrary density function satisfying

|  |  |  |
| --- | --- | --- |
|  | ∫ℝu2​υ​(u)​𝑑u​<∞and∫ℝυ​(u)|​log⁡υ​(u)|d​u<∞,\int\_{\mathbb{R}}u^{2}\upsilon(u)du<\infty\quad\text{and}\quad\int\_{\mathbb{R}}\upsilon(u)|\log\upsilon(u)|du<\infty, |  |

which implies πε∈𝒜\pi^{\varepsilon}\in\mathcal{A}. Suppose that for any (t,x)∈[0,T]×ℝ+(t,x)\in[0,T]\times\mathbb{R}\_{+} and any such perturbed strategy πε\pi^{\varepsilon}, we have

|  |  |  |
| --- | --- | --- |
|  | lim supε↓0J​(t,x;πε)−J​(t,x;π∗)ε≤0.\limsup\_{\varepsilon\downarrow 0}\frac{J(t,x;\pi^{\varepsilon})-J(t,x;\pi^{\ast})}{\varepsilon}\leq 0. |  |

Then, π∗\pi^{\ast} is an equilibrium investment policy for
problem ([3.2](https://arxiv.org/html/2512.09224v1#S3.E2 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), and J​(t,x;π∗)J(t,x;\pi^{\ast}) is the corresponding value
function.

Define the infinitesimal generator for ψ​(t,x)∈C1,2​([0,T]×ℝ)\psi(t,x)\in C^{1,2}([0,T]\times\mathbb{R}) with supx{ψx​x​(t,x)}<∞\sup\_{x}\{\psi\_{xx}(t,x)\}<\infty and π∈𝒜\pi\in\mathcal{A} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒπ​ψ​(t,x)\displaystyle\mathcal{L}^{\pi}\psi(t,x) | =∫ℝ[u​(μ−r)​ψx+12​σ2​u2​ψx​x]​πt,x​(u)​𝑑u\displaystyle=\int\_{\mathbb{R}}\left[u(\mu-r)\psi\_{x}+\frac{1}{2}\sigma^{2}u^{2}\psi\_{xx}\right]\pi\_{t,x}(u)du |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫ℝ×[0,1][ψ​(t,x+Gπt,x​(v)​(ez−1))−ψ​(t,x)−Gπt,x​(v)​(ez−1)​ψx]​ν​(d​z)​𝑑v\displaystyle+\int\_{\mathbb{R}\times[0,1]}[\psi(t,x+G^{\pi\_{t,x}}(v)(e^{z}-1))-\psi(t,x)-G^{\pi\_{t,x}}(v)(e^{z}-1)\psi\_{x}]\nu(dz)dv |  | (3.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫ℝ[u​(μ−r)​ψx+12​σ2​u2​ψx​x+∫ℝ[ψ​(t,x+u​(ez−1))−ψ​(t,x)−u​(ez−1)​ψx]​ν​(d​z)]​πt,x​(u)​𝑑u,\displaystyle=\int\_{\mathbb{R}}\left[u(\mu-r)\psi\_{x}+\frac{1}{2}\sigma^{2}u^{2}\psi\_{xx}+\int\_{\mathbb{R}}[\psi(t,x+u(e^{z}-1))-\psi(t,x)-u(e^{z}-1)\psi\_{x}]\nu(dz)\right]\pi\_{t,x}(u)du, |  | (3.4) |

where the last equality is given by the construction of u=Gπt,x​(v)u=G^{\pi\_{t,x}}(v) and thereby the fact that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ×[0,1]f​(t,x,Gπt,x​(v),z)​ν​(d​z)​𝑑v=∫ℝ∫ℝf​(t,x,u,z)​ν​(d​z)​πt,x​(u)​𝑑u,\displaystyle\int\_{\mathbb{R}\times[0,1]}f(t,x,G^{\pi\_{t,x}}(v),z)\nu(dz)dv=\int\_{\mathbb{R}}\int\_{\mathbb{R}}f(t,x,u,z)\nu(dz)\pi\_{t,x}(u)du, |  |

for some function ff.

The next two theorems establish the theoretical core of this paper, which are critical foundations to design the RL algorithms in the subsequent section.

###### Theorem 3.1 (Verification Theorem)

Suppose that there exist two functions V​(t,x)V(t,x) and g​(t,x)∈ℂ1,2​([0,T]×ℝ)g(t,x)\in\mathbb{C}^{1,2}([0,T]\times\mathbb{R}) such that the following conditions are satisfied.

1. (i)

   For any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R},

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supπ∈𝒜{(∂t+ℒπ)​V+λ​H​(π)+γ​gπ​ℒπ​gπ−γ2​ℒπ​(gπ)2}=0.\sup\_{\pi\in\mathcal{A}}\left\{(\partial\_{t}+\mathcal{L}^{\pi})V+\lambda H(\pi)+\gamma g^{\pi}\mathcal{L}^{\pi}g^{\pi}-\frac{\gamma}{2}\mathcal{L}^{\pi}(g^{\pi})^{2}\right\}=0. |  | (3.5) |
2. (ii)

   Let πt,x∗​(u)\pi^{\*}\_{t,x}(u) be the maximizer that achieves the supremum in ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), and suppose it satisfies, for any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R},

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (∂t+ℒπ)​gπ=0.(\partial\_{t}+\mathcal{L}^{\pi})g^{\pi}=0. |  | (3.6) |
3. (iii)

   For any x∈ℝx\in\mathbb{R} and π∈𝒜\pi\in\mathcal{A},

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | V​(T,x)=g​(T,x;π)=x.V(T,x)=g(T,x;\pi)=x. |  | (3.7) |

Then π∗:={πt,x​(⋅)}(t,x)∈[0,T]×ℝ\pi^{\*}:=\{\pi\_{t,x}(\cdot)\}\_{(t,x)\in[0,T]\times\mathbb{R}} is an equilibrium policy for problem ([3.2](https://arxiv.org/html/2512.09224v1#S3.E2 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")). Moreover, we have the corresponding value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)=J​(t,x;π∗),V(t,x)=J(t,x;\pi^{\*}), |  | (3.8) |

and the auxiliary value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | gπ∗​(t,x)≡g​(t,x;π∗):=𝔼t,x​(XTπ∗).g^{\pi^{\*}}(t,x)\equiv g(t,x;\pi^{\*}):=\mathbb{E}\_{t,x}(X\_{T}^{\pi^{\*}}). |  | (3.9) |

###### Theorem 3.2 (Equilibrium Policy and Value Functions)

An equilibrium investment policy for problem ([3.2](https://arxiv.org/html/2512.09224v1#S3.E2 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt,x∗​(u)∼N​(μ−rγ​(σ2+δ2),λγ​(σ2+δ2)),(t,x)∈[0,T]×ℝ\pi^{\*}\_{t,x}(u)\sim N\left(\frac{\mu-r}{\gamma(\sigma^{2}+\delta^{2})},\frac{\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right),(t,x)\in[0,T]\times\mathbb{R} |  | (3.10) |

where δ2=∫ℝ(ez−1)2​ν​(d​z)\delta^{2}=\int\_{\mathbb{R}}(e^{z}-1)^{2}\nu(dz).

The corresponding value function is V​(t,x)=x+C​(t)V(t,x)=x+C(t) and the corresponding auxiliary value function is g​(t,x;π∗)=x+h∗​(t)g(t,x;\pi^{\*})=x+h^{\*}(t), where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C​(t)\displaystyle C(t) | =(T−t)​[(μ−r)22​γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2))],\displaystyle=(T-t)\left[\frac{(\mu-r)^{2}}{2\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\right], |  | (3.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h∗​(t)\displaystyle h^{\*}(t) | =(T−t)​[(μ−r)2γ​(σ2+δ2)].\displaystyle=(T-t)\left[\frac{(\mu-r)^{2}}{\gamma(\sigma^{2}+\delta^{2})}\right]. |  | (3.12) |

The proofs of Theorems [3.1](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem1 "Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and [3.2](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem2 "Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") are given in Appendices [A.2](https://arxiv.org/html/2512.09224v1#A1.SS2 "A.2 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and [A.3](https://arxiv.org/html/2512.09224v1#A1.SS3 "A.3 Proof of Theorem 3.2 ‣ Appendix A Proofs ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") respectively.

## 4 RL Algorithm

In this section, we design an RL algorithm to iteratively learn the equilibrium investment policy without the knowledge of the market and jump dynamics. We leverage the martingale property, in particular the Orthogonality Condition, from the analytical results in Theorems [3.1](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem1 "Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and [3.2](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem2 "Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") to define a loss function, which we use to optimize our RL model.

Recall that the stock price dynamics are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt−=μt​r​u​e​d​t+σt​r​u​e​d​Wt+∫ℝ(ez−1)​N~​(d​t,d​z),\frac{dS\_{t}}{S\_{t-}}=\mu\_{true}dt+\sigma\_{true}dW\_{t}+\int\_{\mathbb{R}}(e^{z}-1)\tilde{N}(dt,dz), |  | (4.1) |

where (μt​r​u​e∈ℝ,σt​r​u​e>0)(\mu\_{true}\in\mathbb{R},\sigma\_{true}>0) are the true mean and volatility of stock returns.
We consider Merton’s jump-diffusion model, which was studied by [gao2024reinforcement] (see also [merton1976option, bates1991crash, das2002surprise]).
The jump density is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν​(d​z)=ζJ,t​r​u​e​12​π​σJ,t​r​u​e2​exp⁡(−(z−μJ,t​r​u​e)22​σJ,t​r​u​e2)​d​z,\nu(dz)=\zeta\_{J,true}\frac{1}{\sqrt{2\pi\sigma\_{J,true}^{2}}}\exp\left(-\frac{(z-\mu\_{J,true})^{2}}{2\sigma\_{J,true}^{2}}\right)dz, |  | (4.2) |

where ζJ,t​r​u​e>0\zeta\_{J,true}>0 is the true arrival rate of jumps per unit time, and (μJ,t​r​u​e∈ℝ,σJ,t​r​u​e>0)(\mu\_{J,true}\in\mathbb{R},\sigma\_{J,true}>0) are the true mean and standard deviation of jump sizes. Most importantly, they are unknown parameters.

Moreover, we note from ([3.10](https://arxiv.org/html/2512.09224v1#S3.E10 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) that the equilibrium investment policy depends on μ,σ\mu,\sigma, and another parameter δ\delta, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt​r​u​e2:=∫ℝ(ez−1)2​ν​(d​z)=ζJ,t​r​u​e​[exp⁡(2​μJ,t​r​u​e+2​σJ,t​r​u​e2)−2​exp⁡(μJ,t​r​u​e+12​σJ,t​r​u​e2)+1].\begin{split}\delta\_{true}^{2}&:=\int\_{\mathbb{R}}(e^{z}-1)^{2}\nu(dz)\\ &=\zeta\_{J,true}\left[\exp(2\mu\_{J,true}+2\sigma^{2}\_{J,true})-2\exp(\mu\_{J,true}+\frac{1}{2}\sigma^{2}\_{J,true})+1\right].\end{split} |  | (4.3) |

We aggregate the jump parameters (ζJ,μJ,σJ)(\zeta\_{J},\mu\_{J},\sigma\_{J}) into δ\delta, and define the parameterization θ:=(μ,σ,δ)\theta:=(\mu,\sigma,\delta). The parameterized policy is πθ:={πt,xθ​(⋅)}(t,x)∈[0,T]×ℝ\pi^{\theta}:=\{\pi^{\theta}\_{t,x}(\cdot)\}\_{(t,x)\in[0,T]\times\mathbb{R}}, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt,xθ​(u)∼N​(μ−rγ​(σ2+δ2),λγ​(σ2+δ2)),(t,x)∈[0,T]×ℝ.\pi^{\theta}\_{t,x}(u)\sim N\left(\frac{\mu-r}{\gamma(\sigma^{2}+\delta^{2})},\frac{\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right),(t,x)\in[0,T]\times\mathbb{R}. |  | (4.4) |

Under πθ\pi^{\theta}, the portfolio value process in ([2.8](https://arxiv.org/html/2512.09224v1#S2.E8 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtθ=(μt​r​u​e−r)​(μ−r)γ​(σ2+δ2)​d​t+σt​r​u​e2​(λγ​(σ2+δ2)+(μ−r)2γ2​(σ2+δ2)2)​d​Wt+(μ−rγ​(σ2+δ2))​∫ℝ(ez−1)​N~​(d​t,d​z).\begin{split}dX\_{t}^{\theta}=&\frac{(\mu\_{true}-r)(\mu-r)}{\gamma(\sigma^{2}+\delta^{2})}dt+\sqrt{\sigma\_{true}^{2}\left(\frac{\lambda}{\gamma(\sigma^{2}+\delta^{2})}+\frac{(\mu-r)^{2}}{\gamma^{2}(\sigma^{2}+\delta^{2})^{2}}\right)}dW\_{t}\\ &+\left(\frac{\mu-r}{\gamma(\sigma^{2}+\delta^{2})}\right)\int\_{\mathbb{R}}(e^{z}-1)\tilde{N}(dt,dz).\end{split} |  | (4.5) |

Inspired by the HJB ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we define, for a parameterized policy πθ∈𝒜\pi^{\theta}\in\mathcal{A}, a stochastic process Mθ:={Mtθ:=M​(t,Xtθ;πθ)}(t,Xtθ)∈[0,T]×ℝM^{\theta}:=\{M\_{t}^{\theta}:=M(t,X\_{t}^{\theta};\pi^{\theta})\}\_{(t,X\_{t}^{\theta})\in[0,T]\times\mathbb{R}} such that ∀(t,x)∈[0,T]×ℝ\forall(t,x)\in[0,T]\times\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mtθ=Vθ​(t,Xtθ)−γ2​(gθ​(t,Xtθ))2+λ​∫0tH​(πsθ)​𝑑s,\begin{split}M\_{t}^{\theta}&=V^{\theta}(t,X\_{t}^{\theta})-\frac{\gamma}{2}(g^{\theta}(t,X\_{t}^{\theta}))^{2}+\lambda\int\_{0}^{t}H(\pi^{\theta}\_{s})ds,\end{split} |  | (4.6) |

where Vθ​(t,x)=x+Cθ​(t)V^{\theta}(t,x)=x+C^{\theta}(t) and gθ​(t,x)=x+hθ​(t)g^{\theta}(t,x)=x+h^{\theta}(t) are the value function and the auxiliary value function corresponding to the parameterized policy πθ\pi^{\theta}, respectively.
Here, CθC^{\theta} and hθh^{\theta} are respectively given by ([3.11](https://arxiv.org/html/2512.09224v1#S3.E11 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and ([3.12](https://arxiv.org/html/2512.09224v1#S3.E12 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), with π\pi replaced by πθ\pi^{\theta}.

###### Theorem 4.1

The process MθM^{\theta} is an ({ℱt}t∈[0,T],ℙ)(\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{P}) martingale when θ=θt​r​u​e:=(μt​r​u​e,σt​r​u​e,δt​r​u​e)\theta=\theta\_{true}:=(\mu\_{true},\sigma\_{true},\delta\_{true}).

The proof of this theorem is postponed to Appendix [A.4](https://arxiv.org/html/2512.09224v1#A1.SS4 "A.4 Proof of Theorem 4.1 ‣ Appendix A Proofs ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").

Additionally, we know that any square-integrable martingale M:={Mt}t∈[0,T]M:=\{M\_{t}\}\_{t\in[0,T]} has an orthogonality condition

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0Tξt​𝑑Mt]=0,\mathbb{E}\left[\int\_{0}^{T}\xi\_{t}dM\_{t}\right]=0, |  |

where the test function ξ:={ξt}t∈[0,T]\xi:=\{\xi\_{t}\}\_{t\in[0,T]} is an
arbitrary {ℱt}t∈[0,T]\{\mathcal{F}\_{t}\}\_{t\in[0,T]}-adapted process that is
square-integrable with respect to MM. This, together with the martingale
property of MθM^{\theta}, allows us to define an Orthogonality Condition (OC) Loss function. Following [PE], we choose the test function
as the partial derivative of the parameterized value function VθV^{\theta}
with respect to its parameters θ\theta.

###### Definition 4.1 (Orthogonality Condition (OC) Loss)

Take θ=(μ,σ,δ)=(θ1,θ2,θ3)\theta=(\mu,\sigma,\delta)=(\theta\_{1},\theta\_{2},\theta\_{3}).
For (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R} and j=1,2,3j=1,2,3, the OC
loss is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | LO​C​(θj)=𝔼t,x​[∫0T∂Vθ∂θj​(t,Xtπθ)​𝑑Mtθ],L\_{OC}(\theta\_{j})=\mathbb{E}\_{t,x}\left[\int\_{0}^{T}\frac{\partial V^{\theta}}{\partial\theta\_{j}}(t,X\_{t}^{\pi^{\theta}})dM\_{t}^{\theta}\right], |  | (4.7) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Vθ∂θ1​(t,x)\displaystyle\frac{\partial V^{\theta}}{\partial\theta\_{1}}(t,x) | =∂Vθ∂μ=(T−t)​[(μ−r)γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2))],\displaystyle=\frac{\partial V^{\theta}}{\partial\mu}=(T-t)\left[\frac{(\mu-r)}{\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\right], |  | (4.8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Vθ∂θ2​(t,x)\displaystyle\frac{\partial V^{\theta}}{\partial\theta\_{2}}(t,x) | =∂Vθ∂σ=−(T−t)​[(μ−r)2​σγ​(σ2+δ2)2+λ​σ(σ2+δ2)],\displaystyle=\frac{\partial V^{\theta}}{\partial\sigma}=-(T-t)\left[\frac{(\mu-r)^{2}\sigma}{\gamma(\sigma^{2}+\delta^{2})^{2}}+\frac{\lambda\sigma}{(\sigma^{2}+\delta^{2})}\right], |  | (4.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Vθ∂θ3​(t,x)\displaystyle\frac{\partial V^{\theta}}{\partial\theta\_{3}}(t,x) | =∂Vθ∂δ=−(T−t)​[(μ−r)2​δγ​(σ2+δ2)2+λ​δ(σ2+δ2)].\displaystyle=\frac{\partial V^{\theta}}{\partial\delta}=-(T-t)\left[\frac{(\mu-r)^{2}\delta}{\gamma(\sigma^{2}+\delta^{2})^{2}}+\frac{\lambda\delta}{(\sigma^{2}+\delta^{2})}\right]. |  | (4.10) |

###### Remark 4.1

The orthogonality condition loss, first introduced by [PE], is built on the fact that under the true value function, the temporal difference residual (obtained from Itô’s formula and the HJB equation) must be a martingale with zero drift, hence orthogonal to every square-integrable test function.
Intuitively, if VθV^{\theta} correctly approximates the true value function, i.e., θ=θt​r​u​e\theta=\theta\_{true}, then no predictable component should remain in the temporal difference residual, resulting in zero conditional expectation.
Note that under our RL setting, the parameterized policy πθ\pi^{\theta} and the corresponding value function VθV^{\theta} share the same parameters, thus the policy optimization and the value function approximation are achieved simultaneously when θ=θt​r​u​e\theta=\theta\_{true}.
Leveraging the equivalence of parameter convergence and the martingale property from Theorem [4.1](https://arxiv.org/html/2512.09224v1#S4.Thmtheorem1 "Theorem 4.1 ‣ 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"),
the orthogonality condition loss enforces effective updates of policy and value functions, by iteratively updating θ\theta and reducing the loss to zero.

Considering a discretization 0=t0<⋯<tN=T0=t\_{0}<\cdots<t\_{N}=T with mesh size Δ​t\Delta t, the discretized loss function becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | LO​C​(θj)=∑n=0N−1∂Vθ∂θj(tn,Xtnπθ){Vθ(tn+1,Xtn+1πθ)−Vθ(tn,Xtnπθ)−γ2[gθ(tn+1,Xtn+1πθ)2−gθ(tn,Xtnπθ)2]+λ2log(2​π​e​λγ​(σ2+δ2))Δt}.\begin{split}L\_{OC}(\theta\_{j})=&\sum\_{n=0}^{N-1}\frac{\partial V^{\theta}}{\partial\theta\_{j}}(t\_{n},X\_{t\_{n}}^{\pi^{\theta}})\Biggl\{V^{\theta}(t\_{n+1},X\_{t\_{n+1}}^{\pi^{\theta}})-V^{\theta}(t\_{n},X\_{t\_{n}}^{\pi^{\theta}})\\ &-\frac{\gamma}{2}\left[g^{\theta}(t\_{n+1},X\_{t\_{n+1}}^{\pi^{\theta}})^{2}-g^{\theta}(t\_{n},X\_{t\_{n}}^{\pi^{\theta}})^{2}\right]+\frac{\lambda}{2}\log\left(\frac{2\pi e\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\Delta t\Biggr\}.\end{split} |  | (4.11) |

We summarize the whole training procedure in Algorithm [1](https://arxiv.org/html/2512.09224v1#algorithm1 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").

Initialize the number of epochs Ne​p​o​c​h​sN\_{epochs}, the investment horizon TT, the mesh size of the continuous time discretization Δ​t\Delta t, the exploration parameter λ>0\lambda>0, the initial portfolio value x0>0x\_{0}>0, the learning rates η=(η1,η2,η3)\eta=(\eta\_{1},\eta\_{2},\eta\_{3}), the “grounding true” market parameters θt​r​u​e=(θt​r​u​e,1,θt​r​u​e,2,θt​r​u​e,3)\theta\_{true}=(\theta\_{true,1},\theta\_{true,2},\theta\_{true,3}) ≡(μt​r​u​e,σt​r​u​e,δt​r​u​e)\equiv(\mu\_{true},\sigma\_{true},\delta\_{true}), and the model parameters θ(0)=(θ1(0),θ2(0),θ3(0))=(μ(0),σ(0),δ(0))\theta^{(0)}=(\theta\_{1}^{(0)},\theta\_{2}^{(0)},\theta\_{3}^{(0)})=(\mu^{(0)},\sigma^{(0)},\delta^{(0)}).

Compute N=TΔ​tN=\frac{T}{\Delta t}.

for *k=0,⋯,Ne​p​o​c​h−1k=0,\cdots,N\_{epoch}-1* do

Fix a realized path of Brownian motion {Wtn(k)}n=0N\{W\_{t\_{n}}^{(k)}\}\_{n=0}^{N}, with Δ​Wtn(k):=Wtn+1(k)−Wtn(k)∼N​(0,Δ​t)\Delta W\_{t\_{n}}^{(k)}:=W^{(k)}\_{t\_{n+1}}-W^{(k)}\_{t\_{n}}\sim N(0,\Delta t).

Sample number of jumps Nk∼P​o​i​s​s​o​n​(ζJ,t​r​u​e​Δ​t)N\_{k}\sim Poisson(\zeta\_{J,true}\Delta t) and sample the jumps (Z1(k),⋯,ZNk(k))​∼i​i​d​N​(μJ,t​r​u​e,σJ,t​r​u​e2)(Z\_{1}^{(k)},\cdots,Z\_{N\_{k}}^{(k)})\overset{iid}{\sim}N(\mu\_{J,true},\sigma\_{J,true}^{2}).

Simulate {Xtn(k)}n=0N\{X^{(k)}\_{t\_{n}}\}\_{n=0}^{N} via ([4.5](https://arxiv.org/html/2512.09224v1#S4.E5 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), with (μ,σ,δ)(\mu,\sigma,\delta) replaced by (μ(k),σ(k),δ(k))(\mu^{(k)},\sigma^{(k)},\delta^{(k)}), {Wtn}n=0N\{W\_{t\_{n}}\}\_{n=0}^{N} replaced by {Wtn(k)}n=0N\{W\_{t\_{n}}^{(k)}\}\_{n=0}^{N}, and the integral replaced by ∑j=1Nk(eZj(k)−1)\sum\_{j=1}^{N\_{k}}(e^{Z\_{j}^{(k)}}-1).

Compute {∂Vθ(k)∂μ​(tn,Xtn(k))}n=0N\{\frac{\partial V^{\theta^{(k)}}}{\partial\mu}(t\_{n},X\_{t\_{n}}^{(k)})\}\_{n=0}^{N}, {∂Vθ(k)∂σ​(tn,Xtn(k))}n=0N\{\frac{\partial V^{\theta^{(k)}}}{\partial\sigma}(t\_{n},X\_{t\_{n}}^{(k)})\}\_{n=0}^{N} and {∂Vθ(k)∂δ​(tn,Xtn(k))}n=0N\{\frac{\partial V^{\theta^{(k)}}}{\partial\delta}(t\_{n},X\_{t\_{n}}^{(k)})\}\_{n=0}^{N} via ([4.8](https://arxiv.org/html/2512.09224v1#S4.E8 "In Definition 4.1 (Orthogonality Condition (OC) Loss) ‣ 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), ([4.9](https://arxiv.org/html/2512.09224v1#S4.E9 "In Definition 4.1 (Orthogonality Condition (OC) Loss) ‣ 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and ([4.10](https://arxiv.org/html/2512.09224v1#S4.E10 "In Definition 4.1 (Orthogonality Condition (OC) Loss) ‣ 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), with (μ,σ,δ)(\mu,\sigma,\delta) replaced by (μ(k),σ(k),δ(k))(\mu^{(k)},\sigma^{(k)},\delta^{(k)}).

for *j=1,2,3j=1,2,3* do

Compute L​(θj(k)):=Lo​c​(θj(k);{Xtn(k)}n=0N)L(\theta\_{j}^{(k)}):=L\_{oc}(\theta\_{j}^{(k)};\{X\_{t\_{n}}^{(k)}\}\_{n=0}^{N}) via ([4.11](https://arxiv.org/html/2512.09224v1#S4.E11 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")).

Update θj(k+1)←θj(k)+ηj×L​(θj(k))\theta\_{j}^{(k+1)}\leftarrow\theta\_{j}^{(k)}+\eta\_{j}\times L(\theta\_{j}^{(k)})

end for

end for

Algorithm 1 Training with Orthogonality Condition Loss

## 5 Numerical Results

In this section, we train and evaluate our model on simulated data and real market data. On simulated data (Subsection [5.1](https://arxiv.org/html/2512.09224v1#S5.SS1 "5.1 Analysis On Simulated Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we train our model and show that the model parameters converge to the corresponding true values. Moreover, the investment performance (in terms of mean terminal portfolio value) on the simulated data is close to the theoretical expectation. We also examine our model on real market data (Subsection [5.2](https://arxiv.org/html/2512.09224v1#S5.SS2 "5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), which illustrates the potential profitability of our equilibrium policy.

### 5.1 Analysis On Simulated Market Data

From [Yahoo Finance](https://finance.yahoo.com/quote/%5ESP500TR/), we collect the S&P500 market index (total return) as a “representative” stock at a daily frequency, ranging from January 1st of 2000 to December 31st of 2023.
We fit Merton’s jump-diffusion model, parameterized by both the market parameters (μ,σ)(\mu,\sigma) and the jump parameters (μJ,σJ,ζJ)(\mu\_{J},\sigma\_{J},\zeta\_{J}).
Denote by θ:=(μ,σ,μJ,σJ,ζJ)\theta:=(\mu,\sigma,\mu\_{J},\sigma\_{J},\zeta\_{J}). Consider a time discretization 0=t0<⋯<tN=T0=t\_{0}<\cdots<t\_{N}=T with mesh size Δ​t\Delta t. When Δ​t\Delta t is small, we suppose the log-returns Ri:=log⁡(StiSti−1)R\_{i}:=\log\left(\frac{S\_{t\_{i}}}{S\_{t\_{i-1}}}\right), for i=1,⋯,TΔ​ti=1,\cdots,\frac{T}{\Delta t}, are approximately independently and identically distributed with density function

|  |  |  |
| --- | --- | --- |
|  | f​(r;θ)=∑m=0∞pm​(ζJ,Δ​t)⋅ϕ​(r;νm​(θ,Δ​t),τm2​(θ,Δ​t)),f(r;\theta)=\sum\_{m=0}^{\infty}p\_{m}(\zeta\_{J},\Delta t)\cdot\phi(r;\nu\_{m}(\theta,\Delta t),\tau^{2}\_{m}(\theta,\Delta t)), |  |

where pm​(ζJ,Δ​t)=e−ζJ​Δ​t​(ζJ​Δ​t)mm!p\_{m}(\zeta\_{J},\Delta t)=\frac{e^{-\zeta\_{J}\Delta t}(\zeta\_{J}\Delta t)^{m}}{m!} is the Poisson probability of mm jumps, ϕ​(⋅;ν,τ2)\phi(\cdot;\nu,\tau^{2}) is the Gaussian density with mean ν\nu and variance τ2\tau^{2}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | νm​(θ,Δ​t)\displaystyle\nu\_{m}(\theta,\Delta t) | =(μ−12​σ2−λ​(eμJ+12​σJ2−1))​Δ​t+m​μJ\displaystyle=\left(\mu-\frac{1}{2}\sigma^{2}-\lambda(e^{\mu\_{J}+\frac{1}{2}\sigma\_{J}^{2}}-1)\right)\Delta t+m\mu\_{J} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | τm2​(θ,Δ​t)\displaystyle\tau^{2}\_{m}(\theta,\Delta t) | =σ2​Δ​t+μ​σJ2.\displaystyle=\sigma^{2}\Delta t+\mu\sigma\_{J}^{2}. |  |

While the direct computation of an infinite sum f​(r,θ)f(r,\theta) is impractical, we approximate it with a truncated sum up to m=2. Because multiple jumps per interval are very rare and pm​(ζJ,Δ​t)p\_{m}(\zeta\_{J},\Delta t) for m>2m>2 are negligible.
We calculate the likelihood function as L​(θ;R)=∏i=1T/Δ​tf​(Ri;θ)L(\theta;R)=\prod\_{i=1}^{T/\Delta t}f(R\_{i};\theta) and apply the Nelder-Mead method [nelder1965simplex] to obtain the maximum likelihood estimates (MLE) of θ\theta. We choose the MLEs of θ\theta as the “grounding true” parameter values (μt​r​u​e,σt​r​u​e,ζJ,t​r​u​e,μJ,t​r​u​e,σJ,t​r​u​e)(\mu\_{true},\sigma\_{true},\zeta\_{J,true},\mu\_{J,true},\sigma\_{J,true}) for simulation.
In this way, our simulated data reflects the real market.

We consider a one-year investment horizon (T=1)(T=1) with daily rebalancing (Δ​t=1252)(\Delta t=\frac{1}{252}), reflecting an assumption of 252 trading days per year. The investor starts with an initial wealth of x0=1x\_{0}=1, and invests in the stock following the equilibrium policy ([3.10](https://arxiv.org/html/2512.09224v1#S3.E10 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) with initial parametrization (μ0,σ0,δ0)=(0.1,0.1,0.05)(\mu\_{0},\sigma\_{0},\delta\_{0})=(0.1,0.1,0.05).
For simplicity, we suppose there is no cost of borrowing, i.e., the risk free rate r=0r=0. The exploration weight λ\lambda and the risk aversion parameter γ\gamma are set as 11 for training.
We summarize all the parameters in Table [1](https://arxiv.org/html/2512.09224v1#S5.T1 "Table 1 ‣ 5.1 Analysis On Simulated Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").

| Parameters | Values |
| --- | --- |
| x0x\_{0} | 1 |
| (T,Δt)T,\Delta t) | (1,1252)(1,\frac{1}{252}) |
| λ\lambda | 1 |
| γ\gamma | 1 |
| rr | 0.01 |
| (μt​r​u​e,σt​r​u​e)(\mu\_{true},\sigma\_{true}) | (0.0878, 0.1321) |
| ζJ,t​r​u​e\zeta\_{J,true} | 27.6813 |
| (μJ,t​r​u​e,σJ,t​r​u​e)(\mu\_{J,true},\sigma\_{J,true}) | (-0.0040, 0.0274) |
| δt​r​u​e\delta\_{true} (by ([4.3](https://arxiv.org/html/2512.09224v1#S4.E3 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"))) | 0.1449 |
| δ0\delta\_{0} | 0.05 |
| (μ0,σ0)(\mu\_{0},\sigma\_{0}) | (0.1, 0.1) |

Table 1: Parameters for training and evaluation on simulated data.

We train the model following Algorithm [1](https://arxiv.org/html/2512.09224v1#algorithm1 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and all the model parameters converge to their “grounding true” values in 550 epochs as shown in Figure [1](https://arxiv.org/html/2512.09224v1#S5.F1 "Figure 1 ‣ 5.1 Analysis On Simulated Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").
This indicates that our model has been optimized to the equilibrium policy.
We make a note here that the three parameters do not converge at the same rate — in the case showed in Figure [1](https://arxiv.org/html/2512.09224v1#S5.F1 "Figure 1 ‣ 5.1 Analysis On Simulated Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), μ\mu converges fastest while σ\sigma converges slowest 333The speed of parameter convergence depends on how close the initial points are to the corresponding true values..
In the training process, we impose a linear learning rate scheduler to control the learning rates for each parameter.

![Refer to caption](figs/convergence/param_convergence_ckpt3_2_bw.png)


Figure 1: Convergence of μ\mu (left), σ\sigma (middle) and δ\delta (right).

Next, we check if our trained model is able to achieve the theoretically expected investment performance. From Theorem [3.2](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem2 "Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), we know that if an investor follows a policy π∗\pi^{\*}, the expected terminal portfolio value is

|  |  |  |
| --- | --- | --- |
|  | 𝔼0,x0​(XTπ∗)=g​(t,x;π∗)=x0+hπ∗​(t)=x0+(T−t)​[(μ−r)2γ​(σ2+δ2)].\begin{split}\mathbb{E}\_{0,x\_{0}}(X\_{T}^{\pi^{\*}})&=g(t,x;\pi^{\*})=x\_{0}+h^{\pi^{\*}}(t)\\ &=x\_{0}+(T-t)\left[\frac{(\mu-r)^{2}}{\gamma(\sigma^{2}+\delta^{2})}\right].\end{split} |  |

We suppose the investor follows the mean of the equilibrium policy ([3.10](https://arxiv.org/html/2512.09224v1#S3.E10 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), that is, at each time tt, she invests ut=μγ​(σ2+δ2)u\_{t}=\frac{\mu}{\gamma(\sigma^{2}+\delta^{2})} dollars in the stock, and saves the remaining Xt−utX\_{t}-u\_{t} in cash at the risk-free interest rate rr.
If ut>Xtu\_{t}>X\_{t}, this means the investor is investing with leverage, and the cost of borrowing is equal to the risk-free interest rate rr.
If ut<0u\_{t}<0, this means the investor is short-selling the stock, and saving the premium at the risk-free interest rate rr.
We highlight that investing at our policy mean is an extension to the equilibrium policy considered in [bjork2021time], as they coincide with each other when there are no jumps in the market dynamics.
While we train the model with risk aversion parameter γ=1\gamma=1, we examine the investment performance for investors with different risk appetites, γ∈[0.1,0.5,1,2,5]\gamma\in[0.1,0.5,1,2,5]. Higher γ\gamma values represent more risk averse investors, hence holding a smaller long or short position in the stock.
For each investor, we simulate 100 stock price trajectories and make investments repeatedly. As a result, we get 100 portfolio value trajectories. The realized mean and realized volatility of the terminal portfolio value are calculated as the average and the standard deviation of the last entry over the 100 portfolio value trajectories. We also compute and contrast the empirical objective function, Je​m​p​i​r​i​c​a​lJ\_{empirical} using ([3.1](https://arxiv.org/html/2512.09224v1#S3.E1 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) with λ=0\lambda=0 444Because we are following the mean of the equilibrium policy, there is no policy exploration.,
and the theoretical value of the objective function VV given the equilibrium policy, using the value function in Theorem [3.2](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem2 "Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")).

We summarize the investment performance in Table [1](https://arxiv.org/html/2512.09224v1#S5.T1 "Table 1 ‣ 5.1 Analysis On Simulated Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). For the realized mean, realized volatility and Je​m​p​i​r​i​c​a​lJ\_{empirical}, we also compute the Monte Carlo standard errors following the metrics in [morris2019using], which are reported in the parenthesis in Table [1](https://arxiv.org/html/2512.09224v1#S5.T1 "Table 1 ‣ 5.1 Analysis On Simulated Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").
The realized mean terminal portfolio values are pretty close to the corresponding theoretical means. The realized volatility diminishes as the investor becomes more risk averse (i.e., as γ\gamma increases), which is practically meaningful as more aggressive investment results in higher volatility. The empirical objective function values are reasonably close to the theoretical values, and the gap narrows as the investor becomes more risk averse.

| γ\gamma | realized mean | theoretical mean | realized volatility | Je​m​p​i​r​i​c​a​lJ\_{empirical} | theoretical VV |
| --- | --- | --- | --- | --- | --- |
| 0.1 | 2.9980 (0.3032) | 3.0213 | 3.0316 (0.2154) | 2.5384 (0.3055) | 2.0106 |
| 0.5 | 1.3996 (0.0606) | 1.4043 | 0.6063 (0.0431) | 1.3077 (0.0611) | 1.2021 |
| 1 | 1.1998 (0.0303) | 1.2021 | 0.3032 (0.0215) | 1.1538 (0.0305) | 1.1011 |
| 2 | 1.0999 (0.0152) | 1.1011 | 0.1516 (0.0108) | 1.0770 (0.0153) | 1.0505 |
| 5 | 1.0400 (0.0061) | 1.0404 | 0.0606 (0.0043) | 1.0308 (0.0061) | 1.0202 |

Table 2: Investment performance on simulated market data. The Monte Carlo standard errors of the realized means, realized volatilities and Je​m​p​i​r​i​c​a​lJ\_{empirical} are reported in the parenthesis.

### 5.2 Analysis on Real Market Data

To evaluate our model on real market data, we choose the S&P500 market index mentioned in the last subsection as the risky asset. We also collect the US 3-month Treasure Bill (3mTBill) from [Yahoo Finance](https://finance.yahoo.com/quote/%5EIRX/) as the risk free interest rate. The frequency of the 3mTBill data is daily and the range is from January 1st, 2000 to December 31st, 2023, which matches the S&P500 data.

For model training, we divide the investment horizon of 24 years, from 2000 to 2023, into 14 eleven-year rolling windows, 2000-2010, 2001-2011, ⋯\cdots, 2013-2023.
Each rolling window spans from the first day of the starting year to the last day of the ending year, e.g., window 2000-2010 covers the period from January 1st, 2000 to December 31st, 2010. The first 10 years of each window is the training period and the final year is the evaluation period.
We suppose an investor is risk averse with γ=5\gamma=5.
In the training phase, we set λ=5\lambda=5 to encourage exploration within the control space. Over each rolling window, we fit a jump-diffusion model on the training period and use the MLEs as the initial parameters of the RL model. We evaluate the model performance on the evaluation period of each rolling window.

The investment performances on the training periods and the evaluation periods are given in Tables [3](https://arxiv.org/html/2512.09224v1#S5.T3 "Table 3 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and [4](https://arxiv.org/html/2512.09224v1#S5.T4 "Table 4 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), respectively, including the terminal portfolio value means, volatilities and Sharpe Ratios (SR).
Over each training or evaluation period, we simultaneously create 100 self-financing portfolios each with initial value of x0=1x\_{0}=1. We rebalance the portfolios on a daily basis according to the stock and risk-free interest rate dynamics, following the equilibrium policy ([3.10](https://arxiv.org/html/2512.09224v1#S3.E10 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")). To reduce the portfolio volatility, we set λ=0.01\lambda=0.01 if we invest over the training periods and set λ=0.1\lambda=0.1 if we invest over the evaluation periods. The mean and the volatility columns are calculated as the average and standard deviation of the 100 portfolios’ values on the last day of the investment period. The Monte Carlo standard errors are reported in the parenthesis, following the metrics provided in [morris2019using]. The risk-free column values are the terminal values if we hold the risk-free asset throughout the investment period.

| window | mean | volatility | risk-free |
| --- | --- | --- | --- |
| 2000-2010 | 1.3980 (0.0198) | 0.1978 (0.0141) | 1.3071 |
| 2001-2011 | 1.3859 (0.0202) | 0.2022 (0.0144) | 1.2348 |
| 2002-2012 | 1.3845 (0.0185) | 0.1848 (0.0131) | 1.1944 |
| 2003-2013 | 1.8165 (0.0201) | 0.2007 (0.0143) | 1.1766 |
| 2004-2014 | 1.8445 (0.0187) | 0.1869 (0.0133) | 1.1654 |
| 2005-2015 | 1.9569 (0.0140) | 0.1397 (0.0099) | 1.1499 |
| 2006-2016 | 1.5993 (0.0150) | 0.1500 (0.0107) | 1.1148 |
| 2007-2017 | 1.5213 (0.0154) | 0.1535 (0.0109) | 1.0667 |
| 2008-2018 | 1.6454 (0.0146) | 0.1463 (0.0104) | 1.0311 |
| 2009-2019 | 3.6082 (0.0207) | 0.2066 (0.0147) | 1.0370 |
| 2010-2020 | 4.9670 (0.0195) | 0.1945 (0.0138) | 1.0570 |
| 2011-2021 | 5.5411 (0.0272) | 0.2720 (0.0193) | 1.0592 |
| 2012-2022 | 7.4664 (0.0231) | 0.2311 (0.0164) | 1.0591 |
| 2013-2023 | 5.2763 (0.0225) | 0.2246 (0.0160) | 1.0795 |

Table 3: Investment performance on training periods. The model was trained with (λ,γ)=(5,5)(\lambda,\gamma)=(5,5) and the table is calculated with (λ,γ)=(0.01,5)(\lambda,\gamma)=(0.01,5). The Monte Carlo standard errors of the portfolio value means and volatilities are reported in the parenthesis.

Clearly, Table [3](https://arxiv.org/html/2512.09224v1#S5.T3 "Table 3 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") shows that all the portfolios invested over the training periods achieve higher mean returns than the risk-free return, with reasonably low volatility.
The mean terminal portfolio values are very high during the post subprime crisis in 2008 — the portfolio value triples in 2009-2019 and even grows sevenfold in 2012-2022, in spite of the breakout of COVID since 2020.
Even in the training periods that are close to or cover the subprime crisis, the training performance is still reliable, as the mean terminal portfolio value grows at least by around 50% in 2004-2014, 2005-2015, 2006-2016, 2007-2017 and 2008-2018.
This implies that our models are well-trained and the market parameters of the training periods are properly learned through the training process.

Table [4](https://arxiv.org/html/2512.09224v1#S5.T4 "Table 4 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") conveys the generalizability and practical applicability of our model. In 12 out of the 14 evaluation periods, the mean terminal portfolio values are higher than the risk-free portfolio, with reasonably low volatility.
The only two exceptions are in 2018 and 2022, during which the market trend flips, as shown in Figure [2](https://arxiv.org/html/2512.09224v1#S5.F2 "Figure 2 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). That is, the market trend of the training period (2008-2017 and 2012-2021) is opposite to that of the evaluation period (2018 and 2022, respectively). So, the model is mislead by the training period. For example, in the window 2012-2022, the model is trained over a bullish period of 2012-2021 and it will assume the market to continue growing in 2022, which is not the case due to the breakout of COVID. As a result, the model decides to hold a long position in the stock during a bearish evaluation period in 2022.
However, in the windows 2009-2019 and 2013-2023, our model takes the years of 2018 and 2022 as part of the training periods and adjusts the investment strategies, leading to an improved performance in the evaluation periods in 2019 and 2023.
This implies that our model is robust against different market conditions, as long as the market does not significantly violate the model assumptions. Moreover, our model preserves the potential of reversing the adverse performance, by gradually digesting the market dynamics and adjusting the investment strategies accordingly.

For purposes of comparison, we also present the investment performance using the MLEs of a fitted Merton jump-diffusion model as the parameters of the equilibrium investment policy. We use the subscript M​L​EMLE to denote the investment performances using MLEs in Table [4](https://arxiv.org/html/2512.09224v1#S5.T4 "Table 4 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). Except for 2018 and 2022, our model achieves higher Sharpe Ratios in all other evaluation periods, compared to the investment strategy using MLEs. Since our model takes the MLEs as the initial parameters in the training phase, the improved investment performance demonstrates the effectiveness of our algorithm. In the years 2018 and 2022, the investments using MLEs also obtain negative Sharpe Ratios, which provides a poor starting point for us to train the model. This partially explains why our model performance in 2018 and 2022 is poor.

| year | mean | volatility | SR | risk-free | m​e​a​nM​L​Emean\_{MLE} | v​o​l​a​t​i​l​i​t​yM​L​Evolatility\_{MLE} | S​RM​L​ESR\_{MLE} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2010 | 1.0666 (0.0173) | 0.1726 (0.0123) | 0.3784 | 1.0013 | 1.0189 (0.0121) | 0.1214 (0.0086) | 0.1452 |
| 2011 | 1.0227 (0.0186) | 0.1863 (0.0132) | 0.1197 | 1.0004 | 1.0067 (0.0129) | 0.1292 (0.0092) | 0.0487 |
| 2012 | 1.0621 (0.0105) | 0.1054 (0.0075) | 0.5820 | 1.0008 | 1.0226 (0.0081) | 0.0813 (0.0058) | 0.2677 |
| 2013 | 1.2297 (0.0101) | 0.1006 (0.0071) | 2.2791 | 1.0005 | 1.1121 (0.0077) | 0.0774 (0.0055) | 1.4414 |
| 2014 | 1.2132 (0.0124) | 0.1244 (0.0088) | 1.7127 | 1.0002 | 1.0481 (0.0077) | 0.0773 (0.0055) | 0.6187 |
| 2015 | 1.0372 (0.0170) | 0.1696 (0.0121) | 0.2171 | 1.0004 | 1.0095 (0.0108) | 0.1083 (0.0077) | 0.0837 |
| 2016 | 1.0625 (0.0099) | 0.0985 (0.0070) | 0.6029 | 1.0030 | 1.0457 (0.0089) | 0.0894 (0.0064) | 0.4773 |
| 2017 | 1.0880 (0.0043) | 0.0427 (0.0030) | 1.8451 | 1.0093 | 1.0752 (0.0040) | 0.0404 (0.0029) | 1.6309 |
| 2018 | 0.9975 (0.0141) | 0.1412 (0.0100) | -0.1548 | 1.0194 | 1.0098 (0.0118) | 0.1184 (0.0084) | -0.0814 |
| 2019 | 1.4672 (0.0138) | 0.1384 (0.0098) | 3.2274 | 1.0206 | 1.2435 (0.0107) | 0.1069 (0.0076) | 2.0840 |
| 2020 | 1.6298 (0.0476) | 0.4761 (0.0338) | 1.3158 | 1.0034 | 1.2601 (0.0345) | 0.3449 (0.0245) | 0.7445 |
| 2021 | 1.8431 (0.0173) | 0.1726 (0.0123) | 4.8834 | 1.0003 | 1.2414 (0.0108) | 0.1075 (0.0076) | 2.2434 |
| 2022 | 0.2339 (0.0356) | 0.3555 (0.0252) | -2.2119 | 1.0202 | 0.7706 (0.0225) | 0.2246 (0.0160) | -1.1109 |
| 2023 | 1.5263 (0.0201) | 0.2063 (0.0147) | 2.3002 | 1.0517 | 1.1563 (0.0124) | 0.1239 (0.0088) | 0.8440 |

Table 4: Investment performance on evaluation periods. The model was trained with (λ,γ)=(5,5)(\lambda,\gamma)=(5,5) and the table is calculated with (λ,γ)=(0.1,5)(\lambda,\gamma)=(0.1,5). SR denotes the Sharpe Ratio, and the subscript M​L​EMLE denotes the investment performance calculated using MLEs of a Merton’s jump-diffusion model. The Monte Carlo standard errors of the portfolio value means and volatilities are reported in the parenthesis.

Finally, we also consider a more conservative investor with λ=1\lambda=1. After retraining and retesting the model, we improve the investment performance in 2018, as shown in Table [5](https://arxiv.org/html/2512.09224v1#S5.T5 "Table 5 ‣ 5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). This reiterates our model’s robustness against violation of model assumptions in the real-world market.

| year | mean | volatility | SR |
| --- | --- | --- | --- |
| 2018 | 1.0598 (0.0151) | 0.1507 (0.0107) | 0.2679 |

Table 5: Investment performance in 2018. The model was retrained with (λ,γ)=(1,5)(\lambda,\gamma)=(1,5) and the table is calculated with (λ,γ)=(0.01,5)(\lambda,\gamma)=(0.01,5). SR denotes the Sharpe Ratio. The Monte Carlo standard errors of the portfolio value mean and volatility are reported in the parenthesis.

![Refer to caption](figs/SP500_1.png)


Figure 2: S&P500 market index. The period between the dotted vertical lines is the year 2018 and the period between the dashed vertical lines is the year 2022. The market was significantly shocked due to the crash of [cryptocurrency bubble](https://en.wikipedia.org/wiki/Cryptocurrency_bubble#2017_boom_and_2018_crash) in 2018, as well as the post-COVID historical [global interest rate hike](https://www.reuters.com/markets/global-central-banks-deliver-historic-rate-hike-blast-2022-2022-12-23/) and the escalation in [the Russo-Ukrainian war](https://en.wikipedia.org/wiki/Russo-Ukrainian_war_(2022%E2%80%93present)) in 2022.

## 6 Conclusion

In this paper, we apply the time-inconsistent control (TIC) approach to a RL-facilitated exploratory Mean-Variance problem with jump-diffusion market dynamics. Unlike many past works which choose to solve the Lagrangian dual of the MV problem [wang2020continuous, gao2024reinforcement, wu2024reinforcement, chen2025EMVRS, gao2024reinforcement], we tackle the time-inconsistency of the MV problem following the methods introduced in [bjork2021time]. We acknowledge that the uniqueness of an equilibrium solution to a TIC problem remains as an open research topic, as discussed in [dai2023learning]. Therefore, we disregard the uniqueness argument of our solution, and decide to present one solution by establishing and solving the extended HJB equations. We present a verification theorem (Theorem [3.1](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem1 "Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) that ensures our solution is an equilibrium solution, according to Definition [3.1](https://arxiv.org/html/2512.09224v1#S3.Thmdefinition1 "Definition 3.1 ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach").

Furthermore, we choose the RL model parameterization that is practically meaningful, based on our analytical solutions in Theorem [3.2](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem2 "Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). We then leverage the martingale property, specifically the orthogonality condition, to define the Orthogonality Condition (OC) loss function, which is more effective in our problem context compared to another widely-applied Temporal-Difference (TD) loss in RL, as discussed in [PE, chen2025EMVRS]. With our choice of parameterization and loss function, we are able to check whether parameters can converge to the corresponding true values.
Thankfully, all parameters converge correctly in our simulation study, indicating that our RL algorithm is effective to learn the equilibrium policy for jump-diffusion market dynamics.

On real market data, we examine our model over a course of 24 years since 2000. Our model performs well on all the training periods and is profitable in 13 out of 14 evaluation periods, with reasonably low volatility. We acknowledge that our model can be mislead if the market significantly violates the model assumptions.

We conclude this paper with two potential directions for future work.

* (i)

  Bayesian approach to learn the model parameters. We acknowledge the possibility of learning our model parameters via a Bayesian approach, since our model parameters all have practical meanings and the number of parameters is small. One potential way is to apply a filtering method [fulop2011filtering] to iteratively learn the posterior distributions of each model parameter. The stochasticity of the exploratory control thereby has two sources, one from the distribution-valued policy and the other from the posterior distribution of the model parameters.

  Besides, one can also employ Bayesian RL [vlassis2012bayesian, ghavamzadeh2015bayesian] techniques to learn the posterior distribution of the model parameters, instead of learning a single estimate as in the classical RL approaches.
* (ii)

  Extension to a regime-switching market. Past work has considered portfolio optimization in a regime-switching and jump-diffusion market [savku2022stochastic, zhang2021optimal, zhang2022portfolio, gal2005dynamic]. However, to the best of our knowledge, an exploratory formulation of this problem remains untouched.

  As we discussed in Section [5.2](https://arxiv.org/html/2512.09224v1#S5.SS2 "5.2 Analysis on Real Market Data ‣ 5 Numerical Results ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), our model can perform poorly if the market trend in a training period is opposite to that in an evaluating period. Such a trend-flipping phenomenon can potentially be explained by a shift of market regimes. [chen2025EMVRS] solved an exploratory MV problem in a regime-switching market, although their problem setting excludes jumps and they took a time-consistent approach.

## Appendix A Proofs

### A.1 Proof of Lemma [2.1](https://arxiv.org/html/2512.09224v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")

Suppose π∈𝒜\pi\in\mathcal{A}. By the fact that V​a​r​(U)=E​[U2]−(E​[U])2≥0Var(U)=E[U^{2}]-(E[U])^{2}\geq 0 for U∼πU\sim\pi,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝu2​πt,x​(u)​𝑑u≥(∫ℝu​πt,x​(u)​𝑑u)2.\displaystyle\int\_{\mathbb{R}}u^{2}\pi\_{t,x}(u)du\geq\left(\int\_{\mathbb{R}}u\pi\_{t,x}(u)du\right)^{2}. |  |

Furthermore, because u=Gπt,x​(v)u=G^{\pi\_{t,x}}(v) for (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R} and hence d​v=πt,x​(u)​d​udv=\pi\_{t,x}(u)du, we have

|  |  |  |
| --- | --- | --- |
|  | ∫01|Gπt,x​(v)|2​𝑑v=∫ℝu2​πt,x​(u)​𝑑v.\displaystyle\int\_{0}^{1}|G^{\pi\_{t,x}}(v)|^{2}dv=\int\_{\mathbb{R}}u^{2}\pi\_{t,x}(u)dv. |  |

Then, by (2) of Definition [2.1](https://arxiv.org/html/2512.09224v1#S2.Thmdefinition1 "Definition 2.1 (Admissible Policy) ‣ 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach") and the conditions on the Lévy measure ([2.4](https://arxiv.org/html/2512.09224v1#S2.E4 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we know there exists a constant C4C\_{4} such that

|  |  |  |
| --- | --- | --- |
|  | (∫ℝu​πt,x​(u)​𝑑u)2≤C4​(1+x2)\displaystyle\left(\int\_{\mathbb{R}}u\pi\_{t,x}(u)du\right)^{2}\leq C\_{4}(1+x^{2}) |  |
|  |  |  |
| --- | --- | --- |
|  | ∫ℝ×[0,1]|Gπt,x​(v)​(ez−1)|2​ν​(d​z)​𝑑v=(∫ℝ(ez−1)2​ν​(d​z))×(∫01|Gπt,x​(v)|2​𝑑v)≤C4​(1+x2)\displaystyle\int\_{\mathbb{R}\times[0,1]}|G^{\pi\_{t,x}}(v)(e^{z}-1)|^{2}\nu(dz)dv=\left(\int\_{\mathbb{R}}(e^{z}-1)^{2}\nu(dz)\right)\times\left(\int\_{0}^{1}|G^{\pi\_{t,x}}(v)|^{2}dv\right)\leq C\_{4}(1+x^{2}) |  |

for any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R}.
Therefore, there exists C′:=max⁡(C​1,2​C​4)C^{\prime}:=\max(C1,2C4) such that

|  |  |  |
| --- | --- | --- |
|  | (∫ℝu​πt,x​(u)​𝑑u)2+∫ℝu2​πt,x​(u)​𝑑u+∫ℝ×[0,1]|Gπt,x​(v)​(ez−1)|2​ν​(d​z)​𝑑u≤C′​(1+x2),\left(\int\_{\mathbb{R}}u\pi\_{t,x}(u)du\right)^{2}+\int\_{\mathbb{R}}u^{2}\pi\_{t,x}(u)du+\int\_{\mathbb{R}\times[0,1]}|G^{\pi\_{t,x}}(v)(e^{z}-1)|^{2}\nu(dz)du\leq C^{\prime}(1+x^{2}), |  |

for any (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R}. Hence, the drift, diffusion and jump components of the SDE ([2.8](https://arxiv.org/html/2512.09224v1#S2.E8 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) have at most linear growth. Furthermore, by (3) of Definition [2.1](https://arxiv.org/html/2512.09224v1#S2.Thmdefinition1 "Definition 2.1 (Admissible Policy) ‣ 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), the drift, diffusion and jump components of the SDE ([2.8](https://arxiv.org/html/2512.09224v1#S2.E8 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) are also Lipschitz continuous. According to [oksendal2005applied], there exists a unique cádlág adapted solution XπX^{\pi} to the SDE ([2.8](https://arxiv.org/html/2512.09224v1#S2.E8 "In 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T](Xtπ)2]<∞.\mathbb{E}\left[\sup\_{t\in[0,T]}(X\_{t}^{\pi})^{2}\right]<\infty. |  |

### A.2 Proof of Theorem [3.1](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem1 "Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")

First, by Itô’s formula, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x​[g​(T,XTπ∗)]=g​(t,x)+𝔼t,x​[∫tT(∂t+ℒπ)​g​(s,Xsπ∗)​𝑑s].\mathbb{E}\_{t,x}[g(T,X\_{T}^{\pi^{\*}})]=g(t,x)+\mathbb{E}\_{t,x}\left[\int\_{t}^{T}(\partial\_{t}+\mathcal{L}^{\pi})g(s,X\_{s}^{\pi^{\*}})ds\right]. |  | (A.1) |

Then, by ([3.6](https://arxiv.org/html/2512.09224v1#S3.E6 "In item (ii) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and ([3.7](https://arxiv.org/html/2512.09224v1#S3.E7 "In item (iii) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | gπ∗​(t,x)≡g​(t,x;π∗):=𝔼t,x​(XTπ∗),g^{\pi^{\*}}(t,x)\equiv g(t,x;\pi^{\*}):=\mathbb{E}\_{t,x}(X\_{T}^{\pi^{\*}}), |  | (A.2) |

which proves ([3.9](https://arxiv.org/html/2512.09224v1#S3.E9 "In Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")).

Next, we prove ([3.8](https://arxiv.org/html/2512.09224v1#S3.E8 "In Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")). Again by Itô’s formula, ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and ([3.7](https://arxiv.org/html/2512.09224v1#S3.E7 "In item (iii) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)=\displaystyle V(t,x)= | 𝔼t,x​[−∫tT(∂t+ℒπ)​V​(s,Xsπ∗)​𝑑s+V​(T,XTπ∗)]\displaystyle\mathbb{E}\_{t,x}\left[-\int\_{t}^{T}(\partial\_{t}+\mathcal{L}^{\pi})V(s,X\_{s}^{\pi^{\*}})ds+V(T,X\_{T}^{\pi^{\*}})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t,x​[∫tTλ​H​(πs∗)+γ​gπ∗​(s,Xsπ∗)​ℒπ​gπ∗​(s,Xsπ∗)−γ2​ℒπ​(gπ∗​(s,Xsπ∗))2​d​s]+𝔼t,x​[XTπ∗].\displaystyle\mathbb{E}\_{t,x}\Biggl[\int\_{t}^{T}\lambda H(\pi\_{s}^{\*})+\gamma g^{\pi^{\*}}(s,X\_{s}^{\pi^{\*}})\mathcal{L}^{\pi}g^{\pi^{\*}}(s,X\_{s}^{\pi^{\*}})-\frac{\gamma}{2}\mathcal{L}^{\pi}(g^{\pi^{\*}}(s,X\_{s}^{\pi^{\*}}))^{2}ds\Biggr]+\mathbb{E}\_{t,x}[X\_{T}^{\pi^{\*}}]. |  |

Note that for some π∈𝒜,(t,x)∈[0,T]×ℝ\pi\in\mathcal{A},(t,x)\in[0,T]\times\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | γ2​∂t(gπ​(t,x))2=γ​gπ​(t,x)​∂tgπ​(t,x)=−γ​gπ​(t,x)​ℒπ​gπ​(t,x).\frac{\gamma}{2}\partial\_{t}(g^{\pi}(t,x))^{2}=\gamma g^{\pi}(t,x)\partial\_{t}g^{\pi}(t,x)=-\gamma g^{\pi}(t,x)\mathcal{L}^{\pi}g^{\pi}(t,x). |  |

So,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)=\displaystyle V(t,x)= | 𝔼t,x​[∫tTλ​H​(πs∗)​𝑑s−γ2​∫tT(∂t+ℒπ)​(gπ∗​(s,Xsπ∗))2​𝑑s]+𝔼t,x​[XTπ∗]\displaystyle\mathbb{E}\_{t,x}\Biggl[\int\_{t}^{T}\lambda H(\pi\_{s}^{\*})ds-\frac{\gamma}{2}\int\_{t}^{T}(\partial\_{t}+\mathcal{L}^{\pi})(g^{\pi^{\*}}(s,X\_{s}^{\pi^{\*}}))^{2}ds\Biggr]+\mathbb{E}\_{t,x}[X\_{T}^{\pi^{\*}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t,x​[∫tTλ​H​(πs∗)​𝑑s−γ2​(gπ∗​(T,XTπ∗))2+γ2​(gπ∗​(t,x))2]+𝔼t,x​[XTπ∗]\displaystyle\mathbb{E}\_{t,x}\Biggl[\int\_{t}^{T}\lambda H(\pi\_{s}^{\*})ds-\frac{\gamma}{2}(g^{\pi^{\*}}(T,X\_{T}^{\pi^{\*}}))^{2}+\frac{\gamma}{2}(g^{\pi^{\*}}(t,x))^{2}\Biggr]+\mathbb{E}\_{t,x}[X\_{T}^{\pi^{\*}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t,x​[∫tTλ​H​(πs∗)​𝑑s−γ2​(XTπ∗)2+XTπ∗]+γ2​(𝔼t,x​(XTπ∗))2\displaystyle\mathbb{E}\_{t,x}\Biggl[\int\_{t}^{T}\lambda H(\pi\_{s}^{\*})ds-\frac{\gamma}{2}(X\_{T}^{\pi^{\*}})^{2}+X\_{T}^{\pi^{\*}}\Biggr]+\frac{\gamma}{2}\left(\mathbb{E}\_{t,x}(X\_{T}^{\pi^{\*}})\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | J​(t,x;π∗),\displaystyle J(t,x;\pi^{\*}), |  |

where the last equation is by ([3.1](https://arxiv.org/html/2512.09224v1#S3.E1 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")).

Lastly, we show that π∗\pi^{\*}, the maximizer of ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), is an equilibrium policy. Consider a perturbed policy as in Definition [3.1](https://arxiv.org/html/2512.09224v1#S3.Thmdefinition1 "Definition 3.1 ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"). That is, for a small time interval ϵ>0\epsilon>0, πϵ={πs,yϵ​(⋅)}(s,y)∈[0,T]×ℝ\pi^{\epsilon}=\{\pi^{\epsilon}\_{s,y}(\cdot)\}\_{(s,y)\in[0,T]\times\mathbb{R}}, with

|  |  |  |
| --- | --- | --- |
|  | πs,yε(⋅),={υ​(⋅),(s,y)∈[t,t+ε)×ℝ,πs,y∗​(⋅),(s,y)∈[t+ε,T]×ℝ,\pi\_{s,y}^{\varepsilon}(\cdot),=\begin{cases}\upsilon(\cdot),&(s,y)\in[t,t+\varepsilon)\times\mathbb{R},\\ \pi\_{s,y}^{\ast}(\cdot),&(s,y)\in[t+\varepsilon,T]\times\mathbb{R},\end{cases} |  |

where ν​(⋅)∈𝒫​(ℝ)\nu(\cdot)\in\mathcal{P}(\mathbb{R}). Under πϵ\pi^{\epsilon},

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,x;πϵ)=\displaystyle J(t,x;\pi^{\epsilon})= | 𝔼t,x​[∫tt+ϵλ​H​(ν)​𝑑s+∫t+ϵTλ​H​(πs)​𝑑s+XTπϵ−γ2​(XTπϵ)2]+γ2​(𝔼t,x​(XTπϵ))2\displaystyle\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\epsilon}\lambda H(\nu)ds+\int\_{t+\epsilon}^{T}\lambda H(\pi\_{s})ds+X\_{T}^{\pi^{\epsilon}}-\frac{\gamma}{2}(X\_{T}^{\pi^{\epsilon}})^{2}\right]+\frac{\gamma}{2}\left(\mathbb{E}\_{t,x}(X\_{T}^{\pi^{\epsilon}})\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ϵ​λ​H​(ν)+𝔼t,x​(J​(t+ϵ,Xt+ϵπϵ;πϵ))+γ2​(𝔼t,x​(XTπϵ))2−𝔼t,x​[γ2​(𝔼t+ϵ,Xt+ϵπϵ​(XTπϵ))2]\displaystyle\epsilon\lambda H(\nu)+\mathbb{E}\_{t,x}(J(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}};\pi^{\epsilon}))+\frac{\gamma}{2}(\mathbb{E}\_{t,x}(X\_{T}^{\pi^{\epsilon}}))^{2}-\mathbb{E}\_{t,x}\left[\frac{\gamma}{2}\left(\mathbb{E}\_{t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}}}(X\_{T}^{\pi^{\epsilon}})\right)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ϵ​λ​H​(ν)+𝔼t,x​(V​(t+ϵ,Xt+ϵπϵ))−γ2​𝔼t,x​[(gπϵ​(t+ϵ,Xt+ϵπϵ))2−(gπϵ​(t,x))2].\displaystyle\epsilon\lambda H(\nu)+\mathbb{E}\_{t,x}(V(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}}))-\frac{\gamma}{2}\mathbb{E}\_{t,x}\left[(g^{\pi^{\epsilon}}(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}}))^{2}-(g^{\pi^{\epsilon}}(t,x))^{2}\right]. |  |

By Itô’s formula, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x​(V​(t+ϵ,Xt+ϵπϵ))−V​(t,x)\displaystyle\mathbb{E}\_{t,x}(V(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}}))-V(t,x) | =𝔼t,x​[∫tt+ϵ(∂t+ℒν)​V​(s,Xsν)​𝑑s]\displaystyle=\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\epsilon}(\partial\_{t}+\mathcal{L}^{\nu})V(s,X\_{s}^{\nu})ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϵ​(∂t+ℒν)​V​(t,x)+O​(ϵ),\displaystyle=\epsilon(\partial\_{t}+\mathcal{L}^{\nu})V(t,x)+O(\epsilon), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x​[(gπϵ​(t+ϵ,Xt+ϵπϵ))2]−(gπϵ​(t,x))2\displaystyle\mathbb{E}\_{t,x}\left[\left(g^{\pi^{\epsilon}}(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}})\right)^{2}\right]-\left(g^{\pi^{\epsilon}}(t,x)\right)^{2} | =𝔼t,x​[∫tt+ϵ(∂t+ℒν)​(gν​(s,Xsν))2​𝑑s]\displaystyle=\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\epsilon}(\partial\_{t}+\mathcal{L}^{\nu})(g^{\nu}(s,X\_{s}^{\nu}))^{2}ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϵ​(∂t+ℒν)​(gν​(t,x))2+O​(ϵ)\displaystyle=\epsilon(\partial\_{t}+\mathcal{L}^{\nu})(g^{\nu}(t,x))^{2}+O(\epsilon) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϵ​(−2​gν​(t,x)​ℒν​gν​(t,x)+ℒν​(gν​(t,x))2)+O​(ϵ).\displaystyle=\epsilon(-2g^{\nu}(t,x)\mathcal{L^{\nu}}g^{\nu}(t,x)+\mathcal{L}^{\nu}(g^{\nu}(t,x))^{2})+O(\epsilon). |  |

Combining these together, we have

|  |  |  |
| --- | --- | --- |
|  | J​(t,x;πϵ)−V​(t,x)\displaystyle J(t,x;\pi^{\epsilon})-V(t,x) |  |
|  |  |  |
| --- | --- | --- |
|  | =J​(t,x;πϵ)−𝔼t,x​(V​(t+ϵ,Xt+ϵπϵ))+𝔼t,x​(V​(t+ϵ,Xt+ϵπϵ))−V​(t,x)\displaystyle=J(t,x;\pi^{\epsilon})-\mathbb{E}\_{t,x}(V(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}}))+\mathbb{E}\_{t,x}(V(t+\epsilon,X\_{t+\epsilon}^{\pi^{\epsilon}}))-V(t,x) |  |
|  |  |  |
| --- | --- | --- |
|  | =ϵ​(λ​H​(ν)−γ2​ℒν​(gν​(t,x))2+γ​gν​(t,x)​ℒν​gν​(t,x)+(∂t+ℒν)​V​(t,x))+O​(ϵ).\displaystyle=\epsilon\left(\lambda H(\nu)-\frac{\gamma}{2}\mathcal{L}^{\nu}(g^{\nu}(t,x))^{2}+\gamma g^{\nu}(t,x)\mathcal{L}^{\nu}g^{\nu}(t,x)+(\partial\_{t}+\mathcal{L}^{\nu})V(t,x)\right)+O(\epsilon). |  |

We conclude from ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) that

|  |  |  |
| --- | --- | --- |
|  | limsupϵ↓0J​(t,x;πϵ)−J​(t,x;π∗)ϵ=J​(t,x;πϵ)−V​(t,x)ϵ≤0,\lim\sup\_{\epsilon\downarrow 0}\frac{J(t,x;\pi^{\epsilon})-J(t,x;\pi^{\*})}{\epsilon}=\frac{J(t,x;\pi^{\epsilon})-V(t,x)}{\epsilon}\leq 0, |  |

which verifies that π∗\pi^{\*} is an equilibrium policy.

### A.3 Proof of Theorem [3.2](https://arxiv.org/html/2512.09224v1#S3.Thmtheorem2 "Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")

According to the objective function ([3.1](https://arxiv.org/html/2512.09224v1#S3.E1 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and the definition of the auxiliary value function ([3.9](https://arxiv.org/html/2512.09224v1#S3.E9 "In Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we conjecture that the value function is quadratic in xx and the auxiliary value function is linear in xx, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)=A​(t)​x2+B​(t)​x+C​(t),\displaystyle V(t,x)=A(t)x^{2}+B(t)x+C(t), |  | (A.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | gπ​(t,x)=g​(t,x;π)=x+hπ​(t),\displaystyle g^{\pi}(t,x)=g(t,x;\pi)=x+h^{\pi}(t), |  | (A.4) |

with A​(T)=C​(T)=hπ​(T)=0A(T)=C(T)=h^{\pi}(T)=0 and B​(T)=1B(T)=1.
Under this conjecture and by the infinitesimal generator ([3.4](https://arxiv.org/html/2512.09224v1#S3.E4 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), for (t,x)∈[0,T]×ℝ(t,x)\in[0,T]\times\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | ℒπ​gπ​(t,x)=ℒπ​(x+hπ​(t))=∫ℝu​(μ−r)​π​(u)​𝑑u,\mathcal{L}^{\pi}g^{\pi}(t,x)=\mathcal{L}^{\pi}(x+h^{\pi}(t))=\int\_{\mathbb{R}}u(\mu-r)\pi(u)du, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℒπ​(gπ​(t,x))2=ℒπ​(x2+(hπ​(t))2+2​x​hπ​(t))=∫ℝu​(μ−r)​π​(u)​𝑑u⋅(2​x+2​hπ​(t))+∫ℝσ2​u2​π​(u)​𝑑u+∫ℝ∫ℝ[(gπ)2​(t,x+u​(ez−1))−(gπ)2​(t,x)−u​(ez−1)​∂x(gπ)2]​π​(u)​𝑑u​ν​(d​z)=∫ℝu​(μ−r)​π​(u)​𝑑u⋅(2​x+2​hπ​(t))+∫ℝσ2​u2​π​(u)​𝑑u+∫ℝu2​δ2​π​(u)​𝑑u,\begin{split}\mathcal{L}^{\pi}(g^{\pi}(t,x))^{2}&=\mathcal{L}^{\pi}(x^{2}+(h^{\pi}(t))^{2}+2xh^{\pi}(t))\\ &=\int\_{\mathbb{R}}u(\mu-r)\pi(u)du\cdot(2x+2h^{\pi}(t))+\int\_{\mathbb{R}}\sigma^{2}u^{2}\pi(u)du\\ &+\int\_{\mathbb{R}}\int\_{\mathbb{R}}[(g^{\pi})^{2}(t,x+u(e^{z}-1))-(g^{\pi})^{2}(t,x)-u(e^{z}-1)\partial\_{x}(g^{\pi})^{2}]\pi(u)du\nu(dz)\\ &=\int\_{\mathbb{R}}u(\mu-r)\pi(u)du\cdot(2x+2h^{\pi}(t))+\int\_{\mathbb{R}}\sigma^{2}u^{2}\pi(u)du+\int\_{\mathbb{R}}u^{2}\delta^{2}\pi(u)du,\end{split} |  |

where δ2:=∫ℝ(ez−1)2​ν​(d​z)\delta^{2}:=\int\_{\mathbb{R}}(e^{z}-1)^{2}\nu(dz). The last equation is given by the fact that, for some function ψ​(t,x)∈ℂ1,2​([0,T]×ℝ)\psi(t,x)\in\mathbb{C}^{1,2}([0,T]\times\mathbb{R}) and ψ\psi is quadratic in xx, the second order Taylor expansion yields ψ​(t,x+Δ​x)=ψ​(t,x)+ψx​(t,x)​Δ​x+12​ψx​x​(t,x)​(Δ​x)2\psi(t,x+\Delta x)=\psi(t,x)+\psi\_{x}(t,x)\Delta x+\frac{1}{2}\psi\_{xx}(t,x)(\Delta x)^{2}, and so,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ∫ℝ[ψ​(t,x+u​(ez−1))−ψ​(t,x)−u​(ez−1)​ψx]​π​(u)​𝑑u​ν​(d​z)\displaystyle\int\_{\mathbb{R}}\int\_{\mathbb{R}}[\psi(t,x+u(e^{z}-1))-\psi(t,x)-u(e^{z}-1)\psi\_{x}]\pi(u)du\,\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫ℝ∫ℝ12​u2​(ez−1)2​π​(u)​𝑑u​ν​(d​z)⋅ψx​x.\displaystyle=\int\_{\mathbb{R}}\int\_{\mathbb{R}}\frac{1}{2}u^{2}(e^{z}-1)^{2}\pi(u)du\,\nu(dz)\cdot\psi\_{xx}. |  |

So, from ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and by ([3.4](https://arxiv.org/html/2512.09224v1#S3.E4 "In 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (∂t+ℒπ)​V+λ​H​(π)+γ​gπ​ℒπ​gπ−γ2​ℒπ​(gπ)2\displaystyle(\partial\_{t}+\mathcal{L}^{\pi})V+\lambda H(\pi)+\gamma g^{\pi}\mathcal{L}^{\pi}g^{\pi}-\frac{\gamma}{2}\mathcal{L}^{\pi}(g^{\pi})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Vt+∫ℝ[u​(μ−r)​Vx+12​u2​σ2​Vx​x+∫ℝ(V​(t,x+u​(ez−1))−V​(t,x)−u​(ez−1)​Vx)​ν​(d​z)]​πt​(u)​𝑑u\displaystyle V\_{t}+\int\_{\mathbb{R}}\left[u(\mu-r)V\_{x}+\frac{1}{2}u^{2}\sigma^{2}V\_{xx}+\int\_{\mathbb{R}}(V(t,x+u(e^{z}-1))-V(t,x)-u(e^{z}-1)V\_{x})\nu(dz)\right]\pi\_{t}(u)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫ℝλ​πt​(u)​log⁡πt​(u)​𝑑u+∫ℝγ​(x+hπ​(t))​u​(μ−r)​π​(u)​𝑑u\displaystyle-\int\_{\mathbb{R}}\lambda\pi\_{t}(u)\log\pi\_{t}(u)du+\int\_{\mathbb{R}}\gamma(x+h^{\pi}(t))u(\mu-r)\pi(u)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​[∫ℝu​(μ−r)​πt​(u)​𝑑u⋅(2​x+2​hπ​(t))+∫ℝσ2​u2​πt​(u)​𝑑u+∫ℝu2​δ2​πt​(u)​𝑑u]\displaystyle-\frac{\gamma}{2}\Biggl[\int\_{\mathbb{R}}u(\mu-r)\pi\_{t}(u)du\cdot(2x+2h^{\pi}(t))+\int\_{\mathbb{R}}\sigma^{2}u^{2}\pi\_{t}(u)du+\int\_{\mathbb{R}}u^{2}\delta^{2}\pi\_{t}(u)du\Biggr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Vt+∫ℝ[u​(μ−r)​Vx+Vx​x−γ2​u2​(σ2+δ2)−λ​log⁡πt​(u)]​πt​(u)​𝑑u.\displaystyle V\_{t}+\int\_{\mathbb{R}}\left[u(\mu-r)V\_{x}+\frac{V\_{xx}-\gamma}{2}u^{2}(\sigma^{2}+\delta^{2})-\lambda\log\pi\_{t}(u)\right]\pi\_{t}(u)du. |  |

The maximizer π∗\pi^{\*} that attains the supremum of ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt∗​(u)\displaystyle\pi^{\*}\_{t}(u) | =exp⁡(1λ​[u​(μ−r)​Vx+Vx​x−γ2​u2​(σ2+δ2)−1])\displaystyle=\exp\left(\frac{1}{\lambda}\left[u(\mu-r)V\_{x}+\frac{V\_{xx}-\gamma}{2}u^{2}(\sigma^{2}+\delta^{2})-1\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∝exp⁡(12​(σ2+δ2)​(Vx​x−γ)λ​[u2+2​(μ−r)​Vx(σ2+δ2)​(Vx​x−γ)​u])\displaystyle\propto\exp\left(\frac{1}{2}\frac{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}{\lambda}\left[u^{2}+\frac{2(\mu-r)V\_{x}}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}u\right]\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∼N​(−(μ−r)​Vx(σ2+δ2)​(Vx​x−γ),−λ(σ2+δ2)​(Vx​x−γ)).\displaystyle\sim N\left(-\frac{(\mu-r)V\_{x}}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)},-\frac{\lambda}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}\right). |  | (A.5) |

Substituting this back into ([3.5](https://arxiv.org/html/2512.09224v1#S3.E5 "In item (i) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")), we have

|  |  |  |
| --- | --- | --- |
|  | Vt−(μ−r)2​Vx2(σ2+δ2)​(Vx​x−γ)+Vx​x−γ2​(σ2+δ2)​[−λ(σ2+δ2)​(Vx​x−γ)+(μ−r)2​Vx2(σ2+δ2)2​(Vx​x−γ)2]\displaystyle V\_{t}-\frac{(\mu-r)^{2}V\_{x}^{2}}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}+\frac{V\_{xx}-\gamma}{2}(\sigma^{2}+\delta^{2})\left[-\frac{\lambda}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}+\frac{(\mu-r)^{2}V\_{x}^{2}}{(\sigma^{2}+\delta^{2})^{2}(V\_{xx}-\gamma)^{2}}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +λ2​log⁡(−2​π​e​λ(σ2+δ2)​(Vx​x−γ))\displaystyle+\frac{\lambda}{2}\log\left(-\frac{2\pi e\lambda}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =Vt−(μ−r)2​Vx22​(σ2+δ2)​(Vx​x−γ)+λ2​log⁡(−2​π​λ(σ2+δ2)​(Vx​x−γ))=0.\displaystyle=V\_{t}-\frac{(\mu-r)^{2}V\_{x}^{2}}{2(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}+\frac{\lambda}{2}\log\left(-\frac{2\pi\lambda}{(\sigma^{2}+\delta^{2})(V\_{xx}-\gamma)}\right)=0. |  |

Under the conjectured forms of the value function and auxiliary value function, the left-hand-side of the above equation becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | At​(t)​x2+Bt​(t)​x+Ct​(t)−(μ−r)2​(2​A​(t)​x+B​(t))22​(σ2+δ2)​(2​A​(t)−γ)+λ2​log⁡(−2​π​λ(σ2+δ2)​(2​A​(t)−γ))\displaystyle A\_{t}(t)x^{2}+B\_{t}(t)x+C\_{t}(t)-\frac{(\mu-r)^{2}(2A(t)x+B(t))^{2}}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}+\frac{\lambda}{2}\log\left(-\frac{2\pi\lambda}{(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | {At​(t)−4​(μ−r)2​(A​(t))22​(σ2+δ2)​(2​A​(t)−γ)}​x2+{Bt​(t)−4​(μ−r)2​A​(t)​B​(t)2​(σ2+δ2)​(2​A​(t)−γ)}​x\displaystyle\Biggl\{A\_{t}(t)-\frac{4(\mu-r)^{2}(A(t))^{2}}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}\Biggr\}x^{2}+\Biggl\{B\_{t}(t)-\frac{4(\mu-r)^{2}A(t)B(t)}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}\Biggr\}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +{Ct​(t)−(μ−r)2​(B​(t))22​(σ2+δ2)​(2​A​(t)−γ)+λ2​log⁡(−2​π​λ(σ2+δ2)​(2​A​(t)−γ))}=0.\displaystyle+\Biggl\{C\_{t}(t)-\frac{(\mu-r)^{2}(B(t))^{2}}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}+\frac{\lambda}{2}\log\left(-\frac{2\pi\lambda}{(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}\right)\Biggr\}=0. |  |

So, A,B,CA,B,C can be solved by 3 ODEs.

|  |  |  |  |
| --- | --- | --- | --- |
|  | At​(t)−4​(μ−r)2​(A​(t))22​(σ2+δ2)​(2​A​(t)−γ)=0,\displaystyle A\_{t}(t)-\frac{4(\mu-r)^{2}(A(t))^{2}}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}=0, |  | (A.6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Bt​(t)−4​(μ−r)2​A​(t)​B​(t)2​(σ2+δ2)​(2​A​(t)−γ)=0,\displaystyle B\_{t}(t)-\frac{4(\mu-r)^{2}A(t)B(t)}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}=0, |  | (A.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct​(t)−(μ−r)2​(B​(t))22​(σ2+δ2)​(2​A​(t)−γ)+λ2​log⁡(−2​π​λ(σ2+δ2)​(2​A​(t)−γ))=0.\displaystyle C\_{t}(t)-\frac{(\mu-r)^{2}(B(t))^{2}}{2(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}+\frac{\lambda}{2}\log\left(-\frac{2\pi\lambda}{(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}\right)=0. |  | (A.8) |

Moreover, we know from ([3.6](https://arxiv.org/html/2512.09224v1#S3.E6 "In item (ii) ‣ Theorem 3.1 (Verification Theorem) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂t+ℒπ)​gπ​(t,x)=\displaystyle(\partial\_{t}+\mathcal{L}^{\pi})g^{\pi}(t,x)= | htπ​(t)+∫ℝu​(μ−r)​πt​(u)​𝑑u\displaystyle h^{\pi}\_{t}(t)+\int\_{\mathbb{R}}u(\mu-r)\pi\_{t}(u)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | htπ​(t)−(μ−r)2​(2​A​(t)​x+B​(t))(σ2+δ2)​(2​A​(t)−γ)=0.\displaystyle h^{\pi}\_{t}(t)-\frac{(\mu-r)^{2}(2A(t)x+B(t))}{(\sigma^{2}+\delta^{2})(2A(t)-\gamma)}=0. |  |

This tells us that A​(t)=0,∀t∈[0,T]A(t)=0,\forall t\in[0,T]. So,

|  |  |  |  |
| --- | --- | --- | --- |
|  | htπ​(t)+(μ−r)2γ​(σ2+δ2)=0,h^{\pi}\_{t}(t)+\frac{(\mu-r)^{2}}{\gamma(\sigma^{2}+\delta^{2})}=0, |  | (A.9) |

which yields ([3.12](https://arxiv.org/html/2512.09224v1#S3.E12 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")).
Then, it follows from the above ODEs that B​(t)=1,∀t∈[0,T]B(t)=1,\forall t\in[0,T] and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct​(t)+(μ−r)22​γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2))=0,C\_{t}(t)+\frac{(\mu-r)^{2}}{2\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)=0, |  | (A.10) |

which yields ([3.11](https://arxiv.org/html/2512.09224v1#S3.E11 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")).
This indicates that the value function is in fact linear in xx and is V​(t,x)=x+C​(t)V(t,x)=x+C(t).
Substituting V​(t,x)V(t,x) into the equilibrium policy ([A.5](https://arxiv.org/html/2512.09224v1#A1.E5 "In A.3 Proof of Theorem 3.2 ‣ Appendix A Proofs ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt∗​(u)∼N​((μ−r)γ​(σ2+δ2),λγ​(σ2+δ2)),\pi^{\*}\_{t}(u)\sim N\left(\frac{(\mu-r)}{\gamma(\sigma^{2}+\delta^{2})},\frac{\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right), |  | (A.11) |

which is ([3.10](https://arxiv.org/html/2512.09224v1#S3.E10 "In Theorem 3.2 (Equilibrium Policy and Value Functions) ‣ 3 Exploratory Mean-Variance with Jumps Problem ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")). Since πt∗​(u)\pi^{\*}\_{t}(u) does not depend on the portfolio value xx, it is easy to check that it is admissible according to Definition [2.1](https://arxiv.org/html/2512.09224v1#S2.Thmdefinition1 "Definition 2.1 (Admissible Policy) ‣ 2 Problem Formulation and Preliminaries ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach"), which completes the proof.

### A.4 Proof of Theorem [4.1](https://arxiv.org/html/2512.09224v1#S4.Thmtheorem1 "Theorem 4.1 ‣ 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")

Consider a parameterized policy πθ\pi^{\theta}, its corresponding value function VθV^{\theta} and auxiliary value function gθg^{\theta}, and a process MθM^{\theta} defined in ([4.6](https://arxiv.org/html/2512.09224v1#S4.E6 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")). Then, by Itô’s formula, ([4.5](https://arxiv.org/html/2512.09224v1#S4.E5 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")) and ([4.4](https://arxiv.org/html/2512.09224v1#S4.E4 "In 4 RL Algorithm ‣ Exploratory Mean-Variance with Jumps: An Equilibrium Approach")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mtθ=\displaystyle dM\_{t}^{\theta}= | d​Xtθ+Ctθ​(t)​d​t−γ​gθ​d​(gθ)−γ2​d​[gθ]+λ​H​(πtθ)​d​t\displaystyle dX\_{t}^{\theta}+C\_{t}^{\theta}(t)dt-\gamma g^{\theta}d(g^{\theta})-\frac{\gamma}{2}d[g^{\theta}]+\lambda H(\pi^{\theta}\_{t})dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫ℝu​(μt​r​u​e−r)​πtθ​(u)​𝑑u​𝑑t+(…)​d​Wt+(…)​d​N~​(d​t,d​z)\displaystyle\int\_{\mathbb{R}}u(\mu\_{true}-r)\pi^{\theta}\_{t}(u)dudt+(...)dW\_{t}+(...)d\tilde{N}(dt,dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −((μ−r)22​γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2)))​d​t−γ​gθ​[d​Xtθ+htθ​(t)​d​t]\displaystyle-\left(\frac{(\mu-r)^{2}}{2\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\right)dt-\gamma g^{\theta}[dX\_{t}^{\theta}+h\_{t}^{\theta}(t)dt] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​d​[Xtθ]+λ2​log⁡(2​π​e​λγ​(σ2+δ2))​d​t\displaystyle-\frac{\gamma}{2}d[X\_{t}^{\theta}]+\frac{\lambda}{2}\log\left(\frac{2\pi e\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫ℝu​(μt​r​u​e−r)​πtθ​(u)​𝑑u​𝑑t+(…)​d​Wt+(…)​d​N~​(d​t,d​z)\displaystyle\int\_{\mathbb{R}}u(\mu\_{true}-r)\pi^{\theta}\_{t}(u)dudt+(...)dW\_{t}+(...)d\tilde{N}(dt,dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −((μ−r)22​γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2)))​d​t\displaystyle-\left(\frac{(\mu-r)^{2}}{2\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ​gθ​[∫ℝ(μt​r​u​e−r)​πtθ​(u)​𝑑u​𝑑t−(μ−r)2γ​(σ2+δ2)​d​t+(…)​d​Wt+(…)​d​N~​(d​t,d​z)]\displaystyle-\gamma g^{\theta}\left[\int\_{\mathbb{R}}(\mu\_{true}-r)\pi^{\theta}\_{t}(u)dudt-\frac{(\mu-r)^{2}}{\gamma(\sigma^{2}+\delta^{2})}dt+(...)dW\_{t}+(...)d\tilde{N}(dt,dz)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​[∫ℝσt​r​u​e2​u2​πt​(u)​𝑑u​𝑑t+∫ℝ∫ℝu2​(ez−1)2​πt​(u)​𝑑u​𝑑N​(d​t,d​z)]\displaystyle-\frac{\gamma}{2}\left[\int\_{\mathbb{R}}\sigma\_{true}^{2}u^{2}\pi\_{t}(u)dudt+\int\_{\mathbb{R}}\int\_{\mathbb{R}}u^{2}(e^{z}-1)^{2}\pi\_{t}(u)dudN(dt,dz)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ2​log⁡(2​π​e​λγ​(σ2+δ2))​d​t\displaystyle+\frac{\lambda}{2}\log\left(\frac{2\pi e\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫ℝu​(μt​r​u​e−r)​πtθ​(u)​𝑑u​𝑑t+(…)​d​Wt+(…)​d​N~​(d​t,d​z)\displaystyle\int\_{\mathbb{R}}u(\mu\_{true}-r)\pi^{\theta}\_{t}(u)dudt+(...)dW\_{t}+(...)d\tilde{N}(dt,dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −((μ−r)22​γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2)))​d​t\displaystyle-\left(\frac{(\mu-r)^{2}}{2\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ​gθ​[∫ℝ(μt​r​u​e−r)​πtθ​(u)​𝑑u​𝑑t−(μ−r)2γ​(σ2+δ2)​d​t+(…)​d​Wt+(…)​d​N~​(d​t,d​z)]\displaystyle-\gamma g^{\theta}\left[\int\_{\mathbb{R}}(\mu\_{true}-r)\pi^{\theta}\_{t}(u)dudt-\frac{(\mu-r)^{2}}{\gamma(\sigma^{2}+\delta^{2})}dt+(...)dW\_{t}+(...)d\tilde{N}(dt,dz)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​[∫ℝσt​r​u​e2​u2​πt​(u)​𝑑u​𝑑t+∫ℝ∫ℝu2​(ez−1)2​πt​(u)​𝑑u​ν​(d​z)​𝑑t+(…)​N~​(d​t,d​z)]\displaystyle-\frac{\gamma}{2}\left[\int\_{\mathbb{R}}\sigma\_{true}^{2}u^{2}\pi\_{t}(u)dudt+\int\_{\mathbb{R}}\int\_{\mathbb{R}}u^{2}(e^{z}-1)^{2}\pi\_{t}(u)du\nu(dz)dt+(...)\tilde{N}(dt,dz)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ2​log⁡(2​π​e​λγ​(σ2+δ2))​d​t\displaystyle+\frac{\lambda}{2}\log\left(\frac{2\pi e\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (μt​r​u​e−r)​(μ−r)λ​(σ2+δ2)​d​t+(…)​d​Wt+(…)​d​N~​(d​t,d​z)\displaystyle\frac{(\mu\_{true}-r)(\mu-r)}{\lambda(\sigma^{2}+\delta^{2})}dt+(...)dW\_{t}+(...)d\tilde{N}(dt,dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −((μ−r)22​γ​(σ2+δ2)+λ2​log⁡(2​π​λγ​(σ2+δ2)))​d​t\displaystyle-\left(\frac{(\mu-r)^{2}}{2\gamma(\sigma^{2}+\delta^{2})}+\frac{\lambda}{2}\log\left(\frac{2\pi\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ​gθ​[(μt​r​u​e−r)​(μ−r)γ​(σ2+δ2)−(μ−r)2γ​(σ2+δ2)]​d​t\displaystyle-\gamma g^{\theta}\left[\frac{(\mu\_{true}-r)(\mu-r)}{\gamma(\sigma^{2}+\delta^{2})}-\frac{(\mu-r)^{2}}{\gamma(\sigma^{2}+\delta^{2})}\right]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ​(σt​r​u​e2+δt​r​u​e2)2​(λγ​(σ2+δ2)+(μ−r)2γ2​(σ2+δ2)2)​d​t+λ2​log⁡(2​π​e​λγ​(σ2+δ2))​d​t.\displaystyle-\frac{\gamma(\sigma\_{true}^{2}+\delta\_{true}^{2})}{2}\left(\frac{\lambda}{\gamma(\sigma^{2}+\delta^{2})}+\frac{(\mu-r)^{2}}{\gamma^{2}(\sigma^{2}+\delta^{2})^{2}}\right)dt+\frac{\lambda}{2}\log\left(\frac{2\pi e\lambda}{\gamma(\sigma^{2}+\delta^{2})}\right)dt. |  |

The drift term is zero when θ=θt​r​u​e\theta=\theta\_{true}, indicating that MθM^{\theta} is a martingale.