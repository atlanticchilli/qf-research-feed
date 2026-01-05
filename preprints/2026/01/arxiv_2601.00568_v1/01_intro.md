---
authors:
- Enrique Calderín-Ojeda
- Yuyu Chen
- Soon Wei Tan
doc_id: arxiv:2601.00568v1
family_id: arxiv:2601.00568
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Capital allocation and tail central moments for the multivariate normal mean-variance
  mixture distribution
url_abs: http://arxiv.org/abs/2601.00568v1
url_html: https://arxiv.org/html/2601.00568v1
venue: arXiv q-fin
version: 1
year: 2026
---


Enrique Calderín-Ojeda
Department of Economics, University of Melbourne, Australia.
✉ <enrique.calderin@unimelb.edu.au>
  
Yuyu Chen
Department of Economics, University of Melbourne, Australia.
✉ <yuyu.chen@unimelb.edu.au>
  
Soon Wei Tan
Department of Economics, University of Melbourne, Australia. ✉ <soonweit@student.unimelb.edu.au>Corresponding author

###### Abstract

Capital allocation is a procedure used to assess the risk contributions of individual risk components to the total risk of a portfolio. While the conditional tail expectation (CTE)-based capital allocation is arguably the most popular capital allocation method, its inability to reflect important tail behaviour of losses necessitates a more accurate approach. In this paper, we introduce a new capital allocation method based on the tail central moments (TCM), generalising the tail covariance allocation informed by the tail variance. We develop analytical expressions of the TCM as well as the TCM-based capital allocation for the class of normal mean-variance mixture distributions, which is widely used to model asymmetric and heavy-tailed data in finance and insurance. As demonstrated by a numerical analysis, the TCM-based capital allocation captures several significant patterns in the tail region of equity losses that remain undetected by the CTE, enhancing the understanding of the tail risk contributions of risk components.

Keywords: Capital allocation; tail central moments; tail variance; normal mean–variance mixture distribution.

## 1 Introduction

Risk assessment is a core task in finance and insurance. For an agent who manages a portfolio consisting of multiple assets, a common procedure is capital allocation. This is usually achieved through two main steps. Firstly, the agent decides on a total capital reserve based on their risk preferences. Secondly, the capital reserve is distributed across all individual assets in a way that reflects their risk contributions. Capital allocation has broader purposes than its literal meaning of physically allocating capital to each asset, such as deciding portfolio weights, comparing asset profitability, and so on. For discussions on various capital allocation principles, properties, and applications, see, e.g., D01, K05, D12, G21, and references therein.

Risk measure, which maps a random loss to a real number, is a common tool to determine the capital reserve for financial institutions. One of the regulatory risk measures used in the realms of banking and insurance is the conditional tail expectation (CTE); see, e.g., M15. The CTE satisfies the so-called coherence properties that a desirable risk measure should fulfil (A99 and D01). Consequently, the CTE-based capital allocation can effectively capture the diversification benefits in a portfolio, making it the most important case of the Euler allocation principle (e.g., D01, T04, and T08). Moreover, the CTE-based capital allocation arises as a special case of the optimisation approach to capital allocation as shown in, e.g., LG04 and D12.

Despite the various advantages of the CTE and its allocation method, it has been pointed out that the CTE cannot capture sufficient tail behaviour of the loss distribution. Under severely unfavourable conditions, the actual loss may far exceed the agent’s capital reserves based on the CTE. Therefore, this has led to suggestions to supplement the CTE with higher order moments for a more comprehensive evaluation of a portfolio’s risk characteristics. In the finance literature, higher moments, most notably skewness and kurtosis, are commonly used in risk assessment; see, e.g., S70, S01, H10, and AP18. In the context of capital allocation, the most prominent consideration is the tail variance (TV) (see, e.g., V04 and FL06). However, to our best knowledge, research on capital allocation with the TV is scarce, and no studies have yet considered capital allocation with other tail moments of higher order.

To address this gap in the literature, we first introduce a new capital allocation method based on the tail central moments (TCM), generalising the tail covariance-based capital allocation of V04 and FL06. Secondly, we derive recursive analytical expressions of the TCM and the TCM-based capital allocation for the general class of multivariate normal mean-variance mixture (NMVM) distributions (Theorems [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") and [2](https://arxiv.org/html/2601.00568v1#Thmtheorem2 "Theorem 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")). The NMVM class is known to be extremely flexible and contains many notable members (M15). One such example is the generalised hyperbolic (GH) distribution, which itself includes the normal, skewed student-tt, variance Gamma, normal inverse Gaussian, hyperbolic, and other renowned distributions as special cases. The GH distribution is well recognised for its effectiveness in modelling financial and actuarial data due to its connections with the Lévy process, especially one that exhibits tail behaviour and asymmetry (see, e.g., EK95, N09, and KW14).

This paper contributes to the rich literature of capital allocation for multivariate distributions. The literature on the CTE-based capital allocation is extensive and well-developed. P02 derived the CTE-based capital allocation for the multivariate normal distribution. This result was later expanded in different directions. One direction considers distributions with heavy tails, such as the elliptical distribution and its extensions (LV03, IL21, and IL25), the GH distribution (IL15 and IL19), and the NMVM class (KK19). Other directions focus on skewed distributions and compound distributions, see, e.g., V06 for the CTE-based capital allocation of skewed distributions and FL10 and D20 for that of compound distributions. On the contrary, only a few studies have examined the TV-based capital allocation, such as V04 for the normal distribution, V05 and FL06 for the elliptical distribution, L13 for the lognormal distribution, and e.g., W14 and R22 for other applications. Our results broadly contribute to the literature by introducing a novel TCM-based capital allocation to enhance the accuracy of risk assessment. In particular, our results complement those of KK19.

The remainder of this paper is organised as follows. Section [2](https://arxiv.org/html/2601.00568v1#S2 "2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") introduces the TCM-based capital allocation method and the NMVM class. In Section [3](https://arxiv.org/html/2601.00568v1#S3 "3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), recursive analytical expressions for the TCM of the univariate NMVM distribution are derived. Section [4](https://arxiv.org/html/2601.00568v1#S4 "4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") applies the TCM-based capital allocation to the multivariate NMVM class to obtain explicit expressions for the capital allocated to each component. Section [5](https://arxiv.org/html/2601.00568v1#S5 "5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") illustrates our theoretical findings with a numerical example based on the multivariate GH distribution. Section [6](https://arxiv.org/html/2601.00568v1#S6 "6 Conclusion ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") concludes.

### Notation

Denote by ℕ0\mathbb{N}\_{0} (resp. ℕ\mathbb{N} and ℝ+\mathbb{R}\_{+}) the set of non-negative integers (resp. positive integers and non-negative real numbers). All vectors are column vectors. For a random variable XX, we denote by fX,FX,F¯Xf\_{X},F\_{X},{\overline{F}}\_{X}, and hXh\_{X} its density, cumulative distribution, survival and hazard functions, respectively (with hX​(x)=fX​(x)/F¯X​(x)h\_{X}(x)=f\_{X}(x)/{\overline{F}}\_{X}(x) for x∈ℝx\in\mathbb{R}). For α∈(0,1)\alpha\in(0,1), the quantile of a random variable XX is denoted by xα:=inf{x∈ℝ:ℙ​(X≤x)≥α}x\_{\alpha}:=\inf\left\{x\in\mathbb{R}:\mathbb{P}(X\leq x)\geq\alpha\right\}. Whenever we consider the kk-th moment of a random variable XX, we assume that 𝔼​[|X|k]<∞\mathbb{E}[|X|^{k}]<\infty, where k∈ℕk\in\mathbb{N}.

## 2 Preliminaries

In this section, we review the definitions of tail moments, capital allocation methods, and the multivariate normal mean-variance mixture distribution. In particular, we introduce a capital allocation method based on the tail central moments.

### 2.1 Tail moments and tail central moments

The tail moments (TM) and tail central moments (TCM), especially of orders 1 or 2, are commonly used in the literature of capital allocation (see, e.g., O00, V04, and KK19).

###### Definition 1.

Fix k∈ℕk\in\mathbb{N} and α∈(0,1)\alpha\in(0,1). For a random variable XX, the kk-th order tail moment (TM) at confidence level α\alpha is defined as

|  |  |  |
| --- | --- | --- |
|  | TMα,k​(X):=𝔼​[Xk​∣X>​xα].\displaystyle\mathrm{TM}\_{\alpha,k}(X):=\mathbb{E}\left[X^{k}\mid X>x\_{\alpha}\right]. |  |

When k=1k=1, the TM is referred to as the conditional tail expectation (CTE), denoted by CTEα​(X)\mathrm{CTE}\_{\alpha}(X).

###### Definition 2.

Fix k∈ℕk\in\mathbb{N} and α∈(0,1)\alpha\in(0,1). For a random variable XX, the kk-th order tail central moment (TCM) at confidence level α\alpha is defined as

|  |  |  |
| --- | --- | --- |
|  | TCMα,k​(X):=𝔼​[(X−CTEα​(X))k​∣X>​xα].\displaystyle\mathrm{TCM}\_{\alpha,k}(X):=\mathbb{E}\left[\left(X-\mathrm{CTE}\_{\alpha}(X)\right)^{k}\mid X>x\_{\alpha}\right]. |  |

When k=2k=2, the TCM is referred to as the tail variance (TV).

###### Remark 1.

There has been some inconsistency regarding the terminologies of the TM and TCM. The TM and TCM have been referred to as the Tail Conditional Moment in the literature (see, e.g., K10 and H19 for the TM and EK21 for the TCM). When considering an aggregate risk S=X1+⋯+XnS=X\_{1}+\dots+X\_{n}, L23 and Y25 define 𝔼​[Xik​∣S>​sα]\mathbb{E}\left[X^{k}\_{i}\mid S>s\_{\alpha}\right] and 𝔼​[(Xi−CTEα​(Xi))k​∣S>​sα]\mathbb{E}\left[(X\_{i}-\mathrm{CTE}\_{\alpha}(X\_{i}))^{k}\mid S>s\_{\alpha}\right] as the TM and TCM instead.

###### Remark 2.

Another approach to generalising the CTE is via stochastic optimisation formulas, often with desirable properties preserved. For instance, K07 and G22 considered ρ​(X)=infx∈ℝ{x+(1−q)−1​ϕ​(max⁡(X−x,0))}\rho(X)=\inf\_{x\in\mathbb{R}}\left\{x+(1-q)^{-1}\phi(\max(X-x,0))\right\}, with ϕ​(X)=𝔼​[|X|p]1/p\phi(X)=\mathbb{E}\left[|X|^{p}\right]^{1/p} and for some p≥1p\geq 1, q∈(0,1)q\in(0,1), which is named as the higher moment risk measure. When p=1p=1 and FXF\_{X} is differentiable, we recover the CTE representation in RU00.

### 2.2 Tail central moment-based capital allocation

In practice, financial institutions are usually exposed to a portfolio of losses rather than a single loss. The portfolio may consist of policyholders, business lines, or investment assets, depending on the nature of the financial institution. Throughout this paper, we consider an agent with n∈ℕn\in\mathbb{N} random losses X1,…,XnX\_{1},\dots,X\_{n} and denote by S=X1+⋯+XnS=X\_{1}+\dots+X\_{n} its aggregate loss. After determining the total capital reserve of the aggregate loss SS, a common practice is to allocate the risk capital to individual losses. Let K∈ℝK\in\mathbb{R} be the total capital reserve for SS, and Ki∈ℝK\_{i}\in\mathbb{R} be the capital allocated to XiX\_{i} for i=1,…,ni=1,\dots,n. A capital allocation method is said to satisfy the full allocation property if

|  |  |  |
| --- | --- | --- |
|  | K=∑i=1nKi.\displaystyle K=\sum^{n}\_{i=1}K\_{i}. |  |

One popular capital allocation method is the CTE-based capital allocation, which specifies that

|  |  |  |
| --- | --- | --- |
|  | K=CTEα​(S)​ and ​Ki=𝔼​[Xi​∣S>​sα]​ for all ​i=1,…,n.\displaystyle K=\mathrm{CTE}\_{\alpha}(S)\mbox{~~and~~}K\_{i}=\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mbox{~~for all~~}i=1,\dots,n. |  |

It is easy to see that it fulfils the full allocation property. As a coherent allocation principle (see D01) with a simple expression, it has received much interest since its introduction in, e.g., O00. Nonetheless, the CTE-based capital allocation has certain limitations. In particular, the CTE alone is insufficient in capturing the tail behaviour of losses (e.g., dispersion), which can be crucial to risk management. To address these concerns, we introduce a new class of TCM-based capital allocation methods and discuss some of its properties.

###### Definition 3.

For k∈ℕ∖{1}k\in\mathbb{N}\setminus\left\{1\right\}, the kk-th order TCM-based capital allocation with confidence level α∈(0,1)\alpha\in(0,1) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K=TCMα,k​(S)​ and ​Ki=Cov​[Xi,(S−CTEα​(S))k−1​∣S>​sα]​ for all ​i=1,…,n.\displaystyle K=\mathrm{TCM}\_{\alpha,k}(S)\mbox{~~and~~}K\_{i}=\mathrm{Cov}\left[X\_{i},\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right]\mbox{~~for all~~}i=1,\dots,n. |  | (1) |

The TCM-based capital allocation provides direct interpretations of the risk contributions of individual losses to the aggregate loss. For instance, if k=2k=2, the TCM-based capital allocation method recovers the TV-based capital allocation111It is referred to as the tail covariance-based capital allocation in V04 and FL06. in V04 and FL06, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Ki=Cov​[Xi,S​∣S>​sα]​ for all ​i=1,…,n.\displaystyle K\_{i}=\mathrm{Cov}\left[X\_{i},S\mid S>s\_{\alpha}\right]\mbox{~~for all~~}i=1,\dots,n. |  |

The TV-based capital allocation thus quantifies the dependence between individual losses and the aggregate loss in tail regions. The TCM-based capital allocation can also capture relationships between the aggregate tail dispersion and each component. One example is k=3k=3, with

|  |  |  |
| --- | --- | --- |
|  | Ki=Cov​[Xi,(S−CTEα​(S))2​∣S>​sα]​ for all ​i=1,…,n.\displaystyle K\_{i}=\mathrm{Cov}\left[X\_{i},\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{2}\mid S>s\_{\alpha}\right]\mbox{~~for all~~}i=1,\dots,n. |  |

Note that the TCM-based capital allocation can be negative, which shows a diversification benefit.

###### Proposition 1.

The TCM-based capital allocation satisfies the full allocation property.

###### Proof.

Let Sα=S−CTEα​(S)S\_{\alpha}=S-\mathrm{CTE}\_{\alpha}(S). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nKi=\displaystyle\sum^{n}\_{i=1}K\_{i}= | ∑i=1nCov​[Xi,(S−CTEα​(S))k−1​∣S>​sα]\displaystyle~\sum^{n}\_{i=1}\mathrm{Cov}\left[X\_{i},\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1n(𝔼​[Xi​Sαk−1​∣S>​sα]−𝔼​[Xi​∣S>​sα]​𝔼​[Sαk−1​∣S>​sα])\displaystyle~\sum^{n}\_{i=1}\left(\mathbb{E}\left[X\_{i}S\_{\alpha}^{k-1}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S\_{\alpha}^{k-1}\mid S>s\_{\alpha}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[∑i=1nXi​Sαk−1​∣S>​sα]−𝔼​[Sαk−1​∣S>​sα]​∑i=1n𝔼​[Xi​∣S>​sα]\displaystyle~\mathbb{E}\left[\sum^{n}\_{i=1}X\_{i}S\_{\alpha}^{k-1}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[S\_{\alpha}^{k-1}\mid S>s\_{\alpha}\right]\sum^{n}\_{i=1}\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[S​(S−CTEα​(S))k−1​∣S>​sα]−𝔼​[CTEα​(S)​(S−CTEα​(S))k−1​∣S>​sα]\displaystyle~\mathbb{E}\left[S\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[\mathrm{CTE}\_{\alpha}(S)\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[(S−CTEα​(S))k​∣S>​sα]=K.∎\displaystyle~\mathbb{E}\left[\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k}\mid S>s\_{\alpha}\right]=K.\qed |  |

As the CTE alone does not adequately characterise the tail behaviour of losses, it is worth considering linear combinations of the CTE-based and TCM-based capital allocation methods. For instance, an overall capital reserve of

|  |  |  |  |
| --- | --- | --- | --- |
|  | K=m1​CTEα​(S)+m2​TVα​(S)+m3​TCMα,3​(S),\displaystyle K=m\_{1}\mathrm{CTE}\_{\alpha}(S)+m\_{2}\mathrm{TV}\_{\alpha}(S)+m\_{3}\mathrm{TCM}\_{\alpha,3}(S), |  | (2) |

for some m1,m2,m3∈ℝ+m\_{1},m\_{2},m\_{3}\in\mathbb{R}\_{+}, not only measures the average tail loss, but also takes into account other characteristics of the tail region such as dispersion and asymmetry. The corresponding capital allocation is feasible due to linearity. The combination allows a lot of flexibility to the agent when deciding their portfolio management priorities. The idea of combining the CTE and TV has been considered by, e.g., FL06, IL15, and KK19 as a premium principle for the entire portfolio, with only FL06 applying it to capital allocation. We extend this idea by including the 3rd order TCM as well, and demonstrate it via a real-data analysis in Section [5](https://arxiv.org/html/2601.00568v1#S5 "5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution").

###### Remark 3.

The Euler allocation principle is a popular capital allocation method. This is because it possesses the full allocation property as well as other desirable properties, and it aligns with concepts from other disciplines such as economics and game theory (see Section 2.2 of T08 and references therein for detailed discussions). While the TCM does not fulfil the conditions for the Euler allocation principle, we can modify it by “rooting” the TCM so that the Euler allocation principle can be applied under mild assumptions of the random losses, with the following allocation outcome:

|  |  |  |
| --- | --- | --- |
|  | K=TCMα,k​(S)1k​ and ​Ki=Cov​[Xi,(S−CTEα​(S))k−1​∣S>​sα]TCMα,k​(S)1−1k​ for all ​i=1,…,n;\displaystyle K=\mathrm{TCM}\_{\alpha,k}(S)^{\frac{1}{k}}\mbox{~~and~~}K\_{i}=\frac{\mathrm{Cov}\left[X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mid S>s\_{\alpha}\right]}{\mathrm{TCM}\_{\alpha,k}(S)^{1-\frac{1}{k}}}\mbox{~~for all~~}i=1,\dots,n; |  |

see Appendix [A](https://arxiv.org/html/2601.00568v1#A1 "Appendix A The TCM-based Euler allocation principle ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") for the derivation of this result. Clearly, switching between ([1](https://arxiv.org/html/2601.00568v1#S2.E1 "In Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) and the above has no additional computational difficulty. Moving forward, ([1](https://arxiv.org/html/2601.00568v1#S2.E1 "In Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) in Definition [3](https://arxiv.org/html/2601.00568v1#Thmdefinition3 "Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") will be used for its neater expressions. The case when k=2k=2, together with the CTE-based capital allocation, is studied in FL06 and G21 as the risk-adjusted tail value-at-risk allocation method.

### 2.3 Normal mean-variance mixture distributions

The following definition follows Definition 3.11 of M15.

###### Definition 4.

A random vector 𝐗\mathbf{X} is said to follow an nn-dimensional normal mean-variance mixture (NMVM) distribution if

|  |  |  |
| --- | --- | --- |
|  | 𝐗​=𝑑​𝐦​(Θ)+Θ​A​𝐙,\displaystyle\mathbf{X}\overset{d}{=}\mathbf{m}(\Theta)+\sqrt{\Theta}A\mathbf{Z}, |  |

where

1. (i)

   𝐙∼M​V​Nk​(𝟎,𝐈𝐤)\mathbf{Z}\sim MVN\_{k}(\mathbf{0},\mathbf{I\_{k}}) is a kk-dimensional standard multivariate normal random vector with the identity variance-covariance matrix;
2. (ii)

   A∈ℝn×kA\in\mathbb{R}^{n\times k} is a matrix;
3. (iii)

   Θ\Theta is a non-negative random variable, independent of 𝐙\mathbf{Z}, with density function π​(θ)\pi(\theta) for θ>0\theta>0. It is referred to as the mixing random variable;
4. (iv)

   𝐦:[0,∞)→ℝn\mathbf{m}:[0,\infty)\rightarrow\mathbb{R}^{n} is a measurable function of Θ\Theta.

Throughout this paper, we assume that 𝐦​(Θ)=𝝁+Θ​𝜸\mathbf{m}(\Theta)=\bm{\mu}+\Theta\bm{\gamma} where 𝝁,𝜸∈ℝn\bm{\mu},\bm{\gamma}\in\mathbb{R}^{n}. Let Σ:=A​A′=(σi​j)1≤i,j≤n\Sigma:=AA^{\prime}=({\sigma}\_{ij})\_{1\leq i,j\leq n}. We will specify an NMVM random variable (or its distribution) via the parameters 𝝁,𝜸\bm{\mu},\bm{\gamma}, and Σ\Sigma, and the mixing random variable Θ\Theta. For a univariate NMVM random variable, we write the parameters as μ:=𝝁\mu:=\bm{\mu}, γ:=𝜸\gamma:=\bm{\gamma}, and σ2:=Σ{\sigma}^{2}:=\Sigma.

We present below some useful properties of the NMVM distribution. First, it is clear that

|  |  |  |
| --- | --- | --- |
|  | 𝐗∣Θ=θ∼MVNn(𝐦(θ),θΣ)).\displaystyle\mathbf{X}\mid\Theta=\theta\sim MVN\_{n}\left(\mathbf{m}(\theta),\theta\Sigma)\right). |  |

Second, the class of NMVM distributions is closed under linear transformations (see, e.g., Proposition 2.1 of KK19). This is a useful property with many financial applications, such as when portfolio weights are concerned. In particular, it follows that S=X1+⋯+XnS=X\_{1}+\dots+X\_{n} is an NMVM random variable with mixing random variable Θ\Theta and parameters μ=𝟏′​𝝁,σ2=𝟏′​𝚺​𝟏,\mu=\mathbf{1^{\prime}}\bm{\mu},{\sigma}^{2}=\mathbf{1^{\prime}\Sigma 1}, and γ=𝟏′​𝜸\gamma=\mathbf{1^{\prime}}\bm{\gamma}. In general, NMVM distributions are not elliptical, and 𝝁\bm{\mu} and Σ\Sigma are not the mean vector and covariance matrix of 𝐗\mathbf{X}.

The NMVM class contains many important distributions, one of which is the generalised hyperbolic (GH) distribution, where Θ\Theta follows a generalised inverse Gaussian (GIG) distribution with three parameters λ∈ℝ\lambda\in\mathbb{R} and χ,ψ≥0\chi,\psi\geq 0. We denote a nn-dimensional multivariate GH distribution by M​G​Hn​(λ,χ,ψ,𝝁,𝚺,𝜸)MGH\_{n}(\lambda,\ \chi,\ \psi,\ \bm{\mu},\ \bm{\Sigma},\ \bm{\gamma}). The density of the GIG distribution is given by

|  |  |  |
| --- | --- | --- |
|  | π​(θ)=χ−λ​(χ​ψ)λ2​𝒦λ​(χ​ψ)​θλ−1​exp⁡(−12​(χ​θ−1+ψ​θ)),θ>0,\displaystyle\pi(\theta)=\frac{\chi^{-\lambda}(\sqrt{\chi\psi})^{\lambda}}{2\mathcal{K}\_{\lambda}(\chi\psi)}\theta^{\lambda-1}\exp\left(-\frac{1}{2}(\chi\theta^{-1}+\psi\theta)\right),~~\theta>0, |  |

where 𝒦λ\mathcal{K}\_{\lambda} is a modified Bessel function of the second kind with index λ\lambda:

|  |  |  |
| --- | --- | --- |
|  | 𝒦λ​(z)=12​∫0∞xλ−1​e−12​z​(x−1+x)​𝑑x.\displaystyle\mathcal{K}\_{\lambda}(z)=\frac{1}{2}\int^{\infty}\_{0}x^{\lambda-1}e^{-\frac{1}{2}z(x^{-1}+x)}\,dx. |  |

The parameters need to satisfy one of: χ>0,ψ≥0\chi>0,\psi\geq 0 when λ<0\lambda<0; χ>0,ψ>0\chi>0,\psi>0 when λ=0\lambda=0; χ≥0,ψ>0\chi\geq 0,\psi>0 when λ>0\lambda>0. The GIG distribution itself contains the Gamma and inverse Gamma as special cases, and the GH class has several notable members, as listed in the introduction. For more information about the GIG and GH distributions, refer to J82 or Section 6.2.3 of M15.

## 3 Tail moments of univariate NMVM distributions

In this section, we derive an analytical solution to the TCM of the aggregate loss SS faced by the agent as outlined at the start of Section [2.2](https://arxiv.org/html/2601.00568v1#S2.SS2 "2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). The model setup and assumptions for Sections [3](https://arxiv.org/html/2601.00568v1#S3 "3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") and [4](https://arxiv.org/html/2601.00568v1#S4 "4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") are as follows:

1. (i)

   The losses X1,…,XnX\_{1},\dots,X\_{n} follow the multivariate NMVM distribution (Definition [4](https://arxiv.org/html/2601.00568v1#Thmdefinition4 "Definition 4. ‣ 2.3 Normal mean-variance mixture distributions ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"));
2. (ii)

   As the NMVM model is closed under linear combinations, the aggregate loss SS follows a univariate NMVM distribution with mixing random variable Θ\Theta and parameters μ=𝟏′​𝝁\mu=\mathbf{1^{\prime}}\bm{\mu}, σ2=𝟏′​𝚺​𝟏{\sigma}^{2}=\mathbf{1^{\prime}\Sigma 1}, and γ=𝟏′​𝜸\gamma=\mathbf{1^{\prime}}\bm{\gamma};
3. (iii)

   Fix l∈ℕ0l\in\mathbb{N}\_{0}. We assume that there always exists some c∗(l)>0c^{\*(l)}>0 such that π∗(l)​(θ):=(c∗(l))−1​θl​π​(θ)\pi^{\*(l)}(\theta):=(c^{\*(l)})^{-1}\theta^{l}\pi(\theta) is a valid density function. Let c∗c^{\*} and π∗​(θ)\pi^{\*}(\theta) (resp. c∗∗c^{\*\*} and π∗∗​(θ)\pi^{\*\*}(\theta)) be the shorthand notation of c∗(l)c^{\*(l)} and π∗(l)​(θ)\pi^{\*(l)}(\theta) for l=1l=1 (resp. l=2l=2).
4. (iv)

   Denote by S∗(l)S^{\*(l)} an NMVM random variable with the same parameters as SS, except that the density of its mixing random variable is π∗(l)​(θ)\pi^{\*(l)}(\theta). Define α∗(l)=1−F¯S∗(l)​(sα)\alpha^{\*(l)}=1-{\overline{F}}\_{S^{\*(l)}}(s\_{\alpha}) for some α∈(0,1)\alpha\in(0,1). Let S∗S^{\*} and α∗\alpha^{\*} (resp. S∗∗S^{\*\*} and α∗∗\alpha^{\*\*}) be the shorthand notation of S∗(l)S^{\*(l)} and α∗(l)\alpha^{\*(l)} for l=1l=1 (resp. l=2l=2).

Based on (ii) above, the task in this section reduces to finding the TCM of a univariate NMVM distribution. The solution is achieved through a recursive approach. As a necessary step in calculating the TCM, we also provide recursive formulas for the TM. As a direct consequence, we obtain an explicit formula for the 2nd order TM and TCM of SS, studied by KK19, using different techniques.

We first provide the following results, which will be useful in the derivation of Theorem [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution").

###### Lemma 1.

(LV16, Example 3.1)
Fix k∈ℕk\in\mathbb{N}, μ∈ℝ\mu\in\mathbb{R}, and c,σ∈ℝ+c,\ {\sigma}\in\mathbb{R}\_{+}. For a random variable X∼N​(μ,σ2)X\sim N(\mu,{\sigma}^{2}), the kk-th order TM of XX follows the recursive relationship

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xk​∣X>​c]=σ2​ck−1​fX​(c)F¯X​(c)+μ​𝔼​[Xk−1​∣X>​c]+(k−1)​σ2​𝔼​[Xk−2​∣X>​c].\displaystyle\mathbb{E}\left[X^{k}\mid X>c\right]={\sigma}^{2}c^{k-1}\frac{f\_{X}(c)}{{\overline{F}}\_{X}(c)}+\mu\mathbb{E}\left[X^{k-1}\mid X>c\right]+(k-1){\sigma}^{2}\mathbb{E}\left[X^{k-2}\mid X>c\right]. |  | (3) |

###### Lemma 2.

For some fixed k∈ℕk\in\mathbb{N}, l∈ℕ0l\in\mathbb{N}\_{0}, and α∈(0,1)\alpha\in(0,1), we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(S∗(l))k​∣S∗(l)>​sα]=11−α∗(l)​∫0∞F¯S∗(l)|θ​(sα)​𝔼​[(S∗(l))k​∣S∗(l)>​sα,Θ=θ]​π∗(l)​(θ)​𝑑θ.\displaystyle\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha}\right]=\frac{1}{1-\alpha^{\*(l)}}\int^{\infty}\_{0}{\overline{F}}\_{S^{\*(l)}|\theta}(s\_{\alpha})\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha},\Theta=\theta\right]\pi^{\*(l)}(\theta)\,d\theta. |  |

###### Proof.

Let random variable Θ∗(l)\Theta^{\*(l)} have density π∗(l)​(θ)\pi^{\*(l)}(\theta), with θ>0\theta>0. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(S∗(l))k​∣S∗(l)>​sα]=\displaystyle\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha}\right]= | 11−α∗(l)​∫sα∞sk​fS∗(l)​(s)​𝑑s\displaystyle~\frac{1}{1-\alpha^{\*(l)}}\int^{\infty}\_{s\_{\alpha}}s^{k}f\_{S^{\*(l)}}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α∗(l)​∫sα∞sk​∫0∞fS∗(l),Θ∗(l)​(s,θ)​𝑑θ​𝑑s\displaystyle~\frac{1}{1-\alpha^{\*(l)}}\int^{\infty}\_{s\_{\alpha}}s^{k}\int^{\infty}\_{0}f\_{S^{\*(l)},\Theta^{\*(l)}}(s,\theta)\,d\theta\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α∗(l)​∫sα∞∫0∞sk​fS∗(l)|θ​(s)​π∗(l)​(θ)​𝑑θ​𝑑s\displaystyle~\frac{1}{1-\alpha^{\*(l)}}\int^{\infty}\_{s\_{\alpha}}\int^{\infty}\_{0}s^{k}f\_{S^{\*(l)}|\theta}(s)\pi^{\*(l)}(\theta)\,d\theta\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α∗(l)​∫0∞F¯S∗(l)|θ​(sα)​(1F¯S∗(l)|θ​(sα)​∫sα∞sk​fS∗(l)|θ​(s)​𝑑s)​π∗(l)​(θ)​𝑑θ\displaystyle~\frac{1}{1-\alpha^{\*(l)}}\int^{\infty}\_{0}{\overline{F}}\_{S^{\*(l)}|\theta}(s\_{\alpha})\left(\frac{1}{{\overline{F}}\_{S^{\*(l)}|\theta}(s\_{\alpha})}\int^{\infty}\_{s\_{\alpha}}s^{k}f\_{S^{\*(l)}|\theta}(s)\,ds\right)\pi^{\*(l)}(\theta)\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α∗(l)​∫0∞F¯S∗(l)|θ​(sα)​𝔼​[(S∗(l))k​∣S∗(l)>​sα,Θ∗(l)]=θ​d​θ​π∗(l)​(θ).∎\displaystyle~\frac{1}{1-\alpha^{\*(l)}}\int^{\infty}\_{0}{\overline{F}}\_{S^{\*(l)}|\theta}(s\_{\alpha})\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha},\Theta^{\*(l)}\right]=\theta\,d\theta\pi^{\*(l)}(\theta).\qed |  |

Now we state our main result for the TM and TCM of the NMVM random variable SS.

###### Theorem 1.

For k∈ℕk\in\mathbb{N}, the kk-th order TM and TCM of the NMVM random variable SS at confidence level α∈(0,1)\alpha\in(0,1) can be found recursively by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Sk​∣S>​sα]=\displaystyle\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]= | μ​𝔼​[Sk−1​∣S>​sα]+1−α∗1−α​c∗​σ2​sαk−1​hS∗​(sα)\displaystyle~\mu\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}s\_{\alpha}^{k-1}h\_{S^{\*}}(s\_{\alpha}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1−α∗1−α​c∗​(γ​𝔼​[(S∗)k−1​∣S∗>​sα]+(k−1)​σ2​𝔼​[(S∗)k−2​∣S∗>​sα]),\displaystyle~~+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left(\gamma\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right]+(k-1){\sigma}^{2}\mathbb{E}\left[(S^{\*})^{k-2}\mid S^{\*}>s\_{\alpha}\right]\right), |  | (4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(S∗(l))k​∣S∗(l)>​sα]=\displaystyle\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha}\right]= | μ​𝔼​[(S∗(l))k−1​∣S∗(l)>​sα]+(1−α∗(l+1))​c∗(l+1)(1−α∗(l))​c∗(l)​σ2​sαk−1​hS∗(l+1)​(sα)\displaystyle~\mu\mathbb{E}\left[(S^{\*(l)})^{k-1}\mid S^{\*(l)}>s\_{\alpha}\right]+\frac{(1-\alpha^{\*(l+1)})c^{\*(l+1)}}{(1-\alpha^{\*(l)})c^{\*(l)}}{\sigma}^{2}s\_{\alpha}^{k-1}h\_{S^{\*(l+1)}}(s\_{\alpha}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−α∗(l+1))​c∗(l+1)(1−α∗(l))​c∗(l)(γ𝔼[(S∗(l+1))k−1∣S∗(l+1)>sα]\displaystyle~~+\frac{(1-\alpha^{\*(l+1)})c^{\*(l+1)}}{(1-\alpha^{\*(l)})c^{\*(l)}}\Big(\gamma\mathbb{E}\left[(S^{\*(l+1)})^{k-1}\mid S^{\*(l+1)}>s\_{\alpha}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(k−1)σ2𝔼[(S∗(l+1))k−2∣S∗(l+1)>sα]),\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~+(k-1){\sigma}^{2}\mathbb{E}\left[(S^{\*(l+1)})^{k-2}\mid S^{\*(l+1)}>s\_{\alpha}\right]\Big), |  | (5) |

with ([1](https://arxiv.org/html/2601.00568v1#S3.Ex23 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) being a special case of ([1](https://arxiv.org/html/2601.00568v1#S3.Ex24 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) with l=0l=0, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | TCMα,k​(S)=∑j=0k(kj)​𝔼​[Sk−j​∣S>​sα]​(−CTEα​(S))j.\displaystyle\mathrm{TCM}\_{\alpha,k}(S)=\sum^{k}\_{j=0}\binom{k}{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right](-\mathrm{CTE}\_{\alpha}(S))^{j}. |  | (6) |

###### Proof.

We will first prove ([1](https://arxiv.org/html/2601.00568v1#S3.Ex23 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")). We begin with applying Lemma [1](https://arxiv.org/html/2601.00568v1#Thmlemma1 "Lemma 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Sk​∣S>​sα,Θ=θ]=\displaystyle\mathbb{E}\left[S^{k}\mid S>s\_{\alpha},\Theta=\theta\right]= | θ​σ2​sαk−1​fS∣Θ​(sα)F¯S∣Θ​(sα)+(μ+θ​γ)​𝔼​[Sk−1​∣S>​sα,Θ=θ]\displaystyle~\theta{\sigma}^{2}s\_{\alpha}^{k-1}\frac{f\_{S\mid\Theta}(s\_{\alpha})}{{\overline{F}}\_{S\mid\Theta}(s\_{\alpha})}+(\mu+\theta\gamma)\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha},\Theta=\theta\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(k−1)​θ​σ2​𝔼​[Sk−2​∣S>​sα,Θ=θ].\displaystyle~~+(k-1)\theta{\sigma}^{2}\mathbb{E}\left[S^{k-2}\mid S>s\_{\alpha},\Theta=\theta\right]. |  |

Then, applying the above result and Lemma [2](https://arxiv.org/html/2601.00568v1#Thmlemma2 "Lemma 2. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") (with l=0l=0) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Sk​∣S>​sα]=\displaystyle\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]= | 11−α​∫0∞𝔼​[Sk​∣S>​sα,Θ=θ]​F¯S∣θ​(sα)​π​(θ)​𝑑θ\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{0}\mathbb{E}\left[S^{k}\mid S>s\_{\alpha},\Theta=\theta\right]{\overline{F}}\_{S\mid\theta}(s\_{\alpha})\pi(\theta)\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α​∫0∞μ​𝔼​[Sk−1​∣S>​sα,Θ=θ]​F¯S∣θ​(sα)​π​(θ)+σ2​sαk−1​fS∣θ​(sα)​(θ​π​(θ))\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{0}\mu\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha},\Theta=\theta\right]{\overline{F}}\_{S\mid\theta}(s\_{\alpha})\pi(\theta)+{\sigma}^{2}s\_{\alpha}^{k-1}f\_{S\mid\theta}(s\_{\alpha})(\theta\pi(\theta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γ​𝔼​[Sk−1​∣S>​sα,Θ=θ]​F¯S∣θ​(sα)​(θ​π​(θ))\displaystyle~~~~~~~~~~~~~~~~+\gamma\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha},\Theta=\theta\right]{\overline{F}}\_{S\mid\theta}(s\_{\alpha})(\theta\pi(\theta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(k−1)​σ2​𝔼​[Sk−2​∣S>​sα,Θ=θ]​F¯S∣θ​(sα)​(θ​π​(θ))​d​θ\displaystyle~~~~~~~~~~~~~~~~+(k-1){\sigma}^{2}\mathbb{E}\left[S^{k-2}\mid S>s\_{\alpha},\Theta=\theta\right]{\overline{F}}\_{S\mid\theta}(s\_{\alpha})(\theta\pi(\theta))\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | μ​𝔼​[Sk−1​∣S>​sα]+c∗​11−α​σ2​sαk−1​fS∗​(sα)⋅F¯S∗​(sα)F¯S∗​(sα)\displaystyle~\mu\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]+c^{\*}\frac{1}{1-\alpha}{\sigma}^{2}s\_{\alpha}^{k-1}f\_{S^{\*}}(s\_{\alpha})\cdot\frac{{\overline{F}}\_{S^{\*}}(s\_{\alpha})}{{\overline{F}}\_{S^{\*}}(s\_{\alpha})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗1−α​c∗​γ​𝔼​[(S∗)k−1​∣S∗>​sα]+1−α∗1−α​c∗​(k−1)​σ2​𝔼​[(S∗)k−2​∣S∗>​sα]\displaystyle~~+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\gamma\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right]+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(k-1){\sigma}^{2}\mathbb{E}\left[(S^{\*})^{k-2}\mid S^{\*}>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1−α∗1−α​c∗​σ2​sαk−1​hS∗​(sα)+μ​𝔼​[Sk−1​∣S>​sα]\displaystyle~\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}s\_{\alpha}^{k-1}h\_{S^{\*}}(s\_{\alpha})+\mu\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗1−α​c∗​γ​𝔼​[(S∗)k−1​∣S∗>​sα]+1−α∗1−α​c∗​(k−1)​σ2​𝔼​[(S∗)k−2​∣S∗>​sα].\displaystyle~~+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\gamma\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right]+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(k-1){\sigma}^{2}\mathbb{E}\left[(S^{\*})^{k-2}\mid S^{\*}>s\_{\alpha}\right]. |  |

Equation ([1](https://arxiv.org/html/2601.00568v1#S3.Ex24 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) is proven in the same way, as S∗(l)S^{\*(l)} and SS are both NMVM random variables, and (S∗(l))∗=S∗(l+1)(S^{\*(l)})^{\*}=S^{\*(l+1)} by definition. Since π​(θ)\pi(\theta) is an arbitrary density function, we can replace π​(θ)\pi(\theta) with π∗(l)​(θ)\pi^{\*(l)}(\theta). Consequently, SS (resp. S∗S^{\*}) is replaced with S∗(l)S^{\*(l)} (resp. S∗(l+1)S^{\*(l+1)}), and the rest follows.

Lastly, directly applying binomial expansion onto the TCM of SS completes the proof for ([6](https://arxiv.org/html/2601.00568v1#S3.E6 "In Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")).
∎

###### Remark 4.

If we further assume that Θ∼G​I​G​(λ,χ,ψ)\Theta\sim GIG(\lambda,\chi,\psi), then S∼G​H​(λ,χ,ψ,μ,σ,γ)S\sim GH(\lambda,\chi,\psi,\mu,{\sigma},\gamma) (see Definition [4](https://arxiv.org/html/2601.00568v1#Thmdefinition4 "Definition 4. ‣ 2.3 Normal mean-variance mixture distributions ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")). This gives S∗∼G​H​(λ+1,χ,ψ,μ,σ,γ)S^{\*}\sim GH(\lambda+1,\chi,\psi,\mu,{\sigma},\gamma) ((25) to (27) of KK19). This is useful for Section [5](https://arxiv.org/html/2601.00568v1#S5 "5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), where recursive formulas for the TM of GH distributed random variables are computed.

The following corollary presents a particularly interesting case of Theorem [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") when orders of moment are 1 and 2; these results were first obtained by KK19 (see their Theorem 3.1, Proposition 5.1, and Theorem 5.2).

###### Corollary 1.

The CTE of the NMVM random variable SS at confidence level α∈(0,1)\alpha\in(0,1) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | CTEα​(S)=μ+c∗​(1−α∗1−α)​(γ+σ2​hS∗​(sα)),\displaystyle\mathrm{CTE}\_{\alpha}(S)=\mu+c^{\*}\left(\frac{1-\alpha^{\*}}{1-\alpha}\right)\left(\gamma+{\sigma}^{2}h\_{S^{\*}}(s\_{\alpha})\right), |  | (7) |

and the 22-nd order TM and TCM of SS are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | TMα,2​(S)=\displaystyle\mathrm{TM}\_{\alpha,2}(S)= | μ2+1−α∗1−α​c∗​(σ2+2​μ​γ+σ2​(sα+μ)​hS∗​(sα))\displaystyle~\mu^{2}+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left({\sigma}^{2}+2\mu\gamma+{\sigma}^{2}(s\_{\alpha}+\mu)h\_{S^{\*}}(s\_{\alpha})\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1−α∗∗1−α​c∗∗​(γ2+γ​σ2​hS∗∗​(sα)),\displaystyle~~+\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}\left(\gamma^{2}+\gamma{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha})\right), |  | (8) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | TVα​(S)=\displaystyle\mathrm{TV}\_{\alpha}(S)= | 1−α∗1−α​c∗​σ2​(1+(sα−μ)​hS∗​(sα))+1−α∗∗1−α​c∗∗​γ​(γ+σ2​hS∗∗​(sα))\displaystyle~\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}\left(1+(s\_{\alpha}-\mu)h\_{S^{\*}}(s\_{\alpha})\right)+\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}\gamma\left(\gamma+{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha})\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(1−α∗1−α​c∗​(γ+σ2​hS∗​(sα)))2.\displaystyle~~-\left(\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(\gamma+{\sigma}^{2}h\_{S^{\*}}(s\_{\alpha}))\right)^{2}. |  | (9) |

###### Proof.

Equation ([7](https://arxiv.org/html/2601.00568v1#S3.E7 "In Corollary 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) is directly obtained from substituting k=1k=1 into ([1](https://arxiv.org/html/2601.00568v1#S3.Ex23 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) in Theorem [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). Substituting l=1l=1, k=1k=1 into ([1](https://arxiv.org/html/2601.00568v1#S3.Ex24 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) in Theorem [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[S∗​∣S∗>​sα]=μ+c∗∗​(1−α∗∗)c∗​(1−α∗)​(γ+σ2​hS∗∗​(sα)).\displaystyle\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]=\mu+\frac{c^{\*\*}(1-\alpha^{\*\*})}{c^{\*}(1-\alpha^{\*})}(\gamma+{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha})). |  |

Applying Theorem [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), then substituting ([7](https://arxiv.org/html/2601.00568v1#S3.E7 "In Corollary 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) and the above result gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | TMα,2​(S)=\displaystyle\mathrm{TM}\_{\alpha,2}(S)= | 1−α∗1−α​c∗​σ2​sα​hS∗​(sα)+μ​𝔼​[S​∣S>​sα]\displaystyle~\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}s\_{\alpha}h\_{S^{\*}}(s\_{\alpha})+\mu\mathbb{E}\left[S\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗1−α​c∗​γ​𝔼​[S∗​∣S∗>​sα]+1−α∗1−α​c∗​σ2\displaystyle~~+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\gamma\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1−α∗1−α​c∗​σ2​sα​hS∗​(sα)+μ​(μ+1−α∗1−α​c∗​(γ+σ2​hS∗​(sα)))\displaystyle~\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}s\_{\alpha}h\_{S^{\*}}(s\_{\alpha})+\mu\left(\mu+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(\gamma+{\sigma}^{2}h\_{S^{\*}}(s\_{\alpha}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗1−α​c∗​γ​(μ+c∗∗​(1−α∗∗)c∗​(1−α∗)​(γ+σ2​hS∗∗​(sα)))+1−α∗1−α​c∗​σ2,\displaystyle~~+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\gamma\left(\mu+\frac{c^{\*\*}(1-\alpha^{\*\*})}{c^{\*}(1-\alpha^{\*})}(\gamma+{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha}))\right)+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}, |  |

and we obtain ([1](https://arxiv.org/html/2601.00568v1#S3.Ex36 "Corollary 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) after routine algebraic simplification. Subsequently, ([1](https://arxiv.org/html/2601.00568v1#S3.Ex37 "Corollary 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) is obtained by

|  |  |  |  |
| --- | --- | --- | --- |
|  | TVα​(S)=\displaystyle\mathrm{TV}\_{\alpha}(S)= | 𝔼​[S2​∣S>​sα]−𝔼​[S​∣S>​sα]2\displaystyle~\mathbb{E}\left[S^{2}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[S\mid S>s\_{\alpha}\right]^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | μ2+1−α∗1−α​c∗​(σ2+2​μ​γ+σ2​(sα+μ)​hS∗​(sα))\displaystyle~\mu^{2}+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left({\sigma}^{2}+2\mu\gamma+{\sigma}^{2}(s\_{\alpha}+\mu)h\_{S^{\*}}(s\_{\alpha})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗∗1−α​c∗∗​(γ2+γ​σ2​hS∗∗​(sα))−(μ+1−α∗1−α​c∗​(γ+σ2​hS∗​(sα)))2\displaystyle~~+\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}\left(\gamma^{2}+\gamma{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha})\right)-\left(\mu+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(\gamma+{\sigma}^{2}h\_{S^{\*}}(s\_{\alpha}))\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | μ2−μ2+1−α∗1−α​c∗​(σ2+2​μ​γ−2​μ​γ+σ2​(sα+μ−2​μ)​hS∗​(sα))\displaystyle~\mu^{2}-\mu^{2}+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left({\sigma}^{2}+2\mu\gamma-2\mu\gamma+{\sigma}^{2}(s\_{\alpha}+\mu-2\mu)h\_{S^{\*}}(s\_{\alpha})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗∗1−α​c∗∗​(γ2+γ​σ2​hS∗∗​(sα))−(1−α∗1−α​c∗​(γ+σ2​hS∗​(sα)))2\displaystyle~~+\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}\left(\gamma^{2}+\gamma{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha})\right)-\left(\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(\gamma+{\sigma}^{2}h\_{S^{\*}}(s\_{\alpha}))\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1−α∗1−α​c∗​σ2​(1+(sα−μ)​hS∗​(sα))\displaystyle~\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}{\sigma}^{2}\left(1+(s\_{\alpha}-\mu)h\_{S^{\*}}(s\_{\alpha})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−α∗∗1−α​c∗∗​γ​(γ+σ2​hS∗∗​(sα))−(1−α∗1−α​c∗​(γ+σ2​hS∗​(sα)))2.∎\displaystyle~~+\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}\gamma\left(\gamma+{\sigma}^{2}h\_{S^{\*\*}}(s\_{\alpha})\right)-\left(\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}(\gamma+{\sigma}^{2}h\_{S^{\*}}(s\_{\alpha}))\right)^{2}.\qed |  |

## 4 Capital allocation for multivariate NMVM distributions

In Section [3](https://arxiv.org/html/2601.00568v1#S3 "3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), the TCM of the aggregate loss SS has been derived. Next, we proceed to study the TCM-based capital allocation method as defined in Definition [3](https://arxiv.org/html/2601.00568v1#Thmdefinition3 "Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). Again, we obtain an explicit formula for the 2nd-order TCM-based capital allocation as a special case.

Recall the same model setup as in Section [3](https://arxiv.org/html/2601.00568v1#S3 "3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). In addition, let σS2:=∑i=1n∑j=1nσi​j{\sigma}^{2}\_{S}:=\sum^{n}\_{i=1}\sum^{n}\_{j=1}{\sigma}\_{ij} and σi​S:=∑j=1nσi​j{\sigma}\_{iS}:=\sum^{n}\_{j=1}{\sigma}\_{ij} for i∈{1,…,n}i\in\left\{1,\dots,n\right\}. We also denote the NMVM random vector parameters by 𝝁=(μ1,…,μn)′∈ℝn\bm{\mu}=(\mu\_{1},\dots,\mu\_{n})^{\prime}\in\mathbb{R}^{n}, 𝜸=(γ1,…,γn)′∈ℝn\bm{\gamma}=(\gamma\_{1},\dots,\gamma\_{n})^{\prime}\in\mathbb{R}^{n}, and 𝚺=(σi​j)1≤i,j≤n∈ℝn×n\bm{\Sigma}=({\sigma}\_{ij})\_{1\leq i,j\leq n}\in\mathbb{R}^{n\times n}. We start by stating some useful results.

###### Lemma 3.

(KK19, Theorem 4.1)
Consider the multivariate NMVM random vector (X1,…,Xn)(X\_{1},\dots,X\_{n}) with mixing random variable Θ\Theta and parameters 𝛍\bm{\mu}, 𝛄\bm{\gamma}, and 𝚺\bm{\Sigma}, and the aggregate loss SS. Under the CTE-based capital allocation with confidence level α∈(0,1)\alpha\in(0,1), the capital allocated to XiX\_{i} for all i=1,…,ni=1,\dots,n, is given by

|  |  |  |
| --- | --- | --- |
|  | Ki=𝔼​[Xi​∣S>​sα]=a0,i+a1,i​𝔼​[S​∣S>​sα]+a2,i​1−α∗1−α​c∗,\displaystyle K\_{i}=\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]=a\_{0,i}+a\_{1,i}\mathbb{E}\left[S\mid S>s\_{\alpha}\right]+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}, |  |

where the coefficients a0,ia\_{0,i}, a1,ia\_{1,i}, and a2,ia\_{2,i} are defined as

|  |  |  |
| --- | --- | --- |
|  | a0,i=μi−a1,i​∑j=1nμi,a1,i=∑j=1nσi​jσS2,and​a2,i=γi−a1,i​∑j=1nγj.\displaystyle a\_{0,i}=\mu\_{i}-a\_{1,i}\sum^{n}\_{j=1}\mu\_{i},~~a\_{1,i}=\frac{\sum^{n}\_{j=1}{\sigma}\_{ij}}{{\sigma}^{2}\_{S}},~~\mbox{and}~~a\_{2,i}=\gamma\_{i}-a\_{1,i}\sum^{n}\_{j=1}\gamma\_{j}. |  |

###### Lemma 4.

Consider the same random variables X1,…,XnX\_{1},\dots,X\_{n}, and SS in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), as well as all related parameters and coefficients. The random vector (X1,…,Xn∣S=s,Θ=θ)(X\_{1},\dots,X\_{n}\mid S=s,\Theta=\theta) for some s∈ℝs\in\mathbb{R}, θ∈ℝ+\theta\in\mathbb{R}\_{+} follows a multivariate normal distribution, with

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xi∣S=s,Θ=θ]=a0,i+a1,i​s+a2,i​θ​ for all ​i=1,…,n,\displaystyle\mathbb{E}\left[X\_{i}\mid S=s,\Theta=\theta\right]=a\_{0,i}+a\_{1,i}s+a\_{2,i}\theta\mbox{~~for all~~}i=1,\dots,n, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Cov[Xi,Xj∣S=s,Θ=θ]=θ(σi​j−a1,ia1,jσS2) for all i,j=1,…,n.\displaystyle\mathrm{Cov}\left[X\_{i},X\_{j}\mid S=s,\Theta=\theta\right]=\theta({\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S})\mbox{~~for all~~}i,j=1,\dots,n. |  |

###### Proof.

Since the random vector (X1,…,Xn∣Θ=θ)(X\_{1},\dots,X\_{n}\mid\Theta=\theta) follows a multivariate normal distribution (see Definition [4](https://arxiv.org/html/2601.00568v1#Thmdefinition4 "Definition 4. ‣ 2.3 Normal mean-variance mixture distributions ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")), Theorem 3.3.3 of T12 implies that (X1,…,Xn,S∣Θ=θ)(X\_{1},\dots,X\_{n},S\mid\Theta=\theta) also follows a multivariate normal distribution. By Theorem 3.3.4 of T12, (X1,…,Xn∣S=s,Θ=θ)(X\_{1},\dots,X\_{n}\mid S=s,\Theta=\theta) follows a multivariate normal distribution with its mean and covariance given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi∣S=s,Θ=θ]=\displaystyle\mathbb{E}\left[X\_{i}\mid S=s,\Theta=\theta\right]= | 𝔼​[Xi∣Θ=θ]+Cov​[Xi,S∣Θ=θ]Cov​[S,S∣Θ=θ]​(s−𝔼​[S∣Θ=θ])\displaystyle~\mathbb{E}[X\_{i}\mid\Theta=\theta]+\frac{\mathrm{Cov}[X\_{i},S\mid\Theta=\theta]}{\mathrm{Cov}[S,S\mid\Theta=\theta]}(s-\mathbb{E}[S\mid\Theta=\theta]) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (μi+θ​γi)−∑j=1nσi​jσS2​∑k=1n(μk+θ​γk)+∑j=1nσi​jσS2​s\displaystyle~(\mu\_{i}+\theta\gamma\_{i})-\frac{\sum^{n}\_{j=1}{\sigma}\_{ij}}{{\sigma}^{2}\_{S}}\sum^{n}\_{k=1}(\mu\_{k}+\theta\gamma\_{k})+\frac{\sum^{n}\_{j=1}{\sigma}\_{ij}}{{\sigma}^{2}\_{S}}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | μi−a1,i​∑k=1nμk+θ​(γi−a1,i​∑k=1nγk)+a1,i​s\displaystyle~\mu\_{i}-a\_{1,i}\sum^{n}\_{k=1}\mu\_{k}+\theta\left(\gamma\_{i}-a\_{1,i}\sum^{n}\_{k=1}\gamma\_{k}\right)+a\_{1,i}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a0,i+a1,i​s+a2,i​θ,\displaystyle~a\_{0,i}+a\_{1,i}s+a\_{2,i}\theta, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov[Xi,Xj∣S=s,Θ=θ]=\displaystyle\mathrm{Cov}\left[X\_{i},X\_{j}\mid S=s,\Theta=\theta\right]= | Cov​[Xi,Xj∣Θ=θ]−Cov​[Xi,S∣Θ=θ]​Cov​[S,Xj∣Θ=θ]Cov​[S,S∣Θ=θ]\displaystyle~\mathrm{Cov}[X\_{i},X\_{j}\mid\Theta=\theta]-\frac{\mathrm{Cov}[X\_{i},S\mid\Theta=\theta]~\mathrm{Cov}[S,X\_{j}\mid\Theta=\theta]}{\mathrm{Cov}[S,S\mid\Theta=\theta]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | θ​σi​j−(θ​σi​S)​(θ​σj​S)θ​σS2\displaystyle~\theta{\sigma}\_{ij}-\frac{(\theta{\sigma}\_{iS})(\theta{\sigma}\_{jS})}{\theta{\sigma}^{2}\_{S}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | θ​(σi​j−a1,i​a1,j​σS2).∎\displaystyle~\theta({\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}).\qed |  |

Before arriving at the TCM-based capital allocation, we provide a useful intermediate result.

###### Proposition 2.

Consider the same random variables X1,…,XnX\_{1},\dots,X\_{n}, and SS in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), as well as all related parameters and coefficients. Fix k∈ℕ∖{1}k\in\mathbb{N}\setminus\left\{1\right\} and α∈(0,1)\alpha\in(0,1). For all i∈{1,…,n}i\in\left\{1,\dots,n\right\}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​[Xi,Sk−1​∣S>​sα]=\displaystyle\mathrm{Cov}\left[X\_{i},S^{k-1}\mid S>s\_{\alpha}\right]= | a1,i​(𝔼​[Sk​∣S>​sα]−𝔼​[S​∣S>​sα]​𝔼​[Sk−1​∣S>​sα])\displaystyle~a\_{1,i}\left(\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[S\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i​1−α∗1−α​c∗​(𝔼​[(S∗)k−1​∣S∗>​sα]−𝔼​[Sk−1​∣S>​sα]).\displaystyle~~+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left(\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right]-\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]\right). |  |

###### Proof.

Using similar techniques to those in the proof of Lemma [2](https://arxiv.org/html/2601.00568v1#Thmlemma2 "Lemma 2. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​[Xi,Sk−1​∣S>​sα]=\displaystyle\mathrm{Cov}\left[X\_{i},S^{k-1}\mid S>s\_{\alpha}\right]= | 𝔼​[Xi​Sk−1​∣S>​sα]−𝔼​[Xi​∣S>​sα]​𝔼​[Sk−1​∣S>​sα]\displaystyle~\mathbb{E}\left[X\_{i}S^{k-1}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α​∫sα∞sk−1​𝔼​[Xi∣S=s]​fS​(s)​𝑑s\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}s^{k-1}\mathbb{E}\left[X\_{i}\mid S=s\right]f\_{S}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​[Xi​∣S>​sα]​𝔼​[Sk−1​∣S>​sα].\displaystyle~~-\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]. |  |

Explicit solutions to 𝔼​[Xi​∣S>​sα]\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right] and 𝔼​[Sk−1​∣S>​sα]\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right] are available in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") and Theorem [1](https://arxiv.org/html/2601.00568v1#Thmtheorem1 "Theorem 1. ‣ 3 Tail moments of univariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), respectively. Equation (45) in KK19 states that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xi∣S=s]=a0,i+a1,i+a2,i​c∗​fS∗​(s)fS​(s).\displaystyle\mathbb{E}\left[X\_{i}\mid S=s\right]=a\_{0,i}+a\_{1,i}+a\_{2,i}c^{\*}\frac{f\_{S^{\*}}(s)}{f\_{S}(s)}. |  |

Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi​Sk−1​∣S>​sα]=\displaystyle\mathbb{E}\left[X\_{i}S^{k-1}\mid S>s\_{\alpha}\right]= | 11−α​∫sα∞sk−1​(a0,i+a1,i​s+a2,i​c∗​fS∗​(s)fS​(s))​fS​(s)​𝑑s\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}s^{k-1}\left(a\_{0,i}+a\_{1,i}s+a\_{2,i}c^{\*}\frac{f\_{S^{\*}}(s)}{f\_{S}(s)}\right)f\_{S}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α​∫sα∞a0,i​sk−1​fS​(s)+a1,i​sk​fS​(s)+a2,i​c∗​sk−1​fS∗​(s)​d​s\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}a\_{0,i}s^{k-1}f\_{S}(s)+a\_{1,i}s^{k}f\_{S}(s)+a\_{2,i}c^{\*}s^{k-1}f\_{S^{\*}}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a0,i​𝔼​[Sk−1​∣S>​sα]+a1,i​𝔼​[Sk​∣S>​sα]\displaystyle~a\_{0,i}\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]+a\_{1,i}\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i​1−α∗1−α​c∗​𝔼​[(S∗)k−1​∣S∗>​sα],\displaystyle~~+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right], |  |

which gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​[Xi,Sk−1​∣S>​sα]=\displaystyle\mathrm{Cov}\left[X\_{i},S^{k-1}\mid S>s\_{\alpha}\right]= | 𝔼​[Xi​Sk−1​∣S>​sα]−𝔼​[Xi​∣S>​sα]​𝔼​[Sk−1​∣S>​sα]\displaystyle~\mathbb{E}\left[X\_{i}S^{k-1}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a0,i​𝔼​[Sk−1​∣S>​sα]+a1,i​𝔼​[Sk​∣S>​sα]\displaystyle~a\_{0,i}\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]+a\_{1,i}\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i​1−α∗1−α​c∗​𝔼​[(S∗)k−1​∣S∗>​sα]\displaystyle~~+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(a0,i+a1,i​𝔼​[S​∣S>​sα]+a2,i​1−α∗1−α​c∗)​𝔼​[Sk−1​∣S>​sα]\displaystyle~~-\left(a\_{0,i}+a\_{1,i}\mathbb{E}\left[S\mid S>s\_{\alpha}\right]+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\right)\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a1,i​(𝔼​[Sk​∣S>​sα]−𝔼​[S​∣S>​sα]​𝔼​[Sk−1​∣S>​sα])\displaystyle~a\_{1,i}\left(\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[S\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i​1−α∗1−α​c∗​(𝔼​[(S∗)k−1​∣S∗>​sα]−𝔼​[Sk−1​∣S>​sα]).∎\displaystyle~~+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left(\mathbb{E}\left[(S^{\*})^{k-1}\mid S^{\*}>s\_{\alpha}\right]-\mathbb{E}\left[S^{k-1}\mid S>s\_{\alpha}\right]\right).\qed |  |

Now we state our main result in capital allocation.

###### Theorem 2.

Consider the same random variables X1,…,XnX\_{1},\dots,X\_{n}, and SS in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), as well as all related parameters and coefficients. For some k∈ℕ∖{1}k\in\mathbb{N}\setminus\left\{1\right\}, under the kk-th order TCM-based capital allocation in Definition [3](https://arxiv.org/html/2601.00568v1#Thmdefinition3 "Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") with confidence level α∈(0,1)\alpha\in(0,1), the capital allocated to XiX\_{i} for all i=1,…,ni=1,\dots,n, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ki=\displaystyle K\_{i}= | Cov​[Xi,(S−CTEα​(S))k−1​∣S>​sα]\displaystyle~\mathrm{Cov}\left[X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | a1,i​TCMα,k​(S)+a2,i​1−α∗1−α​c∗​(𝔼​[(S∗−CTEα​(S))k−1​∣S∗>​sα]−TCMα,k−1​(S)).\displaystyle~a\_{1,i}\mathrm{TCM}\_{\alpha,k}(S)+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\left(\mathbb{E}\left[\left(S^{\*}-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S^{\*}>s\_{\alpha}\right]-\mathrm{TCM}\_{\alpha,k-1}(S)\right). |  | (10) |

###### Proof.

Using the binomial expansion and Proposition [2](https://arxiv.org/html/2601.00568v1#Thmproposition2 "Proposition 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ki=\displaystyle K\_{i}= | ∑j=0k−1(k−1j)​(−CTEα​(S))j​Cov​[Xi,Sk−1−j​∣S>​sα]\displaystyle~\sum^{k-1}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathrm{Cov}\left[X\_{i},S^{k-1-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0k−2(k−1j)(−CTEα(S))j(a1,i(𝔼[Sk−j∣S>sα]−𝔼[S∣S>sα]𝔼[Sk−1−j∣S>sα])\displaystyle~\sum^{k-2}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\Bigg(a\_{1,i}\left(\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]-\mathbb{E}\left[S\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i1−α∗1−αc∗(𝔼[(S∗)k−1−j∣S∗>sα]\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\Big(\mathbb{E}\left[(S^{\*})^{k-1-j}\mid S^{\*}>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼[Sk−1−j∣S>sα]))+0\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right]\Big)\Bigg)+0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a1,i​∑j=0k−2(k−1j)​((−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]+(−CTEα​(S))j+1​𝔼​[Sk−1−j​∣S>​sα])\displaystyle~a\_{1,i}\sum^{k-2}\_{j=0}\binom{k-1}{j}\left((-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]+(-\mathrm{CTE}\_{\alpha}(S))^{j+1}\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i1−α∗1−αc∗∑j=0k−2(k−1j)((−CTEα(S))j𝔼[(S∗)k−1−j∣S∗>sα]\displaystyle~~+a\_{2,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\sum^{k-2}\_{j=0}\binom{k-1}{j}\Bigg((-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[(S^{\*})^{k-1-j}\mid S^{\*}>s\_{\alpha}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(−CTEα(S))j𝔼[Sk−1−j∣S>sα]).\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right]\Bigg). |  | (11) |

For the latter summation (with coefficient a2,i​c∗​(1−α∗)/(1−α)a\_{2,i}c^{\*}(1-\alpha^{\*})/\left(1-\alpha\right)), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑j=0k−2(k−1j)​(−CTEα​(S))j​(𝔼​[(S∗)k−1−j​∣S∗>​sα]−𝔼​[Sk−1−j​∣S>​sα])\displaystyle~\sum^{k-2}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\left(\mathbb{E}\left[(S^{\*})^{k-1-j}\mid S^{\*}>s\_{\alpha}\right]-\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (∑j=0k−1(k−1j)​(−CTEα​(S))j​𝔼​[(S∗)k−1−j​∣S∗>​sα]−(−CTEα​(S))k−1)\displaystyle~\left(\sum^{k-1}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[(S^{\*})^{k-1-j}\mid S^{\*}>s\_{\alpha}\right]-(-\mathrm{CTE}\_{\alpha}(S))^{k-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(∑j=0k−1(k−1j)​(−CTEα​(S))j​𝔼​[Sk−1−j​∣S>​sα]−(−CTEα​(S))k−1)\displaystyle~~-\left(\sum^{k-1}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right]-(-\mathrm{CTE}\_{\alpha}(S))^{k-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[(S∗−CTEα​(S))k−1​∣S∗>​sα]−𝔼​[(S−CTEα​(S))k−1​∣S>​sα]\displaystyle~\mathbb{E}\left[\left(S^{\*}-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S^{\*}>s\_{\alpha}\right]-\mathbb{E}\left[\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[(S∗−CTEα​(S))k−1​∣S∗>​sα]−TCMα,k−1​(S),\displaystyle~\mathbb{E}\left[\left(S^{\*}-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S^{\*}>s\_{\alpha}\right]-\mathrm{TCM}\_{\alpha,k-1}(S), |  | (12) |

with the second-to-last equality being an application of the binomial theorem. For the former summation (with coefficient a1,ia\_{1,i}), we first notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (−CTEα​(S))k−1​𝔼​[Sk−(k−1)​∣S>​sα]+(−CTEα​(S))k−1+1​𝔼​[Sk−1−(k−1)​∣S>​sα]\displaystyle~(-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mathbb{E}\left[S^{k-(k-1)}\mid S>s\_{\alpha}\right]+(-\mathrm{CTE}\_{\alpha}(S))^{k-1+1}\mathbb{E}\left[S^{k-1-(k-1)}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (−CTEα​(S))k−1​CTEα​(S)+(−CTEα​(S))k=0.\displaystyle~(-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mathrm{CTE}\_{\alpha}(S)+(-\mathrm{CTE}\_{\alpha}(S))^{k}=0. |  |

Using the identity above, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑j=0k−2(k−1j)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]+∑j=0k−2(k−1j)​(−CTEα​(S))j+1​𝔼​[Sk−1−j​∣S>​sα]\displaystyle~\sum^{k-2}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]+\sum^{k-2}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j+1}\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0k−1(k−1j)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]+∑j=0k−1(k−1j)​(−CTEα​(S))j+1​𝔼​[Sk−1−j​∣S>​sα]\displaystyle~\sum^{k-1}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]+\sum^{k-1}\_{j=0}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j+1}\mathbb{E}\left[S^{k-1-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Sk​∣S>​sα]+∑j=1k−1(k−1j)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]\displaystyle~\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]+\sum^{k-1}\_{j=1}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=1k(k−1j−1)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]\displaystyle~~+\sum^{k}\_{j=1}\binom{k-1}{j-1}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Sk​∣S>​sα]+∑j=1k−1(k−1j)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]\displaystyle~\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]+\sum^{k-1}\_{j=1}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=1k−1(k−1j−1)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]+(−CTEα​(S))k\displaystyle~~+\sum^{k-1}\_{j=1}\binom{k-1}{j-1}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]+(-\mathrm{CTE}\_{\alpha}(S))^{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Sk​∣S>​sα]+∑j=1k−1(kj)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]+(−CTEα​(S))k\displaystyle~\mathbb{E}\left[S^{k}\mid S>s\_{\alpha}\right]+\sum^{k-1}\_{j=1}\binom{k}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]+(-\mathrm{CTE}\_{\alpha}(S))^{k} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0k(kj)​(−CTEα​(S))j​𝔼​[Sk−j​∣S>​sα]=TCMα,k​(S),\displaystyle~\sum^{k}\_{j=0}\binom{k}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]=\mathrm{TCM}\_{\alpha,k}(S), |  | (13) |

where the binomial theorem is used at the last equality, and the identity (k−1j)+(k−1j−1)=(kj)\binom{k-1}{j}+\binom{k-1}{j-1}=\binom{k}{j} is used at the fourth equality. Finally, ([2](https://arxiv.org/html/2601.00568v1#S4.Ex77 "Theorem 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) is obtained by substituting ([4](https://arxiv.org/html/2601.00568v1#S4.Ex84 "Proof. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) and ([4](https://arxiv.org/html/2601.00568v1#S4.Ex90 "Proof. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) into ([4](https://arxiv.org/html/2601.00568v1#S4.Ex78 "Proof. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")).
∎

The capital allocation expressions in Theorem [2](https://arxiv.org/html/2601.00568v1#Thmtheorem2 "Theorem 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") can be seen as the sum of two components, signified by the terms with coefficients a1,ia\_{1,i} and a2,ia\_{2,i} in ([2](https://arxiv.org/html/2601.00568v1#S4.Ex77 "Theorem 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")), which are the only variables that are specific to each loss XiX\_{i}. Based on the representations of a1,ia\_{1,i} and a2,ia\_{2,i} in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), the variable a1,ia\_{1,i} represents a direct risk contribution from XiX\_{i} to the total risk TCMα,k​(S)\mathrm{TCM}\_{\alpha,k}(S), whereas a2,ia\_{2,i} shows the indirect adjustments required to reflect other tail behaviours such as tail skewness. The existence of these interpretations allows agents to explain their capital allocation outcome to other stakeholders more easily, while maintaining the rigorous mathematical results that support their complex risk management priorities.

As results of the second order will naturally be of more interest for their intuitive interpretation, we provide explicit results of the 22-nd order TCM-based order capital allocation, which is also known as the TV-based capital allocation (see Definition [3](https://arxiv.org/html/2601.00568v1#Thmdefinition3 "Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")).

###### Corollary 2.

Consider the same random variables X1,…,XnX\_{1},\dots,X\_{n}, and SS in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), as well as all related parameters and coefficients. Under the TV-based capital allocation with confidence level α∈(0,1)\alpha\in(0,1), the capital allocated to XiX\_{i} for all i=1,…,ni=1,\dots,n, is given by

|  |  |  |
| --- | --- | --- |
|  | Ki=Cov​[Xi,S​∣S>​sα]=a1,i​TVα​(S)+1−α∗1−α​c∗​a2,i​(𝔼​[S∗​∣S∗>​sα]−CTEα​(S)).\displaystyle K\_{i}=\mathrm{Cov}\left[X\_{i},S\mid S>s\_{\alpha}\right]=a\_{1,i}\mathrm{TV}\_{\alpha}(S)+\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}a\_{2,i}\left(\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]-\mathrm{CTE}\_{\alpha}(S)\right). |  |

###### Proof.

Simply substituting k=2k=2 into Theorem [2](https://arxiv.org/html/2601.00568v1#Thmtheorem2 "Theorem 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") and noting that TCMα,1​(S)=0\mathrm{TCM}\_{\alpha,1}(S)=0, we obtain the desired result.
∎

###### Remark 5.

In recent literature, IL25 and Y25 studied Var​[Xi​∣S>​sα]\mathrm{Var}[X\_{i}\mid S>s\_{\alpha}] and Cov​[Xi,Xj​∣S>​sα]\mathrm{Cov}\left[X\_{i},X\_{j}\mid S>s\_{\alpha}\right] respectively due to their relevance to the tail behaviour of XiX\_{i}. We provide the expressions for two relevant identities for the NMVM model, which are directly obtainable from Lemma [4](https://arxiv.org/html/2601.00568v1#Thmlemma4 "Lemma 4. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi2​∣S>​sα]=\displaystyle\mathbb{E}\left[X\_{i}^{2}\mid S>s\_{\alpha}\right]= | a1,i2​𝔼​[S2​∣S>​sα]+2​a0,i​a1,i​𝔼​[S​∣S>​sα]\displaystyle~a\_{1,i}^{2}\mathbb{E}\left[S^{2}\mid S>s\_{\alpha}\right]+2a\_{0,i}a\_{1,i}\mathbb{E}\left[S\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​a2,i​a1,i​1−α∗1−α​c∗​𝔼​[S∗​∣S∗>​sα]+a0,i2\displaystyle~~+2a\_{2,i}a\_{1,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]+a\_{0,i}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(2​a0,i​a2,i+σi2−a1,i2​σS2)​1−α∗1−α​c∗+a2,i2​1−α∗∗1−α​c∗∗,\displaystyle~~+(2a\_{0,i}a\_{2,i}+{\sigma}^{2}\_{i}-a\_{1,i}^{2}{\sigma}^{2}\_{S})\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}+a\_{2,i}^{2}\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi​Xj​∣S>​sα]=\displaystyle\mathbb{E}\left[X\_{i}X\_{j}\mid S>s\_{\alpha}\right]= | a1,i​a1,j​𝔼​[S2​∣S>​sα]+(a1,i​a0,j+a0,i​a1,j)​𝔼​[S​∣S>​sα]\displaystyle~a\_{1,i}a\_{1,j}\mathbb{E}\left[S^{2}\mid S>s\_{\alpha}\right]+\left(a\_{1,i}a\_{0,j}+a\_{0,i}a\_{1,j}\right)\mathbb{E}\left[S\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(a1,i​a2,j+a2,i​a1,j)​1−α∗1−α​c∗​𝔼​[S∗​∣S∗>​sα]+a0,i​a0,j\displaystyle~~+\left(a\_{1,i}a\_{2,j}+a\_{2,i}a\_{1,j}\right)\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]+a\_{0,i}a\_{0,j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(a2,i​a0,j+a0,i​a2,j+σi​j−a1,i​a1,j​σS2)​1−α∗1−α​c∗+a2,i​a2,j​1−α∗∗1−α​c∗∗.\displaystyle~~+\left(a\_{2,i}a\_{0,j}+a\_{0,i}a\_{2,j}+{\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}\right)\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}+a\_{2,i}a\_{2,j}\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}. |  |

See Appendix [B](https://arxiv.org/html/2601.00568v1#A2 "Appendix B Proof for Remark 5 ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") for the derivation of these identities.

## 5 Numerical illustration

This section applies the TCM-based capital allocation results obtained in previous sections to financial losses modelled by the multivariate generalised hyperbolic (GH) distribution. A capital allocation based on both the CTE and TCMs is used to decide an appropriate capital reserve allocation.

For this illustration, we selected the historical daily log losses of four stocks, namely Boeing (BA), American Express (AXP), ExxonMobil (XOM), and Chevron (CVX), denoted by X1,…,X4X\_{1},\dots,X\_{4}, from 1 January 2020 to 31 December 2024 (1257 trading days). The daily log loss of a stock at day tt is calculated as Lt=−ln⁡(Pt/Pt−1)L\_{t}=-\ln\left(P\_{t}/P\_{t-1}\right), where PtP\_{t} is the adjusted closing price of the stock at trading day tt. Historical stock data are obtained from Yahoo Finance via the R package quantmod.

The summary statistics of the data are shown in Table [1](https://arxiv.org/html/2601.00568v1#S5.T1 "Table 1 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). We observe that all stocks exhibit non-zero skewness and that the kurtosis is much greater than 3 (the kurtosis of the normal distribution). This indicates the existence of heavy tails in the data, which can be captured by the multivariate GH distribution.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Index | Mean | Median | Minimum | Maximum | St.Dev. | Skewness | Kurtosis |
| BA | 0.000501 | 0.000422 | -0.217677 | 0.272444 | 0.032270 | 0.421802 | 15.44124 |
| AXP | -0.000737 | -0.000785 | -0.197886 | 0.160388 | 0.024025 | -0.599463 | 16.69053 |
| XOM | -0.000511 | -0.000212 | -0.119442 | 0.130391 | 0.021658 | 0.161940 | 7.63877 |
| CVX | -0.000308 | -0.000787 | -0.204904 | 0.250062 | 0.022591 | 1.072524 | 27.08356 |

Table 1: Descriptive statistics of the stocks’ daily log losses

To fit the multivariate GH distribution, we used the EM algorithm calibration in M15 implemented via the fit.ghypmv function in the R package ghyp. As our goal in this section is to illustrate the impact of incorporating the TCMs into the CTE-based capital allocation, we are not concerned with finding the best-fit model in the NMVM or GH families. For such empirical tasks, we refer to IL15 and IL19. The fitted model is 𝐗∼M​G​H4​(−1.689, 4.509×10−5, 1.380,𝝁,𝚺,𝜸)\mathbf{X}\sim MGH\_{4}(-1.689,\ 4.509\times 10^{-5},\ 1.380,\ \bm{\mu},\ \bm{\Sigma},\ \bm{\gamma}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁′=\displaystyle\bm{\mu}^{\prime}= | (2.393,−15.135,−0.474,−0.305)×10−4;\displaystyle~\left(2.393,\ -15.135,\ -0.474,\ -0.305\right)\times 10^{-4}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜸′=\displaystyle\bm{\gamma}^{\prime}= | (2.556, 7.584,−4.530,−0.0287)×10−4;\displaystyle~\left(2.556,\ 7.584,\ -4.530,\ -0.0287\right)\times 10^{-4}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=\displaystyle\bm{\Sigma}= | (9.4623.7902.7102.5383.7905.2782.5332.4172.7102.5335.4954.3382.5382.4174.3384.413)×10−4.\displaystyle~\begin{pmatrix}9.462&3.790&2.710&2.538\\ 3.790&5.278&2.533&2.417\\ 2.710&2.533&5.495&4.338\\ 2.538&2.417&4.338&4.413\end{pmatrix}\times 10^{-4}. |  |

The fitted density function of each marginal XiX\_{i} is shown below.

![Refer to caption](x1.png)


Figure 1: Marginal densities, fXi​(x)f\_{X\_{i}}(x), of X1,X2,X3,X4X\_{1},X\_{2},X\_{3},X\_{4}

From Figure [1](https://arxiv.org/html/2601.00568v1#S5.F1 "Figure 1 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), it is seen that the log losses are slightly asymmetric in general. The stock losses are positively correlated as seen from the parameter 𝚺\bm{\Sigma}, which is reasonable since companies such as XOM and CVX are from the same industry, and therefore the diversification effect is not as strong as expected for this portfolio. Among the individual stocks, BA has a positive mean log loss and a visibly heavier tail than the rest, indicating its riskiness as an investment choice.

Suppose that we have invested a total of $100 equally distributed to X1X\_{1} to X4X\_{4}. We write the total nominal loss of the portfolio as S:=w1​X1+w2​X2+w3​X3+w4​X4S:=w\_{1}X\_{1}+w\_{2}X\_{2}+w\_{3}X\_{3}+w\_{4}X\_{4} where w1,w2,w3,w4w\_{1},w\_{2},w\_{3},w\_{4} represent the nominal amounts invested into each stock (w1=⋯=w4=$​25w\_{1}=\dots=w\_{4}=\mathdollar 25 in our scenario). It is established that capital allocations based on the CTE, TV, and TCMα,3, respectively will yield the following allocation outcome:

1. (i)

   K=CTEα​(S)K=\mathrm{CTE}\_{\alpha}(S) and Ki=𝔼​[wi​Xi​∣S>​sα]K\_{i}=\mathbb{E}\left[w\_{i}X\_{i}\mid S>s\_{\alpha}\right] for all i=1,…,ni=1,\dots,n;
2. (ii)

   K=TVα​(S)K=\mathrm{TV}\_{\alpha}(S) and Ki=Cov​[wi​Xi,S​∣S>​sα]K\_{i}=\mathrm{Cov}\left[w\_{i}X\_{i},S\mid S>s\_{\alpha}\right] for all i=1,…,ni=1,\dots,n;
3. (iii)

   K=TCMα,3​(S)K=\mathrm{TCM}\_{\alpha,3}(S) and Ki=Cov​[wi​Xi,(S−CTEα​(S))2​∣S>​sα]K\_{i}=\mathrm{Cov}\left[w\_{i}X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{2}\mid S>s\_{\alpha}\right] for all i=1,…,ni=1,\dots,n,

where the capital allocated can be calculated by Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), Corollary [2](https://arxiv.org/html/2601.00568v1#Thmcorollary2 "Corollary 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), and Theorem [2](https://arxiv.org/html/2601.00568v1#Thmtheorem2 "Theorem 2. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution").

Figure [2](https://arxiv.org/html/2601.00568v1#S5.F2 "Figure 2 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") below plots CTEα​(S)\mathrm{CTE}\_{\alpha}(S), TVα​(S)\mathrm{TV}\_{\alpha}(S), and TCMα,3​(S)\mathrm{TCM}\_{\alpha,3}(S) and their allocations to each stock. It also displays the relative proportions of the capital allocated (given by Ki/KK\_{i}/K), which can be interpreted as the risk contribution by each stock. Selected capital allocation values for some quantiles are also
presented in Table [2](https://arxiv.org/html/2601.00568v1#S5.T2 "Table 2 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution").

![Refer to caption](x2.png)


Figure 2: The capital allocated to X1,X2,X3,X4X\_{1},X\_{2},X\_{3},X\_{4} based on the CTE, TV, and TCMα,3, and their relative proportions



| 𝜶\bm{\alpha} | Method | BA | AXP | XOM | CVX |
| --- | --- | --- | --- | --- | --- |
|  | CTE | 1.367 | 1.042 | 1.051 | 0.984 |
| 0.950 | TV | 1.941 | 1.826 | 1.165 | 1.317 |
|  | TCMα,3 | 84.616 | 132.798 | -11.467 | 39.308 |
|  | CTE | 1.482 | 1.136 | 1.137 | 1.067 |
| 0.960 | TV | 2.208 | 2.105 | 1.293 | 1.489 |
|  | TCMα,3 | 103.534 | 163.942 | -15.735 | 47.600 |
|  | CTE | 1.640 | 1.266 | 1.254 | 1.181 |
| 0.970 | TV | 2.614 | 2.536 | 1.480 | 1.748 |
|  | TCMα,3 | 134.353 | 215.154 | -23.241 | 60.949 |
|  | CTE | 1.884 | 1.468 | 1.432 | 1.356 |
| 0.980 | TV | 3.331 | 3.314 | 1.790 | 2.199 |
|  | TCMα,3 | 194.097 | 315.683 | -39.261 | 86.399 |
|  | CTE | 2.369 | 1.878 | 1.778 | 1.701 |
| 0.990 | TV | 5.091 | 5.303 | 2.456 | 3.280 |
|  | TCMα,3 | 364.372 | 608.061 | -91.787 | 156.936 |
|  | CTE | 4.918 | 4.180 | 3.422 | 3.463 |
| 0.999 | TV | 22.113 | 27.396 | 5.563 | 12.761 |
|  | TCMα,3 | 2940.939 | 5323.095 | -1227.183 | 1125.261 |

Table 2: Capital allocated to X1,X2,X3,X4X\_{1},X\_{2},X\_{3},X\_{4} based on the CTE, TV, and TCMα,3

The allocated proportions to BA and CVX remain stable over all α∈(0.95,1)\alpha\in(0.95,1) and for the three allocation methods based on the CTE, TV, and TCMα,3, but they are very different for AXP and XOM. When α<0.98\alpha<0.98, the allocated proportion to AXP for the TV is noticeably higher than for the CTE (increasing from approximately 24% to 30% of the total). This trend persists when switching from the TV to the TCMα,3. This observation flips for XOM. Interestingly, the risk contribution to the TCMα,3 for XOM is negative, indicating some diversification benefit to the portfolio. When α>0.98\alpha>0.98, the TV and TCMα,3 amplify the tail behaviour of AXP and XOM (relative to the CTE) to different extents. This is sensible as the TV and TCM measure different dependencies between XiX\_{i} and SS, namely the expectation and dispersion in the tail region, respectively. This demonstrates the necessity of including the TV and TCMα,3 for a more thorough understanding of the stocks’ tail behaviour.

The observations so far suggest that neither the CTE-based nor TCM-based capital allocation should be used in isolation. Therefore, we suggest a linear combination of the CTE, TV, and TCMα,3, as previously mentioned. By taking m1=1m\_{1}=1, m2=pm\_{2}=p and m3=qm\_{3}=q in ([2](https://arxiv.org/html/2601.00568v1#S2.E2 "In 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")), the total capital reserve is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K=CTEα​(S)+p⋅TVα​(S)+q⋅TCMα,3​(S),\displaystyle K=\mathrm{CTE}\_{\alpha}(S)+p\cdot\mathrm{TV\_{\alpha}}(S)+q\cdot\mathrm{TCM}\_{\alpha,3}(S), |  | (14) |

where p,q≥0p,~q\geq 0 represent the importance of the TV and TCMα,3 relative to the CTE, and α∈(0,1)\alpha\in(0,1) is the confidence level. The corresponding capital allocated to stock ii for i=1,…,4i=1,\dots,4 are given by

|  |  |  |
| --- | --- | --- |
|  | Ki=𝔼​[wi​Xi​∣S>​sα]+p⋅Cov​[wi​Xi,S​∣S>​sα]+q⋅Cov​[wi​Xi,(S−CTEα​(S))2​∣S>​sα].\displaystyle K\_{i}=\mathbb{E}\left[w\_{i}X\_{i}\mid S>s\_{\alpha}\right]+p\cdot\mathrm{Cov}\left[w\_{i}X\_{i},S\mid S>s\_{\alpha}\right]+q\cdot\mathrm{Cov}\left[w\_{i}X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{2}\mid S>s\_{\alpha}\right]. |  |

To ensure each term in ([14](https://arxiv.org/html/2601.00568v1#S5.E14 "In 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) has a similar magnitude based on their values in Table [2](https://arxiv.org/html/2601.00568v1#S5.T2 "Table 2 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), a reasonable choice for pp and qq is to select p∈[0,3]p\in[0,3] and q∈[0,0.005]q\in[0,0.005]. Figure [3](https://arxiv.org/html/2601.00568v1#S5.F3 "Figure 3 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") shows how the capital allocation varies when priority shifts from the CTE to the TV and TCMα,3, as shown by different selections of pp and qq, and Figure [4](https://arxiv.org/html/2601.00568v1#S5.F4 "Figure 4 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") shows the respective proportions of allocated capitals.

![Refer to caption](x3.png)


Figure 3: Capital allocated under different CTE-based, TV-based, and TCMα,3-based capital allocation combinations

![Refer to caption](x4.png)


Figure 4: Proportions of capital allocated under different CTE-based, TV-based, and TCMα,3-based capital allocation combinations

The overall observations are not too surprising, as the individual patterns are already displayed in Figure [2](https://arxiv.org/html/2601.00568v1#S5.F2 "Figure 2 ‣ 5 Numerical illustration ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). The more priority placed on the TV or TCMα,3, the more capital allocated for AXP, the lesser for XOM, and roughly the same for BA and CVX.

## 6 Conclusion

In this paper, we introduce a new capital allocation method based on the tail central moments (TCM), which includes the tail variance-based capital allocation of V04 and FL06. Together with the conditional tail expectation (CTE)-based capital allocation, the TCM-based capital allocation provides a more thorough risk assessment approach. This method is applied to the class of normal mean–variance mixture (NMVM) distributions, which has widespread finance and insurance applications. In particular, we derive analytical recursive expressions for the TCM and its capital allocation for the multivariate NMVM class. A numerical illustration shows that the TCM is an insightful risk metric that reveals important tail behaviours which are otherwise not detectable by the CTE alone. These results provide a readily applicable framework to assess each component’s risk contribution to the portfolio’s total risk and to quantify interconnected risks, enabling financial and insurance agents to reliably estimate their tail losses.

Appendices

## Appendix A The TCM-based Euler allocation principle

This section derives the TCM-based capital allocation using the Euler allocation principle in Remark [3](https://arxiv.org/html/2601.00568v1#Thmremark3 "Remark 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). For 𝒘=(w1,…,wn)∈ℝn\bm{w}=(w\_{1},\dots,w\_{n})\in\mathbb{R}^{n}, define L​(𝒘)=w1​X1+⋯+wn​XnL(\bm{w})=w\_{1}X\_{1}+\dots+w\_{n}X\_{n}, and the aggregate loss S=L​(1,…,1)S=L(1,\dots,1). Denote by lα​(𝒘)l\_{\alpha}(\bm{w}) the α\alpha-quantile of L​(𝒘)L(\bm{w}) for α∈(0,1)\alpha\in(0,1). A risk measure is a functional that maps random variables to the real line. A risk measure ρ\rho is positive homogeneous if for all t>0t>0 and any random variable XX, ρ(tX))=tρ(X)\rho(tX))=t\rho(X). Assuming that ρ\rho is positive homogeneous and ρ​(L​(𝒘))\rho(L(\bm{w})) is continuously differentiable in 𝒘∈ℝn\bm{w}\in\mathbb{R}^{n}, the Euler allocation principle with risk measure ρ\rho is defined as

|  |  |  |
| --- | --- | --- |
|  | K=ρ​(L​(1,…,1))​ and ​Ki=wi​∂ρ​(L​(𝒘))∂wi|𝒘=𝟏,\displaystyle K=\rho(L(1,\dots,1))\mbox{~~and~~}K\_{i}=w\_{i}\left.\frac{\partial\rho(L(\bm{w}))}{\partial w\_{i}}\right|\_{\bm{w=1}}, |  |

where KK is the capital reserve for SS and KiK\_{i} is the capital allocated to XiX\_{i}. The Euler allocation principle automatically satisfies the full allocation property since

|  |  |  |
| --- | --- | --- |
|  | ρ​(L​(𝒘))=∑i=1nwi​∂ρ​(L​(𝒘))∂wi​ holds for all 𝒘∈ℝn.\displaystyle\rho(L(\bm{w}))=\sum^{n}\_{i=1}w\_{i}\frac{\partial\rho(L(\bm{w}))}{\partial w\_{i}}\mbox{~~holds for all $\bm{w}\in\mathbb{R}^{n}$}. |  |

Remark [3](https://arxiv.org/html/2601.00568v1#Thmremark3 "Remark 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") states that the Euler allocation method is not applicable to the total capital reserve ρ​(S)=TCMα,k​(S)\rho(S)=\mathrm{TCM}\_{\alpha,k}(S) as in Definition [3](https://arxiv.org/html/2601.00568v1#Thmdefinition3 "Definition 3. ‣ 2.2 Tail central moment-based capital allocation ‣ 2 Preliminaries ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"). This is because the TCM is not positive homogeneous, and some modifications are required.

###### Proposition A.1.

Fix α∈(0,1)\alpha\in(0,1) and k∈ℕk\in\mathbb{N}. Assume that the random vector (X1,…,Xn)∈ℝn(X\_{1},\dots,X\_{n})\in\mathbb{R}^{n} satisfies Assumption 2.3 of T01. The Euler allocation principle with TCMα,k​(⋅)1/k\mathrm{TCM}\_{\alpha,k}(\cdot)^{1/k} is given by

|  |  |  |
| --- | --- | --- |
|  | K=TCMα,k​(S)1k​ and ​Ki=Cov​[Xi,(S−CTEα​(S))k−1​∣S>​sα]TCMα,k​(S)1−1k.\displaystyle K=\mathrm{TCM}\_{\alpha,k}(S)^{\frac{1}{k}}\mbox{~~and~~}K\_{i}=\frac{\mathrm{Cov}\left[X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mid S>s\_{\alpha}\right]}{\mathrm{TCM}\_{\alpha,k}(S)^{1-\frac{1}{k}}}. |  |

###### Proof.

It is easy to show that TCMα,k​(⋅)1/k\mathrm{TCM}\_{\alpha,k}(\cdot)^{1/k} is partially differentiable (refer to, e.g., T01) and positive homogeneous. We first require Corollary 4.2 of T01, which states that

|  |  |  |
| --- | --- | --- |
|  | ∂∂wi​𝔼​[L​(𝒘)k∣L​(𝒘)≥lα​(𝒘)]=k​𝔼​[Xi​L​(𝒘)k−1∣L​(𝒘)≥lα​(𝒘)].\displaystyle\frac{\partial}{\partial w\_{i}}\mathbb{E}\left[L(\bm{w})^{k}\mid L(\bm{w})\geq l\_{\alpha}(\bm{w})\right]=k\mathbb{E}\left[X\_{i}L(\bm{w})^{k-1}\mid L(\bm{w})\geq l\_{\alpha}(\bm{w})\right]. |  |

For 𝒘∈ℝn\bm{w}\in\mathbb{R}^{n}, denote by ρ∗​(𝒘)=TCMα,k​(L​(𝒘))\rho^{\*}(\bm{w})=\mathrm{TCM}\_{\alpha,k}(L(\bm{w})) and ρ​(𝒘)=TCMα,k​(L​(𝒘))1k\rho(\bm{w})=\mathrm{TCM}\_{\alpha,k}(L(\bm{w}))^{\frac{1}{k}}. Using the above result gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ρ∗​(𝒘)∂wi|𝒘=𝟏=\displaystyle\left.\frac{\partial\rho^{\*}(\bm{w})}{\partial w\_{i}}\right|\_{\bm{w=1}}= | ∂∂wi​𝔼​[(L​(𝒘)−CTEα​(L​(𝒘)))k​∣L​(𝒘)>​lα​(𝒘)]|𝒘=𝟏\displaystyle~\left.\frac{\partial}{\partial w\_{i}}\mathbb{E}\left[(L(\bm{w})-\mathrm{CTE}\_{\alpha}(L(\bm{w})))^{k}\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\right|\_{\bm{w=1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∂∂wi​(∑j=0k(kj)​(−1)j​CTEα​(L​(𝒘))j​𝔼​[L​(𝒘)k−j​∣L​(𝒘)>​lα​(𝒘)])|𝒘=𝟏\displaystyle~\left.\frac{\partial}{\partial w\_{i}}\left(\sum\_{j=0}^{k}\binom{k}{j}(-1)^{j}\mathrm{CTE}\_{\alpha}(L(\bm{w}))^{j}\mathbb{E}\left[L(\bm{w})^{k-j}\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\right)\right|\_{\bm{w=1}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0k(kj)​(−1)j​∂∂wi​(CTEα​(L​(𝒘))j​𝔼​[L​(𝒘)k−j​∣L​(𝒘)>​lα​(𝒘)])|𝒘=𝟏,\displaystyle~\sum\_{j=0}^{k}\binom{k}{j}(-1)^{j}\left.\frac{\partial}{\partial w\_{i}}\left(\mathrm{CTE}\_{\alpha}(L(\bm{w}))^{j}\mathbb{E}\left[L(\bm{w})^{k-j}\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\right)\right|\_{\bm{w=1}}, |  | (A.1) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂∂wi​(CTEα​(L​(𝒘))j​𝔼​[L​(𝒘)k−j​∣L​(𝒘)>​lα​(𝒘)])|𝒘=𝟏\displaystyle~\left.\frac{\partial}{\partial w\_{i}}\left(\mathrm{CTE}\_{\alpha}(L(\bm{w}))^{j}\mathbb{E}\left[L(\bm{w})^{k-j}\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\right)\right|\_{\bm{w=1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | CTEα​(L​(𝒘))j​∂∂wi​𝔼​[L​(𝒘)k−j​∣L​(𝒘)>​lα​(𝒘)]|𝒘=𝟏\displaystyle~\mathrm{CTE}\_{\alpha}(L(\bm{w}))^{j}\left.\frac{\partial}{\partial w\_{i}}\mathbb{E}\left[L(\bm{w})^{k-j}\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\right|\_{\bm{w=1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[L​(𝒘)k−j​∣L​(𝒘)>​lα​(𝒘)]​∂∂wi​(𝔼​[L​(𝒘)​∣L​(𝒘)>​lα​(𝒘)])j|𝒘=𝟏\displaystyle~+\mathbb{E}\left[L(\bm{w})^{k-j}\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\left.\frac{\partial}{\partial w\_{i}}\left(\mathbb{E}\left[L(\bm{w})\mid L(\bm{w})>l\_{\alpha}(\bm{w})\right]\right)^{j}\right|\_{\bm{w=1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | CTEα​(S)j⋅(k−j)​𝔼​[Xi​Sk−j−1​∣S>​sα]+𝔼​[Sk−j​∣S>​sα]⋅j​CTEα​(S)j−1​𝔼​[Xi​∣S>​sα].\displaystyle~\mathrm{CTE}\_{\alpha}(S)^{j}\cdot(k-j)\mathbb{E}\left[X\_{i}S^{k-j-1}\mid S>s\_{\alpha}\right]+\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right]\cdot j~\mathrm{CTE}\_{\alpha}(S)^{j-1}\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]. |  |

Hence, ([A](https://arxiv.org/html/2601.00568v1#A1.Ex112 "Proof. ‣ Appendix A The TCM-based Euler allocation principle ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑j=0k(kj)​(k−j)​(−1)j​CTEα​(S)j​𝔼​[Xi​Sk−j−1​∣S>​sα]\displaystyle~\sum\_{j=0}^{k}\binom{k}{j}(k-j)(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j}\mathbb{E}\left[X\_{i}S^{k-j-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=0k(kj)​(j)​(−1)j​CTEα​(S)j−1​𝔼​[Xi​∣S>​sα]​𝔼​[Sk−j​∣S>​sα]\displaystyle~+\sum\_{j=0}^{k}\binom{k}{j}(j)(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j-1}\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0k−1(kj)​(k−j)​(−1)j​CTEα​(S)j​𝔼​[Xi​Sk−j−1​∣S>​sα]+0\displaystyle~\sum\_{j=0}^{k-1}\binom{k}{j}(k-j)(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j}\mathbb{E}\left[X\_{i}S^{k-j-1}\mid S>s\_{\alpha}\right]+0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +0+∑j=1k(kj)​(j)​(−1)j​CTEα​(S)j−1​𝔼​[Xi​∣S>​sα]​𝔼​[Sk−j​∣S>​sα]\displaystyle~+0+\sum\_{j=1}^{k}\binom{k}{j}(j)(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j-1}\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | k​∑j=0k−1(k−1j)​(−1)j​CTEα​(S)j​𝔼​[Xi​Sk−j−1​∣S>​sα]\displaystyle~k\sum\_{j=0}^{k-1}\binom{k-1}{j}(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j}\mathbb{E}\left[X\_{i}S^{k-j-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=0k−1(kj+1)​(j+1)​(−1)j+1​CTEα​(S)j​𝔼​[Xi​∣S>​sα]​𝔼​[Sk−j−1​∣S>​sα]\displaystyle~+\sum\_{j=0}^{k-1}\binom{k}{j+1}(j+1)(-1)^{j+1}\mathrm{CTE}\_{\alpha}(S)^{j}\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-j-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | k​∑j=0k−1(k−1j)​(−1)j​CTEα​(S)j​𝔼​[Xi​Sk−j−1​∣S>​sα]\displaystyle~k\sum\_{j=0}^{k-1}\binom{k-1}{j}(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j}\mathbb{E}\left[X\_{i}S^{k-j-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −k​∑j=0k−1(k−1j)​(−1)j​CTEα​(S)j​𝔼​[Xi​∣S>​sα]​𝔼​[Sk−j−1​∣S>​sα]\displaystyle~-k\sum\_{j=0}^{k-1}\binom{k-1}{j}(-1)^{j}\mathrm{CTE}\_{\alpha}(S)^{j}\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[S^{k-j-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | k​𝔼​[Xi​∑j=0k−1(k−1j)​(−CTEα​(S))j​Sk−1−j​∣S>​sα]\displaystyle~k\mathbb{E}\left[X\_{i}\sum\_{j=0}^{k-1}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}S^{k-1-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −k​𝔼​[Xi​∣S>​sα]​𝔼​[∑j=0k−1(k−1j)​(−CTEα​(S))j​Sk−1−j​∣S>​sα]\displaystyle~-k\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[\sum\_{j=0}^{k-1}\binom{k-1}{j}(-\mathrm{CTE}\_{\alpha}(S))^{j}S^{k-1-j}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | k​𝔼​[Xi​(S−CTEα​(S))k−1​∣S>​sα]−k​𝔼​[Xi​∣S>​sα]​𝔼​[(S−CTEα​(S))k−1​∣S>​sα]\displaystyle~k\mathbb{E}\left[X\_{i}\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right]-k\mathbb{E}\left[X\_{i}\mid S>s\_{\alpha}\right]\mathbb{E}\left[\left(S-\mathrm{CTE}\_{\alpha}(S)\right)^{k-1}\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | k​Cov​[Xi,(S−CTEα​(S))k−1​∣S>​sα].\displaystyle~k\mathrm{Cov}\left[X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mid S>s\_{\alpha}\right]. |  |

Finally, the capital allocated to each component is given by

|  |  |  |
| --- | --- | --- |
|  | Ki=∂ρ​(𝒘)∂wi|𝒘=𝟏=1k​TCMα,k​(S)1−1k​∂ρ∗​(𝒘)∂wi|𝒘=𝟏=Cov​[Xi,(S−CTEα​(S))k−1​∣S>​sα]TCMα,k​(S)1−1k.\displaystyle K\_{i}=\left.\frac{\partial\rho(\bm{w})}{\partial w\_{i}}\right|\_{\bm{w=1}}=\frac{1}{k~\mathrm{TCM}\_{\alpha,k}(S)^{1-\frac{1}{k}}}\left.\frac{\partial\rho^{\*}(\bm{w})}{\partial w\_{i}}\right|\_{\bm{w=1}}=\frac{\mathrm{Cov}\left[X\_{i},(S-\mathrm{CTE}\_{\alpha}(S))^{k-1}\mid S>s\_{\alpha}\right]}{\mathrm{TCM}\_{\alpha,k}(S)^{1-\frac{1}{k}}}. |  |

The proof is complete.
∎

## Appendix B Proof for Remark [5](https://arxiv.org/html/2601.00568v1#Thmremark5 "Remark 5. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")

We revisit the identities given in Remark [5](https://arxiv.org/html/2601.00568v1#Thmremark5 "Remark 5. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), which is given below, in more detail.

###### Lemma A.1.

Consider the same random variables X1,…,XnX\_{1},\dots,X\_{n}, and SS in Lemma [3](https://arxiv.org/html/2601.00568v1#Thmlemma3 "Lemma 3. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution"), as well as all related parameters and coefficients. We have the following identities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi2​∣S>​sα]=\displaystyle\mathbb{E}\left[X\_{i}^{2}\mid S>s\_{\alpha}\right]= | a1,i2​𝔼​[S2​∣S>​sα]+2​a0,i​a1,i​𝔼​[S​∣S>​sα]\displaystyle~a\_{1,i}^{2}\mathbb{E}\left[S^{2}\mid S>s\_{\alpha}\right]+2a\_{0,i}a\_{1,i}\mathbb{E}\left[S\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​a2,i​a1,i​1−α∗1−α​c∗​𝔼​[S∗​∣S∗>​sα]+a0,i2\displaystyle~~+2a\_{2,i}a\_{1,i}\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]+a\_{0,i}^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(2​a0,i​a2,i+σi2−a1,i2​σS2)​1−α∗1−α​c∗+a2,i2​1−α∗∗1−α​c∗∗,\displaystyle~~+(2a\_{0,i}a\_{2,i}+{\sigma}^{2}\_{i}-a\_{1,i}^{2}{\sigma}^{2}\_{S})\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}+a\_{2,i}^{2}\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}, |  | (A.2) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi​Xj​∣S>​sα]=\displaystyle\mathbb{E}\left[X\_{i}X\_{j}\mid S>s\_{\alpha}\right]= | a1,i​a1,j​𝔼​[S2​∣S>​sα]+(a1,i​a0,j+a0,i​a1,j)​𝔼​[S​∣S>​sα]\displaystyle~a\_{1,i}a\_{1,j}\mathbb{E}\left[S^{2}\mid S>s\_{\alpha}\right]+\left(a\_{1,i}a\_{0,j}+a\_{0,i}a\_{1,j}\right)\mathbb{E}\left[S\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(a1,i​a2,j+a2,i​a1,j)​1−α∗1−α​c∗​𝔼​[S∗​∣S∗>​sα]+a0,i​a0,j\displaystyle~~+\left(a\_{1,i}a\_{2,j}+a\_{2,i}a\_{1,j}\right)\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]+a\_{0,i}a\_{0,j} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(a2,i​a0,j+a0,i​a2,j+σi​j−a1,i​a1,j​σS2)​1−α∗1−α​c∗+a2,i​a2,j​1−α∗∗1−α​c∗∗.\displaystyle~~+\left(a\_{2,i}a\_{0,j}+a\_{0,i}a\_{2,j}+{\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}\right)\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}+a\_{2,i}a\_{2,j}\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}. |  | (A.3) |

###### Proof.

Before proving the lemma, we first provide a useful intermediate result below. Fix k∈ℕk\in\mathbb{N}, l∈ℕ0l\in\mathbb{N}\_{0}, α∈(0,1)\alpha\in(0,1), and let random variable Θ∗(l)\Theta^{\*(l)} has density π∗(l)​(θ)\pi^{\*(l)}(\theta), with θ>0\theta>0. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫sα∞∫0∞sk​θl​π​(θ)​fS∣θ​(s)​𝑑θ​𝑑s=\displaystyle\int^{\infty}\_{s\_{\alpha}}\int^{\infty}\_{0}s^{k}\theta^{l}\pi(\theta)f\_{S\mid\theta}(s)\,d\theta\,ds= | c∗(l)​∫0∞π∗(l)​(θ)​∫sα∞sk​fS∣θ​(s)​𝑑s​𝑑θ\displaystyle~c^{\*(l)}\int^{\infty}\_{0}\pi^{\*(l)}(\theta)\int^{\infty}\_{s\_{\alpha}}s^{k}f\_{S\mid\theta}(s)\,ds\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | c∗(l)​∫0∞π∗(l)​(θ)​∫sα∞sk​fS∗(l)|θ​(s)​𝑑s​𝑑θ\displaystyle~c^{\*(l)}\int^{\infty}\_{0}\pi^{\*(l)}(\theta)\int^{\infty}\_{s\_{\alpha}}s^{k}f\_{S^{\*(l)}|\theta}(s)\,ds\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (1−α∗(l))​c∗(l)​∫0∞π∗(l)​(θ)​𝔼​[(S∗(l))k​∣S∗(l)>​sα,Θ∗(l)=θ]​𝑑θ\displaystyle~(1-\alpha^{\*(l)})c^{\*(l)}\int^{\infty}\_{0}\pi^{\*(l)}(\theta)\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha},\Theta^{\*(l)}=\theta\right]\,d\theta |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (1−α∗(l))​c∗(l)​𝔼​[(S∗(l))k​∣S∗(l)>​sα],\displaystyle~(1-\alpha^{\*(l)})c^{\*(l)}\mathbb{E}\left[(S^{\*(l)})^{k}\mid S^{\*(l)}>s\_{\alpha}\right], |  | (A.4) |

where the second equality is due to fS∗(l)|Θ∗(l)​(s∣θ)=fS|Θ∗(l)​(s∣θ)f\_{S^{\*(l)}|\Theta^{\*(l)}}(s\mid\theta)=f\_{S|\Theta^{\*(l)}}(s\mid\theta), based on the definition of S∗(l)S^{\*(l)}.

Using (36) of KK19 (and directly replacing XiX\_{i} with Xi​XjX\_{i}X\_{j}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi​Xj​∣S>​sα]=\displaystyle\mathbb{E}\left[X\_{i}X\_{j}\mid S>s\_{\alpha}\right]= | 11−α​∫sα∞𝔼​[Xi​Xj∣S=s]​fS​(s)​𝑑s\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}\mathbb{E}\left[X\_{i}X\_{j}\mid S=s\right]f\_{S}(s)\,ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 11−α​∫sα∞∫0∞𝔼​[Xi​Xj∣S=s,Θ=θ]​fS∣θ​(s)​π​(θ)​𝑑θ​𝑑s.\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}\int^{\infty}\_{0}\mathbb{E}\left[X\_{i}X\_{j}\mid S=s,\Theta=\theta\right]f\_{S\mid\theta}(s)\pi(\theta)\,d\theta\,ds. |  | (A.5) |

On the other hand, Lemma [4](https://arxiv.org/html/2601.00568v1#Thmlemma4 "Lemma 4. ‣ 4 Capital allocation for multivariate NMVM distributions ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution") implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xi​Xj∣S=s,Θ=θ]=\displaystyle\mathbb{E}\left[X\_{i}X\_{j}\mid S=s,\Theta=\theta\right]= | 𝔼[Xi∣S=s,Θ=θ]𝔼[Xj∣S=s,Θ=θ]+Cov[Xi,Xj∣S=s,Θ=θ]\displaystyle~\mathbb{E}\left[X\_{i}\mid S=s,\Theta=\theta\right]\mathbb{E}\left[X\_{j}\mid S=s,\Theta=\theta\right]+\mathrm{Cov}\left[X\_{i},X\_{j}\mid S=s,\Theta=\theta\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (a0,i+a2,i​θ+a1,i​s)​(a0,j+a2,j​θ+a1,j​s)+θ​(σi​j−a1,i​a1,j​σS2)\displaystyle~\left(a\_{0,i}+a\_{2,i}\theta+a\_{1,i}s\right)\left(a\_{0,j}+a\_{2,j}\theta+a\_{1,j}s\right)+\theta({\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a1,i​a1,j​s2+(a1,i​a0,j+a0,i​a1,j)​s+(a1,i​a2,j+a2,i​a1,j)​θ​s\displaystyle~a\_{1,i}a\_{1,j}s^{2}+\left(a\_{1,i}a\_{0,j}+a\_{0,i}a\_{1,j}\right)s+\left(a\_{1,i}a\_{2,j}+a\_{2,i}a\_{1,j}\right)\theta s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,i​a2,j​θ2+(a2,i​a0,j+a0,i​a2,j+σi​j−a1,i​a1,j​σS2)​θ+a0,i​a0,j.\displaystyle~~+a\_{2,i}a\_{2,j}\theta^{2}+\left(a\_{2,i}a\_{0,j}+a\_{0,i}a\_{2,j}+{\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}\right)\theta+a\_{0,i}a\_{0,j}. |  |

Substituting the above result into ([B](https://arxiv.org/html/2601.00568v1#A2.Ex138 "Proof. ‣ Appendix B Proof for Remark 5 ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) and applying ([B](https://arxiv.org/html/2601.00568v1#A2.Ex135 "Proof. ‣ Appendix B Proof for Remark 5 ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 11−α​∫sα∞∫0∞𝔼​[Xi​Xj∣S=s,Θ=θ]​π​(θ)​𝑑θ​fS​(s)​𝑑s\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}\int^{\infty}\_{0}\mathbb{E}\left[X\_{i}X\_{j}\mid S=s,\Theta=\theta\right]\pi(\theta)\,d\theta f\_{S}(s)\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 11−α∫sα∞∫0∞(a1,ia1,js2+(a1,ia0,j+a0,ia1,j)s+(a1,ia2,j+a2,ia1,j)θs\displaystyle~\frac{1}{1-\alpha}\int^{\infty}\_{s\_{\alpha}}\int^{\infty}\_{0}\big(a\_{1,i}a\_{1,j}s^{2}+\left(a\_{1,i}a\_{0,j}+a\_{0,i}a\_{1,j}\right)s+\left(a\_{1,i}a\_{2,j}+a\_{2,i}a\_{1,j}\right)\theta s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +a2,ia2,jθ2+(a2,ia0,j+a0,ia2,j+σi​j−a1,ia1,jσS2)θ+a0,ia0,j)π(θ)fS∣θ(s)dθds\displaystyle~~~~~~~~~~~~~~~~~~~~~~+a\_{2,i}a\_{2,j}\theta^{2}+\left(a\_{2,i}a\_{0,j}+a\_{0,i}a\_{2,j}+{\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}\right)\theta+a\_{0,i}a\_{0,j}\big)\pi(\theta)f\_{S\mid\theta}(s)\,d\theta\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | a1,i​a1,j​𝔼​[S2​∣S>​sα]+(a1,i​a0,j+a0,i​a1,j)​𝔼​[S​∣S>​sα]\displaystyle~a\_{1,i}a\_{1,j}\mathbb{E}\left[S^{2}\mid S>s\_{\alpha}\right]+\left(a\_{1,i}a\_{0,j}+a\_{0,i}a\_{1,j}\right)\mathbb{E}\left[S\mid S>s\_{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(a1,i​a2,j+a2,i​a1,j)​1−α∗1−α​c∗​𝔼​[S∗​∣S∗>​sα]+a0,i​a0,j\displaystyle~~+\left(a\_{1,i}a\_{2,j}+a\_{2,i}a\_{1,j}\right)\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}\mathbb{E}\left[S^{\*}\mid S^{\*}>s\_{\alpha}\right]+a\_{0,i}a\_{0,j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(a2,i​a0,j+a0,i​a2,j+σi​j−a1,i​a1,j​σS2)​1−α∗1−α​c∗+a2,i​a2,j​1−α∗∗1−α​c∗∗,\displaystyle~~+\left(a\_{2,i}a\_{0,j}+a\_{0,i}a\_{2,j}+{\sigma}\_{ij}-a\_{1,i}a\_{1,j}{\sigma}^{2}\_{S}\right)\frac{1-\alpha^{\*}}{1-\alpha}c^{\*}+a\_{2,i}a\_{2,j}\frac{1-\alpha^{\*\*}}{1-\alpha}c^{\*\*}, |  |

thus ([A.1](https://arxiv.org/html/2601.00568v1#A2.Ex133 "Lemma A.1. ‣ Appendix B Proof for Remark 5 ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) is obtained. By setting j=ij=i, ([A.1](https://arxiv.org/html/2601.00568v1#A2.Ex131 "Lemma A.1. ‣ Appendix B Proof for Remark 5 ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")) is directly implied from ([A.1](https://arxiv.org/html/2601.00568v1#A2.Ex133 "Lemma A.1. ‣ Appendix B Proof for Remark 5 ‣ Capital allocation and tail central moments for the multivariate normal mean-variance mixture distribution")).
∎