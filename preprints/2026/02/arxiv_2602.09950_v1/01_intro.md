---
authors:
- Aurélien Alfonsi
- Ahmed Kebaier
- Jérôme Lelong
doc_id: arxiv:2602.09950v1
family_id: arxiv:2602.09950
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: How can the dual martingale help solving the primal optimal stopping problem?
url_abs: http://arxiv.org/abs/2602.09950v1
url_html: https://arxiv.org/html/2602.09950v1
venue: arXiv q-fin
version: 1
year: 2026
---


Aurélien Alfonsi
 CERMICS, ENPC, Institut Polytechnique de Paris, CNRS, Marne-la-Vallée, France & MathRisk team-project, Inria Paris, France.
  
aurelien.alfonsi@enpc.fr
  
Ahmed Kebaier
LaMME, CNRS, UMR 8071, Université Évry Paris Saclay, 91037, Évry, France.
  
ahmed.kebaier@univ-evry.fr
  
Jérôme Lelong
 Univ. Grenoble Alpes, CNRS, Grenoble INP, LJK, 38000 Grenoble, France.
  
jerome.lelong@univ-grenoble-alpes.fr
  
Acknowledgements: AA and AK benefited from the support of the “chaire Risques financiers”, Fondation du Risque.

(February 10, 2026)

###### Abstract

Motivated by recent results on the dual formulation of optimal stopping problems, we investigate in this short paper how the knowledge of an approximating dual martingale can improve the efficiency of primal methods. In particular, we show on numerical examples that accurate approximations of a dual martingale efficiently reduce the variance for the primal optimal stopping problem.

Keywords: Optimal stopping, Variance Reduction, Pure dual algorithm, Martingale, Least square Monte Carlo, Bermudan option.
  
AMS subject classifications (2020): 62L15, 60G40, 91G20, 65C05.

## 1 Introduction and framework

Let N∈ℕ∗N\in{\mathbb{N}}^{\*} and (Ω,ℱ¯,ℱ=(ℱn)0≤n≤N,ℙ)(\Omega,\overline{{\mathcal{F}}},{\mathcal{F}}=({\mathcal{F}}\_{n})\_{0\leq n\leq N},{\mathbb{P}}) be a filtered probability space with a discrete time filtration.
We consider a market with dd assets (Snk,n≥0)(S^{k}\_{n},n\geq 0), k∈{0,…,d}k\in\{0,\dots,d\}, with S0S^{0} being the risk-free asset. We are interested in the pricing and hedging of a Bermudan option paying Ψ​(Sn1,…,Snd)\Psi(S^{1}\_{n},\dots,S^{d}\_{n}) if exercised at time nn. We denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zn=Ψ​(Sn1,…,Snd)Sn0Z\_{n}=\frac{\Psi(S^{1}\_{n},\dots,S^{d}\_{n})}{S^{0}\_{n}} |  | (1) |

the discounted payoff and we assume that max0≤n≤N⁡𝔼​[|Zn|2]<∞\max\_{0\leq n\leq N}{\mathbb{E}}[|Z\_{n}|^{2}]<\infty.
We define the Snell envelope, for n∈{0,…,N}n\in\{0,\dots,N\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Un=supτ∈𝒯n,N𝔼​[Zτ|ℱn],U\_{n}=\sup\_{\tau\in{\mathcal{T}}\_{n,N}}{\mathbb{E}}[Z\_{\tau}|{\mathcal{F}}\_{n}], |  | (2) |

where 𝒯n,N{\mathcal{T}}\_{n,N} denotes the set of ℱ{\mathcal{F}}-stopping times taking values in {n,…,N}\{n,\dots,N\}.
It classically solves the dynamic programming equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | {UN=ZNUn=max⁡(Zn,𝔼​[Un+1|ℱn]),0≤n≤N−1.\begin{cases}U\_{N}&=Z\_{N}\\ U\_{n}&=\max\left(Z\_{n},{\mathbb{E}}[U\_{n+1}|{\mathcal{F}}\_{n}]\right),\quad 0\leq n\leq N-1.\end{cases} |  | (3) |

The process UU is a L2L^{2} supermartingale and τ⋆:=inf{n∈{0,…,N}:Un=Zn}\tau^{\star}:=\inf\{n\in\{0,\dots,N\}:U\_{n}=Z\_{n}\} is an optimal stopping time for ([2](https://arxiv.org/html/2602.09950v1#S1.E2 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) satisfying that (Un∧τ⋆)0≤n≤N(U\_{n\wedge\tau^{\star}})\_{0\leq n\leq N} is a martingale.
The optimal policy τ⋆\tau^{\star} is obtained from the celebrated Longstaff Schwarz algorithm (see Longstaff and Schwartz ([2001](https://arxiv.org/html/2602.09950v1#bib.bib12)))

|  |  |  |  |
| --- | --- | --- | --- |
|  | {τN=Nτn=n​𝟏{Zn≥𝔼​[Zτn+1|ℱn]}+τn+1​𝟏{Zn<𝔼​[Zτn+1|ℱn]},0≤n≤N−1.\begin{cases}\tau\_{N}&=N\\ \tau\_{n}&=n{\bf 1}\_{\left\{Z\_{n}\geq{\mathbb{E}}[Z\_{\tau\_{n+1}}|{\mathcal{F}}\_{n}]\right\}}+\tau\_{n+1}{\bf 1}\_{\left\{Z\_{n}<{\mathbb{E}}[Z\_{\tau\_{n+1}}|{\mathcal{F}}\_{n}]\right\}},\quad 0\leq n\leq N-1.\end{cases} |  | (4) |

Then, τn\tau\_{n} is the optimal stopping time on the time interval {n,…,N}\{n,\dots,N\}, and satisfies supτ∈𝒯n,N𝔼​[Zτ|ℱn]=𝔼​[Zτn|ℱn]\sup\_{\tau\in{\mathcal{T}}\_{n,N}}{\mathbb{E}}[Z\_{\tau}|{\mathcal{F}}\_{n}]={\mathbb{E}}[Z\_{\tau\_{n}}|{\mathcal{F}}\_{n}]. The stopping time τ0\tau\_{0} is thus equal to τ⋆\tau^{\star}.

Equations ([2](https://arxiv.org/html/2602.09950v1#S1.E2 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")), ([3](https://arxiv.org/html/2602.09950v1#S1.E3 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) and ([4](https://arxiv.org/html/2602.09950v1#S1.E4 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) are often referred to as the primal approach. The dual approach was introduced by Rogers ([2002](https://arxiv.org/html/2602.09950v1#bib.bib13)); Haugh and Kogan ([2004](https://arxiv.org/html/2602.09950v1#bib.bib7)) and consists in writing

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Un\displaystyle U\_{n} | =infM∈ℍ2𝔼​[maxn≤j≤N⁡{Zj−(Mj−Mn)}|ℱn],\displaystyle=\inf\_{M\in{\mathbb{H}}^{2}}{\mathbb{E}}\left[\max\_{n\leq j\leq N}\{Z\_{j}-(M\_{j}-M\_{n})\}\bigg|{\mathcal{F}}\_{n}\right], |  | (5) |

where ℍ2{\mathbb{H}}^{2} is the set of square integrable ℱ{\mathcal{F}}-martingales.
The infimum is achieved, among others, by the martingale M⋆M^{\star} coming from the Doob-Meyer decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | Un=U0+Mn⋆−An⋆,U\_{n}=U\_{0}+M^{\star}\_{n}-A^{\star}\_{n}, |  | (6) |

where M⋆∈ℍ2M^{\star}\in{\mathbb{H}}^{2} vanishes at 0 and A⋆A^{\star} is a predictable, nondecreasing and square integrable process also vanishing at 0. There are many works in the literature proposing approximations of the martingale M⋆M^{\star}. For instance, Haugh and Kogan ([2004](https://arxiv.org/html/2602.09950v1#bib.bib7)), Andersen and Broadie ([2004](https://arxiv.org/html/2602.09950v1#bib.bib2)) and Belomestny et al. ([2009](https://arxiv.org/html/2602.09950v1#bib.bib3)) construct these approximations by first numerically solving the primal problem: Haugh and Kogan ([2004](https://arxiv.org/html/2602.09950v1#bib.bib7)) and Belomestny et al. ([2009](https://arxiv.org/html/2602.09950v1#bib.bib3)) need an approximation of UU, while Andersen and Broadie ([2004](https://arxiv.org/html/2602.09950v1#bib.bib2)) need an approximation of τ⋆\tau^{\star}. In contrast, many other papers such as Desai et al. ([2012](https://arxiv.org/html/2602.09950v1#bib.bib6)), Belomestny et al. ([2019](https://arxiv.org/html/2602.09950v1#bib.bib4)) and Lelong ([2018](https://arxiv.org/html/2602.09950v1#bib.bib10)) propose to directly solve the dual problem ([11](https://arxiv.org/html/2602.09950v1#S3.E11 "In 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")) to get an approximation of one solution of ([5](https://arxiv.org/html/2602.09950v1#S1.E5 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")). Recently, we have proposed in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)) a new purely dual formulation, the only solution of which is M⋆M^{\star}. It is approximated by using only tradable instruments, which makes it also relevant for hedging.

The aim of this short paper is to investigate how the knowledge of this approximation may help to solve the primal problem ([3](https://arxiv.org/html/2602.09950v1#S1.E3 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")). In particular, we propose a new variance reduction technique motivated by the following remark: Zτ⋆−Mτ⋆⋆=Uτ⋆−Mτ⋆⋆=U0Z\_{\tau^{\star}}-M^{\star}\_{\tau^{\star}}=U\_{\tau^{\star}}-M^{\star}\_{\tau^{\star}}=U\_{0} is deterministic. In fact, we have U0=𝔼​[Zτ⋆]=𝔼​[Uτ⋆]=U0−𝔼​[Aτ⋆⋆]U\_{0}={\mathbb{E}}[Z\_{\tau^{\star}}]={\mathbb{E}}[U\_{\tau^{\star}}]=U\_{0}-{\mathbb{E}}[A^{\star}\_{\tau^{\star}}], which gives that Aτ⋆⋆=0A^{\star}\_{\tau^{\star}}=0 almost surely. Thus, if both M⋆M^{\star} and τ⋆\tau^{\star} were exactly known, only one simulation would be necessary to compute U0U\_{0}, which is the paramount of variance reduction! Now, suppose that we have at hand a martingale approximation M^\hat{M} of M⋆M^{\star} and that τ^\hat{\tau} is an approximation of τ⋆\tau^{\star}, then a natural control variate reduction method is to compute a Monte-Carlo approximation of 𝔼​[Zτ^−λ​M^τ^]{\mathbb{E}}[Z\_{\hat{\tau}}-\lambda\hat{M}\_{\hat{\tau}}], where λ\lambda minimizes the variance of Zτ^−λ​M^τ^Z\_{\hat{\tau}}-\lambda\hat{M}\_{\hat{\tau}}. The idea of finding such a martingale for variance reduction purposes has already been considered in the literature, see e.g. Juneja and Kalra ([2009](https://arxiv.org/html/2602.09950v1#bib.bib8)). Here, we want to leverage on our recent results in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)) that presents a generic algorithm to approximate M⋆M^{\star}.

The paper is structured as follows. In Section [2](https://arxiv.org/html/2602.09950v1#S2 "2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?"), we present different ways of using the control variate method based on the approximated dual martingale. Then, we show on different numerical examples the relevance of the method, which provides a much more accurate estimator of U0U\_{0}. We also investigate if directly solving the Longstaff Schwartz algorithm on Z−M^Z-\hat{M} rather than on ZZ may improve the accuracy. Up to our knowledge, this direction has not been much investigated in the literature, but it turns out in our case that it has little effect on the pricing accuracy. In Section [3](https://arxiv.org/html/2602.09950v1#S3 "3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?"), we propose a random time approximation of the optimal policy that uses only M^\hat{M}. Last, the appendix sections recall the approximation M^\hat{M} developed in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)) and also analyse the variance decomposition in the Longstaff Schwartz algorithm.

## 2 The dual martingale as a control variate for the primal problem

### 2.1 Methodology

We start by a simple remark regarding the primal problem. Let us consider M∈ℍ2M\in{\mathbb{H}}^{2}, such that M0=0M\_{0}=0. It is clear from the optional stopping theorem, that supτ∈𝒯0,N𝔼​[Zτ]=supτ∈𝒯0,N𝔼​[Zτ−Mτ]\sup\_{\tau\in{\mathcal{T}}\_{0,N}}{\mathbb{E}}[Z\_{\tau}]=\sup\_{\tau\in{\mathcal{T}}\_{0,N}}{\mathbb{E}}[Z\_{\tau}-M\_{\tau}]. Hence, the Bermudan option price U0U\_{0} can also be obtained by applying the Longstaff Schwartz algorithm either to the discounted payoff ZnZ\_{n} or alternatively to Zn−MnZ\_{n}-M\_{n}.

A first idea would be then to use the martingale M^\hat{M} developed in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)) (see also ([21](https://arxiv.org/html/2602.09950v1#A2.E21 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?"))) and to implement the Longstaff Schwartz algorithm on the option with discounted payoff Z−M^Z-\hat{M}. Note that as M^\hat{M} is an approximation of M⋆M^{\star}, we expect that the least squares approximation of 𝔼​[Zτn+1−M^τn+1|ℱn]{\mathbb{E}}[Z\_{\tau\_{n+1}}-\hat{M}\_{\tau\_{n+1}}|{\mathcal{F}}\_{n}] will have very little variance. Let us be more precise and denote by 𝒫n{\mathcal{P}}\_{n} the L2L^{2} projection on a finite dimensional vector subspace of L2​(Ω,ℱn)L^{2}(\Omega,{\mathcal{F}}\_{n}), which is used for the practical implementation of the Longstaff-Schwartz algorithm (more generally, 𝒫n{\mathcal{P}}\_{n} may be any function from L2​(Ω,ℱN)L^{2}(\Omega,{\mathcal{F}}\_{N}) to L2​(Ω,ℱn)L^{2}(\Omega,{\mathcal{F}}\_{n}) approximating the conditional expectation). Then, ([4](https://arxiv.org/html/2602.09950v1#S1.E4 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) is approximated by

|  |  |  |
| --- | --- | --- |
|  | {τNL​S2′=NτnL​S2′=n​𝟏{Zn−M^n≥𝒫n​(Zτn+1L​S2′−M^τn+1L​S2′)}+τn+1L​S2′​𝟏{Zn−M^n<𝒫n​(Zτn+1L​S2′−M^τn+1L​S2′)},\begin{cases}\tau^{LS^{\prime}\_{2}}\_{N}&=N\\ \tau^{LS^{\prime}\_{2}}\_{n}&=n{\bf 1}\_{\left\{Z\_{n}-\hat{M}\_{n}\geq{\mathcal{P}}\_{n}\left(Z\_{\tau^{LS^{\prime}\_{2}}\_{n+1}}-\hat{M}\_{\tau^{LS^{\prime}\_{2}}\_{n+1}}\right)\right\}}+\tau^{LS^{\prime}\_{2}}\_{n+1}{\bf 1}\_{\left\{Z\_{n}-\hat{M}\_{n}<{\mathcal{P}}\_{n}\left(Z\_{\tau^{LS^{\prime}\_{2}}\_{n+1}}-\hat{M}\_{\tau^{LS^{\prime}\_{2}}\_{n+1}}\right)\right\}},\end{cases} |  |

for 0≤n≤N−10\leq n\leq N-1, but also by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {τNL​S2=NτnL​S2=n​𝟏{Zn≥𝒫n​(Zτn+1L​S2−M^τn+1L​S2+M^n)}+τn+1L​S2​𝟏{Zn<𝒫n​(Zτn+1L​S2−M^τn+1L​S2+M^n)},\begin{cases}\tau^{LS\_{2}}\_{N}&=N\\ \tau^{LS\_{2}}\_{n}&=n{\bf 1}\_{\left\{Z\_{n}\geq{\mathcal{P}}\_{n}\left(Z\_{\tau^{LS\_{2}}\_{n+1}}-\hat{M}\_{\tau^{LS\_{2}}\_{n+1}}+\hat{M}\_{n}\right)\right\}}+\tau^{LS\_{2}}\_{n+1}{\bf 1}\_{\left\{Z\_{n}<{\mathcal{P}}\_{n}\left(Z\_{\tau^{LS\_{2}}\_{n+1}}-\hat{M}\_{\tau^{LS\_{2}}\_{n+1}}+\hat{M}\_{n}\right)\right\}},\end{cases} |  | (7) |

which are not equivalent since we typically have 𝒫n​(M^n)≠M^n{\mathcal{P}}\_{n}(\hat{M}\_{n})\not=\hat{M}\_{n}. In practice, for Markovian models, i.e. when SS introduced in ([1](https://arxiv.org/html/2602.09950v1#S1.E1 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) is a Markov chain, we usually take 𝒫n{\mathcal{P}}\_{n} as the projection on the vector space generated by polynomial functions of SnS\_{n} with a bounded degree. To underline this, note that we do not have Zn−M^n≥𝔼​[Zτn+1−M^τn+1|Sn]⇔Zn≥𝔼​[Zτn+1|Sn]Z\_{n}-\hat{M}\_{n}\geq{\mathbb{E}}[Z\_{\tau\_{n+1}}-\hat{M}\_{\tau\_{n+1}}|S\_{n}]\iff Z\_{n}\geq{\mathbb{E}}[Z\_{\tau\_{n+1}}|S\_{n}] since in general 𝔼​[M^n|Sn]≠M^n{\mathbb{E}}[\hat{M}\_{n}|S\_{n}]\not=\hat{M}\_{n}, but we do have Zn≥𝔼​[Zτn+1−M^τn+1+M^n|Sn]⇔Zn≥𝔼​[Zτn+1|Sn]Z\_{n}\geq{\mathbb{E}}[Z\_{\tau\_{n+1}}-\hat{M}\_{\tau\_{n+1}}+\hat{M}\_{n}|S\_{n}]\iff Z\_{n}\geq{\mathbb{E}}[Z\_{\tau\_{n+1}}|S\_{n}] since 𝔼​[M^τn+1−M^n|Sn]=0{\mathbb{E}}[\hat{M}\_{\tau\_{n+1}}-\hat{M}\_{n}|S\_{n}]=0. This formally explains why it is much better to use ([7](https://arxiv.org/html/2602.09950v1#S2.E7 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) to approximate ([4](https://arxiv.org/html/2602.09950v1#S1.E4 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?"))111For example on the Bermudan put case of Table [1](https://arxiv.org/html/2602.09950v1#S2.T1 "Table 1 ‣ 2.2.1 One dimensional options ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?"), with the same parameters as in the first line of the table, we obtain with τ0L​S2′\tau\_{0}^{LS^{\prime}\_{2}} a Bermudan put price of 9.5831 (below than the European price 9.6642 !) instead of 9.9064 with τ0L​S2\tau\_{0}^{LS\_{2}}, which is closer to the real price since the price is approximated from below. Thus, in all our numerical experiments we will consider ([7](https://arxiv.org/html/2602.09950v1#S2.E7 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")).. We will simply denote by τL​S2=τ0L​S2\tau^{LS\_{2}}=\tau^{LS\_{2}}\_{0} the approximation of the optimal stopping time given by the algorithm. We will compare this stopping time with the classical stopping time computed on ZZ and defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {τNL​S1=NτnL​S1=n​𝟏{Zn≥𝒫n​(Zτn+1L​S1)}+τn+1L​S1​𝟏{Zn<𝒫n​(Zτn+1L​S1)},0≤n≤N−1,\begin{cases}\tau^{LS\_{1}}\_{N}&=N\\ \tau^{LS\_{1}}\_{n}&=n{\bf 1}\_{\left\{Z\_{n}\geq{\mathcal{P}}\_{n}\left(Z\_{\tau^{LS\_{1}}\_{n+1}}\right)\right\}}+\tau^{LS\_{1}}\_{n+1}{\bf 1}\_{\left\{Z\_{n}<{\mathcal{P}}\_{n}\left(Z\_{\tau^{LS\_{1}}\_{n+1}}\right)\right\}},\quad 0\leq n\leq N-1,\end{cases} |  | (8) |

and set τL​S1=τ0L​S1\tau^{LS\_{1}}=\tau^{LS\_{1}}\_{0}.

In practice, the projection 𝒫n{\mathcal{P}}\_{n} can barely be computed in a closed form. We denote by 𝒫^nQ\hat{{\mathcal{P}}}\_{n}^{Q} its empirical approximation using QQ samples of ZZ (and M^\hat{M} if needed). This leads to the following implementable approximation of (τnL​S1)0≤n≤N(\tau^{LS\_{1}}\_{n})\_{0\leq n\leq N}

|  |  |  |
| --- | --- | --- |
|  | {τ^NL​S1,Q=Nτ^nL​S1,Q=n​𝟏{Zn≥𝒫^nQ​(Zτ^n+1L​S1,Q)}+τ^n+1L​S1,Q​𝟏{Zn<𝒫^nQ​(Zτ^n+1L​S1,Q)},0≤n≤N−1.\begin{cases}\hat{\tau}^{LS\_{1},Q}\_{N}&=N\\ \hat{\tau}^{LS\_{1},Q}\_{n}&=n{\bf 1}\_{\left\{Z\_{n}\geq\hat{{\mathcal{P}}}\_{n}^{Q}\left(Z\_{\hat{\tau}^{LS\_{1},Q}\_{n+1}}\right)\right\}}+\hat{\tau}^{LS\_{1},Q}\_{n+1}{\bf 1}\_{\left\{Z\_{n}<\hat{{\mathcal{P}}}\_{n}^{Q}\left(Z\_{\hat{\tau}^{LS\_{1},Q}\_{n+1}}\right)\right\}},\quad 0\leq n\leq N-1.\end{cases} |  |

We define τ^NL​S2,Q\hat{\tau}^{LS\_{2},Q}\_{N} in a similar way.

We advise to use three different sets of samples to avoid potential issues of bias and overfitting that are already well known in the Longstaff Schwartz pricing method alone. The first sample is used to compute the coefficients αnQ1\alpha^{Q\_{1}}\_{n} for n∈{1,…,N}n\in\{1,\dots,N\}, which define the approximation M^n\hat{M}\_{n}, see Eq. ([20](https://arxiv.org/html/2602.09950v1#A2.E20 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")) and ([21](https://arxiv.org/html/2602.09950v1#A2.E21 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")). Then, we implement the Longstaff Schwartz algorithm on the second one to get τ^L​Si,Q2\hat{\tau}^{LS\_{i},Q\_{2}}, i∈{1,2}i\in\{1,2\}. Then, we generate a third sample to calculate out-of-sample Monte-Carlo prices to approximate 𝔼​[Zτ^L​Si,Q2]{\mathbb{E}}[Z\_{\hat{\tau}^{LS\_{i},Q\_{2}}}]. More precisely, we use here a control variate variance reduction and compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1Q3​∑q=1Q3Zτ^L​Si,Q2,(q)(q)−λ^​M^τ^L​Si,Q2,(q)(q),\frac{1}{Q\_{3}}\sum\_{q=1}^{Q\_{3}}Z^{(q)}\_{\hat{\tau}^{LS\_{i},Q\_{2},(q)}}-\hat{\lambda}\hat{M}^{(q)}\_{\hat{\tau}^{LS\_{i},Q\_{2},(q)}}, |  | (9) |

where λ^=∑q=1Q3Zτ^L​Si,Q2,(q)(q)​M^τ^L​Si,Q2,(q)(q)∑q=1Q3(M^τ^L​Si,Q2,(q)(q))2\hat{\lambda}=\frac{\sum\_{q=1}^{Q\_{3}}Z^{(q)}\_{\hat{\tau}^{LS\_{i},Q\_{2},(q)}}\hat{M}^{(q)}\_{\hat{\tau}^{LS\_{i},Q\_{2},(q)}}}{\sum\_{q=1}^{Q\_{3}}(\hat{M}^{(q)}\_{\hat{\tau}^{LS\_{i},Q\_{2},(q)}})^{2}} minimizes the asymptotical variance. Here, we denote by Q3Q\_{3} the number of samples in the second and third sets that are used for the Longstaff Schwartz algorithm and the Monte Carlo estimation.

However, let us note that for a given martingale M^\hat{M}, the statistical error comes from two different sources: the first one is linked to the approximation of τL​Si\tau^{LS\_{i}} by τ^L​Si,Q2\hat{\tau}^{LS\_{i},Q\_{2}} and the second one is the classical statistical error associated with the computation of 𝔼​[ZτL​Si]{\mathbb{E}}[Z\_{\tau^{LS\_{i}}}]. This is analysed in (Clément et al., [2002](https://arxiv.org/html/2602.09950v1#bib.bib5), Theorem 4.2) where a CLT is shown, see Appendix [A](https://arxiv.org/html/2602.09950v1#A1 "Appendix A Variance decomposition in the Longstaff Schwartz algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?") for further discussion.

### 2.2 Numerical examples

#### 2.2.1 One dimensional options

We start our discussion by considering a Bermudan put option with payoff function

|  |  |  |
| --- | --- | --- |
|  | Ψ​(S)=(K−S)+.\Psi(S)=(K-S)\_{+}. |  |

The calculation of the approximating martingale M^\hat{M} is carried out by using the Algorithm presented in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)). Appendix [B](https://arxiv.org/html/2602.09950v1#A2 "Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?") recalls the main steps of this algorithm and its parameters: N¯\bar{N} is the number of subticks, PP the number of local functions used in the regression and Q1Q\_{1} is the number of samples. In Table [1](https://arxiv.org/html/2602.09950v1#S2.T1 "Table 1 ‣ 2.2.1 One dimensional options ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?"), we have reported the prices obtained by three different primal methods.

1. 1.

   The classical Longstaff Schwartz method without any variance reduction. The price and the standard deviation of the Monte-Carlo estimator are given in the caption (multiplied by 1.961.96, this standard deviation gives the half-width of the 95% asymptotic confidence interval).
   The standard deviation is estimated from 40 independent runs of the Longstaff Schwartz algorithm.
2. 2.

   The Longstaff Schwartz method applied to ([7](https://arxiv.org/html/2602.09950v1#S2.E7 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) to determine the optimal stopping rule, and then the control variate reduction method Zτ^L​S2,Q2−λ​M^τ^L​S2,Q2Z\_{\hat{\tau}^{LS\_{2},Q\_{2}}}-\lambda\hat{M}\_{\hat{\tau}^{LS\_{2},Q\_{2}}} to calculate the price. The price and the standard deviation (computed on 40 independent runs) of the Monte-Carlo estimator are given in the 4th and 5th columns.
3. 3.

   The classical Longstaff Schwartz method applied to ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) to determine the optimal stopping rule, and then the control variate reduction method Zτ^L​S1,Q2−λ​M^τ^L​S1,Q2Z\_{\hat{\tau}^{LS\_{1},Q\_{2}}}-\lambda\hat{M}\_{\hat{\tau}^{LS\_{1},Q\_{2}}} to calculate the price. The price and the standard deviation (computed on 40 independent runs) of the Monte-Carlo estimator are given in the 6th and 7th columns.

The last two columns indicate the price and standard deviation given by the dual method presented in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)). This indicates the quality of the approximation of M⋆M^{\star}: heuristically, the smaller is the dual price the better is the martingale M^\hat{M}.

| Q1Q\_{1} | N¯\bar{N} | PP | LS Eq. ([7](https://arxiv.org/html/2602.09950v1#S2.E7 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) | stddev | LS Eq. ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) | stddev | Dual | stddev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10510^{5} | 1 | 50 | 9.9064 | 0.0092 | 9.9025 | 0.0100 | 10.3159 | 0.0087 |
| 10510^{5} | 5 | 50 | 9.9065 | 0.0045 | 9.9045 | 0.0060 | 10.0787 | 0.0050 |
| 2⋅1062\cdot 10^{6} | 20 | 50 | 9.9072 | 0.0007 | 9.9071 | 0.0005 | 9.9625 | 0.0006 |

Table 1: Prices for a put option using a basis of PP local functions with K=S0=100K=S\_{0}=100, T=0.5T=0.5, r=0.06r=0.06, σ=0.4\sigma=0.4 and N=10N=10 exercising dates. Longstaff Schwartz algorithm is run with Q2=Q3=50000Q\_{2}=Q\_{3}=50000 samples and with a polynomial approximation of order 6. The LS price without variance reduction is 9.909.90, with a standard deviation 0.0513\mathbf{0.0513}. The value of λ\lambda in the control variate method is around 0.990.99 for each case.

First, we observe that the use of the martingale M^\hat{M} indeed allows to significantly reduce the variance, from a factor between 2525 up to 10410^{4} depending on the accuracy of M^\hat{M}. Second, we notice that there is almost no difference between using the Longstaff Schwartz algorithm with ([7](https://arxiv.org/html/2602.09950v1#S2.E7 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) or ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")): the main variance gain is given by using the control variate method afterwards. In the next examples, we have observed exactly the same thing, so we only present the results with τ^L​S1\hat{\tau}^{LS\_{1}}. However, we have noticed that the regressors of the Longstaff Schwartz method are often less noisy when using ([7](https://arxiv.org/html/2602.09950v1#S2.E7 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) instead of ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")), but this has almost no incidence on the price computation and its variance, see Appendix [A](https://arxiv.org/html/2602.09950v1#A1 "Appendix A Variance decomposition in the Longstaff Schwartz algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?"). Last, we observe on this example that the optimal value of λ\lambda is around 0.990.99. This is not surprising, since the optimal choice would be 11 if M^\hat{M} were exactly equal to M⋆M^{\star}. The value of λ\lambda is somehow another indicator to measure how M^\hat{M} is close to M⋆M^{\star}.

Now, we consider a butterfly option with payoff function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(S)=2​(K1+K22−S)+−(K1−S)+−(K2−S)+.\Psi(S)=2\left(\frac{K\_{1}+K\_{2}}{2}-S\right)\_{+}-\left(K\_{1}-S\right)\_{+}-\left(K\_{2}-S\right)\_{+}. |  | (10) |

We have reported our results in Table [2](https://arxiv.org/html/2602.09950v1#S2.T2 "Table 2 ‣ 2.2.1 One dimensional options ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?"). We observe a variance reduction222In all the tables, we report the standard deviation of the empirical Monte Carlo estimator that gives the precision on the price. The (multiplicative) computational gain is given by the variance ratio. up to 100100 on this example. The parameter λ\lambda used in the control variate method is between 0.970.97 and 0.990.99 in this experiment.

| Q1Q\_{1} | N¯\bar{N} | PP | LS Eq. ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) | stddev | λ\lambda | Dual | stddev |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10510^{5} | 5 | 50 | 5.6568 | 0.0045 | 0.9743 | 6.1278 | 0.0034 |
| 5⋅1055\cdot 10^{5} | 20 | 50 | 5.6563 | 0.0017 | 0.9905 | 5.8726 | 0.0011 |

Table 2: Prices for a butterfly option with parameters K1=90K\_{1}=90 K2=110K\_{2}=110, S0=95S\_{0}=95, T=0.5T=0.5, r=0.06r=0.06, σ=0.4\sigma=0.4 and N=10N=10, using a basis of PP local functions. The Longstaff-Schwartz algorithm is run with order 66 polynomials and Q2=Q3=50000Q\_{2}=Q\_{3}=50000 samples. The LS price without variance reduction is 5.655.65, with a standard deviation 0.015\mathbf{0.015}.

#### 2.2.2 Bermudan options on many assets

##### Basket option

We consider a put option on a basket of assets with payoff function

|  |  |  |
| --- | --- | --- |
|  | Ψ​(S)=(K−1d∑i=1dSi)+,S∈ℝd.\Psi(S)=\left(K-\mathop{\frac{1}{d}}\nolimits\sum\_{i=1}^{d}S^{i}\right)\_{+},\ S\in{\mathbb{R}}^{d}. |  |

We report in Table [3](https://arxiv.org/html/2602.09950v1#S2.T3 "Table 3 ‣ Basket option ‣ 2.2.2 Bermudan options on many assets ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?") the price of a Bermudan option with this payoff for d=3d=3. We notice that the variance reduction ranges from a factor 2525 for the martingale M^\hat{M} obtained with Q1=105Q\_{1}=10^{5} to a factor 400400 for the one obtained with Q1=5⋅105Q\_{1}=5\cdot 10^{5}.

| Q1Q\_{1} | N¯\bar{N} | PP | LS Eq. ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) | stddev | λ\lambda | Dual | stddev |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10510^{5} | 1 | 50 | 4.0373 | 0.0049 | 0.9782 | 4.3479 | 0.0045 |
| 2.5⋅1052.5\cdot 10^{5} | 5 | 50 | 4.0415 | 0.0015 | 0.9839 | 4.1517 | 0.0016 |
| 5⋅1055\cdot 10^{5} | 10 | 50 | 4.0424 | 0.0009 | 0.9855 | 4.1148 | 0.0009 |

Table 3: Prices for a Basket option with d=3d=3, σ=0.2\sigma=0.2, r=0.05r=0.05, T=1T=1, N=10N=10, S01=S02=S03=100S^{1}\_{0}=S^{2}\_{0}=S^{3}\_{0}=100, K=100K=100. LS implemented with polynomials function of order 55, Q2=Q3=50000Q\_{2}=Q\_{3}=50000. The LS price without variance reduction is 4.034.03, with a standard deviation 0.021\mathbf{0.021}.

##### Max-call option

We consider a call option on the maximum of a basket of assets with payoff:

|  |  |  |
| --- | --- | --- |
|  | Ψ​(S)=(K−max1≤k≤d⁡Sk)+.\Psi(S)=\left(K-\max\_{1\leq k\leq d}S^{k}\right)\_{+}. |  |

We have reported in Table [4](https://arxiv.org/html/2602.09950v1#S2.T4 "Table 4 ‣ Max-call option ‣ 2.2.2 Bermudan options on many assets ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?") the price of a Bermudan option with 2 assets. This example has been considered in (Andersen and Broadie, [2004](https://arxiv.org/html/2602.09950v1#bib.bib2), Table 2). We observe a variance reduction factor from 100100 to 16001600, which is very satisfactory. We note that the value obtained with the dual algorithm is rather far from the primal value, and the optimal value of λ\lambda is around 0.950.95. These facts indicate that M^\hat{M} is quite different from M⋆M^{\star}, nonetheless the variance reduction method still works well.

| Q1Q\_{1} | N¯\bar{N} | PP | LS Eq. ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) | stddev | λ\lambda | Dual | stddev |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10610^{6} | 1 | 10 | 8.0675 | 0.0038 | 0.9357 | 8.9877 | 0.0041 |
| 2⋅1062\cdot 10^{6} | 5 | 10 | 8.0671 | 0.0018 | 0.9480 | 8.5439 | 0.0018 |
| 4⋅1064\cdot 10^{6} | 10 | 10 | 8.0675 | 0.0012 | 0.9501 | 8.4753 | 0.0011 |

Table 4: Prices for a max-call option with d=2d=2, K=100K=100, S01=S02=90S^{1}\_{0}=S^{2}\_{0}=90, σ=0.2\sigma=0.2, δ=0.1\delta=0.1, r=0.05r=0.05, T=3T=3, N=9N=9. LS parameters: polynomial functions of order 55, Q2=Q3=50000Q\_{2}=Q\_{3}=50000. The LS price without variance reduction is 8.068.06, with a standard deviation 0.044\mathbf{0.044}.

##### Min Butterflies

For the last example, we consider a rather exotic option that pays

|  |  |  |
| --- | --- | --- |
|  | min1≤i≤d⁡(Ψ​(Si)),\min\_{1\leq i\leq d}(\Psi(S^{i})), |  |

where Ψ\Psi is the butterfly payoff defined in ([10](https://arxiv.org/html/2602.09950v1#S2.E10 "In 2.2.1 One dimensional options ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")).
Table [5](https://arxiv.org/html/2602.09950v1#S2.T5 "Table 5 ‣ Min Butterflies ‣ 2.2.2 Bermudan options on many assets ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?") reports the prices for such an option on d=2d=2 assets. Again, the variance reduction factor is important and ranges from 16 to 400, according to the effort made to calculate M^\hat{M}. We note that λ≈0.93\lambda\approx 0.93 is quite far from 11 when M⋆M^{\star} is roughly approximated, but gets very close to 11 when more computational effort is made for the calculation of M^\hat{M}.

| Q1Q\_{1} | N¯\bar{N} | PP | LS Eq. ([8](https://arxiv.org/html/2602.09950v1#S2.E8 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) | stddev | λ\lambda | Dual | stddev |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3⋅1053\cdot 10^{5} | 1 | 10 | 2.1940 | 0.0031 | 0.9292 | 2.6744 | 0.0032 |
| 10610^{6} | 5 | 10 | 2.1943 | 0.0013 | 0.9784 | 2.4506 | 0.0012 |
| 4⋅1064\cdot 10^{6} | 10 | 10 | 2.1945 | 0.0007 | 0.9926 | 2.3891 | 0.0005 |

Table 5: Prices for a min-butterflies option with d=2d=2, σ=0.4\sigma=0.4, r=0.06r=0.06, T=0.5T=0.5, N=10N=10, S01=95S^{1}\_{0}=95 S02=90S^{2}\_{0}=90, K1=90K\_{1}=90, K2=110K\_{2}=110. LS implemented with polynomials function of order 66, Q2=Q3=50000Q\_{2}=Q\_{3}=50000. The LS price without variance reduction is 2.192.19, with a standard deviation 0.013\mathbf{0.013}.

## 3 A proxy for the optimal stopping policy

All algorithms coupling ([3](https://arxiv.org/html/2602.09950v1#S1.E3 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) and ([5](https://arxiv.org/html/2602.09950v1#S1.E5 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) tend to rely on the optimal policy obtained from the dynamic programming principle to build a dual martingale. Here, we develop a methodology to do it the other way around: use our dual algorithm and the associated martingale M^\hat{M} to build an optimal policy.
From ([6](https://arxiv.org/html/2602.09950v1#S1.E6 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")), we deduce that for n∈{0,…,N−1}n\in\{0,\dots,N-1\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Un+1|ℱn]=Un+1+(Mn⋆−Mn+1⋆).{\mathbb{E}}[U\_{n+1}|{\mathcal{F}}\_{n}]=U\_{n+1}+(M^{\star}\_{n}-M^{\star}\_{n+1}). |  | (11) |

Noting that 𝔼​[Zτn+1|ℱn]=𝔼​[𝔼​[Zτn+1|ℱn+1]|ℱn]=𝔼​[Un+1|ℱn]{\mathbb{E}}[Z\_{\tau\_{n+1}}|{\mathcal{F}}\_{n}]={\mathbb{E}}[{\mathbb{E}}[Z\_{\tau\_{n+1}}|{\mathcal{F}}\_{n+1}]|{\mathcal{F}}\_{n}]={\mathbb{E}}[U\_{n+1}|{\mathcal{F}}\_{n}], the dynamic programming equation for the optimal policy writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | {τN=Nτn=n​𝟏{Zn≥Un+1+(Mn⋆−Mn+1⋆)}+τn+1​𝟏{Zn<Un+1+(Mn⋆−Mn+1⋆)},0≤n≤N−1.\begin{cases}\tau\_{N}&=N\\ \tau\_{n}&=n{\bf 1}\_{\left\{Z\_{n}\geq U\_{n+1}+(M^{\star}\_{n}-M^{\star}\_{n+1})\right\}}+\tau\_{n+1}{\bf 1}\_{\left\{Z\_{n}<U\_{n+1}+(M^{\star}\_{n}-M^{\star}\_{n+1})\right\}},\quad 0\leq n\leq N-1.\end{cases} |  | (12) |

We also have that UU solves an other dynamic programming equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | {UN=ZNUn=max⁡(Zn,Un+1+(Mn⋆−Mn+1⋆)),0≤n≤N−1.\begin{cases}U\_{N}&=Z\_{N}\\ U\_{n}&=\max(Z\_{n},U\_{n+1}+(M^{\star}\_{n}-M^{\star}\_{n+1})),\quad 0\leq n\leq N-1.\end{cases} |  | (13) |

Note that once M⋆M^{\star} is known, ([13](https://arxiv.org/html/2602.09950v1#S3.E13 "In 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")) is fully explicit and is only useful to solve ([12](https://arxiv.org/html/2602.09950v1#S3.E12 "In 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")).

Assume we have QQ samples of (Zn(q),Mn⋆,(q))0≤n≤N(Z^{(q)}\_{n},M^{\star,(q)}\_{n})\_{0\leq n\leq N}, then we can compute the optimal policy τ1(q)\tau^{(q)}\_{1} along each path q∈{1,…,Q}q\in\{1,\dots,Q\}. So, the primal price can naturally be approximated by Monte Carlo U^0Q=1Q∑q=1QZτ1(q)(q)\hat{U}^{Q}\_{0}=\mathop{\frac{1}{Q}}\nolimits\sum\_{q=1}^{Q}Z^{(q)}\_{\tau^{(q)}\_{1}}.

From a practical point of view, M⋆M^{\star} is unknown and we can only access some approximation. For instance, we can use the martingale M^\hat{M} obtained from ([21](https://arxiv.org/html/2602.09950v1#A2.E21 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")). However, note that not only ([11](https://arxiv.org/html/2602.09950v1#S3.E11 "In 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")) does not hold anymore if we replace M⋆M^{\star} by M^\hat{M}, but the quantity Un+1+(M^n−M^n+1)U\_{n+1}+(\hat{M}\_{n}-\hat{M}\_{n+1}) may not be even ℱn−{\mathcal{F}}\_{n}- measurable. Hence, the policy obtained using M^\hat{M} instead of M⋆M^{\star} may not be a stopping time anymore. More precisely, let us define the sequence of random times (τ^n)0≤n≤N(\hat{\tau}\_{n})\_{0\leq n\leq N} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {τ^N=Nτ^n=n​𝟏{Zn≥U^n+1+(M^n−M^n+1)}+τ^n+1​𝟏{Zn<U^n+1+(M^n−M^n+1)},0≤n≤N−1,\begin{cases}\hat{\tau}\_{N}&=N\\ \hat{\tau}\_{n}&=n{\bf 1}\_{\left\{Z\_{n}\geq\hat{U}\_{n+1}+(\hat{M}\_{n}-\hat{M}\_{n+1})\right\}}+\hat{\tau}\_{n+1}{\bf 1}\_{\left\{Z\_{n}<\hat{U}\_{n+1}+(\hat{M}\_{n}-\hat{M}\_{n+1})\right\}},\quad 0\leq n\leq N-1,\end{cases} |  | (14) |

where

|  |  |  |
| --- | --- | --- |
|  | {U^N=ZNU^n=max⁡(Zn,U^n+1+(M^n−M^n+1)),0≤n≤N−1.\begin{cases}\hat{U}\_{N}&=Z\_{N}\\ \hat{U}\_{n}&=\max(Z\_{n},\hat{U}\_{n+1}+(\hat{M}\_{n}-\hat{M}\_{n+1})),\quad 0\leq n\leq N-1.\end{cases} |  |

###### Proposition 3.1.

Let M^\hat{M} be a ℱ{\mathcal{F}}-martingale and τ=inf{n≥0:U^n=Zn}\tau=\inf\{n\geq 0:\hat{U}\_{n}=Z\_{n}\}. Then, we have τ=τ^0\tau=\hat{\tau}\_{0}, Zτ−M^τ=max0≤n≤N⁡Zn−M^nZ\_{\tau}-\hat{M}\_{\tau}=\max\_{0\leq n\leq N}Z\_{n}-\hat{M}\_{n} and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Zτ−M^τ]=𝔼​[max0≤n≤N⁡Zn−M^n]≥U0.{\mathbb{E}}[Z\_{\tau}-\hat{M}\_{\tau}]={\mathbb{E}}[\max\_{0\leq n\leq N}Z\_{n}-\hat{M}\_{n}]\geq U\_{0}. |  |

###### Proof.

At first, note that U^\hat{U} may not be adapted to the filtration ℱ{\mathcal{F}}. Thus, (τ^n)n(\hat{\tau}\_{n})\_{n} may not define stopping times and U^\hat{U} may not be a Snell envelope.
However, we still have U^n−M^n=max⁡(Z^n−M^n,U^n+1−M^n+1)\hat{U}\_{n}-\hat{M}\_{n}=\max(\hat{Z}\_{n}-\hat{M}\_{n},\hat{U}\_{n+1}-\hat{M}\_{n+1}) and thus by induction

|  |  |  |  |
| --- | --- | --- | --- |
|  | U^n−M^n=maxn≤p≤N⁡Zp−M^p.\hat{U}\_{n}-\hat{M}\_{n}=\max\_{n\leq p\leq N}Z\_{p}-\hat{M}\_{p}. |  | (15) |

We then check that τ^n=inf{p≥n:U^p−M^p=Zp−M^p}\hat{\tau}\_{n}=\inf\{p\geq n:\hat{U}\_{p}-\hat{M}\_{p}=Z\_{p}-\hat{M}\_{p}\} by backward induction. This is true for n=Nn=N. For n<Nn<N, if τ^n>n\hat{\tau}\_{n}>n, then from ([14](https://arxiv.org/html/2602.09950v1#S3.E14 "In 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")) we have Zn−M^n<U^n+1−M^n+1Z\_{n}-\hat{M}\_{n}<\hat{U}\_{n+1}-\hat{M}\_{n+1} and τ^n=τ^n+1\hat{\tau}\_{n}=\hat{\tau}\_{n+1} which gives the claim by the induction assumption. Otherwise, τ^n=n\hat{\tau}\_{n}=n and thus Zn−M^n≥U^n+1−M^n+1Z\_{n}-\hat{M}\_{n}\geq\hat{U}\_{n+1}-\hat{M}\_{n+1}, which gives Zn−M^n=U^n−M^nZ\_{n}-\hat{M}\_{n}=\hat{U}\_{n}-\hat{M}\_{n} by ([15](https://arxiv.org/html/2602.09950v1#S3.E15 "In Proof. ‣ 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")). Therefore,
τ=inf{n≥0:U^n−M^n=Zn−M^n}=τ^0\tau=\inf\{n\geq 0:\hat{U}\_{n}-\hat{M}\_{n}=Z\_{n}-\hat{M}\_{n}\}=\hat{\tau}\_{0}.
Equation ([15](https://arxiv.org/html/2602.09950v1#S3.E15 "In Proof. ‣ 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?")) then gives Zτ−M^τ≥Zp−M^pZ\_{\tau}-\hat{M}\_{\tau}\geq Z\_{p}-\hat{M}\_{p} for p≥τp\geq\tau. By the last formula for τ\tau, we have U^n−M^n=U^n+1−M^n+1\hat{U}\_{n}-\hat{M}\_{n}=\hat{U}\_{n+1}-\hat{M}\_{n+1} for n<τn<\tau and thus U^τ−M^τ=U^n−M^n>Zn−M^n\hat{U}\_{\tau}-\hat{M}\_{\tau}=\hat{U}\_{n}-\hat{M}\_{n}>Z\_{n}-\hat{M}\_{n}. Therefore we have

|  |  |  |
| --- | --- | --- |
|  | Zτ−M^τ=max0≤n≤N⁡Zn−M^n,Z\_{\tau}-\hat{M}\_{\tau}=\max\_{0\leq n\leq N}Z\_{n}-\hat{M}\_{n}, |  |

and the claim follows by the dual formulation ([5](https://arxiv.org/html/2602.09950v1#S1.E5 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")).
■\blacksquare

Note that Proposition [3.1](https://arxiv.org/html/2602.09950v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?") holds for any ℱ{\mathcal{F}}-martingale M^\hat{M}. When we take for M^\hat{M} the approximation of M⋆M^{\star} given by the dual algorithm ([21](https://arxiv.org/html/2602.09950v1#A2.E21 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")), then 𝔼​[Zτ^0−M^τ^0]{\mathbb{E}}[Z\_{\hat{\tau}\_{0}}-\hat{M}\_{\hat{\tau}\_{0}}] coincides with the obtained dual price given by this algorithm.
In the particular case when M^=M⋆\hat{M}=M^{\star}, we have τ^0=τ⋆\hat{\tau}\_{0}=\tau^{\star} and therefore τ^0−τ⋆\hat{\tau}\_{0}-\tau^{\star} can be seen in general as a measure of the quality of the approximating martingale M^\hat{M}. Of course, τ⋆\tau^{\star} is not known exactly, but we use a Longstaff Schwartz algorithm to approximate it. Thus, in Figure [1](https://arxiv.org/html/2602.09950v1#S3.F1 "Figure 1 ‣ 3 A proxy for the optimal stopping policy ‣ How can the dual martingale help solving the primal optimal stopping problem?"), we plot the histograms of τ^0−τ^L​S1,Q2\hat{\tau}\_{0}-\hat{\tau}^{LS\_{1},Q\_{2}} for two different martingales M^\hat{M} on the one dimensional Put option example of Subsection [2.2.1](https://arxiv.org/html/2602.09950v1#S2.SS2.SSS1 "2.2.1 One dimensional options ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?"). We observe, as we may expect, that ℙ​(τ^0=τ^L​S1,Q2){\mathbb{P}}(\hat{\tau}\_{0}=\hat{\tau}^{LS\_{1},Q\_{2}}) is relatively high and more generally the random time τ^0\hat{\tau}\_{0} is close to the stopping time τ^L​S1,Q2\hat{\tau}^{LS\_{1},Q\_{2}}.

![Refer to caption](put_M2E06_tick20_loc50_1doptionFalse_tau.png)

![Refer to caption](tau_dual.png)

Figure 1: Histogram of τ^0−τ^L​S1,Q2\hat{\tau}\_{0}-\hat{\tau}^{LS\_{1},Q\_{2}} on the Put option example obtained with 5000050000 samples, P=50P=50 and Q2=50000Q\_{2}=50000, using the martingale M^\hat{M} obtained with N¯=20\bar{N}=20 subticks (left, with Q1=2×106Q\_{1}=2\times 10^{6}) or using the martingale M^\hat{M} that includes the European call option (right, with Q1=105Q\_{1}=10^{5}), see Equation ([22](https://arxiv.org/html/2602.09950v1#A2.E22 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")).

## Appendix A Variance decomposition in the Longstaff Schwartz algorithm

From Lelong ([2020](https://arxiv.org/html/2602.09950v1#bib.bib11), Theorem 4.5) or Lapeyre and Lelong ([2021](https://arxiv.org/html/2602.09950v1#bib.bib9), Theorem 4.10), we get the following results on the convergence of the estimator ([9](https://arxiv.org/html/2602.09950v1#S2.E9 "In 2.1 Methodology ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?")) when Q2=Q3Q\_{2}=Q\_{3}. First, for every n=1,…,Nn=1,\dots,N,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limQ→∞1Q∑q=1Q(Zτ^nL​S2,Q,(q)(q))2−(1Q∑q=1QZτ^nL​S2,Q,(q)(q))2=Var(ZτnL​S2)a.s.\lim\_{Q\to\infty}\quad\mathop{\frac{1}{Q}}\nolimits\sum\_{q=1}^{Q}\left(Z\_{\hat{\tau}\_{n}^{LS\_{2},Q,(q)}}^{(q)}\right)^{2}-\left(\mathop{\frac{1}{Q}}\nolimits\sum\_{q=1}^{Q}Z\_{\hat{\tau}\_{n}^{LS\_{2},Q,(q)}}^{(q)}\right)^{2}=\mathop{\rm Var}\nolimits(Z\_{\tau\_{n}^{LS\_{2}}})\quad a.s. |  | (16) |

The convergence rate analysis carried out in Clément et al. ([2002](https://arxiv.org/html/2602.09950v1#bib.bib5)) applies steadily to our approach. Then, under suitable assumptions, the vector

|  |  |  |
| --- | --- | --- |
|  | (Q​(1Q∑q=1QZτ^nL​S2,Q,(q)(q)−𝔼​[ZτnL​S2]))n=1,…,N\left(\sqrt{Q}\left(\mathop{\frac{1}{Q}}\nolimits\sum\_{q=1}^{Q}Z\_{\hat{\tau}\_{n}^{LS\_{2},Q,(q)}}^{(q)}-{\mathbb{E}}[Z\_{\tau^{LS\_{2}}\_{n}}]\right)\right)\_{n=1,\dots,N} |  |

converges in law to a Gaussian vector. As noted in Clément et al. ([2002](https://arxiv.org/html/2602.09950v1#bib.bib5), Theorems 4.2 and 4.3), determining the asymptotic variance directly from the data generated by a single run of the algorithm is almost impossible. From the proof of the central limit theorem for their algorithm, we have that

|  |  |  |
| --- | --- | --- |
|  | Q​(1Q∑q=1QZτ^nL​S2,Q,(q)(q)−𝔼​[ZτnL​S2])→Q→∞ℒG1+G2,\sqrt{Q}\left(\mathop{\frac{1}{Q}}\nolimits\sum\_{q=1}^{Q}Z\_{\hat{\tau}\_{n}^{LS\_{2},Q,(q)}}^{(q)}-{\mathbb{E}}[Z\_{\tau\_{n}^{LS\_{2}}}]\right)\xrightarrow[Q\to\infty]{\mathcal{L}}G\_{1}+G\_{2}, |  |

where (G1,G2)(G\_{1},G\_{2}) is a Gaussian vector. We have G1∼𝒩​(0,Var(ZτnL​S2))G\_{1}\sim\mathcal{N}(0,\mathop{\rm Var}\nolimits(Z\_{\tau\_{n}^{LS\_{2}}})) as the limit of Q​(1Q∑q=1QZτnL​S2,(q)(q)−𝔼​[ZτnL​S2])\sqrt{Q}\left(\mathop{\frac{1}{Q}}\nolimits\sum\_{q=1}^{Q}Z\_{\tau\_{n}^{LS\_{2},(q)}}^{(q)}-{\mathbb{E}}[Z\_{\tau\_{n}^{LS\_{2}}}]\right) by the standard central limit theorem. The variance of G2G\_{2} is related to the approximation of τnL​S2\tau\_{n}^{LS\_{2}} by τ^nL​S2,Q\hat{\tau}\_{n}^{LS\_{2},Q}. Then, using the empirical variance of the estimator as a measurement of the algorithm convergence misses part of the variance since from ([16](https://arxiv.org/html/2602.09950v1#A1.E16 "In Appendix A Variance decomposition in the Longstaff Schwartz algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")), we know that the empirical variance only takes into account Var(G1)\mathop{\rm Var}\nolimits(G\_{1}). Yet, on our numerical examples, the predominant part of the variance comes from G1G\_{1}: in the put example of Table [1](https://arxiv.org/html/2602.09950v1#S2.T1 "Table 1 ‣ 2.2.1 One dimensional options ‣ 2.2 Numerical examples ‣ 2 The dual martingale as a control variate for the primal problem ‣ How can the dual martingale help solving the primal optimal stopping problem?"), we have obtained Var(G1)=Var(ZτnL​S2)≈0.0506\mathop{\rm Var}\nolimits(G\_{1})=\mathop{\rm Var}\nolimits(Z\_{\tau\_{n}^{LS\_{2}}})\approx 0.0506 while our estimation of the whole variance is 0.05130.0513.

## Appendix B Calculation of M^\hat{M}: the algorithm

First, we rewrite ([5](https://arxiv.org/html/2602.09950v1#S1.E5 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")) as follows

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U0\displaystyle U\_{0} | =𝔼​[ZN]+infΔ​M1∈ℋ12,…,Δ​MN∈ℋN2∑n=0N−1𝔼​[(Zn+Δ​Mn+1−maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi})+],\displaystyle={\mathbb{E}}[Z\_{N}]+\inf\_{\Delta M\_{1}\in{\mathcal{H}}\_{1}^{2},\dots,\Delta M\_{N}\in{\mathcal{H}}\_{N}^{2}}\sum\_{n=0}^{N-1}{\mathbb{E}}\left[\left(Z\_{n}+\Delta M\_{n+1}-\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M\_{i}\right\}\right)\_{+}\right], |  | (17) |

where Δ​Mn=Mn−Mn−1\Delta M\_{n}=M\_{n}-M\_{n-1} and

|  |  |  |
| --- | --- | --- |
|  | ℋn2={Y∈𝕃2​(Ω):Y​ is real valued, ​ℱn−measurable and ​𝔼​[Y|ℱn−1]=0}.{\mathcal{H}}^{2}\_{n}=\{Y\in{\mathbb{L}}^{2}(\Omega)\,:\,Y\text{ is real valued, }{\mathcal{F}}\_{n}-\text{measurable and }{\mathbb{E}}[Y|{\mathcal{F}}\_{n-1}]=0\}. |  |

The aim of ([17](https://arxiv.org/html/2602.09950v1#A2.E17 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")) is to decompose the global optimization problem into a sequence of smaller ones. However, the lack of strict convexity of (⋅)+(\cdot)\_{+} does not allow to make this rigorous as well as to have a unique minimum. In Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)), we consider the same minimisation problem, when the positive part is replaced by a strictly convex function and obtain in particular the following result.

###### Theorem B.1.

Let M⋆∈ℍ2M^{\star}\in{\mathbb{H}}^{2} be defined by ([6](https://arxiv.org/html/2602.09950v1#S1.E6 "In 1 Introduction and framework ‣ How can the dual martingale help solving the primal optimal stopping problem?")). Then, we have for any M∈ℍ2M\in{\mathbb{H}}^{2}

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ZN]+∑n=0N−1𝔼​[(Zn+Δ​Mn+1−maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi})2]\displaystyle{\mathbb{E}}[Z\_{N}]+\sum\_{n=0}^{N-1}{\mathbb{E}}\left[\left(Z\_{n}+\Delta M\_{n+1}-\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M\_{i}\right\}\right)^{2}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥𝔼​[ZN]+∑n=0N−1𝔼​[(Zn+Δ​Mn+1⋆−maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi⋆})2],\displaystyle\geq{\mathbb{E}}[Z\_{N}]+\sum\_{n=0}^{N-1}{\mathbb{E}}\left[\left(Z\_{n}+\Delta M^{\star}\_{n+1}-\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M^{\star}\_{i}\right\}\right)^{2}\right], |  |

and M⋆M^{\star} is the unique solution of the following sequence of backward optimization problems for n=N−1,…,0n=N-1,\dots,0

|  |  |  |  |
| --- | --- | --- | --- |
|  | infΔ​Mn+1∈ℋn+12𝔼​[(Zn+Δ​Mn+1−maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi})2].\inf\_{\Delta M\_{n+1}\in{\mathcal{H}}^{2}\_{n+1}}{\mathbb{E}}\left[\left(Z\_{n}+\Delta M\_{n+1}-\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M\_{i}\right\}\right)^{2}\right]. |  | (18) |

From a practical point of view, using Theorem [B.1](https://arxiv.org/html/2602.09950v1#A2.Thmtheorem1 "Theorem B.1. ‣ Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?") to approximate M⋆M^{\star} requires to consider finite dimensional approximations ℋn2,p​r{\mathcal{H}}^{2,pr}\_{n} of ℋn2{\mathcal{H}}^{2}\_{n} for each n∈{1,…,N}n\in\{1,\dots,N\} and to replace the expectations by sample averages to effectively solve the least squares problem.

We assume that the sub-vector spaces ℋn2,p​r{\mathcal{H}}^{2,pr}\_{n}, 1≤n≤N1\leq n\leq N, are spanned by L∈ℕ∗L\in{\mathbb{N}}^{\*} random variables Δ​Xn,ℓ∈ℋn2\Delta X\_{n,\ell}\in{\mathcal{H}}^{2}\_{n}, 1≤ℓ≤L1\leq\ell\leq L:

|  |  |  |
| --- | --- | --- |
|  | ℋnp​r=Span({α⋅Δ​Xn:α∈ℝL}).{\mathcal{H}}^{pr}\_{n}=\mathop{\rm Span}\nolimits\left(\left\{\alpha\cdot\Delta X\_{n}\ :\ \alpha\in{\mathbb{R}}^{L}\right\}\right). |  |

Here, LL does not depend on nn for simplicity, and we write α⋅Δ​Xn=∑ℓ=1Lαℓ​Δ​Xn,ℓ\alpha\cdot\Delta X\_{n}=\sum\_{\ell=1}^{L}\alpha\_{\ell}\Delta X\_{n,\ell}. Then, the minimisation problem ([18](https://arxiv.org/html/2602.09950v1#A2.E18 "In Theorem B.1. ‣ Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")) becomes, for 0≤n≤N−10\leq n\leq N-1,

|  |  |  |
| --- | --- | --- |
|  | infα∈ℝL𝔼​[(Zn+α⋅Δ​Xn+1−maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi})2].\inf\_{\alpha\in{\mathbb{R}}^{L}}{\mathbb{E}}\left[\left(Z\_{n}+\alpha\cdot\Delta X\_{n+1}-\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M\_{i}\right\}\right)^{2}\right]. |  |

This is a standard least squares optimisation problem: if the positive semidefinite matrix 𝔼​[Δ​Xn+1​Δ​Xn+1T]{\mathbb{E}}[\Delta X\_{n+1}\Delta X\_{n+1}^{T}] is invertible, the minimum is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn+1\displaystyle\alpha\_{n+1} | =(𝔼​[Δ​Xn+1​Δ​Xn+1T])−1​𝔼​[(maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi}−Zn)​Δ​Xn+1]\displaystyle=\left({\mathbb{E}}[\Delta X\_{n+1}\Delta X\_{n+1}^{T}]\right)^{-1}{\mathbb{E}}\left[\left(\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M\_{i}\right\}-Z\_{n}\right)\Delta X\_{n+1}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(𝔼​[Δ​Xn+1​Δ​Xn+1T])−1​𝔼​[(maxn+1≤j≤N⁡{Zj−∑i=n+2jΔ​Mi})​Δ​Xn+1],\displaystyle=\left({\mathbb{E}}[\Delta X\_{n+1}\Delta X\_{n+1}^{T}]\right)^{-1}{\mathbb{E}}\left[\left(\max\_{n+1\leq j\leq N}\left\{Z\_{j}-\sum\_{i=n+2}^{j}\Delta M\_{i}\right\}\right)\Delta X\_{n+1}\right], |  | (19) |

since 𝔼​[Δ​Xn+1|ℱn]=0{\mathbb{E}}[\Delta X\_{n+1}|{\mathcal{F}}\_{n}]=0.

Assume that we have QQ independent paths Zn(q)Z^{(q)}\_{n} of the underlying process ZnZ\_{n} and Δ​Xn(q)\Delta X^{(q)}\_{n} of the martingale increments Δ​Xn\Delta X\_{n}, for 1≤n≤N1\leq n\leq N and 1≤q≤Q1\leq q\leq Q. If the matrix ∑q=1QΔ​Xn+1(q)​(Δ​Xn+1(q))T\sum\_{q=1}^{Q}\Delta X^{(q)}\_{n+1}(\Delta X^{(q)}\_{n+1})^{T} is invertible, then we define αn+1Q\alpha^{Q}\_{n+1} as the Monte Carlo estimator of ([19](https://arxiv.org/html/2602.09950v1#A2.E19 "In Appendix B Calculation of 𝑀̂: the algorithm ‣ How can the dual martingale help solving the primal optimal stopping problem?")) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | αn+1Q=(∑q=1QΔ​Xn+1q​(Δ​Xn+1q)T)−1​∑q=1Qmaxn+1≤j≤N⁡{Zjq−∑i=n+2jαiQ⋅Δ​Xiq}​Δ​Xn+1q\alpha\_{n+1}^{Q}=\left(\sum\_{q=1}^{Q}\Delta X^{q}\_{n+1}(\Delta X^{q}\_{n+1})^{T}\right)^{-1}\sum\_{q=1}^{Q}\max\_{n+1\leq j\leq N}\left\{Z^{q}\_{j}-\sum\_{i=n+2}^{j}\alpha^{Q}\_{i}\cdot\Delta X^{q}\_{i}\right\}\Delta X^{q}\_{n+1} |  | (20) |

From (Alfonsi et al., [2025](https://arxiv.org/html/2602.09950v1#bib.bib1), Proposition 3), αnQ→Q→∞αn\alpha\_{n}^{Q}\to\_{Q\to\infty}\alpha\_{n} a.s., so it is natural to consider the following approximation of M⋆M^{\star}

|  |  |  |  |
| --- | --- | --- | --- |
|  | M^n=∑ℓ=1nαℓQ⋅Δ​Xn.\hat{M}\_{n}=\sum\_{\ell=1}^{n}\alpha^{Q}\_{\ell}\cdot\Delta X\_{n}. |  | (21) |

Since perfect hedging is only attainable in continuous time when a martingale representation theorem holds, we suggest to use a sub-grid to parametrise the martingale increments. Each interval [Ti,Ti+1][T\_{i},T\_{i+1}] for 0≤i≤N−10\leq i\leq N-1 is split into N¯\bar{N} regular sub-intervals, and we set

|  |  |  |
| --- | --- | --- |
|  | ti,j=Ti+jN¯​TN, for ​0≤j≤N¯.t\_{i,j}=T\_{i}+\frac{j}{\bar{N}}\frac{T}{N},\text{ for }0\leq j\leq\bar{N}. |  |

We consider a family of functions up:ℝd→ℝu\_{p}:{\mathbb{R}}^{d}\to{\mathbb{R}} for p∈{1,…,P¯}p\in\{1,\dots,\bar{P}\} and a family of discounted assets (𝒜k)1≤k≤d¯({\mathcal{A}}^{k})\_{1\leq k\leq\bar{d}}. Then, we define the following elementary martingale increments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xti,jp,k−Xti,j−1p,k=ui,j−1p​(Sti,j−1)​(𝒜ti,jk−𝒜ti,j−1k).X^{{p},k}\_{t\_{i,j}}-X^{{p},k}\_{t\_{i,j-1}}=u^{p}\_{i,j-1}(S\_{t\_{i,j-1}})({\mathcal{A}}^{k}\_{t\_{i,j}}-{\mathcal{A}}^{k}\_{t\_{i,j-1}}). |  | (22) |

In this paper, we consider for ui,jpu^{p}\_{i,j} indicator functions with PP distinct intervals for each dimension (local basis) and martingales constructed only with the underlying asset i.e. d¯=d\bar{d}=d and 𝒜k=S~k{\mathcal{A}}^{k}=\tilde{S}^{k}. Other choices with polynomial functions for regression and European option claims in the hedging martingale are presented in Alfonsi et al. ([2025](https://arxiv.org/html/2602.09950v1#bib.bib1)).

## References

* Alfonsi et al. [2025]

  A. Alfonsi, A. Kebaier, and J. Lelong.
  A pure dual approach for hedging Bermudan options.
  *Mathematical Finance*, 35(4), March 2025.
  doi: 10.1111/mafi.12460.
* Andersen and Broadie [2004]

  L. Andersen and M. Broadie.
  Primal-dual simulation algorithm for pricing multidimensional American options.
  *Management Science*, 50(9):1222–1234, 2004.
  doi: 10.1287/mnsc.1040.0258.
* Belomestny et al. [2009]

  D. Belomestny, C. Bender, and J. Schoenmakers.
  True upper bounds for Bermudan products via non-nested Monte Carlo.
  *Math. Finance*, 19(1):53–71, 2009.
  ISSN 0960-1627,1467-9965.
  doi: 10.1111/j.1467-9965.2008.00357.x.
* Belomestny et al. [2019]

  D. Belomestny, R. Hildebrand, and J. Schoenmakers.
  Optimal stopping via pathwise dual empirical maximisation.
  *Appl. Math. Optim.*, 79(3):715–741, 2019.
  ISSN 0095-4616,1432-0606.
  doi: 10.1007/s00245-017-9454-9.
* Clément et al. [2002]

  E. Clément, D. Lamberton, and P. Protter.
  An analysis of a least squares regression method for American option pricing.
  *Finance Stoch.*, 6(4):449–471, 2002.
  ISSN 0949-2984,1432-1122.
  doi: 10.1007/s007800200071.
* Desai et al. [2012]

  V. V. Desai, V. F. Farias, and C. C. Moallemi.
  Pathwise optimization for optimal stopping problems.
  *Management Science*, 58(12):2292–2308, 2012.
  doi: 10.1287/mnsc.1120.1551.
* Haugh and Kogan [2004]

  M. B. Haugh and L. Kogan.
  Pricing American options: a duality approach.
  *Oper. Res.*, 52(2):258–270, 2004.
  ISSN 0030-364X,1526-5463.
  doi: 10.1287/opre.1030.0070.
* Juneja and Kalra [2009]

  S. Juneja and H. Kalra.
  Variance reduction techniques for pricing American options using function approximations.
  *J. Comput. Finance*, 12(3):79–102, 2009.
  ISSN 1460-1559,1755-2850.
  doi: 10.21314/JCF.2009.208.
* Lapeyre and Lelong [2021]

  B. Lapeyre and J. Lelong.
  Neural network regression for Bermudan option pricing.
  *Monte Carlo Methods Appl.*, 27(3):227–247, July 2021.
  doi: 10.1515/mcma-2021-2091.
* Lelong [2018]

  J. Lelong.
  Dual pricing of American options by Wiener chaos expansion.
  *SIAM J. Financial Math.*, 9(2):493–519, 2018.
  doi: 10.1137/16M1102161.
* Lelong [2020]

  J. Lelong.
  Pricing path-dependent Bermudan options using Wiener chaos expansion: an embarrassingly parallel approach.
  *Journal of Computational Finance*, 24(2), 2020.
  doi: 10.21314/JCF.2020.394.
* Longstaff and Schwartz [2001]

  F. A. Longstaff and E. S. Schwartz.
  Valuing American options by simulation: a simple least-squares approach.
  *The Review of Financial Studies*, 14(1):113–147, 2001.
* Rogers [2002]

  L. C. G. Rogers.
  Monte Carlo valuation of American options.
  *Math. Finance*, 12(3):271–286, 2002.