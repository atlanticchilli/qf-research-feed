---
authors:
- Riccardo Gozzo
doc_id: arxiv:2510.23461v1
family_id: arxiv:2510.23461
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Adaptive Multilevel Splitting: First Application to Rare-Event Derivative
  Pricing'
url_abs: http://arxiv.org/abs/2510.23461v1
url_html: https://arxiv.org/html/2510.23461v1
venue: arXiv q-fin
version: 1
year: 2025
---


Riccardo Gozzo
PhD Student, Scuola Normale Superiore, Pisa. Work conducted while at University of Milano-Bicocca.

###### Abstract

This work analyzes the computational burden of pricing binary options in rare-event settings and introduces an adaptation of the adaptive multilevel splitting (AMS) method for financial derivatives. Standard Monte Carlo is inefficient for deep out of the money binaries due to discontinuous payoffs and low exercise probabilities, requiring very large samples for accurate estimates. An AMS scheme is developed for binary options under Black–Scholes and Heston dynamics, reformulating the rare-event problem as a sequence of conditional events. Numerical experiments compare the method to Monte Carlo and to other techniques such as antithetic variables and multilevel Monte Carlo (MLMC) across four contracts: European digital calls and puts, and Asian digital calls and puts. Results show up to a 200-fold computational gain for deep out-of-the-money cases while preserving unbiasedness. No evidence is found of prior applications of AMS to financial derivatives. The approach improves pricing efficiency for rare-event contracts such as parametric insurance and catastrophe linked securities. An open-source Rcpp implementation is provided, supporting multiple discretizations and importance functions.

Keywords: adaptive multilevel splitting; binary options; monte carlo simulation; rare event simulation; variance reduction

## 1 Introduction

The accurate and efficient pricing of financial derivatives is increasingly critical in modern markets, where advanced numerical methods are required for complex instruments [[1](https://arxiv.org/html/2510.23461v1#bib.bib1)]. The computational challenges of rare-event simulation extend beyond academic interest, creating bottlenecks that affect market functionality. Inaccurate pricing of low-probability events limits the ability of market makers to provide competitive quotes, reducing liquidity for these instruments [[2](https://arxiv.org/html/2510.23461v1#bib.bib2)]. This difficulty is pronounced in the insurance sector, where parametric products depend on binary triggers linked to observable parameters such as earthquake magnitude or wind speed [[3](https://arxiv.org/html/2510.23461v1#bib.bib3), [4](https://arxiv.org/html/2510.23461v1#bib.bib4)]. Computational limitations restrict coverage of catastrophic risks and constrain the development of innovative risk-transfer mechanisms in financial and insurance markets.

These challenges are evident in binary options, which share structural similarities with parametric insurance through trigger-based payoffs. Their discontinuous structure pays a fixed amount if the underlying asset crosses a predetermined barrier at expiration and zero otherwise [[5](https://arxiv.org/html/2510.23461v1#bib.bib5), [6](https://arxiv.org/html/2510.23461v1#bib.bib6)]. This all-or-nothing feature makes pricing highly sensitive to the probability of rare events, particularly for deep out-of-the-money contracts where accurate tail estimation is critical.

Addressing these difficulties naturally leads to simulation-based techniques. Monte Carlo methods are widely used for pricing complex derivatives due to their flexibility in high-dimensional settings [[7](https://arxiv.org/html/2510.23461v1#bib.bib7)]. The convergence rate of O​(N−1/2)O(N^{-1/2}) creates a computational bottleneck, especially for binary options with low exercise probabilities. Reliable estimation in such cases typically requires millions of paths, rendering crude Monte Carlo impractical [[8](https://arxiv.org/html/2510.23461v1#bib.bib8), [9](https://arxiv.org/html/2510.23461v1#bib.bib9)].

Classical variance-reduction techniques attempt to address these challenges. Antithetic variates reduce variance through negative correlation between paired samples [[10](https://arxiv.org/html/2510.23461v1#bib.bib10), [7](https://arxiv.org/html/2510.23461v1#bib.bib7)], but the theoretical gain is bounded by a factor of two [[11](https://arxiv.org/html/2510.23461v1#bib.bib11)]. Control variates can be more effective but require auxiliary variables that are both analytically tractable and highly correlated with the target payoff [[12](https://arxiv.org/html/2510.23461v1#bib.bib12)]. For discontinuous payoffs such as binary options, such variables are difficult to construct, limiting applicability.

More advanced methods have been developed. Importance sampling modifies the probability measure to increase the frequency of rare outcomes and applies likelihood-ratio weighting to remove bias [[7](https://arxiv.org/html/2510.23461v1#bib.bib7), [13](https://arxiv.org/html/2510.23461v1#bib.bib13)]. Its effectiveness depends on the design of suitable distributions, which is problem-specific and difficult to generalize [[14](https://arxiv.org/html/2510.23461v1#bib.bib14)]. Another prominent approach is multilevel Monte carlo (MLMC), which reduces complexity by combining simulations on coarse and fine discretizations [[15](https://arxiv.org/html/2510.23461v1#bib.bib15), [16](https://arxiv.org/html/2510.23461v1#bib.bib16)]. While efficient for path-dependent derivatives, MLMC is not tailored to extreme-event pricing, focusing instead on reducing overall cost.

Recent research combines these techniques to overcome individual limitations. Hybrid methods integrate MLMC with importance sampling to improve efficiency while concentrating sampling in critical regions [[17](https://arxiv.org/html/2510.23461v1#bib.bib17), [18](https://arxiv.org/html/2510.23461v1#bib.bib18)]. Machine learning further enhances importance sampling, with neural networks learning tilting parameters [[19](https://arxiv.org/html/2510.23461v1#bib.bib19)] and tensor-train decompositions enabling high-dimensional distribution approximation [[20](https://arxiv.org/html/2510.23461v1#bib.bib20)].

This work addresses the computational challenges of binary option pricing by applying the adaptive multilevel splitting (AMS) method [[21](https://arxiv.org/html/2510.23461v1#bib.bib21)]. AMS extends classical splitting techniques for rare-event simulation [[22](https://arxiv.org/html/2510.23461v1#bib.bib22)] and builds on the foundations of sequential Monte Carlo [[23](https://arxiv.org/html/2510.23461v1#bib.bib23)]. Originally developed in reliability analysis and statistical physics [[24](https://arxiv.org/html/2510.23461v1#bib.bib24), [25](https://arxiv.org/html/2510.23461v1#bib.bib25), [26](https://arxiv.org/html/2510.23461v1#bib.bib26), [27](https://arxiv.org/html/2510.23461v1#bib.bib27)], AMS decomposes a rare event into a sequence of more frequent conditional events, transforming a single intractable estimation into multiple tractable subproblems. Although AMS has achieved strong results in other scientific domains, no prior applications are documented in financial derivatives pricing. Recent advances provide theoretical guarantees of unbiasedness and convergence [[28](https://arxiv.org/html/2510.23461v1#bib.bib28), [29](https://arxiv.org/html/2510.23461v1#bib.bib29), [30](https://arxiv.org/html/2510.23461v1#bib.bib30)], creating the basis for its use in finance.

The contributions of this study are fourfold. First, an AMS adaptation is introduced for binary option pricing under Black–Scholes and Heston dynamics [[31](https://arxiv.org/html/2510.23461v1#bib.bib31), [32](https://arxiv.org/html/2510.23461v1#bib.bib32)], addressing the specific challenges of risk-neutral valuation and financial time series. Second, the sensitivity of the estimator to parameter choices, including the number of trajectories and resampling rates, is analyzed. Third, numerical experiments compare AMS to standard Monte Carlo, showing substantial gains for deep out-of-the-money options. Fourth, an open-source Rcpp implementation is released, supporting Euler, Milstein, and Andersen discretizations [[33](https://arxiv.org/html/2510.23461v1#bib.bib33), [34](https://arxiv.org/html/2510.23461v1#bib.bib34), [35](https://arxiv.org/html/2510.23461v1#bib.bib35)], two importance functions, and six binary option variants, offering a flexible toolkit for rare-event simulation in derivatives pricing.

The paper is structured as follows. Section 2 reviews the background on SDE discretization, binary option pricing, and AMS methodology. Section 3 presents the limits of classical variance-reduction techniques. Section 4 illustrates the adapted AMS algorithm, establishes its theoretical properties, details the numerical implementation, and reports results against benchmark approaches. Section 5 concludes with a summary of findings and directions for future research.

## 2 Research methodology

### 2.1 Stochastic differential equation models

Numerical experiments are conducted under two standard models for asset price dynamics: the Black–Scholes model [[31](https://arxiv.org/html/2510.23461v1#bib.bib31)] and the Heston model [[32](https://arxiv.org/html/2510.23461v1#bib.bib32)]. These frameworks allow assessment of the robustness of the AMS approach across different model complexities.

For the Black–Scholes case the exact solution, obtained via logarithmic transformation, removes discretization error [[36](https://arxiv.org/html/2510.23461v1#bib.bib36), [7](https://arxiv.org/html/2510.23461v1#bib.bib7)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sk+1=Sk​exp⁡[(r−σ22)​Δ​t+σ​Δ​Wk].S\_{k+1}=S\_{k}\exp\left[\left(r-\tfrac{\sigma^{2}}{2}\right)\Delta t+\sigma\Delta W\_{k}\right]. |  | (1) |

For the Heston model the variance process requires a scheme that preserves positivity and avoids bias. The quadratic–exponential (QE) method of Andersen [[35](https://arxiv.org/html/2510.23461v1#bib.bib35)] is employed, the standard approach for accurate Heston simulation. It matches the first two conditional moments of Vt+Δ​t|VtV\_{t+\Delta t}\,|\,V\_{t} and selects the update regime according to

|  |  |  |
| --- | --- | --- |
|  | ψ≤ψc:Vt+Δ​t=a​(b+Z)2,Z∼𝒩​(0,1),\psi\leq\psi\_{c}:\quad V\_{t+\Delta t}=a(b+Z)^{2},\qquad Z\sim\mathcal{N}(0,1), |  |

|  |  |  |
| --- | --- | --- |
|  | ψ>ψc:Vt+Δ​t={0with probability ​p=ψ−1ψ+1,β−1​log⁡(1−p1−U)with probability ​1−p,\psi>\psi\_{c}:\quad V\_{t+\Delta t}=\begin{cases}0&\text{with probability }p=\dfrac{\psi-1}{\psi+1},\\[4.0pt] \beta^{-1}\log\!\left(\dfrac{1-p}{1-U}\right)&\text{with probability }1-p,\end{cases} |  |

where U∼Uniform​(0,1)U\sim\text{Uniform}(0,1) and β=(1−p)/m\beta=(1-p)/m.

The asset price is then updated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+Δ​t=St​exp⁡[r​Δ​t+K0+K1​Vt+K2​Vt+Δ​t+K3​Vt+K4​Vt+Δ​t​ϵ],S\_{t+\Delta t}=S\_{t}\exp\!\left[r\Delta t+K\_{0}+K\_{1}V\_{t}+K\_{2}V\_{t+\Delta t}+\sqrt{K\_{3}V\_{t}+K\_{4}V\_{t+\Delta t}}\;\epsilon\right], |  | (2) |

with ϵ∼𝒩​(0,1)\epsilon\sim\mathcal{N}(0,1). The coefficients {K0,…,K4}\{K\_{0},\dots,K\_{4}\} and the parameters aa, bb, and ψ\psi are given explicitly in [[35](https://arxiv.org/html/2510.23461v1#bib.bib35)].

This construction preserves the positivity of variance and yields accurate joint dynamics, making it the reference scheme for Heston simulations in rare-event pricing.

### 2.2 Binary option pricing

Binary options are derivatives with discontinuous payoffs that depend on whether the underlying asset satisfies specific conditions. Four contracts are considered:

* •

  digital call: Payoff=𝟏{ST>K}\;\text{Payoff}=\mathbf{1}\_{\{S\_{T}>K\}}
* •

  digital put: Payoff=𝟏{ST<K}\;\text{Payoff}=\mathbf{1}\_{\{S\_{T}<K\}}
* •

  asian digital call: Payoff=𝟏{1m​∑t=1mSt>K}\;\text{Payoff}=\mathbf{1}\_{\left\{\tfrac{1}{m}\sum\_{t=1}^{m}S\_{t}>K\right\}}
* •

  asian digital put: Payoff=𝟏{1m​∑t=1mSt<K}\;\text{Payoff}=\mathbf{1}\_{\left\{\tfrac{1}{m}\sum\_{t=1}^{m}S\_{t}<K\right\}}

The discontinuous structure makes pricing sensitive to small path variations and generates high variance in standard Monte Carlo estimates. Computational difficulties intensify for rare-event regimes, such as deep out of the money contracts, where the target probability ℙ​(A)\mathbb{P}(A) is very small and required sample sizes grow inversely with its magnitude. In these settings, crude Monte Carlo becomes impractical. Binary options are therefore an effective test case for adaptive multilevel splitting: not only do they reallocate computational effort toward trajectories likely to activate the payoff condition, but their payoff naturally corresponds to the estimation of a probability, making AMS directly and rigorously applicable.

### 2.3 Adaptive multilevel splitting (AMS)

Adaptive multilevel splitting (AMS) [[21](https://arxiv.org/html/2510.23461v1#bib.bib21), [24](https://arxiv.org/html/2510.23461v1#bib.bib24)] is a variance reduction method for estimating the probability of rare events by decomposing the target set into a sequence of more probable intermediate events. Instead of brute force sampling, AMS focuses computation on trajectories that are likely to reach the rare-event region.
  
The idea can be illustrated with a random walk that must reach a high threshold LmaxL\_{\max}. Rather than simulating many independent paths and counting those that succeed, AMS repeatedly removes poorly performing trajectories and replicates those that progress toward the target.

![Refer to caption](AMS.png)


Figure 1: Illustration of the first two iterations of the AMS algorithm, where at each iteration the current threshold is L=3L=3 and the worst-performing trajectory (i.e., the one with the lowest maximum) is discarded (K=1K=1); a better-performing trajectory is cloned and resimulated from the time it first crossed LL [[24](https://arxiv.org/html/2510.23461v1#bib.bib24)]

Algorithm description:
Given a Markov process {Xt}t≥0\{X\_{t}\}\_{t\geq 0} with initial distribution η0\eta\_{0}, the goal is to estimate the rare-event probability p=ℙ​(Xτ∈D),p=\mathbb{P}(X\_{\tau}\in D),
where τ\tau is a stopping time and DD is the rare set.
Adaptive multilevel splitting requires three key ingredients expressed here in a single narrative.

First, an importance function ξ:ℝd→ℝ\xi:\mathbb{R}^{d}\to\mathbb{R} measures progress toward DD.
Theorem 3.2 of [[28](https://arxiv.org/html/2510.23461v1#bib.bib28)] shows that unbiasedness holds under the relaxed condition
x∈D⟹ξ​(x)≥Lmaxx\in D\implies\xi(x)\geq L\_{\max}, without the stricter equivalence
ξ​(x)≥Lmax⇔x∈D\xi(x)\geq L\_{\max}\iff x\in D.
This weaker requirement is useful in financial applications, although the closer ξ\xi aligns with DD the lower the estimator variance.

Second, the algorithm fixes a sample size nn and a discard parameter kk with 1≤k<n1\leq k<n.
Choosing 1≤k≤n/21\leq k\leq n/2 in practice maintains diversity of the trajectories.

Third, the importance of an entire trajectory X=(Xt)t∈[0,τf]X=(X\_{t})\_{t\in[0,\tau\_{f}]} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X)=supt∈[0,τf]ξ​(Xt).I(X)=\sup\_{t\in[0,\tau\_{f}]}\xi(X\_{t}). |  | (3) |

The algorithm starts with nn i.i.d. replicas of the Markov chain Xj0=(Xj,t0)t∈ℕX^{0}\_{j}=(X^{0}\_{j,t})\_{t\in\mathbb{N}}, j=1,…,nj=1,\dots,n, initialized outside DD.
At each iteration:

1. 1.

   Compute Sj=I​(Xj)S^{j}=I(X^{j}) for all replicas.
2. 2.

   Sort {Sj}\{S^{j}\} and set Z=S(k)Z=S^{(k)}, the kk-th order statistic.
3. 3.

   If Z≥LmaxZ\geq L\_{\max} or all SjS^{j} are equal, terminate.
4. 4.

   Discard the kk trajectories with Sj≤ZS^{j}\leq Z and replace them by clones of survivors X(i)X^{(i)}, i>ki>k, restarted from the first crossing time of ZZ and resimulated forward. Randomized cloning preserves unbiasedness.
5. 5.

   Update the common weight W←n−kn​WW\leftarrow\tfrac{n-k}{n}W, with W0=1W\_{0}=1.

After QQ iterations the probability estimator is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^AMS=W⋅1n​∑j=1n𝟏{Xj∈D},\hat{p}\_{\mathrm{AMS}}=W\cdot\frac{1}{n}\sum\_{j=1}^{n}\mathbf{1}\_{\{X^{j}\in D\}}, |  | (4) |

which is unbiased for any admissible importance function ξ\xi, and whose variance decreases as ξ\xi aligns more closely with the rare-event set.

Operatively, the adaptive multilevel splitting (AMS) algorithm proceeds as detailed in Algorithm [1](https://arxiv.org/html/2510.23461v1#alg1 "Algorithm 1 ‣ 2.3 Adaptive multilevel splitting (AMS) ‣ 2 Research methodology ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"):

Algorithm 1  Adaptive multilevel splitting (AMS)

0:  Sample size nn, discard count kk, importance function ξ\xi, final level LmaxL\_{\max}.

1:  Generate initial trajectories {Xj}j=1n\{X^{j}\}\_{j=1}^{n} up to their stopping times τj\tau\_{j}.

2:  Compute initial levels Sj←I​(Xtj)S\_{j}\leftarrow I(X\_{t}^{j}) for each trajectory jj.

3:  Sort the levels {Sj}j=1,…,n\{S\_{j}\}\_{j=1,\dots,n} as S(1)≤S(2)≤⋯≤S(n)S\_{(1)}\leq S\_{(2)}\leq\dots\leq S\_{(n)}.

4:  Set Z←S(k)Z\leftarrow S\_{(k)}, iteration counter q←0q\leftarrow 0.

5:  while Z<LmaxZ<L\_{\max} do

6:   Determine the set of trajectories indices Jq={j:Sj>Z}J\_{q}=\{j:S\_{j}>Z\}.

7:   Compute the number of trajectories to discard: Kq=|{j:Sj≤Z}|K\_{q}=|\{j:S\_{j}\leq Z\}|.

8:   Discard the KqK\_{q} trajectories with Sj≤ZS\_{j}\leq Z.

9:   Clone exactly KqK\_{q} trajectories from the set JqJ\_{q}.

10:   Resimulate each cloned trajectory starting from its hitting time of the set {ξ>Z}\{\xi>Z\} up to its stopping time τj\tau\_{j}.

11:   Update Sj←max0≤t≤τj⁡ξ​(Xtj)S\_{j}\leftarrow\max\_{0\leq t\leq\tau\_{j}}\xi(X\_{t}^{j}) for each cloned trajectory.

12:   Sort the levels {Sj}j=1,…,n\{S\_{j}\}\_{j=1,\dots,n} as S(1)≤S(2)≤⋯≤S(n)S\_{(1)}\leq S\_{(2)}\leq\dots\leq S\_{(n)}.

13:   Set Z←S(k)Z\leftarrow S\_{(k)}

14:   q←q+1q\leftarrow q+1.

15:  end while

16:  Compute the final AMS estimator:

|  |  |  |
| --- | --- | --- |
|  | p^AMS=(∏i=0qn−kn)×1n​∑j=1n𝟏{Xj∈D}.\hat{p}\_{\mathrm{AMS}}=\left(\prod\_{i=0}^{q}\frac{n-k}{n}\right)\times\frac{1}{n}\sum\_{j=1}^{n}\mathbf{1}\_{\{X^{j}\in D\}}. |  |

#### 2.3.1 Theoretical properties of AMS

##### Well-posedness and termination.

Let X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} be a Markov process with importance function ξ\xi and rare set DD. For fixed nn and k∈{1,…,n−1}k\in\{1,\dots,n-1\}, AMS is well-posed: the cutting level ZZ is an order statistic and, under standard assumptions (Feller property of XX, continuity of ξ\xi, strict entrance condition), the algorithm terminates almost surely after finitely many iterations [[24](https://arxiv.org/html/2510.23461v1#bib.bib24)].

##### Unbiasedness.

The estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^AMS=(∏q=1Qn−kn)​1n​∑j=1n𝟏{X(j)∈D}\hat{p}\_{\mathrm{AMS}}=\Big(\prod\_{q=1}^{Q}\tfrac{n-k}{n}\Big)\,\frac{1}{n}\sum\_{j=1}^{n}\mathbf{1}\_{\{X^{(j)}\in D\}} |  | (5) |

is unbiased for any ξ\xi and kk. It suffices that D⊂{ξ≥Imax}D\subset\{\xi\geq I\_{\max}\}, without requiring ξ​(x)≥Imax⇔x∈D\xi(x)\geq I\_{\max}\iff x\in D [[28](https://arxiv.org/html/2510.23461v1#bib.bib28), [37](https://arxiv.org/html/2510.23461v1#bib.bib37), [24](https://arxiv.org/html/2510.23461v1#bib.bib24)]. Unbiasedness extends to unnormalised measures γ​(φ)=𝔼​[φ​(Xτ)​𝟏D​(Xτ)]\gamma(\varphi)=\mathbb{E}[\varphi(X\_{\tau})\mathbf{1}\_{D}(X\_{\tau})]. Randomised cloning and correct handling of ties are necessary to avoid bias.

##### LLN and CLT.

A law of large numbers holds for AMS estimators. Under mild assumptions,

|  |  |  |
| --- | --- | --- |
|  | n​(γ1(n)​(φ)−γ1​(φ))⇒𝒩​(0,σ12​(φ)),\sqrt{n}\Big(\gamma^{(n)}\_{1}(\varphi)-\gamma\_{1}(\varphi)\Big)\ \Rightarrow\ \mathcal{N}(0,\sigma\_{1}^{2}(\varphi)), |  |

with asymptotic variance characterized via the Fleming–Viot formulation [[24](https://arxiv.org/html/2510.23461v1#bib.bib24), [38](https://arxiv.org/html/2510.23461v1#bib.bib38)]. For k=1k=1 and target probability pp,

|  |  |  |
| --- | --- | --- |
|  | n​(p^AMS−p)⇒𝒩​(0,σ2),−p2​log⁡p≤σ2≤ 2​p​(1−p).\sqrt{n}(\hat{p}\_{\mathrm{AMS}}-p)\ \Rightarrow\ \mathcal{N}(0,\sigma^{2}),\qquad-p^{2}\log p\ \leq\ \sigma^{2}\ \leq\ 2p(1-p). |  |

A general CLT for k>1k>1 remains open, though evidence suggests n−1/2n^{-1/2} scaling with variance comparable to SMC.

##### Role of the importance function.

Unbiasedness does not depend on ξ\xi, but variance does. Poor or multi-channel choices inflate variance and may yield heavy-tailed errors. In practice, variance is controlled by testing alternative ξ\xi and adjusting nn or kk [[24](https://arxiv.org/html/2510.23461v1#bib.bib24), [28](https://arxiv.org/html/2510.23461v1#bib.bib28)].

##### Key advantages.

AMS adapts intermediate levels and branching rates on the fly, removing the need for a priori specification as in classical Multilevel Splitting [[39](https://arxiv.org/html/2510.23461v1#bib.bib39)] or Sequential Monte Carlo [[40](https://arxiv.org/html/2510.23461v1#bib.bib40), [41](https://arxiv.org/html/2510.23461v1#bib.bib41)]. The algorithm maintains a fixed population size nn, ensuring robustness, parallel efficiency, and predictable memory use. It provides unbiased estimators for both rare-event probabilities and unnormalised measures γ​(φ)\gamma(\varphi), enabling straightforward parallelization across independent runs [[24](https://arxiv.org/html/2510.23461v1#bib.bib24), [28](https://arxiv.org/html/2510.23461v1#bib.bib28), [37](https://arxiv.org/html/2510.23461v1#bib.bib37)].

## 3 Theoretical comparison with variance reduction techniques

### 3.1 Antithetic variates: overview and limitations

Antithetic variates [[42](https://arxiv.org/html/2510.23461v1#bib.bib42)] reduce variance by pairing negatively correlated samples. In option pricing this corresponds to simulating each path together with its reflection obtained by negating Brownian increments. For monotone payoffs the estimator variance decreases, with a theoretical maximum reduction by a factor of two.

For binary options with probabilities as small as 10−610^{-6}, a 2×2\times gain is negligible relative to the computational burden.

### 3.2 Control variates: overview and limitations

Control variates reduce variance by exploiting correlation between the payoff YY and an auxiliary variable WW with known expectation. The estimator

|  |  |  |
| --- | --- | --- |
|  | ψ^CV=1n​∑i=1n(Yi−β​(Wi−𝔼​[W]))\hat{\psi}\_{\mathrm{CV}}=\frac{1}{n}\sum\_{i=1}^{n}\bigl(Y\_{i}-\beta(W\_{i}-\mathbb{E}[W])\bigr) |  |

remains unbiased, with optimal β∗=Cov​(Y,W)/Var​(W)\beta^{\*}=\mathrm{Cov}(Y,W)/\mathrm{Var}(W) yielding

|  |  |  |
| --- | --- | --- |
|  | Var​(ψ^CV)=1n​Var​(Y)​(1−ρY,W2).\mathrm{Var}(\hat{\psi}\_{\mathrm{CV}})=\frac{1}{n}\mathrm{Var}(Y)(1-\rho^{2}\_{Y,W}). |  |

Variance reduction is therefore effective only when WW is strongly correlated with YY.For digital or Asian binaries, suitable highly correlated controls are unavailable, and variance reduction is marginal.

### 3.3 Multilevel Monte Carlo: overview and limitations

Multilevel Monte Carlo (MLMC) [[15](https://arxiv.org/html/2510.23461v1#bib.bib15), [16](https://arxiv.org/html/2510.23461v1#bib.bib16)] exploits a hierarchy of approximations X0,…,XLX\_{0},\dots,X\_{L} of the same quantity. The telescoping identity

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[XL]=𝔼​[X0]+∑ℓ=1L𝔼​[Xℓ−Xℓ−1]\mathbb{E}[X\_{L}]=\mathbb{E}[X\_{0}]+\sum\_{\ell=1}^{L}\mathbb{E}[X\_{\ell}-X\_{\ell-1}] |  |

reduces variance by coupling successive levels with shared randomness. The resulting estimator achieves mean-square error 𝒪​(ε2)\mathcal{O}(\varepsilon^{2}) at cost 𝒪​(ε−2)\mathcal{O}(\varepsilon^{-2}), compared to 𝒪​(ε−3)\mathcal{O}(\varepsilon^{-3}) for standard Monte Carlo [[15](https://arxiv.org/html/2510.23461v1#bib.bib15)].

MLMC is effective for standard option pricing but less suited to rare-event estimation. In tail regimes, the variance of inter-level differences decays slowly, limiting efficiency for digital and barrier options. Optimal allocation of samples,

|  |  |  |
| --- | --- | --- |
|  | Nℓ∝ε−2​Vℓ/Cℓ,N\_{\ell}\propto\varepsilon^{-2}\sqrt{V\_{\ell}/C\_{\ell}}, |  |

depends on variances VℓV\_{\ell} that are themselves costly to estimate and may behave irregularly across levels, especially in rare-event settings. These features complicate implementation and reduce the expected efficiency gains.

### 3.4 Importance sampling: overview and limitations

Importance sampling (IS) [[43](https://arxiv.org/html/2510.23461v1#bib.bib43)] estimates ψ=𝔼​[h​(X)]\psi=\mathbb{E}[h(X)] by sampling from an alternative density gg and reweighting:

|  |  |  |
| --- | --- | --- |
|  | ψ^g=1n​∑i=1nh​(Yi)​f​(Yi)g​(Yi),Yi∼g.\hat{\psi}\_{g}=\frac{1}{n}\sum\_{i=1}^{n}h(Y\_{i})\frac{f(Y\_{i})}{g(Y\_{i})},\qquad Y\_{i}\sim g. |  |

Efficiency depends on the choice of gg, with the optimal density proportional to |h​(y)|​f​(y)|h(y)|f(y), which is generally unavailable.

A common construction is exponential tilting via Girsanov’s theorem. For Brownian-driven models, gθ​(y)=eθ​y−ψ​(θ)​f​(y)g\_{\theta}(y)=e^{\theta y-\psi(\theta)}f(y) with cumulant generating function ψ​(θ)=log⁡𝔼​[eθ​Y]\psi(\theta)=\log\mathbb{E}[e^{\theta Y}]. The optimal parameter θ∗\theta^{\*} satisfies ψ′​(θ∗)=a\psi^{\prime}(\theta^{\*})=a, where aa is the rare-event threshold.

In rare-event regimes IS becomes unstable. When exercise probabilities are of order 10−610^{-6}, the equation ψ′​(θ)=a\psi^{\prime}(\theta)=a may lack a solution or yield extreme θ∗\theta^{\*}, and evaluation of eθ​Ye^{\theta Y} produces flat likelihood landscapes with sporadic spikes. In such cases Newton–Raphson and related solvers fail to converge, and stochastic optimisers are equally unreliable [[44](https://arxiv.org/html/2510.23461v1#bib.bib44)].

Two further issues are critical. 
  
Variance explosion: an inappropriate choice of g​(y)g(y) can inflate the estimator’s variance instead of reducing it [[43](https://arxiv.org/html/2510.23461v1#bib.bib43)]. 
  
Payoff-specific design: effective importance sampling must be tailored to the payoff. Binary calls, binary puts, and Asian options require distinct tilting schemes, and multi-asset payoffs add combinatorial complexity [[13](https://arxiv.org/html/2510.23461v1#bib.bib13)].

AMS can be interpreted as a non-parametric analogue of IS: it requires only an importance function indicating progress toward the rare set, avoiding explicit tilting densities and unstable root-finding, and thus offering broader applicability across option classes.

## 4 AMS applications in finance

Having established the theoretical framework, AMS is now applied to binary option pricing under the Black–Scholes and Heston models. The Markov property of both dynamics makes them directly compatible with AMS, which relies on memoryless trajectories. The method is tested on the four binary contracts of Section 2.2, with efficiency gains most evident for deep out-of-the-money options where standard Monte Carlo becomes infeasible.

### 4.1 Importance function design

AMS performance depends critically on the importance function ξ\xi, which steers trajectories toward the rare-event set. Two constructions are considered:

* •

  Path-based functions. For European binaries, ξ\xi is the asset price StS\_{t}; for Asian binaries, the arithmetic average up to tt, 1t​∑i=0tSti\tfrac{1}{t}\sum\_{i=0}^{t}S\_{t\_{i}}. For puts, the sign is inverted. In all cases Lmax=KL\_{\max}=K ensures D⊆{ξ>Lmax}D\subseteq\{\xi>L\_{\max}\}.
* •

  Analytical approximations. Black–Scholes digital formulas are used as importance functions,

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | CallB​S\displaystyle\text{Call}\_{BS} | =e−r​T​Φ​(d2),\displaystyle=e^{-rT}\Phi(d\_{2}), |  | (6) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | PutB​S\displaystyle\text{Put}\_{BS} | =e−r​T​Φ​(−d2),\displaystyle=e^{-rT}\Phi(-d\_{2}), |  | (7) |

  with d2=ln⁡(S/K)+(r−σ2/2)​Tσ​Td\_{2}=\tfrac{\ln(S/K)+(r-\sigma^{2}/2)T}{\sigma\sqrt{T}}. At each tt, StS\_{t} (or the running average for Asians) is inserted as the spot input, regardless of the underlying model. Although exact only for European binaries under Black–Scholes, this construction captures the curvature of the pricing function and improves guidance toward the rare-event region. Here Lmax=0.5L\_{\max}=0.5 ensures D⊆{ξ>Lmax}D\subseteq\{\xi>L\_{\max}\}.

###### Lemma 4.1 (Unbiasedness of AMS for digital options).

Let (St)(S\_{t}) follow either the Black–Scholes dynamics

|  |  |  |
| --- | --- | --- |
|  | d​St=r​St​d​t+σ​St​d​Wt,dS\_{t}=rS\_{t}\,dt+\sigma S\_{t}\,dW\_{t}, |  |

or the Heston system

|  |  |  |
| --- | --- | --- |
|  | {d​St=r​St​d​t+Vt​St​d​Wt(1),d​Vt=κ​(θ−Vt)​d​t+ξ​Vt​d​Wt(2),\begin{cases}dS\_{t}=rS\_{t}\,dt+\sqrt{V\_{t}}\,S\_{t}\,dW\_{t}^{(1)},\\[4.0pt] dV\_{t}=\kappa(\theta-V\_{t})\,dt+\xi\sqrt{V\_{t}}\,dW\_{t}^{(2)},\end{cases} |  |

with (W(1),W(2))(W^{(1)},W^{(2)}) a correlated Brownian pair. In both cases the state process is Markovian.
  
Let DD be the rare–event set corresponding to the digital payoff
(European or Asian, call or put). For the importance functions ξ\xi introduced in
Section [4.1](https://arxiv.org/html/2510.23461v1#S4.SS1 "4.1 Importance function design ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), the sufficient condition

|  |  |  |
| --- | --- | --- |
|  | x∈D⇒ξ​(x)≥Lmaxx\in D\;\;\Rightarrow\;\;\xi(x)\geq L\_{\max} |  |

of [[28](https://arxiv.org/html/2510.23461v1#bib.bib28), Theorem 3.2] holds. Then the AMS estimator of the risk–neutral probability p=ℚ​(D)p=\mathbb{Q}(D) is

|  |  |  |
| --- | --- | --- |
|  | p^AMS=(∏i=0qn−kn)×1n​∑j=1n𝟏{X(j)∈D},\hat{p}\_{\mathrm{AMS}}=\left(\prod\_{i=0}^{q}\frac{n-k}{n}\right)\times\frac{1}{n}\sum\_{j=1}^{n}\mathbf{1}\_{\{X^{(j)}\in D\}}, |  |

where qq is the number of iterations required to reach the threshold LmaxL\_{\max}.
This estimator is unbiased, and the digital option value

|  |  |  |
| --- | --- | --- |
|  | V^=e−r​T​p^AMS\hat{V}=e^{-rT}\hat{p}\_{\mathrm{AMS}} |  |

is therefore an unbiased estimator of the true price, with the same asymptotic variance properties as in the general AMS framework.

### 4.2 Parameter setting and option strikes for algorithm performance analysis

For the Black–Scholes model, volatility is fixed at σ=0.2\sigma=0.2.
For the Heston model, parameters are set to ρ=−0.5\rho=-0.5, κ=2.0\kappa=2.0, θ=0.04\theta=0.04, and ψ=0.3\psi=0.3. 
  
All performance metrics are averaged over 50 independent runs, obtained by combining results from 5 different initial seeds, each used to generate 10 simulations, ensuring robust statistical confidence in the comparative analysis. 
  
Tests include European digital calls and puts with strikes 2.22.2 and 0.290.29, and Asian digitals. Under Black–Scholes, Asian strikes are 1.71.7 (call) and 0.630.63 (put); under Heston, 1.61.6 and 0.550.55. In all cases option values are of order 7.5×10−67.5\times 10^{-6}, representing rare-event regimes suitable for assessing AMS performance.

### 4.3 Results and discussion

#### 4.3.1 Impact of the selection parameter K on algorithm performance

The selection parameter KK determines the fraction of trajectories discarded at each iteration. Theory shows that asymptotic variance is minimized at K=1K=1 with an optimal importance function [[24](https://arxiv.org/html/2510.23461v1#bib.bib24), [38](https://arxiv.org/html/2510.23461v1#bib.bib38)], but this setting is computationally prohibitive.

We examine KK values from 5% to 45% of N=50,000N=50{,}000 particles, in 5% increments, for a digital call under Heston and an Asian digital call under Black–Scholes, both using the path-based importance function (Section [4.1](https://arxiv.org/html/2510.23461v1#S4.SS1 "4.1 Importance function design ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing")).

The results are reported in Table [1](https://arxiv.org/html/2510.23461v1#S4.T1 "Table 1 ‣ 4.3.1 Impact of the selection parameter K on algorithm performance ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing") and
Figure [2](https://arxiv.org/html/2510.23461v1#S4.F2 "Figure 2 ‣ 4.3.1 Impact of the selection parameter K on algorithm performance ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing").

Table 1: Execution time of the AMS algorithm for different rejection rates KK under two option pricing settings.

|  |  |  |
| --- | --- | --- |
| KK | Time (Digital, Heston) | Time (Digital asian, Black-Scholes) |
| 0.05 | 35.86 | 25.23 |
| 0.10 | 20.02 | 13.46 |
| 0.15 | 13.97 | 9.36 |
| 0.20 | 11.41 | 7.36 |
| 0.25 | 10.20 | 6.08 |
| 0.30 | 8.96 | 5.19 |
| 0.35 | 7.8 | 4.53 |
| 0.40 | 7.38 | 4.03 |
| 0.45 | 6.7 | 3.63 |

![Refer to caption](kkk.png)


Figure 2: Relationship between kk and the normalized variance (horizontal axis) for the simulation results

In the figures, blue markers correspond to the standard digital call option, while red markers represent the Asian digital call option. 
  
Results confirm the trade-off: small KK requires more iterations and substantially longer runtime (up to 30 seconds in the Heston case). Estimator quality, however, shows no clear monotonic dependence on KK, for these options, performance remains stable across the tested range.

#### 4.3.2 Impact of the number of trajectories N on algorithm performance

The particle count NN directly affects AMS performance. Larger NN reduces estimator variance but increases runtime due to higher simulation and sorting costs. Theoretical analysis shows complexity of order N​log⁡(p)​log⁡(N)N\log(p)\log(N), accounting for the sorting step and the generation of one new trajectory per iteration [[24](https://arxiv.org/html/2510.23461v1#bib.bib24), [38](https://arxiv.org/html/2510.23461v1#bib.bib38)].

Numerical experiments under both Black–Scholes and Heston models, using the options of Section [4.3.1](https://arxiv.org/html/2510.23461v1#S4.SS3.SSS1 "4.3.1 Impact of the selection parameter K on algorithm performance ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), confirm this trade-off. All tests use K=0.45K=0.45 and the path-based importance function.

Table 2: Execution time of the AMS algorithm as a function of the number of trajectories NN under two option pricing settings.

| NN | Time (Digital, Heston) | Time (Digital Asian, Black-Scholes) |
| --- | --- | --- |
| 50000 | 5.88 | 3.96 |
| 70000 | 8.79 | 6.08 |
| 90000 | 11.48 | 7.94 |
| 110000 | 14.03 | 9.66 |
| 130000 | 16.84 | 11.62 |
| 150000 | 19.44 | 13.37 |
| 170000 | 22.2 | 15.12 |
| 190000 | 25.06 | 17.19 |
| 210000 | 28.03 | 19.05 |

As reported in Table [2](https://arxiv.org/html/2510.23461v1#S4.T2 "Table 2 ‣ 4.3.2 Impact of the number of trajectories N on algorithm performance ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), computational cost grows consistently with NN, in agreement with the predicted −N​log⁡(p)​log⁡(N)-N\log(p)\log(N) scaling. Substituting the estimated pp and tested NN values yields an approximately constant ratio, supporting the theoretical complexity analysis.

These results highlight the inherent balance between variance reduction and runtime when tuning NN for AMS in option pricing applications.

#### 4.3.3 Analysis of option pricing results

Standard Monte Carlo is benchmarked against AMS, with multilevel Monte Carlo (MLMC) and antithetic variates as additional baselines. Within AMS, two importance functions are tested. Control variates are excluded due to negligible correlation with the payoff, and importance sampling is omitted since optimal tilting fails to converge in the rare-event regime considered and requires payoff-specific design.

Test cases focus on deep out-of-the-money contracts with exercise probabilities of order 10−610^{-6}, where AMS achieves significant gains. For higher probabilities (p>10−3p>10^{-3}), standard Monte Carlo remains competitive and AMS provides only limited advantage.

Performance is evaluated in terms of computational time (horizontal axis) and relative accuracy (vertical axis), defined as
VarMean,\frac{\sqrt{\mathrm{Var}}}{\mathrm{Mean}},
with the mean computed over 50 independent runs. Results are reported in Figures [3](https://arxiv.org/html/2510.23461v1#S4.F3 "Figure 3 ‣ 4.3.3 Analysis of option pricing results ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"),[4](https://arxiv.org/html/2510.23461v1#S4.F4 "Figure 4 ‣ 4.3.3 Analysis of option pricing results ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing").

The discard fraction is set to k=0.45k=0.45, as smaller values did not yield systematic variance reduction (Section [4.3.1](https://arxiv.org/html/2510.23461v1#S4.SS3.SSS1 "4.3.1 Impact of the selection parameter K on algorithm performance ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing")).

![Refer to caption](tot1.png)

Figure 3: Computational time (log scale) as a function of relative accuracy for different simulation methods for the Heston digital call and the Black–Scholes and Heston Asian digital call; numerical values are reported in Tables [5](https://arxiv.org/html/2510.23461v1#A2.T5 "Table 5 ‣ Appendix B Tables underlying the figures ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), [7](https://arxiv.org/html/2510.23461v1#A2.T7 "Table 7 ‣ Appendix B Tables underlying the figures ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), and [9](https://arxiv.org/html/2510.23461v1#A2.T9 "Table 9 ‣ Appendix B Tables underlying the figures ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing")



![Refer to caption](tot2.png)

Figure 4: Computational time (log scale) as a function of relative accuracy for different simulation methods for the Heston digital put and the Black–Scholes and Heston Asian digital put; numerical values are reported in Tables [6](https://arxiv.org/html/2510.23461v1#A2.T6 "Table 6 ‣ Appendix B Tables underlying the figures ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), [8](https://arxiv.org/html/2510.23461v1#A2.T8 "Table 8 ‣ Appendix B Tables underlying the figures ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"), and [10](https://arxiv.org/html/2510.23461v1#A2.T10 "Table 10 ‣ Appendix B Tables underlying the figures ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing")

The results demonstrate substantial efficiency gains of AMS across all tested settings (Figures [3](https://arxiv.org/html/2510.23461v1#S4.F3 "Figure 3 ‣ 4.3.3 Analysis of option pricing results ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"),[4](https://arxiv.org/html/2510.23461v1#S4.F4 "Figure 4 ‣ 4.3.3 Analysis of option pricing results ‣ 4.3 Results and discussion ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing")).

Computational time reduction.
For European binaries under Heston, AMS achieves speedups above 100100, peaking over 200200 at 5%5\% accuracy. Against other variance reduction methods, the gain remains close to 100100. For Asian binaries under Black–Scholes, improvements range from 2525 to 4040 over Monte Carlo, and 1515 to 2020 over MLMC. For digital options under Heston, both importance functions outperform Monte Carlo and MLMC; the first yields 66–10×10\times gains over MLMC, the second 1515–20×20\times.

Role of the importance function.
Performance depends only moderately on ξ\xi. Both tested choices are effective; the Black–Scholes-based function (AMS2) provides smoother guidance via the Φ​(d2)\Phi(d\_{2}) term, improving sampling efficiency in some cases.

Consistency across option types.
Efficiency gains hold for European and Asian binaries under both models, indicating robustness across payoffs and dynamics.

Overall, AMS delivers unbiased estimates with significant computational savings relative to Monte Carlo, and remains competitive with advanced variance reduction methods, particularly in rare-event regimes.

### 4.4 Extreme case analysis

An extreme scenario is considered to further test AMS. A digital option under Black–Scholes with S0=1S\_{0}=1, K=3.5K=3.5, T=1T=1, and r=0.03r=0.03 has analytical value 2.509×10−102.509\times 10^{-10}. Only the path-based importance function is used, to avoid embedding model information into ξ\xi.

Table [3](https://arxiv.org/html/2510.23461v1#S4.T3 "Table 3 ‣ 4.4 Extreme case analysis ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing") reports results for a 10%10\% relative accuracy target. For Monte Carlo, execution time is extrapolated analytically. With

|  |  |  |
| --- | --- | --- |
|  | ϵ=Var​(p^)p=p​(1−p)/Np,\epsilon=\frac{\sqrt{\mathrm{Var}(\hat{p})}}{p}=\frac{\sqrt{p(1-p)/N}}{p}, |  |

the required NN is (1−p)/(ϵ2​p)≈4×1011(1-p)/(\epsilon^{2}p)\approx 4\times 10^{11}, corresponding to TMC≈3.2×106T\_{\mathrm{MC}}\approx 3.2\times 10^{6} seconds (∼\sim888 hours) given 10610^{6} paths in 8 seconds.

Table 3: Comparison between Monte Carlo and AMS in the extreme scenario.

|  |  |  |
| --- | --- | --- |
|  | Monte Carlo | AMS |
| Time (s) | 3,200,000 | 29.979 |

AMS attains the target within 30 seconds, confirming its robustness in extreme rare-event regimes where standard Monte Carlo is computationally infeasible.

## 5 Conclusions and future work

### 5.1 Conclusions

This study establishes adaptive multilevel splitting (AMS) as a computationally superior method for pricing binary options in rare-event regimes. Across both Black–Scholes and Heston models, AMS achieves speedups of up to 200 over standard Monte Carlo while maintaining unbiasedness, and consistently outperforms variance-reduction baselines such as MLMC and antithetic variates.

To our knowledge, this is the first application of AMS to financial rare-event pricing. Benchmarking against the closest variance reduction methods in finance confirms its superior efficiency in deep out-of-the-money regimes, where conventional techniques become computationally infeasible.

The practical implications are significant: AMS renders previously intractable problems feasible, enabling tighter spreads and deeper liquidity for rare-event derivatives, with direct relevance for parametric insurance and catastrophe-linked products.

The method also shows strong scalability. Importance functions are simple to construct and adaptable across payoff types, and performance is less sensitive to their specification than in importance sampling. This robustness facilitates deployment in both academic and industry settings.

### 5.2 Future developments

The success of AMS in binary option pricing suggests several extensions beyond derivatives valuation.

A first direction is risk management, where AMS could improve the computation of tail risk measures. Value-at-Risk (VaR), defined as the loss threshold exceeded with small probability, is a rare-event problem. Existing Monte Carlo and importance sampling approaches are widely used [[45](https://arxiv.org/html/2510.23461v1#bib.bib45), [46](https://arxiv.org/html/2510.23461v1#bib.bib46)]; AMS offers the potential for more accurate and efficient estimates, relevant for stress testing and regulatory capital.

A second extension concerns model coverage. Incorporating exotic payoffs and multi-asset structures would broaden applicability, enabling AMS to address higher-dimensional rare-event problems and increasing the versatility of the package for quantitative finance.

A third avenue is methodological. Rough volatility models such as Bergomi [[47](https://arxiv.org/html/2510.23461v1#bib.bib47)] pose challenges because fractional Brownian motion violates the Markov property central to AMS. One possible solution is a lifted Markovian approximation embedding the non-Markovian dynamics in higher-dimensional state space [[48](https://arxiv.org/html/2510.23461v1#bib.bib48)], potentially extending AMS to this class of models.

## Appendix

## Appendix A C++ implementation with R interface via Rcpp

No R package currently provides AMS functionality for financial applications. To fill this gap, a dedicated implementation was developed in C++ [[49](https://arxiv.org/html/2510.23461v1#bib.bib49)] with an R interface via Rcpp [[50](https://arxiv.org/html/2510.23461v1#bib.bib50)].

The algorithmic structure of AMS, nested loops over splitting levels, trajectory simulation, and resampling, requires extensive floating-point operations and predictable memory access, making compiled code essential. The C++ engine employs pre-allocated trajectory containers, object pooling, vectorized SDE discretization, efficient random number generation, and in-place sorting to minimize memory and copying overhead.

The Rcpp interface exposes all algorithmic parameters and diagnostics within the R environment, while computationally intensive tasks remain in C++. This design combines the usability of R with near-native performance, enabling practical deployment of AMS in quantitative finance.

### A.1 Core implementation

The Rcpp implementation is organized into a set of core functions that handle stochastic simulation, payoff evaluation, importance function construction, and execution of the AMS algorithm (Table [4](https://arxiv.org/html/2510.23461v1#A1.T4 "Table 4 ‣ A.1 Core implementation ‣ Appendix A C++ implementation with R interface via Rcpp ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing")).

Table 4: Summary of core functions

| Function | Description |
| --- | --- |
| simulateAMS | Generates Monte Carlo paths. Implements exact Black–Scholes discretization and three Heston schemes: Euler–Maruyama, Milstein, and Andersen’s Quadratic–Exponential. |
| payoff | Evaluates six exotic payoffs: digital call, digital put, asian digital call, asian digital put, lookback call, and lookback put. |
| functionAMSCpp | Computes the two importance functions described in Section [4.1](https://arxiv.org/html/2510.23461v1#S4.SS1 "4.1 Importance function design ‣ 4 AMS applications in finance ‣ Adaptive Multilevel Splitting: First Application to Rare-Event Derivative Pricing"). |
| AMS | Executes the full AMS algorithm, integrating path generation, resampling, and weighting. Supports six payoff types and two importance functions. Parameters include strike, LmaxL\_{\max}, and selection fraction KK. |

Lookback options are implemented but excluded from the numerical study, as discretization error under discrete monitoring [[51](https://arxiv.org/html/2510.23461v1#bib.bib51)] prevents reliable benchmarking. Experiments are restricted to European and Asian binaries.

Code availability. The full implementation, including C++ source files and the R interface, is publicly available at <https://github.com/RiccardoGozzo/amsSim>.

## Appendix B Tables underlying the figures

Table 5: Computational times (in seconds) for different relative accuracy levels in the Heston digital call experiment.

| Relative accuracy | MC | MCA | MLMC | AMS 1 | AMS 2 |
| --- | --- | --- | --- | --- | --- |
| 0.20 | 86.13 | 78.39 | 56 | 0.729 | 0.54 |
| 0.15 | 146.2 | 124.88 | 114.10 | 1.1 | 1.05 |
| 0.10 | 311.62 | 233.2 | 190.41 | 1.7 | 1.64 |
| 0.05 | 1244.13 | 913.19 | 663.64 | 5.49 | 6.47 |




Table 6: Computational times (in seconds) for different relative accuracy levels in the Heston digital put experiment.

| Relative accuracy | MC | MCA | MLMC | AMS 1 | AMS 2 |
| --- | --- | --- | --- | --- | --- |
| 0.20 | 85.51 | 75.2 | 54.82 | 0.8 | 0.56 |
| 0.15 | 144.83 | 122.11 | 115.2 | 1.21 | 1.12 |
| 0.10 | 307.55 | 231.21 | 188.73 | 1.67 | 1.71 |
| 0.05 | 1235.77 | 910.3 | 659.9 | 5.55 | 6.09 |




Table 7: Computational times (in seconds) for different relative accuracy levels in the Black–Scholes Asian digital call experiment.

| Relative accuracy | MC | MCA | MLMC | AMS 1 | AMS 2 |
| --- | --- | --- | --- | --- | --- |
| 0.20 | 27.53 | 26.23 | 15.38 | 1.16 | 0.2 |
| 0.15 | 49.85 | 46.84 | 29.62 | 2.35 | 0.44 |
| 0.10 | 105.52 | 92.62 | 39.69 | 3.85 | 0.79 |
| 0.05 | 415.65 | 305.63 | 228.73 | 9.8 | 15.27 |




Table 8: Computational times (in seconds) for different relative accuracy levels in the Black–Scholes Asian digital put experiment.

| Relative accuracy | MC | MCA | MLMC | AMS 1 | AMS 2 |
| --- | --- | --- | --- | --- | --- |
| 0.20 | 28.11 | 26.52 | 16.7 | 1.351 | 0.316 |
| 0.15 | 50.73 | 47.41 | 27.91 | 2.160 | 0.504 |
| 0.10 | 106.75 | 95.31 | 38.97 | 3.910 | 0.815 |
| 0.05 | 421.29 | 309.77 | 214.84 | 9.99 | 14.11 |




Table 9: Computational times (in seconds) for different relative accuracy levels in the Heston Asian digital call experiment.

| Relative accuracy | MC | MCA | MLMC | AMS 1 | AMS 2 |
| --- | --- | --- | --- | --- | --- |
| 0.20 | 82.22 | 73.38 | 53.6 | 4.3 | 2.62 |
| 0.15 | 139.31 | 117.6 | 108.37 | 10.94 | 6.76 |
| 0.10 | 301.53 | 228.35 | 185.88 | 14.08 | 10.794 |
| 0.05 | 1221.18 | 899.04 | 640.85 | 106.05 | 36.56 |




Table 10: Computational times (in seconds) for different relative accuracy levels in the Heston Asian digital put experiment.

| Relative accuracy | MC | MCA | MLMC | AMS 1 | AMS 2 |
| --- | --- | --- | --- | --- | --- |
| 0.20 | 84.06 | 74.19 | 53.8 | 4.8 | 2.74 |
| 0.15 | 141.35 | 121.7 | 109.32 | 11.24 | 6.55 |
| 0.10 | 312.04 | 230.14 | 186.05 | 15.28 | 11 |
| 0.05 | 1212.5 | 901.29 | 645.01 | 110.6 | 35.41 |

## References

* [1]

  D. H. Vo, S. V. Huynh, A. T. Vo, and D. T.-T. Ha, “The importance of the financial derivatives markets to economic development in the world’s four major economies,” Journal of Risk and Financial Management, vol. 12, no. 1, 2019.
* [2]

  C. Muellerleile, Derivatives, Market Liquidity, and Infrastructural Finance, p. 13–25.
  Cambridge University Press, 2025.
* [3]

  A. Polacek et al., “Catastrophe bonds: A primer and retrospective,” Chicago Fed Letter, vol. 405, pp. 1–7, 2018.
* [4]

  K. Larsson, “Parametric heat wave insurance,” Journal of Commodity Markets, vol. 31, p. 100345, 2023.
* [5]

  S. Shreve, Stochastic Calculus for Finance II: Continuous-Time Models.
  No. v. 11 in Springer Finance Textbooks, Springer, 2004.
* [6]

  S. Shreve, Stochastic Calculus for Finance I: The Binomial Asset Pricing Model.
  Springer Finance, Springer New York, 2004.
* [7]

  P. Glasserman, Monte Carlo methods in financial engineering.
  New York: Springer, 2004.
* [8]

  J. L. Beck and K. M. Zuev, “Rare event simulation,” 2015.
* [9]

  J. A. Bucklew and J. Bucklew, Introduction to rare event simulation, vol. 5.
  Springer, 2004.
* [10]

  J. M. Hammersley and K. W. Morton, “A new monte carlo technique: antithetic variates,” in Mathematical proceedings of the Cambridge philosophical society, vol. 52, pp. 449–475, Cambridge University Press, 1956.
* [11]

  J. Kleijnen, A. Ridder, and R. Rubinstein, “Variance reduction techniques in monte carlo methods,” workingpaper, Information Management, 2010.
  Pagination: 18.
* [12]

  N. S. Rasmussen, “Control variates for monte carlo valuation of american options,” Journal of Computational Finance, 2005.
* [13]

  P. Glasserman, P. Heidelberger, and P. Shahabuddin, “Asymptotically optimal importance sampling and stratification for pricing path-dependent options,” Mathematical Finance, vol. 9, no. 2, pp. 117–152, 1999.
* [14]

  L. Swiler and N. West, “Importance sampling: Promises and limitations,” in 51st AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference 18th AIAA/ASME/AHS Adaptive Structures Conference 12th, p. 2850, 2010.
* [15]

  M. B. Giles, “Multilevel monte carlo methods,” Acta numerica, vol. 24, pp. 259–328, 2015.
* [16]

  M. B. Giles and L. Szpruch, “Multilevel monte carlo methods for applications in finance,” High-Performance Computing in Finance, pp. 197–247, 2018.
* [17]

  M. B. Alaya, K. Hajji, and A. Kebaier, “Adaptive importance sampling for multilevel monte carlo euler method,” Stochastics, vol. 95, no. 2, pp. 303–327, 2023.
* [18]

  A. Kebaier and J. Lelong, “Coupling importance sampling and multilevel monte carlo using sample average approximation,” Methodology and Computing in Applied Probability, vol. 20, pp. 611–641, 2018.
* [19]

  T. Müller, B. McWilliams, F. Rousselle, M. Gross, and J. Novák, “Neural importance sampling,” ACM Transactions on Graphics (ToG), vol. 38, no. 5, pp. 1–19, 2019.
* [20]

  T. Cui, S. Dolgov, and R. Scheichl, “Deep importance sampling using tensor trains with application to a priori and a posteriori rare events,” SIAM Journal on Scientific Computing, vol. 46, no. 1, pp. C1–C29, 2024.
* [21]

  F. Cérou and A. Guyader, “Adaptive multilevel splitting for rare event analysis,” Stochastic Analysis and Applications, vol. 25, no. 2, pp. 417–443, 2007.
* [22]

  M. J. J. Garvels, “The splitting method in rare event simulation,” 2000.
* [23]

  A. Doucet, N. De Freitas, N. J. Gordon, et al., Sequential Monte Carlo methods in practice, vol. 1.
  Springer, 2001.
* [24]

  F. Cérou, A. Guyader, and M. Rousset, “Adaptive multilevel splitting: Historical perspective and recent results,” Chaos: An Interdisciplinary Journal of Nonlinear Science, vol. 29, no. 4, 2019.
* [25]

  S. Baars, D. Castellana, F. W. Wubs, and H. A. Dijkstra, “Application of adaptive multilevel splitting to high-dimensional dynamical systems,” Journal of Computational Physics, vol. 424, p. 109876, 2021.
* [26]

  C. Innes and S. Ramamoorthy, “Adaptive splitting of reusable temporal monitors for rare traffic violations,” in 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 12386–12393, IEEE, 2024.
* [27]

  Louvin, Henri, Dumonteil, Eric, Lelièvre, Tony, Rousset, Mathias, and Diop, Cheikh M., “Adaptive multilevel splitting for monte carlo particle transport,” EPJ Nuclear Sci. Technol., vol. 3, p. 29, 2017.
* [28]

  C.-E. Bréhier, M. Gazeau, L. Goudenège, T. Lelièvre, and M. Rousset, “Unbiasedness of some generalized adaptive multilevel splitting algorithms,” 2016.
* [29]

  F. Cérou and A. Guyader, “Fluctuation analysis of adaptive multilevel splitting,” 2016.
* [30]

  F. Cérou, P. Héas, and M. Rousset, “Adaptive reduced multilevel splitting,” arXiv preprint arXiv:2312.15256, 2023.
* [31]

  F. Black and M. Scholes, “The pricing of options and corporate liabilities,” Journal of political economy, vol. 81, no. 3, pp. 637–654, 1973.
* [32]

  S. L. Heston, “A closed-form solution for options with stochastic volatility with applications to bond and currency options,” The Review of Financial Studies, vol. 6, no. 2, pp. 327–343, 1993.
* [33]

  V. Bally and D. Talay, “The law of the euler scheme for stochastic differential equations. i: Convergence rate of the distribution function,” Probability Theory and Related Fields, vol. 104, no. 1, pp. 43–60, 1996.
* [34]

  D. J. Higham, X. Mao, and L. Szpruch, “Convergence, non-negativity and stability of a new milstein scheme with applications to finance,” Discrete and Continuous Dynamical Systems - Series B, vol. 18, no. 8, pp. 2083–2100, 2013.
* [35]

  L. B. G. Andersen, “Efficient simulation of the heston stochastic volatility model,” working paper, Bank of America, January 2007.
  38 pages. Posted: 22 Nov 2006.
* [36]

  P. P. Boyle, “Options: A monte carlo approach,” Journal of Financial Economics, vol. 4, no. 3, pp. 323–338, 1977.
* [37]

  A. Lee and N. Whiteley, “Variance estimation in the particle filter,” Biometrika, vol. 105, pp. 609–625, 06 2018.
* [38]

  F. Cérou, B. Delyon, A. Guyader, and M. Rousset, “On the asymptotic normality of adaptive multilevel splitting,” SIAM/ASA Journal on Uncertainty Quantification, vol. 7, no. 1, pp. 1–30, 2019.
* [39]

  H. Kahn and T. E. Harris, “Estimation of particle transmission by random sampling,” National Bureau of Standards applied mathematics series, vol. 12, pp. 27–30, 1951.
* [40]

  M. Garvels, The splitting method in rare event simulation.
  Phd thesis - research ut, graduation ut, University of Twente, Netherlands, Oct. 2000.
* [41]

  F. Cérou, P. del Moral, F. Le Gland, and P. Lezaud, “Genetic genealogical models in rare event analysis,” Research Report RR-5878, INRIA, 2006.
* [42]

  J. E. Gentle, “Antithetic variates,” Wiley Interdisciplinary Reviews: Computational Statistics, vol. 1, no. 1, pp. 114–117, 2009.
* [43]

  S. T. Tokdar and R. E. Kass, “Importance sampling: a review,” Wiley Interdisciplinary Reviews: Computational Statistics, vol. 2, no. 1, pp. 54–60, 2010.
* [44]

  F. Casella and B. Bachmann, “On the choice of initial guesses for the newton-raphson algorithm,” Applied Mathematics and Computation, vol. 398, p. 125991, 2021.
* [45]

  L. J. Hong, Z. Hu, and G. Liu, “Monte carlo methods for value-at-risk and conditional value-at-risk: a review,” ACM Transactions on Modeling and Computer Simulation (TOMACS), vol. 24, no. 4, pp. 1–37, 2014.
* [46]

  L. Sun and L. J. Hong, “Asymptotic representations for importance-sampling estimators of value-at-risk and conditional value-at-risk,” Operations Research Letters, vol. 38, no. 4, pp. 246–251, 2010.
* [47]

  J. Gatheral, M. Fukasawa, T. Jaisson, and M. Rosenbaum, “Rough volatility: An overview,” Global Derivatives, p. 142, 2017.
* [48]

  Q. Zhu, G. Loeper, W. Chen, and N. Langrené, “Markovian approximation of the rough bergomi model for monte carlo option pricing,” Mathematics, vol. 9, no. 5, p. 528, 2021.
* [49]

  W. H. Press, Numerical recipes 3rd edition: The art of scientific computing.
  Cambridge university press, 2007.
* [50]

  D. Eddelbuettel, “Seamless r and c++ integration with rcpp,” 2013.
* [51]

  M. Broadie and P. Glasserman, “Pricing american-style securities using simulation,” Journal of economic dynamics and control, vol. 21, no. 8-9, pp. 1323–1352, 1997.