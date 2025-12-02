---
authors:
- Zeyun Hu
- Yang Liu
doc_id: arxiv:2512.00299v1
family_id: arxiv:2512.00299
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region
  Algorithm and Neural Network'
url_abs: http://arxiv.org/abs/2512.00299v1
url_html: https://arxiv.org/html/2512.00299v1
venue: arXiv q-fin
version: 1
year: 2025
---


Zeyun Hu
School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. Email: zeyunhu@link.cuhk.edu.cn
  
Yang Liu
Corresponding author. School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. Email: yangliu16@cuhk.edu.cn

###### Abstract

We investigate the static portfolio selection problem of S-shaped and non-concave utility maximization under first-order and second-order stochastic dominance (SD) constraints. In many S-shaped utility optimization problems, one should require a liquidation boundary to guarantee the existence of a finite concave envelope function. A first-order SD (FSD) constraint can replace this requirement and provide an alternative for risk management. We explicitly solve the optimal solution under a general S-shaped utility function with a first-order stochastic dominance constraint. However, the second-order SD (SSD) constrained problem under non-concave utilities is difficult to solve analytically due to the invalidity of Sion’s maxmin theorem.
For this sake, we propose a numerical algorithm to obtain a plausible and sub-optimal solution for general non-concave utilities. The key idea is to detect the poor performance region with respect to the SSD constraints, characterize its structure and modify the distribution on that region to obtain (sub-)optimality. A key financial insight is that the decision maker should follow the SD constraint on the poor performance scenario while conducting the unconstrained optimal strategy otherwise. We provide numerical experiments to show that our algorithm effectively finds a sub-optimal solution in many cases. Finally, we develop an algorithm-guided piecewise-neural-network framework to learn the solution of the SSD problem, which demonstrates accelerated convergence compared to standard neural network approaches.

Keywords: Non-concave utility, portfolio selection, risk constraints, first-order stochastic dominance (FSD), second-order stochastic dominance (SSD), numerical method, neural network

## 1 Introduction

S-shaped utility functions, formalized in cumulative prospect theory (Tversky and Kahneman ([1992](https://arxiv.org/html/2512.00299v1#bib.bib16))) and surveyed in behavioral finance (Barberis and Thaler ([2003](https://arxiv.org/html/2512.00299v1#bib.bib1))), capture two salient features of investor behavior: risk seeking in losses and risk aversion in gains. In portfolio selection problems, this non-concavity can induce aggressive tail-risk taking (Carpenter ([2000](https://arxiv.org/html/2512.00299v1#bib.bib2)); He and Kou ([2018](https://arxiv.org/html/2512.00299v1#bib.bib5)); Liang and Liu ([2020](https://arxiv.org/html/2512.00299v1#bib.bib10))). In particular, when the pricing kernel has a heavy right tail, unconstrained S-shaped optimization typically generates a heavy left tail in terminal wealth, leading to large probabilities of extreme losses, which are the risks that classical VaR/ES-type constraints do not reliably mitigate.

We adopt stochastic dominance (SD) constraints as an implementable approach to control such downside risk under non-concave utilities. First-order SD (FSD) relative to a benchmark wealth X0X\_{0} enforces a quantile-by-quantile floor, offering a distribution-level safety guarantee that often aligns better with practice than hard liquidation boundaries. Second-order SD (SSD) controls cumulative quantiles, providing a flexible, model-free form of downside protection from the pathological risk-seeking induced by the convex (loss) region of S-shaped preferences.

Analytically, SD-constrained utility maximization is well understood for strictly concave utilities via quantile reformulations, duality, and saddle-point arguments (Föllmer and Schied ([2016](https://arxiv.org/html/2512.00299v1#bib.bib3)); Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18))). However, extending these tools to non-concave utilities under SSD is challenging. Sion’s max-min theorem no longer applies in the key saddle-point step, concavification is not guaranteed to be valid because optimizers can fall in regions where the utility and its concave envelope differ (Liang and Liu ([2024](https://arxiv.org/html/2512.00299v1#bib.bib11))), and closed-form solutions are scarce beyond special, technically constrained settings (Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18))). This paper contributes on three aspects.

First, we derive an explicit optimal solution for portfolio selection with a general S-shaped utility under an FSD constraint relative to a benchmark. Crucially, the FSD constraint obviates the need for a liquidation boundary: the optimal wealth is counter-comonotone with the pricing kernel and exhibits a two-regime structure, coinciding with the classical solution in favorable states and binding to the benchmark quantile in adverse states. This clarifies how FSD serves as a “soft” and interpretable left-tail boundary.

Second, we propose the Poor-Performance-Region Algorithm (PPRA), a numerical method that constructs a feasible, high-quality suboptimal solution, and in many cases a numerically optimal one. The key idea is to identify the “poor performance region”, namely quantile levels where the unconstrained classical optimizer violates SSD relative to the benchmark. The algorithm partitions this region and applies a state-dependent correction to enforce SSD, while reverting to the unconstrained policy elsewhere. Financially, the resulting rule is intuitive: track the benchmark in poor states to satisfy SSD; otherwise follow the classical optimizer.

Third, we develop an algorithm-guided piecewise-neural-network framework that embeds the PPRA-derived partition and analytic priors into the architecture. This design drastically narrows the functional search space, accelerates convergence, satisfies budget and SSD constraints more quickly, and attains higher objective values than a standard monolithic network, especially in non-concave settings where regular training struggles with infeasibility and local minima.

Methodologically, our approach combines duality and concavification insights (Karatzas et al. ([1987](https://arxiv.org/html/2512.00299v1#bib.bib7)); Carpenter ([2000](https://arxiv.org/html/2512.00299v1#bib.bib2)); Liang and Liu ([2020](https://arxiv.org/html/2512.00299v1#bib.bib10))) with the quantile formulation of utility maximization (He and Zhou ([2011](https://arxiv.org/html/2512.00299v1#bib.bib6)); Föllmer and Schied ([2016](https://arxiv.org/html/2512.00299v1#bib.bib3))) and SD theory (Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)); Wang, Wei and Xia ([2024](https://arxiv.org/html/2512.00299v1#bib.bib17))). For FSD, we provide a closed-form solution without a liquidation boundary and interpret FSD as a distributional safety floor. For SSD, we translate feasibility into integral inequalities in the quantile domain and design a correction that “repairs” exactly where the unconstrained policy underperforms the benchmark.

We validate our methods in a complete-market (Black-Scholes) setting across diverse utilities (CRRA, exponential, log, S-shaped, and piecewise) and benchmarks (log-normal, normal, exponential, uniform). For FSD, the explicit solution confirms that dominance constraints can substitute for liquidation boundaries. For SSD, PPRA consistently produces feasible, interpretable solutions that often match known optima in concave cases. The piecewise neural network guided by PPRA converges substantially faster and to better solutions than a monolithic network, particularly under non-concavity.

Financial implications are immediate.
First, FSD guarantees that all terminal-wealth quantiles exceed those of a benchmark, giving a realistic and implementable floor.
Second, the optimal/near-optimal policy is to adhere to the benchmark in bad states and follow the classical policy otherwise, yielding transparent risk management. Third, SD constraints significantly reduce the probability of extreme losses induced by S-shaped preferences, beyond what standard VaR/ES controls typically achieve.

Scope and limitations. Our analysis focuses on complete markets and static terminal-wealth problems, leveraging their equivalence to dynamic continuous-time settings via the pricing kernel. While PPRA is broadly applicable and robust in experiments, it provides suboptimality guarantees rather than universal optimality in the non-concave SSD case; establishing general sharp optimality conditions remains a promising direction for future research.

The structure of this paper is as follows. Section [2](https://arxiv.org/html/2512.00299v1#S2 "2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") presents the model. Section [3](https://arxiv.org/html/2512.00299v1#S3 "3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") derives the explicit FSD solution for general S-shaped utilities and explains how FSD replaces liquidation boundaries. Section [4](https://arxiv.org/html/2512.00299v1#S4 "4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") explains the analytical hurdles of SSD under non-concavity and introduces PPRA. Section [5](https://arxiv.org/html/2512.00299v1#S5 "5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") provides numerical studies across utilities and benchmarks. Section [6](https://arxiv.org/html/2512.00299v1#S6 "6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") develops the algorithm-guided, piecewise neural-network framework and contrasts it with standard networks. Section [7](https://arxiv.org/html/2512.00299v1#S7 "7 Conclusion ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") concludes.

## 2 Model Settings

Fix an atomless probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). Let L0L^{0} be the set of all random variables on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). Let L1⊂L0L^{1}\subset L^{0} be the set of all integrable random variables.
Denote the pricing kernel by a continuously-distributed random variable ρ:Ω→(0,∞)\rho:\Omega\to(0,\infty) and ρ∈L1\rho\in L^{1}.
For an initial capital x¯∈ℝ\overline{x}\in\mathbb{R}, the static version of the classic Merton ([1969](https://arxiv.org/html/2512.00299v1#bib.bib13))’s problem is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | maxX∈L0⁡𝔼​[U​(X)]​ s.t. ​𝔼​[ρ​X]⩽x¯,\displaystyle\max\_{X\in L^{0}}\mathbb{E}\left[U(X)\right]\text{ s.t. }\mathbb{E}[\rho X]\leqslant\overline{x}, |  | (1) |

where U:ℝ→ℝU:\mathbb{R}\to\mathbb{R} is a utility function to be specified in the following different sections. The constraint is called the budget constraint. For a strictly concave utility, the solution of Problem ([1](https://arxiv.org/html/2512.00299v1#S2.E1 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xcla=I​(λcla​ρ),X\_{\text{cla}}=I(\lambda\_{\text{cla}}\rho), |  | (2) |

where the conjugate function I:(0,∞)→ℝI:(0,\infty)\to\mathbb{R} is given by I​(y)≜arg​supx∈ℝ[U​(x)−x​y],y>0I(y)\triangleq\arg\sup\_{x\in\mathbb{R}}\left[U(x)-xy\right],~y>0
(We will revisit the definition if UU is non-concave)
and λcla>0\lambda\_{\text{cla}}>0 is a Lagrange multiplier solved from
𝔼​[ρ​I​(λcla​ρ)]=x¯.\mathbb{E}[\rho I(\lambda\_{\text{cla}}\rho)]=\overline{x}.
The problem ([1](https://arxiv.org/html/2512.00299v1#S2.E1 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) can be seen as the terminal wealth optimization of the classic continuous-time Merton’s problem in a complete market; see Appendix A of Liang and Liu ([2024](https://arxiv.org/html/2512.00299v1#bib.bib11)) for details.
In the classic Merton’s problem, the utility function is chosen as a smooth and strictly concave function, including power/log (CRRA, constant relative risk aversion) or exponential (CARA, constant absolute risk aversion) functions.

Now we introduce the concept of stochastic dominance (SD). For a random variable X∈L0X\in L^{0}, the (upper) quantile function QX:[0,1]→ℝ∪{±∞}Q\_{X}:[0,1]\to\mathbb{R}\cup\{\pm\infty\} is defined by

|  |  |  |
| --- | --- | --- |
|  | QX​(s)=inf{x∈ℝ|ℙ​(X⩽x)>s},s∈[0,1].Q\_{X}(s)=\inf\{x\in\mathbb{R}\big|\mathbb{P}(X\leqslant x)>s\},~~s\in[0,1]. |  |

Denote by 𝒬\mathcal{Q} the set of all quantile functions:

|  |  |  |
| --- | --- | --- |
|  | 𝒬≜{Q:[0,1]→ℝ∪{±∞}|Q​ is increasing and right-continuous}.\mathcal{Q}\triangleq\left\{Q:[0,1]\to\mathbb{R}\cup\{\pm\infty\}\big|Q\text{ is increasing and right-continuous}\right\}. |  |

###### Definition 1 (Stochastic dominance).

1. (1)

   Fix X,Y∈L0X,Y\in L^{0}. XX is greater than YY in first-order stochastic dominance (FSD) if QX​(s)⩾QY​(s)Q\_{X}(s)\geqslant Q\_{Y}(s) for all s∈(0,1)s\in(0,1), which is denoted by X⪰(1)YX\succeq\_{(1)}Y.
2. (2)

   Fix X,Y∈L1X,Y\in L^{1}. XX is greater than YY in second-order stochastic dominance (SSD) if ∫0tQX​(s)​ds⩾∫0tQY​(s)​ds\int\_{0}^{t}Q\_{X}(s)\mathrm{d}s\geqslant\int\_{0}^{t}Q\_{Y}(s)\mathrm{d}s for all t∈(0,1)t\in(0,1), which is denoted by X⪰(2)YX\succeq\_{(2)}Y.

We specify a given benchmark wealth X0∈L0X\_{0}\in L^{0}.
We proceed to study the problem with the first-order stochastic dominance (FSD) or second-order stochastic dominance (SSD) constraints:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (FSD Problem) | maxX∈L0⁡𝔼​[U​(X)]​ s.t. ​𝔼​[ρ​X]⩽x¯​ and ​X⪰(1)X0,\displaystyle\max\_{X\in L^{0}}\mathbb{E}[U(X)]\text{ s.t. }\mathbb{E}[\rho X]\leqslant\overline{x}\text{ and }X\succeq\_{(1)}X\_{0}, |  | (3) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (SSD Problem) | maxX∈L1⁡𝔼​[U​(X)]​ s.t. ​𝔼​[ρ​X]⩽x¯​ and ​X⪰(2)X0.\displaystyle\max\_{X\in L^{1}}\mathbb{E}[U(X)]\text{ s.t. }\mathbb{E}[\rho X]\leqslant\overline{x}\text{ and }X\succeq\_{(2)}X\_{0}. |  | (4) |

We denote the quantile function of X0X\_{0} by Q0∈𝒬Q\_{0}\in\mathcal{Q}. Further, we define a minimal budget value:

|  |  |  |
| --- | --- | --- |
|  | xQ0≜𝔼​[ρ​X0]=∫01Q0​(s)​Qρ​(1−s)​ds.x\_{Q\_{0}}\triangleq\mathbb{E}[\rho X\_{0}]=\int\_{0}^{1}Q\_{0}(s)Q\_{\rho}(1-s)\mathrm{d}s. |  |

Throughout, we assume x¯⩾xQ0\overline{x}\geqslant x\_{Q\_{0}}. As a result, both problems ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"))-([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) have at least one feasible solution X0X\_{0}.

Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)) propose and solve the FSD and SSD problems ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"))-([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) with smooth and concave utilities; see Wang, Wei and Xia ([2024](https://arxiv.org/html/2512.00299v1#bib.bib17)) for a mean-stochastic-dominance problem. In the following, we investigate the corresponding general non-concave utility optimization, particularly, S-shaped utility optimization.

## 3 FSD Problem and Analytical Solution

In this section, we apply the general S-shaped utility in Definition [2](https://arxiv.org/html/2512.00299v1#Thmdefinition2 "Definition 2 (General S-shaped utility). ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (see Liang and Liu ([2020](https://arxiv.org/html/2512.00299v1#bib.bib10))) and proceed to study Problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")). Now we define a general S-shaped utility function UU.

###### Definition 2 (General S-shaped utility).

A general S-shaped utility function U:ℝ→ℝU:\mathbb{R}\rightarrow\mathbb{R} with the reference point B∈ℝB\in\mathbb{R} has the expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | U(x)={U1​(x),x⩾B,U2​(x),x<B,U(x)=\left\{\begin{aligned} &U\_{1}(x),&&x\geqslant B,\\ &U\_{2}(x),&&x<B,\end{aligned}\right. |  | (5) |

and satisfies the following properties:

1. (i)

   UU is increasing on ℝ\mathbb{R}, U=U1U=U\_{1} is strictly concave on (B,∞)(B,\infty), and U=U2U=U\_{2} is convex on (−∞,B)(-\infty,B).
2. (ii)

   U1​(B)=U2​(B)U\_{1}(B)=U\_{2}(B) and U1′​(B+)=U2′​(B−)=∞U\_{1}^{\prime}(B+)=U\_{2}^{\prime}(B-)=\infty.
3. (iii)

   Inada condition: U1′​(∞)=0U\_{1}^{\prime}(\infty)=0.

The conjugate function I:(0,∞)→ℝI:(0,\infty)\rightarrow\mathbb{R} is given by I​(y)=arg​supx⩾B[U​(x)−x​y]=(U1′)−1​(y)I(y)=\arg\sup\_{x\geqslant B}\left[U(x)-xy\right]=(U\_{1}^{\prime})^{-1}(y). Note that in Definition [2](https://arxiv.org/html/2512.00299v1#Thmdefinition2 "Definition 2 (General S-shaped utility). ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), there is no requirement for a finite left endpoint of the domain of the utility function (known as the liquidation boundary). We solve the FSD problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) with a general S-shaped utility and hence illustrate that using the FSD constraint can replace the liquidation boundary for risk management.

###### Theorem 1.

With a general S-shaped utility in Definition [2](https://arxiv.org/html/2512.00299v1#Thmdefinition2 "Definition 2 (General S-shaped utility). ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), the optimal solution of Problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | XFSD∗={(U1′)−1​(λ​ρ),if ​{ρ<1λ​U1′​(Q0​(1−Fρ​(ρ)))​ and ​Q0​(1−Fρ​(ρ))⩾B}​ or ​{ρ⩽1λ​U1′​(C)​ and ​Q0​(1−Fρ​(ρ))<B};Q0​(1−Fρ​(ρ)),if ​{ρ⩾1λ​U1′​(Q0​(1−Fρ​(ρ)))​ and ​Q0​(1−Fρ​(ρ))⩾B}​ or ​{ρ>1λ​U1′​(C)​ and ​Q0​(1−Fρ​(ρ))<B}.\scriptsize X\_{\text{FSD}}^{\*}=\left\{\begin{aligned} &(U\_{1}^{\prime})^{-1}(\lambda\rho),\text{if }\left\{\rho<\frac{1}{\lambda}U\_{1}^{\prime}\left(Q\_{0}(1-F\_{\rho}(\rho))\right)\text{ and }Q\_{0}\left(1-F\_{\rho}(\rho)\right)\geqslant B\right\}\text{ or }\left\{\rho\leqslant\frac{1}{\lambda}U\_{1}^{\prime}(C)\text{ and }Q\_{0}\left(1-F\_{\rho}(\rho)\right)<B\right\};\\ &Q\_{0}(1-F\_{\rho}(\rho)),\text{if }\left\{\rho\geqslant\frac{1}{\lambda}U\_{1}^{\prime}\left(Q\_{0}(1-F\_{\rho}(\rho))\right)\text{ and }Q\_{0}\left(1-F\_{\rho}(\rho)\right)\geqslant B\right\}\text{ or }\left\{\rho>\frac{1}{\lambda}U\_{1}^{\prime}(C)\text{ and }Q\_{0}\left(1-F\_{\rho}(\rho)\right)<B\right\}.\end{aligned}\right. |  | (6) |

where (i) the Lagrange multiplier λ>0\lambda>0 is solved from the binding budget constraint 𝔼​[ρ​XFSD∗]=x¯\mathbb{E}[\rho X\_{\text{FSD}}^{\*}]=\overline{x}, and (ii) for any Q0​(1−Fρ​(ρ))<BQ\_{0}\left(1-F\_{\rho}(\rho)\right)<B, the (state-dependent) tangent point C∈(B,∞)C\in(B,\infty) is solved from

|  |  |  |  |
| --- | --- | --- | --- |
|  | U1​(C)−U2​(Q0​(1−Fρ​(ρ)))C−Q0​(1−Fρ​(ρ))=U1′​(C).\frac{U\_{1}(C)-U\_{2}(Q\_{0}(1-F\_{\rho}(\rho)))}{C-Q\_{0}(1-F\_{\rho}(\rho))}=U\_{1}^{\prime}(C). |  | (7) |

###### Proof of Theorem [1](https://arxiv.org/html/2512.00299v1#Thmtheorem1 "Theorem 1. ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

As the objective in Problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is an increasing function of XX, the optimal wealth XFSD∗X\_{\text{FSD}}^{\*} of Problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is counter-comonotonic to the pricing kernel ρ\rho (see, e.g., He and Zhou ([2011](https://arxiv.org/html/2512.00299v1#bib.bib6))). Denote by ξ\xi the uniform transformation of ρ\rho such that ξ\xi has the uniform distribution on [0,1][0,1] and Qρ​(ξ)=ρQ\_{\rho}(\xi)=\rho. Hence, the optimal wealth XFSD∗X\_{\text{FSD}}^{\*} under the first-order stochastic dominance constraint should satisfy

|  |  |  |
| --- | --- | --- |
|  | XFSD∗⩾Q0​(1−ξ),Q∈𝒬.X\_{\text{FSD}}^{\*}\geqslant Q\_{0}(1-\xi),~~Q\in\mathcal{Q}. |  |

Hence, Problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is translated to the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxX⩾Q0​(1−ξ),𝔼​[ρ​X]=x⁡𝔼​[U​(X)].\max\_{X\geqslant Q\_{0}(1-\xi),\mathbb{E}\left[\rho X\right]=x}\mathbb{E}\left[U(X)\right]. |  | (8) |

Further, Problem ([8](https://arxiv.org/html/2512.00299v1#S3.E8 "In 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is converted to a state-dependent pointwise optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxX⩾Q0​(1−ξ)⁡{U​(X)−λ​ρ​X},\max\_{X\geqslant Q\_{0}(1-\xi)}\left\{U(X)-\lambda\rho X\right\}, |  | (9) |

where λ>0\lambda>0 is a to-be-determined Lagrange multiplier such that 𝔼​[ρ​X]=x¯\mathbb{E}[\rho X]=\overline{x}. To solve Problem ([9](https://arxiv.org/html/2512.00299v1#S3.E9 "In 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), we have the following two cases:

1. (i)

   for any ω∈Ω\omega\in\Omega satisfying Q0​(1−ξ​(ω))<BQ\_{0}(1-\xi(\omega))<B, we solve the tangent point C​(ω)C(\omega) from ([7](https://arxiv.org/html/2512.00299v1#S3.E7 "In Theorem 1. ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) and have
   X\_FSD^\* = {
   (U1’)-1(λρ), if (U1’)-1(λρ) ¿ C and Q0(1-ξ) ¡ B;Q0(1-ξ), if (U1’)-1(λρ) ⩽C and Q0(1-ξ) ¡ B.
2. (ii)

   for any ω∈Ω\omega\in\Omega satisfying Q0​(1−ξ​(ω))⩾BQ\_{0}(1-\xi(\omega))\geqslant B, we have
   X\_FSD^\* = {
   (U1’)-1(λρ), if (U1’)-1(λρ) ¿ Q0(1-ξ) and Q0(1-ξ) ⩾B;Q0(1-ξ), if (U1’)-1(λρ) ⩽Q0(1-ξ) and Q0(1-ξ) ⩾B.

Further, as ξ=Fρ​(ρ)\xi=F\_{\rho}(\rho), we derive the optimal solution XFSD∗X\_{\text{FSD}}^{\*} given by ([6](https://arxiv.org/html/2512.00299v1#S3.E6 "In Theorem 1. ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).
∎

In the literature, a liquidation boundary is needed for the optimization of the S-shaped utility, otherwise the problem has no solution (mathematically, it is because one cannot establish a concave envelope for the S-shaped utility without a lower bound in the domain). In the problem of FSD, we do not require the liquidation boundary for the S-shaped utility. The solution is twofold. In some good scenarios, it behaves like the classic solution. In some bad scenarios, it behaves like the benchmark quantile. From the solution, we can see that the FSD constraint acts as a good substitute of the liquidation boundary.

## 4 SSD Problem

### 4.1 SSD Problem under Non-concavity: Analytical Difficulty

Let us restate the results of Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)) on strictly concave utilities.

###### Theorem 2 (Theorem 5.10 of Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18))).

Let x¯>x0\overline{x}>x\_{0}. For a strictly concave utility UU with appropriate regularity conditions, the optimal solution to Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is XSSD∗=QSSD∗​(1−Fρ​(ρ))X\_{\text{SSD}}^{\*}=Q\_{\text{SSD}}^{\*}(1-F\_{\rho}(\rho)) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | QSSD∗​(s)=I​(λ​(Qρ​(1−s)−ySSD∗​(1−s))),s∈(0,1),Q\_{\text{SSD}}^{\*}(s)=I\left(\lambda\left(Q\_{\rho}(1-s)-y\_{\text{SSD}}^{\*}(1-s)\right)\right),~s\in(0,1), |  | (10) |

where ySSD∗:[0,1]→[0,∞)y\_{\text{SSD}}^{\*}:[0,1]\to[0,\infty) is a function
given by the system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ySSD∗​ is right-continuous and ​0⩽d​ySSD∗​(t)d​Qρ​(t)⩽1, ​Qρ​(t)−ySSD∗​(t)>0​ for all ​t∈(0,1);zSSD∗​(s)≜−∫s1(I​(λ​(Qρ​(t)−ySSD∗​(t)))−Q0​(1−t))​dt,s∈[0,1];d​ySSD∗​(t)d​Qρ​(t){∈[0,1],zSSD∗​(t)=0;=0,zSSD∗​(t)<0,dQρ-a.e.,\left\{\begin{aligned} &y\_{\text{SSD}}^{\*}\text{ is right-continuous and }0\leqslant\frac{\mathrm{d}y\_{\text{SSD}}^{\*}(t)}{\mathrm{d}Q\_{\rho}(t)}\leqslant 1,\text{ }Q\_{\rho}(t)-y\_{\text{SSD}}^{\*}(t)>0\text{ for all }t\in(0,1);\\ &z\_{\text{SSD}}^{\*}(s)\triangleq-\int\_{s}^{1}\left(I(\lambda(Q\_{\rho}(t)-y\_{\text{SSD}}^{\*}(t)))-Q\_{0}(1-t)\right)\mathrm{d}t,~s\in[0,1];\\ &\frac{\mathrm{d}y\_{\text{SSD}}^{\*}(t)}{\mathrm{d}Q\_{\rho}(t)}\left\{\begin{aligned} &\in[0,1],&&z\_{\text{SSD}}^{\*}(t)=0;\\ &=0,&&z\_{\text{SSD}}^{\*}(t)<0,\end{aligned}\right.\quad dQ\_{\rho}\text{-a.e.,}\end{aligned}\right. |  | (11) |

and the Lagrange multiplier λ>0\lambda>0 is determined by the binding budget constraint equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01QSSD∗​(s)​Qρ​(1−s)​ds=x¯.\displaystyle\int\_{0}^{1}Q\_{\text{SSD}}^{\*}(s)Q\_{\rho}(1-s)\mathrm{d}s=\overline{x}. |  | (12) |

In the proof of Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)), the procedure of solving Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) starts with a view of quantile formulation (He and Zhou ([2011](https://arxiv.org/html/2512.00299v1#bib.bib6)); Xia and Zhou ([2016](https://arxiv.org/html/2512.00299v1#bib.bib20)); Xu ([2016](https://arxiv.org/html/2512.00299v1#bib.bib21))).
Specifically, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝒲≜{w:[0,1]→[0,∞)|w​(0)=0,w​ is increasing and concave},\displaystyle\mathcal{W}\triangleq\{w:[0,1]\to[0,\infty)|w(0)=0,w\text{ is increasing and concave}\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝒲1≜{w∈𝒲|w​(1)=1}.\displaystyle\mathcal{W}\_{1}\triangleq\{w\in\mathcal{W}|w(1)=1\}. |  |

Define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒬2​(Q0)\displaystyle\mathcal{Q}\_{2}(Q\_{0}) | ≜{Q∈𝒬|∫[0,1]Q​(s)​dw​(s)⩾∫[0,1]Q0​(s)​dw​(s)​ for all ​w∈𝒲}\displaystyle\triangleq\left\{Q\in\mathcal{Q}\big|\int\_{[0,1]}Q(s)\mathrm{d}w(s)\geqslant\int\_{[0,1]}Q\_{0}(s)\mathrm{d}w(s)\text{ for all }w\in\mathcal{W}\right\} |  | (13) |
|  |  | ={Q∈𝒬|∫[0,1]Q​(s)​dw​(s)⩾∫[0,1]Q0​(s)​dw​(s)​ for all ​w∈𝒲1}.\displaystyle=\left\{Q\in\mathcal{Q}\big|\int\_{[0,1]}Q(s)\mathrm{d}w(s)\geqslant\int\_{[0,1]}Q\_{0}(s)\mathrm{d}w(s)\text{ for all }w\in\mathcal{W}\_{1}\right\}. |  |

In view of quantile formulation approach, we are going to change the optimization among the random variable XX to its quantile function QXQ\_{X}. We can hence express the objective in SSD Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) as
𝔼​[U​(X)]=∫01U​(QX​(s))​ds.\mathbb{E}[U(X)]=\int\_{0}^{1}U(Q\_{X}(s))\mathrm{d}s.
Based on the counter-monotonic dependence between the optimal solution XX and the pricing kernel ρ\rho (see He and Zhou ([2011](https://arxiv.org/html/2512.00299v1#bib.bib6)) and the proof of Theorem [1](https://arxiv.org/html/2512.00299v1#Thmtheorem1 "Theorem 1. ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), we can express the budget constraint as
𝔼​[ρ​X]=∫01QX​(s)​Qρ​(1−s)​ds.\mathbb{E}[\rho X]=\int\_{0}^{1}Q\_{X}(s)Q\_{\rho}(1-s)\mathrm{d}s.
According to Föllmer and Schied ([2016](https://arxiv.org/html/2512.00299v1#bib.bib3)), SSD Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) reads as
an optimal quantile problem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | maxQ∈𝒬2​(Q0)​∫01U​(Q​(s))​ds​s.t. ​∫01Q​(s)​Qρ​(1−s)​ds⩽x¯.\displaystyle\max\_{Q\in\mathcal{Q}\_{2}(Q\_{0})}\int\_{0}^{1}U(Q(s))\mathrm{d}s~~\text{s.t. }\int\_{0}^{1}Q(s)Q\_{\rho}(1-s)\mathrm{d}s\leqslant\overline{x}. |  | (14) |

The next step of solving Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is a conversion from Problem ([14](https://arxiv.org/html/2512.00299v1#S4.E14 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | maxQ∈𝒬∫01U(Q(s))ds s.t. {∫01Q​(s)​Qρ​(1−s)​ds⩽x,infw∈𝒲1(∫[0,1](Q​(s)−Q0​(s))​dw​(s))⩾0.\displaystyle\max\_{Q\in\mathcal{Q}}\int\_{0}^{1}U(Q(s))\mathrm{d}s~~\text{ s.t. }\left\{\begin{aligned} &\int\_{0}^{1}Q(s)Q\_{\rho}(1-s)\mathrm{d}s\leqslant x,\\ &\inf\_{w\in\mathcal{W}\_{1}}\left(\int\_{[0,1]}(Q(s)-Q\_{0}(s))\mathrm{d}w(s)\right)\geqslant 0.\end{aligned}\right. |  | (15) |

If the optimal solution of the original problem satisfies the second constraint in Problem ([15](https://arxiv.org/html/2512.00299v1#S4.E15 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), then the optimal solution of Problem ([15](https://arxiv.org/html/2512.00299v1#S4.E15 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is the same as that of the original problem and it is considered as a trivial case. In the non-trivial case, for any λ>0\lambda>0, Q∈𝒬Q\in\mathcal{Q} and w∈𝒲w\in\mathcal{W}, we let

|  |  |  |
| --- | --- | --- |
|  | K​(Q,w;λ)=∫01U​(Q​(s))​ds−λ​∫01Q​(s)​Qρ​(1−s)​ds+∫[0,1](Q​(s)−Q0​(s))​dw​(s).K(Q,w;\lambda)=\int\_{0}^{1}U(Q(s))\mathrm{d}s-\lambda\int\_{0}^{1}Q(s)Q\_{\rho}(1-s)\mathrm{d}s+\int\_{[0,1]}(Q(s)-Q\_{0}(s))\mathrm{d}w(s). |  |

One needs to consider the following max-min problem for KK:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxQ∈𝒬⁡minw∈𝒲⁡K​(Q,w;λ).\max\_{Q\in\mathcal{Q}}\min\_{w\in\mathcal{W}}K(Q,w;\lambda). |  | (16) |

Unfortunately, the solution procedure of the SSD Problem under non-concave utility is stuck at this step, because the desired Sion’s max-min theorem requires that KK is concave in QQ, which does not hold generally. In an alternative clue of concavifying UU (see Liang and Liu ([2020](https://arxiv.org/html/2512.00299v1#bib.bib10))), one cannot guarantee that the concavification principle is valid (i.e., the optimal wealth variable under the concave envelope is almost surely not located in the region where the original utility and its concave envelope do not coincide). Even if a similar form of Theorem [2](https://arxiv.org/html/2512.00299v1#Thmtheorem2 "Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") is established for general non-concave utilities, one needs to solve the optimal pair (y∗,z∗)(y^{\*},z^{\*}) from the system ([11](https://arxiv.org/html/2512.00299v1#S4.E11 "In Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), which is an infinite-dimensional optimization problem over the functional space. Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)) propose some explicit optimal solutions based on specific and technical assumptions on UU, QρQ\_{\rho} and Q0Q\_{0}. Beyond these, there is no general analytical expression for optimal solutions.

Nevertheless, Theorem 5.10 of Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)) provides an important idea that the optimal solution may be characterized by the optimal pair (y∗,z∗)(y^{\*},z^{\*}) from the system ([11](https://arxiv.org/html/2512.00299v1#S4.E11 "In Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), and hence we can obtain some heuristics to construct suboptimal solutions based on numerical algorithms and even neural networks. Specifically, we define a concept of the poor performance region:

|  |  |  |
| --- | --- | --- |
|  | C≜{t∈(0,1)|I​(λ​Qρ​(t))−Q0​(1−t)<0}.C\triangleq\left\{t\in(0,1)|I(\lambda Q\_{\rho}(t))-Q\_{0}(1-t)<0\right\}. |  |

Here for the non-concave utility UU, we define
I​(y)≜inf{arg​supx∈ℝ[U​(x)−x​y]},y>0I(y)\triangleq\inf\{\arg\sup\_{x\in\mathbb{R}}\left[U(x)-xy\right]\},~y>0 whenever applicable. For example, if UU is a S-shaped utility with the domain [L,∞)[L,\infty) where L∈ℝL\in\mathbb{R}, we have I​(⋅)I(\cdot) is well-defined, while if the domain is ℝ\mathbb{R}, we have I​(⋅)≡−∞I(\cdot)\equiv-\infty.

Remark: ”Whenever applicable” means that the function II is finite for any y∈(0,∞)y\in(0,\infty). That is, the utility UU has a finite concave envelope function (the smallest concave function dominating UU; see Liang and Liu ([2020](https://arxiv.org/html/2512.00299v1#bib.bib10))). In this case, I​(⋅)I(\cdot) is right-continuous and decreasing on (0,+∞)(0,+\infty).

In the set CC, we compare the unconstrained classic solution I​(λ​Qρ​(t))I(\lambda Q\_{\rho}(t)) with the SSD benchmark Q0​(1−t)Q\_{0}(1-t). If C=∅C=\emptyset, then it means that the unconstrained solution automatically satisfies the SSD constraint and QSSD∗Q\_{\text{SSD}}^{\*} should be the same as the unconstrained solution. Next, we discuss the non-trivial case (i.e., C≠∅C\neq\emptyset). For the scenario tt on this region, the unconstrained solution I​(λ​Qρ​(t))I(\lambda Q\_{\rho}(t)) is smaller (i.e., performing worse) than the SSD benchmark Q0​(1−t)Q\_{0}(1-t).
From Definition [1](https://arxiv.org/html/2512.00299v1#Thmdefinition1 "Definition 1 (Stochastic dominance). ‣ 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), the SSD constraint QSSD∗⪰(2)Q0Q\_{\text{SSD}}^{\*}\succeq\_{(2)}Q\_{0} reads as

|  |  |  |
| --- | --- | --- |
|  | ∫0sQSSD∗​(t)​dt⩾∫0sQ0​(t)​dt​ for any ​s∈(0,1),\int\_{0}^{s}Q\_{\text{SSD}}^{\*}(t)\mathrm{d}t\geqslant\int\_{0}^{s}Q\_{0}(t)\mathrm{d}t~~\text{ for any }s\in(0,1), |  |

which is reflected in the system ([11](https://arxiv.org/html/2512.00299v1#S4.E11 "In Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")):

|  |  |  |
| --- | --- | --- |
|  | zSSD∗​(s)=−∫s1(QSSD∗​(1−t)−Q0​(1−t))​dt⩽0​ for any ​s∈(0,1).z\_{\text{SSD}}^{\*}(s)=-\int\_{s}^{1}\left(Q\_{\text{SSD}}^{\*}(1-t)-Q\_{0}(1-t)\right)\mathrm{d}t\leqslant 0~~\text{ for any }s\in(0,1). |  |

which translates to

|  |  |  |  |
| --- | --- | --- | --- |
|  | zSSD∗​(s)=−∫s1(I​(λ​(Qρ​(t)−ySSD∗​(t)))−Q0​(1−t))​dt⩽0​ for any ​s∈(0,1).z\_{\text{SSD}}^{\*}(s)=-\int\_{s}^{1}\left(I(\lambda(Q\_{\rho}(t)-y\_{\text{SSD}}^{\*}(t)))-Q\_{0}(1-t)\right)\mathrm{d}t\leqslant 0~~\text{ for any }s\in(0,1). |  | (17) |

The theorem inspires that some correction function ySSD∗y\_{\text{SSD}}^{\*} should be added to satisfy the constraint ([17](https://arxiv.org/html/2512.00299v1#S4.E17 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")). In the next subsection, we provide a numerical algorithm and design the correction function to obtain a sub-optimal solution.

### 4.2 SSD Problem: Numerical Algorithm

Algorithm 1  Poor-Performance-Region Algorithm for SSD Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) with general utilities

1:We solve the classic problem without the SSD constraint and obtain the optimal quantile QclaQ\_{\text{cla}}. The Lagrange multiplier is denoted by λcla∈(0,∞)\lambda\_{\text{cla}}\in(0,\infty), which is solved from the following equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | x¯\displaystyle\overline{x} | =∫01Qρ​(s)​I​(λcla​Qρ​(s))​ds.\displaystyle=\int\_{0}^{1}Q\_{\rho}(s)I(\lambda\_{\text{cla}}Q\_{\rho}(s))\mathrm{d}s. |  |

If

|  |  |  |
| --- | --- | --- |
|  | −∫t1(I​(λcla​Qρ​(s))−Q0​(1−s))​ds⩽0-\int\_{t}^{1}\left(I(\lambda\_{\text{cla}}Q\_{\rho}(s))-Q\_{0}(1-s)\right)\mathrm{d}s\leqslant 0 |  |

holds for any t∈[0,1]t\in[0,1], then the optimal solution is Qcla(⋅)≜I(λclaQρ(1−⋅))Q\_{\text{cla}}(\cdot)\triangleq I(\lambda\_{\text{cla}}Q\_{\rho}(1-\cdot)). Otherwise, we start the procedure below.

2:The Lagrange multiplier is initially set as the above λ\lambda (to be determined at last). Compute the set

|  |  |  |
| --- | --- | --- |
|  | C={t∈(0,1)|I​(λ​Qρ​(t))−Q0​(1−t)<0}.C=\left\{t\in(0,1)|I(\lambda Q\_{\rho}(t))-Q\_{0}(1-t)<0\right\}. |  |

3:If C=∅C=\emptyset, then the optimal solution is QclaQ\_{\text{cla}}. Otherwise, specify an appropriate n∈ℕn\in\mathbb{N} and write C=∪i=1n(ai,bi)C=\cup\_{i=1}^{n}(a\_{i},b\_{i}) with ai<bia\_{i}<b\_{i}. Further we set an+1=1a\_{n+1}=1.

4:For i=n,(n−1),…,1i=n,(n-1),\dots,1 (Steps 4-6), we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | y0​(s)=inf{y⩾0|I​(λ​(Qρ​(s)−y))−Q0​(1−s)⩾0},s∈(ai,bi).y\_{0}(s)=\inf\{y\geqslant 0|I\left(\lambda(Q\_{\rho}(s)-y)\right)-Q\_{0}(1-s)\geqslant 0\},~~\text{$s\in(a\_{i},b\_{i})$}. |  | (18) |

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | gi​(s)=−∫sai+1(I​(λ​(Qρ​(t)−y0​(s)))−Q0​(1−t))​dt,s∈(ai,bi).g\_{i}(s)=-\int\_{s}^{a\_{i+1}}\left(I\left(\lambda\left(Q\_{\rho}(t)-y\_{0}(s)\right)\right)-Q\_{0}(1-t)\right)\mathrm{d}t,~~s\in(a\_{i},b\_{i}). |  | (19) |

5:We compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ti=sup{t∈[ai,bi]|gi​(t)+zsub​(ai+1)​𝟙{i≠n}>0},t\_{i}=\sup\Big\{\,t\in[a\_{i},b\_{i}]\;\big|\;g\_{i}(t)+z\_{\text{sub}}(a\_{i+1})\mathds{1}\_{\{i\neq n\}}>0\Big\}, |  | (20) |

where zsub​(⋅)z\_{\text{sub}}(\cdot) will be determined in Step 6.
If {t∈[ai,bi]|gi​(t)+zsub​(ai+1)​𝟙{i≠n}>0}=∅\{t\in[a\_{i},b\_{i}]|g\_{i}(t)+z\_{\text{sub}}(a\_{i+1})\mathds{1}\_{\{i\neq n\}}>0\}=\emptyset, set ti=ait\_{i}=a\_{i}.

6:Set

|  |  |  |  |
| --- | --- | --- | --- |
|  | ysub​(⋅)≡y0​(ti)​ on ​(ti,ai+1)​ and ​ysub​(⋅)=y0​(⋅)​ on ​(ai,ti).y\_{\text{sub}}(\cdot)\equiv y\_{0}(t\_{i})\text{ on }(t\_{i},a\_{i+1})~~\text{ and }~~y\_{\text{sub}}(\cdot)=y\_{0}(\cdot)~\text{ on }(a\_{i},t\_{i}). |  | (21) |

Define zsub​(⋅)z\_{\text{sub}}(\cdot) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zsub​(s)≜−∫s1(I​(λ​(Qρ​(t)−ysub​(t)))−Q0​(1−t))​dt,s∈[ai,ai+1].z\_{\text{sub}}(s)\triangleq-\int\_{s}^{1}\left(I(\lambda(Q\_{\rho}(t)-y\_{\text{sub}}(t)))-Q\_{0}(1-t)\right)\mathrm{d}t,~s\in[a\_{i},a\_{i+1}]. |  | (22) |

7:Set t0=0t\_{0}=0 and y0​(t0)=0y\_{0}(t\_{0})=0. After the iteration, we have Eq. ([21](https://arxiv.org/html/2512.00299v1#S4.E21 "In 6 ‣ Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) for i=n,…,1i=n,\dots,1
and ysub​(⋅)≡y0​(t0)y\_{\text{sub}}(\cdot)\equiv y\_{0}(t\_{0}) on (t0,a1](t\_{0},a\_{1}]. We then verify whether ysub​(⋅)y\_{\textbf{sub}}(\cdot) satisfies the monotonicity condition (non-decreasing over (0,1)(0,1)). If the condition holds, proceed to Step 14; otherwise, apply the correction procedure and proceed to Step 8.

8:For i=n,(n−1),…,2i=n,(n-1),\dots,2 (Steps 8-12), check whether y0​(⋅)y\_{0}(\cdot) is increasing (non-decreasing) over (ai−1,ai+1)(a\_{i-1},a\_{i+1}). If yes, skip and proceed to next iteration; if not, proceed to Step 11.

9:Compute y0​(⋅)y\_{0}(\cdot) over (ai−1,bi−1)(a\_{i-1},b\_{i-1}) and (ai,bi)(a\_{i},b\_{i}) by Eq. ([18](https://arxiv.org/html/2512.00299v1#S4.E18 "In 4 ‣ Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

10:Redefine

|  |  |  |
| --- | --- | --- |
|  | gi​(s)=−∫ss¯(I​(λ​(Qρ​(t)−y0​(s)))−Q0​(1−t))​dt,s∈(ai−1,bi−1),g\_{i}(s)=-\int\_{s}^{\bar{s}}\left(I\left(\lambda\left(Q\_{\rho}(t)-y\_{0}(s)\right)\right)-Q\_{0}(1-t)\right)\mathrm{d}t,~~s\in(a\_{i-1},b\_{i-1}), |  |

where s¯=inf{t⩾ai|y0​(t)−y0​(s)⩾0},t∈[ai,bi).\bar{s}=\inf\{t\geqslant a\_{i}|y\_{0}(t)-y\_{0}(s)\geqslant 0\},t\in[a\_{i},b\_{i}).

11:Compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | tleft=sup{t∈[a1,b1]|g1​(t)>0},tright=s¯.t\_{\text{left}}=\sup\{t\in[a\_{1},b\_{1}]|g\_{1}(t)>0\},\;\;t\_{\text{right}}=\bar{s}. |  | (23) |



12:Replace the initial ysub​(⋅)y\_{\text{sub}}(\cdot) over (tleft,tright)(t\_{\text{left}},t\_{\text{right}}) and set

|  |  |  |
| --- | --- | --- |
|  | ysub​(⋅)≡y0​(tleft)​ on ​(tleft,tright).y\_{\text{sub}}(\cdot)\equiv y\_{0}(t\_{\text{left}})\text{ on }(t\_{\text{left}},t\_{\text{right}}). |  |

13:After the iteration, check whether ysub​(⋅)y\_{\text{sub}}(\cdot) satisfy the monotonicity condition. If yes, proceed to next step; otherwise, the algorithm may fail.

14:Hence, we design the sub-optimal solution by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qsub(s)={I​(λ​(Qρ​(1−s)−y0​(tn))),s∈(1−an+1,1−tn];I​(λ​(Qρ​(1−s)−y0​(1−s)))≡Q0​(s),s∈(1−tn,1−an];…I​(λ​(Qρ​(1−s)−y0​(t0))),s∈(1−a1,1−t0).Q\_{\text{sub}}(s)=\left\{\begin{aligned} &I\left(\lambda\left(Q\_{\rho}(1-s)-y\_{0}(t\_{n})\right)\right),&&s\in(1-a\_{n+1},1-t\_{n}];\\ &I\left(\lambda\left(Q\_{\rho}(1-s)-y\_{0}(1-s)\right)\right)\equiv Q\_{0}(s),&&s\in(1-t\_{n},1-a\_{n}];\\ &\dots\\ &I\left(\lambda\left(Q\_{\rho}(1-s)-y\_{0}(t\_{0})\right)\right),&&s\in(1-a\_{1},1-t\_{0}).\\ \end{aligned}\right. |  | (24) |

15:Set

|  |  |  |
| --- | --- | --- |
|  | zi∗​(t)=−∫t1(I​(λ​(Qρ​(s)−y0​(ti)))−Q0​(1−s))​ds,t∈(max⁡{ai,ti},ai+1).z^{\*}\_{i}(t)=-\int\_{t}^{1}\left(I\left(\lambda\left(Q\_{\rho}(s)-y\_{0}(t\_{i})\right)\right)-Q\_{0}(1-s)\right)\mathrm{d}s,~~t\in(\max\{a\_{i},t\_{i}\},a\_{i+1}). |  |

If for any i=1,…,ni=1,\dots,n, zi∗​(⋅)⩽0z^{\*}\_{i}(\cdot)\leqslant 0 always holds on the interval (max⁡{ai,ti},ai+1)(\max\{a\_{i},t\_{i}\},a\_{i+1}), this
QsubQ\_{\text{sub}} is sub-optimal.

16:Using a bisection method, we determine λsub∈(0,∞)\lambda\_{\text{sub}}\in(0,\infty) from the following equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x¯\displaystyle\overline{x} | =∫01Qρ​(s)​Qsub​(1−s)​ds.\displaystyle=\int\_{0}^{1}Q\_{\rho}(s)Q\_{\text{sub}}(1-s)\mathrm{d}s. |  | (25) |

Inspired by the structure of the optimal solution ([10](https://arxiv.org/html/2512.00299v1#S4.E10 "In Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), We proceed to present a numerical algorithm to propose a suboptimal solution QsubQ\_{\text{sub}}, where we design a correction function ysuby\_{\text{sub}} based on the value of zsubz\_{\text{sub}} in different sections of the poor performance region CC.

Detecting the structure of the poor performance region is the key task. We first define a function

|  |  |  |  |
| --- | --- | --- | --- |
|  | y0​(s)≜inf{y⩾0|I​(λ​(Qρ​(s)−y))−Q0​(1−s)⩾0},s∈(0,1).y\_{0}(s)\triangleq\inf\{y\geqslant 0|I\left(\lambda(Q\_{\rho}(s)-y)\right)-Q\_{0}(1-s)\geqslant 0\},~~s\in(0,1). |  | (26) |

Hence, we alternatively write the poor performance region as

|  |  |  |  |
| --- | --- | --- | --- |
|  | C={t∈(0,1)|y0​(t)>0}.C=\{t\in(0,1)|y\_{0}(t)>0\}. |  | (27) |

For some very poorly-performed scenarios t∈Ct\in C, the function y0y\_{0} is adopted such that Qsub​(1−t)=I​(λ​(Qρ​(t)−y0​(t)))=Q0​(1−t)Q\_{\text{sub}}(1-t)=I(\lambda(Q\_{\rho}(t)-y\_{0}(t)))=Q\_{0}(1-t).

The general idea in the construction of the sub-optimal solution to SSD Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) is: When zsub⩽0z\_{\text{sub}}\leqslant 0, we use the classic solution to achieve optimality (now ysub=0y\_{\text{sub}}=0 or constant, and QSSDQ\_{\text{SSD}} is the form of II); When zsub>0z\_{\text{sub}}>0, we set ysub=y0y\_{\text{sub}}=y\_{0} such that Qsub=Q0Q\_{\text{sub}}=Q\_{0} to satisfy the SSD constraint. Throughout the algorithm design, we need to guarantee that ysuby\_{\text{sub}} is increasing and non-negative.

We therefore propose Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") below, named the Poor-Performance-Region Algorithm. Based on Theorem [2](https://arxiv.org/html/2512.00299v1#Thmtheorem2 "Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), we design a closed-form sub-optimal solution to Problem ([14](https://arxiv.org/html/2512.00299v1#S4.E14 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qsub​(s)=∑i=0nI​(λsub​(Qρ​(1−s)−y0​(ti)))​𝟙{s∈(1−ai+1,1−ti)}+∑i=1nQ0​(s)​𝟙{s∈[1−ti,1−ai]},s∈(0,1).Q\_{\text{sub}}(s)=\sum\_{i=0}^{n}I\left(\lambda\_{\text{sub}}\left(Q\_{\rho}(1-s)-y\_{0}(t\_{i})\right)\right)\mathds{1}\_{\{s\in(1-a\_{i+1},1-t\_{i})\}}+\sum\_{i=1}^{n}Q\_{0}(s)\mathds{1}\_{\{s\in[1-t\_{i},1-a\_{i}]\}},\;\;s\in(0,1). |  | (28) |

This quantile function is also given in Eq. ([24](https://arxiv.org/html/2512.00299v1#S4.E24 "In 14 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")). The key idea is to use an increasing step function ySSD∗​(⋅)y^{\*}\_{\text{SSD}}(\cdot) for approximation. The financial insight is that the decision maker should follow the SSD benchmark quantile Q0Q\_{0} on some poor performance scenario and conduct the unconstrained optimal strategy I​(λsub​(Qρ​(1−s)−y0​(ti)))I\left(\lambda\_{\text{sub}}\left(Q\_{\rho}(1-s)-y\_{0}(t\_{i})\right)\right) otherwise.

Here are some explanations of the algorithm design.

1. a.

   In this algorithm, the partition points {ai}i=1n{\{a\_{i}\}}^{n}\_{i=1} and {ti}i=1n{\{t\_{i}\}}^{n}\_{i=1} of the poor performance region play an essential role in determining the structure of the optimal solution.
2. b.

   In Step 2: In the whole procedure, we are solving out the structure of the optimal solution and the Lagrange multiplier. For the latter, note that the initial Lagrange multiplier may not satisfy the budget constraint. But it is a good initial point to start the algorithm. It will be determined in the last step.
3. c.

   In Step 3: Because I​(λ​Qρ​(⋅))I(\lambda Q\_{\rho}(\cdot)) and Q0(1−⋅)Q\_{0}(1-\cdot) are both nonincreasing, the set CC can be written as the union of disjoint intervals ∪i=1n(ai,bi)\cup\_{i=1}^{n}(a\_{i},b\_{i}) or ∪i=1∞(ai,bi)\cup\_{i=1}^{\infty}(a\_{i},b\_{i}). In the latter case, to construct a numerically tractable solution, we use the union of the first nn disjoint intervals, where nn can be specified based on one’s computational capability.
4. d.

   In Steps 4-5: For any t∈[bi,ai+1)t\in[b\_{i},a\_{i+1}), we have
   I(λ^\* (Q\_ρ(s) - y\_0(t) ) ) - Q\_0(1-s) ⩾I(λ^\* (Q\_ρ(s) ) ) - Q\_0(1-s) ⩾0,    s ∈(t, a\_i+1].
   We then compute
   g\_i(t) = - ∫\_t^a\_i+1 ( I(λ^\* (Q\_ρ(s) - y\_0(t) ) ) - Q\_0(1-s) ) ds ⩽0.
   Hence, any t∈[bi,ai+1)t\in[b\_{i},a\_{i+1}) satisfies the SSD constraint. We desire to search the first point tit\_{i} on (ai,b1)(a\_{i},b\_{1}) which does not satisfy the constraint.
5. e.

   In Steps 8-12, we need to check whether the constructed ysub​(⋅)y\_{\text{sub}}(\cdot) is non-decreasing on (0,1) to make the solution valid. It holds in many cases. However, in some extreme cases, we could still ensure the monotonicity by redesigning the construction of tit\_{i} defined in Eq. ([20](https://arxiv.org/html/2512.00299v1#S4.E20 "In 5 ‣ Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), which is named tleftt\_{\text{left}} in Eq. ([23](https://arxiv.org/html/2512.00299v1#S4.E23 "In 11 ‣ Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")). The specific case will be shown in Section [5](https://arxiv.org/html/2512.00299v1#S5 "5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").
6. f.

   In Step 14, in many cases, one can design that Qsub(⋅)=I(λ(Qρ(1−⋅)−y0(⋅)))=Q0(⋅)Q\_{\text{sub}}(\cdot)=I(\lambda(Q\_{\rho}(1-\cdot)-y\_{0}(\cdot)))=Q\_{0}(\cdot) on (1−tn,1−an](1-t\_{n},1-a\_{n}].
7. g.

   In Step 15, we need to check the condition holds numerically. It holds in many cases.

In the later sections, based on Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), we are able to provide the numerical illustration for the SSD Problem ([4](https://arxiv.org/html/2512.00299v1#S2.E4 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) with various concrete settings.

## 5 Numerical Results

Our study is motivated by the Black-Scholes model in a complete market. A classic Black-Scholes model consists of one riskless bond (d​BtBt=r​d​t,t∈[0,T)\frac{\mathrm{d}B\_{t}}{B\_{t}}=r\mathrm{d}t,~t\in[0,T), where the risk-free rate is r=0.05r=0.05) and one stock (d​StSt=μS​d​t+σS​d​Wt,t∈[0,T)\frac{\mathrm{d}S\_{t}}{S\_{t}}=\mu\_{\text{S}}\mathrm{d}t+\sigma\_{\text{S}}\mathrm{d}W\_{t},~t\in[0,T), which is a geometric Brownian motion with the expected return rate μS=0.086\mu\_{\text{S}}=0.086 and the volatility parameter σS=0.3\sigma\_{\text{S}}=0.3 and {Wt}0⩽t⩽T\{W\_{t}\}\_{0\leqslant t\leqslant T} is a standard Brownian motion).
The wealth process is given by
d​Xt=(r​Xt+(μS−r)​πt)​d​t+σS​πt​d​Wt,t∈[0,T)\mathrm{d}X\_{t}=\left(rX\_{t}+(\mu\_{S}-r)\pi\_{t}\right)\mathrm{d}t+\sigma\_{S}\pi\_{t}\mathrm{d}W\_{t},~t\in[0,T)
and
X0=x¯X\_{0}=\overline{x},
where {πt}0⩽t<T\{\pi\_{t}\}\_{0\leqslant t<T} is the control process representing the investment amount in the stock and T∈(0,∞)T\in(0,\infty) is the evaluation time of investment. We define the pricing kernel process {ρt}0⩽t⩽T\{\rho\_{t}\}\_{0\leqslant t\leqslant T} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​ρtρt=−r​d​t−θ​d​Wt,t∈[0,T],\displaystyle\frac{\mathrm{d}\rho\_{t}}{\rho\_{t}}=-r\mathrm{d}t-\theta\mathrm{d}W\_{t},~~t\in[0,T], |  | (29) |

where we denote the market price of risk by θ≜(μS−r)/σS\theta\triangleq(\mu\_{S}-r)/\sigma\_{S}.

As the market is complete and one can use the martingale method to duplicate the optimal portfolio process, it is sufficient to solve the optimal terminal wealth variable via the static problem ([1](https://arxiv.org/html/2512.00299v1#S2.E1 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) (see, e.g., Liang and Liu ([2024](https://arxiv.org/html/2512.00299v1#bib.bib11))). Hence, our focus is solving the optimal wealth variable in Problem ([1](https://arxiv.org/html/2512.00299v1#S2.E1 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).
Adapting to Problem ([1](https://arxiv.org/html/2512.00299v1#S2.E1 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), we denote the terminal variables of pricing kernel and wealth by ρ:=ρT\rho:=\rho\_{T} and X:=XTX:=X\_{T}, with a slight abuse of notation. Solving from Eq. ([29](https://arxiv.org/html/2512.00299v1#S5.E29 "In 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), ρ\rho follows the log-normal distribution (i.e., log⁡(ρ)∼N​(−(r+θ2/2)​T,(θ​T)2)\log(\rho)\sim\text{N}(-(r+\theta^{2}/2)T,(\theta\sqrt{T})^{2})) and has a quantile function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qρ(t)=exp{θTΦ−1(t)−(r+θ2/2)T)}≜exp{σΦ−1(t)+μ},t∈(0,1),Q\_{\rho}(t)=\exp\left\{\theta\sqrt{T}\Phi^{-1}(t)-(r+\theta^{2}/2)T)\right\}\triangleq\exp\left\{\sigma\Phi^{-1}(t)+\mu\right\},~t\in(0,1), |  | (30) |

where we denote by Φ−1\Phi^{-1} the standard normal quantile function and define σ≜θ​T\sigma\triangleq\theta\sqrt{T} and μ≜−(r+θ2/2)T)\mu\triangleq-(r+\theta^{2}/2)T).
In Sections [5](https://arxiv.org/html/2512.00299v1#S5 "5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")-[6](https://arxiv.org/html/2512.00299v1#S6 "6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), we will mainly consider this QρQ\_{\rho} in Eq. ([30](https://arxiv.org/html/2512.00299v1#S5.E30 "In 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) and specify different benchmark quantile functions Q0Q\_{0} and various utility functions.

We specify the parameters:
the risk-free rate is r=0.05r=0.05;
the expected return rate μS=0.086\mu\_{\text{S}}=0.086;
the volatility parameter σS=0.3\sigma\_{\text{S}}=0.3;
The evaluation time of investment is T=20T=20 (years).
It follows that the market price of risk is θ=(μ−r)/σ=0.12\theta=(\mu-r)/\sigma=0.12. We compute that σ=0.5367\sigma=0.5367 and μ=−1.1440\mu=-1.1440.
We numerically illustrate our result by using the Black-Scholes model above.

### 5.1 FSD Problem: S-shaped Utility (Theorem [1](https://arxiv.org/html/2512.00299v1#Thmtheorem1 "Theorem 1. ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"))

We begin by specifying a S-shaped utility U:[L,∞)→ℝU:[L,\infty)\rightarrow\mathbb{R}, following the general S-shaped utility formulation in Definition [2](https://arxiv.org/html/2512.00299v1#Thmdefinition2 "Definition 2 (General S-shaped utility). ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | U(x)={xpp,x⩾0,−k​(−x)q,L⩽x<0,\displaystyle U(x)=\left\{\begin{aligned} &\frac{x^{p}}{p},&&x\geqslant 0,\\ &-k(-x)^{q},&&L\leqslant x<0,\end{aligned}\right. |  | (31) |

where the parameters are set to p=0.6,q=0.5p=0.6,q=0.5, and k=2k=2.

We then consider two portfolio selection problems. The first is Problem ([3](https://arxiv.org/html/2512.00299v1#S2.E3 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) with the general setting of S-shaped utility in Definition [2](https://arxiv.org/html/2512.00299v1#Thmdefinition2 "Definition 2 (General S-shaped utility). ‣ 3 FSD Problem and Analytical Solution ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (In particular, Eq. ([31](https://arxiv.org/html/2512.00299v1#S5.E31 "In 5.1 FSD Problem: S-shaped Utility (Theorem 1) ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"))) and the benchmark quantile
Q0​(t)=10​t2−1,t∈[0,1].Q\_{0}(t)=10t^{2}-1,\;t\in[0,1].
The second is the Merton problem ([1](https://arxiv.org/html/2512.00299v1#S2.E1 "In 2 Model Settings ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) using the S-shaped utility setting in Eq. ([31](https://arxiv.org/html/2512.00299v1#S5.E31 "In 5.1 FSD Problem: S-shaped Utility (Theorem 1) ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | maxX∈L0⁡𝔼​[U​(X)], s.t. ​𝔼​[ρ​X]⩽x¯,X⩾L​ a.s. ,\displaystyle\max\_{X\in L^{0}}\mathbb{E}[U(X)],\text{ s.t. }\mathbb{E}[\rho X]\leqslant\overline{x},\;X\geqslant L\text{ a.s. }, |  | (32) |

where the liquidation boundary is given by L=−5L=-5. Here we add the liquidation boundary in order to make the second problem well defined and compare with the first problem.

In this example, the first-order SD constraint acts a similar role as the liquidation constraint: if Q0​(1−Fρ​(ρ))=Q0​(0)Q\_{0}(1-F\_{\rho}(\rho))=Q\_{0}(0), then the optimal solution X∗X^{\*} locates at the boundary Q0​(1−Fρ​(ρ))Q\_{0}(1-F\_{\rho}(\rho)), otherwise X∗X^{\*} is the same as the classic solution (U1′)−1​(λ​ρ)(U\_{1}^{\prime})^{-1}(\lambda\rho).

![Refer to caption](x1.png)


Figure 1: First-order SD constraint: x¯=5\bar{x}=5

### 5.2 SSD Problem: Power Utility

We first assume the decision maker has a CRRA utility

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(x)=1p​xp,x>0,U(x)=\frac{1}{p}x^{p},~~x>0, |  | (33) |

where p=0.6p=0.6. We suppose that the benchmark quantile Q0Q\_{0} also follows the log-normal distribution:

|  |  |  |
| --- | --- | --- |
|  | Q0​(t)=exp⁡{σ0​Φ−1​(t)+μ0},t∈[0,1].Q\_{0}(t)=\exp\left\{\sigma\_{0}\Phi^{-1}(t)+\mu\_{0}\right\},\;t\in[0,1]. |  |

The settings are given in Table [1](https://arxiv.org/html/2512.00299v1#S5.T1 "Table 1 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rr | μS\mu\_{\text{S}} | σS\sigma\_{\text{S}} | θ\theta | TT | μ\mu | σ\sigma | x¯\overline{x} | pp |
| 0.05 | 0.086 | 0.3 | 0.12 | 20 | -1.1440 | 0.5367 | 10 | 0.6 |

Table 1: Parameter setting in the numerical illustration.

For the concave utility specified in Eq. ([33](https://arxiv.org/html/2512.00299v1#S5.E33 "In 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), the applicability of Proposition 6.8 in Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)) to power utility with a log-normal pricing kernel provides a theoretical benchmark. Our algorithm’s result coincides with the characterization in Wang and Xia ([2021](https://arxiv.org/html/2512.00299v1#bib.bib18)). Consequently, the algorithm attains the optimal solution in the following cases in Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").
For comparison, we also compute the classical optimal solution obtained without the SSD constraint and plot the figure.

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=226.16321pt]{PowerU\_result/3\_1.eps}&\includegraphics[width=226.16321pt]{PowerU\_result/3\_0.6.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=226.16321pt]{PowerU\_result/3\_1.4.eps}&\includegraphics[width=226.16321pt]{PowerU\_result/3.2\_1.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=226.16321pt]{PowerU\_result/2.3\_2.eps}&\includegraphics[width=226.16321pt]{PowerU\_result/1.5\_2.5.eps}\end{matrix} |  |

Figure 2: Impacts of μ0\mu\_{0} and σ0\sigma\_{0}.



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | parametrization | budget of Q0Q\_{0} | poor performance region CC | λ\lambda | λcla\lambda\_{\text{cla}} | partition parameter |
| (a) | (μ0,σ0)=(3,1)(\mu\_{0},\sigma\_{0})=(3,1) | 7.1231 | (0.6092,1)(0.6092,1) | 0.91040.9104 | 0.9003 | t1=1t\_{1}=1 |
| (b) | (μ0,σ0)=(3,0.6)(\mu\_{0},\sigma\_{0})=(3,0.6) | 6.4109 | (0.4978,1)(0.4978,1) | 0.9471 | 0.9003 | t1=1t\_{1}=1 |
| (c) | (μ0,σ0)=(3,1.4)(\mu\_{0},\sigma\_{0})=(3,1.4) | 9.2876 | (0, 0.0179) | 0.9003 | 0.9003 | t1=0t\_{1}=0 |
| (d) | (μ0,σ0)=(3.2,1)(\mu\_{0},\sigma\_{0})=(3.2,1) | 8.7002 | (0.2858, 1) | 0.9430 | 0.9003 | t1=1t\_{1}=1 |
| (e) | (μ0,σ0)=(2.3,2)(\mu\_{0},\sigma\_{0})=(2.3,2) | 9.2691 | (0, 0.4309) | 1.1951 | 0.9003 | t1=0.0057t\_{1}=0.0057 |
| (f) | (μ0,σ0)=(1.5,2.5)(\mu\_{0},\sigma\_{0})=(1.5,2.5) | 9.8096 | (0, 0.6248) | 1.9965 | 0.9003 | t1=0.0654t\_{1}=0.0654 |

Table 2: Numerical results in Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

The basic logic is that:

1. (i)

   If the value of the pricing kernel is small, then the optimal wealth value is larger. Hence, the pricing kernel value is a signal of the market state: A small value shows a good market scenario.
2. (ii)

   If the poor performance region CC is smaller, then the optimal wealth is better (compared to the SSD constraint). This is because the SSD constraint is easier to achieve and the optimal wealth is closer to the classic unconstrained solution XclaX\_{\text{cla}}.

We apply the Poor-Performance-Region Algorithm (PPRA), the explanations and financial insights from Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") and Table [2](https://arxiv.org/html/2512.00299v1#S5.T2 "Table 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") are as follows:

1. 1.

   Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a) vs (b) vs (d): When the market performs poorly, the optimal wealth must coincide with the benchmark. This is because, in such adverse scenario, the benchmark provides a large value, and the SSD constraint serves to guarantee a minimum safety level and reduce risk.
2. 2.

   Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (c): The poor performance region is very small, which implies the classical solution inherently satisfies the SSD constraint. As a result, we observe that λ=λcla\lambda=\lambda\_{\text{cla}} and the optimal solution essentially coincides with the classical solution. This indicates that the benchmark plays only a limited role in shaping the optimal wealth.
3. 3.

   Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (e) vs (f): The budget of Q0Q\_{0} is close to x¯\bar{x}, to ensure the SSD constraint, the optimal wealth would behave similarly to the benchmark. However, due to a different λ\lambda and a correction function ysub​(⋅)y\_{\text{sub}}(\cdot) in the SSD problem, the solution between the SSD problem and the classical problem differs.

### 5.3 SSD Problem: S-shaped Utility

We use Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") to study the sub-optimal solution of the SSD problem with S-shaped utility. First, we adopt the S-shaped utility setting in Eq. ([31](https://arxiv.org/html/2512.00299v1#S5.E31 "In 5.1 FSD Problem: S-shaped Utility (Theorem 1) ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).
We then suppose that the benchmark quantile Q0Q\_{0} also follows a log-normal distribution:

|  |  |  |
| --- | --- | --- |
|  | Q0​(t)=exp⁡{σ0​Φ−1​(t)+μ0},t∈[0,1].Q\_{0}(t)=\exp\left\{\sigma\_{0}\Phi^{-1}(t)+\mu\_{0}\right\},\;t\in[0,1]. |  |

We also compute the classic optimal solution without the SSD constraint. The settings are provided in Table [3](https://arxiv.org/html/2512.00299v1#S5.T3 "Table 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rr | μS\mu\_{\text{S}} | σS\sigma\_{\text{S}} | θ\theta | TT | μ\mu | σ\sigma | x¯\overline{x} | pp | k |
| 0.05 | 0.086 | 0.3 | 0.12 | 20 | -1.1440 | 0.5367 | 10 | 0.6 | 2 |

Table 3: Parameter setting in Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").



|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=197.8937pt,height=191.42567pt]{3\_1.eps}&\includegraphics[width=197.8937pt,height=191.42567pt]{3\_0.6.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=197.8937pt,height=191.42567pt]{3\_0.8.eps}&\includegraphics[width=197.8937pt,height=191.42567pt]{3.2\_1.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=197.8937pt,height=191.42567pt]{2.3\_2.eps}&\includegraphics[width=197.8937pt,height=191.42567pt]{1.5\_2.5.eps}\end{matrix} |  |

Figure 3: Impacts of μ0\mu\_{0} and σ0\sigma\_{0}.



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | parametrization | budget of Q0Q\_{0} | poor performance region CC | λ\lambda | λcla\lambda\_{\text{cla}} | partition parameter |
| (a) | (μ0,σ0)=(3,1)(\mu\_{0},\sigma\_{0})=(3,1) | 7.1231 | (0.6089,1)(0.6089,1) | 0.91050.9105 | 0.8979 | t1=1t\_{1}=1 |
| (b) | (μ0,σ0)=(3,0.6)(\mu\_{0},\sigma\_{0})=(3,0.6) | 6.4109 | (0.4978,1)(0.4978,1) | 0.9471 | 0.8979 | t1=1t\_{1}=1 |
| (c) | (μ0,σ0)=(3,0.8)(\mu\_{0},\sigma\_{0})=(3,0.8) | 6.6238 | (0.5394,1)(0.5394,1) | 0.9255 | 0.8979 | t1=1t\_{1}=1 |
| (d) | (μ0,σ0)=(3.2,1)(\mu\_{0},\sigma\_{0})=(3.2,1) | 8.7002 | (0.2858, 1) | 0.9430 | 0.8979 | t1=1t\_{1}=1 |
| (e) | (μ0,σ0)=(2.3,2)(\mu\_{0},\sigma\_{0})=(2.3,2) | 9.2691 | (0,0.4355)∪(0.9669,1)(0,0.4355)\cup(0.9669,1) | 1.1987 | 0.8979 | t2=1,t1=0.0061t\_{2}=1,t\_{1}=0.0061 |
| (f) | (μ0,σ0)=(1.5,2.5)(\mu\_{0},\sigma\_{0})=(1.5,2.5) | 9.8087 | (0,0.6840)∪(0.7726,1)(0,0.6840)\cup(0.7726,1) | 2.1508 | 0.8979 | t2=1,t1=0.0957t\_{2}=1,t\_{1}=0.0957 |

Table 4: Numerical results in Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

We apply the Poor-Performance-Region Algorithm (PPRA), the explanations and financial insights from Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") and Table [4](https://arxiv.org/html/2512.00299v1#S5.T4 "Table 4 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") are summarized as follows:

1. 1.

   Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a) vs (b) vs (c) vs (d): These cases correspond to scenarios in which the poor performance region consists of a single interval. Numerically, a smaller μ0\mu\_{0} reduces the size of the poor performance region CC whereas a smaller σ0\sigma\_{0} enlarges it.
2. 2.

   Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"): Across the S-shaped utility cases, we observe that when the market performs poorly, relative to the classical solution, the PPRA wealth exhibits a clear improvement, driven by the SSD constraint. Therefore, in adverse market scenario, the SSD constraint effectively performs as a risk-control mechanism, ensuring that the PPRA wealth remains at least as high as the benchmark wealth.
3. 3.

   Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (e) vs (f): In these examples, the poor performance region splits into two disjoint intervals. We further observe that when the budget of Q0Q\_{0} is close to the bound x¯\bar{x}, the PPRA wealth becomes increasingly close to the benchmark. This phenomenon arises because a high level of the budget of Q0Q\_{0} make the SSD constraint dominate the optimization.
4. 4.

   Figure [3](https://arxiv.org/html/2512.00299v1#S5.F3 "Figure 3 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a) vs (b) vs (d): A deeper examination of the impact of the budget of Q0Q\_{0} shows a consistent pattern: as the budget of Q0Q\_{0} approaches the bar x¯\bar{x}, the PPRA wealth converges towards the benchmark. This illustrates how the budget level critically shapes the structure of the PPRA wealth.

### 5.4 SSD Problem: Various Utilities and Benchmark Quantiles

Based on the proposed algorithm, we further extend its applicability to a broader class of the SSD problem.
To assess the generality of our approach, we conduct numerical experiments using different utilities and benchmark quantiles Q0Q\_{0}.

For the utility function U​(x)U(x), we consider several representative forms capturing different risk preference, as shown in Table [5](https://arxiv.org/html/2512.00299v1#S5.T5 "Table 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |
| --- | --- | --- | --- |
|  | exponential | log | piecewise |
| U​(⋅)U(\cdot) | −1p​exp⁡(−p⋅x),x>0-\dfrac{1}{p}\exp(-p\cdot x),\;x>0 | log⁡(x),x>0\log(x),\;x>0 | {(x−1)p1,x⩾2−λ1​(1−x)q1,1⩽x<2xp2+C,0⩽x<1C−λ2​(−x)q2,−1⩽x<0\begin{cases}(x-1)^{p\_{1}},&x\geqslant 2\\ -\lambda\_{1}(1-x)^{q\_{1}},&1\leqslant x<2\\ x^{p\_{2}}+C,&0\leqslant x<1\\ C-\lambda\_{2}(-x)^{q\_{2}},&-1\leqslant x<0\end{cases} |

Table 5: Setting of various utilities.

For the benchmark quantile Q0Q\_{0}, we consider the following four cases, as shown in Table [6](https://arxiv.org/html/2512.00299v1#S5.T6 "Table 6 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | exponential | log-normal | normal | uniform |
| Q0​(⋅)Q\_{0}(\cdot) | −log⁡(1−t)α+k0-\dfrac{\log(1-t)}{\alpha}+k\_{0} | exp⁡(σ0⋅Φ−1​(t)+μ0)+k0\exp\left(\sigma\_{0}\cdot\Phi^{-1}(t)+\mu\_{0}\right)+k\_{0} | σ0⋅Φ−1​(t)+μ0\sigma\_{0}\cdot\Phi^{-1}(t)+\mu\_{0} | k​t+k0kt+k\_{0} |

Table 6: Benchmark quantiles Q0​(t)Q\_{0}(t), t∈(0,1)t\in(0,1).

The general settings coincide with the previous numerical examples and are given in Table [7](https://arxiv.org/html/2512.00299v1#S5.T7 "Table 7 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| rr | μS\mu\_{\text{S}} | σS\sigma\_{\text{S}} | θ\theta | TT | μ\mu | σ\sigma |
| 0.05 | 0.086 | 0.3 | 0.12 | 20 | -1.1440 | 0.5367 |

Table 7: General setting in Figures [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")-[5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

We investigate several combinations of the utilities and the benchmark quantiles. To illustrate the effectiveness of our proposed algorithm, we present the most representative cases under the parameter settings in Table [8](https://arxiv.org/html/2512.00299v1#S5.T8 "Table 8 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | utility | distribution of Q0Q\_{0} | x¯\overline{x} | parameters of Q0Q\_{0} | parameters of utility |
| (a) | exponential | uniform | 0.3 | k=1,k0=0k=1,k\_{0}=0 | p=0.6p=0.6 |
| (b) | exponential | exponential | 0.3 | α=1.5,k0=0\alpha=1.5,k\_{0}=0 | p=0.6p=0.6 |
| (c) | log | normal | 1.8 | μ0=5,σ0=1\mu\_{0}=5,\sigma\_{0}=1 | – |
| (d) | log | uniform | 1.4 | k=10,k0=0k=10,k\_{0}=0 | – |
| (e) | piecewise | log-normal | 3.5 | μ0=−1,σ0=3,k0=2.3\mu\_{0}=-1,\sigma\_{0}=3,k\_{0}=2.3 | |  | | --- | | p1=q1=0.6,p2=0.8,p\_{1}=q\_{1}=0.6,p\_{2}=0.8, | | q2=0.9,λ1=1,λ2=2q\_{2}=0.9,\lambda\_{1}=1,\lambda\_{2}=2 | |
| (f) | piecewise | exponential | 1.3 | α=0.7,k0=2.3\alpha=0.7,k\_{0}=2.3 | |  | | --- | | p1=q1=0.6,p2=0.8,p\_{1}=q\_{1}=0.6,p\_{2}=0.8, | | q2=0.9,λ1=1,λ2=2q\_{2}=0.9,\lambda\_{1}=1,\lambda\_{2}=2 | |

Table 8: Parameter setting in Figures [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")-[5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

Applying the Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), we obtain the numerical results in Table [9](https://arxiv.org/html/2512.00299v1#S5.T9 "Table 9 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") and plot Figures [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")-[5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), where each panel illustrates the structure of the correction function ysub​(⋅)y\_{\text{sub}}(\cdot) and the Poor-Performance-Region Algorithm (PPRA) solution.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | poor performance region CC | partition parameter | λ\lambda | λcla\lambda\_{\text{cla}} |
| (a) | (0.8803,1)(0.8803,1) | t1=1t\_{1}=1 | λ=1.5540\lambda=1.5540 | λcla=1.4429\lambda\_{\text{cla}}=1.4429 |
| (b) | (0.8904,1)(0.8904,1) | t1=1t\_{1}=1 | λ=1.5498\lambda=1.5498 | λcla=1.4429\lambda\_{\text{cla}}=1.4429 |
| (c) | (0.4608,1)(0.4608,1) | t1=1t\_{1}=1 | λ=0.6497\lambda=0.6497 | λcla=0.5556\lambda\_{\text{cla}}=0.5556 |
| (d) | (0.0426,0.7236)(0.0426,0.7236) | t1=0.1766t\_{1}=0.1766 | λ=0.8260\lambda=0.8260 | λcla=0.7143\lambda\_{\text{cla}}=0.7143 |
| (e) | (0,0.2419)∪(0.8930,1)(0,0.2419)\cup(0.8930,1) | t2=1,t1=0.0049t\_{2}=1,t\_{1}=0.0049 | λ=1.7002\lambda=1.7002 | λcla=0.9005\lambda\_{\text{cla}}=0.9005 |
| (f) | (0.3902,1)(0.3902,1) | t1=1t\_{1}=1 | λ=1.7930\lambda=1.7930 | λcla=1.5516\lambda\_{\text{cla}}=1.5516 |

Table 9: Numerical results in Figures [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")-[5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").



|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=189.88449pt]{exp2\_y.eps}&\includegraphics[width=212.02846pt,height=193.18452pt]{exp2\_Q.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=189.88449pt]{exp3\_y.eps}&\includegraphics[width=212.02846pt,height=193.18452pt]{exp3\_Q.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=189.88449pt]{log1\_y.eps}&\includegraphics[width=212.02846pt,height=193.18452pt]{log1\_Q.eps}\end{matrix} |  |

Figure 4: Setting (a)-(b)-(c).



|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=189.88449pt]{log2\_y.eps}&\includegraphics[width=212.02846pt,height=193.18452pt]{log2\_Q.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=189.88449pt]{hard3\_y.eps}&\includegraphics[width=212.02846pt,height=193.18452pt]{hard3\_Q.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=189.88449pt]{hard1\_y.eps}&\includegraphics[width=212.02846pt,height=193.18452pt]{hard1\_Q.eps}\end{matrix} |  |

Figure 5: Setting (d)-(e)-(f).

Later, we would clarify the structural behavior of the correction function ysub​(⋅)y\_{\text{sub}}(\cdot). The numerical experiments yield the following explanations and financial insights:

1. 1.

   Figure [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a)-(b)-(c): In bad market scenario, the correction function ysub​(⋅)y\_{\text{sub}}(\cdot) satisfies ysub​(⋅)=y0​(⋅)y\_{\text{sub}}(\cdot)=y\_{0}(\cdot), therefore, the PPRA wealth will coincide with the benchmark wealth. In this scenario, the benchmark serves as a risk-control mechanism, which is similar to Figure [2](https://arxiv.org/html/2512.00299v1#S5.F2 "Figure 2 ‣ 5.2 SSD Problem: Power Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a)-(b)-(d).
2. 2.

   Figure [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (c)-(f): Compared with Figure [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a)-(b), the region where ysub​(⋅)=y0​(⋅)y\_{\text{sub}}(\cdot)=y\_{0}(\cdot) expands. Hence, under relatively stagnant or bad market scenario, the PPRA wealth tends to coincide with the benchmark wealth. In such scenario, the SSD constraint plays a more prominent role by ensuring a benchmark wealth to reduce risk.
3. 3.

   Figure [5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (d): The correction function ysub​(⋅)=y0​(⋅)y\_{\text{sub}}(\cdot)=y\_{0}(\cdot) over certain intermediate intervals, causing the PPRA wealth to coincide with the benchmark in mid-range market scenario, as shown in (d)-Right.
4. 4.

   Figure [5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (e): The correction function ysub​(⋅)=y0​(⋅)y\_{\text{sub}}(\cdot)=y\_{0}(\cdot) at both endpoints of the interval (0,1)(0,1). This implies the PPRA wealth must coincide with the benchmark wealth in both extremely bad and exceptionally favorable market scenarios.

In Figure [5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (e), we can observe how Steps 8-12 of Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") ensure that the constructed function ysub​(⋅)y\_{\text{sub}}(\cdot) remains non-decreasing on (0,1)(0,1). The key idea is to modify the construction of gi​(t)g\_{i}(t) in Eq. ([19](https://arxiv.org/html/2512.00299v1#S4.E19 "In 4 ‣ Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) so that both monotonicity requirement of ysub​(⋅)y\_{\text{sub}}(\cdot) and the condition z∗​(⋅)⩽0z^{\*}(\cdot)\leqslant 0 is satisfied throughout the region in which ysub​(⋅)y\_{\text{sub}}(\cdot) is updated. In this example, the interval where ysub​(⋅)=ysub​(t1)y\_{\text{sub}}(\cdot)=y\_{\text{sub}}(t\_{1}) is extended into the region covered by the previous iteration (i.e., the first iteration), updating the original ysub​(⋅)y\_{\text{sub}}(\cdot) in this region.

Across various combinations of the utilities and the benchmark quantiles Q0Q\_{0}, we observe that the poor-performance region typically consists of one or two disjoint intervals. The proposed algorithm exhibits strong adaptability under these diverse settings, effectively identifying the sub-optimal solution in most cases. At the same time, our algorithm is able to handle certain special cases in which the original piecewise construction fails to guarantee monotonicity. By modifying the construction of gi​(t)g\_{i}(t), the algorithm provides a valid sub-optimal solution and, as a result, restores monotonicity and extends the applicability of our approach to more complex configurations.

## 6 Algorithm-Guided Piecewise-Neural-Network Framework

In this section, we propose a novel approach to solve the SSD Problem ([14](https://arxiv.org/html/2512.00299v1#S4.E14 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) by designing a piecewise-neural-network-framework combined with Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"). The key observation is that in Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), the poor performance region CC defined in Eq. ([27](https://arxiv.org/html/2512.00299v1#S4.E27 "In 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) and the construction of the correction function ysub​(⋅)y\_{\text{sub}}(\cdot) provide valuable structural information about the optimal solution, thereby guiding the design of an effective neural network framework.

We begin by applying Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), which yields a correction function ysub​(⋅)y\_{\text{sub}}(\cdot). Using ysub​(⋅)y\_{\text{sub}}(\cdot), we derive a sub-optimal solution Qsub​(⋅)Q\_{\text{sub}}(\cdot) as presented in Eq. ([24](https://arxiv.org/html/2512.00299v1#S4.E24 "In 14 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).
To design a neural network framework, the key idea is that we use the structure information of the derived Qsub​(⋅)Q\_{\text{sub}}(\cdot) to build a piecewise-neural-network framework. Then we apply this framework to train a solution for Problem ([14](https://arxiv.org/html/2512.00299v1#S4.E14 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

### 6.1 Model Setting

Algorithm 2  Algorithm-guided piecewise-neural-network framework for SSD Problem ([39](https://arxiv.org/html/2512.00299v1#S6.E39 "In 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"))

1:Implement Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") and get the sub-optimal solution structure as Eq. ([24](https://arxiv.org/html/2512.00299v1#S4.E24 "In 14 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")). Using the partition intervals (sk,sk+1](s\_{k},s\_{k+1}] defined in Eq. ([40](https://arxiv.org/html/2512.00299v1#S6.E40 "In 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), initialize the neural network architecture as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qθ​(s)\displaystyle Q\_{\theta}(s) | ={fθ0(0)​(𝐬feat​(s)),s∈(s0,s1],fθ1(1)​(𝐬feat​(s)),s∈(s1,s2],⋮fθK(K)​(𝐬feat​(s)),s∈(sK,sK+1),\displaystyle= |  | (34) |

where fθ(k)f^{(k)}\_{\theta} denotes the kk-th neural sub-network parameterized by θk\theta\_{k}, the parameters of the integrated network QQ are denoted as θ={θ0,θ1,…,θK}\theta=\{\theta\_{0},\theta\_{1},\dots,\theta\_{K}\}. 𝐬feat​(s)\mathbf{s}\_{\text{feat}}(s) represents the Fourier feature embedding of the scalar input ss defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐬feat​(s)=[sin⁡(2​π​s),sin⁡(4​π​s),cos⁡(2​π​s),cos⁡(4​π​s)]⊤∈ℝ4.\mathbf{s}\_{\text{feat}}(s)=[\,\sin(2\pi s),\;\sin(4\pi s),\;\cos(2\pi s),\;\cos(4\pi s)\,]^{\top}\in\mathbb{R}^{4}. |  | (35) |

2:Define a prior function as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(s)={I​(Qρ​(1−s)),s∈(s0,s1],Q0​(s),s∈(s1,s2],⋮I​(Qρ​(1−s)),s∈(sK,sK+1).\displaystyle\phi(s)= |  | (36) |

3:For each interval, update the sub-network output with the analytic prior term and activate the integrated network Qθ​(⋅)Q\_{\theta}(\cdot) as follows:

|  |  |  |
| --- | --- | --- |
|  | Qθ​(s)←Qθ​(s)+ϕ​(s),Qθ​(s)←ReLU​(Qθ​(s)).Q\_{\theta}(s)\leftarrow Q\_{\theta}(s)+\phi(s),\;\;Q\_{\theta}(s)\leftarrow\text{ReLU}(Q\_{\theta}(s)). |  |

4:Define the objective function as the expected utility from Eq. ([39](https://arxiv.org/html/2512.00299v1#S6.E39 "In 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).
Since the integral cannot be computed analytically, we approximate it by uniformly sampling nn points si∈(0,1)s\_{i}\in(0,1) and compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒobj​(θ)=1n​∑i=1nU​(Qθ​(si)).\mathcal{L}\_{\text{obj}}(\theta)=\frac{1}{n}\sum\_{i=1}^{n}U\big(Q\_{\theta}(s\_{i})\big). |  | (37) |

5:Take the budget constraint (C1C\_{1}) and SSD constraint (C2C\_{2}) as the penalty of the loss function. Define

|  |  |  |
| --- | --- | --- |
|  | C1=1n​∑i=1nQθ​(si)​Qρ​(1−si),C2=max⁡{0,maxk=1,…,n⁡[1n​∑i=1kQ0​(si)−1n​∑i=1kQθ​(si)]}.C\_{1}=\frac{1}{n}\sum\_{i=1}^{n}Q\_{\theta}(s\_{i})Q\_{\rho}(1-s\_{i}),\;\;C\_{2}=\max\left\{0,\max\_{k=1,\dots,n}\left[\frac{1}{n}\sum\_{i=1}^{k}Q\_{0}(s\_{i})-\frac{1}{n}\sum\_{i=1}^{k}Q\_{\theta}(s\_{i})\right]\right\}. |  |

6:Add weights w1,w2w\_{1},w\_{2} to C1,C2C\_{1},C\_{2} and calculate the loss function as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒp1=w1​(C1−x¯)2,ℒp2=w2⋅C2,\mathcal{L}\_{\text{p1}}=w\_{1}\,(C\_{1}-\bar{x})^{2},\;\;\mathcal{L}\_{\text{p2}}=w\_{2}\cdot C\_{2}, |  | (38) |

|  |  |  |
| --- | --- | --- |
|  | ℒtotal​(θ)=−ℒobj​(θ)+ℒp1+ℒp2.\mathcal{L}\_{\text{total}}(\theta)=-\mathcal{L}\_{\text{obj}}(\theta)+\mathcal{L}\_{\text{p1}}+\mathcal{L}\_{\text{p2}}. |  |

7:Next, start the training process.

8:Neural sub-networks {fθ(k)}k=0K\{f\_{\theta}^{(k)}\}\_{k=0}^{K}, pricing kernel function Qρ​(⋅)Q\_{\rho}(\cdot), benchmark function Q0​(⋅)Q\_{0}(\cdot), utility function U​(⋅)U(\cdot), budget x¯\bar{x}, sample size nn, learning rate η\eta, number of Adam steps AsA\_{s}, penalty weights w1,w2w\_{1},w\_{2}.

9:Trained network Qθ​(s)Q\_{\theta}(s).

10:Sample si∈(0,1)s\_{i}\in(0,1), i=1,…,ni=1,\dots,n.

11:Compute Fourier features 𝐬feat\mathbf{s}\_{\text{feat}} as Eq. ([35](https://arxiv.org/html/2512.00299v1#S6.E35 "In 1 ‣ Algorithm 2 ‣ 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

12:for k=0k=0 to KK do

13:  Initialize each sub-network: fθk(k)​(𝐬feat​(si))f\_{\theta\_{k}}^{(k)}(\mathbf{s}\_{\text{feat}}(s\_{i})).

14:  Compute analytic prior ϕ​(si)\phi(s\_{i}) as Eq. ([36](https://arxiv.org/html/2512.00299v1#S6.E36 "In 2 ‣ Algorithm 2 ‣ 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

15:end for

16:Merge the sub-networks to an integrated network Qθ​(s)Q\_{\theta}(s) as Eq. ([34](https://arxiv.org/html/2512.00299v1#S6.E34 "In 1 ‣ Algorithm 2 ‣ 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

17:Activate the network: Qθ​(s)←ReLU​(Qθ​(s))Q\_{\theta}(s)\leftarrow\text{ReLU}(Q\_{\theta}(s)).

18:for i=0i=0 to AsA\_{s} do

19:  Compute the objective function: ℒobj​(θ)=1n​∑i=1nU​(Qθ​(si))\mathcal{L}\_{\text{obj}}(\theta)=\frac{1}{n}\sum\_{i=1}^{n}U\big(Q\_{\theta}(s\_{i})\big).

20:  Compute constraint penalties ℒp1\mathcal{L}\_{\text{p1}} and ℒp2\mathcal{L}\_{\text{p2}} as Eq. ([38](https://arxiv.org/html/2512.00299v1#S6.E38 "In 6 ‣ Algorithm 2 ‣ 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

21:  Compute the total loss in current iteration: ℒtotal​(θ)=−ℒobj​(θ)+ℒp1+ℒp2\mathcal{L}\_{\text{total}}(\theta)=-\mathcal{L}\_{\text{obj}}(\theta)+\mathcal{L}\_{\text{p1}}+\mathcal{L}\_{\text{p2}}.

22:  Adam update: θ←θ−η​∇θℒtotal​(θ)\theta\leftarrow\theta-\eta\nabla\_{\theta}\mathcal{L}\_{\text{total}}(\theta).

23:end for

24:return Trained network Qθ​(s)Q\_{\theta}(s).

The optimization problem to be approximated by the neural network is formulated as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | maxQ∈𝒬2​(Q0)​∫01U​(Q​(s))​ds​s.t. ​∫01Q​(s)​Qρ​(1−s)​ds⩽x¯,\displaystyle\max\_{Q\in\mathcal{Q}\_{2}(Q\_{0})}\int\_{0}^{1}U(Q(s))\mathrm{d}s~~\text{s.t. }\int\_{0}^{1}Q(s)Q\_{\rho}(1-s)\mathrm{d}s\leqslant\overline{x}, |  | (39) |

which is identical to Problem ([15](https://arxiv.org/html/2512.00299v1#S4.E15 "In 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).

Based on Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), we obtain the suboptimal solution Qsub​(⋅)Q\_{\text{sub}}(\cdot) as given in Eq. ([24](https://arxiv.org/html/2512.00299v1#S4.E24 "In 14 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")), which exhibits a piecewise structure. Specifically, Qsub​(⋅)Q\_{\text{sub}}(\cdot) can be expressed as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qsub​(s)\displaystyle Q\_{\text{sub}}(s) | ={I(λ(Qρ(1−s)−y(⋅)),s∈(s0,s1],Q0​(s),s∈(s1,s2],⋮I(λ(Qρ(1−s)−y(⋅)),s∈(sK,sK+1),\displaystyle= |  | (40) |

where s0=0,sK+1=1.s\_{0}=0,s\_{K+1}=1.

Following this structure, we construct a set of neural sub-networks
{fθk(k)}k=0K\{f^{(k)}\_{\theta\_{k}}\}\_{k=0}^{K} to approximate each interval respectively. The main design considerations are summarized as follows:

1. a

   In Step 1, the piecewise formulation ensures that Qθ​(s)Q\_{\theta}(s) inherits the partition interval of Qsub​(⋅)Q\_{\text{sub}}(\cdot), enabling the network to better capture the structural behavior of the optimal solution. Specifically, each sub-network fθk(k)f^{(k)}\_{\theta\_{k}} is a fully connected feedforward network with 8 hidden layers, each consisting of 256 neurons with Tanh activations.
2. b

   In Step 2, we introduce an analytical prior term into each sub-network fθk(k)f\_{\theta\_{k}}^{(k)}. The design of ϕ​(s)\phi(s) is inspired by the structure of Qsub​(⋅)Q\_{\text{sub}}(\cdot), preserving essential information from the solution of Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") as a prior function and helps the network to capture the intrinsic information of the optimal solution.
3. c

   In Steps 5-6, we square the violation of the budget constraint to represent its penalty, ensuring the budget stays close to x¯\overline{x}.
   For the SSD constraint, we penalize the maximal violation to strictly enforce its satisfaction. The relative importance of satisfying the constraint during training can be adjusted by tuning its associated weight w1,w2w\_{1},w\_{2}.
4. d

   In Steps 8-22, the approximation accuracy of the objective function and constraints can be improved by increasing the number of sampled points nn. The Adam optimizer is used to update the network parameters, and the number of Adam steps AsA\_{s} determines how many gradient-based updates are performed during training, thus controlling the convergence of the network.

### 6.2 Experimental Results

To validate the model, we first conduct experiments under conditions in which the optimal solution Q∗​(⋅)Q^{\*}(\cdot) is available. The optimality is because Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") results numerically satisfy the characterization in Theorem [2](https://arxiv.org/html/2512.00299v1#Thmtheorem2 "Theorem 2 (Theorem 5.10 of Wang and Xia (2021)). ‣ 4.1 SSD Problem under Non-concavity: Analytical Difficulty ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"). We follow the setup in Section [5.4](https://arxiv.org/html/2512.00299v1#S5.SS4 "5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), which considers both the exponential utility and log utility under a linear SSD constraint quantile Q0Q\_{0} (Table [8](https://arxiv.org/html/2512.00299v1#S5.T8 "Table 8 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a)(c)).

We follow the steps in Algorithm [2](https://arxiv.org/html/2512.00299v1#alg2 "Algorithm 2 ‣ 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") to get a trained neural network QθQ\_{\theta}, and the results are summarized in Table [10](https://arxiv.org/html/2512.00299v1#S6.T10 "Table 10 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | utility | distribution of Q0Q\_{0} | optimal value | neural network value |
| (i) | exponential | uniform | -0.8965 | -0.8990 |
| (ii) | log | uniform | 1.4781 | 1.4686 |

Table 10: Objective value for neural network approximation.



|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=204.63057pt]{nn\_graphs/nn\_exp\_Q.eps}&\includegraphics[width=212.02846pt,height=204.63057pt]{nn\_graphs/nn\_exp\_obj.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=204.63057pt]{nn\_graphs/nn\_log\_Q.eps}&\includegraphics[width=212.02846pt,height=204.63057pt]{nn\_graphs/nn\_log\_obj.eps}\end{matrix} |  |

Figure 6: Neural network approximation results.

Here are some illustrations of the neural network results:

1. 1.

   Figure [6](https://arxiv.org/html/2512.00299v1#S6.F6 "Figure 6 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (i)-(ii) Left: Compared with Figure [4](https://arxiv.org/html/2512.00299v1#S5.F4 "Figure 4 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (a) and Figure [5](https://arxiv.org/html/2512.00299v1#S5.F5 "Figure 5 ‣ 5.4 SSD Problem: Various Utilities and Benchmark Quantiles ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (d), the algorithm-guided piecewise-neural-network framework successfully preserves the structure features of the optimal solution, achieving a close match.
2. 2.

   Convergence behavior: The network typically converges within 100-2000 steps. As shown in Table [10](https://arxiv.org/html/2512.00299v1#S6.T10 "Table 10 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"), our algorithm achieves high numerical accuracy relative to the optimal solution, which is reflected in the objective value ∫01U​(Q​(s))​ds\int\_{0}^{1}U(Q(s))\mathrm{d}s in Problem ([39](https://arxiv.org/html/2512.00299v1#S6.E39 "In 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")).
3. 3.

   Figure [6](https://arxiv.org/html/2512.00299v1#S6.F6 "Figure 6 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (i)-(ii) Right: The convergence speed depends on the number of sub-networks: the exponential case uses 2 sub-networks, while the log case uses 3, which also reflects the problem complexity. In simpler cases (Figure [6](https://arxiv.org/html/2512.00299v1#S6.F6 "Figure 6 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (i)), the convergence curves are smooth and rapid because the two constraints in Problem ([39](https://arxiv.org/html/2512.00299v1#S6.E39 "In 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")) are quickly satisfied. In more complex cases (Figure [6](https://arxiv.org/html/2512.00299v1#S6.F6 "Figure 6 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (ii)), the network spends more time mitigating constraint penalties, resulting in slower convergence.

Here we come to the conclusion that our approach, first deriving a sub-optimal solution via the proposed algorithm and then leveraging it to guide the neural network design, effectively captures the essential properties of the optimal solution and provides stable, high-quality performance for the SSD problem.

Extending to non-concave utility functions introduces a substantially more challenging problem. The difficulty stems from several factors. First, the optimization is infinite-dimensional over the space of admissible allocation functions, meaning that the solution is a functional rather than a finite-dimensional vector. Second, in the presence of SSD constraint and budget constraint, the feasible set becomes highly restricted and non-convex, which further complicates convergence.

Remarkably, our algorithm-guided piecewise-neural-network framework remains stable under these challenging conditions and achieves rapid convergence. By leveraging sub-optimal solutions obtained from our proposed Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") as analytic priors and structuring the network in a piecewise manner, the framework effectively reduces the functional search space and guides the optimization toward regions that respect the SSD constraints. In contrast, a standard monolithic-neural-network (non-piecewise) framework exhibits substantially slower convergence, often requiring tens of times more training steps to reach convergence.

To illustrate this, we consider an S-shaped utility following the setup in Section [5.3](https://arxiv.org/html/2512.00299v1#S5.SS3 "5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (Table [4](https://arxiv.org/html/2512.00299v1#S5.T4 "Table 4 ‣ 5.3 SSD Problem: S-shaped Utility ‣ 5 Numerical Results ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (b)). Solutions obtained with our Algorithm [2](https://arxiv.org/html/2512.00299v1#alg2 "Algorithm 2 ‣ 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") are compared against those from a standard monolithic-neural-network framework using identical parameter settings.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | network | neural network value | C1C\_{1} satisfied steps | C2C\_{2} satisfied steps |
| (i) | piecewise | 14.7531 | 83 | 10 |
| (ii) | standard | 12.0320 | 10950 | 4279 |

Table 11: Convergence step and constraint satisfied step.



|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=198.03316pt]{nn\_graphs/convergence\_graph\_prior.eps}&\includegraphics[width=212.02846pt,height=198.03316pt]{nn\_graphs/prior\_penalty.eps}\end{matrix} |  |

|  |  |  |
| --- | --- | --- |
|  | Refer to captionRefer to caption\displaystyle\tiny\begin{matrix}\includegraphics[width=212.02846pt,height=198.03316pt]{nn\_graphs/convergence\_graph\_naive.eps}&\includegraphics[width=212.02846pt,height=194.72942pt]{nn\_graphs/naive\_penalty.eps}\end{matrix} |  |

Figure 7: Convergence behavior and penalty updates.

Here, we illustrate the convergence behavior of different neural network designs:

1. 1.

   Table [11](https://arxiv.org/html/2512.00299v1#S6.T11 "Table 11 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"): The neural network value corresponds to the objective value ∫01U​(Q​(s))​ds\int\_{0}^{1}U(Q(s))\,\mathrm{d}s in Problem ([39](https://arxiv.org/html/2512.00299v1#S6.E39 "In 6.1 Model Setting ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network")). The table also reports the minimum number of steps required to satisfy the SSD and budget constraints for each network design.
2. 2.

   Figure [7](https://arxiv.org/html/2512.00299v1#S6.F7 "Figure 7 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network"): Our algorithm-guided piecewise-neural-network framework reaches near-convergence in roughly 300 Adam steps, whereas a standard monolithic-neural-network requires approximately 10,000 steps to achieve comparable near-convergence. This dramatic acceleration highlights the efficiency of our approach. Furthermore, our piecewise framework achieves a higher sub-optimal objective value compared with the standard framework, indicating that the standard framework is prone to getting trapped in local optima, while our piecewise framework can avoid such traps and attain superior performance.
3. 3.

   Table [11](https://arxiv.org/html/2512.00299v1#S6.T11 "Table 11 ‣ 6.2 Experimental Results ‣ 6 Algorithm-Guided Piecewise-Neural-Network Framework ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") (i) vs. (ii): The significant speedup under the piecewise framework primarily stems from rapid satisfaction of the penalty terms. By incorporating analytic prior inspired from Algorithm [1](https://arxiv.org/html/2512.00299v1#alg1 "Algorithm 1 ‣ 4.2 SSD Problem: Numerical Algorithm ‣ 4 SSD Problem ‣ Stochastic Dominance Constrained Optimization with S-shaped Utilities: Poor-Performance-Region Algorithm and Neural Network") into the network design, our piecewise framework enforces the SSD and budget constraints more efficiently, allowing the neural network to converge quickly while maintaining better approximation of the sub-optimal solution.

In summary, our study demonstrates the effectiveness of the algorithm-guided piecewise-neural-network framework for solving the SSD problem.
For cases where an analytical optimal solution exists, our framework achieves results that closely match the optimal solution both numerically and structurally, indicating its high precision.
From the perspective of convergence, our framework significantly accelerates the optimization process and is capable of escaping local optima, thereby attaining superior objective value compared with the standard monolithic-neural-network framework.
These findings highlight the efficiency and robustness of our approach across different problem settings, and suggest strong potential for extension to more complex scenarios.

## 7 Conclusion

We study a utility maximization problem under stochastic dominance constraints. Starting from an S-shaped utility function, we derive the explicit optimal solution without a liquidation boundary under first-order stochastic dominance (FSD) constraints.
For the more challenging SSD problem, particularly under non-concavity, obtaining an explicit optimal solution is inherently difficult. Motivated by the structural properties of the analytical theorem in the concave case, we introduce a Poor-Performance-Region Algorithm (PPRA). This algorithm efficiently identifies the candidate structure that a potential optimal solution should satisfy and proves effective in the vast majority of cases. In addition, extensive numerical experiments illustrate how the algorithm operates, confirm its broad applicability, and demonstrate its capability to handle the few exceptional cases.

Building on the structural insights provided by the PPRA, we further recognize the potential of neural networks in tackling SSD problems under non-concavity. While neural networks offer strong approximation capabilities, their direct application often suffers from slow convergence and severe sensitivity to local optima induced by non-concavity. By leveraging the PPRA’s ability to capture the essential structure of the optimal solution, we develop an algorithm-guided piecewise-neural-network framework that integrates these structural cues into the learning process. Compared with a standard neural-network approach, this framework achieves significantly faster convergence and effectively avoids undesirable local minima, thereby delivering consistently superior solution quality.

#### Acknowledgement

The authors are grateful to Jianming Xia and members of the research group on financial mathematics and risk management at The Chinese University of Hong Kong, Shenzhen for their insightful discussions and conversations.
Y. Liu acknowledges financial support from the National Natural Science Foundation of China (Grant No. 12401624), The Chinese University of Hong Kong (Shenzhen) University Development Fund (Grant No. UDF01003336) and Shenzhen Science and Technology Program (Grant No. RCBS20231211090814028, JCYJ20250604141203005, 2025TC0010) and is partly supported by the Guangdong Provincial Key Laboratory of Mathematical Foundations for Artificial Intelligence (Grant No. 2023B1212010001).

## References

* Barberis and Thaler (2003)
   Barberis, N., Thaler, R. (2003). A Survey of Behavioral Finance, in Handbook of the Economics of Finance: Vol. 1. Financial Markets and Asset Pricing, M. H. G. M. Constantinides, and R. Stulz, eds., Elsevier, Kidlington, 1053-1128.
* Carpenter (2000)
   Carpenter, J. N. (2000). Does option compensation increase managerial risk appetite? Journal of Finance, 55, 2311-2331.
* Föllmer and Schied (2016)
   Föllmer, H., Schied, A. (2016). *Stochastic Finance. An Introduction in Discrete Time*. Fourth Edition. Walter de Gruyter, Berlin.
* Ghossoub and Zhu (2025)
   Ghossoub, M., Zhu, M. B. (2025). Risk-constrained portfolio choice under rank-dependent utility. Finance and Stochastics, 29, 399-442.
* He and Kou (2018)

  He, X., Kou, S. (2018). Profit sharing in hedge funds. Mathematical Finance, 28, 50-81.
* He and Zhou (2011)
   He, X., Zhou, X. (2011). Portfolio choice under cumulative prospect theory: An analytical treatment. Management Science, 57, 315-331.
* Karatzas et al. (1987)
   Karatzas, I., Lehoczky, J. P., Shreve, S. E. (1987). Optimal portfolio and consumption decisions for a “small investor” on a finite horizon. SIAM Journal on Control and Optimization, 25, 1557-1586.
* Karatzas and Shreve (1998)
   Karatzas, I., Shreve, S. E. (1998). Methods of Mathematical Finance. Springer, New York.
* Kahneman and Tversky (1979)
   Kahneman, D., Tversky, A. (1979). Prospect Theory: an analysis of decision under risk. Econometrica, 47, 263-291.
* Liang and Liu (2020)
   Liang, Z., Liu, Y. (2020). A classification approach to general S-shaped utility optimization with principals’ constraints.
  SIAM Journal on Control and Optimization, 58, 3734-3762.
* Liang and Liu (2024)
   Liang, Z., Liu, Y. (2024). An asymptotic approach to centrally planned portfolio selection. Advances in Applied Probability, 56, 757-784.
* Liang, Liu and Zhang (2025)
   Liang, Z., Liu, Y., Zhang, L. (2025). A framework of state-dependent utility optimization with general benchmarks. Finance and Stochastics, 29, 469-518.
* Merton (1969)
   Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous-time case. The Review of Economics and Statistics, 51, 247-257.
* Rockafellar (1970)
   Rockafellar, R. T. (1970). Convex Analysis. Princeton University Press, 1st edition.
* Scarselli and Tsoi (1998)
   Scarselli, F., Tsoi, A. C. (1998). Universal approximation using feedforward neural networks: A survey of some existing methods, and some new results. Neural Networks, 11(1), 15-37.
* Tversky and Kahneman (1992)
  Tversky, A., Kahneman, D. (1992). Advances in prospect theory: cumulative representation of uncertainty. Journal of Risk and Uncertainty, 5, 297-323.
* Wang, Wei and Xia (2024)
   Wang, Y., Wei, J., Xia, J. (2024). Mean-Stochastic-Dominance portfolio selection in continuous time. SIAM Journal on Financial Mathematics, 15, SC80-SC90.
* Wang and Xia (2021)
   Wang, X., Xia, J. (2021). Expected utility maximization with stochastic dominance constraints in complete markets. SIAM Journal on Financial Mathematics, 12, 1054-1111.
* Wei (2018)
   Wei, P. (2018). Risk management with weighted VaR. Mathematical Finance, 28, 1020-1060.
* Xia and Zhou (2016)
   Xia, J., Zhou, X. (2016). Arrow-Debreu equilibria for rank-dependent utilities. Mathematical Finance, 26, 558-588.
* Xu (2016)
   Xu, Z. (2016). A note on the quantile formulation. Mathematical Finance, 26, 589-601.
* Zhang et al. (2018)
   Zhang, L., Wang, F., Sun, T., Xu, B. (2018). A constrained optimization method based on BP neural network. Neural Computing and Applications, 29(2), 413-421.