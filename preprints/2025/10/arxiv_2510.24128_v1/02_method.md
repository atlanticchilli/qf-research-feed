---
authors:
- Yuchao Dong
- Harry Zheng
doc_id: arxiv:2510.24128v1
family_id: arxiv:2510.24128
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization
  Method'
url_abs: http://arxiv.org/abs/2510.24128v1
url_html: https://arxiv.org/html/2510.24128v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yuchao Dong
and Harry Zheng
 School of Mathematical Sciences, Key Laboratory of Intelligent Computing and Applications (Ministry of Education), Tongji University, Shanghai 200092, China. The work of the second author was funded by National Natural Science Foundation of China
(No.12471425) Department of Mathematics, Imperial College, London SW7 2BZ, UK (Email: h.zheng@imperial.ac.uk). The work was supported by the Engineering and Physical Sciences Research Council of
UK (Grant No. EP/V008331/1).

###### Abstract

This paper studies the time-inconsistent MV optimal stopping problem via a game-theoretic approach to find equilibrium strategies. To overcome the mathematical intractability of direct equilibrium analysis, we propose a vanishing regularization method: first, we introduce an entropy-based regularization term to the MV objective, modeling mixed-strategy stopping times using the intensity of a Cox process. For this regularized problem, we derive a coupled extended Hamilton-Jacobi-Bellman (HJB) equation system, prove a verification theorem linking its solutions to equilibrium intensities, and establish the existence of classical solutions for small time horizons via a contraction mapping argument. By letting the regularization term tend to zero, we formally recover a system of parabolic variational inequalities that characterizes equilibrium stopping times for the original MV problem. This system includes an additional key quadratic term–a distinction from classical optimal stopping, where stopping conditions depend only on comparing the value function to the instantaneous reward.

Keywords: Mean-variance problems, Time-inconsistency, Cox process, Equilibrium stopping time, Extended HJB equation, Vanishing Regularization Method

AMS MSC2010: 60G40; 60J70; 91A10; 91A25; 91G80; 91B02; 91B51.

## 1 Introduction

Given a diffusion process XX, the classical optimal stopping problem is to determine a stopping time τ\tau that maximizes

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[f​(Xτ)].\mathbb{E}\left[f(X\_{\tau})\right]. |  |

Optimal stopping has many applications, for example, financial decision-making (e.g., timing for asset sales) and statistical inference (e.g., stopping rules for hypothesis testing [[17](https://arxiv.org/html/2510.24128v1#bib.bib17)]). However, in financial contexts, there is often an additional imperative to mitigate decision-related risk. In line with the mean-variance analysis of [[14](https://arxiv.org/html/2510.24128v1#bib.bib14)], we identify the return with the expectation and the risk with the variance and aim to select a stopping time that maximizes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[f​(Xτ)]−γ2​Var​[f​(Xτ)],\mathbb{E}\left[f(X\_{\tau})\right]-\frac{\gamma}{2}\text{Var}\left[f(X\_{\tau})\right], |  | (1) |

where γ≥0\gamma\geq 0 denotes the risk aversion coefficient. Problem ([1](https://arxiv.org/html/2510.24128v1#S1.E1 "In 1 Introduction ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) is referred as a mean-variance (MV) stopping problem in the literature.

Similar to the classical dynamic MV problem, the optimal stopping rule typically depends on the initial state xx, which means that it does not generally satisfy Bellman’s principle of optimality. In the literature this is known as time-inconsistency. Time-inconsistent problems are typically studied using two approaches. One is to formulate the problem for a fixed initial state and allow the corresponding optimal stopping rule to depend on that initial state, called the pre-commitment approach. The other is to look for a stopping rule that remains optimal at every period when re-evaluated from that period’s perspective, called the game-theoretic approach.

Strotz [[16](https://arxiv.org/html/2510.24128v1#bib.bib16)] is the first to explore the game-theoretic approach to time-inconsistent problems in dynamic utility maximization with non-exponential discounting. Bjork et al. [[4](https://arxiv.org/html/2510.24128v1#bib.bib4)] give a comprehensive treatment of time-inconsistent Markovian models and characterize the equilibrium by a solution to a generalized HJB equation, called the extended HJB system. Time inconsistent control problems have attracted considerable research interest in recent years with many applications. For example, Bjork et al. [[5](https://arxiv.org/html/2510.24128v1#bib.bib5)] solve a MV problem with state dependent risk aversion. He and Liang [[11](https://arxiv.org/html/2510.24128v1#bib.bib11)] study a defined contribution insurance problem in a MV framework. Dai et al. [[8](https://arxiv.org/html/2510.24128v1#bib.bib8)] solve a MV problem with reinforcement learning method.
All aforementioned papers have fixed finite horizon.

The literature on the game-theoretic approach to time-inconsistent stopping problems is in the early developing stage. Christensen and Lindensjö [[6](https://arxiv.org/html/2510.24128v1#bib.bib6)] study an equilibrium stopping problem with initial state dependent reward. Bayraktar et al. [[2](https://arxiv.org/html/2510.24128v1#bib.bib2)] consider three equilibrium concepts proposed in the literature for time-inconsistent stopping problems with non-exponential discount.
There is little research for MV stopping problems. The only ones the authors are aware of are Peskir and Shiryaev [[15](https://arxiv.org/html/2510.24128v1#bib.bib15)] on the so-called dynamic optimal stopping time, which is similar to the game theoretic approach and Christensen and Lindensjö [[7](https://arxiv.org/html/2510.24128v1#bib.bib7)] on a subgame perfect Nash equilibrium for stopping problems.

In this paper, we study the equilibrium strategy and relate it to the extended HJB equation, which means that we need to formulate the problem as a game and look for equilibrium. It is a fundamental result in game theory that equilibrium generally exists for mixed strategies rather than pure strategies in a broad class of games111For example, the rock - paper - scissors game is a classic example in game theory, and it has no pure strategy Nash equilibrium but has a mixed strategy Nash equilibrium in which the player choose each action with equal probability 1/31/3. . Hence, we focus on mixed strategy stopping times by allowing the agents to choose the intensity function of a Cox process as a randomization device for the stopping decision, whereas [[7](https://arxiv.org/html/2510.24128v1#bib.bib7), [15](https://arxiv.org/html/2510.24128v1#bib.bib15)] characterize the equilibrium and provide other necessary and sufficient equilibrium conditions, but do not derive the extended HJB equation. While their results coincide with ours for geometric Brownian motion case, our derivation is motivated by the vanishing regularity approach, a key distinction from prior research.

We now describe the key methodology for solving the MV stopping problem. We first add a regularization term, weighted by a constant λ\lambda into the target functional (see ([2](https://arxiv.org/html/2510.24128v1#S2.E2 "In 2 Mean Variance Stopping and its Relaxed Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"))), to form a regularized problem with control variate being the intensity (as opposed to the stopping time), which makes the definition of the equilibrium straightforward. We then derive the associated extended HJB equation (see ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"))), prove a verification theorem (see Theorem [3.1](https://arxiv.org/html/2510.24128v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) and establish the existence of its solution under certain technical assumptions (see Theorem [3.2](https://arxiv.org/html/2510.24128v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). Finally, we let λ\lambda tend to zero (i.e., vanishing regularization) to formally obtain a system of parabolic variational inequalities (see ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"))) that characterizes the equilibrium stopping time for the original MV stopping problem. To the best knowledge of the authors, this is the first time such a system of equations is reported in the literature. Furthermore, we find that the stopping condition is not determined solely by comparing the value function with the instantaneous reward; instead, an additional quadratic term also plays a role in the formulation, which is in sharp contrast to the standard optimal stopping problem.

Finally, we aim to emphasize the motivation underlying our method. In [[9](https://arxiv.org/html/2510.24128v1#bib.bib9)], the authors investigated an entropy-regularized optimal stopping problem and demonstrated that the corresponding optimal value function is associated with a penalized form for the variational inequality. Notably, this penalized equation also converges to the original variational inequality as the regularization parameter tends to zero. For MV optimal stopping problems, we adopt an analogous approach: we first introduce and analyze a regularized version of the problem, then subsequently let the regularization parameter vanish to recover results for the original MV stopping problem. Such ideas are pervasive in mathematical research. When addressing a computationally or theoretically challenging problem, researchers often first consider a perturbed or regularized counterpart—whose solution is more tractable to derive—and then take an appropriate limit to revert to the original problem. It is precisely this core logic that leads us to name our approach Vanishing Regularization Method.

The rest of the paper is organized as follows: In Section 2 we formulate the MV stopping problem and its relaxed problem together with the definition of equilibrium. In Section 3 we derive the extended HJB equation for the relaxed problem and prove a verification theorem (Theorem [3.1](https://arxiv.org/html/2510.24128v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) and an existence result (Theorem [3.2](https://arxiv.org/html/2510.24128v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). In Section 4 we let λ\lambda tend to zero to formally get the variation system for the original MV stopping problem and show that it characterizes the equilibrium stopping time (Theorems [4.1](https://arxiv.org/html/2510.24128v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") and [4.2](https://arxiv.org/html/2510.24128v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). In Section 5 we give some further discussions on our results, including infinite horizon case, discrete time approximation, and general time-inconsistent problems. Section 6 concludes the paper. Appendix contains the proofs of a local time approximation relation ([9](https://arxiv.org/html/2510.24128v1#S4.E9 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) and a technical lemma (Lemma [B.1](https://arxiv.org/html/2510.24128v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B A Key Lemma ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) that is needed in the proof of Theorem [3.2](https://arxiv.org/html/2510.24128v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method").

## 2 Mean Variance Stopping and its Relaxed Problem

In this section, we introduce the basic framework of the problem. Especially, we give the formulation for the relaxed MV stopping problem and the definition of related equilibrium strategy.
Let (Ω,ℱ,P)(\Omega,\mathcal{F},P) be a probability space, on which a standard dd-dimensional Brownian motion WW is defined222For simplicity, we consider the case that the dimension of the Brownian motion is same to that of the state process. It can be extended to other cases without any major modification as long as Assumption [2.1](https://arxiv.org/html/2510.24128v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2 Mean Variance Stopping and its Relaxed Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") holds.. The ℝd\mathbb{R}^{d}-valued state process XX satisfies

|  |  |  |
| --- | --- | --- |
|  | d​Xt=b​(t,Xt)​d​t+σ​(t,Xt)​d​Wt.dX\_{t}=b(t,X\_{t})dt+\sigma(t,X\_{t})dW\_{t}. |  |

Denote by 𝔽:={ℱt}t\mathbb{F}:=\{\mathcal{F}\_{t}\}\_{t} the natural filtration generated by WW, augmented by all PP-null sets. The set 𝒯t,T\mathcal{T}\_{t,T} is defined as the totality of all 𝔽\mathbb{F}-stopping time taking values in [t,T][t,T]. For any time t∈[0,T]t\in[0,T], the MV stopping problem is to choose τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T} such that the following functional

|  |  |  |
| --- | --- | --- |
|  | J​(t,x;τ):=𝔼t,x​[f​(Xτ)]−γ2​Vart,x​[f​(Xτ)]J(t,x;\tau):=\mathbb{E}\_{t,x}\left[f(X\_{\tau})\right]-\frac{\gamma}{2}\text{Var}\_{t,x}\left[f(X\_{\tau})\right] |  |

is maximized, where 𝔼t,x​[⋅]\mathbb{E}\_{t,x}[\cdot] and Vart,x​[⋅]\text{Var}\_{t,x}[\cdot] denote the conditional expectation and conditional variance conditioning on Xt=xX\_{t}=x, respectively.

In this paper, we shall adopt the following assumptions on the coefficients.

###### Assumption 2.1.

The coefficients b,σb,\sigma and ff are Lipschitz continuous with linear growth in xx, uniformly in tt, i.e., there exists a constant CC such that, for any t∈[0,T]t\in[0,T] and x,y∈ℝdx,y\in\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | |b​(t,x)|,|σ​(t,x)|,|f​(x)|≤C​(1+|x|),|b(t,x)|,|\sigma(t,x)|,|f(x)|\leq C(1+|x|), |  |

and

|  |  |  |
| --- | --- | --- |
|  | |b​(t,x)−b​(t,y)|,|σ​(t,x)−σ​(t,y)|,|f​(x)−f​(y)|≤C​|x−y|.|b(t,x)-b(t,y)|,|\sigma(t,x)-\sigma(t,y)|,|f(x)-f(y)|\leq C|x-y|. |  |

Moreover, σ​σT\sigma\sigma^{T} is uniformly non-degenerate, i.e., there exists a constant cc such that σ​σT​(t,x)≥c​I\sigma\sigma^{T}(t,x)\geq cI for any t∈[0,T]t\in[0,T] and x∈ℝdx\in\mathbb{R}^{d}.

For any function ff defined on [0,T]×ℝd[0,T]\times\mathbb{R}^{d}, we use the notations ∂tf\partial\_{t}f and ∂xf\partial\_{x}f to represent the derivatives with respect to tt and xx and ∂x​xf\partial\_{xx}f its Hessian. In this paper, we use CC to represent a constant that could depend on the coefficients but may be different from line to line.

It is well-known that, for MV problem, the dynamic programming principle fails. Thus, people focus on two kinds of strategies. One is called pre-committed strategy, which is a fixed plan chosen at the initial time and enforced irrevocably across all future periods, regardless of new information or changing market conditions. On the other hand, an equilibrium strategy or time-consistent strategy is a plan that remains optimal at every period when re-evaluated from that period’s perspective, which aligns with the concept of a subgame perfect equilibrium in dynamic games, where strategies are optimal in all ”subgames” (i.e., at all points in time).

In this paper, we study the equilibrium strategy, especially the extended HJB equation related to it. This means that we need to formulate the problem as a game and look for equilibrium. It is indeed a fundamental result in game theory that equilibrium generally exists for mixed strategies rather than pure strategies in a broad class of games. Hence, it is better to consider some notion of mixed strategy, namely, at each time, the players fix a probability of stopping and decide whether or not to stop according to this probability. Such mixed strategy is also called randomized stopping time in some literature, see, for example, Bayer et al. [[1](https://arxiv.org/html/2510.24128v1#bib.bib1)] and Dong [[9](https://arxiv.org/html/2510.24128v1#bib.bib9)]. Here, we model it as a doubly stochastic Poisson process. More precisely, let Θ\Theta be a random variable, which is exponentially distributed with unit intensity and independent of Brownian motion. Given a non-negative 𝔽\mathbb{F}-adapted process {πs}t≤s≤T\{\pi\_{s}\}\_{t\leq s\leq T}, a random time τ\tau is defined as

|  |  |  |
| --- | --- | --- |
|  | τ:=inf{s∈[t,T]:∫tsπu​𝑑u≥Θ}∧T,\tau:=\inf\left\{s\in[t,T]:\int\_{t}^{s}\pi\_{u}du\geq\Theta\right\}{\wedge}T, |  |

where we adopt the convention that the infimum of an empty set is infinity. It represents the time that the player chooses to stop. Literally speaking, it means that, conditioning on having not stopped before, the probability that the player stops between tt and t+d​tt+dt is πt​d​t\pi\_{t}dt. Under this formulation, instead of choosing a stopping time, the player chooses the intensity process π\pi to optimize the MV objective function.

From the results of doubly stochastic Poisson processes (see Jeanblanc et al. [[12](https://arxiv.org/html/2510.24128v1#bib.bib12)] for details), one can compute that, for any function φ\varphi,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[φ​(Xτ)|ℱT]=∫tTφ​(Xs)​πs​e−∫tsπu​𝑑u​𝑑s+φ​(XT)​e−∫tTπu​𝑑u.\mathbb{E}\left[\varphi(X\_{\tau})|\mathcal{F}\_{T}\right]=\int\_{t}^{T}\varphi(X\_{s})\pi\_{s}e^{-\int\_{t}^{s}\pi\_{u}du}ds+\varphi(X\_{T})e^{-\int\_{t}^{T}\pi\_{u}du}. |  |

Then, we have that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[φ​(Xτ)]=𝔼t,x​[𝔼​[φ​(Xτ)|ℱT]]=𝔼t,x​[∫tTφ​(Xs)​πs​e−∫tsπu​𝑑u​𝑑s+φ​(XT)​e−∫tTπu​𝑑u].\mathbb{E}\_{t,x}[\varphi(X\_{\tau})]=\mathbb{E}\_{t,x}[\mathbb{E}[\varphi(X\_{\tau})|\mathcal{F}\_{T}]]=\mathbb{E}\_{t,x}\left[\int\_{t}^{T}\varphi(X\_{s})\pi\_{s}e^{-\int\_{t}^{s}\pi\_{u}du}ds+\varphi(X\_{T})e^{-\int\_{t}^{T}\pi\_{u}du}\right]. |  |

Thus, the MV criteria can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[f​(Xτ)]−γ2​Vart,x​[f​(Xτ)]=𝔼t,x​[∫tT(f−γ2​f2)​(Xs)​πs​e−∫tsπu​𝑑u​𝑑s+(f−γ2​f2)​(XT)​e−∫tTπu​𝑑u]+γ2​(𝔼t,x​[∫tTf​(Xs)​πs​e−∫tsπu​𝑑u​𝑑s+f​(XT)​e−∫tTπu​𝑑u])2.\begin{split}&\mathbb{E}\_{t,x}\left[f(X\_{\tau})\right]-\frac{\gamma}{2}\text{Var}\_{t,x}\left[f(X\_{\tau})\right]\\ =&\mathbb{E}\_{t,x}\left[\int\_{t}^{T}(f-\frac{\gamma}{2}f^{2})(X\_{s})\pi\_{s}e^{-\int\_{t}^{s}\pi\_{u}du}ds+(f-\frac{\gamma}{2}f^{2})(X\_{T})e^{-\int\_{t}^{T}\pi\_{u}du}\right]\\ &+\frac{\gamma}{2}\left(\mathbb{E}\_{t,x}\left[\int\_{t}^{T}f(X\_{s})\pi\_{s}e^{-\int\_{t}^{s}\pi\_{u}du}ds+f(X\_{T})e^{-\int\_{t}^{T}\pi\_{u}du}\right]\right)^{2}.\end{split} |  |

However, we consider a regularized MV reward, which is defined as the following

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Jλ​(t,x;π)\displaystyle J^{\lambda}(t,x;\pi) | :=\displaystyle:= | 𝔼t,x​[∫tT{(f−γ2​f2)​(Xs)​πs+λ​H​(πs)}​e−∫tsπu​𝑑u​𝑑s+(f−γ2​f2)​(XT)​e−∫tTπu​𝑑u]\displaystyle\mathbb{E}\_{t,x}\left[\int\_{t}^{T}\left\{(f-\frac{\gamma}{2}f^{2})(X\_{s})\pi\_{s}+\lambda H(\pi\_{s})\right\}e^{-\int\_{t}^{s}\pi\_{u}du}ds+(f-\frac{\gamma}{2}f^{2})(X\_{T})e^{-\int\_{t}^{T}\pi\_{u}du}\right] |  | (2) |
|  |  |  | +γ2​(𝔼t,x​[∫tTf​(Xs)​πs​e−∫tsπu​𝑑u​𝑑s+f​(XT)​e−∫tTπu​𝑑u])2,\displaystyle{}+\frac{\gamma}{2}\left(\mathbb{E}\_{t,x}\left[\int\_{t}^{T}f(X\_{s})\pi\_{s}e^{-\int\_{t}^{s}\pi\_{u}du}ds+f(X\_{T})e^{-\int\_{t}^{T}\pi\_{u}du}\right]\right)^{2}, |  |

where the function HH is given by H​(π)=π−π​log⁡πH(\pi)=\pi-\pi\log\pi and λ\lambda is a positive constant.
The regularization term prevents the intensity taking values 0 and ∞\infty, which refers to continue and stop deterministically. This provides mathematically tractability for the problem, which one can derive the related HJB equations. The motivation comes from [[9](https://arxiv.org/html/2510.24128v1#bib.bib9)] in the study of reinforcement learning method for optimal stopping problem, where HH is referred as unnormalized entropy to encourage randomness in the strategy.

We will let λ\lambda tend to zero to go back to the original problem. Dong [[9](https://arxiv.org/html/2510.24128v1#bib.bib9)] proves that the HJB equations converge for optimal stopping problem. To our best knowledge, it is still an open problem for MV stopping problem, but, formally, we will see that the extended HJB equation converge to some system that gives an equilibrium stopping time for MV problem.

Since we focus on extended HJB equation, we shall restrict to the Markovian strategies, i.e., πs=π​(s,Xs)\pi\_{s}=\pi(s,X\_{s}) for some deterministic function π\pi. Similar to [[3](https://arxiv.org/html/2510.24128v1#bib.bib3)], one can define an equilibrium in the following sense.

###### Definition 2.1.

A strategy π∗\pi^{\*} is called an equilibrium strategy, if for any ε,v>0\varepsilon,v>0 and t∈[0,T)t\in[0,T), define the perturbed policy πε,v\pi^{\varepsilon,v} as

|  |  |  |
| --- | --- | --- |
|  | πε,v(s,x)={v, if t≤s≤t+ε;π∗​(s,x)​ if s>t+ε,\pi^{\varepsilon,v}(s,x)=\left\{\begin{split}&v,\text{ if $t\leq s\leq t+\varepsilon$};\\ &\pi^{\*}(s,x)\text{ if $s>t+\varepsilon$},\end{split}\right. |  |

and it holds that

|  |  |  |
| --- | --- | --- |
|  | lim infε→0Jλ​(t,x;π∗)−Jλ​(t,x;πε,v)ε≥0,a.s.,\liminf\_{\varepsilon\rightarrow 0}\frac{J^{\lambda}(t,x;\pi^{\*})-J^{\lambda}(t,x;\pi^{\varepsilon,v})}{\varepsilon}\geq 0,a.s., |  |

for any initial state xx.

## 3 Extended HJB Equation for Regularized Problem

In this section, we derive the extended HJB equation for the regularized MV problem. To this end, we first define an operator ℒ\mathcal{L} as, for any smooth function φ\varphi,

|  |  |  |
| --- | --- | --- |
|  | (ℒ​φ)​(t,x):=12​tr(σ​σT​(t,x)​∂x​xφ​(t,x))+b​(t,x)​∂xφ​(t,x).(\mathcal{L}\varphi)(t,x):=\frac{1}{2}\mathop{\text{tr}}(\sigma\sigma^{T}(t,x)\partial\_{xx}\varphi(t,x))+b(t,x)\partial\_{x}\varphi(t,x). |  |

We have the following verification theorem.

###### Theorem 3.1.

For a Markovian strategy π∗=π∗​(t,x)\pi^{\*}=\pi^{\*}(t,x), let (Vλ,gλ)(V^{\lambda},g^{\lambda}) be a classical solution of the following parabolic system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂tVλ+ℒ​Vλ+λ​exp⁡(−Vλ+γ2​(f−gλ)2−fλ)−γ​|σ​∂xgλ|2=0,Vλ​(T,x)=f​(x),∂tgλ+ℒ​gλ−exp⁡(−Vλ+γ2​(f−gλ)2−fλ)​(gλ−f)=0,gλ​(T,x)=f​(x).\left\{\begin{split}&\partial\_{t}V^{\lambda}+\mathcal{L}V^{\lambda}+\lambda\exp(-\frac{V^{\lambda}+\frac{\gamma}{2}(f-g^{\lambda})^{2}-f}{\lambda})-\gamma|\sigma\partial\_{x}g^{\lambda}|^{2}=0,\ V^{\lambda}(T,x)=f(x),\\ &\partial\_{t}g^{\lambda}+\mathcal{L}g^{\lambda}-\exp(-\frac{V^{\lambda}+\frac{\gamma}{2}(f-g^{\lambda})^{2}-f}{\lambda})(g^{\lambda}-f)=0,\ g^{\lambda}(T,x)=f(x).\end{split}\right. |  | (3) |

Assume that VλV^{\lambda}, gλg^{\lambda}, their derivatives (up to first order in tt and second order in xx) and π\pi are all continuous with polynomial growth in xx, uniformly in tt. Then π∗\pi^{\*} is an equilibrium strategy if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | π∗​(t,x)=exp⁡(−Vλ+γ2​(f−gλ)2−fλ).\pi^{\*}(t,x)=\exp(-\frac{V^{\lambda}+\frac{\gamma}{2}(f-g^{\lambda})^{2}-f}{\lambda}). |  | (4) |

###### Proof.

The proof consists of two steps:

1. 1.

   We start by showing that gλ​(t,x)=𝔼t,x​[f​(Xτ)]g^{\lambda}(t,x)=\mathbb{E}\_{t,x}[f(X\_{\tau})] and Vλ​(t,x)=Jλ​(t,x;π∗)V^{\lambda}(t,x)=J^{\lambda}(t,x;\pi^{\*});
2. 2.

   In the second step, we prove that π∗\pi^{\*} is an equilibrium if and only if ([4](https://arxiv.org/html/2510.24128v1#S3.E4 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) holds.

For the first step, applying Itô formula to gλ​(s,Xs)​e−∫tsπ∗​(u,Xu)​𝑑ug^{\lambda}(s,X\_{s})e^{-\int\_{t}^{s}\pi^{\*}(u,X\_{u})du}, we have that

|  |  |  |
| --- | --- | --- |
|  | d​(gλ​(s,Xs)​e−∫tsπ∗​(u,Xu)​𝑑u)=e−∫tsπ∗​(u,Xu)​𝑑u​((∂t+ℒ)​gλ​(s,Xs)−π∗​(u,Xu)​gλ​(u,Xu))​d​s+σ​∂xgλ​(s,Xs)​e−∫tsπ∗​(u,Xu)​𝑑u​d​Ws.\begin{split}d\left(g^{\lambda}(s,X\_{s})e^{-\int\_{t}^{s}\pi^{\*}(u,X\_{u})du}\right)=&e^{-\int\_{t}^{s}\pi^{\*}(u,X\_{u})du}\left((\partial\_{t}+\mathcal{L})g^{\lambda}(s,X\_{s})-\pi^{\*}(u,X\_{u})g^{\lambda}(u,X\_{u})\right)ds\\ &+\sigma\partial\_{x}g^{\lambda}(s,X\_{s})e^{-\int\_{t}^{s}\pi^{\*}(u,X\_{u})du}dW\_{s}.\end{split} |  |

From the growth assumption on the derivative of gλg^{\lambda}, it holds that the stochastic integral is a martingale. Thus, taking conditional expectation, one can verify that

|  |  |  |
| --- | --- | --- |
|  | gλ​(t,x)=𝔼t,x​[∫tTf​(Xs)​π∗​(s,Xs)​e−∫tsπ∗​(u,Xu)​𝑑u​𝑑s+f​(XT)​e−∫tTπ∗​(u,Xu)​𝑑u],g^{\lambda}(t,x)=\mathbb{E}\_{t,x}\left[\int\_{t}^{T}f(X\_{s})\pi^{\*}(s,X\_{s})e^{-\int\_{t}^{s}\pi^{\*}(u,X\_{u})du}ds+f(X\_{T})e^{-\int\_{t}^{T}\pi^{\*}(u,X\_{u})du}\right], |  |

Then, define the function hλh^{\lambda} as hλ=Vλ−γ2​(gλ)2h^{\lambda}=V^{\lambda}-\frac{\gamma}{2}(g^{\lambda})^{2}. It is easy to see that hλh^{\lambda} solves

|  |  |  |
| --- | --- | --- |
|  | (∂t+ℒ)​hλ​(t,x)+π∗​(t,x)​(f−γ2​f2−hλ)​(t,x)+λ​H​(π∗)=0,hλ​(T,x)=f​(x)−γ2​f2​(x).(\partial\_{t}+\mathcal{L})h^{\lambda}(t,x)+\pi^{\*}(t,x)(f-\frac{\gamma}{2}f^{2}-h^{\lambda})(t,x)+\lambda H(\pi^{\*})=0,\ h^{\lambda}(T,x)=f(x)-\frac{\gamma}{2}f^{2}(x). |  |

Similarly, one can verify that

|  |  |  |
| --- | --- | --- |
|  | hλ​(t,x)=𝔼t,x​[∫tT{(f−γ2​f2)​(Xs)​π∗​(s,Xs)+λ​H​(πs)}​e−∫tsπ∗​(u,Xu)​𝑑u​𝑑s+f​(XT)​e−∫tTπ∗​(u,Xu)​𝑑u].h^{\lambda}(t,x)=\mathbb{E}\_{t,x}\left[\int\_{t}^{T}\left\{(f-\frac{\gamma}{2}f^{2})(X\_{s})\pi^{\*}(s,X\_{s})+\lambda H(\pi\_{s})\right\}e^{-\int\_{t}^{s}\pi^{\*}(u,X\_{u})du}ds+f(X\_{T})e^{-\int\_{t}^{T}\pi^{\*}(u,X\_{u})du}\right]. |  |

This implies that Jλ​(t,x;π∗)=hλ​(t,x)+γ2​gλ​(t,x)=Vλ​(t,x)J^{\lambda}(t,x;\pi^{\*})=h^{\lambda}(t,x)+\frac{\gamma}{2}g^{\lambda}(t,x)=V^{\lambda}(t,x).

Next, we prove the second step. For any tt, ε\varepsilon and vv, consider the perturbed strategy πε,v\pi^{\varepsilon,v}. Since πε,v\pi^{\varepsilon,v} coincides with π∗\pi^{\*} after time t+εt+\varepsilon, it holds that

|  |  |  |
| --- | --- | --- |
|  | Jλ​(t,x;πε,v)=𝔼t,x​[∫tt+ε{(f−γ2​f2)​(Xs)​v+λ​H​(v)}​e−v​(s−t)​𝑑s+hλ​(t+ε,Xt+ε)​e−v​ε]+γ2​(𝔼t,x​[∫tt+εf​(Xs)​v​e−v​(s−t)​𝑑s+gλ​(t+ε,Xt+ε)​e−v​ε])2.\begin{split}J^{\lambda}(t,x;\pi^{\varepsilon,v})=&\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}\left\{(f-\frac{\gamma}{2}f^{2})(X\_{s})v+\lambda H(v)\right\}e^{-v(s-t)}ds+h^{\lambda}(t+\varepsilon,X\_{t+\varepsilon})e^{-v\varepsilon}\right]\\ &+\frac{\gamma}{2}\left(\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}f(X\_{s})ve^{-v(s-t)}ds+g^{\lambda}(t+\varepsilon,X\_{t+\varepsilon})e^{-v\varepsilon}\right]\right)^{2}.\end{split} |  |

Applying Itô formula to gλ​(s,Xs)​e−v​(s−t)g^{\lambda}(s,X\_{s})e^{-v(s-t)} and taking conditional expectation, we get that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[gλ​(t+ε,Xt+ε)​e−v​ε]=gλ​(t,x)+𝔼t,x​[∫tt+ε(∂t+ℒ)​gλ​(s,Xs)​e−v​(s−t)−v​gλ​(s,Xs)​e−v​(s−t)​d​s].\begin{split}\mathbb{E}\_{t,x}[g^{\lambda}(t+\varepsilon,X\_{t+\varepsilon})e^{-v\varepsilon}]=g^{\lambda}(t,x)+\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}(\partial\_{t}+\mathcal{L})g^{\lambda}(s,X\_{s})e^{-v(s-t)}-vg^{\lambda}(s,X\_{s})e^{-v(s-t)}ds\right].\end{split} |  |

Then, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[∫tt+εf​(Xs)​v​e−v​(s−t)​𝑑s+gλ​(t+ε,Xt+ε)​e−v​ε]=gλ​(t,x)+𝔼t,x​[∫tt+ε(∂t+ℒ)​gλ​(s,Xs)​e−v​(s−t)+v​(f−gλ)​(s,Xs)​e−v​(s−t)​d​s]=gλ​(t,x)+((∂t+ℒ)​gλ​(t,x)+v​(f−gλ)​(t,x))​ε+o​(ε),\begin{split}&\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}f(X\_{s})ve^{-v(s-t)}ds+g^{\lambda}(t+\varepsilon,X\_{t+\varepsilon})e^{-v\varepsilon}\right]\\ =&g^{\lambda}(t,x)+\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}(\partial\_{t}+\mathcal{L})g^{\lambda}(s,X\_{s})e^{-v(s-t)}+v(f-g^{\lambda})(s,X\_{s})e^{-v(s-t)}ds\right]\\ =&g^{\lambda}(t,x)+\bigg((\partial\_{t}+\mathcal{L})g^{\lambda}(t,x)+v(f-g^{\lambda})(t,x)\bigg)\varepsilon+o(\varepsilon),\end{split} |  |

where the last equality is due to the fact that the related functions are continuous and XX also has continuous trajectories. Thus, we get that

|  |  |  |
| --- | --- | --- |
|  | (𝔼t,x​[∫tt+εf​(Xs)​v​e−v​(s−t)​𝑑s+gλ​(t+ε,Xt+ε)​e−v​ε])2=(gλ)2​(t,x)+2​gλ​(t,x)​((∂t+ℒ)​gλ​(t,x)+v​(f−gλ)​(t,x))​ε+o​(ε).\begin{split}&\left(\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}f(X\_{s})ve^{-v(s-t)}ds+g^{\lambda}(t+\varepsilon,X\_{t+\varepsilon})e^{-v\varepsilon}\right]\right)^{2}\\ =&(g^{\lambda})^{2}(t,x)+2g^{\lambda}(t,x)\bigg((\partial\_{t}+\mathcal{L})g^{\lambda}(t,x)+v(f-g^{\lambda})(t,x)\bigg)\varepsilon+o(\varepsilon).\end{split} |  |

With a similar argument, one also have that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[∫tt+ε{(f−γ2​f2)​(Xs)​v+λ​H​(v)}​e−v​(s−t)​𝑑s+hλ​(t+ε,Xt+ε)​e−v​ε]=hλ​(t,x)+((∂t+ℒ)​hλ​(t,x)+v​(f−γ2​f2−hλ)​(t,x)+λ​H​(v))​ε+o​(ε).\begin{split}&\mathbb{E}\_{t,x}\left[\int\_{t}^{t+\varepsilon}\left\{(f-\frac{\gamma}{2}f^{2})(X\_{s})v+\lambda H(v)\right\}e^{-v(s-t)}ds+h^{\lambda}(t+\varepsilon,X\_{t+\varepsilon})e^{-v\varepsilon}\right]\\ =&h^{\lambda}(t,x)+\bigg((\partial\_{t}+\mathcal{L})h^{\lambda}(t,x)+v(f-\frac{\gamma}{2}f^{2}-h^{\lambda})(t,x)+\lambda H(v)\bigg)\varepsilon+o(\varepsilon).\end{split} |  |

Combining these estimations together, we get that

|  |  |  |
| --- | --- | --- |
|  | Jλ​(t,x;πε,v)=hλ(t,x)+γ2(gλ)2(t,x)+((∂t+ℒ)hλ(t,x)+γgλ(t,x)(∂t+ℒ)gλ(t,x)+v(f−γ2f2−hλ+γgλf−γ(gλ)2)(t,x)+λH(v))ε+o(ε).\begin{split}J^{\lambda}(t,x;\pi^{\varepsilon,v})=&h^{\lambda}(t,x)+\frac{\gamma}{2}(g^{\lambda})^{2}(t,x)+\bigg((\partial\_{t}+\mathcal{L})h^{\lambda}(t,x)+\gamma g^{\lambda}(t,x)(\partial\_{t}+\mathcal{L})g^{\lambda}(t,x)\\ &+v(f-\frac{\gamma}{2}f^{2}-h^{\lambda}+\gamma g^{\lambda}f-\gamma(g^{\lambda})^{2})(t,x)+\lambda H(v)\bigg)\varepsilon+o(\varepsilon).\end{split} |  |

From the equations satisfied by gλg^{\lambda} and hλh^{\lambda}, also noting that Jλ​(t,x;π∗)=hλ​(t,x)+γ2​(gλ)2​(t,x)J^{\lambda}(t,x;\pi^{\*})=h^{\lambda}(t,x)+\frac{\gamma}{2}(g^{\lambda})^{2}(t,x), we derive that

|  |  |  |
| --- | --- | --- |
|  | limε→0Jλ​(t,x;π∗)−Jλ​(t,x;πε,v)ε=(v−π∗​(t,x))​(f−γ2​f2−hλ+γ​gλ​f−γ​(gλ)2)​(t,x)+λ​(H​(v)−H​(π∗​(t,x))).\begin{split}&\mathop{\text{lim}}\_{\varepsilon\rightarrow 0}\frac{J^{\lambda}(t,x;\pi^{\*})-J^{\lambda}(t,x;\pi^{\varepsilon,v})}{\varepsilon}\\ =&(v-\pi^{\*}(t,x))(f-\frac{\gamma}{2}f^{2}-h^{\lambda}+\gamma g^{\lambda}f-\gamma(g^{\lambda})^{2})(t,x)+\lambda(H(v)-H(\pi^{\*}(t,x))).\end{split} |  |

Hence, π∗\pi^{\*} is an equilibrium strategy if and only if

|  |  |  |
| --- | --- | --- |
|  | π∗​(t,x)∈argmaxv​v​(f−γ2​f2−hλ−γ​(gλ)2+γ​gλ​f)​(t,x)+λ​H​(v),\pi^{\*}(t,x)\in\text{argmax}\_{v}v(f-\frac{\gamma}{2}f^{2}-h^{\lambda}-\gamma(g^{\lambda})^{2}+\gamma g^{\lambda}f)(t,x)+\lambda H(v), |  |

which implies that π∗\pi^{\*} satisfies the optimality condition ([4](https://arxiv.org/html/2510.24128v1#S3.E4 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")).
∎

To our best knowledge, it is still a hard open problem to prove existence and/or uniqueness for solutions of an extended HJB system with a general assumption. In linear-quadratic mean-variance problem, one can reduce it to an ODE system and obtain a solution, see [[5](https://arxiv.org/html/2510.24128v1#bib.bib5)].
For the solvability of ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")), we give an existence result with additional technical assumptions on the coefficients and a small time interval.

###### Theorem 3.2.

In addition to Assumption [2.1](https://arxiv.org/html/2510.24128v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2 Mean Variance Stopping and its Relaxed Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"), we further assume that the coefficients bb,σ\sigma and ff are uniformly bounded. Then, for a sufficiently small TT, ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) admits a classical solution (Vλ,gλ)(V^{\lambda},g^{\lambda}).

###### Proof.

The solution is to be considered as a fixed point of a contraction mapping. For that purpose,
denote by 𝕂\mathbb{K} the Banach space C​([0,T],C1​(ℝd))C([0,T],C^{1}(\mathbb{R}^{d})) equipped with the norm ‖l‖𝕂=supt,x|l​(t,x)|+supt,x|∂xl​(t,x)|\|l\|\_{\mathbb{K}}=\sup\_{t,x}|l(t,x)|+\sup\_{t,x}|\partial\_{x}l(t,x)|. For any l∈𝕂l\in\mathbb{K}, define a mapping FF as k=F​(l)k=F(l) is the solution of the following system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂tv+ℒ​v+λ​exp⁡(−v+γ2​(f−l)2−fλ)−γ​|σ​∂xl|2=0,v​(T,x)=f,∂tk+ℒ​k−exp⁡(−v+γ2​(f−l)2−fλ)​(k−f)=0,k​(T,x)=f.\left\{\begin{split}&\partial\_{t}v+\mathcal{L}v+\lambda\exp(-\frac{v+\frac{\gamma}{2}(f-l)^{2}-f}{\lambda})-\gamma|\sigma\partial\_{x}l|^{2}=0,v(T,x)=f,\\ &\partial\_{t}k+\mathcal{L}k-\exp(-\frac{v+\frac{\gamma}{2}(f-l)^{2}-f}{\lambda})(k-f)=0,k(T,x)=f.\end{split}\right. |  | (5) |

Let Bm​(0)B\_{m}(0) be the ball in 𝕂\mathbb{K} centered at 0 with radius m=‖f‖∞+‖∂xf‖∞+1m=\|f\|\_{\infty}+\|\partial\_{x}f\|\_{\infty}+1. We are to show that, for a sufficiently small TT, FF is a contraction from Bm​(0)B\_{m}(0) into itself and, thus, admits a fixed point, which would be the solution of ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")).

The proof consists of several steps:

Step 11. Well-posedness of first equation. Choose any N>0N>0, let ξN\xi\_{N} be a smooth cutoff function such that ξN​(x)=x\xi\_{N}(x)=x, for x≤Nx\leq N; and ξN​(x)=N+1\xi\_{N}(x)=N+1, for x≥N+1x\geq N+1. Consider the following equation

|  |  |  |
| --- | --- | --- |
|  | ∂tv+ℒ​v+λ​exp⁡(ξN​(−v+γ2​(f−l)2−fλ))−γ​|σ​∂xl|2=0,v​(T,x)=f.\partial\_{t}v+\mathcal{L}v+\lambda\exp(\xi\_{N}(-\frac{v+\frac{\gamma}{2}(f-l)^{2}-f}{\lambda}))-\gamma|\sigma\partial\_{x}l|^{2}=0,v(T,x)=f. |  |

Noting that the third term is a bounded Lipschitz function of vv, it admits a solution vv. Lemma [B.1](https://arxiv.org/html/2510.24128v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B A Key Lemma ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") yields that

|  |  |  |
| --- | --- | --- |
|  | −C​(‖f‖∞+λ​exp⁡(N+1λ))≤v≤C​(T​m2+‖f‖∞).-C(\|f\|\_{\infty}+\lambda\exp(\frac{N+1}{\lambda}))\leq v\leq C(Tm^{2}+\|f\|\_{\infty}). |  |

Let us give a refined lower bound estimation independent of NN, which implies that vv solves the first equation in ([5](https://arxiv.org/html/2510.24128v1#S3.E5 "In 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) when NN is sufficiently large.
Denote by ψ​(x)=1+|x|2\psi(x)=\sqrt{1+|x|^{2}}. One can compute that

|  |  |  |
| --- | --- | --- |
|  | Dx​ψ=x1+|x|2​ and ​Dx2​ψ=11+|x|2​I−1(1+|x|2)12​x⊗x,D\_{x}\psi=\frac{x}{\sqrt{1+|x|^{2}}}\text{ and }D^{2}\_{x}\psi=\frac{1}{\sqrt{1+|x|^{2}}}I-\frac{1}{\left(1+|x|^{2}\right)^{\frac{1}{2}}}x\otimes x, |  |

and, thus, ℒ​ψ≤C\mathcal{L}\psi\leq C. Since vv is a bounded function, it holds that, for any ε>0\varepsilon>0, v+ε​ψv+\varepsilon\psi attains a minimum at some point (t∗,x∗)(t^{\*},x^{\*}). If t∗=Tt^{\*}=T, then the terminal condition implies that

|  |  |  |
| --- | --- | --- |
|  | v≥−‖f‖∞−ε​ψ.v\geq-\|f\|\_{\infty}-\varepsilon\psi. |  |

If t∗<Tt^{\*}<T, it holds that, at (t∗,x∗)(t^{\*},x^{\*}),

|  |  |  |
| --- | --- | --- |
|  | Dx2​v≥−ε​Dx2​ψ,Dx​v=−ε​Dx​ψ, and ​∂tv≥0.D^{2}\_{x}v\geq-\varepsilon D^{2}\_{x}\psi,D\_{x}v=-\varepsilon D\_{x}\psi,\text{ and }\partial\_{t}v\geq 0. |  |

This yields that (∂t+ℒ)​v​(t∗,x∗)≥−ε​ℒ​ψ≥−C​ε(\partial\_{t}+\mathcal{L})v(t^{\*},x^{\*})\geq-\varepsilon\mathcal{L}\psi\geq-C\varepsilon. On the other hand, we have

|  |  |  |
| --- | --- | --- |
|  | (∂t+ℒ)​v=γ​|σ​Dx​l|2−λ​exp⁡(ξN​(−v+γ2​(f−l)2−fλ)).(\partial\_{t}+\mathcal{L})v=\gamma|\sigma D\_{x}l|^{2}-\lambda\exp(\xi\_{N}(-\frac{v+\frac{\gamma}{2}(f-l)^{2}-f}{\lambda})). |  |

Combining these two inequalities, we get that

|  |  |  |
| --- | --- | --- |
|  | λ​exp⁡(ξN​(−v+γ2​(f−l)2−fλ))≤γ​|σ​Dx​l|2+C​ε,\lambda\exp(\xi\_{N}(-\frac{v+\frac{\gamma}{2}(f-l)^{2}-f}{\lambda}))\leq\gamma|\sigma D\_{x}l|^{2}+C\varepsilon, |  |

or, equivalently,

|  |  |  |
| --- | --- | --- |
|  | ξN​(f−v−γ2​(f−l)2λ)≤log⁡γ​|σ​∂xl|2+C​ελ.\xi\_{N}(\frac{f-v-\frac{\gamma}{2}(f-l)^{2}}{\lambda})\ \leq\log\frac{\gamma|\sigma\partial\_{x}l|^{2}+C\varepsilon}{\lambda}. |  |

This implies that, at (r∗,x∗)(r^{\*},x^{\*}),

|  |  |  |
| --- | --- | --- |
|  | v≥f−λ​log⁡γ​|σ​∂xl|2+C​ελ.v\geq f-\lambda\log\frac{\gamma|\sigma\partial\_{x}l|^{2}+C\varepsilon}{\lambda}. |  |

Thus, we have a lower bound estimation

|  |  |  |
| --- | --- | --- |
|  | v≥−‖f‖∞+λ​log⁡γ​C​m2+C​ελ−ε​ψ.v\geq-\|f\|\_{\infty}+\lambda\log\frac{\gamma Cm^{2}+C\varepsilon}{\lambda}-\varepsilon\psi. |  |

Letting ε\varepsilon go to 0, we finally get that

|  |  |  |
| --- | --- | --- |
|  | v≥−‖f‖∞+λ​log⁡γ​C​m2λ.v\geq-\|f\|\_{\infty}+\lambda\log\frac{\gamma Cm^{2}}{\lambda}. |  |

Step 2. Bound and derivative estimations for kk. Note that the second estimation of ([5](https://arxiv.org/html/2510.24128v1#S3.E5 "In 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) is just a linear equation of kk. The well-posedness is straight-forward and one obtains the following bound estimation from Lemma [B.1](https://arxiv.org/html/2510.24128v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B A Key Lemma ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")

|  |  |  |
| --- | --- | --- |
|  | ‖k‖∞≤‖f‖∞.\|k\|\_{\infty}\leq\|f\|\_{\infty}. |  |

To give estimation of the derivative, note that, from lower bound estimation for VV in the first step, it holds that

|  |  |  |
| --- | --- | --- |
|  | exp⁡(−v+γ2​(f−l)2−fλ)≤(γ​C​m2λ)Cλ​(1+‖f‖∞2+m2).\exp(-\frac{v+\frac{\gamma}{2}(f-l)^{2}-f}{\lambda})\leq(\frac{\gamma Cm^{2}}{\lambda})^{\frac{C}{\lambda}(1+\|f\|^{2}\_{\infty}+m^{2})}. |  |

Hence, using Lemma [B.1](https://arxiv.org/html/2510.24128v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B A Key Lemma ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") again, we have that

|  |  |  |
| --- | --- | --- |
|  | ‖∂xk‖∞≤(1+T)​‖∂xf‖∞+C​(T+T)​(γ​C​m2λ)Cλ​(1+‖f‖∞2+m2).\|\partial\_{x}k\|\_{\infty}\leq(1+\sqrt{T})\|\partial\_{x}f\|\_{\infty}+C(\sqrt{T}+T)(\frac{\gamma Cm^{2}}{\lambda})^{\frac{C}{\lambda}(1+\|f\|^{2}\_{\infty}+m^{2})}. |  |

Then, for a sufficiently small TT, FF is mapping from Bm​(0)B\_{m}(0) into itself.

Step 3. Contraction of the mapping FF.
For any hi∈Bm​(0)h\_{i}\in B\_{m}(0) with i=1,2i=1,2, let (vi,ki)(v\_{i},k\_{i}) be the related solutions of ([5](https://arxiv.org/html/2510.24128v1#S3.E5 "In 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). Denote by δ​v=v1−v2\delta v=v\_{1}-v\_{2}, δ​k=k1−k2\delta k=k\_{1}-k\_{2}, and δ​l=l1−l2\delta l=l\_{1}-l\_{2}. Then, we that (δ​v,δ​k)(\delta v,\delta k) satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(∂t+ℒ)​δ​v−δ​e​(δ​v−γ2​(2​f−l1−l2)​δ​l)−γ​(|σ​∂xl1|2−|σ​∂xl2|2)=0,δ​v​(T,x)=0,(∂t+ℒ)​δ​k−exp⁡(−v1+γ2​(f−l1)2−fλ)​δ​k+(k2−f)​δ​e​δ​v−γ2​(2​f−l1−l2)​δ​lλ=0,δ​k​(T,x)=0.\left\{\begin{split}&(\partial\_{t}+\mathcal{L})\delta v-\delta e(\delta v-\frac{\gamma}{2}(2f-l\_{1}-l\_{2})\delta l)-\gamma(|\sigma\partial\_{x}l\_{1}|^{2}-|\sigma\partial\_{x}l\_{2}|^{2})=0,\delta v(T,x)=0,\\ &(\partial\_{t}+\mathcal{L})\delta k-\exp(-\frac{v\_{1}+\frac{\gamma}{2}(f-l\_{1})^{2}-f}{\lambda})\delta k+(k\_{2}-f)\delta e\frac{\delta v-\frac{\gamma}{2}(2f-l\_{1}-l\_{2})\delta l}{\lambda}=0,\delta k(T,x)=0.\end{split}\right. |  | (6) |

with

|  |  |  |
| --- | --- | --- |
|  | δ​e=∫01exp⁡(−v1+γ2​(f−l1)2−f+s​(δ​v−γ2​(2​f−l1−l2)​δ​l)λ)​𝑑s.\delta e=\int\_{0}^{1}\exp(-\frac{v\_{1}+\frac{\gamma}{2}(f-l\_{1})^{2}-f+s(\delta v-\frac{\gamma}{2}(2f-l\_{1}-l\_{2})\delta l)}{\lambda})ds. |  |

From the estimation in previous step, we know that the related functions vi,kiv\_{i},k\_{i} and hih\_{i} are uniformly bounded. Thus, δ​e\delta e is a bounded function. Moreover, one gets that

|  |  |  |
| --- | --- | --- |
|  | ‖δ​e​γ2​(2​f−l1−l2)​δ​l‖∞≤γ2​‖δ​e​(2​f−l1−l2)‖∞​‖δ​l‖∞≤C​‖δ​l‖∞,\|\delta e\frac{\gamma}{2}(2f-l\_{1}-l\_{2})\delta l\|\_{\infty}\leq\frac{\gamma}{2}\|\delta e(2f-l\_{1}-l\_{2})\|\_{\infty}\|\delta l\|\_{\infty}\leq C\|\delta l\|\_{\infty}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ‖|σ​Dx​l1|2−|σ​Dx​l2|2‖∞≤C​‖σ​Dx​l1+σ​Dx​l2‖∞​‖σ​Dx​l1−σ​Dx​l2‖∞≤C​‖σ​Dx​l1−σ​Dx​l2‖∞.\||\sigma D\_{x}l\_{1}|^{2}-|\sigma D\_{x}l\_{2}|^{2}\|\_{\infty}\leq C\|\sigma D\_{x}l\_{1}+\sigma D\_{x}l\_{2}\|\_{\infty}\|\sigma D\_{x}l\_{1}-\sigma D\_{x}l\_{2}\|\_{\infty}\leq C\|\sigma D\_{x}l\_{1}-\sigma D\_{x}l\_{2}\|\_{\infty}. |  |

Then, using Lemma [B.1](https://arxiv.org/html/2510.24128v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B A Key Lemma ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") again, we have that there exists a constant CC depending on the coefficients, mm and λ\lambda such that

|  |  |  |
| --- | --- | --- |
|  | ∥δv∥∞≤CT(∥δl∥∞+∥∂xδl∥∞.\|\delta v\|\_{\infty}\leq CT(\|\delta l\|\_{\infty}+\|\partial\_{x}\delta l\|\_{\infty}. |  |

Furthermore, with a similar argument,

|  |  |  |
| --- | --- | --- |
|  | ‖δ​k‖∞≤C​T​‖(k2−f)​δ​e​δ​v−γ2​(2​f−l1−l2)​δ​lλ‖∞≤C​T​(‖δ​v‖∞+‖δ​l‖∞).,\|\delta k\|\_{\infty}\leq CT\|(k\_{2}-f)\delta e\frac{\delta v-\frac{\gamma}{2}(2f-l\_{1}-l\_{2})\delta l}{\lambda}\|\_{\infty}\leq CT(\|\delta v\|\_{\infty}+\|\delta l\|\_{\infty})., |  |

and

|  |  |  |
| --- | --- | --- |
|  | ‖∂xδ​k‖∞≤C​(T+T)​(‖(k2−f)​δ​e​δ​v−γ2​(2​f−l1−l2)​δ​lλ‖∞+‖exp⁡(−v1+γ2​(f−l1)2−fλ)​δ​k‖∞)≤C​(T+T)​(‖δ​v‖∞+‖δ​l‖∞+‖δ​k‖∞).\begin{split}\|\partial\_{x}\delta k\|\_{\infty}\leq&C(\sqrt{T}+T)(\|(k\_{2}-f)\delta e\frac{\delta v-\frac{\gamma}{2}(2f-l\_{1}-l\_{2})\delta l}{\lambda}\|\_{\infty}+\|\exp(-\frac{v\_{1}+\frac{\gamma}{2}(f-l\_{1})^{2}-f}{\lambda})\delta k\|\_{\infty})\\ \leq&C(\sqrt{T}+T)(\|\delta v\|\_{\infty}+\|\delta l\|\_{\infty}+\|\delta k\|\_{\infty}).\end{split} |  |

Combining these estimations, we see that FF is a contraction for a sufficiently small TT.
∎

## 4 Extended HJB Equation for Original Problem

For the optimal stopping problem, i.e., γ=0\gamma=0, [[9](https://arxiv.org/html/2510.24128v1#bib.bib9)] proves that the first equation in ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) converges to the variational inequality satisfied by the value function. For MV stopping problem, we would like follow the same procedure. Unfortunately, at present, we can only formally deduce the limiting equation. Below is a brief introduction. Assume that
(Vλ,gλ)(V^{\lambda},g^{\lambda}) converge to some functions (V,g)(V,g) when λ\lambda goes to 0 Then, it is natural to conjecture that

|  |  |  |
| --- | --- | --- |
|  | ∂tV+ℒ​V−γ​|σ​∂xg|2=limλ→0∂tVλ+ℒ​Vλ−γ​|σ​∂xgλ|2≤0.\partial\_{t}V+\mathcal{L}V-\gamma\left|\sigma\partial\_{x}g\right|^{2}=\lim\_{\lambda\rightarrow 0}\partial\_{t}V^{\lambda}+\mathcal{L}V^{\lambda}-\gamma\left|\sigma\partial\_{x}g^{\lambda}\right|^{2}\leq 0. |  |

If ∂tVλ+ℒ​Vλ\partial\_{t}V^{\lambda}+\mathcal{L}V^{\lambda} and ∂xgλ\partial\_{x}g^{\lambda} are bounded uniformly in λ\lambda, then so is λ​exp⁡(−Vλ+γ2​(f−gλ)2−fλ)\lambda\exp(-\frac{V^{\lambda}+\frac{\gamma}{2}(f-g^{\lambda})^{2}-f}{\lambda}). This suggests that V+γ2​(f−g)2≥fV+\frac{\gamma}{2}(f-g)^{2}\geq f. Moreover, if V+γ2​(f−g)2>fV+\frac{\gamma}{2}(f-g)^{2}>f, one has exp⁡(−Vλ+γ2​(f−gλ)2−fλ)\exp(-\frac{V^{\lambda}+\frac{\gamma}{2}(f-g^{\lambda})^{2}-f}{\lambda}) converges to 0, which implies ∂tV+ℒ​V−γ​|σ​∂xg|2=0\partial\_{t}V+\mathcal{L}V-\gamma\left|\sigma\partial\_{x}g\right|^{2}=0, and ∂tg+ℒ​g=0\partial\_{t}g+\mathcal{L}g=0. From ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")), it is not clear what is satisfied by gg on the set {V+γ2​(f−g)2=f}\{V+\frac{\gamma}{2}(f-g)^{2}=f\}. But, from the probabilistic representation of gλg^{\lambda}, one also guess that g​(t,x)=𝔼t,x​[f​(Xτ)]g(t,x)=\mathbb{E}\_{t,x}[f(X\_{\tau})] for a stopping time τ\tau. If τ\tau is the hitting time of the set {V+γ2​(f−g)2=f}\{V+\frac{\gamma}{2}(f-g)^{2}=f\}, Then, gg should equal to ff on that set. In summary, ([3](https://arxiv.org/html/2510.24128v1#S3.E3 "In Theorem 3.1. ‣ 3 Extended HJB Equation for Regularized Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) formally converges to the following system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {min⁡{−(∂tV+ℒ​V−γ​|σ​∂xg|2),V+γ2​(f−g)2−f}=0,V​(T,x)=f,∂tg+ℒ​g=0, on {V+γ2​(f−g)2>f},g=f​ on {V+γ2​(f−g)2=f},g​(T,x)=f​(x).\left\{\begin{split}&\min\left\{-\left(\partial\_{t}V+\mathcal{L}V-\gamma\left|\sigma\partial\_{x}g\right|^{2}\right),V+\frac{\gamma}{2}(f-g)^{2}-f\right\}=0,V(T,x)=f,\\ &\partial\_{t}g+\mathcal{L}g=0,\text{ on $\{V+\frac{\gamma}{2}(f-g)^{2}>f\}$},\\ &g=f\text{ on $\{V+\frac{\gamma}{2}(f-g)^{2}=f\}$},g(T,x)=f(x).\end{split}\right. |  | (7) |

Now, let us assume that the above system admits a pair of solution (V,g)(V,g). The means that (V,g)(V,g) is a pair of continuous functions, second-order continuous differentiable in the region {V+γ2​(f−g)2>f}\{V+\frac{\gamma}{2}(f-g)^{2}>f\} and satisfies ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). Define the set

|  |  |  |
| --- | --- | --- |
|  | 𝒞={(t,x)|V+γ2​(f−g)2>f}.\mathcal{C}=\{(t,x)|V+\frac{\gamma}{2}(f-g)^{2}>f\}. |  |

Construct the stopping time τ𝒞\tau\_{\mathcal{C}} as

|  |  |  |
| --- | --- | --- |
|  | τ𝒞=inf{s≥t|(s,Xs)∉𝒞}.\tau\_{\mathcal{C}}=\inf\{s\geq t|(s,X\_{s})\notin\mathcal{C}\}. |  |

One can verify that

|  |  |  |
| --- | --- | --- |
|  | V​(t,x)=𝔼t,x​[f​(Xτ𝒞)]−γ2​Vart,x​[f​(Xτ𝒞)], and ​g​(t,x)=𝔼t,x​[f​(Xτ𝒞)].V(t,x)=\mathbb{E}\_{t,x}\left[f(X\_{\tau\_{\mathcal{C}}})\right]-\frac{\gamma}{2}\text{Var}\_{t,x}\left[f(X\_{\tau\_{\mathcal{C}}})\right],\text{ and }g(t,x)=\mathbb{E}\_{t,x}\left[f(X\_{\tau\_{\mathcal{C}}})\right]. |  |

Moreover, we also define

|  |  |  |
| --- | --- | --- |
|  | h​(t,x):=V​(t,x)−γ2​g2​(t,x)=𝔼t,x​[(f−γ2​f2)​(Xτ𝒞)].h(t,x):=V(t,x)-\frac{\gamma}{2}g^{2}(t,x)=\mathbb{E}\_{t,x}\left[(f-\frac{\gamma}{2}f^{2})(X\_{\tau\_{\mathcal{C}}})\right]. |  |

Next, we prove that these functions characterize a stopping policy that is an equilibrium in some sense. Before that, let us first introduce some definitions. For any (t,x)∈ℝ×ℝn(t,x)\in\mathbb{R}\times\mathbb{R}^{n} and r>0r>0, the parabolic cylinder Q​(t,x;r)Q(t,x;r) is defined as333The definition of parabolic cylinders is different from that in text books of parabolic PDEs, see [[13](https://arxiv.org/html/2510.24128v1#bib.bib13)]. The reason is that we consider PDEs with terminal conditions instead of initial conditions.

|  |  |  |
| --- | --- | --- |
|  | Q​(t,x;r):={(s,y)∈ℝ×ℝn|max⁡{|x−y|,(s−t)12}≤r,s≥t}.Q(t,x;r):=\{(s,y)\in\mathbb{R}\times\mathbb{R}^{n}|\max\{|x-y|,(s-t)^{\frac{1}{2}}\}\leq r,s\geq t\}. |  |

For any set Ω\Omega, the parabolic boundary 𝒫​Ω\mathcal{P}\Omega is defined as the set of all points (t,x)∈Ω¯(t,x)\in\bar{\Omega} such that for any ε>0\varepsilon>0, Q​(t,x;ε)Q(t,x;\varepsilon) contains points not in Ω\Omega. Finally, note that, since 𝒞\mathcal{C} is a open set, for any (t,x)∈𝒞(t,x)\in\mathcal{C}, there exists ε>0\varepsilon>0 such that Q​(t,x;ε)∈𝒞Q(t,x;\varepsilon)\in\mathcal{C}.

The notion of equilibrium strategy is similar to that used in [[7](https://arxiv.org/html/2510.24128v1#bib.bib7)].
For any v≥0v\geq 0, let NvN^{v} be a Poisson point process independent of the Brownian motion WW. Its first jump time after tt is denoted as τv\tau^{v}, i.e.,

|  |  |  |
| --- | --- | --- |
|  | τv=inf{s≥t|Ns−Nt=1}.\tau^{v}=\inf\left\{s\geq t|N\_{s}-N\_{t}=1\right\}. |  |

For any ε\varepsilon, define two stopping time

|  |  |  |
| --- | --- | --- |
|  | τε=inf{s≥t||Xs−Xt|≥ε}∧(t+ε)∧T,\tau^{\varepsilon}=\inf\left\{s\geq t||X\_{s}-X\_{t}|\geq\varepsilon\right\}\wedge(t+\varepsilon)\wedge T, |  |

and

|  |  |  |
| --- | --- | --- |
|  | τ~𝒞=inf{s≥τε|(s,Xs)∉𝒞}.\tilde{\tau}\_{\mathcal{C}}=\inf\left\{s\geq\tau^{\varepsilon}|(s,X\_{s})\notin\mathcal{C}\right\}. |  |

The perturbation τ𝒞ε,v\tau^{\varepsilon,v}\_{\mathcal{C}} of τ𝒞\tau\_{\mathcal{C}} is defined as,

|  |  |  |
| --- | --- | --- |
|  | τ𝒞ε,v=1{τv≤τε}​τv+1{τv>τε}​τ~𝒞.\tau\_{\mathcal{C}}^{\varepsilon,v}=1\_{\{\tau^{v}\leq\tau^{\varepsilon}\}}\tau^{v}+1\_{\{\tau^{v}>\tau^{\varepsilon}\}}\tilde{\tau}\_{\mathcal{C}}. |  |

###### Theorem 4.1.

Assume that there exists a solution (V,g)(V,g) of ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) such that the functions and their derivatives are polynomial-growth w.r.t. xx uniformly in tt. For any (t,x)∈𝒞∪(𝒞c/𝒫​𝒞c)(t,x)\in\mathcal{C}\cup(\mathcal{C}^{c}/\mathcal{P}\mathcal{C}^{c}), it holds that

|  |  |  |
| --- | --- | --- |
|  | lim infε→0J​(t,x;τ𝒞)−J​(t,x;τ𝒞ε,v)𝔼t,x​[τε−t]≥0.\liminf\_{\varepsilon\to 0}\frac{J(t,x;\tau\_{\mathcal{C}})-J(t,x;\tau\_{\mathcal{C}}^{\varepsilon,v})}{\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]}\geq 0. |  |

###### Proof.

From the definition of τ𝒞ε,v\tau\_{\mathcal{C}}^{\varepsilon,v}, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[f​(Xτ𝒞ε,v)]=𝔼t,x​[∫tτεf​(Xs)​v​e−v​(s−t)​𝑑s+f​(Xτ~𝒞)​e−v​(τε−t)]=𝔼t,x​[∫tτεf​(Xs)​v​e−v​(s−t)​𝑑s+g​(τε,Xτε)​e−v​(τε−t)].\begin{split}&\mathbb{E}\_{t,x}\left[f(X\_{\tau\_{\mathcal{C}}^{\varepsilon,v}})\right]\\ =&\mathbb{E}\_{t,x}\left[\int\_{t}^{\tau^{\varepsilon}}f(X\_{s})ve^{-v(s-t)}ds+f(X\_{\tilde{\tau}\_{\mathcal{C}}})e^{-v(\tau^{\varepsilon}-t)}\right]\\ =&\mathbb{E}\_{t,x}\left[\int\_{t}^{\tau^{\varepsilon}}f(X\_{s})ve^{-v(s-t)}ds+g(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})e^{-v(\tau^{\varepsilon}-t)}\right].\end{split} |  |

Note that, for sufficiently small ε\varepsilon, XsX\_{s} stays in 𝒞\mathcal{C} or 𝒞c\mathcal{C}^{c} for s∈[t,τε]s\in[t,\tau^{\varepsilon}] as we assume that (t,x)∈𝒞∪(𝒞c/𝒫​𝒞c)(t,x)\in\mathcal{C}\cup(\mathcal{C}^{c}/\mathcal{P}\mathcal{C}^{c}). Thus, one can apply Itô formula to get that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[g​(τε,Xτε)​e−v​τε]=g​(t,x)+𝔼​[∫tτε(∂t+ℒ)​g​(s,Xs)​e−v​(s−t)−v​g​(s,Xs)​e−v​(s−t)​d​s].\begin{split}&\mathbb{E}\_{t,x}\left[g(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})e^{-v\tau^{\varepsilon}}\right]\\ =&g(t,x)+\mathbb{E}\left[\int\_{t}^{\tau^{\varepsilon}}(\partial\_{t}+\mathcal{L})g(s,X\_{s})e^{-v(s-t)}-vg(s,X\_{s})e^{-v(s-t)}ds\right].\end{split} |  |

Then, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[f​(Xτ𝒞ε,v)]=g​(t,x)+((∂t+ℒ)​g​(t,x)+v​(f−g)​(t,x))​𝔼​[τε−t]+o​(𝔼​[τε−t]),\begin{split}&\mathbb{E}\_{t,x}\left[f(X\_{\tau^{\varepsilon,v}\_{\mathcal{C}}})\right]\\ =&g(t,x)+\left((\partial\_{t}+\mathcal{L})g(t,x)+v(f-g)(t,x)\right)\mathbb{E}\left[\tau^{\varepsilon}-t\right]+o(\mathbb{E}\left[\tau^{\varepsilon}-t\right]),\end{split} |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | (𝔼t,x​[f​(Xτ𝒞ε,v)])2=g2​(t,x)+2​g​(t,x)​((∂t+ℒ)​g​(t,x)+v​(f−g)​(t,x))​𝔼​[τε−t]+o​(𝔼​[τε−t]).\begin{split}&\left(\mathbb{E}\_{t,x}\left[f(X\_{\tau^{\varepsilon,v}\_{\mathcal{C}}})\right]\right)^{2}\\ =&g^{2}(t,x)+2g(t,x)\left((\partial\_{t}+\mathcal{L})g(t,x)+v(f-g)(t,x)\right)\mathbb{E}\left[\tau^{\varepsilon}-t\right]+o(\mathbb{E}\left[\tau^{\varepsilon}-t\right]).\end{split} |  |

Similarly, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[(f−γ2​f2)​(Xτ𝒞ε,v)]=h​(t,x)+((∂t+ℒ)​(h)+v​(f−γ2​f2−h))​𝔼​[τε−t]+o​(𝔼​[τε−t]).\begin{split}&\mathbb{E}\_{t,x}\left[(f-\frac{\gamma}{2}f^{2})(X\_{\tau^{\varepsilon,v}\_{\mathcal{C}}})\right]\\ =&h(t,x)+\left((\partial\_{t}+\mathcal{L})(h)+v(f-\frac{\gamma}{2}f^{2}-h)\right)\mathbb{E}\left[\tau^{\varepsilon}-t\right]+o(\mathbb{E}\left[\tau^{\varepsilon}-t\right]).\end{split} |  |

Hence, recalling that h=V−γ2​g2h=V-\frac{\gamma}{2}g^{2},

|  |  |  |
| --- | --- | --- |
|  | J​(t,x;τ𝒞ε,v)−J​(t,x;τ𝒞)=((∂t+ℒ)​h+γ​g​(∂t+ℒ)​g+v​(f−(V+γ2​(f−g)2)))​𝔼​[τε−t]+o​(𝔼​[τε−t])=((∂t+ℒ)​V−γ​|σ​∂xg|2+v​(f−(V+γ2​(f−g)2)))​𝔼​[τε−t]+o​(𝔼​[τε−t]).\begin{split}&J(t,x;\tau\_{\mathcal{C}}^{\varepsilon,v})-J(t,x;\tau\_{\mathcal{C}})\\ =&((\partial\_{t}+\mathcal{L})h+\gamma g(\partial\_{t}+\mathcal{L})g+v(f-(V+\frac{\gamma}{2}(f-g)^{2})))\mathbb{E}[\tau^{\varepsilon}-t]+o(\mathbb{E}[\tau^{\varepsilon}-t])\\ =&((\partial\_{t}+\mathcal{L})V-\gamma|\sigma\partial\_{x}g|^{2}+v(f-(V+\frac{\gamma}{2}(f-g)^{2})))\mathbb{E}[\tau^{\varepsilon}-t]+o(\mathbb{E}[\tau^{\varepsilon}-t]).\end{split} |  |

The first equation in ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) implies the desired result.
∎

For the case (t,x)∈𝒫​𝒞c\{T}×ℝ(t,x)\in\mathcal{P}\mathcal{C}^{c}\backslash\{T\}\times\mathbb{R}, it turns out to be a very subtle problem. Thus, we focus on one dimensional case, i.e., x∈ℝx\in\mathbb{R} and assume that the free boundary 𝒫​𝒞c\{T}×ℝ\mathcal{P}\mathcal{C}^{c}\backslash\{T\}\times\mathbb{R} is locally Lipschitz continuous with respect to time tt. More precisely, there exists a small ball Q​(t,x;r)Q(t,x;r) and a Lipschitz continuous curve cc and r>0r>0 such that 𝒞​⋂Q​(t,x;r)={(s,y)|t≤s≤t+r12,|y−x|≤r,y≥c​(s)}\mathcal{C}\bigcap Q(t,x;r)=\{(s,y)|t\leq s\leq t+r^{\frac{1}{2}},|y-x|\leq r,y\geq c(s)\}.

###### Theorem 4.2.

In addition to the assumption in Theorem [4.1](https://arxiv.org/html/2510.24128v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") and locally Lipschitz assumption on the free boundary, we further assume
that VV is C1C^{1} in Q​(t,x;r)Q(t,x;r). If it holds that, for (t,x)∈𝒫​𝒞c\{T}×ℝ(t,x)\in\mathcal{P}\mathcal{C}^{c}\backslash\{T\}\times\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂t+ℒ)​V​(t,x+)+(∂t+ℒ)​V​(t,x−)≤γ​σ2​(t,x)​(∂xg​(t,x+)+∂xg​(t,x−)2)2,(\partial\_{t}+\mathcal{L})V(t,x+)+(\partial\_{t}+\mathcal{L})V(t,x-)\leq\gamma\sigma^{2}(t,x)\left(\frac{\partial\_{x}g(t,x+)+\partial\_{x}g(t,x-)}{2}\right)^{2}, |  | (8) |

then we have

|  |  |  |
| --- | --- | --- |
|  | lim infε→0J​(t,x;τ𝒞)−J​(t,x;τ𝒞ε,v)𝔼t,x​[τε−t]≥0.\liminf\_{\varepsilon\rightarrow 0}\frac{J(t,x;\tau\_{\mathcal{C}})-J(t,x;\tau\_{\mathcal{C}}^{\varepsilon,v})}{\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]}\geq 0. |  |

###### Proof.

From Itô-Tanaka formula (see [[15](https://arxiv.org/html/2510.24128v1#bib.bib15)]), one can get that

|  |  |  |
| --- | --- | --- |
|  | g(τε,Xτε)e−(τε−t)=g(t,x)+∫tτε12((∂t+ℒ)g(s,Xs+)e−v​(s−t)−vg(s,Xs+)e−v​(s−t)+(∂t+ℒ)g(s,Xs−)e−v​(s−t)−vg(s,Xs−)e−v​(s−t))1{Xs≠c​(s)}ds+∫tτε12​σ​(∂xg​(s,Xs+)+∂xg​(s,Xs−))​e−v​(t−s)​𝑑Ws+12​∫tτε(∂xg​(s,Xs+)−∂xg​(s,Xs−))​e−v​(s−t)​1{Xs=c​(s)}​𝑑lsc,\begin{split}&g(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})e^{-(\tau^{\varepsilon}-t)}=g(t,x)+\int\_{t}^{\tau^{\varepsilon}}\frac{1}{2}\bigg((\partial\_{t}+\mathcal{L})g(s,X\_{s}+)e^{-v(s-t)}-vg(s,X\_{s}+)e^{-v(s-t)}\\ &+(\partial\_{t}+\mathcal{L})g(s,X\_{s}-)e^{-v(s-t)}-vg(s,X\_{s}-)e^{-v(s-t)}\bigg)1\_{\{X\_{s}\neq c(s)\}}ds\\ &+\int\_{t}^{\tau^{\varepsilon}}\frac{1}{2}\sigma(\partial\_{x}g(s,X\_{s}+)+\partial\_{x}g(s,X\_{s}-))e^{-v(t-s)}dW\_{s}\\ &+\frac{1}{2}\int\_{t}^{\tau^{\varepsilon}}(\partial\_{x}g(s,X\_{s}+)-\partial\_{x}g(s,X\_{s}-))e^{-v(s-t)}1\_{\{X\_{s}=c(s)\}}dl^{c}\_{s},\end{split} |  |

where lscl^{c}\_{s} is the local time of XX at the curve cc. Then, we have that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x[∫tτε12((∂t+ℒ)g(s,Xs+)e−v​(s−t)−vg(s,Xs+)e−v​(s−t)+(∂t+ℒ)g(s,Xs−)e−v​(s−t)−vg(s,Xs−)e−v​(s−t))1{Xs≠c​(s)}ds]=12(((∂t+ℒ)g(t,x+)+(∂t+ℒ)g(t,x−)−2vg(t,x))𝔼[τε−t]+o(𝔼[τε−t]).\begin{split}&\mathbb{E}\_{t,x}\bigg[\int\_{t}^{\tau^{\varepsilon}}\frac{1}{2}\bigg((\partial\_{t}+\mathcal{L})g(s,X\_{s}+)e^{-v(s-t)}-vg(s,X\_{s}+)e^{-v(s-t)}\\ &+(\partial\_{t}+\mathcal{L})g(s,X\_{s}-)e^{-v(s-t)}-vg(s,X\_{s}-)e^{-v(s-t)}\bigg)1\_{\{X\_{s}\neq c(s)\}}ds\bigg]\\ =&\frac{1}{2}\left(((\partial\_{t}+\mathcal{L})g(t,x+)+(\partial\_{t}+\mathcal{L})g(t,x-)-2vg(t,x)\right)\mathbb{E}[\tau^{\varepsilon}-t]+o(\mathbb{E}[\tau^{\varepsilon}-t]).\end{split} |  |

It is proved in Appendix [A](https://arxiv.org/html/2510.24128v1#A1 "Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼t,x​[lτεc−ltc])2=σ2​(t,x)​𝔼t,x​[τε−t]+o​(𝔼t,x​[τε−t]),\left(\mathbb{E}\_{t,x}[l^{c}\_{\tau^{\varepsilon}}-l\_{t}^{c}]\right)^{2}=\sigma^{2}(t,x)\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]+o(\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]), |  | (9) |

which further implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼t,x​[∫tτε(∂xg​(s,Xs+)−∂xg​(s,Xs−))​e−v​(s−t)​1{Xs=c​(s)}​𝑑lsc])2=(∂xg​(t,x+)−∂xg​(t,x−))2​σ2​(t,x)​𝔼t,x​[τε−t]+o​(𝔼t,x​[τε−t]).\begin{split}&\left(\mathbb{E}\_{t,x}[\int\_{t}^{\tau^{\varepsilon}}(\partial\_{x}g(s,X\_{s}+)-\partial\_{x}g(s,X\_{s}-))e^{-v(s-t)}1\_{\{X\_{s}=c(s)\}}dl^{c}\_{s}]\right)^{2}\\ =&\left(\partial\_{x}g(t,x+)-\partial\_{x}g(t,x-)\right)^{2}\sigma^{2}(t,x)\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]+o(\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]).\end{split} |  | (10) |

Hence,

|  |  |  |
| --- | --- | --- |
|  | (𝔼t,x[e−v​τεg(τε,Xτε)])2=g2(t,x)+(((∂t+ℒ)g(t,x+)+(∂t+ℒ)g(t,x−))g(t,x)−2vg12(t,x)+(∂xg​(t,x+)−∂xg​(t,x−)2)2σ2(t,x))𝔼t,x[τε−t]+g​(t,x)​𝔼t,x​[∫tτε(∂xg​(s,Xs+)−∂xg​(s,Xs−))​e−v​(s−t)​1{Xs=c​(s)}​𝑑lsc]+o​(𝔼t,x​[τε−t]).\begin{split}&(\mathbb{E}\_{t,x}[e^{-v\tau^{\varepsilon}}g(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})])^{2}=g^{2}(t,x)+\bigg(((\partial\_{t}+\mathcal{L})g(t,x+)+(\partial\_{t}+\mathcal{L})g(t,x-))g(t,x)-2vg^{2}\_{1}(t,x)\\ &+\left(\frac{\partial\_{x}g(t,x+)-\partial\_{x}g(t,x-)}{2}\right)^{2}\sigma^{2}(t,x)\bigg)\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]\\ &+g(t,x)\mathbb{E}\_{t,x}[\int\_{t}^{\tau^{\varepsilon}}(\partial\_{x}g(s,X\_{s}+)-\partial\_{x}g(s,X\_{s}-))e^{-v(s-t)}1\_{\{X\_{s}=c(s)\}}dl^{c}\_{s}]+o(\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]).\end{split} |  |

Similarly,

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[e−v​τε​h​(τε,Xτε)]=h​(t,x)+12​((∂t+ℒ)​h​(t,x+)+(∂t+ℒ)​h​(t,x−)−v​h​(t,x))​𝔼t,x​[τε−t]+12​𝔼t,x​[∫tτε(∂xh​(s,Xs+)−∂xh​(s,Xs−))​e−v​(s−t)​1{Xs=c​(s)}​𝑑lsc].\begin{split}&\mathbb{E}\_{t,x}[e^{-v\tau^{\varepsilon}}h(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})]\\ =&h(t,x)+\frac{1}{2}\left((\partial\_{t}+\mathcal{L})h(t,x+)+(\partial\_{t}+\mathcal{L})h(t,x-)-vh(t,x)\right)\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]\\ &+\frac{1}{2}\mathbb{E}\_{t,x}[\int\_{t}^{\tau^{\varepsilon}}(\partial\_{x}h(s,X\_{s}+)-\partial\_{x}h(s,X\_{s}-))e^{-v(s-t)}1\_{\{X\_{s}=c(s)\}}dl^{c}\_{s}].\end{split} |  |

Since V=h+γ2​g2V=h+\frac{\gamma}{2}g^{2} is C1C^{1} across cc, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x[∫tτε(∂xh(s,Xs+)−∂xh(s,Xs−))e−v​(s−t)1{Xs=c​(s)}dlsc+γ​g​(t,x)​𝔼t,x​[∫tτε(∂xg​(s,Xs+)−∂xg​(s,Xs−))​e−v​(s−t)​1{Xs=c​(s)}​𝑑lsc]=o​(𝔼t,x​[τε−t]).\begin{split}&\mathbb{E}\_{t,x}[\int\_{t}^{\tau^{\varepsilon}}(\partial\_{x}h(s,X\_{s}+)-\partial\_{x}h(s,X\_{s}-))e^{-v(s-t)}1\_{\{X\_{s}=c(s)\}}dl^{c}\_{s}\\ &+\gamma g(t,x)\mathbb{E}\_{t,x}[\int\_{t}^{\tau^{\varepsilon}}(\partial\_{x}g(s,X\_{s}+)-\partial\_{x}g(s,X\_{s}-))e^{-v(s-t)}1\_{\{X\_{s}=c(s)\}}dl^{c}\_{s}]=o(\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]).\end{split} |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | J​(t,x;τ𝒞ε,v)−J​(t,x;τ𝒞)𝔼t,x​[τε−t]=12​((∂t+ℒ)​(V−γ2​g2)​(t,x+)+γ​g​(∂t+ℒ)​g​(t,x+))+12​((∂t+ℒ)​(V−γ2​g2)​(t,x−)+γ​g​(∂t+ℒ)​g​(t,x−))+γ2​(∂xg​(t,x+)−∂xg​(t,x−)2)2​σ2​(t,x)+o​(1)=12((∂t+ℒ)V(t,x+)−γ|σ∂xg|2(t,x+)+(∂t+ℒ)V(t,x−)−γ|σ∂xg|2(t,x−))+γ2​(∂xg​(t,x+)−∂xg​(t,x−)2)2​σ2​(t,x)+o​(1),\begin{split}&\frac{J(t,x;\tau\_{\mathcal{C}}^{\varepsilon,v})-J(t,x;\tau\_{\mathcal{C}})}{\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]}\\ =&\frac{1}{2}\left((\partial\_{t}+\mathcal{L})(V-\frac{\gamma}{2}g^{2})(t,x+)+\gamma g(\partial\_{t}+\mathcal{L})g(t,x+)\right)\\ &+\frac{1}{2}\left((\partial\_{t}+\mathcal{L})(V-\frac{\gamma}{2}g^{2})(t,x-)+\gamma g(\partial\_{t}+\mathcal{L})g(t,x-)\right)\\ &+\frac{\gamma}{2}\left(\frac{\partial\_{x}g(t,x+)-\partial\_{x}g(t,x-)}{2}\right)^{2}\sigma^{2}(t,x)+o(1)\\ =&\frac{1}{2}\bigg((\partial\_{t}+\mathcal{L})V(t,x+)-\gamma|\sigma\partial\_{x}g|^{2}(t,x+)\\ &+(\partial\_{t}+\mathcal{L})V(t,x-)-\gamma|\sigma\partial\_{x}g|^{2}(t,x-)\bigg)\\ &+\frac{\gamma}{2}\left(\frac{\partial\_{x}g(t,x+)-\partial\_{x}g(t,x-)}{2}\right)^{2}\sigma^{2}(t,x)+o(1),\\ \end{split} |  |

which gives the desired result according the assumption of the theorem.
∎

###### Remark 4.1.

It is a well-known result in the theory of optimal stopping that the value function is C1C^{1} across the free boundary. However, one can not expect that gg is also C1C^{1}, see the example given in Subsection [5.1](https://arxiv.org/html/2510.24128v1#S5.SS1 "5.1 Infinite Horizon Case ‣ 5 Further Discussions ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"). Note that a similar condition is also given in [[7](https://arxiv.org/html/2510.24128v1#bib.bib7)].

## 5 Further Discussions

### 5.1 Infinite Horizon Case

In this subsection, we consider an infinite horizon example that one can give an explicit solution. Let XX be a geometric Brownian motion

|  |  |  |
| --- | --- | --- |
|  | d​Xt=μ​Xt​d​t+σ​Xt​d​Wt.dX\_{t}=\mu X\_{t}dt+\sigma X\_{t}dW\_{t}. |  |

Consider the MV stopping problem

|  |  |  |
| --- | --- | --- |
|  | J​(x;τ)=𝔼x​[Xτ]−γ2​Varx​[Xτ].J(x;\tau)=\mathbb{E}\_{x}\left[X\_{\tau}\right]-\frac{\gamma}{2}\text{Var}\_{x}\left[X\_{\tau}\right]. |  |

For this infinite horizon case, one can have an elliptic system similar to ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | {min⁡{−(ℒ​v−γ2​|σ​x​∂xg|2),v+γ2​(f−g)2−f}=0,ℒ​g=0, on {v+γ2​(f−g)2>f},g=f​ on {v+γ2​(f−g)2=f},\left\{\begin{split}&\min\left\{-\left(\mathcal{L}v-\frac{\gamma}{2}\left|\sigma x\partial\_{x}g\right|^{2}\right),v+\frac{\gamma}{2}(f-g)^{2}-f\right\}=0,\\ &\mathcal{L}g=0,\text{ on $\{v+\frac{\gamma}{2}(f-g)^{2}>f\}$},\\ &g=f\text{ on $\{v+\frac{\gamma}{2}(f-g)^{2}=f\}$},\end{split}\right. |  | (11) |

with ℒ=12​σ2​x2​∂2∂x2+μ​x​∂∂x\mathcal{L}=\frac{1}{2}\sigma^{2}x^{2}\frac{\partial^{2}}{\partial x^{2}}+\mu x\frac{\partial}{\partial x}. Denote by ρ=2​μσ2\rho=\frac{2\mu}{\sigma^{2}} and assume that ρ∈(0,1/2)\rho\in(0,1/2). Let b=2​ργ​(1−ρ)b=\frac{2\rho}{\gamma(1-\rho)}. Let us check that

|  |  |  |
| --- | --- | --- |
|  | V(x)={(1−γ2​b)​bρ​x1−ρ+γ2​b2​ρ​x2−2​ρ, for x<b,x, for x≥b,V(x)=\left\{\begin{split}&(1-\frac{\gamma}{2}b)b^{\rho}x^{1-\rho}+\frac{\gamma}{2}b^{2\rho}x^{2-2\rho},\text{ for $x<b$},\\ &x,\text{ for $x\geq b$},\end{split}\right. |  |

and

|  |  |  |
| --- | --- | --- |
|  | g(x)={bρ​x1−ρ, for x<b,x, for x≥b,g(x)=\left\{\begin{split}&b^{\rho}x^{1-\rho},\text{ for $x<b$},\\ &x,\text{ for $x\geq b$},\end{split}\right. |  |

satisfy ([11](https://arxiv.org/html/2510.24128v1#S5.E11 "In 5.1 Infinite Horizon Case ‣ 5 Further Discussions ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). For x<bx<b, it holds that

|  |  |  |
| --- | --- | --- |
|  | ∂xV=(1−ρ)​(1−γ2​b)​bρ​x−ρ+γ​(1−ρ)​b2​ρ​x1−2​ρ,\partial\_{x}V=(1-\rho)(1-\frac{\gamma}{2}b)b^{\rho}x^{-\rho}+\gamma(1-\rho)b^{2\rho}x^{1-2\rho}, |  |

|  |  |  |
| --- | --- | --- |
|  | ∂x​xV=−ρ​(1−ρ)​(1−γ2​b)​bρ​x−ρ−1+γ​(1−ρ)​(1−2​ρ)​b2​ρ​x−2​ρ,\partial\_{xx}V=-\rho(1-\rho)(1-\frac{\gamma}{2}b)b^{\rho}x^{-\rho-1}+\gamma(1-\rho)(1-2\rho)b^{2\rho}x^{-2\rho}, |  |

and ∂xg=(1−ρ​bρ​x−ρ)\partial\_{x}g=(1-\rho b^{\rho}x^{-\rho}). Thus, it is easy to check that, for x<bx<b, ℒ​V−γ2​|σ​x​∂xg|2=0\mathcal{L}V-\frac{\gamma}{2}\left|\sigma x\partial\_{x}g\right|^{2}=0 and ℒ​g=0\mathcal{L}g=0. When x≥bx\geq b, it is easy to see that ∂xV=∂xg=1\partial\_{x}V=\partial\_{x}g=1 and ∂x​xV=0\partial\_{xx}V=0. Hence,

|  |  |  |
| --- | --- | --- |
|  | ℒ​V−γ2​|σ​x​∂xg|2=μ​x−γ2​σ2​x2=γ2​σ2​x​(ργ−x)≤0.\mathcal{L}V-\frac{\gamma}{2}\left|\sigma x\partial\_{x}g\right|^{2}=\mu x-\frac{\gamma}{2}\sigma^{2}x^{2}=\frac{\gamma}{2}\sigma^{2}x(\frac{\rho}{\gamma}-x)\leq 0. |  |

Now let us verify that V+γ2​(x−g)2>xV+\frac{\gamma}{2}(x-g)^{2}>x for x<bx<b. Direct computation yields that

|  |  |  |
| --- | --- | --- |
|  | V+γ2​(x−g)2=(1−γ2​b)​bρ​x1−ρ+γ2​b2​ρ​x2−2​ρ+γ2​(x−bρ​x1−ρ)2=γ2​x2+γ​b2​ρ​x2−2​ρ−γ​bρ​x2−ρ+(1−γ2​b)​bρ​x1−ρ=x​(γ2​x+γ​b2​ρ​x1−2​ρ−γ​bρ​x1−ρ+(1−γ2​b)​bρ​x−ρ).\begin{split}&V+\frac{\gamma}{2}(x-g)^{2}\\ =&(1-\frac{\gamma}{2}b)b^{\rho}x^{1-\rho}+\frac{\gamma}{2}b^{2\rho}x^{2-2\rho}+\frac{\gamma}{2}(x-b^{\rho}x^{1-\rho})^{2}\\ =&\frac{\gamma}{2}x^{2}+\gamma b^{2\rho}x^{2-2\rho}-\gamma b^{\rho}x^{2-\rho}+(1-\frac{\gamma}{2}b)b^{\rho}x^{1-\rho}\\ =&x\left(\frac{\gamma}{2}x+\gamma b^{2\rho}x^{1-2\rho}-\gamma b^{\rho}x^{1-\rho}+(1-\frac{\gamma}{2}b)b^{\rho}x^{-\rho}\right).\end{split} |  |

Thus, we have to show that γ2​x+γ​b2​ρ​x1−2​ρ−γ​bρ​x1−ρ+(1−γ2​b)​bρ​x−ρ>1\frac{\gamma}{2}x+\gamma b^{2\rho}x^{1-2\rho}-\gamma b^{\rho}x^{1-\rho}+(1-\frac{\gamma}{2}b)b^{\rho}x^{-\rho}>1 for x<bx<b. For that purpose, define a function κ​(z)=γ2​b​z2​ρ−1+(1−γ2​b)​zρ\kappa(z)=\frac{\gamma}{2}bz^{2\rho-1}+(1-\frac{\gamma}{2}b)z^{\rho}. Let us find its infimum on [1,∞)[1,\infty). Taking derivative with respect to zz, we see that κ′​(z)=zρ−1​((2​ρ−1)​γ2​b​zρ−1+(1−γ2​b)​ρ)\kappa^{\prime}(z)=z^{\rho-1}((2\rho-1)\frac{\gamma}{2}bz^{\rho-1}+(1-\frac{\gamma}{2}b)\rho). Since ρ≤12\rho\leq\frac{1}{2} and z≥1z\geq 1, it holds that

|  |  |  |
| --- | --- | --- |
|  | (2​ρ−1)​γ2​b​zρ−1+(1−γ2​b)​ρ≥(2​ρ−1)​γ2​b+(1−γ2​b)​ρ=0,(2\rho-1)\frac{\gamma}{2}bz^{\rho-1}+(1-\frac{\gamma}{2}b)\rho\geq(2\rho-1)\frac{\gamma}{2}b+(1-\frac{\gamma}{2}b)\rho=0, |  |

where we use the fact that b=2​ργ​(1−ρ)b=\frac{2\rho}{\gamma(1-\rho)}.
This implies that κ\kappa is strictly increasing on [1,∞)[1,\infty) and taking minimum at z=1z=1, which equals to 11. Then, for x<bx<b,

|  |  |  |
| --- | --- | --- |
|  | γ2​x+γ​b2​ρ​x1−2​ρ−γ​bρ​x1−ρ+(1−γ2​b)​bρ​x−ρ=γ2​x​(1−bρ​x−ρ)2+γ2​b2​ρ​x1−2​ρ+(1−γ2​b)​bρ​x−ρ≥κ​(b​x−1)>1.\begin{split}&\frac{\gamma}{2}x+\gamma b^{2\rho}x^{1-2\rho}-\gamma b^{\rho}x^{1-\rho}+(1-\frac{\gamma}{2}b)b^{\rho}x^{-\rho}\\ =&\frac{\gamma}{2}x(1-b^{\rho}x^{-\rho})^{2}+\frac{\gamma}{2}b^{2\rho}x^{1-2\rho}+(1-\frac{\gamma}{2}b)b^{\rho}x^{-\rho}\\ \geq&\kappa(bx^{-1})>1.\end{split} |  |

Thus, (V,g)(V,g) is a solution of ([11](https://arxiv.org/html/2510.24128v1#S5.E11 "In 5.1 Infinite Horizon Case ‣ 5 Further Discussions ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). On x=bx=b, we can check that

|  |  |  |
| --- | --- | --- |
|  | ℒ​V​(b−)=γ2​σ2​b2​(1−ρ)2,ℒ​V​(b+)=μ​b,∂xg​(b−)=1−ρ, and ​∂xg​(b+)=1.\mathcal{L}V(b-)=\frac{\gamma}{2}\sigma^{2}b^{2}(1-\rho)^{2},\mathcal{L}V(b+)=\mu b,\partial\_{x}g(b-)=1-\rho,\text{ and }\partial\_{x}g(b+)=1. |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | ℒ​V​(b−)+ℒ​V​(b+)=γ2​σ2​b2​(1−ρ)2+μ​b=σ2​b​(γ2​b​(1−ρ)2+ρ)=σ2​b​ρ​(2−ρ),\mathcal{L}V(b-)+\mathcal{L}V(b+)=\frac{\gamma}{2}\sigma^{2}b^{2}(1-\rho)^{2}+\mu b=\sigma^{2}b(\frac{\gamma}{2}b(1-\rho)^{2}+\rho)=\sigma^{2}b\rho(2-\rho), |  |

and

|  |  |  |
| --- | --- | --- |
|  | γ​σ2​b2​(1+1−ρ2)2=σ2​b​(2−ρ)​(2−ρ)​γ​b4=σ2​b​(2−ρ)​ρ​2−ρ2−2​ρ>σ2​b​(2−ρ)​ρ.\gamma\sigma^{2}b^{2}\left(\frac{1+1-\rho}{2}\right)^{2}=\sigma^{2}b(2-\rho)\frac{(2-\rho)\gamma b}{4}=\sigma^{2}b(2-\rho)\rho\frac{2-\rho}{2-2\rho}>\sigma^{2}b(2-\rho)\rho. |  |

Thus, the stopping time is an equilibrium.

Moreover, one can also compute that V′​(b+)=V′​(b−)V^{\prime}(b+)=V^{\prime}(b-), g1′​(b−)=1−ρg^{\prime}\_{1}(b-)=1-\rho and g1′​(b+)=1g^{\prime}\_{1}(b+)=1. This suggests that one can expect VV to be C1C^{1}, but gg not C1C^{1}, so one can not assume that gg is C1C^{1} across the free boundary.

### 5.2 Discrete Time Approximation

For many time-inconsistent problems, the equilibrium solution in continuous time is regarded as the limit of its counterpart in discrete-time models. This is the logical structure of the derivation for extended HJB equation, see [[4](https://arxiv.org/html/2510.24128v1#bib.bib4)]. For that reason, we would like to check that whether one can get the same equation by considering the discrete time MV stopping problem.

Let Δ​t=TN\Delta t=\frac{T}{N} and tk=k​Δ​tt\_{k}=k\Delta t for k=0,1,…,Nk=0,1,...,N. We assume that one can only stop at these time points. Recursively define a sequence of stopping times {τi}i=0,1,…,N\{\tau\_{i}\}\_{i=0,1,...,N} as the follows. Set τN=tN\tau\_{N}=t\_{N}, U​(N,x)=f​(x)U(N,x)=f(x), and V​(N,x)=f​(x)V(N,x)=f(x). For i=N−1,N−2,…,0i=N-1,N-2,...,0, define

|  |  |  |
| --- | --- | --- |
|  | U​(i,x):=𝔼ti,x​[f​(Xτi+1)]−γ2​Varti,x​[f​(Xτi+1)],U(i,x):=\mathbb{E}\_{t\_{i},x}[f(X\_{\tau\_{i+1}})]-\frac{\gamma}{2}\text{Var}\_{t\_{i},x}[f(X\_{\tau\_{i+1}})], |  |

|  |  |  |
| --- | --- | --- |
|  | τi:={ti, if f​(Xti)≥Ui​(Xti),τi+1,if f​(Xti)<Ui​(Xti),\tau\_{i}:=\left\{\begin{matrix}t\_{i},\text{ if $f(X\_{t\_{i}})\geq U\_{i}(X\_{t\_{i}})$,}\\ \tau\_{i+1},\text{if $f(X\_{t\_{i}})<U\_{i}(X\_{t\_{i}})$,}\end{matrix}\right. |  |

and

|  |  |  |
| --- | --- | --- |
|  | V​(i,x):=𝔼ti,x​[f​(Xτi)]−γ2​Varti,x​[f​(Xτi)].V(i,x):=\mathbb{E}\_{t\_{i},x}[f(X\_{\tau\_{i}})]-\frac{\gamma}{2}\text{Var}\_{t\_{i},x}[f(X\_{\tau\_{i}})]. |  |

Moreover, we also define g​(i,x):=𝔼ti,x​[f​(Xτi)]g(i,x):=\mathbb{E}\_{t\_{i},x}[f(X\_{\tau\_{i}})]. The motivation of these definitions are the following. We view the MV stopping problem from a game-theoretic perspective as a non-cooperative game. We have one player at each time point tnt\_{n}, who can only choose the stopping decision at tnt\_{n}. The stopping time τi\tau\_{i} represent the time the process being stopped conditioned on its has not been stopped before tit\_{i}. Player nn has two options: to stop immediately or to continue. The reward of the first option is f​(Xti)f(X\_{t\_{i}}). Choosing to continue, the process is stopped at time τi+1\tau\_{i+1} and the expected reward is given by U​(i,Xti)U(i,X\_{t\_{i}}). Thus, the strategy of player nn is to decide to stop when f​(Xti)≥U​(i,Xti)f(X\_{t\_{i}})\geq U(i,X\_{t\_{i}}).

Now let us check the equation satisfied by ViV\_{i}. It is easy to see that V​(i,x)≥f​(x)V(i,x)\geq f(x). If V​(i,x)>f​(x)V(i,x)>f(x), it implies that τi=τi+1\tau\_{i}=\tau\_{i+1}. In this case, it holds that

|  |  |  |
| --- | --- | --- |
|  | V​(i,x)=U​(i,x)=𝔼ti,x​[V​(i+1,Xti+1)]−γ2​Varti,x​[g​(i+1,Xti+1)].V(i,x)=U(i,x)=\mathbb{E}\_{t\_{i},x}[V(i+1,X\_{t\_{i+1}})]-\frac{\gamma}{2}\text{Var}\_{t\_{i},x}[g(i+1,X\_{t\_{i+1}})]. |  |

Combining two situations, we have

|  |  |  |
| --- | --- | --- |
|  | min⁡{V​(i,x)−(𝔼ti,x​[V​(i+1,Xti+1)]−γ2​Varti,x​[g​(i+1,Xti+1)]),V​(i,x)−f​(x)}=0.\min\left\{V(i,x)-\left(\mathbb{E}\_{t\_{i},x}[V(i+1,X\_{t\_{i+1}})]-\frac{\gamma}{2}\text{Var}\_{t\_{i},x}[g(i+1,X\_{t\_{i+1}})]\right),V(i,x)-f(x)\right\}=0. |  |

Now we let Δ​t\Delta t go to zero. Formally, one see that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ti,x​[V​(i+1,Xti+1)]−V​(i,x)=(∂tV+ℒ​V)​(ti,x)​Δ​t+o​(Δ​t),\mathbb{E}\_{t\_{i},x}[V(i+1,X\_{t\_{i+1}})]-V(i,x)=(\partial\_{t}V+\mathcal{L}V)(t\_{i},x)\Delta t+o(\Delta t), |  |

and

|  |  |  |
| --- | --- | --- |
|  | Varti,x​[g​(i+1,Xti+1)]=𝔼ti,x​[g2​(i+1,Xti+1)]−(𝔼ti,x​[g​(i+1,Xti+1)])2=g2​(i,x)+(∂t+ℒ)​g2​Δ​t−(g​(i,x)+(∂t+ℒ)​g​Δ​t)2​o​(Δ​t)=(∂t+ℒ)​g2​Δ​t−g​(∂t+ℒ)​g​Δ​t+o​(Δ​t)=|σ​∂xg|2​Δ​t+o​(Δ​t).\begin{split}&\text{Var}\_{t\_{i},x}[g(i+1,X\_{t\_{i+1}})]=\mathbb{E}\_{t\_{i},x}[g^{2}(i+1,X\_{t\_{i+1}})]-\left(\mathbb{E}\_{t\_{i},x}[g(i+1,X\_{t\_{i+1}})]\right)^{2}\\ =&g^{2}(i,x)+(\partial\_{t}+\mathcal{L})g^{2}\Delta t-\left(g(i,x)+(\partial\_{t}+\mathcal{L})g\Delta t\right)^{2}o(\Delta t)\\ =&(\partial\_{t}+\mathcal{L})g^{2}\Delta t-g(\partial\_{t}+\mathcal{L})g\Delta t+o(\Delta t)\\ =&|\sigma\partial\_{x}g|^{2}\Delta t+o(\Delta t).\end{split} |  |

Hence, we get the following system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {min⁡{−(∂tV+ℒ​V−γ​|σ​∂xg|2),V−f}=0,V​(T,x)=f,∂tg+ℒ​g=0, on {V>f},g=f​ on {V=f},g​(T,x)=f​(x).\left\{\begin{split}&\min\left\{-\left(\partial\_{t}V+\mathcal{L}V-\gamma\left|\sigma\partial\_{x}g\right|^{2}\right),V-f\right\}=0,V(T,x)=f,\\ &\partial\_{t}g+\mathcal{L}g=0,\text{ on $\{V>f\}$},\\ &g=f\text{ on $\{V=f\}$},g(T,x)=f(x).\end{split}\right. |  | (12) |

Note that this equation is different from ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) with the condition V+γ2​(f−g)2≥fV+\frac{\gamma}{2}(f-g)^{2}\geq f replaced by V≥fV\geq f. Clearly V≥fV\geq f implies V+γ2​(f−g)2≥fV+\frac{\gamma}{2}(f-g)^{2}\geq f. Moreover, on {V=f}\{V=f\}, we also have g=fg=f and hence, V+γ2​(f−g)2=fV+\frac{\gamma}{2}(f-g)^{2}=f. Thus, the solution of the above system also satisfies
([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). In this sense, it seems that ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) is a more general equation. However, it remains unclear whether there exists a solution that satisfies ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")), but do not satisfy ([12](https://arxiv.org/html/2510.24128v1#S5.E12 "In 5.2 Discrete Time Approximation ‣ 5 Further Discussions ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")).

### 5.3 General Time-inconsistent Problems

To explain the additional quadratic term in the condition V+γ2​(f−g)2≥fV+\frac{\gamma}{2}(f-g)^{2}\geq f of ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")), let us consider a more general time-inconsistent problem in which the player choose stopping time to maximize the following functional

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[f​(Xτ)]+G​(𝔼t,x​[k​(Xτ)]).\mathbb{E}\_{t,x}[f(X\_{\tau})]+G(\mathbb{E}\_{t,x}[k(X\_{\tau})]). |  |

We just give some formal arguments for illustration. First, we consider the regularized problem. For an equilibrium π∗\pi^{\*}, define g​(t,x)=𝔼t,x​[k​(Xτ)]g(t,x)=\mathbb{E}\_{t,x}[k(X\_{\tau})] and h​(t,x)=𝔼t,x​[f​(Xτ)+∫0τλ​H​(πs∗)​𝑑s]h(t,x)=\mathbb{E}\_{t,x}[f(X\_{\tau})+\int\_{0}^{\tau}\lambda H(\pi^{\*}\_{s})ds]. Then, it holds that (g,h)(g,h) solves

|  |  |  |
| --- | --- | --- |
|  | {(∂t+ℒ)​h+λ​H​(π∗)+π∗​(f−h)=0,g2​(T)=f,(∂t+ℒ)​g+π∗​(k−g)=0,g​(T)=k.\left\{\begin{split}&(\partial\_{t}+\mathcal{L})h+\lambda H(\pi^{\*})+\pi^{\*}(f-h)=0,g\_{2}(T)=f,\\ &(\partial\_{t}+\mathcal{L})g+\pi^{\*}(k-g)=0,g(T)=k.\end{split}\right. |  |

For a purterbed strategy πε,v\pi^{\varepsilon,v}, one can get that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[k​(Xπε,v)]=g​(t,x)+((∂t+ℒ)​g+v​(k−g))​ε+o​(ε),\mathbb{E}\_{t,x}[k(X\_{\pi^{\varepsilon,v}})]=g(t,x)+\left((\partial\_{t}+\mathcal{L})g+v(k-g)\right)\varepsilon+o(\varepsilon), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[f​(Xπε,v)+∫0τε,vλ​H​(πsε,v)​𝑑s]=h​(t,x)+((∂t+ℒ)​h+v​(f−h)+λ​H​(v))​ε+o​(ε).\begin{split}&\mathbb{E}\_{t,x}[f(X\_{\pi^{\varepsilon,v}})+\int\_{0}^{\tau^{\varepsilon,v}}\lambda H(\pi^{\varepsilon,v}\_{s})ds]\\ =&h(t,x)+\left((\partial\_{t}+\mathcal{L})h+v(f-h)+\lambda H(v)\right)\varepsilon+o(\varepsilon).\end{split} |  |

Moreover, it holds that

|  |  |  |
| --- | --- | --- |
|  | G​(𝔼t,x​[k​(Xπε,v)])=G​(g)+G′​(g)​((∂t+ℒ)​g+v​(k−g))​ε+o​(ε).G(\mathbb{E}\_{t,x}[k(X\_{\pi^{\varepsilon,v}})])=G(g)+G^{\prime}(g)\left((\partial\_{t}+\mathcal{L})g+v(k-g)\right)\varepsilon+o(\varepsilon). |  |

Then, one can show that π∗\pi^{\*} is an equilibrium if and only if

|  |  |  |
| --- | --- | --- |
|  | π∗=exp⁡(−h+G′​(g)​g−f−G′​(g)​kλ).\pi^{\*}=\exp(-\frac{h+G^{\prime}(g)g-f-G^{\prime}(g)k}{\lambda}). |  |

Note that the value function V=h+G​(g)V=h+G(g) and satisfies

|  |  |  |
| --- | --- | --- |
|  | (∂t+ℒ)​V+λ​exp⁡(−h+G′​(g)​g−f−G′​(g)​kλ)+ℋG​(g)=0,(\partial\_{t}+\mathcal{L})V+\lambda\exp(-\frac{h+G^{\prime}(g)g-f-G^{\prime}(g)k}{\lambda})+\mathcal{H}\_{G}(g)=0, |  |

where the operator ℋG\mathcal{H}\_{G} is defined as

|  |  |  |
| --- | --- | --- |
|  | ℋG​(φ)=G′​(φ)​ℒ​φ−ℒ​G​(φ).\mathcal{H}\_{G}(\varphi)=G^{\prime}(\varphi)\mathcal{L}\varphi-\mathcal{L}G(\varphi). |  |

We also see that

|  |  |  |
| --- | --- | --- |
|  | h+G′​(g)​g−f−G′​(g)​k=V−(f+G​(k))+G​(k)−G​(g)−G′​(g)​(k−g).h+G^{\prime}(g)g-f-G^{\prime}(g)k=V-(f+G(k))+G(k)-G(g)-G^{\prime}(g)(k-g). |  |

Denote by ΔG​(k,g)=G​(k)−G​(g)−G′​(g)​(k−g)\Delta\_{G}(k,g)=G(k)-G(g)-G^{\prime}(g)(k-g). Then, when letting λ\lambda go to zero, VV should converge to the following variational inequality

|  |  |  |
| --- | --- | --- |
|  | min⁡{−((∂t+ℒ)​V+HG​(g)),V−(f+G​(k))+ΔG​(k,g)}=0.\min\left\{-\left((\partial\_{t}+\mathcal{L})V+H\_{G}(g)\right),V-(f+G(k))+\Delta\_{G}(k,g)\right\}=0. |  |

Note that the condition is written as V+ΔG​(k,g)≥(f+G​(g))V+\Delta\_{G}(k,g)\geq(f+G(g)). For MV case, i.e., G​(k)=γ2​k2G(k)=\frac{\gamma}{2}k^{2}, ΔG​(k,g)=γ2​(k−g)2\Delta\_{G}(k,g)=\frac{\gamma}{2}(k-g)^{2}, which is the same condition in ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")). Moreover, define the set

|  |  |  |
| --- | --- | --- |
|  | 𝒞={(t,x)|V+ΔG​(k,g)>f+G​(k)},\mathcal{C}=\{(t,x)|V+\Delta\_{G}(k,g)>f+G(k)\}, |  |

and the stopping time τ𝒞\tau\_{\mathcal{C}} as

|  |  |  |
| --- | --- | --- |
|  | τ𝒞=inf{s>t|(s,Xs)∉𝒞}.\tau\_{\mathcal{C}}=\inf\{s>t|(s,X\_{s})\notin\mathcal{C}\}. |  |

Then, one can formally verify that τ𝒞\tau\_{\mathcal{C}} in the same sense as that in the statement of Theorem [4.1](https://arxiv.org/html/2510.24128v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method").

From the previous discussion, we see that the appearance of the additional term ΔG​(k,g)\Delta\_{G}(k,g) is due to two factors. One is that GG is a non-linear function, which makes the problem time-inconsistent. The other is that, when equilibrium is under consideration, the perturbation lies within the family of relaxed strategies rather than pure strategies. This coincides with the fact in the game theory that pure strategy equilibrium is different from mixed strategy equilibrium.

## 6 Conclusions

This paper systematically investigates the MV optimal stopping problem–a time-inconsistent stochastic optimization problem-by developing a vanishing regularization method and deriving the corresponding extended HJB equation. More precisely, to tackle the mathematical intractability of direct equilibrium analysis, we introduce a regularized problem, which enables rigorous derivation of the equilibrium strategy and the associated extended HJB equation. Then, letting λ→0\lambda\rightarrow 0, i.e. vanishing regularization, we formally recover a system of parabolic variational inequalities ([7](https://arxiv.org/html/2510.24128v1#S4.E7 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) for the original MV problem. This system characterizes equilibrium stopping times and includes a key quadratic term γ2​(f−g)2\frac{\gamma}{2}(f-g)^{2}–a distinction from classical optimal stopping, where stopping conditions depend only on comparing the value function to the instantaneous reward. By extending the analysis to general time-inconsistent problems, we demonstrate that the additional term in our stopping condition arises from the non-linearity of the objective (responsible for time inconsistency) and the use of mixed strategies.

This work provides a rigorous mathematical foundation for MV stopping problems, with potential applications in financial decision-making (e.g., asset sale timing, portfolio liquidation) and statistical inference (e.g., risk-aware hypothesis testing stopping rules). However, there are still some open problems left for future research, including
proving rigorous convergence of the regularized extended HJB system to the limiting variational inequality and developing numerical algorithms to compute equilibrium stopping rules for practical applications.

## References

* [1]

  C. Bayer, D. Belomestny, P. Hager, P. Pigato, and J. Schoenmakers, Randomized optimal stopping algorithms and their convergence analysis, SIAM
  Journal on Financial Mathematics, 12 (2021), pp. 1201–1225.
* [2]

  E. Bayraktar, Z. Wang, and Z. Zhou, Equilibria of time-inconsistent
  stopping for one-dimensional diffusion processes, Mathematical Finance, 33
  (2023), pp. 797–841.
* [3]

  T. Björk, M. Khapko, and A. Murgoci, On time-inconsistent
  stochastic control in continuous time, Finance and Stochastics, 21 (2017),
  pp. 331–360.
* [4]

  T. Björk, M. Khapko, A. Murgoci, et al., Time-inconsistent
  control theory with finance applications, vol. 732, Springer, 2021.
* [5]

  T. Björk, A. Murgoci, and X. Y. Zhou, Mean–variance portfolio
  optimization with state-dependent risk aversion, Mathematical Finance: An
  International Journal of Mathematics, Statistics and Financial Economics, 24
  (2014), pp. 1–24.
* [6]

  S. Christensen and K. Lindensjö, On finding equilibrium stopping
  times for time-inconsistent markovian problems, SIAM Journal on Control and
  Optimization, 56 (2018), pp. 4228–4255.
* [7]

  S. Christensen and K. Lindensjö, On time-inconsistent stopping
  problems and mixed strategy stopping times, Stochastic Processes and their
  Applications, 130 (2020), pp. 2886–2917.
* [8]

  M. Dai, Y. Dong, and Y. Jia, Learning equilibrium mean-variance
  strategy, Mathematical Finance, 33 (2023), pp. 1166–1212.
* [9]

  Y. Dong, Randomized optimal stopping problem in continuous time and
  reinforcement learning algorithm, SIAM Journal on Control and Optimization,
  62 (2024), pp. 1590–1614.
* [10]

  K. D. Elworthy and X.-M. Li, Formulae for the derivatives of heat
  semigroups, Journal of Functional Analysis, 125 (1994), pp. 252–286.
* [11]

  L. He and Z. Liang, Optimal investment strategy for the dc plan with
  the return of premiums clauses in a mean–variance framework, Insurance:
  Mathematics and Economics, 53 (2013), pp. 643–649.
* [12]

  M. Jeanblanc, M. Yor, and M. Chesney, Mathematical methods for
  financial markets, Springer Science & Business Media, 2009.
* [13]

  G. M. Lieberman, Second order parabolic differential equations,
  World scientific, 1996.
* [14]

  H. M. Markowitz, Portfolio selection: efficient diversification of
  investments, Yale university press, 2008.
* [15]

  G. Peskir and A. Shiryaev, Optimal stopping and free-boundary
  problems, Springer, 2006.
* [16]

  R. H. Strotz, Myopia and inconsistency in dynamic utility
  maximization, The review of economic studies, 23 (1955), pp. 165–180.
* [17]

  A. Tartakovsky, I. Nikiforov, and M. Basseville, Sequential
  analysis: Hypothesis testing and changepoint detection, CRC press, 2014.

## Appendix A Proof of ([9](https://arxiv.org/html/2510.24128v1#S4.E9 "In 4 Extended HJB Equation for Original Problem ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method"))

Define another stopping time τ~ε\tilde{\tau}^{\varepsilon} as

|  |  |  |
| --- | --- | --- |
|  | τ~ε=inf{s≥t||Xs−Xt|≥ε}.\tilde{\tau}^{\varepsilon}=\inf\{s\geq t||X\_{s}-X\_{t}|\geq\varepsilon\}. |  |

Note that τε\tau^{\varepsilon} coincides to τ~ε\tilde{\tau}^{\varepsilon} on the set {τ~ε<t+ε}\{\tilde{\tau}^{\varepsilon}<t+\varepsilon\}. Then, we claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2𝔼t,x​[τ~ε−t]=σ2​(t,x).\lim\_{\varepsilon\rightarrow 0}\frac{\varepsilon^{2}}{\mathbb{E}\_{t,x}[\tilde{\tau}^{\varepsilon}-t]}=\sigma^{2}(t,x). |  | (13) |

To prove the claim, we follow the same argument as that in the proof of Lemma 5.5 in [[7](https://arxiv.org/html/2510.24128v1#bib.bib7)]. For any a>1σ2​(t,x)a>\frac{1}{\sigma^{2}(t,x)}, define a function FF as F​(t,y)=a​(y−x)2−tF(t,y)=a(y-x)^{2}-t. It is easy to see that

|  |  |  |
| --- | --- | --- |
|  | (∂t+ℒ)​F​(s,y)=2​a​μ​(s,y)​(y−x)+a​σ2​(s,y)−1,(\partial\_{t}+\mathcal{L})F(s,y)=2a\mu(s,y)(y-x)+a\sigma^{2}(s,y)-1, |  |

which is greater than 0 for {(s,y)||y−x|≤ε,s−t≤ε}\{(s,y)||y-x|\leq\varepsilon,s-t\leq\varepsilon\} with a sufficiently small ε\varepsilon. Thus, applying Itô formula to F​(s,Xs)F(s,X\_{s}) and taking conditional expectation, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[τ~ε−t]≤a​𝔼t,x​[|Xτ~ε−x|2]=a​ε2.\mathbb{E}\_{t,x}[\tilde{\tau}^{\varepsilon}-t]\leq a\mathbb{E}\_{t,x}[|X\_{\tilde{\tau}^{\varepsilon}}-x|^{2}]=a\varepsilon^{2}. |  |

Similarly, one also has

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[τ~ε−t]≥a​ε2,\mathbb{E}\_{t,x}[\tilde{\tau}^{\varepsilon}-t]\geq a\varepsilon^{2}, |  |

for a<1σ2​(t,x)a<\frac{1}{\sigma^{2}(t,x)}. Combining these two estimations give the claim ([13](https://arxiv.org/html/2510.24128v1#A1.E13 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")).
Using Chebyshev’s inequality, we also have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(τ~ε>t+ε)≤𝔼t,x​[τ~ε−t]ε=O​(ε).P(\tilde{\tau}^{\varepsilon}>t+\varepsilon)\leq\frac{\mathbb{E}\_{t,x}[\tilde{\tau}^{\varepsilon}-t]}{\varepsilon}=O(\varepsilon). |  | (14) |

The argument for ([13](https://arxiv.org/html/2510.24128v1#A1.E13 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) also yields that

|  |  |  |
| --- | --- | --- |
|  | limh→0𝔼t,x​[|Xτε−x|2]𝔼t,x​[τε−t]=σ2​(t,x).\lim\_{h\rightarrow 0}\frac{\mathbb{E}\_{t,x}[|X\_{\tau^{\varepsilon}}-x|^{2}]}{\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]}=\sigma^{2}(t,x). |  |

Note that, using ([14](https://arxiv.org/html/2510.24128v1#A1.E14 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")),

|  |  |  |
| --- | --- | --- |
|  | ε2≥𝔼t,x​[|Xτε−x|2]≥ε2​P​(τε<t+ε)=ε2−ε2​P​(τε=t+ε)=ε2+o​(ε2).\varepsilon^{2}\geq\mathbb{E}\_{t,x}[|X\_{\tau^{\varepsilon}}-x|^{2}]\geq\varepsilon^{2}P(\tau^{\varepsilon}<t+\varepsilon)=\varepsilon^{2}-\varepsilon^{2}P(\tau^{\varepsilon}=t+\varepsilon)=\varepsilon^{2}+o(\varepsilon^{2}). |  |

Hence, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x​[τε−t]=1σ2​(t,x)​ε2+o​(ε).\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]=\frac{1}{\sigma^{2}(t,x)}\varepsilon^{2}+o(\varepsilon). |  | (15) |

Let k​(t,y):=|c​(t)−y|k(t,y):=|c(t)-y|. From Itô-Tanaka formula, one has that

|  |  |  |
| --- | --- | --- |
|  | k​(τε,Xτε)=∫tτε12​((∂t+ℒ)​k​(s,Xs+)+(∂t+ℒ)​k​(s,Xs−))​𝑑s+∫tτε12​σ​(∂yk​(s,Xs+)+∂yk​(s,Xs−))​𝑑Ws+∫tτε12​(∂yk​(s,Xs+)−∂yk​(s,Xs−))​1{Xs=c​(s)}​𝑑lsc.\begin{split}k(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})=&\int\_{t}^{\tau^{\varepsilon}}\frac{1}{2}((\partial\_{t}+\mathcal{L})k(s,X\_{s}+)+(\partial\_{t}+\mathcal{L})k(s,X\_{s}-))ds\\ &+\int\_{t}^{\tau^{\varepsilon}}\frac{1}{2}\sigma(\partial\_{y}k(s,X\_{s}+)+\partial\_{y}k(s,X\_{s}-))dW\_{s}\\ &+\int\_{t}^{\tau^{\varepsilon}}\frac{1}{2}(\partial\_{y}k(s,X\_{s}+)-\partial\_{y}k(s,X\_{s}-))1\_{\{X\_{s}=c(s)\}}dl\_{s}^{c}.\end{split} |  |

Note that, for Xs=c​(s)X\_{s}=c(s), ∂yk​(s,Xs+)=1\partial\_{y}k(s,X\_{s}+)=1 and ∂yk​(s,Xs+)=−1\partial\_{y}k(s,X\_{s}+)=-1. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼t,x​[k​(τε,Xτε)])2=(𝔼t,x​[lτεc−ltc])2+o​(𝔼t,x​[τε−t]).(\mathbb{E}\_{t,x}[k(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})])^{2}=(\mathbb{E}\_{t,x}[l^{c}\_{\tau^{\varepsilon}}-l^{c}\_{t}])^{2}+o(\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]). |  | (16) |

When tt is fixed, for sufficienly small ε\varepsilon,

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[k​(τε,Xτε)]=𝔼t,x​[|x+ε−c​(τε)|​1{Xτε=x+ε}]+𝔼t,x​[|x−ε−c​(τε)|​1{Xτε=x−ε}]+𝔼t,x​[|Xτε−c​(τε)|​1{τε=t+ε}].\begin{split}\mathbb{E}\_{t,x}[k(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})]=&\mathbb{E}\_{t,x}[|x+\varepsilon-c(\tau^{\varepsilon})|1\_{\{X\_{\tau^{\varepsilon}=x+\varepsilon}\}}]+\mathbb{E}\_{t,x}[|x-\varepsilon-c(\tau^{\varepsilon})|1\_{\{X\_{\tau^{\varepsilon}=x-\varepsilon}\}}]\\ &+\mathbb{E}\_{t,x}[|X\_{\tau^{\varepsilon}}-c(\tau^{\varepsilon})|1\_{\{\tau^{\varepsilon}=t+\varepsilon\}}].\end{split} |  |

We estimate the right hand side term by term. Estimations for the first two term
are similar. It holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[|x±ε−c​(τε)|​1{Xτε=x±ε}]≤𝔼t,x​[(|x±ε−c​(t)|+|c​(t)−c​(τε)|)​1{Xτε=x±ε}]≤p±​ε+C​𝔼t,x​[τε−t]=p±+O​(ε2),\begin{split}\mathbb{E}\_{t,x}[|x\pm\varepsilon-c(\tau^{\varepsilon})|1\_{\{X\_{\tau^{\varepsilon}=x\pm\varepsilon}\}}]&\leq\mathbb{E}\_{t,x}[\left(|x\pm\varepsilon-c(t)|+|c(t)-c(\tau^{\varepsilon})|\right)1\_{\{X\_{\tau^{\varepsilon}=x\pm\varepsilon}\}}]\\ &\leq p\_{\pm}\varepsilon+C\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]=p\_{\pm}+O(\varepsilon^{2}),\end{split} |  |

where p±=P​(Xτε=x±ε)p\_{\pm}=P(X\_{\tau^{\varepsilon}}=x\pm\varepsilon) and the last inequality is due to the assumption that c​(⋅)c(\cdot) is Lipschitz continuous. For the last term,

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[|Xτε−c​(τε)|​1{τε=t+ε}]=𝔼t,x​[|Xτε−c​(t)+c​(t)−c​(τε)|​1{τε=t+ε}]≤C​ε​P​(τε=t+ε)=C​ε​P​(τ~ε>t+ε)=O​(ε2).\begin{split}\mathbb{E}\_{t,x}[|X\_{\tau^{\varepsilon}}-c(\tau^{\varepsilon})|1\_{\{\tau^{\varepsilon}=t+\varepsilon\}}]=&\mathbb{E}\_{t,x}[|X\_{\tau^{\varepsilon}}-c(t)+c(t)-c(\tau^{\varepsilon})|1\_{\{\tau^{\varepsilon}=t+\varepsilon\}}]\\ \leq&C\varepsilon P(\tau^{\varepsilon}=t+\varepsilon)=C\varepsilon P(\tilde{\tau}^{\varepsilon}>t+\varepsilon)=O(\varepsilon^{2}).\end{split} |  |

Combining these estimations, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[k​(τε,Xτε)]=(p−+p+)​ε+O​(ε2)=ε+O​(ε2),\mathbb{E}[k(\tau^{\varepsilon},X\_{\tau^{\varepsilon}})]=(p\_{-}+p\_{+})\varepsilon+O(\varepsilon^{2})=\varepsilon+O(\varepsilon^{2}), |  | (17) |

where we use ([14](https://arxiv.org/html/2510.24128v1#A1.E14 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) again to get the last equality.
Hence, ([15](https://arxiv.org/html/2510.24128v1#A1.E15 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")),([16](https://arxiv.org/html/2510.24128v1#A1.E16 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) and ([17](https://arxiv.org/html/2510.24128v1#A1.E17 "In Appendix A Proof of (9) ‣ Extended HJB Equation for Mean-Variance Stopping Problem: Vanishing Regularization Method")) yield that

|  |  |  |
| --- | --- | --- |
|  | limε→0(𝔼t,x​[lτεc−ltc])2𝔼t,x​[τε−t]=σ2​(t,x).\lim\_{\varepsilon\rightarrow 0}\frac{(\mathbb{E}\_{t,x}[l^{c}\_{\tau^{\varepsilon}}-l^{c}\_{t}])^{2}}{\mathbb{E}\_{t,x}[\tau^{\varepsilon}-t]}=\sigma^{2}(t,x). |  |

## Appendix B A Key Lemma

###### Lemma B.1.

Let φ\varphi be the solution of

|  |  |  |
| --- | --- | --- |
|  | (∂t+ℒ)​φ+c​φ=g,φ​(T,x)=f,(\partial\_{t}+\mathcal{L})\varphi+c\varphi=g,\varphi(T,x)=f, |  |

with c,gc,g being bounded continuous functions and ff also bounded with bounded derivatives. Then

1. 1.

   There exists a constant CC depending on the coefficients such that

   |  |  |  |
   | --- | --- | --- |
   |  | −C​(‖f−‖∞+T​‖g−‖∞)≤φ≤C​(‖f+‖∞+T​‖g+‖∞),-C(\|f^{-}\|\_{\infty}+T\|g^{-}\|\_{\infty})\leq\varphi\leq C(\|f^{+}\|\_{\infty}+T\|g^{+}\|\_{\infty}), |  |

   where f±f^{\pm} represents the positive and negative part of ff respectively. If c≤0c\leq 0, the constant CC can be chosen to be 11.
2. 2.

   Assuming that c≡0c\equiv 0, we have

   |  |  |  |
   | --- | --- | --- |
   |  | ‖∂xφ‖∞≤(1+C​T)​‖∂xf‖∞+C​(T+T)​‖g‖∞.\|\partial\_{x}\varphi\|\_{\infty}\leq(1+C\sqrt{T})\|\partial\_{x}f\|\_{\infty}+C(\sqrt{T}+T)\|g\|\_{\infty}. |  |

###### Proof.

From Feymann-Kac representation, it holds that

|  |  |  |
| --- | --- | --- |
|  | φ​(t,x)=𝔼t,x​[e∫tTc​(u,Xu)​𝑑u​f​(XT)+∫tTe∫tsc​(u,Xu)​𝑑u​g​(s,Xs)​𝑑s].\varphi(t,x)=\mathbb{E}\_{t,x}\left[e^{\int\_{t}^{T}c(u,X\_{u})du}f(X\_{T})+\int\_{t}^{T}e^{\int\_{t}^{s}c(u,X\_{u})du}g(s,X\_{s})ds\right]. |  |

Then, one can easily get the first estimation from the assumptions on the coefficients.

To prove the second estimation, define two processes ∇X\nabla X and NN as

|  |  |  |
| --- | --- | --- |
|  | d​∇X=∂xb​(Xt)​∇Xt​d​t+∂xσ​(Xt)​∇Xt​d​Wt,∇Xt=I,d\nabla X=\partial\_{x}b(X\_{t})\nabla X\_{t}dt+\partial\_{x}\sigma(X\_{t})\nabla X\_{t}dW\_{t},\nabla X\_{t}=I, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Ns=1s−t​∫ts<σ−1​(Xu)​∇Xu,d​Wu>.N\_{s}=\frac{1}{s-t}\int\_{t}^{s}<\sigma^{-1}(X\_{u})\nabla X\_{u},dW\_{u}>. |  |

One can verify that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x​[supt≤s≤T|∇Xs−I|2]≤C​T​, and ​𝔼t,x​[|Ns|2]≤C​(1s−t+1).\mathbb{E}\_{t,x}[\sup\_{t\leq s\leq T}|\nabla X\_{s}-I|^{2}]\leq CT\text{, and }\mathbb{E}\_{t,x}[|N\_{s}|^{2}]\leq C(\frac{1}{s-t}+1). |  |

Then, using Bismut-Elworthy-Li formula [[10](https://arxiv.org/html/2510.24128v1#bib.bib10)], we get that, for any function ξ\xi

|  |  |  |
| --- | --- | --- |
|  | ∂x𝔼t,x​[ξ​(Xs)]=𝔼t,x​[∂xξ​(Xs)​∇Xs]=𝔼t,x​[ξ​(Xs)​Ns].\partial\_{x}\mathbb{E}\_{t,x}[\xi(X\_{s})]=\mathbb{E}\_{t,x}[\partial\_{x}\xi(X\_{s})\nabla X\_{s}]=\mathbb{E}\_{t,x}[\xi(X\_{s})N\_{s}]. |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | ∂xφ​(t,x)=𝔼t,x​[∂xf​(XT)​∇XT]+∫tT𝔼t,x​[g​(s,Xs)​Ns]​𝑑s.\partial\_{x}\varphi(t,x)=\mathbb{E}\_{t,x}[\partial\_{x}f(X\_{T})\nabla X\_{T}]+\int\_{t}^{T}\mathbb{E}\_{t,x}[g(s,X\_{s})N\_{s}]ds. |  |

Clearly, we have

|  |  |  |
| --- | --- | --- |
|  | |𝔼t,x​[∂xf​(XT)​∇XT]|≤(C​T+1)​‖∂xf‖∞,|\mathbb{E}\_{t,x}[\partial\_{x}f(X\_{T})\nabla X\_{T}]|\leq(C\sqrt{T}+1)\|\partial\_{x}f\|\_{\infty}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∫tT𝔼t,x​[g​(s,Xs)​Ns]​𝑑s≤‖g‖∞​∫tT(𝔼t,x​[|Ns|2])12​𝑑s≤C​‖g‖∞​∫tT1(s−t)12+1​d​s=C​(T−t+(T−t))​‖g‖∞.\begin{split}&\int\_{t}^{T}\mathbb{E}\_{t,x}[g(s,X\_{s})N\_{s}]ds\leq\|g\|\_{\infty}\int\_{t}^{T}(\mathbb{E}\_{t,x}[|N\_{s}|^{2}])^{\frac{1}{2}}ds\\ \leq&C\|g\|\_{\infty}\int\_{t}^{T}\frac{1}{(s-t)^{\frac{1}{2}}}+1ds=C(\sqrt{T-t}+(T-t))\|g\|\_{\infty}.\end{split} |  |

This gives the second estimation.
∎