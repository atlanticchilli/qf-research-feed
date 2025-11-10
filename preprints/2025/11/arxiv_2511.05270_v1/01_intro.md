---
authors:
- Guojiang Shao
- Zuo Quan Xu
- Qi Zhang
doc_id: arxiv:2511.05270v1
family_id: arxiv:2511.05270
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Competitive optimal portfolio selection under mean-variance criterion
url_abs: http://arxiv.org/abs/2511.05270v1
url_html: https://arxiv.org/html/2511.05270v1
venue: arXiv q-fin
version: 1
year: 2025
---


Guojiang Shao
School of Mathematical Sciences, Fudan University, Shanghai 200433, China (<gjshao23@m.fudan.edu.cn>).
  
Zuo Quan Xu
Contact author. Department of Applied Mathematics, The Hong Kong Polytechnic University, Kowloon, Hong Kong SAR, China (<maxu@polyu.edu.hk>).
  
Qi Zhang
School of Mathematical Sciences, Fudan University, Shanghai 200433, China and Laboratory of Mathematics for Nonlinear Science, Fudan University, Shanghai 200433, China (<qzh@fudan.edu.cn>).

(November 7, 2025)

###### Abstract

We investigate a portfolio selection problem involving multi competitive agents, each exhibiting mean-variance preferences. Unlike classical models, each agent’s utility is determined by their relative wealth compared to the average wealth of all agents, introducing a competitive dynamic into the optimization framework. To address this game-theoretic problem, we first reformulate the mean-variance criterion as a constrained, non-homogeneous stochastic linear-quadratic control problem and derive the corresponding optimal feedback strategies. The existence of Nash equilibria is shown to depend on the well-posedness of a complex, coupled system of equations. Employing decoupling techniques, we reduce the well-posedness analysis to the solvability of a novel class of multi-dimensional linear backward stochastic differential equations (BSDEs). We solve a new type of nonlinear BSDEs (including the above linear one as a special case) using fixed-point theory. Depending on the interplay between market and competition parameters, three distinct scenarios arise: (i) the existence of a unique Nash equilibrium, (ii) the absence of any Nash equilibrium, and (iii) the existence of infinitely many Nash equilibria. These scenarios are rigorously characterized and discussed in detail.

  

Keywords: Competitive portfolio selection, mean-variance, stochastic linear quadratic problem, backward stochastic differential equation.

## 1 Introduction

The seminal work of Markowitz [[15](https://arxiv.org/html/2511.05270v1#bib.bib15), [16](https://arxiv.org/html/2511.05270v1#bib.bib16)] introduced mean-variance (MV) analysis, establishing a foundational framework for optimizing asset allocation by balancing risk and return. Since then, MV theory has been extended in numerous directions, including the incorporation of stochastic factors, which are central to the models considered in this paper. In parallel, the study of multi-agent games and, more broadly, mean-field games has emerged as a vibrant area in mathematical finance, particularly in the context of multi-agent optimal investment. These models capture the interactions among multiple investors, where each agent seeks to optimize not only their individual wealth but also their relative performance compared to others. Consequently, the agents’ decisions are influenced by both their personal risk preferences and the competitive dynamics of the market.

This paper investigates competitive optimal portfolio selection under the MV criterion, bridging game theory and portfolio theory in non-Markovian market setting. In contrast to traditional frameworks where agents optimize in isolation, we consider a scenario in which agents compete to maximize their terminal wealth relative to the average wealth of all agents. This leads naturally to a non-cooperative stochastic differential game formulation.

The continuous-time MV portfolio selection problem has been extensively studied under various market assumptions and methodological approaches. We briefly review some key developments in this area. Li and Zhou [[22](https://arxiv.org/html/2511.05270v1#bib.bib22)] addressed the continuous-time MV portfolio selection problem using the embedding technique and stochastic linear-quadratic (LQ) control theory. Under the constraint of no short-selling, Li, Zhou, and Lim [[12](https://arxiv.org/html/2511.05270v1#bib.bib12)] analyzed the MV portfolio selection problem in continuous time via the Hamilton-Jacobi-Bellman (HJB) equation and two Riccati equations. In a complete market with random coefficients, Lim and Zhou [[14](https://arxiv.org/html/2511.05270v1#bib.bib14)] investigated the continuous-time MV problem using stochastic LQ control and backward stochastic differential equation (BSDE) theory. Subsequent works by Zhou and Yin [[23](https://arxiv.org/html/2511.05270v1#bib.bib23)] and Xiong and Zhou [[18](https://arxiv.org/html/2511.05270v1#bib.bib18)] extended the MV framework to settings with regime switching and partial information, respectively. More recently, Hu, Shi, and Xu [[9](https://arxiv.org/html/2511.05270v1#bib.bib9)] generalized the problem to non-homogeneous stochastic LQ control with random coefficients and regime-switching dynamics, applying their results to asset-liability management under MV criterion.

Meanwhile, optimal investment and reinsurance strategies under relative performance criteria in mean-field and multi-agent games have garnered increasing attention in recent years. The study of portfolio games with relative performance considerations can be traced back to Espinosa and Touzi [[4](https://arxiv.org/html/2511.05270v1#bib.bib4)], who examined multi-agent games with portfolio constraints under CARA utility by analyzing the associated systems of quadratic BSDEs. Subsequently, Lacker and Zariphopoulou [[11](https://arxiv.org/html/2511.05270v1#bib.bib11)] derived explicit constant equilibrium strategies for both CARA and CRRA utilities in Markovian markets, utilizing HJB equations. Building on these results, extensions to proportional reinsurance and investment were proposed by Bo, Wang, and Zhou [[2](https://arxiv.org/html/2511.05270v1#bib.bib2)], as well as He, He, Chen, and Liu [[8](https://arxiv.org/html/2511.05270v1#bib.bib8)]. More recently, Wang, Xu, and Zhang [[17](https://arxiv.org/html/2511.05270v1#bib.bib17)] advanced this line of research by investigating competitive portfolio selection in non-Markovian markets, employing quadratic BSDEs to characterize Nash equilibria under both CARA and CRRA utility frameworks.

However, existing results on competitive optimal portfolio selection under the MV criterion are relatively scarce. In fact, research in this area has primarily focused on time-consistent Nash equilibrium strategies, as seen in works such as Guan and Hu [[7](https://arxiv.org/html/2511.05270v1#bib.bib7)], Zhu, Guan, and Li [[24](https://arxiv.org/html/2511.05270v1#bib.bib24)], and Yang, Chen, and Xu [[19](https://arxiv.org/html/2511.05270v1#bib.bib19)]. These studies investigated time-consistent investment and proportional reinsurance strategies for competitive insurers under the MV criterion, utilizing the extended HJB equations developed by Bj’́ork, Khapko, and Murgoci [[1](https://arxiv.org/html/2511.05270v1#bib.bib1)]. For further related results on portfolio selection based on relative performance, see Deng, Su, and Zhou [[3](https://arxiv.org/html/2511.05270v1#bib.bib3)], Fu [[5](https://arxiv.org/html/2511.05270v1#bib.bib5)], Fu and Zhou [[6](https://arxiv.org/html/2511.05270v1#bib.bib6)], Lacker and Soret [[10](https://arxiv.org/html/2511.05270v1#bib.bib10)], Liang and Zhang [[13](https://arxiv.org/html/2511.05270v1#bib.bib13)], and Zhang and Huang [[21](https://arxiv.org/html/2511.05270v1#bib.bib21)], among others.

Distinct from the aforementioned results on time-consistent Nash equilibrium strategies, the problem addressed in this paper involves time-inconsistent Nash equilibrium strategies under the MV criterion for a multi-agent game, where the extended HJB equations are not applicable. To tackle this game-theoretic problem, we first reformulate it as a constrained stochastic LQ control problem with a non-homogeneous state equation. Employing Lagrange duality, we derive the optimal feedback strategy for each agent. The existence of a Nash equilibrium requires analyzing a coupled system comprising linear optimal feedback controls, forward stochastic differential equations (SDEs), and BSDEs. By applying decoupling techniques, we separate the SDEs from the coupled system and characterize the Nash equilibrium via a novel class of linear multi-dimensional BSDEs with random coefficients:

|  |  |  |
| --- | --- | --- |
|  | {d​𝒉​(t)=−{A​(t)​𝒉​(t)+B​(t)​𝜼​(t)+C​(t)​𝒉​(0)+F​(t)}​d⁡t+𝜼​(t)​d⁡W​(t),t∈[0,T],𝒉​(T)=0.\left\{\begin{array}[]{l}\mathrm{d}\boldsymbol{h}(t)=-\left\{A(t)\boldsymbol{h}(t)+B(t)\boldsymbol{\eta}(t)+C(t)\boldsymbol{h}(0)+F(t)\right\}\operatorname{d}\!t+\boldsymbol{\eta}(t)\operatorname{d}\!W(t),\quad t\in[0,T],\\ \boldsymbol{h}(T)=0.\end{array}\right. |  |

Notably, the driver of this BSDE depends on the solution 𝒉​(0)\boldsymbol{h}(0), making it a nonstandard BSDE. To ensure the admissibility of the Nash equilibrium, we establish the solvability of a class of general nonlinear BSDEs (including the above linear one as a special case) using fixed-point theory. Depending on the market and competition parameters, three scenarios may arise: the existence of a unique Nash equilibrium, the absence of any Nash equilibrium, or the existence of infinitely many Nash equilibria. These scenarios are thoroughly analyzed and discussed. It is worth emphasizing that, in contrast to the results in [[11](https://arxiv.org/html/2511.05270v1#bib.bib11)], [[7](https://arxiv.org/html/2511.05270v1#bib.bib7)], and [[17](https://arxiv.org/html/2511.05270v1#bib.bib17)], our derived strategy depends on both the initial and current values of wealth.

The remainder of this paper is organized as follows. In Section [2](https://arxiv.org/html/2511.05270v1#S2 "2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion"), we formulate the competitive optimal portfolio selection problem under MV criterion and turn it into a constrained stochastic LQ control problem. Section [3](https://arxiv.org/html/2511.05270v1#S3 "3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion") presents the derivation of the optimal strategy for each agent under the MV criterion. In Section [4](https://arxiv.org/html/2511.05270v1#S4 "4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), we address the Nash equilibrium by analyzing a coupled system comprising linear optimal feedback controls, SDEs, and BSDEs. Section [5](https://arxiv.org/html/2511.05270v1#S5 "5 Example ‣ Competitive optimal portfolio selection under mean-variance criterion") considers a special case to illustrate our theoretical results. Finally, Section [6](https://arxiv.org/html/2511.05270v1#S6 "6 Conclusion ‣ Competitive optimal portfolio selection under mean-variance criterion") summarizes our findings in a comprehensive table. Appendix [A](https://arxiv.org/html/2511.05270v1#A1 "Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion") provides a proof of the well-posedness for a new class of general nonlinear BSDEs, whose linear form arises in our study.

## 2 Problem Formulation

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a complete probability space, and {W​(t)}t∈[0,T]\{W(t)\}\_{t\in[0,T]} is a one-dimensional Brownian motion on it.
Denote by 𝔽={ℱt}t∈[0,T]\mathbb{F}=\{\mathcal{F}\_{t}\}\_{t\in[0,T]} the filtration generated by WW.
For n∈ℕn\in\mathbb{N}, we define some useful spaces as follows.

|  |  |  |
| --- | --- | --- |
|  | L𝔽∞​(0,T;ℝn):the set of 𝔽-adapted essentially bounded ​ℝn​-valued processes;L𝔽∞​(0,T;ℝn×n):the set of 𝔽-adapted essentially bounded ​ℝn×n​-valued processes;L𝔽∞​(0,T;ℝ+):the set of 𝔽-adapted essentially bounded nonnegative processes;L𝔽∞​(0,T;ℝ>0):the set of 𝔽-adapted essentially bounded positive processes;L𝔽∞​(0,T;ℝ≫1):the set of 𝔽-adapted processes ​v:[0,T]×Ω→(0,+∞)​suchthat c−1⩽v​(t)⩽c a.e. a.s. for some constant c>0;L𝔽∞​(0,T;ℝ≪−1):the set of 𝔽-adapted processes ​ v:[0,T]×Ω→(−∞,0) ​suchthat c−1⩽v​(t)⩽c a.e. a.s. for some constant c<0;L𝔽2​(0,T;ℝn):the set of 𝔽-adapted processes ​v:[0,T]×Ω→ℝn​such that 𝔼​[∫0T|v​(t)|2​d⁡t]<∞;S𝔽2​(0,T;ℝn):the set of 𝔽-adapted processes v:[0,T]×Ω→ℝn withcontinuous sample paths such that ​𝔼​[supt∈[0,T]|v​(t)|2]<∞.\displaystyle\begin{array}[]{rl}L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}^{n}\right):&\text{the set of $\mathbb{F}$-adapted essentially bounded }\mathbb{R}^{n}\text{-valued processes;}\\ L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}^{n\times n}\right):&\text{the set of $\mathbb{F}$-adapted essentially bounded }\mathbb{R}^{n\times n}\text{-valued processes};\\ L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{+}\right):&\text{the set of $\mathbb{F}$-adapted essentially bounded nonnegative processes};\\ L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{>0}\right):&\text{the set of $\mathbb{F}$-adapted essentially bounded positive processes};\\ L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{\gg 1}\right):&\text{the set of $\mathbb{F}$-adapted processes }v:[0,T]\times\Omega\rightarrow(0,+\infty)~\text{such}\\ &\text{that $c^{-1}\leqslant v(t)\leqslant c$ a.e. a.s. for some constant $c>0$};\\ L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{\ll-1}\right):&\text{the set of $\mathbb{F}$-adapted processes }$ {\small$v:[0,T]\times\Omega\to(-\infty,0)$} $\text{such}\\ &\text{that $c^{-1}\leqslant v(t)\leqslant c$ a.e. a.s. for some constant $c<0$};\\ L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n}\right):&\text{the set of $\mathbb{F}$-adapted processes }v:[0,T]\times\Omega\rightarrow\mathbb{R}^{n}~\text{such that }\\ &\mathbb{E}\left[\int\_{0}^{T}|v(t)|^{2}\operatorname{d}\!t\right]<\infty;\\ S\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n}\right):&\text{the set of $\mathbb{F}$-adapted processes $v:[0,T]\times\Omega\rightarrow\mathbb{R}^{n}$ with}\\ &\text{continuous sample paths such that }\mathbb{E}\left[\sup\_{t\in[0,T]}|v(t)|^{2}\right]<\infty.\end{array} |  |

BMO martingale, which is a short form of the martingale of bounded mean oscillation, plays a big role in this paper. For any f∈L𝔽2​(0,T;ℝ1)f\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}), ∫0⋅f​(s)​d⁡W​(s)\int\_{0}^{\cdot}f(s)\operatorname{d}\!W(s) is a BMO martingale on [0,T][0,T] if and only if there exists a constant c>0c>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫τT|f​(s)|2​ds|ℱτ]⩽c,\mathbb{E}\left[\int\_{\tau}^{T}|f(s)|^{2}\mathrm{~d}s\;\bigg|\;\mathcal{F}\_{\tau}\right]\leqslant c, |  |

holds for all 𝔽\mathbb{F}-stopping times τ⩽T\tau\leqslant T. We denote the space of BMO martingales by

|  |  |  |
| --- | --- | --- |
|  | L𝔽2,BMO​(0,T;ℝn)={f∈L𝔽2​(0,T;ℝn):∫0⋅f​(s)​d⁡W​(s)​is a BMO martingale on ​[0,T]}.L\_{\mathbb{F}}^{2,\mathrm{BMO}}(0,T;\mathbb{R}^{n})=\left\{f\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}):\int\_{0}^{\cdot}f(s)\operatorname{d}\!W(s)~\text{is a BMO martingale on }[0,T]\right\}. |  |

We now introduce our financial market, in which there is a risk-free asset (bond) and n⩾2n\geqslant 2 risky assets (stocks). Correspondingly, there are nn agents in the market, each of which has its preference for a stock to invest. Consequently,
the dynamic equations of bond S0={S0​(t)}t∈[0,T]S\_{0}=\{S\_{0}(t)\}\_{t\in[0,T]} and the stock ii for the agent ii Si={Si​(t)}t∈[0,T]S\_{i}=\{S\_{i}(t)\}\_{t\in[0,T]} are given by

|  |  |  |
| --- | --- | --- |
|  | {d​S0​(t)S0​(t)=r​(t)​d⁡t,S0​(0)=s0>0,t∈[0,T],d​Si​(t)Si​(t)=μi​(t)​d⁡t+σi​(t)​d⁡W​(t),Si​(0)=si>0,t∈[0,T],\left\{\begin{array}[]{l}\frac{\mathrm{d}S\_{0}(t)}{S\_{0}(t)}=r(t)\operatorname{d}\!t,\quad S\_{0}(0)=s\_{0}>0,\quad t\in[0,T],\\ \frac{\mathrm{d}S\_{i}(t)}{S\_{i}(t)}=\mu\_{i}(t)\operatorname{d}\!t+\sigma\_{i}(t)\operatorname{d}\!W(t),\quad S\_{i}(0)=s\_{i}>0,\quad t\in[0,T],\end{array}\right. |  |

where r∈L𝔽∞​(0,T;ℝ+)r\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}\_{+}), μi∈L𝔽∞​(0,T;ℝ+)\mu\_{i}\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}\_{+}) and σi∈L𝔽∞​(0,T;ℝ≫1)\sigma\_{i}\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}\_{\gg 1}) serve as the interest rate, the appreciation rate of stock ii and the volatility, respectively.
Our model is non-Markovian since these parameters are stochastic.

Denote by ρi≜μi−rσi∈L𝔽∞​(0,T;ℝ1)\rho\_{i}\triangleq\frac{\mu\_{i}-r}{\sigma\_{i}}\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}^{1}) the risk premium of stock ii. If ρi≡0\rho\_{i}\equiv 0, there is no motivation for agent ii to invest in stock ii, hence in the rest of this paper, we always assume ρi≢0\rho\_{i}\not\equiv 0. For simplicity, we only consider the case that the common noise WW in the market is 11-dimensional Brownian motion.

Denote by {πi​(t)}t∈[0,T]\{\pi\_{i}(t)\}\_{t\in[0,T]} the amount of money invested in stock ii. Then the self-financing wealth of agent ii, {Xi​(t)}t∈[0,T]\{X\_{i}(t)\}\_{t\in[0,T]}, is given by

|  |  |  |
| --- | --- | --- |
|  | {d​Xi​(t)=[r​(t)​Xi​(t)+πi​(t)​σi​(t)​ρi​(t)]​d⁡t+πi​(t)​σi​(t)​d⁡W​(t),t∈[0,T],Xi​(0)=xi.\left\{\begin{aligned} \mathrm{d}X\_{i}(t)&=\left[r(t)X\_{i}(t)+\pi\_{i}(t)\sigma\_{i}(t)\rho\_{i}(t)\right]\operatorname{d}\!t+\pi\_{i}(t)\sigma\_{i}(t)\operatorname{d}\!W(t),\quad t\in[0,T],\\ X\_{i}(0)&=x\_{i}.\end{aligned}\right. |  |

###### Definition 2.1.

A vector portfolio strategy 𝛑≜(π1,π2,⋯,πn)⊤\boldsymbol{\pi}\triangleq(\pi\_{1},\pi\_{2},\cdots,\pi\_{n})^{\top} is called admissible if 𝛑∈L𝔽2​(0,T;ℝn)\boldsymbol{\pi}\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}).

Set 𝒰≜L𝔽2​(0,T;ℝ1)\mathcal{U}\triangleq L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}),
then 𝝅\boldsymbol{\pi} is admissible if and only if πi∈𝒰\pi\_{i}\in\mathcal{U} for all i=1,2,⋯,ni=1,2,\cdots,n.

In our game, each agent aims to outperform the others.
We assume that every agent uses an MV preference on the relative wealth.
The arithmetic average wealth at time TT is defined as

|  |  |  |
| --- | --- | --- |
|  | X¯​(T)≜1n​∑i=1nXi​(T).\bar{X}(T)\triangleq\frac{1}{n}\sum\_{i=1}^{n}X\_{i}(T). |  |

For agent ii, the relative wealth compared to others is defined as Xi​(T)−θi​X¯​(T)X\_{i}(T)-\theta\_{i}\bar{X}(T), where θi∈[0,1]\theta\_{i}\in[0,1] is a parameter describing agent ii’s relative preference between their own wealth and average wealth. The agent ii’s MV preference is formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ji​(π1,π2,…,πn,θi,γi)≜𝔼​[Xi​(T)−θi​X¯​(T)]−γi2​Var​[Xi​(T)−θi​X¯​(T)],J\_{i}(\pi\_{1},\pi\_{2},\ldots,\pi\_{n},\theta\_{i},\gamma\_{i})\triangleq\mathbb{E}[X\_{i}(T)-\theta\_{i}\bar{X}(T)]-\frac{\gamma\_{i}}{2}\text{Var}[X\_{i}(T)-\theta\_{i}\bar{X}(T)], |  | (2.1) |

where γi>0\gamma\_{i}>0 is the risk aversion parameter of agent ii.

To simplify our problem, we put forward a new cost functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | J^i​(π1,π2,…,πn,θi,γi)≜𝔼​[Xi​(T)−θi​X^i​(T)]−γi2​Var​[Xi​(T)−θi​X^i​(T)],\hat{J}\_{i}(\pi\_{1},\pi\_{2},\ldots,\pi\_{n},\theta\_{i},\gamma\_{i})\triangleq\mathbb{E}[X\_{i}(T)-\theta\_{i}\hat{X}\_{i}(T)]-\frac{\gamma\_{i}}{2}\text{Var}[X\_{i}(T)-\theta\_{i}\hat{X}\_{i}(T)], |  | (2.2) |

where

|  |  |  |
| --- | --- | --- |
|  | X^i​(t)≜∑k≠iXk​(t)n−1,\hat{X}\_{i}(t)\triangleq\frac{\sum\_{k\neq i}X\_{k}(t)}{n-1}, |  |

satisfying the state equation

|  |  |  |
| --- | --- | --- |
|  | {d​X^i​(t)=[r​(t)​X^i​(t)+(ρ​σ​π)^i​(t)]​d⁡t+(σ​π)^i​(t)​d⁡W​(t),t∈[0,T],X^i​(0)=x^i,\left\{\begin{aligned} \mathrm{d}\hat{X}\_{i}(t)&=[r(t)\hat{X}\_{i}(t)+\widehat{(\rho\sigma\pi)}\_{i}(t)]\operatorname{d}\!t+\widehat{(\sigma\pi)}\_{i}(t)\operatorname{d}\!W(t),\quad t\in[0,T],\\ \hat{X}\_{i}(0)&=\hat{x}\_{i},\end{aligned}\right. |  |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ρ​σ​π)^i​(t)\displaystyle\widehat{(\rho\sigma\pi)}\_{i}(t) | ≜1n−1​∑k≠iρk​(t)​σk​(t)​πk​(t),\displaystyle\triangleq\frac{1}{n-1}\sum\_{k\neq i}\rho\_{k}(t)\sigma\_{k}(t)\pi\_{k}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (σ​π)^i​(t)\displaystyle\widehat{(\sigma\pi)}\_{i}(t) | ≜1n−1​∑k≠iσk​(t)​πk​(t),\displaystyle\triangleq\frac{1}{n-1}\sum\_{k\neq i}\sigma\_{k}(t)\pi\_{k}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | x^i\displaystyle\hat{x}\_{i} | ≜1n−1​∑k≠ixk.\displaystyle\triangleq\frac{1}{n-1}\sum\_{k\neq i}x\_{k}. |  |

A direct computation reveals the relation between the two cost functionals ([2.1](https://arxiv.org/html/2511.05270v1#S2.E1 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) and ([2.2](https://arxiv.org/html/2511.05270v1#S2.E2 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")):

|  |  |  |
| --- | --- | --- |
|  | Ji​(π1,π2,…,πn,θi,γi)=(1−θin)​J^i​(π1,π2,…,πn,(n−1)​θin−θi,(1−θin)​γi),J\_{i}\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n},\theta\_{i},\gamma\_{i}\right)=\left(1-\frac{\theta\_{i}}{n}\right)\hat{J}\_{i}\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n},\frac{(n-1)\theta\_{i}}{n-\theta\_{i}},\left(1-\frac{\theta\_{i}}{n}\right)\gamma\_{i}\right), |  |

where (1−θin)​γi>0\left(1-\frac{\theta\_{i}}{n}\right)\gamma\_{i}>0 and (n−1)​θin−θi\frac{(n-1)\theta\_{i}}{n-\theta\_{i}} monotonically increases from 0 to 11 as θi\theta\_{i} increases from 0 to 11. Hence optimizing the cost functional ([2.1](https://arxiv.org/html/2511.05270v1#S2.E1 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) is equivalent to optimizing the cost functional ([2.2](https://arxiv.org/html/2511.05270v1#S2.E2 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) with a trivial difference in parameters θi\theta\_{i} and γi\gamma\_{i}. For simplicity, we focus on the cost functional ([2.2](https://arxiv.org/html/2511.05270v1#S2.E2 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) in the rest of the paper. We define Nash equilibrium as follows.

###### Definition 2.2.

An admissible vector strategy 𝛑∗=(π1∗,π2∗,…,πn∗)⊤\boldsymbol{\pi}^{\*}=(\pi\_{1}^{\*},\pi\_{2}^{\*},\ldots,\pi\_{n}^{\*})^{\top} is called a Nash equilibrium (strategy) if, for each agent i∈{1,…,n}i\in\{1,\ldots,n\} and any πi∈𝒰\pi\_{i}\in\mathcal{U},

|  |  |  |
| --- | --- | --- |
|  | J^i​(π1∗,…,πi−1∗,πi∗,πi−1∗,…,πn∗;θi,γi)⩾J^i​(π1∗,…,πi−1∗,πi,πi+1∗,…,πn∗;θi,γi).\hat{J}\_{i}\left(\pi\_{1}^{\*},\ldots,\pi\_{i-1}^{\*},\pi\_{i}^{\*},\pi\_{i-1}^{\*},\ldots,\pi\_{n}^{\*};\theta\_{i},\gamma\_{i}\right)\geqslant\hat{J}\_{i}\left(\pi\_{1}^{\*},\ldots,\pi\_{i-1}^{\*},\pi\_{i},\pi\_{i+1}^{\*},\ldots,\pi\_{n}^{\*};\theta\_{i},\gamma\_{i}\right). |  |

In the rest of this section, we further simplify our model.
Set Zi​(t)≜Xi​(t)−θi​X^i​(t)Z\_{i}(t)\triangleq X\_{i}(t)-\theta\_{i}\hat{X}\_{i}(t) as a new state variable. Then it satisfies the dynamic equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Zi​(t)=[r​(t)​Zi​(t)+ρi​(t)​σi​(t)​πi​(t)−θi​(ρ​σ​π)^i​(t)]​d⁡t+[σi​(t)​πi​(t)−θi​(σ​π)^i​(t)]​d⁡W​(t),t∈[0,T],Zi​(0)=zi≜xi−θi​x^i.\left\{\begin{aligned} \mathrm{d}Z\_{i}(t)=&\left[r(t)Z\_{i}(t)+\rho\_{i}(t)\sigma\_{i}(t)\pi\_{i}(t)-\theta\_{i}\widehat{(\rho\sigma\pi)}\_{i}(t)\right]\operatorname{d}\!t\\ &+\left[\sigma\_{i}(t)\pi\_{i}(t)-\theta\_{i}\widehat{(\sigma\pi)}\_{i}(t)\right]\operatorname{d}\!W(t),\quad t\in[0,T],\\ Z\_{i}(0)=&z\_{i}\triangleq x\_{i}-\theta\_{i}\hat{x}\_{i}.\end{aligned}\right. |  | (2.3) |

When the n−1n-1 agents’ strategies πk∈𝒰\pi\_{k}\in\mathcal{U}, k≠ik\neq i, are fixed, the game problem for agent ii reduces to an MV portfolio selection problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxπi𝔼​[Zi​(T)]−γi2​Var⁡(Zi​(T)),subject to{πi∈𝒰,(Zi,πi)​ satisfies ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).\begin{array}[]{rl}\max\limits\_{\pi\_{i}}&\mathbb{E}[Z\_{i}(T)]-\frac{\gamma\_{i}}{2}\operatorname{Var}(Z\_{i}(T)),\\ \text{subject to}&\left\{\begin{array}[]{l}\pi\_{i}\in\mathcal{U},\\ (Z\_{i},\pi\_{i})\text{ satisfies }\eqref{state1}.\end{array}\right.\end{array} |  | (2.4) |

As its cost functional involves Var⁡(⋅)\operatorname{Var}(\cdot), it is a mean field stochastic control problem. To avoid using the dedicated mean field stochastic control theory, we introduce the following constrained stochastic control problem, parameterized by a target d∈ℝ1d\in\mathbb{R}^{1}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minπiVar⁡(Zi​(T))=𝔼​[Zi​(T)−d]2,subject to{𝔼​[Zi​(T)]=d,πi∈𝒰,(Zi,πi)​ satisfies ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).\begin{array}[]{rl}\min\limits\_{\pi\_{i}}&\operatorname{Var}(Z\_{i}(T))=\mathbb{E}\left[Z\_{i}(T)-d\right]^{2},\\ \text{subject to}&\left\{\begin{array}[]{l}\mathbb{E}[Z\_{i}(T)]=d,\\ \pi\_{i}\in\mathcal{U},\\ (Z\_{i},\pi\_{i})\text{ satisfies }\eqref{state1}.\end{array}\right.\end{array} |  | (2.5) |

Since ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) is a convex optimization problem, we can introduce a Lagrange multiplier λ∈ℝ1\lambda\in\mathbb{R}^{1} to deal with the goal constraint 𝔼​[Zi​(T)]=d\mathbb{E}[Z\_{i}(T)]=d. Then ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) can be further transformed into an unconstrained stochastic control problem, i.e. for each fixed λ\lambda,

|  |  |  |  |
| --- | --- | --- | --- |
|  | minπi𝔼​[|Zi​(T)−d|2]+2​λ​(𝔼​[Zi​(T)]−d)≜Ji​(πi,λ),subject to{πi∈𝒰,(Zi,πi)​ satisfies ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")),\begin{array}[]{rl}\min\limits\_{\pi\_{i}}&\mathbb{E}\left[|Z\_{i}(T)-d|^{2}\right]+2\lambda\left(\mathbb{E}[Z\_{i}(T)]-d\right)\triangleq J\_{i}(\pi\_{i},\lambda),\\ \text{subject to}&\left\{\begin{array}[]{l}\pi\_{i}\in\mathcal{U},\\ (Z\_{i},\pi\_{i})\text{ satisfies }\eqref{state1},\end{array}\right.\end{array} |  | (2.6) |

where the constant 22 in front of λ\lambda is used to complete the square. As a result, above control problem is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | minπi𝔼​[|Zi​(T)−b|2]≜𝒥i​(πi),subject to{πi∈𝒰,b=d−λ,(Zi,πi)​ satisfies ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).\begin{array}[]{rl}\min\limits\_{\pi\_{i}}&\mathbb{E}\left[|Z\_{i}(T)-b|^{2}\right]\triangleq\mathscr{J}\_{i}(\pi\_{i}),\\ \text{subject to}&\left\{\begin{array}[]{l}\pi\_{i}\in\mathcal{U},\\ b=d-\lambda,\\ (Z\_{i},\pi\_{i})\text{ satisfies }\eqref{state1}.\end{array}\right.\end{array} |  | (2.7) |

Therefore, to solve the MV portfolio selection problem ([2.4](https://arxiv.org/html/2511.05270v1#S2.E4 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), the key is to first solve the stochastic LQ control problem ([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).

## 3 Solutions for the MV Problems ([2.4](https://arxiv.org/html/2511.05270v1#S2.E4 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion"))-([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion"))

In this section, we fix the strategies πk∈𝒰\pi\_{k}\in\mathcal{U}, k≠ik\neq i, of the n−1n-1 agents, and solve the MV portfolio selection problems ([2.4](https://arxiv.org/html/2511.05270v1#S2.E4 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion"))-([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) for agent ii.

We first introduce two useful BSDEs,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​pi=−((2​r−ρi2)​pi−2​ρi​Λi−Λi2pi)​d⁡t+Λi​d⁡W,t∈[0,T],pi​(T)=1,\left\{\begin{aligned} &\mathrm{d}p\_{i}=-\left(\left(2r-\rho\_{i}^{2}\right)p\_{i}-2\rho\_{i}\Lambda\_{i}-\frac{\Lambda\_{i}^{2}}{p\_{i}}\right)\operatorname{d}\!t+\Lambda\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ &p\_{i}(T)=1,\end{aligned}\right. |  | (3.1) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​hi={r​hi+θi​(ρ​σ​π)^i−θi​ρi​(σ​π)^i+ρi​ηi}​d⁡t+ηi​d⁡W,t∈[0,T],hi​(T)=−(d−λ).\left\{\begin{array}[]{l}\mathrm{d}h\_{i}=\left\{rh\_{i}+\theta\_{i}\widehat{(\rho\sigma\pi)}\_{i}-\theta\_{i}\rho\_{i}\widehat{(\sigma\pi)}\_{i}+\rho\_{i}\eta\_{i}\right\}\operatorname{d}\!t+\eta\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ h\_{i}(T)=-(d-\lambda).\end{array}\right. |  | (3.2) |

Here and hereafter, we may omit time variables in equations and formulas if it does not cause confusion.

###### Lemma 3.1.

BSDE ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (pi,Λi)∈L𝔽∞​(0,T;ℝ≫1)×L𝔽2,BMO​(0,T;ℝ1)(p\_{i},\Lambda\_{i})\in L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{\gg 1}\right)\times L\_{\mathbb{F}}^{2,\mathrm{BMO}}(0,T;\mathbb{R}^{1}). Furthermore, pi​(t)p\_{i}(t) is explicitly given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​(t)=1𝔼​[exp⁡(∫tT−2​ρi​(s)​d⁡W​(s)+∫tT(−2​r​(s)−|ρi​(s)|2)​d⁡s)|ℱt],t∈[0,T].p\_{i}(t)=\frac{1}{\mathbb{E}\left[\exp\left(\int\_{t}^{T}-2\rho\_{i}(s)\operatorname{d}\!W(s)+\int\_{t}^{T}\left(-2r(s)-|\rho\_{i}(s)|^{2}\right)\operatorname{d}\!s\right)\bigg|\mathcal{F}\_{t}\right]},\quad t\in[0,T]. |  | (3.3) |

###### Proof.

The first part of the claim follows from Theorem 3.2 in [[17](https://arxiv.org/html/2511.05270v1#bib.bib17)]. To establish ([3.3](https://arxiv.org/html/2511.05270v1#S3.E3 "In Lemma 3.1. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), observe that (pˇi,Λˇi)≜(1pi,−Λipi2)(\check{p}\_{i},\check{\Lambda}\_{i})\triangleq\left(\frac{1}{p\_{i}},-\frac{\Lambda\_{i}}{p\_{i}^{2}}\right) solves the linear BSDE

|  |  |  |
| --- | --- | --- |
|  | {d​pˇi=−(−(2​r−ρi2)​pˇi−2​ρi​Λˇi)​d⁡t+Λˇi​d⁡W,t∈[0,T],pˇi​(T)=1.\left\{\begin{aligned} &\mathrm{d}\check{p}\_{i}=-\left(-\left(2r-\rho\_{i}^{2}\right)\check{p}\_{i}-2\rho\_{i}\check{\Lambda}\_{i}\right)\operatorname{d}\!t+\check{\Lambda}\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ &\check{p}\_{i}(T)=1.\end{aligned}\right. |  |

By a simple change of measure, we obtain the explicit expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pˇi​(t)=𝔼​[exp⁡(∫tT−2​ρi​(s)​d⁡W​(s)+∫tT(−2​r​(s)−|ρi​(s)|2)​d⁡s)|ℱt].\check{p}\_{i}(t)=\mathbb{E}\left[\exp\left(\int\_{t}^{T}-2\rho\_{i}(s)\operatorname{d}\!W(s)+\int\_{t}^{T}\left(-2r(s)-|\rho\_{i}(s)|^{2}\right)\operatorname{d}\!s\right)\;\Bigg|\;\mathcal{F}\_{t}\right]. |  | (3.4) |

So pi​(t)=1pˇi​(t)p\_{i}(t)=\frac{1}{\check{p}\_{i}(t)} yields ([3.3](https://arxiv.org/html/2511.05270v1#S3.E3 "In Lemma 3.1. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")).

###### Lemma 3.2.

BSDE ([3.2](https://arxiv.org/html/2511.05270v1#S3.E2 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution

|  |  |  |
| --- | --- | --- |
|  | (hi,ηi)∈S𝔽2​(0,T;ℝ1)×L𝔽2​(0,T;ℝ1).(h\_{i},\eta\_{i})\in S\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{1}\right)\times L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}). |  |

###### Proof.

Notice r∈L𝔽∞​(0,T;ℝ+)r\in L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{+}\right), ρi∈L𝔽∞​(0,T;ℝ1)\rho\_{i}\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}^{1}) and θi​(ρ​σ​π)^i−θi​ρi​(σ​π)^i∈L𝔽2​(0,T;ℝ1)\theta\_{i}\widehat{(\rho\sigma\pi)}\_{i}-\theta\_{i}\rho\_{i}\widehat{(\sigma\pi)}\_{i}\in L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{1}\right). The conclusion follows immediately.

For now on, we fix the solutions (pi,Λi)(p\_{i},\Lambda\_{i}) for BSDE ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and (hi,ηi)(h\_{i},\eta\_{i}) for BSDE ([3.2](https://arxiv.org/html/2511.05270v1#S3.E2 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")). Based on them, we now introduce a non-homogeneous linear SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Zi∗=(r​Zi∗+θi​ρi​(σ​π)^i−θi​(ρ​σ​π)^i−ρi​[ηi+(Λipi+ρi)​(Zi∗+hi)])​d⁡t−(ηi+(Λipi+ρi)​(Zi∗+hi))​d⁡W,t∈[0,T],Zi∗​(0)=zi.\left\{\begin{aligned} \mathrm{d}{Z}^{\*}\_{i}=&\left(r{Z}^{\*}\_{i}+\theta\_{i}\rho\_{i}\widehat{(\sigma\pi)}\_{i}-\theta\_{i}\widehat{(\rho\sigma\pi)}\_{i}-\rho\_{i}[\eta\_{i}+(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i})({Z}^{\*}\_{i}+h\_{i})]\right)\operatorname{d}\!t\\ &-\left(\eta\_{i}+(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i})({Z}^{\*}\_{i}+h\_{i})\right)\operatorname{d}\!W,\quad t\in[0,T],\\ {Z}^{\*}\_{i}(0)&=z\_{i}.\end{aligned}\right. |  | (3.5) |

Note this SDE has unbounded coefficients, so its solvability is not immediately ready.

###### Lemma 3.3.

SDE ([3.5](https://arxiv.org/html/2511.05270v1#S3.E5 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a solution Zi∗∈L𝔽2​(0,T;ℝ1){Z}^{\*}\_{i}\in L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{1}\right).

###### Proof.

Clearly, the following SDE with bounded coefficients admits a unique strong solution Yi∈S𝔽2​(0,T;ℝ1)Y\_{i}\in S\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Yi=−r​Yi​d⁡t−ρi​Yi​d⁡W,t∈[0,T],Yi​(0)=pi​(0)​(zi+hi​(0)).\left\{\begin{aligned} &\mathrm{d}Y\_{i}=-rY\_{i}\operatorname{d}\!t-\rho\_{i}Y\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ &Y\_{i}(0)=p\_{i}(0)\left(z\_{i}+h\_{i}(0)\right).\end{aligned}\right. |  | (3.6) |

Applying Itô’s formula, one can see

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi∗≜Yipi−hi,{Z}^{\*}\_{i}\triangleq\frac{Y\_{i}}{p\_{i}}-h\_{i}, |  | (3.7) |

is a solution in L𝔽2​(0,T;ℝ1)L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}) to the original SDE ([3.5](https://arxiv.org/html/2511.05270v1#S3.E5 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")). Since the above linear transformation is invertible, the uniqueness follows.

Now we are ready to solve the stochastic LQ control problem ([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).

###### Theorem 3.4.

The stochastic LQ control problem ([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) is well-posed, with the unique optimal feedback control given by

|  |  |  |
| --- | --- | --- |
|  | πi∗​(t,Zi)=θi​(σ​π)^iσi−1σi​[ηi+(Λipi+ρi)​(Zi+hi)],\pi\_{i}^{\*}(t,Z\_{i})=\theta\_{i}\frac{\widehat{(\sigma\pi)}\_{i}}{\sigma\_{i}}-\frac{1}{\sigma\_{i}}\left[\eta\_{i}+(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i})(Z\_{i}+h\_{i})\right], |  |

and its corresponding optimal cost functional given by

|  |  |  |
| --- | --- | --- |
|  | 𝒥i​[πi∗]=pi​(0)​|zi+hi​(0)|2,\mathscr{J}\_{i}[\pi\_{i}^{\*}]=p\_{i}(0)|z\_{i}+h\_{i}(0)|^{2}, |  |

where πi∗=πi∗​(t,Zi∗)\pi\_{i}^{\*}=\pi^{\*}\_{i}(t,Z\_{i}^{\*}) and Zi∗Z^{\*}\_{i} is determined by ([3.5](https://arxiv.org/html/2511.05270v1#S3.E5 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")).

###### Proof.

One can check the pair (πi∗,Zi∗)(\pi^{\*}\_{i},Z^{\*}\_{i}) satisfies the state equation ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).
Applying Lemma [3.3](https://arxiv.org/html/2511.05270v1#S3.Thmthm3 "Lemma 3.3. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion"), we can get πi∗∈𝒰\pi\_{i}^{\*}\in\mathcal{U}.
For any πi∈𝒰\pi\_{i}\in\mathcal{U}, let ZiZ\_{i} denote the corresponding state determined by ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).
Applying Itô’s formula to pi​|Zi+hi|2p\_{i}|Z\_{i}+h\_{i}|^{2},
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(pi​(Zi+hi)2)=\displaystyle\mathrm{d}\left(p\_{i}(Z\_{i}+h\_{i})^{2}\right)= | pi​σi2​|πi−πi∗|2​d⁡t\displaystyle p\_{i}\sigma\_{i}^{2}|\pi\_{i}-\pi\_{i}^{\*}|^{2}\operatorname{d}\!t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(|Zi+hi|2​Λi+2​p​(Zi+hi)​(σi​πi−θi​(σ​π)^i+ηi))​d⁡W.\displaystyle+\left(|Z\_{i}+h\_{i}|^{2}\Lambda\_{i}+2p(Z\_{i}+h\_{i})(\sigma\_{i}\pi\_{i}-\theta\_{i}\widehat{(\sigma\pi)}\_{i}+\eta\_{i})\right)\operatorname{d}\!W. |  |

It yields that

|  |  |  |
| --- | --- | --- |
|  | 𝒥i​(πi)=pi​(0)​|zi+hi​(0)|2+𝔼​[∫0Tpi​σi2​|πi−πi∗|2​d⁡t].\displaystyle\mathscr{J}\_{i}(\pi\_{i})=p\_{i}(0)|z\_{i}+h\_{i}(0)|^{2}+\mathbb{E}\left[\int\_{0}^{T}p\_{i}\sigma\_{i}^{2}|\pi\_{i}-\pi\_{i}^{\*}|^{2}\operatorname{d}\!t\right]. |  |

Since (πi∗,Zi∗)(\pi^{\*}\_{i},Z^{\*}\_{i}) satisfies the state equation ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), it implies that

|  |  |  |
| --- | --- | --- |
|  | 𝒥i​[πi∗]=pi​(0)​|zi+hi​(0)|2.\mathscr{J}\_{i}[\pi\_{i}^{\*}]=p\_{i}(0)|z\_{i}+h\_{i}(0)|^{2}. |  |

The above two equations confirm the optimality of πi∗\pi\_{i}^{\*}.

Next we turn to the constrained optimization problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")). We first establish the feasible condition for it, i.e. for a given target dd, there exists an admissible portfolio πi∈𝒰\pi\_{i}\in\mathcal{U} satisfying 𝔼​[Zi​(T)]=d\mathbb{E}[Z\_{i}(T)]=d.

###### Theorem 3.5.

The constrained LQ Problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) is feasible for any d∈ℝ1d\in\mathbb{R}^{1} if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​∫0T|ρi​(t)​ψ​(t)+ξ​(t)|2​d⁡t>0,\mathbb{E}\int\_{0}^{T}\left|\rho\_{i}(t)\psi(t)+\xi(t)\right|^{2}\operatorname{d}\!t>0, |  | (3.8) |

where (ψ,ξ)∈L𝔽∞​(0,T;ℝ≫1)×L𝔽2​(0,T;ℝ1)(\psi,\xi)\in L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{\gg 1}\right)\times L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}) is the unique solution to the linear BSDE

|  |  |  |
| --- | --- | --- |
|  | {d​ψ=−r​ψ​d⁡t+ξ​d⁡W,t∈[0,T],ψ​(T)=1.\left\{\begin{array}[]{l}\mathrm{d}\psi=-r\psi\operatorname{d}\!t+\xi\operatorname{d}\!W,\quad t\in[0,T],\\ \psi(T)=1.\end{array}\right. |  |

###### Proof.

Since σi∈L𝔽∞​(0,T;ℝ≫1)\sigma\_{i}\in L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}\_{\gg 1}\right), we claim that the feasible condition ([3.8](https://arxiv.org/html/2511.05270v1#S3.E8 "In Theorem 3.5. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​∫0T|ρi​(t)​σi​(t)​ψ​(t)+σi​(t)​ξ​(t)|2​d⁡t>0.\mathbb{E}\int\_{0}^{T}\left|\rho\_{i}(t)\sigma\_{i}(t)\psi(t)+\sigma\_{i}(t)\xi(t)\right|^{2}\operatorname{d}\!t>0. |  | (3.9) |

For any admissible πi∈𝒰\pi\_{i}\in\mathcal{U} and β∈ℝ1\beta\in\mathbb{R}^{1}, define the scaled portfolio πiβ≜β​πi\pi\_{i}^{\beta}\triangleq\beta\pi\_{i}. Denote by ZiβZ\_{i}^{\beta} the wealth process corresponding to πiβ\pi\_{i}^{\beta}. Then for t∈[0,T]t\in[0,T], Ziβ​(t)=β​x​(t)+y​(t)Z\_{i}^{\beta}(t)=\beta x(t)+y(t), where xx and yy satisfy

|  |  |  |
| --- | --- | --- |
|  | {d​x=(r​x+ρi​σi​πi)​d⁡t+σi​πi​d⁡W,t∈[0,T],x​(0)=0,\left\{\begin{aligned} \mathrm{d}x&=\left(rx+\rho\_{i}\sigma\_{i}\pi\_{i}\right)\operatorname{d}\!t+\sigma\_{i}\pi\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ \quad x(0)&=0,\end{aligned}\right. |  |

and

|  |  |  |
| --- | --- | --- |
|  | {d​y=[r​y−θi​(ρ​σ​π)^i]​d⁡t−θi​(σ​π)^i​d⁡W,t∈[0,T],y​(0)=zi.\left\{\begin{aligned} \mathrm{d}y&=\left[ry-\theta\_{i}\widehat{(\rho\sigma\pi)}\_{i}\right]\operatorname{d}\!t-\theta\_{i}\widehat{(\sigma\pi)}\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ \quad y(0)&=z\_{i}.\end{aligned}\right. |  |

Then we have 𝔼​[Ziβ​(T)]=β​𝔼​[x​(T)]+𝔼​[y​(T)]\mathbb{E}[Z\_{i}^{\beta}(T)]=\beta\mathbb{E}[x(T)]+\mathbb{E}[y(T)], where 𝔼​[y​(T)]\mathbb{E}[y(T)] is independent of πi\pi\_{i} and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[x​(T)]=𝔼​∫0T[ρi​(t)​ψ​(t)+ξ​(t)]​σi​(t)​πi​(t)​d⁡t.\mathbb{E}[x(T)]=\mathbb{E}\int\_{0}^{T}[\rho\_{i}(t)\psi(t)+\xi(t)]\sigma\_{i}(t)\pi\_{i}(t)\operatorname{d}\!t. |  |

We first prove the “if” part. For t∈[0,T]t\in[0,T], taking πi​(t)=σi​(t)​[ρi​(t)​ψ​(t)+ξ​(t)]\pi\_{i}(t)=\sigma\_{i}(t)[\rho\_{i}(t)\psi(t)+\xi(t)] in above equality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[x​(T)]=𝔼​∫0T|ρi​(t)​σi​(t)​ψ​(t)+σi​(t)​ξ​(t)|2​d⁡t>0.\mathbb{E}[x(T)]=\mathbb{E}\int\_{0}^{T}\left|\rho\_{i}(t)\sigma\_{i}(t)\psi(t)+\sigma\_{i}(t)\xi(t)\right|^{2}\operatorname{d}\!t>0. |  |

Hence for any d∈ℝ1d\in\mathbb{R}^{1}, there exists β∈ℝ1\beta\in\mathbb{R}^{1} such that 𝔼​[Ziβ​(T)]=d\mathbb{E}[Z\_{i}^{\beta}(T)]=d, and thus πiβ∈𝒰\pi\_{i}^{\beta}\in\mathcal{U} satisfying 𝔼​[Zi​(T)]=𝔼​[x​(T)]+𝔼​[y​(T)]=d\mathbb{E}[Z\_{i}(T)]=\mathbb{E}[x(T)]+\mathbb{E}[y(T)]=d.

For “only if” part, assume that problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) is feasible for any d∈ℝ1d\in\mathbb{R}^{1}, then there exists a πi∈𝒰\pi\_{i}\in\mathcal{U} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[x​(T)]=𝔼​∫0T[ρi​(t)​ψ​(t)+ξ​(t)]​σi​(t)​πi​(t)​d⁡t≠0,\mathbb{E}[x(T)]=\mathbb{E}\int\_{0}^{T}[\rho\_{i}(t)\psi(t)+\xi(t)]\sigma\_{i}(t)\pi\_{i}(t)\operatorname{d}\!t\neq 0, |  |

which implies that ([3.9](https://arxiv.org/html/2511.05270v1#S3.E9 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) is true.

###### Remark 3.1.

From Theorem [3.5](https://arxiv.org/html/2511.05270v1#S3.Thmthm5 "Theorem 3.5. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion"), we see that if the feasible condition ([3.8](https://arxiv.org/html/2511.05270v1#S3.E8 "In Theorem 3.5. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) does not hold, there is only one feasible target dd for the constrained LQ Problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")). To avoid this trivial case, we always assume the feasible condition ([3.8](https://arxiv.org/html/2511.05270v1#S3.E8 "In Theorem 3.5. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) holds from now on, which allows us to deal with the constraint 𝔼​[Zi​(T)]=d\mathbb{E}[Z\_{i}(T)]=d by the Lagrangian method.

To move forward on the solvability of constrained optimization problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), we decompose BSDE ([3.2](https://arxiv.org/html/2511.05270v1#S3.E2 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) into two components as follows:

|  |  |  |
| --- | --- | --- |
|  | hi=h~i+(d−λ)​hˇiandηi=η~i+(d−λ)​ηˇi,h\_{i}=\tilde{h}\_{i}+(d-\lambda)\check{h}\_{i}\ \ {\rm and}\ \ \eta\_{i}=\tilde{\eta}\_{i}+(d-\lambda)\check{\eta}\_{i}, |  |

where (h~i,η~i)(\tilde{h}\_{i},\tilde{\eta}\_{i}) and (hˇi,ηˇi)(\check{h}\_{i},\check{\eta}\_{i}) solve the following two linear BSDEs

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​h~i=[r​h~i+θi​(ρ​σ​π)^i−θi​ρi​(σ​π)^i+ρi​η~i]​d⁡t+η~i​d⁡W,t∈[0,T],h~i​(T)=0,\left\{\begin{array}[]{l}\mathrm{d}\tilde{h}\_{i}=\left[r\tilde{h}\_{i}+\theta\_{i}\widehat{(\rho\sigma\pi)}\_{i}-\theta\_{i}\rho\_{i}\widehat{(\sigma\pi)}\_{i}+\rho\_{i}\tilde{\eta}\_{i}\right]\operatorname{d}\!t+\tilde{\eta}\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ \tilde{h}\_{i}(T)=0,\end{array}\right. |  | (3.10) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​hˇi=(r​hˇi+ρi​ηˇi)​d⁡t+ηˇi​d⁡W,t∈[0,T],hˇi​(T)=−1.\left\{\begin{array}[]{l}\mathrm{d}\check{h}\_{i}=\left(r\check{h}\_{i}+\rho\_{i}\check{\eta}\_{i}\right)\operatorname{d}\!t+\check{\eta}\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ \check{h}\_{i}(T)=-1.\end{array}\right. |  | (3.11) |

For the stochastic LQ control problem ([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), the unique optimal feedback control can be written as

|  |  |  |
| --- | --- | --- |
|  | πi∗=θi​(σ​π)^iσi−1σi​[η~i+(d−λ)​ηˇi+(Λipi+ρi)​(Zi∗+h~i+(d−λ)​hˇi)],\pi\_{i}^{\*}=\theta\_{i}\frac{\widehat{(\sigma\pi)}\_{i}}{\sigma\_{i}}-\frac{1}{\sigma\_{i}}\left[\tilde{\eta}\_{i}+(d-\lambda)\check{\eta}\_{i}+(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i})(Z^{\*}\_{i}+\tilde{h}\_{i}+(d-\lambda)\check{h}\_{i})\right], |  |

with the corresponding cost functional

|  |  |  |
| --- | --- | --- |
|  | 𝒥i​[πi∗]=pi​(0)​|zi+hi​(0)|2=pi​(0)​|zi+h~i​(0)+(d−λ)​hˇi​(0)|2.\mathscr{J}\_{i}[\pi\_{i}^{\*}]=p\_{i}(0)|z\_{i}+h\_{i}(0)|^{2}=p\_{i}(0)|z\_{i}+\tilde{h}\_{i}(0)+(d-\lambda)\check{h}\_{i}(0)|^{2}. |  |

By Proposition 3.5 in [[14](https://arxiv.org/html/2511.05270v1#bib.bib14)], the inequality pi​(0)​hˇi​(0)2<1p\_{i}(0)\check{h}\_{i}(0)^{2}<1 holds.
By Proposition 4.1 in [[14](https://arxiv.org/html/2511.05270v1#bib.bib14)], BSDE ([3.11](https://arxiv.org/html/2511.05270v1#S3.E11 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (hˇi,ηˇi)∈L𝔽∞​(0,T;ℝ≪−1)×L𝔽2​(0,T;ℝ1)(\check{h}\_{i},\check{\eta}\_{i})\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}\_{\ll-1})\times L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | hˇi​(t)=−𝔼​[exp⁡(∫tT−ρi​d⁡W+∫tT(−r−ρi22)​d⁡s)|ℱt].\displaystyle\check{h}\_{i}(t)=-\mathbb{E}\bigg[\exp\bigg(\int\_{t}^{T}-\rho\_{i}\operatorname{d}\!W+\int\_{t}^{T}(-r-\frac{\rho\_{i}^{2}}{2})\operatorname{d}\!s\bigg)\;\bigg|\;\mathcal{F}\_{t}\bigg]. |  | (3.12) |

The assumption on the feasible condition ([3.8](https://arxiv.org/html/2511.05270v1#S3.E8 "In Theorem 3.5. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) allows us to solve the constrained control problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) by solving ([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) for a fixed mean 𝔼​[Zi​(T)]=d\mathbb{E}[Z\_{i}(T)]=d. By the Lagrange duality theorem, the minimization problem ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) is equivalent to the unconstrained maximization problem

|  |  |  |
| --- | --- | --- |
|  | minπi​(⋅)∈𝒰,𝔼​[Zi​(T)]=d⁡Var⁡(Zi​(T))=maxλ∈ℝ1⁡minπi​(⋅)∈𝒰⁡Ji​(πi,λ).\min\_{\pi\_{i}(\cdot)\in\mathcal{U},\mathbb{E}[Z\_{i}(T)]=d}\operatorname{Var}(Z\_{i}(T))=\max\_{\lambda\in\mathbb{R}^{1}}\min\_{\pi\_{i}(\cdot)\in\mathcal{U}}J\_{i}(\pi\_{i},\lambda). |  |

In particular, by ([2.6](https://arxiv.org/html/2511.05270v1#S2.E6 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), ([2.7](https://arxiv.org/html/2511.05270v1#S2.E7 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) and Theorem [3.4](https://arxiv.org/html/2511.05270v1#S3.Thmthm4 "Theorem 3.4. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion"), we have

|  |  |  |
| --- | --- | --- |
|  | minπi​(⋅)∈𝒰⁡Ji​(πi,λ)=Ji​(πi∗,λ)=𝒥i​[πi∗​(⋅)]−λ2=pi​(0)​|zi+h~i​(0)+(d−λ)​hˇi​(0)|2−λ2.\min\_{\pi\_{i}(\cdot)\in\mathcal{U}}J\_{i}(\pi\_{i},\lambda)=J\_{i}(\pi\_{i}^{\*},\lambda)=\mathscr{J}\_{i}[\pi\_{i}^{\*}(\cdot)]-\lambda^{2}=p\_{i}(0)|z\_{i}+\tilde{h}\_{i}(0)+(d-\lambda)\check{h}\_{i}(0)|^{2}-\lambda^{2}. |  |

Thanks to pi​(0)​hˇi​(0)2<1p\_{i}(0)\check{h}\_{i}(0)^{2}<1, the maximum of λ↦Ji​(πi∗,λ)\lambda\mapsto J\_{i}(\pi\_{i}^{\*},\lambda) is attained at the optimal Lagrange multiplier

|  |  |  |
| --- | --- | --- |
|  | λ∗=pi​(0)​hˇi​(0)​(zi+h~i​(0)+hˇi​(0)​d)pi​(0)​|hˇi​(0)|2−1,\lambda^{\*}=\frac{p\_{i}(0)\check{h}\_{i}(0)\left(z\_{i}+\tilde{h}\_{i}(0)+\check{h}\_{i}(0)d\right)}{p\_{i}(0)|\check{h}\_{i}(0)|^{2}-1}, |  |

which gives the optimal value of ([2.5](https://arxiv.org/html/2511.05270v1#S2.E5 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) as

|  |  |  |
| --- | --- | --- |
|  | pi​(0)​|zi+h~i​(0)+hˇi​(0)​d|21−pi​(0)​|hˇi​(0)|2.\frac{p\_{i}(0)|z\_{i}+\tilde{h}\_{i}(0)+\check{h}\_{i}(0)d|^{2}}{1-p\_{i}(0)|\check{h}\_{i}(0)|^{2}}. |  |

Finally, let us study the MV portfolio selection problem ([2.4](https://arxiv.org/html/2511.05270v1#S2.E4 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")). We only need to solve

|  |  |  |
| --- | --- | --- |
|  | maxd∈ℝ1⁡(d−γi2⋅pi​(0)​|zi+h~i​(0)+hˇi​(0)​d|21−pi​(0)​|hˇi​(0)|2),\max\_{d\in\mathbb{R}^{1}}\left(d-\frac{\gamma\_{i}}{2}\cdot\frac{p\_{i}(0)|z\_{i}+\tilde{h}\_{i}(0)+\check{h}\_{i}(0)d|^{2}}{1-p\_{i}(0)|\check{h}\_{i}(0)|^{2}}\right), |  |

which attains its maximum

|  |  |  |
| --- | --- | --- |
|  | 1−pi​(0)​|hˇi​(0)|22​γi​pi​(0)​|hˇi​(0)|2−zi+h~i​(0)hˇi​(0),\frac{1-p\_{i}(0)|\check{h}\_{i}(0)|^{2}}{2\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}}-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}, |  |

at the optimal mean

|  |  |  |
| --- | --- | --- |
|  | d∗=1γi​(1pi​(0)​|hˇi​(0)|2−1)−zi+h~i​(0)hˇi​(0).d^{\*}=\frac{1}{\gamma\_{i}}\left(\frac{1}{p\_{i}(0)|\check{h}\_{i}(0)|^{2}}-1\right)-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}. |  |

In this way, we know

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗−λ∗=−zi+h~i​(0)hˇi​(0)+1γi​pi​(0)​|hˇi​(0)|2.d^{\*}-\lambda^{\*}=-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}+\frac{1}{\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}}. |  | (3.13) |

Therefore, for problem ([2.4](https://arxiv.org/html/2511.05270v1#S2.E4 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), the linear optimal feedback control for agent ii is

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi∗=θi(σ​π∗)^iσi−1σi[η~i+(−zi+h~i​(0)hˇi​(0)+1γi​pi​(0)​|hˇi​(0)|2)ηˇi+(Λipi+ρi)(Zi∗+h~i+(−zi+h~i​(0)hˇi​(0)+1γi​pi​(0)​|hˇi​(0)|2)hˇi)].\pi\_{i}^{\*}=\theta\_{i}\frac{\widehat{(\sigma\pi^{\*})}\_{i}}{\sigma\_{i}}-\frac{1}{\sigma\_{i}}\bigg[\tilde{\eta}\_{i}+(-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}+\frac{1}{\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}})\check{\eta}\_{i}\\ +(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i})\bigg(Z^{\*}\_{i}+\tilde{h}\_{i}+(-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}+\frac{1}{\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}})\check{h}\_{i}\bigg)\bigg]. |  | (3.14) |

## 4 Solving the Nash Equilibrium

In Section [3](https://arxiv.org/html/2511.05270v1#S3 "3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion"), we deal with the mena-variance problem by fixing the other n−1n-1 agents’ strategies, while in this section, we study the Nash equilibrium of the MV portfolio selection problem ([2.4](https://arxiv.org/html/2511.05270v1#S2.E4 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")). It means that we need to find out a vector portfolio strategy 𝝅∗=(π1∗,π2∗,⋯,πn∗)⊤∈L𝔽2​(0,T;ℝn)\boldsymbol{\pi^{\*}}=(\pi^{\*}\_{1},\pi^{\*}\_{2},\cdots,\pi^{\*}\_{n})^{\top}\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}) such that ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) is satisfied for all i=1,2,⋯,ni=1,2,\cdots,n.

Needless to say, it is much more complicated to solve the Nash equilibrium than to solve a single MV problem. Notice that the coefficients of BSDEs ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and BSDEs ([3.11](https://arxiv.org/html/2511.05270v1#S3.E11 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) only depend on market parameters rather than portfolio strategies, but SDEs ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and linear optimal feedback controls ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) constitute a coupled system. Hence the key point is to establish the well-posedness of this coupled system.

We start from decoupling SDEs ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")).
Due to ([3.13](https://arxiv.org/html/2511.05270v1#S3.E13 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), we have

|  |  |  |
| --- | --- | --- |
|  | hi​(0)=h~i​(0)+hˇi​(0)​(−zi+h~i​(0)hˇi​(0)+1γi​pi​(0)​|hˇi​(0)|2)=−zi+1γi​pi​(0)​hˇi​(0).h\_{i}(0)=\tilde{h}\_{i}(0)+\check{h}\_{i}(0)\left(-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}+\frac{1}{\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}}\right)=-z\_{i}+\frac{1}{\gamma\_{i}p\_{i}(0)\check{h}\_{i}(0)}. |  |

Rewritten SDEs ([3.6](https://arxiv.org/html/2511.05270v1#S3.E6 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) as (here and hereafter, we use Yi∗Y^{\*}\_{i} instead of YiY\_{i} in the discussion of Nash equilibrium):

|  |  |  |
| --- | --- | --- |
|  | {d​Yi∗=−r​Yi∗​d⁡t−ρi​Yi∗​d⁡W,t∈[0,T],Yi∗​(0)=1γi​hˇi​(0),\left\{\begin{aligned} \mathrm{d}Y^{\*}\_{i}&=-rY^{\*}\_{i}\operatorname{d}\!t-\rho\_{i}Y^{\*}\_{i}\operatorname{d}\!W,\quad t\in[0,T],\\ Y^{\*}\_{i}(0)&=\frac{1}{\gamma\_{i}\check{h}\_{i}(0)},\end{aligned}\right. |  |

with the explicit expression

|  |  |  |
| --- | --- | --- |
|  | Yi∗​(t)=1γi​hˇi​(0)​exp⁡(∫0t−ρi​(s)​d⁡W​(s)+∫0t(−r​(s)−ρi​(s)22)​d⁡s),t∈[0,T],Y^{\*}\_{i}(t)=\frac{1}{\gamma\_{i}\check{h}\_{i}(0)}\exp\left(\int\_{0}^{t}-\rho\_{i}(s)\operatorname{d}\!W(s)+\int\_{0}^{t}\left(-r(s)-\frac{\rho\_{i}(s)^{2}}{2}\right)\operatorname{d}\!s\right),\quad t\in[0,T], |  |

which only depends on market parameters, and is independent of portfolio strategies of all agents.
Substituting ([3.7](https://arxiv.org/html/2511.05270v1#S3.E7 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) into the optimal feedback controls ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi∗=θi​(σ​π∗)^iσi−1σi​[η~i+(−zi+h~i​(0)hˇi​(0)+1γi​pi​(0)​|hˇi​(0)|2)​ηˇi+(Λipi+ρi)​Yi∗pi].\pi\_{i}^{\*}=\theta\_{i}\frac{\widehat{(\sigma\pi^{\*})}\_{i}}{\sigma\_{i}}-\frac{1}{\sigma\_{i}}\left[\tilde{\eta}\_{i}+\left(-\frac{z\_{i}+\tilde{h}\_{i}(0)}{\check{h}\_{i}(0)}+\frac{1}{\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}}\right)\check{\eta}\_{i}+(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i})\frac{Y^{\*}\_{i}}{p\_{i}}\right]. |  | (4.1) |

After decoupling SDEs ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) from the coupled system, we obtain the system of linear equations ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) of unknown variables πi∗\pi\_{i}^{\*}, i=1,2,⋯,ni=1,2,\cdots,n, coupled with BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")). Next, we further decouple BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) by giving explicit forms of πi∗\pi\_{i}^{\*}, i=1,2,⋯,ni=1,2,\cdots,n, with the help of ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")).

For this, define two constants

|  |  |  |
| --- | --- | --- |
|  | Ψ≜∑i=1nθin−1+θi∈[0,1],γ^≜∑i=1n1γi,\Psi\triangleq\sum\_{i=1}^{n}\frac{\theta\_{i}}{n-1+\theta\_{i}}\in[0,1],\quad\hat{\gamma}\triangleq\sum\_{i=1}^{n}\frac{1}{\gamma\_{i}}, |  |

and three average quantities

|  |  |  |
| --- | --- | --- |
|  | σ​π∗¯≜1n​∑k=1nσk​πk∗,x¯≜1n​∑k=1nxk,ρ¯≜1n​∑i=1nρi.\overline{\sigma\pi^{\*}}\triangleq\frac{1}{n}\sum\_{k=1}^{n}\sigma\_{k}\pi^{\*}\_{k},\quad\bar{x}\triangleq\frac{1}{n}\sum\_{k=1}^{n}x\_{k},\quad\bar{\rho}\triangleq\frac{1}{n}\sum\_{i=1}^{n}\rho\_{i}. |  |

Substitute ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) into σ​π∗¯\overline{\sigma\pi^{\*}}, and it yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​πi∗=θi​n​σ​π∗¯−σi​πi∗n−1−ϕi,\sigma\_{i}\pi^{\*}\_{i}=\theta\_{i}\frac{n\overline{\sigma\pi^{\*}}-\sigma\_{i}\pi^{\*}\_{i}}{n-1}-\phi\_{i}, |  | (4.2) |

where

|  |  |  |
| --- | --- | --- |
|  | ϕi≜η~i+ci​h~i​(0)+fi,\phi\_{i}\triangleq\tilde{\eta}\_{i}+c\_{i}\tilde{h}\_{i}(0)+f\_{i}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | ci=−ηˇihˇi​(0),fi=(−zihˇi​(0)+1γi​pi​(0)​|hˇi​(0)|2)​ηˇi+(Λipi+ρi)​Yi∗pi.c\_{i}=-\frac{\check{\eta}\_{i}}{\check{h}\_{i}(0)},\quad f\_{i}=\left(-\frac{z\_{i}}{\check{h}\_{i}(0)}+\frac{1}{\gamma\_{i}p\_{i}(0)|\check{h}\_{i}(0)|^{2}}\right)\check{\eta}\_{i}+\left(\frac{\Lambda\_{i}}{p\_{i}}+\rho\_{i}\right)\frac{Y^{\*}\_{i}}{p\_{i}}. |  |

The equality ([4.2](https://arxiv.org/html/2511.05270v1#S4.E2 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​πi∗=n​θin−1+θi​σ​π∗¯−ϕi1+θin−1.\sigma\_{i}\pi^{\*}\_{i}=\frac{n\theta\_{i}}{n-1+\theta\_{i}}\overline{\sigma\pi^{\*}}-\frac{\phi\_{i}}{1+\frac{\theta\_{i}}{n-1}}. |  | (4.3) |

Sum up all agents, and then divide by nn. It turns out that

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​π∗¯=Ψ​σ​π∗¯−1n​∑i=1nϕi1+θin−1.\overline{\sigma\pi^{\*}}=\Psi\overline{\sigma\pi^{\*}}-\frac{1}{n}\sum\_{i=1}^{n}\frac{\phi\_{i}}{1+\frac{\theta\_{i}}{n-1}}. |  | (4.4) |

So it can be seen from above that the solvability of ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) depends on the value of Ψ\Psi. Then we will discuss the solvability of ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) in the usual case Ψ<1\Psi<1 and in the marginal case Ψ=1\Psi=1, respectively.

### 4.1 The usual case

For Ψ<1\Psi<1,
substituting the average control σ​π∗¯\overline{\sigma\pi^{\*}} obtained in ([4.4](https://arxiv.org/html/2511.05270v1#S4.E4 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) into ([4.3](https://arxiv.org/html/2511.05270v1#S4.E3 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​πi∗=−11−Ψ​n​θin−1+θi​∑i=1nϕin+n​θin−1−ϕi1+θin−1.\sigma\_{i}\pi^{\*}\_{i}=-\frac{1}{1-\Psi}\frac{n\theta\_{i}}{n-1+\theta\_{i}}\sum\_{i=1}^{n}\frac{\phi\_{i}}{n+\frac{n\theta\_{i}}{n-1}}-\frac{\phi\_{i}}{1+\frac{\theta\_{i}}{n-1}}. |  | (4.5) |

Then the terms θi​(ρ​σ​π∗)^i−θi​ρi​(σ​π∗)^i\theta\_{i}\widehat{(\rho\sigma\pi^{\*})}\_{i}-\theta\_{i}\rho\_{i}\widehat{(\sigma\pi^{\*})}\_{i} can be given explicitly as a linear combination of h~j\tilde{h}\_{j}, η~j\tilde{\eta}\_{j} and h~j​(0)\tilde{h}\_{j}(0) for j=1,2,⋯,nj=1,2,\cdots,n.

Set 𝒉~≜(h~1,h~2,⋯,h~n)⊤\tilde{\boldsymbol{h}}\triangleq(\tilde{h}\_{1},\tilde{h}\_{2},\cdots,\tilde{h}\_{n})^{\top} and 𝜼~≜(η~1,η~2,⋯,η~n)⊤\tilde{\boldsymbol{\eta}}\triangleq(\tilde{\eta}\_{1},\tilde{\eta}\_{2},\cdots,\tilde{\eta}\_{n})^{\top}. BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝒉~=−[A​𝒉~+B​𝜼~+C​𝒉~​(0)+F]​d⁡t+𝜼~​d⁡W,t∈[0,T],𝒉~​(T)=0,\left\{\begin{array}[]{l}\mathrm{d}\tilde{\boldsymbol{h}}=-\left[A\tilde{\boldsymbol{h}}+B\tilde{\boldsymbol{\eta}}+C\tilde{\boldsymbol{h}}(0)+F\right]\operatorname{d}\!t+\tilde{\boldsymbol{\eta}}\operatorname{d}\!W,\quad t\in[0,T],\\ \tilde{\boldsymbol{h}}(T)=0,\end{array}\right. |  | (4.6) |

where AA, BB, and CC are coefficient matrices,
and FF is a coefficient vector.
Precisely, for i,j=1,2,⋯,ni,j=1,2,\cdots,n,

|  |  |  |
| --- | --- | --- |
|  | Ai​j≜{0,i≠j,−r,i=j,Bi​j≜{θi​Mi​j,i≠j,θi​Mi​i−ρi,i=j,A\_{ij}\triangleq\left\{\begin{aligned} 0,\ \ \ \ \ &i\neq j,\\ -r,\ \ \ &i=j,\end{aligned}\right.\ \ \ \ \ B\_{ij}\triangleq\left\{\begin{aligned} \theta\_{i}M\_{ij},\ \ \ \ \ \ \ \ \ &i\neq j,\\ \theta\_{i}M\_{ii}-\rho\_{i},\ \ \ &i=j,\end{aligned}\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Ci​j≜{θi​Mi​j​cj,i≠j,θi​Mi​i​ci,i=j,Fi≜θi(Mi​ifi+∑i≠jMi​jfj),C\_{ij}\triangleq\left\{\begin{aligned} \theta\_{i}M\_{ij}c\_{j},\ \ \ &i\neq j,\\ \theta\_{i}M\_{ii}c\_{i},\ \ \ &i=j,\end{aligned}\right.\ \ \ \ \ F\_{i}\triangleq\theta\_{i}(M\_{ii}f\_{i}+\sum\_{i\neq j}M\_{ij}f\_{j}), |  |

with

|  |  |  |
| --- | --- | --- |
|  | Mi​j≜{1n−1​11−Ψ​∑k≠i(n−1)​θk​(ρk−ρi)(n−1+θk)​(n−1+θj)−(n−1)(ρj−ρi))n−1+θj,i≠j,1n−1​11−Ψ​∑k≠i(n−1)​θk​(ρk−ρi)(n−1+θk)​(n−1+θi),i=j.M\_{ij}\triangleq\left\{\begin{aligned} \frac{1}{n-1}\frac{1}{1-\Psi}\sum\_{k\neq i}\frac{(n-1)\theta\_{k}(\rho\_{k}-\rho\_{i})}{(n-1+\theta\_{k})(n-1+\theta\_{j})}-\frac{(n-1)(\rho\_{j}-\rho\_{i}))}{n-1+\theta\_{j}},\ \ \ &i\neq j,\\ \frac{1}{n-1}\frac{1}{1-\Psi}\sum\_{k\neq i}\frac{(n-1)\theta\_{k}(\rho\_{k}-\rho\_{i})}{(n-1+\theta\_{k})(n-1+\theta\_{i})},\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ &i=j.\end{aligned}\right. |  |

Obviously A∈L𝔽∞​(0,T;ℝn×n)A\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}^{n\times n}), B∈L𝔽∞​(0,T;ℝn×n)B\in L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}^{n\times n}\right), C∈L𝔽2​(0,T;ℝn×n)C\in L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n\times n}\right) and F∈L𝔽2​(0,T;ℝn)F\in L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n}\right).

Note that ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is a new type of BSDE since its driver depends on 𝒉~​(0)\tilde{\boldsymbol{h}}(0). In Lemma [A.1](https://arxiv.org/html/2511.05270v1#A1.E1 "In Lemma A.1. ‣ Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion") in Appendix [A](https://arxiv.org/html/2511.05270v1#A1 "Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion"), the solvability of an extended class of general nonlinear BSDEs in the solution space S𝔽2​(0,T;ℝn)×L𝔽2​(0,T;ℝn)S\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n})\times L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}) is established by the fixed-point method for sufficiently small T>0T>0. Given 𝒉~​(0)\tilde{\boldsymbol{h}}(0), due to the linear structure of BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), its explicit solution can be obtained for any given T>0T>0.
For this, we introduce an SDE with solution in L𝔽2​(0,T;ℝn×n)L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n\times n}):

|  |  |  |
| --- | --- | --- |
|  | {d​Γ=Γ​[A​d⁡t+B​d⁡W],t∈[0,T],Γ​(0)=In.\left\{\begin{aligned} \mathrm{d}\Gamma&=\Gamma\left[A\operatorname{d}\!t+B\operatorname{d}\!W\right],\quad t\in[0,T],\\ \Gamma(0)&=I\_{n}.\end{aligned}\right. |  |

For the solution Γ\Gamma to the above SDE, its inverse flow Γ−1\Gamma^{-1} satisfies another SDE:

|  |  |  |
| --- | --- | --- |
|  | {d​Γ−1=Γ−1​[(−A+B2)​d⁡t−B​d⁡W],t∈[0,T],Γ−1​(0)=In.\left\{\begin{aligned} \mathrm{d}\Gamma^{-1}&=\Gamma^{-1}[\left(-A+B^{2}\right)\operatorname{d}\!t-B\operatorname{d}\!W],\quad t\in[0,T],\\ \Gamma^{-1}(0)&=I\_{n}.\end{aligned}\right. |  |

Applying Itô’s formula to Γ​𝒉~\Gamma\tilde{\boldsymbol{h}}, we have

|  |  |  |
| --- | --- | --- |
|  | d​(Γ​𝒉~)=−Γ​(C​𝒉~​(0)+F)​d⁡t+Γ​(𝜼~+B​𝒉~)​d⁡W.\mathrm{d}(\Gamma\tilde{\boldsymbol{h}})=-\Gamma\left(C\tilde{\boldsymbol{h}}(0)+F\right)\operatorname{d}\!t+\Gamma(\tilde{\boldsymbol{\eta}}+B\tilde{\boldsymbol{h}})\operatorname{d}\!W. |  |

Noticing 𝒉~​(T)=0\tilde{\boldsymbol{h}}(T)=0, we have

|  |  |  |
| --- | --- | --- |
|  | 𝒉~​(t)=Γ−1​(t)​𝔼​[∫tTΓ​(s)​(C​(s)​𝒉~​(0)+F​(s))​d⁡s|ℱt].\tilde{\boldsymbol{h}}(t)=\Gamma^{-1}(t)\mathbb{E}\left[\int\_{t}^{T}\Gamma(s)\left(C(s)\tilde{\boldsymbol{h}}(0)+F(s)\right)\operatorname{d}\!s\,\bigg|\,\mathcal{F}\_{t}\right]. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | 𝒉~​(0)=𝔼​[∫0TΓ​(s)​(C​(s)​𝒉~​(0)+F​(s))​d⁡s].\tilde{\boldsymbol{h}}(0)=\mathbb{E}\left[\int\_{0}^{T}\Gamma(s)\left(C(s)\tilde{\boldsymbol{h}}(0)+F(s)\right)\operatorname{d}\!s\right]. |  |

Set K≜𝔼​[∫0TΓ​(s)​C​(s)​d⁡s]K\triangleq\mathbb{E}\big[\int\_{0}^{T}\Gamma(s)C(s)\operatorname{d}\!s\big] and D≜𝔼​[∫0TΓ​(s)​F​(s)​d⁡s]D\triangleq\mathbb{E}\big[\int\_{0}^{T}\Gamma(s)F(s)\operatorname{d}\!s\big], then

|  |  |  |
| --- | --- | --- |
|  | (In−K)​𝒉~​(0)=D.(I\_{n}-K)\tilde{\boldsymbol{h}}(0)=D. |  |

The following result studies the well-posedness of BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) in the usual case.

###### Theorem 4.1.

Assume Ψ<1\Psi<1. Then the well-posedness of BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) can be classified into the following situations.

1. 1.

   Unique Solution: If In−KI\_{n}-K is invertible, there exists a unique consistent initial vector 𝒉~​(0)=(In−K)−1​D\tilde{\boldsymbol{h}}(0)=(I\_{n}-K)^{-1}D. Consequently, BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (𝒉~,𝜼~)∈S𝔽2​(0,T;ℝn)×L𝔽2​(0,T;ℝn)(\tilde{\boldsymbol{h}},\tilde{\boldsymbol{\eta}})\in S\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n})\times L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}).
2. 2.

   Infinitely Many Solutions: If In−KI\_{n}-K is singular and D∈Im​(In−K)D\in\text{Im}(I\_{n}-K), there exist infinitely many solutions (𝒉~,𝜼~)∈S𝔽2​(0,T;ℝn)×L𝔽2​(0,T;ℝn)(\tilde{\boldsymbol{h}},\tilde{\boldsymbol{\eta}})\in S\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n})\times L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}). These solutions are characterized by initial vectors 𝒉~​(0)\tilde{\boldsymbol{h}}(0) in the affine space

   |  |  |  |
   | --- | --- | --- |
   |  | 𝒉~​(0)∈ker⁡(In−K)+(In−K)†​D,\tilde{\boldsymbol{h}}(0)\in\ker(I\_{n}-K)+(I\_{n}-K)^{\dagger}D, |  |

   where (In−K)†(I\_{n}-K)^{\dagger} represents the Moore-Penrose pseudoinverse of In−KI\_{n}-K.
3. 3.

   No Solution: If In−KI\_{n}-K is singular but D∉Im​(In−K)D\notin\text{Im}(I\_{n}-K), no solution exists to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")).

###### Remark 4.1.

For sufficiently small T>0T>0, the norm ‖K‖∞\|K\|\_{\infty} is also sufficiently small due to the integral structure of KK. This guarantees the invertibility of In−KI\_{n}-K and a unique solution to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). This is consistent with Lemma [A.1](https://arxiv.org/html/2511.05270v1#A1.E1 "In Lemma A.1. ‣ Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion") which assets that a unique solution to BSDE ([A.1](https://arxiv.org/html/2511.05270v1#A1.E1 "In Lemma A.1. ‣ Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion")) (a generalized nonlinear form of BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"))) exists for sufficiently small T>0T>0.

Next, we establish the connection between BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) and Nash equilibrium.

###### Theorem 4.2.

Assume Ψ<1\Psi<1. Then there exists a one-to-one correspondence between Nash equilibrium strategies and the solutions to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")).

###### Proof.

Step 1. Nash Equilibrium ⇒\Rightarrow Solution to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")): Assume that there exists a Nash equilibrium strategy 𝝅∗=(π1∗,π2∗,⋯,πn∗)⊤∈L𝔽2​(0,T;ℝn)\boldsymbol{\pi^{\*}}=(\pi^{\*}\_{1},\pi^{\*}\_{2},\cdots,\pi^{\*}\_{n})^{\top}\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}). By Definition [2.2](https://arxiv.org/html/2511.05270v1#S2.Thmdefn2 "Definition 2.2. ‣ 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion"), 𝝅∗\boldsymbol{\pi^{\*}} satisfies the coupled system composed of SDEs ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and linear optimal feedback controls ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")). Decoupling SDEs ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")) as what we do at the beginning of Section [4](https://arxiv.org/html/2511.05270v1#S4 "4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), we transform the coupled system to a simpler one composed of ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). Then, substituting the equilibrium strategy 𝝅∗\boldsymbol{\pi^{\*}} into ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we solve ([4.1](https://arxiv.org/html/2511.05270v1#S4.E1 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) to obtain h~j\tilde{h}\_{j}, η~j\tilde{\eta}\_{j} and h~j​(0)\tilde{h}\_{j}(0) for j=1,2,⋯,nj=1,2,\cdots,n. Consequently, the vector-valued linear BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) with a solution (𝒉~,𝜼~)(\tilde{\boldsymbol{h}},\tilde{\boldsymbol{\eta}}) follows from BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), where 𝒉~=(h~1,h~2,⋯,h~n)⊤\tilde{\boldsymbol{h}}=(\tilde{h}\_{1},\tilde{h}\_{2},\cdots,\tilde{h}\_{n})^{\top} and 𝜼~=(η~1,η~2,⋯,η~n)⊤\tilde{\boldsymbol{\eta}}=(\tilde{\eta}\_{1},\tilde{\eta}\_{2},\cdots,\tilde{\eta}\_{n})^{\top}.

Step 2. Solution to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) ⇒\Rightarrow Nash Equilibrium: Assume that BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a solution (𝒉~,𝜼~)(\tilde{\boldsymbol{h}},\tilde{\boldsymbol{\eta}}). The strategies πi∗\pi^{\*}\_{i}, i=1,2,⋯,ni=1,2,\cdots,n can be explicitly constructed by ([4.5](https://arxiv.org/html/2511.05270v1#S4.E5 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). The construction of 𝝅∗=(π1∗,π2∗,⋯,πn∗)⊤\boldsymbol{\pi^{\*}}=(\pi^{\*}\_{1},\pi^{\*}\_{2},\cdots,\pi^{\*}\_{n})^{\top} guarantees that it belongs to L𝔽2​(0,T;ℝn)L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n}) and satisfies the coupled system composed of SDEs ([2.3](https://arxiv.org/html/2511.05270v1#S2.E3 "In 2 Problem Formulation ‣ Competitive optimal portfolio selection under mean-variance criterion")), BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and linear optimal feedback controls ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), and thus 𝝅∗\boldsymbol{\pi^{\*}} is a Nash equilibrium.

Step 3. Bijectivity: With a known Nash equilibrium, we can construct a solution to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) by Step 1, and with this solution to BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we can retrieve the Nash equilibrium by Step 2. Therefore, the correspondence is invertible.

We next introduce two new assumptions on the market parameters for further discussions.

###### Assumption 4.1.

The Sharpe ratios of all risky assets are identical, but not identical to 0, i.e.

|  |  |  |
| --- | --- | --- |
|  | ρi​(t)=ρ​(t)≢0,for all ​i=1,2,⋯,n, and ​t∈[0,T].\rho\_{i}(t)=\rho(t)\not\equiv 0,\quad\text{for all }i=1,2,\cdots,n,\text{ and }\ t\in[0,T]. |  |

###### Assumption 4.2.

None of the Sharpe ratios ρi\rho\_{i}, i=1,2,⋯,ni=1,2,\cdots,n, is identical to 0, and the interest rate rr are all deterministic processes.

###### Remark 4.2.

Under Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), (ρ​σ​π)^i−ρi​(σ​π)^i=0\widehat{(\rho\sigma\pi)}\_{i}-\rho\_{i}\widehat{(\sigma\pi)}\_{i}=0 for i=1,2,⋯,ni=1,2,\cdots,n, and BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (h~i,η~i)≡(0,0)(\tilde{h}\_{i},\tilde{\eta}\_{i})\equiv(0,0).

###### Remark 4.3.

Under Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), BSDE ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solutions

|  |  |  |
| --- | --- | --- |
|  | (pi​(t),Λi​(t))=(exp⁡(∫tT(2​r​(s)−|ρi​(s)|2)​d⁡s),0),\left(p\_{i}\left(t\right),\Lambda\_{i}\left(t\right)\right)=\left(\exp\left(\int\_{t}^{T}\left(2r(s)-|\rho\_{i}(s)|^{2}\right)\operatorname{d}\!s\right),0\right), |  |

and BSDE ([3.11](https://arxiv.org/html/2511.05270v1#S3.E11 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (hˇi​(t),ηˇi​(t))=(−exp⁡{∫tT(−r​(s))​d⁡s},0)\left(\check{h}\_{i}\left(t\right),\check{\eta}\_{i}\left(t\right)\right)=(-\exp\{\int\_{t}^{T}(-r(s))\operatorname{d}\!s\},0).

###### Remark 4.4.

Under Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), since rr is deterministic, ξ≡0\xi\equiv 0 and ψ>0\psi>0. Thus ([3.8](https://arxiv.org/html/2511.05270v1#S3.E8 "In Theorem 3.5. ‣ 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) also holds due to ρi≠0\rho\_{i}\neq 0, i=1,2,⋯,ni=1,2,\cdots,n.

###### Theorem 4.3.

Assume Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and Ψ<1\Psi<1. Then there exists a unique Nash equilibrium.

###### Proof.

Under Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admit only trivial solutions (0,0)(0,0). BSDEs ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), ([3.2](https://arxiv.org/html/2511.05270v1#S3.E2 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and ([3.11](https://arxiv.org/html/2511.05270v1#S3.E11 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) are independent of the agent index ii. Hence we always denote their solutions by pp, Λ\Lambda, hh, η\eta, hˇ\check{h}, and ηˇ\check{\eta} without index ii under Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"). The optimal strategies ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) reduces to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | πi∗=θiσ​π∗^σi−1σi[\displaystyle\pi^{\*}\_{i}=\theta\_{i}\frac{\widehat{\sigma\pi^{\*}}}{\sigma\_{i}}-\frac{1}{\sigma\_{i}}\bigg[ | (−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)​ηˇ\displaystyle\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{\eta} |  | (4.7) |
|  |  | +(Λp+ρ)(Zi∗+(−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)hˇ)].\displaystyle+\left(\frac{\Lambda}{p}+\rho\right)\left(Z^{\*}\_{i}+\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{h}\right)\bigg]. |  |

And in this case ϕi\phi\_{i} has a form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕi=(−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)​ηˇ+(Λp+ρ)​(Zi∗+(−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)​hˇ),\phi\_{i}=\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{\eta}+\left(\frac{\Lambda}{p}+\rho\right)\left(Z^{\*}\_{i}+\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{h}\right), |  | (4.8) |

or equivalently

|  |  |  |
| --- | --- | --- |
|  | ϕi=(−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)​ηˇ+(Λp+ρ)​Yi∗p.\phi\_{i}=\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{\eta}+\left(\frac{\Lambda}{p}+\rho\right)\frac{Y^{\*}\_{i}}{p}. |  |

Substituting ϕi\phi\_{i} into ([4.7](https://arxiv.org/html/2511.05270v1#S4.E7 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we obtain a fully decoupled linear system. Noticing Ψ<1\Psi<1, we can derive a unique Nash equilibrium from ([4.5](https://arxiv.org/html/2511.05270v1#S4.E5 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) based on the fully decoupled linear system.

###### Theorem 4.4.

Assume Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and Ψ<1\Psi<1. Then there exists a unique Nash equilibrium.

###### Proof.

Under Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), both BSDE ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and BSDE ([3.11](https://arxiv.org/html/2511.05270v1#S3.E11 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) degenerate into ordinary differential equations with deterministic coefficients. Consequently, Λi=0\Lambda\_{i}=0, ηˇi=0\check{\eta}\_{i}=0. In the mean time, the coefficient matrices AA and BB are deterministic, and C=K=0C=K=0. By Theorems [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmthm1 "Theorem 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmthm2 "Theorem 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), BSDE ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution which corresponds to the unique Nash equilibrium.

### 4.2 The marginal case

For Ψ=1\Psi=1, by definition of Ψ\Psi, we have θi=1\theta\_{i}=1 for all i=1,2,⋯,ni=1,2,\cdots,n. Then the equilibrium strategy ([4.3](https://arxiv.org/html/2511.05270v1#S4.E3 "In 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​πi∗=n​θin−1+θi​σ​π∗¯−ϕi1+θin−1=σ​π∗¯−n−1n​ϕi.\sigma\_{i}\pi^{\*}\_{i}=\frac{n\theta\_{i}}{n-1+\theta\_{i}}\overline{\sigma\pi^{\*}}-\frac{\phi\_{i}}{1+\frac{\theta\_{i}}{n-1}}=\overline{\sigma\pi^{\*}}-\frac{n-1}{n}\phi\_{i}. |  | (4.9) |

Set Φ≜∑i=1nϕi\Phi\triangleq\sum\_{i=1}^{n}\phi\_{i}, then we discuss the existence of Nash equilibrium based on Φ\Phi.

1. 1.

   No Equilibrium: If Φ≠0\Phi\neq 0, it contradicts with ([4.9](https://arxiv.org/html/2511.05270v1#S4.E9 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) since a sum of ([4.9](https://arxiv.org/html/2511.05270v1#S4.E9 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) implies Φ=0\Phi=0.
2. 2.

   Uncertain Situation: If Φ=0\Phi=0, the existence of Nash equilibrium is uncertain. But if it exists, the equilibrium strategy should be parameterized by a process χ∈L𝔽2​(0,T;ℝ1)\chi\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}) chosen as a degree of freedom, i.e.

   |  |  |  |
   | --- | --- | --- |
   |  | σi​πi∗=χ−n−1n​ϕi,i=1,2,⋯,n.\sigma\_{i}\pi^{\*}\_{i}=\chi-\frac{n-1}{n}\phi\_{i},\ \ \ \ i=1,2,\cdots,n. |  |

Set 𝒉~′=(h~1′,h~2′,⋯,h~n′)⊤\tilde{\boldsymbol{h}}^{\prime}=(\tilde{h}^{\prime}\_{1},\tilde{h}^{\prime}\_{2},\cdots,\tilde{h}^{\prime}\_{n})^{\top} and 𝜼~′=(η~1′,η~2′,⋯,η~n′)⊤\tilde{\boldsymbol{\eta}}^{\prime}=(\tilde{\eta}^{\prime}\_{1},\tilde{\eta}^{\prime}\_{2},\cdots,\tilde{\eta}^{\prime}\_{n})^{\top}. BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝒉~′=−{A′​𝒉~′+B′​𝜼~′+C′​𝒉~′​(0)+F′}​d⁡t+𝜼~′​d⁡W,t∈[0,T],𝒉~′​(T)=0,\left\{\begin{array}[]{l}\mathrm{d}\tilde{\boldsymbol{h}}^{\prime}=-\left\{A^{\prime}\tilde{\boldsymbol{h}}^{\prime}+B^{\prime}\tilde{\boldsymbol{\eta}}^{\prime}+C^{\prime}\tilde{\boldsymbol{h}}^{\prime}(0)+F^{\prime}\right\}\operatorname{d}\!t+\tilde{\boldsymbol{\eta}}^{\prime}\operatorname{d}\!W,\quad t\in[0,T],\\ \tilde{\boldsymbol{h}}^{\prime}(T)=0,\end{array}\right. |  | (4.10) |

where A′A^{\prime}, B′B^{\prime}, and C′C^{\prime} are coefficient matrices,
and F′F^{\prime} is a coefficient vector. Precisely, for i,j=1,2,⋯,ni,j=1,2,\cdots,n,

|  |  |  |
| --- | --- | --- |
|  | Ai​j′≜{0,i≠j,−r,i=j,Bi​j′≜{ρj−ρin,i≠j,−ρi,i=j,A^{\prime}\_{ij}\triangleq\left\{\begin{aligned} 0,\ \ \ \ \ &i\neq j,\\ -r,\ \ \ &i=j,\end{aligned}\right.\ \ \ \ \ B^{\prime}\_{ij}\triangleq\left\{\begin{aligned} \frac{\rho\_{j}-\rho\_{i}}{n},\ \ \ &i\neq j,\\ -\rho\_{i},\ \ \ \ \ \ \ \ &i=j,\end{aligned}\right. |  |

|  |  |  |
| --- | --- | --- |
|  | Ci​j′≜{ρj−ρin​cj,i≠j,0,i=j,Fi′≜∑i≠jρj−ρinfj−∑i≠jρj−ρin−1χ.C^{\prime}\_{ij}\triangleq\left\{\begin{aligned} \frac{\rho\_{j}-\rho\_{i}}{n}c\_{j},\ \ \ &i\neq j,\\ 0,\ \ \ \ \ \ \ \ \ \ \ \ \ &i=j,\end{aligned}\right.\ \ \ \ \ F^{\prime}\_{i}\triangleq\sum\_{i\neq j}\frac{\rho\_{j}-\rho\_{i}}{n}f\_{j}-\sum\_{i\neq j}\frac{\rho\_{j}-\rho\_{i}}{n-1}\chi. |  |

Obviously A′∈L𝔽∞​(0,T;ℝn×n)A^{\prime}\in L\_{\mathbb{F}}^{\infty}(0,T;\mathbb{R}^{n\times n}), B′∈L𝔽∞​(0,T;ℝn×n)B^{\prime}\in L\_{\mathbb{F}}^{\infty}\left(0,T;\mathbb{R}^{n\times n}\right), C′∈L𝔽2​(0,T;ℝn×n)C^{\prime}\in L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n\times n}\right) and F′∈L𝔽2​(0,T;ℝn)F^{\prime}\in L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n}\right).
Set K′≜𝔼​[∫0TΓ′​(s)​C′​(s)​d⁡s]K^{\prime}\triangleq\mathbb{E}\big[\int\_{0}^{T}\Gamma^{\prime}(s)C^{\prime}(s)\operatorname{d}\!s\big] and D′≜𝔼​[∫0TΓ′​(s)​F′​(s)​d⁡s]D^{\prime}\triangleq\mathbb{E}\big[\int\_{0}^{T}\Gamma^{\prime}(s)F^{\prime}(s)\operatorname{d}\!s\big],
where Γ′∈L𝔽2​(0,T;ℝn×n)\Gamma^{\prime}\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{n\times n}) solves SDE

|  |  |  |
| --- | --- | --- |
|  | {d​Γ′=Γ′​[A′​d⁡t+B′​d⁡W],t∈[0,T],Γ′​(0)=In.\left\{\begin{aligned} \mathrm{d}\Gamma^{\prime}&=\Gamma^{\prime}\left[A^{\prime}\operatorname{d}\!t+B^{\prime}\operatorname{d}\!W\right],\quad t\in[0,T],\\ \Gamma^{\prime}(0)&=I\_{n}.\end{aligned}\right. |  |

Then the consistent condition for 𝒉~′​(0)\tilde{\boldsymbol{h}}^{\prime}(0) to guarantee the well-posedness of BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) in the marginal case becomes

|  |  |  |
| --- | --- | --- |
|  | (In−K′)​𝒉~′​(0)=D′.(I\_{n}-K^{\prime})\tilde{\boldsymbol{h}}^{\prime}(0)=D^{\prime}. |  |

In general, with a degree of freedom process χ\chi, it is difficult to guarantee both Φ=0\Phi=0 and the well-posedness of BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) in the mean time. Even if the well-posedness of BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is achieved by the invertibility of In−K′I\_{n}-K^{\prime} with the help of a sufficiently small time horizon T>0T>0, to guarantee Φ=0\Phi=0 with a suitable choice of χ∈L𝔽2​(0,T;ℝ)\chi\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}) is still a challenging problem. If we further know that BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution, the difficulty is still there due to the required delicate balance between the free-choice parameter χ\chi and Φ=0\Phi=0 in the marginal case. However, under the homogeneous risk preferences condition (Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) or the deterministic coefficients condition (Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), the coupled system is simplified much, and explicit criteria could be derived to guarantee both Φ=0\Phi=0 and the well-posedness of BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")).

We first discuss the delicate balance between χ\chi and Φ=0\Phi=0 under Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion").

###### Theorem 4.5.

Assume Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and Ψ=1\Psi=1. Then the existence of Nash equilibrium can be classified into the following situations.

1. 1.

   Infinitely Many Equilibria: If the equality

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼​∫0T(r​(s)+12​|ρ​(s)|2)​d⁡s=∫0T(r​(s)+12​|ρ​(s)|2)​d⁡s+∫0Tρ​(s)​d⁡Ws,\mathbb{E}\int\_{0}^{T}\left(r(s)+\frac{1}{2}|\rho(s)|^{2}\right)\operatorname{d}\!s=\int\_{0}^{T}\left(r(s)+\frac{1}{2}|\rho(s)|^{2}\right)\operatorname{d}\!s+\int\_{0}^{T}\rho(s)\operatorname{d}\!W\_{s}, |  | (4.11) |

   holds, then there exist infinitely many Nash equilibria whose components are parameterized by χ∈L𝔽2​(0,T;ℝ1)\chi\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}^{1}) as below

   |  |  |  |
   | --- | --- | --- |
   |  | πi∗=χσi−n−1n​σi​[(−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)​ηˇ+(Λp+ρ)​Yi∗p].\pi^{\*}\_{i}=\frac{\chi}{\sigma\_{i}}-\frac{n-1}{n\sigma\_{i}}\left[\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{\eta}+\left(\frac{\Lambda}{p}+\rho\right)\frac{Y^{\*}\_{i}}{p}\right]. |  |
2. 2.

   No Equilibrium: If ([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) does not hold, no Nash equilibrium exists.

###### Proof.

Under Assumption [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), BSDEs ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) admit only trivial solutions (0,0)(0,0). Since θi=1\theta\_{i}=1 for all i=1,2,⋯,ni=1,2,\cdots,n, ∑k=1nZk∗=0\sum\limits\_{k=1}^{n}Z^{\*}\_{k}=0 and ∑k=1nzk=0\sum\limits\_{k=1}^{n}z\_{k}=0. It follows from ([4.8](https://arxiv.org/html/2511.05270v1#S4.E8 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) that

|  |  |  |
| --- | --- | --- |
|  | Φ=γ^p​(0)​hˇ​(0)2​(ηˇ+(Λp+ρ)​hˇ).\Phi=\frac{\hat{\gamma}}{p(0)\check{h}(0)^{2}}\left(\check{\eta}+\left(\frac{\Lambda}{p}+\rho\right)\check{h}\right). |  |

Notice γ^p​(0)​hˇ​(0)2≠0\frac{\hat{\gamma}}{p(0)\check{h}(0)^{2}}\neq 0. Define

|  |  |  |
| --- | --- | --- |
|  | Ξ≜ηˇ+(Λp+ρ)​hˇ.\Xi\triangleq\check{\eta}+\left(\frac{\Lambda}{p}+\rho\right)\check{h}. |  |

We claim that there is no Nash equilibrium if Ξ≢0\Xi\not\equiv 0, and there are infinitely many Nash equilibria if Ξ≡0\Xi\equiv 0.

Then we present an equivalent condition to Ξ≡0\Xi\equiv 0. We claim that
Ξ≡0\Xi\equiv 0 if and only if ([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) holds.

Ξ≡0⟹\Xi\equiv 0\implies ([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")): Set L​(t)=p​(t)​hˇ​(t)L(t)=p(t)\check{h}(t) for t∈[0,T]t\in[0,T], and by Itô’s formula, it follows that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​L\displaystyle\mathrm{d}L | =[hˇ​(−r​p+ρ2​p+2​ρ​Λ+Λ2p)+ηˇ​(ρ​p+Λ)]​d⁡t+(ηˇ​p+hˇ​Λ)​d⁡W,\displaystyle=\left[\check{h}\left(-rp+\rho^{2}p+2\rho\Lambda+\frac{\Lambda^{2}}{p}\right)+\check{\eta}\left(\rho p+\Lambda\right)\right]\operatorname{d}\!t+\left(\check{\eta}p+\check{h}\Lambda\right)\operatorname{d}\!W, |  | (4.12) |
|  |  | =(−r​L+Ξ​(ρ​p+Λ))​d⁡t+(−ρ​L+p​Ξ)​d⁡W.\displaystyle=\left(-rL+\Xi(\rho p+\Lambda)\right)\operatorname{d}\!t+\left(-\rho L+p\Xi\right)\operatorname{d}\!W. |  |

If Ξ≡0\Xi\equiv 0, we get from ([4.12](https://arxiv.org/html/2511.05270v1#S4.E12 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) an SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​L=−r​L​d⁡t−ρ​L​d⁡W,t∈[0,T],L​(T)=−1,L​(0)=p​(0)​hˇ​(0).\left\{\begin{array}[]{l}\mathrm{d}L=-rL\operatorname{d}\!t-\rho L\operatorname{d}\!W,\quad t\in[0,T],\\ L(T)=-1,\\ L(0)=p(0)\check{h}(0).\end{array}\right. |  | (4.13) |

The first two equations in ([4.13](https://arxiv.org/html/2511.05270v1#S4.E13 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) give a unique explicit 𝔽\mathbb{F}-adapted solution as below

|  |  |  |
| --- | --- | --- |
|  | L​(t)=−exp⁡(∫tTρ​(s)​d⁡Ws+∫tT(r​(s)+12​ρ​(s)2)​d⁡s),t∈[0,T].L(t)=-\exp\left(\int\_{t}^{T}\rho(s)\operatorname{d}\!W\_{s}+\int\_{t}^{T}\left(r(s)+\frac{1}{2}\rho(s)^{2}\right)\operatorname{d}\!s\right),\quad t\in[0,T]. |  |

Hence, if SDE ([4.13](https://arxiv.org/html/2511.05270v1#S4.E13 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is solvable, then

|  |  |  |
| --- | --- | --- |
|  | ∫0Tρ​(s)​d⁡Ws+∫0T(r​(s)+12​ρ​(s)2)​d⁡s=L​(0)=p​(0)​hˇ​(0),\int\_{0}^{T}\rho(s)\operatorname{d}\!W\_{s}+\int\_{0}^{T}\left(r(s)+\frac{1}{2}\rho(s)^{2}\right)\operatorname{d}\!s=L(0)=p(0)\check{h}(0), |  |

must be a constant, which implies that ([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is true.

([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) ⟹Ξ≡0\implies\Xi\equiv 0: If ([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) holds, ∫0T(r​(s)+12​ρ​(s)2)​d⁡s+∫0Tρ​(s)​d⁡W\int\_{0}^{T}\left(r(s)+\frac{1}{2}\rho(s)^{2}\right)\operatorname{d}\!s+\int\_{0}^{T}\rho(s)\operatorname{d}\!W is a constant, which together with ∫0tρ​(s)​d⁡Ws+∫0t(r​(s)+12​ρ​(s)2)​d⁡s\int\_{0}^{t}\rho(s)\operatorname{d}\!W\_{s}+\int\_{0}^{t}\left(r(s)+\frac{1}{2}\rho(s)^{2}\right)\operatorname{d}\!s is ℱt\mathcal{F}\_{t}-measurable, leads to ∫tTρ​(s)​d⁡Ws+∫tT(r​(s)+12​ρ​(s)2)​d⁡s\int\_{t}^{T}\rho(s)\operatorname{d}\!W\_{s}+\int\_{t}^{T}\left(r(s)+\frac{1}{2}\rho(s)^{2}\right)\operatorname{d}\!s is ℱt\mathcal{F}\_{t}-measurable for t∈[0,T]t\in[0,T]. According to ([3.4](https://arxiv.org/html/2511.05270v1#S3.E4 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and ([3.12](https://arxiv.org/html/2511.05270v1#S3.E12 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), we know

|  |  |  |
| --- | --- | --- |
|  | p​(t)​hˇ​(t)=−𝔼​[exp⁡{∫tT−ρ​d⁡W+∫tT(−r−ρ22)​d⁡s}|ℱt]𝔼​[exp⁡{∫tT−2​ρ​d⁡W+∫tT(−2​r−ρi2)​d⁡s}|ℱt],p(t)\check{h}(t)=-\frac{\mathbb{E}\bigg[\exp\Big\{\int\_{t}^{T}-\rho\operatorname{d}\!W+\int\_{t}^{T}(-r-\frac{\rho^{2}}{2})\operatorname{d}\!s\Big\}\;\bigg|\;\mathcal{F}\_{t}\bigg]}{\mathbb{E}\bigg[\exp\Big\{\int\_{t}^{T}-2\rho\operatorname{d}\!W+\int\_{t}^{T}(-2r-\rho\_{i}^{2})\operatorname{d}\!s\Big\}\;\bigg|\;\mathcal{F}\_{t}\bigg]}, |  |

and due to measurability we further have

|  |  |  |
| --- | --- | --- |
|  | p​(t)​hˇ​(t)=−exp⁡(∫tTρ​d⁡W+∫tT(r+12​ρ2)​d⁡s).p(t)\check{h}(t)=-\exp\left(\int\_{t}^{T}\rho\operatorname{d}\!W+\int\_{t}^{T}(r+\frac{1}{2}\rho^{2})\operatorname{d}\!s\right). |  |

This shows that L​(t)=p​(t)​hˇ​(t)L(t)=p(t)\check{h}(t) is a solution of SDE ([4.13](https://arxiv.org/html/2511.05270v1#S4.E13 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). Bearing in mind that p​(t)​hˇ​(t)p(t)\check{h}(t) is also a solution of SDE ([4.12](https://arxiv.org/html/2511.05270v1#S4.E12 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we immediately have Ξ≡0\Xi\equiv 0.

Let us see the delicate balance between χ\chi and Φ=0\Phi=0 under Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion").

###### Theorem 4.6.

Assume Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and Ψ=1\Psi=1. Then the existence of Nash equilibrium can be classified into the following situations.

1. 1.

   Infinitely Many Equilibria: If the equality

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫0T𝔼​[q​(ρ¯​η^′+G)]​d⁡s=∫0Tq​(ρ¯​η^′+G)​d⁡s+∫0Tq​η^′​d⁡W,\int\_{0}^{T}\mathbb{E}\big[q(\bar{\rho}\hat{\eta}^{\prime}+G)\big]\operatorname{d}\!s=\int\_{0}^{T}q(\bar{\rho}\hat{\eta}^{\prime}+G)\operatorname{d}\!s+\int\_{0}^{T}q\hat{\eta}^{\prime}\operatorname{d}\!W, |  | (4.14) |

   holds, where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | q​(t)≜e−∫0tr​(s)​d⁡s,η^′≜∑i=1nρi​Yi∗pi,G≜∑i=1n∑j≠iρj−ρin​ρj​Yj∗pj,q(t)\triangleq e^{-\int\_{0}^{t}r(s)\operatorname{d}\!s},\quad\hat{\eta}^{\prime}\triangleq\sum\_{i=1}^{n}\rho\_{i}\frac{Y^{\*}\_{i}}{p\_{i}},\quad G\triangleq\sum\_{i=1}^{n}\sum\_{j\neq i}\frac{\rho\_{j}-\rho\_{i}}{n}\rho\_{j}\frac{Y^{\*}\_{j}}{p\_{j}}, |  | (4.15) |

   there exist infinitely many Nash equilibria whose components are parameterized by χ∈L𝔽2​(0,T;ℝ)\chi\in L\_{\mathbb{F}}^{2}(0,T;\mathbb{R}) as below

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | πi∗=χσi−n−1n​σi​(η~i′+ρi​Yi∗pi),\pi^{\*}\_{i}=\frac{\chi}{\sigma\_{i}}-\frac{n-1}{n\sigma\_{i}}\left(\tilde{\eta}\_{i}^{\prime}+\rho\_{i}\frac{Y^{\*}\_{i}}{p\_{i}}\right), |  | (4.16) |

   where η~i′\tilde{\eta}^{\prime}\_{i} is the solution to BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")).
2. 2.

   No Equilibrium: If ([4.14](https://arxiv.org/html/2511.05270v1#S4.E14 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) does not hold, no Nash Equilibrium exists.

###### Proof.

Under Assumption [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), ci=0c\_{i}=0 for i=1,2,⋯,ni=1,2,\cdots,n and thus C′=0C^{\prime}=0. Then BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (𝒉~′,𝜼~′)(\tilde{\boldsymbol{h}}^{\prime},\tilde{\boldsymbol{\eta}}^{\prime}) parameterized by χ\chi. In this case ϕi\phi\_{i} has a form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕi=η~i′+ρi​Yi∗pi.\phi\_{i}=\tilde{\eta}\_{i}^{\prime}+\rho\_{i}\frac{Y^{\*}\_{i}}{p\_{i}}. |  | (4.17) |

Denote by 1→=(1,1,…,1)⊤∈ℝn\vec{1}=(1,1,\ldots,1)^{\top}\in\mathbb{R}^{n} the unit vector. Noticing ∑i=1nAi​j′=−r\sum\limits\_{i=1}^{n}A^{\prime}\_{ij}=-r and ∑i=1nBi​j′=−ρ¯\sum\limits\_{i=1}^{n}B^{\prime}\_{ij}=-\bar{\rho}, and using BSDE ([4.10](https://arxiv.org/html/2511.05270v1#S4.E10 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we get a scalar-valued BSDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​h^=−{−r​h^−ρ¯​η^+G}​d⁡t+η^​d⁡W,t∈[0,T],h^​(T)=0,\left\{\begin{array}[]{l}\mathrm{d}\hat{h}=-\left\{-r\hat{h}-\bar{\rho}\hat{\eta}+G\right\}\operatorname{d}\!t+\hat{\eta}\operatorname{d}\!W,\quad t\in[0,T],\\ \hat{h}(T)=0,\end{array}\right. |  | (4.18) |

where h^≜1→⋅𝒉~′\hat{h}\triangleq\vec{1}\cdot\tilde{\boldsymbol{h}}^{\prime}, η^≜1→⋅𝜼~′\hat{\eta}\triangleq\vec{1}\cdot\tilde{\boldsymbol{\eta}}^{\prime} and G≜1→⋅F′G\triangleq\vec{1}\cdot F^{\prime}.
Note that GG is independent of χ\chi and so is BSDE ([4.18](https://arxiv.org/html/2511.05270v1#S4.E18 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). By ([4.15](https://arxiv.org/html/2511.05270v1#S4.E15 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) and ([4.17](https://arxiv.org/html/2511.05270v1#S4.E17 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) we know η^=η^′−Φ\hat{\eta}=\hat{\eta}^{\prime}-\Phi, so BSDE ([4.18](https://arxiv.org/html/2511.05270v1#S4.E18 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) involves Φ\Phi.
Clearly, if Φ=0\Phi=0, there are infinitely many equilibria given by ([4.16](https://arxiv.org/html/2511.05270v1#S4.E16 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), and otherwise there is no Nash Equilibrium. So we need to prove that ([4.14](https://arxiv.org/html/2511.05270v1#S4.E14 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is a criteria to determine Φ=0\Phi=0 or not.

If Φ=0\Phi=0, BSDE ([4.18](https://arxiv.org/html/2511.05270v1#S4.E18 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) can be rewritten as the following SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​h^=−{−r​h^+ρ¯​η^′+G}​d⁡t−η^′​d⁡W,t∈[0,T],h^​(T)=0.\left\{\begin{aligned} &\mathrm{d}\hat{h}=-\left\{-r\hat{h}+\bar{\rho}\hat{\eta}^{\prime}+G\right\}\operatorname{d}\!t-\hat{\eta}^{\prime}\operatorname{d}\!W,\quad t\in[0,T],\\ &\hat{h}(T)=0.\end{aligned}\right. |  | (4.19) |

By SDE ([4.19](https://arxiv.org/html/2511.05270v1#S4.E19 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) and Itô’s lemma, we obtain

|  |  |  |
| --- | --- | --- |
|  | h^​(t)=1q​(t)​[h^​(0)−∫0tq​(ρ¯​η^′+G)​d⁡s−∫0tq​η^′​d⁡W].\hat{h}(t)=\frac{1}{q(t)}\bigg[\hat{h}(0)-\int\_{0}^{t}q(\bar{\rho}\hat{\eta}^{\prime}+G)\operatorname{d}\!s-\int\_{0}^{t}q\hat{\eta}^{\prime}\operatorname{d}\!W\bigg]. |  |

Letting t=Tt=T and taking expectation, we have

|  |  |  |
| --- | --- | --- |
|  | h^​(0)=∫0T𝔼​[q​(ρ¯​η^′+G)]​d⁡s.\hat{h}(0)=\int\_{0}^{T}\mathbb{E}\big[q(\bar{\rho}\hat{\eta}^{\prime}+G)\big]\operatorname{d}\!s. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | h^​(t)=1q​(t)​[∫0T𝔼​[q​(ρ¯​η^′+G)]​d⁡s−∫0tq​(ρ¯​η^′+G)​d⁡s−∫0tq​η^′​d⁡W].\hat{h}(t)=\frac{1}{q(t)}\bigg[\int\_{0}^{T}\mathbb{E}\big[q(\bar{\rho}\hat{\eta}^{\prime}+G)\big]\operatorname{d}\!s-\int\_{0}^{t}q(\bar{\rho}\hat{\eta}^{\prime}+G)\operatorname{d}\!s-\int\_{0}^{t}q\hat{\eta}^{\prime}\operatorname{d}\!W\bigg]. |  |

If the equality ([4.14](https://arxiv.org/html/2511.05270v1#S4.E14 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) holds, the constraint h^​(T)=0\hat{h}(T)=0 is satisfied, and the constrained SDE ([4.19](https://arxiv.org/html/2511.05270v1#S4.E19 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is well-posed.

On the other hand, if the constrained SDE ([4.19](https://arxiv.org/html/2511.05270v1#S4.E19 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) is well-posed with a solution h^\hat{h}, then (h^,−η^′)(\hat{h},-\hat{\eta}^{\prime}) is also a solution to BSDE ([4.18](https://arxiv.org/html/2511.05270v1#S4.E18 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). By the uniqueness of solution to BSDE ([4.18](https://arxiv.org/html/2511.05270v1#S4.E18 "In 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")), we know −η^′=η^-\hat{\eta}^{\prime}=\hat{\eta} which implies Φ=η^+η^′=0\Phi=\hat{\eta}+\hat{\eta}^{\prime}=0.

## 5 Example

In the case that both Assumptions [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") are satisfied, explicit expressions for the feedback strategies can be given (if existing). We will show this in the following theorem, which can also be regarded as a special example for our theoretical results.

###### Theorem 5.1.

Assume Assumptions [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") hold. Then there exists a unique Nash equilibrium if Ψ<1\Psi<1 and no Nash equilibrium exists if Ψ=1\Psi=1.

###### Proof.

Under Assumptions [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), rr and ρ\rho are deterministic functions, and

|  |  |  |
| --- | --- | --- |
|  | p​(t)=exp⁡((−2​r+ρ2)​(t−T)),hˇ​(t)=−exp⁡{r​(t−T)},Λ=h~=η~=ηˇ=0,p(t)=\exp((-2r+\rho^{2})(t-T)),\quad\check{h}(t)=-\exp\{r(t-T)\},\quad\Lambda=\tilde{h}=\tilde{\eta}=\check{\eta}=0, |  |

where (p,Λ)(p,\Lambda), (h~,η~)(\tilde{h},\tilde{\eta}) and (hˇ,ηˇ)(\check{h},\check{\eta}) are the solutions to BSDE ([3.1](https://arxiv.org/html/2511.05270v1#S3.E1 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), ([3.10](https://arxiv.org/html/2511.05270v1#S3.E10 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) and ([3.11](https://arxiv.org/html/2511.05270v1#S3.E11 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")), respectively.

If Ψ<1\Psi<1, by Remark [4.4](https://arxiv.org/html/2511.05270v1#S4.Thmremark4 "Remark 4.4. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and Theorems [4.3](https://arxiv.org/html/2511.05270v1#S4.Thmthm3 "Theorem 4.3. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.4](https://arxiv.org/html/2511.05270v1#S4.Thmthm4 "Theorem 4.4. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), there exists a unique Nash equilibrium. In this case the optimal feedback strategy ([3.14](https://arxiv.org/html/2511.05270v1#S3.E14 "In 3 Solutions for the MV Problems (2.4)-(2.7) ‣ Competitive optimal portfolio selection under mean-variance criterion")) reduces to

|  |  |  |
| --- | --- | --- |
|  | πi∗=θi​(σ​π∗)^iσi−ρσi​(Zi∗−er​t​zi−exp⁡(r​(t−T)+ρ2​T)γi).\pi\_{i}^{\*}=\theta\_{i}\frac{\widehat{(\sigma\pi^{\*})}\_{i}}{\sigma\_{i}}-\frac{\rho}{\sigma\_{i}}\left(Z^{\*}\_{i}-e^{rt}z\_{i}-\frac{\exp\left(r(t-T)+\rho^{2}T\right)}{\gamma\_{i}}\right). |  |

And ϕi\phi\_{i} has a form

|  |  |  |
| --- | --- | --- |
|  | ϕi=ρ​(Zi∗−er​t​zi−exp⁡(r​(t−T)+ρ2​T)γi).\phi\_{i}=\rho\left(Z^{\*}\_{i}-e^{rt}z\_{i}-\frac{\exp\left(r(t-T)+\rho^{2}T\right)}{\gamma\_{i}}\right). |  |

Hence the unique Nash equilibrium is

|  |  |  |
| --- | --- | --- |
|  | σi​πi∗=−11−Ψ​n​θin−1+θi​∑i=1nϕin+n​θin−1−ϕi1+θin−1.\sigma\_{i}\pi^{\*}\_{i}=-\frac{1}{1-\Psi}\frac{n\theta\_{i}}{n-1+\theta\_{i}}\sum\_{i=1}^{n}\frac{\phi\_{i}}{n+\frac{n\theta\_{i}}{n-1}}-\frac{\phi\_{i}}{1+\frac{\theta\_{i}}{n-1}}. |  |

If Ψ=1\Psi=1, no equilibrium exists. It follows from
the term in Theorem [4.5](https://arxiv.org/html/2511.05270v1#S4.Thmthm5 "Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") that

|  |  |  |
| --- | --- | --- |
|  | Ξ=ηˇ+(Λp+ρ)​hˇ=ρ​hˇ≢0,\Xi=\check{\eta}+\left(\frac{\Lambda}{p}+\rho\right)\check{h}=\rho\check{h}\not\equiv 0, |  |

or equivalently, ([4.11](https://arxiv.org/html/2511.05270v1#S4.E11 "In item 1 ‣ Theorem 4.5. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) does not hold since r+12​ρ2r+\frac{1}{2}\rho^{2} is deterministic and ∫0Tρ​d⁡W≢0\int\_{0}^{T}\rho\operatorname{d}\!W\not\equiv 0. Alternatively, we obtain the same conclusion by checking ([4.14](https://arxiv.org/html/2511.05270v1#S4.E14 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) in Theorem [4.6](https://arxiv.org/html/2511.05270v1#S4.Thmthm6 "Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"). If ([4.14](https://arxiv.org/html/2511.05270v1#S4.E14 "In item 1 ‣ Theorem 4.6. ‣ 4.2 The marginal case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")) holds,

|  |  |  |
| --- | --- | --- |
|  | ∫0T𝔼​[q​ρ¯​η^′]​d⁡s=∫0Tq​ρ¯​η^′​d⁡s+∫0Tq​η^′​d⁡W.\int\_{0}^{T}\mathbb{E}\left[q\bar{\rho}\hat{\eta}^{\prime}\right]\operatorname{d}\!s=\int\_{0}^{T}q\bar{\rho}\hat{\eta}^{\prime}\,\operatorname{d}\!s+\int\_{0}^{T}q\hat{\eta}^{\prime}\,\operatorname{d}\!W. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | ρ¯​η^′=∑i=1nρ2​Yi∗p=∑i=1nρ2​(Zi∗+(−zihˇ​(0)+1γi​p​(0)​hˇ​(0)2)​hˇ)=∑i=1nγ^​ρ2p​(0)​hˇ​(0)2​hˇ,\bar{\rho}\hat{\eta}^{\prime}=\sum\_{i=1}^{n}\rho^{2}\frac{Y^{\*}\_{i}}{p}=\sum\_{i=1}^{n}\rho^{2}\left(Z^{\*}\_{i}+\left(-\frac{z\_{i}}{\check{h}(0)}+\frac{1}{\gamma\_{i}p(0)\check{h}(0)^{2}}\right)\check{h}\right)=\sum\_{i=1}^{n}\frac{\hat{\gamma}\rho^{2}}{p(0)\check{h}(0)^{2}}\check{h}, |  |

we see
q​ρ¯​η^′q\bar{\rho}\hat{\eta}^{\prime} is deterministic and η^′≢0\hat{\eta}^{\prime}\not\equiv 0. But ∫0Tq​η^′​d⁡W\int\_{0}^{T}q\hat{\eta}^{\prime}\,\operatorname{d}\!W obeys the law of normal distribution, which results in a contradiction.

## 6 Conclusion

In this paper, we investigate time-inconsistent Nash equilibrium strategies for a multi-agent game under MV criterion. We first solve a linearly constrained stochastic LQ control problem to derive optimal strategies for each agent. Then we use a decoupling technique to establish a connection between the Nash equilibrium and a novel type of linear multi-dimensional BSDEs ([4.6](https://arxiv.org/html/2511.05270v1#S4.E6 "In 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion")). The well-posedness of such BSDEs is studied in both the usual case and the marginal case. Based on Assumptions [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion"), we have more refined analyses of Nash equilibria, as summarized in the following table.

Table 1: Existence of Nash Equilibria

| Assumptions | None | [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") | [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") | [4.1](https://arxiv.org/html/2511.05270v1#S4.Thmassmp1 "Assumption 4.1. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") and [4.2](https://arxiv.org/html/2511.05270v1#S4.Thmassmp2 "Assumption 4.2. ‣ 4.1 The usual case ‣ 4 Solving the Nash Equilibrium ‣ Competitive optimal portfolio selection under mean-variance criterion") |
| --- | --- | --- | --- | --- |
| Ψ<1\Psi<1 | Discussion | Unique | Unique | Unique |
| Ψ=1\Psi=1 | Open | None or infinity | None or infinity | None |

## Appendix A Well-Posedness of a New Type of Nonlinear BSDEs

###### Lemma A.1.

Consider the following BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y​(t)=ξ+∫tTf​(s,Y​(s),Z​(s),C​(s)​Y​(0))​d⁡s−∫tTZ​(s)​d⁡W​(s),t∈[0,T],Y(t)=\xi+\int\_{t}^{T}f\big(s,Y(s),Z(s),C(s)Y(0)\big)\operatorname{d}\!s-\int\_{t}^{T}Z(s)\operatorname{d}\!W(s),\quad t\in[0,T], |  | (A.1) |

where

1. (a1)

   {W​(t)}t∈[0,T]\left\{W(t)\right\}\_{t\in[0,T]} is a standard mm-dimensional Brownian motion with its natural filtration denoted by 𝔽={ℱt}t∈[0,T]\mathbb{F}=\left\{\mathcal{F}\_{t}\right\}\_{t\in[0,T]};
2. (a2)

   ξ∈ℱT\xi\in\mathcal{F}\_{T} and 𝔼​|ξ|2<∞\mathbb{E}|\xi|^{2}<\infty;
3. (a3)

   f:Ω×[0,T]×ℝn×ℝn×m×ℝn→ℝnf:\Omega\times[0,T]\times\mathbb{R}^{n}\times\mathbb{R}^{n\times m}\times\mathbb{R}^{n}\rightarrow\mathbb{R}^{n} is 𝒫⊗ℬ​(ℝn)⊗ℬ​(ℝn×m)⊗ℬ​(ℝn)\mathscr{P}\otimes\mathcal{B}(\mathbb{R}^{n})\otimes\mathcal{B}(\mathbb{R}^{n\times m})\otimes\mathcal{B}(\mathbb{R}^{n})-measurable and C:Ω×[0,T]→ℝn×nC:\Omega\times[0,T]\rightarrow\mathbb{R}^{n\times n} is 𝒫\mathscr{P}-measurable, where 𝒫\mathscr{P} is the predictable sub-σ\sigma algebra of ℱ⊗ℬ​([0,T])\mathcal{F}\otimes\mathcal{B}([0,T]);
4. (a4)

   for any t∈[0,T],y1,y2∈ℝn,z1,z2∈ℝn×mt\in[0,T],y\_{1},y\_{2}\in\mathbb{R}^{n},z\_{1},z\_{2}\in\mathbb{R}^{n\times m}, there exists a Lipschitz constant L⩾0L\geqslant 0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | |f​(t,y1,z1,ζ1)−f​(t,y2,z2,ζ2)|⩽L​(|y1−y2|+|z1−z2|+|ζ1−ζ2|);|f\left(t,y\_{1},z\_{1},\zeta\_{1}\right)-f\left(t,y\_{2},z\_{2},\zeta\_{2}\right)|\leqslant L\left(|y\_{1}-y\_{2}|+|z\_{1}-z\_{2}|+|\zeta\_{1}-\zeta\_{2}|\right); |  |
5. (a5)

   𝔼​∫0T(|f​(t,0,0,0)|2+|C​(t)|2)​d⁡t<∞\mathbb{E}\int\_{0}^{T}(|f(t,0,0,0)|^{2}+|C(t)|^{2})\operatorname{d}\!t<\infty.

Fix the terminal value ξ\xi, the driver ff and process CC, then
BSDE ([A.1](https://arxiv.org/html/2511.05270v1#A1.E1 "In Lemma A.1. ‣ Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion")) admits a unique solution (Y,Z)∈S𝔽2​(0,T;ℝn)×L𝔽2​(0,T;ℝn×m)(Y,Z)\in S\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n}\right)\times L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n\times m}\right), provided that the horizon time T>0T>0 is sufficiently small.

###### Proof.

For a given v∈ℝnv\in\mathbb{R}^{n}, consider BSDE

|  |  |  |
| --- | --- | --- |
|  | Yv​(t)=ξ+∫tTf​(s,Yv​(s),Zv​(s),C​(s)​v)​d⁡s−∫tTZv​(s)​d⁡W​(s),t∈[0,T].Y^{v}(t)=\xi+\int\_{t}^{T}f\big(s,Y^{v}(s),Z^{v}(s),C(s)v\big)\operatorname{d}\!s-\int\_{t}^{T}Z^{v}(s)\operatorname{d}\!W(s),\quad t\in[0,T]. |  |

It is well known that, under (a1)–(a5), the above BSDE admits a unique solution (Yv,Zv)∈S𝔽2​(0,T;ℝn)×L𝔽2​(0,T;ℝn×m)(Y^{v},Z^{v})\in S\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n}\right)\times L\_{\mathbb{F}}^{2}\left(0,T;\mathbb{R}^{n\times m}\right).

Define the mapping Φ:ℝn→ℝn\Phi:\mathbb{R}^{n}\to\mathbb{R}^{n} by Φ​(v)=Yv​(0)\Phi(v)=Y^{v}(0). Below, we analyze the contraction property of Φ\Phi.

Consider the following two BSDEs with parameters v^\hat{v} and v~∈ℝn\tilde{v}\in\mathbb{R}^{n}:

|  |  |  |
| --- | --- | --- |
|  | {Y^v^​(t)=ξ+∫tT(f​(s,Y^v^​(s),Z^v^​(s),C​(s)​v^))​d⁡s−∫tTZ^v^​(s)​d⁡W​(s),Y~v~​(t)=ξ+∫tT(f​(s,Y~v~​(s),Z~v~​(s)),C​(s)​v~)​d⁡s−∫tTZ~v~​(s)​d⁡W​(s).\begin{cases}\displaystyle\hat{Y}^{\hat{v}}(t)=\xi+\int\_{t}^{T}\big(f(s,\hat{Y}^{\hat{v}}(s),\hat{Z}^{\hat{v}}(s),C(s)\hat{v})\big)\operatorname{d}\!s-\int\_{t}^{T}\hat{Z}^{\hat{v}}(s)\operatorname{d}\!W(s),\\ \displaystyle\tilde{Y}^{\tilde{v}}(t)=\xi+\int\_{t}^{T}\big(f(s,\tilde{Y}^{\tilde{v}}(s),\tilde{Z}^{\tilde{v}}(s)),C(s)\tilde{v}\big)\operatorname{d}\!s-\int\_{t}^{T}\tilde{Z}^{\tilde{v}}(s)\operatorname{d}\!W(s).\end{cases} |  |

For β=16​(L2+1)\beta=16(L^{2}+1), the standard estimate for BSDEs yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |Y^v^​(t)−Y~v~​(t)|2+12​𝔼ℱt​[∫tTeβ​(s−t)​(|Y^v^​(s)−Y~v~​(s)|2+|Z^v^​(s)−Z~v~​(s)|2)​d⁡s]\displaystyle|\hat{Y}^{\hat{v}}(t)-\tilde{Y}^{\tilde{v}}(t)|^{2}+\frac{1}{2}\mathbb{E}^{\mathcal{F}\_{t}}\left[\int\_{t}^{T}e^{\beta(s-t)}\left(|\hat{Y}^{\hat{v}}(s)-\tilde{Y}^{\tilde{v}}(s)|^{2}+|\hat{Z}^{\hat{v}}(s)-\tilde{Z}^{\tilde{v}}(s)|^{2}\right)\operatorname{d}\!s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩽\displaystyle\leqslant | L24​(L2+1)​𝔼ℱt​∫tTeβ​(s−t)​|C​(s)|2​|v^−v~|2​d⁡s.\displaystyle\frac{L^{2}}{4(L^{2}+1)}\mathbb{E}^{\mathcal{F}\_{t}}\int\_{t}^{T}e^{\beta(s-t)}|C(s)|^{2}|\hat{v}-\tilde{v}|^{2}\operatorname{d}\!s. |  |

In particular, it implies

|  |  |  |
| --- | --- | --- |
|  | |Y^v^​(0)−Y~v~​(0)|2⩽14​∫0Teβ​s​𝔼​[|C​(s)|2]​d⁡s⋅|v^−v~|2.|\hat{Y}^{\hat{v}}(0)-\tilde{Y}^{\tilde{v}}(0)|^{2}\leqslant\frac{1}{4}\int\_{0}^{T}e^{\beta s}\mathbb{E}\big[|C(s)|^{2}\big]\operatorname{d}\!s\cdot|\hat{v}-\tilde{v}|^{2}. |  |

Taking T>0T>0 sufficiently small such that ∫0Teβ​s​𝔼​[|C​(s)|2]​d⁡s<1,\int\_{0}^{T}e^{\beta s}\mathbb{E}\big[|C(s)|^{2}\big]\operatorname{d}\!s<1, the above estimate leads to i.e.,

|  |  |  |
| --- | --- | --- |
|  | |Φ​(v1)−Φ​(v2)|⩽12​|v1−v2|,|\Phi(v\_{1})-\Phi(v\_{2})|\leqslant\frac{1}{2}|v\_{1}-v\_{2}|, |  |

so that Φ\Phi is a contraction mapping.
By the fixed-point theory, there exists a unique v∈ℝnv\in\mathbb{R}^{n} such that Φ​(v)=v\Phi(v)=v, i.e., Yv​(0)=vY^{v}(0)=v, from which the existence and uniqueness of solution to BSDE ([A.1](https://arxiv.org/html/2511.05270v1#A1.E1 "In Lemma A.1. ‣ Appendix A Well-Posedness of a New Type of Nonlinear BSDEs ‣ Competitive optimal portfolio selection under mean-variance criterion")) follows.

## References

* [1]

  T. Björk, M. Khapko, and A. Murgoci, On time-inconsistent
  stochastic control in continuous time, Finance and Stochastics, 21 (2017),
  pp. 331–360.
* [2]

  L. Bo, S. Wang, and C. Zhou, A mean field game approach to optimal
  investment and risk control for competitive insurers, Insurance: Mathematics
  and Economics, 116 (2024), pp. 202–217.
* [3]

  C. Deng, X. Su, and C. Zhou, Relative wealth concerns with partial
  information and heterogeneous priors, SIAM Journal on Financial Mathematics,
  15 (2024), pp. 360–398.
* [4]

  G.-E. Espinosa and N. Touzi, Optimal investment under relative
  performance concerns, Mathematical Finance, 25 (2015), pp. 221–257.
* [5]

  G. Fu, Mean field portfolio games with consumption, Mathematics and
  Financial Economics, 17 (2023), pp. 79–99.
* [6]

  G. Fu and C. Zhou, Mean field portfolio games, Finance and
  Stochastics, 27 (2023), pp. 189–231.
* [7]

  G. Guan and X. Hu, Time-consistent investment and reinsurance
  strategies for mean–variance insurers in n-agent and mean-field games,
  North American Actuarial Journal, 26 (2022), pp. 537–569.
* [8]

  Y. He, L. He, D. Chen, and Z. Liu, Mean field and n-insurers games
  for robust optimal reinsurance-investment in correlated markets., Journal of
  Industrial & Management Optimization, 19 (2023).
* [9]

  Y. Hu, X. Shi, and Z. Q. Xu, Non-homogeneous stochastic LQ control
  with regime switching and random coefficients, Math. Control Relat. Fields,
  14 (2024), pp. 671–694.
* [10]

  D. Lacker and A. Soret, Many-player games of optimal consumption and
  investment under relative performance criteria, Mathematics and Financial
  Economics, 14 (2020), pp. 263–281.
* [11]

  D. Lacker and T. Zariphopoulou, Mean field and n-agent games for
  optimal investment under relative performance criteria, Mathematical
  Finance, 29 (2019), pp. 1003–1038.
* [12]

  X. Li, X. Y. Zhou, and A. E. Lim, Dynamic mean-variance portfolio
  selection with no-shorting constraints, SIAM Journal on Control and
  Optimization, 40 (2002), pp. 1540–1555.
* [13]

  Z. Liang and K. Zhang, Time-inconsistent mean field and-agent games
  under relative performance criteria, SIAM Journal on Financial Mathematics,
  15 (2024), pp. 1047–1082.
* [14]

  A. E. Lim and X. Y. Zhou, Mean-variance portfolio selection with
  random parameters in a complete market, Mathematics of Operations Research,
  27 (2002), pp. 101–120.
* [15]

  H. Markowitz, Modern portfolio theory, Journal of Finance, 7
  (1952), pp. 77–91.
* [16]

  H. M. Markowitz, Portfolio selection: efficient diversification of
  investments, Yale university press, 2008.
* [17]

  G. Wang, Z. Q. Xu, and P. Zhang, Competitive optimal portfolio
  selection in a non-markovian financial market: A backward stochastic
  differential equation study, arXiv preprint arXiv:2408.02286, (2024).
* [18]

  J. Xiong and X. Y. Zhou, Mean-variance portfolio selection under
  partial information, SIAM Journal on Control and Optimization, 46 (2007),
  pp. 156–175.
* [19]

  P. Yang, Z. Chen, and Y. Xu, Time-consistent equilibrium
  reinsurance–investment strategy for n competitive insurers under a new
  interaction mechanism and a general investment framework, Journal of
  Computational and Applied Mathematics, 374 (2020), p. 112769.
* [20]

  J. Zhang, Backward stochastic differential equations, Springer,
  2017.
* [21]

  P. Zhang and P. Huang, Optimal portfolio with relative performance
  and partial information: A mean-field game approach, Asian Journal of
  Control, 26 (2024), pp. 703–716.
* [22]

  X. Y. Zhou and D. Li, Continuous-time mean-variance portfolio
  selection: A stochastic lq framework, Applied Mathematics and Optimization,
  42 (2000), pp. 19–33.
* [23]

  X. Y. Zhou and G. Yin, Markowitz’s mean-variance portfolio selection
  with regime switching: A continuous-time model, SIAM Journal on Control and
  Optimization, 42 (2003), pp. 1466–1482.
* [24]

  J. Zhu, G. Guan, and S. Li, Time-consistent non-zero-sum stochastic
  differential reinsurance and investment game under default and volatility
  risks, Journal of Computational and Applied Mathematics, 374 (2020),
  p. 112737.