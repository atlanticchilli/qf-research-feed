---
authors:
- Aurélien Alfonsi
- Ahmed Kebaier
doc_id: arxiv:2602.18234v1
family_id: arxiv:2602.18234
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Weak error approximation for rough and Gaussian mean-reverting stochastic volatility
  models
url_abs: http://arxiv.org/abs/2602.18234v1
url_html: https://arxiv.org/html/2602.18234v1
venue: arXiv q-fin
version: 1
year: 2026
---


Aurélien Alfonsi
CERMICS, ENPC, Institut Polytechnique de Paris, CNRS, Marne-la-Vallée, France & MathRisk team-project, Inria Paris, France.
[aurelien.alfonsi@enpc.fr](mailto:aurelien.alfonsi@enpc.fr)
 and 
Ahmed Kebaier
LaMME, CNRS, UMR 8071, Université Évry Paris Saclay, 91037, Évry, France.
[ahmed.kebaier@univ-evry.fr](mailto:ahmed.kebaier@univ-evry.fr)

###### Abstract.

For a class of stochastic models with Gaussian and rough mean-reverting volatility that embeds the genuine rough Stein-Stein model, we study the weak approximation rate when using a Euler type scheme with integrated kernels. Our first result is a weak convergence rate for the discretised rough Ornstein-Uhlenbeck process, that is essentially in min⁡(3​α−1,1)\min(3\alpha-1,1), where tα−1Γ​(α)\frac{t^{\alpha-1}}{\Gamma(\alpha)} is the fractional convolution kernel with α∈(1/2,1)\alpha\in(1/2,1). Then, our main result is to obtain the same convergence rate for the corresponding stochastic rough volatility model with polynomial test functions.

###### Key words and phrases:

Stochastic Volterra Equation, Rough volatility model, Weak error rate, Stein and Stein model, Malliavin calculus

###### 2010 Mathematics Subject Classification:

60H35 60G22 60L90 91G60

The authors benefited from the support of the “chaire Risques financiers”, Fondation du Risque.

## 1. Introduction

In recent years, the modelling of financial markets has evolved significantly beyond classical stochastic differential equations (SDEs) to account for more realistic dynamics, including rough volatility and long memory effects. Traditional models, such as the Heston model or the Black-Scholes framework, often fail to capture the persistent roughness observed in empirical volatility time series Gatheral et al. [[13](https://arxiv.org/html/2602.18234v1#bib.bib13)]. To address these limitations, stochastic Volterra equations (SVEs) have emerged as a powerful tool, allowing for non-Markovian dynamics and flexible autocorrelation structures.

Among the various approaches within this framework, the Stein-Stein stochastic volatility model [[24](https://arxiv.org/html/2602.18234v1#bib.bib24), [23](https://arxiv.org/html/2602.18234v1#bib.bib23)] has been revisited in the context of rough volatility, providing a tractable yet realistic description of asset price dynamics. Recent studies by Bayer et al. [[4](https://arxiv.org/html/2602.18234v1#bib.bib4)], El Euch and Rosenbaum [[9](https://arxiv.org/html/2602.18234v1#bib.bib9)] have demonstrated that rough volatility models, particularly those driven by fractional Brownian motion, outperform traditional models in capturing the observed roughness and persistence in volatility. The extension of the mean-reverting Stein-Stein model to a stochastic Volterra (see e.g. Abi Jaber [[1](https://arxiv.org/html/2602.18234v1#bib.bib1)] and very recently Abi Jaber et al. [[3](https://arxiv.org/html/2602.18234v1#bib.bib3), [2](https://arxiv.org/html/2602.18234v1#bib.bib2)]) setting offers a promising direction, combining analytical tractability with empirical accuracy.
This paper investigates the weak error of Euler-type approximation schemes for a generalized rough stochastic volatility version of the Stein-Stein model.

More precisely, we focus on the weak error for asset log-price models LL with a Gaussian mean-reverting rough volatility process. Namely, we are interested in the following model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Lt=L0+∫0tb​(Xs)​𝑑s+∫0tf​(Xs)​𝑑Bs,Xt=x0+∫0t(t−s)α−1Γ​(α)​(κ1+κ2​Xs)​𝑑s+σ​∫0t(t−s)α−1Γ​(α)​𝑑Ws,\displaystyle\begin{cases}L\_{t}&=L\_{0}+\int\_{0}^{t}b(X\_{s})ds+\int\_{0}^{t}f(X\_{s})dB\_{s},\\ X\_{t}&=x\_{0}+\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}(\kappa\_{1}+\kappa\_{2}X\_{s})ds+\sigma\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s},\end{cases} |  | (1.1) |

where x0,κ1,κ2,L0∈ℝx\_{0},\kappa\_{1},\kappa\_{2},L\_{0}\in{\mathbb{R}}, σ>0\sigma>0, ρ∈[−1,1]\rho\in[-1,1], α∈(1/2,1]\alpha\in(1/2,1], Bt=(ρ​Wt+1−ρ2​Wt⊥)B\_{t}=(\rho W\_{t}+\sqrt{1-\rho^{2}}W^{\bot}\_{t}) with WW and W⊥W^{\bot} independent real Brownian motions on a given filtered probability space (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) and b,f:ℝ→ℝ+b,f:{\mathbb{R}}\to{\mathbb{R}}\_{+} are smooth functions. The case b=−12​f2b=-\frac{1}{2}f^{2} corresponds to a stochastic volatility model. In particular, when f​(x)=xf(x)=x this model encompasses the rough Stein-Stein model, see [[1](https://arxiv.org/html/2602.18234v1#bib.bib1)]. Here, without loss of generality, we assume a zero interest rate.
We consider a time horizon T>0T>0 and a regular time grid tk=k​Tnt\_{k}=\frac{kT}{n} for n≥1n\geq 1 and k∈{0,…,n}k\in\{0,\dots,n\}. For t∈[0,T]t\in[0,T], we denote η​(t)=tk\eta(t)=t\_{k} if tk≤t<tk+1t\_{k}\leq t<t\_{k+1} and consider the following scheme for t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Lˇtn=L0+∫0tb​(Xˇnη​(s))​𝑑s+∫0tf​(Xˇnη​(s))​𝑑Bs,Xˇtn=x0+∫0t(t−s)α−1Γ​(α)​(κ1+κ2​Xˇnη​(s))​𝑑s+σ​∫0t(t−s)α−1Γ​(α)​𝑑Ws.\displaystyle\begin{cases}\check{L}^{n}\_{t}&=L\_{0}+\int\_{0}^{t}b({\check{X}^{n}}\_{\eta(s)})ds+\int\_{0}^{t}f({\check{X}^{n}}\_{\eta(s)})dB\_{s},\\ \check{X}^{n}\_{t}&=x\_{0}+\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}(\kappa\_{1}+\kappa\_{2}{\check{X}^{n}}\_{\eta(s)})ds+\sigma\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s}.\end{cases} |  | (1.2) |

The analysis of numerical approximation methods for rough SDEs is known to be a difficult issue, which is a current hot topic of research. Fukasawa and Ugai [[11](https://arxiv.org/html/2602.18234v1#bib.bib11)] have studied, for more general coefficients, the limit distribution of nα−1/2​(XˇTn−XT)n^{\alpha-1/2}(\check{X}^{n}\_{T}-X\_{T}). Jourdain and Pagès [[16](https://arxiv.org/html/2602.18234v1#bib.bib16)] have obtained the strong error rate for more general kernels and coefficients, which is in O​(n1/2−α)O(n^{1/2-\alpha}) for the rough kernel with time-homogeneous coefficients. These results give a straightforward upper bound for the weak error on the volatility process

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Ψ​(XˇTn)]−𝔼​[Ψ​(XT)],{\mathbb{E}}[\Psi(\check{X}^{n}\_{T})]-{\mathbb{E}}[\Psi(X\_{T})], |  |

for Lipschitz test functions Ψ:ℝ→ℝ\Psi:{\mathbb{R}}\to{\mathbb{R}}. In the literature, the weak error has been mostly studied for the asset price component of the model, namely 𝔼​[Φ​(LˇTn)]−𝔼​[Φ​(LT)]{\mathbb{E}}[\Phi(\check{L}^{n}\_{T})]-{\mathbb{E}}[\Phi(L\_{T})], for Φ:ℝ→ℝ\Phi:{\mathbb{R}}\to{\mathbb{R}}. However, up to our knowledge, these studies bring only for the particular case κ1=κ2=0\kappa\_{1}=\kappa\_{2}=0, where there is no approximation error on the volatility process but only on the process LL. These works also assume that b=0b=0. More precisely, Bayer et al. [[6](https://arxiv.org/html/2602.18234v1#bib.bib6)] have obtained a weak error rate of O​(n−α)O(n^{-\alpha}) for f​(x)=xf(x)=x and ρ=1\rho=1. Bayer et al. [[5](https://arxiv.org/html/2602.18234v1#bib.bib5)] have further shown by using Malliavin calculus a rate of O​(n1−2​α)O(n^{1-2\alpha}), but for a larger family of functions ff (namely 𝒞2\mathcal{C}^{2} with a polynomial growth assumption). A decisive step has then been reached by Gassiat [[12](https://arxiv.org/html/2602.18234v1#bib.bib12)] who has shown a sharper weak error rate of O​(𝐯n​(α))O({\bf v}\_{n}(\alpha)) for the cubic test function, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐯n​(α)={1n​ if ​α∈(2/3,1)log⁡(n)n​ if ​α=2/31n3​α−1​ if ​α∈(1/2,2/3).{\bf v}\_{n}(\alpha)=\begin{cases}\frac{1}{n}\text{ if }\alpha\in(2/3,1)\\ \frac{\log(n)}{n}\text{ if }\alpha=2/3\\ \frac{1}{n^{3\alpha-1}}\text{ if }\alpha\in(1/2,2/3).\end{cases} |  | (1.3) |

More recently, Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] have generalized his analysis to encompass polynomial test functions Φ\Phi, smooth functions ff with derivatives having a sub-exponential growth, and ρ∈[−1,1]\rho\in[-1,1]. Besides, Bonesini et al. [[7](https://arxiv.org/html/2602.18234v1#bib.bib7)] obtain the same rate for the same model but for more general test functions Φ\Phi, by using a different analysis based on path-dependent PDE. A nice summary of these different rates of convergence is given in a table of [[7](https://arxiv.org/html/2602.18234v1#bib.bib7), Section 1.2], with the Hurst exponent H=α−1/2∈(0,1/2)H=\alpha-1/2\in(0,1/2).

In contrast with these studies, we consider coefficients κ1,κ2∈ℝ\kappa\_{1},\kappa\_{2}\in{\mathbb{R}} and bb possibly different from 0, which allows to reach the genuine rough Stein-Stein model [[1](https://arxiv.org/html/2602.18234v1#bib.bib1), Eq. (1.5) and (1.6)]. It allows to have a stationary distribution for the volatility XX when κ2<0\kappa\_{2}<0, see Corollary [2.5](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem5 "Corollary 2.5. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), which is an interesting feature for modelling purposes. Note that when κ2≠0\kappa\_{2}\not=0, the scheme ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) introduces a discretisation error on the volatility that we handle in this paper. Our first contribution in this paper is to analyse the weak convergence of the rough Volterra Ornstein-Uhlenbeck process that represents the volatility in ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). We prove that for any 𝒞2\mathcal{C}^{2} test functions Ψ\Psi such that Ψ\Psi, Ψ′\Psi^{\prime} and Ψ′′\Psi^{\prime\prime} have exponential growth, 𝔼​[Ψ​(XˇTn)]−𝔼​[Ψ​(XT)]=O​(𝐯n​(α)){\mathbb{E}}[\Psi(\check{X}^{n}\_{T})]-{\mathbb{E}}[\Psi(X\_{T})]=O({\bf v}\_{n}(\alpha)), see Theorem [2.7](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). This is the main result of Section [2](https://arxiv.org/html/2602.18234v1#S2 "2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), that also presents key tools to analyse the weak approximation error on the process LL. Then, Section [3](https://arxiv.org/html/2602.18234v1#S3 "3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") presents the study of the weak error for 𝔼​[(LˇTn)3]−𝔼​[(LT)3]{\mathbb{E}}[(\check{L}^{n}\_{T})^{3}]-{\mathbb{E}}[(L\_{T})^{3}] and b=0b=0. It is noticed in [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Proposition 6.1] that the cubic case allows to get familiar with the structure of the weak error rate, avoiding too much heavy notation, and prepares for tackling the general polynomial case. We prove in Theorem [3.2](https://arxiv.org/html/2602.18234v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") that 𝔼​[(LˇTn)3]−𝔼​[(LT)3]=O​(𝐯n​(α)){\mathbb{E}}[(\check{L}^{n}\_{T})^{3}]-{\mathbb{E}}[(L\_{T})^{3}]=O({\bf v}\_{n}(\alpha)) when the coefficient ff is 𝒞3\mathcal{C}^{3}, with f(i)f^{(i)} having exponential growth for 0≤i≤30\leq i\leq 3. Section [4](https://arxiv.org/html/2602.18234v1#S4 "4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") is dedicated to our main result (Theorem [4.1](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")): 𝔼​[Φ​(LˇTn)]−𝔼​[Φ​(LT)]=O​(𝐯n​(α)){\mathbb{E}}[\Phi(\check{L}^{n}\_{T})]-{\mathbb{E}}[\Phi(L\_{T})]=O({\bf v}\_{n}(\alpha)) for any polynomial test function Φ\Phi, when the coefficients bb and ff are 𝒞∞\mathcal{C}^{\infty} with all derivatives of exponential growth. For this last result, we extend the framework proposed by Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] to our setting. Finally, the two appendix sections are devoted to useful results and technical proofs.

## 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process

We focus in this section on the main properties of the rough volatility process. The first subsection is devoted to the process XX itself and calculates its expectation and covariance functions as well as its Malliavin derivative. We also prove a crucial estimate for the analysis of the weak error, see Theorem [2.6](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). The second subsection shows a weak error results on the rough Ornstein-Uhlenbeck process. To prove it, we establish key estimates on the error between the process and its approximation Xˇn{\check{X}^{n}} for the expectation and the covariance. These estimates will be essential also in the next sections to estimate the weak error in the rough Stein and Stein model.

We recall few classical results concerning the special functions that we will use through the paper. Let Γ​(α)=∫0∞tα−1​e−t​𝑑t\Gamma(\alpha)=\int\_{0}^{\infty}t^{\alpha-1}e^{-t}dt denote the Euler function. For α,β>0\alpha,\beta>0, we have Γ​(α+β)Γ​(α)​Γ​(β)​∫01xα−1​(1−x)β−1​𝑑x=1\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\int\_{0}^{1}x^{\alpha-1}(1-x)^{\beta-1}dx=1 and therefore for any 0≤s<t0\leq s<t,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫st(u−s)α−1Γ​(α)​(t−u)β−1Γ​(β)​𝑑u=tα+β−1Γ​(α+β),\int\_{s}^{t}\frac{(u-s)^{\alpha-1}}{\Gamma(\alpha)}\frac{(t-u)^{\beta-1}}{\Gamma(\beta)}du=\frac{t^{\alpha+\beta-1}}{{\Gamma(\alpha+\beta)}}, |  | (2.1) |

by using the change of variable u=s+x​(t−s)u=s+x(t-s). We also recall the confluent hypergeometric function [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Eq. 15.6.1 and 15.1.2] that is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2F1(a,b,c;z)=Γ​(c)Γ​(b)​Γ​(c−b)∫01tb−1​(1−t)c−b−1(1−z​t)adt\_{2}F\_{1}(a,b,c;z)=\frac{\Gamma(c)}{\Gamma(b)\Gamma(c-b)}\int\_{0}^{1}\frac{t^{b-1}(1-t)^{c-b-1}}{(1-zt)^{a}}dt |  | (2.2) |

for z∈[0,1)z\in[0,1), c>b>0c>b>0. For z=1z=1, the function can be extended continuously provided that c−a−b>0c-a-b>0.

### 2.1. The rough Ornstein-Uhlenbeck process

###### Proposition 2.1.

Let XX be the solution of the Stochastic Volterra Equation ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).
Then, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xt]=∑i=0∞κ2i​(x0​tα​iΓ​(α​i+1)+κ1​tα​(i+1)Γ​(α​(i+1)+1))=x0​Eα​(κ2​tα)+κ1κ2​(Eα​(κ2​tα)−1),{\mathbb{E}}[X\_{t}]=\sum\_{i=0}^{\infty}\kappa\_{2}^{i}\left(x\_{0}\frac{t^{\alpha i}}{\Gamma(\alpha i+1)}+\kappa\_{1}\frac{t^{\alpha(i+1)}}{\Gamma(\alpha(i+1)+1)}\right)=x\_{0}E\_{\alpha}(\kappa\_{2}t^{\alpha})+\frac{\kappa\_{1}}{\kappa\_{2}}(E\_{\alpha}(\kappa\_{2}t^{\alpha})-1), |  | (2.3) |

where Eα​(z)=∑i=0∞ziΓ​(α​i+1)E\_{\alpha}(z)=\sum\_{i=0}^{\infty}\frac{z^{i}}{\Gamma(\alpha i+1)} is the Mittag-Leffler function.

Note that limz→0Eα​(z)−1z=1Γ​(α+1)\lim\_{z\to 0}\frac{E\_{\alpha}(z)-1}{z}=\frac{1}{\Gamma(\alpha+1)}. Therefore, there is no singularity for κ2=0\kappa\_{2}=0, and we have 𝔼​[Xt]=x0+κ1​tαΓ​(α+1){\mathbb{E}}[X\_{t}]=x\_{0}+\frac{\kappa\_{1}t^{\alpha}}{\Gamma(\alpha+1)}.

###### Proof.

By Zhang [[25](https://arxiv.org/html/2602.18234v1#bib.bib25), Theorem 3.1], there exists a unique strong solution of the SVE such that supt∈[0,T]𝔼​[Xt2]<∞\sup\_{t\in[0,T]}{\mathbb{E}}[X\_{t}^{2}]<\infty for all T>0T>0. We can thus take the expectation and get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xt]\displaystyle{\mathbb{E}}[X\_{t}] | =x0+∫0t(t−s)α−1Γ​(α)​(κ1+κ2​𝔼​[Xs])​𝑑s\displaystyle=x\_{0}+\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}(\kappa\_{1}+\kappa\_{2}{\mathbb{E}}[X\_{s}])ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x0+κ1​tαΓ​(α+1)+κ2​∫0t(t−s)α−1Γ​(α)​𝔼​[Xs]​𝑑s,\displaystyle=x\_{0}+\kappa\_{1}\frac{t^{\alpha}}{\Gamma(\alpha+1)}+\kappa\_{2}\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{s}]ds, |  |

and therefore 𝔼​[Xt]{\mathbb{E}}[X\_{t}] is the unique solution of this fractional linear differential equation. From the Beta distribution identity ([2.1](https://arxiv.org/html/2602.18234v1#S2.E1 "In 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we have ∫0t(t−s)α−1Γ​(α)​sα​iΓ​(α​i+1)​𝑑s=tα​(i+1)Γ​(α​(i+1)+1)\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}\frac{s^{\alpha i}}{\Gamma(\alpha i+1)}ds=\frac{t^{\alpha(i+1)}}{\Gamma(\alpha(i+1)+1)} for i≥0i\geq 0, and we get

|  |  |  |
| --- | --- | --- |
|  | ∫0t(t−s)α−1Γ​(α)​∑i=0∞κ2i​(x0​sα​iΓ​(α​i+1)+κ1​sα​(i+1)Γ​(α​(i+1)+1))​d​s\displaystyle\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}\sum\_{i=0}^{\infty}\kappa\_{2}^{i}\left(x\_{0}\frac{s^{\alpha i}}{\Gamma(\alpha i+1)}+\kappa\_{1}\frac{s^{\alpha(i+1)}}{\Gamma(\alpha(i+1)+1)}\right)ds |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=1∞κ2i​(x0​tα​iΓ​(α​i+1)+κ1​tα​(i+1)Γ​(α​(i+1)+1)),\displaystyle=\sum\_{i=1}^{\infty}\kappa\_{2}^{i}\left(x\_{0}\frac{t^{\alpha i}}{\Gamma(\alpha i+1)}+\kappa\_{1}\frac{t^{\alpha(i+1)}}{\Gamma(\alpha(i+1)+1)}\right), |  |

which gives that ([2.3](https://arxiv.org/html/2602.18234v1#S2.E3 "In Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) is the desired solution.
∎

###### Proposition 2.2.

Let t∈ℝ+t\in{\mathbb{R}}\_{+} and T≥tT\geq t. Let XX be the solution of ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and 𝒴t=Xt−𝔼​[Xt]\mathcal{Y}\_{t}=X\_{t}-{\mathbb{E}}[X\_{t}] for t≥0t\geq 0.
We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒴t=σ​∑i=1∞κ2i−1​∫0t(t−s)i​α−1Γ​(i​α)​𝑑Ws.\displaystyle\mathcal{Y}\_{t}=\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\int\_{0}^{t}\frac{(t-s)^{i\alpha-1}}{\Gamma(i\alpha)}dW\_{s}. |  | (2.4) |

In particular, (Xt,t≥0)(X\_{t},t\geq 0) is a Gaussian process with covariance function cov​(Xt,XT)=𝒞X​(t,T)\textup{cov}(X\_{t},X\_{T})={\mathcal{C}^{X}}(t,T) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞X​(t,T)=σ2​∑i1,i2=1∞κ2i1+i2−2​ti1​α​Ti2​α−1Γ​(i1​α+1)​Γ​(i2​α)2​F1​(1−i2​α,1;i1​α+1,tT).\displaystyle{\mathcal{C}^{X}}(t,T)=\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{t^{i\_{1}\alpha}T^{i\_{2}\alpha-1}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\ \_{2}F\_{1}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{t}{T}). |  | (2.5) |

Besides, Xt∈𝔻1,2X\_{t}\in\mathbb{D}^{1,2} (i.e. ‖Xt‖1,22:=𝔼​[Xt2]+∫0t𝔼​[𝒟s​Xt2]​𝑑s<∞\|X\_{t}\|^{2}\_{1,2}:={\mathbb{E}}[X\_{t}^{2}]+\int\_{0}^{t}{\mathbb{E}}[\mathcal{D}\_{s}X\_{t}^{2}]ds<\infty see [[19](https://arxiv.org/html/2602.18234v1#bib.bib19), p. 27]) and the Malliavin derivative 𝒟s​Xt\mathcal{D}\_{s}X\_{t} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟s​Xt=𝟏s<t​σ​∑i=1∞κ2i−1​(t−s)i​α−1Γ​(i​α).\mathcal{D}\_{s}X\_{t}=\mathbf{1}\_{s<t}\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{(t-s)^{i\alpha-1}}{\Gamma(i\alpha)}. |  | (2.6) |

###### Remark 2.3.

From ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we easily get that for any T>0T>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | CT=sups∈[0,T]∫0s|𝒟r​Xs|​𝑑r<∞C\_{T}=\sup\_{s\in[0,T]}\int\_{0}^{s}|\mathcal{D}\_{r}X\_{s}|dr<\infty |  | (2.7) |

and there exists a constant CT′C^{\prime}\_{T} such that for any s,t∈[0,T]s,t\in[0,T] with s<ts<t,

|  |  |  |
| --- | --- | --- |
|  | |𝒟s​Xt|≤CT′​(1+(t−s)α−1).|\mathcal{D}\_{s}X\_{t}|\leq C^{\prime}\_{T}(1+(t-s)^{\alpha-1}). |  |

###### Remark 2.4.

From Propositions [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), the distribution of the Gaussian vector (Xtk)0≤k≤n(X\_{t\_{k}})\_{0\leq k\leq n} and even (Wtk,Xtk)0≤k≤n(W\_{t\_{k}},X\_{t\_{k}})\_{0\leq k\leq n} is known so that it can be sampled exactly, up to the truncation of the series ([2.5](https://arxiv.org/html/2602.18234v1#S2.E5 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). Then, we can simulate exactly the volatility process on a given time grid.
In this work, we consider instead an approximation of XX, which adds new terms in the error analysis and allows to understand the effect of discretising the volatility process. Beyond the theoretical interest, this extension is also useful in practice, for example to calculate the parameter sensitivity by Monte Carlo or for a multi-asset model. Suppose that we approximate dd​κ2​𝔼​[Φ​(LT)]≈𝔼​[Φ​(LTκ2+ε)−Φ​(LTκ2−ε)2​ε]\frac{d}{d\kappa\_{2}}{\mathbb{E}}[\Phi(L\_{T})]\approx{\mathbb{E}}[\frac{\Phi(L^{\kappa\_{2}+\varepsilon}\_{T})-\Phi(L^{\kappa\_{2}-\varepsilon}\_{T})}{2\varepsilon}] with 0<ε≪10<\varepsilon\ll 1: for variance purposes, it is crucial to sample XX with the parameters κ2−ε\kappa\_{2}-\varepsilon and κ2+ε\kappa\_{2}+\varepsilon with the same driving Brownian motion. If we use the exact simulation, this gives a nearly singular covariance matrix that may raise numerical issues, while the two approximation schemes can be sampled easily from (∫0tk(tk−s)α−1Γ​(α)​𝑑Ws)k≤n(\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s})\_{k\leq n}.

###### Proof.

We have XT=x0+∫0T(T−s)α−1Γ​(α)​(κ1+κ2​Xs)​𝑑s+σ​∫0T(T−s)α−1Γ​(α)​𝑑WsX\_{T}=x\_{0}+\int\_{0}^{T}\frac{(T-s)^{\alpha-1}}{\Gamma(\alpha)}(\kappa\_{1}+\kappa\_{2}X\_{s})ds+\sigma\int\_{0}^{T}\frac{(T-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s} and thus 𝔼​[XT]=x0+∫0T(T−s)α−1Γ​(α)​(κ1+κ2​𝔼​[Xs])​𝑑s{\mathbb{E}}[X\_{T}]=x\_{0}+\int\_{0}^{T}\frac{(T-s)^{\alpha-1}}{\Gamma(\alpha)}(\kappa\_{1}+\kappa\_{2}{\mathbb{E}}[X\_{s}])ds. This gives

|  |  |  |
| --- | --- | --- |
|  | 𝒴T=∫0T(T−s)α−1Γ​(α)​κ2​𝒴s​𝑑s+σ​∫0T(T−s)α−1Γ​(α)​𝑑Ws,T≥0.\mathcal{Y}\_{T}=\int\_{0}^{T}\frac{(T-s)^{\alpha-1}}{\Gamma(\alpha)}\kappa\_{2}\mathcal{Y}\_{s}ds+\sigma\int\_{0}^{T}\frac{(T-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s},T\geq 0. |  |

We then obtain

|  |  |  |
| --- | --- | --- |
|  | 𝒴T=∫0T(T−t)α−1Γ​(α)​κ2​(∫0t(t−s)α−1Γ​(α)​κ2​𝒴s​𝑑s+σ​∫0t(t−s)α−1Γ​(α)​𝑑Ws)​𝑑t+σ​∫0T(T−t)α−1Γ​(α)​𝑑Wt.\mathcal{Y}\_{T}=\int\_{0}^{T}\frac{(T-t)^{\alpha-1}}{\Gamma(\alpha)}\kappa\_{2}\left(\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}\kappa\_{2}\mathcal{Y}\_{s}ds+\sigma\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s}\right)dt+\sigma\int\_{0}^{T}\frac{(T-t)^{\alpha-1}}{\Gamma(\alpha)}dW\_{t}. |  |

By using Fubini’s theorem and then ([2.1](https://arxiv.org/html/2602.18234v1#S2.E1 "In 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get

|  |  |  |
| --- | --- | --- |
|  | ∫0T(T−t)α−1Γ​(α)​∫0t(t−s)α−1Γ​(α)​𝒴s​𝑑s​𝑑t=∫0T𝒴s​(T−s)2​α−1Γ​(2​α)​𝑑s,\int\_{0}^{T}\frac{(T-t)^{\alpha-1}}{\Gamma(\alpha)}\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}\mathcal{Y}\_{s}dsdt=\int\_{0}^{T}\mathcal{Y}\_{s}\frac{(T-s)^{2\alpha-1}}{\Gamma(2\alpha)}ds, |  |

Similarly, the stochastic Fubini theorem (see e.g. [[22](https://arxiv.org/html/2602.18234v1#bib.bib22), Theorem IV.65]) gives

|  |  |  |
| --- | --- | --- |
|  | ∫0T(T−t)α−1Γ​(α)​(∫0t(t−s)α−1Γ​(α)​𝑑Ws)​𝑑t=∫0T(T−s)2​α−1Γ​(2​α)​𝑑Ws,\int\_{0}^{T}\frac{(T-t)^{\alpha-1}}{\Gamma(\alpha)}\left(\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s}\right)dt=\int\_{0}^{T}\frac{(T-s)^{2\alpha-1}}{\Gamma(2\alpha)}dW\_{s}, |  |

and we get

|  |  |  |
| --- | --- | --- |
|  | 𝒴T=∫0T(T−s)2​α−1Γ​(2​α)​κ22​𝒴s​𝑑s+σ​∑i=12κ2i−1​∫0T(T−s)i​α−1Γ​(i​α)​𝑑Ws.\mathcal{Y}\_{T}=\int\_{0}^{T}\frac{(T-s)^{2\alpha-1}}{\Gamma(2\alpha)}\kappa\_{2}^{2}\mathcal{Y}\_{s}ds+\sigma\sum\_{i=1}^{2}\kappa\_{2}^{i-1}\int\_{0}^{T}\frac{(T-s)^{i\alpha-1}}{\Gamma(i\alpha)}dW\_{s}. |  |

By induction, we get using again the same Fubini argument

|  |  |  |
| --- | --- | --- |
|  | 𝒴T=∫0T(T−s)n​α−1Γ​(n​α)​κ2n​𝒴s​𝑑s+σ​∑i=1nκ2i−1​∫0T(T−s)i​α−1Γ​(i​α)​𝑑Ws\mathcal{Y}\_{T}=\int\_{0}^{T}\frac{(T-s)^{n\alpha-1}}{\Gamma(n\alpha)}\kappa\_{2}^{n}\mathcal{Y}\_{s}ds+\sigma\sum\_{i=1}^{n}\kappa\_{2}^{i-1}\int\_{0}^{T}\frac{(T-s)^{i\alpha-1}}{\Gamma(i\alpha)}dW\_{s} |  |

for n≥1n\geq 1. The first term and the rest ∑i=n+1∞κ2i−1​∫0t(T−s)i​α−1Γ​(i​α)​𝑑Ws\sum\_{i=n+1}^{\infty}\kappa\_{2}^{i-1}\int\_{0}^{t}\frac{(T-s)^{i\alpha-1}}{\Gamma(i\alpha)}dW\_{s} vanish in L2​(Ω)L^{2}(\Omega) as n→∞n\to\infty. We have indeed

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0T(T−s)n​α−1Γ​(n​α)​κ2n​𝒴s​𝑑s)2]\displaystyle{\mathbb{E}}\left[\left(\int\_{0}^{T}\frac{(T-s)^{n\alpha-1}}{\Gamma(n\alpha)}\kappa\_{2}^{n}\mathcal{Y}\_{s}ds\right)^{2}\right] | ≤T​supt∈[0,T]𝔼​[|Xt|2]​∫0T(T−s)2​n​α−2Γ​(n​α)2​κ22​n​𝑑s\displaystyle\leq T\sup\_{t\in[0,T]}{\mathbb{E}}[|X\_{t}|^{2}]\int\_{0}^{T}\frac{(T-s)^{2n\alpha-2}}{\Gamma(n\alpha)^{2}}\kappa\_{2}^{2n}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T​supt∈[0,T]𝔼​[|Xt|2]​T2​n​α−1(2​n​α−1)​Γ​(n​α)2​κ22​n→n→∞0,\displaystyle=T\sup\_{t\in[0,T]}{\mathbb{E}}[|X\_{t}|^{2}]\frac{T^{2n\alpha-1}}{(2n\alpha-1)\Gamma(n\alpha)^{2}}\kappa\_{2}^{2n}\to\_{n\to\infty}0, |  |

by Stirling’s formula. Similarly, we have by the Itô isometry

|  |  |  |
| --- | --- | --- |
|  | 𝔼1/2​[(∫0T(T−s)i​α−1Γ​(i​α)​κ2i​𝑑Ws)2]=|κ2|i​Ti​α−1/2(2​i​α−1)1/2​Γ​(i​α),{\mathbb{E}}^{1/2}\left[\left(\int\_{0}^{T}\frac{(T-s)^{i\alpha-1}}{\Gamma(i\alpha)}\kappa\_{2}^{i}dW\_{s}\right)^{2}\right]=\frac{|\kappa\_{2}|^{i}T^{i\alpha-1/2}}{(2i\alpha-1)^{1/2}\Gamma(i\alpha)}, |  |

and we obtain ∑i=n+1∞𝔼1/2​[(κ2i−1​∫0t(T−s)i​α−1Γ​(i​α)​𝑑Ws)2]→n→∞0\sum\_{i=n+1}^{\infty}{\mathbb{E}}^{1/2}\left[\left(\kappa\_{2}^{i-1}\int\_{0}^{t}\frac{(T-s)^{i\alpha-1}}{\Gamma(i\alpha)}dW\_{s}\right)^{2}\right]\to\_{n\to\infty}0. By uniqueness of the limit in L2​(Ω)L^{2}(\Omega), we get

|  |  |  |
| --- | --- | --- |
|  | 𝒴T=σ​∑i=1∞κ2i−1​∫0T(T−s)i​α−1Γ​(i​α)​𝑑Ws​ a.s., for ​T>0.\mathcal{Y}\_{T}=\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\int\_{0}^{T}\frac{(T-s)^{i\alpha-1}}{\Gamma(i\alpha)}dW\_{s}\text{ a.s., for }T>0. |  |

We now calculate the covariance by Itô isometry for t∈[0,T]t\in[0,T]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cov​(𝒴t,𝒴T)\displaystyle\textup{cov}(\mathcal{Y}\_{t},\mathcal{Y}\_{T}) | =σ2​∫0t∑i1,i2=1∞κ2i2+i2−2​(t−s)i1​α−1Γ​(i1​α)​(T−s)i2​α−1Γ​(i2​α)​d​s\displaystyle=\sigma^{2}\int\_{0}^{t}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{2}+i\_{2}-2}\frac{(t-s)^{i\_{1}\alpha-1}}{\Gamma(i\_{1}\alpha)}\frac{(T-s)^{i\_{2}\alpha-1}}{\Gamma(i\_{2}\alpha)}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =σ2​∑i1,i2=1∞κ2i2+i2−2Γ​(i1​α)​Γ​(i2​α)​ti1​α​Ti2​α−1​∫01(1−u)i1​α−1​(1−u​tT)i2​α−1​𝑑u,\displaystyle=\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\frac{\kappa\_{2}^{i\_{2}+i\_{2}-2}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}t^{i\_{1}\alpha}T^{i\_{2}\alpha-1}\int\_{0}^{1}(1-u)^{i\_{1}\alpha-1}\left(1-u\frac{t}{T}\right)^{i\_{2}\alpha-1}du, |  |

with the change of variable s=u​ts=ut. This gives ([2.5](https://arxiv.org/html/2602.18234v1#S2.E5 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) by ([2.2](https://arxiv.org/html/2602.18234v1#S2.E2 "In 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). Last, we apply the chain rule to ([2.4](https://arxiv.org/html/2602.18234v1#S2.E4 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) (see [[19](https://arxiv.org/html/2602.18234v1#bib.bib19), Proposition 1.3.8]) and we get ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). We then observe that ∫0t(𝒟s​Xt)2​𝑑s=σ2​∑i1,i2=1∞κ2i2+i2−2Γ​(i1​α)​Γ​(i2​α)​t(i1+i2)​α−1(i1+i2)​α−1\int\_{0}^{t}(\mathcal{D}\_{s}X\_{t})^{2}ds=\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\frac{\kappa\_{2}^{i\_{2}+i\_{2}-2}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}\frac{t^{(i\_{1}+i\_{2})\alpha-1}}{(i\_{1}+i\_{2})\alpha-1} by the same calculation as above with T=tT=t, and therefore ‖Xt‖1,2<∞\|X\_{t}\|\_{1,2}<\infty.
∎

###### Corollary 2.5.

If κ2<0\kappa\_{2}<0, then XtX\_{t} converges in distribution when t→∞t\to\infty to 𝒩​(−κ1κ2,Σ∞2)\mathcal{N}(-\frac{\kappa\_{1}}{\kappa\_{2}},\Sigma\_{\infty}^{2}), with

|  |  |  |
| --- | --- | --- |
|  | Σ∞2=σ2​∫0∞s2​α−2​Eα,α2​(κ2​sα)​𝑑s,\Sigma\_{\infty}^{2}=\sigma^{2}\int\_{0}^{\infty}s^{2\alpha-2}E\_{\alpha,\alpha}^{2}(\kappa\_{2}s^{\alpha})ds, |  |

where Eα,β​(z)=∑i=0∞ziΓ​(α​i+β)E\_{\alpha,\beta}(z)=\sum\_{i=0}^{\infty}\frac{z^{i}}{\Gamma(\alpha i+\beta)} for z∈ℝz\in{\mathbb{R}} is the generalized Mittag-Leffler function.

###### Proof.

Since XtX\_{t} follows a normal distribution, it is sufficient to get the convergence of the mean and the variance. By [[21](https://arxiv.org/html/2602.18234v1#bib.bib21), Theorem 1.6], Eα​(z)=Eα,1​(z)→z→−∞0E\_{\alpha}(z)=E\_{\alpha,1}(z)\to\_{z\to-\infty}0, and we get 𝔼​[Xt]→t→+∞−κ1κ2{\mathbb{E}}[X\_{t}]\to\_{t\to+\infty}-\frac{\kappa\_{1}}{\kappa\_{2}} from ([2.3](https://arxiv.org/html/2602.18234v1#S2.E3 "In Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). From ([2.4](https://arxiv.org/html/2602.18234v1#S2.E4 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get

|  |  |  |
| --- | --- | --- |
|  | Var​(Xt)=σ2​∫0t∑i1,i2=1∞κ2i1+i2−2​s(i1+i2)​α−2Γ​(i1​α)​Γ​(i2​α)​d​s=σ2​∫0ts2​α−2​Eα,α2​(κ2​sα)​𝑑s.{\rm Var}(X\_{t})=\sigma^{2}\int\_{0}^{t}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{s^{(i\_{1}+i\_{2})\alpha-2}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}ds=\sigma^{2}\int\_{0}^{t}s^{2\alpha-2}E\_{\alpha,\alpha}^{2}(\kappa\_{2}s^{\alpha})ds. |  |

Note that Eα,α​(0)=1Γ​(α)E\_{\alpha,\alpha}(0)=\frac{1}{\Gamma(\alpha)}, and the integral is well defined in 0+0+ since 2​α−1>02\alpha-1>0. Using again [[21](https://arxiv.org/html/2602.18234v1#bib.bib21), Theorem 1.6], we get |Eα,α​(z)|≤C1−z|E\_{\alpha,\alpha}(z)|\leq\frac{C}{1-z} for z<0z<0, so that s2​α−2​Eα,α2​(κ2​sα)=s→+∞O​(s−2)s^{2\alpha-2}E\_{\alpha,\alpha}^{2}(\kappa\_{2}s^{\alpha})=\_{s\to+\infty}O(s^{-2}) is integrable. This gives the desired result.
∎

We end this section by a crucial estimate on the process XX. The proof is quite technical and is postponed in the appendix section.

###### Theorem 2.6.

Let T>0T>0, n∈ℕ∗n\in{\mathbb{N}}^{\*} and tk=k​Tnt\_{k}=k\frac{T}{n} for k∈ℕk\in{\mathbb{N}}. Let η​(s)=tk\eta(s)=t\_{k} for tk≤s<tk+1t\_{k}\leq s<t\_{k+1}. There exists a constant CT∈ℝ+C\_{T}\in{\mathbb{R}}\_{+} such that for any t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[Xt​(Xs−Xη​(s))]​𝑑s|≤CT​((1+tα−1)​𝐯n​(α)+t2​α−2n).\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{t}(X\_{s}-X\_{\eta(s)})]ds\right|\leq C\_{T}\left(\left(1+t^{\alpha-1}\right){\bf v}\_{n}(\alpha)+\frac{t^{2\alpha-2}}{n}\right). |  |

### 2.2. Weak rate of convergence

The goal of this subsection is to analyse the weak rate of convergence of the kernel integrated Euler scheme ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) for Xˇn{\check{X}^{n}} only. We start by a remark that motivates the choice of this scheme rather than the discretised kernel Euler scheme:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtn\displaystyle X^{n}\_{t} | =x0+∫0t(t−η​(s))α−1Γ​(α)​(κ1+κ2​Xη​(s)n)​𝑑s+σ​∫0t(t−η​(s))α−1Γ​(α)​𝑑Ws,t∈[0,T].\displaystyle=x\_{0}+\int\_{0}^{t}\frac{(t-\eta(s))^{\alpha-1}}{\Gamma(\alpha)}(\kappa\_{1}+\kappa\_{2}X^{n}\_{\eta(s)})ds+\sigma\int\_{0}^{t}\frac{(t-\eta(s))^{\alpha-1}}{\Gamma(\alpha)}dW\_{s},\;t\in[0,T]. |  |

We recall that η​(s)=k​Tn\eta(s)=\frac{kT}{n} for k​Tn≤s<(k+1)​Tn\frac{kT}{n}\leq s<\frac{(k+1)T}{n}. Let us consider the simplest case: κ1=κ2=0\kappa\_{1}=\kappa\_{2}=0 and σ=1\sigma=1, and consider Xtn=∫0t(t−η​(s))α−1Γ​(α)​𝑑WsX^{n}\_{t}=\int\_{0}^{t}\frac{(t-\eta(s))^{\alpha-1}}{\Gamma(\alpha)}dW\_{s}, the approximation of Xt=∫0t(t−s)α−1Γ​(α)​𝑑Ws=XˇntX\_{t}=\int\_{0}^{t}\frac{(t-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s}={\check{X}^{n}}\_{t}. Both are Gaussian processes, and we have

|  |  |  |
| --- | --- | --- |
|  | XT∼𝒩​(0,T2​α−1(2​α−1)​Γ​(α)2),XTn∼𝒩​(0,∫0T(T−η​(s))2​α−2Γ​(α)2​𝑑s).X\_{T}\sim\mathcal{N}\left(0,\frac{T^{2\alpha-1}}{(2\alpha-1)\Gamma(\alpha)^{2}}\right),\ X^{n}\_{T}\sim\mathcal{N}\left(0,\int\_{0}^{T}\frac{(T-\eta(s))^{2\alpha-2}}{\Gamma(\alpha)^{2}}ds\right). |  |

Thus, we have the following equation between characteristic functions ΦXTn​(u)=𝔼​[ei​u​XTn]\Phi\_{X^{n}\_{T}}(u)={\mathbb{E}}[e^{iuX^{n}\_{T}}] and ΦXT​(u)=𝔼​[ei​u​XT]\Phi\_{X\_{T}}(u)={\mathbb{E}}[e^{iuX\_{T}}]:

|  |  |  |
| --- | --- | --- |
|  | u∈ℝ,ΦXTn​(u)=ΦXT​(u)​exp⁡(u22​(T2​α−1(2​α−1)​Γ​(α)2−∫0t(T−η​(s))2​α−2Γ​(α)2​𝑑s)).u\in{\mathbb{R}},\ \Phi\_{X^{n}\_{T}}(u)=\Phi\_{X\_{T}}(u)\exp\left(\frac{u^{2}}{2}\left(\frac{T^{2\alpha-1}}{(2\alpha-1)\Gamma(\alpha)^{2}}-\int\_{0}^{t}\frac{(T-\eta(s))^{2\alpha-2}}{\Gamma(\alpha)^{2}}ds\right)\right). |  |

By McGown and Parks [[18](https://arxiv.org/html/2602.18234v1#bib.bib18)], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | T2​α−1(2​α−1)​Γ​(α)2−∫0T(t−η​(s))2​α−2Γ​(α)2​𝑑s\displaystyle\frac{T^{2\alpha-1}}{(2\alpha-1)\Gamma(\alpha)^{2}}-\int\_{0}^{T}\frac{(t-\eta(s))^{2\alpha-2}}{\Gamma(\alpha)^{2}}ds | =1Γ​(α)2​(T22​α−1−Tn​∑i=1n∑i=1n(i​Tn)2​α−2)\displaystyle=\frac{1}{\Gamma(\alpha)^{2}}\left(\frac{T^{2}}{2\alpha-1}-\frac{T}{n}\sum\_{i=1}^{n}\sum\_{i=1}^{n}\left(\frac{iT}{n}\right)^{2\alpha-2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∼n→∞1Γ​(α)2​ζ​(2​(1−α))​T2​α−1n2​α−1,\displaystyle\sim\_{n\to\infty}\frac{1}{\Gamma(\alpha)^{2}}\zeta(2(1-\alpha))\frac{T^{2\alpha-1}}{n^{2\alpha-1}}, |  |

which gives a weak rate of convergence proportional to n−(2​α−1)n^{-(2\alpha-1)} for the family of test functions x↦ei​u​xx\mapsto e^{iux}. We cannot therefore hope to reach the rate of O​(𝐯n​(α))O({\bf v}\_{n}(\alpha)) defined by ([1.3](https://arxiv.org/html/2602.18234v1#S1.E3 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

In what follows, we introduce the functional spaces that will be used through the paper (in particular as test functions), for ℓ∈ℕ\ell\in{\mathbb{N}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞expℓ​(ℝ,ℝ):={g∈𝒞ℓ​(ℝ,ℝ):∀k∈{0,…,ℓ},∃C∈ℝ+​∀x∈ℝ,|g(k)​(x)|≤C​eC​|x|},\displaystyle\mathcal{C}\_{\exp}^{\ell}({\mathbb{R}},{\mathbb{R}}):=\{g\in\mathcal{C}^{\ell}({\mathbb{R}},{\mathbb{R}}):\forall k\in\{0,\dots,\ell\},\exists C\in{\mathbb{R}}\_{+}\forall x\in{\mathbb{R}},\ |g^{(k)}(x)|\leq Ce^{C|x|}\}, |  | (2.8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞exp∞​(ℝ,ℝ):={g∈𝒞∞​(ℝ,ℝ):∀k∈ℕ,∃C∈ℝ+​∀x∈ℝ,|g(k)​(x)|≤C​eC​|x|}.\displaystyle\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}):=\{g\in\mathcal{C}^{\infty}({\mathbb{R}},{\mathbb{R}}):\forall k\in{\mathbb{N}},\exists C\in{\mathbb{R}}\_{+}\forall x\in{\mathbb{R}},\ |g^{(k)}(x)|\leq Ce^{C|x|}\}. |  | (2.9) |

It is easy to check that 𝒞exp∞​(ℝ,ℝ)\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}) is a vector space such that for g∈𝒞exp∞​(ℝ,ℝ)g\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}), we have g′∈𝒞exp∞​(ℝ,ℝ)g^{\prime}\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}). Similarly, for g1,g2∈𝒞exp∞​(ℝ,ℝ)g\_{1},g\_{2}\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}), we have g1​g2∈𝒞exp∞​(ℝ,ℝ)g\_{1}g\_{2}\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}) by Leibniz rule.

The main result of this section is the following theorem.

###### Theorem 2.7.

There exists a constant CTC\_{T} that depends on TT and α∈(1/2,1]\alpha\in(1/2,1] such that for 0<k1,k2≤n0<k\_{1},k\_{2}\leq n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[Xtk1]−𝔼​[Xˇntk1]|≤CTn,|{\mathbb{E}}[X\_{t\_{k\_{1}}}]-{\mathbb{E}}[{\check{X}^{n}}\_{t\_{k\_{1}}}]|\leq\frac{C\_{T}}{n}, |  | (2.10) |

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[Xtk1​Xtk2]−𝔼​[Xˇtk1n​Xˇtk2n]|≤CT​((1+tk1α−1+tk2α−1)​𝐯n​(α)+tk12​α−2+tk22​α−2n)|{\mathbb{E}}[X\_{t\_{k\_{1}}}X\_{t\_{k\_{2}}}]-{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}\check{X}^{n}\_{t\_{k\_{2}}}]|\leq C\_{T}\left((1+t\_{k\_{1}}^{\alpha-1}+t\_{k\_{2}}^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{t\_{k\_{1}}^{2\alpha-2}+t\_{k\_{2}}^{2\alpha-2}}{n}\right) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |C​o​v​(Xtk1,Xtk2)−C​o​v​(Xˇtk1n,Xˇtk2n)|≤CT​((1+tk1α−1+tk2α−1)​𝐯n​(α)+tk12​α−2+tk22​α−2n).|Cov(X\_{t\_{k\_{1}}},X\_{t\_{k\_{2}}})-Cov(\check{X}^{n}\_{t\_{k\_{1}}},\check{X}^{n}\_{t\_{k\_{2}}})|\leq C\_{T}\left((1+t\_{k\_{1}}^{\alpha-1}+t\_{k\_{2}}^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{t\_{k\_{1}}^{2\alpha-2}+t\_{k\_{2}}^{2\alpha-2}}{n}\right). |  | (2.11) |

Besides, for any Ψ∈𝒞exp2​(ℝ,ℝ)\Psi\in\mathcal{C}\_{\exp}^{2}({\mathbb{R}},{\mathbb{R}}), there exists a constant C∈ℝ+C\in{\mathbb{R}}\_{+} such that

|  |  |  |
| --- | --- | --- |
|  | ∀n≥1,1≤k≤n,|𝔼​[Ψ​(Xˇntk)]−𝔼​[Ψ​(Xtk)]|≤CT​((1+tkα−1)​𝐯n​(α)+tk2​α−2n).\forall n\geq 1,1\leq k\leq n,\ \ |{\mathbb{E}}[\Psi({\check{X}^{n}}\_{t\_{k}})]-{\mathbb{E}}[\Psi(X\_{t\_{k}})]|\leq C\_{T}\left((1+t\_{k}^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{t\_{k}^{2\alpha-2}}{n}\right). |  |

In particular, for k=nk=n we get the weak error |𝔼​[Ψ​(XˇnT)]−𝔼​[Ψ​(XT)]|=O​(𝐯n​(α))|{\mathbb{E}}[\Psi({\check{X}^{n}}\_{T})]-{\mathbb{E}}[\Psi(X\_{T})]|=O({\bf v}\_{n}(\alpha)).

###### Remark 2.8.

Note that if k1=0k\_{1}=0, we have by ([2.10](https://arxiv.org/html/2602.18234v1#S2.E10 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[Xtk1​Xtk2]−𝔼​[Xˇtk1n​Xˇtk2n]|=|X0|​|𝔼​[Xtk2−Xˇtk2n]|≤CTn,|{\mathbb{E}}[X\_{t\_{k\_{1}}}X\_{t\_{k\_{2}}}]-{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}\check{X}^{n}\_{t\_{k\_{2}}}]|=|X\_{0}||{\mathbb{E}}[X\_{t\_{k\_{2}}}-\check{X}^{n}\_{t\_{k\_{2}}}]|\leq\frac{C\_{T}}{n}, |  |

and also obviously C​o​v​(Xtk1,Xtk2)=C​o​v​(Xˇtk1n,Xˇtk2n)=0Cov(X\_{t\_{k\_{1}}},X\_{t\_{k\_{2}}})=Cov(\check{X}^{n}\_{t\_{k\_{1}}},\check{X}^{n}\_{t\_{k\_{2}}})=0.

###### Remark 2.9.

From Proposition [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and ([2.10](https://arxiv.org/html/2602.18234v1#S2.E10 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get that max0≤k≤n⁡|𝔼​[Xˇntk]|≤CT\max\_{0\leq k\leq n}|{\mathbb{E}}[{\check{X}^{n}}\_{t\_{k}}]|\leq C\_{T} for a constant that does not depend on nn.
Besides, using ([2.5](https://arxiv.org/html/2602.18234v1#S2.E5 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and ([2.11](https://arxiv.org/html/2602.18234v1#S2.E11 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we also obtain max0≤k1,k2≤n⁡|C​o​v​(Xˇtk1n,Xˇtk2n)|≤CT\max\_{0\leq k\_{1},k\_{2}\leq n}|Cov(\check{X}^{n}\_{t\_{k\_{1}}},\check{X}^{n}\_{t\_{k\_{2}}})|\leq C\_{T} for a constant that does not depend on nn since t1α−1​𝐯n​(α)t\_{1}^{\alpha-1}{\bf v}\_{n}(\alpha) and t12​α−2n\frac{t\_{1}^{2\alpha-2}}{n} go to 0 as n→∞n\to\infty for any α∈(1/2,1]\alpha\in(1/2,1].

Before proving the theorem, we introduce some notation and an important preliminary result of Gronwall type.
For this aim, let us note Δtk=Xtk−Xˇtkn\Delta\_{t\_{k}}=X\_{t\_{k}}-\check{X}^{n}\_{t\_{k}} for k∈{0,…,n}k\in\{0,\dots,n\}, that satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δtk\displaystyle\Delta\_{t\_{k}} | =∫0tk(tk−s)α−1Γ​(α)​κ2​(Xs−Xη​(s)+Xη​(s)−Xˇnη​(s))​𝑑s\displaystyle=\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}\kappa\_{2}(X\_{s}-X\_{\eta(s)}+X\_{\eta(s)}-{\check{X}^{n}}\_{\eta(s)})ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0tk(tk−s)α−1Γ​(α)​κ2​(Xs−Xη​(s))​𝑑s+∑i=2kΔti−1​∫ti−1ti(tk−s)α−1Γ​(α)​𝑑s.\displaystyle=\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}\kappa\_{2}(X\_{s}-X\_{\eta(s)})ds+\sum\_{i=2}^{k}\Delta\_{t\_{i-1}}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}ds. |  | (2.12) |

###### Lemma 2.10.

Let 𝒱\mathcal{V} be a square integrable random variable. Then, there exists C∈ℝ+C\in{\mathbb{R}}\_{+} that does not depend on 𝒱\mathcal{V} and nn, such that

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|𝔼​[𝒱​Δtk]|≤C​max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[𝒱​(Xs−Xη​(s))]​𝑑s|\max\_{1\leq k\leq n}\left|{\mathbb{E}}[\mathcal{V}\Delta\_{t\_{k}}]\right|\leq C\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[\mathcal{V}(X\_{s}-X\_{\eta(s)})]ds\right| |  |

###### Proof.

We have from ([2.12](https://arxiv.org/html/2602.18234v1#S2.E12 "In 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), for k∈{1,…,n}k\in\{1,\dots,n\}:

|  |  |  |
| --- | --- | --- |
|  | 𝒱​Δtk=𝒱​κ2​∫0tk(tk−s)α−1Γ​(α)​(Xs−Xη​(s))​𝑑s+κ2​∑i=2k𝒱​Δti−1​∫ti−1ti(tk−s)α−1Γ​(α)​𝑑s.\mathcal{V}\Delta\_{t\_{k}}=\mathcal{V}\kappa\_{2}\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}(X\_{s}-X\_{\eta(s)})ds+\kappa\_{2}\sum\_{i=2}^{k}\mathcal{V}\Delta\_{t\_{i-1}}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}ds. |  |

We then take the expectation and get by the triangular inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[𝒱​Δtk]|≤\displaystyle|{\mathbb{E}}[\mathcal{V}\Delta\_{t\_{k}}]|\leq | |κ2|​|∫0tk(tk−s)α−1Γ​(α)​𝔼​[𝒱​(Xs−Xη​(s))]​𝑑s|\displaystyle|\kappa\_{2}|\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[\mathcal{V}(X\_{s}-X\_{\eta(s)})]ds\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|κ2|​∑i=2k|𝔼​[𝒱​Δti−1]|​(k−i+1)α−(k−i)αΓ​(α+1)​(Tn)α.\displaystyle+|\kappa\_{2}|\sum\_{i=2}^{k}|{\mathbb{E}}[\mathcal{V}\Delta\_{t\_{i-1}}]|\frac{(k-i+1)^{\alpha}-(k-i)^{\alpha}}{\Gamma(\alpha+1)}\left(\frac{T}{n}\right)^{\alpha}. |  |

By ([A.1](https://arxiv.org/html/2602.18234v1#A1.E1 "In Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we obtain

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[𝒱​Δtk]|≤𝐌+|κ2|​Cα​(Tn)α​∑j=1k−1|𝔼​[𝒱​Δtj]|​(k−j)α−1,|{\mathbb{E}}[\mathcal{V}\Delta\_{t\_{k}}]|\leq\mathbf{M}+|\kappa\_{2}|C\_{\alpha}\left(\frac{T}{n}\right)^{\alpha}\sum\_{j=1}^{k-1}|{\mathbb{E}}[\mathcal{V}\Delta\_{t\_{j}}]|(k-j)^{\alpha-1}, |  |

with 𝐌=|κ2|​max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[𝒱​(Xs−Xη​(s))]​𝑑s|\mathbf{M}=|\kappa\_{2}|\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[\mathcal{V}(X\_{s}-X\_{\eta(s)})]ds\right|. We conclude by the Gronwall type estimate [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.4].
∎

###### Proof of Theorem [2.7](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

We start by proving the first bound. We apply Lemma [2.10](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem10 "Lemma 2.10. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") with 𝒱=1\mathcal{V}=1 and get

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|𝔼​[Xtk]−𝔼​[Xˇntk]|≤C​max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​(𝔼​[Xs]−𝔼​[Xη​(s)])​𝑑s|.\max\_{1\leq k\leq n}|{\mathbb{E}}[X\_{t\_{k}}]-{\mathbb{E}}[{\check{X}^{n}}\_{t\_{k}}]|\leq C\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}({\mathbb{E}}[X\_{s}]-{\mathbb{E}}[X\_{\eta(s)}])ds\right|. |  |

By Proposition [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), 𝔼​[Xt]=x0​tα+z​(t){\mathbb{E}}[X\_{t}]=x\_{0}t^{\alpha}+z(t) where zz is a 𝒞1\mathcal{C}^{1} function on ℝ+{\mathbb{R}}\_{+}. We apply respectively [[8](https://arxiv.org/html/2602.18234v1#bib.bib8), Theorem 2.4 (b) and (a)] to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫0tk(tk−s)α−1Γ​(α)​(𝔼​[Xs]−𝔼​[Xη​(s)])​𝑑s|≤Tn​(C​T2​α−1+maxt∈[0,T]⁡|z′​(t)|α​Tα),\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}({\mathbb{E}}[X\_{s}]-{\mathbb{E}}[X\_{\eta(s)}])ds\right|\leq\frac{T}{n}\left(CT^{2\alpha-1}+\frac{\max\_{t\in[0,T]}|z^{\prime}(t)|}{\alpha}T^{\alpha}\right), |  | (2.13) |

which gives the claim on the expectation.

We now focus on covariance terms and have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Xtk1​Xtk2]−𝔼​[Xˇtk1n​Xˇtk2n]\displaystyle{\mathbb{E}}[X\_{t\_{k\_{1}}}X\_{t\_{k\_{2}}}]-{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}\check{X}^{n}\_{t\_{k\_{2}}}] | =𝔼​[Xtk2​(Xtk1−Xˇtk1n)]+𝔼​[Xˇtk1n​(Xtk2−Xˇtk2n)]\displaystyle={\mathbb{E}}[X\_{t\_{k\_{2}}}(X\_{t\_{k\_{1}}}-\check{X}^{n}\_{t\_{k\_{1}}})]+{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}(X\_{t\_{k\_{2}}}-\check{X}^{n}\_{t\_{k\_{2}}})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[Xtk2​Δtk1]+𝔼​[Xˇtk1n​Δtk2],\displaystyle={\mathbb{E}}[X\_{t\_{k\_{2}}}\Delta\_{t\_{k\_{1}}}]+{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}\Delta\_{t\_{k\_{2}}}], |  |

with Δtk\Delta\_{t\_{k}} given by ([2.12](https://arxiv.org/html/2602.18234v1#S2.E12 "In 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).
We apply Lemma [2.10](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem10 "Lemma 2.10. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") twice: first with 𝒱=Xtk2\mathcal{V}=X\_{t\_{k\_{2}}} and then with 𝒱=Xˇtk1n\mathcal{V}=\check{X}^{n}\_{t\_{k\_{1}}}.

We start with 𝒱=Xtk2\mathcal{V}=X\_{t\_{k\_{2}}} and get

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|𝔼​[Xtk2​Δtk]|≤C​max1≤k≤n⁡|∫0tk(tk−u)α−1Γ​(α)​𝔼​[Xtk2​(Xu−Xη​(u))]​𝑑u|.\max\_{1\leq k\leq n}|{\mathbb{E}}[X\_{t\_{k\_{2}}}\Delta\_{t\_{k}}]|\leq C\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{t\_{k\_{2}}}(X\_{u}-X\_{\eta(u)})]du\right|. |  |

By Theorem [2.6](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we obtain

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|𝔼​[Xtk2​Δtk]|≤CT​((1+tk2α−1)​𝐯n​(α)+tk22​α−2n).\max\_{1\leq k\leq n}|{\mathbb{E}}[X\_{t\_{k\_{2}}}\Delta\_{t\_{k}}]|\leq C\_{T}\left((1+t\_{k\_{2}}^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{t\_{k\_{2}}^{2\alpha-2}}{n}\right). |  |

We now apply Lemma [2.10](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem10 "Lemma 2.10. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") with 𝒱=Xˇtk1n\mathcal{V}=\check{X}^{n}\_{t\_{k\_{1}}}:

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|𝔼​[Xˇtk1n​(Xtk−Xˇtkn)]|≤C​max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[Xˇtk1n​(Xs−Xη​(s))]​𝑑s|.\max\_{1\leq k\leq n}|{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}(X\_{t\_{k}}-\check{X}^{n}\_{t\_{k}})]|\leq C\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}(X\_{s}-X\_{\eta(s)})]ds\right|. |  |

Then, we write

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xˇtk1n​(Xs−Xη​(s))]=𝔼​[(Xˇtk1n−Xtk1)​Xs]+𝔼​[Xtk1​(Xs−Xη​(s))]+𝔼​[Xη​(s)​(Xtk1−Xˇtk1n)],\displaystyle{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}(X\_{s}-X\_{\eta(s)})]={\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{s}]+{\mathbb{E}}[X\_{t\_{k\_{1}}}(X\_{s}-X\_{\eta(s)})]+{\mathbb{E}}[X\_{\eta(s)}(X\_{t\_{k\_{1}}}-\check{X}^{n}\_{t\_{k\_{1}}})], |  |

and use the triangle inequality. We first notice that the second term

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[Xtk1​(Xs−Xη​(s))]​𝑑s|\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{t\_{k\_{1}}}(X\_{s}-X\_{\eta(s)})]ds\right| |  |

is again
upper bounded by CT​((1+tk1α−1)​𝐯n​(α)+tk12​α−2n)C\_{T}\left((1+t\_{k\_{1}}^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{t\_{k\_{1}}^{2\alpha-2}}{n}\right) using Theorem [2.6](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). For the two other terms, we have to upper bound

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xs]​𝑑s|​ and ​max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xη​(s)]​𝑑s|\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{s}]ds\right|\text{ and }\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{\eta(s)}]ds\right| |  |

To do so, we use Lemma [2.10](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem10 "Lemma 2.10. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") with 𝒱=Xs\mathcal{V}=X\_{s} and then
Theorem [2.6](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[(Xˇtk1n−Xtk1)​Xs]|\displaystyle|{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{s}]| | ≤C​max1≤k≤n⁡|∫0tk(tk−u)α−1Γ​(α)​𝔼​[Xs​(Xu−Xη​(u))]​𝑑u|\displaystyle\leq C\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{s}(X\_{u}-X\_{\eta(u)})]du\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤CT​((1+sα−1)​𝐯n​(α)+s2​α−2n).\displaystyle\leq C\_{T}\left((1+s^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{s^{2\alpha-2}}{n}\right). |  |

Therefore, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xs]​𝑑s|\displaystyle\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{s}]ds\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CT​(∫0tk(tk−s)α−1Γ​(α)​(1+sα−1)​𝐯n​(α)​𝑑s+∫0tk(tk−s)α−1Γ​(α)​s2​α−2n​𝑑s)\displaystyle C\_{T}\left(\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}(1+s^{\alpha-1}){\bf v}\_{n}(\alpha)ds+\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}\frac{s^{2\alpha-2}}{n}ds\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | CT​(𝐯n​(α)​(tkαΓ​(α+1)+tk2​α−1​Γ​(α)Γ​(2​α))+tk3​α−2​Γ​(2​α−1)Γ​(3​α−1)​n)\displaystyle C\_{T}\left({\bf v}\_{n}(\alpha)\left(\frac{t\_{k}^{\alpha}}{\Gamma(\alpha+1)}+t\_{k}^{2\alpha-1}\frac{\Gamma(\alpha)}{\Gamma(2\alpha)}\right)+t\_{k}^{3\alpha-2}\frac{\Gamma(2\alpha-1)}{\Gamma(3\alpha-1)n}\right) |  |

If 3​α−2≥03\alpha-2\geq 0, this is upper bounded by CT​𝐯n​(α)C\_{T}{\bf v}\_{n}(\alpha), using that tk≤Tt\_{k}\leq T. Otherwise, we have tk3​α−2n≤t13​α−2n=T3​α−2n3​α−1≤CT​𝐯n​(α)\frac{t\_{k}^{3\alpha-2}}{n}\leq\frac{t\_{1}^{3\alpha-2}}{n}=\frac{T^{3\alpha-2}}{n^{3\alpha-1}}\leq C\_{T}{\bf v}\_{n}(\alpha). Therefore,

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xs]​𝑑s|≤CT​𝐯n​(α)\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{s}]ds\right|\leq C\_{T}{\bf v}\_{n}(\alpha) |  |

in all cases. We now prove that the same estimate holds for

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xη​(s)]​𝑑s|.\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{\eta(s)}]ds\right|. |  |

We use the triangular inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xη​(s)]​𝑑s|\displaystyle\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{\eta(s)}]ds\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |X0|​∫0t1(tk−s)α−1Γ​(α)​|𝔼​[Xˇtk1n−Xtk1]|​𝑑s\displaystyle|X\_{0}|\int\_{0}^{t\_{1}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}|{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}}]|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +CT​∫t1tk(tk−s)α−1Γ​(α)​(1+η​(s)α−1)​𝐯n​(α)​𝑑s+CT​∫t1tk(tk−s)α−1Γ​(α)​η​(s)2​α−2n​𝑑s.\displaystyle+C\_{T}\int\_{t\_{1}}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}(1+\eta(s)^{\alpha-1}){\bf v}\_{n}(\alpha)ds+C\_{T}\int\_{t\_{1}}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}\frac{\eta(s)^{2\alpha-2}}{n}ds. |  |

The first term is bounded by CT​TnC\_{T}\frac{T}{n} by using ([2.10](https://arxiv.org/html/2602.18234v1#S2.E10 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), and the other terms can be upper bounded as above, using that s2≤η​(s)\frac{s}{2}\leq\eta(s) for s≥t1s\geq t\_{1}. We finally get

|  |  |  |
| --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−s)α−1Γ​(α)​𝔼​[(Xˇtk1n−Xtk1)​Xη​(s)]​𝑑s|≤CT​𝐯n​(α).\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[(\check{X}^{n}\_{t\_{k\_{1}}}-X\_{t\_{k\_{1}}})X\_{\eta(s)}]ds\right|\leq C\_{T}{\bf v}\_{n}(\alpha). |  |

This gives the first estimate.

Finally, we get the estimate on the covariance ([2.11](https://arxiv.org/html/2602.18234v1#S2.E11 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |C​o​v​(Xtk1,Xtk2)−C​o​v​(Xˇtk1n,Xˇtk2n)|\displaystyle|Cov(X\_{t\_{k\_{1}}},X\_{t\_{k\_{2}}})-Cov(\check{X}^{n}\_{t\_{k\_{1}}},\check{X}^{n}\_{t\_{k\_{2}}})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |𝔼​[Xtk1​Xtk2]−𝔼​[Xˇtk1n​Xˇtk2n]|+|𝔼​[Xtk1]|​|𝔼​[Xtk2−Xˇntk2]|+|𝔼​[Xˇntk2]|​|𝔼​[Xtk1−Xˇntk1]|,\displaystyle|{\mathbb{E}}[X\_{t\_{k\_{1}}}X\_{t\_{k\_{2}}}]-{\mathbb{E}}[\check{X}^{n}\_{t\_{k\_{1}}}\check{X}^{n}\_{t\_{k\_{2}}}]|+|{\mathbb{E}}[X\_{t\_{k\_{1}}}]||{\mathbb{E}}[X\_{t\_{k\_{2}}}-{\check{X}^{n}}\_{t\_{k\_{2}}}]|+|{\mathbb{E}}[{\check{X}^{n}}\_{t\_{k\_{2}}}]||{\mathbb{E}}[X\_{t\_{k\_{1}}}-{\check{X}^{n}}\_{t\_{k\_{1}}}]|, |  |

noting that |𝔼​[Xtk1]||{\mathbb{E}}[X\_{t\_{k\_{1}}}]| and |𝔼​[Xˇntk2]||{\mathbb{E}}[{\check{X}^{n}}\_{t\_{k\_{2}}}]| are bounded (see Remark [2.9](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and using that |𝔼​[Xtk1−Xˇntk1]|≤CTn≤CT​𝐯n​(α).|{\mathbb{E}}[X\_{t\_{k\_{1}}}-{\check{X}^{n}}\_{t\_{k\_{1}}}]|\leq\frac{C\_{T}}{n}\leq C\_{T}{\bf v}\_{n}(\alpha).

As Ψ∈𝒞exp2​(ℝ,ℝ)\Psi\in\mathcal{C}\_{\exp}^{2}({\mathbb{R}},{\mathbb{R}}), we apply Lemma [A.6](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and get with m​(u)=(1−u)​𝔼​[Xtk]+u​𝔼​[Xˇntk]m(u)=(1-u){\mathbb{E}}[X\_{t\_{k}}]+u{\mathbb{E}}[{\check{X}^{n}}\_{t\_{k}}], Σ​(u)=(1−u)​𝒞X​(tk,tk)+u​C​o​v​(Xˇntk,Xˇntk)\Sigma(u)=(1-u){\mathcal{C}^{X}}(t\_{k},t\_{k})+uCov({\check{X}^{n}}\_{t\_{k}},{\check{X}^{n}}\_{t\_{k}}), u∈[0,1]u\in[0,1], and Zu∼𝒩​(m​(u),Σ​(u))Z\_{u}\sim\mathcal{N}(m(u),\Sigma(u)),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Ψ​(Xˇntk)]−𝔼​[Ψ​(Xtk)]=\displaystyle{\mathbb{E}}[\Psi({\check{X}^{n}}\_{t\_{k}})]-{\mathbb{E}}[\Psi(X\_{t\_{k}})]= | ∫01(𝔼​[Xˇntk]−𝔼​[Xtk])​𝔼​[Ψ′​(Zu)]​𝑑u\displaystyle\int\_{0}^{1}\left({\mathbb{E}}[{\check{X}^{n}}\_{t\_{k}}]-{\mathbb{E}}[X\_{t\_{k}}]\right){\mathbb{E}}[\Psi^{\prime}(Z\_{u})]du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0112​(C​o​v​(Xˇntk,Xˇntk)−𝒞X​(tk,tk))​𝔼​[Ψ′′​(Zu)]​𝑑u.\displaystyle+\int\_{0}^{1}\frac{1}{2}\left(Cov({\check{X}^{n}}\_{t\_{k}},{\check{X}^{n}}\_{t\_{k}})-{\mathcal{C}^{X}}(t\_{k},t\_{k})\right){\mathbb{E}}[\Psi^{\prime\prime}(Z\_{u})]du. |  |

By straightforward calculations, |𝔼​[Ψ′​(Zu)]|+|𝔼​[Ψ′′​(Zu)]|≤C​eC​|m​(u)|+C2​Σ​(u)22≤C​eC​m¯+C2​Σ¯22|{\mathbb{E}}[\Psi^{\prime}(Z\_{u})]|+|{\mathbb{E}}[\Psi^{\prime\prime}(Z\_{u})]|\leq Ce^{C|m(u)|+\frac{C^{2}\Sigma(u)^{2}}{2}}\leq Ce^{C\overline{m}+\frac{C^{2}\overline{\Sigma}^{2}}{2}} for some C∈ℝ+C\in{\mathbb{R}}\_{+}, where

|  |  |  |
| --- | --- | --- |
|  | m¯=supn≥1max1≤k≤nmax(|𝔼(Xtk)|,|𝔼(Xˇntk|) and Σ¯=supn≥1max1≤k≤nmax(𝒞X(tk,tk),Cov(Xˇntk,Xˇntk))\overline{m}=\sup\_{n\geq 1}\max\_{1\leq k\leq n}\max(|{\mathbb{E}}(X\_{t\_{k}})|,|{\mathbb{E}}({\check{X}^{n}}\_{t\_{k}}|)\text{ and }\overline{\Sigma}=\sup\_{n\geq 1}\max\_{1\leq k\leq n}\max({\mathcal{C}^{X}}(t\_{k},t\_{k}),Cov({\check{X}^{n}}\_{t\_{k}},{\check{X}^{n}}\_{t\_{k}})) |  |

are finite by Equations ([2.3](https://arxiv.org/html/2602.18234v1#S2.E3 "In Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and ([2.5](https://arxiv.org/html/2602.18234v1#S2.E5 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and Remark [2.9](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). Using again Equation ([2.11](https://arxiv.org/html/2602.18234v1#S2.E11 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[Ψ​(Xˇntk)]−𝔼​[Ψ​(Xtk)]|≤C​eC​m¯+C2​Σ¯22​CT​((1+tkα−1)​𝐯n​(α)+tk2​α−2n).∎|{\mathbb{E}}[\Psi({\check{X}^{n}}\_{t\_{k}})]-{\mathbb{E}}[\Psi(X\_{t\_{k}})]|\leq Ce^{C\overline{m}+\frac{C^{2}\overline{\Sigma}^{2}}{2}}C\_{T}\left((1+t\_{k}^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{t\_{k}^{2\alpha-2}}{n}\right).\qed |  |

We see from the proof that the covariance estimation ([2.11](https://arxiv.org/html/2602.18234v1#S2.E11 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) is only needed at time tn=Tt\_{n}=T to deduce the weak error rate. However, the full estimation ([2.11](https://arxiv.org/html/2602.18234v1#S2.E11 "In Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) at times tk1t\_{k\_{1}} and tk2t\_{k\_{2}} will be crucial to get the weak error rate of the rough mean-reverting stochastic volatility model. We will also need the following estimate between the Malliavin derivatives of the scheme and the SVE.

###### Lemma 2.11.

Let 1≤k≤n1\leq k\leq n. We have Xˇntk∈𝔻1,2{\check{X}^{n}}\_{t\_{k}}\in\mathbb{D}^{1,2}. The Malliavin derivative of Xˇntk{\check{X}^{n}}\_{t\_{k}} is deterministic and satisfies for s∈(0,tk)s\in(0,t\_{k}),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒟s​Xˇntk\displaystyle\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}} | =κ2​∫0tk𝒟s​Xˇnη​(u)​(tk−u)α−1Γ​(α)​𝑑u+σ​(tk−s)α−1Γ​(α).\displaystyle=\kappa\_{2}\int\_{0}^{t\_{k}}\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(u)}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du+\sigma\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}. |  | (2.14) |

Besides, there is a constant C∈ℝ+C\in{\mathbb{R}}\_{+} depending on the parameters α,κ2,σ\alpha,\kappa\_{2},\sigma, γ\gamma and T>0T>0 such that for all n≥1n\geq 1 and tj≤tk≤Tt\_{j}\leq t\_{k}\leq T,

|  |  |  |
| --- | --- | --- |
|  | |∫0tj(𝒟s​Xˇntk−𝒟s​Xtk)​𝑑s|≤C​Tn​ and ​∫0tk|𝒟s​Xˇntk|​𝑑s≤C.\left|\int\_{0}^{t\_{j}}\left(\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}-\mathcal{D}\_{s}X\_{t\_{k}}\right)ds\right|\leq C\frac{T}{n}\text{ and }\int\_{0}^{t\_{k}}|\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}|ds\leq C. |  |

Let us note that 𝒟s​Xˇntk\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}} not only blows up when s→tks\to t\_{k}, but also from the induction formula ([2.14](https://arxiv.org/html/2602.18234v1#S2.E14 "In Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) when s→tjs\to t\_{j} for j≤kj\leq k, since 𝒟s​Xˇntk=∑j=1k−1∫tjtj+1(tk−u)α−1Γ​(α)​𝑑u​𝒟s​Xˇntj+σ​(tk−s)α−1Γ​(α)\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}=\sum\_{j=1}^{k-1}\int\_{t\_{j}}^{t\_{j+1}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{j}}+\sigma\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}. In contrast, 𝒟s​Xtk\mathcal{D}\_{s}X\_{t\_{k}} is continuous for s<tks<t\_{k} and only blows up when s→tks\to t\_{k}. Therefore, there is no hope to get a uniform bound on |𝒟s​Xˇntk−𝒟s​Xtk||\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}-\mathcal{D}\_{s}X\_{t\_{k}}| for s∈[0,tk)s\in[0,t\_{k}). However, Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") shows that the error between the integrals has a nice rate of convergence. Besides, We will also need the following estimates on some integrals of |𝒟s​Xˇntk−𝒟s​Xtk||\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}-\mathcal{D}\_{s}X\_{t\_{k}}|.

###### Lemma 2.12.

There exists a constant C∈ℝ+C\in{\mathbb{R}}\_{+} that does not depend on n∈ℕ∗n\in{\mathbb{N}}^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | max0≤k,ℓ≤n​∫0tk|𝒟s​Xtℓ−𝒟s​Xˇntℓ|​𝑑s≤C​n−α.\max\_{0\leq k,\ell\leq n}\int\_{0}^{t\_{k}}|\mathcal{D}\_{s}X\_{t\_{\ell}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{\ell}}|ds\leq Cn^{-\alpha}. |  |

This lemma will be crucial and enough to prove the weak rate of convergence for the mean-reverting rough stochastic volatility model.
Their proofs are postponed in the appendix section.

## 3. Weak error approximation with the cubic test function

In this section, we are interested in studying the weak error convergence rate of the scheme ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). Namely, for Φ:ℝ→ℝ\Phi:{\mathbb{R}}\to{\mathbb{R}}, we want to upper bound 𝔼​[Φ​(LˇTn)]−𝔼​[Φ​(LT)]{\mathbb{E}}[\Phi(\check{L}^{n}\_{T})]-{\mathbb{E}}[\Phi(L\_{T})]. When Φ\Phi has a polynomial growth, these expectations are well defined. More precisely, we have the following result.

###### Lemma 3.1.

Let Φ,f:ℝ→ℝ\Phi,f:{\mathbb{R}}\to{\mathbb{R}} be measurable. We assume that:

* •

  there exists C,p>0C,p>0 such that |Φ​(x)|≤C​(1+|x|p)|\Phi(x)|\leq C(1+|x|^{p}) for all x∈ℝx\in{\mathbb{R}},
* •

  there exists C>0C>0 such that |f​(x)|≤C​eC​|x||f(x)|\leq Ce^{C|x|}.

Then, 𝔼​[Φ​(LˇTn)]{\mathbb{E}}[\Phi(\check{L}^{n}\_{T})] and 𝔼​[Φ​(LT)]{\mathbb{E}}[\Phi(L\_{T})] are well defined and finite.

###### Proof.

Without loss of generality, we assume p≥2p\geq 2. By Burkholder-Davis-Gundy’s inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|∫0Tf​(Xt)​𝑑Bt|p]\displaystyle{\mathbb{E}}\left[\left|\int\_{0}^{T}f(X\_{t})dB\_{t}\right|^{p}\right] | ≤Cp​𝔼​[|∫0Tf2​(Xt)​𝑑t|p/2]\displaystyle\leq C\_{p}{\mathbb{E}}\left[\left|\int\_{0}^{T}f^{2}(X\_{t})dt\right|^{p/2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cp​Tp/2−1​∫0T𝔼​[|f​(Xt)|p]​𝑑t\displaystyle\leq C\_{p}T^{p/2-1}\int\_{0}^{T}{\mathbb{E}}\left[|f(X\_{t})|^{p}\right]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cp​Tp/2−1​∫0TCp​𝔼​[ep​C​|Xt|]​𝑑t,\displaystyle\leq C\_{p}T^{p/2-1}\int\_{0}^{T}C^{p}{\mathbb{E}}\left[e^{pC|X\_{t}|}\right]dt, |  |

which is finite since XtX\_{t} is a Gaussian process with continuous mean and variance, see Propositions [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). The same conclusion holds for Xˇn{\check{X}^{n}} by using Remark [2.9](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").
∎

For the sake of readability, we start by the case Φ​(x)=x3\Phi(x)=x^{3} as in Gassiat [[12](https://arxiv.org/html/2602.18234v1#bib.bib12)], to better emphasize the difficulty coming from the discretization of the rough Volterra SDE and how to manage it. The case Φ​(x)=x2\Phi(x)=x^{2} is too simple due to the Itô isometry as pointed out by Neuenkirch in [[6](https://arxiv.org/html/2602.18234v1#bib.bib6)]. We also assume in this section b≡0b\equiv 0 and L0=0L\_{0}=0 in ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) for the sake of simplicity. We want to analyse the weak error:

|  |  |  |
| --- | --- | --- |
|  | ℰ=𝔼​[(∫0Tf​(Xt)​𝑑Bt)3]−𝔼​[(∫0Tf​(Xˇnη​(t))​𝑑Bt)3].\mathcal{E}={\mathbb{E}}\left[\left(\int\_{0}^{T}f(X\_{t})dB\_{t}\right)^{3}\right]-{\mathbb{E}}\left[\left(\int\_{0}^{T}f({\check{X}^{n}}\_{\eta(t)})dB\_{t}\right)^{3}\right]. |  |

It is known (see [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Proposition 6.1]) to be the prototypical case to get familiar with the structure of the weak error rate, avoiding too much heavy notation. Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] have indeed noticed this and were able to extend to any polynomial test function by an induction procedure with iterated integrals. In Section [4](https://arxiv.org/html/2602.18234v1#S4 "4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we show that we can also in our case extend the result to any polynomial functions. However, the iterated integrals coming from arbitrary polynomial functions raise new difficulties due to the discretization step, which does not appear in the work by Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)].

By Itô calculus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∫0Tf​(Xt)​𝑑Bt)3=\displaystyle\left(\int\_{0}^{T}f(X\_{t})dB\_{t}\right)^{3}= | 3​∫0T(∫0tf​(Xs)​𝑑Bs)2​f​(Xt)​𝑑Bt\displaystyle 3\int\_{0}^{T}\left(\int\_{0}^{t}f(X\_{s})dB\_{s}\right)^{2}f(X\_{t})dB\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​∫0T(∫0tf​(Xs)​𝑑Bs)​f​(Xt)2​𝑑t,\displaystyle+3\int\_{0}^{T}\left(\int\_{0}^{t}f(X\_{s})dB\_{s}\right)f(X\_{t})^{2}dt, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∫0Tf​(Xˇnη​(t))​𝑑Bt)3=\displaystyle\left(\int\_{0}^{T}f({\check{X}^{n}}\_{\eta(t)})dB\_{t}\right)^{3}= | 3​∫0T(∫0tf​(Xˇnη​(s))​𝑑Bs)2​f​(Xˇnη​(t))​𝑑Wt\displaystyle 3\int\_{0}^{T}\left(\int\_{0}^{t}f({\check{X}^{n}}\_{\eta(s)})dB\_{s}\right)^{2}f({\check{X}^{n}}\_{\eta(t)})dW\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3​∫0T(∫0tf​(Xˇnη​(s))​𝑑Bs)​f​(Xˇnη​(t))2​𝑑t.\displaystyle+3\int\_{0}^{T}\left(\int\_{0}^{t}f({\check{X}^{n}}\_{\eta(s)})dB\_{s}\right)f({\check{X}^{n}}\_{\eta(t)})^{2}dt. |  |

We assume that f∈𝒞exp3​(ℝ,ℝ)f\in\mathcal{C}\_{\exp}^{3}({\mathbb{R}},{\mathbb{R}}), see ([2.8](https://arxiv.org/html/2602.18234v1#S2.E8 "In 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).
This gives in particular that the Itô integrals are true martingales and have a zero expectation. We then use the Clark-Ocone formula (see e.g. [[19](https://arxiv.org/html/2602.18234v1#bib.bib19), Proposition 1.3.14] that can be applied thanks to Proposition [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0Tf​(Xt)​𝑑Bt)3]\displaystyle{\mathbb{E}}\left[\left(\int\_{0}^{T}f(X\_{t})dB\_{t}\right)^{3}\right] | =3​∫0T𝔼​[(∫0tf​(Xs)​𝑑Bs)​f​(Xt)2]​𝑑t\displaystyle=3\int\_{0}^{T}{\mathbb{E}}\left[\left(\int\_{0}^{t}f(X\_{s})dB\_{s}\right)f(X\_{t})^{2}\right]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =6​ρ​∫0T∫0t𝔼​[f​(Xs)​f​f′​(Xt)​𝒟s​Xt]​𝑑s​𝑑t.\displaystyle=6\rho\int\_{0}^{T}\int\_{0}^{t}{\mathbb{E}}[f(X\_{s})ff^{\prime}(X\_{t})\mathcal{D}\_{s}X\_{t}]dsdt. |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0Tf​(Xˇnη​(t))​𝑑Bt)3]\displaystyle{\mathbb{E}}\left[\left(\int\_{0}^{T}f({\check{X}^{n}}\_{\eta(t)})dB\_{t}\right)^{3}\right] | =3​∫0T𝔼​[(∫0tf​(Xˇnη​(s))​𝑑Bs)​f​(Xˇnη​(t))2]​𝑑t\displaystyle=3\int\_{0}^{T}{\mathbb{E}}\left[\left(\int\_{0}^{t}f({\check{X}^{n}}\_{\eta(s)})dB\_{s}\right)f({\check{X}^{n}}\_{\eta(t)})^{2}\right]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =6​ρ​∫0T∫0η​(t)𝔼​[f​(Xˇnη​(s))​f​f′​(Xˇnη​(t))​𝒟s​Xˇnη​(t)]​𝑑s​𝑑t.\displaystyle=6\rho\int\_{0}^{T}\int\_{0}^{\eta(t)}{\mathbb{E}}[f({\check{X}^{n}}\_{\eta(s)})ff^{\prime}({\check{X}^{n}}\_{\eta(t)})\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}]dsdt. |  |

Let us recall that from Proposition [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), both 𝒟s​Xt\mathcal{D}\_{s}X\_{t} and 𝒟s​Xˇnη​(t)\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)} are deterministic.
We write then this error as ℰ=6​ρ​(ℰ1+ℰ2)\mathcal{E}=6\rho(\mathcal{E}\_{1}+\mathcal{E}\_{2}), with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℰ1\displaystyle\mathcal{E}\_{1} | =∫0T∫0t𝔼​[f​(Xs)​f​f′​(Xt)]​𝒟s​Xt−𝔼​[f​(Xη​(s))​f​f′​(Xη​(t))]​𝒟s​Xη​(t)​d​s​d​t,\displaystyle=\int\_{0}^{T}\int\_{0}^{t}{\mathbb{E}}[f(X\_{s})ff^{\prime}(X\_{t})]\mathcal{D}\_{s}X\_{t}-{\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{\eta(t)})]\mathcal{D}\_{s}X\_{\eta(t)}dsdt, |  | (3.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℰ2\displaystyle\mathcal{E}\_{2} | =∫0T∫0η​(t)𝔼​[f​(Xη​(s))​f​f′​(Xη​(t))]​𝒟s​Xη​(t)−𝔼​[f​(Xˇnη​(s))​f​f′​(Xˇnη​(t))]​𝒟s​Xˇnη​(t)​d​s​d​t,\displaystyle=\int\_{0}^{T}\int\_{0}^{\eta(t)}{\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{\eta(t)})]\mathcal{D}\_{s}X\_{\eta(t)}-{\mathbb{E}}[f({\check{X}^{n}}\_{\eta(s)})ff^{\prime}({\check{X}^{n}}\_{\eta(t)})]\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}dsdt, |  | (3.2) |

noting that 𝒟s​Xη​(t)=𝒟s​Xˇnη​(t)=0\mathcal{D}\_{s}X\_{\eta(t)}=\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}=0 for s∈(η​(t),t)s\in(\eta(t),t).
The analysis of ℰ1\mathcal{E}\_{1} adapts the arguments of Gassiat [[12](https://arxiv.org/html/2602.18234v1#bib.bib12)] and Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] for the rough Stochastic Volterra Equation XX, since the model considered in these papers corresponds to the case κ1=κ2=0\kappa\_{1}=\kappa\_{2}=0. In contrast, the analysis of ℰ2\mathcal{E}\_{2} is completely new and exploits the results obtained in Section [2](https://arxiv.org/html/2602.18234v1#S2 "2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") to upper bound the approximation error on the volatility process XX. The striking result is that we still get a convergence rate in O​(𝐯n​(α))O({\bf v}\_{n}(\alpha)), the same as in [[12](https://arxiv.org/html/2602.18234v1#bib.bib12)] and [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)]. Thus, the additional discretization of XX does not affect the convergence rate.

###### Theorem 3.2.

Let LL be the process defined by ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) with L0=0L\_{0}=0, b≡0b\equiv 0 and f∈𝒞exp3​(ℝ,ℝ)f\in\mathcal{C}\_{\exp}^{3}({\mathbb{R}},{\mathbb{R}}). Let Lˇn\check{L}^{n} denote the approximation scheme ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) with time step T/nT/n. Then, there exists C∈ℝ+C\in{\mathbb{R}}\_{+} such that for n≥1n\geq 1,

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[(LˇTn)3]−𝔼​[(LT)3]|≤C​𝐯n​(α).\left|{\mathbb{E}}[(\check{L}^{n}\_{T})^{3}]-{\mathbb{E}}[(L\_{T})^{3}]\right|\leq C{\bf v}\_{n}(\alpha). |  |

###### Proof.

We split the analysis in the two terms ([3.1](https://arxiv.org/html/2602.18234v1#S3.E1 "In 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and ([3.2](https://arxiv.org/html/2602.18234v1#S3.E2 "In 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

∙\bullet Analysis of ℰ1\mathcal{E}\_{1}.
The term ℰ1\mathcal{E}\_{1} can be analysed in the same way as [[12](https://arxiv.org/html/2602.18234v1#bib.bib12), Theorem 2.1], but with some modifications to get symmetrized estimates on the covariance (see Lemma [A.3](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). We write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1\displaystyle\mathcal{E}\_{1} | =ℰ1,1+ℰ1,2​ with\displaystyle=\mathcal{E}\_{1,1}+\mathcal{E}\_{1,2}\text{ with} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,1\displaystyle\mathcal{E}\_{1,1} | =∫0T∫0t𝔼​[f​(Xs)​f​f′​(Xt)]​(𝒟s​Xt−𝒟s​Xη​(t))​𝑑s​𝑑t\displaystyle=\int\_{0}^{T}\int\_{0}^{t}{\mathbb{E}}[f(X\_{s})ff^{\prime}(X\_{t})](\mathcal{D}\_{s}X\_{t}-\mathcal{D}\_{s}X\_{\eta(t)})dsdt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,2\displaystyle\mathcal{E}\_{1,2} | =∫0T∫0η​(t)𝔼​[(f​(Xs)​f​f′​(Xt)−f​(Xη​(s))​f​f′​(Xη​(t)))]​𝒟s​Xη​(t)​𝑑s​𝑑t\displaystyle=\int\_{0}^{T}\int\_{0}^{\eta(t)}{\mathbb{E}}\left[\left(f(X\_{s})ff^{\prime}(X\_{t})-f(X\_{\eta(s)})ff^{\prime}(X\_{\eta(t)})\right)\right]\mathcal{D}\_{s}X\_{\eta(t)}dsdt |  |

where we use for ℰ1,2\mathcal{E}\_{1,2} that 𝒟s​Xη​(t)=0\mathcal{D}\_{s}X\_{\eta(t)}=0 for s>η​(t)s>\eta(t). In fact, we get from ([2.4](https://arxiv.org/html/2602.18234v1#S2.E4 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")):

|  |  |  |
| --- | --- | --- |
|  | 𝒟s​Xt=𝒟s​𝒴t=𝟏s<t​σ​∑i=1∞κ2i−1​(t−s)i​α−1Γ​(i​α),\mathcal{D}\_{s}X\_{t}=\mathcal{D}\_{s}\mathcal{Y}\_{t}=\mathbf{1}\_{s<t}\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{(t-s)^{i\alpha-1}}{\Gamma(i\alpha)}, |  |

which is deterministic.

We first focus on ℰ1,1\mathcal{E}\_{1,1}. We note

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(s,t)=𝔼​[f​(Xs)​f​f′​(Xt)],s,t≥0,\phi(s,t)={\mathbb{E}}[f(X\_{s})ff^{\prime}(X\_{t})],\ s,t\geq 0, |  | (3.3) |

and have
ℰ1,1=ℰ1,1′+ℰ1,1′′{\mathcal{E}}\_{1,1}={\mathcal{E}}^{\prime}\_{1,1}+{\mathcal{E}}^{\prime\prime}\_{1,1}
with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,1′\displaystyle{\mathcal{E}}^{\prime}\_{1,1} | =∫0T∫0t(ϕ​(s,t)−ϕ​(t,t))​(𝒟s​Xt−𝒟s​Xη​(t))​𝑑s​𝑑t\displaystyle=\int\_{0}^{T}\int\_{0}^{t}(\phi(s,t)-\phi(t,t))(\mathcal{D}\_{s}X\_{t}-\mathcal{D}\_{s}X\_{\eta(t)})dsdt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,1′′\displaystyle{\mathcal{E}}^{\prime\prime}\_{1,1} | =∫0Tϕ​(t,t)​∫0t(𝒟s​Xt−𝒟s​Xη​(t))​𝑑s​𝑑t.\displaystyle=\int\_{0}^{T}\phi(t,t)\int\_{0}^{t}(\mathcal{D}\_{s}X\_{t}-\mathcal{D}\_{s}X\_{\eta(t)})dsdt. |  |

By Corollary [A.5](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem5 "Corollary A.5. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (1), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ϕ​(t,t)−ϕ​(s,t)|\displaystyle|\phi(t,t)-\phi(s,t)| | ≤C​|t−s|2​α−1.\displaystyle\leq C|t-s|^{2\alpha-1}. |  |

From the formula of 𝒟s​Xt\mathcal{D}\_{s}X\_{t}, we get by the triangular inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ1,1′|≤C∑i=1∞|κ2i−1|Γ​(i​α)∫0T(\displaystyle|{\mathcal{E}}^{\prime}\_{1,1}|\leq C\sum\_{i=1}^{\infty}\frac{|\kappa\_{2}^{i-1}|}{\Gamma(i\alpha)}\int\_{0}^{T}\Bigg( | ∫0η​(t)(t−s)2​α−1​|(t−s)i​α−1−(η​(t)−s)i​α−1|​𝑑s\displaystyle\int\_{0}^{\eta(t)}(t-s)^{2\alpha-1}\left|(t-s)^{i\alpha-1}-(\eta(t)-s)^{i\alpha-1}\right|ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫η​(t)t(t−s)2​α−1(t−s)i​α−1)dt.\displaystyle+\int\_{\eta(t)}^{t}(t-s)^{2\alpha-1}(t-s)^{i\alpha-1}\Bigg)dt. |  |

For i≥2i\geq 2, we have i​α−1>0i\alpha-1>0 and the term in parentheses is equal to

|  |  |  |
| --- | --- | --- |
|  | ∫0t(t−s)(2+i)​α−2​𝑑s−∫0η​(t)(t−s)2​α−1​(η​(t)−s)i​α−1​𝑑s\displaystyle\int\_{0}^{t}(t-s)^{(2+i)\alpha-2}ds-\int\_{0}^{\eta(t)}(t-s)^{2\alpha-1}(\eta(t)-s)^{i\alpha-1}ds |  |
|  |  |  |
| --- | --- | --- |
|  | ≤1(2+i)​α−1(t(2+i)​α−1−η(t))(2+i)​α−1)≤T(2+i)​α−2Tn.\displaystyle\leq\frac{1}{(2+i)\alpha-1}(t^{(2+i)\alpha-1}-\eta(t))^{(2+i)\alpha-1})\leq T^{(2+i)\alpha-2}\frac{T}{n}. |  |

For i=1i=1, the same term is equal to

|  |  |  |
| --- | --- | --- |
|  | ∫0η​(t)(t−s)2​α−1​(η​(t)−s)α−1​𝑑s−∫0t(t−s)3​α−2​𝑑s+2​∫η​(t)t(t−s)3​α−2​𝑑s\displaystyle\int\_{0}^{\eta(t)}(t-s)^{2\alpha-1}(\eta(t)-s)^{\alpha-1}ds-\int\_{0}^{t}(t-s)^{3\alpha-2}ds+2\int\_{\eta(t)}^{t}(t-s)^{3\alpha-2}ds |  |
|  |  |  |
| --- | --- | --- |
|  | =t2​α−1​(η​(t)α​F12​(1−2​α,1,1+α,η​(t)t)−tα​F12​(1−2​α,1,1+α,1))+2​∫η​(t)t(t−s)3​α−2​𝑑s.\displaystyle=t^{2\alpha-1}\left(\eta(t)^{\alpha}{{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,\frac{\eta(t)}{t})-t^{\alpha}{{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,1)\right)+2\int\_{\eta(t)}^{t}(t-s)^{3\alpha-2}ds. |  |

By elementary calculations, we get ∫0T∫η​(t)t(t−s)3​α−2​𝑑s=O​(1n3​α−1)=O​(𝐯n​(α))\int\_{0}^{T}\int\_{\eta(t)}^{t}(t-s)^{3\alpha-2}ds=O(\frac{1}{n^{3\alpha-1}})=O({\bf v}\_{n}(\alpha)). Now, we write the term in parenthesis as the sum

|  |  |  |
| --- | --- | --- |
|  | η​(t)α​(F12​(1−2​α,1,1+α,η​(t)t)−F12​(1−2​α,1,1+α,1))+(η​(t)α−tα)​F12​(1−2​α,1,1+α,1).\eta(t)^{\alpha}\left({{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,\frac{\eta(t)}{t})-{{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,1)\right)+(\eta(t)^{\alpha}-t^{\alpha}){{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,1). |  |

We have ∫0Tt2​α−1​(tα−η​(t)α)​𝑑t≤T2​α−1​∫0T(tα−η​(t)α)​𝑑t≤C​Tn\int\_{0}^{T}t^{2\alpha-1}(t^{\alpha}-\eta(t)^{\alpha})dt\leq T^{2\alpha-1}\int\_{0}^{T}(t^{\alpha}-\eta(t)^{\alpha})dt\leq C\frac{T}{n} by [[8](https://arxiv.org/html/2602.18234v1#bib.bib8), Theorem 2.4], and we focus now on the first term

|  |  |  |
| --- | --- | --- |
|  | ∫0Tt2​α−1​η​(t)α​(F12​(1−2​α,1,1+α,η​(t)t)−F12​(1−2​α,1,1+α,1))​𝑑t,\int\_{0}^{T}t^{2\alpha-1}\eta(t)^{\alpha}\left({{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,\frac{\eta(t)}{t})-{{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,1)\right)dt, |  |

which is positive since z↦F12​(1−2​α,1,1+α,z)z\mapsto{{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,z) is decreasing, as the first argument is negative see [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Eq. 15.6.1]. We use then η​(t)α≤tα\eta(t)^{\alpha}\leq t^{\alpha}.
The function z↦F12​(1−2​α,1,1+α,z)z\mapsto{{}\_{2}F\_{1}}(1-2\alpha,1,1+\alpha,z) is differentiable, and the derivative is given by 1−2​α1+α​F12​(2−2​α,2,2+α,z)\frac{1-2\alpha}{1+\alpha}{{}\_{2}F\_{1}}(2-2\alpha,2,2+\alpha,z), see [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Eq. 15.5.1]. It is bounded uniformly for z∈[0,1]z\in[0,1] if 3​α−2>03\alpha-2>0, see Equation ([A.4](https://arxiv.org/html/2602.18234v1#A1.E4 "In Proof. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), and then the term is upper bounded by C​T/nCT/n. Otherwise,
it is upper bounded, up to a constant by C​(1−z)3​α−2C(1-z)^{3\alpha-2} (see [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Eq. 15.8.1]), and the same term is then upper bounded by

|  |  |  |
| --- | --- | --- |
|  | ∫0Tt3​α−1​∫η​(t)t1C​(1−z)3​α−2​𝑑z​𝑑t=C3​α−1​∫0T(t3​α−1−η​(t)3​α−1)​𝑑t≤C​Tn,\int\_{0}^{T}t^{3\alpha-1}\int\_{\frac{\eta(t)}{t}}^{1}C(1-z)^{3\alpha-2}dzdt=\frac{C}{3\alpha-1}\int\_{0}^{T}(t^{3\alpha-1}-\eta(t)^{3\alpha-1})dt\leq C\frac{T}{n}, |  |

by [[8](https://arxiv.org/html/2602.18234v1#bib.bib8), Theorem 2.4]. Thus, in all cases, we have ℰ1,1′≤C​𝐯n​(α).{\mathcal{E}}^{\prime}\_{1,1}\leq C{\bf v}\_{n}(\alpha).

For ℰ1,1′′{\mathcal{E}}^{\prime\prime}\_{1,1}, we have ∫0t𝒟s​Xt−𝒟s​Xη​(t)​d​s=σ​∑i=1∞κ2i−1​ti​α−η​(t)i​αΓ​(i​α+1)\int\_{0}^{t}\mathcal{D}\_{s}X\_{t}-\mathcal{D}\_{s}X\_{\eta(t)}ds=\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{t^{i\alpha}-\eta(t)^{i\alpha}}{\Gamma(i\alpha+1)} and thus using the boundedness of ϕ\phi we get

|  |  |  |
| --- | --- | --- |
|  | |ℰ1,1′′|≤C​σ​∑i=1∞|κ2|i−1​1Γ​(i​α+1)​∫0T(ti​α−η​(t)i​α)​𝑑t.|{\mathcal{E}}^{\prime\prime}\_{1,1}|\leq C\sigma\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\frac{1}{\Gamma(i\alpha+1)}\int\_{0}^{T}(t^{i\alpha}-\eta(t)^{i\alpha})dt. |  |

We have ∫0T(ti​α−η​(t)i​α)​𝑑t≤C​i​α​Ti​α​Tn\int\_{0}^{T}(t^{i\alpha}-\eta(t)^{i\alpha})dt\leq Ci\alpha T^{i\alpha}\frac{T}{n} by [[8](https://arxiv.org/html/2602.18234v1#bib.bib8), Theorem 2.4], which gives that |ℰ1,1′′|≤Cn|{\mathcal{E}}^{\prime\prime}\_{1,1}|\leq\frac{C}{n} since the series converges.

We now analyse ℰ1,2=∫0T∫0η​(t)(ϕ​(s,t)−ϕ​(η​(s),η​(t)))​𝒟s​Xη​(t)​𝑑s​𝑑t{\mathcal{E}}\_{1,2}=\int\_{0}^{T}\int\_{0}^{\eta(t)}(\phi(s,t)-\phi(\eta(s),\eta(t)))\mathcal{D}\_{s}X\_{\eta(t)}dsdt. We proceed as in [[12](https://arxiv.org/html/2602.18234v1#bib.bib12), Lemma 2.3] and split the integration domain as the disjunct union of

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃1\displaystyle\mathbf{D}\_{1} | :={(s,t)∈(0,T)2:s≤η​(t),t−s≤2​Tn,s≥2​Tn}\displaystyle:=\{(s,t)\in(0,T)^{2}:s\leq\eta(t),\ t-s\leq\frac{2T}{n},\ s\geq\frac{2T}{n}\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃2\displaystyle\mathbf{D}\_{2} | :={(s,t)∈(0,T)2:s≤η​(t),t−s>2​Tn,s≥2​Tn}\displaystyle:=\{(s,t)\in(0,T)^{2}:s\leq\eta(t),\ t-s>\frac{2T}{n},\ s\geq\frac{2T}{n}\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃3\displaystyle\mathbf{D}\_{3} | :={(s,t)∈(0,T)2:s≤η​(t),s<2​Tn},\displaystyle:=\{(s,t)\in(0,T)^{2}:s\leq\eta(t),\ s<\frac{2T}{n}\}, |  |

and we note ℰ1,2,1{\mathcal{E}}\_{1,2,1}, ℰ1,2,2{\mathcal{E}}\_{1,2,2} and ℰ1,2,3{\mathcal{E}}\_{1,2,3} the corresponding terms. From Corollary [A.5](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem5 "Corollary A.5. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (1) and ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ1,2,1|\displaystyle|{\mathcal{E}}\_{1,2,1}| | ≤C​(Tn)2​α−1​∫0T∫2​Tn∨(t−2​Tn)η​(t)σ​∑i=1∞|κ2|i−1​(η​(t)−s)i​α−1Γ​(i​α)​d​s​d​t\displaystyle\leq C\left(\frac{T}{n}\right)^{2\alpha-1}\int\_{0}^{T}\int\_{\frac{2T}{n}\vee\left(t-\frac{2T}{n}\right)}^{\eta(t)}\sigma\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\frac{(\eta(t)-s)^{i\alpha-1}}{\Gamma(i\alpha)}dsdt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(Tn)2​α−1​σ​∑i=1∞|κ2|i−1​∫0T(η​(t)−(t−2​T/n))i​αΓ​(i​α+1)​𝑑t\displaystyle\leq C\left(\frac{T}{n}\right)^{2\alpha-1}\sigma\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\int\_{0}^{T}\frac{(\eta(t)-(t-2T/n))^{i\alpha}}{\Gamma(i\alpha+1)}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(Tn)2​α−1​σ​∑i=1∞|κ2|i−1​T​(2​T/n)i​αΓ​(i​α+1)=O​((Tn)3​α−1),\displaystyle\leq C\left(\frac{T}{n}\right)^{2\alpha-1}\sigma\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}T\frac{(2T/n)^{i\alpha}}{\Gamma(i\alpha+1)}=O\left(\left(\frac{T}{n}\right)^{3\alpha-1}\right), |  |

where we used 0≤η​(t)−(t−2​T/n)≤2​T/n0\leq\eta(t)-(t-2T/n)\leq 2T/n for the last inequality.

The second term is equal to

|  |  |  |
| --- | --- | --- |
|  | ℰ1,2,2=∫0T∫2​Tnt−2​Tn𝒟s​Xη​(t)​(∫η​(s)s∂1ϕ​(u,t)​d​u+∫η​(t)t∂2ϕ​(η​(s),v)​d​v)​𝑑s​𝑑t.\displaystyle{\mathcal{E}}\_{1,2,2}=\int\_{0}^{T}\int\_{\frac{2T}{n}}^{t-\frac{2T}{n}}\mathcal{D}\_{s}X\_{\eta(t)}\left(\int\_{\eta(s)}^{s}\partial\_{1}\phi(u,t)du+\int\_{\eta(t)}^{t}\partial\_{2}\phi(\eta(s),v)dv\right)dsdt. |  |

By Corollary [A.5](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem5 "Corollary A.5. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (2) and (3), we get since s↦s2​α−2s\mapsto s^{2\alpha-2} is decreasing

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ1,2,2|\displaystyle|{\mathcal{E}}\_{1,2,2}| | ≤C​Tn​∫0T∫2​Tnt−2​Tn|𝒟s​Xη​(t)|​(η​(s)2​α−2+(t−s)2​α−2+η​(t)2​α−2+(η​(t)−η​(s))2​α−2)​𝑑s​𝑑t\displaystyle\leq C\frac{T}{n}\int\_{0}^{T}\int\_{\frac{2T}{n}}^{t-\frac{2T}{n}}|\mathcal{D}\_{s}X\_{\eta(t)}|\left(\eta(s)^{2\alpha-2}+(t-s)^{2\alpha-2}+\eta(t)^{2\alpha-2}+(\eta(t)-\eta(s))^{2\alpha-2}\right)dsdt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​Tn​∫0T∫2​Tnt−2​Tn|𝒟s​Xη​(t)|​(s2​α−2+(t−s)2​α−2)​𝑑s​𝑑t.\displaystyle\leq C\frac{T}{n}\int\_{0}^{T}\int\_{\frac{2T}{n}}^{t-\frac{2T}{n}}|\mathcal{D}\_{s}X\_{\eta(t)}|\left(s^{2\alpha-2}+(t-s)^{2\alpha-2}\right)dsdt. |  |

For the last inequality, we used that η​(t)−η​(s)≥(t−s)/2\eta(t)-\eta(s)\geq(t-s)/2 and η​(s)≥s/2\eta(s)\geq s/2 since t−s≥2​Tnt-s\geq\frac{2T}{n} and s≥2​Tns\geq\frac{2T}{n}. From ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we have |𝒟s​Xη​(t)|≤C​(t−s)α−1+C|\mathcal{D}\_{s}X\_{\eta}(t)|\leq C(t-s)^{\alpha-1}+C since (η​(t)−s)≥(t−s)/2(\eta(t)-s)\geq(t-s)/2. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ1,2,2|\displaystyle|{\mathcal{E}}\_{1,2,2}| | ≤C​Tn​∫0T(t2​α−1+∫0ts2​α−2​(t−s)α−1​𝑑s+∫2​Tnt−2​Tns3​α−3​𝑑s)​𝑑t.\displaystyle\leq C\frac{T}{n}\int\_{0}^{T}\left(t^{2\alpha-1}+\int\_{0}^{t}s^{2\alpha-2}(t-s)^{\alpha-1}ds+\int\_{\frac{2T}{n}}^{t-\frac{2T}{n}}s^{3\alpha-3}ds\right)dt. |  |

Notice that ∫0ts2​α−2​(t−s)α−1​𝑑s=Γ​(2​α−1)​Γ​(α)Γ​(3​α−1)​t3​α−1\int\_{0}^{t}s^{2\alpha-2}(t-s)^{\alpha-1}ds=\frac{\Gamma(2\alpha-1)\Gamma(\alpha)}{\Gamma(3\alpha-1)}t^{3\alpha-1}. Thus the two first terms are in O​(T/n)O(T/n), and the third one is of order Tn​∫2​Tnt−2​Tns3​α−3​𝑑s=O​(𝐯n​(α))\frac{T}{n}\int\_{\frac{2T}{n}}^{t-\frac{2T}{n}}s^{3\alpha-3}ds=O({\bf v}\_{n}(\alpha)) using standard calculations.

Using again Corollary [A.5](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem5 "Corollary A.5. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (1), we bound the last term by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ1,2,3|\displaystyle|{\mathcal{E}}\_{1,2,3}| | ≤C​(Tn)2​α−1​∫TnT∫0η​(t)∧2​Tn(η​(t)−s)α−1+1​d​s​d​t\displaystyle\leq C\left(\frac{T}{n}\right)^{2\alpha-1}\int\_{\frac{T}{n}}^{T}\int\_{0}^{\eta(t)\wedge\frac{2T}{n}}(\eta(t)-s)^{\alpha-1}+1dsdt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(Tn)2​α−1​(2​T2n+∫Tn2​Tn(Tn)α​𝑑t+∫2​TnTη​(t)α−(η​(t)−2​Tn)α​d​t)=O​((Tn)3​α−1),\displaystyle\leq C\left(\frac{T}{n}\right)^{2\alpha-1}\left(\frac{2T^{2}}{n}+\int\_{\frac{T}{n}}^{\frac{2T}{n}}\left(\frac{T}{n}\right)^{\alpha}dt+\int\_{\frac{2T}{n}}^{T}\eta(t)^{\alpha}-(\eta(t)-\frac{2T}{n})^{\alpha}dt\right)=O\left(\left(\frac{T}{n}\right)^{3\alpha-1}\right), |  |

where we used the α\alpha-Hölder property of t↦tαt\mapsto t^{\alpha}. Gathering all the terms, we get

|  |  |  |
| --- | --- | --- |
|  | ℰ1,2=ℰ1,2,1+ℰ1,2,2+ℰ1,2,3=O​(𝐯n​(α)).\mathcal{E}\_{1,2}=\mathcal{E}\_{1,2,1}+\mathcal{E}\_{1,2,2}+\mathcal{E}\_{1,2,3}=O({\bf v}\_{n}(\alpha)). |  |

∙\bullet Analysis of ℰ2\mathcal{E}\_{2}. From ([3.2](https://arxiv.org/html/2602.18234v1#S3.E2 "In 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we have ℰ2=ℰ2,1+ℰ2,2\mathcal{E}\_{2}=\mathcal{E}\_{2,1}+\mathcal{E}\_{2,2} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ2,1\displaystyle\mathcal{E}\_{2,1} | =∫0T∫0η​(t)(𝔼​[f​(Xη​(s))​f​f′​(Xη​(t))]−𝔼​[f​(Xˇnη​(s))​f​f′​(Xˇnη​(t))])​𝒟s​Xˇnη​(t)​𝑑s​𝑑t\displaystyle=\int\_{0}^{T}\int\_{0}^{\eta(t)}\left({\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{\eta(t)})]-{\mathbb{E}}[f({\check{X}^{n}}\_{\eta(s)})ff^{\prime}({\check{X}^{n}}\_{\eta(t)})]\right)\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}dsdt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ2,2\displaystyle\mathcal{E}\_{2,2} | =∫0T∫0η​(t)𝔼​[f​(Xη​(s))​f​f′​(Xη​(t))]​(𝒟s​Xη​(t)−𝒟s​Xˇnη​(t))​𝑑s​𝑑t.\displaystyle=\int\_{0}^{T}\int\_{0}^{\eta(t)}{\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{\eta(t)})](\mathcal{D}\_{s}X\_{\eta(t)}-\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)})dsdt. |  |

We first focus on ℰ2,1\mathcal{E}\_{2,1}. We have by using Corollary [A.7](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem7 "Corollary A.7. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ2,1|≤\displaystyle|\mathcal{E}\_{2,1}|\leq | C∫0T∫0η​(t)(|𝔼[Xη​(s)−Xˇnη​(s)]|+|𝔼[Xη​(t)−Xˇnη​(t)]|+|Var(Xη​(s))−Var(Xˇnη​(s))|\displaystyle C\int\_{0}^{T}\int\_{0}^{\eta(t)}\Bigg(|{\mathbb{E}}[X\_{\eta(s)}-{\check{X}^{n}}\_{\eta(s)}]|+|{\mathbb{E}}[X\_{\eta(t)}-{\check{X}^{n}}\_{\eta(t)}]|+|Var(X\_{\eta(s)})-Var({\check{X}^{n}}\_{\eta(s)})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|Var(Xη​(t))−Var(Xˇnη​(t))|+|Cov(Xη​(s),Xη​(t))−Cov(Xˇnη​(s),Xˇnη​(t))|)𝒟sXˇnη​(t)dsdt.\displaystyle+|Var(X\_{\eta(t)})-Var({\check{X}^{n}}\_{\eta(t)})|+|Cov(X\_{\eta(s)},X\_{\eta(t)})-Cov({\check{X}^{n}}\_{\eta(s)},{\check{X}^{n}}\_{\eta(t)})|\Bigg)\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}dsdt. |  |

By using Theorem [2.7](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and using that 𝔼​[Xt0−Xˇnt0]=V​a​r​(Xt0)=V​a​r​(Xˇnt0)=C​o​v​(Xt0,Xtk)=C​o​v​(Xˇnt0,Xˇntk)=0{\mathbb{E}}[X\_{t\_{0}}-{\check{X}^{n}}\_{t\_{0}}]=Var(X\_{t\_{0}})=Var({\check{X}^{n}}\_{t\_{0}})=Cov(X\_{t\_{0}},X\_{t\_{k}})=Cov({\check{X}^{n}}\_{t\_{0}},{\check{X}^{n}}\_{t\_{k}})=0, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ2,1|\displaystyle|\mathcal{E}\_{2,1}| | ≤C​∫t1T∫t1η​(t)((1+η​(s)α−1+η​(t)α−1)​𝐯n​(α)+η​(s)2​α−2+η​(t)2​α−2n)​𝒟s​Xˇnη​(t)​𝑑s​𝑑t\displaystyle\leq C\int\_{t\_{1}}^{T}\int\_{t\_{1}}^{\eta(t)}\Bigg((1+\eta(s)^{\alpha-1}+\eta(t)^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{\eta(s)^{2\alpha-2}+\eta(t)^{2\alpha-2}}{n}\Bigg)\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}dsdt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤C​∫t1T∫t1η​(t)((1+η​(s)α−1)​𝐯n​(α)+η​(s)2​α−2n)​𝒟s​Xˇnη​(t)​𝑑s​𝑑t,\displaystyle\leq C\int\_{t\_{1}}^{T}\int\_{t\_{1}}^{\eta(t)}\Bigg((1+\eta(s)^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{\eta(s)^{2\alpha-2}}{n}\Bigg)\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(t)}dsdt, |  | (3.4) |

since α−1<0\alpha-1<0. By ([2.14](https://arxiv.org/html/2602.18234v1#S2.E14 "In Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get for k>1k>1 and β∈(−1,0]\beta\in(-1,0]

|  |  |  |
| --- | --- | --- |
|  | ∫t1tkη​(s)β​|𝒟s​Xˇntk|​𝑑s≤|κ2|​∑i=1k−1ci,k​∫t1tkη​(s)β​|𝒟s​Xˇnti|​𝑑s+σ​∫t1tkη​(s)β​(tk−s)α−1Γ​(α)​𝑑s\int\_{t\_{1}}^{t\_{k}}\eta(s)^{\beta}|\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}|ds\leq|\kappa\_{2}|\sum\_{i=1}^{k-1}c\_{i,k}\int\_{t\_{1}}^{t\_{k}}\eta(s)^{\beta}|\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{i}}|ds+\sigma\int\_{t\_{1}}^{t\_{k}}\eta(s)^{\beta}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}ds |  |

with ci,k=∫titi+1(tk−u)α−1Γ​(α)​𝑑uc\_{i,k}=\int\_{t\_{i}}^{t\_{i+1}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du. We observe that for s≥t1s\geq t\_{1}, η​(s)≥s/2\eta(s)\geq s/2 and therefore the last integral is upper bounded by

|  |  |  |
| --- | --- | --- |
|  | 2−β​∫0tksβ​(tk−s)α−1Γ​(α)​𝑑s=2−β​Γ​(β+1)Γ​(α+β+1)​tkα+β≤Cα,β​(𝟏α+β≥0​Tα+β+𝟏α+β<0​t1α+β).2^{-\beta}\int\_{0}^{t\_{k}}s^{\beta}\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}ds=2^{-\beta}\frac{\Gamma(\beta+1)}{\Gamma(\alpha+\beta+1)}t\_{k}^{\alpha+\beta}\leq C\_{\alpha,\beta}\left(\mathbf{1}\_{\alpha+\beta\geq 0}T^{\alpha+\beta}+\mathbf{1}\_{\alpha+\beta<0}t\_{1}^{\alpha+\beta}\right). |  |

We now apply the Gronwall type lemma [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.4] to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫t1tkη​(s)β​|𝒟s​Xˇntk|​𝑑s≤C​(𝟏α+β≥0​Tα+β+𝟏α+β<0​t1α+β), 1≤k≤n.\int\_{t\_{1}}^{t\_{k}}\eta(s)^{\beta}|\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}|ds\leq C\left(\mathbf{1}\_{\alpha+\beta\geq 0}T^{\alpha+\beta}+\mathbf{1}\_{\alpha+\beta<0}t\_{1}^{\alpha+\beta}\right),\ 1\leq k\leq n. |  | (3.5) |

We apply this bound in ([3.4](https://arxiv.org/html/2602.18234v1#S3.E4 "In Proof. ‣ 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) with β=0\beta=0, β=α−1\beta=\alpha-1 and β=2​α−2\beta=2\alpha-2 and get

|  |  |  |
| --- | --- | --- |
|  | |ℰ2,1|≤C​T​((C​(Tβ+T2​α−1))​𝐯n​(α)+𝟏α≥2/3​T3​α−2+𝟏α<2/3​t13​α−2n).|\mathcal{E}\_{2,1}|\leq CT\left(\left(C(T^{\beta}+T^{2\alpha-1})\right){\bf v}\_{n}(\alpha)+\frac{\mathbf{1}\_{\alpha\geq 2/3}T^{3\alpha-2}+\mathbf{1}\_{\alpha<2/3}t\_{1}^{3\alpha-2}}{n}\right). |  |

Note that t13​α−2n=T3​α−2n3​α−1≤T3​α−2​𝐯n​(α)\frac{t\_{1}^{3\alpha-2}}{n}=\frac{T^{3\alpha-2}}{n^{3\alpha-1}}\leq T^{3\alpha-2}{\bf v}\_{n}(\alpha), which gives

|  |  |  |
| --- | --- | --- |
|  | |ℰ2,1|≤C​𝐯n​(α).|\mathcal{E}\_{2,1}|\leq C{\bf v}\_{n}(\alpha). |  |

Last, we focus on ℰ2,2\mathcal{E}\_{2,2}.
We have

|  |  |  |
| --- | --- | --- |
|  | ℰ2,2=Tn​∑k=1n−1∫0tk𝔼​[f​(Xη​(s))​f​f′​(Xtk)]​(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s,\mathcal{E}\_{2,2}=\frac{T}{n}\sum\_{k=1}^{n-1}\int\_{0}^{t\_{k}}{\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{t\_{k}})](\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds, |  |

and we focus on each integral. Let ϕ\phi be defined by ([3.3](https://arxiv.org/html/2602.18234v1#S3.E3 "In Proof. ‣ 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). By Corollary [A.5](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem5 "Corollary A.5. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), it is continuously differentiable and we write ϕ​(η​(s),tk)=ϕ​(tk,tk)−∫η​(s)tk∂1ϕ​(u,tk)​d​u\phi(\eta(s),t\_{k})=\phi(t\_{k},t\_{k})-\int\_{\eta(s)}^{t\_{k}}\partial\_{1}\phi(u,t\_{k})du. This gives

|  |  |  |
| --- | --- | --- |
|  | ∫0tk𝔼​[f​(Xη​(s))​f​f′​(Xtk)]​(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s\displaystyle\int\_{0}^{t\_{k}}{\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{t\_{k}})](\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds |  |
|  |  |  |
| --- | --- | --- |
|  | =ϕ​(tk,tk)​∫0tk(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s−∫0tk∫0tk𝟏η​(s)≤u​∂1ϕ​(u,tk)​(𝒟s​Xtk−𝒟s​Xˇntk)​d​s​d​u\displaystyle=\phi(t\_{k},t\_{k})\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds-\int\_{0}^{t\_{k}}\int\_{0}^{t\_{k}}\mathbf{1}\_{\eta(s)\leq u}\partial\_{1}\phi(u,t\_{k})(\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})dsdu |  |
|  |  |  |
| --- | --- | --- |
|  | =ϕ​(tk,tk)​∫0tk(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s−∫0tk∂1ϕ​(u,tk)​(∫0η¯​(u)(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s)​d​u,\displaystyle=\phi(t\_{k},t\_{k})\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds-\int\_{0}^{t\_{k}}\partial\_{1}\phi(u,t\_{k})\left(\int\_{0}^{\bar{\eta}(u)}(\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds\right)du, |  |

by using Fubini theorem.
By using the triangle inequality, ϕ\phi bounded, Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and Corollary [A.5](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem5 "Corollary A.5. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we get

|  |  |  |
| --- | --- | --- |
|  | |∫0tk𝔼​[f​(Xη​(s))​f​f′​(Xtk)]​(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s|\displaystyle\left|\int\_{0}^{t\_{k}}{\mathbb{E}}[f(X\_{\eta(s)})ff^{\prime}(X\_{t\_{k}})](\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​(Tn+∫0tk(u2​α−2+(tk−u)2​α−2)​|∫0η¯​(u)(𝒟s​Xtk−𝒟s​Xˇntk)​𝑑s|​𝑑u)\displaystyle\leq C\left(\frac{T}{n}+\int\_{0}^{t\_{k}}\left(u^{2\alpha-2}+(t\_{k}-u)^{2\alpha-2}\right)\left|\int\_{0}^{\bar{\eta}(u)}(\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})ds\right|du\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​Tn​(1+tk2​α−1)≤C​Tn​(1+T2​α−1),\displaystyle\leq C\frac{T}{n}\left(1+t\_{k}^{2\alpha-1}\right)\leq C\frac{T}{n}\left(1+T^{2\alpha-1}\right), |  |

since 2​α−1>02\alpha-1>0. Therefore, we get |ℰ2,2|≤C​T​(1+T2​α−1)​Tn|\mathcal{E}\_{2,2}|\leq CT(1+T^{2\alpha-1})\frac{T}{n}, which completes the proof.
∎

## 4. Weak error approximation with polynomial test functions

We now state our main result on the weak convergence rate for any polynomial test function. To get this result, we build up on the framework developed in Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] that we extend to our setting. In contrast with the cubic case with b=0b=0 considered in Section [3](https://arxiv.org/html/2602.18234v1#S3 "3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), it is worth noting that the analysis of some terms is more challenging for this general context. In particular the term ℰ2,2\mathcal{E}\_{2,2} requires a much more involved analysis when studied with general polynomial test functions.

###### Theorem 4.1.

Let LL be the process defined by ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) with b,f∈𝒞exp∞​(ℝ,ℝ)b,f\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}).
Let Lˇn\check{L}^{n} denote the approximation scheme ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) with time step T/nT/n with n≥1n\geq 1. Then, for any polynomial function Φ:ℝ→ℝ\Phi:{\mathbb{R}}\to{\mathbb{R}}, there exists C∈ℝ+C\in{\mathbb{R}}\_{+} such that for all nn,

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[Φ​(LˇTn)]−𝔼​[Φ​(LT)]|≤C​𝐯n​(α).\left|{\mathbb{E}}[\Phi(\check{L}^{n}\_{T})]-{\mathbb{E}}[\Phi(L\_{T})]\right|\leq C{\bf v}\_{n}(\alpha). |  |

The proof of this theorem is the goal of Section [4](https://arxiv.org/html/2602.18234v1#S4 "4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). It is split into two main steps. The first one consists in representing the weak error by the mean of a sum of iterated integrals coming from the Malliavin duality formula. This is made in Subsection [4.1](https://arxiv.org/html/2602.18234v1#S4.SS1 "4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). In Subsection [4.2](https://arxiv.org/html/2602.18234v1#S4.SS2 "4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we analyse the weak error itself. Guided by the cubic case, we decompose the error in a similar way and provide the analysis of each term. It turns out that the analysis of some terms is much involved than for the cubic case since we have, due to the combinatorics generated by higher polynomial degrees, more different terms to analyse.

### 4.1. Representation of the weak error

We adopt and extend the framework introduced by Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] to analyse the weak error for polynomial test functions. Without loss of generality as x↦(L0+x)Nx\mapsto(L\_{0}+x)^{N} is still a polynomial function, we assume that L0=0L\_{0}=0 in Section [4](https://arxiv.org/html/2602.18234v1#S4 "4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").
We introduce, for m∈ℕm\in{\mathbb{N}},

|  |  |  |
| --- | --- | --- |
|  | Δm∘:={(r1,…,rm):0<rm<⋯<r1<T},\Delta^{\circ}\_{m}:=\{(r\_{1},\dots,r\_{m}):0<r\_{m}<\dots<r\_{1}<T\}, |  |

the open simplex of order mm.
We recall that b,f∈𝒞exp∞​(ℝ,ℝ)b,f\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}). Let 𝒬m\mathcal{Q}^{m} be the set of functions F:ℝm×Δm∘→ℝF:{\mathbb{R}}^{m}\times\Delta^{\circ}\_{m}\to{\mathbb{R}} such that for any 𝐫=(r1,…,rm)∈Δm∘{\bf r}=(r\_{1},\dots,r\_{m})\in\Delta^{\circ}\_{m}, F​(⋅,𝐫)F(\cdot,{\bf r}) is a smooth function on ℝm{\mathbb{R}}^{m} with derivatives of all orders with exponential growth. For N≥1N\geq 1, we define the three following operators ℐN,𝒥N,𝒦N:𝒬m→𝒬m+1\mathcal{I}^{N},\mathcal{J}^{N},\mathcal{K}^{N}:\mathcal{Q}^{m}\to\mathcal{Q}^{m+1} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℐN​F)​(x1,…,xm,y,r1,…,rm,s)=ρ​N​f​(y)​∑j=1m∂xjF​(x1,…,xm,r1,…,rm)​Ds​Xrj,\displaystyle(\mathcal{I}^{N}F)(x\_{1},\dots,x\_{m},y,r\_{1},\dots,r\_{m},s)=\rho Nf(y)\sum\_{j=1}^{m}\partial\_{x\_{j}}F(x\_{1},\dots,x\_{m},r\_{1},\dots,r\_{m})D\_{s}X\_{r\_{j}}, |  | (4.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒥N​F)​(x1,…,xm,y,r1,…,rm,s)=N​(N−1)2​f2​(y)​F​(x1,…,xm,r1,…,rm)\displaystyle(\mathcal{J}^{N}F)(x\_{1},\dots,x\_{m},y,r\_{1},\dots,r\_{m},s)=\frac{N(N-1)}{2}f^{2}(y)F(x\_{1},\dots,x\_{m},r\_{1},\dots,r\_{m}) |  | (4.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒦N​F)​(x1,…,xm,y,r1,…,rm,s)=N​b​(y)​F​(x1,…,xm,r1,…,rm),\displaystyle(\mathcal{K}^{N}F)(x\_{1},\dots,x\_{m},y,r\_{1},\dots,r\_{m},s)=Nb(y)F(x\_{1},\dots,x\_{m},r\_{1},\dots,r\_{m}), |  | (4.3) |

where 𝐫=(r1,…,rm)∈Δm∘{\bf r}=(r\_{1},\dots,r\_{m})\in\Delta^{\circ}\_{m}, x∈ℝmx\in{\mathbb{R}}^{m}, s∈(0,rm)s\in(0,r\_{m}) and y∈ℝy\in{\mathbb{R}}. Recall that Ds​XrjD\_{s}X\_{r\_{j}} is the (deterministic) Malliavin derivative given by Proposition [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

###### Lemma 4.2.

Let N≥1N\geq 1. Let m≥1m\geq 1, F∈𝒬mF\in\mathcal{Q}^{m}, 𝐫∈Δm∘{\bf r}\in\Delta^{\circ}\_{m}, t∈[0,rm)t\in[0,r\_{m}) and denote 𝐗𝐫=(Xr1,…,Xrm){\bf X}\_{{\bf r}}=(X\_{r\_{1}},\dots,X\_{r\_{m}}). We have, for N≥1N\geq 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Lt)N​F​(𝐗𝐫,𝐫)]=\displaystyle{\mathbb{E}}\left[(L\_{t})^{N}F({\bf X}\_{{\bf r}},{\bf r})\right]= | ∫0t𝔼​[(Ls)N−1​(ℐN​F)​(𝐗𝐫,Xs,𝐫,s)]​𝑑s\displaystyle\int\_{0}^{t}{\mathbb{E}}\left[(L\_{s})^{N-1}(\mathcal{I}^{N}F)({\bf X}\_{{\bf r}},X\_{s},{\bf r},s)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t𝔼​[(Ls)N−1​(𝒦N​F)​(𝐗𝐫,Xs,𝐫,s)]​𝑑s\displaystyle+\int\_{0}^{t}{\mathbb{E}}\left[(L\_{s})^{N-1}(\mathcal{K}^{N}F)({\bf X}\_{{\bf r}},X\_{s},{\bf r},s)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t𝔼​[(Ls)N−2​(𝒥N​F)​(𝐗𝐫,Xs,𝐫,s)]​𝑑s,\displaystyle+\int\_{0}^{t}{\mathbb{E}}\left[(L\_{s})^{N-2}(\mathcal{J}^{N}F)({\bf X}\_{{\bf r}},X\_{s},{\bf r},s)\right]ds, |  |

where the last integral is meant to be 0 for N=1N=1.

###### Proof.

First, we apply Itô formula to get

|  |  |  |
| --- | --- | --- |
|  | LtN=∫0tN​LsN−1​f​(Xs)​𝑑Bs+∫0tN​LsN−1​b​(Xs)+N​(N−1)2​LsN−2​f2​(Xs)​d​s.L\_{t}^{N}=\int\_{0}^{t}NL\_{s}^{N-1}f(X\_{s})dB\_{s}+\int\_{0}^{t}NL\_{s}^{N-1}b(X\_{s})+\frac{N(N-1)}{2}L\_{s}^{N-2}f^{2}(X\_{s})ds. |  |

From the Clark-Ocone formula, we have

|  |  |  |
| --- | --- | --- |
|  | F​(𝐗𝐫,𝐫)=𝔼​[F​(𝐗𝐫,𝐫)]+∑j=1m∫0rj𝔼​[∂xjF​(𝐗𝐫,𝐫)|ℱs]​Ds​Xrj​𝑑Ws,F({\bf X}\_{{\bf r}},{\bf r})={\mathbb{E}}[F({\bf X}\_{{\bf r}},{\bf r})]+\sum\_{j=1}^{m}\int\_{0}^{r\_{j}}{\mathbb{E}}[\partial\_{x\_{j}}F({\bf X}\_{{\bf r}},{\bf r})|\mathcal{F}\_{s}]D\_{s}X\_{r\_{j}}dW\_{s}, |  |

where (ℱs,s≥0)(\mathcal{F}\_{s},s\geq 0) denotes the natural filtration of (B,W)(B,W). This gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0tN​LsN−1​f​(Xs)​𝑑Bs)​F​(𝐗𝐫,𝐫)]\displaystyle{\mathbb{E}}\left[\left(\int\_{0}^{t}NL\_{s}^{N-1}f(X\_{s})dB\_{s}\right)F({\bf X}\_{{\bf r}},{\bf r})\right] | =ρ​∑j=1m∫0tN​𝔼​[(Ls)N−1​f​(Xs)​∂xjF​(𝐗𝐫,𝐫)]​Ds​Xrj​𝑑s\displaystyle=\rho\sum\_{j=1}^{m}\int\_{0}^{t}N{\mathbb{E}}[(L\_{s})^{N-1}f(X\_{s})\partial\_{x\_{j}}F({\bf X}\_{{\bf r}},{\bf r})]D\_{s}X\_{r\_{j}}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t𝔼​[(Ls)N−1​(ℐN​F)​(𝐗𝐫,Xs,𝐫,s)]​𝑑s.\displaystyle=\int\_{0}^{t}{\mathbb{E}}\left[(L\_{s})^{N-1}(\mathcal{I}^{N}F)({\bf X}\_{{\bf r}},X\_{s},{\bf r},s)\right]ds. |  |

The two other terms follow immediately.
∎

Lemma [4.2](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") gives a recursive way to obtain 𝔼​[(Lt)N]{\mathbb{E}}[(L\_{t})^{N}]. We now want to remove this recursion and get an explicit form. To do so, we use the same procedure as Friz et al. [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)]. Let 𝒲\mathcal{W} be the set of all words with letters {I,J,K}\{I,J,K\}. We denote by |⋅||\cdot| the length of a word, i.e. |w|=m|w|=m for w=w1​…​wm∈𝒲w=w\_{1}\dots w\_{m}\in\mathcal{W}. We define also ℓ:𝒲→ℕ\ell:\mathcal{W}\to{\mathbb{N}} by

|  |  |  |
| --- | --- | --- |
|  | ℓ​(w)=∑j=1|w|ℓ​(wj), for ​w=w1​…​wm,\ell(w)=\sum\_{j=1}^{|w|}\ell(w\_{j}),\text{ for }w=w\_{1}\dots w\_{m}, |  |

with ℓ​(I)=ℓ​(K)=1\ell(I)=\ell(K)=1 and ℓ​(J)=2\ell(J)=2. Heuristically, ℓ\ell counts the decrease of the degree of the monomial part of the expectation. To any word w∈𝒲w\in\mathcal{W}, we associate an application ι\iota defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ι​(w)={ι​(w1​…​wm−1)∘ℐℓ​(w) if ​wm=I,ι​(w1​…​wm−1)∘𝒥ℓ​(w) if ​wm=J,ι​(w1​…​wm−1)∘𝒦ℓ​(w) if ​wm=K,\displaystyle\iota(w)=\begin{cases}\iota(w\_{1}\dots w\_{m-1})\circ\mathcal{I}^{\ell(w)}\quad\text{ if }w\_{m}=I,\\ \iota(w\_{1}\dots w\_{m-1})\circ\mathcal{J}^{\ell(w)}\quad\text{ if }w\_{m}=J,\\ \iota(w\_{1}\dots w\_{m-1})\circ\mathcal{K}^{\ell(w)}\quad\text{ if }w\_{m}=K,\\ \end{cases} |  | (4.4) |

where by convention ι​(w1​…​wm−1)\iota(w\_{1}\dots w\_{m-1}) is the identity for m=1m=1 and the operators ℐℓ​(w)\mathcal{I}^{\ell(w)}, 𝒥ℓ​(w)\mathcal{J}^{\ell(w)} and 𝒦ℓ​(w)\mathcal{K}^{\ell(w)} are respectively defined by ([4.1](https://arxiv.org/html/2602.18234v1#S4.E1 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), ([4.2](https://arxiv.org/html/2602.18234v1#S4.E2 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and ([4.3](https://arxiv.org/html/2602.18234v1#S4.E3 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).
Since the operator ℐ\mathcal{I} involves only derivatives, we get that for the constant function 11, ι​(w)​(1)=0\iota(w)(1)=0 for any word ww with last letter II.

###### Theorem 4.3.

We have, for any N≥1N\geq 1,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Lt)N]=∑w∈𝒲,ℓ​(w)=N∫0t…​∫0r|w|−1𝔼​[(ι​(w)​1)​(Xr1,…,Xr|w|,r1,…,r|w|)]​𝑑r|w|​…​𝑑r1.\displaystyle{\mathbb{E}}\left[(L\_{t})^{N}\right]=\sum\_{w\in\mathcal{W},\ell(w)=N}\int\_{0}^{t}\dots\int\_{0}^{r\_{|w|-1}}{\mathbb{E}}\left[(\iota(w)1)(X\_{r\_{1}},\dots,X\_{r\_{|w|}},r\_{1},\dots,r\_{|w|})\right]dr\_{|w|}\dots dr\_{1}. |  |

###### Proof.

We follow [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] and prove the following more general result: for m≥1m\geq 1, 𝐮∈Δm∘{\bf u}\in\Delta^{\circ}\_{m}, t<umt<u\_{m} and F∈𝒬mF\in\mathcal{Q}^{m}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Lt)N​F​(𝐗𝐮,𝐮)]\displaystyle{\mathbb{E}}\left[(L\_{t})^{N}F({\bf X}\_{\bf u},{\bf u})\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑w∈𝒲,ℓ​(w)=N∫0t…​∫0r|w|−1𝔼​[(ι​(w)​F)​(𝐗𝐮,Xr1,…,Xr|w|,𝐮,r1,…,r|w|)]​𝑑r|w|​…​𝑑r1.\displaystyle=\sum\_{w\in\mathcal{W},\ell(w)=N}\int\_{0}^{t}\dots\int\_{0}^{r\_{|w|-1}}{\mathbb{E}}\left[(\iota(w)F)({\bf X}\_{\bf u},X\_{r\_{1}},\dots,X\_{r\_{|w|}},{\bf u},r\_{1},\dots,r\_{|w|})\right]dr\_{|w|}\dots dr\_{1}. |  |

We show this result by induction on NN. For N=1N=1, this is given by Lemma [4.2](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). For N≥2N\geq 2, we apply again Lemma [4.2](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and the induction hypothesis as in the proof of [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Proposition 3.8], using that for w∈𝒲w\in\mathcal{W} such that ℓ​(w)=N\ell(w)=N, either ι​(w)​F=ι​(w1​…​w|w|−1)​ℐN​F\iota(w)F=\iota(w\_{1}\dots w\_{|w|-1})\mathcal{I}^{N}F or ι​(w)​F=ι​(w1​…​w|w|−1)​𝒥N​F\iota(w)F=\iota(w\_{1}\dots w\_{|w|-1})\mathcal{J}^{N}F or ι​(w)​F=ι​(w1​…​w|w|−1)​𝒦N​F\iota(w)F=\iota(w\_{1}\dots w\_{|w|-1})\mathcal{K}^{N}F. We conclude by taking F≡1F\equiv 1.
∎

We now want a similar formula for the approximation scheme ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). For N≥1N\geq 1, we define the following operator ℐˇN:𝒬m→𝒬m+1\check{\mathcal{I}}^{N}:\mathcal{Q}^{m}\to\mathcal{Q}^{m+1} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℐˇN​F)​(x1,…,xm,y,r1,…,rm,s)=ρ​N​f​(y)​∑j=1m∂xjF​(x1,…,xm,r1,…,rm)​Ds​Xˇnη​(rj),\displaystyle(\check{\mathcal{I}}^{N}F)(x\_{1},\dots,x\_{m},y,r\_{1},\dots,r\_{m},s)=\rho Nf(y)\sum\_{j=1}^{m}\partial\_{x\_{j}}F(x\_{1},\dots,x\_{m},r\_{1},\dots,r\_{m})D\_{s}{\check{X}^{n}}\_{\eta(r\_{j})}, |  | (4.5) |

where 𝐫=(r1,…,rm)∈Δm∘{\bf r}=(r\_{1},\dots,r\_{m})\in\Delta^{\circ}\_{m}, x∈ℝmx\in{\mathbb{R}}^{m}, s∈(0,rm)s\in(0,r\_{m}) and y∈ℝy\in{\mathbb{R}}. Recall that Ds​XˇnrjD\_{s}{\check{X}^{n}}\_{r\_{j}} is the (deterministic) Malliavin derivative given by Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). We then define for any word w∈𝒲w\in\mathcal{W} with w=w1​…​wmw=w\_{1}\dots w\_{m} the application

|  |  |  |
| --- | --- | --- |
|  | ιˇ​(w)={ιˇ​(w1​…​wm−1)∘ℐˇℓ​(w) if ​wm=I,ιˇ​(w1​…​wm−1)∘𝒥ℓ​(w) if ​wm=J,ιˇ​(w1​…​wm−1)∘𝒦ℓ​(w) if ​wm=K,\displaystyle\check{\iota}(w)=\begin{cases}\check{\iota}(w\_{1}\dots w\_{m-1})\circ\check{\mathcal{I}}^{\ell(w)}\quad\text{ if }w\_{m}=I,\\ \check{\iota}(w\_{1}\dots w\_{m-1})\circ\mathcal{J}^{\ell(w)}\quad\text{ if }w\_{m}=J,\\ \check{\iota}(w\_{1}\dots w\_{m-1})\circ\mathcal{K}^{\ell(w)}\quad\text{ if }w\_{m}=K,\\ \end{cases} |  |

where again by convention ιˇ​(w1​…​wm−1)\check{\iota}(w\_{1}\dots w\_{m-1}) is the identity for m=1m=1 and the operators ℐˇℓ​(w)\check{\mathcal{I}}^{\ell(w)}, 𝒥ℓ​(w)\mathcal{J}^{\ell(w)} and 𝒦ℓ​(w)\mathcal{K}^{\ell(w)} are respectively defined by ([4.5](https://arxiv.org/html/2602.18234v1#S4.E5 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), ([4.2](https://arxiv.org/html/2602.18234v1#S4.E2 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and ([4.3](https://arxiv.org/html/2602.18234v1#S4.E3 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

###### Theorem 4.4.

We have, for any N≥1N\geq 1,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Lˇnt)N]=∑w∈𝒲,ℓ​(w)=N∫0t…​∫0r|w|−1𝔼​[(ιˇ​(w)​1)​(Xˇη​(r1),…,Xˇη​(r|w|),r1,…,r|w|)]​𝑑r|w|​…​𝑑r1.\displaystyle{\mathbb{E}}\left[({\check{L}^{n}}\_{t})^{N}\right]=\sum\_{w\in\mathcal{W},\ell(w)=N}\int\_{0}^{t}\dots\int\_{0}^{r\_{|w|-1}}{\mathbb{E}}\left[(\check{\iota}(w)1)(\check{X}\_{\eta(r\_{1})},\dots,\check{X}\_{\eta(r\_{|w|})},r\_{1},\dots,r\_{|w|})\right]dr\_{|w|}\dots dr\_{1}. |  |

###### Proof.

The proof is similar to the one of Theorem [4.3](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). More precisely, we first show for N≥1N\geq 1, m≥1m\geq 1, F∈𝒬mF\in\mathcal{Q}^{m}, 𝐫∈Δm∘{\bf r}\in\Delta^{\circ}\_{m}, and t∈[0,rm)t\in[0,r\_{m})

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Lˇnt)N​F​(𝐗ˇ𝐫n,𝐫)]=\displaystyle{\mathbb{E}}\left[({\check{L}^{n}}\_{t})^{N}F(\check{\mathbf{X}}^{n}\_{{\bf r}},{\bf r})\right]= | ∫0t𝔼​[(Lˇns)N−1​(ℐˇN​F)​(𝐗ˇ𝐫n,Xˇnη​(s),𝐫,s)]​𝑑s\displaystyle\int\_{0}^{t}{\mathbb{E}}\left[({\check{L}^{n}}\_{s})^{N-1}(\check{\mathcal{I}}^{N}F)(\check{\mathbf{X}}^{n}\_{{\bf r}},{\check{X}^{n}}\_{\eta(s)},{\bf r},s)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t𝔼​[(Lˇns)N−1​(𝒦N​F)​(𝐗ˇ𝐫n,Xˇnη​(s),𝐫,s)]​𝑑s\displaystyle+\int\_{0}^{t}{\mathbb{E}}\left[({\check{L}^{n}}\_{s})^{N-1}({\mathcal{K}}^{N}F)(\check{\mathbf{X}}^{n}\_{{\bf r}},{\check{X}^{n}}\_{\eta(s)},{\bf r},s)\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t𝔼​[(Lˇns)N−2​(𝒥N​F)​(𝐗ˇ𝐫n,Xˇnη​(s),𝐫,s)]​𝑑s,\displaystyle+\int\_{0}^{t}{\mathbb{E}}\left[({\check{L}^{n}}\_{s})^{N-2}({\mathcal{J}}^{N}F)(\check{\mathbf{X}}^{n}\_{{\bf r}},{\check{X}^{n}}\_{\eta(s)},{\bf r},s)\right]ds, |  |

with 𝐗ˇ𝐫n=(Xˇnr1,…,Xˇnrm)\check{\mathbf{X}}^{n}\_{{\bf r}}=({\check{X}^{n}}\_{r\_{1}},\dots,{\check{X}^{n}}\_{r\_{m}}), as in Lemma [4.2](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). We then conclude by induction. ∎

Theorems [4.3](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and [4.4](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") give the moments explicitly by means of the the functions ι​(w)​1\iota(w)1 and ιˇ​(w)​1\check{\iota}(w)1. However, these functions are defined by induction, and the goal of the next proposition is to get rid of it.

###### Proposition 4.5.

(Calculation of ι​(w)\iota(w) defined by ([4.4](https://arxiv.org/html/2602.18234v1#S4.E4 "In 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).)
Let q≥0q\geq 0, ψ1,…,ψq∈𝒞exp∞​(ℝ,ℝ)\psi\_{1},\dots,\psi\_{q}\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}) and F∈𝒬qF\in\mathcal{Q}^{q} such that F​(x1,…,xq,r1,…,rq)=∏i=1qψi​(xi)F(x\_{1},\dots,x\_{q},r\_{1},\dots,r\_{q})=\prod\_{i=1}^{q}\psi\_{i}(x\_{i}) (convention F≡1F\equiv 1 if q=0q=0). Let w∈𝒲w\in\mathcal{W} with w=w1​…​wmw=w\_{1}\dots w\_{m} and m=|w|≥1m=|w|\geq 1. We define NIw={j:wj=I}N\_{I}^{w}=\{j:w\_{j}=I\}, NJw={j:wj=J}N\_{J}^{w}=\{j:w\_{j}=J\} and NKw={j:wj=K}N\_{K}^{w}=\{j:w\_{j}=K\}.

* •

  If NIw=∅N\_{I}^{w}=\emptyset (i.e w∈𝒲w\in\mathcal{W} does not contain the letter II), then we have

  |  |  |  |
  | --- | --- | --- |
  |  | (ι​(w)​F)​(x1,…,xq+m,r1,…,rq+m)=Cw​∏i=1qψi​(xi)​∏l∈NJwf2​(xm+q−l+1)​∏l∈NKwb​(xm+q−l+1).(\iota(w)F)(x\_{1},\dots,x\_{q+m},r\_{1},\dots,r\_{q+m})=C\_{w}\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\prod\_{l\in N^{w}\_{J}}f^{2}(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{K}}b(x\_{m+q-l+1}). |  |
* •

  Otherwise, let k=#​NIw≤mk=\#N\_{I}^{w}\leq m and 1≤j1<⋯<jk≤m1\leq j\_{1}<\dots<j\_{k}\leq m such that NIw={j1,…,jk}N\_{I}^{w}=\{j\_{1},\dots,j\_{k}\}. Then, we have

  |  |  |  |
  | --- | --- | --- |
  |  | (ι​(w)​F)​(x1,…,xq,…,xq+m,r1,…,rq,…,rq+m)\displaystyle(\iota(w)F)(x\_{1},\dots,x\_{q},\dots,x\_{q+m},r\_{1},\dots,r\_{q},\dots,r\_{q+m}) |  |
  |  |  |  |
  | --- | --- | --- |
  |  | =Cw​∑l1=1m+q−j1…​∑lk=1m+q−jk𝒟rm+q−j1+1​Xrl1​…​𝒟rm+q−jk+1​Xrlk\displaystyle=C\_{w}\sum\_{l\_{1}=1}^{m+q-j\_{1}}\dots\sum\_{l\_{k}=1}^{m+q-j\_{k}}\mathcal{D}\_{r\_{m+q-j\_{1}+1}}X\_{r\_{l\_{1}}}\dots\mathcal{D}\_{r\_{m+q-j\_{k}+1}}X\_{r\_{l\_{k}}} |  |
  |  |  |  |
  | --- | --- | --- |
  |  | ×∂xl1…∂xlk(∏i=1qψi(xi)∏l∈NJwf2(xm+q−l+1)∏l∈NKwb(xm+q−l+1)∏l∈NIwf(xm+q−l+1)),\displaystyle\times\partial\_{x\_{l\_{1}}}\dots\partial\_{x\_{l\_{k}}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\prod\_{l\in N^{w}\_{J}}f^{2}(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{K}}b(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{I}}f(x\_{m+q-l+1})\right), |  |

with Cw=2−#​NJw​ρ#​NIw×ℓ​(w)!C\_{w}=2^{-\#N\_{J}^{w}}\rho^{\#N\_{I}^{w}}\times\ell(w)!.

The same formulas hold for ιˇ​(w)​F\check{\iota}(w)F, with 𝒟rm+q−jν+1​Xˇnη​(rlν)\mathcal{D}\_{r\_{m+q-j\_{\nu}+1}}{\check{X}^{n}}\_{\eta(r\_{l\_{\nu}})} instead of 𝒟rm+q−jν+1​Xrlν\mathcal{D}\_{r\_{m+q-j\_{\nu}+1}}X\_{r\_{l\_{\nu}}} for ν∈{1,…,k}\nu\in\{1,\dots,k\}.

###### Remark 4.6.

This proposition slightly extends (in our framework) [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Proposition 3.13] that calculates ι​(w)​1\iota(w)1. Here, we use a different induction argument that allows to better keep track of the constant CwC\_{w}.

###### Remark 4.7.

Proposition [4.5](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") gives ι​(w)​1\iota(w)1 simply by taking formally q=0q=0 in the above formula. This is clear when ww has a single letter (i.e. |w|=1|w|=1). We indeed have ι​(I)​1=0\iota(I)1=0, (ι​(J)​1)​(x,r)=f2​(x)(\iota(J)1)(x,r)=f^{2}(x) and (ι​(K)​1)​(x,r)=b​(x)(\iota(K)1)(x,r)=b(x). For |w|≥2|w|\geq 2, we just use the induction w=w′​wmw=w^{\prime}w\_{m} with wm∈{I,J,K}w\_{m}\in\{I,J,K\} and apply Proposition [4.5](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for w′w^{\prime}, q=1q=1 and F​(x,r)=(ι​(K)​1)​(wm,r)∈𝒬1F(x,r)=(\iota(K)1)(w\_{m},r)\in\mathcal{Q}^{1}.

###### Proof.

We prove this result by induction on the length |w|=m|w|=m. For m=1m=1, if w=Jw=J (resp. w=Kw=K) then NJw={1}N\_{J}^{w}=\{1\} (resp. NKw={1}N\_{K}^{w}=\{1\}) so that

|  |  |  |
| --- | --- | --- |
|  | (ι​(J)​F)​(x1,…,xq+1,r1,…,rq+1)=f2​(xq+1)​∏i=1qψi​(xi)(\iota(J)F)(x\_{1},\dots,x\_{q+1},r\_{1},\dots,r\_{q+1})=f^{2}(x\_{q+1})\prod\_{i=1}^{q}\psi\_{i}(x\_{i}) |  |

(resp. (ι​(K)​F)​(x1,…,xq+1,r1,…,rq+1)=b​(xq+1)​∏i=1qψi​(xi)(\iota(K)F)(x\_{1},\dots,x\_{q+1},r\_{1},\dots,r\_{q+1})=b(x\_{q+1})\prod\_{i=1}^{q}\psi\_{i}(x\_{i})). If w=Iw=I, we have j1=1j\_{1}=1 and

|  |  |  |
| --- | --- | --- |
|  | (ι​(I)​F)​(x1,…,xq+1,r1,…,rq+1)=ρ​f​(xq+1)​∑l=1q∂xl(∏i=1qψi​(xi))​𝒟rq+1​Xrl.(\iota(I)F)(x\_{1},\dots,x\_{q+1},r\_{1},\dots,r\_{q+1})=\rho f(x\_{q+1})\sum\_{l=1}^{q}\partial\_{x\_{l}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\right)\mathcal{D}\_{r\_{q+1}}X\_{r\_{l}}. |  |

We now prove the induction step and consider m≥2m\geq 2. We write w=w′​wmw=w^{\prime}w\_{m}, where w′∈𝒲w^{\prime}\in\mathcal{W} with |w′|=m−1|w^{\prime}|=m-1. Let us first consider the case w=w′​Jw=w^{\prime}J so that ι​(w)=ι​(w′)∘𝒥ℓ​(w)\iota(w)=\iota(w^{\prime})\circ\mathcal{J}^{\ell(w)}. We have

|  |  |  |
| --- | --- | --- |
|  | 𝒥ℓ​(w)​F​(x1,…,xq+1,r1,…,rq+1)=ℓ​(w)​(ℓ​(w)−1)2​f2​(xq+1)​∏i=1qψi​(xi),\mathcal{J}^{\ell(w)}F(x\_{1},\dots,x\_{q+1},r\_{1},\dots,r\_{q+1})=\frac{\ell(w)(\ell(w)-1)}{2}f^{2}(x\_{q+1})\prod\_{i=1}^{q}\psi\_{i}(x\_{i}), |  |

and we apply the induction hypothesis to this function. If w′w^{\prime} does not contain the letter II, we get

|  |  |  |
| --- | --- | --- |
|  | (ι​(w′)​𝒥ℓ​(w)​F)​(x1,…,xq+m,r1,…,rq+m)\displaystyle(\iota(w^{\prime})\mathcal{J}^{\ell(w)}F)(x\_{1},\dots,x\_{q+m},r\_{1},\dots,r\_{q+m}) |  |
|  |  |  |
| --- | --- | --- |
|  | =Cw′​ℓ​(w)​(ℓ​(w)−1)2​f2​(xq+1)​∏i=1qψi​(xi)​∏l∈NJw′f2​(xm+q−l+1)​∏l∈NKw′b​(xm+q−l+1)\displaystyle=C\_{w^{\prime}}\frac{\ell(w)(\ell(w)-1)}{2}f^{2}(x\_{q+1})\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\prod\_{l\in N^{w^{\prime}}\_{J}}f^{2}(x\_{m+q-l+1})\prod\_{l\in N^{w^{\prime}}\_{K}}b(x\_{m+q-l+1}) |  |
|  |  |  |
| --- | --- | --- |
|  | =Cw​∏i=1qψi​(xi)​∏l∈NJwf2​(xm−q−l+1)​∏l∈NKwb​(xm+q−l+1),\displaystyle=C\_{w}\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\prod\_{l\in N^{w}\_{J}}f^{2}(x\_{m-q-l+1})\prod\_{l\in N^{w}\_{K}}b(x\_{m+q-l+1}), |  |

with Cw=ℓ​(w)​(ℓ​(w)−1)2​Cw′C\_{w}=\frac{\ell(w)(\ell(w)-1)}{2}C\_{w^{\prime}} since NJw=NJw′∪{m}N^{w}\_{J}=N^{w^{\prime}}\_{J}\cup{\{m\}} and NKw=NKw′N^{w}\_{K}=N^{w^{\prime}}\_{K}. If w′w^{\prime} contains the letter II, we get

|  |  |  |
| --- | --- | --- |
|  | (ι​(w′)​𝒥ℓ​(w)​F)​(x1,…,xq+m,r1,…,rq+m)=Cw′​ℓ​(w)​(ℓ​(w)−1)2\displaystyle(\iota(w^{\prime})\mathcal{J}^{\ell(w)}F)(x\_{1},\dots,x\_{q+m},r\_{1},\dots,r\_{q+m})=C\_{w^{\prime}}\frac{\ell(w)(\ell(w)-1)}{2} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∑l1=1m+q−j1′…∑lk=1m+q−jk′𝒟rm+q−j1′+1Xrl1…𝒟rm+q−jk′+1Xrlk\displaystyle\times\sum\_{l\_{1}=1}^{m+q-j^{\prime}\_{1}}\dots\sum\_{l\_{k}=1}^{m+q-j^{\prime}\_{k}}\mathcal{D}\_{r\_{m+q-j^{\prime}\_{1}+1}}X\_{r\_{l\_{1}}}\dots\mathcal{D}\_{r\_{m+q-j^{\prime}\_{k}+1}}X\_{r\_{l\_{k}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∂xl1…∂xlk(∏i=1qψi(xi)f2(xq+1)∏l∈NJw′f2(xm+q−l+1)∏l∈NKw′b(xm+q−l+1)∏l∈NIw′f(xm+q−l+1))\displaystyle\times\partial\_{x\_{l\_{1}}}\dots\partial\_{x\_{l\_{k}}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})f^{2}(x\_{q+1})\prod\_{l\in N^{w^{\prime}}\_{J}}f^{2}(x\_{m+q-l+1})\prod\_{l\in N^{w^{\prime}}\_{K}}b(x\_{m+q-l+1})\prod\_{l\in N^{w^{\prime}}\_{I}}f(x\_{m+q-l+1})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =Cw​∑l1=1m+q−j1…​∑lk=1m+q−jk𝒟rm+q−j1+1​Xrl1​…​𝒟rm+q−jk+1​Xrlk\displaystyle=C\_{w}\sum\_{l\_{1}=1}^{m+q-j\_{1}}\dots\sum\_{l\_{k}=1}^{m+q-j\_{k}}\mathcal{D}\_{r\_{m+q-j\_{1}+1}}X\_{r\_{l\_{1}}}\dots\mathcal{D}\_{r\_{m+q-j\_{k}+1}}X\_{r\_{l\_{k}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∂xl1…∂xlk(∏i=1qψi(xi)∏l∈NJwf2(xm+q−l+1)∏l∈NKwb(xm+q−l+1)∏l∈NIwf(xm+q−l+1)),\displaystyle\times\partial\_{x\_{l\_{1}}}\dots\partial\_{x\_{l\_{k}}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\prod\_{l\in N^{w}\_{J}}f^{2}(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{K}}b(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{I}}f(x\_{m+q-l+1})\right), |  |

with Cw=ℓ​(w)​(ℓ​(w)−1)2​Cw′C\_{w}=\frac{\ell(w)(\ell(w)-1)}{2}C\_{w^{\prime}}, using again NJw=NJw′∪{m}N^{w}\_{J}=N^{w^{\prime}}\_{J}\cup{\{m\}}, NKw=NKw′N^{w}\_{K}=N^{w^{\prime}}\_{K}, NIw=NIw′N^{w}\_{I}=N^{w^{\prime}}\_{I} which amounts to have j1′=j1,…,jk′=jkj^{\prime}\_{1}=j\_{1},\dots,j^{\prime}\_{k}=j\_{k}.

The proof is similar if w=w′​Kw=w^{\prime}K with Cw=Cw′​ℓ​(w)C\_{w}=C\_{w^{\prime}}\ell(w). For w=w′​Iw=w^{\prime}I, we have

|  |  |  |
| --- | --- | --- |
|  | ℐℓ​(w)​F​(x1,…,xq+1,r1,…,rq+1)=ρ​ℓ​(w)​f​(xq+1)​∑l=1q∂xl(∏i=1qψi​(xi))​𝒟rq+1​Xrl.\mathcal{I}^{\ell(w)}F(x\_{1},\dots,x\_{q+1},r\_{1},\dots,r\_{q+1})=\rho\ell(w)f(x\_{q+1})\sum\_{l=1}^{q}\partial\_{x\_{l}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\right)\mathcal{D}\_{r\_{q+1}}X\_{r\_{l}}. |  |

Using the linearity of the operator ι​(w′)\iota(w^{\prime}) and the fact that ∂xl(∏i=1qψi​(xi))=ψl′​(xl)​∏i≠lψi​(xi)\partial\_{x\_{l}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\right)=\psi\_{l}^{\prime}(x\_{l})\prod\_{i\not=l}\psi\_{i}(x\_{i}) is a product of smooth functions, we get by induction (in the case where w′w^{\prime} contains the letter II, the other case can be analysed in the same way applying the first assertion of Proposition [4.5](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))

|  |  |  |
| --- | --- | --- |
|  | (ι(w′)ℐℓ​(w)F)(x1,…,xq+m,r1,…,rq+m)=ρCw′ℓ(w)×∑l=1q∑l1=1m+q−j1′…∑lk=1m+q−jk′{\displaystyle(\iota(w^{\prime})\mathcal{I}^{\ell(w)}F)(x\_{1},\dots,x\_{q+m},r\_{1},\dots,r\_{q+m})=\rho C\_{w^{\prime}}\ell(w)\times\sum\_{l=1}^{q}\sum\_{l\_{1}=1}^{m+q-j^{\prime}\_{1}}\dots\sum\_{l\_{k}=1}^{m+q-j^{\prime}\_{k}}\bigg\{ |  |
|  |  |  |
| --- | --- | --- |
|  | ∂xl1…​∂xlk(∂xl(∏i=1qψi​(xi)​f​(xq+1))​∏l¯∈NJw′f2​(xm+q−l¯+1)​∏l¯∈NKw′b​(xm+q−l¯+1)​∏l¯∈NIw′f​(xm+q−l¯+1))\displaystyle\partial\_{x\_{l\_{1}}}\dots\partial\_{x\_{l\_{k}}}\left(\partial\_{x\_{l}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})f(x\_{q+1})\right)\prod\_{\bar{l}\in N^{w^{\prime}}\_{J}}f^{2}(x\_{m+q-\bar{l}+1})\prod\_{\bar{l}\in N^{w^{\prime}}\_{K}}b(x\_{m+q-\bar{l}+1})\prod\_{\bar{l}\in N^{w^{\prime}}\_{I}}f(x\_{m+q-\bar{l}+1})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ×𝒟rm+q−j1′+1Xrl1…𝒟rm+q−jk′+1Xrlk×Drq+1Xrl},\displaystyle\times\mathcal{D}\_{r\_{m+q-j^{\prime}\_{1}+1}}X\_{r\_{l\_{1}}}\dots\mathcal{D}\_{r\_{m+q-j^{\prime}\_{k}+1}}X\_{r\_{l\_{k}}}\times D\_{r\_{q+1}}X\_{r\_{l}}\bigg\}, |  |

where k=#​NIw′k=\#N\_{I}^{w^{\prime}} and NIw′={j1′,…,jk′}N\_{I}^{w^{\prime}}=\{j^{\prime}\_{1},\dots,j^{\prime}\_{k}\}.
We notice that j1′=j1,…,jk′=jkj^{\prime}\_{1}=j\_{1},\dots,j^{\prime}\_{k}=j\_{k} and jk+1=mj\_{k+1}=m so that m+q−jk+1+1=q+1m+q-j\_{k+1}+1=q+1. Besides, m+q−l¯+1≥q+2m+q-\bar{l}+1\geq q+2 since l¯≤m−1\bar{l}\leq m-1, so that we can put the product of functions inside the derivation with respect to xlx\_{l}, for l≤ql\leq q. Since NIw=NIw′∪{m}N\_{I}^{w}=N\_{I}^{w^{\prime}}\cup\{m\}, NJw=NJw′N\_{J}^{w}=N\_{J}^{w^{\prime}} and NKw=NKw′N\_{K}^{w}=N\_{K}^{w^{\prime}}, this gives

|  |  |  |
| --- | --- | --- |
|  | (ι​(w′)​ℐℓ​(w)​F)​(x1,…,xq+m,r1,…,rq+m)=\displaystyle(\iota(w^{\prime})\mathcal{I}^{\ell(w)}F)(x\_{1},\dots,x\_{q+m},r\_{1},\dots,r\_{q+m})= |  |
|  |  |  |
| --- | --- | --- |
|  | =Cw​∑l1=1m+q−j1′…​∑lk+1=1m+q−jk+1𝒟rm+q−j1′+1​Xrl1​…​𝒟rm+q−jk+1+1​Xrlk+1\displaystyle=C\_{w}\sum\_{l\_{1}=1}^{m+q-j^{\prime}\_{1}}\dots\sum\_{l\_{k+1}=1}^{m+q-j\_{k+1}}\mathcal{D}\_{r\_{m+q-j^{\prime}\_{1}+1}}X\_{r\_{l\_{1}}}\dots\mathcal{D}\_{r\_{m+q-j\_{k+1}+1}}X\_{r\_{l\_{k+1}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∂xl1…∂xlk+1(∏i=1qψi(xi)∏l∈NJwf2(xm+q−l+1)∏l∈NKwb(xm+q−l+1)∏l∈NIwf(xm+q−l+1)),\displaystyle\times\partial\_{x\_{l\_{1}}}\dots\partial\_{x\_{l\_{k+1}}}\left(\prod\_{i=1}^{q}\psi\_{i}(x\_{i})\prod\_{l\in N^{w}\_{J}}f^{2}(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{K}}b(x\_{m+q-l+1})\prod\_{l\in N^{w}\_{I}}f(x\_{m+q-l+1})\right), |  |

with Cw=ρ​Cw′​ℓ​(w)C\_{w}=\rho C\_{w^{\prime}}\ell(w).
∎

### 4.2. Weak error analysis

We are now in position to analyse the error

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(LT)N]−𝔼​[(LˇnT)N]\displaystyle{\mathbb{E}}[(L\_{T})^{N}]-{\mathbb{E}}[({\check{L}^{n}}\_{T})^{N}] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑w∈𝒲,ℓ​(w)=N∫0T…∫0r|w|−1𝔼[(ι(w)1)(Xr1,…,Xr|w|,r1,…,r|w|)\displaystyle=\sum\_{w\in\mathcal{W},\ell(w)=N}\int\_{0}^{T}\dots\int\_{0}^{r\_{|w|-1}}{\mathbb{E}}\bigg[(\iota(w)1)(X\_{r\_{1}},\dots,X\_{r\_{|w|}},r\_{1},\dots,r\_{|w|}) |  |
|  |  |  |
| --- | --- | --- |
|  | −(ιˇ(w)1)(Xˇnη​(r1),…,Xˇnη​(r|w|),r1,…,r|w|)]dr|w|…dr1.\displaystyle\quad\quad-(\check{\iota}(w)1)({\check{X}^{n}}\_{\eta(r\_{1})},\dots,{\check{X}^{n}}\_{\eta(r\_{|w|})},r\_{1},\dots,r\_{|w|})\bigg]dr\_{|w|}\dots dr\_{1}. |  |

By Proposition [4.5](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and Remark [4.7](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem7 "Remark 4.7. ‣ 4.1. Representation of the weak error ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), the expectation can be written as a finite sum of the following terms

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Ψl1,…,lkw​(Xr1,…,Xrm)]​∏ν=1k𝒟rm−jν+1​Xrlν\displaystyle{\mathbb{E}}\left[\Psi^{w}\_{l\_{1},\dots,l\_{k}}(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{r\_{l\_{\nu}}} |  |
|  |  |  |
| --- | --- | --- |
|  | −𝔼​[Ψl1,…,lkw​(Xˇnη​(r1),…,Xˇnη​(rm))]​∏ν=1k𝒟rm−jν+1​Xˇnη​(rlν),\displaystyle-{\mathbb{E}}\left[\Psi^{w}\_{l\_{1},\dots,l\_{k}}({\check{X}^{n}}\_{\eta(r\_{1})},\dots,{\check{X}^{n}}\_{\eta(r\_{m})})\right]\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}{\check{X}^{n}}\_{\eta(r\_{l\_{\nu}})}, |  |

with m=|w|m=|w|, k=#​NIwk=\#N\_{I}^{w}, {j1,…,jk}=NIw\{j\_{1},\dots,j\_{k}\}=N\_{I}^{w} and Ψl1,…,lkw:ℝm→ℝm\Psi^{w}\_{l\_{1},\dots,l\_{k}}:{\mathbb{R}}^{m}\to{\mathbb{R}}^{m} is a product of mm functions i.e. Ψl1,…,lkw​(x1,…,xm)=∏m′=1mgm′​(xm′)\Psi^{w}\_{l\_{1},\dots,l\_{k}}(x\_{1},\dots,x\_{m})=\prod\_{m^{\prime}=1}^{m}g\_{m^{\prime}}(x\_{m^{\prime}}) with g1,…,gm∈𝒞exp∞​(ℝ,ℝ)g\_{1},\dots,g\_{m}\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}), see Equation ([2.9](https://arxiv.org/html/2602.18234v1#S2.E9 "In 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). Note that every word ww finishing by the letter II gives ι​(w)​1=0\iota(w)1=0. Thus, we may assume in what follows that jk<mj\_{k}<m and k<mk<m.

In the following, we drop the superscript and subscript of Ψ\Psi to have a simpler notation, and we analyse the error term

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ=∫0T…​∫0rm−1\displaystyle\mathcal{E}=\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}} | 𝔼​[Ψ​(Xr1,…,Xrm)]​∏ν=1k𝒟rm−jν+1​Xrlν\displaystyle{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{r\_{l\_{\nu}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​[Ψ​(Xˇnη​(r1),…,Xˇnη​(rm))]​∏ν=1k𝒟rm−jν+1​Xˇnη​(rlν)​d​rm​…​d​r1,\displaystyle-{\mathbb{E}}\left[\Psi({\check{X}^{n}}\_{\eta(r\_{1})},\dots,{\check{X}^{n}}\_{\eta(r\_{m})})\right]\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}{\check{X}^{n}}\_{\eta(r\_{l\_{\nu}})}\ dr\_{m}\dots dr\_{1}, |  |

when Ψ​(x1,…,xm)=∏i=1mgi​(xi)\Psi(x\_{1},\dots,x\_{m})=\prod\_{i=1}^{m}g\_{i}(x\_{i}) for some functions g1,…,gm∈𝒞exp∞​(ℝ,ℝ)g\_{1},\dots,g\_{m}\in\mathcal{C}\_{\exp}^{\infty}({\mathbb{R}},{\mathbb{R}}). In particular, Ψ\Psi satisfies

|  |  |  |
| --- | --- | --- |
|  | ∀k1,…,km∈ℕ,∃C∈ℝ+​∀x∈ℝm,|∂1k1…​∂mkmΨ​(x)|≤C​eC​∑i=1m|xi|.\forall k\_{1},\dots,k\_{m}\in{\mathbb{N}},\exists C\in{\mathbb{R}}\_{+}\forall x\in{\mathbb{R}}^{m},\ |\partial\_{1}^{k\_{1}}\dots\partial\_{m}^{k\_{m}}\Psi(x)|\leq Ce^{C\sum\_{i=1}^{m}|x\_{i}|}. |  |

As in Section [3](https://arxiv.org/html/2602.18234v1#S3 "3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for the cubic case, we split ℰ\mathcal{E} as follows

|  |  |  |
| --- | --- | --- |
|  | ℰ=ℰ1,1+ℰ1,2+ℰ2,1+ℰ2,2,\mathcal{E}=\mathcal{E}\_{1,1}+\mathcal{E}\_{1,2}+\mathcal{E}\_{2,1}+\mathcal{E}\_{2,2}, |  |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,1\displaystyle\mathcal{E}\_{1,1} | =∫0T…​∫0rm−1𝔼​[Ψ​(Xr1,…,Xrm)]​(∏ν=1k𝒟rm−jν+1​Xrlν−∏ν=1k𝒟rm−jν+1​Xη​(rlν))​𝑑rm​…​𝑑r1,\displaystyle=\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\left(\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{r\_{l\_{\nu}}}-\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{\eta(r\_{l\_{\nu}})}\right)dr\_{m}\dots dr\_{1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,2\displaystyle\mathcal{E}\_{1,2} | =∫0T…​∫0rm−1𝔼​[Ψ​(Xr1,…,Xrm)−Ψ​(Xη​(r1),…,Xη​(rm))]​∏ν=1k𝒟rm−jν+1​Xη​(rlν)​d​rm​…​d​r1,\displaystyle=\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})-\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})\right]\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{\eta(r\_{l\_{\nu}})}dr\_{m}\dots dr\_{1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ2,1\displaystyle\mathcal{E}\_{2,1} | =∫0T…​∫0rm−1𝔼​[Ψ​(Xη​(r1),…,Xη​(rm))−Ψ​(Xˇnη​(r1),…,Xˇnη​(rm))]​∏ν=1k𝒟rm−jν+1​Xˇnη​(rlν)​d​rm​…​d​r1,\displaystyle=\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})-\Psi({\check{X}^{n}}\_{\eta(r\_{1})},\dots,{\check{X}^{n}}\_{\eta(r\_{m})})\right]\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}{\check{X}^{n}}\_{\eta(r\_{l\_{\nu}})}dr\_{m}\dots dr\_{1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ2,2\displaystyle\mathcal{E}\_{2,2} | =∫0T…​∫0rm−1𝔼​[Ψ​(Xη​(r1),…,Xη​(rm))]​(∏ν=1k𝒟rm−jν+1​Xη​(rlν)−∏ν=1k𝒟rm−jν+1​Xˇnη​(rlν))​𝑑rm​…​𝑑r1.\displaystyle=\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})\right]\left(\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{\eta(r\_{l\_{\nu}})}-\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}{\check{X}^{n}}\_{\eta(r\_{l\_{\nu}})}\right)dr\_{m}\dots dr\_{1}. |  |

The two first terms do not involve the discretization process Xˇn{\check{X}^{n}} and are essentially already analysed in [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)]. Namely, ℰ1,2\mathcal{E}\_{1,2} corresponds to [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (25)] and ℰ1,1\mathcal{E}\_{1,1} corresponds to a sum of terms [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (26)], with the Malliavin derivatives replacing the kernels111Note that one should of course either read in [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (26)] W^𝐭\widehat{W}\_{\bf t} instead of W^η​(𝐭)\widehat{W}\_{\eta(\bf t)} or in [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (25)] KK instead of K~\tilde{K}, so that the sum of [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (25) and (26)] gives the weak error [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (24)].. Thus, we will be brief on the analysis of these two terms and rather focus on the two other terms which are specific to our new setting and arise from the discretization of the dynamics of the rough process XX. For that purpose, we provide additional technical analysis, see in particular Proposition [4.8](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

#### 4.2.1. Analysis of ℰ1,1\mathcal{E}\_{1,1} and ℰ1,2\mathcal{E}\_{1,2}

Following [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)], we rewrite

|  |  |  |
| --- | --- | --- |
|  | ∏ν=1k𝒟rm−jν+1​Xrlν=∏i=2m𝒟ri​Xrα​(i),\prod\_{\nu=1}^{k}\mathcal{D}\_{r\_{m-j\_{\nu}+1}}X\_{r\_{l\_{\nu}}}=\prod\_{i=2}^{m}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}, |  |

with α:{1,…​m}→ℕ\alpha:\{1,\dots m\}\to\mathbb{N} such that α​(i)=lν\alpha(i)=l\_{\nu} if i=m−jν+1i=m-j\_{\nu}+1 for some ν∈{1,…,k}\nu\in\{1,\dots,k\}, and α​(i)=0\alpha(i)=0 otherwise. We use as in [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)] the convention that 𝒟ri​Xrα​(i)=1\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}=1 if α​(i)=0\alpha(i)=0. Note that α​(i)<i\alpha(i)<i, so that ri<rα​(i)r\_{i}<r\_{\alpha(i)}. Note also that α​(1)=0\alpha(1)=0 since jk<mj\_{k}<m (we recall that words ww finishing by the letter II give ι​(w)​I=0\iota(w)I=0, and that j1,…,jkj\_{1},\dots,j\_{k} are the positions of the letter II in the word ww), which explains why the above product starts from 22. This new expression is used to have all the indices i∈{1,…,m}i\in\{1,\dots,m\} which makes the following error decomposition clearer. Namely, using that ∏i=2mai−∏i=2mbi=∑j=2m(∏i<jai)​(aj−bj)​(∏i>jbi)\prod\_{i=2}^{m}a\_{i}-\prod\_{i=2}^{m}b\_{i}=\sum\_{j=2}^{m}(\prod\_{i<j}a\_{i})(a\_{j}-b\_{j})(\prod\_{i>j}b\_{i}), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ1,1=\displaystyle\mathcal{E}\_{1,1}= | ∑j=2m∫0T…​∫0rm−1𝔼​[Ψ​(Xr1,…,Xrm)]​∏i<j𝒟ri​Xrα​(i)\displaystyle\sum\_{j=2}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\prod\_{i<j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(𝒟rj​Xrα​(j)−𝒟rj​Xη​(rα​(j)))​∏i>j𝒟ri​Xη​(rα​(i))​d​rm​…​d​r1\displaystyle\times\left(\mathcal{D}\_{r\_{j}}X\_{r\_{\alpha(j)}}-\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}\right)\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}dr\_{m}\dots dr\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =:\displaystyle=: | ∑j=2mℰ1,1,j.\displaystyle\sum\_{j=2}^{m}\mathcal{E}\_{1,1,j}. |  |

The term ℰ1,1,j\mathcal{E}\_{1,1,j} corresponds in our framework to [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Equation (26)], with the Malliavin derivatives replacing the kernels.
From ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), the Malliavin derivative is a series whose the first term is precisely the fractional kernel considered in [[10](https://arxiv.org/html/2602.18234v1#bib.bib10)]. Following their analysis (namely [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Lemmas 4.4 and 4.7]) by distinguishing the first term in ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and the other ones as in the analysis of ℰ1,1\mathcal{E}\_{1,1} in Section [3](https://arxiv.org/html/2602.18234v1#S3 "3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we get that |ℰ1,1,j|≤C​𝐯n​(α)|\mathcal{E}\_{1,1,j}|\leq C{\bf v}\_{n}(\alpha) and then |ℰ1,1|≤C​𝐯n​(α)|\mathcal{E}\_{1,1}|\leq C{\bf v}\_{n}(\alpha).
In the same way, adapting [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Lemma 4.3] to our framework allows to get |ℰ1,2|≤C​𝐯n​(α)|\mathcal{E}\_{1,2}|\leq C{\bf v}\_{n}(\alpha).

#### 4.2.2. Analysis of ℰ2,1\mathcal{E}\_{2,1}

We use the same notation as for ℰ1,1\mathcal{E}\_{1,1} and write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ2,1\displaystyle\mathcal{E}\_{2,1} | =∫0T…​∫0rm−1𝔼​[Ψ​(Xη​(r1),…,Xη​(rm))−Ψ​(Xˇnη​(r1),…,Xˇnη​(rm))]​∏i=2m𝒟ri​Xˇnη​(rα​(i))​d​rm​…​d​r1.\displaystyle=\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})-\Psi({\check{X}^{n}}\_{\eta(r\_{1})},\dots,{\check{X}^{n}}\_{\eta(r\_{m})})\right]\prod\_{i=2}^{m}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}dr\_{m}\dots dr\_{1}. |  |

By Corollary [A.7](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem7 "Corollary A.7. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ2,1|\displaystyle|\mathcal{E}\_{2,1}| | ≤C∫0T…∫0rm−1(∑1≤k≤l≤m|Cov(Xη​(rk),Xη​(rl))−Cov(Xˇnη​(rk),Xˇnη​(rl))|\displaystyle\leq C\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}\bigg(\sum\_{1\leq k\leq l\leq m}|Cov(X\_{\eta(r\_{k})},X\_{\eta(r\_{l})})-Cov({\check{X}^{n}}\_{\eta(r\_{k})},{\check{X}^{n}}\_{\eta(r\_{l})})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑l=1m|𝔼[Xη​(rl)]−𝔼[Xˇnη​(rl)]|)∏i=2m|𝒟riXˇnη​(rα​(i))|drm…dr1.\displaystyle+\sum\_{l=1}^{m}|{\mathbb{E}}[X\_{\eta(r\_{l})}]-{\mathbb{E}}[{\check{X}^{n}}\_{\eta(r\_{l})}]|\bigg)\prod\_{i=2}^{m}|\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}|dr\_{m}\dots dr\_{1}. |  |

By Theorem [2.7](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), and noting that the term in parenthesis vanishes when rl<t1r\_{l}<t\_{1}, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ2,1|\displaystyle|\mathcal{E}\_{2,1}| | ≤C​∑l=1m∫0T…​∫0rm−1𝟏rl>t1​((1+η​(rl)α−1)​𝐯n​(α)+η​(rl)2​α−2n)​∏i=2m|𝒟ri​Xˇnη​(rα​(i))|​d​rm​…​d​r1,\displaystyle\leq C\sum\_{l=1}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}\mathbf{1}\_{r\_{l}>t\_{1}}\bigg((1+\eta(r\_{l})^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{\eta(r\_{l})^{2\alpha-2}}{n}\bigg)\prod\_{i=2}^{m}|\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}|dr\_{m}\dots dr\_{1}, |  |

since rl≤rkr\_{l}\leq r\_{k}. By Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℰ2,1|\displaystyle|\mathcal{E}\_{2,1}| | ≤C​∑l=1m∫0T…​∫0rl−1𝟏rl>t1​((1+η​(rl)α−1)​𝐯n​(α)+η​(rl)2​α−2n)​∏i=2l|𝒟ri​Xˇnη​(rα​(i))|​d​rl​…​d​r1,\displaystyle\leq C\sum\_{l=1}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{l-1}}\mathbf{1}\_{r\_{l}>t\_{1}}\bigg((1+\eta(r\_{l})^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{\eta(r\_{l})^{2\alpha-2}}{n}\bigg)\prod\_{i=2}^{l}|\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}|dr\_{l}\dots dr\_{1}, |  |

by integrating with respect to rm,…,rl+1r\_{m},\dots,r\_{l+1} (as usual, the constant CC changes from line to line). Now, we proceed as in the cubic case: by ([3.5](https://arxiv.org/html/2602.18234v1#S3.E5 "In Proof. ‣ 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get

|  |  |  |
| --- | --- | --- |
|  | ∫t1rl−1η​(rl)β​|𝒟rl​Xˇnη​(rα​(l))|​𝑑rl≤C​(𝟏α+β≥0​Tα+β+𝟏α+β<0​t1α+β),\int\_{t\_{1}}^{r\_{l-1}}\eta(r\_{l})^{\beta}|\mathcal{D}\_{r\_{l}}{\check{X}^{n}}\_{\eta(r\_{\alpha(l)})}|dr\_{l}\leq C\left(\mathbf{1}\_{\alpha+\beta\geq 0}T^{\alpha+\beta}+\mathbf{1}\_{\alpha+\beta<0}t\_{1}^{\alpha+\beta}\right), |  |

for β∈(−1,0]\beta\in(-1,0]. This gives with β∈{α−1,2​α−2}\beta\in\{\alpha-1,2\alpha-2\}, as in the cubic case,

|  |  |  |
| --- | --- | --- |
|  | ∫0rl−1𝟏rl>t1​C​((1+η​(rl)α−1)​𝐯n​(α)+η​(rl)2​α−2n)​|𝒟rl​Xˇnη​(rα​(l))|​𝑑rl≤C​𝐯n​(α).\int\_{0}^{r\_{l-1}}\mathbf{1}\_{r\_{l}>t\_{1}}C\bigg((1+\eta(r\_{l})^{\alpha-1}){\bf v}\_{n}(\alpha)+\frac{\eta(r\_{l})^{2\alpha-2}}{n}\bigg)|\mathcal{D}\_{r\_{l}}{\check{X}^{n}}\_{\eta(r\_{\alpha(l)})}|dr\_{l}\leq C{\bf v}\_{n}(\alpha). |  |

Finally, we use again Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") to get |ℰ2,1|≤C​𝐯n​(α)|\mathcal{E}\_{2,1}|\leq C{\bf v}\_{n}(\alpha).

#### 4.2.3. Analysis of ℰ2,2\mathcal{E}\_{2,2}

We use the usual decomposition for the difference of the products

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∏i∈Iai−∏i∈Ibi=∑j∈I(∏i∈I,i<jbi)​(aj−bj)​(∏i∈I,i>jai)\prod\_{i\in I}a\_{i}-\prod\_{i\in I}b\_{i}=\sum\_{j\in I}\left(\prod\_{i\in I,i<j}b\_{i}\right)(a\_{j}-b\_{j})\left(\prod\_{i\in I,i>j}a\_{i}\right) |  | (4.6) |

to get with I={2​…,m}I=\{2\dots,m\}

|  |  |  |
| --- | --- | --- |
|  | ∏i=2m𝒟ri​Xη​(rα​(i))−∏i=2m𝒟ri​Xˇnη​(rα​(i))\displaystyle\prod\_{i=2}^{m}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\prod\_{i=2}^{m}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})} |  |
|  |  |  |
| --- | --- | --- |
|  | =∑j=2m∏2≤i<j𝒟ri​Xˇnη​(rα​(i))×(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​∏m≥i>j𝒟ri​Xη​(rα​(i)).\displaystyle=\sum\_{j=2}^{m}\prod\_{2\leq i<j}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}\times\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)\prod\_{m\geq i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}. |  |

Here, we use the standard convention ∏∅=1\prod\_{\emptyset}=1.
Note that in ([4.6](https://arxiv.org/html/2602.18234v1#S4.E6 "In 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) aa and bb play symmetric role up to the minus sign, but it is important to keep the Malliavin derivatives of the original process for i>ji>j in the next analysis to be able to show the integration by parts ([4.8](https://arxiv.org/html/2602.18234v1#S4.E8 "In 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).
We then write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℰ2,2\displaystyle\mathcal{E}\_{2,2} | =∑j=2m∫0T…​∫0rm−1𝔼​[Ψ​(Xr1,…,Xrm)]​∏i<j𝒟ri​Xˇnη​(rα​(i))\displaystyle=\sum\_{j=2}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\prod\_{i<j}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})} |  | (4.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​∏i>j𝒟ri​Xrα​(i)​d​rm​…​d​r1+ℛ2,21+ℛ2,22​ with\displaystyle\times\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}dr\_{m}\dots dr\_{1}+\mathcal{R}^{1}\_{2,2}+\mathcal{R}^{2}\_{2,2}\text{ with } |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ2,21\displaystyle\mathcal{R}^{1}\_{2,2} | =∑j=2m∫0T…​∫0rm−1𝔼​[Ψ​(Xr1,…,Xrm)]​∏i<j𝒟ri​Xˇnη​(rα​(i))\displaystyle=\sum\_{j=2}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\prod\_{i<j}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​(∏i>j𝒟ri​Xη​(rα​(i))−∏i>j𝒟ri​Xrα​(i))​d​rm​…​d​r1\displaystyle\times\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)\left(\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}\right)dr\_{m}\dots dr\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ2,22\displaystyle\mathcal{R}^{2}\_{2,2} | =∑j=2m∫0T…​∫0rm−1(𝔼​[Ψ​(Xη​(r1),…,Xη​(rm))]−𝔼​[Ψ​(Xr1,…,Xrm)])​∏i<j𝒟ri​Xˇnη​(rα​(i))\displaystyle=\sum\_{j=2}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}\left({\mathbb{E}}\left[\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})\right]-{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\right)\prod\_{i<j}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​∏i>j𝒟ri​Xη​(rα​(i))​d​rm​…​d​r1.\displaystyle\times\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}dr\_{m}\dots dr\_{1}. |  |

Note that ℛ2,22\mathcal{R}^{2}\_{2,2} “replaces” 𝔼​[Ψ​(Xη​(r1),…,Xη​(rm))]{\mathbb{E}}\left[\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})\right] by 𝔼​[Ψ​(Xr1,…,Xrm)]{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right] and ℛ2,21\mathcal{R}^{1}\_{2,2} “replaces” ∏i>j𝒟ri​Xη​(rα​(i))\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})} by ∏i>j𝒟ri​Xrα​(i)\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}.

We first analyse ℛ2,21\mathcal{R}^{1}\_{2,2}. To do so, we use an upper bound of |𝔼​[Ψ​(Xr1,…,Xrm)]||{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]| and the triangular inequality, so that we have to upper bound the integrals

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T…​∫0rm−1∏i<j|𝒟ri​Xˇnη​(rα​(i))|\displaystyle\int\_{0}^{T}\dots\int\_{0}^{r\_{m-1}}\prod\_{i<j}|\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}| | |𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j))|\displaystyle\left|\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×|∏i>j𝒟ri​Xη​(rα​(i))−∏i>j𝒟ri​Xrα​(i)|​d​rm​…​d​r1.\displaystyle\times\left|\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}\right|dr\_{m}\dots dr\_{1}. |  |

We use again ([4.6](https://arxiv.org/html/2602.18234v1#S4.E6 "In 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and get

|  |  |  |
| --- | --- | --- |
|  | ∏i>j𝒟ri​Xη​(rα​(i))−∏i>j𝒟ri​Xrα​(i)=∑i>j∏j<k<i𝒟rk​Xrα​(k)​(𝒟ri​Xη​(rα​(i))−𝒟ri​Xrα​(i))​∏k>i𝒟rk​Xη​(rα​(k)).\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}=\sum\_{i>j}\prod\_{j<k<i}\mathcal{D}\_{r\_{k}}X\_{r\_{\alpha(k)}}\left(\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}\right)\prod\_{k>i}\mathcal{D}\_{r\_{k}}X\_{\eta(r\_{\alpha(k)})}. |  |

Let us consider the term ii of this sum, and integrate first from the d​rmdr\_{m} to d​ridr\_{i}. We have

|  |  |  |
| --- | --- | --- |
|  | ∫0ri−1…​∫0rm−1|𝒟ri​Xη​(rα​(i))−𝒟ri​Xrα​(i)|​∏k>i|𝒟rk​Xη​(rα​(k))|​d​rm​…​d​ri\displaystyle\int\_{0}^{r\_{i-1}}\dots\int\_{0}^{r\_{m-1}}\left|\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}\right|\prod\_{k>i}|\mathcal{D}\_{r\_{k}}X\_{\eta(r\_{\alpha(k)})}|dr\_{m}\dots dr\_{i} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤CTm−i−1​∫0ri−1|𝒟ri​Xη​(rα​(i))−𝒟ri​Xrα​(i)|​𝑑ri,\displaystyle\leq C\_{T}^{m-i-1}\int\_{0}^{r\_{i-1}}\left|\mathcal{D}\_{r\_{i}}X\_{\eta(r\_{\alpha(i)})}-\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}}\right|dr\_{i}, |  |

by using ([2.7](https://arxiv.org/html/2602.18234v1#S2.E7 "In Remark 2.3. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). Now, using ([B.8](https://arxiv.org/html/2602.18234v1#A2.E8 "In Proof of Lemma 2.12. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we obtain that this integral is O​(n−α)O(n^{-\alpha}). Integrating then from d​ridr\_{i} to d​rj+1dr\_{j+1}, we get

|  |  |  |
| --- | --- | --- |
|  | ℛ2,21≤C​n−α​∑j=2m∫0T…​∫0rj−1∏i<j|𝒟ri​Xˇnη​(rα​(i))|​|𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j))|​d​rj​…​d​r1.\mathcal{R}^{1}\_{2,2}\leq Cn^{-\alpha}\sum\_{j=2}^{m}\int\_{0}^{T}\dots\int\_{0}^{r\_{j-1}}\prod\_{i<j}|\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}|\left|\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right|dr\_{j}\dots dr\_{1}. |  |

We now use Lemma [2.12](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for the integration with respect to d​rjdr\_{j} and then Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for the integration from d​rj−1dr\_{j-1} to d​r1dr\_{1}, and we get ℛ2,21≤C​n−2​α=O​(𝐯n​(α))\mathcal{R}^{1}\_{2,2}\leq Cn^{-2\alpha}=O({\bf v}\_{n}(\alpha)) since 2​α>12\alpha>1.

We now analyse ℛ2,22\mathcal{R}^{2}\_{2,2}. By Proposition [A.4](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (1), we have

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[Ψ​(Xη​(r1),…,Xη​(rm))]−𝔼​[Ψ​(Xr1,…,Xrm)]|≤C​(Tn)2​α−1.\left|{\mathbb{E}}\left[\Psi(X\_{\eta(r\_{1})},\dots,X\_{\eta(r\_{m})})\right]-{\mathbb{E}}\left[\Psi(X\_{r\_{1}},\dots,X\_{r\_{m}})\right]\right|\leq C\left(\frac{T}{n}\right)^{2\alpha-1}. |  |

Then, we integrate from d​rmdr\_{m} to d​r1dr\_{1} as follows: we use ([2.7](https://arxiv.org/html/2602.18234v1#S2.E7 "In Remark 2.3. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) for d​ridr\_{i} with i>ji>j, Lemma [2.12](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for the integral with respect to d​rjdr\_{j} and finally Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for d​ridr\_{i} with i<ji<j. This leads to

|  |  |  |
| --- | --- | --- |
|  | |ℛ2,22|≤C​(Tn)3​α−1=O​(𝐯n​(α)).|\mathcal{R}^{2}\_{2,2}|\leq C\left(\frac{T}{n}\right)^{3\alpha-1}=O({\bf v}\_{n}(\alpha)). |  |

We then go back to Equation ([4.7](https://arxiv.org/html/2602.18234v1#S4.E7 "In 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and define

|  |  |  |
| --- | --- | --- |
|  | ℰ2,2,j=∫0T…​∫0rj−1Gj​(r1,…,rj)​∏i<j𝒟ri​Xˇnη​(rα​(i))​(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​d​rj​…​d​r1,\displaystyle\mathcal{E}\_{2,2,j}=\int\_{0}^{T}\dots\int\_{0}^{r\_{j-1}}G\_{j}(r\_{1},\dots,r\_{j})\prod\_{i<j}\mathcal{D}\_{r\_{i}}{\check{X}^{n}}\_{\eta(r\_{\alpha(i)})}\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)dr\_{j}\dots dr\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | Gj​(r1,…,rj)=∫0rj∫0rj+1…​∫0rm−1𝔼​[Ψ​(X𝐫)]​Πj​(𝐫)​𝑑rj+1​…​𝑑rm,\displaystyle G\_{j}(r\_{1},\dots,r\_{j})=\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+1}}\dots\int\_{0}^{r\_{m-1}}{\mathbb{E}}\left[\Psi({X}\_{{\bf r}})\right]\Pi\_{j}({\bf r})dr\_{j+1}\dots dr\_{m}, |  |

with 𝐫=(r1,…,rm){\bf r}=(r\_{1},\dots,r\_{m}),

|  |  |  |
| --- | --- | --- |
|  | Πj​(𝐫):=∏i>j𝒟ri​Xrα​(i)\Pi\_{j}({\bf r}):=\prod\_{i>j}\mathcal{D}\_{r\_{i}}X\_{r\_{\alpha(i)}} |  |

and X𝐫=(Xr1,…,Xrm)X\_{{\bf r}}=(X\_{r\_{1}},\dots,X\_{r\_{m}}). Note that in the product, we distinguish the indices strictly greater than jj that are frozen on the time grid, while the indices smaller or equal to jj are not frozen, so that the function GjG\_{j} is continuous with respect to (r1,…,rj)(r\_{1},\dots,r\_{j}). The analysis of this term mainly relies on the following proposition, whose proof is quite technical and is postponed in the appendix.

###### Proposition 4.8.

Let 1≤j≤m1\leq j\leq m, ℓj+1,…,ℓm≥1\ell\_{j+1},\dots,\ell\_{m}\geq 1. Then the function

|  |  |  |
| --- | --- | --- |
|  | Hj​(r1,…,rj)=∫0rj∫0rj+1…​∫0rm−1ϕ​(𝐫)​∏i>j(rα​(i)−ri)ℓi​α−1​d​rm​…​d​rj+1\displaystyle H\_{j}(r\_{1},\dots,r\_{j})=\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+1}}\dots\int\_{0}^{r\_{m-1}}\phi({\bf r})\prod\_{i>j}(r\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{j+1} |  |

with 𝐫=(r1,…,rm){\bf r}=(r\_{1},\dots,r\_{m}) and ϕ​(𝐫)=𝔼​[Ψ​(X𝐫)]\phi({\bf r})={\mathbb{E}}[\Psi(X\_{\bf r})] is differentiable with respect to rjr\_{j} and

|  |  |  |
| --- | --- | --- |
|  | ∫0rj−1|∂jH​(r1,…,rj)|​𝑑rj≤Cm,ϕ​T2​α​∑i=j+1mℓi.\int\_{0}^{r\_{j-1}}|\partial\_{j}H(r\_{1},\dots,r\_{j})|dr\_{j}\leq C\_{m,\phi}T^{2\alpha\sum\_{i=j+1}^{m}\ell\_{i}}. |  |

We now make an integration by part with respect to rjr\_{j} that we justify afterwards:

|  |  |  |
| --- | --- | --- |
|  | ∫0rj−1Gj​(r1,…,rj)​(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​𝑑rj\displaystyle\int\_{0}^{r\_{j-1}}G\_{j}(r\_{1},\dots,r\_{j})\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)dr\_{j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =Gj​(r1,…,rj−1,rj−1)​∫0rj−1(𝒟s​Xη​(rα​(j))−𝒟s​Xˇnη​(rα​(j)))​𝑑s\displaystyle=G\_{j}(r\_{1},\dots,r\_{j-1},r\_{j-1})\int\_{0}^{r\_{j-1}}\left(\mathcal{D}\_{s}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)ds |  | (4.8) |
|  |  |  |
| --- | --- | --- |
|  | −∫0rj−1∂jGj​(r1,…,rj)​∫0rj(𝒟s​Xη​(rα​(j))−𝒟s​Xˇnη​(rα​(j)))​𝑑s​𝑑rj.\displaystyle\ \ -\int\_{0}^{r\_{j-1}}\partial\_{j}G\_{j}(r\_{1},\dots,r\_{j})\int\_{0}^{r\_{j}}\left(\mathcal{D}\_{s}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)dsdr\_{j}. |  |

In fact, we can write by ([2.6](https://arxiv.org/html/2602.18234v1#S2.E6 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) GjG\_{j} as an infinite sum of terms that can be written as in Proposition [4.8](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), and using this Proposition, we have ∫0rj−1|∂jGj​(r1,…,rj)|​𝑑rj≤C\int\_{0}^{r\_{j-1}}|\partial\_{j}G\_{j}(r\_{1},\dots,r\_{j})|dr\_{j}\leq C for a constant CC that depends on ϕ\phi but does not depend on nn. Of course, this justifies the integration by parts. We observe also that GjG\_{j} is bounded. Therefore, we get from ([4.8](https://arxiv.org/html/2602.18234v1#S4.E8 "In 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")

|  |  |  |
| --- | --- | --- |
|  | |∫0rj−1Gj​(r1,…,rj)​(𝒟rj​Xη​(rα​(j))−𝒟rj​Xˇnη​(rα​(j)))​𝑑rj|≤C​Tn.\displaystyle\left|\int\_{0}^{r\_{j-1}}G\_{j}(r\_{1},\dots,r\_{j})\left(\mathcal{D}\_{r\_{j}}X\_{\eta(r\_{\alpha(j)})}-\mathcal{D}\_{r\_{j}}{\check{X}^{n}}\_{\eta(r\_{\alpha(j)})}\right)dr\_{j}\right|\leq C\frac{T}{n}. |  |

We conclude that |ℰ2,2,j|≤C​Tn|\mathcal{E}\_{2,2,j}|\leq C\frac{T}{n} by using Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for the integration from d​rj−1dr\_{j-1} to d​r1dr\_{1}. This leads to |ℰ2,2|≤C​𝐯n​(α)|\mathcal{E}\_{2,2}|\leq C{\bf v}\_{n}(\alpha). This concludes the proof of Theorem [4.1](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")

## Appendix A Technical results

We first recall that there exists Cα>0C\_{\alpha}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (i+1)α−iα≤Cα​iα−1,(i+1)α−iα≤Cα​(i+1)α−1,i∈ℕ,(i+1)^{\alpha}-i^{\alpha}\leq C\_{\alpha}i^{\alpha-1},\ (i+1)^{\alpha}-i^{\alpha}\leq C\_{\alpha}(i+1)^{\alpha-1},\ i\in{\mathbb{N}}, |  | (A.1) |

and refer to [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.1] for a proof (note that 1≤i+1i≤21\leq\frac{i+1}{i}\leq 2 for i≥2i\geq 2, so that the first inequality implies the second one, and the second one is trivially satisfied for i=0i=0). We present a useful lemma, which is an adaptation to our context of [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.2].

###### Lemma A.1.

Let α,β∈(0,1)\alpha,\beta\in(0,1). Then, we have for all k≥1k\geq 1

|  |  |  |
| --- | --- | --- |
|  | ∑i=1k(k−(i−1))β−1​iα−1≤Γ​(α)​Γ​(β)Γ​(α+β)​kα+β−1.\sum\_{i=1}^{k}(k-(i-1))^{\beta-1}i^{\alpha-1}\leq\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}k^{\alpha+\beta-1}. |  |

###### Proof.

We write

|  |  |  |
| --- | --- | --- |
|  | ∑i=1k(k−(i−1))β−1​iα−1=kα+β−1​1k​∑i=1k(1−i−1k)β−1​(ik)α−1,\sum\_{i=1}^{k}(k-(i-1))^{\beta-1}i^{\alpha-1}=k^{\alpha+\beta-1}\frac{1}{k}\sum\_{i=1}^{k}\left(1-\frac{i-1}{k}\right)^{\beta-1}\left(\frac{i}{k}\right)^{\alpha-1}, |  |

and observe that ∫i−1kik(1−x)β−1​xα−1​𝑑x≥1k​(1−i−1k)β−1​(ik)α−1\int\_{\frac{i-1}{k}}^{\frac{i}{k}}(1-x)^{\beta-1}x^{\alpha-1}dx\geq\frac{1}{k}\left(1-\frac{i-1}{k}\right)^{\beta-1}\left(\frac{i}{k}\right)^{\alpha-1} since x↦xα−1x\mapsto x^{\alpha-1} and x↦xβ−1x\mapsto x^{\beta-1} are positive decreasing functions. Therefore,

|  |  |  |
| --- | --- | --- |
|  | ∑i=1k(k−(i−1))β−1​iα−1≤kα+β−1​∫01(1−x)β−1​xα−1​𝑑x=Γ​(α)​Γ​(β)Γ​(α+β)​kα+β−1.∎\sum\_{i=1}^{k}(k-(i-1))^{\beta-1}i^{\alpha-1}\leq k^{\alpha+\beta-1}\int\_{0}^{1}(1-x)^{\beta-1}x^{\alpha-1}dx=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}k^{\alpha+\beta-1}.\qed |  |

###### Lemma A.2.

Let T>0T>0, n≥1n\geq 1. Let tk=k​T/nt\_{k}=kT/n for k∈{0,…,n}k\in\{0,\dots,n\}. Let α,β∈(0,1)\alpha,\beta\in(0,1).
Then, there exists a constant Cα,βC\_{\alpha,\beta} that only depends on α\alpha and β\beta such that for any k≤nk\leq n,

|  |  |  |
| --- | --- | --- |
|  | ∑i=1k((tk−ti−1)β−(tk−ti)β)​(tiα−ti−1α)≤Cα,β​(Tn)α+β​kα+β−1.\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\beta}-(t\_{k}-t\_{i})^{\beta}\right)\left(t\_{i}^{\alpha}-t\_{i-1}^{\alpha}\right)\leq C\_{\alpha,\beta}\left(\frac{T}{n}\right)^{\alpha+\beta}k^{\alpha+\beta-1}. |  |

###### Proof.

We have by using ([A.1](https://arxiv.org/html/2602.18234v1#A1.E1 "In Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1k((tk−ti−1)β−(tk−ti)β)​(tiα−ti−1α)\displaystyle\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\beta}-(t\_{k}-t\_{i})^{\beta}\right)\left(t\_{i}^{\alpha}-t\_{i-1}^{\alpha}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (Tn)α+β​∑i=1k((k−(i−1))β−(k−i)β)​(iα−(i−1)α)\displaystyle\left(\frac{T}{n}\right)^{\alpha+\beta}\sum\_{i=1}^{k}\left((k-(i-1))^{\beta}-(k-i)^{\beta}\right)\left(i^{\alpha}-(i-1)^{\alpha}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | Cα​Cβ​(Tn)α+β​∑i=1k(k−(i−1))β−1​iα−1≤Cα​Cβ​Γ​(α)​Γ​(β)Γ​(α+β)​(Tn)α+β​kα+β−1,\displaystyle C\_{\alpha}C\_{\beta}\left(\frac{T}{n}\right)^{\alpha+\beta}\sum\_{i=1}^{k}(k-(i-1))^{\beta-1}i^{\alpha-1}\leq C\_{\alpha}C\_{\beta}\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}\left(\frac{T}{n}\right)^{\alpha+\beta}k^{\alpha+\beta-1}, |  |

by Lemma [A.1](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").
∎

We now present a lemma that is the analogous of [[12](https://arxiv.org/html/2602.18234v1#bib.bib12), Proposition 4.1] in our framework.

###### Lemma A.3.

Let α∈(1/2,1)\alpha\in(1/2,1) and T>0T>0. There exists a constant CC depending on TT, σ\sigma, κ2\kappa\_{2} and α\alpha such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀s,t∈[0,T],|𝒞X​(s,t)−𝒞X​(t,t)|≤C​|t−s|2​α−1.\forall s,t\in[0,T],\ |{\mathcal{C}^{X}}(s,t)-{\mathcal{C}^{X}}(t,t)|\leq C|t-s|^{2\alpha-1}. |  | (A.2) |

Moreover, the function t↦𝒞X​(t,s)t\mapsto{\mathcal{C}^{X}}(t,s) is differentiable on (0,T)(0,T) for t≠st\not=s, and there exists a constant CC depending on TT, σ\sigma, κ2\kappa\_{2} and α\alpha such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀s,t∈(0,T),s≠t,|∂1𝒞X​(t,s)|≤C​(sα−1​tα−1+|s−t|2​α−2).\forall s,t\in(0,T),s\not=t,\ |\partial\_{1}{\mathcal{C}^{X}}(t,s)|\leq C\left(s^{\alpha-1}t^{\alpha-1}+\left|s-t\right|^{2\alpha-2}\right). |  | (A.3) |

Note that by symmetry we get from ([A.3](https://arxiv.org/html/2602.18234v1#A1.E3 "In Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))

|  |  |  |
| --- | --- | --- |
|  | ∀s,t∈(0,T),s≠t,|∂2𝒞X​(t,s)|≤C​(sα−1​tα−1+|s−t|2​α−2).\forall s,t\in(0,T),s\not=t,\ |\partial\_{2}{\mathcal{C}^{X}}(t,s)|\leq C\left(s^{\alpha-1}t^{\alpha-1}+\left|s-t\right|^{2\alpha-2}\right). |  |

###### Proof.

The first part of the claim is an easy consequence of the second. Indeed, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝒞X​(s,t)−𝒞X​(t,t)|\displaystyle|{\mathcal{C}^{X}}(s,t)-{\mathcal{C}^{X}}(t,t)| | ≤∫(s,t)|∂1𝒞X​(u,t)|​𝑑u\displaystyle\leq\int\_{(s,t)}|\partial\_{1}{\mathcal{C}^{X}}(u,t)|du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​∫(s,t)(uα−1​tα−1+|u−t|2​α−2)​𝑑u\displaystyle\leq C\int\_{(s,t)}\left(u^{\alpha-1}t^{\alpha-1}+\left|u-t\right|^{2\alpha-2}\right)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C​(tα−1α​|sα−tα|+|s−t|2​α−12​α−1)≤C​|s−t|2​α−1,\displaystyle=C\left(\frac{t^{\alpha-1}}{\alpha}|s^{\alpha}-t^{\alpha}|+\frac{|s-t|^{2\alpha-1}}{2\alpha-1}\right)\leq C|s-t|^{2\alpha-1}, |  |

since |sα−tα|≤|t−s|α≤T1−α​|t−s|2​α−1|s^{\alpha}-t^{\alpha}|\leq|t-s|^{\alpha}\leq T^{1-\alpha}|t-s|^{2\alpha-1}. This gives ([A.2](https://arxiv.org/html/2602.18234v1#A1.E2 "In Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

From ([2.5](https://arxiv.org/html/2602.18234v1#S2.E5 "In Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞X​(t,s)\displaystyle{\mathcal{C}^{X}}(t,s) | =σ2​∑i1,i2=1∞κ2i1+i2−2​ti1​α​si2​α−1Γ​(i1​α+1)​Γ​(i2​α)​F12​(1−i2​α,1;i1​α+1,ts),t≤s,\displaystyle=\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{t^{i\_{1}\alpha}s^{i\_{2}\alpha-1}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{t}{s}),\ t\leq s, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞X​(t,s)\displaystyle{\mathcal{C}^{X}}(t,s) | =σ2​∑i1,i2=1∞κ2i1+i2−2​si1​α​ti2​α−1Γ​(i1​α+1)​Γ​(i2​α)​F12​(1−i2​α,1;i1​α+1,st),s≤t.\displaystyle=\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{s^{i\_{1}\alpha}t^{i\_{2}\alpha-1}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{s}{t}),\ s\leq t. |  |

We can differentiate and get for 0<t<s0<t<s by using [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), 15.5.1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂1𝒞X​(t,s)=\displaystyle\partial\_{1}{\mathcal{C}^{X}}(t,s)= | σ2​∑i1,i2=1∞κ2i1+i2−2​ti1​α−1​si2​α−1Γ​(i1​α)​Γ​(i2​α)​F12​(1−i2​α,1;i1​α+1,ts)\displaystyle\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{t^{i\_{1}\alpha-1}s^{i\_{2}\alpha-1}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{t}{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ2​∑i1,i2=1∞κ2i1+i2−2​ti1​α​si2​α−2Γ​(i1​α+1)​Γ​(i2​α)​1−i2​αi1​α+1​F12​(2−i2​α,2;i1​α+2,ts).\displaystyle+\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{t^{i\_{1}\alpha}s^{i\_{2}\alpha-2}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\frac{1-i\_{2}\alpha}{i\_{1}\alpha+1}{{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,\frac{t}{s}). |  |

By ([2.2](https://arxiv.org/html/2602.18234v1#S2.E2 "In 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), the maximum of F12​(a,b;c,z){}\_{2}F\_{1}(a,b;c,z) on z∈[0,1]z\in[0,1] is reached by z=0z=0 if a≤0a\leq 0 and z=1z=1 if a>0a>0. We get by [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), 15.4.20]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxz∈[0,1]⁡F12​(a,b;c,z)=1a≤0+1a>0​Γ​(c)​Γ​(c−a−b)Γ​(c−a)​Γ​(c−b).\max\_{z\in[0,1]}\ {}\_{2}F\_{1}(a,b;c,z)=1\_{a\leq 0}+1\_{a>0}\frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}. |  | (A.4) |

Therefore, we have

|  |  |  |
| --- | --- | --- |
|  | |σ2​∑i1,i2=1∞κ2i1+i2−2​ti1​α−1​si2​α−1Γ​(i1​α)​Γ​(i2​α)​F12​(1−i2​α,1;i1​α+1,ts)|\displaystyle\left|\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{t^{i\_{1}\alpha-1}s^{i\_{2}\alpha-1}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{t}{s})\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤sα−1​tα−1​σ2​∑i1,i2=1∞|κ2|i1+i2−2​t(i1−1)​α​s(i2−1)​αΓ​(i1​α)​Γ​(i2​α)​maxz∈[0,1]⁡F12​(1−i2​α,1;i1​α+1,z)\displaystyle\leq s^{\alpha-1}t^{\alpha-1}\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}\frac{t^{(i\_{1}-1)\alpha}s^{(i\_{2}-1)\alpha}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}\max\_{z\in[0,1]}\ {}\_{2}F\_{1}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,z) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤sα−1​tα−1​σ2​∑i1,i2=1∞|κ2|i1+i2−2​T(i1+i2−2)​αΓ​(i1​α)​Γ​(i2​α)​maxz∈[0,1]⁡F12​(1−i2​α,1;i1​α+1,z)\displaystyle\leq s^{\alpha-1}t^{\alpha-1}\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}\frac{T^{(i\_{1}+i\_{2}-2)\alpha}}{\Gamma(i\_{1}\alpha)\Gamma(i\_{2}\alpha)}\max\_{z\in[0,1]}\ {}\_{2}F\_{1}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,z) |  |
|  |  |  |
| --- | --- | --- |
|  | =:CT1sα−1tα−1.\displaystyle=:C^{1}\_{T}s^{\alpha-1}t^{\alpha-1}. |  |

For the second series, we first observe that F12​(2−i2​α,2;i1​α+2,1)<∞{}\_{2}F\_{1}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,1)<\infty if (i1+i2)​α−2>0(i\_{1}+i\_{2})\alpha-2>0 (which holds if i1+i2≥4i\_{1}+i\_{2}\geq 4) by ([A.4](https://arxiv.org/html/2602.18234v1#A1.E4 "In Proof. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and have

|  |  |  |
| --- | --- | --- |
|  | |σ2​∑i1+i2≥4∞κ2i1+i2−2​ti1​α​si2​α−2Γ​(i1​α+1)​Γ​(i2​α)​1−i2​αi1​α+1​F12​(2−i2​α,2;i1​α+2,ts)|\displaystyle\left|\sigma^{2}\sum\_{i\_{1}+i\_{2}\geq 4}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{t^{i\_{1}\alpha}s^{i\_{2}\alpha-2}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\frac{1-i\_{2}\alpha}{i\_{1}\alpha+1}{{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,\frac{t}{s})\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​sα−1​tα−1​∑i1+i2≥4∞|κ2|i1+i2−2​t(i1−1)​α+1​s(i2−1)​α−1Γ​(i1​α+1)​Γ​(i2​α)​|1−i2​α|i1​α+1​F12​(2−i2​α,2;i1​α+2,ts)\displaystyle\leq\sigma^{2}s^{\alpha-1}t^{\alpha-1}\sum\_{i\_{1}+i\_{2}\geq 4}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}\frac{t^{(i\_{1}-1)\alpha+1}s^{(i\_{2}-1)\alpha-1}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\frac{|1-i\_{2}\alpha|}{i\_{1}\alpha+1}{{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,\frac{t}{s}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​sα−1​tα−1​∑i1+i2≥4∞|κ2|i1+i2−2​T(i1+i2−2)​αΓ​(i1​α+1)​Γ​(i2​α)​|1−i2​α|i1​α+1​maxz∈[0,1]⁡F12​(2−i2​α,2;i1​α+2,z)\displaystyle\leq\sigma^{2}s^{\alpha-1}t^{\alpha-1}\sum\_{i\_{1}+i\_{2}\geq 4}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}\frac{T^{(i\_{1}+i\_{2}-2)\alpha}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\frac{|1-i\_{2}\alpha|}{i\_{1}\alpha+1}\max\_{z\in[0,1]}\ {{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,z) |  |
|  |  |  |
| --- | --- | --- |
|  | =:CT2sα−1tα−1,\displaystyle=:C^{2}\_{T}s^{\alpha-1}t^{\alpha-1}, |  |

using t≤s≤Tt\leq s\leq T for the last inequality.

We now focus on the three other terms of the second series, i.e. i1=i2=1i\_{1}=i\_{2}=1; i1=1i\_{1}=1 and i2=2i\_{2}=2; i2=1i\_{2}=1 and i1=2i\_{1}=2.
To analyse these terms, we use [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Formula 15.8.1]
F12​(2−i2​α,2;i1​α+2,ts)=(1−ts)2(i1+i2)​α−2​F1​((i1+i2)​α,i1​α;i1​α+2,ts){}\_{2}F\_{1}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,\frac{t}{s})=(1-\frac{t}{s})^{(i\_{1}+i\_{2})\alpha-2}\ \_{2}F\_{1}((i\_{1}+i\_{2})\alpha,i\_{1}\alpha;i\_{1}\alpha+2,\frac{t}{s}).

∙\bullet The term obtained with i1=i2=1i\_{1}=i\_{2}=1 is:

|  |  |  |
| --- | --- | --- |
|  | σ2​(1−α)1+α​tα​sα−2Γ​(1+α)​Γ​(α)​(1−ts)22​α−2​F1​(2​α,α;α+2,ts).\frac{\sigma^{2}(1-\alpha)}{1+\alpha}\frac{t^{\alpha}s^{\alpha-2}}{\Gamma(1+\alpha)\Gamma(\alpha)}\left(1-\frac{t}{s}\right)^{2\alpha-2}\ \_{2}F\_{1}(2\alpha,\alpha;\alpha+2,\frac{t}{s}). |  |

∙\bullet The term obtained with i1=1i\_{1}=1, i2=2i\_{2}=2 is:

|  |  |  |
| --- | --- | --- |
|  | σ2​κ2​(1−2​α)1+α​tα​s2​α−2Γ​(1+α)​Γ​(2​α)​(1−ts)23​α−2​F1​(3​α,α;α+2,ts).\frac{\sigma^{2}\kappa\_{2}(1-2\alpha)}{1+\alpha}\frac{t^{\alpha}s^{2\alpha-2}}{\Gamma(1+\alpha)\Gamma(2\alpha)}\left(1-\frac{t}{s}\right)^{3\alpha-2}\ \_{2}F\_{1}(3\alpha,\alpha;\alpha+2,\frac{t}{s}). |  |

∙\bullet The term obtained with i1=2i\_{1}=2, i2=1i\_{2}=1 is:

|  |  |  |
| --- | --- | --- |
|  | σ2​κ2​(1−α)1+2​α​t2​α​sα−2Γ​(1+2​α)​Γ​(α)​(1−ts)23​α−2​F1​(3​α,2​α;2​α+2,ts).\frac{\sigma^{2}\kappa\_{2}(1-\alpha)}{1+2\alpha}\frac{t^{2\alpha}s^{\alpha-2}}{\Gamma(1+2\alpha)\Gamma(\alpha)}\left(1-\frac{t}{s}\right)^{3\alpha-2}\ \_{2}F\_{1}(3\alpha,2\alpha;2\alpha+2,\frac{t}{s}). |  |

By ([A.4](https://arxiv.org/html/2602.18234v1#A1.E4 "In Proof. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), the sum of these three terms can be upper bounded for all 0<t<s≤T0<t<s\leq T, up to a multiplicative constant (depending on α\alpha, σ\sigma and κ2\kappa\_{2}), by

|  |  |  |
| --- | --- | --- |
|  | (s−t)2​α−2+(s−t)3​α−2≤(1+Tα)​(s−t)2​α−2.(s-t)^{2\alpha-2}+(s-t)^{3\alpha-2}\leq(1+T^{\alpha})(s-t)^{2\alpha-2}. |  |

Finally, there exists a constant CTC\_{T} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀0<t<s≤T,|∂1𝒞X​(t,s)|≤CT​(s2​α−2+(s−t)2​α−2).\forall 0<t<s\leq T,\ |\partial\_{1}{\mathcal{C}^{X}}(t,s)|\leq C\_{T}\left(s^{2\alpha-2}+\left(s-t\right)^{2\alpha-2}\right). |  | (A.5) |

Now, we turn to the case 0<s<t≤T0<s<t\leq T and we get using [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), 15.5.1]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂1𝒞X​(t,s)=\displaystyle\partial\_{1}{\mathcal{C}^{X}}(t,s)= | σ2​∑i1,i2=1∞κ2i1+i2−2​(i2​α−1)​si1​α​ti2​α−2Γ​(i1​α+1)​Γ​(i2​α)​F12​(1−i2​α,1;i1​α+1,st)\displaystyle\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}(i\_{2}\alpha-1)\frac{s^{i\_{1}\alpha}{t}^{i\_{2}\alpha-2}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{s}{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ2​∑i1,i2=1∞κ2i1+i2−2​i2​α−1i1​α+1​si1​α+1​ti2​α−3Γ​(i1​α+1)​Γ​(i2​α)​F12​(2−i2​α,2;i1​α+2,st).\displaystyle+\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{i\_{2}\alpha-1}{i\_{1}\alpha+1}\frac{s^{i\_{1}\alpha+1}{t}^{i\_{2}\alpha-3}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,\frac{s}{t}). |  |

For the first series, we have

|  |  |  |
| --- | --- | --- |
|  | |σ2​∑i1,i2=1∞κ2i1+i2−2​(i2​α−1)​si1​α​ti2​α−2Γ​(i1​α+1)​Γ​(i2​α)​F12​(1−i2​α,1;i1​α+1,st)|\displaystyle\left|\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}(i\_{2}\alpha-1)\frac{s^{i\_{1}\alpha}{t}^{i\_{2}\alpha-2}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,\frac{s}{t})\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​∑i1,i2=1∞|κ2|i1+i2−2​|i2​α−1|​si1​α​ti2​α−2Γ​(i1​α+1)​Γ​(i2​α)​maxz∈[0,1]⁡F12​(1−i2​α,1;i1​α+1,z)\displaystyle\leq\sigma^{2}\sum\_{i\_{1},i\_{2}=1}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}|i\_{2}\alpha-1|\frac{s^{i\_{1}\alpha}{t}^{i\_{2}\alpha-2}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\max\_{z\in[0,1]}\ {{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,z) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​sα−1​tα−1​∑i1,i2=1∞|κ2|i1+i2−2​|i2​α−1|​T(i1+i2−2)​αΓ​(i1​α+1)​Γ​(i2​α)​maxz∈[0,1]⁡F12​(1−i2​α,1;i1​α+1,z)\displaystyle\leq\sigma^{2}s^{\alpha-1}t^{\alpha-1}\sum\_{i\_{1},i\_{2}=1}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}|i\_{2}\alpha-1|\frac{T^{(i\_{1}+i\_{2}-2)\alpha}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\max\_{z\in[0,1]}\ {{}\_{2}F\_{1}}(1-i\_{2}\alpha,1;i\_{1}\alpha+1,z) |  |
|  |  |  |
| --- | --- | --- |
|  | =:C~T1sα−1tα−1.\displaystyle=:\tilde{C}^{1}\_{T}s^{\alpha-1}t^{\alpha-1}. |  |

For the second series, using the same arguments as for the first part of the proof, we have

|  |  |  |
| --- | --- | --- |
|  | σ2​|∑i1+i2≥4∞κ2i1+i2−2​i2​α−1i1​α+1​si1​α+1​ti2​α−3Γ​(i1​α+1)​Γ​(i2​α)​F12​(2−i2​α,2;i1​α+2,st)|\displaystyle\sigma^{2}\left|\sum\_{i\_{1}+i\_{2}\geq 4}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{i\_{2}\alpha-1}{i\_{1}\alpha+1}\frac{s^{i\_{1}\alpha+1}{t}^{i\_{2}\alpha-3}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}{{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,\frac{s}{t})\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​sα−1​tα−1​∑i1+i2≥4∞|κ2|i1+i2−2​|i2​α−1|i1​α+1​s(i1−1)​α+2​t(i2−1)​α−2Γ​(i1​α+1)​Γ​(i2​α)​maxz∈[0,1]⁡F12​(2−i2​α,2;i1​α+2,z)\displaystyle\leq\sigma^{2}s^{\alpha-1}t^{\alpha-1}\sum\_{i\_{1}+i\_{2}\geq 4}^{\infty}|\kappa\_{2}|^{i\_{1}+i\_{2}-2}\frac{|i\_{2}\alpha-1|}{i\_{1}\alpha+1}\frac{s^{(i\_{1}-1)\alpha+2}t^{(i\_{2}-1)\alpha-2}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\max\_{z\in[0,1]}\ {{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,z) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​sα−1​tα−1​∑i1+i2≥4∞κ2i1+i2−2​|i2​α−1|i1​α+1​T(i1+i2−2)​αΓ​(i1​α+1)​Γ​(i2​α)​maxz∈[0,1]⁡F12​(2−i2​α,2;i1​α+2,z)\displaystyle\leq\sigma^{2}s^{\alpha-1}t^{\alpha-1}\sum\_{i\_{1}+i\_{2}\geq 4}^{\infty}\kappa\_{2}^{i\_{1}+i\_{2}-2}\frac{|i\_{2}\alpha-1|}{i\_{1}\alpha+1}\frac{T^{(i\_{1}+i\_{2}-2)\alpha}}{\Gamma(i\_{1}\alpha+1)\Gamma(i\_{2}\alpha)}\max\_{z\in[0,1]}\ {{}\_{2}F\_{1}}(2-i\_{2}\alpha,2;i\_{1}\alpha+2,z) |  |
|  |  |  |
| --- | --- | --- |
|  | =:C~T2sα−1tα−1.\displaystyle=:\tilde{C}^{2}\_{T}s^{\alpha-1}t^{\alpha-1}. |  |

Now the remaining terms are given by [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Formula 15.8.1]
  
∙\bullet for i1=i2=1i\_{1}=i\_{2}=1 is

|  |  |  |
| --- | --- | --- |
|  | σ2​α−1α+1​sα+1​tα−3Γ​(α+1)​Γ​(α)​(1−st)2​α−2​F12​(2​α,α;α+2,st)\sigma^{2}\frac{\alpha-1}{\alpha+1}\frac{s^{\alpha+1}{t}^{\alpha-3}}{\Gamma(\alpha+1)\Gamma(\alpha)}\left(1-\frac{s}{t}\right)^{2\alpha-2}{{}\_{2}F\_{1}}(2\alpha,\alpha;\alpha+2,\frac{s}{t}) |  |

∙\bullet for i1=1i\_{1}=1 i2=2i\_{2}=2 is

|  |  |  |
| --- | --- | --- |
|  | κ2​2​α−1α+1​sα+1​t2​α−3Γ​(α+1)​Γ​(2​α)​(1−st)3​α−2​F12​(3​α,α;α+2,st)\kappa\_{2}\frac{2\alpha-1}{\alpha+1}\frac{s^{\alpha+1}{t}^{2\alpha-3}}{\Gamma(\alpha+1)\Gamma(2\alpha)}\left(1-\frac{s}{t}\right)^{3\alpha-2}{{}\_{2}F\_{1}}(3\alpha,\alpha;\alpha+2,\frac{s}{t}) |  |

∙\bullet for i1=2i\_{1}=2 i2=1i\_{2}=1 is

|  |  |  |
| --- | --- | --- |
|  | κ2​α−12​α+1​s2​α+1​tα−3Γ​(2​α+1)​Γ​(α)​(1−st)3​α−2​F12​(3​α,2​α;2​α+2,st).\kappa\_{2}\frac{\alpha-1}{2\alpha+1}\frac{s^{2\alpha+1}{t}^{\alpha-3}}{\Gamma(2\alpha+1)\Gamma(\alpha)}\left(1-\frac{s}{t}\right)^{3\alpha-2}{{}\_{2}F\_{1}}(3\alpha,2\alpha;2\alpha+2,\frac{s}{t}). |  |

The sum of these three terms can be upper bounded for 0<s<t≤T0<s<t\leq T, up to a multiplicative constant (depending on α\alpha, σ\sigma and κ2\kappa\_{2}), by

|  |  |  |
| --- | --- | --- |
|  | (s−t)2​α−2+(s−t)3​α−2≤(1+Tα)​(s−t)2​α−2.(s-t)^{2\alpha-2}+(s-t)^{3\alpha-2}\leq(1+T^{\alpha})(s-t)^{2\alpha-2}. |  |

Combining this with ([A.5](https://arxiv.org/html/2602.18234v1#A1.E5 "In Proof. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get ([A.3](https://arxiv.org/html/2602.18234v1#A1.E3 "In Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).
∎

###### Proposition A.4.

Let Ψ∈𝒞2​(ℝd,ℝ)\Psi\in\mathcal{C}^{2}({\mathbb{R}}^{d},{\mathbb{R}}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∃C∈ℝ+,∀x∈ℝd,|Ψ​(x)|+∑k=1d|∂kΨ​(x)|+∑k1,k2=1d|∂k1∂k2Ψ​(x)|≤C​eC​∑i=1d|xi|.\exists C\in{\mathbb{R}}\_{+},\ \forall x\in{\mathbb{R}}^{d},\ |\Psi(x)|+\sum\_{k=1}^{d}|\partial\_{k}\Psi(x)|+\sum\_{k\_{1},k\_{2}=1}^{d}|\partial\_{k\_{1}}\partial\_{k\_{2}}\Psi(x)|\leq Ce^{C\sum\_{i=1}^{d}|x\_{i}|}. |  | (A.6) |

Let ϕ\phi be defined by

|  |  |  |
| --- | --- | --- |
|  | ϕ​(r1,…,rd)=𝔼​[Ψ​(Xr1,…,Xrd)],r1,…,rd∈[0,T].\phi(r\_{1},\dots,r\_{d})={\mathbb{E}}[\Psi(X\_{r\_{1}},\dots,X\_{r\_{d}})],\ r\_{1},\dots,r\_{d}\in[0,T]. |  |

Then, ϕ\phi is continuous and continuously differentiable on {(r1,…,rd)∈[0,T]:r1>⋯>rd}\{(r\_{1},\dots,r\_{d})\in[0,T]:r\_{1}>\dots>r\_{d}\}. Moreover, there exists C∈ℝ+C\in{\mathbb{R}}\_{+} that depends on TT and Ψ\Psi such that |ϕ​(r1,…,rd)|≤C|\phi(r\_{1},\dots,r\_{d})|\leq C and

1. (1)

   |  |  |  |
   | --- | --- | --- |
   |  | |ϕ​(r1,…,rd)−ϕ​(r̊1,…,r̊d)|≤C​(∑i=1d|ri−r̊i|2​α−1),|\phi(r\_{1},\dots,r\_{d})-\phi(\mathring{r}\_{1},\dots,\mathring{r}\_{d})|\leq C\left(\sum\_{i=1}^{d}|r\_{i}-\mathring{r}\_{i}|^{2\alpha-1}\right), |  |
2. (2)

   for 2≤i≤d2\leq i\leq d,

   |  |  |  |
   | --- | --- | --- |
   |  | |∂iϕ​(r1,…,rd)|≤C​((ri−1−ri)2​α−2+(ri−ri+1)2​α−2),|\partial\_{i}\phi(r\_{1},\dots,r\_{d})|\leq C\left((r\_{i-1}-r\_{i})^{2\alpha-2}+(r\_{i}-r\_{i+1})^{2\alpha-2}\right), |  |
3. (3)

   |  |  |  |
   | --- | --- | --- |
   |  | |∂1ϕ​(r1,…,rd)|≤C​(r1−r2)2​α−2,|∂dϕ​(r1,…,rd)|≤C​(rd2​α−2+(rd−1−rd)2​α−2).|\partial\_{1}\phi(r\_{1},\dots,r\_{d})|\leq C(r\_{1}-r\_{2})^{2\alpha-2},\ |\partial\_{d}\phi(r\_{1},\dots,r\_{d})|\leq C\left(r\_{d}^{2\alpha-2}+(r\_{d-1}-r\_{d})^{2\alpha-2}\right). |  |

###### Proof.

The boundedness of ϕ\phi is obvious since |Ψ​(x)|≤C​eC​∑i=1d|xi||\Psi(x)|\leq Ce^{C\sum\_{i=1}^{d}|x\_{i}|} and (Xr1,…,Xrd)(X\_{r\_{1}},\dots,X\_{r\_{d}}) is normally distributed with a continuous mean and covariance from Propositions [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") and [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

Let mm and Γ\Gamma (resp. m̊\mathring{m} and Γ̊\mathring{\Gamma}) be the mean and the covariance of (Xr1,…,Xrd)(X\_{r\_{1}},\dots,X\_{r\_{d}}) (resp. (Xr̊1,Xr2,…,Xrd)(X\_{\mathring{r}\_{1}},X\_{r\_{2}},\dots,X\_{r\_{d}})). We define, for u∈[0,1]u\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | Zu∼𝒩d​((1−u)​m+u​m̊,(1−u)​Γ+u​Γ̊).Z\_{u}\sim\mathcal{N}\_{d}\left((1-u)m+u\mathring{m},(1-u)\Gamma+u\mathring{\Gamma}\right). |  |

From ([A.6](https://arxiv.org/html/2602.18234v1#A1.E6 "In Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), 𝔼​[∂1Ψ​(Zu)]{\mathbb{E}}[\partial\_{1}\Psi(Z\_{u})] and 𝔼​[∂1∂iΨ​(Zu)]{\mathbb{E}}[\partial\_{1}\partial\_{i}\Psi(Z\_{u})], 1≤i≤d1\leq i\leq d are bounded for u∈[0,1]u\in[0,1] and we get by Lemma [A.6](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

|  |  |  |
| --- | --- | --- |
|  | |ϕ​(r̊1,r2,…,rm)−ϕ​(r1,r2,…,rm)|\displaystyle|\phi(\mathring{r}\_{1},r\_{2},\dots,r\_{m})-\phi(r\_{1},r\_{2},\dots,r\_{m})| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​(|𝔼​[Xr̊1]−𝔼​[Xr1]|+∑i=2d|𝒞X​(r̊1,ri)−𝒞X​(r1,ri)|+|𝒞X​(r̊1,r̊1)−𝒞X​(r1,r1)|)\displaystyle\leq C\left(|{\mathbb{E}}[X\_{\mathring{r}\_{1}}]-{\mathbb{E}}[X\_{r\_{1}}]|+\sum\_{i=2}^{d}|{\mathcal{C}^{X}}(\mathring{r}\_{1},r\_{i})-{\mathcal{C}^{X}}(r\_{1},r\_{i})|+|{\mathcal{C}^{X}}(\mathring{r}\_{1},\mathring{r}\_{1})-{\mathcal{C}^{X}}(r\_{1},r\_{1})|\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​(|𝔼​[Xr̊1]−𝔼​[Xr1]|+∑i=1d|𝒞X​(r̊1,ri)−𝒞X​(r1,ri)|+|𝒞X​(r̊1,r̊1)−𝒞X​(r̊1,r1)|),\displaystyle\leq C\left(|{\mathbb{E}}[X\_{\mathring{r}\_{1}}]-{\mathbb{E}}[X\_{r\_{1}}]|+\sum\_{i=1}^{d}|{\mathcal{C}^{X}}(\mathring{r}\_{1},r\_{i})-{\mathcal{C}^{X}}(r\_{1},r\_{i})|+|{\mathcal{C}^{X}}(\mathring{r}\_{1},\mathring{r}\_{1})-{\mathcal{C}^{X}}(\mathring{r}\_{1},r\_{1})|\right), |  |

using the triangular inequality.
By Proposition [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), t↦𝔼​[Xt]t\mapsto{\mathbb{E}}[X\_{t}] is α\alpha-Hölder (and thus (2​α−1)(2\alpha-1)-Hölder) on [0,T][0,T]. We conclude by using Lemma [A.3](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), Equation ([A.2](https://arxiv.org/html/2602.18234v1#A1.E2 "In Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")). By symmetry, and with the triangular inequality, we deduce ([1](https://arxiv.org/html/2602.18234v1#A1.I1.i1 "item 1 ‣ Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

Let T≥r1>⋯>rd>0T\geq r\_{1}>\dots>r\_{d}>0 be fixed.
Let ZrZ\_{r} be the distribution of (Xr,Xr2,…,Xrd)(X\_{r},X\_{r\_{2}},\dots,X\_{r\_{d}}), r∈(r1,T]r\in(r\_{1},T]. By using again Lemma [A.6](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we obtain

|  |  |  |
| --- | --- | --- |
|  | ∂1ϕ​(r1,…,rd)=dd​r​[𝔼​[Xr]]|r=r1​𝔼​[∂1Ψ​(Xr1,Xr2,…,Xrd)]+\displaystyle\partial\_{1}\phi(r\_{1},\dots,r\_{d})=\frac{d}{dr}[{\mathbb{E}}[X\_{r}]]\_{\big|\_{r=r\_{1}}}{\mathbb{E}}[\partial\_{1}\Psi(X\_{r\_{1}},X\_{r\_{2}},\dots,X\_{r\_{d}})]+ |  |
|  |  |  |
| --- | --- | --- |
|  | 12​dd​r​[𝒞X​(r,r)]|r=r1​𝔼​[∂12Ψ​(Xr1,Xr2,…,Xrd)]+∑j=2d∂1𝒞X​(r1,rj)​𝔼​[∂1∂jΨ​(Xr1,Xr2,…,Xrd)].\displaystyle\ \ \frac{1}{2}\frac{d}{dr}[{\mathcal{C}^{X}}(r,r)]\big|\_{r=r\_{1}}{\mathbb{E}}[\partial\_{1}^{2}\Psi(X\_{r\_{1}},X\_{r\_{2}},\dots,X\_{r\_{d}})]+\sum\_{j=2}^{d}\partial\_{1}{\mathcal{C}^{X}}(r\_{1},r\_{j}){\mathbb{E}}[\partial\_{1}\partial\_{j}\Psi(X\_{r\_{1}},X\_{r\_{2}},\dots,X\_{r\_{d}})]. |  |

Using the sub-exponential growth property ([A.6](https://arxiv.org/html/2602.18234v1#A1.E6 "In Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), the above expectations are bounded. By Proposition [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), dd​r​𝔼​[Xr]≤C​rα−1≤C​r2​α−2\frac{d}{dr}{\mathbb{E}}[X\_{r}]\leq Cr^{\alpha-1}\leq Cr^{2\alpha-2} for r∈(0,T]r\in(0,T] and by Lemma [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), dd​r​𝒞X​(r,r)≤C​r2​α−2\frac{d}{dr}{\mathcal{C}^{X}}(r,r)\leq Cr^{2\alpha-2} for r∈(0,T]r\in(0,T]. Then, using Lemma [A.3](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we obtain

|  |  |  |
| --- | --- | --- |
|  | |∂1ϕ​(r1,…,rd)|≤C​(r12​α−2+∑i=2d(r1−ri)2​α−2)≤C​d​(r1−r2)2​α−2.|\partial\_{1}\phi(r\_{1},\dots,r\_{d})|\leq C\left(r\_{1}^{2\alpha-2}+\sum\_{i=2}^{d}(r\_{1}-r\_{i})^{2\alpha-2}\right)\leq Cd(r\_{1}-r\_{2})^{2\alpha-2}. |  |

For i∈{2,…,d−1}i\in\{2,\dots,d-1\}, we note ZrZ\_{r} be the distribution of (Xr1,…,Xri−1,Xr,Xri+1,…,Xrd)(X\_{r\_{1}},\dots,X\_{r\_{i-1}},X\_{r},X\_{r\_{i+1}},\dots,X\_{r\_{d}}), r∈(ri−1,ri+2)r\in(r\_{i-1},r\_{i+2}). We have

|  |  |  |
| --- | --- | --- |
|  | ∂iϕ​(r1,…,rd)=dd​r​[𝔼​[Xr]]|r=ri​𝔼​[∂iΨ​(Xr1,…,Xrd)]+\displaystyle\partial\_{i}\phi(r\_{1},\dots,r\_{d})=\frac{d}{dr}[{\mathbb{E}}[X\_{r}]]\_{\big|\_{r=r\_{i}}}{\mathbb{E}}[\partial\_{i}\Psi(X\_{r\_{1}},\dots,X\_{r\_{d}})]+ |  |
|  |  |  |
| --- | --- | --- |
|  | 12​dd​r​[𝒞X​(r,r)]|r=ri​𝔼​[∂i2Ψ​(Xr1,…,Xrd)]+∑j=1,j≠id∂1𝒞X​(ri,rj)​𝔼​[∂i∂jΨ​(Xr1,…,Xrd)],\displaystyle\ \ \frac{1}{2}\frac{d}{dr}[{\mathcal{C}^{X}}(r,r)]\big|\_{r=r\_{i}}{\mathbb{E}}[\partial\_{i}^{2}\Psi(X\_{r\_{1}},\dots,X\_{r\_{d}})]+\sum\_{j=1,j\not=i}^{d}\partial\_{1}{\mathcal{C}^{X}}(r\_{i},r\_{j}){\mathbb{E}}[\partial\_{i}\partial\_{j}\Psi(X\_{r\_{1}},\dots,X\_{r\_{d}})], |  |

which is upper bounded by

|  |  |  |
| --- | --- | --- |
|  | C​(ri2​α−2+∑j≠i|rj−ri|2​α−2)≤C​d​((ri−1−ri)2​α−2+(ri−ri+1)2​α−2),C\left(r\_{i}^{2\alpha-2}+\sum\_{j\not=i}|r\_{j}-r\_{i}|^{2\alpha-2}\right)\leq Cd((r\_{i-1}-r\_{i})^{2\alpha-2}+(r\_{i}-r\_{i+1})^{2\alpha-2}), |  |

using that |rj−ri|2​α−2≤(ri−1−ri)2​α−2|r\_{j}-r\_{i}|^{2\alpha-2}\leq(r\_{i-1}-r\_{i})^{2\alpha-2} if j<ij<i and |rj−ri|2​α−2≤(ri−ri+1)2​α−2|r\_{j}-r\_{i}|^{2\alpha-2}\leq(r\_{i}-r\_{i+1})^{2\alpha-2} if j>ij>i. The derivative with respect to rdr\_{d} is handled in the same way.
∎

We obtain easily then the following corollary.

###### Corollary A.5.

Let ϕ\phi be defined by ([3.3](https://arxiv.org/html/2602.18234v1#S3.E3 "In Proof. ‣ 3. Weak error approximation with the cubic test function ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and assume that f∈𝒞exp2​(ℝ,ℝ)f\in\mathcal{C}\_{\exp}^{2}({\mathbb{R}},{\mathbb{R}}). Then, ϕ​(s,t)\phi(s,t) is continuous and continuously differentiable on {(s,t)∈(ℝ+∗)2,s≠t}\{(s,t)\in({\mathbb{R}}\_{+}^{\*})^{2},s\not=t\}. Moreover, there exists C∈ℝ+C\in{\mathbb{R}}\_{+} such that we have for 0≤s,t≤T0\leq s,t\leq T, |ϕ​(s,t)|≤C|\phi(s,t)|\leq C and the following estimates:

1. (1)

   |  |  |  |
   | --- | --- | --- |
   |  | |ϕ​(s,t)−ϕ​(t,t)|≤C​|t−s|2​α−1,|\phi(s,t)-\phi(t,t)|\leq C|t-s|^{2\alpha-1}, |  |
2. (2)

   |  |  |  |
   | --- | --- | --- |
   |  | |∂1ϕ​(s,t)|≤C​((s∧t)2​α−2+|t−s|2​α−2),|\partial\_{1}\phi(s,t)|\leq C\left((s\wedge t)^{2\alpha-2}+|t-s|^{2\alpha-2}\right), |  |
3. (3)

   |  |  |  |
   | --- | --- | --- |
   |  | |∂2ϕ​(s,t)|≤C​(tα−1​(s∧t)2​α−2+|t−s|2​α−2).|\partial\_{2}\phi(s,t)|\leq C\left(t^{\alpha-1}(s\wedge t)^{2\alpha-2}+|t-s|^{2\alpha-2}\right). |  |

###### Proof.

The proof is the same as for Proposition [A.4](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") with Ψ​(x,y)=f​(x)​f​f′​(y)\Psi(x,y)=f(x)ff^{\prime}(y). However, since f∈𝒞exp2​(ℝ,ℝ)f\in\mathcal{C}\_{\exp}^{2}({\mathbb{R}},{\mathbb{R}}), Ψ\Psi may not be 𝒞2\mathcal{C}^{2} and we explain why it still works.

For the Hölder property, we introduce

|  |  |  |
| --- | --- | --- |
|  | Zu∼𝒩​([(1−u)​𝔼​[Xs]+r​𝔼​[Xt]𝔼​[Xt]],(1−u)​[𝒞X​(s,s)𝒞X​(s,t)𝒞X​(s,t)𝒞X​(t,t)]+u​[𝒞X​(t,t)𝒞X​(t,t)𝒞X​(t,t)𝒞X​(t,t)]),Z\_{u}\sim\mathcal{N}\left(\left[\begin{array}[]{c}(1-u){\mathbb{E}}[X\_{s}]+r{\mathbb{E}}[X\_{t}]\\ {\mathbb{E}}[X\_{t}]\end{array}\right],(1-u)\left[\begin{array}[]{cc}{\mathcal{C}^{X}}(s,s)&{\mathcal{C}^{X}}(s,t)\\ {\mathcal{C}^{X}}(s,t)&{\mathcal{C}^{X}}(t,t)\end{array}\right]+u\left[\begin{array}[]{cc}{\mathcal{C}^{X}}(t,t)&{\mathcal{C}^{X}}(t,t)\\ {\mathcal{C}^{X}}(t,t)&{\mathcal{C}^{X}}(t,t)\end{array}\right]\right), |  |

with u∈[0,1]u\in[0,1]. We stress that the second diagonal term of the covariance is constant. Since 𝔼​[∂1Ψ​(Zu)]{\mathbb{E}}[\partial\_{1}\Psi(Z\_{u})], 𝔼​[∂12Ψ​(Zu)]{\mathbb{E}}[\partial^{2}\_{1}\Psi(Z\_{u})], 𝔼​[∂1∂2Ψ​(Zu)]{\mathbb{E}}[\partial\_{1}\partial\_{2}\Psi(Z\_{u})] are bounded, we can thus apply the second part of Lemma [A.6](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (without requiring the boundedness of 𝔼​[∂22Ψ​(Zu)]{\mathbb{E}}[\partial^{2}\_{2}\Psi(Z\_{u})]) and get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ϕ​(t,t)−ϕ​(s,t)|\displaystyle|\phi(t,t)-\phi(s,t)| | ≤C​(|𝔼​[Xt]−𝔼​[Xs]|+|𝒞X​(s,t)−𝒞X​(t,t)|+|𝒞X​(s,s)−𝒞X​(t,t)|)\displaystyle\leq C\left(|{\mathbb{E}}[X\_{t}]-{\mathbb{E}}[X\_{s}]|+|{\mathcal{C}^{X}}(s,t)-{\mathcal{C}^{X}}(t,t)|+|{\mathcal{C}^{X}}(s,s)-{\mathcal{C}^{X}}(t,t)|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(|𝔼​[Xt]−𝔼​[Xs]|+2​|𝒞X​(s,t)−𝒞X​(t,t)|+|𝒞X​(s,s)−𝒞X​(s,t)|),\displaystyle\leq C\left(|{\mathbb{E}}[X\_{t}]-{\mathbb{E}}[X\_{s}]|+2|{\mathcal{C}^{X}}(s,t)-{\mathcal{C}^{X}}(t,t)|+|{\mathcal{C}^{X}}(s,s)-{\mathcal{C}^{X}}(s,t)|\right), |  |

which gives the 2​α−12\alpha-1-Hölder property as in Proposition [A.4](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").
The same remark allows to get also the estimates for ∂1ϕ\partial\_{1}\phi and ∂2ϕ\partial\_{2}\phi.
∎

We state a lemma that slightly extends [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Lemma 2.2] to the non-centered case, and can be seen as a direct application of [[14](https://arxiv.org/html/2602.18234v1#bib.bib14), Theorem 1.9], see also [[15](https://arxiv.org/html/2602.18234v1#bib.bib15), Theorem 2.1].

###### Lemma A.6.

Let a<ba<b, d∈ℕ∗d\in{\mathbb{N}}^{\*}, m:[a,b]→ℝdm:[a,b]\to{\mathbb{R}}^{d} and Σ:[a,b]→ℝd×d\Sigma:[a,b]\to{\mathbb{R}}^{d\times d} be continuously differentiable, such that Σ​(r)\Sigma(r) is positive semidefinite for all r∈[a,b]r\in[a,b].
Let g:ℝd→ℝg:{\mathbb{R}}^{d}\to{\mathbb{R}} be a 𝒞2\mathcal{C}^{2} function such that there exists C>0C>0,

|  |  |  |
| --- | --- | --- |
|  | ∀x∈ℝd,|g​(x)|+∑k=1d|∂kg​(x)|+∑k,l=1d|∂k,l2g​(x)|≤C​eC​|x|.\forall x\in{\mathbb{R}}^{d},|g(x)|+\sum\_{k=1}^{d}|\partial\_{k}g(x)|+\sum\_{k,l=1}^{d}|\partial^{2}\_{k,l}g(x)|\leq Ce^{C|x|}. |  |

Then, φ:[a,b]→ℝ\varphi:[a,b]\to{\mathbb{R}} defined by φ​(r)=𝔼​[g​(Zr)]\varphi(r)={\mathbb{E}}[g(Z\_{r})] with Zr∼𝒩d​(m​(r),Σ​(r))Z\_{r}\sim\mathcal{N}\_{d}(m(r),\Sigma(r)) is 𝒞1\mathcal{C}^{1} and satisfies

|  |  |  |
| --- | --- | --- |
|  | φ​(r)=φ​(a)+∫ar∑k=1dmk′​(s)​𝔼​[∂kg​(Zs)]+12​∑k,l=1dΣk,l′​(s)​𝔼​[∂k,l2g​(Zs)]​d​s,r∈[a,b].\varphi(r)=\varphi(a)+\int\_{a}^{r}\sum\_{k=1}^{d}m^{\prime}\_{k}(s){\mathbb{E}}[\partial\_{k}g(Z\_{s})]+\frac{1}{2}\sum\_{k,l=1}^{d}\Sigma^{\prime}\_{k,l}(s){\mathbb{E}}[\partial^{2}\_{k,l}g(Z\_{s})]ds,\ r\in[a,b]. |  |

Suppose in addition that Σ​(t)k,l\Sigma(t)\_{k,l} is constant for (k,l)∉ℐ⊂{1,…,d}2(k,l)\not\in\mathcal{I}\subset\{1,\dots,d\}^{2}. Then, the same result holds for g∈𝒞1g\in\mathcal{C}^{1} such that for all (k,l)∈ℐ(k,l)\in\mathcal{I}, ∂kg\partial\_{k}g is continuously differentiable with respect to the ll-th coordinate and satisfies

|  |  |  |
| --- | --- | --- |
|  | ∀x∈ℝd,|g​(x)|+∑k=1d|∂kg​(x)|+∑(k,l)∈ℐ|∂k,l2g​(x)|≤C​eC​|x|.\forall x\in{\mathbb{R}}^{d},|g(x)|+\sum\_{k=1}^{d}|\partial\_{k}g(x)|+\sum\_{(k,l)\in\mathcal{I}}|\partial^{2}\_{k,l}g(x)|\leq Ce^{C|x|}. |  |

###### Proof.

Let F​(r,x)=g​(m​(r)+x)F(r,x)=g(m(r)+x). We have ∂rF​(r,x)=∑k=1dmk′​(r)​∂kg​(m​(r)+x)\partial\_{r}F(r,x)=\sum\_{k=1}^{d}m^{\prime}\_{k}(r)\partial\_{k}g(m(r)+x), and thus |∂rF​(r,x)|≤C​eC​|x||\partial\_{r}F(r,x)|\leq Ce^{C|x|} for some constant C>0C>0, since mm is 𝒞1\mathcal{C}^{1} on [a,b][a,b]. We apply then the weak Itô formula [[14](https://arxiv.org/html/2602.18234v1#bib.bib14), Theorem 1.9].

The second statement can be easily deduced by adapting the proof of [[14](https://arxiv.org/html/2602.18234v1#bib.bib14), Theorem 1.9], since the partial derivatives ∂k,l2g​(x)\partial\_{k,l}^{2}g(x) for (k,l)∉ℐ(k,l)\not\in\mathcal{I} no longer appear in the calculations.
∎

###### Corollary A.7.

Let Z1∼𝒩d​(m1,Σ1)Z\_{1}\sim\mathcal{N}\_{d}(m\_{1},\Sigma\_{1}) and Z2∼𝒩d​(m2,Σ2)Z\_{2}\sim\mathcal{N}\_{d}(m\_{2},\Sigma\_{2}) with m1,m2∈ℝdm\_{1},m\_{2}\in{\mathbb{R}}^{d} and Σ1,Σ2\Sigma\_{1},\Sigma\_{2} positive semidefinite matrices. Let gg satisfy the same assumption as in Lemma [A.6](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). Then, for any M>0M>0, there is a constant C∈ℝ+C\in{\mathbb{R}}\_{+} such that

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[g​(Z2)]−𝔼​[g​(Z1)]|≤C​(∑k=1d|(m1−m2)k|+∑k,l=1d|(Σ1−Σ2)k,l|),|{\mathbb{E}}[g(Z\_{2})]-{\mathbb{E}}[g(Z\_{1})]|\leq C\left(\sum\_{k=1}^{d}|(m\_{1}-m\_{2})\_{k}|+\sum\_{k,l=1}^{d}|(\Sigma\_{1}-\Sigma\_{2})\_{k,l}|\right), |  |

for all m1,m2,Σ1,Σ2m\_{1},m\_{2},\Sigma\_{1},\Sigma\_{2} such that max⁡(|m1|,|m2|,|Σ1|,|Σ2|)≤M\max(|m\_{1}|,|m\_{2}|,|\Sigma\_{1}|,|\Sigma\_{2}|)\leq M.

###### Proof.

Let φ​(r)=𝔼​[g​(Zr)]\varphi(r)={\mathbb{E}}[g(Z\_{r})] with Zr∼𝒩d​(r​m1+(1−r)​m2,r​Σ1+(1−r)​Σ2)Z\_{r}\sim\mathcal{N}\_{d}(rm\_{1}+(1-r)m\_{2},r\Sigma\_{1}+(1-r)\Sigma\_{2}) for r∈[0,1]r\in[0,1]. The, we get by Lemma [A.6](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")

|  |  |  |
| --- | --- | --- |
|  | φ​(1)−φ​(0)=∫01∑k=1d(m1−m2)k​𝔼​[∂kg​(Zr)]+12​∑k,l=1d(Σ1−Σ2)k,l​𝔼​[∂k,l2g​(Zr)]​d​r.\varphi(1)-\varphi(0)=\int\_{0}^{1}\sum\_{k=1}^{d}(m\_{1}-m\_{2})\_{k}{\mathbb{E}}[\partial\_{k}g(Z\_{r})]+\frac{1}{2}\sum\_{k,l=1}^{d}(\Sigma\_{1}-\Sigma\_{2})\_{k,l}{\mathbb{E}}[\partial^{2}\_{k,l}g(Z\_{r})]dr. |  |

From the assumption on gg, supr∈[0,1]∑k=1d𝔼​[|∂kg​(Zr)|]+∑k,l=1d𝔼​[|∂k,l2g​(Zr)|]\sup\_{r\in[0,1]}\sum\_{k=1}^{d}{\mathbb{E}}[|\partial\_{k}g(Z\_{r})|]+\sum\_{k,l=1}^{d}{\mathbb{E}}[|\partial^{2}\_{k,l}g(Z\_{r})|] is bounded by a constant depending on MM. We then get the claim.
∎

## Appendix B Technical proofs

###### Proof of Theorem [2.6](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

We first observe that 𝔼​[Xt​(Xu−Xη​(u))]=𝔼​[Xt]​𝔼​[(Xu−Xη​(u))]+𝔼​[𝒴t​(Xu−Xη​(u))]{\mathbb{E}}[X\_{t}(X\_{u}-X\_{\eta(u)})]={\mathbb{E}}[X\_{t}]{\mathbb{E}}[(X\_{u}-X\_{\eta(u)})]+{\mathbb{E}}[\mathcal{Y}\_{t}(X\_{u}-X\_{\eta(u)})]. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | max1≤k≤n⁡|∫0tk(tk−u)α−1Γ​(α)​𝔼​[Xt​(Xu−Xη​(u))]​𝑑u|≤\displaystyle\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{t}(X\_{u}-X\_{\eta(u)})]du\right|\leq | |𝔼​[Xt]|​max1≤k≤n⁡|∫0tk(tk−u)α−1Γ​(α)​𝔼​[Xu−Xη​(u)]​𝑑u|\displaystyle|{\mathbb{E}}[X\_{t}]|\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{u}-X\_{\eta(u)}]du\right| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +max1≤k≤n⁡|∫0tk(tk−u)α−1Γ​(α)​𝔼​[𝒴t​(Xu−Xη​(u))]​𝑑u|.\displaystyle+\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[\mathcal{Y}\_{t}(X\_{u}-X\_{\eta(u)})]du\right|. |  | (B.1) |

We use the estimate |∫0tk(tk−u)α−1Γ​(α)​(𝔼​[Xu]−𝔼​[Xη​(u)])​𝑑u|≤CTn\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}({\mathbb{E}}[X\_{u}]-{\mathbb{E}}[X\_{\eta(u)}])du\right|\leq\frac{C\_{T}}{n} (see Equation ([2.13](https://arxiv.org/html/2602.18234v1#S2.E13 "In Proof of Theorem 2.7. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))) for some CT∈ℝ+C\_{T}\in{\mathbb{R}}\_{+}. By Proposition [2.1](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem1 "Proposition 2.1. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), |𝔼​[Xt]||{\mathbb{E}}[X\_{t}]| is bounded uniformly on t∈[0,T]t\in[0,T], and we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀t∈[0,T],|𝔼​[Xt]|​max1≤k≤n⁡|∫0tk(tk−u)α−1Γ​(α)​𝔼​[Xu−Xη​(u)]​𝑑u|≤CTn,\forall t\in[0,T],\ |{\mathbb{E}}[X\_{t}]|\max\_{1\leq k\leq n}\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[X\_{u}-X\_{\eta(u)}]du\right|\leq\frac{C\_{T}}{n}, |  | (B.2) |

where CTC\_{T} is a constant depending on TT and on X0X\_{0}, κ1\kappa\_{1}, κ2\kappa\_{2}, σ\sigma and α\alpha, that may change from line to line.

We are thus interested in studying 𝔼​[𝒴t​(Xu−Xη​(u))]=𝒞X​(t,u)−𝒞X​(t,η​(u)){\mathbb{E}}[\mathcal{Y}\_{t}(X\_{u}-X\_{\eta(u)})]={\mathcal{C}^{X}}(t,u)-{\mathcal{C}^{X}}(t,\eta(u)). For ξ∈[0,Tα]\xi\in[0,T^{\alpha}], let222Note that this change of variable allows us to get tα−1t^{\alpha-1} instead of t2​α−2t^{2\alpha-2} that appears from a direct application of Lemma [A.3](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"). gt​(ξ)=𝒞X​(t,ξ1/α)g\_{t}(\xi)={\mathcal{C}^{X}}(t,\xi^{1/\alpha}). We have gt′​(ξ)=1α​ξ1/α−1​∂2𝒞X​(t,ξ1/α)g^{\prime}\_{t}(\xi)=\frac{1}{\alpha}\xi^{1/\alpha-1}\partial\_{2}{\mathcal{C}^{X}}(t,\xi^{1/\alpha}), and by Lemma [A.3](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), we get

|  |  |  |
| --- | --- | --- |
|  | ∀ξ∈(0,T),|gt′​(ξ)|≤CT​(tα−1+|t−ξ1/α|2​α−2).\forall\xi\in(0,T),\ |g^{\prime}\_{t}(\xi)|\leq C\_{T}(t^{\alpha-1}+|t-\xi^{1/\alpha}|^{2\alpha-2}). |  |

We have

|  |  |  |
| --- | --- | --- |
|  | |∫0tk(tk−u)α−1Γ​(α)​𝔼​[𝒴t​(Xu−Xη​(u))]​𝑑u|\displaystyle\left|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}{\mathbb{E}}[\mathcal{Y}\_{t}(X\_{u}-X\_{\eta(u)})]du\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0tk(tk−u)α−1Γ​(α)​|gt​(uα)−gt​(η​(u)α)|​𝑑u=∑i=1k∫ti−1ti(tk−u)α−1Γ​(α)​|gt​(uα)−gt​(ti−1α)|​𝑑u\displaystyle\leq\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}|g\_{t}(u^{\alpha})-g\_{t}(\eta(u)^{\alpha})|du=\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}|g\_{t}(u^{\alpha})-g\_{t}(t\_{i-1}^{\alpha})|du |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=1k∫ti−1ti(tk−u)α−1Γ​(α)​(uα−ti−1α)​|∫01gt′​(z​uα+(1−z)​ti−1α)​𝑑z|​𝑑u\displaystyle=\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}(u^{\alpha}-t\_{i-1}^{\alpha})\left|\int\_{0}^{1}g\_{t}^{\prime}(zu^{\alpha}+(1-z)t\_{i-1}^{\alpha})dz\right|du |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∑i=1k∫ti−1ti(tk−u)α−1Γ​(α)​(uα−ti−1α)​∫01CT​(tα−1+|t−(z​uα+(1−z)​ti−1α)1/α|2​α−2)​𝑑z​𝑑u\displaystyle\leq\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}(u^{\alpha}-t\_{i-1}^{\alpha})\int\_{0}^{1}C\_{T}\left(t^{\alpha-1}+\left|t-(zu^{\alpha}+(1-z)t\_{i-1}^{\alpha})^{1/\alpha}\right|^{2\alpha-2}\right)dzdu |  |
|  |  |  |
| --- | --- | --- |
|  | =:𝒜+ℬ.\displaystyle=:\mathcal{A}+\mathcal{B}. |  |

The first term 𝒜:=CT​tα−1​∑i=1k∫ti−1ti(tk−u)α−1Γ​(α)​(uα−ti−1α)​𝑑u=CT​tα−1​∫0tk(tk−u)α−1Γ​(α)​(uα−η​(u)α)​𝑑u≤CT​tα−1​tk2​α−1n≤CT​tα−1n\mathcal{A}:=C\_{T}t^{\alpha-1}\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}(u^{\alpha}-t\_{i-1}^{\alpha})du=C\_{T}t^{\alpha-1}\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}(u^{\alpha}-\eta(u)^{\alpha})du\leq C\_{T}t^{\alpha-1}\frac{t\_{k}^{2\alpha-1}}{n}\leq\frac{C\_{T}t^{\alpha-1}}{n} by using [[8](https://arxiv.org/html/2602.18234v1#bib.bib8), Theorem 2.4 (b)].
The second term is equal to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ:=\displaystyle\mathcal{B}:= | ∑i=1k∫ti−1ti(tk−u)α−1Γ​(α)​(uα−ti−1α)​∫01CT​|t−(z​uα+(1−z)​ti−1α)1/α|2​α−2​𝑑z​𝑑u\displaystyle\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}(u^{\alpha}-t\_{i-1}^{\alpha})\int\_{0}^{1}C\_{T}\left|t-(zu^{\alpha}+(1-z)t\_{i-1}^{\alpha})^{1/\alpha}\right|^{2\alpha-2}dzdu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1k∫ti−1ti(tk−u)α−1Γ​(α)​(uα−ti−1α)​∫ti−1uCT​|t−v|2​α−2​d​v1α​(uα−ti−1α)​v1−α​𝑑u\displaystyle=\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}(u^{\alpha}-t\_{i-1}^{\alpha})\int\_{t\_{i-1}}^{u}C\_{T}\left|t-v\right|^{2\alpha-2}\frac{dv}{\frac{1}{\alpha}(u^{\alpha}-t\_{i-1}^{\alpha})v^{1-\alpha}}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1k∫ti−1tiα​(tk−u)α−1Γ​(α)​∫ti−1uCT​vα−1​|t−v|2​α−2​𝑑v​𝑑u\displaystyle=\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{\alpha(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\int\_{t\_{i-1}}^{u}C\_{T}v^{\alpha-1}\left|t-v\right|^{2\alpha-2}dvdu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i=1k∫ti−1tiα​(tk−u)α−1Γ​(α)​∫ti−1tiCT​vα−1​|t−v|2​α−2​𝑑v​𝑑u\displaystyle\leq\sum\_{i=1}^{k}\int\_{t\_{i-1}}^{t\_{i}}\frac{\alpha(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\int\_{t\_{i-1}}^{t\_{i}}C\_{T}v^{\alpha-1}\left|t-v\right|^{2\alpha-2}dvdu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =CTΓ​(α)​∑i=1k((tk−ti−1)α−(tk−ti)α)​∫ti−1tivα−1​|t−v|2​α−2​𝑑v.\displaystyle=\frac{C\_{T}}{\Gamma(\alpha)}\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\int\_{t\_{i-1}}^{t\_{i}}v^{\alpha-1}\left|t-v\right|^{2\alpha-2}dv. |  |

Next, we use

|  |  |  |
| --- | --- | --- |
|  | vα−1​|t−v|2​α−2≤(t2)α−1​|t−v|2​α−2+(t2)2​α−2​vα−1,v^{\alpha-1}\left|t-v\right|^{2\alpha-2}\leq\left(\frac{t}{2}\right)^{\alpha-1}\left|t-v\right|^{2\alpha-2}+\left(\frac{t}{2}\right)^{2\alpha-2}v^{\alpha-1}, |  |

since vα−1​|t−v|2​α−2≤(t2)α−1​|t−v|2​α−2v^{\alpha-1}\left|t-v\right|^{2\alpha-2}\leq\left(\frac{t}{2}\right)^{\alpha-1}\left|t-v\right|^{2\alpha-2} for v≥t/2v\geq t/2 and vα−1​|t−v|2​α−2≤(t2)2​α−2​vα−1v^{\alpha-1}\left|t-v\right|^{2\alpha-2}\leq\left(\frac{t}{2}\right)^{2\alpha-2}v^{\alpha-1} for v∈(0,t/2)v\in(0,t/2).
This gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ≤ℬ1+ℬ2,\mathcal{B}\leq\mathcal{B}\_{1}+\mathcal{B}\_{2}, |  | (B.3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ1\displaystyle\mathcal{B}\_{1} | :=(t2)2​α−2​CTΓ​(α)​∑i=1k((tk−ti−1)α−(tk−ti)α)​∫ti−1tivα−1​𝑑v\displaystyle:=\left(\frac{t}{2}\right)^{2\alpha-2}\frac{C\_{T}}{\Gamma(\alpha)}\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\int\_{t\_{i-1}}^{t\_{i}}v^{\alpha-1}dv |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ2\displaystyle\mathcal{B}\_{2} | :=(t2)α−1​CTΓ​(α)​∑i=1k((tk−ti−1)α−(tk−ti)α)​∫ti−1ti|t−v|2​α−2​𝑑v.\displaystyle:=\left(\frac{t}{2}\right)^{\alpha-1}\frac{C\_{T}}{\Gamma(\alpha)}\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\int\_{t\_{i-1}}^{t\_{i}}\left|t-v\right|^{2\alpha-2}dv. |  |

On the one hand, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ1≤\displaystyle\mathcal{B}\_{1}\leq | (t2)2​α−2​CTΓ​(α)​∑i=1k((tk−ti−1)α−(tk−ti)α)​∫ti−1tivα−1​𝑑v\displaystyle\left(\frac{t}{2}\right)^{2\alpha-2}\frac{C\_{T}}{\Gamma(\alpha)}\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\int\_{t\_{i-1}}^{t\_{i}}v^{\alpha-1}dv |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (t2)2​α−2​CTα​Γ​(α)​∑i=1k((tk−ti−1)α−(tk−ti)α)​(tiα−ti−1α)\displaystyle\left(\frac{t}{2}\right)^{2\alpha-2}\frac{C\_{T}}{\alpha\Gamma(\alpha)}\sum\_{i=1}^{k}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\left(t\_{i}^{\alpha}-t\_{i-1}^{\alpha}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CT​t2​α−2​k2​α−1n2​α≤CT​t2​α−2n,\displaystyle C\_{T}\frac{t^{2\alpha-2}k^{2\alpha-1}}{n^{2\alpha}}\leq C\_{T}\frac{t^{2\alpha-2}}{n}, |  | (B.4) |

by Lemma [A.2](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"), using that 2​α>12\alpha>1 and k≤nk\leq n.

On the other hand, we use the following equality for ℬ2\mathcal{B}\_{2}:

|  |  |  |
| --- | --- | --- |
|  | ∫ti−1ti|t−v|2​α−2​𝑑v=12​α−1×{(t−ti−1)2​α−1−(t−ti)2​α−1​ if ​ti≤t(ti−t)2​α−1+(t−ti−1)2​α−1​ if ​ti−1≤t<ti(ti−t)2​α−1−(ti−1−t)2​α−1​ if ​ti−1>t.\int\_{t\_{i-1}}^{t\_{i}}\left|t-v\right|^{2\alpha-2}dv=\frac{1}{2\alpha-1}\times\begin{cases}(t-t\_{i-1})^{2\alpha-1}-(t-t\_{i})^{2\alpha-1}\text{ if }t\_{i}\leq t\\ (t\_{i}-t)^{2\alpha-1}+(t-t\_{i-1})^{2\alpha-1}\text{ if }t\_{i-1}\leq t<t\_{i}\\ (t\_{i}-t)^{2\alpha-1}-(t\_{i-1}-t)^{2\alpha-1}\text{ if }t\_{i-1}>t.\end{cases} |  |

We then split the sum defining ℬ2\mathcal{B}\_{2} in three terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ2=∑i=1kai,k\displaystyle\mathcal{B}\_{2}=\sum\_{i=1}^{k}a\_{i,k} | =∑i=1,ti≤tkai,k+∑i=1,ti−1>tkai,k+𝟏k≥𝐢​(t)+1​a𝐢​(t)+1,k\displaystyle=\sum\_{i=1,t\_{i}\leq t}^{k}a\_{i,k}+\sum\_{i=1,t\_{i-1}>t}^{k}a\_{i,k}+\mathbf{1}\_{k\geq{\bf i}(t)+1}a\_{{\bf i}(t)+1,k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1min⁡(k,𝐢​(t))ai,k+∑i=𝐢​(t)+2kai,k+𝟏k≥𝐢​(t)+1a𝐢​(t)+1,k=:ℬ21+ℬ22+ℬ23,\displaystyle=\sum\_{i=1}^{\min(k,{\bf i}(t))}a\_{i,k}+\sum\_{i={\bf i}(t)+2}^{k}a\_{i,k}+\mathbf{1}\_{k\geq{\bf i}(t)+1}a\_{{\bf i}(t)+1,k}=:\mathcal{B}\_{21}+\mathcal{B}\_{22}+\mathcal{B}\_{23}, |  |

where 𝐢​(t)∈{0,…,n}{\bf i}(t)\in\{0,\dots,n\} is the index such that η​(t)=t𝐢​(t)\eta(t)=t\_{{\bf i}(t)} for t∈[0,T]t\in[0,T] and setting ai,k=(t2)α−1​CTΓ​(α)​((tk−ti−1)α−(tk−ti)α)​∫ti−1ti|t−v|2​α−2​𝑑va\_{i,k}=\left(\frac{t}{2}\right)^{\alpha-1}\frac{C\_{T}}{\Gamma(\alpha)}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\int\_{t\_{i-1}}^{t\_{i}}\left|t-v\right|^{2\alpha-2}dv, with using the standard convention ∑i=i1i2ai,k=0\sum\_{i=i\_{1}}^{i\_{2}}a\_{i,k}=0 if i2<i1i\_{2}<i\_{1}.

∙\bullet Term ℬ21\mathcal{B}\_{21}: Since t↦(t−ti−1)2​α−1−(t−ti)2​α−1t\mapsto(t-t\_{i-1})^{2\alpha-1}-(t-t\_{i})^{2\alpha-1} is decreasing for t≥tit\geq t\_{i},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i≤k,ti≤t((tk−ti−1)α−(tk−ti)α)​((t−ti−1)2​α−1−(t−ti)2​α−1)\displaystyle\sum\_{i\leq k,t\_{i}\leq t}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\left((t-t\_{i-1})^{2\alpha-1}-(t-t\_{i})^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∑i≤k,ti≤t((tk−ti−1)α−(tk−ti)α)(η(t)−ti−1)2​α−1−(η(t)−ti)2​α−1)\displaystyle\sum\_{i\leq k,t\_{i}\leq t}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\left(\eta(t)-t\_{i-1})^{2\alpha-1}-(\eta(t)-t\_{i})^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (Tn)3​α−1​∑i=1min⁡(k,𝐢​(t))((k−i+1)α−(k−i)α)​((𝐢​(t)−i+1)2​α−1−(𝐢​(t)−i)2​α−1)\displaystyle\left(\frac{T}{n}\right)^{3\alpha-1}\sum\_{i=1}^{\min(k,{\bf i}(t))}\left((k-i+1)^{\alpha}-(k-{i})^{\alpha}\right)\left(({\bf i}(t)-i+1)^{2\alpha-1}-({\bf i}(t)-{i})^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CTn3​α−1​∑i=1min⁡(k,𝐢​(t))(k−i+1)α−1​(𝐢​(t)−i+1)2​α−2​ by ([A.1](https://arxiv.org/html/2602.18234v1#A1.E1 "In Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))\displaystyle\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i=1}^{\min(k,{\bf i}(t))}(k-i+1)^{\alpha-1}({\bf i}(t)-i+1)^{2\alpha-2}\text{ by~\eqref{eq\_LiZeng}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CTn3​α−1​∑i=1min⁡(k,𝐢​(t))(min⁡(k,𝐢​(t))−i+1)3​α−3=CTn3​α−1​∑i=1min⁡(k,𝐢​(t))i3​α−3≤CTn3​α−1​∑i=1ni3​α−3.\displaystyle\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i=1}^{\min(k,{\bf i}(t))}(\min(k,{\bf i}(t))-i+1)^{3\alpha-3}=\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i=1}^{\min(k,{\bf i}(t))}i^{3\alpha-3}\leq\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i=1}^{n}i^{3\alpha-3}. |  |

We now observe that ∑i=1ni3​α−3=O​(n3​α−2)\sum\_{i=1}^{n}i^{3\alpha-3}=O(n^{3\alpha-2}) for α>2/3\alpha>2/3, ∑i=1ni3​α−3=O​(log⁡(n))\sum\_{i=1}^{n}i^{3\alpha-3}=O(\log(n)) for α=2/3\alpha=2/3, and ∑i=1ni3​α−3=O​(1)\sum\_{i=1}^{n}i^{3\alpha-3}=O(1) for 1/2<α<2/31/2<\alpha<2/3. This gives

|  |  |  |
| --- | --- | --- |
|  | ℬ21≤CT​tα−1​𝐯n​(α).\mathcal{B}\_{21}\leq C\_{T}t^{\alpha-1}{\bf v}\_{n}(\alpha). |  |

∙\bullet Term ℬ22\mathcal{B}\_{22}: Similarly, since t↦(ti−t)2​α−1−(ti−1−t)2​α−1t\mapsto(t\_{i}-t)^{2\alpha-1}-(t\_{i-1}-t)^{2\alpha-1} is increasing for t<ti−1t<t\_{i-1}, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i≤k,t<ti−1((tk−ti−1)α−(tk−ti)α)​((ti−t)2​α−1−(ti−1−t)2​α−1)\displaystyle\sum\_{i\leq k,t<t\_{i-1}}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\left((t\_{i}-t)^{2\alpha-1}-(t\_{i-1}-t)^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∑i≤k,t<ti−1((tk−ti−1)α−(tk−ti)α)​((ti−t𝐢​(t)+1)2​α−1−(ti−1−t𝐢​(t)+1)2​α−1)\displaystyle\sum\_{i\leq k,t<t\_{i-1}}\left((t\_{k}-t\_{i-1})^{\alpha}-(t\_{k}-t\_{i})^{\alpha}\right)\left((t\_{i}-t\_{{\bf i}(t)+1})^{2\alpha-1}-(t\_{i-1}-t\_{{\bf i}(t)+1})^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | CTn3​α−1​∑i=η​(t)+2k((k−i+1)α−(k−i)α)​((i−𝐢​(t)−1)2​α−1−(i−𝐢​(t)−2)2​α−1)\displaystyle\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i=\eta(t)+2}^{k}\left((k-i+1)^{\alpha}-(k-i)^{\alpha}\right)\left((i-{\bf i}(t)-1)^{2\alpha-1}-(i-{\bf i}(t)-2)^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | CTn3​α−1​∑i=𝐢​(t)+2k(k−i+1)α−1​(i−𝐢​(t)−1)2​α−2​ by ([A.1](https://arxiv.org/html/2602.18234v1#A1.E1 "In Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))\displaystyle\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i={\bf i}(t)+2}^{k}(k-i+1)^{\alpha-1}(i-{\bf i}(t)-1)^{2\alpha-2}\text{ by~\eqref{eq\_LiZeng}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | CTn3​α−1​∑i=1k−𝐢​(t)−1(k−𝐢​(t)−i)α−1​i2​α−2\displaystyle\frac{C\_{T}}{n^{3\alpha-1}}\sum\_{i=1}^{k-{\bf i}(t)-1}(k-{\bf i}(t)-i)^{\alpha-1}i^{2\alpha-2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝟏k≥𝐢​(t)+2​CTn3​α−1​(k−𝐢​(t)−1)3​α−2,\displaystyle\mathbf{1}\_{k\geq{\bf i}(t)+2}\frac{C\_{T}}{n^{3\alpha-1}}(k-{\bf i}(t)-1)^{3\alpha-2}, |  |

where we used Lemma [A.1](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") for the last inequality.
Therefore, we get

|  |  |  |
| --- | --- | --- |
|  | ℬ22≤CT​tα−1​𝐯n​(α),\mathcal{B}\_{22}\leq C\_{T}t^{\alpha-1}{\bf v}\_{n}(\alpha), |  |

by using that k−𝐢​(t)−1≤nk-{\bf i}(t)-1\leq n for 3​α−2>03\alpha-2>0 and 𝟏k≥𝐢​(t)+2​(k−𝐢​(t)−1)3​α−2≤1\mathbf{1}\_{k\geq{\bf i}(t)+2}(k-{\bf i}(t)-1)^{3\alpha-2}\leq 1 for 3​α−2≤03\alpha-2\leq 0.

∙\bullet Term ℬ23\mathcal{B}\_{23}: We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ23=\displaystyle\mathcal{B}\_{23}= | 𝟏k≥𝐢​(t)+1​(t2)α−1​CT(2​α−1)​Γ​(α)​((tk−η​(t))α−(tk−t𝐢​(t)+1)α)​((t𝐢​(t)+1−t)2​α−1+(t−η​(t))2​α−1)\displaystyle\mathbf{1}\_{k\geq{\bf i}(t)+1}\left(\frac{t}{2}\right)^{\alpha-1}\frac{C\_{T}}{(2\alpha-1)\Gamma(\alpha)}\left((t\_{k}-\eta(t))^{\alpha}-(t\_{k}-t\_{{\bf i}(t)+1})^{\alpha}\right)\left((t\_{{\bf i}(t)+1}-t)^{2\alpha-1}+(t-\eta(t))^{2\alpha-1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝟏k≥𝐢​(t)+1​CT​tα−1​(t𝐢​(t)+1−η​(t))αn2​α−1≤CT​tα−1​1n3​α−1≤CT​tα−1​𝐯n​(α),\displaystyle\leq\mathbf{1}\_{k\geq{\bf i}(t)+1}C\_{T}t^{\alpha-1}\frac{(t\_{{\bf i}(t)+1}-\eta(t))^{\alpha}}{n^{2\alpha-1}}\leq C\_{T}t^{\alpha-1}\frac{1}{n^{3\alpha-1}}\leq C\_{T}t^{\alpha-1}{\bf v}\_{n}(\alpha), |  |

by using the α\alpha-Hölder inequality and also that 2​α−1>02\alpha-1>0 and max⁡(t−η​(t),t𝐢​(t)+1−t)≤T/n\max(t-\eta(t),t\_{{\bf i}(t)+1}-t)\leq T/n. Gathering all the terms, we get

|  |  |  |
| --- | --- | --- |
|  | ℬ2=ℬ21+ℬ22+ℬ23≤CT​tα−1​𝐯n​(α).\mathcal{B}\_{2}=\mathcal{B}\_{21}+\mathcal{B}\_{22}+\mathcal{B}\_{23}\leq C\_{T}t^{\alpha-1}{\bf v}\_{n}(\alpha). |  |

From ([B.1](https://arxiv.org/html/2602.18234v1#A2.E1 "In Proof of Theorem 2.6. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we get the claim by using ([B.2](https://arxiv.org/html/2602.18234v1#A2.E2 "In Proof of Theorem 2.6. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), ([B.3](https://arxiv.org/html/2602.18234v1#A2.E3 "In Proof of Theorem 2.6. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), ([B.4](https://arxiv.org/html/2602.18234v1#A2.E4 "In Proof of Theorem 2.6. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) with the last inequality and tα−1≤1+t2​α−2t^{\alpha-1}\leq 1+t^{2\alpha-2} since α≤1\alpha\leq 1.
∎

###### Proof of Lemma [2.11](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem11 "Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

Let us first check by induction that Xˇntk∈𝔻1,2{\check{X}^{n}}\_{t\_{k}}\in\mathbb{D}^{1,2} so that 𝒟s​Xˇntk\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}} is well defined. For k=1k=1, we have Xˇnt1=x0+(κ1+κ2​x0)​t1αΓ​(α+1)+σ​∫0t1(t1−s)α−1Γ​(α)​𝑑Ws{\check{X}^{n}}\_{t\_{1}}=x\_{0}+(\kappa\_{1}+\kappa\_{2}x\_{0})\frac{t\_{1}^{\alpha}}{\Gamma(\alpha+1)}+\sigma\int\_{0}^{t\_{1}}\frac{(t\_{1}-s)^{\alpha-1}}{\Gamma(\alpha)}dW\_{s} and thus 𝒟s​Xˇnt1=𝟏s<t1​(t1−s)α−1Γ​(α)\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{1}}=\mathbf{1}\_{s<t\_{1}}\frac{(t\_{1}-s)^{\alpha-1}}{\Gamma(\alpha)}, which is deterministic and satisfies ∫0t1(𝒟s​Xˇnt1)2​𝑑s<∞\int\_{0}^{t\_{1}}(\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{1}})^{2}ds<\infty. Next, we proceed by induction on kk from the dynamics ([1.2](https://arxiv.org/html/2602.18234v1#S1.E2 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) on Xˇn{\check{X}^{n}}. Then, we necessarily have 𝒟s​Xˇntk=∑j=1k−1(∫tjtj+1(tk−u)α−1Γ​(α)​𝑑u)​𝒟s​Xˇntj+σ​(tk−s)α−1Γ​(α)\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}=\sum\_{j=1}^{k-1}\left(\int\_{t\_{j}}^{t\_{j+1}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du\right)\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{j}}+\sigma\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}, which gives that ∫0tk(𝒟s​Xˇntk)2​𝑑s<∞\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}})^{2}ds<\infty by using ∫0tk(tk−s)2​α−2​𝑑s<∞\int\_{0}^{t\_{k}}(t\_{k}-s)^{2\alpha-2}ds<\infty and the induction hypothesis. Therefore,
𝒟s​Xˇntk\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}} is well defined, deterministic, and satisfies ([2.14](https://arxiv.org/html/2602.18234v1#S2.E14 "In Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

From ([1.1](https://arxiv.org/html/2602.18234v1#S1.E1 "In 1. Introduction ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), we also easily get

|  |  |  |
| --- | --- | --- |
|  | 𝒟s​Xtk=κ2​∫0tk𝒟s​Xu​(tk−u)α−1Γ​(α)​𝑑u+σ​(tk−s)α−1Γ​(α).\mathcal{D}\_{s}X\_{t\_{k}}=\kappa\_{2}\int\_{0}^{t\_{k}}\mathcal{D}\_{s}X\_{u}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du+\sigma\frac{(t\_{k}-s)^{\alpha-1}}{\Gamma(\alpha)}. |  |

Combined with ([2.14](https://arxiv.org/html/2602.18234v1#S2.E14 "In Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")), this gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟s​Xtk−𝒟s​Xˇntk\displaystyle\mathcal{D}\_{s}X\_{t\_{k}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}} | =κ2​∫0tk(𝒟s​Xη​(u)−𝒟s​Xˇnη​(u))​(tk−u)α−1Γ​(α)​𝑑u+κ2​∫0tk(𝒟s​Xu−𝒟s​Xη​(u))​(tk−u)α−1Γ​(α)​𝑑u\displaystyle=\kappa\_{2}\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}X\_{\eta(u)}-\mathcal{D}\_{s}{\check{X}^{n}}\_{\eta(u)})\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du+\kappa\_{2}\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)})\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =κ2​∑i=1k−1ci,k​(𝒟s​Xti−𝒟s​Xˇnti)+κ2​∫0tk(𝒟s​Xu−𝒟s​Xη​(u))​(tk−u)α−1Γ​(α)​𝑑u,\displaystyle=\kappa\_{2}\sum\_{i=1}^{k-1}c\_{i,k}(\mathcal{D}\_{s}X\_{t\_{i}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{i}})+\kappa\_{2}\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)})\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du, |  | (B.5) |

with ci,k=∫titi+1(tk−u)α−1Γ​(α)​𝑑uc\_{i,k}=\int\_{t\_{i}}^{t\_{i+1}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}du. We integrate on [0,tj][0,t\_{j}], set I​Δj,k=∫0tj(𝒟s​Xˇntk−𝒟s​Xtk)​𝑑sI\Delta\_{j,k}=\int\_{0}^{t\_{j}}\left(\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}-\mathcal{D}\_{s}X\_{t\_{k}}\right)ds and get for j≤kj\leq k,

|  |  |  |
| --- | --- | --- |
|  | I​Δj,k=κ2​∑i=1k−1ci,k​I​Δj,i+κ2​∫0tj∫0tk(𝒟s​Xu−𝒟s​Xη​(u))​(tk−u)α−1Γ​(α)​𝑑u​𝑑s.I\Delta\_{j,k}=\kappa\_{2}\sum\_{i=1}^{k-1}c\_{i,k}I\Delta\_{j,i}+\kappa\_{2}\int\_{0}^{t\_{j}}\int\_{0}^{t\_{k}}(\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)})\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}duds. |  |

Then, we get

|  |  |  |
| --- | --- | --- |
|  | |I​Δj,k|≤|κ2|​∑i=1k−1ci,k​|I​Δj,i|+|κ2|​∫0tk(tk−u)α−1Γ​(α)​|∫0tj(𝒟s​Xu−𝒟s​Xη​(u))​𝑑s|​𝑑u.|I\Delta\_{j,k}|\leq|\kappa\_{2}|\sum\_{i=1}^{k-1}c\_{i,k}|I\Delta\_{j,i}|+|\kappa\_{2}|\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\left|\int\_{0}^{t\_{j}}(\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)})ds\right|du. |  |

So, by a Grönwall type inequality [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.4], it is sufficient to check that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮j,k:=∫0tk(tk−u)α−1Γ​(α)​|∫0tj(𝒟s​Xu−𝒟s​Xη​(u))​𝑑s|​𝑑u≤C​Tn,\mathcal{S}\_{j,k}:=\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\left|\int\_{0}^{t\_{j}}(\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)})ds\right|du\leq C\frac{T}{n}, |  | (B.6) |

for a constant CC that does not depend on 0≤j≤k≤n0\leq j\leq k\leq n.
We have by Lemma [2.2](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1. The rough Ornstein-Uhlenbeck process ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tj(𝒟sXu\displaystyle\int\_{0}^{t\_{j}}(\mathcal{D}\_{s}X\_{u} | −𝒟sXη​(u))ds={σ​∑i=1∞κ2i−1​ui​α−η​(u)i​αΓ​(i​α+1)​ for ​u≤tj,σ∑i=1∞κ2i−1ui​α−(u−tj)i​α−(η​(u)i​α−(η​(u)−tj)i​α)Γ​(i​α+1) for u∈]tj,tk],\displaystyle-\mathcal{D}\_{s}X\_{\eta(u)})ds=\begin{cases}\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{u^{i\alpha}-\eta(u)^{i\alpha}}{\Gamma(i\alpha+1)}\text{ for }u\leq t\_{j},\\ \sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{u^{i\alpha}-(u-t\_{j})^{i\alpha}-(\eta(u)^{i\alpha}-(\eta(u)-t\_{j})^{i\alpha})}{\Gamma(i\alpha+1)}\text{ for }u\in]t\_{j},t\_{k}],\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =σ​∑i=1∞κ2i−1​ui​α−η​(u)i​αΓ​(i​α+1)−𝟏u>tj​σ​∑i=1∞κ2i−1​(u−tj)i​α−(η​(u)−tj)i​αΓ​(i​α+1).\displaystyle=\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{u^{i\alpha}-\eta(u)^{i\alpha}}{\Gamma(i\alpha+1)}-\mathbf{1}\_{u>t\_{j}}\sigma\sum\_{i=1}^{\infty}\kappa\_{2}^{i-1}\frac{(u-t\_{j})^{i\alpha}-(\eta(u)-t\_{j})^{i\alpha}}{\Gamma(i\alpha+1)}. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮j,k≤\displaystyle\mathcal{S}\_{j,k}\leq | ∫0tk(tk−u)α−1Γ​(α)​∑i=1∞|κ2|i−1​ui​α−η​(u)i​αΓ​(i​α+1)​d​u\displaystyle\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\frac{u^{i\alpha}-\eta(u)^{i\alpha}}{\Gamma(i\alpha+1)}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tjtk(tk−u)α−1Γ​(α)​∑i=1∞|κ2|i−1​(u−tj)i​α−(η​(u)−tj)i​αΓ​(i​α+1)​d​u\displaystyle+\int\_{t\_{j}}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\frac{(u-t\_{j})^{i\alpha}-(\eta(u)-t\_{j})^{i\alpha}}{\Gamma(i\alpha+1)}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫0tk(tk−u)α−1Γ​(α)​∑i=1∞|κ2|i−1​ui​α−η​(u)i​αΓ​(i​α+1)​d​u\displaystyle\int\_{0}^{t\_{k}}\frac{(t\_{k}-u)^{\alpha-1}}{\Gamma(\alpha)}\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\frac{u^{i\alpha}-\eta(u)^{i\alpha}}{\Gamma(i\alpha+1)}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0tk−j(tk−j−u)α−1Γ​(α)​∑i=1∞|κ2|i−1​ui​α−η​(u)i​αΓ​(i​α+1)​d​u.\displaystyle+\int\_{0}^{t\_{k-j}}\frac{(t\_{k-j}-u)^{\alpha-1}}{\Gamma(\alpha)}\sum\_{i=1}^{\infty}|\kappa\_{2}|^{i-1}\frac{u^{i\alpha}-\eta(u)^{i\alpha}}{\Gamma(i\alpha+1)}du. |  |

We separate the term i=1i=1 from z​(u):=∑i=2∞|κ2|i−1​ui​αΓ​(i​α+1)z(u):=\sum\_{i=2}^{\infty}|\kappa\_{2}|^{i-1}\frac{u^{i\alpha}}{\Gamma(i\alpha+1)} which is a 𝒞1​([0,T])\mathcal{C}^{1}([0,T]) function and apply respectively [[8](https://arxiv.org/html/2602.18234v1#bib.bib8), Theorem 2.4 (b) and (a)] to get |𝒮j,k|≤Tn​(C​T2​α−1+‖z′‖∞α​Tα)|\mathcal{S}\_{j,k}|\leq\frac{T}{n}\left(CT^{2\alpha-1}+\frac{\|z^{\prime}\|\_{\infty}}{\alpha}T^{\alpha}\right) and thus ([B.6](https://arxiv.org/html/2602.18234v1#A2.E6 "In Proof of Lemma 2.11. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")).

For the last inequality, we set Ij,k=∫0tj|𝒟s​Xˇntk|​𝑑sI\_{j,k}=\int\_{0}^{t\_{j}}|\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{k}}|ds and we obtain from ([2.14](https://arxiv.org/html/2602.18234v1#S2.E14 "In Lemma 2.11. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models"))

|  |  |  |
| --- | --- | --- |
|  | Ij,k≤|κ2|​∑i=1k−1ci,k​Ij,i+σ​TαΓ​(α+1),I\_{j,k}\leq|\kappa\_{2}|\sum\_{i=1}^{k-1}c\_{i,k}I\_{j,i}+\frac{\sigma T^{\alpha}}{\Gamma(\alpha+1)}, |  |

in a similar way as above. We conclude by the same Grönwall type inequality [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.4].
∎

###### Proof of Lemma [2.12](https://arxiv.org/html/2602.18234v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2. Weak rate of convergence ‣ 2. Convergence for the rough Volterra Ornstein-Uhlenbeck process ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

Let k∈{1,…,n}k\in\{1,\dots,n\} be fixed. We set I​Δ~ℓ,k=∫0tk|𝒟s​Xtℓ−𝒟s​Xˇntℓ|​𝑑s\widetilde{I\Delta}\_{\ell,k}=\int\_{0}^{t\_{k}}|\mathcal{D}\_{s}X\_{t\_{\ell}}-\mathcal{D}\_{s}{\check{X}^{n}}\_{t\_{\ell}}|ds and get from ([B](https://arxiv.org/html/2602.18234v1#A2.Ex38 "Proof of Lemma 2.11. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and the triangle inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​Δ~ℓ,k≤|κ2|​∑i=1ℓ−1ci,ℓ​I​Δ~i,k+𝒮~ℓ,k,\widetilde{I\Delta}\_{\ell,k}\leq|\kappa\_{2}|\sum\_{i=1}^{\ell-1}c\_{i,\ell}\widetilde{I\Delta}\_{i,k}+\widetilde{\mathcal{S}}\_{\ell,k}, |  | (B.7) |

with

|  |  |  |
| --- | --- | --- |
|  | 𝒮~ℓ,k=|κ2|​∫0tℓ(∫0tk|𝒟s​Xu−𝒟s​Xη​(u)|​𝑑s)​(tℓ−u)α−1Γ​(α)​𝑑u.\widetilde{\mathcal{S}}\_{\ell,k}=|\kappa\_{2}|\int\_{0}^{t\_{\ell}}\left(\int\_{0}^{t\_{k}}|\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)}|ds\right)\frac{(t\_{\ell}-u)^{\alpha-1}}{\Gamma(\alpha)}du. |  |

We now bound uniformly 𝒮~ℓ,k\widetilde{\mathcal{S}}\_{\ell,k} and we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝒟s​Xu−𝒟s​Xη​(u)|≤\displaystyle|\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)}|\leq | |𝟏s<u​(u−s)α−1Γ​(α)−𝟏s<η​(u)​(η​(u)−s)α−1Γ​(α)|\displaystyle|\mathbf{1}\_{s<u}\frac{(u-s)^{\alpha-1}}{\Gamma(\alpha)}-\mathbf{1}\_{s<\eta(u)}\frac{(\eta(u)-s)^{\alpha-1}}{\Gamma(\alpha)}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑i=2∞|κ2|i−1​(u−s)+i​α−1−(η​(u)−s)+i​α−1Γ​(i​α).\displaystyle+\sum\_{i=2}^{\infty}|\kappa\_{2}|^{i-1}\frac{(u-s)\_{+}^{i\alpha-1}-(\eta(u)-s)\_{+}^{i\alpha-1}}{\Gamma(i\alpha)}. |  |

We then obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0t|𝒟s​Xu−𝒟s​Xη​(u)|​𝑑s≤Cnα,\int\_{0}^{t}|\mathcal{D}\_{s}X\_{u}-\mathcal{D}\_{s}X\_{\eta(u)}|ds\leq\frac{C}{n^{\alpha}}, |  | (B.8) |

since the integral of the sum can be calculated exactly and is a O​(1/n)O(1/n) using that 2​α−1>02\alpha-1>0, and [[10](https://arxiv.org/html/2602.18234v1#bib.bib10), Lemma 4.5 with β=0\beta=0] gives the bound for the first term.
This gives |𝒮~ℓ,k|≤C​|κ2|​TαΓ​(α+1)​1nα|\widetilde{\mathcal{S}}\_{\ell,k}|\leq C|\kappa\_{2}|\frac{T^{\alpha}}{\Gamma(\alpha+1)}\frac{1}{n^{\alpha}}. This bound is thus uniform in ℓ\ell, kk and nn. We finally apply the Gronwall type estimate given by [[17](https://arxiv.org/html/2602.18234v1#bib.bib17), Lemma 3.4] to ([B.7](https://arxiv.org/html/2602.18234v1#A2.E7 "In Proof of Lemma 2.12. ‣ Appendix B Technical proofs ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) and get the claim.
∎

###### Proof of Proposition [4.8](https://arxiv.org/html/2602.18234v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4.2.3. Analysis of ℰ_{2,2} ‣ 4.2. Weak error analysis ‣ 4. Weak error approximation with polynomial test functions ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models").

Let I=sup{i>j:α​(k)=k−1​ for ​j<k≤i}I=\sup\{i>j:\alpha(k)=k-1\text{ for }j<k\leq i\}, with I=jI=j if {i>j:α​(k)=k−1​ for ​j<k≤i}=∅\{i>j:\alpha(k)=k-1\text{ for }j<k\leq i\}=\emptyset i.e. α​(j+1)<j\alpha(j+1)<j.

Case 1: I=jI=j. We can differentiate directly and get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂jHj​(r1,…,rj)=\displaystyle\partial\_{j}H\_{j}(r\_{1},\dots,r\_{j})= | ∫0rj∫0rj+2…∫0rm−1ϕ(𝐫¯)×\displaystyle\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+2}}\dots\int\_{0}^{r\_{m-1}}\phi({\bf\bar{r}})\times |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (rα​(j+1)−rj)ℓj+1​α−1​∏i>j+1(r¯α​(i)−ri)ℓi​α−1​d​rm​…​d​rj+2\displaystyle\phantom{\*\*\*\*\*\*\*\*\*}(r\_{\alpha(j+1)}-r\_{j})^{\ell\_{j+1}\alpha-1}\prod\_{i>j+1}(\bar{r}\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{j+2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0rj∫0rj+1…​∫0rm−1∂jϕ​(𝐫)​∏i>j(rα​(i)−ri)ℓi​α−1​d​rm​…​d​rj+1\displaystyle+\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+1}}\dots\int\_{0}^{r\_{m-1}}\partial\_{j}\phi({\bf r})\prod\_{i>j}(r\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{j+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0rj∫0rj+1…∫0rm−1ϕ(𝐫)∑i>j:α​(i)=j(ℓiα−1)(rj−ri)ℓi​α−2×\displaystyle+\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+1}}\dots\int\_{0}^{r\_{m-1}}\phi({\bf r})\sum\_{i>j:\alpha(i)=j}(\ell\_{i}\alpha-1)(r\_{j}-r\_{i})^{\ell\_{i}\alpha-2}\times |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∏i′>j,i′≠i(rα​(i′)−ri′)ℓi′​α−1​d​rm​…​d​rj+1\displaystyle\phantom{\*\*\*\*\*\*\*\*\*}\prod\_{i^{\prime}>j,i^{\prime}\not=i}(r\_{\alpha(i^{\prime})}-r\_{i^{\prime}})^{\ell\_{i^{\prime}}\alpha-1}dr\_{m}\dots dr\_{j+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:I1+I2+I3,\displaystyle=:I\_{1}+I\_{2}+I\_{3}, |  |

with 𝐫¯=(r1,…,rj,rj,rj+2,…,rm){\bf\bar{r}}=(r\_{1},\dots,r\_{j},r\_{j},r\_{j+2},\dots,r\_{m}).
We use that ϕ\phi is bounded and integrate from d​rmdr\_{m} to d​rj+2dr\_{j+2} to get

|  |  |  |
| --- | --- | --- |
|  | |I1|≤‖ϕ‖∞​T∑i=j+2mα​ℓi∏i=j+2mα​ℓi​(rα​(j+1)−rj)ℓj+1​α−1.|I\_{1}|\leq\|\phi\|\_{\infty}\frac{T^{\sum\_{i=j+2}^{m}\alpha\ell\_{i}}}{\prod\_{i=j+2}^{m}\alpha\ell\_{i}}(r\_{\alpha(j+1)}-r\_{j})^{\ell\_{j+1}\alpha-1}. |  |

Note that α​(j+1)<j\alpha(j+1)<j since we are in the case I=jI=j. We get that

|  |  |  |
| --- | --- | --- |
|  | ∫0rj−1(rα​(j+1)−rj)ℓj+1​α−1​𝑑rj≤1α​ℓj​Tℓj+1​α.\int\_{0}^{r\_{j-1}}(r\_{\alpha(j+1)}-r\_{j})^{\ell\_{j+1}\alpha-1}dr\_{j}\leq\frac{1}{\alpha\ell\_{j}}T^{\ell\_{j+1}\alpha}. |  |

Thus, I1I\_{1} is integrable with respect to rjr\_{j}.

For the second integral, we use Proposition [A.4](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") (2) that gives

|  |  |  |
| --- | --- | --- |
|  | |∂jϕ​(𝐫)|≤C​((rj−rj+1)2​α−2+(rj−1−rj)2​α−2).|\partial\_{j}\phi({\bf r})|\leq C((r\_{j}-r\_{j+1})^{2\alpha-2}+(r\_{j-1}-r\_{j})^{2\alpha-2}). |  |

Integrating again from d​rmdr\_{m} to d​rj+2dr\_{j+2}, we obtain

|  |  |  |
| --- | --- | --- |
|  | |I2|≤C​T∑i=j+2mα​ℓi∏i=j+2mα​ℓi​∫0rj((rj−rj+1)2​α−2+(rj−1−rj)2​α−2)​(rα​(j+1)−rj+1)ℓj+1​α−1​𝑑rj+1.|I\_{2}|\leq C\frac{T^{\sum\_{i=j+2}^{m}\alpha\ell\_{i}}}{\prod\_{i=j+2}^{m}\alpha\ell\_{i}}\int\_{0}^{r\_{j}}((r\_{j}-r\_{j+1})^{2\alpha-2}+(r\_{j-1}-r\_{j})^{2\alpha-2})(r\_{\alpha(j+1)}-r\_{j+1})^{\ell\_{j+1}\alpha-1}dr\_{j+1}. |  |

If ℓj+1≥2\ell\_{j+1}\geq 2, we get

|  |  |  |
| --- | --- | --- |
|  | |I2|≤C​T∑i=j+2mα​ℓi∏i=j+2mα​ℓi​Tℓj+1​α−1​(rj2​α−12​α−1+(rj−1−rj)2​α−2),|I\_{2}|\leq C\frac{T^{\sum\_{i=j+2}^{m}\alpha\ell\_{i}}}{\prod\_{i=j+2}^{m}\alpha\ell\_{i}}T^{\ell\_{j+1}\alpha-1}\left(\frac{r\_{j}^{2\alpha-1}}{2\alpha-1}+(r\_{j-1}-r\_{j})^{2\alpha-2}\right), |  |

and ∫0rj−1(rj2​α−12​α−1+(rj−1−rj)2​α−2)​𝑑rj≤CT\int\_{0}^{r\_{j-1}}\left(\frac{r\_{j}^{2\alpha-1}}{2\alpha-1}+(r\_{j-1}-r\_{j})^{2\alpha-2}\right)dr\_{j}\leq C\_{T}. Otherwise, ℓj+1=1\ell\_{j+1}=1 and we use (rα​(j+1)−rj+1)α−1≤(rj−1−rj+1)α−1(r\_{\alpha(j+1)}-r\_{j+1})^{\alpha-1}\leq(r\_{j-1}-r\_{j+1})^{\alpha-1} since α​(j+1)<j\alpha(j+1)<j. This gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | |I2|\displaystyle|I\_{2}| | ≤C​T∑i=j+2mα​ℓi∏i=j+2mα​ℓi​∫0rj((rj−1−rj)2​α−2+(rj−rj+1)2​α−2)​(rj−1−rj+1)α−1​𝑑rj+1\displaystyle\leq C\frac{T^{\sum\_{i=j+2}^{m}\alpha\ell\_{i}}}{\prod\_{i=j+2}^{m}\alpha\ell\_{i}}\int\_{0}^{r\_{j}}((r\_{j-1}-r\_{j})^{2\alpha-2}+(r\_{j}-r\_{j+1})^{2\alpha-2})(r\_{j-1}-r\_{j+1})^{\alpha-1}dr\_{j+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​T∑i=j+2mα​ℓi∏i=j+2mα​ℓi​(Tαα​(rj−1−rj)2​α−2+∫0rj(rj−rj+1)2​α−2​(rj−1−rj+1)α−1​𝑑rj+1).\displaystyle\leq C\frac{T^{\sum\_{i=j+2}^{m}\alpha\ell\_{i}}}{\prod\_{i=j+2}^{m}\alpha\ell\_{i}}\left(\frac{T^{\alpha}}{\alpha}(r\_{j-1}-r\_{j})^{2\alpha-2}+\int\_{0}^{r\_{j}}(r\_{j}-r\_{j+1})^{2\alpha-2}(r\_{j-1}-r\_{j+1})^{\alpha-1}dr\_{j+1}\right). |  |

If α>2/3\alpha>2/3, we have (rj−1−rj+1)α−1≤(rj−rj+1)α−1(r\_{j-1}-r\_{j+1})^{\alpha-1}\leq(r\_{j}-r\_{j+1})^{\alpha-1} and
∫0rj(rj−rj+1)3​α−3​𝑑rj+1≤T3​α−23​α−2\int\_{0}^{r\_{j}}(r\_{j}-r\_{j+1})^{3\alpha-3}dr\_{j+1}\leq\frac{T^{3\alpha-2}}{3\alpha-2}. We can thus conclude as for ℓj+1≥2\ell\_{j+1}\geq 2. Otherwise, we have α∈(1/2,2/3]\alpha\in(1/2,2/3] and the integral is equal, up to a positive multiplicative constant to

|  |  |  |
| --- | --- | --- |
|  | rj2​α−1​rj−1α−1​F12​(1−α,1;2​α,rjrj−1),r\_{j}^{2\alpha-1}r\_{j-1}^{\alpha-1}{{}\_{2}}F\_{1}(1-\alpha,1;2\alpha,\frac{r\_{j}}{r\_{j-1}}), |  |

using the change of variable rj+1=u​rjr\_{j+1}=ur\_{j}, u∈[0,1]u\in[0,1]. By [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Eq. 15.8.1], this term is also equal, up to a positive multiplicative constant to

|  |  |  |
| --- | --- | --- |
|  | (rjrj−1)2​α−1​(rj−1−rj)3​α−2​F12​(3​α−1,2​α−1;2​α,rjrj−1).\left(\frac{r\_{j}}{r\_{j-1}}\right)^{2\alpha-1}(r\_{j-1}-r\_{j})^{3\alpha-2}{{}\_{2}}F\_{1}(3\alpha-1,2\alpha-1;2\alpha,\frac{r\_{j}}{r\_{j-1}}). |  |

For α<2/3\alpha<2/3, we use ([A.4](https://arxiv.org/html/2602.18234v1#A1.E4 "In Proof. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models")) to get that this term is dominated by (rj−1−rj)3​α−2(r\_{j-1}-r\_{j})^{3\alpha-2} and is thus integrable with respect to rj∈[0,rj−1]r\_{j}\in[0,r\_{j-1}]. For α=2/3\alpha=2/3, we use [[20](https://arxiv.org/html/2602.18234v1#bib.bib20), Eq. 15.4.21] to get the integrability.

We now upper bound I3I\_{3}. We use that ϕ\phi is bounded, so that we have to upper bound

|  |  |  |
| --- | --- | --- |
|  | ∫0rj∫0rj+1…​∫0rm−1|ℓi​α−1|​(rj−ri)ℓi​α−2​∏i′>j,i′≠i(rα​(i′)−ri′)ℓi′​α−1​d​rm​…​d​rj+1.\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+1}}\dots\int\_{0}^{r\_{m-1}}|\ell\_{i}\alpha-1|(r\_{j}-r\_{i})^{\ell\_{i}\alpha-2}\prod\_{i^{\prime}>j,i^{\prime}\not=i}(r\_{\alpha(i^{\prime})}-r\_{i^{\prime}})^{\ell\_{i^{\prime}}\alpha-1}dr\_{m}\dots dr\_{j+1}. |  |

When ℓi≥2\ell\_{i}\geq 2, we can upper bound this integral in the same way as I1I\_{1}. We now consider ℓi=1\ell\_{i}=1 and integrate from d​rmdr\_{m} to d​ri+1dr\_{i+1} to get the upper bound

|  |  |  |
| --- | --- | --- |
|  | T∑k=i+1mα​ℓk∏k=i+1mα​ℓk​∫0rj…​∫0ri−2(∫0ri−1(1−α)​(rj−ri)α−2​𝑑ri)​∏i>i′>j(rα​(i′)−ri′)ℓi′​α−1​d​ri−1​…​d​rj+1\displaystyle\frac{T^{\sum\_{k=i+1}^{m}\alpha\ell\_{k}}}{\prod\_{k=i+1}^{m}\alpha\ell\_{k}}\int\_{0}^{r\_{j}}\dots\int\_{0}^{r\_{i-2}}\left(\int\_{0}^{r\_{i-1}}(1-\alpha)(r\_{j}-r\_{i})^{\alpha-2}dr\_{i}\right)\prod\_{i>i^{\prime}>j}(r\_{\alpha(i^{\prime})}-r\_{i^{\prime}})^{\ell\_{i^{\prime}}\alpha-1}dr\_{i-1}\dots dr\_{j+1} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤T∑k=i+1mα​ℓk∏k=i+1mα​ℓk​∫0rj∫0rj+1…​∫0ri−2(rj−ri−1)α−1​∏i>i′>j(rα​(i′)−ri′)ℓi′​α−1​d​ri−1​…​d​rj+1.\displaystyle\leq\frac{T^{\sum\_{k=i+1}^{m}\alpha\ell\_{k}}}{\prod\_{k=i+1}^{m}\alpha\ell\_{k}}\int\_{0}^{r\_{j}}\int\_{0}^{r\_{j+1}}\dots\int\_{0}^{r\_{i-2}}(r\_{j}-r\_{i-1})^{\alpha-1}\prod\_{i>i^{\prime}>j}(r\_{\alpha(i^{\prime})}-r\_{i^{\prime}})^{\ell\_{i^{\prime}}\alpha-1}dr\_{i-1}\dots dr\_{j+1}. |  |

Using that 2​x​y≤x2+y22xy\leq x^{2}+y^{2}, we get

|  |  |  |
| --- | --- | --- |
|  | ∫0ri−2(rj−ri−1)α−1​(rα​(i−1)−ri−1)ℓi−1​α−1​𝑑ri−1≤12​(T2​α−12​α−1+T2​ℓi−1​α−12​α​ℓi−1−1)\int\_{0}^{r\_{i-2}}(r\_{j}-r\_{i-1})^{\alpha-1}(r\_{\alpha(i-1)}-r\_{i-1})^{\ell\_{i-1}\alpha-1}dr\_{i-1}\leq\frac{1}{2}\left(\frac{T^{2\alpha-1}}{2\alpha-1}+\frac{T^{2\ell\_{i-1}\alpha-1}}{2\alpha\ell\_{i-1}-1}\right) |  |

and then integrating from d​ri−2dr\_{i-2} to d​rjdr\_{j}, we get the result.

Case 2: I>jI>j. We make a change of variable in the integral to differentiate with respect to rjr\_{j}. Namely, we set (rj+1,rj+2,…,rI)=(uj+1​rj,uj+2​uj+1​rj,…,∏k=j+1Iuk​rj)(r\_{j+1},r\_{j+2},\dots,r\_{I})=(u\_{j+1}r\_{j},u\_{j+2}u\_{j+1}r\_{j},\dots,\prod\_{k=j+1}^{I}u\_{k}r\_{j}) with uj+1,…,uI∈(0,1)u\_{j+1},\dots,u\_{I}\in(0,1). We first observe that (using the definition of II)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∏i>j(rα​(i)−ri)ℓi​α−1\displaystyle\prod\_{i>j}(r\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1} | =∏I≥i>j(ri−1−ri)ℓi​α−1​∏i>I(rα​(i)−ri)ℓi​α−1\displaystyle=\prod\_{I\geq i>j}(r\_{i-1}-r\_{i})^{\ell\_{i}\alpha-1}\prod\_{i>I}(r\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =rj∑i=j+1I(ℓi​α−1)​∏I≥i>jui∑k=i+1I(ℓk​α−1)​(1−ui)ℓi​α−1​∏i>I(rα​(i)−ri)ℓi​α−1,\displaystyle=r\_{j}^{\sum\_{i=j+1}^{I}(\ell\_{i}\alpha-1)}\prod\_{I\geq i>j}u\_{i}^{\sum\_{k=i+1}^{I}(\ell\_{k}\alpha-1)}(1-u\_{i})^{\ell\_{i}\alpha-1}\prod\_{i>I}(r\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}, |  |

and noting that the Jacobian is equal to rjI−j​uj+1I−j−1​…​uI−22​uI−1r\_{j}^{I-j}u\_{j+1}^{I-j-1}\dots u\_{I-2}^{2}u\_{I-1}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hj​(r1,…,rj)\displaystyle H\_{j}(r\_{1},\dots,r\_{j}) | =rj∑i=j+1Iℓi​α∫01…∫01∫0∏k=j+1Iuk​rj∫0rI+1…∫0rm−1ϕ(𝐫𝐮)×\displaystyle=r\_{j}^{\sum\_{i=j+1}^{I}\ell\_{i}\alpha}\int\_{0}^{1}\dots\int\_{0}^{1}\int\_{0}^{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}\int\_{0}^{r\_{I+1}}\dots\int\_{0}^{r\_{m-1}}\phi({\bf ru})\times |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∏I≥i>jui∑k=i+1Iℓk​α​(1−ui)ℓi​α−1​∏i>I(𝐫𝐮α​(i)−ri)ℓi​α−1​d​rm​…​d​rI+1​d​uI​…​d​uj+1\displaystyle\prod\_{I\geq i>j}u\_{i}^{\sum\_{k=i+1}^{I}\ell\_{k}\alpha}(1-u\_{i})^{\ell\_{i}\alpha-1}\prod\_{i>I}({\bf ru}\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{I+1}du\_{I}\dots du\_{j+1} |  |

with 𝐫𝐮=(r1,…,rj,uj+1​rj,…,∏k=j+1Iuk​rj,rI+1,…,rm){\bf ru}=(r\_{1},\dots,r\_{j},u\_{j+1}r\_{j},\dots,\prod\_{k=j+1}^{I}u\_{k}r\_{j},r\_{I+1},\dots,r\_{m}). Note that all the integrals between 0 and 11 are well defined and finite since they have a density of beta type.
We then set
  
𝐫𝐮~=(r1,…,rj,uj+1​rj,…,∏k=j+1Iuk​rj,∏k=j+1Iuk​rj,rI+2,…,rm)\widetilde{\bf ru}=(r\_{1},\dots,r\_{j},u\_{j+1}r\_{j},\dots,\prod\_{k=j+1}^{I}u\_{k}r\_{j},\prod\_{k=j+1}^{I}u\_{k}r\_{j},r\_{I+2},\dots,r\_{m}) and get

|  |  |  |
| --- | --- | --- |
|  | ∂jHj​(r1,…,rj)\displaystyle\partial\_{j}H\_{j}(r\_{1},\dots,r\_{j}) |  |
|  |  |  |
| --- | --- | --- |
|  | =(∑i=j+1Iℓiα)rj∑i=j+1Iℓi​α−1∫01…∫01∫0∏k=j+1Iuk​rj∫0rI+1…∫0rm−1ϕ(𝐫𝐮)×\displaystyle=\left(\sum\_{i=j+1}^{I}\ell\_{i}\alpha\right)r\_{j}^{\sum\_{i=j+1}^{I}\ell\_{i}\alpha-1}\int\_{0}^{1}\dots\int\_{0}^{1}\int\_{0}^{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}\int\_{0}^{r\_{I+1}}\dots\int\_{0}^{r\_{m-1}}\phi({\bf ru})\times |  |
|  |  |  |
| --- | --- | --- |
|  | ∏I≥i>jui∑k=i+1Iℓk​α​(1−ui)ℓi​α−1​∏i>I(𝐫𝐮α​(i)−ri)ℓi​α−1​d​rm​…​d​rI+1​d​uI​…​d​uj+1\displaystyle\prod\_{I\geq i>j}u\_{i}^{\sum\_{k=i+1}^{I}\ell\_{k}\alpha}(1-u\_{i})^{\ell\_{i}\alpha-1}\prod\_{i>I}({\bf ru}\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{I+1}du\_{I}\dots du\_{j+1} |  |
|  |  |  |
| --- | --- | --- |
|  | +rj∑i=j+1Iℓi​α∫01…∫01∫0∏k=j+1Iuk​rj∫0rI+2…∫0rm−1ϕ(𝐫𝐮~)×\displaystyle+r\_{j}^{\sum\_{i=j+1}^{I}\ell\_{i}\alpha}\int\_{0}^{1}\dots\int\_{0}^{1}\int\_{0}^{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}\int\_{0}^{r\_{I+2}}\dots\int\_{0}^{r\_{m-1}}\phi(\widetilde{\bf ru})\times |  |
|  |  |  |
| --- | --- | --- |
|  | ∏I≥i>jui1+∑k=i+1Iℓk​α​(1−ui)ℓi​α−1​∏i>I(𝐫𝐮~α​(i)−ri)ℓi​α−1​d​rm​…​d​rI+2​d​uI​…​d​uj+1\displaystyle\prod\_{I\geq i>j}u\_{i}^{1+\sum\_{k=i+1}^{I}\ell\_{k}\alpha}(1-u\_{i})^{\ell\_{i}\alpha-1}\prod\_{i>I}(\widetilde{\bf ru}\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{I+2}du\_{I}\dots du\_{j+1} |  |
|  |  |  |
| --- | --- | --- |
|  | +rj∑i=j+1Iℓi​α∫01…∫01∫0∏k=j+1Iuk​rj∫0rI+1…∫0rm−1[∑p=jI(∏k=j+1puk)(∂pϕ)(𝐫𝐮)]×\displaystyle+r\_{j}^{\sum\_{i=j+1}^{I}\ell\_{i}\alpha}\int\_{0}^{1}\dots\int\_{0}^{1}\int\_{0}^{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}\int\_{0}^{r\_{I+1}}\dots\int\_{0}^{r\_{m-1}}\left[\sum\_{p=j}^{I}\left(\prod\_{k=j+1}^{p}u\_{k}\right)(\partial\_{p}\phi)({\bf ru})\right]\times |  |
|  |  |  |
| --- | --- | --- |
|  | ∏I≥i>jui∑k=i+1Iℓk​α​(1−ui)ℓi​α−1​∏i>I(𝐫𝐮α​(i)−ri)ℓi​α−1​d​rm​…​d​rI+1​d​uI​…​d​uj+1\displaystyle\prod\_{I\geq i>j}u\_{i}^{\sum\_{k=i+1}^{I}\ell\_{k}\alpha}(1-u\_{i})^{\ell\_{i}\alpha-1}\prod\_{i>I}({\bf ru}\_{\alpha(i)}-r\_{i})^{\ell\_{i}\alpha-1}dr\_{m}\dots dr\_{I+1}du\_{I}\dots du\_{j+1} |  |
|  |  |  |
| --- | --- | --- |
|  | +rj∑i=j+1Iℓi​α​∫01…​∫01∫0∏k=j+1Iuk​rj∫0rI+1…​∫0rm−1ϕ​(𝐫𝐮)×∏I≥i>jui∑k=i+1Iℓk​α​(1−ui)ℓi​α−1\displaystyle+r\_{j}^{\sum\_{i=j+1}^{I}\ell\_{i}\alpha}\int\_{0}^{1}\dots\int\_{0}^{1}\int\_{0}^{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}\int\_{0}^{r\_{I+1}}\dots\int\_{0}^{r\_{m-1}}\phi({\bf ru})\times\prod\_{I\geq i>j}u\_{i}^{\sum\_{k=i+1}^{I}\ell\_{k}\alpha}(1-u\_{i})^{\ell\_{i}\alpha-1} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∑i>I:j≤α​(i)≤I(ℓiα−1)𝐫𝐮α​(i)rj(𝐫𝐮α​(i)−ri)−1∏i′>I(𝐫𝐮α​(i′)−ri′)ℓi′​α−1drm…drI+1duI…duj+1\displaystyle\times\sum\_{i>I:j\leq\alpha(i)\leq I}(\ell\_{i}\alpha-1)\frac{{\bf ru}\_{\alpha(i)}}{r\_{j}}({\bf ru}\_{\alpha(i)}-r\_{i})^{-1}\prod\_{i^{\prime}>I}({\bf ru}\_{\alpha(i^{\prime})}-r\_{i^{\prime}})^{\ell\_{i^{\prime}}\alpha-1}dr\_{m}\dots dr\_{I+1}du\_{I}\dots du\_{j+1} |  |
|  |  |  |
| --- | --- | --- |
|  | =:J1+J1′+J2+J3.\displaystyle=:J\_{1}+J^{\prime}\_{1}+J\_{2}+J\_{3}. |  |

We can then upper bound J1+J1′J\_{1}+J^{\prime}\_{1} and J3J\_{3} with similar arguments as, respectively, I1I\_{1} and I3I\_{3}. We now focus on J2J\_{2} which is similar to I2I\_{2}, but we prefer to give more details since its analysis is more involved. We use Proposition [A.4](https://arxiv.org/html/2602.18234v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Technical results ‣ Weak error approximation for rough and Gaussian mean-reverting stochastic volatility models") to get

|  |  |  |
| --- | --- | --- |
|  | |∑p=jI(∏k=j+1puk)​(∂pϕ)​(𝐫𝐮)|≤C​((rj−1−rj)2​α−2+rj2​α−2​𝐀​(u)+(∏k=j+1Iuk​rj−rI+1)2​α−2),\left|\sum\_{p=j}^{I}\left(\prod\_{k=j+1}^{p}u\_{k}\right)(\partial\_{p}\phi)({\bf ru})\right|\leq C\left((r\_{j-1}-r\_{j})^{2\alpha-2}+r\_{j}^{2\alpha-2}{\bf A}(u)+\left(\prod\_{k=j+1}^{I}u\_{k}r\_{j}-r\_{I+1}\right)^{2\alpha-2}\right), |  |

with 𝐀​(u)=(1−uj+1)2​α−2+⋯+(∏k=j+1Iuk)2​α−2​(1−uI)2​α−2{\bf A}(u)=(1-u\_{j+1})^{2\alpha-2}+\dots+\left(\prod\_{k=j+1}^{I}u\_{k}\right)^{2\alpha-2}(1-u\_{I})^{2\alpha-2}.
As for I2I\_{2}, we first integrate from d​rmdr\_{m} to d​rI+2dr\_{I+2} and get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |J2|\displaystyle|J\_{2}| | ≤CT∑k=I+2mα​ℓk∏k=I+2mα​ℓkrj∑i=j+1Iℓi​α∫01…∫01∫0∏k=j+1Iuk​rj∏I≥i>jui∑k=i+1Iℓk​α(1−ui)ℓi​α−1×\displaystyle\leq C\frac{T^{\sum\_{k=I+2}^{m}\alpha\ell\_{k}}}{\prod\_{k=I+2}^{m}\alpha\ell\_{k}}r\_{j}^{\sum\_{i=j+1}^{I}\ell\_{i}\alpha}\int\_{0}^{1}\dots\int\_{0}^{1}\int\_{0}^{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}\prod\_{I\geq i>j}u\_{i}^{\sum\_{k=i+1}^{I}\ell\_{k}\alpha}(1-u\_{i})^{\ell\_{i}\alpha-1}\times |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ((rj−1−rj)2​α−2+rj2​α−2​𝐀​(u)+(∏k=j+1Iuk​rj−rI+1)2​α−2)​(𝐫𝐮α​(I+1)−rI+1)ℓI+1​α−1\displaystyle\left((r\_{j-1}-r\_{j})^{2\alpha-2}+r\_{j}^{2\alpha-2}{\bf A}(u)+\left(\prod\_{k=j+1}^{I}u\_{k}r\_{j}-r\_{I+1}\right)^{2\alpha-2}\right)({\bf ru}\_{\alpha(I+1)}-r\_{I+1})^{\ell\_{I+1}\alpha-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | d​rI+1​d​uI​…​d​uj+1.\displaystyle\phantom{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}dr\_{I+1}du\_{I}\dots du\_{j+1}. |  |

If ℓI+1≥2\ell\_{I+1}\geq 2, we bound (𝐫𝐮α​(I+1)−rI+1)ℓI+1​α−1≤TℓI+1​α−1({\bf ru}\_{\alpha(I+1)}-r\_{I+1})^{\ell\_{I+1}\alpha-1}\leq T^{\ell\_{I+1}\alpha-1} and the integral with respect to rI+1r\_{I}+1 is upper bounded by
C​((rj−1−rj)2​α−2+rj2​α−2+(∏k=j+1Iuk​rj)2​α−1)C((r\_{j-1}-r\_{j})^{2\alpha-2}+r\_{j}^{2\alpha-2}+\left(\prod\_{k=j+1}^{I}u\_{k}r\_{j}\right)^{2\alpha-1}), which is integrable with respect to rj∈[0,rj−1]r\_{j}\in[0,r\_{j-1}]. In the case ℓI+1=1\ell\_{I+1}=1, since the terms (rj−1−rj)2​α−2(r\_{j-1}-r\_{j})^{2\alpha-2} and rj2​α−2​𝐀​(u)r\_{j}^{2\alpha-2}{\bf A}(u) do not depend on rI+1r\_{I+1}, their corresponding integrals are easily upper bounded by C​((rj−1−rj)2​α−2+rj2​α−2)C((r\_{j-1}-r\_{j})^{2\alpha-2}+r\_{j}^{2\alpha-2}), which is integrable with respect to rj∈[0,rj−1]r\_{j}\in[0,r\_{j-1}]. We thus focus on

|  |  |  |
| --- | --- | --- |
|  | ∫0rI(rI−rI+1)2​α−2​(𝐫𝐮α​(I+1)−rI+1)α−1​𝑑rI+1.\int\_{0}^{r\_{I}}(r\_{I}-r\_{I+1})^{2\alpha-2}({\bf ru}\_{\alpha(I+1)}-r\_{I+1})^{\alpha-1}dr\_{I+1}. |  |

If α>2/3\alpha>2/3, this integral is upper bounded by T3​α−23​α−2\frac{T^{3\alpha-2}}{3\alpha-2}, and we conclude easily. Otherwise, by a change of variable this integral is equal, up to multiplicative constant, to

|  |  |  |
| --- | --- | --- |
|  | (∏k=j+1Iuk​rj𝐫𝐮α​(I+1))2​α−1​(𝐫𝐮α​(I+1)−∏k=j+1Iuk​rj)3​α−2​F12​(3​α−1,2​α−1;2​α,∏k=j+1Iuk​rj𝐫𝐮α​(I+1)).\left(\frac{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}{{\bf ru}\_{\alpha(I+1)}}\right)^{2\alpha-1}\left({\bf ru}\_{\alpha(I+1)}-\prod\_{k=j+1}^{I}u\_{k}r\_{j}\right)^{3\alpha-2}{{}\_{2}}F\_{1}\left(3\alpha-1,2\alpha-1;2\alpha,\frac{\prod\_{k=j+1}^{I}u\_{k}r\_{j}}{{\bf ru}\_{\alpha(I+1)}}\right). |  |

We conclude as for J2J\_{2}.
∎

## References

* [1]

  E. Abi Jaber.
  The characteristic function of Gaussian stochastic volatility models: an analytic expression.
  Finance Stoch., 26(4):733–769, 2022.
* [2]

  E. Abi Jaber and M. Guellil.
  Complex discontinuities of the square root of Fredholm determinants in the Volterra Stein-Stein model.
  arXiv 2503.02965, 2025.
* [3]

  E. Abi Jaber, D. Hainaut, and E. Motte.
  The Volterra Stein-Stein model with stochastic interest rates.
  arXiv 2503.01716, 2025.
* [4]

  C. Bayer, P. Friz, and J. Gatheral.
  Pricing under rough volatility.
  Quant. Finance, 16(6):887–904, 2016.
* [5]

  C. Bayer, M. Fukasawa, and S. Nakahara.
  Short communication: on the weak convergence rate in the discretization of rough volatility models.
  SIAM J. Financial Math., 13(2):SC66–SC73, 2022.
* [6]

  C. Bayer, E. J. Hall, and R. Tempone.
  Weak error rates for option pricing under linear rough volatility.
  Int. J. Theor. Appl. Finance, 25(7-8):Paper No. 2250029, 47, 2022.
* [7]

  O. Bonesini, A. Jacquier, and A. Pannier.
  Rough volatility, path-dependent PDEs and weak rates of convergence.
  arXiv 2304.03042, 2025.
* [8]

  K. Diethelm, N. J. Ford, and A. D. Freed.
  Detailed error analysis for a fractional Adams method.
  Numer. Algorithms, 36(1):31–52, 2004.
* [9]

  O. El Euch and M. Rosenbaum.
  The characteristic function of rough Heston models.
  Math. Finance, 29(1):3–38, 2019.
* [10]

  P. K. Friz, W. Salkeld, and T. Wagenhofer.
  Weak error estimates for rough volatility models.
  Ann. Appl. Probab., 35(1):64–98, 2025.
* [11]

  M. Fukasawa and T. Ugai.
  Limit distributions for the discretization error of stochastic Volterra equations with fractional kernel.
  Ann. Appl. Probab., 33(6B):5071–5110, 2023.
* [12]

  P. Gassiat.
  Weak error rates of numerical schemes for rough volatility.
  SIAM J. Financial Math., 14(2):475–496, 2023.
* [13]

  J. Gatheral, T. Jaisson, and M. Rosenbaum.
  Volatility is rough.
  Quant. Finance, 18(6):933–949, 2018.
* [14]

  F. Hirsch, C. Profeta, B. Roynette, and M. Yor.
  Peacocks and associated martingales, with explicit constructions, volume 3 of Bocconi Springer Ser.
  New York, NY: Springer, 2011.
* [15]

  F. Hirsch, B. Roynette, and M. Yor.
  Unifying constructions of martingales associated with processes increasing in the convex order, via Lévy and Sato sheets.
  Expo. Math., 28(4):299–324, 2010.
* [16]

  B. Jourdain and G. Pagès.
  Convex ordering for stochastic Volterra equations and their Euler schemes.
  Finance Stoch., 29(1):1–62, 2025.
* [17]

  C. Li and F. Zeng.
  The finite difference methods for fractional ordinary differential equations.
  Numer. Funct. Anal. Optim., 34(2):149–179, 2013.
* [18]

  K. J. McGown and H. R. Parks.
  The generalization of Faulhaber’s formula to sums of non-integral powers.
  J. Math. Anal. Appl., 330(1):571–575, 2007.
* [19]

  D. Nualart.
  The Malliavin calculus and related topics.
  Probability and its Applications (New York). Springer-Verlag, Berlin, second edition, 2006.
* [20]

  A. B. Olde Daalhuis.
  Hypergeometric function.
  In NIST handbook of mathematical functions, pages 383–401. U.S. Dept. Commerce, Washington, DC, 2010.
* [21]

  I. Podlubny.
  Fractional differential equations, volume 198 of Mathematics in Science and Engineering.
  Academic Press, Inc., San Diego, CA, 1999.
  An introduction to fractional derivatives, fractional differential equations, to methods of their solution and some of their applications.
* [22]

  P. E. Protter.
  Stochastic integration and differential equations, volume 21 of Applications of Mathematics (New York).
  Springer-Verlag, Berlin, second edition, 2004.
  Stochastic Modelling and Applied Probability.
* [23]

  R. Schöbel and J. Zhu.
  Stochastic volatility with an Ornstein–Uhlenbeck process: An extension.
  Review of Finance, 3(1):23–46, 04 1999.
* [24]

  E. M. Stein and J. C. Stein.
  Stock price distributions with stochastic volatility: An analytic approach.
  The Review of Financial Studies, 4(4):727–752, 1991.
* [25]

  X. Zhang.
  Stochastic Volterra equations in Banach spaces and stochastic partial differential equation.
  J. Funct. Anal., 258(4):1361–1425, 2010.