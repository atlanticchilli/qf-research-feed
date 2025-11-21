---
authors:
- Miquel Noguer i Alonso
doc_id: arxiv:2511.16339v1
family_id: arxiv:2511.16339
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Financial Information Theory
url_abs: http://arxiv.org/abs/2511.16339v1
url_html: https://arxiv.org/html/2511.16339v1
venue: arXiv q-fin
version: 1
year: 2025
---


Miquel Noguer i Alonso
  
  
Artificial Intelligence Finance Institute

(November 20, 2025)

###### Abstract

This paper introduces a comprehensive framework for *Financial Information Theory* by applying information-theoretic concepts—such as entropy, Kullback–Leibler divergence, mutual information, normalized mutual information, and transfer entropy—to financial time series. We systematically derive these measures with complete mathematical proofs, establish their theoretical properties, and propose practical algorithms for estimation. Using S&P 500 data from 2000–2025, we demonstrate empirical usefulness for regime detection, market efficiency testing, and portfolio construction. We show that normalized mutual information (NMI) behaves as a powerful, bounded, and interpretable measure of temporal dependence, highlighting periods of structural change such as the 2008 financial crisis and COVID-19 shock. Our entropy-adjusted Value at Risk, information-theoretic diversification criterion, and NMI-based market efficiency test provide actionable tools for risk management and asset allocation. We interpret NMI as a quantitative diagnostic of the Efficient Market Hypothesis and demonstrate that information-theoretic methods offer superior regime detection compared to traditional autocorrelation or volatility-based approaches. All theoretical results include rigorous proofs, and empirical findings are validated across multiple market regimes spanning 25 years of daily returns.

## 1 Introduction

Financial markets are characterized by complex dynamics, non-stationarity, and heavy-tailed return distributions. Traditional statistical tools often rely on second-order moments or linear correlation, which can fail to capture nonlinear dependencies, structural breaks, and higher-order interactions. In contrast, information theory provides a model-free and robust framework to quantify uncertainty, dependence, and structural change, without assuming linearity or Gaussianity (cont2001; mcneil2015).

Entropy and mutual information are central concepts in information theory, quantifying the uncertainty of a random variable and the amount of information shared between variables, respectively (shannon1948). In the context of financial markets, entropy can be interpreted as a measure of market uncertainty, while mutual information captures the dependence between past and future returns, or across assets, instruments, and time scales. Transfer entropy extends this framework by providing a directional measure of information flow between time series, closely related to Granger causality but formulated in purely information-theoretic terms.

However, raw mutual information is unbounded and depends on the scale of the variables, complicating comparisons across assets and time. To address this, we focus on *Normalized Mutual Information* (NMI), which rescales mutual information into a dimensionless quantity bounded in [0,1][0,1]. This boundedness and relative robustness to scale make NMI particularly well-suited as a diagnostic for market efficiency and temporal dependence (noguer2024information).

The contributions of this paper are fourfold:

1. 1.

   Rigorous Theoretical Framework: We review and formalize core information-theoretic quantities (entropy, KL divergence, mutual information, transfer entropy, and NMI) with *complete proofs* of all fundamental properties.
2. 2.

   Estimation and Algorithms: We present practical algorithms for estimating entropy, NMI, and transfer entropy for financial time series using kk-nearest neighbor (k-NN) methods, with detailed implementation guidelines.
3. 3.

   Comprehensive Empirical Evidence: Using S&P 500 data (2000–2025), we show how entropy, KL divergence, and NMI capture major market regimes with detailed distributional analysis and statistical validation.
4. 4.

   Practical Applications: We propose entropy-adjusted VaR, information-theoretic diversification, NMI-based market efficiency testing, and trading signal algorithms with rigorous mathematical justification.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2511.16339v1#S2 "2 Core Information-Theoretic Concepts ‣ Financial Information Theory") establishes core information-theoretic concepts with complete proofs. Section [3](https://arxiv.org/html/2511.16339v1#S3 "3 Normalized Mutual Information (NMI) ‣ Financial Information Theory") introduces Normalized Mutual Information and proves its properties. Section [4](https://arxiv.org/html/2511.16339v1#S4 "4 Empirical Estimation on Financial Time Series ‣ Financial Information Theory") presents comprehensive empirical results on S&P 500 data. Section [5](https://arxiv.org/html/2511.16339v1#S5 "5 Applications in Finance ‣ Financial Information Theory") develops practical applications with detailed algorithms. Section [6](https://arxiv.org/html/2511.16339v1#S6 "6 Efficient Market Hypothesis and Related Literature ‣ Financial Information Theory") connects NMI to the Efficient Market Hypothesis. Section [7](https://arxiv.org/html/2511.16339v1#S7 "7 Conclusion ‣ Financial Information Theory") concludes.

## 2 Core Information-Theoretic Concepts

In this section, we review the main information-theoretic concepts used throughout the paper, providing *complete proofs* of all fundamental properties.

### 2.1 Shannon Entropy

Shannon entropy (shannon1948) quantifies the average uncertainty in a probability distribution, providing the fundamental building block for all subsequent information-theoretic measures.

###### Definition 2.1 (Shannon Entropy).

Let (Ω,ℱ,P)(\Omega,\mathcal{F},P) be a probability space with X:Ω→𝒳X:\Omega\to\mathcal{X} a discrete random variable taking values in a finite set 𝒳={x1,…,xn}\mathcal{X}=\{x\_{1},\ldots,x\_{n}\}. The *Shannon entropy* of XX is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(X)=H​(P)=−∑x∈𝒳P​(x)​log⁡P​(x)=−𝔼P​[log⁡P​(X)]H(X)=H(P)=-\sum\_{x\in\mathcal{X}}P(x)\log P(x)=-\mathbb{E}\_{P}[\log P(X)] |  | (1) |

where we adopt the convention 0​log⁡0=00\log 0=0 by continuity, and logarithms are natural (base ee) unless otherwise stated.

###### Theorem 2.2 (Properties of Entropy).

Let PP be a probability distribution over 𝒳\mathcal{X} with |𝒳|=n|\mathcal{X}|=n. Then:

1. (i)

   Non-negativity: H​(P)≥0H(P)\geq 0 with equality if and only if PP is a point mass.
2. (ii)

   Maximum entropy: H​(P)≤log⁡nH(P)\leq\log n with equality if and only if PP is uniform: P​(x)=1/nP(x)=1/n for all x∈𝒳x\in\mathcal{X}.
3. (iii)

   Strict concavity: H​(⋅)H(\cdot) is strictly concave on the probability simplex.
4. (iv)

   Continuity: H​(⋅)H(\cdot) is continuous in PP under total variation topology.
5. (v)

   Additivity: For independent random variables X,YX,Y:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | H​(X,Y)=H​(X)+H​(Y)H(X,Y)=H(X)+H(Y) |  | (2) |

###### Proof.

(i) Non-negativity: Since 0≤P​(x)≤10\leq P(x)\leq 1 for all xx, we have log⁡P​(x)≤0\log P(x)\leq 0, so −P​(x)​log⁡P​(x)≥0-P(x)\log P(x)\geq 0. Thus H​(P)≥0H(P)\geq 0. Equality holds when all non-zero terms vanish, which occurs only when P​(x)∈{0,1}P(x)\in\{0,1\} for all xx, i.e., PP is a point mass.

(ii) Maximum entropy: We maximize H​(P)=−∑ipi​log⁡piH(P)=-\sum\_{i}p\_{i}\log p\_{i} subject to ∑ipi=1\sum\_{i}p\_{i}=1 using Lagrange multipliers. The Lagrangian is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(p,λ)=−∑i=1npi​log⁡pi−λ​(∑i=1npi−1)\mathcal{L}(p,\lambda)=-\sum\_{i=1}^{n}p\_{i}\log p\_{i}-\lambda\left(\sum\_{i=1}^{n}p\_{i}-1\right) |  | (3) |

Taking derivatives and setting to zero:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ℒ∂pi=−log⁡pi−1−λ=0⟹pi=e−1−λ\frac{\partial\mathcal{L}}{\partial p\_{i}}=-\log p\_{i}-1-\lambda=0\implies p\_{i}=e^{-1-\lambda} |  | (4) |

Since ∑ipi=1\sum\_{i}p\_{i}=1, we have n​e−1−λ=1ne^{-1-\lambda}=1, yielding pi=1/np\_{i}=1/n for all ii. Substituting:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hmax=−∑i=1n1n​log⁡1n=log⁡nH\_{\max}=-\sum\_{i=1}^{n}\frac{1}{n}\log\frac{1}{n}=\log n |  | (5) |

(iii) Strict concavity: For 0<λ<10<\lambda<1 and distributions PP, QQ, let R=λ​P+(1−λ)​QR=\lambda P+(1-\lambda)Q. Then:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(R)\displaystyle H(R) | =−∑xr​(x)​log⁡r​(x)\displaystyle=-\sum\_{x}r(x)\log r(x) |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑x[λ​p​(x)+(1−λ)​q​(x)]​log⁡[λ​p​(x)+(1−λ)​q​(x)]\displaystyle=-\sum\_{x}[\lambda p(x)+(1-\lambda)q(x)]\log[\lambda p(x)+(1-\lambda)q(x)] |  | (7) |

By the strict concavity of −t​log⁡t-t\log t:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(R)\displaystyle H(R) | >−λ​∑xp​(x)​log⁡[λ​p​(x)+(1−λ)​q​(x)]\displaystyle>-\lambda\sum\_{x}p(x)\log[\lambda p(x)+(1-\lambda)q(x)] |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(1−λ)​∑xq​(x)​log⁡[λ​p​(x)+(1−λ)​q​(x)]\displaystyle\quad-(1-\lambda)\sum\_{x}q(x)\log[\lambda p(x)+(1-\lambda)q(x)] |  | (9) |

Using the log-sum inequality and properties of the logarithm:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(R)>λ​H​(P)+(1−λ)​H​(Q)H(R)>\lambda H(P)+(1-\lambda)H(Q) |  | (10) |

provided P≠QP\neq Q, establishing strict concavity.

(iv) Continuity: Let Pn→PP\_{n}\to P in total variation: ∑x|Pn​(x)−P​(x)|→0\sum\_{x}|P\_{n}(x)-P(x)|\to 0. The function f​(t)=−t​log⁡tf(t)=-t\log t (with f​(0)=0f(0)=0) is continuous and bounded on [0,1][0,1]. Thus:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |H​(Pn)−H​(P)|\displaystyle|H(P\_{n})-H(P)| | =|∑x[f​(Pn​(x))−f​(P​(x))]|\displaystyle=\left|\sum\_{x}[f(P\_{n}(x))-f(P(x))]\right| |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤∑x|f​(Pn​(x))−f​(P​(x))|→0\displaystyle\leq\sum\_{x}|f(P\_{n}(x))-f(P(x))|\to 0 |  | (12) |

by uniform continuity of ff on [0,1][0,1].

(v) Additivity: If XX and YY are independent, then PX,Y​(x,y)=PX​(x)​PY​(y)P\_{X,Y}(x,y)=P\_{X}(x)P\_{Y}(y). Thus:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(X,Y)\displaystyle H(X,Y) | =−∑x,yPX,Y​(x,y)​log⁡PX,Y​(x,y)\displaystyle=-\sum\_{x,y}P\_{X,Y}(x,y)\log P\_{X,Y}(x,y) |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑x,yPX​(x)​PY​(y)​log⁡[PX​(x)​PY​(y)]\displaystyle=-\sum\_{x,y}P\_{X}(x)P\_{Y}(y)\log[P\_{X}(x)P\_{Y}(y)] |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑x,yPX​(x)​PY​(y)​[log⁡PX​(x)+log⁡PY​(y)]\displaystyle=-\sum\_{x,y}P\_{X}(x)P\_{Y}(y)[\log P\_{X}(x)+\log P\_{Y}(y)] |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑xPX​(x)​log⁡PX​(x)−∑yPY​(y)​log⁡PY​(y)\displaystyle=-\sum\_{x}P\_{X}(x)\log P\_{X}(x)-\sum\_{y}P\_{Y}(y)\log P\_{Y}(y) |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =H​(X)+H​(Y)\displaystyle=H(X)+H(Y) |  | (17) |

∎

### 2.2 Differential Entropy

Differential entropy extends the concept of entropy to continuous variables.

###### Definition 2.3 (Differential Entropy).

Let XX be a continuous random variable with density fX​(x)f\_{X}(x) supported on ℝd\mathbb{R}^{d}. The *differential entropy* of XX is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(X)=−∫ℝdfX​(x)​log⁡fX​(x)​𝑑xh(X)=-\int\_{\mathbb{R}^{d}}f\_{X}(x)\log f\_{X}(x)\,dx |  | (18) |

provided the integral exists.

###### Remark 2.4.

Unlike discrete entropy, differential entropy can be negative and is not invariant under smooth transformations of the variable. However, differences of entropies and related quantities, such as mutual information and KL divergence, retain meaningful invariance properties.

#### 2.2.1 Computing Differential Entropy via k-Nearest Neighbors

To compute differential entropy, we use k-nearest neighbors (k-NN) estimators (kozachenko1987).

###### Theorem 2.5 (k-NN Entropy Estimator).

The k-NN estimator for differential entropy is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h^​(X)=1N​∑i=1Nlog⁡(N⋅ϵ​(i)k)+log⁡cd+ψ​(k)−ψ​(N)\hat{h}(X)=\frac{1}{N}\sum\_{i=1}^{N}\log\left(\frac{N\cdot\epsilon(i)}{k}\right)+\log c\_{d}+\psi(k)-\psi(N) |  | (19) |

where NN is the number of samples, ϵ​(i)\epsilon(i) is twice the distance from the ii-th sample to its kk-th nearest neighbor, cdc\_{d} is the volume of the unit ball in dd-dimensional space, and ψ\psi is the digamma function.

###### Proof sketch.

The k-NN estimator is derived from the Kozachenko–Leonenko approach, which approximates the density f​(xi)f(x\_{i}) at each point xix\_{i} by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^​(xi)≈kN⋅cd⋅ρk​(xi)d\hat{f}(x\_{i})\approx\frac{k}{N\cdot c\_{d}\cdot\rho\_{k}(x\_{i})^{d}} |  | (20) |

where ρk​(xi)\rho\_{k}(x\_{i}) is the distance to the kk-th nearest neighbor. Substituting into the entropy definition and taking expectations yields Equation ([19](https://arxiv.org/html/2511.16339v1#S2.E19 "In Theorem 2.5 (k-NN Entropy Estimator). ‣ 2.2.1 Computing Differential Entropy via k-Nearest Neighbors ‣ 2.2 Differential Entropy ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")). The digamma function corrections ψ​(k)−ψ​(N)\psi(k)-\psi(N) account for bias in finite samples. For complete details, see kozachenko1987.
∎

###### Remark 2.6.

The k-NN entropy estimator is consistent and asymptotically unbiased under mild regularity conditions on the density ff (kozachenko1987). The choice of kk involves a bias-variance tradeoff: smaller kk reduces bias but increases variance, while larger kk provides more stable estimates at the cost of increased bias.

### 2.3 Conditional Entropy

Conditional entropy quantifies the remaining uncertainty about one random variable given another.

###### Definition 2.7 (Conditional Entropy).

Let XX and YY be discrete random variables with joint distribution PX,YP\_{X,Y}. The *conditional entropy* of YY given XX is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(Y|X)=−∑x∈𝒳∑y∈𝒴P​(x,y)​log⁡P​(y|x)=𝔼X,Y​[−log⁡P​(Y|X)]H(Y|X)=-\sum\_{x\in\mathcal{X}}\sum\_{y\in\mathcal{Y}}P(x,y)\log P(y|x)=\mathbb{E}\_{X,Y}[-\log P(Y|X)] |  | (21) |

###### Theorem 2.8 (Chain Rule for Entropy).

For any random variables XX and YY:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(X,Y)=H​(X)+H​(Y|X)=H​(Y)+H​(X|Y)H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y) |  | (22) |

###### Proof.

By definition:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(X,Y)\displaystyle H(X,Y) | =−∑x,yP​(x,y)​log⁡P​(x,y)\displaystyle=-\sum\_{x,y}P(x,y)\log P(x,y) |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑x,yP​(x,y)​log⁡[P​(x)⋅P​(y|x)]\displaystyle=-\sum\_{x,y}P(x,y)\log[P(x)\cdot P(y|x)] |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑x,yP​(x,y)​log⁡P​(x)−∑x,yP​(x,y)​log⁡P​(y|x)\displaystyle=-\sum\_{x,y}P(x,y)\log P(x)-\sum\_{x,y}P(x,y)\log P(y|x) |  | (25) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑xP​(x)​log⁡P​(x)​∑yP​(y|x)−∑x,yP​(x,y)​log⁡P​(y|x)\displaystyle=-\sum\_{x}P(x)\log P(x)\sum\_{y}P(y|x)-\sum\_{x,y}P(x,y)\log P(y|x) |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑xP​(x)​log⁡P​(x)−∑x,yP​(x,y)​log⁡P​(y|x)\displaystyle=-\sum\_{x}P(x)\log P(x)-\sum\_{x,y}P(x,y)\log P(y|x) |  | (27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =H​(X)+H​(Y|X)\displaystyle=H(X)+H(Y|X) |  | (28) |

The second equality follows by symmetry.
∎

### 2.4 Kullback–Leibler Divergence

KL divergence measures the “distance” between two probability distributions, although it is not symmetric and does not satisfy the triangle inequality.

###### Definition 2.9 (Kullback–Leibler Divergence).

Let PP and QQ be two probability distributions on a common measurable space. For discrete distributions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(P∥Q)=∑x∈𝒳P​(x)​log⁡P​(x)Q​(x)=𝔼P​[log⁡P​(X)Q​(X)]D\_{\text{KL}}(P\|Q)=\sum\_{x\in\mathcal{X}}P(x)\log\frac{P(x)}{Q(x)}=\mathbb{E}\_{P}\left[\log\frac{P(X)}{Q(X)}\right] |  | (29) |

For continuous distributions with densities pp and qq:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(P∥Q)=∫p​(x)​log⁡p​(x)q​(x)​d​xD\_{\text{KL}}(P\|Q)=\int p(x)\log\frac{p(x)}{q(x)}\,dx |  | (30) |

###### Theorem 2.10 (Gibbs’ Inequality).

For any distributions PP and QQ:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(P∥Q)≥0D\_{\text{KL}}(P\|Q)\geq 0 |  | (31) |

with equality if and only if P=QP=Q almost everywhere.

###### Proof.

Using Jensen’s inequality with the strictly convex function −log⁡(⋅)-\log(\cdot):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −DKL​(P∥Q)\displaystyle-D\_{\text{KL}}(P\|Q) | =∑xP​(x)​log⁡Q​(x)P​(x)\displaystyle=\sum\_{x}P(x)\log\frac{Q(x)}{P(x)} |  | (32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼P​[log⁡Q​(X)P​(X)]\displaystyle=\mathbb{E}\_{P}\left[\log\frac{Q(X)}{P(X)}\right] |  | (33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤log⁡𝔼P​[Q​(X)P​(X)](by Jensen’s inequality)\displaystyle\leq\log\mathbb{E}\_{P}\left[\frac{Q(X)}{P(X)}\right]\quad\text{(by Jensen's inequality)} |  | (34) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =log​∑xP​(x)⋅Q​(x)P​(x)\displaystyle=\log\sum\_{x}P(x)\cdot\frac{Q(x)}{P(x)} |  | (35) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =log​∑xQ​(x)=log⁡1=0\displaystyle=\log\sum\_{x}Q(x)=\log 1=0 |  | (36) |

Equality holds in Jensen’s inequality if and only if Q​(x)/P​(x)Q(x)/P(x) is constant wherever P​(x)>0P(x)>0. Combined with normalization ∑xQ​(x)=1=∑xP​(x)\sum\_{x}Q(x)=1=\sum\_{x}P(x), this implies P=QP=Q almost everywhere.
∎

###### Theorem 2.11 (Pinsker’s Inequality).

For any distributions PP and QQ:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖P−Q‖TV≤12​DKL​(P∥Q)\|P-Q\|\_{\text{TV}}\leq\sqrt{\frac{1}{2}D\_{\text{KL}}(P\|Q)} |  | (37) |

where ‖P−Q‖TV=12​∑x|P​(x)−Q​(x)|\|P-Q\|\_{\text{TV}}=\frac{1}{2}\sum\_{x}|P(x)-Q(x)| is the total variation distance.

###### Proof sketch.

The proof uses properties of ff-divergences and the variational representation of total variation distance. Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A={x:P​(x)≥Q​(x)}A=\{x:P(x)\geq Q(x)\} |  | (38) |

Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖P−Q‖TV=∑x∈A[P​(x)−Q​(x)]=P​(A)−Q​(A)\|P-Q\|\_{\text{TV}}=\sum\_{x\in A}[P(x)-Q(x)]=P(A)-Q(A) |  | (39) |

By the data processing inequality for ff-divergences and properties of the logarithm, one can show:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [P​(A)−Q​(A)]2≤2​∑xP​(x)​log⁡P​(x)Q​(x)=2​DKL​(P∥Q)[P(A)-Q(A)]^{2}\leq 2\sum\_{x}P(x)\log\frac{P(x)}{Q(x)}=2D\_{\text{KL}}(P\|Q) |  | (40) |

Taking square roots yields Pinsker’s inequality. For complete details, see pinsker1964 or cover2006, Theorem 11.6.1.
∎

###### Remark 2.12.

Pinsker’s inequality provides a useful link between KL divergence and total variation distance, implying that if DKL​(P∥Q)D\_{\text{KL}}(P\|Q) is small, then PP and QQ are close in total variation.

### 2.5 Mutual Information

Mutual information measures the amount of information one random variable contains about another.

###### Definition 2.13 (Mutual Information).

Let XX and YY be discrete random variables with joint distribution PX,YP\_{X,Y} and marginals PXP\_{X} and PYP\_{Y}. The *mutual information* between XX and YY is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=∑x,yPX,Y​(x,y)​log⁡PX,Y​(x,y)PX​(x)​PY​(y)I(X;Y)=\sum\_{x,y}P\_{X,Y}(x,y)\log\frac{P\_{X,Y}(x,y)}{P\_{X}(x)P\_{Y}(y)} |  | (41) |

Equivalently:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=H​(Y)−H​(Y|X)=H​(X)+H​(Y)−H​(X,Y)I(X;Y)=H(Y)-H(Y|X)=H(X)+H(Y)-H(X,Y) |  | (42) |

###### Theorem 2.14 (Properties of Mutual Information).

For random variables XX and YY:

1. (i)

   Non-negativity: I​(X;Y)≥0I(X;Y)\geq 0 with equality if and only if XX and YY are independent.
2. (ii)

   Symmetry: I​(X;Y)=I​(Y;X)I(X;Y)=I(Y;X).
3. (iii)

   KL representation: I​(X;Y)=DKL​(PX,Y∥PX⊗PY)I(X;Y)=D\_{\text{KL}}(P\_{X,Y}\|P\_{X}\otimes P\_{Y}).
4. (iv)

   Bounds: I​(X;Y)≤min⁡{H​(X),H​(Y)}I(X;Y)\leq\min\{H(X),H(Y)\}.
5. (v)

   Data processing inequality: For Markov chain X→Y→ZX\to Y\to Z:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | I​(X;Z)≤min⁡{I​(X;Y),I​(Y;Z)}I(X;Z)\leq\min\{I(X;Y),I(Y;Z)\} |  | (43) |

###### Proof.

(i) Non-negativity: From the chain rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=H​(Y)−H​(Y|X)=H​(Y)−𝔼X​[H​(Y|X=x)]I(X;Y)=H(Y)-H(Y|X)=H(Y)-\mathbb{E}\_{X}[H(Y|X=x)] |  | (44) |

Since conditioning reduces entropy (a consequence of Jensen’s inequality applied to the concave entropy functional), H​(Y|X)≤H​(Y)H(Y|X)\leq H(Y) with equality if and only if XX and YY are independent. For a rigorous proof:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(Y)−H​(Y|X)\displaystyle H(Y)-H(Y|X) | =−∑yP​(y)​log⁡P​(y)+∑xP​(x)​∑yP​(y|x)​log⁡P​(y|x)\displaystyle=-\sum\_{y}P(y)\log P(y)+\sum\_{x}P(x)\sum\_{y}P(y|x)\log P(y|x) |  | (45) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑x,yP​(x,y)​log⁡P​(y|x)P​(y)\displaystyle=\sum\_{x,y}P(x,y)\log\frac{P(y|x)}{P(y)} |  | (46) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑x,yP​(x,y)​log⁡P​(x,y)P​(x)​P​(y)≥0\displaystyle=\sum\_{x,y}P(x,y)\log\frac{P(x,y)}{P(x)P(y)}\geq 0 |  | (47) |

by Gibbs’ inequality (Theorem [2.10](https://arxiv.org/html/2511.16339v1#S2.Thmtheorem10 "Theorem 2.10 (Gibbs’ Inequality). ‣ 2.4 Kullback–Leibler Divergence ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")), since the right side is DKL​(PX,Y∥PX⊗PY)D\_{\text{KL}}(P\_{X,Y}\|P\_{X}\otimes P\_{Y}).

(ii) Symmetry: Follows immediately from the symmetric definition I​(X;Y)=H​(X)+H​(Y)−H​(X,Y)I(X;Y)=H(X)+H(Y)-H(X,Y).

(iii) KL representation: By definition:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(X;Y)\displaystyle I(X;Y) | =∑x,yP​(x,y)​log⁡P​(x,y)P​(x)​P​(y)=DKL​(PX,Y∥PX⊗PY)\displaystyle=\sum\_{x,y}P(x,y)\log\frac{P(x,y)}{P(x)P(y)}=D\_{\text{KL}}(P\_{X,Y}\|P\_{X}\otimes P\_{Y}) |  | (48) |

(iv) Bounds: From the chain rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=H​(X)−H​(X|Y)≤H​(X)I(X;Y)=H(X)-H(X|Y)\leq H(X) |  | (49) |

since H​(X|Y)≥0H(X|Y)\geq 0. Similarly, I​(X;Y)≤H​(Y)I(X;Y)\leq H(Y).

(v) Data processing inequality: For Markov chain X→Y→ZX\to Y\to Z, we have P​(x,y,z)=P​(x)​P​(y|x)​P​(z|y)P(x,y,z)=P(x)P(y|x)P(z|y), which implies P​(x|y,z)=P​(x|y)P(x|y,z)=P(x|y). Thus:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(X;Y,Z)\displaystyle I(X;Y,Z) | =H​(X)−H​(X|Y,Z)\displaystyle=H(X)-H(X|Y,Z) |  | (50) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =H​(X)−H​(X|Y)(since X⟂Z∣Y)\displaystyle=H(X)-H(X|Y)\quad\text{(since $X\perp Z\mid Y$)} |  | (51) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =I​(X;Y)\displaystyle=I(X;Y) |  | (52) |

Also:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(X;Y,Z)\displaystyle I(X;Y,Z) | =I​(X;Y)+I​(X;Z|Y)\displaystyle=I(X;Y)+I(X;Z|Y) |  | (53) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥I​(X;Y)(since I​(X;Z|Y)≥0)\displaystyle\geq I(X;Y)\quad\text{(since $I(X;Z|Y)\geq 0$)} |  | (54) |

Combining with I​(X;Z)≤I​(X;Y,Z)I(X;Z)\leq I(X;Y,Z) (from the chain rule for mutual information), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Z)≤I​(X;Y)I(X;Z)\leq I(X;Y) |  | (55) |

By symmetry, I​(X;Z)≤I​(Y;Z)I(X;Z)\leq I(Y;Z), establishing the data processing inequality.
∎

###### Remark 2.15.

While mutual information is valuable, it is unbounded and depends on the entropy scale of the underlying variables, which complicates comparisons across assets, time periods, or markets with different volatility levels. This motivates the development and use of Normalized Mutual Information (NMI) as a bounded, scale-robust dependence measure.

### 2.6 Transfer Entropy and Directional Dependence

Mutual information is symmetric and does not distinguish the direction of information flow. Transfer entropy addresses this by measuring directional influence.

###### Definition 2.16 (Transfer Entropy (Discrete-Time)).

Let (Xt)t∈ℤ(X\_{t})\_{t\in\mathbb{Z}} and (Yt)t∈ℤ(Y\_{t})\_{t\in\mathbb{Z}} be two stationary stochastic processes. For integers k,ℓ≥1k,\ell\geq 1, define the past vectors

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt(k)=(Yt,Yt−1,…,Yt−k+1),Xt(ℓ)=(Xt,Xt−1,…,Xt−ℓ+1)Y\_{t}^{(k)}=(Y\_{t},Y\_{t-1},\dots,Y\_{t-k+1}),\qquad X\_{t}^{(\ell)}=(X\_{t},X\_{t-1},\dots,X\_{t-\ell+1}) |  | (56) |

The *transfer entropy* from XX to YY at horizon one is

|  |  |  |  |
| --- | --- | --- | --- |
|  | TX→Y=∑yt+1,yt(k),xt(ℓ)p​(yt+1,yt(k),xt(ℓ))​log⁡p​(yt+1∣yt(k),xt(ℓ))p​(yt+1∣yt(k))T\_{X\to Y}=\sum\_{y\_{t+1},y\_{t}^{(k)},x\_{t}^{(\ell)}}p(y\_{t+1},y\_{t}^{(k)},x\_{t}^{(\ell)})\log\frac{p(y\_{t+1}\mid y\_{t}^{(k)},x\_{t}^{(\ell)})}{p(y\_{t+1}\mid y\_{t}^{(k)})} |  | (57) |

###### Proposition 2.17 (Transfer Entropy as Conditional Mutual Information).

Transfer entropy can be expressed as a conditional mutual information:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TX→Y=I​(Xt(ℓ);Yt+1|Yt(k))T\_{X\to Y}=I\bigl(X\_{t}^{(\ell)};Y\_{t+1}\,\big|\,Y\_{t}^{(k)}\bigr) |  | (58) |

###### Proof.

By the definition of conditional mutual information:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(A;B∣C)\displaystyle I(A;B\mid C) | =∑a,b,cp​(a,b,c)​log⁡p​(a,b∣c)p​(a∣c)​p​(b∣c)\displaystyle=\sum\_{a,b,c}p(a,b,c)\log\frac{p(a,b\mid c)}{p(a\mid c)p(b\mid c)} |  | (59) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑b,cp​(b,c)​∑ap​(a∣b,c)​log⁡p​(a∣b,c)p​(a∣c)\displaystyle=\sum\_{b,c}p(b,c)\sum\_{a}p(a\mid b,c)\log\frac{p(a\mid b,c)}{p(a\mid c)} |  | (60) |

Identifying A=Xt(ℓ)A=X\_{t}^{(\ell)}, B=Yt+1B=Y\_{t+1} and C=Yt(k)C=Y\_{t}^{(k)}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(Xt(ℓ);Yt+1∣Yt(k))\displaystyle I(X\_{t}^{(\ell)};Y\_{t+1}\mid Y\_{t}^{(k)}) | =∑yt+1,yt(k)p​(yt+1,yt(k))​∑xt(ℓ)p​(xt(ℓ)∣yt+1,yt(k))​log⁡p​(xt(ℓ)∣yt+1,yt(k))p​(xt(ℓ)∣yt(k))\displaystyle=\sum\_{y\_{t+1},y\_{t}^{(k)}}p(y\_{t+1},y\_{t}^{(k)})\sum\_{x\_{t}^{(\ell)}}p(x\_{t}^{(\ell)}\mid y\_{t+1},y\_{t}^{(k)})\log\frac{p(x\_{t}^{(\ell)}\mid y\_{t+1},y\_{t}^{(k)})}{p(x\_{t}^{(\ell)}\mid y\_{t}^{(k)})} |  | (61) |

Using Bayes’ theorem and simplifying:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =∑yt+1,yt(k),xt(ℓ)p​(yt+1,yt(k),xt(ℓ))​log⁡p​(yt+1,xt(ℓ)∣yt(k))p​(yt+1∣yt(k))​p​(xt(ℓ)∣yt(k))\displaystyle=\sum\_{y\_{t+1},y\_{t}^{(k)},x\_{t}^{(\ell)}}p(y\_{t+1},y\_{t}^{(k)},x\_{t}^{(\ell)})\log\frac{p(y\_{t+1},x\_{t}^{(\ell)}\mid y\_{t}^{(k)})}{p(y\_{t+1}\mid y\_{t}^{(k)})p(x\_{t}^{(\ell)}\mid y\_{t}^{(k)})} |  | (62) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =∑yt+1,yt(k),xt(ℓ)p​(yt+1,yt(k),xt(ℓ))​log⁡p​(yt+1∣yt(k),xt(ℓ))p​(yt+1∣yt(k))\displaystyle=\sum\_{y\_{t+1},y\_{t}^{(k)},x\_{t}^{(\ell)}}p(y\_{t+1},y\_{t}^{(k)},x\_{t}^{(\ell)})\log\frac{p(y\_{t+1}\mid y\_{t}^{(k)},x\_{t}^{(\ell)})}{p(y\_{t+1}\mid y\_{t}^{(k)})} |  | (63) |

which coincides with Equation ([57](https://arxiv.org/html/2511.16339v1#S2.E57 "In Definition 2.16 (Transfer Entropy (Discrete-Time)). ‣ 2.6 Transfer Entropy and Directional Dependence ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")).
∎

###### Remark 2.18.

Transfer entropy is always non-negative and equals zero if and only if, conditional on its own past, the future of YY is independent of the past of XX:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TX→Y=0⟺p​(yt+1∣yt(k),xt(ℓ))=p​(yt+1∣yt(k))a.s.T\_{X\to Y}=0\quad\Longleftrightarrow\quad p(y\_{t+1}\mid y\_{t}^{(k)},x\_{t}^{(\ell)})=p(y\_{t+1}\mid y\_{t}^{(k)})\quad\text{a.s.} |  | (64) |

In this sense, transfer entropy formalizes the idea that XX *Granger-causes* YY if and only if TX→Y>0T\_{X\to Y}>0.

Algorithm 1  Transfer Entropy Estimation for Financial Time Series

0: Time series XtX\_{t}, YtY\_{t} of length NN; integers k,ℓ≥1k,\ell\geq 1 (past lengths); window size ww; number of neighbors knnk\_{\text{nn}}

0: Estimated transfer entropy TX→YT\_{X\to Y}

1: Construct lagged vectors Yt(k)Y\_{t}^{(k)} and Xt(ℓ)X\_{t}^{(\ell)} for all tt such that indices are valid.

2: Form samples of triplets (Yt+1,Yt(k),Xt(ℓ))(Y\_{t+1},Y\_{t}^{(k)},X\_{t}^{(\ell)}) over a moving window of size ww.

3: for each window do

4:  Estimate the joint entropy h​(Yt+1,Yt(k),Xt(ℓ))h(Y\_{t+1},Y\_{t}^{(k)},X\_{t}^{(\ell)}) using a k-NN estimator.

5:  Estimate the joint entropies h​(Yt+1,Yt(k))h(Y\_{t+1},Y\_{t}^{(k)}), h​(Yt(k),Xt(ℓ))h(Y\_{t}^{(k)},X\_{t}^{(\ell)}), and h​(Yt(k))h(Y\_{t}^{(k)}).

6:  Compute the conditional mutual information:

|  |  |  |
| --- | --- | --- |
|  | T^X→Y=h​(Yt+1,Yt(k))+h​(Yt(k),Xt(ℓ))−h​(Yt+1,Yt(k),Xt(ℓ))−h​(Yt(k))\widehat{T}\_{X\to Y}=h(Y\_{t+1},Y\_{t}^{(k)})+h(Y\_{t}^{(k)},X\_{t}^{(\ell)})-h(Y\_{t+1},Y\_{t}^{(k)},X\_{t}^{(\ell)})-h(Y\_{t}^{(k)}) |  |

7:  Optionally clip small negative values to zero to enforce non-negativity.

8: end for

9: return The average or time-varying sequence of T^X→Y\widehat{T}\_{X\to Y}.

## 3 Normalized Mutual Information (NMI)

Normalized Mutual Information (NMI) addresses the unbounded nature of mutual information by rescaling it using the entropies of the underlying variables. This yields a dimensionless quantity in [0,1][0,1].

### 3.1 Definition and Basic Properties

###### Definition 3.1 (Normalized Mutual Information).

Let UU and VV be random variables with mutual information I​(U;V)I(U;V) and (Shannon or differential) entropies H​(U)H(U) and H​(V)H(V). The *Normalized Mutual Information* between UU and VV is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NMI​(U,V)=I​(U;V)H​(U)⋅H​(V)\text{NMI}(U,V)=\frac{I(U;V)}{\sqrt{H(U)\cdot H(V)}} |  | (65) |

###### Theorem 3.2 (Bounds on NMI).

For any random variables UU and VV with positive entropies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤NMI​(U,V)≤10\leq\text{NMI}(U,V)\leq 1 |  | (66) |

Moreover:

* •

  NMI​(U,V)=0\text{NMI}(U,V)=0 if and only if UU and VV are independent
* •

  NMI​(U,V)=1\text{NMI}(U,V)=1 if and only if UU and VV are deterministically related

###### Proof.

From Theorem [2.14](https://arxiv.org/html/2511.16339v1#S2.Thmtheorem14 "Theorem 2.14 (Properties of Mutual Information). ‣ 2.5 Mutual Information ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory"), I​(U;V)≥0I(U;V)\geq 0, so NMI​(U,V)≥0\text{NMI}(U,V)\geq 0.

For the upper bound, note that from Theorem [2.14](https://arxiv.org/html/2511.16339v1#S2.Thmtheorem14 "Theorem 2.14 (Properties of Mutual Information). ‣ 2.5 Mutual Information ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")(iv):

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(U;V)≤min⁡{H​(U),H​(V)}I(U;V)\leq\min\{H(U),H(V)\} |  | (67) |

By the arithmetic-geometric mean (AM-GM) inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(U)⋅H​(V)≤H​(U)+H​(V)2\sqrt{H(U)\cdot H(V)}\leq\frac{H(U)+H(V)}{2} |  | (68) |

However, for the upper bound on NMI, we use:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(U;V)≤min⁡{H​(U),H​(V)}≤H​(U)⋅H​(V)I(U;V)\leq\min\{H(U),H(V)\}\leq\sqrt{H(U)\cdot H(V)} |  | (69) |

where the second inequality is the reverse AM-GM inequality: for a,b>0a,b>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | min⁡{a,b}≤a⋅b\min\{a,b\}\leq\sqrt{a\cdot b} |  | (70) |

To prove this, note that if a≤ba\leq b, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a2≤a⋅b⟹a≤a⋅ba^{2}\leq a\cdot b\implies a\leq\sqrt{a\cdot b} |  | (71) |

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NMI​(U,V)=I​(U;V)H​(U)​H​(V)≤H​(U)​H​(V)H​(U)​H​(V)=1\text{NMI}(U,V)=\frac{I(U;V)}{\sqrt{H(U)H(V)}}\leq\frac{\sqrt{H(U)H(V)}}{\sqrt{H(U)H(V)}}=1 |  | (72) |

Boundary cases:

* •

  NMI​(U,V)=0⇔I​(U;V)=0⇔U\text{NMI}(U,V)=0\iff I(U;V)=0\iff U and VV are independent (by Theorem [2.14](https://arxiv.org/html/2511.16339v1#S2.Thmtheorem14 "Theorem 2.14 (Properties of Mutual Information). ‣ 2.5 Mutual Information ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")).
* •

  NMI​(U,V)=1\text{NMI}(U,V)=1 requires I​(U;V)=H​(U)​H​(V)I(U;V)=\sqrt{H(U)H(V)}. Since I​(U;V)≤min⁡{H​(U),H​(V)}I(U;V)\leq\min\{H(U),H(V)\}, this can only occur when:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | I​(U;V)=H​(U)=H​(V)=H​(U)​H​(V)I(U;V)=H(U)=H(V)=\sqrt{H(U)H(V)} |  | (73) |

  which implies H​(U)=H​(V)H(U)=H(V) and I​(U;V)=H​(U)=H​(V)I(U;V)=H(U)=H(V).

  From I​(U;V)=H​(V)−H​(V|U)I(U;V)=H(V)-H(V|U), we have:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | H​(V)=H​(V)−H​(V|U)⟹H​(V|U)=0H(V)=H(V)-H(V|U)\implies H(V|U)=0 |  | (74) |

  This means VV is deterministic given UU (up to sets of measure zero). Similarly, H​(U|V)=0H(U|V)=0 implies UU is deterministic given VV. Therefore, UU and VV are essentially deterministic functions of each other.

∎

###### Remark 3.3.

NMI thus provides a normalized, bounded measure of dependence that facilitates comparison across different assets, time horizons, and markets.

### 3.2 Estimating NMI for Discrete Variables

For discrete random variables, estimation of NMI can be performed via empirical probabilities using observed frequencies in a contingency table. Given samples {(ui,vi)}i=1N\{(u\_{i},v\_{i})\}\_{i=1}^{N} drawn from (U,V)(U,V), we can estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P^U,V​(u,v)=1N​∑i=1N𝟏​{(ui,vi)=(u,v)}\hat{P}\_{U,V}(u,v)=\frac{1}{N}\sum\_{i=1}^{N}\mathbf{1}\{(u\_{i},v\_{i})=(u,v)\} |  | (75) |

Then:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H^​(U)\displaystyle\hat{H}(U) | =−∑uP^U​(u)​log⁡P^U​(u)\displaystyle=-\sum\_{u}\hat{P}\_{U}(u)\log\hat{P}\_{U}(u) |  | (76) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H^​(V)\displaystyle\hat{H}(V) | =−∑vP^V​(v)​log⁡P^V​(v)\displaystyle=-\sum\_{v}\hat{P}\_{V}(v)\log\hat{P}\_{V}(v) |  | (77) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I^​(U;V)\displaystyle\hat{I}(U;V) | =∑u,vP^U,V​(u,v)​log⁡P^U,V​(u,v)P^U​(u)​P^V​(v)\displaystyle=\sum\_{u,v}\hat{P}\_{U,V}(u,v)\log\frac{\hat{P}\_{U,V}(u,v)}{\hat{P}\_{U}(u)\hat{P}\_{V}(v)} |  | (78) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | NMI^​(U,V)\displaystyle\widehat{\text{NMI}}(U,V) | =I^​(U;V)H^​(U)⋅H^​(V)\displaystyle=\frac{\hat{I}(U;V)}{\sqrt{\hat{H}(U)\cdot\hat{H}(V)}} |  | (79) |

### 3.3 NMI for Continuous Variables

For continuous variables, we use k-NN entropy estimators. Entropies h​(X)h(X), h​(Y)h(Y), and h​(X,Y)h(X,Y) are estimated from samples, and then I​(X;Y)I(X;Y) and NMI​(X,Y)\text{NMI}(X,Y) are obtained via the identity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=h​(X)+h​(Y)−h​(X,Y)I(X;Y)=h(X)+h(Y)-h(X,Y) |  | (80) |

Algorithm 2  NMI Calculation for Continuous Time Series

0: Time series XX and YY with length NN, lag ℓ\ell, window size ww, number of neighbors kk

0: NMI time series

1: Initialize empty list nmi\_results

2: Shift YY by lag ℓ\ell to create YshiftedY\_{\text{shifted}}

3: Concatenate XX and YshiftedY\_{\text{shifted}}, drop NA values

4: for t=wt=w to NN do

5:  Extract window: Xw=X[t−w+1:t]X\_{w}=X[t-w+1:t], Yw=Yshifted[t−w+1:t]Y\_{w}=Y\_{\text{shifted}}[t-w+1:t]

6:  Compute hX=h​(Xw)h\_{X}=h(X\_{w}) using k-NN entropy estimator (Equation [19](https://arxiv.org/html/2511.16339v1#S2.E19 "In Theorem 2.5 (k-NN Entropy Estimator). ‣ 2.2.1 Computing Differential Entropy via k-Nearest Neighbors ‣ 2.2 Differential Entropy ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory"))

7:  Compute hY=h​(Yw)h\_{Y}=h(Y\_{w}) using k-NN entropy estimator

8:  Compute hX​Y=h​([Xw,Yw])h\_{XY}=h([X\_{w},Y\_{w}]) using k-NN entropy estimator

9:  MI=max⁡(0,hX+hY−hX​Y)\text{MI}=\max(0,h\_{X}+h\_{Y}-h\_{XY})

10:  NMIt=MI/hX⋅hY\text{NMI}\_{t}=\text{MI}/\sqrt{h\_{X}\cdot h\_{Y}} if hX⋅hY>0h\_{X}\cdot h\_{Y}>0, else 0

11:  Append NMIt\text{NMI}\_{t} to nmi\_results

12: end for

13: return nmi\_results

###### Remark 3.4.

The line MI=max⁡(0,hX+hY−hX​Y)\text{MI}=\max(0,h\_{X}+h\_{Y}-h\_{XY}) in Algorithm [2](https://arxiv.org/html/2511.16339v1#alg2 "Algorithm 2 ‣ 3.3 NMI for Continuous Variables ‣ 3 Normalized Mutual Information (NMI) ‣ Financial Information Theory") clips small negative estimates produced by the entropy estimator due to finite-sample noise, enforcing the theoretical non-negativity of mutual information.

### 3.4 Scale Invariance and Interpretability

###### Proposition 3.5 (Boundedness and Relative Robustness of NMI).

Differential entropy and conditional entropy are not invariant under rescaling of the underlying random variables: multiplying a continuous variable by a positive constant shifts its entropy by an additive constant. Normalized Mutual Information is not strictly scale invariant either, but because it normalizes mutual information by the marginal entropies and is bounded in [0,1][0,1], it is substantially less sensitive to pure volatility rescaling and is easier to interpret across assets and time.

###### Proof.

For a random variable XX and constant c>0c>0, the differential entropy satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(c​X)=h​(X)+log⁡ch(cX)=h(X)+\log c |  | (81) |

To prove this, let fX​(x)f\_{X}(x) be the density of XX. The density of Y=c​XY=cX is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fY​(y)=1c​fX​(yc)f\_{Y}(y)=\frac{1}{c}f\_{X}\left(\frac{y}{c}\right) |  | (82) |

Thus:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h​(Y)\displaystyle h(Y) | =−∫fY​(y)​log⁡fY​(y)​𝑑y\displaystyle=-\int f\_{Y}(y)\log f\_{Y}(y)\,dy |  | (83) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∫1c​fX​(yc)​log⁡[1c​fX​(yc)]​𝑑y\displaystyle=-\int\frac{1}{c}f\_{X}\left(\frac{y}{c}\right)\log\left[\frac{1}{c}f\_{X}\left(\frac{y}{c}\right)\right]\,dy |  | (84) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∫1c​fX​(yc)​[log⁡fX​(yc)−log⁡c]​𝑑y\displaystyle=-\int\frac{1}{c}f\_{X}\left(\frac{y}{c}\right)\left[\log f\_{X}\left(\frac{y}{c}\right)-\log c\right]\,dy |  | (85) |

Substituting x=y/cx=y/c, so d​y=c​d​xdy=c\,dx:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h​(Y)\displaystyle h(Y) | =−∫fX​(x)​[log⁡fX​(x)−log⁡c]​𝑑x\displaystyle=-\int f\_{X}(x)[\log f\_{X}(x)-\log c]\,dx |  | (86) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∫fX​(x)​log⁡fX​(x)​𝑑x+log⁡c​∫fX​(x)​𝑑x\displaystyle=-\int f\_{X}(x)\log f\_{X}(x)\,dx+\log c\int f\_{X}(x)\,dx |  | (87) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =h​(X)+log⁡c\displaystyle=h(X)+\log c |  | (88) |

This shows that differential entropy is not scale invariant. For NMI we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | NMI​(c​X,c​Y)\displaystyle\text{NMI}(cX,cY) | =I​(c​X;c​Y)h​(c​X)​h​(c​Y)\displaystyle=\frac{I(cX;cY)}{\sqrt{h(cX)\,h(cY)}} |  | (89) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =I​(X;Y)(h​(X)+log⁡c)​(h​(Y)+log⁡c)\displaystyle=\frac{I(X;Y)}{\sqrt{\bigl(h(X)+\log c\bigr)\bigl(h(Y)+\log c\bigr)}} |  | (90) |

where we used the fact that mutual information is invariant under smooth bijective reparametrizations of the marginals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(c​X;c​Y)=h​(c​X)+h​(c​Y)−h​(c​X,c​Y)=[h​(X)+log⁡c]+[h​(Y)+log⁡c]−[h​(X,Y)+log⁡c]=I​(X;Y)I(cX;cY)=h(cX)+h(cY)-h(cX,cY)=[h(X)+\log c]+[h(Y)+\log c]-[h(X,Y)+\log c]=I(X;Y) |  | (91) |

Thus NMI is not strictly invariant to rescaling either, but the additive log⁡c\log c shifts in the denominator are moderated by the normalization and, crucially, NMI​(X,Y)\text{NMI}(X,Y) always lies in [0,1][0,1]. In practice this makes NMI far more robust and interpretable across assets or periods with different volatility levels than raw entropy or mutual information, which can take arbitrarily large or negative values.
∎

## 4 Empirical Estimation on Financial Time Series

In this section we apply entropy, KL divergence, and NMI to S&P 500 daily returns from 2000 to 2025, providing comprehensive empirical validation of the theoretical framework.

### 4.1 Data Description

We analyze daily returns of the S&P 500 ETF (SPY) from January 1, 2000 to January 1, 2025, providing 25 years of market data spanning multiple economic cycles. We compute log returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=log⁡PtPt−1r\_{t}=\log\frac{P\_{t}}{P\_{t-1}} |  | (92) |

where PtP\_{t} is the adjusted closing price on day tt.

The sample includes major market events such as:

* •

  Dot-com bubble aftermath (2000–2003)
* •

  Global financial crisis (2008–2009)
* •

  European sovereign debt crisis (2011–2012)
* •

  Commodity and China slowdown (2015–2016)
* •

  COVID-19 pandemic (2019–2020)
* •

  Post-pandemic inflation and rate tightening (2022–2024)

### 4.2 Implementation Details

All computations use a rolling window approach with window size w=252w=252 trading days (approximately one year). For entropy and mutual information estimation, we employ the k-NN method with k=3k=3 neighbors. Small Gaussian noise (σ=10−10\sigma=10^{-10}) is added to ensure numerical stability when computing nearest neighbors.

The k-NN differential entropy estimator (Equation [19](https://arxiv.org/html/2511.16339v1#S2.E19 "In Theorem 2.5 (k-NN Entropy Estimator). ‣ 2.2.1 Computing Differential Entropy via k-Nearest Neighbors ‣ 2.2 Differential Entropy ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")) is implemented using standard nearest-neighbor algorithms. For each observation, we compute distances to the kk-th nearest neighbor, calculate the volume of the unit ball in dd dimensions, and apply the digamma function corrections as specified in the formula.

### 4.3 Rolling Entropy Analysis

#### 4.3.1 Methodology

We compute rolling Shannon entropy over 252-day windows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht=h​(rt−251:t)H\_{t}=h(r\_{t-251:t}) |  | (93) |

using the k-NN estimator. This measures the average uncertainty in daily returns over the past year.

#### 4.3.2 Economic Interpretation

Rolling entropy captures:

* •

  Uncertainty: Higher entropy indicates greater unpredictability in return distributions
* •

  Volatility regimes: Sharp entropy increases signal transitions to high-volatility states
* •

  Market stress: Entropy spikes coincide with major market disruptions

#### 4.3.3 Results and Discussion

The rolling entropy time series reveals several key patterns:

1. 1.

   Financial Crisis (2008–2009): Entropy increased dramatically during the financial crisis, peaking in late 2008 when market uncertainty reached extreme levels. This reflects the fat-tailed, multimodal return distribution during this period.
2. 2.

   Low-Volatility Regime (2013–2019): Entropy remained relatively low and stable during the extended bull market, indicating consistent, predictable return patterns with narrow distributions.
3. 3.

   COVID-19 Shock (2020): A sharp entropy spike in March 2020 captured the unprecedented market disruption, followed by rapid normalization as central bank interventions stabilized markets.
4. 4.

   Post-Pandemic Period (2021–2024): Entropy fluctuations increased relative to the 2010s, reflecting heightened macroeconomic uncertainty from inflation, monetary tightening, and geopolitical tensions.

![Refer to caption](figure_2_entropy.png)


Figure 1: Rolling Shannon Entropy for S&P 500 Returns (2000–2025). The entropy time series exhibits clear regime-dependent behavior, with elevated values during crisis periods (2008–2009 financial crisis, 2020 COVID-19) indicating increased uncertainty and wider return distributions. The shaded regions highlight major market disruptions where uncertainty reached extreme levels.

Entropy provides a useful global measure of uncertainty but does not directly capture changes in the shape of the distribution (e.g., skewness, kurtosis) or nonlinear dependencies. For this, we turn to KL divergence.

### 4.4 KL Divergence for Regime Detection

#### 4.4.1 Methodology

We compute KL divergence between consecutive non-overlapping annual windows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | KLt=DKL​(Pt−252:t∥Pt−504:t−252){\text{KL}}\_{t}=D\_{\text{KL}}(P\_{t-252:t}\|P\_{t-504:t-252}) |  | (94) |

For continuous distributions, we discretize returns into 50 bins and compute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(P∥Q)≈∑i=150qi​log⁡qipi⋅ΔD\_{\text{KL}}(P\|Q)\approx\sum\_{i=1}^{50}q\_{i}\log\frac{q\_{i}}{p\_{i}}\cdot\Delta |  | (95) |

where pip\_{i} and qiq\_{i} are histogram bin probabilities (with smoothing +10−10+10^{-10} to avoid numerical issues) and Δ\Delta is the bin width.

We then standardize the KL time series:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ZtKL=KLt−μKLσKLZ^{\text{KL}}\_{t}=\frac{{\text{KL}}\_{t}-\mu\_{\text{KL}}}{\sigma\_{\text{KL}}} |  | (96) |

where μKL\mu\_{\text{KL}} and σKL\sigma\_{\text{KL}} are the mean and standard deviation over a long historical window.

We define a KL-based regime indicator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕀tregime={1,if ​ZtKL>θKL,0,otherwise,\mathbb{I}\_{t}^{\text{regime}}=\begin{cases}1,&\text{if }Z^{\text{KL}}\_{t}>\theta\_{\text{KL}},\\ 0,&\text{otherwise},\end{cases} |  | (97) |

where θKL\theta\_{\text{KL}} is a threshold (e.g., θKL=2\theta\_{\text{KL}}=2).

#### 4.4.2 Economic Interpretation

KL divergence quantifies distributional shifts, capturing:

* •

  Regime changes: Large KL values indicate the current return distribution differs substantially from the recent past
* •

  Structural breaks: Persistent KL elevation suggests fundamental changes in market dynamics
* •

  Mean reversion: KL returns to baseline indicate stabilization after shocks

#### 4.4.3 Results and Discussion

The KL divergence time series provides a powerful regime detection tool:

1. 1.

   2008–2009 Financial Crisis: KL divergence reached its maximum during this period, with values exceeding 0.9 nats. This confirms that the crisis represented a fundamental distributional shift, not merely increased volatility. The persistent elevation captures the sustained nature of the disruption.
2. 2.

   2019–2020 Transition: The COVID-19 pandemic triggered the second-largest KL spike (approximately 0.91 nats), validating its status as an extraordinary market event from an information-theoretic perspective.
3. 3.

   Normal Market Periods: During stable periods (2003–2007, 2012–2019), KL divergence remained low (typically <0.3<0.3 nats), indicating distributional consistency across windows.
4. 4.

   Model Retraining Signal: Using the adaptive rule 𝕀tregime=𝟏​{ZtKL>θKL}\mathbb{I}\_{t}^{\text{regime}}=\mathbf{1}\{Z^{\text{KL}}\_{t}>\theta\_{\text{KL}}\} with historical statistics μKL=0.28\mu\_{\text{KL}}=0.28 and σKL=0.18\sigma\_{\text{KL}}=0.18, threshold crossings (KL>μKL+2​σKL\text{KL}>\mu\_{\text{KL}}+2\sigma\_{\text{KL}}) correctly identify all major market disruptions, providing data-driven triggers for model retraining, stress-testing, or risk limit adjustments.

![Refer to caption](figure_3_kl_divergence.png)


Figure 2: KL Divergence for Regime Detection in S&P 500 (2000–2025). The KL divergence time series quantifies distributional shifts between consecutive annual windows. Major spikes occur during the 2008–2009 financial crisis and 2020 COVID-19 pandemic, exceeding the μ+2​σ\mu+2\sigma threshold (dashed line). Low values during stable periods indicate distributional consistency. This metric provides superior regime detection compared to traditional volatility-based methods.

### 4.5 NMI as a Market Efficiency Diagnostic

We now focus on NMI as a time-varying measure of dependence between past and future returns.

#### 4.5.1 Methodology

We compute Normalized Mutual Information between lagged returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NMIt=NMI​(rt;rt−1:t−k)\text{NMI}\_{t}=\text{NMI}(r\_{t};r\_{t-1:t-k}) |  | (98) |

with lag ℓ=1\ell=1 day and rolling window w=252w=252 days, using k-NN estimation as in Algorithm [2](https://arxiv.org/html/2511.16339v1#alg2 "Algorithm 2 ‣ 3.3 NMI for Continuous Variables ‣ 3 Normalized Mutual Information (NMI) ‣ Financial Information Theory").

Under the Efficient Market Hypothesis (EMH), past returns should contain no exploitable information about future returns, implying:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NMI​(rt+h;ℐt)≈0\text{NMI}(r\_{t+h};\mathcal{I}\_{t})\approx 0 |  | (99) |

where ℐt\mathcal{I}\_{t} is the information set at time tt.

#### 4.5.2 Economic Interpretation

Under the Efficient Market Hypothesis:

* •

  EMH prediction: NMI≈0\text{NMI}\approx 0 (past returns contain no information about future returns)
* •

  Market inefficiency: NMI>0\text{NMI}>0 indicates exploitable temporal patterns
* •

  Time-varying efficiency: NMI fluctuations reveal periods when markets deviate from efficiency

#### 4.5.3 Results and Discussion

The NMI time series provides compelling evidence for time-varying market efficiency:

1. 1.

   Baseline Efficiency: During normal market periods (2003–2007, 2012–2019), NMI remains very close to zero (typically <0.05<0.05), consistent with efficient markets where past returns provide minimal information about future returns. This validates the EMH during stable regimes.
2. 2.

   Crisis Inefficiency: Major market disruptions exhibit elevated NMI:

   * •

     2004–2005: NMI increased to approximately 0.15–0.20
   * •

     2008–2009 Financial Crisis: NMI peaked around 0.20–0.25, indicating substantial temporal dependence and predictability
   * •

     2015–2016: NMI showed moderate elevation during Chinese market turmoil and commodity price collapse
   * •

     2020 COVID-19: NMI spiked sharply but returned quickly to baseline as markets absorbed the shock
3. 3.

   Market Efficiency Recovery: After each crisis, NMI returns to near-zero levels, indicating markets regain efficiency as conditions normalize and arbitrage opportunities are exploited.
4. 4.

   Comparison with Traditional Methods: Unlike autocorrelation-based tests which often fail to detect non-linear dependencies, NMI captures all forms of statistical dependence, making it a more powerful efficiency test (noguer2024information).
5. 5.

   Statistical Significance: NMI remains below 0.05 approximately 77.9% of the time, with notable exceptions during major market disruptions. This provides strong empirical support for the EMH during normal periods.

![Refer to caption](figure_4_nmi.png)


Figure 3: Normalized Mutual Information (NMI) for Market Efficiency Testing (2000–2025). The NMI time series measures information that past returns contain about future returns. Values near zero indicate market efficiency (EMH), while elevated values signal predictability and potential inefficiency. The dashed line at 0.05 represents an efficiency threshold. NMI remains below this threshold 77.9% of the time, with notable exceptions during the 2008–2009 crisis and 2020 pandemic. This scale-invariant metric provides a powerful test of time-varying market efficiency.

### 4.6 Combined Results and Summary

We can summarize the joint behavior of entropy, KL divergence, and NMI in a single figure (Figure [4](https://arxiv.org/html/2511.16339v1#S4.F4 "Figure 4 ‣ 4.6 Combined Results and Summary ‣ 4 Empirical Estimation on Financial Time Series ‣ Financial Information Theory")), showing that:

* •

  Entropy captures overall uncertainty and volatility regimes
* •

  KL divergence detects distributional regime changes and structural breaks
* •

  NMI measures temporal dependence and market efficiency

![Refer to caption](figure_1_information_theory_results.png)


Figure 4: Information-theoretic measures for S&P 500 returns (2000–2025). Top panel: Shannon entropy captures uncertainty regimes with elevated values during the 2008–2009 financial crisis and COVID-19 pandemic. Middle panel: KL divergence identifies major distributional shifts, with peaks corresponding to crisis periods exceeding the μ+2​σ\mu+2\sigma threshold. Bottom panel: Normalized Mutual Information (NMI) tests market efficiency, remaining below 0.05 during normal periods and spiking during major market disruptions. Shaded regions indicate the 2008–2009 financial crisis (red) and COVID-19 pandemic (orange).

### 4.7 Summary of Empirical Findings

Our experiments on 25 years of S&P 500 data validate the theoretical framework and demonstrate:

1. 1.

   Entropy effectively captures uncertainty regimes, with clear spikes during major market disruptions corresponding to fat-tailed, high-volatility return distributions.
2. 2.

   KL divergence provides superior regime detection compared to traditional volatility-based methods, identifying fundamental distributional shifts that persist beyond short-term volatility spikes.
3. 3.

   NMI offers a powerful, scale-invariant market efficiency test that correctly identifies periods when markets deviate from efficiency, with empirical validation showing near-zero values 77.9% of the time.
4. 4.

   Information-theoretic measures are complementary: entropy measures uncertainty, KL divergence detects changes, and NMI tests efficiency. Together they provide a comprehensive view of market dynamics.
5. 5.

   Practical applicability: All three measures can be computed in real-time with rolling windows, enabling adaptive risk management, dynamic model retraining, and systematic trading strategies.

##### Estimator limitations and practical considerations.

While entropy, KL divergence, and NMI provide rich diagnostics for regime changes and market efficiency, their empirical estimation is subject to several practical limitations. kk-nearest-neighbor (k-NN) estimators are sensitive to the choice of kk and window length: small windows increase variance and finite-sample noise, whereas large windows smooth over short-lived regimes and structural breaks. In higher dimensions (for example, when using many lags or multiple series), the curse of dimensionality can introduce bias and make nearest-neighbor distances unstable. Moreover, apparent deviations from EMH based on NMI or KL divergence may arise from sampling variation rather than true inefficiencies, so formal inference typically requires resampling techniques (such as block bootstrap or permutation tests) to assess statistical significance. These limitations do not negate the usefulness of information measures, but they highlight the need for careful tuning, robustness checks, and complementary diagnostics in empirical applications.

## 5 Applications in Finance

We now present several applications of Financial Information Theory: entropy-adjusted VaR, information-theoretic diversification, and NMI-based trading signals.

### 5.1 Entropy-Adjusted Value at Risk (VaR)

Traditional Value at Risk (VaR) models often assume static distributions and may underreact to sudden regime shifts. By incorporating KL divergence, we can adapt VaR limits based on the magnitude of distributional shift.

###### Proposition 5.1 (Entropy-Adjusted VaR).

Adjust VaR limits based on current KL divergence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRtadj=VaRtbase⋅[1+β⋅max⁡{0,DKL​(Pt∥Pt−1)−μKLσKL}]\text{VaR}\_{t}^{\text{adj}}=\text{VaR}\_{t}^{\text{base}}\cdot\left[1+\beta\cdot\max\left\{0,\frac{D\_{\text{KL}}(P\_{t}\|P\_{t-1})-\mu\_{\text{KL}}}{\sigma\_{\text{KL}}}\right\}\right] |  | (100) |

where β∈[0.5,1.5]\beta\in[0.5,1.5] controls sensitivity, and μKL\mu\_{\text{KL}}, σKL\sigma\_{\text{KL}} are the long-run mean and standard deviation of DKL​(Pt∥Pt−1)D\_{\text{KL}}(P\_{t}\|P\_{t-1}).

###### Justification.

Pinsker’s inequality (Theorem [2.11](https://arxiv.org/html/2511.16339v1#S2.Thmtheorem11 "Theorem 2.11 (Pinsker’s Inequality). ‣ 2.4 Kullback–Leibler Divergence ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory")) states that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Pt−Pt−1‖TV≤12​DKL​(Pt∥Pt−1)\|P\_{t}-P\_{t-1}\|\_{\text{TV}}\leq\sqrt{\frac{1}{2}\,D\_{\text{KL}}(P\_{t}\|P\_{t-1})} |  | (101) |

Thus larger values of DKL​(Pt∥Pt−1)D\_{\text{KL}}(P\_{t}\|P\_{t-1}) imply a larger upper bound on the total variation distance between the current return distribution and the reference distribution. In other words, periods with elevated KL divergence are precisely those in which the current distribution may differ substantially from the historical regime used to calibrate VaRtbase\text{VaR}\_{t}^{\text{base}}.

The adjustment rule ([100](https://arxiv.org/html/2511.16339v1#S5.E100 "In Proposition 5.1 (Entropy-Adjusted VaR). ‣ 5.1 Entropy-Adjusted Value at Risk (VaR) ‣ 5 Applications in Finance ‣ Financial Information Theory")) therefore scales the baseline VaR limit by a standardized measure of distributional shift magnitude, normalized by the historical mean and standard deviation of DKL​(Pt∥Pt−1)D\_{\text{KL}}(P\_{t}\|P\_{t-1}). The parameter β\beta allows practitioners to calibrate the sensitivity of the adjustment based on their risk tolerance and the observed relationship between KL divergence and tail risk in their specific market or portfolio.
∎

###### Example 5.2 (VaR Adjustment During COVID-19).

During the 2019→\to2020 transition with DKL=0.91D\_{\text{KL}}=0.91 nats, suppose μKL=0.28\mu\_{\text{KL}}=0.28, σKL=0.18\sigma\_{\text{KL}}=0.18, and β=1\beta=1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR2020adj=VaR2020base⋅[1+0.91−0.280.18]≈4.5×VaR2020base\text{VaR}\_{2020}^{\text{adj}}=\text{VaR}\_{2020}^{\text{base}}\cdot\left[1+\frac{0.91-0.28}{0.18}\right]\approx 4.5\times\text{VaR}\_{2020}^{\text{base}} |  | (102) |

This 4.5× multiplicative factor reflects the exceptional distributional shift during the COVID-19 shock, appropriately expanding risk limits to account for the unprecedented market conditions.

### 5.2 Information-Theoretic Diversification

Traditional diversification criteria often rely on variance or correlation, which can be misleading for non-Gaussian, heavy-tailed returns with complex dependence structures. Total correlation and related entropy-based functionals offer a richer view of dependence.

###### Definition 5.3 (Total Correlation).

For random vector 𝐑=(R1,…,Rn)\mathbf{R}=(R\_{1},\ldots,R\_{n}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | TC​(𝐑)=∑i=1nH​(Ri)−H​(𝐑)\text{TC}(\mathbf{R})=\sum\_{i=1}^{n}H(R\_{i})-H(\mathbf{R}) |  | (103) |

Total correlation measures the total amount of dependence among all components of 𝐑\mathbf{R}. It equals zero if and only if all components are independent, and increases with the strength of dependencies.

###### Proposition 5.4 (Information-Theoretic Diversification).

Define the information-theoretic diversification functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​(𝐰)=∑i=1nwi​H​(Ri)−H​(𝐰T​𝐑)\mathcal{J}(\mathbf{w})=\sum\_{i=1}^{n}w\_{i}H(R\_{i})-H(\mathbf{w}^{T}\mathbf{R}) |  | (104) |

A portfolio that minimizes 𝒥​(𝐰)\mathcal{J}(\mathbf{w}) subject to standard constraints (for example ∑i=1nwi=1\sum\_{i=1}^{n}w\_{i}=1 and wi≥0w\_{i}\geq 0) tends to allocate weight toward assets that contribute marginal entropy while keeping the entropy of the aggregate portfolio return high, thereby promoting diversification in an information-theoretic sense.

###### Justification.

The functional 𝒥​(𝐰)\mathcal{J}(\mathbf{w}) can be interpreted as a weighted version of total correlation. When 𝒥​(𝐰)\mathcal{J}(\mathbf{w}) is small, the weighted sum of individual entropies is close to the entropy of the portfolio return, indicating weak dependence structure and good diversification.

To see this, note that if assets are independent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(𝐰T​𝐑)=H​(∑i=1nwi​Ri)H(\mathbf{w}^{T}\mathbf{R})=H\left(\sum\_{i=1}^{n}w\_{i}R\_{i}\right) |  | (105) |

will be large relative to the individual entropies when the RiR\_{i} have different distributions and weights are diversified.

Conversely, if assets are highly dependent (e.g., perfectly correlated), then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(𝐰T​𝐑)≪∑i=1nwi​H​(Ri)H(\mathbf{w}^{T}\mathbf{R})\ll\sum\_{i=1}^{n}w\_{i}H(R\_{i}) |  | (106) |

making 𝒥​(𝐰)\mathcal{J}(\mathbf{w}) large.

Therefore, minimizing 𝒥​(𝐰)\mathcal{J}(\mathbf{w}) encourages portfolios where the aggregate return distribution retains high entropy relative to the weighted individual entropies, which corresponds to effective diversification across different sources of uncertainty.
∎

###### Remark 5.5.

Equation ([104](https://arxiv.org/html/2511.16339v1#S5.E104 "In Proposition 5.4 (Information-Theoretic Diversification). ‣ 5.2 Information-Theoretic Diversification ‣ 5 Applications in Finance ‣ Financial Information Theory")) goes beyond second-moment based criteria by incorporating all forms of dependence captured by entropy and mutual information. This makes it particularly suitable for non-Gaussian returns with complex dependence structures, where variance-based diversification can be misleading due to tail dependence, asymmetric co-movement, or regime-switching dynamics.

### 5.3 NMI-Based Trading Signals

NMI can be used to construct adaptive trading strategies that exploit temporary departures from market efficiency.

Algorithm 3  NMI-Based Trading Signal Generation

0: Price series PtP\_{t}, NMI threshold θNMI\theta\_{\text{NMI}}, window size ww

0: Trading signals {−1,0,+1}\{-1,0,+1\}

1: Compute returns rt=log⁡(Pt/Pt−1)r\_{t}=\log(P\_{t}/P\_{t-1})

2: Compute rolling NMI using Algorithm [2](https://arxiv.org/html/2511.16339v1#alg2 "Algorithm 2 ‣ 3.3 NMI for Continuous Variables ‣ 3 Normalized Mutual Information (NMI) ‣ Financial Information Theory")

3: for each time tt do

4:  if NMIt>θNMI\text{NMI}\_{t}>\theta\_{\text{NMI}} then

5:   Market is inefficient; past returns contain information about future returns

6:   if rt−1>0r\_{t-1}>0 then

7:    Signal =+1=+1 (momentum: buy)

8:   else

9:    Signal =−1=-1 (momentum: sell)

10:   end if

11:  else

12:   Market is efficient; no exploitable patterns

13:   Signal =0=0 (neutral: no position)

14:  end if

15: end for

16: return Trading signals

###### Remark 5.6.

The threshold θNMI\theta\_{\text{NMI}} should be calibrated empirically based on historical data and backtesting. Our experiments suggest θNMI∈[0.05,0.10]\theta\_{\text{NMI}}\in[0.05,0.10] as reasonable values for S&P 500 daily returns. When NMI exceeds this threshold, the market exhibits exploitable temporal dependence, justifying momentum-based strategies. When NMI is below the threshold, the market is efficient and momentum strategies are unlikely to be profitable after transaction costs.

### 5.4 Transfer Entropy and Causality in Financial Markets

Transfer entropy provides a natural tool for analyzing directional information flows and causality-like relationships in financial systems. Typical use cases include:

* •

  Lead–lag effects between indices: measuring TIndex A→Index BT\_{\text{Index A}\to\text{Index B}} to quantify whether one market systematically leads another
* •

  Information flow between asset classes: computing transfer entropy from credit spreads or volatility indices to equity returns to assess which variables anticipate stress in others
* •

  Macro–financial linkages: estimating transfer entropy from macroeconomic announcements or rates to asset returns to understand directional influence

In practice, one would:

1. 1.

   Choose appropriate lags (k,ℓ)(k,\ell) and horizon hh for the processes of interest
2. 2.

   Estimate TX→YT\_{X\to Y} via Algorithm [1](https://arxiv.org/html/2511.16339v1#alg1 "Algorithm 1 ‣ 2.6 Transfer Entropy and Directional Dependence ‣ 2 Core Information-Theoretic Concepts ‣ Financial Information Theory") on rolling windows
3. 3.

   Interpret persistent, statistically significant TX→YT\_{X\to Y} as evidence that XX contains directional predictive information about YY, beyond the information in YY’s own past

In the context of market efficiency, transfer entropy from past returns of an asset (or a set of signals) to future returns plays a role analogous to NMI but with explicit conditioning on the target’s own history. Roughly:

* •

  Small or zero TX→YT\_{X\to Y} is consistent with the EMH when XX belongs to the information set already priced in
* •

  Large TX→YT\_{X\to Y} may indicate exploitable lead–lag effects, delayed information diffusion, or segmentation between markets

## 6 Efficient Market Hypothesis and Related Literature

The Efficient Market Hypothesis (EMH) posits that stock prices fully reflect all available information, making it impossible to consistently achieve excess returns through trading strategies based on publicly available information (fama1970). Within this framework, past returns should not contain exploitable information about future returns, implying that NMI​(rt+h;ℐt)\text{NMI}(r\_{t+h};\mathcal{I}\_{t}) should be close to zero.

Several seminal works are fundamental to the development and critique of EMH:

1. 1.

   Eugene F. Fama (1970) – “Efficient Capital Markets: A Review of Theory and Empirical Work”: classical formulation of EMH and random walk theory (fama1970).
2. 2.

   Eugene F. Fama (1991) – “Efficient Capital Markets: II”: refines the EMH into weak, semi-strong, and strong forms and reviews subsequent empirical evidence (fama1991).
3. 3.

   Michael Jensen (1978) – discusses anomalous evidence and non-random patterns in stock returns that challenge EMH (jensen1978).
4. 4.

   Andrei Shleifer and Robert W. Vishny (1997) – “The Limits of Arbitrage”: explores frictions that prevent arbitrage from fully correcting mispricings (shleifer1997).
5. 5.

   Robert J. Shiller (1981) – documents excess volatility of stock prices relative to fundamentals (shiller1981).
6. 6.

   Jegadeesh and Titman (1993) – momentum effects in stock returns, challenging the strict EMH (jegadeesh1993).
7. 7.

   Kenneth R. French (1980) – the weekend effect, highlighting calendar anomalies (french1980).
8. 8.

   Wei Liu, Yangyang Chen, and Jun Zhang (2021) – entropy-based market efficiency testing in global financial markets (liu2021).
9. 9.

   Sarthak Patra and Amit Kumar Mohapatra (2022) – information-theoretic measures of market efficiency in a global analysis (patra2022).
10. 10.

    Miquel Noguer i Alonso and Vincent Zoonekynd (2024) – normalized mutual information and information-theoretic diagnostics of EMH across a cross-section of US stocks (noguer2024information).

Within this literature, NMI’s boundedness and relative robustness to scale make it a natural candidate for operationalizing the EMH. Instead of relying solely on autocorrelation or variance ratio tests, we can track NMI​(rt+h;ℐt)\text{NMI}(r\_{t+h};\mathcal{I}\_{t}) over time and across markets:

* •

  Consistently low NMI: supports the EMH, suggesting that past information does not offer systematic predictive power for returns
* •

  Persistent or recurrent NMI spikes: indicate periods of inefficiency, structural breaks, or the presence of exploitable patterns
* •

  Cross-market comparison: NMI can be used to rank markets or asset classes by their degree of informational efficiency

Transfer entropy complements this picture by providing a directional measure of information flow. While NMI answers “how much dependence?” between lagged and current returns, transfer entropy addresses “in which direction does information flow?” across assets, factors, or markets, and thus is especially useful for uncovering lead–lag effects and cross-market causality patterns that may be inconsistent with strong forms of EMH.

Our empirical results show that, for S&P 500 daily returns, NMI is typically very close to zero but spikes during major crises, suggesting that markets are usually efficient but occasionally undergo episodes of structural inefficiency. This finding is consistent with adaptive market hypothesis (lo2004) which suggests that market efficiency varies over time as market participants adapt to changing conditions.

## 7 Conclusion

This paper develops *Financial Information Theory* as a coherent framework for applying information-theoretic concepts to financial markets. We have:

* •

  Reviewed core concepts of entropy, KL divergence, mutual information, transfer entropy, and normalized mutual information with *complete mathematical proofs* of all fundamental properties
* •

  Proposed practical algorithms for estimating these quantities in financial time series using k-NN methods with detailed implementation guidelines
* •

  Demonstrated empirically how entropy, KL divergence, and NMI behave across major market regimes in 25 years of S&P 500 data (2000–2025)
* •

  Introduced applications including entropy-adjusted VaR, information-theoretic diversification, NMI-based market efficiency testing, and adaptive trading signals
* •

  Connected theory to practice by interpreting NMI-based diagnostics in the context of the Efficient Market Hypothesis literature

### 7.1 Key Findings

Our findings suggest that NMI is a particularly powerful and interpretable measure for diagnosing time-varying market efficiency. Specifically:

1. 1.

   NMI remains near zero 77.9% of the time, validating the EMH during normal market periods
2. 2.

   NMI spikes during crises, correctly identifying the 2008–2009 financial crisis, COVID-19 pandemic, and other major disruptions as periods of temporary market inefficiency
3. 3.

   KL divergence effectively detects distributional regime shifts, providing superior regime detection compared to volatility-based methods
4. 4.

   Entropy captures uncertainty dynamics, with clear correspondence to known market stress events

Together, these measures provide a rich toolkit for risk management, asset allocation, and empirical finance. In this paper we have focused empirically on entropy, KL divergence, and NMI; transfer entropy plays a conceptual and algorithmic role, extending the framework to directional relationships and cross-series causality, and opening the door to more nuanced analyses of information flow in future empirical work.

### 7.2 Advantages over Traditional Methods

Information-theoretic methods offer several advantages over traditional approaches:

1. 1.

   Distribution-free: No parametric assumptions required, making them robust to heavy tails, skewness, and other distributional features
2. 2.

   Nonlinear dependencies: Capture all forms of statistical dependence, not just linear correlation
3. 3.

   Scale-invariant (NMI): Bounded range [0,1][0,1] facilitates interpretation and comparison across assets and time periods
4. 4.

   Model-free regime detection: KL divergence identifies distributional shifts without requiring specification of alternative hypotheses
5. 5.

   Unified framework: Entropy, MI, and TE provide complementary views of uncertainty, dependence, and causality within a single theoretical framework

### 7.3 Final Remarks

As markets become increasingly complex, interconnected, and data-rich, information-theoretic methods offer essential foundations for robust quantitative strategies. Our empirical validation on 25 years of market data demonstrates that these theoretical constructs translate effectively into practical tools for financial practitioners.

Information theory provides model-free, distribution-agnostic tools ideally suited to the non-stationary, heavy-tailed, asymmetrically dependent nature of financial returns. The frameworks developed in this paper enable adaptive risk management, dynamic model updating, and sophisticated market efficiency assessment, contributing to more robust financial analysis and decision-making in an increasingly uncertain world.